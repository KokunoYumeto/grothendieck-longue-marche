from audit_amend import *
t=(WORK/'pages/16_scan006.tex').read_text()
# The same double ellipse is an inline TikZ box inside the displayed array.
# Avoid the paragraph-making figure wrapper in math mode; no reading changes.
old=r'\figure{\begin{tikzpicture}[baseline=(e.base)]\node[draw,ellipse,double,double distance=.6pt,inner sep=2pt] (e) {$\mathcal E_i^{2n-i}$};\end{tikzpicture}}'
new=old.replace(r'\figure{',r'\text{',1)
assert old in t;t=t.replace(old,new)
ivs=[r for r in readrows(PREFIX+'_inventory.csv') if r['scan']=='16/006']
cr=[];iv=[]
for words,needle,place in [(r"l'annulateur de $\pi_i$ dans $\mathfrak Z\mathcal E^0$",'annulateur','annihilator replacement'),(r'$v:M^i-M^{2n-i}$,','v:','inserted final map')]:
 old='\\inserted{'+words+'}'
 new=r'\inserted{\figure{\begin{tikzpicture}[x=1cm,y=1cm]\node at (0,.35) {'+words+r'};\draw (-1.8,-.4) .. controls (-1.85,-.1) and (-1.5,.05) .. (-1.1,.02) .. controls (.4,-.04) and (1.6,.05) .. (1.8,.2);\end{tikzpicture}}}'
 assert old in t;t=t.replace(old,new)
 matches=[r for r in ivs if r['kind']=='insertion' and needle in r['first_words_or_objects']]
 assert len(matches)==1,(needle,matches)
 cr.append(change(place+' leader','inserted reading without leader','leader absent','inserted reading and curved leader','The inserted reading sits above a long shallow curve, with a downward left hook and a short upward right tip.','drawing or diagram',c=True))
 iv.append((int(matches[0]['element']),inv('drawing',place,'curved insertion leader')))
amend('16','006',t,cr,iv)
log('formatting only 16/006 '+now()+': retained the double ellipse using a math-safe inline TikZ wrapper; no transcription reading changed')
