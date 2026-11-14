default(parisize,256000000);
default(parisizemax,2000000000);
default(realprecision,100);
run()={
  my(dat=read("research_norm_index/code/cyclotomic_base1_nf.bin"),F=dat[1],z9=dat[2],a=dat[3],beta=a*z9);
  my(ps=idealprimedec(F,3),bids=vector(3,j,idealstar(F,idealpow(F,ps[j],10),2,3)));
  for(j=1,3,print("LOCAL_CUBIC_UNIT_GROUP ",j," ",bids[j].cyc," GENERATORS ",bids[j].gen));
  my(v0=Mod(1,F.pol),v1=Mod(0,F.pol),v2=Mod(0,F.pol),norms=List(),powers=List());
  for(k=1,40,
    my(w0=v0+beta*v2,w1=v0+v1,w2=v1+v2);
    v0=w0;v1=w1;v2=w2;
    my(u0=v0+1,N=u0^3+beta*v1^3+beta^2*v2^3-3*beta*u0*v1*v2);
    for(j=1,3,if(idealval(F,N,ps[j])!=0,error("nonunit local norm")));
    listput(norms,nfalgtobasis(F,N));listput(powers,k);
  );
  my(chars=List(),matrices=List());
  for(j=1,3,
    my(M=Mat(vector(#norms,k,ideallog(F,norms[k],bids[j]))),rank=matrank(Mod(M,3)),H=matker(Mod(M~,3)));
    print("LOCAL_NORM_MATRIX ",j," ",lift(Mod(M,3))," RANK ",rank," CHARACTER ",lift(H));
    if(#bids[j].cyc!=7 || rank!=6 || matsize(H)!=[7,1],error("insufficient local norm span"));
    listput(chars,lift(H[,1]));listput(matrices,lift(Mod(M,3)));
  );
  writebin("research_norm_index/code/cyclotomic_base1_local_norms.bin",[bids,Vec(chars),Vec(matrices),Vec(norms)]);
  print("DONE: exact local norm characters at all three wild primes.");
};
run();
quit;
