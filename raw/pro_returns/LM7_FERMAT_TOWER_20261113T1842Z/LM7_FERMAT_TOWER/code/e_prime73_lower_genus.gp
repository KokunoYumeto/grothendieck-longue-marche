default(parisize,256000000);
default(parisizemax,2000000000);
default(realprecision,100);
setrand(817333);
run()={
  my(F=nfinit(x^6+17*x^3+289),B=bnfinit(F,1),beta=Mod(x,F.pol),pi=beta+1);
  if(bnfcertify(B)!=1 || B.cyc!=[3,3],error("certified degree6 base only"));
  my(ps=[idealprimedec(F,3)[1],idealprimedec(F,17)[1]],bid=idealstar(F,idealpow(F,ps[1],10),2,3));
  my(v0=Mod(1,F.pol),v1=Mod(0,F.pol),v2=Mod(0,F.pol),norms=List());
  for(k=1,40,
    my(w0=v0+beta*v2,w1=v0+v1,w2=v1+v2);v0=w0;v1=w1;v2=w2;
    my(u0=v0+1,N=u0^3+beta*v1^3+beta^2*v2^3-3*beta*u0*v1*v2);
    if(idealval(F,N,ps[1])!=0,error("exact local norm unit"));listput(norms,nfalgtobasis(F,N));
  );
  my(M=Mat(vector(#norms,k,ideallog(F,norms[k],bid))),H=matker(Mod(M~,3)));
  if(#bid.cyc!=7 || matrank(Mod(M,3))!=6 || matsize(H)!=[7,1],error("full local norm character"));
  my(fac=matrix(2,2,i,j,if(j==1,ps[i],if(i==1,10,1))),crt=idealchinese(F,fac),Ray=bnrinit(B,fac,0,9),rels=List());
  for(j=1,2,
    my(bb=idealstar(F,idealpow(F,ps[j],fac[j,2]),2));
    for(k=1,#bb.gen,
      my(vals=[1,1]);vals[j]=nfeltpow(F,bb.gen[k],3);
      listput(rels,bnrisprincipal(Ray,idealchinese(F,crt,vals),0));
    );
    if(j==1,
      my(indices=matindexrank(Mod(M,3))[2]);
      for(k=1,#indices,my(vals=[norms[indices[k]],1]);listput(rels,bnrisprincipal(Ray,idealchinese(F,crt,vals),0)));
    );
  );
  my(pres=concat(matdiagonal(Ray.cyc),Mat(Vec(rels))),K=mathnf(pres),SM=matsnf(K,1),U=SM[1],D=SM[3],ds=vector(#Ray.cyc,i,D[i,i]));
  if(prod(i=1,#ds,ds[i])!=81 || U*K*SM[2]!=D,error("exact lower genus order"));
  my(P=idealhnf(F,73,x-22));
  if(idealnorm(F,P)!=73,error("actual contracted prime"));
  my(C=matrix(#ds,2));
  for(j=1,2,
    my(f2=fac,vals=[1,1]);f2[j,2]++;vals[j]=if(j==1,pi,beta);
    my(a=idealchinese(F,f2,vals),I=idealdiv(F,a,ps[j]));
    for(i=1,2,if(idealval(F,I,ps[i])!=0,error("Artin ideal coprimality")));
    C[,j]=-U*bnrisprincipal(Ray,I,0);
  );
  my(target=3*U*bnrisprincipal(Ray,P,0));
  print("LOWER_BASE_PRIME_CLASS ",bnfisprincipal(B,P,0));
  print("LOWER_GENUS_SMITH ",ds," HNF ",K," LEFT ",U," RIGHT ",SM[2]," LEFT_INVERSE ",U^-1," RIGHT_INVERSE ",SM[2]^-1);
  print("LOWER_RAMIFIED_PRIME_ARTIN ",matrix(#ds,2,i,j,lift(Mod(C[i,j],ds[i]))));
  print("LOWER_EXTENDED_PRIME73_ARTIN ",vector(#ds,i,lift(Mod(target[i],ds[i])))~);
  writebin("research_e81/code/e_prime73_lower_genus.bin",[B,Ray,pres,K,SM,ds,C,P,target]);
  print("DONE: actual lower prime norm and exact lower genus Artin image.");
};
run();
quit;
