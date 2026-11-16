from page_106_005 import art
import sys
sys.path.insert(0,'/workspace/scratch/4bbc351d3cab/MPL_106+107/scripts')
from save_page import save
letters=[
['PPPPPPPPPPPP']+['PP        PP']*3+['PPPPPPPPPPPP','PPPPPPPPPPP']+['PP']*5,
['LL']*9+['LLLLLLLLLLLL']*2,
['OOOOOOOOOOOO']+['OO        OO']*8+['OOOOOOOOOOOO']*2,
['TTTTTTTTTTTT']+['     TT']*10,
['EEEEEEEEEEEE']+['EE']*3+['EEEEEEEE']*2+['EE']*3+['EEEEEEEEEEEE']*2,
['DDDDDDDDDD','DD       DD']+['DD        DD']*7+['DDDDDDDDDD','DDDDDDDDD'],
['IIIIIIIIII']+['    II']*8+['IIIIIIIIII']*2,
['TTTTTTTTTTTT']+['     TT']*10]
tex=art(letters,14)+'\n\n'
line=r'\texttt{****A\quad END\quad JOB 7747\quad PLOTEDIT\qquad ROOM\qquad 8.39.37 AM 25 AUG 82\quad R6.PR1\quad SYS JES2\quad JOB 7747\quad END\quad A****}'
tex+='\n\n'.join([line]*6)+'\n\n'+r'\mspage{6}'
elements=[('drawing','upper edge after rotation','PLOTEDIT character banner, eleven visible rows')]
for i in range(6):elements.append(('text',f'printed line {i+1}','****A END JOB 7747 PLOTEDIT ROOM 8.39.37 AM 25 AUG 82 R6.PR1 SYS JES2 JOB 7747 END A****'))
elements.append(('text','original lower left','6'))
if __name__=='__main__':save(106,7,tex,elements,kind='reused_typed',notes='Printed PLOTEDIT separator; the character banner is clipped at the scan edge and only eleven visible rows are represented. Six repeated job-ending records have timestamp 8.39.37 AM 25 AUG 82. Pencil sheet number 6; no mathematical writing. The printing date does not establish the date of manuscript composition.')
