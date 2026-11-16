// Actual genus-two quotient of the point-3 Fermat-eight cover.
// No analytic rank, GRH or BSD assumption is supplied.
SetSeed(1);
Q := Rationals();
R<x> := PolynomialRing(Q);
C := HyperellipticCurve(3*x^5-2*x);
J := Jacobian(C);
P := J![x-1,R!1];
print "CURVE", C;
print "POINT", P;
print "DOUBLE", 2*P;
for p in [5,7,11,13,17,19,23,29,31] do
    Cp := BaseChange(C,GF(p));
    Jp := Jacobian(Cp);
    Pp := Jp!P;
    print "REDUCTION", p, #Jp, Order(Pp);
end for;
time lo, hi := RankBounds(J);
print "RANK BOUNDS", lo, hi;
T, tm := TorsionSubgroup(J);
print "TORSION", T;
print "POINT TORSION", IsFiniteOrder(P);
