# Candidate F.46: proper pro-formation closures over algebraic constants

Status: independently reviewed by root and degeneration; integrated as F.46 in
`sections/F_geometric_proformation_extension.tex`. This complete candidate is
retained as the review history. This
combines the two different sufficient mechanisms in F.44 and F.45, with
a necessary change of Hilbertian base field. It is not a converse
classification for F.9.

## 1. Statement

Let \(\mathcal C\) be a proper isomorphism-invariant subclass of finite
groups containing all cyclic groups and closed under subgroups, quotients
and extensions. Let \(K_0/\overline{\mathbf Q}\) be finitely generated
of positive transcendence degree, and let
\(k=K_0^{\mathcal C}\) be its maximal Galois pro-\(\mathcal C\)
extension in a fixed separable closure. Then:

1. every finitely generated extension \(L/k\) has the actual
   closed-point-preserving all-scheme étale-topos reconstruction property;
2. every subfield \(k_0\subset L\) with
   \(\operatorname{trdeg}_{\mathbf Q}k_0>0\) has that property.

The example \(\overline{\mathbf Q}(t)^{\mathrm{solv}}\) is outside
both F.44's sufficient class and F.45's sufficient class. The arbitrary
algebraic-constant subfield cannot be included: every such \(k\)
contains the negative field \(\overline{\mathbf Q}\).

All comparisons use the corrected CHW convention, not the relative-only
definition refuted in F.1/F.17.

## 2. Two distinct descent fields

Choose a finitely generated field \(D/\mathbf Q\) inside \(K_0\) with
\[
                      K_0=D\overline{\mathbf Q}.           \tag{G1}
\]
The extension \(K_0/D\) is algebraic Galois. Every automorphism over
\(D\) preserves \(K_0\) and its maximal pro-\(\mathcal C\)
extension, because it permutes finite Galois extensions with groups in
\(\mathcal C\). Consequently \(k/D\) is algebraic Galois.

For any finitely generated \(L/k\) and any finite set of data over
\(L\), choose a finitely generated \(F/\mathbf Q\) containing \(D\)
and those data, with
\[
  L=Fk,
  \qquad B:=F\overline{\mathbf Q},
  \qquad L/F\text{ Galois},
  \qquad L/B\text{ Galois pro-}\mathcal C.                  \tag{G2}
\]
The last assertion follows by base change from \(k/K_0\), since
\(K_0\subset B\). The field \(B/\overline{\mathbf Q}\) is finitely
generated and has positive transcendence degree, so it is Hilbertian by
the opened Bary-Soroker–Paran Theorem1.2/Corollary3.2 used in F.45.

The two bases have different roles. Hilbert specialization is carried out
over \(B\), where the remaining algebraic extension is pro-\(\mathcal C\).
The arithmetic equivariance and Tate-Hom arguments use \(F\), which is
finitely generated over \(\mathbf Q\) and satisfies
\(G_L\triangleleft G_F\). There is no assertion that
\(\operatorname{Gal}(L/F)\) is pro-\(\mathcal C\).

Finite-extension stability is immediate: every finite extension of
\(L\) is still finitely generated over the fixed \(k\), and admits
such a descent field \(F\). A finite collection of point coordinates
and actual values can be placed in one finite extension of a sufficiently
large \(F\): all elements of \(k\) are algebraic over \(D\), so only
finitely many algebraic coefficients are needed. Thus passing back to a
finitely generated \(\mathbf Q\)-field loses no finite data.

## 3. Divisible elements and missing geometric extensions

The group \(k^\times\) is divisible. Indeed \(\mu_\infty\subset K_0\).
For \(a\in k^\times\), choose a finite Galois \(E/K_0\) with group in
\(\mathcal C\) containing \(a\). Adjoin \(n\)-th roots of all its
conjugates. The resulting normal extension has an abelian kernel over
\(E\), and hence has group in \(\mathcal C\) by the closure hypotheses.
It lies in \(k\) and contains an \(n\)-th root of \(a\).

For every finite \(E/k\),
\[
                  D(E^\times)=k^\times.                   \tag{G3}
\]
Here is the fixed-field argument, including its arithmetic descent.
Choose a finite Galois \(M/D\) with \(E\subset Mk\). This is possible
because \(E/k\) is finite and \(k/D\) is algebraic: descend its finitely
many equations and roots and take a finite normal closure over \(D\).
The field \(M\) is finitely generated over \(\mathbf Q\).
For \(a\in D(E^\times)\), enlarge \(M\) once to contain \(a\), still
with \(E\subset Mk\). Fix
\(\sigma\in\operatorname{Gal}(Mk/k)\). For each \(n\), choose
\(z_n\in E\) with \(z_n^n=a\). If
\(\tau\in\operatorname{Gal}(Mk/M)\), then \(\sigma\) and \(\tau\)
commute: on \(M\), \(\tau\) is the identity and \(\sigma\) preserves
\(M\); on \(k\), \(\sigma\) is the identity and \(\tau\) preserves
\(k\), because it fixes \(D\) and \(k/D\) is Galois. Since
\(\tau z_n/z_n\in\mu_n\subset k\), it follows that
\(\sigma z_n/z_n\in M\). Thus
\(\sigma a/a\in(M^\times)^n\) for every \(n\).

The divisor and number-field-unit argument from F.33 gives
\(D(M^\times)=1\) for finitely generated \(M/\mathbf Q\). Hence
\(\sigma a=a\), for all such \(\sigma\), and \(a\in k\). The
reverse inclusion follows from radical closedness. On a normal proper
model of any finitely generated \(L/k\), an infinitely divisible element
and all its roots have zero divisor, so lie in the finite relative
algebraic closure of \(k\). Applying(G3) gives
\[
                         D(L^\times)=k^\times.             \tag{G4}
\]

There are finite extensions of \(K_0\) not contained in \(L\). To see
this with unbounded residual degrees, use F.44's elementary group fact:
a proper hereditary \(\mathcal C\) excludes \(A_n\) for all sufficiently
large \(n\). The Hilbertian field \(K_0\) has \(S_n\)-extensions
\(\Omega_n/K_0\) for arbitrarily large such \(n\), by the regular Morse
polynomials and Hilbert specialization. For \(n\ge5\), normality of
\(k/K_0\) and the normal subgroups of \(S_n\) show
\[
 \operatorname{Gal}(\Omega_nk/k)=A_n.                       \tag{G5}
\]
The quadratic subextension belongs to \(k\), while the entire
\(S_n\)-extension cannot, since \(A_n\notin\mathcal C\).
The relative algebraic closure of \(k\) in \(L\) is finite, whereas
\(|A_n|\) is unbounded. Therefore some \(\Omega_n\) is not contained
in \(L\). This is a missing **geometric** extension: all algebraic
number-field constants already lie in \(K_0\). It replaces the missing
number field in F.35, and will be used with F.45's moved geometric
divisors.

## 4. Arithmetic finite-quotient detection: specialize over B

Let \(Y\to U\) be a connected finite \(G\)-Galois cover of a smooth
geometrically connected curve over \(L\). Descend it, including its
\(G\)-action, to \(F\) as in(G2), and then view that descent over
\(B=F\overline{\mathbf Q}\). The cover over \(B\) is connected,
because its base change to \(L\) is connected. Let \(M/B\) be the
finite Galois constant field of this cover, and put
\(N=\operatorname{Gal}(Y/ U_M)\), \(P=G/N\). Connectedness over
\(L\) implies
\[
                             M\cap L=B.                   \tag{G6}
\]

Run the complete-linear-system pencil construction of F.24 over \(B\).
Choose its degree \(n\) sufficiently large for the jet and connectedness
arguments there and for \(A_n\notin\mathcal C\). The resulting finite
monodromy group has the reviewed embedding
\[
 H\subset (G\times_P\cdots\times_PG)\rtimes S_n.           \tag{G7}
\]
It contains the literal \(S_n\), and its base subgroup contains the
support-at-most-two elements whose coordinate labels, after permutation
conjugation, generate \(N\). These are precisely the geometric
conclusions of F.24's ordered lift and common-constant construction. Its
proof applies over any characteristic-zero field; no number-field
hypothesis is used in the jet, monodromy, or spanning-tree arguments.
The Galois closure can have additional constants, as already allowed in
F.24.

Now use Hilbert irreducibility over the **Hilbertian field \(B\)** to
obtain \(\Omega/B\) with full group \(H\), and set
\[
                    J=\operatorname{Gal}(\Omega L/L).
\]
Since \(L/B\) is Galois pro-\(\mathcal C\),
\[
        J\triangleleft H,\qquad H/J\in\mathcal C,
                         \qquad J\twoheadrightarrow P.    \tag{G8}
\]
The last assertion uses(G6), which is preserved by the full-degree
specialization and its specified constant-field embedding.

Simplicity gives \(A_n\subset J\): otherwise
\(A_n\cap J=1\) and \(A_n\) would embed in \(H/J\in\mathcal C\).
For an element \(u\) of the base subgroup supported on at most two
coordinates, choose an even permutation \(\tau\) with
\(\tau^{-1}(i)\) outside that support. Then
\[
        [u,\tau]\in J\cap N^n,
                     \qquad [u,\tau]_i=u_i.               \tag{G9}
\]
Normality transports all such labels to every coordinate. The
intersection \(J_i\) of \(J\) with a selected coordinate stabilizer
therefore projects onto \(N\). Since \(J\to P\) is onto, multiplication
by a literal even permutation returns the selected coordinate to itself
without changing its constant image. Hence \(J_i\to G\) is onto.
The corresponding closed point of \(U\) detects the full arithmetic
quotient. As \(n\) is arbitrarily large, its degrees are unbounded;
\(A_n\subset J\) makes the block action transitive of degree \(n\).
Avoiding a prescribed finite closed set is achieved in the same linear
system as in F.24. The cover-preserving curve reduction of F.29 extends
detection to every smooth geometrically connected source.

**Necessary distinction.** If one instead specialized over the
finitely generated \(\mathbf Q\)-field \(F\), then the total quotient
\(H_F/J_F\) need not lie in \(\mathcal C\), because it can contain
arbitrary number-field constant quotients. Nor does a literal
\(A_n\) being geometric before specialization, on its own, prove that
it fixes all constants newly acquired after that specialization. The
proof does not make either inference. It changes the Hilbertian base to
\(B\) first, and only then uses(G8). The normality over \(F\) required
later is a different assertion already established in(G2).

## 5. Moved divisors and the fixed finite norm field

Take the punctured-line class with actual point values in the form used
in F.43/F.45,
\[
 \kappa(b_0)+\sum_j\lambda_j
     \bigl([P_j(T)]-[P_j(x_0)]\bigr),
                     \quad\lambda_j\in\widehat{\mathbf Z}. \tag{G10}
\]
Descend its data to \(F/\mathbf Q\) as in(G2). Choose a finite Galois
\(M/\mathbf Q(t_1,\ldots,t_d)\), where the \(t_i\) form a
transcendence basis of \(F\), containing \(F\), the puncture roots, and
a finite descent of a missing geometric extension from(G5). Then
\(Mk/L\) is finite Galois and nontrivial. Choose
\(\sigma\in\operatorname{Gal}(Mk/L)\) whose restriction to \(M\) is
nontrivial. It fixes \(\overline{\mathbf Q}\subset k\) and acts as a
finite-order nonidentity automorphism over
\(C_M=M\cap\overline{\mathbf Q}\).

Apply F.45's moved-divisor lemma, allowing one finite normal enlargement
of the number-field constants in \(M\). This enlargement lies in
\(k\), so changes neither \(Mk\) nor the prescribed fixed action of
\(\sigma\) on \(k\). The resulting geometric DVRs
\(v_i,\sigma^{-1}v_i\) are pairwise distinct and good for all roots,
derivatives and resultants. The same semilocal CRT construction gives
\(\alpha\in U(M)\) with
\[
 R_j=\frac{P_j(\sigma\alpha)}{P_j(\alpha)}\in M^\times,
                        \qquad v_i(R_j)=-\delta_{ij}.      \tag{G11}
\]
Again \(\sigma\) fixes coefficients but need not fix individual roots.

Let \(b_\alpha\in Mk\) be the actual value. Choose **once** a finite
extension \(S_0/D\) inside \(k\) such that
\[
                         F'=MS_0
\]
contains \(b_\alpha\). This is possible because \(k/D\) is algebraic
and only finitely many elements of \(k\) occur in one expression for
\(b_\alpha\). The field \(F'\) is finite over \(M\), finitely
generated over \(\mathbf Q\), and \(\sigma\)-stable. It is fixed
before any radical level is chosen.

If \(a\in(F')^\times\) has an \(n\)-th root \(z\in Mk\), then for
\(\tau\in\operatorname{Gal}(Mk/F')\) the automorphisms
\(\sigma,\tau\) commute. On \(M\), \(\tau\) is the identity and
\(\sigma\) preserves \(M\); on \(k\), \(\sigma\) is the identity
and \(\tau\) preserves \(k\), because \(D\subset M\) and \(k/D\)
is Galois. The element \(\tau z/z\) lies in \(\mu_n\subset k\), so
\(\sigma z/z\) is fixed by every \(\tau\) and belongs to \(F'\).
Consequently
\[
                 \sigma a/a\in((F')^\times)^n.             \tag{G12}
\]

For representatives \(a_{j,n}\) of \(\lambda_j\bmod n\), the actual
evaluation of(G10) gives an \(n\)-th power in \(Mk\) of an element
of \(F'\). Applying(G12) gives
\[
 \frac{\sigma b_\alpha}{b_\alpha}
                 \prod_jR_j^{-a_{j,n}}
                          \in((F')^\times)^n.              \tag{G13}
\]
The integer character \(v_i\circ N_{F'/M}\) now yields
\[
 [F':M]\lambda_i
   =-(v_i\circ N_{F'/M})(\sigma b_\alpha/b_\alpha)
                         \in\mathbf Z.                    \tag{G14}
\]
Since \(\lambda_i\in\widehat{\mathbf Z}\), it is an ordinary integer.
This gives the actual regular unit on the punctured line.

It would be incorrect to apply F.45's direct integer-valued prolongation
argument through \(Mk/M\): the pro-\(\mathcal C\) geometric extension
can ramify these divisors. The fixed finite field \(F'\) and its norm
are the replacement. Every radical level uses the same finite
degree \([F':M]\), which is exactly what makes(G14) effective.

## 6. Generalized Albanese and actual point functions

All arithmetic inputs for the F.43 proof are now verified, but it is
useful to state the descent match explicitly. For a pointed smooth
geometrically connected affine \(X/L\), descend the geometry and
generalized Albanese to \(F\) in(G2), after a finite extension splitting
the boundary. The integral Spiess–Szamuely comparison identifies
\(H^1(X_{\bar L},\mathbf Z_\ell(1))\) with the dual of the Albanese
Tate module. Set \(H=G_L\triangleleft G_F\) and
\(W=(V_\ell A)_H\). All roots of unity lie in \(L\). The finite
arithmetic quotient detection from Section4 makes the projected
point-Kummer homomorphisms span \(W\), by the annihilating-functional
argument of F.43/F.45.

Choose finitely many spanning point images. Their coordinates and actual
values descend to one finitely generated \(M/\mathbf Q\), finite over
a sufficiently enlarged \(F\). The normality of \(G_L\) in \(G_F\)
keeps \(W\) stable. Conjugation of each point cocycle has a coboundary
term killed in the \(H\)-coinvariants, while the actual multiplicative
value transforms by the cyclotomic character. Their equality therefore
makes the functional \(G_M\)-equivariant on the spanning images, hence
everywhere. Jannsen's **original Theorem4.3(ii), p.676** is applied over
this finitely generated \(M\). It puts the functional in the integral
unit lattice; splitting the boundary and normalizing at the basepoint
makes that one lattice independent of the coefficient prime. No Tate
theorem over \(K_0\), \(k\) or \(L\) is assumed.

Norms to punctured rational lines use Section5 to make every curve
residue integral, with residue degree rather than ramification index as
the norm coefficient. Smooth transverse curves give the same assertion
for each divisor of a compactification in higher dimension. The
injective integral divisor matrix then gives an actual regular unit
\(h\), normalized by the actual basepoint value. Galois descent of the
unit and finite-level Hochschild–Serre remove any remaining constant
class exactly as in F.43, because the ratio has zero divisor and value1
at the basepoint. Thus the given compatible point-theoretic Kummer class
is \(\kappa(h)\).

Equation(G4) leaves actual point values in the form
\(\phi(x)=c_xh(x)\) with \(c_x\in k^\times\). Closed points of
unbounded degrees and the fixed pole-degree comparisons of F.28/F.43
apply to every nonempty inverse-image open. They force a nonconstant
point function to equal one normalized regular unit: pull back \(T-1\)
and then \(T-b\) for all \(b\in k^\times\), obtaining respectively
the affine relation \(h_1=Ah+B\) and
\(h_b=e_b(ch-b)\). High-degree points have \(h(x)\notin L\), hence
\(h(x)\notin k\). Their degree exceeds the combined pole bound, so the
corresponding rational-function identity is exact. The zeros of the
translated unit then handle points where \(h(x)\in k\).

If \(h\) is constant, choose after a finite extension an element
\(\beta\) with \(\beta/h\notin k\), using the missing geometric
extension established in Section3. All earlier assertions are stable
under that finite extension. No closed point maps to \(\beta\); the
closed-subtopos argument therefore makes \(T-\beta\) available on the
whole source. Its recovered unit is constant by the high-degree argument,
and comparison of its value ratio with \(\phi(x)/h\in k\) forces
\(\phi(x)=h\). Smooth curves through any two prescribed points give
the higher-dimensional point function.

This is exactly CHW Theorem4.18(5), so the full all-scheme reconstruction
property holds over \(L\). The full topos comparison comes from that
theorem, not merely from equality of point functions or generic groups.

## 7. Positive-transcendence subfields

Let \(k_0\subset L\) have positive transcendence degree over
\(\mathbf Q\). Choose a finite transcendence basis \(T\) of
\(k_0/\mathbf Q\), and put \(A=\mathbf Q(T)\subset k_0\). Enlarge
the descent field \(F\) in(G2) to contain \(T\). Let \(R\) be the
relative algebraic closure of \(A\) in \(F\). Then \(R/A\) is finite,
\(R/\mathbf Q\) is finitely generated, and \(F/R\) is regular.

For \(a\in k_0\), let \(N/R\) be the finite normal closure of
\(R(a)/R\). Regularity gives \(N\cap F=R\) and identifies the
\(R\)-conjugates with the \(F\)-conjugates. Normality of \(L/F\)
therefore puts \(N\) inside \(L\). Base change preserves regularity:
\[
    F\overline{\mathbf Q}/R\overline{\mathbf Q}
                       \text{ is regular}.
\]
Thus \(N\overline{\mathbf Q}\cap F\overline{\mathbf Q}
=R\overline{\mathbf Q}\). Its finite Galois group over
\(R\overline{\mathbf Q}\) is identified with that of its compositum
over \(F\overline{\mathbf Q}\), a finite quotient of the
pro-\(\mathcal C\) group in(G2). Hence
\[
        a\in (R\overline{\mathbf Q})^{\mathcal C},
          \qquad k_0\subset (R\overline{\mathbf Q})^{\mathcal C}.
                                                               \tag{G15}
\]
The base \(R\overline{\mathbf Q}/\overline{\mathbf Q}\) is finitely
generated and has positive transcendence degree, because \(T\ne\varnothing\).
The core theorem just proved applies to its maximal
pro-\(\mathcal C\) closure. That closure is algebraic over \(k_0\):
\(R/A\) is finite, \(\overline{\mathbf Q}/\mathbf Q\) is algebraic,
and \(A\subset k_0\). Now apply F.32.

This argument does not use the possibly transcendental compositum
\(k_0k/k_0\). It does not include algebraic subfields, where the
intermediate base in(G15) could be \(\overline{\mathbf Q}\) and the
positive-transcendence core theorem would not apply.

## 8. Strict example and comparison with the earlier classes

Let \(k=\overline{\mathbf Q}(t)^{\mathrm{solv}}\). It reconstructs by
the candidate. Its multiplicative group is divisible and contains the
transcendental element \(t\). If it embedded in a finitely generated
extension \(E/\overline{\mathbf Q}\), the divisor argument(Q1) of
F.45 would send every element of \(k^\times\) into
\(D(E^\times)=\overline{\mathbf Q}^\times\), contradicting the
transcendence of the image of \(t\). Thus this field is outside F.45's
sufficient embedding class.

It is also outside the union of F.44's sufficient classes. Any
finitely generated algebraic model \(F_0\) for it has number-field
constants \(C=F_0\cap\overline{\mathbf Q}\), and its normal closure
contains \(\overline{\mathbf Q}\). Restriction gives a quotient onto
\(G_C\). A virtually pro-\(\mathcal C'\) normal-closure group for a
proper hereditary \(\mathcal C'\) would yield an open pro-\(\mathcal C'\)
subgroup of \(G_C\), impossible by the arbitrarily large symmetric
quotients of every number-field absolute Galois group. This is the
same verified strictness argument as F.45, and it applies to every
proper \(\mathcal C'\), not only the solvable class.

Conversely the new theorem includes F.45's positive class: a finitely
generated \(K_0/\overline{\mathbf Q}\) is an algebraic subfield of
\(K_0^{\mathcal C}\), so F.32 descends the core theorem to \(K_0\),
and the proved subfield step applies. It also includes the
positive-transcendence fields from F.44. Its equivalent algebraic-model
description puts each such field inside \(K^{\mathcal C}\) for a
finitely generated \(K/\mathbf Q\) of positive transcendence degree:
take the finite fixed field of an open pro-\(\mathcal C\) subgroup of
the normal closure. Now
\(K^{\mathcal C}\overline{\mathbf Q}/K\overline{\mathbf Q}\) is
pro-\(\mathcal C\), so it embeds in
\((K\overline{\mathbf Q})^{\mathcal C}\); algebraic composita and
the same positive-subfield descent apply. This does not replace F.44's
positive results for algebraic extensions of number fields.

## 9. Exact source and proof audit

The only Hilbertian theorem needed beyond F.44 is the already opened
Bary-Soroker–Paran Theorem1.2/Corollary3.2, used over
\(B=F\overline{\mathbf Q}\). All geometry of the balanced pencil
is the fully proved F.24 construction; all group closure and
support-two commutator claims are the reviewed F.44 proof. The moved
divisor construction is F.45. The fixed radical-field argument is
written out again in Sections3 and5 because it replaces F.45's direct
valuation calculation.

The remaining primary inputs are Spiess–Szamuely4.1–4.3, Jannsen
original4.3(ii), Poonen–Slavov1.5 and finite-jet curves, CHW4.18(5),
and Stacks030D. Each is used with the original hypotheses stated above.
No new numerical computation or unproved field-automorphism rigidity
claim is used. The targeted literature comparison retains the exact
fresh CHW/Carlson–Stix primary opens recorded for F.44/F.45. Additional
searches on14 November2026 used both engines with the combinations
“étale topos”, “solvable”, “function field”, “étale reconstruction”,
“formation”, and “algebraically closed constants”. No opened primary
statement from that bounded comparison gives the combined scope here.
No priority or exhaustive literature claim is made.

| Potentially invalid shortcut | Replacement actually used |
|---|---|
| Treating the total extension over a Q-descent as pro-C | Keep \(L/F\) merely normal, and \(L/FQbar\) pro-C |
| Assuming a geometric pre-specialization A_n fixes new specialized constants | Perform the Hilbert specialization over \(FQbar\) itself |
| Applying direct integer-valued geometric valuations through the ramified pro-C closure | Use one fixed finite field \(F'=MS_0\) and integer norm valuations |
| Applying Tate-Hom over an infinite algebraic constant field | Establish equivariance and apply it over a finitely generated \(M/\mathbf Q\) |
| Descending through \(k_0k/k_0\) without checking algebraicity | Place \(k_0\) algebraically inside \((R Qbar)^{\mathcal C}\) via relative constants |
| Including the negative algebraic constant subfield | Require positive transcendence degree in the subfield statement |

## 10. Equivalent arithmetic description of this sufficient class

For a fixed allowed \(\mathcal C\), the positive-transcendence class in
Section1 is equivalently described as follows:

> There is a finitely generated field \(F_0\subset k_0\), of positive
> transcendence degree over \(\mathbf Q\), with \(k_0/F_0\) algebraic,
> such that, for its normal closure \(N/F_0\), the geometric group
> \(\operatorname{Gal}(N\overline{\mathbf Q}/F_0\overline{\mathbf Q})\)
> is virtually pro-\(\mathcal C\).

For sufficiency, choose an open pro-\(\mathcal C\) subgroup of this
geometric group and let \(C_0\) be its fixed field. The extension
\(C_0/F_0\overline{\mathbf Q}\) is finite, so
\(C_0/\overline{\mathbf Q}\) is finitely generated of positive
transcendence degree. The Galois pro-\(\mathcal C\) extension
\(N\overline{\mathbf Q}/C_0\) lies in \(C_0^{\mathcal C}\).
Thus \(k_0\subset C_0^{\mathcal C}\), and this latter extension over
\(k_0\) is algebraic. The core theorem and F.32 prove reconstruction;
the inclusion also puts the field in Section1's stated embedding class.

Conversely Section7 puts any field in that embedding class inside
\(K_1=(R\overline{\mathbf Q})^{\mathcal C}\), where \(R/F_0\) is
finite and \(F_0=\mathbf Q(T)\subset k_0\). Let \(R'/F_0\) be the
finite normal closure of \(R\). There are only finitely many
\(F_0\)-conjugates \(K_i\) of \(K_1\): an embedding of \(R\)
determines the conjugate base \(R^\sigma\overline{\mathbf Q}\), and
the maximal pro-\(\mathcal C\) closure of that base is unique in the
fixed algebraic overfield. Their compositum \(E/F_0\) is Galois and
contains \(\overline{\mathbf Q}\). For each \(i\), explicitly form
\[
         (R'\overline{\mathbf Q})K_i/(R'\overline{\mathbf Q}).
\]
It is Galois pro-\(\mathcal C\), by base change from the corresponding
maximal pro-\(\mathcal C\) extension. Their finite compositum is
pro-\(\mathcal C\), since its group is a closed subgroup of a finite
product of pro-\(\mathcal C\) groups. Therefore
\(\operatorname{Gal}(E/F_0\overline{\mathbf Q})\) has an open
pro-\(\mathcal C\) subgroup. The normal closure \(N/F_0\) of
\(k_0\) lies in \(E\), so the indicated geometric normal-closure
group is a quotient and is virtually pro-\(\mathcal C\), as required.

Taking the union over the allowed classes \(\mathcal C\), F.44's
cofinal classes avoiding one alternating subquotient give an equivalent
explicit description: the geometric normal-closure group above has an
open subgroup \(H\) and an \(m\ge5\) such that no finite continuous
quotient of \(H\) has \(A_m\) as a subquotient. This is an equivalent
description of the **proved sufficient embedding class**, not a
necessary condition for arbitrary reconstruction fields. In particular,
the total arithmetic normal-closure group need not satisfy that bound.
