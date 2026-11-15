from pathlib import Path
from tikz import *
from commit_page import commit
root=Path(__file__).resolve().parents[1]
s='\\scanpage{144}\n'+start()+comment('Five local pencil/ink constructions, with red and green dashed alterations.')
s+=paths('p,line width=1pt','.48,8.3 2.6,6.3 5.65,3.6 8.6,.95;.48,8.3 1.35,7.3 1.85,6.3 3.05,5.2 5.78,4.85 6.65,3.9 7.5,2.15 8.6,.95;2.73,2.15 3.05,5.2 3.5,8.25;5.52,1.95 5.78,4.85 5.9,8.1;2.37,5.25 4.1,5.02 5.78,4.85 6.8,4.8;6.7,6.05 8.62,5.27 10.5,4.4 13.2,4.3;7.95,2.85 8.62,3.65 9.5,4.9 10.15,5.95;8.62,3.65 8.6,5.27 8.6,6.0;8.55,2.98 8.53,4.2 8.63,5.4;9.88,4.33 11.8,4.4 13.1,4.33')
s+=paths('k,line width=2pt','3.05,5.2 5.78,4.85')
s+=paths('k','1.85,6.3 3.05,5.2;5.78,4.85 6.55,4.0 7.2,2.6 7.65,1.9')
s+=paths('w,dashed','1.35,6.72 1.85,6.3 3.05,5.2;5.78,4.85 6.55,4.0 8.2,2.5')
s+=dots('k','3.05,5.2 5.78,4.85','.07')+dots('p','8.62,3.65 8.6,5.27','.055')
s+=comment('Small upper-central crossing.')
s+=paths('p','12.6,3.72 14.9,2.65 18.2,1.2;13.52,2.35 14.88,3.88 15.32,4.3;14.9,1.78 14.88,3.88 14.9,4.62;14.88,3.88 16.3,2.28')
s+=comment('Central angular local detours.')
s+=paths('p,line width=.9pt','11.9,6.23 14.9,6.0 18.72,5.62 21.25,5.37 24.48,4.95;15.98,2.7 17.22,4.3 18.72,5.62 19.8,6.83;16.78,4.5 18.4,6.63 19.0,7.6;18.4,6.63 18.72,5.62 19.08,4.4;16.68,5.75 17.2,5.9 17.6,6.4;18.72,5.62 18.9,5.95 19.8,5.6')
s+=paths('k','14.83,6.08 16.4,6.28 18.4,6.63 18.72,5.62 21.25,5.37;16.75,3.62 17.15,4.3 18.4,6.63 18.9,7.6;16.92,4.1 18.72,5.62 19.8,6.73;19.06,4.4 18.72,5.62 18.12,7.68',False)
s+=dots('k','11.9,6.23 18.4,6.63 18.72,5.62 21.25,5.37 24.48,4.95','.07')
s+=paths('k,thin','14.82,6.1 14.93,5.98;20.9,5.34 20.98,5.29',False)
s+=comment('Upper-right fan through three marked points.')
s+=paths('p,line width=1pt','19.5,3.78 21.4,3.25 23.27,2.77 25.1,2.25;20.3,2.55 21.4,3.25 22.6,4.08 23.05,4.32;21.67,2.55 21.4,3.25 21.25,3.72;21.86,2.2 22.3,3.1 22.6,4.08 22.63,4.55;22.86,1.83 22.6,4.08 22.45,4.8;23.77,1.9 23.27,2.77 22.6,4.08;19.5,3.78 21.2,4.0 22.6,4.08 23.5,3.2 24.9,2.3')
s+=dots('p','21.4,3.25 22.6,4.08 23.27,2.77','.07')
s+=comment('Lower-right two-point sketch, coloured dashed paths.')
s+=paths('p','23.95,9.0 25.4,8.0 26.5,7.3 27.9,6.2 28.8,5.45;24.3,7.5 25.4,7.5 27.05,7.47 27.45,7.55;24.85,6.25 25.4,7.5 26.1,8.88;25.3,6.0 25.4,7.5 25.42,8.8;26.25,5.45 27.05,7.47 27.4,8.35;26.98,5.58 27.05,7.47 27.0,8.72;25.8,5.9 26.75,7.15 27.55,7.9;25.15,6.43 25.4,7.5 25.67,8.75')
s+=paths('w,dashed','23.95,9.05 25.0,8.25 27.05,7.47 27.85,6.17 28.8,5.45')
s+=paths('green!50!black,dashed,line width=1.6pt','23.95,8.95 25.0,8.15 25.4,7.5 26.5,6.93 27.9,6.2')
s+=dots('k','25.4,7.5 27.05,7.47','.07')+end()
s+=r'{\ttfamily\unsure{***}\quad\unsure{CRAY2}\quad0025\quad I}'+'\n'
# Each zero position is manually entered from the rotated printed image.
zcols=[list(range(11,19)),list(range(9,19)),[7,8,15,16,17,18],[6,7,13,14,16,17],[5,6,11,12,15,16],[4,5,9,10,14,15],[3,4,7,8,13,14],[2,3,5,6,12,13],[1,2,3,4,11,12],[0,1,2,10,11],list(range(10)),list(range(8))]
zero=[]
for cols in zcols:
 a=[' ']*61
 for off in [0,14,28,42]:
  for j in cols:a[off+j]='0'
 zero.append(''.join(a).rstrip())
banner=[
' CCCCCCCCCC   RRRRRRRRRRR   AAAAAAAAAA   YY        YY   2222222222',
'CCCCCCCCCCCC  RRRRRRRRRRRR AAAAAAAAAAAA  YY        YY  222222222222',
'CC        CC  RR        RR AA        AA  YY      YY   22        22',
'CC            RR        RR AA        AA   YY    YY             22',
'CC            RR        RR AA        AA    YY  YY              22',
'CC            RRRRRRRRRRRR AAAAAAAAAAAA     YYYY              22',
'CC            RRRRRRRRRRR  AAAAAAAAAAAA      YY              22',
'CC            RR    RR     AA        AA      YY             22',
'CC            RR     RR    AA        AA      YY            22',
'CC        CC  RR      RR   AA        AA      YY           22',
'CCCCCCCCCCCC  RR       RR  AA        AA      YY          222222222222',
' CCCCCCCCCC   RR        RR AA        AA      YY          222222222222']
s+=r'{\scriptsize\begin{tabular}{l}'+'\n'
for row in zero+['']+banner:s+=r'\texttt{'+row.replace(' ',r'\ ')+'}'+r'\\'+'\n'
s+=r'\end{tabular}}'+'\n'
for i in range(6):
 s+=r'{\ttfamily ****A\quad\unsure{END|FND}\quad JOB\quad25\quad CRAY2\quad ROOM\quad 9.03.23 AM 19 AUG 82\quad R6.PR1\quad SYS JES2\quad JOB\quad25\quad END\quad A****}'+'\\\\\n'
s+=r'\margin{143}'+'\n'
(root/'pages/MPL_154_127-176_154_scan144.tex').write_text(s)
commit(144,[('drawing','upper left','two marked points; pencil crossings; red dashed path'),('drawing','upper middle','small pencil crossing'),('drawing','centre','angular detours with marked points'),('drawing','upper right','three-point fan'),('drawing','right middle','two-point sketch; green and red dashed paths'),('text','inverted printed lower area','CRAY2 0025 I; four zero-character figures'),('text','inverted printed lower area','CRAY2 letter-character banner'),('text','six inverted printed rows','END/FND JOB 25 CRAY2 ROOM 9.03.23 AM 19 AUG 82 R6.PR1 SYS JES2'),('margin note','bottom left','143')],sheet_kind='reused_typed',observations='Whole, both halves and rotated printed-detail crops visually inspected. The printed four large zero figures and CRAY2 banner are encoded character by character from observed rows; the generator uses manually entered column positions for the repeated zero shapes. END/FND remains an uncertainty at the left end of each repeated printed row because the lower horizontal of E is absent/faint. The clipped tiny heading is separately uncertain. Dark smudges on paper are not interpreted as words or mathematical cancellations. No handwritten prose on this sheet.')
