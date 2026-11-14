default(parisize,256000000);
default(parisizemax,2000000000);
default(realprecision,100);
setrand(817331);

run()={
  my(dat=read("research_e81/code/e_prime73_relative_nf.bin"),R=dat[1],E=dat[2],I=dat[3],rawS=dat[4]);
  my(base=read("research_norm_index/code/cyclotomic_base1_bnf.bin"),B=base[1],F=B.nf);
  my(co=read("research_norm_index/code/cyclotomic_sclass_coordinates.bin"),V=co[3],SU=co[4],PS=concat(idealprimedec(F,3),idealprimedec(F,17)),S=vector(6));
  for(i=1,6,
    my(J=rnfidealup(R,PS[i],1),found=0);
    for(j=1,6,if(idealpow(E,rawS[j],3)==J,S[i]=rawS[j];found++));
    if(found!=1,error("unique totally ramified prime and actual order"));
  );
  my(M=concat(3*V,[0,0,0,1,1,1]~),gens=vector(7));
  for(i=1,6,gens[i]=rnfeltup(R,SU[1][i]));
  gens[7]=rnfeltreltoabs(R,Mod(variable(R.pol),R.pol));
  for(j=1,7,
    my(J=matid(54));
    for(i=1,6,J=idealmul(E,J,idealpow(E,S[i],M[i,j])));
    if(J!=idealhnf(E,gens[j]),error("literal S-principal relation"));
  );
  my(H=mathnf(M),SM=matsnf(H,1),U=SM[1],D=SM[3],Ui=U^-1,orders=vector(6,i,D[i,i]),total=prod(i=1,6,orders[i]));
  if(denominator(Ui)!=1 || U*H*SM[2]!=D,error("exact S-class quotient coordinates"));
  print("KNOWN_S_RELATIONS ",M," HNF ",H," SMITH ",SM," INVERSE_LEFT ",Ui," QUOTIENT_SIZE ",total);
  writebin("research_e81/code/e_prime73_srelation_lattice.bin",[M,H,SM,Ui,S,gens]);
  my(best=10^100,count=0);
  for(k=0,total-1,
    my(z=vector(6),rem=k);
    for(j=1,6,z[j]=rem%orders[j];rem=rem\orders[j];if(2*z[j]>orders[j],z[j]-=orders[j]));
    my(v=Ui*z~,J=I);
    for(i=1,6,J=idealmul(E,J,idealpow(E,S[i],v[i])));
    for(iter=1,2,
      my(weights=if(iter==1,vector(E.r1+E.r2),vector(E.r1+E.r2,j,random(32))),rr=idealred(E,[J,1],weights),nn=idealnorm(E,rr[1]),f=factor(nn));
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
        print("RELATIVE_WITNESS ",rnfeltabstorel(R,nfbasistoalg(E,g)));
        writebin("research_e81/code/e_prime73_sprincipal_witness.bin",[R,E,I,S,g,finalex]);
        print("DONE: exact positive S-principalization certificate.");return(1)
      );
    );
    if((k+1)%81==0,print("SEARCH_PROGRESS ",k+1," OF ",total," REDUCTIONS ",count," BEST ",best));
  );
  print("NO_POSITIVE_WITNESS_AFTER ",count," REDUCTIONS; no nonprincipality inference.");
  print("DONE: complete known S-relation quotient traversed with a bounded reduction search.");
};
run();
quit;
