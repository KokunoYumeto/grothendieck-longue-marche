#!/usr/bin/env python3
"""Finite certificates used for the genus-four cyclotomic counterexample.

The no-point proof is a valuation proof valid for every cyclotomic field,
not an inference from a finite search.  This program checks the residue
classes of the three valuations and the branch divisor calculation.
"""
import sympy as sp

t,y=sp.symbols('t y')
f=t**6+4
assert sp.gcd(f,sp.diff(f,t))==1
print('Genus-four affine equation: t^6+2*y^3+4=0')
print('Map to diagonal cubic: (t,y) |-> (t^2:y:1)')
print('Pullback of X^3+2*Y^3+4*Z^3:',sp.expand((t*t)**3+2*y**3+4))
print('gcd(t^6+4,6*t^5)=',sp.gcd(f,sp.diff(f,t)))
print('Cyclic degree-three cover of P^1_t: six simple finite branch points')
print('Pole order at infinity: 6, hence three unramified points at infinity')
g=1+(-2*3+6*(3-1))//2
assert g==4
print('Riemann-Hurwitz genus:',g)

print('\nAt 2, cyclotomic ramification index e is a power of 2.')
for r in range(12):
    e=2**r
    residues=(0,e%3,(2*e)%3)
    assert len(set(residues))==3
    print('e=2^%d: valuations of X^3,2Y^3,4Z^3 modulo3 = %s'%(r,residues))
print('General residue certificate: 2^r mod3 is 1 for even r, 2 for odd r.')
print('Thus the three nonzero summands have distinct valuation residues;')
print('their minimum valuation occurs once and they cannot sum to zero.')
print('With a zero coordinate, the remaining two residues are still distinct.')
print('The homogeneous diagonal cubic has no point in any Q(mu_N).')
print('Its genus-four finite cover consequently has no Q(mu_infty)-point.')
print('Section existence is proved cohomologically in Statement D5;')
print('the program does not claim to compute an infinite Galois section.')
