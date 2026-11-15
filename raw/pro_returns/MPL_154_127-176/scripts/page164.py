from pathlib import Path
from tikz import *
from commit_page import commit
root=Path(__file__).resolve().parents[1]
s=r'''\scanpage{164}
{\scriptsize\ttfamily\begin{tabular}{lllll}
1 & //CRAY2 JOB '\unsure{********}, & ',' & ', & JOB 0411\\
 & // MSGLEVEL=(1,1) & & &\\
2 & // EXEC PGM=IEFBR14 & & &
\end{tabular}}
'''+start()
s+=path('g,line width=1.6pt','4.71,10.73 6.2,8.72 7.83,7.24 9.09,6.5 11.06,5.65 12.4,5.3 14.49,5.28 16.12,5.78 17.33,6.84 17.87,8.28 17.87,9.75 17.29,11.32 16.23,12.23 14.84,12.72 13.48,12.59 12.19,11.88 10.85,10.64 9.99,9.21 9.46,7.7 9.09,6.5 8.85,4.69 8.79,2.42')
s+=path('g,line width=1.6pt','5.29,13.35 6.72,11.52 8.21,10.15 9.99,9.21 11.09,8.9 12.4,8.85 14.68,9.27 17.87,9.75 19.8,9.71 20.93,9.06 21.2,8.02 20.9,6.25 20.42,4.86 19.7,3.62 18.31,1.48')
s+=path('yellow!70!brown,line width=1.5pt','7.14,15.58 8.91,13.24 10.85,10.64 12.4,8.85 14.41,7.12 16.12,5.78 17.79,4.72 19.7,3.62 21.81,2.75')
s+=paths('g,thin','7.99,14.26 8.39,14.12 9.09,13.08;4.71,10.73 6.2,8.72 7.83,7.24 9.09,6.5')
s+=paths('b,line width=2.8pt','4.63,10.52 4.86,10.12;5.44,13.33 5.8,12.94;7.09,15.3 7.57,14.69;8.72,2.48 8.73,3.08;18.45,1.52 18.69,1.84;21.2,2.84 21.75,2.65;8.95,6.31 8.91,6.47 9.07,6.51;15.99,5.63 16.2,5.64 16.3,5.73;12.22,8.88 12.29,9.04;17.99,9.79 17.84,9.94;10.76,10.42 10.74,10.59;10.0,9.13 10.1,9.26')
s+=paths('k,->','9.12,6.49 9.01,5.96;9.12,6.49 8.58,6.79;16.1,5.76 15.61,5.57;16.14,5.77 16.62,5.53;19.7,3.62 19.55,3.22;19.7,3.62 20.12,3.48;17.87,9.75 18.41,9.75;17.87,9.75 17.68,10.28;12.4,8.85 11.95,8.85;12.4,8.85 12.15,9.25;9.99,9.21 9.63,9.33;9.99,9.21 10.2,9.52;10.85,10.64 10.66,10.14;10.85,10.64 10.56,10.96')
s+=labels([('12.41,5.17','+'),('17.87,4.76','+'),('20.93,8.49','+'),('15.43,12.43','+'),('11.47,9.99','+'),('10.98,8.91','+'),('9.48,7.82','-'),('14.04,7.4','-'),('18.0,7.79','-'),('14.94,9.32','-'),('10.42,9.84','-')])+end()+r'\margin{163}'+'\n'
(root/'pages/MPL_154_127-176_154_scan164.tex').write_text(s)
commit(164,[('text','top printed','CRAY2 JOB0411; MSGLEVEL; EXEC PGM=IEFBR14'),('drawing','whole upper-middle','three oriented yellow-green curves; eleven signs; blue caps'),('margin note','bottom left','163')],sheet_kind='reused_typed',observations='Whole and both halves read. Single large drawing traced as three continuous curves with seven crossings, paired direction arrows, six plus and five minus signs, blue endpoint and crossing marks, and thin retraced lower-left segment. Printed header grouping and blank quote fields retained; count of asterisks marked uncertain.')
