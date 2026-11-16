from save_page import save
tex=r'''
\scanpage{32}

\margin{$\phi^{(\ell)}$\quad ${}_{\ell^\nu}P$}
\[
(2.2.4)\qquad\deleted{\unsure{\$}}\phi^{(\ell)}_\xi\deleted{\unsure{\$}}=(\phi^{\ell^\nu}_\xi)_{\nu\geq0},\quad\text{où}\quad\phi^{\ell^\nu}_\xi:{}_{\ell^\nu}P\times{}_{\ell^\nu}Q\longrightarrow G.
\]
Les diagrammes \deleted{déduits}\inserted{commutatifs} de (2.2.2) en y faisant $n=\ell^\nu$, $n'=\ell^{\nu'}$, pour $\nu'\geq\nu$, montrent que $\phi^{(\ell)}_\xi$ peut être interprété comme un accouplement de \deleted{\unsure{progroupes}} systèmes projectifs de groupes
\[
(2.2.5)\qquad\phi^{(\ell)}_\xi:T_\ell(P)\times T_\ell(Q)\longrightarrow T_\ell(G),
\]
où, pour un groupe $M$ de $T$ et un nombre premier $\ell$, on désigne par
\[
T_\ell(M)=({}_{\ell^\nu}M)_{\nu\geq0}
\]
le système projectif des ${}_{\ell^\nu}M$. L'accouplement \deleted{\unsure{\$}} (2.2.5) est encore appelé \uline{l'accouplement $\ell$-adique associé à} $\xi$ (ou à la biextension $E$ de classe $\xi$). Pour $\xi$ variable, on obtient un homomorphisme canonique
\[
(2.2.6)\qquad\operatorname{Biext}^{\inserted{1}}(P,Q;G)\longrightarrow\operatorname{Hom}(T_\ell(P)\otimes T_\ell(Q),T_\ell(G)).
\]
On notera que les homomorphismes (2.1.2) sont \uline{fonctoriels} en $P,Q,G$ (pour $n$ fixé), d'où on déduit qu'il en est de même de (2.2.6).

\figure{\begin{tikzpicture}\draw (0,0)--(1.7,.07);\draw (-.1,-.13)--(1.85,-.1);\end{tikzpicture}}

2.3. \deleted{On peut regarder} La compatibilité (2.2.2) permet de retrouver $\phi^n_\xi$ connaissant $\phi^{n'}_\xi$, pourvu que ${}_{n'}Q\xrightarrow{m}{}_nQ$ \inserted{soit} un épimorphisme, --- \deleted{\unsure{(NB la}} condition satisfaite, comme il est bien connu, si $nQ=Q$. En effet, comme ${}_{n'}P\xrightarrow{m}{}_nP$ est aussi un épimorphisme, $\phi^n_\xi$ se déduit alors de $\phi^{n'}_\xi$ par passage au quotient. On peut cependant \inserted{donner} une compatibilité légèrement plus précise que (2.2.2), qui permet d\deleted{\unsure{e}}'exprimer $\phi^n$ en termes de $\phi^{n'}$ sans aucune restriction sur $Q$, par la commutativité de

(2.3.1)
\diagram{\begin{tikzcd}[column sep=small,row sep=large]
{}_{n'}P \arrow[d,"m"'] & \times & {}_nQ \arrow[d,"\mathrm{id}"] \arrow[rr,"{\phi^{n'}_\xi|_{{}_{n'}P\times{}_nQ}}"] & & {}_nG \arrow[d,"\mathrm{id}"]\\
{}_{\deleted{\unsure{m}}n}P & \times & {}_nQ \arrow[rr,"\phi^n_\xi"] & & {}_nG
\end{tikzcd}},

en formules
\[
(2.3.2)\qquad\phi^n_\xi(mx,y)=\phi^{n'}_\xi(x,y)\qquad(x\in{}_{n'}P(S),\ y\in{}_nQ(S)).
\]
Cette formule implique évidemment la commutativité de (2.2.2), qui s'écrit en effet
\[
\inserted{(2.3.3)}\qquad\phi^n_\xi(mx,my)=m\phi^{n'}_\xi(x,y)\qquad(x\in{}_{n'}P(S),\ y\in{}_{n'}P(S)),
\]
\margin{31}
'''
e=[('margin note','readable top left two ovals','phi^(l); l^nu P'),('display','readable top (2.2.4)','phi^(l)_xi=(phi^(l^nu)_xi)_nu>=0'),('deletion','left of first phi','dollar-like sign'),('deletion','right of first phi','dollar-like sign'),('text','top paragraph','Les diagrammes ... montrent que'),('deletion','top diagrammes qualifier','déduits'),('insertion','above déduits','commutatifs'),('deletion','before systèmes projectifs','progroupes'),('display','(2.2.5)','phi^(l):T_l(P) x T_l(Q) -> T_l(G)'),('text','above Tate-system definition','où, pour un groupe M de T'),('display','upper middle','T_l(M)=(l^nu M)_nu>=0'),('text','upper middle after definition','le système projectif ... homomorphisme canonique'),('deletion','after L’accouplement','dollar-like sign'),('display','(2.2.6)','Biext^1(P,Q;G) -> Hom(T_l(P) tensor T_l(Q),T_l(G))'),('insertion','Biext superscript','1'),('text','middle paragraph','On notera que les homomorphismes ... fonctoriels'),('drawing','between paragraphs','two short horizontal separator strokes'),('text','section 2.3 paragraph','La compatibilité ... permet de retrouver'),('deletion','section opening','On peut regarder'),('insertion','after n prime Q -> nQ','soit'),('deletion','before condition satisfaite','(NB la uncertain'),('insertion','after On peut cependant','donner'),('deletion','d’exprimer typewriter correction','e'),('text','beside square','(2.3.1)'),('diagram','lower middle square','n prime P x nQ -> nG; m,id,id'),('deletion','lower-left square index','m before n'),('text','below square','en formules'),('display','(2.3.2)','phi^n_xi(mx,y)=phi^n prime_xi(x,y)'),('text','bottom paragraph','Cette formule implique évidemment'),('display','bottom (2.3.3)','phi^n_xi(mx,my)=m phi^n prime_xi(x,y)'),('insertion','bottom equation label','(2.3.3)'),('margin note','original bottom left','31')]
d=[{'line':'(2.2.4), two sides of first phi','reading':'deleted dollar signs','alternatives':'scribbled symbols physically obscured; no semantic reconstruction','confidence':'low'},{'line':'before systèmes projectifs','reading':'progroupes','alternatives':'pro-groupes; overtyped with x','confidence':'medium'},{'line':'after L’accouplement','reading':'deleted dollar sign','alternatives':'same heavily obliterated symbol as first display','confidence':'low'},{'line':'2.3 before condition satisfaite','reading':'(NB la','alternatives':'overtyped short parenthetical fragment','confidence':'low'},{'line':'d’exprimer','reading':'cancelled e','alternatives':'overtyped single letter','confidence':'medium'},{'line':'(2.3.1) lower-left index','reading':'deleted m before n','alternatives':'obliterated character','confidence':'low'}]
save(32,tex,e,d,'Upside-down typed sheet read via 180-degree rotation of whole and both halves. Defines the l-adic pairing as a pairing of projective systems, not silently as their inverse limits. Section 2.3 states a stronger torsion compatibility without restriction on Q and refers to nQ=Q for a quotient reconstruction. Final formula visibly has y in n-prime P(S), preserved despite expected Q. Source order is 032 after 031 though typed mathematical continuation connects backward to 030. Pencil 31.',sheet_kind='reused_typed')
