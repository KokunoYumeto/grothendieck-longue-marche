#!/usr/bin/env python3
"""Rank-one extension of the exact C divisor arithmetic wrapper.
The fixed A.C2.25 sources and witness data are not modified.
"""
from pathlib import Path
import ctypes,hashlib,json,subprocess,random,time

ROOT=Path(__file__).parent;SRC=ROOT/'A_rank_one_theta.c';HASH=hashlib.sha256(SRC.read_bytes()).hexdigest();SO=Path('/tmp')/('A_large_theta_'+HASH[:16]+'.so')
if not SO.exists():subprocess.run(['cc','-O3','-shared','-fPIC',str(SRC),'-o',str(SO)],check=True)
lib=ctypes.CDLL(str(SO))

class Div(ctypes.Structure):
    _fields_=[('d',ctypes.c_uint32),('u',ctypes.c_uint32*3),('v',ctypes.c_uint32*2)]
    def key(self):return self.d,tuple(self.u),tuple(self.v)
    def lists(self):
        v=list(self.v[:self.d])
        while v and not v[-1]:v.pop()
        return list(self.u[:self.d+1]),v
    @classmethod
    def from_lists(cls,D):
        u,v=D;r=cls();r.d=len(u)-1
        for i,x in enumerate(u):r.u[i]=x
        for i,x in enumerate(v):r.v[i]=x
        return r

P=ctypes.POINTER(Div);U=ctypes.c_uint32;L=ctypes.c_uint64
for name,args,rest in [
 ('a_init',[U,U],ctypes.c_int),('a_set_rank_one',[U,U],ctypes.c_int),('a_alpha',[],U),('a_field_mul',[U,U],U),
 ('a_field_inv',[U],U),('a_field_pow',[U,L],U),('a_asroot',[U],U),
 ('a_add',[P,P,P],ctypes.c_int),('a_neg',[P,P],ctypes.c_int),
 ('a_times',[P,L,P],ctypes.c_int),('a_check',[P],ctypes.c_int),
 ('a_point_eta',[U,U,P],ctypes.c_int),('a_curve_point',[U,ctypes.POINTER(U)],ctypes.c_int)]:
    f=getattr(lib,name);f.argtypes=args;f.restype=rest

class Field:
    def __init__(self,e,mod):
        self.e=e;self.q=1<<e;self.mod=mod;self.generator=lib.a_init(e,mod);assert self.generator>0;self.alpha=lib.a_alpha()
    def mul(self,a,b):return int(lib.a_field_mul(a,b))
    def inv(self,a):assert a;return int(lib.a_field_inv(a))
    def pow(self,a,n):return int(lib.a_field_pow(a,n))
    def point(self,x):
        y=U();ok=lib.a_curve_point(x,ctypes.byref(y));return (ok,int(y.value))

ZERO=Div.from_lists(([1],[]))
def add(a,b):
    r=Div();assert lib.a_add(ctypes.byref(a),ctypes.byref(b),ctypes.byref(r))==0;return r
def neg(a):
    r=Div();assert lib.a_neg(ctypes.byref(a),ctypes.byref(r))==0;return r
def times(a,n):
    r=Div();assert lib.a_times(ctypes.byref(a),n,ctypes.byref(r))==0;return r
def eta(x,y):
    r=Div();assert lib.a_point_eta(x,y,ctypes.byref(r))==0;return r

def check():
    from A_theta_F4_moduli_witnesses import Base,pmul,peval
    from A_theta_F4_remaining_Jacobian import Jacobian
    rng=random.Random(1490918);tests=0;start=time.time()
    for e,mod in [(6,67),(8,283)]:
        F=Field(e,mod);B=Base(e,mod);alpha=F.alpha;J=Jacobian(B,[1,1,1]);J.h=[alpha,1,1];J.f=pmul(J.h,[B.mul(alpha,alpha),1,1,1],B);J.T=(J.h,[])
        points=[]
        for x in range(F.q):
            ok,y=F.point(x)
            if ok!=1:continue
            a=eta(x,y);Y=B.mul(peval(J.h,x,B),y);b=J.add(J.check(([x,1],[Y] if Y else [])),J.T)
            assert a.lists()==b and lib.a_check(ctypes.byref(a))==0;points.append((a,b));tests+=1
        for _ in range(300):
            a,b=rng.choice(points);c,d=rng.choice(points)
            assert add(a,c).lists()==J.add(b,d);tests+=1
            n=rng.randrange(10000);assert times(a,n).lists()==J.times(b,n);tests+=1
    out={'status':'PASS','C_source_sha256':HASH,'canonical_divisor_comparisons':tests,'fields':[64,256],'runtime_seconds':time.time()-start}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out)

if __name__=='__main__':check()
