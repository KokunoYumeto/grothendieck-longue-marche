default(parisize,512000000);
default(realprecision,100);
run()={
  my(d=read("research_prime17/frattini_field.bin"),F=d[1],R=d[2]);
  my(z=rnfeltreltoabs(R,Mod(y,R.nf.pol)),r=rnfeltreltoabs(R,Mod(x,R.pol)));
  my(pr3=idealprimedec(F,3)[1],pi=nfbasistoalg(F,bnfisprincipal(F,pr3,1)[2]));
  for(e=-2,4,for(i=0,8,for(c=-3,3,if(c,
    my(v=r-c*z^i*(1-z)^e,n=nfeltnorm(F,v));
    if(n && numerator(abs(n))==3^valuation(numerator(abs(n)),3) && denominator(n)==3^valuation(denominator(n),3),
      my(a=idealval(F,v,pr3),w=bnfisunit(F,v/pi^a));
      print("SMALL ",[c,i,e]," NORM ",n," VECTOR ",concat(concat(vector(8,j,w[j]%3),[a%3]),[w[9]%3]))
    )
  ))));
};
run();
quit;
