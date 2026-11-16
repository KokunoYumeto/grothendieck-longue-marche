import sys
sys.path.insert(0,'/workspace/scratch/4bbc351d3cab/MPL_106+107/scripts')
from save_page import save
tex=r"""
\texttt{PAGE 1}\qquad\texttt{ON=CELMPQRSTV}\qquad\texttt{08/25/82-15:01:26}\qquad\texttt{CFT 1.09(06/28/82)}\qquad\texttt{PAGE 1}

\diagram{\begin{array}{rrll}
1&1.& &\texttt{PROGRAM GRAPHI}\\
2&2.& &\texttt{DIMENSION X(10),Y(10)}\\
3&3.& &\texttt{DATA X/0.,0.,4.,9.,1.,2.,0.,0.,1.,0./,}\\
4&&\texttt{S}&\quad\texttt{Y/7.,2.,0.,1.,0.,2.,0.,3.,0.,4./}\\
5&4.& &\texttt{NOL=10}\\
6&5.& &\texttt{XCM=10.}\\
7&6.& &\texttt{YCM=10.}\\
8&7.& &\texttt{N=10}\\
9&8.& &\texttt{WRITE(6,1)}\\
10&9.& &\texttt{CALL TBRAF(NOL,XCM,YCM,0,0,0,0,0,0,0,X,Y,N,0,0.)}\\
11&10.& &\texttt{WRITE(6,2)}\\
12&11.&1&\texttt{FORMAT(' TBRAF VA ETRE APPELE')}\\
13&12.&2&\texttt{FORMAT(' TBRAF A ETE APPELE')}\\
14&13.& &\texttt{STOP}\\
15&14.& &\texttt{END}
\end{array}}

\mspage{16}
"""
elements=[('text','rotated printed header','PAGE 1 ON=CELMPQRSTV 08/25/82-15:01:26 CFT 1.09(06/28/82) PAGE 1'),('display','printed program table','numbered source listing PROGRAM GRAPHI through END')]
for n,t in enumerate(['PROGRAM GRAPHI','DIMENSION X(10),Y(10)','DATA X/0.,0.,4.,9.,1.,2.,0.,0.,1.,0./,','S Y/7.,2.,0.,1.,0.,2.,0.,3.,0.,4./','NOL=10','XCM=10.','YCM=10.','N=10','WRITE(6,1)','CALL TBRAF(NOL,XCM,YCM,0,0,0,0,0,0,0,X,Y,N,0,0.)','WRITE(6,2)',"1 FORMAT(' TBRAF VA ETRE APPELE')","2 FORMAT(' TBRAF A ETE APPELE')",'STOP','END'],1):elements.append(('text',f'printed source line {n}',t))
elements.append(('text','original lower left','16'))
notes='''Printed Fortran compiler source listing headed PROGRAM GRAPHI, dated 08/25/82-15:01:26, CFT 1.09(06/28/82), PAGE 1 at both ends of the header. No mathematical handwriting; pencil sheet number 16. The listing ends STOP/END, which is part of the reused source and does not mark completion of the manuscript argument on scan 016. The CALL has seven zero arguments between YCM and X; the continuation character on line 4 is printed S.'''
if __name__=='__main__':save(106,17,tex,elements,kind='reused_typed',notes=notes)
