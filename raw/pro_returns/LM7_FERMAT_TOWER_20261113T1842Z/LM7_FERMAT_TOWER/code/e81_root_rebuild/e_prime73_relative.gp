default(parisize,256000000);
default(parisizemax,2000000000);
default(realprecision,100);
setrand(8173);

run()={
  my(dat=read("research_norm_index/code/cyclotomic_base1_bnf.bin"),B=dat[1],F=B.nf,xi=dat[2],beta=dat[3]*xi);
  my(coord=read("research_norm_index/code/cyclotomic_sclass_coordinates.bin"),P=coord[2][1][4],P3=idealpow(F,P,3),ans=bnfisprincipal(B,P3,1));
  if(ans[1]!=[0,0]~,error("base prime cube class"));
  my(gen=ans[2]);
  if(idealhnf(F,gen)!=P3 || nfeltnorm(F,gen)!=73^3,error("literal base cube generator"));
  print("BASE_PRIME_CLASS ",bnfisprincipal(B,P,0));
  print("BASE_PRIME_CUBE_GENERATOR ",lift(nfbasistoalg(F,gen)));
  print("BASE_PRIME_CUBE_NORM ",nfeltnorm(F,gen));
  my(w=varhigher("w",x));
  print("START_RELATIVE_NF: cubic beta2^3=beta1; no BNF computation.");
  my(R=rnfinit(F,w^3-beta));
  print("RELATIVE_ORDER_READY DISC ",R.disc," INDEX ",R.index);
  writebin("research_e81/code/e_prime73_relative_order.bin",[R,xi,beta,P,gen]);
  print("START_ABSOLUTE_NF: degree54 maximal order only.");
  my(E=nfinit(R),I=rnfidealup(R,P,1),g=rnfeltup(R,nfbasistoalg(F,gen)));
  if(idealnorm(E,I)!=73^3 || idealpow(E,I,3)!=idealhnf(E,g),error("absolute extension identity"));
  print("ABSOLUTE_NF_READY DEGREE ",poldegree(E.pol)," DISC_FACTORS ",factor(abs(E.disc)));
  print("ABSOLUTE_POLYNOMIAL ",E.pol);
  print("EXTENDED_PRIME_NORM ",idealnorm(E,I)," CUBE_PRINCIPAL_VERIFIED 1");
  my(S=concat(idealprimedec(E,3),idealprimedec(E,17)));
  if(#S!=6,error("six actual upper S primes"));
  print("UPPER_S_PRIMES ",apply(p->[p.p,p.e,p.f],S));
  writebin("research_e81/code/e_prime73_relative_nf.bin",[R,E,I,S,g]);
  my(best=10^100);
  for(k=1,48,
    my(v=if(k==1,0,vector(E.r2,j,random(16))),rr=idealred(E,[I,1],v),nn=idealnorm(E,rr[1]));
    if(nn<best,best=nn;print("REDUCTION_IMPROVEMENT ",k," NORM ",nn));
    if(nn==1,
      my(z=if(type(rr[2])=="t_MAT",nffactorback(E,rr[2]),rr[2]));
      if(idealhnf(E,z)!=I,error("actual principal witness"));
      print("PRINCIPAL_WITNESS ",lift(nfbasistoalg(E,z)));
      print("RELATIVE_WITNESS ",rnfeltabstorel(R,nfbasistoalg(E,z)));
      writebin("research_e81/code/e_prime73_principal_witness.bin",[R,E,I,z]);
      print("DONE: positive principalization witnessed exactly.");return(1)
    );
    if(k%12==0,print("REDUCTION_PROGRESS ",k," BEST ",best));
  );
  print("NO_POSITIVE_WITNESS_IN_48_DIRECTIONS BEST_NORM ",best);
  print("No nonprincipality or S-capitulation conclusion is inferred from this bounded search.");
  print("DONE: exact field and extended-ideal data retained.");
};
run();
quit;
