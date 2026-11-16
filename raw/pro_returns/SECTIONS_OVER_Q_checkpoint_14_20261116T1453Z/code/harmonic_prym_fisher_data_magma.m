// Fisher, On binary quartics and the Cassels--Tate pairing, Theorem 3.1.
// Build the exact binary quadratic from the retained three covers.
SetSeed(1);
Q := Rationals();
A<X> := PolynomialRing(Q);
K<t> := NumberField(X^2-2);
M := 7*13*23*139*1119169;
bE := 1146*(1+t)^2*M^2;
E := EllipticCurve([K|0,0,0,bE,0]);
S, StoA := TwoSelmerGroup(E);
covers, maps, group_to_cover := TwoDescent(E : MinRed:=false, RemoveTorsion:=true);
P<Z> := PolynomialRing(K);
gs := [P!HyperellipticPolynomials(C) : C in covers];
invs := [];
for g in gs do
    aa := Coefficient(g,4); bb := Coefficient(g,3);
    cc := Coefficient(g,2); dd := Coefficient(g,1); ee := Coefficient(g,0);
    II := 12*aa*ee-3*bb*dd+cc^2;
    JJ := 72*aa*cc*ee-27*aa*dd^2-27*bb^2*ee+9*bb*cc*dd-2*cc^3;
    Append(~invs,<II,JJ>);
end for;
print "RAW INVARIANTS", invs;
II := -48*bE; JJ := K!0;
scales := [];
for i in [1..3] do
    assert invs[i][2] eq 0;
    ok,rr := IsSquare(invs[i][1]/II);
    assert ok;
    ok4,ss := IsSquare(rr);
    if not ok4 then ok4,ss := IsSquare(-rr); end if;
    assert ok4;
    assert ss^4*II eq invs[i][1];
    gs[i] := gs[i]/ss^2;
    Append(~scales,ss);
end for;
print "NORMALIZING SCALES", scales;
print "COMMON INVARIANTS", II,JJ;
F<ph> := quo<P|Z^3-3*II*Z+JJ>;
zgs := [(4*Coefficient(g,4)*ph+3*Coefficient(g,3)^2-8*Coefficient(g,4)*Coefficient(g,2))/3 : g in gs];
pr := &*zgs;
ok0,m0 := IsSquare(Coefficient(P!pr,0));
L<phL> := NumberField(Z^2-3*II);
okL,mL := IsSquare(Evaluate(P!pr,phL));
print "TRIPLE PRODUCT SQUARE FLAGS", ok0, okL;
if ok0 and okL then
    es := Eltseq(mL);
    mf := F!m0 + (F!es[2])*ph + (F!((es[1]-m0)/(3*II)))*ph^2;
    assert mf^2 eq pr;
    g := gs[1];
    aa := Coefficient(g,4); bb := Coefficient(g,3);
    cc := Coefficient(g,2); dd := Coefficient(g,1); ee := Coefficient(g,0);
    G1 := (4*ph*bb+4*(bb*cc-6*aa*dd))/3;
    G2 := (4*ph*cc+2*(2*cc^2-24*aa*ee-3*bb*dd))/3;
    Hs := [zgs[1],G1/2,G2/6+2*(II-ph^2)/9];
    fact := zgs[2]*zgs[3]/mf;
    gamma := [Coefficient(P!(fact*h),2) : h in Hs];
    print "SQUARE ROOT M", Eltseq(mf);
    print "GAMMA COEFFICIENTS x2,xz,z2", gamma;
    print "HILBERT CHARACTER", Coefficient(gs[2],4);
    for i in [1..3] do
        print "QUARTIC", i, Coefficients(gs[i]);
    end for;
end if;
