import sys,importlib.util
sys.path.insert(0,'/workspace/scratch/4bbc351d3cab/MPL_106+107/scripts')
from save_page import save
spec=importlib.util.spec_from_file_location('banner','MPL_106+107/records/page_106_005.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
letters=[m.letters[4],m.letters[3],['TTTTTTTTTTTT','TTTTTTTTTTTT']+['     TT']*10,[' SSSSSSSSSS','SSSSSSSSSSSS','SS        SS','SS','SSS',' SSSSSSSSS','  SSSSSSSSS','         SSS','          SS','SS        SS','SSSSSSSSSSSS',' SSSSSSSSSS']]
tex=m.art(letters,14)+'\n\n'
line=r'\texttt{****P\quad END\quad STC\quad 21\quad GUTS\qquad ROOM\qquad 3.31.25 PM 04 JUN 82\quad R6.PR1\quad SYS JES2\quad STC\quad 21\quad END\quad P****}'
tex+=r'\figure{\begin{tikzpicture}\draw (0,0)--(.015,.25);\fill (.01,-.08) circle (.012);\end{tikzpicture}}'+'\n'+'\n\n'.join([line]*6)+'\n'+r'\mspage{4}'
elements=[('drawing','between T and S near baseline','short vertical mark and dot'),('drawing','centre after rotation','GUTS in twelve rows of repeated characters')]+[('text',f'printed record {i+1}','****P END STC 21 GUTS ROOM 3.31.25 PM 04 JUN 82 R6.PR1 SYS JES2 STC 21 END P****') for i in range(6)]+[('text','original lower left','4')]
if __name__=='__main__':save(107,5,tex,elements,kind='reused_typed',notes='Printed GUTS separator; no handwritten mathematics. Six END records dated 3.31.25 PM 04 JUN 82. Foot number 4. Date is evidence about reused paper only.')
