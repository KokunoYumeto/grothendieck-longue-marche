import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from record_page import save
tex=r"""
\scanpage{84}
% archive foliation: 86
\fbox{\unsure{Modulis|Moduli} $M_{0,4}$ et l'octaèdre}

$I$ ens de card. 4 d'où
\[
J=\mathcal P_{2,2}(I),\quad V(J)\ \text{plan vectoriel sur }\mathbb F_2\text{ avec }V(J)^*\simeq J,
\]
$V(J)\subset\unsure{\mathfrak S}_I$ formé de l'identité et des ``bitranspositions''.

On s'intéresse aux droites projectives (sur $\mathbb C$ disons --- \unsure{ça}
marcherait sur tt corps $k$ \inserted{de car. $\ne2$}) munies de $I\hookrightarrow X$.
(plus précisément $I_{\mathbb C}\hookrightarrow X$, ou $I\longrightarrow X(\mathbb C)$ \ldots).
L'opération de $V(\unsure{I|J})$ sur $I$ se prolonge en une opération de
$V(J)$ sur $X$
\[
V(J)\hookrightarrow G_X=\operatorname{Aut}(X)
\]
Soit
\[
\begin{gathered}
S=\text{ens des pts dans }X\text{ qui sont fixes par un}\\
\text{élément de }J=V(J)^*\\
\operatorname{card}S=6
\end{gathered}
\]
\margin{\uline{\unsure{Commençons}} \uline{par \unsure{ça}}}
En fait, on trouve que \deleted{\unsure{pour les}}\inserted{les} opérations \inserted{fidèles} d'un gr. abstrait $V$
sur un $X$, i.e. les plongements $V(\unsure{J})\hookrightarrow G_X$, sont tous
équivalents (modulo autom. intérieurs de $G_X$)
et sont (pour une base fixée \inserted{$e_0,e_1$}) équivalentes à l'opération sur $\mathbb P^1$
\diagram{\begin{array}{rcll}
u(e_0)&=(z\longmapsto-z)=\begin{pmatrix}-1&0\\0&1\end{pmatrix}& &\text{pts fixes }0,\infty\\[3pt]
u(e_1)&=(z\longmapsto1/z)=\begin{pmatrix}0&1\\1&0\end{pmatrix}& &\text{pts fixes }\pm1\\[3pt]
u(e_0+e_1)&=(z\longmapsto-1/z)=\begin{pmatrix}0&-1\\1&0\end{pmatrix}& &\text{pts fixes }\pm i
\end{array}}
Les \deleted{\unsure{quatre groupes}}\inserted{sous-groupes} isom. à $D_2$ de $G_X$ correspondent 1-1 aux
parties $S$ de cardinal 6 de $X$, isom. à $(\mathbb P_1,\{0,\infty,\pm1,\pm i\})$.
\margin{parties octaédriques d'une droite projective}
Le normalisateur $\Gamma$ d'un tel \deleted{\unsure{D_2}} sous-groupe $V$ \inserted{dans $G_X$} est isomorphe
au groupe \deleted{des rotations} $\unsure{\mathfrak S}_4$ (de façon non canonique), plus
précisément, si $V=V(J)$ avec $J=\unsure{\mathcal P}(I)$ \inserted{i.e. si $I$ est un $V$-torseur}, on trouve \deleted{des} iso
de suites exactes
\diagram{\begin{tikzcd}[column sep=small]
&& \deleted{\unsure{\operatorname{Aut}(I)}} \arrow[d,equal] && \\
\unsure{1} \arrow[r] & V \arrow[r] \arrow[d,equal] & \unsure{\mathfrak S}_I \arrow[r] \arrow[d] & \operatorname{Aut}(V) \arrow[r,dash] \arrow[d,equal] & 1 \\
1 \arrow[r] & V \arrow[r] & \Gamma \arrow[r] & \operatorname{Aut}(V) \arrow[r,dash] & 1
\end{tikzcd}}
défini modulo autom. intérieurs par un élément de $V$.
Quand $I$ est le torseur trivial, \unsure{se donner|on donne} un tel \deleted{iso}\inserted{iso d'ext.}
"""
save(84,tex,[('text','boxed title','Modulis M0,4 et l’octaèdre'),('text','top','I ens de card. 4'),('display','upper','J=P2,2(I), V(J)'),('text','upper','V(J) subset symmetric group'),('text','upper third','On s’intéresse aux droites projectives'),('insertion','above munies','de car. neq2'),('text','upper middle','L’opération de V(I)'),('display','middle','V(J) into G_X=Aut(X)'),('display','middle','S=ens des pts; card S=6'),('margin note','left middle','Commençons par ça'),('text','middle lower','En fait, on trouve que'),('deletion','before opérations','pour les'),('insertion','above deleted pour les','les'),('insertion','above d’un gr.','fidèles'),('insertion','after base fixée','e0,e1'),('diagram','lower middle three rows','u(e0); u(e1); u(e0+e1); matrices; pts fixes'),('text','lower','Les sous-groupes isom. à D2'),('deletion','after Les','quatre groupes'),('insertion','above quatre groupes','sous-groupes'),('margin note','left lower','parties octaédriques d’une droite projective'),('text','lower','Le normalisateur Gamma'),('deletion','before sous-groupe','D2'),('insertion','above est isomorphe','dans G_X'),('deletion','before symmetric group 4','des rotations'),('insertion','above on trouve','i.e. si I est un V-torseur'),('deletion','before iso','des'),('diagram','bottom','two exact sequences and vertical maps'),('deletion','above middle object in diagram','Aut(I)'),('text','bottom two lines','défini modulo autom. intérieurs'),('deletion','last line','iso'),('insertion','last line','iso d’ext.')],doubts=[('title','Modulis','Moduli; terminal stroke uncertain.','medium'),('symmetric-group glyph throughout','mathfrak S','Large curled S resembles a G; font not fully decidable.','medium'),('upper paragraph','ça marcherait','Initial short word faint; marcherait fairly clear.','medium'),('L’opération de V(I)','I','J; the index inside this first occurrence looks like I, unlike next V(J).','low'),('left marginal heading','Commençons par ça','Very compressed diagonal writing.','low'),('deleted words before opérations','pour les','Second word may be a different short word.','low'),('deletion above sous-groupes','quatre groupes','Both words crossed; first may instead be a different qualifier.','low'),('J=P(I)','P','Retraced set-construction glyph; no 2,2 indices securely visible here.','low'),('last line','se donner','on donne; both initial pronoun and infinitive ending uncertain.','low'),('exact-sequence terminal edges','plain lines','No unambiguous arrowheads on the two rightmost edges.','medium')],notations=[('new section symmetric group',r'\unsure{\mathfrak S}_I','Curled S-like letter; consistently distinguished from plain G_X.'),('partitions',r'\mathcal P_{2,2}(I)','Two-by-two partition set.'),('V nonzero elements',r'V(J)^*','Star is nonzero elements, not a dual; compared with earlier T*.'),('dihedral group',r'D_2','D with subscript 2.'),('normaliser',r'\Gamma','Gamma in the lower exact sequence.')],abbreviations=[('tt','tout'),('car.','caractéristique'),('autom.','automorphisme(s)'),('isom.','isomorphe(s)'),('ext.','extensions')],leads=['New title Moduli M0,4 et l’octaèdre; no explicit page count.','Four labels produce Klein-four bitranspositions, a six-point fixed locus and octahedral normaliser; verify exact sequences and characteristic restrictions.','Manuscript says all faithful Klein-four projective-line actions equivalent modulo inner automorphisms; elementary matrices and fixed points provided.'])
