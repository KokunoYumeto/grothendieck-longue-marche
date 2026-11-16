from save_page import save
tex=r'''
\scanpage{33}

\deleted{\unsure{Les inclusions}}

on a \uline{loc.} des hom
\[
{}_nA\longrightarrow A,\qquad{}_nA'\longrightarrow A'.
\]
d'où \uline{loc.} \unsure{un hom.}
\diagram{\begin{tikzcd}[column sep=large,row sep=large]
\operatorname{Ext}^1(A\mathbin{\overset{L}{\otimes}}A\unsure{'},G_m) \arrow[r] \arrow[dr] & \operatorname{Ext}^1({}_nA\mathbin{\overset{L}{\otimes}}{}_nA',G_m)\unsure{\to0} \arrow[d]\\
 & \operatorname{Hom}({}_nA\otimes{}_nA',G_m)
\end{tikzcd}}

\unsure{qui se recollent}, donc \unsure{un hom défini global\textsuperscript{t}}. Donc l'élément $\xi$ envisagé plus haut nous donne
\[
\phi_n^\xi:{}_nA\otimes{}_nA'\longrightarrow G_m
\]
et par passage à la limite
\[
T_\ell(A)\times T_\ell(A')\longrightarrow T_\ell(G_m)\overset{\text{déf}}{=}\mathbf Z_\ell(1).
\]

\uline{\unsure{Prop.|Rmq}} Dans cet accouplement, $D(\unsure{M'_n|M_n})$ est orthogonal à ${}_nG'$, \deleted{\unsure{et}} (a un sens si ${}_nM'=0$) et \deleted{$\unsure{D(M_n)}$} ${}_nG$ est orth. à $D(M_n)$ (a un sens si ${}_nM=0$). Les accouplements induits
\figure{\begin{tikzpicture}\draw (0,0)--(0,1.8);\end{tikzpicture}}

\diagram{\begin{tikzcd}[column sep=small,row sep=small]
\deleted{\unsure{{}_nA/}} & {}_nA'/{}_nG' & \times & D(M'_n) \arrow[rr] \arrow[ll,bend right=75,no head] & & G_m\\
 & \wr & & \Vert & &\\
 & M'_n & & {}_nT & &
\end{tikzcd}}

et
\diagram{\begin{tikzcd}[column sep=small,row sep=small]
D(M_n) & \times & \unsure{{}_nA|A}/{}_nG \arrow[r,no head] & G_m\\
\Vert & & \wr &\\
{}_nT & & M_n &
\end{tikzcd}},

ainsi que
\diagram{\begin{tikzcd}[column sep=small,row sep=small]
\deleted{\unsure{et}} & {}_nG/{}_nT & \times & {}_nG'/{}_nT'\\
 & \Vert\ \deleted{\unsure{\text{et}}} & & \wr\\
 & {}_nB & & {}_nB'
\end{tikzcd}}
sont ceux qu'on devine.

\uline{Corollaire} Si l'accouplement entre ${}_nB$ et ${}_nB'$ est une dualité parfaite (car $\unsure{{}_nT_n}=\unsure{{}_nT'_n}=0$) \deleted{\unsure{donc}} et si ${}_nM=0$, ${}_nM'=0$, $nB=B$, $nB'=B'$, alors l'accouplement de ${}_nA$ et ${}_nA'$ est une dualité parfaite.
\figure{\begin{tikzpicture}\draw (0,0)--(0,2);\end{tikzpicture}}
\margin{32}
'''
e=[('deletion','top line','Les inclusions'),('text','top second line','on a loc. des hom'),('display','upper quarter','nA -> A, nA prime -> A prime'),('text','above triangle','d’où loc. un hom.'),('diagram','upper triangle','Ext^1(A tensor^L A prime,G_m) -> Ext^1(nA tensor^L nA prime,G_m) -> Hom'),('text','middle paragraph','qui se recollent ... l’élément xi ... donne'),('display','middle torsion pairing','phi_n^xi:nA tensor nA prime -> G_m'),('text','middle','et par passage à la limite'),('display','middle limit pairing','T_l(A) x T_l(A prime) -> T_l(G_m)=def Z_l(1)'),('text','lower half proposition','Prop. Dans cet accouplement ... orthogonal'),('deletion','second line of proposition','et'),('deletion','before nG','D(M_n)'),('drawing','left of proposition','vertical bar'),('text','above first induced pairing','Les accouplements induits'),('diagram','first induced pairing','nA prime/nG prime x D(M prime_n) -> G_m; M prime_n and nT below'),('deletion','left of first quotient','nA/'),('text','between first and second induced pairings','et'),('diagram','second induced pairing','D(M_n) x nA/nG - G_m; nT and M_n below'),('text','between second and third pairings','ainsi que'),('diagram','third pair','nG/nT x nG prime/nT prime; nB and nB prime below'),('deletion','left of third pair','et uncertain'),('deletion','below first quotient third pair','et uncertain'),('text','right of third pair','sont ceux qu’on devine'),('text','bottom corollary','Si l’accouplement entre nB et nB prime ... dualité parfaite'),('deletion','corollary after parenthesis','donc'),('drawing','left of corollary','vertical bar'),('margin note','bottom left','32')]
d=[{'line':'top cancellation','reading':'Les inclusions','alternatives':'strokes under horizontal cancellation','confidence':'low'},{'line':'above triangle','reading':'un hom.','alternatives':'faint phrase possibly plural','confidence':'low'},{'line':'triangle first object','reading':'A prime in second factor','alternatives':'prime not clearly separated from A','confidence':'low'},{'line':'triangle upper-right after object','reading':'arrow to 0','alternatives':'short ink stroke and loop may be an abandoned continuation mark','confidence':'low'},{'line':'below triangle','reading':'qui se recollent; un hom défini globalt','alternatives':'faint compressed handwriting and superscript ending','confidence':'low'},{'line':'lower-half heading','reading':'Prop.','alternatives':'Rmq','confidence':'medium'},{'line':'proposition first D object','reading':'M prime_n','alternatives':'M_n; overwritten subscript/prime','confidence':'low'},{'line':'first induced pairing initial cancellation','reading':'nA/','alternatives':'overwritten initial factor','confidence':'low'},{'line':'second pairing quotient numerator','reading':'nA','alternatives':'A; no clear preceding n','confidence':'low'},{'line':'corollary parenthesis','reading':'nT_n=nT prime_n=0','alternatives':'positions of n above/below baseline uncertain','confidence':'low'},{'line':'corollary deletion','reading':'donc','alternatives':'thick cancellation obscures ending','confidence':'low'}]
save(33,tex,e,d,'Ext-to-Hom triangle constructs the torsion pairing and then the Tate pairing. Orthogonality statement and claim that induced pairings are “ceux qu’on devine” have no detailed proof on this sheet; the corollary derives perfect duality under four explicit torsion/divisibility conditions. Local-to-global gluing wording is faint and is a research reading question. The final corollary parenthesis has unresolved n placements, not silently normalized. No authorial question mark confidently seen except possible trace beside the triangle, kept in the transcription as uncertain short continuation. Pencil 32.')
