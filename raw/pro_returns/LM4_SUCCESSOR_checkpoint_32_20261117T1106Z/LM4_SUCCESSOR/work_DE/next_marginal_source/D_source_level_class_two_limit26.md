# The corrected D-source commutator is invisible to every color/chi-x-level detector

Research, checkpoint26. This is the result of the one prescribed exact-word
class-two test requested by root. It is a limitation of that detector,
not a proof or disproof of the actual relation `[m,D_s]=1`.

## 1. The actual whole-orbit class-two target

Use B127's literal splitting `F11=F(U1,...,U8)*T`, with
`T=F(f,g,x)` and `L=ker(F11->T)`. Its actual free basis is
`X_(t,i)=t Ui t^-1`. Put `chi_x(f)=chi_x(g)=0`, `chi_x(x)=1`.
There is a homomorphism from this free group to the free group
`F_level` on the generators `Y_(i,n)`, eight colors and all integer
levels, sending `X_(t,i)` to `Y_(i,chi_x(t))`.

For each of the complete forty node relators, retain the two signed
peripheral factors and their exact retained heads. Order their colors
with the first four-label half first. Let `D_ij` be the finite set of
differences `first level minus second level` occurring for that pair
of colors. The initial factor signs do not change the imposed
commutation. The complete forty-row table, including both original
signs, is stored in the certificate.

Define the class-two quotient `C_level` of `F_level` by imposing

\[
[Y_{i,n},Y_{j,n-d}]=1
\quad\text{for every integer }n\text{ and every }d\in D_{ij}.
\]

This is an actual quotient of `J=L/N`. Indeed every signed source
operator has the same positive peripheral core, has conjugator head
of chi-x value zero, and preserves chi-x on `T`. This is checked on
all thirty-two family images and twelve retained generator images.
Composition and inversion then preserve the two colors and their
level difference for **every** source word. Retained conjugation
shifts both levels equally; conjugation by `L` is irrelevant to a
central commutator. In a group of class two, the nonlinear peripheral
connectors do not alter the commutator of the two cores. Consequently
every translated defining node relation, not merely the forty seeds,
maps to one. This proves the required all-source/all-deck factorization.

## 2. A stronger exact collapse occurs before class two

Consider the literal free quotient

\[
q:F_{11}\longrightarrow F(U_1,\ldots,U_8,x)
\]

which kills the retained letters `f` and `g` separately. The kernel of
the further projection to `<x>` is exactly the preceding free group
`F_level`. The complete actual signed operator arrays satisfy

\[
q\alpha_m=q,\qquad q\alpha_{m^{-1}}=q.       \tag{1}
\]

This is a literal free-word identity on all eleven generators, not
just an identity after abelianization. The certificate deletes `f,g`
from each of the twenty-two actual images and checks that it becomes
the original remaining generator or the empty word, respectively.
Thus (1) holds on every free word.

Retain the complete actual contact words and set

\[
D_s=s_2s_1s_3^{-1}s_1^{-1}s_2^{-1}.
\]

The two actual free-word defects
`alpha_m(D_s)D_s^-1` and `alpha_m^-1(D_s)D_s^-1` have lengths
798 and 648 before this projection. Both reduce to the empty word
already in `F_level`, by (1), and hence have zero image in `C_level`.
The same conclusion holds in **every** further quotient that depends
only on the color and chi-x index, including individual missing-pair
free targets and finite residue-level class-two targets.

This is stronger than an unsuccessful choice of one coefficient:
the entire prescribed color/chi-x-level route cannot detect this
commutator. The discarded `f,g` directions are precisely information
that another target would have to retain. No conclusion about the
word in the actual unfilled group follows.

## 3. Exact attempts and scope

The producer imports no previous evaluator. It reads the complete
actual B123 operator array and B127 factor data. Its first attempt
incorrectly required both node cores to have positive signs; the
actual factorization permits negative cores. That source, stdout
and stderr are preserved under `initial_signed_core_assumption`.
The repaired proof uses absolute colors and retains the original
factor signs; the thirty-two operator cores are still verified
literally positive. There was no failed group-theoretic inference.

Stable files:

- `check_D_source_level_class_two26.py`, `.out`, `.err`, `.json`;
- all forty core-level records, twenty-two complete projected images,
  and both full defect words occur in the JSON;
- root independently read the repaired source and genuine output and
  accepted the universal filling limitation.

No broader target search or orbit-depth enumeration follows this test.
The separate full-retained mod-two comparison is owned by A.
