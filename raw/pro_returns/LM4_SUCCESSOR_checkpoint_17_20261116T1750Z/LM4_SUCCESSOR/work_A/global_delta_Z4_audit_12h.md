# The global invariant fourth-root character: exact remaining input

Research audit, 16 November 2026, 12:10 UTC. This is a bounded continuation
note, not a new numbered result or a solution of the main involution problem.

## Outcome

The recovered CM source gives no global abelianization theorem from which a
continuous, complex-conjugation-invariant lift of the parity character to
`Z/4` follows. Its Gaussian character has an actual fourth-root refinement,
but complex conjugation **inverts** that refinement. A.32 already proves
that no invariant fourth-root refinement of the total parity can factor
through the entire relative congruence image. Repeating a modulus-24 or
modulus-48 CM calculation cannot change this conclusion.

The remaining input is exactly a statement about the two-torsion in a
global coinvariant abelianization, or equivalently about a transgression
from the noncongruence automorphism kernel. Neither object is computed by
the supplied CM arguments or the primary literature checked below.

## 1. What E.65 actually provides

Write `H=ker(lambda: GT_0 -> Zhat^x)`. In the signed normalization of the
supplied LM7_PUSH E.65.1--E.65.4, there are continuous homomorphisms

\[
 T:H\longrightarrow C_6=\langle-I\rangle\times\langle R_0\rangle,
 \qquad W:H\longrightarrow C_4=\langle S\rangle,
 \qquad \delta=\epsilon_3(T)+\overline W.
\]

Here `W` is written additively when regarded as a character to `Z/4`.
E.65.12 proves the actual frame multiplication law; E.65.16 gives its
covariance under all multipliers. For the canonical complex conjugation,
the normalized data are

\[
 \beta_c=1,\qquad A_c=s,\qquad
 \mathcal V_c=\operatorname{diag}(-1,1).
\]

Thus `W(c h c)=-W(h)`. On `T`, conjugation fixes the sign factor and
inverts the order-three factor. In particular the two mod-two characters
are invariant, while the displayed `Z/4` refinement of the Gaussian
character is anti-invariant. This does not rule out an additional global
character, but it does not construct the requested invariant one.

The common-field formula E.65.13 proves equality of the two bits on the
multiplier-one Galois subgroup. It is not a computation of the
abelianization of `H`. The supplied referee's steps 6--10 separately check
the frame multiplication, covariance, sign normalization and Galois
vanishing. E.67 explicitly describes its further comparison as an
identity of characters and does not assign their total parity on full GT.

Sources read directly:

- `recovered_background/LM7_PUSH_checkpoint_09/sections/E_cm_character_agent.tex`,
  E.65.1--E.65.18, especially E.65.12, E.65.13 and E.65.16.
- `recovered_background/referee/REFEREE_B_E61_E65.md`, steps 6--10 and the
  opening scope verdicts.
- The statement and scope of
  `recovered_background/LM7_PUSH_checkpoint_09/sections/E_orbifold_CM_agent.tex`.
- Our A.19 and A.32, reread in the current active source.

## 2. Exact global abelianization criterion

Let

\[
 B=\left(H/\overline{[H,H]\langle c(h)h^{-1}:h\in H\rangle}\right)^{(2)}.
\]

This is the maximal pro-two quotient of the compact abelian coinvariants.
The character `delta` factors through `B`. There exists a continuous
`c`-invariant character `eta:H -> Z/4` reducing to `delta` if and only if

\[
                         \delta(B[2])=0.                 \tag{1}
\]

Here `B[2]` means the actual kernel of multiplication by two in the full
compact group, not the order-two subgroup of one chosen finite image.

Proof of the criterion. Necessity is immediate: an element of order at
most two maps into `{0,2}` in `Z/4`. For sufficiency, suppose (1). If for
every open subgroup `U` contained in `ker(delta)` the finite group `B/U`
had an order-two element with parity one, the compact sets

\[
       \{b\in B:\delta(b)=1,\ 2b\in U\}
\]

would have the finite intersection property. Their intersection would
give an element of `B[2]` of parity one, a contradiction. Hence some
finite quotient `B/U` has no such element. In the decomposition of that
finite abelian two-group into cyclic factors, its parity character is
zero on every factor of order two. On each remaining cyclic factor it
lifts to `Z/4`, by sending a generator to its prescribed parity. The sum
of those lifts, composed with the quotient map, proves sufficiency and
continuity.

The distinction from the main norm equation matters. A genuine
`h c(h)=1` with `delta(h)=1` gives a parity-one element of `B[2]`; the
converse does not reconstruct a nonabelian norm solution. Nor does
torsion-freeness of `H` determine `B[2]`.

## 3. The same input as a precise noncongruence transgression

Put `D=H semidirect <c>` and extend `delta` by `delta_D(c)=0`. With trivial
coefficients, the connecting map for

\[
       0\longrightarrow\mathbf F_2\longrightarrow\mathbf Z/4
         \longrightarrow\mathbf F_2\longrightarrow0
\]

sends `delta_D` to `delta_D cup delta_D`. This follows directly by lifting
the values 0 and 1: the integral carry on a product is the product of the
two mod-two values. Thus the invariant lift exists exactly when

\[
                  \delta_D\smile\delta_D=0\quad
                  \text{in }H^2_{\rm cont}(D,\mathbf F_2).       \tag{2}
\]

Any lift on `D` can be made zero on `c`: its value there is 0 or 2, and
one subtracts twice the character of the external `C2` factor.

Let `Dbar=H_cong semidirect <c>` and `K=ker(D -> Dbar)`. A.31 supplies an
actual involution in `Dbar` on which the descended parity is one.
Consequently

\[
       \overline\delta\smile\overline\delta\ne0
                  \quad\text{in }H^2_{\rm cont}(\overline D,\mathbf F_2):
\]

its restriction to that cyclic order-two subgroup is nonzero. The
continuous five-term sequence gives the exact remaining test

\[
 \delta_D\smile\delta_D=0
 \quad\Longleftrightarrow\quad
 \overline\delta\smile\overline\delta\in
 \operatorname{im}\left(
 H^1(K,\mathbf F_2)^{\overline D}\xrightarrow{\rm tr}
 H^2(\overline D,\mathbf F_2)\right).                       \tag{3}
\]

This is a statement about the **automorphism-group kernel** `K`. The
relative perfectness of a geometric source kernel in `Pi` does not imply
the vanishing of the group on the left of the transgression arrow.

More concretely, if `eta` exists then `eta(K)` is even, and
`chi(k)=eta(k)/2` is an invariant character `K -> F2`. For any full lift
`x=(h,c)` of the parity-one involution constructed on the congruence
image, one has `x^2 in K` and necessarily

\[
                            \chi(x^2)=1.                 \tag{4}
\]

Thus the proposed global character must detect a square that all the
retained congruence data miss. Equations (1)--(4) identify the missing
input; none of the retained calculations evaluates it.

## 4. Literature boundary

Lochak and Schneps (2006, Question 1.2) explicitly pose the abelianization
question for the full profinite **GT**, and Question 1.3 poses the
freeness question for its multiplier-one kernel. These are statements
about a different, pentagon-constrained group; they cannot be used as
theorems about the larger gentle group `GT_0`, or as computations of its
`c`-coinvariant abelianization. The primary author manuscript was opened
again, rather than relying on the search extract.

Marin (2008, Section 4) constructs the modular Kummer cocycle with the
cyclotomic coefficient action. Sections 5--6 construct further
characters through prounipotent rigidity. They do not assert that all
continuous abelian quotients of the full profinite gentle kernel are
accounted for. In particular no global generation or exhaustion of the
character group is inferred from those examples.

References already present in the project bibliography:

- Lochak, P., & Schneps, L. (2006). Open problems in
  Grothendieck--Teichmuller theory. In B. Farb (Ed.), *Problems on Mapping
  Class Groups and Related Topics* (pp. 165--186). American Mathematical
  Society. Primary manuscript:
  https://webusers.imj-prg.fr/~leila.schneps/farb.pdf
  (`A_LS2006`; the author manuscript's Question 1.2 was checked directly).
- Marin, I. (2008). Characters of the Grothendieck--Teichmuller group
  through rigidity of the Burau representation. *Annales de la Faculte
  des Sciences de Toulouse. Mathematiques, 17*(4), 765--780.
  https://doi.org/10.5802/afst.1202 (`AMarin2008`). Primary author version:
  https://www.lamfa.u-picardie.fr/marin/arts/gtrig.pdf
- Poonen, B. (2017). *Rational Points on Varieties*. American Mathematical
  Society. Theorem 6.7.3 and Corollary 6.7.4 supply the continuous
  five-term sequence (`APoonen2017`, already audited for A.54).

Web retrieval record for this bounded audit: primary author PDFs
`turn700view1` (Lochak--Schneps) and `turn699view0` / `turn700view2`
(Marin). No assertion that a current open problem has been settled is
made from this search.

## Continuation decision

The CM-refinement route is exhausted at the stated level of information.
A new attempt would need either an actual invariant character of `K`
with the transgression in (3), or a computation of the full `B[2]` in
(1). No such input has been obtained. The main parity-one involution and
conjugacy questions remain Open.
