import sys
sys.path.insert(0,'/workspace/scratch/4bbc351d3cab/MPL_106+107/scripts')
from save_page import save
from page_106_005 import art,letters as old
P=['PPPPPPPPPPP','PPPPPPPPPPPP']+['PP        PP']*3+['PPPPPPPPPPPP','PPPPPPPPPPP']+['PP']*5
H=['HH        HH']*5+['HHHHHHHHHHHH']*2+['HH        HH']*5
I=['IIIIIIIIII']*2+['    II']*8+['IIIIIIIIII']*2
letters=[old[4],old[5],old[6],P,H,I,old[7]]
tex=r'\texttt{//*\quad GRAPHI2\quad 0421\quad -\quad CRAYI}'+'\n\n'+art(letters,14)+'\n\n'
line=r'\texttt{****A\quad END\quad JOB\quad 421\quad GRAPHI2\quad -\quad CRAY OUTPUT\quad -\qquad ROOM\qquad 3.04.20 PM 25 AUG 82\quad R6.PR1\quad SYS JES2\quad JOB\quad 421\quad END\quad A****}'
tex+='\n\n'.join([line]*6)+r"""

\diagram{\begin{tikzcd}[column sep=large,row sep=large]
x\arrow[dr,hook]&&y&\\
&&y'\arrow[u]&y''\arrow[ul]\\
x\amalg x\arrow[rr,hook]\arrow[dr]&&y'\amalg y''\arrow[u]\arrow[d,no head]\arrow[r,leftrightarrow]&\deleted{\unsure{y}}\\
&x\arrow[r,hook]&\unsure{p|\rho}\arrow[r,hook,two heads]&y
\end{tikzcd}}

\diagram{\begin{tikzcd}[column sep=large,row sep=large]
&x\arrow[r,hook]\arrow[d,"i_1"']&y'\arrow[d]\arrow[dl,phantom,"\text{cocart}" description]\\
\deleted{\unsure{y}}\inserted{x}\arrow[r,"i_2"]\arrow[d,hook]&x\amalg x\arrow[r,hook]\arrow[d,hook]&\unsure{y'|x'}\amalg x\arrow[d,hook]\\
y''\arrow[r]&x\amalg y''\arrow[r,hook]&y'\unsure{\amalg}y''
\end{tikzcd}}

\mspage{14}
"""
tex=tex.replace('x\\arrow[dr,hook]&&y&','x\\arrow[drr,hook]&&y&')
elements=[('text','rotated printed header','//* GRAPHI2 0421 - CRAYI'),('drawing','printed banner','GRAPHI2 formed from repeated characters')]
for i in range(6):elements.append(('text',f'printed job line {i+1}','****A END JOB 421 GRAPHI2 - CRAY OUTPUT - ROOM 3.04.20 PM 25 AUG 82 R6.PR1 SYS JES2 JOB 421 END A****'))
elements += [('diagram','original lower right upper group','x, y, y prime, y double prime; coproduct and p'),('diagram','original lower right lower group','x y prime; x coproduct x; y double prime; cocart'),('text','original lower left','14')]
notes='''A reused GRAPHI2 CRAY job-end sheet carrying two connected groups of diagrams about coproducts and common factorizations. Printed timestamp 3.04.20 PM, 25 AUG 82. No mathematical prose beyond “cocart” in the lower diagram. Small arrowheads, overdrawn coproduct signs and the central object p/rho are uncertain. Sheet number 14.'''
if __name__=='__main__':save(106,15,tex,elements,kind='reused_typed',notes=notes)
