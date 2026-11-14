\\ Actual element witnesses only: no class/unit completeness is inferred from this BNF.
default(parisize,256000000);default(parisizemax,2000000000);
default(realprecision,100);setrand(176119);
check(a,s)=if(!a,error(s));
cf(a,n)=vector(n,i,Str(polcoef(lift(a),i-1)));
jmat(M)=vector(matsize(M)[1],i,Vec(M[i,]));
{
 my(CC=polcompositum(x^3-53,polcyclo(9),3),P=CC[1],alpha=CC[2],xi=CC[3],z=xi^3,beta=alpha*xi);
 check(Mod(x,P)==xi-alpha,"literal primitive element");
 my(B=bnfinit(P,1),Q=idealprimedec(B,3),T=idealprimedec(B,53),S=concat(Q,T),SU=bnfsunit(B,S),U=concat(concat([xi],B.fu),vector(#SU[1],i,Mod(SU[1][i],P))));
 check(#Q==3 && #T==3,"actual six places");
 print("{\"type\":\"candidate_elements\",\"polynomial\":\"",P,"\",\"candidate_class_number_unused\":",B.no,",\"candidate_class_cyclic_unused\":",B.cyc,",\"elements\":",#U,",\"scope\":\"only literal elements and their verified divisors are used\"}");
 writebin("e53_six_character_elements.bin",[B,alpha,xi,beta,Q,T,U]);
 my(a0=sqrtn(53+O(3^80),3),aa=lift(a0),lab=vector(3),C=matrix(6,#U),Vals=matrix(6,#U),py=polcyclo(9,'y));
 check(valuation(a0+1,3)==2,"53 ninth-power branch");
 for(j=0,2,
  my(vs=vector(3,k,idealval(B,alpha-aa*z^j,Q[k])),mx=vecmax(vs));
  check(mx>100,"actual wild branch label");
  for(k=1,3,if(vs[k]==mx,lab[j+1]=k));
  my(loc=Mod(y-a0*y^(3*j),py),nb=polresultant(py,1+a0*y^(1+3*j),'y));
  check(valuation(nb,3)==1,"norm uniformizer at each three-place");
  for(k=1,#U,
   my(v=idealval(B,U[k],Q[lab[j+1]]),uu=subst(lift(U[k]),x,loc),nu=polresultant(py,lift(uu),'y)/nb^v);
   check(valuation(nu,3)==0 && valuation(nu-1,3)>=2 && padicprec(nu,3)>=4,"wild cyclotomic norm precision");
   Vals[j+1,k]=v;C[j+1,k]=lift(Mod(-(lift(nu)-1)/9,3));
  );
 );
 for(j=1,3,
  my(pr=nfmodprinit(B,T[j],'t),zr=nfmodpr(B,z,pr));
  for(k=1,#U,
   my(v=idealval(B,U[k],T[j]),ur=nfmodpr(B,U[k]/beta^v,pr)^((53^2-1)/3),e=if(ur==1,0,if(ur==zr,1,if(ur==zr^2,2,error("tame cube root")))));
   Vals[j+3,k]=v;C[j+3,k]=lift(Mod(-e,3));
  );
 );
 for(k=1,#U,check(sum(j=1,6,C[j,k])%3==0,"actual product formula"));
 my(rank=matrank(Mod(C,3)));
 print("{\"type\":\"six_characters\",\"wild_labels_in_actual_prime_list\":",lab,",\"unit_columns\":",vector(#U,k,cf(U[k],18)),",\"S_valuation_matrix\":",jmat(Vals),",\"character_matrix\":",jmat(C),",\"rank\":",rank,"}");
 writebin("e53_six_character_witness.bin",[B,alpha,xi,beta,Q,T,U,lab,Vals,C]);
 print("{\"type\":\"completion\",\"status\":\"PASS\",\"actual_character_rank\":",rank,"}");
}
quit;
