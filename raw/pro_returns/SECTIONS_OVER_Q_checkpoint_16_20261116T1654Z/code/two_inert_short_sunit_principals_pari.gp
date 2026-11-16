\\ Candidate search only. Every returned element requires the independent
\\ S-support, divisor and saturation certificates before it is used.
default(parisizemax,1500000000);
default(parisize,256000000);
default(realprecision,150);setrand(3);
d=649;B=bnfinit(x^9-3*d^6,1);
S=concat(vector(4,j,idealprimedec(B,[2,3,11,59][j])));
print("BASE READY");
for(i=6,8,ideal_candidate=if(i==7,idealmul(B,S[5],S[7]),S[i]); R=bnfisprincipal(B,ideal_candidate,3); print("GENERATOR ",i," CLASS ",R[1]); print("POLYNOMIAL ",i," ",Vecrev(lift(nfbasistoalg(B,R[2])))));
quit;
