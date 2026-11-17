from record import save_page
tex=r'''\scanpage{15}
% archive foliation: 14

\[
\underline{\mathrm{Hom}}(A,M)\simeq
\underline{\mathrm{Hom}}_!(\widehat A,M)\simeq
\mathrm{Hom}_!(\widehat A_{ab},M).
\]
\[\deleted{\unsure{\sharp}}\]
\figure{\begin{tikzpicture}\draw (0,0) -- (.20,.02) -- (.36,-.04);\draw (.55,.15)--(.9,.15);\end{tikzpicture}}

\uline{Ex} $M=\unsure{Ab}$
\diagram{\begin{array}{c}
\underline{\mathrm{Hom}}(B^\circ,Ab)\simeq\widehat B_{ab}\\
\rotatebox{90}{$\simeq$}\\
\mathrm{Hom}_!(\widehat A_{ab}
\end{array}}

\[A=B^\circ\quad|\quad B=A^\circ\]

\diagram{\begin{array}{lll}
\underline{\mathrm{Hom}}_{\deleted{\unsure{\sharp}}}(A,M)\simeq
\mathrm{Hom}^{\deleted{\unsure{\sharp}}}_!(\widehat A,M)
& \deleted{\unsure{\text{cofaisceaux}}} & \text{cofaisceaux sur }A,\ \text{à val. dans }M.\\
\rotatebox{90}{$\simeq$} &&\\
\underline{\mathrm{Hom}}(B^\circ,M)\simeq\mathrm{Hom}^!(\widehat B^\circ,M)
&&\text{faisceaux sur }B,\ \text{à val. dans }M.
\end{array}}

\diagram{\begin{array}{c}
\mathcal F(\mathcal X,M)^\circ\simeq\mathcal F^\vee(\mathcal X,M^\circ)\\
\rotatebox{90}{$\equiv$}\\
(\mathrm{Hom}^!(A,M))^\circ\\
\rotatebox{90}{$\simeq$}\\
\mathrm{Hom}_!(A^\circ,M^\circ)
\end{array}}

$\mathcal F(\mathcal X,M)$ et $\mathcal F^\vee(\mathcal X,M^\circ)$ sont \unsure{duals|duales} l'une de l'autre
\[
\mathcal F(\mathcal X,M)\simeq\mathcal F^\vee(\mathcal X^\circ,M)
\]
\[
\underline{\mathrm{Hom}}^!(A^\circ,M)\simeq\underline{\mathrm{Hom}}_!(A,M^\circ)^\circ
\]
'''
elements=[
('display','top','Hom(A,M), Hom_!(Ahat,M), Hom_!(Ahat_ab,M)'),
('deletion','under A in first display','sharp-like mark'),
('drawing','upper middle','two short ink strokes'),
('text','upper left','Ex M=Ab'),
('diagram','under example','Hom(B opposite,Ab), Bhat_ab; unfinished Hom_!(Ahat_ab'),
('display','middle left','A=B opposite | B=A opposite'),
('diagram','middle','Hom(A,M), Hom_!(Ahat,M); Hom(B opposite,M), Hom^!(Bhat opposite,M)'),
('deletion','middle first Hom','sharp-like subscript'),
('deletion','middle second Hom','sharp-like superscript'),
('deletion','middle after formula','cofaisceaux'),
('text','middle right first row','cofaisceaux sur A, à val. dans M.'),
('text','middle right second row','faisceaux sur B, à val. dans M.'),
('diagram','lower left','F(X,M) opposite, F dual, Hom^!, Hom_!'),
('text','lower right','F(X,M) et F dual sont duals'),
('display','lower right','F(X,M) equivalent F dual(X opposite,M)'),
('display','bottom right','Hom^!(A opposite,M), Hom_!(A,M opposite) opposite'),
]
doubts=[
('top, below first A','deleted sharp-like mark','overwritten or cancelled letter','low'),
('example M=','Ab','initial A compressed','medium'),
('unfinished example continuation','Hom_!(Ahat_ab','argument overwritten; expression stops here','medium'),
('middle Hom decorations','deleted sharp-like marks','unresolved letter or notation','low'),
('middle cancelled word','cofaisceaux','heavy continuous cancellation','low'),
('lower script letters','script F and script X','ordinary calligraphic shapes; retained consistently with 115009','medium'),
('lower right prose','duals','duales; compressed final letters','low'),
]
save_page(115,15,tex,elements,doubts=doubts,notes='Final sheet has an unfinished example after Hom_!(Ahat_ab; no missing closing parenthesis supplied. Set-valued/abelian functor extension identities and duality identities are written without proof. Printed-paper reverse carries no visible printer text on this face.')
