from pathlib import Path
import json,re
root=Path('/workspace/scratch/98070f078628/SP116_CW_75_work')
out=root/'readers/scan006'
m=json.loads((out/'crop_boxes.json').read_text())
proposal=(out/'proposal.tex').read_text()
source='J75-01_75_scan006.jpg'
changes=[]
def ch(place,key,c,h,final,evidence,confidence='high',kind='reading',against_c=False,against_h=True,marked=False,math_note=''):
    z=m[key]
    changes.append(dict(id=f'scan006-c{len(changes)+1:02}',place=place,c=c,h=h,final=final,
        evidence=f'{evidence} Source {source}, original pixel bbox {z["box"]}; inspected crop {Path(z["crop"]).name}.',
        crop=z['crop'],box=z['box'],confidence=confidence,kind=kind,against_c=against_c,against_h=against_h,
        marked_in_H=marked,math_note=math_note))
ch('opening; H above sous-groupes','h_insert',r'\inserted{$H$}',r'$H$',r'\inserted{$H$}',
   'Two upright strokes joined by a crossbar form H above the baseline; the small return mark locates the insertion between sous-groupes and de.',kind='insertion')
ch('opening; punctuation after Z/H','dots','.....','…','.....',
   'Five separated dot positions follow the closing parenthesis; the fourth is paler, and the last position is a heavier two-lobed deposit.',kind='punctuation')
ch('heading; cancelled short word','heading_deleted',r'\deleted{\unsure{Ch.|En.}}','déf.',r'\deleted{\unsure{Ch.|En.}}',
   'The cancellation crosses the middle of a short word. The first upper curve permits C or E; the following high stroke and low ending permit h or n. The terminal stop survives, but the crossed letters do not settle Ch. against En.',
   'low','retained doubt',marked=False)
ch('heading Prop; terminal punctuation','prop',r'\uline{Prop}',r'\emph{Prop.}',r'\uline{Prop}',
   'P-r-o-p are followed by the rising end of the underline. The dark rightmost mark is continuous with that underline; there is no separate dot at word height.',
   'medium','punctuation')
ch('after Soit; cancelled suffix','soit_suffix',r'\deleted{\unsure{s|x}}','',r'\deleted{\unsure{s|x}}',
   'Immediately after the t there is an additional crossed small body. Its lower curve permits s and its crossing strokes permit x; the overwriting prevents a letter-level resolution.',
   'low','retained doubt')
ch('proposition; strict above baseline','strict_deleted',r'\deleted{\unsure{strict}}',r'\struck{\ill{}}',r'\inserted{\deleted{\unsure{strict}}}',
   'The small word is written above the space after contour, with a return caret descending toward that space. A cancellation crosses its centre; s/t-like outer stems survive but the interior letters are partly covered.',
   'low','insertion and deletion',True,True,True)
ch('proposition; empty-set glyph','empty',r'$\ne\varnothing$',r'$\neq\emptyset$',r'$\ne\phi$',
   'After the two inequality strokes, the glyph has a small closed bowl and a long descending oblique stem through it. It is the phi-shaped sign recorded in the notation table, not the slashed-circle forms supplied by the witnesses.',
   kind='symbol',against_c=True,math_note='Glyph reading only; the meaning of the proposition was not used to replace the sign.')
ch('a; interlinear replacement Soit g un','soit_insert',r'\deleted{Un}\inserted{Soit $g$ un}',r'Soit \struck{Un} $g$ un',r'\inserted{Soit $g$ un}',
   'Soit, the descending-loop g, and un occupy the smaller line above the cancelled Un; their placement makes one replacement phrase.',
   kind='insertion',marked=True)
ch('a; cancelled Un','un_deleted',r'\deleted{Un}',r'\struck{Un}',r'\deleted{\unsure{Un}}',
   'The two tall sides of U remain, but the following n is crossed by the heavy horizontal cancellation. The word is plausible as Un without every stroke being recoverable.',
   'medium','new doubt',True,True,True)
ch('a; cancelled est','est_deleted','est','',r'\unsure{est}',
   'The small e-shaped body and two higher prongs survive beneath the cancellation; the s and t joins are covered in part, so certainty is not retained.',
   'medium','new doubt',True,True,True)
ch('a; cancelled dit','dit_deleted','dit','',r'\unsure{dit}',
   'The d loop and terminal t stem remain under the overline, while the short central stroke and its dot overlap the interlinear writing. The complete word remains doubtful.',
   'medium','new doubt',True,True,True)
ch('a; cancelled direct','direct_deleted',r'\uline{\unsure{direct}}',r'\struck{\ill{}}',r'\uline{\unsure{direct}}',
   'A d-like initial rise and terminal upright strokes can be followed, but the cancellation obscures the middle of the underlined word.',
   'low','retained doubt',False,True,True)
ch('a; Conditions équiv. addition and punctuation','conditions_insert',r'\inserted{Conditions équiv.}',r'\emph{Conditions équiv.} :',r'\inserted{Conditions équiv.}',
   'Conditions équiv. sits above the cancelled predication, with a discrete stop after the v. The space to its right contains no second dot making a colon.',
   kind='insertion and punctuation',marked=True)
ch('a; marginal d’orientation state','dorientation',r"\deleted{\uline{d'orientation}}",r"\note{d'orientation souligné deux fois}",r"\margin{\uuline{d'orientation}}",
   'The letter chain d-apostrophe-orientation remains uncrossed. Two separate horizontal strokes run below its baseline; neither crosses the body of the word. They are double underlining, not deletion.',
   kind='margin note and deletion boundary',against_c=True,against_h=False,marked=True)
ch('a1; cancelled si','si_deleted',r'\deleted{\unsure{si}}',r'\struck{\ill{}}',r'\deleted{\unsure{si}}',
   'A left curling s-like trace and the high dot of i survive around the crossing line, while their baseline strokes remain partly hidden.',
   'low','retained doubt',False,True,True)
ch('a2; punctuation after A','a_punct',r'$\forall a\in A\quad ga$',r'$\forall a\in A$, $ga$',r'$\forall a\in A\quad ga$',
   'The capital A has two sloping sides and a short crossbar. The following space is blank: there is no detached comma or punctuation stroke.',
   kind='punctuation')
ch('a; cancelled brace-like mark','brace_deleted',r'\deleted{\unsure{$\{$|$f$}}',r'\struck{\ill{}}',r'\deleted{\unsure{$\{$|$f$}}',
   'The outer curving stroke has upper and lower right-turning ends, but the blue cancellation adds a central loop and crossing that could belong to f. Neither reading is established.',
   'low','retained doubtful symbol',False,True,True)
ch('a; cancelled item before On dit','b_deleted',r'\deleted{\unsure{b)|Si}}',r'\struck{\ill{}} \uncertain{Déf.}',r'\deleted{\unsure{b)|Si}}',
   'A left upright with a small loop is crossed, and a larger descending parenthesis-like stroke stands to the right. Separate letters é and f cannot be recovered; the b)/Si alternatives remain.',
   'low','retained doubt',False,True,True)
ch('a; cancelled autom. before orientation','autom_deleted',r"\deleted{\unsure{autom.} d'}",r'\struck{\ill{}}',r'\unsure{autom.}',
   'The t ascender, a low m-like ending and the abbreviation stop survive, but a dense horizontal stroke covers the intervening loops.',
   'low','retained doubt',False,True,True)
ch('a; d-apostrophe belongs to cancelled scope','dprime',r"\deleted{\unsure{autom.} d'}\uline{orientation}",r"\emph{d'orientation}",r"\deleted{\unsure{autom.} d'}\uline{orientation}",
   'The d loop, ascender and detached apostrophe are visible. The thin cancellation from autom. continues through d-apostrophe and ends before the following orientation.',
   kind='deletion boundary',marked=True)
ch('b; omega or w','omega',r'$\unsure{\omega|w}(X)$',r'$\omega(X)$',r'$\omega(X)$',
   'The first sign consists of two rounded lobes with an interior upstroke and inward-turning ends; the following (X) is also visible. The sign is omega rather than an angular Latin w.',
   kind='resolved doubt',against_c=True,against_h=False)
ch('b; l’ens terminal punctuation','ens',"l'ens","l'ens.","l'ens",
   'The final connected downhook belongs to s. No detached dot follows the abbreviation before the next word.',
   kind='punctuation')
ch('b; Aut containment addition','aut_insert',r'\inserted{$\subset\operatorname{Aut}(X)$}',r'$\subset\operatorname{Aut}(X)$',r'\inserted{$\subset\operatorname{Aut}(X)$}',
   'An open cup-shaped containment sign and Aut(X) are written above the main baseline, with a descending return stroke toward the gap after omega(X).',
   kind='insertion')
ch('b; cancelled autom. d-apostrophe','autom_b_deleted',r"\deleted{autom. d'}",r"\struck{\ill{}} d'orientation",r"\deleted{\unsure{autom.} d'}",
   'The abbreviation has an initial low bowl, t stem and compressed terminal m under the heavy horizontal cancellation. Its inner loops are obscured. The cancellation continues across d-apostrophe.',
   'low','new doubt and deletion boundary',True,True,True)
ch('b; orientations ending','orientations_b','orientations',"d'orientation",r'\unsure{orientations|orientation}',
   'The uncancelled word begins orientation; its last horizontal/downward hook may include a final s, but the separation of that hook from the n ending is not secure. The preceding d-apostrophe is struck.',
   'medium','word ending and new doubt',True,True,False)
ch('b; complete inverse sentence is interlinear','inverse_insert',r'Si $g\in\omega(X)$, on a $g^{-1}\in\omega(X)$.',r'et si $g\in\omega(X)$, on a $g^{-1}\in\omega(X)$,',r'\inserted{Si $g\in\omega(X)$, on a $g^{-1}\in\omega(X)$.}',
   'The smaller complete sentence begins with capital Si between the b introduction and Alors. Its g carries a raised minus and 1; the final omega(X) and stop precede the separate right-hand parenthetical addition.',
   'medium','insertion and source order',True,True,True)
ch('b; strict parenthetical addition placement','strict_insert',r'\inserted{(si $X$ est strict i.e. si $\unsure{c|(}=\operatorname{card}S\ne2$)}',r'(si $X$ est strict i.e. si $\operatorname{card}S\neq2$)',r'\inserted{(si $X$ est strict i.e. si $\unsure{c|(}=\operatorname{card}S\ne2$)}',
   'The complete smaller parenthesis is above the Alors line, and its return mark descends toward the region after card omega(X)=2. Before card S there is a separate open curved glyph and two parallel equality bars.',
   'medium','insertion order and omitted symbols',False,True,False,math_note='No mathematical correction or choice of attachment from the theorem was made.')
ch('b; c-like glyph in entire strict formula','c_insert',r'$\unsure{c|(}=\operatorname{card}S\ne2$',r'$\operatorname{card}S\neq2$',r'$\unsure{c|(}=\operatorname{card}S\ne2$',
   'The glyph before the equality has a nearly vertical open left curve. A short inward turn allows c, but its length also permits an opening parenthesis. Both equality bars are visible. The entire formula was examined in scan006_strict_insert.jpg as well.',
   'low','retained doubtful formula',False,True,False,math_note='The visible c-like mark and equality were retained even though H omits them.')
ch('b; stop after card omega equals 2','two_punct',r'\unsure{;|,}',',',r'\unsure{;|,}',
   'The mark after 2 contains an upper deposit and a lower loop/tail, with overtracing that prevents a secure distinction between semicolon and comma.',
   'low','retained doubt')
ch('b; cancelled et','et_deleted','et',r'\struck{\ill{}}',r'\unsure{et}',
   'A small e loop and the upper t stroke survive, but the cancellation passes across their join.',
   'medium','new doubt',True,True,True)
ch('b; cancelled si','si_b_deleted','si',r'\struck{\ill{}}',r'\unsure{si}',
   'The i dot and a short upright survive; the s-shaped baseline is crossed by the cancellation.',
   'low','new doubt',True,True,True)
ch('b; cancelled g membership phrase','g_deleted',r'$g\in\unsure{\omega|\omega(X)}$',r'\struck{\ill{}}',r'$\unsure{g\in\omega|g\in\omega(X)}$',
   'The g loop and descender can be followed, while the adjacent membership stroke is partly covered. The whole short formula was inspected in scan006_phrase_deleted.jpg; uncertainty now covers the partly masked membership as well.',
   'low','new doubt scope',True,True,True)
ch('b; cancelled omega and possible (X)','omega_deleted',r'\unsure{\omega|\omega(X)}',r'\struck{\ill{}}',r'$\unsure{g\in\omega|g\in\omega(X)}$',
   'A long heavy horizontal cancellation covers the omega and following region. One curved descending remnant is present; it does not establish or exclude a following (X).',
   'low','retained doubtful formula',False,True,True)
ch('c cancelled definition; ss-grpe','ssgrpe_deleted','ss-grpe','s-groupe',r'\unsure{ss-grpe}',
   'The abbreviation starts with two joined s-like uprights, a detached hyphen and a long descending g loop. The r/p/e chain is compressed and partly intersected by the cancellation; the expanded groupe is not written.',
   'medium','abbreviation and new doubt',True,True,True)
ch('c cancelled definition; formé','forme_deleted','formé',r'\ill{}',r'\unsure{formé}',
   'The initial f has a tall upper loop and long descender. The remaining letters are reduced to low connected strokes under the cancellation, with a small high terminal mark; they do not support removing the doubt.',
   'low','new doubt',True,True,True)
ch('c cancelled definition; whole g membership formula','gin_deleted',r'$g\in\operatorname{Aut}X$',r'\ill{} $\operatorname{Aut}X$',r'$\unsure{g\in\operatorname{Aut}X}$',
   'The g loop is crossed by a diagonal cancellation and the following curved membership-like stroke is partly masked. Aut X can be followed to the right in the complete cancelled-scope crop; the whole formula retains a doubt.',
   'low','new doubtful formula',True,True,True)
ch('c cancelled definition; triviality abbreviation','triv_deleted',r'\unsure{triv$^{\mathrm{lt}}$|triv$^{\mathrm{t}}$}','trivialement',r'\unsure{triv$^{\mathrm{lt}}$|triv$^{\mathrm{t}}$}',
   'A t stem, low r/i/v sequence and a higher terminal stroke cluster are visible. The long crossing line intersects the raised cluster, leaving lt versus t unresolved. There is no written full trivialement.',
   'low','retained doubt and abbreviation',False,True,True)
ch('c cancelled definition; opening [i.e. without closing bracket','ie_deleted','[i.e.','[i.e.]','[i.e.',
   'The left square bracket, i dot, e loop and both abbreviation stops remain visible. The large curve to the right connects with the sweeping cancellation and is not a matching square closing bracket.',
   'medium','punctuation',False,True,True)
ch('c; Aut action arrow','aut_arrow',r'\operatorname{Aut}(X)\unsure{-|\to}\operatorname{Aut}(\omega(X))\simeq\mathbb{Z}/2\mathbb{Z}',r'\operatorname{Aut}(X)\to\operatorname{Aut}(\omega(X))\simeq\mathbf{Z}/2\mathbf{Z}',r'\operatorname{Aut}(X)\unsure{\to|-}\operatorname{Aut}(\omega(X))\simeq\mathbb{Z}/2\mathbb{Z}',
   'The connector is a horizontal stroke ending in a point with a small backward/downward spur. That spur favours a small right arrowhead, but its upper wing is not separately resolved, so a dash remains an alternative. Both Aut expressions and the following quotient were examined together.',
   'medium','retained doubtful formula; preferred order changed',True,True,False,math_note='No inference that a homomorphism must be present was used to remove the arrow doubt.')
ch('c; hom abbreviation','hom','hom','homom.','hom',
   'The word has one tall h, a compressed low o connection and a terminal m run. There is no second om group or final detached stop.',
   kind='abbreviation')
ch('c; ss-grpe before indice','ssgrpe_c','ss-grpe','s-groupe','ss-grpe',
   'Two joined s forms precede a distinct hyphen; the g descender is followed by the compressed r/p/e ending. The expanded ou sequence of groupe is absent.',
   kind='abbreviation')
ch('c; tt abbreviation','tt',r'\unsure{tt|tout}',r'\uncertain{tt}','tt',
   'There are two tall t strokes with a low connecting loop and short cross-stroke; no separate o or u bodies occur between them.',
   kind='resolved doubt',against_c=True,against_h=True,marked=True)
ch('corollary addition; produit ending','produit','produit','produits',r'\unsure{produit|produits}',
   'The p descender, r/o chain and d stem are followed by a compressed low ending. Its final small curl may be an abbreviated t ending or include s; the crop does not warrant a confident singular/plural decision.',
   'medium','new doubt',True,True,False)
ch('corollary addition; direct ending','direct','direct','directs','direct',
   'After the d loop and i dot, the low r/e/c chain ends at a tall t with a right cross-stroke. There is no further s-shaped body before the parenthesis.',
   kind='word ending')
ch('corollary addition; colon','cor_punct',':','',':',
   'Two separated dark dots, one above the other, follow the closing parenthesis.',
   kind='punctuation')
ch('corollary; word or arrow after H','h_est','est',r'$\to$',r'\unsure{est|$\to$}',
   'After H the mark starts with a small curved entry and continues in a long low run, then rises to a dark hooked terminal cluster. That entry and terminal loop permit compressed est; the pointed end also permits an arrow. The ink does not settle the choice.',
   'low','new doubt',True,True,False,math_note='The expected prose construction was not used to suppress the arrow alternative.')
ch('corollary; ss-grpe','ssgrpe_cor','ss-grpe','ss-groupe','ss-grpe',
   'The raised paired s forms and hyphen precede a large g descender and compressed r/p/e run. The crop, rotated upright by three degrees, shows no separate ou group.',
   kind='abbreviation')
ch('corollary parenthesis; etant alternatives','etant',r'\unsure{étant|étans|etant}','dans',r'\unsure{etant|étant|étans|dans}',
   'The upright crop shows an initial open bowl, a joined tall stem and a compressed terminal run with a right upturn. A separate accent cannot be isolated above the initial bowl; the terminal t/s and the initial e-t versus d construction remain unresolved.',
   'low','retained doubt; preferred unaccented reading',True,True,False)
ch('corollary parenthesis; fixé ending','fixee',r'\unsure{fixé|fixée}','fixée',r'\unsure{fixé|fixée}',
   'After the f stem, dotted i and crossing x, a short acute stroke stands over the final e-shaped cluster. Its lower part has two close return strokes, which do not securely distinguish one e from a tightly joined ee ending.',
   'medium','retained doubt')
ch('left margin; drawings and corner retracing','drawing','TikZ lens and pentagon','prose description and simplified drawing',re.search(r'\\figure\{.*?\\end\{tikzpicture\}\}',proposal,re.S).group(0),
   'The dark lens has two filled endpoints joined by two distinct arcs. The blue drawing has five corners and five boundary segments; its lower-right segment is retraced, with short hooks at the corners and a detached small deposit near the bottom corner. A short downward-right hook at the upper-left pentagon corner is included.',
   kind='drawing detail',against_c=True,against_h=True)
ch('lower left archive numeral','archive5','% archive sheet number: 5',r'\page{5}','% archive sheet number: 5',
   'The isolated low-left numeral has a short upper horizontal, descending left turn and a large lower bowl: 5. It lies outside the main text block at the foot, not at the head of the manuscript text.',
   kind='archive mark',against_c=False,against_h=False)
ch('a; punctuation after de X','a_x_punct',r'$X$',r'$X$.',r'$X$',
   'The two crossing diagonals of X end before an empty interval leading to the cancelled predication. No detached stop occurs in that interval.',
   kind='punctuation')

doubts=[
('heading cancelled short word',r'\deleted{\unsure{Ch.|En.}}',['Ch.','En.'],'low'),
('Soit cancelled suffix',r'\deleted{\unsure{s|x}}',['s','x'],'low'),
('inserted and cancelled strict',r'\inserted{\deleted{\unsure{strict}}}',['strict','unresolved interior letters'],'low'),
('a cancelled Un',r'\deleted{\unsure{Un}}',['Un','unresolved n'],'medium'),
('a cancelled est',r'\unsure{est}',['est','unresolved crossed join'],'medium'),
('a cancelled dit',r'\unsure{dit}',['dit','unresolved middle stroke'],'medium'),
('a cancelled direct',r'\uline{\unsure{direct}}',['direct','unresolved middle letters'],'low'),
('a1 cancelled si',r'\deleted{\unsure{si}}',['si','unresolved baseline letters'],'low'),
('a cancelled brace-like mark',r'\deleted{\unsure{$\{$|$f$}}',[r'$\{$',r'$f$'],'low'),
('a cancelled item before On dit',r'\deleted{\unsure{b)|Si}}',['b)','Si','H suggests Déf.'],'low'),
('a cancelled autom.',r'\unsure{autom.}',['autom.','unresolved interior letters'],'low'),
('b cancelled autom.',r'\unsure{autom.}',['autom.','unresolved interior letters'],'low'),
('b orientations ending',r'\unsure{orientations|orientation}',['orientations','orientation'],'medium'),
('b strict formula',r'$\unsure{c|(}=\operatorname{card}S\ne2$',['c=card S≠2','(=card S≠2'],'low'),
('b punctuation after 2',r'\unsure{;|,}',[';',','],'low'),
('b cancelled et',r'\unsure{et}',['et','unresolved join'],'medium'),
('b cancelled si',r'\unsure{si}',['si','unresolved s'],'low'),
('b cancelled membership formula',r'$\unsure{g\in\omega|g\in\omega(X)}$',[r'g\in\omega',r'g\in\omega(X)','membership stroke partly covered'],'low'),
('c cancelled ss-grpe',r'\unsure{ss-grpe}',['ss-grpe','unresolved compressed ending'],'medium'),
('c cancelled formé',r'\unsure{formé}',['formé','unresolved low letters'],'low'),
('c cancelled membership formula',r'$\unsure{g\in\operatorname{Aut}X}$',[r'g\in\operatorname{Aut}X','membership partly covered'],'low'),
('c cancelled triv abbreviation',r'\unsure{triv$^{\mathrm{lt}}$|triv$^{\mathrm{t}}$}',[r'triv$^{\mathrm{lt}}$',r'triv$^{\mathrm{t}}$'],'low'),
('c Aut action formula',r'$\operatorname{Aut}(X)\unsure{\to|-}\operatorname{Aut}(\omega(X))\simeq\mathbb{Z}/2\mathbb{Z}$',[r'\to','-'],'medium'),
('corollary produit ending',r'\unsure{produit|produits}',['produit','produits'],'medium'),
('corollary after H',r'$H$ \unsure{est|$\to$}',['est',r'$\to$'],'low'),
('corollary etant',r'\unsure{etant|étant|étans|dans}',['etant','étant','étans','dans'],'low'),
('corollary fixé',r'\unsure{fixé|fixée}',['fixé','fixée'],'medium')]
doubts=[dict(place=p,reading=r,alternatives=a,confidence=c) for p,r,a,c in doubts]
inventory=[]
def inv(element,kind,pos,words,hand='main blue cursive hand'):
    inventory.append(dict(element=element,kind=kind,position=pos,first_words_or_objects=words,sheet_kind='manuscript leaf',hand=hand,transcribed='yes'))
inv('opening','text','upper text, y 65–218','Ils correspondent aux sous-groupes')
inv('opening H','insertion','above opening, x 1040–1136, y 35–123','H')
inv('orientation heading','text','y 294–365',"Orientation d'un contour")
inv('cancelled heading abbreviation','deletion','right end of heading, y 294–352','Ch.|En.')
inv('proposition','text','y 374–448','Prop Soit X=(S,A,R)')
inv('Soit suffix','deletion','after Soit, y 375–437','s|x')
inv('strict interlinear word','insertion','above contour/connexe, y 335–423','strict')
inv('strict cancellation','deletion','above contour/connexe, y 335–423','strict')
inv('dark lens','drawing','left margin, x 60–202, y 401–565','two vertices and two arcs','dark graphitic strokes; hand not distinguishable from the drawing alone')
inv('blue pentagon','drawing','left margin, x 177–479, y 507–811','five corners, five boundary segments, retracing and corner hooks')
inv('a proposition clause','text','y 433–534','a) Soit g un autom.')
inv('a replacement phrase','insertion','above cancelled Un, y 433–492','Soit g un')
inv('a initial cancelled Un','deletion','y 472–523','Un')
inv('a cancelled predication','deletion','y 466–534','est dit direct.')
inv('a conditions addition','insertion','above cancelled predication, y 425–498','Conditions équiv.')
inv('d’orientation marginal qualification','margin note','left of first condition below autom. g, x 509–777, y 545–620',"d'orientation; two underlines")
inv('condition one','display','y 545–622','1°) ∀s∈S, s est lié à gs')
inv('condition one cancelled si','deletion','y 552–607','si')
inv('condition two','display','y 629–706','2°) ∀a∈A ga est lié à a')
inv('cancelled brace-like mark','deletion','left of condition two, x 529–594, y 640–722','{|f')
inv('orientation definition','text','y 719–819','On dit que g est une orientation de X.')
inv('cancelled item before definition','deletion','x 450–533, y 737–813','b)|Si')
inv('cancelled autom. d-apostrophe','deletion','x 1241–1548, y 718–790',"autom. d'")
inv('b introduction','text','y 824–899',"b) Soit ω(X) l'ens des orientations de X")
inv('containment addition','insertion','above b introduction, x 785–1027, y 770–859','⊂Aut(X)')
inv('b cancelled autom. d-apostrophe','deletion','y 826–887',"autom. d'")
inv('inverse sentence','insertion','interline left, x 434–941, y 870–938','Si g∈ω(X), on a g⁻¹∈ω(X).')
inv('strict parenthesis','insertion','interline right, x 934–1536, y 858–939','(si X est strict i.e. si c=card S≠2)')
inv('b cardinality and generating pair','text','y 923–1038','Alors card ω(X)=2; et si')
inv('b cancelled phrase','deletion','x 1008–1538, y 920–985','et si g∈ω[(X)]')
inv('c cancelled definition','deletion','x 350–1652, y 1023–1245','Soit Aut⁺(X)⊂Aut(X) le ss-grpe')
inv('c action formula','display','y 1232–1313','Aut(X) → Aut(ω(X)) ≃ Z/2Z')
inv('c homomorphism and kernel','text','y 1312–1479',"C'est un hom surjectif, i.e. le noyau")
inv('c cyclic group sentence','text','y 1512–1675','De plus, Aut⁺(X) est un groupe cyclique')
inv('corollary','text','y 1731–2055','Corollaire Aut(X)≃Z/2Z·Z/H')
inv('corollary product addition','insertion','above corollary formula, x 1233–1620, y 1660–1730','(produit 1/2 direct):')
inv('corollary group formula','display','y 1731–1820','Aut(X)≃Z/2Z·Z/H')
inv('archive numeral','margin note','lower left, x 37–89, y 2268–2322','5','dark pencil-like numeral; hand not securely assigned')

boxes=[]
def sb(kind,box,reading):
    x0,y0,x1,y1=box
    boxes.append(dict(box=f'b{len(boxes)+1:02}',kind=kind,x0=x0,y0=y0,x1=x1,y1=y1,reading=reading))
# Every individual disagreement/doubt crop is given to the second reader.
for c in changes:
    if c['kind']=='drawing detail': k='drawing'
    elif c['kind']=='archive mark': k='penned number'
    elif 'formula' in c['kind'] or 'symbol' in c['kind']: k='doubtful formula'
    elif 'insertion' in c['kind']: k='insertion'
    elif 'margin' in c['kind']: k='margin note'
    elif 'deleted' in c['place'] or 'cancelled' in c['place'] or 'deletion' in c['kind']: k='deletion'
    else: k='different word'
    sb(k,c['box'],c['final'])
# Complete scopes and complete formulas, in addition to letter-level boxes.
full_c=next(x for x in proposal.splitlines() if x.startswith('c) '))
sb('deletion',m['c_deleted_scope']['box'],full_c)
sb('deletion',[1135,466,1633,534],r'\deleted{\unsure{est} \unsure{dit} \uline{\unsure{direct}}.}')
sb('deletion',[1241,718,1548,790],r"\deleted{\unsure{autom.} d'}")
sb('deletion',m['phrase_deleted']['box'],r'\deleted{\unsure{et} \unsure{si} $\unsure{g\in\omega|g\in\omega(X)}$}')
sb('doubtful formula',[1150,918,1538,989],r'$\unsure{g\in\omega|g\in\omega(X)}$')
sb('doubtful formula',[650,1095,1030,1185],r'$\unsure{g\in\operatorname{Aut}X}$')
sb('doubtful formula',[650,770,1030,895],r'$\omega(X)$\inserted{$\subset\operatorname{Aut}(X)$}')
sb('doubtful formula',[1252,858,1536,939],r'$\unsure{c|(}=\operatorname{card}S\ne2$')
sb('doubtful formula',m['aut_arrow']['box'],r'$\operatorname{Aut}(X)\unsure{\to|-}\operatorname{Aut}(\omega(X))\simeq\mathbb{Z}/2\mathbb{Z}$')
sb('doubtful formula',m['h_est']['box'],r'$H$ \unsure{est|$\to$}')
sb('insertion',[1233,1660,1620,1730],r'\inserted{(\unsure{produit|produits} $\frac{1}{2}$ direct):}')
# Numerals, with complete adjacent formula where necessary for the second reading.
sb('penned number',[775,543,875,622],r'$1^{\circ})$')
sb('penned number',[775,625,879,706],r'$2^{\circ})$')
sb('penned number',m['inverse_insert']['box'],r'\inserted{Si $g\in\omega(X)$, on a $g^{-1}\in\omega(X)$.}')
sb('penned number',[1252,858,1536,939],r'$\unsure{c|(}=\operatorname{card}S\ne2$')
sb('penned number',[583,927,996,996],r'$\operatorname{card}\omega(X)=2$')
sb('penned number',[912,975,1538,1040],r'$\omega(X)=\{g,g^{-1}\}$')
sb('penned number',m['aut_arrow']['box'],r'$\operatorname{Aut}(X)\unsure{\to|-}\operatorname{Aut}(\omega(X))\simeq\mathbb{Z}/2\mathbb{Z}$')
sb('penned number',[1110,1405,1450,1487],r"d'indice $2$")
sb('penned number',m['half']['box'],r'$\frac{1}{2}$')
sb('penned number',[690,1728,1410,1820],r'$\operatorname{Aut}(X)\simeq\mathbb{Z}/2\mathbb{Z}\cdot\mathbb{Z}/H$')
sb('penned number',[1390,1825,1665,1940],r'$g^{n}=1$')
# c superscript-plus formula is not a numeral but is included as a whole cancelled formula.
sb('deletion',[690,1023,1210,1112],r'$\operatorname{Aut}^{+}(X)\subset\operatorname{Aut}(X)$')

coverage=[
'Scan marker 6 is editorial metadata; lower archive 5 is recorded separately, without inventing a manuscript heading.',
'Five dots retained (c02); both drawings transcribed in TikZ, with detailed ink marks (c50).',
'Cancelled short-word alternatives retained; H déf. not adopted (c03).',
'No independent period after Prop (c04).',
'Cancelled s/x suffix retained (c05).',
'Strict retained uncertain, and its interlinear insertion plus cancellation marked (c06).',
'Minipage/TikZ token stretch is chiefly formatting. All drawing objects are represented; a) lexical differences handled separately.',
'Soit belongs to the interlinear replacement Soit g un (c08); H order is not followed.',
'Same replacement scope as row 8; cancelled Un remains uncertain (c09).',
'Cancelled est, dit, direct each cropped and retained with uncertainty (c10–c12).',
'Doubly underlined marginal d’orientation is not cancelled (c14); Conditions addition has a stop but no colon (c13).',
'1-degree typographic syntax only; source numeral and degree checked and included in second_boxes.',
'Cancelled si retained doubtful (c15); H itemize delimiter is macro syntax.',
'H itemize delimiter only; condition text read in full.',
'2-degree typographic syntax only; source numeral and degree included in second_boxes.',
'H itemize delimiter only.',
'No comma between A and ga (c16).',
'Cancelled brace/f and b)/Si retained (c17–c18); H marginal double underline accepted (c14); no secure Déf. read.',
'Autom. remains uncertain and d-apostrophe is within cancellation, while orientation remains underlined (c19–c20).',
'Minipage closing syntax only.',
'Omega resolved from its two rounded lobes (c21).',
'No stop after l’ens (c22).',
'Cancelled autom. d-apostrophe marked and orientation(s) ending remains doubtful (c24–c25).',
'Physical order retained: inverse sentence at left and strict parenthesis at right above Alors; H relocation rejected (c26–c28).',
'Alors card omega(X)=2 retained; punctuation remains ;/comma (c29).',
'Each cancelled et/si/formula component examined (c30–c33); c-like glyph and equality in strict insertion retained (c28).',
'Entire Si ... inverse sentence is interlinear addition, rather than only the inverse formula (c26).',
'Cancelled ss-grpe is literal abbreviation; uncertainty preserved (c34).',
'Same hyphenated word as row 28; grpe not expanded to groupe (c34).',
'Cancelled formé retained with new uncertainty (c35).',
'Cancelled whole g-membership formula retains uncertainty (c36).',
'Literal triv with unresolved raised lt/t retained; no expansion to trivialement (c37).',
'No square closing bracket supplied after [i.e. (c38).',
'H display delimiter only.',
'Arrow/dash retained uncertain; small endpoint spur favours arrow (c39).',
'H display closing delimiter only.',
'Literal hom retained, without H expansion homom. (c40).',
'Literal doubled ss abbreviation retained (c41).',
'Literal grpe retained, not groupe (c41).',
'tt resolved from two t strokes; no tout expansion (c42).',
'H display delimiter only.',
'Produit/produits retained doubtful (c43); visible 1/2 recorded; direct singular (c44).',
'Colon follows insertion parenthesis (c45).',
'H display delimiter only.',
'Est/arrow remains doubtful after H (c46).',
'Literal ss-grpe retained (c47).',
'Etant/étant/étans/dans unresolved; unaccented form first because no separate accent is isolated (c48).',
'Fixé/fixée retained doubtful (c49).']
assert len(coverage)==48
lines=[
'L01 y35–123: Ils correspondent aux sous-groupes [H inserted] de Z, distincts de Z.',
'L02 y160–220: (c=card Z/H).....',
'L03 y294–365: underlined Orientation d’un contour : [cancelled Ch.|En.].',
'L04 y335–448: Prop Soit [cancelled s|x] X=(S,A,R) un contour [interlinear cancelled strict] connexe ≠phi.',
'L05 y425–534: a) [cancelled Un] [Soit g un added] autom. g de X [est dit direct. cancelled] [Conditions équiv. added].',
'L06 y545–622: doubly underlined marginal d’orientation; 1°) [si cancelled] ∀s∈S, s est lié à gs.',
'L07 y629–722: 2°) ∀a∈A ga est lié à a; cancelled brace/f at left.',
'L08 y719–813: [cancelled b)|Si] On dit que g est une [autom. d’ cancelled] orientation underlined.',
'L09 y790–819: de X.',
'L10 y770–899: b) Soit omega(X) [⊂Aut(X) inserted] l’ens des [autom. d’ cancelled] orientations|orientation de X.',
'L11 y870–938 left addition: Si g∈omega(X), on a g⁻¹∈omega(X).',
'L12 y858–939 right addition: (si X est strict i.e. si [c|(]=card S≠2).',
'L13 y920–995: Alors card omega(X)=2 [;|,] [et si g∈omega[(X)] cancelled], et.',
'L14 y975–1040: si g∈omega(X), on a omega(X)={g,g⁻¹}.',
'L15 y1023–1112: c) [cancelled Soit Aut⁺(X)⊂Aut(X) le ss-grpe de Aut X].',
'L16 y1095–1185: [cancelled formé par les g∈Aut X].',
'L17 y1160–1245: [cancelled tels que g opère triv^(lt|t) sur omega(X) [i.e.].',
'L18 y1232–1313: Considérons Aut(X) [arrow|dash] Aut(omega(X))≃Z/2Z.',
'L19 y1312–1393: C’est un hom surjectif, i.e. le noyau.',
'L20 y1405–1487: Aut⁺(X) est un ss-grpe d’indice 2.',
'L21 y1512–1580: De plus, Aut⁺(X) est un groupe cyclique.',
'L22 y1600–1675: engendré par tt g∈omega(X).',
'L23 y1660–1730 interlinear: (produit|produits 1/2 direct):.',
'L24 y1728–1820: Corollaire Aut(X)≃Z/2Z·Z/H, où H [est|arrow].',
'L25 y1825–1951: le ss-grpe de Z formé des n∈Z tels que gⁿ=1.',
'L26 y1937–2055: (g [etant|étant|étans|dans] une orientation [fixé|fixée]).']
record=dict(
 scan='scan006',line_count=len(lines),changes=changes,doubts=doubts,inventory=inventory,second_boxes=boxes,
 notation=[
 r'\phi: closed small bowl with long descending stem in connexe \ne\phi; matches the current notation table.',
 r'\omega(X): two rounded lobes distinguish omega from Latin w; first C omega/w doubt resolved.',
 r'Literal abbreviations retained: autom., l’ens, i.e., ss-grpe, hom, tt, and doubtful triv with raised lt/t.',
 r'\operatorname{Aut}^{+}(X), \mathbb{Z}/2\mathbb{Z}, g^{-1}, and \frac12 preserved as written; no algebraic normalization.',
 'Double underlining under d’orientation is an emphasis mark, not a cancellation.'
 ],
 hand_habits=[
 'The paired s abbreviation in ss-grpe can resemble two linked upright strokes; the g has a conspicuous deep loop and the r/p/e ending is compressed.',
 'Short words such as est may collapse to a long low run with an upturned terminal cluster, sometimes resembling a small arrow.',
 'Cancelled text is often struck with a long horizontal line and then sweeping diagonal or curved strokes; these intersect individual letters and require retained doubt.',
 'Interlinear additions are smaller and have return marks; the inverse sentence is written in the interline as a complete sentence.',
 'The written tt abbreviation has two tall strokes and a low connecting loop; it has no intervening o/u letter bodies.'
 ],
 notes=[
 'Restricted reading: only scan006 packet, the supplied rules/preamble and current notation table were consulted for this page. No other page, global witness, web source, OCR or TeX compilation was used.',
 'Full-page entry was attempted once for layout; its image output was unavailable after tool truncation. Both supplied halves were successfully inspected once. Source-order text, agreements, all symbols and every C deleted/inserted scope were compared with C and H.',
 'All 55 crop files derive from original J75-01_75_scan006.jpg coordinates, use autocontrast and LANCZOS enlargement to a maximum dimension of 2800 px, and were saved as JPEG quality 94. Existing files were preserved. Crop rotations are recorded in crop_boxes.json.',
 'The six c-deletion crops had an inaccessible, truncated first output and were then displayed successfully once. Other successful crop inspections were not repeated.',
 'Original-coordinate boxes refer to the unrotated 1690×2358 image. The arrow crop was rotated -1 degree; the final ss-grpe, etant and fixé word crops were rotated -3 degrees to level their writing.',
 'The line_count is 26 source-order written-line units, including detached interlinear segments. It excludes the archive numeral. Adjacent inserted words are recorded with their base line and separately inventoried.',
 'Drawing count pass 1, following the boundary clockwise: lens two endpoints/two arcs; pentagon upper-left, upper-right, right-lower, bottom, left-lower = five corners and five connecting boundary segments.',
 'Drawing count pass 2, following connections counterclockwise from the bottom: pentagon bottom→left-lower→upper-left→upper-right→right-lower→bottom = five segments/five corners; lens lower-left→upper-right by outer arc and back by inner arc = two arcs/two endpoints. The lower-right retracing is not counted as an additional edge. All visible hooks and the small bottom deposit are represented in TikZ.',
 'Numeral review boxes include both numbered conditions, both inverse exponents -1, both card-related 2s, the two quotient denominators 2, index 2, numerator/denominator 1/2, terminal constant 1, and the archive 5. Some number boxes retain the adjoining whole formula to avoid isolating a superscript.',
 'No mathematical claim was proved, refuted, or used to repair the ink in this first-reader pass. Accordingly check_events is empty. The root agent is handling its own independent mathematical check.',
 'The two drawings are kept together in TikZ before a); their exact left-margin source positions are preserved in inventory and boxes. The marginal qualification uses the supplied margin macro outside a minipage.',
 'marked_in_H records an explicit uncertainty, cancellation or editorial/marginal note at the relevant locus. Ordinary alphabet/font macro differences were not counted as substantive disagreements.'
 ],
 check_events=[],
 deleted_inserted_check=[
 'Opening H: inserted above the sous-groupes/de gap; retained insertion.',
 'Heading short word: cancellation confirmed; Ch./En. remains doubtful.',
 'Soit suffix: cancellation confirmed; s/x unresolved.',
 'Strict: interlinear position and return caret show insertion, subsequently cancelled; doubt retained.',
 'a Un: struck original beneath Soit g un; uncertainty added because cancellation masks n.',
 'a Soit g un: entire replacement phrase is above the line.',
 'a est dit direct.: original predication cancelled; each differing word separately cropped, and letter-level doubts retained.',
 'a Conditions équiv.: interlinear replacement; no colon supplied.',
 'a d’orientation: two underlines below the letters; cancellation rejected.',
 'a1 si: struck; retained doubt.',
 'Brace/f: crossed mark to left of second condition; no secure symbol resolution.',
 'b)/Si before On dit: struck; H Déf. cannot be recovered from the surviving letters.',
 'a autom. d-apostrophe: cancellation extends through d-apostrophe but not orientation.',
 'b containment ⊂Aut(X): interlinear addition with return mark.',
 'b autom. d-apostrophe: both parts cancelled; abbreviation interior remains doubtful.',
 'b inverse sentence: complete smaller interlinear sentence marked inserted.',
 'b et si g∈omega[(X)]: entire short phrase struck; individual et, si, g/membership and omega region cropped, and whole formula retained doubtful.',
 'b strict parenthesis: smaller interlinear addition located above the Alors clause; c-like mark and equality preserved.',
 'c Soit Aut⁺... [i.e.: all three written lines fall inside the same sweeping cancellation; opening bracket survives, no square closing bracket added. Word and formula doubts retained.',
 'Corollary product parenthesis with 1/2 and colon: interlinear addition retained; produit singular/plural remains doubtful.'
 ],
 diff_coverage=[dict(row=i+1,disposition=t) for i,t in enumerate(coverage)],
 lines_read=lines)
(out/'record.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'changes':len(changes),'doubts':len(doubts),'inventory':len(inventory),'second_boxes':len(boxes),'diff_rows':len(coverage),'line_count':len(lines)},ensure_ascii=False))
