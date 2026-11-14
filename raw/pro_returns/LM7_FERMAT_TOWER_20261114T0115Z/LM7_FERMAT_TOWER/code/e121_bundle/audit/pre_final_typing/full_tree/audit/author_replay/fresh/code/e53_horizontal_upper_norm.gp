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
lc(L,beta,z,Q,T,u)={
 my(v=idealval(L,u,Q),nu=nfeltnorm(L,u)/2757^v,pr=nfmodprinit(L,T,'t),rr=nfmodpr(L,u/beta^idealval(L,u,T),pr)^((53^2-1)/3),zz=nfmodpr(L,z,pr));
 check(valuation(nu,3)==0 && valuation(nu-1,3)>=2,"literal wild norm quotient");
 [lift(Mod(-(nu-1)/9,3)),if(rr==1,0,if(rr==zz,2,if(rr==zz^2,1,error("tame phase"))))];
};
{
 my(E=read("../inputs/e119_e53_genus_transition.bin"),D=E[1],B=D[1],beta=D[4],G=E[3],HB=E[13],KB=E[15],SB=E[17],rhoB=concat(vector(6,i,1),E[6]));
 my(F=read("../inputs/e119_e53_positional_genus_transition.bin"),L=F[1][4],SL=F[1][5],GL=F[2],HL=F[8],KL=F[10],KLs=F[12],rhoL=concat([1,1],F[4]),bl=Mod(x,L.pol),zl=bl^3/53);
 my(N=matrix(4,9),NI=vector(3),CF=vector(3),CC=matrix(2,3),CH=matrix(2,3),records=List());
 for(i=1,3,N[1,i]=1;N[2,i+3]=1);
 for(i=1,3,
  my(fac=idealfactor(B,G[i]),I=idealhnf(L,1));
  for(j=1,matsize(fac)[1],
   my(P=fac[j,1],e=fac[j,2],p=P[1],pr=nfmodprinit(B,P,'t),low=idealprimedec(L,p),hit=0);
   check(isprime(p) && p!=3 && p!=53,"certified outside-S prime for actual contraction");
   for(k=1,#low,
    my(ww=nfbasistoalg(L,low[k][2]),img=subst(lift(ww),x,beta));
    if(nfmodpr(B,img,pr)==0,check(hit==0,"unique contracted prime");hit=k);
   );
   check(hit,"actual prime contraction exists");my(W=low[hit],fr=P[4]/W[4]);
   check(denominator(fr)==1,"actual residue-degree quotient integral");
   I=idealmul(L,I,idealpow(L,W,e*fr));
   listput(records,[i,p,e,P[4],hit,W[4],fr,jmat(idealhnf(L,W))]);
  );
  check(idealnorm(B,G[i])==idealnorm(L,I),"actual ideal norm absolute norm equality");
  my(cc=bnfisprincipal(L,I,0),J=idealdiv(L,I,idealfactorback(L,GL,cc)),pr=bnfisprincipal(L,J,5),chi=vector(2));
  check(pr[1]==[0,0]~ && factoredidealcheck(L,pr[2],J),"complete horizontal ideal correction");
  for(j=1,matsize(pr[2])[1],chi+=pr[2][j,2]*lc(L,bl,zl,SL[1],SL[2],nfbasistoalg(L,pr[2][j,1])));
  chi=lift(Mod(chi,3));NI[i]=I;CF[i]=pr[2];CC[,i]=cc;CH[,i]=Col(chi);
  for(j=1,2,N[j,i+6]=-chi[j];N[j+2,i+6]=cc[j]);
 );
 check(denominator(HL^-1*N*HB)==1,"horizontal norm on full genus relation lattices");
 check(lift(Mod(rhoL*N-rhoB,3))==vector(9),"horizontal norm actual cyclic restriction square");
 my(NQ=KLs[1]*KL^-1*N*KB*SB[1]^-1);
 check(denominator(NQ)==1,"horizontal norm maps exact restriction kernel lattices");
 check(denominator(KLs[3]^-1*NQ*SB[3])==1,"horizontal Smith norm well-defined");
 my(A=read("e53_normalizer_actions.bin"));
 check(denominator(KLs[3]^-1*NQ*(A[4][2]-matid(9)))==1,"actual h-invariance of horizontal norm");
 my(image=mathnf(concat(KLs[3],NQ)));
 print("{\"type\":\"horizontal_genus_norm\",\"prime_contractions\":",Vec(records),",\"ordinary_class_columns\":",jmat(CC),",\"principal_correction_characters\":",jmat(CH),",\"genus_norm\":",jmat(N),",\"coinvariant_Smith_norm\":",jmat(NQ),",\"target_relation_diagonal\":",jmat(KLs[3]),",\"image_HNF\":",jmat(image),",\"image_cokernel_Smith\":",Vec(matsnf(image)),"}");
 writebin("e53_horizontal_upper_norm.bin",[E,F,N,NI,CF,CC,CH,NQ,image,Vec(records)]);
 print("{\"type\":\"completion\",\"status\":\"PASS\"}");
}
quit;
