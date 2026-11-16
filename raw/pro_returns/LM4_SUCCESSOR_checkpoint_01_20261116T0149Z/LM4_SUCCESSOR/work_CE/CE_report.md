# C and E.1 research report — INCOMPLETE

## Outcome table

| Prompt task | Current result | Successor statements |
|---|---|---|
| C.1: actual torus fixed kernel K′=1 | Open. A nontrivial kernel must have an infinitely generated free pro-p quotient for some odd p; an abelian kernel is trivial. A two-generated projective retract shows the coarse conditions alone do not imply triviality. | C.1–C.4, C.12 |
| C.2: negative torus peripheral conjugacy | Open. Exact transporter and centralizer reformulations independently proved; the additional outside centralizer element has not been constructed. | C.8, C.11, C.13–C.14 |
| C.3: scalar cubic action | Open. Explicit integral symplectic lattice and a geometric filled-surface model prove why the quartic linear contradiction does not transfer; no full torus action or exclusion is asserted. | C.24, C.26 |
| C.4: LM4 D.42 | Complete independent proof, including primary faithfulness, the order-three assertion, both transposition signs, and the finite-group consequence. | C.15–C.17, C.23 |
| C.4: LM4 D.70 | Complete independent proof, including global involution sign, quartic lifting, exact dihedral quotient, integral square, and actual filling/fixed-character contradiction. | C.17–C.22 |
| C.4: LM4 D.74 | Independently proved, including full finite-coefficient duality and permutation-module detection; the stated unique coboundary does not prove the missing third-cusp equation. | C.5–C.7 |
| C.4: LM4 D.75 | Independently proved with the global sign theorem independently supplied in C.18. | C.8, C.13 |
| C.4: LM4 D.76 | Independently proved, including compact projectivity, free rank two, and exact generation criterion. | C.9 |
| C.4: LM4 D.77 | Independently proved and checked in A5. | C.10; code/check_D77.py |
| C.4: LM4 D.78 | Independently proved with all finite E-set coefficients and the exact cohomology comparison; original K′ question remains open. | C.11–C.12 |
| E.1: LM6 C.13–C.19 | Each independently proved in its exact category. C.16 and C.17 use the prime-two element theorem only. | E.1–E.7 |
| E.1: six fixed congruence kernels and H1 sets | Uncomputed. Exact inverse-limit and oval-stabilizer-fibre descriptions supplied; no full-completion/procongruence identification assumed. | E.8–E.10 |

## Scope and proof distinctions

The files `C_torus.tex`, `C_audit.tex`, `C_quartic.tex`, `C_further.tex`, and `E_real.tex` contain original successor exposition and proofs. They are not extracts of the earlier return. Statements labelled Open are still explicit tasks. In particular the result that a pro-odd kernel cannot be finitely generated is not a proof that it vanishes, and the model in C.2 is not an actual punctured-torus action.

We read LM4 D.42, D.70, D.74–D.78 and all LM6 C.13–C.19. For dependencies we read LM4 D.58–D.62 and D.68–D.69, and have independently reconstructed D.33, D.43, D.46 and the needed part of D.55, followed by D.68–D.70 and the D.36/D.41 transposition signs. The old text remains a claim under audit; proofs in the successor identify the exact continuous maps instead of appealing to an unrefereed row as authority.

The genus-three result does not solve the mapping-class congruence subgroup problem. Even for the five oval types, the formula `C_P(τ)=K_c^τ ⋊ closure(C_Γ(τ))` does not compute `K_c^τ`. In the free real type, density of the completed nonorientable mapping-class action in the displayed procongruence centralizer is an additional issue. The nonabelian H1 fibre is an orbit set for the full quotient centralizer; that action need not fix the trivial class. A finite D8 example verifies this qualification.

## Computations performed

- `code/check_kernel_model.py` and its `.out`: finite quotients of the projective countermodel, with orders 18, 36 and 324. The script checks multiplication, generation, the cyclic quotient, derived subgroup and kernel, and invariant-vector failure. Projectivity and all-open-subgroup assertions are proved in C.2, not inferred from these finite samples.
- `code/check_D77.py` and its `.out`: permutations in A5 give original generated group order 60, selected subgroup order 10, kernel image order 5 and incidence cokernel size 5. This is a full finite witness of the failure of the chosen triple to generate.
- `code/check_real_models.py` and its `.out`: D8 cocycle orbit action, the N4 orientation-cover graph and signed twist permutations, squarefreeness and exact real-root counts for the six degree-eight hyperelliptic models. Topological dividing-type assertions are proved in the text rather than inferred merely from polynomial root counts.

## Primary reading and citation discipline

See `source_log.md` and `CE_references.bib`. Each bibliography entry is marked verified only for the source and precise portion actually opened. In particular the Feit–Thompson theorem is used as an established theorem; its 255-page proof is not claimed to have been reaudited. Boggi–Zalesskii is used only for one element of order two in these sections. The possibly invalid nonsolvable-centralizer intersection is not used.

## Exact remaining work and attempted routes

1. For C.1, the finite-set formulation detects any nontrivial kernel element. The obstacle is to prove surjectivity for all actual finite E-sets, not just mod-two dimensions or maximal pro-p quotients. The projective countermodel satisfies the coarse numerical conditions and blocks that shortcut. An abelianity argument, or a theorem identifying the actual fixed group as a free profinite factor, would be decisive; neither has been established for the actual group.
2. For C.2, C.13 supplies exact unique transporters. The obstruction is an outside element in the centralizer of at least one full-unit transporter. Pro-p generation does not supply such an element in the full group.
3. For C.3, the cubic deck module has cyclotomic and regular summands. The integral fixed vectors on regular summands have pairings divisible by three; the quartic fixed-character contradiction is therefore not automatically available. The exact lattice and geometric construction are now C.24; the unresolved descent obstruction is C.26.
4. For E.1, inverse limits of finite fixed groups and finite nonabelian cohomology sets are exact, but no finite quotient of the actual congruence kernel has been computed that settles these inverse limits. The oval-stabilizer fibre gives an exact geometric target: uniqueness of its fixed lift would prove trivial fixed kernel. No such fixed-lift theorem has been supplied.

## Files and build status

The `D_*.tex`, `D_*_proof.tex`, `LM6_C_*.tex`, and `LM6_C_*_proof.tex` files are identifiable intermediate extracts copied from supplied AI text for audit. They are not successor proofs and should be excluded from the final archive as duplicate supplied material, with the exclusion recorded. Downloaded primary PDFs and their selected rendered pages document actual source reading.

A private test wrapper `CE_check.tex` was created. The first system LuaLaTeX invocation failed before reading document content because its format was absent. Root has since provided a private LuaLaTeX runtime and will build the combined paper; this is not a claim of a successful typesetting check. Build corrections and final counts will be recorded by root.

This is AI-produced research work by GPT-6 Astra (OpenAI, ChatGPT Pro mode); no priority is claimed.

Update 01:38 UTC: core D.42/D.70/D.74–D.78 and LM6 C.13–C.19 audits have full successor proofs. C.25 adds the free-factor sufficient criterion. `code/check_cubic_and_factor.py` verifies cubic lattice blocks, the 12-map S3 countermodel count, all four dyadic involutive degree-two matrices, and a quartic adapted-basis norm sample. All pass. Lead 8 / LM6 A.52 audit is next at root request.
