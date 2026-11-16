# Independent audit: odd abelian factors over two-power dihedral covers

**FULL PROOF PASS**, conditional on the separately audited A70 as stated by the candidate. No canonical source or registry was changed.

Candidate: `notes/fgh_dihedral_abelian_extension_draft.tex`, SHA-256 `e1eb0ad55f805e94e77d70b10e2eed8823edaf73f5acae4683e9bd6aaa5c45ae`.

## 1. Actual subgroup and closure decomposition — PASS

Coprime-order powers split every subgroup and normal quotient kernel of G2 x B. The abelian intermediate extends to an elliptic isogeny because the peripheral commutator dies in an abelian quotient.

## 2. Connected pullback — PASS

The normal closure of the dihedral intermediate has two-power degree and the abelian isogeny is Galois of odd degree over the geometric base. Their intersection is the base field, so the actual compositum is a field and the smooth proper pullback is geometrically connected. The argument identifies the actual covering subgroup and does not select an arbitrary component.

## 3. Proper map and models — PASS

The genus-one case is exactly A40. Otherwise the compact-type Abel map based at a cusp extends the actual q:Z to E by composing with the extended Jacobian homomorphism. The precise A41 Abel-map input applies; no rational-map extension over an arbitrary singular surface is presumed. The odd isogeny extends finite etale over good elliptic models; its kernel is prime to the residue characteristic.

## 4. Semistable pullback — PASS

Finite etale base change preserves the nodal semistable local models and disjoint marked sections. Properness and flatness are inherited. The connected generic fibre is proved separately by the field argument.

## 5. Whole graph is a tree — PASS

The actual geometric closure is nilpotent and its only possible branch point is the origin on the good elliptic model. The exact Lehr-Matignon6.13 scope audited for A69 applies. Norm to the intermediate yields potential good JY, and semistable toric rank zero forces the whole dual graph to be a tree. No false assertion that an etale cover of a compact-type curve automatically has compact type occurs.

## 6. Lift of the selected rational path — PASS

The entire rational subtree joining P and Q maps constantly to O: every rational component has constant map to the smooth elliptic special fibre and the constants agree at nodes. Pullback along the finite etale isogeny is literally a disjoint union of copies of that subtree. A chosen cusp lift therefore has a distinct Q lift on the same rational copy, using kernel sections with distinct reductions.

## 7. Stabilization and old graph-cycle failure — PASS

Contracting unstable rational vertices cannot introduce a positive-genus vertex on the marked joining path. The two distinct marks prevent contraction of the entire marked path into an invalid coincident marking. The separately proved whole-tree condition makes this path the unique path required by A42. This explicitly avoids the earlier A4 graph-cycle failure.

## 8. All-prime arithmetic conclusions — PASS

The rational companion property holds for every selected cusp, so A42 applies at every coefficient prime without any special two-rank-zero claim for the new Jacobian. A59 applies directly to the actual nilpotent closure for normalizers. Finite field restriction and inner base-point changes preserve the original permitted packets and open-derived-group statements.

## 9. Conditional scope and supporting A70 read — PASS

The complete A70 dependency draft was read, including its three actual degree-two rotation quotients, generating-pair exhaustion, genus-one degeneracies and all intermediate cusp paths. The present deduction is explicitly conditional on A70 and does not claim products with a second nonabelian Sylow group. No new numerical certificate is needed for this structural deduction.

The exact dependency file hashes and audit time are in the companion JSON. The argument supplies a structural deduction, so no new finite numerical calculation was substituted for any geometric or arithmetic step.
