from pathlib import Path
import sys,csv
sys.path.insert(0,str(Path(__file__).resolve().parent))
from audit import audited
root=Path(__file__).resolve().parents[1]
p=root/'pages/MPL_108+112+113+114+115_115_scan006.tex';s=p.read_text().replace(r'\mspage{2}',r'\mspage{\textcircled{2}}')
old=r'''\diagram{\begin{tikzcd}[column sep=large,row sep=small]
A^\circ,\widehat A^\circ,A^\vee\arrow[dr] & \widehat A\\
B^\circ,\widehat B^\circ,B^\vee\arrow[ur] & \widehat B
\end{tikzcd}}'''
new=r'''\diagram{\left.\begin{array}{c}A^\circ,\widehat A^\circ,A^\vee\\B^\circ,\widehat B^\circ,B^\vee\end{array}\right|
\begin{tikzcd}[column sep=small,row sep=small]{}\arrow[dr]&{}\\{}\arrow[ur]&{}\end{tikzcd}
\left|\begin{array}{c}\widehat A\\\widehat B\end{array}\right.}'''
assert old in s;s=s.replace(old,new)
s=s.replace(r'$(A_i)_{i\in I}$ famille de (petites) catégories',r'$(A_i)_{i\in I}$ famille de (petites) catégories'+'\n'+r'\figure{\begin{tikzpicture}\draw (0,0)--(0,1.4);\end{tikzpicture}}')
p.write_text(s)
f=root/'MPL_108+112+113+114+115_inventory.csv';rows=list(csv.DictReader(f.open()));fields=list(rows[0]);n=max(int(r['element']) for r in rows if int(r['cote'])==115 and int(r['scan'])==6)+1
rows.append(dict(zip(fields,['115','6','text',str(n),'drawing','lower left, right of index-family text','vertical separator','yes'])));rows.sort(key=lambda r:(int(r['cote']),int(r['scan']),int(r['element'])))
with f.open('w',newline='') as o:w=csv.DictWriter(o,fieldnames=fields);w.writeheader();w.writerows(rows)
audited(115,6,'Both halves read object by object and arrow by arrow. Preserved circled author number, restored two bars around crossing-arrow schematic and lower vertical separator. All upper/lower exclamation marks and asymmetric NE inner arrow retained.')
