#!/usr/bin/env python3
"""Finite certificates for the exact Heisenberg step in D.49."""
from pathlib import Path
import json


def mul(a,b,n):
    return ((a[0]+b[0])%n,(a[1]+b[1])%n,
            (a[2]+b[2]+a[0]*b[1])%n)


def power(a,m,n):
    z=(0,0,0)
    for _ in range(m):
        z=mul(z,a,n)
    return z


def reduce_word(word):
    stack=[]
    for v in word:
        if stack and stack[-1]==-v:
            stack.pop()
        else:
            stack.append(v)
    return stack


def main():
    rows=[]
    checks=0
    for n in (2,3,4,5,6,7,8,9,10,12,16,25,27,32,49,64):
        x,y=(1,0,0),(0,1,0)
        xy=mul(x,y,n)
        solutions=[]
        for m in range(2*n):
            left=power(xy,m,n)
            right=mul(power(y,m,n),power(x,m,n),n)
            assert left==(m%n,m%n,(m*(m+1)//2)%n)
            assert right==(m%n,m%n,0)
            assert (left==right)==(m*(m+1)//2%n==0)
            if left==right:
                assert ((2*m+1)**2-1)%(8*n)==0
                solutions.append(m)
            checks+=1
        rows.append({'modulus':n,'m_tested_modulo':2*n,
                     'solution_m_residues':solutions,
                     'all_solutions_satisfy_mu_squared_one_modulo':8*n})
    # a^{-1}(ab)^{-1}a = a^{-1}b^{-1}; gives u_- = a^{-1}u.
    assert reduce_word([-1,-2,-1,1])==[-1,-2]
    ans={'claim':'D.49','Heisenberg_coordinates_checked':checks,
         'moduli':rows,'opposite_multiplier_conjugator_word_check':True,
         'scope':'Finite certificates for the displayed identities; D.34 supplies the full global-sign conclusion.'}
    Path(__file__).with_name('standard_involution_centralizer_output.json').write_text(json.dumps(ans,indent=2)+'\n')
    print(json.dumps(ans,indent=2))


if __name__=='__main__':
    main()
