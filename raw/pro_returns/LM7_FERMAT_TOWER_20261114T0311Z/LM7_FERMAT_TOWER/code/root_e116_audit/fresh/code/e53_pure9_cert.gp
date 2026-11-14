\\ First actual pure ninth-root field for ell53; separate bounded job.
default(parisize,128000000);
default(parisizemax,1000000000);
default(realprecision,100);
setrand(17611653);
{
 print("{\"type\":\"start\",\"field\":\"Q(ninthroot53)\",\"degree\":9}");
 my(B=bnfinit(x^9-53,1));
 print("{\"type\":\"uncertified_bnf_completed\",\"class_number\":",B.no,",\"cyclic\":",B.cyc,"}");
 my(c=bnfcertify(B));
 if(c!=1,error("unconditional certification failed"));
 my(Q=idealprimedec(B,3),T=idealprimedec(B,53));
 print("{\"type\":\"certified_field\",\"certification_flag\":0,\"certification_return\":",c,",\"class_number\":",B.no,",\"cyclic\":",B.cyc,",\"three_prime_ef\":",vector(#Q,i,[Q[i][3],Q[i][4]]),",\"ell_prime_ef\":",vector(#T,i,[T[i][3],T[i][4]]),"}");
 for(i=1,#Q,
  my(v=bnfisprincipal(B,Q[i],0));
  print("{\"type\":\"three_prime_class\",\"index\":",i,",\"class_coordinates\":",Vec(v),",\"ideal\":\"",Q[i],"\"}");
 );
 print("{\"type\":\"ell_prime_class\",\"coordinates\":",Vec(bnfisprincipal(B,T[1],0)),"}");
 writebin("e53_pure9_cert.bin",[B,Q,T]);
 print("{\"type\":\"completion\",\"status\":\"PASS\"}");
}
quit;
