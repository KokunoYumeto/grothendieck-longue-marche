"""Complete fresh D56 rebuild; compare every field except named run times."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / 'D56_EXPERIMENTS'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
manifest_path = SOURCE / 'ledger/d_arithmetic_detecting_quotient_manifest.json'
manifest = json.loads(manifest_path.read_text())
for row in manifest['files'] + manifest['runtime_inputs']:
    assert sha(SOURCE / row['path']) == row['sha256'], row['path']
code = HERE / 'code'
code.mkdir(exist_ok=True)
for row in manifest['runtime_inputs']:
    target = code / Path(row['path']).name
    assert not target.exists(), target
    shutil.copyfile(SOURCE / row['path'], target)
for name in manifest['run_order']:
    assert not (code / name).exists(), name
    shutil.copyfile(SOURCE / 'code' / name, code / name)

stages = []
for name in manifest['run_order']:
    target = code / name
    with target.with_suffix('.out').open('w') as out:
        result = subprocess.run([sys.executable, str(target)], cwd=HERE,
                                stdout=out, stderr=subprocess.STDOUT, check=False)
    assert result.returncode == 0, (name, result.returncode)
    stages.append({'program': name, 'source_sha256': sha(target),
                   'returncode': result.returncode})
    print('Rebuilt ' + name, flush=True)

def compare(a, b, path, excluded):
    assert type(a) is type(b), (path, type(a), type(b))
    if isinstance(a, dict):
        assert a.keys() == b.keys(), path
        for key in a:
            child = path + '/' + key
            if key == 'elapsed_seconds':
                assert isinstance(a[key], (float, int)) and isinstance(b[key], (float, int))
                excluded.append({'path': child, 'actual_values': [a[key], b[key]]})
            else:
                compare(a[key], b[key], child, excluded)
    elif isinstance(a, list):
        assert len(a) == len(b), path
        for i, (x, y) in enumerate(zip(a, b)):
            compare(x, y, path + '/' + str(i), excluded)
    else:
        assert a == b, path

comparisons = []
for name in manifest['run_order']:
    assert sha(code / name) == sha(SOURCE / 'code' / name)
    for ext in ['.json', '.out']:
        original = (SOURCE / 'code' / name).with_suffix(ext)
        fresh = (code / name).with_suffix(ext)
        texts = [p.read_text() for p in [original, fresh]]
        starts = [t.index('{') for t in texts]
        assert texts[0][:starts[0]] == texts[1][:starts[1]], original.name
        a, b = [json.loads(t[i:]) for t, i in zip(texts, starts)]
        excluded = []
        compare(a, b, '', excluded)
        assert excluded and all(x['path'].endswith('/elapsed_seconds') for x in excluded)
        comparisons.append({'file': original.name, 'source_sha256': sha(original),
                            'fresh_sha256': sha(fresh), 'complete_prefix_equal': True,
                            'all_remaining_fields_equal': True,
                            'only_excluded_fields': excluded})
for row in manifest['runtime_inputs']:
    assert sha(SOURCE / row['path']) == sha(code / Path(row['path']).name) == row['sha256']
for row in manifest['files']:
    assert sha(SOURCE / row['path']) == row['sha256'], row['path']
result = {'status': 'PASS', 'section_sha256': sha(SOURCE / 'sections/D_arithmetic_detecting_quotient.tex'),
          'frozen_manifest_sha256': sha(manifest_path), 'stages': stages,
          'complete_comparisons': comparisons, 'unchanged_runtime_inputs': manifest['runtime_inputs'],
          'root_source_review': 'All seven programs read completely; full section read completely.'}
(HERE / 'comparison.json').write_text(json.dumps(result, indent=2) + '\n')
print('PASS all seven fresh D56 programs; complete JSON/stdout equality except named elapsed_seconds fields.', flush=True)
