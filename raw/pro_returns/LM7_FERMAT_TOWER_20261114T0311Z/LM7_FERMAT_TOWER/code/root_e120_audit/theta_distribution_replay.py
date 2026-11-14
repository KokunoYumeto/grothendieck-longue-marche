"""Replay the frozen theta/principal-divisor certificate in a fresh directory."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys

BASE = Path(__file__).resolve().parent
AUTHOR = BASE.parent / 'research_e120'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    source_manifest = AUTHOR/'ledger/a_theta_principal_distribution_manifest.json'
    raw = source_manifest.read_bytes()
    assert sha(raw) == 'c59f0dcd88e32fcc42422611050ecfe6dac5532ae6936b1d4615b769199f9e26'
    manifest = json.loads(raw)
    records = manifest['owned'] + manifest['immutable_inputs']

    def check_author():
        for item in records:
            data = (AUTHOR/item['path']).read_bytes()
            assert len(data) == item['bytes'] and sha(data) == item['sha256'], item

    check_author()
    (BASE/'theta_distribution_author_manifest.json').write_bytes(raw)
    shutil.copy2(AUTHOR/'notes/theta_principal_distribution.md', BASE/'theta_distribution_author_note.md')
    fresh = BASE/'theta_distribution_fresh'
    fresh.mkdir()
    code = fresh/'code'
    code.mkdir()
    selected = ['code/a_theta_principal_distribution.py'] + [r['path'] for r in manifest['immutable_inputs']]
    for relative in selected:
        shutil.copy2(AUTHOR/relative, fresh/relative)
    executions = []

    def execute(filename, args=()):
        script = code/filename
        command = [sys.executable, str(script), *args]
        result = subprocess.run(command, cwd=code, capture_output=True, timeout=60)
        script.with_suffix('.out').write_bytes(result.stdout)
        script.with_suffix('.err').write_bytes(result.stderr)
        executions.append({'program':filename,'arguments':list(args),'exit_code':result.returncode,
                           'source_sha256':sha(script.read_bytes()),
                           'stdout_sha256':sha(result.stdout),'stderr_sha256':sha(result.stderr),
                           'stdout_bytes':len(result.stdout),'stderr_bytes':len(result.stderr)})
        assert result.returncode == 0 and not result.stderr
        return result

    silent = execute('a_e120_exact.py')
    assert silent.stdout == b''
    (code/'a_e120_exact_status.json').write_text(json.dumps({
        'status':'silent module executed successfully','exit_code':0,
        'reason':'The exact field-arithmetic module defines functions and has no standalone print operation; the freshly executed distribution certificate imports and exercises it.',
        'execution':executions[-1]},indent=2)+'\n')
    execute('a_local_smith.py', ('--help',))
    (code/'a_local_smith_status.json').write_text(json.dumps({
        'status':'help entry point executed; arithmetic exercised by importing certificate',
        'exit_code':0,'reason':'The standalone entry point requires the original larger Smith input; the distribution certificate imports local_smith and verifies all four inverse-pair products on its actual integral operator.',
        'execution':executions[-1]},indent=2)+'\n')
    execute('a_theta_principal_distribution.py')
    comparisons = []
    for suffix in ['.out','.err','.json']:
        filename = 'a_theta_principal_distribution'+suffix
        data = (code/filename).read_bytes()
        assert data == (AUTHOR/'code'/filename).read_bytes()
        comparisons.append({'file':str((code/filename).relative_to(BASE)),
                            'bytes':len(data),'sha256':sha(data),'complete_byte_equality':True})
    check_author()
    result = {
        'status':'PASS','manifest_sha256':sha(raw),
        'owned_files_checked_before_and_after':len(manifest['owned']),
        'immutable_inputs_checked_before_and_after':len(manifest['immutable_inputs']),
        'executions':executions,'comparisons':comparisons,
        'fields_or_bytes_excluded':[], 'author_sources_modified':False,
        'checked_utc':datetime.now(timezone.utc).isoformat()}
    (BASE/'theta_distribution_replay_audit.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
