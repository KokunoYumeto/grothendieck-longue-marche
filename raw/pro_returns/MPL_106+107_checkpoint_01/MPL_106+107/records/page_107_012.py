import sys
sys.path.insert(0,'/workspace/scratch/4bbc351d3cab/MPL_106+107/scripts')
from save_page import save
tex=r"""\mspage{e}
\diagram{\begin{tikzcd}
& (A\times B)^\wedge \arrow[dl,"p_{B*}"'] \arrow[dr,"p_{A*}"] & \\
\widehat A \arrow[ur,bend left=55,"p_B^*"] \arrow[dr,"q_{A*}=\Gamma_A"'] && \widehat B \arrow[ul,bend right=55,"p_A^*"'] \arrow[dl,"q_{B*}=\Gamma_B"] \\
& (\mathrm{Ens}) &
\end{tikzcd}}
\margin{\uline{\unsure{Récapitulation|Récapitulat$^\circ$}}}
\[
\begin{aligned}
X(a,b)&=\unsure{\Gamma|E}_{A\times B}\mathrm{Hom}(\overbrace{p_B^*(a)}^{\text{identifié à }\unsure{{}^g a}}\times\overbrace{p_A^*(b)}^{\text{identifié à }{}^d b},X)\\
&=\Gamma_{A\times B}(\underline{\mathrm{Hom}}_{A\times B}(\deleted{\unsure{p_B^*}}a\boxtimes b,X))
\end{aligned}
\quad\left\{\begin{aligned}&=\Gamma_A p_{B*}\underline{\mathrm{Hom}}\\&=\Gamma_B p_{A*}\underline{\mathrm{Hom}}\end{aligned}\right.
\]
\[
\deleted{\unsure{\simeq}}
\]
\[
{}^gX(a)=p_{\unsure{A|B}*}\underline{\mathrm{Hom}}_{A\times B}({}^ga,X)
\]
\[
{}^dX(b)=p_{B*}\underline{\mathrm{Hom}}_{A\times B}({}^db,X)
\]
\[
\deleted{\mathrm{Hom}(L\boxtimes M,X)=X(L,M)}
\]
\[
\begin{aligned}
X(L,M)&=\mathrm{Hom}_{A\times B}(L\boxtimes M,X)\\
&=\Gamma_{A\times B}\underline{\mathrm{Hom}}(L\boxtimes M,\unsure{Y|X})
\end{aligned}
\]
\[
{}^gX(L)=p_{A*}\underline{\mathrm{Hom}}_{A\times B}({}^gL,X)=\underline{\mathrm{Hom}}_B({}^gL,X)
\]
\[
{}^dX(M)=p_{\unsure{B|A}*}\underbrace{\underline{\mathrm{Hom}}_{A\times B}({}^dM,X)}_{X^M}=\underline{\mathrm{Hom}}_A({}^dM,X)
\]
\[
\underline{\mathrm{Hom}}_B(X,Y^M)\simeq\underline{\mathrm{Hom}}_B(X\otimes M,Y)
\]
\mspage{11}
"""
elements=[('text','top','e'),('diagram','upper right','presheaf projections diamond and inverse images'),('margin note','upper right beside diagram','Récapitulation'),('display','upper middle','X(a,b) = Γ Hom'),('display','middle right','Γ_A p_B* Hom; Γ_B p_A* Hom'),('display','middle','cancelled equivalence sign'),('display','middle','gX(a) = p_A* Hom'),('display','middle','dX(b) = p_B* Hom'),('display','lower middle','cancelled Hom(L⊠M,X)=X(L,M)'),('display','lower middle','X(L,M) = Hom_A×B'),('display','lower','gX(L) = p_A* Hom'),('display','lower','dX(M) = p_B* Hom; underbrace X^M'),('display','bottom','Hom_B(X,Y^M) ≃ Hom_B(X⊗M,Y)'),('text','bottom left','11')]
if __name__=='__main__':save(107,12,tex,elements,notes='Recapitulation sheet. New left superscripts g,d (not primes) on X,a,b,L,M; external product boxtimes. Diagram labels read p_B*, p_A* and p_B^*, p_A^*. First Γ is overworked and may look E; one internal-Hom terminal variable looks Y rather than X. Several projection subscripts are overwritten, and the first identified left-superscript a is poorly legible. Retain as readings, not mathematical corrections. No title page-count assertion beyond e and 11.')
