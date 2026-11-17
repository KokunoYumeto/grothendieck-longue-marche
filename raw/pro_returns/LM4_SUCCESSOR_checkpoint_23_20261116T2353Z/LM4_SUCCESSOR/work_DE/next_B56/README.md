# B.56 thirteen-generator extension: exact provenance and use

Status: integrated into `../B_rigid7.tex` after the checkpoint03 source freeze. The separate `B56_embedded_kernel_extension.tex` is the authoring copy. All mathematical assertions are in the main section; no additional statement ID is introduced. No priority is claimed.

## Result

A rationally specified meridian fan is a free basis e1,...,e13 of the ordered tetrahedral parameter curve S_T. The exact certificate computes all13 images in PB6 of the rigid seven-point forgetful map, on78 rational segments. Total reduced braid-word length is680. The main subgroup is exactly ker(theta), for this explicitly specified homomorphism theta:F13→PB6, and the completed test subgroup is ker(theta-hat). Capping identifies PB6 modulo its central full twist with PΓ0,7; forgetting the two normalized constant strands gives a pair-linking character which is zero on theta and sends the central twist to1. Thus no central-power ambiguity remains in either category.

The finite-word procedure substitutes the13words and uses the faithful Artin action. The source h=e6 e11 e6^-1 e5^-1 maps to the identity braid. All14 peripheral meridians survive. The test performs no Artin expansion of the long w or k words and does not claim an algorithm on arbitrary profinite elements.

The rigid and all-four-point kernels are incomparable. The cross-ratio ((u²−1)/(u²+1))² for q={1,2,3,5} is a degree4 unramified covering away from six branch preimages and detects h. The balanced meridian commutator w has length384 and dies under all495 four-point maps; its rigid braid has an explicitly noncentral image in GL6(F101), via checked unreduced Burau matrices. The common word [h,w] has length776 and nonempty exact free reduction. Both witnesses survive the stated completed target tests by explicit finite detection (or residual finiteness of F2 for h).

## Reproduction

Run from this directory with Python3 and SymPy available:

```sh
python certify_all13_monodromy.py
python membership_rigid7.py
python check_all13_pair_linking.py
python check_all13_burau.py
python membership_rigid7.py '[6,11,-6,-5]'
```

The main path certificate ran to `ALL EXACT CHECKS PASS` in80.69seconds. It uses rational root isolation and rational sign tests throughout. It verifies exactly the three previously certified words at indices5,6,11. The auxiliary membership, linking and finite matrix checks also pass. `all13_braid_words.txt` is a plain rendering of the JSON words; all actual algebraic routines read the JSON, not this human rendering. `uncovered_four_orbits.json` is exploratory and is not an input to any proof. The `.partial.json` produced during a rerun is a recoverable checkpoint, not the completed certificate.

## Exact remaining limit

No equality of the completed test kernel with the closure of the discrete kernel is inferred. That question is equivalent to whether the discrete image theta(F13) has its full profinite topology induced from PB6. The full completion of the abstract infinite-rank discrete kernel is separately nonmetrizable and cannot equal the metrizable completed test kernel. These conclusions concern the proposed test route and do not decide the actual completed A5 centralizer K.

## Files and hashes

- `certify_all13_monodromy.py`: 9501 bytes; SHA256 `28ecb5481011ed936830ec898ec148859aada97b924f4ed7b51e1718975c3476`.
- `certify_all13_monodromy.out`: 5365 bytes; SHA256 `d36b2d26065e6d8d688234dd96416ae96095117bae78a0e841084e55e2b9736f`.
- `all13_exact_certificate.json`: 2338837 bytes; SHA256 `a09ba0aabe3ccd652867aa89e9c2b9f33c471bb8543b5dae75c3b4b707439f69`.
- `all13_braid_words.json`: 9051 bytes; SHA256 `f87e7ec24a5183d906c8ce84ebdea1041757e44fd459f912c99ac3c08e01f6fc`.
- `all13_basis_geometry.json`: 3822 bytes; SHA256 `4e491eec7c195df89833845644e5734be312582431d1765e0ca974d505af1986`.
- `membership_rigid7.py`: 4676 bytes; SHA256 `e01fcc90cab9e2d9ac905b053f27a2442c6930b19349ff0fab99f4c726f9049b`.
- `membership_rigid7.out`: 2961 bytes; SHA256 `adeb54c61a393221cbe71ff65a04317bf02ee3b8db92d50795f83e5d9d4537ed`.
- `check_all13_burau.py`: 2556 bytes; SHA256 `1dc95dbc9a8f47bc3b7f89c03b71dc8e062872eed75b4775fce5493dacd0e844`.
- `check_all13_burau.out`: 635 bytes; SHA256 `224fc002a62c100970a5ab20e373ed9d676cfc575c284d8043f3f04c8bdd564c`.
- `check_all13_pair_linking.py`: 2373 bytes; SHA256 `ec1c83e5f46e1a140b71926372b1e42b50a3165ad94846c81f0c325832ec1273`.
- `check_all13_pair_linking.out`: 790 bytes; SHA256 `19279eb6439c3af7911f80d1acfb41bca0931fdbf03ee95fe3e00d14667d2fe4`.
- `all13_source_words.json`: 9239 bytes; SHA256 `441036940b7c513f0969655498aee9ab492e8758697c6185776786564f472e12`.


## All13 extension QA (03:57 UTC)

The integrated B component rebuilt twice to16pages and150311bytes, with zero overfull boxes and zero LaTeX warnings. The initial draft had one33.86365pt overflow in the isolated review and one15.11322pt overflow after integration; both were fixed by shortening paragraph leads. The final three extension pages13–15 were rasterized at100dpi and opened for visual inspection: all formulas, the13-column word table, the6×6 matrix, margins and text are legible. The final logs are B56_all13_final_build_0.out and _1.out; image checks are qa_B56_all13-13.png through -15.png. The pair-linking and Burau auxiliary checks and finite-word selftest were rerun after their final edits and passed.
