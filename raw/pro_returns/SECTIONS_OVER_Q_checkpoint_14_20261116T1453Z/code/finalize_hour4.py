#!/usr/bin/env python3
"""Record the audited fourth-hour integrations and the hourly progress review."""
from pathlib import Path
import json

work = Path(__file__).resolve().parents[1]
meta_path = work / 'notes/register_metadata.json'
meta = json.loads(meta_path.read_text())
meta['A.79'] = {
    'answers': 'A1; A7; L15; L19',
    'depends_on': 'A.14; A.16; A.37; A.41; A.54; A.78; exact local logarithm valuations and the unique-minimum valuation argument',
    'uses_local_theorem': 'no for the stated Selmer-section result; extension to arbitrary sections uses R1',
    'manuscript_passages': 'cote149; scans48,54–56,66; A7; L15; L19',
    'notes': 'For even integer realizations, an explicit unique-minimum logarithmic valuation criterion excludes every contact-zero cusp. It proves the point conclusion with arbitrary labeled integral comparison when v2(lambda) is outside{2,4}, and with full H-conjugacy in the remaining two cases. New infinite families191^(2j+1)+1 and3^(2j+1)+1 and the examples88,120 are proved. The certificate checks all even integers through5000; its comparison is explicitly against the listed earlier criteria, without a completeness claim.'
}
meta_path.write_text(json.dumps(meta, indent=2, ensure_ascii=False) + '\n')

report = work / 'SECTIONS_OVER_Q_report.md'
s = report.read_text()
s = s.replace('all individual root-torsor norm tests in the stated coefficient range',
              'all individual root-torsor norm tests at every coefficient prime for the constructed point3-congruent ghosts')
s = s.replace('individual norm-level survival for one fixed pair in its stated range',
              'individual norm-level survival at every coefficient prime for one fixed constructed point3-congruent pair')
s = s.replace('Every ordinary pair with v3(A)=1 passes each individual odd-prime norm test, including coefficient3:',
              'Every ordinary pair with v3(A)=1 passes each individual odd-prime norm test, including coefficient3:')
old = 'The remaining inverse limit is represented by the exact norm-kernel class, with no compactness inference for the completed prime lattices. Root and local-agent audits passed.'
new = ('At coefficient2 the same conclusion holds when A/3 is a square, as for the constructed ghosts: the local decomposition group at2 is the entire affine splitting group, and the opened Oki duality statement gives the Hasse norm principle. Thus the same constructed pair passes every individual norm level at every coefficient prime. The remaining inverse limit is represented by the exact norm-kernel class, with no compactness inference for the completed prime lattices. Root and local-agent audits passed.')
assert old in s
s = s.replace(old, new)

lines = s.splitlines()
for i, line in enumerate(lines):
    if line.startswith('| A7 |') and 'Open in general:' in line:
        line = line.replace('A.74, A.78 |', 'A.74, A.78–A.79 |')
        line = line.replace('Recognition from H alone still requires solving these simultaneous equations.',
            'A.79 adds a computable logarithmic minimum criterion, the infinite families191^(2j+1)+1 and3^(2j+1)+1 with their exact comparison scopes, and composite-neighbour examples88,120. General recognition still requires solving the remaining simultaneous equations.')
        lines[i] = line
    elif line.startswith('| A5 |') and 'Constructed genuine' in line:
        lines[i] = line[:-2] + (' A.75 now identifies the full obstruction with its finite-weight integral images for the same pair: the augmentation-ideal compatibility term is zero. A.77 makes one fixed constructed pair pass all individual norm levels at every coefficient prime; its coherent-norm class remains unevaluated. |')
    elif line.startswith('| A7 |') and 'Proved integral labeled realization' in line:
        lines[i] = ('| A7 | The exact integral labeled realization, multiplier comparison and earlier recognition families are proved. A.70 isolates every rational realization after an explicit finite Kummer enlargement. A.78 fixes every ordinary potentially multiplicative local value exactly and confines all relative exponents to actual cuspidal places with24-divisibility and square-unit formulas. A.79 rules out contact-zero cusps by the unique least p-adic logarithm valuation; it gives two additional infinite families and the composite-neighbour examples88,120. The general simultaneous cusp equations remain unresolved. |')
    elif line.startswith('| L10 |') and 'Full class two, actual infinite-support' in line:
        lines[i] = ('| L10 | Full class two, ordinary infinite-support integral lifts at every fixed nilpotent depth, and locally matched examples for each fixed finite modular quotient are established. A.71 gives the exact full/pro-prime metabelian comparison, and A.75 removes the extra augmentation-ideal compatibility class for one fixed pair. A.77 proves that one fixed constructed pair passes every individual root-torsor norm test at every coefficient prime. Its coherent-norm class and the full same-pair metabelian lift remain the next unresolved steps. |')
s = '\n'.join(lines) + '\n'
anchor = 'A.78 proves exact equality with the realized parameter'
start = s.index(anchor)
end = s.index('\n\n', start)
s = s[:end] + ('\n\nA.79 proves a logarithmic valuation recognition criterion for even integer realizations. At every candidate contact-zero prime, the opposite-coordinate logarithmic summands have exact valuations determined by the rational parameter. A unique least valuation excludes that cusp. The proof retains arbitrary labeled integral comparisons except for dyadic valuations2 and4, where it uses full H-conjugacy. The families191^(2j+1)+1 and3^(2j+1)+1 and the examples88,120 are proved with those exact scopes. Root and local-agent audits passed. The exact certificate checks714 qualifying even parameters through5000; it identifies17 additional unrestricted-comparison examples and217 additional H examples relative to A.41, A.45 and A.63, with199 of the latter remaining after the explicit A.64 comparison.') + s[end:]
report.write_text(s)

with (work / 'notes/root_progress.md').open('a') as f:
    f.write('\n04:46 UTC: A.74–A.79 independently audited and integrated. A.75 computes the full same-pair Alexander obstruction and proves its augmentation-ideal lim1 term vanishes. A.77 proves all individual root-torsor norm tests at every coefficient prime for one fixed constructed ghost; coherent norms remain unresolved. A.78 confines global relative exponents to actual cuspidal places and fixes ordinary bad-place values exactly. A.79 adds two infinite recognition families and a computable unique-minimum logarithm criterion. A.74 gives the exact odd-prime point/cusp map and separating Kummer level; A.76 detects every nontrivial completed Kummer class on a positive-density set and identifies the completed-old-coordinate failure of A.69/A.73.\n')

with (work / 'notes/root_source_continuation.md').open('a') as f:
    f.write('\n04:46 UTC: Root opened the original Tate uniformization PDF at https://people.math.harvard.edu/~ctm/home/text/others/tate/tate-unif/tate-unif.pdf and checked the coordinate series(1)–(4) used in A.78; its constant term is rearranged explicitly in the proof. Root opened Oki, arXiv2508.10706v2 (10June2026), Proposition6.4 and Corollary6.5, printedp35. These state the general torus duality comparison used by A.77; the later prime-squared specialization is not imported into the general statement. The full local decomposition-group proof and dyadic radical square class are independently audited.\n')

print('Integrated A79 metadata; updated A5/A7/L10 and the dyadic A77 range; recorded root and source audits.')
