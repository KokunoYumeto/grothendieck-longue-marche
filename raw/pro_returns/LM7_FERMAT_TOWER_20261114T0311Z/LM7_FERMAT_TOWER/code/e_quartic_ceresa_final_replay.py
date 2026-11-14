"""Fresh execution of the complete E109 certificate, with whole-output checks."""
from pathlib import Path
from tempfile import TemporaryDirectory
import hashlib
import json
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'e_quartic_ceresa_shadow.py'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
originals = [SOURCE.with_suffix(s) for s in ['.py', '.out', '.json']]
before = {p.name: sha(p) for p in originals}
with TemporaryDirectory(prefix='e109_fresh_', dir=HERE.parent) as directory:
    target = Path(directory) / SOURCE.name
    shutil.copy2(SOURCE, target)
    with target.with_suffix('.out').open('wb') as stream:
        result = subprocess.run([sys.executable, str(target)], stdout=stream,
                                stderr=subprocess.STDOUT)
    assert result.returncode == 0, result.returncode
    checks = []
    for suffix in ['.out', '.json']:
        old, new = SOURCE.with_suffix(suffix), target.with_suffix(suffix)
        assert old.read_bytes() == new.read_bytes(), suffix
        checks.append({'file': old.name, 'sha256': sha(new),
                       'complete_byte_equality': True})
    destination = HERE.parent / 'replay_verified'
    destination.mkdir(exist_ok=True)
    for suffix in ['.py', '.out', '.json']:
        shutil.copy2(target.with_suffix(suffix), destination / target.with_suffix(suffix).name)
assert before == {p.name: sha(p) for p in originals}
record = {'status': 'PASS', 'actual_exit_code': result.returncode,
          'source_sha256': sha(SOURCE), 'checks': checks, 'excluded_fields': [],
          'scope': 'Fresh full execution of finite elliptic shadows, coefficient maps with a cohomology left inverse, all order-sixteen character averages, and the literal curve/isogeny comparison.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
