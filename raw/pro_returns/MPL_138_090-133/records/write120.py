from records.graph_pic import *
r=[]
r.append(r'f) $1$ sommet d’ordre $3$, $1$ d’ordre $2$, $1$ d’ordre $2$')
f=[(0,1,D+r'\draw(0,.7)--(0,-.7);\draw(0,0)--(1.3,0);\fill(0,-.7)circle(2pt);\fill(.65,0)circle(2pt);\node at(.9,.55){$\times$};','C:1'),
(3,1,D+r'\draw(-.8,.4)--(0,0)--(1,.6)--(2,.5);\draw(0,0)--(0,-.8);\fill(0,-.8)circle(2pt);\fill(1,.6)circle(2pt);\draw(1,.6)--(1.5,1.2);','C:1'),
(6.8,1,D+r'\draw(-.5,.7)--(0,0)--(-.5,-.7);\draw(0,0)--(2,0);\fill(1,0)circle(2pt);\fill(2,0)circle(2pt);\node at(.8,.65){$\times$};',z),
(0,-1.5,loop+r'\draw(-.6,.6)--(0,0)--(-.6,-.5);\fill(-.6,.6)circle(2pt);\fill(.95,.1)circle(2pt);',''),
(3,-1.5,loop+r'\draw(-.7,.5)--(0,0)--(-.7,-.5);\draw(0,0)--(1,0);\fill(1,0)circle(2pt);',r'\unsure{1}\quad\mathbb Z_2'),
(6.8,-1.5,loopL+r'\draw(0,0)--(1.6,0);\fill(.7,0)circle(2pt);',z)]
extra=r'\draw(2,2)--(1.8,-1.8);\draw(3.8,2)--(3.4,-1.6);\draw(4.7,2)--(4,-1.9);\draw(2,-1.5)..controls(3,-4)and(4,-2.5)..(4.6,-1.4)..controls(5.1,-.4)and(4.4,-.7)..(4,-1.6);\draw(2.7,-1.7)circle(.4);\draw(2.3,-1.3)--(3.1,-2.1);\draw(3.1,-1.3)--(2.3,-2.1);'
r.append(pic(f,extra))
r.append(r'\margin{$'+p(v(3,2,1),v(r'2_2',r'1_2'),r'\unsure6')+r'$\\$'+p(v(3,2,1),v(r'2_2',r'1_2'),r'\unsure6')+r'$\\$'+p(v(3,2,1),r'\unsure{2_3}',v(5,1))+r'$\\$'+p(v(3,2,1),r'2_3',v(4,2))+r'$}')
r.append(r'\figure{\begin{tikzpicture}\draw(0,0)..controls(.1,.7)and(.6,.8)..(.8,.8)--(.8,1.3);\draw(.9,.8)..controls(1.2,.4)and(2,.7)..(2.7,0);\draw(1.4,2.6)..controls(.8,2.4)..(1,2.1);\end{tikzpicture}}')
r.append(r'g) $1$ sommet d’ordre $3$, \unsure{trois} d’ordre $1$')
r.append(pic([(0,0,star(3)+r'\foreach\a in{90,210,330}\fill(\a:.65)circle(2pt);',r'\uuline{D_3}'),(3,0,star(3)+r'\draw(-.2,.8)--(.5,.6)--(-.3,.1)--(.5,0)--(-.3,-.5)--(.2,-.5);','')]))
r.append(r'\['+p(v(3,r'1_3'),r'2_3',6)+r'\]')
r.append(r'h) $3$ sommets d’ordre $2$')
r.append(pic([(0,0,r'\draw(0,0)circle(.8);\foreach\a in{90,180,320}\fill(\a:.8)circle(2pt);',r'\uline{\mathbb Z_2.\unsure{D_3|\mathfrak S_3}}'),(3.5,0,r'\draw(-1.4,0)--(1.4,0);\foreach\x in{-.7,0,.7}\fill(\x,0)circle(1.5pt);',zz)]))
r.append(r'\margin{$'+p(r'2_3',r'2_3',r'3_2')+r'$\\$'+p(r'2_3',v(r'2_2',r'1_2'),6)+r'$}')
r.append(r'i) $2$ sommets d’ordre $2$, $2$ d’ordre $1$')
r.append(pic([(0,0,r'\draw(-1.2,0)--(1.2,0);\foreach\x in{-1.2,-.4,.4,1.2}\fill(\x,0)circle(2pt);',zz)]))
r.append(r'\['+p(v(r'2_2',r'1_2'),r'2_3',6)+r'\]')
r.append(r'j) $1$ sommet d’ordre $2$, $4$ d’ordre $1$')
r.append(r'\figure{\begin{tikzpicture}\draw(0,0)--(.9,0);\fill(0,0)circle(1pt);\fill(.9,0)circle(1pt);\node[draw,ellipse]at(3,.3){impossible};\end{tikzpicture}}')
e=[('text','top','f)1 sommet3,1 ordre2,1 ordre2')]
for i in range(6):e.extend([('figure',f'partf graph{i+1}','map'),('formula',f'partf graph{i+1}','group label / circled1')])
e.extend([('cancelled_figure','partf','oblique strokes across two middle graphs'),('formula','right margin','four partition triples partly covered by ink'),('figure','right margin','bracketing strokes'),('text','middle','g)1 sommet3,trois ordre1'),('figure','partg','three-ray tree with endpoints'),('formula','partg','D3'),('cancelled_figure','partg','three rays'),('formula','partg','partition triple'),('text','lower','h)3 sommets2'),('figure','parth','circle3vertices'),('formula','parth','Z2.D3'),('figure','parth','line3vertices'),('formula','parth','Z2 timesZ2'),('formula','parth margin','two partition triples'),('text','lower','i)2 sommets2,2 ordre1'),('figure','parti','line4vertices'),('formula','parti','Z2 timesZ2 andpartition'),('text','bottom','j)1 sommet2,4 ordre1'),('figure','bottom','small segment'),('annotation','bottom','circled impossible')])
save(120,'\\scanpage{120}\n% archive foliation: 119\n'+'\n'.join(r),e,doubts=[('right top two triples','6 and6 in third columns','ink spill covers substantial portions; only lower curves visible','low'),('right third triple','2₃','subscript intersects ink spill','low'),('g text','trois','initial letters covered by ink','medium'),('h group','D₃','ornate S₃ superposed','low')],leads='Further degree6 cases f–j. Top text actually writes 3,2,2 (do not repair expected3,2,1). Severe ink damage over right partition triples. Circled impossible on j (degree sequence2,1,1,1,1); some initially circled trivial groups are subsequently cancelled. Preserve status changes in research.')
