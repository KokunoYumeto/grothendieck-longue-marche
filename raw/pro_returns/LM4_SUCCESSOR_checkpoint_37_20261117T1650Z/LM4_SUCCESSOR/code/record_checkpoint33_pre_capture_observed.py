"""Record actual tool completions and explicit agent pause acknowledgments."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
root=Path(__file__).resolve().parents[1]
sha=lambda rel:hashlib.sha256((root/rel).read_bytes()).hexdigest()
estimate=json.loads((root/'records/checkpoint33_size_estimate.json').read_text())
assert estimate['estimated_total_with_allowance']==517017137
assert not (root/'records/checkpoint33_size_estimate_run.err').read_bytes()
review=json.loads((root/'work_DE/review_checkpoint33_readiness_publisher.json').read_text())
assert review['result']=='PASS' and sha(review['source'])==review['source_sha256']
agents=[
 dict(agent='/root/involutions',paused=True,evidence_time='2026-11-17T11:46:33.232703+00:00',evidence='work_A/status_checkpoint33.md',owned_live_producers=[]),
 dict(agent='/root/torus_real',paused=True,evidence_time='2026-11-17T11:45:23.668684+00:00',evidence='work_CE/checkpoint33_pause_status.json',owned_live_producers=[]),
 dict(agent='/root/topology_census',paused=True,evidence_time='2026-11-17T11:45:48.502671+00:00',evidence='work_DE/checkpoint33_final_status.md',owned_live_producers=[]),
]
for row in agents:row['evidence_sha256']=sha(row['evidence'])
producers=[
 dict(role='formal_integration',producer='Seven reviewed sources integrated',tool_chunk='ef9857',exit_code=0),
 dict(role='final_build',producer='Corrected final combined build and stabilization',session_id=14597,completion_tool_chunk='90d4ec',exit_code=0),
 dict(role='final_metrics',producer='Fresh354-statement final metrics',tool_chunk='1d5a60',exit_code=0),
 dict(role='final_render',producer='Final corrected626-page PDF image render',session_id=38640,completion_tool_chunk='e98f25',exit_code=0),
 dict(role='corrected_pdf_audit',producer='Complete final logs and exact final-image identity',tool_chunk='22a4de',exit_code=0),
 dict(role='final_visual_record',producer='Bound final image observations and actual individual-page reviews',tool_chunk='ac574f',exit_code=0),
 dict(role='late_research_binding',producer='Six complete separately reviewed research proofs bound',tool_chunk='cc116f',exit_code=0),
 dict(role='final_size_estimate',producer='All three actual compression streams and direct-payload estimate',session_id=47557,completion_tool_chunk='324830',actual_exit_observed_at='2026-11-17 11:46:06 UTC',exit_code=0),
]
record=dict(recorded_at=datetime.now(timezone.utc).isoformat(),root_observed_actual_exit_codes=True,
    observed_producer_completions=producers,agents=agents,live_producers=[],
    source_review_binding={'work_DE/review_checkpoint33_readiness_publisher.md':sha('work_DE/review_checkpoint33_readiness_publisher.md'),
        'work_DE/review_checkpoint33_readiness_publisher.json':sha('work_DE/review_checkpoint33_readiness_publisher.json')},
    stopped_attempt=dict(session_id=88588,actual_exit_code=130,completion_tool_chunk='216a87',preserved=True),
    next_writer='The sole scheduled33 capture controller; no root research or PDF writer remains live.',
    historical_unconfirmed=['old estimator29436 lost context','old DEg3:543 lost context'])
target=root/'records/checkpoint33_pre_capture_observed.json';assert not target.exists();target.write_text(json.dumps(record,indent=2)+'\n')
append=('\n## Observed completion appended before scheduled capture\n\n'
    'Final estimator47557 actually exited0, observed in tool chunk324830 at11:46:06 UTC. Its recorded stream completion was11:44:44.154127 UTC. '
    'All three actual streams are complete: image403398390 compressed bytes with64MiB dictionary; document53467690 bytes with8MiB; data19382808 bytes with64MiB. '
    'Estimated total517017137 bytes includes5000000 bytes allowance and leaves19853775 bytes below536870912. The final PDF binding is80e44d3c3e9766d79c3e740dc83577f7a60a80947a254e6803c74725e0534c70. '
    'The entire estimate record and empty stderr were read. Final immutable size remains authoritative.\n\n'
    'All three writers explicitly paused: CE11:45:23.668684,DE11:45:48.502671,A11:46:33.232703 UTC. Their exact saved evidence and current producer completions are bound in checkpoint33_pre_capture_observed.json. '
    'No current owned producer remains. The stopped first estimator130 and historical unconfirmed sessions retain those distinct statuses. '
    'The sole scheduled capture controller is the only intended next project writer. Release all writers immediately after actual capture exit0.\n')
path=root/'records/checkpoint33_computation_audit_state.md';path.write_text(path.read_text()+append)
print('Recorded actual final producer exits and all three explicit writer pauses.',flush=True)
