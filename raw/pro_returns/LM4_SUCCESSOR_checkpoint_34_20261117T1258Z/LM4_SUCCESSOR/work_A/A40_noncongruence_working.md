# A.40 working proof: a compatible noncongruence involution refinement

**Status:** independently reviewed by the parent and CE agents and incorporated as formal A.40--A.41. This file preserves the working proof; the formal source is authoritative. The conclusion is an involution in an actual quotient image of the full group, not a full involution.

## Statement and retained data

Write Pi=C2 amalg C3, with generators s,r and tau=sr. Let K=ker(Pi -> A5), let R=R_nil(K_cong), and put C=Pi/R. A.34 proves R=[R,Pi]. A.31--A.33 provide an actual continuous automorphism beta_C of C with the following properties:

1. beta_C has order two, sends tau_C literally to tau_C^(-1), and is the image of a full negative GT0 element.
2. Its image on A5 agrees with genuine standard complex conjugation c.
3. Its actual outer image on the level-twelve relative quotient has Delta=1.
4. The two literal C-frames can be retained from A.33.

Let c_C be genuine standard conjugation on C, and put h_C=beta_C c_C, with rightmost map applied first. Then h_C acts identically on A5, fixes tau_C literally, and preserves the positive s/r conjugacy classes. It has the literal C-frames inherited from the chosen full positive element in A.33.

There is a finite GT0-invariant quotient q:Pi -> Q=M semidirect A5, with M a nonempty finite product of copies of A9, such that:

* A5 acts freely and regularly on each orbit of the simple factors;
* q(R)=M;
* for N=R intersect ker(q), the actual quotient D=Pi/N is Q fiber-product-over-A5 C;
* a full h in H exists whose actual action on D is (id_Q,h_C), retaining the specified C-frames;
* consequently a=h c is a full negative element with Delta(a)=1 whose actual automorphism on D is (c_Q,beta_C), of order two.

The entire relative principal-congruence tower is a quotient of D, while D has an A9 composition factor. Thus this is a genuine noncongruence refinement of A.31. It remains a particular GT0-invariant quotient; no assertion is made that it is a characteristic quotient for all automorphisms of the free group, or that a itself has order two.

## The finite invariant quotient

The twelve cusps of K are the twelve A5/C5 cosets. Their antipodal involution is the unique nontrivial element of N_A5(C5)/C5. Consider all kernels of epimorphisms K -> A9 which factor through a three-cusp filling, where the retained three-subset consists of one antipodal pair and one further cusp, and for which each retained positive cusp maps to a seven-cycle. There are finitely many such kernels because K is finitely generated and A9 is finite.

This family is nonempty by B.57's exact triple X=(1234567), Y=(1254389), Z=(XY)^(-1). All three are seven-cycles and generate A9. The certificate in work_CE/code/check_common_kernel_alt9.py verifies the claim by full enumeration.

The family is invariant under the full normalized GT0 action. The action preserves K by the congruence covariance used in A.31, permutes its cusp classes, and preserves the antipodal relation: the latter is intrinsically N_A5(C5)/C5. It replaces each positive meridian by a conjugate of a common unit power. A unit power of a seven-cycle is again a seven-cycle. Precomposition therefore permutes exactly the defined epimorphism kernels.

The A5-stabilizer of each kernel is trivial. Indeed it must preserve its nonzero cusp support, and a triple consisting of an antipodal pair and a third vertex has trivial A5-stabilizer, as proved in B.57. Thus every A5-orbit of kernels has sixty members.

Choose one epimorphism for each orbit of kernels, induce it from K to Pi by the regular wreath-product construction of B.57, and take the product of these maps over their common A5 quotient. The result is q:Pi -> M semidirect A5, with one A9 coordinate for each distinct kernel. The restriction to K has full product image. The elementary proof is the same commutator argument as B.57: in a chosen coordinate, every other distinct maximal normal kernel maps onto that simple factor; their iterated commutator gives that factor alone. Hence all coordinates occur independently. The image of Pi then contains M and surjects onto A5, so is the full semidirect product. The kernel of q is the intersection of the defined kernel family, and is consequently GT0-invariant.

Every coordinate sends R onto A9. Otherwise that epimorphism would factor through K/R, an open **normal** subgroup of C, making A9 a composition factor of a finite quotient of C. A.31 proves that the nonabelian composition factors of finite quotients of C are only PSL2(F_p), for primes p. A9 is not one of these, by the order calculation in A.35. Since q(R) is normal in M and projects onto every simple factor, q(R)=M.

It follows directly, without an image/intersection interchange, that

    D=Pi/(R intersect ker q) = Q x_(A5) C = M semidirect C.

Indeed lift a specified C-coordinate to Pi, then correct its finite M-coordinate by an element of R. The action of C on M factors through its given A5 quotient.

## The actual central refinement splits over C

Set E#=Pi/[N,Pi] and Z=N/[N,Pi]. This is the actual central refinement required by A.3, with E#/Z=D. Let R#=R/[N,Pi], the full preimage of M. It is a central extension of the finite perfect group M.

The canonical image M# of the universal central cover (2.A9)^t in R# is finite, perfect, normal in E#, and surjects onto M. Here t is the number of simple factors. The universal-cover input H2(A9,Z)=C2 is the same primary ATLAS input already used and cited in B.57. The canonical image is preserved by every automorphism of R# induced from E#, by uniqueness of lifts from a perfect group. Since the extension is central, R#=M# Z.

Now R=[R,Pi] implies

    R#=[R#,E#]=[M# Z,E#] <= M#.

Therefore R#=M#. In particular Z is finite, central, and contained in M#.

Let C# be the preimage in E# of the specified pure C-section of D=M semidirect C. Its map onto C has central kernel Z. The actual images of s and r in D are M-conjugate to the pure C-elements s_C and r_C. To verify this, work in each regular wreath orbit. The permutation of s has only two-cycles, and the permutation of r has only three-cycles. The base cycle products are all one because the actual elements have orders two and three. The coordinate conjugator equations therefore remove the entire base component. This is exactly the regular-wreath calculation used in B.57.

Lift these M-conjugators to M#. Conjugating the actual s and r in E# gives elements S,R_3 of C# of orders dividing two and three, respectively, projecting to the named s_C,r_C. The universal property of Pi gives a homomorphism j:Pi -> C# with j(s)=S and j(r)=R_3. Its projection to C is the canonical quotient map. Thus j(R) is central. Since R=[R,Pi], it follows that j(R)=1. Hence j factors to a continuous section i:C -> C#.

Consequently

    E# = M# semidirect C.

The action of C on M# factors through A5. Its action on M is the given factor permutation. If an element of C maps trivially to A5, conjugation by its section lift induces the identity on M. An automorphism of the perfect group M# inducing the identity on its central quotient M is the identity: its difference is a homomorphism from M# to the abelian central kernel. Thus the kernel of C -> A5 acts trivially on M#. This also shows that the A5-action is the unique lift of its action on M.

Set Q#=M# semidirect A5. The splitting gives the exact identification

    E# = Q# x_(A5) C.

The actual s and r have images in Q# which are M#-conjugate to the pure permutation elements. Indeed the section i was constructed to contain precisely their chosen M#-conjugates. More generally a different splitting would only introduce a central shift, which would not affect the centralizer surjectivity below. No choice making the cusp component have odd order is needed.

## The positive automorphism on the actual central refinement

Because h_C acts identically on A5, the formula

    psi# = id_(M#) semidirect h_C

defines a continuous automorphism of E#=M# semidirect C. Equivalently it is (id_(Q#),h_C) in the displayed fiber product. It covers psi_D=(id_Q,h_C).

It fixes the **actual** tau in E# literally. Its Q#-coordinate is unchanged, and its C-coordinate tau_C is fixed by h_C. Equality follows in the actual fiber product. This observation avoids any assumption about the order of the finite cusp lift or about a fourth-root character.

For s, write A=q#(s) and let d_s in C be the specified literal conjugator satisfying h_C(s_C)=d_s s_C d_s^(-1). Since h_C acts identically on A5, the image of d_s lies in C_(A5)(bar s). The map

    C_(Q#)(A) -> C_(A5)(bar s)

is onto: A is M#-conjugate to the pure permutation bar s, and every pure permutation centralizing bar s centralizes that element in Q#. Conjugating this section by the same M# element proves surjectivity for A. Choose a centralizing e_s in Q# with the same A5 image as d_s. Then (e_s,d_s) belongs to E# and conjugates s to psi#(s). This retains the specified C-conjugator.

The identical argument applies to r, using its positive h_C-conjugator and the centralizer of bar r. The chosen conjugators are literal elements of the actual central refinement, not of a substitute central cover.

Thus psi# is an automorphism of Pi/[N,Pi], covering psi_D on Pi/N, preserving the three positive peripheral conjugacy classes with specified literal C-frames and fixing tau literally.

## Full ordinary lift and actual involution at D

Apply the closed-normal central-quotient criterion A.3/A.34 to psi#. It gives a full positive peripheral automorphism inducing psi_D and retaining the projected literal conjugators. The full cusp conjugator has image one on D; conjugate the full lift by its inverse, an element of N, to make tau literally fixed. This changes neither its D-action nor its retained C-frames. By the standard modular/GT0 identification, the resulting full element h belongs to H.

Now set a=h c. Because the entire defined kernel family and R are c-invariant, genuine c acts on Q and C. Its Q-action is denoted c_Q. The actual induced map is

    a_D=(c_Q,h_C c_C)=(c_Q,beta_C).

The two coordinates agree on A5, and both square to one. Hence a_D^2=1. It has order exactly two, since its action on the order-three quotient of Pi^ab=C6 is inversion. Its level-twelve outer image is the one retained from A.31, so Delta(a)=1. This also rules out conjugacy to the standard image in the actual GT0 image on D, because Delta factors through that image via its quotient at level twelve.

Nothing in this ordinary lifting argument gives a^2=1 in the full group. In particular it does not claim that the newly chosen finite frames have zero norm, only that the actual automorphism at D has order two and the old full C-frames are retained.

## Optional countable semisimple extension, to be separately reviewed

The proof uses seven-cycles only to exhibit a nonempty invariant A9 family. More generally take all kernels of epimorphisms from the same antipodal-pair tripod fillings onto finite nonabelian simple groups S which are not isomorphic to PSL2(F_p) for a prime p. There is no cycle-type condition. Every retained cusp is automatically nontrivial: if one were killed, a two-cusp quotient would be procyclic and could not surject onto S. The finite families for each fixed S are invariant under GT0, and all A5-orbits are free.

For any finite union of such invariant families, the joint base M is a product of nonabelian finite simple groups, the same full-product and q(R)=M arguments apply, and its universal central cover is finite. The finiteness is the standard finite-perfect-group fact: its kernel is the finite Schur multiplier. The same proof then gives a nonempty closed set of full h in H with prescribed C-action and frames and with identity action on that entire finite joint quotient. For finitely many such requirements, their union is another finite requirement. Compactness of H gives one h satisfying all of them.

The resulting a=h c has order two in the actual image on the inverse limit of C together with all these semisimple tripod quotients. This is still a specifically defined tower. The argument says nothing about finite quotients having nonsimple chief layers that do not split into these regular simple-coordinate blocks, and it does not show cofinality in the full characteristic tower. Those layers retain the norm/H2 obstruction of A.19.

If the optional extension is incorporated, cite a primary source for finiteness of the Schur multiplier of a finite group or give the elementary finite-chain/transfer proof. The fixed A9 result above already has its complete explicit universal-cover input in B.57.
