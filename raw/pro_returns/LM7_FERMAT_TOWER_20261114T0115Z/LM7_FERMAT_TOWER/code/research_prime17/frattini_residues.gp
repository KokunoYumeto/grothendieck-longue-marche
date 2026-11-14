default(parisize,512000000);
default(parisizemax,2000000000);
default(realprecision,100);
check(a,s)=if(!a,error(s));
run()={
  my(data=read("research_prime17/frattini_field.bin"),F=data[1],R=data[2],P=F.pol);
  my(z=rnfeltreltoabs(R,Mod(y,R.nf.pol)),r=rnfeltreltoabs(R,Mod(x,R.pol)));
  my(pr3=idealprimedec(F,3)[1],gg=bnfisprincipal(F,pr3,1));
  check(gg[1]==[]~,"prime-three generator");
  my(pi=nfbasistoalg(F,gg[2]),units=concat(concat(F.fu,[pi]),[z]));
  print("PRIME3_GENERATOR ",pi);
  check(#units==10,"unit dimension");
  my(D=idealprimedec(F,17),M=matrix(10,#D));
  check(#D==9,"nine Frattini primes");
  for(j=1,#D,
    my(mp=nfmodprinit(F,D[j]),rz=nfmodpr(F,z^3,mp));
    check(D[j][4]==2,"seventeen residue degree");
    for(i=1,10,M[i,j]=fflog(nfmodpr(F,units[i],mp)^96,rz));
    print("PRIME17 ",j," HNF ",idealhnf(F,D[j])," VECTOR ",M[,j]);
  );
  print("FROBENIUS_MATRIX ",M);
  print("FROBENIUS_RANK ",matrank(Mod(M,3)));
  print("FROBENIUS_RELATIONS ",lift(matker(Mod(M,3))));
  my(D2=idealprimedec(F,2),N=matrix(10,#D2));
  for(j=1,#D2,
    my(mp=nfmodprinit(F,D2[j]),rz=nfmodpr(F,z^3,mp));
    for(i=1,10,N[i,j]=fflog(nfmodpr(F,units[i],mp)^((2^D2[j][4]-1)/3),rz));
    print("PRIME2 ",j," ROOT3_RESIDUE ",nfmodpr(F,r,mp)," VECTOR ",N[,j]);
  );
  print("FROBENIUS2_CUBES ",N);
  writebin("research_prime17/frattini_residues.bin",[units,D,M,D2,N]);
};
run();
quit;
