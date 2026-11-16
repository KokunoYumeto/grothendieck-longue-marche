import sys
sys.path.insert(0,'/workspace/scratch/4bbc351d3cab/MPL_106+107/scripts')
from save_page import save
rows=[
'end','disp cray1',
'//PREDONTA JOB CNU0000-PREDONT,MSGCLASS=A,TYPRUN=UIC',
'/*JOB=PREDONTA,ACCT=Y62200301',
'//PREDONTA JOB MSGLEVEL=(1,1)',
'//          EXEC CSSBATCH',
'//CRAYIN    DD *',
'JOB,JN=PREDONTA,T=9,TIO=9.','CFT.','LDR.','/EOF',
'      PROGRAM GUTS','      WRITE(6,1)',"    1 FORMAT(' BONJOUR')",'      STOP','      END','/*','//',
'205 //     space=(trk,(180,0,35),rlse)','l modulconv',
r'00010 //PREDONTA JOB CNU0049\#NODER-PREDONT,\deleted{CLASS=R,TIME=(0,3)}',
'00020 //JOBLIB DD DSN=CNU2.MODULEF.UTIA,DISP=SHR',
'00030 //ETAP1 EXEC PGM=FLIPFLOP',
'00040 //SYSUT1 DD DSN=CNU1.MODULEF.V33.INTERME1(MEFCOSDS),DISP=(OLD,PASS)',
r'00050 //SYSUT2 DD DSN=\&AUX,SPACE=(TRK,180),UNIT=SYSDA,DISP=(,PASS),',
'00060 // DCB=(RECFM=F,LRECL=80,BLKSIZE=80)',
'00070 //ETAP2 EXEC PGM=UPDATE,PARM=NEW,COND=(0,NE,ETAP1)',
'00080 //SYSPRINT DD DUMMY',
r'00090 //SYSIN DD DSN=\&AUX,DISP=(OLD,DELETE)',
r'00100 //SYSIN2 DD UNIT=SYSDA,SPACE=(CYL,\deleted{\unsure{4}}\inserted{6})',
'00110 //SYSUT2 DD DSN=CNU2.MODULEF.COSDS,',
'00120 // UNIT=SYSDA,DISP=(,CATLG,DELETE),SPACE=(TRK,(180,0,35),RLSE),',
'00130 // VOL=SER=SYSPFP,DCB=(RECFM=FB,LRECL=80,BLKSIZE=19040)',
'00140 //'
]
tex=r'\figure{\begin{tikzpicture}[x=.075cm,y=.16cm]'+'\n'
for i,line in enumerate(rows):tex+=r'\node[anchor=base west,inner sep=0pt,font=\tiny\ttfamily] at (0,'+str(-i)+') {'+line.replace(' ','\\ ')+'};\n'
tex+=r"""
\node[anchor=base west] at (-5,-20) {$(\ast$};
\draw[->,thick] (-2.5,-20)--(-.5,-20);
\node[anchor=base west] at (47,-18.8) {\inserted{REGION}};
\draw (53,-23) ellipse (3,.65);
\draw (34,-30) ellipse (3,.65);
\draw[->,thick] (-2.8,-29)--(-.5,-29);
\draw[->,thick] (-2.8,-33)--(-.5,-33);
\draw (1,-33.2)--(3,-32.6)--(3,-33.4) (5,-33.3)--(7,-32.8)--(7,-33.5) (8,-33.5)--(10,-33.0);
\end{tikzpicture}}
\mspage{8}
"""
elements=[('text',f'printed listing row {i}',line) for i,line in enumerate(rows)]+[('drawing','left of 00010','open parenthesis, asterisk, arrow'),('drawing','row 00040','oval around COSDS'),('drawing','row 00110','oval around COSDS'),('drawing','left of 00100 and clipped 00140','two arrows'),('drawing','clipped lower edge','three rising strokes'),('text','original foot','8')]
if __name__=='__main__':save(107,9,tex,elements,kind='reused_typed',notes='Reused job-control and Fortran printout. CLASS=R,TIME=(0,3) cancelled, REGION inserted above; numeral 6 overwrites a printed digit (tentatively 4). Last printed row is clipped after 00140 // and handwritten strokes are partly outside the photographed sheet. Only visible characters have been transcribed; no continuation supplied.')
