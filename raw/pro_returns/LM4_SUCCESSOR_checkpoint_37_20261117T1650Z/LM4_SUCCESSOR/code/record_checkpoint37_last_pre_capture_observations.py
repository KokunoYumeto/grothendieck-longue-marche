"""Record the actual completed final size run and late source-only mathematics."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
def bind(rel):
    raw = (ROOT / rel).read_bytes()
    return {'path': rel, 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}
r = json.loads((ROOT / 'records/checkpoint37_size_estimate.json').read_text())
w = r['previous_direct_data_migration_witnesses']
assert len(w) == len({row['old_direct_path'] for row in w}) == 6778
assert sum(row['old_compressed_payload_bytes'] for row in w) == 31061701
assert all(row['headers_removed'] == 0 for row in w)
assert r['estimated_total_with_allowance'] == 525352754
assert r['estimated_headroom_bytes'] == 11518158
assert not (ROOT / 'records/checkpoint37_size_estimate_run.err').read_bytes()
record = {
 'recorded_at': datetime.now(timezone.utc).isoformat(),
 'final_size_producer': {'session_id': 54149, 'launch_chunk': 'e61160',
                         'actual_exit_code': 0, 'actual_exit_tool_chunk': 'fcd502'},
 'complete_stdout_and_empty_stderr_read': 'd7f7a7',
 'report': bind('records/checkpoint37_size_estimate.json'),
 'all_predicted_history_rows_read': 'a1eace',
 'migration_read_scope': 'All6778 per-payload witnesses were validated against the exact prospective snapshot by the successful estimator; root parsed the complete JSON and checked their count, uniqueness, sum and zero-header accounting, but does not claim a manual reading of every identity.',
 'final_audit_writer_actual0_chunk': 'd344a5',
 'late_sources': [bind(rel) for rel in [
   'work_A/actual_annular_positive_cubic_hexagon_gate37.md',
   'work_DE/actual_annular_negative_fixed_group37.md',
   'work_A/actual_annular_source_gauge_identity37.md']],
 'root_complete_source_reads': ['f73f5b', '60d7cd', 'e203d1'],
 'root_complete_C28_reopening': ['0a4e11', '022e31', '537a37'],
 'read_scope_note': '60d7cd displayed the entire first fixed-group note; its exit1 concerned only an absent second review filename. No incomplete first-source read or mathematical producer failure is inferred.',
 'scope': 'The positive word maps exactly to the original marked hexagon obstruction; the actual negative source has trivial fixed subgroup by a fully justified central splitting and torsion argument; the source gauge is literally Phi_S Z_phi,S. No fixedness or vanishing of the positive cube, original CM value, or Main A decision is proved. Complete new saved-byte source-gauge peer review remains separate.',
 'ready_or_archive_claimed': False,
}
with (ROOT / 'records/checkpoint37_last_pre_capture_observations.json').open('x') as stream:
    json.dump(record, stream, indent=2)
    stream.write('\n')
report = ROOT / 'records/thirty_seventh_hour_research_report.md'
addition = '''
## Last source-level advances before capture37

The prescribed positive annular word has the exact original modular
image q(C_+^3)=iota_s(H_d)^{-1}. Its source cube, elliptic image cube,
and modular image cube remain separate gates. The original negative
annular source involution has trivial fixed subgroup, including after
the proved canonical gauge; the complete proof supplies an equivariant
central splitting of the pure braid group before using the full source
torsion classification. A further ordered calculation identifies the
source gauge itself as H_S=Phi_S Z_phi,S. These are full-source statements.
The literal transformed positive-cubic row has been written out, but
fixedness of its cube is not proved; inverse-conjugacy does not suffice.
The exact sources and root-read scope are retained in the last
pre-capture observation record. The existing PDF remains frozen.

In Main B, the retained bar-a branch keeps the mixed defect nontrivial
in its complete m-only HNN presentation. The second source has a common
family correction, yet its head image still contains an essential D
syllable in the initial quotient. The next two-head-square normal-closure
test is saved explicitly as pending: m-invariance is proved, while the
full second-source/inverse test and actual all-source survival are not.
All signed-source saturation requirements remain in the genuine target.
'''
assert '## Last source-level advances before capture37' not in report.read_text()
with report.open('a') as stream:
    stream.write(addition)
print(json.dumps({'result': 'ACTUAL_FINAL_SIZE_AND_LATE_SCOPE_RECORDED',
                  'actual_size_exit_code': 0, 'no_archive_claimed': True}))
