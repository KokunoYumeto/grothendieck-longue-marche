from pathlib import Path
import sys,json
sys.path.insert(0,str(Path('SP02_CW_10+12/scripts').resolve()))
from root_record import Record
r=Record('B10-10',10,133);ch=r.change
phi=r'\unsure{\phi|\varphi}'
vee=r'\overset{\handwritten{\unsure{\vee|\nu|v}}}{X}'
CX=r'\rlap{\(X\)}C'
F=r'\unsure{\rlap{f}F|F}'
U=r'\rlap{\(M\)}U'
one=r'\unsure{\rlap{\(4\)}1|\mathbb{1}|1}'
X=r'\rlap{\(C\)}X'
gen=r'gén\handwritten{\unsure{é|\rlap{u}é}}ral'
paren=r'\unsure{\rlap{,})|)}'
r.edit(r'avec $\otimes,',r'avec $\unsure{\otimes|\Omega},')
r.edit(r'\unsure{\varphi|\phi}',phi)
r.edit(r'\unsure{X|X^{\handwritten{\vee}}}',vee)
r.edit(r'\deleted{\unsure{X}}C',CX)
r.edit(r'sans doute\deleted{\unsure{s|x}}',r'sans doute\deleted{i}')
r.edit(r'Ils\deleted{\unsure{s|x}}',r'Ils\deleted{s}')
r.edit('Pour remédier','Pour rémédier')
r.edit('des Faisceaux','des '+F+'aisceaux')
r.edit('relativement',r'relative\rlap{e}ment')
r.edit(r'\unsure{\mathbb{U}|U}',U)
r.edit('serait satisfait',r'serait \rlap{s}\kern.35em atisfait')
r.edit(r'\handwritten{\varphi}',r'\handwritten{\phi}')
r.edit(r'{}^{\handwritten{\unsure{\vee|\nu|v}}}',r'{}^{\handwritten{\vee}}')
r.edit(r'\unsure{\mathbb{1}|1}',one)
r.edit(r'\unsure{orops|orps|corps}','orops')
r.edit(r'\unsure{\mathbb{X}|X}',X)
r.edit('sur $k$ (NB',r'\rlap{(}sur $k$ (NB')
r.edit('en général pas','en '+gen+' pas')
r.edit("``cohérent'').", "``cohérent''"+paren+'.')
# Each leader is a drawing; the inserted words occur only once.
def leader(text,width=6.2):
 return r'''\begin{tikzpicture}[baseline=-.6ex,x=1cm,y=1cm]
\node[anchor=west,inner sep=0] at (0,.4) {'''+text+r'''};
\draw (.05,-.25) .. controls (-.15,.15) and (.35,.12) .. (1,.15) -- ('''+str(round(width-.3,2))+r''',.15) .. controls ('''+str(width)+r''',.16) and ('''+str(width)+r''',.28) .. ('''+str(round(width-.05,2))+r''',.42);
\end{tikzpicture}'''
hand=r'\inserted{\handwritten{$\mathrm{Hom}(X,Y)$ de dim. finie sur $k$,}}'
r.edit(hand,leader(hand,6.6))
ax=r'\inserted{(axiome de rigidité)}';r.edit(ax,leader(ax,4.4))
ab=r'\inserted{abélienne}';r.edit(ab,leader(ab,2.0))
co=r'\inserted{i.e. cohérents}';r.edit(co,leader(co,3.2))
ch('raised round glyph in H',r'H^{\unsure{0|o}}',r'H^0',r'H^{\unsure{0|o}}','The raised character is a small unbroken oval; its strokes do not distinguish digit zero from lowercase o. C alternatives retained.','H0','misread symbol or index','medium',False,True,False,True)
ch('inserted category C',r'\inserted{C}','omitted',r'\inserted{C}','A plain typewritten C stands above the gap between catégorie and des.','Cinsert','omission','high',False,True,False,True)
ch('first typed tensor',r'\otimes',r'\otimes',r'\unsure{\otimes|\Omega}','The oval and crossed diagonals end on a divided flat foot. The Omega-like appearance remains an alternative; all four occurrences were individually enlarged.','tensor1; tensor2; tensor3; tensor4','misread symbol or index','medium',True,True,False,True)
ch('first hand phi',r'\unsure{\varphi|\phi}',r'\varphi',phi,'A closed oval is crossed by an oblique stem extending above and below. Phi is favored over varphi, without suppressing the latter alternative. The second instance has the same construction.','phi1; phi2psi2','misread symbol or index','medium',True,True,False,True)
ch('first hand psi',r'\unsure{\psi|\varphi|\mu}',r'\psi',r'\unsure{\psi|\varphi|\mu}','The serifed cup with right foot is crossed by a long oblique hand stroke. The overlapping construction does not settle C three alternatives.','psi1; phi2psi2','misread symbol or index','medium',False,True,False,True)
ch('canceled Hom before unit',r'\deleted{Hom}','omitted',r'\deleted{Hom}','H, round o and m shoulders remain readable beneath the row of x cancellation strokes.','Homcancel','deletion state')
ch('hand Hom note and leader','insertion text','marginal after sentence','insertion with curved leader','The note reads Hom(X,Y) de dim. finie sur k, including its comma. Its long curved leader runs above mais l-homomorphisme, turns down at the left and up at the right. Both text and leader are reproduced.','handnote; handleader; handnoteupright; handleft; handright','drawing or diagram','high',True,True)
ch('accent above first X',r'\unsure{X|X^{\vee}}',r'\check{X}',vee,'A separate dark V-shaped mark stands above the X, crossing but not belonging to the paler insertion leader. The mark is present; its vee/nu/v identity is qualified at this first occurrence.','operand; handright','misread symbol or index','medium',True,True,False,True)
ch('relation before internal Hom',r'\simeq',r'\to',r'\simeq','The upper stroke is curved and the lower stroke horizontal. There is no arrowhead.','simeq','misread symbol or index','high',False,True,False,True)
ch('axiom insertion leader','insertion text','marginal text after sentence','insertion with curved leader','The typewritten parenthesis lies above the sentence ending. A curved leader descends to just before the period after isomorphisme and rises at its right end.','axiominsert; uniso','drawing or diagram','high',True,True)
ch('C/X overlap after Galois',r'\deleted{\unsure{X}}C',r'\underline{C}',CX,'The cell contains the open C curve together with the two serifed diagonals of X. The unlike characters occupy one cell; no separate canceled X or underline is visible.','GaloisC','deletion state','high',True,True,False,True)
ch('canceled character after doute',r'\deleted{\unsure{s|x}}','omitted',r'\deleted{i}','A small dot and upright i stem remain under the x cancellation. Neither an s curve nor a standalone live x accounts for these strokes.','doutecancel','deletion state','high',True,True)
ch('canceled character after Ils',r'\deleted{\unsure{s|x}}','omitted',r'\deleted{s}','Both reverse curves of a small s remain under the x cancellation. C uncertainty is resolved.','Ilscancel','deletion state','high',True,True)
ch('canceled Pour y rém',r'\deleted{Pour y rém}',r'\struck{\ill{}}',r'\deleted{Pour y rém}','The P stem and loop, our, separate y, r shoulder, acute accent and m shoulders can be followed beneath the cancellation row.','Pourcancel','readable ink left as \\ill{}','high',False,True,True)
ch('second remedier spelling','remédier','rémédier','rémédier','Separate acute marks stand above both e characters.','remedier','misread word','high',True,False)
for place,crop in [('C after sans que','Cmid'),('C after définir','Cdefine'),('C before n-a pas','Cpara'),('C in A prouver','Chead'),('C before est limite','Cbottom')]:
 ch(place,'C',r'\underline{C}','C','The capital has a single open curve, with no underline beneath its baseline.',''+crop,'misread symbol or index','high',False,True,False,True)
ch('gap between U and X',r'U\quad X',r'U\subset X',r'U\quad X','The enlarged gap contains only paper texture. No subset sign or other relation is visible.','UXgap','text not on the page','high',False,True,False,True)
ch('initial F of Faisceaux','F','F',F,'The capital F contour coexists with an extra leftward middle bar and hook-like strokes. A lowercase f overlapping F is favored but the heavily impressed single F remains possible.','Faisceaux; Ffine','misread word','medium',True,True)
ch('middle of relativement','relativement','relativement',r'relative\rlap{e}ment','At the m cell, a closed e bowl and horizontal bar overlap the m stems and shoulders. Both unlike forms are retained.','relativement; relativefine','misread word','high',True,True)
ch('U after membership',r'\unsure{\mathbb{U}|U}','U',U,'The U lower bowl and upright sides coexist with two inward upper diagonals forming M. These are unlike-letter strokes, not merely a doubled U.','xU; Ufine','misread symbol or index','high',True,True,False,True)
ch('acute in axiome','áxiome','axiome','áxiome','A short rising acute stroke is visible above a.','axiome','misread word')
ch('initial sa in last satisfait','satisfait','satisfait',r'\rlap{s}\kern.35em atisfait','The s reverse curves and a bowl/right foot collide in a partly shared cell. The transcription retains both letters and their partial overlap without inferring typing order.','satisfait2; safine','other','high',True,True)
ch('abelienne insertion leader','insertion only','insertion only','insertion with curved leader','A blue curved stroke runs beneath the inserted word, descends between catégorie and avec, and curls up at its right end.','abelienne','drawing or diagram','high',True,True)
ch('canceled lower character at tensor',r'\deleted{\unsure{k|x}}','omitted',r'\deleted{\unsure{k|x}}','The dark lower character is crossed and largely filled. Short uprights and a right diagonal survive, but k versus x remains unsettled.','tensor3','deletion state','low',False,True,False,True)
ch('lower hand phi',r'\varphi',r'\varphi',r'\phi','The same closed oval and long oblique stem as the first phi are visible here. The alternative is marked at the first recurrence on this page.','phi2psi2','misread symbol or index','medium',True,True,False,True)
ch('raised sign in A prouver',r'\unsure{\vee|\nu|v}',r'\vee',r'\vee','Two straight arms meet at a low point. The same sign family is qualified above the first X; this occurrence and the one after conoyaux were separately enlarged.','unitvee; vee2','misread symbol or index','medium',True,False,False,True)
ch('period after rigidité','. and Alors a) k=End','comma, inserted k=End and repeated End','. and Alors a) inserted k=End','There is a round period after rigidité. Only k= is inserted above the following line, directly over the one occurrence of End; H duplicates End and relocates the insertion.','rigiditeperiod; kinsert; Endunit','insertion or placement','high',False,True,False,True)
ch('overprinted unit in End',r'\unsure{\mathbb{1}|1}',r'\underline{1}',one,'Two upright forms, a lower cross-stroke and a rightward horizontal bar occupy the unit cell. A 4/1 overlap is provisionally favored; doubled 1 and plain 1 remain alternatives. No separate underline is present.','Endunit; Endfine','misread symbol or index','low',True,True,False,True)
ch('canceled word before corps',r'\unsure{orops|orps|corps}','groupes','orops','Five underlying letter positions show a round o, r shoulder, another o, descending p and s curves under the x strikes. There is no six-letter groupes.','orops; oropsfine','misread word','high',True,True)
ch('first argument of lower Hom',r'\unsure{\mathbb{X}|X}','X',X,'The X diagonals coexist with an open C curve, upper right terminal and lower right terminal. The glyph is an unlike C/X overlap, not a second displaced X.','Hom2; Xfine','misread symbol or index','high',True,True,False,True)
ch('i.e. coherents placement and leader','insertion before sur k','marginal after sur k','insertion before sur k with curved leader','The words are above the gap after finie. Their blue leader turns down before sur and up after cohérents, so the insertion precedes sur k.','coherentinsert','drawing or diagram','high',True,True)
ch('parenthesis overlapping sur','sur','sur',r'\rlap{(}sur','A tall black opening-parenthesis curve extends above and below the small s. It is distinct from the blue insertion leader.','surfine; coherentinsert','omission','high',True,True)
ch('closing punctuation of NB',')',')',paren,'A dark round mark with a short descending tail overlaps the lower end of the closing parenthesis. A comma/parenthesis overlap is favored; a single unusually heavy parenthesis remains possible.','quotes; quotesend','misread symbol or index','medium',True,True)
ch('quotation marks around coherent',"``cohérent''",'« cohérent »',"``cohérent''",'Both opening and closing pairs are short raised vertical strokes; there are no angled guillemets.','quotes','other')
ch('canceled C in lower line','C',r'\underline{C}','C','The surviving capital C curve is crossed by the same x cancellation row as its neighbors, without a separate underline.','cancelc1; cancelc2','misread symbol or index')
ch('clipped end of canceled line',r'\unsure{engend}','engendrement fini',r'\unsure{engend}','The visible sequence ends at engen and the left edge of another clipped character. The d remains qualified; no ink of rement fini survives inside the image.','cancelc2; clippedend','text not on the page','low',False,True)
ch('hand-repaired second e in general','général','général',gen,'The second accented letter has blue curved hand strokes and a raised accent over faint vertical remnants. The visible é is retained, with a possible underlying u left as an alternative.','general; generalfine','misread word','medium',True,True)
for a,b,c,d,e in [
 ('H raised round glyph','0','o','medium','Small unbroken oval.'),
 ('first typed tensor',r'\otimes',r'\Omega','medium','Oval crossing and divided flat foot; four instances inspected.'),
 ('first hand phi',r'\phi',r'\varphi','medium','Closed oval crossed by long oblique stem; second instance agrees.'),
 ('first hand psi',r'\psi',r'\varphi; \mu','medium','Overlapping serifed cup and diagonal construction.'),
 ('accent above first X',r'\vee',r'\nu; v','medium','Distinct V-shaped ink above X crossing insertion leader.'),
 ('initial Faisceaux',r'\rlap{f}F','F','medium','Extra leftward middle bar/hook-like strokes.'),
 ('canceled tensor subscript','k','x','low','Heavily filled cancellation obscures original character.'),
 ('End unit',r'\rlap{\(4\)}1',r'\mathbb{1}; 1','low','Two upright forms and rightward mid-bar.'),
 ('NB closing parenthesis',r'\rlap{,})',')','medium','Possible comma bulb and tail on lower parenthesis.'),
 ('clipped canceled word','engend','','low','Final d largely outside the surviving right edge.'),
 ('general second e','hand é','u overlapped by é','medium','Blue repair and faint underlying vertical remnants.')]:r.doubt(a,b,c,d,e)
r.notation('typed tensor',r'first \unsure{\otimes|\Omega}, later \otimes','10:133 category data; X tensor Y; A prouver; after conoyaux','uncertain')
r.notation('hand phi and psi',r'\phi|\varphi; \psi|\varphi|\mu','10:133 first category data and A prouver data','uncertain')
r.notation('hand dual mark',r'\vee|\nu|v','10:133 above X in homomorphism; raised after unit in A prouver; after conoyaux','uncertain')
r.notation('typed plain capitals','X,C,U,Y,H,O','10:133 top X; H formula X/O_X; inserted C; X after sur; first formula X,Y and Hom arguments; points X; C after que; U blank X; C after définir; sur U; U!=X; U=X; C n-a pas; C A prouver; canceled C; C est limite; lower Hom Y')
r.notation('unlike math overprints',r'\rlap{\(X\)}C; \rlap{\(M\)}U; \rlap{\(C\)}X','10:133 after Galois; x membership U; lower Hom first argument')
r.notation('unit glyph',one,'10:133 End argument; plain 1 in both data lists separately inspected','uncertain')
r.notation('lowercase x and k','x, k, k(x), k_i','10:133 initial corps k; top equality k; handnote k; point x and k(x); relatively k; membership x; extension k; inserted k=; lower sur k; NB sur k and k est; final k_i')
r.notation('relation signs',r'\simeq; \in; \not=; =','10:133 homomorphism; point x in U; U not equal X; U equal X; top H equality; inserted k=')
r.notation('internal Hom underline',r'\underline{\mathrm{Hom}}','10:133 list of internal objects and right side of homomorphism')
r.r['abbreviations']=[dict(abbreviation=a,expansion=b,attestations='10:133 '+c) for a,b,c in [('dim.','dimension','hand insertion'),('loc.','localement','Modules loc. libres'),('i.e.','id est','lower insertion'),('NB','nota bene','lower parenthesis')]]
r.r['inventory_overrides']={
 '133-08':dict(first_words_or_objects='hand simeq and distinct raised vee/nu/v above X'),
 '133-10':dict(kind='text',first_words_or_objects='unlike X/C overlap after Galois, no separately canceled X'),
 '133-11':dict(first_words_or_objects='canceled i after doute'),
 '133-12':dict(first_words_or_objects='canceled s after Ils'),
 '133-20':dict(first_words_or_objects='a) inserted k=End with uncertain overprinted 4/1, doubled1 or plain1'),
 '133-22':dict(first_words_or_objects='canceled orops'),
 '133-23':dict(first_words_or_objects='b) Hom with C/X overlap in first argument'),
 '133-26':dict(first_words_or_objects='Toute sous-catégorie de C stable par tout et à clipped engend')}
extras=[('curved leader below Hom note','drawing','upper interline','his hand'),('curved leader below axiome de rigidité','drawing','upper sentence end','his hand'),('uncertain f/F overlap in Faisceaux','text','middle','typewriter'),('e/m overlap in relativement','text','middle','typewriter'),('M/U overlap after membership','text','middle','typewriter'),('partial s/a overlap in satisfait','text','end of first paragraph','typewriter'),('curved leader below abélienne','drawing','above A prouver data','his hand'),('curved leader below i.e. cohérents','drawing','lower paragraph','his hand'),('opening parenthesis overlapping s of sur','text','lower paragraph after finie','typewriter'),('possible comma at closing parenthesis','text','NB end','typewriter'),('hand repair of second é in général','text','lower paragraph','his hand')]
for i,(s,k,p,h) in enumerate(extras,1):r.r['inventory_extra'].append(dict(scan='10:133',sheet_kind='typescript',hand=h,element=f'133-R{i:03d}',kind=k,position=p,first_words_or_objects=s,transcribed='yes'))
r.r['crops']=sum([json.loads(Path('work/'+p).read_text()) for p in ['crops133.json','crops133_extra.json']],[])
r.r['inspection_note']='Root alone viewed the whole page and both halves before opening C/H, all14 C doubts and all29 inventory rows. All84 crop recipes were actually viewed; Cpara/k4/satisfait2 from an initially truncated output were re-viewed. Hand note was rotated -1 degree and both fine halves read. Every mathematical sign, unlike-letter collision, insertion and cancellation was enlarged. Both halves were reread line by line before finalization. All14 C doubts received explicit decisions. The archival132 remains solely an archive comment. No OCR, parallel transcription, context access or mathematical checking occurred.'
r.save('work/record133.json')
