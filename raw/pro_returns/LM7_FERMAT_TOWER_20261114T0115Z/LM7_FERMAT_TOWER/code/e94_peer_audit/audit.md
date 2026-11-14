# Independent E.94 proof and map audit

**Verdict: PASS. No mathematical correction requested.**

## Exact scope

I read the complete frozen theorem/proof, the Python verifier, and all three owned GP sources: `e_mu27_local.gp`, `e_mu27_genus.gp`, and `e_mu27_export.gp`. I then copied the Python source and the91-record exact export into a separate audit directory and executed that verifier afresh. The complete JSON is byte-identical to the author certificate, with no JSON field omitted. The verifier-stage stdout is also byte-identical. The author stdout additionally has the six actual GP rebuild PASS lines; this audit did not rerun those six GP stages, and makes no independent BNF/ray reconstruction claim. Root separately performed that full rebuild.

The frozen section SHA256 is `cdcb8f90477f012bb1e5e793857e8b0130bf7ab8f69ef6d17750adce54ab6869`.

## Local characters, inverse cyclotomic convention, and maximality

The local cyclotomic normalization checks with arithmetic Frobenius. At a three-prime the completion of F is Q3(mu9). Norm(xi)=1, Norm(beta1)=17²≡19 mod27, and Norm(1+beta1)=273. The arithmetic local Artin action of a Q3 unit on mu27 uses its inverse. Thus the latter two cyclotomic values are1 and2 in the coordinate eta↦zeta eta: 19^{-1}=10 and (273/3)^{-1}=91^{-1}=19 modulo27. Removing the rational factor3 is justified by the actual Q3 local reciprocity decomposition. The chosen coherent roots and the specific eta coordinate are preserved.

The literal norm family in F_v[Y]/(Y³-xi) has a rank-six image in the seven-dimensional unit quotient modulo cubes. Every spanning column is an actual unit norm, and local norm index3 proves this is the entire kernel. Its annihilating row is fixed by the computed value on beta1, not by an arbitrary sign. The radical row scale is fixed independently by the tame character -log_xi(u^32) at seventeen and global reciprocity. I additionally checked a unit determinant minor in the three unknown wild scaling rows: columns(0,7,12) have determinant -2. Therefore the three wild scales are uniquely determined modulo9; the output(5,5,5,8,5,4) has no remaining normalization freedom.

The radical and cyclotomic characters on units at three are independent: xi has radical value5 and cyclotomic value0, while beta1 has radical value0 and cyclotomic value1. This gives full inertia C9×C3 and proves total ramification there. At seventeen, mu27 is the actual unramified cubic extension of the residue field F289; the radical factor is totally ramified degree9. The ideal norm and extension coefficients(1,3) and(3,1) follow with their respective residue/ramification degrees.

For an abelian extension over F containing E, becoming unramified over E is exactly the condition that its local Artin map kills Norm(O_E^×). The imposed local rows are those complete norm groups. At primes away from S, unramified base change cannot remove ramification. The modulus exponent16 is sufficient since the local logarithm divides by9 from filtration16 to filtration4, which remains in its convergence/isomorphism range. The local residual unit quotients have exponent9 and the ordinary base class group exponent3, so every resulting three-primary ray quotient has exponent dividing27. The exponent27 ray construction therefore retains the full maximal field specified in E94.4.

The full local norm uniformizers are also correctly typed. At Q, (1+beta1)beta1^{-2} has valuation1 and both characters0. At T, beta1³ has valuation3 and both characters0. Their ray classes are obtained with the required negative sign from the prime-to-S ideal(z)/v^{v(u_v)}. They compute the actual upper prime Frobenii, including the distinct norm coefficients at the ramified and inert primes.

## Actual norm and extension through the E.91 residual group

The original ninth-genus field lies in the new maximal genus field by inclusion of the actual local unit norm groups. The old/new ray-basis comparison evaluates the same actual basis ideals and retains its inverse; it is not an identification by abstract cyclic factors. Restriction of upper Frobenius is the lower Frobenius raised to its residue degree, so the resulting matrix N is the ideal norm.

For extension, the field automorphism G³ preserves B3, restricts to the actual g2, and belongs to Gal(E/F). On the abelian-over-F genus quotient A it acts identically. Equivariance of ideal extension therefore kills (g2-1)Cl(B3){3}=W. This gives an actual factor J:A9→A before any finite matrix is selected.

Both full class norms are onto: E/B3 is cyclic cubic and ramified at Q, so its intersection with either relevant Hilbert class field of B3 is trivial. Chebotarev in the compositum supplies degree-one primes above any prescribed ordinary or S-class. On A, the deck H³ acts identically; hence the actual identities are JN=1+H³+H⁶=3 and NJ=3. The computed ker N is C3², so three times a lift under N is independent of the lift. It uniquely forces J to be the stated matrix. All six prime columns satisfy both degree-weighted norm and extension diagrams.

## Normalizer and S-class map

The substitutions G and H satisfy the literal semidirect relation and all243 elements. G does not preserve B3; G³ and H do. The proof uses this exact distinction via the demonstrated field maps. Both automorphisms preserve F and the actual maximal genus construction, so their induced ray actions preserve all three relation/kernel lattices. The computed ordinary actions have cube1 and commute, consistent with their restrictions; the S action is G=I and H=[[1,3],[2,1]] on C9×C3.

The norm row to the original C3 is obtained from the certified base S-class coordinate on the same ray ideals and the actual E86 coherent prime73 norm isomorphism. It is exactly(-1,0), with kernel C3². The noncyclic module conclusion follows through the displayed surjection to C9×C3 with trivial H³ action. It does not assign either full upper class group to that quotient. The original transvection value and eventual exponent h remain unevaluated, exactly as stated.

## Reopened primary source

Official J.S. Milne, *Class Field Theory*, https://www.jmilne.org/math/CourseNotes/CFT.pdf , version4.03. I reopened III Theorem3.1 and its restriction/corestriction proof, III3.4; V Example3.2, Proposition3.3 and Theorems3.5–3.6; V Proposition5.2 and Summary5.10, especially printed181–182 for the inverse cyclotomic convention; and VIII7.4. The proof uses the proved III3.1 compatibility. It does not rely on the nearby III Lemma3.2 placeholder proof.

## Fresh finite verification

The copied verifier checks all ten exact Smith systems and inverse maps, all2187 ordinary relative coordinates, all27 relative S coordinates, the243 normalizer elements, all norm/extension matrices, and the exact local character matrices. The complete91-record JSON agrees byte for byte. Its SHA256 is `6f3d3d0e87c9ef4228f7a01168a91be0d4157adca88811200ccd26babb61a36b`.
