# Duplicate screen (Jaccard on word/number tokens > threshold) of this batch's rec/*.json against
# (a) all prior releases (ref/prior.json, built from every processed_batches_*/compiled_records.json) and
# (b) the rec/*.json drafts of the OTHER batches of this run (run.json range).
# Usage (in work/bNNN): python3 dup.py [threshold=0.45]
import json,glob,re,os,sys
th=float(sys.argv[1]) if len(sys.argv)>1 else 0.45
me=os.path.basename(os.getcwd())
from qbpaths import PRIOR, FIRST, LAST, work
prior=[(r['id'],r['question']) for r in json.load(open(PRIOR))]
for d in [work(b) for b in range(FIRST,LAST+1)]:
    if os.path.basename(d)==me: continue
    for f in glob.glob(d+'/rec/*.json'):
        for r in json.load(open(f)): prior.append((f"aops-topic-{r['topic_id']}-q{r['part']:02} [{os.path.basename(d)} draft]",r['question']))
def tok(s): return set(re.findall(r'[a-z]+|\d+',s.lower()))
P=[(i,tok(q)) for i,q in prior if q]
Q=dict(prior)
new=[]
for f in sorted(glob.glob('rec/*.json')):
    for r in json.load(open(f)): new.append((f"{r['topic_id']}-q{r['part']:02}",tok(r['question']),r['question']))
hits=[]
for nid,t,q in new:
    if not t: continue
    sc=sorted(((len(t&u)/len(t|u)),i) for i,u in P)[-3:]
    for s,i in reversed(sc):
        if s>th: hits.append((round(s,2),nid,i,q))
print(len(P),'prior questions;',len(new),'new;',len(hits),'hits')
for h in sorted(hits,reverse=True):
    print(f'## {h[0]} {h[1]} ~ {h[2]}'); print('   NEW:',re.sub(r'\s+',' ',h[3])[:300]); print('   OLD:',re.sub(r'\s+',' ',Q[h[2]])[:300])
