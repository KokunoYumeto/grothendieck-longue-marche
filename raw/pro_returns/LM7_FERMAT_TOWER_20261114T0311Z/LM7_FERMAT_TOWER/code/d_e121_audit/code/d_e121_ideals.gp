\\ Independent peer check: direct HNF sums/products, no class reconstruction.
\\ Inputs are exact copied author objects; this is not the author's GP replay.
default(parisize,256000000);
default(parisizemax,2000000000);
ck(b,s)=if(!b,error(s));
jmat(M)=vector(matsize(M)[1],i,Vec(M[i,]));

\\ Extend an ideal by the literal marked generator image, using every HNF column.
extend_ideal(F,B,I,img)={
 my(H=idealhnf(F,I),J=idealhnf(B,0));
 for(i=1,matsize(H)[2],
  my(a=subst(lift(nfbasistoalg(F,H[,i])),x,img));
  J=idealadd(B,J,idealhnf(B,a));
 );idealhnf(B,J);
};
aut_ideal(B,I,img)=extend_ideal(B,B,I,img);
principal_product(B,fac)={
 my(M=Map(),P=Map(),J=idealhnf(B,1));
 for(i=1,matsize(fac)[1],
  my(ff=idealfactor(B,fac[i,1]));
  for(k=1,matsize(ff)[1],
   ck(isprime(ff[k,1][1]),"rational prime in exact factor support");
   my(I=idealhnf(B,ff[k,1]),key=Str(I),v=if(mapisdefined(M,key),mapget(M,key),0));
   mapput(~M,key,v+fac[i,2]*ff[k,2]);mapput(~P,key,I);
  );
 );
 my(keys=Vec(M));
 for(i=1,#keys,
  my(v=mapget(M,keys[i]));
  if(v,J=idealmul(B,J,idealpow(B,mapget(P,keys[i]),v)));
 );idealhnf(B,J);
};
class_product(B,G,c)={
 my(J=idealhnf(B,1));
 for(i=1,#G,J=idealmul(B,J,idealpow(B,G[i],c[i])));
 idealhnf(B,J);
};

{
 my(Ad=read("../inputs/e53_normalizer_actions.bin"),E=Ad[1],D=E[1]);
 my(B=D[1],alpha=D[2],xi=D[3],beta=D[4],Q=D[5],T=D[6],lab=D[8]);
 my(G=E[3],S=concat(vector(3,i,Q[lab[i]]),T));
 my(g=xi-xi^3*alpha,h=xi^4-xi^-3*alpha);
 ck(subst(lift(xi),x,g)==xi && subst(lift(alpha),x,g)==xi^3*alpha,"g marked field generators");
 ck(subst(lift(xi),x,h)==xi^4 && subst(lift(alpha),x,h)==xi^-3*alpha,"h marked field generators");
 my(principal_count=0,S_count=0,hnf_columns=0);
 for(k=1,2,
  my(aut=[g,h][k]);
  for(i=1,6,
   my(J=aut_ideal(B,S[i],aut));
   ck(J==idealhnf(B,S[Ad[5][k][i]]),"all marked S-prime HNF images");
   S_count++;hnf_columns+=18;
  );
  for(i=1,3,
   my(J=aut_ideal(B,G[i],aut));
   my(P=idealmul(B,class_product(B,G,Ad[7][k][,i]),principal_product(B,Ad[6][k][i])));
   ck(J==idealhnf(B,P),"normalizer complete HNF principal correction");
   principal_count++;hnf_columns+=18;
  );
 );
 print("{\"type\":\"normalizer_HNF\",\"S_prime_images\":",S_count,",\"principal_identities\":",principal_count,"}");

 my(Nd=read("../inputs/e53_horizontal_upper_norm.bin"),F=Nd[2]);
 my(L=F[1][4],GL=F[2],lh=Mod(x,L.pol));
 for(i=1,3,
  my(I=Nd[4][i],J=extend_ideal(L,B,I,beta),P=idealhnf(B,G[i]));
  P=idealmul(B,P,aut_ideal(B,G[i],h));
  P=idealmul(B,P,aut_ideal(B,aut_ideal(B,G[i],h),h));
  ck(J==idealhnf(B,P),"extended actual horizontal norm equals product of conjugates");
  ck(idealnorm(L,I)==idealnorm(B,G[i]),"horizontal norm absolute norm");
  ck(idealhnf(L,I)==idealhnf(L,idealmul(L,class_product(L,GL,Nd[6][,i]),principal_product(L,Nd[5][i]))),"horizontal norm principal correction by HNF");
  principal_count++;hnf_columns+=6+54;
 );
 my(Jd=read("../inputs/e53_horizontal_upper_extension.bin"));
 for(i=1,2,
  my(I=extend_ideal(L,B,GL[i],beta));
  ck(I==idealhnf(B,Jd[4][i]),"literal extension of six HNF columns");
  ck(I==aut_ideal(B,I,h),"extended ideal h fixed");
  ck(idealnorm(B,I)==idealnorm(L,GL[i])^3,"extended ideal absolute norm cube");
  ck(I==idealhnf(B,idealmul(B,class_product(B,G,Jd[6][,i]),principal_product(B,Jd[5][i]))),"horizontal extension principal correction by HNF");
  principal_count++;hnf_columns+=6+18;
 );
 print("{\"type\":\"horizontal_HNF\",\"norm_identities\":3,\"extension_identities\":2}");

 my(Cd=read("../inputs/e53_cyclic_nine_comparison.bin"),Fd=Cd[2],CF=Fd[1],xf=Mod(x,CF.pol));
 for(i=1,3,
  my(I=Cd[4][i],J=extend_ideal(CF,B,I,xi),P=idealhnf(B,G[i]));
  P=idealmul(B,P,aut_ideal(B,G[i],g));
  P=idealmul(B,P,aut_ideal(B,aut_ideal(B,G[i],g),g));
  ck(J==idealhnf(B,P),"extended cyclic-nine norm equals conjugate product");
  ck(idealnorm(CF,I)==idealnorm(B,G[i]),"cyclic-nine norm absolute norm");
  ck(idealhnf(CF,I)==principal_product(CF,Cd[5][i]),"cyclic-nine exact principal HNF identity");
  principal_count++;hnf_columns+=6+54;
 );

 my(U=[xf,1+xf,1+xf^2,xf^4-1,-4+xf^4+xf^5,3+2*xf+3*xf^2+3*xf^3-xf^4+xf^5,-4-xf+xf^2-xf^4]);
 ck(U==Fd[2],"all seven literal full S-unit generators");
 my(P3=idealprimedec(CF,3)[1],PT=idealprimedec(CF,53),C=matrix(4,7),V=matrix(4,7));
 for(j=1,7,
  my(v=idealval(CF,U[j],P3),n=polresultant(CF.pol,lift(U[j]))/3^v);
  ck(valuation(n-1,3)>=2,"wild norm congruence");
  C[1,j]=lift(Mod(-(n-1)/9,3));V[1,j]=v;
 );
 for(i=1,3,
  my(pr=nfmodprinit(CF,PT[i],'z),rx=nfmodpr(CF,xf,pr));
  for(j=1,7,
   my(v=idealval(CF,U[j],PT[i]),a=nfmodpr(CF,U[j]/(53*xf^3)^v,pr),b=a^312,hit=-1);
   for(k=0,8,if(b==rx^k,ck(hit==-1,"unique ninth root phase");hit=k));
   ck(hit>=0,"ninth root phase exists");C[i+1,j]=(-hit)%9;V[i+1,j]=v;
  );
 );
 ck(C==Fd[3] && V==Fd[4],"full seven-unit local character and valuation matrices");
 ck(C==matrix(4,7,i,j,if(i==1,0,[3,6,3,6,0,0,0][j])),"literal local character table");
 print("{\"type\":\"literal_units\",\"S_units\":7,\"tame_phases\":21,\"wild_norms\":7,\"characters\":",jmat(C),",\"valuations\":",jmat(V),"}");
 print("{\"status\":\"PASS\",\"scope\":\"Independent direct HNF ideal checks and literal unit-character checks on copied certified lower-field objects; no upper-field BNF or author replay claimed\",\"S_prime_images\":",S_count,",\"principal_ideal_identities\":",principal_count,",\"marked_HNF_columns\":",hnf_columns,"}");
}
quit;
