\\ E.57: unconditional first complex norm transition at17.
default(parisize,512000000);
default(realprecision,100);
setrand(1701);
check(a,s)=if(!a,error(s));
jpoly(v)=Str(vector(poldegree(lift(v))+1,i,Str(polcoef(lift(v),i-1))));
jmat(M)=Str(vector(matsize(M)[1],i,vector(matsize(M)[2],j,M[i,j])));
K=bnfinit(y^2+y+1,1);
R=rnfinit(K,x^3-17*y);
P=x^6+17*x^3+289;
L=bnfinit(P,1);
check(bnfcertify(K)==1 && bnfcertify(L)==1,"unconditional certification");
check(L.cyc==[3,3],"class group");
z=Mod(x^3/17,P); t=Mod(x,P); zk=Mod(y,K.pol);
pi=2-z; pibar=3+z; lambda=1-z;
c=t+3*z+1; g1=-2-3*z-z*t; g2=-3-z+z*t;
P1=idealhnf(L,7,x-3); P2=idealhnf(L,7,x+1); P3=idealhnf(L,7,x+2);
G=Mod(Mat([bnfisprincipal(L,P1,0),bnfisprincipal(L,P2,0)]),3);
check(matdet(G)!=0,"actual class generators");
classv(I)=lift(G^(-1)*Mod(bnfisprincipal(L,I,0),3));
Nelt(u)=rnfeltnorm(R,Mod(lift(u),x^3-17*zk));
relideal(I)=rnfidealabstorel(R,vector(6,i,sum(j=1,6,I[j,i]*L.zk[j])));
Nideal(I)=rnfidealnormrel(R,relideal(I));
run()={
  my(Q3=idealhnf(L,idealprimedec(L,3)[1]),Q17=idealhnf(L,idealprimedec(L,17)[1]));
  my(D7=idealprimedec(L,7),Qbar);
  for(j=1,#D7,if(D7[j][4]==3,Qbar=idealhnf(L,D7[j])));
  check(classv(P1)==[1,0]~ && classv(P2)==[0,1]~ && classv(P3)==[2,2]~,"prime classes");
  check(classv(Q3)==[0,0]~ && classv(Q17)==[0,0]~,"ramified prime classes");
  check(idealhnf(L,c)==Q3 && idealhnf(L,t)==Q17,"literal uniformizers");
  check(idealhnf(L,g1)==idealpow(L,P1,3),"first class cube");
  check(idealhnf(L,g2)==idealpow(L,P2,3),"second class cube");
  my(src=concat(concat(L.fu,[c,t,pibar,pi,g1,g2]),[z]));
  my(expected=[1,1,1-zk,17*zk,(3+zk)^3,(2-zk)^3,-zk^2*(2-zk)^3,zk^2*(2-zk)^3,1]);
  for(j=1,9,
    check(Nelt(src[j])==expected[j] || (j<=2 && Nelt(src[j])==-1),"literal norm");
  );
  my(ideals=[Q3,Q17,P1,P2,P3,Qbar],V=matrix(6,9));
  for(i=1,6,for(j=1,9,V[i,j]=idealval(L,src[j],idealfactor(L,ideals[i])[1,1])));
  my(N=[0,0,1,0,0,0,0,0,0;0,0,0,1,0,0,0,0,0;0,0,0,0,0,3,3,3,0;0,0,0,0,3,0,0,0,0;0,0,0,1,0,0,2,2,0]);
  my(w=g1^2/pi^2);
  check(Nelt(w)==zk,"root norm correction");
  check(idealfactor(L,w)==idealfactor(L,idealmul(L,idealpow(L,P1,4),idealmul(L,idealpow(L,P2,-2),idealpow(L,P3,-2)))),"zero norm divisor");
  print("{\"type\":\"field\",\"certified\":1,\"class_group\":[3,3],\"polynomial\":",jpoly(P),",\"integral_basis\":[",concat(vector(6,i,concat([if(i>1,",",""),jpoly(L.zk[i])]))),"]}");
  print("{\"type\":\"basis\",\"source\":[",concat(vector(9,i,concat([if(i>1,",",""),jpoly(src[i])]))),"],\"norms\":[",concat(vector(9,i,concat([if(i>1,",",""),jpoly(Nelt(src[i]))]))),"],\"valuation_matrix\":",jmat(V),",\"norm_matrix\":",jmat(N),"}");
  print("{\"type\":\"ideals\",\"hnf\":[",concat(vector(6,i,concat([if(i>1,",",""),jmat(ideals[i])]))),"],\"class_columns\":[[0,0],[0,0],[1,0],[0,1],[2,2],[0,0]]}");
  print("{\"type\":\"root_norm\",\"element\":",jpoly(w),",\"norm\":",jpoly(Nelt(w)),",\"valuations\":[0,0,4,-2,-2,0]}");
  my(count=0);
  forprime(p=2,61,if(p!=3 && p!=7 && p!=17,
    my(D=idealprimedec(L,p));
    for(j=1,#D,
      my(H=idealhnf(L,D[j]),cv=classv(H),J=idealmul(L,H,idealmul(L,idealpow(L,P1,-cv[1]),idealpow(L,P2,-cv[2]))));
      my(gg=bnfisprincipal(L,J,1),q=nfbasistoalg(L,gg[2]));
      check(gg[1]==[0,0]~ && idealhnf(L,q)==J,"corrected divisor");
      my(base=rnfidealdown(R,relideal(H)),bg=bnfisprincipal(K,base,1),pbase=nfbasistoalg(K,bg[2]));
      my(f=D[j][4]/idealfactor(K,base)[1,1][4],norm=Nelt(q),eps=norm*(2-zk)^(cv[1]+cv[2])/pbase^f,e=-1);
      for(i=0,2,if(eps==zk^i || eps==-zk^i,e=i));
      check(e>=0,"exact root factor");
      print("{\"type\":\"global_column\",\"rational_prime\":",p,",\"prime_index\":",j,",\"relative_residue_degree\":",f,",\"class\":",Vec(cv),",\"source\":",jpoly(q),",\"norm\":",jpoly(norm),",\"base_prime_generator\":",jpoly(pbase),",\"root_exponent\":",e,"}");
      count++;
    )
  ));
  print("{\"type\":\"completion\",\"status\":\"PASS\",\"certified_fields\":2,\"source_generators\":9,\"global_norm_columns\":",count,"}");
};
run();
quit;
