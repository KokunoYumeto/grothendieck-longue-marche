from save_page import save
text=r'''
\scanpage{40}
% archive foliation: 39
\deleted{Bien sûr, par définition,}

\uline{Il \unsure{faudr.} expliciter} que pour une catégorie $I$ d'indices, telle que les Inf des parties non vides existent, les foncteurs $X\longrightarrow I$ sont en corr. $1$-$1$ avec les filtrations \deleted{\unsure{croiss.}} applications croissantes
\[
\begin{aligned}I&\longrightarrow\operatorname{SsCatOuv}(X)\\i&\longmapsto X_i\end{aligned}
\]
qui commutent aux dits Inf, et telles que l'on ait $X=\bigcup X_i$.
\margin{cette dernière condition équivaut aussi à $\varinjlim X_i\simeq X$.}

Ceci posé, on a
\[
X_{/i}=X_i
\]
\deleted{d'où \unsure{l'explicitation}, pour $f$}
\[
f_i:X_i\mathbin{-}Y_i
\]
s'identifie à
\[
f_{/i}:X_{/i}\mathbin{-}Y_{/i}
\]
donc on gagne par L3.

\uline{Corollaire \unsure{1|!}} Idem dans un $\widehat A$, en utilisant le fait que $i_A$ commute aux \uline{$\varinjlim$} quelconques et \deleted{aux} produits fibrés.

\margin{\uline{Cor?} Si les $X_i$ sont \inserted{$\underline W$-}asphériques et $I$ connexe, alors $X$ est $\underline W$-asphérique (On prend $Y_i=\unsure{e_{(I_i)}|e_i}$).}

\uuline{Thm} L'ens. $\underline W$ est saturé

\uline{Cor} Pour $\forall A$, $\underline W_A$ est saturé.

\deleted{
\uline{Dém} Soit $f:X\mathbin{-}Y$ tel que $\unsure{\sigma|\gamma}(f)$ iso, d'où
\diagram{\begin{tikzcd}[column sep=small,row sep=small]
X\arrow[dr,"f"]&&X\arrow[d,"\alpha\in\underline W"']\arrow[drr,"f"]\\
&Y\arrow[r,"g"]\arrow[l,phantom,"\unsure{\exists}"]&X'\arrow[drr,"f'"']&&Y\arrow[d,"\beta\in\underline W"]\\
&&&&Y'
\end{tikzcd}}
\deleted{avec $\sigma(gf)=\sigma(\alpha)$, et}
avec $\sigma(gf)=\sigma(\alpha)$, $\sigma(f'g)=\sigma(\beta)$, $\beta f\simeq f'\alpha$.

Quitte à changer $\alpha$ en composé avec $X'\mathbin{-}X'_1$, et item pour $Y'$ avec $Y'\mathbin{-}Y'_1$, OPS $gf\sim\alpha$, $f'g\sim\beta$, \inserted{donc $gf\in\underline W$, $f'g\in\underline W$} \deleted{et pr (quitte à changer encore $\alpha$ et $\beta$ par $gf$ et $f'g$) \unsure{qui sont égales}}
\diagram{\begin{tikzcd}
X\arrow[r,"f"]\arrow[d,"\alpha"']&Y\arrow[d,"\beta"]\arrow[dl,"g"']\\
X'\arrow[r,"f'"']&Y'
\end{tikzcd}}
\[
\underbrace{\begin{gathered}\alpha,\beta\in W\\gf=\alpha,\quad f'g=\beta\\(\text{quitte à \unsure{factoriser}})\end{gathered}}
\]
\margin{\diagram{\begin{tikzcd}[column sep=small]
X\arrow[r,"f"']&Y\arrow[r,"g"']&Y'\arrow[r,"f'"']&X'
\end{tikzcd}} $gf\in\underline W$, $f'g\in\underline W$}

On pourrait d'ailleurs supposer que $f$ soit imm. ouverte, puis (quitte à factoriser \deleted{$g$, puis $f'$}) que $f,g,f'$ \unsure{sont|soient} des imm. ouvertes.
\diagram{\begin{tikzcd}[row sep=large,column sep=large]
X\arrow[rr,hook]&&Y\arrow[dl,"g_1"']\\
&X'_1\arrow[dl,shift right]\arrow[dr,hook]\\
X'\arrow[ur,shift right]\arrow[rr]&&Y'
\end{tikzcd}}
}
'''
elements=[('deletion','left top','Bien sûr, par définition'),('text','left upper','Il faudr. expliciter'),('display','left upper','I; Inf; X → I; corr. 1-1'),('text','left upper middle','avec les filtrations'),('deletion','left middle','croiss.'),('text','left middle','applications croissantes'),('display','left middle','I → SsCatOuv(X); i maps to X_i'),('text','left middle','qui commutent aux dits Inf'),('display','left middle','X=union X_i'),('margin note','left page right edge','cette dernière condition équivaut aussi à lim X_i ≃ X'),('text','left middle lower','Ceci posé, on a'),('display','left middle lower','X_/i=X_i'),('deletion','left lower','d’où l’explicitation, pour f'),('display','left lower','f_i:X_i - Y_i'),('text','left lower','s’identifie à'),('display','left lower','f_/i:X_/i - Y_/i'),('text','left lower','donc on gagne par L3'),('text','left bottom','Corollaire 1 Idem dans un Ahat'),('display','left bottom','i_A; lim directes'),('deletion','left bottom','aux'),('margin note','left foot','Cor? Si les X_i sont asphériques'),('insertion','left foot above asphériques','W-'),('display','left foot','Y_i=e_(I_i)'),('text','right top','Thm L’ens. W est saturé'),('text','right upper','Cor Pour forall A W_A est saturé'),('deletion','right proof from Dém to bottom','full proof crossed by long diagonal strokes'),('text','within cancelled right proof upper','Dém Soit f:X - Y tel que sigma(f) iso'),('diagram','within cancelled right proof upper','X f→Y g→X′; X f→Y; alpha; beta; X′ f′→Y′'),('deletion','within cancelled right proof upper middle','avec sigma(gf)=sigma(alpha), et'),('display','within cancelled right proof middle','sigma(gf)=sigma(alpha); sigma(f′g)=sigma(beta); beta f ≃ f′alpha'),('text','within cancelled right proof middle','Quitte à changer alpha en composé avec'),('display','within cancelled right proof middle','X′ - X′_1; Y′ - Y′_1'),('text','within cancelled right proof middle','OPS'),('display','within cancelled right proof middle','gf~alpha; f′g~beta'),('insertion','above cancelled et pr','donc gf in W f′g in W'),('deletion','within cancelled right proof middle','et pr (quitte à changer encore alpha et beta...)'),('diagram','within cancelled right proof lower','X f→Y; alpha; beta; g; X′ f′→Y′'),('display','within cancelled right proof lower right','alpha,beta in W; gf=alpha; f′g=beta'),('text','within cancelled right proof lower right','quitte à factoriser'),('margin note','right proof left middle','X f→Y g→Y′ f′→X′; gf and f′g in W'),('diagram','within marginal cancelled proof','X → Y → Y′ → X′'),('text','within cancelled right proof bottom','On pourrait d’ailleurs supposer'),('deletion','within cancelled right proof bottom','g, puis f′'),('diagram','within cancelled right proof bottom left','X hook→Y; g_1; X′_1; X′; Y′')]
save(40,text,'text',elements,'Landscape sheet: left continuation of passage-to-limit argument, right saturation theorem with proof crossed by two long diagonal strokes; theorem and corollary headings are not crossed. Nested deletions retained. Source has plain dash in several maps; no arrowhead supplied. Right small chain actually reads X,Y,Y-prime,X-prime in that order, despite the separate square. Bottom right diagram is heavily retraced; lower upward arrow may be cancelled. Notation sigma/gamma, last left terminal-object subscript, and several deleted phrases need audit. No proof checked.')
