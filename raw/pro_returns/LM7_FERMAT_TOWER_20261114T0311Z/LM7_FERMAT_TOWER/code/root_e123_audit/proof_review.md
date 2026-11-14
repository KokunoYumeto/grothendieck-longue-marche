# Root review of the frozen E.123 proof and certificates

**Verdict: PASS for the stated positional factor, its actual class and unit maps, its coherent divisor image, and the displayed family of H-section classes.**

Reviewed proof: `research_e123/sections/E_fiftythree_positional_stable.tex`, SHA-256 `70a7e93c7a7466069c375505991bb9a273e2c7bebf95164e2734a17a3c2908a4`.
Frozen manifest: SHA-256 `f375db968bbce03f11ca1ea434a9c52f7998cc87a6426ea69e9183909336224a`.
The root has read the entire final statement and proof, all eight final mathematical programs, the complete portable replay driver, and the source-evidence record. The uniform finite-node argument and the explicit three-primary projection are included in the reviewed final text. This review is additional to the author's review; a separate third-agent review is not claimed here.

## Actual class-field comparison

The inclusions in (E123.14) follow in both directions from unramifiedness and splitting at S. The maximal abelian intermediate field is therefore the stated S-Hilbert three-class field of L_d. For the actual extension with abelian kernel A_d and cyclic quotient, commuting a lift of the quotient generator with A_d gives exactly (h-1)A_d. Its abelianization yields (E123.15), with the left map identified with ideal norm through the Frobenius square. Thus the known horizontal coinvariants give the order 81 at every level.

The intersection with L_(d+1) is L_d because the latter cubic is ramified at the S-primes and the class field is S-split. A prescribed class-field Frobenius extends with identity on L_(d+1); Chebotarev supplies a prime whose relative residue degree is one. Its norm represents the prescribed class. Equal finite orders then prove that the actual norm is an isomorphism. The equalities for sigma_d and j_d follow from this map and the trace identity. The horizontal and vertical squares use the actual linearly disjoint fields, including their residue-degree weights. The proof consequently transports the full E.121 matrices and their Artin convention.

## Unit characters, defects, and completion

The local equation with a_1 gives the literal completion Q_3(mu_27). The displayed global roots of unity follow from the horizontal degree and E.122. The witness w is checked in its rational coefficient ring, by full polynomial norm, and by the separate resultant computation. Its denominator and absolute norm prove S-support; the actual residue gives the positive local character. The norm of beta_d down to beta_2 and the cup-product projection formula preserve this character at every higher level. The cyclic Hasse norm theorem then identifies the full field-norm obstruction.

The divisor construction in (E123.20) is well defined: Hilbert 90 accounts for changes of x, and the invariant outside-S divisors are the extended base divisors because the extension is unramified there. Conversely an invariant ideal class supplies the required principal correction. This proves the map and inverse onto the ambiguous-class quotient. Its prime-to-three part vanishes under the trace identity. The vertical quotient C_2/3C_2, the horizontal invariant quotient, and the nonzero witness character give the stated unit quotients. Included cubes are unit norms, so the elementary-abelian quotient and the coordinate carries are justified. Completion is taken on finitely generated unit groups; diagonalizing the integer map and retaining its actual roots of unity proves the displayed kernel ranks and torsion.

## Literal pivot ideals and the entire three-primary presentation

The lower principal corrections retain their full ideals and positive Artin columns. The E.119 lattice sends their idelic coordinates to (4,1) and (4,0). The stated genus map is invertible modulo three, so these are actual generators of the already proved C_9^2. Their residues select the surviving prime branches.

The seven upper ideal equalities define a homomorphism from the order-81 relation quotient. Its image contains these two actual generators. This proves the complete three-primary presentation without a correctness assumption about the proposed upper BNF group. The matrices P and Q give the inverse maps modulo the actual relation lattice. The supplied integral basis has the stated discriminant and the local maximality proof; the independent nf-only verifier also returns empty nfcertify obstruction lists for both fields.

For an arbitrary surviving prime, the terminating ideal-relation enumeration includes m congruent to 1 modulo 9. Such an m kills its prime-to-three class component and acts as the identity on C_2. This supplies the required three-primary projection rather than leaving the uncomputed class-group component implicit.

## Coherent divisors and topology

The affine Frobenius calculation is uniform on each finite residue ball away from its fixed point. The valuation t of x-x_0 is constant after a finite refinement, and the orbit weight has three-part 3^max(0,m-s-t). Therefore the image of all sufficiently deep descendants is divisible by any prescribed power of three. This proves vanishing of a coherent mass at that finite node, including the sum over all its descendants. The nested fixed nodes retain precisely the unique fixed branch. The residue calculation then gives exactly the prime set P in (E123.6).

At each field level the principal outside-S divisor group is free. Its intrinsic power filtration and the induced divisor filtration are cofinal, with the two-step bound supplied by the exponent-nine three-class group. Its completed image is consequently the kernel of the class map. The coherent lifting argument uses nonempty compact unit torsors and the finite intersection property: every finite chain is obtained by taking norms from its highest level. Surjectivity of individual unit norms is not required for this argument.

The two literal prime classes prove surjectivity of c. Formula (E123.9) and its inverse retain the carries divided by nine. Restricted support modulo every power of three makes the sums converge. Arbitrary coherent lifts of these basis divisors give the section in (E123.11); the same restricted support proves convergence in every field-level power topology and continuity of both maps. The change of lifts is displayed as an actual coordinate change.

The coherent unit group is compact, metrizable, and torsion-free, since the only component torsion is mu_3 and every vertical norm cubes it. Its countable discrete dual is divisible. The selected chains of finite characters and their finite-equation inverse construct the product coordinates. The occurrence of infinitely many coordinates follows by restricting Kato's actual coherent universal-norm system over L_d to the later positional fields. The one prime above three gives rank 3^d in the d-th projection, and these ranks are unbounded. The use of Kato is confined to this finite-index rank consequence.

## Actual rational norm and section map

The residue degrees one and two give exactly the exponents in (E123.12). The root family beta_d is norm compatible and supplies (nu_3,nu_53)=(0,2). The E.46 positional-factor comparison retains the other factors and the original total-norm cube condition in (E123.26). Cubing the selected section produces (E123.13); its inverse is the outside-S divisor divided by three. Its closed image has unit coordinate one and divisor subgroup 3D. The remaining valuation functionals, other factors, and intrinsic lifts are retained with their explicit scope.

## Fresh replay and exact comparison

The retained `replay.py/.out/.err` executed successfully. `replay_audit.json` records:

- all 304 owned files and all eight immutable inputs checked before and after;
- all eight final mathematical stages executed in a fresh copied tree;
- complete stdout and stderr comparisons, both complete JSON comparisons, and byte identity of the generated standalone GP source;
- equality of the entire four-component and thirteen-component PARI GEN objects;
- all nine standalone ideal equalities and both unconditional maximal-order checks;
- no excluded mathematical fields and no modification of the frozen author sources.

The binary containers have distinct serialization bytes in the fresh process; both decoded objects are compared in full. The retained audit states this explicitly and gives both container hashes. The independent verifier reconstructs the literal fields, ideals, and rational polynomials without reading a BNF object.

## Primary-source check

The root reopened Milne, *Class Field Theory*, v4.03, at the official PDF, including III.3.1 and its restriction/corestriction proof; V.3.3 and its norm/Frobenius proof; VIII.3.1 and its injectivity proof; and VIII.7.4. The source record also retains the earlier checks of the class-field existence and S-unit statements. III.3.2's absent proof is explicitly recorded and supplies no claimed proof text. Root retrievals: `turn1146view0`, `turn1147view0`–`turn1147view3`, and `turn1148view0`–`turn1148view3`.

The root also reopened Kato's original *Universal Norms of p-Units in Some Non-Commutative Galois Extensions*, at its definition on printed page 551 and Theorem 1.1(2) on page 552. The definition uses the image of an inverse limit of actual norm-compatible p-unit systems, exactly the system restricted in the proof. Its proof passages were already read in the retained E.69/E.110 work. Fresh root retrieval: `turn1146view1`. Official URLs:

- https://www.jmilne.org/math/CourseNotes/CFT.pdf
- https://ems.press/content/book-chapter-files/27477

No claim about the still-open original E.23 beyond the precise displayed positional result follows from this review.
