#!/usr/bin/env python3
"""Add exact frozen-text anchors and actual post-freeze root check records.

This script never opens a page file for writing. The transcription is frozen.
"""
from pathlib import Path
import csv
import re

ROOT = Path(__file__).resolve().parent.parent
CONTEXT = ROOT.parent / 'context'
RECORDS = ROOT / 'records'
WHO = 'GPT-6 Astra Pro; effort inherited/not separately exposed; run MPL_93_047-091; /root'
DATE = '2026-11-18'

def norm(s):
    return ' '.join(s.split())

quotes = {
1: (86, r'Données équivalentes'),
2: (86, r'M=\check E\otimes E\simeq\underline{\operatorname{End}}(E)'),
3: (86, r'\Gamma^2E\otimes(\Lambda^2E)^{-1}'),
4: (86, r'\unsure{f^*\Lambda^2E|f^*(\Lambda^2E)^{-1}}'),
5: (86, r'\unsure{expliciter|expliquer} !'),
6: (87, r'2 inv.!'),
7: (86, r'M\overset{?}{\simeq}f_*\bigl(P^1_{P/X}(\underline t_{P/X})\bigr)'),
8: (86, r'en est le centre'),
9: (86, r'can, iso si 2 inv. sur $X$'),
10: (86, r'attention à la Car. (notamment Car. 2!)'),
11: (86, r'schéma des Idéaux à gauche'),
12: (87, r'rep. \unsure{vraie|naïve}'),
13: (87, r'avec section marquée $\sigma$'),
14: (87, r"f) Une \unsure{$O_X$ Algèbre|Ext($O_X$)}"),
15: (87, r'\unsure{\mathcal I^2L|\mathcal IL}'),
16: (87, r"clôture projective du torseur sous $W(\Omega)$ défini par l'extension."),
17: (87, r'avec idéal annulateur de $\Omega$'),
18: (87, r'et $\mathcal L$ est une ss.-Alg. de Borel'),
19: (87, r'\unsure{exprimer|expliquer} aussi'),
20: (87, r'vérifier!'),
21: (87, r'déduits par passage au quot. par Centre $\mu_2$'),
22: (87, r'\margin{\uline{faux}}'),
23: (87, r"\unsure{Il nous sera peut-être commode d'expliciter|Il me sera peut-être commode d'expliciter}"),
24: (88, r'\uline{deux} sections \uline{disjointes}'),
25: (88, r'somme directe de deux Idéaux spéciaux'),
26: (88, r'Mais dans la table de multiplication'),
27: (88, r"le choix d'une des deux sous-Algèbres"),
28: (88, r'avec couple de \unsure{Killing}'),
29: (89, r'Une connexion (sans courbure)'),
30: (89, r'toute dérivation de $\mathfrak g$ est intérieure!'),
31: (89, r'\overset{?}{=}'),
32: (90, r'\text{poids }2'),
33: (90, r'\unsure{tte|toute} connexion $c$ satisfait'),
34: (90, r'qui est \uline{linéaire}'),
35: (90, r'\boxed{c_{1,2}=-2c_{2,3}}'),
36: (90, r'On trouve que la connexion respecte la filtration ssi'),
37: (90, r'forment un torseur sous $\mathfrak g\otimes\uline\omega$'),
38: (90, r'\uline{Ce dernier} est splitté canoniquement'),
39: (90, r"d'où torseur $\mathrm{Conn}_i$ sous $\mathcal L\otimes\uline\omega$"),
40: (90, r'C_\Omega(f\omega)-fC_\Omega(\omega)\simeq\omega\otimes df.'),
41: (90, r"(p.e. en Car. $2$?) c'est \unsure{peut-être|encore} plus précis"),
42: (91, r'une restriction du Groupe structural'),
43: (91, r'ce qui implique $2$ inv.'),
44: (91, r'est défini à isom unique près par $X/S$'),
45: (91, r"et existe ssi $\uline\omega=\underline\Omega^1_{X/S}$ est inversible"),
46: (91, r'à $\Omega\otimes\uline\omega$'),
47: (87, r'(P,\sigma,C)'),
48: (86, r'\mathfrak{sl}(\unsure{1|2})_X'),
49: (91, r'd^1_{X/S,\underset{\uline\omega}{\unsure{\omega|\infty}}}'),
}

op_path = RECORDS / 'research_opers.md'
op_text = op_path.read_text()
for n, (scan, quote) in quotes.items():
    page = ROOT / f'pages/MPL_93_047-091_93_scan{scan:03}.tex'
    assert norm(quote) in norm(page.read_text()), (n, scan, quote)
    pattern = rf'(### OP{n:02} — [^\n]+\n\n)(?!\*\*Short quote)'
    addition = f'**Short quote (frozen TeX, scan {scan:03}):** `{quote}`.\n\n'
    op_text = re.sub(pattern, lambda m: m[1] + addition, op_text)
op_path.write_text(op_text)

proof_path = RECORDS / 'projective_proof_checks.md'
proof_text = proof_path.read_text()
proof_text = proof_text.replace('and its kernel of variation is `Omega tensor omega`.',
    'and, at fixed i, its kernel of variation is `Omega tensor omega`.')
proof_text = proof_text.replace('global extensions, if present, form the corresponding space of sections, and their sheaf is a torsor.',
    'global extensions, if present, form a torsor under `H^0(X, omega^2)`, and their sheaf is a torsor under `omega^2`.')
proof_path.write_text(proof_text)

# All of these terms are actually searched now; zero results are recorded.
# The narrower manuscript/context comparison has also been read by the root.
context_paths = [CONTEXT/'README.md', CONTEXT/'notes/RESULTS_STATE.md',
                 CONTEXT/'same_cote_93/MPL_93_002-046_notes.md',
                 CONTEXT/'hua_project/93.modern.tex']
source_lines = {p: p.read_text().splitlines() for p in context_paths}
root_texts = [op_path.read_text(), (RECORDS/'research_context_s20.md').read_text()]
blocks = []
for text in root_texts:
    for match in re.finditer(r'^### ((?:OP\d+|S20-\d+|HC\d+)) — ([^\n]+)\n(.*?)(?=^### |^## |\Z)', text, re.M|re.S):
        blocks.append((match[1], match[2], match[3]))
assert len(blocks) == 68, len(blocks)
with (RECORDS/'research_root_context_search.tsv').open('w', newline='') as f:
    w = csv.writer(f, delimiter='\t')
    w.writerow(['note_id','literal_casefold_query','file','match_count','first_matching_lines','sample_excerpt'])
    for note, title, body in blocks:
        query_match = re.search(r'\*\*Context queries:\*\* ([^\n]+)', body)
        assert query_match, note
        terms = [term.strip().rstrip('.') for term in query_match[1].split(';') if term.strip()]
        for term in terms:
            for path, lines in source_lines.items():
                hits = [(i+1,line) for i,line in enumerate(lines) if term.casefold() in line.casefold()]
                w.writerow([note,term,str(path.relative_to(CONTEXT)),len(hits),
                    ','.join(str(i) for i,line in hits[:8]),hits[0][1][:360] if hits else 'NO LITERAL MATCH'])

outcomes = {
1:'Checked real-conic counterexample to a global rank-two presentation; local Azumaya formulation compared with OP-S2.',
2:'Checked tensor cancellation and wedge-dual identity without inverting 2; line-twist ambiguity compared with OP-S2.',
3:'Checked both sequences on a free rank-two basis; divided and symmetric squares remain distinguished.',
4:'Checked inverse-determinant tangent formula in quotient convention; frozen alternative remains unresolved as ink.',
5:'Independent matrix commutator calculation in proof A gives the three stated brackets.',
6:'Proof A and exact certificate give determinant -32; orthogonality is used only where 2 is invertible.',
7:'Proof C checks canonical pushed-forward relative-jet splitting and the lack of a compatible equivariant trace retraction at 2; no negative bare-bundle assertion.',
8:'Matrix-unit centralizer and local projective vector fields checked; no bad-characteristic Lie-automorphism equivalence inferred.',
9:'Trace subtraction and the different centres in characteristic 2 checked in proof A.',
10:'Explicit characteristic-2 Lie automorphism family has dimension 6; unrestricted identification refuted; refined statement OP10-R.',
11:'Checked split-model special left ideal parametrization; unrestricted Lie-subalgebra classification remains unproved.',
12:'Checked scalar central action obstructing descent of the standard GL2 representation; doubtful word remains unresolved.',
13:'Checked degree-one divisor, rigidification, pushforward and marked quotient construction.',
14:'Cancelled frozen wording compared with Hua VII; neither interpretation nor an equivalence proved.',
15:'Checked fibre ranks and H0/H1 of O(-1) for the first infinitesimal neighborhood; reading remains frozen.',
16:'Checked local translation gluing of the complement of the marked section in the quotient convention.',
17:'Checked annihilator stability under left multiplication and identified Hom(L/Omega,L).',
18:'Checked symmetric-square kernel and Borel transition matrix, including the rank-two filtration.',
19:'Checked the local symmetric-square reconstruction; retained group/Lie distinction at 2.',
20:'Proof B gives a characteristic-2 nonsplit-extension counterexample; corrected statement OP20-R requires 2 invertible.',
21:'Checked determinant-square-root fppf lifting and kernel mu2; no etale-cover claim.',
22:'Located isolated faux in frozen text and compared later horizontal/transverse distinction; attachment remains unresolved.',
23:'Compared frozen 087 intention with actual 089–090 calculation; corrected connection category retained.',
24:'Checked ordered disjoint-section splitting and the effect of interchanging the order.',
25:'Checked column-annihilator direct sum as left modules, not two-sided algebras.',
26:'Independent sl2 commutators give coefficients -2,+2,1 and H mapping to 2h.',
27:'Characteristic-2 ad(h) is scalar on W, so every line is stable; unrestricted two-line claim refuted, refinement OP27-R.',
28:'Compared doubtful terminal word with Hua VII; no alternate glyph reading or theorem inferred.',
29:'Checked coefficientwise differentiation preserves constant brackets and squares to zero locally.',
30:'Proof A and exact derivation equations refute unrestricted innerness; 090 supplies refinement OP30-R.',
31:'Compared interrupted 089 formula with 090 and checked completed matrix in proof A; transcription unchanged.',
32:'Matrix columns independently computed; crowded lambda/weight annotations remain reading questions.',
33:'Flat characteristic-2 connection d+D dt violates the filtration claim for arbitrary Lie connections; refinement OP33-R retains group origin or 2 invertible.',
34:'Checked that the Leibniz term dies in the next graded quotient.',
35:'Matrix calculation gives c12=-2c and c23=c exactly.',
36:'Checked Borel-valued local form, horizontal marked section, and flag preservation equivalence for projective-bundle connections.',
37:'Checked difference-sheaf torsor calculation; no global nonemptiness or canonical origin asserted.',
38:'Checked that Borel frame-change derivative has zero normal component, giving the canonical quotient origin.',
39:'Checked kernel of the normal-component map and the torsor at fixed i.',
40:'Checked differential-operator symbol and quotient -2i; comparison with principal-parts universal property.',
41:'Proof D checks that quotient operator detects c in characteristic 2 while the Omega restriction loses it.',
42:'Checked kernel of restriction within the fixed-i torsor; no claim that all coefficients are fixed.',
43:'Checked local line-bundle unit-product argument: invertible -2i forces 2 invertible.',
44:'Independent universal-property proof E identifies the restricted first-jet triple and its uniqueness.',
45:'Checked scope of the existence equivalence with inherited 2-invertibility; neither smoothness nor full global connection inferred.',
46:'Checked remaining local torsor is omega squared, with global sections a torsor if nonempty; Hua tensor-degree expression differs.',
47:'Compared precise smooth-complex-curve projective oper description with Beilinson–Drinfeld; no Gauss–Manin realization claimed.',
48:'Recorded Hua alternative to frozen sl index; no reading resolved after freeze.',
49:'Compared universal-operator interpretation with frozen subscript; glyph remains unresolved.',
}
background_op = {14,22,28,48,49}
independent_op = {5,6,7,9,18,26,30,35,38,41,44,46}
refuted_op = {10,20,27,30,33}
events = []
for n in range(1,50):
    typ = ('carried as background without fault found' if n in background_op else
           'independent re-proof' if n in independent_op else 'targeted proof check')
    events.append([f'OP{n:02}',DATE,WHO,typ,outcomes[n]])
    if n in refuted_op:
        events.append([f'OP{n:02}',DATE,WHO,'refuted, with the refined statement\'s id',
                       f'Unqualified claim refuted with the counterexample in OP{n:02}; refined statement OP{n:02}-R.'])
    if n in {5,6,9,10,18,20,26,27,30,32,33,35,41}:
        events.append([f'OP{n:02}',DATE,WHO,'computation or formal certificate',
                       'Exact symbolic/rational calculation in scripts/check_projective_algebra.py and records/projective_algebra_certificate.json; not a proof-assistant formalization.'])

for note,title,body in blocks:
    if note.startswith('OP'):
        continue
    if note == 'HC06':
        typ = 'targeted proof check'
        outcome = 'Checked nonadditivity over F2[x,y]: (x+y)d(x+y)-x dx-y dy=x dy+y dx=d(xy), nonzero before cohomology; applies to Hua interpretation only.'
    elif note == 'HC02':
        typ = 'used and rechecked in this run'
        outcome = 'Compared current 072–074 against Hua IX and the result candidate; reviewed exact scope of C7–C8, not a general global theorem.'
    else:
        typ = 'used and rechecked in this run'
        outcome = ('Compared the frozen current-page evidence with the cited context locations for: '+title+
                   '; this is an evidentiary comparison, not a new proof of a later claim or an inspected later original image.')
    events.append([note,DATE,WHO,typ,outcome])

extras = [
('ROOT-PROOF-A-E','independent re-proof','Written checks A–E plus exact executable certificate; source hypotheses and characteristic restrictions retained.'),
('ROOT-PEER-EC01-54','targeted proof check','Root read EC01–54 and proof details, checked Euler telescope counterexample and reduced-quadratic/Postnikov construction, and opened cited primary theorem hypotheses; no conical-end finiteness or uniqueness theorem promoted.'),
('ROOT-PEER-SC01-60','targeted proof check','Root read SC01–60 and C1–C10; checked normalization, sign and counterexample scope. Full universal classification remains unproved.'),
('SC114','targeted proof check','Root independently reviewed C8 monic-algebra descent: flat base change of the kernel, singular-matrix uniqueness, rank-one descent, Pic(A)=0, and determinant/denominator units; accepted precisely the stated local monic model.'),
('HC06','refuted, with the refined statement\'s id','Hua XIII closed-form-level universal assignment is not additive; refinement HC06-R passes to cohomology or uses explicitly chosen representatives.'),
('OP-S1','used and rechecked in this run','Root opened and read Stacks 01OA quotient convention.'),
('OP-S2','used and rechecked in this run','Root opened and read Stacks 0A2J Azumaya definition and line-twist lemma.'),
('OP-S3','used and rechecked in this run','Root opened and read Stacks 09CN exact sequence and 09CH Lemma10.133.3 universal principal-parts construction; independently checked the symbol argument.'),
('OP-S4','used and rechecked in this run','Root opened Beilinson–Drinfeld Opers and read relevant 1.2,2.7,3.1–3.3 statements for smooth complex curves.'),
('SC-C8-Stacks058Q','used and rechecked in this run','Root opened and read the finite-projective faithfully flat descent proposition and proof used in C8.'),
('SC85-Stacks0B5B','used and rechecked in this run','Root opened and read Riemann–Roch/duality statement used only for the conditional genus count.'),
('OP20-genus-one-background','carried as background without fault found','Standard H1(O)=k for a smooth proper genus-one curve carried as background; transition-matrix and nonsplit-extension h0 comparison were checked here.'),
]
for note,typ,outcome in extras:
    events.append([note,DATE,WHO,typ,outcome])

# Record each explicitly used prior note by its exact package-qualified ID.
# These are comparison leads; their reported status is never upgraded here.
prior_ids = ['P01','P03','P04','P05','P06','P07','P08','P09','C19','C25','C30','C33','E26','O01']
for note in prior_ids:
    events.append(['MPL_93_002-046 '+note,DATE,WHO,'carried as background without fault found',
                   'Read and used as an explicitly credited prior/context comparison lead; no re-proof or independent certification of its reported status.'])
events += [
['Hua 93-integral-schwarzian-level-p2',DATE,WHO,'used and rechecked in this run',
 'Compared supplied scans with Hua reported later pages; integral cocycle and precise monic local models checked in C1–C8 only. General global statement and priority not established.'],
['README S20',DATE,WHO,'used and rechecked in this run',
 'Projective and crystalline clusters support thematic connection; no specified Gauss–Manin realization or p-curvature computation on 047–091; cotes159 and64 not supplied.'],
]
with (RECORDS/'research_root_events.tsv').open('w', newline='') as f:
    w = csv.writer(f, delimiter='\t')
    w.writerow(['statement_id','date','who','type','outcome'])
    w.writerows(events)

(RECORDS/'research_root_quality_check.txt').write_text(
    '49/49 OP short quotes matched frozen page TeX after whitespace normalization only.\n'
    '68 root research items have actual per-term context searches across all four supplied context sources.\n'
    f'{len(events)} root check/context/source events written with explicitly limited outcomes.\n'
    'Post-freeze edits are confined to research records; no transcription write operations.\n')
print(f'Root research: {len(quotes)} exact anchors; {len(blocks)} context-searched notes; {len(events)} events.')
