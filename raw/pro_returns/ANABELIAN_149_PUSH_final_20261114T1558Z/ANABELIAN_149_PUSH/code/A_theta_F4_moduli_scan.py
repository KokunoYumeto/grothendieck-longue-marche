#!/usr/bin/env python3
"""Exact exploratory theta-n Hankel scan on all 48 ordinary F4 moduli triples.

Every monic cubic over F4 with nonzero constant encodes a Frobenius-stable
unordered nonzero coefficient triple. The roots lie in F4, F16, or F64.
The complete geometric theta-n criterion is proved in A_theta_Hankel_scan.md.
All arithmetic below is exact, self-contained, and uses binary polynomial masks.
A positive result requires all maximal minors; a negative result stops only
when their partial gcd is already a unit away from t=0,1.
"""
from pathlib import Path
from itertools import combinations_with_replacement
import argparse,json,time


def clmul(a,b):
    if a.bit_length()<b.bit_length():a,b=b,a
    r=0
    while b:
        low=b&-b;r^=a<<(low.bit_length()-1);b^=low
    return r

class Arithmetic:
    def __init__(self,e,mod):
        self.e=e;self.mod=mod;self.q=1<<e
        self.zero=(0,)*e;self.one=(1,)+(0,)*(e-1)
        self.x=(2,)+(0,)*(e-1)
        self.mt=[[self.fmul_slow(a,b) for b in range(self.q)] for a in range(self.q)]
        self.inv=[0]+[next(b for b in range(1,self.q) if self.mt[a][b]==1) for a in range(1,self.q)]
        self.low=[i for i in range(e) if (mod>>i)&1]
        self.scales=[[self.mt[c][1<<i] for i in range(e)] for c in range(self.q)]
        self.alpha=next(a for a in range(2,self.q) if self.mt[a][a]^a^1==0)
        self.f4=[0,1,self.alpha,self.alpha^1]
        self.f4code={a:i for i,a in enumerate(self.f4)}
        self.checks=0
        for a in range(1,self.q):
            assert self.mt[a][self.inv[a]]==1;self.checks+=1
    def fmul_slow(self,a,b):
        r=0
        while b:
            if b&1:r^=a
            a<<=1
            if a&self.q:a^=self.mod
            b>>=1
        return r
    def fpow(self,a,n):
        r=1
        while n:
            if n&1:r=self.mt[r][a]
            a=self.mt[a][a];n>>=1
        return r
    def add(self,a,b):return tuple(x^y for x,y in zip(a,b))
    def deg(self,a):return max(v.bit_length() for v in a)-1
    def const(self,c):return tuple((c>>i)&1 for i in range(self.e))
    def shift(self,a,k):return tuple(v<<k for v in a)
    def scale(self,a,c):
        if c==0:return self.zero
        if c==1:return a
        out=[0]*self.e
        for mask,basis in zip(a,self.scales[c]):
            if mask:
                while basis:
                    low=basis&-basis;out[low.bit_length()-1]^=mask;basis^=low
        return tuple(out)
    def mul(self,a,b):
        raw=[0]*(2*self.e-1)
        for i,x in enumerate(a):
            if x:
                for j,y in enumerate(b):
                    if y:raw[i+j]^=clmul(x,y)
        for k in range(2*self.e-2,self.e-1,-1):
            if raw[k]:
                for j in self.low:raw[k-self.e+j]^=raw[k]
        return tuple(raw[:self.e])
    def square(self,a):
        # Squaring doubles polynomial exponents and squares each field basis.
        out=[0]*self.e
        for i,v in enumerate(a):
            z=0
            while v:
                low=v&-v;z^=1<<(2*(low.bit_length()-1));v^=low
            basis=self.mt[1<<i][1<<i]
            while basis:
                low=basis&-basis;out[low.bit_length()-1]^=z;basis^=low
        return tuple(out)
    def leading(self,a):
        d=self.deg(a);return sum(((v>>d)&1)<<i for i,v in enumerate(a))
    def divmod(self,a,b):
        assert b!=self.zero
        db=self.deg(b);ib=self.inv[self.leading(b)]
        monic=self.scale(b,ib);q=self.zero;r=a
        multiples=[self.scale(monic,c) for c in range(self.q)]
        while r!=self.zero and self.deg(r)>=db:
            k=self.deg(r)-db;c=self.leading(r)
            r=self.add(r,self.shift(multiples[c],k))
            q=self.add(q,self.shift(self.const(c),k))
        return self.scale(q,ib),r
    def exactdiv(self,a,b):
        q,r=self.divmod(a,b);assert r==self.zero,(self.deg(a),self.deg(b),r)
        return q
    def gcd(self,a,b):
        while b!=self.zero:a,b=b,self.divmod(a,b)[1]
        return self.scale(a,self.inv[self.leading(a)]) if a!=self.zero else self.zero
    def power(self,a,n):
        r=self.one
        while n:
            if n&1:r=self.mul(r,a)
            a=self.square(a);n>>=1
        return r
    def det(self,M):
        M=[row[:] for row in M];n=len(M);prev=self.one
        for k in range(n-1):
            if M[k][k]==self.zero:
                i=next((i for i in range(k+1,n) if M[i][k]!=self.zero),None)
                if i is None:return self.zero
                M[k],M[i]=M[i],M[k]
            pivot=M[k][k]
            for i in range(k+1,n):
                for j in range(k+1,n):
                    M[i][j]=self.exactdiv(self.add(self.mul(pivot,M[i][j]),self.mul(M[i][k],M[k][j])),prev)
                M[i][k]=self.zero
            prev=pivot
        return M[-1][-1]
    def maximal_gcd(self,M):
        """All maximal-minor ideal via one augmented Bareiss solve.

        Choose an invertible square block A and remaining row b. Bareiss on
        [A^t|b^t], followed by exact back substitution, computes
        det(A) A^{-t}b^t. Its entries are the other signed maximal minors.
        Signs are one in characteristic two. Every intermediate division
        is asserted exact; stopping at a unit gcd is conclusive.
        """
        s=len(M[0]);assert len(M)==s+1
        for omitted in [0,s]+list(range(1,s)):
            indices=[i for i in range(s+1) if i!=omitted]
            A=[M[i] for i in indices];b=M[omitted]
            T=[[A[j][i] for j in range(s)]+[b[i]] for i in range(s)]
            prev=self.one;singular=False
            for k in range(s-1):
                if T[k][k]==self.zero:
                    i=next((i for i in range(k+1,s) if T[i][k]!=self.zero),None)
                    if i is None:singular=True;break
                    T[k],T[i]=T[i],T[k]
                pivot=T[k][k]
                for i in range(k+1,s):
                    for j in range(k+1,s+1):
                        T[i][j]=self.exactdiv(self.add(self.mul(pivot,T[i][j]),self.mul(T[i][k],T[k][j])),prev)
                    T[i][k]=self.zero
                prev=pivot
            if singular or T[-1][s-1]==self.zero:continue
            Delta=T[-1][s-1];G=Delta;residual=self.strip(G)
            records=[{'omitted_row':omitted,'minor_degree':self.deg(Delta),'gcd_degree':self.deg(G),'residual_degree':self.deg(residual)}]
            if residual==self.one:return G,residual,records
            nums=[self.zero]*s
            for i in range(s-1,-1,-1):
                v=self.mul(Delta,T[i][s])
                for j in range(i+1,s):v=self.add(v,self.mul(T[i][j],nums[j]))
                nums[i]=self.exactdiv(v,T[i][i])
                G=self.gcd(G,nums[i]);residual=self.strip(G)
                records.append({'omitted_row':indices[i],'minor_degree':self.deg(nums[i]),'gcd_degree':self.deg(G),'residual_degree':self.deg(residual)})
                if residual==self.one:return G,residual,records
            assert len(records)==s+1
            return G,residual,records
        raise AssertionError('all maximal minors vanish identically')
    def strip(self,g):
        for f in [self.x,self.add(self.x,self.one)]:
            while g!=self.zero and self.divmod(g,f)[1]==self.zero:g=self.exactdiv(g,f)
        return g
    def coeffs(self,p):
        return [sum(((v>>j)&1)<<i for i,v in enumerate(p)) for j in range(self.deg(p)+1)]
    def test(self,abc,n,method="adjugate"):
        started=time.time();a,b,c=abc;d=(n-3)//2
        xp1=self.add(self.x,self.one);D=self.mul(self.x,xp1)
        xpow=[self.one];ypow=[self.one]
        for k in range(2*n):
            xpow.append(self.mul(xpow[-1],self.x));ypow.append(self.mul(ypow[-1],xp1))
        P={}
        for k in range(1,n):
            v=self.add(self.scale(self.mul(xpow[k-1],ypow[2*k]),b),self.scale(self.mul(xpow[2*k],ypow[k-1]),c))
            if k==1:v=self.add(v,self.scale(self.square(D),a))
            if k%2==0:v=self.add(v,self.square(P[k//2]))
            P[k]=v
        matrix=[[P[i-j] for j in range(d+1)] for i in range(d+1,n)]
        if method=="adjugate":
            G,residual,records=self.maximal_gcd(matrix)
        else:
            order=[0,d+1]+list(range(1,d+1));G=self.zero;records=[]
            for omitted in order:
                det=self.det([row for i,row in enumerate(matrix) if i!=omitted])
                G=self.gcd(G,det);residual=self.strip(G)
                records.append({'omitted_row':omitted,'minor_degree':self.deg(det),'gcd_degree':self.deg(G),'residual_degree':self.deg(residual)})
                if residual==self.one:break
        assert G!=self.zero
        if residual!=self.one:assert len(records)==d+2
        return {'n':n,'method':method,'theta_n_exists':residual!=self.one,'coordinate_polynomial_degree':self.deg(residual),'coordinate_polynomial_masks':[str(v) for v in residual],'coordinate_polynomial_coefficients':self.coeffs(residual),'minor_records':records,'all_minors_or_unit_gcd':True,'runtime_seconds':time.time()-started}


def moduli_rows(fields):
    rows=[]
    for abc in combinations_with_replacement(fields[2].f4[1:],3):
        rows.append({'splitting_type':'1+1+1','field_degree':2,'coefficients':list(abc)})
    for e,length in [(4,2),(6,3)]:
        A=fields[e];seen=set()
        for r in range(1,A.q):
            if r in A.f4 or r in seen:continue
            orbit=[];s=r
            for _ in range(length):orbit.append(s);s=A.fpow(s,4)
            assert s==r and len(set(orbit))==length
            seen.update(orbit)
            if length==2:
                for a in A.f4[1:]:rows.append({'splitting_type':'1+2','field_degree':e,'coefficients':[a]+orbit})
            else:rows.append({'splitting_type':'3','field_degree':e,'coefficients':orbit})
    for row in rows:
        A=fields[row['field_degree']];a,b,c=row['coefficients']
        s1=a^b^c;s2=A.mt[a][b]^A.mt[a][c]^A.mt[b][c];s3=A.mt[A.mt[a][b]][c]
        assert all(s in A.f4code for s in [s1,s2,s3])
        row['moduli_cubic_F4_coefficients']=[A.f4code[s3],A.f4code[s2],A.f4code[s1],1]
        row['moduli_key']=''.join(str(A.f4code[s]) for s in [s1,s2,s3])
    assert len(rows)==48 and len({r['moduli_key'] for r in rows})==48
    return sorted(rows,key=lambda r:r['moduli_key'])


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--orders',default='3,5,7,9,11,13,15')
    parser.add_argument('--only-unresolved',action='store_true')
    parser.add_argument('--all-orders',action='store_true')
    parser.add_argument('--method',choices=['adjugate','separate'],default='adjugate')
    parser.add_argument('--output',default=str(Path(__file__).with_suffix('.json')))
    args=parser.parse_args();orders=[int(x) for x in args.orders.split(',')]
    fields={e:Arithmetic(e,m) for e,m in [(2,7),(4,19),(6,67)]}
    rows=moduli_rows(fields);started=time.time();output=Path(args.output)
    old=json.loads(output.read_text()) if output.exists() else None
    if args.only_unresolved and old:
        previous={r['moduli_key']:r for r in old['curves']}
        for row in rows:
            if row['moduli_key'] in previous:row.update(previous[row['moduli_key']])
    out={'status':'EXPLORATORY exact geometric theta-n scan','field_presentations':{str(e):{'binary_modulus':A.mod,'F4_alpha':A.alpha,'field_inverse_checks':A.checks} for e,A in fields.items()},'moduli_count':48,'splitting_type_counts':{t:sum(r['splitting_type']==t for r in rows) for t in ['1+1+1','1+2','3']},'orders':orders,'curves':rows,'scope':'Complete geometric theta-n coordinate tests at the listed n; no universal boundedness conclusion. Positive A1 implications require the separately proved primitive-orbit criterion.'}
    for row in rows:
        row.setdefault('tests',[]);row.setdefault('successful_orders',[])
        if args.only_unresolved and row['successful_orders']:continue
        done={v['n'] for v in row['tests']}
        A=fields[row['field_degree']]
        for n in orders:
            if n in done:continue
            result=A.test(row['coefficients'],n,args.method);row['tests'].append(result)
            if result['theta_n_exists']:row['successful_orders'].append(n)
            print(json.dumps({'key':row['moduli_key'],'field':A.q,'abc':row['coefficients'],'n':n,'theta':result['theta_n_exists'],'degree':result['coordinate_polynomial_degree'],'seconds':round(result['runtime_seconds'],3)}),flush=True)
            output.write_text(json.dumps(out,indent=2)+'\n')
            if result['theta_n_exists'] and not args.all_orders:break
        output.write_text(json.dumps(out,indent=2)+'\n')
    out['remaining_moduli_keys']=[r['moduli_key'] for r in rows if not r['successful_orders']]
    out['runtime_seconds']=time.time()-started
    output.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':'COMPLETE','remaining':out['remaining_moduli_keys'],'runtime_seconds':out['runtime_seconds'],'positive_count':48-len(out['remaining_moduli_keys'])}),flush=True)
if __name__=='__main__':main()
