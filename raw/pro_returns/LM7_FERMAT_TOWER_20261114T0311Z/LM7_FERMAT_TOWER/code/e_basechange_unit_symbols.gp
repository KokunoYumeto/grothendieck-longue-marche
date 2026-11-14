default(parisize,256000000);
default(parisizemax,2000000000);
default(realprecision,100);
run()={
  my(dat=read("research_norm_index/code/cyclotomic_base1_bnf.bin"),B=dat[1],F=B.nf,z9=dat[2],a=dat[3],beta=a*z9);
  my(local=read("research_norm_index/code/cyclotomic_base1_local_norms.bin"),bids=local[1],chars=local[2],units=concat([z9],B.fu),M=matrix(6,#units));
  for(j=1,3,for(k=1,#units,M[j,k]=lift(Mod(chars[j]~*ideallog(F,units[k],bids[j]),3))));
  my(ps=idealprimedec(F,17));
  for(j=1,3,
    my(bid=idealstar(F,ps[j],2,3));
    if(bid.cyc!=[3],error("tame quotient"));
    for(k=1,#units,M[j+3,k]=lift(Mod(ideallog(F,units[k],bid)[1],3)));
  );
  print("UNIT_SYMBOL_MATRIX ",M," RANK ",matrank(Mod(M,3)));
  print("ROW_RELATIONS ",lift(matker(Mod(M~,3))));
  print("CLASS_GENERATORS ",B.gen);
  forprime(p=2,50,
    if(p!=3 && p!=17,
      my(v=idealprimedec(F,p));
      for(j=1,#v,
        my(cl=bnfisprincipal(B,v[j],0));
        if(cl[2]!=0,
          my(modp=nfmodprinit(F,v[j],'t),res=nfmodpr(F,beta,modp));
          print("CLASS_PRIME ",p," ",j," E_F ",[v[j].e,v[j].f]," CLASS ",cl," KUMMER ",res^((p^v[j].f-1)/3));
        );
      );
    );
  );
  writebin("research_norm_index/code/cyclotomic_base1_unit_symbols.bin",[M,units]);
};
run();
quit;
