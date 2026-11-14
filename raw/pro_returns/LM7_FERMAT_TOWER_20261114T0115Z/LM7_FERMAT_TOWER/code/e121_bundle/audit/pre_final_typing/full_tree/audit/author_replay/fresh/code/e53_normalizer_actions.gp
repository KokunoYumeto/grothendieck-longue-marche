\\ Exact ordinary class generation and next S-genus quotient from actual ideals.
default(parisize,256000000);default(parisizemax,2000000000);
check(a,s)=if(!a,error(s));
cf(a,n)=vector(n,i,Str(polcoef(lift(a),i-1)));
jmat(M)=vector(matsize(M)[1],i,Vec(M[i,]));
localchars(B,alpha,xi,beta,Q,T,lab,a0,u)={
 my(v=vector(6),py=polcyclo(9,'y));
 for(j=0,2,
  my(loc=Mod(y-a0*y^(3*j),py),nn=polresultant(py,lift(subst(lift(u),x,loc)),'y),nb=polresultant(py,1+a0*y^(1+3*j),'y),vv=idealval(B,u,Q[lab[j+1]]),un=nn/nb^vv);
  check(valuation(un,3)==0 && valuation(un-1,3)>=2 && padicprec(un,3)>=4,"local norm precision");
  v[j+1]=lift(Mod(-(lift(un)-1)/9,3));
 );
 for(j=1,3,
  my(pr=nfmodprinit(B,T[j],'t),zz=nfmodpr(B,xi^3,pr),vv=idealval(B,u,T[j]),rr=nfmodpr(B,u/beta^vv,pr)^((53^2-1)/3));
  v[j+3]=if(rr==1,0,if(rr==zz,2,if(rr==zz^2,1,error("tame phase"))));
 );v;
};
factoredchars(B,alpha,xi,beta,Q,T,lab,a0,f)={
 my(v=vector(6));
 for(k=1,matsize(f)[1],v+=f[k,2]*localchars(B,alpha,xi,beta,Q,T,lab,a0,nfbasistoalg(B,f[k,1])));
 lift(Mod(v,3));
};
factoredidealcheck(B,f,I)={
 my(M=Map());
 for(k=1,matsize(f)[1],
  my(V=idealfactor(B,f[k,1]));
  for(j=1,matsize(V)[1],check(isprime(V[j,1][1]),"proved rational prime in principal divisor");my(key=Str(idealhnf(B,V[j,1])),old=if(mapisdefined(M,key),mapget(M,key),0));mapput(~M,key,old+f[k,2]*V[j,2]));
 );
 my(V=idealfactor(B,I));
 for(j=1,matsize(V)[1],my(key=Str(idealhnf(B,V[j,1])),old=if(mapisdefined(M,key),mapget(M,key),0));mapput(~M,key,old-V[j,2]));
 my(keys=Vec(M));for(j=1,#keys,if(mapget(M,keys[j])!=0,return(0)));1;
};
{
 my(E=read("../inputs/e119_e53_genus_transition.bin"),D=E[1],B=D[1],alpha=D[2],xi=D[3],beta=D[4],Q=D[5],T=D[6],lab=D[8],S=concat(vector(3,j,Q[lab[j]]),T),G=E[3],H=E[13],Rel=E[12],SN=E[14],K=E[15],KS=E[17],rho=concat(vector(6,i,1),E[6]),a0=sqrtn(53+O(3^100),3));
 my(auts=[xi-xi^3*alpha,xi^4-xi^-3*alpha],names=["g","h"],MA=vector(2),MQ=vector(2),Perm=vector(2),corrs=vector(2),classes=vector(2),chars=vector(2));
 check(nfgaloisapply(B,auts[1],xi)==xi && nfgaloisapply(B,auts[1],alpha)==xi^3*alpha,"literal g on generators");
 check(nfgaloisapply(B,auts[2],xi)==xi^4 && nfgaloisapply(B,auts[2],alpha)==xi^-3*alpha,"literal h on generators");
 for(at=1,2,
  my(aut=nfalgtobasis(B,auts[at]),A=matrix(9,9),pm=vector(6),cfac=vector(3),ccmat=matrix(3,3),chmat=matrix(6,3));
  for(i=1,6,
   my(J=idealhnf(B,nfgaloisapply(B,aut,S[i])),hit=0);
   for(j=1,6,if(J==idealhnf(B,S[j]),hit=j));check(hit,"actual S-prime permutation");
   pm[i]=hit;A[hit,i]=1;
  );
  for(i=1,3,
   print("{\"type\":\"progress\",\"normalizer\":\"",names[at],"\",\"ideal\":",i,"}");
   my(I=idealhnf(B,nfgaloisapply(B,aut,G[i])),cc=bnfisprincipal(B,I,0),J=idealdiv(B,I,idealfactorback(B,G,cc)),pr=bnfisprincipal(B,J,5));
   check(pr[1]==Col(vector(3)),"literal normalizer class correction");
   check(factoredidealcheck(B,pr[2],J),"exact normalizer principal-ideal identity");
   cfac[i]=pr[2];ccmat[,i]=cc;chmat[,i]=Col(factoredchars(B,alpha,xi,beta,Q,T,lab,a0,pr[2]));
   for(j=1,6,A[j,i+6]=-chmat[j,i]);for(j=1,3,A[j+6,i+6]=cc[j]);
  );
  check(denominator(H^-1*A*Rel)==1,"normalizer preserves full genus relation lattice");
  check(lift(Mod(rho*A-rho,3))==vector(9),"actual cyclic restriction invariant");
  check(denominator(K^-1*A*K)==1,"actual restriction kernel preserved");
  my(Aq=KS[1]*(K^-1*A*K)*KS[1]^-1);
  check(denominator(KS[3]^-1*Aq*KS[3])==1,"Smith action is well-defined");
  MA[at]=A;MQ[at]=Aq;Perm[at]=pm;corrs[at]=cfac;classes[at]=ccmat;chars[at]=chmat;
  writebin(Str("e53_normalizer_",names[at],"_checkpoint.bin"),[A,Aq,pm,cfac,ccmat,chmat]);
  print("{\"type\":\"actual_normalizer\",\"name\":\"",names[at],"\",\"field_generator_image\":",cf(auts[at],18),",\"S_prime_permutation\":",pm,",\"ideal_class_columns\":",jmat(ccmat),",\"principal_correction_characters\":",jmat(chmat),",\"genus_action\":",jmat(A),",\"coinvariant_Smith_action\":",jmat(Aq),"}");
 );
 check(denominator(H^-1*(MA[1]^3-matid(9)))==1 && denominator(H^-1*(MA[2]^3-matid(9)))==1,"actual order-three actions on genus");
 check(denominator(H^-1*(MA[2]*MA[1]-MA[1]*MA[2]))==1,"actual commuting quotient actions");
 my(N0=matconcat([matrix(2,6),E[5][1..2,]]),HP=[2,2;1,0]);
 check(lift(Mod(N0*MA[1]-N0,3))==matrix(2,9),"g-equivariant class norm");
 check(lift(Mod(N0*MA[2]-HP*N0,3))==matrix(2,9),"h-equivariant class norm");
 my(DQ=KS[3],cg=mathnf(concat(DQ,MQ[1]-matid(9))),ch=mathnf(concat(DQ,MQ[2]-matid(9))),cgh=mathnf(concat(concat(DQ,MQ[1]-matid(9)),MQ[2]-matid(9))));
 print("{\"type\":\"actual_action_quotients\",\"Q_sigma_diagonal\":",jmat(DQ),",\"g_coinvariant_HNF\":",jmat(cg),",\"g_coinvariant_Smith\":",Vec(matsnf(cg)),",\"h_coinvariant_Smith\":",Vec(matsnf(ch)),",\"joint_coinvariant_Smith\":",Vec(matsnf(cgh)),",\"lower_h_action\":",jmat(HP),"}");
 writebin("e53_normalizer_actions.bin",[E,auts,MA,MQ,Perm,corrs,classes,chars,cg,ch,cgh]);
 print("{\"type\":\"completion\",\"status\":\"PASS\"}");
}
quit;
