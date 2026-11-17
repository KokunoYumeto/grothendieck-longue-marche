from pathlib import Path
import sys,csv
sys.path.insert(0,str(Path(__file__).resolve().parent))
from audit import audited,doubt
root=Path(__file__).resolve().parents[1]
p=root/'pages/MPL_108+112+113+114+115_115_scan012.tex';s=p.read_text().replace(r'\mspage{6}',r'\mspage{\textcircled{6}}')
s=s.replace(r'\margin{Cas où',r'\figure{\begin{tikzpicture}\draw(0,0)--(.04,1.4);\end{tikzpicture}}'+'\n'+r'\margin{Cas où',1)
s=s.replace(r'\margin{$\varphi^{\unsure{\sharp|\natural}}$ fidèle}',r'\margin{\figure{\begin{tikzpicture}\draw(0,0)--(.3,1.4);\end{tikzpicture}}$\varphi^{\unsure{\sharp|\natural}}$ fidèle}')
s=s.replace(r'(i.e. $a\longrightarrow F\quad\unsure{F\'|G}\longrightarrow b$)',r'(i.e. $a\longrightarrow F\quad\unsure{F\'|G}\longrightarrow b$)')
s=s.replace("(i.e. $a\\longrightarrow F\\quad\\unsure{F'|G}\\longrightarrow b$)","(i.e. $a\\longrightarrow F\\quad\\unsure{F'|G}\\longrightarrow b$)\n"+r'\figure{\begin{tikzpicture}\draw(0,1.1)..controls(-.15,.7)and(-.2,.6)..(-.1,.45)..controls(0,.2)and(-.12,.05)..(-.35,0);\end{tikzpicture}}')
s=s.replace(r"v'(\varphi_*u)",r"v'(\unsure{\varphi|\varphi_*}u)")
p.write_text(s)
f=root/'MPL_108+112+113+114+115_inventory.csv';rows=list(csv.DictReader(f.open()));fields=list(rows[0]);n=max(int(r['element']) for r in rows if int(r['cote'])==115 and int(r['scan'])==12)+1
for k,pos,words in [(0,'left of upper-right question','vertical separator'),(1,'beside faithful annotation','slanted separator'),(2,'right of u and u-prime condition','curved brace')]:rows.append(dict(zip(fields,['115','12','text',str(n+k),'drawing',pos,words,'yes'])))
rows.sort(key=lambda r:(int(r['cote']),int(r['scan']),int(r['element'])))
with f.open('w',newline='') as o:w=csv.DictWriter(o,fieldnames=fields);w.writeheader();w.writerows(rows)
doubt(115,12,'composition row',r"v′(φu) / v′(φ_*u)",'subscript may be absent in this occurrence; last product has it','low')
audited(115,12,'Both halves read; circled author 6, two separator strokes and condition brace restored. Macro arguments braced without reading changes. Opposite directions of the isolated tilde-f and final oval tilde-f are retained; composition φ/φ-substar marked doubtful.')
