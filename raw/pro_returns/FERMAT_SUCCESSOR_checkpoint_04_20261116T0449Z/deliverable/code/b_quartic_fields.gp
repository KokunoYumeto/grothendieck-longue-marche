\\ Independent finite arithmetic certificates for the quartic local-order law.
\\ PARI/GP >=2.17.  Run: gp -q b_quartic_fields.gp
\\ No inherited computational output or data file is read.
default(parisize,256000000);
default(parisizemax,2000000000);
default(realprecision,100);
must(ok,msg)=if(!ok,error(msg));
decomp(B,p)=my(z=idealprimedec(B,p));vector(#z,j,[z[j].e,z[j].f]);
record(P,tag,ell,expected)= {
  my(B=bnfinit(P,1),cert=bnfcertify(B));
  must(cert==1,"unconditional BNF certification failed");
  must(B.no==expected,"class number differs from claimed value");
  must(gcd(B.no,ell)==1,"unwanted primary ideal class group");
  print(tag,"; polynomial=",P,"; degree=",poldegree(P),"; discriminant=",B.disc,"; h=",B.no,"; certificate=",cert,"; at 2=",decomp(B,2),"; at ",ell,"=",decomp(B,ell));
  B;
};

print("PARI version: ",version());
BF=record(x^4+1,"F=Q(zeta8)",3,1);
ue=bnfisunit(BF,Mod(1+x-x^3,x^4+1));
must(#ue==2 && abs(ue[1])==1 && BF.tu[1]==8,"wrong full quartic unit group");
print("Full units: mu8 times <1+sqrt(2)>; fundamental-unit coordinates=",ue,"; PASS");

\\ Degree-sixteen third-division fields, reconstructed from the actual radical.
forcase3(A)={
  my(P=x^8+216*A^3*x^4-3888*A^6,z=polcompositum(P,x^2+1,1));
  must(#z==1,"unexpected intersection in third-division compositum");
  my(Q=z[1][1],a=Mod(z[1][2],Q),ii=Mod(z[1][3],Q));
  must(poldegree(Q)==16 && polisirreducible(Q),"wrong third-division degree");
  must(subst(P,x,a)==0 && ii^2==-1,"radical maps fail");
  my(Y=a/3,X=12*A^2*a^2/(a^4+108*A^3),m=(3*X^2+A)/(2*Y));
  must(Y^2==X^3+A*X,"point not on elliptic curve");
  must(m^2-2*X==X && m*(X-(m^2-2*X))-Y==-Y,"point is not nonzero 3-torsion");
  my(rt=(3*X^2+3*A)/(2*A),zz=(-1+ii*rt)/2);
  must(rt^2==3 && zz^2+zz+1==0,"actual cyclotomic embedding fails");
  my(B=record(polredbest(Q),Str("Q(E",A,"[3])"),3,1));
  must(decomp(B,2)==[[8,2]] && decomp(B,3)==[[8,2]],"wrong local third-division group");
};
forcase3(1);
forcase3(4);

\\ Twelve degree-eight fields kill every character of the residual fifth-division class group.
VV=[[1,0],[0,1],[1,1],[1,2],[1,3],[2,1]];
HH=[1,1,2,2,1,2];
pointcase5(sig,A)={
  my(P=x^8-2*sig*x^4+5,a=Mod(x,P),ii=(a^4/sig-1)/2);
  must(ii^2==-1,"Gaussian embedding in fifth-division field fails");
  my(Y=if(A==1,(1+ii)*a/(2-ii),4*a/(2-ii)),X=5*Y^2/(A*(4+2*ii)));
  must(Y^2==X^3+A*X,"fifth-division point misses the curve");
  my(m=(3*X^2+A)/(2*Y),XX=m^2-2*X,YY=m*(X-XX)-Y);
  must(XX==-X && YY==ii*Y,"actual [2]P=[i]P identity fails");
  print("Exact fifth-division radical and doubling identity, A=",A,": PASS");
};
pointcase5(-1,1);
pointcase5(1,4);
forcase5(sig,k)={
  my(u=VV[k][1],v=VV[k][2],ii=Mod(y,y^2+1));
  my(c=sig^(u+v)*(1+2*ii)^u*(1-2*ii)^v,P);
  if(u==1 && v==1,
    P=polcompositum(x^4-5,x^2+1)[1],
    P=polresultant(y^2+1,x^4-lift(c),y)
  );
  must(poldegree(P)==8 && polisirreducible(P),"wrong character-field degree");
  record(polredbest(P),Str("fifth-division character field sigma=",sig,"; (u,v)=",VV[k]),5,HH[k]);
};
for(sigidx=1,2,for(k=1,6,forcase5(if(sigidx==1,-1,1),k)));
print("All 15 field/class/local certificates passed unconditionally.");
quit;
