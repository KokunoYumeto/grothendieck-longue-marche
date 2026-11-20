# Scan011 — initial text comparison before final reports

R2 was read in full. The following unified diffs convey each full R1/R3 variant against it. All three final reports must be read before main image adjudication.

## R2 versus R1

```diff
--- R2
+++ R1
@@ -1,5 +1,5 @@
 \scanpage{11}
-$T$ torseur \unsure{:|à} droite sous \unsure{grp|grpe} $\mathbb{Z}$
+$T$ torseur \unsure{:|à} droite sous \unsure{grpe|grp} $\unsure{\mathbb{Z}|Z}$
 
 \[
 \deleted{\unsure{\operatorname{Aut}_{\substack{G\text{-ens}\\G\text{-}\unsure{\mathrm{var}|\mathrm{op}}}}(\unsure{D|T})
@@ -8,16 +8,18 @@
 
 \diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=small]
 1\arrow[r] \& \mathbb{Z}\arrow[r,"i"] \& \operatorname{Aut}(\mathbb{Z},T)\arrow[r,"p"]
- \& \operatorname{Aut}(\mathbb{Z})\arrow[r,dash]\arrow[l,dashed,bend left=28,"q_t"] \& 1
+ \& \operatorname{Aut}(\mathbb{Z})\arrow[r,dash]\arrow[l,dashed,bend left=28,"q_t"'] \& 1
 \end{tikzcd}}
 
-% A detached short dark mark stands above un; ink versus surface trace is unresolved.
-$\forall t\in T$, on a \tikz[baseline=(wordun.base)]{
-\node[anchor=base west,inner sep=0pt] (wordun) at (0,0) {un};
-\node[inner sep=0pt] at (.30,.42) {\unsure{\tikz[baseline=-.2ex]{\draw[line width=.6pt,line cap=round] (0,0)--(.05,0);}}};}
+% A detached dark trace stands above un; its attribution to writing is uncertain.
+$\forall t\in T$, on a
+\tikz[baseline=(unword.base)]{
+\node[inner sep=0pt] (unword) {un};
+\node[inner sep=0pt] at ([xshift=.35em,yshift=1.45em]unword.base)
+ {\unsure{\rule{.12em}{.055em}}};}
 splitting $q_t$, défini par
 \[
-\left\{\begin{aligned}&q_t(\gamma)(t)=t\\&p(q_t(\gamma))=\gamma\end{aligned}\right.
+\left\{\begin{aligned}q_t(\gamma)(t)&=t\\p(q_t(\gamma))&=\gamma\end{aligned}\right.
 \]
 
 Quelle est la relation entre $q_t$ et $q_{t'}$ ?
@@ -29,66 +31,91 @@
 \]
 
 [ Pour le vérifier, il suffit de voir que
-% The brace starts after int, ends below q_t, and has a displaced slanting equals below it.
 \[
-\begin{tikzpicture}[baseline=(proofint.base)]
-\node[anchor=base west,inner sep=0pt] (proofint) at (0,0) {$\operatorname{int}$};
-\node[anchor=base west,inner sep=0pt] (proofarg) at (proofint.base east) {$(i(g))\circ(q_t$};
-\node[anchor=base west,inner sep=0pt] (prooftail) at (proofarg.base east) {$(\gamma))$};
-\node[anchor=base west,inner sep=0pt] at (prooftail.base east) {$:\quad t'\longmapsto t'$};
-\draw ([yshift=-.10cm]proofarg.south west)
- .. controls +(.65cm,-.01cm) and +(-.15cm,.12cm) .. ([yshift=-.28cm]proofarg.south)
- .. controls +(.15cm,.16cm) and +(-.35cm,-.04cm) .. ([yshift=-.06cm]proofarg.south east);
-\node[inner sep=0pt,rotate=-60] at ([xshift=.18cm,yshift=-.40cm]proofarg.south) {$=$};
-\node[anchor=north west,inner sep=0pt] at ([yshift=-.57cm]proofarg.south west)
+\begin{tikzpicture}[x=.012cm,y=-.012cm,baseline=0]
+\node[anchor=base west,inner sep=0pt] at (0,0)
+ {$\operatorname{int}(i(g))\unsure{\circ}(q_t(\gamma))$};
+\node[anchor=base west,inner sep=0pt] at (382,-4)
+ {$:\quad t'\longmapsto t'$};
+% The brace covers only the middle of the expression, as drawn.
+\draw[line width=.55pt] (76,24)
+ .. controls (104,29) and (145,28) .. (170,36)
+ .. controls (190,18) and (237,25) .. (294,14);
+% Two separate slanted strokes form the equality below and right of the cusp.
+\draw[line width=.55pt] (195,33)--(200,41);
+\draw[line width=.55pt] (203,31)--(208,39);
+\node[anchor=base west,inner sep=0pt] at (73,76)
  {$i(g)\,q_t(\gamma)\,i(g)^{-1}$};
 \end{tikzpicture}
 \]
 or \quad $t'=tg$
 \[
 \begin{aligned}
-&\deleted{q_t(\gamma)(t')=q_t(\gamma)(t)\,\gamma(g)=t.\gamma(g)}\\
-&\hspace{.3em}\deleted{\operatorname{int}(i(g))\,q_t(\gamma)\,(t')=}\\
-&\quad i(g)^{-1}(t')=t\qquad q_t(\gamma)\,i(g)^{-1}(t')=q_{\unsure{b|t}}(\gamma)\,t=t\\
-&\qquad i(g)\,q_t(\gamma)\,i(g)^{-1}(t')=tg=t'\qquad\text{ok}\qquad ]
+&\deleted{q_t(\unsure{\gamma})(t')=q_t(\gamma)(t)\,\gamma(g)=t.\gamma(g)}\\
+&\deleted{\operatorname{int}(i(g))\,q_t(\gamma)\,(t')=}\\
+&i(g)^{-1}(t')=t\qquad q_t(\gamma)\,i(g)^{-1}(t')=q_{\unsure{b|t}}(\gamma)\,t=t\\
+&i(g)\,q_t(\gamma)\,i(g)^{-1}(t')=tg=t'\qquad\text{ok}\qquad ]
 \end{aligned}
 \]
 
 \reversemarginpar
-\margin{\begin{tikzpicture}[x=.65cm,y=.65cm,baseline=(itou.base)]
-\node[anchor=west,inner sep=0pt] (itou) at (0,0) {Itou pour $\operatorname{Aut}^{\Gamma}(\mathbb{Z},T)$};
-\draw (1.85,1.13) .. controls (3.15,1.55) and (3.55,.12) .. (5.20,-.18)
- .. controls (4.05,-.50) and (2.88,-.73) .. (2.15,-.68);
+\margin{\begin{tikzpicture}[x=.01cm,y=-.01cm,baseline=0]
+\node[anchor=base west,inner sep=0pt] at (0,0)
+ {Itou pour $\operatorname{Aut}^{\Gamma}(\mathbb{Z},T)$};
+\draw[line width=.55pt] (172,-112)
+ .. controls (310,-163) and (327,-11) .. (484,17);
+\draw[line width=.55pt] (204,58)
+ .. controls (286,64) and (421,34) .. (484,17);
 \end{tikzpicture}}
 \normalmarginpar
 
-% Ex and Z=Z_n are on the baseline of the lower (Aut) row; the canceled fragment lies beneath Z=Z_n.
 \[
-\begin{aligned}
-&\text{\uline{Ex}}\quad \mathbb{Z}=\mathbb{Z}_n\quad
-\left\{\begin{aligned}[b]
-\operatorname{End}\mathbb{Z}&=\mathbb{Z}_n\\
-\operatorname{Aut}\mathbb{Z}&=\mathbb{Z}_n^{*}\supset\{\pm1\}=\Gamma
-\end{aligned}\right.\\
-&\hspace{3.8em}\deleted{\Gamma\in}
-\end{aligned}
+\begin{tikzpicture}[x=1cm,y=1cm,baseline=0]
+\node[anchor=base west,inner sep=0pt] at (0,0) {\uline{Ex}};
+\node[anchor=base west,inner sep=0pt] at (1.3,0) {$\mathbb{Z}=\mathbb{Z}_n$};
+\node[anchor=base west,inner sep=0pt] at (3.9,.66) {$\operatorname{End}\mathbb{Z}=\mathbb{Z}_n$};
+\node[anchor=base west,inner sep=0pt] at (3.9,0)
+ {$\operatorname{Aut}\mathbb{Z}=\mathbb{Z}_n^{*}\supset\{\pm1\}=\Gamma$};
+\draw[line width=.55pt] (3.68,.85)
+ .. controls (3.48,.75) and (3.73,.54) .. (3.56,.45)
+ .. controls (3.74,.36) and (3.54,.03) .. (3.73,-.04);
+\node[anchor=base west,inner sep=0pt] at (1.43,-.70)
+ {$\deleted{\unsure{\Gamma\subset|\Gamma\in}}$};
+\end{tikzpicture}
 \]
-\margin{(\uline{NB} \unsure{si} $n=2$, $+1=-1$ dans $\mathbb{Z}_n^{*}$\ldots)}
+\margin{\begin{tabular}{@{}l@{}}
+(\uline{NB} \unsure{si} $n=2$, $+1=-1$\\
+\quad dans $\mathbb{Z}_n^{*}$\ldots)
+\end{tabular}}
 
 \[
-\begin{aligned}
-&\operatorname{Aff}(\mathbb{Z}_n)=\mathbb{Z}_n\mathbin{.}\mathbb{Z}_n^{*}
- \quad\text{(produit ${}^1\! /\! {}_2$ direct)}
- \quad\raisebox{.7em}{\unsure{\tikz[baseline=0pt]{\fill (0,0) circle (.4pt);\fill (.05,.075) circle (.4pt);}}}\\[-.3em]
-&\text{\llap{\unsure{\tikz[baseline=-.1ex]{\draw[line width=.7pt,line cap=round] (0,.04)--(0,0)--(.025,0);}}\hspace{1.6em}}}
- \hspace{1.7em}\rotatebox{90}{$\subset$}\\[-.3em]
-&\hspace{.5em}\operatorname{Aff}^{\{\pm1\}}(\mathbb{Z}_n)=\mathbb{Z}_n\mathbin{.}\{\pm1\}
-\end{aligned}
+\begin{tikzpicture}[x=.01cm,y=-.01cm,baseline=0]
+\node[anchor=base west,inner sep=0pt] at (0,0)
+ {$\operatorname{Aff}(\mathbb{Z}_n)=\mathbb{Z}_n\mathbin{.}\mathbb{Z}_n^{*}$};
+\node[anchor=base west,inner sep=0pt] at (526,0)
+ {(produit $1/2$ direct)};
+% Open upward stroke between the formulas, without an assigned set-operation meaning.
+\draw[line width=.55pt] (98,47)
+ .. controls (96,70) and (113,72) .. (111,45);
+% Detached short dark stroke to the left of the interline relation.
+\draw[line width=.75pt] (-86,38)--(-85,43);
+\node[anchor=base west,inner sep=0pt] at (30,126)
+ {$\operatorname{Aff}^{\{\pm1\}}(\mathbb{Z}_n)=\mathbb{Z}_n\mathbin{.}\{\pm1\}$};
+\end{tikzpicture}
 \]
-% The two upper-right points and the lower-left hooked point have no assigned function; ink/surface status is unresolved.
-\margin{groupe diédral d'indice $n$, $\mathbb{D}_n$ (on suppose $n\ne2$\ldots)}
+\margin{\begin{tabular}{@{}l@{}}
+groupe \unsure{diédral|diédhral}\\
+d'indice $n$, $\mathbb{D}_n$\\
+(on suppose $n\ne2$\ldots)
+\end{tabular}}
 
-Soit $T$ torseur sous $Z$ groupe cyclique d'ordre $n\geq3$ muni d'une famille $\{u,u^{-1}\}$ de 2 gén. \deleted{\unsure{d'ordre $n$}.}\raisebox{.7ex}{\inserted{inverses l'un de l'}}autre.
+Soit $T$ torseur sous $Z$ groupe cyclique d'ordre $n\geq3$ muni d'une famille $\{u,u^{-1}\}$ de 2 gén.
+\tikz[baseline=(old.base)]{
+\node[anchor=base west,inner sep=0pt] (old) at (0,0)
+ {\deleted{\unsure{d'ordre $n$}.}};
+\node[anchor=south west,inner sep=0pt] at ([yshift=.14em]old.north west)
+ {\inserted{inverses l'un de l'}};}
+autre.
 \diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=small]
 1\arrow[r] \& Z\arrow[r,dash,"i"] \& \operatorname{Aut}^{\pm1}(T,Z)\arrow[r,dash,"p"]
  \& \{\pm1\}\arrow[r,dash]\arrow[l,bend left=25,"q"] \& 1
```

## R2 versus R3

```diff
--- R2
+++ R3
@@ -1,5 +1,5 @@
 \scanpage{11}
-$T$ torseur \unsure{:|à} droite sous \unsure{grp|grpe} $\mathbb{Z}$
+$T$ torseur à droite sous \unsure{grpe|grp} $\mathbb{Z}$
 
 \[
 \deleted{\unsure{\operatorname{Aut}_{\substack{G\text{-ens}\\G\text{-}\unsure{\mathrm{var}|\mathrm{op}}}}(\unsure{D|T})
@@ -11,13 +11,14 @@
  \& \operatorname{Aut}(\mathbb{Z})\arrow[r,dash]\arrow[l,dashed,bend left=28,"q_t"] \& 1
 \end{tikzcd}}
 
-% A detached short dark mark stands above un; ink versus surface trace is unresolved.
-$\forall t\in T$, on a \tikz[baseline=(wordun.base)]{
-\node[anchor=base west,inner sep=0pt] (wordun) at (0,0) {un};
-\node[inner sep=0pt] at (.30,.42) {\unsure{\tikz[baseline=-.2ex]{\draw[line width=.6pt,line cap=round] (0,0)--(.05,0);}}};}
-splitting $q_t$, défini par
+$\forall t\in T$, on a
+\tikz[baseline=(un.base)]{\node[inner sep=0pt] (un) {un};
+\node[inner sep=0pt] at ([xshift=.35em,yshift=1.1em]un.north)
+ {\unsure{\tikz{\fill (0,0) rectangle (.05,.018);}}};}
+\unsure{splitting} $q_t$, défini par
+% The tiny raised trace over un is retained without assigning punctuation or a function.
 \[
-\left\{\begin{aligned}&q_t(\gamma)(t)=t\\&p(q_t(\gamma))=\gamma\end{aligned}\right.
+\left\{\begin{aligned}q_t(\gamma)(t)&=t\\p(q_t(\gamma))&=\gamma\end{aligned}\right.
 \]
 
 Quelle est la relation entre $q_t$ et $q_{t'}$ ?
@@ -29,18 +30,19 @@
 \]
 
 [ Pour le vérifier, il suffit de voir que
-% The brace starts after int, ends below q_t, and has a displaced slanting equals below it.
+% The drawn brace starts after int and ends under q_t; the equality below it is slanted.
 \[
-\begin{tikzpicture}[baseline=(proofint.base)]
-\node[anchor=base west,inner sep=0pt] (proofint) at (0,0) {$\operatorname{int}$};
-\node[anchor=base west,inner sep=0pt] (proofarg) at (proofint.base east) {$(i(g))\circ(q_t$};
-\node[anchor=base west,inner sep=0pt] (prooftail) at (proofarg.base east) {$(\gamma))$};
-\node[anchor=base west,inner sep=0pt] at (prooftail.base east) {$:\quad t'\longmapsto t'$};
-\draw ([yshift=-.10cm]proofarg.south west)
- .. controls +(.65cm,-.01cm) and +(-.15cm,.12cm) .. ([yshift=-.28cm]proofarg.south)
- .. controls +(.15cm,.16cm) and +(-.35cm,-.04cm) .. ([yshift=-.06cm]proofarg.south east);
-\node[inner sep=0pt,rotate=-60] at ([xshift=.18cm,yshift=-.40cm]proofarg.south) {$=$};
-\node[anchor=north west,inner sep=0pt] at ([yshift=-.57cm]proofarg.south west)
+\begin{tikzpicture}[baseline=(intname.base)]
+\node[anchor=base west,inner sep=0pt] (intname) at (0,0) {$\operatorname{int}$};
+\node[anchor=base west,inner sep=0pt] (bracepart) at (intname.base east)
+ {$(i(g))\unsure{\circ}(q_t$};
+\node[anchor=base west,inner sep=0pt] at (bracepart.base east)
+ {$(\gamma))\;:\;t'\longmapsto t'$};
+\draw ([yshift=-.12em]bracepart.south west)
+ .. controls +(.4em,-.2em) and +(-.7em,.3em) .. ([xshift=-.3em,yshift=-.4em]bracepart.south)
+ .. controls +(.3em,.5em) and +(-.5em,-.1em) .. ([yshift=.2em]bracepart.south east);
+\node[inner sep=0pt] at ([xshift=.2em,yshift=-.8em]bracepart.south) {\rotatebox{-65}{$=$}};
+\node[anchor=base west,inner sep=0pt] at ([yshift=-2em]bracepart.south west)
  {$i(g)\,q_t(\gamma)\,i(g)^{-1}$};
 \end{tikzpicture}
 \]
@@ -48,47 +50,49 @@
 \[
 \begin{aligned}
 &\deleted{q_t(\gamma)(t')=q_t(\gamma)(t)\,\gamma(g)=t.\gamma(g)}\\
-&\hspace{.3em}\deleted{\operatorname{int}(i(g))\,q_t(\gamma)\,(t')=}\\
-&\quad i(g)^{-1}(t')=t\qquad q_t(\gamma)\,i(g)^{-1}(t')=q_{\unsure{b|t}}(\gamma)\,t=t\\
-&\qquad i(g)\,q_t(\gamma)\,i(g)^{-1}(t')=tg=t'\qquad\text{ok}\qquad ]
+&\deleted{\operatorname{int}(i(g))\,q_t(\gamma)\,(t')=}\\
+&i(g)^{-1}(t')=t\qquad q_t(\gamma)\,i(g)^{-1}(t')=q_{\unsure{b|t}}(\gamma)\,t=t\\
+&i(g)\,q_t(\gamma)\,i(g)^{-1}(t')=tg=t'\qquad\text{ok}\qquad ]
 \end{aligned}
 \]
 
 \reversemarginpar
 \margin{\begin{tikzpicture}[x=.65cm,y=.65cm,baseline=(itou.base)]
-\node[anchor=west,inner sep=0pt] (itou) at (0,0) {Itou pour $\operatorname{Aut}^{\Gamma}(\mathbb{Z},T)$};
-\draw (1.85,1.13) .. controls (3.15,1.55) and (3.55,.12) .. (5.20,-.18)
- .. controls (4.05,-.50) and (2.88,-.73) .. (2.15,-.68);
+\node[anchor=base west,inner sep=0pt] (itou) at (0,0) {Itou pour $\operatorname{Aut}^{\Gamma}(\mathbb{Z},T)$};
+% Open callout: its two left ends begin over and below Aut, not at the start of Itou.
+\draw (2.1,1.15) .. controls (3.65,1.7) and (3.85,.15) .. (5.65,-.18);
+\draw (2.45,-.65) .. controls (3.6,-.65) and (4.85,-.4) .. (5.65,-.18);
 \end{tikzpicture}}
 \normalmarginpar
 
-% Ex and Z=Z_n are on the baseline of the lower (Aut) row; the canceled fragment lies beneath Z=Z_n.
-\[
-\begin{aligned}
-&\text{\uline{Ex}}\quad \mathbb{Z}=\mathbb{Z}_n\quad
-\left\{\begin{aligned}[b]
-\operatorname{End}\mathbb{Z}&=\mathbb{Z}_n\\
-\operatorname{Aut}\mathbb{Z}&=\mathbb{Z}_n^{*}\supset\{\pm1\}=\Gamma
-\end{aligned}\right.\\
-&\hspace{3.8em}\deleted{\Gamma\in}
-\end{aligned}
-\]
+\noindent\uline{Ex}\quad
+\begin{tikzpicture}[baseline=(exgroup.base)]
+\node[anchor=base west,inner sep=0pt] (exgroup) at (0,0) {$\mathbb{Z}=\mathbb{Z}_n$};
+\node[anchor=base west,inner sep=0pt] (exsystem) at ([xshift=.7em]exgroup.base east)
+ {$\left\{\begin{aligned}[b]
+ \operatorname{End}\mathbb{Z}&=\mathbb{Z}_n\\
+ \operatorname{Aut}\mathbb{Z}&=\mathbb{Z}_n^{*}\supset\{\pm1\}=\Gamma
+ \end{aligned}\right.$};
+\node[anchor=north west,inner sep=0pt] at ([xshift=.1em,yshift=-.5em]exgroup.south west)
+ {$\deleted{\unsure{\Gamma\in|\Gamma\subset}}$};
+\end{tikzpicture}
 \margin{(\uline{NB} \unsure{si} $n=2$, $+1=-1$ dans $\mathbb{Z}_n^{*}$\ldots)}
 
 \[
-\begin{aligned}
-&\operatorname{Aff}(\mathbb{Z}_n)=\mathbb{Z}_n\mathbin{.}\mathbb{Z}_n^{*}
- \quad\text{(produit ${}^1\! /\! {}_2$ direct)}
- \quad\raisebox{.7em}{\unsure{\tikz[baseline=0pt]{\fill (0,0) circle (.4pt);\fill (.05,.075) circle (.4pt);}}}\\[-.3em]
-&\text{\llap{\unsure{\tikz[baseline=-.1ex]{\draw[line width=.7pt,line cap=round] (0,.04)--(0,0)--(.025,0);}}\hspace{1.6em}}}
- \hspace{1.7em}\rotatebox{90}{$\subset$}\\[-.3em]
-&\hspace{.5em}\operatorname{Aff}^{\{\pm1\}}(\mathbb{Z}_n)=\mathbb{Z}_n\mathbin{.}\{\pm1\}
-\end{aligned}
+\begin{tikzpicture}[x=1cm,y=1cm,baseline=(afftop.base)]
+\node[anchor=base west,inner sep=0pt] (afftop) at (0,0)
+ {$\operatorname{Aff}(\mathbb{Z}_n)=\mathbb{Z}_n\mathbin{.}\mathbb{Z}_n^{*}
+ \quad\text{(produit $1/2$ direct)}$};
+\node[inner sep=0pt] at (.85,-.62) {\rotatebox{90}{$\subset$}};
+\node[anchor=base west,inner sep=0pt] at (.25,-1.25)
+ {$\operatorname{Aff}^{\{\pm1\}}(\mathbb{Z}_n)=\mathbb{Z}_n\mathbin{.}\{\pm1\}$};
+% Detached angular ink mark left of the comparison; no meaning is assigned to it.
+\draw[line width=.65pt] (-.66,-.39) -- (-.66,-.44) -- (-.62,-.44);
+\end{tikzpicture}
 \]
-% The two upper-right points and the lower-left hooked point have no assigned function; ink/surface status is unresolved.
-\margin{groupe diédral d'indice $n$, $\mathbb{D}_n$ (on suppose $n\ne2$\ldots)}
+\margin{groupe diédral d'indice $n$, $\unsure{\mathbb{D}|D}_n$ (on suppose $n\ne2$\ldots)}
 
-Soit $T$ torseur sous $Z$ groupe cyclique d'ordre $n\geq3$ muni d'une famille $\{u,u^{-1}\}$ de 2 gén. \deleted{\unsure{d'ordre $n$}.}\raisebox{.7ex}{\inserted{inverses l'un de l'}}autre.
+Soit $T$ torseur sous $Z$ groupe cyclique d'ordre $n\geq3$ muni d'une famille $\{u,u^{-1}\}$ de 2 gén. \deleted{d'ordre $n$.}\inserted{inverses l'un de l'}autre.
 \diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=small]
 1\arrow[r] \& Z\arrow[r,dash,"i"] \& \operatorname{Aut}^{\pm1}(T,Z)\arrow[r,dash,"p"]
  \& \{\pm1\}\arrow[r,dash]\arrow[l,bend left=25,"q"] \& 1
```
