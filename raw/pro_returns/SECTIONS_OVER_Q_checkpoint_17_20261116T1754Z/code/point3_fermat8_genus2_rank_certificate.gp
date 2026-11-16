\\ Exact local PARI certificate for A186.  No external service is called.
\\ Complete S-unit information is certified with flag-zero bnfcertify.
default(parisizemax,2000000000);
check(t,msg)={if(!t,error(msg));};
qsquare(a,p)={my(v);if(a==0,return(1));v=valuation(a,p);if(v%2,return(0));a=a/p^v;if(p==2,return(lift(Mod(a,8))==1),return(kronecker(lift(Mod(a,p)),p)==1));};
cases=[  [-54,-55296,[x^3/9-x^2/3+x-2,-x^3/9+x^2/3-x+3,2*x^2/3+5,-2*x^3/9+2*x^2/3-2*x+5,-1],[[2,-96],[2,-93],[2,-86]],[1,0,1,1,0;0,0,1,1,1;0,1,1,0,0]],  [648,2048,[x^3/108,x^3/108-1,x^3/108+1,-x^2/18+1,-x^2/18-x/3-1,-1],[[2,-95],[2,-90],[2,-56],[3,-96]],[0,1,0,1,0,0;1,1,0,0,0,1;1,1,0,0,0,0;0,0,0,0,1,1]],  [-432,-6912,[x^3/72+1,x^3/72,x^2/12+2,x^3/72+x^2/12+x/2+2,-1],[[2,-95],[2,-90],[2,-76]],[1,0,0,1,0;0,0,1,1,1;0,1,1,0,0]],  [13824,55296,[-x^3/144-x^2/48+x/2+10,5*x^3/576+x^2/12+x/4-6,-23*x^3/288+5*x^2/12+3*x-95,-1],[[2,-100],[2,-40]],[0,1,1,1;0,0,0,1]],  [27,432,[-x^3/18+x^2/6+x/2+1/2,-x^3/18+x/2,-x^3/18+x^2/6-x/2+1/2,-x^2/6+1/2],[[2,-97],[2,-93]],[0,1,0,1;1,1,1,1]],  [-4608,-18432,[x^3/192+x^2/24+x/4+2,-x^3/192-x^2/16-x/2-3,-x^2/48-1,x^3/32+x^2/4+2*x+17,-1],[[2,-100],[2,-72],[2,-32]],[0,1,0,1,1;1,1,1,0,1;0,0,0,0,1]] ];
main()={
 print("LOCAL PARI VERSION ",version());
 for(k=1,#cases,
  my(C=cases[k],c=C[1],F=x^4+c,B,S,U,G,D,L,M,T=Mod(x,x^4+c));
  check(polisirreducible(F),"quartic irreducibility");
  check(poldisc(x*F)==256*c^5,"curve discriminant");
  B=bnfinit(F,1);
  check(bnfcertify(B)==1,"unconditional class/unit certification");
  check(B.disc==C[2],"field discriminant");
  S=concat(idealprimedec(B,2),idealprimedec(B,3));
  U=bnfunits(B,S);
  check(bnfsunit(B,S)[5][1]==1,"S class number");
  G=vector(#C[3],i,Mod(C[3][i],F));
  D=matrix(#G,#G);
  for(j=1,#G,
   my(v=bnfisunit(B,G[j],U));
   check(#v==#G,"literal generator is an S-unit");
   D[,j]=v;
  );
  check(matrank(Mod(D,2))==#G,"literal basis spans every S-unit squareclass");
  print("CASE ",k," c=",c," disc=",B.disc," signature=",B.sign);
  print("INTEGRAL BASIS ",B.zk);
  print("CLASS GROUP ",B.clgp," CERTIFIED 1; S CLASS GROUP ",bnfsunit(B,S)[5]);
  print("S PRIME IDEALS ",S);
  print("S PRIME CLASS COORDINATES ",vector(#S,i,bnfisprincipal(B,S[i],0)));
  if(c==13824,check(vector(#S,i,bnfisprincipal(B,S[i],0))==[[1]~,[1]~],"both support primes generate the order-two class group"));
  print("LITERAL GENERATORS ",G);
  print("CERTIFIED S UNIT COORDINATES ",D);
  M=matrix(#C[4],#G);
  for(i=1,#C[4],
   my(p=C[4][i][1],q=C[4][i][2],a=q^5+c*q,v=valuation(a,p),P=idealprimedec(B,p),z=q*(q-T));
   check(a!=0 && qsquare(a,p),"actual local curve point");
   print("POINT ",i," p=",p," x=",q," v(f(x))=",v," square-unit-residue=",lift(Mod(a/p^v,if(p==2,8,p))));
   for(j=1,#G,
    my(h=vector(#P,l,nfhilbert(B,G[j],z,P[l])));
    M[i,j]=(1-prod(l=1,#P,h[l]))/2;
    print("HILBERT ",i,",",j," PRIMEWISE ",h);
   );
  );
  check(M==C[5],"literal full Hilbert matrix");
  check(matrank(Mod(M,2))==#G-2,"two-dimensional surviving Kummer group");
  print("MATRIX ",M," RANK ",matrank(Mod(M,2))," KERNEL ",matker(Mod(M,2)));
  print("PASS CASE ",k);
 );
 print("PASS: six unconditional S-unit/class certificates and all seventeen literal local Hilbert rows; each kernel has dimension2");
};
main();
