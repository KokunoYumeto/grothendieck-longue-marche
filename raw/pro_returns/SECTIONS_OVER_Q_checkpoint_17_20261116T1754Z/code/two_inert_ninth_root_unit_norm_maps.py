#!/usr/bin/env python3
"""Actual norm operators on the complete A199 unit quotient."""
from pathlib import Path
import runpy,json
import sympy as S
B=Path(__file__).resolve().parent
C=runpy.run_path(str(B/'two_inert_ninth_root_full_units_certificate.py'))
finite=C['finite_value']; es=C['es']; uv=C['uv'];anti=C['anti'];r=C['v']['rr'];s=C['ss'];d=C['d']
columns=C['columns']; fixed=C['fixed_rows'];rank=C['rank']

def values(p,t,z):
    om=pow(z,3,p)
    vals=[finite(e,p,t,z)for e in es]
    for j in range(3):
        tj=t*pow(z,j,p)%p;aj=pow(tj,3,p)*pow(d*d,-1,p)%p
        pi=aj*aj*pow(om-1,-1,p)%p;tp=-om*pi%p
        ve=(1+pi)*pow(1+pi*pi,-1,p)%p;tv=(1+tp)*pow(1+tp*tp,-1,p)%p
        vals += [finite(u,p,tj,z)for u in uv]+[ve*pow(tv,-1,p)%p]+[finite(a,p,tj,z)for a in anti]
    vals += [finite(r,p,t*pow(z,j,p)%p,z)for j in range(9)]
    vals += [finite(s,p,t*pow(z,j,p)%p,z)for j in range(9)]
    assert all(vals)
    return vals

norm_h=[];norm_sigma=[];rows=[]
for p,t,z in fixed:
    logs={1:0,pow(z,3,p):1,pow(z,6,p):2}
    hh=[values(p,t,pow(z,4**j,p))for j in range(3)]
    ss=[values(p,t*pow(z,3*j,p)%p,z)for j in range(3)]
    a=[];b=[]
    for k in range(51):
        x=1;y=1
        for j in range(3):x=x*hh[j][k]%p;y=y*ss[j][k]%p
        a.append(logs[pow(x,(p-1)//3,p)])
        b.append(logs[pow(y,(p-1)//3,p)])
    norm_h.append(a);norm_sigma.append(b)
    rows.append({'p':p,'t':t,'zeta9':z,'norm_h_row':a,'norm_sigma_row':b})
rh=rank(norm_h);rs=rank(norm_sigma)
assert rh==rank([[row[j-1]for j in columns]for row in norm_h])
assert rs==rank([[row[j-1]for j in columns]for row in norm_sigma])
print('EXACT complete-cube-quotient norm ranks: h=',rh,' sigma=',rs)
print('Norm M/E2 target image dimension including Norm(zeta9)=zeta3:',rh+1)
print('Norm M/Fprime target image dimension:',rs)
assert (rh,rs)==(6,4)

def solve_injective(A,Y):
    m=[[x%3 for x in row]+[x%3 for x in y]for row,y in zip(A,Y)]
    n=len(A[0]); r=0
    for j in range(n):
        k=next(k for k in range(r,len(m))if m[k][j])
        m[r],m[k]=m[k],m[r]
        iv=pow(m[r][j],-1,3);m[r]=[iv*x%3 for x in m[r]]
        for k in range(len(m)):
            if k!=r:
                q=m[k][j];m[k]=[(x-q*y)%3 for x,y in zip(m[k],m[r])]
        r+=1
    assert all(not any(row)for row in m[r:])
    return [row[n:]for row in m[:n]]

R=C['matrix']
hc=solve_injective([row[9:17]for row in R],norm_h)
sc=solve_injective([row[:9]for row in R],norm_sigma)
ha=[[0,0,0,0,0,0,1,0],[0,0,0,0,0,2,0,1]]
sa=[[1,1,2,1,1,0,0,0,0],[1,2,0,0,0,1,0,0,0],
    [0,0,0,0,0,0,1,0,0],[0,1,1,2,0,0,0,1,0],
    [2,2,1,0,0,0,0,0,1]]
def matmul(a,b):
    return [[sum(x*y for x,y in zip(row,col))%3 for col in zip(*b)]for row in a]
assert not any(x for row in matmul(ha,hc)for x in row)
assert not any(x for row in matmul(sa,sc)for x in row)
assert rank(ha)==2 and rank(sa)==5
assert rank(hc)==6 and rank(sc)==4
hcols=[5,7,34,43,44,45];scols=[34,43,44,45]
hm=[[row[j-1]for j in hcols]for row in hc]
sm=[[row[j-1]for j in scols]for row in sc]
assert rank(hm)==6 and rank(sm)==4
qdata=json.loads((B/'two_inert_zeta9_base_units_certificate_data.json').read_text())
q=[x['row']for x in qdata['tame_rows']]
assert rank(q)==3 and rank(q[:3])==3
assert not any(x for row in matmul(q,sc)for x in row)
factor=list(map(list,zip(*solve_injective(list(map(list,zip(*sa))),list(map(list,zip(*q[:3])))))))
assert matmul(factor,sa)==q[:3] and rank(factor)==3
field_units=[[0,1,0,0,0,0,0,0,0],[0,0,1,2,0,0,0,0,0]]
assert not any(x for row in matmul(q,list(map(list,zip(*field_units))))for x in row)
support_images=matmul(sa,list(map(list,zip(*field_units))))
assert rank(support_images)==2
assert not any(x for row in matmul(factor,support_images)for x in row)
print('PASS: exact h image x_r3=0, x_r4=x_r2; zeta3 is Norm_h(zeta9).')
print('PASS: exact sigma five-row annihilator, rank3 tame quotient, and support-kernel basis e2,e3/e4.')
print('TAME_QUOTIENT_FACTOR',factor)
data={'h':'t fixed, zeta9 maps to zeta9^4; M/E2',
      'sigma':'t maps to zeta3*t, zeta9 fixed; M/Fprime',
      'rows':rows,'norm_h_restricted_rank':rh,'norm_sigma_restricted_rank':rs,
      'norm_M_E2_target_dimension':rh+1,'norm_M_Fprime_target_dimension':rs,
      'h_coordinates':hc,'sigma_coordinates':sc,'h_annihilator':ha,'sigma_annihilator':sa,
      'h_basis_columns_1based':hcols,'sigma_basis_columns_1based':scols,
      'h_basis_matrix':hm,'sigma_basis_matrix':sm,
      'tame_quotient_factor':factor,'support_kernel_unit_coordinates':field_units,
      'support_kernel_images':support_images}
(B/'two_inert_ninth_root_unit_norm_maps_data.json').write_text(json.dumps(data,indent=2)+'\n')
