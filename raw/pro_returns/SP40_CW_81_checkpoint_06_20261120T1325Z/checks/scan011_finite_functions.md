# Scan011 — finite Hom argument-order computation

Executed: 2026-11-20 12:22:20 UTC.

Assign X={x}, Z={z0,z1}, E={e0,e1,e2}. Hom here is the explicitly enumerated set of all functions between these finite sets. A function is recorded by its ordered tuple of values. This calculation does not assign a meaning to the manuscript’s P or looped E; it selects no ink reading.

A=Hom(Z×X,E) has9 elements. B=Hom(X,Hom(Z,E)) has9 elements. The exact map T(a)(x)(z)=a(z,x) and inverse T⁻¹(b)(z,x)=b(x)(z) were enumerated over every element; both compositions returned the input.

C=Hom(X,Hom(E,Z)) has8 elements. The additional exact map R:A→C is given in the table: number A lexicographically from0 through8, reduce that index modulo8, and read its three binary digits as indices into Z in the order e0,e1,e2. Its image equals C. Its first and last input have the same image.

| a, values on (z0,x),(z1,x) | T(a), the single inner function’s values on z0,z1 | R(a), the single inner function’s values on e0,e1,e2 |
| --- | --- | --- |
| ('e0', 'e0') | ('e0', 'e0') | ('z0', 'z0', 'z0') |
| ('e0', 'e1') | ('e0', 'e1') | ('z0', 'z0', 'z1') |
| ('e0', 'e2') | ('e0', 'e2') | ('z0', 'z1', 'z0') |
| ('e1', 'e0') | ('e1', 'e0') | ('z0', 'z1', 'z1') |
| ('e1', 'e1') | ('e1', 'e1') | ('z1', 'z0', 'z0') |
| ('e1', 'e2') | ('e1', 'e2') | ('z1', 'z0', 'z1') |
| ('e2', 'e0') | ('e2', 'e0') | ('z1', 'z1', 'z0') |
| ('e2', 'e1') | ('e2', 'e1') | ('z1', 'z1', 'z1') |
| ('e2', 'e2') | ('e2', 'e2') | ('z0', 'z0', 'z0') |

The records N1 and N2 report these finite computations. They provide no general certification of the manuscript expressions and no reason to replace a written argument by an expected one.
