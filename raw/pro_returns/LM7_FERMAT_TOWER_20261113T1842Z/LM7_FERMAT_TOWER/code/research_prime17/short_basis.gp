default(parisize,512000000);
default(realprecision,100);
run()={
  my(d=read("research_prime17/frattini_field.bin"),F=d[1],R=d[2]);
  my(v=read("research_prime17/frattini_residues.bin"),U=v[1],pi=U[9]);
  my(z=rnfeltreltoabs(R,Mod(y,R.nf.pol)),r=rnfeltreltoabs(R,Mod(x,R.pol)));
  my(pr3=idealprimedec(F,3)[1]);
  for(k=1,2,
    my(q=[r,1-z][k],a=idealval(F,q,pr3),w=bnfisunit(F,q/pi^a));
    print("SHORT ",k," VECTOR ",concat(concat(vector(8,i,w[i]%3),[a%3]),[w[9]%3]))
  );
};
run();
quit;
