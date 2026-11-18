# Targeted checks for the real elliptic section

This file supports notes E01–E30. The frozen transcription is not altered. These are mathematical checks of stated interpretations, not a further handwriting transcription. Hua's supplied Lean claim is reported with attribution; no Lean source or certificate was supplied or executed here.

## P1. The module–triple equivalence (E01–E02)

Let k be any ring and let M be a left k-module for which multiplication by 2 is injective. Let σ be k-linear with σ²=1. Put P=ker(1−σ), Q=ker(1+σ). Their intersection is zero, since an element in it satisfies 2x=0. The identity 2x=(x+σx)+(x−σx) identifies 2M with a submodule N of P⊕Q containing 2P⊕2Q. If 2x belongs to P, injectivity of 2 gives σx=x, so N∩P=2P; likewise N∩Q=2Q. Consequently m=N/(2P⊕2Q) meets both direct summands of P/2P⊕Q/2Q trivially. Its two projections are injective, so it is the graph of an isomorphism between its two projected submodules.

Conversely, from 2-regular P,Q and such an m, let N be its inverse image in P⊕Q, with σ_N(p,q)=(p,−q). This preserves N since minus equals plus modulo 2. The eigenspaces of N are 2P and 2Q: for example the plus eigenspace has q=0 and its residue in m meets P/2P only in zero. Identify P with 2P and Q with 2Q by multiplication by 2; under these identifications the triple obtained from N recovers m, because 2N/(4P⊕4Q) is the image of m under doubling. Starting with M gives N=2M and the equivariant isomorphism x↦2x.

For the category of triples take a morphism to be a pair of k-linear maps f:P→P', g:Q→Q' whose reductions carry m into m'. Then f⊕g restricts to the inverse-image modules, and the multiplication-by-2 identifications above are natural. This supplies unit and counit and proves the equivalence, with no commutativity, finite generation or projectivity assumption. It checks the mathematical content of **Hua, findings register, 67-involution-modules-triples** and Hua's modernised section XII, but not the asserted Lean implementation.

## P2. Scope of the revised rank-two corollary on scan 91 (E03)

The retained broad hypotheses “k comm.”, “k 2-régulier”, “M projectif de rang 2” and σ≠±id do not by themselves imply that P,Q are invertible rank-one modules. Take k=Q×Q and M=k², so M corresponds to (Q²,Q²), and let σ=(diag(1,−1),id). This is an involution different from both global ±id. Its eigenspaces have ranks P=(1,2) and Q=(1,0) on the two components, hence neither has constant rank one. This refutes only the literal unrestricted corollary, not the general equivalence in P1; the obscured/deleted earlier hypotheses may record a narrower intended claim.

A sufficient refinement when 2 is invertible is to require the ± eigenspaces to have rank one on every connected component; then the idempotents (1±σ)/2 split them as rank-one projective summands. Over a PID domain, the nontrivial rank-two involution also has rank-one free eigenspaces, but classification of the gluing slope still needs P3.

## P3. Unit reduction and rank-two integral conjugacy (E04–E05)

For a PID domain k with 2 nonzero and k₀=k/2k a field, let M be free of rank two and σ≠±1. The two eigenspaces are free rank one, so m is either zero or the graph of a nonzero slope λ in k₀×. Changing bases in P and Q changes λ by the ratio of two reductions of units of k. Therefore the nonsplit conjugacy classes are indexed by

(k₀)× / image(k×→k₀×),

and there is additionally one split class. In particular there are precisely two classes only if that reduction map is onto. This is the proviso retained by Hua's modernised corollary but struck through in the supplied scan 100.

A concrete counterexample to an unconditional two-class assertion is k=Z[ω], ω=(1+sqrt(−11))/2, so ω²−ω+3=0. It is norm-Euclidean: for any complex number in Q(sqrt(−11)), choose the ω coefficient modulo Z in [−1/2,1/2], then choose an integer translation to leave real part in [−1/2,1/2]; the remaining norm is at most 1/4+11/16=15/16<1. Thus k is a PID. The norm a²+ab+3b²=(a+b/2)²+11b²/4 equals 1 only for b=0,a=±1, so k×={±1}. Modulo 2, ω²+ω+1=0 is irreducible and k₀=F₄; both units reduce to 1, hence there are three nonsplit classes and one split class.

Explicit involutions on k² are A_λ=[[1,0],[−λ,−1]] for λ=1,ω,ω+1. They satisfy A_λ²=1, and the three gluing slopes have distinct residue classes modulo the image of k×. Their inequivalence follows from the functorial eigenspace/gluing invariant in P1, not from a bounded search.

## P4. Real forms and the square exception (E09–E14,E16)

Assume an origin-preserving complex torus has a reflection σ and its rotation group has order n∈{2,4,6}, as on scans 94–95. Write the extended group as D_n=<r,σ | r^n=σ²=1, σrσ=r^{-1}>. The reflections are r^jσ; conjugating by r^k changes j by 2k. Since n is even there are exactly two rotation-conjugacy classes. The element −σ is r^{n/2}σ, so it is in the same class as σ exactly when n/2 is even, namely n=4.

This checks the manuscript's square exception on 97–98 and exposes a limit of Hua's footnote that calls the two forms quadratic twists by −1. Twisting the descent datum by the central automorphism −1 changes σ to −σ; for n=4 this is the same real form, not the other one. The other class is represented by rσ. Thus “exactly two real forms” remains correct, while the proposed universal identification of the second form with the −1 quadratic twist does not.

For a rank-two lattice with primitive eigenvectors e₊,e₋ and diagonal metric Q(e₊)=1,Q(e₋)=a, replacing σ by −σ swaps the two vectors, so a goes to 1/a and the lattice splitting type stays the same. This explains the retraction of scan95 by scans97–98; no new family index prime should be inferred from the parameter prime a'. The same underlying complex curve has the same modular invariant under this change, which already rules out j=c log(a) for a fixed nonzero c on an entire family: reciprocal a changes the sign of log(a) but not the complex curve.

## P5. Hexagonal metric and period check (E15,E17)

For a regular triangular lattice take Q(u)=Q(v)=1 and B(u,v)=1/2, with reflection fixing u. The anti-invariant primitive vector is 2v−u. Its squared norm is

Q(2v−u)=4Q(v)−4B(u,v)+Q(u)=4−2+1=3.

Hence the quadratic-form ratio a is 3; sqrt(3) is the ratio of lengths, not squared lengths. Hua's modernised XII already identifies this correction, and this run rechecks it. With the manuscript's period formula τ=(1+i sqrt(a))/2, a=3 gives the angle-60-degree period (1+i sqrt(3))/2; a=sqrt(3) does not. The frozen transcription continues to read sqrt(3) at scan98.

The period formulas themselves follow by identifying e₊ with 1 and e₋/sqrt(a) with i. In the split lattice the generators become 1,i sqrt(a), while in the nonsplit lattice generated by u=e₊ and v=(e₊+e₋)/2 they become 1,(1+i sqrt(a))/2.

## P6. Fixed loci and H¹ over R (E18–E21,E24,E30)

For the split lattice Λ=Z e₊⊕Z e₋, σ(x,y)=(x,−y), so real points satisfy 2y∈Z and give two circles modulo Λ. For the nonsplit lattice with basis u,v and σu=u, σv=u−v, the fixed-point condition is y(u−2v)∈Λ; since the coefficient of u is y this is equivalent to y∈Z, leaving one circle. The positive sign in the scan99 difference formula is immaterial to that integrality test, but it is not the literal algebraic difference.

The conformal quotient has Euler characteristic zero and its boundary is the fixed locus. For two boundary circles, the classification of compact surfaces forces an annulus; for one boundary circle, orientability would give Euler characteristic 1−2g, so the quotient is instead the Möbius strip. This supplies the topology invoked by Hua and E18, with the lattice calculations furnishing the boundary count.

For C₂=<σ>, the periodic resolution with alternating maps σ−1 and N=1+σ gives H²(C₂,Λ)=Λ^σ/NΛ. An R-vector space V has no positive-degree C₂-cohomology: the projectors (1±σ)/2 split it, so the alternating resolution is exact in positive degrees. The long exact sequence of 0→Λ→V→E(C)→0 therefore gives H¹(C₂,E(C))≅H²(C₂,Λ).

In the split case Λ^σ=Z e₊ and NΛ=2Z e₊, giving Z/2. In the nonsplit case Λ^σ=Z u and Nv=u, so the quotient is zero. These are the calculations written on scan101 and already explained in Hua XII; the check here supplies no new claim about the much harder nonabelian H¹(C₂,K_c) in **LM4_SUCCESSOR E.10**.

A concrete nontrivial torsor in the split case has underlying complex torus C/(Z+i t Z), t>0, with antiholomorphic descent map c_T(z)=bar(z)+1/2. Its square is translation by 1 and thus the identity on the torus. It has no fixed point, because bar(z)+1/2−z has real part 1/2, which cannot be the real part of an element of Z+i t Z. Its action on differences is ordinary conjugation, so its Jacobian is E_{t²}, and its cocycle is the nonzero class just computed.

The quotient of this fixed-point-free involution is compact, without boundary, nonorientable and has Euler characteristic zero (the cover is a torus). It is a Klein bottle. This confirms Hua's reading of the geometry behind the cancelled “sans” on101; it does not reinstate the cancelled word in the frozen transcription. “Genre 1” in that sentence is the complex/arithmetic genus convention; the Klein bottle has two crosscaps in the usual classification of closed nonorientable topological surfaces.

## Limits

These checks do not independently establish algebraic uniformization, the full real moduli stack, integral compactification, or any higher-genus profinite conjugacy/classification claim. The broad register entries were used only to specify these limits. The direct algebra above does not require consulting or correcting the frozen manuscript readings.
