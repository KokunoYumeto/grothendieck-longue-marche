default(parisize,256000000);
default(parisizemax,2000000000);
default(realprecision,100);
run()={
  my(dat=read("research_e81/code/e_prime73_field.bin"),B=dat[1],F=dat[2],R=dat[3],E=dat[4],P=dat[5],I=dat[6],PS=dat[7],S=dat[8]);
  my(ar=read("research_e81/code/e_prime73_artin.bin"),ds=ar[5],C=ar[6],target=ar[7],H=read("research_e81/code/e_prime73_relations.bin")[4],records=List());
  for(a=-1,1,for(b=-1,1,for(c=-1,1,
    my(v=[3*a+2*b+2*c,b,c,-1,1,0]~,J=I,N=idealpow(F,P,3));
    for(i=1,6,J=idealmul(E,J,idealpow(E,S[i],v[i]));N=idealmul(F,N,idealpow(F,PS[i],v[i])));
    my(ans=bnfisprincipal(B,N,1));
    if(ans[1]!=[0,0]~ || idealhnf(F,ans[2])!=N,error("literal principal cube below"));
    my(g=rnfeltup(R,nfbasistoalg(F,ans[2])));
    if(idealpow(E,J,3)!=idealhnf(E,g),error("literal upper cube identity"));
    for(j=1,#ds,if((target+C*v)[j]%ds[j],error("candidate genus zero")));
    listput(records,[[a,b,c],v,N,ans[2],g]);
  )));
  for(i=1,#records,for(j=i+1,#records,if(denominator(H^-1*(records[i][2]-records[j][2]))==1,error("duplicate correction class"))));
  print("CANDIDATE_COUNT ",#records," EXACT_CUBE_IDENTITIES ",#records," DISTINCT_PAIRS ",#records*(#records-1)/2);
  writebin("research_e81/code/e_prime73_candidates.bin",Vec(records));
  print("DONE: all27 exact candidate ideals, principal cube generators, and distinct lattice coordinates.");
};
run();
quit;
