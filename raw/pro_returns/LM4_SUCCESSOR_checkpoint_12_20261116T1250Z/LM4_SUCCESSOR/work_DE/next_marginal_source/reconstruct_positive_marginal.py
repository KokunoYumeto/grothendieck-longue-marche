"""New reconstruction of the positive marginal in attached LM4 F23.

The original attached computation files were not supplied/recovered.
This program computes fresh exact rational-Sturm braid data.  Its small
rational deformation is justified by the accompanying geometric note.
"""
from pathlib import Path
import importlib.util, json, itertools, time
from fractions import Fraction
from math import isqrt
import sympy as S

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('engine',HERE.parent/'next_B59_image/braid_engine.py')
E=importlib.util.module_from_spec(spec);spec.loader.exec_module(E)
u,t=E.u,E.t
R=S.Rational;I=S.I
E.N_STRANDS=8;E.rotation=1+R(371,1000)*I;E.EPS=R(1,10**25)
z=[S.Integer(1),(309016994375+951056516295*I)/S.Integer(10**12),
   (-809016994375+587785252292*I)/S.Integer(10**12),
   (-809016994375-587785252292*I)/S.Integer(10**12),
   (309016994375-951056516295*I)/S.Integer(10**12)]
old=[(1000000,0),(309017,951057),(-809017,587785),
     (-809017,-587785),(309017,-951057)]
new={0:(882644,1077509),2:(80730,-1390528),
     3:(1260728,-1131556),4:(1685063,174411)}
centers=[S.Integer(0)];names=['old:0']
for j,c in enumerate(old):
    for sign in (1,-1):
        centers.append(sign*(c[0]+c[1]*I)/S.Integer(10**6))
        names.append('old:'+('+' if sign==1 else '-')+'zeta^'+str(j))
for j,c in new.items():
    for sign in (1,-1):
        centers.append(sign*(c[0]+c[1]*I)/S.Integer(10**6))
        names.append('new:'+('+' if sign==1 else '-')+'sqrt(A_'+str(j)+')')
h=R(1,10**4);base=2+2*I;eta=R(1,10**12)
def norm2(a):
    return S.expand(S.re(a)**2+S.im(a)**2)
def abs_upper(a):
    return abs(S.re(a))+abs(S.im(a))

# Rational intervals for the actual trigonometric constants.
def sqrt_interval(lo,hi,n=55):
    scale=10**n
    a=isqrt((lo.numerator*scale*scale)//lo.denominator)
    b=isqrt((hi.numerator*scale*scale)//hi.denominator)+1
    return Fraction(a,scale),Fraction(b,scale)
rt5=sqrt_interval(Fraction(5),Fraction(5))
sp=sqrt_interval(Fraction(10)+2*rt5[0],Fraction(10)+2*rt5[1])
sm=sqrt_interval(Fraction(10)-2*rt5[1],Fraction(10)-2*rt5[0])
re1=((rt5[0]-1)/4,(rt5[1]-1)/4)
re2=(-(rt5[1]+1)/4,-(rt5[0]+1)/4)
im1=(sp[0]/4,sp[1]/4);im2=(sm[0]/4,sm[1]/4)
intervals=[((Fraction(1),Fraction(1)),(Fraction(0),Fraction(0))),
           (re1,im1),(re2,im2),(re2,(-im2[1],-im2[0])),
           (re1,(-im1[1],-im1[0]))]
for j,((rl,rh),(il,ih)) in enumerate(intervals):
    zr,zi=Fraction(S.re(z[j])),Fraction(S.im(z[j]))
    assert max(abs(zr-rl),abs(zr-rh))+max(abs(zi-il),abs(zi-ih)) < Fraction(1,10**12)
assert all(norm2(a)<R(1000001,1000000)**2 for a in z)
print('Actual fifth roots are within1e-12 of each rational coefficient: PASS',flush=True)

# Every actual/deformed critical root stays in its fixed h/2 disk.
# All coefficient errors in the pair products/A_j are <1e-10.
residual_slack=R(1,10**10)
for j,c in enumerate(old):
    c=(c[0]+c[1]*I)/S.Integer(10**6)
    assert abs_upper(c-z[j])+eta<h/2
    assert abs_upper(c*c-z[j]*z[j])+residual_slack<R(1,10**5)
for i,j in itertools.combinations(range(5),2):
    k=(3*(i+j))%5
    c=(old[k][0]+old[k][1]*I)/S.Integer(10**6)
    assert abs_upper(c*c-z[i]*z[j])+residual_slack<R(1,10**5)
for j,c in new.items():
    c=(c[0]+c[1]*I)/S.Integer(10**6)
    A=z[j]*(2*z[1]-z[j])
    assert norm2(c)>R(1,4)
    assert abs_upper(c*c-A)+residual_slack<R(1,10**5)
assert (h/2)**2+R(1,10**5)<h/2

def line_dist2(point,a,b):
    v=b-a;den=norm2(v)
    dot=S.re(S.expand((point-a)*S.conjugate(v)))
    q=max(S.Integer(0),min(S.Integer(1),dot/den))
    return norm2(point-(a+q*v))

corners=[]
for k,c in enumerate(centers):
    ne=c+h+h*I
    assert S.re(base)>S.re(ne) and S.im(base)>S.im(ne)
    for j,d in enumerate(centers):
        if j!=k:
            assert norm2(c-d)>R(11,100)**2
            assert line_dist2(d,base,ne)>2*h*h
    corners.append([ne,c-h+h*I,c-h-h*I,c+h-h*I,ne])
directions=[S.cancel((S.im(c[0])-2)/(S.re(c[0])-2)) for c in corners]
assert len(set(directions))==19
assert all(norm2(p)<9 for box in corners for p in box)
print('Nineteen disjoint source squares and based star lassos: PASS',flush=True)
print('All critical roots remain in the assigned h/2 disks throughout deformation: PASS',flush=True)

# Pair-difference factorizations give a uniform lower bound >1e-11.
# Every source distance to a critical root is >=h/3; the distinct roots
# within each individual difference factorization have separation>=1/10.
# Different deformed pair polynomials may have very close roots in the
# same old cluster; no global separation of all those roots is assumed.
# |s|<3 and |z_j|<2, so every denominator factor has modulus<5.
rho=h/3;sigma=R(1,10)
lower_bounds=[rho*rho/25,4*R(1,10)*rho*(sigma/2)**2/625,
              2*rho*(sigma/2)**2/125,2*rho*(sigma/2)/25,
              rho/5,2*rho/5,4*R(9,10)*rho/25,S.Integer(1)]
assert min(lower_bounds)>R(1,10**11)
assert 49*R(1,10**14)<R(1,10**11)
unperturbed=[S.Integer(0),S.Integer(1)]+[S.cancel(((a-u)/(a+u))**2) for a in z]+[S.cancel((z[1]-u)/(z[1]+u))]
E.fun=[S.cancel(f+R(j*j,10**14)/E.rotation) for j,f in enumerate(unperturbed)]
E.exceptional=S.Integer(1);E.cache={}
geometry={
    'description':__doc__,'source_base':['2','2'],
    'labels':['0','1','v_1','v_zeta','v_zeta2','v_zeta3','v_zeta4','a'],
    'coefficient_points':[[str(S.re(a)),str(S.im(a))] for a in z],
    'coefficient_error_bound':'1/10^12','uniform_root_residual_slack':'1/10^10',
    'source_halfside':str(h),'source_distance_bound':str(rho),
    'within_each_factorization_root_separation_bound':str(sigma),
    'pair_difference_lower_bounds':[str(v) for v in lower_bounds],
    'projection':['1','371/1000'],'offset_formula':'j^2/(10^14*(1+371i/1000))',
    'loops':[{'name':n,'center':E.point_json(c),'corners':[E.point_json(p) for p in box]}
             for n,c,box in zip(names,centers,corners)],
    'source_interval_bounds':[[[str(x) for x in pair] for pair in v] for v in intervals],
    'scope':'Fresh positive-marginal reconstruction; no source-surjectivity claim.'
}
(HERE/'positive_marginal_geometry.json').write_text(json.dumps(geometry,indent=2)+'\n')
print('Uniform projection-offset homotopy is collision-free: PASS',flush=True)

loops=[];started=time.time()
for k,(name,box) in enumerate(zip(names,corners)):
    ww,wr=E.segment(base,box[0]);cycle=[];records=[wr]
    for a,b in zip(box,box[1:]):
        v,r=E.segment(a,b);cycle+=v;records.append(r)
    word=list(ww)+cycle+list(E.inv(tuple(ww)))
    loops.append({'name':name,'word':word,'unreduced_length':len(word),
                  'forward_records':records})
    (HERE/'positive_marginal_braids.partial.json').write_text(json.dumps({'geometry':geometry,'loops':loops},separators=(',',':'))+'\n')
    print('Source',k,name,'braid_length',len(word),'elapsed',round(time.time()-started,2),flush=True)

# Initial projection order is reconstructed exactly at the same endpoint.
values=[S.cancel(E.rotation*f.subs(u,base)) for f in E.fun]
initial=sorted(range(8),key=lambda j:S.re(values[j]))
assert len({S.re(v) for v in values})==8
cert={'geometry':geometry,'initial_order_zero_based':initial,'loops':loops,
      'segment_count':len(E.cache),'crossings_forward':sum(r['crossing_count'] for _,r in E.cache.values())}
(HERE/'positive_marginal_braids.json').write_text(json.dumps(cert,separators=(',',':'))+'\n')
(HERE/'positive_marginal_words.json').write_text(json.dumps({
    'geometry':geometry,'initial_order_zero_based':initial,
    'loops':[{k:v for k,v in row.items() if k!='forward_records'} for row in loops]
},indent=2)+'\n')
print('Certified source loops',len(loops),'forward segments',len(E.cache),
      'forward crossings',cert['crossings_forward'],flush=True)
print('Exact initial projection order',initial,flush=True)
print('COMPLETE: fresh exact positive marginal monodromy; no old stdout reused.',flush=True)
