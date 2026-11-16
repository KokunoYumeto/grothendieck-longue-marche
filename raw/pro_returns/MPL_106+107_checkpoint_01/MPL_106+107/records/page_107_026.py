import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from save_page import save
rows=[
['000000','','','','1','IAND START','','IAND...1'],
['','','','','2','$SAVE OPTION=FUN','','IAND...2'],
['000000','','','','3+','CNOP 0,4','','$SAVE.91'],
['','','','00000','4+','USING *,15','','$SAVE.92'],
['000000','47F0 F00C','0000C','','5+','BC 15,*+12','','$SAVE.94'],
['000004','04','','','6+','DC AL1(4)','','$SAVE.95'],
['000005','C9C1D5C4404040','','','7+',"DC CL7'IAND'",'','$SAVE.96'],
['00000C','90EC D00C','0000C','','8+','STM 14,12,12(13)','','$SAVE.97'],
['000010','182D','','','9+','LR 2,13','','$SAVE.99'],
['000012','98DE F020','00020','','10+','LM 13,14,*+14','','$SAV.100'],
['000016','5020 D004','00004','','11+','ST 2,4(0,13)','','$SAV.101'],
['00001A','50D0 2008','00008','','12+','ST 13,8(0,2)','','$SAV.102'],
['00001E','07FE','','','13+','BCR 15,14','','$SAV.103'],
['000020','00000028','','','14+','DC A(SAV0001A)','','$SAV.104'],
['000024','00000070','','','15+','DC A(*+76)','','$SAV.106'],
['','','','','16+','DROP 15','','$SAV.107'],
['','','','00028','17+','USING *,13','','$SAV.109'],
['000028','00000000','','','18+','SAV0001A DC A(SAV0001B)','','$SAV.110'],
['','*** ERROR ***','','','','','',''],
['00002C','','','','19+','DS 17F','','$SAV.111'],
['000070','5821 0000','00000','','20','L 2,0(1)','','IAND...3'],
['000074',r'\unsure{5802|5302} 0000','00000','','21','L 0,0(2)','','IAND...4'],
['000078','5821 0004','00004','','22','L 2,4(1)','','IAND...5'],
['00007C','5402 0000','00000','','23','N 0,0(2)','','IAND...6'],
['','','','','24','RETURN','','IAND...7'],
['000080','07FE','','','25+','BR 14','RETURN','02000000'],
['','','','','26','END','','IAND...8']]
tex=r"""\hfill\texttt{PAGE 2}
\texttt{LOC OBJECT CODE ADDR1 ADDR2 STMT SOURCE STATEMENT}\hfill\texttt{ASM 0201 15.27 06/04/82}
"""
tex+='\\diagram{\\begin{array}{llllllll}\n'+'\\\\\n'.join('&'.join('\\texttt{'+s.replace('$',r'\$')+'}' for s in row) for row in rows)+'\n\\end{array}}\n'
tex+=r"""
\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw[red!60!black] (0,0)..controls(.4,-.17)and(.8,.16)..(1.5,.04)--(1.5,.22)..controls(1,-.07)and(.4,.02)..(.2,.02);
\draw[red!60!black] (.1,-.06)..controls(.5,-.2)and(1,.03)..(1.5,-.04);
\end{tikzpicture}}
\mspage{25}
"""
elements=[('text','printed header','PAGE 2'),('text','printed columns','LOC OBJECT CODE ADDR1 ADDR2 STMT SOURCE STATEMENT; ASM 0201 15.27 06/04/82')]+[('text',f'printed row {i+1}',' '.join(row)) for i,row in enumerate(rows)]+[('drawing','under A(SAV0001B)','red doubled curved underline and angular endpoint'),('text','corner','25')]
if __name__=='__main__':save(107,26,tex,elements,'reused_typed',notes='Assembler listing, PAGE 2, printed date 06/04/82, manuscript foliation 25; no further mathematical prose. Red mark beneath A(SAV0001B) retained separately in TikZ.')
