from pathlib import Path
from tikz import *
from commit_page import commit
root=Path(__file__).resolve().parents[1]
s='\\scanpage{143}\n'
s+=r'''{\color{gray}\ttfamily
\unsure{CRAY2}\quad\unsure{0025}\quad\unsure{1}
}
'''
# Printed character banners: manually read rows of the reversed show-through.
zero=[
'       00000000      00000000      00000000      00000000',
'     0000000000    0000000000    0000000000    0000000000',
'   00      0000  00      0000  00      0000  00      0000',
'  00     00 00  00     00 00  00     00 00  00     00 00',
' 00    00   00 00    00   00 00    00   00 00    00   00',
'00   00     0000   00     0000   00     0000   00     00',
'00 00      00 00 00      00 00 00      00 00 00      00',
'0000      00  0000      00  0000      00  0000      00',
'000      00   000      00   000      00   000      00',
'0000000000    0000000000    0000000000    0000000000',
'00000000      00000000      00000000      00000000']
banner=[
' CCCCCCCCCC   RRRRRRRRRRR   AAAAAAAAAA   YY        YY  2222222222',
'CCCCCCCCCCCC  RRRRRRRRRRRR AAAAAAAAAAAA  YY        YY 222222222222',
'CC            RR       RR AA        AA  YY      YY  22        22',
'CC            RR       RR AA        AA   YY    YY             22',
'CC            RR       RR AA        AA    YY  YY              22',
'CC            RRRRRRRRRRR AAAAAAAAAAAA     YYYY              22',
'CC            RRRRRRRRRR  AAAAAAAAAAAA      YY              22',
'CC            RR    RR    AA        AA      YY             22',
'CC            RR     RR   AA        AA      YY            22',
'CC            RR      RR  AA        AA      YY           22',
'CCCCCCCCCCCC  RR       RR AA        AA      YY          222222222222',
' CCCCCCCCCC   RR        RR AA       AA      YY          222222222222']
s+=r'{\color{gray}\scriptsize\unsure{'+'\n'+r'\begin{tabular}{l}'+'\n'
for row in zero+['']+banner:s+=r'\texttt{'+row.replace(' ',r'\ ')+'}'+r'\\'+'\n'
s+=r'\end{tabular}}}'+'\n'
for i in range(6):
 s+=r'{\color{gray}\ttfamily ****A\quad END\quad JOB\quad25\quad CRAY2\quad ROOM\quad 9.03.23 AM 19 AUG 82\quad\unsure{R6.PR1}\quad SYS JES2\quad JOB\quad25\quad END\quad A****}'+'\\\\\n'
s+=start()+comment('Upper-left frame with opposed written orders.')
s+=paths('k','1.8,2.3 4.5,2.1 7.9,1.96;1.8,2.3 1.9,4.6 2.1,6.3 2.25,7.65;1.75,2.5 2.0,5.2 2.2,7.6;8.03,1.96 8.18,4.05 8.25,6.0 8.1,7.7;1.9,4.6 4.5,4.35 8.18,4.05;2.1,6.3 4.8,6.0 8.16,5.9;2.3,7.75 5.2,7.65 8.48,7.48')
s+=paths('k,->','1.32,2.4 1.35,3.2;8.4,1.7 8.85,1.65',False)
for xy,t in [('2.6,1.83','A'),('3.35,1.83','B'),('4.15,1.7','C'),('4.65,1.83','D'),('5.35,1.7','E'),('5.9,1.73','F'),('6.6,1.7','G'),('7.4,1.65','H'),('2.8,8.15','H'),('3.4,8.12','G'),('4.0,8.08','F'),('4.55,8.03','E'),('5.35,8.03','D'),('6.0,7.98','C'),('6.85,7.98','B'),('7.68,7.95','A')]:s+=labels([(xy,t)])
s+=paths('k','2.65,2.18 2.65,2.35;3.34,2.12 3.34,2.28;3.9,2.1 3.9,2.25;4.55,2.05 4.55,2.22;5.15,2.04 5.15,2.2;5.8,2.0 5.8,2.18;6.56,2.0 6.56,2.2;7.3,1.98 7.3,2.18;2.8,7.68 2.8,7.9;3.5,7.6 3.5,7.82;4.1,7.59 4.1,7.8;4.6,7.56 4.6,7.75;5.35,7.55 5.35,7.75;6.15,7.52 6.15,7.7;6.85,7.5 6.85,7.67;7.6,7.48 7.6,7.65',False)
s+=comment('Large upper-right numbered grid with strands and arrows.')
ys=[2.3,3.1,3.8,4.65,5.45,6.03,6.75,7.4,8.15,8.6,9.2]
for j,y in enumerate(ys):
 s+=path('p','14.4,'+str(y)+' 24.1,'+str(y-.1),False)
 s+=labels([(f'{23.15+j*.035},{y-.02}',str(j+1))])
 if j<9:s+=labels([(f'14.8,{(y+ys[j+1])/2}',str(j+1)+"'")])
s+=paths('k','14.45,2.3 14.32,9.15;22.88,2.17 22.92,9.2;15.47,2.3 15.52,4.65 15.5,5.5 15.6,6.7 15.5,8.6 15.0,9.23;15.5,8.6 15.9,9.23;16.53,2.3 16.56,5.35 16.7,5.9 17.25,6.45 18.9,7.3 19.85,7.85 20.9,8.4 21.35,9.15;17.4,2.3 17.45,4.6 18.1,5.3 18.5,5.9 18.9,7.3 17.7,8.0 18.7,8.6 19.1,9.15;18.5,2.3 19.17,2.97 20.15,3.85 20.58,4.6 20.55,7.15 19.85,7.85 18.7,8.6 18.35,9.15;19.68,2.3 19.17,2.97 18.65,3.8 19.2,4.6 19.45,5.25 19.4,6.6 18.9,7.3 17.7,8.0 17.0,8.6 16.9,9.15;20.65,2.3 21.2,2.9 21.95,3.85 22.08,4.5 22.05,7.65 20.9,8.4 20.5,9.15;21.8,2.2 21.2,2.9 20.15,3.85 19.2,4.6 18.1,5.3 16.7,5.9 15.6,6.7 15.5,8.6')
s+=paths('k,line width=2.6pt','20.65,2.3 21.2,2.9;16.7,5.9 15.6,6.7 15.5,8.6;16.7,7.4 17.25,6.45 18.5,5.9;17.25,6.45 18.2,6.85 18.9,7.3')
s+=dots('k','15.47,2.3 16.53,2.3 17.4,2.3 18.5,2.3 19.17,2.97 21.2,2.9 21.8,2.2 20.15,3.85 19.2,4.6 18.1,5.3 16.7,5.9 17.25,6.45 15.6,6.7 18.9,7.3 19.85,7.85 20.9,8.4 18.7,8.6','.065')
s+=r'\draw[k,fill=white] (17.7,8.0) circle (.07);'+'\n'
s+=paths('k,->','18.6,2.55 18.5,2.4;19.75,2.9 19.7,2.42;20.75,3.3 20.28,3.75;19.65,3.35 20.0,3.75;19.7,4.2 19.3,4.55;18.65,5.05 18.2,5.3;17.4,5.75 16.85,5.9;16.1,6.4 15.65,6.65;16.9,6.1 17.2,6.4;18.3,6.95 18.8,7.25;18.3,7.7 17.85,7.98;19.4,7.6 19.78,7.82;20.35,8.15 20.8,8.38;19.35,8.2 18.85,8.55;18.2,8.35 18.62,8.57;18.4,8.9 18.35,9.15;18.9,8.85 19.1,9.15;20.65,8.8 20.5,9.15;21.15,8.8 21.35,9.15',False)
s+=paths('k,thin','16.55,6.12 16.7,6.3 16.42,6.48 16.72,6.55 16.4,6.7 16.65,6.85 16.35,7.0 16.63,7.1 16.42,7.24;16.68,6.35 16.48,6.62 16.72,6.75 16.5,6.9 16.75,7.05 16.52,7.24;18.45,5.98 18.3,6.16 18.5,6.24 18.28,6.36 18.55,6.42 18.35,6.55 18.6,6.63 18.4,6.75 18.68,6.84 18.5,6.98 18.78,7.08;16.6,6.85 17.05,7.1 17.6,6.86 18.2,6.77 18.9,7.3;16.7,7.1 16.95,6.95 17.1,7.15 17.33,6.95 17.3,7.2 17.55,7.02 17.8,7.08 18.15,6.93;15.5,7.07 15.78,7.15 15.38,7.35 15.75,7.4;15.38,7.9 15.7,8.0 15.35,8.13 15.7,8.2',False)
s+=labels([(f'{x},1.73',t) for x,t in [(15.55,'A'),(16.5,'B'),(17.4,'C'),(18.5,'D'),(19.7,'E'),(20.7,'F'),(21.8,'G')]])
s+=labels([(f'{x},9.7',t) for x,t in [(15.0,'G'),(15.9,'A'),(16.95,'E'),(18.4,'D'),(19.15,'C'),(20.5,'F'),(21.4,'B')]])
s+=comment('Middle-left lens with zigzag strands.')
s+=paths('k,thin','1.25,9.98 3.05,9.58 5.3,9.38 6.68,9.35 7.8,9.35 8.55,9.6;1.25,9.98 2.58,10.38 3.5,10.4 4.5,10.3 6.3,10.05 8.55,9.6;2.1,9.6 2.0,10.43;2.58,10.38 3.05,9.58 3.5,10.4 4.05,9.48 4.5,10.3;5.3,9.38 5.32,9.95 5.45,10.22;6.3,10.05 6.68,9.35 7.05,9.9;7.3,9.35 7.5,9.77 7.8,9.35')
s+=dots('k','3.05,9.58 3.5,10.4 4.05,9.48 4.5,10.3 6.68,9.35 7.5,9.77')
s+=comment('Lower-left elementary crossing sketch.')
s+=paths('k','1.45,12.95 4.47,12.95 7.7,12.94;1.52,14.12 4.0,14.22 6.35,14.25;2.53,12.62 2.55,14.68;6.85,12.5 6.83,14.95;6.85,12.5 6.98,12.65;3.95,12.0 4.47,12.95 5.4,14.3 5.85,15.25;5.08,12.0 4.47,12.95 3.18,14.95;4.47,12.95 5.25,13.9 5.73,15.02')
s+=dots('k','4.47,12.95','.07')
s+=paths('p,->','7.1,14.0 7.02,14.6',False)+path('k','7.45,14.16 7.78,14.18',False)
s+=comment('Middle lower partial strand drawing.')
s+=paths('p','10.3,11.4 15.5,11.33 15.58,11.8 10.3,11.85;10.3,12.45 15.6,12.15;10.3,13.05 15.6,12.8',False)
s+=paths('k','10.78,11.4 10.8,12.2 10.75,13.5;11.28,11.4 11.35,13.5;11.78,11.4 11.73,12.9 12.15,13.5 13.15,12.4 14.1,11.3;12.25,11.3 12.58,11.78 13.15,12.4 13.55,13.1 13.73,13.55;12.85,11.3 12.58,11.78 12.25,12.45 12.65,12.85 13.05,13.5;13.4,11.3 13.75,11.77 14.15,12.4 14.22,13.5',False)
s+=paths('k,line width=2pt','12.58,11.78 12.25,12.45 12.65,12.85 13.15,12.4',False)
s+=comment('Two elliptical rims with written circular orders, joined as a cylinder.')
s+=paths('k,thin','13.3,14.5 12.6,14.32 10.8,14.4 9.5,15.0 9.5,15.65 10.4,16.1 12.5,16.4 14.4,16.15 14.95,15.68 14.7,15.1 13.7,14.7;9.5,15.65 9.44,17.9;14.95,15.68 14.9,17.72;9.44,17.9 10.95,18.55 12.3,18.7 14.4,18.5 14.9,17.72;9.5,17.65 10.7,17.3 12.0,17.1 13.9,17.3 14.9,17.72')
s+=paths('k','10.4,16.05 10.4,16.2;12.47,16.3 12.47,16.45;14.4,16.07 14.43,16.24;13.95,14.76 14.0,14.92;11.65,14.24 11.67,14.45;10.32,14.35 10.4,14.52;9.7,14.88 9.85,14.97;9.55,17.95 9.7,18.08;10.95,18.45 10.95,18.65;12.25,18.65 12.28,18.75;14.4,18.45 14.3,18.65;13.9,17.25 13.9,17.4;12.0,17.04 12.0,17.2;10.3,17.32 10.15,17.38',False)
s+=labels([('10.25,16.45','A'),('12.5,16.8','B'),('14.5,16.6','C'),('14.45,14.8','D'),('11.8,14.0','E'),('10.4,14.0','F'),('9.55,14.4','G'),('9.3,18.45','C'),('10.65,19.0','B'),('12.65,18.95','A'),('14.7,18.7','G'),('13.6,17.7','F'),('12.25,17.45','E'),('10.9,17.45','D')])
s+=comment('Lower-right grid: visible initial portions and diagonal staircase.')
ys2=[11.92,12.55,13.15,13.75,14.3,14.92,15.5,16.1,16.65,17.23,17.85]
for j,y in enumerate(ys2):
 s+=path('p',f'18.85,{y} 24.85,{y+.03}',False)
 s+=labels([(f'25.25,{y+.02}',str(j+1))])
for x in [18.85,19.65,20.4,21.2,21.95,22.7,23.45,24.1,24.85]:s+=path('p',f'{x},11.92 {x-.1},17.85',False)
s+=paths('k','19.68,11.92 19.63,14.3 19.55,15.5 19.65,17.85;20.38,11.92 20.4,13.2 20.3,14.92 20.35,16.7;21.22,11.92 21.2,14.3 21.1,14.92 20.35,15.5 21.0,16.1;21.95,11.92 21.95,12.55 22.7,13.15 22.65,13.75;22.7,11.92 21.95,12.55 21.92,13.75;23.45,11.92 23.4,13.75;24.1,11.92 23.45,12.55 22.7,13.15 21.92,13.75 21.2,14.3 20.3,14.92 19.55,15.5;19.55,15.5 19.55,17.23 20.3,17.85',False)
s+=paths('k,line width=2pt','19.55,15.5 19.55,17.23;20.35,15.5 20.35,16.65;21.22,11.92 21.22,13.5',False)
for xy in ['19.55,15.5','19.55,16.1','19.55,17.23']:s+='\\draw[k,fill=white] ('+xy+') circle (.065);\n'
s+=labels([(f'{x},11.55',t) for x,t in [(19.75,'A'),(20.4,'B'),(21.2,'C'),(21.95,'D'),(22.75,'E'),(23.45,'F'),(24.15,'G')]])
s+=labels([('19.6,18.25',r'\unsure{G}'),('20.35,18.25','A')])+end()
# Arrow diagram, encoded separately in tikz-cd; empty cells are actual unlabelled joins.
nodes={(1,5):'D',(1,7):'E',(1,9):'F',(1,11):'G',(2,6):r'\bullet',(2,10):r'\bullet'}
edges=[((1,5),(2,6)),((1,7),(2,6)),((1,9),(2,10)),((1,11),(2,10)),((2,6),(3,8)),((2,10),(3,8)),((3,8),(4,7)),((4,7),(5,6)),((5,6),(6,5)),((6,5),(7,4)),((6,5),(7,6)),((7,4),(8,4)),((8,4),(9,4)),((9,4),(10,4)),((10,4),(11,3)),((10,4),(11,5)),((7,6),(8,7)),((8,7),(9,6)),((8,7),(9,8)),((9,6),(10,7)),((9,8),(10,7)),((9,8),(10,9)),((10,7),(11,6)),((10,7),(11,8)),((10,9),(11,8)),((10,9),(11,10))]
s+=r'\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=.4em,row sep=.8em]'+'\n'
for row in range(1,12):
 cells=[]
 for col in range(1,12):
  cell=nodes.get((row,col),'{}')
  for a,b in edges:
   if a==(row,col):
    dr,dc=b[0]-row,b[1]-col
    direction=('d'*dr if dr>=0 else 'u'*(-dr))+('r'*dc if dc>=0 else 'l'*(-dc))
    cell+='\\arrow['+direction+']'
  cells.append(cell)
 s+=' \\& '.join(cells)+(r'\\' if row<11 else '')+'\n'
s+=r'\end{tikzcd}}'+'\n'+r'\margin{142}'+'\n'
(root/'pages/MPL_154_127-176_154_scan143.tex').write_text(s)
commit(143,[('text','reversed show-through lower half','CRAY2; 0025; character banners'),('text','six reversed printed rows','END JOB 25 CRAY2 ROOM 9.03.23 AM 19 AUG 82 R6.PR1 SYS JES2'),('drawing','upper left','frame; A B C D E F G H; H G F E D C B A'),('drawing','upper right','grid A B C D E F G; rows 1–11; primed intervals'),('diagram','centre descending','D E F G; converging arrows; branching unlabelled chain'),('drawing','middle left','lens with zigzag strands'),('drawing','lower left','crossing with two horizontals'),('drawing','lower middle','partial strand drawing'),('drawing','lower middle cylinder','A B C D E F G on two elliptical rims'),('drawing','lower right','grid A B C D E F G; 1–11; staircase'),('margin note','bottom left','142')],observations='Read whole and halves, plus vertically reflected printing and an enlargement of the arrow tree. The printed banner is made of repeated characters; its complete manually keyed rows are marked collectively uncertain because of overlay and faintness. Six repeated job-end rows are retained individually, not summarized. Right grid endpoint orders are copied as written. Overdrawn central grid strokes and hatched patches were traced without resolving them into a cleaner braid. Unlabelled arrow joins are unlabelled in tikz-cd; only the two visibly filled initial joins carry bullets. Drawing coordinates and spacing approximate the visible placement.')
