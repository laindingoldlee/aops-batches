import json,hashlib,zipfile,os,collections,re,glob,shutil
from alts import ALT
from qbpaths import prefix
from screen import EXCL,PARTIAL
exec(open('assemble.py').read())
SRC=SRC  # rebuilds Z, recs, prov, ALIASES
OUT=f'out/processed_batches_{BATCH:04}_{BATCH:04}'; os.makedirs(OUT,exist_ok=True)
files={}
for r in recs:
    qid=r['id'];m=r['_meta'];src=SRC[r['topic_id']]
    for p in m['diagram_previews']:
        a=ALT[(qid[11:],p['file'][:-4])]
        p['alt']=a[p['index']-1] if isinstance(a,list) else a
    for key in ['question','solution']:
        body=Z[f'questions/{qid}/{key}.tex'].decode()
        tex=f'% Source: {src["url"]}\n% Stable identity: {qid}\n'+body
        # hash check after header
        for i,mm in enumerate(ENV.finditer(tex),1):
            p=[p for p in m['diagram_previews'] if p['file']==key+'.tex' and p['index']==i][0]
            assert p['source_sha256']==hashlib.sha256(mm.group().encode()).hexdigest()
        files[f'questions/{qid}/{key}.tex']=tex.encode()
    for a in m['assets']: files[f'questions/{qid}/{a["path"]}']=Z[f'questions/{qid}/{a["path"]}']
    files[f'questions/{qid}/metadata.json']=(json.dumps(m,ensure_ascii=False,indent=2)+'\n').encode()
manifest=dict(schema_version='1.0',question_ids=[r['id'] for r in recs])
files['manifest.json']=(json.dumps(manifest,indent=2)+'\n').encode()
zp=OUT+'/question_bank_import.zip'
with zipfile.ZipFile(zp,'w',zipfile.ZIP_DEFLATED) as z:
    for k,v in files.items(): z.writestr(k,v)
# verify zip
with zipfile.ZipFile(zp) as z:
    assert z.testzip() is None
    mf=json.loads(z.read('manifest.json')); names=set(z.namelist())
    assert len(mf['question_ids'])==len(set(mf['question_ids']))
    for q in mf['question_ids']:
        md=json.loads(z.read(f'questions/{q}/metadata.json')); assert md['id']==q
        assert z.read(f'questions/{q}/question.tex').strip() and z.read(f'questions/{q}/solution.tex').strip()
        for a in md['assets']: assert f'questions/{q}/{a["path"]}' in names
        for p in md['diagram_previews']:
            tex=z.read(f'questions/{q}/{p["file"]}').decode()
            envs=list(ENV.finditer(tex)); assert hashlib.sha256(envs[p['index']-1].group().encode()).hexdigest()==p['source_sha256']
        nd=sum(len(list(ENV.finditer(z.read(f'questions/{q}/{f}').decode()))) for f in ['question.tex','solution.tex'])
        assert nd==len(md['diagram_previews'])
# screening
byt=collections.defaultdict(list)
for r in recs: byt[r['topic_id']].append(r['id'])
screen=[]
for tid,t in SRC.items():
    qids=byt.get(tid,[])
    al=[a for a in ALIASES if a.split('-')[2]==tid]
    if qids: st='partial' if tid in PARTIAL else 'included'; reason=PARTIAL.get(tid,'Mathematical material prepared with full solutions; adaptations recorded in provenance.')
    elif al: st='duplicate'; reason='Known duplicate of a record in a prior release; canonical ID recorded.'
    else: st='excluded'; reason=EXCL[tid]
    screen.append(dict(topic_id=tid,title=t['title'],url=t['url'],status=st,reason=reason,question_ids=qids+[ALIASES[a] for a in al],records=len(qids)))
json.dump(screen,open(OUT+'/screening_log.json','w'),ensure_ascii=False,indent=2)
json.dump(prov,open(OUT+'/provenance.json','w'),ensure_ascii=False,indent=2)
json.dump([dict(alias=a,canonical=c,canonical_in_this_zip=(c in {r['id'] for r in recs}),source_url=SRC[a.split('-')[2]]['url']) for a,c in ALIASES.items()],open(OUT+'/duplicate_aliases.json','w'),indent=2)
compiled=[{k:v for k,v in r.items() if k!='_meta'} for r in recs]
json.dump(compiled,open(OUT+'/compiled_records.json','w'),ensure_ascii=False,indent=1)
reg2=dict(identity_version=reg['identity_version'],rule=reg['rule'],aliases={**reg['aliases'],**ALIASES},records=reg['records']+[dict(id=r['id'],topic_id=r['topic_id'],part=r['part']) for r in recs])
json.dump(reg2,open(OUT+'/deduplication_registry.json','w'),ensure_ascii=False,indent=1)
stat=collections.Counter(s['status'] for s in screen)
summary=dict(question_records=len(recs),topics_screened=len(screen),screening_statuses=stat,diagram_previews=npreview,missing_diagram_previews=0,diagram_previews_compiled=True,zip_members=len(files),zip_sha256=hashlib.sha256(open(zp,'rb').read()).hexdigest(),checks_passed=True)
json.dump(summary,open(OUT+'/validation_summary.json','w'),indent=2)
print(json.dumps(summary,indent=1))
os.makedirs(OUT+'/review_logs/builders',exist_ok=True)
for f in sorted(glob.glob(prefix(BATCH)+'[0-9][0-9].py'))+sorted(glob.glob('chk_'+prefix(BATCH)+'*.py'))+['qb.py','compile.py','assemble.py','finalize.py','alts.py','screen.py','chk.py','aliases.json','sheet.py','dup.py','pdfcheck.py','precheck.py','findprior.py','showprior.py','figsheets.py','qbpaths.py']: shutil.copy(f,OUT+'/review_logs/builders/')
