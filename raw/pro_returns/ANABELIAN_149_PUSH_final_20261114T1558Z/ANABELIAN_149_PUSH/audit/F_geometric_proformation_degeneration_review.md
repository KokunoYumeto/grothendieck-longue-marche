# Independent review of F.46: geometric pro-formation closures

**Reviewer:** degeneration. **Outcome:** PASS.
Reviewed the full candidate `audit/F_geometric_proformation_candidate.md`,
including Sections 2--8 and the two different descent fields.
This review verifies a sufficient field class; no converse classification
of reconstruction fields is inferred.

## 1. Exact statement and standing conventions

Let \(\mathcal C\) be a proper isomorphism-invariant class of finite
groups containing the cyclic groups and closed under subgroups,
quotients and extensions. Let \(K_0/\overline{\mathbf Q}\) be finitely
generated with positive transcendence degree, and let
\(k=K_0^{\mathcal C}\). The candidate proves the actual CHW
closed-point-preserving all-scheme reconstruction property for
finitely generated extensions \(L/k\) and for their subfields of
positive transcendence degree over \(\mathbf Q\).

The proof retains the corrected relative structural convention from
the preceding manuscript. It neither includes the algebraic subfield
\(\overline{\mathbf Q}\) nor substitutes a point-function conclusion
for the full CHW comparison theorem.

## 2. Normality and the two descent fields

Choose \(D/\mathbf Q\) finitely generated inside \(K_0\) with
\(K_0=D\overline{\mathbf Q}\). Every \(D\)-automorphism of the
ambient algebraic closure preserves both \(K_0\) and the collection
of its finite Galois \(\mathcal C\)-extensions. Hence \(k/D\)
is algebraic Galois.

For any finitely generated \(L/k\), take a finitely generated
\(F/\mathbf Q\), inside \(L\), containing \(D\), the finitely many
generators of \(L/k\), and all finite data at issue. Then
\[
 L=Fk,\qquad L/F\ \text{Galois},\qquad
 B=F\overline{\mathbf Q},\qquad L/B\ \text{Galois pro-}\mathcal C.
\]
The last assertion is base change of \(k/K_0\), because \(K_0\subset B\).
These assertions persist for finite extensions of \(L\) after choosing
their new finite descent fields.

The proof correctly uses \(B\) for Hilbert specialization and \(F\)
for arithmetic equivariance/Tate-Hom. It does **not** assume
\(\operatorname{Gal}(L/F)\) is pro-\(\mathcal C\).

I directly reopened Bary-Soroker--Paran, *Fully Hilbertian fields*,
https://arxiv.org/pdf/0907.0343, Theorem 1.2, author p.2
(retrieval `turn819view0`). Its hypothesis is a finitely generated
transcendental extension of an arbitrary field. This applies to
\(B/\overline{\mathbf Q}\). The version caveat in the source ledger
is correct: the retrieved arXiv header is v1, while the internal
date is September 16, 2021.

## 3. Divisible elements: the commuting-action argument

The multiplicative group \(k^\times\) is divisible: to adjoin an
\(n\)-th root of \(a\), first place \(a\) in a finite Galois
\(\mathcal C\)-extension of \(K_0\), then adjoin roots of all its
conjugates. The new normal kernel is abelian since all roots of
unity already lie in \(K_0\). The closure assumptions on
\(\mathcal C\) therefore place this new extension in \(k\).

For finite \(E/k\), the proof of \(D(E^\times)=k^\times\) is sound.
All elements of \(E\) are algebraic over \(D\), so one finite
Galois \(M/D\) can be chosen with \(E\subset Mk\), and enlarged
to contain the particular divisible element \(a\).

If \(\sigma\in\operatorname{Gal}(Mk/k)\) and
\(\tau\in\operatorname{Gal}(Mk/M)\), their restrictions commute
on each generator field:

- on \(M\), \(\tau\) is the identity and \(\sigma M=M\);
- on \(k\), \(\sigma\) is the identity and \(\tau k=k\), by
  normality of \(k/D\).

For \(z_n^n=a\) in \(E\), one has
\(\tau z_n/z_n\in\mu_n\subset k\), fixed by \(\sigma\).
Thus \(\sigma z_n/z_n\) is fixed by every \(\tau\), so belongs
to \(M\). Hence \(\sigma a/a\in(M^\times)^n\) for every \(n\).
The previously proved \(D(M^\times)=1\) for finitely generated
\(M/\mathbf Q\) gives \(a\in k\).

The passage to a finitely generated \(L/k\) uses a normal proper
model: an infinitely divisible element and all its roots have
zero divisors and lie in the finite relative algebraic closure
of \(k\). I directly reopened Stacks Lemma 9.26.11,
https://stacks.math.columbia.edu/tag/030D
(retrieval `turn819view1`), which states exactly the finiteness
needed here. Thus \(D(L^\times)=k^\times\), also after every
finite extension used in the later argument.

## 4. A missing geometric extension really remains

A proper subgroup-closed \(\mathcal C\) excludes \(A_n\) for
all sufficiently large \(n\): fix one finite group outside
\(\mathcal C\) and embed it in all sufficiently large alternating
groups. This is stronger than excluding one alternating group
and suffices for unbounded degrees.

The Hilbertian field \(K_0\) has \(S_n\)-extensions
\(\Omega_n/K_0\) for arbitrarily large such \(n\), by the
already checked regular Morse polynomial construction.
For \(n\ge5\), the quadratic fixed field of \(A_n\) belongs
to \(k\), but the whole extension cannot belong to \(k\),
since its Galois group would contain the excluded \(A_n\).
The normal subgroup possibilities of \(S_n\) therefore give
\[
                     \operatorname{Gal}(\Omega_nk/k)=A_n.
\]
If every one of these \(\Omega_n\) were contained in \(L\),
the finite relative algebraic closure of \(k\) in \(L\)
would contain extensions of unbounded degree \(|A_n|\).
This is impossible.

The resulting extension is geometric in the required sense:
\(K_0\), and already \(k\), contain all algebraic number-field
constants. Its defining finite data can be put in the finite
Galois \(M/\mathbf Q(t_1,\dots,t_d)\) used later.
Then \(Mk/L\) remains nontrivial. A nonidentity automorphism
in this group restricts nontrivially to \(M\), fixes
\(M\cap\overline{\mathbf Q}\), and has finite order.

## 5. Finite-quotient detection uses the repaired base

Let the finite arithmetic \(G\)-cover descend to \(B\).
It is connected there because its base change to \(L\) is
connected. Its finite Galois constant field \(M/B\) satisfies
\(M\cap L=B\).

The reviewed F.24 pencil construction over the characteristic-zero
field \(B\) gives a finite group \(H\), a literal \(S_n\subset H\),
and the support-at-most-two elements in its \(N^n\) subgroup.
Hilbert specialization over **\(B\)** retains the full group \(H\)
and the prescribed constant embedding \(M\).

For the specialized extension \(\Omega/B\), put
\(J=\operatorname{Gal}(\Omega L/L)\). Then
\[
 J\triangleleft H,\qquad H/J\in\mathcal C,\qquad J\longrightarrow P=G/N
 \ \text{surjective}.
\]
The third assertion follows from \(M\cap L=B\), not from a
presumed equality of all constant fields of the pencil.

Since \(A_n\) is simple and excluded from \(\mathcal C\),
\(A_n\subset J\). For a support-at-most-two element \(u\)
and an even permutation \(\tau\) with
\(\tau^{-1}i\) outside that support,
\[
 [u,\tau]\in J\cap N^n,\qquad [u,\tau]_i=u_i.
\]
This membership only uses \(\tau\in J\), \(u\in H\), and
normality. It does not assume \(u\in J\). Literal permutation
conjugation transports every generating label to every
coordinate. Thus the selected coordinate stabilizer \(J_i\)
surjects onto \(N\). Multiplication by an even permutation
returns the chosen coordinate to itself while preserving its
constant image, so \(J_i\) also maps onto \(P\), and hence onto
\(G\).

The block action is transitive because \(A_n\subset J\).
The corresponding closed point consequently has degree \(n\),
and its decomposition group detects the prescribed arithmetic
quotient. Arbitrarily large allowed \(n\) give the unbounded
degrees needed later.

The warning in the candidate is necessary: specializing over
\(F\) would not justify \(H_F/J_F\in\mathcal C\), and being
geometric before specialization does not itself control newly
acquired specialized constants. The repaired proof makes
neither inference.

## 6. The fixed radical field and norm integrality

After choosing the missing extension and its \(\sigma\), the
moved-divisor lemma applies to the nonidentity finite-order
automorphism of the finitely generated field \(M\) over its
number-field constants. The permitted finite constant
enlargement lies in \(k\), so does not change \(Mk\), and
\(\sigma\) acts trivially on the new constants.

The semilocal CRT can and does choose
\(\alpha\in U(M)\). This makes
\[
 R_j=P_j(\sigma\alpha)/P_j(\alpha)\in M^\times,\qquad
                        v_i(R_j)=-\delta_{ij}
\]
immediate. The author made this field explicit after my review
comment.

One finite \(S_0/D\) inside \(k\) suffices to put the actual
value \(b_\alpha\) in \(F'=MS_0\): an element of a compositum
uses only finitely many coefficients. Then \(F'/M\) is finite
and \(\sigma F'=F'\), because \(\sigma\) preserves \(M\) and
fixes \(S_0\subset k\).

For \(\tau\in\operatorname{Gal}(Mk/F')\), the same two-field
restriction argument proves that \(\tau\) and \(\sigma\)
commute. If \(z^n=a\in F'\) with \(z\in Mk\), then
\[
                         \sigma z/z\in F',
 \qquad                  \sigma a/a\in(F'^\times)^n.
\]
Crucially \(F'\) is fixed before \(n\) varies. Applying this
to the finite-level evaluated Kummer identity and then taking
\(v_i\circ N_{F'/M}\) yields, in \(\widehat{\mathbf Z}\),
\[
 [F':M]\lambda_i
 =-(v_i\circ N_{F'/M})(\sigma b_\alpha/b_\alpha)\in\mathbf Z.
\]
An element of \(\widehat{\mathbf Z}\) whose multiple by a
positive integer is an ordinary integer is itself an
ordinary integer: for every prime, the required denominator
divides the numerator. Thus the punctured-line integrality
argument is valid.

This norm step properly replaces F.45's direct valuation
argument. Geometric divisors can ramify in \(Mk/M\), so
their prolongations need not have value group \(\mathbf Z\).
No such false unramifiedness assertion remains.

## 7. Generalized Albanese and point functions

The inputs now match the previously reviewed F.43/F.45
arguments:

- finite arithmetic quotient detection supplies the spanning
  point-Kummer images;
- \(G_L\triangleleft G_F\) supplies the stable coinvariants;
- finitely many point coordinates and actual values descend
  to one finitely generated \(\mathbf Q\)-field;
- Jannsen's integral Tate-Hom theorem is applied over that
  field, after equivariance has been proved, not over \(k\)
  or an algebraically closed constant field;
- the single boundary divisor lattice and the norm result
  above produce a genuine normalized unit;
- \(D(E^\times)=k^\times\) for finite \(E/L\) identifies the
  residual value ambiguity exactly.

The unbounded detecting degrees are enough for the same pole-degree
point-function argument: for a nonconstant function of degree \(d\),
a point of degree greater than \(d\) cannot have its value in \(L\),
and hence cannot have it in \(k\). The affine comparison from
\(T-1\), followed by \(T-b\) for all \(b\in k^\times\), handles
both transcendental-over-\(k\) values and the values lying in \(k\).

For a constant recovered unit, the missing geometric extension
gives, after finite extension, a \(\beta\) with \(\beta/h\notin k\).
The actual point-value ambiguity forbids \(\beta\) everywhere,
so the closed-subtopos argument permits \(T-\beta\) on the
whole source. The high-degree comparison then proves that
its unit is constant and removes the remaining ambiguity.
Finite-extension stability, already proved, is used at this
step.

The final passage to all-scheme reconstruction is explicitly
CHW Theorem 4.18(5), in the original corrected convention.
It is not obtained merely by asserting that points determine
arbitrary étale-topos morphisms.

## 8. Positive-transcendence subfield descent

This is the other substantially new step, and it checks.

Let \(A=\mathbf Q(T)\subset k_0\subset L\), where \(T\) is a
finite transcendence basis of \(k_0/\mathbf Q\). Enlarge \(F\)
to contain \(T\), and let \(R\) be the relative algebraic
closure of \(A\) in \(F\). Then \(R/A\) is finite and \(F/R\)
is regular.

For \(a\in k_0\), let \(N/R\) be the normal closure of \(R(a)/R\).
Regularity identifies its \(R\)-conjugates with the corresponding
\(F\)-conjugates. Since \(L/F\) is normal and contains \(a\),
it contains \(N\). Base changing the regular extension to
\(R\overline{\mathbf Q}\) gives
\[
          N\overline{\mathbf Q}\cap F\overline{\mathbf Q}
                           =R\overline{\mathbf Q}.
\]
Thus
\[
 \operatorname{Gal}(N\overline{\mathbf Q}/R\overline{\mathbf Q})
 \cong
 \operatorname{Gal}(N F\overline{\mathbf Q}/F\overline{\mathbf Q})
\]
is a finite quotient of the pro-\(\mathcal C\) group
\(\operatorname{Gal}(L/F\overline{\mathbf Q})\).
Therefore
\[
                 k_0\subset(R\overline{\mathbf Q})^{\mathcal C}.
\]
The right-hand field reconstructs by the core theorem because
\(T\ne\varnothing\). It is algebraic over \(A\), hence over its
intermediate subfield \(k_0\). The reviewed F.32 algebraic
descent applies.

This argument checks the required algebraicity explicitly.
It does not substitute \(k_0k/k_0\), which can be
transcendental. It also explains exactly why the algebraic
subfields cannot be included.

## 9. Scope comparisons

The strict example \(\overline{\mathbf Q}(t)^{\mathrm{solv}}\)
is outside the finitely generated algebraic-constant embedding
class: its multiplicative group is divisible, whereas the
divisible subgroup of a finitely generated
\(E/\overline{\mathbf Q}\) is exactly \(\overline{\mathbf Q}^\times\).
Any embedding preserves transcendence over the algebraic
closure of \(\mathbf Q\), so cannot send \(t\) there.

The comparison with the previous proper-formation class
uses its already proved algebraic-model equivalence. Any
such model's normal closure here contains \(\overline{\mathbf Q}\)
and has a quotient onto an absolute Galois group of a number
field. No open subgroup of the latter can be pro-\(\mathcal C'\)
for a proper hereditary \(\mathcal C'\), because every
number-field absolute Galois group has arbitrarily large
symmetric quotients. This gives the claimed strictness within
the precise earlier sufficient classes.

The new theorem includes the positive-transcendence portions
of those classes by the explicit algebraic descent in Section 7.
It does not supersede their algebraic number-field-extension
cases and does not solve the intrinsic necessity problem.

**Final review:** all new field, group, valuation and descent
steps pass. No mathematical correction remains after the
harmless clarification \(\alpha\in U(M)\).

## 10. Addendum: the equivalent geometric normal-closure description

**Later addition reviewed independently: PASS.** This addresses the
candidate's Section 10, which was added after the preceding review.

For the forward sufficient implication, an open pro-\(\mathcal C\)
subgroup of
\[
 \operatorname{Gal}(N\overline{\mathbf Q}/F_0\overline{\mathbf Q})
\]
has a finite fixed field \(C_0/F_0\overline{\mathbf Q}\).
The field \(C_0/\overline{\mathbf Q}\) remains finitely generated
of positive transcendence degree. The ambient extension is Galois
over \(C_0\), with exactly that pro-\(\mathcal C\) group, even
when the open subgroup is not normal over the original base.
It therefore lies in \(C_0^{\mathcal C}\). This field contains
\(k_0\), and is algebraic over it: every intermediate field here
is algebraic over \(F_0\subset k_0\). Thus both the embedding
claim and the application of F.32 are justified.

Conversely, Section 7 embeds the field into
\((R\overline{\mathbf Q})^{\mathcal C}\), where \(R/F_0\)
is finite and \(F_0\subset k_0\). There are finitely many
\(F_0\)-conjugates \(K_i\) of this maximal closure.
Indeed the image is determined by the image of \(R\);
automorphisms also permute \(\overline{\mathbf Q}\), but
preserve it as a field. The maximal pro-\(\mathcal C\)
extension of a fixed conjugate base is unique in the
chosen algebraic overfield.

Their compositum \(E\) is Galois over \(F_0\).
It contains the normal closure \(R'\) of \(R/F_0\), since
all conjugate copies of \(R\) occur among the bases, and
it contains \(\overline{\mathbf Q}\). The explicitly
written composita
\[
 (R'\overline{\mathbf Q})K_i/(R'\overline{\mathbf Q})
\]
are Galois pro-\(\mathcal C\) by base change. This formulation
is essential: an individual \(K_i\) need not contain \(R'\).
Their compositum is \(E\), and its group over
\(R'\overline{\mathbf Q}\) is a closed subgroup of the
finite product of those pro-\(\mathcal C\) groups.
The subgroup/quotient closure assumptions on \(\mathcal C\)
make it pro-\(\mathcal C\).

Because \(R'\overline{\mathbf Q}/F_0\overline{\mathbf Q}\)
is finite, this subgroup is open in the geometric group
of \(E\). The normal closure \(N/F_0\) of \(k_0\) is
contained in \(E\), so the desired geometric group for
\(N\overline{\mathbf Q}\) is a quotient. The image of
an open pro-\(\mathcal C\) subgroup is again open and
pro-\(\mathcal C\). This establishes the claimed equivalence.

Finally, the union over proper allowed classes is equivalent
to avoiding one alternating subquotient on the finite
quotients of an open subgroup. Every proper hereditary
class excludes all sufficiently large \(A_m\), and then
cannot contain a group having \(A_m\) as a subquotient.
Conversely the finite groups without an \(A_m\) subquotient
form a proper subgroup-, quotient-, and extension-closed
class containing the cyclic groups. For extension closure,
a simple \(A_m\) subquotient would have either its whole
image or trivial image from the kernel, placing it in
one of the two factors.

This equivalence concerns exactly the **proved sufficient
embedding class**. It neither asserts necessity for all
reconstruction fields nor puts the same restriction on
the total arithmetic normal-closure group.


