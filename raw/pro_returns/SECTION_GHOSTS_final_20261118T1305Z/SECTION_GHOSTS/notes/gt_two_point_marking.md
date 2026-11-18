# E183: the literal two-point elliptic bridge

Completed on 18 November 2026. This is an independent marked comparison, not a citation to the missing historical double-cover covariance.

The actual two-pole torus group is \(B_4/\langle(abc)^4\rangle\). In its three-chain marking put \(\omega=(ab)^3\), \(d=\omega^2\), and \(y_3=ba^2b=\omega a^{-2}\). The pants path \(\{a,c\}\to\{a,d\}\to\{b,d\}\), with one A move followed by one S move, has the exact flat weight \(f(c,d)^{-1}f(a^2,b^2)^{-1}\).

The independently verified braid relation \((c\omega)^2=(\omega c)^2\) defines a homomorphism from the actual index-three mixed subgroup of \(B_3\), sending its two generators to \(c,\omega\). The uncapped E179 identity therefore gives \(f(c,\omega^2)=f(c^2,\omega)\). Removing the commuting \(a^{-2}\) input from \(f(y_3,c^2)\) is legal because \(f\) has zero exponent sums. Consequently the genus-one pants action and the standard genus-zero action differ by the single pure inner gauge \(g=f(\omega,c^2)\), on the whole completed actual group.

The exact path and generator identities are checked by code/check_gt_two_point_marking.py, using five literal identities and 43 defining braid-relation steps. Certificate SHA-256: 1cacc027efe676c6ec504960af38cf7791352c2bc046e9d43d3d00122733633c. This is a certificate in the presented ordinary braid group, not a test in selected finite quotients.

## Opened primary sources

- Schneps (2006), equation (1.3), printed p.657; the B4-center and two-pole torus marking, p.659. Primary author-hosted publisher PDF: https://webusers.imj-prg.fr/~leila.schneps/automorphisms.pdf . Opened refs turn111016760view0 and turn881180230view0; root independently reopened both locators.
- Hatcher, Lochak, and Schneps (2000), flat weights and formula (3), pp.18–19. Primary scan: https://webusers.imj-prg.fr/~pierre.lochak/textes/crelle.pdf . Source scope and visual checks are recorded in notes/gt_tower_repair.md.

## Independent checks and limit

Root fully read E183, checked the uncapped E179 input, independently reopened the precise primary locators, and reran the certificate positively. The cohomology agent fully read the proof and executable certificate and independently reran all five identities/43 steps with the same hash. Its review checked the actual mixed-subgroup homomorphism, central-input removal, and the order and purity of the common gauge. No error was found.

This closes the two-point marking comparison only. A higher-point elliptic-involution normalizer and branch quotient still require their own proof. No original finite compiler bound or historical CM conclusion is certified from E183 alone.
