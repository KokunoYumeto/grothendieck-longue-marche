# Independent E.66 proof and code audit

Status: PASS. This records a full proof and program read, not an independent execution of the large finite certificates. Root separately replayed the K3 source certificates.

## Exact maps checked

- The positive cyclic Schreier section gives coordinate zero exactly delta_n; x-exponent is divided by n and remains zero on F-prime.
- The common 5223-point image is derived before projecting to the five coordinate-zero blocks. Thus its degree-4849 projection is the actual common correction image.
- The index-two subgroup gives genuine nonzero characters on both projections. The binary mask175728 uses the stated ordered coordinates; mask16 is exactly the lower-left entry divided by two for n=3.
- The signed modulo-four representative has diagonal entries one, so the lower-left formula is a homomorphism with the printed sign.
- The membership target is old_value inverse times new_value. N_B-prime lies in ker(q_F), so the ordinary q_F(f_i) coordinate remains unchanged.
- In the explicit Schreier inverse, stripping a right transversal makes the returned word prepend each later transversal. The recorded DAG multiplication and conjugation conventions agree with this order.
- Every one of the 288 successful correction words is built from the complete derived-source DAG and is replayed on all 5223 points, retaining the exact E62 coordinate.
- The three-coordinate and six-coset K3 source comparisons use the identical N_B-prime domain. Their odd abelianization eliminates any nontrivial common two-group quotient with C. No equation is imposed on an untested conjugate coordinate.

The revised statement names the E17 words actually used by E62/E66. No correction vector is transported from the original E1 word list.

## Reviewed hashes

- `sections/E_distribution_overlap_agent.tex`: `87f7c44d63c0a4b90136c1827f0c1366c5053f794e42e81d2d12eb74efab981f`
- `code/a_cm_distribution_e62.py`: `3d08d5c40baf2e06ce59f244f50062a7e25bdeb6f9ea6993c44efcda49b8c5e4`
- `code/a_cm_distribution_overlap.py`: `cd786cafa31c878d6794bb307f4064586c36cc1c6c8e51a293e722bbf85b2a6f`
- `code/a_cm_distribution_witnesses.py`: `154ea5fd63e68b785ddbb3c35e2ee19c02c0cfcc520e8f061ee19dcbaa31b228`
- `code/a_cm_distribution_e62.json`: `33c61d6b062b9ad614fba59bfc5a636c95c06944cc0edd0aa92dad50fc2672b4`
- `code/a_cm_distribution_overlap.json`: `72d3c3cc29c2adc5debeffbd696f2138e9d897cb28e845349b481681650c5101`
- `code/a_cm_distribution_witnesses.json`: `b6cabce3be789a6c3c675129a3705a797d11edd91a29384503214a34f5c82a01`
