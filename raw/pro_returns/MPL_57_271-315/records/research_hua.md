# Research check of the two Hua findings

This is a statement-level comparison with the transcription frozen by the root reader at 2026-11-16 19:18:43 UTC. No manuscript image was consulted and no transcription or per-scan record was edited. The intake entries in `context/notes/RESULTS_STATE.md`, under “Findings of another project on these pages, to check,” are AI-produced claims with intake “new to us: our package for this cote is waiting”; this check does not upgrade their status or independently verify a mathematical theorem.

## H1 — Hua, findings register, `57-ns-p-divisibility-generization`

**Exact current source:** `MPL_57_271-315/MPL_57_271-315_transcription.tex`, cote 57, scans 289–290, manuscript footers 288–289.

**What the pages assert.** Scan 289 sets up an abelian scheme over the spectrum of a discrete valuation ring, with closed and generic fibres indexed 0 and 1, and finite subgroup schemes F and G. With A=X/F and B=X/G, it constructs a homomorphism u from the factorization of pβ and explicitly asserts `u₁∉p Hom(A₁,B₁)` but divisibility of u₀ by p. The stated explanation is the contrast between `F₁⊄G₁` and `F₀⊂G₀`.

Scan 290 then takes `C=A×B′`, where B′ is declared dual to B, displays the decomposition of its relative NS object with a `Hom(A,B)` factor, and places u in that factor with its other two components zero. Its explicit conclusion is “sur la fibre … spéciale, on a” `ū₀=pv̄₀`, whereas “on ne peut avoir” `ū=pv̄`. Thus the register's central description of special-fibre p-divisibility without global p-divisibility is directly supported as a manuscript assertion; the preceding scan states the stronger generic nondivisibility used in its argument.

**Correction to the register's scope.** The elliptic-curve construction is explicitly said to work “en égales ou inégales car” on scan 289. The register's restriction to mixed characteristic is therefore narrower than the manuscript's stated intention: the page claims both equal- and unequal-characteristic realizations. The stated construction uses a special elliptic fibre without a point of order p and a generic fibre with such a point, together with two distinct rank-p subgroup schemes on the generic fibre whose specializations coincide.

**Proof boundary.** This is corroboration of the assertion and its intended mechanism, not a new complete proof of the construction. The frozen text retains uncertain subgroup indices and an unresolved target in the special-fibre Hom expression; its displayed relation (iii) and the continuation's subgroup wording must not be silently normalized to obtain a clean proof. Nothing in this check changes those readings.

**Literature boundary supplied by the root reader.** The independently checked primary-paper comparison is consolidated in final research notes E05 and E08. This local Hua check did not independently reopen that paper; its citations are not an additional verification.

## H2 — Hua, findings register, `57-analytic-pic-completion-criterion`

**Exact current source:** `MPL_57_271-315/MPL_57_271-315_transcription.tex`, cote 57, scans 271–272, especially scan 272(ii)–(iii). The register also cites earlier pages outside this selection; the comparison below is only with the supplied overlap.

**What the pages actually contain.** Scan 271 is a reused typescript defining divisors, linear equivalence and linear systems; it does not state a Picard-completion criterion. Scan 272 is headed “Questions” and starts with a noetherian henselian local ring A that is also a “bon anneau,” described using regularity of the completion map, and X proper over A with `X̂=X⊗A Â`.

Item (ii) assumes `supp R¹f*(O_X)⊂{y}`, gives the example that X is unchanged away from y, and asks “Est-il vrai alors que” the map from `Pic(X)` to the Picard group of a completed object is an isomorphism, followed by “??”. The target remains the frozen alternative `Pic(Ŷ|X̂)`; this research check does not select or repair it. Item (iii) asks the analogous comparison for `Y−{y}` and its completed punctured counterpart at an isolated singularity, links this conditionally to (ii) and resolution, and ends with a question about an analytic algebra when the singularity is not isolated.

**Supported overlap.** The scan supplies a question in the sufficiency direction: a support condition on first coherent direct-image cohomology is proposed as a reason for a Picard-completion comparison to be an isomorphism. Interpreting that support condition as finite length uses the usual finite-module/coherent local setting; that interpretation should be labeled separately from the actual wording, which does not say “longueur finie.”

**Not supplied by these two scans.** They do not state the register's general proper-complex-analytic setup, the precise germ group `(R¹f*O_X*)_y`, the target `lim Pic(X_n)`, or the necessity direction of an “if and only if.” Nor do they prove the sufficiency question they do ask. Consequently the full Hua formulation is **not locally verified and not locally refuted**: it may depend on the earlier cited pages that are absent here. It must not be promoted to a theorem or attributed in full to scans 271–272 alone.

## C — Context comparison: Pic⁰, Picτ, and the whole Picard group

**Exact context:** `context/MPL_16+47+54+44_transcription.tex`, cote 16, scan 19, equations (8.13)–(8.16), and scan 21, equation (8.7). Context status remains “not yet second-passed; claims,” following `context/README.md`. `context/MPL_16+47+54+44_notes.md`, entries `16:19:1`–`16:19:4`, are unreviewed leads and explicitly flag the absent preceding hypotheses.

Cote 16, scan 19, defines `Pic(U)⁰` using the neutral component and `NS(U)` as the quotient by that component. It then identifies NS(U) with a **finite** intersection-matrix cokernel and gives a discriminant pairing, while its final paragraph asserts only prime-to-characteristic divisibility of `Pic(U)₀`. Scan 21 separately retains the ℓ-primary torsion in its NS/cohomology comparison. These passages show why the quotient and prime must be specified when comparing an integral p-divisibility claim.

By contrast, the current cote 57, scan 275, defines `Picτ` by fibrewise numerical triviality with the explanation that a multiple deforms to zero, and forms `Pic/Picτ`; scan 309(b) again writes that quotient. The finite discriminant group arising from quotienting by Pic⁰ in the cote-16 fragment cannot simply be identified with this quotient by Picτ. This is a source-level distinction, not a claim that the two quotients differ in every abelian-scheme instance of scans 289–290.

The completion question on scan 272 concerns the **whole** Picard group. Neither the neutral-component discussion in cote 16 nor the numerical component in later cote 57 supplies the missing passage from a coherent support hypothesis to the full analytic iff claimed by the register.

## Search record

- Read both exact Hua entries and their status preamble in `context/notes/RESULTS_STATE.md`.
- Searched the frozen current TEX for scan markers 271, 272, 289, 290; then read their full text. Searched `longueur`, `supp.*R`, completion/Picard terms, `analyt`, `NS` and `Picτ`; only scan 272 supplied the relevant completion question.
- Searched context TEX and notes for `Pic(U)`, `Picard`, `8.14`, `8.15`, `8.16`, `torsion`, `analyt`, `complétion`, `finite length` and `longueur finie`; directly read cote 16, scans 19 and 21, plus notes `16:19:1`–`16:19:4`. No duplicate statement of the full analytic iff was found in the supplied context.
