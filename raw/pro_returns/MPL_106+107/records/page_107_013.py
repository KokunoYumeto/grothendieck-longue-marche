import sys
sys.path.insert(0,'/workspace/scratch/4bbc351d3cab/MPL_106+107/scripts')
from save_page import save
rows=[
r'00010 //PREDONTA JOB CNU0049\#NODER-PREDONT,REGION=1500K,TYPRUN=SCAN',
'00020 /*JOBPARM L=30',
'00030 //JOBLIB DD DSN=CNU2.MODULEF.UTIA,DISP=SHR',
'00040 //ETAP1 EXEC PGM=FLIPFLOP',
'00050 //SYSUT1 DD DSN=CNU1.MODULEF.V33.INTERME1(MEFCOSDS),DISP=(OLD,PASS)',
r'00060 //SYSUT2 DD DSN=\&AUX,SPACE=(CYL,6),UNIT=SYSDA,DISP=(,PASS),',
'00070 // DCB=(RECFM=F,LRECL=80,BLKSIZE=80)',
'00080 //ETAP2 EXEC PGM=UPDATE,PARM=NEW,COND=(0,NE,ETAP1)',
'00090 //SYSPRINT DD DUMMY',
r'00100 //SYSIN DD DSN=\&AUX,DISP=(OLD,DELETE)',
'00110 //SYSIN2 DD UNIT=SYSDA,SPACE=(CYL,6)',
'00120 //SYSUT2 DD DSN=CNU2.MODULEF.COSDS,',
'00130 // UNIT=SYSDA,DISP=(,CATLG,DELETE),SPACE=(TRK,(180,0,35),RLSE),',
r'00140 // VOL=SER=SYS\unsure{PPP|PFP},DCB=(RECFM=FB,LRECL=80,BLKSIZE=19040)',
r'00150 //COMP       EXEC FORTXC,PARM=TERM,REGION=500K,\deleted{COND=EVEN}',
r'00160 //FORT.SYSPRINT DD DSN=\&MESSYS,SPACE=(CYL,6),UNIT=SYSDA,DISP=(MOD,PASS)',
r'00170 //FORT.SYSTERM  DD DSN=\&MESCOM,SPACE=(CYL,\deleted{\unsure{3}}\inserted{2}),UNIT=SYSDA,DISP=(MOD,PASS)',
'00180 //SYSIN    DD DSN=CNU1.MODULEF.V33.INTERME1(MEFCOSDS),DISP=OLD',
r'00190 //CUTR    EXEC PGM=CUTTER,COND=((0,NE,COMP.FORT),\deleted{EVEN})',
r'00200 //TERMINAL DD DSN=\&MESCOM,DISP=(OLD,DELETE)',
r'00210 //OBJECT1  DD DSN=\&OBJ,DISP=(OLD,DELETE)',
r'00220 //SOURCE1  DD DSN=\&MESSYS,DISP=(OLD,DELETE)',
'00230 //SYSPRINT DD SYSOUT=*',
'00240 //SOURCE2  DD DUMMY',
r'00250 //OBJECT2  DD DSN=\&OBJ2,SPACE=(CYL,6),UNIT=SYSDA,DISP=(MOD,PASS)',
r'00260 //LIEN       EXEC FORTXL,COND=((0,NE,COMP.FORT),(0,NE,CUTR),\deleted{EVEN}),',
'00270 //            PARM=NCAL',
r'00280 //LKED.SYSLIN  DD DSN=\&OBJ2,DISP=(OLD,DELETE)',
'00290 //LKED.SYSLMOD DD DSN=CNU2.MODULEF.COSD,SPACE=(TRK,(180,0,35),RLSE),',
r'00300 //  DCB=(RECFM=U,BLKSIZE=19040),UNIT=SYSDA,VOL=SER=SYS\unsure{PPP|PFP},DISP=(,CATLG\deleted{)}\inserted{,DELETE)}',
'00310 //'
]
tex=r'\figure{\begin{tikzpicture}[x=.075cm,y=.18cm]'+'\n'
for i,line in enumerate(rows):tex+=r'\node[anchor=base west,inner sep=0pt,font=\tiny\ttfamily] at (0,'+str(-i)+') {'+line.replace(' ','\\ ')+'};\n'
for i in [5,10,14,15,18,24,25]:tex+='\\draw[->,thick] (-3,'+str(-i)+')--(-.5,'+str(-i)+');\n'
for y,xend in [(-2.6,66),(-6.6,74),(-13.6,69),(-17.6,77),(-24.6,85)]:tex+='\\draw (-1,'+str(y)+')--('+str(xend)+','+str(y)+');\n'
tex+=r"""
\draw (38,-5) ellipse (1.4,.8);
\draw (39.5,-10) ellipse (1.2,.85);
\draw (48,-15) ellipse (1.5,.9);
\draw (41,-24) ellipse (1.4,1.05);
\node[anchor=base west,font=\scriptsize] at (42,-22.8) {\inserted{24}};
\end{tikzpicture}}
\mspage{12}
"""
elements=[('text',f'printed listing row {i+1:02d}',line) for i,line in enumerate(rows)]+[('drawing','left of 00060,00110,00150,00160,00190,00250,00260','seven arrows'),('drawing','after 00030,00070,00140,00180,00250','five horizontal rules'),('drawing','digits in 00060,00110,00160,00250','four ovals'),('text','original foot','12')]
if __name__=='__main__':save(107,13,tex,elements,kind='reused_typed',notes='Another reused 31-line job-control listing. Circled printed 6s are not silently deleted; 24 is added above the last. Printed digit in SYSTERM space field overwritten by handwritten 2, underlying 3 doubtful. Three EVEN conditions struck, final DELETE added to disposition. Seven left arrows and five rules reproduce grouping. No mathematical text.')
