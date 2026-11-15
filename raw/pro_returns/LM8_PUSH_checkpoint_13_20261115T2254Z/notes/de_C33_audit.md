# Independent audit of C.33

**Verdict: PASS.** This audit reads the complete unregistered proof in `notes/pbc_C33_draft.tex`, the actual lifting proofs P.2 and P.4, the graded computation `code/pbc_gentle_even_fast.py`, and the integral lattice certificate. It does not infer an actual group character merely from a graded dimension.

## Actual local image

P.2's correction map in each later homogeneous degree is the integral map `(u,v) -> [u,x]+[v,y]`, which is onto by Jacobi induction. Successive corrections therefore integrate any displayed special homogeneous derivation, preserve its leading term, and converge in the actual pro-13 group. The pro-13 IA kernel and coprimality of 6 allow the nonabelian S3 discrepancy cocycle to be removed in strictly higher degree. The full relative pronilpotent lifting argument P.4 then lifts the entire pro-13 solution with the other prime components the identity, so the leading weight-twelve vector has an actual global multiplier-one representative.

The normalization has no peripheral-centralizer ambiguity in degrees at least two. The conjugator convention produces the derivation `D_f(y)=[y,f]`; its commutator is the stated Ihara bracket `[f,g]+D_f(g)-D_g(f)`.

## Integral lattice and logarithm

The unit-minor argument is sufficient: the full kernel of the integral equation matrix is saturated, and the computed rational basis remains independent modulo 13 in the ambient free module. Its Z13 span must therefore be the full integral kernel. I reran `pbc_gentle_weight12_integral.py` without rewriting the author's JSON. The independently saved stdout is `code/de_C33_integral_audit.out`. It verifies rank seven, bracket rank six, the primitive functional `(-4,1,8,-4,-17,14,84)`, and the normalized modulo-thirteen witness value one.

The actual quotient U has a finite filtration by free Z13 modules and hence is finitely generated, torsion-free, and pro-13. Starting in conjugator weight three, it has nilpotency class at most four. On the Magnus algebra modulo augmentation degree fourteen, U acts faithfully: a conjugator of weight twelve changes a generator in degree thirteen, whereas weight thirteen acts trivially. Every operator `a-1` raises positive augmentation degree by at least three. Its logarithm and exponential therefore have at most four nonzero terms, with denominators prime to thirteen. The proof never applies a class-thirteen integral BCH assertion to the free group.

## Tame splitting and character extension

The inverse image of μ12 in the compact arithmetic image has pro-13 kernel, so coprime complement conjugacy supplies an actual element of order twelve in that image. This need not lift to an element of order twelve in the absolute Galois group, and the proof does not claim that it does.

Weights three through twelve have pairwise distinct residues modulo twelve. Each tame idempotent therefore gives an actual integral filtered splitting: its image lies in the corresponding filtration step, maps onto its grade, and has zero kernel because no later grade carries that character. The Ihara brackets become the exact brackets between these eigensummands; there is no hidden higher-degree commutator contribution. The integral weight-twelve functional consequently kills the full Lie commutator lattice.

On the abelianized lattice the action factors through the multiplier group, so all multipliers commute with the tame action there even if chosen lifts do not commute in G. The top eigensummand transforms by the exact twelfth power of the multiplier, which is trivial modulo thirteen. This establishes invariance of the character. The vanishing of H2(Z13^×,F13), by coprime averaging and cd13(Z13)=1, then gives an actual continuous extension to G.

## Arithmetic correction

The primary Hain–Matsumoto statement is for the actual pro-prime automorphism representation at the standard tangential basepoint, not only its outer or rational unipotent image. It is unramified away from thirteen. Kronecker–Weber makes every additive F13 character with this ramification a scalar multiple of `(λ13^12-1)/13 mod13`. Subtracting that character removes the entire arithmetic restriction and vanishes on global multiplier one. Thus the actual weight-twelve witness remains nonzero. No rational-cohomology vanishing or unproved integral denominator control is used.

## Independently opened primary sources

- Garaialde Ocaña–González-Sánchez, *Transporting cohomology in Lazard correspondence*, https://arxiv.org/pdf/1405.4654, Theorem 1, printed page 3; references `turn726view0`, `turn727view0`, `turn727view3`. Its clauses include subgroups, ideals, and automorphisms for finitely generated pro-p groups of class less than p.
- Hain–Matsumoto, *Weighted Completion of Galois Groups and Galois Actions on the Fundamental Group of P1−{0,1,∞}*, https://arxiv.org/pdf/math/0006158, §8.5, printed page 28, immediately before Theorem 8.7; references `turn726view1`, `turn727view2`.
- Milne, *Class Field Theory*, https://www.jmilne.org/math/CourseNotes/CFT.pdf, I Theorem 4.16 and its proof, printed pages 49–50; references `turn726view2`, `turn727view1`. The proof uses only roots of unity supported at the actually ramified primes.

No mathematical blocker was found. The exponent-two metabelian conclusion C.32 then excludes factorization of the new character through that image.
