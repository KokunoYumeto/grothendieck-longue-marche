from page_106_005 import art,zero
import sys
sys.path.insert(0,'/workspace/scratch/4bbc351d3cab/MPL_106+107/scripts')
from save_page import save
tex=r'\texttt{//*\quad PLOTEDIT7747\qquad I}'+'\n\n'+art([zero]*4,14)+'\n\n'+art([[s] for s in ['PPPPPPPPPPP','LL','OOOOOOOOOOOO','TTTTTTTTTTTT','EEEEEEEEEEEE','DDDDDDDDD','IIIIIIIIII','TTTTTTTTTTTT']],14)+'\n\n'+r'\mspage{10}'
elements=[('text','printed heading after rotation','//* PLOTEDIT7747 I'),('drawing','printed banner','four slanted zeros built of 0'),('drawing','cropped page edge','single visible top row of PLOTEDIT character art'),('text','original lower left','10')]
if __name__=='__main__':save(106,11,tex,elements,kind='reused_typed',notes='Reused separator: heading //* PLOTEDIT7747 I, four zero-shaped character drawings, and only one visible row of a PLOTEDIT banner at the cut edge. Sheet number 10. No mathematics. No missing off-image rows are supplied.')
