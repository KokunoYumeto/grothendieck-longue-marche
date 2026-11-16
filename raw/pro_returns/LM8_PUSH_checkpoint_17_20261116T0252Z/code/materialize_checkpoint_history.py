#!/usr/bin/env python3
"""Retain every indexed historical version without nesting old ZIP containers.

Run prepare_final_history.py first. All historical entry bytes are checked
against their indexed hashes. Large superseded numerical encodings have a
separate, already verified decoded-payload accounting; no proof text is omitted.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import zipfile

ROOT = Path(__file__).resolve().parents[1]
plan = json.loads((ROOT / 'notes/final_history_inventory.json').read_text())
outdir = ROOT / 'checkpoint_history'
outdir.mkdir(exist_ok=True)

def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()

objects = {}
restored = {}
snapshots = []
omissions = []
checked_entries = 0
for snapshot in plan['snapshots']:
    serial = snapshot['serial']
    archive = Path(snapshot['archive_path'])
    assert sha(archive) == snapshot['archive_sha256'], str(archive)
    entries = []
    with zipfile.ZipFile(archive) as z:
        assert len([i for i in z.infolist() if not i.is_dir()]) == snapshot['entry_count']
        for row in snapshot['entries']:
            entry = {k: row[k] for k in ('path', 'bytes', 'sha256')}
            representation = row['representation']
            # Reading each entry also performs ZIP CRC verification.
            data = z.read(row['path'])
            assert len(data) == row['bytes']
            assert hashlib.sha256(data).hexdigest() == row['sha256'], (serial, row['path'])
            checked_entries += 1
            if representation == 'superseded_encoding':
                entry.update(representation=representation,
                             retained_payload=row['retained_payload'], reason=row['reason'])
                omissions.append({'checkpoint': serial, **entry})
            elif representation == 'current_restored_exact':
                source = row['source_path']
                if source not in restored:
                    path = ROOT / source
                    assert path.stat().st_size == row['bytes']
                    assert sha(path) == row['sha256'], source
                    restored[source] = {k: row[k] for k in ('bytes', 'sha256')}
                assert restored[source]['sha256'] == row['sha256']
                entry.update(representation='current_restored_exact', source_path=source)
            else:
                digest = row['sha256']
                if digest not in objects:
                    suffix = Path(row['path']).suffix
                    relative = f'checkpoint_history/objects/{digest[:2]}/{digest}{suffix}'
                    target = ROOT / relative
                    target.parent.mkdir(parents=True, exist_ok=True)
                    if target.exists():
                        assert target.stat().st_size == len(data) and sha(target) == digest
                    else:
                        with target.open('xb') as stream:
                            stream.write(data)
                    objects[digest] = {'path': relative, 'bytes': len(data), 'sha256': digest}
                entry.update(representation='history_object', object_path=objects[digest]['path'])
            entries.append(entry)
    snapshots.append({k: v for k, v in snapshot.items() if k != 'entries'} | {'entries': entries})
    print(f'Checkpoint {serial:02d}: verified and materialized {len(entries)} entries', flush=True)

index = {
    'status': 'MATERIALIZED_VERIFIED_HISTORY',
    'created_utc': datetime.now(timezone.utc).isoformat(),
    'through_checkpoint': plan['through_checkpoint'],
    'snapshots': snapshots,
    'objects': list(objects.values()),
    'exact_current_restoration_dependencies': restored,
    'individually_superseded_encodings': omissions,
    'verified_prefix_checks': plan['prefix_checks'],
    'historical_entries': checked_entries,
    'container_policy': 'Each old ZIP wrapper is superseded here by its complete file/version index; original archives remain unchanged. Every other omission is individually recorded below.',
    'restoration': 'python code/restore_checkpoint_history.py --checkpoint NN --destination NEW_DIRECTORY; see checkpoint_history/README.md',
}
(outdir / 'HISTORY_INDEX.json').write_text(json.dumps(index, indent=2) + '\n')
readme = '''# Complete checkpoint file and version history

`HISTORY_INDEX.json` accounts for every actual file entry in each selected,
successfully saved checkpoint. Every text, source, PDF, note, certificate,
failed attempt and metadata version is retained byte for byte, either as a
content object or as an exactly restorable current file. Identical content
objects may share their storage with current files in the outer archive.

The original checkpoint ZIP wrappers are not nested again. Their exact names,
sizes and SHA-256 hashes are recorded individually in the index; the saved
originals remain unchanged. Three obsolete numerical encoding files are also
individually superseded. Their complete decoded mathematical payloads, including
the verified historical prefix where needed, remain reconstructable. The
accounting records every original encoding hash and its replacement.

To restore a historical file tree from a clean extraction, first run the
outer archive's `RESTORE_LARGE_LOGS.py`. This reconstructs current encoded
logs and page images, checking full decoded counts and hashes. Then run:

```sh
python code/restore_checkpoint_history.py --checkpoint 11 --destination ../restored_checkpoint_11
```

Select any checkpoint serial covered by the index. The destination must be
new. The history helper checks each exact file hash again. For a superseded
numerical encoding, it restores the original mathematical log payload at its
original source path and writes an individual accounting record, instead of
recreating an obsolete binary encoding or its incidental gzip wrapper.
Historical recovery helpers can subsequently be run inside that directory:
already reconstructed original log paths are left unchanged.

This is content/version restoration, not byte-for-byte recreation of the old
ZIP container. No earlier proof passage or failed attempt is silently removed.
'''
(outdir / 'README.md').write_text(readme)
lines = ['# Final history preservation and individual supersessions', '',
         'The earlier plan to nest raw checkpoint ZIP containers is superseded by the complete, verified content/version history in `checkpoint_history/HISTORY_INDEX.json`. The original saved checkpoints remain unchanged. Every historical file entry has an exact retained object, an exact current-restoration reference, or an individually stated numerical-encoding replacement. All historical proof text, notes, logs, failures, source, register and PDF versions remain covered.', '',
         '## Checkpoint containers', '',
         'These ZIP wrappers are individually superseded by the corresponding complete entry lists in the history index; their file contents are accounted for there.', '',
         '| Checkpoint | Original bytes | Original SHA-256 | Replacement |',
         '|---|---:|---|---|']
for s in snapshots:
    lines.append(f"| {s['serial']:02d} | {s['archive_bytes']} | `{s['archive_sha256']}` | History index snapshot {s['serial']:02d} and exact objects/restoration recipes |")
lines += ['', '## Individually superseded numerical encodings', '',
          '| Checkpoint and original path | Original bytes and SHA-256 | Retained exact decoded replacement |',
          '|---|---|---|']
for e in omissions:
    p = e['retained_payload']
    lines.append(f"| {e['checkpoint']:02d}: `{e['path']}` | {e['bytes']}; `{e['sha256']}` | `{p['source_path']}`; first {p['decoded_bytes']} decoded bytes, SHA-256 `{p['decoded_sha256']}`. {p['comparison']}. |")
lines += ['', 'Only these compression representations and the named ZIP wrappers are omitted from the history materialization. Their mathematical records are retained exactly as specified. This does not promote any unresolved mathematical claim.', '',
          f"Materialization checked all {checked_entries} historical ZIP entries, retained {len(objects)} distinct exact content objects, and checked {len(restored)} exact current-restoration dependencies. The packager may deduplicate identical content objects against current archive bytes, with an explicit copy recipe.", '']
(ROOT / 'notes/final_history_preservation.md').write_text('\n'.join(lines))
result = {'status': 'PASS', 'through_checkpoint': plan['through_checkpoint'],
          'historical_entries_checked': checked_entries, 'unique_objects': len(objects),
          'object_bytes_before_deduplication': sum(e['bytes'] for e in objects.values()),
          'exact_restoration_dependencies': len(restored),
          'individually_superseded_encodings': len(omissions)}
(ROOT / 'notes/final_history_materialization.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2), flush=True)
