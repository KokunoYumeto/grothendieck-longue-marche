from audit_amend import *
t=(WORK/'pages/16_scan004.tex').read_text()
ivs=[r for r in readrows(PREFIX+'_inventory.csv') if r['scan']=='16/004']
cr=[]; additions=[]
for words,needle,place in [(r'de $k$-modules','k-modules','grading insertion'),(r'satisfaisant $(1.1.)$','satisfaisant','projector-condition insertion')]:
 old='\\inserted{'+words+'}'
 new=r'\inserted{\figure{\begin{tikzpicture}[x=1cm,y=1cm]\node at (0,.35) {'+words+r'};\draw (-1.5,-.45) .. controls (-1.55,-.1) and (-1.1,.01) .. (-.8,.02) .. controls (.2,.05) and (1.5,.08) .. (1.55,.27);\end{tikzpicture}}}'
 assert old in t;t=t.replace(old,new)
 matches=[r for r in ivs if r['kind']=='insertion' and needle in r['first_words_or_objects']]
 assert len(matches)==1,(needle,matches)
 additions.append((int(matches[0]['element']),inv('drawing',place,'curved insertion leader')))
 cr.append(change(place+' leader','inserted words without leader','leader absent','inserted words with curved leader','A descending left hook runs into a long shallow curve immediately below the inserted words and turns upward at the right.','drawing or diagram',c=True))
amend('16','004',t,cr,additions)
