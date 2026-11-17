from record import save
save(15,r'''\scanpage{15}
Ceci posé, on \unsure{suppose} $W$ construit en recollant $P$ et $Q$ suivant leurs bords \deleted{\unsure{communs}} via $\varphi$.

\deleted{\unsure{On peut}}

\deleted{\unsure{On aura}}

L'hypothèse que $\partial P$ est un fibré trivial sur $S$ implique que l'inclusion \deleted{\unsure{un}}
\diagram{\begin{tikzcd}
W-Q=P-\partial P \arrow[r,hook] & P
\end{tikzcd}}
est un isomorphisme d'homotopie,

\deleted{\unsure{En fait}}

et de même pour
\diagram{\begin{tikzcd}
W-P=Q-\partial Q \arrow[r,hook] & Q & \text{''\qquad ''\qquad ''}.
\end{tikzcd}}

\deleted{\unsure{On a donc}}

Considérons le diagramme
\diagram{\begin{tikzcd}[row sep=large,column sep=large]
& & T=\partial M & t \arrow[l,very thick] \\
& W & Q \arrow[l,hook] \arrow[u,"\unsure{2|q}"] & N=D_{\unsure{1}}\sim e \arrow[l,hook] \arrow[u,hook,very thick] \\
\partial N=S^1 & P \arrow[l] \arrow[u,hook,very thick] & {\begin{gathered}S^1\times T=\partial N\times\partial M\deleted{\unsure{\partial}}\\=\partial P=\partial Q=P\cap Q\end{gathered}} \arrow[l,hook] \arrow[u,hook] & \partial N=\unsure{S^1} \arrow[l] \arrow[u,hook] \\
s \arrow[u] & M \arrow[l] \arrow[u,hook] & \partial M=T \arrow[l,hook] \arrow[u,hook] & (s,t) \arrow[l,hook] \arrow[u,hook]
\end{tikzcd}}
\mspage{14}
''',[
('text','top three lines','Ceci posé, on suppose W construit'),
('deletion','line 3 before via','communs'),
('deletion','upper middle first attempt','On peut'),
('deletion','upper middle second attempt','On aura'),
('text','upper middle','L’hypothèse que ∂P est un fibré trivial sur S'),
('deletion','after l’inclusion','un'),
('diagram','middle','W−Q=P−∂P → P'),
('text','right of first inclusion','est un isomorphisme d’homotopie'),
('deletion','below first inclusion','En fait'),
('text','middle','et de même pour'),
('diagram','second inclusion and ditto marks','W−P=Q−∂Q → Q'),
('deletion','above Considérons','On a donc'),
('text','above main diagram','Considérons le diagramme'),
('diagram','lower half','T=∂M; t; W; Q; N=D_1∼e; P; M; S¹×T'),
('deletion','central diagram object after ∂M','∂'),
('margin note','bottom left','14')
],[
('line 1','suppose','Very compressed verb; “suppose” is the best letter-based reading.','medium'),
('line 3','communs (deleted)','A cancellation masks most internal letters.','low'),
('upper middle','On peut; On aura (deleted)','Two abandoned starts, heavily struck.','low'),
('after l’inclusion','un (deleted)','Only a short wavy trace survives beneath the strike.','low'),
('middle','En fait; On a donc (deleted)','Crossed-out starts; endings obscured.','low'),
('diagram, Q→T','2|q','The small arrow label resembles 2; it is not silently read as a projection name.','low'),
('diagram, N','D_1','The 1 appears at baseline/subscript height, not confidently as a superscript.','medium'),
('diagram centre','∂ (deleted)','Small crossed mark after ∂M may be an abandoned boundary sign.','low'),
('diagram right','S^1','A thick extra stroke below the superscript is not confidently separable.','medium')
],['Hypothesis of boundary fibration triviality is invoked before the interior inclusion homotopy isomorphism; assess dependence only after freeze.','Specialization N=D_1∼e, ∂N=S¹ enters the large diagram without an explicit accompanying sentence.'])
