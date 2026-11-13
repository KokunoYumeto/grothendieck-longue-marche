default(parisize,256000000);
default(parisizemax,2000000000);
default(realprecision,100);
run()={
  my(D=read("research_e94/code/e_mu27_local.bin"),B=D[1],F=D[2],xi=D[3],a=D[4],beta=D[5],ps=D[6],pi=beta+1);
  my(old=read("research_norm_index/code/cyclotomic_base1_ninth_genus.bin"),fac=old[2],R=bnrinit(B,fac,1,27),r=#R.cyc,crt=idealchinese(F,fac));
  if(R.cyc!=old[1].cyc,error("ray group basis changed"));
  my(rels=List(),records=List());
  for(j=1,6,
    if(j<=3,
      my(bid=idealstar(F,idealpow(F,ps[j],16),2,9),K=D[13][j]);
      for(k=1,7,
        my(u=nffactorback(F,bid.gen,K[,k]),vals=vector(6,i,1));vals[j]=u;
        my(z=idealchinese(F,crt,vals),cl=bnrisprincipal(R,z,0));
        listput(rels,cl);listput(records,[j,"joint_kernel",k,cl]);
      );
      my(full=idealstar(F,idealpow(F,ps[j],16),2));
      for(k=1,#full.gen,
        my(vals=vector(6,i,1));vals[j]=nfeltpow(F,full.gen[k],9);
        my(z=idealchinese(F,crt,vals),cl=bnrisprincipal(R,z,0));
        listput(rels,cl);listput(records,[j,"ninth",k,cl]);
      );
    ,
      my(bid=idealstar(F,ps[j],2));
      for(k=1,#bid.gen,
        my(vals=vector(6,i,1));vals[j]=nfeltpow(F,bid.gen[k],9);
        my(z=idealchinese(F,crt,vals),cl=bnrisprincipal(R,z,0));
        listput(rels,cl);listput(records,[j,"ninth",k,cl]);
      );
    );
  );
  my(H=mathnf(concat(matdiagonal(R.cyc),Mat(Vec(rels)))),S=matsnf(H,1),ds=vector(r,i,S[3][i,i]));
  if(S[1]*H*S[2]!=S[3] || abs(matdet(S[1]))!=1 || abs(matdet(S[2]))!=1,error("ordinary genus Smith"));
  if(abs(matdet(H))!=3^10,error("ordinary genus predicted idelic order"));
  if(denominator(old[4]^-1*H)!=1,error("literal restriction to original ninth genus"));
  print("MU27_ORDINARY_GENUS ORDERS ",ds," HNF ",H," LEFT ",S[1]," RIGHT ",S[2]," LEFT_INVERSE ",S[1]^-1," RIGHT_INVERSE ",S[2]^-1);
  my(chi=matrix(2,r),classes=vector(r),basis=matrix(r,r),prime_records=List());
  for(j=1,r,
    basis[,j]=bnrisprincipal(R,R.gen[j],0);
    classes[j]=bnfisprincipal(B,R.gen[j],0)[2]%3;
    my(ff=idealfactor(F,R.gen[j]),rec=List());
    for(k=1,matsize(ff)[1],
      my(pr=ff[k,1],pw=ff[k,2],mp=nfmodprinit(F,pr),q=pr.p^pr.f);
      if(pr.p==3 || pr.p==17 || (q-1)%9,error("bad marked Kummer prime"));
      my(z=nfmodpr(F,xi,mp),c=nfmodpr(F,beta,mp),e=fflog(c^((q-1)/9),z,9),f=fflog(z^((q-1)/3),z^3,3));
      if(z^e!=c^((q-1)/9) || z^(3*f)!=z^((q-1)/3),error("literal Kummer residue"));
      chi[1,j]=(chi[1,j]+pw*e)%9;chi[2,j]=(chi[2,j]+pw*f)%3;
      listput(rec,[pr.p,pr.f,pw,e,f]);
    );
    listput(prime_records,[j,Vec(rec)]);
  );
  my(inv=matrix(r,r));for(j=1,r,inv[,j]=matsolvemod(basis,R.cyc~,matid(r)[,j]));
  if(denominator(matdiagonal(R.cyc)^-1*(basis*inv-matid(r)))!=1,error("actual ray basis inverse"));
  chi=chi*inv;for(j=1,r,chi[1,j]=chi[1,j]%9;chi[2,j]=chi[2,j]%3);
  classes=lift(Mod(classes*inv,3));
  if(denominator(matdiagonal([9,3])^-1*chi*H)!=1,error("Kummer characters fail to descend"));
  my(K=mathnf(matsolvemod(chi,[9,3]~,0,1)[2]),P=K^-1*H,KS=matsnf(P,1));
  if(abs(matdet(K))!=27 || denominator(P)!=1 || KS[1]*P*KS[2]!=KS[3],error("relative genus maps"));
  print("MU27_ACTUAL_KUMMER_CHARACTERS ",chi," PRIME_RECORDS ",Vec(prime_records)," RAY_BASIS ",basis," INVERSE ",inv," BASE_S_CLASS ",classes);
  print("MU27_RELATIVE_ORDINARY_GENUS K ",K," K_INVERSE ",K^-1," PRESENTATION ",P," SMITH ",KS);
  my(scols=List(),srecs=List());
  for(j=1,6,
    my(f2=fac,vals=vector(6,i,1),v=if(j<=3,1,3),u=if(j<=3,pi/beta^2,beta^3));
    f2[j,2]=fac[j,2]+v;vals[j]=u;
    my(z=idealchinese(F,f2,vals),I=idealdiv(F,z,idealpow(F,ps[j],v)),cl=-bnrisprincipal(R,I,0));
    for(k=1,6,if(idealval(F,I,ps[k])!=0,error("full local norm ideal not coprime")));
    if(denominator(matdiagonal([9,3])^-1*chi*cl)!=1,error("full local norm not in Kummer kernel"));
    listput(scols,cl);listput(srecs,[j,v,u,I,cl]);
    print("MU27_S_NORM_UNIFORMIZER ",j," VALUATION ",v," ELEMENT ",u," IDEAL ",I," RAY_CLASS ",cl);
  );
  my(HS=mathnf(concat(H,Mat(Vec(scols)))),SS=matsnf(HS,1),PS=K^-1*HS,KSS=matsnf(PS,1));
  if(SS[1]*HS*SS[2]!=SS[3] || KSS[1]*PS*KSS[2]!=KSS[3] || denominator(PS)!=1,error("S genus exact Smith"));
  if(abs(matdet(HS))!=3^6 || abs(matdet(PS))!=27,error("S genus predicted idelic order"));
  if(lift(Mod(classes*HS,3))!=vector(r,i,0),error("base S-class norm map"));
  print("MU27_S_GENUS HNF ",HS," SMITH ",SS," LEFT_INVERSE ",SS[1]^-1," RIGHT_INVERSE ",SS[2]^-1);
  print("MU27_RELATIVE_S_GENUS PRESENTATION ",PS," SMITH ",KSS," LEFT_INVERSE ",KSS[1]^-1," RIGHT_INVERSE ",KSS[2]^-1," NORM_ROW ",classes*K*KSS[1]^-1);
  my(autH=a*xi^-3-xi^4,autG=a*xi^3-xi,AH=bnrgaloismatrix(R,lift(autH)),AG=bnrgaloismatrix(R,lift(autG)));
  if(subst(F.pol,x,autH)!=0 || subst(F.pol,x,autG)!=0,error("base automorphism equations"));
  if(subst(lift(beta),x,autH)!=beta || subst(lift(xi),x,autH)!=xi^4,error("H restriction"));
  if(subst(lift(beta),x,autG)!=xi^3*beta || subst(lift(xi),x,autG)!=xi,error("G restriction"));
  for(i=1,2,
    my(A=if(i==1,AG,AH));
    if(denominator(H^-1*A*H)!=1 || denominator(HS^-1*A*HS)!=1 || denominator(K^-1*A*K)!=1,error("actual invariant genus lattices"));
    print("MU27_BASE_ACTION ",i," RAY ",A," RELATIVE_S ",KSS[1]*K^-1*A*K*KSS[1]^-1);
  );
  writebin("research_e94/code/e_mu27_genus.bin",[R,H,S,chi,K,P,KS,HS,SS,PS,KSS,classes,AG,AH,Vec(records),Vec(prime_records),Vec(srecs),basis,inv]);
  print("DONE: actual ordinary and S-split mu27 genus quotients and all restriction maps.");
};
run();
quit;
