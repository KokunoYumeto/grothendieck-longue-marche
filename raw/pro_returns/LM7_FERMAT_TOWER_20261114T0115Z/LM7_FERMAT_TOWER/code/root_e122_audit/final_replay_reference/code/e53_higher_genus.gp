\\ Actual cyclic-nine B3/B1 genus, using the exact local norm subgroups.
default(parisize,256000000);default(parisizemax,2000000000);
check(a,s)=if(!a,error(s));
jmat(M)=vector(matsize(M)[1],i,Vec(M[i,]));
cf(a,n)=vector(n,i,Str(polcoef(lift(a),i-1)));
E122PrecMin=1000000;
localnine(D,LD,u)={
 my(B=D[1],alpha=D[2],xi=D[3],beta=D[4],Q=D[5],T=D[6],lab=D[8],F=LD[1],bid=LD[5],aa=LD[6],py=F.pol,v=vector(6));
 my(coeff=Vec(lift(u)),cm=vecmin(vector(#coeff,i,valuation(coeff[i],3))));
 for(j=0,2,
  my(vv=idealval(B,u,Q[lab[j+1]]),pr=min(6*(valuation(aa^3-53,3)-1)+6*cm-vv,6*(valuation(aa^3-53,3)-1)-1));
  check(pr>=16,"proved relative p-adic precision after normalization");E122PrecMin=min(E122PrecMin,pr);
  my(loc=Mod(y-aa*y^(3*j),py),uu=subst(lift(u),x,loc)/(1+aa*Mod(y,py)^(1+3*j))^vv);
  check(idealval(F,uu,LD[4])==0,"normalized local unit");
  v[j+1]=lift(Mod(LD[8][j+1][5]*ideallog(F,uu,bid),9));
 );
 for(j=1,3,
  my(pr=nfmodprinit(B,T[j],'t),xr=nfmodpr(B,xi,pr),vv=idealval(B,u,T[j]),rr=nfmodpr(B,u/beta^vv,pr)^((53^2-1)/9),e=-1);
  for(k=0,8,if(rr==xr^k,e=k));check(e>=0,"literal ninth tame phase");v[j+3]=lift(Mod(-e,9));
 );v;
};
factorchars(D,LD,f)={
 my(v=vector(6));for(k=1,matsize(f)[1],v+=f[k,2]*localnine(D,LD,nfbasistoalg(D[1],f[k,1])));lift(Mod(v,9));
};
{
 my(E=read("../inputs/e119_e53_genus_transition.bin"),D=E[1],B=D[1],xi=D[3],beta=D[4],U=D[7],G=E[3],LD=read("e53_higher_local.bin"));
 my(C=matrix(6,#U));for(i=1,#U,C[,i]=Col(localnine(D,LD,U[i])));
 check(lift(Mod(C,3))==D[10],"exact restriction to prior cubic characters");
 check(lift(Mod(vector(6,i,1)*C,9))==vector(#U),"global ninth product formula on every complete S-unit generator");
 my(IH=mathnf(concat(9*matid(6),C)),IS=matsnf(IH,1));
 print("{\"type\":\"higher_complete_S_unit_characters\",\"matrix\":",jmat(C),",\"local_inertia_HNF\":",jmat(IH),",\"local_inertia_Smith\":",Vec(matsnf(IH)),",\"minimum_proved_precision\":",E122PrecMin,"}");
 my(ff=vector(3),factors=List());
 for(i=1,3,
  my(Fac=idealfactor(B,G[i]));
  for(j=1,matsize(Fac)[1],
   my(P=Fac[j,1],e=Fac[j,2],p=P[1],qq=p^P[4],pr=nfmodprinit(B,P,'t),xr=nfmodpr(B,xi,pr),rr=nfmodpr(B,beta,pr)^((qq-1)/9),v=-1);
   check(p!=3 && p!=53 && isprime(p),"proved outside-S prime");
   for(k=0,8,if(rr==xr^k,v=k));check(v>=0,"positive Frobenius on ninth radical");
   ff[i]=lift(Mod(ff[i]+e*v,9));listput(factors,[i,p,P[4],e,v]);
  );
 );
 my(Rc=matrix(6,3),Rs=matrix(6,6));
 for(i=1,3,Rc[,i]=Col(factorchars(D,LD,E[10][i])));
 for(i=1,6,Rs[,i]=-Col(factorchars(D,LD,E[11][i])));
 my(Rel=concat(concat(concat(matconcat([9*matid(6);matrix(3,6)]),matconcat([C[,1..9];matrix(3,9)])),matconcat([Rc;matdiagonal(B.cyc)])),matconcat([Rs;E[7]])));
 my(H=mathnf(Rel),SN=matsnf(H,1),rho=concat(vector(6,i,1),ff));
 check(lift(Mod(rho*Rel,9))==vector(matsize(Rel)[2]),"actual restriction kills all principal/class relations");
 my(K=matid(9));K[1,1]=9;for(i=2,9,K[1,i]=-rho[i]);
 my(KR=K^-1*H,KS=matsnf(KR,1));
 check(denominator(KR)==1 && SN[1]*H*SN[2]==SN[3] && KS[1]*KR*KS[2]==KS[3],"full exact Smith identities");
 print("{\"type\":\"B3_over_B1_genus\",\"relation_matrix\":",jmat(Rel),",\"relation_HNF\":",jmat(H),",\"smith_left\":",jmat(SN[1]),",\"smith_right\":",jmat(SN[2]),",\"smith_diagonal\":",Vec(matsnf(H)),",\"restriction_row\":",rho,",\"kernel_lattice\":",jmat(K),",\"kernel_relations\":",jmat(KR),",\"kernel_smith_left\":",jmat(KS[1]),",\"kernel_smith_right\":",jmat(KS[2]),",\"kernel_smith_diagonal\":",Vec(matsnf(KR)),",\"Frobenius_factors\":",Vec(factors),",\"minimum_proved_precision\":",E122PrecMin,"}");
 writebin("e53_higher_genus.bin",[E,LD,C,IH,IS,ff,Rc,Rs,Rel,H,SN,rho,K,KR,KS]);
 print("{\"type\":\"completion\",\"status\":\"PASS\"}");
}
quit;
