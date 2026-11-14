\\ Exact cube tests in the degree54 field; no BNF is constructed here.
default(parisize,512000000);default(parisizemax,3000000000);
default(realprecision,150);setrand(1225302);
check(a,s)=if(!a,error(s));
cf(a,n)=vector(n,i,Str(polcoef(lift(a),i-1)));
{
 my(F=nfinit(y^6+y^3+1),eq=rnfequation(F,x^9-53*Mod(y,F.pol)^3,1),P=eq[1],xi=eq[2],beta=Mod(x,P)-eq[3]*xi);
 check(poldegree(P)==54 && xi^6+xi^3+1==0 && beta^9==53*xi^3,"literal degree54 root maps");
 print("{\"type\":\"field_equation\",\"degree\":54,\"polynomial\":\"",P,"\",\"xi\":",cf(xi,54),",\"beta2\":",cf(beta,54),"}");
 my(N=nfinit(P));writebin("e53_upper_exact_nf.bin",[N,xi,beta,eq]);
 print("{\"type\":\"exact_nf_ready\",\"signature\":",N.sign,",\"discriminant\":\"",N.disc,"\"}");
 my(D=read("../inputs/e119_e53_genus_transition.bin")[1],W=read("e53_upper_unit_candidates.bin"),ell=xi-beta^3/xi,U=vector(45));
 for(i=1,15,U[i]=subst(lift(D[7][i]),x,ell));
 for(i=1,10,for(j=0,2,U[15+3*(i-1)+j+1]=subst(lift(W[4][i]),x,beta*xi^j)));
 my(V=read("e53_upper_root_candidates.txt"),roots=List(),norms=List(),flags=vector(#V));
 my(EL=matrix(54,18,i,j,polcoef(lift(ell^(j-1)),i-1)),sig=xi^3*beta+eq[3]*xi);
 for(k=1,#V,
  print("{\"type\":\"root_test_start\",\"index\":",k,"}");
  my(u=prod(i=1,45,U[i]^V[k][i]),v=0,ok=nfeltispower(N,u,3,&v));flags[k]=ok;
  if(ok,
   v=nfbasistoalg(N,v);check(v^3==u,"literal cube identity");
   my(nr=v*nfgaloisapply(N,sig,v)*nfgaloisapply(N,sig,nfgaloisapply(N,sig,v)),co=Col(vector(54,i,polcoef(lift(nr),i-1))),lo=matinverseimage(EL,co));
   check(#lo==18 && EL*lo==co,"literal descent of cubic norm to lower field");
   listput(roots,[k,v]);listput(norms,[k,lo]);
   print("{\"type\":\"exact_root\",\"index\":",k,",\"exponents\":",V[k],",\"root\":",cf(v,54),",\"relative_norm_lower\":",vector(18,i,Str(lo[i])),"}");
  ,print("{\"type\":\"proved_non_cube\",\"index\":",k,",\"exponents\":",V[k],"}"));
  writebin("e53_upper_exact_roots.bin",[N,xi,beta,U,V,flags,Vec(roots),Vec(norms)]);
 );
 print("{\"type\":\"completion\",\"status\":\"PASS\",\"tests\":",#V,",\"cube_count\":",sum(i=1,#flags,flags[i]),"}");
}
quit;
