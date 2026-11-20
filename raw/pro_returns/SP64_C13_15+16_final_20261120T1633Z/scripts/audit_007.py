from audit_amend import *
t=(WORK/'pages/16_scan007.tex').read_text()
words=r'$\mathcal E^*$ sous-algèbre graduée de $\operatorname{End}(M^*)$,'
old='\\inserted{'+words+'}'
new=r'\inserted{\figure{\begin{tikzpicture}[x=1cm,y=1cm]\node at (0,.35) {'+words+r'};\draw (-3.1,-.5)--(-3.1,-.12) .. controls (-2.8,.02) and (-1.1,.03) .. (2.9,.03) .. controls (3.25,.03) and (3.35,.08) .. (3.35,.23);\end{tikzpicture}}}'
assert old in t;t=t.replace(old,new)
after=int(next(r['element'] for r in readrows(PREFIX+'_inventory.csv') if r['scan']=='16/007' and r['kind']=='insertion'))
amend('16','007',t,[change('subalgebra insertion leader','inserted phrase without leader','leader absent','inserted phrase with long curved leader','A long shallow line beneath the inserted subalgebra phrase has a descending left hook and an upward right return.','drawing or diagram',c=True)],[(after,inv('drawing','subalgebra insertion','long curved insertion leader'))])
