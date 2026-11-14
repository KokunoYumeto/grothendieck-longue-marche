# Independent read of the E75 finite Gaussian frame enumeration

Reviewed `code/bc_gaussian_kn_frames.py`, SHA256
`068a42a31a628911ee4a2c82d371098651f1a0ca99915f2832cf5ed1e9c7bcd1`,
and its exact coordinate decoder in `bc_gaussian_kn_characters.py`.
This is a proof/code read, not a fresh numerical rerun.

The semidirect product law retains the actual order-four deck map.
All 2,187 pure-kernel elements are used for each frame variable: the
order-four conjugacy lookup is complete, and each value has exactly
three preimages. For each y-frame the equation x y' z'=1 determines
z' exactly. The subsequent fourth-power test and complete z-frame
lookup retain every cusp-preserving framed map. The source graph is
tested in all three paired coordinates using the actual automorphisms
A and B. The Hall-to-class-two conversion is the same literal map as
the earlier model; every surviving lower frame is matched to its
actual E69 record.

The endomorphism assertion has an exact quotient justification. In
Gamma=C2*C4 the common C4 deck kernel is free of rank two, with
generators X=x^2 y and Y=z^2 y. The displayed values satisfy those
identities in the target. The equations y'^2=z'^4=1 give the map from
Gamma, and the unchanged deck values send the free kernel into P3.
The characteristic verbal relations gamma4(P), gamma2(P)^3 and P^9
vanish there, so this is an endomorphism of P3 semidirect C4 itself.
The program checks determinant one on the two-dimensional Frattini
quotient. Hence its restriction to the finite three-group P3 is
surjective, and therefore invertible; the deck map is the identity.

The exact output is 324 automorphisms, 2,916 cusp-preserving frames,
and 972 frames satisfying the source graph. Each of the twelve old
E69 frames has 81 of the latter. Only twelve of these source frames
come from the four displayed inner actions. The program and stated
scope retain this distinction: the full pro-three lifting argument
is asserted only for the E70 inner families.

No gap was found in this finite enumeration or its stated quotient
and automorphism arguments.

## Label clarification and complete E75 proof

The subsequent program revision only clarifies that the saved
`specified_inner_x_power_0_to_3` field and its summary counts refer to
those four displayed powers. Its SHA256 is
`3a052ef0ce70d42744b601121e342f4f972b1fdd29da536a232fea6c5e36ef59`.
The prior passing source/output is retained under
`research/E75_frame_count_before_label_precision/`. The mathematical
values are unchanged; powers outside that specified range were not
excluded by the audit above.

The full `sections/E_gaussian_matrix_pro3_agent.tex` was also read.
The literal target-factor embedding gives elementary Sylow-three
subgroups of P71: each matrix factor has the displayed central-two
kernel in Q times Q, and all other stated factors have elementary
three-Sylow groups. A Sylow-three subgroup surjects onto every finite
three-group quotient, so every such quotient of P71 is elementary.
This is the exact input needed to put Phi(H) inside the actual common
kernel. The twelve-character detector then identifies that kernel
with the kernel of the specified six ordinary characters, proving the
full fibre product with the actual projection maps.

The complete whole-J source is retained by deriving before projection
and adding all 95 integral sixth-power words. The compact image and
kernel arguments use that same source, so no smaller family of word
preimages is substituted. The finite count 4,478,976 retains all 243
frames over each E71 value; the whole-pro-three conclusion retains
the twelve specified E70 frames. The full proof read passes. This
additional review did not rerun the large common-source certificates.
