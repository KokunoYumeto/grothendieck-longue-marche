default(parisize,256000000);
default(parisizemax,2000000000);
default(realprecision,120);
setrand(177409);
run()={
  my(dat=read("research_norm_index/code/prime3_field2.bin"),F=dat[1],I=matid(18));
  my(z=Mod(x^9/17,F.pol),aut=nfalgtobasis(F,Mod(x,F.pol)*z),p17=idealprimedec(F,17)[1],modp=nfmodprinit(F,p17,'t));
  my(M=Map(),key,prev,collisions=0,found=0,distinct=Map(),witnesses=List());
  print("FIELD ",F.pol," DEGREE ",poldegree(F.pol)," DISCRIMINANT ",F.disc);
  for(k=1,1200,
    my(v=vector(F.r2,j,random(40)),R=idealred(F,[I,1],v));
    my(g=if(type(R[2])=="t_MAT",nffactorback(F,R[2]),R[2]),J=idealhnf(F,R[1]));
    if(idealmul(F,J,g)!=I,error("reduction orientation"));
    for(j=0,2,
      key=Str(J);
      if(mapisdefined(M,key,&prev),
        my(u=nfeltdiv(F,g,prev));
        if(idealhnf(F,u)!=I,error("collision is not unit"));
        collisions++;
        my(r=nfmodpr(F,u,modp),test=r^96,primary=r^64);
        if(!mapisdefined(distinct,Str(primary)),
          mapput(distinct,Str(primary),1);
          print("NEW_RESIDUE ",k," ",j," ",primary," CUBE_TEST ",test);
          print("UNIT ",lift(nfbasistoalg(F,u)));
          listput(witnesses,u);
        );
        if(test!=1,
          print("NONCUBE_UNIT ",k," ",j," ",lift(nfbasistoalg(F,u))," RESIDUE ",r," CUBE_TEST ",test);
          found=1;break;
        );
      ,
        mapput(M,key,g)
      );
      J=idealhnf(F,nfgaloisapply(F,aut,J));
      g=nfgaloisapply(F,aut,g);
    );
    if(found,break);
    if(k%100==0,print("PROGRESS ",k," IDEALS ",#M," COLLISIONS ",collisions," RESIDUES ",Vec(distinct)));
  );
  print("DONE IDEALS ",#M," COLLISIONS ",collisions," FOUND_NONCUBE ",found," RESIDUES ",Vec(distinct));
  writebin("research_norm_index/code/layer2_unit_collisions_witnesses.bin",Vec(witnesses));
};
run();
quit;
