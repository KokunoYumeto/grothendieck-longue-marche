# Root research notes prepared after the transcription freeze

These items will be incorporated into the final notes with the specialist research checks. Context references below mean the attached `context/hua_project/29.modern.tex` (Michel Hua's project, an AI-produced modernised interpretation), not a source for changing the transcription.

## Orientation and scope

### N-ORI-01 — What this retained range actually contains

**Witness:** cote 29, scans 049–094, with 079–081 and 083 absent by the task's stated selection. **Kind:** unpursued implication / source structure. **Words:** “π₁ et Pic^τ birationnels” (060); “Revêtements formels étales et th. de Mumford” (078). **Context:** `README.md`, package238/rank24; Hua, “Le fil du dossier, et l'ordre des feuillets,” and the two corresponding titled sections (modern pp59–76 and77–85; our060–077 and078–086). **RESULTS_STATE:** package238 orientation; LM1 E.11 and E.2 considered, with no direct resolution.

The retained material is chiefly a finiteness/birational-invariant sequence and a formal tame-covering sequence, interleaved with reused distribution, Raynaud and diagonalizable-group typescripts. It confirms the broad fundamental-group and SGA setting of the planning note, while supplying no letter, named recipient or explicit date of writing in these retained images. The date30April1969 and Murre's accompanying letter belong to the context's account of omitted scans079–081, so they are a contextual association rather than an independently read date for the present sheets.

### N-ORI-02 — Limits of the results-state matches

**Witness:** 085, 089, 091, 093. **Kind:** unpursued implication. **Words:** “groupe de Raynaud”; “Un groupe diagonalisable est réflexif”. **Context:** `notes/RESULTS_STATE.md`, matching group-scheme rows; Hua, “Deux feuillets de son propre tapuscrit : l'extension de Raynaud” (modern84/our085), with no dedicated subsection found for the interleaved diagonalizable typescript. **RESULTS_STATE:** LM1 E.11 [Open, return's claim], LM1 E.2 [Proved, return's claim]; MPL_11_043-058+56 N063 and N100 [first-pass leads].

The diagonalizable and Raynaud sheets provide concrete special classes of group schemes, but they do not establish the arbitrary separated locally finitely presented group-scheme source theorem requested in LM1E.11 or the characteristic-zero unipotent exponential statement LM1E.2. The two cote56 notes concern other rank/descent and Weyl-subquotient questions, and no implication from the present pages to them has been verified. Those statuses are reported as the supplied register's claims, without promoting them to reviewed results or re-proving them here.

## Finiteness, constructibility, and the distinction from finite generation

### N-FIN-01 — The continuation of the descent lemma is not a standalone theorem

**Witness:** 050, concluding paragraph and NB. **Kind:** unproved claim. **Words:** “généralise … SGA IX 6.1, 6.2”; “fibre … générique”. **Context:** Hua, “Lemme1 : un isomorphisme générique géométrique descend,” modern47,49/our048,050; the opening sheet048 is outside this package. **RESULTS_STATE:** no directly matching theorem; package238 orientation only.

The page concludes a descent argument and writes a homotopy sequence, but its initial hypotheses are on an unavailable preceding sheet and its own corrections remain among the least legible in the package. Hua's modern statement should therefore be treated as a reconstruction to check against the missing beginning, not as a theorem certified by scan050 alone. The frozen reading of the final comparison is “pas” plus a doubtful interlinear “néc|ici” before “générique,” whereas Hua writes a contrast with a “vraie” generic fibre; this difference belongs in a reading question, not a silent repair.

### N-FIN-02 — Degree-zero constructibility needs its own reference

**Witness:** 052, Lemme2. **Kind:** unproved claim. **Words:** “Y loc. noeth. et univ. japonais”; “f_*(F) est constructible”. **Context:** Hua, “Lemme2 : constructibilité de f_*,” modern51/our052. **RESULTS_STATE:** no matching result.

The manuscript states a degree-zero theorem for constructible sheaves of sets under a universally Japanese hypothesis and gives a short, uncertain reference cue. Hua's comparison with a finiteness theorem for the whole derived direct image under excellence is useful background but does not by itself show a gap in this weaker degree-zero assertion. A source check should isolate precisely f_* on finite constructible sets, including the nonproper case, before either strengthening the hypothesis or treating the lemma as proved.

### N-FIN-03 — The partition lemma preserves an inserted base hypothesis

**Witness:** 052, Lemme3. **Kind:** withdrawn in the same text / unproved claim. **Words:** “univ. japonais” inserted; “Cette application est à fibres finies”. **Context:** Hua, “Lemme3 : H¹ le long d'une partition,” modern51/our052. **RESULTS_STATE:** no matching result.

The live claim is the finite-fibre assertion for restriction along a finite locally closed partition, and the earlier hypothesis that every stratum already has finite H¹ is deleted and retained only as a consequence. Unlike Hua's modern statement, the scan inserts “univ. japonais” into the assumptions, so the hypothesis should not disappear when assessing the stated proof by recollement and Lemme2. What is left to check is the gluing classification of torsors for an open/closed decomposition, then induction on the partition; the present run does not certify that entire historical argument.

### N-FIN-04 — A short check of the finite Hom lemma

**Witness:** 052, inserted Lemme4. **Kind:** own idea / independent re-proof of a stated claim. **Words:** “Hom(F,G) est un ens fini”. **Context:** Hua, same partition subsection, modern51/our052, which repeats the claim without expanding the check. **RESULTS_STATE:** no matching result. **Confidence:** high; a finite stalkwise bound gives the result directly.

For constructible sheaves of finite sets F and G on a noetherian scheme, take a common finite stratification on which both are finite locally constant, then split its strata into their finitely many connected components. A morphism is determined on each such component by its map on one geometric stalk, and equality of all those stalk maps detects equality globally, giving an injection of Hom(F,G) into a finite product of finite sets. This verifies the finite Hom input itself, not the additional pushforward and recollement steps of Lemme3; the stratification convention is the one in [Stacks, Tag05BE](https://stacks.math.columbia.edu/tag/05BE).

### N-FIN-05 — The quantifiers in the main proposition matter

**Witness:** 054, (ii)–(iv); 056, Cor1–2. **Kind:** reading question / unproved claim. **Words:** “rev. fini étale”; “un ouvert non vide U de S′”; “H de G×G”. **Context:** Hua, “La proposition principale” and “Les deux corollaires,” modern53,55/our054,056. **RESULTS_STATE:** no matching result.

The frozen page reads finite étale S′ over an integral normal affine stratum, and the open U in (iii) lies in S′, whereas Hua's compressed version substitutes an open dense S′ and then an open of X. Likewise, the commutative simplification on054 says “Lorsque G est commutatif,” while Hua's enumeration says H; these distinctions change the proposed reduction and should be checked against the original quantifiers. The G×G subgroup hypothesis is naturally relevant to comparing two G-torsors, but that explanation does not authorize changing any of the doubtful qualifiers in the page.

### N-FIN-06 — Finite H¹ for each finite target is not finite generation

**Witness:** 052–058, H¹ finiteness statements, contrasted with061. **Kind:** own idea / correction of context inference. **Words:** “H¹(X,G) est fini”; “de degré donné est fini”. **Context:** Hua, “Le pont entre H¹ et π₁,” modern46–57/our047–058, explicitly asserts an if-and-only-if with topological finite generation. **RESULTS_STATE:** no matching result. **Confidence:** high; the counterexample and both relevant bounds are elementary.

Let P=∏_ℓ(F_ℓ)^{d_ℓ}, over distinct primes with every d_ℓ finite but unbounded: each continuous homomorphism P→G to a fixed finite group kills all factors whose prime does not divide |G|, so there are only finitely many such maps and conjugacy classes. Yet P cannot have d topological generators for any fixed d, because its quotient (F_ℓ)^{d_ℓ} requires d_ℓ generators. Thus the general profinite condition extracted from all these finite torsor counts is smallness, not finite generation; this refutes Hua's stated abstract converse and leaves the separate geometric finite-generation argument of061 to do genuine work (compare the definition of smallness in [Helbig, §1](https://arxiv.org/html/1511.08760v2)).

### N-FIN-07 — A concrete reason for the prime-to-characteristic restriction

**Witness:** 056 NB, 058 question, 061 theorem. **Kind:** own idea / boundary test. **Words:** “G premier à la car. de k”; “pour tt … courbe … de degré donné”. **Context:** Hua, “La récurrence sur la dimension” and “La première page,” modern57,60/our058,061. **RESULTS_STATE:** no matching result. **Confidence:** high; the Artin–Schreier calculation is explicit.

Over an algebraically closed field of characteristic p, the equations y^p−y=x^m for positive m prime to p give infinitely many classes in H¹(A¹,F_p): any nonzero F_p-linear combination of those monomials has highest degree prime to p, whereas h^p−h has degree divisible by p when h is nonconstant. The derivative with respect to y is −1, so these are finite étale torsors; the cohomological identification follows from the Artin–Schreier sequence and affine vanishing in [Stacks, Tag0A3J](https://stacks.math.columbia.edu/tag/0A3J). This does not refute the conditional proposition beside the question mark on058, but shows why its premise cannot simply be dropped in positive characteristic.

### N-FIN-08 — The dimension induction leaves a geometric construction to supply

**Witness:** 058, upper proof. **Kind:** unproved claim. **Words:** “une fibration lisse X→Y”; “fibres géom. connexes non vides, de dim1”. **Context:** Hua, “La récurrence sur la dimension,” modern57/our058. **RESULTS_STATE:** no matching result.

The reduction requires finding a suitable smooth relative curve after removing and stratifying closed subsets, then transporting the torsor comparison through Lemme1. Hua's version only says dimY<dimX, whereas the retained page supplies the stronger one-dimensional fibre condition and its geometric connectedness. A complete proof must explain that construction, its compatibility with the finite partition, and the relevant base-field assumptions; none is supplied merely by citing induction on dimension.

## Murre's exposition, descent, and the cancelled stratification sheet

### N-ED-01 — The wish for a champ has a later contextual counterpart

**Witness:** 082, item25. **Kind:** conjecture / unpursued implication. **Words:** “fppf descent for tamely ramified coverings?”; “a ‘champ’ on Et/S”. **Context:** Hua, “Notes de lecture, et l'appel d'un champ,” modern81/our082; “Domaines de ramification : les axiomes R1 à R4,” modern190–191/our191–192; “La2-catégorie Domram(S), et le recollement,” modern197–198/our198–199. **RESULTS_STATE:** package238 orientation and Hua finding29-formal-tame-pi1-self-intersection, indirectly; no matching settled theorem.

The page separately asks for fppf descent and, at least, an étale champ, so proving only the latter would not discharge the former. Hua's project links this wish to the later domain-of-ramification construction in the same cote, and the context makes that a useful comparison to pursue. Those later scans were not supplied here, and neither their chronology nor full effectiveness theorem is certified by the present run.

### N-ED-02 — Equations for divisors lead to a concrete gluing problem

**Witness:** 082, item16; 090 and094. **Kind:** own idea. **Words:** “case when D.'s have equations”; “This should make the situation much clearer!” **Context:** Hua, “Le cas kummérien,” modern19–20/our020–021, and “Exemple2 : des diviseurs, et la gerbe,” modern199–200/our200–201. **RESULTS_STATE:** Hua finding29-formal-tame-pi1-self-intersection. **Confidence:** medium; the relation is structurally clear, but a comparison of full covering categories remains to be proved.

Use local equations for each Cartier divisor to build finite Kummer covers, then track the units relating those equations on overlaps and the resulting root data on triple overlaps. This is a concrete route from the editorial request to the Chern-class obstruction in090/094 and to Hua's reported later gerbe construction. A gerbe of roots of the line bundle and a root stack of the line bundle with its section are different objects, so their inertia and covering categories should be compared explicitly before adopting the modern root-stack interpretation wholesale.

### N-ED-03 — The requested tame Lefschetz variant has a precise literature comparison

**Witness:** 082, boxed request. **Kind:** unpursued implication. **Words:** “Include variant of Lefschetz's Theorem for π₁ᵗ”. **Context:** Hua, “Notes de lecture, et l'appel d'un champ,” modern81/our082; “Théorème de Bertini et variantes,” modern112–115/our113–116. **RESULTS_STATE:** no matching result; package238 orientation only.

Esnault–Kindler give a directly relevant later formulation: for a regular projective X, a strict normal-crossings divisor D and an ample regular hyperplane Y transverse to D, restriction of tame coverings is an equivalence for dimX≥3 and fully faithful for dimX=2 ([arXiv:1509.08160](https://arxiv.org/abs/1509.08160), theorem stated in the abstract). This supplies a precise target for comparing the requested variant and the later context, with hypotheses and direction of the categorical conclusion fixed. The published result has been read as a source statement here, not independently re-proved, and no claim of novelty or direct historical dependence is made beyond the paper's own attribution to Grothendieck–Murre.

### N-ED-04 — A significant correction from tame to prime-to-p

**Witness:** 082, boxed application after Mumford's theorem. **Kind:** withdrawn in the same text. **Words:** deleted “tame”, inserted “prime to p”. **Context:** Hua, “Notes de lecture, et l'appel d'un champ,” modern81/our082, and “Invariance birationnelle, et le groupe fondamental local,” modern42/our043. **RESULTS_STATE:** package238 orientation; no matching result.

The requested local finite-generation application is explicitly narrowed from tame to prime-to-p in the scan. That is a mathematical revision of the requested scope, not interchangeable terminology, and it should remain attached to any comparison with the local-group discussion in the context. The publication's contents list a local complete-ring application, but its existence alone does not identify which draft hypotheses were ultimately retained ([Grothendieck–Murre, LNM208](https://link.springer.com/book/10.1007/BFb0069608), contents).

### N-ED-05 — Specialization paths require a definition and a chosen lift

**Witness:** 084, VIII.3. **Kind:** unproved claim / unpursued implication. **Words:** “the ‘paths’ of y-bar to x-bar correspond exactly to … liftings”. **Context:** Hua, “Notes de lecture, et l'appel d'un champ,” modern83/our084; the precise rewritten path paragraph is not developed there. **RESULTS_STATE:** no matching result.

The direction and the lift to the strict localization should be compared with a geometric specialization, which induces a natural transformation from the special stalk functor to the general stalk functor ([Stacks, Tag0GJ2](https://stacks.math.columbia.edu/tag/0GJ2)). The word “paths” must be fixed at that level before claiming the same bijection for all isomorphisms between finite-étale fibre functors; the latter forgets information about arbitrary étale sheaves. The displayed product of fields also needs its indexing and hypotheses checked in the proposed generality “S any scheme,” rather than assuming a finite product without justification.

### N-ED-06 — The guessed equivalence remains a named verification task

**Witness:** 084, VII.2 and margin. **Kind:** self-flagged: a step he himself marks as unverified. **Words:** “I guess that one has equivalence of categories anyhow!!”; “to check!”. **Context:** Hua, “Notes de lecture, et l'appel d'un champ,” modern83/our084; preceding formal quotient discussion modern43,45/our044,046. **RESULTS_STATE:** package238 orientation; no matching result.

The claim should be indexed as an equivalence to verify, not as an established comparison theorem. To make it testable, recover the two categories and the functor of Murre's chapterVII, then separate full faithfulness, algebraization of objects, and preservation of tameness. The present sheet supplies a strong expectation but not those definitions or a proof.

### N-ED-07 — The gluing assertion depends on omitted ambient hypotheses

**Witness:** 086, items1 and12. **Kind:** unproved claim. **Words:** “finite presentation … or loc. free”; “Should be trivial with the conditions considered!”. **Context:** Hua, same notes-of-reading section, modern85/our086. **RESULTS_STATE:** no matching result.

The first item asks that the quasi-coherent gluing theorem preserve finite type, finite presentation and local freeness, and the last reduces the tame-covering assertion to its restrictions to S₁,S₂. The ambient gluing square and the precise class of finite flat covers are not stated on this sheet, so ordinary descent for modules alone does not certify the ramification assertion. A useful next check is to write the gluing equivalence for finite algebras, verify local freeness, and only then test the boundary valuations or Kummer charts defining tameness.

### N-ED-08 — Unramified is not a unique deformation rule

**Witness:** 087, cancelled draft and dashed n.r. arrow. **Kind:** own idea / boundary test. **Words:** “Il faut vérifier”; “voisinages infinitésimaux de tous ordres”. **Context:** Hua, “Images inverses et voisinages infinitésimaux,” modern86/our087, including its warning about non-uniqueness. **RESULTS_STATE:** no matching result. **Confidence:** high; the two lifts are explicit affine schemes.

For T₀=Spec k inside T=Spec k[ε]/(ε²), both the closed immersion T₀→T and the identity T→T are unramified and restrict to the same identity T₀→T₀, but they are distinct lifts. Thus a dashed arrow labelled n.r. does not by itself specify a unique lifted scheme; extra data, flatness or an étale replacement must enter the argument. This supports Hua's caution, rather than contradicting the cancelled draft, and uses only the elementary fact that closed immersions and identities are unramified ([Stacks, Tag02G3](https://stacks.math.columbia.edu/tag/02G3)). The issue is lifting objects, not uniqueness of a map into one fixed formally unramified target.

## Reused typescripts and source identification

### N-TYP-01 — The distribution sheets are a separate, partly reversed text

**Witness:** 049, 051, 053, 055, 057, 059. **Kind:** unpursued implication / source structure. **Words:** “n°385”; “Distributions et vecteurs tangents”; “Produit cartésien de deux distributions”. **Context:** full-file searches of Hua's modernised cote29 for distribution/tangent/produit cartésien found no dedicated treatment of these interleaved sheets; the nearest section is the surrounding relative-finiteness text, modern46–57/our047–058. **RESULTS_STATE:** package238 orientation; no matching result.

Their printed page sequence is23,22,13,12,11,10 in scan order, which makes the continuations51→49 and59→57→55→53 visible without rearranging the diplomatic transcription. They develop multiplication of a distribution by a function, the coproduct, tangent vectors and external products, and should not be read as steps of the adjacent étale-finiteness proof. The unresolved differentiability-class symbol and the isolated source number385 prevent a secure author/title identification here; any bibliographic identification remains a separate task.

### N-TYP-02 — A finite-jet algebra explains the visible coproduct formulas

**Witness:** 049, 051, 053, 055, 057, 059, numbered formulas and propositions. **Kind:** own idea / unpursued implication. **Words:** “Pφ_*(μ)”; “Produit d'une fonction et d'une distribution”. **Context:** no exact distribution subsection found in Hua's modernised cote29; nearest group-duality material is its much later infinitesimal-group discussion, modern124–129/our125–130, which is only an analogy. **RESULTS_STATE:** LM1 E.2 only by broad group-scheme subject, with no proved implication. **Confidence:** medium; the finite-order algebra model is clear, but the manuscript's differentiability class remains unresolved.

For a finite local jet algebra A/m^{r+1}, multiplication dualizes to a coalgebra structure on its dual and makes multiplication by functions compatible with pushforward, matching the shape of the formulas on051. The tangent subspace is read from the dual of m/m², and coordinate multiindices explain the bases on049 and053. This is an interpretive model to compare with the text's class-C^r conventions, not a justification for replacing its doubtful class symbol or supplying the source's missing reference on053.

### N-TYP-03 — The Raynaud sheet changes the named object in place

**Witness:** 085, top insertion and (7.2.2)–(7.2.5). **Kind:** withdrawn in the same text / unproved claim. **Words:** “groupe de Raynaud”; deleted “extension canonique du”; “T₀ isotrivial”. **Context:** Hua, “Deux feuillets de son propre tapuscrit : l'extension de Raynaud,” modern84/our085; its companion modern82/our083 is omitted from this package. **RESULTS_STATE:** LM1 E.11, narrower special class only.

The handwritten revision moves the naming from the extension to a group scheme and adds isotriviality of T₀, while retaining the extension by a torus and the formal-completion characterization. The whole sheet is crossed diagonally, but that reuse mark is not enough to call the existence or base-change theorem mathematically retracted. Hua supplies a coherent modern statement, whereas the diplomatic text retains a disrupted splice and the uncertain natural/sharp superscript; those are reading issues to keep distinct from the theorem's validity.

### N-TYP-04 — The diagonalizable sheets have an identifiable published counterpart

**Witness:** 089, 091, 093. **Kind:** unpursued implication / source identification. **Words:** “Définition1.1”; “Corollaire1.4”; “Propriétés d'exactitude du foncteur D_S”. **Context:** no dedicated treatment found in Hua's modernised cote29; its live formal-inertia section modern87–93/our088–094 omits these interleaved typescript arguments. **RESULTS_STATE:** LM1 E.11 and E.2, no direct resolution.

The sequence of biduality, diagonalizable representability and exactness matches SGA3, ExposéVIII, §§1–3, providing a precise bibliographic target for these reused sheets ([Grothendieck, ExposéVIII, re-edition](https://www.wstein.org/sga/SGA3/Exp8-8nov09.pdf)). This match was made only after the freeze, so the printed edition's arrows, parentheses and operators have not been imported into the visibly blank positions of089,091 or093. The match identifies a textual counterpart, not the physical date or production stage of these particular copies.

### N-TYP-05 — Finite flat length and geometric point count separate at p

**Witness:** 093, first paragraph. **Kind:** own idea / independent check. **Words:** “n_i est premier à la caractéristique p”; “card D(T)(k)=n”. **Context:** no exact counterpart in Hua's modernised cote29; link to its roots-of-unity inertia discussion modern87/our088. **RESULTS_STATE:** Hua finding29-formal-tame-pi1-self-intersection, coefficient distinction; no LM1 theorem settled. **Confidence:** high; the coordinate ring and roots are explicit.

For T=Z/p over an algebraically closed field of characteristic p, D(T)=μ_p has coordinate algebra k[t]/(t^p−1)=k[t]/((t−1)^p), hence length p but one geometric point. For an integer n prime to p, t^n−1 has n distinct roots, and products give the criterion recorded in the typescript. This independent check explains why the live formal discussion uses invertible orders; it does not turn the missing μ and product glyphs on the copy into written ink.

### N-TYP-06 — Exact duality can be checked on the group algebra

**Witness:** 093, Th3.1. **Kind:** own idea / independent re-proof of the affine part. **Words:** “u′ est fidèlement plat et quasi-compact”. **Context:** no exact diagonalizable subsection found in Hua's modernised cote29; SGA3VIII§3 is the published counterpart, identified after freeze. **RESULTS_STATE:** LM1 E.11, special diagonalizable case only. **Confidence:** high; the module decomposition is explicit.

For an injection of abelian groups M′⊂M, choose representatives of M/M′; the group algebra O_S[M] is a direct sum of copies of O_S[M′] indexed by those representatives. It is consequently faithfully flat over O_S[M′], and the corresponding map of affine diagonalizable groups is quasi-compact; the kernel identification follows by applying Hom(−,R*) to the quotient M/M′. This checks the exactness mechanism on the sheet and does not extend it to arbitrary group schemes in LM1E.11.

## Context-only reading questions that leave the frozen text unchanged

### N-RQ-01 — “More natural” versus “unnatural”

**Witness:** 082, item26. **Kind:** reading question. **Frozen words:** “Normality assumption more natural”. **Context:** Hua, “Notes de lecture, et l'appel d'un champ,” modern81/our082, writes “Normality-assumption unnatural”. **RESULTS_STATE:** package238 orientation.

These readings have opposite force and deserve a fresh expert comparison with the scan. The present transcription retains its pre-context reading, and the research notes do not use that sentence to establish either approval or rejection of the normality hypothesis.

### N-RQ-02 — The proposed local point description is reversed in the commentary

**Witness:** 084, IV. **Kind:** reading question. **Frozen words:** “take point of Spec(O_{S,s})!”; “Introduce geometric points of S”. **Context:** Hua, same notes-of-reading section, modern83/our084, says to introduce geometric points rather than reason on that spectrum. **RESULTS_STATE:** package238 orientation.

The two instructions on the scan should be read together, but the context's “rather than” supplies a contrast not present in the frozen wording. This is a question about the intended relation between local-scheme points and formal geometric points, not permission to alter the transcription.

### N-RQ-03 — A faint marginal fragment is not a secure retraction

**Witness:** 092, lower-left margin. **Kind:** reading question. **Frozen words:** individually doubtful “ce qui du / pro. dans / est faux”. **Context:** Hua, “Le cas où la classe s'annule : Picard formel,” modern91/our092, says much of the prose is unreadable and supplies no secure referent for this fragment. **RESULTS_STATE:** Hua finding29-formal-tame-pi1-self-intersection.

Both the words and their referent are too uncertain to classify the surrounding realization argument as withdrawn. The mathematical qualifications in FORMAL-01–17 therefore rest on explicit calculations and stated hypotheses, not on this tentative marginal reading.
