import sys
sys.path.insert(0,'MPL_31_002-051_work/scripts')
from save_page import save
s=r'''\scanpage{25}
\uline{Lemme de Cartan}

$\unsure{\mathbb T|T}$ \deleted{\unsure{un}} site, \deleted{$S\in\unsure{\mathrm{Ob}\,T|T}$}

$F$ faisceau abélien sur $T$

$n\in\mathbb Z$

\deleted{$\mathcal U\inserted{\unsure{=(U_i^\alpha)}}$ famille \unsure{filtrante} croissante de rec. de $S$\inserted{\unsure{cofinale}},}

$\mathcal M$ sous-ens de $\operatorname{Ob}T$ \deleted{formé de}
\deleted{tt}
\inserted{\figure{\begin{tikzpicture}[baseline=(n.base)]\node[draw,circle,inner sep=2pt] (n) {a};\end{tikzpicture}} $\mathcal M$ stable par produits finis}

On suppose \deleted{que}\inserted{\figure{\begin{tikzpicture}[baseline=(n.base)]\node[draw,circle,inner sep=2pt] (n) {b};\end{tikzpicture}}}
pour tt $S\in\deleted{\unsure{\operatorname{Ob}T}}\inserted{\mathcal M}$, \deleted{\unsure{il existe}}
les \uline{recouvrements} de $S$ formés par des $\in\mathcal M$ sont
cofinaux pour les rec [il suffit \unsure{$=$}, qu'ils
suffisent à effacer \deleted{$\unsure{H^q(S,)}$} tt classe
de $H^q(\unsure{S|U},F)$, $0<q\leq n$.].

\margin{\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw[thin] (.1,4.6) .. controls (1.2,4.4) and (2.2,4.35) .. (3.1,4.5);
\draw[line width=.6pt] (0,4.4) .. controls (-.08,3.5) and (.18,2.8) .. (.08,2.2);
\draw[thin] (.06,4.42) .. controls (.14,4.1) and (.1,3.9) .. (.03,3.6);
\draw[thin] (.1,2.15) .. controls (.18,1.2) and (.26,.4) .. (.26,0);
\draw[thin] (2.2,.5)--(4.3,2.6);
\node at (.18,2.75) {$\unsure{*}$};
\end{tikzpicture}}}

Conditions équivalentes

(i) $\forall S\in\mathcal M$, $H^i(S,F)=0$ pour $0<i\leq n$

(ii) $\forall S\in\mathcal M$, \deleted{\unsure{tout}} et tt rec.\inserted{$\mathcal U$} de $S$
formé par des $S_i\in\mathcal M$, on a
\[
\check H^i(\mathcal U,F)=0\quad\text{pour }0<i\leq n
\]

(iii) $\forall S\in\mathcal M$, on a
\[
\varinjlim_{\mathcal U}\check H^i(\mathcal U,F)=0\quad\text{pour }0<i\leq n
\]
où $\mathcal U$ varie sur les rec de $S$ formés
d'objets $\in\mathcal M$
\margin{\figure{\begin{tikzpicture}\draw (0,2.2)--(0,1.8);\draw (.04,.6)--(.07,0);\end{tikzpicture}}}
\margin{24}
'''
e=[('text','heading','Lemme de Cartan'),('text','premises top','T site'),('deletion','top','un'),('deletion','top right','S∈Ob T'),('text','premise 2','F faisceau abélien sur T'),('display','premise 3','n∈Z'),('deletion','upper fourth line','U famille filtrante croissante de rec. de S'),('insertion','within cancelled line','=(Ui^α)'),('insertion','right above cancelled line','cofinale'),('text','upper middle','M sous-ens de Ob T'),('deletion','upper middle right','formé de'),('deletion','below M','tt'),('insertion','between lines','a M stable par produits finis'),('drawing','between lines','circled a'),('text','middle','On suppose pour tt S'),('deletion','middle','que'),('insertion','middle above que','b'),('drawing','middle','circled b'),('deletion','middle after S∈','Ob T'),('insertion','middle above cancelled Ob T','M'),('deletion','middle right','il existe'),('text','middle','les recouvrements de S formés par des ∈M'),('text','middle bracket','il suffit = qu’ils suffisent à effacer'),('deletion','middle bracket','H^q(S,'),('display','end of bracket','H^q(S,F) 0<q≤n'),('drawing','left and across premises','marginal bracket-like strokes and diagonal'),('text','lower middle heading','Conditions équivalentes'),('display','lower middle i','∀S∈M H^i(S,F)=0'),('text','lower ii','∀S∈M et tt rec. de S'),('deletion','ii before et','tout'),('insertion','ii above rec.','U'),('text','ii next line','formé par des Si∈M on a'),('display','ii','check H^i(U,F)=0'),('text','iii','∀S∈M on a'),('display','iii','lim_U check H^i(U,F)=0'),('text','bottom','où U varie sur les rec de S'),('drawing','left lower','two vertical emphasis strokes'),('margin note','bottom left','24')]
save(25,s,e,observations='Whole and both halves read, then enlarged premise/cancellation and lower-formula crops compared. Script M and covering U are rendered calligraphically; the first doubled T remains an alphabet doubt. A short equals-like mark after il suffit is retained rather than expanded. The long faint pencil diagonal is represented as a stroke, not treated as cancellation of all live mathematical text. Reused reverse-side type visible through the paper is not a separate front-side inscription.')
