#!/usr/bin/env python3
"""Build the report from the frozen row inventory and audited narrative."""
from pathlib import Path
import json
import re

base = Path(__file__).resolve().parents[1]

def source(name):
    p = base / name
    return p if p.exists() else base / 'audit' / 'ledger_inputs' / name

def show(value):
    return ', '.join(map(str, value)) if isinstance(value, list) else str(value)

def cell(value):
    return show(value).replace('|', r'\|').replace('\n', ' ')

rows = []
for prefix in ['AB', 'CF', 'DE', 'ROOT']:
    rows += json.loads(source(prefix + '_coverage.json').read_text())
by_id = {r.get('id', r.get('row')): r for r in rows}
assert len(by_id) == len(rows), 'Repeated coverage row'
mandatory = [f'F{i}' for i in range(1, 27)] + [f'G{i}' for i in range(1, 5)]
assert all(k in by_id for k in mandatory)
order = mandatory + [k for k in by_id if k not in mandatory]
table = ['INCOMPLETE', '', '| Row | Manuscript location | Words or assertion examined | Verdict and exact scope | Paper statements | Opened source / proof |', '|---|---|---|---|---|---|']
for ident in order:
    r = by_id[ident]
    loc = r.get('scan')
    if not loc:
        loc = '149; manuscript pp. ' + show(r.get('manuscript_pages', '')) + '; scans ' + show(r.get('scans', ''))
    table.append('| ' + ' | '.join(cell(v) for v in [ident, loc, r['words'], r['verdict'], r['statements'], r['source_opened']]) + ' |')

checks = json.loads((base / 'audit' / 'assembly_checks.json').read_text())
counts = checks['status_counts']
narrative = f'''

# FLAGGED_149 — research report

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). 12 November 2026. No priority is claimed.

## Status and scope of the return

The requested project is **not complete**. The table above contains all thirty named rows, F1–F26 and G1–G4, together with {len(rows)-30} additional sweep rows. The paper contains {checks['numbered_results']} numbered statements: {counts['Proved']} labelled Proved, {counts['Known']} Known, {counts['Refuted']} Refuted, and {counts['Open']} Open. These counts describe numbered statements; a single Open statement can contain several precise unresolved objectives, and a coverage row can combine a proved correction with an unresolved broader assertion. They are not a claim that every requested row is settled.

The result ledger has exactly one row for each numbered statement and preserves its entire statement and hypotheses. The reading ledger contains {checks['reading_rows']} entries. The bibliography has {checks['bibliography_entries']} entries, including separately identified versions and the supplied manuscripts and prior return; this number is not a count of independent research papers. All citation keys used in the TeX have entries. Verification notes identify what was actually opened.

The incomplete label records mathematical incompleteness. No environment disconnection or external termination is asserted. The exact unresolved statements, the arguments attempted, their failure points, and the next mathematical obligations remain in the paper and below.

## What was read

We swept both supplied transcriptions of cote 149 in full: scans 1–90 and 91–136. The section-by-section inventory covers scans 1–40, 41–104, and 105–136, including statements without an explicit question mark when they contain a substantive admitted step. We also read cote 142 scans 1–22. Its opening sheets were read in the order 3, 4, 6, 5, 7, then 8 onward. Cover material and the end of the opening passage introduce no additional mathematical assertion. The inventory includes withdrawn proposals as withdrawn, without restoring them as hypotheses.

The image checks concentrated on the passages where wording changes the mathematics. In cote 149 these include scans 13, 21, 24, 34–40, 45, 52, 54, 79, 81, 85, 90, 102 and all thirteen supplied section-4 pages. In cote 142 the supplied opening images were inspected, particularly scans 4–14. The reading ledger records the image evidence locally and identifies readings for which no image was supplied. An inspected image is editorial evidence, not a final reading. The manuscript page and archive scan number remain separate fields throughout.

We read the supplied R149_WARGAME_EXCERPTS and R149_NOTES and the relevant proof text of the attached CYCLOTOMIC_KERNEL return. That return is cited by exact statement where the prompt permits it. Its prose is not treated as independent literature authority. The source audit files record the primary texts, opened versions, theorem numbers, hypotheses, and comparison maps used in the present paper. Full downloaded research papers are not redistributed in this ZIP.

## Principal mathematical findings

### Group theory and faithfulness

A1 supplies the geometric cohomological dimension and the arithmetic value with the exact real exception at the prime 2. Formal reality concerns the field itself; the proof does not infer it solely from a real embedding of its constant number field. A2–A5 supply the finite-order classification, free and proper surface-group assertions, cusp intersections and normalizers, and the omitted inverse-limit comparison. Every inverse-limit projection used there is proved surjective.

A6 proves the strengthening of the centralizer assertion for positive transcendence degree. Its outer-faithfulness reduction uses the actual successive quotients from the absolute geometric function-field group to a one-variable function field and then to a hyperbolic curve group. A7–A9 record the additional field-restriction, cofinal-model, extension-reconstruction, and continuous-lifting assertions found in the sweep. In B10, the characteristic-p faithfulness statement retains the identity marking over the arithmetic base groupoid. The Frobenius comparison is calculated with that marking.

### Rigidity, translations, and Kummer theory

The open-subset translation lemma of scan 37 is false for a once-punctured elliptic curve. For Y=E minus{{0}} and u nonzero, the open W=E minus{{0,−u}} satisfies W+u contained in Y. B4 proves the exact curve-type correction. G3 proves the whole-curve stability statement used in cote 142: Y+u=Y forces u=0 for every hyperbolic curve. The kernel-of-homology computation in B4 identifies why shrinking W in scans 39–40 does not repair the one-cusp failure.

The separate assertion on scan 38 that a nonzero toric-kernel translation has no intersection with Y is false in genus zero. In the embedding t↦(t,t−1) of the thrice-punctured line, multiplication by (2,3) sends (2,1) to (4,3), both on the curve. B13 proves the positive-genus assertion and gives an exact genus-zero intersection criterion.

B1 refutes finite generation for general semiabelian rational-point groups while proving the structure needed for Kummer injectivity. B2 gives the exact completion maps and their omitted-prime torsion kernels. B5 proves the characteristic-zero rigidity corollaries through the actual tower fibre extensions. It does not require the false intermediate assertion that every elementary hyperbolic tower immerses in a semiabelian variety. B11 gives explicit affine counterexamples to that assertion, including a tower with genus-zero base and fibres. B12 refutes the claimed semiabelian Albanese homology comparison for arbitrary reduced sources by the nodal rational cubic; B3 supplies a proof of the surviving corollary without that comparison.

For characteristic p, B6 proves full point-section injectivity under the actual semiabelian-immersion hypothesis, using finite-field Lang torsors and a precise henselian comparison. B7 supplies a computable failure for the prime-to-p abelianized extension. B8 proves prime-to-p nonabelian point injectivity for all punctured genus-one curves. The higher-genus range remains explicitly in B9; its current concrete test and any resolved subcase are recorded there and in the adjacent result rather than inferred from the abelian quotient.

### Sections over a base and reduction

C1–C5 prove extension across codimension at least two, the trait criterion, and the hyperbolic homotopy exact sequence with the exact prime-to-residue-characteristic qualifications. The nonabelian inertia map is the cusp inclusion composed with multiplication by the actual intersection multiplicity. This includes a single cusp and keeps the source tame group explicit.

C6 computes the sign of the cusp extension from transition functions: with the stated fibre-coordinate convention it is the normal-line Chern class. Reversing the loop generator changes the sign, and the conormal bundle is the dual line. C7–C8 prove the arithmetic completed-unit and splitting-torsor statements, including the injection of ordinary units. C9 computes tangential specialization on the regular-and-invertible locus of the leading coefficient.

F9 gives the precise pinned-topos reconstruction statements and the relative natural-transformation convention. It also supplies explicit counterexamples to unrestricted fullness, including the finite-field case. F17 gives the valid nonabelian good-reduction criterion, a compact-type genus-two degeneration invisible to abelian and class-two outer monodromy, the class-two detection of colliding cusps, a five-loop obstruction to a smooth residue action, and the quadratic-twist counterexample to the proposed converse. F17.6 proves the global stable-bad obstruction for every residue splitting. F17.7 identifies condition e exactly with potential good marked reduction, for every residue splitting, and constructs the realizing curve over the original residue field by explicit finite Galois descent. Allowing a finite residue extension gives the same condition. F17.8 computes a degeneration with two Galois-conjugate nodes, supplying the needed qualification to individual-node invariance.

### Arbitrary valuations and boundary strata

D2 proves the valuation-ring description of the Riemann–Zariski limit without resolution. Its noetherian stalks are the field and DVRs; a DVR need not be divisorial. D3 constructs valuations of K(x,y) with value groups Q and Z[1/2] and residue K. These examples control several failures that rational rank alone would miss.

D4 gives I_v=Hom(Gamma_v,T), equivalently the character group of (Gamma_v tensor Q)/Gamma_v, and constructs a continuous splitting of the residue Galois sequence. Its l-adic rank is dim_F_l(Gamma_v/l Gamma_v). D5 removes the maximal divisible convex subgroup of the value group to obtain a coarsening w with the same actual inertia and proves N_G_L(I_v)=D_w. The geometric normalizer and both decomposition-normalizer variants are then calculated explicitly. D6 provides actual unequal-subgroup examples.

D7 proves the center-detection converse for DVRs on the stated elementary towers and refutes its arbitrary-valuation extension, even on a product of hyperbolic curves. D8 types valuation restriction and its local Galois maps. D9 corrects the actual L in scan 127 by exhibiting why the function-field formula fails and proving the stated U version through the attached result.

E1–E3 compute the local meridians, prove the product compactification's terminal property among smooth proper SNC compactifications, and give the exact saturation criterion for openness of a valuation inertia image at a crossing. Equality of rational rank with branch count is insufficient. E6 additionally constructs an algebraic but infinite residue extension and proves the extra arithmetic finite-index requirement.

E4 gives two equivalent criteria for the left exactness of the stratum sequence: the vanishing of its normal-bundle Chern boundary on pi_2, and the existence, after finite étale base change, of roots of each normal line bundle at every finite level. E5 refutes universal vanishing. A blow-up of a boundary point of a product of three thrice-punctured lines yields a complete P1 stratum with normal degrees (1,−1); its boundary sends a to (a,−a), while the global meridian map sends (m,n) to m+n.

### Surfaces, completion, and the additional cote 142 programme

G1–G3 prove the periodic rigidity assertions, including a purely topological proof and the failure at level 2. G11 tests the different plausible meanings of the doubtful homology qualification through explicit comparison pairings and counterexamples. G4 proves contractibility of the finite-cover components, their stabilizers and the finite orbit count. Its characterization of finite stabilizers by free realizations explicitly allows the target surface to vary. G5 refutes the all-finite-subgroups margin by the genus-two hyperelliptic involution.

G6 constructs the Hausdorff profinite envelope with continuous associative composition. The completed right orbit is the quotient of widehat(A_X) by left cosets of closure(S_u). G7 and G9 prove why the closure and closed-stabilizer qualifications are necessary. G8 verifies the surface hypotheses and the uniquely marked factorization; G10 proves the already-profinite variant.

Z142a corrects the no-isolated-points claim in type (0,3). Z142b constructs the characteristic-zero algebraic description through actual Hurwitz-stack transport and compares it with the completed topological category. Z142c gives an Artin–Schreier counterexample to the full fundamental-group base-invariance premise in characteristic p. Z142d constructs the field-automorphism action with its exact inner ambiguity. Z142e computes a degree-six family refuting the ordinary-path interpretation of the asserted two-sided isotopy orbit after filling holes. Its explicit factorization uses two finite étale covers and two puncture fillings, so the example lies in the category generated by the permitted arrows. Z142f gives the exact source-containment and critical-point conditions for the restricted maps. The unspecified wild and enlarged-category programmes remain in Z142g.

## Corrections to the supplied leads, notes, and prior claims

| Claim | Correction and evidence |
|---|---|
| R2, its cusp centralizer formula | The exact centralizer formula survives with its hypotheses. The comparison identifies zero cyclotomic centralizer with noncuspidality. Exhaustion by rational points still requires the section assertion recorded in ZCF6. The prior four-cusp orbit argument cannot itself supply that exhaustion. |
| R3 and the scan-45 star | F8a checks the attached B1 proof, including the additional choice of an auxiliary rational prime unramified in the number field. The result includes every open arithmetic subgroup. |
| R4 and the proposed Torelli shortcut | An integral symplectic Tate-module comparison by itself does not supply the isomorphism of principally polarized abelian varieties required by the proposed step. No proof uses that unproved passage. The compact-type calculation and the nonabelian node/loop argument are given explicitly. |
| H1 | The fixed inertia is the product of exactly those l-adic factors on which the l-adic cyclotomic character is trivial. Nontriviality of one factor does not force triviality of the entire cyclotomic character. The attached AE2/AE4 example and ZCF5 give the corrected formula. |
| H2 | F17.6 proves the full stable-bad obstruction, including the nonabelian log comparison and the affine cusp count, for every residue splitting. F17.7 proves that e, both over the original residue field and with finite residue extension, is equivalent to potential good marked reduction. F17.8 refutes literal invariance of each individual node under the whole residue Galois group; an open subgroup fixing the node and its branches is required. |
| F5 lead | The requested open-subset lemma fails for (1,1); the whole-curve stability assertion remains true. B4 and G3 give the two actual maps and their proofs. |
| Global immersion and genus-zero fibres | B11 refutes both the general semiabelian-immersion assertion and the claimed torus consequence of genus-zero fibres. The surviving tower rigidity is proved by fibre-extension pullbacks. |
| F6 lead / scan 34 | Mordell–Weil finite generation for an abelian quotient does not give finite generation of G(K) with a torus part. B1–B2 prove the needed divisible-intersection statement and exact Kummer kernels. |
| Normal/conormal; moving-cusp test | C6 determines the sign by gluing and an O(−1) test. P1 minus{{0,infinity,t^mu u}} has colliding boundary over the trait; it tests the local multiplicity, while its trivial normal line cannot detect the global Chern sign. |
| F17 / S23 | Homological conditions do not imply good reduction. A geometric pulled-back residue action can coexist with bad reduction, as the explicit quadratic twist shows. Stable-bad and potentially-good cases are treated with their actual specialization maps. |
| F19–F22 leads | Divisible value-group directions may disappear from inertia. Rational rank and the manuscript codimension do not determine the l-adic inertia ranks. The arbitrary-valuation normalizer and center-converse need the corrections in D3–D7. |
| F25, rank-equality and algebraic residue | E3 replaces rational-rank equality by its exact finite saturation-index criterion. E6 proves that algebraic residue need not be finite and gives the additional arithmetic openness condition. |
| F26 / prior diagonal calculation | The nonzero diagonal meridian does not force the full stratum fibre group to inject. E5 computes the nonzero Chern relation killed by the global sum map. |
| Riemann–Zariski model opens, scan 123 | A common proper model proves closure under finite unions and intersections. ZD4 refutes the written finite-union negation and proves the nonscheme assertion in transcendence degree at least two. |
| Continuity in B-prime | Open stabilizers of rational functions give finite orbits of level generators. Their stable compositum supplies an invariant finite étale quotient; ZCF12 descends it over the original field and constructs the actual continuous section. This corrects our earlier overstatement of an additional finite-level gap. The comparison is with the cyclotomic-kernel fixed-point formulation of B at the same base field. Actions without the open-stabilizer hypothesis remain in ZCF6(4). |
| General completion and scan-14 uniqueness | The actual completed stabilizer is its closure in the endpoint completion. Injectivity alone need not give a closed image. G7/G9 give counterexample categories and G6/G8 prove the replacement. |

The readings ledger records the mathematical corrections to the symbols and words themselves, including the written L/U issue, normalizer/centralizer, p-primary versus exponent-p torsion, the curve over which a cover is taken, and the isotopy and homology alternatives. No doubtful glyph is declared finally settled.

## Precise unresolved assertions and the attacks made

### B9: the higher-genus prime-to-p point problem

B9 proves the reduction from finitely generated fields to finite fields separately for each geometric curve type, through the actual prime-to-p relative extension and its generic/special fibre-product maps. The compactification homomorphism carries an affine point-section collision to a proper one, preserving its geometric conjugator and the two distinct points. Together with the finite-field reduction and the genus-zero and punctured-genus-one results, the remaining universal objective is exactly point-section injectivity for smooth proper curves of genus at least two over finite fields. The original formulation over fields finitely generated over F_p is retained, with the full arithmetic quotient and geometrically prime-to-p kernel specified in B9. Equal section classes imply compatible lifts on every such cover and p-primary Jacobian differences after the common finite extension. The known finite exceptional decomposition-point set confines a possible coincidence but does not prove that the set is empty. Its behaviour under covers is recorded in the final B9 text.

The successful genus-one argument holds the compact elliptic curve fixed under multiplication covers while the number of modulus points grows past the fixed p-power torsion order. Higher-genus covers introduce extra Jacobian factors; no uniform bound for their p-primary differences has been proved here. Proper covers also supply no growing cusp modulus. B14 resolves the former genus-two F3 test y^3−y=x+x^{-1}: a double cover produces differences of orders divisible by 5 and of exact order 6, and the prime-to-3 Lang quotient gives a degree-640 finite étale cover over F27 with a rational point over P and none over Q. The conclusion persists after every finite constant extension. B15 also separates the genus-two pair on y²=x⁵+(x²+1)² over F5, whose initial divisor difference has exact order 5. Its elliptic quotient has eight rational points and gives a degree-16 separating cover. Both examples are resolved over all finite constant extensions. These finite examples are not extrapolated to all curves; the remaining smallest type is the universal proper genus-two finite-field assertion, rather than either of these now-resolved pairs. For odd-characteristic genus two, B9 also gives an exact finite test for each of the fifteen branch-pair double covers: the two norm maps reduce the surviving p-primary question to whether a specified 2-torsion divisor class vanishes. Its Riemann–Roch test is explicit; universal success of those fifteen choices is unproved. A further joint-cover argument proves that all successful lift choices are compatible on the connected degree-16, genus-17 pullback of multiplication by 2 on the Jacobian. The exact hyperplane norm identity confines the remaining class to a finite 2-primary kernel killed by 8. That joint kernel is nonzero for every such curve: it contains the actual subgroup pi-star(J_C[8]), isomorphic to (Z/4)^4. This identifies a concrete limitation of the norm data. It does not supply a colliding point pair, since no nonzero class in that subgroup has been identified with the required lifted-point difference. The next general step must either control these particular point differences through further covers, eliminate the exceptional set by another argument, or produce a verified collision, with the exact section comparison retained.

### ZCF6 and ZD10: points, fixed pro-points, and birational lifts

For U=P1_Q minus{{0,1,infinity}}, the zero-centralizer condition proves that a section is noncuspidal. The requested conclusion that every such section comes from a rational point remains unproved here. The fixed-pro-point uniqueness assertions are proved; existence is retained as the precise missing statement. The corresponding birational objective asks for decomposition containment of every section of G_Q(t) over G_Q.

For an arbitrary section s of U, ZD10 constructs the actual pullback extension E_s=G_Q(t) times_{{pi1(U),s}} G_Q. A birational lift is exactly a continuous splitting of this extension. All point and cusp sections are lifted. The normalizer calculation identifies a decomposition group once an appropriate nonzero inertia subgroup has been supplied; it does not construct one for arbitrary s. Abelianizing the kernel checks only abelian lifting obstructions and supplies no implication back to the required splitting.

The precise opened cuspidally central lifting theorem has positive-genus and torsion-packet hypotheses and a smaller quotient. Its comparison with E_s is written out. The pinned-topos reconstruction theorem gives actual points from full pinned-topos maps, but a section of the fundamental-group quotient has not been lifted to such a map. The map that would perform that lift is the unresolved obligation, rather than an assumed equivalence of categories.

ZD11 gives an additional exact reduction through Bresciani's Theorems A and B. For a fixed hyperbolic curve over a field finitely generated over Q, universal birational liftability over all finitely generated extensions is equivalent to the corresponding universal section-conjecture assertion. The proof writes the base-change section over F(t) and the actual fibre-product identification. This establishes the strength of the manuscript's universal demand; it proves neither of the equivalent universal assertions.

### ZCF6(4): the remaining abstract semilinear actions

ZCF12 now proves the finite-level reduction for every action with open stabilizers of rational functions; normalization of an initial deck group is not assumed. The compositum of the finitely many translates of a set of level generators is a stable finite covering field. Its quotient curve inherits the actual action on the open curve and its boundary. A normal open coefficient-and-generator stabilizer, followed by effective finite Galois descent, gives a hyperbolic curve over the original field and an actual continuous arithmetic section. Cofinality of the two covering systems identifies their compatible points on the completed pro-covers, with their full Galois actions. Thus continuous B-prime is equivalent to the cyclotomic-kernel fixed-point formulation of B, quantified over all hyperbolic curves at the same base field. The proof does not establish that fixed point's existence.

The additional unresolved scope is an abstract semilinear action without open function stabilizers. ZCF6 writes it as an explicit crossed-homomorphism problem relative to a fixed tangential action. We have neither constructed nor excluded an action normalizing none of the deck groups of finite hyperbolic quotients. Without the continuity clause, the orbit of a field generator may be infinite, so the generated compositum need not be a finite covering field. This identifies the exact failed step and retains the fixed-point assertion itself as unresolved.

### Z142g: wild covers, arithmetic images, and the category after filling holes

The characteristic-zero category is constructed. The full characteristic-p base-change premise is refuted by an explicit Artin–Schreier class, but that does not define or refute every possible wild replacement. The requested wild category still needs specified objects, arrows and transport compatible with factorization. The enlarged hole-filling construction requires a precise isotopy relation and composition relations; ordinary path isotopy is refuted by Z142e. The intrinsic arithmetic-image programme is retained as a programme with the existing action constructed and the requested intrinsic characterization unproved. No undefined predicate, including the manuscript's “pas trop loufoque,” is assigned a theorem value.

## Computations and proof audit

The ZIP includes the actual programs and their recorded outputs. AB_checks checks the elliptic examples, rational-point enumerations, nodal normalization, quotient-family divisors, the toric translation intersection, meridian spans, and the exact 15-by-16 hyperplane-incidence identity in the joint genus-two cover. CF_checks checks the genus-two and elliptic discriminants, the colliding-cusp class-two action, five-loop homology lines, quadratic twists, Kummer multiplicities and the finite-field root-count inequality. CF_hyperplane verifies eight affine singularity ideals, eighteen branch-slice determinants and 216 branch triples for the explicit ample surface used to refute the dominance assertion. DE_checks verifies the finite norm computations, meridian kernels, Chern relation, residue-recovery polynomials and incidence example. G_checks verifies the finite homology and mapping-class examples, the factorization of the degree-six isotopy counterexample, its twenty distinct source punctures, and the change in its critical values. F7_test supplies 34 exact checks for B14, including the smooth sextic/quartic/octic models, all relevant point and Frobenius counts, and the degree-640 Lang construction. F7_test5 supplies twenty exact checks for the degree-16 characteristic-5 construction in B15. CF_h2_checks verifies the conjugate-node discriminant and jets, 153 thickness/modulus checks for the node map, the isomorphism of the CM elliptic components, and their smoothness modulo 5.

Finite computations verify the displayed examples and algebraic identities. Infinite valuation, profinite, completion and inverse-limit assertions have separate proofs; none is inferred from a finite search. The cross-audit checked C1–C9, F9.1–F9.5 and F17.1–F17.5 against the maps used by the valuation part, including the compatible node roots in F17.4. F17.6–F17.8 were audited for the full logarithmic comparison, the tree/graph homology arguments, the finite-extension maps, and the actual node permutation; the key primary texts were reopened during that audit. G1–G11 and the Hurwitz comparison were separately checked; the surface-stabilizer quantifier and the generated-category scope of the isotopy example were corrected during that review. ZCF8's finite-level descent, ZCF9's retained-point construction, and ZCF12's invariant compositum, effective descent and cofinal pro-point comparison were also reviewed.

The assembly program checks one result per ledger row, exact status agreement, nonempty reading fields, distinct identifiers and complete citation keys. The final audit records the LuaLaTeX/BibTeX build and PDF checks. The mathematics remains subject to the explicit Open labels regardless of successful compilation.

## Files and reproduction

The ZIP contains the main TeX file and compiled PDF, all section inputs, the result and reading CSV files, the verified bibliography, this report, and code with exact outputs. The audit directory retains source-verification notes, the metadata and coverage inputs used to build the ledgers, assembly checks and build/visual records. code/README.md gives the ordinary LuaLaTeX/BibTeX sequence and Python commands. The downloaded TeX runtime, caches, temporary files and copies of external papers are excluded.
'''

(base / 'FLAGGED_149_report.md').write_text('\n'.join(table) + narrative, encoding='utf-8')
summary = {'coverage_rows': len(rows), 'mandatory_rows': len(mandatory), 'additional_rows': len(rows)-len(mandatory), 'unique_ids': True, 'all_mandatory_present': True}
(base / 'audit' / 'coverage_checks.json').write_text(json.dumps(summary, indent=2) + '\n')
print(json.dumps(summary, indent=2))
