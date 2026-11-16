from pathlib import Path
import sys,csv
r=Path('MPL_154_127-176_work');p=r/'pages/MPL_154_127-176_154_scan135.tex';s=p.read_text()
a=s.index('\\diagram{',s.index('On a les quatre'))
b=s.index('sur les repères',a)
s=s[:a]+r'''\diagram{\[\begin{tikzcd}[ampersand replacement=\&,column sep=small]
\overbrace{\sigma_1}^{\text{fuseaux locaux}},\&\overbrace{\sigma,\ \sigma_2}^{\text{fuseaux globaux}\leftrightarrow\text{\unsure{ds}}},\&\sigma_0
\end{tikzcd}\]}
'''+s[b:]
s=s.replace(r'\margin{134}',r'\margin{\mspage{134}}')
# Preserve two physically cancelled drawings, including their cancellation strokes.
a=s.index('\\figure{');h=s.index('\n',a);header=s[a:h]
cut=s.index(r'\draw[k,line width=2.5pt]',a)
s=s[:cut]+'\\end{tikzpicture}}}\n'+header+'\n'+s[cut:]
s=s[:a]+r'\deleted{'+s[a:]
a=s.rindex('\\figure{');end=s.index(r'\end{tikzpicture}}',a)+len(r'\end{tikzpicture}}')
s=s[:end]+'}'+s[end:];s=s[:a]+r'\deleted{'+s[a:]
p.write_text(s)
f=r/'MPL_154_127-176_inventory.csv'
with f.open(newline='') as h: rows=list(csv.DictReader(h));fields=rows[0].keys()
for i,pos,words in [(24,'upper centre','cancelled green strip and orange crossings'),(25,'lower right','cancelled p.r. critique D drawing')]:rows.append(dict(cote='154',scan='135',sheet_kind='text',element=f'E{i:02}',kind='deletion',position=pos,first_words_or_objects=words,transcribed='yes'))
rows.sort(key=lambda x:(int(x['scan']),int(x['element'][1:])))
with f.open('w',newline='') as h:w=csv.DictWriter(h,fields);w.writeheader();w.writerows(rows)
sys.path.insert(0,str(r/'scripts'));from audit_page import audit
audit(135,'Whole, both halves and enlarged brace cluster compared with the source. Replaced spurious diagonal connectors above the four involutions by the visible braces. The upper trial drawing and lower p.r. critique drawing have unmistakable long cancellation zigzags; retained all paths and labels and added deleted wrappers and inventory entries. Kept uncertain prose and the visibly unfinished opening set-brace; sheet number encoded as mspage.')
