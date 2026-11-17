from audit_support import revise
revise(38,replacements=[
(r'\unsure{généraliser|linéariser}',r'\unsure{linéariser|généraliser}'),
(r'\inserted{(\unsure{commutatif})}',r'\inserted{(\unsure{evt. commut.|est commut.})}'),
(r'La \unsure{seule}',r'La \unsure{double|seule}'),
(r'C^{*\unsure{!}}',r'C^{*!}'),
(r'\inserted{\unsure{$C^*$}}',r'\inserted{$C^*$ \unsure{avec}}')],
doubts=[('first line','linéariser','généraliser','medium'),('upper-right insertion','evt. commut.','est commut.','low'),('line 5','double','seule','medium'),('last insertion','C* avec','C* followed by uncertain short word','medium')],
notation=[('cochain exponent star plus exclamation',r'C^{*!}','Both enlarged occurrences show the short raised stroke and separate dot of !; compare C* without it at the left of the lower equality.')],
note='Second visual audit with enlarged original-color regions. Recovered the abbreviated qualifier before commut., the short word in the last insertion, and preferred the visible l-initial verb reading. Both C-star-exclamation occurrences were checked for the separated dot rather than normalized as primes; Γ-shaped operations remain distinct from the looped type letter on 032–034.')
