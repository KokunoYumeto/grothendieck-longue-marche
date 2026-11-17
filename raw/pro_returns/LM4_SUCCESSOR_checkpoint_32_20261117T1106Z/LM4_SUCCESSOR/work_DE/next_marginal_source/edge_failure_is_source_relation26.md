# The failed enlarged-edge relation is the actual source commutator

Research comparison, checkpoint26. This note uses the actual markings of
B125, A's `hnn_edge_enlargement_failure26.md`, and the raw source identity
proved in B130. It makes no new presentation or embedding claim after
cross filling.

## 1. Actual pre-cross groups and words

Let `A=R *_K (K semidirect_eta <j>)` be the actual pre-cross group,
with the original parity zero on `K,j` and one on the regional cone `C`.
Its parity kernel is the proper star of B125. In its mirror-even cover,
collapse the `K` edge and write

\[
V=R^0*_{K}p(R^0),\qquad p(r)=j_0rj_0,\qquad
p(u)=\eta(u)\quad(u\in K).
\]

Set

\[
a_1=CaC,\quad k_1=CkC,\quad t=j_0j_1,\quad
v_0=p(aa_1^{-1}),\quad t_0=v_0t.
\]

The existing HNN edge map, before any proposed enlargement, is

\[
tut^{-1}=\sigma(u)=p\bigl(C\eta(CuC)C\bigr)
\quad(u\in CKC).
\]

In particular `t a1 t^-1=sigma(a1)`. The selected opposite cone is
`tau=t0 C`; this is the actual selected-gap convention, not the local
regional cone. Since `tau^2=1`,

\[
\tau a\tau=t_0a_1t_0^{-1}.
\]

Hence, already in the pre-cross group,

\[
N_\tau(a):=a\tau a\tau
 =a v_0\sigma(a_1)v_0^{-1}.                 \tag{1}
\]

This uses only the genuine old edge relation. It does not presume a
map from the larger subgroup `<CKC,CkC>` into `V`.

## 2. Exact relation comparison

Put `s=v0^-1 k v0`. For arbitrary free words the complete identity is

\[
[k,a v_0\sigma(a_1)v_0^{-1}]
 =[k,a]\,(a v_0)[s,\sigma(a_1)](a v_0)^{-1}.       \tag{2}
\]

The regional relation `[k,a]=1` is already present before the cross
filling. Thus (1)--(2) give the literal marked conjugacy

\[
[k,N_\tau(a)]
 =(a v_0)[s,\sigma(a_1)](a v_0)^{-1}.              \tag{3}
\]

The right-hand commutator is exactly A's failed edge-extension image
of the true domain relation `[k1,a1]=1`. The actual cross relation is
`t k1 t^-1=s`. Conjugating the domain relation by `t` after filling
therefore kills the right side of (3), and hence the left side.

## 3. The nontrivial base word and its actual source marking

Write `A0=eta(a)`, `q=p(a1)`, and

\[
v=a^{-1}\eta(a)a=B a^{-1}B^{-1},\qquad Y=p(CvC).
\]

The literal neck formula is
`eta(a)=a B a^-1 B^-1 a^-1`. Therefore

\[
v_0=A_0q^{-1},\quad q^{-1}\sigma(a_1)q=Y,
\]
and the exact equivalent version of (3) is

\[
[k,N_\tau(a)]
 =(aA_0)\,[A_0^{-1}kA_0,Y]\,(aA_0)^{-1}.         \tag{4}
\]

The first factor of this middle commutator lies in `R0` outside `K`
by its base winding one. The second lies in `p(R0)` outside `K`:
`CvC` is nontrivial in the embedded free conjugate neck `CKC`, while
the actual regional retraction sends it to one. Membership in `K`
would contradict that retraction. Thus the middle word is a reduced
alternating length-four word in the proper amalgam `V`. It is
nontrivial, so (4) is nontrivial before cross filling.

The raw proof of B130 uses only the three actual plus regional node
relations and the actual neck reflection. All are already present in
this pre-cross group. Consequently its raw source prelifts satisfy

\[
U=s_1s_4^{-1}s_1^{-1}=N_\tau(a)
\]
before imposing the cross commutator. The specified source word
`[k,s1 s4^-1 s1^-1]` is therefore exactly the nontrivial base element
in (4), killed by the actual cross relation. This connects the failed
unchanged-base HNN proposal with the source noninjectivity result;
they are not unrelated obstructions.

## 4. Exact scope and evidence

This is a discrete marked identity and normal-form comparison. It
does not assert a new full profinite embedding for `V`, nor that any
regional vertex survives after cross filling. B130 separately proves
the actual full source noninjectivity and its specified compact
intermediate comparison.

The independent checker `check_edge_source_identity26.py` retains the
entire regional `[k,a]` correction in the universal word calculation,
checks the actual selected cone and old stable-letter words, and
reads the literal `eta(a)` from the complete actual presentation.
Its genuine stdout/stderr and JSON are adjacent. No producer from A
or CE is imported, and no group census is used.
