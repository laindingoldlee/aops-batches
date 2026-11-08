# Compile every question and solution body in rec/*.json (aliases excluded) into one PDF.
# Usage: python3 pdfcheck.py [records.json ...]   (default: rec/*.json in the cwd)
# pdflatex -> asy -render=0 on the generated .asy files -> pdflatex; reports any LaTeX/asy errors.
import json, glob, os, sys, subprocess, re, shutil
files = sys.argv[1:] or sorted(glob.glob('rec/*.json'))
ALIASES = json.load(open('aliases.json')) if os.path.exists('aliases.json') else {}
recs = []
for f in files:
    d = json.load(open(f)); d = d['records'] if isinstance(d, dict) else d
    for r in d:
        rid = r.get('id') or f"aops-topic-{r['topic_id']}-q{int(r['part']):02}"
        if rid in ALIASES: continue
        recs.append((rid, r['question'], r['solution']))
W = os.path.abspath('pdfcheck'); shutil.rmtree(W, ignore_errors=True); os.makedirs(W)
doc = [r'\documentclass{article}', r'\usepackage[margin=2cm]{geometry}', r'\usepackage{amsmath,amssymb,enumitem}',
       r'\usepackage[inline]{asymptote}', r'\begin{document}']
for rid, q, s in recs:
    doc += [r'\section*{' + rid.replace('_', r'\_') + '}', r'\subsection*{Question}', q, '', r'\subsection*{Solution}', s, r'\clearpage']
doc.append(r'\end{document}')
open(W + '/all.tex', 'w').write('\n'.join(doc) + '\n')
def latex():
    return subprocess.run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error', 'all.tex'], cwd=W, capture_output=True, text=True, timeout=900)
r = latex()
asys = sorted(glob.glob(W + '/all-*.asy'))
bad = []
for a in asys:
    p = subprocess.run(['asy', '-render=0', os.path.basename(a)], cwd=W, capture_output=True, text=True, timeout=300)
    if p.returncode != 0: bad.append((a, p.stderr[-600:]))
r = latex(); r = latex()
log = open(W + '/all.log', errors='replace').read()
errs = [m.group(0) for m in re.finditer(r'^! .*(?:\n.*){0,3}', log, re.M)]
undefined = re.findall(r'(?:Undefined control sequence|Missing \$ inserted|Runaway argument).*', log)
pages = re.search(r'Output written on all.pdf \((\d+) pages?', log)
print(f'records={len(recs)} asy_files={len(asys)} asy_failures={len(bad)} pages={pages.group(1) if pages else None}')
for a, e in bad: print('ASY FAIL', a, e)
for e in errs[:20]: print('LATEX ERROR', e)
warn = re.findall(r'^(?:LaTeX|Package) .*Warning.*$', log, re.M)
print('warnings:', len(warn)); [print('  ', w) for w in warn[:10]]
# inline-label colour leak: in each figure's inline label file the last fill-colour special must be black
leak = []
for t in sorted(glob.glob(W + '/all-*.tex')):
    sp = re.findall(r'\\special\{pdf:([0-9. ]+) (rg|g)\}', open(t).read())
    if sp and not all(float(x) == 0 for x in sp[-1][0].split()): leak.append(os.path.basename(t))
print('figures whose last label colour is not black:', len(leak), leak[:10])
print('OK' if (not bad and not errs and pages and not leak) else 'PROBLEMS')
