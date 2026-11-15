from pathlib import Path
import json
r=Path(__file__).resolve().parents[1]
p=r/'records/root_research_entries.json'
e=json.loads(p.read_text())
e=[x for x in e if not x['id'].startswith('O')]
WG='WG2 §2.4 #3 — unchecked planning question'
def add(i,scans,kind,quote,body,query,ctx,relation,ledger,confidence):
 e.append(dict(id=i,scans=scans,kind=kind,quote=quote,body=body,query=query,context=ctx,relation=relation,ledger=ledger,confidence=confidence))
add('O01','003, 007, 011–013, 027','own idea','Hom(X,Y)=A(X×Y); Δ_X',r'''Take the explicit graded algebra \(A=\mathbf Q[t]/(t^2)\), \(\deg t=2\), with \(\kappa(1)=0\), \(\kappa(t)=1\): the source's action sends \(u=a+b t_1+c t_2+d t_1t_2\) to
\[
\rho(u)(r+st)=(br+as)+(dr+cs)t,
\qquad \rho(u)=\begin{pmatrix}b&a\\d&c\end{pmatrix}.
\]
The inverse sends \(\begin{psmallmatrix}x&y\\z&w\end{psmallmatrix}\) to \(y+x t_1+w t_2+z t_1t_2\), and convolution against \(v=\alpha+\beta t_1+\gamma t_2+\delta t_1t_2\) has coefficients \((\beta a+\alpha c,\beta b+\alpha d,\delta a+\gamma c,\delta b+\gamma d)\), exactly the entries of \(\rho(v)\rho(u)\) in this inverse order.
Consequently the explicit map takes \(t_1+t_2\) to the identity, \(t_1t_2\) to \(L=E_{21}\), \(1\) to \(\Lambda=E_{12}\), \(t_1\) to \(\pi_0=E_{11}\), and \(t_2\) to \(\pi_2=E_{22}\); the five-element \(n=1\) basis in CT16/017 therefore gives a map \(\Phi\otimes\mathbf Q\to\operatorname{End}(A)\) with \(\pi_1\mapsto0\) and kernel \(\mathbf Q\pi_1\), since the other four images are independent matrix units.
This is a fully specified single-object comparison for the planning question, with the multiplication checked directly and with no attribution of a general motive construction to the manuscript.''',r'Phi|varphi_i|pi_0|pi_1|pi_2','CT16/015, matrix-unit multiplication; CT16/017, the explicit n=1 five-element basis; CT16/018, the ring-map setting','adds a concrete morphism, inverse on the kernel algebra, and kernel computation',WG+'; WG2 §6. #9 — unchecked planning question','High: the four coefficient calculations, inverse linear map and matrix-unit images are explicit; the contextual Φ comparison uses the unambiguous n=1 basis rather than the doubtful general index range.')
add('O02','007, 034, 038, 042','own idea','il suffit de connaître δ_*; Δ=δ_*(1)',r'''For the same \(A=\mathbf Q[t]/(t^2)\) and trace, multiplication \(\mu:A\otimes A\to A\) has the explicit trace adjoint
\[
\delta_*(1)=\Delta=1\otimes t+t\otimes1,
\qquad \delta_*(t)=t\otimes t,
\qquad \delta_*(a)=(a\otimes1)\Delta.
\]
The four products with \(b,c\in\{1,t\}\) verify \((\kappa\otimes\kappa)(\delta_*(a)(b\otimes c))=\kappa(abc)\), while \((t\otimes1)\Delta=(1\otimes t)\Delta=t\otimes t\), the flip fixes \(\Delta\), and \((\kappa\otimes1)\Delta=(1\otimes\kappa)\Delta=1\).
Both iterates applied to 1 equal \(1\otimes t\otimes t+t\otimes1\otimes t+t\otimes t\otimes1\), and both applied to t equal \(t\otimes t\otimes t\), which checks coassociativity in this example.
These displayed maps give a concrete test for the unfinished diagonal axioms on 042 and explain the same diagonal element's unit action in O01, without asserting a complete general axiom list.''',r'Poincar|associativ|reconstituer|diagon','CT16/025, reconstruction and separate associativity/Poincaré conditions; CT47/004, diagonal operations','adds a checked example for the proposed diagonal reconstruction','Hua, findings register, 11-simplicial-bivariant-poincare-equivalence — conjecture (unsearched); '+WG,'High: the formulas are checked on the two-element basis and all tensor basis products; no general classification is claimed.')
add('O03','034, 036, 038, 042','own idea','on trouve une équivalence; spécial',r'''For each nonempty finite set I let P(I) be its set of partitions and \(B(I)=\mathbf Q^{P(I)}\), all in degree zero, with \(\kappa_I(x)=\sum_{p\in P(I)}x(p)\); for \(\alpha:I\to J\), pullback of partitions gives \(q_\alpha:P(J)\to P(I)\), and the bivariant map \(B(J)\to B(I)\) has algebra component \(q_\alpha^*\) and fiber-sum component \(q_{\alpha*}\).
The identities
\[
q_{\alpha*}(xq_\alpha^*y)=(q_{\alpha*}x)y,
\quad \kappa_Iq_{\alpha*}=\kappa_J,
\quad q_{\beta\alpha}=q_\alpha q_\beta
\]
give both projection formulas, gauge compatibility and contravariant functoriality, and the coordinate dot-product pairings are perfect, so these are Poincaré algebras in the written finite-projective sense of 027.
Let C be the constant \(\mathbf Q\) functor and t_I the indiscrete partition: the maps \(\tau_I^*(x)=x(t_I)\), \(\tau_{I*}(a)=a1_{\{t_I\}}\) form a natural bivariant transformation \(\tau:C\to B\), because \(q_\alpha(t_J)=t_I\), but its one-point component is the identity and its two-point component has rank one between dimensions one and two.
Thus evaluation at a point fails to reflect isomorphisms on the unrestricted category described in the ledger excerpt, whereas the source's special map here is \(\mathbf Q\otimes\mathbf Q\to\mathbf Q^2\), \(a\otimes b\mapsto(ab,ab)\), and is not an isomorphism, so this calculation tests the need to retain “spécial” rather than deciding the intended special equivalence or the unseen full Hua card.''',r'simplicial|bivariant|Poincar|reconstituer','CT16/025, the closest Poincaré/reconstruction data; RESULTS_STATE Hua excerpt; no same finite-set construction in CT','adds an explicit counterexample to the unrestricted reading and a natural transformation witnessing the failure','Hua, findings register, 11-simplicial-bivariant-poincare-equivalence — conjecture (unsearched), intake “new to us”; '+WG,'High for the finite construction and failure to reflect isomorphisms, independently checked in records/partition_counterexample_review.md; medium for the intended scope of the source sentence, because “spécial” immediately precedes it and is not repeated there.')
add('O04','027, 031, 034, 042','own idea','produit fibré ... dim. correctes?; f_*(y)=yσ',r'''Write \(\mathbf Q_\lambda\) for the degree-zero algebra Q with trace \(\lambda\operatorname{id}\): the pair \((f^*,f_*)=(\operatorname{id},(\lambda/\mu)\operatorname{id})\) is an actual bivariant isomorphism \(\mathbf Q_\lambda\to\mathbf Q_\mu\), with inverse ratio \(\mu/\lambda\).
Use the square \(X'\xrightarrow{q}X\), \(Y'\xrightarrow{p}Y\), with vertical maps \(f':X'\to Y'\), \(f:X\to Y\), where \(X'=\mathbf Q_2\) and \(X=Y'=Y=\mathbf Q_1\): all pullbacks are identities, \(q_*=f'_*=2\operatorname{id}\), \(f_*=p_*=\operatorname{id}\), the square commutes, and its universal lift is \(h=q^{-1}u\) with \(f'h=p^{-1}fu=v\), proving that it is Cartesian.
All four assigned degrees are zero, yet
\[
p^*f_*=\operatorname{id}\ne2\operatorname{id}=f'_*q^*,
\qquad f^*p_*=\operatorname{id}\ne2\operatorname{id}=q_*f'^*.
\]
This is a concrete negative answer to the literal abstract sufficiency question in the gauge category and uses exactly the \(\sigma=2\) mechanism of 042; it does not transfer that conclusion to a geometric cohomology square with its specified trace normalizations.''',r'chgt\. de base|changement de base|trace|isom','CT47/004 and 007, base change in a specified geometric kernel setting; CT16/025, chosen pairing data','adds a Cartesian scalar-gauge test and identifies a normalization requirement in the abstract question',WG+'; '+ 'MPL_14_002-044 A36 — first-pass lead','High: inverse pairs, universal lift and both unequal composites are explicit and independently checked in records/gauge_basechange_review.md; scope is the gauge category actually defined on 027/034, with degree zero as in 036.')
add('O05','005, 007, 013, 019, 031, 034, 036','own idea','signe (−1)^{δj}; Il faut choisir',r'''Using the source's degrees \(|x|=i\), \(|y|=j\), \(\deg f_*=\delta\), the recorded left projection formula and graded commutation give the direct calculation
\[
f_*(x f^*y)=(-1)^{ij}f_*(f^*y\,x)
=(-1)^{ij}y f_*x
=(-1)^{ij+j(i+\delta)}f_*x\,y
=(-1)^{\delta j}f_*x\,y.
\]
This reproduces the exact exponent written in the margin on 034 and explains the disappearance of this factor under the even-degree restriction explicitly adopted on 031.
The calculation isolates one projection-formula sign; the earlier tensor-product retraction has its own recorded exponents and is not replaced by this calculation.''',r'anticommut|xy.*-y|alternée|signe','CT16/025, the explicit odd-product reversal; CT47/004, projection-formula use','restates the recorded sign with a degree-by-degree calculation',WG,'High: the two swaps give ij+j(i+δ)=δj modulo2; the statement is limited to the recorded projection-formula convention.')
add('O06','017, 027, 034, 042','own idea; unpursued implication','satisfaisant Künneth et Poincaré',r'''The degree-one comparison supplied by Oda is the canonical map \(M({}_pX)\xrightarrow{\sim}H^1_{\mathrm{DR}}(X)\) of left Dieudonné modules for the abelian variety over a perfect characteristic-p field treated in Corollary5.11, printed p.131, with \(VM({}_pX)\) mapping to \(H^0(X,\Omega^1)\).
This gives a precise input map for comparing the de Rham algebra in the final example with CT54/003–007's extension and Cartier-duality questions; the passage from degree one to the full bivariant power-system still requires the multiplication, trace and finite-set maps specified on 034–042.
Oda's next corollary specifies a canonical injection from the dual Dieudonné module of p-torsion in the Picard scheme for the general smooth proper case and identifies its image, so the supplied paper itself records which actual map must be used in that broader setting.''',r'Hodge.DeRham|Cartier|extension|Poincar','CT54/003, 005, 007; Oda1969, Corollaries5.11–5.12, printed131, supplied PDF page70; CN54:7 entries as leads','adds an explicit printed realization comparison to the abstract cohomology example','MPL_15_195-228+18_002-017 P01 and M07 — first-pass research-note leads; '+WG,'High for the map and filtration statement visually checked in the supplied PDF; medium for historical connection to cote11, because this packet does not name Oda, Dieudonné modules or Frobenius.')
add('O07','003, 005, 011–013, 021–025','unpursued implication','u(x)=p_{2*}(u p_1^*(x)); de type A′',r'''CT47/003 writes \(\Phi_{\mathcal L}(F)=\mathbf R p_{2*}(\mathbf Lp_1^*F\otimes\mathcal L)\), and taking its recorded K-class gives the actual comparison map
\[
[F]\longmapsto[\Phi_{\mathcal L}(F)]
=p_{2*}\bigl([\mathcal L]\,p_1^*[F]\bigr).
\]
This is the same pullback–kernel product–pushforward operator pattern displayed on 011, with the kernel identified explicitly as \([\mathcal L]\), and CT47/004 supplies the corresponding base-change, projection and Künneth calculation for its product assertion.
The comparison is through this written K-class map and its operations; no equivalence between a derived category and the general correspondence category is asserted.''',r'Phi|varphi|Künneth|formule de proj','CT47/003–004, the kernel functor and its K-class map; CN47:3 entries as leads','adds a direct application of the cote11 operator formula to a supplied neighboring kernel construction',WG+'; MPL_15_195-228+18_002-017 M07 — first-pass research-note lead','High for the displayed operator comparison, since CT47 names the K-class map and writes every operation; the source setup supplies its own relative/properness conditions.')
# Repair only research prose, never transcription.
for x in e:
 if x['id']=='H06':
  x['body']=x['body'].replace('p₂*(y)',r'\(p_2^*(y)\)').replace('κ_{X×Y}((\\(p_2^*(y)\\)u−u\\(p_2^*(y)\\))p₁*(x))',r'\(\kappa_{X\times Y}((p_2^*(y)u-up_2^*(y))p_1^*(x))\)')
 if x['id']=='RQ03':x['body']=x['body'].replace('The stronger formulation would be the factorization','The stronger formulation is the factorization')
p.write_text(json.dumps(e,ensure_ascii=False,indent=2)+'\n')
print(len(e),'root entries including calculations')
