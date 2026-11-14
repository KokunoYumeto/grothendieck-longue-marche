# Independent review of the literal double cover and binary source collector

The group and Ferrari model were read in full and independently reproduced in
isolated directories. `a_cm_double_a6_replay.json` and
`a_cm_double_a6_model_replay.json` retain every protected hash, every compared
array, and the exact commands. Their statuses are PASS; the program runtimes
were respectively 42.895 and 1.355 seconds. The original files were unchanged.

The group argument uses the actual determinant-one matrices over
F3[t]/(t²+1), the actual 120-element subgroup, and its six cosets. The complete
720-by-720 product comparison supplies the quotient to the retained six-point
A6. The full Cayley-edge calculation supplies all 1440 automorphism lifts.
No abstract identification of a named cover was substituted for these maps.

The model uses the complete 53 old epikernels and all four central twists.
Its exact coordinate law retains both the central shear E and the ordinary
two-dimensional exponent coordinate. The free image U^53 follows from its
surjective A6^53 projection, JZ=U^53, and perfection. The additional C2²
factor follows by the perfect/abelian common-quotient argument.

The four subsequent source files were independently read in full:

- `e_a6_double_kernel_prepare_root.py`;
- `e_a6_double_kernel_head_root.cpp`;
- `e_a6_double_kernel_root.cpp`;
- `e_a6_double_kernel_replay_root.py`.

All six actual pure pairs have affine coordinates M=I and t=0. Consequently
the packed XOR formula for E is the literal restriction of the full model's
law on every induced coordinate. The old A6 projection agrees with both
unchanged source generators under the saved compression map.

The collector evaluates every complete old Schreier relator, including its
entire final sift, and retains the original generators as literal strong
nodes. The normal closure of the resulting binary vectors supplies the upper
bound; the saved actual kernel words and independent full-coordinate replay
supply the matching lower bound. No large run was repeated for this proof
review. The parent owns the numerical completion and its replay.

The claimed containment of the relative kernel in the F-derived image also
uses the old exact abelianization C120². The checked orders of the two new
free generators make the new abelianization a quotient of C120², while its
map onto the old C120² is onto. Hence that map is an isomorphism, which kills
the entire relative kernel. Orders of generators alone were not used for
this deduction.

Review outcome: PASS for the complete constructions and comparison maps.
