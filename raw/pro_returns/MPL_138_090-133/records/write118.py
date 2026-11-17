from records.record_page import save
from records.graph_rows import D,loop,loopL,double,star,y
r=[]
def fig(g):return r'\figure{\begin{tikzpicture}[line cap=round,scale=.7]'+g+r'\end{tikzpicture}}'
def sh(g,x,y=0):return r'\begin{scope}[shift={('+str(x)+','+str(y)+r')}]'+g+r'\end{scope}'
x=r'\node at(1.4,0){$\times$};'
r.append(r'c) $\unsure2$ sommets d’ordre $2$')
r.append(fig(r'\draw(0,0)ellipse(.65 and.5);\fill(0,.5)circle(2pt);\fill(0,-.5)circle(2pt);'+sh(r'\draw(-1,0)--(1,0);\fill(-.35,0)circle(2pt);\fill(.35,0)circle(2pt);',3)))
r.append(r'd) $3$ sommets, dont deux d’ordre $1$, $1$ d’ordre $2$')
r.append(fig(r'\draw(-1,0)--(1,0);\foreach\a in{-1,0,1}\fill(\a,0)circle(2pt);\draw(-2,-.3)..controls(0,-.5)and(2,-1)..(4,1);'))
r.append(r'\uline{degré $5$} \deleted{\unsure{4}}\quad a) $1$ sommet d’ordre $5$')
r.append(fig(star(5)+r'\node at(-.8,.4){$\times$};'+sh(loop+r'\draw(-.7,.3)--(.5,-.1);\draw(-.6,-.3)--(0,0);\node at(.8,.1){$\times$};',3,1)+sh(loop+r'\draw(-.7,.6)--(0,0)--(-.7,0);\draw(0,0)--(-.5,-.5);\node at(.6,.1){$\times$};',3,-.4)+sh(double+r'\draw(0,0)--(.5,.1);'+x,5,-1)+sh(double+r'\draw(0,0)--(0,.5);'+x,5,-2.1)))
r.append(r'b) $2$ sommets, d’ordre $4$ et $1$')
r.append(fig(star(4)+r'\fill(-.65,0)circle(2pt);\node at(-.45,-.4){$\times$};'+sh(loop+r'\draw(-.9,0)--(0,0)--(.5,.7);\fill(-.9,0)circle(2pt);\node[draw]at(2,.2){\uline{rigide}};',0,-1.7)+sh(loop+r'\draw(-1,0)--(.5,0);\fill(-1,0)circle(2pt);'+x,0,-3.2)))
r.append(r'c) $2$ sommets, d’ordre $3$ et $2$')
r.append(fig(y.replace(r'\fill(-.9,0)circle(2pt);',r'\fill(-.5,0)circle(2pt);')+x+sh(loop+r'\draw(-1.5,0)--(0,0);\fill(-.8,0)circle(2pt);'+x,0,-1.4)+sh(r'\draw(0,0)circle(.8);\fill(-.8,0)circle(2pt);\fill(.8,0)circle(2pt);\draw(.8,0)--(1.9,0);',0,-3.2)))
r.append(r'd) $3$ sommets, dont $1$ d’ordre $3$, deux d’ordre $1$')
r.append(fig(y+r'\fill(.6,-.4)circle(2pt);'+x))
r.append(r'e) $3$ sommets, \deleted{dont} $2$ d’ordre $2$, $1$ d’ordre $1$')
r.append(r'\deleted{'+fig(loop+r'\draw(-.3,.5)--(.7,.6)--(0,-.2)--(1,0)--(.5,-.3);')+'}')
r.append(fig(r'\draw(-1,0)--(1.8,0);\foreach\a in{-1,0,1}\fill(\a,0)circle(2pt);\node at(2.3,0){$\times$};'))
r.append(r'f) $4$ sommets, dont trois d’ordre $1$, $1$ d’ordre $2$\margin{impossible\ldots}')
e=[('text','top','c)2 sommets'),('figure','top','oval two vertices'),('figure','top right','line two vertices'),('text','upper','d)3 sommets'),('figure','upper','line three vertices'),('figure','upper','curved separator'),('heading','middle','degré5'),('cancelled_number','heading','4'),('text','middle','a)1 sommet'),('figure','degree5a','five rays'),('figure','degree5a','loop inner and outer tails'),('figure','degree5a','loop three outer tails'),('figure','degree5a','double loop inner tail'),('figure','degree5a','double loop outer tail'),('text','middle','b)2 sommets'),('figure','degree5b','cross withendpoint'),('figure','degree5b','loop unequal tails'),('annotation','degree5b','boxed rigide'),('figure','degree5b','loop inner and outer tails withendpoint'),('text','lower','c)2 sommets'),('figure','degree5c','Y with subdivision'),('figure','degree5c','loop withsubdividedtail'),('figure','degree5c','oval with extra vertex'),('text','lower','d)3 sommets'),('figure','degree5d','Y two filled ends'),('text','lower','e)3 sommets'),('cancelled_figure','degree5e','scribbled loop'),('figure','degree5e','line three vertices'),('text','bottom','f)4 sommets'),('margin','bottom','impossible...'),('annotation','throughout','cross marks adjacent to selected drawings')]
save(118,'\\scanpage{118}\n% archive foliation: 117\n'+'\n'.join(r),e,doubts=[('top','2 sommets','2 overwritten to look like1','medium'),('degree5 heading','cancelled4','overdrawn small numeral','low')],leads='Continuation of enumeration114: degree4 c,d and degree5 a–f. Explicit boxed rigide on asymmetric loop-tail graph. Explicit impossible for four vertices, three order1 and one order2. Cross marks by selected figures must not be inferred as mathematical negation without context.')
