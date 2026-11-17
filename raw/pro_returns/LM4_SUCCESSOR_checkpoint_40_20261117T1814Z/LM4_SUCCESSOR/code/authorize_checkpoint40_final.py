"""Authorize the exact documented derivative exclusions in a distinct hourly slot."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import package_checkpoint39_frozen as prior_policy

ROOT = Path(__file__).resolve().parents[1]
FIRST = ROOT.parent / '.checkpoint39_stage_ie3483cd'
SECOND = ROOT.parent / '.checkpoint39_stage_revision_9gl459jj'
FIRST_SHA = 'e797d372a8937b48d5b76c209eb4b881710f364cc56979757bfb909451302102'
SECOND_SHA = '6813d72b14ace12d6c2c15c2739551d65761655fa2b862597beb84869595319b'
OMISSIONS = 'records/checkpoint40_approved_derivative_omissions.csv'
OMISSIONS_SHA = '947c60823e46447a8eb3d3306d0ab07b9e63e1afd03cb160d71b76f772c4f615'
TARGET = 'records/checkpoint40_final_authorized.json'
PAUSES = ['work_A/checkpoint40_final_pause_receipt.json',
          'work_CE/checkpoint40_final_pause_receipt.json',
          'work_DE/checkpoint40_final_pause_receipt.json']


def load(rel):
    return json.loads((ROOT / rel).read_text())


def binding(rel):
    p = ROOT / rel
    assert p.is_file() and not p.is_symlink() and p.resolve().is_relative_to(ROOT.resolve())
    h, size = hashlib.sha256(), 0
    with p.open('rb') as f:
        for block in iter(lambda: f.read(4 * 1024 * 1024), b''):
            h.update(block); size += len(block)
    return {'path':rel, 'bytes':size, 'sha256':h.hexdigest()}


def main():
    now = datetime.now(timezone.utc)
    assert datetime(2026,11,17,19,49,30,tzinfo=timezone.utc) <= now < datetime(2026,11,17,20,49,30,tzinfo=timezone.utc)
    assert not (ROOT.parent / 'LM4_SUCCESSOR_checkpoint_39.zip').exists()
    assert not (ROOT.parent / 'LM4_SUCCESSOR_checkpoint_40.zip').exists()
    for stage, expected, size in [(FIRST,FIRST_SHA,547320902),(SECOND,SECOND_SHA,548237023)]:
        raw = (stage / 'sealed-plan.json').read_bytes()
        assert hashlib.sha256(raw).hexdigest() == expected
        plan = json.loads(raw)
        assert plan['result'] == 'FAIL_EXACT_CAP' and not plan['archive_created']
        assert plan['layout']['exact_zip_bytes'] == size
        assert not (stage / 'assembly-open-attempt.json').exists()
    first = load('records/checkpoint39_first_prepare_observed.json')
    scope = load('records/checkpoint40_delivery_scope.json')
    assert first['actual_tool_result_observed'] and first['actual_exit_code'] == 1
    assert first['actual_completion_tool_chunk'] == '7179ef'
    assert scope['second_prepare']['actual_exit_code'] == 1
    assert scope['second_prepare']['completion_chunk'] == '5e4aee'
    assert scope['approved_omissions'] == 59 and scope['historical_omissions'] == 0
    assert scope['historical_identity_rows_checked'] == [196804,12502]
    assert binding(OMISSIONS)['sha256'] == OMISSIONS_SHA
    omitted = list(csv.DictReader((ROOT / OMISSIONS).open()))
    assert len(omitted) == 59 and len({r['path'] for r in omitted}) == 59
    assert sum(int(r['bytes']) for r in omitted) == 20053999
    assert sum(r['path'].endswith('.png') for r in omitted) == 58
    assert all(r['reason'] and r['superseded_by'] == 'LM4_SUCCESSOR_paper.pdf' and r['regeneration_recipe'] for r in omitted)
    old = load('records/checkpoint39_frozen_inputs_authorized.json')
    for row in old['bindings'] + [old['final_pdf'],old['retention_ledger']]:
        assert binding(row['path']) == row, row['path']
    agents = set()
    for rel in PAUSES:
        pause = load(rel)
        assert pause['paused'] is True and pause['owned_live_producers'] == []
        stamp = datetime.fromisoformat(pause['paused_at'])
        assert stamp.tzinfo and datetime(2026,11,17,19,45,tzinfo=timezone.utc) < stamp <= now
        agents.add(pause['agent'])
    assert agents == {'/root/involutions','/root/torus_real','/root/topology_census'}
    snap = json.loads((FIRST / 'snapshot.json').read_text())
    original = {r['path'] for r in snap['logical_rows_before_generated']} | set(prior_policy.GENERATED)
    supplements = []
    for p in sorted(ROOT.rglob('*')):
        if p.is_file() and prior_policy.exclusion_reason(p) is None:
            rel = p.relative_to(ROOT).as_posix()
            if rel not in original and rel != TARGET:
                assert p.suffix.lower() not in {'.png','.pdf','.tar'}
                supplements.append(rel)
    for rel in PAUSES + ['code/authorize_checkpoint40_final.py',
                        'code/package_checkpoint40_frozen.py','code/checkpoint40_filtered_prepare.py',
                        'records/checkpoint40_root_source_review.json',OMISSIONS,
                        'LM4_SUCCESSOR_final_delivery_report.md']:
        assert rel in supplements, rel
    bindings = {r['path']:r for r in old['bindings']}
    bindings.update({p:binding(p) for p in supplements})
    out = {'checkpoint':40,'result':'PASS_FROZEN_INPUTS_AUTHORIZED','authorizer':'/root',
           'recorded_at':datetime.now(timezone.utc).isoformat(),
           'final_pdf':old['final_pdf'],'retention_ledger':old['retention_ledger'],
           'bindings':[bindings[p] for p in sorted(bindings)],
           'pause_receipts':[binding(p) for p in PAUSES],
           'revision':{'kind':'APPROVED_DERIVATIVE_OMISSIONS_40',
                       'predecessor_stage':str(FIRST),'predecessor_plan_sha256':FIRST_SHA,
                       'actual_prior_prepare_exit_code':1,'actual_prior_prepare_tool_chunk':'7179ef',
                       'failed_revision_stage':str(SECOND),'failed_revision_plan_sha256':SECOND_SHA,
                       'actual_revision_prepare_exit_code':1,'actual_revision_prepare_tool_chunk':'5e4aee',
                       'omissions_csv':binding(OMISSIONS),'supplements':supplements},
           'open_not_before':'2026-11-17T19:49:30+00:00',
           'open_before':'2026-11-17T20:49:30+00:00','archive_cap_bytes':536870912,
           'approved_current_derivative_omissions':59,'historical_omissions':0,
           'mathematical_exploration_stopped':True,'capture38_exit_code':None,
           'future_prepare_or_archive_success_claimed':False}
    with (ROOT / TARGET).open('x') as f:
        json.dump(out,f,indent=2); f.write('\n')
    print(json.dumps({'result':out['result'],'authorization':binding(TARGET),
                      'supplements':supplements,'future_success_claimed':False},indent=2))


if __name__ == '__main__':
    main()
