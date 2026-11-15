# Post-freeze research memo: early handwritten sequence

Scope: cote33, even scans002–036. This is a research draft for the parent agent, based solely on the frozen text and supplied context; no image was viewed and no transcription, doubt, inventory or progress file was modified. The full README, RESULTS_STATE and same-cote research notes were read. External primary literature has not been independently verified in this memo and is being handled in the main research pass. In mathematical discussion, gamma denotes the first proposed reading of the still-doubtful gamma/sigma fundamental-class glyph; this convention does not settle that reading.

The source-line locators below are exact lines in the frozen individual `.tex` files, not physical manuscript line counts. Supplied same-cote notes are first-pass leads, never treated as established results. A context relation marked “adds” means new scan evidence or a distinct check, not historical novelty or proof priority.

## E01. The programme begins with formalism and ends with L-functions

**File:** cote33. **Scans:** 002. **TeX lines:** 3–9. **Kind:** unpursued implication.

“Nous prendrons comme prétexte la théorie des fonctions $L$” explicitly orders torsion duality/Künneth/Lefschetz, extension to $l$-adic coefficients, and applications to $L$-functions. This is direct evidence for the README's SGA 4/5 placement, while these opening pages do not by themselves substantiate a developed SGA 7 monodromy argument. The later supplied lead that the author prefers to complete the formalism before applications restates this priority, although scan order cannot establish the sheets' dates.

**Context comparison:** same_cote_33/MPL_33_098-146_notes.md, N20–N21, scan122: restates the programme and adds its opening three-part order; N24, scan128: the finite-level-to-adic passage is still reported as an expectation.

**Results-state connection:** Bears on MPL_33_098-146 N20 and N21; differs in subject from WG H9 and WG2 §2.1 #2. No mathematical result status is changed.

**Search record:** `research_context_early_searches.json`, E01; terms: fonctions, formalism, adic, Lefschetz, SGA 4.

## E02. The field example requires a precise site/topos convention

**File:** cote33. **Scans:** 002. **TeX lines:** 22–38. **Kind:** reading question.

The displayed $X_{\mathrm{ét}}\simeq\widetilde X_{\mathrm{ét}}\simeq\operatorname{Ens}(\pi)$ places the site notation and its topos beside the same Galois-action category. A reconstruction should recover whether the site admits all étale schemes or only a finite-presentation basis, and whether continuity/discreteness is included in $\operatorname{Ens}(\pi)$, rather than identifying arbitrary profinite actions with étale sheaves. This is a convention question attached to the literal display, not an emendation of it.

**Context comparison:** same_cote_33/MPL_33_098-146_notes.md, N54–N55, scan145: adds an actual field/Galois example to the separately reused axiomatic étale source; those notes do not settle this notation convention.

**Results-state connection:** Related to MPL_33_098-146 N54 only as a separate étale-scope caution; no direct bearing on LM7 E.23 or LM7_PUSH C.6.

**Search record:** `research_context_early_searches.json`, E02; terms: Ens, Galois, étale, axiom.

## E03. Strict localization supplies the local test behind later reductions

**File:** cote33. **Scans:** 004. **TeX lines:** 14–43. **Kind:** unpursued implication.

“La famille des foncteurs fibres est conservative” is followed by the strict-local expression for a stalk and an application to the fibres of $R^qf_*$. These statements supply the local testing mechanism used later for base change and comparison maps; the NB about lacking a complete ordinary-topological analogue is a caution about the model, not an explicit mathematical doubt. A detailed proof must retain the quasi-compact/quasi-separated condition attached to the direct-image application.

**Context comparison:** same_cote_33/MPL_33_098-146_notes.md, N12, scan114: adds the strict-local foundation of the reported geometric-fibre proof proposal; N18, scan120: adds the boundary stalk viewpoint behind that note's support example.

**Results-state connection:** Adds to the S19 mapping programme in README.md; no directly matching settled RESULTS_STATE entry.

**Search record:** `research_context_early_searches.json`, E03; terms: stalk, strict, geometric fibres, localization, quasi.

## E04. Proper and smooth base change have different coefficient scopes

**File:** cote33. **Scans:** 004,006. **TeX lines:** 004:50; 006:4–18. **Kind:** unproved claim.

The proper theorem is stated for a “faisceau de torsion” and arbitrary base change, while the nonproper smooth-base-change NB requires $F$ “premier aux car. rés.”. The extension-of-separably-closed-fields example repeats the same proper/nonproper distinction. A reconstruction should preserve this separation instead of importing the invertibility condition into every proper statement or dropping it from the nonproper addition.

**Context comparison:** same_cote_33/MPL_33_098-146_notes.md, N14, scans118–120, and N15, scan118: adds the base-change foundations for their proper-factor and nonproper Künneth distinction; no contradiction is established.

**Results-state connection:** Bears on MPL_33_098-146 N15; that entry remains a first-pass lead.

**Search record:** `research_context_early_searches.json`, E04; terms: proper base change, prime-to-characteristic, one proper, invertible, 118.

## E05. The analytic comparison is widened on the sheet

**File:** cote33. **Scans:** 006,008. **TeX lines:** 006:20–32; 008:2–13. **Kind:** withdrawn in the same text.

In the relative comparison sentence the qualifier “propre” is cancelled and “de type fini” remains, while the following proper analytic-algebra remark is cancelled as a whole. Scan008 restarts the relative analytic discussion and explicitly leaves its isomorphism claim to prove. The cancellation therefore records a changed exposition and scope, not a proof that analytic comparison or proper spreading is false.

**Context comparison:** same_cote_33/MPL_33_098-146_notes.md, N36, scans144–146: differs in mathematical subject but restates the need to distinguish cancelled exposition from a retracted theorem; no same analytic comparison passage is supplied.

**Results-state connection:** Bears on MPL_33_098-146 N36 as an evidentiary comparison only, and adds a separate S19 analytic-comparison locus.

**Search record:** `research_context_early_searches.json`, E05; terms: analytic, comparison, cancelled, restarts, N36.

## E06. The GAGA margin needs an algebraic constructibility convention

**File:** cote33. **Scans:** 006. **TeX lines:** 30. **Kind:** own idea.

The asserted “équivalence des catégories” of algebraic and analytic constructible torsion sheaves needs its constructibility convention or a properness hypothesis recovered. Under the usual local analytic-stratification convention, on $\mathbb C$ the finite-coefficient sheaf supported on the closed discrete analytic set $\mathbb Z=V(\sin\pi z)$ is analytically constructible, whereas its support is not an algebraically constructible subset of $\mathbb A^1_{\mathbb C}$. This is a conditional scope test for the isolated margin, not a claim that an algebraically stratified comparison theorem is false.

**Confidence and reason:** High for the stated support obstruction; medium for its applicability to the manuscript until the analytic-constructibility convention is recovered. Primary-literature verification is assigned to the main research pass.

**Context comparison:** same_cote_33/MPL_33_098-146_notes.md: searches for analytic constructibility/GAGA find no same-point theorem; N42, scan099, concerns an unrelated analytic operator sheet, while N19, scans112/120, cautions against enlarging a different constructibility-like scope. Adds a distinct question to README.md/S19.

**Results-state connection:** No RESULTS_STATE theorem settles this point; do not identify it with MPL_33_098-146 N25 or N41.

**Search record:** `research_context_early_searches.json`, E06; terms: GAGA, analytic, constructible, stratif.

## E07. Relative analytic comparison is explicitly unproved

**File:** cote33. **Scans:** 008. **TeX lines:** 6–13. **Kind:** self-flagged: a step he himself marks as unverified.

“À prouver que ce sont des isomorphismes” refers to both the cohomology comparison and the relative direct-image comparison for the written “schéma relatif” over an analytic base. The page gives the comparison maps but no argument proving them isomorphisms. The scope, the site on such a relative object, and compatibility with the analytic base must be supplied by a reconstruction.

**Context comparison:** same_cote_33/MPL_33_098-146_notes.md, N12, scan114: differs from its explicit functoriality problem for projection; no same relative analytic theorem occurs in the supplied context. Adds a new self-flagged step to README.md/S19.

**Results-state connection:** Bears on MPL_33_098-146 §65 by adding a distinct explicit verification to the archive-wide inventory; no same-point result is registered.

**Search record:** `research_context_early_searches.json`, E07; terms: À prouver, analytic, isomorphismes, Il faut vérifier, relative.

## E08. Rigid analytic comparison is a stated expectation

**File:** cote33. **Scans:** 008. **TeX lines:** 15. **Kind:** conjecture.

“Devrait aussi se généraliser au contexte rigide analytique” proposes transferring the relative comparison to a further analytic setting. Neither the coefficient restrictions nor the intended rigid site are specified in this brief margin. Its literal status is an expectation, independent of whether later comparison theorems validate an appropriately formulated version.

**Context comparison:** same_cote_33/MPL_33_098-146_notes.md: no match for rigid analytique/rigid comparison; N03, scan102, asks a different extension-to-general-topoi question. Adds a previously unlisted analytic direction to README.md.

**Results-state connection:** Adds to MPL_33_098-146 §65 only as a separate self-flagged/expectation index; no LM or WG result is implicated.

**Search record:** `research_context_early_searches.json`, E08; terms: rigid, rigide, general topoi, topos généraux.

## E09. The analytic-germ calculation is conditional on comparison and continuity

**File:** cote33. **Scans:** 008. **TeX lines:** 17–26. **Kind:** unproved claim.

“Passant à la limite … on trouverait alors” makes the local analytic-ring calculation conditional on the preceding comparison claim. The example $X=Y-Z$ then proposes calculating the analytic direct image of locally constant torsion coefficients in algebraic geometry. A proof must justify the neighbourhood limit and the identification of the algebraic germ, not merely repeat the unproved comparison maps.

**Context comparison:** same_cote_33/MPL_33_098-146_notes.md, N24 and N40, scan128 and scans128/132/146: differs from their adic inverse-limit problem; adds a neighbourhood-limit problem with a different indexing direction and geometric object.

**Results-state connection:** Bears on MPL_33_098-146 N40 as a methodological contrast; it does not reuse that finite-projective compatibility test as a proof.

**Search record:** `research_context_early_searches.json`, E09; terms: limite, limit, analytic, neighbourhood, N40.

## E10. Smooth proper specialization is stated without its dévissage

**File:** cote33. **Scans:** 010. **TeX lines:** 2. **Kind:** unproved claim.

For proper smooth $f$ and prime-to-residue-characteristic locally free torsion $F$, the page states that the $R^qf_*F$ “sont loc. libres.” The preceding proper/smooth base-change tools suggest the mechanism, but no proof of local constancy or preservation of the stated module condition is written here. A reconstruction must distinguish finite locally constant sheaves from locally free modules over a fixed coefficient ring if “loc. libres” is read literally.

**Context comparison:** same_cote_33/MPL_33_098-146_notes.md, N19, scans112/120, and N25, scans126–132: adds a coefficient-freeness question before the later distinction between local constancy, nonprojective cohomology, and perfect complexes.

**Results-state connection:** Bears on MPL_33_098-146 N25 and N23; those notes are leads, not permission to replace the handwritten wording.

**Search record:** `research_context_early_searches.json`, E10; terms: locally constant, free cohomology, nonprojective, proper, N25.

## E11. Cohomological dimension is not the topology of the scheme

**File:** cote33. **Scans:** 010. **TeX lines:** 4–14. **Kind:** unproved claim.

The $2n$ bound and the affine $n$ bound are stated without proof, and the author warns that the affine drop “peut donner des idées fausses.” The warning separates étale cohomological estimates from an unqualified identification of scheme-theoretic dimension with topological dimension. The uncertain strict/non-strict inequality in the first display remains a reading question even when a modern vanishing theorem has a familiar endpoint.

**Context comparison:** same_cote_33/MPL_33_098-146_notes.md, N09, scan110, and N32, scans140–142: adds an absolute/affine starting point to their relative-direct-image and compact-support bounds; those contexts concern different functors.

**Results-state connection:** Bears on MPL_33_098-146 N30 through the need for boundedness, but adds no solution to the open register items.

**Search record:** `research_context_early_searches.json`, E11; terms: cohomological dimension, 2d, affine, absolute, relative.

## E12. The support formalism isolates the low-degree exception

**File:** cote33. **Scans:** 012. **TeX lines:** 14–42. **Kind:** unproved claim.

The support/Ext identifications are accompanied by $\underline H^i_Y(F)=R^{i-1}u_*(F|U)$ only for $i\geq2$, with kernel and cokernel explicitly reserved for degrees zero and one. A proof should recover the localization exact triangle or its injective-resolution predecessor, preserving those low-degree terms. The references “SGA 1962” and “Notes Hartshorne 1961” are source leads rather than proofs supplied on this sheet.

**Context comparison:** same_cote_33/MPL_33_098-146_notes.md, N01, scan098: adds the earlier support calculation behind the later closed-immersion/duality exchange argument; N18, scan120, uses a related boundary-support distinction.

**Results-state connection:** Bears on MPL_33_098-146 N01; no registered result already settles the historical identification of the cited notes.

**Search record:** `research_context_early_searches.json`, E12; terms: closed-immersion, support, localization, Hartshorne, 1962.

## E13. The requested local fundamental class is supplied later

**File:** cote33. **Scans:** 012,022,024. **TeX lines:** 012:52; 022:8–43; 024:3–38. **Kind:** unproved claim.

“Donner définition de la classe fondamentale locale” on012 is answered by the divisor/Kummer construction on022–024 and its complete-intersection product. This is a deferred task that the present package takes up, not an indefinitely unanswered margin. Independence of the local regular sequence remains a separate assertion requiring proof.

**Context comparison:** same_cote_33/MPL_33_098-146_notes.md, N29, scans134–136, and N36–N37, scans144–146: adds a geometric fundamental-class strand to the later categorical/local-trace leads; the context does not reproduce this local class definition.

**Results-state connection:** Bears on MPL_33_098-146 N29 and N37 by supplying geometric input, while their endomorphism-trace constructions are distinct.

**Search record:** `research_context_early_searches.json`, E13; terms: fundamental, classe, Kummer, local trace, duality.

## E14. Tate twists are locally trivial but not canonically constant

**File:** cote33. **Scans:** 014. **TeX lines:** 20–28. **Kind:** unpursued implication.

“surtout pas les confondre” distinguishes $\mu_n$ from the constant $\mathbb Z/n\mathbb Z$ even though they are locally isomorphic in the étale topology. The change-of-primitive-section formula records dependence on an orientation choice; the multiplier must preserve primitivity, and the direction of the chosen isomorphism determines the coordinate convention. These points are reasons to retain Tate twists in the class and trace constructions, rather than identify them globally with constant coefficients.

**Context comparison:** same_cote_33/MPL_33_098-146_notes.md, N23–N24, scans126–128, and N40, scans128/132/146: adds coefficient-orientation data to their integral/adic compatibility concern; there is no same-point discussion of primitive roots or twists.

**Results-state connection:** Bears on MPL_33_098-146 N23 and N40; no registered proof of the twist convention is supplied.

**Search record:** `research_context_early_searches.json`, E14; terms: mu_, twist, primitive, coefficient, integral.

## E15. Absolute purity is formulated as a problem with a conditional route

**File:** cote33. **Scans:** 014,026. **TeX lines:** 014:30–37; 026:40–46. **Kind:** self-flagged: a step he himself marks as unverified.

“Pb sans hypothèse de lissité remplacée par hyp. de régularité” is followed by a claimed characteristic-zero route using resolution of singularities, with the inserted scope “bons préschémas” uncertain. Scan026 later lists the regular/excellent characteristic-zero case among settings for the required low-degree vanishing. This records a problem and a conditional claimed solution in specified cases, not a statement that arbitrary mixed-characteristic absolute purity has already been proved in the draft.

**Context comparison:** same_cote_33/MPL_33_098-146_notes.md, N20, scan122: differs from the curve/Lefschetz expectation “sans résolution des singularités” but adds concrete evidence for the role that resolution and purity play in this programme. No same absolute-purity theorem is provided in the context.

**Results-state connection:** Bears on MPL_33_098-146 N20 and §65; preserves their first-pass status.

**Search record:** `research_context_early_searches.json`, E15; terms: purity, pureté, resolution, résolution, excellent.

## E16. The normal-crossings extension is only a marginal programme

**File:** cote33. **Scans:** 014. **TeX lines:** 42. **Kind:** unproved claim.

“Extension aux div. à croisements normaux” is written beside the purity/compact-support transition without a construction or a precisely stated theorem. The next task is to determine whether it concerns local classes, purity with a stratification, or a related support calculation before assigning it a stronger logarithmic interpretation. Nothing on these pages supplies that identification.

**Context comparison:** same_cote_33/MPL_33_098-146_notes.md, N47, scan123: differs from the reused relative-divisor extension, which has its own missing definitions; no normal-crossings match appears in the supplied context.

**Results-state connection:** Adds to README.md/S19; no directly corresponding RESULTS_STATE entry, and no implication for WG H9 is established merely from divisor vocabulary.

**Search record:** `research_context_early_searches.json`, E16; terms: normal crossings, croisements, divisor, relative divisors, WG H9.

## E17. The nonproper constructibility question is explicitly conditional

**File:** cote33. **Scans:** 016,018. **TeX lines:** 016:16–26; 018:3–11. **Kind:** self-flagged: a step he himself marks as unverified.

The proper constructibility theorem is followed by “Question de la généralisation” to finite-type $f$, reduced to an open immersion and said to hold when resolution “$+$ pureté” is available. This is a substantive extension problem, with the small scope insertions still uncertain. Its coefficient restrictions must be recovered from the invoked purity statement, since the proper theorem itself was stated for torsion coefficients generally.

**Context comparison:** same_cote_33/MPL_33_098-146_notes.md, N15–N16, scan118, and N30, scans136/140/142: adds the open-immersion constructibility issue to their nonproper coefficient and finiteness distinctions; it is not the same Künneth assertion.

**Results-state connection:** Bears on MPL_33_098-146 N15, N20 and N30; no LM result is advanced.

**Search record:** `research_context_early_searches.json`, E17; terms: constructib, nonproper, resolution, purity, open immersion.

## E18. Wild coefficients obstruct the unrestricted open-immersion extension

**File:** cote33. **Scans:** 016,018. **TeX lines:** 016:16–26; 018:3–11. **Kind:** own idea.

If the proposed finite-type extension is read with unrestricted torsion, take $j:\mathbb G_m\hookrightarrow\mathbb A^1$ over an algebraically closed field of characteristic $p$ and coefficients $\mathbb F_p$. At the origin the Artin–Schreier classes $t^{-m}$, for $m>0$ prime to $p$, are linearly independent in the punctured strict-local $H^1$: a nonzero negative-valuation term $h^p-h$ has pole order divisible by $p$. The resulting infinite stalk of $R^1j_*\mathbb F_p$ prevents constructibility, so the purity restriction is essential even on a smooth curve where resolution itself is not the issue.

**Confidence and reason:** High for the stated conditional example: pole orders prove independence; a primary Artin–Schreier reference should be verified by the main literature pass.

**Context comparison:** same_cote_33/MPL_33_098-146_notes.md, N16, scan118: adds an open-boundary stalk counterexample to that note's different mixed-polynomial Künneth test; N15, scan118, reports the prime-to-characteristic repair for its own formula.

**Results-state connection:** Bears on MPL_33_098-146 N15; N16 is in the full supplied note file but not separately listed in RESULTS_STATE. This is not a re-derivation of LM7_PUSH C.6.

**Search record:** `research_context_early_searches.json`, E18; terms: Artin, characteristic-p, open, stalk, prime-to-characteristic.

## E19. Compactification independence is asserted from base change

**File:** cote33. **Scans:** 018,020. **TeX lines:** 018:15–28; 020:3–5. **Kind:** unproved claim.

The construction $R^q\bar f_*(i_!F)$ is said to be independent of the chosen factorization “de façon quasi-triviale du th. du changement de base.” A proof still needs comparison compactifications and compatibility of the induced identifications, not only an objectwise isomorphism. This supplies the construction underlying the later derived compact-support operations rather than a second, unrelated support functor.

**Context comparison:** same_cote_33/MPL_33_098-146_notes.md, N11–N13, scans112–116: adds the compactification-level foundation beneath their projection/Künneth formulas; N12's explicit functoriality question on114 is a related later compatibility obligation.

**Results-state connection:** Bears on MPL_33_098-146 §76 and N01; no same-point settled register result.

**Search record:** `research_context_early_searches.json`, E19; terms: compactif, base change, functorial, independen, compact-support.

## E20. Quasi-finite exactness and étale trace are compressed claims

**File:** cote33. **Scans:** 020. **TeX lines:** 20–39. **Kind:** unproved claim.

The list says that a quasi-finite $f$ has $R^i_!f_*F=0$ for $i>0$, then introduces an étale trace and covariance. Neither the trace construction nor its compatibility with composition and supports is proved here; the repeated numbering “(vi)” is merely retained. A useful reconstruction starts with sums over finite geometric fibres and then checks descent and extension by zero.

**Context comparison:** same_cote_33/MPL_33_098-146_notes.md, N13–N14, scans116–120: adds an elementary étale/finite-fibre input to their compact-support functoriality; N29, scans134–136, concerns a different categorical trace, so it is not a duplicate theorem.

**Results-state connection:** Bears on MPL_33_098-146 N29 as a distinction between two trace constructions and on S19.

**Search record:** `research_context_early_searches.json`, E20; terms: trace, étale, finite, covarian, compact-support.

## E21. The divisor class is constructed through two boundary maps

**File:** cote33. **Scans:** 022,024. **TeX lines:** 022:10–43; 024:3–12. **Kind:** unproved claim.

The section $d\varphi$ is called “canonique,” and the local fundamental class is its image under the Kummer boundary $\partial_n$. The argument uses the invariance of an equation under multiplication by a unit, the support exact sequence, and invertibility of $n$; these ingredients should be checked with their exact hypotheses before generalizing from Cartier divisors. The phrase “dim relative $1$” and the switch between $u$ and $i_*$ remain literal notation questions.

**Context comparison:** same_cote_33/MPL_33_098-146_notes.md, N47, scan123: adds an actual Cartier-equation/cohomology construction, while that reused relative-divisor page depends on missing meromorphic-function definitions; no identical local class formula is supplied.

**Results-state connection:** Adds to README.md/S19; no RESULTS_STATE claim settles this construction or licenses a connection to WG H9.

**Search record:** `research_context_early_searches.json`, E21; terms: Kummer, Cartier, divisor, meromorphic, fundamental.

## E22. Independence of a complete-intersection presentation is left to prove

**File:** cote33. **Scans:** 024. **TeX lines:** 17–38. **Kind:** unproved claim.

“on prouve que cette section ne dépend pas du choix des $Y_i$” is the decisive unexpanded step in passing from products of divisor classes to a global class of a regular immersion. Agreement under localization and admissible base change does not by itself show invariance under replacing one regular sequence by another. A reconstruction must prove that invariance, then use it to justify gluing.

**Context comparison:** same_cote_33/MPL_33_098-146_notes.md, N37, scan146: adds a different descent/compatibility obligation before the later local trace; there is no regular-sequence/fundamental-class independence result in the supplied context.

**Results-state connection:** Bears on MPL_33_098-146 N37 as an additional local-to-global input; no registered proof is reused.

**Search record:** `research_context_early_searches.json`, E22; terms: regular sequence, independence, fundamental, local-to-global, descent.

## E23. The multiplicativity assertion excludes excess intersection

**File:** cote33. **Scans:** 026. **TeX lines:** 6–18. **Kind:** unproved claim.

The formula for the product of local classes is explicitly restricted to $Y.Y'$ “sans dim. excédentaire.” Dropping that phrase would change the claim: excess-intersection corrections are not constructed on these pages. The “propriétés caractéristiques” label also suggests a uniqueness claim whose admissible base changes and intersection hypotheses need a precise formulation.

**Context comparison:** same_cote_33/MPL_33_098-146_notes.md, N47, scan123: adds a no-excess condition to the separate relative-divisor/transversality lead; N34–N37, scans144–146, supply later correspondence language without proving this intersection claim.

**Results-state connection:** Related to MPL_33_098-146 N37; differs from WG H9 rather than proving its codimension-m lattice assertion.

**Search record:** `research_context_early_searches.json`, E23; terms: intersection, transversal, excess, codimension, correspondence.

## E24. Finite-coefficient compatibility is an input to the adic programme

**File:** cote33. **Scans:** 026,034. **TeX lines:** 026:24–28; 034:27. **Kind:** unproved claim.

“Compatibilité pour $n$ variable” is asserted both for the local class and for the geometric trace, and the “bonne” class is placed in $\mathbb Z_\ell(d)$-cohomology. The transition maps and compatibility diagrams are not written out. These are concrete finite-level prerequisites for the adic programme, but they do not by themselves supply derived inverse-limit or finiteness arguments.

**Context comparison:** same_cote_33/MPL_33_098-146_notes.md, N24, scan128, and N40, scans128/132/146: adds geometric class/trace compatibility data to their later expectation and proposed perfect-complex test; it neither restates nor completes the matrix-trace argument.

**Results-state connection:** Bears directly on MPL_33_098-146 N40 and on N23's integral-coefficient objective; these remain first-pass leads.

**Search record:** `research_context_early_searches.json`, E24; terms: coefficient reduction, compatib, adic, limite, finite-level.

## E25. The normal codimension-one case must not be enlarged to full purity

**File:** cote33. **Scans:** 026. **TeX lines:** 33–46. **Kind:** reading question.

The operative assumption is vanishing of $\underline H^i_Y$ for $i<2d$, after which three situations are listed, including “$d=1$, $X$ normal.” The normal codimension-one clause must therefore be read against this low-degree vanishing, not silently promoted to concentration in degree $2d$ with a rank-one purity isomorphism in every singular setting. Scan012's stronger displayed purity statement has smoothness/regularity hypotheses of its own.

**Context comparison:** same_cote_33/MPL_33_098-146_notes.md, N30 and N32, scans136/140/142: adds another instance where the exact degree interval matters; no same normal codimension-one purity assertion is supplied.

**Results-state connection:** Bears on MPL_33_098-146 N30 only through hypothesis and bound discipline; no direct result match.

**Search record:** `research_context_early_searches.json`, E25; terms: purity, normal, vanish, degree, bounds.

## E26. The edge isomorphism supplies a canonical global supported class

**File:** cote33. **Scans:** 028. **TeX lines:** 2–23. **Kind:** unproved claim.

“Alors la suite spectrale implique” turns the low-degree local vanishing into an edge isomorphism in degree $2d$, making the local section a global supported cohomology class. The Kummer NB also records that the resulting class maps to zero in supported $G_m$-cohomology. A proof should identify the local-to-global spectral sequence and the precise support-forgetting maps before using this construction in another support family.

**Context comparison:** same_cote_33/MPL_33_098-146_notes.md, N01, scan098, and N34, scan144: adds a support/degree-edge mechanism to the later derived duality and correspondence leads; neither supplies this exact spectral-sequence argument.

**Results-state connection:** Bears on MPL_33_098-146 N01; no settled register entry already proves this archival step.

**Search record:** `research_context_early_searches.json`, E26; terms: spectral, support, cohomology class, local-to-global, degree-zero.

## E27. Point-class normalization is deferred and then linked to trace

**File:** cote33. **Scans:** 028,030,034. **TeX lines:** 028:25–38; 030:2–8; 034:16–25. **Kind:** unproved claim.

“Il va résulter du théorème qui va suivre” promises that the point class is a basis of top compactly supported cohomology and independent of $x$ for geometrically connected smooth $X$. The curve case is reported as already checked by $t(\gamma_{x/X})=1$, and the subsequent trace statement supplies the promised general framework, but no complete construction of that trace is proved here. Thus the promise is taken up within the package at the level of a theorem statement, rather than simply abandoned or fully demonstrated.

**Context comparison:** same_cote_33/MPL_33_098-146_notes.md, N29, scans134–136, and N37, scan146: adds geometric integration normalized by a point class, distinct from their intrinsic endomorphism trace; N20, scan122, is a later curve application lead.

**Results-state connection:** Bears on MPL_33_098-146 N29, N37 and N20, without identifying the two notions of trace.

**Search record:** `research_context_early_searches.json`, E27; terms: trace, curve, normaliz, point, Kummer.

## E28. The support comparison in Example 2 needs its properness convention

**File:** cote33. **Scans:** 030. **TeX lines:** 11–21. **Kind:** reading question.

“$X$ et $Y$ lisses sur $S$” precedes a map from $Y$-supported cohomology to $R^{2d}_!f_*$, but the passage itself does not restate properness of the support over $S$. The usual inclusion of support families requires that condition, or a different interpretation of the source support family. The preceding discussion on028 assumes $X$ proper in one branch; a reconstruction must decide whether that branch is inherited here rather than supplying the hypothesis to the frozen text.

**Context comparison:** same_cote_33/MPL_33_098-146_notes.md, N18, scan120, N30, scans136/140/142, and N36, scans144–146: adds a concrete support-family scope question alongside their explicit ordinary/compact-support distinctions and cancelled properness wording.

**Results-state connection:** Bears on MPL_33_098-146 N30 and N36; no contradiction with either lead is established.

**Search record:** `research_context_early_searches.json`, E28; terms: support, properness, ordinary, compact, local pairing.

## E29. Locally variable relative dimension is handled piecewise

**File:** cote33. **Scans:** 032. **TeX lines:** 10–20. **Kind:** unpursued implication.

For a smooth morphism of locally variable relative dimension the twist is defined “sur les divers morceaux.” This identifies the geometric pieces on which an orientation object can be formed before a uniform-dimensional trace is stated. In a derived reconstruction the corresponding degree shifts must vary with those pieces too, and a pointwise definition should not be confused with one uniform global amplitude bound.

**Context comparison:** same_cote_33/MPL_33_098-146_notes.md, N31, scans138–140: adds a geometric source of locally varying degrees to that note's distinction between local perfectness and uniform bounds; N41, scans130–146, gives a later formal comparison target.

**Results-state connection:** Bears on MPL_33_098-146 N41; N31 is available in the full same-cote notes but not separately registered.

**Search record:** `research_context_early_searches.json`, E29; terms: uniform, locally, dimension, degrees, perfectness.

## E30. Trace uniqueness is stated through normalization and composition

**File:** cote33. **Scans:** 032,034. **TeX lines:** 032:19–23; 034:2–25. **Kind:** unproved claim.

“Ces conditions caractérisent les hom $\mathrm{Tr}_f$” assigns uniqueness to base change, transitivity, isomorphisms, and the Kummer normalization for $\mathbb P^1$. The existence and uniqueness reductions are not proved on these pages. The geometric trace is the integration map for a smooth compactifiable morphism, and should be kept distinct from the later trace of an endomorphism of a perfect complex.

**Context comparison:** same_cote_33/MPL_33_098-146_notes.md, N27–N29, scans132–136: adds the geometric normalization problem beside the categorical trace construction; N37, scan146, is a later local pairing where the two strands may interact.

**Results-state connection:** Bears on MPL_33_098-146 N29 and N37; differs from WG2 §2.1 #2's graded Lefschetz-operator problem.

**Search record:** `research_context_early_searches.json`, E30; terms: trace, character, transitiv, Kummer, contraction.

## E31. Connected fibres versus geometrically connected fibres

**File:** cote33. **Scans:** 034. **TeX lines:** 24–25. **Kind:** own idea.

If “fibres conn. non vides” means ordinary connectedness, $f:\operatorname{Spec}\mathbb C\to\operatorname{Spec}\mathbb R$ is a smooth proper relative-dimension-zero counterexample to the asserted trace isomorphism. Its fibre over the real point is connected, but after geometric base change the trace is addition $A^2\to A$, which is not an isomorphism for nonzero $A$. This tests the missing convention and supports recovering geometric connectedness, while leaving the words on the page unchanged.

**Confidence and reason:** High for the conditional example: the two geometric points and the summation map are explicit; unresolved whether “fibres conn.” already abbreviates geometric fibres in the intended convention.

**Context comparison:** same_cote_33/MPL_33_098-146_notes.md, N14, scans118–120: adds a geometric-fibre warning to a theorem explicitly placed over a separably closed field there; searches find no same connected-fibre trace test.

**Results-state connection:** Related to MPL_33_098-146 N29's trace vocabulary only; no corresponding settled RESULTS_STATE item.

**Search record:** `research_context_early_searches.json`, E31; terms: connected, geometric, trace, separably closed.

## E32. A finite-level test linking local classes to geometric integration

**File:** cote33. **Scans:** 026,028,034,036. **TeX lines:** 026:24–28; 028:30–35; 034:27; 036:40. **Kind:** own idea.

A useful next check is to choose the point-class normalizations simultaneously for $n=\ell^r$ and verify that coefficient reduction commutes with both the local Kummer boundary and the geometric trace. If the resulting squares commute, the identity sending each point class to $1$ becomes compatible across the coefficient tower. This supplies geometric input to, rather than repeats, the context's separate perfect-complex supertrace compatibility test.

**Confidence and reason:** Medium: the finite-level normalization is visible, but the compatibility squares and geometric inverse-limit construction have not been proved in this memo.

**Context comparison:** same_cote_33/MPL_33_098-146_notes.md, N40, scans128/132/146: adds a cycle-class/integration test to its matrix-trace proposal; N24, scan128, explains why a full inverse-limit argument still remains.

**Results-state connection:** Bears directly on MPL_33_098-146 N40; does not upgrade its first-pass proposal to an established result.

**Search record:** `research_context_early_searches.json`, E32; terms: coefficient, matrix trace, finite-level, compatible, passage.

## E33. Purity and trace compatibility calls for derived categories

**File:** cote33. **Scans:** 036. **TeX lines:** 19–45. **Kind:** unproved claim.

“Compatibilité avec les hom traces” is followed by “S’exprime plus aisément quand on dispose de la catégorie dérivée.” This is a claim that the patched degreewise purity/trace diagram has a more complete derived formulation, not that the displayed typing and all coherence conditions have already been verified. The intended reconstruction should recover a shifted purity isomorphism and its compatibility with integration before matching the degreewise arrows.

**Context comparison:** same_cote_33/MPL_33_098-146_notes.md, N01, scan098, N29, scans134–136, and N37, scan146: adds an explicit local-to-global geometric bridge to the later exchange, contraction, and local trace leads.

**Results-state connection:** Bears directly on MPL_33_098-146 N01, N29 and N37; adds a new S19 comparison locus.

**Search record:** `research_context_early_searches.json`, E33; terms: duality, purity, trace, compatib, derived.

## E34. Cancelled purity formulas are an expositional withdrawal

**File:** cote33. **Scans:** 036. **TeX lines:** 10–17,19–40. **Kind:** withdrawn in the same text.

The initial $T$-tensor/purity identities and an unfinished direct-image line are cancelled before a revised vanishing/isomorphism display and support diagram. The page therefore withdraws that written presentation and restarts it, but supplies no prose retracting the underlying purity compatibility. The overwritten exponents and map letters must remain a reading problem rather than be resolved by the later context.

**Context comparison:** same_cote_33/MPL_33_098-146_notes.md, N36, scans144–146: restates a later pattern of cancelled local-pairing exposition followed by a restart, but concerns different formulas and cannot repair these glyphs.

**Results-state connection:** Bears on MPL_33_098-146 N36 as a comparable documentary state; no theorem is declared refuted.

**Search record:** `research_context_early_searches.json`, E34; terms: cancelled, restarts, local pairing, overwritten, N36.

## E35. The compact-support heading is moved after constructibility

**File:** cote33. **Scans:** 014,016,018. **TeX lines:** 014:39–48; 016:3–6; 018:13–28. **Kind:** withdrawn in the same text.

The cancelled “13) Les $R^i_!f_*(F)$” and its compactification definition continue onto016 before a new section13 on constructible sheaves; the compact-support construction reappears as section14 on018. This documents a reordered exposition and a numbering revision, not a mathematical retraction of compactifiability. Both endpoints should be retained in a study of how the draft was organized.

**Context comparison:** same_cote_33/MPL_33_098-146_notes.md, T03, scans100/108/122, and T04, scan124: adds an earlier heading-revision instance to the later numbered Formulaire and Künneth-to-Lefschetz changes; no same heading sequence is supplied.

**Results-state connection:** Adds to the standing title/numbering question and MPL_33_098-146 §65; no result entry is affected.

**Search record:** `research_context_early_searches.json`, E35; terms: heading, number, Künneth, Formulaire, cancelled.

## E36. The global class reverses the displayed index order

**File:** cote33. **Scans:** 024,028. **TeX lines:** 024:10–12; 028:12,22. **Kind:** reading question.

The global class on028 has the literal subscript $X/Y$, whereas the local definition on024 and the same-page Kummer NB on028 use $Y/X$. The context provides no parallel class formula that decides whether this is an intentional convention or a slip. The discrepancy therefore belongs in the research apparatus and cannot be normalized after the freeze.

**Context comparison:** same_cote_33/MPL_33_098-146_notes.md, N33, scans138–142, and N39, scan146: adds another source-level notation/type discrepancy, while neither lead supplies the missing local-class comparison.

**Results-state connection:** Related to MPL_33_098-146 §76 as a collation task; no mathematical status is changed.

**Search record:** `research_context_early_searches.json`, E36; terms: fundamental, subscript, notation, literal, mismatched.

## Standing-question index: explicit doubts, expectations, conditions and deferrals

This index is exhaustive for the explicit self-flagged wording found in the assigned handwritten scans002–036, with routine claimed results and ordinary hypotheses separated from authorial uncertainty. An `\unsure` macro records the reader's doubt and is never, by itself, an authorial question.

| Scan(s) | Exact short words in the frozen text | Classification | Disposition / item |
|---|---|---|---|
|006|“Utilise en plus” followed by uncertain resolution/projectivity wording|Explicit proof dependency; small wording uncertain|No full proof; E05; do not treat every doubtful word as Grothendieck's doubt.|
|008|“À prouver que ce sont des isomorphismes”|Explicitly unverified comparison|Both maps are to be proved; E07.|
|008|“Devrait aussi se généraliser au contexte rigide analytique”|Expectation / conjecture|No rigid theorem or precise hypotheses supplied; E08.|
|008|“Passant à la limite … on trouverait alors”|Conditional consequence / deferred verification|Depends on comparison and continuity; E09.|
|012 →022–024|“Donner définition de la classe fondamentale locale”|Deferred expository task|Definition is taken up; presentation-independence remains asserted; E13/E22.|
|014|“Dém presque immédiate par th. du changement de base”|Compressed proof claim|Not an explicit uncertainty, but proof omitted; E14.|
|014|“Pb sans hypothèse de lissité remplacée par hyp. de régularité”|Explicit problem|Conditional characteristic-zero/resolution route follows; E15.|
|014|“O.K.” … “quand on dispose de la résolution des singularités (Artin)”|Claim with a stated methodological condition|Not a proof of general absolute purity; E15.|
|014|“Il y a aussi un th de pureté relatif sur une base quelconque”|Unproved existence claim|No precise relative theorem or proof here; include with E15 if a separate item is not preferred.|
|014|“Extension aux div. à croisements normaux”|Unworked extension programme|The target assertion is unspecified; E16.|
|016→018|“Question de la généralisation” … “Se résoud par l'affirmative lorsqu'on dispose de … $+$ pureté”|Explicit question with conditional claimed route|Coefficient scope is essential; E17/E18.|
|018→020|“de façon quasi-triviale du th. du changement de base”|Compressed proof claim|Independence and comparison coherence not written out; E19.|
|024|“on prouve que cette section ne dépend pas du choix des $Y_i$”|Unproved presentation-independence claim|E22.|
|026|“propriétés caractéristiques”; “Compatibilité pour $n$ variable”|Unproved characterization/compatibility|E23/E24.|
|026|“Supposons … $i<2d$”|Explicit mathematical hypothesis, not uncertainty|Preserve its scope; E25.|
|028→030,034|“Il va résulter du théorème qui va suivre”|Promise of a later theorem|Taken up by curve normalization and general trace statement; full trace proof absent; E27.|
|028→030|“C'est qu'on avait vérifié directement dans le cas où $d=1$”|Report of an earlier verification|Its value $1$ is recorded, not the full proof; E27.|
|032→034|“on peut définir un … hom. canonique”|Construction asserted|Trace existence not proved here; E30.|
|034|“Ces conditions caractérisent les hom $\mathrm{Tr}_f$”|Unproved uniqueness claim|E30.|
|034|“Compatibilité pour $n$ variable”|Unproved compatibility|E24/E32.|
|036|“Compatibilité avec les hom traces ....”|Unworked compatibility statement|E33.|
|036|“S'exprime plus aisément quand on dispose de la catégorie dérivée, et s'énonce sous forme plus complète”|Explicit deferred reformulation|Derived categories are announced next; E33.|

No literal “à vérifier”, “sauf erreur”, “je présume”, “admis”, or standalone authorial question mark appears in the frozen assigned even-page text; the actual explicit flags are the words listed above. The strong numerical and sign doubts in the transcription remain paleographic questions, not authorial admissions of doubt.

## Negative results-register connections

| Entry | Effect of this assigned sequence |
|---|---|
|LM7 E.23|No section-map image/fibre calculation for metabelian or marked depth-two arithmetic quotients is present; the field/Galois example on002 does not advance this open item.|
|LM4 D.12|No full profinite GT torsion/conjugacy result appears; no status change.|
|LM4 F.7|No nonsolvable completion-centralizer comparison or geometric A5 action appears; no status change.|
|LM7_PUSH C.6|No class-two germ/residue classification is attempted or re-derived.|
|INTAKE LM7_CONTINUED §?|No evidence concerning the stated section-map/integrality intake; not promoted to a referee verdict.|
|WG H9|The manuscript's trace/Künneth/Lefschetz programme is different from the proposed Hodge-index/Mordell–Weil lattice formula; no implication established.|
|WG2 §2.1 #2|Tate twists and geometric integration are not identified with the register's graded-ring Lefschetz operators.|
|MPL_142_001-093 §316; MPL_91_099-143 §68|Methodological/bibliographic or planning exemplars only; their full underlying files are not supplied, and they cannot furnish parallel scans for current claims.|
|MPL_14_002-044 §107|Its truncated correspondence/Lefschetz excerpt suggests a thematic comparison but provides no exact theorem or scan here; do not claim a precise confirmation.|

## Priority issues for the parent research synthesis

1. Keep proper torsion-general results separate from nonproper prime-to-characteristic extensions (E04/E17/E18).
2. State the analytic constructibility convention before treating the GAGA margin as an equivalence (E06).
3. Preserve the weak low-degree vanishing in the normal codimension-one case (E25).
4. Recover properness of support for the source-to-compact-support comparison on030 (E28).
5. Recover geometric connectedness for the trace-isomorphism statement (E31).
6. Distinguish integration trace from categorical endomorphism trace while connecting their roles (E27/E30/E33).
7. Do not infer chronology from scan order, nor treat cancelled presentations as rejected theorems (E01/E05/E34/E35).
