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
 my(D=read("e53_six_character_witness.bin"),Gd=read("e53_genus_kummer.bin"),B=D[1],alpha=D[2],xi=D[3],beta=D[4],Q=D[5],T=D[6],U=D[7],lab=D[8],C=D[10],S=concat(Q,T),a0=sqrtn(53+O(3^100),3),pis=vector(3,i,subst(lift(Gd[3][i]),x,xi)));
 my(G=vector(3),corr=vector(3));
 for(i=1,3,
  my(ap=idealappr(B,matrix(6,2,r,c,if(c==1,S[r],idealval(B,B.gen[i],S[r])))));
  corr[i]=nfbasistoalg(B,ap);G[i]=idealdiv(B,B.gen[i],ap);
  check(vector(6,j,idealval(B,G[i],S[j]))==vector(6),"class generator moved outsideS");
 );
 my(gclass=matrix(3,3),ff=vector(3),factorrecords=List());
 for(i=1,3,
  my(Fac=idealfactor(B,G[i]),count=matsize(Fac)[1]);
  for(j=1,count,
   my(P=Fac[j,1],e=Fac[j,2],p=P[1],qq=p^P[4],pr=nfmodprinit(B,P,'t),zz=nfmodpr(B,xi^3,pr),vv=vector(4));
   check(p!=3 && p!=53 && isprime(p),"proved outside-S ideal factor");
   for(k=1,4,
    my(rr=nfmodpr(B,if(k<=3,pis[k],beta),pr)^((qq-1)/3));
    vv[k]=if(rr==1,0,if(rr==zz,1,if(rr==zz^2,2,error("Frobenius root"))));
   );
   for(k=1,3,gclass[k,i]=lift(Mod(gclass[k,i]+e*vv[k],3)));ff[i]=lift(Mod(ff[i]+e*vv[4],3));
   listput(factorrecords,[i,p,P[4],e,vv]);
  );
  check(sum(k=1,3,gclass[k,i])%3==0,"actual genus phase sum");
 );
 check(matrank(Mod(gclass,3))==2,"actual class generators span complete S-class");
 my(Rc=matrix(6,3),Sc=matrix(3,6),Rs=matrix(6,6),cgens=vector(3),sgens=vector(6));
 for(i=1,3,
  my(I=idealpow(B,G[i],B.cyc[i]),pr=bnfisprincipal(B,I,5));
  check(pr[1]==Col(vector(3)),"literal class power relation");
  cgens[i]=pr[2];check(factoredidealcheck(B,cgens[i],I),"actual class-power ideal equality");
  Rc[,i]=Col(factoredchars(B,alpha,xi,beta,Q,T,lab,a0,cgens[i]));
 );
 for(v=1,6,
  my(cc=bnfisprincipal(B,S[v],0),I=idealdiv(B,S[v],idealfactorback(B,G,cc)));
  Sc[,v]=cc;
  my(pp=bnfisprincipal(B,I,5));check(pp[1]==Col(vector(3)),"literal S-prime class relation");
  sgens[v]=pp[2];check(factoredidealcheck(B,sgens[v],I),"actual S-prime ideal equality");
  Rs[,v]=-Col(factoredchars(B,alpha,xi,beta,Q,T,lab,a0,sgens[v]));
 );
 my(Rel=concat(concat(concat(matconcat([3*matid(6);matrix(3,6)]),matconcat([C[,1..9];matrix(3,9)])),matconcat([Rc;matdiagonal(B.cyc)])),matconcat([Rs;Sc])));
 my(H=mathnf(Rel),SN=matsnf(H,1),row=concat(vector(6,j,1),ff));
 check(matsize(H)==[9,9] && abs(matdet(H))==729,"exact next genus order729");
 check(lift(Mod(row*Rel,3))==vector(matsize(Rel)[2]),"actual field restriction annihilates every relation");
 check(SN[1]*H*SN[2]==SN[3],"genus Smith maps");
 my(K=matid(9));K[1,1]=3;for(j=2,9,K[1,j]=-row[j]);
 my(KR=K^-1*H,KS=matsnf(KR,1));check(denominator(KR)==1,"actual field kernel lattice");
 check(KS[1]*KR*KS[2]==KS[3] && abs(matdet(KR))==243,"norm-coinvariant Smith inverse");
 my(N0=matconcat([matrix(2,6),gclass[1..2,]]),NK=N0*K*KS[1]^-1);
 print("{\"type\":\"ordinary_class_actual_generation\",\"orders\":",B.cyc,",\"original_generator_ideals\":",vector(3,i,jmat(B.gen[i])),",\"moved_generator_corrections\":",vector(3,i,cf(corr[i],18)),",\"genus_coordinates\":",jmat(gclass),",\"Frobenius_beta\":",ff,",\"S_prime_coordinates\":",jmat(Sc),",\"factor_records\":",Vec(factorrecords),"}");
 print("{\"type\":\"next_genus_presentation\",\"relation_matrix\":",jmat(Rel),",\"relation_HNF\":",jmat(H),",\"smith_left\":",jmat(SN[1]),",\"smith_right\":",jmat(SN[2]),",\"smith_diagonal\":",jmat(SN[3]),",\"restriction_row\":",row,",\"kernel_lattice\":",jmat(K),",\"kernel_relation_matrix\":",jmat(KR),",\"kernel_smith_left\":",jmat(KS[1]),",\"kernel_smith_right\":",jmat(KS[2]),",\"kernel_smith_diagonal\":",jmat(KS[3]),",\"actual_norm_matrix\":",jmat(NK),"}");
 writebin("e53_genus_transition.bin",[D,Gd,G,corr,gclass,ff,Sc,Rc,Rs,cgens,sgens,Rel,H,SN,K,KR,KS,NK]);
 print("{\"type\":\"completion\",\"status\":\"PASS\"}");
}
quit;
