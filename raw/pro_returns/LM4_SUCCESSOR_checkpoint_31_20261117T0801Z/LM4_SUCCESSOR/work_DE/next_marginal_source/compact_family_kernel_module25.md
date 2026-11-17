# The actual completed family-kernel abelianization

DE, 2026-11-17. Research only. This identifies the continuous abelianization of the actual closed filling kernel; it does not identify that kernel with the abstract full completion of the discrete kernel and does not solve the nonlinear fixed-source problem.

## 1. The actual closed kernels

Use the literal B123 free group
\[
 F=F(U_1,\ldots,U_8)*T,\qquad T=F(f,g,x),
\]
its free retraction \(\pi:F\to T\), and \(L=\ker\pi\). The actual all-source-orbit node subgroup is \(N\triangleleft F\), and \(W=F/N\). The complete discrete proof in CE's `family_kernel_schreier_and_abelianization25.txt` establishes
\[
 N\subseteq[L,L].
\]
This assertion concerns the entire defining normal closure, since every node is a commutator inside L and every signed source operator and ambient conjugation preserves [L,L]. It does not come from a bounded orbit check.

Let \(\widehat F\) and \(\widehat T\) denote the full completions. The literal retained free-factor section extends to a section of \(\widehat\pi\). Put
\[
 \mathcal L=\ker(\widehat F\to\widehat T),\qquad
 \mathcal N=\overline N\subseteq\widehat F.
\]
The finite-quotient universal property gives \(\mathcal L=\overline L\): finite quotients of F killing L are exactly finite quotients of T. The same property gives
\[
 \widehat W=\widehat F/\mathcal N,
 \qquad \mathcal J=\ker(\widehat W\to\widehat T)
                  =\mathcal L/\mathcal N.
\]
Here \(\mathcal J\) is the actual closed filling kernel, not a notation for \(\widehat J\). In particular no induced-topology assertion for the infinite discrete group J is used.

Set \(D=\overline{[\mathcal L,\mathcal L]}\). Since N is contained in [L,L],
\[
 \mathcal N\subseteq D.
\]
The image of D in \(\mathcal J\) is exactly its closed commutator subgroup: commutators map to commutators and the image of the compact group D is closed. Consequently
\[
 \mathcal J^{\mathrm{ab}}_{\mathrm{cont}}
 =\mathcal L/D.
\]
All quotient identities are identities of the actual compact groups.

## 2. Two inverse universal maps

Define the completed integral group ring and its free rank-eight module by
\[
 \Omega=\widehat{\mathbf Z}[[\widehat T]]
   =\varprojlim_{n,V}(\mathbf Z/n)[\widehat T/V],
 \qquad M=\Omega^8,
\]
where V runs over open normal subgroups of \(\widehat T\) and n over positive integers ordered by divisibility. We use left coefficients and write \(e_i\) for the eight distinguished module elements.

The module universal property used here is for **continuous compact modules**. If a profinite group acts continuously on a profinite abelian group A, invariant open subgroups of A are cofinal. Indeed, for an open subgroup B of A, compactness of the acting group and continuity at its product with 0 supply an open subgroup C with tC contained in B for every t. The invariant intersection of all tB contains C and is open. Finite quotients of A by these subgroups therefore define the continuous completed-group-ring action. A continuous equivariant assignment of the eight basis elements extends uniquely to a continuous homomorphism M to A.

There is a continuous homomorphism
\[
 \Phi:\widehat F\longrightarrow M\rtimes\widehat T,
 \quad U_i\longmapsto(e_i,1),\quad
 t\longmapsto(0,t)\quad(t=f,g,x).
\]
Its composite with the second projection is \(\widehat\pi\), so it sends \(\mathcal L\) into the abelian subgroup M and kills D. It induces
\[
 \overline\Phi:\widehat F/D\longrightarrow M\rtimes\widehat T.
\]

Conversely, the retained section splits \(\widehat F/D\) as
\((\mathcal L/D)\rtimes\widehat T\). Let \(A=\mathcal L/D\). For each i the continuous orbit map
\[
 t\longmapsto t\overline U_i t^{-1}
\]
defines the unique continuous \(\widehat T\)-module map \(M\to A\) taking \(e_i\) to \(\overline U_i\). Together with the retained section it defines
\[
 \Psi:M\rtimes\widehat T\longrightarrow\widehat F/D.
\]
Both composites are the identity on the eight family generators and three retained generators. These eleven elements topologically generate both groups: on the module side their conjugates contain every \(t e_i\), whose integral span is dense in M. Therefore the maps are inverse. Restricting to the kernels of the retained projections proves the exact continuous module identity
\[
 \boxed{\ \mathcal J^{\mathrm{ab}}_{\mathrm{cont}}
       =\mathcal L/D\cong\widehat{\mathbf Z}[[\widehat T]]^8.\ }
\]
This proof constructs the actual module directly. It does not interchange completion with the abelianization of an arbitrary infinite discrete subgroup.

## 3. Literal involution and continuous Tate groups

Let \(\beta=\delta_T\) be the continuous retained involution
\[
 \beta(f)=xgx^{-1},\quad \beta(g)=xfx^{-1},\quad \beta(x)=x^{-1}.
\]
The free-group formula, already valid before imposing node relations, is
\(\delta(U_i)=xU_{\bar i}x^{-1}\), where bar exchanges the two four-label sets. Under the module identification,
\[
 \delta(\lambda e_i)=\beta(\lambda)x e_{\bar i}
 \qquad(\lambda\in\Omega).
\]
This is a continuous semilinear equality, and its square is the identity because \(\beta(x)x=1\).

Let \(M_+\) be the first four coefficient summands. The map
\[
 M_+\times M_+\longrightarrow M,\qquad
 (a,b)\longmapsto a+\delta(b)
\]
is a continuous isomorphism of profinite abelian groups under which delta exchanges the two factors. Thus M is an induced compact \(C_2\)-module. The norm and difference formulas on the two coordinates give exactness directly: invariants are \((a,a)\), every such vector is a norm, and the kernel of the norm consists of \((a,-a)\), the image of \(1-\delta\). Consequently all continuous Tate groups of this actual abelianization vanish. No theorem about infinite discrete-module completion is required.

## 4. The source-level warning persists in a finite continuous quotient

The exact complete-input certificate `source_abelian_levels25.json` establishes that each of the twelve signed retained generator images preserves \(\chi_x:T\to\mathbf Z\), and all thirty-two family conjugator heads have \(\chi_x=0\). The four raw contact words have complete abelianizations equal to negative paired basis vectors, with first-half color levels 0 and second-half levels 1, one for each of a,B,d,e. These facts were independently reconstructed from the literal source words by DE's `verify_source_abelian_levels25.py`.

Extend \(\chi_x\) continuously to \(\widehat T\to\widehat{\mathbf Z}\), reduce modulo 2, and reduce coefficients modulo 2. This gives the explicit finite continuous module map
\[
 M\longrightarrow \bigl(\mathbf F_2[C_2]\bigr)^8.
\]
Every signed source operator acts trivially on these finite color/level coordinates. Hence the image of the actual closed source-family subgroup \(\overline I\) is exactly the span of the four paired vectors with first-half level0 and second-half level1. The invariant class
\[
 e_{(x,a)}+e_{(1,\bar a)}
\]
in M has the opposite levels and a nonzero coordinate outside that span. It remains outside the image of \(\overline I\), with a finite continuous detector; in particular the discrete support observation does not disappear merely by taking closures.

This is still only an assertion about the image in an abelian quotient. The displayed invariant class has **not** been lifted to an element of \(\mathcal J^\delta\). Continuous Tate vanishing of \(\mathcal J^{\mathrm{ab}}_{\mathrm{cont}}\) supplies no such nonlinear lift. Neither \(\mathcal J^\delta=\overline I\) nor its discrete counterpart is settled.

## 5. Evidence and scope

Inputs are the actual B123 free presentation and full signed-source operators, CE's complete family-kernel note and certificate, and the exact source-level certificate. The two inverse maps above are the proof of the completed module statement. All node and operator identities needed for the actual typing were independently replayed in `family_kernel_schreier_independent25.json`; the separate finite source-level replay is `verify_source_abelian_levels25.py/.out/.err`.

No new numbered statement or assembled source change is proposed this checkpoint. No infinite relation family, retained translate, or signed source operator is omitted.
