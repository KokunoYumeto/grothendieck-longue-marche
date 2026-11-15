#!/usr/bin/env python3
"""During active transcription, check new or changed fragments in a scratch mirror.

This technical helper never modifies pages/. It does not read scan images or
context files. It stops after --seconds and records every checked source hash.
"""
import argparse
import datetime as dt
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time

sys.dont_write_bytecode = True

SCRIPTS = Path(__file__).resolve().parent
ROOT = SCRIPTS.parent


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--seconds', type=int, default=900)
    args = parser.parse_args()
    qa = load_module('qa', SCRIPTS / 'check_latex.py')
    propose = load_module('propose', SCRIPTS / 'propose_latex_fixes.py')
    env = qa.env_for_tex()
    qa.ensure_format(env)
    report_path = ROOT / 'records' / 'latex_qa_continuous.json'
    report = json.loads(report_path.read_text()) if report_path.exists() else {'scope': 'Syntax-only scratch-mirror checks; no image/context reading or page edits', 'checks': {}}
    seen = {name: value['original_sha256'] for name, value in report['checks'].items()}
    end = time.monotonic() + args.seconds
    while time.monotonic() < end:
        pending = [p for p in sorted((ROOT / 'pages').glob('*.tex')) if seen.get(p.name) != digest(p)]
        if pending:
            propose = load_module('propose', SCRIPTS / 'propose_latex_fixes.py')
            manifest = propose.main()
            for path in pending:
                original_hash = manifest[path.name]['original_sha256']
                result = qa.compile_page(propose.MIRROR / path.name, env)
                result['original_sha256'] = original_hash
                result['checked_utc'] = dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
                report['checks'][path.name] = result
                seen[path.name] = original_hash
                print(result['scan'], 'PASS' if result['returncode'] == 0 and not result['structural'] else 'FAIL', flush=True)
                for message in result['errors'][:6]:
                    print('  ' + message, flush=True)
                report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
        time.sleep(min(20, max(0, end - time.monotonic())))
    print('Watcher finished; source pages were not modified.', flush=True)


if __name__ == '__main__':
    main()
