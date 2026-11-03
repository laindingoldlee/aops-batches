# Start a run: python3 tools/setup_run.py FIRST LAST
# Writes run.json and creates work/bNNN for each batch with the tools copied in, an empty rec/, aliases.json = {},
# and a chk.py. Existing work folders are left alone (so an interrupted run can resume).
import sys, os, json, shutil, glob
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
first, last = int(sys.argv[1]), int(sys.argv[2])
reg = json.load(open(ROOT + '/ref/base_registry.json'))
covered = json.load(open(ROOT + '/ref/progress.json'))['registry_through'] if os.path.exists(ROOT + '/ref/progress.json') else None
if covered is not None and first != covered + 1:
    raise SystemExit(f'ref/ registry covers batches through {covered}; the next run must start at {covered + 1}, not {first}')
for b in range(first, last + 1):
    if not os.path.exists(f'{ROOT}/source/batch_{b:04}.json'): raise SystemExit(f'missing source/batch_{b:04}.json')
json.dump({'first': first, 'last': last}, open(ROOT + '/run.json', 'w'))
TOOLS = ['qbpaths.py', 'qb.py', 'compile.py', 'sheet.py', 'figsheets.py', 'dup.py', 'findprior.py', 'showprior.py',
         'assemble.py', 'finalize.py', 'precheck.py', 'pdfcheck.py', 'chk.py']
for b in range(first, last + 1):
    d = f'{ROOT}/work/b{b}'
    new = not os.path.exists(d)
    os.makedirs(d + '/rec', exist_ok=True)
    for t in TOOLS: shutil.copy(f'{ROOT}/tools/{t}', d + '/' + t)   # tools are refreshed, your files are untouched
    if not os.path.exists(d + '/aliases.json'): open(d + '/aliases.json', 'w').write('{}\n')
    print(('created ' if new else 'refreshed tools in ') + d)
print(f'run.json = {first}-{last}; prior records: {len(json.load(open(ROOT + "/ref/prior.json")))}; registry records: {len(reg["records"])}')
