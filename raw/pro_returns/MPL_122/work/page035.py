from record import save
tex=r'''\scanpage{35}
\uline{Inconvénient sérieux} de la \unsure{solution|notation}
$\unsure{\operatorname{ad}^{n}|\operatorname{ad}^{\circ}}(S,\unsure{J|I};\mathcal A)$ lorsque $\mathcal A$ satisfait $(\mathrm{AB}\,5)$, $\unsure{\mathfrak I|\mathfrak B}$ $S$ noethérien : les conditions de finitude naturelles (pour $\mathcal A$ loc \unsure{noeth}) sur des systèmes inductifs adiques, ou co. adiques, ou \unsure{fst ann. adiques}, ne semblent pas stables par \uline{conoyaux} [\unsure{dualemt}, dans $\unsure{\mathrm{cc}|\operatorname{ad}}(S,\unsure{J|I};\mathcal A)$ quand $\mathcal A$ satisfait $(\mathrm{AB}\,5^{\unsure{\alpha|*}})$, les \unsure{condns} de finitude artiniennes ne semblent pas stables par noyaux] !!

\deleted{\uline{Exemple} $A$ anneau [noeth], $f,g$ deux éléments de $A$, $M$ un objet de \deleted{\unsure{\(\mathcal A\)}} $\mathcal C$, \unsure{tel que} $(f,g)$ soit \unsure{$M$-régulier}. Soit
\[P=M_f/M=\varinjlim_n M/f^nM\]
($M/f^mM\longrightarrow M/f^nM$ est donné par $f^{n-m}$ ; le système inductif est à morphismes de transition injectifs). Soit
\[Q=\]
}
\mspage{34}
'''
e=[('text','top heading and paragraph','Inconvénient sérieux de la solution'),('text','upper notation','ad^n(S,J;A), AB5, S noethérien'),('text','middle bracket','dualemt, cc(S,J;A), AB5alpha'),('deletion','lower whole example','Exemple A anneau [noeth]'),('deletion','inside cancelled example','mathcal A'),('display','cancelled example','P=M_f/M=varinjlim_n M/f^nM'),('text','cancelled example transition','M/f^mM → M/f^nM est donné par f^{n-m}'),('display','cancelled example last line','Q=')]
d=[('heading last word','solution | notation','Rapid strokes; solution fits visible opening better.','low'),('initial category','ad^n | ad^circ (S,J|I;mathcal A)','Category superscript and second argument uncertain.','low'),('after AB5','fraktur I | fraktur B, S noethérien','Isolated Gothic-looking symbol; its attachment is unclear.','low'),('natural finiteness parenthesis','loc noeth','Abbreviated adjective.','medium'),('list of systems','fst ann. adiques','Heavily compressed abbreviated group; no expansion in transcription.','low'),('dual bracket','dualemt; cc|ad; AB5alpha|star; condns','Several abbreviated words and superscript uncertain.','low'),('cancelled example','deleted mathcal A; tel que; M-régulier','Crossing cancellation lines obscure the letter and agreement ending.','low')]
o=['Distinct final note: serious drawback of finiteness conditions, possible failure of cokernel stability and dual kernel stability. Its category notation remains uncertain before context.','Entire example P=M_f/M and unfinished Q= is cancelled; do not treat as a completed counterexample.']
save(35,tex,e,d,o)
