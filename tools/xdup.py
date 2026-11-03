# Cross-batch near-duplicate scan of all drafts in this run (Jaccard > 0.35 between different batches)
import json,glob,re,os,sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from qbpaths import FIRST, LAST, work
def tok(s): return set(re.findall(r'[a-z]+|\d+',s.lower()))
R=[]
for b in range(FIRST,LAST+1):
    al=json.load(open(f'{work(b)}/aliases.json')) if os.path.exists(f'{work(b)}/aliases.json') else {}
    for f in sorted(glob.glob(f'{work(b)}/rec/*.json')):
        for r in json.load(open(f)):
            i=f"aops-topic-{r['topic_id']}-q{r['part']:02}"
            if i in al: continue
            R.append((b,i,tok(r['question']),r['question']))
out=[]
for x in range(len(R)):
    for y in range(x+1,len(R)):
        a,b=R[x],R[y]
        if a[0]==b[0]: continue
        j=len(a[2]&b[2])/len(a[2]|b[2])
        if j>0.35: out.append((round(j,2),a,b))
for j,a,b in sorted(out,key=lambda t:-t[0]):
    print('##',j,a[0],a[1],'|',b[0],b[1]); print('  A:',re.sub(r'\s+',' ',a[3])[:250]); print('  B:',re.sub(r'\s+',' ',b[3])[:250])
print(len(R),'records',len(out),'pairs')
