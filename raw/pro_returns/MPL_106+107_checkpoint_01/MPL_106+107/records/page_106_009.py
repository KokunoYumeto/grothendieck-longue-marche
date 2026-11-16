from page_106_005 import art
from page_106_007 import letters as tail
import sys
sys.path.insert(0,'/workspace/scratch/4bbc351d3cab/MPL_106+107/scripts')
from save_page import save
letters=[[first]+rows for first,rows in zip(['PPPPPPPPPPP','LL','OOOOOOOOOOOO','TTTTTTTTTTTT','EEEEEEEEEEEE','DDDDDDDDD','IIIIIIIIII','TTTTTTTTTTTT'],tail)]
tex=art(letters,14)+r"""
\margin{\unsure{P|9}}
"""
line=r'\texttt{****A\quad START\quad JOB 7747\quad PLOTEDIT\qquad ROOM\qquad 8.39.24 AM 25 AUG 82\quad R6.PR1\quad SYS JES2\quad JOB 7747\quad START\quad A****}'
tex+='\n\n'.join([line]*6)+r"""

\texttt{DERNIERE MISE A JOUR DE JOURNAL : 11-08-82}

\diagram{\begin{array}{ll|ll}
\text{CRAY 1}&579/1&\unsure{849}&\text{CRAY 1}\\
\text{GRAPHI1}&2&&
\end{array}}

\texttt{TRACEUR I\quad BUFFER 1020\quad BANDE 9 PISTES\quad PLUMES : 3\quad XMAX = 10100.0\quad YMAX = 30.0\quad STNB = 100.00000}

\texttt{25/ 8/ 82\qquad 8 HEURES 37 MINUTES}

\diagram{\begin{array}{lll}
\texttt{JOB}&\texttt{BANDE IBM NUMERO}&\texttt{TRACEUR UTILISE}\\
&\texttt{****************************************}&\texttt{REMISE DE LA BANDE}\\
&&\texttt{DEBUT DE TRAITEMENT}\\
&&\texttt{FIN DE TRAITEMENT}\\
&&\texttt{REMISE DES GRAPH.}\\
&&\texttt{INCIDENTS SURVENUS}
\end{array}}

\diagram{\begin{array}{lllllllll}
\texttt{PLOT 3C}&&\texttt{CALQUE}&&&&0&0&\\
\texttt{CNU*0579 GRAPHI1}&&&\texttt{I.C}&82237&083702&0&0&\\
\texttt{GRAPHI1}&\texttt{CNU*0579}&82237&\texttt{M06}&\texttt{P02900500}&7\quad0&0&0&3
\end{array}}
\mspage{8}
"""
elements=[('drawing','top after rotation','PLOTEDIT, character banner'),('margin note','between banner and job records','P or 9')]
for i in range(6):elements.append(('text',f'printed job line {i+1}','****A START JOB 7747 PLOTEDIT ROOM 8.39.24 AM 25 AUG 82 R6.PR1 SYS JES2 JOB 7747 START A****'))
elements += [('text','below job records','DERNIERE MISE A JOUR DE JOURNAL : 11-08-82'),('diagram','handwritten two-row table','CRAY 1 579/1 | 849 CRAY 1; GRAPHI1 2'),('text','lower band','TRACEUR I BUFFER 1020 BANDE 9 PISTES'),('text','above job form','25/ 8/ 82 8 HEURES 37 MINUTES'),('diagram','job form','JOB BANDE IBM NUMERO TRACEUR UTILISE'),('diagram','bottom printed records','PLOT 3C CALQUE; CNU*0579 GRAPHI1'),('text','original lower left','8')]
notes='''Reused PLOTEDIT start-job sheet, six records timestamped 8.39.24 AM 25 AUG 82, plus operational plotter records and a handwritten CRAY/GRAPHI1 table. No mathematical claim. Sheet number 8; a separate looped mark between banner and records could be P or 9. The hardware/job date should not be turned into a date of the mathematics.'''
if __name__=='__main__':save(106,9,tex,elements,kind='reused_typed',notes=notes)
