default(parisize,256000000);
default(parisizemax,2000000000);
default(realprecision,80);
setrand(170369);
run()={
  for(d=1,3,
    my(m=3^d,P=x^(2*m)+17*x^m+289);
    my(B=concat(vector(m,j,x^(j-1)),vector(m,j,x^(m+j-1)/17)));
    print("START ",d," DEGREE ",2*m);
    my(F=nfinit([P,B,[3,17]]));
    if(F.disc != -3^(m*(2*d+1))*17^(2*m-2),error("discriminant"));
    print("FIELD ",d," DISC ",F.disc," INDEX ",F.index);
    my(pp=idealprimedec(F,3));
    if(#pp!=1 || pp[1][3]!=2*m || pp[1][4]!=1,error("prime3"));
    my(p=pp[1], c=Mod(x^(3^(d-1))+3*x^m/17+1,P));
    if(idealhnf(F,c)!=idealhnf(F,idealpow(F,p,3^(d-1))),error("included generator"));
    print("INCLUDED_GENERATOR ",d," VALUATION ",3^(d-1)," NORM ",nfeltnorm(F,c));
    my(k=if(d==1,1,3),I=idealpow(F,p,k));
    my(red=idealred(F,[I,1]));
    print("REDUCTION ",d," POWER ",k," REDUCED_NORM ",idealnorm(F,red[1]));
    print("REDUCED_IDEAL ",d," ",red[1]);
    print("TRACKING ",d," ",red[2]);
    writebin(Str("research_norm_index/code/prime3_field",d,".bin"),[F,p,I,red]);
  );
};
run();
quit;
