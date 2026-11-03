# Show prior record(s) in full: python3 showprior.py aops-topic-NNN-qNN [...]
import json,sys
from qbpaths import PRIOR
R={r['id']:r for r in json.load(open(PRIOR))}
for i in sys.argv[1:]:
    r=R.get(i)
    if not r: print('NOT FOUND',i); continue
    print('=====',i,r['src'],r.get('tags')); print('Q:',r['question']); print('S:',r['solution'][:3000]); print('NOTE:',r['note'])
