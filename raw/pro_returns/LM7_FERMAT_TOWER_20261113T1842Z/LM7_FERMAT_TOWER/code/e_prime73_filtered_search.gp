default(parisize,256000000);
default(parisizemax,2000000000);
default(realprecision,100);
setrand(817332);
run()={
  my(dat=read("research_e81/code/e_prime73_relative_nf.bin"),R=dat[1],E=dat[2],I=dat[3]);
  my(fil=read("research_e81/code/e_prime73_genus_filter.bin"),allowed=fil[6],S=fil[7][5]);
  my(best=10^100,count=0);
  for(k=1,#allowed,
    my(v=allowed[k],J=I);
    for(i=1,6,J=idealmul(E,J,idealpow(E,S[i],v[i])));
    for(iter=1,4,
      my(weights=if(iter==1,vector(E.r1+E.r2),vector(E.r1+E.r2,j,random(36))),rr=idealred(E,[J,1],weights),nn=idealnorm(E,rr[1]),f=factor(nn));
      count++;
      if(nn<best,best=nn;print("REDUCED_NORM_IMPROVEMENT ",count," NORM ",nn," INPUT_S_EXPONENTS ",v));
      if(vecmax(concat([0],vector(matsize(f)[1],j,if(f[j,1]==3 || f[j,1]==17,0,1))))==0,
        my(g=if(type(rr[2])=="t_MAT",nffactorback(E,rr[2]),rr[2]),ex=vector(6,i,idealval(E,rr[1],S[i]))~,JJ=matid(54));
        for(i=1,6,JJ=idealmul(E,JJ,idealpow(E,S[i],ex[i])));
        if(JJ!=rr[1] || idealmul(E,rr[1],g)!=J,error("exact reduced identity"));
        my(finalex=ex-v,II=idealhnf(E,g));
        for(i=1,6,II=idealmul(E,II,idealpow(E,S[i],finalex[i])));
        if(II!=I,error("actual S-principalization identity"));
        print("S_PRINCIPAL_WITNESS ",lift(nfbasistoalg(E,g)));
        print("S_PRINCIPAL_IDENTITY I=(g)*S^e EXPONENTS ",finalex);
        writebin("research_e81/code/e_prime73_sprincipal_witness.bin",[R,E,I,S,g,finalex]);
        print("DONE: exact positive S-principalization certificate.");return(1)
      );
    );
    print("FILTERED_PROGRESS ",k," OF ",#allowed," REDUCTIONS ",count," BEST ",best);
  );
  print("NO_POSITIVE_WITNESS_AFTER ",count," REDUCTIONS; no S-nonprincipality inference.");
  print("DONE: all27 necessary correction cosets tested by bounded reduction.");
};
run();
quit;
