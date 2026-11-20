from pathlib import Path
import sys,json
sys.path.insert(0,str(Path('SP02_CW_10+12/scripts').resolve()))
from root_record import Record
r=Record('B10-10',10,131);ch=r.change
label=r'\rlap{\(x\)}-'
firstlabel=r'\unsure{'+label+r'|*}'
au=r'a\unsure{\rlap{y}u|u|y}'
par=r'pa\unsure{\rlap{f}r|r|f}'
ext=r'exten\unsure{\rlap{i}s\rlap{o}i\rlap{n}on|siion|sion}'
conf=r'conf\rlap{i}ormité'
quon=r"qu'\rlap{i}o\rlap{l}n"
alg=r'alg\unsure{\rlap{g}é|é}briquement'
finalsig=r'\unsure{\rlap{\(\varphi\)}\uparrow\psi|(\uparrow\psi|\varphi\psi|\psi\varphi}'
r.edit(r"d'un $\otimes$",r"d'un $\unsure{\otimes|\Omega}$")
r.edit(r'\unsure{\varphi|\phi}',r'\unsure{\varphi|\phi|\psi}')
r.edit(r'\deleted{W}',r'\deleted{\unsure{M|W}}')
r.edit(r'$(*)$ \deleted{avec $(**)$}',r'$('+firstlabel+r')$ \deleted{, avec $('+label+label+r')$}')
r.edit(r'\unsure{au|ay}',au)
r.edit('commutatif (par exemple','commutatif ('+par+' exemple')
r.edit(r'\deleted{$k^{\handwritten{*}}$) et $k$}',r'\deleted{$k^{\handwritten{*}}$), et $k$}')
r.edit(r'\unsure{il ne se tue alors dans}','il ne se tue alors dans')
r.edit(r'\unsure{extension|extensiion}',ext)
r.edit('si $k$ est algébriquement','si $k$ est '+alg)
r.edit(r'\unsure{confôrmité|conformité}',conf)
r.edit(r'\unsure{étudier}','étudier')
r.edit(r'\unsure{+|\&}',r'\unsure{\&|+}')
r.edit(r'\unsure{aux graduations|des graduations}','aux graduations')
r.edit(r"\unsure{qu'on|qu'ôn}",quon)
r.edit(r'\unsure{gradués}','gradués')
r.edit(r'$(\unsure{\uparrow\psi|\varphi\psi|\psi\varphi}$ ??)',r'$'+finalsig+'$ ??')
# Preserve the irregular enclosing outline and four handwritten lines.
C=Path('source/SP02_CW_10+12_witnesses/codex/B10-10/pages/B10-10_10_scan131.tex').read_text()
start=C.index(r'\margin{\figure{');end=C.index(r'\end{tikzpicture}}}',start)+len(r'\end{tikzpicture}}}')
old=C[start:end]
for e in r.r['edits']:old=old.replace(e['old'],e['new'])
new=r'''\margin{\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\node[anchor=north west,align=left,inner sep=2pt] at (.12,-.05) {\handwritten{Exemple de foncteurs}\\\handwritten{fibres gradués mod 2}\\\handwritten{non loc. isom. aux}\\\handwritten{\unsure{vrais|sans} $'''+finalsig+r'''$ ??}};
\draw (0,0) .. controls (1.3,.1) and (3.6,.02) .. (4.5,.12) .. controls (4.9,.12) and (5,-.4) .. (4.8,-.65) -- (4.05,-.9) .. controls (3.9,-1) and (4.2,-1.5) .. (4.05,-1.7) .. controls (2.6,-2.05) and (.8,-1.95) .. (.05,-2.05) .. controls (-.2,-2.15) and (-.15,-.4) .. (0,0);
\draw (.05,-2.05)--(.1,-2.2);
\end{tikzpicture}}}'''
r.edit(old,new)
ch('typed tensor sign',r'\otimes',r'\otimes',r'\unsure{\otimes|\Omega}','The rounded upper contour, crossing diagonals and flat lower foot form the typed tensor-like construction; an Omega-like reading remains possible.','tensor','misread symbol or index','medium',True,True,False,True)
ch('top canceled symbol group',r'\unsure{k\handwritten\varphi|k\handwritten\psi}',r'\struck\varphi',r'\deleted{\unsure{k\handwritten{\varphi}|k\handwritten{\psi}}}','The first typed k-like cell has a separate upright and diagonals, followed by a densely overlaid hand loop/fork. Cancellation crosses the group. C alternatives are retained because the hand sign is not separable securely.','topcancel','misread symbol or index','low',False,True,False,True)
ch('first live looped symbol',r'\unsure{\varphi|\phi}',r'\varphi',r'\unsure{\varphi|\phi|\psi}','The blue hand correction has a left cup, a closed upper-right loop and long oblique descending stem. The looped phi form is favored, but phi and a forked psi reading remain possible.','phivee','misread symbol or index','medium',True,True,False,True)
ch('raised v-shaped sign',r'\unsure{\vee|\nu|v}',r'\vee',r'\unsure{\vee|\nu|v}','Two sloping arms meet at a low point, with a short return at the upper right. The raised placement is clear; comparisons with the typed v do not securely settle vee/nu/v or justify replacing the hand attribution. C alternatives retained.','phivee; vclose; vcmp','misread symbol or index','medium',False,True,False,True)
ch('live sign after canceled avec',r'\handwritten{\unsure{\psi|\varphi|\mu}}',r'\struck\psi',r'\handwritten{\unsure{\psi|\varphi|\mu}}','The wavy cancellation passes through avec and stops before the separate hand sign. Its blue stem descends below the looped body and extends to an upper-right arm; it remains live. C alternatives retained.','avecpsi','deletion state','medium',False,True,False,True)
ch('short dash','-','em dash','-','A short single typewriter horizontal stroke stands before On prend.','dash','other')
ch('corrected indexed system letter',r'\deleted W\handwritten L_g','M_g',r'\deleted{\unsure{M|W}}\handwritten L_g','The hand L is distinct over the typed capital. Two upper serifed stems and an inward descending middle favor M; W remains possible because the hand stroke obscures the lower contours.','Lg; Lgclose; Meme','deletion state','medium',True,True,False,True)
ch('three typed label glyphs','asterisks','asterisks',r'first '+firstlabel+r'; two canceled recurrences '+label,'Each label glyph has x-shaped serifed diagonals with a horizontal midline. The first is qualified; the two in the canceled parenthesized label use the same first reading.','labels','misread symbol or index','medium',True,True,False,True)
ch('canceled comma after first label','omitted',r'\ill{}',r'\deleted{,}','A curved comma tail descends beneath the first x cancellation after the live right parenthesis.','labelcomma; labels','omission','high',True,True)
ch('canceled avec between labels','avec',r'\ill{}','avec','The a bowl, v diagonals, e bowl/bar and c curve survive beneath the x strikes.','labels',r'readable ink left as \ill{}','high',False,True,True)
ch('second parenthesized label state','canceled','live','canceled','The parenthesized pair is crossed through; it belongs to the same canceled continuation as avec.','labels','deletion state','high',False,True,False,True)
ch('au mixed cell',r'\unsure{au|ay}','au',au,'The second cell contains the u cup and right foot together with a y diagonal and curved descending tail. The raw overlap is favored, with single-letter alternatives retained.','au','misread word','medium',True,True)
ch('one-to-one correspondence dash','1-1','1--1','1-1','The central horizontal is a short single typewriter hyphen.','range','other')
ch('par example final cell','par','par',par,'The final r-shaped cell has an additional tall f-like upper loop and a crossing horizontal bar. No correction order is inferred.','par','misread word','medium',True,True)
ch('canceled characteristic fragment',r'k*) et k',r'\ill{}',r'k*), et k','The first k, hand raised star, closing parenthesis, comma, e/t and last k can be distinguished under the x line. The comma is visible below the cancellation and was omitted by C.','cancelk; cancelcomma',r'readable ink left as \ill{}','high',True,True,True,True)
ch('canceled nonvanishing phrase',r'\unsure{il ne se tue alors dans}',r'\ill{}','il ne se tue alors dans','The i dot, l/t/d ascenders and each n/e/s/u/a/o/r contour remain legible under the x strikes. C doubt resolved.','cancelphrase',r'readable ink left as \ill{}','high',True,True,True)
ch('extension final cells',r'\unsure{extension|extensiion}','extension',ext,'After exten, the first cell combines s with dotted i, the second combines dotted i with o, and the third combines o with n; a final n follows. The layered reading is retained first, with the simpler C candidates as alternatives.','extension; extcells','misread word','medium',True,True)
ch('second algébriquement é cell','é','é',alg,'A lower g-shaped loop descends beneath the é cell, and a rightward g ear coexists with the e bowl/bar and acute accent. Plain é remains a less favored alternative.','algeb; algebclose','misread word','medium',True,True)
ch('conformité second o',r'\unsure{confôrmité|conformité}','conformité',conf,'A straight i stem with a separate dot overlaps the o circle. The raised mark is a dot, not a circumflex; C doubt resolved to the raw unlike-letter overlap.','conformite','misread word','high',True,True)
ch('quon two overprints',r"\unsure{qu'on|qu'ôn}","qu'on",quon,'The o has an internal i stem and detached dot; the n has an extra tall l stem and upper-left serif. Both overlapping forms are retained, without inferring the sequence of typing. C doubt resolved.','quon','misread word','high',True,True)
ch('extra la before contrainte','no second la','la contrainte','contrainte','After the canceled condition de, the following live line begins directly with contrainte.','condition; contrainte','text not on the page')
ch('first marginal opening',r'\unsure{étudier}','étudier','étudier','Rotated upright, the initial acute, crossed t, u, looped d, dotted i and final e/r group are readable. C doubt resolved.','etudiant; margin1full','misread word','high',True,False)
ch('first marginal comm abbreviation','de comm.',r'\ill{}','de comm.','The d/e join and short c/o/m/m group ending with a detached period are visible in the rotated note.','margin1full',r'readable ink left as \ill{}','high',False,True,True)
ch('first marginal joining sign',r'\unsure{+|\&}',r'\ill{}',r'\unsure{\&|+}','The sign has a long oblique left arm, curled upper-right return and descending stem. The ampersand-like reading is favored over a plain plus, but the compressed construction remains uncertain.','marginjoin; marginassoc',r'readable ink left as \ill{}','low',True,True,True)
ch('first marginal association abbreviation',r'\unsure{associon|assoc.}','associées',r'\unsure{associon|assoc.}','The compressed opening a/s/s-like strokes are followed by o/c and a dotted narrow ending. No secure é/e/s sequence supports associées. C alternatives retained.','marginassoc; margin1full','misread word','low',False,True)
ch('first marginal graduations phrase',r'\unsure{aux graduations|des graduations}',r'\ill{}','aux graduations','The initial a loop, u and crossed x precede a continuous g/r/a/d/u/a/t/i/o/n/s group. Mod2 follows on the next hand line. C doubt resolved.','margingrad; margin1full',r'readable ink left as \ill{}','medium',True,True,True)
ch('second marginal gradués',r'\unsure{gradués}',r'\uncertain{gradués}','gradués','The g descender, r join, a loop, d ascender, u, acute é and final s are readable after rotation. C and H doubts resolved.','margin2full','misread word','high',True,True,True)
ch('second marginal final word',r'\unsure{vrais|sans}',r'\ill{}',r'\unsure{vrais|sans}','The opening pointed v-like stroke and following short joins favor vrais; compressed middle strokes still permit sans. C alternatives retained.','bottomword; margin2full',r'readable ink left as \ill{}','low',False,True,True)
ch('second marginal final symbol construction',r'(\unsure{\uparrow\psi|\varphi\psi|\psi\varphi}',r'\ill{}',finalsig,'The first gray loop has its own vertical stem, while a darker upward arrowhead and stem overlap it; a separate forked psi-like sign follows. Raw phi/arrow overlap is favored, but a parenthesis plus arrow and the earlier two-letter candidates remain alternatives.','bottomsigns; margin2full',r'readable ink left as \ill{}','low',True,True,True,True)
ch('second marginal final closing parenthesis','closing parenthesis after ??','no closing parenthesis','no closing parenthesis','Two hooked question marks with lower points end the line. No additional closing parenthesis follows them.','bottomsigns; margin2full','text not on the page','high',True,False)
ch('second marginal enclosing outline','rounded polygon','described as boxed','curved irregular contour with right indentation and short lower tail','The outline runs above four hand lines, bulges at the upper right, turns inward at mid-right, curves along the bottom and has a short descending tail at its lower-left join. The drawing is reproduced with those features.','marginall; margin2full','drawing or diagram','high',True,True)
# Surviving doubts, including all retained C alternatives.
for a,b,c,d,e in [
 ('typed tensor',r'\otimes',r'\Omega','medium','Crossed rounded form with flat foot.'),
 ('top canceled group',r'k\handwritten\varphi',r'k\handwritten\psi','low','Typed and hand layers are densely canceled.'),
 ('first live looped sign',r'\varphi',r'\phi; \psi','medium','Left cup, closed right loop and descending oblique stem.'),
 ('raised v-shaped sign',r'\vee',r'\nu; v','medium','Raised position clear; two-arm shape not unique.'),
 ('three live symmetry signs',r'\psi',r'\varphi; \mu','medium','First after canceled avec qualified; two later cup/diagonal signs separately enlarged and unmarked.'),
 ('typed capital replaced by L','M','W','medium','Lower contours obscured by the hand L.'),
 ('three label glyphs',label,'*','medium','First qualified, two canceled recurrences use same reading.'),
 ('au second cell',r'\rlap{y}u','u; y','medium','Cup and foot coexist with descending y tail.'),
 ('par final cell',r'\rlap{f}r','r; f','medium','Extra tall upper loop and bar over r.'),
 ('extension final cells',ext,'extensiion; extension','medium','Three visibly overlapping cells, no strike order inferred.'),
 ('second algébriquement é',r'\rlap{g}é','é','medium','Lower g loop beneath e plus acute.'),
 ('first margin joining sign',r'\&','+','low','Curled upper arm and descending stem.'),
 ('first margin abbreviation','associon','assoc.','low','Ending compressed; no expansion supplied.'),
 ('second margin final word','vrais','sans','low','Middle cursive joins remain compressed.'),
 ('second margin final symbol group',r'\rlap{\(\varphi\)}\uparrow\psi',r'(\uparrow\psi; \varphi\psi; \psi\varphi','low','Gray loop/stem overlaps black arrow-like construction; followed by forked glyph.')]:r.doubt(a,b,c,d,e)
r.notation('typed tensor sign',r'\unsure{\otimes|\Omega}','10:131 opening example','uncertain')
r.notation('first looped hand sign',r'\unsure{\varphi|\phi|\psi}','10:131 after1','uncertain')
r.notation('three live symmetry signs',r'first \unsure{\psi|\varphi|\mu}; later psi','10:131 after canceled avec; second paragraph; third paragraph','uncertain')
r.notation('raised hand v shape',r'{}^{\handwritten{\unsure{\vee|\nu|v}}}','10:131 after first looped sign','uncertain')
r.notation('three typed label constructions',firstlabel+'; later '+label,'10:131 live single and canceled pair','uncertain')
r.notation('five handwritten exponent stars',r'k^{\handwritten{*}}','10:131 first extension; H2 formula; canceled characteristic fragment; second extension; divisible clause')
r.notation('three typed cohomology exponents',r'H^2','10:131 correspondence; first nonzero H; second nonzero H')
r.notation('indexed correction',r'\deleted{\unsure{M|W}}\handwritten L_g','10:131 system letter','uncertain')
r.notation('final marginal composite',finalsig,'10:131 boxed note ending','uncertain')
r.notation('ordinary typed capitals',r"E,F,F',G,H,U",'10:131 heading E; inserted F-prime; both F and both further F-primes; all G/H; final U; each enlarged separately')
r.r['abbreviations']=[dict(abbreviation=a,expansion=b,attestations='10:131 '+c) for a,b,c in [('sss','si et seulement si','first paragraph'),('car.','caractéristique','first paragraph'),('alg.','algébriquement','first paragraph'),('loc.','localement','third paragraph and boxed note'),('isom.','isomorphes / isomorphe','third paragraph and boxed note'),('comm.','commutativité','first margin'),('associon / assoc.','association / associativité (uncertain)','first margin'),('mod','modulo','both margins')]]
r.r['inventory_overrides']={
 '131-03':dict(first_words_or_objects=r'phi/phi/psi; raised vee/nu/v; live psi/phi/mu'),
 '131-05':dict(first_words_or_objects=r'\unsure{M|W}'),
 '131-06':dict(position='line4 over typed M/W'),
 '131-07':dict(first_words_or_objects='comma, avec and parenthesized two constructed marks'),
 '131-09':dict(first_words_or_objects='k-star), et k'),
 '131-10':dict(first_words_or_objects='il ne se tue alors dans'),
 '131-16':dict(first_words_or_objects=r'étudier les contraintes de comm. uncertain &/+ uncertain associon/assoc. aux graduations mod2.'),
 '131-17':dict(first_words_or_objects='Exemple de foncteurs fibres gradués mod2 non loc. isom. aux uncertain vrais/sans; overlapping phi/arrow then psi; ??'),
 '131-18':dict(first_words_or_objects='curved irregular outline, right indentation and short lower-left tail')}
extras=[('u/y overlap in au','text','first paragraph'),('r/f overlap in par','text','first paragraph'),('three overlapping final cells of extension','text','end of first paragraph'),('g/é overlap in algébriquement','text','second paragraph'),('i/o overlap in conformité','text','second paragraph'),('i/o and l/n overlaps in quon','text','third paragraph')]
for i,(s,k,p) in enumerate(extras,1):r.r['inventory_extra'].append(dict(scan='10:131',sheet_kind='typescript',hand='typewriter',element=f'131-R{i:03d}',kind=k,position=p,first_words_or_objects=s,transcribed='yes'))
r.r['crops']=json.loads(Path('work/crops131.json').read_text())
r.r['inspection_note']='Root alone viewed whole image then both halves, C/H, all16 C doubt loci and all23 C inventory items. All64 enlarged crop recipes were actually viewed; both marginal notes were rotated upright at several angles with finer detail crops. Every mathematical sign, disputed/doubtful locus, cancellation and marginal item was enlarged, and all agreed prose was checked line by line with both halves reread. Right-edge foncteurs and donné comma remain legible in dedicated crops. All16 C doubts have explicit decisions. Archive130 remains only an archive comment. No OCR, parallel transcription, context access or mathematical checking occurred.'
r.save('work/record131.json')
