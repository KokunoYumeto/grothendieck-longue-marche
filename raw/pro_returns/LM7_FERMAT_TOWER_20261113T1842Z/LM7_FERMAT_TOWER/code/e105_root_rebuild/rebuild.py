"""Independent copied execution of every frozen E105 mathematical program."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
AUTHOR = HERE.parent / 'research_e105'
MANIFEST = AUTHOR / 'ledger/e_quartic_class2_manifest.json'
EXPECTED = '662e1c77f11110d9280d1bca4a733a0165cf32adf3ee8f3c3ab8296117710608'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(MANIFEST) == EXPECTED
manifest = json.loads(MANIFEST.read_text())
assert manifest['statement'] == 'E.105'
assert manifest['external_project_inputs'] == []
for relative, metadata in manifest['files'].items():
    p = AUTHOR / relative
    assert p.stat().st_size == metadata['bytes'], relative
    assert sha(p) == metadata['sha256'], relative
    if relative.endswith(('.py', '.tex')):
        destination = HERE / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(p, destination)

names = ['a_quartic_frames_explore', 'a_quartic_class2', 'a_quartic_toric_cups']
def execute(name):
    command = [sys.executable, str(HERE / 'code' / (name + '.py'))]
    with (HERE / 'code' / (name + '.out')).open('w') as stream:
        run = subprocess.run(command, cwd=HERE, stdout=stream, stderr=subprocess.STDOUT)
    assert run.returncode == 0, (name, run.returncode)
    comparisons = []
    for suffix in ('.out', '.json'):
        relative = 'code/' + name + suffix
        fresh = (HERE / relative).read_bytes()
        assert fresh == (AUTHOR / relative).read_bytes(), relative
        comparisons.append({'path':relative, 'bytes':len(fresh), 'sha256':sha(HERE / relative),
                            'entire_file_byte_identical':True})
    return {'program':name, 'command':command, 'exit_code':run.returncode,
            'source_sha256':sha(HERE / 'code' / (name + '.py')), 'comparisons':comparisons}

with ThreadPoolExecutor(max_workers=3) as pool:
    records = list(pool.map(execute, names))
for relative, metadata in manifest['files'].items():
    assert sha(AUTHOR / relative) == metadata['sha256'], relative
assert sha(MANIFEST) == EXPECTED
result = {'status':'PASS', 'statement':'E.105', 'author_manifest_sha256':EXPECTED,
          'proof_sha256':sha(AUTHOR / manifest['section']),
          'manifest_files_checked':len(manifest['files']), 'records':records,
          'excluded_fields':[], 'author_sources_unchanged':True,
          'scope':'All three mathematical programs were copied and executed. Every complete stdout and JSON agrees byte for byte, including the separate endpoint-sign data, rational-two root carries, all121 frames, exact central averaging comparisons, actual tame defects and retained phantom prefix.'}
(HERE / 'comparison.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
