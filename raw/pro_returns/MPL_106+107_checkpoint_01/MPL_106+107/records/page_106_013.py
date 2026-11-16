import sys
sys.path.insert(0,'/workspace/scratch/4bbc351d3cab/MPL_106+107/scripts')
from save_page import save
from page_106_005 import art,zero,letters
tex=r'\texttt{//*\quad DOCUGRA20005\qquad I}'+'\n\n'+art([zero]*4,14)+'\n\n'+art(letters,14)+'\n\n'
line=r'\texttt{****A\quad END\quad JOB\quad 5\quad DOCUGRA2\qquad ROOM\qquad 2.28.52 PM 24 AUG 82\quad R6.PR1\quad SYS JES2\quad JOB\quad 5\quad END\quad A****}'
tex+='\n\n'.join([line]*6)+r"""

\diagram{\begin{tikzcd}[column sep=large,row sep=large]
x\arrow[drr]\arrow[ddr] &&x\arrow[d,hook,shift left=1]\
&&x'\arrow[u,hook,shift left=1]\arrow[dl,shift right=1]\
&x''\arrow[ur,hook,very thick,shift right=1]&
\end{tikzcd}}

\diagram{\begin{tikzcd}
x\arrow[dr]&x\arrow[d,"\sim"]\\
\deleted{x}\arrow[r,phantom,"\deleted{\unsure{\longrightarrow}}" description]&\bar x
\end{tikzcd}}

\diagram{\begin{tikzcd}
\widetilde C\arrow[r,"\unsure{\Phi|\varphi}"]&W^{-1}C
\end{tikzcd}}

\mspage{12}
"""
tex=tex.replace(']\\\n',']\\\\\n')
elements=[('text','top of print in rotated orientation','//* DOCUGRA20005 I'),('drawing','printed upper banner','four zero-shaped arrangements of printed 0'),('drawing','printed middle banner','DOCUGRA2 formed from repeated characters')]
for i in range(6):elements.append(('text',f'printed job line {i+1}','****A END JOB 5 DOCUGRA2 ROOM 2.28.52 PM 24 AUG 82 R6.PR1 SYS JES2 JOB 5 END A****'))
elements += [('diagram','original lower right; upright after 180-degree rotation','x, x, x prime, x double prime; opposing arrows'),('diagram','original lower right below larger sketch','x to bar x, x to bar x, cancelled x branch'),('diagram','original lower left above number; upright after 180-degree rotation','tilde C to W inverse C, Phi'),('text','original lower left','12')]
notes='''Reused typed DOCUGRA2 job-end sheet (printed timestamp 2.28.52 PM, 24 AUG 82) carrying two informal arrow sketches and the comparison tilde C to W^{-1}C. The handwriting is upside down relative to the original portrait scan. The cancelled branch remains represented. The thick arrow and opposing arrows in the larger sketch are retained; there is no accompanying prose asserting a result. Pencil sheet number 12.'''
if __name__=='__main__':save(106,13,tex,elements,kind='reused_typed',notes=notes)
