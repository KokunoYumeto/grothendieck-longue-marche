# Effective configuration-cover recognition — proof work retained before checkpoint08

These are new proof notes, not an integrated theorem or a completed pentagon census. The ordinary source is the exact configuration space X and action in `tower_configuration_fixed_locus.tex` (A.4.46). Root requested preservation before the checkpoint08 QA. No integrated fragment is edited.

## 1. Explicit cohomology killing for an iterated free extension

All cohomology in this note has coefficients F3. Let G have an iterated Fadell–Neuwirth extension of length l whose free kernel ranks are at most r, with r≥2. The actual configuration group K0 has l=8 and ranks2,3,...,9. A subgroup U of index d has the induced extension tower, with every rank at most1+d(r−1), by the actual finite-index free-group Schreier maps.

For a free normal kernel F of rank s, put N=F′F³ and Q1=F/(N′N³). The regular graph cover gives

|Q1|=3^{s+1+3^s(s−1)}, and Z(Q1)→F/N has trivial image.

Every overgroup G in which F is normal acts on Q1 by actual conjugation, because the kernel is characteristic in F. The kernel J of G→Aut(Q1) therefore has J∩F⊂N: an element of F acting trivially on Q1 has central image in Q1. Its index is at most

A(s)=3^{s(s+1+3^s(s−1))}.

This argument does not require a split extension or a trivial base action on H1(F).

For 1→F→G→B→1, first choose an inductively constructed finite-index B0≤B on which restriction of every positive-degree cohomology class of B is zero. Set G1=π^{-1}(B0)∩J. In the natural map of LHS spectral sequences, the q=1 row is zero because H1(F,F3)→H1(G1∩F,F3) is zero; this is the actual coefficient map and needs no trivial-action assumption. The positive-degree q=0 row is zero because the base image is contained in B0. Consequently the map on each positive total-degree associated graded is zero. Each such total degree has only the two possible filtration pieces q=0,1. Repeat the same construction for G1. The composite restriction to G2 is zero on the actual cohomology in every positive degree.

An explicit uniform index bound is defined recursively by

C(1,r)=3^r;
a=C(l−1,r)A(r);
r1=1+a(r−1);
C(l,r)=a C(l−1,r1) A(r1), for l≥2.

The construction gives actual subgroups and homomorphisms. To replace the resulting subgroup V≤U≤K0 by an H-invariant characteristic cover, use

m=d C(8,1+8d),  U_new=κ_m(K0).

The action of K0 on its cosets modulo V has degree [K0:V]≤m, so κ_m(K0)⊂V. All positive cohomology restrictions from U to U_new remain zero. The characteristic property makes the cover invariant under the actual H action even though the chosen free-group filtration is not H-invariant. Since K0 has44 generators, the index of this new subgroup is at most (m!)^{(m!)^{44}}.

## 2. A literal finite-dimensional equivariant cell model

X is the complement of the diagonals in T^{16}, with coordinates z_h=(z_{h,1},z_{h,2}) for h≠0 and z_0=0. The H action (a·z)_h=z_{h+a}−z_a is integral linear. Use the periodic rational hyperplane arrangement

3(z_{h,j}−z_{k,j})=integer, for unordered h≠k in H and j=1,2.

There are72 normal directions. The arrangement is H-invariant and Z^{16}-periodic, includes the coordinate grid, and makes every removed diagonal a union of cells. Each fundamental cube meets at most504 of these hyperplanes (the seven possible integer values from−3 to3 suffice). The convex sign-pattern cells give a finite H-invariant polyhedral model after quotienting by Z^{16}; further barycentric subdivision removes cell inversions. The grid fixed points are vertices. The complement of the diagonal subcomplex deformation retracts equivariantly onto the full barycentric subcomplex of vertices corresponding to cells not contained in that subcomplex: delete the other barycentric coordinates and renormalize. This gives a finite H-CW model of dimension at most16, with all actual inclusion and covering maps.

Every finite cover is the actual cell cover specified by its subgroup of K0. Choose the coset-one lift of the grid basepoint. H-invariant kernels give the unique H action fixing this lift. A chain of characteristic refinements gives literal cellular covering maps, preserving the chosen fixed points. Thus the cochains in the next step are finite-dimensional in each of the17 vertical degrees; they are not unspecified completed cochains.

## 3. Cyclic Smith map argument — written for independent review

For a cellular C3 action and a chosen fixed basepoint, take cellular cochains relative to that point. Use the complete two-periodic resolution of the trivial F3[C3]-module, with alternating differentials1−g and1+g+g², and form its Tate hypercohomology with those bounded cochains. Filter by the vertical cochain degree. The spectral sequence has E2^{s,t}=TateH^s(C3,H^t(Y,*;F3)), with0≤t≤16. A map zero on relative ordinary cohomology is zero on E2, and hence strictly raises the induced finite vertical filtration on each total-degree abutment. Seventeen consecutive such maps give zero on Tate hypercohomology.

Restriction from Y to its C3-fixed subcomplex is an isomorphism on Tate hypercohomology. The relative cellular cochains for the pair(Y,Y^{C3}) are sums of free orbit modules after subdivision, so their Tate hypercohomology is zero. On the fixed subcomplex both resolution differentials are zero, since the action is trivial and3=0. Its Tate hypercohomology is therefore the direct sum of its ordinary relative cohomology groups in the corresponding total degrees. A zero Tate map implies a zero ordinary cohomology map on the fixed subcomplex.

Apply this first to one actual normal C3 subgroup A<H. Blocks of17 cohomology-killing covers give zero relative cohomology maps on the A-fixed subcomplexes. Apply the same argument to H/A acting on these subcomplexes, still of dimension at most16. After17 such blocks, i.e.289 covers, the induced map on H^0 of the H-fixed sets relative to the chosen basepoint is zero.

Every fixed set here is discrete, since its covering projection lands in the48-point set X^H. A zero relative-H0 pullback means that every fixed point in the top cover maps to the chosen fixed point of the bottom cover: the characteristic function of any other bottom fixed point would otherwise have nonzero pullback. Thus, for an initial H-stable normal U⊂K0 and the resulting characteristic V⊂U, this proves the exact finite centralizer projection

image(C_{(K0/V)⋊H}(H)∩(K0/V) → K0/U)=1.

This argument uses the two cyclic stages explicitly; it does not apply a whole-H localization statement that ignores proper isotropy. The horizontal resolution remains two-periodic throughout. Its vertical filtration has17 rows, so the count does not discard the second augmentation differential. Independent review is still required before assigning an integrated result number.

## 4. Retaining this K0 quotient in an actual finite mapping-class quotient

Let V be characteristic in K0. The whole ordinary mixed group M=Γ1,[9] normalizes K0 and V, so conjugation gives an actual map

M→Aut(⊕_{i=0}^8 H^i(V,F3)).

Its restriction to K0 factors through K0/V and is faithful. Indeed the regular cover X_V has Euler characteristic [K0:V]·40320, since the eight free factors have Euler characteristics−1,...,−8. A nonidentity deck transformation has Lefschetz number zero on the cellular cover, whereas the identity has that nonzero Euler characteristic. Thus the total action on rational cohomology is faithful. Every such integral cohomology action on the free parts has finite order. If its modulo-three cohomology action were identity, the induced matrices on the free parts modulo three would be identity; the torsion-free principal-congruence argument from DR.6 would make all rational actions identity, a contradiction. This proves faithfulness without assuming H1 alone detects the deck group.

The cohomology space is finite. The free-tower spectral sequence bounds its total dimension by (2+8[K0:V])^8. Therefore the actual mapping-class image has order at most3^{((2+8[K0:V])^8)^2}. Joining it with the specified lower quotient and the label permutation retains the actual subgroup (K0/V)⋊H, with all maps induced by the original group. This supplies the ambient finite homomorphism needed by the preceding centralizer statement; no arbitrary cochain automorphism is substituted for a geometric image.

## 5. Remaining comparison and fusion scope

For a finite normalizer element whose lower QL comparison gives label-linear action equal to its integral compact period modulo three, an actual affine torus map with that integral period has the same labels. Their quotient lies in K0. If both normalize H with the same label action, the quotient centralizes H at the retained finite level, so the proposed recognition refinement kills its prescribed lower image. This is the route from the exact centralizer assertion to d=j0 on the lower finite normalizer.

A full finite fusion result for arbitrary competing labelled H copies remains to be proved. The centralizer argument above uses the canonical H action fixing the grid lift. A competing finite complement acts on the finite covers but need not have a chosen fixed lift; nonemptiness and actual conjugator recovery must be retained in a separate argument. No completion of A.4 or finite shadow census is inferred here.
