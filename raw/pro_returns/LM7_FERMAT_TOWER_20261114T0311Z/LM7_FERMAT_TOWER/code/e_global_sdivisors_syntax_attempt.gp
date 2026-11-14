default(parisize,256000000);
default(parisizemax,2000000000);
jmat(M)=Str(vector(matsize(M)[1],i,vector(matsize(M)[2],j,M[i,j])));
jmatq(M)=Str(vector(matsize(M)[1],i,vector(matsize(M)[2],j,[numerator(M[i,j]),denominator(M[i,j])]))));
run()={
 my(lo=read("research_e86/code/e_stable_lower_genus.bin"),B=lo[1],F=B.nf,Ray=lo[2],U=lo[5][1],ds=lo[6],rec=List());
 my(S=[2,2;0,1],Sinv=lift(Mod(S,3)^-1));
 forprime(p=2,2000,
  if(p!=3 && p!=17 && valuation(znorder(Mod(17,p)),3)==1,
   my(root=znprimroot(p)^((p-1)/3),zz=0);
   for(k=1,2,if(valuation(znorder(Mod(17,p)*root^k),3)==0,zz=lift(root^k)));
   if(!zz,error("unique complex prime branch"));
   my(m=(p-1)/3^valuation(p-1,3),a=Mod(17*zz,p),r1=lift(a^lift(Mod(3,m)^-1)),r2=lift(a^lift(Mod(9,m)^-1)));
   my(P=idealhnf(F,p,Mod(x,F.pol)-r1),cl=bnfisprincipal(B,P,0),sc=lift(Mod(Sinv*cl,3)),gen=U*bnrisprincipal(Ray,P,0));
   if(idealnorm(F,P)!=p || Mod(r2,p)^3!=Mod(r1,p),error("actual prime norm branch"));
   if((2*(gen[1]+gen[2]+gen[3]))%3,error("lower cubic split character"));
   my(l=lift(Mod(gen[1]-3*gen[2]-3*gen[3],9)),m2=lift(Mod(gen[2],3)));
   if(l%3!=sc[1] || m2!=sc[2],error("actual norm-compatible S-class coordinates"));
   my(z=[p,zz,r1,r2,Vec(cl),Vec(sc),[l,m2]]);
   listput(rec,z);
   print("{\"type\":\"eligible_prime\",\"p\":",p,",\"zeta\":",zz,",\"beta1\":",r1,",\"beta2\":",r2,",\"L1_class\":",Vec(cl),",\"S_class\":",Vec(sc),",\"L2_class\":[",l,",",m2,"]}");
  );
 );
 my(v=Vec(rec),at7=0,at73=0);
 for(i=1,#v,if(v[i][1]==7,at7=i);if(v[i][1]==73,at73=i));
 if(!at7 || !at73 || v[at7][6]!=[2,1] || v[at73][6]!=[0,1],error("two actual pivots"));
 my(ord=concat([at7,at73],select(i->i!=at7 && i!=at73,[1..#v])),N=#ord,Q=matrix(N,N),C=matrix(2,N),L=vector(N));
 Q[1,1]=3;Q[2,2]=3;
 for(j=1,N,
  my(z=v[ord[j]]);C[,j]=Col(z[6]);L[j]=z[7][1];
  if(j>=3,Q[j,j]=1;Q[1,j]=z[6][1];Q[2,j]=-z[6][1]-z[6][2]);
 );
 if(abs(matdet(Q))!=9 || lift(Mod(C*Q,3))!=matrix(2,N),error("complete finite pivot lattice"));
 my(H=mathnf(Q),SM=matsnf(H,1),phase=-L*Q/3);
 if(denominator(phase)!=1 || SM[1]*H*SM[2]!=SM[3],error("exact phase and Smith inverse"));
 print("{\"type\":\"pivot_system\",\"prime_order\":",vector(N,i,v[ord[i]][1]),",\"class_map\":",jmat(C),",\"basis\":",jmat(Q),",\"basis_inverse\":",jmatq(Q^-1),",\"hnf\":",jmat(H),",\"left\":",jmat(SM[1]),",\"right\":",jmat(SM[2]),",\"left_inverse\":",jmat(SM[1]^-1),",\"right_inverse\":",jmat(SM[2]^-1),",\"diagonal\":",vector(N,i,SM[3][i,i]),",\"L2_first_coordinates\":",L,",\"phase_on_basis_mod3\":",lift(Mod(phase,3)),"}");
 print("{\"type\":\"explicit_norm_families\",\"plus_base_norm\":273,\"plus_support\":[3,7,13],\"plus_3_valuation\":1,\"minus_base_norm\":307,\"minus_support\":[307],\"minus_3_valuation\":0}");
 writebin("research_e88/code/e_global_sdivisors.bin",[v,ord,Q,C,L,H,SM,phase]);
 print("{\"type\":\"completion\",\"status\":\"PASS\"}");
};
run();
quit;
