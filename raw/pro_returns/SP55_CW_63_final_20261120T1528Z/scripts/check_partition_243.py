"""Exact finite check of scan 43's stated counterexample, from scan 42's product."""
n=243
coeff=[0]*(n+1)
coeff[0]=1
for part in range(1,n+1):
    for degree in range(part,n+1):
        coeff[degree]+=coeff[degree-part]
p=coeff[n]
print({'n':n,'24n-1':24*n-1,'quotient_by_343':(24*n-1)//343,'p(n)':p,'p(n)_mod_343':p%343,'p(n)_mod_49':p%49})
