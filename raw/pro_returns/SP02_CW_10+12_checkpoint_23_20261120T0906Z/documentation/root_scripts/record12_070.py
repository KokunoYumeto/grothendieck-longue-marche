from pathlib import Path
import sys,json
sys.path.insert(0,str(Path('SP02_CW_10+12/scripts').resolve()))
from root_record import Record
r=Record('B12-01',12,70,'cancelled_draft')
H='[No H text supplied.]'
def ch(place,C,final,shows,crop,kind='other',confidence='high',against_C=False,consequential=False):
 r.change(place,C,H,final,shows,crop,kind,confidence,against_C,False,False,consequential)
def stack(base,ins,center=False,shift='0cm'):
 anchor='south' if center else 'south west';point='north' if center else 'north west'
 return r'\mbox{\begin{tikzpicture}[baseline=(base.base)]'+'\n'+r'\node[inner sep=0] (base) {'+base+r'};'+'\n'+r'\node[anchor='+anchor+r',inner sep=0,yshift=.08cm,xshift='+shift+r'] at (base.'+point+r') {\inserted{'+ins+r'}};'+'\n'+r'\end{tikzpicture}}'
chacune=stack(r'\deleted{Les}','Chacune des',True)
r.edit(r'\deleted{Les}\inserted{Chacune des}',chacune)
raisedR=r'\raisebox{1.7ex}{\inserted{\uuline{R}}}'
r.edit(r'\inserted{\uuline{R}}',raisedR)
cond=stack(r'vérifier la condition (b), \deleted{qui}','et la cond univ cat dans (ii)',False,'-.05cm')
r.edit(r'vérifier la condition (b)\inserted{et la cond univ cat dans (ii)}, \deleted{qui}',cond)
qui=stack('est','qui')
r.edit(r'\inserted{qui} est',qui)
r.edit(r'\unsure{tout que|tant que}',r'\unsure{tout|tant} que')
cas=stack('lieu singulier. Cette condition est','(et dans le cas (ii) est univ cat).',False,'.25cm')
r.edit(r'lieu singulier.\inserted{(et dans le cas (ii) est univ cat).} Cette condition est',cas)
cat=r'caté\rlap{h}naire'
r.edit('caténaire',cat)
tir=r'ti\rlap{e}rer'
r.edit('tirer',tir)
gata=r'''\margin{\deleted{\mbox{\begin{tikzpicture}[baseline=(word.base)]
\node[inner sep=0] (word) {gata};
% Faint extra curved impression and lower spot at the right of the last a; identity/function uncertain.
\draw[line width=.35pt,opacity=.65] ([xshift=-.05cm,yshift=.10cm]word.east) .. controls ([xshift=.09cm,yshift=.11cm]word.east) and ([xshift=.10cm,yshift=.03cm]word.east) .. ([xshift=.02cm,yshift=-.01cm]word.east);
\fill[opacity=.65] ([xshift=.04cm,yshift=-.05cm]word.east) circle (.015cm);
\end{tikzpicture}}}}'''
r.edit(r'\margin{\deleted{gata}}',gata)
condmark=r'''\mbox{\begin{tikzpicture}[baseline=(word.base)]
\node[inner sep=0] (word) {condition};
\path (word.north west) -- coordinate[pos=.32] (mark) (word.north east);
% Isolated short brownish vertical trace; no letter or function assigned.
\draw[line width=.4pt] ([yshift=.08cm]mark) -- ([yshift=.21cm,xshift=-.01cm]mark);
\end{tikzpicture}}'''
r.edit('aux condition a)','aux '+condmark+' a)')
ch('heading, Chacune des over deleted Les',r'\deleted{Les}\inserted{Chacune des}',chacune,'Chacune des is centered on the line above the canceled Les, extending left and right of its three cells. The L stem/foot, e middle and s curves remain readable under the x row. No insertion leader is present. The two vertical levels are preserved.','heading; Les','insertion or placement','high',True)
ch('heading, inserted R',r'\inserted{\uuline{R}}',raisedR,'R is on the upper typing line, above the gap between propriétés and suivantes. Two separate underlines lie beneath its feet. C records the word order but leaves the R at the baseline; the raised position is retained.','heading; Rinsert','insertion or placement','high',True)
ch('above the first condition','[not represented]',condmark,'A short isolated brownish near-vertical trace stands above the first third of condition. It has no securely alphabetic form; its line is reproduced without identifying a letter, origin or function.','condition; brownmarkA','drawing or diagram','low',True)
ch('et la cond univ cat dans (ii), interlinear addition',r'\inserted{et la cond univ cat dans (ii)}',cond,'The addition occupies the line above vérifier la condition (b), qui, beginning almost above the v of vérifier. All words and both i letters are clear; no abbreviation periods or leader are visible. Its placement is preserved.','condinsert; insertplaceB; bquice','insertion or placement','high',True)
ch('replacement qui above est',r'\inserted{qui} est',qui,'The q descender, u and dotted i are typed immediately above est at the next line start. The earlier qui after (b) is x-canceled and ce remains live within the globally canceled paragraph. The replacement is kept above est.','quiinsert; quiplaceB; bquice','insertion or placement','high',True)
ch('canceled words after si',r'\unsure{tout que|tant que}',r'\unsure{tout|tant} que','The two t ascenders/crossbars and the central rounded/bowled forms support tout, but x overtyping prevents a secure decision against tant. In the following word the q descender and foot, u lower bowl and final e curves/middle are recoverable despite the diagonal line. C macro/table doubt is narrowed to the first word.','toutcancel; toutcellsB; queB','misread word','medium',True)
ch('parenthetical interlinear addition',r'\inserted{(et dans le cas (ii) est univ cat).}',cas,'The parenthetical is typed between the quotient/régulier line and the Nagata/lieu singulier line, beginning above the middle of lieu and extending over Cette condition est. Its outer parentheses, two i letters and final period are present. No leader assigns it a new baseline position.','casinsert; insertplaceB','insertion or placement','high',True)
ch('universellement caténaire, n cell','caténaire',cat,'The cell after é has a full tall left stem and ascender-height serif matching h in Coh, plus a second leftward serif at x height matching n in normal. The arch/right leg and feet are shared. Both h and n impressions are retained without a typing chronology.','catenaire; catcellB; hcontrolA; ncontrolA','misread word','high',True)
ch('last line, tirer, first r cell','tirer',tir,'The cell after i contains the r left stem, long upper serif/shoulder and foot, together with a complete e upper curve, middle bar and lower bowl. The following e and final r are separate. Both overlapping impressions are retained without chronology.','tirer; tircellB','misread word','high',True)
ch('left margin gata, extra impression at final a','gata',gata,'The four letters gata are readable. At the right edge of the last a there is a faint separate curved upper trace and a lower spot, which resembles a small question mark but cannot be securely identified. Those marks are reproduced as shapes; they are not asserted as a question or another letter. The long global diagonal crosses t.','gata; gatalastB; gataextraB','drawing or diagram','low',True)
ch('left margin gata, purpose','gata','gata','The fragment is lower and far left of the fully written Nagata on the main line. It has no leader. C table uncertainty about its relationship to Nagata is retained; the main Nagata is complete and no attachment is supplied.','gata; Nagata; NagatafullB','other','medium')
for loc,reading,desc,crop in [
 ('opening grammatical form','aux condition a) et b)','The final n of condition is followed by a blank and a); no s is typed.','condition; firstrefA'),
 ('middle paragraph spelling','vérifiéé','A distinct acute is visible over each of the two final e letters, as well as over the first e. The spelling is retained.','verifiee; quiplaceB'),
 ('list (i)',r'\operatorname{coprof}C\quad n','The p stem is partly crossed by the global diagonal but its lower foot survives. C and n stand at the same height with a blank between; no comparison sign is present.','coprof'),
 ('bottom morphism spaces',r'A\quad B; \operatorname{Spec}(B)\quad\operatorname{Spec}(A)','The A and B are visible under the deletion row, with only x strokes between. The later Spec(B) and Spec(A) have clear blank space between; no arrow is supplied.','ABcancel; SpecBSpecA'),
 ('canceled bottom clauses','il en est de même; (Spec(B) étant','Letter contours, the circumflex in même, the acute in étant, and the parentheses survive the x rows. The unfinished opening parenthesis is retained.','ilenest; Specdeleted'),
 ('separate canceled reference in Remarques (ii)',r'\deleted{(ii)}','A short oblique pencil stroke crosses just this (ii), in addition to the long global cancellation strokes. Both dotted i letters and both parentheses remain clear.','remrefs; remiicancel')]:
 ch(loc,reading,reading,desc,crop)
r.doubt('canceled word after si','tout','tant','low','The middle two letters are fused with x strokes; que is independently readable.')
r.doubt('left margin gata','gata','relationship to Nagata undetermined','medium','Both the full main-line name and the detached fragment are present; there is no connecting leader.')
r.doubt('right edge of final a in gata','curved trace and separate lower spot','small question mark; stray/overtyped impression','low','Shapes reproduced without asserting a question mark or an alphabetic value.')
r.doubt('short vertical trace above condition','near-vertical stroke','origin/function undetermined','low','No letter or textual meaning is assigned to the isolated brownish trace.')
r.notation('typed double-underlined property R',r'\uuline{R}; \text{\uuline R}(A); \text{\uuline R}(B)','12:070 heading insertion and all four bottom property occurrences have two separate underlines; list R_n is plain.')
r.notation('lowered condition indices',r'S_n; R_n','12:070 list ii/v; each n is lowered, with no underline or prime.')
r.notation('blank relation slots',r'\operatorname{coprof}C\quad n; A\quad B; \operatorname{Spec}(B)\quad\operatorname{Spec}(A)','12:070 all three visible blank slots retained; no inequality or arrow supplied.')
r.notation('overprinted typewriter letters',cat+'; '+tir,'12:070 h/n cell in caténaire and e/r cell in tirer; shared glyph cells with no chronology assigned.')
r.notation('spelling and accents retained','aux condition; vérifiéé','12:070 singular condition and two final acute-accented e letters verified in separate enlargements.')
for a,e in [('Coh Mac','Cohen–Macaulay'),('coprof','coprofondeur'),('cond','condition'),('univ cat','universellement caténaire'),('univ','universellement')]:
 r.r.setdefault('abbreviations',[]).append(dict(abbreviation=a,expansion=e,attestations='12:070'))
r.r['inventory_overrides']={'070-19':dict(first_words_or_objects='qualified tout/tant; readable que'), '070-21':dict(first_words_or_objects='gata; faint extra curved trace and lower spot at final a')}
for i,(s,k,p,h) in enumerate([('h/n overprint in caténaire','text','middle paragraph','typewriter'),('e/r overprint in tirer','text','last line','typewriter'),('faint curved trace and separate spot at final a of gata, identity uncertain','drawing','left margin','another unnamed hand'),('short near-vertical trace, origin/function uncertain','drawing','above first condition','another unnamed hand'),('archive sheet number 69 retained as comment','margin note','bottom-left corner','another unnamed hand')],1):
 r.r['inventory_extra'].append(dict(scan='12:070',sheet_kind='cancelled_draft',hand=h,element=f'070-R{i:03d}',kind=k,position=p,first_words_or_objects=s,transcribed='yes'))
r.r['crops']=json.loads(Path('work/crops12_070.json').read_text())+json.loads(Path('work/fine12_070.json').read_text())
r.r['inspection_note']='Root alone viewed whole070 and both actual supplied halves before C/H, then the C macro doubt, both table doubts, three slips, five abbreviations and all28 inventory elements. H has no text, so all H flags remain false. All67 crop recipes were viewed (50 initial,17 fine); the cropped Nagata tail was extended to cover the full name. Every mathematical sign/index, deletion, insertion, overprint and marginal mark was enlarged. Four long oblique cancellation strokes were followed across the page; the separately canceled (ii) was distinguished from them. No slanted verbal note occurs. Both actual halves were reread line by line after all crops. Fai at the right edge continues as re on the next line, and égale- continues as ment; joined words do not supply absent letters. The two small isolated traces are drawn without assigning alphabetic content or a definite origin. Archive69 remains a comment. Context is sealed; this is first-pass collation, not ordered audit or mathematical checking.'
r.save('work/record12_070.json')
