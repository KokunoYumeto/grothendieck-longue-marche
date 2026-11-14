\\ Reuse the saved degree18 object. No bnfinit is launched here.
default(parisize,256000000);default(parisizemax,1000000000);
check(a,s)=if(!a,error(s));
jmat(A)=vector(matsize(A)[1],i,Vec(A[i,]));
{
 my(B=read("../inputs/e122_L2_candidate_bnf.bin"));
 print("{\"stage\":\"candidate_loaded\",\"class_orders_unused_until_certified\":",B.cyc,"}");
 my(cert=bnfcertify(B,1));check(cert==1,"flag-one natural class-presentation certification");
 print("{\"stage\":\"flag_one_return\",\"value\":",cert,"}");
 my(S=concat(idealprimedec(B,3),idealprimedec(B,53)),C=matrix(#B.cyc,#S));
 for(i=1,#S,C[,i]=bnfisprincipal(B,S[i],0));
 my(Rel=concat(matdiagonal(B.cyc),C),SN=matsnf(Rel,1),UF=SN[1],Diag=SN[3]);
 my(ds=vector(#B.cyc,i,Diag[i,matsize(Diag)[2]-#B.cyc+i]),ord=prod(i=1,#ds,ds[i]));
 check(ord==81,"independently proved full S-class order81");
 print("{\"stage\":\"S_class\",\"ordinary_presentation_orders\":",B.cyc,",\"S_columns\":",jmat(C),",\"relation_columns\":",jmat(Rel),",\"Smith_orders\":",ds,",\"Smith_forward\":",jmat(UF),",\"Smith_inverse\":",jmat(UF^-1),"}");
 my(rows=List(),pivot=List(),Qp=matrix(#ds,0));
 forprime(p=5,3000,
  if(p!=53 && p%9==4 && Mod(53,p)^((p-1)/3)!=1,
   my(m=(p-1)/3,bp=lift(Mod(53,p)^(3*lift(Mod(27,m)^-1))),PP=idealprimedec(B,p),hit=0);
   for(i=1,#PP,if(PP[i][4]==1 && idealval(B,Mod(x-bp,B.pol),PP[i])>0,check(!hit,"unique selected degree-one prime");hit=i));
   check(hit,"actual selected prime");
   my(cl=bnfisprincipal(B,PP[hit],0),sc=UF*cl);
   sc=vector(#ds,i,lift(Mod(sc[i],ds[i])));
   listput(rows,[p,bp,Vec(cl),sc]);
   my(qnew=concat(Qp,Col(sc)));
   if(matrank(Mod(qnew,3))>matsize(Qp)[2],listput(pivot,[p,bp,idealhnf(B,PP[hit]),Vec(cl),sc]);Qp=qnew);
   if(matsize(Qp)[2]==2,break);
  )
 );
 check(#pivot==2,"two actual pivot primes form a full C9-square basis");
 print("{\"stage\":\"pivot_candidates\",\"rows\":",Vec(rows),",\"pivot_primes\":",vector(2,i,pivot[i][1]),",\"pivot_residues\":",vector(2,i,pivot[i][2]),",\"pivot_ideals\":",vector(2,i,jmat(pivot[i][3])),",\"ordinary_columns\":",vector(2,i,pivot[i][4]),",\"S_columns\":",vector(2,i,pivot[i][5]),"}");
 writebin("e53_positional_pivots.bin",[B,S,C,UF,Diag,Vec(pivot),Vec(rows)]);
 print("{\"stage\":\"completion\",\"status\":\"PASS\",\"scope\":\"full S-class presentation only, with exact lower bound from E121; units not certified\"}");
}
quit;
