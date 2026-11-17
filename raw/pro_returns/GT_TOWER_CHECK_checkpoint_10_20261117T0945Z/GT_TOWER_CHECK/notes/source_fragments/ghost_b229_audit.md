# Independent audit of B.2.29

Reviewed source: `work/centralizer_perfect_source_factor.tex`, with the exact definitions and image equality in B.2.13–15 and the normalization calculation in B.2.27. No mathematical defect was found.

## Actual perfect factor

The modular source homomorphism sends s and r to the displayed projective matrices of orders two and three. Their product is the upper unipotent with parameter −1, so its powers give every upper unipotent over F_p; conjugation by S gives the lower ones. Thus the displayed map is onto PSL2(F_p).

The retained Brunnian matrix uses the exact source convention x=(sr)^−2 and y=sxs. These are the matrices with upper-right entry2 and lower-left entry−2, respectively. The two gcds128 and2 show that the word is neither I nor−I modulo any odd prime. Therefore the image of the actual normal six-coordinate kernel K0 is nontrivial, and simplicity makes it all of Q_p.

For K0,R=K0∩ker(q_R), its image is again normal in Q_p. If that image were trivial, the already-surjective K0→Q_p would factor through the subgroup K0/K0,R of the finite group R. The divisibility p∣|Q_p| would force p∣|R|. This contradicts the specified choice of p. Hence q_p(K0,R)=Q_p. The joint map to U0,R×Q_p is onto by an actual kernel calculation. The profinite joint map has the same conclusion because it contains this discrete kernel image; no identification of an unspecified completion kernel is required.

The primary author PDF by Keith Conrad was opened independently at https://kconrad.math.uconn.edu/blurbs/grouptheory/PSLnsimple.pdf. Theorems3.3–3.5, printed pp.4–5, give exactly the generation, perfectness and simplicity statements used here.

## Integral canonical central kernel

Put L=K0,R,p. It lies in B0′, so B0ab→(B0/L)ab is an isomorphism C6. The integral homology five-term sequence is

H2(B0,Z) → H2(B0/L,Z) → L/[B0,L] → H1(B0,Z) → H1(B0/L,Z) → 0.

The first group vanishes for B0=C2*C3, and the last displayed map is an isomorphism. Thus the middle transgression is an actual isomorphism H2(B0/L,Z)≅L/[B0,L]. This remains an integral assertion even when U0,R is infinite.

For the actual product U0,R×Q_p, integral Künneth in degree two has the two factor H2 groups and the term H1(U0,R,Z)⊗H1(Q_p,Z). The latter vanishes because Q_p is perfect. There is no Tor contribution in this degree: its possible factors involve H0=Z. The splitting is induced by the actual coordinate inclusions and projections.

## Character separation and the centralizer lift

Choose the actual word v∈K0,R mapping to q_p(s). Its image is b=(1,q_p(s)), and the named source s has image (s_U,q_p(s)); these commute in the product. Their lift commutator defines an element m of the canonical integral central kernel.

For every character χ of that kernel into Q/Z, push out the central extension. Since Q/Z is injective as an abelian group, the universal-coefficient Ext term vanishes. Naturality of the preceding Künneth splitting says that this pushed-out H2 class is the sum of classes pulled back from the two actual factors.

In a pullback from U0,R, b projects to the identity. Every lift of it is central in the first-factor extension, hence commutes with a lift of s. In a pullback from Q_p, b and s project to the same element. Their first-factor lifts differ by a central element and again commute. The commutator pairing on commuting elements is additive under Baer sum. Therefore χ(m)=0 for every χ.

Characters into Q/Z separate arbitrary abelian groups: a character detecting a nonzero element on its cyclic subgroup extends by injectivity. Consequently m=0 integrally. This proves the literal word containment [v,s]∈[B0,K0,R,p], which maps directly into the closed profinite commutator subgroup. The proof does not infer the containment from vanishing in a finite quotient or from an unproved completion comparison.

## Full lift and normalization

The kernel K_R,p is closed, normal, and contained in F∩B′, so the full central-cover image equality B.2.14 applies with this exact kernel. The identity automorphism of its central cover has the prescribed pure s-frame v and the trivial r- and cusp frames. This yields the full positive cusp-fixed automorphism and the two exact frame residues stated in B.AB4.

Its s-frame β lies in K. The two actual six-coordinate abelian maps give 3u+v=0 and u+3v=0 modulo6. They imply u,v divisible by3 and congruent modulo2, hence t=v−u∈6 Zhat. The normalized source action changes the first-coordinate descendant by conjugation with s^t=1. The resulting normalized element therefore lies in the literal kernel of D_P. The statement correctly does not claim that normalization leaves every additional PSL2(F_p) frame residue unchanged; the later harmonic calculation tracks that separately.
