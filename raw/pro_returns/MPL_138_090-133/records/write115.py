from records.record_page import save
D=r'\fill(0,0)circle(2pt);'
def star(n):
    return D+''.join(r'\draw(0,0)--('+str(a)+':.65);' for a in ([90,210,330] if n==3 else [90,180,270,0] if n==4 else [90,162,234,306,18]))
seg=r'\draw(0,0)--(.7,0);'+D
line1=r'\draw(-.7,0)--(.7,0);'+D
line2=r'\draw(-.7,0)--(.7,0);\fill(-.7,0)circle(2pt);\fill(0,0)circle(2pt);'
edge=r'\draw(-.5,0)--(.5,0);\fill(-.5,0)circle(2pt);\fill(.5,0)circle(2pt);'
loop=D+r'\draw(0,0)..controls(1.3,1.4)and(1.4,-1)..(0,0);'
loopL=D+r'\draw(0,0)..controls(-1.3,1.4)and(-1.4,-1)..(0,0);'
y=D+r'\draw(-.9,0)--(0,0)--(.6,.4);\draw(0,0)--(.6,-.4);\fill(-.9,0)circle(2pt);'
cross=star(4)
double=D+r'\draw(0,0)..controls(-1.2,1.3)and(-1.5,-1.2)..(0,0)..controls(1.4,1.2)and(1.4,-1.2)..(0,0);'
z=r'\mathbb Z_2'; zz=z+r'\times'+z
rows=[]
def row(n,graphs,groups,passports,braces=(),underline=()):
    count=len(graphs); sp=3.1
    t=r'\figure{\begin{tikzpicture}[scale=.7,line cap=round]'+'\n'
    if n:t+=r'\node[draw,circle]at(-1.6,.3){$'+str(n)+r'$};'+'\n'
    for i,(g,group,passport) in enumerate(zip(graphs,groups,passports)):
        t+=r'\begin{scope}[shift={('+str(i*sp)+r',0)}]'+g+'\n'
        gr=(r'\uuline{'+group+'}' if i in underline else group)
        t+=r'\node at(0,-1.0){$'+gr+r'$};'+'\n'
        if passport:t+=r'\node at(0,-2.0){$'+passport+r'$};'+'\n'
        t+=r'\end{scope}'+'\n'
    for i,j in braces:
        a=i*sp;b=j*sp;m=(a+b)/2
        t+=r'\draw('+str(a)+r',-1.4)..controls('+str(m)+r',-1.4)and('+str(m)+r',-1.4)..('+str(m)+r',-1.6)..controls('+str(m)+r',-1.4)and('+str(m)+r',-1.4)..('+str(b)+r',-1.4);'+'\n'
    t+=r'\end{tikzpicture}}'
    rows.append(t)
def v(*x):return r'\begin{smallmatrix}'+'\\\\'.join(map(str,x))+r'\end{smallmatrix}'
def p(*x):return r'\left('+','.join(map(str,x))+r'\right)'
row(1,[seg],[z],[p(1,1,1)],underline=(0,))
row(2,[line1,edge,loop],[zz,zz,zz],[p(2,v(1,1),2),p(v(1,1),2,2),p(2,2,v(1,1))],braces=((1,2),),underline=(0,1,2))
row(3,[star(3),loop+r'\draw(-.8,0)--(0,0);',line2],[r'\mathfrak S_3',z,z],[p(3,v(1,1,1),3),p(3,v(2,1),v(2,1)),p(v(2,1),v(2,1),3)],braces=((1,2),),underline=(0,))
row(4,[y,loop+r'\draw(-.6,.4)--(0,0)--(-.6,-.4);',r'\draw(-1,0)--(1,0);\fill(-.35,0)circle(2pt);\fill(.35,0)circle(2pt);',loop+r'\draw(-.7,0)--(.5,0);'],[z,z,zz,zz],[p(v(3,1),v(2,1,1),4),p(4,v(2,1,1),v(3,1)),p(v(2,2),v(2,1,1),4),p(4,v(2,1,1),v(2,2))],braces=((0,1),(2,3)))
row(None,[cross,r'\draw(-1,0)--(1,0);\foreach\x in{-1,0,1}\fill(\x,0)circle(2pt);',double],[r'D_4',zz,zz],[p(4,v(1,1,1,1),4),p(v(2,1,1),v(2,2),4),p(4,v(2,2),v(2,1,1))],braces=((1,2),),underline=(0,))
row(None,[r'\draw(0,0)ellipse(.5 and.65);\fill(0,.65)circle(2pt);\fill(0,-.65)circle(2pt);',loopL+r'\draw(0,0)--(.9,0);\fill(.9,0)circle(1pt);'],[r'D_4',z],[p(v(2,2),v(2,2),v(2,2)),p(v(3,1),v(r'\unsure2',2),v(1,3))],underline=(0,))
row(5,[star(5),cross+r'\fill(-.65,0)circle(2pt);',loopL+r'\draw(.7,.45)--(0,0)--(.7,0);\draw(0,0)--(.7,-.45);'],[r'D_5',z,z],[p(r'5\deleted{\unsure{1}}',r'1_5',5),p(v(4,1),v(2,r'1_3'),5),p(5,v(2,r'1_3'),v(4,1))],braces=((1,2),),underline=(0,))
rows.append(r'\margin{\deleted{$\unsure{\left(\begin{smallmatrix}5\\1_2\end{smallmatrix}\right),}$}}')
row(None,[loopL+r'\draw(-.55,0)--(0,0)--(.6,.4);\draw(0,0)--(.6,-.4);',y.replace(r'\fill(-.9,0)circle(2pt);',r'\fill(-.5,0)circle(2pt);'),double+r'\draw(0,0)--(.4,0);',r'\draw(-1,0)--(1,0);\foreach\x in{-1,-.3,.4}\fill(\x,0)circle(1.5pt);'],[z,z,z,z],[p(5,v(2,r'1_3'),v(3,2)),p(v(3,2),v(2,r'1_3'),5),p(5,v(r'2_2',1),v(r'\unsure{2_2}',1)),p(v(r'2_2',1),v(r'2_2',1),5)],braces=((0,1),(2,3)))
tex='\\scanpage{115}\n% archive foliation: 114\n'+'\n'.join(rows)
e=[]
for n,count in [(1,1),(2,3),(3,3),(4,9),(5,7)]:
 e.append(('heading',f'degree{n}',f'circled{n}'))
 for k in range(count):
  e.extend([('figure',f'degree{n} drawing{k+1}','map drawing'),('formula',f'degree{n} drawing{k+1}','group label'),('formula',f'degree{n} drawing{k+1}','branching triple')])
e.extend([('figure','pairings','six connecting braces'),('cancelled_formula','degree5 left','cancelled partition'),('cancelled_symbol','degree5 passport','overwritten subscript')])
save(115,tex,e,doubts=[('pencil graph under degree4','middle partition 2,2','first2 overwritten','medium'),('degree5 left margin','cancelled 5,1₂','tiny overwritten partition','low'),('degree5 last pair','2₂,1 in third partition','overwritten first entry','medium')],notation=[('Z₂','\\mathbb Z_2','group labels drawn double-stroke Z'),('S₃','\\mathfrak S_3','ornate S with lower3'),('stacked integers','\\begin{smallmatrix}...\\end{smallmatrix}','partitions are vertical lists, not fractions')],leads='Small-degree map catalogue with group labels Z2, Z2×Z2, S3, D4,D5 and branching triples; orientation-reversing automorphisms likely included—do not silently identify with the oriented groups of104. Degree4 extra pencil loop-tail appears. Check completeness and association only in research afterfreeze.')
