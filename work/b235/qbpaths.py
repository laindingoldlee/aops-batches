# Central paths for the question-bank pipeline (repo layout). Every tool imports this.
#   <root>/run.json            {"first": 221, "last": 230}  -- the batch range of the current run
#   <root>/ref/                spec.md, prior.json (all earlier records), base_registry.json (registry through first-1)
#   <root>/source/             batch_NNNN.json source files
#   <root>/work/bNNN/          one working folder per batch (tools copied in by setup_run.py)
#   <root>/output/             final merged package processed_batches_FFFF_LLLL
import os, json
def _find_root():
    if os.environ.get('QB_ROOT'): return os.path.abspath(os.environ['QB_ROOT'])
    for start in (os.getcwd(), os.path.dirname(os.path.abspath(__file__))):
        d = start
        while True:
            if os.path.exists(os.path.join(d, 'run.json')) and os.path.isdir(os.path.join(d, 'ref')): return d
            p = os.path.dirname(d)
            if p == d: break
            d = p
    raise SystemExit('qbpaths: cannot find the repo root (folder with run.json and ref/); set QB_ROOT')
ROOT = _find_root()
REF = ROOT + '/ref'
SPEC = REF + '/spec.md'
PRIOR = REF + '/prior.json'
BASE_REGISTRY = REF + '/base_registry.json'
SRCDIR = ROOT + '/source'
WORK = ROOT + '/work'
OUTPUT = ROOT + '/output'
RUN = json.load(open(ROOT + '/run.json'))
FIRST, LAST = int(RUN['first']), int(RUN['last'])
def src_path(b): return f'{SRCDIR}/batch_{b:04}.json'
def work(b): return f'{WORK}/b{b}'
def prefix(b): return f'p{b}_'   # builders p221_01.py ..., checks chk_p221_01.py ...
def batch_out(b): return f'{work(b)}/out/processed_batches_{b:04}_{b:04}'
