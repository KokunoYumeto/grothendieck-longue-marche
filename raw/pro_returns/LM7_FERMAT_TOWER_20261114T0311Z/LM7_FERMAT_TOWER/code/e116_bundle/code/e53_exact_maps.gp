\\ Actual divisor norm/extension and quadratic norm coordinates at53.
default(parisize,128000000);
default(parisizemax,1000000000);
check(a,s)=if(!a,error(s));
cf(a,n)=vector(n,i,Str(polcoef(lift(a),i-1)));
jmat(M)=vector(matsize(M)[1],i,Vec(M[i,]));
{
 my(V=read("e53_pure9_norm_witness.bin"),D=V[1],F=D[3],B=V[2],P=V[3],U=V[4]);
 my(ext=matrix(4,3),nd=matrix(3,4),lower=concat(idealprimedec(F,3),idealprimedec(F,53)));
 for(j=1,3,
   my(v=Mod(subst(lift(U[j+1]),x,x^3),B.pol));
   for(i=1,4,ext[i,j]=idealval(B,v,P[i]));
 );
 for(i=1,4,
   my(j=0);for(k=1,3,if(ext[i,k],check(j==0,"unique prime below");j=k));
   check(j>0 && P[i][4]%lower[j][4]==0,"actual prime below and residue degree");
   nd[j,i]=P[i][4]/lower[j][4];
 );
 check(nd*ext==3*matid(3),"actual cubic ideal norm/extension identity");
 print("{\"type\":\"pure_divisor_maps\",\"extension\":",jmat(ext),",\"norm\":",jmat(nd),",\"norm_extension\":",jmat(nd*ext),"}");
 my(Z=read("e53_prime_columns.bin"),C=D[2],a=D[4],z=D[5],Q=D[11],qgen=Z[2]);
 my(basis=[1,a,a^2,z,z*a,z*a^2],T=matrix(6,6,i,j,polcoef(lift(basis[j]),i-1)));
 my(eq=matrix(3,2),nq=matrix(2,3),co=matrix(4,3),nn=vector(3),sg=vector(3));
 for(j=1,2,
   my(v=subst(lift(U[j+1]),x,a));
   for(i=1,3,eq[i,j]=idealval(C,v,Q[i]));
 );
 for(i=1,3,
   my(j=0);for(k=1,2,if(eq[i,k],check(j==0,"unique quadratic prime below");j=k));
   nq[j,i]=Q[i][4]/lower[j][4];
   my(v=qgen[i]*subst(lift(qgen[i]),x,z^2-a),w=matsolve(T,Col(vector(6,j,polcoef(lift(v),j-1)))));
   check(w[4]==0 && w[5]==0 && w[6]==0,"quadratic norm in actual pure field");
   nn[i]=Mod(sum(j=1,3,w[j]*x^(j-1)),F.pol);v=nn[i];
   for(j=1,3,co[j+1,i]=idealval(F,v,lower[j]);v/=U[j+1]^co[j+1,i]);
   my(ex=bnfisunit(F,v));check(#ex==2,"actual lower quadratic unit coordinate");
   co[1,i]=ex[1];sg[i]=lift(v/U[1]^ex[1]);check(sg[i]==1 || sg[i]==-1,"actual quadratic reconstruction sign");
 );
 check(nq*eq==2*matid(2),"actual quadratic ideal norm/extension identity");
 check(nq==co[2..3,],"quadratic principal generator divisor square");
 print("{\"type\":\"quadratic_divisor_maps_PARI_order\",\"extension\":",jmat(eq),",\"norm\":",jmat(nq),",\"norm_extension\":",jmat(nq*eq),"}");
 print("{\"type\":\"quadratic_prime_generator_norms\",\"elements\":",vector(3,i,cf(nn[i],3)),",\"coordinates_in_e_pA_pB_a\":",jmat(co),",\"signs\":",sg,"}");
 writebin("e53_exact_maps.bin",[ext,nd,eq,nq,co,nn,sg]);
 print("{\"type\":\"completion\",\"status\":\"PASS\"}");
}
quit;
