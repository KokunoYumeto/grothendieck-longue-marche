import sys,re
sys.path.insert(0,'/workspace/scratch/4bbc351d3cab/MPL_106+107/scripts')
from save_page import save
zero=['           00000000','         0000000000','       00      0000','      00     00 00','     00    00  00','    00   00   00','   00  00    00','  00 00     00',' 0000      00','000       00','0000000000','00000000']
letters=[
['DDDDDDDDD','DDDDDDDDDD','DD       DD','DD        DD','DD        DD','DD        DD','DD        DD','DD        DD','DD        DD','DD       DD','DDDDDDDDDD','DDDDDDDDD'],
['OOOOOOOOOOOO','OOOOOOOOOOOO','OO        OO','OO        OO','OO        OO','OO        OO','OO        OO','OO        OO','OO        OO','OO        OO','OOOOOOOOOOOO','OOOOOOOOOOOO'],
[' CCCCCCCCCC','CCCCCCCCCCCC','CC        CC','CC','CC','CC','CC','CC','CC','CC        CC','CCCCCCCCCCCC',' CCCCCCCCCC'],
['UU        UU']*10+['UUUUUUUUUUUU',' UUUUUUUUUU'],
[' GGGGGGGGGG','GGGGGGGGGGGG','GG        GG','GG','GG','GG','GG     GGGGG','GG     GGGGG','GG        GG','GG        GG','GGGGGGGGGGGG',' GGGGGGGGGG'],
['RRRRRRRRRRR','RRRRRRRRRRRR','RR        RR','RR        RR','RR        RR','RRRRRRRRRRRR','RRRRRRRRRRR','RR    RR','RR     RR','RR      RR','RR       RR','RR        RR'],
[' AAAAAAAAAA','AAAAAAAAAAAA','AA        AA','AA        AA','AA        AA','AAAAAAAAAAAA','AAAAAAAAAAAA','AA        AA','AA        AA','AA        AA','AA        AA','AA        AA'],
[' 2222222222','222222222222','22        22','          22','          22','         22','       22','     22','   22',' 22','222222222222','222222222222']]
def art(blocks,offset):
    t=[r'\figure{\begin{tikzpicture}[x=.085cm,y=.14cm]']
    for k,block in enumerate(blocks):
        for row,line in enumerate(block):
            for m in re.finditer(r'\S+',line):
                t.append(r'\node[anchor=base west,inner sep=0pt,font=\tiny\ttfamily] at ('+str(offset*k+m.start())+','+str(-row)+') {'+m.group()+'};')
    t.append(r'\end{tikzpicture}}')
    return '\n'.join(t)
tex=r'\texttt{//*\quad DOCUGRA20005}\qquad\unsure{\texttt{I}|\texttt{1}}'+'\n\n'+art([zero]*4,14)+'\n\n'+art(letters,14)+'\n\n'
line=r'\texttt{****A\quad START\quad JOB\quad 5\quad DOCUGRA2\qquad ROOM\qquad 2.24.59 PM 24 AUG 82\quad R6.PR1\quad SYS JES2\quad JOB\quad 5\quad START\quad A****}'
tex+='\n\n'.join([line]*6)+'\n\n'+r'\texttt{DERNIERE MISE A JOUR DE JOURNAL : 11-08-82}'+'\n\n'+r'\figure{\begin{tikzpicture}\draw (0,0)--(1.1,0.03);\end{tikzpicture}}'+'\n'+r'\mspage{4}'
elements=[('text','top after rotation','//* DOCUGRA20005 I'),('drawing','upper printed banner','four zero-shaped arrangements of printed 0'),('drawing','middle printed banner','DOCUGRA2 formed from repeated characters')]
for i in range(6):elements.append(('text',f'printed job line {i+1}','****A START JOB 5 DOCUGRA2 ROOM 2.24.59 PM 24 AUG 82 R6.PR1 SYS JES2 JOB 5 START A****'))
elements += [('text','below job lines','DERNIERE MISE A JOUR DE JOURNAL : 11-08-82'),('drawing','right edge of printed banner','short line'),('text','original lower left','4')]
notes='''Reused computer job separator sheet with no mathematical prose. The printed job timestamp is “2.24.59 PM 24 AUG 82”; the journal update is “11-08-82”. These date the reused paper and are not an explicit date of the handwriting. The printed banner reads DOCUGRA2; manuscript/archival pencil number 4 at the foot in the scan orientation. O and 0 are close in this typeface; the zero art and letter O art are represented literally in TikZ.'''
if __name__=='__main__':save(106,5,tex,elements,kind='reused_typed',notes=notes)
