# Finite relation-module frame extraction

Post-checkpoint11 research proposal; not inserted into frozen formal source.

Let Pi=C2 amalg C3 with generators s,r, and let q:Pi→Q be a finite
quotient which injects both factors. Put L=ker(q), d=1+|Q|/6, and

  G6=Pi / closure([L,L] L^6).

Then |G6|=|Q|·6^d. The exact exponent-six relative abelian quotient
is used, not its Q-coinvariant (scalar) quotient.

## Centralizers in one relative module level

The image of C_G6(s) in Q is exactly <s_Q>, and the image of
C_G6(r) in Q is exactly <r_Q>.

For p=2 or3, write a=s orr, respectively, and first work in
G_p=Pi/Phi_p(L). If m lifts an element centralizing a in G_p, then
q(m) centralizes a_Q. Thus a and m a m^-1 both lie in the open
subgroup J=q^-1(<a_Q>), even when m itself does not lie in J.
Their images in J/Phi_p(J) agree, since Phi_p(L) is contained in
Phi_p(J). Open profinite Kurosh writes J as a finite free profinite
product of C_p factors and a finite-rank full free profinite group.
The other source factor contributes no torsion because q injects it
and J/L has orderp. The free-product torsion theorem puts a and its
conjugate into C_p factors. Distinct factors, and distinct nonidentity
powers of a fixed factor generator, have distinct images in the
modp abelianization. Hence the two elements are J-conjugate. Their
transporter differs from m by an element of C_Pi(a)=<a>, so q(m)
lies in <a_Q>. The reverse inclusion is immediate. Since G6 maps
to both G_p, the assertion follows for G6.

## The action determines lower normalized frames

Suppose Q retains the standard S3 quotient and an automorphism b of
G6 induces the identity on S3. Whenever an induced action on Q is
used, stability of the kernel of G6→Q is an additional explicit
hypothesis; the frame uniqueness argument itself only uses the fixed
projection and its centralizer images. Suppose beta and J in G6 satisfy

  b(s)=beta s beta^-1,
  b(r)=J r^-1 J^-1,

with the prescribed S3 normalizations beta→1 and J→s. Any other
conjugator for the same equation differs on the right by the relevant
centralizer. Therefore the Q-image of beta is unique, and the
Q-image of J is unique: the only possible ambiguity lies in <s_Q>
or <r_Q>, respectively, and its intersection with the pure S3 kernel
is trivial.

If b^2=1 on G6, its two lower normalizer norms are automatically1:
b(beta)beta centralizes s, and b(J)J centralizes r. Their S3 images
are1, so the centralizer-image statements force their Q-images1.
Thus a next-level action both encodes the previous normalized frames
and enforces their norm equations.

## Scope and unresolved conversion gate

This is a general finite action-to-frame mechanism. Together with
A76 it explains why arbitrary scalar refinements can miss an order
obstruction: scalar quotients discard precisely the nontrivial
Q-action on the full relative relation module used above.

It does not yet convert the prescribed-frame A76 counterexample into
an unframed counterexample. That conversion would require an actual
involutory action on the next relative module quotient whose uniquely
induced lower frame is the bad one. Such an action has not been
constructed; its existence is a substantive additional gate.

Likewise, a successful frame at one finite level does not supply a
compatible family at all noncentral refinements. The independently
verified A76 frame reselection shows that the six-cup test alone does
not rule out every frame for the original finite action.
