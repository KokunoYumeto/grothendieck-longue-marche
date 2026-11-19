import sys
sys.path.insert(0,'out/scripts');from work import commit
T=r'''\clearpage
\scanpage{5}
\figure{\begin{tikzpicture}[every node/.style={anchor=base west}]
\node at (0,0) {C)};
\node at (1.2,0) {Mèthodes};\node at (3.6,0) {projectives};
\node at (3.5,.75) {\inserted{de construction}};
\draw (1.2,-.15)--(6.1,-.08);\draw (3.7,.53)--(6.1,.53);
\draw (6.6,.7)..controls (6.8,.2) and (4.1,.43)..(3.5,.3)..controls (3.3,.15) and (3.4,-.25)..(3.45,-.4);
\end{tikzpicture}}

\S\,14\quad Familles limitées.

\figure{\begin{tikzpicture}[every node/.style={anchor=base west}]
\node at (0,0) {\S\,15};\node at (1.4,0) {Schémas de Hilbert.};\node at (7.4,0) {(+ appl. aux quotients).};
\node at (1.7,.55) {\inserted{Foncteurs et}};\node at (1.3,.75) {\unsure{-}};
\draw (4.4,.7)--(4.4,.35)..controls (3.2,.25) and (1.6,.35)..(1.35,.18)..controls (1.1,0) and (1.22,-.2)..(1.3,-.35);
\end{tikzpicture}}

\figure{\begin{tikzpicture}[every node/.style={anchor=base west}]
\node at (0,0) {\S\,16};\node at (1.4,0) {Schémas de Picard.};
\node at (1.7,.55) {\inserted{Foncteurs et}};
\draw (4.7,.7)--(4.7,.35)..controls (3.3,.2) and (1.6,.35)..(1.35,.18)..controls (1.1,0) and (1.22,-.2)..(1.3,-.35);
\end{tikzpicture}}
\margin{\begin{tikzpicture}[every node/.style={anchor=north west,font=\scriptsize,align=left}]
\node[text width=4cm] at (0,0) {(Ths d'existence projectifs};
\node[text width=3.2cm] at (1,-.45) {exclusivement\deleted{\unsure{)}}; également le cas de gpe structural affine commutatif plus général que $\mathrm G_{\mathrm m}$\ldots.};
\draw (-.45,-.4)--(.4,-.4)..controls (.65,-.4) and (.6,-.5)..(.6,-.7)--(.65,-1.7)..controls (.65,-1.85) and (.8,-1.8)..(1.1,-1.85)--(3.9,-1.9)..controls (4.1,-1.85) and (4.3,-1.75)..(4.3,-1.6);
\end{tikzpicture}}

\S\,17\quad Variantes de Picard.

\S\,1\deleted{\unsure{7}}8\quad Applications aux courbes

\S\,1\deleted{\unsure{8}}\unsure{9|8}\quad Formalisme des normes

\S\,\deleted{\unsure{19}}20\quad Invariants multiprojectifs de Mumford.

\figure{\begin{tikzpicture}[every node/.style={anchor=base west}]
\node at (0,0) {D)};\node at (1.2,0) {Méthodes};\node at (3.8,0) {mixtes};
\node at (3,.65) {\inserted{de construction}};
\draw (1.1,-.16)--(5.4,-.08);\draw (3.2,.45)--(5.4,.45);
\draw (5.8,.55)..controls (6,.35) and (4.1,.35)..(3.7,.2)..controls (3.4,.1) and (3.5,-.1)..(3.5,-.25);
\end{tikzpicture}}

\S\,2\deleted{0}1\quad Cas de représentabilité de $\mathrm P\underline{\mathrm{ic}}$, $\mathrm P\underline{\mathrm i\unsure{\mathrm c|\mathrm e}}^{\unsure{0|o|\circ}}$, $\unsure{-|\deleted{\mathrm P}}\mathrm P\underline{\mathrm{ic}}_{X}^{\tau}$ \ldots

(y compris le cas de Mumford utilisant \S\,\deleted{\unsure{19}}20).

\S\,21\quad Cas de représentabilité des foncteurs $\prod_{\deleted{X}Y/S}X/Y$ etc.

(\unsure{ths|Ths} du type Matsumura).

\noindent\rule{\linewidth}{.3pt}

NB.\quad On suppose \unsure{connues|connus} toutes les \unsure{gén.} fonctorielles (topologies, descente faisceaux, \unsure{quotients|quotient}) ; à rappeler au besoin dans $\unsure{0|O}_{\underline{\overline{\mathrm V}}}$.

\noindent\rule{\linewidth}{.3pt}

\uline{Manquent} :

\figure{\begin{tikzpicture}[every node/.style={anchor=north west,align=left,font=\small}]
\node at (.7,0) {\deleted{Il \unsure{manquera|manquerait}}};
\node[text width=3.6cm] at (0,-.6) {dans Chap. sur schémas\\en groupes};
\node at (4.7,.1) {les ths relatifs aux VA};
\node[text width=8.3cm] at (4.7,-.6) {les ths \unsure{genx|g\textsuperscript{enx}} \unsure{pointus|partiels} sur Picard, et l'étude\\qualitative générale des schémas de Picard,\\(y compris critère de lissité de Mumford\ldots)};
\draw[line width=1pt] (4.2,.15)..controls (3.95,.25) and (4.02,-.1)..(4.02,-.18)--(3.94,-.24)--(4.04,-.29)--(4.04,-.59)..controls (4.02,-.65) and (4.15,-.64)..(4.23,-.63);
\draw (2,-1.1)..controls (2.5,-1.4) and (3.4,-.95)..(3.9,-.65);
\node[text width=2.2cm] at (2,-3.15) {dans\\Chapitre sur\\Picard};
\draw (4.28,-.85)..controls (4.2,-1.35) and (4.65,-2.25)..(4.38,-2.6)--(4.3,-2.68)..controls (4.7,-2.85) and (4.6,-3.45)..(4.6,-3.8)..controls (4.6,-4.15) and (4.72,-4.4)..(4.8,-4.52);
\node at (5.5,-2.05) {\inserted{Étude du}};
\node[text width=8.8cm] at (4.55,-2.4) {(?) \deleted{\unsure{Relation} entre} Picard d'un schéma projectif\\\hspace*{.9cm}en termes d'un pinceau de sections\\\hspace*{.9cm}hyperplanes.};
\node[text width=8.4cm] at (4.8,-4.1) {Les th. sur Picard genre ``\unsure{certines|certaines} \unsure{équivalences|équivalence}''.};
\node[text width=2.4cm] at (2,-4.9) {dans Chap.\\sur $\unsure{\pi_1|\pi}$};
\draw (4.8,-4.8)..controls (4.87,-4.95) and (5,-5.1)..(4.88,-5.22)--(4.8,-5.27)..controls (4.98,-5.38) and (4.95,-5.55)..(5.1,-5.85);
\node[text width=8.2cm] at (5.1,-4.8) {Les formulations de descente à la van Kampen\\\hspace*{.8cm}etc, en termes de groupe fondamental};
\end{tikzpicture}}
% archive sheet number: 4
'''
L=[]
def a(p,c,h,f,ink,conf='high',ac=True,ah=True,k='other',mh='no',con=None):
 d=dict(place=p,c=c,h=h,final=f,ink=ink,confidence=conf,against_c=ac,against_h=ah,kind=k,marked_in_H=mh)
 if con:d['consequential']=con
 L.append(d)
a('C heading accent',r'\unsure{Mèthodes|Méthodes}','Méthodes','Mèthodes','C: the small detached accent descends from upper left to lower right, a grave.',k='misread word')
a('C heading insertion order and leader','de construction inserted before projectives; leader absent','after projectives in heading; box described in note','de construction above; curved leader ends before projectives','C: the long lower edge of the insertion curves down at the left of projectives; it is not a closed box. The base and insertion have separate underline strokes.',k='insertion or placement')
a('§14 last word',r'\unsure{limitées}',r'\uncertain{limitées}','limitées','fourteen: tall l and t, two i strokes with dots, accent over e and terminal ees are individually visible.','medium',k='misread word',mh='yes')
a('§15 small isolated stroke','omitted','omitted',r'\unsure{-}','dash15: short dark horizontal stroke above-left of Foncteurs et, followed by faint grey taper. Its role as punctuation is uncertain.','low',k='omission')
for s,cr in [('15','fifteen'),('16','sixteen')]:
 a('§'+s+' insertion leader','Foncteurs et inserted; line absent','interlining described; opening parenthesis asserted in note','Foncteurs et with bent leader before Schémas',cr+': the horizontal line beneath the insertion is continuous with the left downward curl before Schémas; it is a leader, not a detached parenthesis.',k='drawing or diagram')
a('§16 margin abbreviation',r'\unsure{Ths|Thes}','Ths','Ths','margin16_upright: tall T followed by h and s; no separate e between them.','medium',ah=False)
a('§16 margin adverb',r'\unsure{exclusivement}','exclusivement','exclusivement','exclusivement: the e-x-c-l-u-s-i-v-e-m-e-n-t sequence remains visible despite overlap near the terminal t.','medium',ah=False)
a('§16 old closing parenthesis',r'\deleted{\unsure{)}}','omitted',r'\deleted{\unsure{)}}','exclusivement: thick crossed curved stroke after t could be the old closing parenthesis; no secure complete outline survives.','low',False,True,'omission')
a('§16 gpe abbreviation',r'\unsure{gpe|gpes}',r'\uncertain{groupes}','gpe','structural: looped g and descending p followed by short e ending, with no final s.','medium',k='abbreviation expanded or spelling modernised',mh='yes')
a('§16 structural ending',r'\unsure{structural|structuraux}',r'\uncertain{structuraux}','structural','structural/affine: terminal tall ascending-returning l precedes the distinct next word; no x-shaped terminal crossing.','medium',k='misread word',mh='yes')
a('§16 affine ending','affine',r'\uncertain{affines}','affine','affine: paired f loops, i dot and compressed ne; no additional s after final e.',ac=False,k='misread word',mh='yes')
a('§16 commutatif ending',r'\unsure{commutatif}','commutatifs','commutatif','commutatif: final long f descender turns left at the bottom; no separate s follows.','medium',k='misread word')
a('§16 général ending','général',r'\uncertain{généraux}','général','generalG: the last stroke is a tall l-like return, not the two diagonals of x.','medium',False,True,'misread word','yes')
a('§16 group symbol',r'\unsure{\mathrm G_{\mathrm m}|\mathrm G_m}',r'\mathbb G_m',r'\mathrm G_{\mathrm m}','generalG: one bowl and internal short bar form G; no second stem. Two low humps form the m index.','medium',k='misread symbol or index')
a('§16 terminal dots',r'\ldots',r'\ldots',r'\ldots.','generalG: four separated dark dots follow the low m, before the pale enclosing curve.','medium',k='omission')
a('§16 margin enclosure and final parenthesis','margin prose, final )','brace grouping §§16–20 asserted, final )','pencil left/down enclosure; no added final parenthesis','whole/margin16_upright/generalG: pale line enters from the left, bends downward beside the note and continues below it, turning up at far right. The terminal curve belongs to this line, not to a separate closing parenthesis.','medium',k='drawing or diagram')
a('Applications overwritten number',r'1\deleted{\unsure7}8','18; overwrite described',r'1\deleted{\unsure7}8','num18: live 8 has two dark loops; the older digit is cut through and remains tentatively7.','low',False,True,'omission')
a('Formalisme overwritten number',r'1\deleted{\unsure8}\unsure{9|8}','18',r'1\deleted{\unsure8}\unsure{9|8}','num19: current outline resembles9 but a lower loop from the overwritten figure interferes; neither the live nor old digit can be fully resolved.','low',False,True,'misread symbol or index')
a('Invariants live number',r'\unsure{20}','20','20','num20: a top hook and descending diagonal with basal foot form2, followed by a full oval0.','medium',ah=False)
a('Invariants old number',r'\deleted{\unsure{19}}','overwrite described without old reading',r'\deleted{\unsure{19}}','num20: old narrow vertical and curved traces survive under20; 19 remains tentative.','low',False,True,'omission')
a('Invariants adjective','multiprojectifs',r'\uncertain{multiprojectifs}','multiprojectifs','twenty: m-u-l-t-i-p-r-o-j-e-c-t-i-f-s can be traced through the light central letters; initial m is not preceded by a parenthesis.','medium',False,True,'misread word','yes')
a('D heading insertion order and leader','de construction before mixtes, no leader','after mixtes; parentheses described','insertion above, leader before mixtes','D: one continuous curved line runs beneath de construction and down before mixtes, not a pair of parentheses; two separate underlines are present.',k='insertion or placement')
a('first representability old number',r'2\deleted0 1','21; correction described',r'2\deleted0 1','twentyone: dense old oval0 remains between2 and the separately written1.',ac=False,k='omission')
a('three Pic underlines','underline entire Pic','underline entire Pic','underline ic only','Pic/firstPic/secondPic: each horizontal rule starts to the right of the descending P stem and runs only beneath the small following letters.','medium',k='misread symbol or index')
a('second Pic final letter','c','c',r'\unsure{\mathrm c|\mathrm e}','secondPic: the small final body has a closed loop and a lower right tail, unlike the open c beside it; c/e cannot be distinguished securely.','low',k='misread symbol or index')
a('second Pic exponent','0',r'\circ',r'\unsure{0|o|\circ}','Pic/secondPic: small closed raised oval, with no feature distinguishing numeral0, lettero and circle.','low',k='misread symbol or index')
a('mark before third Pic',r'\deleted{\unsure{\mathrm P}}','omitted',r'\unsure{-|\deleted{\mathrm P}}','oldP/Pic: after the comma-like stroke there is an isolated short horizontal dash; no separate P bowl and stem can be traced there. Dash is primary; a remnant of a cancelled P remains an alternative.','low',k='misread symbol or index')
a('third Pic exponent',r'\unsure{\tau|\mathrm t}',r'\tau',r'\tau','Pic: broad upper horizontal and hooked lower return, without a separate ascender above the bar.',ah=False)
a('Mumford reference old number',r'\deleted{\unsure{19}}','overwrite described',r'\deleted{\unsure{19}}','old19: superposed dark strokes leave a narrow old vertical and rounder component, insufficient to resolve19. The live20 is clear.','low',False,True,'omission')
a('last section number','21','22','21','num22: the final figure has a diagonal upper entry, straight downward stem and broad foot; it is1, not a curved2. The tight crop supersedes the initial impression from the wide crop.',ac=False,k='misread symbol or index',con='The last item is numbered21 again, not22; the visible numbering is retained.')
a('product old index',r'\deleted{\unsure X}Y/S','Y/S, old X described',r'\deleted X Y/S','prod: two crossing old diagonals remain under the live Y; no inference from another page was needed.','medium',k='omission')
a('Matsumura abbreviation case',r'\unsure{ths}','Ths',r'\unsure{ths|Ths}','Matsumura: crossed first stem with long return resembles t, but its height does not decisively separate lower t from capital T.','low',k='abbreviation expanded or spelling modernised')
a('NB connues ending','connues','connus,',r'\unsure{connues|connus}','connues: the final compressed low strokes do not securely distinguish ues from us; the comma-like last stroke may be the s itself, with no independent following comma.','low',k='misread word')
a('NB quantifier',r'\unsure{toutes}','tous','toutes','toutesles: a second tall t ascender appears after the long low ou stroke, followed by the dark es ending.','medium',k='misread word')
a('NB abbreviation',r'\unsure{gén.}','gén.',r'\unsure{gén.}','NB_upright: g loop and accent are visible, but compressed ending and tiny punctuation remain insufficiently distinct.','low',False,True,'misread word')
a('NB adjective',r'\unsure{fonctorielles}','fondamentaux','fonctorielles','fonctorielles/NB_upright: initial f, compressed onct, dotted i and two l ascenders followed by es; no d-a-m-e-n-t-a-u-x sequence.','medium',k='misread word',con='The presupposed material is called gén. fonctorielles, not gén. fondamentaux.')
a('NB descente punctuation','descente faisceaux','descente, faisceaux','descente faisceaux','NB_upright: descente reaches the line end with no separate comma before the next-line faisceaux.','medium',False,True,'text not on the page')
a('NB quotient ending','quotients','quotient',r'\unsure{quotients|quotient}','quotients: final t and long basal return are clear; the return could include a compressed s, but no separate s contour is securely isolated.','low',k='misread word')
a('NB instruction','à rappeler',r'i.e. \uncertain{rappelés}','à rappeler','NB_upright: grave-marked a followed by the tall paired p stems and terminal r; no i.e. group is present.','medium',False,True,'misread word','yes')
a('NB chapter notation',r'\unsure{0|O}_{\underline{\overline V}}',r'\uncertain V; round and underline described',r'\unsure{0|O}_{\underline{\overline V}}','NBV: a separate round mark stands above-left of V; V has distinct top and bottom rules. Round0/O remains unresolved.','low',False,True,'omission','yes')
a('Manquent underline','underlined','plain','underlined','manquent: continuous dark rule below Manquent; colon is outside its right end.',ac=False,k='omission')
a('old marginal sentence',r'\deleted{Il \unsure{manquera}}',r'\struck{Il manquerait}',r'\deleted{Il \unsure{manquera|manquerait}}','oldIl: strike traverses the final r/a/i/t region; its thick ending prevents deciding the suffix. Il and the start manqu are visible.','low',k='misread word')
a('VA abbreviation',r'\unsure{ths}','ths','ths','bottomfirst_upright: lower t crossed near the stem, h ascender and terminal s are visible.','medium',ah=False)
a('Picard general abbreviation',r'\unsure{ths g\textsuperscript{enx}|ths génx}','ths genre',r'ths \unsure{genx|g\textsuperscript{enx}}','gencase: the g descends, then e-n and a crossed x-like ending; no acute accent is visible. The small letters are near a common baseline, though their raised status remains uncertain.','low',k='abbreviation expanded or spelling modernised')
a('Picard adjective',r'\unsure{pointus|partiels}','finitude',r'\unsure{pointus|partiels}','pointus: initial descending p-like stem, short dotted stroke and later crossed t are visible; compressed middle prevents resolving C alternatives. No full finitude letter sequence is supported.','low',False,True,'misread word')
a('qualitative and générale placement','qualitative générale','qualitative (générale; interlining asserted','qualitative générale, actual line placement retained','bottomfirst_upright: the descending g loop follows qualitative; no distinct opening parenthesis can be separated from that letter. The words occupy the continuation line, without a caret or cancellation.','medium',False,True,'insertion or placement')
a('Mumford criterion',r'\unsure{critère}','critère','critère','critere: c-r-i, tall crossed t and compressed grave-bearing è-r-e are visible.','medium',ah=False)
a('Mumford lissité',r'\unsure{lissité}','lissité','lissité','critere: looped l, dotted i, paired low s bodies, crossed t and final acute e can be followed.','medium',ah=False)
a('question mark before Étude','(?)','(1.)','(?)','question_upright/bottombraces: curved upper stroke bends down and a detached dot lies below; it is not a straight1.',ac=False,k='misread symbol or index')
a('deleted Relation',r'\unsure{Relation}','Relation',r'\unsure{Relation}','question_upright: initial R, l ascender and partial t/i traces remain under the dark cancellation, but the full word is not independently recoverable.','low',False,True,'misread word')
a('inserted Étude article','Étude du','Étude des','Étude du','question_upright: looped d followed by one shallow u-shaped return; no e+s ending. The phrase sits above the cancelled Relation entre.','medium',False,True,'misread word')
a('quoted first word',r'\unsure{certaines|certines|sections}',r'\uncertain{certaines}',r'\unsure{certines|certaines}','certaines: initial c, e/r and tall t followed by a dotted i and compressed nes; a separate a cannot be found, so certines is primary. The initial c excludes sections.','low',k='misread word',mh='yes')
a('quoted second word',r'\unsure{équivalences|équivalentes|équivalence}',r'\uncertain{équivalences}',r'\unsure{équivalences|équivalence}','equiv_upright/equivalences: q descender, v, tall l and final rounded ce/s-like strokes are visible. No second t ascender/crossbar supports équivalentes; singular/plural ending remains uncertain.','low',k='misread word',mh='yes')
a('quoted phrase marks','double backticks/apostrophes','guillemets','double backticks/apostrophes','certaines/equivalences: two short raised strokes at each end, not angular guillemets.',ac=False,k='other')
a('bottom braces and chapter labels','large textual braces with margin labels','itemize; first brace assigned first two lines','TikZ braces, labels and curved leader at observed positions','whole/bottombraces/marg_schemas_upright/marg_pic_upright/marg_last_upright: short first brace ends beside upper part of second les; long brace begins just below that les and reaches the quoted line; third encloses descent lines. Curved leader runs from groupes to the short brace. Geometry is preserved without forcing a semantic grouping.','medium',k='drawing or diagram')
a('descent phrase','à la',' : le','à la','last_upright: a grave over the first a and looped l+a follow descente, not colon and le.',ac=False,k='misread word')
a('descent group article','de groupe','du groupe','de groupe','last_upright: the small word ends in the same e-shaped low return as other de on the page, without u-shaped bowl.','medium',False,True,'misread word')
a('last marginal index',r'\unsure{\pi_1|\pi}',r'\pi_1',r'\unsure{\pi_1|\pi}','pi1/marg_last_upright: a dark short stroke below-right of pi may be1, but grey intersecting marks prevent isolating its full contour.','low',False,True,'misread symbol or index')
I=[]
def i(k,p,t):I.append(dict(kind=k,position=p,text=t))
i('text','upper heading','C) Mèthodes projectives')
i('insertion','above C heading','de construction, anchor before projectives')
i('drawing','C heading','base underline, insertion underline, curved leader')
i('text','§14','Familles limitées.')
i('text','§15','Schémas de Hilbert. (+ appl. aux quotients).')
i('insertion','above §15','Foncteurs et')
i('text','above-left §15 insertion','uncertain short dash')
i('drawing','§15','bent insertion leader')
i('text','§16','Schémas de Picard.')
i('insertion','above §16','Foncteurs et')
i('drawing','§16','bent insertion leader')
i('margin note','right of §§16–19','Ths d’existence projectifs exclusivement; également le cas de gpe structural affine commutatif plus général que G_m....')
i('deletion','right margin after exclusivement','uncertain closing parenthesis')
i('drawing','around right margin note','pencil left/down enclosure, upturned right end')
i('text','§17','Variantes de Picard.')
i('text','§18','Applications aux courbes')
i('deletion','§18 old digit','uncertain7')
i('insertion','§18 live digit','8')
i('text','§19','Formalisme des normes')
i('deletion','§19 old digit','uncertain8')
i('insertion','§19 live digit','uncertain9/8')
i('text','§20','Invariants multiprojectifs de Mumford.')
i('deletion','§20 old number','uncertain19')
i('insertion','§20 live number','20')
i('text','D heading','Méthodes mixtes')
i('insertion','above D heading','de construction')
i('drawing','D heading','two underlines and curved insertion leader')
i('text','first §21','Cas de représentabilité de Pic, Pic^0/o/circle, Pic_X^tau; underlines beneath ic')
i('deletion','first §21 old digit','0')
i('insertion','first §21 live digit','1')
i('text','before third Pic','uncertain dash / deleted P remnant')
i('text','parenthesis below first §21','y compris le cas de Mumford utilisant §20')
i('deletion','Mumford reference old number','uncertain19')
i('insertion','Mumford reference live number','20')
i('text','second §21','Cas de représentabilité des foncteurs product Y/S X/Y etc.')
i('deletion','product index','old X')
i('insertion','product index','Y')
i('text','below product','ths/Ths du type Matsumura')
i('drawing','above NB','long horizontal divider')
i('text','NB','On suppose connues/connus toutes les gén. fonctorielles... à rappeler... 0/O with barred V index')
i('drawing','below NB','long horizontal divider')
i('text','lower heading','Manquent, underlined, colon outside rule')
i('deletion','lower left','Il manquera/manquerait')
i('margin note','lower left first label','dans Chap. sur schémas en groupes')
i('drawing','lower first grouping','short brace and curved leader from groupes')
i('text','lower first line','les ths relatifs aux VA')
i('text','lower Picard paragraph','les ths genx... pointus/partiels... étude qualitative... critère de lissité de Mumford')
i('margin note','lower left middle label','dans Chapitre sur Picard')
i('drawing','lower middle grouping','long brace, top just below second les, bottom beside quoted line')
i('text','lower question','(?) Picard d’un schéma projectif... pinceau de sections hyperplanes')
i('deletion','lower question opening','uncertain Relation entre')
i('insertion','above cancelled opening','Étude du')
i('text','lower quoted line','Les th. sur Picard genre certines/certaines équivalences/équivalence, double quotes')
i('margin note','lower left final label','dans Chap. sur pi_1/pi')
i('drawing','last grouping','short left brace')
i('text','last lines','Les formulations de descente à la van Kampen etc, en termes de groupe fondamental')
commit(26,5,dict(text=T,changes=L,inventory=I,sheet_kind='text',hand='his hand',observations='Whole and both supplied halves personally viewed before C/H, then every word compared line by line. All disagreements, C doubts, mathematical symbols, cancellations and marginal/slanted notes enlarged; slight slants rotated upright, recorded in crop_manifest. All crop26_005.py outputs viewed. Repeated ellipses and exact final dots checked, archive4 comment only. Grey reverse-side typescript show-through is not a second live text on this side. No watermark added. No context opened.'))
