"""Record the root's completed source readings before the final40 input freeze.

This recorder does not authorize, prepare, encode, assemble, or verify an archive.
"""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
NEW = {
    'code/record_checkpoint40_delivery_scope.py': '6204dc68fab74e96ca5f6be469f64258cad49e53907329ce3a8f2951df7f449f',
    'code/authorize_checkpoint40_final.py': 'f4d700a67ef249dd5fa47bc92b69be4473f5abeaa71e333c4a9a5dbaf9ca418d',
    'code/package_checkpoint40_frozen.py': 'e9623e56b2a82fb78e7b3653ab794bbc7413246f1e928665c331ba70f37803b3',
    'code/checkpoint40_filtered_prepare.py': 'dc656935b7abe7102266931e0f1ebda967b77fbd88d0bfdc2e6b081f368fc301',
    'code/verify_checkpoint40_snapshot.py': 'eba50bda9445dba7fe1fe5c08e9a01fb8c6e19717b17b24cbcfe9df460d231f0',
    'code/verify_checkpoint40_system_tars.py': '7b80d8d1ac7334c991980a11aef9e6656376f421af37d0e60c56e4f1493451c4',
    'code/verify_checkpoint40_retention.py': '5a8cf8df60b6f4d12cfa28421e55ccdfa262c88e87f3e3b5ce418c80913beb9e',
}
OLD = {
    'code/checkpoint39_retention_common.py': 'e02c9c602920dcdef1523c0328cfe10e4d05fab388136d69689b41eebf937c2d',
    'code/compose_checkpoint39_frozen_retention.py': '805aa672a42620660daed6fef4217ea9e78b01ebe71ba96571cf597435945eed',
    'code/verify_checkpoint39_snapshot.py': '43788390861fd6a2bf54c75ece3cd3e781a451ef3c724e486698e7e370dbe62e',
    'code/verify_checkpoint39_system_tars.py': 'c31ad84cae128135527d30df2a12000413105828df94282f1ee47cf224e789df',
    'code/verify_checkpoint39_retention.py': '638abd65162f0661489d4921c24429d40ba357c3b0b87d3a3a98f28242e3b27a',
}
EVIDENCE = [
    'records/checkpoint40_filtered_source_manifest.json',
    'records/checkpoint40_verifier_source_manifest.json',
    'work_DE/review_checkpoint40_pipeline_and_authorizer.md',
    'work_DE/review_checkpoint40_pipeline_and_authorizer.json',
    'work_DE/review_checkpoint40_delivery_scope_source.json',
    'work_DE/review_checkpoint40_verifier_sources.md',
    'work_DE/review_checkpoint40_verifier_sources.json',
    'records/checkpoint40_delivery_scope.json',
    'records/checkpoint40_approved_derivative_omissions.csv',
    'LM4_SUCCESSOR_final_delivery_report.md',
    'work_A/checkpoint40_final_pause_receipt.json',
    'work_CE/checkpoint40_final_pause_receipt.json',
    'work_DE/checkpoint40_final_pause_receipt.json',
]


def binding(rel):
    path = ROOT / rel
    assert path.is_file() and not path.is_symlink()
    raw = path.read_bytes()
    return {'path': rel, 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}


def main():
    for rel, expected in {**NEW, **OLD}.items():
        assert binding(rel)['sha256'] == expected, rel
    assert not (ROOT.parent / 'LM4_SUCCESSOR_checkpoint_39.zip').exists()
    assert not (ROOT.parent / 'LM4_SUCCESSOR_checkpoint_40.zip').exists()
    scope = json.loads((ROOT / 'records/checkpoint40_delivery_scope.json').read_text())
    assert scope['approved_omissions'] == 59 and scope['historical_omissions'] == 0
    assert scope['historical_identity_rows_checked'] == [196804, 12502]
    inventory_rel = 'records/checkpoint40_computation_inventory_addendum.csv'
    inventory_sources = sorted([*NEW, 'code/record_checkpoint40_root_source_review.py'])
    with (ROOT / inventory_rel).open('x', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=['path', 'bytes', 'sha256', 'scope'])
        writer.writeheader()
        for rel in inventory_sources:
            writer.writerow(dict(binding(rel), scope='Final40 delivery source; no mathematical status inferred from presence.'))
    record = {
        'result': 'PASS_COMPLETE_ROOT_SOURCE_REVIEW_NO_ARCHIVE_EXECUTION',
        'reviewer': '/root', 'recorded_at': datetime.now(timezone.utc).isoformat(),
        'reviewed_sources': [binding(p) for p in sorted(NEW)],
        'recorder_source': binding('code/record_checkpoint40_root_source_review.py'),
        'unchanged_certificate_sources': [binding(p) for p in sorted(OLD)],
        'evidence_bindings': [binding(p) for p in EVIDENCE],
        'computation_inventory_addendum': binding(inventory_rel),
        'entire_root_reads': {
            'assembler_and_filtered_prepare': ['943a54', 'b2de22'],
            'generic_verifier': ['037655'],
            'native_verifier': ['62be24'],
            'retention_verifier': ['32d9e5'],
            'authorizer_and_all_peer_receipts_and_pauses': ['f240ac', '594b1f'],
            'scope_producer': 'Root authored full source; DE entire independent review ecb14c.',
            'this_recorder': 'Root authored full source; metadata recording only.'},
        'scope_producer_observation': {'actual_exit_code': 0, 'completion_tool_chunk': '43a1dd',
                                       'complete_output_and_scope_read': '344819'},
        'truncated_prior_retention_read_counted': False,
        'approved_current_derivative_omissions': 59,
        'historical_omissions': 0, 'historical_identity_rows': [196804, 12502],
        'archive_cap_bytes': 536870912,
        'opening_window': ['2026-11-17T19:49:30+00:00', '2026-11-17T20:49:30+00:00'],
        'mathematical_exploration_stopped': True,
        'future_authorization_preparation_or_archive_success_claimed': False,
        'closed_archive_verifier_runs_remain_required': 3,
    }
    target = ROOT / 'records/checkpoint40_root_source_review.json'
    with target.open('x') as stream:
        json.dump(record, stream, indent=2); stream.write('\n')
    print(json.dumps({'result': record['result'], 'record': binding(target.relative_to(ROOT).as_posix()),
                      'inventory': binding(inventory_rel)}, indent=2))


if __name__ == '__main__':
    main()
