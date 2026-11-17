# Independent full review: actual compact cyclic-edge embeddings

Status: **PASS** at the exact pre-filling scope. I read the complete source, including the arbitrary whole-subgroup target argument, all three completed intersections, and the coset-tree embedding paragraph. This is a proof review; no new finite-target producer was run.

Source: `work_DE/next_marginal_source/compact_actual_edge_embedding28.md`.
Source SHA256: `545b2f0d160ced17f4a92f11f70b94f1124840fa6aff7316873ffad83a512e26`.

## 1. Exact common finite edge and subamalgam

The two retractions are genuinely to the same based K, with the right identification retaining eta. For an arbitrary finite target of Hi, full topology of its two actual vertex subgroups permits the two restriction-kernel refinements. Choosing one finite-index normal M of K below both initial edge kernels and adjoining the entire retraction modulo M gives edge kernel exactly M on both sides. No identification of unrelated vertex normal subgroups is required.

The crucial finite intersection assertion is proved in the source rather than assumed. If the image of e in E1 equals the image of x in K, the retraction coordinate forces xM=r_L(e)M. Since r_L(e) is a power of f and M lies in the first coordinate's edge kernel, the two complete finite vertex images agree with that power of f. Thus A1 intersect C equals C1, and similarly on the other side. These exact intersections imply the ordinary embedding J=A1 amalg_C1 B1 in A amalg_C B by reduced normal form.

The original arbitrary finite target psi factors through J: its restrictions factor through A1 and B1, and their maps agree on C1 because the cyclic restriction kernel is already contained in ker psi. This is essential for arbitrary mixed words; separate vertex separation alone would not prove the result.

## 2. Full induced topology of the whole subgroup

The finite-group amalgam is virtually free by the explicit aligned regular permutation construction. The kernel is free because it meets all conjugates of the finite vertex groups trivially and acts freely on the ordinary Bass--Serre tree. The finite-index quotient graph gives finite rank. The previously fully read finite-core/finite-index argument supplies both separability and full topology of every finitely generated subgroup J of this group. A finite target of the whole Hi is therefore refined by a finite target of V. This is the correct kernel-containment formulation; extension of psi with its exact target is not needed.

The theta-transferred conclusion for Hj is valid. The argument uses the actual retractions and the proved all-n topology input for Bi, so it does not appeal to an unrestricted compact subamalgam theorem.

## 3. Completed intersections

The proof of Section4 is independent of any automatic interchange of closure and intersection. For x in Hihat intersect R_Lhat, repeat the construction for each arbitrary finite psi of Hi. Its image lies in closure(J) intersect the finite vertex A inside Ghat. Since J is separable in the virtually free G, this intersection is J intersect A=A1. The extension of psi_J is legitimate because J has its full induced topology in G. Hence every finite image of x lies in the corresponding image of E1. By compactness, equivalently by the finite-quotient description of a closed subgroup of Hihat, x belongs to E1bar. The same argument applies to the other vertex and to finite edge C, giving Bi and F respectively.

These arguments establish the stated actual completed intersections without presuming the later coset-tree conclusion. All reverse inclusions are immediate.

## 4. Compact coset-tree embedding and boundary

Full completion preserves the defining pushout of the abstract amalgam. The already established full subgroup topologies make its vertex and cyclic edge maps injective, so the resulting full profinite amalgam is proper. The exact completed intersections from Section4 make each vertex and edge coset map into the ambient compact tree injective. Compactness and the Hausdorff property then give genuine embeddings, respecting incidence. Thus the standard compact tree of Hihat embeds as the claimed actual compact subtree.

The source correctly stops short of a whole compact Hi/Hj intersection theorem. In particular the ordinary argument by finite paths has not been transplanted to arbitrary points of a profinite tree. It also makes no claim about survival after either family of initial relators, about the image of Dloc in V_star, or about invariance of the actual matching kernel.

## 5. Dependency audit

The finite-core and product-separation inputs were fully read in the earlier bound review `work_A/review_compact_vertex_overlap28.md`. That review includes an actual primary reading of Ribes and Zalesskii (2004), complete Lemma3.1 and Theorem3.13 proofs, through the author PDF. The current source only requires the already established finitely generated subgroup topology/separability consequence for virtually free groups, plus its own explicit finite-group amalgam construction. No new literature theorem or unverified profinite cyclic-edge recognition result is inserted.

No correction is requested.
