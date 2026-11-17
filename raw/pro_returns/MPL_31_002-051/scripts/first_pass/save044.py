import sys
sys.path.insert(0,'MPL_31_002-051_work/scripts')
from save_page import save
text=r'''\scanpage{44}

\uline{1)} Soit $G$ groupe fini d'automorphismes d'un anneau \unsure{semi-local} $O$.
$G$ est transitif sur les idéaux maximaux $\underline m$, soit $G_d$ le stabilisateur de $\underline m_0$, et $G_i\subset G_d$ l'ens des \unsure{éléments} de $G_d$ qui définissent l'automorphisme identique de $O/\underline m$.
Sous ces conditions

a) Il existe $x\in O^{G_i}$ tel que $T_{G/G_i}x=1$. Donc pour $\unsure{\forall}$ $G$-$O$-modules $M$, on a
\[
\widehat H(G,M)=\widehat H(G_i,M)^{G/G_i}.
\]
\unsure{Doute|D'autre} pour qu'on ait $1\in T_G O$, i.e. $\widehat H(G,M)=0$ $\forall$ $M$, il f. et s. que $[G_i:e]$ ne soit pas multiple de la caractéristique $p$ de $O/\underline m$.

b) Si $G_i=\{e\}$, on a $H^1(G,O^*)=\{e\}$.

Plus généralement, quel que soit $G_i$, l'hom naturel
\[
H^1(G,O^*)\longrightarrow H^1\bigl(G_i,(\underline O^{\deleted{\unsure{G}}}/m)^*\bigr)
\]
est bijectif (?). Qu'en est-il dans le cas \deleted{$\unsure{G}$} des $\operatorname{Gl}(n,\underline O)$ au lieu de $\unsure{O^\times|O^*}$ ?
\margin{?}
\figure{\begin{tikzpicture}\draw (0,0)--(0,-1.25);\end{tikzpicture}}

Dans a, \unsure{entre}
\[
\begin{aligned}
\underbrace{\overline{\widehat H(G,M)}=\widehat H(G,\overline M)}_{\substack{\text{\unsure{justification}}\\\text{par Zariski;}\\\text{il y a des}\\\text{hyp. \unsure{noethériennes}}\\\text{à faire ??}}}
&=\widehat H\left(G,\bigoplus_{s\in G/G_d}s.\overline M_{\underline m_0}\right)
=\widehat H(G_d,\overline M_{\underline m_0})\\
&=\overline{H(G_d,M_{\underline m_0})}.
\end{aligned}
\]
\margin{dans le cas où $O$ est de dim $1$,\par \unsure{car} \unsure{annule} $\widehat H(G,M)$ !}
\figure{\begin{tikzpicture}\draw (0,0)--(0,-1.7);\end{tikzpicture}}

Considérons alors le diagramme :
\diagram{\begin{tikzcd}[column sep=large,row sep=large]
\widehat H(G,M)\arrow[r,"\sim"]\arrow[d,"\unsure{\sim}"'] & \widehat H(G_i,M)_{\deleted{\unsure{\underline m_0}}}^{G/G_i}\arrow[r,"\unsure{\mathrm{inj}}","\alpha"'] & \widehat H(G_i,M_{\underline m_0})^{G_d/G_i}\\
\widehat H(G_d,M)^{G/G_d}\arrow[rr,"\beta"] & & \widehat H(G_d,M_{\underline m_0})\simeq\widehat H(G_d,M)_{O_d-m_0O_d}\arrow[u,"\unsure{\sim}"']
\end{tikzcd}}
\margin{$\alpha$ et $\beta$ sont injectifs ; images denses}
\margin{on passe au quotient !}
\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw[gray] (0,-2.1)--(0,0)--(2.1,.15)--(1.9,-.75).. controls (1.8,-1.1) and (2.8,-.9)..(3.7,-1.1).. controls (4,-1.4) and (4.2,-1.9)..(3.5,-2.05)--(.2,-1.95);
\draw (2.6,-.45).. controls (2.55,-.8) and (2.65,-1.1)..(2.7,-1.35);
\end{tikzpicture}}

\mspage{43}'''
elements=[
('text','top','1) Soit G groupe fini'),('text','upper','G est transitif'),('text','upper','Sous ces conditions'),('text','upper','a) Il existe x'),('display','upper middle','Hhat(G,M)=Hhat(Gi,M)^(G/Gi)'),('text','middle','Doute pour qu’on ait'),('text','middle','b) Si Gi={e}'),('text','middle','Plus généralement'),('display','middle','H1(G,O*) → H1(Gi,(O/m)*)'),('deletion','display numerator','G superscript on O'),('text','below display','est bijectif (?). Qu’en est-il'),('deletion','same paragraph','G'),('margin note','left','?'),('drawing','left of paragraph','vertical marking stroke'),('text','lower','Dans a, entre'),('display','lower','bar Hhat(G,M)=Hhat(G,bar M)'),('margin note','under first equality','justification par Zariski; il y a des hyp.'),('drawing','under equality','underbrace'),('margin note','left oblique','dans le cas où O est de dim 1'),('drawing','left of equation','vertical marking stroke'),('text','lower','Considérons alors le diagramme'),('diagram','bottom','Hhat(G,M) → Hhat(Gi,M) → Hhat(Gi,Mm0)'),('deletion','diagram top middle','m0 subscript'),('margin note','diagram right','α et β sont injectifs ; images denses'),('margin note','pencil beside diagram','on passe au quotient !'),('drawing','diagram right','pencil enclosure and ink vertical bracket'),('text','bottom left','43')]
save(44,text,elements,observations='Whole page and both halves inspected, including enlarged top, question, equality, diagram, underbrace annotation and rotated marginal note. The opening word before the trace criterion is uncertain (Doute / D’autre); no missing part is supplied. The final equality has a plain H under the bar. Small margin wording and cancelled symbols remain explicit doubts; no mathematical correction was made.')
