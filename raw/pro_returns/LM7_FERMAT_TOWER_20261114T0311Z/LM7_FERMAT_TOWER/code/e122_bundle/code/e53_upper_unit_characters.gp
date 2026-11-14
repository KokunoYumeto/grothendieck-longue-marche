\\ Actual included smaller-field S-units and their three conjugates.
\\ No class/unit completeness is inferred from candidate BNF data.
default(parisize,256000000);default(parisizemax,2000000000);
check(a,s)=if(!a,error(s));
jmat(M)=vector(matsize(M)[1],i,Vec(M[i,]));
cf(a,n)=vector(n,i,Str(polcoef(lift(a),i-1)));
E122UnitPrecMin=1000000;
localnine(D,LD,u)={
 my(B=D[1],alpha=D[2],xi=D[3],beta=D[4],Q=D[5],T=D[6],lab=D[8],F=LD[1],bid=LD[5],aa=LD[6],py=F.pol,v=vector(6));
 my(coeff=Vec(lift(u)),cm=vecmin(vector(#coeff,i,valuation(coeff[i],3))));
 for(j=0,2,
  my(vv=idealval(B,u,Q[lab[j+1]]),pr=min(6*(valuation(aa^3-53,3)-1)+6*cm-vv,6*(valuation(aa^3-53,3)-1)-1));
  check(pr>=16,"proved relative p-adic precision after normalization");E122UnitPrecMin=min(E122UnitPrecMin,pr);
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
 my(E=read("../inputs/e119_e53_genus_transition.bin"),D=E[1],B=D[1],alpha=D[2],xi=D[3],beta=D[4],LD=read("e53_higher_local.bin"),W=read("e53_upper_unit_candidates.bin"),U=W[4],C=matrix(6,3*#U),NN=vector(3*#U),recs=List());
 for(i=1,#U,
  my(ff=subst(lift(U[i]),x,'w),nr=polresultant(w^3-beta,ff,'w));
  check(nfeltnorm(B,nr)==nfeltnorm(W[1],U[i])^3,"exact tower absolute norm");
  for(j=0,2,
   my(v=nfgaloisapply(B,xi-xi^(3*j)*alpha,nr),ch=localnine(D,LD,v));
   check(lift(Mod(ch,3))==vector(6),"actual field norm lies in cubic kernel");
   C[,3*(i-1)+j+1]=Col(ch/3);NN[3*(i-1)+j+1]=v;
   listput(recs,[i,j,cf(v,18),ch]);
  );
 );
 my(ALL=concat(D[10],C));
 check(lift(Mod(vector(6,i,1)*ALL,3))==vector(matsize(ALL)[2]),"full actual product formula");
 print("{\"type\":\"literal_candidate_upper_characters\",\"records\":",Vec(recs),",\"candidate_character_matrix\":",jmat(C),",\"with_included_lower_characters\":",jmat(ALL),",\"rank_mod3\":",matrank(Mod(ALL,3)),",\"minimum_proved_precision\":",E122UnitPrecMin,"}");
 writebin("e53_upper_unit_characters.bin",[W,NN,C,ALL]);
 print("{\"type\":\"completion\",\"status\":\"PASS\"}");
}
quit;
