# Actual C8 main component at residue two

Notes only; no new registered result. This computes a genuine positive-genus valuation of the nonstable curve `v²=w16−6w8+1`. It does not yet determine the remaining components, the graph, or cusp paths. All original normalizers are already A59, and pro2 fixedness is already A22.

Choose a with a³=18±6√3 and put c4=a(a³−24). The Deuring equation

    y²+a xy+y=x³

has c6=0 and discriminant a³−27, a unit at two, so it is a good model of E after a finite extension. With v2(2)=1, v2(a)=1/2. Choose beta with beta²=48/c4, then a square root u of beta. Set

    r=beta a²/12,
    x_old=beta(x+a²/12),
    y_old=u³(y+a x/2+1/2).

These satisfy y_old²=x_old³−x_old, as checked exactly in the certificate. We have v2(beta)=1. Moreover

    r²=a³/[3(a³−24)],

so r is a unit and v2(r²−1)=1. The two factors r−1,r+1 therefore both have valuation1/2. Let c=beta/(r−1). Then v2(c)=1/2, and the exact parameter equations give

    c(a−c)²=4.

Thus d=a−c has valuation3/4. The actual Kummer slope from the separate C8 map certificate becomes

    R=y_old/(x_old−1),
    R/R0=(1+a x+2y)/(1+c x)
         =1+[d x+2y]/(1+c x),
    R0=u³/[2(r−1)].

After adjoining a fourth root of R0, write the original Kummer coordinate as T with T⁴=R/R0. Choose rho⁴=d and put T=1+rho V. Its exact equation is

    (1+c x)[V⁴+4V³/rho+6V²/rho²+4V/rho³]
      =x+(2/d)y.

Here v2(rho)=3/16. The three lower binomial coefficients have valuations29/16,5/8,23/16, respectively, and v2(2/d)=1/4. All are integral and vanish in the special fibre. On the good affine elliptic chart, the special equations therefore are

    x=V⁴,  y²+y=V¹².

The special ring is integral. Its function field normalizes by

    Y=y+V⁶+V³,
    Y²+Y=V³.

This is a supersingular genus-one function field; moreover y=Y⁴ and x=V⁴. The actual main component consequently maps to the good base elliptic curve by the second Frobenius. The finite flat affine chart is regular at its special generic point because its special fibre is reduced; normalization/resolution preserves this positive-genus valuation. The comparison uses the same elementary valuation-to-component mechanism already written out in A52/A58/A61, not a claim of a complete stable model.

The executed certificate is `fgh_C8_good_two_main.py/.json/.out`. It checks the parameter relations, the actual elliptic coordinate change, the slope identity, every binomial coefficient, and the characteristic-two normalization and Frobenius identities.

## Remaining gate

The curve has genus7, so this accounts for only one of its seven genera. The exceptional fibre over the good base point O contains the four original branch/cusp points and can contain additional positive-genus components or graph homology. Neither the good main component nor the purely inseparable degree-four map proves compact type. A42 cannot be applied until the remaining six genera and the marked attachment paths are identified. Yu Yang's exact inertia formula remains available, but its actual component inertia inputs have not yet been computed.
