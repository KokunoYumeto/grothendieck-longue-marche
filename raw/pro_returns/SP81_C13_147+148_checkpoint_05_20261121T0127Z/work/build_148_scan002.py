import json
from pathlib import Path

BASE = Path('/workspace/scratch/15c7af26487b/edition')
PAGE = '148_scan002'
F = {}
F['opening'] = r'''Soit $X$ surf. à bord compacte orientée, à
\begin{tikzpicture}[baseline=(torique.base)]
\node[anchor=west,inner sep=1pt] (torique) at (0,0) {structure torique};
\node[anchor=south west,inner sep=2pt,align=left] (torusnote) at (-.25,.5)
{\inserted{\begin{tabular}{@{}l@{}}(i.e. torseur sous\\
\quad$\mathbb U=\{z\in\mathbb C\mid |z|=1\}$)\end{tabular}}};
\draw (torusnote.north west) to[out=210,in=180] (torusnote.south west)
 -- (torusnote.south east) to[out=0,in=100] (4.2,-.35)
 to[out=50,in=-30] (torique.east);
\end{tikzpicture}
donnée sur les comp. connexes du bord.
On définit'''
F['definition'] = r'''\[
\begin{aligned}
\operatorname{SRT}(\unsure{X})={}&
\text{quotient du groupe des autom de }X
\text{ (\deleted{\unsure{en}} resp. l'orientation}\\
&\text{et les structures toriques) par la comp. neutre du}\\
&\text{sous-groupe }\operatorname{Aut}^!(\vec X)
\deleted{\unsure{\mathrm{bijec.}}}
\text{ de Aut qui induit}\\
&\text{l'identité sur }\partial X
\end{aligned}
\]'''
F['devissage'] = r'''On a ainsi un dévissage de $\operatorname{SRT}(X)$ en trois étages'''
F['first_stages'] = r'''\[
\underbrace{S_{\unsure{*}}T^!(X)}_{
\operatorname{Aut}^!(\unsure{\vec X|\overline X})/
\text{comp. neutre}}
\qquad\mathbb U^I\qquad\unsure{\mathfrak S_I}
\qquad I=\pi_0(\partial X)
\]'''
F['second_stages'] = r'''\[
\mathbb Z^I\qquad T(X)\qquad\mathbb U^I\qquad\unsure{\mathfrak S_I}
\]'''
F['can_droit'] = r'''En fait, on définit can! un sous-groupe
\begin{tikzpicture}[baseline=(ri.base)]
\node[inner sep=1pt] (ri) at (0,0) {$\mathbb R^I$};
\node[anchor=south] at (-.1,.55) {\inserted{droit}};
\draw (-.7,.55) .. controls (-.55,.4) and (-.2,.55) .. (-.1,.25)
 .. controls (-.05,.5) and (.35,.45) .. (.55,.63);
\end{tikzpicture}
de $\operatorname{SRT}(X)$
contenant $\mathbb Z^I$, de telle façon qu'on ait'''
F['kernel'] = r'''\[
\underbrace{\operatorname{SRT}^!(X)}_{
\substack{\text{noyau de}\\
\operatorname{SRT}^!(\alpha)\to\unsure{\mathfrak S_I'|\mathfrak S_I^!}}}
=\mathbb R^I.S_*T^!(X)
\]'''
F['small_diagram'] = r'''\diagram{
\begin{tikzpicture}[x=1cm,y=1cm]
\node (r) at (0,1.85) {$\mathbb R^I$};
\node (z) at (0,0) {$\mathbb Z^I$};
\node (p) at (2.4,1.85) {$\mathord{:}$};
\node (st) at (2.4,0) {$S_*T^!$};
\node at (3.5,0) {$\subset$};
\node at (4.55,0) {$\operatorname{SRT}^!$};
\node at (5.5,0) {$\subset$};
\node at (6.35,0) {$\operatorname{SRT}$};
\draw (.72,2.12) .. controls (.53,1.94) and (.51,1.84) .. (.64,1.84)
 -- (1.95,1.84);
% The upper end of this left stroke merges with cancelled lettering and a diagonal.
\draw (0,.43) -- (0,1.46);
\draw (0,1.46) .. controls (-.02,1.61) and (.08,1.69) .. (.18,1.56)
 .. controls (.24,1.47) and (.13,1.45) .. (0,1.46);
\draw (-.21,1.18) -- (.72,1.83);
\node[anchor=east] at (-.24,1.62) {$\unsure{\phantom{\uparrow}}$};
\draw (0,.43) .. controls (.0,.24) and (.18,.44) .. (.3,.53);
\node[anchor=west] at (.45,.94) {cocart};
\node[anchor=west] at (-.6,1.47) {\deleted{\unsure{et propre}}};
\draw[->] (.55,0) -- (1.88,0);
\draw (.76,.18) .. controls (.52,.15) and (.51,.0) .. (.55,0);
\draw[->] (2.4,.43) -- (2.4,1.45);
\draw (2.4,.43) .. controls (2.4,.25) and (2.63,.43) .. (2.72,.58);
% The following two source strokes have an unresolved reading (lambda / crossed 2).
\draw (2.98,1.61) -- (3.87,.61);
\draw (3.23,1.6) .. controls (3.53,1.78) and (3.49,1.12) .. (3.49,1.12)
 -- (3.77,1.12);
\node[anchor=west] at (3.91,1.12) {$\unsure{\phantom{\lambda}}$};
\end{tikzpicture}
}'''
F['right_nb'] = r'''\margin{\uline{NB} $\operatorname{SUT}(X)\simeq
T(X)\times_{\unsure{\mathfrak S_I}}\operatorname{Aut}((T_i)_{i\in I})$}'''
F['left_note'] = r'''\margin{Jusqu'ici on ne fait intervenir
que $S_*T^!(X)$, à l'exclusion de $S_*T(X)$,
dont la défini. exige une str. suppl.
$\uline{s}$, cf ci-dessous}'''
F['lattice'] = r'''\diagram{
\begin{tikzpicture}[x=1cm,y=1cm]
\node (top) at (0,2.45) {$\operatorname{SRT}(X)$};
\node (mid) at (0,1.25) {$\mathbb R^I.\unsure{S_*T^!}$};
\node (left) at (-1.75,0) {$\mathbb R^I$};
\node (right) at (1.7,0) {$S_*T^!(X)$};
\node (bottom) at (0,-1.2) {$\mathbb Z^I$};
\draw (top.south) -- (mid.north) node[midway,right] {$\unsure{\mathfrak S_I}$};
\draw (mid.south west) -- (left.north east) node[midway,above left] {$T^!$};
\draw (mid.south east) -- (right.north west) node[midway,above right] {$\mathbb U^I$};
\draw (left.south east) -- (bottom.north west) node[midway,below left] {$\mathbb U^I$};
\draw (bottom.north east) -- (right.south west) node[midway,below right] {$T^!(X)$};
\draw (-1.3,2.58) .. controls (-1.65,2.45) and (-1.75,2.02) .. (-2.05,1.87)
 .. controls (-2.16,1.79) and (-2.27,1.86) .. (-2.29,1.94)
 .. controls (-2.24,1.66) and (-2.74,1.32) .. (-2.97,1.08);
\node[anchor=east] at (-2.1,2.22) {$T(X)$};
\draw (1.18,2.5) .. controls (1.48,2.51) and (1.37,2.06) .. (1.77,1.99)
 .. controls (1.89,1.96) and (1.99,2.05) .. (2.04,2.08)
 .. controls (1.92,1.75) and (2.44,1.45) .. (2.47,1.13);
\node[anchor=south west] at (1.48,2.45) {$\operatorname{Aut}((T_i)_{i\in I})$};
\end{tikzpicture}
}'''
F['quotient'] = r'''d'où
\diagram{
\begin{tikzpicture}[x=1cm,y=1cm]
\node (quot) at (0,0) {$\operatorname{SRT}\deleted{(X)}/\mathbb Z^I
 \overset{\text{déf}}=\operatorname{SUT}(X)$};
\node (prod) at (-.85,-1.1) {$T^!(X)\times\mathbb U^I$};
\draw[->] (-1.2,-.3) -- (-1.2,-.78);
\node at (1.42,-.62) {$\Big\}\ \unsure{\mathfrak S_I}$};
\draw (-3.0,-1.52) .. controls (-2.4,-1.6) and (-2.0,-1.54) .. (-1.62,-1.51)
 .. controls (-1.44,-1.71) and (-.92,-1.6) .. (-.4,-1.51)
 .. controls (.13,-1.64) and (.48,-1.64) .. (1.1,-1.45)
 .. controls (1.52,-1.41) and (1.85,-1.47) .. (2.0,-1.47);
\end{tikzpicture}
}'''
F['sequence'] = r'''\[
(*)\qquad1\longrightarrow\mathbb U^I\longrightarrow
\operatorname{SUT}(X)\longrightarrow
\unsure{\deleted{\mathfrak S}T|T}(X)-1
\]'''
F['marquage'] = r'''De plus, chaque fois qu'on se donne un
marquage, i.e. un pt \deleted{\unsure{de}}'''
F['product'] = r'''\[
\uline{s}=(s_i)\in
\prod_{i\in I=\pi_0(\partial X)}
\deleted{\unsure{\mathbb U_i}}T_i
\]'''
F['boundary_note'] = r'''\margin{$T_i=$ comp. connexe (torique) de
$\partial X$ d'indice $i$\par\hspace{1.1cm}$\unsure{i}$}'''
F['embedding'] = r'''on trouve un plongement
\[
S_*T^{\deleted{\unsure{!}}}(X,\uline{s})\hookrightarrow\operatorname{SRT}(X)
\]
tel qu'on en \unsure{déduise|déduire}'''
F['last_formula'] = r'''\[
S_*T^{\deleted{\unsure{!}}}(X,\uline{s})
\mathbin{\wedge}_{\mathbb Z^I}\mathbb R^I
\simeq\operatorname{SRT}(X)
\]'''

parts = [r'''\cotefile{148}
\scanpage{2}

\margin{(29.11.83)}''',F['opening'],F['definition'],F['devissage'],F['first_stages'],
         'ou encore',F['second_stages'],F['can_droit'],F['kernel'],F['small_diagram'],
         'i.e. on a',F['right_nb'],F['left_note'],F['lattice'],F['quotient'],F['sequence'],
         F['marquage'],F['product'],F['boundary_note'],F['embedding'],F['last_formula'],r'''\margin{1}''']
(BASE/'work'/f'{PAGE}.tex').write_text('\n\n'.join(parts)+'\n',encoding='utf-8')

BOX = {
 'definition':[215,318,1668,532], 'devissage':[213,548,1649,631],
 'first_stages':[532,625,1340,800], 'second_stages':[477,807,992,892],
 'can_droit':[188,863,1675,1006], 'kernel':[1219,1001,1672,1216],
 'small_diagram':[181,1115,835,1373], 'right_nb':[1251,1182,1666,1421],
 'left_note':[15,1395,532,1981], 'lattice':[465,1406,1110,1767],
 'quotient':[970,1452,1634,1700], 'sequence':[932,1696,1665,1767],
 'marquage_complete':[210,1748,1420,1944], 'product_complete':[620,1876,1140,2028],
 'boundary_note':[1261,1880,1671,2050], 'embedding':[214,2026,1657,2203],
 'last_formula':[432,2199,1118,2323], 'torus_insertion':[1120,27,1668,204],
 'lower_number':[25,2279,84,2343]
}

R = dict(page=PAGE,reader='reader_b',line_count=21,
 layout='One upright sheet with 21 principal prose/display baselines, counting the lower row of the upper small drawing with its following prose and excluding subsidiary annotation lines and internal drawing rows. The dated left margin faces the first sentence; an outlined supralinear explanation joins structure torique. Four definition baselines follow. Two stage rows, an inserted droit, and a kernel annotation occupy the upper middle. A small subgroup drawing stands at left, followed by a larger lattice with two braces, diagonal notes on both sides, and a quotient drawing at right. The lower paragraph has a product, a right boundary note, two formulas with struck superscripts, and a lighter lower-left number. Reading order follows the upright prose; diagonal marginal material remains marginal.',
 changes=[], decisions=[], unnumbered_decisions=[], inventory=[], doubts=[], notation=[],
 abbreviations=[], hand=[], notes='',check_events=[], second_boxes=[],diff_coverage=[],deletion_insertion_check='')

def change(n,place,c,h,final,evidence,key,confidence,kind,sheet,dc,dh,mh=False,conseq=False):
    R['changes'].append(dict(id=f'{PAGE}-{n:02}',place=place,C=c,H=h,final=final,
        evidence=f'{evidence} Crop {PAGE}_{key}.png, original box {BOX[key]}.',
        crop=f'{PAGE}_{key}.png',box=BOX[key],confidence=confidence,kind=kind,
        error_sheet_kind=sheet,differs_C=dc,differs_H=dh,marked_in_H=mh,consequential=conseq))

change(1,'L04, definition first baseline',
 r'''autom de $X$ (\deleted{\unsure{en}} resp. l'orientation''',
 r'''autom.\ de $X$ (\uncertain{respectant} l'orientation''',
 r'''autom de $X$ (\deleted{\unsure{en}} resp. l'orientation''',
 'The abbreviation ends after the short descending p and a dot. A compact cancelled word precedes it. No separate period is visible after autom. The cancelled letters remain doubtful.',
 'definition','high','abbreviation expanded or spelling modernised','Abbreviations expanded, spelling modernised',False,True,True)
change(2,'L06, cancelled word after Aut',
 r'''\deleted{\unsure{\mathrm{bijec.}}}''',r'''\struck{\ill{}}''',r'''\deleted{\unsure{\mathrm{bijec.}}}''',
 'The strike crosses an initial tall b-like stroke and a dotted descending j-like stroke. The remaining connected letters and terminal punctuation are not all clear; bijec. is retained as a candidate, with the whole word cancelled.',
 'definition','low',r'''readable ink left as \ill{}''','Readable ink left as illegible',False,True,True)
change(3,'L08, sentence introducing the stages',r'''un \unsure{dévissage}''',r'''une \uncertain{filtration}''',r'''un dévissage''',
 'After un, the word begins with a looped d and short accented e; the middle has the repeated low strokes of viss, and the ending has a descending g loop. The source has no terminal e after un.',
 'devissage','high','misread word','Words',False,True,True)
change(4,'L11, abbreviation before un sous-groupe',r'''can!''',r'''canon.\ ''',r'''can!''',
 'The visible baseline letters are c-a-n, followed by a raised upright and a separate dot. No second o-n sequence is written.',
 'can_droit','high','abbreviation expanded or spelling modernised','Abbreviations expanded, spelling modernised',False,True)
change(5,'Kernel annotation beneath L12, argument',r'''\operatorname{SRT}^!(\unsure{\alpha|X})''',
 r'''SRT^{!}(X)''',r'''\operatorname{SRT}^!(\alpha)''',
 'The argument has a closed left loop with a right diagonal crossing and short lower-right tail. The ordinary X immediately above has two open crossing strokes. The closed loop is preserved as alpha.',
 'kernel','high','misread symbol or index','Symbols and indices',False,True,False,True)
change(6,'Kernel annotation beneath L12, terminal raised stroke',
 r'''\unsure{\mathfrak S_I^!|\mathfrak S_I'}''',r'''\mathfrak S_I^! [H note: ! read without certainty]''',
 r'''\unsure{\mathfrak S_I'|\mathfrak S_I^!}''',
 'One detached raised stroke is visible to the right of the looped group letter. A separate lower dot is not clear. The prime is placed first, while the exclamation reading and the identity of the looped letter remain doubtful.',
 'kernel','medium','misread symbol or index','Symbols and indices',True,True,True,True)
change(7,'Upper small subgroup drawing, including its crossed material',
 r'''\mathbb R^I & \mathord{:}\arrow[l,phantom,"\subset"']\arrow[dr,no head,"\unsure{\lambda}"] &&\\ \mathbb Z^I\arrow[u,"\text{cocart}"']\arrow[r,hook]&S_*T^!\arrow[u,hook]\arrow[r,phantom,"\subset"]&\operatorname{SRT}^!\arrow[r,phantom,"\subset"]&\operatorname{SRT}; \margin{\deleted{\unsure{et propre}}}''',
 r'''\note{à gauche, un petit diagramme : $\mathbf{R}^{I}$ en haut, une flèche d'inclusion, un trait biffé, une flèche verticale marquée « \uncertain{cocart} », et un point ; puis la ligne ci-dessous} $\mathbf Z^I\hookrightarrow S_*T^!\subset SRT^!\subset SRT$''',
 F['small_diagram'],
 'There are two vertically separated dots and a long upper horizontal stroke with a curved left end. At the bottom of the left vertical, the stem bends right and returns upward in a continuous exposed curve, matching the geometry of the right vertical’s lower return. At the top, the left stem meets a small rounded loop at the cancellation line; a diagonal segment crosses from lower left to upper right through this area. The crossed text conceals their junction, so an independent arrowhead cannot be securely traced. That upper junction is reproduced by its exposed loop and diagonal, with an in-place doubt marker and no categorical arrowhead. The right vertical’s upper pointed end is exposed. The separate oblique stroke and curved, footed stroke farther right are also drawn directly; whether they form a labelled diagonal or a cancelled glyph remains open. The cancelled phrase stays beside the left vertical, with its letters doubtful.',
 'small_diagram','medium','drawing or diagram','Drawings and diagrams',True,True,True,True)
change(8,'Left diagonal marginal note',
 r'''\unsure{jusqu'ici on ne fait intervenir} que $S_*T^!(X)$; à l'exclusion de $S_*T(X)$, dont la défini. exige une str. suppl. $\uline{s}$, cf ci-dessous''',
 r'''Jusqu'ici on a fait intervenir $S_*T^{!}(X)$, i.e.\ \uncertain{l'exclusion} \ill{} de la définition $T(X)$ \ill{} $S_*T(X)$, str.\ \ill{}. \ill{}''',
 F['left_note'],
 'The rotated crop exposes Jusqu’ici on, then ne fait intervenir, que followed by the first group, à l’exclusion, de followed by the second group, dont la défini., exige une str. suppl., and the underlined s with cf ci-dessous. The first letter is tall J; after the first parenthesis the visible descending punctuation is retained as a comma.',
 'left_note','high',r'''readable ink left as \ill{}''','Readable ink left as illegible',True,True,True,True)
change(9,'Left brace and label beside the large lattice',
 r'''\margin{$T(X)\left\{\vphantom{\begin{matrix}a\\a\\a\end{matrix}}\right.$}''',
 r'''[no left T(X) brace in H; H describes only the right Aut brace]''',
 F['lattice'],
 'The left of the top two lattice levels has a long, bent brace and the complete label T(X). The right Aut label and brace are also present. Their source attachments are drawn with the lattice. C already records both labels and braces; its separate margin wrappers are treated as layout syntax.',
 'lattice','high','omission','Omissions',False,True,False,True)
change(10,'Quotient drawing following d’où',
 r'''\operatorname{SRT}\deleted{(X)}/\mathbb Z^I\overset{\mathrm{def}}=\operatorname{SUT}(X)\arrow[d,"\unsure{\mathfrak S_I}"]\\T^!(X)\times\mathbb U^I''',
 r'''SRT/\mathbf Z^I\overset{\mathrm{def}}=SUT(X)\quad\big\rbrace\ \mathfrak S_I; \note{sous $SUT(X)$, une flèche vers le bas et « $T^{!}(X)\times\mathbb U^I$ », surmonté d’une accolade}''',
 F['quotient'],
 'The parentheses and X between SRT and the slash are crossed. An accent stroke stands over the e of déf. The downward arrow lies under the left quotient, while a separate right brace precedes the looped group label. A long shallow wavy stroke lies below the lower product. These positions are reproduced; the looped letter remains doubtful.',
 'quotient','high','drawing or diagram','Drawings and diagrams',True,True,False,True)
change(11,'Display (*), overworked letter before (X)',r'''T(X)''',r'''T(X)''',
 r'''\unsure{\deleted{\mathfrak S}T|T}(X)''',
 'A dark upright and top bar form the foreground T, while exposed curved strokes run around its left and upper-right sides. A looped group letter beneath T is possible; heavy retracing of T is also possible. The alternative retains that uncertainty instead of silently discarding the extra contours.',
 'sequence','low','deletion state','Struck text',True,True,False,True)
change(12,'Display (*), terminal connector',r'''T(X)-1''',r'''T(X)\to1''',r'''\unsure{\deleted{\mathfrak S}T|T}(X)-1''',
 'The final connector is a short horizontal stroke with a blunt right end. The preceding three connectors have separate pointed ends. The handwritten terminal 1 is retained.',
 'sequence','high','misread symbol or index','Symbols and indices',False,True,False,True)
change(13,'L17, cancelled word following un pt',r'''un pt \deleted{\unsure{de}}''',r'''un pt de''',r'''un pt \deleted{\unsure{de}}''',
 'A thick horizontal cancellation runs across the small word after pt. A short ascender survives at its beginning, but the two individual letters are obscured. The cancellation is clear and the candidate de remains doubtful.',
 'marquage_complete','high','deletion state','Struck text',False,True)
change(14,'L18, cancelled object before T_i',r'''\deleted{\unsure{\mathbb U_i}}T_i''',
 r'''T_i; \note{après le produit, un mot biffé illisible}''',r'''\deleted{\unsure{\mathbb U_i}}T_i''',
 'The hatching covers a rounded double-stemmed form and a small lowered mark immediately before the exposed T_i. The candidate U_i remains uncertain; all hatching belongs to the preceding object and leaves the final T_i live.',
 'product_complete','low',r'''readable ink left as \ill{}''','Readable ink left as illegible',False,True,True)
change(15,'Right boundary note, placement and enclosing punctuation',
 r'''\margin{$T_i=$ comp. connexe (torique) de $\partial X$ d'indice $i$}''',
 r'''($T_i$ = comp.\ connexe (torique) de $\partial X$ d'indice $i$),''',
 r'''\margin{$T_i=$ comp. connexe (torique) de $\partial X$ d'indice $i$}''',
 'The note occupies three short right-margin lines. Parentheses enclose torique only; no outer opening before T_i or terminal closing after the last i is visible.',
 'boundary_note','high','insertion or placement','Insertions put in the wrong place',False,True)
change(16,'Small dotted glyph below the right boundary note',r'''[no transcription]''',r'''[no transcription]''',
 r'''$\unsure{i}$ [below d'indice]''',
 'Below the d’indice line is a dark small looped upright with a separate dot. It may be an i or a correction to that portion of the line; its attachment is unmarked. It is retained on a separate lower line as a doubtful glyph.',
 'boundary_note','low','omission','Omissions',True,True)
change(17,'L20, first final formula superscript',r'''S_*T^{\deleted{\unsure{!}}}(X,\uline{s})''',
 r'''S_*T^!(X,\underline{s}) [H note: exponent overworked and read ! without certainty]''',
 r'''S_*T^{\deleted{\unsure{!}}}(X,\uline{s})''',
 'Several short diagonal black strokes cross the small superscript. The surrounding T and opening parenthesis stay exposed. The superscript is retained as cancelled; the original ! remains a doubtful reading.',
 'embedding','high','deletion state','Struck text',False,True,True,True)
change(18,'L20, prose after the embedding',r'''tel qu'on en déduise''',
 r'''tel qu'on \ill{} \uncertain{en déduire}''',r'''tel qu'on en \unsure{déduise|déduire}''',
 'The phrase tel qu’on en is present without a separate unreadable intervening word. The last verb has d-é-d-u-i followed by a low connected ending. That ending favors the first reading but does not securely distinguish s from r in this hand.',
 'embedding','medium','misread word','Words',False,True,True)
change(19,'L21, final formula superscript',r'''S_*T^{\deleted{\unsure{!}}}(X,\uline{s})''',
 r'''S_*T^!(X,\underline{s}) [H note: exponent overworked and read ! without certainty]''',
 r'''S_*T^{\deleted{\unsure{!}}}(X,\uline{s})''',
 'The raised place is filled with a separate vertical zigzag of cancelling strokes. Its extent stops before the opening parenthesis; the proposed underlying ! remains doubtful.',
 'last_formula','high','deletion state','Struck text',False,True,True,True)
change(20,'L21, index beneath the wedge',r'''\mathbin{\wedge}_{\mathbb Z^I}''',
 r'''\wedge^{\mathbf Z^I} [H note itself says the index is under the sign]''',r'''\mathbin{\wedge}_{\mathbb Z^I}''',
 'The full Z^I is lower than the wedge and between the two group factors. H’s body sets a superscript, although its editorial description records the lower position.',
 'last_formula','high','misread symbol or index','Symbols and indices',False,True,False,True)
change(21,'Lower-left lighter marginal number',r'''\margin{1}''',r'''[no transcription]''',r'''\margin{1}''',
 'A lighter single numeral with an ascending lead-in and long descending stem occupies the lower-left corner. It reads 1 and is kept in the margin convention.',
 'lower_number','high','omission','Omissions',False,True)
change(22,'L07, end of the definition',r'''l'identité sur $\partial X$''',r'''l'identité sur $\partial X$.''',r'''l'identité sur $\partial X$''',
 'After the final crossed strokes of X, the baseline is blank. No separate period is exposed at the end of this definition.',
 'definition','high','text not on the page','Text that is not on the page',False,True)

def decision(mid,status,reading,evidence,key,confidence):
    R['decisions'].append(dict(id=mid,decision=status,reading=reading,evidence=evidence,
        crop=f'{PAGE}_{key}.png {BOX[key]}',confidence=confidence))
decision('M0036','undecided',r'''\unsure{X}''','The two oblique strokes of X are visible, but dark horizontal retracing at their crossing prevents a clean reading of the full overwritten form.','definition','medium')
decision('M0037','first','dévissage','The initial looped d, accented e, repeated low middle strokes, and descending g are exposed on the complete baseline.','devissage','high')
decision('M0038','undecided',r'''S_{\unsure{*}}T^!(X)''','The lower mark is dark and pointed, but its arms are merged. Other stars on this sheet do not recover the hidden arms of this occurrence.','first_stages','medium')
decision('M0039','undecided',r'''\operatorname{Aut}^!(\unsure{\vec X|\overline X})''','The short overhead stroke has a thickened right tip; the image does not separate an arrowhead from a terminal ink accumulation.','first_stages','medium')
for mid,key in [('M0040','first_stages'),('M0041','second_stages'),('M0045','right_nb'),('M0047','lattice'),('M0049','quotient')]:
    decision(mid,'undecided',r'''\unsure{\mathfrak S_I}''','The open outer loop and inward lower curl recur on this sheet with a lowered I. They are retained as the proposed fraktur S form, but the exact letter/alphabet is not independently settled by its strokes. The whole formula or drawing was inspected.',key,'medium')
decision('M0042','first',r'''\alpha''','A closed left loop and right crossing/tail are visible inside the parentheses, in contrast to the open crossed X written immediately above.','kernel','high')
decision('M0043','undecided',r'''\unsure{\mathfrak S_I'|\mathfrak S_I^!}''','Only one detached raised stroke is exposed. A distinct exclamation dot is not clear; prime is therefore first while both proposed readings remain.','kernel','medium')
decision('M0044','undecided',r'''\unsure{\lambda|2}; the two strokes are reproduced directly in the drawing''','The oblique stroke meets a curved upper stroke with a short right foot. The image allows a label crossing an oblique segment or a cancelled glyph. The drawing retains both strokes and an in-place doubt marker without choosing their function.','small_diagram','low')
decision('M0046','other',"Jusqu'ici on ne fait intervenir",'The rotated marginal baseline exposes the tall initial J, the top-line on, and the separate next-line ne before the looped f of fait. The rest of intervenir is visible across the next connected strokes.','left_note','high')
decision('M0048','undecided',r'''\mathbb R^I.\unsure{S_*T^!}''','The S and T with raised upright-and-dot are visible, but the star/subscript area merges into a heavy dark stroke and the vertical segment from above.','lattice','medium')
R['decisions'].sort(key=lambda d:d['id'])

for place,reading,key,reason in [
 ('L04, struck word before resp.',r'''\deleted{\unsure{en}}''','definition','The cancellation hides both small letter interiors.'),
 ('L06, struck word after Aut',r'''\deleted{\unsure{\mathrm{bijec.}}}''','definition','Some b/j-like strokes survive, but the complete letters and punctuation are not exposed.'),
 ('Upper small drawing, struck phrase',r'''\deleted{\unsure{et propre}}''','small_diagram','A heavy horizontal strike and an upright diagram segment obscure the central letters.'),
 ('L17, struck word after pt',r'''\deleted{\unsure{de}}''','marquage_complete','The strike masks the short word; its initial ascender survives.'),
 ('L18, struck object before T_i',r'''\deleted{\unsure{\mathbb U_i}}''','product_complete','Hatching crosses the double-stemmed rounded form and its lower mark.'),
 ('L20, struck exponent',r'''^{\deleted{\unsure{!}}}''','embedding','Cancellation is visible; the original isolated exponent is hidden.'),
 ('L21, struck exponent',r'''^{\deleted{\unsure{!}}}''','last_formula','The thick zigzag cancellation hides the original raised sign.')]:
    R['unnumbered_decisions'].append(dict(place=place,decision='undecided',reading=reading,
        evidence=reason,crop=f'{PAGE}_{key}.png {BOX[key]}',confidence='low'))

inv = [
 ('margin note','Upper-left oblique date','(29.11.83)'),
 ('text','Top three principal baselines','Soit X surf. à bord; donnée sur les comp.; On définit'),
 ('insertion','Above structure torique, outlined and joined to that phrase','(i.e. torseur sous U={z∈C | |z|=1})'),
 ('display','Four-baseline definition','SRT(X)=quotient du groupe des autom de X'),
 ('deletion','Definition first baseline','en before resp.'),
 ('deletion','Definition third baseline','bijec. after Aut^!(vec X)'),
 ('text','Stage introduction and far-right continuation','On a ainsi un dévissage; ou encore'),
 ('display','First stage row, with lower Aut annotation','S_*T^!(X), U^I, looped group letter with I; I=pi_0(∂X)'),
 ('display','Second stage row','Z^I, T(X), U^I, looped group letter with I'),
 ('text','Two baselines below stage rows','En fait, on définit can!; contenant Z^I'),
 ('insertion','Above R^I in the first of those baselines','droit with a shallow attachment brace'),
 ('display','Right end of contenant baseline and its annotation','SRT^!(X)=R^I.S_*T^!(X); noyau de SRT^!(alpha) to looped letter'),
 ('diagram','Upper small left drawing','R^I, colon, Z^I, S_*T^!, SRT^!, SRT; cocart'),
 ('deletion','Across upper-left part of the small drawing','et propre, doubtful'),
 ('drawing','Upper-right part of the small drawing','Oblique stroke and curved footed stroke, unresolved reading'),
 ('text','Right of small drawing','i.e. on a'),
 ('margin note','Right diagonal note','Underlined NB; SUT(X)≃T(X)×_S Aut((T_i)_{i∈I})'),
 ('margin note','Left diagonal note','Jusqu’ici on ne fait intervenir que S_*T^!(X)'),
 ('diagram','Large central lattice including both braces','SRT(X), R^I.S_*T^!, R^I, S_*T^!(X), Z^I; T(X), Aut((T_i)_{i∈I})'),
 ('text','Beside the central lattice','d’où'),
 ('diagram','Right quotient drawing and lower wavy stroke','SRT deleted (X)/Z^I =déf SUT(X), downward arrow, T^!(X)×U^I, brace and looped letter'),
 ('deletion','Within quotient expression','(X) after SRT'),
 ('display','Sequence beneath the quotient drawing','(*), 1→U^I→SUT(X)→overworked T(X)-1'),
 ('deletion','Overworked letter in sequence, status doubtful','Possible underlying looped group letter beneath T'),
 ('text','Two lower prose baselines','De plus, chaque fois qu’on se donne un marquage, i.e. un pt'),
 ('deletion','After un pt','de, doubtful'),
 ('display','Product display','underlined s=(s_i)∈product_{i∈I=pi_0(∂X)} deleted U_i T_i'),
 ('deletion','Before exposed T_i in product','U_i, doubtful'),
 ('margin note','Right of product','T_i=comp. connexe (torique) de ∂X d’indice i; small dotted glyph below'),
 ('text','Lower continuation','on trouve un plongement; tel qu’on en déduise/déduire'),
 ('display','First final formula','S_*T with cancelled exponent (X,underlined s) hooks into SRT(X)'),
 ('deletion','Exponent in first final formula','!, doubtful'),
 ('display','Final formula','S_*T with cancelled exponent (X,underlined s) wedge_{Z^I}R^I≃SRT(X)'),
 ('deletion','Exponent in final formula','!, doubtful'),
 ('margin note','Lower-left lighter number','1')
]
for i,(kind,pos,words) in enumerate(inv,1):
    R['inventory'].append(dict(sheet_kind='text',hand='unattributed lighter hand' if i==35 else 'his hand',
        element=f'E{i:02}',kind=kind,position=pos,first_words_or_objects=words,transcribed='yes'))

def doubt(place,reading,alts,reason,conf='medium'):
    R['doubts'].append(dict(place=place,reading=reading,alternatives=alts,confidence=conf,reason=reason))
doubt('L04 definition argument',r'''\unsure{X}''','X; unidentified retracing','The crossed letter has additional heavy horizontal strokes.')
doubt('L04 struck word',r'''\deleted{\unsure{en}}''','en; unreadable cancelled word','Letter interiors are hidden by cancellation.','low')
doubt('L06 struck word',r'''\deleted{\unsure{\mathrm{bijec.}}}''','bijec.; other abbreviation','The final connected letters and punctuation remain covered.','low')
doubt('First stage, subscript',r'''S_{\unsure{*}}T^!(X)''','star; unclassified small mark','The dark pointed subscript has merged arms.')
doubt('First stage, Aut argument decoration',r'''\unsure{\vec X|\overline X}''','short arrow; bar','Its right tip is too thick to distinguish arrowhead from an ink accumulation.')
doubt('Five group-letter occurrences and the kernel target',r'''\unsure{\mathfrak S_I}''','proposed fraktur S; another looped capital','The repeated outer curve and lower return are visible, but this page alone does not securely fix the alphabet.')
doubt('Kernel target raised stroke',r'''\unsure{\mathfrak S_I'|\mathfrak S_I^!}''','prime; exclamation','A raised stroke survives without a clearly separate dot.')
doubt('Small drawing, crossed/diagonal glyph',r'''\unsure{\lambda|2}''','lambda label crossing a segment; cancelled 2-like glyph','Directly reproduced strokes have an unresolved function.','low')
doubt('Small drawing, left upper endpoint','directly drawn rounded loop and crossing diagonal at the upper junction','arrowhead merged into cancelled lettering; letter loop and overlapping diagonal','The left vertical ends in a rounded loop at the strike line. A diagonal crosses the same area, and the cancelled text conceals their junction. A separate pointed head cannot be traced securely; the exposed strokes are drawn with a doubt marker.','low')
doubt('Small drawing, crossed phrase',r'''\deleted{\unsure{et propre}}''','et propre; other phrase','The strike and vertical segment cover multiple letters.','low')
doubt('Large lattice central object',r'''\mathbb R^I.\unsure{S_*T^!}''','S_*T^!; unclear lower mark','The star area merges into the S and the upper vertical stroke.')
doubt('Sequence (*), overworked letter',r'''\unsure{\deleted{\mathfrak S}T|T}(X)''','underlying looped letter replaced by T; heavily retraced T','Additional exposed loops are present, but their previous identity and replacement state remain uncertain.','low')
doubt('After un pt',r'''\deleted{\unsure{de}}''','de; another short word','The cancellation is clear; its letters are obscured.','low')
doubt('Product before T_i',r'''\deleted{\unsure{\mathbb U_i}}''','U_i; other rounded indexed object','Dense hatching obscures both the main object and the index.','low')
doubt('Below boundary note',r'''\unsure{i}''','i; another small dotted glyph; correction to the preceding word','A separate dotted looped upright is visible, without an attachment mark.','low')
doubt('Embedding superscript',r'''\deleted{\unsure{!}}''','cancelled !; another cancelled raised sign','Crossing strokes obscure the underlying glyph.','low')
doubt('Final prose verb',r'''\unsure{déduise|déduire}''','déduise; déduire','The short connected s/r position remains ambiguous.')
doubt('Last formula superscript',r'''\deleted{\unsure{!}}''','cancelled !; another cancelled raised sign','A dark zigzag hides the original raised symbol.','low')

R['notation'] = [
 dict(form=r'''\mathbb U=\{z\in\mathbb C\mid |z|=1\}''',meaning='The inserted explanation names this U and calls the boundary structure a torseur under it.',evidence='Upper-right inserted annotation; the modulus and handwritten 1 are visible.',scope='Inserted definition and each exposed U^I on this page.'),
 dict(form=r'''I=\pi_0(\partial X)''',meaning='This equality is written beside the stage row and again in the product index.',evidence='First-stage row; lower product.',scope='Both explicit equalities, including their lower zeros.'),
 dict(form=r'''\operatorname{SRT}(X),\operatorname{Aut}^!(\vec X)''',meaning='The page defines SRT by a written quotient paragraph involving the displayed Aut subgroup; the initial SRT argument remains overworked.',evidence='Four definition baselines.',scope='All clearly exposed SRT and Aut occurrences; underbrace vector/bar and kernel alpha are separately recorded.'),
 dict(form=r'''\operatorname{SUT}(X)''',meaning='The quotient drawing writes this name after the equals sign bearing déf.',evidence='Right quotient drawing, and the right NB note.',scope='All exposed SUT occurrences on this page.'),
 dict(form=r'''S_*T^!(X),S_*T(X),S_*T^{\deleted{\unsure{!}}}(X,\uline s)''',meaning='These written strings occur on this sheet. The left note mentions the first two, and the final two formulas have black cancellation at the superscript place; this entry records the source wording only.',evidence='Left marginal note and final formulas.',scope='Every exposed subscript star and superscript on this sheet; unresolved merged marks stay doubtful.'),
 dict(form=r'''\unsure{\mathfrak S_I}''',meaning='A recurring proposed letter form, used in stage rows, notes, and diagram labels; no alphabet identification is established.',evidence='Outer loop with inward lower curl and lowered I in six contexts.',scope='All six occurrences retained as doubtful, with the kernel raised stroke separately recorded.')
]
R['abbreviations'] = [dict(form=a,expansion=b) for a,b in [
 ('surf.','surface (tentative)'),('i.e.','id est (tentative)'),('comp.','composante(s) (tentative)'),
 ('autom','automorphismes (tentative)'),('resp.','respectant (tentative)'),('Aut','automorphismes (tentative)'),
 ('can!','canoniquement (tentative; literal punctuation retained)'),('NB','nota bene (tentative)'),
 ('défini.','définition (tentative)'),('str.','structure (tentative)'),('suppl.','supplémentaire (tentative)'),
 ('cf','confer (tentative)'),('déf','définition (tentative)'),('pt','point (tentative)')]]
R['hand'] = [
 dict(habit='The capital index I has broad top and bottom bars; lowercase i has a separate dot and descends to a lower index level.',places='Stage rows, group powers, product index, boundary note.',scope='All exposed I/i positions on this page checked; the additional tiny boundary glyph remains doubtful.',witness_errors='None asserted for an unambiguous I/i substitution.'),
 dict(habit='Several exclamation exponents have a conspicuous separated dot; cancellation zigzags in the final two superscript positions cover the original sign.',places='Aut^!, S_*T^!, SRT^!; two final formulas.',scope='Every raised ! position on the page examined individually.',witness_errors='H typesets the two cancelled final exponents as live !; kernel target remains doubtful.'),
 dict(habit='The recurring looped group letter has an outer open curve and inward lower return, so it can resemble more than one alphabetic capital.',places='Stage rows, kernel target, NB, lattice, quotient.',scope='All six forms on this page inspected; no global alphabet decision.',witness_errors='Both witnesses propose fraktur S; the transcription retains C’s doubt rather than resolving from that agreement.'),
 dict(habit='The subscript star can become a compact dark wedge or blot.',places='First stage, kernel product, small drawing, large lattice, final two formulas.',scope='All exposed S subscripts inspected; first stage and central lattice remain unresolved.',witness_errors='No resolved substitution asserted.'),
 dict(habit='Ordinary prose is often reduced to low connected strokes, while f, q, g and d preserve long loops or descenders.',places='dévissage; diagonal note; marquage; final verb.',scope='These page-specific word loci only.',witness_errors='H filtration, marginal omissions and expanded respectant; the final s/r ending remains doubtful.'),
 dict(habit='A horizontal terminal connector can have a blunt end where neighboring connectors have visible pointed ends.',places='Display (*).',scope='All four connectors in that display compared.',witness_errors='H supplies a right arrow at the final blunt stroke.')
]
R['notes'] = ('The manuscript dated (29.11.83) introduces a compact oriented surface with toric structures on its boundary components, '
 'and writes a quotient definition for SRT in L04–L07. It calls the next rows a dévissage, then introduces R^I with a supralinear droit '
 'and a kernel annotation whose argument is read alpha. The small subgroup drawing, the large lattice, the NB expression, and the quotient '
 'drawing are transcribed as source claims and drawings, with their indices and doubtful letter forms retained. Display (*) ends in a blunt dash '
 'before 1; its preceding T is visibly overworked, and the proposed underlying letter is uncertain. The lower paragraph speaks of a marquage, '
 'writes the product point, and gives two formulas with cancelled raised signs. This reading supplies no proof or new mathematical statement. '
 'The additional small dotted glyph below d’indice is retained without inventing an attachment. The top explanation and droit have their source '
 'attachment contours drawn; the two side braces remain with the lattice, and the quotient’s right brace and lower wavy stroke are preserved. '
 'Second-reading targets are localized complete formulas, coherent prose baselines, or single marginal passages; neutral scope labels explicitly '
 'exclude crossing context. Twenty-one crop files were viewed, covering nineteen physical loci. Two original crops were incomplete at unresolved '
 'descender/strike boundaries; completion files replace those two for the reading evidence. No decided locus was recropped. The whole sheet and both supplied halves were read line by line. No OCR, '
 'external source, other page, TeX compilation, or mathematical verification was used.')
R['notes'] += ('\n\nLegibility and witness comparison. The exposed upright prose is generally legible, but the initial SRT argument, '
 'cancelled definition words, first star, central lattice subscript, and final raised signs retain merged or covered strokes. The rotated '
 'left-note crop recovers a coherent sequence that C largely preserves: Jusqu’ici on ne fait intervenir, à l’exclusion, dont la défini., '
 'exige une str. suppl., and cf ci-dessous. H has substantial gaps in this passage. The devissage and can_droit crops support C’s dévissage '
 'and literal can!, while the definition crop supports resp. rather than H’s expansion respectant. H’s descriptions usefully record the '
 'small drawing and quotient brace, although their endpoint and placement details require comparison with the image. In the small_diagram '
 'crop, both lower vertical returns are exposed; the left upper junction remains obscured by cancelled lettering and a crossing diagonal, '
 'so the revised drawing preserves those strokes with an explicit doubt. The sequence crop exposes a blunt terminal connector and an '
 'overworked foreground T; the latter’s underlying identity stays open. Both witnesses leave the dotted glyph below d’indice unrecorded, '
 'and it is retained as doubtful after comparison with the boundary_note crop. Agreement on the recurring proposed fraktur letter does '
 'not settle its exact alphabetic form. The two final-formula crops show cancellation at the exponent positions that H’s formulas print '
 'as live signs. These comparisons apply to this sheet alone.')

def second(key,kind,reading,coords=None):
    vals=BOX[key] if coords is None else coords
    R['second_boxes'].append(dict(box=f"B{len(R['second_boxes'])+1:02}",kind=kind,
        x0=vals[0],y0=vals[1],x1=vals[2],y1=vals[3],reading=reading))
second('definition','Upper-left marginal annotation only; adjacent upright prose is context',r'''\margin{(29.11.83)}''',[18,61,181,239])
second('torus_insertion','Upper-right inserted annotation and its connector only; upright sentence is context',
 F['opening'][F['opening'].index(r'''\begin{tikzpicture}'''):F['opening'].index(r'''\end{tikzpicture}''')+len(r'''\end{tikzpicture}''')])
second('definition','Complete upper multiline formula, all baselines',F['definition'])
second('devissage','Complete upright baseline between the definition and displays',F['devissage'])
second('first_stages','Complete upper mathematical row with lower annotation and right-hand extension',F['first_stages'])
second('second_stages','Complete following mathematical row',F['second_stages'])
second('can_droit','Upright prose baseline with its supralinear insertion; preceding display is context',
 F['can_droit'].split('\ncontenant')[0])
second('kernel','Complete right-hand formula and its lower annotation; neighboring prose is context',F['kernel'])
second('small_diagram','Complete upper-left drawing with all labels and crossed material',F['small_diagram'])
second('right_nb','Diagonal right marginal note only; neighboring upright ink is context',F['right_nb'])
second('left_note','Diagonal left marginal note only; exclude crossing upright prose and drawing labels',F['left_note'])
second('lattice','Complete central drawing and both side annotations only; marginal prose and adjacent display are context',F['lattice'])
second('quotient','Complete right-hand drawing and its introducing prose; adjacent central drawing is context',F['quotient'])
second('sequence','Complete horizontal display below the right-hand drawing',F['sequence'],[932,1690,1665,1767])
second('marquage_complete','Two upright prose baselines only; diagonal note and following display are context',F['marquage'])
second('product_complete','Complete lower formula with its crossed material; prose above is context',F['product'])
second('boundary_note','Complete right marginal annotation and lower detached glyph',F['boundary_note'])
second('embedding','Lower upright prose and adjacent complete formula; marginal glyph above is context',F['embedding'])
second('last_formula','Complete terminal formula with its raised crossed material',F['last_formula'])
second('lower_number','Isolated lower-left marginal numeral',r'''\margin{1}''')

coverage = {
246:'Scan marker is editorial metadata; no manuscript text difference.',
247:'H editorial description of the date’s position; both read the same source date.',
248:'Same donnée sur les comp. connexes du bord; ordering difference arises from placement of the supralinear explanation. The explanation is attached to structure torique.',
249:'H editorial attachment description, and shifted main prose. Both source passages retained; connector reproduced.',
250:'Aligned environment syntax only.',251:'Display delimiter and prose/display layout syntax only.',
252:'148_scan002-01: no period after autom is visible.',253:'148_scan002-01: source resp. and its preceding cancelled word retained.',
254:'148_scan002-02: uncertain cancelled bijec. candidate retained against H struck illegibility.',
255:'Environment delimiters are syntax; 148_scan002-22 records the absent terminal period supplied by H.',
256:'148_scan002-03; M0037 resolved from crop.',
257:'Same lower Aut/comp. neutre annotation is present in H’s editorial description; vector/bar doubt remains M0039. Underbrace syntax is not an omission.',
258:'H editorial explanation interrupts the same stage rows. Both rows, the lower annotation, and ou encore are retained; M0038–M0041 remain as recorded.',
259:'148_scan002-04: literal can! retained.',
260:'Same source droit; represented as a supralinear insertion attached above R^I.',
261:'H repeats droit in an editorial placement description; no duplicate source word. The attachment brace is reproduced.',
262:'148_scan002-05 and -06 cover the actual kernel reading differences. H’s editorial text already contains the under-annotation.',
263:'Same multiplication dot; H uses cdot and C a literal period.',
264:'Diagram wrapper against H editorial description. Kernel differences covered by -05/-06; small drawing by -07.',
265:'Layout options and H editorial kernel/small-drawing description; source readings covered by -05/-06/-07.',
266:'148_scan002-07: full upper drawing, including the two-dot mark and crossed material, reproduced.',
267:'148_scan002-07; M0044 retained as an unresolved stroke combination, directly drawn.',
268:'148_scan002-07: the left lower end curves right and upward; its upper end merges into a rounded loop, crossed text, and a diagonal. The upper junction is drawn directly with an explicit doubt, without a categorical arrowhead.',
269:'148_scan002-07; right vertical hook and same lower subset relations drawn.',
270:'Subset arrow/phantom syntax; same visible subset relation, in -07 full drawing.',
271:'Subset arrow/phantom syntax; same lower SRT relation, in -07 full drawing.',
272:'Closing arrow label syntax only.',
273:'148_scan002-07 includes the uncertain cancelled phrase at its physical position; H refers only to crossed material.',
274:'Display delimiter only; i.e. on a is the same text.',
275:'148_scan002-08 for the left diagonal note; H’s en oblique belongs to the right NB editorial description.',
276:'148_scan002-08 for the rest of the left note; H’s droite is editorial position text for the NB note.',
277:'TikZ row-spacing option only.',
278:'Same product dot; H’s cdot is a macro difference.',
279:'Same lower Z^I object, ordered differently in the two TikZ sources.',
280:'Both scripts specify no-head on the same edge; ur versus dl is coding traversal, not a source arrow reversal.',
281:'TikZ label-side syntax; no textual prime in the source label.',
282:'Same Z^I object reordered within diagram code.',
283:'148_scan002-09: the left T(X) brace is retained; H’s prose gives only the right brace. The full lattice is reproduced.',
284:'Phantom matrix syntax in C’s brace height; both actual braces are retained with the lattice.',
285:'H’s editorial closing quotation mark only.',
286:'Diagram wrapper syntax; physical differences are in -10.',
287:'Layout option syntax only.',
288:'148_scan002-10: cancelled (X) remains in the quotient.',
289:'148_scan002-10: down arrow and separate right brace are drawn in their source positions.',
290:'Label syntax; unresolved looped letter retained as M0049 and included in -10 drawing.',
291:'H’s description confirms a downward arrow, which is drawn; position covered by -10.',
292:'148_scan002-10: the long wavy stroke is below the product on the source.',
293:'148_scan002-12: final blunt dash retained; -11 separately preserves the overworked preceding letter.',
294:'H reorders the left note after (*); -08 covers its actual word differences. Upright lower prose is retained, with cancelled de covered by -13.',
295:'148_scan002-14: cancelled U_i remains a candidate, with uncertainty.',
296:'148_scan002-14 and -15: H describes the strike, then adds an outer opening parenthesis to the marginal explanation.',
297:'148_scan002-15: no outer closing parenthesis/comma around the right marginal note; -16 records the detached lower glyph.',
298:'148_scan002-18: complete phrase retained, final déduise/déduire ending left doubtful.',
299:'148_scan002-20: lower position is explicit in the source and in H’s note, despite H’s body superscript.',
300:'148_scan002-17/-19 for the two cancelled exponents, -20 for the lower wedge index, and -21 for the lighter numeral omitted by H. H’s comparison to another page is editorial and was not used.'
}
R['diff_coverage']=[dict(row=n,disposition=coverage[n]) for n in range(246,301)]
R['deletion_insertion_check'] = ('The upper i.e. explanation is inserted above structure torique, with its enclosing attachment contour; it is written once. '
 'The droit insertion sits above R^I with a shallow brace and is written once. In the definition, the small word before resp. and the longer word '
 'after Aut^!(vec X) are cancelled, with en and bijec. left doubtful. The phrase et propre remains cancelled at the upper-left of the small drawing, '
 'and the separate diagonal/footed-stroke combination is reproduced without settling whether it is cancelled. The (X) within SRT(X)/Z^I is crossed '
 'and retained. The overworked T in (*) has an explicit alternative between a cancelled underlying looped letter and simple retracing. The word after '
 'un pt is cancelled, with de doubtful. The hatching before T_i is limited to the preceding candidate U_i; the final T_i stays live. Both final T '
 'superscripts are crossed separately; neither ! is asserted to remain live. The small dotted glyph below d’indice is preserved without claiming '
 'an insertion attachment. The three margin notes, their underlines, the date, both lattice braces, the quotient brace and lower stroke, and the '
 'lighter lower-left number are present. All C deletion and insertion loci were checked on the listed crops.')

(BASE/'work'/f'{PAGE}_report.json').write_text(json.dumps(R,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(page=PAGE,changes=len(R['changes']),decisions=len(R['decisions']),
                     unnumbered=len(R['unnumbered_decisions']),inventory=len(R['inventory']),
                     doubts=len(R['doubts']),second_boxes=len(R['second_boxes']),
                     coverage=len(R['diff_coverage'])),ensure_ascii=False))
