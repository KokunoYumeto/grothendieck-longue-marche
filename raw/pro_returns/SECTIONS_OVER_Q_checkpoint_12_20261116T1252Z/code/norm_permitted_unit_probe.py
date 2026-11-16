from sympy import primerange, nthroot_mod, factorint
for q in primerange(73, 2000000):
    if q%24!=1 or (q-1)%9==0:
        continue
    if pow(q-2,(q-1)//24,q)!=1:
        continue
    roots=sorted(map(int,nthroot_mod(3,3,q,all_roots=True)))
    if len(roots)!=3 or any(pow((1-z)%q,(q-1)//3,q)!=1 for z in roots):
        continue
    c=roots[0]
    while (c**3-3)%(q*q)==0:
        c+=q
    norm=c**3-3
    print('q=',q,'roots=',roots,'c=',c,'Norm(c-alpha)=',norm,'factorization=',factorint(norm))
    print('q mod72=',q%72,'B24 residue test=',pow(q-2,(q-1)//24,q))
    print('canonical beta cubic symbols=',[pow((1-z)%q,(q-1)//3,q) for z in roots])
    print('root-ratio cubic symbols=',[pow(z*pow(roots[0],-1,q)%q,(q-1)//3,q) for z in roots])
    print('common repaired beta unit cubic symbol=',pow(pow(norm//q,-1,q),(q-1)//3,q))
    break
else:
    raise RuntimeError('no prime found')
