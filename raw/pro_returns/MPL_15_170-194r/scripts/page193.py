from record_page import record

record(193, r'''\scanpage{193}
Les $\unsure{\xi}_l$ de (i) dépendent du choix d'un pt géom de $X$,
mais à isom non unique près (dépendant du
\uuline{$\pi_1(X)$}) \inserted{[$\pi_1(X)$ opère sur $\unsure{\xi}_l$]}
\deleted{sont} \unsure{indépendants} de ce choix.

Les $\unsure{\xi}_p^\alpha$ dépendent du choix d'un \deleted{corps} pt\inserted{de $X$}
à valeurs dans un corps parfait sans plus,
si on veut les $k(x)^{\mathrm{pf}}$ (clôture parfaite de $k(x)$),
et pour $k$ donné, il ne \uline{semble pas} qu'il y ait
\deleted{ait} des isom entre les $\unsure{\xi}_{p,a}^{(\alpha)}$ correspondants
aux divers pts à valeurs dans $k$ (c'est la
``partie continue'' du $\unsure{H^1|H^2}$ préc. qui v. faire des
ennuis), s'ils sont localisés en le $\overline{\mathrm m}$ $x\in X$, \deleted{il}\inserted{et}
\deleted{sont} si $k$ est alg. clos, ils sont conjugués par
autom. de $k$\inserted{(étendus à $\mathbb W_p(k)$)}, les groupes alg. associés sont
donc conjugués par autom. de $k$ $-\, -\, -\, -$ il est $\overline{\mathrm m}$
gentil qu'ils \unsure{veuillent} être l'un \unsure{tordu} de
l'autre $-\, -\, -\, -$ Le gpe $\pi_1(X)$ n'opère pas sur $\unsure{\xi}_p^\alpha$
\figure{\begin{tikzpicture}[baseline=-.4ex,scale=.22]\draw (0,0)--(1,2);\draw (1,2) circle (.18);\end{tikzpicture}}, par
contre le groupe des autom de $k$ sur $k(x)$
\deleted{[\unsure{au $\overline{\mathrm m}$ de $k$} \unsure{$H$ précédent}]}
opère de façon $1/2$ \uline{linéaire} sur $\unsure{\xi}_p^{(\alpha)}$ $-\, -\, -\, -$
\margin{[\unsure{En une descente}
\figure{\begin{tikzpicture}[baseline=-.4ex,scale=.22]\draw (0,0)--(1,2);\draw (0,0) circle (.18);\end{tikzpicture}}}

\margin{\figure{\begin{tikzpicture}[baseline=-.4ex,scale=.22]\draw (0,0)--(1,2);\draw (1,2) circle (.18);\end{tikzpicture}}
En revanche, on a comme structure supplémentaire
les opérations $F,V$ avec $FV=p$}

\margin{\figure{\begin{tikzpicture}[baseline=-.4ex,scale=.22]\draw (0,0)--(1,2);\draw (0,0) circle (.18);\end{tikzpicture}}
\unsure{élégante.} D'autre part, un autom $\sigma$
de $k$ qui n'est pas $k(x)$-linéaire
transforme en général $\unsure{\xi}_{xp}^{\unsure{\alpha}}$ en un
$\unsure{\xi}_{xp}^{\sigma}$ qui n'est plus isom
à $\unsure{\xi}_{x,p}$ $-\, -\, -\, -$}

Notations

\diagram{\[
\text{(i)}\left\{\begin{array}{ll}
\unsure{\xi}_{\bar x,l} & \text{foncteurs fibres $l$-adiques en}\\
& \leftarrow\ \text{pt géom }\bar x\\[6pt]
\unsure{\xi}_{x,l} & \text{par desc. de la \unsure{$2$-gpe|$l$-gpe} pour $x\in X$}\\
& \text{ou un pt de $X$ à val.}\\
& \text{dans un corps quelc.}\\
& \text{($\unsure{\xi}_{x,l}$ déf. à isom \uline{non uniq.} près)}
\end{array}\right.
\]}

\margin{\uline{On peut mettre}\\
\uline{des \unsure{exposants} $\alpha$}\\
\uline{à \unsure{volonté}}}

\diagram{\[
\text{(ii)}\left\{\begin{array}{ll}
\unsure{\xi}_{x,p} & \text{$x$ \unsure{est pt} de $X$ à val. dans un corps}\\[6pt]
\unsure{\xi}_{x,p}^{0} &
\end{array}\right.
\]}

\margin{192}
''', [
('text','upper, first paragraph','Les xi_l de (i); choix d\'un pt géom de X'),
('insertion','between lines 2–3','[pi_1(X) opère sur xi_l]'),
('deletion','upper, line 3','sont'),
('text','upper-middle, second paragraph opening','Les xi_p^alpha; corps parfait; clôture parfaite'),
('deletion','line 4, before pt','corps'),
('insertion','above end of line 4','de X'),
('text','middle, lines 7–10','il ne semble pas; isom entre xi_(p,a)^(alpha); partie continue'),
('deletion','middle, repeated word before des isom','ait'),
('text','middle, continuation','s\'ils sont localisés; k alg. clos; conjugués'),
('deletion','middle, end of localisés line','il'),
('insertion','middle, over deleted il','et'),
('deletion','middle, beginning of following line','sont'),
('insertion','middle, after autom. de k','(étendus à W_p(k))'),
('text','middle-lower','les groupes alg. associés; gentil; l\'un tordu de l\'autre'),
('text','lower main paragraph','Le gpe pi_1(X) n\'opère pas; autom de k sur k(x)'),
('drawing','lower main paragraph, after xi_p^alpha','diagonal reference stroke with top circle'),
('deletion','lower right, bracketed phrase','au m-bar de k H précédent'),
('text','lower main paragraph ending','opère de façon 1/2 linéaire sur xi_p^(alpha)'),
('margin note','lower right, beneath cancelled bracket','[En une descente'),
('drawing','lower right, beside short marginal phrase','diagonal reference stroke with bottom circle'),
('margin note','left upper, vertical','En revanche; opérations F,V; FV=p'),
('drawing','left upper, beginning of vertical note','reference stroke with top circle'),
('margin note','left middle, vertical','élégante; D\'autre part; autom sigma; k(x)-linéaire'),
('drawing','left middle, beginning of vertical note','reference stroke with bottom circle'),
('text','lower, above braces','Notations'),
('diagram','lower, brace (i)','xi_(x-bar,l); xi_(x,l); foncteurs fibres l-adiques; pt géom'),
('margin note','bottom left above pencil number','On peut mettre des exposants alpha à volonté'),
('diagram','bottom, brace (ii)','xi_(x,p); xi_(x,p)^0; x est pt de X à val. dans un corps'),
('margin note','bottom left','192')
], sheet_kind='reused_typed', observations='Whole, both halves, enlarged text and all rotated left marginal notes inspected. Faint mirrored blue type is reverse-side show-through. The two long diagonal reference strokes have circles at opposite ends; they are reproduced as small TikZ drawings, with their matching marks in the margins, rather than silently identified as Greek letters. The lower-right cancelled bracket and the short phrase below it are very weak readings. The brace tables at the bottom are transcribed as arrays, including the literal leftward arrow by pt géom and the incomplete final description. The barred m occurs twice and agrees visually with the contraction discussed at scan 191. There is no attempt to supply what follows corps at the end of the page. The possible reading of the abbreviation in par desc. de la 2-gpe remains open.')
