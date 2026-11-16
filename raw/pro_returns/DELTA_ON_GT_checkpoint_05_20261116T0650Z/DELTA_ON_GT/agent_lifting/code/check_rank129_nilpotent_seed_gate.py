"""Normal nilpotent-image gate for actual controlled R2 seeds.
Exact 16D boundary/proper extension, joined with signed SL2(F3).
Written by GPT-6 Astra, OpenAI, 16 November 2026.
"""
from pathlib import Path
import json,numpy as np
HERE=Path(__file__).resolve().parents[1]
D=np.load(HERE.parent/'agent_five'/'ferrari_harmonic16_module.npz')
I2=(1,0,0,1);Z2=(2,0,0,2)
Q0=(0,1,2,3)+I2*8
W=[tuple(map(int,v))for v in D['kernel_basis']]
def m2(a,b):return tuple((a[2*i]*b[j]+a[2*i+1]*b[2+j])%3 for i in range(2)for j in range(2))
def i2(a):
 d=(a[0]*a[3]-a[1]*a[2])%3;assert d
 return(d*a[3]%3,-d*a[1]%3,-d*a[2]%3,d*a[0]%3)
def qm(g,h):
 p=g[:4];q=h[:4];out=tuple(p[q[j]]for j in range(4))
 for off in(4,20):
  out+=tuple(x for j in range(4)for x in m2(g[off+4*q[j]:off+4*q[j]+4],h[off+4*j:off+4*j+4]))
 return out
def qi(g):
 p=g[:4];ip=tuple(p.index(j)for j in range(4));out=ip
 for off in(4,20):out+=tuple(x for j in range(4)for x in i2(g[off+4*ip[j]:off+4*ip[j]+4]))
 return out
def act(g,v):
 out=[0]*16
 for j in range(4):
  k=g[j];value=m2(m2(g[4+4*j:8+4*j],v[4*j:4*j+4]),i2(g[20+4*j:24+4*j]))
  out[4*k:4*k+4]=value
 return tuple(out)
J0=Q0+I2
def jm(g,h):return qm(g[:36],h[:36])+m2(g[36:],h[36:])
def ji(g):return qi(g[:36])+i2(g[36:])
def jp(*gg):
 r=J0
 for g in gg:r=jm(r,g)
 return r
def jc(g,h):return jp(g,h,ji(g),ji(h))
def closure(gens,bound):
 out=[J0];seen={J0}
 for g in out:
  for h in gens:
   k=jm(g,h)
   if k not in seen:
    seen.add(k);out.append(k)
    assert len(out)<=bound
 return out,seen
def normal_closure(seeds,ambient_gens,bound):
 gens=[];G=[J0];seen={J0}
 for s in seeds:
  if s not in seen:gens.append(s);G,seen=closure(gens,bound)
 j=0
 while j<len(gens):
  g=gens[j];j+=1
  for h in ambient_gens:
   z=jp(h,g,ji(h))
   if z not in seen:gens.append(z);G,seen=closure(gens,bound)
 assert all(jp(h,g,ji(h))in seen for g in gens for h in ambient_gens)
 return G,gens
def basis(rows):
 piv={}
 for vv in rows:
  v=list(vv)
  for j,w in sorted(piv.items()):
   z=v[j]
   if z:v=[(a-z*b)%3 for a,b in zip(v,w)]
  nz=[j for j,a in enumerate(v)if a]
  if nz:
   j=nz[0];z=v[j];piv[j]=tuple(z*a%3 for a in v)
 return list(piv.values())
qgens=[tuple(map(int,g))for g in D['generator_bases']]
gens=[qgens[0]+(1,2,0,1),qgens[1]+(1,0,1,1)]
assert all(jp(g,ji(g))==J0 for g in gens)
module_comm=basis([tuple((a-b)%3 for a,b in zip(act(g,w),w))for g in qgens for w in W])
assert len(module_comm)==4
first,fgens=normal_closure([jc(gens[0],gens[1])],gens,384*8)
second,sgens=normal_closure([jc(g,h)for g in fgens for h in fgens],fgens,64*2)
assert all(jc(g,h)in set(second)for g in fgens for h in fgens)
negative=[g for g in second if g[36:]==Z2]
centralizing=[g for g in negative if all(act(g[:36],w)==w for w in W)]
out={'harmonic_character_orbit':[1,7,18,20],'normal_three_module_dimension':4,
     'module_commutator_dimension':len(module_comm),
     'joint_with_signed_SL2F3_first_derived_order':len(first),
     'joint_with_signed_SL2F3_second_derived_order':len(second),
     'second_derived_elements_over_negative_identity':len(negative),
     'such_elements_centralizing_entire_normal_three_module':len(centralizing),
     'centralizing_candidates':centralizing,
     'criterion':'A normal nilpotent image has its characteristic Sylow2 subgroup normal in the whole image; it centralizes every normal3 subgroup. A controlled seed in F second derived with compact projection -I must therefore give one of the centralizing candidates.',
     'scope':'Necessary gate for actual R2 residual seeds, not a pentagon/sign theorem or a finite GT-candidate test.'}
(HERE/'records'/'rank129_nilpotent_seed_gate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
