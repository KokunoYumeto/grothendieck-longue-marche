from pathlib import Path
from tikz import *
root=Path(__file__).resolve().parents[1]
s='\\scanpage{132}\n'+start()
s+=comment('E01-E06: six unlabelled small studies at left, including two empty outlines.')
s+=paths('g','3.4,1.99 4.36,2.3 4.44,3.7 3.51,4.37 2.5,4.02 2.4,3.05',close=True)
s+=paths('r','2.4,3.3 4.4,3.3;2.5,3.82 3.6,3.68 4.4,2.43;3.65,1.99 3.3,2.95 3.54,4.36;3.3,2.02 3.13,3.4 2.82,4.31')
s+=paths('r','2.45,3.24 3.27,2.08;2.58,3.53 3.36,2.14;2.75,3.54 3.43,2.24;2.94,3.65 3.5,2.19',False)
s+=paths('g','7.53,2.5 8.54,2.69 9.11,3.65 8.65,4.51 7.3,4.85 6.35,4.03 6.57,3.12',close=True)
s+=paths('r','6.37,3.87 8.83,2.82;6.37,3.87 9.12,3.67;6.77,3.0 8.36,3.43 8.84,4.22;7.34,2.56 8.0,3.29 8.17,4.68;7.76,2.5 8.4,3.52 8.48,4.57;6.62,4.3 7.41,2.99 8.83,2.82;6.96,4.69 8.4,2.63')
s+=paths('g','8.1,5.37 9.26,5.79 9.31,7.11 8.66,7.84 7.4,7.7 6.78,6.45 7.18,5.7',close=True)
s+=paths('p','10.76,6.87 11.67,7.27 11.91,8.21 11.46,8.9 10.41,8.99 9.84,8.61 9.92,7.48',close=True)
s+=paths('g','3.38,6.73 4.57,7.2 4.8,8.7 3.72,9.69 2.42,9.45 1.91,8.47 2.21,7.26',close=True)
s+=paths('r','1.93,8.32 4.78,8.32;1.95,8.19 2.44,7.91;2.45,9.33 3.02,7.93;2.73,7.93 3.16,9.54;3.85,7.9 3.68,9.69;4.27,7.94 4.6,8.88;4.58,7.96 4.79,8.25',False)
s+=paths('r','1.98,11.71 2.44,10.77 3.39,10.39 4.62,10.83 4.9,11.69;1.99,11.69 4.9,11.69;1.98,11.89 2.2,12.65 3.23,13.09 4.08,12.84 4.79,11.91;3.14,10.46 3.04,11.09;3.15,10.45 3.38,11.0;3.79,10.49 3.79,11.34;4.53,10.8 4.07,11.63')
s+=paths('g','1.9,11.6 2.55,10.93 3.5,10.73 4.52,11.07 4.9,11.69')
s+=paths('g,dashed','1.94,11.27 2.66,10.5 3.68,10.3 4.8,10.62 4.96,11.5')
s+=comment('E07: large upper-central numbered arrangement.')
s+=paths('r','14.93,2.72 16.52,3.36 16.96,4.7 16.25,6.42 14.22,6.93 13.1,6.3 12.78,4.74 13.4,3.33',close=True)
s+=paths('r','14.02,2.91 14.74,4.28 15.21,6.87;15.61,2.82 14.69,4.18 14.22,6.93;13.15,6.2 14.59,5.53 16.51,3.5;12.54,4.76 17.31,4.72')
s+=paths('g','12.65,4.96 13.71,3.96 14.67,3.58 15.69,3.8 17.1,4.99')
s+=path('->','17.2,3.64 17.0,3.17')
s+=dots('black','12.84,4.44 13.07,4.76 12.84,5.0 14.58,3.75 14.84,3.7 15.08,3.43 14.5,3.48 16.22,3.86 16.01,4.18 16.92,4.45 16.67,4.72 16.84,5.0 17.21,4.7')
s+=labels([(xy,t) for xy,t in [('12.63,4.46','5'),('12.31,4.8','6'),('12.94,5.24','11=1'),('13.21,4.98','10'),('14.43,3.91','9'),('15.04,3.84','8'),('16.17,4.42','7'),('16.6,4.98','6'),('16.97,5.21','5'),('17.07,4.42','1'),('17.48,4.75','10'),('16.15,3.7','2'),('16.6,3.18','2'),('15.01,3.27','3'),('15.68,2.58','3'),('14.21,3.5','4'),('14.07,2.57','4')]])
s+=comment('E08: upper-right arrangement, boundary numbering and starred labels.')
s+=paths('r','22.71,2.78 24.77,3.55 25.44,5.35 24.8,7.36 23.27,8.19 21.65,8.22 20.13,7.02 19.9,5.3 20.65,3.79',close=True)
s+=paths('r','21.65,3.01 22.76,4.52 23.28,8.19;23.61,2.84 22.32,4.87 21.65,8.22;20.13,7.02 23.19,6.09 25.27,4.14;19.69,5.29 25.46,5.51')
s+=paths('g,dashed','19.72,5.51 20.93,4.23 22.62,3.66 24.17,4.06 25.46,5.5')
s+=dots('black','21.65,3.01 23.61,2.84 25.27,4.14 25.42,5.24 25.4,5.59 19.93,5.02 19.91,5.51 20.13,7.02 21.65,8.22 23.28,8.19')
s+=labels([('21.65,2.71','4'),('23.7,2.61','3'),('25.48,3.9','2'),('25.67,5.26','1'),('25.62,5.94',r'\unsure{10|40}'),('19.75,4.91','5'),('19.72,5.76','6'),('19.85,7.24','7'),('21.54,8.56','8'),('23.2,8.62','9'),('20.44,5.17',r'10^*'),('25.1,5.37',r'6^*')])
s+=paths('w,->','20.15,5.49 19.88,5.5;25.28,5.8 25.1,5.49')
s+=comment('E09: small right circular count, marks and two orange arrows.')
s+=paths('k','26.8,6.81 27.8,7.4 27.98,8.3 27.44,9.35 26.52,9.65 25.62,9.17 25.35,8.35 25.8,7.32',close=True)
s+=paths('g,line width=3pt','25.28,8.33 25.6,7.48 26.24,6.86 27.12,6.77 27.93,7.59 28.1,8.36')
s+=paths('k','25.36,8.33 28.0,8.33',False)
s+=paths('k','25.83,7.35 26.0,7.57;26.46,6.88 26.49,7.1;27.23,6.95 27.12,7.18;27.83,7.52 27.59,7.7;27.92,8.88 27.67,9.04;27.39,9.38 27.24,9.18;26.45,9.63 26.47,9.4;25.64,9.22 25.9,8.94',False)
s+=paths('r,->','25.13,8.53 25.1,8.94;28.37,8.46 28.24,8.86')
s+=comment('E10: mid-left second numbered arrangement.')
s+=paths('r','8.05,9.43 9.45,9.94 9.62,11.13 8.91,12.25 7.48,12.53 6.59,11.94 6.44,10.61 7.03,9.71',close=True)
s+=paths('r','7.66,9.53 8.0,10.92 8.94,12.25;8.46,9.48 7.63,10.69 7.56,12.43;7.09,12.2 8.5,11.38 9.17,9.78;6.45,11.0 9.56,10.96')
s+=paths('g','6.51,10.78 7.25,9.95 8.35,9.79 9.59,10.78;6.49,10.98 7.31,10.25 8.25,10.0 9.55,10.97')
s+=paths('->','6.52,10.4 6.66,10.07;9.64,10.48 9.68,10.02')
s+=dots('black','6.53,10.7 6.87,11.0 7.75,9.84 7.8,10.11 8.22,9.73 8.22,10.0 9.09,10.0 8.89,10.43 9.34,10.95 9.57,10.9')
s+=labels([('6.36,10.57','5'),('6.92,11.24','10'),('7.59,10.34','9'),('8.23,10.16','8'),('8.77,10.54','7'),('9.28,11.17','6'),('9.74,10.59','1'),('9.27,10.03','2'),('8.41,9.7','3'),('7.67,9.67','4')])
s+=comment('E11 and E12: black circular studies with ticks, dot and directed arcs.')
s+=paths('k','15.21,8.5 16.3,8.84 16.55,9.91 15.51,10.96 14.33,10.98 13.78,10.2 13.93,9.21',close=True)
s+=paths('k','15.25,8.7 16.13,8.95 16.25,9.7 15.36,10.63 14.52,10.78 14.03,10.14 14.11,9.22',close=True)
s+=paths('k','15.21,8.57 16.26,8.91 16.44,9.88 15.5,10.87 14.39,10.86 13.86,10.11 14.06,9.24',close=True)
s+=paths('k','13.81,9.32 14.15,9.44;15.13,8.33 15.17,8.78;15.0,10.75 15.23,11.3;13.66,10.62 14.13,10.27;16.13,9.95 16.65,10.22;15.99,9.14 16.4,8.75',False)
s+=dots('black','16.28,8.82',r='.08')
s+=paths('k','10.1,13.7 10.45,12.64 11.32,11.94 12.36,11.93 13.15,12.47 13.55,13.21;13.6,13.78 13.09,14.61 11.94,15.03 10.8,14.77 10.21,13.95;10.17,13.6 10.4,12.5 11.37,11.86 12.43,12.0 13.2,12.7 13.6,13.2;13.5,13.8 13.05,14.55 11.95,14.92 10.71,14.66 10.17,13.99')
s+=paths('k,->','13.78,13.24 13.72,12.8 13.43,12.42;10.8,14.6 10.19,13.9')
s+=dots('black','13.57,13.48',r='.08')
s+=comment('E13: middle-right divided count and crossing arrows.')
s+=labels([('23.03,10.35',r'2n\,/\,2(n\unsure{-|+}1)+2=2n')])
s+=paths('g','21.58,11.65 24.59,11.39',False)
s+=paths('k,->','22.93,12.12 22.87,10.89;22.92,11.55 22.88,11.3',False)
s+=comment('E14: lower central coloured circle with primed numbers.')
s+=paths('w','18.75,12.13 20.42,12.54 21.21,14.3 20.65,16.13 19.35,16.89 17.46,16.42 16.56,15.2 16.77,13.48',close=True)
s+=paths('r','17.23,12.91 17.8,14.95 18.7,15.73 20.72,16.07;19.08,12.1 18.7,14.5 19.08,15.9 19.85,16.86;16.95,15.94 19.36,14.71 21.0,13.3;16.42,14.7 21.58,14.55')
s+=paths('g','16.49,14.96 16.95,13.97 18.08,13.52 19.72,13.69 21.34,14.53')
s+=paths('w,dashed','16.46,14.24 17.53,13.46 18.82,13.31 20.28,13.62 21.22,14.26;16.82,14.3 17.58,13.79 18.81,13.68 20.12,13.87 21.07,14.38')
s+=paths('k','17.19,13.06 17.3,13.29;17.24,13.56 17.44,13.71;18.52,13.26 18.87,13.26;18.54,13.61 18.78,13.61;20.47,13.49 20.73,13.66;20.46,13.8 20.69,14.0',False)
s+=path('k,->','19.98,12.03 19.77,12.13')
s+=labels([('17.1,12.45','4'),('19.0,11.82','3'),('21.2,13.04','2'),('21.4,14.12','0'),('21.56,14.68',r"1'"),('21.0,16.18',r"4'"),('19.96,17.36',r"3'"),('16.86,16.3',r"2'"),('16.2,14.7','1'),('16.39,14.15',r"0'"),('16.93,14.96',r'\unsure{\alpha|11}'),('21.03,14.83',r"\unsure{\alpha'}")])
s+=comment('E15: left rectangular numbered strip.')
s+=paths('p','4.94,14.25 7.76,14.06;4.94,15.26 7.57,15.35',False)
s+=paths('k','4.94,14.39 4.93,15.26;7.77,14.25 7.7,15.09',False)
s+=paths('p','5.8,14.07 5.8,14.28;6.42,14.03 6.42,14.19;7.14,13.98 7.14,14.12;5.64,15.16 5.64,15.36;6.94,15.25 6.94,15.45',False)
s+=labels([('4.75,14.02','5'),('5.82,13.81','4'),('6.39,13.8','3'),('7.13,13.69','2'),('7.99,14.08','1'),('4.65,15.59',r"5'"),('5.64,15.65',r"4'"),('6.3,15.6',r"3'"),('6.97,15.71',r"2'"),('7.8,15.62',r"1'")])
s+=comment('E16: left lower circle with indexed Greek labels.')
s+=paths('k','2.44,15.85 3.34,16.12 3.68,17.12 3.5,17.83 2.5,18.25 1.56,17.84 1.43,16.88 1.86,16.19',close=True)
s+=path('p','1.43,17.13 3.66,17.17',False)
s+=dots('black','1.43,17.13 1.49,17.71 1.6,16.66 3.63,16.63 3.67,17.12 3.57,17.74')
z=r'\unsure{\zeta|\xi}'
s+=labels([('1.08,16.32',z+'_{n-2}'),('.96,17.23',z+r'_{n-1}=\unsure{\alpha}'),('1.03,17.07',r"\unsure{\alpha'}"),('1.07,18.12',z+r"'_1"),('1.96,18.55',z+r"'_2"),('3.89,16.64',z+'_1'),('3.92,17.25',z+'_0'),('4.0,18.11',z+r"'_{n-2}")])
s+=path('k','2.84,18.65 3.14,18.52 2.95,18.89 2.81,18.7 3.09,18.81 2.91,18.57')
s+=comment('E17-E18: two order diagrams, and the arrowed circle at bottom right.')
s+=labels([('22.97,12.88','1'),('23.54,12.88','2'),('24.12,12.88','3'),('24.62,12.88','4'),('22.99,13.5',r"1'"),('23.55,13.5',r"2'"),('24.12,13.5',r"3'"),('24.68,13.5',r"4'")])
s+=path('p','23.44,12.54 24.95,12.54 25.1,13.12 25.1,13.67 23.34,13.89 23.34,12.56',False)
s+=path('p,->','24.91,12.7 25.01,12.92 24.46,13.12 22.7,13.13 22.49,13.4 22.88,13.52')
seq=['0',"2'","3'","4'",r'\unsure{0}\prime','1','2','3','4',"1'"]
s+=labels([(str(22.95+i*.4)+',14.8',v) for i,v in enumerate(seq)])
for a,b,y in [(22.91,25.05,15.22),(23.36,25.44,15.39),(23.75,25.84,15.56),(24.15,26.21,15.66),(24.55,25.03,15.08)]:
 s+=path('k',f'{a},15.02 {a},{y} {b},{y} {b},15.02')
s+=labels([('24.48,16.43',r'\mathrm{Circ}(\overrightarrow{I\setminus\{i_0\}})\leftarrow\widetilde{\imath}_0')])
s+=paths('k','25.15,18.46 26.16,19.03 26.28,20.01 25.53,20.71 24.5,20.64 23.92,19.94 24.07,18.94',close=True)
s+=path('k','23.99,19.58 26.28,19.58',False)
s+=path('k,->','26.62,19.48 26.58,18.72 26.27,18.31')
s+=dots('black','23.99,19.58 26.28,19.58')
s+=labels([('23.65,19.98',r'\alpha'),('26.76,19.91',r"\alpha'")])
s+=comment('E19: lower central empty green outline.')
s+=paths('g','15.5,17.63 16.63,18.03 17.04,19.56 16.14,21.14 14.69,21.06 14.04,19.59 14.21,18.24',close=True)
s+=end()
s+=r'''
% E20: two-arrow diagram; the overwritten sign remains marked.
\diagram{\[\begin{tikzcd}[column sep=large,row sep=large]
\widetilde{\Delta}_{\widetilde{\unsure{S|s}}}\arrow[r,"\varphi_0", "\sim"']\arrow[dr,"\varphi_1"'] & \widetilde{\Delta}'_{\widetilde{\unsure{S|s}}'_0}\unsure{.}\\
&\widetilde{\Delta}'_{\widetilde{\unsure{S|s}}_1}\deleted{\unsure{\xi}}
\end{tikzcd}\]}
% E21: labels and sequences below the left circle.
\[1\quad2\quad3\quad4\qquad1'\quad2'\quad3'\quad4'\]
\[\unsure{\zeta|\xi}_0\quad\unsure{\zeta|\xi}_1\quad\unsure{\zeta|\xi}_2\quad\unsure{\zeta|\xi}_3=\unsure{\zeta|\xi}_{n-1}.\]
\[\alpha\quad u^n\unsure{\zeta|\xi}_0,\ u^{n+1}\unsure{\zeta|\xi}_0,\ {-}\ u^{2(n-1)-1}\unsure{\zeta|\xi}_0\]
% E22: lower central sequence, with annotation written underneath.
\[\unsure{\zeta|\xi}_0\quad\unsure{\zeta|\xi}_1\quad {-}\quad\unsure{\zeta|\xi}_{n-2}\quad\underset{u^{n-1}}{\unsure{\zeta|\xi}_{n-1}}=\unsure{\zeta|\xi}'_0\]
% E23: lower-right two sequences and separate alpha.
\[\alpha,\ u^n\unsure{\zeta|\xi}_0,\ u^{n+1}\unsure{\zeta|\xi}_0,\ {-},\ u^{2n-2}\unsure{\zeta|\xi}_0\]
\[\alpha,\]
\[\unsure{\zeta|\xi}_0\quad\unsure{\zeta|\xi}_1\quad {-}\quad\unsure{\zeta|\xi}_{n-1}\quad\unsure{\bar\zeta_n|\bar\xi_n}=\unsure{\zeta|\xi}'_0\]
% E24: faint, mirrored printed matter visible through the sheet.
\begin{center}\reflectbox{\begin{minipage}{.95\linewidth}\ttfamily\scriptsize\color{gray}
STMT NO. MESSAGE\par
4\quad\unsure{IEF653I} SUBSTITUTION JCL - PGM=\unsure{CRBATCH},REGION=100K,PARM=\par
\$HASP373 STARTED - INIT 10 - CLASS Q - SYS E333\par
IEF236I ALLOC. FOR CRAY2\par
IEF237I 220 ALLOCATED TO SYSUT1\par
IEF237I 4C9 ALLOCATED TO SYSUT2\par
IEF237I VIO ALLOCATED TO SYSIN\par
IEF237I JES2 ALLOCATED TO SYSOUT\par
IEF237I 77F ALLOCATED TO \unsure{SYS004}\par
IEF237I JES2 ALLOCATED TO SYSLST\par
IEF237I 77F ALLOCATED TO \unsure{SYS013}\par
IEF237I 79F ALLOCATED TO \unsure{SYS012}\par
IEF285I \unsure{CRAY2.JOB18221.T150735.R002}\quad CATALOGED\par
IEF285I VOL SER NOS= \unsure{CRAY11}.\par
CSS2060 - JOB QUEUED FOR TRANSFER\par
IEF142I CRAY2 CSSBATCH - STEP WAS EXECUTED - COND CODE 0000\par
IEF285I CISI.PROD.CSSBATCH.V1.\unsure{YY01}\quad KEPT\par
IEF285I VOL SER NOS= \unsure{VS?04}.\par
IEF285I \unsure{SYSCINC.VSAC15}\quad KEPT\par
IEF285I VOL SER NOS= \unsure{SAC15}.\par
IEF285I \unsure{SYS821.T150702.RA000.CRAY2.SYSUT1}\quad DELETED\par
IEF285I JES2.JOB00352.S00002\quad SYSOUT\par
IEF285I \unsure{SYSCAR.JIF}\quad KEPT\par
IEF285I VOL SER NOS= CRAY11.\par
IEF285I JES2.JOB00352.S00101\quad SYSIN\par
IEF285I SYS.CTLG.VCRAY11\quad KEPT\par
IEF285I VOL SER NOS= \unsure{CRAY11}.\par
IEF373I STEP /CSSBATCH/ START 82231.1507\par
IEF374I STEP /CSSBATCH/ STOP 82231.1507 CPU\quad 0MIN 00.16SEC SRB\quad 0MIN 00.02SEC VIRT\par
IEF375I JOB /CRAY2\quad / START 82231.1507\par
IEF376I JOB /CRAY2\quad / STOP 82231.1507 CPU\quad 0MIN 00.16SEC SRB\quad 0MIN 00.02SEC
\end{minipage}}\end{center}
\margin{131}
'''
(root/'pages/MPL_154_127-176_154_scan132.tex').write_text(s,encoding='utf-8')
