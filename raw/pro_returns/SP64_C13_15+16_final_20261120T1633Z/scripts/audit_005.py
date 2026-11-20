from audit_amend import *
t=(WORK/'pages/16_scan005.tex').read_text()
specs=[
 ('mutuellement',14,False,r'\draw (-1.25,-.42) .. controls (-1.3,.01) and (-1,.08) .. (-.6,.02) .. controls (.3,-.08) and (1,.07) .. (1.28,.16)--(1.2,.24);'),
 ('$i<n$,',15,False,r'\draw (-.7,-.5)--(-.65,-.13) .. controls (-.4,.04) and (.5,.03) .. (.7,.2);'),
 (r'\alpha+(2n-2i)>2n-i',28,True,r'\draw (-1.6,-.15) .. controls (-.9,-.28) and (-.15,-.25) .. (0,-.45) .. controls (.12,-.25) and (.85,-.2) .. (1.6,-.1);'),
 (r'\alpha\leq i',29,True,r'\draw (-.7,.65) .. controls (-.3,.78) and (.45,.6) .. (.65,.85)--(.72,1.08);')
]
cr=[];iv=[]
for words,after,math,path in specs:
 old='\\inserted{'+words+'}'
 label='$'+words+'$' if math else words
 tikz=r'\begin{tikzpicture}[x=1cm,y=1cm,baseline=(reading.base)]\node (reading) at (0,.35) {'+label+'};'+path+r'\end{tikzpicture}'
 new=r'\inserted{\text{'+tikz+'}}' if math else r'\inserted{\figure{'+tikz+'}}'
 assert old in t;t=t.replace(old,new)
 cr.append(change('leader at '+words,'insertion without leader','leader absent','insertion with curved leader','The reread shows the curved attachment stroke next to the inserted reading: below mutuellement and i<n, beneath the upper case condition, and above the lower case condition respectively.','drawing or diagram',c=True))
 iv.append((after,inv('drawing','at insertion '+words,'curved insertion leader')))
amend('16','005',t,cr,iv)
