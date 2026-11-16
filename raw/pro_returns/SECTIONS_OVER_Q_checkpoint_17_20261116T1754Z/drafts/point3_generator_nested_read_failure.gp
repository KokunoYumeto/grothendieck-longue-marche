\\ Run from the work/deliverable root. All root witnesses are exact.
\\ Reuse and execute the full certified candidate-space calculation.
default(parisizemax,2000000000);
read("code/point3_fermat8_genus2_rank_certificate.gp");
rr=varhigher("rr",x);
genpoints=[[3,9],[6,108],[6,72],[24,2880],[3,18],[-8,64]];
generator_coordinates()={
 for(k=1,#cases,
  my(C=cases[k],c=C[1],F=x^4+c,B=bnfinit(F,1),T=Mod(x,F),G=vector(#C[3],i,Mod(C[3][i],F)),P=genpoints[k],eta=[P[1]-T,-T],coords=matrix(#G,2));
  check(bnfcertify(B)==1,"generator field class/unit certification");
  check(P[2]^2==P[1]^5+c*P[1],"literal rational curve point");
  print("GENERATOR CASE ",k," c=",c," POINT ",P);
  for(j=1,2,
   my(found=0);
   for(mask=0,2^#G-1,
    my(e=vector(#G,i,bittest(mask,i-1)),g=prod(i=1,#G,G[i]^e[i]),q=eta[j]/g,roots=nfroots(B.nf,rr^2-q));
    if(#roots,
     check(roots[1]^2==q,"literal square-root witness");
     check(!found,"unique basis coordinates");
     found=1;coords[,j]=e~;
     print("KUMMER ",j," COORDINATES ",e," ROOT ",roots[1]);
    );
   );
   check(found,"a supported squareclass coordinate was found");
  );
  check(Mod(C[5]*coords,2)==0*Mod(C[5]*coords,2),"known classes lie in exact Selmer kernel");
  print("POINT-TORSION COORDINATE MATRIX ",coords," MOD2 RANK ",matrank(Mod(coords,2)));
 );
 print("PASS: all six point/torsion squareclass coordinates have literal verified square-root witnesses");
};
generator_coordinates();
