\\ Local candidate search only.  Every extracted unit identity is independently
\\ checked in rational arithmetic; no class-group completeness is used.
default(parisizemax, 1500000000);
default(parisize, 256000000);
default(realprecision, 150);
setrand(3);
d=649; P=x^9-3*d^6;
B=bnfinit(P,1);
print("PARI VERSION ",version());
print("SEARCH CLASS PRESENTATION ",B.cyc);
for(i=1,#B.fu,print("UNIT ",i," ",Vecrev(lift(B.fu[i]))));
quit;
