"""Replay the entire E109 shadow certificate and compare complete outputs."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
SOURCE = HERE/'e_quartic_ceresa_shadow.py'
DEST = HERE.parent/'replay'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert not DEST.exists()
DEST.mkdir()
before = {p.name:sha(p) for p in [SOURCE,SOURCE.with_suffix('.json'),SOURCE.with_suffix('.out')]}
target=DEST/SOURCE.name
shutil.copy2(SOURCE,target)
with target.with_suffix('.out').open('wb') as output:
    result=subprocess.run([sys.executable,str(target)],stdout=output,stderr=subprocess.STDOUT)
assert result.returncode==0,result.returncode
checks=[]
for suffix in ['.json','.out']:
    original=SOURCE.with_suffix(suffix);fresh=target.with_suffix(suffix)
    assert original.read_bytes()==fresh.read_bytes(),suffix
    checks.append({'file':original.name,'complete_byte_equality':True,'sha256':sha(fresh)})
assert before=={p.name:sha(p) for p in [SOURCE,SOURCE.with_suffix('.json'),SOURCE.with_suffix('.out')]}
record={'status':'PASS','exit_code':result.returncode,'source_sha256':sha(SOURCE),
        'checks':checks,'excluded_fields':[],
        'scope':'Fresh complete execution. The earlier stdout already recorded PASS; this replay independently records an observed process exit0 without modifying that original output.'}
SOURCE.with_name('e_quartic_ceresa_replay.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
