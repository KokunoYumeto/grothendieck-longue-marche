from save_page import save_page

save_page(104, r'''
\scanpage{104}
% archive foliation: 103
\deleted{
(par le choix d'isomorphismes $\unsure{\widehat{\mathbf Z}_\ell|\mathbf Z_\ell}(1)\simeq\mathbf Z_\ell$ pour $\forall\ell$)

\unsure{on trouve} qu'on a défini une représentation du produit semi-direct de $\mathbf Z$ avec $\mathbf Z$, opérant sur le sous-groupe $\mathbf Z$ par multiplication par $q$. Donc ce groupe est engendré par deux éléments $f$ (correspondant à $\operatorname{frob}_q$) et $g$, satisfaisant la relation
\[
(6.4)\qquad fgf^{-1}=g^q
\]
\unsure{Or on a le}

\uline{Lemme} 6.5. Soient $F,G$ deux automorphismes d'un vectoriel \inserted{$E$} de dim finie sur un corps, et $q$ \deleted{supposant que} un entier $>1$ tel qu'on ait \deleted{\unsure{$FG$}}
\[
FGF^{-1}=G^q
\]
Alors $G$ est quasi-unipotent, i.e. ses valeurs propres sont toutes des racines de $1$, ou encore: il existe un entier $N\geq1$ tel que $G^N$ soit unipotent.

\uline{Dém.} L'\unsure{ens} des valeurs propres de $G$ \deleted{et $FGF^{-1}$} \deleted{dans} (\unsure{c-à-d vues} dans une clôture alg. $\overline R$ de $R$) étant le \deleted{\unsure{même, et}} $=$ que celui de $FGF^{-1}$, donc le $=$ que celui de $G^q$, il s'ensuit que c'est une partie \inserted{\deleted{\unsure{finie}} $\Phi$} de $\overline R^*$ stable par l'application
\[
\lambda\longrightarrow\lambda^q
\]
Comme $\Phi$ est fini, il existe donc pour tt $\lambda\in\Phi$ deux entiers $N'\unsure{>\!|\geq}N''$ \deleted{tels} $\geq0$ tels que
}
''', [
('deletion','whole page','three long cancellation strokes across the draft'),
('text','top','(par le choix d’isomorphismes'),
('text','upper paragraph','on trouve qu’on a défini'),
('display','upper middle','(6.4) fgf⁻¹=g^q'),
('text','middle transition','Or on a le'),
('text','middle lemma','Lemme 6.5. Soient F,G'),
('insertion','above vectoriel / de','E'),
('deletion','lemma before un entier','supposant que'),
('deletion','lemma right after ait','FG'),
('display','middle','FGF⁻¹=G^q'),
('text','middle lower','Alors G est quasi-unipotent'),
('text','lower proof','Dém. L’ens des valeurs propres'),
('deletion','proof first line right','et FGF⁻¹'),
('deletion','proof second line left','dans'),
('deletion','proof third line','même, et'),
('insertion','proof above partie / de','Φ'),
('deletion','within insertion above partie','finie'),
('display','lower','λ→λ^q'),
('text','bottom','Comme Φ est fini'),
('deletion','bottom after N′ N″','tels'),
], [
('top parenthesis','hat on Z_l','possibly plain Z_l; small mark above Z is indistinct','medium'),
('lemma opening','d’un vectoriel E','no separate espace is visible; E is inserted','high'),
('proof opening','L’ens; c-à-d vues','very compressed abbreviations; not expanded','low'),
('proof cancellation after étant le','même, et','crossed letters uncertain; following equals sign preserved literally','low'),
('proof insertion','deleted finie, then Φ','first inserted word crossed through','medium'),
('bottom inequality','N′ > N″','relation is heavily retraced; ≥ possible','medium'),
], [
'Cancelled draft: relation (6.4) fgf⁻¹=g^q; lemma 6.5 asserts quasi-unipotence for finite-dimensional F,G over a field with FGF⁻¹=G^q and q>1, followed by a finite-spectrum proof that continues on the next sheet. Treat the entire claim as withdrawn here, not an endorsed final statement.',
], sheet_kind='cancelled_draft')
