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
ninechars(F,xi,Q3,T,u)={
 my(C=vector(4),v=idealval(F,u,Q3),nn=nfeltnorm(F,u)/3^v);
 check(valuation(nn,3)==0 && valuation(nn-1,3)>=2,"exact normalized ninth wild norm");
 C[2]=lift(Mod(-(nn-1)/9,3));
 for(i=1,3,
  my(vv=idealval(F,u,T[i]),pr=nfmodprinit(F,T[i],'t),rr=nfmodpr(F,u/(53*xi^3)^vv,pr)^((53^2-1)/9),xr=nfmodpr(F,xi,pr),hit=-1);
  for(k=0,8,if(rr==xr^k,hit=k));check(hit>=0,"literal ninth tame phase");C[[1,3,4][i]]=lift(Mod(-hit,9));
 );C;
};
{
 my(E=read("../inputs/e119_e53_genus_transition.bin"),D=E[1],B=D[1],xi=D[3],G=E[3],HB=E[13],KB=E[15],SB=E[17],rhoB=concat(vector(6,i,1),E[6]),BT=D[6]);
 my(Fd=read("e53_order_nine_genus.bin"),F=Fd[1],xf=Mod(x,F.pol),FT=idealprimedec(F,53),FQ=idealprimedec(F,3)[1],HF=Fd[7],KF=Fd[9],SF=Fd[11],rhoF=[1,3,1,1]);
 my(N=matrix(4,9),NI=vector(3),CF=vector(3),CH=matrix(4,3),records=List(),tperm=vector(3));
 for(i=1,3,N[2,i]=1;
  my(pr=nfmodprinit(B,BT[i],'t),hit=0);
  for(j=1,3,if(nfmodpr(B,subst(lift(nfbasistoalg(F,FT[j][2])),x,xi),pr)==0,check(!hit,"unique tame contraction");hit=j));
  check(hit,"tame contraction exists");tperm[i]=hit;N[[1,3,4][hit],i+3]=3;
 );
 for(i=1,3,
  my(fac=idealfactor(B,G[i]),I=idealhnf(F,1));
  for(j=1,matsize(fac)[1],
   my(P=fac[j,1],p=P[1],e=fac[j,2],pr=nfmodprinit(B,P,'t),low=idealprimedec(F,p),hit=0);
   check(isprime(p) && p!=3 && p!=53,"certified outside-S norm factor");
   for(k=1,#low,if(nfmodpr(B,subst(lift(nfbasistoalg(F,low[k][2])),x,xi),pr)==0,check(!hit,"unique contracted F-prime");hit=k));
   check(hit,"actual F-prime contraction");my(W=low[hit],fr=P[4]/W[4]);check(denominator(fr)==1,"actual relative residue degree");
   I=idealmul(F,I,idealpow(F,W,e*fr));listput(records,[i,p,e,P[4],hit,W[4],fr,jmat(idealhnf(F,W))]);
  );
  check(idealnorm(B,G[i])==idealnorm(F,I),"literal F ideal norm equality");
  my(pr=bnfisprincipal(F,I,5),chi=vector(4));check(#pr[1]==0 && factoredidealcheck(F,pr[2],I),"full class-one ideal principal identity");
  for(k=1,matsize(pr[2])[1],chi+=pr[2][k,2]*ninechars(F,xf,FQ,FT,nfbasistoalg(F,pr[2][k,1])));
  for(k=1,4,chi[k]=lift(Mod(chi[k],if(k==2,3,9)));N[k,i+6]=-chi[k]);
  NI[i]=I;CF[i]=pr[2];CH[,i]=Col(chi);
 );
 check(denominator(HF^-1*N*HB)==1,"actual cyclic-nine norm preserves relations");
 check(lift(Mod(rhoF*N-3*rhoB,9))==vector(9),"exact g-cubing restriction square");
 my(NQ=SF[1]*KF^-1*N*KB*SB[1]^-1);
 check(denominator(NQ)==1 && denominator(SF[3]^-1*NQ*SB[3])==1,"exact cyclic-nine quotient map on kernel lattices");
 my(A=read("e53_normalizer_actions.bin"),image=mathnf(concat(SF[3],NQ)));
 check(denominator(SF[3]^-1*NQ*(A[4][1]-matid(9)))==1,"cyclic-nine quotient kills actual g differences");
 check(abs(matdet(image))==1,"actual g-coinvariant quotient is onto");
 my(Cmap=[1,0,1,1;0,1,0,0],qchar=([0,1,0,0]*N*KB*SB[1]^-1));
 check(lift(Mod(Cmap[1,]*Fd[6],9))==vector(matsize(Fd[6])[2]) && lift(Mod(Cmap[2,]*Fd[6],3))==vector(matsize(Fd[6])[2]),"literal compositum Artin rows well-defined");
 print("{\"type\":\"cyclic_nine_actual_comparison\",\"tame_prime_contractions\":",tperm,",\"prime_norm_records\":",Vec(records),",\"principal_correction_characters\":",jmat(CH),",\"genus_norm\":",jmat(N),",\"coinvariant_quotient\":",jmat(NQ),",\"target_Smith_diagonal\":",jmat(SF[3]),",\"cyclotomic_compositum_Artin_map\":",jmat(Cmap),",\"mu27_character_on_Q_sigma\":",qchar,"}");
 writebin("e53_cyclic_nine_comparison.bin",[E,Fd,N,NI,CF,CH,NQ,Vec(records),Cmap,qchar,tperm]);
 print("{\"type\":\"completion\",\"status\":\"PASS\"}");
}
quit;
