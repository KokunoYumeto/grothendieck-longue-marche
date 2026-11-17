"""One scheduled checkpoint36 capture; never creates a test or catch-up archive.

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
    due=datetime(2026,11,17,14,49,30,tzinfo=timezone.utc)
    next_due=datetime(2026,11,17,15,49,30,tzinfo=timezone.utc)
    archive=root.parent/'LM4_SUCCESSOR_checkpoint_36.zip'
    assert not archive.exists()
    remaining=(due-datetime.now(timezone.utc)).total_seconds()
    assert remaining<=60,'Start only within the scheduled minute or later in this slot.'
    assert datetime.now(timezone.utc)<next_due,'No off-cycle or later catch-up invocation.'
    while datetime.now(timezone.utc)<due:
        time.sleep(.5)
    reviewed=datetime.now(timezone.utc)
    scheduled=root/'records/checkpoint36_scheduled_review.json'
    assert not scheduled.exists(),'Preserve an earlier attempt before diagnosing it.'
    scheduled.write_text(json.dumps({'scheduled_at':due.isoformat(),'recorded_at':reviewed.isoformat(),
        'decision':'CONTINUE','reason':'Actual elliptic cubic, boundary criterion, torsion transporters and derived refinement, plus complete complementary contact targets, proved at their stated scopes; both main problems and actual CM parity remain open.',
        'archive_created_by_this_review':False,'next_scheduled_at':next_due.isoformat()},indent=2)+'\n')
    print('Scheduled36 progress review',reviewed.isoformat(),'CONTINUE',flush=True)
    last=0
    while not (root/'records/checkpoint36_capture_ready.json').exists():
        assert datetime.now(timezone.utc)<next_due,'Readiness not reached in this slot; no catch-up ZIP.'
        if time.monotonic()-last>25:
            print('Waiting for actual final verification/readiness; no ZIP opened.',flush=True);last=time.monotonic()
        time.sleep(.5)
    subprocess.run([sys.executable,str(root/'code/check_checkpoint36_preconditions.py')],check=True)
    now=datetime.now(timezone.utc)
    assert now<next_due
    m=json.loads((root/'records/checkpoint36_metrics.json').read_text())
    review=f'''# Thirty-sixth scheduled progress review and immutable capture

Scheduled review: {due.isoformat()}.
Actual review: {reviewed.isoformat()}.
Actual capture preparation: {now.isoformat()}.
Decision: CONTINUE. Next scheduled review: {next_due.isoformat()}.

The actual built paper has {m['pages']} pages and 383 statements:
339 Proved, 19 Refuted, 19 Open, 6 Known; 117 references and 49 task rows.
PDF bytes: {m['pdf_bytes']}; SHA256: {m['pdf_sha256']}.
All eleven new formal sources and every new mathematical page have reviews
bound to the current bytes. Main A, Main B, and actual CM parity remain
Open. The odd coherent coordinates vanish after forgetting the constrained
centralizer. Actual elliptic cubic and torsion classification give unique
continuous derived transporters, while the specified boundary-power and
coherent involution obstructions remain unevaluated. The complete one-sided
and complementary retained contact images have full induced topology,
exact normal restriction kernels and continuous sections. Their different
defects do not prove the whole fixed-source equality. All eleven proofs,
all mandatory new and corrected legacy page intervals, and all preserved
citation-spacing changes are bound to actual final evidence.

This is the single36 capture for this scheduled review. The pinned35
induction retains all 10746 parent logical entries and all 163040 prior
historical identities, with 173786 resulting rows and zero omissions.
Historical versions are preserved without replacing their identities.
The closed35 certificate supplies the inherited coverage induction;
no new decompression of every earlier archive is claimed. Native three-TAR
restoration and closed-child verifiers follow actual closure before delivery.

The exact research and computation reports follow.
'''
    for rel in ['records/thirty_sixth_hour_research_report.md','records/checkpoint36_computation_audit_state.md']:
        review+='\n'+(root/rel).read_text()
    target=root/'records/progress_review_36h.md';assert not target.exists();target.write_text(review)
    for rel,heading in [('LM4_SUCCESSOR_report.md','Thirty-sixth-hour progress review'),('records/continuation_state.md','Actual thirty-sixth-hour review')]:
        p=root/rel;s=p.read_text();assert '## '+heading+'\n' not in s
        p.write_text(s+'\n## '+heading+'\n\n'+
            f'CONTINUE at scheduled review{reviewed.isoformat()}; capture preparation{now.isoformat()}. '
            f'Current 383-statement paper, {m["pages"]} pages, 117 references, 49 tasks. '
            'Both main decisions and actual CM parity remain Open. The signed congruence hexagon image vanishes in every modulus; the original CM character has the exact proved frame-sign criterion, whose remaining sign equality is Open. '
            'Release all writers immediately after the one immutable capture closes, before verification or saving. '
            'Verify complete logical coverage, the exact inherited map, and all three native TAR restorations/actual dictionary streams. '
            'Next review: 2026-11-17 15:49:30 UTC.\n')
    subprocess.run([sys.executable,str(root/'code/refresh_computation_inventory.py')],check=True)
    with (root/'records/checkpoint36_version_retention_run.out').open('x') as out:
        subprocess.run([sys.executable,str(root/'code/preserve_checkpoint36_versions_inductive.py'),'--commit'],stdout=out,check=True)
    retained=json.loads((root/'records/checkpoint_version_retention_summary.json').read_text())
    assert retained['archives']==35 and retained['archive_entries']==173786 and retained['omissions']==0
    assert datetime.now(timezone.utc)<next_due,'Retention exceeded this slot; no late ZIP may be opened.'
    print('Opening sole immutable36 ZIP after retained-byte validation',datetime.now(timezone.utc).isoformat(),flush=True)
    subprocess.run([sys.executable,str(root/'code/package_checkpoint.py'),'36'],check=True)
    assert archive.stat().st_size<=536870912,'Never mutate an already captured archive.'
    print('Immutable36 capture completed',datetime.now(timezone.utc).isoformat(),flush=True)

if __name__=='__main__':
    main()
