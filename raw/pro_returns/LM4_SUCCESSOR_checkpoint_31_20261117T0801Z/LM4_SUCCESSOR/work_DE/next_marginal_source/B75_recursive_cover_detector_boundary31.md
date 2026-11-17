# The actual B75 recursive-cover heads cannot be cofinal

Cycle31 research. This is an exact boundary on one proposed source detector, not a conclusion about the actual icosahedral residual group. It uses the complete marked B73–B75 input, which was reread in full. No new finite census or contraction theorem is invoked.

## 1. Actual source and the degree-five map

Use B74's full dihedral centralizer G=C2*Z, with source parameter

    q=(u^5+1)^2/u^5.

The Galois cover from the u sphere has transformations u to zeta u and u to1/u, hence actual deck group D5 of order10. B75's V stabilizer G_V has index5 in G, and the intermediate parameter

    w=4((u+1)/(u-1))^2

is the quotient by u to1/u. Its map to the q sphere is the exact degree-five rational function

    F(w)=4 w(w²+40w+80)²/(w-4)^5.

Therefore its five-sheet monodromy is exactly the faithful action of D5 on its five reflection cosets. This is a consequence of the actual intermediate covering, not a numerical guess from branch cycles. The verified identity

    F(w)-4=16(5w²+40w+16)²/(w-4)^5

shows that the branch values are among0,4,infinity; the total ramification is8, so no further branch value is omitted. Their forward images are0, infinity and4. Thus every iterate F^n restricts to an ordinary covering away from the same postcritical set. These are the recursive-cover towers considered below. The cone relation in G is compatible with these actions because the0-preimages have local degree at most2, and a critical point over0 cannot subsequently recur as another critical point along a backward branch. Alternatively one can work first with the punctured-sphere free group and then its actual orbifold quotient.

## 2. Uniform finite-group restriction for every level

The monodromy of a composition of finite covers preserves its blocks of intermediate sheets. Its action on each block is a subgroup of the monodromy of that stage, transported by a path. Inductively the monodromy of F^n is a subgroup of the n-fold permutational wreath product of D5. This does not assert equality with that wreath product. It proves that every such finite monodromy group has order involving only the primes2 and5.

Restriction to G_V, subgroups, quotients, finite products and subdirect products preserve this prime set. Consequently the kernel T of any finite collection of these actual recursive permutation actions on G_V has index2^a5^b for nonnegative integers a,b. The same conclusion holds for their finite-index stabilizers: the index divides an integer with only those primes.

Now use B75's actual common based presentation

    G_V=<e,a0,c1,c2 | e²=1>.

The assignment a0 to1 in C3 and e,c1,c2 to0 is a literal epimorphism. Let U0 be its kernel, of index3. No such T can be contained in U0, because containment would force

    [G_V:T]=[G_V:U0][U0:T]

and hence divisibility by3. This contradicts its prime set. The same argument applies to every open subgroup in the topology generated solely by all recursive-cover kernels. Thus these heads are not cofinal for the full profinite topology of the actual source. No finite-depth observation is involved.

## 3. Exact implication for the original criterion

B75.6 asks, for every finite-index normal U0 of G_V, for a characteristic finite-index N0 in the ACTUAL Birman group N=B4(S0,4) such that delta(g) in N0 implies g in U0. The proof above does not rule out such N0 and gives no nonidentity element of the residual completed zero set. It only rules out replacing that unrestricted condition by the topology supplied solely by the degree-five recursive-cover permutation heads, already for the explicit C3 source quotient.

In particular a contraction statement about the discrete rational virtual endomorphism would not by itself repair the full finite-target quantifier. Nor does the local one-family corrected-inner-action theorem B153 supply an original B75 detector: its faithful even-source basis lies in a specifically retained F(r,w), whereas B75 uses the different actual G_V source and its four-moving-point Birman kernel. The original forgetting projection kills c1,c2. Any proposed faithful free quotient or peripheral normalization must retain their complete marked action and separate arbitrary finite source targets.

The exact unresolved construction remains an actual homomorphism or compatible finite-target family for the original marked source/Birman extension which separates the whole complement of each prescribed U0. Full source embeddings, pointwise separation of individual delta values, and the recursive permutation tower do not supply it.

## Evidence and category boundary

Inputs are work_DE/B_birman_cocycle.tex and work_DE/next_common_involution/full_dihedral_centralizer.md, with the original complete rational/permutation certificate work_DE/next_common_involution/Birman_cocycle_data.json. No new producer or external theorem was needed for the wreath inclusion or index obstruction. The independently audited arbitrary-finite centralizer closure claims remain subject to records/centralizer_dependency_audit.md and B1/B39; the recent primary search returned that same already-known unresolved route and is not used here.
