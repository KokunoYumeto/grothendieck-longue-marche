"""Authorize one explicitly supplemented, lossless revision after observed cap failure."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import package_checkpoint39_frozen as base

ROOT = Path(__file__).resolve().parents[1]
STAGE = ROOT.parent / '.checkpoint39_stage_ie3483cd'
PRIOR_SHA = 'e797d372a8937b48d5b76c209eb4b881710f364cc56979757bfb909451302102'
TARGET = 'records/checkpoint39_revision_authorized.json'
PAUSES = ['work_A/checkpoint39_revision_pause_receipt.json',
          'work_CE/checkpoint39_revision_pause_receipt.json',
          'work_DE/checkpoint39_revision_pause_receipt.json']


def load(rel):
    return json.loads((ROOT / rel).read_text())


def bind(rel):
    p = ROOT / rel
    assert p.is_file() and not p.is_symlink()
    assert p.resolve().is_relative_to(ROOT.resolve())
    h = hashlib.sha256()
    size = 0
    with p.open('rb') as f:
        for block in iter(lambda: f.read(4 * 1024 * 1024), b''):
            size += len(block)
            h.update(block)
    return {'path': rel, 'bytes': size, 'sha256': h.hexdigest()}


def main():
    now = datetime.now(timezone.utc)
    assert datetime(2026,11,17,18,49,30,tzinfo=timezone.utc) <= now < datetime(2026,11,17,19,49,30,tzinfo=timezone.utc)
    assert not (ROOT.parent / 'LM4_SUCCESSOR_checkpoint_39.zip').exists()
    raw = (STAGE / 'sealed-plan.json').read_bytes()
    assert hashlib.sha256(raw).hexdigest() == PRIOR_SHA
    prior = json.loads(raw)
    assert prior['result'] == 'FAIL_EXACT_CAP' and not prior['archive_created']
    assert prior['layout']['exact_zip_bytes'] == 547320902
    observation = load('records/checkpoint39_first_prepare_observed.json')
    assert observation['actual_tool_result_observed'] is True
    assert observation['actual_exit_code'] == 1 and observation['actual_completion_tool_chunk'] == '7179ef'
    old = load('records/checkpoint39_frozen_inputs_authorized.json')
    for row in old['bindings'] + [old['final_pdf'], old['retention_ledger']]:
        assert bind(row['path']) == row, row['path']
    expected_agents = {'/root/involutions', '/root/torus_real', '/root/topology_census'}
    found = set()
    for rel in PAUSES:
        pause = load(rel)
        assert pause['paused'] is True and pause['owned_live_producers'] == []
        stamp = datetime.fromisoformat(pause['paused_at'])
        assert stamp.tzinfo and stamp <= now and stamp > datetime(2026,11,17,19,31,tzinfo=timezone.utc)
        found.add(pause['agent'])
    assert found == expected_agents
    snapshot = json.loads((STAGE / 'snapshot.json').read_text())
    original = {x['path'] for x in snapshot['logical_rows_before_generated']} | set(base.GENERATED)
    supplements = []
    for p in sorted(ROOT.rglob('*')):
        if p.is_file() and not base.exclusion_reason(p):
            rel = p.relative_to(ROOT).as_posix()
            if rel not in original and rel != TARGET:
                assert p.suffix.lower() not in {'.png','.pdf','.tar'}
                supplements.append(rel)
    assert 'code/authorize_checkpoint39_revision.py' in supplements
    assert 'records/checkpoint39_first_prepare_observed.json' in supplements
    assert 'records/checkpoint39_revision_root_source_review.json' in supplements
    for rel in PAUSES:
        assert rel in supplements
    previous = {x['path']: x for x in old['bindings']}
    previous.update({rel: bind(rel) for rel in supplements})
    out = {'checkpoint':39, 'result':'PASS_FROZEN_INPUTS_AUTHORIZED',
           'recorded_at':datetime.now(timezone.utc).isoformat(), 'authorizer':'/root',
           'final_pdf':old['final_pdf'], 'retention_ledger':old['retention_ledger'],
           'bindings':[previous[p] for p in sorted(previous)],
           'pause_receipts':[bind(p) for p in PAUSES],
           'revision':{'kind':'DATA512_FAMILY_RESEAL', 'predecessor_stage':str(STAGE),
                       'predecessor_plan_sha256':PRIOR_SHA, 'actual_prior_prepare_exit_code':1,
                       'actual_prior_prepare_tool_chunk':'7179ef', 'supplements':supplements,
                       'document_search_revision_allowed':True,
                       'document_search_scope':'Same frozen raw TAR and256MiB decoder property; separately observed stronger encode/decode, smaller verified stream selection, original stream retained.'},
           'open_not_before':'2026-11-17T18:49:30+00:00',
           'open_before':'2026-11-17T19:49:30+00:00', 'archive_cap_bytes':536870912,
           'old_bound_sources_and_mathematical_deliverables_unchanged':True,
           'capture38_exit_code':None, 'future_prepare_or_archive_success_claimed':False}
    with (ROOT / TARGET).open('x') as f:
        json.dump(out,f,indent=2)
        f.write('\n')
    print(json.dumps({'result':out['result'],'authorization':bind(TARGET),
                      'supplement_count':len(supplements),'supplements':supplements,
                      'future_success_claimed':False},indent=2))


if __name__ == '__main__':
    main()
