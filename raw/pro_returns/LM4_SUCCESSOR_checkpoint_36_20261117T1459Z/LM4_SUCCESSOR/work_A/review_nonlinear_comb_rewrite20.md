# Independent review of the actual nonlinear comb rewrite

Reviewed 16 November 2026. Complete producer, genuine output, and result
schema read: `work_CE/code/nonlinear_comb_rewrite.py`, its `.out`/`.err`,
and `work_CE/next_symmetric_nodes/nonlinear_comb_rewrite.json`.

Verdict: PASS, at its stated pre-filling scope.

## Exact free basis

In the graph with vertices R_A times R_B, take every A-tree and the
B-tree at A=1. Their union is a spanning tree: each vertex is reached
uniquely by its B path followed by its A path. A non-tree positive
B edge at (a,b), with a nontrivial, gives the free generator

    c(a,b,x)=b[a,x]b^-1.

This is a genuine free basis of N_gen, not merely a basis of its
abelianization. The retained T-forest comparison is exactly the actual
one in B104.

## Prefix invariant and signed update

Every original paired F21 prefix is maintained as n*b*a*t in the free
group. A retained letter updates t and its actual beta image. An A
letter updates a. A positive B letter appends c(a,b,x) to n and updates
b to bx. A negative B letter appends c(a,bx^-1,x)^-1 and updates b to
bx^-1. These identities hold before any cross-commutator relation is
imposed. If a=1 the edge is in the spanning tree and contributes no
new generator. The implementation has the correct signed prefixes and
performs literal free cancellation at every level.

For all128 existing node words, the producer expands the complete
resulting free word back into the actual free product and compares it
with the entire original Schreier word. All pass. Their total comb
length is4946. The large geometric image is retained as a46944-letter
comb word using the proved prefix invariant; no unperformed expansion
of its large conjugators is claimed. Both its abelianization and the
seed abelianization agree exactly with the complete B103 dictionaries.

## Individual primitive witnesses

Every one of the128 node words has a basis generator occurring exactly
once. If its word is L*x*R with x absent from L,R, the map x->L*x*R
is an automorphism with inverse x->L^-1*x*R^-1. If the occurrence is
negative, the inverse rule is x->R*x^-1*L. The producer records the
position and sign and uses these correct rules. This gives explicit
individual primitive certificates rather than inferring primitivity
from the abelianized coefficient.

Nothing here identifies the whole relator family with a simultaneous
free basis. The actual filled M requires the entire generic-deck and
source-operator orbit of these relators. That orbit is not replaced by
the128 seed words or by their abelianizations.

## Complete nonlinear and selected-cone proof review

The full note `work_CE/research_nonlinear_comb_and_cones_20h.txt` was
subsequently read: PASS. In the actual free-product tree of
W semidirect C2=C2_tau * C2_tau1 * F10, the subgroup
N_gen semidirect C2 has nontrivial selected-cone vertex stabilizers
indexed by diag(R). This follows from its image centralizer
G^F times C2. The other cone supplies no stabilizer, since its image
is not conjugate to the selected cone already in the retained
T semidirect C2 quotient.

Choosing all representatives from one maximal-tree transversal gives
the asserted free product of those C2 factors and a free group.
Arbitrary independent representatives of the conjugacy classes would
not justify a generating free-product family; the note correctly
excludes that shortcut. Multiplying odd free stable letters by the
selected involution makes them orientation-even. Schreier normal forms
then give the orientation-kernel basis d_r=tau_r*tau and the exchanged
pairs, with exactly the stated inversion/pair involution action.

In the actual full node quotient, a residual diagonal target r has a
fixed lift exactly when the images of tau_r and tau_1 are conjugate by
M. The actual source supplies these identifications on the cosets rI.
One terminology correction was requested: use 'cosets rI' in place of
'right cosets R/I'. No quotient-tree, free-kernel, or conjugacy
injectivity conclusion is inferred.

## Uniform nonlinear transport and the non-splitting correction

The complete added Sections7--8 and
`work_CE/code/check_nonlinear_comb_transport.py`, its genuine output,
and the exact identity certificate were read independently: PASS.

Using g=(u,v,t) and the actual set section q_g=v_B*u_A*t, direct
free reduction gives

    q_g q_h = omega(g,h) q_(gh),
    omega(g,h)=v[u,tau_beta(t)(b)]v^-1

for h=(a,b,s). This is an actual nontrivial section defect. Its inner
action gives rho_g rho_h=Inn(omega) rho_(gh), and the stated
three-variable cocycle law follows from associativity. No splitting
W=N_gen semidirect G is asserted.

For a comb generator c(a,b,x), write a',b',x' for the actual retained
shifts and P_g(b)=v[u,b']v^-1. Independent expansion gives precisely

    rho_g(c(a,b,x))
      =P_g(b) c(u a',v b',x') c(u,v b',x')^-1 P_g(b)^-1.

The factor order and the conjugation correction are essential. They
reduce after abelianization to the two-term B103 formula; they do not
give a two-letter formula for the nonlinear word without its
conjugating factors.

The involution formula C(b;a) C(bx;a)^-1 also has the correct order:
the commutator identity reduces it to b_A[a_B,x_A]b_A^-1.
The section defect eta(g)=[v_A,u_B] satisfies
F(q_g)=eta(g)q_(F(g)), whence F rho_g F=Inn(eta(g))rho_(F(g)).
Its literal square equation is F(eta(g))eta(F(g))=1.

All seven executed checks are universal free-word identities. The
checker does not impose cross-family commutation. The three-variable
cocycle is correctly described as the proved associativity consequence,
not as an additional executed test. The whole-family normal-closure,
simultaneous basis, and fixed-lifting gates remain open.
