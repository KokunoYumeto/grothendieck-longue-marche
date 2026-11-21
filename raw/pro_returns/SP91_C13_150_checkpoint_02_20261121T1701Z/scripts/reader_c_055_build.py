import json,os
from pathlib import Path
root=Path('edition').resolve();out=root/'reader_returns'
items=json.loads((root/'scripts/reader_c_055_crop_manifest.json').read_text());cs={n:b for n,b,a in items}
def cp(n):return 'crops/150_scan055_'+n+'.png'
tex=r'''\scanpage{55}
\mspage{23}
avec la structure de stratification cylindrique \inserted{ordonnée}
locale. \deleted{Par exemple}, Une autre façon de
décrire les $\Gamma(d)=\Sigma^{<}(d+1)$, c'est de
prendre la puiss. \deleted{\unsure{sym.}} \inserted{cart. relative} $d$.ième de $\Gamma_0$\deleted{\unsure{$(\varnothing)$}}\inserted{$=\Sigma^{<}(1)$}
sur $\Sigma\ (=\Gamma(\varnothing))$, dont on enlève les images
des puiss. cart. relatives \deleted{\unsure{inférieures}} \inserted{\deleted{$\Gamma'(d)$} des $d'$.ième ($d'<d$)} par les applic\unsure{ns}
$\tfrac12$ simpliciales entre celles ci. Cela donne à priori
les \deleted{\unsure{ens tot.}} suites ordonnées de $d$ germes de
strates de codim $1$ \inserted{en un $=$ point,} \unsure{(mutuel\textsuperscript{t}|\deleted{(mutuel\textsuperscript{t}}} distinctes), \deleted{soit}
$\Gamma'(d)$. On a alors \inserted{$\unsure{\Gamma^{\deleted{'}}(d)|\Gamma(d)}\subset\Gamma'(d)$},
$\Gamma(d)$ est une partie à la fois ouverte et
\unsure{fermée|\deleted{fermée}} de $\Gamma'(d)$, et \deleted{$\Gamma'(d)\unsure{\simeq}$}
\[
(35)\qquad \Gamma'(d)\simeq\unsure{\mathfrak S_d|\mathcal S_d}\times\Gamma(d)
\]
Pour avoir \deleted{la}\inserted{une} structure d'ordre \inserted{total} relative, de
\margin{\deleted{il s'agit de}}
\deleted{\unsure{$\Gamma'(1)$ sur}} $\Gamma_0=\Sigma^{<}(1)$ sur $\Sigma_{\deleted{\unsure{*|0}}}=\Sigma^{<}(0)$, il \deleted{suffit}\inserted{\unsure{uniquement}}
de se donner, \deleted{dans $\Gamma'_1(\unsure{0|2})=\unsure{\Sigma^{<}(0)|\Sigma^{<}(2)}$, $\Gamma'_{1+1}$} dans
$\Gamma_0\times_\Sigma\Gamma_0\setminus\text{diagonale}$, une partie \inserted{(i.e. \unsure{néc.}} ouverte et fermée)
$\Gamma_1$, telle que $\Gamma_1\cup{}^s\Gamma_1=\Gamma_0\times\Gamma_0\setminus\text{diag}$, $\Gamma_1\cap{}^s\Gamma_1=\varnothing$
\margin{$\Gamma_1$ est le graphe de la relation $x<y$}
i.e. une section de $\Gamma_0\times_\Sigma\Gamma_0\setminus\text{diag}$ \unsure{au|\deleted{au}} dessus
\margin{ou une section \deleted{de $\Gamma_0\times_\Sigma\Gamma_0\setminus\unsure{\text{diagonale}|\text{diag}}$}\deleted{de $\operatorname{Sym}^2(\Gamma_0\times_\Sigma\Gamma_0)$}\deleted{de}}
de $\operatorname{Sym}^2_\Sigma(\Gamma_0)^*$ (``choix d'un premier élément parmi deux
éléments distincts), avec la condition de transitivité
\deleted{$\unsure{\text{que }\Gamma_1}$}
\diagram{\begin{tikzcd}[column sep=large,row sep=small]
(36)\quad (\Gamma_1\times_\Sigma\Gamma_0)\cap(\Gamma_0\times_\Sigma\Gamma_1)
 \arrow[r,"{\operatorname{Pr}_{\unsure{13|23}}}"] \arrow[d,phantom,"\cap" description]
 & \Gamma_0\times\Gamma_0 \arrow[d,phantom,"\cup" description]
 & \text{se factorise par }\Gamma_1 \\
\unsure{\Sigma_0|\Gamma_0}\times\Gamma_0\times\Gamma_0 & \Gamma_1 &
\end{tikzcd}}
\margin{54}
'''
ch=[]
def add(place,C,H,fin,ac,ah,kind,cat,m,conf,ev,p,mc=''):
 ch.append(dict(id=f'055-{len(ch)+1:02d}',place=place,C=C,H=H,final=fin,against_C=ac,against_H=ah,kind=kind,error_category=cat,marked_in_H=m,confidence=conf,evidence=ev,crop=cp(p),box=cs[p],mathematical_consequence=mc))
W=('misread word','Words');S=('misread symbol or index','Symbols and indices');O=('omission','Omissions');D=('deletion state','Struck text');A=('abbreviation expanded or spelling modernised','Abbreviations expanded, spelling modernised');T=('text not on the page','Text that is not on the page');R=('readable ink left as '+chr(92)+'ill{}','Readable ink left as illegible');P=('insertion or placement','Insertions put in the wrong place');X=('other','Other')
add('line 1, addition',r'\inserted{\uline{ordonnée}}',r'\add{ordonnée}',r'\inserted{ordonnée}',True,False,*P,False,'high','The line beneath ordonnée continues directly into the V-shaped leader pointing after cylindrique. It is recorded as the insertion leader, without a second independent underline.','p01_ordonne')
add('line 2, after cancelled phrase',r'\deleted{Par exemple}',r'\struck{Par exemple,}',r'\deleted{Par exemple},',True,True,*O,False,'high','A separate comma curves downward beneath the end of exemple. The straight cancellation crosses the words above the comma; the comma is retained outside the deletion because its own stroke remains uncrossed.','p02_par_exemple')
add('line 3, body exponent',r'\Sigma^{<}(d+1)',r'\Sigma^{*}(d+1)',r'\Sigma^{<}(d+1)',False,True,*S,False,'high','The superscript has a left vertex and two short rightward arms, followed by the opening parenthesis; it is the angular body sign.','p03_opening_formula','Preserves the author’s written Γ(d)=Σ^<(d+1).')
add('line 4, ordinal punctuation',r'$d$.ième',r'$d$-ième',r'$d$.ième',False,True,*X,False,'high','A dark point stands after d at the baseline before ième; there is no horizontal hyphen.','p04_cart_relative')
add('line 4, cancelled argument after Γ₀',r'\deleted{\unsure{$(\varnothing)$}}',r'\struck{\ill{}}',r'\deleted{\unsure{$(\varnothing)$}}',False,True,*R,True,'low','The opening and closing parentheses remain, with a heavily overdrawn central slashed-loop-like group. The reading (∅) remains explicitly doubtful.','p05_gamma0_added')
add('line 4, added equality',r'\Sigma^{<}(1)',r'\Sigma^{*}(1)',r'\Sigma^{<}(1)',False,True,*S,False,'high','The raised mark above Σ is the same angular two-arm form used in the body. The argument is the written numeral 1.','p05_gamma0_added','Preserves =Σ^<(1) in the addition attached to Γ₀.')
add('line 5, after closing parenthesis','dont',r'\uncertain{d\'où}','dont',False,True,*W,True,'high','A looped d is followed by low connected o/n strokes and a short terminal upturn; no apostrophe separates an où group.','p06_dont_enleve')
add('line 5, verb','enlève',r'\uncertain{utilise}','enlève',False,True,*W,True,'high','The initial low en is followed by a tall looped l, with the detached accent over the following e and the short final ve strokes.','p06_dont_enleve')
add('line 6, location of upper addition',r'\inserted{$\Gamma\'(d\')$ des $d\'$ième ($d\'<d$)}',r'les images \add{$\Gamma\'(d)$} en dim. ($d\'\le d$) des puiss. cart. relatives',r'relatives \deleted{\unsure{inférieures}} \inserted{\deleted{$\Gamma\'(d)$} des $d\'$.ième ($d\'<d$)}',False,True,*P,False,'high','The long curved leader starts beside the cancelled word after relatives in line 6 and runs beneath the added phrase. The added words are attached there, below the line ending images.','p07_relative_powers')
add('line 6, argument of cancelled added Γ′',r'\Gamma\'(d\')',r'\Gamma\'(d)',r'\Gamma\'(d)',True,False,*S,False,'high','The prime after Γ is visible above its right shoulder. Within the parentheses there is d followed by the closing parenthesis, without a separate prime after d.','p07_relative_powers','Preserves the unprimed argument d in the cancelled added Γ′(d).')
add('line 6, state of added Γ′ expression',r'\inserted{$\Gamma\'(d\')$}',r'\add{$\Gamma\'(d)$}',r'\inserted{\deleted{$\Gamma\'(d)$}}',True,True,*D,False,'high','An independent diagonal stroke crosses the small Γ′(d) from its lower left through the argument. It is separate from the lower curved leader of the surrounding insertion.','p07_relative_powers')
add('line 6, added words after Γ′',r'des $d\'$ième','en dim.',r'des $d\'$.ième',True,True,*W,False,'high','The added phrase has the small des group followed by a large d, a raised prime, a baseline point, and ième. H’s en dim. does not represent these visible letters.','p07_relative_powers')
add('line 6, added inequality',r'd\'<d',r'd\'\le d',r'd\'<d',False,True,*S,False,'high','The relation is one left-angle stroke. No separate lower bar is visible beneath it.','p07_relative_powers','The written range uses the strict sign d′<d; H supplies ≤.')
add('line 6, cancelled word',r'\deleted{inférieures}',r'\struck{définies}',r'\deleted{\unsure{inférieures}}',False,True,*W,False,'medium','The beginning consists of low i/n strokes followed by the long f ascender/descender. The remainder is crossed and compressed; inférieures is retained with explicit doubt.','p07_relative_powers')
add('line 6, final abbreviation',r'applic\unsure{ns}','applications',r'applic\unsure{ns}',False,True,*A,False,'medium','The long p/l group is followed by a curtailed terminal group. The full -ations supplied by H is not separately written; the final ns remains doubtful.','p08_applicns')
add('line 7, two-word form','celles-ci','celles-ci','celles ci',True,True,*T,False,'high','There is a visible blank between the final stroke of celles and the opening c of ci. No hyphen occupies the gap.','p09_half_simplicial')
add('line 7, preposition','à',':','à',False,True,*W,False,'high','A distinct accent stands over the very reduced lower a stroke.','p10_a_priori')
add('line 7, phrase ending','priori',r'\uncertain{préciser}','priori',False,True,*W,True,'high','The word begins with the long descending p, followed by r and the dotted i group; its ending is the low ori sequence and final i, without the c/s sequence of préciser.','p10_a_priori')
add('line 8, cancellation',r'\deleted{\unsure{ens tot.}}',r'\struck{\ill{}}',r'\deleted{\unsure{ens tot.}}',False,True,*R,True,'low','The left low group and the two tall t stems with final stop survive the crossing. The intermediate joins remain covered, so ens tot. stays tentative.','p11_ens_tot')
add('line 9, abbreviation','codim','codim.','codim',False,True,*A,False,'high','The final m ends before the open space leading to the numeral 1, with no following stop.','p13_codim1')
add('line 9, compressed word under insertion',r'\unsure{mutuellement}',r'\ill{}',r'\unsure{mutuel\textsuperscript{t}}',True,True,*A,True,'low','The short visible sequence has low initial mutuel-like joins and a raised terminal t-like stroke. The full -lement sequence cannot be separated. The proposed abbreviated form is explicitly doubtful.','p12_distincts')
add('line 9, state of parenthesis and compressed word',r'\deleted{(\unsure{mutuellement}}',r'(\struck{\ill{}}',r'\unsure{(mutuel\textsuperscript{t}|\deleted{(mutuel\textsuperscript{t}}}',True,True,*D,True,'low','The long stroke above the word is continuous with the insertion’s curved leader. It crosses some tall strokes but leaves most low joins below it. The proposed primary reading is live, with cancellation explicitly retained as an alternative.','p12_distincts')
add('line 9, sign in insertion',r'en un $=$ \unsure{point|pt}',r'\uncertain{en un pt}',r'en un $=$ point',False,True,*O,True,'high','Between un and point there are two short horizontal strokes joined by a slight left return. The literal = is retained.','p12_distincts')
add('line 9, last word of insertion',r'\unsure{point|pt}','pt','point',False,True,*W,True,'high','After the descending p, a low o/i/n sequence extends to a short terminal t; the insertion contains the written length of point.','p12_distincts')
add('line 9, comma in insertion',',','(nothing)',',',False,True,*O,False,'high','A separate downward-curving comma stands after point above the main baseline, before the leader turns upward.','p12_distincts')
add('line 9, attachment of insertion',r'\deleted{(\unsure{mutuellement}} \inserted{en un $=$ \unsure{point|pt},}',r'\add{\uncertain{en un pt}} (\struck{\ill{}}',r'\inserted{en un $=$ point,} \unsure{(mutuel\textsuperscript{t}|\deleted{(mutuel\textsuperscript{t}}}',True,False,*P,False,'medium','The left end of the curved leader turns down immediately before the compressed mutuel-like word, after the numeral 1. The addition is placed at that join.','p12_distincts')
add('line 9, final word',r'\deleted{soit}','soit',r'\deleted{soit}',False,True,*D,False,'medium','A horizontal crossing runs across the compact final soit group after the comma, including the low letter bodies.','p12_distincts')
add('line 10, first Γ in containment',r'\unsure{\Gamma^{\deleted{\'}}(d)|\Gamma(d)}',r'\Gamma(d)',r'\unsure{\Gamma^{\deleted{\'}}(d)|\Gamma(d)}',False,True,*O,False,'low','A small overdrawn group remains above the opening parenthesis after Γ. It can be a cancelled prime, but the exact pen sequence is not secure; both readings are kept.','p14_containment')
add('line 11, after partie','à',':','à',False,True,*W,False,'high','The separate upper accent and low lower stroke give the page’s compressed à form.','p15_a_la_fois')
add('line 12, state of fermée',r'\deleted{fermée}','fermée',r'\unsure{fermée|\deleted{fermée}}',True,False,*D,False,'medium','The long stroke enters from the left of f and follows the joined low letter baseline. A distinct second crossing is not securely separable. The live primary reading and cancelled alternative are both represented in place.','p16_fermee','The word fermée is present in either reading; its status in the author’s phrase ouverte et fermée remains explicitly open.')
add('line 12, sign in cancelled formula',r'\Gamma\'(d)\simeq',r'\Gamma\'(d) \ill{}',r'\Gamma\'(d)\unsure{\simeq}',False,True,*R,True,'medium','A wavy group and a lower short remnant remain to the right of the cancelled Γ′(d); the broad cancellation partly covers the sign. A tentative ≃ is retained.','p17_cancelled_formula')
add('display (35), final punctuation','.', '(nothing)','(nothing)',True,False,*T,False,'high','The closing parenthesis after Γ(d) is followed by blank paper within the crop; no terminal point is visible.','p18_equation35')
add('line 14, inserted adjective',r'\inserted{total}',r'\add{totale}',r'\inserted{total}',False,True,*W,False,'high','The insertion ends in the tall l stroke with a downward return. There is no separate final e after it.','p20_total_relative')
add('line 14, after relative','relative','relative,','relative,',True,False,*O,False,'high','A compact looped comma with a downward tail stands below and to the right of relative before de.','p20_total_relative')
add('line 15, opening cancellation',r'\deleted{\unsure{$\Gamma\'(1)$ sur}}',r'\struck{\ill{}}',r'\deleted{\unsure{$\Gamma\'(1)$ sur}}',False,True,*R,True,'low','Γ and its high prime, two parentheses and sur remain under the horizontal cancellation. The overwritten interior numeral is tentatively 1 and is not claimed fully settled.','p21_cancelled_gamma')
add('line 15, first live Σ expression',r'\Sigma^{<}(1)',r'\Sigma^{*}(1)',r'\Sigma^{<}(1)',False,True,*S,False,'high','The raised mark above Σ is a compact two-arm left angle, followed by the argument 1.','p22_sigma_formulas','Preserves Γ₀=Σ^<(1).')
add('line 15, cancelled subscript on Σ',r'\Sigma_{\deleted{\unsure{*}}}',r'\Sigma',r'\Sigma_{\deleted{\unsure{*|0}}}',False,True,*O,False,'low','A compact scribbled-out subscript remains at the lower right of Σ. Its underlying form is not fully separable; * and 0 are explicitly retained as possibilities.','p22_sigma_formulas')
add('line 15, second live Σ expression',r'\Sigma^{<}(0)',r'\Sigma^{*}(0)',r'\Sigma^{<}(0)',False,True,*S,False,'high','The superscript is the same angular mark; the parenthesized numeral has the rounded 0 form seen elsewhere in the body.','p22_sigma_formulas','Preserves the author’s written Σ=Σ^<(0), including its separately cancelled subscript.')
add('line 15, addition over suffit',r'\inserted{\unsure{uniquement|suffit}}',r'\add{\uncertain{suffit}}',r'\inserted{\unsure{uniquement}}',False,True,*W,True,'medium','The added word begins with low joined u/n forms and a dotted i. The two initial f ascenders required by suffit are absent from this upper word; the later letters remain compressed, so uniquement retains doubt.','p23_uniquement')
add('line 16, prime on first cancelled Γ',r'\Gamma\'_1(0)',r'\Gamma_1(2)',r'\Gamma\'_1(\unsure{0|2})',False,True,*S,False,'medium','A raised short stroke remains at the upper right of the first Γ, distinct from the numeral 1 below it.','p24_struck_formulas','Preserves the visible prime on the first cancelled Γ expression.')
add('line 16, argument of first cancelled Γ','0','2',r'\unsure{0|2}',False,True,*S,False,'low','The argument contains an overwritten rounded loop with a closing parenthesis. The loop favors 0, but the crossing prevents a complete exclusion of 2.','p24_struck_formulas')
add('line 16, superscript on cancelled Σ',r'\Sigma^{<}',r'\Sigma^{*}',r'\Sigma^{<}',False,True,*S,False,'medium','Above the cancelled Σ a short left angular form remains; the raised arms are distinct from the long cancelling stroke.','p24_struck_formulas','Preserves the angular body superscript in the cancelled formula.')
add('line 16, argument of cancelled Σ',r'\unsure{\Sigma^{<}(0)}',r'\Sigma^{*}(2)',r'\unsure{\Sigma^{<}(0)|\Sigma^{<}(2)}',False,True,*S,False,'low','The parenthesized argument has an open rounded loop like the author’s 0, but its bottom is crossed. Both numerical readings remain explicit.','p24_struck_formulas')
add('line 16, last cancelled index',r'\Gamma\'_{\unsure{1+1}}',r'\Gamma\' (\ill{})',r'\Gamma\'_{1+1}',False,True,*R,True,'high','Below the last Γ′, two small upright numerals are separated by a visible plus. The cancellation runs above most of the index.','p24_struck_formulas','Preserves the author’s cancelled subscript 1+1.')
add('line 17, added abbreviation',r'\inserted{(i.e.}','(',r'\inserted{(i.e. \unsure{néc.}}',False,True,*O,False,'high','A left parenthesis and i.e. are visible above ouverte, with a curved leader attaching the addition immediately before that adjective.','p25_ie_insertion')
add('line 17, second word of addition','(nothing)','(nothing)',r'\unsure{néc.}',True,True,*O,False,'low','After i.e. there is a second compact word with low joined initial strokes, a detached accent above the final part, an open c-shaped stroke and a stop. The tentative néc. is preserved as an abbreviation with its visible accent and stop.','p25_ie_insertion')
add('line 19, state of au',r'\unsure{\deleted{au}|au}','au',r'\unsure{au|\deleted{au}}',True,False,*D,False,'medium','The low au group is heavily joined, but a separate crossing cannot be isolated from its baseline. The live form is preferred while the cancellation remains an explicit alternative.','p26_au_dessus')
add('line 19, between au and dessus','(nothing)','-','(nothing)',False,True,*T,False,'high','The space between the end of au and the tall initial d of dessus is blank.','p26_au_dessus')
add('line 20, Sym expression grouping',r'\operatorname{Sym}^2_\Sigma(\Gamma_0)^*',r'(\mathrm{Sym}^2_\Sigma\Gamma_0)^{*}',r'\operatorname{Sym}^2_\Sigma(\Gamma_0)^*',False,True,*S,False,'high','The opening parenthesis is immediately before Γ₀. There is no outer parenthesis before Sym. The closing parenthesis follows Γ₀ and the asterisk is at its upper right.','p27_sym2','Preserves the written scope and placement of the parentheses and final asterisk.')
add('line 20, opening quotation',"``choix",'« choix',"``choix",False,True,*X,False,'high','Two short high strokes stand between the opening parenthesis and choix.','p28_open_quotes')
add('line 21, end of quotation','distincts)','distincts »)','distincts)',False,True,*T,False,'high','After distincts there is a closing parenthesis and comma. No pair of closing quotation marks is visible.','p29_distincts_end')
add('left margin beside lines 19–20, graph note',r'$\Gamma_1$ est le graphe de la relation $x<y$.',r'$\Gamma_1$ \uncertain{se voit} \ill{} $x<y$ \ldots\ \uncertain{relations}',r'$\Gamma_1$ est le graphe de la relation $x<y$',False,True,*R,True,'high','In the rotated crop the three short lines read Γ₁ est le / graphe de la / relation x<y. The tall g and p descenders and the loops of de/la are visible.','p31_margin_graph','The author explicitly describes Γ₁ as the graph of x<y.')
add('left margin, after x<y','.','(nothing)','(nothing)',True,False,*T,False,'high','The y ends in a long descending return, followed by blank paper; no terminal point is visible.','p31_margin_graph')
add('lower margin, initial phrase','ou une section','ou encore une section','ou une section',False,True,*T,False,'high','The line has a short ou, then une and section. The spaces and visible word groups provide no additional encore.','p32_margin_section')
add('lower margin, state of initial phrase','ou une section',r'\struck{ou encore une section}',r'ou une section',False,True,*D,False,'high','The phrase ou une section is above the two cancelled mathematical lines and has no crossing stroke through its letters.','p32_margin_section')
add('lower margin, first cancelled mathematical line',r'\deleted{de $\Gamma_0\times_\Sigma\Gamma_0\setminus\text{diagonale}$}',r'\struck{\ill{} de $\Gamma_0\times_\Sigma\Gamma_0$ \ill{}}',r'\deleted{de $\Gamma_0\times_\Sigma\Gamma_0\setminus\unsure{\text{diagonale}|\text{diag}}$}',False,True,*R,True,'medium','The rotated crop shows de and two Γ₀ factors with the base Σ under ×. The trailing subtraction/diagonal wording is crossed and overlaps neighboring writing; its exact ending remains doubtful.','p32_margin_section')
add('lower margin, argument of cancelled Sym²',r'\unsure{\Sigma\times_\Sigma\Gamma_0}',r'\ldots',r'\Gamma_0\times_\Sigma\Gamma_0',True,True,*S,True,'medium','Inside the parentheses the first object has a top bar and descending left stem, with a small lower 0. It is read as Γ₀, followed by × with base Σ and another Γ₀.','p32_margin_section','Preserves Γ₀ as the first factor in the cancelled Sym² argument, without replacing it by Σ.')
add('lower margin, final unattached cancellation','(nothing)','(nothing)',r'\deleted{de}',True,True,*O,False,'high','A further separate de is written below the second cancelled formula at the lower left and has its own horizontal crossing. It is retained without supplying a continuation.','p32_margin_section')
add('before display (36), cancelled fragment',r'\deleted{$\unsure{\text{que }\Gamma_1}$}','(nothing)',r'\deleted{$\unsure{\text{que }\Gamma_1}$}',False,True,*O,False,'low','To the left of the displayed product, an overwritten short word and Γ with a low index are crossed by a long horizontal stroke. The tentative que Γ₁ is retained. H mentions a crossed word only in its editorial note.','p33_diagram36')
add('display (36), first factor below vertical ∩',r'\Gamma_0',r'\Gamma_0',r'\unsure{\Sigma_0|\Gamma_0}',True,True,*S,False,'low','The first lower factor is overdrawn, with top and bottom horizontal strokes and a dark angular middle. Its visible outline is Σ₀-like, while an overwritten Γ₀ remains possible. The ambient-product expectation is not used to regularize it.','p33_diagram36','Keeps the source’s unresolved first lower factor Σ₀/Γ₀ in the displayed ambient product.')
add('display (36), projection label initial',r'\operatorname{pr}_{13}',r'\mathrm{pr}_{13}',r'\operatorname{Pr}_{\unsure{13|23}}',True,True,*S,False,'medium','The first letter has a tall stem and an upper loop without a lower descender, giving the capital-shaped P. The first index digit is dark and overdrawn and is separately left doubtful.','p33_diagram36')
add('display (36), vertical relations and ambient product',r'\arrow[d,phantom,"\cap" description] ... \arrow[d,phantom,"\cup" description]',r'où l\'intersection est prise dans $\Gamma_0\times\Gamma_0\times\Gamma_0$ et $\Gamma_1\subset\Gamma_0\times\Gamma_0$',r'\text{vertical }\cap\text{ over }\unsure{\Sigma_0|\Gamma_0}\times\Gamma_0\times\Gamma_0;\quad \text{vertical }\cup\text{ over }\Gamma_1',False,True,'drawing or diagram','Drawings and diagrams',False,'high','Under the source expression is an upward arch and the written triple product. Under the right-hand product is a U-shaped vertical inclusion mark and Γ₁. The source has these written vertical relations, without H’s explanatory sentence. They are typeset in the diagram.','p33_diagram36')
add('display (36), number and concluding phrase placement',r'\end{tikzcd}} (36) \quad se factorise par $\Gamma_1$',r'(36)\qquad ...\quad\text{se factorise par }\Gamma_1',r'(36)\text{ at left of diagram; se factorise par }\Gamma_1\text{ at right}',True,False,*P,False,'high','The handwritten (36) is at the left below the cancelled fragment; se factorise par Γ₁ runs to the right of the upper diagram row. The proposed layout retains those sides.','p33_diagram36')
# Convert apostrophe escapes introduced only to delimit Python strings; they are literal manuscript primes/apostrophes.
for r in ch:
 for k in ['C','H','final']:
  r[k]=r[k].replace("\\'", "'")
dec=[]
def decision(id,status,reading,ev,p,conf):dec.append(dict(id=id,decision=status,reading=reading,evidence=ev,crop=cp(p),box=cs[p],confidence=conf))
decision('M0572','undecided',r'\unsure{ns}','The abbreviation’s terminal group is compact; the full applications is not written, but ns is not individually secure.','p08_applicns','low')
decision('M0573','first',r'\tfrac12','The sign consists of a written 1, oblique fraction stroke and lowered 2.','p09_half_simplicial','high')
decision('M0574','first','point','The word shows the descending p and a low sequence extending through o/i/n to a terminal t; its written length exceeds pt.','p12_distincts','high')
decision('M0575','first','distinctes','Following the tall t, the ending contains a small e turn before the final s return.','p12_distincts','high')
decision('M0576','undecided',r'\unsure{\Gamma^{\deleted{\'}}(d)|\Gamma(d)}','An overdrawn raised group after Γ can be a cancelled prime, but its exact strokes remain crowded.','p14_containment','low')
decision('M0577','undecided',r'\unsure{\mathfrak S_d|\mathcal S_d}','The handwritten S has a large rounded outer curve and an inner hook. Its ornamental alphabet assignment is not uniquely fixed by this handwritten glyph.','p18_equation35','medium')
decision('M0578','undecided',r'\unsure{uniquement}','The initial u/n joins and dotted i support uniquement and allow the suffit alternative to be removed. The later letters remain too compressed to remove doubt completely.','p23_uniquement','medium')
decision('M0579','undecided',r'\unsure{au|\deleted{au}}','The low group is heavily joined. A separate deletion stroke cannot be isolated confidently from its baseline, so both states remain.','p26_au_dessus','medium')
for r in dec:r['reading']=r['reading'].replace("\\'", "'")
inv=[]
def item(kind,pos,txt,hand='his hand'):inv.append(dict(element=f'E{len(inv)+1:02d}',kind=kind,position=pos,first_words_or_objects=txt,sheet_kind='text',hand=hand,transcribed='yes'))
item('margin note','upper-left corner','23')
item('text','body, lines 1–12',"avec la structure ... de Γ′(d), et ...")
item('insertion','above right end of line 1','ordonnée')
item('deletion','line 2','Par exemple')
item('deletion','line 4','sym. (tentative)')
item('insertion','above line 4, over sym.','cart. relative')
item('deletion','line 4, after Γ₀','(∅) (tentative)')
item('insertion','above right end of line 4','=Σ^<(1)')
item('deletion','line 6, after relatives','inférieures (tentative)')
item('insertion','above line 6','cancelled Γ′(d), des d′.ième (d′<d)')
item('deletion','within insertion above line 6','Γ′(d)')
item('deletion','line 8','ens tot. (tentative)')
item('insertion','above line 9, after codim 1','en un = point,')
item('deletion','line 9, state unresolved','(mutuel^t; live/cancelled alternatives both represented')
item('deletion','right end of line 9','soit')
item('insertion','right side of line 10','Γ with possible cancelled prime, (d) ⊂ Γ′(d)')
item('deletion','within addition at line 10, state unresolved','possible prime on first Γ')
item('deletion','line 12, state unresolved','fermée; live/cancelled alternatives represented')
item('deletion','right end of line 12','Γ′(d) ≃ (sign tentative)')
item('display','line 13, number (35)','Γ′(d) ≃ S_d × Γ(d), ornamental S alphabet unresolved')
item('text','body, lines 14–21','Pour avoir ... condition de transitivité')
item('deletion','line 14','la')
item('insertion','above line 14','une')
item('insertion','above right side of line 14','total')
item('deletion','line 15, first expression','Γ′(1) sur (tentative)')
item('deletion','line 15, lower-right of Σ','cancelled subscript * / 0')
item('deletion','right side of line 15','suffit')
item('insertion','above suffit in line 15','uniquement (tentative)')
item('deletion','line 16','dans Γ′₁(0/2)=Σ^<(0/2), Γ′_{1+1}')
item('insertion','above ouverte in line 17','(i.e. néc. (last abbreviation tentative)')
item('deletion','line 19, state unresolved','au; live/cancelled alternatives represented')
item('margin note','left margin alongside line 15','cancelled il s’agit de')
item('deletion','within marginal note alongside line 15','il s’agit de')
item('margin note','left margin beside lines 19–20','Γ₁ est le graphe de la relation x<y')
item('margin note','lower left margin, diagonal','ou une section, followed by cancelled mathematical lines and final de')
item('deletion','first cancelled line of lower marginal note','de Γ₀×_ΣΓ₀ minus diagonale/diag')
item('deletion','second cancelled line of lower marginal note','de Sym²(Γ₀×_ΣΓ₀)')
item('deletion','last short line of lower marginal note','de')
item('deletion','left of display (36)','que Γ₁ (tentative)')
item('diagram','bottom, numbered (36), two rows','intersection of two fiber products; projection; two vertical inclusion marks; ambient triple product; se factorise par Γ₁')
item('margin note','bottom-left corner','54','another unnamed hand')
doubts=[]
def doubt(place,reading,alts,conf,reason):doubts.append(dict(place=place,reading=reading,alternatives=alts,confidence=conf,reason=reason))
doubt('line 4, cancellation','sym.','Obscured middle joins','low','The cancellation covers the low letters; the original C doubt remains.')
doubt('line 4, cancelled argument','(∅)','Overdrawn central symbol','low','Parentheses are visible, while the central slashed-loop group is heavily overwritten.')
doubt('line 6, cancelled word','inférieures','Exact compressed ending unresolved','medium','The initial in/f structure is visible; later joins are crossed.')
doubt('line 6, final abbreviation','applicns','Terminal shortened group unresolved','low','The complete full-word ending supplied by H is not visible.')
doubt('line 8, cancellation','ens tot.','Obscured low joins','low','Two t stems and stop remain, while parts of the first group are crossed.')
doubt('line 9, abbreviated word and state','(mutuel^t, live','mutuellement; cancellation of either written form','low','The visible sequence is short and under the insertion leader; both written form and deletion state remain uncertain.')
doubt('line 10, first Γ in containment','Γ with cancelled prime','Γ without a separate prime','low','The raised group is overwritten.')
doubt('line 12, state of fermée','live fermée','cancelled fermée','medium','The long stroke may be the f crossbar and joined baseline; no independent crossing is securely isolated.')
doubt('line 12, cancelled relation','≃','Exact overwritten relation','medium','Wavy and lower remnants survive under the strike.')
doubt('display (35), alphabet','fraktur S_d','calligraphic S_d','medium','The ornamental handwritten S admits either typographic assignment.')
doubt('line 15, first cancelled formula','Γ′(1) sur','Interior numeral may be overwritten','low','The argument is not completely separable under the crossing.')
doubt('line 15, deleted subscript on Σ','*','0','low','The underlying small symbol is scribbled over.')
doubt('line 15, insertion','uniquement','Later compressed letters unresolved','medium','The initial u/n/i supports this word; the later letters do not all separate.')
doubt('line 16, first cancelled argument','0','2','low','Rounded overwritten loop, partly crossed.')
doubt('line 16, cancelled Σ argument','0','2','low','Rounded open loop partly lost beneath the strike.')
doubt('line 17, inserted abbreviation','néc.','Unresolved short word with detached accent and final c/point','low','Extra letters after i.e. are visible; their reading remains tentative and is not expanded.')
doubt('line 19, state of au','live au','cancelled au','medium','The heavy joining stroke and a possible cancellation cannot be fully distinguished.')
doubt('lower margin, first cancelled formula','diagonale','diag','medium','The ending is crossed and overlaps neighboring writing.')
doubt('before display (36), cancelled fragment','que Γ₁','Overwritten short word and index','low','The crossing obscures the low letters and subscript.')
doubt('display (36), projection index','13','23; unidentified underlying overwritten first digit','low','The first digit is dark and overdrawn; no separate underlying digit can be read reliably.')
doubt('display (36), first lower factor','Σ₀','overwritten Γ₀','low','The visible glyph has a Σ-like outline; it is preserved without substitution from the expected product.')
notes=[
 dict(id='150-055-N01',text='The author continues the description of a local ordered cylindrical stratification. He describes Γ(d)=Σ^<(d+1) through a relative Cartesian power of Γ₀ with images of lower powers removed, then speaks of ordered sequences of germs of codimension-one strata. He writes the relation numbered (35), Γ′(d) ≃ S_d × Γ(d), with the ornamental form of S left typographically doubtful. These are statements of the manuscript; they were not independently proved or checked.'),
 dict(id='150-055-N02',text='The lower paragraph discusses a relative total order on Γ₀ over Σ. The author writes conditions involving Γ₁, its superscript-s counterpart, a union covering the complement of the diagonal, and an empty intersection. He describes a section involving Sym² and writes a transitivity requirement in diagram (36), followed by se factorise par Γ₁. The marginal note calls Γ₁ the graph of x<y. These claims and descriptions are attributed to the author; no proof of their equivalence was undertaken.'),
 dict(id='150-055-N03',text='The author’s written d.ième and d′.ième forms, the separate d+1 in Γ(d)=Σ^<(d+1), and the strict comparison d′<d are all preserved. No dimensional shift or indexing convention was supplied to reconcile them. The cancelled added Γ′(d) has an unprimed argument d.'),
 dict(id='150-055-N04',text='Several apparent cancellations must be separated from insertion leaders and joined handwriting. The stroke under ordonnée is continuous with its insertion leader. The state of the compressed mutuel^t-like word, of fermée, and of au remains marked in place. The author’s upper word over suffit is narrowed to tentative uniquement. The added short word after i.e. is tentatively néc.; its detached accent and stop are preserved.'),
 dict(id='150-055-N05',text='In diagram (36), the first factor of the lower triple product has a crowded Σ₀-like outline with Γ₀ also possible. The transcription retains that ambiguity rather than choosing from the surrounding mathematical expectation. The first projection-index digit is overdrawn; 13/23 remains open. The two inclusion marks are written vertically and are reproduced vertically, while H paraphrases them in prose.'),
 dict(id='150-055-N06',text='The upper-left 23 is in the main dark hand. The bottom-left 54 is smaller and lighter, in another unnamed hand, and is recorded as foliation. H’s page marker and editorial notes are not source prose. The lower diagonal margin has an additional final cancelled de, with no continuation supplied.'),
 dict(id='150-055-N07',text='All decisions were made from the whole image, the two full-resolution halves and the listed crops. Repeated written forms were compared within the page and with the supplied notation snapshot. No mathematical calculation, proof-check or independent re-proof was used in deciding a reading.')
]
notation=[
 dict(form=r'\Sigma^{<}',meaning='Body object/space notation as written.',evidence='Angular raised signs in Γ(d)=Σ^<(d+1), Γ₀=Σ^<(1), Σ=Σ^<(0), and a cancelled equality.',places='lines 3, 4 addition, 15 twice, 16 cancellation'),
 dict(form=r'\Gamma_0',meaning='The object written equal to Σ^<(1), used in Cartesian products over Σ.',evidence='Explicit equality and repeated indexed factors.',places='lines 4, 15, 17–20, lower marginal formulas, display (36)'),
 dict(form=r'\Gamma_1',meaning='The author’s proposed graph of the relation x<y.',evidence='The explicit marginal sentence and the union/intersection formulas.',places='line 18, graph margin, display (36)'),
 dict(form=r'{}^s\Gamma_1',meaning='A superscript-s version of Γ₁ used by the author in the two displayed set relations.',evidence='The s is above and to the left of Γ₁ in both expressions.',places='line 18'),
 dict(form=r'\tfrac12\text{ simpliciales}',meaning='The author’s written shorthand accompanying simpliciales.',evidence='Numeral 1, diagonal slash, lowered numeral 2.',places='line 7'),
 dict(form=r'\unsure{\mathfrak S_d|\mathcal S_d}',meaning='The ornamentally written S with subscript d in (35); alphabet assignment unresolved.',evidence='Large rounded outer curve with internal hook.',places='display (35)'),
 dict(form=r'\operatorname{Sym}^2_\Sigma(\Gamma_0)^*',meaning='The source’s Sym expression with an explicit final asterisk.',evidence='Parentheses enclose Γ₀ only, followed by a multi-armed asterisk.',places='line 20'),
 dict(form=r'\cap\text{ and }\cup\text{ placed vertically}',meaning='Vertical relation marks connecting the two levels of diagram (36).',evidence='Upward arch over the lower triple product; U-shaped sign above the lower Γ₁.',places='display (36)'),
 dict(form=r'\operatorname{Pr}_{\unsure{13|23}}',meaning='Written projection label with a dark first index digit.',evidence='Capital-shaped P, small r, overdrawn first digit and a visible 3.',places='display (36)')
]
ab=[
 dict(written='puiss.',expansion='puissance / puissances',places='lines 4, 6'),
 dict(written='sym.',expansion='symétrique (tentative cancelled short form)',places='line 4'),
 dict(written='cart.',expansion='cartésienne / cartésiennes',places='lines 4 addition, 6'),
 dict(written='applicns',expansion='applications; terminal written group remains doubtful',places='line 6'),
 dict(written='½',expansion='semi-',places='line 7'),
 dict(written='ens tot.',expansion='ensembles totalement ... (tentative; cancelled phrase unfinished)',places='line 8'),
 dict(written='codim',expansion='codimension',places='line 9'),
 dict(written='mutuel^t',expansion='mutuellement (tentative written abbreviation)',places='line 9'),
 dict(written='i.e.',expansion='id est',places='lines 17 addition, 19'),
 dict(written='néc.',expansion='nécessairement (tentative abbreviation)',places='line 17 addition'),
 dict(written='diag',expansion='diagonale',places='lines 18–19; lower margin ending uncertain'),
 dict(written='Pr',expansion='projection',places='display (36)')
]
hand=[
 dict(habit='The angular body superscript can be small and partly filled where its two arms meet.',places='lines 3, 4, 15, 16',scope='All six body occurrences on this leaf, including the cancelled equality.',witness_errors='H repeatedly gives * for these angular signs.'),
 dict(habit='Long insertion leaders curve downward at the attachment and run beneath the added words; they can cross tall letters of the original line.',places='ordonnée line 1; upper addition line 6; en un = point line 9; total line 14; i.e. néc. line 17',scope='These visibly led additions; a crossing alone does not establish cancellation.',witness_errors='C underlines ordonnée and assigns cancellation to the mutuel-like wording under a leader; the latter state remains open.'),
 dict(habit='Long f crossbars and joined low baselines can resemble deletion strokes.',places='fermée line 12; au line 19',scope='These specific words remain state-doubtful.',witness_errors='C gives fermée as deleted and prefers deleted au; H gives both live.'),
 dict(habit='Shortened words can be written with very compressed low joins and a relatively high terminal stroke.',places='applicns line 6; mutuel^t-like form line 9; uniquement line 15; néc. line 17',scope='Specified occurrences only; all unresolved letter groups are marked in the text.',witness_errors='C expands the mutuel-like sequence and omits the second short word after i.e.; H expands applications and omits the i.e. addition.'),
 dict(habit='A separate high accent must be retained even when the abbreviated word remains unresolved.',places='néc. in line 17 addition; à in lines 7 and 11',scope='These inspected high strokes are dark and detached from their lower letter groups.',witness_errors='Both witnesses omit the short néc.-like word; H reads : for the two à forms.'),
 dict(habit='The diagonal marginal writing becomes readable when rotated; separate live and cancelled lines remain distinguishable.',places='left margin graph note and lower section note',scope='All three marginal note blocks on this leaf were separately cropped and visually read.',witness_errors='H supplies se voit and encore, gives portions as illegible, and strikes the live initial ou une section.'),
 dict(habit='Overwritten mathematical characters can retain competing outlines.',places='first Γ of line-10 containment; cancelled indices line 16; first lower factor and projection index in (36)',scope='No identity is imposed from expected mathematics at these places.',witness_errors='Both witnesses give Γ₀ for the lower first factor; final retains Σ₀/Γ₀ uncertainty.')
]
boxes=[]
def bx(kind,xy,reading):boxes.append(dict(box=f'B{len(boxes)+1:02d}',kind=kind,x0=xy[0],y0=xy[1],x1=xy[2],y1=xy[3],reading=reading))
bx('handwritten number',[37,29,96,85],'23')
bx('insertion',[1470,28,1666,125],r'\inserted{ordonnée}')
bx('struck passage',[558,154,916,240],r'\deleted{Par exemple},')
bx('handwritten number',[743,232,1262,334],r'$\Gamma(d)=\Sigma^{<}(d+1)$,')
bx('insertion',[870,327,1118,428],r'\deleted{\unsure{sym.}} \inserted{cart. relative}')
bx('lexical disagreement',[1112,352,1274,413],r'$d$.ième')
bx('handwritten number',[1452,297,1665,421],r'$\Gamma_0$\deleted{\unsure{$(\varnothing)$}}\inserted{$=\Sigma^{<}(1)$}')
bx('lexical disagreement',[832,452,1270,507],'dont on enlève')
bx('insertion',[842,493,1517,561],r'\inserted{\deleted{$\Gamma\'(d)$} des $d\'$.ième ($d\'<d$)}')
bx('struck passage',[1035,553,1246,644],r'\deleted{\unsure{inférieures}}')
bx('lexical disagreement',[1464,550,1661,649],r'applic\unsure{ns}')
bx('handwritten number',[269,678,324,755],r'$\tfrac12$')
bx('lexical disagreement',[832,665,1092,736],'celles ci.')
bx('lexical disagreement',[1417,659,1626,751],'à priori')
bx('struck passage',[383,756,622,843],r'\deleted{\unsure{ens tot.}}')
bx('handwritten number',[287,842,824,931],r'strates de codim $1$')
bx('insertion',[818,796,1175,893],r'\inserted{en un $=$ point,} \unsure{(mutuel\textsuperscript{t}|\deleted{(mutuel\textsuperscript{t}}}')
bx('lexical disagreement',[1174,817,1489,925],'distinctes),')
bx('struck passage',[1493,825,1605,910],r'\deleted{soit}')
bx('doubtful formula',[1103,891,1536,1002],r'\inserted{$\unsure{\Gamma^{\deleted{\'}}(d)|\Gamma(d)}\subset\Gamma\'(d)$},')
bx('lexical disagreement',[983,1019,1031,1084],'à')
bx('struck passage',[252,1138,508,1265],r'\unsure{fermée|\deleted{fermée}}')
bx('doubtful formula',[1199,1122,1498,1207],r'\deleted{$\Gamma\'(d)\unsure{\simeq}$}')
bx('doubtful formula',[292,1258,1186,1361],r'$(35)\qquad\Gamma\'(d)\simeq\unsure{\mathfrak S_d|\mathcal S_d}\times\Gamma(d)$')
bx('insertion',[641,1347,749,1424],r'\deleted{la}\inserted{une}')
bx('insertion',[1270,1283,1598,1436],r'\inserted{total} relative, de')
bx('doubtful formula',[255,1446,495,1538],r'\deleted{\unsure{$\Gamma\'(1)$ sur}}')
bx('doubtful formula',[538,1437,1261,1540],r'$\Gamma_0=\Sigma^{<}(1)$ sur $\Sigma_{\deleted{\unsure{*|0}}}=\Sigma^{<}(0)$,')
bx('insertion',[1277,1408,1612,1518],r'il \deleted{suffit}\inserted{\unsure{uniquement}}')
bx('doubtful formula',[702,1528,1347,1629],r'\deleted{dans $\Gamma\'_1(\unsure{0|2})=\unsure{\Sigma^{<}(0)|\Sigma^{<}(2)}$, $\Gamma\'_{1+1}$} \inserted{(i.e. \unsure{néc.}}')
bx('handwritten number',[274,1630,810,1721],r'$\Gamma_0\times_\Sigma\Gamma_0\setminus\text{diagonale}$,')
bx('insertion',[1083,1565,1323,1686],r'\inserted{(i.e. \unsure{néc.}} ouverte')
bx('handwritten number',[276,1698,1618,1833],r'$\Gamma_1$, telle que $\Gamma_1\cup{}^s\Gamma_1=\Gamma_0\times\Gamma_0\setminus\text{diag}$, $\Gamma_1\cap{}^s\Gamma_1=\varnothing$')
bx('handwritten number',[851,1820,1228,1931],r'$\Gamma_0\times_\Sigma\Gamma_0\setminus\text{diag}$')
bx('medium-confidence departure',[1241,1810,1550,1920],r'\unsure{au|\deleted{au}} dessus')
bx('handwritten number',[365,1922,581,2042],r'$\operatorname{Sym}^2_\Sigma(\Gamma_0)^*$')
bx('lexical disagreement',[574,1933,830,2038],r'(``choix d\'')
bx('lexical disagreement',[456,2027,740,2119],'distincts),')
bx('margin note',[18,1440,240,1615],r'\deleted{il s\'agit de}')
bx('margin note',[21,1801,280,2063],r'$\Gamma_1$ est le graphe de la relation $x<y$')
bx('margin note',[23,1894,539,2273],r'ou une section \deleted{de $\Gamma_0\times_\Sigma\Gamma_0\setminus\unsure{\text{diagonale}|\text{diag}}$}\deleted{de $\operatorname{Sym}^2(\Gamma_0\times_\Sigma\Gamma_0)$}\deleted{de}')
bx('doubtful formula',[260,2075,1666,2306],r'\deleted{$\unsure{\text{que }\Gamma_1}$} (36)\quad (\Gamma_1\times_\Sigma\Gamma_0)\cap(\Gamma_0\times_\Sigma\Gamma_1)\xrightarrow{\operatorname{Pr}_{\unsure{13|23}}}\Gamma_0\times\Gamma_0\quad\text{se factorise par }\Gamma_1;\quad\text{beneath the left object: }\cap,\ \unsure{\Sigma_0|\Gamma_0}\times\Gamma_0\times\Gamma_0;\quad\text{beneath the right object: }\cup,\ \Gamma_1')
bx('handwritten number',[23,2295,82,2348],'54')
for b in boxes:b['reading']=b['reading'].replace("\\'", "'")
# The final diagram is supplied as actual TikZ-cd in the audit reading as well.
boxes[-2]['reading']=r'''\deleted{$\unsure{\text{que }\Gamma_1}$} \diagram{\begin{tikzcd}[column sep=large,row sep=small]
(36)\quad(\Gamma_1\times_\Sigma\Gamma_0)\cap(\Gamma_0\times_\Sigma\Gamma_1)\arrow[r,"{\operatorname{Pr}_{\unsure{13|23}}}"]\arrow[d,phantom,"\cap" description]&\Gamma_0\times\Gamma_0\arrow[d,phantom,"\cup" description]&\text{se factorise par }\Gamma_1\\
\unsure{\Sigma_0|\Gamma_0}\times\Gamma_0\times\Gamma_0&\Gamma_1&
\end{tikzcd}}'''
purposes=['Top-right ordonnée leader','Cancelled Par exemple and comma scope','Opening formula and angular exponent','cart. relative, sym. and ordinal punctuation','Γ₀ addition and cancelled argument','dont / d’où and enlève / utilise','Crowded insertion, cancelled Γ′(d), inequality and inférieures','Application abbreviation, M0572','½ and unhyphenated celles ci, M0573','à priori','Cancelled ens tot.','point, distinctes, compressed mutuel-like word and states, M0574–M0575','codim punctuation and numeral 1','Whole containment formula and M0576','à la fois','State of fermée','Cancelled formula and relation','Whole formula (35), M0577 and final punctuation','une over la','total and comma after relative','Cancelled Γ expression before Γ₀','Whole live Σ formulas and cancelled subscript','Upper uniquement and cancelled suffit, M0578','Whole cancelled line-16 formulas and all indices','Full i.e. néc.-like insertion','au state and absent hyphen, M0579','Whole Sym² expression and grouping','Opening high quotation marks','Absence of closing quotes','Cancelled diagonal il s’agit de','Graph-of-relation margin note','Section margin, both cancelled formulas and final cancelled de','Whole diagram (36), vertical relations and overwritten symbols']
data=dict(scan='055',reader='reader_c',line_count=23,changes=ch,decisions=dec,inventory=inv,doubts=doubts,notes=notes,check_events=[],notation=notation,abbreviations=ab,hand_log=hand,audit_boxes=boxes,crops=[dict(file=cp(n),box=b,purpose=purposes[i],rotation_degrees=a) for i,(n,b,a) in enumerate(items)],unresolved=[f"{d['place']}: {d['reading']} ({d['alternatives']})." for d in doubts],coverage=dict(whole_image_viewed=True,halves_viewed=['top','bottom'],all_tokens_read=True,all_C_insertions_deletions_checked=True,differences_considered=len((root/'packets/150_scan055/diffs.tsv').read_text().splitlines())-1,macro_only_differences_ignored='Ignored equivalent C/H insertion and deletion macro names, equivalent empty-set forms, math font wrappers around ordinary operator words, editorial page markers and notes, and display versus inline wrappers for otherwise unchanged formulas. Actual punctuation, written abbreviation lengths, strike states, insertion attachments and the diagram’s vertical relations were examined. The line count includes 20 running-text lines, equation (35), and the two rows of diagram (36).'))
for name,content in [('150_scan055.tex',tex),('150_scan055.json',json.dumps(data,ensure_ascii=False,indent=2)+'\n')]:
 target=out/name;tmp=out/(name+'.reader_c.tmp')
 with tmp.open('w',encoding='utf-8') as f:f.write(content);f.flush();os.fsync(f.fileno())
 os.replace(tmp,target)
print(json.dumps({'changes':len(ch),'against_C':sum(c['against_C'] for c in ch),'against_H':sum(c['against_H'] for c in ch),'decisions':len(dec),'inventory':len(inv),'audit_boxes':len(boxes),'crops':len(items),'files':[str(out/'150_scan055.tex'),str(out/'150_scan055.json')]}))
