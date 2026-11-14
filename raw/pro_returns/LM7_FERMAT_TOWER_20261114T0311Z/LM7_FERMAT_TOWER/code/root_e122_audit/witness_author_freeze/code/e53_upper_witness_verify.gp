\\ Literal relative-ring verification of every unit, cube and norm witness.
\\ Inputs are coefficients, not an upper NF/BNF or a unit-basis assertion.
default(parisize,256000000);default(parisizemax,2000000000);
check(a,s)=if(!a,error(s));
jmat(M)=vector(matsize(M)[1],i,Vec(M[i,]));
E122WitnessPrecMin=1000000;
localnine(D,LD,u)={
 my(B=D[1],xi=D[3],beta=D[4],Q=D[5],T=D[6],lab=D[8],F=LD[1],bid=LD[5],aa=LD[6],py=F.pol,v=vector(6));
 my(coeff=Vec(lift(u)),cm=vecmin(vector(#coeff,i,valuation(coeff[i],3))));
 for(j=0,2,
  my(vv=idealval(B,u,Q[lab[j+1]]),pr=min(6*(valuation(aa^3-53,3)-1)+6*cm-vv,6*(valuation(aa^3-53,3)-1)-1));
  check(pr>=16,"proved relative p-adic precision after normalization");E122WitnessPrecMin=min(E122WitnessPrecMin,pr);
  my(loc=Mod(y-aa*y^(3*j),py),uu=subst(lift(u),x,loc)/(1+aa*Mod(y,py)^(1+3*j))^vv);
  check(idealval(F,uu,LD[4])==0,"normalized local unit");
  v[j+1]=lift(Mod(LD[8][j+1][5]*ideallog(F,uu,bid),9));
 );
 for(j=1,3,
  my(pr=nfmodprinit(B,T[j],'t),xr=nfmodpr(B,xi,pr),vv=idealval(B,u,T[j]),rr=nfmodpr(B,u/beta^vv,pr)^((53^2-1)/9),e=-1);
  for(k=0,8,if(rr==xr^k,e=k));check(e>=0,"literal ninth tame phase");v[j+3]=lift(Mod(-e,9));
 );v;
};
{
 my(W=read("../inputs/e122_literal_unit_witnesses.txt"),D=read("../inputs/e119_e53_genus_transition.bin")[1],LD=read("e53_higher_local.bin"));
 my(py=y^6+y^3+1,z=Mod(y,py),pol=x^9-53*z^3,b=Mod(x,pol),xi=Mod(z,pol),ell=xi-b^3/xi);
 check(b^9==53*xi^3 && xi^9==1,"literal relative field relations");
 my(U=vector(45),NL=nfinit(x^18+53*x^9+2809),candidate_norms=vector(10),candidate_divisors=List());
 for(i=1,15,
  check(Mod(sum(j=1,18,W[1][i][j]*x^(j-1)),D[1].pol)==D[7][i],"exact lower unit coefficient input");
  U[i]=sum(j=1,18,W[1][i][j]*ell^(j-1));
 );
 for(i=1,10,
  my(v=Mod(sum(j=1,18,W[2][i][j]*x^(j-1)),NL.pol),fac=idealfactor(NL,v));
  for(k=1,matsize(fac)[1],check(fac[k,1][1]==3 || fac[k,1][1]==53,"actual smaller-field S-unit support"));
  candidate_norms[i]=Str(nfeltnorm(NL,v));
  listput(candidate_divisors,vector(matsize(fac)[1],k,[fac[k,1][1],fac[k,1][3],fac[k,1][4],fac[k,2]]));
  for(a=0,2,U[15+3*(i-1)+a+1]=sum(j=1,18,W[2][i][j]*(b*xi^a)^(j-1)));
 );
 my(C=matrix(6,22),coordinates=matrix(15,22,i,j,W[5][i][j]),norms=vector(22),roots=vector(22));
 for(k=1,22,
  my(v=sum(i=0,8,sum(j=0,5,W[3][k][6*i+j+1]*b^i*xi^j)),pos=1,neg=1);
  for(i=1,45,if(W[4][k][i]>0,pos*=U[i]^W[4][k][i]);if(W[4][k][i]<0,neg*=U[i]^(-W[4][k][i])));
  check(v^3*neg==pos,"independent literal relative-ring cube identity");roots[k]=v;
  my(nr=prod(a=0,2,subst(lift(v),x,b*xi^(3*a))),nn=0);
  for(i=0,8,
   my(cc=polcoef(lift(nr),i));
   if(i%3,check(cc==0,"relative norm fixed by vertical automorphism"),nn+=subst(lift(cc),y,D[3])*D[4]^(i\3));
  );
  check(nn==W[6][k]*prod(i=1,15,D[7][i]^coordinates[i,k]),"literal lower-basis norm identity including sign");norms[k]=nn;
  my(ch=localnine(D,LD,nn));check(lift(Mod(ch,3))==vector(6),"literal root norm belongs to cubic norm subgroup");C[,k]=Col(ch/3);
 );
 my(ALL=concat(D[10],C),HN=mathnf(concat(3*matid(15),coordinates)),SN=matsnf(HN,1));
 check(matrank(Mod(ALL,3))==5 && lift(Mod(vector(6,i,1)*ALL,3))==vector(matsize(ALL)[2]),"actual five independent product-formula characters");
 check(abs(matdet(HN))==729 && SN[1]*HN*SN[2]==SN[3],"full embedded norm-unit lattice index and exact Smith maps");
 print("{\"type\":\"literal_unit_witness_verification\",\"cube_identities\":22,\"relative_norm_identities\":22,\"candidate_divisors\":",Vec(candidate_divisors),",\"candidate_absolute_norms\":",candidate_norms,",\"root_character_matrix\":",jmat(C),",\"with_included_lower_characters\":",jmat(ALL),",\"rank_mod3\":",matrank(Mod(ALL,3)),",\"minimum_proved_precision\":",E122WitnessPrecMin,",\"norm_lattice_HNF\":",jmat(HN),",\"norm_smith_left\":",jmat(SN[1]),",\"norm_smith_right\":",jmat(SN[2]),",\"norm_smith_diagonal\":",jmat(SN[3]),"}");
 writebin("e53_upper_witness_verify.bin",[C,ALL,HN,SN,roots,norms]);
 print("{\"type\":\"completion\",\"status\":\"PASS\"}");
}
quit;
