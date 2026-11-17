# Complete independent exact one-family fixed-source presentation review

Status: **PASS**. UTC 2026-11-17T05:38:58.386647+00:00.

Source: `work_CE/one_family_fixed_source_exact_presentation29.txt`

SHA-256: `4a9caed1b0247f73bd00848e923e88701479a8158194bab808d2544aca0b8ef5`

I read the entire proof. The actual orientation descends to Q/H because H is even, and both C/tau edge labels are odd. Hence the even full subgraph has no edges. Distinct left cosets sL give distinct even vertices sH, and the selected edge norms project to distinct free generators under the odd-vertex deletion. This proves simultaneous free independence of the whole family; B139's existing complete fixed-word proof supplies generation, so A(G)^delta=F(S/L) is exact.

The source S action permutes those free generators literally. Both maps between F(S/L) semidirect S and S amalg_L (L times Z(A)) are explicit and inverse. Thus the full source kernel is exactly the normal closure of all [A,l], l in the actual L=H intersect S. Neither a sampled stabilizer nor L=<m> is substituted.

The marked assignment A->A_src, m->m, v->v extends exactly when [A_src,L]=1; its composition with the quotient is then identity on all three generators. This is a precise particular fixed-lifting criterion, compatible with whole-coarse nonsplitting and with the proved fixed surjectivity. It does not claim that failure of this one lift would preclude every lift.

For Section5, the asserted norm-copy retraction can be written directly on graph generators: send a_(sH) to A_(sL) on the chosen even S orbit, send every other graph generator to1, and fix S. Every graph edge has an odd endpoint killed by this map, so all relations hold. The map is S-equivariant and fixes every norm A_(sL), proving the stated retraction on A(G) semidirect S. There is no claimed extension over retained Q_f or full topology in Gamma_a. The actual compact equality from B139 remains separately scoped.

No new producer or primary retrieval was necessary: the only new input is this direct parity/free-basis argument and the complete coset presentation.
