\\ Exact residual division fields of y^2=x^3+A*x at three.
default(parisizemax,2000000000);
for(j=1,2, A=if(j==1,1,4); P=x^8+216*A^3*x^4-3888*A^6; C=polcompositum(P,x^2+1,1); print("FIELD ",j," compositum degrees ",vector(#C,k,poldegree(C[k][1]))); Z=C[1]; Q=polredabs(Z[1]); print("POL ",Q); print("DISC ",nfdisc(Q)); B=bnfinit(Q,1); print("CLASS ",B.clgp); print("PRIMES2 ",vector(#idealprimedec(B,2),k,[idealprimedec(B,2)[k].e,idealprimedec(B,2)[k].f])); print("PRIMES3 ",vector(#idealprimedec(B,3),k,[idealprimedec(B,3)[k].e,idealprimedec(B,3)[k].f])); print("CERT ",bnfcertify(B)); writebin(Str("research_e117/code/three_division_",j,".bin"),[A,P,Z,Q,B]));
print("PASS");
