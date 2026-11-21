"""First-reader proposal for 148_scan067 only. Retain this work documentation."""
from pathlib import Path
import json
import re

ROOT = Path('/workspace/scratch/f28c4f52d3ec')
PAGE = '148_scan067'
PARTS = {}

PARTS['opening'] = r'''Un pantalon \inserted{(topologique)} subdivisé de façon standard, avec un ens $J$ de trous $(\operatorname{card}J=3)$ correspond à un OPENQUOTEtriangle pondéré'' i.e.
\[
J\xrightarrow{\pi}\mathbb N
\qquad(\mathrm{NB}\ \pi(j)=\text{nb d'arêtes qui relient $j$ et $k$, $i\ne j\ne k$})
\]'''.replace('OPENQUOTE', chr(96)*2)

PARTS['card_title'] = r'''Carte \inserted{orientée} décomposée pantaloniquement de façon standard $\Longleftrightarrow$ \deleted{\unsure{graphe}} squelette pantalonique généralisé'''

PARTS['cancelled_def'] = r'''\deleted{i.e. carte \unsure{cellulaire} (\unsure{pas néc. orientée}) dont les sommets marqués sont d'ordre $3$ (avec des sommets topologiques non marqués d'ordre $1$ éventuellement), et avec une pondération des \deleted{\unsure{arêtes orientées|arêtes repérées}} \inserted{drapeaux de types $0,1$} (sommet \inserted{marqué} et arête incidente) de telle façon que l'on ait pour chaque arête (cf ci-contre)}'''

PARTS['pants'] = r'''\figure{\begin{tikzpicture}[scale=.72,>=stealth]
% Pale earlier contours remain beside the red boundaries.
\draw[gray] (-.1,-.1) ellipse (4.55 and 4.12);
\draw[gray] (-1.42,-.22) ellipse (.88 and 1.05);
\draw[gray] (1.66,-.47) ellipse (.92 and 1.04);
\draw[red!65!black,line width=.7pt] (0,0) ellipse (4.5 and 4.1);
\draw[red!65!black,line width=.7pt] (-1.35,-.25) ellipse (.86 and 1.02);
\draw[red!65!black,line width=.7pt] (1.7,-.5) ellipse (.88 and 1.02);
\node at (-1.35,-.25) {$0$}; \node at (1.7,-.5) {$1$};
\node at (4.45,2.65) {$\infty$};
\draw[gray,->] (.95,2.6) arc (10:320:.16);
\coordinate (B01) at (-1.1,.72); \coordinate (B02) at (-1.78,.65);
\coordinate (B03) at (-2.02,.27); \coordinate (B04) at (-2.2,-.1);
\coordinate (B05) at (-2,-.82);
\coordinate (BO1) at (-.2,4.09); \coordinate (BO2) at (-2.73,3.25);
\coordinate (BO3) at (-3.86,2.1); \coordinate (BO4) at (-4.49,.1);
\coordinate (BO5) at (-3.2,-2.87);
\foreach \i in {1,2,3,4,5}{
 \draw[gray] (B0\i) to[bend left=4] (BO\i);
 \node[above left,inner sep=2pt] at (B0\i) {$b_{\i}^{0}$};
 \node[above left] at (BO\i) {$b_{\i}^{\infty}$};
}
\foreach \i in {1,2,4,5} \fill (B0\i) circle (1.4pt);
\coordinate (C01) at (-.63,.38); \coordinate (C02) at (-.5,-.48);
\coordinate (C03) at (-.87,-1.11); \coordinate (C04) at (-1.5,-1.25);
\coordinate (C11) at (1.28,.4); \coordinate (C12) at (.83,-.5);
\coordinate (C13) at (.98,-1.18); \coordinate (C14) at (1.48,-1.48);
\foreach \i in {1,2,3,4}{
 \fill (C0\i) circle (1.4pt); \fill (C1\i) circle (1.4pt);
 \node[right,inner sep=1pt] at (C0\i) {$c_\i^0$};
 \node[left,inner sep=1pt] at (C1\i) {$c_\i^1$};
}
\draw[gray] (C01) to[bend left=9] (C11);
\draw[gray] (C02)--(C12);
\draw[gray] (C03)--(C13);
\draw[gray] (C04) to[bend right=32] (C14);
\coordinate (A11) at (2.12,.4); \coordinate (A12) at (2.58,-.43);
\coordinate (A13) at (2.19,-1.35);
\coordinate (AO1) at (4,1.85); \coordinate (AO2) at (4.49,.05);
\coordinate (AO3) at (4.1,-1.65);
\foreach \i in {1,2,3}{
 \draw[gray] (A1\i) to[bend right=8] (AO\i);
 \node[right,inner sep=1pt] at (A1\i) {$a_\i^1$};
 \node[right] at (AO\i) {$a_\i^\infty$};
}
\fill (A13) circle (1.5pt);
\draw[gray!65] (1.46,-1.47) .. controls (2.35,-2.3) and (3.05,-2.85) .. (3.48,-2.59);
\draw[->,red!65!black] (-.53,.02)--(-.49,-.18);
\draw[->,red!65!black] (.95,-.01)--(1.08,.2);
\draw[->,red!65!black] (2.7,3.28)--(2.49,3.42);
\draw[red!65!black,line width=1.3pt] (3.38,-2.68)--(3.55,-2.49);
\draw[red!65!black,line width=1pt] (-2.95,3.1)--(-2.72,3.27);
\draw[red!65!black,line width=1pt] (-4.51,.32)--(-4.5,.02);
\end{tikzpicture}}'''

PARTS['edge_condition'] = r'''\figure{\begin{tikzpicture}[>=stealth,scale=.9]
\fill (0,0) circle (1.4pt) node[above left] {$s$};
\fill (2.5,0) circle (1.4pt) node[above right] {$t$};
\draw (0,0)--(2.5,0) node[midway,above] {$a$};
\draw (0,0)--(-.65,.65) node[left] {$\alpha_s$};
\draw (0,0)--(-.65,-.65) node[left] {$\beta_s$};
\draw (2.5,0)--(3.15,.65) node[right] {$\unsure{\beta_t^*|\beta_t}$};
\draw (2.5,0)--(3.15,-.65) node[right] {$\alpha_t$};
\node[below] at (.4,0) {$\gamma_s$};
\node[below] at (2.1,0) {$\gamma_t$};
% The diagram lies inside the subsequently cancelled block.
\draw (-.45,1.05)--(.35,-1.03);
\draw (2.96,1.02)--(3.38,-.95);
\end{tikzpicture}}
\[
\deleted{\underbrace{\alpha_s+\beta_s}_{\unsure{\deleted{\alpha}\gamma'_s|\gamma'_s}}
=\underbrace{\unsure{\alpha_t^*+\beta_t^*|\alpha_t+\beta_t}}_{\gamma'_t}}
\]'''

PARTS['torsors'] = r'''\deleted{et $=$ la \uline{donnée} d'un \deleted{\unsure{isom}} \inserted{anti-}isom des torseurs sous $\mathbb Z/\unsure{\gamma}$ $(\gamma=\gamma'_s=\gamma'_t)$}
\[
\deleted{\substack{\text{somme circulaire}\\\text{de }[1,\alpha_s]\text{ et }[1,\beta_s]}
\ \unsure{\simeq|\not\simeq}\
\substack{\text{somme}\\\text{circulaire de}\\{}[1,\alpha_t]\text{ et }[1,\beta_t]}}
\]'''

PARTS['pencil_map'] = r'''\figure{\begin{tikzpicture}[scale=.55,>=stealth]
% The pale map is earlier than the black text; only its visible runs are drawn.
\draw[gray] (-4,2.2) .. controls (-4.4,4.6) and (-1.7,5.3) .. (-.9,4.1)
 .. controls (-.1,2.6) and (-1.2,.8) .. (-2.4,.55)
 .. controls (-4.2,.3) and (-4.6,1.3) .. (-4,2.2);
\draw[gray] (-4,2.2) .. controls (-3.2,2.9) and (-2.2,2.8) .. (-1.1,3.55);
\draw[gray] (-3.9,2.15) .. controls (-2.7,1.9) and (-1.6,1.3) .. (-1.2,.55);
\draw[gray] (-2.4,.55) .. controls (-3.3,-.15) and (-3.8,-1.8) .. (-3.25,-3.2)
 .. controls (-2.9,-4.25) and (-2.2,-4.6) .. (-1.55,-4.95);
\draw[gray] (-1.2,.55) .. controls (-.4,-.8) and (-.95,-3.6) .. (-1.2,-4.75);
\draw[gray] (-1.45,-1.45) .. controls (-.7,-1.8) and (-.2,-2.1) .. (.35,-1.8);
\draw[gray] (.35,-1.8)--(1.5,-1.83);
\draw[gray] (2.3,-1.2) .. controls (2.6,.1) and (3.7,.4) .. (4.45,-.2)
 .. controls (6,-1.9) and (5.8,-4.1) .. (4.9,-4.9)
 .. controls (3.9,-5.2) and (3,-4.8) .. (2.75,-3.85)
 .. controls (2.3,-2.65) and (2.05,-1.9) .. (2.3,-1.2);
\draw[gray] (2.3,-1.2)--(4.7,-.45);
\draw[gray] (2.35,-1.7)--(4.65,-1.2);
\draw[gray] (2.55,-2.55) .. controls (3.2,-2.35) and (3.6,-2.85) .. (4.5,-3.1);
\draw[gray] (1.55,-1.85) .. controls (1.9,-2.05) and (2,-2.4) .. (2.2,-2.55);
\node at (-2.1,-4.5) {$A_{\infty0}$};
\node at (-1.65,-2.6) {$A_{0\infty}$};
\node at (-.1,-3.12) {$A_{01}$};
\node at (1.38,-3.12) {$A_{10}$};
\node at (3.1,-3.28) {$A_{1\infty}$};
\node at (5.65,-2.6) {$A_{\infty1}$};
% Black pentagon and its five legs, including the long leftward arrow.
\coordinate (p) at (2.6,2.1); \coordinate (q) at (4.2,1.45);
\coordinate (r) at (3.92,.26); \coordinate (s) at (2.48,-.1);
\coordinate (t) at (1.62,.9);
\draw[black] (p)--(q)--(r)--(s)--(t)--cycle;
\draw[black] (p)--(2.35,3.25) (q)--(5.5,2.02) (r)--(4.55,-.5) (s)--(2.5,-1.3);
\draw[black,->] (t)--(-.6,.23);
\fill[black] (r) circle (2pt);
% Two long cancellation strokes are distinct from the pentagon's left leg.
\draw[black,line width=.8pt] (-3.6,-2.1)--(1.25,3.9);
\draw[black,line width=.8pt] (-.6,-2.4)--(5.1,2.65);
\draw[black] (5.8,-2.5) .. controls (6.6,.6) and (6.55,2.2) .. (6.9,4.1);
\end{tikzpicture}}
% crop-candidate: scan 67'''

PARTS['loops'] = r'''\figure{\begin{tikzpicture}[>=stealth,scale=.8]
\draw[rotate=35] (0,0) ellipse (.72 and 1.05);
\draw (-.8,-.6)--(.8,.65);
\foreach \x/\y in {-.84/-.1,-.7/.35,-.4/.7,0/.93,.4/.86}
 \fill (\x,\y) circle (1.3pt);
\draw[->] (.65,.35) to[bend right=24] (.48,.7);
\draw[->] (-.74,-.3)--(-.77,-.55);
\begin{scope}[shift={(.6,-2.4)},rotate=35]
\draw[->] (-1,-.2) to[bend right=34] (1,.2);
\draw[->] (1,.4) to[bend right=34] (-1,-.05);
\end{scope}
\node at (1,-3.1) {$\unsure{[0,\alpha][1,\beta)|[1,\gamma][1,\beta)}$};
\draw[->] (-.4,-4.6) .. controls (-1.1,-4.2) and (-.2,-3.3) .. (.2,-4.3);
\draw[->] (-.3,-4.75) to[bend right=20] (.25,-4.45);
\draw[->] (.5,-4.9) to[bend left=36] (1.3,-4.55);
\draw[->] (1.4,-4.7) to[bend left=35] (.6,-5.1);
\draw[->] (.55,-5) to[bend left=28] (1.25,-4.7);
\fill (.67,-4.93) ellipse (.055 and .045);
\fill (1.04,-4.77) ellipse (.065 and .04);
\end{tikzpicture}}'''

OLD_EXPR = r"\unsure{(\alpha'+\beta'-\gamma')-\deleted{(\beta-\gamma)}|(\alpha'+\beta'-\gamma')-(\beta-\gamma)}\ \unsure{=}"
PALE_FRACTION = r"\unsure{\alpha'=\dfrac{\alpha'+\beta'+\gamma'}2}"
PARTS['algebra_main'] = r'''\figure{\begin{tikzpicture}[x=1cm,y=1cm]
% Pale earlier writing and dark replacements occupy the same area.
\node[gray,anchor=west] at (4.35,.47) {$PALE_FRACTION$};
\node[gray,anchor=west] at (4.92,-1.05) {$\deleted{\unsure{\alpha}}$};
\node[gray,anchor=west,font=\small] at (5.18,-2.00) {$OLD_EXPR$};
\node[gray] at (9.8,-3.05) {$\unsure{\alpha'}$};
\node[anchor=west] at (0,0) {$\beta+\gamma=\alpha'$};
\node[anchor=west] at (0,-1.18) {$\gamma+\alpha=\beta'$};
\node[anchor=west] at (0,-2.4) {$\alpha+\beta=\gamma'$};
\node[anchor=west] at (4.05,0) {$\alpha=\dfrac{\beta'+\gamma'-\alpha'}2=\dfrac{\alpha'+\beta'+\gamma'}2-\alpha'$};
\node[anchor=west] at (4.05,-1.18) {$\beta=\dfrac{\gamma'+\alpha'-\beta'}2$};
\node[anchor=west] at (4.05,-2.4) {$\gamma=\dfrac{\alpha'+\beta'-\gamma'}2$};
\end{tikzpicture}}'''.replace('OLD_EXPR', OLD_EXPR).replace('PALE_FRACTION', PALE_FRACTION)

PARTS['algebra_pencil'] = r'''{\color{gray}
\[
\begin{aligned}
2(\alpha+\beta+\gamma)&=\unsure{\alpha'+\beta'+\gamma'}\\
2\alpha+\beta+\gamma&=\unsure{\beta'+\gamma'}\\
\beta+\gamma&=\unsure{\alpha'}
\end{aligned}
\]}'''

PARTS['triangle1'] = r'''\figure{\begin{tikzpicture}[scale=.8]
\draw[gray] (0,0)--(2,3.7)--(4,0)--cycle;
\node[above] at (2,3.7) {$0$}; \node[left] at (0,0) {$1$}; \node[right] at (4,0) {$\infty$};
\foreach \i in {1,2,3} {
 \draw (\i,-.06)--(\i,.06); \node[below] at (\i,0) {$a_\i$};
}
\foreach \i in {1,2,3,4} {
 \pgfmathsetmacro{\y}{3.7-.72*\i}
 \pgfmathsetmacro{\x}{2*\y/3.7}
 \draw (\x-.06,\y)--(\x+.06,\y); \node[left] at (\x,\y) {$c_\i$};
}
\foreach \i in {1,2,3,4,5} {
 \pgfmathsetmacro{\y}{.6*\i}
 \pgfmathsetmacro{\x}{4-2*\y/3.7}
 \draw (\x-.06,\y)--(\x+.06,\y); \node[right] at (\x,\y) {$b_\i$};
}
\node at (-.9,2.2) {$\gamma=4$};
\node at (4.7,2) {$\beta=5$};
\node at (2,-.9) {$\alpha=3$};
\end{tikzpicture}}'''

PARTS['triangle2'] = r'''\figure{\begin{tikzpicture}[scale=.7]
\draw[gray] (0,0)--(1.7,3.4)--(3.7,0)--cycle;
\node[above] at (1.7,3.4) {$0$}; \node[left] at (0,0) {$1$}; \node[right] at (3.7,0) {$\infty$};
\node at (1.85,1.8) {$c_1\ c_2\ c_3\ c_4\cdot b_5\ b_4\ b_3\ b_2\ b_1$};
\node at (1.8,.45) {$a_3$};
\node at (1.8,-.12) {$a_2$};
\node at (1.8,-.63) {$\unsure{a^1|a_1}$};
\draw (3.55,-.7)--(3.6,-.96);
\end{tikzpicture}}'''

PARTS['triangle3'] = r'''\figure{\begin{tikzpicture}[scale=.85]
\draw[gray] (0,0)--(1.5,2.8)--(2.2,-.5)--cycle;
\node[above] at (1.5,2.8) {$\infty$};
\node[left] at (0,0) {$a$}; \node[right] at (2.2,-.5) {$b$};
\node[gray,left] at (-.05,.24) {$0$};
\node[gray,right] at (2.26,-.24) {$1$};
\foreach \i in {1,2,3,4} {
 \pgfmathsetmacro{\x}{1.5-.25*\i}
 \pgfmathsetmacro{\y}{2.8-.4667*\i}
 \draw (\x-.08,\y+.03)--(\x+.06,\y-.05);
 \node[left] at (\x,\y) {$b_\i$};
}
\draw (.17,.50)--(.31,.42);
\node[left] at (.25,.4665) {$\unsure{c_5|b_5}$};
\fill (1.74,1.67) circle (1.5pt);
\node[right] at (1.74,1.67) {$a_3$};
\fill (1.89,.95) circle (1.5pt);
\node[right] at (1.89,.95) {$\unsure{a_{2\,0}|a_2}$};
\fill (2.04,.23) circle (1.5pt);
\node[right] at (2.04,.23) {$\unsure{a_1}$};
\foreach \i in {1,2,3,4} {
 \pgfmathsetmacro{\x}{.45*\i}
 \pgfmathsetmacro{\y}{-.5*\x/2.2}
 \draw (\x,\y-.07)--(\x,\y+.07);
 \node[below] at (\x,\y) {$\unsure{c_\i|\deleted{a_\i}c_\i}$};
}
% Unresolved pale overwritten letter fragments are preserved geometrically.
\draw[gray!65] (.38,1.31) .. controls (.22,1.48) and (.18,1.14) .. (.35,1.17)
 .. controls (.48,1.2) and (.42,1.4) .. (.38,1.31);
\draw[gray!65] (2.27,1.01) .. controls (2.37,1.27) and (2.53,1.14) .. (2.5,.92);
\draw[gray!65] (2.27,.99)--(2.47,1.02);
\end{tikzpicture}}'''

PARTS['nb'] = r'''\uline{NB} $\alpha',\beta',\gamma'$ OK ssi $\alpha'+\beta'+\gamma'$ pair'''

PARTS['sphere'] = r'''\figure{\begin{tikzpicture}[scale=.83,>=stealth]
\draw[gray] (0,0) ellipse (2.55 and 2.7);
\coordinate (z) at (-1.95,-.5); \coordinate (o) at (1.75,-.3); \coordinate (i) at (.4,1.1);
% Five visible 0--1 runs; the lowest remains above the outer contour.
\draw[gray] (z) .. controls (-1.45,.85) and (1,.8) .. (o);
\draw[gray] (z) .. controls (-.9,.35) and (.85,.25) .. (o);
\draw[gray] (z) .. controls (-.8,-.42) and (.65,-.37) .. (o);
\draw[gray] (z) .. controls (-1.1,-1.38) and (.9,-1.35) .. (o);
\draw[gray] (z) .. controls (-1.28,-2.05) and (1.1,-2.03) .. (o);
% Visible wraps toward infinity are traced separately.
\draw[gray] (z) .. controls (-1.75,.35) and (-.2,.9) .. (i);
\draw[gray] (z) .. controls (-1.5,1.0) and (-.35,1.25) .. (i);
\draw[gray] (z) .. controls (-2,1.35) and (-.8,1.58) .. (i);
\draw[gray] (z) .. controls (-2.7,.4) and (-2.4,1.92) .. (-.65,1.55) .. controls (-.2,1.45) and (.2,1.15) .. (i);
\draw[gray] (z) .. controls (-2.9,.7) and (-2.1,2.35) .. (-.35,1.9) .. controls (.05,1.65) and (.22,1.35) .. (i);
\draw[gray] (i) .. controls (.9,1.1) and (1.65,.45) .. (o);
\draw[gray] (i) .. controls (1.6,1.4) and (2.25,.5) .. (o);
\draw[gray] (i) .. controls (2.8,1.55) and (2.45,-.02) .. (o);
\draw[gray] (-2.5,.45) .. controls (-2.6,1.9) and (-.7,1.6) .. (i)
 .. controls (2,1.5) and (2.6,1.5) .. (2.5,.6);
\foreach \p in {z,o,i} {
 \fill (\p) circle (3pt);
 \begin{scope}[shift={(\p)}]
 \draw[dashed] (0,.28) arc (90:270:.28);
 \draw (0,-.28) arc (-90:90:.28);
 \end{scope}
}
\node[below] at (z) {$0$}; \node[below right] at (o) {$1$}; \node[above right] at (i) {$\infty$};
\draw[->] (-1.68,-.57) arc (-15:62:.28);
\draw[->] (2.02,-.37) arc (-15:62:.28);
\draw (.64,1.02)--(.66,1.14)--(.58,1.10);
\end{tikzpicture}}'''

COUNT_WORD = r"\unsure{\deleted{bigones}\,arêtes|bigones}"
PARTS['counts'] = r'''\[
\begin{array}{l|l}
\text{trois sommets}&\text{sommets d'ordre }\alpha',\beta',\gamma'\\
\alpha+\beta+\gamma\ \text{COUNT_WORD}&
\end{array}
\]
\deleted{$\unsure{\alpha+\beta+\gamma}$}
\[
\left\{\begin{array}{ll}
(\alpha-1)+(\beta-1)+(\gamma-1)&
\overbrace{\text{faces-bigones}}^{=\alpha+\beta+\gamma-2}\\
2&\text{faces-triangles}
\end{array}\right.
\quad\bigg|\quad \alpha+\beta+\gamma-1\ \text{faces}
\]'''.replace('COUNT_WORD', COUNT_WORD)

PARTS['folio'] = r'''\mspage{66}'''

ORDER = ['opening','card_title','cancelled_def','pants','edge_condition','torsors',
         'pencil_map','loops','algebra_main','algebra_pencil','triangle1','triangle2',
         'triangle3','nb','sphere','counts','folio']

BOXES = {
    'opening': [183,0,1080,530], 'card_title':[1190,0,2945,245],
    'cancelled_def':[1190,193,2746,634], 'edge_condition':[1410,498,2210,730],
    'torsors':[1480,705,2370,1058], 'pencil_map':[1360,0,2873,1370],
    'pants':[419,495,1451,1439], 'loops':[105,1278,561,2001],
    'algebra_main':[1306,1274,2207,1578], 'algebra_pencil':[1235,1517,1715,1732],
    'triangle1':[583,1472,1350,2100], 'triangle2':[1235,1706,1737,2170],
    'triangle3':[1633,1528,2051,1845], 'nb':[2270,1268,2981,1369],
    'sphere':[2077,1342,2809,1954], 'counts':[1950,1817,2972,2160],
    'folio':[102,2101,212,2208],
}
FULL = {'opening','card_title','cancelled_def','edge_condition','pencil_map','triangle1'}

def crop_for(place):
    suffix = place + ('_full' if place in FULL else '')
    return f'crops/{PAGE}_{suffix}.png'

DATA = {
    'page':PAGE, 'reader':'reader_b', 'lines_read':35, 'places_cropped':17,
    'changes':[], 'decisions':[], 'implicit_decisions':[], 'doubts':[],
    'inventory':[], 'notes':[], 'check_events':[], 'notation':[], 'abbreviations':[],
    'second_boxes':[],
}

ERRORS = {
    'misread word':'Words', 'misread symbol or index':'Symbols and indices',
    'omission':'Omissions', 'text not on the page':'Text that is not on the page',
    'deletion state (struck given live or live given struck)':'Struck text',
    'insertion or placement':'Insertions put in the wrong place',
    'abbreviation expanded or spelling modernised':'Abbreviations expanded, spelling modernised',
    r'readable ink left as \ill{}':'Readable ink left as illegible',
    'drawing or diagram':'Drawings and diagrams', 'other':'Other',
}

def change(place, detail, c, h, final, evidence, kind='misread word',
           dc=True, dh=True, confidence='high', marked=False, consequential=False):
    DATA['changes'].append({
        'id':f'{PAGE}-{len(DATA["changes"])+1:02d}', 'place':detail,
        'c':c, 'h':h, 'final':final, 'diff_c':dc, 'diff_h':dh, 'kind':kind,
        'error_kind':ERRORS[kind], 'evidence':evidence,
        'crop':crop_for(place), 'box':BOXES[place],
        'confidence':confidence, 'marked_in_h':marked, 'consequential':consequential,
    })

def decision(id, place, reading, evidence, choice='undecided', confidence='medium', implicit=False):
    DATA['implicit_decisions' if implicit else 'decisions'].append({
        'id':id, 'decision':choice, 'reading':reading, 'evidence':evidence,
        'crop':crop_for(place), 'box':BOXES[place], 'confidence':confidence,
    })

def doubt(place, reading, alternatives, reason, confidence='medium'):
    DATA['doubts'].append({'place':place, 'reading':reading,
        'alternatives':alternatives, 'confidence':confidence, 'reason':reason})

def note(text, event=None, outcome=None):
    nid=f'{PAGE}-N{len(DATA["notes"])+1:02d}'
    DATA['notes'].append({'id':nid,'text':text})
    if event:
        DATA['check_events'].append({'statement_id':nid,'type':event,'outcome':outcome})
    return nid

def finish():
    (ROOT/'proposed'/f'{PAGE}.tex').write_text(
        '\\scanpage{67}\n\n'+'\n\n'.join(PARTS[k] for k in ORDER)+'\n', encoding='utf-8')
    (ROOT/'proposed'/f'{PAGE}.json').write_text(
        json.dumps(DATA,ensure_ascii=False,indent=2)+'\n', encoding='utf-8')
    (ROOT/'proposed'/f'{PAGE}_units.json').write_text(
        json.dumps(PARTS,ensure_ascii=False,indent=2)+'\n', encoding='utf-8')

# Metadata is appended below; finish() is called at its end.

change('opening','Opening abbreviation ens', 'ens', r'ens.\ ', 'ens',
       'The low joined e/n/s run ends in an upward exit; the following blank has no detached terminal point.',
       'abbreviation expanded or spelling modernised', dc=False)
change('opening','Quotation marks around triangle pondéré', chr(96)*2+"triangle pondéré''",
       '« triangle pondéré »', chr(96)*2+"triangle pondéré''",
       'Two small raised strokes flank the phrase; there are no paired angular guillemets.',
       'misread symbol or index', dc=False)
change('opening','NB, between k and i≠j≠k', r'k$, \unsure{où} $i\ne j\ne k',
       r'k$, où $i \neq j \neq k', r'k$, $i\ne j\ne k',
       'After the k there is a comma and then the separate i. No o loop or u connection occurs in the gap.',
       'text not on the page')
change('card_title','Title, décomposée and its live state', 'décomposée',
       r'\struck{découpée}', 'décomposée',
       'The word contains the low m humps and a long descending p, followed by the o/s/é/e ending. The retracing is confined to letters; no independent straight strike crosses the word.',
       dc=False)
change('card_title','Title, pantaloniquement', 'pantaloniquement',
       r'\uncertain{pantalonniquement}', 'pantaloniquement',
       'After the tall l and the rounded o, one n-like joining run leads into i and the descending q. There is no separate second n.',
       dc=False, marked=True)
change('card_title','Title, equivalence arrow', r'\longleftrightarrow',
       r'\Longleftrightarrow', r'\Longleftrightarrow',
       'Two parallel shafts run between separate left and right heads; the lower shaft is visible across the middle.',
       'misread symbol or index', dh=False)
change('card_title','Title, cancelled former noun', r'\deleted{\unsure{graphe}}',
       r'\struck{\ill{}}', r'\deleted{\unsure{graphe}}',
       'The initial g-like descender and following r/a outlines are visible, but the horizontal cancellation hides the internal p/h/e connections. The word is only tentatively recovered.',
       r'readable ink left as \ill{}', dc=False, confidence='low', marked=True)
change('card_title','Title, live phrase after the cancelled noun',
       'squelette pantalonique généralisé',
       r'\uncertain{une} carte pantalonnière généralisée',
       'squelette pantalonique généralisé',
       'The first word starts with a short s followed by a long descending q, then u/e and tall l/t strokes. There is no separate une or carte. The next ending is -nique and the final word ends é, without another e loop.',
       dc=False, marked=True)
change('cancelled_def','Scope of the cancelled definition', PARTS['cancelled_def'],
       r'\struck{i.e.\ carte cellulaire (pas néc.\ orientée), dont les sommets} ...',
       PARTS['cancelled_def'],
       'The top horizontal strike, long descending boundary strokes and diagonal cancellation continue across the following definition, its raised replacements, and the lower edge/torsor construction. H stops its struck wrapper after the first line.',
       'deletion state (struck given live or live given struck)', dc=False)
change('cancelled_def','After parenthesis pas néc. orientée',
       r'orientée}) dont', r'orientée), dont', r'orientée}) dont',
       'The closing parenthesis is followed directly by the start of dont. The nearby lower oblique belongs to the crossing drawing, not a detached comma.',
       'text not on the page', dc=False)
change('cancelled_def','Sommets marqués', 'marqués', r'\ill{}', 'marqués',
       'The m humps, open a, r, descending q, accented e and final s remain separable between the crossing strokes.',
       r'readable ink left as \ill{}', dc=False, marked=True)
change('cancelled_def','Parenthesis after order 3', r'\unsure{avec des sommets topologiques}',
       r'sauf des sommets \uncertain{topologiques}', 'avec des sommets topologiques',
       'The initial four letters are a short rounded a, low v, e loop and open c. There is no tall f. The full topologiques run has the tall l, descending g/q-like connection and final es.',
       dc=False, marked=True)
change('cancelled_def','Non marqués before d’ordre 1', 'non marqués', r'\ill{}',
       'non marqués',
       'Three low n/o/n groups precede the separate m/a/r/q/u/é/s run. The order-1 numeral follows after d’ordre.',
       r'readable ink left as \ill{}', dc=False, marked=True)
change('cancelled_def','Raised qualifier de types 0,1',
       r'avec une \inserted{\unsure{de types $0,1$}} pondération',
       r'\note{Au bout de la ligne « et avec une » un ajout, « \ill{} de types $0, 1$ », non situé}',
       r'\deleted{\unsure{arêtes orientées|arêtes repérées}}\ \inserted{drapeaux de types $0,1$}',
       'The raised d/r/a/p/e/a/u/x and following de types share the interline directly above the cancelled arêtes group. The small 0, comma and 1 continue this raised run to the right; they do not belong after une.',
       'insertion or placement', marked=True)
change('cancelled_def','Old cancelled arêtes qualification',
       r'\deleted{\unsure{arêtes orientées}}', r'\struck{arêtes repérées}',
       r'\deleted{\unsure{arêtes orientées|arêtes repérées}}',
       'The arêtes group can be followed, but the next word is intersected by the strike and the descenders of raised drapeaux/types. The supposed p may be intrusive, so orientées and repérées remain open.',
       confidence='low')
change('cancelled_def','Raised replacement drapeaux',
       r'\inserted{drapeaux}', r'\add{\ill{}}', r'\inserted{drapeaux de types $0,1$}',
       'The raised replacement has a tall d, short r, a loop, long descending p, then e/a/u and crossed terminal x. It continues directly into de types 0,1.',
       r'readable ink left as \ill{}', dc=False, marked=True)
change('cancelled_def','Inserted marqué after sommet', r'\inserted{marqué}',
       'absent', r'\inserted{marqué}',
       'A smaller raised m/a/r/q/u/é run sits after sommet and above the following et. Its lower attachment belongs to this insertion, not to arête.',
       'omission', dc=False)
change('cancelled_def','Abbreviation cf', 'cf', r'cf.\ ', 'cf',
       'The c is open and the f has its descending return; no independent point stands before ci-contre.',
       'abbreviation expanded or spelling modernised', dc=False)
change('edge_condition','Elevated marks in diagram and equality',
       r'\beta_t; \alpha_t+\beta_t', r'\beta_t; \alpha_t+\beta_t',
       r'\unsure{\beta_t^*|\beta_t}; \unsure{\alpha_t^*+\beta_t^*|\alpha_t+\beta_t}',
       'The elevated diagram β mark meets the long boundary stroke. The elevated α-side mark of the equality overlaps a descender from cf above, whereas the β-side blot is more detached and has several lobes. Actual extra ink is present, but star-like superscripts cannot be separated securely from intrusive strokes. The whole RHS is kept doubtful.',
       'misread symbol or index', confidence='low', consequential=True)
change('edge_condition','Left underbrace label, possible old alpha',
       r"\gamma'_s", r"\gamma'_s",
       r"\unsure{\deleted{\alpha}\gamma'_s|\gamma'_s}",
       'A dark small loop lies to the left of the descending γ stroke. It may be an overwritten alpha, or part of the heavily retraced gamma; the prime and s themselves are visible.',
       'omission', confidence='low')
change('torsors','Torsor clause, article, number and gender',
       r"la \uline{donnée} d'un", r"de données d'une", r"la \uline{donnée} d'un",
       'The article starts with a tall l and a small a. Donnée ends in a final e loop with no independent s. After d’ the low u/n connection ends before the gap, with no further e. A separate straight line lies below donnée only.',
       dc=False)
change('torsors','Cancelled old isom', r'\deleted{\unsure{isom}}',
       r'\struck{\ill{}}', r'\deleted{\unsure{isom}}',
       'A short i-like stroke and s/o/m-like loops remain below the inserted anti-, but the heavy overstrike merges several connections. The candidate is retained without claiming every letter clear.',
       r'readable ink left as \ill{}', dc=False, confidence='low', marked=True)
change('torsors','Live isom abbreviation', 'isom', r'isom.\ ', 'isom',
       'The last m has a long low exit and is followed by a blank before des. There is no detached abbreviation point.',
       'abbreviation expanded or spelling modernised', dc=False)
change('torsors','Order of group and parenthetical equality',
       r"sous $\unsure{\mathbb Z|\mathbf Z}/\gamma$ $(\gamma=\gamma'_s=\gamma'_t)$",
       r"$(\gamma = \gamma'_s = \gamma'_t)$ sous $\mathbb{Z}/\gamma$",
       r"sous $\mathbb Z/\unsure{\gamma}$ $(\gamma=\gamma'_s=\gamma'_t)$",
       'Sous and the doubled Z/divisor lie at the left on the lower continuation; the parenthesized γ equality sits separately to their right. H reverses the reading order.',
       'insertion or placement', dc=False, marked=True)
change('torsors','Circular-sum wording on both sides',
       r'somme circulaire; somme circulaire de', r'sommes circulaires; sommes circulaires de',
       r'somme circulaire; somme circulaire de',
       'Both somme endings finish with a single e loop; the circulaire endings run out from e without a separate s. The cancellation crosses the block but does not supply those endings.',
       dc=False)
change('torsors','Crossed sign between the circular sums', r'\unsure{\simeq}',
       r'\rightleftarrows', r'\unsure{\simeq|\not\simeq}',
       'Two near-horizontal strokes, the upper one curved, are crossed by a dark oblique. The crossing may be a local negation/cancellation or part of the larger strike. There are no separately readable opposing arrowheads.',
       'misread symbol or index', confidence='low', marked=True, consequential=True)
change('torsors','Punctuation after group and right circular sum',
       r'[1,\beta_t]}.', r'\mathbb{Z}/\gamma\,: ... [1,\beta_t].',
       r'[1,\beta_t]}',
       'There is no independent colon after the quotient. The lower enclosing stroke passes beneath the right brackets; nearby tiny spots do not form secure terminal punctuation.',
       'text not on the page', confidence='medium')
change('torsors','Scope of cancellation across torseurs and both sums',
       PARTS['torsors'], 'H leaves the torsor clause and both circular sums live',
       PARTS['torsors'],
       'The long diagonal and enclosing return cut through and surround the complete lower construction, continuing the cancellation begun above. The raised anti- is included in that later scope.',
       'deletion state (struck given live or live given struck)', dc=False)
change('pencil_map','Pentagon’s long left leg',
       r'\draw (t)--(-1,-.5);', 'not individually specified in H drawing synopsis',
       r'\draw[black,->] (t)--(-.6,.23);',
       'The left leg extends far beneath the equality’s right brace and terminates in a distinct leftward head. It is a separate near-horizontal line, not one of the long diagonal cancellations.',
       'drawing or diagram', dh=False)
change('pencil_map','Earlier pencil map, visible contours and cancellation geometry',
       'Two schematized lobes, internal runs and two diagonal strokes',
       'Editorial synopsis of a trivalent map and six A regions',
       PARTS['pencil_map'],
       'The completed upper boundary shows the broad pale top lobe. Lower contour fragments, internal partitions, six written A labels and the right outer cancellation run remain visible under later ink. The proposal traces those runs without inferring obscured connections.',
       'drawing or diagram', dh=False, confidence='medium')
change('pants','All eight inter-hole labels',
       r'a_\i^0 (i=1,2,3,4); b_\i^1 (i=1,2,3,4)',
       r'a^0_1,\ldots,a^0_4; b^1_1,\ldots,b^1_4',
       r'c_1^0,c_2^0,c_3^0,c_4^0;\ c_1^1,c_2^1,c_3^1,c_4^1',
       'Every inter-hole label begins with an open crescent c. These are distinct from the closed a forms on the right and the tall ascenders of b on the left. All eight low indices and upper 0/1 indices were read separately.',
       'misread symbol or index', consequential=True)
change('pants','Boundary point fills at b3^0 and a3^1',
       'filled b3^0; unfilled a3^1', 'not individually specified in H drawing synopsis',
       'no separate fill at b3^0; filled a3^1',
       'At b3^0 the radial line joins the contour without a separate dark disk; at a3^1 there is a distinct filled dark spot.',
       'drawing or diagram', dh=False)
change('pants','Lower-right outer red mark', 'arrowhead on the lower-right outer contour',
       'not individually specified in H drawing synopsis',
       'blunt red retracing, without an arrowhead',
       'The lower-right red segment ends as a thick straight continuation with no divergent head strokes. The upper-right outer mark has a separate head and remains an arrow.',
       'drawing or diagram', dh=False)
change('pants','Faint earlier inner contours and extra radial run', 'absent',
       'not individually specified in H drawing synopsis',
       'two earlier inner contour traces and an unlabelled run from near c4^1 toward the lower-right outer border',
       'Pale curves sit beside both red inner loops. A further thin run leaves the neighbourhood of the lowest right inter-hole attachment and continues down and right beyond the labelled arcs.',
       'drawing or diagram', dh=False)
change('loops','Top loop, five marks and unheaded chord',
       'six filled marks; arrowheaded diagonal chord',
       'not individually specified in H drawing synopsis',
       'five discrete filled/ticked marks; unheaded chord',
       'Five separate heavy spots lie on the upper/left contour. The lower-left pointed mark belongs to the contour arrow, and the diagonal ends in a thick straight terminal without a separate head.',
       'drawing or diagram', dh=False)
change('loops','Right contour arrow on top loop', 'right contour arrow points down',
       'not individually specified in H drawing synopsis', 'right contour arrow points up',
       'The head lies at the upper end of the short right arc; the separate left contour head points downward.',
       'drawing or diagram', dh=False)
change('loops','Lower-right arc cluster, heavy spots', 'absent',
       'not individually specified in H drawing synopsis',
       'two irregular heavy spots on the three-arc cluster',
       'Two compact dark thickenings are visible on the lower-right bundle and are reproduced as ink shapes without interpreting them as extra graph vertices.',
       'drawing or diagram', dh=False, confidence='medium')

change('algebra_main','Pale prefix before the earlier fraction', 'absent', 'absent',
       PALE_FRACTION,
       'Above the first dark α row, a pale alpha-like loop has a detached raised tick followed by two short horizontal strokes. This appears to be α′= before the pale numerator/fraction; the entire old formula remains unsure because dark replacement strokes obscure its letters.',
       'omission', confidence='low')
change('algebra_main','Old expression near the gamma row',
       r"\unsure{(\alpha'+\beta'-\gamma')-(\beta+\gamma)}",
       r"\note{« $-(\beta-\gamma)$ » biffé à côté}",
       OLD_EXPR,
       'Inside the right old parenthesis the sign between β and γ is a horizontal dash, without the upright required for plus. The pale left parenthesis and primed letters overlap the dark gamma row; the extent of the local crossing remains uncertain.',
       'misread symbol or index', dh=False, confidence='low', marked=True, consequential=True)
change('algebra_main','Separate lower-right pale alpha prime',
       r"\unsure{\alpha'}", 'absent', r"\unsure{\alpha'}",
       'A separate pale loop with a raised tick occurs at about original x1980–2000,y1520. It lies to the right of, and is not the same ink as, the small triangle apex infinity near x1900,y1540.',
       'omission', dc=False, confidence='low')
change('algebra_main','Pale earlier fraction', r"\unsure{\dfrac{\alpha'+\beta'+\gamma'}2}",
       'absent', PALE_FRACTION,
       'Faint primed letters, plus strokes, a fraction line and a low 2 remain behind/above the first dark equation. The visible prefix and overlapping dark numerator prevent a fully secure old formula.',
       'omission', dc=False, confidence='low')
change('algebra_main','Old cancelled alpha near the beta equation',
       r'\deleted{\unsure{\alpha}}', 'absent', r'\deleted{\unsure{\alpha}}',
       'A pale alpha-like loop remains beside the dark beta equality; dark replacement strokes cross it. Its exact old outline is not recoverable with certainty.',
       'omission', dc=False, confidence='low')
change('algebra_main','Placement of the earlier pencil algebra',
       r"\deleted{\unsure{\alpha}},\quad \unsure{(\alpha'+\beta'-\gamma')-(\beta+\gamma)},\quad \unsure{\alpha'},\quad \unsure{\dfrac{\alpha'+\beta'+\gamma'}2}.",
       r"\note{la dernière ligne de droite est surchargée}",
       PARTS['algebra_main'],
       'The pale forms occupy positions above, behind and beside the dark right-hand column; they are not a separate baseline list with commas and a final period.',
       'insertion or placement', confidence='medium')
change('algebra_pencil','First lower pencil equality',
       r"\unsure{2(\alpha+\beta+\gamma)=\alpha'+\beta'+\gamma'}",
       r'2(\alpha+\beta+\gamma) = \ldots',
       r"2(\alpha+\beta+\gamma)=\unsure{\alpha'+\beta'+\gamma'}",
       'The 2, opening and closing parentheses, three Greek letters and two plus signs are separable on the left. Faint RHS loops and raised ticks remain compatible with the three primed letters but are not completely secure.',
       'omission', dc=False, confidence='low', marked=True)
change('algebra_pencil','Second lower pencil equality',
       r"\unsure{2\alpha+\beta+\gamma=\beta'+\gamma'}",
       r'2\alpha+\beta+\gamma = \ldots',
       r"2\alpha+\beta+\gamma=\unsure{\beta'+\gamma'}",
       'The left 2α+β+γ and equality are visible. The right-hand upper ticks and lower loops are much fainter; the proposed β′+γ′ remains explicitly doubtful.',
       'omission', dc=False, confidence='low', marked=True)
change('algebra_pencil','Added punctuation and one-line layout',
       r"\unsure{2(\alpha+\beta+\gamma)=\alpha'+\beta'+\gamma'}, \qquad \unsure{2\alpha+\beta+\gamma=\beta'+\gamma'}, \qquad \unsure{\beta+\gamma=\alpha'}.",
       r"\note{au crayon, en dessous, un essai « $2(\alpha+\beta+\gamma) = \ldots$, $2\alpha + \beta + \gamma = \ldots$, $\beta + \gamma = \alpha'$ »}",
       PARTS['algebra_pencil'],
       'The pencil trials occupy three successive rows. No comma or final period is written at their ends.',
       'text not on the page', dh=False)
change('triangle2','Dot between c4 and b5', r'c_4\ b_5', r'c_4 \cdot b_5',
       r'c_4\cdot b_5',
       'A detached, dark round point stands between c4 and b5 on the same central row, distinct from both letter strokes.',
       'misread symbol or index', dh=False)
change('triangle2','Three a labels and bottom raised 1',
       r'a_3;\ a_2;\ a_1', 'absent',
       r'a_3;\ a_2;\ \unsure{a^1|a_1}',
       'The upper two labels have low 3 and 2. The last small straight 1 is visibly higher beside the a; whether it is an exponent or a displaced lower index remains open.',
       'misread symbol or index', confidence='medium')
change('triangle2','Isolated lower-right oblique stroke', 'absent', 'absent',
       r'\draw (3.55,-.7)--(3.6,-.96);',
       'A short oblique lies apart from the labels below and right of the triangle. It has no clear numeral context or separate foot and is preserved as a drawing fragment.',
       'drawing or diagram', confidence='medium')
change('triangle3','Small triangle, vertex labels',
       r'\infty,\ \unsure{a},\ \unsure{b},\ 0,\ 1', 'absent',
       r'\infty,\ a,\ b,\ 0,\ 1',
       'The black a has a closed small oval and right exit; b has a tall ascender and bowl. Pale 0 and 1 remain alongside them; infinity has two joined loops at the apex.',
       'omission', dc=False)
change('triangle3','Lowest left edge label', r'\unsure{b_5}', r'b_5',
       r'\unsure{c_5|b_5}',
       'The lowest left initial is an open curve without the tall b ascender found in the four labels above. The small low 5 is visible, but retracing prevents excluding a damaged b.',
       'misread symbol or index', confidence='medium', consequential=True)
change('triangle3','Extra low loop at middle right a2 label',
       r'\unsure{a_2}', r'a_2', r'\unsure{a_{2\,0}|a_2}',
       'Beside/below the readable 2 there is another small rounded loop. It may be a surviving old 0 or reinforced ink; the notation records the extra visible loop without treating it as a securely intended two-part index.',
       'omission', confidence='low', consequential=True)
change('triangle3','Overwritten base labels and older side fragments',
       r'\unsure{c_\i}', r'c_1,\ldots,c_4',
       r'\unsure{c_\i|\deleted{a_\i}c_\i}\quad(i=1,2,3,4)',
       'The four base labels have open c-like outer curves but closed/retraced inner traces compatible with earlier a forms. Additional pale A-like fragments near the left b3 and right a2 are drawn geometrically; no complete earlier letter is claimed.',
       'deletion state (struck given live or live given struck)', confidence='low')
change('nb','NB, primes on all three initial letters', r"\alpha',\beta',\gamma'",
       r'\alpha,\beta,\gamma', r"\alpha',\beta',\gamma'",
       'Each of the three initial letters has a separate short raised tick, matching the ticks on the sum to the right.',
       'misread symbol or index', dc=False, consequential=True)
change('nb','NB, literal condition OK', r'\unsure{OK|$\in\mathbb N$}',
       r'\in\mathbb N', 'OK',
       'A rounded O is followed by a tall K with two diverging right strokes. There is no membership sign followed by a separate N.',
       'misread symbol or index', dc=False, marked=True, consequential=True)
change('sphere','Five visible paths between 0 and 1',
       r'\foreach \b in {16,0,-16,-32}', 'absent',
       PARTS['sphere'],
       'Two curves bow above the central shallow run and two bow below it. The lowest run is separate from the still-lower outside sphere contour. The count is kept even though the pants drawing has four inter-hole c arcs.',
       'drawing or diagram', dh=False, consequential=True)
change('sphere','Local circle sectors and orientations',
       r'\draw[dashed] (\p) circle (.28);', 'absent',
       PARTS['sphere'],
       'The local left sectors are broken, the right sectors continuous. The 0 and 1 arrowheads point upward on the right. The small infinity-side head is less distinct and is traced as a short angular mark.',
       'drawing or diagram', dh=False, confidence='medium')
change('counts','Right column, d’ordre', "sommets d'ordre", "sommets d'indice",
       "sommets d'ordre",
       'After d’ the rounded o is followed by r/d/r and an e exit; there is no separate in/d/i/c sequence.',
       dc=False)
change('counts','Right column, no additional numeral 3',
       "sommets d'ordre", r"\uncertain{3} sommets d'indice", "sommets d'ordre",
       'The first large curled stroke belongs to the initial s of sommets. No independent numeral stands before that word.',
       'text not on the page', dc=False, marked=True)
change('counts','Right column, primed degree labels',
       r"\alpha',\beta',\gamma'", r'\alpha,\beta,\gamma', r"\alpha',\beta',\gamma'",
       'Separate upper ticks occur after all three Greek letters; they are visible above the bowls and before the punctuation or next letter.',
       'misread symbol or index', dc=False, consequential=True)
change('counts','Overworked word after the edge total', 'arêtes',
       r'\struck{bigônes} arêtes', COUNT_WORD,
       'A long descending g-like loop is securely present in the overworked group. Several upper strokes overlap, so a separate fully legible live arêtes cannot be isolated from the old bigones-like layer.',
       'deletion state (struck given live or live given struck)', confidence='low', marked=True)
change('counts','Written bigones spelling', 'faces-bigones', 'faces-bigônes',
       'faces-bigones',
       'The o bowl has no separate circumflex above it. The stroke above the word belongs to the overbrace and does not form an accent.',
       'abbreviation expanded or spelling modernised', dc=False)
change('folio','Lower pale folio annotation', r'\mspage{66}', 'absent',
       r'\mspage{66}',
       'Two pale 6 forms, each with a loop and a rising entry stroke, stand apart at the lower-left corner.',
       'omission', dc=False)
change('algebra_main','Pale terminal equality after the old right parenthesis',
       'absent', 'absent', r'\unsure{=}',
       'Two separate short pale horizontal strokes follow the older right closing parenthesis around original x2120,y1470. Their equality reading remains doubtful. The separate alpha-prime on the lower row is not typographically attached as a right-hand side.',
       'omission', confidence='low')

# The supplied marks retain their original order. Extra deleted doubts are separate.
decision('M0784','opening',r"k$, $i\ne j\ne k",
         'A comma is followed directly by i; neither an o bowl nor a u connection exists in the intervening gap.',
         'other','high')
decision('M0785','loops',r'\unsure{[0,\alpha][1,\beta)|[1,\gamma][1,\beta)}',
         'The interval annotation is small and intersected by nearby arc strokes. The opening digit and first Greek letter cannot be distinguished securely; the last beta-like loop and closing parenthesis are more visible.',
         confidence='low')
decision('M0786','algebra_main',r"\beta=\dfrac{\gamma'+\alpha'-\beta'}2",
         'The full numerator is γ′+α′−β′. Under its long fraction bar the denominator has a curved descending entry and a short flat lower exit, the writer’s compressed 2, not a question mark or an omitted divisor.',
         'first','high')
decision('M0787','algebra_pencil',r"2(\alpha+\beta+\gamma)=\unsure{\alpha'+\beta'+\gamma'}",
         'The entire left side, parentheses and equality are visible; the RHS retains faint loops and three raised ticks but not enough contrast for an unconditional reading.',
         confidence='low')
decision('M0788','algebra_pencil',r"2\alpha+\beta+\gamma=\unsure{\beta'+\gamma'}",
         'The left 2α+β+γ and equality are separable. The RHS is pale and remains doubtful as β′+γ′.',
         confidence='low')
decision('M0789','algebra_pencil',r"\beta+\gamma=\unsure{\alpha'}",
         'The beta descender, plus and gamma loop on the left are readable. The right small loop and detached tick are compatible with α′ but remain faint.',
         confidence='low')
decision('M0790','algebra_main',OLD_EXPR,
         'The right old parenthesis contains a horizontal minus between β and γ. The old primed group to its left overlaps the dark equation; whether the right term is independently struck remains unresolved. Two faint horizontal strokes after the closing parenthesis are retained as a doubtful terminal equals sign, separate from the lower alpha-prime.',
         confidence='low')
decision('M0791','algebra_main',r"\unsure{\alpha'}",
         'A separate pale alpha-like loop and raised tick occur around original x1980–2000,y1520. They are distinct from the two-loop infinity of the adjacent triangle at about x1900,y1540.',
         confidence='low')
decision('M0792','algebra_main',PALE_FRACTION,
         'The pale earlier numerator/fraction overlaps the dark upper right equation. The old prefix has an alpha-like loop, a raised tick and two equality strokes; the whole pale formula remains unsure.',
         confidence='low')
decision('M0793','triangle3','a',
         'The black vertex label has a closed low oval with a right exit and no ascender; the nearby pale 0 is a separate earlier mark.',
         'first','high')
decision('M0794','triangle3','b',
         'The black vertex letter has a tall ascender and a distinct bowl; the pale 1 beside it remains separately visible.',
         'first','high')
decision('M0795','triangle3',r'b_1\quad b_2\quad b_3\quad b_4\quad\unsure{c_5|b_5}',
         'The upper four labels have b ascenders and separate low indices 1–4. The lowest initial lacks that ascender and looks like c, while its small 5 is visible. A damaged b remains possible.',
         confidence='medium')
decision('M0796','triangle3',r'a_3\quad\unsure{a_{2\,0}|a_2}\quad\unsure{a_1}',
         'The upper a3 is readable. The middle a2 has an extra low round trace beside the 2, and the lower a1 is retraced. The apparent old traces are not normalized away.',
         confidence='low')
decision('M0797','triangle3',r'\unsure{c_1|\deleted{a_1}c_1}\quad\unsure{c_2|\deleted{a_2}c_2}\quad\unsure{c_3|\deleted{a_3}c_3}\quad\unsure{c_4|\deleted{a_4}c_4}',
         'All four base positions have visible low numeric indices. The initial letters are heavily retraced open c-like curves with possible closed a-like underlying loops; the old-letter interpretation remains tentative.',
         confidence='low')
decision('M0798','nb','OK',
         'The sign consists of a rounded O and a K with a stem and two diverging right strokes, following three individually primed Greek letters.',
         'first','high')
decision('M0799','counts','2',
         'The raised total ends in a short curved digit with a lower right exit, visibly 2. There is no second rounded lobe of 3. The full row and both count totals were read together.',
         'first','high')

implicit_specs = [
 ('I067-01','card_title',r'\deleted{\unsure{graphe}}','Initial g and parts of r/a remain visible, but the strike obscures the p/h/e connections.','undecided','low'),
 ('I067-02','cancelled_def',r'\unsure{cellulaire}','The tall l strokes and final aire-like run remain visible; the horizontal strike masks several middle letter joins.','undecided','low'),
 ('I067-03','cancelled_def',r'\unsure{pas néc. orientée}','The parentheses and word outlines survive, but the strike shares the baseline of several small letters; every letter is not independently plain.','undecided','low'),
 ('I067-04','cancelled_def','avec des sommets topologiques','The four low letters a/v/e/c, the separate des, and all subsequent tall/descending letters are visible on the completed crop.','first','high'),
 ('I067-05','cancelled_def',r'\inserted{drapeaux de types $0,1$}','The raised de/types run, including the tall t, p descender, 0, comma and 1, is clear and attaches to drapeaux above the old arêtes group.','first','high'),
 ('I067-06','cancelled_def',r'\deleted{\unsure{arêtes orientées|arêtes repérées}}','The second old word is crossed by both the cancellation and raised descenders; the possible p is not securely part of that baseline.','undecided','low'),
 ('I067-07','cancelled_def','sommet','Initial s/o, the two m humps, e and final tall t are separable on the full crop; the following marqué is raised.','first','high'),
 ('I067-08','torsors',r'$=$','Two separated short horizontal bars follow et; no additional letter is needed or supplied.','first','high'),
 ('I067-09','torsors',r'\deleted{\unsure{isom}}','The old low loop sequence is heavily crossed below anti-; every letter is not plain.','undecided','low'),
 ('I067-10','torsors',r'\mathbb Z', 'The full quotient and following equality were inspected. The Z has two separated diagonal strokes. This resolves the alphabet only; its lower-right divisor is overworked and remains gamma only tentatively.','first','high'),
 ('I067-11','torsors',r'\unsure{\simeq|\not\simeq}','Two horizontal/curved bars are crossed by an oblique whose local or global scope cannot be separated.','undecided','low'),
 ('I067-12','algebra_main',r'\deleted{\unsure{\alpha}}','A pale alpha-like loop under dark replacement strokes remains only partially recoverable.','undecided','low'),
 ('I067-13','counts',r'\deleted{$\unsure{\alpha+\beta+\gamma}$}','The crossed sum has alpha/beta/gamma-shaped surviving portions and plus-like strokes, but the heavy strike conceals parts of each.','undecided','low'),
]
for iid,place,reading,evidence,choice,conf in implicit_specs:
    decision(iid,place,reading,evidence,choice,conf,True)

doubt('Title, old cancelled noun',r'\deleted{\unsure{graphe}}','graphe; other crossed word',
      'The cancellation masks several internal letters.','low')
doubt('Cancelled definition, cellulaire',r'\unsure{cellulaire}','cellulaire; damaged middle letters',
      'The horizontal strike merges with the baseline.','low')
doubt('Cancelled definition, parenthesis',r'\unsure{pas néc. orientée}','pas néc. orientée; locally unread crossed letters',
      'The phrase outline is plausible but not every letter is independent of the strike.','low')
doubt('Cancelled definition, old arêtes qualification',r'\deleted{\unsure{arêtes orientées|arêtes repérées}}',
      'arêtes orientées; arêtes repérées',
      'Raised descenders and cancellation obscure the old second word.','low')
doubt('Edge diagram, beta-t elevated mark',r'\unsure{\beta_t^*|\beta_t}',
      'star-like elevated mark; intrusive boundary stroke',
      'The elevated cluster intersects the long cancellation/border stroke.','low')
doubt('Edge equality, complete RHS',r'\unsure{\alpha_t^*+\beta_t^*|\alpha_t+\beta_t}',
      'two star-like elevated marks; intrusive cf/border ink; possible mixed case',
      'The alpha-side cluster overlaps cf above, while the beta-side blot is more detached. Neither the witnesses nor mathematical expectation settle the ink.','low')
doubt('Edge equality, first underbrace',r"\unsure{\deleted{\alpha}\gamma'_s|\gamma'_s}",
      'old alpha overwritten before gamma-prime-s; reinforced gamma stroke',
      'A small loop lies immediately left of gamma, with no secure separation of layers.','low')
doubt('Torsor clause, old isom',r'\deleted{\unsure{isom}}','isom; another short crossed group',
      'The old letters lie beneath a heavy overstrike.','low')
doubt('Torsor group, divisor',r'\mathbb Z/\unsure{\gamma}','gamma; gamma with overwritten index or extra stroke',
      'The divisor has a loop and return but is too heavily worked to separate additional ink.','low')
doubt('Sign between circular sums',r'\unsure{\simeq|\not\simeq}',
      'simeq crossed by global cancellation; locally negated/cancelled simeq',
      'The oblique meets both horizontal bars and continues toward the global cancellation.','low')
doubt('Loop interval annotation',r'\unsure{[0,\alpha][1,\beta)|[1,\gamma][1,\beta)}',
      '[0,alpha][1,beta); [1,gamma][1,beta)',
      'Opening digit and first Greek letter remain ambiguous beside arc strokes.','low')
doubt('Pale upper algebra formula',PALE_FRACTION,
      'alpha-prime equals the half-sum; other overwritten prefix or numerator',
      'All parts are pale and partly hidden by the dark first equation.','low')
doubt('Pale overwritten alpha by beta row',r'\deleted{\unsure{\alpha}}',
      'alpha; another loop beneath the replacement',
      'Dark strokes obscure the earlier glyph.','low')
doubt('Pale older expression near gamma row',OLD_EXPR,
      'same old expression with the right parenthesis locally cancelled; old expression crossed only by later writing',
      'The right internal minus is preferable to plus, but the left primed group and precise strike scope remain open.','low')
doubt('Pale terminal equality after the old right parenthesis',r'\unsure{=}',
      'equals sign; two separate pale short strokes',
      'The two bars lie after the old closing parenthesis. They are not used to attach the isolated lower-row alpha-prime as a right-hand side.','low')
doubt('Separate lower-right pale alpha prime',r"\unsure{\alpha'}",
      'alpha-prime; pale loop with an intrusive raised stroke',
      'Distinct position is secure; exact glyph remains faint.','low')
doubt('First lower pencil equality',r"2(\alpha+\beta+\gamma)=\unsure{\alpha'+\beta'+\gamma'}",
      'three primed letters on the RHS; partly unread pale RHS',
      'Right-side loops and ticks are much fainter than the left side.','low')
doubt('Second lower pencil equality',r"2\alpha+\beta+\gamma=\unsure{\beta'+\gamma'}",
      'beta-prime plus gamma-prime; partly unread pale RHS',
      'Only portions of the right-side loops and ticks remain distinct.','low')
doubt('Third lower pencil equality',r"\beta+\gamma=\unsure{\alpha'}",
      'alpha-prime; partly unread pale RHS',
      'The final small loop and upper tick are faint.','low')
doubt('Second triangle, last a label',r'\unsure{a^1|a_1}','exponent 1; displaced subscript 1',
      'The small straight digit sits higher than the other two a indices.')
doubt('Small triangle, lowest left label',r'\unsure{c_5|b_5}','c5; damaged b5',
      'The initial is open and lacks a clear ascender, unlike the four b labels above.')
doubt('Small triangle, middle right label',r'\unsure{a_{2\,0}|a_2}',
      'a2 with an old low 0-like trace; a2 with reinforced ink',
      'The extra small loop is visible but its state and intended relation to the 2 are not secure.','low')
doubt('Small triangle, lower right label',r'\unsure{a_1}','a1; overwritten initial or index',
      'The label is heavily retraced at its joining strokes.','low')
for i in range(1,5):
    doubt(f'Small triangle, base label {i}',
          rf'\unsure{{c_{i}|\deleted{{a_{i}}}c_{i}}}',
          f'c{i}; earlier a{i} overwritten by c{i}',
          'An open outer curve and closed inner retracing cannot be separated into secure successive letters.','low')
doubt('Small triangle, pale side fragments',
      'pale loop/stem fragments reproduced in TikZ',
      'earlier A-like letters; nonletter retracing',
      'Neither fragment has enough independent structure to assign a complete earlier letter.','low')
doubt('Sphere, infinity local orientation mark',
      'short angular stroke reproduced geometrically',
      'arrowhead; reinforced local-circle stroke',
      'The tiny mark lacks the distinct separated head visible at 0 and 1.')
doubt('Counts, overworked edge word',COUNT_WORD,
      'cancelled bigones overwritten by arêtes; a single overworked bigones-like group',
      'The g descender is secure, but a separate complete live word arêtes is not.','low')
doubt('Counts, cancelled old sum',r'\deleted{$\unsure{\alpha+\beta+\gamma}$}',
      'alpha+beta+gamma; obscured signs within the crossed sum',
      'The heavy cancellation covers parts of every symbol.','low')

inventory_specs = [
 ('text','upper left','Un pantalon ...'),
 ('insertion','above pantalon','(topologique)'),
 ('display','upper left below paragraph','J to N; NB π(j) ...'),
 ('text','upper right, two-line title','Carte ... squelette pantalonique généralisé'),
 ('insertion','above Carte','orientée'),
 ('deletion','title after equivalence arrow','graphe'),
 ('deletion','upper right, complete definition','i.e. carte cellulaire ... cf ci-contre'),
 ('deletion','within cancelled definition','arêtes orientées / repérées'),
 ('insertion','raised over old arêtes group, itself included in later cancellation','drapeaux de types 0,1'),
 ('insertion','raised after sommet, itself included in later cancellation','marqué'),
 ('drawing','large left-centre','red/pencil pants; 0,1,∞; b^0,c^0,c^1,a^1,b^∞,a^∞'),
 ('diagram','centre, inside cancelled block','edge s--t, a, six local weights'),
 ('display','beside edge, cancelled','underbraced edge equality; elevated marks'),
 ('deletion','centre below edge equality','et = la donnée d’un ...'),
 ('deletion','old baseline below anti-','isom'),
 ('insertion','above old isom, inside later cancellation','anti-'),
 ('display','bottom of cancelled block','two circular sums and crossed sign'),
 ('drawing','earlier pale layer behind upper-right text','two irregular lobes, partitions, six A labels'),
 ('deletion','upper-right black drawing','pentagon, five legs, one leftward head, filled lower-right vertex'),
 ('drawing','lower left','oriented loop, two open arcs, interval label, two lower arc clusters'),
 ('display','lower centre, three paired dark rows','β+γ=α′ and cyclic inverse equations'),
 ('display','pale layer above first right equation','doubtful α′= half-sum'),
 ('deletion','pale layer beside beta row','doubtful old alpha'),
 ('display','pale layer overlapping gamma row','old primed expression, right parenthesis and doubtful terminal equals sign'),
 ('display','below and right of gamma row','separate faint alpha prime'),
 ('display','three pencil rows below equations','2(α+β+γ)=...; 2α+β+γ=...; β+γ=...'),
 ('drawing','lower-left centre','first triangle, 0/1/∞, all a/b/c indices, α=3 β=5 γ=4'),
 ('drawing','bottom centre','second triangle, dotted central sequence, three a labels, isolated oblique'),
 ('drawing','small central triangle','∞; pale 0/1 and black a/b; overwritten edge labels and fragments'),
 ('margin note','above right sphere','underlined NB; α′,β′,γ′ OK ssi ... pair'),
 ('drawing','lower right','sphere with three labelled vertices, visible wraps and local circles'),
 ('display','below sphere, upper table','trois sommets; edge total; sommets d’ordre α′,β′,γ′'),
 ('deletion','after edge total','overworked bigones/arêtes layer'),
 ('deletion','above face-count rows','old α+β+γ'),
 ('display','bottom right','two braced face rows, raised written −2, total faces'),
 ('margin note','bottom left, pale','66'),
]
for i,(kind,position,objects) in enumerate(inventory_specs,1):
    DATA['inventory'].append({
        'element':f'E{i:02d}','sheet_kind':'text',
        'hand':'unnamed hand (folio annotation; attribution uncertain)' if i==len(inventory_specs) else 'his hand',
        'kind':kind,'position':position,'first_words_or_objects':objects,'transcribed':'yes',
    })

note('The opening relates a standardly subdivided topological pair of pants with three holes to a weighted triangle. The NB visibly writes π(j) while counting edges joining j and k, followed by i≠j≠k. The descending j is preserved; a complementary-index interpretation would suggest i but is not substituted.',
     'carried as background without fault found',
     'The opening assertion was transcribed and its written index retained. No proof of the correspondence was attempted in this reading.')
note('The cancelled upper-right construction includes the raised drapeaux de types 0,1, marqué and anti- additions. The equality and torsor construction remain in the same cancelled scope. The possible elevated stars and old underbrace alpha are ink uncertainties, not readings decided from the mathematics.',
     'carried as background without fault found',
     'The edge/torsor construction was carried as background. No existence, gluing or global surface argument was proved.')
note('The main reader/root directly checked the three cyclic linear relations and their inverse: α=(β′+γ′−α′)/2 cyclically. For integer primed inputs, even total gives integrality. Nonnegative outputs additionally require the three triangle inequalities. The even triple (5,1,0) gives (−2,2,3). The written word OK is not an explicit nonnegativity assertion, so this is a qualification of one possible mathematical interpretation, not a correction of the ink.',
     'targeted proof check',
     'Performed by the main reader/root: direct addition and substitution verified the inverse formulas and the parity qualification, including the explicit (5,1,0) counterexample to parity alone implying nonnegativity.')
note('The raised face-count result visibly ends in −2 and is preserved. The main reader/root directly checked that (α−1)+(β−1)+(γ−1)=α+β+γ−3; adding two triangular faces gives F=α+β+γ−1. With V=3 and E=α+β+γ this yields Euler characteristic 2. The written −2 is therefore a local arithmetic slip; the final total already agrees with −3 plus two.',
     'targeted proof check',
     'Performed by the main reader/root: expansion of the displayed sum, addition of the two triangles, and V−E+F were checked. This does not constitute a proof of the global surface construction.')
note('Both witnesses misname the eight pants labels between the holes: the visible open crescents are c_i^0 and c_i^1. The sphere sketch separately has five visible 0–1 curves, whereas the pants sketch has four inter-hole c arcs. Both observed counts are retained; no compatibility repair is imposed.')
note('The three lower pencil equations and the earlier right-column algebra remain pale and partly overwritten. The isolated lower-right alpha-prime candidate near x1980–2000,y1520 is spatially distinct from the nearby small-triangle infinity near x1900,y1540. The additional pale alpha-prime/equality prefix above the first dark equation is also preserved, with the entire old formula unsure. Two faint bars after the older right parenthesis are retained as a doubtful terminal equals sign; no equation with the isolated alpha-prime below is inferred.')
note('The small triangle retains the apparent c5 rather than silently normalizing to the expected b5, with b5 as an alternative. The extra small loop beside the right a2 and the possible earlier a layers under the base c labels remain open. Geometric rendering of the pale side fragments does not assert that they are complete A letters.')
note('The drawing reconstruction preserves visible contour fragments, local heads, filled spots, crossed strokes and relative positions. Grey distinguishes the pale pencil layer; red follows the coloured pants contours. It does not infer unseen connecting paths beneath later writing. H’s editorial page marker, synopses, prose descriptions of drawings and typographic wrappers are not transcribed as ink; where a synopsis merely leaves geometry unspecified, no H reading error is counted for that omission.')
note('The original was viewed once for layout and each prepared left/right half once. Seventeen distinct places were enlarged. Six boundary completions—opening, card_title, cancelled_def, edge_condition, pencil_map and triangle1—extend previously clipped units and retain the original files, giving 23 PNG evidence files. They were completions of unresolved boundaries, not new crops of decided ink. Existing algebra_main and counts crops were revisited for unresolved layer placement and brace scope during completion of this first reading.')
note('Large PNG transport failures were not counted as views. Pixel-identical lossless WebP was used for loops, sphere, triangle1, triangle2 and two full text boundaries. Pants and pencil_map, and the two final drawing boundary completions, were displayed as JPEG quality98 without chroma subsampling at unchanged dimensions. Canonical PNG evidence and page-specific generators form the archive record. Transport encodings served only for display. Reduced working copies were generated but not viewed.')
note('The pale lower folio 66 is transcribed without attributing it to the author. Dark circular punch holes, paper texture and nonletter specks are physical features rather than written punctuation. No additional page heading or number was supplied.')
note('The count of 35 principal physical text/formula rows treats parallel columns on one baseline as one row. Raised additions, isolated drawing labels and their numeric indices are inventoried and covered by the independent-reading boxes separately; they have all been read against the image.')

DATA['notation'] = [
 {'sign':r'\pi(j)','meaning_or_form':'The argument has a descending j, although the adjacent edge-count wording may call for the complementary index.',
  'places':'Opening NB','universality':'One explicit occurrence; no silent replacement by i.',
  'witness_errors':'Both witnesses retain j. The proposal preserves it as written and notes the possible slip.'},
 {'sign':r'\Longleftrightarrow','meaning_or_form':'Two parallel shafts with heads at both ends.',
  'places':'Title after standard','universality':'One occurrence.',
  'witness_errors':'C gives a single-shaft longleftrightarrow; H retains the double shaft.'},
 {'sign':r'c_i^0,\ c_i^1','meaning_or_form':'Open crescent c, distinct from the closed a and tall b elsewhere in the pants figure.',
  'places':'All eight inter-hole labels in pants','universality':'All four labels at each inner circle were separately checked.',
  'witness_errors':'Both witnesses substitute a_i^0 and b_i^1.'},
 {'sign':r'\gamma,\ \gamma_s,\ \gamma_t','meaning_or_form':'A low loop with a long descending return may look sigma-like in this hand.',
  'places':'Edge weights, algebra and counts','universality':'The clear occurrences were checked individually. The torsor divisor and overwritten underbrace remain doubtful.',
  'witness_errors':'No blanket Greek-letter replacement is imposed.'},
 {'sign':r'\mathbb Z','meaning_or_form':'Doubled diagonal Z; the divisor beside it is separately overworked.',
  'places':'Cancelled torsor group','universality':'One occurrence on this page.',
  'witness_errors':'C offers mathbb/bold alternatives. The doubled letter resolves the alphabet only, not the divisor.'},
 {'sign':r'=','meaning_or_form':'Two short horizontal strokes used as shorthand for même.',
  'places':'et = la donnée','universality':'One nonmathematical shorthand occurrence here; equalities elsewhere are mathematical.',
  'witness_errors':'C doubts the sign; H preserves it.'},
 {'sign':'OK','meaning_or_form':'Rounded O followed by a tall K with two right branches.',
  'places':'NB above sphere','universality':'One occurrence.',
  'witness_errors':'C offers OK/membership; H reads membership in N and drops three primes.'},
 {'sign':'2','meaning_or_form':'A compressed curved upper entry and a short flat or curled lower exit.',
  'places':'Beta denominator; raised count ending −2','universality':'Both disputed digits checked on complete formulas.',
  'witness_errors':'C doubts both. The ink supports 2 in each, including the arithmetically mistaken count.'},
 {'sign':'Elevated star-like clusters','meaning_or_form':'Short multistroke groups can result from overlapping upper-line descenders and cancellation boundaries.',
  'places':'Diagram beta-t; equality alpha-t and beta-t','universality':'A local uncertainty; ordinary primes in clear formulas remain distinct.',
  'witness_errors':'Both witnesses omit these clusters. The proposal retains whole-formula alternatives.'},
]
DATA['abbreviations'] = [
 {'form':'ens','expansion':'ensemble'},
 {'form':'nb','expansion':'nombre'},
 {'form':'i.e.','expansion':'id est'},
 {'form':'NB','expansion':'nota bene'},
 {'form':'néc.','expansion':'nécessairement'},
 {'form':'cf','expansion':'confer'},
 {'form':'isom','expansion':'isomorphisme'},
 {'form':'ssi','expansion':'si et seulement si'},
 {'form':'=','expansion':'même (in et = la donnée)'},
]

SECOND_KINDS = {
 'opening':'insertion','card_title':'different words','cancelled_def':'struck passage',
 'pants':'handwritten number','edge_condition':'doubtful formula','torsors':'struck passage',
 'pencil_map':'struck passage','loops':'doubtful formula','algebra_main':'doubtful formula',
 'algebra_pencil':'doubtful formula','triangle1':'handwritten number',
 'triangle2':'doubtful formula','triangle3':'doubtful formula',
 'nb':'different words','sphere':'handwritten number','counts':'doubtful formula',
 'folio':'handwritten number',
}
for i,key in enumerate(ORDER,1):
    x0,y0,x1,y1=BOXES[key]
    DATA['second_boxes'].append({
        'box':f'B{i:02d}','kind':SECOND_KINDS[key],
        'x0':x0,'y0':y0,'x1':x1,'y1':y1,'reading':PARTS[key],
    })

# Use literal source excerpts for whole-drawing and cancellation comparisons.
C_TEXT=(ROOT/'packets'/PAGE/'C.tex').read_text(encoding='utf-8')
def balanced_macros(text, macro):
    results=[]
    pos=0
    start_pattern='\\'+macro+'{'
    while True:
        start=text.find(start_pattern,pos)
        if start<0: return results
        p=start+len(start_pattern)
        depth=1
        while depth and p<len(text):
            if text[p]=='{' and (p==0 or text[p-1]!='\\'): depth+=1
            elif text[p]=='}' and (p==0 or text[p-1]!='\\'): depth-=1
            p+=1
        results.append(text[start:p])
        pos=p
C_FIGURES=balanced_macros(C_TEXT,'figure')
FIG_INDEX={'pants':0,'edge_condition':1,'pencil_map':3,'loops':4,'triangle1':5,
           'triangle2':6,'triangle3':7,'sphere':8}
for row in DATA['changes']:
    key=next((k for k in BOXES if row['crop']==crop_for(k)),None)
    if row['kind']=='drawing or diagram' and key in FIG_INDEX:
        if row['c']!='absent':
            row['c']=C_FIGURES[FIG_INDEX[key]]
        row['final']=PARTS[key]
    if row['h']=='not individually specified in H drawing synopsis':
        row['h']='absent'
    if row['place']=='Scope of the cancelled definition':
        start=C_TEXT.index(r'\deleted{i.e.')
        row['c']=C_TEXT[start:].split('\n\n',1)[0]
    if row['place']=='Scope of cancellation across torseurs and both sums':
        start=C_TEXT.index(r'et \unsure{=}')
        row['c']=r'\deleted{'+C_TEXT[start:C_TEXT.index(r'\]}',start)+3]
    if row['place']=='Pentagon’s long left leg':
        row['c']=C_FIGURES[2]
    if row['place']=='Earlier pencil map, visible contours and cancellation geometry':
        row['h']='absent (only an editorial drawing synopsis)'

finish()
