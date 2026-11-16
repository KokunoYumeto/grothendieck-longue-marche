"""Build the final immutable return, retaining every checkpoint file version.

Run only when the research turn is ready to end.  This does not create an
extra hourly checkpoint.  Historical versions are deduplicated by exact
SHA-256, with a complete per-checkpoint path index in the final archive.
"""
from pathlib import Path
import csv
import hashlib
import json
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[2]
DELIVERABLE = ROOT / 'deliverable'
target = ROOT / 'FERMAT_SUCCESSOR_final.zip'
if target.exists():
    raise SystemExit('Refusing to overwrite the final return')
if sys.argv[1:] != ['--final']:
    raise SystemExit('This final-only operation requires --final')

gate = subprocess.run(
    [sys.executable, str(DELIVERABLE / 'code/validate_artifacts.py'), '--publication'],
    cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
(DELIVERABLE / 'code/validate_artifacts.out').write_text(gate.stdout)
if gate.returncode:
    raise SystemExit(gate.stdout)

report = DELIVERABLE / 'FERMAT_SUCCESSOR_report.md'
history_note = '''\n\n## Preservation of hourly checkpoints\n\nThe final archive retains every file content that appeared in an hourly checkpoint. Unchanged contents are present in the current deliverable or work tree; earlier contents are retained under checkpoint_history/. The exact per-checkpoint file, digest, and final location are recorded in records/final_checkpoint_preservation.json. This includes superseded proof passages, intermediate status reports, earlier published PDFs, and their logs. Historical drafts retain their historical claims and must be read with the current numbered statements and corrections. No checkpoint file content is silently discarded. Original attachments, downloaded primary-source scans, and reproducible temporary runtime files remain excluded on the same basis as the hourly checkpoints.\n'''
if '## Preservation of hourly checkpoints' not in report.read_text():
    report.write_text(report.read_text() + history_note)

with (ROOT / 'background/MANIFEST.tsv').open() as handle:
    attached = {row['sha256'] for row in csv.DictReader(handle, delimiter='\t')}

payloads = {}
current_excluded = []
for base in (DELIVERABLE, ROOT / 'work'):
    for path in sorted(base.rglob('*')):
        if not path.is_file() or path.is_symlink():
            continue
        rel = path.relative_to(ROOT)
        if '__pycache__' in rel.parts:
            continue
        if base.name == 'work':
            if rel.parts[1] in ('primary', 'texformat') or rel.parts[1].startswith(('pari-', 'library_helpers_')):
                continue
            if path.suffix.lower() in ('.pdf', '.png', '.jpg', '.dvi', '.tar', '.xz'):
                continue
        data = path.read_bytes()
        digest = hashlib.sha256(data).hexdigest()
        if digest in attached:
            current_excluded.append({'path': str(rel), 'reason': 'identical to attached input', 'sha256': digest})
            continue
        payloads[str(rel)] = data

digest_to_location = {}
for name, data in payloads.items():
    digest_to_location.setdefault(hashlib.sha256(data).hexdigest(), name)

checkpoint_records = []
history_count = 0
for checkpoint in sorted(ROOT.glob('FERMAT_SUCCESSOR_checkpoint_[0-9][0-9].zip')):
    label = checkpoint.stem
    version_records = []
    with zipfile.ZipFile(checkpoint) as archive:
        names = archive.namelist()
        if len(names) != len(set(names)):
            raise SystemExit(f'Duplicate archive paths in {checkpoint.name}')
        for name in names:
            if name.endswith('/'):
                continue
            data = archive.read(name)
            digest = hashlib.sha256(data).hexdigest()
            destination = digest_to_location.get(digest)
            if destination is None:
                destination = f'checkpoint_history/{label}/{name}'
                if destination in payloads:
                    raise SystemExit(f'Historical path collision: {destination}')
                payloads[destination] = data
                digest_to_location[digest] = destination
                history_count += 1
            version_records.append({'checkpoint_path': name, 'sha256': digest, 'final_path': destination})
    checkpoint_records.append({
        'checkpoint': checkpoint.name,
        'checkpoint_sha256': hashlib.sha256(checkpoint.read_bytes()).hexdigest(),
        'file_versions': version_records,
    })

preservation = {
    'policy': 'Every checkpoint file content retained; exact duplicate contents share a final path.',
    'checkpoint_count': len(checkpoint_records),
    'additional_historical_contents': history_count,
    'current_identical_input_exclusions': current_excluded,
    'checkpoints': checkpoint_records,
}
index_path = DELIVERABLE / 'records/final_checkpoint_preservation.json'
index_path.write_text(json.dumps(preservation, indent=2) + '\n')
payloads[str(index_path.relative_to(ROOT))] = index_path.read_bytes()
payloads['README.txt'] = (
    'FERMAT_SUCCESSOR — final research return\n'
    'AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode)\n\n'
    'The current paper, PDF, statement register, bibliography, report, and code are in deliverable/.\n'
    'Read deliverable/FERMAT_SUCCESSOR_report.md first for the complete task/lead outcome table.\n'
    'The return is INCOMPLETE wherever the current register says Open or the task table says INCOMPLETE.\n'
    'work/ contains research and audit records. checkpoint_history/ preserves superseded versions;\n'
    'its exact index is deliverable/records/final_checkpoint_preservation.json.\n'
    'SHA256SUMS.txt covers every other file in this archive.\n'
).encode('utf-8')

hashes = {name: hashlib.sha256(data).hexdigest() for name, data in payloads.items()}
manifest = ''.join(f'{hashes[name]}  {name}\n' for name in sorted(hashes)).encode('utf-8')
with zipfile.ZipFile(target, 'x', zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
    for name in sorted(payloads):
        archive.writestr(name, payloads[name])
    archive.writestr('SHA256SUMS.txt', manifest)

with zipfile.ZipFile(target) as archive:
    for name, digest in hashes.items():
        if hashlib.sha256(archive.read(name)).hexdigest() != digest:
            raise SystemExit(f'Final archive digest mismatch: {name}')
    for record in checkpoint_records:
        for version in record['file_versions']:
            if hashes[version['final_path']] != version['sha256']:
                raise SystemExit(f'Checkpoint content not preserved: {version}')

print(json.dumps({
    'path': str(target), 'bytes': target.stat().st_size,
    'sha256': hashlib.sha256(target.read_bytes()).hexdigest(),
    'files': len(payloads) + 1, 'historical_contents': history_count,
    'checkpoints_fully_preserved': len(checkpoint_records),
    'all_archived_hashes_verified': True,
}, indent=2))
