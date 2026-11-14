\\ Separate peer construction of all ten candidate principal divisors.
default(parisize,256000000);default(parisizemax,2000000000);
check(a,s)=if(!a,error(s));
{
 my(F=nfinit(x^18+53*x^9+2809),b=Mod(x,F.pol),C=read("../inputs/candidate_coefficients.txt"),rows=List());
 check(poldegree(F.pol)==18 && polisirreducible(F.pol),"actual candidate field");
 for(i=1,#C,
  my(u=sum(j=1,#C[i],C[i][j]*b^(j-1)),P=idealfactor(F,u),I=matid(18),fac=List());
  for(j=1,matsize(P)[1],
   my(pr=P[j,1],e=P[j,2]);check(isprime(pr[1]) && (pr[1]==3 || pr[1]==53),"complete divisor support");
   I=idealmul(F,I,idealpow(F,pr,e));listput(fac,[pr[1],pr[3],pr[4],e]);
  );
  check(idealhnf(F,u)==I,"full literal principal ideal reconstruction");
  check(abs(nfeltnorm(F,u))==idealnorm(F,I),"literal absolute norm");
  listput(rows,[i,Str(nfeltnorm(F,u)),Vec(fac)]);
 );
 print("{\"status\":\"PASS\",\"candidate_count\":",#C,",\"literal_principal_divisors\":",Vec(rows),",\"scope\":\"Independent nfinit/prime-HNF reconstruction of all ten literal candidate ideals; no upper BNF or unit completeness assertion.\"}");
}
quit;
