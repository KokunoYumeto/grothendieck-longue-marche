# Part A: completed results and proof audit

The Part A deliverable contains 20 numbered claims: 17 Proved and 3 Known with full reductions. Every requested discrete, full profinite, and finite-step solvable case is handled in the scope of A(a)–A(d). No Part A mathematical obligation is left open. The filling theorem in A(d) is the discrete theorem of scans186–189; A.20 gives its exact comparison with completed discrete and full continuous automorphism groups.

| Task | Statements | Outcome |
|---|---|---|
| A(a): definitions, orientation lines, ranks and exceptions | A.1–A.2 | Proved, with the explicit dual, boundary, relative-cochain and filling maps; the plane and sphere exceptions are computed. |
| A(b): discrete rigidity, geometric extension normalizers/transporters, extension classification | A.3–A.6 | Proved for hyperbolic types; all four abelian types tabulated with explicit failure witnesses and strongest correct replacements. |
| A(c): full profinite rigidity, Lemme5/Corollaire2, closed base loops, abstract axioms, all finite-step solvable cases | A.7–A.11, A.14–A.19 | Completed. The one-puncture peripheral assertion fails exactly at depth2, where its centralizer and normalizer equal the full derived subgroup. It holds at every depth>=3. Closed finite-step base-loop centralizers and slimness are proved for all depths in A.19. |
| A(d): filling and exact orientation/permutation compatibility, one-side abelian cases | A.12–A.13, A.20 | Discrete theorem proved with exact index2nu!. The annulus target needs indexed peripheral source/orientation data for the full isomorphism; the punctured torus filling gives GL2(Z)→GL2(Z). The typed completion square states precisely what completion supplies. |

## The resulting finite-step table

Write P_m=P/P^[m], m>=2, where the derived subgroups are closed. All groups in this table are full profinite or pro-Sigma groups, with nonempty Sigma; the full profinite and single-prime cases are included. A standard handle generator means a generator in a geometric surface basis.

| Hyperbolic type | Centre and torsion | Open subgroup centralizers | Peripheral C(L^n), N(L), and transporters in an action extension | Standard handle C(<x>^n) |
|---|---|---|---|---|
| nu>=2 | Centre-free and torsion-free | Trivial | L at every depth; extension normalizer/transporter is E_s | <x> at every depth |
| nu=1,m=2 | Centre-free and torsion-free | Trivial | P_2′, strictly containing L; extension normalizer/transporter is P_2′E_s | <x> |
| nu=1,m>=3 | Centre-free and torsion-free | Trivial | L; extension normalizer/transporter is E_s | <x> |
| nu=0,g>=2 | Centre-free and torsion-free | Trivial | No peripheral indices | <x> at every depth |

Distinct peripheral indices remain noncommensurable in all hyperbolic punctured finite-step quotients. The exceptional groups1,1,Zhat,Zhat² are already abelian, so their finite-step quotients are unchanged and A.4 applies verbatim. In an annulus action, N_E(L)=Trans_E(L^d,L)=E; equality with the peripheral E_s is equivalent to fixing both ends. On the plane the peripheral mixed group has a noninjective map into E, with kernel Z in the discrete case and Zhat after completion; using its image gives the equality, but it cannot be identified with a subgroup before that kernel is removed.

## Proof details requiring particular care

### Closed solvable groups: A.19

The initial partial bound C_{P_m}(H) subset P_m^[m-1] is retained in A.18, but the obstruction is resolved by A.19. The proof starts with an explicit continuous Magnus homomorphism F→R^r⋊F_ab. Its kernel is proved to be F″ by factoring every finite metabelian quotient through a finite wreath embedding. Thus no exactness of an unspecified completed cellular chain complex is assumed.

For the surface relator, its image is the Fox vector v=(1-b1,a1-1,…,1-bg,ag-1). The closed normal relator module is exactly Rv, because Rv is a compact image. This proves the injection P′/P″→R^(2g)/Rv. Multiplication by a1^n-1 is injective on this quotient: the independent a2-1 coordinate is a nonzerodivisor modulo a1^n-1. Both nonzerodivisor assertions are proved by finite-coefficient cyclic orbit sums; choosing M divisible by the Sigma-part of n and passing from C_M to C_{kM} makes each orbit fibre sum k equal coefficients modulo k. This explicitly includes p=2,3 and integers n divisible by p.

Finite class-two groups with commutator module (wedge²A)/(sum a_i wedge b_i) force the abelianization of a centralizer element onto the selected generator's line. This proves the metabelian base case. For higher depth, every finite abelian cover has a lift x^d of the selected nonseparating simple curve. Its integral homology pushes forward to d[x], so it is again nonseparating and can be made a standard handle generator. A.15 justifies both required intersections of closed derived subgroups and products. Induction proves all depths, and two independent standard-generator powers then prove slimness.

This proof does not establish the broader arbitrary-characteristic assertion discussed as unknown in the supplied Yamaguchi preprint. It establishes exactly the characteristic-zero topological surface groups requested here. No priority is claimed.

### One-puncture peripheral threshold: A.16

Finite abelian covers of a once-punctured surface have at least three cusps after choosing the cofinal family of deck degrees>=3. In the cusp homology module Z_Sigma^Q/Z_Sigma(sum e_q), an equality n e_q=a e_1 forces q=1 and a=n. This puts every peripheral power-centralizer into the derived subgroup. At depth2 that subgroup is abelian and is the entire centralizer. At depth>=3 the same cover makes c a primitive free-basis element, so the finite-rank free theorem at one smaller depth applies. A.15 then descends the result back to the original quotient. The strict metabelian inclusion is certified by explicit UT4 matrices at p=2,3,5 and by the same symbolic matrix calculation at any p in Sigma.

### Exact source applications

- Mochizuki–Tamagawa, Definition1.2, Remark1.2.2 and Proposition1.4 apply to hyperbolic geometric surface groups over an algebraically closed characteristic-zero field and an arbitrary nontrivial full formation. The ordinary/full/pro-p presentation comparisons and the deduction of torsion-freeness from finite p-cohomological dimension are written out.
- Mochizuki2004 Lemma1.3.7 gives commensurable terminality for both full and pro-l cusp inertia. A centralizer of an integer power lies in that commensurator, giving A.7.
- Mochizuki2007 Proposition1.2(i) identifies underlying edges when an intersection is open in one. It does not literally identify arbitrary chosen conjugate subgroup representatives. A.5 therefore proves its one-sided transporter assertion using exact power-centralizers and compact recurrence, with no strengthened quotation of Proposition1.2(i).
- Closed base-loop centralizers in the unquotiented completion are obtained twice, from Boggi–Zalesskii2019 Proposition3.6 and from Mochizuki2007 Proposition1.2(ii) after a one-node degeneration. Genus2 is checked explicitly: its normalization has genus1 and two inverse branches, hence remains stable and hyperbolic.
- The finite-rank part of Yamaguchi2026 Theorem1.5 is used in A.14. Its finite semidirect-product step, metabelian module step and descent to finite abelian covers were read. No infinite-rank limiting argument is imported. A.17 independently checks the cover/transfer proof of the centre and torsion statements. A.19 independently proves the precise Magnus embedding used in the closed argument.
- Yagasaki's actual supplied TeX was read. The compact marked-surface case needed for A.12 lies in Lemma2.1; the finite marked set is a compact subpolyhedron. We also read Theorem1.1 and the local-extension theorem. This avoids treating a statement about diffeomorphisms as one about compact-open homeomorphisms without a comparison.
- Farb–Margalit Theorem4.6 includes punctures/boundary and has an explicit extended-group remark. Theorem8.8 is the extended punctured Dehn–Nielsen–Baer theorem. A.12 uses the inverse-track convention needed to make point-pushing a homomorphism and checks its induced inner automorphism. The book's p235 informal phrase about a unique representative fixing the distinguished loop is not used: conjugation by that loop supplies many representatives. The quotient automorphism is unique because those residual conjugations die upon filling.

## Corrections and typed comparisons

The bracket nu<=3 on scan116 is false at the pair of pants; the correct bound is nu<=2. The rank2g+nu-1 requires nu>=1. The admitted plane retains its noninjective peripheral source map, while the closed sphere is excluded from the nontrivial orientation-by-group-cohomology definition. The early cohomological orientation marking is related to the later covariant orientation line by an explicit dual map, rather than an unmarked inversion of its character.

The torus needs the same H² extension-class correction as the annulus. The pure orientation-preserving index on scan189 is exactly2nu!, where nu counts the old punctures. In the abelian filling exception, forgetting annulus peripheral indices and orientation loses a C2; retaining the complete data restores the four-element target and the isomorphism. The scan194 abelian labels refer to filled types; both drilled groups there are F2.

The phrase relation génératrice on scan318 gives the full profinite presentation, hence the explicit isomorphism to the standard completion. The Zhat² example refutes only the weakened requirement that a generating tuple satisfy the equation. It is not presented as a counterexample to the actual full-presentation axiom.

A.20 has all four domains and the completion comparison maps written out. The discrete filling isomorphism gives an isomorphism of the full completions of the two discrete automorphism groups. It also gives the commutative square with the separately defined normalized filling map on all continuous automorphisms. Neither vertical surjectivity nor a bottom-arrow isomorphism is needed for A(d). For odd p the proposed replacement of the upper full completions by pro-p completions has an explicit obstruction: an orientation-reversing involution is killed in a pro-p group while acting by -1 on the pro-p orientation line.

## Sources actually read and searches

The primary local PDFs for Mochizuki2004, Mochizuki2007, Mochizuki–Tamagawa2008 and Nakamura1994 were extracted and their relevant theorem statements and proofs read. Titles were checked on first pages: the 2008 article is *The Algebraic and Anabelian Geometry of Configuration Spaces*; the 1994 article is *Galois Rigidity of Pure Sphere Braid Groups and Profinite Calculus*. Publisher metadata for the former and for Mochizuki2007 was opened. Boggi–Zalesskii2019 was opened in its author arXiv PDF and Proposition3.6 read. Yamaguchi's supplied source and arXivv4 HTML were opened. Yagasaki's primary supplied source was read.

The Farb–Margalit author URL returned403 and the Pisa/KIAS mirrors timed out. An actual primary book copy was then opened successfully at https://euclid.nmu.edu/~joshthom/teaching/ma589/farbmarg.pdf; the case-sensitive lowercase path matters. The precise statements and adjacent remarks were inspected there. All bibliography entries in this Part A file are consequently marked verified. An original Ihara1999 proof was searched for while auditing the Magnus step; its bibliography and RIMS1177 listing were found, but no original text was obtained. No claim is made that it was read, it is not a relied-on bibliography entry, and the required embedding was proved directly in A.19.

Before recording the finite-step arguments, searches included combinations of “finite-step solvable surface group centralizer,” “profinite metabelian surface group centralizer,” “peripheral product commutators solvable quotient,” the exact Yamaguchi title/arXiv identifier, and “Ihara Blanchfield Lyndon Theorem A-2.” The actual proof stands independently of any claim that those searches are exhaustive. No newness or priority claim is made.

The prior LM3 return and review were consulted as leads and compared with the new proofs of Lemme5 and the two closed-loop source reductions. Their status labels are not used as authority. The initially suspected absence of prior-return source files was rechecked and disproved; the files are present and no missing-file limitation remains.

## Computation and files

`code/check_part_a.py` uses only the Python standard library. The run completed successfully and wrote `code/check_part_a_output.json`. It enumerates the UT4 groups at p=2,3,5; verifies that each generated group is metabelian; computes c and its conjugate; checks that the conjugate is outside the cyclic subgroup generated by c; checks the genus2 relation in the same finite group; verifies the pair-of-pants filling kernel automorphism as exact free words; and checks the finite abelian weakened-presentation example. The output explicitly warns that a large centralizer in a finite quotient alone is not an inverse-limit counterexample.

The LaTeX fragment uses the common macros requested by the root document plus standard LaTeX/amsmath/amsfonts commands. It defines no global preamble. Actual manuscript scan images were inspected for every reading recorded in `readings.json`; reduced inspection images are only working aids. The root document owns the final LuaLaTeX compilation, overflow audit, rendering and PDF pagination, so this fragment report does not claim a PDF inspection that has not been performed here.
