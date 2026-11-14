default(parisize,256000000);
default(parisizemax,2000000000);
default(realprecision,100);
run()={
  my(dat=read("research_norm_index/code/cyclotomic_base1_bnf.bin"),B=dat[1],F=B.nf,xi=dat[2],zeta=xi^3,beta=dat[3]*xi,pi=beta+1);
  my(ps=concat(idealprimedec(F,3),idealprimedec(F,17)),SU=bnfsunit(B,ps),units=concat(concat([xi],B.fu),SU[1]));
  print("S_CLASS_GROUP ",SU[5]," S_NONUNIT_GENERATORS ",SU[1]);
  print("S_VALUATION_LATTICE ",matrix(6,#SU[1],i,j,idealval(F,SU[1][j],ps[i])));
  my(c1=beta+3*zeta+1);
  for(j=4,6,
    my(mp=nfmodprinit(F,ps[j]),res=nfmodpr(F,c1,mp),z=nfmodpr(F,zeta,mp));
    if(res^96!=z || z==1,error("c1 local obstruction"));
    print("C1_NONCUBE_RESIDUE ",j," RESIDUE ",res," POWER96 ",res^96," ZETA ",z);
  );
  for(nn=1,2,
    my(n=if(nn==1,3,9),loc=if(nn==1,read("research_norm_index/code/cyclotomic_base1_local_norms.bin"),read("research_norm_index/code/cyclotomic_base1_ninth_norms.bin")),M=matrix(6,#units));
    for(j=1,3,
      my(ch=if(nn==1,loc[2][j]~,loc[3][j][1][1,]));
      for(k=1,#units,
        my(v=idealval(F,units[k],ps[j]),u=nfeltdiv(F,units[k],pi^v));
        M[j,k]=lift(Mod(ch*ideallog(F,u,loc[1][j]),n));
      );
    );
    for(j=4,6,
      my(bid=idealstar(F,ps[j],2,n));
      for(k=1,#units,
        my(v=idealval(F,units[k],ps[j]),u=nfeltdiv(F,units[k],beta^v));
        M[j,k]=ideallog(F,u,bid)[1];
      );
    );
    my(H=mathnf(concat(n*matid(6),M)),S=matsnf(H,1),ds=vector(6,i,S[3][i,i]),idx=n^6/prod(i=1,6,ds[i]));
    if(S[1]*H*S[2]!=S[3],error("S character Smith"));
    print("S_NORM_CHARACTERS ",n," MATRIX ",M," COKERNEL ",ds," INDEX ",idx," S_CLASS_AMBIGUOUS_ORDER ",3*n^5/idx," HNF ",H," LEFT ",S[1]," RIGHT ",S[2]);
  );
  print("DONE: exact S-unit norm characters; full upper S-class groups remain unevaluated.");
};
run();
quit;
