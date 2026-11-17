"""One scheduled recovery32 capture; never creates a test or catch-up archive.

The scheduled progress review is recorded when due. If final verification
is still running, wait for root's completed readiness record before the
single capture. A readiness record is evidence of finished work, not a
request for user permission. Every actual timestamp is recorded honestly.
"""
from pathlib import Path
from datetime import datetime, timezone
import json, subprocess, sys, time

def main():
    root=Path(__file__).resolve().parents[1]
    due=datetime(2026,11,17,10,49,30,tzinfo=timezone.utc)
    next_due=datetime(2026,11,17,11,49,30,tzinfo=timezone.utc)
    archive=root.parent/'LM4_SUCCESSOR_checkpoint_32.zip'
    assert not archive.exists()
    remaining=(due-datetime.now(timezone.utc)).total_seconds()
    assert remaining<=60,'Start only within the scheduled minute or later in this slot.'
    assert datetime.now(timezone.utc)<next_due,'No off-cycle or later catch-up invocation.'
    while datetime.now(timezone.utc)<due:
        time.sleep(.5)
    reviewed=datetime.now(timezone.utc)
    scheduled=root/'records/checkpoint32_scheduled_review.json'
    assert not scheduled.exists(),'Preserve an earlier attempt before diagnosing it.'
    scheduled.write_text(json.dumps({'scheduled_at':due.isoformat(),'recorded_at':reviewed.isoformat(),
        'decision':'CONTINUE','reason':'Actual full-GT affine finite-image hexagon gate closed; full main and CM comparisons still require research.',
        'archive_created_by_this_review':False,'next_scheduled_at':next_due.isoformat()},indent=2)+'\n')
    print('Scheduled32 progress review',reviewed.isoformat(),'CONTINUE',flush=True)
    last=0
    while not (root/'records/checkpoint32_capture_ready.json').exists():
        assert datetime.now(timezone.utc)<next_due,'Readiness not reached in this slot; no catch-up ZIP.'
        if time.monotonic()-last>25:
            print('Waiting for actual final verification/readiness; no ZIP opened.',flush=True);last=time.monotonic()
        time.sleep(.5)
    subprocess.run([sys.executable,str(root/'code/check_checkpoint32_preconditions.py')],check=True)
    now=datetime.now(timezone.utc)
    assert now<next_due
    m=json.loads((root/'records/checkpoint32_metrics.json').read_text())
    review=f'''# Thirty-second scheduled progress review and immutable capture

Scheduled review:{due.isoformat()}.
Actual review:{reviewed.isoformat()}.
Actual capture preparation:{now.isoformat()}.
Decision: CONTINUE. Next scheduled review:{next_due.isoformat()}.

The actual rebuilt paper has{m['pages']} pages and347 statements:
303 Proved,19 Refuted,19 Open,6 Known;115 references and49 task rows.
PDF bytes:{m['pdf_bytes']}; SHA256:{m['pdf_sha256']}.
All14 reconstructed formal sources and every new mathematical page have
fresh reviews bound to the current bytes. Lost pre-outage sources/PDFs
are identified explicitly and are not claimed recovered. Main A, Main B,
and the actual CM parity comparison remain Open. The new full affine
pentagon proof closes the original signed mod3/mod12 hexagon-image gate,
with its precise full-GT specialization and no full-word inference.

The08:49:30 and09:49:30 slots were missed during the unavailable execution
environment. No catch-up or test archive was made. This is the single32
capture for the present scheduled review. The pinned31 induction retains
all9388 parent logical entries and all123532 prior historical identities,
with132920 resulting rows and zero omissions. Native three-TAR restoration
and closed-child verifiers follow actual closure before delivery.

The exact recovery, research and computation reports follow.
'''
    for rel in ['records/thirty_second_hour_research_report.md','records/checkpoint32_computation_audit_state.md']:
        review+='\n'+(root/rel).read_text()
    target=root/'records/progress_review_32h.md';assert not target.exists();target.write_text(review)
    for rel,heading in [('LM4_SUCCESSOR_report.md','Thirty-second-hour progress review'),('records/continuation_state.md','Actual thirty-second-hour review')]:
        p=root/rel;s=p.read_text();assert '## '+heading+'\n' not in s
        p.write_text(s+'\n## '+heading+'\n\n'+
            f'CONTINUE at scheduled review{reviewed.isoformat()}; capture preparation{now.isoformat()}. '
            f'Fresh reconstructed347-statement paper,{m["pages"]} pages,115 references,49 tasks. '
            'Both main decisions and actual CM parity remain Open. The signed mod3/mod12 hexagon image is proved in the retained affine research source. '
            'Release all writers immediately after the one immutable capture closes, before verification or saving. '
            'Verify complete logical coverage, the exact inherited map, and all three native TAR restorations/actual dictionary streams. '
            'Next review:2026-11-17 11:49:30 UTC.\n')
    subprocess.run([sys.executable,str(root/'code/refresh_computation_inventory.py')],check=True)
    with (root/'records/checkpoint32_version_retention_run.out').open('x') as out:
        subprocess.run([sys.executable,str(root/'code/preserve_checkpoint_versions_inductive.py'),'--commit'],stdout=out,check=True)
    retained=json.loads((root/'records/checkpoint_version_retention_summary.json').read_text())
    assert retained['archives']==31 and retained['archive_entries']==132920 and retained['omissions']==0
    print('Opening sole immutable32 ZIP after retained-byte validation',datetime.now(timezone.utc).isoformat(),flush=True)
    subprocess.run([sys.executable,str(root/'code/package_checkpoint.py'),'32'],check=True)
    assert archive.stat().st_size<=536870912,'Never mutate an already captured archive.'
    print('Immutable32 capture completed',datetime.now(timezone.utc).isoformat(),flush=True)

if __name__=='__main__':
    main()
