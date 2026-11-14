default(parisize,256000000);
default(parisizemax,2000000000);
default(realprecision,100);
run()={
  my(dat=read("research_e81/code/e_prime73_field.bin"),B=dat[1],F=dat[2],R=dat[3],E=dat[4],P=dat[5],PS=dat[7],S=dat[8],xi=dat[10],beta=dat[11],zeta=xi^3,a=beta/xi);
  my(hF=zeta^2*a-zeta*xi,gF=zeta*a-xi,HF=matrix(2,2),GF=matrix(2,2));
  for(i=1,2,HF[,i]=bnfisprincipal(B,nfgaloisapply(F,hF,B.gen[i]),0);GF[,i]=bnfisprincipal(B,nfgaloisapply(F,gF,B.gen[i]),0));
  my(hP=bnfisprincipal(B,nfgaloisapply(F,hF,P),0),gP=bnfisprincipal(B,nfgaloisapply(F,gF,P),0));
  if(lift(Mod(HF*[2,1]~,3))!=hP || lift(Mod(GF*[2,1]~,3))!=gP,error("actual base class map"));
  print("BASE_H_CLASS_MATRIX ",HF," PRIME73_CLASS ",hP);
  print("BASE_G_CLASS_MATRIX ",GF," PRIME73_CLASS ",gP);
  my(ww=Mod(variable(E.pol),E.pol),b2=ww-R[11][3]*R[11][2],xu=rnfeltup(R,xi),au=rnfeltup(R,a),zu=xu^3);
  my(h=b2+R[11][3]*(zu^2*au-zu*xu),g=xu*b2+R[11][3]*(zu*au-xu),sig=zu*b2+R[11][3]*R[11][2]);
  if(nfgaloisapply(E,g,b2)!=xu*b2 || nfgaloisapply(E,g,xu)!=xu || nfgaloisapply(E,g,au)!=zu*au,error("actual g on generators"));
  if(nfgaloisapply(E,g,nfgaloisapply(E,g,g))!=sig,error("g cube equals sigma"));
  my(hperm=vector(6),gperm=vector(6));
  for(i=1,6,
    my(Qh=idealhnf(E,nfgaloisapply(E,h,S[i])),Qg=idealhnf(E,nfgaloisapply(E,g,S[i])));
    for(j=1,6,if(Qh==idealhnf(E,S[j]),hperm[i]=j);if(Qg==idealhnf(E,S[j]),gperm[i]=j));
    if(!hperm[i] || !gperm[i],error("actual upper prime permutation"));
  );
  print("UPPER_H_PRIME_PERMUTATION ",hperm);
  print("UPPER_G_PRIME_PERMUTATION ",gperm);
  writebin("research_e84/code/e_ramified_class_action.bin",[hF,gF,HF,GF,hP,gP,h,g,sig,hperm,gperm]);
  print("DONE: both actual K-automorphisms, exact base class matrices and six-prime permutations.");
};
run();
quit;
