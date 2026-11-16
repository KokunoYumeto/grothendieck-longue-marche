# Independent DE audit of A68

**PASS, mathematical proof, primary-source normalization, and complete exact certificate.** The full candidate was read before checkpoint13 capture, and the formatting-repaired 250-line text was reread after capture. This ledger is written after root released notes/code writes; no canonical paper or register is changed by this audit.

Audited candidate: `notes/fgh_A68_draft.tex`, current SHA256 `753cc556611411a6d230b10713344fb42f108861036244aaa6f5031a587183f6`. Certificate source SHA256 `81cd9a3387b673cade7f3af03b608f5eb57d9462f7bd844d55e8068c176d97a1`; complete output SHA256 `8ce6e618f1804f2f0e961b676202e7b426cb210b0299a203bf89aca757d103e2`.

## Actual curves, maps, and Jacobian factor

The degree-sixteen map satisfies the elliptic equation and factors through the specified fourth-root torsor followed by elliptic duplication. The divisor of the torsor function is exactly the four indicated elliptic two-torsion points, each with odd valuation, so the four punctures have ramification index four. The displayed dihedral generators preserve the actual map, satisfy its relations, and give sixteen different deck transformations.

The reciprocal involution and the subsequent free involution give the stated genus-two function field, not merely an isomorphic branch configuration. Its quintic has discriminant minus two to the twentieth power. The two explicit pulled-back differentials span the claimed odd plane; its rotation translate is complementary because the two eigenvalues in each paired index are distinct. Together with the even differential space of the actual genus-three quotient, this proves the full Jacobian isogeny with the same factor used in the reduction argument.

## Exact invariant normalization and original reduction criterion

**verified:** The original Liu author PDF was independently opened at <https://www.math.u-bordeaux.fr/~qliu/articles/genre2.pdf> (retrieval `turn1100view0`). The original printed pages203 and204 were also actually viewed from the cached source images listed in `notes/fgh_C8_Liu_source.json`. The definitions of the auxiliary invariants and every clause of Theorem1(V*) and(V) used here were checked directly.

**verified:** Dąbrowski–Sadek equation(3), printed pages2–3, was independently opened at <https://journals.sns.it/index.php/annaliscienze/article/download/6999/2547/4995> (`turn1101view0`, `turn1101view1`). This confirms the Igusa–Clebsch to Igusa conversions and the quintic discriminant normalization. The official Sage primary implementation was independently opened at <https://github.com/sagemath/sage/blob/develop/src/sage/schemes/hyperelliptic_curves/invariants.py> (`turn1102view0`, also `turn1101view2` and `turn1101view3`) to check the normalized transvectant and the three Clebsch conversion coefficients.

The resulting Igusa tuple is `(24,-24,1248,7344,-256)`. Liu's auxiliary valuations are7,14,4,8. The three(V*) quotients have valuations20,12,32; the two(V) quotients have valuations48,20. Thus the proper stable fibre consists of two smooth elliptic components meeting once. Both displayed reduced symmetric expressions in their j-invariants vanish in characteristic two, so both components have j=0. There is no missing weighted-scaling or residue-two normalization assumption.

## Specialization and fixed-group consequence

The canonical A37 proper-factor calculation and the exact application scopes of A41, A42, and A59 were reread. The Jacobian isogeny transfers potential good reduction and special two-rank zero. The four function identities give the stated cusp divisor relations with multiplicity eight; their connected incidence graph makes every cusp difference eight-torsion. Those classes specialize to zero on the good special Jacobian. A41 consequently makes every joining path rational, and each of the four punctures has another puncture as companion. A42 then gives the full fixed-subgroup conclusion at every coefficient prime. The actual dihedral closure is nilpotent, so the separate A59 normalizer implication is applicable.

## Independent execution and editorial correction

During capture the certificate was executed read-only with its final writer disabled; its entire computed JSON matched the retained owner JSON, not only a PASS flag. The normalized transvectants, maps, differential spans, invariant tuple, all five criterion valuations, and cusp divisors agreed.

Several missing display closers in the original notes draft were reported to the author and root. The author repaired them after capture; the reread current text has the intended displays. This was a presentation defect, not an altered mathematical premise. The original candidate and checkpoint preserve the audit trail.

## Additional proposed intermediate-cover scope

The author's proposed extension to every intermediate of this actual dihedral cover is mathematically sound, subject to being written explicitly. Norm makes the intermediate Jacobian an isogeny quotient, so potential good reduction and special two-rank zero persist. Over an algebraic closure, pushing the eight-torsion cusp divisors forward preserves their multiplicity, irrespective of ramification. The inertia group is the Frattini subgroup generated by the square of the order-eight rotation. For any proper subgroup H, the cusp number is the index of H times inertia, which is at least two by the Frattini property. Thus the same companion-path application is available. This last paragraph audits that proposed extension; it is not a claim that it was already in the candidate statement above.

### Written intermediate addendum: final independent PASS

The complete `notes/fgh_A68_intermediate_addendum.tex` was subsequently read end to end. Its actual inertia computation, elementary Frattini argument, norm of actual functions, inherited good two-rank-zero Jacobian, marked rational paths, and scoped A42/A59 applications all pass. The independent read-only execution of the additional nineteen-subgroup certificate matches its entire JSON. Exact hashes and execution confirmation are in `notes/de_A68_intermediate_audit.json`. No mathematical correction is needed.
