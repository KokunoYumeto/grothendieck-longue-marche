from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / 'research_e105'
OUT = HERE / 'copied'
OUT.mkdir(exist_ok=True)

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

records = []
for name in ('a_quartic_frames_explore', 'a_quartic_class2', 'a_quartic_toric_cups'):
    original = SOURCE / 'code' / (name + '.py')
    copied = OUT / original.name
    shutil.copy2(original, copied)
    with copied.with_suffix('.out').open('wb') as stream:
        completed = subprocess.run([sys.executable, str(copied)], cwd=OUT,
                                   stdout=stream, stderr=subprocess.STDOUT)
    record = {'program': name, 'source_sha256': sha(original),
              'exit_code': completed.returncode}
    assert completed.returncode == 0, record
    for suffix in ('.out', '.json'):
        reference = original.with_suffix(suffix)
        actual = copied.with_suffix(suffix)
        equal = actual.read_bytes() == reference.read_bytes()
        record[suffix + '_byte_equal'] = equal
        record[suffix + '_sha256'] = sha(actual)
        assert equal, (name, suffix)
    records.append(record)
    print(json.dumps(record, sort_keys=True), flush=True)

result = {'status': 'PASS', 'excluded_fields': [], 'records': records,
          'section_sha256': sha(SOURCE / 'sections' / 'E_quartic_class_two.tex')}
(HERE / 'rebuild.json').write_text(json.dumps(result, indent=2) + '\n')
print('PASS: every complete stdout and JSON is byte-identical; no fields excluded.')
