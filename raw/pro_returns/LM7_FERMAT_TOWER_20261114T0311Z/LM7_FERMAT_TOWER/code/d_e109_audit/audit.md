# Independent E109 audit

**Result: PASS. No mathematical correction requested.**

Audited section SHA256: `44272e13556e1bf024600c6bad597ac576f1c5f3db4add3cd1002d3b2f61beea`.

I read the complete current E109 proof, all of its author program, the cited E103 isogeny/duality argument, and the primary-source passages below. This review includes a fresh independent finite computation. The parent owns the separate full replay of the author program; this audit does not claim a second full replay.

## Integral coefficient and cohomology maps

The quotient by q is the actual class-two surface quotient. Contraction gives 2h; alternation gives 3eta modulo qH and -2qH on inner maps. The explicit Pi is integral at five and is a Galois-equivariant left inverse on coefficients, hence on continuous cochains and H1. The rank-six inner map remains rank six modulo five.

## CM polarization and Galois stability

E103 has Psi=Phi dagger and PsiPhi=[4], hence Phi scales the polarizations by four. Transferring the product [i] therefore preserves the polarization. The integral plus/minus eigenspaces are isotropic and perfectly paired; Galois preserves or exchanges them.

## Affine filling and changes of origin

The block-matrix equation gives cC=pB cA j+Jj-g(Jj) with the retained actual section pj=1. Geometric change of section contributes exactly ad of the abelian component; Pi kills it. No associated-graded-only argument is used.

## Harris-Pulte factor two and sign

HM uses g(u)u^{-1}; Proposition5.5 extends 2tau and Theorem3 identifies that extension with mu. BLLS Corollary2.17 and full Proposition2.23 comparison identify the unique alternating preimage of twice MD with mu. The degree-two logarithm sends xyx^{-1}y^{-1} to XY-YX, matching the positive wedge convention.

## Entire Delta projection

All twenty exterior characters checked. Exactly the pure plus and pure minus cubes are invariant; H and qH have no invariant character. Curve-automorphism invariance modulo inner maps makes the same average apply to the class. Restriction/corestriction index four is a unit in Z5, proving the full GQ equality.

## Plus/minus curves, maps and cycle

Read and checked all three rational maps and the exact translation by T=(0,0). The based images are two-torsion, so [2]rho=[2]PhiB i_b literally. Pushforward on H3 of the abelian threefold is eight, a five-adic unit. This gives the cycle-class equality without assuming translation invariance. PhiB is Phi followed by permutation and CM units and preserves the pure-CM projector.

## Original Bloch nonvanishing and infinite order

Original printed98-101,103-104 read, with six actual page images viewed. Proposition2.1/Corollary2.2 and the Section3 correspondence detect the pure CM class through 4delta. The independent p19 calculation gives delta=(17,16) of order10 and fourdelta=(9,4) of order5. Section4 states nonzero beta5 and uses Frobenius -11 on the relevant quotient; -12 is a five-adic unit, so rationalization of H1 is injective. Restriction index two and the literal curve isomorphism preserve nonvanishing.

## Program source and execution scope

Read the entire author program. Parent owns the complete fresh author replay; this peer audit does not duplicate or claim that replay. A separate independent program, importing neither author code nor certificate, was freshly executed with exit0 and verifies all coefficient columns, rank modulo5, Delta invariants, the nineteen trace-one summands at p19, exact point orders, and the group-ring sign.

## Primary-source scope

- **Hain-Matsumoto2005**: Theorem3, PDF/printed4; Section5.1 Magnus convention,13; Section5.2, Lemmas5.2-5.3 and proofs,14-15; Section5.3, Lemma5.4 and Proposition5.5,16-17; Theorem8.1 and Theorem3 proof,28-29.
- **Bisogno-Li-Litt-Srinivasan2023**: Corollary2.17,11; Lemmas2.20-2.22 and Proposition2.23,12; Full Proposition2.23 proof,13-14.
- **Bloch1984**: Proposition2.1, printed98/PDF6; Corollary2.2, maps and Lemma3.1,99/PDF7; Lemma3.2 and formula3.3,100/PDF8; Pure CM projector,101/PDF9; Formula3.6,103/PDF11; Section4 and Theorem4.1,104/PDF12.

The actual viewed page-image filenames and hashes, all reviewed artifact hashes, and the precise execution scope are in `audit.json`. The focused independent verifier is `code/d_e109_independent.py`; its actual stdout and JSON are retained alongside it.

No proof or author-code files were changed.
