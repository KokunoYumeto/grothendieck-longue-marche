from audit_amend import *
t=(WORK/'pages/15_scan187.tex').read_text()
old=r'\inserted{sous forme ``analytique\'\'}'.replace("\\'","'")
old="\\inserted{sous forme ``analytique''}"
new=r"\inserted{\figure{\begin{tikzpicture}[x=1cm,y=1cm]\node at (0,.35) {sous forme ``analytique''};\draw (-1.8,-.5)--(-1.85,-.1) .. controls (-.6,.03) and (.7,.03) .. (1.7,.03) .. controls (1.9,.03) and (2,.1) .. (1.95,.3);\end{tikzpicture}}}"
assert old in t;t=t.replace(old,new)
ivs=readrows(PREFIX+'_inventory.csv')
after=int(next(r['element'] for r in ivs if r['scan']=='15/187' and r['kind']=='insertion'))
amend('15','187',t,[change('analytique insertion leader','inserted words without drawn leader','inserted words without drawn leader','hooked curved leader below the inserted phrase','A vertical left hook rises to a long shallow curve under the inserted words and ends in a short upward curl.','drawing or diagram',c=True)],[(after,inv('drawing','under sous forme analytique','hooked curved insertion leader'))])
