"""Render the fully specified A156 element from its exact certificate data."""
from pathlib import Path
import json

base=Path(__file__).resolve().parent
data=json.loads((base/'two_inert_norm2_generator_certificate_data.json').read_text())
B=10**40
rows=[]
for i,c in enumerate(data['generator_numerators']):
    sign='+' if c>0 else '-'
    z=abs(c);digits=[]
    for _ in range(4):digits.append(z%B);z//=B
    assert z==0
    rows.append((i,sign,*digits))

text=r'''\subsection{An exact extension of the first norm seed in the two-prime tower}

\begin{statement}{A.156}{Proved}
{An explicit integral norm-two generator at the first changed level}
Put \(d=649=11\cdot59\), and let
\[
 \begin{gathered}
 K_1=\Q(\alpha),\quad\alpha^3=3,\qquad
 K_2=\Q(t),\quad t^9=3d^6=224176165072750803,\\
 \alpha=t^3/d^2,\qquad
 \rho_1=d^8\alpha,\qquad\rho_2=d^2t.
 \end{gathered}
\tag{A.156.1}
\]
These are the actual first two fields in the tower for
\(a=3d^{24}\), since \(\rho_1^3=a\) and \(\rho_2^3=\rho_1\).
The element \(\gamma\) specified below is integral and satisfies
\[
                  N_{K_2/K_1}(\gamma)=\alpha-1,
                 \qquad N_{K_2/\Q}(\gamma)=2.
\tag{A.156.2}
\]
Its principal ideal is exactly the unique prime \(P_{2,0,2}\)
of residue degree one above two.
Consequently
\[
 \beta_0=-2,\qquad\beta_1=1-\alpha,\qquad\beta_2=-\gamma
\tag{A.156.3}
\]
is one actual two-step norm family:
\(N_{K_2/K_1}\beta_2=\beta_1\) and
\(N_{K_1/\Q}\beta_1=\beta_0\).
Each element is a unit away from the primes above two.
In particular the exact class \(e_2\) of A.155 is zero.
The theorem does not claim extension of this particular \(\beta_2\)
to every later level.
\end{statement}

Here is the complete element, using integer blocks to keep its
coefficients legible.  Put \(B=10^{40}\), \(D=d^5=115139273278249\), and
\[
 \gamma=D^{-1}\sum_{i=0}^{8}c_i t^i,\qquad
 c_i=\sigma_i(c_{i,0}+B c_{i,1}+B^2c_{i,2}+B^3c_{i,3}).
\tag{A.156.4}
\]
All entries in the following two tables are nonnegative integers;
\(\sigma_i\) is the displayed sign.
{\scriptsize
\[
\begin{array}{c|c|r|r}
i&\sigma_i&c_{i,0}&c_{i,1}\\\hline
'''
text+='\n'.join(f'{i}&{sgn}&{c0}&{c1}\\\\' for i,sgn,c0,c1,c2,c3 in rows)
text+=r'''
\end{array}
\tag{A.156.5}
\]
}
{\scriptsize
\[
\begin{array}{c|r|r}
i&c_{i,2}&c_{i,3}\\\hline
'''
text+='\n'.join(f'{i}&{c2}&{c3}\\\\' for i,sgn,c0,c1,c2,c3 in rows)
text+=r'''
\end{array}
\tag{A.156.6}
\]
}

\begin{proof}
The defining degree-nine polynomial is Eisenstein at three, so
the fields and degrees in (A.156.1) are as stated.
The equations for the old and new roots follow by taking the
indicated powers; in particular \([K_2:K_1]=3\).

There are two independent exact arithmetic checks of the element.
For the relative norm, put
\[
 A_j=D^{-1}\sum_{k=0}^{2}c_{j+3k}d^{2k}\alpha^k\quad(0\leq j<3),
 \qquad w=d^2\alpha.
\tag{A.156.7}
\]
Thus \(\gamma=A_0+A_1t+A_2t^2\) and \(t^3=w\).
Multiplying the three conjugates gives the literal cubic norm formula
\[
 A_0^3+wA_1^3+w^2A_2^3-3wA_0A_1A_2=\alpha-1.
\tag{A.156.8}
\]
Substitution of (A.156.5)--(A.156.6) and reduction by
\(\alpha^3=3\) verifies all three coefficients in this equality.
Since \(N_{K_1/\Q}(\alpha-1)=2\), it also gives the absolute norm.

To check integrality without using a class-group computation, form
the integer multiplication matrix \(H\), indexed by \(0\leq i,j<9\),
\[
 H_{ij}=\begin{cases}
             c_{i-j},&i\geq j,\\
             (3d^6)c_{9+i-j},&i<j.
          \end{cases}
\tag{A.156.9}
\]
Multiplication by \(\gamma\) in the basis \(1,t,\ldots,t^8\)
is exactly \(D^{-1}H\).
Writing
\(\det(ZI-H)=\sum_{j=0}^{9}h_jZ^{9-j}\), the retained exact
integer calculation verifies
\[
       D^j\mid h_j\ (0\leq j\leq9),\qquad
       \det(H)=2D^9.
\tag{A.156.10}
\]
Thus \(D^{-9}\det(DZI-H)\) is a monic polynomial in \(\Z[Z]\)
with constant coefficient \(-2\), annihilating \(\gamma\).
This proves integrality, and independently gives its norm two.
The full characteristic polynomial, the integer coefficients
\(h_j\), and the literal zero-remainder check are retained in
\path{code/two_inert_norm2_generator_certificate_data.json}.
The program
\path{code/two_inert_norm2_generator_certificate.py}
performs these divisions and determinant calculations over the
rationals and integers, without an analytic or class-group input.

The polynomial defining \(K_2\) has odd discriminant and reduces
modulo two to
\[
 X^9-1=(X-1)(X^2+X+1)(X^6+X^3+1).
\tag{A.156.11}
\]
The last factor is irreducible because the order of two modulo nine
is six, and the middle factor is irreducible of degree two.
Thus there is exactly one prime of norm two, namely the branch
used for \(P_{2,0,2}\) in A.155.
The integral principal ideal \((\gamma)\) has norm two by
(A.156.2), so it is exactly that prime.
Negation has relative norm minus one in the cubic extension.
Equation (A.156.8) therefore proves both norm compatibilities in
(A.156.3), with the fixed first element \(1-\alpha\).
\end{proof}

The element was located by a bounded search for principal relations.
Only its displayed coefficients and the subsequent integer/rational
certificate are used above.  The search's proposed class-group
presentation is not used as a class-number or completeness assertion.
The full search input, request, response and output are retained under
\path{code/two_inert_balanced_level2_magma_v3}.
'''
(base.parent/'sections/two_inert_norm2_generator_agent.tex').write_text(text)
print('Wrote A156 with every generator coefficient and the exact field/norm maps.')
