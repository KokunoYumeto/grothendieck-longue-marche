\\ Actual Artin characters of three integral ideals, factored in the certified nf.
default(parisize,64000000);
check(a,s)=if(!a,error(s));
{
 my(B=vector(18,i,if(i%2,x^((i-1)\2),x^(9+(i-2)\2)/53)),N=nfinit([x^18+53*x^9+2809,B,[3,53]],4));
 check(nfcertify(N)==[],"maximal order independently certified");
 my(Z=read("../inputs/e53_ordinary_frobenius_input.txt"),beta=Mod(x,N.pol),zeta=beta^9/53,F=vector(3));
 for(i=1,3,
  my(I=matrix(18,18,j,k,Z[i][j][k]),fa=idealfactor(N,I),cc=0);
  for(k=1,matsize(fa)[1],
   my(pr=fa[k,1],e=fa[k,2],q=pr[1]^pr[4],modpr=nfmodprinit(N,pr,'t),b=nfmodpr(N,beta,modpr),z=nfmodpr(N,zeta,modpr),c=-1);
   check(pr[1]!=3 && pr[1]!=53,"unramified class-generator ideal");
   for(j=0,2,if(b^((q-1)/3)==z^j,c=j));check(c>=0,"actual arithmetic Frobenius phase");cc+=e*c;
   print("{\"type\":\"prime_factor\",\"generator\":",i,",\"rational_prime\":",pr[1],",\"residue_degree\":",pr[4],",\"ideal_exponent\":",e,",\"beta_residue\":\"",b,"\",\"zeta_residue\":\"",z,"\",\"Frobenius\":",c,"}");
  );F[i]=lift(Mod(cc,3));
 );
 print("{\"status\":\"PASS\",\"actual_Frobenius_columns\":",F,"}");
}
quit;
