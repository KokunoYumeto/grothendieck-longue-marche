// Only explicit conic points are requested.  Every output coordinate is
// substituted back into its equation by the independent certificate.
SetSeed(1);
Q:=Rationals(); P<t0>:=PolynomialRing(Q); K<t>:=NumberField(t0^2-2);
M:=7*13*23*139*1119169; b:=1146*(1+t)^2*M^2;
ds:=[K|3,191,23,139*(99+52*t),7*(1059+34*t),7*(1059-34*t)];
A<N,Z,V>:=PolynomialRing(K,3);
for i in [1..#ds] do
    d:=ds[i]; C:=Conic([K|1,-d,-b/d]);
    time ok,pt:=HasRationalPoint(C); assert ok;
    es:=Eltseq(pt); assert es[1]^2 eq d*es[2]^2+(b/d)*es[3]^2;
    print "CONIC",i;
    print "D",Eltseq(d);
    print "POINT",[Eltseq(x):x in es];
end for;
