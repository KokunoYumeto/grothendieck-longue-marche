# Independent check of the formal-Picard unit-boundary counterexample

Requested by the root researcher after completion of the Picard memo; checked independently by the Picard research agent, GPT-6 Astra Pro, run 2026-11-18. No images or frozen transcription files were changed. The construction was proposed by the root researcher; the check below is an independent verification, not an independent attribution of the idea.

## Statement being tested

The manuscript at cote 29 scan094 claims the kernels `Pic(X_m)→Pic(X_0)` are “uniquement divisibles” by n when n is invertible; the boxed “à vérifier en détail” stands nearby. Hua, modernised reading of cote29, `context/hua_project/29.modern.tex`, “Le cas où la classe s'annule : Picard formel,” p.93/scan094, claims the kernel is filtered by additive coherent-cohomology groups and therefore uniquely n-divisible. The displayed general lemma at [Stacks Project, tag0C6S](https://stacks.math.columbia.edu/tag/0C6S), opened during this check, likewise claims `Pic(X′)[n]→Pic(X)[n]` bijective for arbitrary thickenings; its proof reduces to vanishing of n-torsion and n-quotients in coherent cohomology but does not account for the preceding global-unit boundary.

The direct calculation below gives a counterexample to the unconditional injectivity/unique-divisibility statement for a nonproper special fibre. It does not disprove versions with a suitable global-unit lifting condition, proper connected geometric fibres, or some other additional hypothesis, and it does not decide whether the later tame-cover construction needs uniqueness rather than divisibility.

## First-order construction

Let E be a smooth projective connected elliptic curve over C, let `A=C[ε]/(ε²)`, and choose a nonzero class `a∈H¹(E,O_E)`, represented by an additive Čech cocycle `a_ij` on an affine cover of E. On `E_A`, glue a line bundle L by the multiplicative cocycle `g_ij=1+ε a_ij`; the additive cocycle relation and ε²=0 ensure this is a line bundle, and its restriction to E is the trivial bundle. Set `X′=L^×`, the complement of the zero section in its total space; its closed fibre `X_0` is `E×G_m`, and the ideal `I=ε O_{X′}` is square-zero and canonically isomorphic as an `O_{X_0}`-module to `O_{X_0}`. Hence `X_0⊂X′` is an actual first-order thickening, locally the product thickening, not merely a formal class in a deformation group.

## Global units and the boundary

Since E is proper connected and reduced, `Γ(E,O_E)=C`, whence `Γ(X_0,O_{X_0})=C[z,z^{-1}]` and `Γ(X_0,O_{X_0}^*)=C^*·z^Z`. On local charts of L, the fibre coordinate z lifts to a unit, but its local lifts differ by `1+ε a_ij` or its inverse, depending on the coordinate convention; therefore the boundary of z in `H¹(X_0,I)` is `±a⊗1`. Constants lift, so the entire image of the boundary is exactly the cyclic subgroup `Z·(a⊗1)`, not its C-linear span. Affineness of `E×G_m→E` and quasi-coherent cohomology give `V=H¹(X_0,I)=H¹(E,O_E)⊗_C C[z,z^{-1}]`.

## Picard kernel calculation

The units sequence `1→1+I→O_{X′}^*→O_{X_0}^*→1`, with `1+I≅I` additively, gives

`ker(Pic(X′)→Pic(X_0)) ≅ V / Z·(a⊗1)`.

For every integer n>1, the class of `(a⊗1)/n` in this quotient is nonzero and is killed by n: equality with an integer multiple of a would imply `1/n∈Z`. Thus the kernel has nonzero n-torsion despite n being invertible over C. It is still n-divisible because V is n-divisible; uniqueness, and the injectivity of the n-torsion restriction map, fail.

## Equivalent geometric verification

Let M on `E_A` have transition functions `1+ε a_ij/n`, so `M^{⊗n}≅L`. On `X′=L^×`, the pullback of L has its nowhere-zero tautological section, so the pullback of M is an n-torsion line bundle. Its restriction to X_0 is trivial; its class is exactly `(a⊗1)/n` modulo the global-unit boundary, so the preceding calculation proves it is not trivial on X′. This gives a second description of the same witness and identifies the precise line bundle, rather than relying only on an abstract possible failure of an exact-sequence argument.

## Extension to a regular formal scheme

Using the same additive cocycle, glue formal line bundles on `E×Spf C[[t]]` with transition functions `exp(t a_ij)` and `exp(t a_ij/n)`. Their punctured total spaces are locally `Spf(O_E(U)[z,z^{-1}][[t]])`, so the resulting formal scheme is regular, with regular special fibre `E×G_m` cut out by the principal divisor t; the two bundles are related by the nth tensor power as above. The pullback of the root bundle is formally n-torsion and reduces to the already nontrivial first-order class, so it is nontrivial formally. This construction does not require algebraizing the formal line bundle to establish the counterexample in the formal category.

## Why topological invariance of the étale site does not invalidate it

For invertible n, `H¹_et(−,μ_n)` is insensitive to a nilpotent thickening, but this classifies a line bundle together with a chosen trivialization of its nth power. The Kummer sequence also contains the global-units quotient before that group, so it does not identify `Pic[n]` alone under arbitrary thickenings. In this example the µ_n-torsor reduces to the nontrivial Kummer torsor for the unit z on `E×G_m`, while its associated line bundle on the special fibre is trivial. Thus there is no contradiction with topological invariance or with the Kummer exact sequence; the distinction is explicitly visible in [Stacks tag03PK](https://stacks.math.columbia.edu/tag/03PK).

## Precise source-check status

The currently opened wording of tag0C6S is contradicted by the explicit first-order construction above; this is a finding of this run, not an assertion accepted from an earlier context note. The unrestricted conclusion should therefore not be cited as a checked supporting theorem for scan094. A safe elementary sufficient condition for unique n-divisibility in the first-order case is that all global units on X_0 lift to X′, in which case the boundary vanishes and the kernel is `H¹(X_0,I)`; for higher-order thickenings, impose the corresponding condition at each step.

Tool references for the root's source review: tag0C6S = `turn708340837view0`; Kummer sequence = `turn372659338view0`. The proposed mathematical check event is an independent re-proof of the root's construction, with the outcome “counterexample confirmed for arbitrary nonproper thickenings; proper/global-unit-lifting refinements not refuted.”
