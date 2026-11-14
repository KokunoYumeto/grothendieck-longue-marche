\\ Exact small pure/complex fields and literal unit-norm maps for E116.
default(parisize,128000000);
default(parisizemax,1000000000);
default(realprecision,100);
setrand(176116);
check(a,s)=if(!a,error(s));
cf(a,n)=vector(n,i,Str(polcoef(lift(a),i-1)));
jmat(M)=vector(matsize(M)[1],i,Vec(M[i,]));
{
 my(data=List(),trans=List());
 for(k=1,6,
  my(ell=[2,5,11,23,53,71][k],C=polcompositum(x^3-ell,x^2+x+1,3),P=C[1],a=C[2],z=C[3]);
  check(z-a==Mod(x,P),"literal primitive element");
  my(B=bnfinit(P,1),cert=bnfcertify(B),F=bnfinit(x^3-ell,1),fcert=bnfcertify(F));
  check(cert==1 && fcert==1,"unconditional default flag0 certification");
  check(B.no%3!=0 && F.no%3!=0,"first pure and complex three-classes");
  my(U=concat([z],B.fu),basis=[1,a,a^2,z,z*a,z*a^2],D=matrix(6,6,i,j,polcoef(lift(basis[j]),i-1)));
  my(uc=matrix(6,3),nk=vector(3),nf=vector(3),Fcoord=matrix(2,3));
  for(i=1,3,
   uc[,i]=matsolve(D,Col(vector(6,j,polcoef(lift(U[i]),j-1))));
   nk[i]=prod(j=0,2,subst(lift(U[i]),x,z-z^j*a));
   my(v=U[i]*subst(lift(U[i]),x,z^2-a),vc=matsolve(D,Col(vector(6,j,polcoef(lift(v),j-1)))));
   check(vc[4]==0 && vc[5]==0 && vc[6]==0,"actual quadratic norm lies in pure field");
   nf[i]=Mod(sum(j=1,3,vc[j]*x^(j-1)),F.pol);
   Fcoord[,i]=bnfisunit(F,nf[i]);
  );
  my(Q=idealprimedec(B,3),T=idealprimedec(B,ell),q=idealprimedec(F,3),tt=idealprimedec(F,ell));
  print("{\"type\":\"base_field\",\"ell\":",ell,",\"complex_polynomial\":\"",P,"\",\"complex_class_number\":",B.no,",\"complex_class_cyclic\":",B.cyc,",\"pure_class_number\":",F.no,",\"pure_class_cyclic\":",F.cyc,",\"certification_flag\":0,\"certification_returns\":[",cert,",",fcert,"]}");
  print("{\"type\":\"unit_coordinates\",\"ell\":",ell,",\"columns_in_1_a_a2_z_za_za2\":",vector(3,i,vector(6,j,Str(uc[j,i]))),",\"norm_to_K\":",vector(3,i,cf(nk[i],6)),",\"quadratic_norm_to_F\":",vector(3,i,cf(nf[i],3)),",\"pure_unit_coordinates\":",jmat(Fcoord),"}");
  print("{\"type\":\"primes\",\"ell\":",ell,",\"complex_three\":",vector(#Q,i,[Q[i][3],Q[i][4]]),",\"complex_ell\":",vector(#T,i,[T[i][3],T[i][4]]),",\"pure_three\":",vector(#q,i,[q[i][3],q[i][4]]),",\"pure_ell\":",vector(#tt,i,[tt[i][3],tt[i][4]]),"}");
  listput(data,[ell,B,F,a,z,U,uc,nk,nf,Fcoord,Q,T,q,tt]);
  if(ell==2 || ell==5,
   my(G=bnfinit(x^9-ell,1),gc=bnfcertify(G),R=matrix(1,4),N=vector(4));
   check(gc==1 && G.no%3!=0,"certified next pure field");
   for(i=1,4,
    N[i]=Mod(subst(polresultant(x^3-y,lift(G.fu[i]),x),y,x),F.pol);
    my(ex=bnfisunit(F,N[i]));check(#ex==2,"actual relative norm unit");R[1,i]=ex[1];
   );
   my(S=matsnf(R,1));check(S[1]*R*S[2]==S[3],"literal Smith maps");
   check(gcd(vector(4,i,R[1,i]))%3!=0,"onto three-adic pure norm");
   print("{\"type\":\"pure_transition\",\"ell\":",ell,",\"upper_polynomial\":\"",G.pol,"\",\"upper_class_number\":",G.no,",\"certification_return\":",gc,",\"lower_unit\":",cf(F.fu[1],3),",\"upper_units\":",vector(4,i,cf(G.fu[i],9)),",\"actual_norms\":",vector(4,i,cf(N[i],3)),",\"matrix\":",jmat(R),",\"smith_left\":",jmat(S[1]),",\"smith_right\":",jmat(S[2]),",\"smith_diagonal\":",jmat(S[3]),"}");
   listput(trans,[ell,G,R,N,S]);
  );
 );
 writebin("e_small_inert_units.bin",[Vec(data),Vec(trans)]);
 print("{\"type\":\"completion\",\"status\":\"PASS\",\"base_fields\":12,\"upper_pure_fields\":2}");
}
quit;
