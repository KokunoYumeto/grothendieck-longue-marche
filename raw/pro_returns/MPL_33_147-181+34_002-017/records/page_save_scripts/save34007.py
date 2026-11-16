import sys
sys.path.insert(0,'MPL_33_147-181+34_002-017_work/records')
from workflow import save_page
tex=r'''\scanpage{7}
\mspage{5}

schéma fini étale sur $S$, alors on a des isomorphismes
\[
\operatorname{Hom}_S(\bar s,S')\xleftarrow{\sim}\operatorname{Hom}_S(\deleted{\unsure{\bar s}}\widetilde S,S')\xrightarrow{\sim}\operatorname{Hom}_S(\deleted{\unsure{\eta}}\bar\eta,S')
\]
d'où un isom canonique
\[
(2.3.1)\qquad\operatorname{Hom}_S(\bar s,S')\simeq\operatorname{Hom}_S(\bar\eta,S'),
\]
fonctoriel en $S'$ (isom. des \inserted{2} foncteurs ``fibre'' sur la cat. des rev. étales de $S$, définis resp. par les pts géom. $\bar\eta$ et $\bar s$). Faisant $S'=\mu_n$, $n$ \inserted{entier} inversible dans $k$, on trouve en particulier un isom
\[
(2.\unsure{1|3}.2)\qquad \mu_n(\bar s)={}_n\bar k^*\simeq\mu_n(\bar K)={}_n\bar K^*,
\]
d'où par passage à la limite sur les puissances du nb premier $\ell$, $\ell\ne\operatorname{car}.k$ :
\[
(2.3.3)\qquad T_\ell(\bar k^*)\simeq T_\ell(\bar K^*).
\]
\deleted{On notera.} Les deux membres, \deleted{qui} sont des modules libres de rang 1 sur $\mathbf Z_\ell$, \deleted{\unsure{que l'on désigne}} \inserted{qu'on identifie} désormais et désigne par $\mathbf Z_\ell(1)$. \deleted{Sa puissance} \inserted{Sa puiss. tensorielle} nième $(n\in\mathbf Z)$ est notée $\mathbf Z_\ell(n)$. Donc on a
\margin{$(2.3.4)\qquad\mathbf Z_\ell(1)\simeq\cdots$}
\[
(2.3.4)\qquad \mathbf Z_\ell(n)\simeq\varprojlim_\nu\mu_{\ell^\nu}(\bar k^*)^{\otimes n}\simeq\varprojlim_\nu\mu_{\ell^\nu}(\bar K^*)^{\otimes n}.
\]
Les isomorphismes \deleted{\unsure{sont compatibles aux}} opérations de $\pi$ sur $\mu_{\unsure{n}}(\bar K^*)$ \inserted{et} \unsure{ou} celles de $\pi_0$ sur $\mu_n(\bar k^*)$ etc\ldots compte tenu de l'épimorphisme canonique $\pi\longrightarrow\pi_0$.
\margin{6}
'''
e=[('text','top','schéma fini étale sur S'),('display','top','Hom_S(sbar,S′) ← Hom_S(Stilde,S′) → Hom_S(etabar,S′)'),('deletion','top display middle','sbar'),('deletion','top display right','eta'),('text','upper','d’où un isom canonique'),('display','upper','(2.3.1) Hom_S(sbar,S′)'),('text','upper-middle','fonctoriel en S′'),('insertion','after des','2'),('insertion','after n','entier'),('display','middle','(2.1|3.2) μn(sbar)'),('text','middle','d’où par passage à la limite'),('display','middle-lower','(2.3.3) Tℓ(kbar*)'),('deletion','lower','On notera'),('deletion','lower','qui'),('text','lower','Les deux membres'),('deletion','lower right','que l’on désigne'),('insertion','lower right above deletion','qu’on identifie'),('deletion','lower right','Sa puissance'),('insertion','lower left','Sa puiss. tensorielle'),('margin note','interlinear left','(2.3.4) Zℓ(1) ≃ ...'),('display','lower','(2.3.4) Zℓ(n)'),('text','bottom','Les isomorphismes'),('deletion','bottom','sont compatibles aux'),('insertion','bottom interlinear','et'),('margin note','bottom left','6')]
save_page(34,7,tex,e,remarks='The isolated interlinear (2.3.4) Zℓ(1)≃... is preserved separately; its dots are actually present. The deleted compatibility phrase leaves the final sentence syntactically rough, which has not been repaired. The second equation label appears 2.1.2 rather than the expected 2.3.2; both readings are marked.')
