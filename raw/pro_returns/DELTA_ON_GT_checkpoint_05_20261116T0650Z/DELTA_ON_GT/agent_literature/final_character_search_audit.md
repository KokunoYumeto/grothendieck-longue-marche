# Focused character search and final hypothesis audit

Checked 16 November 2026. This supplements `source_audit.md`; it does not replace the earlier bibliography audit or claim that an exhaustive literature search is possible.

## Finding

No opened primary source in this focused search proves that every finite quadratic character of **full profinite** GT which vanishes on the Galois image is zero. No opened source identifies the harmonic and equianharmonic modular frame signs on all full profinite GT. This is a bounded search finding, not a theorem that such a result does not exist, and not a novelty claim.

There is a more precise remaining route than an abstract abelianization computation. Ihara's full profinite Kummer character at 3 has an integral coefficient-two realization in an index-three cover of the free profinite group. Our independent KM.1–KM.3 prove that its half modulo two is defined on the actual multiplier-one gentle group and is visible in an explicit order-twelve affine quotient. The Gaussian frame instead uses a diagonal order-three component. Equating these components, or equating either with the five-point integer character, remains a separate assertion. The complete proof and conventions are in `Kummer_mixed_component.tex`.

KM.3 was independently checked by the five-point auditor. KM.5 gives an explicit integral coefficient-ring countermodel to deducing the diagonal sign from gamma factorization, reflection, and off-diagonal logarithmic data alone. It uses an order-three-character idempotent in the coefficient-two completed group ring. It is explicitly **not** a constructed GT element and is not evidence that the desired full pentagon comparison is false.

## Concrete sources checked

### The new dihedral quotients of full profinite GT

Bortnovskyi, Dolgushev, Holikov, and Pashkovskyi, *Accessing non-abelian quotients of the Grothendieck–Teichmueller group via elementary tools*, arXiv:2405.11725v3, **6 August 2026**, was opened in full HTML. Theorem 5.3 and Corollary 5.4 give finite quotients receiving surjections from Galois; Theorem 5.7 does the same for their inverse limit. The maps already exist on gentle GT. Proposition 5.8 identifies the limit with

\[
Q_2=\{(k,u)\in\mathbb Z_2\rtimes\mathbb Z_2^\times:
 k\bmod2=\epsilon_5(u)\},
\]

where \(\epsilon_5((-1)^a5^b)=b\bmod2\).

Our immediate deductions are useful limitations. Projection to \(u\) has kernel \(2\mathbb Z_2\); the commutator of \((1,5)\) and \((0,-1)\) is \((2,1)\). Therefore \(Q_2^{\mathrm{ab}}\cong\mathbb Z_2^\times\). Also, R4's nonzero character on gentle GT cannot factor through \(Q_2\): it vanishes on Galois, which surjects onto \(Q_2\). A factorization of its **restriction to full GT** would suffice for vanishing but is not supplied by this theorem.

Primary URLs: <https://arxiv.org/abs/2405.11725>, <https://arxiv.org/html/2405.11725v3>. Retrieval references: `turn134view0`, `turn135view0`, `turn136view0`–`turn136view4`, `turn137view0`–`turn137view2`.

### Extension of representations is not uniqueness of characters

Bleher, Chinburg, and Lubotzky (2022), *On representations of Gal(Qbar/Q), GT-hat and Aut(Fhat2)*, Journal of Algebra 607, 134–159, was opened in its complete 19-page primary arXiv manuscript. Theorem 1.2 extends certain arithmetic Tate-module representations to **finite-index subgroups** of Aut(Fhat2); Theorem 1.1 is an elliptic-curve instance. The introduction recalls that abelian Galois representations extend to full GT. Existence of extensions says nothing about the kernel of restriction on character groups. It therefore does not identify either modular frame sign or rule out a relative quadratic character.

Primary: <https://arxiv.org/abs/2004.08860>, <https://arxiv.org/pdf/2004.08860>. Version 3, 10 June 2021; published DOI 10.1016/j.jalgebra.2021.06.005. Retrieval: `turn134view1`, `turn135view1`.

Chinburg's January 2024 ICTS slides were also opened, especially slide 23. Their proposed modular-form extension imposes three explicit stability/lifting hypotheses. They state that a lift, when it exists, is unique **up to a quadratic character**. This is an ambiguity, not a theorem killing that character or identifying the present two frame normalizations.

Primary slides: <https://www.icts.res.in/sites/default/files/seminar%20doc%20files/Ted%20Chinburg%2004.01.2024.pdf>. Retrieval: `turn141view1`, `turn142view1`.

### The precise full profinite Kummer and gamma boundary

Schneps (2006), published p.657, displays Ihara's full profinite formula

\[
 \rho_n(f)=\frac1n\sum_{i=0}^{n-1}
 (\zeta_n^i-1)A_f(\zeta_n^i,1),\qquad
 f\equiv A_f(x,y)[x,y]\pmod{F''}.
\]

The displayed page was visually checked and saved. Adjacent typography incorrectly gives the additive character a unit-group target and uses the wrong root-of-unity subscript in the Kummer interpretation. KM.1–KM.2 remove this ambiguity by proving the index-three Schreier-coordinate formula. The geometric implications in Schneps's Theorem 3.4 are explicitly for the subgroup defined by additional five- and six-point special-locus equations; they are not asserted for all GT.

Primary published PDF: <https://webusers.imj-prg.fr/~leila.schneps/automorphisms.pdf>. Retrieval: `turn150view0`; local visual source: `schneps_657.png`.

Ihara's **original** beta/gamma II manuscript was recovered from RIMS as PostScript, converted without modification, and read in full. Its introduction recalls the full-profinite pentagon theorem giving
\(B(s,t)=\Gamma(s)\Gamma(t)/\Gamma(s+t)\).
Anderson's multiplication formula is instead an additional condition defining \(\mathrm{GT}_A\). Section 2 distinguishes its logarithmic-derivative condition, proves the stated inclusions among \(\mathrm{GT}_K,\mathrm{GT}_A,\mathrm{GT}_{A'}\), and explicitly warns that the derivation has a **nonconstant kernel involving different prime components**. Consequently the opened factorization theorem cannot simply replace the coefficient-two/order-three unit by its logarithmic Kummer data.

Primary source: <https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1224.ps.gz>; source index <https://www.kurims.kyoto-u.ac.jp/preprint/preprint_y1999.html>. Local full files: `ihara_RIMS1224.ps`, `ihara_RIMS1224.pdf`, `ihara_RIMS1224.txt`. Published metadata are independently confirmed on Ihara's RIMS publication list: J. reine angew. Math. 527 (2000), 1–11. The original beta/gamma **I** manuscript was not obtained; its theorem is reported here through its author's explicit account in II, not through an assertion that I's proof was inspected.

### Domain exclusions

Sharifi's *Soulé characters in the work of Ihara*, Theorem 2 and Proposition 4, was opened in full. Its groups are arithmetic Galois groups unramified outside a prime and infinity, with cyclotomic-twist coefficients. It is not a computation of \(H^1(\widehat{\mathrm{GT}},\mathbb F_2)\). The index three in our \(\rho_3\) denotes the rational number 3, not the weight of a Soulé character. Primary: <https://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/2120-11.pdf> (`turn139view0`).

The newly indexed Goto–Ishii preprint arXiv:2610.21052 concerns local restrictions of elliptic Soulé characters arising from **pro-p** Galois actions. Its primary abstract and the author's publication list were located; direct full-paper retrieval failed. No full theorem from it is asserted or treated as a full-GT comparison. Nakamura–Tsunogai II (2006), Contemporary Mathematics 416, 197–211, was located in primary publication metadata, but the AMS full-text endpoint was inaccessible. The already opened NT2002 and NTY2010 formulas retain their earlier carefully stated domains.

## Independent review of assembled new claims

The following judgments concern the stated hypotheses and the actual proofs, rather than an assumption that a finite computation proves a profinite lifting result.

| Claim | Independent judgment and indispensable scope |
|---|---|
| M3 / assembled A.62 | The two maps use the same positive loops: level-two inclusion sends \((x_L,y_L)\) to \(((rs)^2,(sr)^2)\), while the open map sends them to \((s,sr)\). The real basepoint transport changes only the already removed inner ambiguity. Conjugation of the arithmetic image by \(\kappa=\sigma c\) preserves it **as a subgroup**; no identification of individual old/new Galois labels is required. The conclusion is \(D_P(g)=cgc\), not literal fixedness. The real-algebraic fixed-field argument proves the needed Galois centralizer directly. The compact Kummer witness disproves only the current-marking fixed-point assertions. |
| M6 / assembled A.65 | The original quotient is identified with GF0, with an existential even parameter \(\kappa\); HF0 is equivalent by the normalized pure frame. GF1 needs the displayed additional V comparison, and HF1 needs IV-bis. The text correctly makes these conditional inclusions between equation loci. It does not identify this \(\kappa\) globally with Ihara's \(\rho_3\) or infer the extra equations from the pentagon. |
| AD.1–AD.3 / assembled A.71–A.73 | The signed covariance uses an actual gentle braid automorphism as supplied. The local ring is \(\mathbb Z_\ell\), so the nonabelian-image argument validly excludes the degenerate braid solution. Equal exponent sums kill the central ambiguity in the signed lifts. The claimed failure of surjectivity concerns the literal full projective norm-one targets and follows from the level-four restriction; it makes no assertion about the exact image in the smaller restricted target. The mod-four frame values can be justified directly by the frame abelianizations and commuting order-two images of \(x,y\), as recorded in `AD_adelic_audit.md`. |
| PC.1 / assembled P.13 | Valid under **R1, R2, R4 and the actual lift LP.5**. For each finite \(\ell\)-quotient of \(F\), the image of \(U\) is nilpotent; hence \(R_{\rm nil}(U)\subseteq O^\ell(F)\). R2 is identity on the actual relative pro-\(\ell\) quotient. Centralizer uniqueness then makes its complete normalized pro-\(\ell\) parameter trivial, so multiplying the lifted counterexample retains its pentagon defect. The two cases selected by the existing character supply both sign fibers without guessing the value on the first lift. No equality between full GT and the character kernel is inferred. |

No remaining claim stronger than its proof was found in these four items on this review. Their explicit supplied-result dependencies must remain visible.

## Search boundary

Both available search engines were used. The focused combinations included full/profinite Grothendieck–Teichmüller with `abelianization`, `relative abelianization`, `finite order characters`, `quadratic character`, `Kummer 3`, `rho_3`, `half Kummer`, and `modulo 2`; follow-up searches were restricted to the concrete primary leads above and their exact cited papers. The newer dihedral paper's actual **v3 date** was checked, rather than retaining the January 2026 v2 date found in an index. The search does not substitute GT1, GRT, a pro-unipotent quotient, or a pro-ell quotient for full profinite GT.

The final unproved comparison is now stated in finite, convention-sensitive terms in KM.4 and the five-point audit. Whether the full profinite pentagon forces that comparison remains under investigation; no literature-only resolution was obtained here.
