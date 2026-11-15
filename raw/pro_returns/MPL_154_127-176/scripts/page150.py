from pathlib import Path
from tikz import *
from commit_page import commit
root=Path(__file__).resolve().parents[1]
s=r'''\scanpage{150}
{\ttfamily\unsure{ACCOUNT NUMBER}\quad\unsure{**********}\quad DATE = 82.231\quad TIME = 8.51.16\quad SYSTEM 370/081 E333\quad VS2 \unsure{03.86|03.8G}\\
JOBNAME= CRAY2\quad NUMBER=231J002SCNU\quad CPU TOTAL = 1\quad RATE = 0, 1}
\diagram{{\tiny\begin{tabular}{cc|cc|cccccccccc|cc|c}
\multicolumn{2}{c|}{STEP}&\multicolumn{2}{c|}{TIME}&\multicolumn{10}{c|}{NUMBER OF EXCPS}&\multicolumn{2}{c|}{BYTES}&\\
NO&CORE&TIO&TCPU&3330&330-1&3340&3350&2250&\unsure{T/7TRK}&\unsure{T/9-16}&T/6250&SPOOL&VIO&SYSIN&SYSOUT&C.U\\\hline
1&8&\unsure{4}&1&0&0&0&0&0&0&0&0&1&0&0&0000288&105\\\hline
\multicolumn{2}{c|}{TOTALS}&\unsure{4}&1&0&0&0&0&0&0&0&0&1&0&0&0000288&105
\end{tabular}}}
\diagram{{\tiny\begin{tabular}{ccccc|cc|cccc|cccc|c|c}
\multicolumn{5}{c|}{STEP}&\multicolumn{2}{c|}{PAGING}&\multicolumn{4}{c|}{SWAP}&\multicolumn{4}{c|}{VIO}&CORE&SETUP TIME\\
NO&NAME&P.G.M&C.C.U&SRB&IN&OUT&N&OUT&P.IN&P.OUT&TOT&TOP&DU&OM&TU&TM.ELAPS\\\hline
1&&\unsure{TEFBR1}&105&0&0&0&0&0&0&0&6064&200&0&0&0&0\quad0\\\hline
\multicolumn{3}{c}{TOTALS}&\unsure{300}&0&0&0&0&0&0&0&\unsure{0}&\unsure{0}&0&0&0&0\quad0
\end{tabular}}}
{\ttfamily\unsure{RESOURCES ESTIMATED}\quad ( SYSOUT = \unsure{0120000|0130000}\quad EXCP = 1000\quad TIME = 6\quad REGION = 150K )\quad GIVING CLASS/PRIO = 1/ 6\\
RESOURCES USED\quad ( \unsure{SYSOUT = 0000288}\quad EXCP = 0\quad TIME = 1\quad REGION = 8K )\quad GIVING CLASS/PRIO = A/14\\
\unsure{\$HASP399} ENDED}
'''
s+=start()+comment('Upper chain of three pencil loops.')
s+=path('p,line width=.9pt','9.72,4.21 10.72,3.58 11.78,3.4 13.08,3.76 13.44,4.31 12.8,4.95 11.69,5.22 10.48,4.9 9.72,4.21',True)
s+=paths('p','9.72,4.21 10.56,4.93 11.69,5.22 12.78,5.03 13.59,4.56;10.33,3.82 10.49,4.61 10.93,4.98;13.23,4.33 14.23,4.35')
s+=path('p,line width=.8pt','14.23,4.35 15.33,3.48 16.63,3.14 18.08,3.4 18.95,4.24 18.1,5.01 16.66,5.37 15.12,5.14 14.23,4.35')
s+=paths('p','14.23,4.35 15.6,5.16 16.66,5.37 17.91,4.92 18.95,4.24;18.95,4.24 21.92,4.08;18.0,6.5 19.18,5.96 20.89,5.88 21.98,6.28')
s+=path('p','21.92,4.08 22.51,3.52 24.04,3.3 25.31,3.53 25.6,4.27 25.17,4.76 23.85,4.96 22.45,4.67 21.92,4.08')
s+=path('p,line width=2pt','25.6,4.27 27.11,4.27')+dots('p','9.72,4.21','.1')
s+=comment('Horizontal line with three marked crossings and pencil detours.')
s+=paths('p','4.52,7.62 6.2,8.63 8.1,9.89 9.3,10.52;7.53,6.74 6.2,8.63 5.23,9.86;9.49,6.5 10.27,8.47 10.81,9.84;11.25,6.65 10.27,8.47 9.25,10.89;10.79,6.65 11.19,7.69 11.77,8.9;14.58,6.55 14.92,7.51 15.27,8.62 16.64,10.51;16.28,7.19 15.27,8.62 14.01,10.53;14.85,7.37 14.25,8.89;15.27,8.62 16.13,8.17 16.96,7.44 18.35,8.67;16.96,7.44 17.33,9.0;16.96,7.44 16.18,8.62 16.0,8.85;6.2,8.63 9.67,7.66 11.1,7.28 13.1,7.37 14.92,7.51;10.27,8.47 12.71,7.89 14.92,7.51 16.05,7.56')
s+=path('w,line width=.8pt','3.47,8.76 6.2,8.63 10.27,8.47 15.27,8.62')+path('p,line width=2pt','15.27,8.62 16.9,8.62 18.35,8.67')+dots('k','6.2,8.63 10.27,8.47 15.27,8.62 18.35,8.67','.09')
s+=path('p,line width=1.4pt','7.22,11.45 10.06,11.05 12.43,10.64')+dots('p','10.06,11.05','.06')
s+=comment('Right two-point lens and small parallelogram.')
s+=paths('p','19.44,8.85 21.37,7.96 23.29,7.86 25.52,8.28 26.95,9.2;19.44,8.85 21.04,9.67 23.29,9.99 25.4,9.71 26.95,9.2;19.44,8.85 21.25,9.52 23.29,9.87 25.2,9.54 26.95,9.2;18.68,9.44 19.44,8.85 20.36,8.45;19.13,8.44 19.44,8.85;26.95,9.2 27.34,9.79;26.95,9.2 27.43,8.95')
s+=path('p,line width=1.3pt','19.44,8.85 23.45,8.99 26.95,9.2')+dots('p','19.44,8.85 26.95,9.2','.08')
s+=paths('p','19.68,13.44 19.56,12.64 20.01,11.59 21.17,10.77 22.15,10.54 22.81,10.86;19.68,13.44 20.2,13.82 21.08,13.91 21.69,13.74')
s+=paths('k','19.68,13.44 20.62,12.58;20.62,12.58 21.17,11.73 22.08,11.56 21.53,12.35 20.62,12.58;22.08,11.56 23.49,10.58',False)+dots('k','20.62,12.58 21.17,11.73 22.08,11.56 21.53,12.35','.11')
s+=comment('Lower central crossings with red and green dashed paths.')
s+=paths('p,line width=1.4pt','12.31,12.55 15.23,12.6 18.67,12.82;11.94,15.9 15.1,15.94 19.1,16.28;13.65,11.5 13.53,13.16 13.5,16.43 13.51,16.94;16.88,11.15 16.69,13.56 16.4,15.59 16.14,18.79;12.52,18.34 14.92,14.23 16.71,12.06 18.03,10.31;12.73,13.58 16.47,11.27;15.05,16.47 18.73,14.23')
s+=paths('p','12.36,12.2 14.92,14.23 17.06,15.78 19.11,17.74;12.83,17.7 14.92,14.23 18.02,10.8;13.03,15.7 16.29,16.08 19.2,16.29;12.4,15.77 15.12,15.81 18.97,16.17')
s+=paths('w,dash pattern=on 11pt off 7pt','12.99,11.62 14.92,14.23 16.29,16.08 17.49,17.73')
s+=paths('green!50!black,dash pattern=on 10pt off 5pt','13.09,11.52 14.92,14.23 16.4,15.59 18.2,17.94')
s+=paths('k,dashed','12.74,12.19 14.92,14.23 16.68,15.91 18.4,18.07')
s+=dots('k','13.62,12.58 13.7,12.98 16.4,15.59 16.29,16.08','.065')+dots('w','14.92,14.23','.16')
s+=path('k,fill=black','13.62,12.58 13.93,13.04 13.55,13.12',False,True)+path('k,fill=black','16.4,15.59 16.29,16.08 16.05,15.8',False,True)
s+=comment('Left axes, short segment and two collinear points.')
s+=paths('p,line width=1pt','6.88,12.16 6.64,14.85 6.67,17.24;3.86,14.86 6.64,14.85 10.19,14.67;4.16,18.64 8.32,18.46;7.53,20.08 10.29,20.01 17.69,20.06')
s+=dots('p','4.16,18.64 8.32,18.46 7.79,20.03 10.29,20.01','.085')
s+=path('p','7.79,20.03 9.07,19.84 10.29,20.01')
s+=comment('Right long narrow loops and lower construction.')
s+=paths('p','20.75,14.73 21.73,14.37 23.11,14.26 24.77,14.53 26.01,14.9 27.56,14.88 29.29,14.6;20.75,14.73 22.2,14.92 23.72,14.8 24.77,14.53 26.05,14.25 27.55,14.22 29.29,14.6;20.75,14.73 24.77,14.53 27.4,14.4 29.49,14.26;25.14,14.52 25.65,13.91 26.76,13.86 27.56,13.96 28.07,14.18;20.99,17.17 22.38,16.45 24.29,15.8 26.67,15.64 28.07,15.99;20.99,17.17 23.43,17.11 26.62,16.54 28.07,15.99;19.58,14.75 20.43,17.19 21.89,20.28;19.7,19.9 21.05,18.33 22.38,16.45;18.97,18.63 21.05,18.33 23.78,17.96')
s+=paths('p,line width=1.4pt','20.99,17.17 23.43,17.28 26.62,16.62 28.07,15.99')
s+=end()+r'\margin{149}'+'\n'
(root/'pages/MPL_154_127-176_154_scan150.tex').write_text(s)
commit(150,[('text','reverse printed upper header','ACCOUNT NUMBER; DATE 82.231; TIME 8.51.16; SYSTEM 370/081 E333'),('diagram','reverse printed upper table','STEP TIME NUMBER OF EXCPS BYTES C.U'),('drawing','top','three pencil loops linked by segments'),('drawing','upper middle','horizontal line with crossings, detours and marked endpoint'),('drawing','right middle','two-point pencil lens'),('diagram','reverse printed lower table','STEP PAGING SWAP VIO CORE SETUP TIME'),('drawing','middle left','oblique segment and marked point'),('drawing','middle right','four-point parallelogram on oblique line'),('drawing','lower centre','crossings with two dark triangles; red and green dashed paths'),('drawing','lower left','axes; short segment; two collinear points'),('drawing','lower right','narrow loops; long lens and pencil crossings'),('text','reverse printed footer','RESOURCES ESTIMATED; RESOURCES USED; HASP399 ENDED'),('margin note','bottom left','149')],sheet_kind='reused_typed',observations='Whole, both halves and horizontally reflected crops of the printing inspected. The reflected print is transcribed in reading order, with tables retaining fields and observed values; ambiguous overwritten fields and clipped headings are marked unsure. The page has no handwritten prose. Colour and pencil construction of each sketch retained.')
