default(parisize,128000000);
default(parisizemax,1000000000);
{
 my(V=read("../inputs/e114_cyclo9_base.bin"),B=V[1],z=V[2],U=V[3],T=V[5],F=B.nf,P=B.pol);
 my(C=matrix(7,3),sgn=vector(3),O=vector(3));
 for(g=0,2,
  my(u=subst(lift(U[5]),x,z^(4^g)),vs=vector(3,i,idealval(F,u,T[i])),v=u);
  O[g+1]=u;
  for(i=1,3,v/=U[i+4]^vs[i];C[i+4,g+1]=vs[i]);
  my(uc=bnfisunit(B,v));
  if(#uc!=3,error("orbit ratio not an ordinary unit"));
  C[2,g+1]=uc[1];C[3,g+1]=uc[2];
  v/=U[2]^uc[1]*U[3]^uc[2];
  my(ok=0);
  for(e=0,8,
   if(v==z^e,C[1,g+1]=e;sgn[g+1]=1;ok=1);
   if(v==-z^e,C[1,g+1]=e;sgn[g+1]=-1;ok=1);
  );
  if(!ok,error("literal torsion coordinate"));
  my(rec=sgn[g+1]*prod(i=1,7,U[i]^C[i,g+1]));
  if(rec!=u,error("literal orbit-unit relation"));
  print("{\"type\":\"orbit\",\"g\":",g,",\"polynomial_coefficients\":",vector(6,i,Str(polcoef(lift(u),i-1))),",\"prime_valuations\":",vs,",\"S_unit_coordinates\":",Vec(C[,g+1]),",\"sign\":",sgn[g+1],"}");
 );
 print("{\"type\":\"matrix\",\"rows\":",vector(7,i,Vec(C[i,])),"}");
 writebin("e_inert_tail_orbit.bin",[V,O,C,sgn]);
 print("{\"type\":\"completion\",\"status\":\"PASS\"}");
}
quit;
