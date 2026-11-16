import sys
sys.path.insert(0,'/workspace/scratch/4bbc351d3cab/MPL_106+107/scripts')
from save_page import save
tex=r"""
\mspage{g}
\uline{Corollaire} $p_B^*: \widehat A\mathbin{-}\widehat{(A\times B)}$ commute aux $\underline{\operatorname{Hom}}$
(\unsure{$d^{\circ}$} symétrique pour $p_A^*$)

Il suffit de prendre $\deleted{\unsure{M'=e_{\widehat B},M=}}\quad M'=M=e_{\widehat B}$. On trouve
\[
\underline{\operatorname{Hom}}(L'\boxtimes M',L\boxtimes e_{\widehat B})\simeq\underline{\operatorname{Hom}}(L',L)\boxtimes e_{\widehat B}
\]
en particulier, faisant $L'=e_{\widehat A}$ et changeant $M'$ en $M$
\[
\underline{\operatorname{Hom}}(e_{\widehat A}\boxtimes M,L\boxtimes e_{\widehat B})\xleftarrow{\sim}L\boxtimes e_{\widehat B}
\]
--- on retrouve ici la \deleted{\unsure{flèche}} \unsure{cette} flèche canonique
\diagram{\begin{tikzcd}\underline{\operatorname{Hom}}(P,Q)&Q\arrow[l]\end{tikzcd}}
valable en tt \unsure{catégorie|catégories}, \deleted{\unsure{munie de produits}}, \deleted{\unsure{fini}}.

Dans la notation $X^M$, si on identifie $M$ à $e_{\widehat A}\boxtimes M=p_A^*(M)$, et de \unsure{même} $L$ à $L\boxtimes e_{\widehat B}\simeq p_B^*(L)$, on trouve donc
\[
L^M=L\qquad\text{pour }\unsure{L\in\operatorname{Ob}\widehat A|L\operatorname{Ob}\widehat A},\ M\in\operatorname{Ob}\widehat B
\]
\mspage{15}
"""
elements=[('text','top','g'),('text','top heading','Corollaire p_B^*'),('text','parenthetic row','d° symétrique'),('text','proof opening','Il suffit de prendre'),('display','upper middle','Hom(L boxtimes M,L boxtimes e)'),('text','middle','en particulier, faisant'),('display','middle','Hom(e boxtimes M,L boxtimes e) <-'),('text','middle below','on retrouve ici la'),('diagram','middle below','Hom(P,Q) <- Q'),('text','right of diagram','valable en tt'),('text','lower paragraph','Dans la notation X^M'),('display','last row','L^M=L'),('text','foot','15')]
if __name__=='__main__':save(107,16,tex,elements,notes='Corollary that p_B^* commutes with internal Hom and symmetric statement for p_A^*. Replaces M,Mprime by final objects, then states Hom(e_A boxtimes M,L boxtimes e_B) <-~ L boxtimes e_B and L^M=L. The prose around the canonical arrow and its crossed-out qualification is very compressed; doubtful readings preserved. Top category connector has no distinct arrowhead. Possible future correction must be tracked, not anticipated.')
