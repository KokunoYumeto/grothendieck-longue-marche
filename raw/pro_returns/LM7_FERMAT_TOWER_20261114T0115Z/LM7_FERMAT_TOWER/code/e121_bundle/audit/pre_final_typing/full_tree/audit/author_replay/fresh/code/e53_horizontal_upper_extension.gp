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
 my(E=read("../inputs/e119_e53_genus_transition.bin"),D=E[1],B=D[1],alpha=D[2],xi=D[3],beta=D[4],Q=D[5],T=D[6],lab=D[8],G=E[3],HB=E[13],KB=E[15],SB=E[17],rhoB=concat(vector(6,i,1),E[6]),a0=sqrtn(53+O(3^100),3));
 my(F=read("../inputs/e119_e53_positional_genus_transition.bin"),L=F[1][4],GL=F[2],HL=F[8],KL=F[10],SL=F[12],rhoL=concat([1,1],F[4]));
 my(J=matrix(9,4),IJ=vector(2),CF=vector(2),CC=matrix(3,2),CH=matrix(6,2));
 for(i=1,3,J[i,1]=1;J[i+3,2]=1);
 for(i=1,2,
  print("{\"type\":\"progress\",\"extended_ideal\":",i,"}");
  my(I=idealhnf(B,subst(lift(nfbasistoalg(L,GL[i][,1])),x,beta)));
  for(k=2,6,I=idealadd(B,I,subst(lift(nfbasistoalg(L,GL[i][,k])),x,beta)));
  check(idealnorm(B,I)==idealnorm(L,GL[i])^3,"literal ideal-extension absolute norm");
  my(cc=bnfisprincipal(B,I,0),R=idealdiv(B,I,idealfactorback(B,G,cc)),pr=bnfisprincipal(B,R,5));
  check(pr[1]==Col(vector(3)) && factoredidealcheck(B,pr[2],R),"complete ideal-extension principal correction");
  my(chi=Col(factoredchars(B,alpha,xi,beta,Q,T,lab,a0,pr[2])));
  IJ[i]=I;CF[i]=pr[2];CC[,i]=cc;CH[,i]=chi;
  for(k=1,6,J[k,i+2]=-chi[k]);for(k=1,3,J[k+6,i+2]=cc[k]);
 );
 check(denominator(HB^-1*J*HL)==1,"actual genus transfer preserves relations");
 check(lift(Mod(rhoB*J,3))==vector(4),"transfer lies in actual cyclic restriction kernel");
 my(JQ=SB[1]*KB^-1*J*KL*SL[1]^-1);
 check(denominator(JQ)==1 && denominator(SB[3]^-1*JQ*SL[3])==1,"actual Smith extension well-defined");
 my(Nd=read("e53_horizontal_upper_norm.bin"),N=Nd[3],NQ=Nd[8],Ad=read("e53_normalizer_actions.bin"),AH=Ad[3][2],HQ=Ad[4][2]);
 check(denominator(HL^-1*(N*J-3*matid(4)))==1,"literal field norm composed with extension isdegree3");
 check(denominator(HB^-1*(J*N-matid(9)-AH-AH^2))==1,"literal extension composed with norm is conjugate sum");
 check(denominator(SL[3]^-1*(NQ*JQ-3*matid(4)))==1,"Smith norm-extension compositiondegree3");
 check(denominator(SB[3]^-1*(JQ*NQ-matid(9)-HQ-HQ^2))==1,"Smith extension-norm conjugate sum");
 check(denominator(SB[3]^-1*(HQ-matid(9))*JQ)==1,"extension image is h-invariant");
 my(image=mathnf(concat(SB[3],JQ)));
 print("{\"type\":\"horizontal_genus_extension\",\"ordinary_class_columns\":",jmat(CC),",\"principal_correction_characters\":",jmat(CH),",\"genus_extension\":",jmat(J),",\"coinvariant_Smith_extension\":",jmat(JQ),",\"image_cokernel_Smith\":",Vec(matsnf(image)),"}");
 writebin("e53_horizontal_upper_extension.bin",[E,F,J,IJ,CF,CC,CH,JQ,image]);
 print("{\"type\":\"completion\",\"status\":\"PASS\"}");
}
quit;
