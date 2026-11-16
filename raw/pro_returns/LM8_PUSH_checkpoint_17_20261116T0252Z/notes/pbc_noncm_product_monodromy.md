# Product monodromy for non-CM elliptic factors

Notes-only structural lemma requested by FGH. This is not a new registered statement.

## Exact assertion

Let \(E_1,\ldots,E_s\) be geometrically pairwise nonisogenous elliptic curves over a number field, all without CM. Fix a prime \(\ell\), and put \(V_i=T_\ell(E_i)\otimes\mathbb Q_\ell\). The connected derived algebraic monodromy group on \(\bigoplus_i V_i\) is the product \(\prod_i\mathrm{SL}(V_i)\). For repeated geometric isogeny classes, pass to a finite extension defining the chosen isogenies; the same group acts by its standard two-dimensional representation with the prescribed multiplicities.

On every ordinary tensor space of total degree \(d\) built from these \(V_i\), its derived-group invariant subspace is zero unless every factor's multidegree is even. On the nonzero invariant subspace the actual Galois action, after the above finite extension, is the scalar \(\chi_\ell^{d/2}\). Thus it is a direct sum of copies of the corresponding Tate representation. The convention is homological Tate modules; dual cohomology reverses the twist. An additional CM factor can be retained separately: the connected derived group acts trivially on it, and this lemma controls the non-CM tensor slots.

## Proof without an independence assumption

1. Let \(H\) be the Zariski closure of the Galois image in \(\prod_i\mathrm{GL}(V_i)\). Faltings' semisimplicity theorem makes \(H^\circ\) reductive: its faithful defining representation is semisimple. Serre's open-image theorem makes every projection \(H^\circ\to\mathrm{GL}(V_i)\) surjective. The determinants of all blocks are the same cyclotomic character.

2. The Lie algebra of \((H^\circ)^{\mathrm{der}}\) is therefore a semisimple subdirect product of the simple Lie algebras \(\mathfrak{sl}(V_i)\). The elementary Lie-Goursat argument says that it is a product of diagonally identified simple factors. To see the needed dichotomy, project to a pair of simple factors. A proper subdirect projection is the graph of an isomorphism, because both quotient kernels are ideals in a simple Lie algebra. Induction on the number of factors then decomposes the full subdirect algebra into diagonal blocks; if all pair projections are full, the full product is obtained.

3. Suppose two different indices occur in one diagonal block. Every automorphism of the split Lie algebra \(\mathfrak{sl}_2\) over the characteristic-zero field \(\mathbb Q_\ell\) is inner, so the two standard modules admit an invertible intertwiner \(T:V_i\to V_j\) for the derived Lie algebra. The center of \(\operatorname{Lie}H^\circ\) acts by scalars in every block: its image centralizes the full \(\mathfrak{sl}(V_i)\). Equal determinants imply equal traces, and therefore equal scalar actions on \(V_i,V_j\). Consequently \(T\) intertwines the entire Lie algebra of \(H^\circ\).

4. In characteristic zero, an element of a finite-dimensional rational representation of a connected algebraic group fixed by its Lie algebra is fixed by the group. Thus \(T\) is fixed by \(H^\circ\) in \(\operatorname{Hom}(V_i,V_j)\). After a finite extension of the number field, the Galois image lies in \(H^\circ\). Faltings' Hom theorem then identifies \(T\) with an element of \(\operatorname{Hom}(E_i,E_j)\otimes\mathbb Q_\ell\). In particular that Hom group is nonzero, and a nonzero morphism between elliptic curves is an isogeny. This contradicts geometric nonisogeny. No diagonal block can contain two distinct geometric isogeny classes.

5. Hence the derived Lie algebra is the full product. The connected derived algebraic subgroup lies in \(\prod_i\mathrm{SL}(V_i)\) and has its full Lie algebra, so it is precisely that product. This conclusion does not assume a priori that distinct elliptic factors are independent.

6. For multiplicities, choose all geometric isogenies over one finite extension. Their maps identify each isotypic summand with \(V_i\otimes W_i\), with trivial Galois action on the finite-dimensional multiplicity space \(W_i\). In a tensor component of multidegree \(d_i\), invariance under the central element \(-I\in\mathrm{SL}(V_i)\) forces \(d_i\) even. If \(A_i\in\mathrm{GL}(V_i)\), after extending scalars write \(A_i=c_i B_i\), where \(B_i\in\mathrm{SL}(V_i)\) and \(c_i^2=\det A_i\). On invariant tensors \(B_i\) is trivial and \(c_i^{d_i}=(\det A_i)^{d_i/2}\), independent of the square-root choice. Since all determinants equal \(\chi_\ell\), the action is exactly \(\chi_\ell^{\sum_i d_i/2}\). This also applies to invariant subquotients of such tensor spaces, because rational representations of a reductive group in characteristic zero are semisimple.

## Opened primary sources

- **Verified**: G. Faltings, *Endlichkeitssätze für abelsche Varietäten über Zahlkörpern*, Inventiones Mathematicae73 (1983),349–366. Original paper: https://math.uchicago.edu/~drinfeld/Deligne%27s_conjecture_Manin_conf/Faltings_argument/Faltings.pdf. Section5, **Satz3 and Satz4, printed p360**, give semisimplicity and the endomorphism theorem; **Korollar1, printed p361**, gives the exact Hom theorem for two abelian varieties, by applying Satz4 to their product. These statements and their proof context were opened and read. Web refs turn1290view0, turn1291view2, turn1291view3. The Hom conclusion is used after an explicitly allowed finite extension.

- **Verified previously in the A80 audit**: J.-P. Serre, *Propriétés galoisiennes des points d'ordre fini des courbes elliptiques*, Inventiones Mathematicae15 (1972),259–331, **Théorème3, printed p299**, non-CM open image. Original author-hosted PDF https://www.college-de-france.fr/media/jean-pierre-serre/UPL5874918517843398173_Serre_proprie_te_s_galoisiennes_des_courbes_elliptiques.pdf. The actual printed page was viewed in the A80 audit; retained image inputs/source_cache/serre1972_A80_page_41.png, ref turn1282view0.

The Lie-Goursat reduction, exclusion of diagonal correlations, and invariant-tensor calculation above are supplied here as proofs. No additional product-independence theorem is asserted or cited without inspection.
