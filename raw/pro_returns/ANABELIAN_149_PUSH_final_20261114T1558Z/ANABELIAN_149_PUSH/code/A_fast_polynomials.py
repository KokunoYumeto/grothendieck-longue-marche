#!/usr/bin/env python3
"""Optional exact C arithmetic behind the unchanged canonical Hankel engine.

Every operation has the same bit-plane representation as Arithmetic. The C
source performs ordinary finite-field scalar multiplication, block carryless
convolution, and leading-term long division. The Python verifier compares
both operations with the separate canonical implementations, including
nonmonic divisors, zero remainders, and binary-word boundaries.
"""
from pathlib import Path
import ctypes,json,random,time
import A_theta_F4_moduli_scan as scan
from A_carryless_accelerator import _lib,DIGEST

_mul=_lib.a_gf_mul
_mul.argtypes=[ctypes.c_uint,ctypes.c_uint,ctypes.c_char_p,ctypes.c_size_t,ctypes.c_char_p,ctypes.c_size_t,ctypes.c_void_p]
_mul.restype=ctypes.c_int
_div=_lib.a_gf_div
_div.argtypes=[ctypes.c_uint,ctypes.c_uint,ctypes.c_char_p,ctypes.c_size_t,ctypes.c_long,ctypes.c_char_p,ctypes.c_size_t,ctypes.c_long,ctypes.c_void_p,ctypes.c_void_p]
_div.restype=ctypes.c_int

def packed(a,n):return b''.join(x.to_bytes(8*n,'little') for x in a)
def unpacked(buffer,e,n):
    raw=buffer.raw
    return tuple(int.from_bytes(raw[8*n*i:8*n*(i+1)],'little') for i in range(e))

class FastArithmetic(scan.Arithmetic):
    def mul(self,a,b):
        da,db=self.deg(a),self.deg(b)
        if da<0 or db<0:return self.zero
        if da==0:return self.scale(b,self.leading(a))
        if db==0:return self.scale(a,self.leading(b))
        na=(da+64)//64;nb=(db+64)//64;nc=na+nb
        out=ctypes.create_string_buffer(self.e*nc*8)
        assert _mul(self.e,self.mod,packed(a,na),na,packed(b,nb),nb,out)==0
        return unpacked(out,self.e,nc)
    def divmod(self,a,b):
        da,db=self.deg(a),self.deg(b);assert db>=0
        if da<db:return self.zero,a
        if db==0:return self.scale(a,self.inv[self.leading(b)]),self.zero
        na=(da+64)//64;nb=(db+64)//64
        q=ctypes.create_string_buffer(self.e*na*8);r=ctypes.create_string_buffer(self.e*na*8)
        assert _div(self.e,self.mod,packed(a,na),na,da,packed(b,nb),nb,db,q,r)==0
        return unpacked(q,self.e,na),unpacked(r,self.e,na)

def main():
    rng=random.Random(14920261115);tests=0;start=time.time()
    for e,mod in [(2,7),(4,19),(6,67)]:
        slow=scan.Arithmetic(e,mod);fast=FastArithmetic(e,mod)
        for da in [0,1,15,63,64,65,127,128,129,255,511,1023,2047]:
            for db in [0,1,31,63,64,65,129]:
                a=tuple(rng.getrandbits(da+1) for _ in range(e));b=tuple(rng.getrandbits(db+1) for _ in range(e))
                if b==slow.zero:b=slow.one
                product=fast.mul(a,b);assert product==slow.mul(a,b);tests+=1
                assert fast.divmod(a,b)==slow.divmod(a,b);tests+=1
                assert fast.divmod(product,b)==(a,slow.zero);tests+=1
    out={'status':'PASS','source_sha256':DIGEST,'independent_operation_comparisons':tests,
         'fields':[4,16,64],'maximum_input_degree':2047,'runtime_seconds':time.time()-start}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out)

if __name__=='__main__':main()
