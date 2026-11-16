import sys
sys.path.insert(0,'/workspace/scratch/4bbc351d3cab/MPL_106+107/scripts')
from save_page import save
rows=[
'l modulef5',
r'00010 //\unsure{PREDONTA|PREDDNTA} JOB CNU0049\unsure{\#|\&}NODER-PREDONT,REGION=1500K',
'00020 /*JOBPARM L=30',
'00030 //COMP       EXEC FORTXC,PARM=TERM,REGION=1500K',
r'00040 //FORT.SYSPRINT DD DSN=\&MESSYS,SPACE=(CYL,\unsure{\deleted{0}}\inserted{6}),UNIT=SYSDA,DISP=(MOD,PASS)',
r'00050 //FORT.SYSTERM  DD DSN=\&MESCOM,SPACE=(CYL,\unsure{\deleted{0}}\inserted{3}),UNIT=SYSDA,DISP=(MOD,PASS)',
'00060 //SYSIN    DD DSN=CNU1.MODULEF.V33.INTERME1(MEFCOSDS),DISP=OLD',
'00080 //    EXEC PGM=CUTTER',
'00080 //STEPLIB  DD DSN=CNU2.MODULEF.UTIA,DISP=SHR',
r'00090 //TERMINAL DD DSN=\&MESCOM,DISP=(OLD,DELETE)',
r'00100 //OBJECT1  DD DSN=\&OBJ,DISP=(OLD,DELETE)',
r'00110 //SOURCE1  DD DSN=\&MESSYS,DISP=(OLD,DELETE)',
'00120 //SYSPRINT DD SYSOUT=*',
r'00130 //SOURCE2  DD \deleted{DSN=\&SOURCE,SPACE=(CYL,4),UNIT=SYSDA,DISP=(MOD,PASS)}',
r'00140 //OBJECT2  DD DSN=\&OBJ2,SPACE=(CYL,3),UNIT=SYSDA,DISP=(MOD,PASS)',
'00150 //UPDT    EXEC PGM=UPDATE,COND=(0,NE,CUTR),PARM=NEW',
'00160 //STEPLIB DD DSN=CNU2.MODULEF.UTIA,DISP=SHR',
r'00170 //SYSIN   DD DSN=\&SOURCE,DISP=(OLD,DELETE)',
'00180 //SYSIN2 DD UNIT=SYSDA,SPACE=(CYL,4)',
'00190 //SYSUT2 DD DSN=CNU2.MODULEF.COSDS,DISP=(,CATLG),',
'00200 //      DCB=(RECFM=FB,LRECL=80,BLKSIZE=19040),UNIT=SYSDA,',
'00205 //      SPACE=(TRK,(180,0,35),RLSE),VOL=SER=SYSPFP',
'00210 //SYSPRINT DD DUMMY',
'00220 //LIEN      EXEC FORTXL,COND=(0,NE,CUTR),PARM=NCAL',
r'00230 //LKED.SYSLIN  DD DSN=\&OBJ2,DISP=(OLD,DELETE)',
'00240 //LKED.SYSLMOD DD DSN=CNU2.MODULEF.COSD,SPACE=(TRK,(180,0,35),RLSE),',
'00250 //  DCB=(RECFM=U,BLKSIZE=19040),UNIT=SYSDA,VOL=SER=SYSPFP,DISP=(,CATLG)',
'00260 //FIN   EXEC PGM=IEFBR14,COND=((0,EQ,UPDT),(4,GE,LIEN.LKED),EVEN)',
'00270 //SOURCE DD DSN=CNU2.MODULEF.CONVS,DISP=(OLD,DELETE)',
'00280 //MODEX  DD DSN=CNU2.MODULEF.CONV,DISP=(OLD,DELETE)',
'00290 //'
]
tex=r'\figure{\begin{tikzpicture}[x=.075cm,y=.16cm]'+'\n'
for i,line in enumerate(rows):tex+=r'\node[anchor=base west,inner sep=0pt,font=\tiny\ttfamily] at (0,'+str(-i)+') {'+line.replace(' ','\\ ')+'};\n'
tex+=r"""
\draw[->] (-3,-4)--(-.5,-4);
\draw[->] (-3,-5)--(-.5,-5);
\draw[->] (-3,-13)--(-.5,-13);
\draw (1, -.4) .. controls (-1,-.6) and (-1,-1.7) .. (1,-2.2);
\draw (1,-2.2) .. controls (4,-2.5) and (4,-.5) .. (4,-.5);
\draw (9,-2) .. controls (11,1) and (12,-2) .. (13,-1) .. controls (14,1) and (15,-3) .. (16,-1) .. controls (17,1) and (18,-2) .. (19,-1) .. controls (20,1) and (21,-3) .. (22,-1) .. controls (23,-3) and (24,1) .. (25,-1) .. controls (26,-.8) and (40,-.5) .. (48,-1);
\draw[<-] (74,-13)--(75,-13);
\draw (54,-6) ellipse (3,.52);
\node[anchor=base,font=\small] at (56,-12.4) {\inserted{dummy}};
\draw (-.3,-14.6)--(45,-14.6);
\draw (-.3,-14.6) .. controls (-1,-17) and (-1,-21.5) .. (-.3,-22.4);
\draw (-.3,-22.4)--(58,-22.4);
\draw (0,-20) .. controls (8,-14) and (16,-13) .. (18,-19) .. controls (19,-23) and (26,-18) .. (32,-18) .. controls (36,-18) and (39,-16) .. (44,-16) .. controls (46,-16) and (45,-20.5) .. (48,-20);
\end{tikzpicture}}
\mspage{6}
"""
elements=[('text',f'listing row {i}',line) for i,line in enumerate(rows)]+[('drawing','listing rows 00010–00020','left enclosure and wavy stroke'),('drawing','left of rows 00040,00050,00130','three arrows'),('drawing','row 00060','oval around COSDS'),('drawing','rows 00150–00210','bracket and curved crossing line'),('text','original foot','6')]
if __name__=='__main__':save(107,7,tex,elements,kind='reused_typed',notes='Reused job-control listing, handwritten 6 and 3 overwriting printed digits, source declaration struck and “dummy” inserted; several circled/bracketed records. No mathematical prose. Two successive row numbers 00080 retained exactly. Distinguish COSDS and COSD file labels, and the paper’s annotations from manuscript mathematical assertions.')
