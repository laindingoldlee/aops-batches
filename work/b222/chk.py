# Answer checks for this batch: runs every chk_pNNN_KK.py in its own namespace; run: python3 chk.py
import runpy, glob, os
from qbpaths import prefix
B = int(os.path.basename(os.getcwd())[1:])
fs = sorted(glob.glob('chk_' + prefix(B) + '[0-9][0-9].py'))
assert fs, 'no chk files'
for f in fs:
    runpy.run_path(f, run_name='__main__'); print('ok', f)
print("chk OK")
