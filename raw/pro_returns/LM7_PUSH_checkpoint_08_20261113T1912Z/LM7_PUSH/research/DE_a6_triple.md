# Explicit central-three Ferrari refinement of the retained A6 source

This is an ongoing finite-source calculation, outside the frozen E48,
E54 and E57 packages. No assertion about a CM fibre lifting through this
new source has yet been made.

## Exact matrix cover

`de_a6_triple_cover.py` enumerates all 262144 matrices over
F4=F2[t]/(t^2+t+1). Exactly60480 have determinant one. The six displayed
projective points are the four points (1,u,u^2), u in F4, together with
(0,0,1) and (0,1,0). All20 triples are independent. The complete
determinant-one stabilizer U has order1080. Its actual permutation on
these six points is identified element by element with the retained
360-element A6 model; every one of the1080^2 products respects this
specified quotient map. Its kernel and its entire centre are the three
scalar matrices. Thus the actual map is

    1 -> <tI> -> U -> A6 -> 1.

The chosen two lifts of the retained A6 generators generate U. The
normal closure of their commutator is the entire1080-element group,
proving that U is perfect. A literal word in their commutator conjugates
evaluates to tI and has zero ordinary exponent sums; the word is saved.
No identification of U with an abstract multiplier-table entry is used.

Every retained automorphism of A6 has been lifted. For each of the1440
maps, the program begins with fixed lifts of its two generator images
and retains both independent central shifts. The complete2160-edge
Cayley presentation gives a linear system over F3. Its two selected
independent rows determine the shifts; all2160 rows are then checked.
Each resulting map is bijective and respects every Cayley edge.
All1440^2 compositions are checked on both generating elements. The
centre character is exactly (1,2,1,2) on the saved outerV4 coordinate
order. It is explicitly a homomorphism.

The map Aut(U)->Aut(A6) is also injective: an automorphism inducing the
identity on U/Z(U) has the form u->u z(u), with z:U->Z(U) a homomorphism.
Perfection of U makes z trivial. Together with the explicit1440 lifts,
this proves the actual automorphism comparison is an isomorphism.

This program passed in46.841 seconds; its complete matrix tables,
quotient map, automorphism maps, central shifts, literal Cayley trees
and relation exponent matrix are saved in `de_a6_triple_cover.npz`.

## Universal free image and all epikernels

For each of the53 retained Aut(A6)-orbits of epimorphisms F2->A6,
choose the two saved U lifts. The joint image J in U^53 maps onto A6^53:
the original complete epikernel enumeration and the explicit simplicity
certificate prove this projection by the subdirect-product argument.
Write Z=Z(U)^53. Then JZ=U^53, and centrality gives

    U^53=[U^53,U^53]=[JZ,JZ]=[J,J] <= J.

Hence J=U^53. Adjoining the ordinary free abelianization F2->C3^2
gives the full product U^53 x C3^2, since any common quotient of the
perfect group U^53 and the abelian group C3^2 is trivial.

Every generating pair of A6 has nine U lifts, all generating by the same
central-perfect argument. Distinct central twists over a fixed A6 pair
cannot be identified by an automorphism of U: such an automorphism
would induce the identity on A6 and is therefore the identity. Thus
there are exactly53*9=477 epikernels to U. The remaining424 evaluations
are recovered from the chosen53 and the two global C3 characters by

    w(z^a g,z^b h)=z^(a exp_x(w)+b exp_y(w)) w(g,h).

The exact formula holds because z is central. The model separately
checks every477 evaluation on50 literal free words.

## Exact Ferrari action

An automorphism of the universal image has retained coordinates
(p,alpha,E,M), where p permutes the53 factors, alpha_j belongs to the
actual Aut(U), E has53 rows and two F3 entries, and M acts on C3^2.
It sends (k,t) to

    ( z^(E_j t) alpha_j(k_(p(j))), M t ).

If epsilon(alpha) is the proved centre character, composition has cross
term E N + epsilon(alpha) D[p]. This character is retained in every
operation, including inversion. A Ferrari element additionally retains
its translation (k,t), giving271 integer coordinates. The two Nielsen
generators act by (g,h)->(g,hg) and (g,h)->(g h^-1,h), and c=xi1 a.
These exact formulas give all three braid relations, all four free-kernel
conjugation identities and all six pentagon substitution pairs.

The projection to the retained full A6 model is

    (p,alpha,E,M,k,t) -> (p, Inn(q(k)) alpha, alpha),

where q:U->A6 is the specified six-point quotient. Its second projection
is the affine action (M,t) on F3^2. The common kernel in the ambient
model is the elementary abelian group with53 central translation and106
cross-character coordinates, dimension159. All159^2 basis products,
their conjugation actions and the conjugation composition law are
checked. The full model also independently verifies both projections
on1000 successive literal braid words and all six substitution pairs.
All three braid generators have exact order60.

`de_a6_triple_model.py` passed in2.009 seconds. These are comparisons of
actual finite maps. The induced B source and its complete correction
image still require the next calculation.

## Induced source base gate

`de_a6_triple_affine_prepare.py` reconstructs all36 source evaluations
using the saved six-coset free-product comparison. The full A6 projection
matches the9462-point strong-generator certificate literally, after its
saved compression and point conjugacy. The affine projection acts on324
points and has order46656. All source generator products respect both
projections.

`de_a6_triple_affine.cpp` is checking the complete865049-relator
presentation of that actual A6 source in the affine projection. The
result will decide the exact base for the elementary-three extension;
factorization is not inferred from the two group orders.
