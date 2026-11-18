# Reading doubts

## Package notation table

This table records the single reader's decisions, reconciled against the images before the transcription was frozen. Differences that belong to the ink are retained; an unresolved difference is marked in place, not silently standardized. Scan numbers below are archive PDF scan numbers, not the author's pagination.

| Recurring ink / convention | LaTeX transcription | Evidence and limits |
|---|---|---|
| Double quotation marks | Two backticks and two apostrophes | Used for the visible double quotes, including “hensélien,” “point marqué,” “S réduit,” and the cover's “Vrai”; no conversion to guillemets. |
| Prime, double prime, triple prime | `'`, `''`, `^{\prime\prime\prime}` | Checked separately on group, ring, point and diagram symbols; triple-prime notation occurs in the rotated scan 131 diagram. A prime is not substituted for an exclamation exponent. |
| Exclamation mark | Literal `!` in prose | No secure exclamation-mark exponent was identified in this package. `\!` in `>\!` is only a LaTeX spacing command, not a manuscript exclamation mark. |
| Angular two-stem homotopy-group sign | `\unsure{\Pi|\pi}` on 096, 098, 100, 107 | These occurrences were visually compared with 105 and 129. The angular outline favors capital Pi, but case is not secure in the rapid hand; the same explicit alternative is used throughout these four sheets. |
| Clearly tall Pi and underlined Pi | `\Pi_2`, `\Pi_1`, `\underline\Pi_1` | The clearer signs on 105 and 129 remain capital Pi. The underlining of the relative/system-local objects on 129 is retained separately from the un-underlined product and abelian-variety formulas. |
| Tame qualification | Superscript `^t`, subscript `_t`, or word `\mathrm{tame}` | The positions vary between 096–098 and 100 and were not unified. |
| Roots-of-unity notation | `\mu`, `\mu_{n_i}`, `\mu_{\underline n}`, `\mu_t^\infty` | Indices, base subscripts and the infinity sign are retained as they occur. The ambiguous first insertion on 096 remains unsure. |
| Tuple of exponents | `\underline n=(n_1,\ldots,n_r)` | Underlining, rather than a supplied vector arrow, is used in 101 and 103. A few single n occurrences differ in the source and are not automatically changed to underlined n. |
| Ambient script X | `\mathcal X` | Distinguished from ordinary X in 096–098 and from the neighborhood model in 135; it is not read as a Greek letter. |
| Structure-ring letters | `\underline{O}`, `\mathrm O`, `\mathcal O` | Underlined typed O in 095/101/103, upright typed O in 106/107, and script handwritten O in 131/135 are preserved as distinct graphic forms. |
| Base points and their conjugates | `\xi`, `\bar\xi`, `\xi_i`, `\xi_i^0`, `\xi'` | Angular xi and its bars were checked in 096–103, 117, 133 and 138–140. Retraced indices and cancelled points carry local doubt marks. |
| Torsor-pair labels | `(P,\xi)`, `(Q,\eta)`, `(R,\lambda)` | The three pairs are kept distinct in 138–140. No closing argument is added after the fibre-product opening on 140. |
| Gamma versus script letters | `\Gamma`, `\mathcal F`, `\mathcal K` | Gamma in extensions and constant groups is not conflated with the script F/K pen samples on 105. The difficult K sample remains unsure. |
| Inertia bars | `I_i`, `\bar I_i`, `\bar I` | Insertions and replacements of barred for unbarred symbols on 103 are recorded explicitly; the remaining unbarred I in a displayed expression is not repaired from context. |
| Tilde | `\widetilde X`, `\widetilde D`, `\widetilde K` | Covers, pulled-back divisors and fields are kept distinct. An uncertain subscript 1 on 101 remains marked. |
| Completion hats | `\widehat A`, `\widehat X`, `\widehat{\mathbf Z}` | Scans 104, 107 and 111; the hat on the opening Tate expression in 104 is uncertain. Scan 107 has a literal square exponent on the completed integer group. |
| Roman versus Gothic ideal/prime letters | `p` with `\mathfrak p` alternative where needed | The heavily written completed-ring subscripts in 107 do not securely distinguish these alphabets. No global conversion to Gothic is made. |
| Pointed-torsor functor glyph | `\mathcal Z` with local `\unsure` | In 139 the definition favors superscript 0 over 1, the proposition source has a 1-like stroke, and its target has no distinct superscript. The overwritten target glyph and the replacement a are recorded, rather than forcing one formula everywhere. |
| Infinitesimal, separable and reduced indices | `\mathrm{inf}`, `\text{sép}`, `\text{réd}` | Typed indices on 126 and the small handwritten reduced index on 138 were checked independently. The candidate U/H in 137 remains unsure. |
| Bold lettering and pen samples | `\mathbf T`, `\mathbf E_i`, `\mathbf G_i`, etc. | The inverted samples on 105 are reproduced in their relative positions, including cancelled glyphs; they are not expanded into a mathematical assertion. |
| Underlining in prose / notation | `\uline`, `\uuline`, `\underline` | Single and double rules are distinguished; scan 131's uncertain marginal word has two underlines. Heavy single rules are not automatically counted as double. |
| Plain connector without a visible head | `\arrow[...,no head]`, `\arrow[...,dash]`, or `\unsure{-|\to}` | No direction is supplied just because the mathematics suggests one. The lowest strokes of the two triple connectors in 131 have no distinct head. |
| Blank typescript connector slot | `\quad` or a phantom labelled connector | Scans 095 and 097 have gaps where no connector ink is recoverable. Their absent arrows are not reconstructed from published text. |
| Isomorphism / equality / word “même” | `\simeq`, `=`, or the literal word | The author's use of `=` inside French prose, notably 104, 131 and 138, is preserved instead of being expanded to “même.” |
| Ordinary multiplication / contracted products | `\times`, `\times_G`, `\mathbin{\times}^{\Gamma}` | Subscript versus superscript placement follows each formula. The anomalous final formula on 138 is transcribed literally. |
| Author numbering versus foliation | `\mspage{5}`, `{6}`, `{2}`, `{5}`, `{6}` on 096, 098, 126, 129, 130 | Archive corner foliation is only a TeX comment. Circled section numbers on 100/101/103 and typed I-6 on 132 are not promoted to manuscript page numbers. |
| Cancellation, insertion and page state | `\deleted`, `\inserted`, `\margin` | Repeated deletions are retained, including nested deletions in an already cancelled passage. The wholly crossed scan 104 is a cancelled draft, not automatically a refuted theorem. |

## Doubts by page

Confidence concerns the reading, not the truth of a mathematical statement. High-confidence rows document a surprising literal reading or a deliberate non-restoration. Audit additions are grouped with their page; where an audit replaced a first-pass reading, the final reading is stated explicitly.

| Cote | Scan | Approximate line / place | Reading | Alternatives | Confidence |
|---|---|---|---|---|---|
| 29 | 95 | above Soit in Cor. 3.2 | en | Misplaced typed correction; attachment unclear | low |
| 29 | 95 | all blank mathematical connectors | Visible gaps retained as spaces / phantom arrows | No connector strokes can be read; no direction supplied | low |
| 29 | 95 | proof a), first deletion | libre sur | libre; overtyping conceals the last strokes | medium |
| 29 | 95 | proof a), second deletion | tout système de représentants | Overtyped letters | medium |
| 29 | 95 | proof b), deletion | posant | pesant | medium |
| 29 | 95 | Cor. 3.3 last sentence | de G'' dans Ker u' | The printed double prime is retained despite mathematical tension | high |
| 29 | 96 | opening paragraph | la théorie; revêtement | le théorie; extension; very rapid pen, with the article and noun both uncertain | medium |
| 29 | 96 | opening paragraph, fourth line | groupe d'inertie de Galois; égal au | Second phrase particularly compressed; the audit replaces the first-pass son reading | low |
| 29 | 96 | insertion beside J_0 | mu_t^infty | Terminal index / flourish is uncertain | low |
| 29 | 96 | right margin | beta^0; beta^i; partial simeq K^ab | Right edge is cut; superscripts unclear | low |
| 29 | 96 | exact sequence and later occurrences | calligraphic X; xi-bar | Script X and angular xi retained consistently | medium |
| 29 | 96 | H^2 argument, deletion | -D_0 | Overwritten superscript or prime after D_0 | low |
| 29 | 96 | lower paragraph | exactement; n | compressed word after correspond; coefficient may be another letter | low |
| 29 | 96 | lower right deletion | En tout cas | Ends are crossed out | low |
| 29 | 96 | bottom-left deletion | illegible, estimated two words | Heavy overstriking remains unreadable at enlarged view | low |
| 29 | 96 | last formula | xi-bar_1; X_0-D_0 | Subscript overwritten; D_0 has no clearly visible prime | medium |
| 29 | 96 | after J_0 in opening paragraph | égal au | second reading recovers two compressed words previously taken as son | medium |
| 29 | 96 | opening noun after un | revêtement / extension | letter sequence remains uncertain in enlarged top crop | low |
| 29 | 96 | recurring handwritten homotopy-group sign | Π | π; angular two-stem handwriting does not securely distinguish typographic case; reconciled consistently across 096, 098, 100 and 107 | medium |
| 29 | 97 | b), final quotient | G/G prime | An extra overtyped mark appears before the prime | medium |
| 29 | 97 | c), initial deletion | Par suite (image) | Last parenthetical word heavily overtyped | low |
| 29 | 97 | c), deletion after quasi-compact | et | Several cancellation x strokes | low |
| 29 | 97 | proof, deletions | définis par; définis | Overtyped, especially first phrase | medium |
| 29 | 97 | Remarques, first deletion | ainsi que | Heavy cancellation | low |
| 29 | 97 | Remarques, second deletion | affirmant que si G=D_S | Last symbols partly overtyped | low |
| 29 | 97 | all homomorphism and factorization gaps | Spaces and phantom connectors retained | No visible arrow strokes in this carbon copy | high |
| 29 | 98 | upper cancelled formula | plain X | Overwritten central letter | medium |
| 29 | 98 | outlined marginal note | puisque; tous / toutes | Opening word and agreement compressed | low |
| 29 | 98 | deletion before Si | Le pb de | Abbreviation pb and last word crossed | medium |
| 29 | 98 | arithmetic paragraph after classes | sans doute; n'est en général pas | Very compressed phrase; negation needs further comparison | low |
| 29 | 98 | arithmetic paragraph, cancelled word | vraiment | Last strokes overstruck | low |
| 29 | 98 | inserted product | (Z/ell Z)^* | No real/infinite-place qualifier supplied by the manuscript here | high |
| 29 | 98 | final product | mu^infty(ell)_{X_0} | The parenthesized letter resembles ell | medium |
| 29 | 98 | recurring handwritten homotopy-group sign | Π | π; angular two-stem handwriting does not securely distinguish typographic case; reconciled consistently across 096, 098, 100 and 107 | medium |
| 29 | 99 | Cor. 3.5, deleted fragment | sché | Only the start of the abandoned word is visible | medium |
| 29 | 99 | Cor. 3.5, subgroup letter | H | G, as in the later displayed equality; no silent normalization | low |
| 29 | 99 | Cor. 3.5 proof, left subscript | n | m-shaped typewriter glyph | medium |
| 29 | 99 | section 4, definition transition | Par définition, un S-préschéma Rappelons qu'un | The abandoned clause has no visible cancellation; retained live | high |
| 29 | 99 | morphism gaps | G [space] G; S prime [space] U | No connector strokes visible | high |
| 29 | 100 | cancelled square, object arguments | xi-bar | Heavy overstriking prevents identification; best symbol reading | low |
| 29 | 100 | X hypothesis | n.th. | noeth.; preserve the shorter visible abbreviation | medium |
| 29 | 100 | divisor and component letters | D, D_i; Y_i in parenthesis | D/Y distinction in the overwritten large letters is uncertain | low |
| 29 | 100 | henselian insertion | pour; l'image inverse; pi_0(Z prime) | Very small marginal revision at right edge; cancelled phrases overlap | low |
| 29 | 100 | U definition deletion | supp | support abbreviated; final stroke uncertain | low |
| 29 | 100 | statement b), relatif | colon / à | Two dot-like strokes favor a colon; final transcription places colon first | medium |
| 29 | 100 | statement b), deleted symbols and phrase | de pi_1(U),xi; on a; xi before product | Heavy local cancellation | low |
| 29 | 100 | product subscript | D_i, replacing Z | Component letter partly overwritten | medium |
| 29 | 100 | statement c), map separator | plain dash | Arrowhead not clearly visible | medium |
| 29 | 100 | proof b), qualifiers | fini (deleted); normal; irred | compressed and overwritten words | low |
| 29 | 100 | proof b), I | I without subscript | No clearly visible subscript on Il faut prouver que I | medium |
| 29 | 100 | proof c), deletion | Et. | Overwritten abbreviation | low |
| 29 | 100 | relatif connector in b) | : / à | second enlarged reading favors the literal two-dot colon | medium |
| 29 | 100 | recurring handwritten homotopy-group sign | Π | π; angular two-stem handwriting does not securely distinguish typographic case; reconciled consistently across 096, 098, 100 and 107 | medium |
| 29 | 101 | X tilde subscripts throughout | 1 | Several 1-like strokes are overwritten or could be deleted subscripts | low |
| 29 | 101 | extension connectors | plain dashes after mu | No arrowheads visible on these three connectors | high |
| 29 | 101 | condition b), X prime | slash before sur X | May be a correction/leader stroke rather than division | low |
| 29 | 101 | condition b), inserted exponent | d'exposant n_i | Exposant compressed | medium |
| 29 | 101 | condition b squared, deleted ending | défini par | Heavy crossing | low |
| 29 | 101 | left-margin topos diagram | B_Gamma/(X tilde,G) | The final group and B subscript are overwritten; topology retained | low |
| 29 | 101 | cohomology, coefficient subscript | mu_n | Underlining of n not visible here although vector n was underlined above | medium |
| 29 | 101 | cohomology quotient denominator | Gamma | Overwritten letter may be G | low |
| 29 | 101 | desired conclusion introduction | si | Could be a short unfinished word or punctuation | low |
| 29 | 101 | under Chern class formula | one cancelled word unreadable | Crosshatching hides it even enlarged | low |
| 29 | 101 | torseur insertion and X | qui au Gamma-torseur X | Phrase unfinished as written; no missing verb supplied | medium |
| 29 | 103 | title hypothesis | loc. intègre | Final word compressed; not silently replaced with noetherian | medium |
| 29 | 103 | divisor line | D_i; intègres; deleted réunis | Suffixes and abandoned word uncertain | low |
| 29 | 103 | cover hypothesis, deleted word | plat | Crossed almost completely | low |
| 29 | 103 | inertia conditions | chacun des; soient; points de | Many revisions; these phrases remain provisional | low |
| 29 | 103 | extension sequence ending | 1-1 | Two distinct 1-like strokes and a dash retained | low |
| 29 | 103 | cancelled line under extension | isomorphe au produit des mu(n_i) | Faint under a long horizontal strike | low |
| 29 | 103 | quotient cover | bar I with a-like lower stroke | Could be a crossed subscript or a correction stroke | low |
| 29 | 103 | extension class paragraph | de alpha; D prime deleted; Or | Small and overlapping words | low |
| 29 | 103 | canonical isomorphisms | I versus bar I; n / vector n | Overwritten formulas retain each visible bar/underline separately | low |
| 29 | 103 | Kummer-property sentence | en le; par fibres; deleted pareil | The clause is syntactically incomplete; no connective supplied | low |
| 29 | 103 | boxed note | au-dessus d'un pt gén. D_i | Small words partly crossed by the outline | low |
| 29 | 103 | boxed note top line | On peut supposer treated as deleted | Outline runs through these words; cancellation status uncertain | low |
| 29 | 104 | top parenthesis | hat on Z_l | possibly plain Z_l; small mark above Z is indistinct | medium |
| 29 | 104 | lemma opening | d’un vectoriel E | no separate espace is visible; E is inserted | high |
| 29 | 104 | proof opening | L’ens; c-à-d vues | very compressed abbreviations; not expanded | low |
| 29 | 104 | proof cancellation after étant le | même, et | crossed letters uncertain; following equals sign preserved literally | low |
| 29 | 104 | proof insertion | deleted finie, then Φ | first inserted word crossed through | medium |
| 29 | 104 | bottom inequality | N′ > N″ | relation is heavily retraced; ≥ possible | medium |
| 29 | 105 | with M, cancelled words | faisceau de; constant | faint pencil crossed by horizontal lines | low |
| 29 | 105 | annotation beneath X tilde | pointé | possibly ponctué; compressed central strokes | medium |
| 29 | 105 | pen samples, upside-down bottom | T(E₁,…,E_n), X, K, F, K | letter styles approximated; heavily inked small shapes marked unsure | medium |
| 29 | 105 | pen samples, small indices | p₁, p_n; deleted π | small upper shape may be a different letter or pen test | low |
| 29 | 105 | cohomology-functor connector | wavy arrow / mapsto | pencil stroke is wavy and the usual mapsto initial bar is not clear | medium |
| 29 | 106 | typeset header, handwritten number | 878 | attribution of pencilled pagination uncertain; reproduced in header, not treated as manuscript foliation | medium |
| 29 | 106 | two heavy typescript overstrikes | one unreadable word in each place | no recoverable letters at highest zoom | low |
| 29 | 106 | proof overstrike before X=Spec(C) | X=Spec | letters beneath x-overtyping uncertain | low |
| 29 | 106 | proof added reference | (17.4.1,d)) | closing parentheses look doubled; preserved | medium |
| 29 | 106 | structure-sheaf symbols | upright O | typewriter capital O, no visible calligraphic glyph | high |
| 29 | 107 | annotations after completed rings | correspond -- corps résiduel | first word very compressed; may be a different abbreviation | low |
| 29 | 107 | completed-ring subscripts | p′ and p″ | ordinary p versus Gothic p not settled by heavy ink | medium |
| 29 | 107 | subscript cancelled beneath Z | a | overwritten blob retains no reliable full outline | low |
| 29 | 107 | last prose line | hom. canoniques | hom. is abbreviated and compressed | medium |
| 29 | 107 | bottom margin diagram | cancelled A′ and brace, then A→B | tiny top scribble may be lettering practice; preserved with doubt | low |
| 29 | 107 | recurring handwritten homotopy-group sign | Π | π; angular two-stem handwriting does not securely distinguish typographic case; reconciled consistently across 096, 098, 100 and 107 | medium |
| 29 | 108 | lemma hypothesis | idˣ étrangers | abbreviation for ideals uncertain; not expanded in transcription | medium |
| 29 | 108 | lemma conclusion | isom | end of word compressed, probably abbreviation | medium |
| 29 | 108 | proof (ii) transition | par hypothèse; il s’ensuit | heavily compressed handwriting | low |
| 29 | 108 | proof first existential element | b | overwritten with an earlier loop; b is best reading | medium |
| 29 | 108 | final map product symbol | × | could be a plus; literal alternative retained | medium |
| 29 | 108 | pale typescript beneath manuscript | mirror-image reverse-side show-through | orientation checked by rotation; not a second text written on this face | high |
| 29 | 108 | ideal-product proof, first equality | Q∩Q′ = Q∩Q′(Q+Q′) | no parentheses surround the first factor on the right; audit removed supplied parentheses | high |
| 29 | 109 | typed spellings throughout | fonctori; explicité; emploie; Kaplanski; moyenne-ageuse; trainer | unmodernized spellings retained; no silent normalization | high |
| 29 | 110 | quotient in a) | B/R | first letter appears overwritten from A; A remains possible | medium |
| 29 | 110 | ideal letters throughout | J,J′ | J-shaped handwritten glyphs, possibly I; same choice kept throughout page | medium |
| 29 | 110 | a) ambient ring | de A; J+J′=A | A is what is written although the opening names B; retained | high |
| 29 | 110 | middle claim | est uniquement de la forme (P)=(Q)(Q′) | adverb compressed; first letter in parentheses overdrawn P/R | medium |
| 29 | 110 | lower representative abbreviation | repr. | letters compressed; no expansion attempted | low |
| 29 | 110 | crossed bracket | [NB. … faut | two separated units under a horizontal strike; NB. and faut uncertain | low |
| 29 | 110 | last transition | l’unicité résulte qu’ | syntactically awkward best reading; not repaired | low |
| 29 | 110 | bottom operator | Spec A local | operator could be abbreviated Sp or Spm | low |
| 29 | 111 | cancelled sentence at top | fatalité par contre ne pourrait que m’inquiéter sérieusement | opening word and ne doubtful under strike | low |
| 29 | 111 | cancelled local-ring adjective | intègre | middle letters obscured by horizontal cancellation | medium |
| 29 | 111 | arrow between completed Y and Z | right arrow | left end retraced; possible second arrowhead | medium |
| 29 | 111 | word cancelled beside completed product | connexe | very heavily scribbled; best reading only | low |
| 29 | 111 | lower-right equality | Â=Â′ | hat over final A′ partly coincides with enclosing stroke; A′ also possible | medium |
| 29 | 111 | lower drawings | TikZ stroke reconstruction | relative parts and labels preserved; free pen strokes approximated | medium |
| 29 | 117 | superscripts after G and after donc X̄ | cancelled prime-like marks | heavily inked marks could be other typed accidents | low |
| 29 | 117 | transitivity word | transitiv[deleted e]ement | x overstrike appears between v and e; original character doubtful | medium |
| 29 | 117 | second paragraph crossed word | se placera | x-overtyping leaves only some consonants visible | low |
| 29 | 117 | normalisation paragraph | normalisé de Ū; relatief to Ū′ sur Ū | Ū is visible where mathematical context might suggest X̄; retained as written | high |
| 29 | 117 | normalisation plural | normaalisés | overlapping type could instead be normalisés | low |
| 29 | 117 | third paragraph initial cancellation | X est | first symbol densely overwritten | low |
| 29 | 117 | bar-p formula | p̄(O_X̄′)^G | no pushforward star or subscript is visible after p̄ | high |
| 29 | 118 | cancelled operator between P,Q | ⊗ | circled overprint obscured by strike; no original connector added beneath | low |
| 29 | 118 | isolated stroke by fragment | short pen stroke | could be a numeral 1; not secure enough to identify authorial pagination | low |
| 29 | 118 | pale reversed text | show-through of scan 117 | not repeated as a second text on this face | high |
| 29 | 124 | pencilled subtitle last word | ensembles | schémas possible; very faint compressed strokes, first reading follows visible loop pattern | low |
| 29 | 126 | cancelled sentence above vi | est essentiellement provisoire | x-overtyping obscures most of the cancelled sentence | low |
| 29 | 126 | before Lemme | justifier la vérité; cause | first phrase heavily crossed; inserted word looks like cause despite awkward wording | low |
| 29 | 126 | lemma point | cancelled géométrique | x-overtyping largely conceals the old word | low |
| 29 | 126 | after produits | trivial) et | several overtyped x marks; et itself may be cancelled original matter | medium |
| 29 | 126 | projection G to G_sép | G [blank] G_sép | no arrow visible; not supplied | high |
| 29 | 126 | bottom mark | drawn angular ink mark | not securely a letter; reproduced as strokes | low |
| 29 | 129 | second line deleted word | respectifs | x-overtyping; uncertain entire word | low |
| 29 | 129 | after système local des groupes fondamentaux | en x | overtyped letters might be another short qualifier | low |
| 29 | 129 | inside cancelled block | groupe; on devrait pouvoir mettre | groupe overtyped; last word of unfinished sentence obscured | low |
| 29 | 129 | insert above nommé | (sur X, | parenthesis and comma visible; no inserted closing parenthesis found | medium |
| 29 | 129 | after associer / after Witt et | à un / donc | x-overtyping makes these short cancelled words uncertain | low |
| 29 | 129 | handwritten right margin near bottom | soit | est is another possible reading; dark overlaid strokes | low |
| 29 | 129 | fundamental-group notation | underlined Π₁ in first paragraph; plain Π₁ below | underlining distinguishes pro-group schemes; retained only where drawn | high |
| 29 | 130 | first line cancelled word | en | two overtyped letters | medium |
| 29 | 130 | after J’espère | arriver-dans | thin oblique stroke may be incidental rather than a hyphen | low |
| 29 | 130 | second paragraph cancelled words | ce qui | x-overtyping but q descender visible | low |
| 29 | 130 | near end | multiplodoque | typed word clearly ends doque; retained rather than normalized | high |
| 29 | 131 | end of first line | universellt | universelle is possible; abbreviated ending not secure | low |
| 29 | 131 | qualifiers of G | cancelled plat; cancelled séparable; inserted étale | first cancellation is a dense short horizontal mark | low |
| 29 | 131 | group formula cancelled end | ×X | crossed symbol could be another X with index | low |
| 29 | 131 | pointing condition insertion | d’un isom. before σ_T*(X′) ≃ G_T | placement under munis and curved line over the formula; attachment uncertain | medium |
| 29 | 131 | N.B. middle clause | puisqu’on suppose que G | compressed cursive; could read s’il en est …; not settled by mathematical expectation | low |
| 29 | 131 | N.B. final words | Cas fini?? | perhaps another qualifier; two question marks visible | low |
| 29 | 131 | after Si oui | sch. | compact looped abbreviation could be a letter denoting the representing object | low |
| 29 | 131 | last main line | ex. et à gauche | ex. and gauche suggested by strokes; exact middle wording doubtful | low |
| 29 | 131 | right margin rotated 180 degrees | 4.9; 4.17 or 4.13; fid. plat; plat; exacte; finis? | last short word and second reference uncertain | low |
| 29 | 131 | margin diagram lower indices | bullets on first three C objects; 0 on last | extra ink dots below first two objects drawn separately; indices may instead all be 0 | low |
| 29 | 131 | margin diagram multiple connectors | double and triple right arrows | some arrowheads faint; horizontal dash from first to second lower object has no visible head | medium |
| 29 | 131 | foot formula | H¹(X,G | no closing parenthesis visible; curve through labels reproduced | high |
| 29 | 131 | N.B., word after tel | fibré | fonct.; the short word has an F-like initial and compressed middle strokes | low |
| 29 | 131 | rotated margin, third connector in each row | bottom of each three-stroke connector has no distinct arrowhead | possible incomplete arrowhead; no head supplied | medium |
| 29 | 132 | recurring coordinate index | α | a is also possible in this typeface; same uncertainty preserved throughout | medium |
| 29 | 132 | first paragraph | the set all families | missing of is in the typescript; not supplied | high |
| 29 | 132 | second paragraph | such a vector is in T | v was introduced in V and T in W; the visible text is retained | high |
| 29 | 133 | isolated top mark | cancelled (iv) | numeral resembles iv but heavily retraced | low |
| 29 | 133 | ii | fidèlement plats qua. cpts. | compressed ending of fidèlement; agreement and abbreviations retained | medium |
| 29 | 133 | v | tt; K′ in prose; k′ in formula | abbreviation and capitalization retained as seen | medium |
| 29 | 133 | v cancelled material | plat or k | dense stroke over small group of letters | low |
| 29 | 133 | map in v | F(k) - F(k′) | connector appears a dash without clear head; arrow is alternative | medium |
| 29 | 133 | cancelled heading | Recommençons | whole word crossed; possible different opening R-word | low |
| 29 | 133 | local proof dimension | n | 1 is alternative; stroke is nearly horizontal | low |
| 29 | 133 | open complement | S₁=S-y | s is also possible; y-like descender visible | low |
| 29 | 133 | cancelled words after M₁ | Considérons les points | last word crossed through too densely to settle | low |
| 29 | 133 | cancelled formula after ξ_i^0 | ∈F₀/k | partly erased by multiple strokes; all symbols tentative | low |
| 29 | 133 | condition iii bracket | opening square bracket only | no closing bracket appears beside the condition; not supplied | high |
| 29 | 135 | cancelled symbol before X(s) | X_s | dense crossed letter; subscript uncertain | low |
| 29 | 135 | inline φ_st and φ_s connectors | dash | no definite arrowheads; arrows given as alternatives | medium |
| 29 | 135 | left-margin opening wording | une définition de | perhaps un modèle; rapid strokes do not settle the phrase | low |
| 29 | 135 | left-margin cancellations | la; le groupe; X_t | all strongly overwritten, especially the mathematical letter | low |
| 29 | 135 | left-margin final qualifier | compatibles avec les φ | very small writing, final symbol/word uncertain | low |
| 29 | 135 | left-margin diagram first upper connector | X(s)—𝓧 | straight line has no visible head; retained as a dash | high |
| 29 | 135 | main proof introduction after pleinement fidèle | Je vais pour du moins ramener au local | compressed cursive; syntax remains unresolved rather than regularized | low |
| 29 | 135 | before par récurrence | le prouver | ending r is not secure | low |
| 29 | 135 | final comparison | sous-préschémas fermés de S ≠ S | same S repeated without added prime; not repaired | high |
| 29 | 135 | opening lemma, after et pour | tout | tt; the middle of the rapid word is compressed | medium |
| 29 | 137 | second object in sequence | U | H is possible beneath retracing; U in surrounding prose | medium |
| 29 | 137 | sequence connectors | e—U and G—Γ | no clear heads; unlike the U→G and Γ→e arrows | medium |
| 29 | 137 | conditions of U | cancelled s; un homéomorphisme | small isolated cancellation and crossed phrase are uncertain | low |
| 29 | 137 | Γ to S connector | dash | could be a minimally drawn arrow | medium |
| 29 | 137 | after point a | cancelled ξ | small zigzag heavily cancelled | low |
| 29 | 137 | after Proposition | soit S′→S | heavily scribbled; first word and symbols tentative | low |
| 29 | 137 | question at old implication | ? | small isolated mark above the end of cancellation may be a question mark | low |
| 29 | 137 | proof wording | de le théorème | visible de at previous line end followed by le; no contraction supplied | medium |
| 29 | 138 | insertion after P in proposition 3 | princ. sous G | could be principal sous G; abbreviation cramped | low |
| 29 | 138 | proposition 3 phrase | ont = valeur | literal equality sign; no expansion to même | high |
| 29 | 138 | before Q in bracketed paragraph | cancelled P | heavily overwritten letter | low |
| 29 | 138 | end of bracketed paragraph | et l’isomorphisme réciproque induit par s | no est supplied: none clearly written | medium |
| 29 | 138 | cancelled words before relatif | est dit | heavy horizontal cancellation | low |
| 29 | 138 | minimality condition | on ne peut trouver | compressed handwriting; tentative word sequence | medium |
| 29 | 138 | minimality, group of (P′,ξ′) | G | no prime clearly visible here | medium |
| 29 | 138 | contracted product in final formula | ×_G G′ | subscript G and terminal G′ read literally, despite expected opposite order | high |
| 29 | 138 | overwriting of ξ in final formula | cancelled ξ′ | small dark overwritten mark above ξ; identification tentative | low |
| 29 | 139 | pointed-torsor functor notation, three occurrences | calligraphic Z: uncertain 0 in definition, 1-like stroke in proposition source, no distinct exponent in target | Letter style and retraced initial exponent remain uncertain; occurrences were compared individually rather than regularized | low |
| 29 | 139 | first definition | classes d’isomorphie | line break is after isom; ending phie retained | medium |
| 29 | 139 | left marginal annotation | Sans rigueur | small oblique cursive, especially first word, uncertain | low |
| 29 | 139 | qualifier above Hom | gr. | small superscript abbreviation | medium |
| 29 | 139 | u,v:G to G′ and diagonal G′ to product | dash | no unequivocal head in either short connector | medium |
| 29 | 139 | first product subscript | S | heavily retraced with long stroke to right | low |
| 29 | 139 | bottom torsor diagram target | Q | letter heavily retraced, follows the preceding overbrace label | medium |
| 29 | 139 | first definition exponent | 0 | 1; the closed dark loop favors 0, whereas the proposition has a 1-like stroke | low |
| 29 | 139 | first definition pointing symbol | deleted ξ with a above it | strong retracing; the lower cancelled mark is not securely legible | low |
| 29 | 139 | proposition target functor | deleted Z-like mark followed by Z without a distinct superscript | no superscript 1 supplied at this occurrence | medium |
| 29 | 140 | otherwise blank sheet | pale mirrored show-through | reverse-side writing is not an additional autograph layer on this face | high |

## Abbreviations encountered

Expansions below are editorial suggestions only. They are not substituted into the LaTeX; a final period is not supplied where the manuscript omits it. Variants in the same row are listed only where they actually occur in the transcription.

| Written form | Probable expansion / sense | Scans or caution |
|---|---|---|
| `il f et s` | il faut et suffit | 095 |
| `cf` | confer / compare | 097 |
| `N°` | numéro | 097 |
| `i.e.`, `i.e` | id est / c'est-à-dire | 096–104, 117, 126, 130–131 |
| `c-à-d` | c'est-à-dire | 104; the reading is unsure |
| `e.g.` | exempli gratia / par exemple | 109 |
| `loc.`, `loc` | localement | 100–103, 133, 135 |
| `n.th.` | noethérien | 100; shorter visible form retained with doubt |
| `noeth.` | noethérien | 133, 135 |
| `préschém.` | préschéma | 133, 135 |
| `schém.` | schéma | 101 |
| `sch.` | schéma | 131; could instead be a symbol naming the representing object |
| `grpes` | groupes | 103 |
| `gr.` | groupes / de groupes | 139, superscript on Hom |
| `s-groupe`, `ss-groupe` | sous-groupe | 100, 138; the S in S-ss-groupe denotes the base, not part of the abbreviation |
| `hom`, `hom.` | homomorphisme; in “principal hom.”, homogène | 096, 101, 107, 135, 137, 139; sense depends on the phrase |
| `isom`, `isom.` | isomorphisme | 096, 103, 108, 131, 135, 138 |
| `ens`, `ens.` | ensemble | 104, 131, 139 |
| `à g.` | à gauche | 105 |
| `cont` | continu | 105, Hom cont |
| `op.` | opérateurs / opérations | 101, “à op. G” |
| `p.r.` | par rapport | 103 |
| `revêtt` | revêtement | 103 |
| `rec.` | recouvrement or revêtement | 100, 103; the abbreviation alone does not settle the terminology |
| `pt` | point | 100, 103, 138 |
| `géom`, `géom.` | géométrique | 100, 103, 117 |
| `gén.` | générique | 100, 103 |
| `car.`, `car` | caractéristique | 098, 100 |
| `alg.`, `alg` | algébrique / algébriquement | 096, 104, 129, 133 |
| `ext.` | extension | 133 |
| `conn` | connexe | 100 |
| `irred` | irréductible | 100; uncertain reading |
| `supp` | support | 100, deleted |
| `Et.` | Étude | 100, deleted and uncertain |
| `Dém.` | Démonstration | 104 |
| `dim` | dimension | 104, 133 |
| `tt`, `tte` | tout, toute | 100, 104, 110, 133, 135; tout/tt remains unsure in 135's opening |
| `déc.` | décomposition | 110 |
| `repr.` | représentant | 110; uncertain reading |
| `NB.`, `N.B.` | nota bene | 110, 131 |
| `fid.` | fidèlement | 131 |
| `qua.`, `qu.` | quasi | 133 |
| `cpts.` | compacts | 133 |
| `princ.` | principal | 138; alternative fully written principal is retained in place |
| `t.q.` | tel que / tels que | 138–139 |
| `th.` | théorème | 107 |
| `universellt` | universellement | 131; ending uncertain, with universelle as alternative |
| `ex.` | exact | 131; the entire “ex. et à gauche” reading remains unresolved |
| `fonct.` | foncteur | 131; only a reading alternative to the uncertain fibré, not an established occurrence |
| `mod` | modulo | 101, marginal Chern class |

## Legibility and limits

The typescripts are substantially easier to read than the rapid manuscript sheets, but carbon-copy gaps, typewriter overstriking, and handwritten replacements still require explicit doubt. The greatest uncertainty is in the opening and right edge of 096, the dense changes in 100–103, the short algebraic proof transitions in 108–110, the very compressed main text and upside-down margin of 131, the marginal neighborhood hypothesis and proof introduction in 135, and the overwritten functor notation and small diagonal annotation in 139. The pencil cover subtitle on 124 remains particularly faint.

The large displays and most clearly printed words are more secure than those passages. This is not a claim that every unmarked word is infallible: even after the second visual audit, fast cursive can support more than one reading. The small word-count illegibility markers are confined to physically unreadable cancelled words; no formula or diagram symbol has been replaced by an illegibility count. The drawings are hand-coded TikZ approximations of the visible contours, positions and labels, not metric facsimiles.

Pale mirrored show-through was distinguished from writing on the viewed face, especially in 108–109, 117–118, 131–132 and 139–140. The actual typescripts on reused sheets were transcribed in full, including when upside down; their provenance was not inferred from typography alone. No OCR, published edition, neighbouring transcription or contextual source was used to establish the readings. All 31 supplied pages received a sequential first reading and a sequential second audit before context access.
