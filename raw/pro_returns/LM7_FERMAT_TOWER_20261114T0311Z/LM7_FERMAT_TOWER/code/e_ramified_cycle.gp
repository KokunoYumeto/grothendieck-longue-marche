default(parisize,256000000);
default(parisizemax,2000000000);
default(realprecision,100);
setrand(841734);
run()={
  my(dat=read("research_e81/code/e_prime73_field.bin"),B=dat[1],F=dat[2],R=dat[3],E=dat[4],PS=dat[7],S=dat[8],xi=dat[10],beta=dat[11]);
  my(ww=Mod(variable(E.pol),E.pol),b2=ww-R[11][3]*R[11][2],xu=rnfeltup(R,xi),au=rnfeltup(R,beta/xi),zu=xu^3);
  my(h=b2+R[11][3]*(zu^2*au-zu*xu),sig=zu*b2+R[11][3]*R[11][2]);
  if(nfgaloisapply(E,h,b2)!=b2 || nfgaloisapply(E,h,xu)!=zu*xu || nfgaloisapply(E,h,au)!=zu^2*au,error("actual h on generators"));
  if(nfgaloisapply(E,h,nfgaloisapply(E,h,h))!=ww || nfgaloisapply(E,sig,nfgaloisapply(E,sig,sig))!=ww || nfgaloisapply(E,h,sig)!=nfgaloisapply(E,sig,h),error("commuting cubic automorphisms"));
  my(perm=vector(6));
  for(i=1,6,
    my(Q=idealhnf(E,nfgaloisapply(E,h,S[i])),found=0);
    for(j=1,6,if(Q==idealhnf(E,S[j]),perm[i]=j;found++));
    if(found!=1 || idealhnf(E,nfgaloisapply(E,sig,S[i]))!=idealhnf(E,S[i]),error("actual ramified-prime action"));
  );
  print("RAMIFIED_H_PERMUTATION ",perm);
  print("H_ACTION_GENERATORS beta2_fixed xi_to_zeta_xi a_to_zeta2_a; COMMUTES_WITH_SIGMA 1");
  my(J=idealdiv(E,idealmul(E,S[2],S[3]),idealpow(E,S[1],2)),J0=idealdiv(F,idealmul(F,PS[2],PS[3]),idealpow(F,PS[1],2)),ans=bnfisprincipal(B,J0,1));
  if(ans[1]!=[0,0]~,error("base ratio principal"));
  my(g0=rnfeltup(R,nfbasistoalg(F,ans[2])));
  if(idealpow(E,J,3)!=idealhnf(E,g0),error("literal ratio cube"));
  print("BASE_RATIO_CUBE_GENERATOR ",lift(nfbasistoalg(F,ans[2])));
  writebin("research_e84/code/e_ramified_cycle.bin",[h,sig,perm,J,J0,ans[2],g0]);
  my(logs=apply(x->2*log(abs(x))/(3*log(2)),nfeltembed(E,g0)),ul=vector(8,i,apply(x->2*log(abs(x))/(3*log(2)),nfeltembed(E,rnfeltup(R,B.fu[i])))),best=10^100);
  for(k=0,96,
    my(ll=logs);
    if(k>0,
      if(k<=16,my(j=(k+1)\2,sg=if(k%2,1,-1));ll+=sg*ul[j],
        if(k<=48,for(j=1,8,ll+=(random(7)-3)*ul[j]),ll+=vector(27,j,random(25)-12))
      )
    );
    my(weights=apply(x->max(0,round(x-vecmin(ll))),ll),rr=idealred(E,[J,1],weights),nn=idealnorm(E,rr[1]));
    if(nn<best,best=nn;print("RATIO_REDUCTION_IMPROVEMENT ",k+1," NORM ",nn));
    if(nn==1,
      my(g=if(type(rr[2])=="t_MAT",nffactorback(E,rr[2]),rr[2]));
      if(idealhnf(E,g)!=J,error("literal principal ratio"));
      print("RAMIFIED_RATIO_PRINCIPAL_GENERATOR ",lift(nfbasistoalg(E,g)));
      print("RAMIFIED_RATIO_VALUATIONS ",vector(6,i,idealval(E,g,S[i])));
      writebin("research_e84/code/e_ramified_ratio_principal.bin",[J,g,h,sig]);
      print("DONE: actual cubic action and exact principal ratio generator.");return(1)
    );
  );
  print("NO_SMALL_GENERATOR_AFTER 97 REDUCTIONS BEST_NORM ",best);
  print("DONE: actual action and cube identity; bounded generator search only.");
};
run();
quit;
