default(parisize,256000000);
default(parisizemax,2000000000);
default(realprecision,100);
setrand(8173);

run()={
  my(dat=read("research_e81/code/e_prime73_relative_nf.bin"),R=dat[1],E=dat[2],I=dat[3],S=dat[4]);
  if(idealnorm(E,I)!=73^3,error("cached actual extension ideal"));
  my(best=10^100);
  for(k=1,96,
    my(v=if(k==1,vector(E.r1+E.r2),vector(E.r1+E.r2,j,random(24))),rr=idealred(E,[I,1],v),nn=idealnorm(E,rr[1]));
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
  print("NO_POSITIVE_WITNESS_IN_96_DIRECTIONS BEST_NORM ",best);
  print("No nonprincipality or S-capitulation conclusion is inferred from this bounded search.");
  print("DONE: exact field and extended-ideal data retained.");
};
run();
quit;
