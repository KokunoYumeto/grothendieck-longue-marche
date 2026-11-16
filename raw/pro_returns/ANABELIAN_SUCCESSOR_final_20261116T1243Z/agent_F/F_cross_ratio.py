from fractions import Fraction

def orbit(a):
    a=Fraction(a)
    return {a,1-a,1/a,1/(1-a),a/(a-1),(a-1)/a}

for a in [2,3]:
    print(a, sorted(str(x) for x in orbit(a)))
assert orbit(2).isdisjoint(orbit(3))
print('The two anharmonic cross-ratio orbits are disjoint.')
print('Therefore P1 minus {0,1,infinity,2} and P1 minus {0,1,infinity,3}')
print('are not isomorphic over any field of characteristic zero.')
