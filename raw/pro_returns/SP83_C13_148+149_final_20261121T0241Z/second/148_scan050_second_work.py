"""Independent crop readings, written before consulting any first reading."""
READINGS = {
'B01': r'''\mspage{6}''',
'B02': r'''\uline{\unsure{Remarque|Remarques}}''',
'B03': r'''\deleted{\unsure{complétée}}\deleted{\unsure{remplacée}}\inserted{\unsure{remplacée|remplacé}}''',
'B04': r'''\deleted{une application}\inserted{une \deleted{\unsure{triple}} famille}''',
'B05': r'''$\unsure{A}\quad
\begin{array}{r@{}c@{}l}
\deleted{(\widetilde R,\alpha,\unsure{p|\rho}:R\longrightarrow}&\deleted{\vec A}&\deleted{)}\\
&\Vert&\\
&\unsure{\vec A/\sigma|\deleted{\vec A/\sigma}}&
\end{array}$''',
'B06': r'''\margin{$\omega(a)\overset{\mathrm{def}}{=}\{\vec a\in\vec A/\vec a\ \text{\unsure{au} dessus de }a\}$}''',
'B07': r'''d'ensembles, et pour $\forall a\in A$, si $\omega(a)$ désigne l'ens des
\unsure{deux|des} \unsure{orientations|directions} ``de $a$'' $(\operatorname{card}\omega(a)\in\{1,2\})$, une application
\deleted{\illegible{9}}''',
'B08': r'''\deleted{$R$ et $p$ une application $R\longrightarrow A$ \unsure{qui} \illegible{2} $\unsure{a}$}''',
'B09': r'''$\omega\mapsto u_\omega:\omega(a)\longrightarrow\operatorname{Circ}(R_a)$ ens des \unsure{permutations|permutat.},
circulaires sur $R_a$''',
'B10': r'''\deleted{et \unsure{relie} à \unsure{une} \unsure{bi.} une application \uline{injection}}
\deleted{$R/\alpha\unsure{\lhook\joinrel\longrightarrow|\longrightarrow}\vec A$}''',
'B11': r'''que si $\omega,\omega'\in\omega(a)$, $\omega\ne\omega'$, alors
\deleted{$u_\omega u_{\omega'}=\operatorname{id}_{R_a}$}
$u_{\omega'}=u_\omega^{-1}$''',
'B12': r'''\unsure{simplification} \unsure{vient|vraie} : la donnée des''',
'B13': r'''\begin{tikzpicture}[x=1cm,y=1cm]
\node[anchor=west] at (1.1,0) {$\nu:A\longrightarrow\mathbb N$};
\draw[line width=.7pt] (1.12,-.48)--(1.16,-.74);
\draw[line width=.7pt] (1.28,-.54)--(1.31,-.76);
\node[anchor=west] at (0,-1.2) {$a\longmapsto\operatorname{card}p^{-1}(a)$};
\end{tikzpicture}''',
'B14': r'''et la donnée d'une famille''',
'B15': r'''$(R_a)_{a\in A}$, \deleted{\illegible{1}}''',
'B16': r'''$R_a$ un torseur sous $\mathbb Z/\nu(a)\mathbb Z\underset{\{\pm1\}}{\wedge}\omega(a)$ On associe''',
'B17': r'''\inserted{($\widetilde\Sigma_a$ le comp. connexe de $\widetilde\Sigma$ \deleted{\unsure{correspondant}} \inserted{qui correspond à} $a\in A\simeq\pi_0(\widetilde\Sigma)$)}''',
'B18': r'''\deleted{$R=\ell(\unsure{\partial C|\alpha C})$,}
\deleted{\begin{tikzpicture}[x=1cm,y=1cm,baseline=(R.base)]
\node (R) at (0,1.2) {$\unsure{\widetilde R|R}$};
\node (S) at (2.5,1.2) {$S$};
\node (I) at (0,0) {$\unsure{I|1|i}$};
\node (P) at (2.5,0) {$\pi_0(\unsure{\Sigma|\widetilde\Sigma})$};
\draw[->] (R)--(S);
\draw (0.01,.86)--(.04,.62)..controls(.07,.53)and(.13,.52)..(.19,.53);
\draw (.16,.82)--(.18,.57);
\draw (2.42,.84)--(2.44,.57);
\draw (2.56,.83)--(2.58,.58);
\draw (I.east)--(P.west);
\end{tikzpicture}}''',
'B19': r'''\deleted{et $p$ déduit de \illegible{3} \unsure{sur} \illegible{1} $R_a$}''',
'B20': r'''\uline{NB} Même si $\nu(\omega)=1$ ou $\nu(\omega)=2$, le fait de distinguer''',
'B21': r'''49''',
}

NOTES = {
'B02': 'The final e/s-like run is compressed; no missing continuation is supplied.',
'B03': 'Several overlapping word-level revisions occupy this target. Two crossed lower groups and a raised replacement are retained; the old wording and replacement ending remain doubtful.',
'B04': 'The lower application is crossed. A raised une precedes a crossed triple-like group and the live famille. Surrounding clipped ascenders at the top are context.',
'B05': 'The A-like group just before the cancelled tuple is retained with scope uncertainty. The lower target annotation is overworked; its cancellation state is doubtful. Small clipped strokes at the top and bottom belong to adjacent context.',
'B06': 'Read the sloping marginal baseline, excluding the large crossing main-text letters. A rotated rendering of this same exact box was used. The short word before dessus remains partly obscured; no target continuation is clipped.',
'B07': 'Two live lines are included. The intervening cancelled line is too obscured for a reliable reading; nine is an approximate count of separated word/symbol groups, not a recovered phrase. The upper and lower edges also clip incidental adjoining text. An orientation helper uses exactly this source box.',
'B08': 'The cancelled line is preserved. Its last groups remain obscured and are not restored from syntax. Upper and lower edges clip neighboring live lines; these are read in B07 and B09. An orientation helper uses exactly this source box.',
'B09': 'Read the live map and its two-line explanation. The abbreviation or full ending of permutations remains compressed. The cancelled line through the middle is read separately in B10. No absent continuation is supplied. An orientation helper uses exactly this source box.',
'B10': 'The whole cancelled sentence and its separate cancelled map are included. Several old word groups and the map arrow tail remain doubtful. The live text clipped at the top and bottom is separately covered by B09 and B11. An orientation helper uses exactly this source box.',
'B11': 'Both the cancelled product identity and its live inverse replacement are retained, including the numeric exponent minus one. The initial que is complete; context outside this box is not supplied.',
'B12': 'The two leading words remain uncertain from the pen forms. Ascenders of the following la donnée des are partly clipped by the upper boundary; that fragment is retained, without supplying the continuation.',
'B13': 'The two-line map and its numeric exponent minus one are complete. Two short near-vertical strokes between the lines are drawn as marks without assigning them a semantic value. The lower endpoint of the initial a and mapsto is close to the bottom edge but the reading is recoverable.',
'B14': 'The two tall l ascenders in famille reach or pass the upper crop boundary; the word remains readable. No continuation beyond the last word is supplied.',
'B15': 'The full indexed family is visible. The following heavily blackened group is not securely recoverable as either a word or a symbolic expression; illegible one records one contiguous group, not a confident word count.',
'B16': 'The contracted-product-shaped expression is retained with its omega(a) factor and the full ±1 index. The fragment On associe follows without any securely visible separating punctuation.',
'B17': 'The target is the raised explanatory insertion. Its inner crossed correspondant-like word and live qui correspond à are both preserved. Incidental portions of the long cancelled line crossing the lower half belong to the neighboring cancelled display/passage, not to this insertion. A far-right curved stroke may be punctuation or another closing parenthesis; its attachment lies outside the secure target scope.',
'B18': 'The entire visible cancelled expression and diagram are preserved, but the argument of ell, the top-left accent, and the lower-left object remain doubtful. The left vertical connector is reproduced as two actual short paths with a bent lower end, without declaring it an arrow or equality. The lower connector has no secure visible arrowhead and is drawn as a plain shaft. The right parenthesis of the lower-right object is clipped by the right edge. The line of prose clipped below is context.',
'B19': 'The cancelled line is read independently, with its obscured middle represented as unknown groups. The three-plus-one counts are approximate separations of ink groups, not recovered wording. Cropped context above and the following live NB line are excluded here; B20 contains the latter.',
'B20': 'The underlined NB and both numeric equalities are retained. The argument resembles omega and has not been changed to a on mathematical grounds. The final word is intact; continuation outside the rectangle is not supplied.',
'B21': 'Pale lower folio annotation 49; no attribution of its hand is inferred.',
}
