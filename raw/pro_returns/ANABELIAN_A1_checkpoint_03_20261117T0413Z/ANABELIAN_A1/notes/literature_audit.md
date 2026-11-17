# Literature audit: A10, A11, A14, C4

Work in progress. This is an independent source audit, not a proof of the main theorem. Mathematical conclusions depending on AG.40–42 remain conditional until the separate audits finish. We claim no priority.

## Verified source inventory

All the following primary sources were opened on 17 November 2026. The external PDFs and text extractions are in `../sources/` for checking; the task's three supplied LaTeX sources remain in `background/literature/`.

| Source | Opened location | Source reference | Exact passages read |
|---|---|---|---|
| Mochizuki, *Absolute Anabelian Cuspidalizations of Proper Hyperbolic Curves*, June 2007 original author version | https://www.kurims.kyoto-u.ac.jp/~motizuki/Absolute%20Anabelian%20Cuspidalizations.pdf | turn2view1 | §§0–1 definitions; Proposition 1.8(ii) and proof; Definition 1.18; Theorem 3.10; relevant dependence cross-references |
| Same, LaTeX version | https://www.kurims.kyoto-u.ac.jp/~motizuki/Absolute%20Anabelian%20Cuspidalizations%20(LaTeX%20version).pdf | turn1view3 | Corresponding Proposition 1.6(ii), definitions and central-extension construction |
| Mochizuki, Comments, February 2014 | https://www.kurims.kyoto-u.ac.jp/~motizuki/Absolute%20Anabelian%20Cuspidalizations%20(comments).pdf | turn2view0, turn4view2 | Complete two pages, all four corrections |
| Mochizuki–Tamagawa, *The Algebraic and Anabelian Geometry of Configuration Spaces*, July 2007 author version, published 2008 | https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Algebraic%20and%20Anabelian%20Geometry%20of%20Configuration%20Spaces.pdf | turn4view3 | Introduction; Definition 1.1; Proposition 2.2 and complete proof; related exact-sequence uses |
| M–T Comments, April 2015 | https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Algebraic%20and%20Anabelian%20Geometry%20of%20Configuration%20Spaces%20(comments).pdf | turn2view2 | Complete one page |
| Saïdi–Tamagawa 2009 journal version | https://www.kurims.kyoto-u.ac.jp/~prims/pdf/45-1/45-1-5.pdf | turn16view1 | Numbering comparison, §§1–2 claims, Theorem 2.6, Remark 3.14 |
| Saïdi–Tamagawa 2009 arXiv text | Supplied `src_arXiv_0801.1452/main.tex` | User-provided source | §2 and Remark 3.13, inspected alongside journal |
| Saïdi–Tamagawa 2017/2018 | Supplied `src_arXiv_1708.08773/finite-final.tex` | User-provided source | §3 review and comparison with 2009 |
| Wakabayashi 2016 | Supplied `src_arXiv_1507.00622/wakabayashi_cuspidalization.tex` | User-provided source | Introduction Theorems A–C, §1 conventions, Theorem 3.9, Corollary 3.10, Theorem 4.4 |
| Sun 2025, v2 (17 August 2025) | https://arxiv.org/html/2505.06826v2 ; https://arxiv.org/pdf/2505.06826v2 | turn2view3 | Definition 3.1, Corollary 3.2, Proposition 3.7, Corollary 3.8; §6 |
| Sun 2026, v1 (26 April 2026) | https://arxiv.org/html/2604.23485v1 ; https://arxiv.org/pdf/2604.23485v1 | turn2view4 | Introduction and geometricity criterion; further details being checked |
| Boggi–Zalesskii, arXiv version corresponding to 2019 publication | https://arxiv.org/pdf/1408.5419 | turn14view1 | Definition 1.1, Lemma 3.1 and complete proof |
| Stix 2005, *A monodromy criterion for extending curves* | https://www.math.uni-frankfurt.de/~stix/research/preprints/STIXMonodromyCriterionIII.pdf | turn16view0, turn18search26 | §2.3: relative pro-L quotient preserving the full base; direct PDF byte download returned HTTP 403 |
| SGA1, recomposed original French source | https://arxiv.org/pdf/math/0206203 | downloaded and read locally | XIII Corollary 2.9, §2.10, Lemma 2.11, Corollary 2.12; Proposition 5.2, Corollary 5.3 |

## Numbering corrections

The prompt and previous return conflate arXiv and journal numbering in two important places:

* The conditional configuration-space route and question whether the exceptional set is empty are **arXiv Remark 3.13 = journal Remark 3.14**, printed journal pp.177–178. Journal Remark 3.13 instead concerns extension of the Isom theorem to finitely generated fields.
* The maximal cuspidally pro-l reconstruction theorem is **arXiv Theorem 2.7 = journal Theorem 2.6**, journal p.164.
* For K1, Definition 1.3, Definition 1.5, Remark 1.2 and Proposition 1.8 have the same numbering in the supplied arXiv source and journal.
* Mochizuki's **original author Proposition 1.8(ii) = LaTeX/journal Proposition 1.6(ii)**; original Theorem 3.10 = LaTeX/journal Theorem 3.1. Specify the version whenever citing the original numbering.

## A10: the literal configuration assertion

### What the text actually says

Mochizuki's original Proposition 1.8(ii), printed pp.14–15, identifies the inverse image of a rational point decomposition subgroup under either projection from the configuration group with the indicated punctured-curve group. At the beginning of §1, the set Sigma is arbitrary subject to containing an invertible prime. At original p.11 the configuration geometric group is defined by first taking the maximal pro-Sigma quotient of the tame group and then its maximal cuspidally pro-Sigma-dagger quotient over the proper product. For a finite field of characteristic p and Sigma consisting of all primes other than p, Sigma-dagger equals Sigma. Every closed subgroup of a pro-Sigma group is already pro-Sigma, so that second operation does nothing. The analogous punctured-curve definition behaves the same way. Thus the literal assertion specializes to the full prime-to-p fibre identification; there is no singleton-prime convention that avoids this specialization.

Consequently, **if the independently proved R4 holds, it contradicts this literal assertion**, not merely a careless reading of it. Its proof invokes Stix §2.3. Stix completes only the fibre kernel and retains the full fundamental group of the base. Passing from that relative completion to simultaneous completion of both base and total group requires an additional argument; right exactness alone cannot supply the missing injection.

The 2014 Comments correct four other issues: decomposition-group recognition via all descended forms; the targets of two diagonal covers; replacing an asserted Kummer isomorphism by the injection actually needed; and replacing faithfulness of one cyclotomic action by infinitude of its image. They do not revise the fibre assertion.

### Scope that is already safe

Mochizuki–Tamagawa 2008 explicitly works with **PT-formations** (Definition 1.1): primary, or total. For the class of all finite Sigma-groups, these mean a singleton Sigma, or all primes. Proposition 2.2(i) requires that formation, invertibility on the connected base, and the stated cyclotomic/compactified-fibre mod-l monodromy images to be groups in the formation. Its proof uses the fact that the kernel of the pro-l automorphism action on mod-l abelianization is pro-l. Hence the statement does not include mixed prime sets omitting p. R4 would refute an extrapolation beyond its hypotheses, not Proposition 2.2 as stated.

Wakabayashi consistently fixes one invertible prime l and works with geometrically pro-l groups. Its configuration sequence is inside the primary scope; no full prime-to-p fibre sequence is asserted.

Saïdi–Tamagawa's conditional route is explicitly conditional. Refuting its proposed left exactness refutes the proposed sufficient route, not its Isom theorem. However the central and fixed-l cuspidal reconstruction inputs imported from Mochizuki require a separate limited repair audit; it is not enough to call the entire published proof unaffected merely because Remark 3.14 is conditional.

### Repairs under separate audit

The source uses the overly strong fibre identification as an intermediate assertion in Proposition 1.8(iii), Proposition 1.10 and its inverse-limit cuspidally abelian constructions, and again in the fixed-l construction behind Theorem 3.10. The fixed-r relative theorem AG.41 is tailored to the latter use. It does **not** repair the original full prime-to-p statement: it supplies a different quotient. A complete paper-level dependence check must distinguish the central, cuspidally abelian, and cuspidally pro-l consequences from that false full statement. No global claim that every proof in Mochizuki is repaired has yet been established in this audit.

## A11: Wakabayashi's actual theorem

Theorem A (proved as Theorem 3.9) fixes an invertible prime l and hyperbolic curves X/K, Y/L over finite fields. A Frobenius-preserving isomorphism between the geometrically pro-l groups of X minus x and Y minus y, carrying specified cusp decomposition groups to each other, extends to an isomorphism of their two-point configuration groups compatible with switching and the base isomorphism. Its ambiguity is inner automorphism. The resulting corollary transports cuspidalizations at other rational points whose decomposition groups correspond. Theorem C (=4.4) reconstructs all configuration groups from a Frobenius-preserving isomorphism of the geometrically pro-l curve groups, compatibly with projections and permutations.

These are reconstruction statements, not point-separation statements. They neither retain the full prime-to-p proper quotient in AG.40 nor by themselves establish AG.41's relative completion. A family of separately reconstructed pro-l quotients does not determine the mixed finite quotients of the prime-to-p group. In particular one cannot combine them with a finiteness theorem whose hypothesis is a cofinite Sigma by silently replacing a singleton Sigma with all primes other than p. Their stated conclusions do not conflict with AG.40–42.

## C4 and A14: the virtual-curve construction is in the literature

Sun 2025 Definition 3.1 already defines the virtual fundamental group by pulling a smooth surjective fundamental-group map back along a Galois section. Corollary 3.2 records the extension and independence of the geometric kernel from the section. For a family of hyperbolic curves, Proposition 3.7 identifies that kernel with the geometric fibre group; Corollary 3.8 identifies the pullback with the actual fibre group when the section is geometric. Thus attaching a virtual punctured curve to a section of a configuration-space group is not a new construction here.

The elementary group argument is worth recording independently. Given a continuous exact sequence `1 -> F -> E -> Pi -> 1` and a continuous section `s:G_k -> Pi`, the profinite fibre product `E_s = E x_Pi G_k` has exact sequence `1 -> F -> E_s -> G_k -> 1`. If `s_Q = Inn(gamma) s_P` and gamma lifts to d in E, conjugation by d identifies the two inverse images. If E also maps to the proper product and d has prescribed diagonal projection, the induced map on the other proper factor is Inn(gamma); composing with a geometric inner automorphism of the target fibre removes it. To preserve the new cusp, however, the lift must lie in a suitable diagonal boundary decomposition group. Exactness alone does not identify arbitrary boundary subgroups. That extra datum and its local construction are exactly what AG.42 supplies.

No claim is made that this pullback construction makes a nongeometric section geometric. An abstract extension can be defined without a corresponding punctured curve over k. The full characteristic-zero criterion and Sun 2026 geometricity hypothesis are being checked separately.

## SGA1 checks supporting A4/A5

XIII Corollary 2.9 uses a smooth proper morphism of finite presentation, a relative normal-crossings boundary, and coefficient primes excluding all residual characteristics. It gives the needed cohomological properness and local constancy for tame finite L-group torsors. Section 2.10 constructs specialization via strict localization and a path, with only inner ambiguity; Lemma 2.11 transports inertia. Proposition 5.2 states extension after extracting the indicated prime-to-residue-characteristic roots of boundary parameters over the **whole** regular Kummer chart, uniquely up to unique isomorphism. Its proof invokes purity after the codimension-one calculation. Thus the earlier concern that this only produces an extension at generic boundary points is not justified.

## Search scope and limits

Queries run included the paper titles; `prime to p point separation finite field anabelian exceptional set injective Saidi Tamagawa cuspidal configuration fundamental group`; `Mochizuki 1.8 configuration prime-to exact`; and the exact Stix title with §2.3. Both named recent arXiv preprints were opened in full. No independent published proof of universal prime-to-p point separation has been identified by these searches. This is a bounded search result, not a claim that none exists. Precise novelty of the relative fixed-r exactness or the AG.40 criterion has not been established.

## Update: exact J-large support theorem and stronger criterion

The supplied 2017 source, lines 1913–2250, is decisive. Definition 2.9 calls C almost Sigma-separated when the compositum F_C of the residue fields of E_C is proper in kbar. Proposition 2.12 assumes that Sigma is J_C-large, meaning that the Galois action on the omitted-prime Tate module has nonzero kernel (Definition 2.6). It proves support over a finite extension of the fixed field of that kernel. It does not prove that E_C is finite.

Its proof uses delta:C×C→J, off the diagonal, with geometric fibres of cardinality at most 2 (at most 1 if nonhyperelliptic). Two equal differences give P+Q′ linearly equivalent to P′+Q. If the divisors differ, they are fibres of the hyperelliptic degree-two pencil; the only second pair is (iota Q,iota P). This is explicitly linked to 2009 Claim 1.9(i), whose proof is written after a reduction to the nonhyperelliptic case. Taking squares of the omitted-Tate kernel kills its action on these at most two points. Thus the delta lemma and support-field idea are known predecessors.

Proposition 2.13 chooses an auxiliary prime l for which the Z_l tower, and every finite extension of that tower, meet every fixed finite extension of F_C in a finite field. Hence the exceptional rational points are uniformly bounded along the finite stages. Largeness permits l in Sigma union {p}; positive p-rank permits l in Sigma. The extra restriction is unnecessary for the following argument.

### A strengthening of the final criterion, independently derived

Use n=the exact order of [P−Q], so div(f)=n(P−Q), rather than requiring n=p^e or r∤n. The difference class kappa_r(f)−n chi has zero residues, and evaluation of chi at transported labelled points is zero; multiplication by n is all that is used. Minimality of n implies f is not a geometric rth power for every r≠p: valuations exclude it if r∤n; otherwise an rth root would make (n/r)(P−Q) principal.

After a finite extension L containing mu_r, let D be the smooth proper connected model of z^r=f/a. It is geometrically connected. Along L_m of degree l^m over L, put Q_m=|L_m| and let M_m count noncuspidal points with f(R)/a an rth power. Then r M_m ≤ #D(L_m), so the Weil bounds give

`#C(L_m)−2−M_m ≥ (1−1/r)(Q_m+1)−(2g+2g(D)/r) sqrt(Q_m)−2 → infinity`.

The exceptional points in this tower are bounded. A remaining point has nonzero mod-r Kummer evaluation, contradicting the criterion. This proves almost-separated implies separated, assuming the separately audited relative fixed-r transport argument in the Sigma category. It works even when l=r. The parent and both mathematical auditors received this argument.

For the main full p′ case there is an elementary direct support proof: choose odd l≠p with l not dividing |GL_f(F_p)|, where f is p-rank. The Z_l factor of G_k acts trivially on T_pJ (congruence kernel is pro-p), hence on all geometric p-primary torsion, and then on each at-most-two-element delta fibre. The potential bad labels therefore lie over kbar^{Z_l}, uniformly bounded in an l-power field tower. The earlier Boxall finiteness theorem can be audited separately without serving as a main-proof input.

## Update: explicit quotient repair and existing arbitrary-point reconstruction

Write K_F,K_E for the fibre and configuration cuspidal kernels over the proper geometric group and product. Right exactness gives K_F→K_E surjective. AG.41 for each r gives K_F^(r)≅K_E^(r), hence their abelianizations agree prime by prime and K_F^ab≅K_E^ab. Thus the cuspidally abelian fibre comparison follows. The one-puncture central comparison follows from orientation coinvariants. This repairs exactly the central, cuspidally abelian and fixed-r fibre identifications used at the checked loci, not the full mixed-prime assertion.

The configuration auditor independently confirmed the multiple-labelled-section extension needed for finite proper pullbacks: for a product compactification C0×B minus disjoint section graphs, choose the Galois A-cover C1→C0 required by a finite fibre quotient. Take a finite Galois Sigma-cover of B dominating the pullback of C1 along each section. Then all punctures are labelled, compactification remains product, and mod-r monodromy is shear. The same normal-core argument applies with finite deck group A×A_B.

Original Mochizuki Theorem 3.10 starts arbitrary matching rational x*,y*, with a Frobenius-preserving proper-group isomorphism and no separation hypothesis. Its proof starts from configuration cab reconstruction (Theorem 1.16(iii)), chooses matching splittings in the diagonal boundary group and restricts to the cab fibres. Thus the mere reference in ST2009 journal Theorem 2.6 to its outside-E Corollary 2.3 is not sufficient to dismiss the arbitrary-point reconstruction theorem. The actual fibre input must be repaired. The known statement is strong; this audit supplies a quotient-level correction rather than a global paper verdict.

## Update: characteristic-zero scope

Owned sections `sections/A_literature.tex` and `sections/C_literature.tex`, metadata `notes/literature_statements.json`, and bibliography `notes/literature_references.bib` now contain the detailed statements. C4 is proved as a pullback theorem with a retained diagonal cusp. An exact quotient that has killed the new cusp recovers only the corresponding quotient, not the discarded full punctured group. The extension attached to arbitrary s need not split by construction.

For full base groups over fields finitely generated over Q, a cusp-preserving over-identity isomorphism projects to equality of sections, then ordinary all-prime Kummer injectivity separates points. For positive compactified genus this is Mordell–Weil–Lang–Néron; for genus zero take a coordinate with zero and pole at two boundary points and use injectivity on k×. Finite generation of the entire group k× is not asserted. Its no-infinitely-divisible-elements property follows from divisorial valuations, the number field of constants, and its unit theorem. A singleton-l Kummer map can kill prime-to-l torsion, so no unsupported all-quotient separation claim is made.

## Additional primary sources opened during this update

| Source | URL | Ref | Scope read |
|---|---|---|---|
| ST2017 PDF | https://arxiv.org/pdf/1708.08773 | turn50view0 | Full primary version; support statements above |
| Wakabayashi PDF | https://arxiv.org/pdf/1507.00622 | turn50view1 | Theorem A and source comparison |
| Ciperiani–Stix 2015 | https://jtnb.centre-mersenne.org/item/10.5802/jtnb.892.pdf | turn50view2 | Section 1.2, finitely generated fields and Kummer injectivity |
| Poonen 2005 corrected | https://math.mit.edu/~poonen/papers/etale.pdf | turn38view0, turn51view1 | Theorem 1.7, all four hypotheses, proof Sections 2–3 |
| Bogomolov–Tschinkel | https://cims.nyu.edu/~tschinke/papers/yuri/02ram/ram4.pdf | turn38view1, turn51view0 | Theorem 1.7, Conjecture 2.6, Sections 2 and 4 |
| Achter–Pries 2015 | https://www.math.colostate.edu/~pries/Preprints/15suprank1015arxiv.pdf | turn42view0 | Superspecial rank versus isogeny factors; no relevant universal cover theorem |

The Stix Brauer–Manin author URL returned 403 and is not treated as an opened source. The Stix monodromy arXiv PDF was successfully opened as turn23view1 and downloaded as `Stix2005_monodromy_arxiv.pdf`.

## Update: arbitrary Sigma containing an invertible prime

The configuration auditor's A.CF12 extends the relative fixed-r theorem to proper pro-Sigma groups even when p belongs to Sigma. This is a direct algebraic proof using Stix Proposition 2.7, not an equivariant characteristic-zero lifting argument. For an arbitrary finite proper etale Galois A-cover C'->C, the complement of its deck graphs in C'×C' has constant proper compactification and labelled boundary. Its mod-r fibre homology is an extension of two trivial modules, hence the monodromy image is an r-group of shears. Stix retains the full base fundamental group while completing the fibre kernel. Conjugation into Aut(F_r), followed by the pro-r congruence-kernel calculation and centrelessness of F_r, then gives the needed pro-r injection. The finite normal-core detection uses an extension of an r-group by A×A, still a Sigma-group even if p divides |A|.

For Mochizuki's exact conventions, the cuspidal abelian comparison therefore also extends. His groups are formed from tame boundary groups, followed by maximal cuspidally pro-Sigma-dagger completion, with Sigma-dagger=Sigma minus {p}; this is explicit at original text lines 524–525, 721, and 737–738. The cuspidal kernel is normally generated by conjugates of tame inertia. Every map of it to a finite p-group kills these generators, so its maximal pro-p quotient is trivial. Its abelianization is consequently the product of the r-abelianizations for r in Sigma-dagger, all supplied by A.CF12. The surviving central orientation module is Zhat^{Sigma-dagger}(1). **The same assertion is false for the full wild punctured etale group**, where Artin–Schreier covers give p-primary cusp quotients. A.LIT2 now states this distinction explicitly.

The criterion auditor correspondingly extended A.CR9–10 to every Sigma containing a non-p prime. Finite-field p-adic Kummer detects the p-primary rational subgroup: [p^n] factors through a connected radicial kernel, bijective on geometric points, and a finite etale quotient; the latter supplies the same division-point cocycle. Thus A.LIT6 and the ST2017 consequences now include p in Sigma. All earlier limitations to Sigma subset p-prime in this running notebook should be read with this later, explicitly proved extension.

## B5: proved constructions and precise remaining obstacle

The complete proofs are in `sections/B_literature.tex`, B.LIT1–4. They do not assert the arbitrary-curve case.

### Finite torsion positioning, all characteristics

For any elliptic curve E and finite set S in P1, an affine change after initial coordinates places S among the images of prime-to-p torsion under E->E/{±1}. For ordinary E, choose a finite field where its unit Frobenius root alpha is 1 modulo p, and put a=v_p(alpha-1). Along extensions of degree prime to p the p-primary rational torsion is killed by p^a. The iterated Verschiebung E^(p^a)->E has image exactly that prime-to-p subgroup on these finite-field points. Compose with the degree-two quotient to obtain a genus-one Galois cover of P1 with group ker(V^a) semidirect {±1}. Translate N copies so that their branch sets are pairwise disjoint. The compositum is geometrically connected: inertia at a branch point unique to factor i is supported only there, and all such inertia normally generates that factor because P1 has no nontrivial connected etale cover. Thus the full product group occurs. Weil bounds along an auxiliary l-power constant tower give a simultaneous rational preimage avoiding the branch set. This proves the positioning lemma even in characteristic two, where the degree-two map is wild. The compositum genus is 1+(N-1)(2p^a)^N.

### Odd-characteristic hyperelliptic sources

Choose four branch points of C->P1 to form an elliptic double cover E. Its normalized pullback C0 is an etale double cover of C and a branched double cover of E. Move one branch value to the elliptic origin. The positioning lemma places the branch values of any hyperelliptic target H over prime-to-p torsion of E. Pull C0->E back along multiplication by an integer prime to p killing all this torsion. The new cover ramifies with index two above all the relevant torsion points. Pulling back H now cancels all its ramification and gives an etale cover mapping to H. All source-cover steps have prime-to-p Galois order; the Galois closure of their composite is prime-to-p by finite wreath products.

This includes p=3, where the explicit supersingular target y^2=x^9-x has genus four. More generally y^2=x^Q-x for Q=p^b>=5 attains a Weil bound over F_(Q^2): its count is Q^2+1+epsilon(Q^2-Q), epsilon=(-1)^((Q+1)/2). Every Frobenius slope is therefore 1/2. The argument strengthens the checked formation control of the known hyperelliptic correspondence construction; no novelty is asserted.

### Expanded low-genus Galois cases

Poonen Theorem 1.7, cases (1)–(3), begins with a prime-to-p finite Galois action on a curve of genus at least two and quotient genus at most two. In odd characteristic we retain the prime-to-p Galois-closure condition throughout his proof when: the quotient has genus one or two; the group is solvable; or two branch indices have a common prime factor. The full derivation is in B.LIT4. The elliptic case uses multiplication by a prime l>=5, and cyclic e-covers of P1 with four or six branch values to obtain hyperelliptic targets. The solvable case inducts on a normal subgroup and treats cyclic prime order explicitly. The common-factor case iterates cyclic base changes of P1; degrees and genera increase while the Galois degrees to P1 stay bounded, yielding arbitrarily many branch values and six with the same index. Every covering step is etale cyclic prime-to-p or a connected base change of such a step. This includes all tame superelliptic curves in odd characteristic.

Poonen's modular fourth case uses indices 2,3,l for the stated finite list of primes l. His proof uses PSL_2(F_l), a Borel subgroup, and an Atkin–Lehner involution. We obtain the requested prime-to-p conclusion under the additional explicit condition p not dividing l(l^2-1). Local tameness of indices 2,3,l alone does not impose this global group-order condition.

### Characteristic two and unsuccessful general routes

B.LIT3 proves the case of a map to P1 with three fibres whose ramification indices are all divisible by three. Pull back the cyclic cubic E:y^3=x(x-1), which is the supersingular elliptic curve z^2+z=t^3. The normalized cover of the source is etale of degree one or three. Every cyclic cubic curve of genus at least two satisfies the hypothesis.

An arbitrary tame map to P1 does not supply such uniformly divisible fibres: its generic simple branch value has an unramified point elsewhere in the same fibre. A branched target cover stays ramified at that point. Passing to the Galois closure need not preserve the prime-to-p formation, and taking an etale subcover does not in general remove this problem. The tame Belyi theorem of Kedlaya–Litt–Witaszek Theorem 1.5 supplies neither uniform divisibility throughout the fibres nor a prime-to-p Galois closure. The general odd-characteristic reduction would be a prime-to-p etale cover dominating a hyperelliptic curve; it is closely related to, but not logically identical with, the universal-correspondence assertion recorded as Bogomolov–Tschinkel Conjecture 2.6.

Raynaud 2000 Theorem 2 gives a solvable prime-to-p etale cover which is nonordinary, not a supersingular factor or a map to a supersingular curve. The distinction is decisive. Ozman–Pries 2019 likewise supplies Prym p-rank information, not the missing universal supersingular target; their characteristic-two genus-two example warns that cyclic cubic Pryms of a p-rank-zero curve can be ordinary. These sources did not close the general B5 case. No claim of present-day openness is inferred from an older conjecture alone; the exact unproved reduction and attempted routes remain recorded.

## C1, C2, C5: exact improvements without overclaiming

`sections/C_literature_consequences.tex` contains C.LIT5–8. ST2017 Theorems 4.22 and 4.23 already conclude global Isom correspondences under their hypotheses; their final statements do not have a finite set removed. The new consequence is that the intermediate exceptional sets vanish under the retained J-large hypotheses, for every Sigma containing a non-p prime, including p in Sigma. Point labels, their degrees, compatible labels at every finite etale Sigma-cover, arbitrary finite marked sets in Corollary 3.3, and the pointwise Green compatibility of Proposition 3.12 therefore have no exceptional exclusions. The omitted-prime pseudo-function quotients and torsion controls are not removed, and neither is largeness.

For ST2009 Theorem 3.9 and Corollary 3.10, the full prime-to-p main theorem makes all exceptional sets empty, including when p is also retained in the proper group by projecting to p-prime. The outside-exceptional-set restrictions in Corollary 2.3, Theorem 3.6 and Proposition 3.8 disappear. The p-primary correction terms remain. The relative fixed-r fibre theorem cannot simply replace the false full sequence inside a theorem which requires the full punctured group. The valid route proves point separation via the relative criterion first, then uses the repaired central/abelian/fixed-r reconstruction inputs for the already-known Isom conclusion.

For Mochizuki 2007 the clauses checked individually are original Definition 1.18, Theorem 2.5(i), Proposition 2.6(ii),(iii), and Corollary 3.11, with version correspondences recorded in C.LIT8. Their separation conditions become automatic in the finite-field full-prime-to-p scope after every finite proper cover. The principal-divisor condition in Theorem 2.5(ii) is a separate condition and is not deleted. The arbitrary-matching-point theorem, original Theorem 3.10, already has that existence scope; new point-label uniqueness is not a new existence theorem. No conclusion is asserted for the whole paper beyond the checked clauses. Wakabayashi's singleton-prime hypotheses and Sun's special geometricity hypotheses remain distinct.

## Independent audits requested by the parent

Read `sections/A_root_fields.tex` and checked the semabelian Kummer-kernel argument, the full cover-condition comparison, positive-characteristic specialization, and the affine genus-one generalized-Jacobian zero count. They pass with one scope clarification: over an imperfect field a smooth affine curve's smooth compactification or geometrically reduced boundary need not be obtained by a separable extension alone. Either the convention already includes a smooth proper compactification and etale boundary, or the proof should allow a finite purely inseparable extension first and invoke universal-homeomorphism invariance. This was sent to the parent.

Read `sections/B_root_primitive.tex` and independently checked the genus-two elliptic-quotient geometry, Frobenius [-2^19], the unique theta characteristic, the zero-count/difference bound, the conductor cutoff, and the character-orbit interpretation. These arguments pass. This audit did not independently rerun the large finite-field certificates, which the parent's verifier owns. Suggested explicit notation for the Frobenius twist in the theta argument.

The independent residue-characteristic-zero audit is saved separately as `notes/reconstruction_residue0_independent_audit.md`. It checks Lepage Theorems 1.6 and 1.8, the node lift, explicit compatibility with mark-forgetting contractions, arithmetic cusp quotients, and the entire small etale-site passage. The generic-arc lemma's incidence-dimension and elimination calculation was also independently checked and found sound; its separate centralizer theorem was not yet included in that file.

## Additional opened primary-source log

| Source | URL | Tool ref | Exact scope |
|---|---|---|---|
| Kedlaya–Litt–Witaszek | https://arxiv.org/pdf/2010.01130 | turn68view0 | Theorem 1.5 and scope of tame Belyi maps; journal metadata verified by publisher |
| Raynaud 2000 | https://www.cambridge.org/core/services/aop-cambridge-core/content/view/16AB72912D3CE32BFC5D012B1025A8E4/S0010437X00000440a.pdf/revetements-des-courbes-en-caracteristique-pandgt0-et-ordinarite.pdf | turn81view0 | Theorem 2; Theorems 14 and 17 checked for the ordinarity distinction |
| Ozman–Pries 2019 | https://archive.intlpress.com/site/pub/files/_fulltext/journals/ajm/2019/0023/0003/AJM-2019-0023-0003-a005.pdf | turn78view1, turn79view2 | Theorem 1.1, Section 8.2, Example 9.4; no general supersingular-target claim |
| Lepage 2013 | https://www.numdam.org/article/AIF_2013__63_4_1427_0.pdf | turn87view0 | Independently read Theorems 1.6 and 1.8, Corollary 1.9, and their precise base hypotheses |

The download script and manifest include these primary PDFs and extracted text. Existing files are preserved and every failure is recorded explicitly.

## Further completed audits and new residue-zero extension

The independent B.CF4–9 audit is now complete in `notes/reconstruction_primary_audit.md`, including the full formal-arc argument and the all-finite-extension centralizer theorem. Primary exact citations are Khassa–Khanduja 2010 Lemma 2.1 for automorphism continuity; Hoshi–Tsujimura 2023 Definition 4.3 and Corollary 4.5(3) for slimness of number-field absolute Galois groups; ADH Corollary 3.3.22 and Propositions 3.3.25–27 for the algebraic-closure/henselization calculation; and Carlson–Haine–Wolf Proposition 3.6 and Theorem 4.18(5) for the precise topos reconstruction formulation. These references use the configuration auditor's existing bibliography keys. The original F. K. Schmidt article was not opened; its continuity consequence is used through the fully opened primary Khassa–Khanduja lemma, with that provenance stated.

The new `sections/B_reconstruction_nondiscrete.tex` proves B.LIT5–6. B.LIT5 derives all-prime Kummer-cover comparison for proper stable marked models over a henselian rank-one valuation ring of residue characteristic zero, using the full valuative log structure. It combines AHLS Lemma 5.3.2 (henselian excellent regular snc approximation), Definition 3.4.4 and Proposition 4.2.6 (affine-charted saturated covering-category continuity), and Lepage 1.6/1.8 at the noetherian stages. Saturated node monoids (AHLS Example 2.4.5) make ordinary and logarithmic base change agree. The local residue-field limits give the actual log closed fibre. AHLS Corollary 4.4.9 independently checks that the arithmetic base is the full BG_K in residue characteristic zero. Finite Kummer covers here have integral, not necessarily finite, underlying maps; silently imposing the latter would be incorrect.

B.LIT6 extends the supported scaling and its logarithmic compatibility to arbitrary rank-one radii, replacing pi-powers by fixed scalars d,e and using z=(b-a)/d+(e/d)w. The same scalars are used before and after the point permutation. All initial forms and every contraction pullback agree. The whole étale-site argument therefore gives a nonalgebraic pinned equivalence for every henselian rank-one residue-characteristic-zero field. Finite transcendence degree implies finite rational rank of the value group, hence a rank-one coarsening. ADH Lemma 3.4.2 proves this coarsening remains henselian. Thus all residue-characteristic-zero finite-transcendence-degree cases of B8 are covered, including nondiscrete valuations and positive transcendence defect. Mixed-characteristic fields without such a coarsening remain outside this argument. Parent and configuration auditor independently read the draft; criterion auditor was asked for a third review.

## Completed A10/C5 dependency and condition census

A.LIT2 has been expanded to every perfect ground field, with Sigma-dagger exactly the primes in Sigma invertible in that field. Its proof uses no finite-field counting. The arithmetic inverse-image statement follows from the geometric isomorphism and the unchanged G_k quotient; finite labels split separably and their natural Galois data descend. This covers all M07 ground fields because the paper's section 0 explicitly defines its nonarchimedean local fields as finite extensions of Q_p. It does not include full wild cusp kernels in positive characteristic.

New A.LIT8 records all three direct textual uses of original Proposition 1.8(ii): inside the proof of (iii), the surjectivity paragraph before Proposition 1.12, and the insertion immediately before Proposition 3.8 (original p.63). The first two use only central or abelian quotients. At the third locus S=S_* and S_0 is empty, and every ensuing Lie construction uses pro-l quotients of punctured finite proper covers; replacing the ambient group and its fibre by the relative cuspidally pro-l quotient supplies the same diagonal actions and retained boundaries. M07 3.9(v) invokes singleton-l configuration slimness, where M–T 2.2 applies. The original full mixed-prime fibre insertion is false and remains deleted. The asserted full mixed-group slimness consequence of 1.8(ii) is **not** inferred from our relative or abelian proofs and is independently unestablished here. This distinction does not leave the listed downstream quotient arguments unproved.

M–T 2008 uses its own PT-formation exactness, and its M07 citation in Remark 4.8.2 is motivational. ST2009 imports precisely central, abelian and fixed-l constructions in Theorem 2.2, Corollary 2.3, Proposition 2.4 and Theorem 2.6; ST2017 repeats them in 3.2,3.3,3.4,3.6. These lie in the repaired scope. ST2009 journal Remark 3.14 remains a conditional failed full-group proposal, not a premise of its Isom proof. Wakabayashi 1.4 derives its singleton fibre theorem from M–T or Stix; Theorem 4.4's proper n=2 input cites the singleton specialization of M07 fixed-l reconstruction. None imports the refuted mixed formation at that point.

New C.LIT9 gives the complete explicit separation/point-theoreticity condition census in M07: Definition 1.18, Remark 1.18.2, Proposition 2.3(ii), Definition 2.4, Theorem 2.5, Proposition 2.6(ii),(iii), Remark 2.6.1, Corollaries 2.7–2.8, Proposition 2.10(iii), and Corollary 3.11; Theorem 3.10 assumes matching groups without separation. It states precisely what disappears over finite fields for full prime-to-p groups and which other assumptions remain. Wakabayashi assumes no missing mixed-prime separation condition; its explicit nonuniqueness warning cannot be removed for singleton groups. Sun2025 virtual pullback works for arbitrary sections in characteristic zero. Sun2026 Lemma5.6(i) uses already known full-group point injectivity over its arithmetic fields (number or p-adic local fields); (ii) and later geometricity criteria require additional hypotheses. No source theorem there becomes a section-surjectivity theorem from R1.

## Latest primary-source log

| Source | URL | Tool ref | Verified statement |
|---|---|---|---|
| Hoshi–Sawada–Tsujimura 2024 | https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1984.pdf | turn98view0, turn100view0, turn105view1 | Definitions1.1,1.3,1.6; Lemma1.8, Theorem1.13, Corollary1.14; retains full tame base |
| Hoshi–Tsujimura October2026 | https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS2007.pdf | turn98view1, turn105view0 | TheoremA(i)=1.8; full étale affine Artin–Schreier evaluation, degree-p Galois extension hypothesis |
| AHLS 2024v1 | https://arxiv.org/pdf/2411.13662 | turn108view0, turn116view0, turn116view1 | Example2.4.5; Definition3.4.4; Proposition4.2.6; Proposition4.4.3; Corollary4.4.9; Lemma5.3.2 |
| Hassett 2003 | https://www.math.brown.edu/bhassett/papers/weights/weights10.pdf | turn123view0; publisher turn118search2 | Theorem2.1, proper smooth moduli stack and projective coarse scheme; genus0 all labels gives fine scheme |
| ADH online January2025 | https://www.mat.univie.ac.at/~maschenbrenner/pdf/mt.pdf | turn126view0, turn128view0 | Lemma3.4.2 and its proof, henselian coarsening; earlier 3.3.22–27 independently checked |
| Knudsen 1983II | https://journals.msp.org/mscand/article/download/1622/1621/1653 | turn123view1; metadata turn121view0 | Publisher scanned PDF preserved; no exact theorem in it is invoked without a readable independent verification |
| Milne AV version2.0 (2008) | https://www.jmilne.org/math/CourseNotes/AV.pdf | parent turn112view0 | Parent's verified II Lemma1.3 and Remark1.4, pp77–78; downloaded and logged as requested |

The owned metadata now records 23 statements in five section files, including A.LIT8, B.LIT5–6 and C.LIT9. The downloader records 29 opened primary PDFs with extracted text and SHA256 hashes. No whole-paper or universal-priority claim is made by this census.

## Post-checkpoint B5 investigation and exact cyclic-thirteen certificate

The metadata now has 24 claims in six owned section files. New B.LIT7 in `sections/B_literature_probe.tex` proves an exact positive-2-rank primitive-zero example for C0: Y²+X²Y=X⁵+X over F2. Its Lang-character cyclic13 cover over F64 has numerator (1−T−80T²−64T³+4096T⁴)(1+12T+64T²)^12. The primitive slopes are 1/3 and 2/3, twelve of each, and its relative class number is 77^12=43439888521963583647921. The base Jacobian is geometrically simple of 2-rank one, with irreducible characteristic polynomial U⁴+U³+2U+4; hence neither the base nor the cover has a geometric supersingular factor. This distinguishes B4 from B5 without claiming a counterexample to the existence of some different odd cover. Producer `b5_char2_13_certificate.py` and root's independent CRT/tangent verifier `c0_cyclic13_verify.py` agree on every point projection and all13 subgroup elements; the latter imports no Cantor implementation. The exact Milne citation is standalone Jacobian Varieties §9 Proposition9.1, applied after base change to a separably closed field. In the combined AV2008 volume it occurs in Chapter III, printed pp113–114; the immediately preceding sentence imposes separable closedness.

The auxiliary theta-Taylor elimination excludes odd torsion orders3,5,7,9,11 on the translated Raynaud theta curve for C0, and gives the order13 candidate polynomial r²+r+1. The separate constant-field character probe checks all exponent-one prime quotient factors occurring over F2^m for 1≤m≤10, retaining full twisted quadratic polynomials. Neither computation classifies all geometric covers.

A distinct attempt uses C7: y²+y=x⁷, genus3 and 2-rank zero. Its characteristic polynomial is U⁶−2U³+8. Four rational cyclic3 quotient kernels over F256 all have point occupancies (113,72,72), giving first twisted coefficient41. The exact full3 computation over F2^24 finds all729 geometric3-torsion points: every nonzero point has reduced Mumford degree3. There is also a direct proof of the resulting obstruction for every characteristic-two hyperelliptic genus3 curve of 2-rank zero. Let P be its unique Weierstrass point. The exact differential dx has divisor4P, so Raynaud's line bundle is O(2P). A nonzero3-torsion point on its theta divisor would be represented by a reduced effective D of degree d≤2, with 3D−3dP principal. But every function with its only pole of order≤6 at P lies in k[x], whereas its zero divisor contains hyperelliptic conjugate pairs; the reduced divisor D cannot. Thus all its cyclic3 Pryms are ordinary. This closes the cubic-reflection route, not the arbitrary odd-cover question.

Recent primary sources opened for possible further constructions are logged below. None supplies the requested arbitrary-source, prime-to-p Galois-closure theorem. The downloaded PDFs and text of the first three are retained; the updated Carlson–Stix PDF opened once through its author page but subsequent fetch/download attempts returned403 and are not represented as successful downloads.

| Source | URL | Tool refs | Exact use and limitation |
|---|---|---|---|
| Leonardo Zapponi, Lamé operators in characteristic two, arXiv1004.3695v3 | https://arxiv.org/pdf/1004.3695 | turn640500930view0; turn891547806view1, turn891547806view2 | Proposition2.1 and Theorem2.2 give tame supersingular-elliptic covers with branch datum (n;n;3,1,…,1). A source needs uniform n,n,3 fibres to cancel their ramification. For a genus2 source and n≥5, Riemann–Hurwitz excludes that pattern. AppendixB.2's blanket assertion that y²+y=x^(2g+1) is supersingular for every g is not used: g=3 gives the contrary polynomial above. |
| Aaron Landesman and Daniel Litt, Prill's problem, Algebraic Geometry11(2)(2024),290–295, DOI10.14231/AG-2024-009 | https://api.algebraicgeometry.nl/Article/20170/2024-2-009.pdf | turn256309751view1; turn569124275view0; turn891547806view3 | Theorem1.2 and Proposition2.4 are explicitly over C; the degree36 construction includes degree2 steps, so no characteristic-two prime-to-2 inference. |
| Jeremy Booher and Rachel Pries, Producing supersingular curves of genus five, arXiv2410.20262v2 | https://arxiv.org/pdf/2410.20262v2 | turn256309751view2 | Theorem1.2 constructs special genus3 bases with supersingular unramified double covers when p≡3 mod4. It is not an assertion about every prescribed base. |
| Magnus Carlson and Jakob Stix, version20September2026 | https://www.math.uni-frankfurt.de/~stix/research/preprints/CARLSON-STIX-VoevodskyQp20260920.pdf | turn434708151view0; author page turn578337889view0 | TheoremsA/4.1 and B retain sub-p-adic hypotheses; PropositionC/3.17 retains Kummer-faithfulness. Their reconstruction route invokes Mochizuki Hom after the open/constant dichotomy. A stable p-Kummer kernel equal to μ∞ does not meet either the Kummer-faithful or CHW amenability condition. |
| Armand Brumer, On the units of algebraic number fields, Mathematika14(2)(1967),121–124 | https://doi.org/10.1112/S0025579300003703 | turn480919083view0, turn480919083view1 | Metadata verified; original full text and first-page image could not be retrieved. No false assertion that the original proof was read. |
| Bernard Rousseau, exposé11, Séminaire de théorie des nombres de Bordeaux1968–1969 | https://www.numdam.org/item/STNB_1968-1969____A11_0.pdf | turn480919083view2 | Primary proof of Brumer's p-adic logarithmic independence theorem, opened and read. Applies to algebraic-over-Q units; Q-linear independence of their p-adic logarithms implies Qbar-linear independence. Configuration auditor also opened independently. |

The direct CHW source check uses Definition5.15(5.15.1): no nonzero prime-to-exponential-characteristic divisible elements in any torus, and separately (5.15.2): Tate-module vanishing for the Picard group of every regular finite-type scheme. In characteristic zero μ∞ already violates the first condition for Gm. The second does not follow from a statement only about the p-Kummer kernel of Gm. This prevents importing those reconstruction theorems from the new pronilpotent-field kernel result alone.


## Further proved B5 scope as of 04:02 UTC

Parent independently approved the elementary cubic obstruction and fixed-function ramification obstruction. They are now B.LIT8 and B.LIT9 in `sections/B_literature_probe.tex`. The last paragraph of B.LIT8 has been expanded to prove the wild reflection quotient and Prym decomposition directly: the lifted involution squares to1, fixes exactly one point, has local different2g+2, and yields quotient genusg−1; two conjugate reflection pullback images meet in six-torsion and sum isogenously to the Prym. No characteristic-zero dihedral formula is imported silently.

B.LIT10 positively extends the uniform-three-fibre construction to every odd r≥3 with r dividing p^a+1. The target H_r:y^r=x(x−1) has genus(r−1)/2 and is dominated by Fermat_r, which is dominated by the degree-p^a+1 Hermitian Fermat curve. The proof counts p^(3a)+1 points explicitly and uses the attained Weil bound. In characteristic two this includes cyclic-prime covers with even multiplicative order of2 modulo the covering prime, for example5,11,13,17,19. The cover of the prescribed source is cyclic étale of degree dividingr, so the required prime-to-p Galois-closure condition is explicit. It still leaves cyclic7 and arbitrary characteristic-two genus2 sources unresolved.

The owned metadata now contains27 claims in six sections. A further recent primary paper, Naranjo–Ortega–Pirola–Spelta, *Families of simple Jacobians with many automorphisms*, Algebraic Geometry12(6)(2025),869–887, DOI10.14231/AG-2025-026, was opened at https://api.algebraicgeometry.nl/Article/21295/2025-6-026.pdf (turn988220803view0, turn202760500view0). Its introduction explicitly works with complex curves; Theorems1.1–1.3 concern generic simplicity and Prym Torelli/finiteness. Remark4.4 explicitly has not excluded hyperelliptic quotient curves, but provides no theorem forcing those quotients to be hyperelliptic. It therefore does not justify an iterative genus-reducing construction in characteristic two.
