# Technical LaTeX review of the saved page fragments

> This is the initial technical snapshot, preserved with its matching
> `static_results.json`. Several findings have subsequently been fixed by the
> primary auditor. See `INTERIM_ENCODING_REVIEW.md` for the targeted follow-up.
> The completed final validation is now in `FINAL_TECHNICAL_REPORT.md` and
> `final_validation.json`; it supersedes this initial snapshot.

## Scope and result

This review is limited to the 42 `.tex` fragments in `../pages/`. No scan images,
context files, or archives were opened. No transcription file was edited. The
review does not judge wording, readings, mathematical correctness, or intended
diagram geometry.

The associated `static_results.json` records the UTC check time, SHA-256 hash,
and line count of every reviewed file. Because the primary transcription audit
may still change those files, that manifest identifies the exact snapshot to
which this report applies. All filenames below have the prefix
`MPL_138_046-089_138_` and reside in `../pages/`.

The static pass found three concrete mode hazards at three locations, plus five
math-array call sites whose success depends on the custom `\diagram` definition.
Braces, environments, and explicit math delimiters are balanced in the checked
snapshot. Balanced delimiters do not establish correct mode nesting: scan051
line 5 illustrates that distinction.

The checker inspected 110 `\arrow[...]` option lists. No unknown option remained
after review of the keys actually used. No additional clear standard-command
misspelling was found.

## 1. Concrete mode hazards

The remedies below change only LaTeX encoding. They preserve the existing
characters, mathematical tokens, and annotation nesting. These are suggestions;
this review applied none of them.

### `scan051.tex`, line 5

The saved fragment is already within `\[ ... \]`, but contains:

```latex
\uline{$\cos^2u$}
```

The additional dollar delimiters are unsafe when `\uline` is operating in the
existing math mode, as with the standard `ulem` math-mode behavior. A minimal
encoding is:

```latex
\uline{\cos^2u}
```

The explicitly mathematical spelling is `\underline{\cos^2u}`. If the project's
custom `\uline` intentionally accepts text only, the alternative is to enter
text explicitly around the original argument:

```latex
\text{\uline{$\cos^2u$}}
```

Choose the form consistent with the actual macro definition; do not leave
uncontrolled inner dollar delimiters in a math argument. The `ulem` manual
describes its commands as primarily textual, notes only approximate math-mode
support, and retains `\underline` for mathematical use [1].

### `scan060.tex`, line 31

This occurs in running text:

```latex
\deleted{\unsure{G_x}}
```

The raw subscript needs math mode unless an annotation macro supplies it. A
conservative mode-independent encoding is:

```latex
\deleted{\unsure{\ensuremath{G_x}}}
```

Putting `$G_x$` in the same innermost position also works if the annotation
definitions establish text there. `\ensuremath` is safer across both callers.

### `scan068.tex`, line 8

After the closing `$s\geq p$`, running text contains:

```latex
\deleted{\unsure{\frac1p+\frac13+\frac12}}
```

All three `\frac` tokens require math mode. Preserve the exact token sequence
inside an explicit math wrapper:

```latex
\deleted{\unsure{\ensuremath{\frac1p+\frac13+\frac12}}}
```

No other unambiguous raw math-only command in running text was found by this
pass. `\ldots` in scan072 line 3 is not a defect: LaTeX supports it in text mode.

## 2. `\diagram` calls that require math mode

The fragment files do not supply the definition of `\diagram`. These five calls
contain math-only material without local math delimiters:

| File | Lines | Body begins with |
| --- | --- | --- |
| `MPL_138_046-089_138_scan047.tex` | 23–25 | `\boxed{\begin{array}{ccc}` |
| `MPL_138_046-089_138_scan047.tex` | 30 | `\boxed{\begin{array}{ccc}` |
| `MPL_138_046-089_138_scan060.tex` | 14–16 | `\begin{array}{ccccccccc}` |
| `MPL_138_046-089_138_scan062.tex` | 16–19 | `\begin{array}{ll}` |
| `MPL_138_046-089_138_scan066.tex` | 65–70 | `\left\{\begin{array}{lll}` |

If `\diagram` already establishes math mode for these bodies, no change is
required. Otherwise wrap the complete existing body at each listed call site:

```latex
\diagram{\ensuremath{<the complete existing math body>}}
```

For example, wrap the complete `\left\{ ... \right.` construction together,
not merely its `array`. This keeps the delimiter pair in one math group.

Do not resolve these sites by placing every `\diagram` argument in math mode:
the same macro also wraps `tabular` environments, `tikzcd` environments, and at
least one body that already contains explicit `$...$`. Its implementation must
accommodate those distinct contents, or the math-only call sites must mark
their own mode.

## 3. Other underlining within math

The following calls contain no nested dollar delimiters and are not identified
as definite errors. They matter if a rendering wrapper replaces the project's
underlining macros with text-only implementations.

| File and line | Current call | Conservative compatibility option |
| --- | --- | --- |
| `MPL_138_046-089_138_scan060.tex:10` | `\uuline{\text{Surj}}` | `\text{\uuline{Surj}}` keeps the double underline in text mode. |
| `MPL_138_046-089_138_scan061.tex:28` | `\uline{\text{surjection}}` | `\text{\uline{surjection}}` if the custom command is text-only. |
| `MPL_138_046-089_138_scan062.tex:17` | `\uline{\text{Sommets}}` | `\text{\uline{Sommets}}` under the same condition. |
| `MPL_138_046-089_138_scan062.tex:18` | `\uline{\text{arêtes}}` | `\text{\uline{arêtes}}` under the same condition. |
| `MPL_138_046-089_138_scan066.tex:39` | `\uline{N\text{ quelconque}}` | A mode-aware `\uline` is suitable; native math spelling is `\underline{N\text{ quelconque}}`. |

These are conditional compatibility alternatives, not recommendations to alter
valid standard `ulem` calls indiscriminately.

## 4. TikZ and TikZ-cd findings

### Option syntax

The currently used arrow keys, including `dash`, `dashed`, `dotted`, `tail`,
`leftrightarrow`, `mapsto`, `draw=none`, `bend left`, `bend right`, and
`shorten <`/`shorten >`, are recognizable TikZ/TikZ-cd syntax. Quoted labels
followed by `description` or `near start` are label-option syntax, not bare
text leaking into the key list.

The originally reported `\arrow[d,\unsure{dash}]` on scan047 line 49 is absent
from the checked snapshot; that option now uses `draw=none` with a label.

The old spelling `uu rrr` on scan053 line 27 was not itself a confirmed syntax
error. The official direction parser consumes undelimited tokens, which skip
ordinary spaces [2]. The current saved spelling is `uurrr`. Both specify the
same movement.

### Existing coordinate observations requiring the primary visual audit

These observations describe the saved matrix coordinates only. They do not
infer the intended handwritten connections.

| File and line | Saved endpoint behavior | Encoding only if the stated intended endpoint is confirmed |
| --- | --- | --- |
| `MPL_138_046-089_138_scan053.tex:27` | From row 7, column 2, `uurrr` reaches the explicit empty `{}` at row 5, column 5. | An explicitly created empty node may be intentional. No unconditional change is proposed. |
| `MPL_138_046-089_138_scan078.tex:7` | From row 1, column 3, `ddll`/`ddrr` reach empty row 3, columns 1/5. | If destinations are the existing row 4, columns 1/5 nodes, use `dddll`/`dddrr`. |
| `MPL_138_046-089_138_scan078.tex:11` | From row 5, column 3, `ul`/`ur` reach empty row 4, columns 2/4. | If destinations are the existing row 3, columns 2/4 nodes, use `uul`/`uur`. |
| `MPL_138_046-089_138_scan078.tex:11` | `uuuu` reaches row 1, column 3; the row 2, column 3 node is one row closer. | If the latter node is intended, use `uuu`. |

### Macro argument tokenization

The `tikzcd` environments are passed as arguments to `\diagram`. An ordinary
argument-capturing macro can tokenize their `&` separators before TikZ installs
the matrix catcodes, causing the familiar wrong-ampersand-catcode failure. The
actual project definition may already handle this. For a generic compilation
wrapper, either use a definition that safely handles that tokenization or
encode affected matrices with `ampersand replacement=\&` and corresponding
`\&` separators. The latter is an encoding change, and should be applied
consistently within each affected matrix. This review did not modify them.

Similarly, annotation macros such as `\deleted` must accept both math and text,
and some uses span paragraphs or displays. Defining them as a text-only box or
a short, non-paragraph macro would introduce wrapper failures unrelated to the
readings. The prescribed custom `\figure{...}` name also coincides with the
standard LaTeX float macro; a test preamble must deliberately redefine that
name instead of blindly issuing `\newcommand{\figure}`.

## 5. Reproducing the static check and its limits

From the project directory:

```sh
python technical_qa/static_latex_check.py --json technical_qa/static_results.json
```

The script reads only `.tex` files from its selected pages directory and writes
only the explicitly requested JSON output. It reports structural mismatches,
recognized math commands in text, raw script characters in text, explicit math
delimiters inside math, conditional math-array wrappers, underlining calls in
math, and arrow options outside its small reviewed allowlist. It does not
expand custom macros or validate mathematical content.

The JSON contains 14 token-level findings, which consolidate to the three mode
hazard locations and five conditional `\diagram` call sites above. Repeated
tokens at one site are separate machine findings. It also inventories six
underlining calls in math and 110 arrow option lists.

No successful compilation is claimed. `pdflatex`, `lualatex`, and `xelatex`
executables are available, but `kpsewhich` could not locate `article.cls`,
`amsmath.sty`, `tikz.sty`, `tikz-cd.sty`, or `latex.fmt`. The pass therefore
remained static. The original structural check also passed all 42 fragments.

## Technical references

1. Donald Arseneau, [The ulem package](https://ctan.math.illinois.edu/macros/latex/contrib/ulem/ulem.pdf),
   2019-11-18, sections 1 and 3. Consulted only for package behavior, not for any
   transcription reading.
2. Augusto Stoffel, [TikZ-cd source](https://github.com/astoff/tikz-cd/blob/master/tikzlibrarycd.code.tex),
   specifically the direction parser and quoted-label handling. This is the
   repository linked by the [CTAN package page](https://ctan.org/pkg/tikz-cd).
