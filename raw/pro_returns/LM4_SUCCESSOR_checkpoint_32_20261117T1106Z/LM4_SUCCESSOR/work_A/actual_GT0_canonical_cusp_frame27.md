# Canonical third-cusp frame: one literal full-word obstruction

Research, checkpoint27. This is an addendum to the separately reviewed `actual_GT0_third_cusp_half_rotation27.md`; that source and the V4/Fox source remain unchanged. It removes the two-branch normalization ambiguity by using the actual zero-abelianization cusp frame and A45's prescribed multiplier. It does not prove that the resulting obstruction vanishes.

## 1. There is one canonical zero-abelianization cusp reflection

Retain z=(xy)^-1 and tau=alpha v. The actual regular-pants property supplies h in F with

tau(z)=h^-1 z^-1 h.

As proved in the half-rotation note, r=h tau is an involution. On F_ab=Zhat², tau acts by negative-swap. Thus r²=1 implies

h_ab+tau(h_ab)=0,

so h_ab=(ell,ell) for a unique ell in Zhat. The actual element

h0=z^ell h

still satisfies the same cusp transport and has zero abelianization. It is independent of the original choice h: any other such h differs from it by left multiplication by an element of C_F(z)=closure<z>, whose abelianization is a unique multiple of (-1,-1). There is therefore exactly one h0 in the actual closed commutator subgroup F' satisfying this transport equation.

The actual one-section theorem and C_F(tau)=1 supply a unique q in F with

h0 tau=q tau q^-1,

or equivalently h0=q tau(q)^-1. Its abelianization has the form

q_ab=(t,-t), t in Zhat,

because h0_ab=0. Neither h0 nor q is supplied by an unproved positive peripheral conjugator; both are defined by the existing actual regular involution and its known single section class.

Put e=(xu)v and b=q^-1 e q as before. Then tau(b)=b^-1.

## 2. Actual mod-two homology selects one branch

Let d=d_alpha be A45's prescribed unit. Its dyadic component satisfies d=1 modulo4. In the actual semidirect homology quotient

G_v -> (F_ab/2F_ab) semidirect<v>,

v interchanges the two coordinate vectors X,Y. Since u is in F', e has image (X,v). The image of q is (t,t) modulo2 and is fixed by the swap. Hence b=q^-1 e q also has image (X,v).

The element (X,v) has square (X+Y,1) and fourth power1. Therefore, because d=1 modulo4,

b^d has image (X,v),
v b^d v has image (Y,v).

The actual canonical word d_d=x^d v has image (X,v), since d is odd. The two normalized equalities in the half-rotation note are consequently distinguished by this actual homology quotient: the second cannot hold. Thus the complete full third-cusp condition is equivalent to the SINGLE literal equality

x^d v = (q^-1 (xu)v q)^d

in the actual full group G_v. In that event the actual original F-conjugator is q^-1, and squaring gives

x^d u^-1 y^d u = q^-1 (xy)^d q.

The quotient used here is simply the stated actual mod-two homology action; no group enumeration, search, or finite testing has been performed.

## 3. A canonical full-group obstruction and its first coefficient

Define the actual even word

Omega_alpha=(x^d v) (q^-1 (xu)v q)^(-d) in F.

Both factors have the same nontrivial v-parity, so the product lies in F. The complete original negative-GT0 conjugacy criterion is equivalent to Omega_alpha=1. If it vanishes, C29 gives generation and hence the Fox unit B=1+(y-1)u_y. No converse from the Fox unit alone is asserted: the full third-cusp equation retains its marked content.

Its full ordinary abelianization is also explicit. Write n=(d-1)/2, which is even at2, and q_ab=(t,-t). In F_ab semidirect<v>,

b has coefficient (1-2t,2t),
b^d has coefficient (n+1-2t,n+2t),
x^d v has coefficient (d,0).

It follows that

(Omega_alpha)_ab=(n+2t,-n-2t).

Therefore vanishing of the full obstruction necessarily implies

t=-(d-1)/4.

The division by4 is well defined in Zhat because d-1 belongs to4Zhat; it is unique because Zhat is torsion-free. This is a necessary relation between two actual canonical data, the dihedral multiplier d and the abelianization of the unique regular cusp-frame q. It is not asserted to be independent of all previously established GT0 identities, and no actual involution violating it has been constructed. Even its validity would leave the full nonlinear word Omega_alpha to be tested.

## 4. Exact status

The previous existential full cusp conjugacy has become a single literal equality of actual uniquely normalized words, and its first abelian coefficient is retained. Neither equality nor coefficient vanishing has been proved. In particular this note supplies no Main-A decision and no all-P statement. It uses the actual negative-GT0 V4, the full primitive-cusp centralizer, the actual regular one-section theorem, and A45's exact full unit with dyadic residue1 modulo4. No change was made to the frozen V4/Fox note or half-rotation proof.
