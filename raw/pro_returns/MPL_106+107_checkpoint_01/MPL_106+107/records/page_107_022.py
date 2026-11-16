import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from save_page import save
rows=[
('1','//PREDONTA JOB CNU0049-PREDONT,TIME=(0,3),CLASS=R','JOB 1085'),
('2','// EXEC ASMFCL','00000020'),
('3',"XXASMFCL PROC MAC='SYS1.MACLIB',MAC1='CNU1.MACLIB'",'00010071'),
('','*** REFER SYS1.PROCLIB(ASMFCL)','00020000'),
('','*** COMPID SYSTEM','00030000'),
('','*** DOC THIS PROCEDURE EXECUTES THE ASSEMBLER AND THE LINKAGE','00040000'),
('','*** EDITOR.','00050000'),
('','***','00060000'),
('4','XXASM EXEC PGM=IFOX00,PARM=OBJ','00070075'),
('5','//ASM.SYSLIB DD DSN=CNU2.MODULEF.UTIMS,DISP=SHR','00000030'),
('','X/SYSLIB DD DSN=&MAC,DISP=SHR','00080070'),
('6','// DD DSN=SYS1.MACLIB,DISP=SHR       -','00000040'),
('','X/ DD DSN=&MAC1,DISP=SHR','00090070'),
('7','// DD DSN=CNU1.MACLIB,DISP=SHR','00000050'),
('8','XXSYSUT1 DD DSN=&&SYSUT1,UNIT=VIO,SPACE=(CYL,(20,20))','00091076'),
('9','XXSYSUT2 DD DSN=&&SYSUT2,UNIT=VIO,SPACE=(CYL,(10,10))','00092076'),
('10','XXSYSUT3 DD DSN=&&SYSUT3,UNIT=VIO,SPACE=(CYL,(5,5))','00093076'),
('11','XXSYSPRINT DD SYSOUT=*,DCB=BLKSIZE=1089','00130072'),
('12','XXSYSPUNCH DD DUMMY','00140071'),
('13','XXSYSGO DD DSN=&&OBJSET,UNIT=SYSDA,SPACE=(80,(200,50)),','00150070'),
('','XX DISP=(MOD,PASS)','00160000'),
('14','//ASM.SYSIN DD DSN=CNU2.MODULEF.UTIAS(IAND),DISP=SHR','00000060'),
('15','XXLKED EXEC PGM=IEWL,PARM=(XREF,LET,LIST,NCAL),REGION=128K,','00170070'),
('','XX COND=(8,LE,ASM)','00180071'),
('16','XXSYSLIN DD DSN=&&OBJSET,DISP=(OLD,DELETE)','00190070'),
('17','XX DD DDNAME=SYSIN','00200070'),
('18','//LKED.SYSLMOD DD DSN=CNU2.MODULEF.UTIA(IAND),DISP=SHR','00000070'),
('','X/SYSLMOD DD DSN=&&GOSET(GO),UNIT=3350,SPACE=(1024,(50,20,1)),','00210073'),
('','XX DISP=(MOD,PASS)','00220000'),
('19','XXSYSUT1 DD DSN=&&SYSUT1,UNIT=VIO,SPACE=(1024,(50,20))','00230070'),
('20','XXSYSPRINT DD SYSOUT=*,DCB=(RECFM=FB,LRECL=121,BLKSIZE=1210)','00240072'),
('','//','00000080')]
esc=lambda s:s.replace('&',r'\&').replace('_',r'\_').replace('#',r'\#')
tex='\\diagram{\\begin{array}{rll}\n'+'\\\\\n'.join(r'\texttt{'+a+r'}&\texttt{'+esc(b)+r'}&\texttt{'+c+'}' for a,b,c in rows)+'\n\\end{array}}\n'
tex+=r"""
\diagram{\begin{tikzcd}
A \arrow[r,"\unsure{a}"] \arrow[d,very thick,"\mathrm{cof}"'] & X \arrow[d,very thick,"p"]\\
A\times I \arrow[r,"h"'] \arrow[ur,very thick] & Y
\end{tikzcd}}
\figure{\begin{tikzpicture}[scale=.55]
\draw (0,2.8) .. controls (-.9,1.4) and (-.3,.9) .. (.6,.7) .. controls (.8,1.6) and (.5,2.5) .. (0,2.8);
\draw[->,very thick] (.1,2.1)--(.1,1.4);
\draw[->] (-.1,.6) .. controls (-.6,-.2) and (-.2,-.6) .. (.5,-.6);
\draw (.45,.8) .. controls (.8,.1) and (.8,-.4) .. (.5,-.6);
\draw[->,very thick] (.2,.25)--(.2,-.3);
\end{tikzpicture}}
\margin{$\unsure{\mathrm{fib}}$}
\diagram{\begin{tikzcd}
A & X \arrow[l]\\
A^I \arrow[u,"\deleted{\unsure{\partial_1}}\partial_0"'] & Y \arrow[l,very thick] \arrow[u,very thick,"\mathrm{cofib.}"]
\end{tikzcd}}
\figure{\begin{tikzpicture}
\draw (0,0)--(.3,.8)--(.4,.4);
\node at (2,0) {$\unsure{Y_x}$};
\end{tikzpicture}}
\diagram{\begin{tikzcd}
A \arrow[r,very thick] \arrow[d,very thick] & X \arrow[d,very thick]\\
B \arrow[r] \arrow[ur,very thick] & Y
\end{tikzcd}}
\mspage{21}
"""
elements=[('text',f'printed row {i+1}',f'{a} {b} {c}') for i,(a,b,c) in enumerate(rows)]+[
('diagram','handwriting top left','A, X, A×I, Y; a,p,h,cof'),('drawing','right of first square','two loops with downward arrows'),('diagram','handwriting centre left','A, X, A^I, Y; ∂0,cofib.'),('drawing','below second square','angular stroke; Y_x'),('diagram','handwriting lower left','A, X, B, Y'),('text','lower corner','21')]
if __name__=='__main__':save(107,22,tex,elements,'reused_typed',notes='Three lifting diagrams on reused assembler listing; no accompanying prose. Preserve arrow directions in the dual square and the uncertain overwritten ∂ label.')
