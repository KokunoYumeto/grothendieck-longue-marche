default(parisize,256000000);
default(parisizemax,2000000000);
default(realprecision,100);
run()={
  my(dat=read("research_norm_index/code/cyclotomic_base1_bnf.bin"),B=dat[1],F=B.nf,z9=dat[2],a=dat[3],beta=a*z9);
  my(Y=varhigher("Y",x),ps=idealprimedec(F,3),bids=vector(3,j,idealstar(F,idealpow(F,ps[j],16),2,9)));
  for(j=1,3,print("LOCAL_NINTH_UNIT_GROUP ",j," ",bids[j].cyc," GENERATORS ",bids[j].gen));
  my(v=vector(9,j,Mod(if(j==1,1,0),F.pol)),norms=List(),matrices,sm,done=0);
  for(k=1,60,
    my(w=vector(9,j,if(j==1,v[1]+beta*v[9],v[j]+v[j-1])));v=w;
    my(u=1+sum(j=1,9,v[j]*Y^(j-1)),N=norm(Mod(u,Y^9-beta)));
    if(k==1 && N!=512+beta,error("first ninth norm"));
    for(j=1,3,if(idealval(F,N,ps[j])!=0,error("nonunit ninth norm")));
    listput(norms,nfalgtobasis(F,N));
    matrices=vector(3,j,Mat(vector(#norms,k,ideallog(F,norms[k],bids[j]))));
    sm=vector(3,j,matsnf(mathnf(concat(matdiagonal(bids[j].cyc),matrices[j]))));
    print("NINTH_NORM_STEP ",k," QUOTIENT_SMITH ",sm);
    done=1;
    for(j=1,3,if(prod(i=1,#sm[j],sm[j][i])!=9,done=0));
    if(done,break);
  );
  if(!done,error("ninth local norm kernel not spanned"));
  my(transforms=vector(3,j,matsnf(mathnf(concat(matdiagonal(bids[j].cyc),matrices[j])),1)));
  for(j=1,3,
    my(H=mathnf(concat(matdiagonal(bids[j].cyc),matrices[j])),S=transforms[j]);
    if(S[1]*H*S[2]!=S[3] || abs(matdet(S[1]))!=1 || abs(matdet(S[2]))!=1,error("ninth Smith identity"));
    print("NINTH_LOCAL_KERNEL ",j," MATRIX ",matrices[j]," HNF ",H," LEFT ",S[1]," RIGHT ",S[2]," SMITH ",S[3]);
  );
  writebin("research_norm_index/code/cyclotomic_base1_ninth_norms.bin",[bids,matrices,transforms,Vec(norms)]);
  print("DONE: exact ninth local norm kernels at all three wild primes.");
};
run();
quit;
