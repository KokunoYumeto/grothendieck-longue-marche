default(parisize,256000000);
default(parisizemax,2000000000);
default(realprecision,100);
setrand(841731);
run()={
  my(dat=read("research_e81/code/e_prime73_field.bin"),B=dat[1],F=dat[2],R=dat[3],E=dat[4],S=dat[8],xi=dat[10],beta=dat[11]);
  my(zeta=xi^3,c1=beta+1+3*zeta,target=xi*c1,cup=rnfeltup(R,c1),J=matid(54));
  for(i=1,3,J=idealmul(E,J,S[i]));
  if(idealpow(E,J,3)!=idealhnf(E,cup) || idealnorm(E,J)!=27,error("actual ideal cube"));
  if(nfeltnorm(F,c1)!=27 || (1+3*zeta)^3!=1-18*zeta,error("downward norm identities"));
  print("C1_BASE_VALUATIONS ",vector(6,i,idealval(F,c1,dat[7][i])));
  for(i=4,6,
    my(mp=nfmodprinit(F,dat[7][i]),r=nfmodpr(F,c1,mp),correct=nfmodpr(F,target,mp));
    if(r^96!=nfmodpr(F,zeta,mp) || correct^96!=1,error("local17 norm correction"));
    print("LOCAL17 ",i-3," C1_CUBIC_RESIDUE ",r^96," XI_C1_CUBIC_RESIDUE ",correct^96);
  );
  my(logs=apply(x->2*log(abs(x))/(3*log(2)),nfeltembed(E,cup)),baseweights=apply(x->round(x-vecmin(logs)),logs));
  my(unitlogs=vector(8,i,apply(x->2*log(abs(x))/(3*log(2)),nfeltembed(E,rnfeltup(R,B.fu[i])))),best=10^100,count=0);
  for(k=0,48,
    my(ll=logs);
    if(k>0,
      if(k<=16,
        my(j=(k+1)\2,sg=if(k%2,1,-1));ll+=sg*unitlogs[j],
        for(j=1,8,ll+=(random(7)-3)*unitlogs[j])
      )
    );
    my(weights=apply(x->max(0,round(x-vecmin(ll))),ll),red=idealred(E,[J,1],weights),nn=idealnorm(E,red[1]));
    count++;
    if(nn<best,best=nn;print("ROOT_PROFILE_IMPROVEMENT ",count," NORM ",nn," WEIGHTS ",weights));
    if(nn==1,
      my(g=if(type(red[2])=="t_MAT",nffactorback(E,red[2]),red[2]));
      if(idealhnf(E,g)!=J,error("exact principal witness"));
      my(nm=rnfeltnorm(R,rnfeltabstorel(R,nfbasistoalg(E,g))),u=nfeltdiv(F,nm,c1));
      if(idealhnf(F,u)!=matid(18),error("norm quotient is an ordinary unit"));
      print("PRINCIPAL_J_GENERATOR ",lift(nfbasistoalg(E,g)));
      print("RELATIVE_NORM ",lift(nm)," UNIT_RATIO_COORDINATES ",bnfisunit(B,u));
      writebin("research_e84/code/e_c1_root_profile_witness.bin",[J,g,nm,u]);
      print("DONE: positive exact principal ideal and norm certificate.");return(1)
    );
  );
  print("NO_POSITIVE_WITNESS_AFTER ",count," ROOT_PROFILE_REDUCTIONS BEST_NORM ",best);
  print("DONE: exact local obstruction and bounded profile search; no nonprincipality inference.");
};
run();
quit;
