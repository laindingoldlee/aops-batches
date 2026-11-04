# Render figures for visual review.
#   python3 figsheets.py            -> every figure of non-aliased records in rec/*.json, 640 px wide, 4 per sheet:
#                                      figs/sheet_NN.png + figs/index.txt (which record/body/figure is in each panel)
#   python3 figsheets.py ID [ID..]  -> only those records (ID = aops-topic-NNN-qKK or NNN-qKK) -> figs/only_NN.png
# Read every sheet with the Read tool.
import json, glob, os, sys, re, io, shutil
import cairosvg
from PIL import Image, ImageDraw
from compile import compile_env
ENV = re.compile(r'\\begin\{(asy|tikzpicture)\}[\s\S]*?\\end\{\1\}')
ALIASES = json.load(open('aliases.json')) if os.path.exists('aliases.json') else {}
want = {a if a.startswith('aops-topic-') else 'aops-topic-' + a for a in sys.argv[1:]}
items = []
for f in sorted(glob.glob('rec/*.json')):
    for r in json.load(open(f)):
        rid = f"aops-topic-{r['topic_id']}-q{r['part']:02}"
        if rid in ALIASES or (want and rid not in want): continue
        for key in ('question', 'solution'):
            for i, m in enumerate(ENV.finditer(r[key]), 1):
                items.append((rid, key, i, m.group(), r['question']))
os.makedirs('figs', exist_ok=True)
tag = 'only' if want else 'sheet'
for old in glob.glob(f'figs/{tag}_*.png'): os.remove(old)
os.makedirs('/tmp/figsvg', exist_ok=True)
panels = []
for rid, key, i, env, q in items:
    out = f'/tmp/figsvg/{os.path.basename(os.getcwd())}-{rid[11:]}-{key}-{i}.svg'
    ok, err = compile_env(env, out)
    if not ok:
        print('FAIL', rid, key, i, err); im = Image.new('RGB', (640, 200), 'white'); ImageDraw.Draw(im).text((10, 10), 'COMPILE FAIL', fill='red')
    else:
        im = Image.open(io.BytesIO(cairosvg.svg2png(url=out, output_width=640, background_color='white'))).convert('RGB')
        if im.height > 900: im.thumbnail((640, 900))
    panels.append((f'{rid} {key} fig{i}', im, q))
W, PH = 680, 960
idx = []
for s in range(0, len(panels), 4):
    grp = panels[s:s + 4]
    sheet = Image.new('RGB', (2 * W, 2 * PH), 'white'); d = ImageDraw.Draw(sheet)
    n = s // 4 + 1
    for k, (lab, im, q) in enumerate(grp):
        x, y = (k % 2) * W, (k // 2) * PH
        d.text((x + 10, y + 8), f'[{k + 1}] {lab}', fill='red')
        sheet.paste(im, (x + 20, y + 30)); d.rectangle([x, y, x + W - 1, y + PH - 1], outline='#bbbbbb')
        idx.append(f'{tag}_{n:02} [{k + 1}] {lab} :: ' + re.sub(r'\s+', ' ', q)[:300])
    h = max(30 + im.height for _, im, _ in grp[:2]) + 10
    if len(grp) > 2: h = PH + max(30 + im.height for _, im, _ in grp[2:]) + 10
    sheet.crop((0, 0, 2 * W, min(h, 2 * PH))).save(f'figs/{tag}_{n:02}.png')
open(f'figs/index{"_only" if want else ""}.txt', 'w').write('\n'.join(idx) + '\n')
print(len(panels), 'figures on', (len(panels) + 3) // 4, 'sheets in figs/')
