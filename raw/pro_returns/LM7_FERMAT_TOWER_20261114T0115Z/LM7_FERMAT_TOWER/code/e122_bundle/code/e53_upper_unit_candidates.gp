\\ Candidate elements in the smaller degree18 field only; no class/unit
\\ completeness is asserted from this uncertified BNF generation.
default(parisize,256000000);default(parisizemax,2000000000);
default(realprecision,100);setrand(12253);
check(a,s)=if(!a,error(s));
cf(a,n)=vector(n,i,Str(polcoef(lift(a),i-1)));
{
 my(P=x^18+53*x^9+2809);
 print("{\"type\":\"start\",\"polynomial\":\"",P,"\",\"degree\":18,\"scope\":\"candidate units only; no BNF class assertion\"}");
 my(B=bnfinit(P,1));
 writebin("e53_upper_unit_candidate_bnf.bin",B);
 print("{\"type\":\"candidate_bnf_return\",\"candidate_class_number_unused\":",B.no,"}");
 my(Q=idealprimedec(B,3),T=idealprimedec(B,53),SU=bnfsunit(B,concat(Q,T)),U=concat(B.fu,vector(#SU[1],i,Mod(SU[1][i],P))));
 my(V=matrix(#Q+#T,#U),NN=vector(#U));
 for(i=1,#U,
  my(I=idealfactor(B,U[i]),S=concat(Q,T));
  for(k=1,matsize(I)[1],check(I[k,1][1]==3 || I[k,1][1]==53,"actual S-unit divisor support"));
  NN[i]=Str(nfeltnorm(B,U[i]));for(k=1,#S,V[k,i]=idealval(B,U[i],S[k]));
 );
 print("{\"type\":\"verified_candidate_S_units\",\"elements\":",vector(#U,i,cf(U[i],18)),",\"absolute_norms\":",NN,",\"S_valuations\":",vector(matsize(V)[1],i,Vec(V[i,])),"}");
 writebin("e53_upper_unit_candidates.bin",[B,Q,T,U,V,NN]);
 print("{\"type\":\"completion\",\"status\":\"PASS\"}");
}
quit;
