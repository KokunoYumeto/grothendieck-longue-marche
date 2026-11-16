"""Take a stable working-tree snapshot immediately before an hourly ZIP.

Pause source writers for this copy only. Archive compression and upload can
then proceed against the snapshot while research resumes in the main tree.
This helper does not itself create or upload a checkpoint.
"""
import argparse
import json
import shutil
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('--destination', required=True)
parser.add_argument('--utc', required=True)
args = parser.parse_args()
source = Path(__file__).resolve().parents[1]
destination = Path(args.destination).resolve()
if destination.exists():
    raise SystemExit('Refusing to overwrite a previous snapshot')
shutil.copytree(source, destination, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
record = {'source': str(source), 'snapshot': str(destination),
          'observed_utc': args.utc,
          'purpose': 'Stable input for the scheduled hourly ZIP; original writers may resume.'}
(destination / 'notes' / 'snapshot_record.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2), flush=True)
