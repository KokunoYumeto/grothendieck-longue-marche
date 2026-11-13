default(parisize,256000000);
default(parisizemax,2000000000);
default(realprecision,100);
run()={
  my(dat=read("research_norm_index/code/cyclotomic_base1_bnf.bin"),B=dat[1],F=B.nf,z9=dat[2],a=dat[3],beta=a*z9,pi=beta+1);
  my(local=read("research_norm_index/code/cyclotomic_base1_local_norms.bin"),norms=local[4]);
  my(ps=concat(idealprimedec(F,3),idealprimedec(F,17)),expo=[10,10,10,1,1,1]);
  my(fac=matrix(6,2,i,j,if(j==1,ps[i],expo[i])),crt=idealchinese(F,fac));
  my(R=bnrinit(B,fac,0,9),rels=List(),record=List());
  print("RAY_CLASS ",R.cyc," ORDER ",R.no);
  for(j=1,6,
    my(bid=idealstar(F,idealpow(F,ps[j],expo[j]),2));
    for(k=1,#bid.gen,
      my(vals=vector(6,i,1),u=nfeltpow(F,bid.gen[k],3));vals[j]=u;
      my(x=idealchinese(F,crt,vals),col=bnrisprincipal(R,x,0));
      listput(rels,col);listput(record,[j,"cube",k,col]);
    );
    if(j<=3,
      my(indices=matindexrank(Mod(local[3][j],3))[2]);
      for(k=1,#indices,
        my(vals=vector(6,i,1));vals[j]=norms[indices[k]];
        my(x=idealchinese(F,crt,vals),col=bnrisprincipal(R,x,0));
        listput(rels,col);listput(record,[j,"norm",indices[k],col]);
      );
    );
  );
  my(pres=concat(matdiagonal(R.cyc),Mat(Vec(rels))),H=mathnf(pres),S=matsnf(H,1),U=S[1],V=S[2],D=S[3]);
  if(U*H*V!=D || abs(matdet(U))!=1 || abs(matdet(V))!=1,error("Smith identity"));
  my(ds=vector(#R.cyc,i,D[i,i]));
  print("GENUS_GALOIS_SMITH ",ds," ORDER ",prod(i=1,#ds,ds[i]));
  print("RELATIONS ",Vec(record));
  print("HNF ",H," LEFT ",U," RIGHT ",V," LEFT_INVERSE ",U^-1," RIGHT_INVERSE ",V^-1);
  for(j=1,3,
    my(f2=fac,vals=vector(6,i,1));f2[j,2]=11;vals[j]=pi;
    my(x=idealchinese(F,f2,vals),I=idealdiv(F,x,ps[j]),cl=-bnrisprincipal(R,I,0),coord=U*cl,ord=1);
    for(i=1,6,if(idealval(F,I,ps[i])!=0,error("prime Artin ideal not coprime")));
    for(i=1,#ds,ord=lcm(ord,ds[i]/gcd(ds[i],coord[i])));
    print("PRIME3_GENUS_FROBENIUS ",j," IDEAL ",I," CLASS ",cl," COORD ",coord," ORDER ",ord);
  );
  writebin("research_norm_index/code/cyclotomic_base1_genus.bin",[R,fac,pres,H,U,V,D,record]);
  print("DONE");
};
run();
quit;
