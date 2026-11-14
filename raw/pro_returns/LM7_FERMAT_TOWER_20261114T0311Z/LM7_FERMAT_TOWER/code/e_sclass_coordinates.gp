default(parisize,256000000);
default(parisizemax,2000000000);
default(realprecision,100);
run()={
  my(dat=read("research_norm_index/code/cyclotomic_base1_bnf.bin"),B=dat[1],F=B.nf,xi=dat[2],beta=dat[3]*xi,pi=beta+1);
  my(ps=concat(idealprimedec(F,3),idealprimedec(F,17)),SU=bnfsunit(B,ps),units=concat(concat([xi],B.fu),SU[1]),V=matrix(6,6,i,j,idealval(F,SU[1][j],ps[i])));
  my(allrecords=List());
  for(nn=1,2,
    my(n=3^nn,loc=if(nn==1,read("research_norm_index/code/cyclotomic_base1_local_norms.bin"),read("research_norm_index/code/cyclotomic_base1_ninth_norms.bin")),M=matrix(6,#units));
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
    my(U=vecextract(M,"..","1..9"),C=vecextract(M,"..","10..15"),H=mathnf(concat(n*matid(6),U)),S=matsnf(H,1),W=S[1]*C,ds=vector(6,i,S[3][i,i])~);
    my(sol=matsolvemod(W,ds,0,1),K=mathnf(sol[2]),KS=matsnf(K,1),VK=V*K,VKS=matsnf(VK,1),correct=matrix(9,6));
    if(denominator(H^-1*C*K)!=1 || abs(matdet(K))!=matdet(H)/matdet(mathnf(concat(H,C))),error("full valuation-kernel index"));
    for(j=1,6,correct[,j]=matsolvemod(U,n,-C*K[,j]));
    if(lift(Mod(U*correct+C*K,n))!=matrix(6,6),error("literal unit corrections"));
    if(KS[1]*K*KS[2]!=KS[3] || VKS[1]*VK*VKS[2]!=VKS[3],error("Smith coordinates"));
    print("S_DIVISOR_NORM_LATTICE ",n," UNIT_MATRIX ",U," S_MATRIX ",C," UNIT_HNF ",H," K ",K," K_INVERSE ",K^-1," K_SMITH ",KS," VALUATION_LATTICE ",VK," VALUATION_SMITH ",VKS," CORRECTION ",correct);
    listput(allrecords,[n,U,C,H,K,KS,VK,VKS,correct]);
  );
  my(found=vector(2,i,0),prime_records=List());
  forprime(p=2,1000,
    if(p==3 || p==17,next);
    my(prs=idealprimedec(F,p));
    for(j=1,#prs,
      my(pr=prs[j],cl=bnfisprincipal(B,pr,0));
      if(cl[2]%3!=1,next);
      my(mp=nfmodprinit(F,pr),card=p^pr.f,b=nfmodpr(F,beta,mp));
      for(nn=1,2,
        my(n=3^nn);
        if(found[nn] || b^((card-1)/n)!=1,next);
        my(zz,rt=sqrtn(b,n,&zz));
        if(!zz || rt^n!=b,error("actual split-prime root"));
        print("S_CLASS_SPLIT_GENERATOR ",n," RATIONAL_PRIME ",p," DEGREE ",pr.f," PRIME ",pr," HNF ",idealhnf(F,pr)," CLASS ",cl," BETA_RESIDUE ",b," ROOT ",rt," ROOT_UNITY ",zz," MODPR ",mp);
        listput(prime_records,[n,p,pr.f,pr,idealhnf(F,pr),cl,b,rt,zz]);
        found[nn]=1;
      );
      if(vecmin(found),break);
    );
    if(vecmin(found),break);
  );
  if(!vecmin(found),error("no split cyclic S-class module generator in search range"));
  writebin("research_norm_index/code/cyclotomic_sclass_coordinates.bin",[Vec(allrecords),Vec(prime_records),V,SU]);
  print("DONE: complete principal-S-divisor norm lattices and actual split-prime module generators.");
};
run();
quit;
