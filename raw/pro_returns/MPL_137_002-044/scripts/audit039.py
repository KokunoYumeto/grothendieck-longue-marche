from audit_support import revise
revise(39,replacements=[
(r'$k$ principal en $1^\circ$',r'$k$ principal en \unsure{le|cas} $1^\circ$'),
(r'\unsure{fainéantise|générateurs} et \unsure{platitudes|relations}',r'\unsure{fainéantise} et \unsure{platonisme|platitudes}')],
doubts=[('line 4 before 1°','le','cas','low'),('last parenthesis','fainéantise et platonisme','platitudes for second word','medium')],
note='Second visual audit of all written lines, enlarged bands and original-color final words. Recovered a short word before 1°. The final p-l-a-t-o-n-i-s-m-e-like sequence supports platonisme rather than the earlier platitudes/relations candidates; all remaining uncertainty stays explicit. The reconstruction question and its preceding De Rham comparison were checked separately.')
