// Exact complementary elliptic factor of the harmonic genus-three curve.
// Public Magma calculator input; default class-group proof settings retained.
// No GRH, BSD, or unproved rank assumption is enabled.
SetSeed(1);
Q := Rationals();
A<X> := PolynomialRing(Q);
K<t> := NumberField(X^2-2);
M := 7*13*23*139*1119169;
b := 1146*(1+t)^2*M^2;
E := EllipticCurve([K|0,0,0,b,0]);
print "FIELD", K;
print "M", M;
print "CURVE", E;
print "TORSION BOUND", TorsionBound(E,10);
time ranks, points, sha := MordellWeilShaInformation(E : Effort:=1, RankOnly:=true);
print "RANK BOUNDS", ranks;
print "POINTS", points;
print "SHA INFORMATION", sha;
for P in points do
    assert P[2]^2*P[3] eq P[1]^3+b*P[1]*P[3]^2;
end for;
