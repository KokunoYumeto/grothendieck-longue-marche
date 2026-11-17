# Generic retained-zero presentation: a useful exact change

Research after the final B108--B111 build. This is an algebraic change
of the generic annular presentation. The ten actual filled relations
must still be carried through it before making an assertion about the
filled annular centralizer. It adds no formal register row.

Use the complete q0-adapted basis in CE's actual certificate. Its cone
is C, its branch is F, and its other four ordinary generators are Ui.
The retained far-section loop is g0, with

    g0^-1 x g0 = Inn(CF)(x) for x=C,F;
    g0^-1 Ui g0 = Ui.

The actual even cone-source lift in this marking is h=g0 CFC. Thus

    [h,C]=1,
    h^-1 F h=CFC,
    h^-1 Ui h=(CFC)^-1 Ui(CFC).

Define k=hC and l=F^-1 h. The first relation gives [k,C]=1.
The second gives h C F=F h C, hence [k,F]=1. Since k also
commutes with h, it commutes with l. The same second relation gives
h(CFC)^-1=F^-1 h=l. Each last relation is consequently [Ui,l]=1.
Since h=g0 CFC, this also identifies l=g0 literally.

The inverse substitutions are

    h=kC,   F=k C l^-1,   g0=l.

Indeed [k,C]=[k,l]=1 makes k commute with F and h, and therefore
recovers h^-1 F h=CFC. The remaining four relations follow by
replacing l with h(CFC)^-1. Thus the two transformations are inverse
and every defining relation is recovered in both directions.

The generic annular orbifold group is therefore the graph product

    <C,k,l,U1,U2,U3,U4 |
       C^2=1, [k,C]=1, [k,l]=1, [l,Ui]=1 (i=1,2,3,4)>.

The orientation is epsilon(C)=epsilon(k)=1 and epsilon(l)=epsilon(Ui)=0.
The cone-source element is h=kC, not k alone. The ordinary source
therefore has the expected even character. A's ongoing relative-HNN
work may use this generic graph presentation, but a filled-group
conclusion requires simultaneous substitution of all ten actual
relations from inner_q0_adapted_basis22.json. B111 already rules out
simply transporting the slit centralizer unchanged.

Root sent this derivation to A for independent review. No numerical
or finite-quotient experiment is involved. Its current role is a
presentation change for the next annular calculation.
