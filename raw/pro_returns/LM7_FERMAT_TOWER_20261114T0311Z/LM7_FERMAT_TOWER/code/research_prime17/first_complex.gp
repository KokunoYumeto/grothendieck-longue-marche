default(parisize,512000000);
default(parisizemax,2000000000);
default(realprecision,100);
setrand(1701);
check(a,s)=if(!a,error(s));
K=bnfinit(y^2+y+1,1);
R=rnfinit(K,x^3-17*y);
P=x^6+17*x^3+289;
L=bnfinit(P,1);
check(bnfcertify(K)==1 && bnfcertify(L)==1,"uncertified fields");
print("CERTIFIED_CLASS_GROUP ",L.cyc);
print("INTEGRAL_BASIS ",L.zk);
print("RELATIVE_ABSOLUTE_POLYNOMIAL ",R.polabs);
print("CLASS_GENERATORS ",L.gen);
print("FUNDAMENTAL_UNITS ",L.fu);
print("TORSION ",L.tu);
Nelt(u)={
  my(v=Mod(lift(u),x^3-17*Mod(y,K.pol)));
  return(rnfeltnorm(R,v))
};
Nideal(I)={
  my(v=vector(6,i,sum(j=1,6,I[j,i]*L.zk[j])));
  return(rnfidealnormrel(R,rnfidealabstorel(R,v)))
};
run()={
  for(i=1,#L.gen,
    print("CLASS_GEN ",i," FACTOR ",idealfactor(L,L.gen[i]));
    print("CLASS_GEN ",i," NORM_IDEAL ",Nideal(L.gen[i]));
    print("CLASS_GEN_CUBE ",i," PRINCIPAL ",bnfisprincipal(L,idealpow(L,L.gen[i],3),1));
  );
  for(i=1,#L.fu,print("UNIT_NORM ",i," ",Nelt(L.fu[i])));
  forprime(p=2,61,
    my(D=idealprimedec(L,p));
    for(j=1,#D,
      print("PRIME ",p," INDEX ",j," EF ",[D[j][3],D[j][4]],
        " HNF ",idealhnf(L,D[j])," CLASS ",bnfisprincipal(L,D[j],0),
        " NORM_IDEAL ",Nideal(idealhnf(L,D[j])))
    )
  );
  my(T=rnfisnorminit(K,x^3-17*y,1));
  for(i=1,3,
    my(a=[Mod(y,K.pol),Mod(1-y,K.pol),17][i], z=rnfisnorm(T,a));
    print("NORM_EQUATION ",a," SOLUTION ",z);
    if(z[2]==1,
      print("NORM_EQUATION_CHECK ",rnfeltnorm(R,z[1]));
      my(abs=rnfeltreltoabs(R,z[1]));
      print("ABSOLUTE_SOLUTION ",abs," DIVISOR ",idealfactor(L,abs))
    )
  );
};
run();
quit;
