from records.record_page import save
from records.graph_rows import D,loop,loopL,double,star,z,zz,p,v
r=[]
def pic(items,extra=''):
 t=r'\figure{\begin{tikzpicture}[scale=.64,line cap=round,line join=round]'
 for xx,yy,g,lab in items:
  t+=r'\begin{scope}[shift={('+str(xx)+','+str(yy)+r')}]'+g
  if lab.startswith('C:'):t+=r'\node[draw,circle]at(0,-1){$'+lab[2:]+r'$};'
  elif lab:t+=r'\node at(0,-1){$'+lab+r'$};'
  t+=r'\end{scope}'
 t+=extra+r'\end{tikzpicture}}';return t
r.append(r'\uline{degré $6$}\quad a) $1$ sommet d’ordre $6$')
a=[(6,3,D+''.join(r'\draw(0,0)--('+str(i)+':.8);' for i in [30,90,150,210,270,330]),r'\uuline{D_6}'),(9,3,loop+r'\draw(-.7,.4)--(0,0)--(-.7,-.4);\draw(0,-.7)--(0,0)--(.4,-.6);',z),(12,3,loop+r'\draw(-.7,.2)--(0,0)--(.5,.1);\draw(-.5,-.6)--(0,0)--(0,-.7);',z),
(0,1.1,loop+r'\draw(-.7,.3)--(0,0)--(.6,.2);\draw(-.7,-.4)--(0,0)--(.6,-.2);',zz),
(3.1,1.1,double+r'\draw(-.6,-.6)--(0,0)--(0,-.8);',z),
(6.5,1.1,double+r'\draw(.7,.2)--(0,0)--(.6,-.2);\node at(1.2,-.7){$\times$};',z),
(10,1.1,double+r'\draw(-.7,0)--(.7,.2);',zz),
(0,-1.3,double+r'\draw(0,.7)--(0,0)--(.7,0);\node at(-1.2,-.8){$\times$};','C:1'),
(3,-1.3,double+r'\draw(0,0)..controls(-.5,-1.7)and(.6,-1.7)..(0,0);',r'\mathfrak S_3'),
(6.5,-1.3,double+r'\draw(0,0)..controls(1.1,.7)and(1.1,-.7)..(0,0);',z),
(10.6,-1.6,double+r'\draw(0,-.8)--(0,.8);',zz)]
extra=r'\draw(7.5,3.8)--(7,2.5);\draw(7.6,3.8)--(7.1,2.5);\draw(1.7,2)--(1.7,.3);\draw(1.8,2)--(1.8,.3);\draw(1.5,-.5)--(1.1,-2.3);\draw(1.6,-.5)--(1.2,-2.3);\draw(12.1,1.5)--(12.2,.1);\foreach\y in{.2,.4,...,1.5}\draw(12,\y)--(12.3,\y+.15);\draw(1.9,2.1)..controls(4,2.4)and(4,1.1)..(4.8,.4)..controls(7,-.2)and(9.8,-.3)..(11.5,-.3)..controls(12.7,-2.7)..(11.4,-2.7)--(9.3,-2.7)..controls(8.8,-2.7)and(9,-1.5)..(8.5,-1)..controls(7,.1)and(4,-.2)..(3,-.25)..controls(1.5,-.4)..(1.9,2.1);'
extra+=r'\node at(10.5,-3.4){$'+p(6,v(r'2_2',r'1_2'),v(r'\unsure4',r'\unsure{1_2}'))+r'$};'
r.append(pic(a,extra))
r.append(r'b) $1$ sommet d’ordre $5$, $1$ d’ordre $1$')
b=[(0,1.5,D+r'\draw(-.8,0)--(0,0)--(.8,.5);\draw(0,-.7)--(0,.7);\draw(0,0)--(.8,-.2);\fill(-.8,0)circle(2pt);',z),
(3.3,1.5,loop+r'\draw(-1,0)--(0,0)--(0,-.7);\draw(0,0)--(.4,-.7);\fill(-1,0)circle(2pt);',r'\deleted{\unsure{\mathbb Z_2}}\quad1'),
(6.8,1.5,loop+r'\draw(-1,0)--(.6,0);\draw(0,0)--(-.2,-.7);\fill(-1,0)circle(2pt);','C:1'),
(10.2,1.5,loop+r'\draw(-1,0)--(0,0)--(.7,.2);\draw(0,0)--(.7,-.2);\fill(-1,0)circle(2pt);',z),
(0,-1.2,D+r'\draw(-.9,0)--(0,0)..controls(.6,1.6)and(1.6,1.1)..(0,0)..controls(1.6,-.1)and(1.6,-1.5)..(0,0);\fill(-.9,0)circle(2pt);',z),
(3.3,-1.2,D+r'\draw(0,0)..controls(.6,1.6)and(1.6,1.1)..(0,0)..controls(1.6,-.1)and(1.6,-1.5)..(0,0);\draw(0,0)--(.8,.5);\fill(.8,.5)circle(2pt);','C:1'),
(8,-1.6,loop+r'\draw(-1,0)--(0,0)--(-.4,.5);\draw(0,0)--(-.4,-.5);\fill(-1,0)circle(1.5pt);',z)]
r.append(pic(b,r'\draw(2,1.8)..controls(2,2.7)and(5,2.8)..(5,2)..controls(4.9,.7)and(8,.1)..(9,-.6)..controls(11,-2.7)and(7,-3.4)..(6,-1.5)..controls(5,.5)and(1.8,.7)..(2,1.8);\draw[->](4.3,.7)..controls(6,-.5)..(6.4,-1);'))
r.append(r'c) $1$ sommet d’ordre $4$, $1$ d’ordre $2$')
c=[(0,0,D+r'\draw(-1.5,0)--(.9,0);\draw(.8,.6)--(0,0)--(.8,-.6);\fill(-.8,0)circle(2pt);',z),
(4,0,loop+r'\draw(-1.5,0)--(0,0)--(.6,-.7);\fill(-.8,0)circle(2pt);','C:1'),
(8,0,loop+r'\draw(-1.5,0)--(.5,0);\fill(-.8,0)circle(2pt);',z)]
r.append(pic(c))
r.append(r'\margin{'+pic([(-1,1.7,loop+r'\draw(-.6,0)--(.4,0);\fill(.9,.2)circle(1.5pt);\node at(-.7,.6){$(\alpha)$};',z),(1.6,1.7,loop+r'\draw(-.5,.3)--(0,0)--(-.5,-.3);\fill(.9,.2)circle(1.5pt);\node at(-.7,.6){$(\gamma)$};',z),(-1,-.4,double+r'\fill(-.9,0)circle(1.5pt);\node at(-1.2,.6){$(\beta)$};',z)])+'}')
r.append(r'd) $1$ sommet d’ordre $4$, deux d’ordre $1$')
r.append(pic([(0,0,D+r'\foreach\a in{45,135,225,315}\draw(0,0)--(\a:.8);\fill(45:.8)circle(2pt);\fill(135:.8)circle(2pt);',z),(3,0,D+r'\draw(-.6,.6)--(0,0)--(.6,.6);\fill(-.6,.6)circle(2pt);\fill(.6,.6)circle(2pt);\draw(0,0)..controls(-1,-1.6)and(1,-1.6)..(0,0);',z),(5.7,0,star(4)+r'\fill(-.65,0)circle(1.5pt);\fill(.65,0)circle(1.5pt);\node at(-.9,.6){$(\delta)$};',zz),(8.3,0,loopL+r'\draw(-.5,0)--(.5,0);\fill(-.5,0)circle(1.5pt);\fill(.5,0)circle(1.5pt);\node at(-.8,.6){$(\unsure{\eta})$};',z)]))
r.append(r'e) $2$ sommets d’ordre $3$\margin{$\deleted{\unsure2}$}')
dumb=r'\draw(0,0)--(1.2,0);\draw(0,0)..controls(-1.4,1.4)and(-1.4,-1.2)..(0,0);\draw(1.2,0)..controls(2.6,1.4)and(2.6,-1.2)..(1.2,0);\fill(0,0)circle(2pt);\fill(1.2,0)circle(2pt);'
r.append(r'\deleted{'+pic([(0,0,dumb+r'\foreach\x in{-.7,-.5,...,2}\draw(\x,-.6)--(\x+.7,.8);',r'\mathbb Z')])+'}')
r.append(pic([(7,1,dumb,zz),(2,-1.4,loopL+r'\draw(0,0)--(1.2,0)--(1.8,.5);\draw(1.2,0)--(1.8,-.5);\fill(1.2,0)circle(2pt);',z),(7,-1.4,r'\draw(-.7,.5)--(0,0)--(-.7,-.5);\draw(0,0)--(1,0);\draw(1.7,.5)--(1,0)--(1.7,-.5);\fill(0,0)circle(2pt);\fill(1,0)circle(2pt);',zz)]))
theta=r'\draw(0,0)..controls(.6,.8)and(1.1,.8)..(1.5,0)..controls(1,-.8)and(.4,-.8)..(0,0);\fill(0,0)circle(2pt);\fill(1.5,0)circle(2pt);'
r.append(pic([(0,0,theta+r'\draw[thick](0,0)--(1.5,0);',r'\mathbb Z_2.\mathfrak S_3\quad\deleted{\unsure{D_3\times\mathbb Z_2}}'),(4,0,theta+r'\draw(-.6,0)--(0,0);\draw(1.5,0)--(2.1,0);',zz),(8,0,theta+r'\draw(0,0)--(.6,0);\draw(1.5,0)--(2.1,0);',zz)]))
e=[]
for letter,count in [('a',11),('b',7),('c',6),('d',4),('e',7)]:
 e.append(('text',f'part{letter}','vertex order description'))
 for j in range(count):e.extend([('figure',f'part{letter} graph{j+1}','map drawing'),('formula',f'part{letter} graph{j+1}','group label')])
e += [('figure','partsa,b','pencil enclosing contours'),('formula','parta pencil','partition triple'),('figure','partb','pencil arrow'),('cancelled_formula','partb second','Z2'),('cancelled_formula','bottom','D3 timesZ2'),('cancelled_figure','parte','double-loop draft'),('annotation','throughout','cross marks and circled1'),('figure','parta','double slash dividers')]
save(119,'\\scanpage{119}\n% archive foliation: 118\n'+'\n'.join(r),e,doubts=[('a pencil passport','4 over1₂','both overwritten','low'),('d pencil label','eta','epsilon','low'),('bottom theta label','deleted D₃×Z₂','strongly overdrawn, Z₂.S₃ before it clearer','low'),('a lower labels','S₃','ornate S, not G','medium')],leads='Degree6 enumeration. Several circled trivial automorphism groups, and one corrected Z2→1; possible chiral maps. All pencil insertions retained. Theta-graph label Z2.S3 with cancelled D3×Z2. No identification of these symmetry groups with monodromy absent argument.')
