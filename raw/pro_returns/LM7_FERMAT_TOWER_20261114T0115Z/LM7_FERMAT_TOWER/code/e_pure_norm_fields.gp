\\ E.65: certified pure fields, actual relative unit norms and prime contractions.
default(parisize,256000000);
default(parisizemax,2000000000);
default(realprecision,100);
setrand(1765);
check(a,s)=if(!a,error(s));
jpoly(v)=Str(vector(poldegree(lift(v))+1,i,Str(polcoef(lift(v),i-1))));
jmat(M)=Str(vector(matsize(M)[1],i,vector(matsize(M)[2],j,M[i,j])));
run()={
  my(B=bnfinit(y^3-17,1),R=rnfinit(B,x^3-y),C=bnfinit(x^9-17,1));
  check(bnfcertify(B)==1 && bnfcertify(C)==1,"unconditional fields");
  check(B.cyc==[] && C.cyc==[],"both pure class groups trivial");
  print("{\"type\":\"units\",\"base_class\":",B.cyc,",\"source_class\":",C.cyc,",\"base_unit\":",jpoly(B.fu[1]),",\"source_units\":[",concat(vector(#C.fu,i,concat([if(i>1,",",""),jpoly(C.fu[i])]))),"]}");
  my(row=vector(#C.fu),signs=vector(#C.fu));
  for(i=1,#C.fu,
    my(n=rnfeltnorm(R,Mod(lift(C.fu[i]),R.pol)),v=bnfisunit(B,n));
    check(#v==2,"unit norm in certified basis");
    row[i]=v[1];signs[i]=v[2];
    print("{\"type\":\"unit_norm\",\"index\":",i,",\"element\":",jpoly(C.fu[i]),",\"norm\":",jpoly(n),",\"coordinates\":",Vec(v),"}");
  );
  check(row==[0,3,0,0] && signs==[0,0,1,0],"literal unit norm matrix");
  for(d=1,2,
    my(F=if(d==1,nfinit(x^3-17),C.nf),D3=idealprimedec(F,3),D17=idealprimedec(F,17));
    check(#D3==2 && vecsort(vector(#D3,i,[D3[i][3],D3[i][4]]))==[[3^(d-1),1],[2*3^(d-1),1]],"pure primes at3");
    check(#D17==1 && D17[1][3]==3^d && D17[1][4]==1,"pure prime at17");
    print("{\"type\":\"pure_field\",\"d\":",d,",\"polynomial\":",jpoly(F.pol),",\"signature\":",F.sign,",\"disc\":",F.disc,",\"prime3_degrees\":",vector(#D3,i,[D3[i][3],D3[i][4]]),",\"prime3_hnfs\":[",concat(vector(#D3,i,concat([if(i>1,",",""),jmat(idealhnf(F,D3[i]))]))),"],\"prime17_hnf\":",jmat(idealhnf(F,D17[1])),"}");
    my(cp=polcompositum(x^(3^d)-17,x^2+x+1,3),M=nfinit(cp[1]),P3=idealprimedec(M,3));
    check(cp[2]^(3^d)==17 && cp[3]^2+cp[3]+1==0,"actual compositum embeddings");
    check(#P3==3 && vector(#P3,i,[P3[i][3],P3[i][4]])==vector(3,i,[2*3^(d-1),1]),"complexification primes at3");
    print("{\"type\":\"complexification\",\"d\":",d,",\"polynomial\":",jpoly(cp[1]),",\"alpha\":",jpoly(cp[2]),",\"zeta\":",jpoly(cp[3]),",\"prime3_degrees\":",vector(#P3,i,[P3[i][3],P3[i][4]]),"}");
  );
  my(F=nfinit(x^3-17),L=C.nf,a=Mod(x,F.pol),count=0,split=0,inert=0,mixed=0);
  forprime(p=2,97,if(p!=3 && p!=17,
    my(D=idealprimedec(F,p),E=idealprimedec(L,p));
    for(i=1,#D,
      my(mp=nfmodprinit(F,D[i],'t),ra=nfmodpr(F,a,mp),N=p^D[i][4],g=-1,rz=ra^0);
      if(N%3==1,
        rz=ffprimroot(ra)^((N-1)/3);
        my(sym=ra^((N-1)/3));
        for(j=0,2,if(sym==rz^j,g=j));
        check(g>=0,"actual finite-field cubic character")
      );
      my(gen=nfbasistoalg(F,D[i][2]),up=Mod(subst(lift(gen),x,x^3),L.pol),above=List());
      for(j=1,#E,if(idealval(L,up,E[j])>0,listput(above,[E[j][3]/D[i][3],E[j][4]/D[i][4]])));
      my(degs=vecsort(Vec(above)),expect=if(N%3==2,[[1,1],[1,2]],if(g==0,[[1,1],[1,1],[1,1]],[[1,3]])));
      check(degs==expect,"exact pure relative prime degrees");
      if(N%3==2,mixed++,if(g==0,split++,inert++));
      print("{\"type\":\"prime\",\"p\":",p,",\"index\":",i,",\"f\":",D[i][4],",\"hnf\":",jmat(idealhnf(F,D[i])),",\"generator\":",jpoly(gen),",\"residue_polynomial\":",jpoly(ra.pol),",\"residue_modulus\":",jpoly(ra.mod),",\"zeta_polynomial\":",jpoly(rz.pol),",\"symbol\":",g,",\"relative_degrees\":",degs,"}");
      count++;
    )
  ));
  print("{\"type\":\"completion\",\"status\":\"PASS\",\"certified_fields\":2,\"norm_row\":",row,",\"norm_signs\":",signs,",\"unit_norm_index\":",gcd(row),",\"prime_records\":",count,",\"split_records\":",split,",\"inert_records\":",inert,",\"mixed_records\":",mixed,"}");
};
run();
quit;
