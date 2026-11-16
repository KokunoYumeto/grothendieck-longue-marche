// Exact 2-coverings without the failing minimisation step.
// Compute their actual Cassels--Tate pairing with default proof settings.
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
print "COVER COUNT", #covers;
print "COVER GROUP", Domain(group_to_cover);
SetVerbose("CasselsTate",2);
time ct := CasselsTatePairing(covers[1],covers[2]);
print "CASSELS TATE PAIRING 1,2", ct;
