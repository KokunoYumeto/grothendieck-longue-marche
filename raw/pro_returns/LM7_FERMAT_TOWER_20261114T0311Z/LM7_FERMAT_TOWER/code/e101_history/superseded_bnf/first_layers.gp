default(parisizemax, 4000000000);
default(realprecision, 80);
pols = [x^3-17, x^6+17*x^3+289, x^9-17, x^18+17*x^9+289];
run()={
for(i=1,#pols,
  P=pols[i];
  print("FIELD ",i," POLY ",P);
  B=bnfinit(P,1);
  print("CERTIFIED ",bnfcertify(B));
  print("CLASS_NUMBER ",B.no," CLASS_CYC ",B.cyc);
  print("SIGNATURE ",B.sign," DISCRIMINANT ",B.disc);
  forprime(p=3,17,if(p==3 || p==17,
    D=idealprimedec(B,p);
    print("PRIME ",p," EF ",vector(#D,j,[D[j][3],D[j][4]]))
  ));
);
};
run();
quit;
