# Independent check of the module calculations on scans 024–025

This research-only check used the frozen TeX and the early research draft A11–A13 after context opening. It does not change a reading, supply missing geometric hypotheses, or claim a refutation of the full rigidification theorem. The context comparison is Hua, modernised reading of cote 91, II, “Une variante sous hypothèse de rigidité”, pages 23–24; its credited interpretation is the one tested in A11–A13.

## The mixed relation in A11

Let \(L=M=J=k\), \(i=\sigma=\mathrm{id}\), \(N=L'=0\), \(M'=N'=k\), \(d'=\beta=\mathrm{id}\), and \(\alpha=\pi'=\gamma=0\). Set the remaining maps \(d=i'=0\). Both rows are exact, all squares commute, \(\pi':k\to0\) retracts the zero inclusion, and \(\gamma:k\to0\) is surjective.

The joint maps are

\[
q:L\oplus M'\longrightarrow M,\quad q(a,b)=a+b,\qquad
\rho:L\oplus M'\longrightarrow J,\quad \rho(a,b)=a.
\]

Hence \(\rho(\ker q)=k\), while the two displayed proposed relation groups \(R_1\) and \(R_2\) vanish. The two equations for \(\mu\) at \(\lambda=\mathrm{id}_J\) force \(\mu=\mathrm{id}\) and \(\mu=0\). Thus the missing mixed relation is real under exactly these abstract hypotheses.

Surjectivity of \(\alpha\) would exclude this example and suffices abstractly for the proposed reduction: for \((l,m')\in\ker q\), lift \(l=\alpha l'\); then \(m'+i'l'\in\ker\beta\), and using the retraction identity gives \(\rho(l,m')=\sigma\alpha\pi'(m'+i'l')\). This makes the relation lie in \(R_2\). No claim is made that the source's geometric construction supplies this extra surjectivity.

## The universal quotient in A12

The relevant map has codomain \(M\oplus J\):

\[
(q,-\rho):L\oplus M'\longrightarrow M\oplus J.
\]

Maps from its cokernel to \(G\) are exactly pairs \((\mu,\lambda)\) satisfying \(\mu q=\lambda\rho\). Since \(q\) is surjective, inclusion of \(J\) into \(M\oplus J\) induces a canonical isomorphism

\[
J/\rho(\ker q)\ \simeq\ \operatorname{coker}(q,-\rho).
\]

The comparison with the source's \(\operatorname{coker}\rho\) fails in the elementary case \(L=M=J=k\), \(i=\sigma=\mathrm{id}\), \(N=0\), and all primed modules zero: the joint cokernel is \(k\), while \(\operatorname{coker}\rho=0\).

## Base change

For a fixed compatible module diagram, the joint cokernel commutes with arbitrary scalar extension. Although tensoring may destroy injectivity on \(\ker q\), right exactness still makes \(\ker(q\otimes B)\) the image of \((\ker q)\otimes B\), which suffices for the same quotient formula after base change. The caution about flatness in A13 applies to the separately proposed kernels \(R_1,R_2\) and the construction of geometric representing modules; it must not be read as a flatness restriction on this corrected fixed-presentation cokernel.

Confidence is high for all these module computations: each follows from the written maps and elementary exactness. The relation to a completed geometric obstruction theory remains conditional on the separate source obligations.
