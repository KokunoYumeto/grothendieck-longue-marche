default(parisize,256000000);
default(parisizemax,2000000000);
jmat(M)=Str(vector(matsize(M)[1],i,vector(matsize(M)[2],j,M[i,j])));
redmat(M,ds)=matrix(matsize(M)[1],matsize(M)[2],i,j,lift(Mod(M[i,j],ds[i])));
redvec(v,ds)=vector(#ds,i,lift(Mod(v[i],ds[i])))~;
run()={
  my(dat=read("research_e86/code/e_stable_class_coordinates.bin"),RU=dat[1],RL=dat[2]);
  my(up=read("research_e81/code/e_prime73_field.bin"),ar=read("research_e81/code/e_prime73_artin.bin"),ac=read("research_e84/code/e_ramified_class_action.bin"),gn=read("research_norm_index/code/cyclotomic_base1_genus.bin"));
  my(lo=read("research_e86/code/e_stable_lower_genus.bin"));
  my(CU=RU[4][1]*RU[2]^-1,EU=RU[2]*RU[4][1]^-1,CL=RL[4][1]*RL[2]^-1,EL=RL[2]*RL[4][1]^-1,du=[9,3,3],dl=[9,3]);
  my(autos=vector(2));
  for(k=1,2,
    my(GA=gn[5]*bnrgaloismatrix(gn[1],lift(ac[k]))*gn[5]^-1,AA=matrix(4,4,i,j,GA[i,j]),CC=CU*AA*EU,A=redmat(matrix(3,3,i,j,CC[i,j]),du));autos[k]=A;
    print("{\"type\":\"class_action\",\"name\":\"",if(k==1,"h","g"),"\",\"matrix\":",jmat(A),",\"cyclic\":",du,"}");
  );
  my(M=matrix(3,3),NH=matrix(2,3),NV=matrix(2,3),records=List());
  for(j=1,3,
    my(z=RU[5][RU[6][j]],p=z[1],P=idealprimedec(up[2],p)[z[2]],v=CU*Col(z[4]),PL=idealhnf(lo[1].nf,p,Mod(x,lo[1].pol)-z[7]),vl=lo[5][1]*bnrisprincipal(lo[2],PL,0));
    if(idealnorm(lo[1].nf,PL)!=p || z[5]!=0 || z[3]!=1,error("actual contracted degree-one primes"));
    vl=CL*Col(vector(3,i,vl[i]));
    M[,j]=vector(3,i,lift(Mod(v[i],du[i])))~;
    NH[,j]=vector(2,i,lift(Mod(vl[i],dl[i])))~;
    NV[,j]=bnfisprincipal(up[1],P,0);
    listput(records,[p,z[6],z[7],z[9],Vec(M[,j]),Vec(NH[,j]),Vec(NV[,j])]);
  );
  my(Mi=lift(Mod(M,9)^-1),N=redmat(NH*Mi,dl),Nvert=redmat(NV*Mi,[3,3]));
  if(redmat(N*M-NH,dl)!=matrix(2,3) || redmat(Nvert*M-NV,[3,3])!=matrix(2,3),error("norm generator maps"));
  my(seven=List(),F=up[2],Ps=idealprimedec(F,7));
  for(i=1,#Ps,
    my(mp=nfmodprinit(F,Ps[i]));
    if(nfmodpr(F,up[11],mp)==6,
      my(v=ar[3]*bnrisprincipal(ar[1],Ps[i],0),vv=Col(vector(4,j,v[j])),c=CU*vv);
      if(lift(Mod((RU[1]*vv)[1],3))!=0,error("split cubic over the contracted 7 prime"));
      listput(seven,[i,Vec(redvec(vector(3,j,c[j])~,du))]);
    );
  );
  if(#seven!=3 || Vec(seven)!=[[4,[0,2,0]],[5,[0,2,0]],[6,[0,2,0]]],error("actual inertia prime transfer"));
  my(J=matrix(3,2));J[2,1]=1;
  my(Jvert=matrix(3,2));Jvert[1,2]=6;
  if(redmat(J*N-(matid(3)+autos[1]+autos[1]^2),du)!=matrix(3,3) || redmat(N*J-3*matid(2),dl)!=matrix(2,2),error("actual h norm and extension identities"));
  if(redmat(Jvert*Nvert-3*matid(3),du)!=matrix(3,3),error("vertical norm and extension identity"));
  print("{\"type\":\"actual_norms\",\"upper_prime_classes\":",jmat(M),",\"upper_prime_inverse_mod9\":",jmat(Mi),",\"prime_records\":",Vec(records),",\"norm_to_L2\":",jmat(N),",\"extension_from_L2\":",jmat(J),",\"norm_to_B1\":",jmat(Nvert),",\"extension_from_B1\":",jmat(Jvert),",\"seven_transfer\":",Vec(seven),"}");
  my(PL73=idealhnf(lo[1].nf,73,Mod(x,lo[1].pol)-22),PL7=idealhnf(lo[1].nf,7,Mod(x,lo[1].pol)+1),baseM=concat(bnfisprincipal(lo[1],PL73,0)-bnfisprincipal(lo[1],PL7,0),bnfisprincipal(lo[1],PL73,0)));
  print("{\"type\":\"coherent_S_basis\",\"L1_class_matrix\":",jmat(redmat(baseM,[3,3])),",\"L2_long_prime_ratio\":[[73,63],[7,-1]],\"L2_short_prime\":[73,63],\"h_restriction\":[1,0],\"B_to_L_norm\":[0,1],\"L_adjacent_norm\":[[1,0],[0,1]],\"L_adjacent_extension\":[[0,0],[0,0]]}");
  writebin("research_e86/code/e_stable_class_maps.bin",[autos,M,Mi,N,J,Nvert,Jvert,Vec(records),Vec(seven),baseM]);
  print("{\"type\":\"completion\",\"status\":\"PASS\"}");
};
run();
quit;
