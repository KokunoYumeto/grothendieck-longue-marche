\\ Convert the exact roots to the literal (beta2,xi) relative basis and
\\ express every root norm in the already certified complete lower basis.
default(parisize,512000000);default(parisizemax,3000000000);
check(a,s)=if(!a,error(s));
cf(a,n)=vector(n,i,Str(polcoef(lift(a),i-1)));
jmat(M)=vector(matsize(M)[1],i,Vec(M[i,]));
{
 my(SS=read("e53_upper_exact_roots.bin"),R=SS[#SS],N=R[1],xi=R[2],beta=R[3],E=read("../inputs/e119_e53_genus_transition.bin"),D=E[1],B=D[1],U=D[7],V=D[9],W=read("e53_upper_unit_candidates.bin"));
 check(#SS==22 && #R[7]==22,"complete literal root stream");
 my(RB=matrix(54,54,i,j,polcoef(lift(beta^((j-1)\6)*xi^((j-1)%6)),i-1)),RI=RB^-1,rels=vector(22),coords=matrix(15,22),signs=vector(22),SV=V[,10..15]);
 check(RB*RI==matid(54),"exact relative field basis and inverse");
 for(k=1,22,
  my(v=R[7][k][2],r=RI*Col(vector(54,i,polcoef(lift(v),i-1))),nr=Mod(sum(i=1,18,R[8][k][2][i]*x^(i-1)),B.pol));
  check(RB*r==Col(vector(54,i,polcoef(lift(v),i-1))),"relative cube-root coordinates");rels[k]=vector(54,i,Str(r[i]));
  my(vals=Col(vector(6,i,idealval(B,nr,if(i<=3,D[5][D[8][i]],D[6][i-3])))),sv=SV^-1*vals);
  check(denominator(sv)==1,"actual norm S-valuation coordinates");
  my(u=nr/prod(i=1,6,U[9+i]^sv[i]),ex=bnfisunit(B,u));
  check(#ex==9,"actual lower ordinary unit coordinates");
  my(rr=u/prod(i=1,8,U[1+i]^ex[i]),found=-1,sgn=0);
  for(a=0,8,if(rr==D[3]^a,found=a;sgn=1);if(rr==-D[3]^a,found=a;sgn=-1));
  check(found>=0,"literal xi coordinate and prime-to-three sign");
  coords[,k]=concat(concat([found]~,ex[1..8]),sv);signs[k]=sgn;
  check(nr==sgn*prod(i=1,15,U[i]^coords[i,k]),"full exact root-norm exponent identity");
 );
 my(Full=concat(3*matid(15),coords),HN=mathnf(Full),rk=matrank(Mod(coords,3)));
 print("{\"type\":\"relative_root_witnesses\",\"relative_order\":\"beta2^i*xi^j, i=0..8 then j=0..5\",\"roots\":",rels,",\"exponents\":",R[5],",\"lower_norm_coordinates\":",jmat(coords),",\"lower_norm_signs\":",signs,",\"norm_lattice_HNF\":",jmat(HN),",\"norm_lattice_index\":",abs(matdet(HN)),",\"norm_coordinate_rank_mod3\":",rk,"}");
 writebin("e53_upper_witness_export.bin",[rels,R[5],coords,signs,HN,RB,RI]);
 print("{\"type\":\"completion\",\"status\":\"PASS\"}");
}
quit;
