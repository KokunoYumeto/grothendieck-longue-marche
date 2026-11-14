default(parisize,128000000);
default(parisizemax,1000000000);
default(realprecision,100);
setrand(176110);
check(a,s)=if(!a,error(s));
coeffs(a,n)=vector(n,k,Str(polcoef(lift(a),k-1)));
{
  my(C=polcompositum(x^3-17,x^2+x+1,3),P=C[1],a=C[2],z=C[3]);
  my(B=bnfinit(P,1),F=B.nf,cert=bnfcertify(B));
  check(cert==1,"unconditional certification: default flag0, return1");
  check(a^3==17 && z^2+z+1==0 && z-a==Mod(x,P),"literal field maps");
  my(u1=((1-4*z)*a^2+(11+13*z)*a-35-7*z)/3);
  my(u2=((5+z)*a^2+(13+2*z)*a+35+7*z)/3);
  my(U=[z,u1,u2],I=[Mod(x,P),z-z*a,z-z^2*a]);
  my(V=matrix(3,3));
  print("{\"type\":\"field\",\"polynomial\":\"",P,"\",\"class_number\":",B.no,",\"class_cyclic\":",B.cyc,",\"certification_flag\":0,\"certification_return\":",cert,",\"signature\":",F.sign,"}");
  print("{\"type\":\"field_map\",\"alpha\":",coeffs(a,6),",\"zeta\":",coeffs(z,6),"}");
  for(i=1,3,
    my(u=U[i],v=bnfisunit(B,u),nu=prod(j=1,3,subst(lift(u),x,I[j])));
    check(#v==3,"actual ordinary unit coordinates");
    V[,i]=v;
    my(mp=minpoly(u),den=lcm(vector(6,k,denominator(polcoef(lift(u),k-1)))));
    check(denominator(Vec(mp))==1 && abs(polcoef(mp,0))==1,"monic integral unit polynomial");
    print("{\"type\":\"unit\",\"index\":",i,",\"coefficients\":",coeffs(u,6),",\"denominator\":",den,",\"minimal_polynomial\":\"",mp,"\",\"certified_unit_coordinates\":",Vec(v),",\"norm_to_K\":",coeffs(nu,6),"}");
  );
  check(abs(matdet(V[1..2,2..3]))==1,"free ordinary unit basis");
  check(gcd(V[3,1],3)==1,"primitive three-primary root");
  my(Q=idealprimedec(F,3),T=idealprimedec(F,17));
  check(#Q==3 && #T==1,"actual ramified-prime counts");
  print("{\"type\":\"primes\",\"three\":",vector(#Q,i,[Q[i][3],Q[i][4]]),",\"seventeen\":",vector(#T,i,[T[i][3],T[i][4]]),"}");
  writebin("e_pure_tower_base.bin",[B,a,z,U,V,Q,T]);
  print("{\"type\":\"completion\",\"status\":\"PASS\"}");
}
quit;
