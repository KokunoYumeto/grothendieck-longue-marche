"""Write root research check records, supplementing each note's own event.

Dates identify this run. Descriptions distinguish source reading, background,
proofs and computations. No frozen transcription file is opened for writing.
"""
from pathlib import Path
import csv
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent / "research_checks"
WHO = "GPT-6 Astra Pro; effort not exposed; MPL_93_092-134/root"
DATE = datetime.now(timezone.utc).strftime("%Y-%m-%d")
FIELDS = ["statement_id", "date", "who", "type", "outcome"]
background = []
def add(statement, kind, outcome):
    background.append([statement, DATE, WHO, kind, outcome])

for note, outcome in {
    "P01":"Prior Schwarzian normalization compared with frozen116-121 and B12-B14; its first-pass status retained.",
    "P02":"Prior self-correction is a parallel to A06, not the same manuscript calculation or a settled proof used here.",
    "P03":"Prior transformation-law caution compared with frozen114 and independently checked chain law in B14.",
    "P04":"Prior projective/rank-two link compared with B13 and F09; Legendre comparison is an additional identified example.",
    "P06":"Zero versus nilpotent p-curvature distinction checked against Katz1970 Theorems5.1 and10.0; scalar G0 is not itself p-curvature.",
    "P09":"Prior demand for an actual comparison is met by F09 in one example; general and unseen-cote identification remains open.",
}.items():
    add("MPL_93_002-046 " + note, "used and rechecked in this run", outcome)
for note, outcome in {
    "P05":"Prior calculation claim carried with supplied unreviewed status; deliberately not recomputed and not used to assert p-curvature vanishing.",
    "P07":"Proposed arithmetic bridge retained as a lead; Katz1972 Theorem3.2 full text was not verified in this run.",
    "P08":"Prior proposed elliptic comparison retained as a lead; F09-F10 supply an independently checked Legendre example without promoting all earlier claims.",
    "E12":"Prior warning about nilpotent coefficients used as a lead; D07 independently proves the needed linear coefficient statement.",
    "E26":"Prior Hasse-scalar claim retained as a lead; its normalization and sign not recomputed.",
    "C25":"Earlier cohomological comparison retained as a proposed target; no comparison map imported as established.",
    "C33":"Earlier crystalline comparison retained as a proposed target; no missing geometric identification assumed.",
}.items():
    add("MPL_93_002-046 " + note, "carried as background without fault found", outcome)
add("MPL_5+6_001-037 cote6 scan007 item10", "carried as background without fault found", "RESULTS_STATE pointer to earlier Cartier material used only as a lead in F03; source manuscript not supplied or read here.")
add("README S20", "used and rechecked in this run", "Explicit uniformization and Frobenius evidence in current pages; F09 adds one external geometric realization and F10 its theorem-based nilpotence consequence. General historical identification and cotes159/64 remain unverified.")
add("Hua findings 93-integral-schwarzian-level-p2", "targeted proof check", "Compared H-FIND with integral polynomial certificate, arbitrary-base local proof, descent and odd-characteristic Picard refinement D01-D14. Candidate priority status retained.")
add("Classical complex uniformization", "carried as background without fault found", "Used for connected simply connected universal covers and finite-type cusp behavior; not independently re-proved. No classification of arbitrary homogeneous open subsets asserted.")
add("Discrete subgroups of C under addition", "carried as background without fault found", "Rank0/1/2 lattice classification used after the independently checked fixed-point reduction in E08.")
for statement, outcome in [
    ("Beilinson-Drinfeld Opers sections1.1-1.4,2.6-2.7,3.3", "Primary preprint read for modern oper definitions, adjoint rigidity and central lift qualifications. No full-paper proof audit or historical attribution."),
    ("Deligne LNM163 I5.2-5.10", "Primary text read for second/third jets, Proposition5.8 and formula5.9.2; direct normalization gives theta=-G0. Geometric parallel only, no manuscript dating."),
    ("Deligne LNM163 II Theorem5.9", "Primary theorem and regular-algebraic/analytic flat-bundle categories read; checked scope excludes automatic algebraicity of an arbitrary additional marked section."),
    ("Serre GAGA section12 Theorems1-3", "Read primary statements for coherent cohomology, morphisms and algebraization on projective complex varieties; applied to compact curves and meromorphic tensors in B15/B17."),
    ("Katz1970 Theorem5.1", "Read zero-p-curvature Cartier descent statement and hypotheses; no independent proof of the theorem."),
    ("Katz1970 Theorem7.4 and Corollary7.5", "Read the conjugate-piece/Gauss-Manin comparison and its base-change or flat-Frobenius hypothesis; not conflated with an unconditional identification."),
    ("Katz1970 sections9.0-9.1 Theorem10.0", "Read global-nilpotence hypotheses; F10 checks their application to the smooth proper Legendre family, not every uniformizing equation."),
    ("Katz1970 Introduction (0.5.2)", "Read printed p176: the projective Legendre family and its smooth thickening over Z[1/2] are given explicitly. Corroborates the family used in F09-F10; theorem hypotheses separately checked."),
    ("McMullen2000 section2 Projective structures", "Read explicit real-analytic/nonholomorphic Fuchsian-section statement; used for closed marked genus at least2."),
    ("Loustau2015 Proposition6.4 and following paragraph", "Read maximal-totally-real explanation for Fuchsian section; no claim about every restricted family."),
    ("Zograf-Takhtadzhyan1987 primary abstract", "Read primary abstract corroborating nonholomorphic uniformizing variation; full original proof not retrieved."),
    ("Stacks tag058S Proposition10.83.3", "Read faithful-flat descent of finite projectivity and checked hypotheses for the solution line K in D10."),
    ("Hoshi2024 Definition6.2 Remark6.4.2 and section3", "Read level-one degeneration and characteristic2 locally exact-differential construction; limited comparison, no exhaustive novelty conclusion."),
    ("Dumas2009 section3.2 equation3.1", "Read solution-ratio/Schwarzian source statement; local normalization separately calculated in B13."),
    ("Takhtajan2014 sections2.1-2.2", "Read finite-type hyperbolic cusp coefficient and uniformizing projective-connection statement; used with compact GAGA in B17."),
    ("Harnad1999 section1 equations1.9-1.12", "Opened primary preprint and read Legendre period equation and inverse Schwarzian comparison; exact differential certificate independently verifies the equality in F09."),
]:
    add(statement, "used and rechecked in this run", outcome)
add("Katz1972 Theorem3.2 as cited by prior P07", "carried as background without fault found", "Unverified prior pointer: full theorem text unavailable in retrieval; no theorem from this source newly asserted.")
add("MPL_93_092-134 D01-D11 certificate root rerun", "computation or formal certificate", "Reran integral_certificate.py; exact symbolic and finite-ring checks passed. Output integral_certificate_root_recheck.txt. Finite examples are supplementary to arbitrary-ring proof.")
add("MPL_93_092-134 F09 certificate root rerun", "computation or formal certificate", "Reran legendre_certificate.py; exact differential residual and projective-coefficient difference both zero. Output legendre_certificate_root_recheck.txt.")

refutations = []
for statement, refined, outcome in [
    ("93:097:first_Riccati_normalization", "A06/B03/B12", "Later manuscript calculation itself replaces the early factor; corrected relation checked algebraically without editing the earlier reading."),
    ("93:100:literal_operator_without_f", "A09", "Literal formula fails at f=0; the contextual extra factor f is a reading question after freeze."),
    ("93:102:literal_Mobius_invariance_of_Dt", "B01", "Under t->1/t the coordinate affine connection changes; projective class is invariant. Reading question retained."),
    ("93:114:literal_pure_weight_transformation", "B14.chain", "Exact chain rule has an inhomogeneous Schwarzian term; t->t² supplies a direct counterexample to the literal formula."),
    ("93:117:quotient_by_all_diagonal_matrices", "C03/D11", "The projective matrix quotient is by common scalar matrices, not arbitrary diagonal matrices; uncertain wording remains frozen."),
    ("93:119:sheaf_Conn_on_P1_is_terminal", "C04", "Local quadratic differentials give many local sections; unique global projective connection on P1 does hold."),
    ("93:122:first_Frobenius_constants_preserve_G0_at_small_p", "D04/D05", "Hua examples t+t² and t+t³ independently checked; common first-three-Hasse-derivative constants required."),
    ("93:122:determinant_one_conclusion", "D09/D10", "Hua F5 example s=2t has determinant2d², never1; corrected unit-determinant statement proved."),
    ("93:126:mere_homogeneity_three_types", "E01.simply_connected_scope", "C* is a homogeneous open subset of P1 with fundamental group Z; simply connected uniformization scope retained."),
    ("93:126:full_PGL2R_stabilizes_upper_half_plane", "E02.positive_component", "Imaginary-part formula requires positive determinant; z->-z leaves the upper half-plane."),
    ("93:127:all_real_forms_are_boundary_circles", "E03.split_real_form", "Fixed-point-free real structure -1/conjugate(z) and anisotropic real conic disprove the unrestricted statement."),
    ("Hua VIIIb or S20:fiberwise_algebraicity_implies_algebraic_family", "B16/F06", "Explicit e^s family disproves the generic inference; primary sources separately confirm nonholomorphic Fuchsian variation in genus>=2."),
    ("Hua Xb:three_puncture_connection_restricted_from_zero_on_P1", "B18/F09", "Fixed cusp leading terms give nonzero rational coefficient, independently equal to the Legendre period coefficient. This is an outside-range contextual statement, not a reading of absent scans."),
    ("Draft interpretation B07:two_associated_bundle_relations_inequivalent", "B07", "Independent note QA showed the two relations are equivalent after replacing g by its inverse; corrected the research draft, never the frozen transcription."),
]:
    refutations.append([statement, DATE, WHO, "refuted, with the refined statement's id", f"Refined statement: {refined}. {outcome}"])

for name, rows in [("background_events.tsv", background), ("source_refutations.tsv", refutations)]:
    with (ROOT / name).open("w", newline="") as f:
        w = csv.writer(f, delimiter="\t")
        w.writerow(FIELDS)
        w.writerows(rows)
print(f"Recorded {len(background)} background/source/recheck events and {len(refutations)} refutation events.")
