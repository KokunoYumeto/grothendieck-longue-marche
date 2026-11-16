\\ Local exact candidate generation only; no completeness assertion.
default(parisizemax, 1500000000);
default(parisize, 256000000);
default(realprecision, 150);
setrand(3);
d=649;P=x^9-3*d^6;B=bnfinit(P,1);
qs=[2,3,11,59];S=concat(vector(4,j,idealprimedec(B,qs[j])));
print("S COUNT ",#S);
for(i=1,#S,print("PRIME ",i," ",[S[i][1],S[i][3],S[i][4]]));
US=bnfunits(B,S)[1];
for(i=1,#S,g=nffactorback(B,US[i]);print("SUNIT ",i," ",Vecrev(lift(nfbasistoalg(B,g))));print("VALUATIONS ",i," ",vector(#S,j,idealval(B,g,S[j])));print("NORM ",i," ",nfeltnorm(B,g)));
quit;
