from audit_amend import *
t=(WORK/'pages/16_scan008.tex').read_text()
specs=[
 ("l'anneau",4,False,r'\draw (-.9,-.4)--(-.9,-.1) .. controls (-.4,.05) and (.5,.02) .. (.9,.08)--(.85,.2);','Short hooked leader beneath l\'anneau.'),
 (r'(et $(3.0)$: $\pi_i=0$ si $i\notin[0,2n]$)',5,False,r'\draw (-2.6,.15) .. controls (-2.7,-.15) and (-1.5,-.14) .. (-1.2,-.22)--(-1.08,-.4) .. controls (-1.02,-.2) and (-.4,-.1) .. (.3,-.1) .. controls (1.5,-.1) and (2.5,-.12) .. (2.65,.15);','A long shallow curved bracket beneath the support condition has a downward cusp near its left third.'),
 (r'i.e. $\pi_i$ et $\pi_{2n-i}\in\mathcal E$.',11,False,r'\draw (-1.6,-.4)--(-1.65,-.1) .. controls (-1.3,.07) and (.3,.03) .. (1.5,.1)--(1.6,.2);','The endpoint-membership insertion has a descending left hook and a long undercurve.'),
 (r'on a $\varphi_i,\psi_{2n-i}\in\mathcal E$, d\'où'.replace("\\'","'"),15,False,r'\draw (-2.2,.2) .. controls (-2.5,-.06) and (-1.8,-.12) .. (-.65,-.12)--(-.5,-.38)--(-.42,-.14) .. controls (.3,-.03) and (2.1,-.2) .. (2.35,.2);','The replacement after Notons que has a wide undercurve with a downward point attaching after the reference to section 3.'),
 (r'\quad\text{car }w_i\pi_{2n-i}=\pi_iw_i',27,True,r'\draw (-1.6,-.55) .. controls (-1.55,-.3) and (-1.48,-.08) .. (-1.3,.02);','A short curved leader rises from the product computation to its first car annotation.'),
 (r'\quad\text{car }w_iv_i\pi_i=\pi_i',28,True,r'\draw (-1.45,-.55) .. controls (-1.4,-.22) and (-.55,-.1) .. (-.4,.05);','A second, longer curved leader rises rightward from the last product factors to the second car annotation.')
]
cr=[];iv=[]
for words,after,math,path,evidence in specs:
 old='\\inserted{'+words+'}'
 label='$'+words+'$' if math else words
 tikz=r'\begin{tikzpicture}[x=1cm,y=1cm,baseline=(reading.base)]\node (reading) at (0,.35) {'+label+'};'+path+r'\end{tikzpicture}'
 new=r'\inserted{\text{'+tikz+'}}' if math else r'\inserted{\figure{'+tikz+'}}'
 assert old in t,(after,words);t=t.replace(old,new)
 cr.append(change('insertion leader '+str(after),'insertion without drawn leader','leader absent','insertion with curved leader',evidence,'drawing or diagram',c=True))
 iv.append((after,inv('drawing','at '+words,'curved insertion leader')))
amend('16','008',t,cr,iv)
