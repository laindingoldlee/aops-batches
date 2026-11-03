# After a run is merged and committed: python3 tools/advance.py
# Folds the run into ref/ so the NEXT run screens duplicates against it and chains its registry from it:
#   ref/base_registry.json <- output/processed_batches_FFFF_LLLL/deduplication_registry.json
#   ref/prior.json         += that package's compiled_records.json
#   ref/progress.json      registry_through = LAST
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from qbpaths import FIRST, LAST, OUTPUT, REF
pkg = f'{OUTPUT}/processed_batches_{FIRST:04}_{LAST:04}'
reg = json.load(open(pkg + '/deduplication_registry.json'))
base = json.load(open(REF + '/base_registry.json'))
prog = json.load(open(REF + '/progress.json'))
if prog['registry_through'] >= LAST: raise SystemExit(f'already advanced through {prog["registry_through"]}')
assert len(reg['records']) > len(base['records']), 'new registry is not larger than the base'
prior = json.load(open(REF + '/prior.json'))
have = {r['id'] for r in prior}
added = 0
for r in json.load(open(pkg + '/compiled_records.json')):
    if r['id'] in have: continue
    prior.append(dict(id=r['id'], src=os.path.basename(pkg), tags=r.get('tags'), question=r['question'], solution=r['solution'], note=r.get('note', '')))
    added += 1
json.dump(prior, open(REF + '/prior.json', 'w'), ensure_ascii=True)
json.dump(reg, open(REF + '/base_registry.json', 'w'), ensure_ascii=False, indent=1)
prog['registry_through'] = LAST; prog.setdefault('runs', []).append(f'{FIRST}-{LAST}')
json.dump(prog, open(REF + '/progress.json', 'w'), indent=1)
print(f'ref/ now covers batches through {LAST}: +{added} prior records, registry {len(reg["records"])} records')
