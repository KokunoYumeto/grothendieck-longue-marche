default(parisize,256000000);
default(parisizemax,2000000000);
default(realprecision,100);
run()={
  my(dat=read("research_norm_index/code/cyclotomic_base1_bnf.bin"),B=dat[1],F=B.nf,z9=dat[2],a=dat[3],beta=a*z9,pi=beta+1);
  my(local=read("research_norm_index/code/cyclotomic_base1_ninth_norms.bin"),norms=local[4]);
  my(ps=concat(idealprimedec(F,3),idealprimedec(F,17)),expo=[16,16,16,1,1,1]);
  my(fac=matrix(6,2,i,j,if(j==1,ps[i],expo[i])),crt=idealchinese(F,fac));
  my(units=concat([z9],B.fu),M=matrix(6,#units));
  for(j=1,3,
    my(row=local[3][j][1][1,]);
    for(k=1,#units,M[j,k]=lift(Mod(row*ideallog(F,units[k],local[1][j]),9)));
  );
  for(j=4,6,
    my(bid=idealstar(F,ps[j],2,9));
    if(bid.cyc!=[9],error("tame ninth quotient"));
    for(k=1,#units,M[j,k]=ideallog(F,units[k],bid)[1]);
  );
  my(US=matsnf(mathnf(concat(9*matid(6),M))),unitindex=9^6/prod(i=1,6,US[i]));
  print("NINTH_UNIT_SYMBOLS ",M," COKERNEL ",US," IMAGE_ORDER ",unitindex," AMBIGUOUS_CLASS_ORDER ",9*9^6/(9*unitindex));
  my(R=bnrinit(B,fac,0,27),rels=List(),record=List());
  print("NINTH_RAY_CLASS ",R.cyc," ORDER ",R.no);
  for(j=1,6,
    my(bid=idealstar(F,idealpow(F,ps[j],expo[j]),2));
    for(k=1,#bid.gen,
      my(vals=vector(6,i,1));vals[j]=nfeltpow(F,bid.gen[k],9);
      my(z=idealchinese(F,crt,vals),col=bnrisprincipal(R,z,0));
      listput(rels,col);listput(record,[j,"ninth",k,col]);
    );
    if(j<=3,
      for(k=1,#norms,
        my(vals=vector(6,i,1));vals[j]=norms[k];
        my(z=idealchinese(F,crt,vals),col=bnrisprincipal(R,z,0));
        listput(rels,col);listput(record,[j,"norm",k,col]);
      );
    );
  );
  my(pres=concat(matdiagonal(R.cyc),Mat(Vec(rels))),H=mathnf(pres),S=matsnf(H,1),U=S[1],V=S[2],D=S[3]);
  if(U*H*V!=D || abs(matdet(U))!=1 || abs(matdet(V))!=1,error("ninth Smith identity"));
  my(ds=vector(#R.cyc,i,D[i,i]));
  print("NINTH_GENUS_GALOIS_SMITH ",ds," ORDER ",prod(i=1,#ds,ds[i]));
  if(prod(i=1,#ds,ds[i])!=9*9^6/unitindex,error("ray/ambiguity mismatch"));
  print("NINTH_RELATIONS ",Vec(record));
  print("NINTH_HNF ",H," LEFT ",U," RIGHT ",V," LEFT_INVERSE ",U^-1," RIGHT_INVERSE ",V^-1);
  my(aut=a*z9^-3-z9^4);
  if(subst(F.pol,x,aut)!=0 || subst(lift(beta),x,aut)!=beta || subst(lift(z9),x,aut)!=z9^4,error("actual cyclotomic automorphism"));
  my(AM=bnrgaloismatrix(R,lift(aut)));
  if(denominator(H^-1*AM*H)!=1,error("unstable genus quotient"));
  my(CH=mathnf(concat(H,AM-matid(#R.cyc))),CS=matsnf(CH,1),CD=vector(#R.cyc,i,CS[3][i,i]));
  if(CS[1]*CH*CS[2]!=CS[3],error("coinvariant Smith identity"));
  print("NINTH_DELTA_ACTION ",AM," COINVARIANT_SMITH ",CD," COINVARIANT_LEFT ",CS[1]," COINVARIANT_HNF ",CH);
  my(primes=List());
  for(j=1,3,
    my(f2=fac,vals=vector(6,i,1));f2[j,2]=17;vals[j]=pi;
    my(z=idealchinese(F,f2,vals),I=idealdiv(F,z,ps[j]),cl=-bnrisprincipal(R,I,0),coord=U*cl,co=CS[1]*cl,ord=1,cord=1);
    for(i=1,6,if(idealval(F,I,ps[i])!=0,error("prime Artin ideal not coprime")));
    for(i=1,#ds,ord=lcm(ord,ds[i]/gcd(ds[i],coord[i]));cord=lcm(cord,CD[i]/gcd(CD[i],co[i])));
    print("NINTH_PRIME3_FROBENIUS ",j," IDEAL ",I," CLASS ",cl," COORD ",coord," ORDER ",ord," COINVARIANT_COORD ",co," COINVARIANT_ORDER ",cord);
    listput(primes,[I,cl,coord,ord,co,cord]);
  );
  writebin("research_norm_index/code/cyclotomic_base1_ninth_genus.bin",[R,fac,pres,H,U,V,D,record,AM,CH,CS,primes,M,unitindex]);
  print("DONE: ninth relative genus quotient and actual prime Frobenius.");
};
run();
quit;
