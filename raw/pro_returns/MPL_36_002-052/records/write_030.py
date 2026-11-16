from save_page import save
tex=r'''
\scanpage{30}

or le premier membre (grâce à (2.3.2)) est $\phi^{n'}(x,my)=m\phi^{n'}(x,y)$. La compatibilité \deleted{(2.3.1)} (\unsure{2.3.2|2.2.2}) \deleted{est}\inserted{implique} à son tour \deleted{\unsure{conséquence de}} la compatibilité symétrique\inserted{de (2.3.1)}, exprimée par la commutativité de

(2.3.\unsure{4|3})
\diagram{\begin{tikzcd}[column sep=small,row sep=large]
\deleted{\unsure{et}} & {}_nP \arrow[d,"\mathrm{id}"'] & \times & {}_{n'}Q \arrow[d,"m"] \arrow[rr,"{\phi^{n'}_\xi|_{{}_nP\times{}_{n'}Q}}"] & & {}_nG \arrow[d,"\mathrm{id}"]\\
 & {}_nP & \times & {}_nQ \arrow[rr,"\phi^n_\xi"] & & {}_nG
\end{tikzcd}},

qui s'écrit en formules
\[
(2.3.\unsure{5|4})\qquad \phi^n(x,my)=\phi^{n'}(x,y)\qquad (x\in{}_nP(S),\ y\in{}_nQ(S)).
\]

\deleted{Montrons comment (2.3.\unsure{2}) implique (2.3.\unsure{4}), avec les notations de cette dernière formule,}
Comme ${}_{mn'}P\xrightarrow{m}{}_nP$ est un épimorphisme, on est ramené à prouver (2.3.2) dans le cas où $x=mx'$, où $x'\in{}_{n'}P(S)$, \deleted{donc}\inserted{or} on a
\[
\deleted{\unsure{\phi^n(mx,y)=\phi^n(m^2x',y)=\phi^n}}
\quad
\phi^n_{\inserted{\xi}}(mx',my)\overset{\inserted{(2.3.3)}}{=}m\phi^{n'}_{\inserted{\xi}}(x',y)=\phi^{n'}_{\inserted{\xi}}(mx',y)
\]
(par bilinéarité de $\phi^{n'}$) $=\phi^{n'}_{\inserted{\xi}}(x,y)$ puisque $x=mx'$ dans ${}_{n'}P(S)$, ce qui établit (2.3.5).

Prouvons donc la compatibilité (2.3.1). La fonctorialité\inserted{en $Q$} de l'\unsure{homomorphisme} (2.1.2) nous montre qu'on peut supposer $nQ=0$. Alors (2.1.2) est le composé

\diagram{\begin{tikzcd}[column sep=small]
\operatorname{Biext}^1(P,Q;G) \arrow[r,"\sim"] & \operatorname{Hom}(\underline{\operatorname{Tor}}_1(P,Q),G) & \operatorname{Hom}({}_nP\otimes Q,G) \arrow[l,"\sim"']
\end{tikzcd}},

\deleted{en $Q$ nous montre que (2.1.2) est le composé}
\[
\deleted{\operatorname{Biext}^1(P,Q;G)\qquad\operatorname{Hom}(\operatorname{Tor}_1(P,Q),G)\qquad\operatorname{Hom}(\operatorname{Tor}_1(P,{}_nQ),G)}
\]

où la première flèche est celle de (1.1.3) et ne dépend pas du choix de $n$, et où la deuxième flèche est transposée de l'isomorphisme $\underline{\operatorname{Tor}}_1(P,Q)\overset{\inserted{\unsure{\delta|\partial}}}{\xrightarrow{\sim}}{}_nP\otimes Q$ défini dans (1.3.4). Donc la compatibilité voulue équivaut essentiellement à \deleted{\unsure{voir}} la commutativité du diagramme

\diagram{\begin{tikzcd}[row sep=small,column sep=large]
 & {}_{n'}P\otimes Q \arrow[dd,"m\otimes\mathrm{id}_Q"]\\
\underline{\operatorname{Tor}}_1(P,Q) \arrow[ur] \arrow[dr] & \\
 & {}_nP\otimes Q\quad\deleted{\unsure{+}}\quad\deleted{\unsure{\xi}}
\end{tikzcd}},

où les flèches obliques sont les deux isomorphismes du type (1.3.4), relatifs à $n$ et $n'$ respectivement. Or cette compatibilité résulte de

\margin{29}
'''
e=[('text','readable orientation, top paragraph','or le premier membre'),('deletion','top paragraph old reference','(2.3.1)'),('deletion','top paragraph verb','est'),('insertion','above deleted est','implique'),('deletion','top paragraph after à son tour','conséquence de'),('insertion','above symétrique','de (2.3.1)'),('text','beside first diagram','(2.3.4) corrected digit'),('diagram','upper quarter','nP x n prime Q -> nG; id,m,id'),('deletion','left of first diagram','et uncertain'),('text','below first diagram','qui s’écrit en formules'),('display','upper middle (2.3.5)','phi^n(x,my)=phi^n prime(x,y)'),('deletion','two typed lines before Comme','Montrons comment ... dernière formule'),('text','middle paragraph','Comme mn prime P -> nP est un épimorphisme'),('deletion','middle before on a','donc'),('insertion','above donc','or'),('deletion','middle formula initial cancelled chain','phi^n(mx,y) = phi^n(m^2 x prime,y)=phi^n'),('display','middle live formula','phi^n_xi(mx prime,my)=m phi^n prime_xi(x prime,y)'),('insertion','first phi in live formula','xi'),('insertion','over equality in live formula','(2.3.3)'),('insertion','second phi in live formula','xi'),('insertion','third phi in live formula','xi'),('text','following formula','par bilinéarité ... établit (2.3.5)'),('insertion','phi in following text','xi'),('text','middle-lower paragraph','Prouvons donc la compatibilité'),('insertion','above fonctorialité','en Q'),('diagram','middle-lower chain','Biext^1 -> Hom(Tor_1,G) <- Hom(nP tensor Q,G)'),('deletion','below chain typed line','en Q nous montre que ... composé'),('deletion','below typed line cancelled display','Biext^1 Hom(Tor_1) Hom(Tor_1(P,nQ),G)'),('text','lower paragraph','où la première flèche est celle de'),('insertion','above Tor isomorphism','delta / partial'),('deletion','before la commutativité','voir uncertain'),('diagram','lower triangle','Tor_1(P,Q); n prime P tensor Q; nP tensor Q'),('deletion','right of triangle bottom object','+ uncertain'),('deletion','right of triangle bottom object, second mark','xi uncertain'),('text','bottom two lines','où les flèches obliques ... résulte de'),('margin note','original scan bottom left','29')]
d=[{'line':'top paragraph reference','reading':'2.3.2','alternatives':'2.2.2; overwritten middle digit','confidence':'medium'},{'line':'top paragraph cancellation','reading':'conséquence de','alternatives':'overstrike obscures letters','confidence':'medium'},{'line':'first diagram number','reading':'2.3.4','alternatives':'2.3.3; overwritten last digit','confidence':'medium'},{'line':'first display number','reading':'2.3.5','alternatives':'2.3.4; overwritten last digit','confidence':'medium'},{'line':'middle cancelled formula','reading':'phi^n(mx,y)=phi^n(m^2 x prime,y)=phi^n','alternatives':'arguments/handwritten 2 under heavy cancellation','confidence':'low'},{'line':'fonctorialité paragraph','reading':'homomorphisme','alternatives':'initial typewriter letters overlap','confidence':'medium'},{'line':'lower Tor isomorphism annotation','reading':'delta','alternatives':'partial','confidence':'low'},{'line':'lower paragraph deletion','reading':'voir','alternatives':'four overstruck letters','confidence':'low'},{'line':'bottom triangular diagram cancelled marks','reading':'+; xi','alternatives':'two small obliterated symbol marks','confidence':'low'}]
save(30,tex,e,d,'Reused typed sheet, upside down in scan, read after lossless 180-degree rotation of whole and both supplied halves. Compatibility calculations for torsion biextension pairings, with two square/triangle diagrams and several corrected numbering references. Preserved mn-prime in epimorphism and all displayed n/n-prime indices even when surprising. The proof ends mid-sentence “Or cette compatibilité résulte de”; continuation not inferred. This is not an authorial self-flagged doubt, but an excerpt boundary. Pencil 29 is in original scan orientation.',sheet_kind='reused_typed')
