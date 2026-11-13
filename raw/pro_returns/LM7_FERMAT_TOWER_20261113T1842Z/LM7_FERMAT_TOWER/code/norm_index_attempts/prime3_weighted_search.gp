default(parisize,256000000);
default(parisizemax,2000000000);
default(realprecision,80);
setrand(17036902);
run()={
  for(d=1,3,
    my(dat=read(Str("research_norm_index/code/prime3_field",d,".bin")));
    my(F=dat[1],I=dat[3],n=F.r2,found=0,minnorm=idealnorm(F,I));
    print("START ",d," DEGREE ",poldegree(F.pol)," INITIAL_NORM ",minnorm);
    for(k=1,120,
      my(v=vector(n,j,random(20)),R=idealred(F,[I,1],v),z=idealnorm(F,R[1]));
      if(z<minnorm,minnorm=z;print("MINIMUM ",d," ",k," ",z));
      if(z==1,
        print("PRINCIPAL ",d," ITERATION ",k," DIRECTION ",v," FACTOR ",R[2]);
        my(g=if(type(R[2])=="t_MAT",nffactorback(F,R[2]),R[2]));
        if(idealhnf(F,g)!=idealhnf(F,I),error("principal identity"));
        print("GENERATOR ",d," ",lift(nfbasistoalg(F,g))," NORM ",nfeltnorm(F,g));
        found=1;break;
      );
    );
    print("DONE ",d," FOUND ",found," MINIMUM_NORM ",minnorm);
  );
};
run();
quit;
