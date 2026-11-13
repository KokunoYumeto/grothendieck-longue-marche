default(parisize,256000000);
default(parisizemax,2000000000);
default(realprecision,100);

run()={
  my(base=read("research_norm_index/code/cyclotomic_base1_bnf.bin"),B=base[1],F=B.nf,beta=base[2]*base[3],pi=beta+1);
  my(dat=read("research_norm_index/code/cyclotomic_base1_genus.bin"),Ray=dat[1],fac=dat[2],U=dat[5],D=dat[7],ds=vector(#Ray.cyc,i,D[i,i]));
  my(co=read("research_norm_index/code/cyclotomic_sclass_coordinates.bin"),P=co[2][1][4],ps=concat(idealprimedec(F,3),idealprimedec(F,17)),C=matrix(#Ray.cyc,6));
  for(j=1,6,
    my(f2=fac,vals=vector(6,i,1));f2[j,2]++;vals[j]=if(j<=3,pi,beta);
    my(x=idealchinese(F,f2,vals),I=idealdiv(F,x,ps[j]),cl=-bnrisprincipal(Ray,I,0));
    for(i=1,6,if(idealval(F,I,ps[i])!=0,error("prime Artin ideal coprimality")));
    C[,j]=U*cl;
  );
  my(target=3*U*bnrisprincipal(Ray,P,0),sol=matsolvemod(C,ds~,-target,1),K=mathnf(sol[2]),p=sol[1]);
  if(!sol,error("E79 norm-isomorphism compatibility"));
  my(srel=read("research_e81/code/e_prime73_srelation_lattice.bin"),H=srel[2],SM=srel[3],Ui=srel[4],orders=vector(6,i,SM[3][i,i]),total=prod(i=1,6,orders[i]),allowed=List());
  if(denominator(K^-1*H)!=1,error("known principal relations are in genus kernel"));
  for(j=1,6,for(i=1,#ds,if((C*H)[i,j]%ds[i],error("literal relation map"))));
  for(k=0,total-1,
    my(z=vector(6),rem=k);
    for(j=1,6,z[j]=rem%orders[j];rem=rem\orders[j];if(2*z[j]>orders[j],z[j]-=orders[j]));
    my(v=Ui*z~,good=1,im=target+C*v);
    for(j=1,#ds,if(im[j]%ds[j],good=0));
    if(good,listput(allowed,v));
  );
  if(#allowed!=abs(matdet(H)/matdet(K)),error("complete affine fiber size"));
  print("GENUS_CYCLIC ",ds);
  print("UPPER_S_PRIME_ARTIN_MAP ",matrix(#ds,6,i,j,lift(Mod(C[i,j],ds[i]))));
  print("EXTENDED_PRIME73_ARTIN ",vector(#ds,i,lift(Mod(target[i],ds[i])))~);
  print("EXACT_AFFINE_S_CORRECTION p+K*Z6 ",p," K ",K," INVERSE ",K^-1);
  print("ALLOWED_S_CLASSES ",#allowed," OF ",total," VECTORS ",Vec(allowed));
  writebin("research_e81/code/e_prime73_genus_filter.bin",[ds,C,target,p,K,Vec(allowed),srel]);
  print("DONE: exact necessary genus condition, with actual Artin maps and every inverse lattice coordinate.");
};
run();
quit;
