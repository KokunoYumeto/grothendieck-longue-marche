// Search for an explicit principal-ideal certificate at the actual n=2 level.
// No class number or completeness assertion is drawn from the bounded search.
SetSeed(2);
Q:=Rationals(); R<X>:=PolynomialRing(Q);
d0:=11*59;
K<t>:=NumberField(X^9-3*d0^6);
O:=MaximalOrder(K);
print "FIELD", K;
print "ACTUAL RADICAND MAP: rho_2=d0^2*t; alpha=t^3/d0^2";
assert (d0^2*t)^9 eq 3*d0^24;
assert (t^3/d0^2)^3 eq 3;
print "DISCRIMINANT", Factorization(Discriminant(O));
print "MINKOWSKI BOUND", MinkowskiBound(O);
SetVerbose("ClassGroup",1);
time G,cl:=ClassGroup(O:Bound:=1000,Proof:="Subgroup",UsePowerProduct:=true);
print "BOUNDED RELATION SEARCH GROUP (NO COMPLETENESS CLAIM)", G;
rels:=[]; ideals:=[];
for q in [2,11,59] do
  dec:=Decomposition(O,q);
  degrees:=[Valuation(Integers()!Norm(z[1]),q):z in dec];
  print "LOCAL PRIME DATA",q,[(z[2],degrees[i]):i->z in dec];
  j:=Index(degrees,1); assert j ne 0;
  P0:=dec[j][1];
  if q eq 2 then P2:=P0; end if;
  for i in [1..#dec] do
    if i ne j then
      A:=dec[i][1]/P0^degrees[i];
      Append(~ideals,A);
      Append(~rels,(dec[i][1]@@cl)-degrees[i]*(P0@@cl));
    end if;
  end for;
end for;
C,pi:=quo<G|rels>;
e:=pi(P2@@cl);
print "BOUNDED BALANCED PRESENTATION", C;
print "IMAGE ORDER",Order(e);
if Valuation(Order(e),3) eq 0 then
  m:=Order(e);
  Z:=FreeAbelianGroup(#rels);
  f:=hom<Z->G|rels>;
  yes,v:=IsInImage(f,m*(P2@@cl));assert yes;
  cc:=Eltseq(v);
  A:=P2^m;
  for i in [1..#ideals] do A:=A*ideals[i]^(-cc[i]);end for;
  yes,gamma:=IsPrincipal(A);
  print "PRINCIPAL CERTIFICATE FOUND",yes;
  if yes then
    assert ideal<O|gamma> eq A;
    print "MULTIPLIER",m;
    print "BALANCED COEFFICIENTS",cc;
    print "GENERATOR POWER BASIS",Eltseq(K!gamma);
    print "GENERATOR NORM",Norm(K!gamma);
    print "EXACT IDEAL IDENTITY", Factorization(ideal<O|gamma>);
  end if;
end if;
