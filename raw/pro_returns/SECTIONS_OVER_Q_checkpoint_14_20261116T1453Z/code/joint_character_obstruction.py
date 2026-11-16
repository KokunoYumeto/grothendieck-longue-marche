"""Exact finite certificate accompanying A.69.

The Q_2 fourth root exists by log/exp, proved in the text.  The root
below checks the chosen branch to finite precision.  No global point
or all-puncture completed class is inferred from these calculations.
"""
from fractions import Fraction as F
from pathlib import Path


def transform(t):
    return (4-15*F(t))/68


old=[F(4,15),F(-64,15),F(869,868)]
punctures=list(map(transform,old))
assert punctures==[F(0),F(1),F(-9563,59024)]
R=transform(0)
bad=transform(-4)
c=transform(1)
assert (R,bad,c)==(F(1,17),F(16,17),F(-11,68))
coeff=[R-d for d in punctures]
fibre=[(c-d)/a for d,a in zip(punctures,coeff)]
assert fibre==[F(-11,4),F(79,64),F(1,869)]
assert fibre[0]*fibre[1]*fibre[2]==F(-1,256)
assert 4**4*fibre[0]*fibre[1]*fibre[2]==-1
assert [(bad-d)/a for d,a in zip(punctures,coeff)]==[
    F(16),F(1,16),F(4341,869)]
assert all((R-d)/a==1 for d,a in zip(punctures,coeff))
assert (bad-c)/(R-c)==5
assert R-c==F(15,68)
assert len(set(punctures+[R,bad,c]))==6

u=F(4341,869)
assert u.numerator%16==u.denominator%16==5
precision=64
modulus=2**precision
target=u.numerator*pow(u.denominator,-1,modulus)%modulus
root=1
for k in range(4,precision):
    difference=(target-pow(root,4,2**(k+1)))%2**(k+1)
    assert difference%2**k==0
    if (difference//2**k)%2:
        root+=2**(k-2)
    assert pow(root,4,2**(k+1))==target%2**(k+1)
assert root%4==1
assert pow(root,4,modulus)==target
hilbert=(-1)**((5*5-1)//8)
assert hilbert==-1

out=(
    'A.69 exact rational identities: all passed.\n'
    f'Old punctures: {punctures}; base={R}; bad local point={bad}; new={c}.\n'
    f'Coefficients: {coeff}.\n'
    f'Joint fibre constants: {fibre}; product=-1/256.\n'
    'At the bad point the fourth powers are16,1/16,4341/869.\n'
    f'Chosen fourth root of4341/869 modulo2^{precision-2}: {root}.\n'
    f'Its fourth power agrees modulo2^{precision}; branch=1mod4.\n'
    'Normalized new coordinate is1 at the base and5 at the bad point.\n'
    'Exact dyadic Hilbert sign(5,2)=-1, invariant1/2.\n'
    'The infinite root and global nonextension follow from the proofs, not from finite testing.\n'
)
Path(__file__).with_name('joint_character_obstruction_output.txt').write_text(out)
print(out,end='')
