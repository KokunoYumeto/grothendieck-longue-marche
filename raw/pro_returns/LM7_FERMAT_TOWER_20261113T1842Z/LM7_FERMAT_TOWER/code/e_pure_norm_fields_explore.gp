default(parisize,256000000);
for(d=1,2,C=polcompositum(x^(3^d)-17,x^2+x+1,3);F=nfinit(C[1]);print("FIELD ",d," ",C[1]);print("ALPHA ",C[2]," ZETA ",C[3]);D=idealprimedec(F,3);print("PRIMES3 ",vector(#D,i,[D[i][3],D[i][4]])));
quit;
