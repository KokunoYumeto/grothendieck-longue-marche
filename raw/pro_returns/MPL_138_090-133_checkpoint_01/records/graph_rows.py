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
