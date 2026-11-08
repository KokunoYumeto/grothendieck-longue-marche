# LM_C3-397-415: editorial and research notes

## Source and scope

Grothendieck, A. (1981). *La Longue Marche à travers la théorie de Galois* [Autograph manuscript, cote 140-3, archive file “pages 293–650”; supplied scans 397–415]. Université de Montpellier.

The transcription is based exclusively on the 19 supplied image files. No published transcription, external edition, or reconstruction from later mathematics was used. All scan references below refer to those supplied filenames. Research observations cite this primary source by scan and local formula or text position; they are not a literature review and make no claim of novelty.

### Pagination and transcription conventions

- `\scanpage{N}` follows the filename, from 397 through 415. The secondary lower numerals are 396 through 414 and therefore must not be used to shift the scan references.
- Original pagination visible at the top is retained with `\mspage`; a doubtful overwritten numeral remains marked. Lower handwritten numerals inside the black frame are retained as marginal numerals without attributing their hand. The printed archival footer outside that frame is not manuscript text.
- Cancellations, insertions, marginal remarks, unusual numbering, unclosed written punctuation, and unreconciled mathematical notation remain in the fragment. No expected right-hand term has been supplied for an unfinished formula.
- Confidence concerns the reading of ink, not the truth of a mathematical statement. High confidence is used only for a secure reading that merits comment because it may appear surprising. Alternative readings remain local in `\unsure{reading|alternative}`.
- The LaTeX file is a fragment and supplies no macro definitions or preamble. It uses standard LaTeX, AMS mathematical notation, `tikz-cd`, and TikZ, with the requested editorial macros. An integrating preamble should give `\uline` and `\uuline` robust text-and-math definitions, allow the editorial macros in both modes, and treat `\diagram` as a mode-neutral wrapper: arrays include their own math delimiters. The diagrams use `ampersand replacement=\&` so that their matrices work inside macro arguments. `\rotatebox` is used for written vertical signs. The standard `\figure` command must be redefined as the requested editorial wrapper.

## Table of doubts

Locations are approximate visual lines or positions on the scan; parenthesized formula numbers are the manuscript’s own. A row may cover repeated occurrences of one doubtful letter or abbreviation. The complete occurrence index at the end also locates every in-place uncertainty mark in the delivered fragment.

| Scan | Approximate line / location | Reading | Alternative(s) / qualification | Confidence |
|---|---|---|---|---|
| 397 | (4), initial overwritten letter | `\deleted{\unsure{\mathcal A}}\mathcal M` | Overwritten first letter may be a previous M; underlying strokes cannot be separated securely. | low |
| 397 | prose after (4) | `évidemt` | Appears abbreviated, rather than the full “évidemment”; final superscript is uncertain. | medium |
| 397 | following line | `trivial` with superscript `mt` | The last strokes could form `t` alone. | medium |
| 397 | (5)–(7), group superscript | `*\flat` | Second dark sign might be `\sharp` or an overwritten/deleted sign. | low |
| 397 | (5), just after `(0)` | cancelled `\infty` | Several black strokes meet the arrow; original sign uncertain. | low |
| 397 | (6), first ambient factor | cancelled `\mathbb G_m` followed by `T_0` | Overwriting may instead involve a previous T; present T₀ is retained. | low |
| 398 | (9), lower left group | `SG`, with cancelled `SLG` | Underlying overwritten letters are difficult to separate. | low |
| 398 | (9), right vertical map | cancelled `det` | Could be a different overwritten label; arrow itself is clear. | medium |
| 398 | after (9), “et G …” | `idm` | `idem`; the abbreviated ending is not clear. | medium |
| 398 | “Notons-le” | `Notons` | Initial N is heavily overwritten. | medium |
| 398 | (10), far right | an additional terminal `1` connected by a stroke | Could be a retraced/cancelled end of the sequence; retained rather than silently suppressed. | low |
| 398 | last line | inserted “à composantes”, then `toriques` | `torique`; the long stroke above the adjective is read as the insertion leader, but could also partly cancel it. | medium |
| 399 | first prose paragraph, fourth line | `déductions` | `directions`; middle letters are compressed. | medium |
| 399 | (14), first left-hand group | cancelled `J`, then `I` | Overwritten glyph could still be J; no correction from the mathematics has been made. | low |
| 399 | (14), determinant after the bar | cancelled `x`, then `y` | Overwriting may be a retrace rather than a distinct cancelled x. | low |
| 399 | (14), next line, left group | `J` | `I`; index after ρ looks overwritten, σ/x. | low |
| 399 | (14), N prime superscript | `\flat` | `\sharp` or overwritten old sign. | low |
| 399 | final paragraph | `dévissage` | Middle syllables are very compressed; no full alternative securely read. | medium |
| 400 | annotation above (15) | `compos. neutre` | First abbreviated word could be `comp.`; leader points to the neutral-component notation. | medium |
| 400 | last line of the ambient-product identification | `T_σ` | Index looks retraced over ρ. | medium |
| 400 | (17), last scalar condition | `λ²` | The λ and superscript are overwritten; the square is read from the ink, not imposed. | medium |
| 400 | (17), cancelled expression to the right | `≃ T_ρ ×_{G_m} T_σ` | Cancellation traverses the symbols; fiber-product subscript is faint. | medium |
| 400 | (17), last group superscript | `*` | Black scribble could be an altered superscript. | low |
| 401 | annotation to (19) | `p. 487' (20)` | A short stroke after 487 is retained as a prime. | medium |
| 401 | small map below (20) | cancelled `(0)` | Overwritten suffix may have been `(∞)`; ink does not settle it. | low |
| 401 | paragraph after (20) | `on`, cancelled `a deux`, inserted `le` | Revision crosses several words; surviving syntax is not repaired. | low |
| 401 | second exact sequence number | cancelled `(22)`, then `(21)\|(22)` | Both digits have been retraced; the second digit more closely resembles 1. | low |
| 401 | “On a … dans” | cancelled `donc` | Only part of the word survives the dark stroke. | low |
| 401 | replacement above “suite de composition” | `structure d'extension` | Right end runs toward the edge; ending uncertain. | medium |
| 401 | cancelled filtration, before SG | `×` | A dark correction could be a product dot. | low |
| 401 | NB note, last line | `et J° ∩ SG ≃` | No right-hand object is securely visible; the leader continues toward the product sign. The unfinished expression is retained. | medium |
| 401 | (24), after SG | `}` | Curved stroke could be a continuation/correction mark rather than a formula delimiter. | low |
| 401 | cancelled line below (24) | `utilisant l'inclusion` | First word faint under the deletion. | medium |
| 401 | annotation above cancelled inclusion | `inexistant` | Ending and attachment are uncertain; leader points toward the claimed G inclusion. | medium |
| 402 | 4 | envisagés | Final plural stroke is faint; envisagé is possible. | medium |
| 402 | (27) | deleted `+` after `M^{circ+}` | Compact overwrite; an earlier superscript cannot be separated confidently. | low |
| 402 | (27), final superscript | `+` | `*`; the superscript is overwritten. | low |
| 402 | above (28) | deleted `M` | Letter is overwritten; could be an abandoned symbol. | low |
| 402 | below (28) | paraphrase | The diagonal marginal note crosses the beginning. | medium |
| 402 | left marginal note, opening | Vu un peu traîner | Opening is difficult even after enlargement and rotation; this is a tentative reading of each group of strokes. | low |
| 402 | marginal note, parenthesis | deleted qui; est tombé au loin | Overwritten first word and cramped sloping text. | low |
| 402 | marginal note, middle | même dans la suite suivant I | Last roman numeral and grammatical joins are uncertain. | low |
| 402 | marginal note, parenthesis after `tau` | dans l'expression ! | Tiny overlapping characters; mathematical subscript is clearer than the prose. | low |
| 402 | marginal note, last line | noter | Could be another short infinitive; no mathematical correction inferred. | low |
| 403 | reference after opening paragraph | §45 | §46; last digit has a fast diagonal stroke. | medium |
| 403 | remark, just before “sur S” | connexe relativement | The first word is a continuous low stroke; the second has a compact overwrite at its beginning. | low |
| 403 | (33) | dotted tau, dotted tau infinity | Dotted `t`; small handwriting does not clearly distinguish the two alphabets. | medium |
| 403 | before (34), group letter after Gamma | script M | Script G or an overwritten earlier group letter; a reading from the asserted meaning has not been substituted. | medium |
| 404 | (35), before `r_0` | deleted tau | The earlier symbol is overwritten by the present name. | low |
| 404 | (35), first matrix, lower right | 0 | The zero has been retraced or overwritten. | medium |
| 404 | middle, replacement above a crossed word | deleted comportant; inserted donnant | Deleted ending is obscured by the horizontal stroke. | medium |
| 404 | middle, after “les sections” | deleted involutives | Overlapped by the inserted three tau labels and “sont de.” | medium |
| 404 | struck line above `Z` | isomorphe à | The line is cancelled through letter centres; reading is tentative. | low |
| 404 | `Z` definition below struck line | insertion, underlined | A curved enclosing line and upward stroke connect it to the cancelled centre assertion; the insertion's precise intended anchor is uncertain. | low |
| 404 | crossed lower block | “injectifs” | The strokes after the opening quotation mark are compressed; closing quotation mark is weak. | medium |
| 404 | crossed penultimate line | la composée | “les composés” is possible; singular/plural must not be chosen from grammar. | low |
| 404 | crossed last line | mb | Abbreviation for membre is likely; a terminal `r` is not distinct. | medium |
| 405 | crossed opening continuation | centralité triviale | The middle word has long, joined strokes and is crossed obliquely; this is a tentative reading, not a correction of the mathematical phrase. | low |
| 405 | top deleted product and target | G_m times; T_rho | Small former annotation and heavily retraced target letter. | medium |
| 405 | On a mbar, first group | T_0 prime | B_0 prime; the letter has been thickly overwritten. | low |
| 405 | crossed parenthesis above non trivial | resp. phi avec f=1 | First cluster may instead be a compact tuple; only “avec f=1” is secure. | low |
| 405 | crossed word right of {+-1} | Le | Tiny word under several strokes. | low |
| 405 | insertion defining L_0 | i.e. | Could be a differently punctuated abbreviated phrase; the following L_0 and epsilon_0^2=ell_0 are clearer. | medium |
| 405 | left below action display | (*) | Isolated mark could instead be a cancelled connective; retained as a tentative symbol. | low |
| 405 | before il est de la forme | deleted etc.; on trouve; nous | All three short fragments are crossed or overwritten. | low |
| 405 | alpha computation | zeta | xi; the descending Greek character is cursive. | medium |
| 405 | epsilon prime computation | epsilon_3(mu) | epsilon_3^b(mu); a small stroke between subscript and argument is uncertain. | low |
| 405 | u matrix, top left deletion | mu | Earlier small entry has been overwritten by diagonal pen strokes. | low |
| 405 | u matrix, top right | mu D | mu B; the ink looks more like D, and the algebra has not been used to silently replace it. | medium |
| 405 | crossed original tuple in (36) | u_infty=-1, a_infty=1, b_infty=tau_infty | Dense hatching obscures much of the tuple; the clear replacement is separately transcribed. | low |
| 405 | NB matrix, deletion before B_0 prime | Gl | Earlier group letter is heavily scribbled. | low |
| 405 | final automorphism sentence, after Sl(2,Z) prime | simeq | The low wavy mark may instead belong to a superscript tilde; left locally uncertain. | low |
| 406 | upper beta expression, before u tau_infinity | deleted tau_infinity | Thick local crossing obscures the final subscript. | medium |
| 406 | (37), old group name after membership sign | deleted M; S script G | The capital prefix is overwritten; script G without the S is also possible. The subsequent new M[0] annotation is transcribed separately. | low |
| 406 | (37), parenthesized group index | 0 | Heavily overwritten but a zero remains the best reading. | low |
| 406 | (37), coefficient ring in lower inserted group name | hatted Z | Plain Z; the small upper stroke partly meets the annotation leader. | medium |
| 406 | cancelled first 2 degree, following the matrix | appliquer le | The last part of the verb overlaps the cancellation wave. | medium |
| 406 | cancelled line below Mais ce n’est pas | paragraphe précédent | raisonnement précédent; the entire phrase is faint and traversed by a long strike. | low |
| 406 | correction paragraph | normalisée | Ending is overwritten; normalisé is possible. | medium |
| 406 | cancelled phrase after normalisée | d’ailleurs nous | The last word is largely hidden by the strike. | low |
| 406 | after lambda=0 | deleted On aura | Thick scribble; a different short future phrase remains possible. | low |
| 406 | retained 2 degree, before (38) | les remarques précédentes | Singular la remarque précédente is possible because the plural endings are fast strokes. | medium |
| 406 | (38), first symbol | r_1 | tau_1; the first horizontal stroke resembles a tau. The subscript on the tuple coordinate was rechecked as u_1. | medium |
| 406 | left sloping margin, first word | réduisant | Ending is a long downward stroke; réduisons is possible. | medium |
| 406 | insertion above qui ne normalise | equality and completion hat on second G | The equality may be an isomorphism sign, and the completion hat is written toward the upper right; both placements are retained as alternatives. | medium |
| 406 | bottom paragraph, crossed word after est | comme | Small low strokes under a horizontal cancellation line. | low |
| 406 | final line, cancelled tau expression | tau_infinity prime | A trailing overwritten stroke is not separable confidently. | low |
| 407 | Top pagination | `504` | Overwritten strokes obscure the first two digits. | low |
| 407 | Line 2, after « élément » | One deleted word unreadable | Dense crossing-out. | low |
| 407 | Equation (40), last line | `dihédral`, `d'ordre 4` | The adjective ending is cursive; the numeral resembles 4, retained despite the square-symmetry parenthesis. | medium |
| 407 | Equation (41), underbrace | `groupe engendré` | Possibly an abbreviation of « sous-groupe engendré ». | low |
| 407 | Below (41) | `trivialt` | The abbreviated ending is a short stroke. | medium |
| 407 | Last underbrace in (41) | Downward mark / arrow | The lower brace meets a short looped downward stroke. | low |
| 407 | Equation (42), after tau | Deleted `[0]` | A dense overwritten bracketed mark. | low |
| 407 | Cancelled bottom line | `et flèche précisée par` | Several endings and the short final word are obscured by diagonal cancellation. | low |
| 407 | Cancelled bottom arrow target | `\mathcal M_{\rho,\sigma}[0](\mathbb Z)` | Initial letter overwritten; cancellation crosses the target. | low |
| 408 | After « pour », above (43) | Deleted `\mathcal M_{\rho,\sigma}(\mathbb Z), donc` | The final word under the long crossing-out is uncertain. | low |
| 408 | Below (44) | `autom. int.` | Very abbreviated strokes; no expansion made in the transcription. | medium |
| 408 | Below the matrix | `l'épim canonique` | Could end at « épi »; final letter is overwritten. | medium |
| 408 | Below the unnumbered arrow | `se factorise par homo` | The beginning is overwritten or struck through; the exact extent of the deletion is uncertain. | low |
| 408 | Denominator in (45) | 4 deleted, 6 inserted | The old low stroke appears to be 4; the active numeral is read as 6. | medium |
| 408 | Last paragraph, after `\mathbb Z/4\mathbb Z` | Deleted `\det a` | Strongly overwritten mathematical letters. | low |
| 408 | Penultimate line | `On notera` | Possibly « On note »; the ending is cursive. | medium |
| 409 | Second body line | `du le sous-groupe` | An extra small article-like stroke is visible after « du »; it may instead belong to a correction. | low |
| 409 | First paragraph | `trivialt` | Abbreviated ending. | medium |
| 409 | Insertions around « centre de SG » | `sous-groupe des points [fixes → invariants] par M` | The two curved insertion routes intersect the prose; exact attachment and the overwritten words are uncertain. | low |
| 409 | After « Le dernier » | Inserted `centre` | The placement of the small added word is uncertain; the underlying « dernier » has not been silently suppressed. | low |
| 409 | Deleted sentence after `\mu_2` | `Il en est de même` | Most of the middle words are obscured by the inserted formula and the cancellation line. | low |
| 409 | Inserted sentence after `\mu_2` | `trivialement` | The word is split across widely separated ends of successive lines. | medium |
| 409 | Upper-left marginal correction | `trivialt`, `invariant`, `G` | Faint ending and highly cursive final group letter. | medium |
| 409 | First factor of parenthetical product | Deleted `\mu_2`, inserted `1` | Initial factor heavily overwritten; the 1 is separate and clearer. | medium |
| 409 | Before (46) | `B'_0 opère trivialt` | The visible word is retained despite the adjoining argument; no mathematical correction made. | medium |
| 409 | Deleted formula before (46) | `\mu_2\subset B'_0` | Inclusion sign obscured by a long cancellation stroke. | low |
| 409 | Before (47) | `s-groupe` | Very abbreviated, possibly « sous-groupe ». | medium |
| 409 | Left of « Reste » | `non!` | The short word consists mainly of a wavy stroke. | medium |
| 409 | Product in final paragraph | `N'_\sigma` deleted, `T_\sigma` inserted | N/T overwrite is visible; the original prime is less secure. | medium |
| 409 | Lower marginal note | `avec \tau^0_{\rho,\sigma}` | The connective is faint near the edge. | medium |
| 410 | Equation (48), lower-left object | `T_0` | The letter is reinforced or overwritten. | medium |
| 410 | Equation (48), lower-left object | `N'_\sigma` deleted, `T_\sigma` inserted | Overwritten N/T and prime. | medium |
| 410 | Immediately after (48), after « sur » | Deleted tau-like symbol | A small cancelled group-letter start precedes the full `\tau^0` on the next line. | low |
| 410 | After « plus généralement, que la » | `portion`, possibly deleted | The first half is crossed or overwritten; the exact cancellation state is uncertain. | low |
| 410 | Final paragraph | `épimorphiquement` | Initial letters overwritten, but the underlined word is mostly legible. | medium |
| 411 | Equation (49), second line | Deleted `Centre` | Dense cancellation over the word before the parenthesized product. | low |
| 411 | Equation (49), tuple | `\lambda` | The letter is heavily retraced; an older letter cannot be securely separated. | medium |
| 411 | Equation (49), determinant condition | Deleted `a`, inserted `det a`; right side `\varepsilon'\lambda^2` | The older left symbol and the final right-side exponent are overwritten. | low |
| 411 | Before (50) | `trivialt` | The final abbreviated strokes are compressed. | medium |
| 411 | Equations (50)–(51) | `ST'_\rho` | Prime placement and thick retracing over S/T; could instead be a prime attached to the prefix S. | low |
| 411 | Equation (50), superscript on `\tau` | `a` or `0` | Small black shape is a-like; no mathematical normalization to the identity-component superscript has been made. | low |
| 411 | Equation (50), final factor | `N'_\sigma` | N is overwritten or reinforced; underlying traces are not independently readable. | medium |
| 411 | Left of second line of (52) | Deleted `Groupe de` | Last letters are crossed by the cancellation rule. | medium |
| 412 | Lines 3 and 5 | `trivialement` | The ending is compressed; an abbreviated ending may have been intended. | medium |
| 412 | End of upper paragraph | Deleted `tau_{rho,sigma}` | The abandoned symbol is overwritten and its subscript is particularly poor. | low |
| 412 | First display | `T_sigma` | The subscript has been overwritten. | medium |
| 412 | First display, determinant condition | Cancelled parentheses and exponent `2` around `det a` | The cancellation is local and heavily overwritten; it is not entirely clear how far its strokes extend. | low |
| 412 | Before equation (53) | `On` | A short detached word to the left of the equation; perhaps `en`. | low |
| 412 | Left middle margin | `Centre est de dim 3` | `est` is compressed to a single joined stroke. | medium |
| 412 | Lower display number | `54` | The first digit can look like `1`; both `54` and `14` are recorded in the transcription. | medium |
| 412 | Cancelled text after the comparison | `(bien que celui-ci` | No closing parenthesis can be identified confidently; the last word is crossed through. | low |
| 412 | Last line | `dévissage` | `discussion`; the shape favours an ending in `-age`, but the long cancellation crosses it. | medium |
| 413 | Introductory paragraph, projective group | `GP(1)` | `PGL(1)`; the ink does not warrant replacing the numeral by 2. | medium |
| 413 | Introductory paragraph, subgroup | `1-paramètre` | The final stroke might mark a plural ending. | medium |
| 413 | Crossed-out word before `additif` | `multiplicatif` | `complet`; the heavy strike obscures most internal letters. | low |
| 413 | Word before the map | `bordé` | `basé`; the letters between the initial b and final é are faint. | low |
| 413 | Generator symbol throughout (1), (3), (6), (8) | `xi` | `varepsilon`; each doubtful occurrence remains marked. | medium |
| 413 | Interlinear symbol below the first map label | Inserted `xi_0` | `varepsilon_0`; its attachment to the preceding map label is uncertain because there is no clear caret. | low |
| 413 | Parenthetic account of the unipotent section | Cancelled `de`; `régulière de xi_0` | Both short marks are difficult; the second appears to be a separate `de`, so it is not silently removed for grammar. | low |
| 413 | Cancelled word before `par les conditions` | `satisfais` | The ending is obscured; it is not expanded to `satisfaisant`. | low |
| 413 | Cancelled symbols before the brace in (3) | `sigma rho` | Perhaps a tilde-rho or a partial initial attempt at the left-hand side. | low |
| 413 | `On construit un ...` | `épinglage` | The middle letters are compressed. | medium |
| 413 | Left of equation (5) | Cancelled `(4)` and `tau_{rho,sigma}=` | The original label and subscript are overwritten. | low |
| 413 | Scalar parameter in (7)–(8) | `v` | Greek `upsilon`; the rounded handwritten form does not settle the alphabet. | medium |
| 413 | Right edge of (7) | Open parenthesis before `v in Gamma G_m` | No closing parenthesis is confidently visible before the frame; none has been supplied. | high |
| 414 | (9), (11) | Generator `xi` | `varepsilon`, as on scan 413. | medium |
| 414 | Right of second row of (9) | `id` | A ditto/idem annotation linked to the parameter condition above; the last letter is unusually angular. | medium |
| 414 | Far right beside (10) | `—` | Isolated horizontal pen stroke; no word is legible there. | low |
| 414 | (11), last row after rho | Opening round parenthesis | An opening brace is also possible; two closing round parentheses are visible. | low |
| 414 | Left of brace in (12) | Deleted `mathcal G_{rho,sigma}` | The initial symbol and subscript have been heavily overwritten. | low |
| 414 | Between the two definitions in (12) | Deleted `de O_S` | The short text before O_S is not secure; the cancellation runs diagonally through it. | low |
| 414 | (11)–(12), scalar parameter | `v` | Greek `upsilon`; continued from scan 413. | medium |
| 415 | Upper left notation list, second line | `tau_{rho,sigma}` | `mathcal G_{rho,sigma}`; the initial letter is overwritten. | low |
| 415 | Upper left notation list, crossed symbol on third line | Deleted `mathcal M_{rho,sigma} circle` | The hatch crosses both the initial letter and superscript. | low |
| 415 | Upper left notation list, last superscript | `circle +` | `circle *`; the added small cross is thick. | medium |
| 415 | (16), ambient group | `mathcal B_{rho,sigma} star` | `mathcal G_{rho,sigma} star`; the upper part has been retraced into a B-like form while a lower loop remains. The chronology of this overwriting is not asserted. | low |
| 415 | Right of (17) | `défini par u = 1` | The underlined u and the numeral 1 are clear enough to retain, despite the apparent tension with the following intersection with T_0. No mathematically motivated replacement is made. | high |
| 415 | (19), second factor | `mathcal M[0)` | `mathcal M(0)`; the left delimiter has a square-looking top while the right delimiter is curved. | medium |
| 415 | (20), initial M | Dotted M | Undecorated M; a short detached mark is visible above the initial upstroke. | low |
| 415 | Below (20), notation line | An opening brace before `g maps to ...` | No matching closing brace is visible; it is not supplied. | medium |
| 415 | Beside epsilon_2 formula | `(cf (13)(14)` | Only the closing parenthesis for 14 is visible at the right edge; no additional final parenthesis is supplied. | medium |
| 415 | Right of (21) | `où` | This is a very short undulating stroke and could instead be an unfinished continuation. | low |
| 415 | Lower left marginal note | `inspirée à tort` | The short words after `inspirée` are compressed. | medium |
| 415 | Lower left marginal note, first subscript | `tau_{g,nu}` | `tau_{g,r}`; the second subscript is less secure here than in the final `Gamma_{g,nu}`. | medium |
| 415 | Lower left marginal note | `la suite montre` | The middle word and final tense ending are compressed. | medium |
| 415 | Above (22) | `et le composé` | The first word is overlapped by the diagonal marginal addition. | low |
| 415 | (23), first letter | `mathcal M` | `mathcal G`; the letter is retraced. | low |
| 415 | (23), tau | Undecorated tau | Tau with a prime; a small detached mark appears above the final subscript. | low |

## Abbreviations met

Expansions are confined to this list. Entries are grouped by the scans on which they were recorded; different punctuation or abbreviated endings have not been silently standardized in the transcription.

### Scan 397

`hom.` / `hom`: homomorphisme; `épi`: épimorphisme (or épimorphique in adjective position); `i.e.`: id est; `cf`: confer / compare; `p.`: page; `déf`: définition; `évidemt`: évidemment (uncertain abbreviation); `trivial` with superscript `mt`: trivialement (uncertain abbreviation).

### Scan 398

`dim`: dimension; `épi`: épimorphisme; `idm` (uncertain): idem.

### Scan 399

`pr₃`: troisième projection. The manuscript writes `1/2 direct`; this is preserved, with its likely meaning “semi-direct” confined to this list.

### Scan 400

`cf`: compare; `p.`: page; `déf`: définition; `compos.` (uncertain): composante.

### Scan 401

`cf`: compare; `p.`: page; `déf`: définition; `NB`: nota bene; `i.e.`: id est; `hom.`: homomorphisme.

### Scans 402–406

| As written | Tentative expansion, only here |
|---|---|
| hom. | homomorphisme(s) |
| etc | et cetera |
| can | canonique |
| Rmq. | Remarque |
| `m̄` | même |
| cf. | confer / comparez |
| p. | page |
| respᵗ | respectivement |
| df | définition / par définition |
| Centr | centre |
| mb | membre (uncertain abbreviation) |

- `autom`: automorphisme.
- `NB`: nota bene.
- `i.e.` (uncertain reading): id est.

### Scans 407–411

| Written form | Possible expansion (only in these notes) |
|---|---|
| `\overline{\mathrm m}` | même |
| `NB` | nota bene |
| `trivialt` | trivialement |
| `hom` / `homo` | homomorphisme (the latter reading is uncertain) |
| `can.` | canonique |
| `autom. int.` | automorphisme intérieur |
| `épim` | épimorphisme |
| `pts.` | points |
| `s-groupe` | sous-groupe |
| `1/2 direct` | semi-direct (written numerically in the margin) |
| `proj` | projection |
| `1ère` | première |
| `suppl.` | supplémentaire |
| `Centr` | Centre |

### Scans 412–415

| As written | Possible expansion (notes only) |
|---|---|
| `ss-groupe` | sous-groupe |
| `dim` | dimension |
| `pts` | points |
| `Rmq.` | Remarque |
| `th.` | théorème |
| `p.` | page |

### scan 413

| As written | Possible expansion (notes only) |
|---|---|
| `m` with overbar | même |
| `i.e.` | id est, c'est-à-dire |
| `Tr` | trace |
| `det` | déterminant |

### scan 414

| As written | Possible expansion (notes only) |
|---|---|
| `id` | idem |
| `iso` | isomorphismes |
| `schém.` | schéma |
| `1/2-direct` | semi-direct |

### scan 415

| As written | Possible expansion (notes only) |
|---|---|
| `dfn` | définition |
| `i.e.` | id est, c'est-à-dire |
| `cf` | confer, comparer |
| `iso` | isomorphisme |
| `1/2-direct` | semi-direct |

## Legibility

Most principal formulas and continuous prose are recoverable at enlargement, but the handwriting frequently compresses word endings, superscripts, and the distinction between similar group letters. The least secure passages are the sloping marginal note on scan 402; the revised centre discussion and crossed lower calculation on 404; the hatched tuple and small overwritten matrix entry on 405; the abandoned notation and prose around (37) on 406; overlapping insertions on 409; and the retraced symbols and cancelled centre formulas on 411–412. On 415, both diagonal margins were inspected separately; the notation list, the ambient letter in (16), and the final symbols in (23) still warrant particular caution.

The fragment contains one `\illegible{1}` for a fully obscured deleted word on scan 407. Other doubtful passages have attempted readings in place. Apparent inconsistencies—including the order numeral beside the square-symmetry description, the differing cyclic factors on scans 407–408, the unfinished intersection on 401, and “défini par u = 1” on 415—have not been repaired by mathematical inference. The marked uncertainties are genuine limitations of this transcription, especially where several correction strokes overlap.

## Research notes — English

These observations are separate from the transcription. “Unproved claim” means that the supporting proof is not supplied in full at the cited location in this packet; it does not assert that the claim is false or unproved elsewhere. Cancelled claims are explicitly identified. Items labeled “own idea” are proposed checks or possible directions, with a confidence assessment and reason; none is asserted to be established or new.

- **Scan 397, after (4)–(7); unproved claim.** “il est … épi” reduces surjectivity of Θ to surjectivity of its determinant composite. The text identifies that composite with the multiplier and then with determinants in two coordinate presentations; a proof would need the precise meanings of epimorphism and the determinant-surjectivity statements over the base S.

- **Scan 397, (8); unpursued implication.** “Définissons” introduces the kernel of χ before a diagram continuing on the next sheet. Tracking how this kernel depends on the chosen presentation is a useful check on subsequent exact sequences; the present page supplies the definition, not an independent base-change argument.

- **Scan 398, paragraph after (9); unproved claim.** “nécessairement plat de dim relative 2” is asserted for the kernel of Θ, followed by the relative dimension 3 of the projective kernel. Verifying this passage requires the hypotheses under which the displayed group morphism is faithfully flat and the corresponding dimension formula applies.

- **Scan 398, final paragraph; conjecture.** “on prévoit qu'il est commutatif” is an explicit expectation about J, which is presented as playing the role of a “radical.” The following toric expectation is conditional and continues on the next page; it should not be quoted as an unconditional proved structure theorem from this sentence.

- **Scan 398, (10)–(11); own idea.** Compare the proposed subgroup filtration with the later coordinate descriptions and distinguish an identity component from the whole projective kernel. **Confidence: medium**, because the page itself calls commutativity an expectation and the next pages alter the approach; this is a proposed consistency check, not a claim of novelty.

- **Scan 399, opening paragraph and (12)–(13); unproved claim.** “par construction du produit 1/2 direct” introduces an embedding into a product and identifies Θ with the third projection. A verification should explicitly check compatibility of the semidirect-product action with the regrouping and then derive, rather than assume, the determinant conditions (13).

- **Scan 399, (14); unproved claim.** “Cela montre que” gives coordinate descriptions of two kernels. The overwritten I/J labels are an editorial obstacle; after resolving them, a proof should distinguish a scalar matrix λ from its determinant λ² and retain the indicated sign conditions over the base.

- **Scan 399, last paragraph; unpursued implication.** “Il me semble plus naturel” changes the proposed approach to beginning with the neutral component. This is a methodological expectation that motivates the following component-group calculation, not itself a proof of connectedness.

- **Scan 400, (15); unproved claim.** The component quotient is identified with μ₂ × μ₂ with the reference “cf p. 489 (23).” Checking the claim requires the earlier referenced construction and a precise convention for the neutral component over S; those earlier pages are outside this packet.

- **Scan 400, (16)–(18); unproved claim.** “Donc le noyau” and “on en déduit” pass from determinant equations to the two kernels. A complete proof should exhibit the proposed isomorphisms as morphisms of group functors, not only match their dimensions.

- **Scan 400, (17); own idea.** Conditional on the reading `det x = det y = λ²`, examine the natural map that forgets λ before accepting the displayed fiber-product identification. **Confidence: high in the diagnostic, conditional on the reading**, because two choices of λ with the same square suggest a possible μ₂ kernel; this is an elementary check prompted by the equation, not a claim that the manuscript's intended morphism has been identified.

- **Scan 401, theorem (19)–(20); unproved claim.** “est extension de μ₂ × μ₂ par” recapitulates the component description as a theorem. Its dependence on the earlier definition, explicitly cited as p. 487′ (20), should be tracked separately from what can be verified from this packet alone.

- **Scan 401, (21) and following exact sequence; unproved claim.** The subgroup is called “central (dans M … tout entier).” Verifying centrality in every component requires the action of the disconnected quotient, not only a calculation in the neutral component.

- **Scan 401, NB between the two boxes; unproved claim.** “J … est encore central” appears in a correction note whose last intersection formula is unfinished. A proof should compare the projective kernel, its intersection with SG, and the multiplication morphism, while preserving the fact that the preceding product expression has been struck out.

- **Scan 401, cancelled passage below (24); unpursued implication.** A proposed inclusion of G in the neutral component is cancelled and annotated, probably “inexistant.” This deserves comparison with the retained inclusion of SG into the neutral component: the page itself rejects the stronger displayed construction.

- **Scan 401, (25); unpursued implication.** “On a un hom. canonique” introduces three μ₂ factors, continuing on the next page. Whether this remains an embedding on all bases and how its three factors sit in the centre are natural questions for the subsequent calculation; the statement here is a homomorphism, so injectivity should not be assumed merely from the drawn hook.

- **Scan 402, (27); unproved claim.** The canonical homomorphisms are said to have been “déjà envisagés par ailleurs.” The relation between the three indicated `mu_2` inclusions and the displayed homomorphism from `(Z/2Z)^3` needs comparison with the earlier construction, including the precise target superscript, which is overwritten here.

- **Scan 402, (30)–(31); unproved claim.** The phrase “un scindage canonique en produit semi-direct” asserts the displayed splitting. A verification should identify the section, check that it is a group morphism, and specify the conjugation action on `SG`; these requirements are research tasks, not corrections to the transcription.

- **Scan 402, marginal note; unpursued implication.** The note appears to distinguish a `Gamma_{rho,sigma}` notation from `tau_{rho,sigma}` and discusses the sign `!`. Its exact wording is too uncertain to support a stronger conclusion, but tracing the notation through later sections would help separate the originally proposed quotient notation from later editorial changes.

- **Scan 403, remark; conjecture / question considered and rejected.** “On aurait envie d'introduire” an extension, with the inserted alternative “(ou produit),” introduces the proposed `tau_{rho,sigma}` and its quotient relation. The author then writes “ce n'est pas possible dans le contexte des schémas en groupes”; the obstruction and the precise category in which the attempted quotient would live deserve a full reconstruction, particularly because the short phrase giving the reason is faint.

- **Scan 403, (33)–(34); unproved claim.** The modular case is said to admit “une section canonique,” represented by the diagonal matrix displayed in (34). Checking membership in the indicated group and the claimed canonicity requires the earlier definitions; the matrix itself is clear.

- **Scan 403, final line, continued on scan 404; conjecture / question.** “Il serait intéressant de voir si, en dehors du” begins a question about extension beyond the modular case. The continuation on the following scan must remain part of the research item; the page boundary does not turn the question into a conclusion.

- **Scan 404, first paragraph and (35); conjecture.** Continuing the preceding page, he asks for “anti-involutions” that “généralisent les réflexions géométriques,” and writes “je suis convaincu que oui.” The three concrete matrices specify the modular model; a general construction would need to state its base hypotheses and show how those matrix symmetries survive without the modular coordinates.

- **Scan 404, middle correction; unpursued implication.** “Mais je me mélange là les pinceaux” explicitly retracts the initial identification of the three reflection sections with the displayed `mu_2` factors in the identity component. The replacement text places the reflections over the “la moins triviale” section `(-1,-1)` of the component quotient; it is worth checking how this changes any proposed common lifting or splitting.

- **Scan 404, deleted centre assertion and inserted `Z` definition; unproved claim.** The cancelled sentence concerns “le centre,” while the connected addition defines `Z_{rho,sigma}` through the centre of the identity component. This is an abandoned or revised argument, not an established theorem on this page; a proof must distinguish the centre of the full group from the centre of its identity component and track the action of other components.

- **Scan 404, deleted calculation after (36); own idea.** Compare the scalar maps `j_rho` and `j_sigma` with the displayed determinant maps to locate the precise obstruction encountered in the cancelled argument. **Confidence: medium as a useful verification task**, because the manuscript explicitly writes the composite `lambda -> lambda^2`; no claim is made here that this supplies the desired reflection sections.

- **Scan 405, middle calculation of the invariants — unproved claim / proof referred to earlier work.** “les calculs déjà faits donnent” introduces alpha, beta, mu and the two signs for tau_infinity, and “attention au signe -” explicitly distinguishes the two Sl expressions he writes. A verification would need the earlier definitions of rho(alpha), the multipliers and the tuple coordinates, while keeping track of this central sign; the present transcription does not infer the uncertain matrix entry from the expected algebra.

- **Scan 405, NB at the foot, continued on scan406 — question.** For a general upper triangular u he asks “quels sont ces invariants alpha,beta etc ?”. The answer must distinguish the automorphism induced on the named group from membership in the smaller subgroup in which the tuple (36) lay; the next page is needed for the actual restriction.

- **Scan 405, tuples (36) and NB — own idea (medium confidence).** Check the proposed coordinates functorially over the precise coefficient rings displayed before specializing to integral points. This is a verification task, not an asserted new result: the NB visibly juxtaposes a hatted Z and an unhatted Z, and the subsequent calculations may specify which point sets are intended.

- **Scan 406, correction immediately following (37) — unproved claim / qualification.** “ce n’est pas un élément sous forme normalisée” is followed by the explicit exception “sauf si lambda=0”. The claim calls for checking the earlier definition of the normalized subgroup against the upper triangular coordinate u; the abandoned 2° and its rewritten version should be kept distinct in any mathematical reconstruction.

- **Scan 406, left marginal NB beside (38) — unproved claim.** The note says that tau_infinity and r_1 “ont mbar image” after reducing modulo L_0, and gives the triple (-1,1,tau_infinity). A proof would compare their two upper triangular matrices modulo that subgroup and verify the quotient coordinate convention, which is not supplied again in the margin.

- **Scan 406, 3° after the reflection matrix — conjecture / expectation.** He writes “ça vaut mieux, si on veut que” the three reflections generate the displayed Gl group, or its primed alternative. This frames generation as the desired compatibility with the fact that the third reflection does not normalize L_0; no proof of generation is given on this page.

- **Scan 406, final paragraph continuing on scan407 — unpursued implication.** The product identity tau_infinity prime = tau_infinity sigma_infinity and the phrase “le deuxième est tautologique” reduce the third reflection’s image to the already computed first image and the canonical SG component. The final sentence begins to assert that it has the same quotient image; its completion lies on the next page.

- **Scans 405–406, comparison of (36)–(38) — own idea (medium confidence).** Explicitly compare the images of all three reflection matrices first in M and then in its quotient by the distinguished SG subgroup. The displayed product identity and the marginal equality of two quotient images make this a useful consistency check, but neither the full quotient identification nor a generation theorem is asserted here as established by this transcription.

- **407, equation (40); kind: unproved claim.** The identification `N'_\sigma(\mathbb Z)\simeq D_4` is accompanied by « symétries du carré » and an order numeral read as 4. The generator relations and the convention for the notation `D_4` should be checked directly; this note does not resolve the possibly inconsistent numeral.

- **407, equation (41); kind: unproved claim.** The manuscript states that « \(\tau_\infty\) opère trivialt sur les deux premiers facteurs et par symétrie sur le dernier ». A verification requires computing conjugation on the displayed generators of the three finite cyclic factors and matching those computations to the written product decomposition.

- **407, marginal NB beside (42); kind: unpursued implication.** The determinant-sign condition is called « automatique » because `\mathbb G_m(\mathbb Z)=\{\pm1\}`. This argument is explicitly about integral points; whether the analogous simplification survives a change of base or a passage from points to group schemes is not established by this marginal observation.

- **408, equations (43)–(44); kind: unproved claim.** The displayed expression is called a « produit semi-direct », with action through the canonical map to `{1,\tau_\infty}`. A proof should identify the chosen section and verify that its conjugation action agrees with the written matrix; the occurrence of a cyclic factor of order 4 here, versus 6 in (42), should be checked without silently harmonizing the text.

- **408, equation (45) and final paragraph; kind: unpursued implication.** The sign map is said to be zero on the cyclic factors and to take the value « \((-1,-1)\) » on `\tau_\infty`. This points toward an image consisting of the diagonal sign subgroup on integral points, an issue the author begins to draw out at the page break.

- **409, opening line; kind: unproved claim.** The preceding discussion concludes « pas surjectif » for the map on integral points. A complete argument should distinguish this failure on global sections from any asserted surjectivity of the underlying group-scheme or sheaf morphism.

- **409, first paragraph and upper marginal correction; kind: unproved claim.** The proposed description of the centre is explicitly challenged by the double-underlined « faux ». The margin says that an element `g.f` of a semidirect product can be central without `g` acting trivially on the invariant group, so the body’s product description must not be treated as an established result.

- **409, equation (46); kind: unproved claim.** The calculation uses `B'_0\cap\mu_2=\{1\}`, with `\mu_2` identified as the « centre de SG ». Verifying the resulting kernel description requires checking the precise embedding and action of `B'_0`, especially because the adjacent abbreviated verb has been read as « opère trivialt » rather than silently corrected.

- **409, final paragraph and lower margin; kind: unpursued implication.** « Reste : déterminer le centre » proposes passing to invariants of the action of `\mu_2\times\mu_2` on `\tau^0`. The lower marginal note limits this to « au moins l'intersection du centre avec \(\tau^0\) », leaving the other components as a separate issue.

- **409, upper marginal correction; kind: own idea.** A useful check is to compute the centre directly in a chosen convention `N\rtimes A`: centrality of `(n,a)` requires both `a(x)=n^{-1}xn` for every `x\in N` and compatibility with every element of `A`. **Confidence: high as a verification strategy**, because these conditions can be derived by multiplying the two orders of a pair; this is an independent suggested calculation, not a claim of novelty or a replacement for the manuscript.

- **410, equation (48) and following paragraph; kind: unproved claim.** The diagram is used to show that the component-group action factors through « son premier facteur », acts trivially on `T_0\times T_\rho`, and acts on `T_\sigma` by `\sigma\mapsto\varepsilon\sigma`. A verification should compare the displayed quotient map and its conjugation action with the earlier definitions, rather than infer the action solely from the form of an exact sequence.

- **410, middle paragraph; kind: unproved claim.** The manuscript says that the invariants in `T_\sigma` are « réduits aux scalaires \(\mathbb G_m\) ». The fixed subgroup should be calculated from the defining equations, with the meaning of invariance kept at the same group-scheme or sheaf level as the rest of the construction.

- **410, final paragraph; kind: unproved claim.** The asserted faithfulness on `\tau'` is justified by the statement that it « s'envoie épimorphiquement sur \(T_\sigma\) ». A complete proof needs the stated epimorphism and the passage from that epimorphism to faithfulness, which are only briefly invoked here.

- **410, fixed-subgroup calculation; kind: own idea.** Test the equations for the fixed subgroup over rings with `2=0` and over rings containing nilpotents before using a computation on geometric points. **Confidence: medium as a useful diagnostic**, because the passage concerns an action of `\mu_2`, and equations that are indistinguishable on a restricted set of points can still differ as functors; no counterexample is asserted.

- **411, equations (49)–(50); kind: unproved claim.** The page summarizes the centre of the companion group and its intersection with `\tau`, then imposes « la restriction suppl. \(u=1\) » for trivial action on `SG`. To verify the resulting subgroup one should compare both the determinant equations and the action kernel with the preceding definitions, keeping the overwritten symbols separate from the mathematical inference.

- **411, equation (51) and adjacent margin; kind: unproved claim.** The proposed description of the full centre is crossed out and corrected by « faux le centre est plus grand ». The subsequent insertion changes « centre » to « groupe », so the finite calculation in (52) should be understood as a calculation for the displayed subgroup, not silently promoted to a calculation of the entire centre.

- **411, equation (52) and lower margin; kind: unpursued implication.** The marginal note states « Ce groupe est en fait contenu dans \(\mathcal M^0_{\rho,\sigma}(\mathbb Z)\) ». This indicates a comparison with the identity component that is distinct from the failed full-centre description; verifying it requires locating the displayed generators in that component.

- **411, paragraph after (52); kind: unproved claim.** The order-three cyclic factor is described as « engendré naturellement par \(-\rho\) », and the remaining elementary abelian factor is identified with the earlier group `\Sigma`. A check should track the embeddings of these factors and the cited passage « (IX) », rather than infer the identification from equal abstract orders.

- **411, final line; kind: conjecture / expectation.** « Plus intéressant serait sans doute le » begins an expectation that continues on the next scan. Its object is not supplied on this page, so the note records the open transition without completing it from context.

- **411, cancelled (51); kind: own idea.** Compare the explicitly computed subgroup with the full centre by solving centrality simultaneously against `SG` and the complementary factor, allowing their induced inner actions to cancel. **Confidence: high as a verification strategy**, because the author’s earlier marginal objection concerns precisely such cancellation in a semidirect product; no corrected centre formula is asserted here.

- **Scan 412, middle left margin — unproved claim.** The correction reads “faux ! Centre [est] de dim 3.” It rejects the adjoining centre calculation; a reconstruction would need to start again from the group definition and identify the central scalar direction, rather than rely on the cancelled displayed decomposition.

- **Scan 412, equation (54) and the paragraph following it — unpursued implication.** The cancelled comparison says “deux fois plus gros” about integral points of centres. This remains worth checking separately from the group-scheme centre, since a comparison of integral points alone does not identify the underlying centre functor; the cancelled status is essential evidence here.

- **Scan 412, final remark — unproved claim (cancelled).** The remark identifies the neutral component as `ST_rho × ST_sigma` and appeals to the earlier “dévissage” on p. 501′. The marginal dimension correction makes this appeal a specific point to re-examine against that earlier argument, rather than a proof supplied on this page.

- **Scan 412 — own idea; confidence: medium.** Recompute the centre in a determinant-constrained product presentation while retaining all scalar variables until the final quotient. The reason for this proposed check is the mismatch between the displayed two-factor neutral centre and the explicit marginal “dim 3”; this is a research suggestion, not an established correction or a claim of novelty.

- **Scan 413, conditions (1)–(3) — unproved claim.** “On définit des relèvements canoniques” asserts that the projective data admit the stated normalized lifts. A proof would need existence, uniqueness, compatibility with base change, and an explanation of the role played by the trace condition and fibrewise independence.

- **Scan 413, (5)–(8) — unproved claim.** “On construit un épinglage” is followed by a matrix normalization of the unipotent element and then matrices for rho and sigma. The text here does not display the construction establishing that this normalization gives a global isomorphism rather than only local coordinates.

- **Scan 413, (1) and (3) — own idea; confidence: medium.** Check carefully how the sign in the lifted relation interacts with passage to the projective group, including fibres of characteristic 2. This is prompted by the visible positive projective relation and negative lifted relation; it is a request for verification, not an asserted inconsistency.

- **Scan 413, (7) — unpursued implication.** The displayed normalization leaves a single invertible scalar parameter (read uncertainly as v/upsilon), with equal determinants. Studying which changes of pinning preserve or modify that parameter could clarify whether it classifies the normalized data or only this presentation.

- **Scan 414, (9)–(11) — own idea; confidence: high.** Distinguish the subgroup L_0 as a set or subgroup scheme from the chosen parameterization by the additive group. The first displayed upper-right entry is lambda, whereas the later chosen parameterization uses lambda/v; since the preceding page requires v to be invertible, rescaling is a plausible explanation worth verifying against the intended notation.

- **Scan 414, (12) — own idea; confidence: high.** Check the loci on the base where the two quadratic algebras are étale: the displayed polynomials have discriminants 1 + 4v and 4v. This direct computation suggests a useful case separation for any later statement treating their unit group schemes as tori; it does not alter the manuscript's more cautious “schém. des unités.”

- **Scan 414, (13)–(14) — unproved claim.** The word “d'où” introduces the exact sequence from the sign normalizer to mu_2. A scheme-level proof should identify its kernel with T_sigma and verify surjectivity as an appropriate sheaf map, including in characteristic 2 where treating mu_2 only through geometric points would lose information.

- **Scan 414, (10) — unpursued implication.** The displayed “produit 1/2-direct” of the upper triangular subgroup specifies a natural action of T_0 on L_0. Writing that action in the parameterization fixed in (11) would make later quotient and splitting formulas directly checkable.

- **Scan 415, (17)–(19) — unproved claim.** The page asserts a “produit 1/2-direct” and identifies the complement through intersection with `T_0 × T_rho × N'_sigma`. Proving this directly from the determinant-constrained triple description would identify the group action and establish the claimed decomposition without relying only on the notation.

- **Scan 415, (17) — own idea; confidence: high as a proposed check, not as a correction.** Compare the literal “défini par u = 1” with the immediately following intersection with T_0 and with the later quotient isomorphism. These three statements create a concrete verification target: determine precisely which coordinate the normalization fixes. The manuscript wording is preserved in the transcription, and no corrected formula is asserted here.

- **Scan 415, (20)–(23) — unproved claim.** “Trivial sur L_0” and “est un iso” assert descent of the three characters and an isomorphism from the chosen complement to the quotient. A scheme-level verification can be made by checking the formulas on test schemes, the normality of L_0, and the compatibility of the quotient and complement maps; those checks are not written out here.

- **Scan 415, lower left marginal note — unpursued implication.** “Cette notation n'est pas du tout adéquate” proposes Gamma rather than tau, with references to `Gamma_{g,nu}` and `Gamma_{0,3}`. The note explicitly signals an intended analogy whose structural scope is not developed on this final page. Tracking which operations or exact sequences survive that analogy would be more informative than treating it solely as a change of letter.

## Occurrence index of in-place doubts

This is a locator index, not a second confidence assessment. The preceding table gives the reading assessments and groups repeated uncertainties. The line column below is the physical line of the delivered `.tex` file, not a claimed line number in the manuscript. Arguments are shown as LaTeX so that every uncertainty can be found without losing the letter shape, superscript, or editorial nesting.

| Scan | Fragment line | Macro | Argument as transcribed |
|---|---|---|---|
| 397 | 6 | `unsure` | `\mathcal A` |
| 397 | 10 | `unsure` | `évidemt` |
| 397 | 11 | `unsure` | `trivial\textsuperscript{mt}` |
| 397 | 26 | `unsure` | `\flat\|\sharp` |
| 397 | 27 | `unsure` | `\infty` |
| 397 | 29 | `unsure` | `\flat\|\sharp` |
| 397 | 37 | `unsure` | `\flat\|\sharp` |
| 397 | 38 | `unsure` | `\mathbb G_m` |
| 397 | 51 | `unsure` | `\flat\|\sharp` |
| 398 | 82 | `unsure` | `\det` |
| 398 | 83 | `unsure` | `SLG` |
| 398 | 90 | `unsure` | `idm\|idem` |
| 398 | 92 | `unsure` | `Notons` |
| 398 | 106 | `unsure` | `1` |
| 398 | 126 | `unsure` | `toriques\|torique` |
| 399 | 134 | `unsure` | `déductions\|directions` |
| 399 | 167 | `unsure` | `J` |
| 399 | 170 | `unsure` | `x` |
| 399 | 172 | `unsure` | `J\|I` |
| 399 | 172 | `unsure` | `\sigma\|x` |
| 399 | 173 | `unsure` | `\flat\|\sharp` |
| 399 | 178 | `unsure` | `dévissage` |
| 400 | 188 | `unsure` | `compos.` |
| 400 | 205 | `unsure` | `\sigma\|\rho` |
| 400 | 235 | `unsure` | `\lambda^2` |
| 400 | 236 | `unsure` | `\simeq T_\rho\times_{\mathbb G_m}T_\sigma` |
| 400 | 239 | `unsure` | `*` |
| 401 | 284 | `unsure` | `(0)` |
| 401 | 289 | `unsure` | `on` |
| 401 | 290 | `unsure` | `a deux` |
| 401 | 303 | `unsure` | `(22)` |
| 401 | 303 | `unsure` | `(21)\|(22)` |
| 401 | 313 | `unsure` | `donc` |
| 401 | 314 | `unsure` | `extension` |
| 401 | 318 | `unsure` | `\times\|\mathbin{.}` |
| 401 | 342 | `unsure` | `\}` |
| 401 | 344 | `unsure` | `utilisant` |
| 401 | 346 | `unsure` | `inexistant` |
| 401 | 350 | `unsure` | `\longrightarrow` |
| 402 | 379 | `unsure` | `envisagés` |
| 402 | 383 | `unsure` | `+` |
| 402 | 384 | `unsure` | `+\|*` |
| 402 | 390 | `unsure` | `\mathcal M` |
| 402 | 394 | `unsure` | `paraphrase` |
| 402 | 400 | `unsure` | `Vu un peu traîner` |
| 402 | 400 | `unsure` | `qui` |
| 402 | 400 | `unsure` | `est tombé au loin` |
| 402 | 400 | `unsure` | `même dans la suite suivant I` |
| 402 | 400 | `unsure` | `dans l'expression !` |
| 402 | 400 | `unsure` | `noter` |
| 403 | 427 | `unsure` | `45\|46` |
| 403 | 429 | `unsure` | `connexe` |
| 403 | 429 | `unsure` | `relativement` |
| 403 | 432 | `unsure` | `\dot\tau\|\dot t` |
| 403 | 432 | `unsure` | `\dot\tau_\infty\|\dot t_\infty` |
| 403 | 434 | `unsure` | `\mathcal M` |
| 404 | 451 | `unsure` | `\tau` |
| 404 | 451 | `unsure` | `0` |
| 404 | 458 | `unsure` | `comportant` |
| 404 | 458 | `unsure` | `involutives` |
| 404 | 459 | `unsure` | `isomorphe à` |
| 404 | 477 | `unsure` | ```injectifs''` |
| 404 | 484 | `unsure` | `la composée` |
| 404 | 484 | `unsure` | `mb` |
| 405 | 488 | `unsure` | `centralité triviale` |
| 405 | 489 | `unsure` | `\mathbb G_m\times` |
| 405 | 492 | `unsure` | `T_\rho` |
| 405 | 500 | `unsure` | `T'_0\|B'_0` |
| 405 | 500 | `unsure` | `resp. $\varphi$` |
| 405 | 500 | `unsure` | `Le` |
| 405 | 502 | `unsure` | `i.e.` |
| 405 | 506 | `unsure` | `(\ast)` |
| 405 | 512 | `unsure` | `etc.` |
| 405 | 512 | `unsure` | `on trouve` |
| 405 | 512 | `unsure` | `nous` |
| 405 | 515 | `unsure` | `\zeta\|\xi` |
| 405 | 523 | `unsure` | `\varepsilon_3(\mu)\|\varepsilon_3^b(\mu)` |
| 405 | 530 | `unsure` | `\mu` |
| 405 | 530 | `unsure` | `\mu D\|\mu B` |
| 405 | 543 | `unsure` | `(\underline u_\infty=-1,\underline a_\infty=1,\underline b_\infty=\tau_\infty)` |
| 405 | 552 | `unsure` | `\mathrm{Gl}` |
| 405 | 554 | `unsure` | `\simeq` |
| 406 | 563 | `unsure` | `\tau_\infty` |
| 406 | 577 | `unsure` | `\widehat{\mathbb Z}\|\mathbb Z` |
| 406 | 578 | `unsure` | `\mathcal M` |
| 406 | 578 | `unsure` | `S\mathcal G\|\mathcal G` |
| 406 | 578 | `unsure` | `0` |
| 406 | 583 | `unsure` | `appliquer le` |
| 406 | 585 | `unsure` | `paragraphe précédent\|raisonnement précédent` |
| 406 | 585 | `unsure` | `normalisée` |
| 406 | 585 | `unsure` | `nous` |
| 406 | 585 | `unsure` | `On aura` |
| 406 | 587 | `unsure` | `les remarques précédentes` |
| 406 | 590 | `unsure` | `r_1\|\tau_1` |
| 406 | 594 | `unsure` | `réduisant` |
| 406 | 596 | `unsure` | `=\|\simeq` |
| 406 | 596 | `unsure` | `\widehat{\widetilde G}_{0,3}^{+}\|\widetilde G_{0,3}^{+\wedge}` |
| 406 | 598 | `unsure` | `comme` |
| 406 | 598 | `unsure` | `\tau'_\infty` |
| 407 | 602 | `unsure` | `504` |
| 407 | 604 | `illegible` | `1` |
| 407 | 628 | `unsure` | `dihédral` |
| 407 | 628 | `unsure` | `4` |
| 407 | 636 | `unsure` | `groupe engendré` |
| 407 | 639 | `unsure` | `trivialt` |
| 407 | 642 | `unsure` | `\downarrow` |
| 407 | 650 | `unsure` | `[0]` |
| 407 | 655 | `unsure` | `flèche précisée par` |
| 407 | 658 | `unsure` | `\mathcal M` |
| 408 | 668 | `unsure` | `donc` |
| 408 | 689 | `unsure` | `autom. int.` |
| 408 | 695 | `unsure` | `épim` |
| 408 | 699 | `unsure` | `\deleted{se factorise}` |
| 408 | 699 | `unsure` | `homo` |
| 408 | 704 | `unsure` | `4` |
| 408 | 708 | `unsure` | `\det a` |
| 408 | 708 | `unsure` | `notera` |
| 409 | 715 | `unsure` | `du le` |
| 409 | 715 | `unsure` | `trivialt` |
| 409 | 715 | `unsure` | `points` |
| 409 | 715 | `unsure` | `fixes` |
| 409 | 715 | `unsure` | `invariants` |
| 409 | 715 | `unsure` | `en est de même` |
| 409 | 715 | `unsure` | `trivialement` |
| 409 | 717 | `unsure` | `trivialt` |
| 409 | 717 | `unsure` | `invariant` |
| 409 | 717 | `unsure` | `G` |
| 409 | 726 | `unsure` | `\mu_2` |
| 409 | 726 | `unsure` | `trivialt` |
| 409 | 726 | `unsure` | `\subset` |
| 409 | 730 | `unsure` | `s-groupe` |
| 409 | 736 | `unsure` | `non!` |
| 409 | 737 | `unsure` | `N'_\sigma` |
| 409 | 738 | `unsure` | `avec` |
| 410 | 755 | `unsure` | `T_0` |
| 410 | 755 | `unsure` | `N'_\sigma` |
| 410 | 759 | `unsure` | `\tau` |
| 410 | 759 | `unsure` | `\deleted{portion}` |
| 410 | 766 | `unsure` | `épimorphiquement` |
| 411 | 783 | `unsure` | `\mathrm{Centre}` |
| 411 | 787 | `unsure` | `\lambda` |
| 411 | 788 | `unsure` | `\underline a` |
| 411 | 788 | `unsure` | `\lambda^2` |
| 411 | 792 | `unsure` | `trivialt` |
| 411 | 797 | `unsure` | `ST'_\rho` |
| 411 | 797 | `unsure` | `a\|0` |
| 411 | 797 | `unsure` | `N'_\sigma` |
| 411 | 798 | `unsure` | `ST'_\rho` |
| 411 | 807 | `unsure` | `ST'_\rho` |
| 411 | 820 | `unsure` | `Groupe de` |
| 412 | 831 | `unsure` | `trivialement` |
| 412 | 831 | `unsure` | `trivialement` |
| 412 | 831 | `unsure` | `\tau_{\rho,\sigma}` |
| 412 | 837 | `unsure` | `T_\sigma` |
| 412 | 839 | `unsure` | `2` |
| 412 | 847 | `unsure` | `On` |
| 412 | 855 | `unsure` | `est` |
| 412 | 860 | `unsure` | `54\|14` |
| 412 | 866 | `unsure` | `\mathcal{M}_{\rho,\sigma}` |
| 412 | 866 | `unsure` | `bien que celui-ci` |
| 412 | 868 | `unsure` | `dévissage\|discussion` |
| 413 | 879 | `unsure` | `\mathrm{GP}(1)\|\mathrm{PGl}(1)` |
| 413 | 879 | `unsure` | `1-paramètre` |
| 413 | 879 | `unsure` | `multiplicatif\|complet` |
| 413 | 879 | `unsure` | `bordé\|basé` |
| 413 | 881 | `unsure` | `\xi\|\varepsilon` |
| 413 | 883 | `unsure` | `\xi_0\|\varepsilon_0` |
| 413 | 884 | `unsure` | `de` |
| 413 | 884 | `unsure` | `de` |
| 413 | 884 | `unsure` | `\xi_0\|\varepsilon_0` |
| 413 | 888 | `unsure` | `\xi\|\varepsilon` |
| 413 | 889 | `unsure` | `\xi\|\varepsilon` |
| 413 | 890 | `unsure` | `\xi\|\varepsilon` |
| 413 | 891 | `unsure` | `\xi\|\varepsilon` |
| 413 | 892 | `unsure` | `\xi\|\varepsilon` |
| 413 | 900 | `unsure` | `satisfais` |
| 413 | 902 | `unsure` | `\sigma\rho` |
| 413 | 904 | `unsure` | `\xi_0\|\varepsilon_0` |
| 413 | 905 | `unsure` | `\xi_1\|\varepsilon_1` |
| 413 | 912 | `unsure` | `épinglage` |
| 413 | 914 | `unsure` | `4` |
| 413 | 914 | `unsure` | `\tau_{\rho,\sigma}` |
| 413 | 917 | `unsure` | `\xi_1\|\varepsilon_1` |
| 413 | 919 | `unsure` | `\xi_1\|\varepsilon_1` |
| 413 | 925 | `unsure` | `v\|\upsilon` |
| 413 | 926 | `unsure` | `v\|\upsilon` |
| 413 | 927 | `unsure` | `v\|\upsilon` |
| 413 | 928 | `unsure` | `v\|\upsilon` |
| 413 | 932 | `unsure` | `\xi_0\|\varepsilon_0` |
| 413 | 933 | `unsure` | `v\|\upsilon` |
| 414 | 943 | `unsure` | `\xi\|\varepsilon` |
| 414 | 947 | `unsure` | `\xi\|\varepsilon` |
| 414 | 949 | `unsure` | `\text{id}` |
| 414 | 960 | `unsure` | `---` |
| 414 | 966 | `unsure` | `\xi\|\varepsilon` |
| 414 | 967 | `unsure` | `\xi_0\|\varepsilon_0` |
| 414 | 968 | `unsure` | `v\|\upsilon` |
| 414 | 969 | `unsure` | `\xi\|\varepsilon` |
| 414 | 970 | `unsure` | `\xi_1\|\varepsilon_1` |
| 414 | 973 | `unsure` | `\xi\|\varepsilon` |
| 414 | 974 | `unsure` | `(\,\|\{\,` |
| 414 | 974 | `unsure` | `\xi_0\|\varepsilon_0` |
| 414 | 975 | `unsure` | `\xi_0\|\varepsilon_0` |
| 414 | 981 | `unsure` | `\mathcal{G}_{\rho,\sigma}` |
| 414 | 985 | `unsure` | `v\|\upsilon` |
| 414 | 986 | `unsure` | `de` |
| 414 | 989 | `unsure` | `v\|\upsilon` |
| 415 | 1017 | `unsure` | `\tau_{\rho,\sigma}\|\mathcal G_{\rho,\sigma}` |
| 415 | 1019 | `unsure` | `\mathcal M_{\rho,\sigma}^{\circ}` |
| 415 | 1020 | `unsure` | `+\|*` |
| 415 | 1027 | `unsure` | `\mathcal B_{\rho,\sigma}^{*}\|\mathcal G_{\rho,\sigma}^{*}` |
| 415 | 1051 | `unsure` | `[0)\|(0)` |
| 415 | 1057 | `unsure` | `\dot{\mathcal M}\|\mathcal M` |
| 415 | 1078 | `unsure` | `où` |
| 415 | 1080 | `unsure` | `inspirée à tort` |
| 415 | 1080 | `unsure` | `\nu\|r` |
| 415 | 1080 | `unsure` | `la suite montre` |
| 415 | 1082 | `unsure` | `et` |
| 415 | 1089 | `unsure` | `\mathcal M\|\mathcal G` |
| 415 | 1090 | `unsure` | `\tau_{\rho,\sigma}\|\tau_{\rho,\sigma}'` |

## Inventory and technical verification

The inventory records **458 elements** across all 19 scans. Every row is marked `yes`, meaning that the inventoried element is represented in the transcription, including local uncertainty when necessary; this is not a claim that every reading is certain. Element identifiers are local to each scan.

| Scan | Inventoried elements |
|---|---:|
| 397 | 23 |
| 398 | 14 |
| 399 | 15 |
| 400 | 16 |
| 401 | 37 |
| 402 | 18 |
| 403 | 13 |
| 404 | 26 |
| 405 | 39 |
| 406 | 33 |
| 407 | 27 |
| 408 | 23 |
| 409 | 29 |
| 410 | 21 |
| 411 | 23 |
| 412 | 23 |
| 413 | 27 |
| 414 | 21 |
| 415 | 30 |

The fragment was checked for the complete ordered scan sequence, balanced braces and environments, permitted editorial macro names, and valid diagram syntax. A separate temporary preamble was used to compile it; that preamble and its proof PDF are not part of the requested deliverable. Compilation verifies LaTeX syntax, not the accuracy of a manuscript reading or the validity of its mathematics.
