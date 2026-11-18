# R8: independent audit of the recovered original Fermat proofs

Date: 18 November 2026. Auditor: GPT-6 Astra Pro, `/root/literature`.
Current proof: `sections/part_E_fermat_audit.tex`, E.98–E.100.
Independent finite certificate: `code/check_fermat_audit.py` and its executed JSON.

## Scope and outcome

The recovered original LM6 contains substantive proofs of the positive
statements. They cannot be replaced by the unqualified sentence that every
Fermat curve, at every coefficient prime, has noncuspidal nilpotent and
metabelian sections. Its actual positive field is **Q**, its exponents are
**n=3^r or n=5^r**, and its pro-prime construction uses the corresponding
coefficient prime p. A noncuspidal full pronilpotent section is obtained by
using that one noncuspidal p-coordinate and the reference tangent at every
other coefficient prime. The other projections are therefore cuspidal.

The full metabelian claim is real: the construction lives in N/N'', not just
the product of maximal pro-prime metabelian quotients. The essential bridge
is a characteristic Haar idempotent in the full completed Alexander module.
It gives an actual arithmetic-equivariant injection
(N^(p))'/(N^(p))'' into N'/N''. This additional argument is independently
reconstructed in E.99.

Even plus Fermat curves have no geometrically pro-2 abelian section, already
over R. E.100 proves the real extension class directly from a Schreier basis.
Thus the unrestricted universal reading is false, while the exact recovered
positive range has been independently proved. The positive constructions
use no unpublished local section theorem.

The cuspidality convention is essential. At a nilpotent or abelian quotient,
the statement concerns images of actual cusp packets. In an abelian group
every geometric element centralizes a boundary line, so arbitrary sections
of its arithmetic normalizer are a much larger notion. E.99 separately
proves that the full metabelian quotient has exactly the expected cusp
normalizers and packets.

## Original source actually read

`recovered_sources/sq_background/LM6_return/LM6_POINTS_AS_SECTIONS_paper.tex`:

| Original location | Assertion actually audited | Current outcome |
|---|---|---|
| E.1, lines10980ff | Intrinsic N_n abelian rank n²+1 versus rank-two ambient toric quotient N_n/F' | Independently checked from the power cover and Schreier formula; retained throughout |
| E.5, lines11175ff | Every even plus n has nonzero real pro-2 abelian extension class | Reproved in E.100; no local conjecture |
| E.16, lines12184–12378 | Every S-unramified abelian class lifts fully pro-p over Q, p=3 or5,n=p^r; infinitely many noncuspidal classes | Reproved in E.98 with the actual arithmetic quotient and exact packet convention |
| E.31, lines14718–14964 | Full profinite metabelian zero-abelian cubic family; central modulo27 detector | Full family reproved by E.99; central detector reproved; a stronger wholly finite conjugacy reading is not certified |
| E.32, lines14966–15043 | One actual full pronilpotent noncuspidal section, all coefficient primes simultaneously | Reproved in E.98 by canonical Sylow product, with one noncuspidal factor and the reference tangent elsewhere |
| E.33, lines15045–15245 | Full metabelian Z_3^d_n family, zero abelian cocycle, all nonzero parameters noncuspidal | Reproved in E.99, including full metabelian cusp-normalizer calculation |
| E.34, lines15247–15401 | Corresponding Z_5^d_n family | Reproved in E.99 by free-source lifting and exact finite-complement averaging |
| E.38, lines16179–16435 | An actual cubic central class-two cocycle whose marked class-three obstruction vanishes at every finite coefficient but not continuously | Original proof read, but its extra E.19/E.37 action coordinates and missing 330-dimensional Smith certificate are not independently reconstructed; not used as authority |

The line locators refer to the recovered original, not to a results CSV.
The full original LM6 report and readings register were consulted only to
identify missing files and dependencies, not as proof.

## Arithmetic lifting: checks of the field and action

Let K=Q(mu_p), p=3 or5, and let Omega be the maximal **pro-p** extension of K
unramified away from p. It is Galois over Q. Gamma=Gal(Omega/Q) has a free
pro-p normal subgroup of index p−1, of rank (p+1)/2. It is not the unrestricted
maximal extension of Q unramified outside p, and Gamma is not asserted to
be pro-p.

The small-prime freeness is independently checked using the class-number-one
calculation, Kummer S-units, and the finite Euler formula. The graph of an
abelian cocycle factors through Gamma; the pro-p-kernel lifting problem is
solved over Gamma itself. There is no descent of an arbitrary K-section and
no equivariance assumption imposed after making an uncontrolled lift.

For the actual based action use s=−X/Z at O=[0:−1:1]. Then t=s^n and
−Y/Z=(1−s^n)^(1/n), with rational leading constants one. The tangential
cover comparison is therefore genuinely G_Q-equivariant. The standard unit
tripod tangent has actual action unramified away from p, as proved in
Wojtkowiak's primary paper. Its Frattini kernel is pro-p. This proves the
required action factorization on the whole geometric pro-p group, not only
on its outer action or abelianization.

For the proper Tate module, the fixed-S continuous H2 vanishes because
finite modules have a filtration by trivial F_p modules over K, and the
finite-complement average is exact. The finite H1 groups remove lim¹ at
this fixed ramification set. The Euler rank is the minus eigenspace dimension
of complex conjugation. It is g(X_n)>0 for the proper Tate module, so
infinite-order classes exist and lift to the affine abelian module and then
to the full pro-p group. The tangent-line divisor n(d−O) makes each cusp's
proper Kummer class n-torsion. This is the noncuspidality detector; no
classification of all sections is inferred.

## The full metabelian bridge

The completed Alexander sequence is reconstructed from finite abelian
covering graphs. To justify equality in the inverse limit, every finite
character on N' extends to N'V for some open normal V: choose V with
N'∩V in its kernel and set the extension to zero on V. Conversely,
compactness of N lifts any compatible system of finite abelianized covering
elements to N'. Thus the kernel of the completed edge boundary is exactly
N'/N'', with no replacement by a dense image.

In the coefficient-p part of Zhat[[N^ab]], normalized averaging over the
prime-to-p abelian factor gives a compatible idempotent. Its summand is
Z_p[[N^ab,(p)]]. Applying it to the Alexander sequence identifies the derived
module summand with (N^(p))'/(N^(p))''. Naturality and characteristicity make
the injection equivariant for the actual full arithmetic action.

To lift a B=exterior²V cocycle to this pro-p derived module, kill the finite
complement component by averaging, lift its values on free pro-p generators,
and then average the lifted cocycle under the complement. The resulting
cocycle is continuous and projects to the prescribed original cocycle
exactly. This proves surjectivity on H1 without an unjustified inverse limit
of unrelated solutions.

The rank calculation uses three real cusps, (3n−3)/2 conjugate cusp pairs,
and the anti-symplectic compact real action. Thus
dimV+=(n²−1)/2, dimV−=(n²+3)/2, and
d_n=dim(exterior²V)−=(n²−1)(n²+3)/4. A free cohomology submodule supplies
the Z_p^d_n parameter family.

Full conjugacy is checked: H0(G_Q,N^ab)=0 coefficient by coefficient by good
Frobenius weights, so a conjugator between two zero-abelian sections lies in
N'/N''. Projection to the chosen class-two cohomology submodule then proves
injectivity. For cusp normalizers, a primitive x has centralizer <x> in the
full metabelian group: class two forces the abelian coordinate to be a multiple
of x; the remaining derived component is killed by X−1; multiplication by
X−1 is injective on the completed full group ring. The latter assertion is
proved by refinement in the primitive q-adic direction at each coefficient
prime q. Arithmetic cusp packets therefore have the required usual form.

## Cubic modulo27: a sharper distinction and a simpler proof

The original E.31 finite calculation establishes a nonzero class in the
central H1 module modulo27. Its full-conjugacy argument uses integral
H0(G_Q,A)=0. The proof does not automatically establish the same absence of
conjugacy in a wholly finite quotient with A also reduced modulo27, because
H0(G_Q,A/27A) may be nonzero. E.99 retains exactly the proved central-module
claim and the independently proved full-metabelian injection. No specific
wholly finite conjugacy statement is imported.

There is a much shorter proof of the central detector. The generalized
Jacobian extension of the Fermat cubic by its boundary torus is killed by
three, since all nine cusp differences are three-torsion. Its pullback under
[3] splits uniquely, because Hom(E,T)=0. The resulting Q-map j0:E→J_D has
proper projection [3]. On exterior-square Tate modules the proper projection
of exterior²j0 is multiplication by9. Apply this to kappa_3(3), and lift the
class through the free-source/averaging argument. Its proper wedge coordinate
is9kappa_3(3), nonzero modulo27 since v_3(3^9)=9.

The independent script also reconstructs the old displayed degree-one
matrices and their45-dimensional exterior squares. The first proper-wedge
coordinate alone is a left kernel row of the normalized coboundary matrix
and has value9 on w. Multiplying that row by208 gives the original reported
scalar1872, with residue9 modulo27. This is a new checked row, not a claim
to have recovered the missing historical script or its literal row.

## Exact comparison with the ordinary tripod problem

The cover sends (u,v)=(−X/Z,−Y/Z) to (u^n,v^n)=(t,1−t); both leading
constants at the reference tangent are1. For the full pronilpotent section,
the p-coordinate unit classes are a kappa_p(p),b kappa_p(p), because the
cocycle is unramified outside p. Every other coefficient coordinate is zero.
Thus its completed pair is (p^(na epsilon_p),p^(nb epsilon_p)), where
epsilon_p is the p-supported idempotent of Zhat. In particular the
2-primary pair is (1,1). Since Q_2^× injects into its pro-2 completion, no
ordinary local t can have this pair. The full metabelian family has zero
intrinsic abelian cocycle, hence full tripod pair exactly(1,1).

This explicitly excludes every constructed family from the local-ordinary
hypothesis of the main questions. Noncuspidality in a quotient does not imply
ordinary local point matching. The construction does not supply even an
ordinary finite-support pair on the tripod, much less an infinite-support
counterexample.

## Missing original pieces

The recovered LM6 folder contains only the main TeX, report, bibliography,
readings and results registers. Its named `full_metabelian_family.py`,
`metabelian_family_rank.py` and E.38 Smith computation are absent.

The recovered review `earlier_returns/LM7_PUSH_ITEMS_E32_lim1.md` contains a
substantial proof of its LM7 E.32 cohomology comparison and a correction to
E.25: the quaternion(−1,−1) is nonzero at **both2 and infinity**, not only
infinity. Its cited original `E_completed_pairs.tex`, `E_cubic.tex`,
`E_cuspidally_central.tex`, `E_intrinsic_positive.tex`, `D.tex`,
`D_cm_shadow.tex`, and `D_cm_refine.tex` were not found in this recovered
archive. The restored `LM7_PUSH_checkpoint_09` is a different run and does
not provide those original proofs. The original LM8 F.21 proof was also not
found. The abstract derived-limit phenomenon has already been independently
proved in current A.24, so these missing sources are not needed for that
current theorem. They do not certify the exact geometric obstruction of
LM6 E.38: that proof additionally needs E.19, E.37 and the stated330-dimensional
Smith valuations. This audit does not silently mark that marked instance as
proved from the abstract cohomology theorem.

## Primary sources opened in this audit

| Source | Exact opened locator | URL and web references |
|---|---|---|
| Milne, Arithmetic Duality Theorems,2nd ed.(2006) | I.4.15 printedp62; I.5.1 setup printedp66 and formula p67 | https://www.jmilne.org/math/Books/ADTnot.pdf ; `turn287401600view0`, `turn969810928view1`, `turn928083084view2` |
| Hoshi(2010), nongeometric pro-p sections | Lemma3.2 authorp14; TheoremB authorp5; exact field hypotheses preserved | https://www.kurims.kyoto-u.ac.jp/~yuichiro/RIMS1689revised.pdf ; `turn287401600view1`, `turn937195460view2`, `turn620661213view2` |
| Wojtkowiak(2007), Galois actions on torsors of pathsI | Definition2.0pp198–199; Theorem2.1p199 and proofp200 | https://www.ms.u-tokyo.ac.jp/journal/pdf/jms140203.pdf ; `turn287401600view2`, `turn928083084view3` |
| Pacheco–Stevenson(2000) | Proposition4.3 printedp149, general pro-p-kernel projectivity criterion, not the geometric positive-characteristic theorem | https://msp.org/pjm/2000/192-1/pjm-v192-n1-p08-p.pdf ; `turn832508331view0` |
| Wickelgren(2014),2-nilpotent real section conjecture | Section1 equation(4), authorp3: completed equivariant topological extension equals the real arithmetic extension | https://services.math.duke.edu/~kgw/papers/delta2real.pdf ; `turn928083084view0`, `turn832508331view1` |

Existing verified bibliography keys are reused: CohMilneADT, LitHoshi2010,
AuditWojtkowiak2007, LitPachecoStevenson2000, LitWickelgrenReal2014. Segal's
2023 author paper on metabelian profinite groups was also opened during a
search for the Alexander comparison, but its pro-p scope is not used to
justify the full profinite sequence; that sequence is proved directly here.

Searches/checks included: `Wickelgren 2 nilpotent real section conjecture
abelian no real points PDF`; `profinite free metabelian group completed group
ring Alexander module exact sequence Magnus embedding`; exact filename and
content searches for LM7/LM8/F.21 and the two missing metabelian scripts in
both recovered source trees. Every source relied upon was opened, and the
source registers were not substituted for proofs.

## Executed verification

`python SECTION_GHOSTS/code/check_fermat_audit.py` exited0 with PASS.
It independently checked:

- cubic integral matrices, conjugation square, primitive w, T w=7w,
  J w=−w, normalized coboundary rank21 and free rank24;
- central detector9 modulo27 and an independent row with value1872;
- conjugate Frobenius7 Kummer vectors(2,0),(2,2), whose determinant is a3-adic unit;
- exact real/exterior rank formulas at n=3,5,9,25;
- normalized finite Haar idempotents at coefficient powers27 and125;
- nonzero odd real lift-square coordinates modulo2 through256, and no
  primitive dyadic conic solution modulo4.

These finite checks supplement the proofs. They do not turn the central H1
detector into an unchecked full finite conjugacy statement. The LaTeX
environment and math-delimiter check passed; the parent handles the full
document build.
