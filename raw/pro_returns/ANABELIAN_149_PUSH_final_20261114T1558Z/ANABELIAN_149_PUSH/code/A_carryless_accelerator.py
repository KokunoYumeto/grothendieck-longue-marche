#!/usr/bin/env python3
"""Optional exact accelerator; the canonical mathematical engine is unchanged.

Compile the adjacent C source into a content-addressed /tmp shared
library. Verification compares every result with the separate canonical
shift-and-XOR implementation, including block boundaries and long inputs.
The caller may set A_theta_F4_moduli_scan.clmul=clmul to accelerate its exact
polynomial arithmetic. All certificates remain reproducible without this.
"""
from pathlib import Path
import ctypes,hashlib,json,random,subprocess,time

ROOT=Path(__file__).parent
SOURCE=ROOT/'A_carryless_accelerator.c'
DIGEST=hashlib.sha256(SOURCE.read_bytes()).hexdigest()
LIB=Path('/tmp')/('ANABELIAN_A_clmul_'+DIGEST[:16]+'.so')
if not LIB.exists():
    subprocess.run(['cc','-O3','-shared','-fPIC','-mpclmul','-msse2',str(SOURCE),'-o',str(LIB)],check=True)
_lib=ctypes.CDLL(str(LIB));_mul=_lib.a_clmul
_mul.argtypes=[ctypes.c_char_p,ctypes.c_size_t,ctypes.c_char_p,ctypes.c_size_t,ctypes.c_void_p]
_mul.restype=None

def canonical(a,b):
    if a.bit_length()<b.bit_length():a,b=b,a
    r=0
    while b:
        low=b&-b;r^=a<<(low.bit_length()-1);b^=low
    return r

def clmul(a,b):
    if not a or not b:return 0
    if min(a.bit_length(),b.bit_length())<=16:return canonical(a,b)
    na=(a.bit_length()+63)//64;nb=(b.bit_length()+63)//64
    aa=a.to_bytes(8*na,'little');bb=b.to_bytes(8*nb,'little')
    out=ctypes.create_string_buffer(8*(na+nb));_mul(aa,na,bb,nb,out)
    return int.from_bytes(out.raw,'little')

def main():
    rng=random.Random(14920261114);sizes=[0,1,2,15,16,17,31,32,63,64,65,127,128,129,255,256,257,511,512,513,1023,1024,1025,4095,4096,4097,8192,12000]
    tests=0;start=time.time()
    for a in sizes:
        for b in sizes:
            x=rng.getrandbits(a);y=rng.getrandbits(b)
            assert clmul(x,y)==canonical(x,y);tests+=1
    for a in [63,64,65,127,128,129,1023,1024,1025]:
        for b in [63,64,65,127,128,129,1023,1024,1025]:
            x=(1<<(a+1))-1;y=(1<<(b+1))-1
            assert clmul(x,y)==canonical(x,y);tests+=1
    assert clmul(0,0)==0
    out={'status':'PASS','source_sha256':DIGEST,'canonical_shift_XOR_comparisons':tests,
         'input_bit_lengths_through':12000,'runtime_seconds':time.time()-start,
         'semantics':'64x64 carryless block products accumulated by XOR; no modular reduction or numerical approximation.'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out)

if __name__=='__main__':main()
