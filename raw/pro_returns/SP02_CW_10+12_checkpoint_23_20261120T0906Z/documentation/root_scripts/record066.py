import sys,json
from pathlib import Path
sys.path.insert(0,'SP02_CW_10+12/scripts')
from root_record import Record
r=Record('B10-04',10,66);ch=r.change
r.edit(r'qui définit $\handwritten{\mathcal{M}}$',r'qui définit $\handwritten{\unsure{\deleted{\mathcal{A}}\mathcal{M}|\deleted{\mathcal{M}}\mathcal{A}|\mathcal{M}}}$')
inter=r'\deleted{\inserted{(qui implique déjà la donnée}}'
r.edit(inter,'')
r.edit(r'en plus \unsure{du|de|da} groupe',r'en plus \unsure{du|de|da}\\ \hspace*{3cm}'+inter+r'\\ groupe')
r.edit(r'u_{\handwritten{\unsure{*|\sigma}}}',r'u_{\unsure{\deleted{\illegible{1}}\handwritten{*}|\handwritten{\sigma}}}')
r.edit(r'\unsure{\deleted{d}n|\deleted{n}d|n|d}',r'\unsure{\deleted{d}n|\deleted{n}d}')
r.edit(r'\handwritten{\unsure{\sigma|\xi}}',r'\handwritten{\deleted{\unsure{\xi}}\sigma}')
r.edit(r'\operatorname{card}(\handwritten{\sigma})\operatorname{ord}',r'\operatorname{card}(\handwritten{\sigma})\operatorname{\unsure{\deleted{d}o|\deleted{o}d}rd}')
rel=r'\mathrel{\begin{tikzpicture}[x=1cm,y=1cm,baseline=-.05cm]\draw[thin] (0,0)--(.5,0)--(.47,.12);\end{tikzpicture}}'
r.edit(r'\mathrel{-\! -}',rel)
r.edit(r'\unsure{\times|x|\mathbb{x}}',r'\unsure{\times|x|\mathbb{x}|*}')
r.edit(r'\unsure{On va exes|On va ex}',r'On va e\unsure{t|x|i}e\unsure{s}')
r.edit('(pro-dénombrable ?) On va','(pro-dénombrable ?). On va')
r.edit(r'H^{\handwritten{2}}(k,\underline{Z}',r'H^{\handwritten{2}}(\unsure{\deleted{i}k|\deleted{k}i},\underline{Z}')
r.edit(r'Gardons \deleted{le}',r"Gardons \deleted{l\unsure{'|i|t}e}")
old=r'''\diagram{\begin{tikzcd}[ampersand replacement=\&]
0 \handwritten{\arrow[r]} \& G \handwritten{\arrow[r,dash]} \arrow[r,phantom,"u"] \& \underline{Z}^{\times} \handwritten{\arrow[r]} \arrow[r,phantom,"N_{Z/k}"] \& \underline{G}_m \handwritten{\arrow[r]} \& 0\ ,
\end{tikzcd}}'''
new=r'''\diagram{\begin{tikzpicture}[x=1cm,y=1cm]
\node at (0,0) {$0$};\node at (1.7,0) {$G$};\node at (3.3,0) {$\underline{Z}^{\times}$};\node at (6.2,0) {$\underline{G}_m$};\node at (8.2,0) {$0$};\node at (9,0) {$,$};
\draw[thin] (.4,0)--(1.25,.03);\fill (1.12,-.025)--(1.25,.03)--(1.13,.105)--cycle;
\draw[thin] (2.05,0)--(2.75,0)--(2.74,.05);\node at (2.4,.4) {$u$};
\draw[thin] (3.8,-.05)--(5.5,0)--(5.48,.04);\node at (4.6,.46) {$\unsure{\mathbb{N}|N}_{Z/k}$};
\draw[thin] (6.75,0)--(7.75,.03)--(7.71,.13);
\draw[thin,gray] (7.3,-.03)--(7.45,-.45);\draw[thin,gray] (7.4,-.03)--(7.57,-.5);\draw[thin,gray] (7.52,-.03)--(7.74,-.64);
\end{tikzpicture}}'''
r.edit(old,new)
cancel=r'''\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw[thin] (.95,2.4).. controls (.7,1.5) and (.35,.5)..(.3,.12);
\draw[thin] (.38,2.18).. controls (.8,1.2) and (1.7,.4)..(2.52,0);
\draw[thin] (2.79,2.27).. controls (2.4,1.4) and (2.1,.4)..(2.2,-.08);
\draw[thin] (3.34,2.17).. controls (4.2,1.8) and (4.7,.6)..(5.5,.1);
\draw[thin] (4.83,2.17).. controls (4.7,1.5) and (4.25,.3)..(4.2,-.1);
\draw[thin] (6.62,2.19).. controls (7.2,1.35) and (8.1,.6)..(8.72,.16);
\draw[thin] (7.58,2.34).. controls (7.35,1.4) and (6.8,.4)..(6.85,-.1);
\draw[thin] (9.76,2.17).. controls (9.45,1.45) and (9.1,.4)..(9.05,-.1);
\draw[thin] (9.57,1.91).. controls (9.8,1.05) and (10.55,.6)..(11.32,-.06);
\draw[thin] (10.87,2.19).. controls (10.8,1.5) and (10.3,.4)..(10.25,-.1);
\end{tikzpicture}}'''
r.edit(r'\deleted{et le résultat précédent montre que l\x27ensemble des classes de}'.replace(r'\x27',"'"),r"\deleted{et le résultat précédent montre que l'ensemble des classes de}"+'\n'+cancel)
ch('first category glyph','M','M',r'\unsure{\deleted{A}M|\deleted{M}A|M}','The category symbol has pale earlier uprights and a dark rounded inner loop as well as the M-like outer strokes. A/M replacement order versus a heavily retraced M remains unresolved.','M','misread symbol or index','low',True,True,False,True)
ch('cancelled interline wording','(qui implique déjà la donnée',r'\ill{}','(qui implique déjà la donnée','The opening parenthesis, qui, implique, both accents in déjà and donnée, and all intervening letter cells survive under the x cancellation.','interline','readable ink left as \\ill{}','high',False,True,True)
ch('cancelled interline placement','attached after category M','after en plus du','separate physical interline below en plus du; intended anchor unresolved','The crossed line lies between the line ending en plus du and groupe de t.m.; no leader identifies a logical insertion anchor. It is now placed as a separate interline.','top; interline','insertion or placement','high',True,False)
ch('en plus final vowel',r'\unsure{du|de|da}','du',r'\unsure{du|de|da}','The final cell is densely overprinted and combines rounded and upright traces; no single du/de/da reading is secure.','du','misread word','medium')
ch('first u subscript',r'\unsure{*|\sigma}','sigma',r'\unsure{\deleted{\illegible{1}}*|\sigma}','The enlarged cell has a dark upper pen mark over a lower serifed, hollow-looking cell. An overwritten unreadable typed sign beneath a star is possible; an overworked sigma remains an alternative.','ustar1','misread symbol or index','low',True,True,False,True)
ch('rank initial overtyping',r'\unsure{\deleted{d}n|\deleted{n}d|n|d}','n',r'\unsure{\deleted{d}n|\deleted{n}d}','Both a d ascender and n arch remain in the same typed cell. The plain unaltered-letter alternatives do not account for all strokes.','ncell','misread symbol or index','low',True,True,False,True)
ch('rank argument overtyping',r'\unsure{\sigma|\xi}','sigma',r'\deleted{\unsure{\xi}}\sigma','A dark closed sigma loop and horizontal tail lie above a pale long descending zigzag, compatible with an earlier xi. The final sigma is clearer than the earlier layer.','rankarg','misread symbol or index','medium',True,True,False,True)
ch('ord initial overtyping','ord','ord',r'\unsure{\deleted{d}o|\deleted{o}d}rd','The initial cell has a closed o outline and a distinct d ascender with left top serif. Their order is unresolved.','ord','misread word','low',True,True,False,True)
ch('rank-formula multiplication stop','juxtaposition','centered dot','juxtaposition','The space between the closing parenthesis after card and the first ord letter is blank.','rank','text not on the page','high',False,True)
ch('cancelled de before xi','de',r'\ill{}','de','The d ascender and lower bowl, followed by the crossed e cell, remain readable.','de','readable ink left as \\ill{}','high',False,True,True)
ch('crossed sign below G',r'G_{\deleted{\times}}','G only',r'G_{\deleted{\times}}','A serifed cross-shaped typed sign lies directly below the G and overlaps its lower part.','Gsub','omission','high',False,True,False,True)
ch('second u subscript','star','sigma','star, with sigma alternative retained in page notation table','The small handwritten mark has a rising arm, a rightward stroke and a looped lower part; a star versus sigma reading remains uncertain, as for the first occurrence.','u2','misread symbol or index','medium',False,True,False,True)
ch('u-map relation',r'\unsure{\mathrel{-\! -}|\longrightarrow}',r'\to','drawn shaft and short upturned end; arrow alternative','The shaft is continuous and the right end turns upward; a full two-arm arrowhead is not separately visible.','u2arrow','drawing or diagram','medium',True,True,False,True)
ch('three raised unit signs',r'\unsure{\times|x|\mathbb{x}}','asterisks',r'\unsure{\times|x|\mathbb{x}|*} at first occurrence','All three raised signs have crossed, serifed outlines and a central horizontal stroke. Letter, multiplication-cross and asterisk conventions are not separated securely.','x1; x2; x3','misread symbol or index','medium',True,True,False,True)
ch('cancelled On va fragment',r'\unsure{On va exes|On va ex}',r'\ill{}',r'On va e\unsure{t|x|i}e\unsure{s}','On va and the two later e bowls are readable. The intervening crossed cell has a tall upper blob compatible with t or i; x remains possible. The final s-like curve meets the cropped edge.','onva','readable ink left as \\ill{}','low',True,True,True)
ch('stop after pro-dénombrable question','omitted','omitted','full stop','A distinct round dot stands below and just to the right of the closing parenthesis at the page edge.','proend','omission','high',True,True)
ch('example labels emphasis','Exemple underlined; number plain','Exemple 1 and Exemple 2 italic','Exemple underlined; number plain','Both headings have a single horizontal rule only beneath the typed word Exemple; the number sits beyond it.','example1; example2','other','high',False,True)
ch('first example number',r'\unsure{\mathbb{I}|I|1}','1',r'\unsure{\mathbb{I}|I|1}','The label has two upright outlines with top/bottom serifs and a dense rightward middle trace; it cannot be reduced securely to an ordinary numeral 1.','label','misread symbol or index','low')
ch('negative clause','s\x27il n\x27est trivial','s\x27il n\x27est pas trivial','s\x27il n\x27est trivial','The words n’est and trivial are adjacent with one ordinary space; no pas appears.','example1','text not on the page','high',False,True)
ch('first example u relation','dash','arrow','drawn shaft with very short upturned end','The line below u ends in a small rounded rise, with no distinct two-arm arrowhead.','diag1','drawing or diagram','high',True,True,False,True)
ch('norm label capital','N','N',r'\unsure{\mathbb{N}|N}','The norm capital has a dark main impression and a parallel pale right upright/diagonal. A double-struck N versus an offset repeated impression of ordinary N remains unresolved.','normN','misread symbol or index','medium',True,True,False,True)
ch('norm relation','arrow','arrow','drawn long shaft with blunt terminal','The long horizontal pen line below the norm label ends in a small blob rather than a clear arrowhead.','diag1','drawing or diagram','high',True,True,False,True)
ch('last relation in first example','arrow','arrow','drawn shaft with upward terminal','The last horizontal stroke has a short thick upturned right end; its outline is reproduced directly.','diag1','drawing or diagram','high',True,True)
ch('pale strokes beneath last relation','omitted','omitted','three descending gray strokes in TikZ','Three pale oblique traces descend from below the last horizontal line, separate from the typed zero.','diag1','drawing or diagram','high',True,True)
ch('kernel second coefficient field','k','k',r'\unsure{\deleted{i}k|\deleted{k}i}','The k-like ascender and arms coexist with an i-like short upright and upper dot. The two typed impressions cannot be ordered.','ker-k','misread symbol or index','medium',True,True,False,True)
ch('kernel expression placement','inline','display','inline','The kernel expression shares its typed line with est nul and the next sentence.','example1','insertion or placement','high',False,True)
ch('cancelled word after Gardons','le',r'\ill{}',r"l\unsure{'|i|t}e",'The l and e are visible with an additional raised dark mark in an intervening crossed cell. Apostrophe, i and t remain possible for this mark.','le','readable ink left as \\ill{}','low',True,True,True)
ch('blank before 2','blank','geq','blank','The area between entier and 2 has no inequality; the oblique stroke near 2 is one of the long cancellation lines.','blank','text not on the page','high',False,True,False,True)
ch('n-id separator','baseline period','centered multiplication dot','baseline period','The point after n lies at the same baseline as the sentence stops, before the upright id.','example2','misread symbol or index','high',False,True)
ch('cancelled sequence arrows','absent','four rightward arrows','absent','The sequence consists of separated typed 0, G-prime, G, raised n, G and 0; no horizontal connectors are present between them.','example2','text not on the page','high',False,True,False,True)
ch('cancelled sequence state','deleted entries','live mathematical display','deleted entries','The same large oblique cancellation strokes that cross the surrounding prose also cross this sequence.','example2','deletion state (struck given live or live given struck)','high',False,True)
ch('large cancellation strokes','only deletion macros','described in editorial note','ten curved diagonal strokes drawn in TikZ, with deleted text retained','Six tall oblique strokes and four crossing downward curves span the entire bottom example and its final unfinished sentence.','example2; last','drawing or diagram','high',True,True)
ch('editorial continuation and next heading','absent','editorial notes and next-section heading','absent','Below the cancelled final words classes de, the scan ends. The long H note and heading for the following text have no corresponding ink on this page.','example2; last','text not on the page','high',False,True)
for p,rd,alt,co in [('first category glyph','old A then M','old M then A; retraced M','low'),('en plus vowel','du','de; da','medium'),('cancelled interline anchor','physical interline after en plus du','logical attachment after preceding category M; later attachment in paragraph','low'),('first u subscript','star over unreadable cancelled typed cell','overworked sigma','low'),('rank initial',r'\deleted{d}n',r'\deleted{n}d','low'),('rank argument earlier layer',r'\xi','','medium'),('ord initial',r'\deleted{d}o',r'\deleted{o}d','low'),('second u subscript','*',r'\sigma','medium'),('u-map relation','drawn upturned shaft','arrow','medium'),('raised unit sign',r'\times',r'x; \mathbb{x}; *','medium'),('On va fragment middle','t','x; i','low'),('On va fragment ending','s','','low'),('first example label',r'\mathbb{I}','I; 1','low'),('norm capital',r'\mathbb{N}','N','medium'),('kernel second field',r'\deleted{i}k',r'\deleted{k}i','medium'),('Gardons cancelled middle',"'",'i; t','low')]:r.doubt(p,rd,alt,co)
for id,pos,txt,hand in [('M-layer','first category symbol','A/M replacement or retracing unresolved','his hand'),('u-layer','first u subscript','possible unreadable typed underlayer','typewriter'),('ord-layer','rank formula ord initial','d/o overlapping impressions','typewriter'),('k-layer','kernel second field','i/k overlapping impressions','typewriter')]:
 r.r['inventory_extra'].append(dict(scan='10:066',sheet_kind='typescript',hand=hand,element='066-'+id,kind='deletion',position=pos,first_words_or_objects=txt,transcribed='yes'))
for id,pos,txt in [('pale-lines','below last relation in first sequence','three pale descending strokes'),('cancel-lines','entire Example 2','ten curved oblique cancellation strokes')]:
 r.r['inventory_extra'].append(dict(scan='10:066',sheet_kind='typescript',hand='his hand',element='066-'+id,kind='drawing',position=pos,first_words_or_objects=txt,transcribed='yes'))
r.r['inventory_overrides']={'066-005':{'first_words_or_objects':'A/M overwrite or retracing uncertainty'},'066-007':{'position':'separate crossed interline after line ending en plus du'},'066-008':{'position':'separate crossed interline; intended anchor unresolved'},'066-009':{'first_words_or_objects':'star over unreadable typed cell, or overworked sigma'},'066-014':{'first_words_or_objects':'d/n overtyping; order uncertain'},'066-015':{'first_words_or_objects':'dark sigma over pale xi-like layer'},'066-017':{'first_words_or_objects':'n(sigma)=card(sigma) ord(xi_sigma); ord initial d/o overtype'},'066-034':{'first_words_or_objects':r'On va e\unsure{t|x|i}e\unsure{s}'},'066-038':{'first_words_or_objects':'sequence with drawn shafts/terminals and uncertain double-struck norm N'},'066-040':{'first_words_or_objects':'short shaft with upturned end'},'066-041':{'first_words_or_objects':'long blunt norm shaft'},'066-042':{'first_words_or_objects':'last shaft with upturned end and pale descending traces'},'066-050':{'first_words_or_objects':r"l\unsure{'|i|t}e"}}
r.notation('u-map subscripts','star | sigma; first may cover a cancelled unreadable typed cell','10/066 first paragraph and determination question','unresolved; first occurrence marked and second listed')
r.notation('raised unit signs',r'\times | x | \mathbb{x} | *','10/066 determination map, sequence and kernel','unresolved convention; first occurrence qualified')
r.notation('norm capital',r'\mathbb{N} | N','10/066 first example sequence','double-struck appearance versus offset impression unresolved')
r.r['abbreviations']=[dict(abbreviation='pl',expansion='plat',attestations='10/066 cohomology sites'),dict(abbreviation='t.m.',expansion='type multiplicatif',attestations='10/066 first paragraph'),dict(abbreviation='th.',expansion='théorème',attestations='10/066 th. 90')]
r.r['crops']=json.loads(Path('work/crops066.json').read_text())
r.r['inspection_note']='Whole and both halves read before C/H. All text blocks, math capitals, indices, primes, handwritten Greek forms and relations were enlarged, as were every C doubt, C/H difference, cancelled phrase and newly visible overtype. All three raised unit signs and the norm capital were separately enlarged. No slanted prose occurs; the slanted cancellation strokes are drawn from their visible geometry. The bottom blank and absent sequence arrows are preserved. The cancelled interline is placed physically without asserting its logical anchor. H editorial notes/next heading are excluded. No OCR, later scan or sealed context used.'
r.save('work/record066.json')
