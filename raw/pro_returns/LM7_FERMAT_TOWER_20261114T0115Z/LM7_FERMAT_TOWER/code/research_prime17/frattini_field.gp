default(parisize,512000000);
default(parisizemax,2000000000);
default(realprecision,100);
setrand(1702);
run()={
  my(K=nfinit(y^6+y^3+1),R=rnfinit(K,x^3-3),P=R.polabs);
  print("ABS_POLY ",P);
  my(F=bnfinit(P,1));
  print("CERTIFIED ",bnfcertify(F)," CLASS ",F.cyc," DISC ",F.disc);
  print("ROOTS_OF_UNITY ",F.tu);
  print("ZETA9 ",rnfeltreltoabs(R,Mod(y,K.pol)));
  print("ROOT3 ",rnfeltreltoabs(R,Mod(x,R.pol)));
  print("UNIT_BASIS ",F.fu);
  print("PRIME3 ",idealprimedec(F,3));
  writebin("research_prime17/frattini_field.bin",[F,R]);
};
run();
quit;
