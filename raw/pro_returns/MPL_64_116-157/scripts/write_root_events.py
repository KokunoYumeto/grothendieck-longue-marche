#!/usr/bin/env python3
"""Record post-freeze checks actually performed by the principal researcher.

Dates identify the UTC date of the work, not an invented sub-minute timestamp.
This script writes only research/root_events.tsv; it never changes transcription.
"""
from pathlib import Path
import csv

root = Path(__file__).resolve().parents[1]
who = "GPT-6 Astra Pro; effort inherited (runtime value not exposed); MPL_64_116-157/root"
rows = []

def event(statement_id, kind, outcome, date="2026-11-17"):
    rows.append([statement_id, date, who, kind, outcome])

target = "targeted proof check"
proof = "independent re-proof"
computation = "computation or formal certificate"
used = "used and rechecked in this run"
background = "carried as background without fault found"

event("L01", background, "Post-freeze comparison of scans118–121, Hua's pinning section, LM140-2 scans527–528 and570, and the result register; functoriality and square-normalization obligations remain open. This is textual/programmatic comparison, not a proof of the pinning.")
event("L02", proof, "AC01 proves the canonical exact-sequence comparison by evaluation, division by a section vanishing at t, and the coordinate transformation of principal parts; condition c is not proved.")
event("L03", target, "Substitution of lambda*delta into the weight-minus-one formula proves independence of phi(delta)*delta; it does not define differentiation or a connection.")
event("L04", proof, "AC02 proves rank two and the cyclic-difference kernel for distinct roots, hence uniqueness up to scalar; no square normalization inferred.")
event("L05", target, "Distinctness follows by applying multiplication by2 to the three chosen points; the line-divisor criterion and rational-half proviso were checked at the stated elliptic-curve hypotheses, while the earlier referenced proposition was not image-audited.")
event("T01", target, "Checked marked-automorphism rigidity by its scalar action on the tangent coordinate and fixed lattice basis. Holomorphic-family representability is carried from Hain2021 Propositions2.3–2.4, not independently reproved.")
event("T02", target, "Type-checked phi:L->V and the two scan132 expressions: the second use of phi(x) has the wrong source for x in V; replacing its argument by phi inverse(x) gives T02.R, solely in research notes.")
event("T03", proof, "AC03 derives J_z from conjugate transport and computes det(e1,J_ze1)=-1/Im(z); this verifies the manuscript's own withdrawal of the positive-orientation assertion.")
event("T04", target, "AC04 computes the antiholomorphic period ratio -conjugate(z) and applies the checked local holomorphic-period criterion; the later tau family supplies refinement T04.R.")
event("T05", target, "AC05 verifies the right-action ratio and sigma(gh)=sigma(h)sigma(g); no arithmetic inertia or LM2 multiplier result follows from this convention conversion.")
event("T06", proof, "AC05 proves the automorphy-factor cocycle, conjugation on translation columns rho(g), and the product (g,v)(h,w)=(gh,v+rho(g)w) for the exact scan149 action order.")
event("T07", target, "AC07 computes the total-family fundamental group over contractible H as Z^2 and distinguishes the framed-base orbifold classifying map from literal family and coarse-quotient readings; this is an explicitly stated mathematical interpretation.")
event("T08", proof, "AC07 uses the punctured torus retraction onto two circles and abelianization to obtain rank2, refuting the literal rank1 parenthesis under the stated type(1,1) hypothesis.")
event("T09", target, "AC06 constructs peripheral-conjugacy-preserving outer generators, checks the SL2(Z) presentation modulo inner automorphisms and the abelianization left inverse. Full Out(F2)=GL2(Z) is carried separately, not independently proved.")
event("T10", target, "Checked period coordinates C* x H, the conjugated representation R(g)=PgP, and the inverse scaling of periods/fiber under a tangent-frame change; no connection operator inferred.")
event("T11", proof, "AC08 proves freeness of the separate period actions and the four fixed points of the product element (-1,-I), including three surviving nonzero2-torsion points after removal of zero.")
event("T12", background, "Own proposed finite-stabilizer test case compared with LM4 D.12, LM6 A.22 and LM7_PUSH E.3; usefulness is an argued proposal, not a checked arithmetic comparison or a status upgrade.")
event("T13", proof, "Faithfulness forces the common absolute circle weight to1; replacing J by -J changes complex orientation by (-1)^n, and a rotation-invariant positive symmetric form in real dimension2 is scalar. These elementary arguments check only the stated compact-circle claims.")
event("T14", background, "Bounded post-freeze comparison: current complex stabilizers and dyadic normality do not compute characteristic3 elliptic automorphisms; LM140-2 notes S2 scans562–565 and the orientation request are carried as leads.")
event("G01", target, "Direct associativity proves y=uxu inverse and g'g=(u'u)(u inverse x'u)x; cancellation is not treated as refutation, and no unprovided definition of G0 is inferred.")

# Each documentary note is recorded as a use/comparison, not as a proof event.
documentary = {
"U01": "Scans118–121 announce a canonical pinning programme; compared with Hua and LM140-2 R22 scan570. Deferred work is inventoried without a new proof.",
"U02": "Scan121 explicitly defers condition c; compared with loose calculations123/125/126 and Hua. The linear kernel calculation is not treated as a solution of the square condition.",
"U03": "Scans134–139 contain a conjugate-eigenspace flag and an internal orientation withdrawal; mathematical check is separately recorded at T03/AC03.",
"U04": "Scan139's analytic-naturality question is recorded verbatim in short form and compared with Hua and LM140-3; the obstruction is separately checked at T04/AC04.",
"U05": "Scan140's request for an explicit outer action remains a manuscript deferral; modern generators are separately checked at T09/AC06, and later scan150 supplies no such generators.",
"U06": "Scan152's marginal2-torsion observation and deleted freeness assertion are inventoried as an internal withdrawal; the counterexample is separately proved at T11/AC08.",
"U07": "Scan132's request to see another explanation is inventoried as a deferral and linked to scans132–134; no standalone conjecture is invented.",
"U08": "Searched the frozen selection for uncertainty markers; distinguishes a doubtful question mark, an exceptional-locus sauf, and an unproved sufficiency assertion. Negative finding is bounded to supplied pages.",
"C01": "Scan128 is a separate title cover with no page count; compared to Hua page127. Documentary comparison only.",
"C02": "Scan129's doubtful21/22 count is compared to Hua's21 and the22 scan positions/21 retained mathematical pages; hand attribution and frozen uncertainty remain unresolved.",
"C03": "Scan131's internal heading and the later second attempt are compared to Hua's editorial divisions; archive foliation is not promoted to authorial mspage numbering.",
"C04": "Scans153/155 title sheets compared with Hua's claim that its page152 is blank; visible cover contradicts that limited documentary claim, not a mathematical theorem.",
"C05": "Scan124's Pappalardo thesis notice gives paper dates4/12November1980; compared with Hua's short identification, with no neighboring composition date inferred.",
"C06": "Scan127's Jambon notice gives its title and12December1980 lecture date; compared with Hua's footnote without dating surrounding drafts.",
"C07": "Scan157's reused examination notice and doubtful leading digit are retained; printed dates are compared to Hua's partial treatment without dating neighboring mathematical sheets.",
"R01": "Compared frozen doubtful marteaux-pilons on scan140 with Hua's orthodoxes; reading question remains unresolved and transcription unchanged.",
"R02": "Compared frozen doubtful zeta/xi diagram label on scan147 with Hua's printed2; mathematical role does not decide the ink.",
"R03": "Compared physical scan order147/148 with Hua's explicitly reversed exposition; original order is retained, with no transcription repair."
}
for note, outcome in documentary.items():
    event(note, background, "Post-freeze textual comparison; no mathematical proof check. " + outcome)

# Manuscript assertion IDs keep the location and the refinement explicit.
for sid, refinement, outcome in [
("MPL64.scan132.eq8.second_argument", "T02.R", "With phi:L->V, x in V must enter phi inverse before multiplication by i; the literal second formula is not type-correct."),
("MPL64.scan135.positive_orientation", "T03.R", "Under the displayed conjugate transport, det(e1,Je1)=-1/y<0; the author's withdrawal is correct."),
("MPL64.scan139.holomorphic_framed_family", "T04.R", "The displayed period -conjugate(z) is antiholomorphic; a holomorphic period tau or a changed base complex structure is needed."),
("MPL64.scan140.rank1_abelianization", "T08.R", "A once-punctured torus has pi1=F2 and abelianization Z^2, so the stated rank1 parenthesis fails."),
("MPL64.scan152.deleted_product_freeness", "T11.R", "(-1,-I) fixes all2-torsion points in the fiber; three nonzero fixed points remain after deleting the zero section.")
]:
    event(sid, "refuted, with refined statement " + refinement, outcome)
    event(refinement, target, outcome + " Research-only refinement; frozen text unchanged.")

for sid, outcome in {
"MPL64.scan119.eq78-81": "Canonical exact-sequence comparison proved at AC01/L02.",
"MPL64.scan120-121.weight_minus1": "Scaling cancellation checked at L03.",
"MPL64.scan123-126.kernel": "Cyclic-difference kernel and rank-two uniqueness checked at AC02/L04; detailed basis signs are separately in L92.",
"MPL64.scan146-148.action_conversion": "Anti-homomorphism and order conversion verified at AC05/T05.",
"MPL64.scan147-149.total_action": "Automorphy cocycle and semidirect translation action proved at AC05/T06.",
"MPL64.scan140.requested_outer_action": "Modern discrete construction supplied at AC06/T09; historical deferred wording and profinite bounds retained.",
"MPL64.scan149.universal_cover_wording": "Total-space pi1 obstruction checked at AC07/T07; corrected moduli interpretation explicitly distinguished from literal wording.",
"MPL64.scan151-152.period_frame": "Representation and inverse scaling checked at AC05/T10.",
"MPL64.scan132-134.circle_weights": "Faithfulness, orientation parity and invariant metric checked at T13.",
"MPL64.scan154.cancelled_associativity": "Associativity computation checked at G01, without identifying the poorly specified group."
}.items():
    event(sid, target, outcome)

for sid, outcome in {
"AC01": "Independent principal-parts proof as in L02; no finite-level completion inferred.",
"AC02": "Independent cyclic-difference/rank proof as in L04.",
"AC03": "Independent complex-structure and orientation calculation as in T03.",
"AC04": "Holomorphic-period obstruction checked using the cited local criterion, as in T04.",
"AC05": "Derived fractional action, automorphy cocycle, rho action, anti-homomorphism and period representation; exact symbolic certificate confirms identities.",
"AC06": "Constructed and free-reduced S,T lifts and checked presentation modulo inner automorphisms; full outer-automorphism theorem remains background.",
"AC07": "Elementary homotopy and abelianization checks; orbifold interpretation separated from literal family wording.",
"AC08": "Separate freeness and product fixed-point counterexample proved."
}.items():
    event(sid, proof if sid in {"AC01","AC02","AC03","AC08"} else target, outcome)
event("CERT.analytic_certificates", computation, "Ran research/analytic_certificates.py with SymPy1.14; output research/analytic_certificate_output.json records exact cyclic-kernel, J, matrix/cocycle and free-word identities. Finite symbolic verification is not a formal proof of general cited theorems.")

# Register claims are used with their supplied status, never silently promoted.
for sid, outcome in {
"LM4 D.12": "Open torsion question carried from RESULTS_STATE orientation; current geometric fixed points give a proposed test case only.",
"LM6 A.22": "Open CM/arithmetic-image lead carried from RESULTS_STATE orientation; no arithmetic comparison map constructed.",
"LM7_PUSH E.3": "Open CM arithmetic-image lead carried from RESULTS_STATE orientation; complex stabilizers do not settle it.",
"MPL_93_002-046 P09": "Own-idea comparison programme carried from register; modern S03–S05 tests do not identify missing original cote93/cote159 connections.",
"MPL_93_002-046 E14": "Conjectural/deformation lead carried from register only; underlying cote93 text was not supplied and no new proof is claimed.",
"MPL_93_002-046 E16": "Conjectural/deformation lead carried from register only; underlying cote93 text was not supplied and no new proof is claimed.",
"MPL_93_002-046 C29": "Own-idea moduli/deformation lead carried from register only; no status change.",
"README S20": "Historical comparison programme read and tested within available scope; actual cote93 and159 texts are absent, so historical identification remains unaddressed."
}.items():
    event(sid, background, outcome)

for sid, outcome in {
"CTX.LM_140-2_notes.R22.scan570": "Level-four Jacobi/Legendre programme located and compared to L01/L05/U01; no proof of the earlier note or unseen scans asserted.",
"CTX.LM_140-2_notes.R24.R28.R29.scans527-528": "Earlier Legendre-family/level-two monodromy leads located; distinguished from the level-four programme on scan570.",
"CTX.LM_140-2_notes.467-1": "Earlier explicit outer-action programme compared to T09/U05; retained as context, with new F2 construction separately checked.",
"CTX.LM_140-2_notes.467-5.467-7": "Earlier abstract extension/B3 leads compared to T10/H02; Hua's lattice realization credited separately.",
"CTX.LM_140-2_text.scans259-263": "Modular topos, rigidification and universal-family extension read as supplied transcription; no new image audit of those scans.",
"CTX.LM_140-3_notes.R30-R36.scans19-20": "Family, conjugation, rank, conventions, special-orbit and ineffective-action leads compared to T01–T12/U03–U06; geometric quotient interpretation stated with its limits.",
"CTX.LM_140-2_notes.S2.scans562-565": "Characteristic3/special-invariant lead compared to T14; absence of corresponding current computation explicitly retained.",
"CTX.Hua64.V.first_attempt": "Read relevant first-attempt section for family, inverse, orientation and rank repairs; comparisons are not new readings of ink.",
"CTX.Hua64.V.second_attempt": "Read relevant second-attempt section for action conventions, page reversal, diagram label and tangent frames; source repairs remain credited.",
"CTX.Hua64.Legendre": "Read pinning and loose-sheet interpretation; condition c remains open and loose attachment is credited as Hua's inference.",
"CTX.Hua64.VI": "Read arithmetic interpretation and documentary claims for research; uncertain local-ring hypothesis and sign questions do not alter frozen text."
}.items():
    event(sid, background, outcome)

for sid, outcome in {
"LIT.Hain2021.Propositions2.3-2.4": "Primary author PDF read at pp13–15; checked local holomorphic-period argument and representability statement used in T01/T04; no independent proof of the whole representability theorem.",
"LIT.Hain2021.SL2_presentation": "Primary author PDF p10 presentation matched to exact free-word identities in AC06; presentation itself carried as established literature.",
"LIT.Hain2021.OrbifoldModuli": "Primary author PDF section3 and Theorem3.18 read for automorphism-retaining quotient; compared to elementary total-space pi1 obstruction.",
"LIT.Hain2014.TangentAndBraid": "Primary arXiv v3 Proposition5.16 and Propositions8.1–8.2/Corollary8.3/Remark8.4 read; checked tangent/Hodge duality and central-square qualification against separate matrix certificate.",
"LIT.Grothendieck1960-1961.I": "Primary text sections1–3 read for Torelli/Jacobi terminology and family-level historical context; general representability proof not independently audited.",
"LIT.Grothendieck1960-1961.X": "Primary text introduction and section3 read for genus-one lattice discussion; Serre appendix located, without importing an unverified higher-dimensional theorem.",
"LIT.Katz1968.Legendre": "Primary pp71–74 read for period/Hasse example; modern exact differential and p=3 calculations have independent certificates.",
"LIT.Katz1970.CorrectHypotheses": "Primary Theorem5.1,7.3.3,7.4–7.5 checked for zero-vs-nilpotent p-curvature, smooth-base Frobenius-flatness and elliptic exponent bound2; general theorem carried, not independently reproved.",
"LIT.Stacks.00P7": "Opened exact primary statement Lemma10.119.7; DVR characterization supports arithmetic local proof under explicitly conditional DVR hypothesis.",
"LIT.Stacks.02JN": "Opened exact primary statement Lemma10.104.2; regular hypersurface quotient is Cohen–Macaulay, with the nonzerodivisor hypothesis matched.",
"LIT.Stacks.031O": "Opened exact primary Serre normality criterion Lemma10.157.4; R1+S2 application checked against the arithmetic proof.",
"LIT.Stacks.0BNH": "Opened exact primary completion statement Lemma10.97.1; distinguished m-adic quotient completion from unsupported T-adic interpretation.",
"LIT.Stacks.02GI": "Opened standard-etale definition; derivative-unit criterion matched to u^2-ru-h over D(P).",
"LIT.Stacks.0AP2": "Opened primary permanence statement for etale algebras over Dedekind domains; its normality application checked in arithmetic proof.",
"LIT.Stacks.02DN": "Opened ordinary-double-point reference over fields; mixed-characteristic claim explicitly limited to nondegenerate tangent cone rather than an equicharacteristic completed-ring assertion."
}.items():
    event(sid, background, outcome)

event("INTEGRATION.review_fixes", used, "Applied all four textual corrections in research/integration_review.md: current quotations in T12/R03, actual C1 location, and finished H03 cross-references; rendered custom transcription macros as literal code or explicit doubts in Markdown. Only research files edited.", "2026-11-18")
event("INTEGRATION.final_scope", used, "Read the complete independent S03–S05 review and successful output; adopted its explicit parameter-base tensor specialization wording in S05 and clarified S06's moduli target. Added word-number spacing in research prose. These are scope/presentation refinements, not edits to frozen transcription or new historical evidence.", "2026-11-18")

out = root / "research/root_events.tsv"
with out.open("w", encoding="utf-8", newline="") as handle:
    writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
    writer.writerow(["statement_id", "date", "who", "type", "outcome"])
    writer.writerows(rows)
print(f"Wrote {len(rows)} accurately scoped root events to {out.name}")
