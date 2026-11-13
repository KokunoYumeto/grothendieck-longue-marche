default(parisize,256000000);
default(parisizemax,2000000000);
default(realprecision,100);
run()={
  my(dat=read("research_norm_index/code/cyclotomic_base1_bnf.bin"),B=dat[1],F=B.nf,xi=dat[2],a=dat[3],beta=a*xi,pi=beta+1);
  my(rad=read("research_norm_index/code/cyclotomic_base1_ninth_norms.bin"),bids=rad[1]);
  my(ps=concat(idealprimedec(F,3),idealprimedec(F,17)),SU=bnfsunit(B,ps),units=concat(concat([xi],B.fu),SU[1]));
  my(v=[Mod(1,F.pol),Mod(0,F.pol),Mod(0,F.pol)],ns=List(),rows=List(),localK=List(),localS=List(),mats);
  for(k=1,50,
    v=[v[1]+xi*v[3],v[1]+v[2],v[2]+v[3]];
    my(r=1+v[1],N=r^3+xi*v[2]^3+xi^2*v[3]^3-3*xi*r*v[2]*v[3]);
    if(k==1 && N!=8+xi,error("first literal cyclotomic norm"));
    if(vecmax(vector(3,j,abs(idealval(F,N,ps[j]))))!=0,next);
    listput(ns,nfalgtobasis(F,N));
    mats=vector(3,j,Mat(vector(#ns,i,ideallog(F,ns[i],bids[j]))));
    if(vecmin(vector(3,j,matrank(Mod(mats[j],3))))==6,break);
  );
  for(j=1,3,
    my(K=matker(Mod(mats[j]~,3)),row,scale);
    if(matsize(K)!=[7,1],error("cyclotomic kernel rank"));
    row=lift(K[,1]~);scale=lift(Mod(row*ideallog(F,beta,bids[j]),3));
    if(!scale,error("cyclotomic character of beta vanishes"));
    row=lift(Mod(row/scale,3));
    if(lift(Mod(row*ideallog(F,xi,bids[j]),3))!=0,error("xi should be a cyclotomic norm"));
    my(C=concat(rad[3][j][1][1,],row),CC=matrix(2,7,i,k,if(i==1,rad[3][j][1][1,k],row[k])));
    my(H=mathnf(matsolvemod(CC,[9,3]~,0,1)[2]),S=matsnf(H,1));
    if(abs(matdet(H))!=27 || denominator(matdiagonal([9,3])^-1*CC*H)!=1,error("joint local norm index"));
    if(S[1]*H*S[2]!=S[3] || abs(matdet(S[1]))!=1 || abs(matdet(S[2]))!=1,error("local Smith maps"));
    listput(rows,row);listput(localK,H);listput(localS,S);
    print("MU27_LOCAL_CHARACTER ",j," ROW ",row," BETA_VALUE 1 XI_VALUE 0 PI_VALUE 2");
    print("MU27_JOINT_LOCAL_KERNEL ",j," CHARACTERS ",CC," HNF ",H," SMITH ",S," INVERSE_LEFT ",S[1]^-1," INVERSE_RIGHT ",S[2]^-1);
  );
  my(M9=matrix(6,#units),P3=matrix(6,#units),V=matrix(6,#units,i,k,idealval(F,units[k],ps[i])));
  for(j=1,3,
    my(radrow=rad[3][j][1][1,]);
    for(k=1,#units,
      my(u=nfeltdiv(F,units[k],pi^V[j,k]),lg=ideallog(F,u,bids[j]));
      M9[j,k]=lift(Mod(radrow*lg,9));
      P3[j,k]=lift(Mod(rows[j]*lg+2*V[j,k],3));
    );
  );
  for(j=4,6,
    my(bid=idealstar(F,ps[j],2,9));
    for(k=1,#units,
      my(u=nfeltdiv(F,units[k],beta^V[j,k]));
      M9[j,k]=ideallog(F,u,bid)[1];
      P3[j,k]=lift(Mod(2*V[j,k],3));
    );
  );
  if(lift(Mod(vector(6,j,1)*P3,3))!=vector(#units,k,0),error("actual cyclotomic reciprocity"));
  my(tweights=vector(3,j,lift(Mod(4/M9[j+3,1],9))),qw=matsolvemod(vecextract(M9,"1..3","..")~,9,-vecextract(M9,"4..6","..")~*tweights~));
  my(weights=concat(Vec(qw),tweights));
  if(lift(Mod(weights*M9,9))!=vector(#units,k,0),error("actual radical reciprocity normalization"));
  my(M=concat(M9~,P3~)~,ds=concat(vector(6,j,9),vector(6,j,3)),H=mathnf(concat(matdiagonal(ds),M)),S=matsnf(H,1));
  my(N9=mathnf(matsolvemod(M9,9,0,1)[2]),res=lift(Mod(P3*N9,3)),rr=matrank(Mod(res,3)));
  my(OU=vecextract(M,"..","1..9"),OH=mathnf(concat(matdiagonal(ds),OU)),OS=matsnf(OH,1));
  if(S[1]*H*S[2]!=S[3] || OS[1]*OH*OS[2]!=OS[3],error("global Smith maps"));
  print("MU27_S_UNIT_CHARACTERS M9 ",M9," P3 ",P3," ACTUAL_RADICAL_WEIGHTS ",weights);
  print("MU27_S_UNIT_IMAGE_ORDER ",prod(j=1,#ds,ds[j])/abs(matdet(H))," COKERNEL_SMITH ",S[3]," HNF ",H," LEFT ",S[1]," RIGHT ",S[2]);
  print("MU27_FIELD_NORM_KERNEL ",N9," CYCLOTOMIC_IMAGE ",res," RANK ",rr);
  print("MU27_ORDINARY_UNIT_IMAGE_ORDER ",prod(j=1,#ds,ds[j])/abs(matdet(OH))," COKERNEL_SMITH ",OS[3]);
  writebin("research_e94/code/e_mu27_local.bin",[B,F,xi,a,beta,ps,SU,units,V,Vec(ns),mats,Vec(rows),Vec(localK),Vec(localS),M9,P3,weights,H,S,N9,res,OH,OS]);
  print("DONE: exact mu27 local characters and joint norm lattices.");
};
run();
quit;
