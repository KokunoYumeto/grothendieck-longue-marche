# Root audit of the odd-abelian extension of the dihedral family

**PASS for the complete structural proof, conditional on the now fully audited A70.** Read the entire notes/fgh_dihedral_abelian_extension_draft.tex, SHA-256 `e1eb0ad55f805e94e77d70b10e2eed8823edaf73f5acae4683e9bd6aaa5c45ae`. This audit follows checkpoint14 capture; the candidate remains unregistered until the scheduled save releases the canonical freeze.

## Exact factorization and connectedness

Every subgroup of a finite direct product of coprime orders splits: powers of each element isolate its two coordinates. Applying this to the quotient kernel and covering subgroup proves the actual closure and intermediate factorization. An abelian quotient kills the peripheral commutator, so the odd factor extends over the proper elliptic curve. Choosing a point above the origin after a finite extension makes it an actual odd-degree isogeny.

The two-power normal closure and the odd Galois isogeny extension are linearly disjoint over the base function field. The compositum is therefore a field, and the normalization of the actual fibre product is the specified connected cover. Its removed set consists of exactly the pairs of dihedral cusps and isogeny-kernel points. The genus-one case stays genus one under this unramified pullback and is covered by A40.

## Proper model and actual map

For higher genus, A70 supplies a compact-type marked model of Z with rational companions at all cusps. The isogenous E' has good reduction once E does. The extended odd-degree isogeny between good elliptic schemes is finite etale, since its finite-flat kernel has order prime to the residue characteristic two.

Root freshly opened and read Dupuy–Rabinoff, A rigid analytic proof that the Abel–Jacobi map extends to compact-type models, Theorem1.1 and Proposition3.2, https://arxiv.org/pdf/1705.03034 , especially turn1169view1. The morphism extends across the nodes and permits rational components; the stronger closed-immersion assertion is not used. Basing the Abel map at a cusp sent to O, then composing with the extended actual Jacobian homomorphism, extends the original Z-to-E map on the full compact-type model. The fibre product with the etale good isogeny is therefore a genuine semistable model of the connected generic curve. Rational components map constantly, including inserted components separating marks.

## Compact type is supplied independently

The proof correctly retains the risk that an etale cover of a semistable tree of component curves can create graph cycles. It does not derive compact type from the fibre product alone. Instead it applies the nilpotent-cover theorem to the actual total geometric closure, whose group is the direct product of a dihedral two-group and an odd abelian group. The base has good reduction and the sole possible branch section O is etale; generic characteristic zero supplies the theorem's tameness condition.

Root reopened the published workshop collection at https://www.numdam.org/item/RSMUP_2005__113__129_0.pdf and its readable author version https://arxiv.org/pdf/math/0411059 . The exact Theorem6.13 statement was freshly read in turn1170view0: it is for nilpotent G, not only a p-group, and its tame condition concerns the generic characteristic. The conclusion is a tree-like special fibre or potential good Jacobian. No zero-p-rank or stronger marked-fibre conclusion is imported. Taking the actual norm quotient gives potential good reduction of the intermediate Jacobian, so the semistable pullback model has a tree graph after finite extension.

## Lifting every rational companion

The entire rational subtree connecting a selected original cusp to its companion maps to O: each projective-line component maps constantly to the good elliptic special fibre, the constants agree at nodes, and the cusp section fixes the common value. Over an algebraically closed residue field, the odd etale isogeny's fibre above O is a reduced discrete set. The inverse image of the subtree is literally a disjoint union of copies. The copy selected by the chosen cusp also contains a mark above the distinct original companion; prime-to-two kernel sections have distinct reductions. The two marked generic points remain distinct because they have different images on Z.

Stabilization can contract rational components but cannot insert positive genus into that path. The independently proved global tree condition makes the path the unique joining path required by A42. Thus the argument works for every selected cusp at every coefficient prime. A59 gives normalizers for the nilpotent closure. Finite field descent and base-point comparisons retain exactly the inner-conjugacy convention verified in A70.

No two-rank assertion is needed for the new pullback Jacobian. This proof does not extend to a second nonabelian Sylow factor. Its genuinely structural arguments require no new finite illustrative computation; the actual map, group, model and divisor comparisons are all supplied.
