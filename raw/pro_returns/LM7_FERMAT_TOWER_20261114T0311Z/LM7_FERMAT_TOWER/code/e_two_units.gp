\\ E.52: actual certified number-field and fundamental-unit computations.
\\ This script uses PARI/GP 2.19.0; every bnf is certified unconditionally.
default(parisize, 512000000);
default(realprecision, 100);
check(a,s)=if(!a,error(s));
pol(d,j)=if(j==0,x^(3^d)-2,x^(2*3^(d+j-1))+2^(3^(j-1))*x^(3^(d+j-1))+2^(2*3^(j-1)));
jstr(v)=Str("\"",v,"\"");
jstrvec(v)=Str(vector(#v,i,Str(v[i])));
jmat(M)=Str(vector(matsize(M)[1],i,vector(matsize(M)[2],j,M[i,j])));
fields=List();
build(d,j)={
  my(P=pol(d,j), B, ce, P2, P3, mp, z, rz, q, co, aa, E, r, b);
  setrand(1000+100*j+d);
  B=bnfinit(P,1); ce=bnfcertify(B);
  check(ce==1,"uncertified bnf");
  check(B.no%3!=0,"three class number");
  P2=idealprimedec(B,2); P3=idealprimedec(B,3);
  check(#P2==1 && #P3==1,"prime uniqueness");
  check(P2[1][3]==3^d,"ramification at two");
  check(P2[1][4]==if(j==0,1,eulerphi(3^j)),"residue degree at two");
  check(P3[1][3]==poldegree(P) && P3[1][4]==1,"total ramification at three");
  mp=nfmodprinit(B,P2[1]); r=#B.fu;
  aa=vector(r); E=vector(r);
  if(j,
    z=Mod(x^(3^d)/2,P); q=2^P2[1][4]; co=(q-1)/3^j;
    rz=nfmodpr(B,z,mp);
    check(fforder(rz)==3^j,"root residue order");
    check(rz^((q-1)/3)!=1,"primitive root is a noncube");
    for(i=1,r,
      b=nfmodpr(B,B.fu[i],mp);
      aa[i]=fflog(b^co,rz^co);
      E[i]=B.fu[i]*z^(-aa[i]);
      check(nfmodpr(B,E[i],mp)^co==1,"residue-one basis");
    ),
    E=B.fu
  );
  check(r==if(j==0,(3^d-1)/2,3^(d+j-1)-1),"unit rank");
  listput(fields,[d,j,B,E,aa]);
  print("{\"type\":\"field\",\"d\":",d,",\"j\":",j,
    ",\"polynomial\":",jstr(P),",\"degree\":",poldegree(P),
    ",\"certified\":",ce,",\"class_number\":",B.no,
    ",\"signature\":",B.sign,",\"root_order\":",B.tu[1],
    ",\"prime_two\":[",P2[1][3],",",P2[1][4],"]",
    ",\"prime_three\":[",P3[1][3],",",P3[1][4],"]",
    ",\"residue_exponents\":",aa,
    ",\"fundamental_units\":",jstrvec(B.fu),
    ",\"normalized_units\":",jstrvec(E),"}");
};
getfield(d,j)={
  for(i=1,#fields,if(fields[i][1]==d && fields[i][2]==j,return(fields[i])));
  error("missing field");
};
transition(d,j)={
  my(lo=getfield(d,j),hi=getfield(d+1,j),B=lo[3],C=hi[3],
     r=#lo[4],s=#hi[4],R=matrix(r,s), norms=vector(s),
     exps, nn, u, test, sn);
  for(i=1,s,
    nn=polresultant(x^3-y,lift(hi[4][i]),x);
    nn=Mod(subst(nn,y,x),B.pol);
    exps=bnfisunit(B,nn); check(#exps==r+1,"relative norm is not a unit");
    for(a=1,r,R[a,i]=exps[a]);
    test=nn;
    for(a=1,r,test/=lo[4][a]^exps[a]);
    check(test==1 || test==-1,"normalized norm has nontrivial three-torsion");
    norms[i]=nn;
  );
  if(r,sn=matsnf(R);for(i=1,#sn,check(sn[i]%3!=0,"unit norm matrix not onto over Z3")),sn=[]);
  print("{\"type\":\"transition\",\"d\":",d,",\"j\":",j,
    ",\"rows\":",r,",\"columns\":",s,",\"matrix\":",jmat(R),
    ",\"smith\":",sn,",\"normalized_unit_norms\":",jstrvec(norms),"}");
};
for(i=1,8,my(v=[[0,0],[1,0],[2,0],[0,1],[1,1],[2,1],[0,2],[1,2]][i]);build(v[1],v[2]));
transition(0,0);
transition(1,0);
transition(0,1);
transition(1,1);
transition(0,2);
print("{\"type\":\"completion\",\"status\":\"PASS\",\"fields\":8,\"transitions\":5}");
quit;
