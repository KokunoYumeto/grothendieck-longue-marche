# Formal normalization and group actions: post-freeze checks

Author: GPT-6 Astra Pro, delegated agent `formal_checks`, 18 November 2026.
The transcription was frozen at 2026-11-18 01:04:49 UTC. This report uses only
the frozen page TeX and the supplied context. No scan image was read, and no
page TeX was changed. All line references below refer to the frozen files
`pages/MPL_159_159_scanNNN.tex`. A line reference identifies the proposition
being checked; it does not resolve the transcription's `unsure` alternatives.

The exact finite calculations are in `formal_group_checks.py`, with output
`formal_group_certificate.json`. The finite calculations certify the examples
and listed jets, not the general theorems; the proofs below supply the latter.
Proposed events, separate from the main event ledger, are in
`CHECK_EVENTS_formal_proposed.tsv`.

## Source and context credit

The supplied `context/hua_project/README.md` identifies the modernized reading
as the AI-produced work of Michel Hua's project, not as a transcription and
not as our own result. This report credits its formal-rigidity interpretation
to **Hua, modernised reading of cote 159**, particularly these subsections:

- **Le cadre, tel que les pages 32 et 33 le posent**, lines 1217–1279;
- **Le théorème de rigidité (pages 25 et 26)**, lines 1282–1344;
- **Le calcul du changement de paramètre (pages 27, 28 et 30)**, lines 1347–1400;
- **La structure du groupe G (pages 29 et 31)**, lines 1403–1462;
- **L'énoncé final**, lines 1465–1493.

The supplied findings register names this interpretation
`159-formal-rigidity-quadratic-torsor`
(`context/notes/RESULTS_STATE.md`, lines 18 and 468). Its use of **invertible
symbol** is essential. The independent work here checks the triangular
calculation, supplies exact hypotheses and counterexamples, and corrects two
claims in that interpretation. It does not claim a new proof of every global
existence statement in the findings register.

## A. The group-action lemma on scan 032

### FC-A1. The factorization and transversal assertion are valid

**Frozen source:** scan 032, lines 5–12, 17–25 and 30–33; compare scan 030,
lines 13–43. **Context:** Hua, *La structure du groupe G*, lines 1435–1457.

Let a group G act on C, let H be a subgroup, and suppose the action map

\[
H\times C_0\longrightarrow C
\]

is a bijection. For c in C₀, set A = G(c) = {a in G : ac is in C₀}.
For each g in G, write gc = h c′ using the unique pair (h,c′) supplied by the
hypothesis. Then a = h⁻¹g belongs to A, so g = ha. If ha = h′a′, uniqueness
of the expression of the common point h(ac) = h′(a′c) gives h = h′ and then
a = a′. Thus multiplication H × A → G is bijective, and A maps bijectively
to the set of left cosets H\G. No assumption that A is a subgroup is used.

The margin assertion on scan 032, lines 28–29, is also valid: H\C is C₀;
if H is normal, G/H acts on that orbit set, and C/G is C₀/(G/H). The induced
action on C₀ means transporting the action on H\C through the bijection;
it need not mean restricting the original G-action to C₀.

### FC-A2. The orbit intersection requires a stabilizer quotient

**Frozen source:** scan 032, line 34 explicitly asks whether gc=c implies
g=1; lines 38–39 then assert O∩C₀ ≅ H\G. **Context:** Hua, *La structure du
groupe G*, lines 1459–1462, endorses the orbit assertion without this caveat.

Put K = Stab_G(c). A is stable under right multiplication by K. The
evaluation map A → (Gc)∩C₀, a ↦ ac, is onto and has exactly the fibers aK.
Consequently the corrected formula is

\[
(Gc)\cap C_0\simeq A/K\simeq H\backslash G/K.
\]

The manuscript's simpler formula is correct if K is trivial. The original
hypothesis implies that H acts freely on C, but it does not imply that G
does. Equivalently, it ensures K∩g⁻¹Hg={1}, which allows nontrivial K.

**Finite counterexample.** Let G=C₂×C₂, H=C₂×{0}, K={0}×C₂, let C=G/K,
and let C₀ consist of the identity coset. H×C₀→C is bijective. The left
coset space H\G has two elements, whereas (Gc)∩C₀ has one. This is checked
by exhaustive enumeration in the certificate. It directly refutes the
unqualified abstract orbit assertion, not the factorization lemma.

In the actual characteristic-zero formal-coordinate application, a regular
symbol makes the full group G act freely by the leading-coefficient argument
in FC-B3 below. Thus this abstract omission need not invalidate the concrete
orbit conclusion once that extra freeness is supplied.

### FC-A3. G(c) need not be a subgroup

**Frozen source:** scan 030, line 13 calls G(c) a *sous-ensemble*.
**Context:** Hua, *La structure du groupe G*, line 1428 upgrades this to
*sous-groupe*. That upgrade is false without another hypothesis.

Take G=C₄ additively, H={0,2}, C=G with its regular action, C₀={0,1}, c=0.
The action map H×C₀→C is bijective, and H is normal, but G(c)={0,1} is not
closed under addition: 1+1=2. Thus even normality of H and freeness of G do
not turn the transversal into a subgroup. FC-B7 supplies a counterexample
inside the specific formal-normalization setup as well.

## B. Symbols and formal normalization on scans 026–034

### FC-B1. The induced graded map contains the factor i

**Frozen source:** scan 033, lines 34–45 and scan 034, lines 3–4. Compare
scan 031, lines 15–17 and 36–39, where the factors i and i+1 are explicit.
**Context:** Hua, *Le cadre*, lines 1260–1273 repeats an induced graded map
given by a coefficient independent of i.

For an ordinary algebra derivation C and a local generator t,

\[
C(t^i)=i t^{i-1}C(t).
\]

If C(t) modulo J is a₀η, the map grⁱ→grⁱ⁻¹⊗Ω¹ sends tⁱ to
i a₀tⁱ⁻¹η. It is the degree −1 derivation determined by the degree-one
symbol, not a Sym(Ω)-linear map. Already C(t)=dx gives
C(t²)=2t dx, whereas tC(t)=t dx. The degree-one symbol a₀ is independent
of i; the induced maps are not. Over a Q-algebra one can separately divide
the degree-i map by i, but that is a different construction, absent from
the displayed ordinary graded derivation. The frozen transcription should
remain unchanged; the mathematical statement requires this qualification.

The other coefficient assertion on scan 033, lines 26–31, is valid. In
C(λt)=λC(t)+t dλ the additional term has degree one, so each coefficient
except the degree-one coefficient is O-linear. The degree-one coefficient
is a connection on Ω. This verifies the corresponding distinction in Hua,
*Le cadre*, lines 1245–1256.

### FC-B2. When a complete augmented algebra is a power-series algebra

**Frozen source:** scan 033, lines 4–5 and 18–19; strengthened symbol
hypothesis on scan 026, lines 4–8. **Context:** Hua, *Le cadre*, lines
1221–1237, and the distinction between regular and very regular in frozen
scan 034, lines 3–8.

The conditions that A is separated and complete for its augmentation ideal
J and that J/J² is an invertible R-module do not alone give A≅R[[t]].
For example, A=Q[x][ε]/(ε²), J=(ε), satisfies them. It even admits an algebra
connection extending d on Q[x], with C(ε)=0. It is not a power-series
algebra. This example has zero symbol.

Here is a sufficient statement using the connection rather than a separate
formal-smoothness hypothesis. Work locally, let R be a Q-algebra, let
Ω¹_R/S=Rη, and suppose A is an augmented, J-adically separated and complete
R-algebra with J/J² free of rank one. Suppose C extends d_R and that its
symbol sends a generator of J/J² to a₀η, with a₀ a non-zero-divisor in R.
Then A≅R[[t]] as an augmented topological R-algebra. In particular, this
applies when the symbol is an isomorphism, as explicitly required on
scan 026.

**Proof.** Choose a lift t in J of a generator. Multiplication shows that
Jⁿ/Jⁿ⁺¹ is generated by tⁿ: replace each factor of a product of n elements
of J by its first-order multiple of t. Successive approximation and
completeness give a continuous surjection φ:R[[T]]→A, T↦t. Write
d_R(r)=D_R(r)η and choose a series f(T) lifting C(t)/η, with f(0)=a₀.
The derivation

\[
\widetilde D=D_R+f(T)\partial_T
\]

lifts C/η, so I=ker φ is stable under it. The derivations are continuous
with a one-step loss of filtration, by Leibniz, which justifies this identity
for series. If I≠0, choose a nonzero F in I of smallest T-adic order n.
Since φ respects the augmentation and is the identity on R, n≥1. If the
first coefficient of F is r≠0, then the first term of D̃F is
n a₀r Tⁿ⁻¹. It is nonzero because n is a unit and a₀ is a non-zero-divisor.
This is a relation in I of lower order, a contradiction. Therefore I=0.

This is an independently checked local proof, not a claim that completeness
by itself supplies formal smoothness. With only a bare rank-one conormal
module, one must assume a suitable free/formally smooth formal-disc
presentation or prove it using additional structure as above.

The characteristic restriction matters even for this presentation step.
Over R=F_p[x], the truncated algebra A=R[t]/(t^p), J=(t), has J/J²≅R and
the connection C=(∂_x+∂_t)dx has unit symbol. It is well-defined since
∂_t(t^p)=0, yet A is a truncated algebra, not R[[t]].

### FC-B3. Exact coordinate formula and recursive normalization

**Frozen source:** scan 029, lines 9–29 and 31–45; scan 031, lines 36–39;
scan 026, lines 24–28; scan 027, lines 2 and 6–10. **Context:** Hua,
*Le calcul du changement de paramètre* and *Le théorème de rigidité*.

Use R a Q-algebra, Ω¹_R/S=Rη, A=R[[t]], and write

\[
C=\bigl(D_R+f(t)\partial_t\bigr)\eta,
\qquad f(t)=a_0+a_1t+a_2t^2+\cdots.
\]

Here D_R acts coefficientwise and d_R(r)=D_R(r)η. If h is the augmented
R-algebra automorphism t↦h(t), and k is its compositional inverse, fix the
action convention C^h=h⁻¹Ch. Its coefficient is exactly

\[
f^h(t)=\bigl(D_Rh+f\,\partial_t h\bigr)(k(t)).
\]

For h(t)=t+b_m t^m+O(t^{m+1}), m≥3, this gives

\[
f^h(t)=f(t)+m a_0b_m t^{m-1}+O(t^m).
\]

Indeed D_R(b_m)t^m has order m, and substituting k(t)=t−b_mt^m+…
into f affects it only from order m onward. This is the precise version
of scan 029's factor (n+1)α_n with m=n+1.

If a₀ is a unit, normalize successively at m=4,5,… . If r_{m−1} is the
current coefficient of t^{m−1}, take

\[
b_m=-\frac{r_{m-1}}{m a_0}.
\]

Each step fixes all previously normalized coefficients. The infinite
composition converges t-adically to an automorphism in G₀ (identity modulo
t⁴), and leaves precisely the quadratic coefficient function
a₀+a₁t+a₂t². If two such normalizations existed, their quotient would have
a first nonzero coefficient b_m at some m≥4. The displayed formula would
produce a nonzero coefficient in degree m−1≥3, contradicting that both
connections are quadratic. Thus the normalization is unique.

The same first-nonzero-coefficient argument gives uniqueness when a₀ is
only a non-zero-divisor. It also shows that the full group G (identity
modulo t³) has trivial stabilizers on connections with regular symbol:
an automorphism fixing a connection would have m a₀b_m=0 at its first
nonzero term, impossible. This supplies the missing K={1} hypothesis for
the concrete use of FC-A2.

For G, the coefficient b₃ is free. It changes the quadratic coefficient
by 3a₀b₃, and the coefficients of degree at least four in h are then
determined uniquely by the same recursion. Intrinsically the cubic jet is
in Hom(Ω,Ω³)=Ω². This checks the local mechanism behind the quadratic
differential ambiguity credited to Hua; it is not, by itself, a proof that
every global third-order lifting torsor is nonempty.

### FC-B4. Regular symbol gives uniqueness; invertible symbol gives existence

**Frozen source:** scan 034, lines 3–8, 15 and 19–23. Its alternatives
`bijective|injective` and `resp.|unq.` remain reading questions.
**Context:** Hua, *Le cadre*, lines 1273–1276 merges the two notions;
*L'énoncé final*, lines 1467–1477 uses that merged terminology.

Take R=Q[x], A=R[[t]], and

\[
C=\bigl(\partial_x+(x+t^3)\partial_t\bigr)dx.
\]

The symbol x is a non-zero-divisor, but it is not a unit at x=0. For any
h=t+b₄(x)t⁴+…, the cubic coefficient of C^h is 1+4xb₄(x). It cannot
vanish in Q[x], or in the local ring at x=0, as evaluating at x=0 shows.
Thus the G₀-normalization map is not surjective for this regular symbol.
This makes a regular/injective versus very-regular/bijective distinction
mathematically natural, without choosing a frozen paleographic alternative.

The phrase characteristic zero should also be interpreted strongly enough
to allow these divisions, for example over a Q-scheme. The ring Z[x] has
characteristic zero, but for C=(∂_x+(1+t³)∂_t)dx the first correction would
require b₄=−1/4. No such normalization exists over Z[x]. This does not
assert that the manuscript intended the broader ring-theoretic meaning.

### FC-B5. Positive-characteristic resonance, even with zero p-curvature

**Frozen source:** scan 029, lines 25–29 and 45; scan 034, line 9.
**Context:** Hua, *Le calcul du changement de paramètre*, lines 1378–1389.

Let R=F_p[x], A=R[[t]], C=(∂_x+∂_t)dx. Choose a p-power q=p^r≥4 and set
g(t)=t+t^q, fixing R. It is a nontrivial augmented automorphism, identity
modulo t⁴, with inverse

\[
g^{-1}(t)=\sum_{j\geq0}(-1)^j t^{q^j}.
\]

Both compositions are the identity because qth powers act termwise and
the terms cancel successively (in characteristic two the signs coincide,
and cancellation still holds). Since g′=1 and its coefficients are
constant in x, g commutes with ∂_x+∂_t. Thus C^g=C: uniqueness at a fixed
third jet fails for every prime p, even with unit symbol. This is an
all-orders counterexample, supplemented by exact finite checks for
p=2,3,5,7,11 in the certificate.

For additional modern comparison, this example has zero p-curvature.
The definition ψ(D)=∇(D)^p−∇(D^p) and its Frobenius-linearity are in
Nicholas M. Katz, *Nilpotent connections and the monodromy theorem:
applications of a result of Turrittin*, Publ. Math. IHÉS 39 (1970),
§5, equation (5.0.4), p.190, and Proposition 5.2, p.191:
<https://www.numdam.org/item/PMIHES_1970__39__175_0.pdf>.
Here the two partial derivations commute and each has pth iterate zero,
so (∂_x+∂_t)^p=0 and (∂_x)^p=0. Hence ψ(∂_x)=0, and Frobenius-linearity
gives ψ=0. The same identities are valid on the completed algebra.
Only the definition and Frobenius-linearity are credited to Katz; this
specific example and its use here are independently checked.

This is a limitation of ordinary connection rigidity in characteristic p;
it does not claim that the manuscript formulates p-curvature, or settle
what an additional stratification or divided-power structure would do.

### FC-B6. Reciprocal multiplication is not compositional inversion

**Frozen source:** scan 029, lines 4–6; scan 031, lines 46–48.
**Context:** Hua, *Le calcul du changement de paramètre*, lines 1357–1369,
explains a multiplicative factor but does not address this distinction.

Write h(t)=t(1+Σα_it^i) and k=h⁻¹. The identity h(k(t))=t gives

\[
k(t)=\frac{t}{1+\sum_i\alpha_i k(t)^i}.
\]

It does not in general give k(t)=t/(1+Σα_it^i). For h(t)=t+t³, which
already lies in G, the actual inverse begins

\[
k(t)=t-t^3+3t^5-12t^7+55t^9-273t^{11}+\cdots,
\]

whereas the displayed reciprocal substitution gives t−t³+t⁵−t⁷+… .
Composing h with the latter gives t−2t⁵+5t⁷−9t⁹+… . The certificate
checks both inverse compositions through degree eleven.

Thus the literal same-coefficient, same-variable denominators in the
frozen formulas cannot be exact automorphism conjugation. A suppressed
evaluation at k(t), or an unstated redefinition of the coefficients, could
repair the expression; neither is explicit in those frozen displays. This
is recorded as a mathematical reading question, not a transcription edit.
It does not refute the valid leading congruence used in FC-B3: at the first
nonzero coefficient, reciprocal and compositional inverse agree to the
order needed for that congruence.

### FC-B7. A normal-form transversal that is not a subgroup

**Frozen source:** scan 030, line 13 and lines 21–25; scan 034, lines 28–33.
**Context:** Hua, *La structure du groupe G*, line 1428.

Over Q[x][[t]], take C=(∂_x+∂_t)dx, and let h be the unique series with
h(0)=0 satisfying h′=1+h². It starts

\[
h=t+\tfrac13t^3+\tfrac{2}{15}t^5+\cdots,
\quad h^{-1}=t-\tfrac13t^3+\tfrac15t^5+\cdots.
\]

Both are in G. With C^h=h⁻¹Ch,

\[
C^h(t)=(1+t^2)dx,
\qquad C^{h^{-1}}(t)=
(1-t^2+\tfrac13t^4-\tfrac{2}{45}t^6+\cdots)dx.
\]

The first is projective/quadratic, the second is not. Hence h belongs to
G(c) but h⁻¹ does not. This confirms, within the actual formal setup, that
the valid factorization gives a transversal, not generally a subgroup.
The certificate constructs h recursively and checks the inverse and
conjugated coefficients through the stated finite order; the nonzero
t⁴ coefficient already proves failure of subgroup closure.

### FC-B8. Sheaf quotients, global groups, and the pseudo-torsor caveat

**Frozen source:** scan 027, lines 8–10 explicitly inserts *pseudo* before
*torseur*; scan 030, line 7 and scan 034, line 33 identify G/G₀ with global
sections. **Context:** Hua, *Le théorème de rigidité*, lines 1323–1325;
*La structure du groupe G*, lines 1405–1419; *L'énoncé final*.

Locally, extraction of the cubic coefficient gives an exact sequence of
sheaves of groups with quotient the additive sheaf Ω². This does not alone
prove that every global section of Ω² lifts to a global automorphism.
For a general sheaf extension, local lifts differ by a G₀-cocycle whose
torsor class must be neutral for a global lift. Consequently one must
distinguish (G/G₀)(X) from G(X)/G₀(X).

There are concrete sufficient hypotheses in this problem:

1. **Globally split algebra.** If the algebra is globally
   Symhat(Ω), a global q:Ω→Ω³ extends to the formal automorphism defined
   on Ω by ω↦ω+q(ω). Its invertible first-order term gives a formal inverse,
   constructed uniquely degree by degree. This is a global lift of q,
   so G(X)/G₀(X)≅Γ(X,Ω²) in this case. No vanishing of H¹ is required.
2. **Given very regular projective connection on a completion of a
   P¹-bundle.** Suppose one has a global projective connection c with unit
   symbol. A global q in Γ(Ω²) defines a second projective connection
   c′ by adding the vertical quadratic vector field with coefficient
   3·symbol(c)·q. This is intrinsic: in local section coordinates, the
   transition t_j=a t_i/(1+b t_i) sends t_i²∂_{t_i} to
   a⁻¹t_j²∂_{t_j}; these fields form the required line subbundle.
   The local normalization proof produces a unique conjugacy from c to c′
   with cubic jet q. The local conjugacies agree on overlaps by uniqueness
   with a prescribed third jet, so they glue. This supplies a global lift
   and justifies the quotient under these hypotheses as well.

Similarly, when a fixed global P¹-bundle and section are already given,
the local unit-symbol G₀ normalization of a formal connection glues:
two local normalizations, compared in a projective transition coordinate,
differ by a G₀ transformation between quadratic connections, hence agree.
This is an obstruction-control argument, beyond local jet-surjectivity.

For an arbitrary formal algebra and an order-two identification with a
prospective projective model, this report does not prove that the sheaf of
order-three extensions has a global section. If it has a section, its set
of global sections is a torsor under Γ(Ω²); otherwise it is empty. The
frozen *pseudo-torseur* accurately preserves this possibility. The local
recursion gives existence and uniqueness of the infinite extension of a
**given** third-order identification under the stated unit-symbol
hypotheses. It does not silently establish nonemptiness of that earlier
lifting problem.

### FC-B9. A prescribed third jet fixes the compatible quadratic connection

**Frozen source:** scan 026, lines 24–28, continued by scan 027, line 2,
whose literal wording quantifies over every very regular c while also
requiring extension of a fixed u₃. **Context:** Hua, *Le théorème de
rigidité*, lines 1303–1306 and 1323–1327 organizes the extension theorem
and the correspondence; its footnote at lines 1312–1318 does not check
this compatibility condition.

In the coordinates of FC-B3, a prescribed third jet h(t)=t+b₃t³ modulo
t⁴ forces the first three target coefficients to be

\[
(a'_0,a'_1,a'_2)=(a_0,a_1,a_2+3a_0b_3).
\]

There is one compatible quadratic coefficient function, not an arbitrary
independently chosen quadratic connection. Subsequent terms of h cannot
change these coefficients. For instance, let C=(∂_x+∂_t)dx over Q[x][[t]]
and prescribe u₃=id modulo t⁴. Every prolongation lies in G₀ and has
quadratic coefficient zero after conjugation, whereas the very regular
projective connection c′=(∂_x+(1+t²)∂_t)dx has quadratic coefficient one.
There is no such prolongation carrying C to c′. Changing the direction
of the conjugation does not affect this counterexample.

Accordingly, the checked theorem is: a given third-order identification
extends uniquely to a normalization, and thereby determines a compatible
projective connection. If a target projective connection is specified as
well, its coefficients through degree two must match those forced by the
third-order identification. The unqualified combination of an arbitrary
c and an arbitrary fixed u₃ is false. This is another mathematical
qualification of the frozen wording, not a proposed page edit.

## Verification scope and reproducibility

Run `python3 MPL_159/research_checks/formal_group_checks.py` from the
workspace root. The script uses only Python's standard library and exact
rational or finite-field arithmetic. It checks the two finite group
counterexamples, the reciprocal-inverse counterexample, the formal
normal-form non-subgroup counterexample, the ordinary graded factor,
and finite truncations of the positive-characteristic automorphisms.
Every assertion passed. The all-orders algebra and descent arguments are
given explicitly above; they are not inferred from finite testing.

No claim here decides a paleographic uncertainty, changes the frozen
transcription, proves a broad new theorem about p-curvature, or removes
the global nonemptiness caveat on arbitrary third-order liftings.
