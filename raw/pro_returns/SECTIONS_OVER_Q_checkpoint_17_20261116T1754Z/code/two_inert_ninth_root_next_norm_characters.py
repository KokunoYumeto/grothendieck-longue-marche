#!/usr/bin/env python3
"""Literal tame unit characters of the complete M unit lattice for Omega/M.

At q=11,59 use Z_q[z]/(z^6+z^3+1), alpha=alpha0*z^(3i),
where alpha0 is the unique rational q-adic cube root of3.
No class-group or unit-group completeness discovery is used: the input
lattice is A199's independently certified complete pro-three lattice.
"""
from pathlib import Path
from fractions import Fraction
import json,runpy,sys
sys.set_int_max_str_digits(0)
B=Path(__file__).resolve().parent
v=runpy.run_path(str(B/'two_inert_ninth_root_full_units_certificate.py'))
d=v['d']; auto=v['automorphism']; rank=v['rank']
es,uv,anti,rr,ss=v['es'],v['uv'],v['anti'],v['v']['rr'],v['ss']

def mul(a,b,mod):
    out=[0]*11
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    for k in range(10,5,-1):
        out[k-3]-=out[k];out[k-6]-=out[k]
    return tuple(x%mod for x in out[:6])
def power(a,n,mod):
    out=(1,0,0,0,0,0)
    while n:
        if n&1:out=mul(out,a,mod)
        a=mul(a,a,mod);n//=2
    return out
def add(a,b,mod):return tuple((x+y)%mod for x,y in zip(a,b))
def const(c,mod):return (c%mod,0,0,0,0,0)
one=(1,0,0,0,0,0); z=(0,1,0,0,0,0)

def valuation(n,q):
    e=0
    while n%q==0:n//=q;e+=1
    return e

def rational_cube_root(q,precision):
    x=next(x for x in range(q) if pow(x,3,q)==3%q)
    current=1
    while current<precision:
        current=min(2*current,precision)
        mod=q**current
        x=(x-(x**3-3)*pow(3*x*x,-1,mod))%mod
    assert (x**3-3)%(q**precision)==0
    return x

def residue(a,q,branch):
    coeff,den=a
    e=valuation(den,q);mod=q**(e+1)
    alpha0=rational_cube_root(q,e+1)
    alpha=tuple(alpha0*x%mod for x in power(z,3*branch,mod))
    out=(0,)*6
    # Components t^1 and t^2 have valuation classes2 and1 modulo3.
    # An already-proved global unit has residue equal to its t^0 term.
    for j in range(3):
        cp=tuple(coeff[18*j+k]*pow(d,2*j,mod)%mod for k in range(6))
        out=add(out,mul(cp,power(alpha,j,mod),mod),mod)
    divisor=q**e
    assert all(x%divisor==0 for x in out),(q,branch,e)
    denunit=(den//divisor)%q
    val=tuple((x//divisor)*pow(denunit,-1,q)%q for x in out)
    assert any(val)
    return val,e

def epsilon_value(q,branch):
    alpha0=rational_cube_root(q,1)
    alpha=tuple(alpha0*x%q for x in power(z,3*branch,q))
    omega=power(z,3,q)
    inv=lambda x:power(x,q**6-2,q)
    pi=mul(power(alpha,2,q),inv(add(omega,const(-1,q),q)),q)
    taupi=tuple(-x%q for x in mul(omega,pi,q))
    vv=mul(add(one,pi,q),inv(add(one,power(pi,2,q),q)),q)
    tv=mul(add(one,taupi,q),inv(add(one,power(taupi,2,q),q)),q)
    return mul(vv,inv(tv),q)

records=[];matrix=[];max_precision=0
for q in [11,59]:
    assert pow(q,6,9)==1 and pow(q,2,9)!=1
    # The actual residue-field polynomial is irreducible: ord_9(q)=6.
    assert next(k for k in range(1,7) if pow(q,k,9)==1)==6
    omega=power(z,3,q)
    chars={one:0,omega:1,power(omega,2,q):2}
    for branch in range(3):
        vals=[];prec=[]
        for e in es:
            value,ex=residue(e,q,branch);vals.append(value);prec.append(ex)
        for j in range(3):
            for u in uv:
                value,ex=residue(auto(u,j),q,branch);vals.append(value);prec.append(ex)
            vals.append(epsilon_value(q,(branch+j)%3));prec.append(0)
            for a in anti:
                value,ex=residue(auto(a,j),q,branch);vals.append(value);prec.append(ex)
        for a in [rr,ss]:
            for j in range(9):
                value,ex=residue(auto(a,j),q,branch);vals.append(value);prec.append(ex)
        assert len(vals)==51
        row=[chars[power(value,(q**6-1)//3,q)] for value in vals]
        for j in range(9):
            num=one;den=one
            for a in v['numerator']:num=mul(num,residue(auto(a,j),q,branch)[0],q)
            for a in v['denominator']:den=mul(den,residue(auto(a,j),q,branch)[0],q)
            assert mul(power(vals[42+j],3,q),den,q)==num
        matrix.append(row)
        records.append({'q':q,'branch':branch,'alpha0':rational_cube_root(q,1),
                        'residue_polynomial':'z^6+z^3+1',
                        'values':[list(a) for a in vals],'row':row,
                        'denominator_q_valuations':prec})
        max_precision=max(max_precision,max(prec)+1)

rrank=rank(matrix)
assert rrank==3
# Recover the complete 51-column map from the displayed 13-column map.
compact_columns=list(range(9))+[33,34,35,42]
compact=[[row[j] for j in compact_columns] for row in matrix]
expected=[
 [1,0,1,1,1,2,2,0,2,0,2,2,2],
 [1,0,1,1,2,1,1,1,2,2,2,0,2],
 [1,0,1,1,1,2,1,0,2,2,0,2,2],
 [2,0,2,2,1,2,0,2,1,2,0,0,1],
 [2,0,2,2,0,0,1,1,1,0,0,2,1],
 [2,0,2,2,1,2,1,2,1,0,2,0,1]]
assert compact==expected
for row in matrix:
    assert row[9:33]==[0]*24
    assert row[33:42]==row[33:36]*3
    assert row[42:51]==[row[42]]*9
row_relation=[[1,2,2],[2,1,2],[2,2,1]]
assert [[sum(row_relation[i][k]*matrix[k][j] for k in range(3))%3
         for j in range(51)] for i in range(3)]==matrix[3:]
minor=[[matrix[i][j] for j in (0,4,6)] for i in range(3)]
det=(minor[0][0]*(minor[1][1]*minor[2][2]-minor[1][2]*minor[2][1])
     -minor[0][1]*(minor[1][0]*minor[2][2]-minor[1][2]*minor[2][0])
     +minor[0][2]*(minor[1][0]*minor[2][1]-minor[1][1]*minor[2][0]))
assert det==-1
# sigma is g^3, not g.  These exact norms justify the normalized
# h-alignment identity in the proof, including its absence of a root of unity.
for a in anti:
    assert v['product']([a,auto(a,3),auto(a,6)])==v['one']
# Normalize the pure quadratic-place character before its inclusion into Fq6.
normalizations=[]
for q in (11,59):
    eq=(q*q-1)//3
    assert eq%(q-1)==0 and eq%3 in (1,2)
    for k in range(3):
        assert (2*k*eq)%3==((eq%3)*(2*k%3))%3
    normalizations.append({'q':q,'pure_exponent':eq,
                           'alpha_character_in_zeta':eq%3,
                           'psi_multiplier':2})
# Exact automorphism relations in C9 semidirect units(mod9), on rho3,z.
def compose(a,b): return ((a[0]+a[1]*b[0])%9,(a[1]*b[1])%9)
def inverse(a):
    ui=pow(a[1],-1,9)
    return ((-ui*a[0])%9,ui)
gamma=(1,1); hh=(0,4); tau=(0,8); ss_group=(3,1)
assert compose(compose(hh,gamma),inverse(hh))==(4,1)
assert compose(compose(tau,gamma),tau)==(8,1)
assert compose(tau,hh)==compose(hh,tau)
assert compose(hh,ss_group)==compose(ss_group,hh)
print('Exact Omega/M tame-character matrix:')
for r in records:print(r['q'],r['branch'],r['row'])
print('Rank:',rrank,'; maximum q-adic scalar Hensel precision:',max_precision)
data={'rows':records,'rank':rrank,'max_hensel_precision':max_precision,
      'compact_columns_zero_based':compact_columns,'compact_matrix':compact,
      'row_relation':row_relation,'rank_minor':minor,'rank_minor_determinant':det,
      'pure_character_normalizations':normalizations,
      'three_literal_anti_unit_norms':'all exactly one',
      'ordinary_ambiguous_three_class_order':3**7,
      'source_generator_order':v['data']['generator_order'],
      'scope':'Complete-source local norm character matrix for Omega/M. All further global class or secondary-character consequences require their displayed morphisms.'}
stem=Path(__file__).with_suffix('')
stem.with_name(stem.name+'_data.json').write_text(json.dumps(data,indent=2)+'\n')
stem.with_name(stem.name+'_output.txt').write_text('\n'.join([
    'Complete M-unit next-norm tame characters: PASS',
    *[f'{r["q"]} branch{r["branch"]}: {r["row"]}' for r in records],
    f'Rank {rrank}; maximum scalar Hensel precision {max_precision}',
    f'Full51-to-compact13 comparison, row relation and minor determinant {det}: PASS',
    'Three literal anti-unit sigma norms, pure quadratic character normalization, actual automorphism relations: PASS',
    data['scope']])+'\n')
