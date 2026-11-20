from audit_amend import *

t=(WORK/'pages/16_scan003.tex').read_text()
items=[
 (r'par $\mathbb Z$',6,'par Z',r'\node at (0,.35) {par $\mathbb Z$};\draw (-.55,-.55) .. controls (-.1,-.15) and (.7,.15) .. (.75,.4);','A thin sloping leader descends left from the inserted par Z toward gradué.'),
 ('à graduation finie',7,'finite grading',r'\node at (0,.05) {à graduation};\node at (1.4,.65) {finie};\draw (1.2,.37) .. controls (1.65,.42) and (1.8,.22) .. (1.65,.02)--(2.1,.45);','Finie is raised above the right end of à graduation and joined by a hooked curved stroke.'),
 ("sous-anneau de l'anneau",9,'subring insertion',r"\node at (0,.35) {sous-anneau de l'anneau};\draw (-2.35,-.45)--(-2.35,-.1) .. controls (-1.6,.03) and (.6,.03) .. (1.85,.03) .. controls (2.25,.03) and (2.3,.12) .. (2.25,.2);",'A left hook rises to a long curve beneath the inserted subring phrase and ends in a short upward return.'),
 ('du module ss-jacent (le produit)',10,'underlying module insertion',r'\node at (0,.35) {du module ss-jacent (le produit)};\draw (-2.6,-.45)--(-2.6,-.1) .. controls (-1.8,.03) and (.7,.03) .. (2.6,.03);','The inserted phrase has a descending left hook and a long shallow rule beneath it.'),
 ('intrinsèquement',24,'intrinsic grading insertion',r'\node at (0,.35) {intrinsèquement};\draw (-1.45,-.45)--(-1.45,-.1) .. controls (-.8,.02) and (.8,.05) .. (1.3,.15)--(1.43,.28);','The curved leader begins below the inserted word with a left hook and rises at its right tip.'),
 ('nuls sauf un nb fini.',35,'finite number insertion',r'\node at (0,.35) {nuls sauf un nb fini.};\draw (-1.9,-.45)--(-1.9,-.1) .. controls (-1.2,.03) and (.7,.03) .. (1.75,.08) .. controls (2.05,.09) and (2.1,.18) .. (2.03,.24);','A left descending hook and a long shallow curved leader attach the inserted finiteness phrase after E.')
]
cr=[]; iv=[]
for words,after,place,drawing,evidence in items:
 old='\\inserted{'+words+'}'
 new=r'\inserted{\figure{\begin{tikzpicture}[x=1cm,y=1cm]'+drawing+r'\end{tikzpicture}}}'
 assert old in t,place
 t=t.replace(old,new)
 cr.append(change(place+' leader','insertion without drawn leader','leader absent','insertion with drawn leader',evidence,'drawing or diagram',c=True))
 iv.append((after,inv('drawing',place,'insertion leader')))
amend('16','003',t,cr,iv)
