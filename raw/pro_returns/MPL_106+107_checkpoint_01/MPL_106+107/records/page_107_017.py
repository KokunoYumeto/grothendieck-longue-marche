import sys
sys.path.insert(0,'/workspace/scratch/4bbc351d3cab/MPL_106+107/scripts')
from save_page import save
tex=r"""
\mspage{16}
\[
\underline{\operatorname{Hom}}(A,\underbrace{M}_{\text{stable par }\varinjlim})\simeq\underline{\operatorname{Hom}}_!(\widehat A,M)
\]
\margin{$!=\deleted{\unsure{tt}}\text{commutant aux }\varinjlim$}
\diagram{\begin{array}{l}
\underline{\operatorname{Hom}}(A^o,M)\simeq\underline{\operatorname{Hom}}_!(A^{o\wedge},M)\simeq\bigl(\underline{\operatorname{Hom}}^!(A^{o\wedge o}=\underbrace{A^{\vee o}}_{\text{\unsure{catégorie} stable par }\varprojlim},M^o)\bigr)^o\\
\rotatebox{90}{$\simeq$}\\
\underline{\operatorname{Hom}}(A,M^o)^o\simeq\bigl(\underline{\operatorname{Hom}}_!(\widehat A,M^o)\bigr)^o=\underline{\operatorname{Hom}}^!(A^{\wedge o},M)
\end{array}}
\[
\boxed{\deleted{\underline{\operatorname{Hom}}^!(A^{\vee o},M^o)\simeq\underline{\operatorname{Hom}}_!^{\unsure{g|?}}(\widehat A,M^o)}}
\]
\[
\operatorname{Hom}_!(A^\vee,M)^o\simeq\operatorname{Hom}_!(\widehat A,M^o)
\]
\[
\underline{\operatorname{Hom}}(A^o,M)\simeq\underline{\operatorname{Hom}}_!(A^{o\wedge},M)=\operatorname{Hom}_!(A^\vee,M)
\]
dual
\[\operatorname{Hom}(A,M^o)\simeq\operatorname{Hom}_!(\widehat A,M^o)\]
\figure{\begin{tikzpicture}\draw (0,0)--(5,-9);\end{tikzpicture}}
"""
rows=[
r'00010 //PREDONTA JOB CNU0049\#NODER-PREDONT,REGION=1500K,TYPRUN=SCAN',
'00015 /*JOBPARM L=30',
'00020 //JOBLIB DD DSN=CNU2.MODULEF.UTIA,DISP=SHR',
'00030 //ETAP1 EXEC PGM=FLIPFLOP',
'00040 //SYSUT1 DD DSN=CNU1.MODULEF.V33.INTERME1(MEFCOSDS),DISP=(OLD,PASS)',
r'00050 //SYSUT2 DD DSN=\&AUX,SPACE=(\unsure{\deleted{TRK}\inserted{CYL}|CYL},1\deleted{8}\inserted{6}),UNIT=SYSDA,DISP=(,PASS),',
'00060 // DCB=(RECFM=F,LRECL=80,BLKSIZE=80)',
'00070 //ETAP2 EXEC PGM=UPDATE,PARM=NEW,COND=(0,NE,ETAP1)',
'00080 //SYSPRINT DD DUMMY',
r'00090 //SYSIN DD DSN=\&AUX,DISP=(OLD,DELETE)',
'00100 //SYSIN2 DD UNIT=SYSDA,SPACE=(CYL,6)',
'00110 //SYSUT2 DD DSN=CNU2.MODULEF.COSDS,',
'00120 // UNIT=SYSDA,DISP=(,CATLG,DELETE),SPACE=(TRK,(180,0,35),RLSE),',
r'00130 // VOL=SER=SYS\unsure{PFP|PPP},DCB=(RECFM=FB,LRECL=80,BLKSIZE=19040)',
r'00170 //COMP       EXEC FORTXC,PARM=TERM,REGION=1500K\inserted{,COND=EVEN}',
r'00180 //FORT.SYSPRINT DD DSN=\&MESSYS,SPACE=(CYL,6),UNIT=SYSDA,DISP=(MOD,PASS)',
r'00190 //FORT.SYSTERM DD DSN=\&MESCOM,SPACE=(CYL,2),UNIT=SYSDA,DISP=(MOD,PASS)',
'00200 //SYSIN DD DSN=CNU1.MODULEF.V33.INTERME1(MEFCOSDS),DISP=OLD',
r'00210 //CUTR EXEC PGM=CUTTER\inserted{,COND=((0,NE,COMP.FORT),EVEN)}',
r'\deleted{00220 //STEPLIB DD DSN=CNU2.MODULEF.UTIA,DISP=SHR}',
r'00230 //TERMINAL DD DSN=\&MESCOM,DISP=(OLD,DELETE)',
r'00240 //OBJECT1 DD DSN=\&OBJ,DISP=(OLD,DELETE)',
r'00250 //SOURCE1 DD DSN=\&MESSYS,DISP=(OLD,DELETE)',
'00260 //SYSPRINT DD SYSOUT=*',
'00270 //SOURCE2 DD DUMMY',
r'00280 //OBJECT2 DD DSN=\&OBJ2,SPACE=(CYL,\deleted{\unsure{2}}\inserted{6}),UNIT=SYSDA,DISP=(MOD,PASS)',
r'00370 //LIEN EXEC FORTXL,\deleted{COND=(0,NE,CUTR)},PARM=NCAL\inserted{,COND=((0,NE,COMP.FORT),(0,NE,CUTR),EVEN)}',
r'00380 //LKED.SYSLIN DD DSN=\&OBJ2,DISP=(OLD,DELETE)',
'00390 //LKED.SYSLMOD DD DSN=CNU2.MODULEF.COSD,SPACE=(TRK,(180,0,35),RLSE),',
r'00400 // DCB=(RECFM=U,BLKSIZE=19040),UNIT=SYSDA,VOL=SER=SYS\unsure{PFP|PPP},DISP=(,CATLG)',
'00440 //'
]
tex+=r'\figure{\begin{tikzpicture}[x=.075cm,y=.22cm]'+'\n'
for i,line in enumerate(rows):tex+=r'\node[anchor=base west,inner sep=0pt,font=\tiny\ttfamily] at (0,'+str(-i)+') {'+line.replace(' ','\\ ')+'};\n'
for i in [5,19,25]:tex+='\\draw[->,thick](-3,'+str(-i)+')--(-.5,'+str(-i)+');\n'
tex+=r"""
\draw (48,-18)ellipse(1.4,.65);
\end{tikzpicture}}
"""
elements=[('text','upside-down corner','16'),('display','top','Hom(A,M) ~= Hom_!(Ahat,M)'),('margin note','top right','! = commutant aux lim'),('diagram','top two rows','Hom(Ao,M); Hom(A,Mo)o'),('display','boxed, struck','Hom^!(A vee o,Mo)'),('display','below box','Hom_!(A vee,M)o'),('display','lower mathematical row','Hom(Ao,M)'),('text','lower left','dual'),('display','last mathematical row','Hom(A,Mo)'),('drawing','diagonal across math and print','long diagonal rule')]+[('text',f'rotated printed row {i+1:02d}',row)for i,row in enumerate(rows)]+[('drawing','left of listing','three arrows'),('drawing','handwritten CUTR condition','oval around 0')]
if __name__=='__main__':save(107,17,tex,elements,kind='reused_typed',notes='Trial duality formulae with both upper and lower exclamation marks; checked against visible dots, not primes. Boxed identity explicitly struck out; long separate oblique rule crosses subsequent formulae into reused print. A vee and A hat differ visibly. The upper-right completion note is compressed. Printer insertions concern COND clauses; first space unit and overwritten digits uncertain. Printed volume looks PFP on this scan; consistency review retained for all reused listings.')
