default(parisize,256000000);
default(parisizemax,2000000000);
default(realprecision,100);
run()={
  my(dat=read("research_e81/code/e_prime73_field.bin"),B=dat[1],F=dat[2],R=dat[3],E=dat[4],PS=dat[7],S=dat[8]);
  my(SU=bnfsunit(B,PS),V=matrix(6,6,i,j,idealval(F,SU[1][j],PS[i])));
  if(V!=[3,2,2,1,1,1;0,1,0,0,0,0;0,0,1,0,0,0;0,0,0,1,0,0;0,0,0,0,1,0;0,0,0,0,0,1],error("actual S-unit valuation basis"));
  my(M=concat(3*V,[0,0,0,1,1,1]~),gens=vector(7));
  for(i=1,6,gens[i]=rnfeltup(R,SU[1][i]));
  gens[7]=Mod(variable(E.pol),E.pol)-R[11][3]*R[11][2];
  if(gens[7]^3!=rnfeltup(R,dat[11]),error("actual beta2 embedding"));
  for(j=1,7,
    my(J=matid(54));for(i=1,6,J=idealmul(E,J,idealpow(E,S[i],M[i,j])));
    if(J!=idealhnf(E,gens[j]),error("literal principal S-relation"));
  );
  my(H=mathnf(M),SM=matsnf(H,1));
  if(SM[1]*H*SM[2]!=SM[3] || abs(matdet(H))!=729,error("S-relation Smith maps"));
  print("S_RELATION_MATRIX ",M," HNF ",H," SMITH ",SM," LEFT_INVERSE ",SM[1]^-1," RIGHT_INVERSE ",SM[2]^-1);
  writebin("research_e81/code/e_prime73_relations.bin",[V,SU,M,H,SM,gens]);
  print("DONE: all seven literal principal relations and their complete lattice quotient.");
};
run();
quit;
