# B5: levels, central data, and the proposed place at infinity

Research-only comparison, 17 November 2026, by GPT-6 Astra Pro $`package_support`$. The parent task froze the transcription at 23:01:38 UTC before opening the context. This work used that frozen text, not the scans, and changed no transcription. It is a contribution to the research notes, not a referee report on the earlier research returns.

## Finding and scope

**This range gives an explicit smooth moduli problem with Legendre–Jacobi pinning of level 2, a finite group of changes of pinning, and an announced comparison with relative level 4. It does not work out the proposed place at infinity of the elliptic modular curve.** Its occurrences of infinity must be distinguished: a label in the ordered triple, an omitted value of the moduli parameter, the pole of a function on an individual elliptic curve, and the subscript of a filtered union. None is accompanied here by a degenerating family and its inertia action. This conclusion concerns scans 078–115 only; it does not refute an announcement about the whole of cote 64.

The strongest concrete addition to B5 is the displayed finite lift

\[
D'_3=S_3\times_{\mathbf Z/2}(\mathbf Z/4)
\]

and its character to fourth roots of unity. It is the same abstract central extension as the quotient by the normal complement singled out in the supplied Longue Marche notes for scan 529, as detailed in B5-03 below. It also makes central information visible on a line while that information is absent from the action on the moduli base. These are concrete geometric and group-theoretic links; a compatible identification of families or monodromy has not been constructed here. They are not an all-level congruence theorem, a computation of an arithmetic image, or a classification of profinite torsion.

### Citation convention and limitations

`Pnnn` below means the exact file `MPL_64_078-115/pages/MPL_64_078-115_64_scannnn.tex`, at its `\scanpage{nnn}` marker. Thus, for example, **P090** is `MPL_64_078-115/pages/MPL_64_078-115_64_scan090.tex`, scan 090. Equation numbers are those of the frozen text. Context citations give the full relative filename and its scan or note identifier. The complete frozen range 078–115 was examined as text for this comparison; the requested comparison with 078–100 was then checked against the continuation 101–115 so that a claim about the whole range would not rest on the first part alone.

Some letters in the permutation-group notation remain marked `\unsure{\mathfrak S|\mathcal G}`; this report interprets the described permutations of the three-element set as $S_3$ without changing that reading. The geometric equivalences and representability statements are reported as statements of the manuscript. The finite abstract-group calculation in B5-03 is the only new mathematical verification made here. No external theorem or claim in another project's notes was independently verified in this contribution.

## Proposed note B5-01 — The announced modular cusp is not worked out in this excerpt

**Kind:** documentary scope check; confidence high for this range.

The planning document says cote 64 is announced by cote 149 scans 99–101 as the place at infinity of the modular curve of type (1,1), but explicitly calls this a guess made before the pages were read (`context/README.md`, “What our planning document asks of these folders”). The provided `context/MPL_149_091-136_notes.md`, **RN099-03**, reports the proposal “courbe modulaire pour courbes elliptiques” at scan 099, continuing 100; **RN101-04** reports “structure à l’infini” at scan 101. These are citations to the supplied research notes, not to an independently inspected transcription or image of cote 149. RN099-03's Tate-curve calculation is an earlier note's addition, not text recovered in the present cote 64 excerpt, and its correctness has not been rechecked here.

The current excerpt describes the open locus explicitly. **P080** has $t\in U_{0,3}=\mathbf P^1\setminus\{0,1,\infty\}$; **P082**, following equations (30)–(33), takes $t\in\Sigma_J^*=\Sigma_J\setminus D_J$; **P085–P086**, equations (35)–(37), give the marked moduli scheme $U_{0,3}\times\mu_4^*$. An omitted value of this parameter is a possible boundary direction to investigate. The excerpt does not extend the family over it, select a tangential base point, or calculate the associated inertia.

The later infinity is especially liable to misidentification. **P109**, equation (34), imposes a nonzero discriminant, constructs a smooth elliptic curve, and then makes the image of its origin the infinity of the quotient coordinate: $\Sigma_J\simeq\mathbf P^1, t\mapsto\infty$, equation (37). **P114**, equation (54), says $\wp(0_E)=\infty$; equations (57)–(58) discuss the finite images of the nonzero 2-torsion and the ramification of $\wp$. This infinity is on the quotient of an individual smooth elliptic curve. The chosen coordinate sends a point of $\Sigma_J\setminus D_J$ to infinity, while the level 2 labels previously marked the three points of $D_J$. The two coordinate uses therefore cannot be identified merely because both print “∞”.

For comparison, an explicit cusp passage is already supplied in **`context/LM_140-3_text.tex`, scan 025, §39**, where “point à l’infini de $M_{1,1,\mathbf Q}$” introduces a cusp-inertia map and an asserted lower-unipotent image in $SL_2(\widehat{\mathbf Z})$, qualified “sauf erreur.” The same scan's multiplier discussion is marked “faire la vérification”; the supplied **`context/LM_140-3_notes.md`, LM_P061, notes 10–13 and own note E**, distinguishes that assertion from the failed uniqueness of a full unit multiplier on an outer congruence action. Those are context leads and prior checks, not newly proved here.

**Consequence.** This excerpt supplies coordinates and pinning data for a possible later boundary calculation. It supplies neither the Tate-cusp calculation proposed in RN099-03 nor the missing specification of inertia, generator convention, and actual versus outer action. A useful next question would be to extend the displayed smooth family toward the omitted parameter values and make those choices explicit; that work has not been done in this note. No conclusion is drawn about cote 64 outside 078–115.

**Search audit.** Across all 38 frozen page files, searches used `infini`, `infty`, `cusp`, `place`, `monod`, `inert`, `Tate`, `dégén`, `degener`, `compact`, `discrimin`, and `Delta`. The `infty` hits were classified by their local context; the discriminant occurs at 109; `Delta` also matches many derivative symbols and is not evidence of a boundary discriminant calculation. No cusp, inertia, Tate, monodromy, degeneration, or compactification discussion was located. Context searches used `99`, `100`, `101`, `infini`, `modulaire`, and `congruence`, followed by the exact passages cited above. The negative result rests on the complete text comparison, not keyword absence alone.

## Proposed note B5-02 — Level 2 is present; relative level 4 is a stated task

**Kind:** documentary scope check; confidence high.

**P079** defines a Legendre–Jacobi pinning of “échelon 2” by combining a Legendre pinning with a bijection $J\simeq\{0,1,\infty\}$. **P081**, equation (28), identifies $J$ with the nonzero 2-torsion of the elliptic curve; **P085**, equation (35), repeats its trivialization over a base. **P080** specifies the base $S_0=\operatorname{Spec}\mathbf Z[1/2]$. The manuscript asserts rigidity for the combined structure and representability by $U_{0,3}\times\mu_4^*$ in **P085–P086**. The extra choice in $\mu_4^*$ is a root of $-1$, called the “donnée arithmétique” in **P079**; it must not be silently discarded when reporting the stated moduli problem.

Level 4 occurs as a motivation and an agenda. **P088** says that an alternative definition of Legendre pinning would have a less attractive relation with Jacobi pinnings of level 4. **P093** then says “Il faut maintenant définir” those level 4 pinnings relative to level 2, describes sections of ${}_4E\to{}_2E$ above $J_E$ with a fibrewise sum condition, and says one must show how they canonically give a Legendre pinning. **P094** begins “Mais avant, un commentaire”; **P094–P100** discuss square-root data, torsors and pinning formulas, and **P101–P115** turn to Weierstrass functions. The announced level 4 to Legendre construction is not completed explicitly in these pages. The level 4 reference is real; a full level 4 congruence action or an arbitrary-level tower is not supplied.

This is closely related to, but more finely pinned than, **`context/LM_140-2_text.tex`, scans 517–519**: a four-pointed line yields the elliptic double-cover picture, while $-1$ acts trivially on the quotient and forces care with rigidification. That context passage also discusses general Jacobi level $n$, and **scan 533**, §37, titles the subsequent discussion “rigidification d’échelon 2.” The general-$n$ material belongs to the Longue Marche context; it cannot be imported into cote 64 as though printed in 078–115.

**Consequence for LM2 C.d1.** The explicit level 2 geometry is useful input for recognizing the elementary elliptic/four-pointed-line bridge. It does not define every projective congruence kernel or an action of every actual $GT_0$ loop automorphism on those kernels. The row's label remains **Known (the return's unreviewed claim)** in `context/LM2_CONGRUENCE_ROWS.md`; this note neither reproves it nor provides a counterexample.

**Search audit.** Across 078–115: `échelon`, `echelon`, `niveau`, `congru`, `SL.?2`, `GT`, `widehat`, and explicit `échelon`/`niveau` patterns for 5,7,11. The relevant level hits are 079,085,088–089,093; no congruence-tower or $GT_0$ discussion was found. Context searches used `Legendre`, `Jacobi`, `rigidification`, `congruence`, and the `scanpage` markers 517–519 and 533–538.

## Proposed note B5-03 — A verified finite central lift, with a strict limit on the analogy to LM2 C.r1–r3

**Kind:** targeted finite-group verification and scope comparison; confidence high for the calculation, no claim of a profinite lifting theorem.

**P089–P090**, equations (45)–(50), describe an action of $\mu_4\times S_3$ on $U_{0,3}\times\mu_4^*$: $S_3$ acts on the first factor, and the second factor sees the mixed character $\operatorname{sg}(g)\zeta^2$. Its stabilizer is the fibre product $D'_3=S_3\times_{\mathbf Z/2}\mathbf Z/4$ after choosing a root of $-1$. **P091** calls the resulting structures direct; **P092**, equations (51bis)–(54), gives the character $\chi_4:D'_3\to\mu_4$ and inserts the assertion $D'_{3,\mathrm{ab}}\simeq\mu_4$.

Here is a direct check of that last finite-group assertion, using the permutation interpretation of the uncertain group letter. Write

\[
D=\{(p,a)\in S_3\times\mathbf Z/4:\operatorname{parity}(p)=a\bmod2\}.
\]

It has 12 elements. The second projection is onto $\mathbf Z/4$, with kernel $A_3\times\{0\}$. Let $r=(c,0)$ for a 3-cycle and $s=(t,1)$ for a transposition. Then $srs^{-1}=r^{-1}$, so $[s,r]=r^{-2}=r$. Thus the commutator subgroup is exactly $A_3\times\{0\}$, and $D_{\mathrm{ab}}\simeq\mathbf Z/4$. The projection $D\to S_3$ has central kernel $\{(1,0),(1,2)\}$; every lift of a transposition squares to $(1,2)$, so has order 4. In particular this central extension does not split. An independent enumeration of all 12 elements and all 144 commutators gave the same kernel, commutator subgroup, and orders.

### Concrete bridge to the Longue Marche's normal complement

**context/LM_140-2_text.tex, scans 527–529**, provides the Legendre family, discusses its lift from the four-pointed-line group, and asks about four complements to the centre in $\Gamma(2)$. The lower margin of **scan 529** conjectures normality in $SL_2(\mathbf Z)$ and calls the resulting quotient a potentially interesting central extension of $S_3$ by $\{\pm1\}$. That is a more precise antecedent for **P090–P092** than the generic observation that both passages concern level 2.

The supplied second-pass notes **context/LM_140-2_notes.md, LM_P053, S07–S09**, distinguish the complements. For $\gamma=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\in\Gamma(2)$ they define $\varepsilon(\gamma)=a\bmod4\in\{\pm1\}$, $\beta(\gamma)=(-1)^{b/2}$, and $\kappa(\gamma)=(-1)^{c/2}$. **S09** reports that $H=\ker(\varepsilon\beta\kappa)$ is the unique complement normal in $SL_2(\mathbf Z)$, whereas the untwisted Legendre image $\ker\varepsilon$ is not normal; the quotient $Q=SL_2(\mathbf Z)/H$ is the dicyclic group $C_3\rtimes C_4$ of order 12. These are the supplied note's checked claims, not a new proof of normality in this contribution.

The finite group $D$ checked above has exactly the same presentation:

\[
D=\langle r,s\mid r^3=1,\ s^4=1,\ srs^{-1}=r^{-1}\rangle,
\qquad s^2=(1,2).
\]

Thus, conditional on S09's stated description of $Q$, it is isomorphic to $Q$ as a central extension of $S_3$ by $C_2$, after matching a 3-cycle, a transposition and the central involution. Concretely, the generators can be matched with the classes of $(ST)^2$ and $S$ in $Q$, with $S=\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)$ and $T=\left(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\right)$, up to the chosen identification of the permutation generators. This identifies the abstract finite extension promised in LM scan 529 with the kind displayed in cote 64 scan 090. It does not identify the maps into it or select compatible base points.

There is a plausible family-level link, but the supplied notes themselves qualify it. **LM_P053 S06** says that the twists $u\,y^2=x(x-1)(x-\lambda)$ for $u=1,\lambda,1-\lambda,\lambda(1-\lambda)$ realize the four lifts, labels the idea confidence medium, and asks for a check against the outer-homomorphism convention. **S09**, with its R31 matrix conventions, associates the normal complement with the $\lambda(1-\lambda)$ twist. Matching the present universally pinned curve with that particular twist would require an explicit comparison of the parameter, family, loop generators and linearization. Neither the abstract group calculation nor the order 12 alone provides those identifications. No compatible family or monodromy comparison, cusp calculation, or all-level conclusion is claimed here.

The source's action formula also separates two data sets: the element represented by $(1,-1)\in S_3\times\mu_4$ acts trivially on the base in equation (47), while equation (51) multiplies the indicated $\mathcal O(1)$ line by $-1$. This is a concrete finite example of information lost upon forgetting linear pinning data. It does **not** identify a kernel for an action of $GT_0$.

The character $\chi_4$ is typed as $D'_3\to\mu_4$; it is neither a map from an absolute Galois group nor a character to $\widehat{\mathbf Z}^{\times}$. Even the target $\mu_4$ must not be confused with $(\mathbf Z/4)^{\times}$. Therefore it cannot restore the unique unit multiplier whose loss is the subject of **LM2 C.r2**. **`context/LM_140-3_text.tex`, scans 022–024**, discusses the arithmetic outer congruence action through units modulo squares; **scans 025–026** contain the proposed full multiplier; the supplied **LM_P061 notes 12–13 and own note E** explain the square ambiguity. These earlier claims are not reproved here.

For **LM2 C.r3**, the finite example illustrates why the objects and quotients must be specified, but it computes none of the genuine or outer arithmetic images in that row. The relevant context also explicitly pulls back a central extension in **`context/LM_140-3_text.tex`, scans 176–178**, equations (19)–(21); **scan 177** admits a comparison with §39 rather than proving it, and **scan 178** leaves the arithmetic subgroup to characterize. These qualifications concern the manuscript passage and are not a new objection to a later research return that might supply additional arguments.

**Status retained.** `context/LM2_CONGRUENCE_ROWS.md` labels C.r1 **Proved**, C.r2 **Refuted**, and C.r3 **Proved**, all as unreviewed return claims. C.r2 is listed there under the correction about loss of a unique multiplier; no status is changed here. The finite verification supports only the displayed $D'_3$ calculation and the stated distinction between base and line actions.

**Search audit.** Current-source searches used `D.*3`, `chi_4`, `caractère`, `car.`, `pm1`, `sg`, `torseur`, `arithm`, `congru`, and `cyclot`, then inspected 089–093. Context searches used `carrés`, `scalaire`, `faire la vérification`, `unique`, and the scan markers 022–026 and 176–178; the cited context notes were checked for the scope of their own corrections. The additional normal-complement comparison used LM_P053 S06–S09 and source scans 527–529, with the exact note labels and scan markers as locators.

## Proposed note B5-04 — The automorphisms here do not answer LM4 D.12

**Kind:** scope comparison; confidence high about what the pages do not establish.

The manuscript itself distinguishes its moduli problems. **P084–P085** says Legendre pinning alone need not be rigid, examines surviving permutations in the alternating subgroup of the three-element marking, and calls the exceptional case “hexagonale.” It then introduces the additional Jacobi level 2 marking “Pour éliminer les autom.” and asserts rigidity of the combined problem, **P085–P086**. This explains the apparent difference from **P079**, whose rigidity statement already concerns the combined Legendre–Jacobi structure. The finite group checked in B5-03 is a group of changes of pinning; it is not a new collection of automorphisms of an object with every pinning fixed.

**LM4 D.12** concerns torsion in full profinite $GT_0$ and full low-type groups. `context/notes/RESULTS_STATE.md` lists it **Open (the return's claim)** and reports D.29's counterexample to a finite geometric-recognition assertion for type (0,4). This excerpt does not construct arbitrary profinite torsion, classify involutions, or prove that a preserved peripheral system realizes a geometric action. Its concrete geometric stabilizer discussion therefore neither resolves D.12 nor reverses the reported D.29 result. The detailed all-characteristic geometry behind the manuscript's hexagonal description has not been independently verified in this contribution.

**Search audit.** Across 078–115: `rigide`, `autom`, `exceptionnelle`, `hexagon`, `ordre`, `torsion`, `involu`, `GT`; the relevant moduli passages are 079,084–086. Later involutions concern the Weierstrass quotient and translations, particularly 114–115, not elements of full profinite $GT_0$. Context was searched for the exact statement identifier `LM4 D.12` and its reported D.29 qualification.

## Proposed note B5-05 — Arithmetic pinning data are not the arithmetic image of EXIT_TOWER E.24

**Kind:** scope comparison; confidence high.

The excerpt does contain arithmetic data: **P079–P080** singles out the root of $-1$, and **P090–P093** passes to the base $\widetilde S_0=\mu_4^*$ where direct pinnings and the constant finite group can be used. **P089–P092** makes the relabelling and scalar characters explicit. This is useful for specifying which base and which linear data a proposed comparison should retain.

It is not a calculation of the arithmetic subgroup inside the full outer automorphism groups preserving boundary inertia and centralizing relabellings. The finite $S_3$ relabelling on $U_{0,3}$ does not supply that target group, its exact indices, or witness tests. No absolute-Galois action on those full groups is constructed on these pages, and the cusp-inertia calculation needed to relate the boundary data is absent for the reasons in B5-01. **EXIT_TOWER E.24** therefore remains **Open (the return's claim)** as recorded in `context/notes/RESULTS_STATE.md`. That register entry is itself an excerpt whose displayed formula is truncated; this note does not reconstruct the omitted exact targets or assert a comparison theorem with them.

**Search audit.** Across 078–115: `arithm`, `modulaire`, `Galois`, `lacets`, `inert`, `cyclot`, `congru`; the positive hits are pinning/moduli passages 079,086,089,091–093. The context check used the exact identifier `EXIT_TOWER E.24`, its stated boundary-inertia condition, and the genuine/outer passages of LM cited in B5-03.

## Proposed note B5-06 — The higher kernels of LM4_SUCCESSOR B.38 are untouched

**Kind:** scope comparison; confidence high.

The only levels explicitly named in the current excerpt are 2 and 4, with the latter still a proposed relative construction at **P093**. No kernel $\mathcal K_5,\mathcal K_7,\mathcal K_{11}$, no compatible all-$N$ family of kernels, and no compactification of the corresponding higher-level quotient is calculated. The occurrence of $\mu_4$, or the twelve-element group $D'_3$, cannot by itself serve as evidence for those higher-level assertions.

`context/notes/RESULTS_STATE.md` lists **LM4_SUCCESSOR B.38** as **Open (the return's claim)**, expressly leaving $\mathcal K_5=1$ and the level 7 and 11 kernels undecided. The present source adds an explicit low-level geometric model that could be used in a future comparison. It supplies no new argument about any of those three kernels, so no status change is proposed. The register's reported genera and broader claims about the centralizer problem are not used as independent facts here.

**Search audit.** Across 078–115: `échelon`, `niveau`, `congru`, `K_N`, `mathcal.?K`, `GT`, `compact`, plus level-specific patterns for 5,7,11. The only relevant hits remain 079,085,088–089,093. The context check used the exact identifier `LM4_SUCCESSOR B.38` and the explicit list of its unresolved levels.

## Check-event policy for this contribution

`records/check_events_b5.tsv` proposes entries for the actual documentary comparisons, the finite calculation, and the prior statements used to delimit the conclusions. It contains no event for merely opening or reading a file. A background-use or source-scope event is not a proof check of the corresponding research return, and none upgrades its status. The finite-group event is local to B5-03. The parent editor may merge these proposals into the package's canonical check history while retaining that distinction. The timestamp 2026-11-17 23:13:07 UTC records the preparation of these event proposals, after the checks and uses described; it is not a reconstructed start time for each action. The effort setting is not exposed to this agent.
