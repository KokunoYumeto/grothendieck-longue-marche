# Part E: §50 and the first Fermat example

| Requested item or task | Outcome | Statements | What is established and what remains |
|---|---|---|---|
| Item 5 | partly settled | E.1–E.14 | Exact integrality claims are decided; positive-power and envelope universal theorems are proved for closed linear targets over every ring. The original non-linear scope is retained in E.11. |
| Lead 3 | refuted | E.3–E.8, E.12–E.19 | The envelope is a virtually abelian quasi-unipotent envelope. It is not the full pro-algebraic or Malcev completion, nor its divided-power integral form. Correct maps and separating examples are supplied. |
| E.a | partly settled | E.1–E.3, E.6–E.7, E.11 | Q-algebra theorem for closed linear groups; exact divided-power criterion over torsion-free rings; genuine integral and all-prime smooth Z/p² counterexamples. Arbitrary non-linear targets remain explicit. |
| E.b | refuted | E.4–E.8 | Both principal integrality readings have executed counterexamples. Every degree 1–12 in two specified families is tested at 2, 3, 5. Correct integral-X and sharp p² results are proved. |
| E.c | partly settled | E.8–E.11 | All-ring closed-linear positive-power theorem and the affine dilation proposition are proved. General separated locally finitely presented targets remain outside the proof. |
| E.d | partly settled | E.12–E.14, E.18–E.19, E.11 | Integral construction, fibres, and the linear-target universal property are proved. Maps and separating examples cover the named hulls in their specified domains; no unrestricted general integral Hall/Lazard functor is invented. |
| E.e | partly settled | E.15–E.20, E.24–E.25 | Full and finite-stage models, coordinate rings, fibres, points, and order-12/order-24 relative comparisons are explicit. Fine automorphism parameters and the rational positive-sign group are computed. Two asserted automorphism identifications are false; the remaining named-functor comparison is precise. |
| E.f | proved | E.21–E.22 | Nilpotent, pro-p and rational unipotent assertions proved independently; the S₃ covering calculation executed; the modular envelope retains S₃. |
| E.g | proved | E.18, E.23 | The two rational theories and the integral envelope are compared on the requested group itself. Algebraic goodness and a separating 12-dimensional representation are supplied. |
| After BISITE: Stallings lead | proved | E.21–E.22 | Mathematical assertion proved; historical motivation is not inferred from it. |
| After BISITE: two rational theories | proved | E.23 | The cited theorems are verified and reduced to B𝔖, with all three resulting objects distinguished. |
| After BISITE: Fermat relative completion | partly settled | E.19–E.20, E.24–E.25 | The order-12/order-24 modular relative completion with abelian kernel gives the rational finite stage. Comparisons for the general targets (Z/n)² and S₃×Ẑ* remain absent; the first finite deck test q₂: free F₂→(Z/2)² is now specified in E.20. No unrestricted tower identification is claimed. |

The section has **25 numbered statements: 16 Proved, 6 Refuted, 1 Known, and 2 Open**. “Open” in E.11 and E.20 means unproved in this work, not a claim that the corresponding question is open in the literature. Every partial task has its proved cases, executed computations, precise missing assertion, and first not-covered test on the page. No statement claims that every original question has been proved.

## Sources actually read

We read the checked transcription packages `LM_C4-001-019` and `LM_C4-020-038`, and the relevant continuation through scan 43 in `LM_C4-039-057`. We read the supplied BISITE B.11 and GALOIS C.13–C.14 as statements to verify, not as authorities. The source notes were used to locate questions; their mathematical assertions were not adopted without proof.

Photographs inspected directly for the mathematical readings include C4 scans **5, 6, 9–16, and 29–41**. The attached photograph set has no scans 17–28. Consequently the finite-stage construction and the definition of “métabélien” at scan 25 were read from the checked transcription, with this limitation stated in the reading register. Their mathematical content is independently reconstructed and proved from explicitly stated data. No final palaeographical determination is claimed.

Primary research sources opened and used are:

- Bhargava (2009), the supplied PDF, §1, especially p. 964. The Z-binomial case is proved directly in E.8; a general P-ordering theorem is not invoked without need.
- Hain (1998), the original Numdam article, §1, pp. 47–48, where relative completion and its universal property are stated. E.19 proves the abelian-kernel calculation directly. No Hodge-theoretic conclusion is imported.
- Rivera, Wierstra, and Zeinalian (2021), author-hosted revised article and arXiv manuscript, Theorem 3, repeated with proof as Theorem 16, and Corollary 21. E.23 gives the reduction to the classifying space B𝔖.
- Toën (2006), April 2006 arXiv version 6 and author-hosted text: Lemma 3.3.2, Theorem 3.3.4, Corollary 3.3.7, Definition 3.4.1 and the following examples. The publisher page was also opened to verify the publication data, including pages 39–134. E.23 proves algebraic goodness for the specified virtually abelian group before concluding that its schematization is a classifying stack.

Every entry in `E_refs.bib` is marked **verified**, with exactly what was opened. The original Stallings paper was not used as an authority: the particular nilpotent and pro-p assertions needed here have an independent proof. Hall, Lazard, Hochschild–Mostow and divided-power terminology is used only with explicitly defined universal properties or the explicit abelian models; no unopened theorem is silently cited. We searched the primary sources and relevant completion, schematization, integer-valued polynomial and relative-completion terminology. We claim no priority or novelty.

## Main mathematical corrections

### The unipotence question and the dubious lemma

The source definition matters. A value at 1 of a homomorphism from Gₐ in characteristic p has order dividing p. Thus an element of order p² in W₂ is not a counterexample to the source's own hypothesis. E.7 gives an appropriate replacement: for every prime p the smooth affine line over Z/p² with group law

\[
F_p(x,y)=x+y+p\,C_p(x,y),\qquad
C_p(x,y)=\frac{(x+y)^p-x^p-y^p}{p},
\]

has special fibre Gₐ and section 1, but that section is not the value of any Gₐ homomorphism. The proof rules out every polynomial degree; the finite searches are verification and discovery tools, not substitutes for the proof. The section has order p, so it does not refute the positive-power theorem.

The actual exponential-integrality implication fails already in rank 3: with J the rank-three nilpotent Jordan block, X=J−J²/2 has integral exp(X) and exp(−X), but X is not integral. The subsequent displayed signed sum drops the linear term; that is a different assertion, and E.5 gives its rank-four counterexample. Adding the hypothesis X integral makes the rank-four signed assertion true, with a proof on D(2) and D(3).

The stronger fibrewise question over Z has a genuine rank-five counterexample. Let N be the weighted shift with weights 1,2,3,2. Then I+N is a Gₐ value on every geometric fibre, log(I+N) is integral, but its fourth divided power is E₁₅/2. More generally, the correct local rank bound is r≤p² under Nᵖ∈pMᵣ and Nʳ=0. The first obstruction in the general weighted family has degree p², and the bound is sharp. This explains why the first genuine weighted obstructions in the executed degree-12 range occur at degrees 4 and 9 for p=2 and p=3, while none occurs for p=5 in that range.

The Q-algebra assertion and the integral coefficient criterion are fully proved for closed linear targets. E.10 proves the positive-power theorem for closed linear finitely presented groups over **every commutative ring**, including nonreduced and mixed-characteristic bases. The proof obtains a uniform exponent using compactness of the constructible spectrum, produces an integral binomial one-parameter subgroup, and then kills torsion in finitely many defining equations by another dilation. It does not rely on the false integrality lemma.

### The actual envelope

The source's “métabélien” means finitely generated **virtually abelian** in §50. The modern derived-length-two condition is different. E.12 starts with a normal lattice M≅Zʳ of finite index in Γ, a section of H=Γ/M, its action matrices and its integral 2-cocycle. This constructs a smooth finite-stage scheme with coordinate ring

\[
\prod_{h\in H}\mathbb Z[x_1,\ldots,x_r].
\]

The full envelope has coordinate ring

\[
\varinjlim_n\prod_{h\in\Gamma/nM}\mathbb Z[x_1,\ldots,x_r],
\]

with the explicit affine transition substitutions. Its kernel over the proconstant full profinite completion has coordinate ring Z+(x₁,…,xᵣ)Q[x₁,…,xᵣ]. Each special fibre is the proconstant profinite group, reduced of dimension zero. A finite stage instead remains smooth of relative dimension r in every characteristic.

E.14 proves the universal property for quasi-unipotent representations into closed linear finitely presented targets over every ring. The Hom expression is a **direct** limit of finite-stage Hom sets, correcting the inverse-limit arrow in scan 31(58). The proof explicitly ensures that the one-parameter maps commute with all lattice images before applying the cocycle pushout.

The full pro-algebraic completion maps to this envelope, which maps to the unipotent completion. Equality fails already for Γ=Z: E_Z over Q is Gₐ×Ẑ, whereas the character n↦2ⁿ belongs to the full pro-algebraic theory. The rank-one Hall/Lazard additive model and the usual divided-power polynomial algebra are also different. For Hain's relative completion over a finite quotient there is a compatible map from the envelope. For the nonfinite reductive quotient Z→Gₘ, n↦2ⁿ, the relative completion is Gₐ×Gₘ, and there is no compatible map in either direction between it and Gₐ×Ẑ. These statements are proved by their universal properties and explicit separating quotients.

### The modular example, points and automorphisms

For 𝔖=SL₂(Z)/[Π₀,Π₀], the lattice has rank 2 and the finite quotient H has order 12. Its action matrices are R=[[0,−1],[1,−1]] and S=[[0,1],[1,0]]. All 144 integral cocycle values are supplied, and all 1,728 associativity triples are checked. The finite-stage model is the disjoint union of twelve affine planes over Z; it is smooth at both 2 and 3. The order-24 GL₂ variant and orientation-reversing action −S are also verified.

The point distinction is substantial. For the full envelope,

\[
E_\Gamma(\mathbb Z_p)=\widehat\Gamma,
\qquad E_\Gamma(\widehat{\mathbb Z})=\prod_p\widehat\Gamma.
\]

For a finite stage, the common-component subgroup of its Ẑ-points is Γ̂. That is the Δ superscript in scan 35(13); deleting it changes the assertion. The finite-stage rational model is the completion of SL₂(Z) relative to H after abelianizing its unipotent kernel. The full envelope is larger in its finite component information.

The fine parameter scheme of scan 41 is computed rather than identified with the envelope. For each fixed sign pair it is

\[
\operatorname{Spec}\mathbb Z[a,b,k,(12k+6\nu_2+4\nu_3+1)^{-1}],
\]

smooth of relative dimension 3 even at 2 and 3. Over Q, the actual automorphism group with both conjugators in the normal vector subgroup and with the stated loop relation is Gₐ⋊Gₘ, with composition (t,μ)(t′,μ′)=(t+μt′,μμ′).

Two further manuscript assertions fail. Over F_p[ε]/ε², the nonidentity polynomial automorphism

\[
(v,h)\longmapsto(v+\epsilon(v^{[p]}-v),h)
\]

fixes every discrete element of 𝔖 and preserves the loop line. Thus the values on ρ and σ do not determine the full automorphism functor over arbitrary bases. Imposing linearity on the normal vector subgroup is a sufficient correction, proved over every base. Moreover, over Q the identity automorphism has both 1 and (−1/3,1/3)τ as allowed ρ-conjugators of opposite orientation. The proposed ε₃ is therefore not recoverable from the automorphism alone; keeping that sign adds parameter data. Both observations were independently reviewed against the source conditions, and their exact calculations are executed.

### Coverings and the two rational theories

The endomorphism x↦x, y↦y[x,y] induces automorphisms on every nilpotent quotient, all pro-p completions, and rational unipotent completion. The proof uses its identity action on the lower-central graded group, the finite p-group Frattini argument, and a proof of the relevant profinite Hopfian property. The S₃ permutation action changes from one orbit of size 3 to orbits of sizes 2 and 1. The modular envelope retains that S₃ quotient through reduction modulo 2. This proves the mathematical lead without asserting a historical motive for the passage in §50.

On B𝔖, the Rivera–Wierstra–Zeinalian theory retains the discrete group. Toën's schematization is BP_Q(𝔖): E.23 proves the necessary algebraic goodness through the finite-index lattice, not merely the fundamental-group assertion. The integral envelope has the quasi-unipotent representation theory. An induced 12-dimensional rational representation whose λ₀ eigenvalues include 2 proves that the full pro-algebraic theory is strictly larger on this very group. Since 𝔖 is residually finite, these distinctions do not amount to a nontrivial kernel on the embedded discrete group.

## Executed programs and reproducibility

Run from the project directory, in this order:

```text
python code/E_integrality.py > code/E_integrality.out
python code/E_envelope.py > code/E_envelope.out
python code/E_automorphisms.py > code/E_automorphisms.out
python code/E_registers.py > code/E_registers.out
```

Python 3 and SymPy are used; all arithmetic is exact. Each mathematical program also writes a JSON output with complete matrices, finite tables or search rows. No floating-point evidence is used.

`E_integrality.py` checks the rank-three exponential counterexample; finds the rank-four signed counterexample after 168 candidates in a recorded finite grid; tests all 72 combinations of two matrix families, degrees 1–12 and primes 2,3,5; checks binomial-basis denominators; verifies W₂ group laws and element orders; searches all 1,024 Z/4 polynomials of degree at most 6 with the required two values; verifies the all-prime deformation examples at 2,3,5; and tests the A|K and 3!|6! readings of scan 13. A failed cubic-identity assertion during development exposed an unevaluated symbolic expression, not a mathematical counterexample; the final test expands the polynomial first and passes. The attached output is from the final successful run.

`E_envelope.py` enumerates SL₂(Z/4), GL₂(Z/4), their normal V₄, the quotient H, all cocycle entries and associativity triples; checks the finite quotients 𝔖/nM for n=1,2,3,4,8,9; computes all requested finite-field counts for the finite stage; constructs the induced rational representation and verifies its defining relations; and verifies the S₃ covering orbits.

`E_automorphisms.py` checks the coarse and augmented matrix minors; the explicit integral three-parameter solution; counts the fine scheme over the requested finite fields and rings; tests all 48 finite sign-alternative cases; checks the rational automorphism relations and composition; verifies the opposite-sign centralizer; and checks the nontrivial ε-Frobenius automorphisms as polynomial identities, including all twelve actions and all 144 cocycle values at each of p=2,3,5.

`E_registers.py` builds and audits the 25 statement rows, 25 mathematical reading rows, and 12 task-coverage rows. The degree-12 search is explicitly a search over two specified families; it is not presented as an impossible exhaustive enumeration of all rational matrices.

## Exact residuals

**E.11:** extend the section-extension and positive-power results from closed linear finitely presented targets to arbitrary separated locally finitely presented group schemes over a quasi-compact base. The missing step is an appropriate faithful finite locally free linear realization, or a replacement argument. The first quantified base-dimension-zero tests left outside this proof are arbitrary affine finitely presented targets over Q[ε]/ε² and Z/4, without a specified closed linear embedding. The proven Q-linear, torsion-free integral and all-ring positive-power cases, and every executed counterexample/search, are listed in E.11. These bases are precise first not-covered tests of this proof, not claimed minimal counterexamples or literature-open problems.

**E.20:** compare each exact signed M_{ρ,σ}/N_{ρ,σ} functor with the appropriate automorphism functor, specifying whether it imposes linearity, remembers conjugators and signs, or takes an fppf quotient of the fine parameters. The generic positive-sign group and all fine-scheme fibres have been computed; the unqualified generator and sign identifications are disproved. The first named signed comparison in the requested residue-characteristic list still not established here is over F₂ with both local conjugator and sign data included. A complete answer cannot replace this question with the already computed underlying envelope group.

The distinct group-scheme half of the Fermat-tower follow-up retains the targets **`(Z/n)²` and `S₃×Ẑ*`**. E.19 proves the order-12/order-24 modular comparison only. For the first nontrivial finite deck case, fix the free group F₂=⟨x,y⟩ and q₂:F₂→(Z/2)² by x↦(1,0), y↦(0,1). The rational relative completion of this specified map, or its quotient with abelian unipotent kernel, has not been compared with a specified M_{ρ,σ} or N_{ρ,σ}: the comparison map, compatibility, image and kernel remain absent. Here F₂ denotes a free group, independently of the field F₂ in the preceding residual. The S₃×Ẑ* version also requires the actual tower fundamental group and its continuous quotient map, together with the proconstant target or the compatible finite targets S₃×(Z/m)*. These source and comparison data are not supplied by q₂ or by the order-12/order-24 calculation. The proved modular case, executed finite cocycle computations, generic automorphism identification, and explicit counterexamples are the partial results; no equality of unspecified tower completions is asserted.

The report and proof section are AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). They attribute no new result to a person and claim no priority.
