\\ Actual element and ideal witnesses; no unproved class/unit generation used.
default(parisize,128000000);
default(parisizemax,1000000000);
default(realprecision,100);
setrand(17611653);
check(a,s)=if(!a,error(s));
cf(a,n)=vector(n,i,Str(polcoef(lift(a),i-1)));
jmat(M)=vector(matsize(M)[1],i,Vec(M[i,]));
{
 my(V=read("e_small_inert_units.bin"),D);
 for(i=1,#V[1],if(V[1][i][1]==53,D=V[1][i]));
 my(F=D[3],B=bnfinit(x^9-53,1));
 writebin("e53_pure9_candidate.bin",[B]);
 print("{\"type\":\"candidate_saved\",\"class_data_status\":\"unproved\",\"class_number\":",B.no,",\"cyclic\":",B.cyc,"}");
 my(S=concat(idealprimedec(B,3),idealprimedec(B,53)),slo=concat(idealprimedec(F,3),idealprimedec(F,53)),U=vector(4));
 U[1]=F.fu[1];
 for(i=1,3,
  my(pr=bnfisprincipal(F,slo[i],1));check(#pr[1]==0,"certified lower principal S-prime");
  U[i+1]=nfbasistoalg(F,pr[2]);check(idealhnf(F,U[i+1])==idealhnf(F,slo[i]),"lower principal ideal identity");
 );
 my(su=bnfsunit(B,S),E=concat(B.fu,su[1]),R=matrix(4,#E),N=vector(#E),sgn=vector(#E),vv=matrix(#S,#E));
 for(i=1,#E,
  E[i]=nfbasistoalg(B,E[i]);
  my(I=idealhnf(B,1));
  for(j=1,#S,vv[j,i]=idealval(B,E[i],S[j]);I=idealmul(B,I,idealpow(B,S[j],vv[j,i])));
  check(I==idealhnf(B,E[i]),"actual upper element is an S-unit");
  N[i]=Mod(subst(polresultant(x^3-y,lift(E[i]),x),y,x),F.pol);
  my(v=N[i]);
  for(j=1,3,R[j+1,i]=idealval(F,N[i],slo[j]);v/=U[j+1]^R[j+1,i]);
  my(ec=bnfisunit(F,v));check(#ec==2,"certified lower ordinary unit coordinates");
  R[1,i]=ec[1];sgn[i]=v/U[1]^R[1,i];check(sgn[i]==1 || sgn[i]==-1,"literal norm reconstruction sign");
  print("{\"type\":\"actual_upper_S_unit_norm\",\"index\":",i,",\"element\":",cf(E[i],9),",\"S_valuations\":",Vec(vv[,i]),",\"relative_norm\":",cf(N[i],3),",\"lower_coordinates\":",Vec(R[,i]),",\"sign\":",lift(sgn[i]),"}");
 );
 my(H=matsnf(R,1));check(H[1]*R*H[2]==H[3],"actual norm Smith identity");
 print("{\"type\":\"norm_lattice\",\"lower_S_units\":",vector(4,i,cf(U[i],3)),",\"matrix\":",jmat(R),",\"left\":",jmat(H[1]),",\"right\":",jmat(H[2]),",\"diagonal\":",jmat(H[3]),"}");
 my(PC=matrix(#B.cyc,#S),PG=vector(#S));
 for(i=1,#S,
  my(pr=bnfisprincipal(B,S[i],1),I=idealhnf(B,1));PC[,i]=pr[1];PG[i]=nfbasistoalg(B,pr[2]);
  for(j=1,#B.cyc,I=idealmul(B,I,idealpow(B,B.gen[j],PC[j,i])));
  I=idealmul(B,I,idealhnf(B,PG[i]));check(I==idealhnf(B,S[i]),"actual S-prime class-coordinate relation");
  print("{\"type\":\"verified_class_coordinate_relation\",\"index\":",i,",\"coordinates\":",Vec(PC[,i]),",\"generator\":",cf(PG[i],9),",\"prime_ef\":[",S[i][3],",",S[i][4],"]}");
 );
 writebin("e53_pure9_norm_witness.bin",[D,B,S,U,E,R,N,H,PC,PG,sgn,vv]);
 print("{\"type\":\"completion\",\"status\":\"PASS\",\"class_data_status\":\"generation not certified; all displayed element/ideal identities independently checked\"}");
}
quit;
