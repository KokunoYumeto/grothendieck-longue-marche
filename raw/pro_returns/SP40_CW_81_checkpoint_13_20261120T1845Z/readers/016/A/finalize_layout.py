from pathlib import Path
p=Path('/workspace/scratch/94548b74fbe0/out/readers/016/A/reading.tex')
s=p.read_text()
start=s.index('et par suite')
end=s.index("\n\nL'intersection")
s=s[:start]+r'''% Opening block: fixed full-scan origin (225,65), 0.0085 cm/source pixel.
% Node source order follows the reading order, including the two insertions.
\figure{\begin{tikzpicture}[x=0.0085cm,y=-0.0085cm]
 \path[use as bounding box] (0,0) rectangle (1455,475);
 \begin{scope}[shift={(-225,-65)}]
  \node[anchor=base west,inner sep=0pt,outer sep=0pt] at (237,124) {et par suite};
  \node[anchor=base west,inner sep=0pt,outer sep=0pt] at (688,137) {$\Sigma_2^-\cup\Sigma_{\deleted{\unsure{2}}1}^+$};
  \node[anchor=base west,inner sep=0pt,outer sep=0pt] at (977,135) {\deleted{\unsure{sera|sont}} est};
  \node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1116,140) {un ouvert};
  \node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1463,144) {connexe};
  % STROKE01: observed [1515,147,1670,161]; uncertain role, hand and surface origin.
  \node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1515,147) {\unsure{\begin{tikzpicture}[x=0.0085cm,y=-0.0085cm,baseline=0pt]
   \path[use as bounding box] (0,0) rectangle (155,14);
   \draw[line width=0.23pt] (0,4) .. controls (18,0) and (36,3) .. (54,2)
    (58,3) .. controls (90,3) and (129,8) .. (155,10);
  \end{tikzpicture}}};
  \node[anchor=base west,inner sep=0pt,outer sep=0pt] at (237,221) {de};
  \node[anchor=base west,inner sep=0pt,outer sep=0pt] at (401,220) {$X$};
  \node[anchor=base west,inner sep=0pt,outer sep=0pt] at (517,221) {donc};
  \node[anchor=base west,inner sep=0pt,outer sep=0pt] at (691,221) {de};
  \node[anchor=base west,inner sep=0pt,outer sep=0pt] at (816,234) {$X\setminus E_2$,};
  \node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1048,235) {contenant};
  \node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1187,178) {\inserted{la comp. conn.}};
  % GUIDE01: source-coordinate path, with both hooked ends preserved.
  \draw[line width=0.28pt] (1166,177) .. controls (1167,197) and (1187,198) .. (1233,200)
   .. controls (1295,203) and (1358,203) .. (1385,209)
   .. controls (1399,213) and (1399,226) .. (1398,234);
  \node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1423,239) {$\Sigma_2^-$};
  \node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1543,205) {\inserted{de $X\unsure{/|\setminus}E_{\unsure{2}}$}};
  % GUIDE02: right endpoint reaches the source boundary; the comma below is separate.
  \draw[line width=0.22pt] (1533,246) .. controls (1535,229) and (1552,221) .. (1570,220)
   .. controls (1603,221) and (1641,233) .. (1670,235);
  \node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1520,263) {,};
  \node[anchor=base west,inner sep=0pt,outer sep=0pt] at (241,326) {donc};
  \node[anchor=base west,inner sep=0pt,outer sep=0pt] at (424,323) {\deleted{\unsure{c'est}}};
  \node[anchor=base west,inner sep=0pt,outer sep=0pt] at (642,333) {égale};
  \node[anchor=base west,inner sep=0pt,outer sep=0pt] at (823,327) {\unsure{:|à}};
  \node[anchor=base west,inner sep=0pt,outer sep=0pt] at (938,344) {$\Sigma_2^-$,};
  \node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1115,340) {donc};
  \node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1294,350) {$\Sigma_1^+\subset\Sigma_2^-$,};
  \node[anchor=base west,inner sep=0pt,outer sep=0pt] at (243,446) {cqfd};
 \end{scope}
\end{tikzpicture}}'''+s[end:]
start=s.index('\\[\n \\begin{aligned}\n &\\Sigma_1^+')
end=s.index('\n\nNotons aussi que', start)
s=s[:start]+r'''% Three closure rows: fixed source origin (150,1430), 0.008 cm/source pixel.
\figure{\begin{tikzpicture}[x=0.008cm,y=-0.008cm]
 \path[use as bounding box] (0,0) rectangle (1530,350);
 \begin{scope}[shift={(-150,-1430)}]
  \node[anchor=base west,inner sep=0pt,outer sep=0pt] at (250,1522) {$\Sigma_1^+\subsetneq\overline{\Sigma_1^+}\subset\Sigma_1^+\cup E_1$};
  \node[anchor=base west,inner sep=0pt,outer sep=0pt] at (293,1638) {$\overline{\Sigma_{12}}\subset\overline{\Sigma_1^-}\cap\overline{\Sigma_2^-}\subset(\Sigma_1^-\cup E_1)\cap(\Sigma_2^-\cup E_2)\subset\Sigma_{12}\cup E_1\cup E_2$};
  \node[anchor=base west,inner sep=0pt,outer sep=0pt] at (172,1755) {$\Sigma_2^+\subsetneq\overline{\Sigma_2^+}\subset\Sigma_2^+\cup E_2$};
  % SPOTS02a/b: source origin (1617,1727); undetermined hand, role and surface origin.
  \node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1617,1727) {\unsure{\begin{tikzpicture}[x=0.008cm,y=-0.008cm,baseline=0pt]
   \path[use as bounding box] (0,0) rectangle (12,15);
   \fill (7.2,1.4) .. controls (10.5,0.5) and (12,3.0) .. (9.0,5.0)
    .. controls (6.3,5.9) and (6.1,3.8) .. cycle;
   \fill (2.0,8.3) .. controls (3.5,6.7) and (5.3,8.6) .. (6.0,10.3)
    .. controls (3.2,12.1) and (1.0,11.2) .. cycle;
  \end{tikzpicture}}};
 \end{scope}
\end{tikzpicture}}'''+s[end:]
start=s.index('\\[\n \\overline{\\Sigma_{12}}\\cap E_1')
end=s.index('\nCar si on avait',start)
s=s[:start]+r'''% Conditions and detached SPOT03: source origin (320,1885), 0.008 cm/source pixel.
\figure{\begin{tikzpicture}[x=0.008cm,y=-0.008cm]
 \path[use as bounding box] (0,0) rectangle (835,125);
 \begin{scope}[shift={(-320,-1885)}]
  \node[anchor=base west,inner sep=0pt,outer sep=0pt] at (332,1995) {$\overline{\Sigma_{12}}\cap E_1\ne\varnothing$,};
  \node[anchor=base west,inner sep=0pt,outer sep=0pt] at (787,1982) {$\overline{\Sigma_{12}}\cap E_2\ne\varnothing$};
  % SPOT03: observed [927,1892,932,1899]; no character, role, hand or surface origin assigned.
  \node[anchor=base west,inner sep=0pt,outer sep=0pt] at (926,1891) {\unsure{\begin{tikzpicture}[x=0.008cm,y=-0.008cm,baseline=0pt]
   \path[use as bounding box] (0,0) rectangle (7,9);
   \fill (2.7,1.1) .. controls (4.3,0.9) and (5.0,4.0) .. (5.7,5.8)
    .. controls (3.7,7.3) and (1.9,7.1) .. (1.6,5.7)
    .. controls (1.6,3.3) and (1.9,2.0) .. cycle;
  \end{tikzpicture}}};
 \end{scope}
\end{tikzpicture}}'''+s[end:]
s=s.replace(r'\begin{tikzpicture}[x=0.007cm,y=-0.007cm,baseline=(cancelbase)]',r'\figure{\begin{tikzpicture}[x=0.007cm,y=-0.007cm,baseline=(cancelbase)]')
s=s.replace(r'\path[use as bounding box] (0,0) rectangle (784,123);',r'\path[use as bounding box] (0,0) rectangle (1185,123);')
s=s.replace('''\\end{tikzpicture}
$\\overline{\\Sigma_1^-}\\cap E_1=\\varnothing$,
\\[''',''' \\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (759,88) {$\\overline{\\Sigma_1^-}\\cap E_1=\\varnothing$,};
\\end{tikzpicture}}
\\[''')
p.write_text(s)
print('Saved graphic groups with explicit source origins and figure wrappers.')
