default(parisize,256000000);
default(parisizemax,2000000000);
default(realprecision,100);
run()={
  my(dat=read("research_norm_index/code/cyclotomic_base1_bnf.bin"),B=dat[1],F=B.nf,z9=dat[2],beta=dat[3]*z9);
  my(G3=read("research_norm_index/code/cyclotomic_base1_genus.bin"),G9=read("research_norm_index/code/cyclotomic_base1_ninth_genus.bin"));
  my(R3=G3[1],R9=G9[1],RR=bnrinit(B,G9[2],1,27),r=#R9.cyc,chi=vector(r),records=List(),Q=matrix(#R3.cyc,r));
  if(RR.cyc!=R9.cyc,error("explicit ray group changed"));
  for(j=1,r,
    my(v=bnrisprincipal(R9,RR.gen[j],0));
    for(i=1,r,if((v[i]-(i==j))%R9.cyc[i]!=0,error("ray generator basis changed")));
    Q[,j]=bnrisprincipal(R3,RR.gen[j],0);
    my(ff=idealfactor(F,RR.gen[j]),qdata=List());
    for(k=1,matsize(ff)[1],
      my(pr=ff[k,1],pow=ff[k,2],mp=nfmodprinit(F,pr),card=pr.p^pr.f);
      if(pr.p==3 || pr.p==17 || (card-1)%9,error("bad Kummer prime"));
      my(a=nfmodpr(F,beta,mp)^((card-1)/9),z=nfmodpr(F,z9,mp),e=fflog(a,z,9));
      if(z^e!=a,error("Kummer residue"));
      chi[j]=(chi[j]+pow*e)%9;
      listput(qdata,[pr.p,pr.f,pow,e]);
    );
    listput(records,[j,Vec(qdata)]);
  );
  my(H=G9[4],AM=G9[9],p=0);
  for(j=1,r,if(chi[j]%3,p=j;break));
  if(!p || lift(Mod(Mat(chi)*H,9))!=matrix(1,r),error("Kummer character on genus quotient"));
  my(K=matid(r),s=lift(Mod(chi[p],9)^-1));
  for(j=1,r,if(j==p,K[,j]=9*matid(r)[,p],K[,j]=matid(r)[,j]-s*chi[j]*matid(r)[,p]));
  if(abs(matdet(K))!=9 || denominator(K^-1*H)!=1 || denominator(K^-1*AM*K)!=1,error("relative kernel lattice"));
  my(AH=K^-1*H,AP=concat(AH,K^-1*(AM-matid(r))*K),HH=mathnf(AP),S=matsnf(HH,1),ds=vector(r,i,S[3][i,i]));
  if(S[1]*HH*S[2]!=S[3] || abs(matdet(S[1]))!=1 || abs(matdet(S[2]))!=1,error("relative coinvariant Smith"));
  if(denominator(G3[4]^-1*Q*H)!=1 || mathnf(concat(G3[4],Q))!=matid(#R3.cyc),error("genus restriction map"));
  print("ACTUAL_KUMMER_CHARACTER ",chi," PRIME_RECORDS ",Vec(records));
  print("RELATIVE_KERNEL_BASIS ",K," INVERSE ",K^-1," PRESENTATION ",AH);
  print("RELATIVE_DELTA_COINVARIANTS ",ds," HNF ",HH," LEFT ",S[1]," RIGHT ",S[2]);
  print("GENUS_RESTRICTION ",Q);
  my(prs=List());
  for(j=1,3,
    my(cl=G9[12][j][2],v=K^-1*cl,co=S[1]*v,ord=1);
    if(denominator(v)!=1,error("prime outside relative unramified subgroup"));
    for(i=1,r,ord=lcm(ord,ds[i]/gcd(ds[i],co[i])));
    print("ORIGINAL_PRIME3_DETECTED_CLASS ",j," COORD ",co," ORDER ",ord);
    listput(prs,[v,co,ord]);
  );
  writebin("research_norm_index/code/cyclotomic_base1_ninth_transfer.bin",[chi,records,K,AH,AP,HH,S,Q,prs]);
  print("DONE: actual Kummer character, cyclic-base descent and genus restriction.");
};
run();
quit;
