# Actual Wajnryb sources for the remaining CM character

This work follows E63's frozen replay package. It changes no E63 file,
accepted certificate, assembler, report, or bibliography.

## 1. Primary reading and the exact target

Primary text: Lochak--Nakamura--Schneps,
*The Grothendieck--Teichmüller group GT-hat acts on the genus g mapping
class group with 0 or 1 marked point*, arXiv:2602.12462v1,
12 February 2026, https://arxiv.org/html/2602.12462v1 .
The existing bibliography key is `DE_LochakNakamuraSchneps2026`.
The inherited scope audits at root ledger entries85 and147 were read
before the new calculation.

The concrete input is Theorem3.1's generator presentation, Theorem1.1's
substitution, and the actual braid map of Lemma4.2/Corollary4.4.
The three- and four-genus additional relations are (C) and (C-prime).
Sections7--8 and AppendixA were read for the exact ribbon identities and
their limits: no cutting compatibility or NTY comparison is used here.

The displayed y_k in (3.1) has an extra final a_k; the formula used here
is the one explicitly used by Theorem1.1, Proposition4.3, and the
relation-(B) calculation in Corollary4.5:
`y_k=a_(k-1)...a_2 a_1^2 a_2...a_(k-1)`.
The certificate records this word in full.

## 2. Completed integral homology comparison (E72)

`code/de_wajnryb_homology.py/.out/.err/.json/.npz` is a new independent
integral calculation. Its only finite input is the retained old Sp4(F3)
model, plus the read-only six-coset word implementation. All input hashes
are verified again at completion.

For the skew chain matrix J_n and T_v=I+vv^t J_n, take a_i=T_(e_i),
d=T_(e1+e3). All A/B/C relations hold over the integers; the literal d3
word is T_(e1+e3+e5). The same program also checks genus2 and genus4,
including C-prime, in both column and transposed right-action conventions.

The new genus3 evaluation pairs k=5,6 have exact integral block maps
through the old pairs k=3,4. The change of basis is

`P1=(e1+e3,e4,e5,e6,e1,e2)`.

It sends `(Y5,A5^2)` to `(Z3,B3^2) plus (-I2,I2)` and `(Y6,A6^2)`
to `(Z4,B4^2) plus (-I2,I2)`. This extra sign is already the character
on the old stable line Ze1. The first three evaluations are recovered
through `P0=(e1,e2,e3,e4,e1+e3+e5,e6)`.
Therefore the five new evaluation kernels equal the three old kernels
over every integer modulus, including their actual induced B kernels.
There is no independent parity coordinate to adjoin.

The finite orientation/source check reconstructs all90 coordinates for
s,r,r^-1 on six cosets and five evaluations, using728 nonzero vectors.
The degree21840 source arrays satisfy s^2=r^3=1. Run PASS in0.189286s.
The complete proof is `sections/E_wajnryb_homology_agent.tex` (E72).
This settles this particular attempted new homology source: on the
previous same-Galois-value families it adds no CM restriction.

## 3. Next exact nonlinear representation

A preliminary free-word calculation has passed the following explicit
automorphisms of F_(2g)=<u1,...,u_(2g)> for g=2,3. For i<2g,

`a_i: u_i -> u_i u_(i+1)^-1 u_i, u_(i+1) -> u_i`,

fixing the other generators. The final chain generator sends
`u_j -> u_j u_(2g)^-1` for j<2g and fixes u_(2g). Put
`w=u1 u2^-1 u3 u4^-1`; d sends `u_j -> w u_j` for j<=4 and fixes
the remaining generators. Every inverse is explicit.
The full A/B/C relations have been checked by literal free reduction,
not solely by abelianization. A saved reproducible word certificate and
finite characteristic quotient are the next work; no outcome of that
finite source is claimed here yet.

The one-boundary source and the marked-point quotient must be kept typed.
The original Wajnryb convention is one boundary (publisher primary:
https://msp.org/gt/1999/3-1/gt-v3-n1-p17-p.pdf, introduction p406).
LNS's introduction describes a marked point, whereas its algebraic
proof checks the explicit A/B/C presentation. The immediate calculation
uses precisely that presentation; the capping/outer morphism will be
retained before assigning marked-point notation to a nonlinear target.
