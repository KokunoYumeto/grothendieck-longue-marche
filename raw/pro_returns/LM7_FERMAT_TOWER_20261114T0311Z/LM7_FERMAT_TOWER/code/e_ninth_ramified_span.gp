default(parisize,256000000);
default(parisizemax,2000000000);
default(realprecision,100);
run()={
  my(dat=read("research_norm_index/code/cyclotomic_base1_bnf.bin"),B=dat[1],F=B.nf,xi=dat[2],beta=dat[3]*xi,PS=concat(idealprimedec(F,3),idealprimedec(F,17)));
  my(gd=read("research_norm_index/code/cyclotomic_base1_ninth_genus.bin"),Ray=gd[1],fac=gd[2],U=gd[5],D=gd[7],ds=vector(#Ray.cyc,i,D[i,i]),C=matrix(#Ray.cyc,6),records=List());
  for(j=1,6,
    my(f2=fac,vals=vector(6,i,1));f2[j,2]++;vals[j]=if(j<=3,beta+1,beta);
    my(z=idealchinese(F,f2,vals),I=idealdiv(F,z,PS[j]),cl=-bnrisprincipal(Ray,I,0));
    for(i=1,6,if(idealval(F,I,PS[i])!=0,error("local Artin prime coprimality")));
    C[,j]=U*cl;listput(records,[z,I,cl]);
  );
  my(H=mathnf(concat(D,C)),SM=matsnf(H,1),ord=abs(matdet(D)/matdet(H)),amb=9*9^6/(9*gd[14]));
  if(SM[1]*H*SM[2]!=SM[3] || denominator(SM[1]^-1)!=1 || denominator(SM[2]^-1)!=1,error("exact Smith maps"));
  my(P=idealhnf(F,73,x-33),target=9*U*bnrisprincipal(Ray,P,0));
  print("NINTH_RAMIFIED_ARTIN ",matrix(#ds,6,i,j,lift(Mod(C[i,j],ds[i]))));
  print("NINTH_RAMIFIED_IMAGE_ORDER ",ord," AMBIGUOUS_ORDER ",amb," KERNEL_ORDER_BOUND ",amb/ord);
  print("NINTH_RAMIFIED_IMAGE_HNF ",H," SMITH ",SM," LEFT_INVERSE ",SM[1]^-1," RIGHT_INVERSE ",SM[2]^-1);
  print("NINTH_EXTENDED_PRIME73 ",vector(#ds,i,lift(Mod(target[i],ds[i])))~);
  writebin("research_e84/code/e_ninth_ramified_span.bin",[Ray,fac,U,D,C,H,SM,ord,amb,target,Vec(records)]);
  print("DONE: all six ninth-layer ramified Artin columns and exact image index.");
};
run();
quit;
