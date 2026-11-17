from record import save_page
tex=r'''\scanpage{14}
\mspage{7}
% archive foliation: 13

\diagram{
\begin{tikzcd}[column sep=large,row sep=large]
&& \underline{\mathrm{Hom}}(A^\vee,\unsure{(Ens)}) \\
\widehat A \arrow[r,"\approx"] & \underline{\mathrm{Hom}}_!(A^\vee,Ens) \arrow[ur,hook] && A^{\vee\circ} \arrow[ul,hook] \arrow[r,"\approx"] & \underline{\mathrm{Hom}}_{rep}(A^\vee,(Ens)) \\
&& (Kar(A^\circ))^\circ \simeq Kar(A) \arrow[ul,hook] \arrow[ur,hook] \\
&& \unsure{\overline A|\widetilde A} \arrow[u,hook] \\
&& A \arrow[u,hook]
\end{tikzcd}}

\[\overline{\widetilde{\unsure{\mathcal E|E}}}(A)\]

\diagram{
\begin{tikzcd}[row sep=large,column sep=large]
& \underline{\mathrm{Hom}}(A^\circ,(Ens)) & \\
& \mathcal E(A) \arrow[u,hook,"\mathrm{pl.\ fid.}"] & \\
\widehat A \arrow[ur,hook] && A^{\vee\circ} \arrow[ul,hook] \\
& A=\widehat A\unsure{\cap|,}A^{\vee\circ} \arrow[ul,hook] \arrow[ur,hook] &
\end{tikzcd}}

\figure{\begin{tikzpicture}
\draw (0,3.8) .. controls (2.3,4.5) and (3.6,4.4) .. (4.7,3.5) .. controls (7,1.4) and (9,0.1) .. (10,0);
\end{tikzpicture}}

\diagram{
\begin{tikzcd}[row sep=large,column sep=large]
& M & \\
M_1 \arrow[ur,hook] && M_2 \arrow[ul,hook] \\
& \deleted{\unsure{M_\epsilon}}\inserted{\unsure{N}} \arrow[ul,hook] \arrow[ur,hook] & \\
M'_1 \arrow[uu,hook,"\deleted{\unsure{\mathrm{pl.\ fid.}}}"] && M'_2 \arrow[uu,hook,"\deleted{\unsure{\mathrm{pl.\ fid.}}}"'] \\
& N' \arrow[ul,hook] \arrow[ur,hook] \arrow[uu,hook,"\deleted{\unsure{M_0}}\;\deleted{\unsure{\mathrm{pl.\ fid.}}}"] &
\end{tikzcd}}

\[N=M_1\cap M_2\]
\unsure{Ttes} les flèches pl. fid.

Alors on définit une catégorie $\Sigma'$, somme des sous-catégories pleines $M'_1$ et $M'_2$, avec \unsure{int.} $N'$, et un foncteur pl. fid. $\Sigma'\to M$ (factorisant par $M_1\cup M_2$). Mais --- si $M_1,M_2$ \uline{\unsure{ss.}} pleines en $M$ (avec $N$ donc pl. en $M$), et $M'_1-M_1$, $M'_2-M_2$ des équiv., $M'_1$ et $M'_2$ ne sont pas \unsure{néct.} \unsure{ss.} pl. \unsure{de} $\Sigma'$, et $N'-N$ n'est pas tjrs une équivalence.
'''
elements=[
('diagram','upper half','Ahat, Hom_!, Kar(A), A, A dual opposite'),
('display','left beneath upper diagram','bar tilde E(A)'),
('diagram','middle right','Hom(A opposite,Ens), E(A), Ahat, A dual opposite'),
('drawing','across middle','long curved diagonal separator'),
('diagram','lower left','M, M1, M2, N, M1 prime, M2 prime, N prime'),
('deletion','central node of lower left diagram','M epsilon'),
('insertion','central node of lower left diagram','N'),
('deletion','left vertical arrow','pl. fid.'),
('deletion','right vertical arrow','pl. fid.'),
('deletion','central vertical arrow','M0; pl. fid.'),
('display','right of lower diagram','N=M1 intersection M2'),
('text','right of lower diagram','Ttes les flèches pl. fid.'),
('text','right of lower diagram to bottom','Alors on définit une catégorie Sigma prime'),
]
doubts=[
('upper diagram, top object','Hom(A dual,(Ens))','opening parenthesis before Ens obscured','medium'),
('upper diagram, intermediate A','bar A','tilde A; overwritten upper stroke','low'),
('left isolated expression','bar tilde script E(A)','ordinary E','medium'),
('middle right diagram, bottom','intersection','comma-shaped mark','medium'),
('lower diagram, central node','deleted M epsilon, inserted N','overwritten single N; uncertain correction layers','low'),
('lower diagram, central vertical','deleted M0 and pl. fid.','dense cancellation obscures letters','low'),
('beside lower diagram','Ttes','abbreviation for toutes; initial compressed','medium'),
('lower paragraph','int.','abbreviation and final stroke uncertain','low'),
('lower paragraph','ss.; néct.; ss. pl. de','compressed abbreviations; last preposition uncertain','low'),
]
save_page(115,14,tex,elements,doubts=doubts,notes='Category amalgamation paragraph: full subcategories and equivalences need not give full embeddings into Sigma prime or an equivalence of intersections. Upper diagrams connect Kar(A), presheaves, dual presheaves and E(A); intermediate A decoration doubtful. No contextual interpretation used.')
