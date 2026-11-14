\\ E119 exploratory exact lower fields; flag1 is only a class-presentation upper bound.
default(parisize,128000000);
default(parisizemax,1500000000);
default(realprecision,100);
setrand(176119);
check(a,s)=if(!a,error(s));
cf(a,n)=vector(n,i,Str(polcoef(lift(a),i-1)));
jmat(M)=vector(matsize(M)[1],i,Vec(M[i,]));
{
 my(ell=53,F=bnfinit(polcyclo(9),1),fc=bnfcertify(F));
 check(fc==1 && F.no==1,"full cyclotomic certification");
 my(xi=Mod(x,F.pol),z=xi^3,Q=idealprimedec(F,53),Q3=idealprimedec(F,3),S=concat(Q3,Q),SU=bnfsunit(F,S),U=concat(concat([xi],F.fu),vector(#SU[1],i,Mod(SU[1][i],F.pol))),C=matrix(#Q,#U));
 for(i=1,#Q,
  my(pr=nfmodprinit(F,Q[i],'t),zr=nfmodpr(F,z,pr));
  for(j=1,#U,
   my(v=idealval(F,U[j],Q[i]),r=nfmodpr(F,U[j]/53^v,pr)^((53^2-1)/3));
   C[i,j]=if(r==1,0,if(r==zr,1,if(r==zr^2,2,error("not cubic root"))));
  );
 );
 check(C==matrix(#Q,#U),"every cyclotomic S-unit is an actual local norm");
 print("{\"type\":\"cyclotomic_base\",\"polynomial\":\"",F.pol,"\",\"class_number\":",F.no,",\"flag0_return\":",fc,",\"prime_degrees\":",vector(#S,i,[S[i][3],S[i][4]]),",\"units\":",vector(#U,i,cf(U[i],6)),",\"tame_characters\":",jmat(C),"}");
 my(L=bnfinit(x^6+53*x^3+53^2,1),lc=bnfcertify(L),LS=concat(idealprimedec(L,3),idealprimedec(L,53)),LU=bnfsunit(L,LS));
 check(lc==1,"full first positional certification");
 print("{\"type\":\"positional_first\",\"polynomial\":\"",L.pol,"\",\"class_number\":",L.no,",\"class_cyclic\":",L.cyc,",\"flag0_return\":",lc,",\"S_class\":",LU[5][2],",\"S_prime_classes\":",vector(#LS,i,Vec(bnfisprincipal(L,LS[i],0))),",\"prime_degrees\":",vector(#LS,i,[LS[i][3],LS[i][4]]),",\"ordinary_units\":",vector(#L.fu,i,cf(L.fu[i],6)),"}");
 my(CC=polcompositum(x^3-53,x^3-3*x+1,3),P=CC[1],a=CC[2],theta=CC[3],R=bnfinit(P,1));
 check(a^3==53 && theta^3-3*theta+1==0,"literal real fixed-field embeddings");
 print("{\"type\":\"real_fixed_candidate\",\"polynomial\":\"",P,"\",\"signature\":",R.sign,",\"candidate_class_number\":",R.no,",\"candidate_cyclic\":",R.cyc,"}");
 writebin("e53_horizontal_candidate.bin",[F,U,C,L,LS,LU,R,a,theta]);
 my(rc=bnfcertify(R,1));check(rc==1,"certified natural class-presentation upper bound");
 my(RS=concat(idealprimedec(R,3),idealprimedec(R,53)),RPC=vector(#RS,i,Vec(bnfisprincipal(R,RS[i],0))),RU=bnfsunit(R,RS));
 my(Rrel=vector(#RS),Rpow=vector(#R.gen));
 for(i=1,#RS,
  my(I=idealdiv(R,RS[i],idealfactorback(R,R.gen,Col(RPC[i]))),pr=bnfisprincipal(R,I,3));
  check(pr[1]==Col(vector(#R.gen)),"fixed-field prime class relation");
  Rrel[i]=nfbasistoalg(R,pr[2]);
  check(idealhnf(R,Rrel[i])==idealhnf(R,I),"literal fixed-field prime ideal relation");
 );
 for(i=1,#R.gen,
  my(I=idealpow(R,R.gen[i],R.cyc[i]),pr=bnfisprincipal(R,I,3));
  check(pr[1]==Col(vector(#R.gen)),"fixed-field class power relation");
  Rpow[i]=nfbasistoalg(R,pr[2]);
  check(idealhnf(R,Rpow[i])==idealhnf(R,I),"literal fixed-field class power");
 );
 print("{\"type\":\"real_fixed_upper\",\"flag\":1,\"return\":",rc,",\"natural_upper_class_cyclic\":",R.cyc,",\"S_prime_classes\":",RPC,",\"candidate_S_class\":",RU[5][2],",\"prime_degrees\":",vector(#RS,i,[RS[i][3],RS[i][4]]),"}");
 print("{\"type\":\"real_fixed_literal_ideal_relations\",\"prime_relation_generators\":",vector(#Rrel,i,cf(Rrel[i],9)),",\"class_power_generators\":",vector(#Rpow,i,cf(Rpow[i],9)),",\"full_ideal_equalities_verified\":",#Rrel+#Rpow,"}");
 writebin("e53_horizontal_base.bin",[F,U,C,L,LS,LU,R,a,theta,RS,RPC,RU,Rrel,Rpow]);
 print("{\"type\":\"completion\",\"status\":\"PASS\"}");
}
quit;
