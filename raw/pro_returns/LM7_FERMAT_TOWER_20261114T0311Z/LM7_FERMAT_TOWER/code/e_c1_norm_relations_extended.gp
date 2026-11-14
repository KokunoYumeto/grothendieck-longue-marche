default(parisize,256000000);
default(parisizemax,2000000000);
default(realprecision,100);
setrand(841733);
run()={
  my(dat=read("research_e81/code/e_prime73_field.bin"),B=dat[1],F=dat[2],R=dat[3],E=dat[4],xi=dat[10],beta=dat[11],zeta=xi^3,target=xi*(beta+1+3*zeta));
  my(roots=vector(18,i,(-xi)^i),mon=vector(6,j,beta^((j-1)\3)),records=List(),seen=Map(),smooth=Map(),plist=List(),pmap=Map(),tested=0);
  my(tf=idealfactor(F,target));
  for(j=1,matsize(tf)[1],my(pr=tf[j,1],key=idealhnf(F,pr));if(!mapisdefined(pmap,key),listput(plist,pr);mapput(pmap,key,#plist)));
  for(i=1,5,for(j=i+1,5,for(k=j+1,5,
    for(a=1,18,for(b=1,18,for(c=1,18,
      my(v=[Mod(1,F.pol),Mod(0,F.pol),Mod(0,F.pol)]);
      v[1+i%3]+=roots[a]*mon[i+1];v[1+j%3]+=roots[b]*mon[j+1];v[1+k%3]+=roots[c]*mon[k+1];
      my(nm=v[1]^3+beta*v[2]^3+beta^2*v[3]^3-3*beta*v[1]*v[2]*v[3]);
      tested++;
      if(!nm || mapisdefined(seen,nm),next);mapput(seen,nm,1);
      my(nn=abs(nfeltnorm(F,nm)),good);
      if(!mapisdefined(smooth,nn,&good),my(fac=factor(nn,331));good=(matsize(fac)[1]==0 || fac[matsize(fac)[1],1]<=331);mapput(smooth,nn,good));
      if(!good,next);
      my(fa=idealfactor(F,nm));
      for(jj=1,matsize(fa)[1],my(pr=fa[jj,1],key=idealhnf(F,pr));if(!mapisdefined(pmap,key),listput(plist,pr);mapput(pmap,key,#plist)));
      listput(records,[v,nm,fa,[i,j,k,a,b,c]]);
    )));
    print("POOL_PROGRESS ",[i,j,k]," FORMS ",tested," SMOOTH_NORMS ",#records," SUPPORT ",#plist);
  )));
  print("NORM_POOL FORMS ",tested," DISTINCT_NORMS ",#seen," SMOOTH_NORMS ",#records," SUPPORT_PRIMES ",#plist);
  my(old=read("research_e84/code/e_c1_norm_relations.bin"));
  for(k=1,#old[8],my(rec=old[8][k]);if(!mapisdefined(seen,rec[2]),
    mapput(seen,rec[2],1);listput(records,rec);
    for(j=1,matsize(rec[3])[1],my(pr=rec[3][j,1],key=idealhnf(F,pr));if(!mapisdefined(pmap,key),listput(plist,pr);mapput(pmap,key,#plist)))
  ));
  my(S=Vec(plist),US=bnfunits(B,S),dim=#US[1],M=matrix(dim,#records));
  for(k=1,#records,my(cl=bnfisunit(B,records[k][2],US));if(#cl!=dim,error("S-unit coordinates"));M[,k]=cl);
  my(t=bnfisunit(B,target,US));if(#t!=dim,error("target S-unit coordinates"));
  my(sol=matsolvemod(M,3,t));
  print("NORM_SPAN DIMENSION ",dim," RANK ",matrank(Mod(M,3))," AUGMENTED_RANK ",matrank(Mod(concat(M,t),3)));
  writebin("research_e84/code/e_c1_norm_relations_extended.bin",[B,F,R,E,xi,beta,target,Vec(records),S,US,M,t,sol]);
  if(type(sol)!="t_COL",print("NO_FIELD_NORM_RELATION_IN_THIS_POOL");print("DONE: exact bounded norm-span test; no global non-norm inference.");return(0));
  sol=apply(x->if(x==2,-1,x),sol);
  my(corr=(t-M*sol)/3);
  if(denominator(corr)!=1,error("integral cube-root correction"));
  my(active=select(i->sol[i]!=0,vector(#records,i,i)),coractive=select(i->corr[i]!=0,vector(dim,i,i)),N=Mod(1,F.pol),root=Mod(1,F.pol));
  for(j=1,#active,my(i=active[j]);N*=records[i][2]^sol[i]);
  for(j=1,#coractive,my(i=coractive[j],u=nffactorback(F,US[1][i]));root*=nfbasistoalg(F,u)^corr[i]);
  if(N*root^3!=target,error("literal norm relation"));
  print("NORM_RELATION ACTIVE ",active," EXPONENTS ",vector(#active,j,sol[active[j]])," CUBE_CORRECTION ",corr);
  print("NORM_RELATION ROOT ",lift(root));
  print("NORM_RELATION FORMS ",vector(#active,j,[records[active[j]][4],records[active[j]][1]]));
  writebin("research_e84/code/e_c1_field_norm_witness.bin",[Vec(records),S,US,M,t,sol,corr,root,active]);
  print("DONE: exact field norm preimage as a product of explicit cubic forms and included base correction.");
};
run();
quit;
