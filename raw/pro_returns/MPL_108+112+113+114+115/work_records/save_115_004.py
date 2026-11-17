from record import save_page
save_page(115,4,r'''\scanpage{4}
\mspage{\textcircled{1}}
% archive foliation: 3
\margin{Cas $B=A^\circ$, d'où élément canonique
$H=H_A\in\widehat{(A\times A^\circ)}$.
D'où $A\hookrightarrow\widehat A$, $A^\circ\hookrightarrow A^\vee$
(les plongements can)
\[
A^{\vee\circ}\xrightarrow{!}\widehat A,\quad
\widehat A^\circ\xrightarrow{!}A^\vee\quad(\text{comm. aux }\varprojlim)
\]
\[
\widehat A^\circ\times A^{\vee\circ}\xrightarrow{!!}(\operatorname{Ens})
\]
(bif. can. sur $\widehat A,A^\vee$)
\inserted{i.e. faisceaux sur $A^\vee$ repr. $\widehat A$;
\unsure{i.e. ds} $\widehat A$ repr. $A^\vee$}
(et $\widehat A\unsure{\longrightarrow|{-}}\widehat A$ et
$A^\vee\unsure{\longrightarrow|{-}}A^\vee$ sont les identités)
\[
\widehat A\simeq\underline{\operatorname{Hom}}^!(\widehat A^\circ,\operatorname{Ens})
\simeq\underline{\operatorname{Hom}}_!(A^\vee,\operatorname{Ens})
\]
\[
A^\vee\simeq\underline{\operatorname{Hom}}^!(A^{\vee\circ},\operatorname{Ens})
\simeq\underline{\operatorname{Hom}}_!(\widehat A,\operatorname{Ens})
\]
et \unsure{item|idem} pour $B$}

\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw (0,0) .. controls (1.2,1) and (1,2.5) .. (2.4,2.7)
 .. controls (3.4,3) and (3.4,3.5) .. (4.2,3.5)
 .. controls (5.1,3.8) and (5.2,5) .. (6,5.8);
\end{tikzpicture}}

\margin{$\underline{\operatorname{Hom}}_!$: sous-cat. pleine de $\underline{\operatorname{Hom}}$
formée des foncteurs commutant aux $\varinjlim$.

$\underline{\operatorname{Hom}}^!$: sous-cat. pleine de $\underline{\operatorname{Hom}}$
formée des foncteurs commutant aux $\varprojlim$.}

\diagram{\begin{tikzcd}[column sep=small,row sep=large]
&&\widehat{(A\times B)}\arrow[dl,no head,"\simeq"']\arrow[dr,no head,"\simeq"]&&\\
&\underline{\operatorname{Hom}}(B^\circ,\underline{\widehat A})
&&\underline{\operatorname{Hom}}(A^\circ,\widehat B)&\\
\underline{\operatorname{Hom}}_!(B^\vee,\widehat A)\arrow[ur,"\simeq"]
&\underline{\operatorname{Hom}}^!(\widehat B^\circ,\underline{\widehat A})\arrow[u,"\simeq"']\arrow[dr,"\simeq"']
&&\underline{\operatorname{Hom}}^!(\widehat A^\circ,\widehat B)\arrow[u,"\simeq"]\arrow[dl,"\simeq"]
&\underline{\operatorname{Hom}}_!(A^\vee,\widehat B)\arrow[ul,"\simeq"']\arrow[d,no head,"\simeq"]\\
\underline{\operatorname{Hom}}_{!!}(A^\vee\times B^\vee,(\operatorname{Ens}))\Big]\arrow[u,"\simeq"]
&&\begin{gathered}\underline{\operatorname{Hom}}^{!!}(\widehat A^\circ\times\widehat B^\circ,(\operatorname{Ens}))\\=\operatorname{Bifais}(\widehat A,\widehat B)\end{gathered}
&&\underline{\operatorname{Hom}}_{!!}(A^\vee\times B^\vee,(\operatorname{Ens}))
\end{tikzcd}}

\diagram{\begin{tikzcd}
&A\times B\arrow[dl,"p_B"']\arrow[dr,"p_A"]&\\
A\arrow[dr,no head,"q_A"']&&B\arrow[dl,"q_B"]\\
&e&
\end{tikzcd}}

\[
\left\{\begin{aligned}
\underline{\operatorname{Hom}}_A(X,Y)&\overset{\mathrm{def}}=p_{B*}\underline{\operatorname{Hom}}_{A\times B}(X,Y)\\
\underline{\operatorname{Hom}}_B(X,Y)&\overset{\mathrm{def}}=p_{A*}\underline{\operatorname{Hom}}_{A\times B}(X,Y)\\
\operatorname{Hom}_{A\times B}(X,Y)&\simeq\Gamma_{A\times B}\underline{\operatorname{Hom}}_{A\times B}(X,Y)
\simeq\Gamma_A\underline{\operatorname{Hom}}_A(X,Y)
\simeq\Gamma_B\underline{\operatorname{Hom}}_B(X,Y)
\end{aligned}\right.
\]
\margin{$X,Y\in\operatorname{Ob}\widehat{(A\times B)}$}

\[
\left\{\begin{aligned}
{}^sX(L)&=\underline{\operatorname{Hom}}_B(p_B^*L,X)
=p_{A*}\underline{\operatorname{Hom}}_{A\times B}(p_B^*L,X)\\
{}^dX(M)&=\underline{\operatorname{Hom}}_A(p_A^*M,X)
=p_{B*}\underline{\operatorname{Hom}}_{A\times B}(p_A^*M,X)\\
X(L,M)&=\operatorname{Hom}_{A\times B}(L\boxtimes M,X)
\simeq\operatorname{Hom}_{\widehat A}(L,{}^dX(M))
\simeq\operatorname{Hom}_{\widehat B}(M,{}^sX(L))
\end{aligned}\right.
\]
\margin{$L\in\operatorname{Ob}\widehat A$\quad$M\in\operatorname{Ob}\widehat B$}
où $L\boxtimes M=p_B^*L\times p_A^*M$.

\inserted{Ces formules sont particulièrement intéressantes pour
$L=a\in\operatorname{Ob}A$ $M=b\in\operatorname{Ob}B$}

Soit $X$, définissant $B^\circ\longrightarrow\widehat A$
(savoir $b\longmapsto{}^dX(b)=\underline{\operatorname{Hom}}_B(p_B^*(L),X)$),
\unsure{composons} avec $\widehat A\longrightarrow\operatorname{Ens}$ défini
par un $L_0\in\operatorname{Ob}\widehat A$, par
$L'\longmapsto\operatorname{Hom}(L_0,L')$, on trouve
$B^\circ\longrightarrow\operatorname{Ens}$: i.e.
\deleted{$\unsure{b\longmapsto\operatorname{Hom}}$}
\inserted{$b\longmapsto\operatorname{Hom}_{\widehat A}(L_0,{}^dX(b))$, i.e.}
un élément de $\widehat B$, qui n'est autre que
$\underline{\operatorname{Hom}}_B(p_B^*\unsure{L_0},X)={}^sX(L_0)$.
Interprétation duale pour ${}^dX(M)$.

\[
(L,M)\longmapsto L\boxtimes M:\quad
\widehat A\times\widehat B\longrightarrow\widehat{(A\times B)}
\]
est pleinement fidèle,
\diagram{\begin{tikzcd}
\widehat{(A\times B)}\arrow[d,"\unsure{\simeq}"]\\
\underline{\operatorname{Hom}}^{!!}(\widehat A^\circ\times\widehat B^\circ,\operatorname{Ens})
\subset\widehat{(\widehat A\times\widehat B)}
\end{tikzcd}}
le composé est le foncteur canonique dit ``de Yoneda'' pour
$\widehat A\times\widehat B$.

\[
\operatorname{Hom}_{A\times B}
(\unsure{L'^{\xi}|L^{\xi}}\boxtimes\unsure{M'^{\xi}|M^{\xi}},
L^{\unsure{\xi|\sharp}}\boxtimes M^{\unsure{\xi|\sharp}})
\simeq
(L^{\unsure{\xi|\sharp}}\boxtimes M^{\unsure{\xi|\sharp}})
(L'^{\unsure{\xi|\sharp}}\boxtimes M'^{\unsure{\xi|\sharp}})
\xleftarrow{\sim}
\operatorname{Hom}_{\widehat A}(L'^{\unsure{\xi|\sharp}},L^{\unsure{\xi|\sharp}})
\times\operatorname{Hom}_{\widehat B}(M'^{\unsure{\xi|\sharp}},M^{\unsure{\xi|\sharp}})
\]
\[
\underline{\operatorname{Hom}}_{A\times B}
(L'^{\unsure{\xi|\sharp}}\boxtimes M'^{\unsure{\xi|\sharp}},L^{\unsure{\xi|\sharp}}\boxtimes M^{\unsure{\xi|\sharp}})
\simeq\underline{\operatorname{Hom}}_{\widehat A}(L'^{\unsure{\xi|\sharp}},L^{\unsure{\xi|\sharp}})
\boxtimes\underline{\operatorname{Hom}}_{\widehat B}(M'^{\unsure{\xi|\sharp}},M^{\unsure{\xi|\sharp}})
\]
\margin{p.ex.}
\[
\underline{\operatorname{Hom}}_{A\times B}
(L^{\unsure{\xi'}}\boxtimes M',
\underbrace{L^{\unsure{\xi|\sharp}}\boxtimes e_{\widehat B}}_{p_B^*L^{\unsure{\xi|\sharp}}})
\simeq
\underbrace{\underline{\operatorname{Hom}}_{\widehat A}(L',L^{\unsure{\xi|\sharp}})\boxtimes e_{\widehat B}}_{p_B^*\underline{\operatorname{Hom}}_{\widehat A}(L,L')}
\]
\margin{en particulier faisant $L'=e_{\widehat A}$ et changeant $M'$ en $M$}
\[
\underline{\operatorname{Hom}}_{A\times B}(p_A^*(M),p_B^*L)
\xleftarrow{\sim}p_B^*L
\]
(la flèche étant la flèche canonique
$\underline{\operatorname{Hom}}(\alpha,\beta)\longleftarrow\beta$)

Posant $X^M\overset{\mathrm{def}}=\underline{\operatorname{Hom}}_{A\times B}(p_A^*M,X)$,
on trouve donc $(p_B^*L)^M\simeq p_B^*L$

\unsure{p}
''',[
('margin note','upper left','Cas B=A opposite; H=H_A'),
('display','upper left embeddings','A into Ahat; A opposite into Avee'),
('display','upper left limit extensions','Avee opposite -> Ahat; Ahat opposite -> Avee'),
('display','upper left bifunctor','Ahat opposite times Avee opposite -> Ens'),
('insertion','upper left beside bifunctor','i.e. faisceaux sur Avee repr. Ahat'),
('text','upper left parenthesis','et Ahat -> Ahat et Avee -> Avee sont les identités'),
('display','left dual formula 1','Ahat = Hom^!(Ahat opposite,Ens) = Hom_!(Avee,Ens)'),
('display','left dual formula 2','Avee = Hom^!(Avee opposite,Ens) = Hom_!(Ahat,Ens)'),
('text','left ending','et item pour B'),
('drawing','upper left boundary','curved partition line'),
('margin note','upper right 1','Hom_!: sous-cat. pleine ... commutant aux colimites'),
('margin note','upper right 2','Hom^!: sous-cat. pleine ... commutant aux limites'),
('diagram','upper central main','(A x B)hat; unary Hom equivalences; bifaisceaux'),
('diagram','left middle','A x B -> A,B -> e; pB,pA,qA,qB'),
('display','middle definitions bracket','relative internal Hom_A, Hom_B; global sections equality'),
('margin note','middle right','X,Y in Ob (A x B)hat'),
('display','middle second bracket','sX(L),dX(M),X(L,M) adjunction formulas'),
('margin note','middle right second','L in Ob Ahat; M in Ob Bhat'),
('display','middle below bracket','L external M = pB*L x pA*M'),
('insertion','middle lower','Ces formules sont particulièrement intéressantes pour L=a, M=b'),
('text','lower prose','Soit X, définissant B opposite -> Ahat'),
('deletion','lower prose right','b -> Hom'),
('insertion','lower prose left below','b -> Hom_Ahat(L0,dX(b)), i.e.'),
('display','lower external product functor','(L,M) -> L external M'),
('text','lower claim','est pleinement fidèle'),
('diagram','lower identification','(A x B)hat -> Hom!! subset (Ahat x Bhat)hat'),
('text','lower Yoneda claim','le composé est le foncteur canonique dit de Yoneda'),
('display','lower formula 1','Hom of external products, evaluation, product of Hom'),
('display','lower formula 2','internal Hom external-product factorization'),
('margin note','lower right','p.ex.'),
('display','lower formula 3','internal Hom with e_Bhat, underbrace identifications'),
('margin note','lower right specialization','en particulier faisant L prime=e_Ahat'),
('display','bottom formula 4','internal Hom(pA*M,pB*L) <-iso pB*L'),
('text','bottom parenthesis','la flèche étant la flèche canonique'),
('display','bottom parenthesis arrow','Hom(alpha,beta) <- beta'),
('text','bottom ending','Posant X^M def=internal Hom(pA*M,X), on trouve donc'),
('text','bottom isolated mark','p')],doubts=[
('upper left annotation','i.e. ds; item','Abbreviation compressed; item may be idem.','medium'),
('upper left identity arrows','rightward arrow or dash','Arrowheads not distinct.','medium'),
('projection qA','line without arrowhead','No distinct head at e.','medium'),
('middle prose','composons; L0','Overwritten word and subscript.','medium'),
('lower superscripts','xi, alternative sharp','Repeated multiply stroked exponent, distinct from primes; not safely identified.','low'),
('first lower formula arguments','L prime xi, M prime xi','Primes on first occurrence may be absent/merged with exponent.','low'),
('lower specialization underbrace','Hom_Ahat(L,L prime)','Order appears reversed relative to the expression above; retained.','medium'),
('bottom isolated mark','p','Could be a short continuation mark.','low')],notes='Author circled page 1. Defines Hom_! by colimit preservation and Hom^! by limit preservation; gives the correspondence/bifaisceau equivalence diagram, relative internal Homs, left/right operations sX/dX and external product adjunction. Claims external product fully faithful and stronger internal-Hom factorization/independence formulas without a proof beyond the Yoneda identification. Repeated unclear superscript in latter formulas must not be context-normalized; record reading question after freeze. End asserts (pB*L)^M ≃ pB*L, which needs qualification/investigation; no qualification visible here. Several indices in prose differ from surrounding formulas; preserved, not repaired.')
