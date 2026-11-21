from pathlib import Path
import json,os,re,csv
ROOT=Path('/workspace/scratch/b12af914b284')
OUT=ROOT/'edition/reader_returns'
manifest=json.loads((ROOT/'edition/scripts/150_scan073_crop_index.json').read_text())
crops={x['file'].split('150_scan073_')[1].removesuffix('.png'):x for x in manifest['crops']}

def atomic(path,text):
 t=path.with_name(path.name+'.tmp');t.write_text(text);os.replace(t,path)

tex=r'''\scanpage{73}
\mspage{32}
14. \uline{Description heuristique des} $\Sigma_i,\Sigma_{ij}$.
(Peut se préciser considérablement \unsure{dans|ds} un contexte de topologie modérée).
Pour construire $\Sigma_i$, on prend un voisinage tubulaire
\inserted{``standart'' $T_{<i}$} \unsure{\deleted{fermé}|fermé} de
% The insertion leader curves down before the crowded word; both its reading and strike state remain uncertain.
% The dotted left member has Sigma-like top/bottom bars and X-like crossing diagonals. Their temporal order is not established.
$\unsure{\dot X_i|\dot\Sigma_i}=\displaystyle\bigcup_{k<i}X_i$, et on prend
\[
(42)\qquad\Sigma_i=X_i\setminus X_i\cap\mathring T_{<i}
\]
\[
\mathring T_{<i}\overset{\mathrm{déf}}{=}T_{<i}\setminus\dot T_{<i}.
\]
% Oblique note in the left margin, alongside (42) and the following definition.
\margin{\uline{NB} On peut prendre $T_{<i}=\bigcup_{k<i}T_k$,
où $T_k$ est un vois. tub. standart des $X_k$}
(\uline{NB} Il aurait suffit ici de prendre le voisinage tubulaire
standart dans $X_i$ lui $=$, et de prendre donc
$\Sigma_i=X_i\setminus\mathring T_{<i}$)

Pour construire $\Sigma_{ij}$, on prend un voisinage tubulaire
$T'_{ij}$ de $\Sigma_i$ dans
$X_j\setminus\unsure{X_j}\cap\mathring T_{\unsure{<i0|<i}}=X'_i$
% The second X is overdrawn. After the dotted i a separate small closed oval stands a little above its lower hook; its role/degree is not settled.
(NB cette fois-ci il faut \deleted{\unsure{prendre}} d'abord prendre
$T_{<i}$ vois. tub. standart \uline{\unsure{dans|ds}} $X$, ou sinon, dans $X_j$).
On prend $T'_{ij}$ ``suffisamment petit'' p.r. au choix de $T_{<i}$.
Puis on prend $\dot T'_{ij}$\unsure{\deleted{s}|s}, et dans $\dot T'_{ij}$
% The small s-like remnant has a dense lower diagonal; its deletion state is uncertain.
la trace de $\displaystyle\bigcup_{\unsure{i\leq k<j|i<k<j}}X_{jk}$
(donc c'est vide si $j$ est un successeur de $i$), soit $S\dot T'_{ij}$
(``partie singulière'' de $T'_{ij}$.
% No closing parenthesis is visible before the point after this undotted T'_{ij}.

% Left-margin drawing opposite the singular-part paragraph. The middle stroke begins after a visible gap from the filled point.
\figure{\begin{tikzpicture}[x=.01cm,y=-.01cm,line width=.6pt,line cap=round,line join=round]
\draw (54,11) .. controls (29,6) and (9,33) .. (8,67)
 .. controls (6,99) and (20,123) .. (51,127)
 .. controls (77,131) and (97,112) .. (103,90)
 .. controls (108,68) and (99,38) .. (89,23)
 .. controls (79,12) and (67,9) .. (54,11);
\draw (91,36) .. controls (116,32) and (145,29) .. (173,30)
 .. controls (207,30) and (247,26) .. (271,27);
\draw (66,73) .. controls (96,73) and (113,69) .. (141,67)
 .. controls (187,67) and (236,56) .. (272,60);
\draw (102,101) .. controls (135,97) and (184,92) .. (220,91)
 .. controls (246,89) and (263,96) .. (274,91);
\fill (56,73) circle (1.4pt);
\end{tikzpicture}}

On prend alors un voisinage tubulaire standart
\inserted{$T(S\dot T'_{ij})$} de $S\dot T'_{ij}$ dans $\dot T'_{ij}$,
% One live de stands below the formula's curved insertion leader; no separate cancelled duplicate is isolated.
% The S is reworked; tiny detached dark traces below-left of the following T stem are retained as a local reworking observation, with no invented glyph.
qu'on peut supposer induit par la réunion \inserted{$\bigcup T_k$}
des voisinages tubulaires standart des $X_k$ ($i<k<j$)
dans $\unsure{X\mathbin{\cdot-}X_j|X-X_j}$
% Between the two X groups a detached low dot/short oblique mark precedes one horizontal dash. Its role is uncertain.
(pris ``assez petits'' p.r. aux choix déjà faits de $T_{<i}$
et \inserted{de} $T'_{ij}$).
On \deleted{\unsure{prendra}}\inserted{aura} alors
\[
(43)\qquad\Sigma_{ij}=\dot T'_{ij}\setminus\mathring T(S\dot T'_{ij})
\]
% Pale foliation at the lower left, in another hand; the final display touches the paper edge.
\margin{72}
'''
atomic(OUT/'150_scan073.tex',tex)
print(OUT/'150_scan073.tex')

# The two points after item14 and the space between the title's two objects are literal graphic readings.
tex=tex.replace(r'14. \uline{Description heuristique des} $\Sigma_i,\Sigma_{ij}$.',r'14\unsure{:|..} \uline{Description heuristique des} $\Sigma_i\ \Sigma_{ij}$.')
tex=tex.replace(r'14\unsure{:|..}',r'% Two dark points after 14 are diagonally offset; their punctuation role remains uncertain.'+'\n'+r'14\unsure{:|..}')
atomic(OUT/'150_scan073.tex',tex)

changes=[]
def ch(place,C,H,final,ac,ah,kind,cat,conf,evidence,crop,marked=False,consequence=''):
 c=crops[crop]
 changes.append(dict(id=f'073-{len(changes)+1:02d}',place=place,C=C,H=H,final=final,against_C=ac,against_H=ah,kind=kind,error_category=cat,marked_in_H=marked,confidence=conf,evidence=evidence,crop=c['file'],box=c['box'],mathematical_consequence=consequence))

ch('Heading, item14 punctuation','14.','14.',r'14\unsure{:|..}',True,True,'other','Other','low','Two discrete dark points stand after the 4, the upper one rounder and the lower one slightly oblique; they are offset diagonally. Both are retained, while colon versus two-point punctuation remains open.','p00_heading')
ch('Heading underline scope',r'\uline{Description heuristique des}',r'\emph{Description heuristique des $\Sigma_i$, $\Sigma_{ij}$}',r'\uline{Description heuristique des}',False,True,'other','Other','high','The continuous underline runs from Description through des and stops before the first Sigma. Both Sigma groups stand beyond its right end.','p00_heading')
ch('Heading between the two Sigma groups',r'\Sigma_i,\Sigma_{ij}',r'$\Sigma_i$, $\Sigma_{ij}$',r'\Sigma_i\ \Sigma_{ij}',True,True,'text not on the page','Text that is not on the page','high','The first Sigma has a dotted, hooked i. Its lower hook accounts for the apparent comma; no additional comma is isolated before the second Sigma. The terminal point after the second group is separate.','p00_heading')
ch('Opening parenthesis, after considérablement',r'\unsure{ds|dans}','dans',r'\unsure{dans|ds}',True,False,'misread word','Words','low','After the d a low short rising element and horizontal run precede the terminal s-like curve. The full-word reading is leading, but a and n cannot be separated securely enough to exclude the short form ds.','p01_dans')
ch('First interlinear insertion, quoted spelling',r"``standart''",'« standard »',r"``standart''",False,True,'abbreviation expanded or spelling modernised','Abbreviations expanded, spelling modernised','high','The inserted word ends with a tall returning t form, matching the local terminal t in the later occurrences. Its quotation marks are small high paired strokes, rather than angular chevrons.','p02_insert_ferme')
ch('Crowded word after tubulaire',r'\deleted{\unsure{fermé}}',r'\struck{\ill{}}',r'\unsure{\deleted{fermé}|fermé}',False,True,'other','Struck text','low','A low initial dark oval, a long flat run, a taller middle stroke and low terminal humps remain beside the insertion leader. The candidate fermé remains tentative; an independent cancellation cannot be separated securely from the crowded word and leader. The leading deleted candidate is recorded for collation without treating it as a settled reading.','p02_insert_ferme',True)
ch('First union, right-hand summand',r'\bigcup_{k<i}X_k',r'\bigcup_{k<i}X_k',r'\bigcup_{k<i}X_i',True,True,'misread symbol or index','Symbols and indices','high','At the summand X the subscript has a detached dot over a short curved terminal; it has no tall stem or two k arms. The bound k<i has a separate tall k, visible in the same formula.','p03_first_union',False,'The transcribed summand is literally X_i while the bound remains k<i; this records the manuscript and supplies no correction to its assertion.')
ch('End of formula42',r'\Sigma_i=X_i\setminus X_i\cap\mathring T_{<i}.',r'\Sigma_i=X_i\setminus X_i\cap\mathring T_{<i}',r'\Sigma_i=X_i\setminus X_i\cap\mathring T_{<i}',True,False,'text not on the page','Text that is not on the page','high','The final i consists of its dot and curved lower stroke. No separate point follows it before the blank space at the right.','p04_formula42')
ch('Left margin, opening words','On peut prendre','On prendra','On peut prendre',False,True,'misread word','Words','high','After On the p descends, a low eu run follows, and a terminal t stands before the next line beginning prendre. Both words are separately written.','p09_margin',True)
ch('Left margin, after T_k',r'où $T_k$ est un',r'où $T_k$ vois.\ tub.\ standard \ill{}',r'où $T_k$ est un',False,True,'omission','Omissions','medium','Between T_k and vois. there is a compact est group followed by a distinct low un with two humps.','p09_margin',True)
ch('Left margin, spelling','standart','standard','standart',False,True,'abbreviation expanded or spelling modernised','Abbreviations expanded, spelling modernised','high','The margin word ends with a high t stroke and return, matching the written terminal elsewhere on this sheet.','p09_margin',True)
ch('Left margin, final object',r'des $X_k$',r'\ill{}',r'des $X_k$',False,True,r'readable ink left as \ill{}','Readable ink left as illegible','high','The final margin line has des, with a separate s-like terminal, followed by X and a compact k subscript with a stem and two short arms.','p09_margin',True)
ch('Main NB, opening assertion','Il aurait suffit ici','Il suffirait en fait ici','Il aurait suffit ici',False,True,'misread word','Words','high','Il is followed by the separate aurait group ending in a tall t; suffit then has two tall f strokes and a compact final it. The following word is ici. No independent en fait group intervenes.','p06_nb_phrase')
ch('Main NB, spelling','standart','standard','standart',False,True,'abbreviation expanded or spelling modernised','Abbreviations expanded, spelling modernised','high','The last letter has a tall angled t stem and crossing/return. The same spelling is kept at this occurrence.','p07_nb_standart')
ch('Main NB, after lui',r'lui $\unsure{\overline{\mathrm m}}$','lui-même',r'lui $=$',True,True,'abbreviation expanded or spelling modernised','Abbreviations expanded, spelling modernised','high','Two separate nearly horizontal strokes stand after lui; there are no written m humps or spelled même. The manuscript word abbreviation is retained as an equals sign.','p08_lui')
ch('Main NB, punctuation before closing parenthesis',r'$\Sigma_i=X_i\setminus\mathring T_{<i}$)',r'$\Sigma_i=X_i\setminus\mathring T_{<i}$.)',r'$\Sigma_i=X_i\setminus\mathring T_{<i}$)',False,True,'text not on the page','Text that is not on the page','high','The final dotted i is followed by the large closing parenthesis; no extra point is visible between them.','p08_lui')
ch('Ambient expression for T prime, crowded middle',r'X_j\setminus X_j\cap',r'$X_j$ \ill{}',r'X_j\setminus\unsure{X_j}\cap',False,True,r'readable ink left as \ill{}','Readable ink left as illegible','medium','After the first X_j a heavy descending oblique is visible, followed by crossed X-like strokes with a j hook and a separate cap-shaped arch. The second X is overdrawn, so its local certainty remains qualified.','p10_ambient',True,'The manuscript expression contains the second X_j and the following cap before the ringed T; no ambient-space identity has been checked.')
ch('Ambient expression, subscript of ringed T',r'\unsure{\mathring T_{<i}|\mathring T_{<i0}}',r'\mathring T_{<i}',r'\mathring T_{\unsure{<i0|<i}}',True,True,'misread symbol or index','Symbols and indices','low','After the less-than sign and dotted i there is a separate closed small oval, slightly higher than the i hook. Its presence is clear but its role and exact degree are open, hence <i0 is leading with <i retained.','p10_ambient',True,'A closed oval after the i is preserved in the leading reading rather than removed to obtain the witness formula.')
ch('Second parenthetical NB, emphasis','NB',r'\emph{NB}','NB',False,True,'other','Other','high','The opening parenthesis and NB are present. No independent horizontal underline lies beneath the two letters; the left low curve belongs to the parenthesis.','p30_second_nb')
ch('Second NB, spelling','standart','standard','standart',False,True,'abbreviation expanded or spelling modernised','Abbreviations expanded, spelling modernised','high','The word has a final t-shaped upright and return, retained as standart.','p12_standart_ds')
ch('Second NB, underlined word before X',r'\uline{ds}',r'\emph{dans}',r'\uline{\unsure{dans|ds}}',True,False,'misread word','Words','low','A separate underline runs beneath the compact d-plus-low-run-plus-s group. The inner low strokes favour dans, but remain too compressed to exclude ds.','p12_standart_ds')
ch('Second NB, word before X_j',r'ou sinon, ds $X_j$',r'ou sinon, dans $X_j$',r'ou sinon, dans $X_j$',True,False,'misread word','Words','high','After the looped d a small low a and a short n rise are distinguishable before the terminal s curve. This occurrence supports the full dans.','p13_ds')
ch('Quotation around suffisamment petit',r"``suffisamment petit''",'« suffisamment petit »',r"``suffisamment petit''",False,True,'other','Other','high','Each high quotation group consists of a compact partly joined pair of strokes. The close group stands after the tall final t of petit; no separate final s is visible.','p28_quoted_petit')
ch('After first dotted T prime in Puis on prend',r'\deleted{\unsure{s}}',r"Puis on prend $\dot T'_{ij}$,",r'\unsure{\deleted{s}|s}',False,True,'omission','Omissions','low','Between the ij group and the following comma there is a small s-shaped remnant with an open upper curl and heavy lower oblique. Its cancellation state cannot be isolated securely; both states remain open.','p14_dot_cancel')
ch('Before the second union','la trace de','la trace des','la trace de',False,True,'misread word','Words','high','The de group ends with its own compact return. There is no separate following s comparable to the clearly separated s in des on the lower line.','p15_union')
ch('Second union, first inequality',r'\unsure{i<k<j|i\leq k<j}','i<k<j',r'\unsure{i\leq k<j|i<k<j}',True,True,'misread symbol or index','Symbols and indices','low','The first left-angle has a dense lower stroke extending towards its right endpoint beneath the principal arm. This favours a less-or-equal reading, while overworking prevents excluding a retraced less-than. The final k<j is clear.','p15_union',False,'The first relation in the union bound remains explicitly open; no intended inequality is supplied from the construction.')
ch('Second union, summand',r'\unsure{X_{jk}|X_k}','X_k','X_{jk}',False,True,'misread symbol or index','Symbols and indices','high','After X there is a distinct low j stem and left-returning hook, followed by the stem and right arms of k. Both written index components are preserved.','p15_union',False,'The manuscript summand is transcribed with both j and k; no mathematical correction to the index is made.')
ch('Quotation around partie singulière',r"``partie singulière''",'« partie singulière »',r"``partie singulière''",False,True,'other','Other','high','The opening and closing quotation groups are high paired short strokes; their visible shape is retained as double quotation marks.','p17_singular')
ch('Object named in partie singulière parenthesis',r"de $T'_{ij}$.",r"de $\dot T'_{ij}$).",r"de $T'_{ij}$.",False,True,'misread symbol or index','Symbols and indices','high','The T has its top bar and separate prime, with no dot above that bar. A separate point follows the ij group.','p18_alors',False,'This parenthesis literally names the undotted T prime; the dotted object supplied by H is not substituted.')
ch('End of partie singulière parenthesis',r"$T'_{ij}$.",r"$\dot T'_{ij}$).",r"$T'_{ij}$.",False,True,'text not on the page','Text that is not on the page','high','There is a point after the subscript and then the new sentence On prend. No closing parenthesis occurs between the object and that point. This row records the parenthesis separately from the dot on T.','p18_alors')
ch('Left-margin drawing, middle stroke and endpoint geometry',r'\draw (.06,-.04) .. controls (.68,-.04) and (1.44,.12) .. (2.03,.13);',"d'où part vers la droite un trait horizontal",r'\draw (66,73) .. controls (96,73) and (113,69) .. (141,67) .. controls (187,67) and (236,56) .. (272,60); \fill (56,73) circle (1.4pt);',True,True,'drawing or diagram','Drawings and diagrams','high','The oval has one filled point and three strokes. The middle stroke starts a few pixels to the right of the point with a white gap; the outer two join the oval. Their rightward courses rise slightly and the lower endpoint has a small return. The TikZ preserves those relations.','p19_drawing')
ch('Sentence after the unclosed parenthesis','On prend alors','On prend donc','On prend alors',False,True,'misread word','Words','high','After prend the word begins with the tall joined a/l movement and ends in a low ors run, supporting alors. It has no initial d loop.','p18_alors')
ch('Lower construction, spelling','standart','standard','standart',False,True,'abbreviation expanded or spelling modernised','Abbreviations expanded, spelling modernised','high','The last letter is the same angular t form, with a high terminal stroke and return; it remains standart at this occurrence.','p20_insert_formula')
ch('Lower construction, de under the insertion leader',r"\inserted{$T(S\dot T'_{ij})$} de",r"\add{$T(S\dot T'_{ij})$} \struck{de} de",r"\inserted{$T(S\dot T'_{ij})$} de",False,True,'text not on the page','Text that is not on the page','high','Only one de group is written before S dot T. The line through the upper d ascender continues into the long curved insertion leader. No separate struck duplicate word is isolated.','p20_insert_formula')
ch('Last occurrence before des X_k, spelling','standart','standard','standart',False,True,'abbreviation expanded or spelling modernised','Abbreviations expanded, spelling modernised','high','The final high angular letter has the t form used in the earlier occurrences; the following des has its own separate terminal s.','p22_standart')
ch('Lower ambient-space expression',r'\unsure{X---X_j}',r'$X$ \ill{} $X_j$',r'\unsure{X\mathbin{\cdot-}X_j|X-X_j}',True,True,'misread symbol or index','Symbols and indices','low','After X a detached dark low point/short slanted stroke precedes one separated nearly horizontal dash, then X_j. The point and dash are represented separately in the leading reading; their role remains open. No three successive dashes are visible.','p23_final_ambient',True,'The literal marks between the objects remain explicit; no named mathematical relation is inferred from them.')
ch('Quotation around assez petits',r"``assez petits''",'« assez petits »',r"``assez petits''",False,True,'other','Other','high','The opening and closing groups are each two high short strokes. The word petits has a separate terminal s before the close marks.','p29_quoted_petits')
ch('Last parenthesis, insertion before T prime',r"et \inserted{de} $T'_{ij}$",r"et $T'_{ij}$",r"et \inserted{de} $T'_{ij}$",False,True,'omission','Omissions','high','A small de is written above the line. Its curved leader descends into the gap after et and before T prime; the two parts of the d and e are visible.','p24_insert_de')
ch('Lower-left foliation',r'\mspage{72}','',r'\margin{72}',False,True,'omission','Omissions','high','The pale 7 and 2 are clearly written at the lower-left paper edge in another hand. The changed wrapper records hand attribution, with the written number unchanged from C.','p27_folio')

# Marks: open alternatives are always undecided.
decisions=[]
def dec(mid,decision,reading,evidence,crop,conf):
 c=crops[crop];decisions.append(dict(id=mid,decision=decision,reading=reading,evidence=evidence,crop=c['file'],box=c['box'],confidence=conf))
dec('M0637','undecided',r'\unsure{dans|ds}','The d and terminal s are clear; the intervening low rise and run do not securely separate a and n from a compressed abbreviation.','p01_dans','low')
dec('M0638','undecided',r'\unsure{\dot X_i|\dot\Sigma_i}','Both Sigma-like top/bottom bars and X-like crossing diagonals are visible under the dot. Their temporal order is not established.','p03_first_union','low')
dec('M0639','other',r'=','Two distinct horizontal strokes appear after lui. No m-shaped lower member is written.','p08_lui','high')
dec('M0640','undecided',r'\mathring T_{\unsure{<i0|<i}}','A separate closed oval follows the dotted i, slightly above its hook. Its function/degree remains open.','p10_ambient','low')
dec('M0641','undecided',r'\unsure{i\leq k<j|i<k<j}','The first relation has a dense extra lower stroke, but retracing masks whether it is an independent lower bar.','p15_union','low')
dec('M0642','first',r'X_{jk}','A separate j hook is followed by k stem and arms.','p15_union','high')
dec('M0643','first',"donc c'est",'The d loop, low on run and final c are followed by a separate c, apostrophe and est run.','p16_donc','high')
dec('M0644','undecided',r'\unsure{X\mathbin{\cdot-}X_j|X-X_j}','A low detached dark point/short oblique mark precedes one horizontal dash. Both are preserved with role uncertainty.','p23_final_ambient','low')

inventory=[]
def inv(kind,pos,words,hand='his hand'):
 inventory.append(dict(element=f'E{len(inventory)+1:02d}',kind=kind,position=pos,first_words_or_objects=words,sheet_kind='text',hand=hand,transcribed='yes'))
inv('text','Upper left, above/left of heading','32, authorial number')
inv('text','Top, main baseline1',r'14\unsure{:|..} Description heuristique des; two Sigma groups and final point')
inv('text','Main baselines 1–3','(Peut se préciser considérablement ... topologie modérée).')
inv('text','Main baselines 3–5','Pour construire Sigma_i ... et on prend')
inv('insertion','Above baseline 4, leader into gap after tubulaire',r"``standart'' $T_{<i}$")
inv('deletion','Baseline4, crowded word before de','Candidate fermé; reading and cancellation state explicitly doubtful')
inv('display','Within baseline 4',r'Overdrawn dotted X/Sigma_i = union_{k<i} X_i; bars/crossings retained in doubt and note')
inv('display','Main baseline 6',r'(42) Sigma_i = X_i setminus X_i cap ring T_<i')
inv('display','Left part of main baseline 7',r'ring T_<i overset déf = T_<i setminus dot T_<i, final point')
inv('margin note','Oblique left margin beside baselines 6–9',r'Underlined NB On peut prendre T_<i = union_{k<i} T_k; où T_k est un vois. tub. standart des X_k')
inv('text','Right of baseline 7 through baseline 9',r'(Underlined NB Il aurait suffit ici ... lui = ... Sigma_i = X_i setminus ring T_<i)')
inv('text','Main baselines 10–11','Pour construire Sigma_ij ... T prime_ij de Sigma_i dans')
inv('display','Right part of baseline 11',r'X_j setminus overdrawn X_j cap ring T_<i0 = X prime_i; extra oval role open')
inv('text','Main baselines 12–14','(NB cette fois-ci il faut ... d’abord prendre ... dans X, ou sinon, dans X_j).')
inv('deletion','Baseline12 before d’abord',r'\deleted{\unsure{prendre}}')
inv('text','Main baselines 14–15',r'On prend T prime_ij ``suffisamment petit'' p.r. au choix de T_<i. Puis on prend')
inv('text','Main baseline 16',r'dot T prime_ij, et dans dot T prime_ij la trace de union_{i≤k<j} X_jk; first relation open')
inv('deletion','Baseline16 after first dotted T prime','Small s-like remnant; deletion/live state explicitly open')
inv('text','Main baselines 17–19',r'(donc c’est vide ...), soit S dot T prime_ij (``partie singulière'' de T prime_ij.; no closing parenthesis')
inv('drawing','Left margin opposite baselines 17–18','Vertical oval, one filled point, three rising strokes; small gap before middle stroke')
inv('text','Main baselines 19–24','On prend alors un voisinage tubulaire standart ... (pris ... et de T prime_ij). On ... alors')
inv('insertion','Above baseline 20, curving leader before its live de',r'T(S dot T prime_ij)')
inv('insertion','Above baseline 21, immediately over end of réunion',r'union T_k')
inv('insertion','Above baseline 24, long leader between et and T prime_ij','de')
inv('deletion','Baseline24 after On',r'\deleted{\unsure{prendra}}; masked ending remains doubtful')
inv('insertion','Above cancelled word on baseline 24','aura')
inv('display','Main baseline 25, at the lower paper edge',r'(43) Sigma_ij = dot T prime_ij setminus ring T(S dot T prime_ij)')
inv('margin note','Lower-left corner','72, pale foliation','another unnamed hand')

doubts=[
 dict(place='Item14 punctuation',reading=r'14\unsure{:|..}',alternatives='colon / two points; punctuation role unsettled',confidence='low',reason='Two dark points are present at different heights and slightly offset horizontally.'),
 dict(place='First dans/ds',reading=r'\unsure{dans|ds}',alternatives='dans | ds',confidence='low',reason='The middle low run is too compressed to isolate a and n securely.'),
 dict(place='Crowded word after tubulaire',reading=r'\unsure{\deleted{fermé}|fermé}',alternatives='Tentative fermé, deleted or live; exact letters also remain uncertain',confidence='low',reason='The insertion leader, long horizontal stroke and small residual letter bodies cannot be separated securely.'),
 dict(place='First dotted left-hand symbol',reading=r'\unsure{\dot X_i|\dot\Sigma_i}',alternatives='dotted X_i | dotted Sigma_i; overworking order open',confidence='low',reason='Top/bottom bars and crossed diagonals coexist; neither layer can be assigned a secure temporal order.'),
 dict(place='Crowded second X in ambient formula',reading=r'\unsure{X_j}',alternatives='X_j leading, underlying reworking unspecified',confidence='medium',reason='Crossed X strokes and a j hook are visible under dark retracing; no older letter is recoverable with confidence.'),
 dict(place='Ambient formula, ringed T subscript',reading=r'\mathring T_{\unsure{<i0|<i}}',alternatives='<i0 | <i; oval degree/role open',confidence='low',reason='A separate oval lies slightly above the i hook; its status as an additional 0 is not secure.'),
 dict(place='Cancelled prendre in second NB',reading=r'\deleted{\unsure{prendre}}',alternatives='prendre, with obscured interior letters',confidence='low',reason='The strike masks the low central letters, despite visible initial p and later d. Both witnesses read the same word; this is certainty-only.'),
 dict(place='Underlined dans/ds before X',reading=r'\uline{\unsure{dans|ds}}',alternatives='dans | ds',confidence='low',reason='The low middle strokes are compressed, while the independent underline and outer d/s forms are clear.'),
 dict(place='s-like remnant after first dotted T prime',reading=r'\unsure{\deleted{s}|s}',alternatives='deleted s | live s; letter candidate remains tentative',confidence='low',reason='An open upper curl and heavy lower oblique survive, without a securely separable cancellation stroke.'),
 dict(place='First relation in second union bound',reading=r'\unsure{i\leq k<j|i<k<j}',alternatives='i≤k<j | i<k<j',confidence='low',reason='Dense lower retracing prevents deciding whether the extra stroke is a lower inequality bar.'),
 dict(place='Lower X to X_j expression',reading=r'\unsure{X\mathbin{\cdot-}X_j|X-X_j}',alternatives='Detached point/oblique mark plus dash | dash with unassigned preceding ink',confidence='low',reason='Both marks are visible, but their role as a relation or revision is unsettled.'),
 dict(place='Final cancelled word',reading=r'\deleted{\unsure{prendra}}',alternatives='prendra; masked terminal group may admit prendre',confidence='low',reason='The horizontal strike and retracing conceal the low middle and final letters. Raised aura remains clear.')
]

notes=[
 dict(id='150-073-N01',text='The sheet carries authorial 32, heading 14 with two separated punctuation points, formula numbers (42) and (43), and pale other-hand foliation 72. The page has 25 main baselines; interlinear insertions and the four oblique margin baselines are separately inventoried.'),
 dict(id='150-073-N02',text='The author labels the discussion a heuristic description of the Sigma_i and Sigma_ij and writes that it can be made considerably more precise in a context of topologie modérée. He describes choices of tubular neighbourhoods, writes formula (42) and the definition of the ringed T notation, and adds a marginal proposal expressing T_<i as a union of T_k. This is a report of the manuscript, with no proof check.'),
 dict(id='150-073-N03',text='The author’s main NB reads Il aurait suffit ici, followed by a statement about choosing the neighbourhood in X_i lui =. The literal equals glyph abbreviates même in that phrase. The repeated spelling standart is preserved at every local occurrence. Neither this sentence nor the accompanying formula has been verified mathematically.'),
 dict(id='150-073-N04',text='The first union is literally written with right-hand X_i although its bound is k<i and both witnesses give X_k. The left dotted glyph has Sigma-like bars and X-like diagonals with uncertain layer order. The second ambient expression retains the overdrawn X_j and a visible small oval after the dotted i in the T subscript. These are ink decisions; no intended identity or corrected notation is inferred.'),
 dict(id='150-073-N05',text='For Sigma_ij the author describes a tubular neighbourhood T prime_ij, its dotted version, and a trace of a union with two written index components j and k on X. The first relation of that union bound remains ≤|<. He then calls S dot T prime_ij a partie singulière of an undotted T prime_ij; the parenthesis has no visible closing member before the following full stop. These manuscript formulations are retained without verification or repair.'),
 dict(id='150-073-N06',text='The lower paragraph has an inserted T(S dot T prime_ij), an inserted union T_k above réunion, and an inserted de whose curved leader attaches after et. A single live de beneath the first insertion leader is preserved. The author replaces a partly masked prendra by raised aura and gives formula (43). The lower-left drawing consists of an oval, one filled point, and three slightly rising strokes; a small white gap separates the point from the middle stroke.'),
 dict(id='150-073-N07',text='No mathematical argument, theorem, implication or conditional theorem was supplied or checked in this reading. All mathematical statements in these notes are attributed to the manuscript. check_events is empty because visual transcription and comparison alone are not proof checking.'),
 dict(id='150-073-N08',text='In the lower de S dot T prime_ij phrase, tiny detached dark traces appear below-left of the T stem. Their provenance as pen-start/reworking or surface traces is uncertain, and no coherent extra glyph or attachment is recoverable. They are recorded locally in the comment and audit reading without inventing a linguistic token. In the first dotted X/Sigma and the second X_j, all visible overworking is described without inventing an underlying deleted letter.'),
 dict(id='150-073-N09',text='The final Sigma_ij j descender meets the paper edge; no further stroke below the edge and no terminal punctuation for(43) can be recovered. The reader inspected the whole image, both original halves, and each saved first-pass crop. No OCR, external research, TeX compilation or second-pass recropping was used.')
]
notation=[
 dict(form=r'\mathring T_{<i},\dot T_{<i}',meaning='The manuscript explicitly writes ring T_<i = T_<i setminus dot T_<i, with déf over the equality.',evidence='Separate open ring and filled dot in the definition on baseline 7.',places='Definition below (42), p05'),
 dict(form=r'\dot X_i|\dot\Sigma_i',meaning='Overdrawn dotted left member of the first union formula; order of X/Sigma-like layers remains unresolved.',evidence='Horizontal top/bottom bars and crossed diagonals under one dot.',places='Baseline4, p03'),
 dict(form=r'=',meaning='Written word abbreviation after lui; expanded only in the abbreviation list.',evidence='Two separate horizontal strokes after lui.',places='Main NB, p08'),
 dict(form=r"T(S\dot T'_{ij}), S\dot T'_{ij}",meaning='The author labels the latter partie singulière and inserts the former as the named tubular neighbourhood in the lower paragraph.',evidence='S forms, dotted T, primes and ij groups visibly recur in the insertion, sentence and (43).',places='Baselines18–25, p17,p20,p26'),
 dict(form=r'X_{jk}',meaning='Literal two-component index on the summand in the second union; no correction inferred.',evidence='A left-returning j hook precedes distinct k arms.',places='Baseline16, p15'),
 dict(form=r'\cdot-',meaning='A detached low point/short oblique mark followed by one dash, whose role is unresolved.',evidence='Two separated dark components between X and X_j.',places='Baseline22, p23')
]
abbreviations=[
 dict(written='NB',expansion='nota bene',places='Oblique margin and two main parenthetical notes'),
 dict(written='vois.',expansion='voisinage',places='Margin and second NB'),
 dict(written='tub.',expansion='tubulaire',places='Margin and second NB'),
 dict(written='p.r.',expansion='par rapport',places='After suffisamment petit and after assez petits'),
 dict(written='déf',expansion='définition',places='Above the equality in the definition below (42)'),
 dict(written='=',expansion='même, as a word abbreviation after lui',places='Main NB, p08'),
 dict(written='ds',expansion='dans; this short form remains an alternative at two compressed occurrences',places='Opening parenthesis and underlined word in second NB')
]
hand_log=[
 dict(habit='The low a/n sequence of dans can collapse to a nearly horizontal run between d and s.',places='p01,p12,p13',scope='The first and underlined occurrences remain doubtful; the later occurrence before X_j has separable a/n traces.',witness_errors='C first ds alternative and two further ds readings; H full dans is not automatically expanded at the unresolved places.'),
 dict(habit='Terminal t in standart is tall and angular or hooked, while the middle low letters are strongly compressed.',places='p02,p07,p09,p12,p20,p22',scope='All six occurrences on this page were read locally.',witness_errors='H modernises the ending to standard at each occurrence.'),
 dict(habit='A dotted, hooked i can look like a comma or resemble a compact subscript k when joined to X.',places='Title and first union, p00,p03',scope='Specific local i forms only; the bound k<i has a much taller k.',witness_errors='Both witnesses supply a comma between the title objects and give X_k for the first union summand.'),
 dict(habit='Curved insertion leaders cross nearby ascenders and can resemble parentheses or strike strokes.',places='p02,p20,p24',scope='The lower formula leader and inserted de attachment are secure; the first crowded word’s state remains open.',witness_errors='H duplicates a cancelled de beneath the lower inserted formula; its visible crossing belongs to the leader.'),
 dict(habit='An equals glyph is used as the word abbreviation même.',places='p08',scope='Only the phrase lui =; formula equalities retain their ordinary written role.',witness_errors='C suggests overlined m; H expands to lui-même.'),
 dict(habit='A compact j hook and k may touch in one subscript without erasing either component.',places='p15',scope='The second union summand only.',witness_errors='H omits the visible j from X_jk.'),
 dict(habit='Open rings above T and filled dots above T are drawn distinctly on this sheet.',places='p04,p05,p08,p10,p14,p17,p20,p26',scope='Each occurrence was checked locally; the T in the partie singulière parenthesis has no dot.',witness_errors='H dots the undotted T prime in the parenthesis.'),
 dict(habit='Double quotation marks may be two separate uprights or a compact connected pair of high curves.',places='p02,p17,p28,p29',scope='All four quotation pairs on this sheet.',witness_errors='H renders the pairs as guillemets.'),
]

audit=[]
def ab(kind,box,reading):
 audit.append(dict(box=f'B{len(audit)+1:02d}',kind=kind,x0=box[0],y0=box[1],x1=box[2],y1=box[3],reading=reading))
ab('handwritten number',[42,23,103,78],r'\mspage{32}')
ab('handwritten number',[199,24,260,106],r'14\unsure{:|..} % Two separate points, upper rounder and lower slightly oblique, diagonally offset.')
ab('lexical disagreement',[259,45,1212,162],r'\uline{Description heuristique des} $\Sigma_i\ \Sigma_{ij}$. % At the lower boundary, clipped upper ascenders/accent strokes of the following line are neighbouring fragments; the long q descender belongs to heuristique.')
ab('lexical disagreement',[768,141,880,201],r'\unsure{dans|ds}')
ab('insertion',[466,280,1064,392],r'''\inserted{``standart'' $T_{<i}$}
% Raised above the baseline, leader descending into the gap after tubulaire.
tubulaire \unsure{\deleted{fermé}|fermé} de
% The long curved leader is continuous; no literal opening parenthesis is supplied. Word reading and cancellation state remain open.''')
ab('doubtful formula',[1118,294,1469,419],r'''$\unsure{\dot X_i|\dot\Sigma_i}=\displaystyle\bigcup_{k<i}X_i$,
% The left letter retains horizontal Sigma-like bars and X-like crossing diagonals; their order is unknown.''')
ab('handwritten number',[404,479,1064,568],r'$(42)\qquad\Sigma_i=X_i\setminus X_i\cap\mathring T_{<i}$ % No independent final point.')
ab('doubtful formula',[378,590,835,686],r'$\mathring T_{<i}\overset{\mathrm{déf}}{=}T_{<i}\setminus\dot T_{<i}$.')
ab('lexical disagreement',[950,584,1637,671],r'(\uline{NB} Il aurait suffit ici')
ab('lexical disagreement',[1298,690,1510,753],'standart')
ab('lexical disagreement',[545,797,751,867],r'lui $=$,')
ab('doubtful formula',[1344,767,1656,849],r'$\Sigma_i=X_i\setminus\mathring T_{<i}$) % No point before the closing parenthesis.')
ab('margin note',[14,465,391,869],r'''\margin{\uline{NB} On peut prendre $T_{<i}=\bigcup_{k<i}T_k$, où $T_k$ est un vois. tub. standart des $X_k$}
% Four oblique baselines. Non-margin foreground inside this rectangle: de and dans are the beginnings of two main-body lines at lower right; a clipped neighbouring descender from prend is at the upper right. The rightmost short tub. ending meets the crop boundary; no unseen continuation is supplied.''')
ab('doubtful formula',[1177,970,1557,1083],r'''$X_j\setminus\unsure{X_j}\cap\mathring T_{\unsure{<i0|<i}}=X'_i$
% Second X is overdrawn. The extra closed oval lies just to the right of dotted i, slightly above its hook. Its role/degree remains open.''')
ab('lexical disagreement',[232,1100,365,1177],r'(NB % No independent underline beneath NB.')
ab('struck passage',[931,1087,1112,1152],r'\deleted{\unsure{prendre}} % Continuous horizontal strike masks the low central letters; p descender and later tall d remain.')
ab('lexical disagreement',[728,1161,1073,1228],r'standart \uline{\unsure{dans|ds}}')
ab('lexical disagreement',[249,1288,363,1349],'dans')
ab('lexical disagreement',[1035,1228,1607,1339],r"``suffisamment petit'' % Both high quote pairs are partly joined; petit has no separate terminal s.")
ab('struck passage',[577,1422,749,1527],r"$\dot T'_{ij}$\unsure{\deleted{s}|s}, % The small s-like body has a dense lower diagonal; strike state remains open.")
ab('doubtful formula',[1074,1409,1545,1536],r'''la trace de $\displaystyle\bigcup_{\unsure{i\leq k<j|i<k<j}}X_{jk}$
% A clipped neighbouring lower pen tip from the line above occurs at the top boundary. The union formula, both relations and both summand index components are wholly included.''')
ab('lexical disagreement',[571,1537,1656,1609],r'''(donc c'est vide si $j$ est un successeur
% Near the lower edge is the detached dot over the T of the next line; any clipped top-bar fragment belongs to that following formula, not to this phrase.''')
ab('lexical disagreement',[570,1592,1656,1703],r'''de $i$), soit $S\dot T'_{ij}$ (``partie singulière''
% The upper boundary includes the tail of the j from the preceding line. The dot over this line's T is included above its bar.''')
ab('margin note',[118,1561,399,1694],r'''\figure{\begin{tikzpicture}[x=.01cm,y=-.01cm,line width=.6pt,line cap=round,line join=round]
\draw (54,11) .. controls (29,6) and (9,33) .. (8,67) .. controls (6,99) and (20,123) .. (51,127) .. controls (77,131) and (97,112) .. (103,90) .. controls (108,68) and (99,38) .. (89,23) .. controls (79,12) and (67,9) .. (54,11);
\draw (91,36) .. controls (116,32) and (145,29) .. (173,30) .. controls (207,30) and (247,26) .. (271,27);
\draw (66,73) .. controls (96,73) and (113,69) .. (141,67) .. controls (187,67) and (236,56) .. (272,60);
\draw (102,101) .. controls (135,97) and (184,92) .. (220,91) .. controls (246,89) and (263,96) .. (274,91);
\fill (56,73) circle (1.4pt);
\end{tikzpicture}} % One filled point; middle stroke begins after a small white gap; outer strokes join oval.''')
ab('doubtful formula',[249,1712,527,1813],r'''de $T'_{ij}$. % No dot above T and no closing parenthesis before the period. At the lower right are clipped initial strokes of the interlinear T(S dot T prime_ij) insertion; those belong to the following construction.''')
ab('lexical disagreement',[578,1715,1002,1792],r'''On prend alors % At the lower-left boundary a clipped part of the interlinear formula/leader from the next line is visible; no lexical continuation is supplied.''')
ab('insertion',[479,1768,1087,1910],r'''\inserted{$T(S\dot T'_{ij})$} de $S\dot T'_{ij}$ dans $\dot T'_{ij}$
% Formula raised above the live de; continuous curved leader crosses its ascender. No separate deleted duplicate. At top are clipped descenders of the preceding main line. At bottom are clipped upper strokes of the later union insertion. Two tiny detached traces below-left of the baseline T stem are unassigned reworking/surface marks; no extra glyph is inferred.''')
ab('lexical disagreement',[242,1817,451,1888],'standart')
ab('insertion',[844,1878,970,1939],r'\inserted{$\bigcup T_k$} % Written above the end of réunion; no bound is written beneath the union.')
ab('lexical disagreement',[241,2013,796,2106],r'standart des $X_k$')
ab('doubtful formula',[885,1999,1574,2120],r'''($i<k<j$) dans $\unsure{X\mathbin{\cdot-}X_j|X-X_j}$
% A low detached point/short slanted stroke precedes one dash; role unresolved. Clipped top of an ascender from the following line appears at the lower boundary.''')
ab('lexical disagreement',[382,2119,748,2212],r'''``assez petits''
% Below the quote are the neighbouring inserted de and the upper curved end of its leader; the leader continues below the box. Those visible words read \inserted{de}.''')
ab('insertion',[411,2172,720,2323],r'''et \inserted{de} $T'_{ij}$).
% de is above the line; its long curved leader descends after et. At top are clipped lower strokes from the quoted petits; at lower left is a clipped piece of the neighbouring formula-number parenthesis(43). The complete number is covered in its own box.''')
ab('struck passage',[741,2195,1258,2296],r'''On \deleted{\unsure{prendra}}\inserted{aura} alors
% aura is raised above the cancelled word. The initial p descender survives below the strike. Along the bottom boundary are the dots, ring and upper T bars of the following display, whose full formula has its own box.''')
ab('handwritten number',[333,2258,1258,2359],r'''$(43)\qquad\Sigma_{ij}=\dot T'_{ij}\setminus\mathring T(S\dot T'_{ij})$
% At the upper edge are clipped low remnants of the cancelled word and of alors from the preceding line. The final display's left j descender reaches the paper edge; no extension or terminal point is supplied.''')
ab('handwritten number',[21,2290,84,2345],r'\margin{72} % Pale foliation in another hand.')

records=dict(scan='073',reader='reader_b',line_count=25,changes=changes,decisions=decisions,inventory=inventory,doubts=doubts,notes=notes,check_events=[],notation=notation,abbreviations=abbreviations,hand_log=hand_log,audit_boxes=audit,crops=[{k:v for k,v in c.items() if k!='rotation'} for c in manifest['crops']],unresolved=[d['place']+': '+d['alternatives'] for d in doubts],coverage=dict(whole_image_viewed=True,halves_viewed=['top','bottom'],all_tokens_read=True,all_C_insertions_deletions_checked=True,differences_considered=len(list(csv.DictReader((ROOT/'edition/packets/150_scan073/diffs.tsv').open(),delimiter='\t'))),macro_only_differences_ignored='Equivalent deleted/struck and inserted/add wrappers, mathematical font commands, line wrapping and display packaging, and editorial source-number notes are not counted. Actual underline scope/absence and drawn quotation shapes are counted. The foliation wrapper changes only hand attribution.'))
atomic(OUT/'150_scan073.json',json.dumps(records,ensure_ascii=False,indent=2)+'\n')
print('changes',len(changes),'against C',sum(c['against_C'] for c in changes),'against H',sum(c['against_H'] for c in changes),'audit boxes',len(audit),'crops',len(manifest['crops']),'diff rows',records['coverage']['differences_considered'])
