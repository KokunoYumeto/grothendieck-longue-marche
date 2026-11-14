\\ Exact higher local characters of the verified cubic-root S-units.
default(parisize,256000000);default(parisizemax,2000000000);
check(a,s)=if(!a,error(s));
jmat(M)=vector(matsize(M)[1],i,Vec(M[i,]));
E122RootPrecMin=1000000;
localnine(D,LD,u)={
 my(B=D[1],alpha=D[2],xi=D[3],beta=D[4],Q=D[5],T=D[6],lab=D[8],F=LD[1],bid=LD[5],aa=LD[6],py=F.pol,v=vector(6));
 my(coeff=Vec(lift(u)),cm=vecmin(vector(#coeff,i,valuation(coeff[i],3))));
 for(j=0,2,
  my(vv=idealval(B,u,Q[lab[j+1]]),pr=min(6*(valuation(aa^3-53,3)-1)+6*cm-vv,6*(valuation(aa^3-53,3)-1)-1));
  check(pr>=16,"proved relative p-adic precision after normalization");E122RootPrecMin=min(E122RootPrecMin,pr);
  my(loc=Mod(y-aa*y^(3*j),py),uu=subst(lift(u),x,loc)/(1+aa*Mod(y,py)^(1+3*j))^vv);
  check(idealval(F,uu,LD[4])==0,"normalized local unit");
  v[j+1]=lift(Mod(LD[8][j+1][5]*ideallog(F,uu,bid),9));
 );
 for(j=1,3,
  my(pr=nfmodprinit(B,T[j],'t),xr=nfmodpr(B,xi,pr),vv=idealval(B,u,T[j]),rr=nfmodpr(B,u/beta^vv,pr)^((53^2-1)/9),e=-1);
  for(k=0,8,if(rr==xr^k,e=k));check(e>=0,"literal ninth tame phase");v[j+3]=lift(Mod(-e,9));
 );v;
};
{
 my(D=read("../inputs/e119_e53_genus_transition.bin")[1],LD=read("e53_higher_local.bin"),Stream=read("e53_upper_exact_roots.bin"));
 check(#Stream==22,"all twenty-two append-only exact-root checkpoints");
 my(R=Stream[#Stream],V=R[8],C=matrix(6,#V));
 check(#R==8 && #V==22 && vecsum(R[6])==22,"complete final root checkpoint");
 for(i=1,#V,
  my(u=Mod(sum(j=1,18,V[i][2][j]*x^(j-1)),D[1].pol),ch=localnine(D,LD,u));
  check(lift(Mod(ch,3))==vector(6),"verified upper-root norm in cubic field-norm kernel");
  C[,i]=Col(ch/3);
 );
 my(ALL=concat(D[10],C));
 check(lift(Mod(vector(6,i,1)*ALL,3))==vector(matsize(ALL)[2]),"actual upper-root product formula");
 print("{\"type\":\"verified_root_upper_characters\",\"root_indices\":",vector(#V,i,V[i][1]),",\"root_character_matrix\":",jmat(C),",\"with_included_lower_characters\":",jmat(ALL),",\"rank_mod3\":",matrank(Mod(ALL,3)),",\"minimum_proved_precision\":",E122RootPrecMin,"}");
 writebin("e53_upper_root_characters.bin",[C,ALL]);
 print("{\"type\":\"completion\",\"status\":\"PASS\"}");
}
quit;
