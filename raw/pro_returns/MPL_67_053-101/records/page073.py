import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from record_page import save
tex=r"""
\scanpage{73}
% archive foliation: 75
(soit $U=f(\mathring{\mathbb D})$)

\figure{\begin{tikzpicture}[scale=.9]
\draw (0,0) circle (1.6);
\draw (0,.05) .. controls (.1,.3) and (.22,.3) .. (.3,.1)
 .. controls (.45,-.05) and (.55,.18) .. (.7,.08)
 .. controls (.83,-.03) and (.95,.13) .. (1.08,.02)
 .. controls (1.2,-.1) and (1.37,.08) .. (1.6,-.02);
\fill (0,.05) circle (.03);\node[below] at (0,.05) {$0$};
\node[right] at (1.6,-.02) {$1$};
\end{tikzpicture}}

2) $f(\unsure{\omega|0})=0$, $f(\zeta)=f(\overline\zeta)=1$

\deleted{\unsure{3)} $f|\beta$ est un}
$f|(\alpha\setminus\{\zeta,\overline\zeta\})$ \deleted{est}\inserted{induit} un
homéom avec $\delta\mathbb D\setminus\{1\}$

3) \deleted{$\unsure{f(\beta)=I}$} $f|\beta$ et $f|\overline\beta$ sont bijections et
ont même image $\overline I$, \deleted{\unsure{qui est} et $\overline I\setminus\{1\}$}\inserted{contenant $\{1\}$} d'après
2), et $\overline I\setminus\{1\}$ est contenu dans $\mathring{\mathbb D}$.

4) Soient $f_1:\beta\overset\sim\longrightarrow\overline I$, $f_2:\overline\beta\overset\sim\longrightarrow\overline I$ induites par $f$,
alors $\varphi=f_2^{-1}f_1$

\uline{NB} De nouveau, $f$ est unique. On peut
résumer ce théorème d'uniformisation
au bord dans le \deleted{Scholie}

\uline{Scholie} Il y a corr. $1$-$1$ entre les
données suivantes :

a) Les homéom rectifiables \deleted{\unsure{en}}
\[
\psi:[0,1]\overset\sim-\,[0,1]
\qquad\text{avec }\psi(0)=0\quad(\text{donc }\psi(1)=1)
\]

b) Les segments topologiques \uline{rectifiables}
$\overline I$ dans $\mathbb D$, tels que
\deleted{$\overline I\cap\delta\mathbb D$ soit réduit}
\inserted{$\overline I$ admette $0,1$ comme}
extrémités et \deleted{$\unsure{\overline I\setminus\{1\}\subset\mathbb D}$}
$\overline I\cap\delta\mathbb D=\{1\}$ (i.e.
\deleted{à une extrémité de $\overline I$}
$\overline I\setminus\{1\}\subset\mathring{\mathbb D}$)

c) Les \deleted{\unsure{a}} applications continues $f:\mathbb D\longrightarrow\mathbb D$
qui ont les propriétés 1) 2) 3) de B) ci-dessus
"""
save(73,tex,[('text','top','soit U=f(D°)'),('drawing','top left','disc slit 0 1'),('text','upper right','2) f(ω)=0 f(ζ)=f(barζ)=1'),('deletion','upper right','3) f|β est un'),('text','upper right','f|(α\{ζ,barζ})'),('deletion','upper right','est'),('insertion','upper right','induit'),('deletion','upper middle','f(β)=I'),('text','upper middle','3) f|β et f|barβ'),('deletion','upper middle','qui est et I\{1}'),('insertion','upper middle','contenant {1}'),('text','middle','4) Soient f1 f2'),('text','middle','NB De nouveau f est unique'),('deletion','middle','Scholie'),('text','middle lower','Scholie Il y a corr. 1-1'),('text','lower','a) Les homéom rectifiables'),('deletion','lower','en'),('display','lower','ψ:[0,1]~—[0,1]'),('text','lower','b) Les segments topologiques rectifiables'),('deletion','lower','I∩δD soit réduit'),('insertion','lower','I admette 0 1 comme'),('deletion','lower','I\{1}⊂D'),('deletion','lower','à une extrémité de I'),('text','bottom','c) Les applications continues'),('deletion','bottom','a')],
 doubts=[('condition 2 first argument','ω','0 possible; ink has two lobes, not a clear 1; do not normalize from expected endpoint','low'),('cancelled formula at 3','f(β)=I','overlaid letters obscure entire formula','low'),('cancelled clause after image I','qui est','letter sequence crosses I bar','low'),('Scholie a map connector','plain dash with tilde','no clear arrowhead in ink','medium'),('Scholie b cancelled formula','I\{1}⊂D','multiple overwritten set symbols','low')],
 notations=[('Interval self-map in Scholie',r'\psi','psi distinguished from welding phi'),('Normalized slit',r'\overline I','with endpoints 0,1 in the standard disc')],
 abbreviations=[('corr.','correspondance')],
 leads=['Normalized welding map uniqueness asserted and summarized as one-to-one correspondence among rectifiable interval homeomorphisms, rectifiable normalized slits, and continuous disc maps satisfying B1–3.','Reading question at normalization f(ω/0)=0: printed ink conflicts with expected boundary endpoint; no correction made in transcription.','The Scholie labels maps as rectifiable although every monotone interval homeomorphism has rectifiable graph; meaning of rectifiable requires separate examination.'])
