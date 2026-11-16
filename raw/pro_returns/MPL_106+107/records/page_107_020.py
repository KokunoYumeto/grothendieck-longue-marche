import sys
sys.path.insert(0,'/workspace/scratch/4bbc351d3cab/MPL_106+107/scripts')
from save_page import save
header='J E S 2  J O B  L O G  --  S Y S T E M  J E S 2  --  N O D E  C N U'
body=[
('15.27.06','IEF677I WARNING MESSAGE(S) FOR JOB PREDONTA ISSUED'),
('15.27.06',r'\$HASP373 PREDONTA STARTED - INIT 1 - CLASS R - SYS JES2'),
('15.27.09','CNU000I: STEP=ASM     CODE-RETOUR=0008'),
('15.27.09','CNU000I: STEP=LKED    NON EXECUTE'),
('15.27.09',''),
('15.27.09','+*--------- CONSOMMATION RESSOURCES CENTRALES ----------+'),
('15.27.09','+ STEPNAME +   CPU   + MEMOIRE +   EXCP   + TERME CE  +'),
('15.27.09','+----------+---------+---------+----------+-----------+'),
('15.27.09','+ ASM      +   0.53  +   300K  +    078   +   2.72    +'),
('15.27.09','+ LKED     +   0.00  +   000K  +    000   +   0.00    +'),
('15.27.09','                                             ========='),
('15.27.09','                 - TOTAL TERMES CE -------->    2.72'),
('15.27.09',''),
('15.27.09','+------------ C.N.U.S.C. VENDR. 04 JUIN 82 ------------+'),
('15.27.09','+             DETAIL DES COUTS DE CE CALCUL            +'),
('15.27.09','+    NATURE    + NOMBRE  + COUT UNIT. + COUT TOTAL      +'),
('15.27.09','+-------------+---------+------------+-----------------+'),
('15.27.09','+ PRISE CHARGE +      1 +       2.10 +     2.10  FRS +'),
('15.27.09','+ TERMES CE    +   2.72 +     0.1000 +     0.27  FRS +'),
('15.27.09','+ CARTES LUES  +    009 +     0.0025 +     0.02  FRS +'),
('15.27.09','+ LIGNES IMPR. +    109 +     0.0000 +     0.00  FRS +'),
('15.27.09','+ CARTES PERF. +    000 +     0.0620 +     0.00  FRS +'),
('15.27.09','                                        ==========='),
('15.27.09','TOTAL IMPUTE AU COMPTE CNU0049 -------->      2.39 FRS'),
('15.27.09',''),
('15.27.09',r'\$HASP395 PREDONTA ENDED')
]
rows=[header]+[tm+' JOB 1085  '+line for tm,line in body]
tex=r'\figure{\begin{tikzpicture}[x=.08cm,y=.24cm]'+'\n'
for i,line in enumerate(rows):tex+=r'\node[anchor=base west,inner sep=0pt,font=\tiny\ttfamily] at (0,'+str(-i)+') {'+line.replace(' ','\\ ')+'};\n'
tex+=r"""
\end{tikzpicture}}
\diagram{\begin{tikzcd}\Delta\arrow[d,very thick]\\{}\end{tikzcd}}
\mspage{19}
"""
elements=[('text',f'rotated printed row {i+1:02d}',row)for i,row in enumerate(rows)]+[('diagram','below listing original left','Delta downward arrow, blank target'),('text','foot left','19')]
if __name__=='__main__':save(107,20,tex,elements,kind='reused_typed',notes='Full reused JES2 job log: job 1085, ASM return 0008, LKED not executed, resource/cost tables, Friday 04 June 82, total 2.39 FRS. Only added mathematical mark is Delta and a heavy downward arrow with blank target. Handwritten page number 19.')
