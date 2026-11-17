# Independent review of B.57: finite certificate and filling topology

Reviewed by the D/E agent on 16 November 2026, 03:20–03:27 UTC. Scope requested by root: the original subgroup J and its three fillings; the twelve peripheral images; the three-color order-two filling; the regular sixty-element tripod orbit; and the distinct simple-quotient kernels. The central-extension/lifting argument is being audited separately by root and the A agent and is outside this review.

**Conclusion:** the finite and topological ingredients in the assigned scope are valid. The finite certificate was rerun successfully. An independent certificate using the original modular quotient generators checks all five conjugate colorings and the regular tripod orbit. No amendment to B.57 is required for these ingredients. This conclusion does not independently certify the existence of the full peripheral lift, the Schur-multiplier input, or the final torsion-free procyclic conclusion.

## 1. Files inspected and actual computations

The reviewed source is `work_CE/B_common_kernel_counterexample.tex`, with dependencies `sections/b_resolvents.tex`, `sections/b_nonidentity.tex`, and the cover signatures in `sections/b_geometry.tex`. The original certificate is `work_CE/code/check_common_kernel_alt9.py`. It was read in full and rerun, giving the same output as `work_CE/code/check_common_kernel_alt9.out`.

The independent program is `work_DE/check_B57_cusp_topology.py`; its actual stdout is `work_DE/check_B57_cusp_topology.out` and its exact permutations/partitions are `work_DE/check_B57_cusp_topology.json`. It uses standard-library integer permutations and reduced normal forms in C3*C3. It does not import the original B.57 certificate. Its generators are the original quotient generators of B.55:

\[
s=(0\,1)(2\,3),\qquad r=(0\,2\,4),\qquad\tau=sr.
\]

The generated group has order 60, its elements are even, and the three orders are 2, 3, 5. All five point-stabilizer colorings and all sixty tripod support patterns pass.

## 2. The original J and the width-one peripheral maps

Discretely, B=C2*C3 is the oriented (2,3,infinity) orbifold group and K is the kernel of its prescribed quotient onto A5. The factors inject into A5, so K is torsion-free. Its index is 60, and its cusps are the twelve cosets A5/<tau>, each of width five. Its Euler characteristic is 60(-1/6)=-10; with twelve cusps, this gives genus zero and free rank eleven.

For any point stabilizer T=A4 in the natural five-letter action, J is its preimage in B. The (2,3,infinity) permutations in the degree-five cover have types 2^2*1, 3*1^2, and 5. Hence J has signature (0;2,3,3;infinity), exactly one cusp with meridian conjugate to tau^5, and presentation C2*C3*C3. This is the same geometrically marked J used by B.53, not an abstract group of coincidentally equal rank.

The cover K≤J has degree twelve. Its single J cusp meridian lies in K because tau^5 maps to 1 in A5. Thus every K cusp has relative width one. Equivalently, T acts freely and transitively on A5/<tau>, since T intersects every conjugate of C5 trivially. The twelve K meridians are conjugates in J of the same first power of its cusp meridian. There is no unnoticed fifth power in the filling maps: the fifth power has already been taken in passing from B to J.

Write a geometrically based presentation J=<u,a,b | u^2=a^3=b^3=1>, with its cusp the product uab or its inverse according to the fixed positive-meridian convention. Its images in A4 satisfy uab=1. Killing a or b leaves C2*C3 and carries this cusp to the first power, possibly consistently inverted, of the remaining target cusp. The normal closure of either nonidentity order-three factor in A4 is all A4. Therefore the image of K under either filling is the whole C2*C3. This argument proves equality of images, not merely density. On profinite completions, the images are compact and hence closed, and the same quotient argument gives the stated full profinite target.

Consequently all twelve meridians are conjugates in that full target of one target cusp meridian. If a proposed factor map kills even one of them, it kills the target cusp. The quotient of C2*C3 by the normal closure of the product cusp is trivial: the product relation identifies the order-two and order-three generators up to inverse, forcing both to have order dividing gcd(2,3)=1. This validates the order-three filling contradiction in B.57.

## 3. The order-two filling and its three four-element blocks

Killing u gives D2=C3*C3. The normal closure of u in A4 is V4, so the exact image of K is

\[
P_2=\ker(D_2\longrightarrow A_4/V_4=C_3),\qquad a\mapsto1,\quad b\mapsto-1.
\]

The two surviving finite factors inject into C3, so P2 is torsion-free. The index-three cover has Euler characteristic 3(-1/3)=-1. Its cusp ab is already in the kernel; there are three cusps, all of width one. Therefore the cover is the three-punctured sphere and P2 is free of rank two. After completion it is the full free profinite group of rank two. Finite-index subgroup topology introduces no gap here.

There is also a direct normal-form check of the three meridians. Set c=ab and use the coset representatives 1,a,a^2. Then

\[
c_0=ab,\qquad c_1=aca^{-1}=a^2ba^2,\qquad c_2=a^2ca^{-2}=ba,
\qquad c_2c_1c_0=1.
\]

Schreier rewriting gives these generators and that single peripheral relation. In particular they generate P2, with c0 and c2 free generators. The independent program checks each displayed reduced-word identity. All three are literal first-power conjugates of c, so there is no power loss that could make a killed meridian inconclusive in a finite quotient.

The twelve source cusps correspond to T=A4, while the three target cusp classes correspond to T/V4. Each target color has four source cusps. The independent program constructs the five actual V4 actions on the original twelve cusp cosets and obtains three disjoint blocks of four for every point stabilizer. This supplies the original-label check behind the abstract A4/V4 argument. A quotient supported on only three source cusps kills at least one source meridian in every four-element block. A factorization through P2 would thus kill all three peripheral generators, so it would be trivial. This validates the order-two filling contradiction for all five conjugates.

## 4. A9 and the sixty distinct tripod kernels

The original certificate uses the stated rightmost-first multiplication convention and enumerates the semigroup generated by X,Y; finiteness makes this a subgroup. It finds precisely 181440 even permutations, which is |A9|. Therefore it proves <X,Y>=A9 without a black-box order identification. Direct cycle decomposition verifies that X,Y,(XY)^(-1) all have type (7,1,1).

For each of these three elements, the transposition of its two fixed letters is odd and centralizes it. Multiplying that transposition by the chosen outer transposition gives the explicit even conjugator printed by the program. The centralizer in S9 of X has exactly fourteen elements, namely the seven powers of X times the optional transposition of its two fixed letters. Testing those fourteen against Y leaves only the identity. Thus conjugation by the odd transposition is outer on A9, while preserving each of the three indicated peripheral conjugacy classes. The program does not calculate a Schur multiplier and correctly says so.

The geometric twelve-vertex action is A5/C5. Its six antipodal pairs are the fibers of A5/C5→A5/D5. A three-subset consisting of one antipodal pair and one further vertex has a unique antipodal pair. Its stabilizer lies in D5 and must fix the further vertex. No nonidentity element of D5 fixes any of the other ten vertices: a stabilizer would lie in an intersection with a conjugate C5, whose nonidentity possibility is the original C5, and that group fixes only the two poles. Thus D5 acts freely on the other ten vertices and the tripod stabilizer is trivial. The orbit consequently has sixty elements.

Both the original certificate and the independent original-label certificate verify these counts. The latter checks all sixty tripods against every one of the fifteen four-element color blocks. Every block contains a killed cusp, as required above.

The tripod quotient kills nine cusp conjugacy classes and sends each of the other three to a nonidentity seven-cycle. Its sixty conjugates therefore have sixty distinct supports. Distinct supports imply distinct kernels: choose a cusp present in one support and absent in another; any meridian for that cusp lies in exactly one of the two kernels. No assumption that distinct epimorphisms necessarily have distinct kernels is being made.

## 5. The image/intersection and full-product steps

Each of the fifteen filling kernels is normal in K. Its image under q0 is therefore normal in the nonabelian simple group A9. If that image were trivial, q0 would factor through the corresponding filled image. Sections 2–3 rule this out, so every filling kernel maps onto A9. Closed iterated commutators of the fifteen kernels lie in their intersection V, and their q0-images remain A9 because A9 is perfect. Thus q0(V)=A9 is valid. This is not an interchange of intersection and image.

For the induced sixty-coordinate map, each coordinate kernel is a maximal normal subgroup of K with quotient A9. For a fixed coordinate j, any other coordinate kernel maps onto A9 in coordinate j: otherwise it is contained in the jth kernel and, since both have the same finite index, equals it, contradicting the support test. Iterated commutators of all the other kernels therefore produce the complete jth factor while killing all other coordinates. Repeating this for j=1,...,60 proves that the image of K is A9^60. Surjectivity to A5 then makes the complete induced image the regular wreath product. The formula in B.57 is the standard right-coordinate cocycle formula and is consistent with its stated right action.

Normality of V makes q(V) normal in that full wreath product, in particular in its base A9^60. It projects onto one factor by q0(V)=A9 and onto all factors by transitivity. A normal subgroup of a product of nonabelian simple groups is a product of factors (or prove this by commuting with one factor at a time). Hence q(V)=A9^60. This also validates the claimed fiber-product description of the joint quotient: one first lifts a point of C and then corrects its finite base coordinate by an element of V.

## 6. Exact limits of this review

This audit verifies the finite certificates and the topological/image ingredients through the full-base and joint-quotient construction. It does not independently verify the ATLAS multiplier H2(A9,Z)=C2, the extension of the diagonal automorphism through the actual central refinement, the use of A.3/A.34 to lift it to the full peripheral source, or the R1 torsion-freeness implication at the end. Those are separate logical inputs under independent review by the assigned agents. It also supplies no information about whether the original completed A5 centralizer K is trivial. B.57 concerns the strict insufficiency of the three resolvent tests, with the corrected C3 amalgam C3 target of the third map.
