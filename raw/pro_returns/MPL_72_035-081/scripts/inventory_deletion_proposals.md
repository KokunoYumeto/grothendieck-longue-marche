# Deletion inventory reconciliation proposals

Text/record snapshot: 2026-11-15 00:33:49 UTC. No image or supplied context was read.

## Finding

The deletion-count differences in the specified scans map to 24 existing combined deletion rows and 7 separately marked children inside already listed blocks. Splitting those combined rows gives 33 additional granular rows; listing the children gives 7 more. The proposed structure therefore accounts for the 40-call count difference without adding manuscript text.

The existing inventory already describes most of these source segments in combined form. A count difference does not establish omitted manuscript content. For the five margin-note parents below, the cancelled text is explicitly named already; the proposed child row records a second aspect of that same noted material. The primary transcriber decides the physical element boundaries from the completed image audits. No source or inventory edit is performed by this report.

Element IDs refer to the recorded snapshot. Rebuilding the inventory after edits shifts later IDs; use the recorded position and content as well as the ID. The companion CSV contains all proposed source segments in full, with original whitespace, and has no `transcribed` or completion-status field.

## Existing combined deletion rows

In the evidence column, `D3` means the third `deleted` call in that scan, and `L11` gives its TeX line. These are source locations, not new manuscript numbering.

| Existing element | Current description | Separately marked source evidence | Proposal |
|---|---|---|---|
| 041.09 | 2; 2 | D3, L11: `\unsure{2}`; D4, L13: `\unsure{2}` | Split into 2 located deletion rows. |
| 046.10 | c_i; +1 | D5, L20: `\unsure{c_i}`; D6, L20: `\unsure{+1}` | Split into 2 located deletion rows. |
| 046.29 | two coefficients | D11, L132: `\unsure{2}`; D12, L132: `\unsure{2}` | Split into 2 located deletion rows. |
| 047.09 | earlier i_1+ terms | D1, L30: `\unsure{i_1+}`; D2, L33: `\unsure{i_1+}` | Split into 2 located deletion rows. |
| 048.02 | earlier conditions and coefficient | D1, L6: `\unsure{i,j\ \text{consécutifs}}`; D2, L7: `\unsure{2}`; D3, L7: `\unsure{j=i}`; D4, L8: `\unsure{\text{si }j=i-1}` | Split into 4 located deletion rows. |
| 048.34 | lambda zeta_i; repeated condition; index 0; zeta_-1 | D14, L142: `\unsure{\lambda\zeta_i}`; D15, L144: `\unsure{\text{si }0\leq i\leq n}`; D16, L145: `\unsure{0}`; D17, L147: `\unsure{\zeta_{-1}}` | Split into 4 located deletion rows. |
| 049.20 | interval and J_i notation | D5, L98: `\unsure{\text{intervalles}}`; D6, L101: `\unsure{J_i=\{j_i,j_i+1\}}` | Split into 2 located deletion rows. |
| 049.27 | Delta_n(...)=; delta_n(...)=beta_0 | D7, L120: `$\unsure{\Delta_n(C_0,\ldots,C_{n-1})=}$`; D8, L124: `\unsure{\delta_n(c_1,\ldots,c_n)=\beta_0}` | Split into 2 located deletion rows. |
| 049.38 | Attention; et une puissance; au moins | D11, L162: `\unsure{Attention!}`; D12, L164: `\unsure{(et une puissance)}`; D13, L166: `\unsure{\text{au moins}}` | Split into 3 located deletion rows. |
| 049.40 | earlier suite notation; J'' | D14, L173: `\unsure{\text{suite de }p\text{ intervalles}}`; D15, L174: `\unsure{J''}` | Split into 2 located deletion rows. |
| 050.08 | earlier B and alpha terms | D3, L18: `\unsure{+B_2}`; D4, L19: `\unsure{4-(\alpha_0+\alpha_1)-\alpha_0+}` | Split into 2 located deletion rows. |
| 050.10 | B_3; alpha terms | D5, L23: `\unsure{+B_3}`; D6, L24: `\unsure{\alpha_0+\alpha_1}` | Split into 2 located deletion rows. |
| 050.15 | earlier factors and alpha_4 | D9, L36: `\unsure{\alpha_4}`; D10, L38: `(\alpha_0+2)(\alpha_1+2)`; D11, L40: `\unsure{(\alpha_1+2)(\alpha_3+2)}`; D12, L41: `\unsure{(\alpha_2+2)(\alpha_3+2)}` | Split into 4 located deletion rows. |
| 050.30 | L_2; half delta_n+1; L_3 | D20, L91: `L_2(1,B_0)=4-`; D21, L94: `\unsure{\tfrac12\delta_{n+1}(1,B_0,\ldots,B_{n-1})}`; D22, L96: `L_3(\unsure{1},B_0,` | Split into 3 located deletion rows. |
| 050.34 | 1; B_0^2 B_1; 2 | D24, L105: `\unsure{1}`; D25, L106: `\unsure{B_0^2B_1}`; D26, L106: `\unsure{2}` | Split into 3 located deletion rows. |
| 051.08 | earlier powers and delta_2m fragment | D2, L47: `\unsure{(B_0^{2m}B_1^{2m-1}\mathbin{-})}`; D3, L51: `\unsure{\delta_{2m}\cdots}` | Split into 2 located deletion rows. |
| 052.07 | prime; coefficient 2 | D2, L27: `\unsure{'}`; D3, L31: `\unsure{2}` | Split into 2 located deletion rows. |
| 053.07 | 2 and earlier ratio | D1, L41: `\unsure{2}`; D2, L42: `\unsure{\widetilde o/\rho'}` | Split into 2 located deletion rows. |
| 053.10 | two coefficients | D3, L61: `\unsure{4}`; D4, L62: `\unsure{4}` | Split into 2 located deletion rows. |
| 054.10 | dans; ce qui | D3, L20: `\unsure{dans}`; D4, L20: `\unsure{ce qui}` | Split into 2 located deletion rows. |
| 054.20 | droite; et o' | D7, L54: `droite`; D8, L55: `\unsure{(et $o'$)}` | Split into 2 located deletion rows. |
| 054.30 | précisons; mu | D11, L90: `\unsure{\text{précisons}}`; D12, L93: `\unsure{\mu}` | Split into 2 located deletion rows. |
| 055.02 | g identically zero; Alors f(...)=0 | D1, L3: `$g(\lambda,\mu)=0$ identiquement`; D2, L4: `Alors $f(\lambda s_0+\mu\widetilde o)=0\quad\forall\lambda,\mu$ ⏎ sss $\sigma'$.` | Split into 2 located deletion rows. |
| 055.23 | tels; Ceci définit donc | D9, L49: `tels`; D10, L52: `Ceci définit donc` | Split into 2 located deletion rows. |

## Separately marked children within listed blocks

Retain the existing parent block and add the listed child to make its deletion marking individually addressable. The five margin parents already contain an explicit description of the cancelled content; they are identified here as existing coverage, not as absent text.

| Parent element and kind | Existing coverage | Child source evidence | Proposed treatment |
|---|---|---|---|
| 050.16 (deletion) | long expanded expression | D14, L46: `\unsure{+\alpha_3}` | Retain the outer cancelled expression; add its separately marked inner +alpha_3 deletion. |
| 050.19 (display) | final L_4 alpha formula | D16, L58: `\unsure{+\alpha_0\alpha_3+\alpha_2\alpha_3}` | Retain the display row; add its separately marked +alpha_0 alpha_3+alpha_2 alpha_3 segment. |
| 061.02 (margin note) | cancelled tilde rho_ij=half rho_ij | D1, L7: `\(\widetilde\rho_{ij}=\frac12\rho_{ij}\)` | The existing margin row already describes the cancelled formula; a deletion child makes its marking separately locatable. |
| 069.13 (margin note) | cancelled alpha_0+2 | D5, L22: `\(\unsure{\alpha_0+2}\)` | The existing margin row already describes the cancelled expression; retain that coverage and identify the deletion child. |
| 071.32 (margin note) | cancelled 2sigma sigma'-rho sigma | D11, L98: `2\sigma\sigma'-\rho\sigma=\sigma(2\sigma'-\rho)` | The existing margin row already describes this cancelled calculation; a deletion child records its marked segment. |
| 074.09 (margin note) | deleted dans les fibres | D1, L21: `\unsure{dans les fibres}` | The existing margin row already names the deleted words; a deletion child records the marking without introducing text. |
| 078.02 (margin note) | cancelled s0'=rho s0 tilde; fV(s0') | D1, L3: `$s'_0=\rho\widetilde s_0$\\$f_V(s'_0)$` | One deletion macro encloses both lines already described by this margin row; preserve it as one child, not two. |

## Combined blocks that should remain intact

- **048.08:** one deletion macro encloses the two endpoint formulas in a single box. The existing row names both; no split is proposed merely because the box contains two formula lines.
- **050.16:** retain the cancelled expanded expression as its own outer deletion element. The inner `+\alpha_3` is a separately encoded child; the outer element is not replaced by that child.
- **050.37:** one deletion macro encloses a determinant and its expansion. The existing description covers that block; no extra row is proposed for every equality inside it.
- **051.03:** the cancelled even-case heading, congruence, and unfinished expression occur within one outer deletion macro. The existing row describes that block.
- **055.20:** retain the whole cancelled paragraph. Its inner `tels` and `Ceci définit donc` are already grouped in 055.23; split that child row into two, retaining the outer row.
- **078.02:** the two lines of the cancelled marginal calculation are enclosed by one deletion macro. The proposed child remains one deletion entry.

## Source fingerprints

These fingerprints identify the mapping snapshot and make no freeze claim.

| Scan | Page SHA-256 | Record SHA-256 |
|---|---|---|
| 041 | `71013c5c42f0195b60bd6ea6069ef49c3f93e2cfe4c18a3f6b83f9851b09ac19` | `10edaee0e6d1ea5b205ccf8d40750e674796a69ab9a6d7528e88af8ce8cc8dbe` |
| 046 | `b0f69e17ac02c150ccb7664576cb2783a16da683cb47259a108444c06ec41431` | `d1617ba78e1a4e5a2a0d7cc45307e055e2418e56c86903a79c8a740b0febf9f5` |
| 047 | `18bcc4e60a443ed0e24a3e23f005889a5380a64570ec42942f4f1025f7d55986` | `53fcd3f9bf03b56bf3b3884b27d22506436cf535fc207add613551f500787282` |
| 048 | `62b90361c405722d484b6a066133d0e3d3d475d284bf8487b251e28186c8accb` | `b45bb78c77d3d9c742f69ca7b3daa3207fb818b892e1bff5e68247d2796b9838` |
| 049 | `76aa24a75f2f1056b982456832aef9686e78d71e4dde364d9067319836821f97` | `5ab933446baa118eaa8468dd77220e0163fd7a88d75f12033bb37d81b178f01c` |
| 050 | `e63f92323701d8a4b96974c6e4c5aa015317f74bfd004d0a2383f05f34dc10b4` | `424e47aab083136ed71bade9c491c5528b0ee024132c7fa55030e2bcf887c68a` |
| 051 | `c3efa47404e43c21e5dacf0b627c03f601e71967ad26ea1e2299e1ce95fb19f4` | `f061cab576db53f448df1509efa9234cbeacfd25b1bf86188428101c2778ace4` |
| 052 | `668b8d9a59c586c859fdea2cb99e008f5d90c21ca8e7edc9748407ade43e10b7` | `6a9739cad2fcb3a6112a4e5c36f9a8a3344f18391cc0d1d12cb3e2e28789e9c9` |
| 053 | `00446172a357a2f50a7dbaa0ee0d16953b74dc379f62999b5e8898034d1c8cf6` | `fd91c1aba720ece1a053010bff51ba4d9517540aba013bcd07d5ed86c3a02859` |
| 054 | `10a7b384db84f4ec12a9f15da3cf2d226d6728f88613404e4270d18deaf1a6c0` | `c7aeba3215b85ab22b490109436cbfc2acae86165fd4c5e545b096df2c0c212e` |
| 055 | `961cb3f6eae1275e04e497f59c81f4df8465338dc8b983f0d4417cb090fc826b` | `2af40f0116ba924fdad6efa86aab18524676e0eb6310661841ebd5ff1875a5f2` |
| 061 | `1c4bf791c89fa1d2d5ed23c59edb6b58779454ed48dfefd534dea27b1860d2c9` | `5960ca90339acdc7309ccf5860521b23c0120f691331053bb86cc5c596f1ff91` |
| 069 | `2e0c07949bcbe9cfa2e8f3bf2f49fb02c92fb1b23fed0d2b47deb101ae2e385a` | `19ee6466fbfd7b8ce1599c7895d5ac52c6d8a75b48e0d04fb5b3e6f839bafcb5` |
| 071 | `692237262301772ae5a7b6cc1adef804fb57370ccd2c2b417ffc716f55b45ebd` | `b4adb86da002032ef6b5962cf6a65b011f1d9ef057edfcc949c0f8d86fff3bae` |
| 074 | `84b25c94b58a707e123de52c1900903d28c620522793fd7630fa1ef96857da46` | `35621da13c6d622f3ec5dcb089511129828b9ff6199080ffe775a9269d99f38c` |
| 078 | `a06352425c9e7d799d5ce08f8f4a5a0aabea423534a2c799250679f54ebff571` | `1110730d9bdd6529c246e15f6df06d2ce5fba08e122d52624edc361c4ec13c79` |
