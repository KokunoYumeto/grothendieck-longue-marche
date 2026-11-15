from pathlib import Path
from tikz import *
from commit_page import commit
root=Path(__file__).resolve().parents[1]
# The table structure is visually the same printed form as scan 127; its observed values differ.
a=(root/'pages/MPL_154_127-176_154_scan127.tex').read_text()
head=a[a.index('\\begin{center}'):a.index('\\figure{')]
head=head.replace('&104&','&67&').replace('3,936','3,893')
s='\\scanpage{145}\n'+head
s+=r'''\deleted{$A B C D E F G$}\\
\deleted{$A B C E D$} $G F$
'''
# Main labelled arrow tree and its attached orders.
nodes={(1,5):'D',(1,7):'E',(1,9):'F',(1,11):'G',(2,6):'DE',(2,10):'FG',(3,8):'DG',(4,7):'EG',(5,6):r'\unsure{CG}',(6,5):'BG',(7,4):'AG',(10,4):r'\unsure{AG}'}
seq={2:r'ABC\underbrace{DE}\underbrace{FG}',3:r'ABCE\uline{D}\underbrace{GF}',4:r'ABCE\uline{GD}F',5:r'AB\underbrace{CGE}DF',6:r'AB\underbrace{GC}EDF',7:r'A\underbrace{GB}CEDF',8:r'\textcircled{\scriptsize $\unsure{GA}$}\uline{CB}EDF',9:r'\textcircled{\scriptsize $GA$}C\uline{EB}DF',10:r'\textcircled{\scriptsize $GA$}\uline{EC}D\uline{BF}',11:r'GAED\unsure{C}FB'}
for row,t in seq.items():nodes[(row,13)]=t
for row in range(2,11):nodes[(row,15)]=str(row-1)+"'"
edges=[((1,5),(2,6)),((1,7),(2,6)),((1,9),(2,10)),((1,11),(2,10)),((2,6),(3,8)),((2,10),(3,8)),((3,8),(4,7)),((4,7),(5,6)),((5,6),(6,5)),((6,5),(7,4)),((6,5),(7,6)),((7,4),(8,4)),((8,4),(9,4)),((9,4),(10,4)),((10,4),(11,4)),((11,4),(12,3)),((11,4),(12,5)),((7,6),(8,7)),((8,7),(9,6)),((8,7),(9,8)),((9,6),(10,7)),((9,8),(10,7)),((9,8),(10,9)),((10,7),(11,6)),((10,7),(11,8)),((10,9),(11,8)),((10,9),(11,10)),((11,6),(12,5)),((11,6),(12,7)),((11,10),(12,9)),((11,10),(12,11))]
s+=r'\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=.35em,row sep=.9em]'+'\n'
for row in range(1,13):
 cells=[]
 for col in range(1,16):
  cell=nodes.get((row,col),'{}')
  for a,b in edges:
   if a==(row,col):
    dr,dc=b[0]-row,b[1]-col
    d='d'*dr+('r'*dc if dc>=0 else 'l'*(-dc))
    weight=',line width=1.7pt' if row in [8,9,10] and col>4 else ''
    cell+='\\arrow['+d+weight+']'
  if (row,col) in [(2,10),(3,8),(4,7),(5,6),(6,5),(7,6),(8,7),(9,8),(10,9)]:
   cell+='\\arrow['+'r'*(13-col)+',dash]'
  cells.append(cell)
 s+=' \\& '.join(cells)+(r'\\' if row<12 else '')+'\n'
s+=r'\end{tikzcd}}'+'\n'
s+=start()+comment('Pencil separators behind the main orders and dark redrawings of lower arrows.')
s+=paths('p','7.95,8.4 13.0,8.48 17.5,8.58 18.55,8.4;8.6,9.3 12.0,9.5 17.75,9.7;8.2,9.9 11.0,10.4 15.0,10.5 16.95,10.2;7.3,10.62 11.1,11.07 16.9,11.0;6.2,11.28 10.5,11.5 15.65,11.65;6.5,12.0 10.8,12.1 14.3,12.05;6.2,12.65 10.9,12.72 15.1,12.55;6.1,13.13 9.0,13.05 13.4,13.1;6.08,13.75 10.6,13.55 17.1,13.6')
s+=paths('k,line width=2pt','8.35,12.62 8.0,13.02 8.32,13.35;8.35,12.62 8.97,13.02 8.6,13.43;8.97,13.02 9.6,13.52',False)
s+=paths('k,thin','8.0,13.15 8.3,13.0 8.08,13.3 8.35,13.42 8.13,13.55;8.65,13.2 8.96,13.05 8.76,13.38 9.05,13.2;9.1,13.28 9.4,13.1 9.2,13.45 9.55,13.28',False)
s+=comment('Upper-right marked line and small crossing.')
s+=paths('k','22.0,10.15 23.37,9.3 25.0,8.6 27.75,7.9;25.25,9.2 25.5,8.4 25.75,7.8;26.18,8.45 26.5,7.68;26.75,6.78 26.95,7.15 27.25,7.92 27.58,8.55;26.7,7.5 27.1,6.85')
s+=dots('k','23.37,9.3','.08')
s+=comment('Middle-right partial grid and darker diagonal paths.')
ys=[11.12,11.48,11.95,12.45,12.98,13.48,14.0]
for j,y in enumerate(ys):
 s+=path('p',f'22.5,{y} 28.8,{y-.05}',False)
 s+=labels([(f'29.0,{y}',"5'" if j==0 else str(j+5))])
s+=paths('k','23.1,11.1 23.4,11.9 23.7,12.5 24.0,13.1 24.1,13.9;24.08,11.15 23.96,11.5 23.7,12.5 23.35,13.95;24.7,11.15 24.6,11.6 24.48,11.98 24.3,12.5 24.75,12.98 25.3,13.45 25.55,13.95;25.35,11.1 25.35,11.65 25.15,12.4 24.75,12.98 24.5,13.4 24.4,13.92;26.1,11.1 26.0,12.0 25.98,12.9 25.3,13.45 25.0,13.95;27.05,11.1 26.9,12.0 26.6,13.4 26.95,13.93;23.7,12.5 24.48,11.98 25.15,12.4 25.98,12.9 26.6,13.4 26.3,13.92',False)
s+=paths('k,dashed','22.1,12.5 23.7,12.5 25.15,12.4 27.5,12.4;24.5,11.98 26.6,11.85 27.5,11.8;24.75,12.98 26.6,12.95 27.8,12.96;24.4,13.45 25.3,13.45 27.65,13.45',False)
s+=paths('w,->','25.15,12.4 24.8,12.92;25.15,12.4 25.85,12.86;24.75,12.98 25.22,13.42;25.98,12.9 25.38,13.42',False)
s+=dots('k','23.96,11.5 23.7,12.5 24.48,11.98 25.15,12.4 24.75,12.98 25.98,12.9 25.3,13.45 26.6,13.4 23.35,13.95 24.1,13.9 24.4,13.92 25.55,13.95 26.3,13.92 26.95,13.93','.055')
s+=paths('k','23.4,12.4 23.98,12.32;23.7,12.5 24.25,12.8;23.7,12.5 24.18,13.1',False)
s+=comment('Bottom middle pencil crossing arrangement.')
s+=paths('p','9.35,15.85 14.3,15.6;9.35,16.95 13.85,16.65;9.2,18.13 14.8,17.68;9.65,16.3 10.55,17.95 11.3,19.45;10.62,15.35 10.88,15.78 11.55,16.72 12.45,17.78 13.25,18.7;12.85,15.22 12.4,15.72 11.55,16.72 10.55,17.95 10.12,18.68;14.7,14.7 13.7,16.05 12.45,17.78 12.0,18.6;9.0,17.3 10.88,15.78 11.25,15.5;12.4,15.72 14.3,16.45')
s+=dots('k','10.88,15.78 12.4,15.72 11.55,16.72 10.55,17.95 12.45,17.78','.065')
s+=comment('Bottom-right local arrangement with arrows between three dashed levels.')
s+=paths('p','16.2,17.9 17.65,16.27 18.3,15.5 19.7,13.85;17.75,14.7 18.3,15.5 18.95,16.25 19.52,16.95 20.25,18.1;19.1,13.8 19.85,15.5 20.12,16.27 20.9,17.6;16.95,15.0 17.65,16.27 17.98,16.97 18.9,18.95;17.25,17.65 17.98,16.97 18.95,16.25 19.85,15.5 21.55,13.9;18.2,18.7 19.52,16.95 20.12,16.27 22.4,13.95')
s+=paths('k,dashed','16.2,15.6 18.3,15.5 19.85,15.5 22.25,15.52;15.85,16.3 18.95,16.25 20.12,16.27 22.9,16.32;16.3,17.1 17.98,16.97 19.52,16.95 21.7,17.0',False)
s+=paths('k,->','18.3,15.5 17.7,16.22;18.3,15.5 18.9,16.2;19.85,15.5 19.0,16.22;19.85,15.5 20.1,16.2;17.65,16.27 17.95,16.9;18.95,16.25 18.02,16.92;18.95,16.25 19.48,16.9;20.12,16.27 19.58,16.92',False)
s+=dots('k','18.3,15.5 19.85,15.5 17.65,16.27 18.95,16.25 20.12,16.27 17.98,16.97 19.52,16.95','.065')+end()
s+=r'''\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=.8em,row sep=1em]
\bullet\arrow[dr]\&{}\&\bullet\arrow[dl]\&\bullet\arrow[dr]\&{}\&\bullet\arrow[dl]\\
{}\&{}\arrow[drr]\&{}\&{}\&{}\arrow[dl]\&{}\\
{}\&{}\&{}\&{}\arrow[dl]\&{}\&{}\\
{}\&{}\&{}\arrow[dl]\&{}\&{}\&{}\\
{}\&{}\&{}\&{}\&{}\&{}
\end{tikzcd}}
\margin{144}
'''
(root/'pages/MPL_154_127-176_154_scan145.tex').write_text(s)
commit(145,[('text','upper printed area','DATASETS PICTURES'),('display','upper printed table','SYSMSG CNU M06 A 1 67 3,893 STD. **** ****'),('deletion','above main diagram','ABCDEFG; ABCED'),('diagram','centre left','D E F G; DE FG DG EG CG BG AG; branching arrows'),('display','attached to central diagram','letter orders; 1′–9′; circled GA; underlined groups'),('drawing','behind central diagram','pencil separators and heavily retraced lower arrows'),('drawing','upper right','marked line and crossing'),('drawing','middle right','partial grid; 5′,6–11; red arrows'),('diagram','bottom left','four unlabelled inputs converging'),('drawing','bottom centre','three-level pencil arrangement'),('drawing','bottom right','three dashed levels; arrows between intersections'),('margin note','bottom left','144')],sheet_kind='reused_typed',observations='Full page and both halves read, central sequence enlarged. Printed table differs from scan 127 in records and bytes: 67 and 3,893. Ordered-letter rows are copied individually, including braces, underlining, circles and deletions; lower rows and CG label have overwriting, marked uncertain. The visual heavy arrow redrawings are retained separately alongside the tikz-cd structure; no clean permutation sequence has been substituted for the written one. Right-grid first level reads 5′, followed by 6–11.')
