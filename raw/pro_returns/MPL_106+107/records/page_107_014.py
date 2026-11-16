import sys
sys.path.insert(0,'/workspace/scratch/4bbc351d3cab/MPL_106+107/scripts')
from save_page import save
tex=r"""\mspage{f}
\[
\begin{aligned}
(A\times B)^\wedge&\mathop{=}\limits^{\mathrm{déf}}\underline{\mathrm{Hom}}((A\times B)^o,(\mathrm{Ens}))\simeq\underline{\mathrm{Hom}}(A^o\times B^o,(\mathrm{Ens}))\\
&\simeq\underline{\mathrm{Hom}}(A^o,\deleted{\mathrm{Ens}}\inserted{\widehat B})\simeq\underline{\mathrm{Hom}}_!(\widehat A^o,\deleted{\unsure{\mathrm{Ens}\,\widehat A}}\inserted{\widehat B})\\
&\simeq\underline{\mathrm{Hom}}(B^o,\widehat A)\simeq\underline{\mathrm{Hom}}_!(\widehat B^o,\widehat A)\\
&\simeq\underline{\mathrm{Hom}}_{!!}((\widehat A)^o\times(\widehat B)^o,\mathrm{Ens})\simeq\underline{\mathrm{Hom}}_!((\widehat A\times\widehat B)^o,\mathrm{Ens})
\end{aligned}
\]
\margin{le signe $!$ signifie : foncteurs commutant aux $\varprojlim$ quelconques ! le signe $!!$ a le sens analogue pour \uline{chacune} des variables séparément (\unsure{mais est équiv.} à un seul signe $!$ relatif à $(\widehat A\times\widehat B)^o$)}
\figure{\begin{tikzpicture}\draw (0,0)--(0,1.7);\end{tikzpicture}}
Si $X\in(A\times B)^\wedge$, le foncteur \deleted{\unsure{qui}} correspondant
\[
(\unsure{L|X},M)\longmapsto X(L,M):\underset{(\widehat A\times\widehat B)^o}{\underbrace{\widehat A^o\times\widehat B^o}}\mathbin{\unsure{\text{---}|\longrightarrow}}(\mathrm{Ens})
\]
est donné par
\[
X(L,M)=\mathrm{Hom}(L\boxtimes M,X)\deleted{=\unsure{\mathrm{Hom}}}\quad\text{où}\quad L\boxtimes M=p_B^*(L)\boxtimes p_A^*(M).
\]
\deleted{\uline{Corollaire}}\inserted{\uline{Proposition}} Le foncteur $(L,M)\longmapsto L\boxtimes M$ de $(\widehat A\times\widehat B)^o$ dans $\deleted{\unsure{(A\times B)^\wedge|(\widehat A\times\widehat B)^\wedge}}\inserted{(\widehat A\times\widehat B)^\wedge}$ est pleinement fidèle, il s'identifie au foncteur qui associe à tout \unsure{élém.} $(L,M)$ de $\widehat A\times\widehat B$ le foncteur
\deleted{\unsure{can.}\diagram{\begin{tikzcd}
(\widehat A\times\widehat B)^o\arrow[r] & \underline{\mathrm{Hom}}((\widehat A\times\widehat B)^o,
\end{tikzcd}}}
\unsure{contravariant} \deleted{\unsure{considéré qu'il représente}} sur $\widehat A\times\widehat B$ qu'il représente
\[
(L\boxtimes M)(L',M')\simeq\mathrm{Hom}_{\widehat A\times\widehat B}((L',M'),(L,M))=\mathrm{Hom}(L',L)\times\mathrm{Hom}(M',M)
\]
\margin{\unsure{Hom-}}
\[
\mathrm{Hom}(L'\boxtimes M',L^{\unsure{*}}\boxtimes M)
\]
En effet, la formule est vraie par définition de $L\boxtimes M$ si \deleted{\unsure{L'\in A}}

\deleted{Bien sûr, par fonctorialité, on a}
\deleted{\diagram{\begin{tikzcd}[column sep=large]
\mathrm{Hom}(L',L)\times\mathrm{Hom}(M',M)\arrow[r] & \mathrm{Hom}(L'\boxtimes M',L\boxtimes M)
\end{tikzcd}}}
$L'=a\in\mathrm{Ob}\,A$, $M'=b\in\mathrm{Ob}\,B$, \deleted{\unsure{et le}} D'autre part, pour $L,M$ fixés, et $L',M'$ variables, \unsure{les deux mbs}, comme fonctions de $L',M'$, transforment $\varinjlim$ en $\varprojlim$
\deleted{\unsure{ce qui est le cas}} \deleted{\unsure{et il paraît que}}
--- d'où la conclusion.

\uline{Corollaire}
\[
\underline{\mathrm{Hom}}(L'\boxtimes M',\deleted{\unsure{M}}L\boxtimes M)\simeq\underline{\mathrm{Hom}}(L',L)\boxtimes\underline{\mathrm{Hom}}(M',M)
\]
\uline{Dém.} Il suffit de prendre les $\mathrm{Hom}(a\boxtimes b,-)$, pour $(a,b)\in\mathrm{Ob}\,A\times B$
\[
\begin{array}{ll}
\Vert&\Vert\\
\mathrm{Hom}_{A\times B}(\underbrace{\deleted{a\times L'\boxtimes M'}\inserted{(a\boxtimes b)\times(L'\boxtimes M')}}_{(a\times L')\boxtimes(b\times M')},L\boxtimes M)&\mathrm{Hom}_A(a,\underline{\mathrm{Hom}}(L',L))\times\mathrm{Hom}_B(b,\underline{\mathrm{Hom}}(M',M))\\
\Vert&\Vert\\
\mathrm{Hom}_A(a\times L',L)\times\mathrm{Hom}_B(b\times M',M)&\mathrm{Hom}_A(a\times L',L)\times\mathrm{Hom}_B(b\times M',M)
\end{array}
\]
\margin{OK}
\mspage{13}
"""
elements=[('text','top','f'),('display','upper left','presheaf category and Hom_!, Hom_!! equivalences'),('margin note','upper right','le signe ! signifie'),('drawing','upper margin beside ! definition','vertical stroke'),('text','upper middle','Si X ∈ (A × B)^hat'),('display','upper middle','(L,M) ↦ X(L,M)'),('text','middle','est donné par'),('display','middle','X(L,M)=Hom(L⊠M,X); L⊠M=p_B*(L)⊠p_A*(M)'),('text','middle','Corollaire replaced by Proposition'),('display','middle','cancelled arrow to Hom((Ahat×Bhat)^o,'),('text','middle','contravariant sur Ahat×Bhat'),('display','middle lower','(L⊠M)(L′,M′) ≃ Hom'),('margin note','under middle formula','Hom-'),('display','middle lower','Hom(L′⊠M′,L*⊠M)'),('text','right middle','En effet, la formule est vraie'),('text','middle lower','Bien sûr, par fonctorialité'),('diagram','middle lower','cancelled Hom product comparison'),('text','lower','L′=a ∈ Ob A, M′=b ∈ Ob B; D’autre part'),('text','lower','two cancelled phrases; d’où la conclusion'),('text','lower','Corollaire'),('display','lower','internal Hom exterior-product identity'),('text','bottom','Dém. Il suffit de prendre les Hom'),('display','bottom two columns','two Hom comparison chains'),('margin note','bottom right','OK'),('text','foot','13')]
if __name__=='__main__':save(107,14,tex,elements,notes='Densely revised f sheet. Subscripts ! and !! are explicitly explained as preservation of arbitrary inverse limits, separately in the latter case. Claims exterior product fully faithful and gives a revised representability argument, then an internal-Hom corollary. Many word layers in the deleted proof and the overwritten codomain need low confidence; cancelled “ce qui est le cas / et il paraît que” are only attempted readings. The displayed definition of L⊠M uses a square product between the inverse images; retained rather than changed to cartesian product. A statement of full faithfulness should be checked for withdrawal later. Prime variables and the exclamation subscripts were read separately. Bottom paired vertical strokes are vertical equality signs, represented by Vert, not verbal quotation marks.')
