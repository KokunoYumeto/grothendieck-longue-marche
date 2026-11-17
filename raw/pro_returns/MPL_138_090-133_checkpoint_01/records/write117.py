from records.record_page import save
from records.graph_rows import p,v
r=[]
def line(*x):r.append('\\[\n'+r'\qquad '.join(x)+'\n\\]')
a=v(2,r'1_4');b=v(r'2_2',r'1_2');d=v(r'\deleted{\unsure2}',r'3_2')
line(p(6,r'1_6',6)+r'\mathbin{//}',p(6,a,v(5,1)),p(6,a,v(r'\unsure4',2)),p(6,a,v(3,3))+r'\mathbin{//}\deleted{\unsure{(6}}')
line(p(6,b,v(4,r'1_2')),r'\underbrace{'+p(6,b,v(3,2,1))+r'\quad'+p(6,b,r'2_3')+r'\deleted{\unsure2}\quad'+p(6,b,v(3,2,r'\unsure1'))+r'}_{!}')
line(r'\deleted{\unsure2}'+p(6,r'2_3',v(3,r'1_3')),p(6,r'2_3',v(r'2_2',r'1_2')))
line(p(v(5,1),a,6),p(v(5,1),b,v(5,1)),p(v(5,1),b,v(4,2)),p(v(5,1),b,v(3,3)))
line(p(v(5,1),r'2_3',v(4,r'1_2')),p(v(5,1),r'2_3',v(3,2,1)))
line(p(v(r'\unsure4',r'\unsure2'),a,6),p(v(4,2),b,v(5,1)),p(v(4,2),b,v(4,2)))
line(p(v(4,r'1_2'),b,6),p(v(4,r'1_2'),r'2_3',v(5,1)))
line(p(d,r'2_3',v(4,r'1_2')),p(d,b,v(5,1)),p(d,a,6))
line(p(d,r'2_3',r'2_3'),p(d,b,v(4,2)),p(d,b,v(3,3)))
line(r'(\alpha)\ '+p(v(4,2),v(r'2_2',r'\unsure{2_1|1_2}'),v(r'3_2',r'\deleted{\unsure2}')),r'(\beta)\ '+p(v(4,2),v(r'\deleted{\unsure{2_2}}',r'2_3'),v(3,2,1)),r'(\gamma)\ '+p(v(4,2),v(r'2_2',r'\unsure{2_1|1_2}'),v(4,2)))
line(r'(\delta)\ '+p(v(4,r'\unsure{2_1|1_2}'),v(r'2_2',r'\unsure{2_1|1_2}'),6),r'(\unsure{\eta|\varepsilon})\ '+p(v(4,r'\unsure{2_1|1_2}'),r'2_3',v(r'3_2',r'\deleted{\unsure2}')))
e=[]
counts=[5,5,3,4,2,3,2,3,3,3,2]
for i,n in enumerate(counts,1):
 for j in range(n):e.append(('formula',f'row{i} item{j+1}','partition triple / cancelled entry'))
e.append(('figure','row2','brace with exclamation'))
save(117,'\\scanpage{117}\n% archive foliation: 116\n'+'\n'.join(r),e,doubts=[('top row','third triple 4 over2','top4 overwritten','medium'),('lower six triples','3₂ preceded by cancelled2','first stroke may be a repeated3 rather than2','low'),('last five triples','2₁ in low entries','1₂; ink resembles2 followed by1','low'),('last label','eta','epsilon','low'),('top cancellations','(6,2)','dense crossing leaves fragments','low')],leads='Degree6 candidate partition triples; duplicate (6;(2²1²);321) joined by bracket and !. Five final variants labelled alpha,beta,gamma,delta,eta(?). Numerical enumerations require caution; cancelled and overwritten entries not regularised.')
