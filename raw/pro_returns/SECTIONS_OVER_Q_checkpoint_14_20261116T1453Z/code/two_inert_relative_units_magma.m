// Search only for explicit units.  All resulting identities will be
// independently checked; no completeness assertion is used below.
SetSeed(3);
Q:=Rationals();R<X>:=PolynomialRing(Q);d:=649;
K<t>:=NumberField(X^9-3*d^6);O:=MaximalOrder(K);
G,cl:=ClassGroup(O:Bound:=1000,Proof:="Subgroup");
time U,um:=UnitGroup(O);
print "SEARCH UNIT GROUP",U;
for i in [1..Ngens(U)] do
  u:=K!um(U.i);
  assert Abs(Norm(u)) eq 1;
  print "EXPLICIT UNIT",i,Eltseq(u);
  print "UNIT NORM",i,Norm(u);
end for;
