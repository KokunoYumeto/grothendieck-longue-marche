default(parisize,256000000);
default(parisizemax,2000000000);
default(realprecision,100);
setrand(170372);
tryprincipal(F,I,label,count)={
  my(best=10^100);
  for(k=1,count,
    my(v=vector(F.r2,j,random(20)),R=idealred(F,[I,1],v),nn=idealnorm(F,R[1]));
    if(nn<best,best=nn);
    if(nn==1,
      my(g=if(type(R[2])=="t_MAT",nffactorback(F,R[2]),R[2]));
      if(idealhnf(F,g)!=idealhnf(F,I),error("principal identity"));
      print("PRINCIPAL ",label," AT ",k," GEN ",lift(nfbasistoalg(F,g)));
      return(1)
    )
  );
  print("NO_POSITIVE_WITNESS ",label," MINIMUM_NORM ",best);
  return(0)
};
run()={
  my(dat=read("research_norm_index/code/prime3_field2.bin"),F=dat[1],p3=dat[2]);
  my(P1=idealhnf(F,7,x^3-3),P2=idealhnf(F,7,x^3+1),P3=idealhnf(F,7,x^3+2));
  if(idealnorm(F,P1)!=343 || idealnorm(F,P2)!=343 || idealnorm(F,P3)!=343,error("extension norms"));
  tryprincipal(F,P1,"transfer10",200);
  tryprincipal(F,P2,"transfer01",200);
  tryprincipal(F,P3,"transfer22",200);
  tryprincipal(F,idealdiv(F,P1,P2),"transfer12",200);
  for(a=0,2,for(b=0,2,
    my(I=idealdiv(F,p3,idealmul(F,idealpow(F,P1,a),idealpow(F,P2,b))));
    tryprincipal(F,I,Str("prime3_minus_",a,b),120)
  ));
};
run();
quit;
