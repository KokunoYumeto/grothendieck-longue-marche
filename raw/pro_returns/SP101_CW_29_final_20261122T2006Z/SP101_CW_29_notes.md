# SP101_CW_29: notes while reading

These notes describe only the supplied scans. A transcription decision is not a proof check. Mathematical checks, where actually performed, have separate entries in CHECK_EVENTS.tsv. Printed or typed blank symbol positions remain blank in the transcription; any mathematical completion discussed here is editorial.

## Scan 013

Page-content account: The page begins section 1, Données de ramification sur un schéma. It defines a ramification datum as a pair consisting of a category fibred over the étale site of S and a cartesian functor to the category of relative schemes. Objects of its fibre over S\prime are called ramification models, and their images are called geometric realizations.

Own qualifications in the source: The fibred category is not assumed to be a stack. The realization functor is assumed neither faithful nor fully faithful, so morphisms between models cannot be identified with morphisms between their realizations. The later examples are said to have realizations finite over S\prime.

The final paragraph forms the inverse-image fibred category D of finite étale relative schemes along geometric realization. Its fibre at M is described as finite étale coverings of s(M); the page then begins a definition, ending after the underlined revêtement de and a cancelled word clipped at the right edge.

Targeted check (013-fibre): by the definition of inverse image of a fibred category, an object of D over M is a pair (M, Z → s(M)) with Z finite étale over s(M); a morphism in the fibre is a map of such Z over the identity of s(M). Thus the stated fibre is precisely the category of finite étale covers of s(M). This verifies only the fibre description, not any later descent or representability claim, and does not authorize completing the blank arrows.

## Scan 014

French typed page defining crible couvrant and the category of revêtements of type R from a system of categories, then stating full-faithfulness and compatibility conditions for an inductive-limit construction. It ends mid-sentence with alors et.

The source has detype S, retained without changing S to R. It also has Signaons without l, and spaces in d essus and s chémas.

The compatibility of the realization limits is introduced as an assumption: “Nous supposerons”. The source later prints r(X′_o), although X′ alone was just defined as the restriction; the subscript o is clear and is retained. The phrase detype S occurs where the preceding definition names type R; this is a visible mismatch, not an emendation.

The completed blind audit retains several local qualifications. The raised word ending eine has n/p alternatives in its first cell and e/l or d/l alternatives in its second, with both impression orders open. In variable, the fourth cell combines s/i, while the separately cancelled terminal s remains doubtful. The first cancelled word after forment is un/on/ou; the final s of deleted fibrée(s?) is uncertain against an empty cancelled position. The first r(X) retains displaced/underlined-r readings and both r/f orders, without requiring a separate underline in the r/f alternatives. The final verb preserves the separated r and accorde, followed by plain nt or an m/nt overprint in either order.

## Scan 015

The cancelled opening block proposes a category of coverings as cartesian sections, names Rev_R(S), and defines geometric realization by an inductive limit only if it exists. It additionally makes existence for every covering a condition before the surviving on obtient clause. These are statements in the cancelled source, not adopted conclusions of this edition.

The following live paragraph says the realization functor will be faithful in the cases of interest but need not be fully faithful. It expressly warns that a covering is not determined by knowledge of its geometric realization. The source says une revêtement and déterminée; those agreement forms are retained.

Example 1 begins with an S-scheme Z carrying a finite group G acting by S-automorphisms, with the inserted qualification à droite disons. It introduces the one-object category C_o, whose inserted object name is e and whose endomorphism monoid is G, then the category product Et_S x C_o.

The written text says limite inductive while the arrow under Lim visibly points left. This discrepancy is retained without mathematical correction.

The final paragraph contains a q/a composite in the third cell of ét...les. The completed audit retains both possible impression orders: q cancelled before a, or a cancelled before q. The standing letter is not settled as a plain source spelling.

Targeted check 015-cartesian: for C = Et_S × C_o and a fibre category C′ over Et_S, a cartesian functor is determined, up to coherent isomorphism, by its value E over the terminal base object S and the homomorphism from the endomorphism group G to Aut(E). Cartesianity identifies its values over T with pullbacks of E. Conversely, pullback of E with its action constructs the functor, and equivariant maps give the natural transformations. This verifies the stated categorical identification at the abstract action level; it does not determine the handedness convention or prove the later realization claims.

The completed reading audit retains four alternatives for the cancelled handwritten glyph before the displayed r: underlined s, underlined xi, phi and r. The cancelled phrase before les objets remains sur/aux; the overtyped verb after nous retains both rm/ur orders in the same baseline cells; and the cancelled fragment before catégorie remains mét/rét/cét. In cancelled compatible, only the a between p and t is marked doubtful. These are local transcription uncertainties.

## Scan 016

The page continues a discussion of geometric realizations of G-covers. It says that a realization exists exactly when the quotient Z′/G exists and identifies the realization with that quotient. An affine-open condition on every G-orbit in Z is given as sufficient and inherited by Z′; in the intended situation Z covers S, and the page explicitly adds the sufficient assumption that Z be affine over S. The resulting X is said to be finite over S.

The heuristic description is expressly qualified as en première approximation and en un sens convenable: these covers become étale above the chosen cover Z, which may be ramified. For an open U, the page assumes the restriction of Z is a principal G-cover V and either V is dense or, more generally, every G-stable open-and-closed part of Z containing it is all of Z. Restriction is asserted faithful and descent over V to U an equivalence; the conclusion is faithfulness of geometric realization. The last part describes covers of S with a structure of type underlined R by an isomorphism class of a model and an isomorphism of its realization with X. It stops mid-sentence at (Cette.

Targeted check 016-affine: since Z′→Z is finite, the inverse image of an affine open of Z is affine. The image of a G-orbit in Z′ lies in one G-orbit in Z, so the latter’s affine neighbourhood pulls back to an affine neighbourhood of the former. If Z→S is affine, each orbit lies over one point of S because the action is by S-automorphisms; an affine neighbourhood of that point similarly supplies the claimed neighbourhood. This verifies the stated inheritance of the orbit condition, without checking the general quotient-existence theorem.

Targeted check 016-restriction: for two equivariant maps between finite étale covers, their equalizer is open and closed in the source. The complement has open-and-closed image in Z under the finite étale source map, and this image is G-stable. Agreement over V makes that image disjoint from V. The stated hypothesis on G-stable open-and-closed subsets then forces the image to be empty, so the two maps agree. This verifies the restriction-faithfulness step in the finite étale setting of Example 1.

Check 016-composition records the first reader’s formal implication: composing the stated faithful restriction with the stated descent equivalence gives a faithful composite; if this composite factors through geometric realization, realization is faithful. The independent existence/descent assertions are not established by that implication.

The committed main audit qualifies four local readings. In the cancelled phrase beginning plus généralement que, the next word begins with d/s alternatives and the final s after fibre remains doubtful. After cancelled donc and raised i.e., the following baseline word retains plain d or a d/e overprint in either order, followed by the clear es. The cancelled three-letter form before live un is ajn/ujn, with j and n retained and only its initial a/u unresolved. In cancelled une donnée/donnee de, the acute remains uncertain because the descender of the interlinear catégorie crosses its position. These qualifications preserve the audit's local limits without changing the page's mathematical account.

## Scan 017

Content: continuation of a remark on faithful/fully faithful realization in the dense normal case, followed by Exemple 2 on a filtered projective system (Z_i,G_i), its categories of coverings and a sufficient transition condition. This is a description of the source's statements, not a verification of its proof.

Source qualifications: the page starts mid-sentence with dernière and ends after the added étale Z'_j without closing the last parenthesis. No continuation or missing text has been supplied.

The right paper edge leaves only résult and surjecti. Both witness completions (résulte and surjectif) exceed the surviving ink.

Eight principal map/membership/relation slots are uninked; the restriction bar supplied by H after the second Z-prime is likewise absent. The isomorphism phrase is preserved as Z_j [blank] Z_i/N_ij, including the low R at the comma, without mathematical repair.

Both occurrences of systême have a circumflex. Unaccented epuisent and joined estéquivalente and imagesinverses are preserved. Before groupes, the final cell after de remains unresolved among a cancelled s, live x, live s, deleted s followed by x, and deleted x followed by s. The last R retains its live/struck-state doubt.

Targeted mathematical check (017-normal): on a normal affine integral base, a map between finite étale covers over a dense open induces a map of the generic finite algebras. Each image of an integral generator is integral over the normal finite étale target algebra and therefore lies in it; this gives the unique extension, which glues by uniqueness. This checks the normal-base restriction step under this affine reduction. The further assertion about geometric realization and the transition-system equivalence is recorded, not independently proved here.

The cancelled three-letter group after Rev retains etd/età/est as competing readings in the completed audit. The central tall t and the final hooked or accented form are preserved as local uncertainty; the following live estéquivalente remains joined.

## Scan 019

The first paragraph is a continuation. The author asserts that geometric realization is well defined in the case under discussion, gives the stated restriction to each Rev category, and says that the faithful/fully faithful criteria from example 1 extend immediately. These are source claims, not results independently proved in this reading; the earlier reference numeral has unresolved 1/2 overtyping.

Example 3 imposes hypotheses on R=(C,s) and a factorization through the fibered category of relative schemes with a finite group of operators acting on the right. The page calls the second functor oubli des opérations, retaining its cancelled final key.

The author explicitly motivates the choice of morphisms by the Kummerian example mentioned below. Such morphisms are pairs (f,u), with u a locally constant group-scheme morphism, and the source expressly says pas nécessairement constant !. This qualification is part of the text. The ink says f:X [blank] X prime despite the surrounding object pairs being (Z,G) and (Z prime,G prime).

The further hypotheses state a quotient-isomorphism condition involving the kernel H, prescribe a homomorphism G [blank] Aut(M) with s prime(g) equal to the pair (g_Z,int(g)), add a local-form condition on endomorphisms, and require compatibility with inverse images and with the indicated morphisms. Their asserted relationships are described here as source hypotheses; this page reading does not verify their sufficiency or prove them. The attachment of the isolated tel remains uncertain and therefore the exact scope of that qualification is not silently fixed.

The committed main audit retains a/l and o/l alternatives in the first Flop name and d/l and o/l alternatives in compatib...e, with both impression orders open. The cancelled glyph before pas nécessairement may be an opening parenthesis or f. The live word after cancelled déf is flêche with a circumflex; this does not alter the separate reading of the earlier cancelled flèche passage. The divided cancelled word resolves as one déterminé, with no additional e or repeated miné continuation. In the final target formula, the second object letter remains M, repeated M, or an X/M overstrike in either order. These documentary qualifications leave the source hypotheses and the uncertain attachment of isolated tel as recorded.

## Scan 020

The top three closely spaced lines state that geometric realization is defined and induces the previously described realization functor on each Rev_{R_i}(S). A separate continuation beginning de Z_j gives Z_j′ and the quotient Z_i′/N_{ij}, then says that the faithfulness and full-faithfulness criteria of example 1 extend to this case. No relationship with another physical page has been inferred from H’s editorial note.

Example 3 gives finite automorphism groups for objects M, a unique compatible homomorphism G′ to G for each morphism M′ to M, and an isomorphism from s(M′)/H to s(M) for its kernel H. The corrected condition requires two morphisms from M′ to M to differ by composition with an element of G. It then requires a surjective étale family over which two objects admit a common majorant. The earlier global filtered-category formulation and an intermediate group-homomorphism formulation are cancelled and retained in the transcription.

The page invokes descent to define realization with values in covers of S. It explicitly qualifies this by assuming the s(M) are covers and remarks that affineness over S′ suffices for applying descent. The following faithfulness and full-faithfulness tests are reduced to the corresponding conditions for each pair (s(M),G) in example 1. The bottom heading opens Cas particuliers du type kummérien, case a), and stops after sections.

The local-majorization context could suggest that both object subscripts should be S′_i, but the source distinctly reads M_{S′} and M′_{S_i}; those unequal written indices are retained. The adjacent category C_{S′_i} and the family S′_i confirm the intended local setting without changing the source labels. No mathematical expectation filled a symbol slot or settled the order of the typewriter impressions.

The completed reading audit adds q/a overprint alternatives in the cell following the existing g/f composite of satisfasse. It also retains s as the first reading of the line13 target realization symbol, alongside either e/s overprint order; the local symbol may instead be a damaged s impression. In the cancelled phrase schémas finis sur, only the terminal s of finis is doubtful. These are local transcription uncertainties and do not change the source statements summarized above.

## Scan 021

The page continues a definition from a family of Cartier divisors: objects are revised from couples/triples to quadruples, with a finite group and an isomorphism of group schemes. It gives morphisms, composition/base-change data and a functor to elementary Kummer covers, then states faithfulness and qualified full faithfulness. Part b begins a sheaf construction from divisor decompositions and stops at 'Soit donnée une section du'. These are content descriptions, not a proof verification.

The full-faithfulness sentence visibly includes local noetherianity, normality at points of the supports, reduced divisors and the added qualification about components of distinct D_i. The source uses j in the final added D_j and gives no terminal stop after j≠i. The qualification remains an authorial assertion; its general full-faithfulness claim was not independently proved.

Every symbol slot left uninked in this sheet remains blank, including membership, map, comparison and the gap before D_i in the last equation. H's supplied arrow and mu symbols are not ink; its explanatory note explicitly acknowledges restoration of mu and normalization of 2tant. H's page marker, editorial note and differences.tsv's trailing 'document' artefact are not source text.

Source spellings and printed forms include 2tant, flêche, flêches, Sêc and the short comp. The word s...uf contains an i/a composite in either impression order. The second m of morphismes remains m/n, and its comma directly abuts et. The crossed cell after ç in façon has cancelled a/o/x alternatives, with a first; the live on is separate. Initial normal retains both orders of j/n and i/n. In the added component qualification, the fifth letter of composante remains o/c, while the extra e in de'un is established as cancelled.

In the last divisor equation, the low prime has a broad head, an additional horizontal stroke above it, and a separate equals farther right. The lower of the apparent extra pair merges with the prime head. The committed reading therefore retains an overbarred-prime alternative alongside the three prior live/cancelled equals arrangements. The whole formula and its blank position before D_i are preserved; chronology and cancellation of the equals-like material are not established.

Witness S, c29a_CORRECTIONS.tsv:row2, is confirmed as a report of the literal last-line condition on scan021: nonzero restrictions are deux à deux disjointes. The local-spectrum word is literally Sêc, and the membership slot after s′ is blank. S's replacement sans composante commune is an editorial proposal, not source ink.

Targeted check of the distinction: in A=k[x,y]_(x,y), the effective Cartier divisors D1=V(x) and D2=V(y) are reduced and have no common irreducible component, but their supports meet at the closed point (x,y). Both restrictions to Spec A are nonzero. Thus the literal disjointness condition excludes this elementary normal-crossing example. More generally two nonempty closed subsets of a local spectrum contain its closed point, so nonzero effective divisors cannot be pairwise disjoint there. This proves the stated obstruction; it does not prove every later assertion about the proposed corrected sheaf.

The cancelled et before the first u:G expression is resolved, with its blank map slot and low underlined n retained. The cancelled underlined rounded symbol near the final divisor equation has Q/Omega/delta/D/O alternatives. The separate live symbol remains theta, and the inserted (D_i) remains above the cancelled symbol.

## Scan 022

Page-content account: the continuation associates a sheaf to the preceding presheaf and says that a jokingly called condition canularesque on the family (D_i) makes it a presheaf. Étale-local presentations reduce to the earlier case a), giving ramification data; the literal base in the sentence is B. The sheaf construction and case a) are referred to, not re-derived on this page.

Two divisor cases follow: S locally noetherian with D having normal crossings and étale-local regular irreducible components; and S over a prescheme T with D having relative normal crossings and étale-local smooth components. The final base letter in the second case is an S/T overprint, whose chronology is left unresolved.

The page states a full-subcategory description of coverings in case 1 and expressly qualifies the extension to case 2 by sauf erreur (il faudrait le vérifier). It names broad tame ramification relative to D and says this is broader than ramification data consisting only of D.

The page attributes to Abhyankar a characterization involving being étale off supp D, normal over supp D, having each irreducible component dominate one of S, and classical tame ramification at maximal points of D. These are the source's assertions and qualifications; no external verification was used.

The sheet ends mid-sentence and mid-quotation after relativement à la. The apparently unmatched NB parenthesis and the extra opening parenthesis after Rev are preserved. The category slot after où and the membership slot in the indexed family are visibly blank.

Mathematics used in reading: relative-to-T context identifies why H proposes T, but cannot remove the visible S component or settle chronology. The surrounding S likewise does not change the clear B. The plausible category letter and membership relation were not supplied. No formal derivation was needed to resolve a glyph.

The pen mark crosses the apostrophe/o area of qu'on, rather than standing neatly after the n. Its adjacent encoding does not assert a letter replacement, cancellation, or certain insertion point.

Witness S c29a_CORRECTIONS.tsv:row2 also points to the continuation’s condition canularesque. That literal phrase is confirmed here. The mathematical distinction between local disjointness and having no common component is discussed under scan021 and recorded in CHECK_EVENTS.tsv; this page is not silently rewritten to the proposed corrected condition.

The completed audit retains S/R/fi/si for the cancelled fragment before et, with S first among the unresolved candidates. The semicolon followed by a separate period in intérêt;. remains unchanged. No additional letter is supplied beneath the second cancellation x.

In the cancelled expression before S minus supp D, the small underlined letter remains r/a/R, with r favoured locally. The capital S, blank interval and underline are retained. This is a local reading uncertainty; no missing operator or different mathematical expression is inferred.

## Scan 023

Typescript continuation, with archival foliation 22. The opening completes the relative notion from scan022. The page asserts that the two notions coincide when T is regular and that the tame specialization theorem can be demonstrated by the technique of SGA 1 for the broad notion of moderate ramification. Its stated hypotheses remain: D is at croisement normaux relative to T, and S is proper and smooth over T. The inserted dans les S with barred-t index is live. These are source claims; no proof of specialization is supplied or independently verified here.

The remarks form the fibered category of coverings with ramification datum R over Et_S and its displayed cartesian functor. The NB assumes that geometric realization on C_{S′} takes values in coverings of S′ and that realization on Rev with R(S′) is well defined. The relation slot between the Et expressions and the map position in the display are uninked; the expected equality and arrow are not transcribed. The parenthesized display label retains a heavy asterisk or an asterisk/equals overprint in either order, without an above-line insertion; it is separate from the functor expression.

The page calls R essentially auxiliary: the category and displayed cartesian functor are the object of study. Two data are deemed essentially equivalent when their functors are equivalent through an equivalence inducing the identity on Rev. Its parenthetical stack claim remains a source assertion. In the underlined word, two a/h overprints admit cahmp or champ as the live sequence; the intended term does not settle their chronology. On line 20, the first inline (*) remains unqualified; only the second reference, after c’est, shares the display label’s heavy-asterisk or asterisk/equals-overprint alternatives, in either order.

The final sentence starts an example involving a fibered subcategory C′ of C and continues beyond this leaf. The outside /S′ in the slice formula is visibly lower, while the final C′ underline excludes the prime. The lower R in the first Rev is cancelled and replaced by raised R. Literal auxdiviseur(s), Evidemment and croisement normaux remain. The committed edge review confirms a complete r followed by a partial possible s, so diviseurs/diviseur remains unresolved. The raised dans les S with barred-t index is attached after D with barred-t index and before the parenthesis. The dense x in aux does not establish a separately readable underletter.

## Scan 024

The first passage gives a local majorization condition: for each object M of C indexed by S-prime, a covering by S-prime_i is required on which the pulled-back object is majoré by an object from C-prime. It also explicitly assumes that the geometric realization functor for R-prime is induced by that for R. Under these stated conditions the author says R and R-prime are equivalent.

The Kummer example is expressly restricted to the case in which the D_i have global equations given by sections c_i of underlined O_S. The multi-indices are said to be prime to the characteristic of S, with the exact reservation supposée exister. The crossed-out plural formulation retains caractéristiques/caractéritiques as local alternatives before résiduelles.

The author additionally supposes a chosen isomorphism between the projective group system whose visible notation begins with underlined Z and the system whose base glyph is left blank before a lowered underlined n. The text says such an isomorphism exists when S is a scheme over an algebraically closed field, for example. No missing base symbol or product operator has been supplied.

The author then identifies the situation with the conditions of example 2, obtaining R-prime and asserting its equivalence to the datum R in the Kummer case a). The visible word at the right edge is constat. An e may have lain outside the surviving image, but none has been transcribed, and the truncation is not treated as a proven authorial spelling error.

The second example's initial right-acting group of the principal covering P retains H-prime as the primary reading, alongside H/G overprinting in either order. The audit cannot establish whether the curved remnant belongs to an uneven H or to a superposed G, or determine the strike order if two letters are present. The later commuting-action clause and operator-group clause clearly name G-prime. The separate left action of G is explicitly required to be free. These local readings remain qualified as committed.

The definition of Z-prime has a keyed lower-case x with raised G. The author asserts that the resulting R-prime is equivalent to R and begins to explain this using functors. The final explanation is partly obliterated, so the reading does not establish a complete proof.

The final two baselines contain a large pale/erased band. The second functor name and underline positions are tentative; R-prime above it and opérateurs below are legible. Later black islands cannot be read as complete words. The existing estimate of three unreadable words is retained provisionally, after opérateurs, without assigning identities to the traces.

The cancelled phrase includes a separate dash before alors, retained as - alors. After équivalentes, the crossed punctuation may be a colon, semicolon or period; the following live comma remains distinct.

## Scan 025

The opening continues a local étale reduction to P=G'_S, with the right regular G' action and a left G action described using a monomorphism whose arrow slot is blank. The following paragraph comments on normalizing ramification data and compares the auxiliary/intrinsic distinction with sites and topoi. Neither passage is supplied with preceding-page context here.

Section 2 states finite projective and inductive limits and exactness properties of the displayed Rev category, cites Exp V n-underlined-superscript-o 4 and conditions G1 to G3, and gives epi/mono factorization. An added clause says that epimorphisms and monomorphisms are effective, followed by the assertion that every monomorphism identifies a direct summand. These are source assertions transcribed on this page, not proofs checked by this reader.

The G-to-G' map slot and the main-symbol and basepoint slots in the heading's fundamental-group notation are uninked. No arrow, pi or basepoint letter is supplied. The comment-paragraph Rev alone has a lower rule under the three letters; the later Rev names retain only their separately underlined raised R.

Targeted check of the final warning about products, using the finite-group example on scans015–016. Let k be an algebraically closed field of characteristic other than 2, S=Spec k[[a]], Z=Spec k[[t]] with a=t², and G={±1} acting by t↦−t. The equivariant finite étale cover E=G×Z has geometric realization E/G≅Z. Its categorical square is E×_Z E=(G×G)×Z with diagonal G-action; its quotient is G×Z≅Z⊔Z.

The ordinary scheme product of the two realizations is Spec B, where B=k[[a]][t,u]/(t²−a,u²−a). This is finite over the local ring k[[a]], and its closed fiber k[t,u]/(t²,u²) has one maximal ideal. Hence B is local and its spectrum is connected, whereas Z⊔Z is disconnected. The two products are not isomorphic. Equivalently, the two maps u=t and u=−t give the two branches in the normalization. This directly verifies that realization need not preserve a binary product. It does not prove the full exactness list or the finite-colimit assertion on this page.

The page ends visibly with dis- at the paper edge. The hyphen is retained and the incomplete word is not completed. The archive's pencilled 24 is comment-only. H's page marker is not source text, and purely equivalent operator/font macro syntax was excluded from the difference count.

The completed audit expands the composite before l after alors to both o/i impression orders while retaining the earlier b/d possibilities. The first exactitude word has two separate local uncertainties: plain a or either a/e overprint order, followed by plain s or c or either s/c overprint order. These source forms are not normalized from context.

The cancelled punctuation after de plus remains semicolon/comma, with semicolon first; en particulier remains raised above it. Within the raised effective-epi/mono clause, t, r and i in cancelled stri are resolved and only s is doubtful. In cancelled par suite au, the final x remains doubtful because it cannot be separated from the cancellation row.

The line-initial word is resolved as mnomorphisme: the consecutive keyed cells begin m, n, o, with no intervening first o. The source spelling is retained without a doubt wrapper or an added letter.

## Scan 026

Page-content account: the opening continuation requires a fibre functor and identifies exactness with conditions G4 and G5 of V 4. In example 1 each geometric point of Z gives one; the source says it is conservative under the condition that every G-stable clopen part of Z is empty or all of Z. Example 2 uses a geometric point of the written limit of Z_i.

Targeted check of the case 1 conservativeness condition: for a G-equivariant morphism between finite étale covers of Z, the subset of Z on which it is an isomorphism is open and closed, since finite étale objects and their morphisms become finite sets and set maps étale locally. Equivariance makes that subset G-stable. If the map is bijective at the chosen geometric point, this locus is nonempty. The stated hypothesis that every G-stable clopen subset is empty or all of Z forces it to be all of Z. Thus the geometric-fiber functor reflects isomorphisms in case 1. The broader connected-site equivalence and reconstruction of the profinite group are not independently proved here.

For example 3 the source chooses a point outside its quoted ensemble de ramification and spells out principality for the operator coverings attached to objects M over étale S-prime. The point notation is incompletely keyed, and the prose contains the literal du l’image. Its raised s is an addition after l’image; the later slot after de remains blank.

The source states that the geometric fibre functor is exact and is conservative exactly when the site C with the topology induced from Et_S is connected. It then assumes r(M)/G to S-prime is an isomorphism, with the explicit qualification ce qui sera sans doute le cas dans tous les cas intéressants, and identifies connectedness with connectedness of S under that assumption.

Applying the cited theory of V 4, the page asserts a profinite group and an equivalence between its finite continuous actions and Rev with ramification label R. Its group notation has the upper underlined R and lower 1 but an uninked base symbol and point argument. The next section begins functorialities in S and R and breaks off after announcing a functor from a scheme morphism.

Mathematics used in reading: exactness, geometric fibres, and the profinite-group discussion identify the roles of the blank positions, but do not supply arrows, a pi, or point letters. The quotient-isomorphism assertion is retained as prose without completing its missing map sign. No external theorem or neighbouring page was used to decide a glyph, and no formal mathematical computation was needed.

The committed main audit refines the discarded wording locally. The cancelled cell after à is u/n, with u first. The long cancelled clause reads T à groupe G, followed by du/d and the separate de, then à'un/d'un/l'un, then du schéma à opérateurs G. The du before schéma is resolved as two keyed cells. In the cancelled connectedness gloss, the wording is couvrant du/de ce sjte/site, with du and sjte first. These qualifications concern cancelled wording and leave the mathematical account and its stated limits unchanged.

## Scan 029

Page content: a continuation about inverse-image ramification data, equivalence of covering categories and the induced fundamental-group statement, followed by discussion of why a general inverse-image construction is awkward for Kummerian data and whether axioms on a datum would be preferable.

The opening is a continuation beginning est; its missing subject is not supplied. The asserted equivalence is explicitly 'toujours sous les conditions de l'exemple 3'. The fundamental-group conclusion is additionally conditional on having an unramified geometric point of T. The extension to the Kummerian case is described as following an 'à peu près évidente' étale localization.

The example involving (Z,G) is expressly tied to example 1. The source says the precise inverse image of the datum from (D_i) is not the corresponding datum from (D_{i T}), even up to equivalence of fibred categories; it calls them only 'essentiellement équivalente' in the sense of numbered section 1. These distinct levels of equivalence are preserved.

The suggested axiomatic conditions are again under the conditions of example 3 and are said to 'assurent moralement' the essential-equivalence relation. The source leaves the decision to a rédaction en forme and says the conditions must apply directly to the Kummerian cases. No unqualified theorem or independent proof verification is inferred.

Both arrow slots are uninked. The source's keyed x products, the two systême spellings, the redundant phrase 'à la donnée de définir une donnée', qu' without il, and the page-final général- remain. The final hyphen is not completed from another leaf.

Crop02 shows the rule only beneath rivial; crop17 shows est pas underlined with n' outside the rule. Crop07 has three points before the parenthesis. The two paired-quote passages use raised typewriter strokes, not guillemets.

All seven cancellation/overprint loci are retained. In addition to est and a), the completed audit resolves cancelled capital R and avoir. The cancelled fragment after schéma retains co[n/u]v[r?], and the cancelled cell after au retains g/q. The plusieurs composite retains both h/l and d/l impression orders. The parenthesized reference key retains star/pi and both x/equals overprint orders; its production sequence remains unresolved.

The earlier descriptive candidates cxxvx/connx and xxRx/xxex included crossing-out x impressions. The committed audit replaces them with the partly recovered underlying co[n/u]v[r?] fragment and the resolved cancelled R, respectively. The former avoir/avxix alternatives are resolved to avoir. These changes do not alter the two literal keyed x product signs, and they supply no letters beneath otherwise unrecoverable cancellation marks.

## Scan 031

Page-content account: The opening continues an observation about passage to a completion, with geometrically normal formal fibers of the local ring and excellence given as examples. It then asserts that the same observations apply without a normality or reducedness hypothesis when restricted to the corrected class mod.ram. galoisiens.

The heading opens the treatment of Galois coverings. The paragraph defines an R-type Galois covering using a finite group acting on the right, the principal-object condition and a covering map to the final object. It then describes the same notion through the fundamental groups of the multigaloisian category and through the principal G-coverings of the s(M).

The page itself qualifies the subsequent terminology as an abuse of language for the realized object (r(X),G). It says the abuse is relatively harmless when geometric realization is fully faithful after restricting the source morphisms to isomorphisms; the stated consequence is uniqueness up to canonical isomorphism of the Galois object over a given realized pair. The final sentence promises a necessary and sufficient condition in example 3 but stops at suffisan.

The typed replacement mod.ram. is above x-cancelled kummériens; the latter's individual letters and acute are recoverable. Revêtement is typed above cancelled objet. The insertion's circumflex is fully visible in the supplied half, although crop22 cuts its highest point; blind box b22 begins higher to include the complete sign.

All four Rev formulas have raised, singly underlined R, checked independently in crops08,11,17,20. The local-ring O has its own lower rule and lowered S,s. The s(M), C with lower S-prime, and realization r(X) each retain their individual lower rules. All these capitals are ordinary typewriter forms, not a bold or double-struck alphabet.

Mathematical conservativity: the principal-object formulation indicates where one would expect two map symbols, and the parenthesized object expression indicates a membership relation. The three slots are visibly uninked, so no arrow or membership sign has been supplied. The products use keyed lowercase x, not a printed multiplication glyph. No mathematical inference was used to replace legible ink or decide overprint order. The conditional uniqueness consequence is checked separately below.

S evaluation — c29a_CORRECTIONS.tsv row 1, exact content supplied by the main reader: it revises a single doubtful 3 to doubtful 4|3 in this heading and says that 4 and 3 are overtyped with stroke order undecidable. Crop06 independently supports that two-glyph/order-undecidable observation, so both deletion orders are retained. Its contextual statements about the earlier section heading and the letter of 24.4.67 were not reopened or used as evidence for physical strike order. The row's preferred numeral order is therefore not treated as a recovery of chronology.

The page's parenthesis about uniqueness has a direct conditional justification. If the realization functor, restricted to the stated isomorphisms, is fully faithful, and two objects X,Y carry specified identifications alpha:F(X)→T and beta:F(Y)→T with the given operator cover T, fullness lifts beta⁻¹ alpha to an isomorphism X→Y and faithfulness makes that lift unique. Thus the lift of the fixed identified cover is unique up to a unique compatible isomorphism. The word canonical has this compatible meaning; without fixed identifications the objects may retain automorphisms. This checks the conditional consequence only, not the later criterion for full faithfulness.

The completed blind audit refines seven physical places. The initial s of s'appliqueront is separate from the following d/apostrophe-a overprint, whose order remains open. The first underlined galoisiens has i/s or i/n in the first composite cell and d/s (first) or i/s in the second, retaining both orders and the continuous word underline. The cancelled cell before droite retains r/n/x with r first; the cancelled cell after un resolves to e. The later singular galoisien retains i/e or t/e in both orders. The edge cancellation resolves to ph; its terminal x-shaped impression is crossing-out only, and no missing word ending is completed.

## Scan 032

The page starts with the surviving fragment te; no beginning is reconstructed. It has a French paragraph followed by an indented English paragraph.

In the particular case called example 1, the author takes a strict local object S-prime at a point of S, a connected component Z-prime-sub-o of the base-changed Z-prime, and its stabilizer H in G. The word distingués is an actual raised insertion qualifying the two subgroups H_1 and H_2.

The stated condition concerns a given u between quotient expressions, compatible with a quotient-group isomorphism denoted by a manuscript slashed oval. The source quotient has component index o, while the written target has component index 2. The target 2 is retained literally; it is not changed to o to make the construction consistent.

The author requires an element g of the locally heavy H such that int(g) sends H_1 onto H_2 and induces the manuscript-labeled isomorphism on quotients, and such that u is induced by the endomorphism g indexed by Z-prime-sub-o after passing to quotients. In the general case called example 3, this requirement is asserted for all couples (underlined s(M),G) on the various S-prime in the indicated Et context. The membership and map positions on the page remain uninked and are not completed.

The English paragraph asserts that this condition is satisfied for Kummer data by combining 1.10. and 1.15. of Murre’s notes. Those external results were not opened or verified; this is a statement made by the source.

The author explicitly qualifies the earlier reluctance with wrongly so. The corrected terminology is tamely ramified, replacing cancelled Kummer. The passage says that in the non-galois case a covering needs extra structure rather than merely extra conditions, while in the Galois case that structure is uniquely determined if it exists. The existence qualification is retained.

The source warns that not all nonisomorphism morphisms in the usual naive sense between even Galois tame coverings should be admitted: it restricts them to those coming from morphisms in Rev with raised underlined R over S. It cites a counterexample to prop.1.16. in Murre’s notes as a warning. No counterexample is constructed or checked on this page.

The next claim concerns products of tame coverings whether galois or not: the natural categorical product is said not to be the naïve fibered product over S. The source connects this point to the complication in the proof of Murre’s lemma 4.3. It concludes that the indicated category is needed even in the Galois case for understanding the situation.

Localise has no final accent; come form is the actual word order; undispensable begins with a clearly typed u. These secure source forms are preserved, and none is listed as a remaining doubt. The inserted naive has an ordinary single dotted i, whereas the later naïve has two dots.

Both handwritten formula marks have a closed oval and an oblique through-stem. They are encoded locally as phi-shaped manuscript signs. This does not identify them with the underlined slashed-oval notation of other pages.

At each of the two heavy-letter loci—the first numerator and the group letter after élément g de—the committed audit retains H as the primary reading, adds G/H overprint alternatives in both orders, and keeps the qualified repeated-H possibility. The curved outer-left/lower material permits G without establishing either a definite second impression or its chronology. These local alternatives do not infer a blackboard alphabet from darkness or extend to the other H letters. The manuscript phi, quotient indices, blank map interval and target H/H_2 in the quotient formula remain as committed.

The lower-left 31 is archival foliation and is comment-only in TeX. H’s terminal editorial note about spellings and its following subsection headline are not ink on this scan and are excluded as editorial material rather than counted as source-word differences.

Targeted check 032-tame-product-warning: the quadratic example recorded for scan025 has ramification index 2, prime to the residue characteristic when char(k) is not 2. Its categorical product realizes to a disconnected pair of copies of Z, whereas its naïve fibred product is connected. Thus it also supports the warning here in a tame example. The cited propositions and lemma of Murre were not consulted or independently verified. See scan032_main_math.json and CHECK_EVENTS.tsv.

In the line 4 morphism word, the first composite cell retains both d/s orders; the second now leads with i/o in either order while retaining both h/o orders. These are local reading alternatives, with no chronological priority established. The cancelled fragment before compatible retains il, a blank space at the intervening pure cancellation-x cell, and a tentative final u/n. No missing source letter is inferred from that intervening cancellation.

## Scan 033

Page content: the underlined heading retains two r/o overprints, with the Remords order first. The page criticizes the presentation of example 3 of par.1. as neither elegant nor natural and proposes conditions a)–d) on underlined R instead of the displayed auxiliary structure. The opening has s prime followed by et de and a blank; the absent second datum is not supplied.

Source qualifications in a): for M in underlined C with lower S prime, the associated étale sheaf of automorphisms is said to be represented by underlined G(M), finite and étale over plain S. S is not changed to S prime. The parenthesis opened before évidemment has no closing mark after unique près.

Source qualifications in b): every morphism is called an epimorphism and every endomorphism an automorphism. For a labelled morphism with an uninked map slot and an automorphism g' of M', existence of g with gu=ug' is asserted; the following paragraph asserts uniqueness and a unique compatible group homomorphism. The formal implication from the epimorphism condition is checked below; its existence hypothesis remains an assertion of the source, and no arrow is inferred in the transcription.

Source qualifications in c): si before l'homomorphisme is cancelled, leaving surjectivity asserted in the live sentence. H is named as the kernel and an isomorphism of a quotient is stated. The principal-bundle wording is cancelled and retained as such. The live NB explicitly assumes the s(M) are relatively affine and says this makes the quotient meaningful. No additional affineness or descent hypothesis is supplied.

Source qualification in d): the two homomorphisms are said to differ locally for the étale topology by composition with an automorphism. The final word is physically clipped; only automorphi plus a partial s-shaped boundary remnant is transcribed, not a completed automorphisme.

The raised cancelled M-prime blank M formula attaches between morphisme and dans in condition b). The committed audit identifies the two central x impressions as cancellation marks, so the underlying interval is left blank. No invisible pre-cancellation arrow or other symbol is supplied. Its inserted and deleted states and raised attachment are preserved.

Right-edge loss is distinguished from ordinary spelling: line 15 shows only d, while the a of opér…tions has two surviving left fragments and remains doubtful. The final s in automorphis is likewise only a partial left-edge reading. No invisible letters are completed.

The article cell before cancelled homo contains both an e body and an apostrophe impression. The final objet cell is narrowed to y/t in both orders. The topologie cell retains I/o, t/o and lowercase l/o in both orders. These local alternatives preserve uncertain impression chronology.

Two acute-like marks in the cancelled fibéé are positive ink; the alternative penultimate r therefore retains its own acute. The comma after cancelled s(M) is resolved in the committed audit: its separate rounded head and tapering curved tail extend below the cancellation. This physical place is counted once despite the overlapping boxes.

Underlines were checked locally: the heading is fully ruled and now retains two r/o overprints with the Remords order first; first G(M) in a) is underlined, subsequent G forms are plain; each lower rule on s, C, Et and R is preserved at its own occurrence. Main and reader did not harmonize those differences.

In condition b), uniqueness of the automorphism g follows from the stated epimorphism property of u: if gu=ug'=hu, then g=h by right cancellation. The assignment g'↦g preserves products, since both the assigned image of g'_1g'_2 and the product of the assigned images compose with u to ug'_1g'_2; it also preserves the identity. Applying the same argument after each étale base change makes the assignments compatible with restriction, provided the datum's pullbacks and the universal version of b) are used. Thus they give a morphism of automorphism sheaves; under the representability asserted in a), the representing group schemes inherit this homomorphism. This checks the formal implication and its hypotheses, not representability or the surjectivity and quotient assertions in c).

The sheaf in a) is defined on the étale site of S′, whose relative representing object naturally has base S′; the typescript nevertheless says finite and étale sur S. The printed base is retained, and the intended relative base is discussed only here.

The completed audit narrows cancelled un/du to d followed by uncertain u/e. In cancelled morphisme, only the penultimate m is doubtful. The cancelled principal-bundle clause begins with i and e, while both stops remain uncertain. The single cancelled letter after M-prime in condition d) is resolved as d, replacing the former et/à alternatives.

The cut-edge mark within the split topologie is a line-end hyphen. The supplied C29-03 convention joins line-end hyphenated words; the joined word retains all I/o, t/o and l/o alternatives without treating that hyphen as an additional lexical character. This convention does not complete the separately clipped edge words.

## Scan 035

The leaf is an English letter beginning Dear Murre,. It supplies no date, place, closing, signature or author identification. A single body paragraph explains the intuitive content of the writer's notes through a standard Kummer covering Z=Z_a^n over normal S. The paragraph passes from a bound on ramification to a normalized inverse image, a function-field description, a strictly local reduction, and an equivariant-covering description. It ends at étale coverings without a terminal stop; no continuation or closing has been supplied.

The source's qualifications are retained: the example is offered for definiteness; the description is introduced as intuitive; S is normal; the inserted (normal, say) S′ qualifies the coverings after coverings; the birational discussion assumes S′ connected; the subextension is explicitly a sub-K-extension in an extension L′ unramified with respect to the model Z. The statement hence L′=L is an interlinear addition within the strictly local case. The NB then assumes, for simplicity, Z connected and the normalisation of S in a finite Galois extension L/K. The desired notion is said to be local for the étale topology.

Mathematics was used to locate possible inconsistencies, not to replace letters. The proposed transport of the G action and the later quotient S′=Z′/G suggest that Z′ would be expected as the object carrying the action. The actual intervening source text distinctly reads operate on S′. That S′, agreed by both witnesses, is retained; the expected Z′ belongs only in this editorial account. No unseen context was consulted to settle the claim.

The last inserted étale lies above the coverings followed by (Z,G), not the earlier coverings of S. This placement is confirmed by its physical position and is consistent with the source's distinction between coverings bounded in ramification and equivariant étale coverings. That consistency did not override the ink. No formula is supplied in a blank, no prime has been transferred between letters, and no claim about omitted hypotheses is used to repair the source.

Clear source peculiarities remain: the isomor...ic form lacks p; s rictly contains an empty cell where standard spelling would have t; operationson is joined; now,for has no blank after the comma. The first category is unaccented, whereas the following two catégory forms and final catégories have clear acute accents. These settled observations are not listed as continuing doubts.

The three explicit cancelled passages are But by transport de, the extra h after with inside the interlinear parenthesis, and the fragment after Thus. The last fragment is uncertain w/n, then e, a blank cell and re; its middle x belongs only to the cancellation. The final cell of normalized preserves e/d overtyping with both chronology alternatives. The low loop under the u of But remains locally uncertain. The isomor...ic form retains h/f overprint in both orders, with surviving h first, and a circumflex-like alternative; no p is supplied. The positive mark on e in morėover retains dotted e first, acute e or e with a raised apostrophe-like mark, with no plain-e alternative and no claim about the mark's date or attachment mechanism. None of these local uncertainties establishes a global substitution or typing habit.

The phrase 'G operating on Z must operate on S′' is written with S′, but the next clause calls Z′ a G-covering of Z and gives S′=Z′/G. The compatible action required by that construction is on Z′. This is an editorial type correction, not a transcription change. In the normal affine generic-field model the intended construction can be checked directly: let A′ be a normal domain with fraction field K′, let L/K be the stated finite Galois extension with group G, and let D be the integral closure of A′ in L⊗_K K′ (using its product of field factors). The action on the L factor preserves D. Since (L⊗_K K′)^G=K′, every fixed element of D lies in K′ and is integral over A′, hence belongs to A′; conversely A′ is fixed. Thus D^G=A′, giving the asserted quotient in this affine model, with the action on the normalized pullback. The claim that this normalized pullback is étale over Z is the ramification condition being imposed, not proved by this argument. Finiteness of the normalization where required for a finite covering is an additional ambient hypothesis.

## Scan 079

Murre’s letter is dated 30-4-69 and signed J.P. Murre. He describes a preliminary treatment of formal tamely ramified coverings and plumbing, divided into preliminaries (Chap. I-VII) and Grothendieck’s notes plus plumbing (CHap.VIII-X). He requests an opinion on the preliminary version and says the chapter on the analogue of Mumford’s theorem remains unwritten.

His own qualifications include “am still not ready with the above mentioned” project, “what do you think of this set-up and do you think it worthwhile to continue in this way?”, and “The chapter on the analogue of the theorem of Mumford has still to be written.” No mathematical assertion in this letter has been independently proved in this transcription pass.

## Scan 080

Page content: comments on chapters I, II, III and VI of an unidentified manuscript. The sheet discusses étale morphisms of formal schemes, Kummer coverings, tamely ramified coverings, and dependencies among numbered results. These are source statements; the referenced chapters and proofs were not supplied or consulted, and no mathematical proof verification is claimed.

The author expressly limits these comments: “No attempt has been made towards completeness”; for 3.5.5 there is “only an indication of the proof”; normality is said to be “(perhaps” not stable under étale localization. These are the author's reservations, not conclusions verified in this run. After perhaps, an upper curved tick and separate low horizontal stroke are transcribed as an apostrophe-plus-low-stroke alternative to a damaged closing parenthesis.

## Scan 081

English comments headed Comments (2). The writer discusses technical and delicate results in chapters VII and IX, a canonical isomorphism in VIII, a proof in a Giraud letter, usual schemes and SGA 1 Exp.XII, and the plumbing in X. No date or signature occurs, so authorship is not inferred from this leaf.

Own reservations: “In IX-1 there are several points about which I am not certain”; “In IX-2 I have not included” the proof of key-theorem 9.2.3; “I hope that part IX-3 is correctly written”, with the inserted qualification “and that I don’t have overlooked difficulties”; and the question whether results on usual schemes are included in the planned final SGA 1 Exp.XII. These are the writer’s reports, not proof checks performed here.

The two formulas record disjointness assumptions. The two small round indices in the second formula are read as lowercase o from their type height; no mathematical interpretation is imposed. The small point following 8.1.6 remains uncertain because it coincides with the insertion leader’s endpoint.
