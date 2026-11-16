# Quadratic tensor obstruction over F₂

**Status: verified own calculation.** This is an editorial algebraic argument, not a claim that the manuscript contains the proof. No scan image was read and no transcription was edited.

## Exact hypotheses and conclusion

Let \(H=\mathbf F_2^2\), with ordered basis \(e,f\), quadratic form \(q(xe+yf)=xy\), and isometry \(s(e)=f,\ s(f)=e\). A candidate \(Q:H\otimes H\to\mathbf F_2\) is any quadratic form, including a degenerate one. There is **no** such \(Q\) satisfying both

\[
Q(v\otimes w)=q(v)q(w)\quad(v,w\in H),\qquad
Q((s\otimes\mathrm{id})z)=Q(z)\quad(z\in H\otimes H).
\]

Thus this example obstructs a tensor construction on quadratic forms that has the stated pure-tensor values and is natural even under this one isometry of a factor. It does not assert that no quadratic form can be placed on the tensor space, nor does it concern tensor products of symmetric bilinear forms.

## Polar-form proof

Write \(t_{00}=e\otimes e,\ t_{01}=e\otimes f,\ t_{10}=f\otimes e,\ t_{11}=f\otimes f\), and use the characteristic-two polar form

\[
B_Q(u,v)=Q(u+v)+Q(u)+Q(v).
\]

The pure-tensor condition gives \(Q(t_{ij})=0\). It also gives

\[
B_Q(t_{00},t_{01})=B_Q(t_{10},t_{11})=0,
\]

because the sums in these pairings are \(e\otimes(e+f)\) and \(f\otimes(e+f)\). Set \(x=(e+f)\otimes e=t_{00}+t_{10}\) and \(y=(e+f)\otimes f=t_{01}+t_{11}\). Then \(Q(x)=Q(y)=0\), while \(Q(x+y)=q(e+f)^2=1\); hence bilinearity gives

\[
1=B_Q(x,y)=B_Q(t_{00},t_{11})+B_Q(t_{10},t_{01}).
\]

Invariance of \(Q\) under \(s\otimes\mathrm{id}\) implies invariance of \(B_Q\), and that involution takes the ordered pair \((t_{00},t_{11})\) to \((t_{10},t_{01})\). The two terms on the right are therefore equal, so their sum is zero in \(\mathbf F_2\), a contradiction.

## Exhaustive coefficient check

Use coordinates \((z_0,z_1,z_2,z_3)\) in the ordered tensor basis above. Every quadratic form has a unique expression

\[
Q(z)=\sum_{i=0}^3 a_i z_i^2+\sum_{0\leq i<j\leq3}b_{ij}z_i z_j,
\qquad a_i,b_{ij}\in\mathbf F_2.
\]

These are all \(2^{10}=1,024\) candidates. Evaluating at the four basis tensors forces all \(a_i=0\); evaluating the four rank-one row/column sums forces \(b_{01}=b_{02}=b_{13}=b_{23}=0\). Evaluating at \((e+f)\otimes(e+f)\) forces \(b_{03}+b_{12}=1\). Consequently the only solutions of the pure-tensor condition are

\[
Q_0(z)=z_0z_3,\qquad Q_1(z)=z_1z_2.
\]

The involution sends \(z\) to \((z_2,z_3,z_0,z_1)\), so pullback exchanges these two forms. Neither is invariant. For example, \(z=(1,0,0,1)\) has \(Q_0(z)=1\), whereas its image \((0,1,1,0)\) has \(Q_0=0\).

The companion Python script independently evaluates all 16 ordered pairs \((v,w)\in H^2\) and all 16 ambient vectors for every candidate, checks the coefficient-condition characterization against the evaluation results, verifies the polar expansion for both surviving candidates, and compares the two binary forms below. It finds exactly **2** pure-tensor solutions and **0** invariant pure-tensor solutions; all assertions pass. The JSON output records every coefficient, the swapped solution, explicit invariance counterexamples, and the script’s SHA-256 hash.

## Same polar form, different isotropy

The forms \(q_0(x,y)=xy\) and \(q_1(x,y)=x^2+xy+y^2\) have the same polar form

\[
B((x,y),(u,v))=xv+yu,
\qquad
[B]_{e,f}=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

The polar form is nonsingular in both cases. However, \(q_0\) has the two nonzero isotropic vectors \(e,f\), while \(q_1\) equals \(1\) at each of \(e,f,e+f\), and hence is anisotropic over \(\mathbf F_2\). Therefore the polar form alone does not recover the quadratic form or its isotropy.

## Reproduction

From the extracted package directory, run:

```bash
python research/verify_f2_tensor_quadratic.py
```

It writes `f2_tensor_quadratic_results.json` beside the script. `--output PATH` selects a different JSON destination. The computation uses only Python’s standard library.
