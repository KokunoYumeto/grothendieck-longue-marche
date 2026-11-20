from pathlib import Path
import sys,json
sys.path.insert(0,str(Path('SP02_CW_10+12/scripts').resolve()))
from root_record import Record
r=Record('B12-01',12,97,'text')
insert=r'''\mbox{\begin{tikzpicture}[baseline=(old.base)]
\node[inner sep=0] (old) {\deleted{longtemps}};
\node[anchor=south west,inner sep=0,xshift=-1.7em,yshift=1.1ex] (added) at (old.north west) {\inserted{l'invention de la cohomologie $\unsure{\rlap{o}\handwritten{\ell}|\rlap{b}\handwritten{\ell}}$-adiq\handwritten{u\unsure{e}}}};
\node[anchor=south east,inner sep=0,yshift=.5ex] (ref) at (added.north east) {\handwritten{\unsure{([\quad]|[\quad])}}};
\draw (old.south west) .. controls +(0,.4) and +(-.4,-.1) .. (added.south west) .. controls +(-.4,0) and +(-.4,0) .. (added.north west) -- ([xshift=-1.5em]ref.south west) -- (ref.north west) -- (ref.north east) -- (added.south east) -- ([xshift=.3em]old.north east) .. controls +(0,-.1) and +(0,.2) .. ([xshift=.3em]old.south east);
\end{tikzpicture}}'''
r.edit(r"\deleted{longtemps}\inserted{l'invention de la cohomologie $\handwritten{\ell}$-adique \handwritten{\unsure{([\quad]|[\quad])}}}",insert)
r.edit(r'\deleted{\unsure{,|x}}',r'\deleted{\unsure{x|,}}')
coho=r'''\mbox{\begin{tikzpicture}[baseline=(old.base)]
\node[inner sep=0] (old) {\deleted{dernière}};
\node[anchor=south west,inner sep=0,xshift=.2em,yshift=.4ex] at (old.north west) {\inserted{\handwritten{cohomologie}}};
\end{tikzpicture}}'''
r.edit(r'\deleted{dernière}\inserted{\handwritten{cohomologie}}',coho)
net=r'''n\rlap{\handwritten{e}}\deleted{\unsure{o|e}}t\mbox{\begin{tikzpicture}[baseline=(old.base)]
\node[inner sep=0] (old) {\deleted{ablem}};
\node[anchor=base west,inner sep=0] at (old.base west) {\handwritten{t}};
\node[anchor=base,inner sep=0,xshift=-.3em] at (old.base) {\handwritten{e}};
\node[anchor=base east,inner sep=0] at (old.base east) {\handwritten{m}};
\end{tikzpicture}}ent'''
r.edit(r'n\deleted{\unsure{o|e}}\handwritten{e}t\deleted{\unsure{ablem|able}}\handwritten{tem}ent',net)
r.edit(r'd\handwritten{e}\deleted{leur solution}',r'd\rlap{\handwritten{e}}\deleted{leur solution}')
date=r'''\mbox{\begin{tikzpicture}[baseline=(base.base)]
\node[inner sep=0] (base) {de cette méthode,};
\node[anchor=south west,inner sep=0,yshift=.6ex] at (base.north west) {\inserted{\deleted{(qui remonte à 1964)}}};
\end{tikzpicture}}'''
r.edit(r'de cette méthode\inserted{\deleted{(qui remonte à 1964)}},',date)
r.edit('N°1',r'N\textsuperscript{\uline{o}}1')
r.edit('n°2',r'n\textsuperscript{\uline{o}}2')
r.edit(r'\deleted{\unsure{Le pr}}',r'\deleted{Le pr}')
la=r'''\mbox{\begin{tikzpicture}[baseline=(old.base)]
\node[inner sep=0] (old) {\deleted{\unsure{ux|la}}};
\node[anchor=south west,inner sep=0,yshift=.6ex] (added) at (old.north west) {\inserted{la}};
\draw ([xshift=-.2em]added.west) .. controls +(0,-.3) and +(-.2,0) .. (old.south west) -- (old.south east) -- ([xshift=.4em,yshift=.1em]added.north east);
\end{tikzpicture}}'''
r.edit(r'\deleted{\unsure{ux|la}}\inserted{la}',la)
system=r'''\mbox{\begin{tikzpicture}[baseline=(base.base)]
\node[inner sep=0] (base) {considération\deleted{\unsure{s}}};
\node[anchor=base west,inner sep=0,xshift=.4em] (right) at (base.base east) {des ``poids'' des};
\node[anchor=south west,inner sep=0,xshift=-1em,yshift=.8ex] (added) at (base.north east) {\inserted{systématique}};
\draw ([xshift=-.3em,yshift=-.5ex]base.south east) .. controls +(0,.4) and +(-.3,0) .. (added.south west) -- (added.south east) .. controls +(.2,0) and +(0,-.2) .. ([xshift=.2em]added.east);
\end{tikzpicture}}'''
r.edit(r"considération\deleted{s}\inserted{systématique} des ``poids'' des",system)
analog=r'''\mbox{\begin{tikzpicture}[baseline=(du.base)]
\node[inner sep=0] (du) {\deleted{du}};
\node[anchor=base west,inner sep=0,xshift=.5em] (old) at (du.base east) {\deleted{même principe}};
\node[anchor=base west,inner sep=0] at (du.base west) {\handwritten{ana}};
\node[anchor=south west,inner sep=0,xshift=.3em,yshift=.2ex] at (old.north west) {\inserted{\handwritten{logues}}};
\end{tikzpicture}}'''
r.edit(r'\deleted{du même principe}\inserted{\handwritten{analogues}}',analog)
develop=r'''\mbox{\begin{tikzpicture}[baseline=(left.base)]
\node[inner sep=0] (left) {était};
\node[anchor=base west,inner sep=0,xshift=.4em] (base) at (left.base east) {également};
\node[anchor=south west,inner sep=0,xshift=-.3em,yshift=.6ex] (added) at (base.north west) {\inserted{\handwritten{développé}}};
\draw ([xshift=.2em,yshift=-.4ex]left.south east) .. controls +(0,.4) and +(-.3,0) .. (added.south west) -- (added.south east) .. controls +(.2,0) and +(0,-.3) .. ([xshift=.2em]added.north east);
\end{tikzpicture}}'''
r.edit(r'était\inserted{\handwritten{développé}} également',develop)
exemple=r'exemp\unsure{\rlap{o}l|\rlap{b}l}e'
r.edit(r'\unsure{exempbe|exemple}',exemple)
sujette=r'''\mbox{\begin{tikzpicture}[baseline=(old.base)]
\node[inner sep=0] (old) {\deleted{limitée}};
\node[anchor=south west,inner sep=0,xshift=-.4em,yshift=.7ex] (added) at (old.north west) {\inserted{\handwritten{sujette à caut\unsure{in|ion}}}};
\draw ([yshift=-.5ex]old.south east) .. controls +(0,.5) and +(-.3,0) .. (added.south) .. controls +(.5,0) and +(0,-.3) .. (added.north east);
\end{tikzpicture}}'''
r.edit(r'\deleted{limitée}\inserted{\handwritten{sujette à caution}}',sujette)
def ch(place,C,H,final,shows,crop,kind='other',confidence='high',against_C=False,against_H=True,consequential=False):r.change(place,C,H,final,shows,crop,kind,confidence,against_C,against_H,False,consequential)
ch('first raised insertion and its enclosing stroke',r"longtemps + inserted l'invention de la cohomologie ell-adique",r"struck longtemps + inline l'invention...; note says the whole addition is handwritten",insert,'The added phrase is typed on a raised line. A hand-drawn outline encloses it, steps upward around the separately raised reference at the right, and descends on both sides of cancelled longtemps. H wrongly calls the whole phrase handwritten and flattens its placement. C retains insertion state but omits this enclosing/connecting line.','inventionlayout;invention1;invention2;longtemps','insertion or placement',against_C=True)
ch('ell cell in the first raised insertion',r'\handwritten{\ell}',r'\ell',r'\unsure{\rlap{o}\handwritten{\ell}|\rlap{b}\handwritten{\ell}}','The cell has a typed left top serif, tall stem and broad foot, an additional rounded lower impression extending left of the stem, a second right arc, and a hand diagonal stroke. The extra round impression is not represented by a clean ell; o is the first qualified reading, b the alternative. The similarly altered cell in exemp...e is compared visually, not used to infer the mathematics.','insertell;topellfine;examplecell;examplelcontrol','misread symbol or index','medium',True,True,True)
ch('right end of first raised insertion','-adique','-adique',r'-adiq\handwritten{u\unsure{e}}','After typed adiq the final cells have heavier handwritten retracing. The u trough is visible; the terminal e-shaped ink reaches the dark right edge and its complete contour cannot be separated. No invisible continuation is supplied.','insertending;invention2','misread word','medium',True)
ch('reference above first raised insertion',r'\unsure{([\quad]|[\quad])}',r'[ ]',r'\unsure{([\quad]|[\quad])} raised above the phrase','A separate left curved stroke precedes two square reference brackets. The right side runs into the enclosing vertical stroke, preventing a secure decision about a final parenthesis. The inner slot is empty. C macro/table uncertainty is retained and its raised level preserved.','reference1;firstref;inventionlayout','insertion or placement','low')
ch('after que',r'\deleted{\unsure{,|x}}','omitted',r'\deleted{\unsure{x|,}}','The visible dark cell has crossed diagonals and upper/lower x feet. An underlying comma cannot be isolated. The directly visible x is put first; the alternative comma remains qualified. H has no trace of the cancellation.','quecancel','deletion state','low',True)
ch('cancelled notation before pi',r'\deleted{\unsure{\operatorname{Gal}k|G_k|G(k)}}','omitted',r'\deleted{\unsure{\operatorname{Gal}k|G_k|G(k)}}','Repeated diagonal hand strokes obscure the typed group notation. Left curves, middle feet and the last k-like portions remain, but do not select securely among C alternatives. The whole cancelled locus is preserved with its uncertainty.','Gcancel','omission','low')
ch('cohomology coefficient',r'\underline{Z}_{\handwritten{\ell}}',r'\mathbb{Z}_{\ell}',r'\underline{Z}_{\handwritten{\ell}}','A separate horizontal line lies below the typed Z. The lowered ell has its own crossing stroke; there is no doubled Z upright establishing blackboard bold.','Hformula','misread symbol or index',consequential=True)
ch('replacement above dernière',r'\deleted{dernière}\inserted{\handwritten{cohomologie}}',r'\struck{dernière} cohomologie',coho,'The full cancelled dernière, including grave, remains on the baseline. Handwritten cohomologie stands above it, begins slightly right of its left edge and extends beyond its right edge. The word was rotated for a separate upright reading; no attachment leader is present.','derniere;cohomologie;cohomorot;cohomoplace','insertion or placement',against_C=True)
ch('corrected adverb, old second letter',r'\deleted{\unsure{o|e}}\handwritten{e}','nettement',r'\rlap{\handwritten{e}}\deleted{\unsure{o|e}}','A broad handwritten e lies over a rounded typed impression. Its old middle or right edge cannot be separated sufficiently to decide o/e; C doubt remains. The two components are superposed rather than printed consecutively. H loses the old letter altogether.','nettement;nettementoldfirst','deletion state','medium',True)
ch('corrected adverb, old central letters',r'\deleted{\unsure{ablem|able}}\handwritten{tem}','nettement',r'\deleted{ablem} with overlapping handwritten tem','The typed a lower bowl, b ascender/right bowl, l tall serif/stem, e crossbar and m upright/arches remain beneath the wider hand strokes t/e/m. The final typed m is visible as a distinct cell before the untouched ent; the alternative able is dropped. Placement is reproduced by overlapping nodes.','nettement;nettementoldmiddle','deletion state','high',True)
ch('de and cancelled leur solution',r'd\handwritten{e}\deleted{leur solution}',r'de \struck{solution}',r'd\rlap{\handwritten{e}}\deleted{leur solution}','The added e covers the first cell of cancelled leur, rather than preceding it as a separate baseline letter. The remaining old letters and the next-line solution are under typed crosses/hand cancellation. H omits old leur; the continued cancellation is retained in full.','deleur;deoverlap;solutiondel','deletion state','medium',True)
ch('cancelled date clause',r'de cette méthode\inserted{\deleted{(qui remonte à 1964)}},',r'note only: (qui remonte à 1964), said to be after relatives à un corps',date,'The parenthesis is typed on the line above de cette méthode, left aligned near de and ending over the following qui. Its letters/digits remain legible beneath typed crosses and a hand stroke. H mislocates it after the preceding line; the manuscript position is restored without inventing an attachment leader.','dateinsert;dateplace','insertion or placement',against_C=True)
ch('Nº1 and nº2','N°1; n°2','N° 1; n° 2',r'N\textsuperscript{\uline{o}}1; n\textsuperscript{\uline{o}}2','Both raised round o signs have a separate short horizontal stroke directly beneath them. Capital N occurs at the first reference and lowercase n at the second; 1 and 2 remain on the baseline.','numero1;numero2','misread symbol or index',against_C=True)
ch('cancelled restart before L’idée',r'\deleted{\unsure{Le pr}}','omitted',r'\deleted{Le pr}','The L top/foot, e bar/bowl, p descender/bowl and r shoulder are independently visible under the x row. C macro/table doubt is resolved; no continuation of the fragment is supplied.','Lepr','omission',against_C=True)
ch('cancelled two letters after liés à',r'\deleted{\unsure{ux|la}}','omitted',r'\deleted{\unsure{ux|la}}','Dark overlapping cancel strokes leave bottom serif/descender fragments and an upper right serif, insufficient to choose confidently between the existing alternatives. No restoration is made from the grammar of the following noun.','auxla;auxold','omission','low')
ch('typed la and its insertion leader',r'\inserted{la}',r'inline la; note calls it handwritten',la,'The raised l and a have machine serifs and regular typewriter impressions. A handwritten curved line begins beside the addition, passes under the cancelled cells and rises on the right. Both the level and the line are reproduced.','auxla;auxold','insertion or placement',against_C=True)
ch('cancelled last letter of considérations',r'\deleted{s}','omitted',r'\deleted{\unsure{s}}','The last cell is covered by crossed machine strokes and the hand leader. A low right curve is compatible with s, but the complete letter is not separately readable, so this single character is qualified instead of inferred from the plural.','consids;considscell','deletion state','low',True)
ch('typed systématique and its leader',r'\inserted{systématique}',r'inline systématique; note calls it handwritten',system,'The added word is typed, with visible acute on é, on a raised line above the end of considération and des poids des. Its hand leader rises from below the cancelled final cell, runs under the added word and curls upward at the right.','systematique;systemplace','insertion or placement',against_C=True)
ch('analogues over du même principe',r'\deleted{du même principe}\inserted{\handwritten{analogues}}',r'analogues \struck{même principe}',analog,'The handwritten ana is on top of typed du at the original line end; logues is raised above cancelled même principe on the next line. The normal source line-break hyphen is joined, while these two relative overlay levels are retained. H drops du. The apparent dot after logues belongs to the typed i beneath it, so no new stop is added.','duana;memeprincipe;logues;analogplace','insertion or placement',against_C=True)
ch('séminaire orale correction',r'oral\deleted{e}','oral',r'oral\deleted{e}','A separate typed final e remains at the right of oral with a diagonal cancellation through it. It is not an accent or a live terminal e.','orale','deletion state')
ch('développé and connecting stroke',r'était\inserted{\handwritten{développé}} également','était développé également',develop,'Handwritten développé is above également, beginning slightly before it. Both acute accents are visible. A leader starts after était below the baseline, curves upward beneath the addition and curls at its right end.','developpe;developpeplace','insertion or placement',against_C=True)
ch('altered cell in exemp...e',r'\unsure{exempbe|exemple}','exemple',exemple,'Between p and e there is a tall left-serifed stem with a broad foot, plus a rounded impression extending left of the stem and two partly fused right curves. The neighboring plain l supplies a direct shape control. A qualified o/l or b/l overprint represents the extra ink; neither a clean b nor a clean l alone accounts for it.','exemple;examplecell;examplelcontrol','misread word','medium',True)
ch('replacement above limitée',r'\deleted{limitée}\inserted{\handwritten{sujette à caution}}',r'\struck{limitée} sujette à caution',sujette,'Cancelled limitée is fully readable on the baseline. The hand addition starts above and slightly before it; a leader begins after the old word, curves upward under the addition, and turns up at the right. The placement and leader are reproduced.','limitee;sujette;sujetteplace','insertion or placement',against_C=True)
ch('last word in the handwritten replacement','caution','caution',r'caut\unsure{in|ion}','After c-a-u and the tall t stroke, there is a dotted i-like stroke followed by a short low n-like ending. A separate closed o cannot be distinguished. The directly visible shorter sequence in is put first, with ion retained as the alternative; no grammatical completion is asserted.','sujette;caution','misread word','medium',True)
ch('four sets of quotation marks',r"``géométrique'' (twice); ``poids''; ``résultats''",'« géométrique » (twice); « poids »; « résultats »',r"``géométrique'' (twice); ``poids''; ``résultats''",'Each opening and closing pair consists of two high downward typewriter strokes. No left- or right-pointing angle shapes occur at these four loci.','quotegeo;quotesgeo2;quotespoids;quotesresults','misread symbol or index')
for place,C,shows,crop in [
 ('title and byline','Filtration et poids des espaces de cohomologie des variétés algébriques; par A.GROTHENDIECK','All letters, accents and the period after A are visible. H’s subsection and byline note occur before its page marker and were checked there, so neither is incorrectly counted as omitted.','title1;title2;byline'),
 ('singular verb','définissait','The line-end définis- continues with sait, including only a single t ending. The singular form is retained despite the plural noun earlier.','definiss;sait'),
 ('group and geometric base fields',r'X; k; \bar{k}; \pi=\operatorname{Gal}(\bar{k}/k); X_{\bar{k}}','The k bars are separate horizontal strokes, the quotient slash is diagonal, and the added pi has one horizontal top spanning its two descending strokes. No prime or extra group subscript is supplied.','Xdef;kdef;kbarfirst;pi;Galformula;Xbar'),
 ('three body ell signs and coefficient ell',r'\handwritten{\ell}','Each is a typed l-like serif/stem/foot with a diagonal handwritten modification. Their case and levels match C; the coefficient ell is lowered under the Z.','ell1;ell2;ell3;Hformula'),
 ('empty Tate and Weil references',r'[\quad]; [\quad,\quad]','The Tate brackets contain blank space; the Weil pair contains one separate comma with a descending tail and otherwise blank space. No bibliographical content is supplied.','Tatebrackets;Weilbrackets'),
 ('reference and date',r'SGA 7\handwritten{(}I et II\handwritten{)}; 1964;','One I and two I stems occur within the hand parentheses; the semicolon has separate dot and tail. The date has all four typed digits and a following semicolon.','SGA7;date1964'),
 ('page ending','en caractéristique','The last visible word is caractère-form stem followed by istique, with acute on é and no further continuation on this page. The text ends there.','final')]:ch(place,C,C,C,shows,crop,against_H=False)
for line,reading,alts,conf,comment in [
 ('first raised reference',r'([\quad]',r'[\quad]) or an enclosure stroke rather than a parenthesis','low','Right curved/vertical stroke merges with the outer outline; C doubt retained.'),
 ('first insertion, modified ell cell',r'\rlap{o}\ell',r'\rlap{b}\ell','medium','Additional rounded impression is real; its separation into original characters remains uncertain.'),
 ('first insertion, terminal e','e','edge-obscured final handwritten cell','medium','Ink meets the dark right edge; only the e-like remainder is visible.'),
 ('after que','x',', beneath x','low','Crossing strokes are visible; no underlying comma can be separated.'),
 ('cancelled notation before pi',r'\operatorname{Gal}k',r'G_k; G(k)','low','Repeated diagonal cancellation prevents choosing the typed notation.'),
 ('adverb, old second letter','o','e','medium','Handwritten e covers the old round impression; its middle is obscured.'),
 ('cancelled letters after liés à','ux','la','low','Only fused serif/descender fragments survive the overstrike.'),
 ('cancelled noun ending','s','no secure alternative','low','Remaining low curve is compatible with s but too little is separable for certainty.'),
 ('exemp...e overprint',r'\rlap{o}l',r'\rlap{b}l','medium','Tall serifed stem and extra round impression survive; clean b or l alone is insufficient.'),
 ('last handwritten word','cautin','caution','medium','No separate o loop can be distinguished between the dotted stroke and terminal low n-like curve.')]:r.doubt(line,reading,alts,conf,comment)
r.notation('typewriter l modified to ell',r'\handwritten{\ell}','12:097 three body loci and Z coefficient: typewriter l with added hand diagonal; first raised insertion has a further qualified round overprint.')
r.notation('underlined coefficient alphabet',r'\underline{Z}_{\ell}','12:097 cohomology group: separate underline beneath Z, not blackboard-bold doubling.')
r.notation('underlined raised o in numéro',r'N\textsuperscript{\uline{o}}1; n\textsuperscript{\uline{o}}2','12:097 both number signs have a separate short underline.')
r.notation('overprinted adverb and example',r'n\rlap{e}\deleted{\unsure{o|e}}t; ablem/tem; exemp\unsure{\rlap{o}l|\rlap{b}l}e','12:097 overprints represented without assuming typing chronology; ablem old letters resolved, other round impressions remain qualified.')
r.notation('typewriter double quotes',r"``géométrique''; ``poids''; ``résultats''",'12:097 two high strokes at each end; no guillemets.')
for a,e in [('i.e.','id est'),('Nº; nº','numéro'),('SGA','Séminaire de géométrie algébrique')]:r.r.setdefault('abbreviations',[]).append(dict(abbreviation=a,expansion=e,attestations='12:097'))
r.r['inventory_overrides']={'097-08':dict(first_words_or_objects='x, with possible underlying comma qualified'),'097-17':dict(first_words_or_objects='ablem beneath overlapping handwritten tem'),'097-20':dict(position='e overlapping first cell of cancelled leur'),'097-29':dict(first_words_or_objects='qualified s beneath overstrike and leader'),'097-33':dict(position='ana over du at line end; logues raised above même principe at next line'),'097-39':dict(first_words_or_objects='sujette à cautin/caution, ending qualified')}
extras=[('enclosing outline and two descending leaders around first raised insertion','drawing','above longtemps, stepping up around reference','his hand'),('connecting curve for raised la','drawing','after liés à','his hand'),('connecting curve for raised systématique','drawing','above considération and des poids des','his hand'),('connecting curve for développé','drawing','after était and above également','his hand'),('connecting curve for sujette à cautin/caution','drawing','above and after limitée','his hand'),('extra rounded impression in first raised ell cell','text','first raised insertion','typewriter'),('altered cell between p and e of exemp...e','text','near nº2','typewriter'),('handwritten retracing of ue at right edge','insertion','end of first raised insertion','his hand'),('archive folio 96 retained as comment','margin note','bottom left','another unnamed hand')]
for i,(s,k,p,h) in enumerate(extras,1):r.r['inventory_extra'].append(dict(scan='12:097',sheet_kind='text',hand=h,element=f'097-R{i:03d}',kind=k,position=p,first_words_or_objects=s,transcribed='yes'))
r.r['crops']=json.loads(Path('work/crops12_097.json').read_text())
r.r['inspection_note']='Root alone viewed the whole scan and both actual supplied halves before reading C/H; full C/H, the pre-page H subsection/byline, all eight C macro loci/seven doubt-table rows, the three slips, abbreviations and all39 inventory elements were read. All73 crop recipes were viewed; the initial combined call for quotesresults/final/archive was truncated and counted as unviewed, then each was viewed separately. The 15 adaptive crops localized overprints, cancellation remnants, number signs and ending letters. Both actual halves were then reread line by line. Slanted hand insertions cohomologie/logues/développé/sujette were rotated, with a second smaller cohomologie rotation for an upright reading. Every deletion/addition and mathematics-critical letter/index was inspected. No source is consulted to repair grammar or fill reference slots. Archive96 remains a comment. Context is sealed; this is first-pass collation, not the ordered audit or a mathematical check.'
r.save('work/record12_097.json')
