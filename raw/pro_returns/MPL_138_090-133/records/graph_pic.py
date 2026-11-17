from records.record_page import save
from records.graph_rows import D,loop,loopL,double,star,z,zz,p,v
r=[]
def pic(items,extra=''):
 t=r'\figure{\begin{tikzpicture}[scale=.64,line cap=round,line join=round]'
 for xx,yy,g,lab in items:
  t+=r'\begin{scope}[shift={('+str(xx)+','+str(yy)+r')}]'+g
  if lab.startswith('C:'):t+=r'\node[draw,circle]at(0,-1){$'+lab[2:]+r'$};'
  elif lab:t+=r'\node at(0,-1){$'+lab+r'$};'
  t+=r'\end{scope}'
 t+=extra+r'\end{tikzpicture}}';return t
