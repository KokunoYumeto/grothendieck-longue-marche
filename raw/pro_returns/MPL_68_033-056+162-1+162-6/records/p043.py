import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from record_page import record
record(43,r'''
\scanpage{43}
% archive foliation: 42
Si $u$ nilpotent, il f et s. que $\exp u$ soit un autom d'algèbre.

Op. sur $\operatorname{Hom}_K(M,N)$, quand $\overline G_a$ (resp. $G_a$) opère sur $M$ par $\bar e_u$ (resp. $e_u$), sur $N$ par $\bar e_v$ (resp. $e_v$). Alors il opère sur $\operatorname{Hom}_K(M,N)$ par $\bar e_\delta$ $(e_\delta)$ où
\[
\delta(f)=vf-fu
\]
Mais en \unsure{tte|tt} \uline{rigueur} $\bar e_\delta$ et $e_\delta$ ne sont définis ici que si $\operatorname{Hom}_K(M,N)$ est \inserted{\unsure{is. à}} un foncteur de la forme $W(M)$, ce qui n'est guère assuré que si $M$ proj. de t.f.

Mais on peut généraliser théorie de l'exponentielle aux \deleted{\unsure{les}} endomorphismes de tt $K$-foncteur $\mathcal M$ en $\unsure{\mathcal O|\mathbf Q}$-modules
\diagram{\begin{tikzcd}[row sep=large,column sep=large]
\mathcal M(K')\arrow[d,"\text{est }(K'\to K'')\text{-semi-linéaire}"]&\text{est un }K'\text{-module}\\
\mathcal M(K'')&
\end{tikzcd}}
Alors $\operatorname{End}_K(\mathcal M)$ est une $K$-algèbre.

a) Si $u\in N(\operatorname{End}_K(\mathcal M))$, $\exp u\in\operatorname{End}_K(\mathcal M)$

et aussi $\exp(\lambda u)$ $\forall\lambda\in G_{a\unsure{K}}(K')\simeq K'$ défini $\in\operatorname{End}_{K'}(\mathcal M_{K'})$

On trouve sur $\mathcal M$ une structure de $G_a$-Module \unsure{les}
''',[
('text','top','Si u nilpotent, il f et s. que exp u soit un autom'),
('text','upper','Op. sur Hom_K(M,N)'),
('display','upper-middle','delta(f)=vf-fu'),
('text','middle and fold','Mais en tte rigueur bar e_delta et e_delta'),
('insertion','above est un','is. à'),
('text','below fold','Mais on peut généraliser théorie de lexponentielle'),
('deletion','after aux','les'),
('diagram','lower middle','Mcal(K prime) down to Mcal(K doubleprime); semilinearity'),
('text','lower','Alors End_K(Mcal) est une K-algèbre'),
('text','lower','a) Si u in N(End_K(Mcal))'),
('text','near bottom','et aussi exp(lambda u) forall lambda in G_aK(K prime)'),
('text','bottom','On trouve sur Mcal une structure de G_a-Module les')
],[
('Mais en ... rigueur','tte','tt; compact crossed abbreviation','medium'),
('insertion after est','is. à','first abbreviation faint','medium'),
('deletion after aux','les','initial strokes may include another short fragment','low'),
('functor module alphabet','calligraphic O','bold Q; overwritten rounded letter','low'),
('G_a base in lambda expression','K','small subscript very faint','medium'),
('last word at bottom edge','les','unfinished continuation; strokes faint','low')])
