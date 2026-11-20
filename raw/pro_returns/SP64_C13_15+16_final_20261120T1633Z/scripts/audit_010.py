from audit_amend import *
t=(WORK/'pages/16_scan010.tex').read_text()
specs=[
 ('(i) à (iii)',5,1.25),
 (r'$(6.1)_i$ et',7,1.0),
 (r'$(6.1)_i$ pour tt $i$, (\unsure{défin.|défini|définit|définissant} $\Lambda$) et',17,2.6),
 ('et ils',24,.65),
 ("l'anneau gradué",32,1.25),
 ('Reste à',36,.85)
]
cr=[];iv=[]
for words,after,width in specs:
 old='\\inserted{'+words+'}'
 path=(r'\draw ('+str(-width)+r',-.45) .. controls ('+str(-width-.1)+r',-.1) and ('+str(-width+.3)+r',.05) .. ('+str(-width+.6)+r',.02) .. controls (.3,-.03) and ('+str(width)+r',.03) .. ('+str(width+.05)+r',.22);')
 new=r'\inserted{\figure{\begin{tikzpicture}[x=1cm,y=1cm]\node at (0,.35) {'+words+'};'+path+r'\end{tikzpicture}}}'
 assert old in t,words;t=t.replace(old,new)
 cr.append(change('leader beneath '+words,'inserted reading without drawn leader','leader absent','inserted reading with curved leader','A curved rule immediately beneath this raised insertion descends at its left attachment and curls upward at its right end.','drawing or diagram',c=True))
 iv.append((after,inv('drawing','at insertion '+words,'curved insertion leader')))
amend('16','010',t,cr,iv)
