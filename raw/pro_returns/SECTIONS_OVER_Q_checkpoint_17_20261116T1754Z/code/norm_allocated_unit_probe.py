from sympy import primerange
for q in primerange(7, 200000):
    if q % 3 != 1 or (q-1) % 9 == 0:
        continue
    cubes={pow(z,3,q) for z in range(1,q)}
    roots=[z for z in range(1,q) if pow(z,3,q)==3]
    if len(roots)!=3 or any((1-z)%q not in cubes for z in roots):
        continue
    c=roots[0]
    while (c**3-3)%(q*q)==0:
        c+=q
    print('q=',q,'roots=',roots,'c=',c,'Norm(c-alpha)=',c**3-3)
    print('v3(q-1)=1; canonical beta unit cubic symbols=',[pow((1-z)%q,(q-1)//3,q) for z in roots])
    print('root-ratio cubic symbols=',[pow(z*pow(roots[0],-1,q)%q,(q-1)//3,q) for z in roots])
    print('b cubic symbol=',pow(q-2,(q-1)//3,q))
    break
else:
    raise RuntimeError('no prime found')
