#!/usr/bin/env python3
"""Build all seven readers twice while checking frozen inputs before and after."""
from pathlib import Path
import argparse
import datetime
import hashlib
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / 'work/data'


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--jobs', type=int, default=3)
    args = parser.parse_args()
    if args.jobs < 1:
        parser.error('--jobs must be positive')
    freeze_path = DATA / 'layout_release_checkpoint.json'
    freeze = json.loads(freeze_path.read_text())
    for key in ['all_exact_patches_replayed', 'all_source_marks_preserved',
                'all_raw_source_offsets_valid', 'local_size_gate_pass']:
        assert freeze.get(key) is True, key
    source_dependencies = freeze['sha256']
    for path, expected in source_dependencies.items():
        assert digest(ROOT / path) == expected, 'Stale source freeze: ' + path
    assembly_paths = [
        'work/scripts/build_readers.py', 'work/scripts/editorial.py',
        'work/scripts/mechanical_repairs.py', 'work/scripts/instrument_marks.py',
        'work/scripts/book_preamble.tex', 'work/scripts/book_links.lua',
        'work/data/frontmatter.json', 'work/scripts/build_frozen_release.py',
    ]
    assembly_dependencies = {p: digest(ROOT / p) for p in assembly_paths}
    command = ['work/scripts/build_readers.py', '--stage', 'build', '--compile',
               '--runs', '2', '--jobs', str(args.jobs)]
    record = {
        'status': 'INPUTS_FROZEN_FOR_SEVEN_BOOK_BUILD', 'started_at_utc': now(),
        'freeze_record': freeze_path.relative_to(ROOT).as_posix(),
        'freeze_sha256': digest(freeze_path), 'source_records': freeze['records'],
        'source_dependencies': source_dependencies,
        'assembly_dependencies': assembly_dependencies,
        'compile_passes': 2, 'books': 7, 'command': ['python'] + command,
    }
    output = DATA / 'final_build_inputs.json'
    output.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
    result = subprocess.run([sys.executable] + command, cwd=ROOT)
    changed = [path for path, expected in
               {**source_dependencies, **assembly_dependencies}.items()
               if digest(ROOT / path) != expected]
    if digest(freeze_path) != record['freeze_sha256']:
        changed.append(record['freeze_record'])
    record.update(finished_at_utc=now(), return_code=result.returncode,
                  changed_inputs=changed,
                  status=('TWO_PASS_BUILD_COMPLETE_INPUTS_UNCHANGED'
                          if result.returncode == 0 and not changed
                          else 'BUILD_FAILED_OR_INPUTS_CHANGED'))
    output.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({key: record[key] for key in
                      ['status', 'source_records', 'books', 'compile_passes',
                       'return_code', 'changed_inputs']}, ensure_ascii=False), flush=True)
    return 0 if result.returncode == 0 and not changed else 1


if __name__ == '__main__':
    raise SystemExit(main())
