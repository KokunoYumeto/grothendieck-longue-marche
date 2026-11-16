\\ Exact compact representations of the already extracted candidates.
default(parisizemax, 1500000000);
default(parisize, 256000000);
default(realprecision,150);setrand(3);
d=649;B=bnfinit(x^9-3*d^6,1);
US=bnfunits(B)[1];
for(i=1,4,F=US[i];print("COMPACT UNIT ",i," ",matsize(F)[1]);for(j=1,matsize(F)[1],print("FACTOR ",i," ",j," ",F[j,2]," ",Vecrev(lift(nfbasistoalg(B,F[j,1]))))));
qs=[2,3,11,59];S=concat(vector(4,j,idealprimedec(B,qs[j])));VS=bnfunits(B,S)[1];
for(i=1,#S,F=VS[i];print("COMPACT SUNIT ",i," ",matsize(F)[1]);for(j=1,matsize(F)[1],print("SFACTOR ",i," ",j," ",F[j,2]," ",Vecrev(lift(nfbasistoalg(B,F[j,1]))))));
quit;
