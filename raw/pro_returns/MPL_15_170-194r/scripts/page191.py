from record_page import record

record(191, r'''\scanpage{191}
$X$ préschém. connexe \deleted{\unsure{finitude} \unsure{a priori} \unsure{quelconque}}

$1^\circ)$ $X_{\mathrm{réd}}$ de car $p>0$. Alors dans le pro-torseur fondamental
$(T_\alpha)$, il n'y a pas en général de sections pour les $T_\alpha$.

\margin{$\unsure{\ast}$}
On dispose uniquement, \deleted{de façon canonique}

\margin{Coh. $l$-adique}
(i) des $\unsure{\xi}_l^{(\alpha)}\in T_\alpha(\unsure{\mathbb Z|\mathbb Q}_l)$,
$l\neq p$, provenant sans doute
de $\unsure{\xi}_l\in T_\alpha(\widetilde{\mathbb Z}_{l\mathbb Z})$.
\margin{hensélisé}

\margin{\fbox{\begin{minipage}{.29\linewidth}
Coh. $p$-adique\\
Structure supplémentaire :\\
opérations \fbox{$\uuline{F}\text{ et }\uuline{V}$}\\
$1/2$ \uuline{linéaires} \uuline{\unsure{relatifs}}\\
\unsure{Frobenius sur $k$}
\end{minipage}}}

\diagram{\[
\begin{tikzcd}[column sep=small,row sep=large]
\text{(ii) d'un }\unsure{\xi}_p^{(\alpha)}\in T_\alpha( &
\mathbb W_p(k) \arrow[dr,"\text{``DeRham-Hodge''}"'] &
\begin{gathered}
)\quad\text{si }\deleted{\text{$X$ déf. sur}}\inserted{\text{$k$ est un corps parfait sur $X$}}\\
\deleted{\text{le corps parfait $k$}}\\
[\ \unsure{\xi}_p\ \text{provenant sans doute}\\
\text{d'un }\unsure{\xi}_p\in T_{\unsure{p|\alpha}}(\widetilde{\mathbb Z}_{p\mathbb Z})\ ]
\end{gathered}
\\
\text{(iii)}[\ ?\quad\text{\uline{réduit}}\ \unsure{\xi}_p^{(\alpha)\unsure{0|\circ}}\in T_\alpha( &
\deleted{\unsure{\mathbb W}} & k)\ ]
\end{tikzcd}
\]}
\margin{hensélisé strict.}

\margin{Coh. Hodge-deRham. Mais ici, il faut \deleted{sans doute}
travailler dans la catégorie dérivée. Tenir compte aussi de la
structure \uline{filtrée} de Hodge-DeRham}

$\overline{\mathrm M}$ si $X=\operatorname{Spec}\mathbb F_q$, il y a en général
des \deleted{$\unsure{\xi}$} \unsure{obstructions} \unsure{non triviales} dans
des $H^{\unsure{2|1}}(\mathbb Q,G)$ $-\, -\, -$

\margin{$\unsure{\ast}$}
On utilise des ``foncteurs fibres'' qui induisent sur
les motifs effectifs de poids $0$ le foncteur
canonique. Alors les objets de $T_\alpha(\mathbb Z_l)$ sont
sans doute uniques\inserted{à isom près}, (th. de Lang), de $\unsure{\overline{\mathrm m}|\simeq}$
ceux de $T_\alpha(\unsure{\mathbb W}_p(k))$ si $k$ fini (ib), \inserted{plus gén.} pour un
$k$ parfait de dim \unsure{ch} $1$ (?). En général, il
faut s'attendre que $T_\alpha(k)$ \deleted{soit}\inserted{ait} plus d'un
\unsure{élém.} à isom près, mais il est possible
que $T_{\unsure{\infty}}(k)=\varprojlim T_\alpha(k)$ n'a qu'un \unsure{élém.} à
isom près, celui donné par la \unsure{théorie|théor.} de DeRham
Hodge.

\margin{\unsure{relation avec} \unsure{le problème} \unsure{galoisien} ??
Il doit être \uline{\unsure{équivalent|épuisant}}, cf \uline{Manin}}

\margin{190}
''', [
('text','top line','X préschém. connexe'),
('deletion','top line','finitude a priori quelconque'),
('text','upper, lines 2–3','1°) X_réd de car p>0; pro-torseur fondamental'),
('margin note','left of On dispose','asterisk-like mark'),
('text','upper, line 4','On dispose uniquement'),
('deletion','upper, line 4','de façon canonique'),
('margin note','left beside (i)','Coh. l-adique'),
('text','upper, item (i)','des xi_l^(alpha); l≠p; provenant sans doute'),
('display','upper-right, continuation of (i)','xi_l ∈ T_alpha(Z-tilde_lZ)'),
('margin note','right below (i)','hensélisé'),
('margin note','left, enclosed note beside (ii)','Coh. p-adique; Structure supplémentaire; F et V; 1/2 linéaires'),
('diagram','middle, items (ii)–(iii)','xi_p^(alpha) ∈ T_alpha(W_p(k)); DeRham-Hodge arrow to k; réduit xi_p^(alpha)0'),
('deletion','middle, condition in (ii)','X déf. sur'),
('insertion','above and below cancelled condition','k est un corps parfait sur X'),
('deletion','middle, condition in (ii)','le corps parfait k'),
('text','middle-right, bracketed addition','xi_p provenant sans doute d\'un xi_p'),
('display','middle-right','xi_p ∈ T_p(Z-tilde_pZ)'),
('margin note','right below bracketed addition','hensélisé strict.'),
('margin note','middle beside (iii)','?'),
('deletion','middle, inside T_alpha before k','W-like cancelled letter'),
('margin note','left, below enclosed note','Coh. Hodge-deRham; catégorie dérivée; structure filtrée'),
('deletion','left margin, after il faut','sans doute'),
('text','middle-lower','M-bar si X=Spec F_q; obstructions non triviales'),
('deletion','middle-lower, before obstructions','xi-like cancelled letter'),
('display','middle-lower','H^2(Q,G) - - -'),
('margin note','left of On utilise','asterisk-like mark'),
('text','lower, first paragraph','On utilise des "foncteurs fibres"; motifs effectifs de poids 0'),
('insertion','lower, above uniques','à isom près'),
('insertion','lower, above pour un','plus gén.'),
('text','lower, continuation','k parfait de dim ch 1 (?); En général; T_alpha(k)'),
('deletion','lower, after T_alpha(k)','soit'),
('insertion','lower, above soit','ait'),
('text','bottom paragraph continuation','T_infty(k)=lim T_alpha(k); DeRham Hodge'),
('margin note','lower left, slanting','relation avec le problème galoisien ??; équivalent; cf Manin'),
('margin note','bottom left','190')
], observations='Whole page, both halves, enlarged main text and rotated margin crops inspected. This is a heavily revised note; the cancelled top hypothesis and the lowest left marginal question remain low-confidence. The arrow explicitly labelled "DeRham-Hodge" runs from W_p(k) toward the k in item (iii); its question mark and deleted coefficient are retained. The condition on k is inserted over and below an earlier condition on X, not attached to the l-adic item. The left margin contains a separate enclosed F-and-V note and a derived-category/filtration note. A barred M occurs before si X=Spec F_q; a smaller barred m-like sign occurs after de later in the page, and must be compared to scan 187 in the final notation audit. The notation T_p in the bracketed right addition is not silently changed to T_alpha. The manuscript itself has (?) after the cohomological-dimension qualification, a question mark beside reduction, and two question marks in the lowest margin.')
