"""First-reader proposal for 148_scan071, from this page's inspected ink only.
The unknown overwritten target and isolated mark are drawn, not identified by context.
No OCR, web, TeX compilation, or other page source is used.
"""
from pathlib import Path
import json,csv,re
B=Path('/workspace/scratch/f28c4f52d3ec');PAGE='148_scan071';P=B/'packets'/PAGE
C=(P/'C.tex').read_text();H=(P/'H.tex').read_text()
boxes=json.loads((B/'proposed'/f'{PAGE}_crop_boxes.json').read_text())

firstbox=r'''\begin{tikzpicture}[baseline=(b.base)]
\node[inner xsep=5pt,inner ysep=4pt] (b) {$S\mathcal T_{\mathrm{top}}$};
\draw (b.north west)--(b.south west)--(b.south east)--(b.north east);
\end{tikzpicture}'''
variantbox=r'''\begin{tikzpicture}[baseline=(b.base)]
\node[inner xsep=5pt,inner ysep=4pt] (b) {$S\mathcal T_{\mathrm{top}}^{\pm}$};
\draw (b.north west)--(b.south west)--(b.south east)--([yshift=-4pt]b.north east);
\draw (b.north west)--([xshift=-6pt]b.north east);
\end{tikzpicture}'''
oldtarget=r'''\unsure{\begin{tikzpicture}[baseline=-.4ex,x=.010cm,y=-.010cm,line cap=round,line join=round]
% Unread cancelled target: visible underlying outlines and cancellation strokes.
\draw[thin] (5,12) .. controls (12,1) and (22,2) .. (26,13)
 .. controls (29,22) and (12,28) .. (3,29);
\draw[thick] (15,5) .. controls (13,24) and (13,35) .. (12,47);
\draw[thin] (14,26) .. controls (34,20) and (42,31) .. (30,40)
 .. controls (23,44) and (16,47) .. (7,47);
\draw[thick] (46,40) .. controls (45,49) and (52,53) .. (50,61)
 .. controls (44,65) and (45,69) .. (52,69)
 .. controls (51,80) and (56,84) .. (61,80);
\draw[thin] (68,65)--(82,53)--(94,57);
\draw[thick] (87,47)--(87,68);
\draw[thin] (75,70)--(96,68);
\draw[thick] (108,45) .. controls (111,31) and (129,29) .. (128,40)
 .. controls (127,50) and (115,55) .. (112,55);
\draw[thick] (117,38) .. controls (115,51) and (116,63) .. (111,72)
 .. controls (109,77) and (104,80) .. (101,80);
\draw[thin] (116,54) .. controls (130,51) and (136,59) .. (126,69)
 .. controls (124,76) and (117,81) .. (109,84);
\draw[thick] (3,45)--(42,27);
\draw[thick] (6,51)--(54,32);
\draw[thick] (12,56)--(69,34);
\draw[thick] (25,59)--(82,41);
\draw[thick] (39,65)--(98,44);
\end{tikzpicture}}'''
mark=r'''\unsure{\begin{tikzpicture}[baseline=-.4ex,x=.015cm,y=-.015cm,line cap=round,line join=round]
\draw[line width=1pt] (16,0)--(10,7)--(5,12)--(0,19)
 .. controls (0,25) and (9,31) .. (14,28)
 .. controls (20,25) and (15,15) .. (12,10);
\draw[thick] (7,14) .. controls (2,17) and (3,25) .. (9,27)
 .. controls (15,29) and (19,21) .. (13,20)--(6,15);
\draw[thick] (14,20)--(27,17);
\draw[thin] (5,12)--(12,23);
\fill (30,7)--(31,10)--(36,13)--(33,12)--(29,11)--cycle;
\end{tikzpicture}}'''
heading=r'Groupoïdes de \uline{Teichmüller}'
first_heading='1) Groupoïde topologique. '+firstbox+'.\n(\\uline{groupoïde de Teichmüller spécial orienté topologique})'
objects=r'''Objets : paires $(X,S)$
\[
\left|\begin{array}{l}
X\ \text{surface à bord compacte \uline{orientée}}\\
S\subset\partial X\quad\text{partie finie du bord}
\end{array}\right.
\]'''
morphism1=r"Morphismes $(X,S)\longrightarrow(X',S')$ : classes d'isotopie d'isomorphismes"
case1=r'''$1^\circ)$ $S=\phi$ on écrit $\mathcal T_{\mathrm{top}}$ sous-groupoïde ouvert.
(\uline{groupoïde de T. \deleted{\unsure{orient}} orienté topologique})'''
variants=r'\deleted{Vari} \uline{Variantes}'+'\n'+r'$\unsure{2^\circ|1^\circ})$ '+variantbox+r''' mêmes objets, mais plus de flèches :
classes d'isotopie d'homéom. $(X,S)\xrightarrow{\sim}(X',S')$, ne respectant pas l'orientation nécessairement.'''
functor=r'''\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=large]
S\mathcal T_{\mathrm{top}}^\pm \arrow[r,"\unsure{\chi|\varepsilon}","\text{(signature}"']
\& \text{'''+oldtarget+r'''}\ \substack{\text{groupoïde \deleted{ponctuel}}\\
\text{défini par le groupe}\\
\pm1,\ \text{noté }[\pm1]}
\end{tikzcd}}'''
fibre=r'le \deleted{noyau} \deleted{est} (\unsure{la|$=$} catégorie fibre) est $S\mathcal T_{\mathrm{top}}$'
mark_block='\\figure{\\hspace*{4cm}'+mark+'}'
triple=r'''$2^\circ)$ $(X,\Sigma,S)$, avec
\[
\left|\begin{array}{l}
X\ \text{compacte à bord orienté}\\
\Sigma\ \text{sous-variété \deleted{\unsure{fermée}} \inserted{compacte} de dim $1$}\\
\qquad\text{de }X\setminus\partial X\\
S\subset\Sigma\cup\partial X\quad\text{partie finie}
\end{array}\right.
\]'''
morphism2=r"morphismes : classes d'isotopie d'homéom \unsure{respectant} l'orientation."
notation=r'Notation $\mathcal T\deleted{\unsure{S}}\inserted{D}_{\mathrm{top}}$'
initial=r'($D$) initiale de.'
replacement=r'\deleted{``\unsure{sauvage}\'\'}\inserted{dévissage}) :'
# Apostrophes below are literal quotation marks, never TeX accent commands.
replacement="\\deleted{``\\unsure{sauvage}''}\\inserted{dévissage}) :"
definition="``\\uline{groupoïde de Teichmüller orienté dévissé topologique}''."
nb=r'''\uline{NB}
\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=small,row sep=.15em]
S\mathcal T_{\mathrm{top}} \& \subset \& S\mathcal T D_{\mathrm{top}}
\& \substack{\inserted{\text{imm. ouverte}}\\(\deleted{\text{immersion pleine}})}\\
\Vert\\
\text{\makebox[0pt][l]{sous groupoïde des objets tels que $\Sigma=\phi$}}
\end{tikzcd}}'''
third=r'''$3^\circ)$ On définit de $=$ $\mathcal TS_{\mathrm{top}}^\pm$
(\uline{groupoïde de Teichmüller biorienté dévissé topologique})'''
folio=r'\mspage{70}'
lower='\n\n'.join([mark_block,triple,morphism2,notation,initial,replacement,definition,nb,third])
tex='\\scanpage{71}\n'+ '\n\n'.join([heading,first_heading,objects,morphism1,case1,variants,'On a\n'+functor,fibre,lower,folio])+'\n'
(B/'proposed'/f'{PAGE}.tex').write_text(tex)

changes=[]
def add(place,c,h,final,dc,dh,kind,cat,evidence,crop,confidence='high',consequential=False):
 changes.append({'id':f'{PAGE}-{len(changes)+1:02d}','place':place,'c':c,'h':h,'final':final,'diff_c':dc,'diff_h':dh,'kind':kind,'error_kind':cat,'evidence':evidence,'crop':f'crops/{PAGE}_{crop}.png','box':boxes[crop],'confidence':confidence,'marked_in_h':False,'consequential':consequential})
add('page heading',heading,'absent',heading,False,True,'omission','Omissions','The full Groupoïdes de Teichmüller heading is written above item1; the underline marks the name, running under its right-hand portion.','heading')
add('item1 heading: noun and adjective','Groupoïdes topologiques','Groupoïde topologique','Groupoïde topologique',True,False,'misread word','Words','Neither Groupoïde nor topologique has an independent final s after its terminal e. The singular forms follow the actual exits.','first_heading')
add('point before first enclosure','absent','absent','.',True,True,'omission','Omissions','A small detached dark point follows topologique before the enclosure; it is separate from the terminal word stroke. The larger point after the enclosure is independently present.','first_heading')
add('first category enclosure',r'$\boxed{S\mathcal T_{\mathrm{top}}}$',r'$S\mathcal T_{\mathrm{top}}$\note{encadré}',firstbox,True,False,'drawing or diagram','Drawings and diagrams','Only the left, bottom and right sides are drawn; the top is open. The source formula has no exponent in this occurrence.','first_heading')
add('point after first enclosure','.',r'\note{encadré}', '.',False,True,'omission','Omissions','A distinct dark point lies to the right of the enclosure, separate from the right border.','first_heading')
add('first morphism sentence ending',"d'isomorphismes","d'isomorphismes.","d'isomorphismes",False,True,'text not on the page','Text that is not on the page','The final letter stroke approaches the sheet edge; there is no separate punctuation point after it.','isomorphismes_end')
add('position and order of S-empty subcase and its parenthesis',r'\deleted{\unsure{Vari|Trois}} \uline{Variantes} ... $1^\circ)$ $S=\varnothing$ on écrit $\mathcal T_{\mathrm{top}}$ sous-groupoïde ouvert. (\uline{groupoïde de T. \deleted{\unsure{orient}} orienté topologique})',r'$1^\circ)$ $S=\emptyset$ on écrit $\mathcal T_{\mathrm{top}}$ (groupoïde de T. orienté topologique) sous-groupoïde ouvert.\ \struck{Vari} Variantes',case1,True,True,'insertion or placement','Insertions put in the wrong place','The S-empty clause occupies the line above Variantes. Its sous-groupoïde ouvert continuation stays on that same line; the parenthetic name is below it to the right. The final transcript preserves that physical reading order.','first_case')
add('first empty-set sign',r'$S=\varnothing$',r'$S=\emptyset$',r'$S=\phi$',True,True,'misread symbol or index','Symbols and indices','The oval has a long oblique descending crossing stem, the written phi form used for the empty set.','first_case')
add('old word before orienté',r'\deleted{\unsure{orient}}',r'\struck{\ill{}}',r'\deleted{\unsure{orient}}',False,True,'other','Struck text','The strike leaves an orient-like short run and final tall stroke, but not every middle letter is separable; orient remains a candidate, not a resolved reading.','first_case','low')
add('variant enclosure',r'$\boxed{S\mathcal T_{\mathrm{top}}^\pm}$',r'$S\mathcal T^{\pm}_{\mathrm{top}}$\note{encadré}',variantbox,True,False,'drawing or diagram','Drawings and diagrams','The top border is present, but its right end does not join the upper end of the right border. The two bars and upright of the plus/minus exponent are clear.','variants')
add('caption word below sign arrow','signature','orientation','signature',False,True,'misread word','Words','The caption begins s-i-g with the g descender, then n-a-t-u-r-e; it does not begin o-r-i-e-n.','signature_functor')
add('caption closing parenthesis',r'(signature)',r'(orientation)',r'(signature',True,True,'text not on the page','Text that is not on the page','The opening curved parenthesis is present. No separate closing parenthesis follows the final e. The caption-word correction is logged separately.','signature_functor')
add('unread cancelled target immediately after arrow',r'\deleted{\unsure{\mathfrak G}}',r'[\pm1]\note{le but est écrit sur une rature}',oldtarget,True,True,'drawing or diagram','Drawings and diagrams','The cancelled unit has a B/G-like first outline plus further lower looped strokes and several diagonal cancellation strokes. A single G does not cover all this ink; no mathematical identity is securely recoverable. A small doubtful TikZ transcription preserves the visible forms instead of supplying the expected target.','signature_functor','low',True)
add('cancelled word after groupoïde',r'\deleted{ponctuel}',r'\struck{\ill{}}',r'\deleted{ponctuel}',False,True,r'readable ink left as \ill{}','Readable ink left as illegible','The p descender, o/n/c run, crossed tall t, then u-e-l remain distinguishable around the horizontal cancellation.','signature_functor')
add('punctuation after displayed target',r'[\pm1]',r'[\pm1] ;',r'[\pm1]',False,True,'text not on the page','Text that is not on the page','The final closing square bracket is followed by blank paper, with no semicolon before the next line.','signature_functor')
add('cancelled est after cancelled noyau',r'\deleted{est}','absent',r'\deleted{est}',False,True,'omission','Struck text','A separate crossed e-s-t run follows noyau; the t upright and bar are visible. It is not part of the following parenthesis.','fibre')
add('fibre sentence terminal punctuation',r'$S\mathcal T_{\mathrm{top}}$',r'$S\mathcal T_{\mathrm{top}}$.',r'$S\mathcal T_{\mathrm{top}}$',False,True,'text not on the page','Text that is not on the page','The final top subscript ends in the p descender; no separate period follows the formula.','fibre')
add('isolated dark mark above item2 definition','absent','absent',mark_block,True,True,'omission','Omissions','A crossed looped dark cluster and a detached small right-hand mark are visible. The cluster is 6-like but not securely a numeral. Both pieces are drawn with an in-place doubt and without assigning a numeric identity.','isolated_mark','low')
add('X condition in item2','orienté','orientée','orienté',False,True,'misread word','Words','The final pale e follows the tall t and carries the accent stroke; there is no additional second e.','triple_definition')
add('second homéom abbreviation ending','homéom','homéom.','homéom',False,True,'text not on the page','Text that is not on the page','The m ends in a descending exit, followed by a gap before respectant. There is no independent point in that gap.','homeom_tail')
add('old letter beneath notation D',r'\mathcal T\deleted{\unsure{S}}\inserted{D}_{\mathrm{top}}',r'\mathcal T D_{\mathrm{top}}',r'\mathcal T\deleted{\unsure{S}}\inserted{D}_{\mathrm{top}}',False,True,'omission','Struck text','The clear live D overlays a lower cancelled S-like bowl/run; the old letter remains doubtful. The live D is separately confirmed by its upright and large right-hand curve.','notation_old_d','medium',True)
add('parentheses and point at initiale de',r'($D$ initiale de',r'(($D$) initiale de',initial,True,True,'other','Other','The source shows (D), then initiale de, then a detached point. No additional outer opening parenthesis is securely present. The later closing parenthesis after the cancelled quoted word is retained without balancing it editorially.','notation_old_d')
add('replacement noun','dévissage','divisage','dévissage',False,True,'misread word','Words','The first vowel has an accent stroke; the middle has two successive s forms before a-g-e. The double-s pattern agrees with the separately visible dévissé forms on this page.','definition_words')
add('raised replacement state','dévissage','divisage',r'\inserted{dévissage}',True,True,'insertion or placement','Insertions put in the wrong place','dévissage is written above the cancelled quoted sauvage, in the same replacement position, alongside the S-to-D notation revision. Its insertion state is retained.','definition_words')
add('quoted cancelled candidate',r"\deleted{``\unsure{sauvage}''}",r'\struck{« \ill{} »}',r"\deleted{``\unsure{sauvage}''}",False,True,'other','Struck text','Paired short quotation marks flank a cancelled sauvage-like run. The s/a opening and descending g are visible, but the strike hides some internal letters, so the candidate remains unsure. The marks are paired quotes, not guillemets.','definition_words','low')
add('quoted groupoid name: dévissé','dévissé','divisé','dévissé',False,True,'misread word','Words','The first é has an accent; two distinct short s runs stand between i and the accented final é.','definition_words')
add('live definition quotation marks',definition,'« groupoïde de Teichmüller orienté divisé topologique ». ',definition,False,True,'other','Other','The source opens and closes with paired short raised quote strokes, not drawn guillemets; the final point is present after the closing pair. The dévissé spelling is logged separately.','definition_words')
add('NB replacement and parenthesis scope',r'\substack{\text{imm. ouverte}\\(\deleted{\text{immersion pleine}})}',r'(\add{imm. ouverte} \struck{\ill{} pleine})',r'\substack{\inserted{\text{imm. ouverte}}\\(\deleted{\text{immersion pleine}})}',True,True,'insertion or placement','Insertions put in the wrong place','imm. ouverte is raised above the cancelled immersion pleine. The visible parentheses enclose the lower cancelled phrase, not the live replacement.','nb')
add('NB cancelled first word','immersion',r'\ill{}','immersion',False,True,r'readable ink left as \ill{}','Readable ink left as illegible','The initial i and successive m humps, followed by e-r-s-i-o-n, remain recoverable around the thin strike; the following pleine is also legible.','nb')
add('NB vertical equality',r'\Vert',r'= ',r'\Vert',False,True,'misread symbol or index','Symbols and indices','Two short upright parallel strokes stand below the first S T-top and above its object description. They are a vertical equality, not a baseline equals sign.','nb')
add('NB sous groupoïde spacing','sous groupoïde','sous-groupoïde','sous groupoïde',False,True,'text not on the page','Text that is not on the page','There is a clear gap after sous and no independent hyphen before groupoïde.','nb')
add('NB empty-set condition',r'\Sigma=\varnothing',r'\Sigma=\emptyset',r'\Sigma=\phi',True,True,'misread symbol or index','Symbols and indices','The oval and long descending crossing stroke repeat the visible phi-form empty-set sign of the first subcase.','nb')
add('NB condition terminal point',r'\Sigma=\varnothing',r'\Sigma=\emptyset.',r'\Sigma=\phi',False,True,'text not on the page','Text that is not on the page','No independent punctuation point follows the final empty-set sign; the glyph-form correction is logged separately.','nb')
add('item3 shorthand',r'de $=$','de même',r'de $=$',False,True,'abbreviation expanded or spelling modernised','Abbreviations expanded, spelling modernised','Two horizontal bars are written after de. The sign is retained as the shorthand for même, rather than expanded.','third')
add('item3 groupoid adjective','dévissé','divisé','dévissé',False,True,'misread word','Words','The accented first vowel and two successive s strokes are visible in the final parenthetic groupoid name.','third')
cfigure=C[C.index(r'\figure{'):C.index(r'\mspage{70}')].strip()
add('pale underlying contours and circles',cfigure,'editorial note identifies the pale drawing as show-through','',True,False,'text not on the page','Text that is not on the page','The contours and circles are uniformly pale, soft and beneath the crisp dark text, with associated brown bleed-like dots; they carry no independent dark graph or labels on this face. They are treated as show-through background, not a new recto drawing. No exact match to another leaf or verso was checked or claimed.','background_drawing','medium')
add('lower folio',folio,'absent',folio,False,True,'omission','Omissions','The first digit has the long top stroke, descending stem and crossbar of 7; the second is a closed oval 0.','folio')

marks=list(csv.DictReader((P/'MARKS.tsv').open(),delimiter='\t'))
decisions=[
 {'id':'M0948','decision':'undecided','reading':r'\unsure{2^\circ|1^\circ}','evidence':'The numeral has a curved/diagonal-looking upper and lower run, but a heavily retraced upright prevents secure separation of 2 from 1. The small degree circle is clear. The whole adjacent category formula was checked, including plus/minus and its open enclosure join.','crop':f'crops/{PAGE}_variants.png','box':boxes['variants'],'confidence':'low'},
 {'id':'M0949','decision':'undecided','reading':r'\unsure{\chi|\varepsilon}','evidence':'Crossing upper strokes, a heavy curved descending return and an extra left loop are superposed. They do not securely settle chi versus epsilon or the order of underlying layers. The complete source/arrow/cancelled target and live group description were inspected.','crop':f'crops/{PAGE}_signature_functor.png','box':boxes['signature_functor'],'confidence':'low'}]
assert {m['id'] for m in marks}=={m['id'] for m in decisions}
implicit=[]
def imp(place,dec,reading,ev,crop,confidence):
 implicit.append({'id':f'I{len(implicit)+1:02d}','place':place,'decision':dec,'reading':reading,'evidence':ev,'crop':f'crops/{PAGE}_{crop}.png','box':boxes[crop],'confidence':confidence})
imp('cancelled heading fragment','first',r'\deleted{Vari}','The crossed initial has the two arms of V, followed by a, a low r and a dotted i; the word is Vari, not Trois.','variants','high')
imp('old orient candidate','undecided',r'\deleted{\unsure{orient}}','The cancellation covers some middle letters; the orient-like candidate is retained without claiming full recovery.','first_case','low')
imp('ouvert','first','ouvert','The final t and terminal exit have no added e; the whole word ouvert and following point are readable.','first_case','high')
imp('cancelled target','undecided',oldtarget,'The full crossed unit is drawn because its extended lower looped strokes prevent a secure symbolic identity.','signature_functor','low')
imp('fibre parenthetical opening','undecided',r'(\unsure{la|$=$} catégorie fibre)','After the open curved stroke is a short low run; a separate l is not securely isolated, and an equality shorthand remains possible.','fibre','low')
imp('isolated ink mark','undecided',mark,'The crossed 6-like cluster and separate right mark are preserved graphically without a numeric identification.','isolated_mark','low')
imp('cancelled fermée','undecided',r'\deleted{\unsure{fermée}}','The f descender is visible but the heavy horizontal strike hides some internal letters.','triple_definition','low')
imp('respectant','undecided',r'\unsure{respectant}','The word is retained as a single run; its final thin loops are retraced and do not justify another cancelled word.','homeom_tail','medium')
imp('cancelled old S under D','undecided',r'\deleted{\unsure{S}}','A lower S-like bowl/run remains under the clear live D and cancellation, but cannot be fully isolated.','notation_old_d','low')
imp('cancelled quoted sauvage','undecided',r"\deleted{``\unsure{sauvage}''}",'The outer parts and g descender support sauvage, but not all internal letters are separable under the strike.','definition_words','low')
imp('folio','first',folio,'Crossed 7 followed by a closed oval 0.','folio','high')

doubts=[]
for q in decisions:
 doubts.append({'place':q['id'],'reading':q['reading'],'alternatives':'2° or 1°' if q['id']=='M0948' else 'chi or epsilon; the overwritten layer order is also unresolved','confidence':q['confidence'],'reason':q['evidence']})
for q in implicit:
 if q['decision']=='undecided':doubts.append({'place':q['place'],'reading':q['reading'],'alternatives':'Retained candidate or uncertain drawn ink; no additional identity or hidden lettering is supplied.','confidence':q['confidence'],'reason':q['evidence']})

inventory=[]
def inv(kind,pos,objects,hand='his hand'):
 inventory.append({'element':f'E{len(inventory)+1:02d}','sheet_kind':'text','hand':hand,'kind':kind,'position':pos,'first_words_or_objects':objects,'transcribed':'yes'})
for kind,pos,obj in [
('text','top','Groupoïdes de Teichmüller'),('display','item1 heading','Groupoïde topologique and open three-sided S T-top enclosure'),('text','right of item1 heading','groupoïde de Teichmüller spécial orienté topologique'),('display','item1 object specification','(X,S), X surface à bord compacte orientée; S subset boundary X'),('text','first morphism line','Morphismes (X,S) to (X-prime,S-prime)'),('text','small line above Variantes','1° S=phi, T-top, sous-groupoïde ouvert'),('text','below first subcase on right','groupoïde de T. ... orienté topologique'),('deletion','within that parenthesis','orient candidate'),('deletion','above Variantes on left','Vari'),('display','Variants heading line','Variantes, uncertain 2°/1°, S T-top plus/minus in open-join frame'),('text','below variant display','classes d’isotopie d’homéom.; orientation not necessarily respected'),('diagram','middle upper page','sign functor with overwritten chi/epsilon label and groupoid target description'),('deletion','immediately after sign arrow','unread crossed target, drawn without symbolic identification'),('deletion','after groupoïde in target','ponctuel'),('text','line below functor','le ... (la/= catégorie fibre) est S T-top'),('deletion','fibre line','noyau'),('deletion','fibre line after noyau','est'),('display','item2 object definition','2° (X,Sigma,S), three conditions'),('deletion','Sigma condition','fermée candidate'),('insertion','above cancelled fermée','compacte'),('text','item2 morphism condition','classes d’isotopie d’homéom respectant l’orientation'),('display','Notation line','T with cancelled old S and live D, subscript top'),('deletion','under live D','S candidate'),('insertion','over cancelled old letter','D'),('text','right of Notation line','(D) initiale de.'),('deletion','quoted word beneath replacement noun','sauvage candidate with paired quotes'),('insertion','above cancelled quoted word','dévissage'),('text','two lines following colon','quoted underlined groupoïde de Teichmüller orienté dévissé topologique'),('diagram','NB','S T-top subset S T D-top; vertical equality and Sigma-empty object description'),('deletion','right annotation to NB','immersion pleine within surviving parentheses'),('insertion','above NB cancelled annotation','imm. ouverte'),('text','final item','3° On définit de = T S-top plus/minus; biorienté dévissé topologique')]:inv(kind,pos,obj)
inv('drawing','isolated above item2 definition','crossed looped cluster plus detached small right mark','unnamed hand (isolated ink mark; attribution uncertain)')
inv('margin note','lower left','70','unnamed hand (folio annotation; attribution uncertain)')
notes=[
 {'id':f'{PAGE}-N01','text':'The page defines the special oriented topological Teichmüller groupoid from pairs (X,S), with X a compact oriented surface with boundary and S a finite subset of its boundary, and isotopy classes of isomorphisms as morphisms. The S-empty subcase receives T-top notation. A plus/minus variant permits homeomorphisms without necessarily preserving orientation and is accompanied by a sign/signature functor and a fibre statement. These source definitions and assertions are transcribed, not established by transcription.'},
 {'id':f'{PAGE}-N02','text':'The second construction uses (X,Sigma,S), with Sigma a compact one-dimensional submanifold of the interior and S finite in Sigma union boundary X. The old closedness word fermée is cancelled in favor of compactness. The notation is visibly revised from an S-like letter to D, and the raised dévissage replaces the cancelled quoted sauvage candidate. The NB identifies the Sigma-empty objects by a vertical equality and writes an open-immersion replacement over the cancelled full-immersion phrase. The final item writes T S-top plus/minus even though D was used in the preceding notation; the source S and the missing/added S-prefix variations are preserved, not repaired.'},
 {'id':f'{PAGE}-N03','text':'Conditional qualification of the sign-functor/fibre assertion: if disconnected X with independent orientation reversal on components is allowed, take S empty and X the disjoint union of two oriented disks. The identity and the two independent component reflections generate C2×C2; only the identity in this subgroup preserves both component orientations. Restricting a functor to the one-object groupoid [±1] gives a homomorphism C2×C2 to C2, whose kernel cannot be trivial because four elements map into two. Thus the asserted orientation-preserving fibre needs connectedness or a uniform-sign convention. This is conditional on that disconnected interpretation and is not a fault asserted against an unstated connectedness convention. The source definition is unchanged.'},
 {'id':f'{PAGE}-N04','text':'The first category enclosure is open at the top; the variant enclosure has a top stroke but an open upper-right join. Both are drawn as seen. The unknown cancelled target and the isolated crossed mark are reproduced in small doubtful TikZ drawings, without supplying a mathematical identity or a numeral. The literal point after de and the later unmatched closing parenthesis are retained. The signature caption has an opening parenthesis only.'},
 {'id':f'{PAGE}-N05','text':'The uniformly pale nested contours and small circles under the lower dark writing, with brown bleed-like dots and no corresponding dark graph or labels on this face, are treated as show-through background. C incorrectly promotes them into a separate recto figure. No exact verso or other-leaf match was checked, and none is claimed. The complete lower-block blind audit includes this region so the classification can be assessed independently. The folio is 70 with attribution left uncertain.'},
 {'id':f'{PAGE}-N06','text':'Physical reading count is 37 text/formula runs, including separately positioned caption, interlinear replacement and cancelled lines, the vertical-equality annotation and the folio. The isolated unidentified mark is additionally covered as a drawing. All 16 first-reader crops were viewed. The complete lower block is one audit unit to avoid repeating its revision and background regions across separate rectangles.'}
]
checks=[
 {'statement_id':f'{PAGE}-N01','type':'carried as background without fault found','outcome':'The object/morphism definitions and source notation were read and transcribed; this is not a proof of their mathematical properties.'},
 {'statement_id':f'{PAGE}-N02','type':'carried as background without fault found','outcome':'The triple construction, displayed inclusion and literal notation changes were retained. No independent proof of an open-immersion claim is asserted.'},
 {'statement_id':f'{PAGE}-N03','type':'targeted proof check','outcome':'Checked the conditional two-disk example: independent reflections form C2×C2 and only its identity preserves both orientations; any homomorphism to C2 has nontrivial kernel by cardinality. Root independently rechecked the same argument. This only records a needed qualification under the disconnected/unrestricted-sign interpretation, not an emendation of the source.'}
]
notation_entries=[
 {'sign':r'\phi','meaning_or_form':"ϕ : l'ensemble vide; oval with a long oblique descending crossing stem.",'places':'148_scan071 first S-empty subcase and NB Sigma-empty condition','universality':'Both visible empty-set occurrences on this leaf were checked separately.','witness_errors':'C uses varnothing and H emptyset; the written phi form is retained.'},
 {'sign':r'\Vert','meaning_or_form':'Two short upright parallel strokes denote the vertical equality beneath the first S T-top.','places':'148_scan071 NB','universality':'One local vertical equality.','witness_errors':'H flattens it to a baseline equals sign.'},
 {'sign':'=','meaning_or_form':'Two horizontal bars stand for même in de =.','places':'148_scan071 item3','universality':'One clear shorthand occurrence; the different compressed la/= cluster remains uncertain.','witness_errors':'H expands the item3 sign to même.'},
 {'sign':r'\mathcal TS_{\mathrm{top}}^\pm','meaning_or_form':'The final category has a clear S after calligraphic T, despite the preceding D revision.','places':'148_scan071 item3','universality':'This occurrence is preserved literally; it is not propagated as a corrected naming convention.','witness_errors':'Both witnesses retain S here; no mathematical normalization is made.'},
 {'sign':'raised replacement with crossing descender','meaning_or_form':'The descender of the live raised compacte crosses the old strike without cancelling the replacement. dévissage is likewise placed above its cancelled predecessor.','places':'148_scan071 Sigma condition and D-name explanation','universality':'Both local replacement scopes were checked.','witness_errors':'Both witnesses omit insertion state for dévissage; C also omits replacement state for imm. ouverte.'}
]
second=[]
def audit(box,kind,reading,target):
 x0,y0,x1,y1=box
 second.append({'box':f'B{len(second)+1:02d}','kind':kind,'x0':x0,'y0':y0,'x1':x1,'y1':y1,'reading':reading,'target':target})
audit(boxes['heading'],'different words',heading,'complete page heading')
audit(boxes['first_heading'],'handwritten number',first_heading,'complete item1 heading, enclosure and parenthetic name')
audit(boxes['isomorphismes_end'],'different words',"d'isomorphismes",'end of first morphism sentence')
audit(boxes['first_case'],'struck passage',case1,'complete S-empty subcase and parenthetic name, including cancelled word')
# The adjacent continuation is included to keep the entire variant morphism formula in its unit.
audit([228,494,1670,758],'doubtful formula',variants,'Variants heading and complete first variant, including disputed numeral and both displayed/inline category formulas')
audit(boxes['signature_functor'],'doubtful formula',functor,'complete sign functor, cancelled target and live groupoid description')
audit(boxes['fibre'],'struck passage',fibre,'complete fibre line with both cancellations and la/= doubt')
audit([300,1057,1640,2160],'low-confidence departure',lower,'complete lower block: isolated mark, item2, all lower revisions, NB, item3, and independent assessment of underlying pale contours')
audit(boxes['folio'],'handwritten number',folio,'complete lower folio')

out={'page':PAGE,'reader':'reader_c','lines_read':37,'changes':changes,'decisions':decisions,'implicit_decisions':implicit,'doubts':doubts,'inventory':inventory,'notes':notes,'check_events':checks,'notation':notation_entries,'abbreviations':[{'form':'T.','expansion':'Teichmüller'},{'form':'homéom. / homéom','expansion':'homéomorphismes; the written occurrence-specific point is retained or omitted'},{'form':'dim','expansion':'dimension'},{'form':'imm.','expansion':'immersion'},{'form':'=','expansion':'même in de ='}],'second_boxes':second,
'agreed_ink_checks':['The pair and triple definitions, every prime on the first two morphism pairs, all source plus/minus exponents, each subscript top, the dimension numeral1 and both subset/union/boundary signs were checked against the ink.','Both ordinary morphism paragraphs and the full underlined names were read; respectant remains locally doubtful because of its retraced ending.','Cancellation and replacement scopes were separately checked for Vari, orient, target/ponctuel, noyau/est, fermée/compacte, old S/live D, quoted sauvage/dévissage, and immersion pleine/imm. ouverte.','The final T S-top plus/minus and the folio70 agree with C and were checked directly, without normalizing the category name.'],
'supporting_evidence':[{'name':n,'crop':f'crops/{PAGE}_{n}.png','box':b,'viewed':True} for n,b in boxes.items()],
'reading_protocol':{'original_views':1,'prepared_half_views':[1,1],'evidence_crops_viewed':16,'second_reading_started':False,'ocr_used':False,'web_used':False,'tex_compiled':False,'notation_source':'result/notation_working.md; packet notation.md was stale and empty'}}
# Ensure that quoted apostrophes were not accidentally turned into TeX accent commands.
def clean(v):
 if isinstance(v,str):return v.replace("\\'","'")
 if isinstance(v,list):return [clean(x) for x in v]
 if isinstance(v,dict):return {k:clean(x) for k,x in v.items()}
 return v
out=clean(out)
(B/'proposed'/f'{PAGE}.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'tex':str(B/'proposed'/f'{PAGE}.tex'),'json':str(B/'proposed'/f'{PAGE}.json'),'changes':len(changes),'marks':len(decisions),'implicit':len(implicit),'doubts':len(doubts),'inventory':len(inventory),'second_boxes':len(second)}))
