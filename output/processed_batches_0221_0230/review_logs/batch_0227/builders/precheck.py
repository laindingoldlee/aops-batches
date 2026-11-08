# Pre-finalisation consistency checks for one batch (run in work/bNNN: python3 precheck.py NNN)
# - every topic is accounted for (records, aliases or an EXCL reason), PARTIAL only on topics with records
# - aliases point to IDs that exist (prior registry or this batch's exported records)
# - every diagram in an exported record has alt text in alts.py (ALT[(<topic>-qNN, 'question'|'solution')])
# - no topic ID of this batch already appears in the prior registry
import json, glob, re, os, sys, collections
BATCH = int(sys.argv[1]) if len(sys.argv) > 1 else int(os.path.basename(os.getcwd())[1:])
ENV = re.compile(r'\\begin\{(asy|tikzpicture)\}[\s\S]*?\\end\{\1\}')
from qbpaths import src_path, BASE_REGISTRY, FIRST, work
SRC = {t['topic_id']: t for t in json.load(open(src_path(BATCH)))['topics']}
from screen import EXCL, PARTIAL, NONMATH
from alts import ALT
ALIASES = json.load(open('aliases.json')) if os.path.exists('aliases.json') else {}
reg = json.load(open(BASE_REGISTRY))
prior = {x['id'] for x in reg['records']}
prior_topics = {x['topic_id'] for x in reg['records']} | {a.split('-')[2] for a in reg['aliases']}
recs = [r for f in sorted(glob.glob('rec/*.json')) for r in json.load(open(f))]
problems = []
ids = [f"aops-topic-{r['topic_id']}-q{r['part']:02}" for r in recs]
dupids = [k for k, v in collections.Counter(ids).items() if v > 1]
if dupids: problems.append(('duplicate record ids', dupids))
for r in recs:
    if r['topic_id'] not in SRC: problems.append(('record topic not in batch', r['topic_id']))
exported = {i for i in ids if i not in ALIASES}
# records exported by the other batches of this run (run.json range), for cross-batch aliases to an earlier batch
others = set()
for ob in range(FIRST, BATCH):
    oal = json.load(open(f'{work(ob)}/aliases.json')) if os.path.exists(f'{work(ob)}/aliases.json') else {}
    for f in glob.glob(f'{work(ob)}/rec/*.json'):
        for r in json.load(open(f)):
            i = f"aops-topic-{r['topic_id']}-q{r['part']:02}"
            if i not in oal: others.add(i)
for a, c in ALIASES.items():
    if a not in ids and a.split('-')[2] not in SRC: problems.append(('alias topic not in batch', a))
    if c not in prior and c not in exported and c not in others: problems.append(('alias canonical unknown', a, c))
    if a in prior: problems.append(('alias id already in registry', a))
bytopic = collections.defaultdict(list)
for i in exported: bytopic[i.split('-')[2]].append(i)
aliased_topics = {a.split('-')[2] for a in ALIASES}
for tid in SRC:
    has = bool(bytopic.get(tid)); al = tid in aliased_topics
    if not has and not al and tid not in EXCL: problems.append(('topic not accounted for', tid, SRC[tid]['title']))
    if has and tid in EXCL: problems.append(('topic has records but is in EXCL', tid))
    if tid in PARTIAL and not has: problems.append(('PARTIAL topic without records', tid))
    if tid in prior_topics: problems.append(('topic id already in prior registry (check: re-scrape/duplicate?)', tid))
for t in list(EXCL) + list(PARTIAL):
    if t not in SRC: problems.append(('screen.py topic not in batch', t))
for r in recs:
    rid = f"aops-topic-{r['topic_id']}-q{r['part']:02}"
    if rid in ALIASES: continue
    for key in ('question', 'solution'):
        n = len(list(ENV.finditer(r[key])))
        if not n: continue
        k = (rid[11:], key)
        if k not in ALT: problems.append(('missing alt', k)); continue
        a = ALT[k]
        if n > 1 and not (isinstance(a, list) and len(a) == n): problems.append(('alt list length', k, n))
        if n == 1 and isinstance(a, list) and len(a) != 1: problems.append(('alt list length', k, n))
st = collections.Counter()
for tid in SRC:
    if bytopic.get(tid): st['partial' if tid in PARTIAL else 'included'] += 1
    elif tid in aliased_topics: st['duplicate'] += 1
    else: st['excluded'] += 1
nonmath = sum(1 for t, v in EXCL.items() if v == NONMATH and not bytopic.get(t) and t not in aliased_topics)
print('records exported:', len(exported), ' aliases:', len(ALIASES), ' statuses:', dict(st), ' non-math excluded:', nonmath)
print('diagrams:', sum(len(list(ENV.finditer(r[k]))) for r in recs if f"aops-topic-{r['topic_id']}-q{r['part']:02}" not in ALIASES for k in ('question', 'solution')))
for p in problems: print('PROBLEM', p)
print('PRECHECK OK' if not problems else f'{len(problems)} PROBLEMS')
