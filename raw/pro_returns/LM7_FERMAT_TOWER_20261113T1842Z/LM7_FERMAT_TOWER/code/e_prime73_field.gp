default(parisize,256000000);
default(parisizemax,2000000000);
default(realprecision,100);
run()={
  my(dat=read("research_norm_index/code/cyclotomic_base1_bnf.bin"),B=dat[1],F=B.nf,xi=dat[2],beta=dat[3]*xi);
  my(P=idealhnf(F,73,x-33),P3=idealpow(F,P,3),ans=bnfisprincipal(B,P3,1));
  if(idealnorm(F,P)!=73 || bnfisprincipal(B,P,0)!=[2,1]~ || ans[1]!=[0,0]~,error("actual prime and class"));
  my(gen=ans[2]);
  if(idealhnf(F,gen)!=P3 || nfeltnorm(F,gen)!=73^3,error("literal base cube generator"));
  print("BASE_PRIME_CLASS ",bnfisprincipal(B,P,0));
  print("BASE_PRIME_CUBE_GENERATOR ",lift(nfbasistoalg(F,gen)));
  my(w=varhigher("w",x),R=rnfinit(F,w^3-beta),E=nfinit(R),I=rnfidealup(R,P,1),g=rnfeltup(R,nfbasistoalg(F,gen)));
  if(idealnorm(E,I)!=73^3 || idealpow(E,I,3)!=idealhnf(E,g),error("absolute extension identity"));
  my(PS=concat(idealprimedec(F,3),idealprimedec(F,17)),rawS=concat(idealprimedec(E,3),idealprimedec(E,17)),S=vector(6));
  if(#rawS!=6,error("six upper primes"));
  for(i=1,6,
    my(J=rnfidealup(R,PS[i],1),found=0);
    for(j=1,6,if(idealpow(E,rawS[j],3)==J,S[i]=rawS[j];found++));
    if(found!=1,error("actual prime extension"));
  );
  print("ABSOLUTE_DEGREE ",poldegree(E.pol)," DISCRIMINANT_FACTORS ",factor(abs(E.disc))," RELATIVE_ORDER_INDEX ",R.index);
  print("UPPER_PRIME_DATA ",apply(p->[p.p,p.e,p.f],S));
  writebin("research_e81/code/e_prime73_field.bin",[B,F,R,E,P,I,PS,S,gen,xi,beta]);
  print("DONE: certified base class and exact degree54 extension ideals; no upper BNF run.");
};
run();
quit;
