default(parisize,128000000);
default(parisizemax,1000000000);
setrand(176111);
{
  my(P=polcyclo(9),B=bnfinit(P,1),F=B.nf,z=Mod(x,P));
  if(bnfcertify(B)!=1 || B.no!=1,error("certified cyclotomic class number"));
  my(Q=idealprimedec(F,3),T=idealprimedec(F,17));
  if(#Q!=1 || #T!=3,error("actual base prime counts"));
  my(U=concat([z],B.fu));
  U=concat(U,[1-z]);
  for(i=1,3,
    my(v=bnfisprincipal(B,T[i],1));
    if(#v[1],error("unexpected ideal class"));
    U=concat(U,[nfbasistoalg(F,v[2])]);
  );
  print("{\"type\":\"field\",\"polynomial\":\"",P,"\",\"class_number\":",B.no,",\"certification_flag\":0,\"certification_return\":1,\"unit_rank\":",#B.fu,",\"torsion_order\":",B.tu[1],",\"three_prime_count\":",#Q,",\"seventeen_prime_count\":",#T,"}");
  for(i=1,#U,
    my(u=U[i]);
    print("{\"type\":\"S_unit\",\"index\":",i,",\"coefficients\":",vector(6,k,Str(polcoef(lift(u),k-1))),",\"norm_to_Q\":",nfeltnorm(F,u),",\"three_valuation\":",idealval(F,u,Q[1]),",\"seventeen_valuations\":",vector(3,k,idealval(F,u,T[k])),"}");
  );
  for(i=1,#T,print("{\"type\":\"prime17\",\"index\":",i,",\"e\":",T[i].e,",\"f\":",T[i].f,",\"ideal_hnf_columns\":",vector(6,k,Vec(idealhnf(F,T[i])[,k])),"}"));
  print("{\"type\":\"prime3\",\"e\":",Q[1].e,",\"f\":",Q[1].f,",\"ideal_hnf_columns\":",vector(6,k,Vec(idealhnf(F,Q[1])[,k])),"}");
  writebin("e_nonunit_seventeen_base.bin",[B,z,U,Q,T]);
  print("{\"type\":\"completion\",\"status\":\"PASS\"}");
}
quit;
