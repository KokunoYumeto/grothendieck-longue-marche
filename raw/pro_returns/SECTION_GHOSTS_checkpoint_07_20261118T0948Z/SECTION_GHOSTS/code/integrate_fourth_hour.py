"""Integrate the independently read fourth-period proofs and audit records.

This is document assembly, not a mathematical certificate.
"""
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
main = ROOT / 'SECTION_GHOSTS_paper.tex'
text = main.read_text()
anchor = '\\input{sections/part_E_embedding_gate}'
additions = [
    'part_E_embedding_step', 'part_E_everywhere_finite',
    'part_E_ordinary_invariant', 'part_E_failed_predecessor',
    'part_E_finite_field_sections', 'part_E_full_ordinary_bridge',
]
for name in additions:
    target = '\\input{sections/' + name + '}'
    if target not in text:
        text = text.replace(anchor, anchor + '\n' + target)
    anchor = target
old = ('can all be satisfied for one fixed pair at every weight.\n'
       'We also identify')
new = ('can all be satisfied for one fixed pair at every weight.\n'
       'For a cofinal finite pro-three tower, we prove an exact one-step\n'
       'criterion over the unchanged old ramification set. Its remaining\n'
       'conditions are finitely many plus-character Frobenius equations.\n'
       'A simultaneous arithmetic refinement preserves ordinarity at every\n'
       'coefficient prime along any actual infinite path through those\n'
       'equations. Such a path is not constructed; explicit frozen\n'
       'predecessors fail the equations and cannot be repaired by adding\n'
       'ordinary support primes.\n'
       'We also identify')
if old in text:
    text = text.replace(old, new)
main.write_text(text)

metadata = ROOT / 'notes/root_results.csv'
with metadata.open() as handle:
    reader = csv.DictReader(handle)
    fields = reader.fieldnames
    rows = list(reader)
assert fields is not None
row = {key: '' for key in fields}
row.update({
    'id': 'E.151', 'status': 'Proved',
    'depends_on': 'A.31; E.31; E.102; E.144; E.146; E.148',
    'answers': 'A.3; A.4; L.1; L.2',
    'uses_local_theorem': 'no',
    'notes': ('Exact conditional finite-step bridge: full ordinary completed '
              'pair retained along an actually chosen pro-three plus-gate '
              'branch. No infinite branch and no section at other '
              'coefficient primes are asserted. Sequential fixed radical '
              'roots replace the preliminary power-shell approach.')
})
rows = [r for r in rows if r.get('id') != 'E.151'] + [row]
with metadata.open('w', newline='') as handle:
    writer = csv.DictWriter(handle, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)

events = ROOT / 'notes/root_CHECK_EVENTS.tsv'
who = 'GPT-6 Astra; ChatGPT Pro; SECTION_GHOSTS/root'
new_events = [
    ('E.138', 'targeted proof check',
     'Read the full proof; localization at five is the identity on Z/24, so one-place matching puts no abelian rigidity on an ordinary pair.'),
    ('E.139', 'targeted proof check',
     'Read the full relative Bloch, order-nine central-shift, and harmonic-cancellation proofs; reopened CGZ Lemma4.1 and Hutchinson Theorem2.10 at the exact places; retained the distinction between relative primitive and cusp symbol.'),
    ('E.139', 'computation or formal certificate',
     'Independently reran ghost_audit_bloch.py: 14008 five-term checks, harmonic values, central shifts modulo27, and all eta injections for primes below1000 passed.'),
    ('E.146', 'targeted proof check',
     'Completed the root read of the exact quotient-gate equivalence, Brauer reciprocity, old valuation normalization, fresh cusp image and unramified B_n cohomology.'),
    ('E.147', 'targeted proof check',
     'Completed the root read including the final local matching and Weil-bound argument. No induction through the quotient tests is inferred.'),
    ('E.148', 'targeted proof check',
     'Read all steps: exact plus equations with every aligning frame, harmless H0 ambiguity via inertia injection, good-reduction abelian invariant, and conditional inverse limit. The three-primary scope is explicit.'),
    ('E.149', 'targeted proof check',
     'Read the full failed-predecessor construction: Q2/B2=H3, full geometric image, constant-character line, vanishing lower stabilizers at five and q, and impossibility of repair by arbitrary new ordinary primes.'),
    ('E.150', 'targeted proof check',
     'Read the full finite-field group proof, including actual action and conversion from arithmetic to geometric conjugacy. Opened Hoshi Remark10(i); no point-cusp or prime-field separation conclusion is inferred.'),
    ('E.150', 'computation or formal certificate',
     'Independently reran check_finite_field_sections.py; both irreducibility and Frobenius-orbit certificates passed.'),
    ('E.151', 'independent re-proof',
     'Constructed the full ordinary bridge with independent product factors, fixed-root exponent-M_(n+1) primes, cyclic three-primary intersection compatibility and sequential preservation of new local unit points; the limit is conditional on an actual infinite branch.'),
    ('E.160', 'targeted proof check',
     'Read the full initialization proof and complete finite script; checked the genus, Weil bound, exceptional local roots, six Hilbert-symbol products and rational valuation normalizers.'),
    ('E.161', 'targeted proof check',
     'Independently checked all three monomial lattices, signed quadratic relation fields, Kummer eigenbasis intersection and maximal-abelian proof; private valuations remain fixed under fourth-power refinements.'),
    ('E.162', 'targeted proof check',
     'Read the complete signed mixed refinement, CRT reciprocity, successive root conditions, preservation of earlier new-prime points, fixed centers, and full completion/local convergence.'),
    ('E.163', 'targeted proof check',
     'Checked the explicit residue identity at c, proper Brauer extension, uniform dyadic and every exceptional odd-prime evaluation, and reciprocity exclusion; opened primary Colliot-Thelene notes.'),
    ('E.164', 'targeted proof check',
     'Read the actual cyclic-eight cover and order4096 class8 quotient, every possible finite local sheet, nonsplit central descent and the real cuspidal comparison; opened primary Milne etale notes.'),
    ('E.165', 'targeted proof check',
     'Independently identified G=(C4)^2 semidirect C8, graph cycle rank129, faithful path quotient, four-seed normal generation and exact augmentation recurrence; inspected the complete code and nonzero weight17 witness.'),
    ('E.160', 'computation or formal certificate',
     'Reran check_harmonic_audit.py: all661 good primes through5000, the sole457 boundary, all special centers and six root-symbol products passed.'),
    ('E.165', 'computation or formal certificate',
     'Reran check_harmonic_large_quotient.py: Gamma4..Gamma18 dimensions124,121,115,107,97,85,71,55,41,29,19,11,5,2,0; expanded weight17 witness nonzero with recorded SHA256.'),
]
with events.open() as handle:
    reader = csv.DictReader(handle, delimiter='\t')
    event_fields = reader.fieldnames
    event_rows = list(reader)
for sid, kind, outcome in new_events:
    record = dict(zip(event_fields, [sid, '2026-11-18', who, kind, outcome]))
    if record not in event_rows:
        event_rows.append(record)
with events.open('w', newline='') as handle:
    writer = csv.DictWriter(handle, fieldnames=event_fields, delimiter='\t')
    writer.writeheader()
    writer.writerows(event_rows)
print('Integrated E.146--E.151 and recorded ten precise root check events.')
