default(parisize,256000000);
default(parisizemax,2000000000);
default(realprecision,100);
run()={
  my(dat=read("research_e81/code/e_prime73_field.bin"),F=dat[2],P=dat[5],ps=dat[7],beta=dat[11],pi=beta+1);
  my(rd=read("research_norm_index/code/cyclotomic_base1_genus.bin"),Ray=rd[1],fac=rd[2],U=rd[5],D=rd[7],ds=vector(#Ray.cyc,i,D[i,i]),C=matrix(#Ray.cyc,6));
  my(artin_ideals=List());
  for(j=1,6,
    my(f2=fac,vals=vector(6,i,1));f2[j,2]++;vals[j]=if(j<=3,pi,beta);
    my(x=idealchinese(F,f2,vals),I=idealdiv(F,x,ps[j]),cl=-bnrisprincipal(Ray,I,0));
    for(i=1,6,if(idealval(F,I,ps[i])!=0,error("Artin ideal coprimality")));
    C[,j]=U*cl;listput(artin_ideals,[x,I,cl]);
  );
  my(target=3*U*bnrisprincipal(Ray,P,0),p=[0,0,0,-1,1,0]~,sol=matsolvemod(C,ds~,0,1),K=mathnf(sol[2]),rel=read("research_e81/code/e_prime73_relations.bin"),H=rel[4]);
  for(i=1,#ds,if((target+C*p)[i]%ds[i],error("actual affine origin")));
  if(denominator(K^-1*H)!=1 || abs(matdet(K))!=27,error("complete genus correction lattice"));
  my(Q=K^-1*H,SM=matsnf(Q,1),Cimage=mathnf(concat(D,C)),SI=matsnf(Cimage,1));
  if(SM[1]*Q*SM[2]!=SM[3] || abs(matdet(Q))!=27 || abs(matdet(D)/matdet(Cimage))!=27,error("exact correction and image sizes"));
  print("GENUS_CYCLIC ",ds);
  print("S_PRIME_ARTIN ",matrix(#ds,6,i,j,lift(Mod(C[i,j],ds[i]))));
  print("EXTENDED_PRIME_ARTIN ",vector(#ds,i,lift(Mod(target[i],ds[i])))~);
  print("CORRECTION_ORIGIN ",p," KERNEL ",K," INVERSE ",K^-1," QUOTIENT_MATRIX ",Q," QUOTIENT_SMITH ",SM);
  writebin("research_e81/code/e_prime73_artin.bin",[Ray,fac,U,D,ds,C,target,p,K,Q,SM,Cimage,SI,Vec(artin_ideals)]);
  print("DONE: exact ordinary noncapitulation and all affine S-correction coordinates.");
};
run();
quit;
