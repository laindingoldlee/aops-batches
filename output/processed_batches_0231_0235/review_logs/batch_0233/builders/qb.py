import json,re,difflib
# Brace every \dfrac argument exactly as TeX reads it: \dfrac12 -> \dfrac{1}{2}, \dfrac d2 -> \dfrac{d}{2},
# \dfrac\pi4 -> \dfrac{\pi}{4}. Braced arguments are kept (and normalised recursively). Pure notation change.
def _match(s, m):
    lvl = 0; k = m
    while k < len(s):
        c = s[k]
        if c == '\\': k += 2; continue
        if c == '{': lvl += 1
        elif c == '}':
            lvl -= 1
            if lvl == 0: return k
        k += 1
    raise ValueError('unbalanced brace in \\dfrac argument: ' + s[m:m+40])
def fracnorm(s):
    out = []; i = 0
    while True:
        j = s.find('\\dfrac', i)
        if j < 0: out.append(s[i:]); return ''.join(out)
        k = j + 6
        if k < len(s) and s[k].isalpha():          # some other control word starting with \dfrac
            out.append(s[i:k]); i = k; continue
        out.append(s[i:k])
        for _ in range(2):
            m = k
            while m < len(s) and s[m] in ' \t\n': m += 1
            assert m < len(s), 'missing \\dfrac argument'
            out.append(s[k:m]); c = s[m]
            if c == '{':
                e = _match(s, m); out.append('{' + fracnorm(s[m+1:e]) + '}'); k = e + 1
            elif c == '\\':
                e = m + 1
                if e < len(s) and s[e].isalpha():
                    while e < len(s) and s[e].isalpha(): e += 1
                else: e += 1
                out.append('{' + s[m:e] + '}'); k = e
            else:
                assert c not in '}$%#&^_', ('bad \\dfrac argument', s[j:j+30])
                out.append('{' + c + '}'); k = m + 1
        i = k

from qbpaths import SPEC
PROMPT=open(SPEC,encoding='utf-8').read()
TAGS=set(re.findall(r'^- (.+)$',PROMPT[PROMPT.index('### Arithmetic and numerical reasoning'):PROMPT.index('### Tagging examples')],re.M))
RUBRIC={1:'Immediate application of a definition or basic fact.',2:'A routine procedure with a little reasoning.',3:'One accessible observation or a short chain of familiar deductions.',4:'An unstated approach requiring some exploration and a few connected steps.',5:'A meaningful insight or a moderately demanding combination of familiar ideas.',6:'A difficult-to-spot insight followed by substantial reasoning.',7:'A challenging problem requiring sustained strategic reasoning.'}
def src(comp=None,year=None,div=None,qn=None,paper=None,rnd=None):
    return dict(competition=comp,year=year,division=div,paper=paper,round=rnd,question_number=None if qn is None else str(qn))
NOSRC=src()
class Bank:
    def __init__(self,name):
        self.name=name;self.records=[]
    def add(self,tid,part,q,s,tags,d,rat=None,source=NOSRC,note=''):
        tags=[t.strip() for t in tags.split('|')] if isinstance(tags,str) else tags
        assert rat is None or isinstance(rat,str),(tid,part,"rationale must be a string; pass the source as source=src(...)")
        assert isinstance(source,dict),(tid,part)
        bad=[t for t in tags if t not in TAGS]
        assert not bad,(tid,part,'TAGS NOT IN VOCABULARY:',bad,'closest valid tags:',[difflib.get_close_matches(t,TAGS,4,0.4) for t in bad])
        self.records.append(dict(topic_id=str(tid),part=int(part),question=fracnorm(q.strip()),solution=fracnorm(s.strip()),tags=list(dict.fromkeys(tags)),difficulty=d,rationale=rat or RUBRIC[d],source=source,note=note))
    def save(self):
        json.dump(self.records,open(f'rec/{self.name}.json','w'),ensure_ascii=False,indent=1)
        print(self.name,len(self.records))
RESET='label("\\mbox{}",(min(currentpicture,user=true)+max(currentpicture,user=true))/2,black); // keeps the text after the figure black when LaTeX typesets the labels inline'
def asy(body,size='6cm'):
    return '\n\\begin{asy}\nusepackage("amsmath");\nsize(%s);\ndefaultpen(fontsize(10pt));\n%s\n%s\n\\end{asy}\n'%(size,body.strip(),RESET)
