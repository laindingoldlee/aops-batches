import json, zipfile, hashlib, os, shutil, re, collections, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from qbpaths import FIRST, LAST, OUTPUT, BASE_REGISTRY, work, batch_out
from qb import TAGS

B = list(range(FIRST, LAST + 1))
NAME = f'processed_batches_{FIRST:04}_{LAST:04}'
OUT = f'{OUTPUT}/{NAME}'
shutil.rmtree(OUT, ignore_errors=True); os.makedirs(OUT)
src = {b: batch_out(b) for b in B}
ENV = re.compile(r'\\begin\{(asy|tikzpicture)\}[\s\S]*?\\end\{\1\}')

ids, members, batch_of = [], {}, {}
compiled, prov, screen, aliases = [], [], [], []
per_batch = {}
for b in B:
    d = src[b]
    with zipfile.ZipFile(d + '/question_bank_import.zip') as z:
        assert z.testzip() is None
        mf = json.loads(z.read('manifest.json')); assert mf['schema_version'] == '1.0'
        for q in mf['question_ids']:
            assert q not in batch_of, ('duplicate id across batches', q)
            batch_of[q] = b; ids.append(q)
        for n in z.namelist():
            if n == 'manifest.json': continue
            assert n.startswith('questions/') and n not in members, n
            assert n.split('/')[1] in mf['question_ids'], n
            members[n] = z.read(n)
    c = json.load(open(d + '/compiled_records.json')); assert [r['id'] for r in c] == mf['question_ids']
    compiled += c
    p = json.load(open(d + '/provenance.json')); assert {r['id'] for r in p} == set(mf['question_ids'])
    prov += p
    s = json.load(open(d + '/screening_log.json')); assert len(s) == 100
    screen += [dict(batch=b, **e) for e in s]
    a = json.load(open(d + '/duplicate_aliases.json'))
    aliases += [dict(batch=b, **e) for e in a]
    v = json.load(open(d + '/validation_summary.json')); assert v['checks_passed'] and v['missing_diagram_previews'] == 0
    per_batch[b] = dict(question_records=v['question_records'], aliases=len(a), diagram_previews=v['diagram_previews'],
                        screening_statuses=dict(v['screening_statuses']))

idset = set(ids)
assert len(ids) == len(idset)
# canonical locations of aliases, relative to the merged package
for e in aliases:
    e['canonical_in_this_zip'] = e['canonical'] in idset
    if e['canonical_in_this_zip']: e['canonical_batch'] = batch_of[e['canonical']]
    assert e['alias'] not in idset

# registry: the last batch's registry is cumulative (built on ref/base_registry.json); check it covers everything here
reg = json.load(open(src[LAST] + '/deduplication_registry.json'))
reg_ids = {r['id'] for r in reg['records']}
base = json.load(open(BASE_REGISTRY))
assert {r['id'] for r in base['records']} <= reg_ids and all(reg['aliases'].get(k) == v for k, v in base['aliases'].items())
assert len(reg['records']) == len(base['records']) + len(ids), (len(reg['records']), len(base['records']), len(ids))
assert idset <= reg_ids, len(idset - reg_ids)
assert all(reg['aliases'].get(e['alias']) == e['canonical'] for e in aliases)

# ---- write the merged ZIP (manifest first, then folders in manifest order)
manifest = dict(schema_version='1.0', question_ids=ids)
zp = OUT + '/question_bank_import.zip'
order = sorted(members, key=lambda n: (ids.index(n.split('/')[1]), n))
with zipfile.ZipFile(zp, 'w', zipfile.ZIP_DEFLATED) as z:
    z.writestr('manifest.json', json.dumps(manifest, indent=2) + '\n')
    for n in order: z.writestr(n, members[n])

# ---- independent validation of the merged ZIP
def body_checks(q, key, tex):
    body = '\n'.join(l for l in tex.splitlines() if not l.startswith('% Source:') and not l.startswith('% Stable identity:'))
    plain = ENV.sub('', body); lvl = 0
    for m in re.finditer(r'(?<!\\)[{}]', plain):
        lvl += 1 if m.group() == '{' else -1
        assert lvl >= 0, (q, key, 'brace')
    assert lvl == 0, (q, key, 'brace')
    assert len(re.findall(r'(?<!\\)\$', plain)) % 2 == 0, (q, key, 'dollar')
    assert not re.search(r'\\(?:frac|tfrac|cfrac|over)(?![a-zA-Z])', body), (q, key, 'frac')
    assert not re.search(r'(?<!\\)%', plain), (q, key, 'percent')
    assert not re.search(r'[^\x00-\x7f]', body), (q, key, 'nonascii')
    assert '\\documentclass' not in body and 'tikzpicture' not in body
npreview = 0
with zipfile.ZipFile(zp) as z:
    assert z.testzip() is None
    names = set(z.namelist())
    mf = json.loads(z.read('manifest.json'))
    assert mf['question_ids'] == ids and len(set(mf['question_ids'])) == len(ids)
    folders = {n.split('/')[1] for n in names if n.startswith('questions/')}
    assert folders == idset
    for q in ids:
        md = json.loads(z.read(f'questions/{q}/metadata.json'))
        assert md['id'] == q and md['question_file'] == 'question.tex' and md['solution_file'] == 'solution.tex'
        assert all(t in TAGS for t in md['tags']) and len(md['tags']) == len(set(md['tags'])) and md['tags']
        assert isinstance(md['difficulty'], int) and 1 <= md['difficulty'] <= 10 and md['difficulty_rationale']
        texs = {}
        for key in ('question', 'solution'):
            t = z.read(f'questions/{q}/{key}.tex').decode(); assert t.strip(); body_checks(q, key, t); texs[key + '.tex'] = t
        for a in md['assets']: assert f'questions/{q}/{a["path"]}' in names
        nenv = sum(len(list(ENV.finditer(t))) for t in texs.values())
        assert nenv == len(md['diagram_previews']), q
        for p in md['diagram_previews']:
            envs = list(ENV.finditer(texs[p['file']]))
            assert hashlib.sha256(envs[p['index'] - 1].group().encode()).hexdigest() == p['source_sha256'], q
            assert p['alt'].strip() and f'questions/{q}/{p["path"]}' in names
            assert z.read(f'questions/{q}/{p["path"]}').lstrip().startswith((b'<?xml', b'<svg'))
            npreview += 1
    nmembers = len(names)

# compiled records / provenance consistency with the ZIP
assert [r['id'] for r in compiled] == ids and [r['id'] for r in prov] == ids
st = collections.Counter(e['status'] for e in screen)
assert sum(st.values()) == 100 * len(B) and sum(e['records'] for e in screen) == len(ids)

json.dump(compiled, open(OUT + '/compiled_records.json', 'w'), ensure_ascii=False, indent=1)
json.dump(prov, open(OUT + '/provenance.json', 'w'), ensure_ascii=False, indent=2)
json.dump(screen, open(OUT + '/screening_log.json', 'w'), ensure_ascii=False, indent=2)
json.dump(aliases, open(OUT + '/duplicate_aliases.json', 'w'), indent=2)
shutil.copy(src[LAST] + '/deduplication_registry.json', OUT + '/deduplication_registry.json')
summary = dict(batches=f'{FIRST}-{LAST}', question_records=len(ids), topics_screened=len(screen), screening_statuses=dict(st),
               aliases=len(aliases), diagram_previews=npreview, missing_diagram_previews=0, diagram_previews_compiled=True,
               zip_members=nmembers, zip_sha256=hashlib.sha256(open(zp, 'rb').read()).hexdigest(), checks_passed=True,
               per_batch={str(b): v for b, v in per_batch.items()})
json.dump(summary, open(OUT + '/validation_summary.json', 'w'), indent=2)
# review logs: each batch's builders and its own report
for b in B:
    dst = f'{OUT}/review_logs/batch_{b:04}'
    shutil.copytree(src[b] + '/review_logs/builders', dst + '/builders')
    shutil.copy(f'{work(b)}/processing_report.md', dst + '/processing_report.md')
    for nm in ('draft_notes.md', 'review_notes.md'):
        if os.path.exists(f'{work(b)}/{nm}'): shutil.copy(f'{work(b)}/{nm}', dst + '/' + nm)
print(json.dumps({k: v for k, v in summary.items() if k != 'per_batch'}, indent=1))
print('aliases canonical in this zip:', sum(e['canonical_in_this_zip'] for e in aliases))
print('merged package written to', OUT, '- now write its processing_report.md (see CLAUDE.md)')
