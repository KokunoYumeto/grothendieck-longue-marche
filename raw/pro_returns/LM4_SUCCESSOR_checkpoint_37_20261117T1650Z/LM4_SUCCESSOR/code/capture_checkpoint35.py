"""One scheduled checkpoint35 capture; never creates a test or catch-up archive.

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
    due=datetime(2026,11,17,13,49,30,tzinfo=timezone.utc)
    next_due=datetime(2026,11,17,14,49,30,tzinfo=timezone.utc)
    archive=root.parent/'LM4_SUCCESSOR_checkpoint_35.zip'
    assert not archive.exists()
    remaining=(due-datetime.now(timezone.utc)).total_seconds()
    assert remaining<=60,'Start only within the scheduled minute or later in this slot.'
    assert datetime.now(timezone.utc)<next_due,'No off-cycle or later catch-up invocation.'
    while datetime.now(timezone.utc)<due:
        time.sleep(.5)
    reviewed=datetime.now(timezone.utc)
    scheduled=root/'records/checkpoint35_scheduled_review.json'
    assert not scheduled.exists(),'Preserve an earlier attempt before diagnosing it.'
    scheduled.write_text(json.dumps({'scheduled_at':due.isoformat(),'recorded_at':reviewed.isoformat(),
        'decision':'CONTINUE','reason':'Actual central quotient and residual structures, full modular central tower, normalized residual reduction, entire cyclic and involution obstruction spaces, and a strictly larger mixed contact image proved; both main problems and actual CM parity remain open.',
        'archive_created_by_this_review':False,'next_scheduled_at':next_due.isoformat()},indent=2)+'\n')
    print('Scheduled35 progress review',reviewed.isoformat(),'CONTINUE',flush=True)
    last=0
    while not (root/'records/checkpoint35_capture_ready.json').exists():
        assert datetime.now(timezone.utc)<next_due,'Readiness not reached in this slot; no catch-up ZIP.'
        if time.monotonic()-last>25:
            print('Waiting for actual final verification/readiness; no ZIP opened.',flush=True);last=time.monotonic()
        time.sleep(.5)
    subprocess.run([sys.executable,str(root/'code/check_checkpoint35_preconditions.py')],check=True)
    now=datetime.now(timezone.utc)
    assert now<next_due
    m=json.loads((root/'records/checkpoint35_metrics.json').read_text())
    review=f'''# Thirty-fifth scheduled progress review and immutable capture

Scheduled review: {due.isoformat()}.
Actual review: {reviewed.isoformat()}.
Actual capture preparation: {now.isoformat()}.
Decision: CONTINUE. Next scheduled review: {next_due.isoformat()}.

The actual built paper has {m['pages']} pages and 372 statements:
328 Proved, 19 Refuted, 19 Open, 6 Known; 116 references and 49 task rows.
PDF bytes: {m['pdf_bytes']}; SHA256: {m['pdf_sha256']}.
All ten new formal sources and every new mathematical page have reviews
bound to the current bytes. Main A, Main B, and actual CM parity remain
Open. The actual central quotient has its complete product and odd
cohomology description. The next modular central refinement, entire central
tower, and nontrivial relatively perfect residual retain genuine quotient
automorphisms and full peripheral lifts at their proved scopes. The
normalized residual reduction retains its five-factor transported pentagon;
no unproved ordinary pentagon is assigned to its new word. Entire cyclic
and involution cohomology retains the original coherent obstruction without
deciding it. The actual single-contact compact family is explicit, and a
prescribed mixed contact word lies outside it; the whole contact-image
equality remains open.

This is the single35 capture for this scheduled review. The pinned34
induction retains all 10387 parent logical entries and all 152653 prior
historical identities, with 163040 resulting rows and zero omissions.
Historical versions are preserved without replacing their identities.
The closed34 certificate supplies the inherited coverage induction;
no new decompression of every earlier archive is claimed. Native three-TAR
restoration and closed-child verifiers follow actual closure before delivery.

The exact research and computation reports follow.
'''
    for rel in ['records/thirty_fifth_hour_research_report.md','records/checkpoint35_computation_audit_state.md']:
        review+='\n'+(root/rel).read_text()
    target=root/'records/progress_review_35h.md';assert not target.exists();target.write_text(review)
    for rel,heading in [('LM4_SUCCESSOR_report.md','Thirty-fifth-hour progress review'),('records/continuation_state.md','Actual thirty-fifth-hour review')]:
        p=root/rel;s=p.read_text();assert '## '+heading+'\n' not in s
        p.write_text(s+'\n## '+heading+'\n\n'+
            f'CONTINUE at scheduled review{reviewed.isoformat()}; capture preparation{now.isoformat()}. '
            f'Current 372-statement paper, {m["pages"]} pages, 116 references, 49 tasks. '
            'Both main decisions and actual CM parity remain Open. The signed congruence hexagon image vanishes in every modulus; the original CM character has the exact proved frame-sign criterion, whose remaining sign equality is Open. '
            'Release all writers immediately after the one immutable capture closes, before verification or saving. '
            'Verify complete logical coverage, the exact inherited map, and all three native TAR restorations/actual dictionary streams. '
            'Next review: 2026-11-17 14:49:30 UTC.\n')
    subprocess.run([sys.executable,str(root/'code/refresh_computation_inventory.py')],check=True)
    with (root/'records/checkpoint35_version_retention_run.out').open('x') as out:
        subprocess.run([sys.executable,str(root/'code/preserve_checkpoint35_versions_inductive.py'),'--commit'],stdout=out,check=True)
    retained=json.loads((root/'records/checkpoint_version_retention_summary.json').read_text())
    assert retained['archives']==34 and retained['archive_entries']==163040 and retained['omissions']==0
    assert datetime.now(timezone.utc)<next_due,'Retention exceeded this slot; no late ZIP may be opened.'
    print('Opening sole immutable35 ZIP after retained-byte validation',datetime.now(timezone.utc).isoformat(),flush=True)
    subprocess.run([sys.executable,str(root/'code/package_checkpoint.py'),'35'],check=True)
    assert archive.stat().st_size<=536870912,'Never mutate an already captured archive.'
    print('Immutable35 capture completed',datetime.now(timezone.utc).isoformat(),flush=True)

if __name__=='__main__':
    main()
