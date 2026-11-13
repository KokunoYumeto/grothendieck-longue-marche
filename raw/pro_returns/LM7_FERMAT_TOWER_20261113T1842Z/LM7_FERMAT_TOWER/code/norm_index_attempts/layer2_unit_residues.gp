default(parisize,256000000);
default(parisizemax,2000000000);
default(realprecision,100);
setrand(176903);
run()={
  my(dat=read("research_norm_index/code/prime3_field2.bin"),F=dat[1]);
  my(c=Mod(x^3+3*x^9/17+1,F.pol),I=idealhnf(F,c),p17=idealprimedec(F,17)[1],modp=nfmodprinit(F,p17,'t));
  my(found=0,units=0,residues=List());
  for(k=1,400,
    my(v=vector(F.r2,j,random(20)),R=idealred(F,[I,1],v));
    if(idealnorm(F,R[1])==1,
      my(g=if(type(R[2])=="t_MAT",nffactorback(F,R[2]),R[2]));
      if(idealhnf(F,g)!=I,error("principal identity"));
      g=nfeltdiv(F,g,c);
      if(idealhnf(F,g)!=matid(18),error("unit identity"));
      units++;
      my(r=nfmodpr(F,g,modp),test=r^96);
      listput(residues,r^64);
      if(test!=1,
        print("NONCUBE_UNIT_ITERATION ",k);
        print("UNIT ",lift(nfbasistoalg(F,g)));
        print("UNIT_NORM ",nfeltnorm(F,g)," RESIDUE ",r," CUBE_TEST ",test," ORDER9_PROJECTION ",r^64);
        found=1;break;
      );
    );
  );
  print("DONE UNITS ",units," FOUND_NONCUBE ",found," DISTINCT_3_RESIDUES ",Set(residues));
};
run();
quit;
