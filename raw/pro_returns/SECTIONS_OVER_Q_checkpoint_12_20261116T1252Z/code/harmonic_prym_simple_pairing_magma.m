// Use a smaller literal two-cover for the image of the isogeny class r.
// The actual map to E is psi_b composed with the standard isogeny cover.
SetSeed(1);
Q := Rationals();
A<X> := PolynomialRing(Q);
K<t> := NumberField(X^2-2);
M := 7*13*23*139*1119169;
b := 1146*(1+t)^2*M^2;
E := EllipticCurve([K|0,0,0,b,0]);
time S, StoA := TwoSelmerGroup(E);
print "TWO SELMER ORDER", #S;
time covers, maps, group_to_cover := TwoDescent(E : MinRed:=false, RemoveTorsion:=true);
P<Z> := PolynomialRing(K);
r := K!1119169;
C := HyperellipticCurve(r-4*b/r*Z^4);
print "SMALL COVER", C;
EC, cm := AssociatedEllipticCurve(C : E:=E);
assert EC eq E;
print "SMALL COVER MAP", FactoredDefiningPolynomials(cm);
SetVerbose("CasselsTate",2);
time ct := CasselsTatePairing(C,covers[1]);
print "SMALL COVER PAIRING WITH COVER1", ct;
