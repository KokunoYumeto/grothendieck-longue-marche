from pathlib import Path
from tikz import *
from commit_page import commit
R=Path(__file__).resolve().parents[1]
s=r'''\scanpage{173}
\begin{verbatim}
           00000000      00000000    555555555555       11
         0000000000    0000000000    555555555555      111
       00      0000  00      0000  55               1111
      00     00 00  00     00 00  55                11
     00    00  00  00    00  00  55                11
    00   00   00  00   00   00  555555555         11
   00  00    00  00  00    00  5555555555        11
  00 00     00  00 00     00          55        11
 0000      00  0000      00           55       11
000       00  000       00           55       11
0000000000    0000000000    555555555555   1111111111
00000000      00000000     55555555555   1111111111
\end{verbatim}
\begin{verbatim}
 CCCCCCCCCC   RRRRRRRRRRR    AAAAAAAAAA   YY        YY   2222222222
CCCCCCCCCCCC  RRRRRRRRRRRR  AAAAAAAAAAAA  YY        YY  222222222222
CC        CC  RR        RR  AA        AA   YY      YY   22        22
CC            RR        RR  AA        AA    YY    YY             22
CC            RR        RR  AA        AA     YY  YY              22
CC            RRRRRRRRRRRR  AAAAAAAAAAAA      YYYY              22
CC            RRRRRRRRRRR   AAAAAAAAAAAA       YY              22
CC            RR    RR      AA        AA       YY            22
CC            RR     RR     AA        AA       YY          22
CC        CC  RR      RR    AA        AA       YY        22
CCCCCCCCCCCC  RR       RR   AA        AA       YY       222222222222
 CCCCCCCCCC   RR        RR  AA        AA       YY       222222222222
\end{verbatim}
\begin{verbatim}
****A  END  JOB  537  CRAY2     ROOM     5.22.50 PM 17 AUG 82  R6.PR1  SYS JES2  JOB  537  END  A****
****A  END  JOB  537  CRAY2     ROOM     5.22.50 PM 17 AUG 82  R6.PR1  SYS JES2  JOB  537  END  A****
****A  END  JOB  537  CRAY2     ROOM     5.22.50 PM 17 AUG 82  R6.PR1  SYS JES2  JOB  537  END  A****
****A  END  JOB  537  CRAY2     ROOM     5.22.50 PM 17 AUG 82  R6.PR1  SYS JES2  JOB  537  END  A****
****A  END  JOB  537  CRAY2     ROOM     5.22.50 PM 17 AUG 82  R6.PR1  SYS JES2  JOB  537  END  A****
****A  END  JOB  537  CRAY2     ROOM     5.22.50 PM 17 AUG 82  R6.PR1  SYS JES2  JOB  537  END  A****
\end{verbatim}
'''
# Faint pencil sketch below the reused listing.
s+=start()+paths('p','9.79,11.83 9.27,12.68 9.23,13.14 9.47,14.38;8.56,14.02 9.23,13.14 11.17,12.43;10.91,11.81 11.17,12.43 11.64,13.91;11.34,12.02 11.17,12.43 10.96,13.20 10.68,14.23;8.75,12.90 9.23,13.14 10.19,13.58 12.69,13.61;8.14,13.61 9.72,13.47 10.83,13.45 11.37,13.42')+paths('k,thin','9.16,12.70 9.29,12.69;11.13,12.28 11.20,12.31')+end()
# Lower-right strip with crossings, solid and dashed tracks, two arrow directions.
s+=start()+paths('g','15.28,16.34 17.53,16.28 21.49,16.28 24.15,16.32;15.62,17.06 17.97,17.08 18.99,16.70 20.07,16.35 21.08,16.47 21.48,16.73 22.08,17.05 25.22,17.00')+path('g','15.61,17.06 15.77,16.86 15.93,17.07')+paths('b,dashed,line width=1.7pt','15.28,16.60 19.00,16.67 21.49,16.62 25.01,16.50;21.66,16.78 24.94,16.81')+path('black!75!green,dashed,line width=1.2pt','15.61,16.98 17.98,16.99 19.00,16.70 20.07,16.35 24.16,16.35')+paths('w','15.28,16.72 18.99,16.70 21.48,16.69 24.73,16.57;16.11,15.21 16.16,16.03 16.31,16.72 16.69,18.84;16.87,14.74 16.31,16.72 15.76,18.74;18.68,14.14 18.92,15.44 18.99,16.70 19.16,18.43 19.49,19.36;19.52,14.13 19.33,15.57 18.99,16.70 18.76,17.98 18.52,19.64;21.51,14.58 21.48,16.69 21.42,18.68;23.61,14.85 23.53,16.69 23.44,18.74')+paths('k,thin,->','17.88,17.32 17.10,17.34;24.79,16.58 25.25,16.61')+end()
# Three adjoining oval cylinders and all visible internal curves.
s+=start()+path('g','4.40,18.12 4.71,17.58 5.56,17.11 6.12,17.21 6.89,17.80 6.92,19.91 6.80,20.27 5.73,20.65 4.96,20.61 4.43,20.24',True,True)+path('g','9.30,17.84 10.47,17.22 10.99,17.23 11.65,17.52 11.91,18.07 11.88,19.99 11.67,20.40 10.62,20.59 9.84,20.48 9.19,20.11',True,True)+path('g,dotted','6.89,17.80 7.55,17.15 8.19,17.00 8.78,17.22 9.30,17.84')
s+=path('w','6.89,17.80 7.56,17.18 8.13,17.10 8.79,17.33 9.30,17.84 9.19,20.11 8.73,20.52 7.91,20.69 6.80,20.27',True,True)
for reg in ['4.40,18.12 4.63,18.16 4.69,18.34','5.29,18.81 5.98,19.32 5.30,19.46','5.40,18.42 6.16,18.31 6.14,18.68','6.06,19.40 6.43,19.56 6.02,19.92','6.89,17.80 7.29,18.17 6.61,18.21','6.80,18.72 7.40,19.11 6.85,19.42','7.40,19.11 7.97,19.34 7.50,19.57','7.73,18.48 8.38,18.71 8.39,18.19','8.14,19.43 8.38,19.21 8.38,19.60','6.85,19.42 7.02,19.57 6.80,20.27','9.30,17.84 9.69,18.32 9.31,18.29','10.28,18.68 10.39,18.39 11.03,18.77','10.96,19.40 10.31,19.15 10.35,19.63','11.13,19.31 11.88,18.81 11.88,19.54','11.29,18.39 11.91,18.07 11.88,18.39']:
 s+=path('fill=orange!90!yellow,draw=none',reg,False,True)
s+=paths('w','4.40,18.12 5.40,18.42 6.80,18.72 7.40,19.11 8.14,19.43 9.28,19.65 10.35,19.63 11.13,19.31 11.88,18.81;4.40,18.12 5.29,18.81 5.98,19.32 7.02,19.57 7.50,19.57 8.38,19.21 9.37,18.55 10.39,18.39 11.29,18.39 11.91,18.07;4.43,19.08 5.40,18.42 6.16,18.31 6.61,18.21 7.29,18.17 7.73,18.48 8.38,18.71 9.31,18.29 9.69,18.32 10.28,18.68 11.03,18.77 11.88,18.39;4.43,19.44 5.30,19.46 5.98,19.32 6.80,18.72 7.73,18.48 8.39,18.19 9.31,18.29 10.31,19.15 10.96,19.40 11.88,19.83;4.43,19.65 4.80,20.02 5.47,20.06 6.02,19.92 6.43,19.56 6.85,19.42 7.50,19.57 7.71,19.99 8.44,20.11 9.19,20.11 10.16,20.07 10.87,19.84 11.13,19.31 11.51,18.36 11.91,18.07;5.56,17.11 5.29,18.31 5.29,18.81 5.30,19.46 5.47,20.06 5.57,20.66;5.98,17.18 6.17,18.21 6.14,18.68 6.06,19.40 6.02,19.92 5.73,20.65;8.01,17.12 7.80,18.12 7.73,18.48 7.40,19.11 7.50,19.57 7.91,20.69;8.33,17.14 8.42,18.33 8.38,19.21 8.38,19.60 8.21,20.68;10.47,17.22 10.27,18.12 10.28,18.68 10.31,19.15 10.35,19.63 10.37,20.58;10.99,17.23 11.07,18.10 11.03,18.77 10.96,19.40 10.87,19.84 10.62,20.59')
s+=paths('b,line width=2.4pt','5.56,17.11 6.12,17.21 6.89,17.80;5.73,20.65 6.36,20.47 6.80,20.27;9.30,17.84 10.08,17.34 10.47,17.22 10.99,17.23;9.19,20.11 9.84,20.48 10.37,20.58 10.62,20.59')+paths('black!75!green,line width=3pt','4.40,18.12 4.43,20.24 4.96,20.61 5.57,20.66;6.89,17.80 6.93,18.77 6.85,19.42 6.80,20.27;9.30,17.84 9.27,18.79 9.19,20.11;11.91,18.07 11.88,19.54')+path('b,thin','14.17,20.54 14.55,20.58 15.13,20.53')+end()+r'\margin{172}'+'\n'
(R/'pages/MPL_154_127-176_154_scan173.tex').write_text(s)
commit(173,[('text','upper printed numeric banner','0051 in repeated digits; twelve rows'),('text','middle printed banner','CRAY2; twelve rows'),('text','six repeated listing rows','END JOB 537 CRAY2 ROOM 5.22.50 PM 17 AUG 82'),('drawing','beneath listing left','faint pencil crossing and transversals'),('drawing','lower right','strip with red crossings and dashed tracks'),('drawing','bottom left','three adjoining oval cylinders with orange sectors'),('drawing','bottom middle','short blue stroke'),('margin note','bottom left','172')],sheet_kind='reused_typed',observations='Whole/a/b personally inspected and upper digit banner enlarged. All twelve rows of each banner and all six repeated job lines are written out. The first banner reads 0051 although the printed job number below is 537; it has not been corrected to agree. Two lower coloured drawings and the faint pencil sketch under the listing are reproduced; there is no prose in this scan.')
