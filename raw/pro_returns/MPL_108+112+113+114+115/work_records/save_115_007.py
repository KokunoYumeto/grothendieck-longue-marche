from record import save_page
positions=[[(12,8)],[(10,10)],[(8,2),(16,4)],[(7,2),(14,2),(17,2)],[(6,2),(12,2),(16,2)],[(5,2),(10,2),(15,2)],[(4,2),(8,2),(14,2)],[(3,2),(6,2),(13,2)],[(2,4),(12,2)],[(1,3),(11,2)],[(1,10)],[(1,8)]]
zeros=[]
for row in positions:
 line=[' ']*62
 for offset in (0,14,28,42):
  for start,n in row:
   for k in range(n):line[offset+start-1+k]='0'
 zeros.append(''.join(line).rstrip())
P=['PPPPPPPPPPP ','PPPPPPPPPPPP']+['PP        PP']*3+['PPPPPPPPPPPP','PPPPPPPPPPP ']+['PP          ']*5
R=['RRRRRRRRRRR ','RRRRRRRRRRRR']+['RR        RR']*3+['RRRRRRRRRRRR','RRRRRRRRRRR ','RR    RR    ','RR     RR   ','RR      RR  ','RR       RR ','RR        RR']
E=['EEEEEEEEEEEE']*2+['EE          ']*3+['EEEEEEEE    ']*2+['EE          ']*3+['EEEEEEEEEEEE']*2
D=['DDDDDDDDD   ','DDDDDDDDDD  ','DD       DD ']+['DD        DD']*6+['DD       DD ','DDDDDDDDDD  ','DDDDDDDDD   ']
O=['OOOOOOOOOOOO']*2+['OO        OO']*8+['OOOOOOOOOOOO']*2
N=['NN        NN','NNN       NN','NNNN      NN','NN NN     NN','NN  NN    NN','NN   NN   NN','NN    NN  NN','NN     NN NN','NN      NNNN','NN       NNN','NN        NN','NN         N']
T=['TTTTTTTTTTTT']*2+['     TT     ']*10
A=[' AAAAAAAAAA ','AAAAAAAAAAAA']+['AA        AA']*3+['AAAAAAAAAAAA']*2+['AA        AA']*5
name=['  '.join(r).rstrip() for r in zip(P,R,E,D,O,N,T,A)]
def banner(rows):
 return '\\diagram{\\begin{array}{l}\n'+(' \\\\\n'.join(r'\texttt{'+r.replace(' ',r'\ ')+'}' for r in rows))+'\n\\end{array}}\n'
tex='\\scanpage{7}\n% archive foliation: 6\n'+banner(zeros)
tex+=r'''
\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw[thin](-2,0.3)--(-2.1,-.3)--(-1.75,-.25);
\draw[->,thick](-.7,.15)--(-.2,.15);
\node at (.1,.2){\texttt{//}};
\draw[thick](.4,-.05)--(1.1,-.05)--(1.25,.7)--(.5,.65)--cycle;
\node at (.8,.3){$A$};\node at (2,.3){\texttt{JOB.}};
\draw[gray,thin](.55,.25) ellipse(.75 and .45);
\node at (.8,-.6){\texttt{/*}\unsure{IN|JN}$=$};
\draw[thick](1.6,-1.05)--(2.25,-1.05)--(2.4,-.25)--(1.8,-.25)--cycle;
\draw[thin](1.67,-.98)--(2.19,-.98)--(2.32,-.31)--(1.83,-.31)--cycle;
\node at (2,-.65){$B$};\draw[gray,thin](2,-.65) ellipse(.6 and .52);
\node at (.05,-1.4){\texttt{//}};\node at (.65,-1.4){$C$};\node at (2,-1.4){\texttt{JOB.}};
\draw[thick](.65,-1.4) ellipse(.45 and .25);
\draw[thin](.35,-1.15)--(1.65,-1.2)--(1.4,-1.6)--(.2,-1.65)--cycle;
\draw[->,thin](1.9,-1.05)--(.9,-1.18);
\draw[thin](.25,-1.9)--(.25,-2.05);
\node at (.2,-2.45){\texttt{/}};
\draw[thick](.45,-2.8)--(1.15,-2.8)--(1.32,-2.1)--(.6,-2.1)--cycle;
\node at (.88,-2.45){$D$};\node at (1.35,-2.5){.};
\draw[gray,thin](.85,-2.45) ellipse(.65 and .45);
\end{tikzpicture}}
'''
tex+=banner(name)
record=r'\texttt{****A START JOB 653 PREDONTA ROOM 11.23.37 AM 02 JUN 82 R6.PR1 SYS JES2 JOB 653 START A****}'
tex+='\n\n'.join([record]*6)+'\n\n'+r'\texttt{DERNIERE MISE A JOUR DE JOURNAL: 24-05-82}'
save_page(115,7,tex,[('diagram','printed upper banner','0000 in twelve rows'),('drawing','handwritten upper right','// A JOB.; /* IN = B; // C JOB.; / D.'),('diagram','printed middle banner','PREDONTA in twelve rows')]+[('text',f'printed record {n}','****A START JOB 653 PREDONTA') for n in range(1,7)]+[('text','printed footer','DERNIERE MISE A JOUR DE JOURNAL: 24-05-82')],'reused_typed',doubts=[('handwritten job schematic','/* IN = B','/* JN = B','medium'),('numeric banner','0000 with slanted zero characters','precise count in row 10 left edge uncertain','medium'),('banner','PREDONTA','individual faint E/P/R strokes and spacing','medium')],notes='Printer routing banner 0000, PREDONTA banner and six START JOB 653 records, 02 JUN 82, footer 24-05-82. Four boxed/circled handwritten job identifiers A–D, with connecting line and slash/star syntax, also transcribed as a drawing. No subject-matter prose.')
