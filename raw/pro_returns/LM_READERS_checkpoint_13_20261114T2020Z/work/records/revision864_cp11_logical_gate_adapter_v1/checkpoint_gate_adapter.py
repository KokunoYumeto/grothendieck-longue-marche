#!/usr/bin/env python3
"""Explicit post-CP11 executor correcting only the captured logical-path lookup.

The original integrator/proposal/checkpoint remain byte-identical. This adapter is
new evidence, not a file represented as present in CP11. It delegates unchanged
installation operations only after the original gate, with one bounded lookup
substitution, passes. No original, snapshot, compiler, receipt, or recovery check
is removed.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import importlib.util
import inspect
import json
from pathlib import Path
import sys

ORIGINAL = 'work/scripts/integrate_revision864_residuals.py'
ORIGINAL_SHA = '9bc6751a2449c0338a06c89dd50bf4c2a137df326b954929d5134fcc152b741c'
PROPOSAL = 'work/layout_probes/revision864_residual_staged_v3/proposal.json'
PROPOSAL_SHA = '8465589edcf8402b934f3edd85361c05835b6635b8dcd836da733c42cea82759'
SNAPSHOT = 'work/data/audit_history/revision864_selected_discovery_v3/SNAPSHOT_COMPLETE.json'
SNAPSHOT_SHA = '10799f0becc035f2159da796d8da42b8423f03f0c433cc53ffd32e7b6d2b3ed9'
ARCHIVE = 'deliverables/LM_READERS_checkpoint_11.zip'
ARCHIVE_SHA = '1df3f32c9f47dcbadbf4546f10f8866faf7084f6ded8f9c221e98f1e41512f51'
CLASSIFICATION_SHA = 'd57ade078fb94fa5cfe7c0b3114da8fd15d5c74f9b314f9572d046f6eec811ed'
CLASSIFICATION_BYTES = 808739
OLD_SPAN = """            if expected is not None:
                assert logical[name]['sha256'] == expected['sha256'] and int(logical[name]['bytes']) == expected['bytes'], name
"""
NEW_SPAN = """            if expected is not None:
                _cp11_require_archived_identity(container, logical, row, expected, index)
"""


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def digest(path):
    with Path(path).open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def artifact(path, root):
    path = Path(path).resolve()
    ref = dict(artifact=path.name, sha256=digest(path), bytes=path.stat().st_size)
    if path.is_relative_to(root):
        ref['path'] = path.relative_to(root).as_posix()
    return ref


class CapturedLookup:
    """Closed row-index/name mapping; no hash search or generalized fallback."""
    def __init__(self, qualification):
        rows = qualification['rows']
        self.allowed = {row['original_path']: row for row in rows}
        require(len(rows) == len(self.allowed) == 950, 'Closed mapping must contain exactly 950 unique names')
        require(len({row['snapshot_file_index'] for row in rows}) == 950, 'Repeated snapshot file index')
        self.used = set()
        self.direct = 0
        self.objects = set()

    def __call__(self, container, logical, row, expected, index):
        name = row['original_path']
        if name in logical:
            require(name not in self.allowed, 'An explicitly absent original is unexpectedly present')
            present = logical[name]
            require((present['sha256'], int(present['bytes'])) ==
                    (expected['sha256'], expected['bytes']), 'Present original logical identity differs: ' + name)
            self.direct += 1
            return
        require(name in self.allowed, 'Unqualified absent original logical path: ' + name)
        approved = self.allowed[name]
        require(index == approved['snapshot_file_index'], 'Captured mapping index differs: ' + name)
        require(row['snapshot_path'] == approved['snapshot_path'], 'Captured mapping path differs: ' + name)
        identity = (approved['sha256'], approved['bytes'])
        require(identity == (row['sha256'], row['bytes']) ==
                (row['snapshot_sha256'], row['snapshot_bytes']) ==
                (expected['sha256'], expected['bytes']), 'Original/captured/packaged identity differs: ' + name)
        captured = logical[row['snapshot_path']]
        require((captured['sha256'], int(captured['bytes'])) == identity,
                'Captured archive logical identity differs: ' + name)
        require(captured['storage_kind'] == approved['logical_storage_kind'],
                'Captured archive storage kind differs: ' + name)
        canonical = logical[captured['target_path']] if captured['storage_kind'] == 'alias' else captured
        require(canonical['storage_kind'] == 'blob' and canonical['path'] == approved['canonical_logical_path'],
                'Captured payload is not the qualified primitive or one-hop alias: ' + name)
        require((canonical['sha256'], int(canonical['bytes'])) == identity and
                canonical['object_path'] == approved['archive_object_path'],
                'Captured primitive object differs: ' + name)
        key = (canonical['object_path'], *identity)
        if key not in self.objects:
            info = container.getinfo(canonical['object_path'])
            require(info.file_size == identity[1] and not info.flag_bits & 1,
                    'Captured primitive ZIP header differs: ' + name)
            data = container.read(canonical['object_path'])
            require((sha(data), len(data)) == identity, 'Captured primitive bytes differ: ' + name)
            self.objects.add(key)
        require(name not in self.used, 'Captured mapping was applied twice: ' + name)
        self.used.add(name)


def load_adapter(root, evidence):
    root = Path(root).resolve()
    evidence = Path(evidence).resolve()
    qualification_path = evidence / 'CLASSIFICATION.json'
    raw = qualification_path.read_bytes()
    require((sha(raw), len(raw)) == (CLASSIFICATION_SHA, CLASSIFICATION_BYTES), 'Qualification bytes differ')
    qualification = json.loads(raw)
    require(qualification['status'] == 'EXACT_BYTES_PASS_GATE_CORRECTION_NOT_EXECUTED', 'Wrong qualification status')
    fixed = {
        'original_integrator': (ORIGINAL, ORIGINAL_SHA),
        'proposal': (PROPOSAL, PROPOSAL_SHA),
        'snapshot': (SNAPSHOT, SNAPSHOT_SHA),
        'archive': (ARCHIVE, ARCHIVE_SHA),
    }
    for label, (name, expected) in fixed.items():
        ref = qualification['inputs'][label]
        require(ref['path'] == name and ref['sha256'] == expected, 'Qualification identity differs: ' + label)
        require(digest(root / name) == expected and (root / name).stat().st_size == ref['bytes'],
                'Current qualified input differs: ' + name)
    recovery = qualification['inputs']['full_recovery']
    require(digest(root / recovery['path']) == recovery['sha256'] and
            (root / recovery['path']).stat().st_size == recovery['bytes'], 'Full recovery evidence differs')
    snapshot = json.loads((root / SNAPSHOT).read_bytes())
    require(len(snapshot['files']) == qualification['snapshot_files'] == 3133, 'Snapshot scope differs')
    for approved in qualification['rows']:
        row = snapshot['files'][approved['snapshot_file_index']]
        require(all(row[key] == approved[key] for key in ('original_path', 'snapshot_path', 'sha256', 'bytes')),
                'Qualification does not identify its exact captured source row')
        require((row['snapshot_sha256'], row['snapshot_bytes']) == (approved['sha256'], approved['bytes']),
                'This absent-path correction accepts exact-byte captures only')
    sys.path.insert(0, str(root / 'work/scripts'))
    spec = importlib.util.spec_from_file_location('revision864_original_integrator_for_captured_gate', root / ORIGINAL)
    original = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(original)
    require(original.ROOT == root, 'Original integrator project root differs')
    before = inspect.getsource(original.checkpoint_gate)
    require(before.count(OLD_SPAN) == 1, 'The original gate lookup span differs')
    after = before.replace(OLD_SPAN, NEW_SPAN, 1)
    require(after.replace(NEW_SPAN, OLD_SPAN, 1) == before, 'Gate substitution is not exactly reversible')
    # Every other original module AST node/function remains the loaded original.
    require(len(ast.parse(after).body) == 1 and isinstance(ast.parse(after).body[0], ast.FunctionDef),
            'Gate substitution unexpectedly introduces another definition')
    exec(compile(after, '<explicit-post-cp11-captured-path-gate>', 'exec'), original.__dict__)
    corrected = original.checkpoint_gate

    def gate(stage, proposal, snapshot_path, archive_path):
        require(Path(stage).resolve() == (root / PROPOSAL).parent and
                Path(snapshot_path).resolve() == root / SNAPSHOT and
                Path(archive_path).resolve() == root / ARCHIVE, 'This supplement is scoped to proposal v3 / snapshot v3 / CP11')
        require(digest(root / ORIGINAL) == ORIGINAL_SHA and digest(root / PROPOSAL) == PROPOSAL_SHA,
                'Original helper/proposal changed before gate')
        # The old gate still verifies all current originals, captured records,
        # seven-log privacy, receipts/recovery, PDFs, images and direct names.
        lookup = CapturedLookup(qualification)
        original.__dict__['_cp11_require_archived_identity'] = lookup
        result = corrected(stage, proposal, snapshot_path, archive_path)
        require(lookup.used == set(lookup.allowed), 'Not every qualified absent path was checked')
        require(len(lookup.objects) == qualification['unique_archived_primitive_payloads_checked'],
                'Primitive payload coverage differs')
        require(digest(root / ARCHIVE) == ARCHIVE_SHA and digest(root / SNAPSHOT) == SNAPSHOT_SHA,
                'Checkpoint/snapshot changed during supplemental gate')
        result['post_checkpoint_logical_path_supplement'] = dict(
            schema='revision864-cp11-captured-logical-path-gate-supplement-v1', status='PASS',
            provenance='POST_CHECKPOINT_EXECUTOR_NOT_INCLUDED_IN_CP11',
            adapter=artifact(Path(__file__), root), qualification=artifact(qualification_path, root),
            original_integrator=qualification['inputs']['original_integrator'],
            original_proposal=qualification['inputs']['proposal'],
            original_checkpoint_gate_sha256=sha(before.encode()),
            corrected_checkpoint_gate_sha256=sha(after.encode()),
            change='Only the exact original logical-name assertion is delegated to the closed captured-path lookup; all other original gate and installation code remains unchanged.',
            qualified_absent_names=len(lookup.used), direct_original_names_checked=lookup.direct,
            archived_primitive_payloads_rehashed=len(lookup.objects),
            original_current_and_captured_validation_retained=True,
            present_original_mismatch_is_error=True, arbitrary_same_hash_search=False,
            new_executor_claimed_inside_checkpoint=False, new_visual_review_claims=False)
        return result

    original.checkpoint_gate = gate
    return original


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=('checkpoint-check', 'commit'))
    parser.add_argument('--project-root', type=Path, default=Path.cwd())
    args = parser.parse_args()
    root = args.project_root.resolve()
    evidence = Path(__file__).resolve().parent
    if args.command == 'commit':
        require(evidence.is_relative_to(root), 'Commit requires the reviewed supplement to be retained under the project root')
    module = load_adapter(root, evidence)
    stage = (root / PROPOSAL).parent
    if args.command == 'checkpoint-check':
        result = module.checkpoint_gate(stage, module.load_proposal(stage), root / SNAPSHOT, root / ARCHIVE)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        result = module.commit(stage, root / SNAPSHOT, root / ARCHIVE)
        print(json.dumps({key: result[key] for key in ('status', 'base_records', 'expected_records', 'actual_records')}, ensure_ascii=False))


if __name__ == '__main__':
    main()
