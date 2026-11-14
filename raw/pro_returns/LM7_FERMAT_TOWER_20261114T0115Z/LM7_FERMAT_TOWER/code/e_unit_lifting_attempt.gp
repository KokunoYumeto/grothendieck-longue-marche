\\ Exact ordinary-unit symbol lower bound from principal S-divisors in B2.
default(parisize,256000000);
default(parisizemax,2000000000);
default(realprecision,100);
run()={
  my(dat=read("research_norm_index/code/cyclotomic_base1_bnf.bin"),B=dat[1],F=B.nf,xi=dat[2],beta=dat[3]*xi,pi=beta+1);
  my(ps=concat(idealprimedec(F,3),idealprimedec(F,17)),SU=bnfsunit(B,ps),units=concat(concat([xi],B.fu),SU[1]));
  my(V=matrix(6,#units,i,j,idealval(F,units[j],ps[i])),M=matrix(6,#units),loc=read("research_norm_index/code/cyclotomic_base1_local_norms.bin"));
  for(j=1,3,for(k=1,#units,
    my(v=V[j,k],u=nfeltdiv(F,units[k],pi^v));
    M[j,k]=lift(Mod(loc[2][j]~*ideallog(F,u,loc[1][j]),3));
  ));
  for(j=4,6,
    my(bid=idealstar(F,ps[j],2,3));
    for(k=1,#units,my(u=nfeltdiv(F,units[k],beta^V[j,k]));M[j,k]=ideallog(F,u,bid)[1]);
  );
  my(C=[2,2,2,2,0,1;1,1,1,2,2,2;0,0,0,2,2,2],K=matker(Mod(C*V,3)),Z=Mod(M,3)*K);
  if(Mod(C*V,3)*K!=matrix(3,matsize(K)[2]),error("principal divisor kernel"));
  print("BASE_SUNIT_VALUATIONS ",V);
  print("BASE_SUNIT_CHARACTERS ",M);
  print("UPPER_SCLASS_MATRIX ",C);
  print("UPPER_PRINCIPAL_KERNEL ",lift(K));
  print("LIFTED_ORDINARY_CHARACTERS ",lift(Z));
  print("LIFTED_ORDINARY_SYMBOL_RANK ",matrank(Z));
  print("BASE_ORDINARY_SYMBOL_RANK ",matrank(Mod(M[,1..9],3)));
  print("DONE: exact unit-lifting symbol calculation; no assertion beyond the displayed rank.");
};
run();
quit;
