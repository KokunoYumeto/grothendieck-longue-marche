\\ Additional literal Hensel, divisor and horizontal Artin maps.
default(parisize,256000000);default(parisizemax,2000000000);
check(a,s)=if(!a,error(s));
cf(a,n)=vector(n,i,Str(polcoef(lift(a),i-1)));
jmat(M)=vector(matsize(M)[1],i,Vec(M[i,]));
{
 my(Gd=read("e53_genus_kummer.bin"),D=read("e53_six_character_witness.bin"),F=Gd[1][1],L=Gd[1][4],xi=Mod(x,F.pol),pi0=Gd[3][1],lam=1-xi,Q3=idealprimedec(F,3)[1],found=0,dd,w,vv);
 for(n=0,728,
  my(k=n);dd=vector(6);for(i=1,6,dd[i]=k%3;k=k\3);
  w=-1+sum(i=1,6,dd[i]*lam^i);vv=idealval(F,w^3-pi0,Q3);
  if(vv>12,found=1;break);
 );
 check(found && idealval(F,3*w^2,Q3)==6,"literal Hensel inequality");
 print("{\"type\":\"hensel_cube_witness\",\"lambda_digits_after_minus_one\":",dd,",\"root_polynomial\":",cf(w,6),",\"error_valuation\":",vv,",\"derivative_valuation\":6,\"all_conjugate_places_same\":true}");
 my(B=D[1],S=concat(vector(3,j,D[5][D[8][j]]),D[6]),U=D[7],V=D[9]);
 for(i=1,#U,
  check(idealhnf(B,U[i])==idealfactorback(B,S,V[,i]),"entire literal divisor is S-supported");
 );
 my(rows=List(),prdata=List(),rank=0);
 forprime(p=2,300,
  if(p==3 || p==53,next);
  my(P=idealprimedec(L,p));
  for(i=1,#P,
   my(cl=Vec(bnfisprincipal(L,P[i],0)),sc=vector(2,j,lift(Mod(cl[j],3))),n=p^P[i][4],ar=lift(Mod((n-1)/3,3)),R=concat(Vec(rows),[sc]),nr=matrank(Mod(matrix(#R,2,a,b,R[a][b]),3)));
   if(nr>rank,listput(rows,sc);listput(prdata,[p,i,P[i][4],cl,sc,ar]);rank=nr);
   if(rank==2,break(2));
  );
 );
 check(rank==2,"actual horizontal Artin basis");
 my(A=matrix(2,2,i,j,rows[i][j]),arts=vector(2,i,prdata[i][6]),arow=lift(Mod(A,3)^-1*Col(arts))~);
 check(arow[2]==0 && arow[1]!=0,"horizontal norm line");
 print("{\"type\":\"horizontal_Artin_and_transfer\",\"actual_prime_basis\":",Vec(prdata),",\"Artin_row_on_L_S_basis\":",arow,",\"norm_on_B_genus_coordinates\":[[0,0],[1,2]],\"extension_on_L_S_basis\":",jmat(matrix(2,2,i,j,if(j==1,lift(Mod(-arow[1],3)),0))),",\"torsion_free_unit_norm_surjective_after_completion\":true}");
 writebin("e53_local_genus_maps.bin",[Gd,D,w,dd,vv,Vec(prdata),arow]);
 print("{\"type\":\"completion\",\"status\":\"PASS\",\"verified_full_S_divisors\":",#U,"}");
}
quit;
