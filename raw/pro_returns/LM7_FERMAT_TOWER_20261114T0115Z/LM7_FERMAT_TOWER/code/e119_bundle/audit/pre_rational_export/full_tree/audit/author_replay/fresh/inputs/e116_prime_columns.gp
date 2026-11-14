\\ Read only the saved certified degree-six BNF; no upper BNF.
default(parisize,128000000);
default(parisizemax,1000000000);
check(a,s)=if(!a,error(s));
{
 my(V=read("e_small_inert_units.bin"),D);
 for(i=1,#V[1],if(V[1][i][1]==53,D=V[1][i]));
 my(B=D[2],a=D[4],z=D[5],Q=D[11],F=B.nf,
    basis=[1,a,a^2,z,z*a,z*a^2],C=matrix(6,6,i,j,polcoef(lift(basis[j]),i-1)),U=vector(3));
 for(i=1,3,
  my(pr=bnfisprincipal(B,Q[i],1));check(#pr[1]==0,"certified principal three-prime");
  U[i]=nfbasistoalg(F,pr[2]);
  check(idealhnf(F,U[i])==idealhnf(F,Q[i]),"literal prime generator ideal");
  my(v=matsolve(C,Col(vector(6,j,polcoef(lift(U[i]),j-1)))));
  print("{\"type\":\"prime_generator\",\"index\":",i,",\"coordinates\":",vector(6,j,Str(v[j])),",\"absolute_norm\":",nfeltnorm(F,U[i]),",\"prime_valuations\":",vector(3,j,idealval(F,U[i],Q[j])),"}");
 );
 writebin("e53_prime_columns.bin",[D,U]);
 print("{\"type\":\"completion\",\"status\":\"PASS\"}");
}
quit;
