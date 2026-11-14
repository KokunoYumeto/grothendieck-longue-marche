\\ E.64: actual adjacent complex norm fields and residue symbols.
default(parisize,256000000);
default(parisizemax,2000000000);
default(realprecision,80);
setrand(1764);
check(a,s)=if(!a,error(s));
jpoly(v)=Str(vector(poldegree(lift(v))+1,i,Str(polcoef(lift(v),i-1))));
jmat(M)=Str(vector(matsize(M)[1],i,vector(matsize(M)[2],j,M[i,j])));
run()={
  my(P=x^6+17*x^3+289,Q=x^18+17*x^9+289);
  my(F=nfinit(P),L=nfinit(Q),b=Mod(x,P),z=b^3/17);
  my(B=bnfinit(F,1));
  check(bnfcertify(B)==1 && B.cyc==[3,3],"certified base class group");
  for(d=0,2,
    my(R=if(d==0,x^2+x+1,x^(2*3^d)+17*x^(3^d)+289));
    my(E=if(d==0,nfinit(R),if(d==1,F,L)),D3=idealprimedec(E,3),D17=idealprimedec(E,17));
    check(#D3==1 && D3[1][3]==2*3^d && D3[1][4]==1,"unique totally ramified three-prime");
    check(#D17==1 && D17[1][3]==3^d && D17[1][4]==2,"unique seventeen-prime");
    print("{\"type\":\"field\",\"d\":",d,",\"polynomial\":",jpoly(R),",\"disc\":",E.disc,",\"prime3_hnf\":",jmat(idealhnf(E,D3[1])),",\"prime17_hnf\":",jmat(idealhnf(E,D17[1])),"}");
  );
  my(P17=idealprimedec(F,17)[1],mp17=nfmodprinit(F,P17,'t),zz=nfmodpr(F,z,mp17));
  my(U=concat(B.fu,[z]),unitres=vector(#U),unitpow=vector(#U));
  for(i=1,#U,
    my(r=nfmodpr(F,U[i],mp17),k=-1);
    for(j=0,2,if(r==zz^j,k=j));
    check(k>=0 && r^96==1,"all base units have cube residue");
    unitres[i]=k;unitpow[i]=if(r^96==1,1,0);
  );
  print("{\"type\":\"units\",\"fundamental_units\":[",concat(vector(#B.fu,i,concat([if(i>1,",",""),jpoly(B.fu[i])]))),"],\"root\":",jpoly(z),",\"residue_exponents\":",unitres,",\"cubic_residues\":",unitpow,",\"class_group\":[3,3],\"ambiguous_order\":27}");
  my(count=0,split=0,inert=0);
  forprime(p=2,97,if(p!=3 && p!=17,
    my(D=idealprimedec(F,p),E=idealprimedec(L,p));
    for(i=1,#D,
      my(mp=nfmodprinit(F,D[i],'t),rb=nfmodpr(F,b,mp),rz=nfmodpr(F,z,mp),N=p^D[i][4],sym=rb^((N-1)/3),g=-1);
      for(j=0,2,if(sym==rz^j,g=j));
      check(g>=0,"Kummer residue in mu3");
      my(gen=nfbasistoalg(F,D[i][2]),up=Mod(subst(lift(gen),x,x^3),Q),above=List());
      for(j=1,#E,if(idealval(L,up,E[j])>0,listput(above,[E[j][3]/D[i][3],E[j][4]/D[i][4]])));
      check(if(g==0,#above==3,#above==1),"actual prime count versus Kummer residue");
      for(j=1,#above,check(above[j]==if(g==0,[1,1],[1,3]),"actual relative degrees"));
      if(g==0,split++,inert++);
      print("{\"type\":\"prime\",\"p\":",p,",\"index\":",i,",\"f\":",D[i][4],",\"hnf\":",jmat(idealhnf(F,D[i])),",\"generator\":",jpoly(gen),",\"residue_polynomial\":",jpoly(rb.pol),",\"residue_modulus\":",jpoly(rb.mod),",\"zeta_polynomial\":",jpoly(rz.pol),",\"symbol\":",g,",\"relative_degrees\":",Vec(above),"}");
      count++;
    )
  ));
  print("{\"type\":\"completion\",\"status\":\"PASS\",\"certified_base_class_group\":1,\"prime_records\":",count,",\"split_records\":",split,",\"inert_records\":",inert,",\"unit_records\":",#U,"}");
};
run();
quit;
