\\ Actual local ninth-norm subgroup for B3/B1 at the three primes over3.
default(parisize,256000000);default(parisizemax,2000000000);
check(a,s)=if(!a,error(s));
jmat(M)=vector(matsize(M)[1],i,Vec(M[i,]));
cf(a,n)=vector(n,i,Str(polcoef(lift(a),i-1)));
{
 my(pol=polcyclo(9,'y),F=nfinit(pol),xi=Mod(y,pol),la=1-xi,Q=idealprimedec(F,3)[1],bid=idealstar(F,idealpow(F,Q,16),2,9));
 my(a0=lift(sqrtn(53+O(3^25),3)),indices=concat(select(i->i%3!=0,vector(80,i,i)),[81]));
 check(valuation(a0^3-53,3)>=24 && valuation(a0+1,3)==2,"literal coherent rational cube root precision");
 check(idealval(F,la,Q)==1 && Q[3]==6 && Q[4]==1,"fixed local valuation");
 my(cyc=bid.cyc,lg4=ideallog(F,4,bid),all=vector(3));
 print("{\"type\":\"local_ninth_setup\",\"a0\":",a0,",\"a0_cube_error_valuation\":",valuation(a0^3-53,3),",\"modulus_exponent\":16,\"unit_orders\":",cyc,",\"unit_generators\":",vector(#bid.gen,i,cf(nfbasistoalg(F,bid.gen[i]),6)),",\"four_log\":",Vec(lg4),",\"indices\":",indices,"}");
 for(j=0,2,
  my(beta=a0*xi^(1+3*j),f=(x-1)^9-beta,logs=matrix(#cyc,#indices),norms=vector(#indices));
  check(idealval(F,beta+1,Q)==1,"Eisenstein local constant");
  for(k=1,#indices,
   my(nn=polresultant(f,1+x^indices[k],x));
   check(idealval(F,nn,Q)==0,"actual resultant is norm of unit");
   norms[k]=cf(nn,6);logs[,k]=ideallog(F,nn,bid);
  );
  my(H=mathnf(concat(matdiagonal(cyc),logs)),S=matsnf(H,1),diag=vector(#cyc,i,S[3][i,i]));
  check(abs(matdet(H))==9 && diag[1]==9 && prod(i=2,#cyc,diag[i])==1,"exact local norm quotient C9");
  my(v=lift(Mod(S[1][1,]*lg4,9)),cal=lift(Mod(4*(1+3*j),9)),row=lift(Mod(cal/Mod(v,9)*S[1][1,],9)));
  check(lift(Mod(row*logs,9))==vector(#indices),"character kills every literal norm");
  check(lift(Mod(row*lg4,9))==cal,"positive cyclotomic Artin calibration");
  all[j+1]=[beta,logs,H,S,row];
  print("{\"type\":\"local_ninth_norm\",\"label\":",j,",\"beta\":",cf(beta,6),",\"norm_coefficients\":",norms,",\"norm_logs\":",jmat(logs),",\"norm_HNF\":",jmat(H),",\"smith_left\":",jmat(S[1]),",\"smith_right\":",jmat(S[2]),",\"smith_diagonal\":",diag,",\"positive_character\":",row,",\"calibration_four\":",cal,"}");
 );
 writebin("e53_higher_local.bin",[F,xi,la,Q,bid,a0,indices,all]);
 print("{\"type\":\"completion\",\"status\":\"PASS\"}");
}
quit;
