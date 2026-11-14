\\ Actual B2/F cyclic-nine genus quotient, from the full certified F S-units.
default(parisize,128000000);
default(parisizemax,1000000000);
check(a,s)=if(!a,error(s));
jmat(M)=vector(matsize(M)[1],i,Vec(M[i,]));
{
 my(D=read("../inputs/e119_e53_horizontal_base.bin"),F=D[1],U=D[2]);
 my(xi=Mod(x,F.pol),z=xi^3,Q=idealprimedec(F,53),Q3=idealprimedec(F,3)[1]);
 my(C=matrix(4,#U),V=matrix(4,#U),NN=vector(#U),b=53*z);
 for(j=1,#U,
  my(v=idealval(F,U[j],Q3),n=nfeltnorm(F,U[j])/3^v,nn=lift(Mod(n,27)));
  check(nn%9==1,"actual cyclotomic unit norm lies in1+9Z3");
  V[1,j]=v;NN[j]=Str(n);C[1,j]=lift(Mod(-(nn-1)/9,3));
 );
 for(i=1,3,
  my(pr=nfmodprinit(F,Q[i],'t),xr=nfmodpr(F,xi,pr));
  for(j=1,#U,
   my(v=idealval(F,U[j],Q[i]),r=nfmodpr(F,U[j]/b^v,pr)^((53^2-1)/9),at=-1);
   V[i+1,j]=v;
   for(k=0,8,if(r==xr^k,at=k));check(at>=0,"literal ninth-power residue");
   C[i+1,j]=lift(Mod(-at,9));
  );
 );
 my(perm=[2,1,3,4],CP=matrix(4,#U,i,j,C[perm[i],j]),rho=[1,3,1,1]);
 my(Rel=concat(matdiagonal([9,3,9,9]),CP),H=mathnf(Rel),SN=matsnf(H,1),K=matid(4));
 K[1,1]=9;for(j=2,4,K[1,j]=-rho[j]);
 check(lift(Mod(rho*Rel,9))==vector(matsize(Rel)[2]),"actual cyclic-nine restriction");
 my(KR=K^-1*H,KS=matsnf(KR,1));check(denominator(KR)==1,"exact restriction kernel lattice");
 check(SN[1]*H*SN[2]==SN[3] && KS[1]*KR*KS[2]==KS[3],"complete Smith maps");
 print("{\"type\":\"cyclic_nine_local_characters\",\"coordinate_order\":[\"q3\",\"t1\",\"t2\",\"t3\"],\"unit_character_matrix\":",jmat(C),",\"S_valuation_matrix\":",jmat(V),",\"wild_normalized_absolute_norms\":",NN,"}");
 print("{\"type\":\"cyclic_nine_genus\",\"coordinate_order\":[\"t1\",\"q3\",\"t2\",\"t3\"],\"relation_matrix\":",jmat(Rel),",\"relation_HNF\":",jmat(H),",\"Smith_left\":",jmat(SN[1]),",\"Smith_right\":",jmat(SN[2]),",\"Smith_diagonal\":",jmat(SN[3]),",\"restriction_row\":",rho,",\"kernel_lattice\":",jmat(K),",\"kernel_relations\":",jmat(KR),",\"kernel_Smith_left\":",jmat(KS[1]),",\"kernel_Smith_right\":",jmat(KS[2]),",\"kernel_Smith_diagonal\":",jmat(KS[3]),"}");
 writebin("e53_order_nine_genus.bin",[F,U,C,V,NN,Rel,H,SN,K,KR,KS]);
 print("{\"type\":\"completion\",\"status\":\"PASS\"}");
}
quit;
