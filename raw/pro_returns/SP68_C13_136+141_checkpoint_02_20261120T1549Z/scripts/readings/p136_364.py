import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from workflow import Page
p=Page(136,364)
p.tex=r'''\cotefile{136}
\scanpage{364}
\mspage{3}
\diagram{\begin{tikzcd}[row sep=large]
\underline{H_*(K(\mathbb F_p,n),\mathbb F_p)}^*\simeq H^{n+r}(K(\mathbb F_p,n),\mathbb F_p)\arrow[d,bend left=15]\\
\text{operations coh de type}
\end{tikzcd}}
\diagram{\begin{tikzcd}
K(Z,n)\arrow[r]&K(Z,n\arrow[r]&K(\mathbb F_p,n)
\end{tikzcd}}
Puisque $K(\mathbb F_p,n)$ représente la $\mathbb F_p$, coh
\[
(\mathbb F_p,n,\mathbb F_p,n+r)
\]
$r<n$

Operations stables de deg $r$

$\{P_r\}$\qquad Une collection $\forall n$
\diagram{\begin{tikzcd}
H^n(X,\mathbb F_p)\arrow[r]&H^{n+r}(X,\mathbb F_p)
\end{tikzcd}}
commute
\diagram{\begin{tikzcd}[column sep=large]
\overline H^{n+1}(SX,\mathbb F_p)\arrow[r,"P_{n+1}"]\arrow[d,draw=none,"{\rotatebox{90}{$\simeq$}}" description]&\overline H^{n+1+r}(SX,\mathbb F_p)\arrow[d,draw=none,"{\rotatebox{90}{$\simeq$}}" description]\\
\widetilde H^n(X,\mathbb F_p)\arrow[r,"P_n"]&\widetilde H^{n+r}(X,\mathbb F_p)
\end{tikzcd}}
\margin{$r<n$}
\diagram{\begin{tikzcd}[column sep=small]
&H^{n+r}(K(\mathbb F_p,n),\mathbb F_p)\arrow[dl]&\simeq H^{n+r+1}(K(\mathbb F_p,n+1),\mathbb F_p)\\
H^{n+r-1}(K(\mathbb F_p,n-1,\mathbb F_p)&P_n'&P_{n+1}'
\end{tikzcd}}

\uuline{Operations stables}: Les op stable sont \deleted{\unsure{el}} donnés par l'algebre de Steenrod

$p\ne2$
\[
\mathbb F_p[\underline{P^0,P^1,\ldots P^n,\ldots,\beta}]
\]
\[
P^0=1\qquad\deg P^i=2i(p-1)\qquad\deg\beta=1
\]
Relations d'Adem

\margin{Cohomology operations\par
Steenrod $+$ Epstein\par
Ann of Math Studies N° 50\par
Princeton\par
p 77}
\mspage{365}
'''
p.change('top display, underline',r'\underline{H_*(K(\mathbb F_p,n),\mathbb F_p)}^*',r'H_*(K(\mathbb F_p,n),\mathbb F_p)^*',r'\underline{H_*(K(\mathbb F_p,n),\mathbb F_p)}^*','A thin continuous line lies below the homology expression, ending before the raised star.','omission',against_c=False)
p.change('small K sequence, two Zs','Z',r'\mathbb Z','Z','The two Zs are single handwritten zigzags; the F letters elsewhere have a distinct doubled stem.','misread symbol or index',against_c=False,crop='136_scan364 (530,260,1100,375)')
p.change('small K sequence, middle term','K(Z,n','K(Z,n)','K(Z,n','After the compact n there is no separate closing parenthesis before the right arrow.','text not on the page',confidence='medium',against_c=False,crop='136_scan364 (530,260,1100,375)')
p.change('Puisque line','represente','représente','représente','The small acute stroke belongs to the first e of représente.','misread word',against_h=False)
p.change('operation type punctuation',r'(\mathbb F_p,n,\mathbb F_p,n+r)',r'(\mathbb F_p,n;\mathbb F_p,n+r)',r'(\mathbb F_p,n,\mathbb F_p,n+r)','The separator between the two pairs is a single long comma; no upper dot.','other',against_c=False)
for side in ['left','right']:
 p.change('suspension square, upper '+side,r'\unsure{\overline H|\widetilde H}',r'\widetilde H',r'\overline H','The mark over H is a short almost horizontal bar, unlike the visibly waved mark on the lower row.','misread symbol or index',against_c=False)
p.change('suspension square, vertical identifications','arrowless rotated isomorphism marks','up arrows (editorially supplied)','arrowless rotated isomorphism marks','Each vertical sign is two curved parallel strokes; neither has an arrow shaft or point.','drawing or diagram',against_c=False)
p.change('lower left group','K(F_p,n-1,F_p)','K(F_p,n-1),F_p)','K(F_p,n-1,F_p)','No inner closing parenthesis is present after n-1; the only close is after the final coefficient.','text not on the page',against_c=False,crop='136_scan364 (120,1120,1605,1370)',math=True)
for term in ['P_n','P_{n+1}']:
 p.change('below comparison, '+term,term+r"^{\unsure{'|i}}",term,term+"'",'A short isolated raised stroke is visible to the right of P; it has no separate dot-and-stem i construction.','omission',confidence='medium',against_c=False,crop='136_scan364 (120,1120,1605,1370)',math=True)
p.change('Les op line','stables','stables','stable','The terminal e runs directly into the space before sont, with no final s.','misread word',crop='136_scan364 (865,1380,1595,1545)')
p.change('Les op line','données','données','donnés','After the two n arches the accented e leads directly into final s; no second e can be distinguished.','misread word',confidence='medium',crop='136_scan364 (865,1380,1595,1545)')
p.change('crossed fragment after sont',r'\deleted{\unsure{el|et}}',r'\struck{\ill{}}',r'\deleted{\unsure{el}}','An initial e-shaped loop and a tall loop remain beneath the hatch; no clear t crossbar survives. The fragment is still uncertain.','readable ink left as \\ill{}',confidence='low',against_c=False,crop='136_scan364 (865,1380,1595,1545)')
p.change('Steenrod algebra display and following line','underlined generators; Relations d’Adem on its own line','quotient by Relations d’Adem','underlined generators; Relations d’Adem on its own line','The line under the generators is followed immediately by three degree identities; Relations d’Adem is a separate line below these, not a fraction denominator.','drawing or diagram',against_c=False,math=True)
for ident in range(1016,1034):
 if ident in [1016,1017,1018,1020,1022,1024,1027,1028,1029]:
  p.decision(f'M{ident}','first','K','Angular stem and two arms, compressed almost to a pi shape; the more open K on the lower comparison confirms the same notation.',crop='136_scan364 (530,260,1100,375)' if ident in [1018,1020,1022] else 'page')
 elif ident in [1019,1021,1023]: p.decision(f'M{ident}','first','n','Compact two-stroke n, not a solitary 1.',crop='136_scan364 (530,260,1100,375)',confidence='medium')
 elif ident in [1025,1026]:p.decision(f'M{ident}','first',r'\overline H','A short flat bar over H; the lower row has a separate waved tilde.')
 elif ident in [1030,1032]:p.decision(f'M{ident}','first',"'",'A short raised tick, without the separate stem and dot of i.',crop='136_scan364 (120,1120,1605,1370)',confidence='medium')
 elif ident==1031:p.decision(f'M{ident}','first','1','A long single slanted numeral after n+; the raised tick belongs to P.',crop='136_scan364 (120,1120,1605,1370)')
 else:p.decision(f'M{ident}','first','Adem','Final connected humps form m, not n.')
for kind,pos,words in [('margin note','top right','3'),('display','top','underlined H_* dual ≃ H^{n+r}'),('diagram','upper','K(Z,n) → K(Z,n → K(F_p,n)'),('text','upper left','Puisque K(F_p,n) représente'),('text','upper right, arrow from top','operations coh de type'),('display','upper left','(F_p,n,F_p,n+r)'),('display','left below type','r<n'),('text','upper right','Operations stables de deg r'),('display','right','{P_r}; Une collection ∀n'),('diagram','right middle','H^n(X,F_p) → H^{n+r}(X,F_p)'),('text','left of square','commute'),('diagram','middle','suspension square; bars, tildes; arrowless identifications'),('margin note','left fold','r<n'),('diagram','below fold','three cohomology groups, diagonal arrow, P primes'),('text','lower middle','Operations stables: Les op stable sont'),('deletion','after sont','el'),('display','lower left','p≠2'),('display','lower middle','F_p[P^0,P^1,…,P^n,…,β] with underline'),('display','below generators','P^0=1; deg P^i=2i(p-1); deg β=1'),('text','below degrees','Relations d’Adem'),('margin note','lower left','Cohomology operations / Steenrod + Epstein / Ann of Math Studies N°50 / Princeton / p77'),('margin note','bottom left, pencil','365')]:p.element(kind,pos,words,hand='unnamed hand (pencil foliation)' if words=='365' else 'his hand')
p.note('Manuscript page 3; pencil foliation 365. The page relates cohomology operations to cohomology of K(F_p,n), defines stability through suspension, and records the odd-prime Steenrod generators, their degrees and the name of the Adem relations. A bibliography in the lower left names Cohomology operations, Steenrod + Epstein, Ann of Math Studies N°50, Princeton, p77; no external source was consulted.')
p.note('The first displayed dual is literally H_* dual while the right side has fixed degree n+r. No degree subscript was silently supplied. The small K sequence and the lower left group omit a closing parenthesis as recorded. The lower P labels have isolated raised ticks, read as primes, not the mathematically tempting i. The top row of the suspension square uses flat bars and the bottom row waved tildes: the intended reduced-cohomology notation does not justify making their drawn marks identical.')
p.note('Degree accounting for the square was checked: suspension raises both n and n+r by one; the arrow labels are P_n and P_{n+1}. This check directs attention to the indices but is not a proof of the stability or generation assertions. There is no explicit authorial “à vérifier” on this sheet.')
p.habit('K has a flattened upper arm and can resemble π or κ. All nine relevant marked occurrences on this page are consistent with K; the open K below the fold anchors the identification. C doubted K/κ at each; H used K. This is a page-local pattern, to be rechecked on later sheets.')
p.habit('Reduced-cohomology marks vary in shape within one square: two short flat bars above, two waves below. C left the upper pair doubtful; H regularized them to tildes. The distinction is preserved, not asserted to carry different mathematical meanings.')
p.habit('A small r is angular and can look like 2. Here r in n+r and the degree heading has the same form. The isolated raised ticks on P are provisionally primes (medium confidence), not a general rule for later i exponents.')
p.notation('K(A,n)','Angular capital K, sometimes pi-like; coefficients F_p are double-stem F; plain Z in the small sequence.')
p.notation('H decorations','Flat bar on both upper Hs of the suspension square; waved tilde on both lower Hs; no arrowheads on the vertical isomorphism marks.')
p.notation("P_n′, P_{n+1}′",'Raised isolated ticks retained as primes; subscript n+1 includes a long numeral 1.')
p.doubt('struck fragment after sont',r'\deleted{\unsure{el}}','el (perhaps the beginning of a longer abandoned word)','low')
for a,b in [('coh','cohomologie / cohomological, according to context'),('op','opérations'),('deg','degré'),('Ann','Annals'),('p','page')]:p.abbr(a,b)
p.check('136-364-square-degrees','used and rechecked in this run','Both horizontal operations have degree r; suspension adds one to source and target degrees. No proof of representability or the Steenrod presentation is claimed.')
# Supplemental certainty records: existing primary-reader decisions only.
p.extra_decision('crossed fragment after sont', 'undecided', '\\unsure{el}', 'An initial e-shaped loop and a tall loop remain beneath the hatch; no clear t crossbar survives. The fragment is still uncertain.', crop='136_scan364 (865,1380,1595,1545)', confidence='low', original_mark='\\unsure{el|et}', id='X-136_scan364-01')
p.save()
