from save_page import save_page
save_page(61,r'''\scanpage{61}
% archive foliation: 60
\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw[gray] (-1.2,.25)--(-1.25,-.15);
\draw[->] (.7,0)--(0,0);
\draw (2.85,.15)--(2.81,-.16);
\draw (3.08,.18)--(3.12,-.02)--(3.2,-.2);
\end{tikzpicture}}

\deleted{il en est de même de la famille $(u')$ qui s'en déduit par le change-\newline
ment de base $X'\quad X$.

On aura expliqué au préalable}
''',[
('middle; scan orientation','drawing','left arrow and isolated short pen strokes'),
('bottom; inverted typescript','text',"il en est de même de la famille (u') qui s'en déduit"),
('bottom; inverted typescript','text','On aura expliqué au préalable')],sheet_kind='reused_typed',remarks='Whole page, both halves, and 180-degree rotated page inspected. Entire three-line typescript cancelled by diagonal strokes. No arrow supplied in the printed blank between X-prime and X; isolated central ink marks reproduced as TikZ strokes.')
