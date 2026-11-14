#!/usr/bin/env python3
"""Record manuscript alternatives independently of the theorem-source audit."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]
rows = []

def add(package, cote, scan, folio, place, reading, alternatives, support, strength, ids):
    rows.append({
        "id": f"BC-editorial-{len(rows)+1:02d}",
        "package": package, "cote": cote, "scan": scan, "folio": folio,
        "place": place, "reading": reading, "alternatives": alternatives,
        "support": support, "strength": strength,
        "statement_ids": ids, "provisional": True,
        "fresh_scan_inspection": False,
        "method": "Compared the supplied transcription and its supplied doubt/checked-note register. No fresh palaeographic resolution is claimed."
    })

add("LM_P041", "140-2", [408], "206 continuation", "Before equation (24), admissibility reservation",
    "sous réserve d'admissibilité; the proposed fixed-group definition is cancelled",
    ["Read the following claim with the stated admissibility reservation", "Enlarge it to all arbitrary arithmetic moduli sections"],
    "The checked text expressly reserves admissibility and says that no formed definition is yet available. B.28 proves geometric injectivity and gives an actual collision for the enlarged assertion; it does not remove the reservation from Grothendieck's statement.",
    "Strong mathematical support for retaining the explicit scope; reading remains inherited from the checked transcription", ["B.13","B.28"])
add("LM_P041", "140-2", [409], "207", "Equations (24) and (25), domain and groupoid objects",
    "I' is nonempty and consists of Gamma-fixed objects of a genuine groupoid; I' -> Pts(pi',alpha',Gamma)",
    ["A set fixed pointwise by Gamma", "A merely Gamma-stable finite set, treated later on scan 420"],
    "The source first imposes trivial action on each i'. This supplies the canonical effective lift at that object. The stable-but-not-pointwise-fixed case is exactly the separate descent question of scan 420. B.13 handles its unordered kernel without suppressing the permutation quotient.",
    "Strong typing evidence; not a new scan reading", ["B.13","B.28"])
add("LM_P041", "140-2", [410], "207 continuation", "Rational-point field in explanation of injectivity",
    r"vrais pts rat / \unsure{K^+|K}, corps des \unsure{fixes|invariants} de Gamma",
    ["K^+", "K", "fixes", "invariants"],
    "B.1 proves injection over the actual fixed field when it belongs to the stated finitely generated arithmetic class. Either displayed symbol must be assigned that field before applying the theorem. The proof does not decide the raised mark.",
    "Mathematical content fixed after specifying the field; palaeographic alternative unresolved", ["B.1","B.28"])
add("LM_P041", "140-2", [410], "207 continuation", "Final qualification and margin",
    r"deux définitions \unsure{éventuelles|essentielles}; On \unsure{est ramené|va revenir} au cas Card I'=2",
    ["éventuelles", "essentielles", "est ramené", "va revenir"],
    "The alternatives do not alter the proved injection for actual distinct geometric points. No intrinsic definition is manufactured from either adjective.",
    "No mathematical discrimination between the word readings", ["B.28"])
add("LM_P042", "140-2", [418], "211 continuation", "Axiom ⑤(b), codomain of the two composites",
    "phi_i lambda, phi_i mu : Gamma -> M_a(pi), with no primes in the written target",
    ["Literal M_a(pi)", "Typed target M_{a'}(pi'_i)"],
    "The already defined morphism phi_i has codomain M_{a'}(pi'_i), and conjugation in the same sentence is by pi'_i. B.13 and B.29 use that actual composite. This supports a typed correction, not a claimed change of the ink.",
    "Strong mathematical typing support for the primed target; literal reading retained", ["B.13","B.29"])
add("LM_P042", "140-2", [418], "211 continuation", "Axiom ⑤(c), missing exception",
    "Tout relèvement admissible ... provient ...; no exception for P is repeated",
    ["Literal universal statement including the canonical class P", "Statement restricted to the complement of P, as in the two displayed bijections"],
    "Scan 417 declares P an admissible target class. The display of ⑤ removes P and clause (a) excludes it from the image. The literal final clause therefore conflicts with those two assertions. B.13/B.29 test the displayed complement and preserve the conflict. The suggestion that admissibility already excludes P does not resolve its explicit membership on scan 417.",
    "Strong internal contradiction if all literal quantifiers are imposed; editorial repair remains provisional", ["B.13","B.29"])
add("LM_P042", "140-2", [418], "211 continuation", "Second display, bijection of Gamma-sets after passing to germs",
    "A limit over all open subgroups, with the same deleted point P",
    ["A statement at the one full Galois group", "A Gamma-set statement over all finite extensions"],
    "The second display quantifies over the germ system. B.29 proves the fixed-field finite-descent result; a germ version requires the corresponding input over all finite extensions. The register does not infer those equalities from one field.",
    "Strong quantifier distinction supported by the displayed maps", ["B.13","B.29"])
add("LM_P042", "140-2", [420], "212 continuation", "Axiom ⑥, parenthetical action before the diagram",
    "Gamma' acts, but the parenthetical homomorphism is written Gamma -> N_a(pi)",
    ["Literal Gamma", "Gamma' as required for the given partial action"],
    "The diagram and the subsequent partial splitting place the given action over Gamma'. B.12/B.13 explicitly distinguish the partial domain from its proposed extension.",
    "Strong typing support for Gamma'; no handwriting resolution", ["B.12","B.13"])
add("LM_P042", "140-2", [420], "212 continuation", "Axiom ⑥, concluding action group",
    r"une action admissible unique de \unsure{Gamma|Gamma'} ... qui prolonge celle de Gamma'",
    ["Gamma", "Gamma'"],
    "The dashed diagonal in the diagram has domain Gamma. Extension of the existing Gamma'-action means a full Gamma-action; retaining Gamma' would only restate the supplied action. This supports the former mathematical formulation while preserving the visible alternative.",
    "Strong diagrammatic support for the full domain; reading provisional", ["B.12","B.13"])
add("LM_P043", "140-2", [421], "213", "Definition of L and the following pullback extension",
    r"L=Ker((N_a)_{I'} -> \unsure{N_a|N_0}); the next lines use \unsure{N_{a'}|N_{0'}}",
    ["Written unprimed N_a (first pass N_0)", "Typed target N_{a'} (first pass N_{0'})"],
    "The supplied checked note says the ink has N_a without a prime. The group being pulled back is then described as an extension of N_{a'} by L along Gamma -> N_{a'}. B.12/B.13 use the kernel of that specified map to N_{a'}, and do not present the correction as a new reading.",
    "Strong mathematical typing evidence; the unprimed literal target is retained", ["B.12","B.13"])
add("LM_P043", "140-2", [421], "213", "After equation (31), uniqueness and existence",
    "cette condition implique l'unicité; l'existence signifie que Norm_E(Gamma') -> Gamma est épi",
    ["Uniqueness from L^{Gamma'}=1 and a separate surjectivity condition", "The stronger implication that vanishing alone gives existence"],
    "The checked text expressly separates the two. B.12 proves the normalizer criterion and gives a finite S3 counterexample to the stronger implication posed in the prompt. It is not attributed to the manuscript's written distinction.",
    "Strong agreement of text and exact group proof; no new palaeographic claim", ["B.12"])
add("LM_P044", "140-2", [431], "218", "Margin beside Conjecture provisoire profinie",
    "Canulé cf plus bas...",
    ["Canulé, in the supplied checked reading", "Corrigé, in the superseded first pass"],
    "The author's expressed doubt on scan 433 and failure mechanism on scan 434 support treating the provisional claim as withdrawn. B.16 supplies the actual meeting sections.",
    "Checked-note preference corroborated mathematically; remains an inherited reading", ["B.13","B.16"])
add("LM_P044", "140-2", [431], "218", "Margin on the filling reduction",
    "du moins si g ne 0",
    ["g≠0 in the checked manuscript reading", "g=0 in one printed witness"],
    "The notes report a not-equal sign. The exceptional genus-zero three-puncture regime in B.6/B.25 shows why the stated qualification cannot be discarded; it does not independently decipher the sign.",
    "Mathematical support for caution in genus zero; no independent reading", ["B.6","B.25"])
add("LM_P044", "140-2", [431], "218", "Number attached to the preceding condition",
    "(4°)",
    ["4° in the checked transcription", "3° in the first pass"],
    "The work references the content of the condition rather than using the doubtful former numbering to identify an axiom.",
    "Editorial evidence only; no new mathematical discrimination", ["B.13"])
add("LM_P044", "140-2", [432], "218 continuation", "Margin about universal families and étale multisections",
    "(g,nu) ne (0,3); sans doute ... multisection(s) étale(s)",
    ["(g,nu)≠(0,3)", "Equality sign in an earlier witness", "n'a", "n'admet", "multisection étale", "multisections étales"],
    "The sentence is an expectation marked sans doute. B.17–B.18/B.23 prove stated higher-genus ranges, while B.24 constructs low-genus multisections. None of these makes the entire margin a theorem.",
    "Strong support for treating it as a qualified conjectural margin, not a proved universal prohibition", ["B.17","B.18","B.23","B.24","B.27"])
add("LM_P044", "140-2", [432], "218 continuation", "Definition immediately before conclusions (a)–(d)",
    "Une action effective ... est dite effective, si l'action ext. est effective ...",
    ["Literal repeated effective", "Admissible in the two predicate positions, as suggested by the next sentence"],
    "The checked transcription keeps effective twice. B.tex explicitly types the intended predicate but preserves the circular literal reading in the editorial discussion. The next clause says effectivement de façon admissible.",
    "Strong contextual evidence for a slip; no permission to silently rewrite the transcript", ["B.13"])
add("LM_P044", "140-2", [432,433], "218 continuation and 219", "Stronger fixed-subgroup guess",
    r"pi^{\unsure{Gamma^+|Gamma^dagger}}=(1)",
    ["Gamma^+", "Gamma^dagger"],
    "The 1981 raised mark remains unresolved. F.1 proves the explicitly stated 1983 ker(chi) precision and B.10 gives the full-open-subgroup assertion. The 1983 formula supplies the precise theorem used, not a retroactive reading of this mark.",
    "Strong theorem comparison; no palaeographic discrimination between the two superscripts", ["B.10","B.11","F.1"])
add("LM_P044", "140-2", [433], "219", "Conclusion (c), quotient target",
    r"pi^{prime natural}=\unsure{pi(i)|R(i)}",
    ["pi(i)", "R(i)"],
    "B.13/B.29 define the actual quotient by the closed normal subgroup generated by the filled inertia. Either notation must refer to that specified quotient for their comparison to apply. The transcription alone does not settle the letter.",
    "Mathematical formulation explicit; reading unresolved", ["B.13","B.29"])
add("LM_P044", "140-2", [433], "219", "Conclusion (d), final assertion",
    "le complémentaire de son image ... égale à {P}; tout à fait douteuse",
    ["Image complement equals {P}", "Only injectivity is retained after the stated doubt"],
    "The insertion changes the claim to its complement. The author immediately doubts that additional part, and scans 434–435 explain why meeting family sections invalidate it. B.16 proves that mechanism.",
    "Strong support for separating injection from the withdrawn image assertion", ["B.13","B.16","B.29"])
add("LM_P044", "140-2", [434], "219 continuation", "Comparison of actions and families",
    "correspond. moralement",
    ["moralement in the checked transcription", "maintenant", "manifestement in earlier attempts"],
    "The source describes a heuristic dictionary. B.33 supplies an actual product-family comparison, and the general nonconstant-family theorem remains unfinished. No categorical equivalence is asserted from the adverb.",
    "Checked-note reading; mathematical scope does not exceed the specified map", ["B.16","B.27","B.33"])
add("LM_P044", "140-2", [434], "219 continuation", "Surjectivity sentence",
    "la surjectivité déconne",
    ["déconne in the checked transcription", "demeure in the first pass"],
    "The immediately following explanation is that distinct family sections may meet. B.16's diagonal and constant graph provide exactly that failure, supporting the checked negative reading.",
    "Strong contextual and mathematical support for the checked correction", ["B.16"])
add("LM_P044", "140-2", [435], "220", "Strict distinction and the arithmetic germ subgroup",
    r"strictmt|strictement distinctes; bold Gamma'_dot subset bold Gamma | bold Gamma' subset bold Gamma",
    ["Gamma' with a low dot", "Gamma' without the low dot", "Earlier Pi reading is not retained by the checked notes"],
    "The source says distinct at every point of S and compares restrictions along the point-induced arithmetic germs. B.16 proves the corresponding disjointness condition through these actual section maps. The low dot is not resolved.",
    "Mathematical content strong; typographic dot remains provisional", ["B.16","B.30","B.33"])
add("LM_P044", "140-2", [437], "221", "Margin on points at infinity",
    "Recover the disposition of the points at infinity from the outer involution",
    ["Forget the two local flags when they have the same global class", "Retain the actual two-element cusp torsor and both incidence maps"],
    "C.5 shows the two local elements can map to one global component class. C.6 retains both flags; C.14 uses the functorial finite cover maps to recover cyclic order and its signs. The distinction is a proved map-and-fibre calculation.",
    "Strong mathematical evidence for the flagged interpretation of the programme", ["C.5","C.6","C.14"])
add("LM_P044", "140-2", [438,439], "221 continuation and 222", "Nonorientable quotient assertion and correction",
    "The initial all-nonorientable claim is corrected in the margin; orientable quotients are added",
    ["Only nonorientable quotients", "Both quotient types, with r>0 for the orientable case"],
    "C.1 constructs each quotient's oriented double. The formulas g=q+r−1 and g=2h+r−1 prove the extra types and the corrected count. The manuscript's gamma counts extra crosscaps after RP2, so q=gamma+1.",
    "Strong proof of the corrected mathematical range; no claim that the initial text was different", ["C.1"])
add("LM_P044", "140-2", [440], "222 continuation", "Equation (4), sg sign",
    "sg(sigma)=+1 in the supplied checked text and witnesses",
    ["Literal +1 with an as-yet-unchecked convention for sg", "A slip relative to the usual orientation character, which is −1 for an antiinvolution"],
    "The source notes explicitly ask that sg's definition be checked. C.1–C.18 state orientation reversal directly and do not silently replace the written sign or use it under an unspecified convention.",
    "Unresolved sign convention; no mathematical conclusion depends on choosing one reading", ["C.1","C.10","C.13"])
add("LM_P045", "140-2", [441], "223", "Section-class notation",
    "Sc(E,Z/2)",
    ["Set of pi-conjugacy classes of splittings", "Nonabelian H1 only after a chosen splitting"],
    "C.3/C.4 retain the extension and its section classes, including the nonsplit fixed-point-free case. H1 is used only when a splitting has actually been chosen.",
    "Strong typing support; checked transcription, not newly deciphered", ["C.3","C.4","C.13"])
add("LM_P045", "140-2", [442], "223 continuation", "Conjugation before the fixed-subgroup equality",
    "quitte à remplacer phi_i par un conjugué",
    ["phi_i, in the checked reading", "g_i, in the first pass"],
    "The map from the deck group of the lifted real component is conjugated. Replacing a generator by a conjugate induces the same subgroup comparison, but the proof in C.3/C.4 explicitly keeps the homomorphism and its image.",
    "Checked-note preference with compatible maps; no new reading", ["C.3","C.4"])
add("LM_P045", "140-2", [443], "224", "Parenthesis on factorization through components",
    "assez triviale de ttes façons",
    ["de ttes façons", "de ses fibres in the first pass"],
    "The statement concerns factorization through pi0, not a declaration that the fibres have already been proved trivial. C.3 proves both factorization and bijectivity separately.",
    "Strong contextual support for the corrected scope", ["C.3"])
add("LM_P045", "140-2", [444], "224 continuation", "Equation (10), fixed-cover target",
    "Main insertion: U-tilde^{sigma_i}; margin: U-tilde_i^{sigma_i}",
    ["Target without i", "Target with i"],
    "The cover and its lifted involution are those attached to component Z_i. C.3's covering-square argument uses that actual selected cover. Adding i is a typed notation repair supported by the margin, not a new claim about the main-line ink.",
    "Strong diagrammatic support; both written forms retained", ["C.3","C.4"])
add("LM_P045", "140-2", [445], "225", "Corollary 1, range of i",
    "0≤i≤g in the checked manuscript reading",
    ["0≤i≤g", "1≤i≤g in printed witnesses"],
    "At i=0 there are no real components and hence no order-two effective lift. C.10 keeps the zero-class assertion, while clauses choosing a lift and the later index assertion are vacuous.",
    "Strong boundary-case support for preserving i=0", ["C.3","C.10"])
add("LM_P045", "140-2", [445], "225", "Margin restricting the labels",
    "et X_g/sigma non orientable",
    ["Include the margin's nonorientable-quotient restriction", "Treat the labels by i as a classification of all real types"],
    "C.1 shows why equal oval count can occur for two quotient orientabilities. C.13 supplies the additional dividing invariant. The fixed-group theorem itself holds for both quotient types.",
    "Strong mathematical support for the restriction's exact role", ["C.1","C.3","C.13"])
add("LM_P045", "140-2", [446], "225 continuation", "Definition of Y_{g,i}",
    "Y_{g,i}=X_g^{sigma_i}, followed by a compact connected bordered surface description",
    ["Literal fixed set X_g^{sigma_i}", "Quotient X_g/sigma_i"],
    "The fixed set is a one-dimensional union of circles; the next construction uses the two-dimensional quotient with those circles as boundary. C.1 and C.10 specify the quotient map and its oriented double explicitly. This proves the typed repair without changing the retained literal expression.",
    "Strong dimensional and morphism-based evidence for the quotient interpretation", ["C.1","C.10","C.18"])
add("LM_P045", "140-2", [447], "226", "Equation (16), end arrows and index assertion",
    "The arrows to 1 are cancelled; the source centralizer has kernel T≅Z",
    ["Index of the image in the outer centralizer", "An index of the source group itself as if embedded"],
    "C.10 proves the exact map with kernel Z and uses the orbit stabilizer of a lift class. This computes the image index i. The source is not treated as an embedded subgroup without its quotient map.",
    "Strong exact-sequence evidence; cancellation retained", ["C.10","C.15"])
add("LM_P045", "140-2", [448], "226 continuation", "Interlinear adverb in the orbit proof",
    "transitivement",
    ["transitivement in the checked manuscript reading", "trivialement in several printed witnesses"],
    "The proof then identifies a stabilizer of index i. A trivial action would give index one. C.10 proves actual transitivity by homeomorphisms of the quotient permuting boundary components.",
    "Strong mathematical corroboration of the checked correction", ["C.10"])
add("LM_P045", "140-2", [448], "226 continuation", "Cancelled first proof of Corollary 2",
    "The map of effective to outer centralizers is surjective",
    ["Cancelled surjectivity for all i", "Replacement orbit-stabilizer assertion with index i"],
    "For i≥2 the proved image index is i, so the cancelled claim cannot be used. C.10 writes the actual replacement and the kernel.",
    "Refuted cancelled claim; no revival of struck text", ["C.10"])
add("LM_P045", "140-2", [448], "226 continuation", "Cancelled Corollary 3 on surface torsion",
    "Pi=pi1(U), torsion tied to a nonorientable bordered surface with compact boundary",
    ["Literal ordinary surface group Pi", "Possible intended real extension E of the oriented double"],
    "The literal surface group is torsion-free outside the stated RP2 exception. Replacing it by E would still require correcting the boundary and orientability qualifications, since every real component gives a section. The text is struck and neither version is used as a theorem.",
    "Strong mathematical refutation of the literal cancelled assertion; intended replacement unresolved", ["C.3","C.4"])
add("MPL_148_029-072", "148", [43], "No folio normalization supplied", "Qbar-algebraic row, approximate lines 37–38",
    r"\unsure{pour opération|pour y obtenir}; \unsure{dessus via|des sections}; \unsure{Gal/Q}",
    ["pour opération ... dessus via Gal/Q", "pour y obtenir ... des sections Gal/Q"],
    "The supplied doubt register calls both fragments low confidence and says they remain unresolved after enlargement. B.21 proves the pointwise finite-field-definition/germ content of the section reading, and refutes a stronger universal Q-model reading using j=√2. The operation-via-Galois reading instead supplies an action and is not silently converted into that stronger section claim.",
    "Low palaeographic confidence as supplied; the two mathematical interpretations are explicitly separated by their maps", ["B.21"])
add("MPL_148_029-072", "148", [43], "No folio normalization supplied", "Tower letter and Qbar-algebraic label",
    "Doubled-stem tower letter transcribed mathbb T",
    ["mathbb T", "An unsettled Pi-like doubled-stem form"],
    "The result uses only the row's stated Qbar-algebraic objects and their field-of-definition maps. It does not infer an extra group or topology from the unresolved tower letter.",
    "Medium-to-low supplied reading confidence; no mathematical discrimination", ["B.21"])
add("MPL_143+141", "143", [2], "Top 1; bottom 1", "Constants hypothesis beside the absolute automorphism sequence",
    r"Il faut supposer ... Qbar est la \unsure{clôt. int.} de Q ds \unsure{Gamma_X}",
    ["Integral closure of Q in global functions, as tentatively read", "The compressed symbols remain unresolved"],
    "A precise version must make absolute automorphisms preserve the distinguished constants before mapping them to G_Q. The finite-type field-of-definition proof supplies an open stabilizer; it does not turn the absolute automorphism map into a surjection onto all G_Q. The non-Q-model example in B.21 tests that overreach.",
    "Medium supplied reading confidence; strong necessity of an explicitly preserved constants subring", ["B.21"])
add("MPL_143+141", "143", [2], "Top 1; bottom 1", "Margin after the partial descent lift",
    "grain de sel d'effectivité de descente; de gr. prof.",
    ["Both phrases are tentative in the supplied first pass", "No additional secure alternative supplied"],
    "Actual finite-field models give partial lifts. Conversely one must retain continuous effective descent data; an arbitrary abstract outer action is not assigned a model by the point-germ proof. The margin is treated as a qualification, not a theorem asserting effectivity in all settings.",
    "Medium supplied confidence; general effective-descent interpretation remains provisional", ["B.13","B.21","B.25"])
add("MPL_143+141", "143", [4], "Top 2; bottom 3", "Equation (10), section-germ label",
    r"\unsure{varphi_xi^t|varphi_xi}",
    ["varphi_xi with an overwritten superscript-like stroke", "varphi_xi without a superscript"],
    "The surrounding text defines a germ over an open Gamma', modulo equality after smaller open restriction and geometric conjugacy. B.1/B.21 use that precise equivalence. No exponent is needed or inferred.",
    "Low supplied confidence for the stroke; germ definition itself explicit", ["B.1","B.21"])
add("MPL_143+141", "143", [5], "Bottom 4", "Germ-only phrase and semi-abelian hypothesis",
    "le germe seulement des phi_xi; avec variation à is doubtful",
    ["The parenthetical wording remains tentative", "The semi-abelian embedding clause is retained exactly as a hypothesis"],
    "Equality on a common open subgroup means equality over a common finite field of definition. B.1 proves injectivity there using semi-abelian Kummer theory. It does not infer this point-injection claim for every scheme after discarding the embedding hypothesis.",
    "Strong mathematical proof for the specified hypothesis; doubtful parenthesis unchanged", ["B.1","B.21"])
add("MPL_143+141", "143", [6], "Top 3; bottom 5", "Cyclotomic action and cancelled margin",
    "T(Qbar)=lim mu_n; chi in (18); the chi=1 margin has six and three unread words",
    ["The live cyclotomic action formula", "Cancelled, partly illegible qualification about purely arithmetic interpretation"],
    "B.22 proves equivariance using compatible roots of local parameters and the actual Galois action on roots of unity. The cancelled partly unread margin is not used to impose chi=1 or to modify this map.",
    "Strong live-formula comparison; unread cancelled words remain unread", ["B.22"])
add("MPL_143+141", "143", [7], "Bottom 6", "Normalization of the universal cover",
    r"l'extension \unsure{étale|totale} définie par X'-tilde",
    ["étale", "totale"],
    "B.22 uses the normalization of the compactification in each finite covering field and then the compatible inverse system. Its boundary maps are the actual stabilizer and inertia maps, so no conclusion depends on selecting the uncertain adjective.",
    "No mathematical discrimination between the word readings; construction specified independently", ["B.22"])
add("MPL_143+141", "143", [8], "Top 4; bottom 7", "Margin beside equation (22), dimension reservation",
    r"ici il est supposé dim X=1; autrement il faut \unsure{voir|revoir} la définition",
    ["voir", "revoir"],
    "B.22 retains the one-dimensional construction and replaces it at a strict crossing by the local product inertia with its actual global map. The diagonal kernel example proves that forgetting this map would be an unjustified extension.",
    "Strong mathematical support for the dimension reservation; verb unresolved", ["B.22"])
add("MPL_143+141", "143", [8], "Top 4; bottom 7", "Continuation of the margin, henselian/local wording",
    "pour donner des [one unread word] henséliens ou locaux au dessus d'un pt ...",
    ["The several compressed phrases remain doubtful", "No secure reading of the unread word supplied"],
    "The proof specifies strict henselian normal-crossing local parameters and a homomorphism to the global fundamental group. It does not reconstruct a more general original definition from the unread phrase.",
    "Low supplied confidence; no editorial completion of the unread word", ["B.22"])
add("MPL_143+141", "143", [12], "Top 6?; bottom 11", "Programme, finite-cover paragraph",
    "automatiquement for every finite étale cover; Il faudrait expliciter ce point avec soin",
    ["The live inserted étale", "No claim that the complete reconstruction programme is already proved"],
    "B.22 gives H\\Pi/D_y, the intersections H∩gI_yg^−1, the ramification-index map, and the open subgroup s^−1(H) on which a germ lifts. These are the explicit finite-cover comparison maps. No full intrinsic description of G_Q follows merely from them.",
    "Strong mathematical verification of the finite-cover assertion in its stated range", ["B.22"])
add("MPL_143+141", "143", [12], "Top 6?; bottom 11", "Two viewpoints and the puncturing reservation",
    r"dans les \unsure{=|2} optiques; forage des trous, inserted si dim X=1",
    ["=", "2"],
    "The deletion/filling maps in B.13/B.29 and the cover maps in B.22 are written without selecting the uncertain sign. The explicit dimension-one qualification is retained.",
    "Unresolved glyph; no effect on the stated one-dimensional constructions", ["B.13","B.22","B.29"])

out = ROOT / "B_C_editorial_readings.json"
out.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n")
assert all({"package","scan","place","support","strength"} <= r.keys() for r in rows)
assert all(r["provisional"] and not r["fresh_scan_inspection"] for r in rows)
print(json.dumps({"entries":len(rows), "output":str(out), "fresh_scan_resolutions":0}, indent=2))
