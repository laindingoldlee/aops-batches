# Keyword search over all prior records (questions, optionally notes/solutions).
# Usage: python3 findprior.py 'regex1' ['regex2' ...]   -- all regexes must match (case-insensitive) the question text
#        add --all to also search solution and note text; --n=K to show up to K hits (default 15)
import json,re,sys
args=[a for a in sys.argv[1:] if not a.startswith('--')]
full='--all' in sys.argv
n=next((int(a[4:]) for a in sys.argv if a.startswith('--n=')),15)
from qbpaths import PRIOR
R=json.load(open(PRIOR))
hits=[r for r in R if all(re.search(a,(r['question']+(' '+r['solution']+' '+r['note'] if full else '')),re.I|re.S) for a in args)]
print(len(hits),'hits')
for r in hits[:n]: print('##',r['id'],f"({r['src']})",'|',re.sub(r'\s+',' ',r['question'])[:350])
