\\ Exact first positional genus quotient, with its actual norm and transfer.
default(parisize,128000000);default(parisizemax,1000000000);
check(a,s)=if(!a,error(s));
jmat(M)=vector(matsize(M)[1],i,Vec(M[i,]));
lc(L,beta,z,Q,T,u)={
 my(v=idealval(L,u,Q),nu=nfeltnorm(L,u)/2757^v,pr=nfmodprinit(L,T,'t),rr=nfmodpr(L,u/beta^idealval(L,u,T),pr)^((53^2-1)/3),zz=nfmodpr(L,z,pr));
 check(valuation(nu,3)==0 && valuation(nu-1,3)>=2,"literal wild norm quotient");
 [lift(Mod(-(nu-1)/9,3)),if(rr==1,0,if(rr==zz,2,if(rr==zz^2,1,error("tame phase"))))];
};
{
 my(D=read("e53_horizontal_base.bin"),L=D[4],S=D[5],beta=Mod(x,L.pol),z=beta^3/53,US=bnfunits(L,S),U=vector(#US[1],i,nfbasistoalg(L,nffactorback(L,US[1][i]))),C=matrix(2,#U));
 for(i=1,#U,C[,i]=Col(lc(L,beta,z,S[1],S[2],U[i])));
 check(C==matrix(2,#U),"every actual positional S-unit is a field norm");
 my(G=vector(2),corr=vector(2));
 for(i=1,2,
  corr[i]=nfbasistoalg(L,idealappr(L,matrix(2,2,r,c,if(c==1,S[r],idealval(L,L.gen[i],S[r])))));
  G[i]=idealdiv(L,L.gen[i],corr[i]);check(vector(2,j,idealval(L,G[i],S[j]))==vector(2),"outside-S generators");
 );
 my(ff=vector(2),records=List());
 for(i=1,2,
  my(Fac=idealfactor(L,G[i]));
  for(j=1,matsize(Fac)[1],
   my(P=Fac[j,1],p=P[1],e=Fac[j,2],pr=nfmodprinit(L,P,'t),rr=nfmodpr(L,beta,pr)^((p^P[4]-1)/3),zz=nfmodpr(L,z,pr),f=if(rr==1,0,if(rr==zz,1,if(rr==zz^2,2,error("Frobenius phase")))));
   check(p!=3 && p!=53 && isprime(p),"certified outside-S prime");
   ff[i]=lift(Mod(ff[i]+e*f,3));listput(records,[i,p,P[4],e,f]);
  );
 );
 my(Rc=matrix(2,2),Sc=matrix(2,2),Rs=matrix(2,2),cg=vector(2),sg=vector(2));
 for(i=1,2,
  my(I=idealpow(L,G[i],L.cyc[i]),pr=bnfisprincipal(L,I,3));check(pr[1]==[0,0]~,"actual class relation");cg[i]=nfbasistoalg(L,pr[2]);check(idealhnf(L,cg[i])==idealhnf(L,I),"literal class divisor");Rc[,i]=Col(lc(L,beta,z,S[1],S[2],cg[i]));
 );
 for(i=1,2,
  Sc[,i]=bnfisprincipal(L,S[i],0);my(I=idealdiv(L,S[i],idealfactorback(L,G,Sc[,i])),pr=bnfisprincipal(L,I,3));check(pr[1]==[0,0]~,"actual S-prime relation");sg[i]=nfbasistoalg(L,pr[2]);check(idealhnf(L,sg[i])==idealhnf(L,I),"literal S-prime divisor");Rs[,i]=-Col(lc(L,beta,z,S[1],S[2],sg[i]));
 );
 my(Rel=concat(concat(matconcat([3*matid(2);matrix(2,2)]),matconcat([Rc;matdiagonal(L.cyc)])),matconcat([Rs;Sc])),H=mathnf(Rel),SN=matsnf(H,1),row=concat([1,1],ff));
 check(abs(matdet(H))==81 && lift(Mod(row*Rel,3))==vector(6),"exact positional genus order and restriction");
 my(K=matid(4));K[1,1]=3;for(i=2,4,K[1,i]=-row[i]);my(KR=K^-1*H,KS=matsnf(KR,1));check(denominator(KR)==1 && abs(matdet(KR))==27,"exact positional norm-coinvariant kernel");
 check(SN[1]*H*SN[2]==SN[3] && KS[1]*KR*KS[2]==KS[3],"both exact Smith inverses");
 my(N0=matconcat([matrix(2,2),matid(2)]),NK=N0*K*KS[1]^-1,J=KS[1]*K^-1*matconcat([matrix(2,2);3*matid(2)]));
 print("{\"type\":\"positional_genus_transition\",\"complete_S_unit_characters\":",jmat(C),",\"class_relations_characters\":",jmat(Rc),",\"S_prime_coordinates\":",jmat(Sc),",\"S_prime_relations_characters\":",jmat(Rs),",\"Frobenius_records\":",Vec(records),",\"relation_matrix\":",jmat(Rel),",\"relation_HNF\":",jmat(H),",\"smith_left\":",jmat(SN[1]),",\"smith_right\":",jmat(SN[2]),",\"smith_diagonal\":",jmat(SN[3]),",\"restriction_row\":",row,",\"kernel_lattice\":",jmat(K),",\"kernel_relation_matrix\":",jmat(KR),",\"kernel_smith_left\":",jmat(KS[1]),",\"kernel_smith_right\":",jmat(KS[2]),",\"kernel_smith_diagonal\":",jmat(KS[3]),",\"norm_matrix\":",jmat(NK),",\"extension_matrix_to_coinvariants\":",jmat(J),"}");
 writebin("e53_positional_genus_transition.bin",[D,G,corr,ff,cg,sg,Rel,H,SN,K,KR,KS,NK,J]);
 print("{\"type\":\"completion\",\"status\":\"PASS\"}");
}
quit;
