# C.51 primary-source and scope ledger

Status: notes-only complete candidate, not registered or integrated during checkpoint17 source freeze.

## Verified primary inputs

1. Hilaf Hasson and Jeffrey Yelton, *Prime-to-p étale fundamental groups of punctured projective lines over strictly Henselian fields*, arXiv:1707.00649v4 (22 June 2020), https://arxiv.org/pdf/1707.00649. **Verified**: opened the original full paper and read the setup and Theorem1.2(a),(b), printed p2, including its exact comparison of OUTER actions; also Example3.4, printed p10, for pairwise distinct reductions. The application uses the coordinate change 2t/(t+1), branches0,1,2 and their constant complex family. This proves trivial outer inertia on the SINGLE maximal prime-to-q geometric quotient for each q≥5. It does not infer mixed-prime triviality from separate pro-prime images. Current opened refs: turn1289view0, turn1290view1, turn1291view0. Earlier same-source opened refs: turn1286view0.

2. J. S. Milne, *Class Field Theory*, version4.03 (2020), https://www.jmilne.org/math/CourseNotes/CFT.pdf. **Verified**: original author notes, I Theorem4.16 and its proof, printed pp49–50, global Kronecker–Weber; I Lemma4.17, generation by ramified inertia. Current opened refs: turn1289view1, turn1290view2, turn1291view1; previous turn1287view0, turn1288view0/1. Existing bibliography key PBC_MilneCFT is used. Local principal-unit power identities are proved in the draft; no unverified conductor theorem is invoked.

## Internal dependencies fully retained

- C.50 supplies the specified fully characteristic D, its two-generator/order/derived-length properties, and the exact multiplier-one outer kernel implication.
- C.21 supplies arithmetic vanishing of Delta. The full cyclotomic character of the specified arithmetic subgroup is the standard one.
- C.48 remains the sharp derived-depth-four existence theorem. C.51 gives an explicit depth-at-most-five construction and makes no improvement of that sharp depth.

## Exact bounds and scope

The order bound |Aut(D)|≤|D|² is only numerical. It does NOT give a divisibility bound or v_p(|Aut(D)|)≤2v_p(|D|). The draft avoids that invalid inference, using a=2d0 and v_p([E:Q])≤log_p(d0²)≤a. The conductor bound N=2^(a+2)3^(a+1) is deliberately coarse and completely specified without enumerating D.

The finite arithmetic extension E is used only in the proof. It is not required as input to the construction D*=F/(N_D∩N_ab(N)). The exact Galois correction has the same FULL multiplier and outer identity on D, obtained by agreement on E∩Qab and compactness over cyclotomic fields.

No full finite outer image, efficient all-multiplier evaluation table, minimal detector, or new giant-group enumeration is claimed.
