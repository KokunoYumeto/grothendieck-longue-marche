import sys
sys.path.insert(0,'/workspace/scratch/4bbc351d3cab/MPL_106+107/scripts')
from save_page import save
rows=[
r'00010 //PREDONTA JOB CNU0049\#NODER-PREDONT,REGION=6000K,TYPRUN=SCAN',
'00020 /*JOBPARM L=30',
'00030 //JOBLIB    DD DSN=CNU2.MODULEF.UTIA,DISP=SHR',
'00040 //ETAP1    EXEC PGM=FLIPFLOP',
'00050 //SYSUT1    DD DSN=CNU1.MODULEF.V33.INTERME1(MEFCYGNS),DISP=(OLD,PASS)',
r'00060 //SYSUT2    DD DSN=\&AUX,SPACE=(CYL,24),UNIT=SYSDA,DISP=(,PASS),',
'00070 //            DCB=(RECFM=FB,LRECL=80,BLKSIZE=19040)',
'00080 //ETAP2    EXEC PGM=IEBUPDTE,PARM=NEW,COND=(0,NE,ETAP1)',
'00090 //SYSPRINT  DD DUMMY',
r'00100 //SYSIN     DD DSN=\&AUX,DISP=(OLD,DELETE)',
'00110 //SYSUT2    DD DSN=CNU2.MODULEF.CYGNS,UNIT=SYSDA,DISP=(,CATLG,DELETE),',
r'00120 //            SPACE=(TRK,(180,0,35),RLSE),VOL=SER=SYS\unsure{PPP|PFP},',
'00130 //            DCB=(RECFM=FB,LRECL=80,BLKSIZE=19040)',
'00140 //COMP     EXEC FORTXC,PARM=TERM,REGION=6000K',
r'00150 //FORT.SYSPRINT DD DSN=\&MESSYS,UNIT=SYSDA,DISP=(MOD,PASS),',
'00160 //            SPACE=(CYL,24),',
r'00170 //FORT.SYSTERM  DD DSN=\&MESCOM,UNIT=SYSDA,DISP=(MOD,PASS),',
'00180 //            SPACE=(CYL,12)',
'00190 //SYSIN     DD DSN=CNU1.MODULEF.V33.INTERME1(MEFCYGNS),DISP=OLD',
'00200 //CUTR     EXEC PGM=CUTTER,COND=(0,NE,COMP.FORT)',
r'00210 //TERMINAL  DD DSN=\&MESCOM,DISP=(OLD,DELETE)',
r'00220 //OBJECT1   DD DSN=\&OBJ,DISP=(OLD,DELETE)',
r'00230 //SOURCE1   DD DSN=\&MESSYS,DISP=(OLD,DELETE)',
'00240 //SYSPRINT  DD SYSOUT=*',
'00250 //SOURCE2   DD DUMMY',
r'00260 //OBJECT2   DD DSN=\&OBJ2,SPACE=(CYL,24),UNIT=SYSDA,DISP=(MOD,PASS),',
r'00270 //LIEN     EXEC FORTXL,COND=((\deleted{0,NE},COMP.FORT),(0,NE,CUTR)),',
'00280 //            PARM=NCAL',
r'00290 //LKED.SYSLIN DD DSN=\&OBJ2,DISP=(OLD,DELETE)',
'00300 //LKED.SYSLMOD DD DSN=CNU2.MODULEF.CYGN,SPACE=(TRK,(180,0,35),RLSE),',
r'00310 //           DCB=(RECFM=U,BLKSIZE=19069),UNIT=SYSDA,VOL=SER=SYS\unsure{PPP|PFP},',
'00320 //            DISP=(,CATLG,DELETE)',
'00330 //'
]
tex=r'\figure{\begin{tikzpicture}[x=.075cm,y=.18cm]'+'\n'
for i,line in enumerate(rows):tex+=r'\node[anchor=base west,inner sep=0pt,font=\tiny\ttfamily] at (0,'+str(-i)+') {'+line.replace(' ','\\ ')+'};\n'
tex+=r"""
\draw[->] (-3,-14)--(-.5,-14);
\draw[->] (-3,-16)--(-.5,-16);
\draw[->] (-3,-19)--(-.5,-19);
\draw[->] (-3,-25)--(-.5,-25);
\node[anchor=base west,font=\scriptsize] at (38,-15) {\inserted{DCB=BLKSIZE=19047}};
\node[anchor=base west,font=\scriptsize] at (38,-17) {\inserted{,DCB=BLKSIZE=18 997}};
\node[anchor=base west,font=\scriptsize] at (70,-17.4) {\inserted{// FORT.SYSUT1 $\unsure{\sqcup}$ DD $\unsure{\sqcup}$ DCB=BLKSIZE=19006}};
\draw[<-] (69,-17.3)--(71,-17.3);
\node[anchor=base west,font=\scriptsize] at (61,-19.5) {\inserted{(4,LT,COMP.FORT)}};
\node[anchor=base west,font=\scriptsize] at (77,-25) {\inserted{DCB=BLKSIZE=19040}};
\node[anchor=base west,font=\scriptsize] at (36,-27) {\inserted{4,LT}};
\end{tikzpicture}}
\mspage{10}
"""
elements=[('text',f'printed listing row {i+1:02d}',line) for i,line in enumerate(rows)]+[('drawing','left of 00150,00170,00200,00260','four arrows'),('drawing','right of 00180','left arrow by added FORT.SYSUT1 record'),('text','original foot','10')]
if __name__=='__main__':save(107,11,tex,elements,kind='reused_typed',notes='Full reused 33-line job-control listing. Handwritten DCB block-size additions read 19047, 18 997, 19006, 19040; these are not normalized to the printed block sizes. Conditional 0,NE in 00270 cancelled with 4,LT beneath; a parenthetic alternative condition lies beside 00200. Blank-space-like marks in added FORT.SYSUT1 record represented with doubtful sqcup signs. SYS volume identifier letters P/F remain doubtful. No mathematical assertions.')
