from pathlib import Path
import ast
from tikz import *
from commit_page import commit
root=Path(__file__).resolve().parents[1]
node=ast.parse((root/'scripts/page144.py').read_text())
ns={}
for a in node.body:
 if isinstance(a,ast.Assign) and any(isinstance(t,ast.Name) and t.id in ['zcols','banner'] for t in a.targets):exec(compile(ast.Module(body=[a],type_ignores=[]),'<manually-read-type-banner>','exec'),ns)
s=r'\scanpage{147}'+'\n'+r'{\ttfamily\unsure{*** CRAY2}\quad0025\quad I}'+'\n'
zero=[]
for cols in ns['zcols']:
 a=[' ']*61
 for off in [0,14,28,42]:
  for j in cols:a[off+j]='0'
 zero.append(''.join(a).rstrip())
s+=r'{\scriptsize\begin{tabular}{l}'+'\n'
for row in zero+['']+ns['banner']:s+=r'\texttt{'+row.replace(' ',r'\ ')+'}'+r'\\'+'\n'
s+=r'\end{tabular}}'+'\n'
for i in range(6):s+=r'{\ttfamily ****A\quad START\quad JOB\quad25\quad CRAY2\quad ROOM\quad 9.01.53 AM 19 AUG 82\quad R6.PR1\quad SYS JES2\quad JOB\quad25\quad START\quad A****}'+'\\\\\n'
s+=r'''{\ttfamily
DERNIERE MISE A JOUR DE JOURNAL : 11-08-82\\
ATTENTION .........\\
\unsure{T|I}\qquad UN ARRET EXCEPTIONNEL POUR PREPARER L'ARRIVEE DE NOUVELLES\\
\unsure{T|I}\qquad UNITES AURA LIEU DU VENDREDI 20 AOUT A 17H 30 AU LUNDI\\
\unsure{I|T}\qquad 23 AOUT A 8H.}
'''
s+=start()+comment('Unlabelled pencil and darker ink arrangements, at their relative positions on the reused sheet.')
s+=path('p,line width=.8pt','2.34,7.45 2.74,6.65 3.45,6.25 4.65,6.03 6.31,6.45 7.23,7.48 7.44,8.65 6.65,10.25 5.48,10.94 4.45,11.02 3.62,10.71 2.8,10.08 2.34,8.97',True,True)
s+=paths('p,line width=1pt','2.74,6.65 2.87,7.25 3.75,7.4 4.6,8.12 4.95,8.55 4.99,9.63 5.96,10.63;3.4,6.36 3.39,8.02 3.6,9.65 4.55,10.39 5.28,10.74 6.03,10.63;4.69,6.06 4.6,8.27 4.55,10.4 4.5,10.98;6.31,6.45 6.6,7.01 6.71,8.5 6.3,9.39 6.52,9.99 6.43,10.39;2.36,7.09 3.2,7.06 4.38,7.48 5.5,8.28 6.3,9.39;2.31,7.94 3.5,8.49 4.85,9.02 6.3,9.39 7.13,9.43;2.7,9.74 3.64,9.99 4.63,9.64 5.97,9.05 7.23,7.67;3.62,10.71 4.55,10.39 5.7,9.73 6.9,8.93')
s+=dots('p','6.31,6.45 3.62,10.71','.075')
s+=path('p','8.59,12.43 8.72,11.77 9.58,11.07 10.76,10.76 11.91,11.18 12.29,12.13 12.11,13.15 11.25,13.88 10.2,13.92 9.26,13.68 8.71,13.16',True,True)
s+=paths('p','8.85,11.58 9.6,11.09 10.29,10.78;10.8,13.45 11.14,13.18 11.7,12.33')
s+=path('p,line width=.85pt','1.26,18.49 1.45,17.48 2.36,16.4 3.36,15.87 4.05,15.75 5.06,16.01 5.92,16.68 6.49,17.78 6.58,18.7 5.65,20.12 4.63,21.03 3.5,21.28 2.22,20.87 1.53,19.92',True,True)
s+=paths('p','3.38,15.71 4.19,16.75 5.18,17.4 5.93,17.6;5.06,16.01 4.8,17.25 4.27,18.6 3.88,20.3 3.5,21.28;2.36,16.4 3.43,17.24 4.52,18.19 5.39,19.37 5.7,20.32;1.73,16.94 2.82,17.02 3.85,17.36 5.14,17.56 6.16,17.11;1.26,18.49 2.58,18.64 4.08,18.37 5.07,18.01 6.49,17.78;1.84,19.22 3.02,18.24 4.35,17.4 5.98,16.86;1.7,20.1 3.02,20.01 4.53,19.68 6.57,18.69;2.13,20.8 2.24,20.03 2.87,18.9 4.0,18.05;4.64,21.03 4.35,19.9 4.12,18.39;5.1,20.83 5.05,19.4 4.52,18.2;3.5,21.28 4.8,20.06 5.4,19.47 6.18,19.08')
s+=paths('k','1.75,16.91 2.81,16.9 3.92,17.42 4.54,18.21 4.84,19.05 3.5,21.28;2.23,16.54 3.02,16.8 3.23,17.2 3.39,18.64 3.69,19.6 3.5,21.28;3.01,16.52 3.2,16.65 3.28,18.05 3.5,19.85 3.5,21.28;3.38,15.71 3.79,16.21 4.64,16.62 5.06,17.17 5.01,18.43 4.29,20.2 3.5,21.28;3.5,21.28 3.9,19.93 4.31,19.34 4.92,18.78;3.5,21.28 4.05,20.3 4.73,19.62 5.17,18.94')
s+=paths('w,line width=2pt','4.05,15.75 2.87,15.92 2.44,16.55 2.2,18.47 2.24,20.03 2.83,20.65 3.5,21.28;4.05,15.75 3.01,16.2 2.87,17.68 2.87,18.9 3.22,20.4 3.5,21.28;4.05,15.75 3.93,17.17 3.89,18.7 3.89,19.75 3.5,21.28;4.05,15.75 4.44,16.19 5.07,16.9 5.32,17.72 5.26,18.91 4.63,20.34 3.5,21.28;4.05,15.75 4.13,16.66 4.29,17.54 4.44,18.35 4.21,19.96 3.5,21.28;4.05,15.75 3.73,17.02 3.77,18.76 4.07,19.84 3.5,21.28;3.5,21.28 3.64,19.95 3.63,18.29 3.61,17.03;3.5,21.28 3.48,19.85 3.47,17.65 3.38,17.07')
s+=dots('k','4.05,15.75 3.5,21.28 2.24,20.03','.085')
s+=path('p,line width=.9pt','7.45,17.78 7.73,16.65 8.76,15.83 10.2,15.7 11.98,16.02 12.84,17.09 12.97,18.39 12.17,19.66 10.05,20.68 8.33,19.78 7.57,18.76',True,True)
s+=paths('p,line width=.8pt','9.52,15.72 9.3,16.9 9.28,17.83 9.54,18.64 10.63,19.78 10.88,20.37;9.83,15.7 9.6,16.62 10.36,17.48 11.11,18.59 11.48,19.83 11.43,20.19;10.2,15.7 10.21,17.3 10.1,19.22 10.05,20.68;8.7,15.9 10.7,16.82 11.75,17.88 12.41,19.14;7.68,18.3 9.34,17.52 10.86,16.86 11.98,16.02;7.62,19.1 8.8,18.52 11.03,17.65 12.84,17.09;8.51,20.06 9.44,19.01 11.05,18.25 12.65,17.85;10.05,20.68 9.78,19.58 10.25,18.95 10.96,18.39 12.17,19.66')
s+=paths('k','9.12,15.8 8.83,16.61 8.7,17.06 9.26,17.62 10.3,17.97;9.99,15.71 10.11,16.21 10.5,16.71 10.66,17.16 10.94,17.54 11.0,18.34 10.59,19.67 10.36,20.49;12.38,16.3 12.47,17.36 12.32,18.3 11.82,19.04 11.01,19.23 10.12,19.07 8.3,19.74;8.76,20.04 8.75,18.75 8.85,18.17 9.28,17.63')
s+=dots('k','10.2,15.7 10.05,20.68','.085')
s+=path('p,line width=.85pt','16.36,18.2 16.85,16.72 17.98,15.64 20.15,15.32 21.7,15.92 22.72,17.2 22.95,18.2 22.31,19.68 20.9,20.91 19.32,21.38 17.7,20.88 16.73,19.85',True,True)
s+=paths('p,line width=.85pt','17.84,15.73 17.94,17.2 18.77,18.06 19.76,19.4 20.82,20.94;20.15,15.32 19.99,17.12 19.71,18.9 19.32,21.38;16.6,18.47 18.22,17.43 20.07,16.73 21.85,16.39;17.28,16.03 19.15,16.71 20.4,17.61 22.31,19.68;17.33,19.86 19.46,19.73 21.34,19.16 22.77,18.46')
s+=paths('k','17.91,15.77 17.92,16.64 18.14,17.2 18.7,17.63;22.8,17.3 22.91,18.24 22.54,19.25 21.82,20.07 20.91,20.9 19.32,21.38')
s+=path('p,line width=.8pt','17.62,20.52 18.01,20.52 18.37,20.38 18.8,20.36 19.3,20.6 19.85,20.44 20.28,20.36 20.57,20.64 20.89,20.29 21.28,20.28 21.66,20.21 21.79,20.37')
s+=dots('k','20.15,15.32 19.32,21.38','.085')+end()+r'\margin{146}'+'\n'
(root/'pages/MPL_154_127-176_154_scan147.tex').write_text(s)
commit(147,[('text','upper left clipped heading','*** CRAY2 0025 I'),('text','upper printed area','four zero-character figures; CRAY2 banner'),('text','middle six printed rows','START JOB 25 CRAY2 ROOM 9.01.53 AM 19 AUG 82'),('text','middle lower printed notice','DERNIERE MISE A JOUR DE JOURNAL : 11-08-82'),('drawing','upper left','pencil sphere with intersecting curves and two marked points'),('drawing','middle left','very faint circular pencil sketch'),('drawing','lower left','dense dark red and black meridian fan'),('drawing','lower middle','sphere with two marked poles and crossing curves'),('drawing','lower right','sphere with two marked poles and wavy lower curve'),('margin note','bottom left','146')],sheet_kind='reused_typed',observations='Whole image and both halves inspected. Printed banner manually compared with the previously transcribed same form; all six time rows here read 9.01.53. The clipped heading and three isolated printed line markers remain uncertain. The lower-right wavy stroke is rendered graphically, as no word can be identified there. No algebraic labels are supplied to the unlabelled drawings.')
