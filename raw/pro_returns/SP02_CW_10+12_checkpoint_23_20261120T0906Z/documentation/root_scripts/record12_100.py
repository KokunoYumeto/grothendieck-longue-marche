from pathlib import Path
import sys,json
sys.path.insert(0,str(Path('SP02_CW_10+12/scripts').resolve()))
from root_record import Record
r=Record('B12-01',12,100,'typescript')
ring=r'''\mbox{\begin{tikzpicture}[baseline=(base.base)]
\node[inner sep=0] (base) {intersection};
\node[anchor=base west,inner sep=0,xshift=.7em] (right) at (base.base east) {of};
\node[anchor=south west,inner sep=0,xshift=-.7em,yshift=.5ex] (added) at (base.north east) {\inserted{\handwritten{ring}}};
\draw ([xshift=.1em,yshift=-.8ex]base.south east) -- ([xshift=.25em,yshift=.2ex]base.north east) -- ([xshift=.6em,yshift=-1.5ex]base.south east);
\end{tikzpicture}}'''
r.edit(r'intersection\inserted{\handwritten{ring}} of',ring)
pencil=r'\handwritten{modulo rational equivalence \unsure{[|(}the Chow ring of $(\unsure{K|X})$}'
modulo=r'''\mbox{\begin{tikzpicture}[baseline=(base.base)]
\node[inner sep=0] (base) {on $X$,};
\node[anchor=base west,inner sep=0,xshift=.5em] (right) at (base.base east) {tensored by $Q$. Then, for};
\node[anchor=south west,inner sep=0,xshift=-.7em,yshift=.5ex,font=\small] at (base.north west) {\inserted{'''+pencil+r'''}};
\draw ([xshift=.1em,yshift=-.6ex]base.south east) -- ([xshift=.2em,yshift=.2ex]base.north east) -- ([xshift=.5em,yshift=-1.3ex]base.south east);
\end{tikzpicture}}'''
r.edit(r'on $X$,\inserted{\handwritten{modulo rational equivalence \unsure{(the Chow ring of $(X)$|(the Chow ring of $(K)$}}} tensored by $Q$. Then, for',modulo)
r.edit(r'i\handwritten{\leq}n',r'i\handwritten{\leqslant}n')
r.edit(r'\quad(j=0,\ldots,2n)',r'\quad(j=0,\ldotp\,\unsure{\ldotp}\,\ldotp,2n)')
r.edit(r'\handwritten{\kappa_X\bigl(\alpha\cdot\rho_X(Z)\bigr)=\kappa_Z\bigl(\operatorname{res}_Z(\alpha)\bigr)',r'\handwritten{\unsure{\kappa_X|K_X}\bigl(\alpha\cdot\rho_X(Z)\bigr)=\unsure{\kappa_Z|K_Z}\bigl(\operatorname{res}_Z(\alpha)\bigr)')
over=r'''\mbox{\begin{tikzpicture}[baseline=(old.base)]
\node[inner sep=0] (old) {\deleted{on}};
\node[anchor=south west,inner sep=0,yshift=.2ex] at (old.north west) {\inserted{\handwritten{over}}};
\end{tikzpicture}}'''
r.edit(r'\deleted{on}\inserted{\handwritten{over}}',over)
thet=r'th\rlap{\unsure{a|e}}et'
r.edit(r'\unsure{thet|that}',thet)
image_exponent=r'''\mbox{\begin{tikzpicture}[baseline=(star.base)]
\node[inner sep=0] (star) {$\scriptstyle *$};
\node[anchor=base,inner sep=0,xshift=.12em,yshift=.35ex] at (star.base) {$\scriptstyle\handwritten{\unsure{\imath}}$};
\end{tikzpicture}}'''
r.edit(r'\handwritten{\rho_X}(C^*(X))',r'\handwritten{\rho_X}(C^{'+image_exponent+r'}(X))')
def ch(place,C,H,final,shows,crop,kind='other',confidence='high',against_C=False,against_H=True,marked_in_H=False,consequential=False):
 r.change(place,C,H,final,shows,crop,kind,confidence,against_C,against_H,marked_in_H,consequential)
ch('ring and insertion caret',r'intersection\inserted{\handwritten{ring}} of','intersection ring of',ring,'The pencil word ring is above the intersection/of gap. Two unequal pencil strokes form an insertion caret below it, with the right leg extending farther down. The word was enlarged and rotated to read its r/i/n/g sequence. Both drafts flatten its relative position and omit the caret.','ring;ringrot;ringplace','insertion or placement',against_C=True)
ch('modulo rational equivalence and following pencil note',r'inserted after typed X comma, before tensored',r'modulo rational equivalence, tensored by Q (the Chow ring of X)',modulo,'The entire pencil phrase is on one raised line, beginning above on X and ending above Then, for. A light two-legged insertion mark is immediately after the typed comma following X. H moves the note to after Q and moves the comma to after equivalence; the actual comma and continuous raised phrase are retained. The small pencil words and their mild slant were checked in enlarged and rotated crops.','modulo;equivalence;Chow;Chowrot;modplace;modleader;modrot','insertion or placement',against_C=True)
ch('pencil note opening mark',r'(the Chow ring',r'(the Chow ring',r'\unsure{[|(}the Chow ring','The opening mark has a long nearly vertical middle and a short rightward lower return, with a faint upper bend. A square bracket is the first visible reading, but the faint curved top leaves a parenthesis as an alternative. Neither shape is silently regularized.','Chow;Chowbracket','misread symbol or index','medium',True)
ch('pencil note final letter and parentheses',r'\unsure{(the Chow ring of $(X)$|(the Chow ring of $(K)$}',r'(the Chow ring of X)',r'of $(\unsure{K|X})$','There is a distinct opening parenthesis before a K-like letter with a near-upright left stroke, a short upper-right arm and a lower-right leg, then one closing parenthesis. K is put before X on graphic evidence. No second final closing mark or comma is supplied to balance the earlier opening mark.','Chow;Chowrot;Chowend','misread symbol or index','medium',True,True,False,True)
ch('coefficient Q at four loci',r'Q; Q_\ell; Q; Q_\ell',r'\mathbb{Q} at all four loci',r'Q; Q_\ell; Q; Q_\ell','The three typed Qs each have one rounded body and a small descending hook; the pairing’s hand Q is a single round body with a long lower tail. No double stroke or underline occurs. Both coefficient ells are lowered.','Qtop;pairQ;Qdot;Qcoh','misread symbol or index',consequential=True)
ch('inequality between i and n',r'\leq',r'\leqslant',r'\handwritten{\leqslant}','The separate lower stroke slopes down to the right parallel to the lower arm of the less-than sign. H’s slanted-bar form matches the ink.','ileqn','misread symbol or index',against_C=True,against_H=False)
ch('typed l-adic and Poincare','l-adic Poincare',r'\ell-adic Poincaré','l-adic Poincare','The initial l is a typewriter serifed stem without an added loop/crossing stroke; the final e of Poincare has no acute above it. The printed forms are retained.','Poincare','abbreviation expanded or spelling modernised')
ch('trace label over the pairing arrow',r'\unsure{\kappa_X|K_X}',r'\kappa_X',r'\unsure{\kappa_X|K_X}','The small label has one short left stroke and two right arms; its X is lowered. The ink does not securely distinguish the Greek kappa from a handwritten capital K, so C’s doubt is retained rather than settled by the label’s mathematical role.','trace','misread symbol or index','medium',consequential=True)
ch('isomorphism mark position',r'\overset{\kappa_X}{\overset{\sim}{\longrightarrow}}',r'\xrightarrow[\sim]{\kappa_X}',r'\overset{\unsure{\kappa_X|K_X}}{\overset{\sim}{\longrightarrow}}','The wavy mark is above the rightward arrow, with the trace label on a still higher level. Nothing is written below that arrow. H puts the wavy mark below it.','trace','insertion or placement')
ch('dots in the index range',r'(j=0,\ldots,2n)',r'(j=0,\ldots,2n)',r'(j=0,\ldotp\,\unsure{\ldotp}\,\ldotp,2n)','Two dark separate dots occur between the commas. At the middle position there is only a faint grey trace that cannot securely be separated from the paper texture; it is retained as a qualified possible third dot, not asserted as a normal three-dot ellipsis.','jrange;twodots','misread symbol or index','low',True)
ch('two trace symbols in the defining condition',r'\kappa_X; \kappa_Z',r'\kappa_X; \kappa_Z',r'\unsure{\kappa_X|K_X}; \unsure{\kappa_Z|K_Z}','Both have the same K-shaped construction as the earlier qualified trace label: a left stroke and two rightward arms. The X and Z subscripts are clear. Their alphabet ambiguity is treated consistently with the first label; the restriction symbol and its Z remain unambiguous.','conditionleft;conditionright;trace','misread symbol or index','medium',True,True,False,True)
ch('quotation marks around algebras',r"\handwritten{``}algebras\handwritten{''}",'« algebras »',r"\handwritten{``}algebras\handwritten{''}",'Each pen quotation pair has two short downward strokes above the type line. Neither consists of angle marks.','quotes','misread symbol or index')
ch('over above cancelled on',r'\deleted{on}\inserted{\handwritten{over}}',r'\struck{on} over',over,'The typed on is crossed by a single rising pencil line. Pencil over stands directly above it, beginning at its left edge and extending farther right; the rotated crop gives o/v/e/r. No separate connecting leader is present.','onover;overrot','insertion or placement',against_C=True)
ch('low mark after Q before last display',r'Q\unsure{.}','Q with no mark',r'Q\unsure{.}','A distinct dark oval lies below and to the right of Q, separated from its hooked tail. Its identity as an intentional period rather than stray ink remains uncertain; C’s qualification is kept.','Qdot','omission','low')
ch('two periods after the last display',r'H_\ell^*(X)..',r'H_\ell^*(X).',r'H_\ell^*(X)..','Two separate pen points follow the closing parenthesis, on the same low level. Both are retained.','map2right','omission')
ch('period immediately before is','homomorphism .is','homomorphism is','homomorphism .is','A separate dark typewriter point sits in the space after homomorphism and immediately before the following i. It is not that i’s raised dot.','dotis','omission')
ch('overprinted vowel and final t in thet',r'\unsure{thet|that}','the',thet,'A dark e has a clear bar and open lower-right bowl. An older lighter impression has a right upright/foot and lower bowl compatible with a, but is partly fused, so a/e remains qualified under the e. A separate final typed t has an ascender, crossbar and hooked foot and is not struck. H drops it.','thet;thetcell','misread word','medium',True)
ch('altered exponent in the final paragraph’s image expression',r'\rho_X(C^*(X))',r'\rho_X(C^*(X))',r'\rho_X(C^{'+image_exponent+r'}(X))','The machine asterisk remains visible, but a distinct heavier pen stroke lies over its upper-right part: a short upright turning into a rightward hook, resembling an undotted i. No separate dot can be distinguished at the highest enlargement. Both the old star and the raised, qualified undotted i-like stroke are preserved; no degree is chosen from the mathematics.','Cimage;imageexponent;Ci','misread symbol or index','low',True,True,False,True)
for place,reading,shows,crops in [
 ('underlined headings and term','2. Formalism of Algebraic Cohomology Classes; Cohomology Class Associated to a Cycle; cohomology class','All three have separate drawn underlines. The two heading periods lie beyond the right ends of their lines, as C represents them. The words and title capitals are read directly; font-formatting conventions alone are not counted as separate H text variants.','title;subhead;underline'),
 ('first cycle map',r'\rho_X:C^i(X)\longrightarrow H_\ell^{2i}(X)','The rho has a closed upper bowl and long lower stem, its X is lowered, the source i has a distinct dot, the target exponent has 2 followed by dotted i, and the ell is below H. The arrow has one shaft and one rightward head. No extra twist or decoration is added.','Cstar;rho1;arrow1;H1'),
 ('duality pairing objects and degrees',r'H_\ell^j(X)\times H_\ell^{2n-j}(X)\longrightarrow H_\ell^{2n}(X)','The two j signs each have a dot and descending hooked stroke. The second exponent is 2n-j, the target exponent is 2n, each ell is lowered, and the product sign has two crossing diagonals. The connecting arrow is unlabelled.','pairleft;pairarrow;pairH'),
 ('inline cycle class',r'\rho_X(Z)\in H_\ell^{2i}(X)','The argument Z has top/bottom horizontals joined by a diagonal; membership has an open curve and middle bar; 2i and ell have their stated upper/lower levels.','rhoelement'),
 ('defining equation and range',r'\alpha\cdot\rho_X(Z); \operatorname{res}_Z(\alpha); \text{for all }\alpha\in H_\ell^{2n-2i}(X).','The dot between alpha and rho is separate, res is written in full with lowered Z, both pairs of nested parentheses are visible, and the range exponent is 2n-2i with a dotted final i. A final point follows the right parenthesis.','conditionleft;conditionright;forall'),
 ('extension degree',r'\rho_X; C^{\handwritten{i}}(X)','The standalone rho and subscript X are handwritten. The added i above the typed C has a separate dot and a curved lower end; no star is visible at this locus.','rhotext;Ci'),
 ('graded map',r'\rho_X:C^*(X)\longrightarrow H_\ell^*(X)','Both displayed stars consist of several crossing pen strokes, with no i correction. The target ell is below H, and the sole arrow points right.','map2left;map2right'),
 ('final notation and final rho',r'C_\ell^*(X); Q_\ell; \rho_X.','The target C retains its printed asterisk with a hand ell below; the Q has a separate lower ell before the hyphen. The final standalone rho has a lowered X followed by a pen point.','Ctarget;Qcoh;rhoend')]:ch(place,reading,reading,reading,shows,crops,against_H=False)
for line,reading,alts,conf,comment in [
 ('pencil note opening mark','[','(','medium','Long vertical middle and short rightward foot favour a bracket, but faint upper bend leaves parenthesis possible.'),
 ('pencil note final letter','K','X','medium','Near-upright left stroke and two rightward arms favour K; pencil softness prevents excluding X.'),
 ('trace labels, three occurrences',r'\kappa_X; \kappa_Z',r'K_X; K_Z','medium','The same handwritten K-shaped construction does not distinguish the two alphabets securely.'),
 ('middle of index-range ellipsis',r'\ldotp','paper texture / no intentional middle point','low','Two dark dots are definite; the intervening grey trace remains qualified.'),
 ('after algebras over Q','.','stray ink','low','Separate low dark point is visible, but its punctuation status is not settled.'),
 ('old vowel under e in thet','a','e','medium','Grey lower bowl/right upright are partly fused with the darker e.'),
 ('added stroke over final-paragraph asterisk',r'\imath','unidentified pen modification of the asterisk','low','Short upright and right hook resemble an undotted i; no dot is separately visible. The star remains beneath it.')]:r.doubt(line,reading,alts,conf,comment)
r.notation('trace letter in this typescript',r'\unsure{\kappa_X|K_X}; \unsure{\kappa_Z|K_Z}','12:100 three K-shaped labels treated alike; alphabet unresolved, subscripts clear.','unresolved')
r.notation('plain rational coefficient letter',r'Q; Q_\ell','12:100 three typed Qs and one handwritten Q; no underlines or doubled stems.')
r.notation('slanted lower inequality bar',r'\leqslant','12:100 i/n inequality has lower stroke parallel to the descending lower arm.')
r.notation('hand quotation marks',r"``algebras''",'12:100 two short high pen strokes at each end, not guillemets.')
r.notation('altered degree above C in image expression',r'* with superposed qualified \imath','12:100 final paragraph; both the old printed asterisk and the added pen hook are retained.','unresolved')
r.r['abbreviations']=[dict(abbreviation='res',expansion='restriction',attestations='12:100 defining equation')]
r.r['inventory_overrides']={
 '100-03':dict(hand='another unnamed hand',position='pencil ring above intersection/of gap'),
 '100-04':dict(hand='another unnamed hand',position='pencil line above on X through Then, for',first_words_or_objects='modulo rational equivalence; qualified opening bracket; the Chow ring of (K/X), one final parenthesis'),
 '100-17':dict(hand='another unnamed hand',position='pencil over directly above cancelled on'),
 '100-08':dict(first_words_or_objects='duality pairing; qualified trace alphabet; two dark dots and a qualified faint middle dot'),
 '100-11':dict(first_words_or_objects='qualified kappa/K labels with clear X,Z subscripts; restriction equation'),
 '100-19':dict(first_words_or_objects='The image of a cycle; overprinted e on qualified old a/e in thet')}
for n in [5,6,8,10,11,13,14,15,18,20,21,22,23]:r.r['inventory_overrides'].setdefault(f'100-{n:02d}',{}).update(hand='another unnamed hand')
extras=[
 ('insertion caret for ring','drawing','between intersection and of','another unnamed hand'),
 ('insertion caret for pencil modulo phrase','drawing','after typed X comma','another unnamed hand'),
 ('old vowel impression beneath e in thet','text','associated with ... cycle','typewriter'),
 ('qualified undotted i-like pen stroke above printed asterisk','insertion','rho image expression in final paragraph','another unnamed hand'),
 ('archive folio99 retained as comment','margin note','bottom left','another unnamed hand')]
for i,(s,k,p,h) in enumerate(extras,1):r.r['inventory_extra'].append(dict(scan='12:100',sheet_kind='typescript',hand=h,element=f'100-R{i:03d}',kind=k,position=p,first_words_or_objects=s,transcribed='yes'))
r.edit('we denote ',r'we den\unsure{ö|o}te \unsure{f} ')
ch('marks above o in denote','denote','denote',r'den\unsure{ö|o}te','Two separate short marks stand above the round o, the left dark and the right lighter. They can read as a diaeresis, but the right trace partly approaches the letter and may be an offset type impression. The graphic first reading ö is qualified against o rather than silently discarded on English spelling grounds.','denote;denoteo','misread word','low',True)
ch('faint fragment after denote','omitted','omitted',r'\unsure{f}','A faint further type impression follows the final e at the line end. Its upper hook, partial left upright and possible short crossbar resemble f; the lower parts are too pale to settle the character or whether it was erased. The fragment is retained with qualification and no cancellation state is invented.','denote;denoteend','omission','low',True)
r.doubt('o in denote','ö','o with offset type traces','low','Two high marks are visible, one much fainter; accent versus overprint is not secure.')
r.doubt('faint fragment after denote','f','unidentified pale type impression; possible erasure','low','Upper hook and part of an upright survive; lower contours and state are not secure.')
r.r['inventory_extra'].append(dict(scan='12:100',sheet_kind='typescript',hand='typewriter',element='100-R006',kind='text',position='we denote at end of last-paragraph line',first_words_or_objects='qualified two high marks above o and faint f-like following fragment',transcribed='yes'))
for row in r.r['changes']:
 if row['place']=='altered exponent in the final paragraph’s image expression':row['crop']+=';imageexponentfull'
r.r['crops']=json.loads(Path('work/crops12_100.json').read_text())
r.r['inspection_note']='Root alone viewed the whole supplied scan and both actual halves before reading full C/H, all four C macro/table doubts, five slip rows, the res abbreviation and all23 inventory elements. All54 crop recipes were viewed, including eleven adaptive close-ups; ring, the Chow note, the modulo phrase and over were also viewed rotated upright. Every displayed and inline mathematical sign/index was checked, together with deletions, insertions and punctuation. Both actual halves were reread line by line after the main local choices; that rereading prompted four final crops covering the full space above the altered asterisk and the faint traces at denote. These were checked before finalization. This unsigned English typescript is inventoried as typescript, with typewriter and unnamed pen/pencil hands; attribution is not inferred from either witness’s editorial suggestion. Archive99 is a comment. Context remains sealed, and no mathematical check event or ordered second-reading audit is claimed.'
r.save('work/record12_100.json')
