\\ Local exploratory arithmetic only.  No external submission.
\\ The interpretation as a rank bound is not asserted by this file.
default(parisizemax,2000000000);
sqrat(a,p)={my(v);if(a==0,return(1));v=valuation(a,p);if(v%2,return(0));a=a/p^v;if(p==2,return(lift(Mod(a,8))==1),return(kronecker(lift(Mod(a,p)),p)==1));};
one(c)={
 my(B=bnfinit(x^4+c,1),S,U,G,L=List(),NF,T=Mod(x,x^4+c),h,q,z,w,M);
 print("COEFFICIENT ",c);
 print("CERTIFIED ",bnfcertify(B));
 S=concat(idealprimedec(B,2),idealprimedec(B,3));
 U=bnfunits(B,S);G=vector(#U[1],i,nfbasistoalg(B,nffactorback(B,U[1][i])));
 print("DISCRIMINANT ",B.disc," SIGNATURE ",B.sign," SCLASS ",bnfsunit(B,S)[5]);
 print("GENERATORS ",G);
 for(pindex=1,2,
  my(p=if(pindex==1,2,3),P=idealprimedec(B,p));
  for(e=0,5,for(a=-100,100,
   if(a==0,next());q=a/p^e;w=q^5+c*q;
   if(w==0 || !sqrat(w,p),next());
   z=q*(q-T);
   h=vector(#G,i,(1-prod(j=1,#P,nfhilbert(B,G[i],z,P[j])))/2);
   if(vecsum(h)>0,listput(L,[p,q,h]));
  ));
  print("AFTER PRIME ",p," ROWS ",#L);
 );
 z=-c*T;
 for(pindex=1,2,
  my(p=if(pindex==1,2,3),P=idealprimedec(B,p));
  h=vector(#G,i,(1-prod(j=1,#P,nfhilbert(B,G[i],z,P[j])))/2);
  if(vecsum(h)>0,listput(L,[p,"T0",h]));
 );
 M=matrix(#L,#G,i,j,L[i][3][j]);
 print("FINITE ROW RANK ",matrank(Mod(M,2))," CANDIDATE DIMENSION ",#G-matrank(Mod(M,2)));
 my(V=matrix(0,#G),R=0);
 for(i=1,#L,
  my(W=matconcat([V;Mat(L[i][3])]),RR=matrank(Mod(W,2)));
  if(RR>R,print("PIVOT ",L[i]);V=W;R=RR);
 );
 print("KERNEL ",matker(Mod(M,2)));
};
for(i=1,6,one([-54,648,-432,13824,27,-4608][i]));
