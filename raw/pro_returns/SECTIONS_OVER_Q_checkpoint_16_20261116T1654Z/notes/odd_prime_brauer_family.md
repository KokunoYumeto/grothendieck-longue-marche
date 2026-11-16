# Odd-prime evaluation in the two-coordinate product-relation family

This completed local calculation belongs to the countable-puncture
investigation; it is not used in A.59.

Take coprime positive integers \(k>h\), and put
\[
d=k^2+h^2,\quad
a=\frac{k(k+h)}d,\quad b=\frac{h(k-h)}d=a-1,\quad
c=\frac{k(k-h)}d.
\]
On \(C:aX^4-bY^4=1\), write \(T=aX^4=1+bY^4\).
The rational point \(X=Y=1\) has \(T=a\). The fibre radicands at \(c\) are
\[
D_0=\frac{k-h}{k+h},\qquad D_1=-\frac{k+h}{k-h},\qquad D_0D_1=-1.
\]
Every joint fibre field therefore contains a primitive eighth root of unity.

## Proved identity at every odd prime

At each odd prime \(p\), every local point satisfies
\[
(T-c,2)_p=(a-c,2)_p.
\]
The formulas below are stated where the functions are nonzero; their
unramified evaluations extend the equality across removable zero or pole
points.

Only \(p\equiv3,5\pmod8\) needs proof. At these primes, \(2\) is a
nonsquare unit and \(-1\) is not a fourth power modulo \(p\).
Thus the symbol is determined by the parity of \(v_p(T-c)\).
We show
\[
v_p(T-c)\equiv v_p(a-c)=v_p(2kh/d)\pmod2.
\]

The cancellation test used in the cases below is exact: if \(T\) is closer
to \(c\) than both leading orders permit, then the leading units of the
two fibre ratios, after extraction of their fourth-power uniformizer
factors, are fourth powers in \(\mathbf F_p\). Their product is \(-1\),
which is impossible. The cases check that the root valuations are integers
before using this test.

1. Suppose \(p\nmid kh(k-h)(k+h)\), and put \(s=-v_p(d)\).
   Then \(v_p(a)=v_p(c)=s\). For \(x=v_p(X)\), the leading orders
   in \(T-c\) are \(s+4x\) and \(s\). If \(x\ne0\), the minimum has
   parity \(s\). If \(x=0\), cancellation beyond \(s\) makes both
   normalized fibre ratios fourth powers. For \(s<0\), \(T-1\) has
   the same order \(s\), so \(Y\) is a unit. For \(s=0\), \(c-1\) is
   a unit, and closeness to \(c\) again makes \(Y\) a unit.
   Cancellation is therefore impossible. Here \(v_p(a-c)=s\).

2. Suppose \(p\mid k\), and put \(s=v_p(k)>0\).
   Again \(v_p(a)=v_p(c)=s\), while \(b\) is a unit.
   Unequal leading orders have parity \(s\).
   For \(X\) a unit, extra cancellation would make
   \(D_0\equiv-1\pmod p\) a fourth power. Thus the required parity is
   \(s=v_p(a-c)\).

3. Suppose \(p\mid h\), and put \(s=v_p(h)>0\).
   Now \(a,c\) are units and \(v_p(b)=v_p(c-1)=s\).
   Use
   \[
   T-c=bY^4-(c-1).
   \]
   The orders are \(s+4v_p(Y)\) and \(s\). Unequal orders have parity
   \(s\); at equal orders, extra cancellation would make
   \(D_1\equiv-1\pmod p\) a fourth power. This gives the required
   parity \(s=v_p(a-c)\).

4. Suppose \(p\mid k+h\), and put \(e=v_p(k+h)>0\).
   The orders of \(a,b,c,c-1\) are \(e,0,0,e\).
   Put \(\tau=v_p(T)=e+4v_p(X)\).
   If \(\tau<0\), the equation \(T-1=bY^4\) forces
   \(\tau=4v_p(Y)\), so \(4\mid e\) and \(v_p(T-c)\) is even.
   If \(\tau>0\), then \(T-c\) is a unit.
   If \(\tau=0\), then again \(4\mid e\).
   When \(T-c\) is not a unit, compare \(T-1\) and \(c-1\):
   their orders are \(4v_p(Y)\) and \(e\).
   An unequal minimum is even; equality followed by further
   cancellation is excluded by the normalized fibre-ratio test.
   The parity is zero, as is \(v_p(a-c)\).

5. Suppose \(p\mid k-h\), and put \(e=v_p(k-h)>0\).
   The orders of \(a,b,c,c-1\) are \(0,e,e,0\).
   Now \(\tau=v_p(T)=4v_p(X)\).
   If \(\tau<0\), matching negative orders in \(T-1=bY^4\)
   forces \(4\mid e\); \(v_p(T-c)=\tau\) is even.
   If \(\tau=0\), then \(T-c\) is a unit.
   If \(\tau>0\), \(T-1\) is a unit, so
   \(e+4v_p(Y)=0\), again forcing \(4\mid e\).
   The two orders \(\tau,e\) in \(T-c\) have even minimum.
   Equality with further cancellation would make both normalized
   fibre ratios fourth powers and is impossible.
   The parity is again zero.

These cases exhaust the odd primes: coprimality of \(k,h\) prevents an
odd prime dividing \(d\) from dividing \(kh(k-h)(k+h)\).

## Exact relation and remaining scope

The available global norm identity relates two evaluation classes:
\[
(T-c)(T-(1-c))=ab((XY)^4+1),
\qquad
(XY)^4+1=((XY)^2+1)^2-2(XY)^2.
\]
The first formula uses \(c(1-c)=ab\).
Therefore the sum of the two quaternion classes is the constant class
\((ab,2)\). This formula alone does not prove that either individual class
is constant.

The preceding valuation argument proves that variation within this family
could occur only at two. The root's finite exact search found no such
variation; its code and output are retained under the
new_puncture_brauer_search filename. That finite search is not used as a
proof of two-adic constancy.
