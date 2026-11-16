# Two actual central covers and the remaining two-primary comparison

Status: complete candidate proof with executed exact calculations; independent review requested. C31 remains Open because the fresh G86 quotient relation is not yet proved. Nothing below uses the failed native-collected G86 relation as a mathematical certificate.

## 1. Actual section of the finite group extension

Use C43's actual groups G=G176, Q=G104, A=ker(G→Q)=(C2)^72, and N=ker(Q→G86)=(C3)^18. The original pc source has SHA256 `95fb384593bfaf97d468bbc51f11cd797484a08cb3ec3b954961085b520ffc88`. Write M_j for the right conjugation action of g_j on A, in the original basis g105,…,g176. We use column vectors, so action by a word g_i g_j is M_j M_i.

For i=87,…,104, choose h_i=g_i a_i. Their powers and commutators give linear equations over F2:

\[
(1+M_i+M_i^2)a_i=g_i^3,
\qquad
(M_j-1)a_i+(M_i-1)a_j=d_{ij},
\]

where g_i^{g_j}=g_i d_ij in the actual source, for i>j in N. The file `code/pbc_top_two_section.py` derives these equations directly from every relevant original power/conjugation word. The 12,312 scalar equations have rank1,224 on1,296 variables. A literal solution is retained. Thus the h_i generate a complement H≅N above the normal odd subgroup.

For each of the other86 quotient generators, choose h_j=g_j a_j to normalize H and induce the prescribed conjugation on its quotient. The18 generator conditions give1,296 scalar equations on72 unknowns, of rank72. The retained solutions satisfy every equation.

This produces a section for the ENTIRE Q, not merely its N-subgroup: Schur–Zassenhaus conjugacy shows N_G(H) maps onto Q, and its kernel is C_A(H)=A^N=0. Equivalently the unique lifts normalizing H preserve every quotient relation. An independent standard GAP positive-word replay additionally verifies all104 power relations and all5,356 conjugation relations of Q in the ORIGINAL finite G. It also checks the18 order-three equations,153 pair commutators and1,548 normalizer equations explicitly. See `code/pbc_top_two_section_positive_replay.{g,out,json}` and its generator `pbc_verify_top_two_section_positive.py`.

The slower attempt to construct inverse collector tables was stopped before any result; its source/output and stop ledger are retained. The completed positive-word replay does not rely on it.

## 2. The two central covers of A

C43's two explicit invariant alternating forms B_1,B_2 are linearly independent in Hom((Λ²A)_Q,C2). Their ranks, recalculated from their literal matrices, are72 and36. Only the first is nondegenerate. We therefore call the resulting groups central class-two covers, and do not call the second an extraspecial group on A72.

Each B has a Q-invariant quadratic refinement q, already retained and checked against all104 original action matrices in `pbc_two_top_certificate.py`. Define a bilinear cocycle c with diagonal c(e_i,e_i)=q(e_i), upper triangular entries c(e_i,e_j)=B(e_i,e_j) for i<j, and lower triangular entries zero. Then

\[
E_q=A\times C_2,\qquad
(v,z)(w,t)=(v+w,z+t+c(v,w))
\]

has commutator form B and square map q. The distinguished central kernel is the displayed C2. Throughout, an automorphism fixes this CHOSEN central C2 kernel; for the degenerate form the whole center is larger and is not asserted to be fixed pointwise.

For a matrix M preserving q, the cocycle difference c(Mv,Mw)+c(v,w) is symmetric with zero diagonal. Let q_M be the quadratic function with that polar form and zero values on basis vectors. Every lift of M has the form

\[
(v,z)\longmapsto (Mv,z+q_M(v)+l(v)),\qquad l\in A^*.
\]

In particular, automorphisms fixing the distinguished central kernel map onto O(q), with kernel A*. Pull back this extension along the ACTUAL Q-action. Because N is odd and (A*)^N=0, averaging and Hochschild–Serre give H²(Q,A*)=0; thus the pullback extension splits. We construct this splitting explicitly instead of inferring numerical values from its mere existence.

## 3. Explicit actual Q-actions

`code/pbc_top_two_cover_actions.py` constructs the lift for each form. First choose l_i for i=87,…,104 so that the lifted N-generators have order3 and commute. The order equations on a basis vector e_k are

\[
l_i(e_k+M_i e_k+M_i^2 e_k)
 =q_{M_i}(M_i e_k)+q_{M_i}(M_i^2 e_k).
\]

The commutation equations are obtained by applying the two composites to e_k. The script retains their full exact derivation and verifies all12,312 equations after solving them; the rank is again1,224. As two automorphisms above the same matrix differ by a linear functional, checking the remaining central discrepancy on all basis vectors checks the full automorphism identity.

For each j≤86, impose α_i α_j=α_j α_(i^j), using the actual original conjugation word for i^j in N. Here products mean right actions in the stated order. The already constructed N-action evaluates that entire word. On each e_k the equation for the unknown l_j is

\[
l_j(M_i e_k+e_k)
 =q_{M_j}(M_i e_k)+l_i(e_k)
  +\bigl(\text{central part of }\alpha_{i^j}(M_j e_k)\bigr).
\]

The script first checks equality of the underlying matrices, then solves and rechecks all scalar equations. Each rank is72. The same normalizer argument in the pullback extension gives a genuine action of all Q on E_q. It is not necessary to assume that N acts faithfully on A: the pullback retains the actual Q-coordinate, so the constructed subgroup projects isomorphically onto N. Its normalizer has kernel (A*)^N=0 and maps onto Q by coprime complement conjugacy.

Consequently each semidirect product E_q⋊Q, with the chosen actual group section from§1, is a central C2 extension of the actual G. These are ordinary finite groups, not a formal degree-two approximation.

## 4. Evaluation in the actual covers

Represent elements as a Q-section element followed by an E_q element. If the original generator g_j, j≤104, is lifted as its section generator followed by (a_j,0), multiplication on the right transforms the A-coordinate v and central coordinate z by

\[
v' =M_jv+a_j,
\qquad
z'=z+q_{M_j}(v)+l_j(v)+c(M_jv,a_j).
\]

For j≥105, use the basis vector a_j and M_j=1, q_M=l_j=0. This evaluates every retained original positive word in the ACTUAL central extension. No native raw central normal form is used.

`code/pbc_top_two_cover_values.py` evaluates the three target differences (B_s s)-(aB_s), (B_r r)-(bB_r), and (ab)-(sr), together with every original genuine s- and r-centralizer commutator. The A-coordinates of each compared pair are checked equal. A separate standard GAP positive-word replay now additionally verifies all83 compared pairs in the ORIGINAL finite G176: the three target pairs,71 s-frame pairs and9 r-frame pairs. It uses GAP's own `FromTheLeftCollector_SetCommute` on the actual finite presentation; no central tails are adjoined in this finite check. Exact executed source, stdout and provenance are retained in `code/pbc_top_two_cover_source_fast.g`, `.out`, and `_provenance.json`. The executed source SHA256 is `33df2599e248e95ed7936ada8a8b14f77961c502289d530304dc6c6458dadd48`; the run exited0 after56.4seconds. The earlier conservative all-n-commute attempt was interrupted for capture, and is retained separately without a success claim.

| form | rank | three target component values | total target | 71 s-frame values | 9 r-frame values |
|---|---:|---|---:|---|---|
| B1 |72|0,0,0|0|all zero|all zero|
| B2 |36|1,0,1|0|all zero|all zero|

In particular, every permitted correction of the s-centralizer type also evaluates zero in these covers. A valid quotient identity using those corrections would not acquire a new top obstruction.

## 5. Why these are exactly the missing tests

The restriction of a central extension of A to H2(A,Z)=Λ²A is its commutator pairing B. Changing the diagonal quadratic refinement changes an Ext¹(A,C2) component, not this restriction. C43 identifies the canonical inclusion (Λ²A)_Q→H2(G,Z2) with the exact kernel of the map to H2(Q,Z2), equivalently to H2(G86,Z2). Therefore our two central extensions restrict on that kernel as precisely the two independent coordinate functionals B1,B2. Together they detect every element of the kernel. Any class inflated from H²(Q,C2) evaluates zero on this kernel by naturality, so an ambiguity of that type cannot alter this conclusion.

Thus, IF an independently replayed G86 identity shows that T plus a combination of the original s-centralizer commutators is zero in its two-primary Hopf subgroup, the same corrected original element lies in the top C2² kernel. The two zero values above then force it to vanish in the original group. Combined with C42 this would settle the full finite lifting obstruction. At present the only completed G86 search failed its original-source replay; it cannot discharge this premise. Fresh standard-GAP source rows are being collected for a separate search. C31 remains Open.

## Files and provenance

The exact data and executable sources are `pbc_top_two_section`, `pbc_top_two_cover_actions`, and `pbc_top_two_cover_values` in `code/`, each with `.py`, `.json`, and `.out`. Their JSON ledgers hash their own source and every mathematical input. The actual section's independent GAP replay is in `pbc_top_two_section_positive_replay.*`. No prior raw trace, archive recipe, or canonical statement was changed by this work.


## Completed quotient gate, 23:20 UTC

The preceding conditional scope records the state of the original cover audit. The fresh standard-GAP-row search has now passed its complete literal original-source replay: `code/pbc_quotient86_standard2_literal_original_identity.json`, with 6,446 original source leaves, no coordinate/modulus leaves, and only genuine s-centralizer corrections. The returned correction generators are 6,16,27,35,39,41,43,49,53,55,63,65,72,79,80,85 in the original adapted pc basis. Thus the hypothesis of section 5 is now discharged by this fresh certificate. Combined with C42, the original integral corrected Hopf target is zero. The complete group-lifting and two-normalization proof is in `notes/pbc_C31_draft.tex`, still notes-only pending its full independent audit. The older failed native trace remains outside the mathematical argument.
