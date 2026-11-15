#!/usr/bin/env python3
"""Exact arithmetic certificates for all 23 CDH lambencies.
No computer algebra packages, floating point, or downloaded tables are used.
Darts are primitive row vectors mod N modulo multiplication by units.
Permutations act on row vectors on the right. All q series are formal.
"""
from fractions import Fraction
from math import gcd, comb, isqrt
from collections import Counter
from pathlib import Path
import json

OUT=Path(__file__).resolve().parent
ROWS=[
('2','A_1^{24}',2,[],{2:24,1:-24}),
('3','A_2^{12}',3,[],{3:12,1:-12}),
('4','A_3^8',4,[],{4:8,1:-8}),
('5','A_4^6',5,[],{5:6,1:-6}),
('6','A_5^4D_4',6,[],{2:1,6:5,1:-5,3:-1}),
('7','A_6^4',7,[],{7:4,1:-4}),
('8','A_7^2D_5^2',8,[],{2:2,8:4,1:-4,4:-2}),
('9','A_8^3',9,[],{9:3,1:-3}),
('10','A_9^2D_6',10,[],{2:1,10:3,1:-3,5:-1}),
('12','A_{11}D_7E_6',12,[],{2:2,3:1,12:3,1:-3,4:-1,6:-2}),
('13','A_{12}^2',13,[],{13:2,1:-2}),
('16','A_{15}D_9',16,[],{2:1,16:2,1:-2,8:-1}),
('18','A_{17}E_7',18,[],{2:1,3:1,18:2,1:-2,6:-1,9:-1}),
('25','A_{24}',25,[],{25:1,1:-1}),
('6+3','D_4^6',6,[3],{2:6,6:6,1:-6,3:-6}),
('10+5','D_6^4',10,[5],{2:4,10:4,1:-4,5:-4}),
('14+7','D_8^3',14,[7],{2:3,14:3,1:-3,7:-3}),
('18+9','D_{10}E_7^2',18,[9],{2:3,3:2,18:3,1:-3,6:-2,9:-3}),
('22+11','D_{12}^2',22,[11],{2:2,22:2,1:-2,11:-2}),
('30+15','D_{16}E_8',30,[15],{2:2,3:1,5:1,30:2,1:-2,6:-1,10:-1,15:-2}),
('46+23','D_{24}',46,[23],{2:1,46:1,1:-1,23:-1}),
('12+4','E_6^4',12,[4],{2:4,3:4,12:4,1:-4,4:-4,6:-4}),
('30+6,10,15','E_8^3',30,[6,10,15],{2:3,3:3,5:3,30:3,1:-3,6:-3,10:-3,15:-3}),
]

def divisors(n): return [d for d in range(1,n+1) if n%d==0]
def units(n): return [a for a in range(n) if gcd(a,n)==1] if n>1 else [0]
def cycles(p):
    done=set(); out=[]
    for i in range(len(p)):
        if i not in done:
            c=[]; j=i
            while j not in done:
                c.append(j);done.add(j);j=p[j]
            assert j==i
            out.append(c)
    return out
def passport(p): return dict(sorted(Counter(map(len,cycles(p))).items()))
def inverse(p):
    ans=[None]*len(p)
    for i,j in enumerate(p):ans[j]=i
    return ans
def then(p,q): return [q[p[i]] for i in range(len(p))]
def orbits(perms,points):
    remaining=set(points);out=[]
    while remaining:
        seed=min(remaining);seen={seed};queue=[seed]
        for x in queue:
            for p in perms:
                y=p[x]
                if y not in seen:seen.add(y);queue.append(y)
        remaining-=seen;out.append(sorted(seen))
    return out

def dessin(N):
    un=units(N)
    def canon(v):return min(((a*v[0])%N,(a*v[1])%N) for a in un)
    darts=sorted({canon((a,b)) for a in range(N) for b in range(N) if gcd(gcd(a,b),N)==1})
    idx={v:i for i,v in enumerate(darts)}
    def perm(M):
        a,b,c,d=M
        return [idx[canon((x*a+y*c,x*b+y*d))] for x,y in darts]
    s=perm((0,-1,1,0));r=perm((0,-1,1,1));t=perm((1,1,0,1))
    assert then(s,r)==t
    assert then(s,s)==list(range(len(darts)))
    assert then(then(r,r),r)==list(range(len(darts)))
    mu=len(darts);e2=passport(s).get(1,0);e3=passport(r).get(1,0);c=len(cycles(t))
    gen=1+Fraction(mu,12)-Fraction(e2,4)-Fraction(e3,3)-Fraction(c,2)
    assert gen.denominator==1 and gen>=0
    a2=perm((1,2,0,1));b2=perm((1,0,-2,1))
    oo=orbits([a2,b2],range(mu));trip=[]
    for o in oo:
        ii={x:j for j,x in enumerate(o)}
        aa=[ii[a2[x]] for x in o];bb=[ii[b2[x]] for x in o]
        cc=inverse(then(aa,bb));trip.append({'degree':len(o),'dart_indices':o,'monodromy':[aa,bb,cc], 'passport':[passport(aa),passport(bb),passport(cc)]})
    assert len(oo)==(1 if N%2 else 3)
    assert all(len(o)==mu//len(oo) for o in oo)
    direct=None
    if N%4==0:
        a=perm((1,1,0,1));b=perm((1,0,-4,1));base=idx[canon((0,1))]
        o=next(o for o in orbits([a,b],range(mu)) if base in o)
        ii={x:j for j,x in enumerate(o)};aa=[ii[a[x]] for x in o];bb=[ii[b[x]] for x in o];cc=inverse(then(aa,bb))
        assert len(o)*6==mu
        direct={'degree':len(o),'dart_indices':o,'monodromy':[aa,bb,cc],'passport':[passport(aa),passport(bb),passport(cc)]}
    return {'darts':darts,'s':s,'r':r,'t':t,'passport':[passport(s),passport(r),passport(t)],'index':mu,'genus':int(gen),'elliptic_2':e2,'elliptic_3':e3,'tripod_basechange':trip,'tripod_direct':direct}

def cusp_list(N):
    cs=[]
    for d in divisors(N):
        f=gcd(d,N//d)
        for a in units(f):
            aa=a if a else 1
            while gcd(aa,d)!=1:aa+=f
            cs.append({'d':d,'a':a if f>1 else 1,'representative':[aa,d],'width':N//gcd(d*d,N),'conductor':f})
    return cs

def normalize_cusp(N,x,y):
    gg=gcd(x,y); x//=gg;y//=gg
    d=gcd(y,N);f=gcd(d,N//d)
    return (d,(x*(y//d))%f if f>1 else 1)

def AL_matrix(N,e):
    if e==1:return(1,0,0,1)
    m=N//e;de=pow(e,-1,m) if m>1 else 0;bb=(e*de-1)//m
    ans=(e,bb,N,e*de)
    assert ans[0]*ans[3]-ans[1]*ans[2]==e
    return ans

def eta_series(frame,M=30):
    a=[0]*(M+2);a[0]=1
    for d,k in frame.items():
        for m in range(1,(M+1)//d+1):
            step=d*m;power=-k;fac=[0]*(M+2)
            for j in range((M+1)//step+1):
                if power>=0:coef=(-1)**j*comb(power,j) if j<=power else 0
                else:coef=comb(-power+j-1,j)
                fac[j*step]=coef
            a=[sum(a[i-j]*fac[j] for j in range(i+1)) for i in range(M+2)]
    return {str(i-1):v for i,v in enumerate(a)}

def field_label(f):return 'Q' if f<=2 else f'Q(zeta_{f})'

def analyse(row):
    label,roots,N,added,frame=row;de=dessin(N);cs=cusp_list(N);idx={(c['d'],c['a']):i for i,c in enumerate(cs)}
    assert Counter(c['width'] for c in cs)==Counter({int(k):v for k,v in de['passport'][2].items()})
    perms={};matrices={}
    for e in [1]+added:
        M=AL_matrix(N,e);matrices[e]=M
        p=[]
        for c in cs:
            x,y=c['representative'];a,b,cc,d=M
            key=normalize_cusp(N,a*x+b*y,cc*x+d*y);p.append(idx[key])
        assert then(p,p)==list(range(len(cs)))
        for i,j in enumerate(p):
            assert cs[j]['d']==e*cs[i]['d']//gcd(e,cs[i]['d'])**2
            assert cs[j]['conductor']==cs[i]['conductor']
        perms[e]=p
    for e in perms:
        for f in perms:
            ef=e*f//gcd(e,f)**2
            assert ef in perms and then(perms[e],perms[f])==perms[ef]
    oo=orbits(list(perms.values()),range(len(cs)))
    # Newman congruences and character; exact Ligozat orders.
    r={d:-k for d,k in frame.items()}
    assert sum(r.values())==0
    assert sum(d*a for d,a in r.items())%24==0
    assert sum((N//d)*a for d,a in r.items())%24==0
    square=Fraction(1)
    for d,a in r.items():square*=Fraction(d)**a
    assert isqrt(square.numerator)**2==square.numerator and isqrt(square.denominator)**2==square.denominator
    for c in cs:
        d=c['d'];order=Fraction(N,24)*sum(Fraction(gcd(d,delta)**2*a,gcd(d,N//d)*d*delta) for delta,a in r.items())
        assert order.denominator==1;c['eta_order']=int(order);c['field']=field_label(c['conductor'])
    assert sum(c['eta_order'] for c in cs)==0
    for p in perms.values(): assert all(cs[i]['eta_order']==cs[p[i]]['eta_order'] for i in range(len(cs)))
    poles=[i for i,c in enumerate(cs) if c['eta_order']<0]
    inf=idx[(N,1)]
    po=next(o for o in oo if inf in o)
    assert poles==po and len(po)==len(perms) and all(cs[i]['eta_order']==-1 for i in po)
    qo=[]
    for o in oo:
        f=cs[o[0]]['conductor']; assert all(cs[i]['conductor']==f for i in o)
        stabilizer=[]
        for u in units(f):
            go=sorted(idx[(cs[i]['d'], (cs[i]['a']*u)%f if f>1 else 1)] for i in o)
            if go==o:stabilizer.append(u)
        degree=len(units(f))//len(stabilizer)
        field='Q' if degree==1 else field_label(f) if len(stabilizer)==1 else f'Q(zeta_{f})^<{stabilizer}>'
        qo.append({'indices':o,'gal_stabilizer':stabilizer,'field_degree':degree,'field':field})
    if added:
        # All possible nonidentity cosets have trace sqrt(e)*integer.
        # The sole e=3 coset has a+d even by its determinant equation.
        assert all(e>=4 or (N,e)==(6,3) for e in added)
        e3=0;e2=2*(Fraction(de['index'],6*len(perms))+2-len(oo))
        assert e2.denominator==1 and e2>=0;e2=int(e2)
    else:e2=de['elliptic_2'];e3=de['elliptic_3']
    assert de['genus']==0 if not added else True
    qs=eta_series(frame)
    assert qs['-1']==1 and qs['0']==frame[1]
    # Fixed-point certificates for constant-one Atkin-Lehner multipliers.
    invariance=[]
    for e in added:
        if (N,e)==(12,4):
            fixed=[i for i,j in enumerate(perms[e]) if i==j and cs[i]['eta_order']==0]
            assert fixed;invariance.append({'e':e,'fixed_finite_nonzero_cusp':fixed[0]})
        elif (N,e)==(30,10):
            assert 6 in added and 15 in added and 6*15//gcd(6,15)**2==10
            invariance.append({'e':e,'product':[6,15]})
        else:
            m=N//e
            aa=next(a for a in range(1,m+1) if (e*a*a+1)%m==0)
            bb=-(e*aa*aa+1)//m
            # [e*a,b;N,-e*a] has determinant e and trace zero.
            M=(e*aa,bb,N,-e*aa)
            assert M[0]*M[3]-M[1]*M[2]==e
            invariance.append({'e':e,'elliptic_matrix':M})
    return {'lambency':label,'roots':roots,'N':N,'S':[1]+added,'frame':frame,'dessin':de,'cusps':cs,'Atkin_Lehner_matrices':matrices,'Atkin_Lehner_permutations':perms,'cusp_orbits':qo,'signature':{'genus':0,'e2':e2,'e3':e3,'cusps':len(oo)},'eta_character_square':str(square),'eta_series':qs,'Atkin_Lehner_invariance':invariance}

def ps(p):return ' '.join(str(k)+(f'^{v}' if v>1 else '') for k,v in p.items())
def pst(p):return ' '.join(str(k)+(f'^{{{v}}}' if v>1 else '') for k,v in p.items())
def cusp_name(c):return f"{c['representative'][0]}/{c['representative'][1]}" if c['d']!=1 else '0'
def main():
    ans=[analyse(r) for r in ROWS]
    (OUT/'d_lambencies.json').write_text(json.dumps(ans,indent=2)+'\n')
    lines=['# Exact lambency certificate','', '|lambency|mu|g(X0)|passport 2|passport 3|cusp widths|signature (g;e2,e3;c)|T constant,q|','|---|---:|---:|---|---|---|---|---|']
    for a in ans:
        d=a['dessin'];s=a['signature'];q=a['eta_series'];lines.append(f"|{a['lambency']}|{d['index']}|{d['genus']}|{ps(d['passport'][0])}|{ps(d['passport'][1])}|{ps(d['passport'][2])}|(0;{s['e2']},{s['e3']};{s['cusps']})|{q['0']}, {q['1']}|")
    for a in ans:
        lines += ['',f"## {a['lambency']}: {a['roots']}",'', 'Cusps: '+', '.join(f"{i}={cusp_name(c)} [w={c['width']};{c['field']};ord T={c['eta_order']}]" for i,c in enumerate(a['cusps']))]
        for e,p in a['Atkin_Lehner_permutations'].items():
            if e!=1:lines.append(f'W_{e} cycles (cusp indices): {cycles(p)}')
        lines.append('Quotient cusp orbits / residue fields: '+repr([(o['indices'],o['field']) for o in a['cusp_orbits']]))
        if a['dessin']['tripod_direct']:
            v=a['dessin']['tripod_direct'];lines.append(f"Direct X0(N) -> X0(4): degree {v['degree']}, passport "+repr(v['passport']))
        lines.append('Normalized base change to X(2): '+repr([(t['degree'],t['passport']) for t in a['dessin']['tripod_basechange']]))
        lines.append('q expansion q^-1 through q^8: '+repr({k:v for k,v in a['eta_series'].items() if int(k)<=8}))
    (OUT/'d_lambencies.md').write_text('\n'.join(lines)+'\n')
    # One compact LaTeX table; individual cusp/orbit table kept in a separate complete appendix.
    tex=[r'\begin{longtable}{r|r|r|l|l|l|l}',r'$\ell$ & $\mu$ & $g_0$ & $\sigma_2$ & $\sigma_3$ & cusp widths & $(e_2,e_3;c)$\\\hline']
    for a in ans:
        d=a['dessin'];s=a['signature'];tex.append(f"${a['lambency']}$ & {d['index']} & {d['genus']} & ${pst(d['passport'][0])}$ & ${pst(d['passport'][1])}$ & ${pst(d['passport'][2])}$ & $({s['e2']},{s['e3']};{s['cusps']})$\\\\")
    tex.append(r'\end{longtable}')
    (OUT/'d_lambencies_table.tex').write_text('\n'.join(tex)+'\n')
    print('\n'.join(lines[:27]))
    print('\nAll 23 rows pass: permutation relations; widths; cusp classifications; Atkin-Lehner group law; Newman conditions; exact integral cusp orders; single simple pole orbit; Galois orbit fields; q series through q^30.')

if __name__=='__main__':main()
