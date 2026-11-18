# MPL_98: notation, doubts, and abbreviations

## Notation table (maintained during transcription)

| Manuscript sign | LaTeX | Evidence / caution |
|---|---|---|
| Double quotation marks | Two backticks and two apostrophes | Guillemets only if drawn. |
| Symmetric-power capital sigma | `\Sigma^r(X/Y)` | Retain relative base and exponent exactly, including overwritten bases. |
| Norm/correspondence label | `\unsure{\operatorname{Cor}\|\operatorname{Cn}}` | Compared across scans 007, 011–012 during the second audit; Cor is the common primary reading, with Cn retained as an unresolved alternative. |
| Norm symbol | `N` with literal indices and superscripts | Distinguish ordinary N from the class of morphisms, whose alphabet remains as drawn. |
| Disjoint sum | `\amalg`, `\coprod` | Small two-prong sign versus large indexed coproduct retained. |
| Canonical map label | `\mathrm{can}` | Do not expand in transcription. |
| Typescript underlined letters | `\uline{B}`, `\uline{R}`, etc. | Do not replace with modern bold/blackboard alphabets. |
| Typescript running index | `\unsure{x\|\varkappa}` | Compared on scans 004 and 010; x is the primary reading in both, not silently normalized to a Greek index. |
| Archive corner numbers | TeX comments | Excluded from `\mspage`. |
| Exponents and primes | Literal prime, numeric exponent, or `^!` only when visible | No inferred prime/exclamation equivalence. |
| Group-action functor | `\Phi_A`, `\Phi` | Preserve printed arguments E/A exactly; do not repair from the definition. |
| Class of normed morphisms | `\mathcal N` | Script capital N compared across scans 011–014; distinct from the numerical norm and later integer bound N. |
| Script or underlined cohomology sheaf | `\mathcal H`, `\underline{H}` | Alphabet and underline are read separately on scans 018–020. |
| Multiplicative group | `G_m` | Retain handwritten primes on higher cohomology terms, notably scan 022. |
| Typescript linear system | `\mathcal L(X)` versus `L(X)` | Distinct calligraphic system and vector space. |
| Typescript local ring and maximal ideal | `\mathfrak{o}`, `\mathfrak{m}` | o is a handwritten stylized glyph; doubt retained where recognition is weak. |
| Generic length | `l` | Distinguished from numeral 1; uncertain letter/digit retains a doubt. |
| Geometric-class set | `\unsure{\Phi\|\mathrm{Cl}}(X/k)` | All occurrences on scans 030–033 compared. The rounded stem and occasional apparent second stroke do not settle Phi versus Cl; both remain marked consistently. The later family-class Phi on scans 035 onward is clearer. |
| Operation on tuples | `T(F_1,-F_n)`, later `\Phi` | The alphabet changes visible on scan 032 remain; the operation symbol is not identified with the doubtful class-set glyph merely because of its meaning. |
| Underlined structure ring | `\underline{O}` | Do not silently replace by calligraphic O. |
| Universal extensions | `\widetilde k`, `\widetilde X` | Tilde distinguished from prime and circumflex. |
| Family of fibre classes | `\mathcal E(F)`, `\mathcal E_{X/S}(F)` | Scans 035 onward; distinct from the class-set glyph. |
| Base-change primes | `S'`, `S''`, `S'''` | Prime counts retained literally or marked; several overwritten instances. |
| Homological operations | `\operatorname{Tor}`, `\operatorname{Ext}`, sometimes underlined | Underlines are transcribed only when visible. |
| Dash between objects | `-` or an unheaded TikZ edge | Not silently converted to an arrow. |
| Dash in an argument list | `F_1,-,F_n`, or `F_1,-F_n` where written | Compared on scans 032–044; visible dashes retained instead of supplying ellipsis dots. |
| Integer base | `Z`, or `\unsure{Z\|\mathbf Z}` where doubtful | Plain Z on scan 018; alphabet doubt on scan 028 retained. No automatic conversion to blackboard bold. |
| Hom, Tor, Ext, and their coefficient rings | `\operatorname{Hom}`, `\operatorname{Tor}`, `\operatorname{Ext}`; literal underlines | Underlining and coefficient subscripts checked separately, including the A/B doubt on scan 043 and underlined L on scan 042. |

The table records the pre-context comparison of recurring signs. Consistency means preserving the same visible reading or the same explicit doubt; it does not mean resolving an ambiguity by mathematical expectation. No manuscript `\mspage` number was identified securely; archive foliation is recorded only in comments, and printed reused-sheet page numbers remain ordinary text.

## Doubts: contextual register

The locations below refer approximately to the manuscript. The exhaustive in-text index following this table supplies the exact marked expressions and their locations in the page fragments.

| File | Scan | Approximate line / location | Reading | Alternatives | Confidence |
|---|---|---|---|---|---|
|98.pdf|002|title|Formalisation|Formulation|low|
|98.pdf|002|upper middle faint pencil|P|unidentified pencil mark|low|
|98.pdf|003|initial identity line|1_A tensor ..|1_M tensor ..|low|
|98.pdf|003|tensor display endpoint|closing mark; superset dot|unfinished expression|low|
|98.pdf|003|arrow before T_A^n|Leftarrow|leftarrow|medium|
|98.pdf|003|paragraph|Endomorphismes; commutent; stable|endings hurried|medium|
|98.pdf|003|isolated functor|Cart|Car?|low|
|98.pdf|003|bottom middle overwritten formula|X_S F|times_S F|low|
|98.pdf|003|bottom right arrow label|i|punctuation mark|low|
|98.pdf|004|repeated running index|x|varkappa|medium|
|98.pdf|005|second diagram far left|Q|overwritten letter|low|
|98.pdf|005|middle right arrow label|alpha_(r)|alpha_r|low|
|98.pdf|005|middle left object|u_S^r|G_S^r|low|
|98.pdf|005|composition diagram upper curved-arrow label|(rs)|(n)|low|
|98.pdf|005|box first norm subscript|deleted G before U|overwritten slash|low|
|98.pdf|005|bottom left scattered letter|Y|X|low|
|98.pdf|007|top inserted (i) exponent|r|n|low|
|98.pdf|007|upper-right square interior|comm. polyp.|comm. with abbreviated qualifier|low|
|98.pdf|007|additivity top norm subscript|F_1 oplus F_2|overwritten operation|low|
|98.pdf|007|transitivity sketch right|Cas du *|Cas du with unfinished sign|low|
|98.pdf|007|four enclosed rows|Y-morphisme; Z-morphisme|abbreviated endings|medium|
|98.pdf|007|third enclosed arrow|f|gamma|low|
|98.pdf|007|bottom top-left object exponent|rs|r|low|
|98.pdf|007|bottom arrow label|gamma|f|low|
|98.pdf|007|bottom margin|commutatif|commut...|low|
|98.pdf|007|recurring norm labels|Cor|Cn|low|
|98.pdf|008|last line underlined letter|R|F (faded type)|medium|
|98.pdf|009|top-right source superscript|rs|r|medium|
|98.pdf|009|cancelled fragment above chi diagram|(G_Y)^r|overwritten formula|low|
|98.pdf|009|margin beside chi diagram|Z-morphisme rendant commutatif|ending/number not clear|low|
|98.pdf|009|triangle diagonal label|can. phi_Y|composition sign before phi_Y|low|
|98.pdf|009|lower-right margin opening|lié par|? par|low|
|98.pdf|009|lower prose|par suite|par ...|medium|
|98.pdf|009|boxed RHS middle base index|X|Y overwritten|medium|
|98.pdf|010|second index of A and h throughout example 1|x|varkappa|medium|
|98.pdf|011|title last word|normés|normants / normaux|low|
|98.pdf|011|opening insertion|où les sommes finies existent|word endings compressed|medium|
|98.pdf|011|opening cancellation|appelés morphismes normés|middle overwritten|low|
|98.pdf|011|axiom iv addition|existence; compatible à la formation de sommes|one word physically obscured; attachment difficult|low|
|98.pdf|011|axiom v subgroup alphabet|fraktur S_n|script S_n|medium|
|98.pdf|011|orange quotient addition|et est comp. aux changements de base|abbreviation/end obscured|low|
|98.pdf|011|orange right punctuation|!|?|low|
|98.pdf|011|degree v bis cancelled line|E=Delta^r; F=(tensor^r E)/G|several words obscured by heavy strokes|low|
|98.pdf|011|norm paragraph fragment|sur script N-|unfinished qualification|low|
|98.pdf|011|recurring norm symbol|Cor|Cn|low|
|98.pdf|012|norm labels throughout|Cor|Cn|low|
|98.pdf|012|iv ter insertion|d’injection|d’immersion|low|
|98.pdf|012|right cancelled wording|r tel que pour ∀; il y a|several occluded words|low|
|98.pdf|012|right N.B. group label|G|H|medium|
|98.pdf|012|right last two lines|fonctorielle; i.e.; c’est un hom|edge and overwriting|low|
|98.pdf|013|left margin|déduire; galoisiennes; spéciales; par un autre|marginal wording uncertain|low|
|98.pdf|013|Exemple II sheaf insertion|qu. coh.|f. coh.|low|
|98.pdf|013|Exemple II|d’algèbres|algèbre|medium|
|98.pdf|013|Exemple III covering phrase|non ramifiés; ayant un degré|several compressed word endings|low|
|98.pdf|014|top group|Γ|G|low|
|98.pdf|014|cancelled paragraph|on a encore des exemples, et des|two unreadable words below crossing strokes|low|
|98.pdf|014|lower functor domain|C′|E′|medium|
|98.pdf|014|left bracket annotation|à développer|à vérifier|low|
|98.pdf|014|last parenthesis|id : fait aussi sur N|compressed wording|low|
|98.pdf|014|last word|compos…|author’s word followed by dots|low|
|98.pdf|014|middle object phrase|l’objet|le couple|low|
|98.pdf|015|second intersection display|X_{-1}|X_{-u}; ink resembles -1|medium|
|98.pdf|015|divisor subgroup index|ℓ|l|medium|
|98.pdf|016|display argument|overwritten E then X|X only, overwritten|low|
|98.pdf|016|cancelled formula|A ×_(G) X ×_(G) A|two overlapping abandoned formulas|low|
|98.pdf|016|cancelled line below display|étant donné; la donnée ?|crossing line obscures middle and end|low|
|98.pdf|016|cancelled bottom paragraph|trivialt; lim; foncteurs Hom|word endings and abbreviation uncertain|medium|
|98.pdf|017|bars over D(u), D(a+v), D(v)|overline over complete expression|line does not quite cover closing parenthesis|medium|
|98.pdf|018|boxed abutment exponent|*|single compressed superscript|medium|
|98.pdf|018|upper sheaf term|prépré-faisceau|overwritten first pré; second pré double-underlined|low|
|98.pdf|018|left margin|s’apparente|s’applique|medium|
|98.pdf|018|proof heading|Preuve. utiliser|Pr le. utilisé|low|
|98.pdf|018|final complex description|complexe de simplexe simple défini par T|complexe de sommets; wording uncertain|low|
|98.pdf|019|local ring symbol|fraktur o|v|low|
|98.pdf|019|replacement for théorème|prop|unpunctuated abbreviation|medium|
|98.pdf|019|left marginal pencil|utile au cas non singulier?|cas singulier?|low|
|98.pdf|019|bottom pencil annotation|Nouveau!|Revoir!|low|
|98.pdf|020|left upper annotation|identités|identité|medium|
|98.pdf|020|crowded insertion under definition|valeur en Φ\|S; du foncteur dérivé; il en résulte immédiatement|several overwritten words|low|
|98.pdf|020|relative spectral sequence exponent|natural sign|n|low|
|98.pdf|020|relative spectral sequence coefficients|Φ overwritten by A|A thickened only|low|
|98.pdf|021|typed spelling near middle|augmente.d’une|dot appears between words|high|
|98.pdf|021|proposition (i)|les condition|possible final s at page edge|medium|
|98.pdf|022|first object of large sequence|bullet|0|medium|
|98.pdf|022|small T diagram|S as arrow label|possibly intended as displaced product subscript|medium|
|98.pdf|022|vertical field labels|gal|compressed letters|low|
|98.pdf|022|isolated bottom symbol|vdash|t|low|
|98.pdf|023|local ring throughout|\mathfrak{o}|stylized handwritten o/v glyph|medium|
|98.pdf|023|power-series sum lower limit|j=\infty|j=0 is mathematically expected but not what the enlarged ink shows|high|
|98.pdf|023|monomial ordering sentence|da,s|dans (not supplied)|high|
|98.pdf|024|top description|application|first word highly cursive|medium|
|98.pdf|024|three braces|d’où|ditto abbreviation possible|low|
|98.pdf|024|overwritten group letters third row|deleted G, inserted X|G/X overwrite direction not fully certain|low|
|98.pdf|024|third NB|via celles de|c.-à-d. celles de|low|
|98.pdf|024|marginal labels|Čech|Cartan|medium|
|98.pdf|024|last abutment|B_G|B_X expected but ink G|high|
|98.pdf|025|definition of divisor|sur A une variété V|apparently retained typing error|high|
|98.pdf|025|right edge before codimension|c|partial character or stray mark|low|
|98.pdf|025|separation sentence|séparé|sépare|medium|
|98.pdf|027|opening|deux choses|second noun very compressed|medium|
|98.pdf|027|statement after quotients|de l’un ≃ L, et dont|faint cursive; attachment and first word unresolved|low|
|98.pdf|027|induction|on récure|on récurre|medium|
|98.pdf|027|cancelled and rewritten middle paragraph|pour l=1, alors les énoncés ci-dessus, rien...|extremely faint and overwritten; several words unresolved|low|
|98.pdf|027|last long paragraph|les uns images d’hom. variables|compressed cursive; connection and hom. qualifier unresolved|low|
|98.pdf|027|standalone mark after parenthesis|ι|possibly incomplete letter rather than formula|low|
|98.pdf|027|middle, before collections|l'union de|l'un des|low|
|98.pdf|027|middle, end of paragraph|limité|limitée|low|
|98.pdf|028|first fixed sheaf letter|E|L|medium|
|98.pdf|028|finite set phrase|en deleted nombre inserted nb finis|abbreviation and ending ambiguous|low|
|98.pdf|028|number before Résultat de Chow|a)|4°)|low|
|98.pdf|028|cancelled diagram|arrows P^n T|faint crossed objects uncertain|low|
|98.pdf|028|purity condition cancellation|n’a que les points génériques de dim|crossed text incomplete|low|
|98.pdf|028|final proof|les noyaux de tous les F′_i|noyaux unqualified; preserve phrasing|medium|
|98.pdf|028|Chow statement, base alphabet|Z|\mathbf Z|medium|
|98.pdf|029|equivalence name|K-équivalents|k-équivalents|medium|
|98.pdf|029|left ruled picture|X, K′, G, S, S|small peripheral labels uncertain|low|
|98.pdf|029|bottom deletions|alors; deux de type fini|heavily struck text|low|
|98.pdf|029|proposition|sur un X⊗_kK|un repeated again before X⊗_kK′|high|
|98.pdf|030|question|composée|commune|medium|
|98.pdf|030|universe parenthesis|dans le U-univers que alors contenant|compressed/faint words; grammar not restored|low|
|98.pdf|030|class-set notation|Phi(X/k)|Cl(X/k)|low|
|98.pdf|030|bottom|l’ens|l’on|medium|
|98.pdf|030|lower margin|après|appliqué|low|
|98.pdf|030|end first sentence|de K|de k|medium|
|98.pdf|030|universe qualification|alors|choisi|low|
|98.pdf|031|class notation|Phi|Cl; comparison with scans030–033 does not settle the glyph|low|
|98.pdf|031|equivalence phrase|qui est définie comme suit|faint connecting words|medium|
|98.pdf|031|integer and tuple length|n|h|medium|
|98.pdf|031|condition symbol|mathfrak P|Π|low|
|98.pdf|031|diagonal marginal note|Se donner X et Y sur k...|several faint/crowded words and functor symbols unresolved|low|
|98.pdf|031|diagonal margin, after se donner un|fonction|foncteur|low|
|98.pdf|032|condition i last subscript|i|n|medium|
|98.pdf|032|definition4 operation symbol|Φ|T earlier in same page; manuscript appears to change symbol|medium|
|98.pdf|032|left marginal request|introduire la prop. et la définition|introduction; prop. word uncertain|low|
|98.pdf|032|top margin|à généraliser|à applications|medium|
|98.pdf|033|sum of class sets|réunit|somme|low|
|98.pdf|033|top phrase|sur un = X⊗_kK|un = appears without noun; no repair|medium|
|98.pdf|033|marginal paragraph|par le fait que les F_i sont les fibres...|faint words and final symbols unresolved|low|
|98.pdf|033|deleted word after d’|autres|older word uncertain|low|
|98.pdf|033|left margin, after sont|sur|les|low|
|98.pdf|033|left margin, after fibres des|schémas|faisceaux|low|
|98.pdf|034|a, right|on peut regarder un argument|faint entire continuation|low|
|98.pdf|034|d, first and third lines|former; en ce qui|indistinct abbreviated cursive|low|
|98.pdf|034|c, parenthesis|propre|faint before donné|medium|
|98.pdf|034|f, cancellation|two words|heavily inked over|low|
|98.pdf|034|h, deleted word and condition|quotients; chi=0|first cancelled noun and overwritten characteristic symbol|low|
|98.pdf|034|i, bottom|8 illegible words; F|thick multiple cancellation strokes|low|
|98.pdf|035|middle|composée|ending faint|medium|
|98.pdf|035|tensor display|H_{s double prime}|triple prime possible; two visible strokes|medium|
|98.pdf|035|lower displays|G tensor_{S prime}; G_i tensor_{S prime}|single prime visible, double prime mathematically expected but not substituted|medium|
|98.pdf|035|bottom insertion|parties loc. fermées|number and adjective endings faint|low|
|98.pdf|035|deletion above inclusion|Alors|crossed out|low|
|98.pdf|036|deleted middle|plats puis|faint through cancellation outline|low|
|98.pdf|036|left margin|Rédiger sous forme de lemme; utilisable|compressed diagonal writing; valable possible last adjective|low|
|98.pdf|036|lower paragraph|lemme|very faint ligature|medium|
|98.pdf|036|bottom insertion|disjoints|ending obscured under ink|medium|
|98.pdf|037|upper display|T prime sub i|possibly T prime only|medium|
|98.pdf|037|proof revision|considère les sous-faisceaux; et les; donc sont|heavily revised and crossed lines, attachment uncertain|low|
|98.pdf|037|b statement|type finis|final s faint|medium|
|98.pdf|037|last paragraph|prenant; X et Z sur Y|verb ending faint; unusual ordering retained as seen|medium|
|98.pdf|037|last paragraph|two cancelled words|heavily inked|low|
|98.pdf|037|marginal complex, isolated lower object|H_{i+1}|B_{i+1}|low|
|98.pdf|038|deleted line|Comme le dernier est un l aboutissement|several words faint beneath cancellation; last attempted reading especially weak|low|
|98.pdf|038|spectral sequence display|deleted tensor_Y|overwritten base index and cancellation|low|
|98.pdf|038|final condition|Y-plats|Y seen; no substitution of S|medium|
|98.pdf|038|insertion above commençant|ab. = le dernier,|ab. le dernier,|low|
|98.pdf|039|upper rewritten base symbols|deleted U prime, inserted S prime|ink overwritten heavily; underlying letters tentative|low|
|98.pdf|039|upper display|X_i prime=X ...; F_i prime=F ...|no indices visible on right-hand X,F; retained literally|medium|
|98.pdf|039|lemma inner Tor superscript|O_S|O_Y possible, curved subscript|medium|
|98.pdf|039|left margin|Peut-on faire plus ?|very faint short question; first and middle words uncertain|low|
|98.pdf|040|first deleted word|Preuve|short word crossed at right|medium|
|98.pdf|040|resolution notation|L prime superscript i, deleted A prime subscript|overwritten sub/superscripts|low|
|98.pdf|040|K prime equality|deleted tensor_B B prime|densely overwritten symbols|low|
|98.pdf|040|first Tor subscript|alpha|asterisk possible|medium|
|98.pdf|040|last deletion|établie|crossed word after l apostrophe|low|
|98.pdf|040|margin first words|au lieu de|faint; rest clearer|medium|
|98.pdf|040|marginal object layout, first primed module|M'|M'_1|medium|
|98.pdf|041|top bound and bottom bound|n|N possible; small horizontal n-like stroke|medium|
|98.pdf|041|corollary cancelled words|on ait pour tt|crossed and faint|low|
|98.pdf|041|F prime definition|F times_S S prime|base subscript overwritten; tensor vs times appears as cross|medium|
|98.pdf|042|upper crossed hypothesis|F possède une résolution; libre de type fini|three overlapping revisions; words and attachment low confidence|low|
|98.pdf|042|upper margin label|F-résolution|possible F-complexe; word after F unclear|low|
|98.pdf|042|left margin bound|<=N+1 and <=N|both visible; chronological layering uncertain|low|
|98.pdf|042|left middle cancellation|L_N est de présentation finie; Hom arguments N/G|many overwritten letters and indices; best readings marked in place|low|
|98.pdf|042|main lower revised complex|libres de type fini en tous degrés; acyclique en dim<=N|superimposed text; attachment of inserts provisional|low|
|98.pdf|042|bottom deletion and continuation|en degrés; tous degrés|extensive cancellations and image edge|low|
|98.pdf|042|left margin, cokernel|underlined L_N and L_{N+1}; dash|arrowhead not securely visible|medium|
|98.pdf|043|top condition|deleted +1|indecipherable overwritten exponent|low|
|98.pdf|043|first display and K* definition|Hom_A|Hom_B|low|
|98.pdf|043|first display last Hom argument|N'|N|low|
|98.pdf|043|cancelled bracket|il suffit [en fait?] que N soit; 7 words unreadable|remaining cancelled clause|low|
|98.pdf|043|middle before le conoyau|deleted que||low|
|98.pdf|043|K exponent|deleted N+1, then N||low|
|98.pdf|043|after en tt degré|deleted cqfd||low|
|98.pdf|043|cancelled top bracket|en fait|faint crossed words|low|
|98.pdf|043|second identity|dash|equals sign|medium|
|98.pdf|044|second title insertion|à degrés finis bornés|colon-like initial mark|medium|
|98.pdf|044|end of second title|le; one unreadable word|possibly a phrase about generalisation|low|
|98.pdf|044|Prop 2 cancellation|S réduit||low|
|98.pdf|044|Prop 2 quoted term|virtuelles||low|
|98.pdf|044|Cor 1 cancellations|L before Tors; n after locaux|obliterated symbols|low|
|98.pdf|044|Prop 7 and final corollary subscript|O_X,f|e_X,f|medium|
|98.pdf|044|Proposition 5|dash|arrow|medium|

## Complete in-text doubt index

Every occurrence of `\unsure` and `\illegible` in the final page fragments is listed, including repetitions and marked deletions. Locations are LaTeX source lines, which are stable locators rather than claims about the manuscript lineation. The conservative low confidence below means that the particular occurrence remains unresolved; the contextual register above gives more differentiated confidence where a comparison warrants it.

| File | Scan | Fragment line | Reading | Alternative / unresolved extent | Confidence |
|---|---|---|---|---|---|
|98.pdf|002|4|Formalisation|Formulation|low|
|98.pdf|002|8|P|reading uncertain; no secure alternative|low|
|98.pdf|003|10|1_A|reading uncertain; no secure alternative|low|
|98.pdf|003|10|\cdot\cdot|reading uncertain; no secure alternative|low|
|98.pdf|003|12|0|reading uncertain; no secure alternative|low|
|98.pdf|003|14|\}|reading uncertain; no secure alternative|low|
|98.pdf|003|14|\cdot|reading uncertain; no secure alternative|low|
|98.pdf|003|17|\Leftarrow|\leftarrow|low|
|98.pdf|003|19|Endomorphismes|reading uncertain; no secure alternative|low|
|98.pdf|003|19|commutent|reading uncertain; no secure alternative|low|
|98.pdf|003|19|$\bigwedge$|reading uncertain; no secure alternative|low|
|98.pdf|003|19|stable|reading uncertain; no secure alternative|low|
|98.pdf|003|22|n|reading uncertain; no secure alternative|low|
|98.pdf|003|25|\operatorname{Cart}|reading uncertain; no secure alternative|low|
|98.pdf|003|35|X|reading uncertain; no secure alternative|low|
|98.pdf|003|35|X|reading uncertain; no secure alternative|low|
|98.pdf|003|39|i|reading uncertain; no secure alternative|low|
|98.pdf|004|7|x|\varkappa|low|
|98.pdf|004|7|x|\varkappa|low|
|98.pdf|004|13|x|\varkappa|low|
|98.pdf|004|13|x|\varkappa|low|
|98.pdf|004|13|x|\varkappa|low|
|98.pdf|004|13|x|\varkappa|low|
|98.pdf|004|13|x|\varkappa|low|
|98.pdf|004|13|x|\varkappa|low|
|98.pdf|004|13|x|\varkappa|low|
|98.pdf|004|13|x|\varkappa|low|
|98.pdf|004|17|x|\varkappa|low|
|98.pdf|004|17|x|\varkappa|low|
|98.pdf|005|5|\leftarrow|reading uncertain; no secure alternative|low|
|98.pdf|005|11|Q|reading uncertain; no secure alternative|low|
|98.pdf|005|18|\alpha_{(r)}|\alpha_r|low|
|98.pdf|005|22|u_S^r|G_S^r|low|
|98.pdf|005|30|F|reading uncertain; no secure alternative|low|
|98.pdf|005|33|(rs)|reading uncertain; no secure alternative|low|
|98.pdf|005|39|G|reading uncertain; no secure alternative|low|
|98.pdf|005|44|Y|reading uncertain; no secure alternative|low|
|98.pdf|007|11|r|n|low|
|98.pdf|007|18|\operatorname{Cor}|\operatorname{Cn}|low|
|98.pdf|007|19|\operatorname{Cor}|\operatorname{Cn}|low|
|98.pdf|007|19|u|reading uncertain; no secure alternative|low|
|98.pdf|007|21|comm. polyp.|reading uncertain; no secure alternative|low|
|98.pdf|007|21|comm|reading uncertain; no secure alternative|low|
|98.pdf|007|24|\operatorname{Cor}|\operatorname{Cn}|low|
|98.pdf|007|24|\operatorname{Cor}|\operatorname{Cn}|low|
|98.pdf|007|29|\operatorname{Cor}|\operatorname{Cn}|low|
|98.pdf|007|29|F|reading uncertain; no secure alternative|low|
|98.pdf|007|29|\oplus|reading uncertain; no secure alternative|low|
|98.pdf|007|30|\iota|reading uncertain; no secure alternative|low|
|98.pdf|007|30|S|reading uncertain; no secure alternative|low|
|98.pdf|007|30|\operatorname{Cor}|\operatorname{Cn}|low|
|98.pdf|007|30|\times|reading uncertain; no secure alternative|low|
|98.pdf|007|30|\operatorname{Cor}|\operatorname{Cn}|low|
|98.pdf|007|32|\text{polyp.}|reading uncertain; no secure alternative|low|
|98.pdf|007|36|\text{Cas du}|reading uncertain; no secure alternative|low|
|98.pdf|007|36|*|reading uncertain; no secure alternative|low|
|98.pdf|007|37|rs|reading uncertain; no secure alternative|low|
|98.pdf|007|47|r|reading uncertain; no secure alternative|low|
|98.pdf|007|47|morphisme|reading uncertain; no secure alternative|low|
|98.pdf|007|48|morphisme|reading uncertain; no secure alternative|low|
|98.pdf|007|49|f|reading uncertain; no secure alternative|low|
|98.pdf|007|49|morphisme|reading uncertain; no secure alternative|low|
|98.pdf|007|50|morphisme|reading uncertain; no secure alternative|low|
|98.pdf|007|51|soit comm.|reading uncertain; no secure alternative|low|
|98.pdf|007|53|tels que|reading uncertain; no secure alternative|low|
|98.pdf|007|59|rs|reading uncertain; no secure alternative|low|
|98.pdf|007|59|\gamma|reading uncertain; no secure alternative|low|
|98.pdf|007|62|commutatif|reading uncertain; no secure alternative|low|
|98.pdf|008|19|\text{\uline{$R$}}|\text{\uline{$F$}}|low|
|98.pdf|009|8|rs|reading uncertain; no secure alternative|low|
|98.pdf|009|9|rs|reading uncertain; no secure alternative|low|
|98.pdf|009|16|d'où|reading uncertain; no secure alternative|low|
|98.pdf|009|17|G_Y|reading uncertain; no secure alternative|low|
|98.pdf|009|17|r|reading uncertain; no secure alternative|low|
|98.pdf|009|19|_Y|reading uncertain; no secure alternative|low|
|98.pdf|009|21|morphisme|reading uncertain; no secure alternative|low|
|98.pdf|009|21|rendant commutatif|reading uncertain; no secure alternative|low|
|98.pdf|009|23|\mathrm{can.}\varphi_Y|reading uncertain; no secure alternative|low|
|98.pdf|009|23|\varphi|reading uncertain; no secure alternative|low|
|98.pdf|009|24|G'|reading uncertain; no secure alternative|low|
|98.pdf|009|24|_Y|reading uncertain; no secure alternative|low|
|98.pdf|009|31|lié par|reading uncertain; no secure alternative|low|
|98.pdf|009|36|par suite|reading uncertain; no secure alternative|low|
|98.pdf|009|42|X|Y|low|
|98.pdf|010|9|x|\varkappa|low|
|98.pdf|010|9|x|\varkappa|low|
|98.pdf|010|9|x|\varkappa|low|
|98.pdf|010|9|x|\varkappa|low|
|98.pdf|010|9|x|\varkappa|low|
|98.pdf|010|9|x|\varkappa|low|
|98.pdf|010|9|x|\varkappa|low|
|98.pdf|010|9|x|\varkappa|low|
|98.pdf|010|9|x|\varkappa|low|
|98.pdf|010|9|x|\varkappa|low|
|98.pdf|010|9|x|\varkappa|low|
|98.pdf|010|9|x|\varkappa|low|
|98.pdf|010|9|x|\varkappa|low|
|98.pdf|010|9|x|\varkappa|low|
|98.pdf|010|9|x|\varkappa|low|
|98.pdf|011|3|normés|normants|low|
|98.pdf|011|5|où les sommes finies existent|reading uncertain; no secure alternative|low|
|98.pdf|011|5|morphismes normés|reading uncertain; no secure alternative|low|
|98.pdf|011|11|X\times_Y|reading uncertain; no secure alternative|low|
|98.pdf|011|13|existence|reading uncertain; no secure alternative|low|
|98.pdf|011|13|la|reading uncertain; no secure alternative|low|
|98.pdf|011|13|\illegible{1}|estimated number of unreadable words: 1|low|
|98.pdf|011|13|\prod|reading uncertain; no secure alternative|low|
|98.pdf|011|13|\coprod|reading uncertain; no secure alternative|low|
|98.pdf|011|13|compatible à la formation de|reading uncertain; no secure alternative|low|
|98.pdf|011|13|sommes|reading uncertain; no secure alternative|low|
|98.pdf|011|15|tout|reading uncertain; no secure alternative|low|
|98.pdf|011|15|\mathfrak{S}_n|\mathcal{S}_n|low|
|98.pdf|011|15|et est comp. aux changements de base|reading uncertain; no secure alternative|low|
|98.pdf|011|15|!|?|low|
|98.pdf|011|17|Il est clair que|reading uncertain; no secure alternative|low|
|98.pdf|011|28|un|reading uncertain; no secure alternative|low|
|98.pdf|011|28|fini|reading uncertain; no secure alternative|low|
|98.pdf|011|28|se calcule|reading uncertain; no secure alternative|low|
|98.pdf|011|28|r=\deg(X/Y)|reading uncertain; no secure alternative|low|
|98.pdf|011|28|A|reading uncertain; no secure alternative|low|
|98.pdf|011|29|deux|reading uncertain; no secure alternative|low|
|98.pdf|011|29|\illegible{3}|estimated number of unreadable words: 3|low|
|98.pdf|011|30|\deg(X/Y)^n/G|reading uncertain; no secure alternative|low|
|98.pdf|011|32|tout|reading uncertain; no secure alternative|low|
|98.pdf|011|32|sur|reading uncertain; no secure alternative|low|
|98.pdf|011|34|\operatorname{Cor}|\operatorname{Cn}|low|
|98.pdf|011|34|\operatorname{Cor}|\operatorname{Cn}|low|
|98.pdf|011|36|noté|reading uncertain; no secure alternative|low|
|98.pdf|011|38|\operatorname{Cor}|\operatorname{Cn}|low|
|98.pdf|012|6|\operatorname{Cor}|\operatorname{Cn}|low|
|98.pdf|012|6|\longrightarrow|reading uncertain; no secure alternative|low|
|98.pdf|012|6|\operatorname{Cor}|\operatorname{Cn}|low|
|98.pdf|012|6|\longrightarrow|reading uncertain; no secure alternative|low|
|98.pdf|012|6|\operatorname{Cor}|\operatorname{Cn}|low|
|98.pdf|012|6|Y|reading uncertain; no secure alternative|low|
|98.pdf|012|7|X|reading uncertain; no secure alternative|low|
|98.pdf|012|12|\operatorname{Cor}|\operatorname{Cn}|low|
|98.pdf|012|12|\operatorname{Cor}|\operatorname{Cn}|low|
|98.pdf|012|14|\operatorname{Cor}|\operatorname{Cn}|low|
|98.pdf|012|15|\operatorname{Cor}|\operatorname{Cn}|low|
|98.pdf|012|19|X|reading uncertain; no secure alternative|low|
|98.pdf|012|21|\Pi|reading uncertain; no secure alternative|low|
|98.pdf|012|23|d'injection|d'immersion|low|
|98.pdf|012|25|\operatorname{Cor}|\operatorname{Cn}|low|
|98.pdf|012|25|\operatorname{Cor}|\operatorname{Cn}|low|
|98.pdf|012|25|\operatorname{Cor}|\operatorname{Cn}|low|
|98.pdf|012|29|$r$ tel que pour $\forall$|reading uncertain; no secure alternative|low|
|98.pdf|012|29|il y a|reading uncertain; no secure alternative|low|
|98.pdf|012|29|\illegible{2}|estimated number of unreadable words: 2|low|
|98.pdf|012|29|et|reading uncertain; no secure alternative|low|
|98.pdf|012|29|G|H|low|
|98.pdf|012|29|des $r$-uplets|reading uncertain; no secure alternative|low|
|98.pdf|012|29|éléments|reading uncertain; no secure alternative|low|
|98.pdf|012|29|Alors|reading uncertain; no secure alternative|low|
|98.pdf|012|29|il|reading uncertain; no secure alternative|low|
|98.pdf|012|29|(image|reading uncertain; no secure alternative|low|
|98.pdf|012|29|fonctorielle|reading uncertain; no secure alternative|low|
|98.pdf|012|29|i.e.|reading uncertain; no secure alternative|low|
|98.pdf|012|29|un|reading uncertain; no secure alternative|low|
|98.pdf|012|29|hom|reading uncertain; no secure alternative|low|
|98.pdf|013|3|\operatorname{Cor}|\operatorname{Cn}|low|
|98.pdf|013|5|déduire|reading uncertain; no secure alternative|low|
|98.pdf|013|5|galoisiennes|reading uncertain; no secure alternative|low|
|98.pdf|013|5|spéciales|reading uncertain; no secure alternative|low|
|98.pdf|013|5|par un autre|reading uncertain; no secure alternative|low|
|98.pdf|013|7|bon|reading uncertain; no secure alternative|low|
|98.pdf|013|7|qu. coh.|reading uncertain; no secure alternative|low|
|98.pdf|013|7|d'algèbres|reading uncertain; no secure alternative|low|
|98.pdf|013|7|un|reading uncertain; no secure alternative|low|
|98.pdf|013|7|\operatorname{Cor}|\operatorname{Cn}|low|
|98.pdf|013|9|Variantes|reading uncertain; no secure alternative|low|
|98.pdf|013|9|non ramifiés|reading uncertain; no secure alternative|low|
|98.pdf|013|9|\illegible{2}|estimated number of unreadable words: 2|low|
|98.pdf|014|3|\Gamma|G|low|
|98.pdf|014|3|\illegible{1}|estimated number of unreadable words: 1|low|
|98.pdf|014|3|\illegible{2}|estimated number of unreadable words: 2|low|
|98.pdf|014|3|l'objet|le couple|low|
|98.pdf|014|3|pour|reading uncertain; no secure alternative|low|
|98.pdf|014|5|à développer|reading uncertain; no secure alternative|low|
|98.pdf|014|7|C'|E'|low|
|98.pdf|014|7|id : fait aussi sur|reading uncertain; no secure alternative|low|
|98.pdf|014|7|compos|reading uncertain; no secure alternative|low|
|98.pdf|015|19|-1|-u|low|
|98.pdf|016|6|E|reading uncertain; no secure alternative|low|
|98.pdf|016|6|X|reading uncertain; no secure alternative|low|
|98.pdf|016|8|étant donné|reading uncertain; no secure alternative|low|
|98.pdf|016|8|donnée|reading uncertain; no secure alternative|low|
|98.pdf|016|8|?|reading uncertain; no secure alternative|low|
|98.pdf|016|16|trivialt|reading uncertain; no secure alternative|low|
|98.pdf|016|16|lim|reading uncertain; no secure alternative|low|
|98.pdf|016|16|foncteurs|reading uncertain; no secure alternative|low|
|98.pdf|018|3|*|reading uncertain; no secure alternative|low|
|98.pdf|018|4|s'apparente|reading uncertain; no secure alternative|low|
|98.pdf|018|5|pré|reading uncertain; no secure alternative|low|
|98.pdf|018|7|R|reading uncertain; no secure alternative|low|
|98.pdf|018|9|permuter aux|reading uncertain; no secure alternative|low|
|98.pdf|018|11|Preuve.|reading uncertain; no secure alternative|low|
|98.pdf|018|11|utiliser|reading uncertain; no secure alternative|low|
|98.pdf|018|13|$H^0$|reading uncertain; no secure alternative|low|
|98.pdf|018|19|simplexe|reading uncertain; no secure alternative|low|
|98.pdf|018|19|simple|reading uncertain; no secure alternative|low|
|98.pdf|018|19|0|reading uncertain; no secure alternative|low|
|98.pdf|019|9|\mathfrak{o}|v|low|
|98.pdf|019|25|prop|reading uncertain; no secure alternative|low|
|98.pdf|019|28|utile au cas non singulier?|reading uncertain; no secure alternative|low|
|98.pdf|019|29|Nouveau!|Revoir!|low|
|98.pdf|020|7|identités|reading uncertain; no secure alternative|low|
|98.pdf|020|8|valeur en|reading uncertain; no secure alternative|low|
|98.pdf|020|8|du foncteur dérivé|reading uncertain; no secure alternative|low|
|98.pdf|020|8|hyperfaisceaux|reading uncertain; no secure alternative|low|
|98.pdf|020|8|hyperfaisceaux|reading uncertain; no secure alternative|low|
|98.pdf|020|8|il en résulte immédiatement|reading uncertain; no secure alternative|low|
|98.pdf|020|13|transforme|reading uncertain; no secure alternative|low|
|98.pdf|020|25|\Phi|reading uncertain; no secure alternative|low|
|98.pdf|020|25|\natural|n|low|
|98.pdf|020|25|\Phi|reading uncertain; no secure alternative|low|
|98.pdf|022|6|\bullet|0|low|
|98.pdf|022|10|\mathcal H|reading uncertain; no secure alternative|low|
|98.pdf|022|11|\longrightarrow|reading uncertain; no secure alternative|low|
|98.pdf|022|15|\longrightarrow|reading uncertain; no secure alternative|low|
|98.pdf|022|18|\mathrm{gal}|reading uncertain; no secure alternative|low|
|98.pdf|022|18|\mathrm{gal}|reading uncertain; no secure alternative|low|
|98.pdf|022|19|\vdash|t|low|
|98.pdf|023|16|\mathfrak{o}|reading uncertain; no secure alternative|low|
|98.pdf|024|5|application|reading uncertain; no secure alternative|low|
|98.pdf|024|11|Čech|reading uncertain; no secure alternative|low|
|98.pdf|024|15|\text{d'où}|reading uncertain; no secure alternative|low|
|98.pdf|024|19|trivial|reading uncertain; no secure alternative|low|
|98.pdf|024|22|G|reading uncertain; no secure alternative|low|
|98.pdf|024|23|G|reading uncertain; no secure alternative|low|
|98.pdf|024|27|\text{d'où}|reading uncertain; no secure alternative|low|
|98.pdf|024|29|p|reading uncertain; no secure alternative|low|
|98.pdf|024|29|G|reading uncertain; no secure alternative|low|
|98.pdf|024|31|via celles de|reading uncertain; no secure alternative|low|
|98.pdf|024|37|\parallel|reading uncertain; no secure alternative|low|
|98.pdf|024|37|Čech|reading uncertain; no secure alternative|low|
|98.pdf|024|41|\text{d'où}|reading uncertain; no secure alternative|low|
|98.pdf|025|8|c|reading uncertain; no secure alternative|low|
|98.pdf|025|9|séparé|sépare|low|
|98.pdf|027|3|choses|reading uncertain; no secure alternative|low|
|98.pdf|027|5|l'un|reading uncertain; no secure alternative|low|
|98.pdf|027|5|\simeq|reading uncertain; no secure alternative|low|
|98.pdf|027|5|dont|reading uncertain; no secure alternative|low|
|98.pdf|027|5|dimension|reading uncertain; no secure alternative|low|
|98.pdf|027|8|$L=\underline{O}^k$|reading uncertain; no secure alternative|low|
|98.pdf|027|9|récure|reading uncertain; no secure alternative|low|
|98.pdf|027|9|ses|reading uncertain; no secure alternative|low|
|98.pdf|027|10|l\geq1|reading uncertain; no secure alternative|low|
|98.pdf|027|11|existe une|reading uncertain; no secure alternative|low|
|98.pdf|027|11|\illegible{3}|estimated number of unreadable words: 3|low|
|98.pdf|027|11|pour|reading uncertain; no secure alternative|low|
|98.pdf|027|11|énoncés|reading uncertain; no secure alternative|low|
|98.pdf|027|11|ci-dessus|reading uncertain; no secure alternative|low|
|98.pdf|027|11|rien|reading uncertain; no secure alternative|low|
|98.pdf|027|11|à faire|reading uncertain; no secure alternative|low|
|98.pdf|027|11|l'union de|l'un des|low|
|98.pdf|027|11|collections|reading uncertain; no secure alternative|low|
|98.pdf|027|11|sont|reading uncertain; no secure alternative|low|
|98.pdf|027|11|limité|limitée|low|
|98.pdf|027|14|\operatorname{im}|reading uncertain; no secure alternative|low|
|98.pdf|027|14|\text{cst.}|reading uncertain; no secure alternative|low|
|98.pdf|027|14|résu|reading uncertain; no secure alternative|low|
|98.pdf|027|14|a|reading uncertain; no secure alternative|low|
|98.pdf|027|14|il en sera|reading uncertain; no secure alternative|low|
|98.pdf|027|14|images|reading uncertain; no secure alternative|low|
|98.pdf|027|14|variables|reading uncertain; no secure alternative|low|
|98.pdf|027|14|\iota|reading uncertain; no secure alternative|low|
|98.pdf|028|3|E|L|low|
|98.pdf|028|3|nombre|reading uncertain; no secure alternative|low|
|98.pdf|028|3|nb|reading uncertain; no secure alternative|low|
|98.pdf|028|3|Récurrence|reading uncertain; no secure alternative|low|
|98.pdf|028|5|sur|reading uncertain; no secure alternative|low|
|98.pdf|028|5|a)|4°)|low|
|98.pdf|028|5|Z|\mathbf Z|low|
|98.pdf|028|5|fixé|reading uncertain; no secure alternative|low|
|98.pdf|028|6|\longrightarrow|reading uncertain; no secure alternative|low|
|98.pdf|028|6|P^n|reading uncertain; no secure alternative|low|
|98.pdf|028|6|\longrightarrow|reading uncertain; no secure alternative|low|
|98.pdf|028|6|T|reading uncertain; no secure alternative|low|
|98.pdf|028|7|de|reading uncertain; no secure alternative|low|
|98.pdf|028|8|n|reading uncertain; no secure alternative|low|
|98.pdf|028|8|T|reading uncertain; no secure alternative|low|
|98.pdf|028|11|On|reading uncertain; no secure alternative|low|
|98.pdf|028|11|F|reading uncertain; no secure alternative|low|
|98.pdf|028|13|donc|reading uncertain; no secure alternative|low|
|98.pdf|028|13|n'a que les points|reading uncertain; no secure alternative|low|
|98.pdf|028|13|génériques de dim|reading uncertain; no secure alternative|low|
|98.pdf|028|16|pol.|reading uncertain; no secure alternative|low|
|98.pdf|028|20|les uns sont tous|reading uncertain; no secure alternative|low|
|98.pdf|029|3|de|reading uncertain; no secure alternative|low|
|98.pdf|029|3|K|k|low|
|98.pdf|029|15|G|reading uncertain; no secure alternative|low|
|98.pdf|029|15|S|reading uncertain; no secure alternative|low|
|98.pdf|029|15|S|reading uncertain; no secure alternative|low|
|98.pdf|029|23|alors|reading uncertain; no secure alternative|low|
|98.pdf|029|23|deux de type fini|reading uncertain; no secure alternative|low|
|98.pdf|030|5|composée|commune|low|
|98.pdf|030|7|objets|reading uncertain; no secure alternative|low|
|98.pdf|030|8|que|reading uncertain; no secure alternative|low|
|98.pdf|030|8|\mathcal U|reading uncertain; no secure alternative|low|
|98.pdf|030|8|que|reading uncertain; no secure alternative|low|
|98.pdf|030|8|alors|choisi|low|
|98.pdf|030|8|\Phi|\mathrm{Cl}|low|
|98.pdf|030|10|ens|reading uncertain; no secure alternative|low|
|98.pdf|030|10|\Phi|\mathrm{Cl}|low|
|98.pdf|030|10|/k|reading uncertain; no secure alternative|low|
|98.pdf|030|13|après|reading uncertain; no secure alternative|low|
|98.pdf|030|14|l'ens|reading uncertain; no secure alternative|low|
|98.pdf|030|14|\Phi|\mathrm{Cl}|low|
|98.pdf|031|3|\Phi|\mathrm{Cl}|low|
|98.pdf|031|3|ident|reading uncertain; no secure alternative|low|
|98.pdf|031|3|suivante :|reading uncertain; no secure alternative|low|
|98.pdf|031|3|comme|reading uncertain; no secure alternative|low|
|98.pdf|031|7|\Phi|\mathrm{Cl}|low|
|98.pdf|031|9|n|h|low|
|98.pdf|031|9|\mathfrak P|\Pi|low|
|98.pdf|031|9|$n$-uple|reading uncertain; no secure alternative|low|
|98.pdf|031|9|alg.|reading uncertain; no secure alternative|low|
|98.pdf|031|10|Se donner|reading uncertain; no secure alternative|low|
|98.pdf|031|10|Y|reading uncertain; no secure alternative|low|
|98.pdf|031|10|donné|reading uncertain; no secure alternative|low|
|98.pdf|031|10|donné|reading uncertain; no secure alternative|low|
|98.pdf|031|10|pas!|reading uncertain; no secure alternative|low|
|98.pdf|031|10|un|reading uncertain; no secure alternative|low|
|98.pdf|031|10|fonction|foncteur|low|
|98.pdf|031|10|\Psi|reading uncertain; no secure alternative|low|
|98.pdf|031|10|\Phi|reading uncertain; no secure alternative|low|
|98.pdf|031|10|compatibles|reading uncertain; no secure alternative|low|
|98.pdf|031|10|déf|reading uncertain; no secure alternative|low|
|98.pdf|031|10|\illegible{2}|estimated number of unreadable words: 2|low|
|98.pdf|031|10|aux extensions de|reading uncertain; no secure alternative|low|
|98.pdf|031|10|base|reading uncertain; no secure alternative|low|
|98.pdf|032|4|généraliser|reading uncertain; no secure alternative|low|
|98.pdf|032|6|i|n|low|
|98.pdf|032|6|$T$|reading uncertain; no secure alternative|low|
|98.pdf|032|11|\Phi|\mathrm{Cl}|low|
|98.pdf|032|11|\Phi|\mathrm{Cl}|low|
|98.pdf|032|13|introduire|reading uncertain; no secure alternative|low|
|98.pdf|032|13|prop.|reading uncertain; no secure alternative|low|
|98.pdf|032|15|suite|reading uncertain; no secure alternative|low|
|98.pdf|032|16|proposition|reading uncertain; no secure alternative|low|
|98.pdf|033|5|autres|reading uncertain; no secure alternative|low|
|98.pdf|033|5|\Phi|\mathrm{Cl}|low|
|98.pdf|033|5|réunit|somme|low|
|98.pdf|033|5|\Phi|\mathrm{Cl}|low|
|98.pdf|033|10|sur|les|low|
|98.pdf|033|10|fibres|reading uncertain; no secure alternative|low|
|98.pdf|033|10|schémas|faisceaux|low|
|98.pdf|033|10|\illegible{2}|estimated number of unreadable words: 2|low|
|98.pdf|033|10|qu'on a des|reading uncertain; no secure alternative|low|
|98.pdf|033|10|X_i-\alpha|reading uncertain; no secure alternative|low|
|98.pdf|033|10|réunion|reading uncertain; no secure alternative|low|
|98.pdf|033|12|prendre|reading uncertain; no secure alternative|low|
|98.pdf|034|5|on peut regarder un argument|reading uncertain; no secure alternative|low|
|98.pdf|034|7|former|reading uncertain; no secure alternative|low|
|98.pdf|034|7|en ce qui|reading uncertain; no secure alternative|low|
|98.pdf|034|17|propre|reading uncertain; no secure alternative|low|
|98.pdf|034|23|\illegible{2}|estimated number of unreadable words: 2|low|
|98.pdf|034|27|quotients|reading uncertain; no secure alternative|low|
|98.pdf|034|27|\chi|reading uncertain; no secure alternative|low|
|98.pdf|034|29|\illegible{8}|estimated number of unreadable words: 8|low|
|98.pdf|035|9|F|reading uncertain; no secure alternative|low|
|98.pdf|035|24|composée|reading uncertain; no secure alternative|low|
|98.pdf|035|24|-|\to|low|
|98.pdf|035|24|-|\to|low|
|98.pdf|035|26|s''|s'''|low|
|98.pdf|035|30|Alors|reading uncertain; no secure alternative|low|
|98.pdf|035|37|S'|S''|low|
|98.pdf|035|39|parties loc. fermées|reading uncertain; no secure alternative|low|
|98.pdf|035|41|S'|S''|low|
|98.pdf|036|3|-|\to|low|
|98.pdf|036|12|plats puis|reading uncertain; no secure alternative|low|
|98.pdf|036|19|lemme|reading uncertain; no secure alternative|low|
|98.pdf|036|19|peuvent|reading uncertain; no secure alternative|low|
|98.pdf|036|19|être|reading uncertain; no secure alternative|low|
|98.pdf|036|19|utilisable|valable|low|
|98.pdf|036|21|lemme|reading uncertain; no secure alternative|low|
|98.pdf|037|5|T'_i|T'|low|
|98.pdf|037|9|sous-faisceaux|reading uncertain; no secure alternative|low|
|98.pdf|037|9|K_i|reading uncertain; no secure alternative|low|
|98.pdf|037|9|et les|reading uncertain; no secure alternative|low|
|98.pdf|037|9|donc|reading uncertain; no secure alternative|low|
|98.pdf|037|9|sont|reading uncertain; no secure alternative|low|
|98.pdf|037|12|i|reading uncertain; no secure alternative|low|
|98.pdf|037|13|H|B|low|
|98.pdf|037|17|finis|reading uncertain; no secure alternative|low|
|98.pdf|037|19|prenant|reading uncertain; no secure alternative|low|
|98.pdf|037|19|\illegible{1}|estimated number of unreadable words: 1|low|
|98.pdf|037|19|\illegible{1}|estimated number of unreadable words: 1|low|
|98.pdf|038|3|on a|reading uncertain; no secure alternative|low|
|98.pdf|038|18|est un|reading uncertain; no secure alternative|low|
|98.pdf|038|18|l'aboutissement|reading uncertain; no secure alternative|low|
|98.pdf|038|19|D'une|reading uncertain; no secure alternative|low|
|98.pdf|038|19|ab. = le dernier,|ab. le dernier,|low|
|98.pdf|039|4|désignant par|reading uncertain; no secure alternative|low|
|98.pdf|039|6|U'|reading uncertain; no secure alternative|low|
|98.pdf|039|6|U'|reading uncertain; no secure alternative|low|
|98.pdf|039|6|U'|reading uncertain; no secure alternative|low|
|98.pdf|039|17|S|Y|low|
|98.pdf|039|23|Peut-on faire plus ?|reading uncertain; no secure alternative|low|
|98.pdf|040|3|Preuve|reading uncertain; no secure alternative|low|
|98.pdf|040|7|A'|reading uncertain; no secure alternative|low|
|98.pdf|040|11|\otimes_B B'|reading uncertain; no secure alternative|low|
|98.pdf|040|13|\alpha|*|low|
|98.pdf|040|21|établie|reading uncertain; no secure alternative|low|
|98.pdf|040|24|M'|M'_1|low|
|98.pdf|040|30|au lieu de|reading uncertain; no secure alternative|low|
|98.pdf|041|6|n|N|low|
|98.pdf|041|8|on ait pour tt|reading uncertain; no secure alternative|low|
|98.pdf|041|15|S|reading uncertain; no secure alternative|low|
|98.pdf|041|19|n|N|low|
|98.pdf|042|10|ainsi que tt|reading uncertain; no secure alternative|low|
|98.pdf|042|10|possède une résolution|reading uncertain; no secure alternative|low|
|98.pdf|042|10|libre|reading uncertain; no secure alternative|low|
|98.pdf|042|10|de type fini|reading uncertain; no secure alternative|low|
|98.pdf|042|10|libre de type fini|reading uncertain; no secure alternative|low|
|98.pdf|042|16|$F$-résolution|reading uncertain; no secure alternative|low|
|98.pdf|042|16|N|reading uncertain; no secure alternative|low|
|98.pdf|042|16|libres|reading uncertain; no secure alternative|low|
|98.pdf|042|16|tout|reading uncertain; no secure alternative|low|
|98.pdf|042|16|N+1|reading uncertain; no secure alternative|low|
|98.pdf|042|16|\illegible{2}|estimated number of unreadable words: 2|low|
|98.pdf|042|16|est de présentation finie|reading uncertain; no secure alternative|low|
|98.pdf|042|16|pour que|reading uncertain; no secure alternative|low|
|98.pdf|042|16|N+1|reading uncertain; no secure alternative|low|
|98.pdf|042|16|N|G|low|
|98.pdf|042|16|N|G|low|
|98.pdf|042|16|soit aussi|reading uncertain; no secure alternative|low|
|98.pdf|042|16|N|G|low|
|98.pdf|042|18|-|\longrightarrow|low|
|98.pdf|042|24|libres de type fini en tous degrés|reading uncertain; no secure alternative|low|
|98.pdf|042|24|plats et une résolution|reading uncertain; no secure alternative|low|
|98.pdf|042|24|plate|reading uncertain; no secure alternative|low|
|98.pdf|042|24|résolution supposée|reading uncertain; no secure alternative|low|
|98.pdf|042|24|par|reading uncertain; no secure alternative|low|
|98.pdf|042|24|$M$|reading uncertain; no secure alternative|low|
|98.pdf|042|24|plats|reading uncertain; no secure alternative|low|
|98.pdf|042|24|est une résolution|reading uncertain; no secure alternative|low|
|98.pdf|042|24|en dim|reading uncertain; no secure alternative|low|
|98.pdf|042|28|libre|reading uncertain; no secure alternative|low|
|98.pdf|042|28|en degrés|reading uncertain; no secure alternative|low|
|98.pdf|042|28|tous degrés|reading uncertain; no secure alternative|low|
|98.pdf|042|28|\illegible{1}|estimated number of unreadable words: 1|low|
|98.pdf|043|3|+1|reading uncertain; no secure alternative|low|
|98.pdf|043|5|A|B|low|
|98.pdf|043|5|N'|N|low|
|98.pdf|043|7|A|B|low|
|98.pdf|043|7|en fait|reading uncertain; no secure alternative|low|
|98.pdf|043|7|soit|reading uncertain; no secure alternative|low|
|98.pdf|043|7|\illegible{7}|estimated number of unreadable words: 7|low|
|98.pdf|043|12|-|=|low|
|98.pdf|043|15|que|reading uncertain; no secure alternative|low|
|98.pdf|043|15|N+1|reading uncertain; no secure alternative|low|
|98.pdf|043|19|cqfd|reading uncertain; no secure alternative|low|
|98.pdf|044|6|à|reading uncertain; no secure alternative|low|
|98.pdf|044|6|le|reading uncertain; no secure alternative|low|
|98.pdf|044|6|\illegible{1}|estimated number of unreadable words: 1|low|
|98.pdf|044|11|$S$ réduit|reading uncertain; no secure alternative|low|
|98.pdf|044|11|virtuelles|reading uncertain; no secure alternative|low|
|98.pdf|044|17|-|\longrightarrow|low|
|98.pdf|044|19|$L$|reading uncertain; no secure alternative|low|
|98.pdf|044|19|$n$|reading uncertain; no secure alternative|low|
|98.pdf|044|31|O_X|e_X|low|
|98.pdf|044|33|O_X|e_X|low|

Total marked occurrences indexed: 464.

## Abbreviations (expansions are hypotheses, never substituted in the transcription)

| Written form | Proposed expansion |
|---|---|
|Cf|confer|
|SGA|Séminaire de géométrie algébrique|
|comm|commutatif|
|cor.|corollaire|
|cf.|confer|
|Ens.|Ensembles (reference abbreviation)|
|Chap. / chap.|Chapitre / chapitre|
|prop.|proposition|
|CST|critère de structure typique (tentative)|
|pr|projection|
|resp.|respectivement|
|mod.|modulo|
|can. / can|canonique|
|comm.|commutatif|
|polyp.|polynomial (tentative; reading itself uncertain)|
|exerc.|exercice|
|diag.|diagramme|
|symm|symmétrique (spelling/abbreviation retained)|
|th.|théorème|
|ss-groupe|sous-groupe|
|comp.|compatible|
|deg|degré|
|card|cardinal|
|i.e.|id est|
|N.B.|nota bene|
|ens|ensemble|
|hom|homomorphisme|
|can|canonique|
|loc.|localement|
|qu. coh.|quasi-cohérent|
|Cl|classe|
|ens.|ensemble|
|op.|opération|
|rég.|régulière|
|trivialt|trivialement|
|lim|limites|
|Chap.|chapitre|
|fonc|fonction|
|prop|proposition|
|supp|support|
|IAG|Introduction à la géométrie algébrique (possible bibliographic abbreviation)|
|qième|q-ième|
|mod|modulo|
|rad|radiciel|
|gal|galoisien|
|Th.|théorème|
|Coro.|corollaire|
|op.|opérations|
|coh.|cohomologie|
|coeff.|coefficient|
|IAG|Introduction à la géométrie algébrique (bibliographic expansion unverified)|
|gén.|générique|
|sup.|supremum|
|hom.|homomorphismes|
|cst.|constant|
|ascend.|ascendante|
|nb|nombre|
|dim|dimension|
|pol.|polynômes|
|Hilb|Hilbert|
|hyp.|hypothèse|
|ext.|extension|
|ss-extension|sous-extension|
|k-hom|k-homomorphismes|
|Chap|chapitre|
|isom.|isomorphisme|
|coh.|cohérents|
|ssi|si et seulement si|
|alg. clos|algébriquement clos|
|Déf|définition|
|él.|éléments|
|tt|tout|
|cl|classe|
|arg|argument|
|ds|dans|
|hom|homomorphismes|
|réd|réduit|
|tte|toute|
|noeth|noethérien|
|op.|opérateur|
|ab.|aboutissement (uncertain)|
|coh.|cohérent|
|isom|isomorphisme|
|coh|cohérents|
|cqfd.|ce qu’il fallait démontrer|
|Prop.|proposition|
|Cor.|corollaire|

## Legibility and limits

The reused typescript is generally clearer than the manuscript, although faint letters, accents, punctuation, mathematical alphabets and typed irregularities still require care. The least secure material is the crowded axiomatic revisions on scans 011–014; the faint and cancelled argument on scan 027; the class notation and diagonal additions on scans 030–034; and the superimposed resolution hypotheses and cancellations on scans 042–043. The final parenthesis in the second heading of scan 044 remains unreadable after enlargement. The contextual register and complete index identify the remaining local uncertainties; neither successful compilation nor mathematical plausibility establishes a reading.

All 43 whole images and both supplied halves were personally read in one transcription stream, without OCR, followed by a second visual audit of each scan. Further enlarged crops were inspected for doubtful passages. Recurring glyphs were compared before the transcription was frozen and before any contextual member contents were opened. The surviving Phi/Cl, Cor/Cn, A/B and prime-count doubts are deliberate; no claim of error-free decipherment is made.
