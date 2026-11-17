"""Independently verify the CLOSED36 induction step.

Reads only immutable parent35 and child36 archives, plus the pinned anchor;
never trusts the current mutable retention table. No archive1-34 is opened.
The shared reader/validation routines have no import-time mutation.
"""
from pathlib import Path
import argparse
import json

from checkpoint_archive_io import CheckpointReader, PREFIX
from preserve_checkpoint36_versions_inductive import (
    ROOT, REWRITTEN, MAP_FIELDS, require, sha, file_sha, relative, csv_rows,
    identities, tuple_sha, load_anchor, checked_parent, checked_archive,
)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--archive', type=Path, default=ROOT.parent / 'LM4_SUCCESSOR_checkpoint_36.zip')
    parser.add_argument('--parent', type=Path, default=ROOT.parent / 'LM4_SUCCESSOR_checkpoint_35.zip')
    parser.add_argument('--anchor', type=Path, default=ROOT / 'records/checkpoint36_retention_parent_anchor.json')
    args = parser.parse_args()
    require(args.archive.resolve() != args.parent.resolve(), 'Child is the parent archive')
    anchor, anchor_raw = load_anchor(args.anchor, args.parent)
    with CheckpointReader(args.parent) as parent:
        parent_meta, old, _ = checked_parent(parent, anchor)
    with CheckpointReader(args.archive) as child:
        child_meta = checked_archive(child, 36)
        archived_anchor = child.read(PREFIX + 'records/checkpoint36_retention_parent_anchor.json')
        require(archived_anchor == anchor_raw, 'Child does not retain the exact pinned anchor')
        cert = json.loads(child.read(PREFIX + 'records/checkpoint36_inductive_retention.json'))
        require(cert['schema'] == 'checkpoint-inductive-retention-v1' and
                cert['parent_number'] == 35 and cert['child_number'] == 36,
                'Wrong induction certificate')
        require(cert['parent_archive_sha256'] == anchor['archive_sha256'] and
                cert['parent_archive_bytes'] == anchor['archive_bytes'] and
                cert['anchor_sha256'] == sha(anchor_raw), 'Certificate parent/anchor differs')
        map_data = child.read(PREFIX + 'records/checkpoint36_parent_entry_map.csv')
        require(sha(map_data) == cert['parent_entry_map_sha256'], 'Map hash mismatch')
        mapping_rows = csv_rows(map_data)
        mapping = {}
        for row in mapping_rows:
            require(set(row) == set(MAP_FIELDS), 'Malformed parent-entry map')
            rel = relative(row['original_path'])
            require(rel not in mapping, 'Duplicate parent logical path')
            require(parent_meta.get(rel) == {'bytes': int(row['bytes']), 'sha256': row['sha256']},
                    'Map does not match pinned parent bytes: ' + rel)
            target = relative(row['retained_path'])
            require(child_meta.get(target) == parent_meta[rel],
                    'Child target bytes do not retain the parent payload: ' + rel)
            mapping[rel] = row
        require(set(mapping) == set(parent_meta) and len(mapping) == 10746,
                'Parent-entry map is not total on all logical35 entries')
        index_data = child.read(PREFIX + REWRITTEN[0])
        require(sha(index_data) == cert['retention_csv_sha256'], 'Retention index hash mismatch')
        rows = csv_rows(index_data)
        require(len(rows) == 173786 and cert['resulting_rows'] == 173786 and
                cert['inherited_rows'] == 163040 and cert['parent_logical_entries'] == 10746 and
                cert['omissions'] == 0, 'Wrong induction cardinalities')
        inherited, added = rows[:len(old)], rows[len(old):]
        require(identities(inherited) == identities(old) and
                tuple_sha(inherited) == anchor['inherited_tuple_sha256'] == cert['inherited_tuple_sha256'],
                'Historical key/size/hash tuples were dropped, merged or changed')
        for previous, row in zip(old, inherited):
            require(row['retained_path'] == mapping[previous['retained_path']]['retained_path'],
                    'Inherited map is not the exact composition')
        require({r['original_path'] for r in added} == set(parent_meta) and
                len({r['original_path'] for r in added}) == len(added),
                'New35 rows do not cover exactly the parent entries')
        for row in added:
            require(row['checkpoint'] == '35' and row['archive'] == args.parent.name,
                    'Wrong new historical archive key')
            item = mapping[row['original_path']]
            require(int(row['bytes']) == int(item['bytes']) and row['sha256'] == item['sha256'] and
                    row['retained_path'] == item['retained_path'], 'New35 row differs from parent map')
        keys = set()
        for row in rows:
            key = (row['checkpoint'], row['archive'], relative(row['original_path']))
            require(key not in keys and row['omission_reason'] == '', 'Duplicate key or omission')
            keys.add(key)
            require(child_meta.get(relative(row['retained_path'])) ==
                    {'bytes': int(row['bytes']), 'sha256': row['sha256']},
                    'Historical tuple target bytes absent or different in CLOSED child')
        for rel, key in ((REWRITTEN[1], 'summary_sha256'), (REWRITTEN[2], 'readme_sha256')):
            require(sha(child.read(PREFIX + rel)) == cert[key], 'Published record hash mismatch')
        summary = json.loads(child.read(PREFIX + REWRITTEN[1]))
        require(summary['archives'] == 35 and summary['archive_entries'] == len(rows) and
                summary['omissions'] == 0, 'Closed child summary disagrees')
    report = dict(schema='checkpoint-inductive-closed-verification-v1',
                  archive=args.archive.name, bytes=args.archive.stat().st_size,
                  sha256=file_sha(args.archive), parent_sha256=anchor['archive_sha256'],
                  child_logical_entries=len(child_meta), parent_logical_entries=len(parent_meta),
                  inherited_rows=len(old), all_retained_rows=len(rows), omissions=0,
                  manifest_and_three_bundle_bytes='PASS', complete_parent_map='PASS',
                  historical_tuple_composition='PASS', all_closed_child_targets='PASS',
                  earlier_archives_opened=[], mutable_workspace_records_used=False)
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
