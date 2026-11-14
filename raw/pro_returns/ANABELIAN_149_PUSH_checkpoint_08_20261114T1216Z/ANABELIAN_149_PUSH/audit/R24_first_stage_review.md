# R24 first-stage reconstruction and independent review

Date: 2026-11-14. Responsible agent: degeneration. Reconstruction: `sections/D_local_first_stage.tex`, claims D.15 and D.16. Ledger: `audit/D_local_first_stage_results.json`.

## Scope, attribution, and conclusion

This is an annotated reconstruction of Sections 2–4 of the supplied manuscript *The p-adic section conjecture*, dated 6 October 2026 and attributed to OpenAI. It makes no priority claim and does not attribute this modern completion argument to Grothendieck's manuscript. The exact question and auxiliary-source loci are: 149; manuscript pp.27-31,62v-63; scans56,59-63,126-127; auxiliary R24 Sections2-4, pp.5-12.

The local text reviewed is `tmp/pdf_text/padic_section_conjecture_2026.txt`, approximately lines220–637. The exact statements reconstructed are its Lemmas3.1,3.3,3.4, Proposition3.2, Lemmas4.1–4.3, and Proposition4.4. The supplied manuscript remains a source whose proof is being checked; its asserted conclusion is not used as an external theorem.

No specific gap was found in these sections after adversarial review of whole-collar roots, the separating stable-edge construction on every sheet, the precise RNS model-domination assertion, and evaluation at the specified H-valued point. D.15 and D.16 give complete proofs from the stated established inputs. Their endpoint is the inclusion of the specified compositum L_ell in H inside E. The arbitrary-order root construction, the inclusion of the whole separable closure, and the final section-theoretic deduction belong to subsequent claims and are outside this first-stage certification.

## 1. Fields and exact comparison maps

The reconstruction fixes a finite extension k/Q_p, a smooth proper geometrically connected curve X/k of genus at least2, K=k(X), a separable closure containing a chosen algebraic closure kbar, a real rank-one field norm extending the normalized p-adic norm, and a prolongation of that norm to the chosen separable closure. The universal etale field Ktilde includes every K-embedding of every connected finite etale cover field. Finite constant-field covers put kbar inside Ktilde. Its completion H is the closure of Ktilde in E=completion(Ksep), and Omega=completion(kbar) is a specified subfield of H.

The value group of Omega is Q because completion preserves the value of each nonzero limit. The embedding K0=kbar(X)→H gives a generic H-point over kbar; combining the specified Omega→H gives the H-point of X_Omega used throughout. Its underlying analytic point xi can be Omega-rational, so the proof retains its completed-residue-field embedding into H. A closed support after extending constants is never confused with a closed support over kbar.

The horizontal valuations used in L_ell are the closed-point valuations over kbar and have residue characteristic zero. They are not the characteristic-p reduction valuations. All field inclusions in the conclusion concern the fixed copies inside E.

## 2. D.15: normalization, patching and evaluation

At a horizontal ramification point, t=u^e a(u). After choosing a root of a(0), shrinking until v(a/a(0)−1)>v_p(e)+1/(p−1) permits the logarithm/exponential root even when p divides e. Analytic inversion gives t=z^e. Properness shows that a smaller base disk has its whole inverse image in the chosen charts; this prevents additional sheets outside the local charts. The branch disks can avoid xi because xi is not an algebraic branch point.

For each collar the assumed root is defined on the entire inverse annulus. Every factor Z^e−g*t then splits, and distinct factors are comaximal: their differences are nonzero constants times analytic units. A small absolute value of a root-of-unity difference does not prevent invertibility over Omega. All d sheets are trivialized. The exterior and inner inverse disks form an open cover, and distinct branch disks are disjoint, so these trivializations glue finite locally free analytic algebras without an omitted triple-overlap condition.

Proper coherent GAGA algebraizes the algebra, its unit and its multiplication. Analytification detects etaleness. A nonempty connected component remains surjective over the connected base, and retains the exterior analytic map. The component step does not select a preferred local sheet.

For evaluation, an embedding of the descended cover field into H gives an H-point of the algebraic cover, hence of its Omega-base change. The isomorphism over X_Omega preserves the exact given H-point downstairs. The exterior analytic map is evaluated through the completed residue fields H(c)→H(v)→H. The resulting H-point of C projects to the generic point over kbar, since C→X is finite, yielding the desired K0-field embedding. No descent of the analytic map is assumed.

For index stability, every finite local extension of kbar((t)) is kbar((t^(1/e))). All extensions with e dividing n are subfields of the same cyclic extension kbar((t^(1/n))). This handles composita and Galois closures. Normalized base change t=s^r a(s) gives index e/gcd(e,r). Etale upper composition multiplies an index by1. The statement deliberately does not cover arbitrary composition of two ramified maps.

## 3. D.16: full annuli and stable-edge covers

On a circle of radius in |Omega*| the normalized reductions of a unit and its inverse are inverse Laurent-polynomial units. The reduction is therefore a monomial. A change of dominant Laurent exponent would force a tie at a rational valuation radius, contradicting this monomial property. Convergence on compact subannuli reduces the competing terms to finitely many and yields a single factorization cS^a(1+h) on the entire open annulus. The binomial root of 1+h converges uniformly on each compact subannulus, and these roots agree on overlaps. The disk analogue gives the constant-norm assertion needed in the RNS argument.

For a nonseparating edge, choose a simple circuit. On every residue component along it, Picard divisibility supplies a cyclic degree-ell cover totally ramified at the two circuit marks and unramified elsewhere. The other marked fibres have ell points and are all included. The chosen graph map is harmonic, all residue ramification is tame, and the two Riemann–Hurwitz contributions match the two ramified edge ends, giving zero augmented ramification. Loops and chords are explicitly allowed. Stability is checked by multiplication of 2g−2+valence by ell. Connectedness follows by lifting paths from off-circuit vertices to the first circuit vertex.

For a separating edge, neither side can be a rational tree: its total valence would be2N−1, contrary to stability's lower bound3N. Each side therefore has a circuit or positive-genus vertex. A cyclic graph cover, or a connected etale cyclic cover at a positive-genus residue component with identity copies elsewhere, gives a connected degree-ell cover of that side. Matching the boundary fibres creates ell bridges between two connected sides. Every bridge is nonseparating. The lifted source remains stable. Applying the circuit construction to every bridge and then taking a connected component of their finite etale fibre product preserves all roots, because each projection is finite etale and surjective. The construction does not retain only one bridge or one sheet.

The inverse-skeleton equality in the lifting theorem controls the whole node annulus. Off-skeleton balls map into off-skeleton balls, and continuity identifies their attachment points. Retractions therefore commute. The inverse of the retraction tube of an open edge is exactly the union of all corresponding full source node annuli. The edge expansion factor is the Laurent exponent of the pulled-back coordinate, so divisibility by ell gives the required root on each such annulus.

## 4. RNS, the compact-complement step and the specified field

Algebraic curve, branch-point and parameter data descend to a finite local-field extension. A split semistable marked model exists after a further finite extension. Repeated blowups at smooth marked sections insert node annuli |pi|^(j+1)<|u|<|pi|^j. The parameter ratio t/u has constant norm on a small disk, so these annuli are concentric in t as well. The prescribed model can be unstable after the marks are forgotten. The proof does not assume that the inserted nodes survive stabilization on the original curve.

The RNS theorem is applied with the set of all primes, satisfying both the cardinality and residue-prime requirements. Proposition2.4(iv) supplies, after a finite base extension, a finite etale cover whose stable model maps to that prescribed model. Only the model morphism is used. No finiteness of this model morphism is assumed.

At an irrational valuation level inside a target node annulus, a source model vertex is excluded because its value group is |Omega*|. A source smooth-point tube is also excluded: if it meets the chosen level, the model morphism sends its reduction to the target node, so the entire disk tube maps into the target annulus; the pulled-back parameter is a unit and has constant norm in |Omega*|. Every point above the irrational level consequently lies in one of the finitely many source node annuli mapping to that node.

The complement of this union is closed in a proper analytic curve and hence compact. Intersecting with the inverse image of a closed target subannulus gives a compact set on which the valuation has compact image avoiding the chosen level. A smaller interval with rational endpoints avoids that image, giving a collar whose entire inverse image is in the selected source node annuli. The stable-node root construction applies to all of them simultaneously. This is the point at which control of only a preferred branch would fail; the proof uses the whole compact complement.

Finally the patching cover V_Omega→X_Omega is finite etale and descends to a cover over kbar by proper algebraically closed base-change invariance. Its function field embeds in the specified universal etale field. D.15 evaluates the analytic map at the corresponding H-point and embeds F in H. Because F/K0 is finite normal, every K0-embedding into E has image the specified F itself: all its minimal polynomials split in that copy. This gives F⊂H as an actual inclusion, and taking the compositum proves L_ell⊂H.

## 5. Exact primary-source ledger

The following established passages were opened in their original primary sources. Root also independently opened the lifting and RNS passages. Web retrieval identifiers are recorded as audit metadata, not as substitutes for the citations in the paper.

| Key | Exact opened passage | Primary source and use |
|---|---|---|
| D_OpenAI2026 | Supplied §§2–4; Lemmas3.1,3.3,3.4, Proposition3.2; Lemmas4.1–4.3 and Proposition4.4 | User-supplied unrefereed manuscript, local text `tmp/pdf_text/padic_section_conjecture_2026.txt`; these arguments are reconstructed, not assumed as a theorem. |
| D_Poineau2010 | Appendix A, Theorem A.1(ii), printed p.321 | [Publisher PDF](https://msp.org/ant/2010/4-3/ant-v4-n3-p03-s.pdf). The proper coherent-sheaf equivalence applies with base affinoid equal to Omega and algebraizes the finite locally free analytic algebra. Reopened refs turn344view0, turn345view0, turn346view0. |
| D_Temkin2010 | Facts5.1.3 and5.1.5, printed p.29; Fact5.1.6 and Exercise5.1.7 nearby | [Author lecture notes](https://berkovich-2010.imj-prg.fr/lecture-notes/Temkin-lecture-notes.pdf). Complete-extension-valued points agree and etaleness is detected by analytification. Reopened refs turn344view1, turn345view1–2. |
| D_ABBR2015 | Definitions2.19–2.21 (printed pp.9–10), Definition4.25 (p.26), Definition4.31 (p.27), Theorem7.7 (p.45) | [Author PDF](https://www.math.ens.psl.eu/~amini/Publications/hmmcI.pdf). A tame covering of metrized complexes lifts over the fixed target curve; no punctures means no branch points, and inverse vertex/skeleton equalities are part of the lifting data. Opened refs turn332view0, turn334view0–2, turn336view2–4. |
| D_MochizukiTsujimura2024 | Theorem A (printed p.4), Proposition2.4(iv) (p.50), proof (pp.53–54), 30March2024 version | [Author PDF](https://www.kurims.kyoto-u.ac.jp/~motizuki/Resolution%20of%20Nonsingularities%20for%20Arbitrary%20Hyperbolic%20Curves.pdf). The finite-local-field, all-primes case supplies a stable model mapping to the prescribed compactified model. Opened refs turn332view1, turn334view3, turn336view0–1. |
| E_SGA1 | Exposé X, Corollary1.8 and following descent explanation, original folio266 | Full original source `background/literature/SGA1/src_arXiv_math_0206203/smf_doc-math_3_01.tex`, lines16745–16781, label X.1.8; also [original reedition](https://arxiv.org/abs/math/0206203). Proper finite-etale covers descend up to isomorphism across algebraically closed field extensions. The missing exposition problem of the initially supplied wrapper does not affect this separately obtained complete source. |

## Validation and review boundary

The proofs explicitly check the locally ramified normal form, every marked fibre in the graph covering, augmented Riemann–Hurwitz, source stability, connectedness of the separating-side covers, projection surjectivity from the common fibre-product component, complete inverse annuli, the irrational-level compactness argument, exact H-valued evaluation, and normality at the final inclusion. These are mathematical checks, not numerical extrapolations.

The new fragment contains only the reserved claims D.15 and D.16 and uses the existing root bibliography keys. It does not modify D.tex or the assembler. The audit's conclusion is limited to this first stage. Subsequent arguments and final section-conjecture consequences require their own proof and review.
