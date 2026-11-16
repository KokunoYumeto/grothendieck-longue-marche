# Focused mixed-component continuation

Checked 16 November 2026. The complete numbered arguments are in
`Mixed_duplication_reduction.tex` (MD.1–MD.8). This is a continuation of,
not a replacement for, `final_character_search_audit.md`.

## Concrete mathematical progress

All the following use the intrinsic normalized pair
`x -> x, y -> f^-1 y f`, left conjugation on the Alexander module,
and `[x,y]=xyx^-1y^-1`. Write `Psi_n=m_0` for the index-n Schreier
coefficient. No source's arithmetic sign is silently imported.

1. **MD.2:** In `(Z/4)[omega]`,
   `B_f(-1,omega)=(-1)^(Psi_3/2)` on all actual multiplier-one gentle GT.
   The proof is direct: symmetry of `A_f`, reduction `-1=1 mod2`, and
   KM.3's integral half-character. No gamma factorization is needed.
2. **MD.3:** The five-point affine pentagon character `a_f` in FP.33
   equals `Psi_2 mod3`. Therefore the pentagon supplies `rho=Psi_2 mod3`.
3. **MD.4:** The unit
   `D_2=omega^(2Psi_2) B_f(omega,omega)/B_f(-1,omega)` is exactly the
   sign of the continuous quadratic character
   `d_2=epsilon_2(W)+Psi_3/2` on genuine multiplier-one GT.
   With `e_3=kappa_d+Psi_3/2`, the precise decomposition is
   `Delta=d_2+e_3`. Proving `d_2=e_3` is equivalent to the main equality
   there. Proving both zero is stronger and sufficient.
4. **MD.7–MD.8:** The fixed-original-descent locus and the literal
   harmonic primitive equation each kill `d_2`. More generally,
   `Psi_3/2 mod2=epsilon_2(W_(D_L Phi))=epsilon_2(W_(D_P Phi))` on all
   gentle multiplier-one elements. Hence both fixed loci lie in
   `ker d_2`, although the fixed loci themselves remain distinct.
   The original fixed locus's cubic comparison remains unproved.
5. **MD.5:** The KM.5 coefficient example survives the completed-ring
   integrality and cyclotomic checks. It satisfies reflection, all unit
   substitutions, symmetry and both metabelian three-cycle identities.
   It has zero off-diagonal Kummer data but nontrivial `D_2`.
   It is **not a full profinite GT element or a claimed lift**.
   The audit also checks `Gamma(U^2)=Gamma(U)` and
   `B(U^2,V^2)=B(U,V)`: coefficient-two Frobenius substitution
   does not remove it. Witt Frobenius fixes its values `+1,-1`.
   This substitution identity is distinct from duplication, which
   relates shifted arguments.

The independent executable check retains the order-four exponent
factor and verifies exact identities in `(Z/4)[C_12]`, `(Z/4)[C_36]`,
and `(Z/4)[C_108]` and their two-variable group rings:

- `code/check_mixed_idempotent.py`
- `code/check_mixed_idempotent.out` — all PASS

These finite checks supplement the inverse-limit proof; they do not
prove a global lifting claim.

## Newly opened primary source directly bearing on the bridge

**Furusho, H. (2003).** Geometric and arithmetic subgroups of the
Grothendieck–Teichmüller group. *Mathematical Research Letters, 10*(1),
97–108. Author-hosted complete published PDF:
<https://www.math.nagoya-u.ac.jp/~furusho/paper/GTA-mrl.pdf>.

Theorem 3.1 proves duplication from `(I),(II),(IV),(K_2)`.
Theorem 3.4 gives `GT_K intersect IΓ subset GT_A,2∞`. These are extra
hypotheses. Definition 2.2 supplies the exact Schreier normalization;
p.102 prints the group-ring form
`B{X,X}=X^(-2Psi_2)B{-1,X}`, which is exactly the finite condition
in MD.4 after specialization. It does not identify the cubic frame
character with `Psi_3/2`.

Retrieval references: `turn170view0`, `turn171view0`–`turn171view2`.
Local full source: `furusho_GTA_2003.pdf`, text extraction and
`furusho_p102.png`; the displayed group-ring exponent was visually
checked. The function-value line immediately above it omits a factor
2 relative to the general `(A_n)` on p.101 specialized at `n=2`.
The group-ring statement agrees with that general formula and is the
one used here.

A separate *Detailed and corrected version* dated 3 January 2008
was indexed, retaining the same Theorem 3.1 statement. Its full text
was not retrieved; no claim from its detailed proof is used.
Indexed URL:
<https://citeseerx.ist.psu.edu/document?doi=cc776b8da5855487293757523fd77dc40e761ed5&repid=rep1&type=pdf>
(`turn175search37`, `turn177search4`, `turn180search29`; direct open
returned 403).

## Convention control and special-locus domain

**Lochak, P., Nakamura, H., & Schneps, L. (2004).** Eigenloci of
5 point configurations on the Riemann sphere and the
Grothendieck–Teichmüller group. *Mathematical Journal of Okayama
University, 46*(1), 39–76. <https://doi.org/10.18926/mjou/33919>.

The primary author manuscript was opened at
<https://webusers.imj-prg.fr/~pierre.lochak/textes/eigenloci.pdf>.
Theorems 2–3 retain the Galois domain for the NT primitive equations.
Its Appendix gives the exact sigma/tau path and proword dictionary;
simultaneous free-generator inversion changes the integral Schreier
sign but leaves the half modulo two unchanged. Section 6 explicitly
distinguishes torsion-conjugacy results for full GT from the more
specific primitive formulas for Galois. No all-GT cubic-frame/Kummer
comparison was extracted from it.

Retrieval references: `turn182view0`–`turn182view3`,
`turn183view0`–`turn183view1`. Publisher metadata and page range were
independently checked through the Okayama repository (`turn181search0`,
`turn181search6`).

Ihara II's Theorem 1 writes `(n^(-r))^(sigma-1)=exp(2pi i r Psi_n)`.
Thus it is the negative of the conventional positive-root exponent
in that monodromy convention. This has now been made explicit in
`Kummer_mixed_component.tex`, where the elementary peripheral identity
used in KM.3 was also supplied with a direct proof using the two
three-cycle equations for `(1,f)` and `(-1,f)`.

## Exact boundary of this continuation

The queries were restricted to Ihara beta/gamma multiplication,
Furusho's geometric/arithmetic subgroup comparison, the corresponding
correction, and special-locus primitive formulas. They did not replace
the full profinite group by a pro-unipotent or pro-prime analogue.
The original Ihara beta/gamma I full text remains unobtained. Its
factorization theorem is still cited through its author's explicit
account in II and Furusho's primary discussion.

No opened theorem in this focused continuation proves `d_2=0` or
`e_3=0` on all genuine multiplier-one profinite GT. The countermodel
shows that the specified coefficient identities alone do not imply
`d_2=0`; it does not show independence from the full pentagon.
The new descent factorization and the exact two-character decomposition
are proved reductions, not a resolution of the main question.

## Final finite square-pair clarification

MD.4 now explicitly identifies the known affine pentagon obstruction:
on all gentle multiplier-one elements,
`D_2=omega^(-eta_aff)(-1)^(d_2)`, where
`eta_aff=a_f-rho=Psi_2-rho mod3`. Thus the proved affine pentagon
calculation kills exactly the order-three factor of this duplication
unit. Its sign is the remaining character `d_2`.

The five-point agent identified the new Burau comparison's square pair:
after stripping the central C3, the pair `(p,t)` has orders `(3,4,4)`;
`<p,t^2>` is `A4 x C2`. Multiplication of `t^2` by its central
involution gives an A4 complement with orders `(3,2,3)`, and that
central change does not affect a commutator-word evaluation. Hence
the half-Kummer value is exactly a square-pair evaluation in this
finite comparison. The matrix certificate is in the five-point
agent's `check_burau_square_pair.out`.

MD.9 independently proves the relevant abstract same-word limitation.
For `p=(123), t=(1234)`, the joint map to `S4 x A4` using the pairs
`(p,t)` and `(p,t^2)` is onto, since S4 and A4 have no nontrivial
common quotient. Its derived image is `A4 x V4`, and its second
derived image is `V4 x 1`. The explicit word
`[[x,y],x[x,y]x^-1]` has values `(14)(23)` and the identity.
`code/check_square_pair_goursat.py/.out` independently checks these
facts, with joint derived-series orders 288, 48, 4, 1. This is only
a word-evaluation result; neither a gentle element nor a full GT
element is constructed.

The last focused source queries reproduced Furusho's exact extra
hypotheses and the indexed 2008 correction, without a theorem
removing `(IV)` or `(K2)` on full profinite GT. Retrieval references:
`turn185search5`, `turn185search6`, `turn185search8`. No secondary
survey or pro-unipotent result was substituted for that missing step.

MD.10 records a stronger actual-gentle limitation using LI.8's
already lifted element `k`: all `Psi_n(k)` vanish, `A_f=0`, `B=1`,
one may take `Gamma=1` satisfying every Anderson coefficient
identity, and `rho=epsilon_2(W)=d_2=0`. Nevertheless the gentle
extension `e_tilde_3=epsilon_3(T)+Psi_3/2` equals `Delta(k)=1`.
This proves that the beta/Kummer/Anderson coefficient package
does not suffice for the desired parity on the gentle group.
Membership of this `k` in full profinite GT remains unproved;
no statement about a counterexample inside full GT is made.
