import sys
sys.path.insert(0,'/workspace/scratch/4bbc351d3cab/MPL_106+107/scripts')
from save_page import save
tex=r"""
Question des $\varinjlim$ filtrantes

dans $\mathrm{Hot}$
\mspage{17}
"""
elements=[('text','top right','Question des lim filtrantes'),('text','next line','dans Hot'),('text','foot left','17')]
if __name__=='__main__':save(107,18,tex,elements,kind='cover',notes='New title sheet: Question des lim filtrantes dans Hot. Manuscript page number 17 at lower left. No explicit count of pages. Otherwise blank; light reverse-side print is not a front inscription.')
