default(parisize,256000000);
default(parisizemax,2000000000);
default(realprecision,100);
run()={
  my(dat=read("research_norm_index/code/cyclotomic_base1_bnf.bin"),B=dat[1],F=B.nf,xi=dat[2],beta=dat[3]*xi,pi=beta+1,c1=beta+3*xi^3+1);
  my(ps=concat(idealprimedec(F,3),idealprimedec(F,17)),units=concat([xi],B.fu));
  my(generators=concat([c1],vector(3,j,nfbasistoalg(F,bnfisprincipal(B,idealpow(F,ps[j],3),1)[2]))));
  for(nn=1,2,
    my(n=if(nn==1,3,9),loc=if(nn==1,read("research_norm_index/code/cyclotomic_base1_local_norms.bin"),read("research_norm_index/code/cyclotomic_base1_ninth_norms.bin")),M=matrix(6,#units),T=vector(3,j,idealstar(F,ps[j+3],2,n)));
    my(all=concat(units,generators),C=matrix(6,#all));
    for(j=1,3,
      my(ch=if(nn==1,loc[2][j]~,loc[3][j][1][1,]));
      for(k=1,#all,
        my(v=idealval(F,all[k],ps[j]),u=nfeltdiv(F,all[k],pi^v));
        C[j,k]=lift(Mod(ch*ideallog(F,u,loc[1][j]),n));
      );
    );
    for(j=4,6,
      for(k=1,#all,
        my(v=idealval(F,all[k],ps[j]),u=nfeltdiv(F,all[k],beta^v));
        C[j,k]=ideallog(F,u,T[j-3])[1];
      );
    );
    M=vecextract(C,"..","1..9");
    my(H=mathnf(concat(n*matid(6),M)),Hi=H^-1);
    print("UNIT_IMAGE ",n," MATRIX ",M," HNF ",H);
    for(j=1,#generators,
      for(e=0,2,
        my(k=3^e,v=k*C[,9+j],ok=(denominator(Hi*v)==1));
        print("PRINCIPAL_NORM_TEST ",n," GENERATOR ",j," POWER ",k," CHARACTER ",lift(Mod(v,n))," IN_UNIT_IMAGE ",ok);
        if(ok,
          my(sol=matsolvemod(M,n,-v));
          if(lift(Mod(M*sol+v,n))!=vector(6,i,0)~,error("unit correction"));
          print("UNIT_CORRECTION_EXPONENTS ",sol);
        );
      );
    );
  );
  print("DONE: field-norm tests after exact unit corrections; no principal-ideal conclusion in upper fields.");
};
run();
quit;
