"""Retain parent36 and compose its freshly verified historical map.

This separate37 helper adapts the reviewed36 source; that source is unchanged.
No archive1-35 is opened. The trust base is the explicit, pinned, previously
verified parent36 coverage certificate. Publication requires --commit and
all three mutable records still equal their archived parent36 bytes.
"""
from pathlib import Path, PurePosixPath
from datetime import datetime, timezone
from collections import Counter
import argparse
import csv
import hashlib
import io
import json
import os
import tempfile

from checkpoint_archive_io import (
    CheckpointReader, PREFIX, IMAGE_BUNDLE, DOCUMENT_BUNDLE, DATA_BUNDLE,
)

ROOT = Path(__file__).resolve().parents[1]
FIELDS = ['checkpoint', 'archive', 'original_path', 'bytes', 'sha256',
          'retained_path', 'retention', 'omission_reason']
IDENTITY = FIELDS[:5]
MAP_FIELDS = ['original_path', 'bytes', 'sha256', 'retained_path', 'retention']
REWRITTEN = (
    'records/checkpoint_version_retention.csv',
    'records/checkpoint_version_retention_summary.json',
    'checkpoint_history/README.md',
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def file_sha(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(4 * 1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def relative(value):
    p = PurePosixPath(value)
    require(bool(p.parts) and not p.is_absolute() and
            all(s not in ('', '.', '..') for s in p.parts) and
            str(p) == value and '\\' not in value,
            'Unsafe or noncanonical relative path: ' + repr(value))
    return value


def local(root, value):
    path = root / relative(value)
    require(path.resolve().is_relative_to(root.resolve()),
            'Path escapes project: ' + value)
    require(not path.is_symlink(), 'Symlink is not an authorized payload: ' + value)
    return path


def csv_rows(data, delimiter=','):
    return list(csv.DictReader(io.StringIO(data.decode('utf-8')), delimiter=delimiter))


def csv_bytes(rows, fields):
    out = io.StringIO(newline='')
    writer = csv.DictWriter(out, fieldnames=fields, lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)
    return out.getvalue().encode('utf-8')


def identities(rows):
    return [[str(row[key]) for key in IDENTITY] for row in rows]


def tuple_sha(rows):
    return sha(json.dumps(identities(rows), ensure_ascii=False,
                          separators=(',', ':')).encode('utf-8'))


def json_bytes(obj):
    return (json.dumps(obj, indent=2, sort_keys=True) + '\n').encode('utf-8')


def checked_archive(reader, number, collect=None):
    """Verify every logical payload and all three standard bundle identities."""
    names = reader.names()
    require(len(names) == len(set(names)), 'Duplicate logical archive entries')
    manifest_name = PREFIX + f'records/checkpoint_{number:02d}_contents_sha256.tsv'
    manifest_data = reader.read(manifest_name)
    manifest = csv_rows(manifest_data, '\t')
    expected = {}
    for row in manifest:
        name = PREFIX + relative(row['path'])
        require(name not in expected, 'Duplicate manifest row: ' + name)
        expected[name] = row
    require(set(names) == set(expected) | {manifest_name},
            'Manifest does not cover exactly every logical entry')
    metadata = {}
    for name in sorted(names):
        require(name.startswith(PREFIX), 'Wrong project prefix: ' + name)
        rel = relative(name[len(PREFIX):])
        data = reader.read(name)  # ZipFile checks CRC while reading physical data.
        entry = {'bytes': len(data), 'sha256': sha(data)}
        if name != manifest_name:
            row = expected[name]
            require(entry['bytes'] == int(row['bytes']) and
                    entry['sha256'] == row['sha256'], 'Manifest mismatch: ' + rel)
        metadata[rel] = entry
        if collect is not None:
            collect(rel, data, entry)
    packaging = json.loads(reader.read(
        PREFIX + f'records/checkpoint_{number:02d}_packaging.json'))
    for bundle, blob, members, kind in (
        (IMAGE_BUNDLE, reader.tar_bytes, reader.members, 'image'),
        (DOCUMENT_BUNDLE, reader.document_tar_bytes, reader.document_members, 'document'),
        (DATA_BUNDLE, reader.data_tar_bytes, reader.data_members, 'data'),
    ):
        require(bundle in reader.direct and blob is not None,
                'Required standard TAR absent: ' + bundle)
        require(len(blob) == int(packaging[kind + '_bundle_bytes']) and
                sha(blob) == packaging[kind + '_bundle_sha256'] and
                len(members) == int(packaging[kind + '_paths']),
                'Bundle identity mismatch: ' + kind)
    return metadata


def load_anchor(path, parent):
    raw = path.read_bytes()
    anchor = json.loads(raw)
    require(anchor['schema'] == 'checkpoint-inductive-anchor-v1', 'Wrong anchor schema')
    require(anchor['parent_number'] == 36 and anchor['child_number'] == 37,
            'This helper is bound specifically to36->37')
    require(parent.name == anchor['archive'], 'Wrong parent archive name')
    require(parent.stat().st_size == anchor['archive_bytes'] and
            file_sha(parent) == anchor['archive_sha256'], 'Parent archive identity failure')
    require(bool(anchor['trusted_coverage']['assertion']), 'Missing explicit coverage trust base')
    return anchor, raw


def checked_parent(reader, anchor, collect=None):
    metadata = checked_archive(reader, anchor['parent_number'], collect)
    require(len(metadata) == anchor['logical_entries'], 'Parent logical count changed')
    pinned = {}
    for rel, expected in anchor['pinned_files'].items():
        data = reader.read(PREFIX + relative(rel))
        require(len(data) == expected['bytes'] and sha(data) == expected['sha256'],
                'Pinned parent file mismatch: ' + rel)
        pinned[rel] = data
    old = csv_rows(pinned[REWRITTEN[0]])
    require(len(old) == anchor['inherited_rows'], 'Inherited coverage row count changed')
    require(tuple_sha(old) == anchor['inherited_tuple_sha256'], 'Historical tuples changed')
    require(dict(Counter(row['checkpoint'] for row in old)) == anchor['inherited_counts'],
            'Historical per-checkpoint coverage changed')
    keys = set()
    for row in old:
        require(set(row) == set(FIELDS) and row['omission_reason'] == '',
                'Malformed row or omission in parent retention table')
        key = (row['checkpoint'], row['archive'], relative(row['original_path']))
        require(key not in keys, 'Duplicate historical logical key: ' + repr(key))
        keys.add(key)
        cp = int(row['checkpoint'])
        require(1 <= cp <= 35 and row['archive'] == f'LM4_SUCCESSOR_checkpoint_{cp:02d}.zip',
                'Incorrect historical archive identity')
        target = metadata.get(relative(row['retained_path']))
        require(target == {'bytes': int(row['bytes']), 'sha256': row['sha256']},
                'Inherited row does not match its actual parent payload: ' + repr(key))
    summary = json.loads(pinned[REWRITTEN[1]])
    require(summary['archives'] == anchor['inherited_archives'] and
            summary['archive_entries'] == len(old) and summary['omissions'] == 0,
            'Pinned parent coverage summary disagrees')
    return metadata, old, pinned


def atomic_write(path, data, replace=False):
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not replace:
        require(path.read_bytes() == data, 'Refusing to overwrite different bytes: ' + str(path))
        return
    fd, name = tempfile.mkstemp(prefix='.' + path.name + '.', dir=path.parent)
    try:
        with os.fdopen(fd, 'wb') as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--parent', type=Path)
    parser.add_argument('--anchor', type=Path)
    parser.add_argument('--commit', action='store_true',
                        help='Publish only after all pinned-parent and current-byte checks pass.')
    args = parser.parse_args()
    require(args.commit, 'No publication without explicit --commit')
    root = args.root.resolve()
    parent = args.parent or root.parent / 'LM4_SUCCESSOR_checkpoint_36.zip'
    anchor_path = args.anchor or root / 'records/checkpoint37_retention_parent_anchor.json'
    anchor, anchor_raw = load_anchor(anchor_path, parent)
    reader_pin = anchor['pinned_files']['code/checkpoint_archive_io.py']
    reader_source = Path(__file__).with_name('checkpoint_archive_io.py').read_bytes()
    require(len(reader_source) == reader_pin['bytes'] and sha(reader_source) == reader_pin['sha256'],
            'Archive reader differs from pinned reviewed36 reader')
    plan, copies = {}, {}

    def choose(rel, data, meta):
        active = local(root, rel)
        if rel not in REWRITTEN and active.is_file() and active.read_bytes() == data:
            target, mode = rel, 'active-identical'
        else:
            target = f'checkpoint_history/checkpoint_36/{rel}'
            path = local(root, target)
            if path.exists():
                require(path.is_file() and path.read_bytes() == data,
                        'Historical path collision: ' + target)
                mode = 'history-identical'
            else:
                copies[target] = data
                mode = 'historical-copy'
        plan[rel] = {'original_path': rel, 'bytes': meta['bytes'],
                     'sha256': meta['sha256'], 'retained_path': target, 'retention': mode}

    map_path = 'records/checkpoint37_parent_entry_map.csv'
    certificate_path = 'records/checkpoint37_inductive_retention.json'
    require(not local(root, map_path).exists() and not local(root, certificate_path).exists(),
            'This capture already has inductive publication records; no blind rerun')
    with CheckpointReader(parent) as reader:
        metadata, old, pinned = checked_parent(reader, anchor, choose)
        # Critical no-loss guard: do not overwrite an unarchived current version.
        for rel in REWRITTEN:
            require(local(root, rel).read_bytes() == pinned[rel],
                    'Current mutable record differs from archived36; preserve it separately first: ' + rel)
        inherited = []
        for row in old:
            new = dict(row)
            new['retained_path'] = plan[row['retained_path']]['retained_path']
            new['retention'] = 'inductive-parent36'
            inherited.append(new)
        require(identities(inherited) == identities(old), 'Historical identity tuple was altered')
        added = [dict(checkpoint='36', archive=parent.name, original_path=rel,
                      bytes=str(meta['bytes']), sha256=meta['sha256'],
                      retained_path=plan[rel]['retained_path'],
                      retention=plan[rel]['retention'], omission_reason='')
                 for rel, meta in sorted(metadata.items())]
        rows = inherited + added
        require(len(rows) == 184942 and len(plan) == 11156,
                'Expected exact36->37 coverage cardinality not met')
        for target, data in copies.items():
            atomic_write(local(root, target), data)
        # Every parent payload is compared byte-for-byte with its future retained target.
        for rel, mapping in plan.items():
            require(local(root, mapping['retained_path']).read_bytes() == reader.read(PREFIX + rel),
                    'Final retained-byte mismatch: ' + rel)
        for rel in REWRITTEN:
            require(local(root, rel).read_bytes() == pinned[rel],
                    'Mutable-record race before publication: ' + rel)

        history = root / 'checkpoint_history'
        historical = [p for p in history.rglob('*') if p.is_file() and p != history / 'README.md']
        now = datetime.now(timezone.utc).isoformat()
        summary = dict(recorded_at=now, archives=36, archive_entries=len(rows), omissions=0,
                       new_historical_copies=len(copies),
                       new_historical_bytes=sum(map(len, copies.values())),
                       total_historical_copies=len(historical),
                       total_historical_bytes=sum(p.stat().st_size for p in historical),
                       audit='Every historical logical key and every parent36 payload is retained.',
                       method='Pinned parent36 identity plus exact inherited-map composition.',
                       scope='Durable checkpoints only; no unarchived lost payload is certified.')
        readme = ("# Exact prior checkpoint versions\n\n"
                  "The authoritative index is records/checkpoint_version_retention.csv.\n"
                  "Every historical logical key remains a distinct row, even when equal bytes share storage.\n"
                  "Checkpoint37 composes the pinned, previously verified36 historical map with a\n"
                  "total byte-checked map on EVERY logical36 entry, including its manifests and maps.\n"
                  "The proof record is records/checkpoint37_inductive_retention.json.\n"
                  "Historical sources are not inputs to the current paper or register.\n"
                  "Unarchived lost versions are not asserted to have been recovered.\n").encode()
        map_data = csv_bytes([plan[k] for k in sorted(plan)], MAP_FIELDS)
        index_data = csv_bytes(rows, FIELDS)
        certificate = dict(schema='checkpoint-inductive-retention-v1', recorded_at=now,
                           adapted_from_reviewed_checkpoint36_source=True, parent_number=36, child_number=37,
                           parent_archive=parent.name, parent_archive_bytes=parent.stat().st_size,
                           parent_archive_sha256=anchor['archive_sha256'], anchor_sha256=sha(anchor_raw),
                           inherited_rows=len(old), parent_logical_entries=len(plan),
                           resulting_rows=len(rows), omissions=0,
                           inherited_tuple_sha256=tuple_sha(old),
                           parent_entry_map_sha256=sha(map_data), retention_csv_sha256=sha(index_data),
                           summary_sha256=sha(json_bytes(summary)), readme_sha256=sha(readme),
                           validation='Pinned parent, complete manifest/bundles, all inherited tuples, and exact target bytes PASS.',
                           earlier_archives_opened=[],
                           limitation='Historical coverage1-35 is the explicitly pinned trusted induction base, not a fresh re-read.')
        atomic_write(local(root, map_path), map_data)
        atomic_write(local(root, REWRITTEN[0]), index_data, replace=True)
        atomic_write(local(root, REWRITTEN[1]), json_bytes(summary), replace=True)
        atomic_write(local(root, REWRITTEN[2]), readme, replace=True)
        # Written last: its presence and hashes commit the three-record publication.
        atomic_write(local(root, certificate_path), json_bytes(certificate))
    print(json.dumps(certificate, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
