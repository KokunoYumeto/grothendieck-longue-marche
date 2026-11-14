default(parisize,256000000);
default(parisizemax,2000000000);
default(realprecision,100);
run()={
  my(V=polcompositum(polcyclo(9),x^3-17,1));
  if(#V!=1,error("unexpected compositum factors"));
  my(P=V[1][1],z9=V[1][2],a=V[1][3]);
  if(z9^6+z9^3+1!=0 || a^3!=17,error("compositum maps"));
  print("COMPOSITUM ",P);
  print("ZETA9 ",z9," CUBE17 ",a);
  my(F=nfinit(P),D=factor(abs(F.disc)));
  print("NF_DEGREE ",poldegree(P)," DISCRIMINANT ",F.disc," FACTORS ",D," INDEX ",F.index);
  print("PRIMES3 ",apply(p->[p.e,p.f,idealhnf(F,p)],idealprimedec(F,3)));
  print("PRIMES17 ",apply(p->[p.e,p.f,idealhnf(F,p)],idealprimedec(F,17)));
  writebin("research_norm_index/code/cyclotomic_base1_nf.bin",[F,z9,a]);
  print("START_BNF");
  my(B=bnfinit(F,1));
  print("BNF_CLASS ",B.cyc," CLASS_NUMBER ",B.no," REGULATOR ",B.reg);
  print("BNF_CERTIFY ",bnfcertify(B));
  print("ROOTS_UNITY ",B.tu," FUNDAMENTAL_UNITS ",B.fu);
  forprime(p=3,17,
    if(p==3 || p==17,
      my(v=idealprimedec(F,p));
      for(j=1,#v,print("PRIME_CLASS ",p," ",j," ",bnfisprincipal(B,v[j],0)));
    );
  );
  writebin("research_norm_index/code/cyclotomic_base1_bnf.bin",[B,z9,a]);
  print("DONE");
};
run();
quit;
