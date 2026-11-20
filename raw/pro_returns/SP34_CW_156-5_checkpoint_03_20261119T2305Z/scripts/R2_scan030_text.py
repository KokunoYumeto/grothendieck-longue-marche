from pathlib import Path
import json
root=Path('/workspace/scratch/4770596940a0')
s=(root/'source/SP34_CW_156-5_witnesses/codex/J156-5-04/pages/J156-5-04_156-5_scan030.tex').read_text()
replacements={
 r"${\unsure{F|\mathcal F}}',F,G$":r"$F',F,G$",
 r'\unsure{déf.}':r'\unsure{déf.|def.}',
 r'\unsure{G|L}':r'\unsure{L|G}',
 r'\unsure{p.r.}':'p.r.',
 r'\unsure{dans|ds}':r'\unsure{ds|dans}',
 r'\unsure{valable|valide}':'valable',
 r'\inserted{\unsure{subdivise}}':r'\inserted{subdivise}',
 r'F.G\quad *':r'F.G\quad{}^{*}',
 'Vérifions quand même C7.':r'Vérifions quand même C$7_0$',
 r"\deleted{$(A\cap B\qquad A,A'\in F',$}":r"\deleted{$(A\cap B\qquad A,A'\in F,$}"
}
for a,b in replacements.items():
 assert a in s,a
 s=s.replace(a,b)
a=s.index('% @ lower right, note on uniqueness')
b=s.index('% @ lower part, corollary',a)
right=r'''% @ lower right, two notes and their separating rules
% The stepped boundary is open on the right, as on the sheet.
\margin{\figure{\begin{tikzpicture}[x=.55cm,y=.55cm,every node/.style={font=\scriptsize,inner sep=1pt}]
 \node[anchor=north west,text width=3.4cm] at (.35,0) {Un peu vif, on trouve par $F'.G=G'$ un $G'$ tel que};
 \node at (2.2,-2.0) {$F'$};
 \node at (3.3,-2.0) {$\preceq$};
 \node at (4.4,-2.0) {$F$};
 \node at (2.2,-2.55) {\rotatebox{90}{$\leq$}};
 \node at (4.4,-2.55) {\rotatebox{90}{$\leq$}};
 \node at (2.2,-3.1) {$G'$};
 \node at (3.3,-3.1) {$\preceq$};
 \node at (4.4,-3.1) {$G$};
 \node[anchor=north west,text width=3.4cm] at (.35,-3.55) {mais il faut vérifier encore l'\uline{unicité}};
 \draw[line width=.6pt] (0,.05) -- (-.04,-4.85);
 \node[anchor=north west,text width=3.2cm] at (.85,-5.1) {Cela amène à dégager};
 \node[anchor=north west,align=left] at (.85,-5.7) {a) $P\ll Q\ll R$ et $P\preceq R$\\\hspace*{.35cm}$\Rightarrow P\preceq Q,\ Q\preceq R$};
 \node[anchor=north west,align=left] at (.85,-7.0) {b) $P\ll Q\ll R$ et $P\leq R$};
 \node[anchor=north west] at (2.35,-7.75) {$\deleted{\Rightarrow P\unsure{\leq|<}}\ Q\leq R$};
 \node[anchor=north west] at (2.35,-8.55) {$\Rightarrow P\leq Q$};
 \draw[line width=.6pt] (.2,-5.0) .. controls (.65,-5.1) and (.72,-5.15) .. (.72,-5.5)
 -- (.72,-7.5) -- (2.15,-7.65) -- (2.15,-9.15);
\end{tikzpicture}}}
'''
s=s[:a]+right+s[b:]
(root/'out/readers/R2/scan030.tex').write_text(s)
# A limited check of a general set-theoretic implication invoked on this page.
A={1};B={1};Ap={1,2};Bp={1,3}
result={'A':sorted(A),'B':sorted(B),'A_prime':sorted(Ap),'B_prime':sorted(Bp),'intersection_inclusion':(Ap&Bp)<=(A&B),'A_prime_subset_A':Ap<=A,'B_prime_subset_B':Bp<=B,'scope':'arbitrary sets only; not a counterexample to the manuscript figure-theoretic claim'}
(root/'out/readers/R2/math030.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
print('Saved scan030.tex')
