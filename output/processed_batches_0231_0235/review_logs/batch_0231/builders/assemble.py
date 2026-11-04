import json,glob,re,hashlib,zipfile,os,shutil,collections,sys
from qb import TAGS, fracnorm
from compile import compile_env
from screen import EXCL,PARTIAL
BATCH=int(sys.argv[1]) if len(sys.argv)>1 else int(os.path.basename(os.getcwd())[1:])
ENV=re.compile(r'\\begin\{(asy|tikzpicture)\}[\s\S]*?\\end\{\1\}')
from qbpaths import src_path, batch_out, FIRST, BASE_REGISTRY, SPEC
SRC={t['topic_id']:t for t in json.load(open(src_path(BATCH)))['topics']}
recs=[r for f in sorted(glob.glob('rec/*.json')) for r in json.load(open(f))]
ALIASES=json.load(open('aliases.json')) if os.path.exists('aliases.json') else {}
for r in recs: r['id']=f"aops-topic-{r['topic_id']}-q{r['part']:02}"
recs=[r for r in recs if r['id'] not in ALIASES]
ids=[r['id'] for r in recs]; assert len(ids)==len(set(ids))
REGPATH=batch_out(BATCH-1)+'/deduplication_registry.json'
if BATCH==FIRST or (not os.path.exists(REGPATH) and os.environ.get('QB_FINAL')!='1'):
    REGPATH=BASE_REGISTRY  # registry cumulative through batch FIRST-1 (also pre-check mode before the chain exists)
print('registry:',REGPATH)
reg=json.load(open(REGPATH))
prior_ids={x['id'] for x in reg['records']}
assert not set(ids)&prior_ids
order={t:i for i,t in enumerate(SRC)}
recs.sort(key=lambda r:(order[r['topic_id']],r['part']))
Z={}; issues=[]; prov=[]; npreview=0
def check(qid,key,tex):
    plain=ENV.sub('',tex); lvl=0
    for m in re.finditer(r'(?<!\\)[{}]',plain):
        lvl+=1 if m.group()=='{' else -1
        assert lvl>=0,(qid,key,'brace')
    assert lvl==0,(qid,key,'brace')
    assert len(re.findall(r'(?<!\\)\$',plain))%2==0,(qid,key,'dollar')
    assert not re.search(r'\\(?:frac|tfrac|cfrac|over)(?![a-zA-Z])',tex),(qid,key,'frac')
    assert fracnorm(tex)==tex,(qid,key,'unbraced dfrac argument')
    assert not re.search(r'(?<!\\)%',plain),(qid,key,'percent')
    assert not re.search(r'[^\x00-\x7f]',tex),(qid,key,'nonascii',re.findall(r'[^\x00-\x7f]',tex))
    for m in re.finditer(r'.{0,20}/.{0,20}',plain): issues.append((qid,key,m.group()))
    assert '\\documentclass' not in tex and 'tikzpicture' not in tex
P=open(SPEC).read()
GEO=set(re.findall(r'^- (.+)$',P[P.index('### Geometry'):P.index('### Combinatorics')],re.M))
for r in recs:
    qid=r['id']
    assert all(t in TAGS for t in r['tags']) and len(r['tags'])==len(set(r['tags']))
    assert isinstance(r['difficulty'],int) and 1<=r['difficulty']<=10
    if set(r['tags'])&GEO and 'begin{asy}' not in r['solution']: issues.append((qid,'GEOMETRY WITHOUT SKETCH',set(r['tags'])&GEO))
    assets=[];previews=[];pk=['amsmath','amssymb']
    for key in ['question','solution']:
        tex=r[key].replace('\r\n','\n').replace('\r','\n').strip()+'\n'
        check(qid,key,tex)
        for i,m in enumerate(ENV.finditer(tex),1):
            name=f'assets/{qid}-{key}-diagram-{i:02}.svg'
            path=f'/tmp/qbprev{BATCH}/{name}'; os.makedirs(os.path.dirname(path),exist_ok=True)
            ok,err=compile_env(m.group(),path); assert ok,(qid,err)
            Z[f'questions/{qid}/{name}']=open(path,'rb').read(); npreview+=1
            assets.append(dict(path=name,type='image',usage=f'Website preview generated from diagram {i} in {key}.tex; editable source remains inline in {key}.tex.'))
            previews.append(dict(file=f'{key}.tex',index=i,path=name,source_sha256=hashlib.sha256(m.group().encode()).hexdigest(),alt=''))
        Z[f'questions/{qid}/{key}.tex']=tex.encode()
    if assets: pk.append('asymptote')
    r['_meta']=dict(id=qid,source=r['source'],tags=r['tags'],difficulty=r['difficulty'],difficulty_rationale=r['rationale'],question_file='question.tex',solution_file='solution.tex',
      latex_dependencies=dict(packages=[dict(name=p,options=[]) for p in pk],tikz_libraries=[],preamble_commands=[]),assets=assets,diagram_previews=previews)
    src=SRC[r['topic_id']]
    prov.append(dict(id=qid,topic_id=r['topic_id'],part=r['part'],url=src['url'],title=src['title'],editorial_note=r.get('note','')))
json.dump(recs,open(f'/tmp/recs_final{BATCH}.json','w'))
print(len(recs),'records',npreview,'previews')
print('review:');[print(' ',x) for x in issues]
