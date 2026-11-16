import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from save_page import save
rows=r"""STMT NO. MESSAGE
-
5 IEF653I SUBSTITUTION JCL - DSN=SYS1.MACLIB,DISP=SHR
6 IEF653I SUBSTITUTION JCL - DSN=CNU1.MACLIB,DISP=SHR
20 IEF686I DDNAME REFERRED TO ON DDNAME KEYWORD IN PRIOR STEP WAS NOT RESOLVED
IEF236I ALLOC. FOR PREDONTA ASM
IEF237I 353 ALLOCATED TO SYSLIB
IEF237I 141 ALLOCATED TO
IEF237I 352 ALLOCATED TO
IEF237I VIO ALLOCATED TO SYSUT1
IEF237I VIO ALLOCATED TO SYSUT2
IEF237I VIO ALLOCATED TO SYSUT3
IEF237I JES2 ALLOCATED TO SYSPRINT
IEF237I DMY ALLOCATED TO SYSPUNCH
IEF237I 142 ALLOCATED TO SYSGO
IEF237I 351 ALLOCATED TO SYSIN
IEF142I PREDONTA ASM - STEP WAS EXECUTED - COND CODE 0008
IEF285I CNU2.MODULEF.UTIMS KEPT
IEF285I VOL SER NOS= SYSPPP.
IEF285I SYS1.MACLIB KEPT
IEF285I VOL SER NOS= SYSRES.
IEF285I CNU1.MACLIB KEPT
IEF285I VOL SER NOS= CNU001.
IEF285I SYS82155.T152706.RA000.PREDONTA.SYSUT1 DELETED
IEF285I SYS82155.T152706.RA000.PREDONTA.SYSUT2 DELETED
IEF285I SYS82155.T152706.RA000.PREDONTA.SYSUT3 DELETED
IEF285I JES2.JOB01085.\unsure{S00101|SO0101} SYSOUT
IEF285I SYS82155.T152706.RA000.PREDONTA.OBJSET PASSED
IEF285I VOL SER NOS= PUBL01.
IEF285I CNU2.MODULEF.UTIAS KEPT
IEF285I VOL SER NOS= CNU002.
IEF373I STEP /ASM / START 82155.1527
IEF374I STEP /ASM / STOP 82155.1527 CPU 0MIN 00.53SEC SRB 0MIN 00.01SEC VIRT 300K SYS 268K
CNU000I DETAIL EXCPS: 953----004 741----011 352----000 VIO----038 VIO----009 VIO----008 JES----??? JES----???
142----005 951----003

IEF202I PREDONTA LKED - STEP WAS NOT RUN BECAUSE OF CONDITION CODES
IEF272I PREDONTA LKED - STEP WAS NOT EXECUTED.
IEF373I STEP /LKED / START 82155.1527
IEF374I STEP /LKED / STOP 82155.1527 CPU 0MIN 00.00SEC SRB 0MIN 00.00SEC VIRT 0K SYS 0K

IEF237I 142 ALLOCATED TO SYS00001
IEF285I SYS82155.T152709.RA000.PREDONTA.R0000001 KEPT
IEF285I VOL SER NOS= PUBL01.
IEF285I SYS82155.T152706.RA000.PREDONTA.OBJSET DELETED
IEF285I VOL SER NOS= PUBL01.
IEF375I JOB /PREDONTA/ START 82155.1527
IEF376I JOB /PREDONTA/ STOP 82155.1527 CPU 0MIN 00.53SEC SRB 0MIN 00.01SEC""".splitlines()
tex=r"""
\diagram{\begin{tikzcd}
X \arrow[r,bend left=15,"g_0=\varphi i"] \arrow[r,bend right=15,"g_1=\unsure{\varphi|\psi}i"'] \arrow[d] & Y \arrow[d]\\
X' \arrow[r,bend left=20,"g'_0=g'"] \arrow[r,bend right=20,"g_1=p\unsure{\varphi|\psi}"'] & Y'
\end{tikzcd}}
\diagram{\begin{tikzcd}[row sep=large]
X \arrow[r,bend left=25,"g_0=\varphi i"{name=t}] \arrow[r,bend right=25,"g_1=g"'{name=b}] \arrow[d,very thick,"i"'] & \deleted{X}Y \arrow[d,"p"]\\
X' \arrow[ur,-,bend left=20,"\varphi"] \arrow[r,bend left=25,"g'_0=p\varphi"{name=u}] \arrow[r,bend right=25,"g'_1=g'"'{name=v}] & Y'
\arrow[from=t,to=b,"k"',shorten <=2pt,shorten >=2pt]
\arrow[from=b,to=t,shift right=7pt,shorten <=3pt,shorten >=3pt]
\arrow[from=u,to=v,"h"',shorten <=2pt,shorten >=2pt]
\end{tikzcd}}
"""
tex+='\\diagram{\\begin{array}{l}\n'+'\\\\\n'.join('\\texttt{'+s+'}' if s else '\\strut' for s in rows)+'\n\\end{array}}\n\\mspage{23}\n'
elements=[('diagram','upper handwriting','X,Y,X′,Y′; g0,g1,g′0,g1'),('diagram','lower handwriting','X,Y over X,X′,Y′; φ,k,h,i,p')]+[('text',f'printed row {i+1}',s) for i,s in enumerate(rows) if s]+[('text','corner','23')]
if __name__=='__main__':save(107,24,tex,elements,'reused_typed',notes='Two parallel-arrow homotopy squares on system-job output. The first has altered endpoint labels; preserve g′0=g′ and unprimed g1=pφ as ink, with φ/ψ doubt. The print spells SYSPPP clearly here; compare uncertain volume labels on preceding reused sheets only against their own images.')
