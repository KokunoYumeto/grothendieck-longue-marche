import sys
sys.path.insert(0,'/workspace/scratch/4bbc351d3cab/MPL_106+107/scripts')
from save_page import save
tex=r"""
\unsure{Formalisme} des

$X\otimes M$, $X^M$, $\underline{\operatorname{Hom}}_A$, $\underline{\operatorname{Hom}}_B$

\unsure{relatifs|relatif} : une rédaction \uline{provisoire}

\texttt{PAGE\qquad 4}

\texttt{ASM 0201 15.27 06/04/82}

\figure{\begin{tikzpicture}[x=.018cm,y=.018cm]
\draw[->] (0,0)--(-105,-155);
\draw (70,-10)--(0,-122);
\draw (130,3)--(70,-100);
\draw (200,-5)..controls(205,-45)and(180,-83)..(170,-110);
\end{tikzpicture}}

\mspage{1}
"""
elements=[('text','upper right heading','Formalisme des'),('display','upper right second line','X tensor M, X power M, underlined Hom A and Hom B'),('text','upper right third and fourth lines','relatifs : une rédaction provisoire'),('text','printed below title','PAGE 4'),('text','printed below title','ASM 0201 15.27 06/04/82'),('drawing','over and below printed header','four diagonal strokes, left one arrowheaded'),('text','foot','1')]
notes='''Title sheet on reused computer paper: “Formalisme des X⊗M, X^M, Hom_A, Hom_B relatifs : une rédaction provisoire” (the first word and ending of relatifs are marked doubtful). “provisoire” is underlined. The printed PAGE 4 and ASM 0201 15.27 06/04/82 belong to the reused paper; the pencil sheet number is 1. The title carries no explicit count of manuscript pages. This heading must be recorded separately from the supplied catalogue title of cote 107.'''
if __name__=='__main__':save(107,2,tex,elements,kind='cover',notes=notes)
