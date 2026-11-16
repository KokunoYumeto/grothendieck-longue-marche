// Bypass the V2.30-1 number-field quartic minimisation error.
// Default proof settings; no conditional class-group bounds are enabled.
SetSeed(1);
Q := Rationals();
A<X> := PolynomialRing(Q);
K<t> := NumberField(X^2-2);
M := 7*13*23*139*1119169;
b := 1146*(1+t)^2*M^2;
E := EllipticCurve([K|0,0,0,b,0]);
time S, StoA := TwoSelmerGroup(E);
print "TWO SELMER", S;
print "TWO SELMER ORDER", #S;
print "TWO SELMER REPRESENTATIVES", [S.i@@StoA : i in [1..Ngens(S)]];
time covers, maps, group_to_cover := TwoDescent(E : MinRed:=false, RemoveTorsion:=true);
print "COVER COUNT", #covers;
print "COVER GROUP", Domain(group_to_cover);
print "COVER GROUP ORDER", #Domain(group_to_cover);
print "COVER MAP CODOMAIN", Codomain(group_to_cover);
