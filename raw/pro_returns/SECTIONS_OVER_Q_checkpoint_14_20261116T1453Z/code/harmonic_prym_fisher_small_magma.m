// Fisher's exact three-cover formula, with a small first covering.
// All Selmer and class-group computations use fresh default proof settings.
SetSeed(1);
Q := Rationals();
A<X> := PolynomialRing(Q);
K<t> := NumberField(X^2-2);
M := 7*13*23*139*1119169;
bE := 1146*(1+t)^2*M^2;
E := EllipticCurve([K|0,0,0,bE,0]);
S, StoA := TwoSelmerGroup(E);
print "SEL2 ORDER", #S;
print "ACTUAL SELMER ALGEBRA MODULUS", Modulus(Domain(StoA));
covers, maps, group_to_cover := TwoDescent(E : MinRed:=false);
P<Z> := PolynomialRing(K);
gs := [P!HyperellipticPolynomials(C) : C in covers];
II := -48*bE;
scales := [];
for i in [1..#gs] do
    g := gs[i];
    aa := Coefficient(g,4); bb := Coefficient(g,3);
    cc := Coefficient(g,2); dd := Coefficient(g,1); ee := Coefficient(g,0);
    Iraw := 12*aa*ee-3*bb*dd+cc^2;
    Jraw := 72*aa*cc*ee-27*aa*dd^2-27*bb^2*ee+9*bb*cc*dd-2*cc^3;
    assert Jraw eq 0;
    ok,rr := IsSquare(Iraw/II); assert ok;
    ok4,ss := IsSquare(rr);
    if not ok4 then ok4,ss := IsSquare(-rr); end if;
    assert ok4 and ss^4*II eq Iraw;
    gs[i] := gs[i]/ss^2;
    Append(~scales,ss);
end for;
F<ph> := quo<P|Z^3-3*II*Z>;
L<phL> := NumberField(Z^2-3*II);
Zinv := func<g | (4*Coefficient(g,4)*ph+3*Coefficient(g,3)^2-8*Coefficient(g,4)*Coefficient(g,2))/3>;
r := K!1119169;
g1 := r*(Z+1)^4-4*bE/r*Z^4;
zz1 := Zinv(g1);
found := false;
for i in [1..#gs] do
    zz2 := Zinv(gs[i]);
    if IsSquare(Coefficient(P!zz2,0)) or IsSquare(Coefficient(P!zz2,0)/573) then continue; end if;
    for j in [1..#gs] do
        zz3 := Zinv(gs[j]);
        pr := zz1*zz2*zz3;
        ok0,m0 := IsSquare(Coefficient(P!pr,0));
        okL,mL := IsSquare(Evaluate(P!pr,phL));
        if ok0 and okL then
            found := true; ii := i; jj := j;
            break;
        end if;
    end for;
    if found then break; end if;
end for;
print "FOUND TRIPLE", found, ii, jj;
assert found;
es := Eltseq(mL);
mf := F!m0 + (F!es[2])*ph + (F!((es[1]-m0)/(3*II)))*ph^2;
assert mf^2 eq pr;
aa := Coefficient(g1,4); bb := Coefficient(g1,3);
cc := Coefficient(g1,2); dd := Coefficient(g1,1); ee := Coefficient(g1,0);
G1 := (4*ph*bb+4*(bb*cc-6*aa*dd))/3;
G2 := (4*ph*cc+2*(2*cc^2-24*aa*ee-3*bb*dd))/3;
Hs := [zz1,G1/2,G2/6+2*(II-ph^2)/9];
fact := zz2*zz3/mf;
gamma := [Coefficient(P!(fact*h),2) : h in Hs];
// Substitute binary (X,Z)=(u,1-u), recovering C_r:N^2=r-4*bE/r*u^4.
ga := P![gamma[3],gamma[2]-2*gamma[3],gamma[1]-gamma[2]+gamma[3]];
print "COMMON I", II;
print "BINARY GAMMA", gamma;
print "SMALL COORDINATE GAMMA", Coefficients(ga);
print "HILBERT CHARACTER", Coefficient(gs[ii],4);
print "TRIPLE SQUARE ROOT", Eltseq(mf);
print "SECOND QUARTIC", Coefficients(gs[ii]);
print "THIRD QUARTIC", Coefficients(gs[jj]);
print "SECOND SCALE", scales[ii];
print "THIRD SCALE", scales[jj];
