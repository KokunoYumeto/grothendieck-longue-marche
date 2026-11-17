# Independent complete factored-chain review

The CE circuit and its additional single-G-unit obstruction pass.
Independent producer and genuine output:
`verify_factored_product_tree_chain_independent.py/.out/.err`.
Complete result: `factored_product_tree_chain_independent_review.json`.
No CE producer is imported or executed by this independent verifier.

## Literal input and exact DAG semantics

The verifier starts from the actual paired node(8,0) meridians and
reconstructs their successive images under the signed old word
(6,2,-6,-2), using the six already certified geometric-push/pull arrays.
Their freely reduced commutator is exactly the stored119780-letter
input. The original word has124 letters. Thus the circuit is tied to
the actual geometric row-stabilizer word, not only to an unverified
word supplied to a compression routine.

Every node of the retained and R-word directed acyclic graphs is checked:
the parent is earlier, the signed letter is valid, the length is exactly
one greater, the last letter is not the inverse of the parent's last
letter, and there is a unique node for each parent/letter pair. These
conditions prove that node identifiers are exact canonical freely
reduced words. All common R generators have their actual retained-head
and deleted-slot labels. The counts are331 retained nodes,15903 R-word
nodes, and589 nontrivial common generators.

## Boundary verification without rectangle expansion

For an R_A vertex a, let H(a,v) be the unique oriented A-tree path
from(1,v) to(a,v). A stored term (a,v,j,n) means

 n * path_A(1,a) tensor edge_B(v,vj).

Its boundary is exactly

 n * (H(a,v)-H(a,vj)+edge_B(a,v,j)-edge_B(1,v,j)).

The verifier scans the literal F21 word independently, maintaining the
retained head and its actual beta image, and records its exact A-path
potential changes and B edges. It separately computes the displayed
boundary from every stored term and compares both components. Empty
A-path symbols are deleted because they represent zero. The endpoints
in the retained group and both R factors are all the identity.

The product of the two Cayley trees is contractible and two-dimensional,
so its cellular boundary on finite two-chains is injective. The boundary
comparison therefore identifies the stored circuit with the complete
product-tree chain. It is not merely a boundary consistency test between
two potentially different closed two-chains.

The original small circuit is expanded, and every one of its117
previously audited coefficients agrees. The large circuit is never
expanded. Its exact normal form has33162 terms; a full uncollected
square expansion would contain67823551 rectangles. These numbers are
recomputed from the actual words and the canonical DAG lengths.

## The compressed form is itself an integral basis

For a tree T_A, the boundary map C1(T_A)->ker(C0(T_A)->Z) is an
isomorphism. The root paths path_A(1,a), indexed by nonidentity
vertices a, map to the standard augmentation basis a-1. Hence those
paths form a genuine integral basis of C1(T_A). Tensoring with the
positive B edges gives a genuine integral basis of the product
two-chain group. Thus the collected triples(a,v,j) are a unique
complete-chain normal form, not just a nonunique arithmetic circuit.

An actual element (u,v,t) of G=E semidirect T acts on an A root path by

 path_A(1,a) -> path_A(1,u tau_t(a))-path_A(1,u),

and sends a positive B edge to one positive B edge under the actual
retained relabeling and left translation. Therefore a single signed
G-unit sends a k-term normal form to one with at most2k terms.

This edge assertion uses the actual B94 splitting, not a claim about
general automorphisms of free groups. The Schreier peripheral is
x_(g,i)=g a_i g^-1 in the actual free product T*F(deleted slots).
Consequently t x_(g,i) t^-1=x_(tg,i), literally and with positive
orientation unchanged. On the B factor the common label uses beta
of the retained whisker, so the same calculation gives tau_beta(t).
These are precisely B94.1's multiplication and row-normalization
formulas, and the earlier actual conversion's `act(w,t)` prepends
t to every retained head without changing its signed generator.
Thus the Cayley-tree edge-permutation hypothesis is explicitly
verified in the actual coefficient convention.

The original has42 terms and its image33162 terms, so

  33162 > 2*42

proves that this actual geometric stabilizer image is not a signed
G-unit multiple of the original column.

## Exact limitations

This proves a complete full-chain description and the failure of a
single group-unit multiple. It does not compute the collected support
in the different free G-row basis, prove independence over Z[G],
decide membership in the full64- or128-column block, or evaluate kappa.
An arbitrary group-ring linear combination can have many terms and
is not excluded by the two-times support bound. No further word-depth
or finite-group census is performed.
