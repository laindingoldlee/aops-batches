#!/bin/bash
# Rebuild, check and finalize every batch of the run IN ORDER (each batch's registry builds on the previous one).
# Usage (from anywhere in the repo): bash tools/runall.sh            (whole run.json range)
#                                    bash tools/runall.sh 223 230    (a sub-range; earlier batches must already be finalized)
set -e
ROOT=$(cd "$(dirname "$0")/.." && pwd)
FIRST=$(python3 -c "import json;print(json.load(open('$ROOT/run.json'))['first'])")
LAST=$(python3 -c "import json;print(json.load(open('$ROOT/run.json'))['last'])")
A=${1:-$FIRST}; Z=${2:-$LAST}
for b in $(seq $A $Z); do
  cd "$ROOT/work/b$b"
  echo "=== batch $b"
  rm -f rec/*.json
  for f in p${b}_[0-9][0-9].py; do python3 $f > /dev/null; done
  timeout 900 python3 chk.py > /tmp/chk$b.log 2>&1 || { echo "CHK FAIL $b"; tail -5 /tmp/chk$b.log; exit 1; }
  python3 precheck.py $b | tail -2
  rm -rf out
  QB_FINAL=1 python3 finalize.py $b > /tmp/fin$b.log 2>&1 || { echo "FINALIZE FAIL $b"; tail -20 /tmp/fin$b.log; exit 1; }
  grep -E "registry:" /tmp/fin$b.log | head -1
  python3 -c "import json;v=json.load(open('out/processed_batches_0${b}_0${b}/validation_summary.json'));print({k:v[k] for k in ['question_records','screening_statuses','diagram_previews','zip_members']})"
done
