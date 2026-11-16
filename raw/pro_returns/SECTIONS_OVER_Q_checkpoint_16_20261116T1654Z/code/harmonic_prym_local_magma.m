// Exact local information for the retained Prym factor.
// This uses Tate's algorithm; no rank or analytic assumption is requested.
Q := Rationals();
P<X> := PolynomialRing(Q);
K<t> := NumberField(X^2-2);
OK := Integers(K);
M := 7*13*23*139*1119169;
b := 1146*(1+t)^2*M^2;
E := EllipticCurve([K|0,0,0,b,0]);
P2 := Factorization(2*OK)[1][1];
info, Emin := LocalInformation(E,P2);
print "DYADIC LOCAL INFORMATION", info;
print "MINIMAL MODEL", aInvariants(Emin);
flag, iso := IsIsomorphic(E,Emin);
assert flag;
print "LITERAL ISOMORPHISM", iso;
print "MINIMAL DISCRIMINANT VALUATION", Valuation(Discriminant(Emin),P2);
print "MINIMAL C4 VALUATION", Valuation(cInvariants(Emin)[1],P2);
for p in [5,17,41] do
    for fac in Factorization(p*OK) do
        Ered, red := Reduction(E,fac[1]);
        print "GOOD REDUCTION", p, Norm(fac[1]), #Ered;
    end for;
end for;
print "DIVISION THREE", DivisionPolynomial(E,3);
print "THREE DIVISION FACTORS", Factorization(DivisionPolynomial(E,3));
