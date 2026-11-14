default(parisize,256000000);
default(parisizemax,2000000000);
default(realprecision,100);
setrand(1759);
run()={
  my(P=x^18+17*x^9+289);
  print("ORIGINAL ",P);
  my(red=polredbest(P,1));
  print("REDUCED ",red);
  my(F=nfinit(red[1]));
  print("FIELD_DISC ",F.disc," INDEX ",F.index," SIGNATURE ",F.sign);
  print("FIELD_PRIMES3 ",vector(#idealprimedec(F,3),j,[idealprimedec(F,3)[j][3],idealprimedec(F,3)[j][4]]));
  print("FIELD_PRIMES17 ",vector(#idealprimedec(F,17),j,[idealprimedec(F,17)[j][3],idealprimedec(F,17)[j][4]]));
  my(B=bnfinit(F,1));
  print("CERTIFIED ",bnfcertify(B)," CLASS ",B.cyc," NUMBER ",B.no);
  writebin("research_prime17/layer2_reduced.bin",[B,red]);
};
run();
quit;
