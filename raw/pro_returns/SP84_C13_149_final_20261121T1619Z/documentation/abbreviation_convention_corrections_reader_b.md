# Approved abbreviation and convention corrections — reader B

2026-11-21 15:47:12 UTC

The six abbreviation findings are metadata-only. Scan017 changes are conventions only: no ink resolution, source number, formula value, substantive witness count or audit changed count is altered. Exact draft wording is preserved below. All frozen comparison inputs and adjudications remain byte-identical.

## Scan 011

Path: `abbreviations`

```json
{
  "before": [
    {
      "form": "pt",
      "expansion": "point",
      "place": "Notons insertion and Le choix paragraph; a cancelled candidate also follows Ceci dit, le"
    },
    {
      "form": "géom$^t$",
      "expansion": "géométriquement",
      "place": "qui sont géom raised t conn."
    },
    {
      "form": "conn.",
      "expansion": "connexes",
      "place": "end of the baseline qui sont"
    },
    {
      "form": "géom.",
      "expansion": "géométriquement",
      "place": "interlinear et ... géom. intègres"
    },
    {
      "form": "géom.",
      "expansion": "géométrique",
      "place": "un pt géom. in Le choix paragraph"
    },
    {
      "form": "alg.",
      "expansion": "algébrique",
      "place": "clôture alg. de Q dans K"
    },
    {
      "form": "tt",
      "expansion": "tout",
      "place": "pour tt i insertion"
    },
    {
      "form": "syst.",
      "expansion": "système",
      "place": "qui forment un syst. projectif"
    }
  ],
  "after": [
    {
      "form": "pt",
      "expansion": "point",
      "place": "Le choix paragraph; pt is also a tentative alternative in the cancelled group after Ceci dit, le"
    },
    {
      "form": "p$^t$",
      "expansion": "point",
      "place": "Notons insertion; the t is raised"
    },
    {
      "form": "géom$^t$",
      "expansion": "géométriquement",
      "place": "qui sont géom raised t conn."
    },
    {
      "form": "conn.",
      "expansion": "connexes",
      "place": "end of the baseline qui sont"
    },
    {
      "form": "géom.",
      "expansion": "géométriquement",
      "place": "interlinear et ... géom. intègres"
    },
    {
      "form": "géom.",
      "expansion": "géométrique",
      "place": "un pt géom. in Le choix paragraph"
    },
    {
      "form": "alg.",
      "expansion": "algébrique",
      "place": "clôture alg. de Q dans K"
    },
    {
      "form": "tt",
      "expansion": "tout",
      "place": "pour tt i insertion"
    },
    {
      "form": "syst.",
      "expansion": "système",
      "place": "qui forment un syst. projectif"
    }
  ]
}
```

## Scan 015

Path: `abbreviations.3.form`

```json
{
  "before": "tors. (alternative only)",
  "after": "tors (uncertain alternative)"
}
```

Path: `abbreviations.3.place`

```json
{
  "before": "Cancelled word at the start of L16",
  "after": "Cancelled word at the start of L16; torsion/tors is uncertain, and the following colon/point is a separate punctuation doubt"
}
```

## Scan 017

Path: `changes.8.evidence`

```json
{
  "before": "The complete insertion leader attaches et and the Gamma equality before baseline sont des. Both indexed letters have angular capital K arms, matching the adjacent pi subscript; the kernel pi is small relative to those capitals. A raised cluster, clipped at the top of the frozen b11 rectangle, is independently visible in the full lower half and the single supplementary scope crop. It has an open left curve, faint middle trace and right hooked descent, permitting tentative can but not a certain reading. Its height and position above the index support superscript placement on the right Gamma. Record the cluster explicitly; the second reader’s illegible{1} is a placeholder, not evidence for the numeral 1.",
  "after": "The complete insertion leader attaches et and the Gamma equality before baseline sont des. Both indexed letters have angular capital K arms, matching the adjacent pi subscript; the kernel pi is small relative to those capitals. A raised cluster, clipped at the top of the frozen b11 rectangle, is independently visible in the full lower half and the single supplementary scope crop. It has an open left curve, faint middle trace and right hooked descent, permitting tentative can but not a certain reading. Its height and position above the index support superscript placement on the right Gamma. Record the cluster explicitly; the second reader’s illegible{1} is a placeholder, not evidence for the numeral 1. Current formula serialization uses \\unsure{can}: the unresolved raised traces remain a low-confidence cluster, not a securely recovered word. The former empty \\illegible{} alternative is removed only because that macro is not permitted for a symbol inside a formula; this is not an ink resolution."
}
```

Path: `changes.8.final`

```json
{
  "before": "$\\pi=\\pi_{\\bar K/K}$ \\inserted{et $\\Gamma=\\Gamma_{\\bar K/K}^{\\unsure{can|\\illegible{}}}$} sont des",
  "after": "$\\pi=\\pi_{\\bar K/K}$ \\inserted{et $\\Gamma=\\Gamma_{\\bar K/K}^{\\unsure{can}}$} sont des"
}
```

Path: `doubts.3.reading`

```json
{
  "before": "\\Gamma_{\\bar K/K}^{\\unsure{can|\\illegible{}}}",
  "after": "\\Gamma_{\\bar K/K}^{\\unsure{can}}"
}
```

Path: `doubts.3.reason`

```json
{
  "before": "The complete insertion leader attaches et and the Gamma equality before baseline sont des. Both indexed letters have angular capital K arms, matching the adjacent pi subscript; the kernel pi is small relative to those capitals. A raised cluster, clipped at the top of the frozen b11 rectangle, is independently visible in the full lower half and the single supplementary scope crop. It has an open left curve, faint middle trace and right hooked descent, permitting tentative can but not a certain reading. Its height and position above the index support superscript placement on the right Gamma. Record the cluster explicitly; the second reader’s illegible{1} is a placeholder, not evidence for the numeral 1.",
  "after": "The complete insertion leader attaches et and the Gamma equality before baseline sont des. Both indexed letters have angular capital K arms, matching the adjacent pi subscript; the kernel pi is small relative to those capitals. A raised cluster, clipped at the top of the frozen b11 rectangle, is independently visible in the full lower half and the single supplementary scope crop. It has an open left curve, faint middle trace and right hooked descent, permitting tentative can but not a certain reading. Its height and position above the index support superscript placement on the right Gamma. Record the cluster explicitly; the second reader’s illegible{1} is a placeholder, not evidence for the numeral 1. Current formula serialization uses \\unsure{can}: the unresolved raised traces remain a low-confidence cluster, not a securely recovered word. The former empty \\illegible{} alternative is removed only because that macro is not permitted for a symbol inside a formula; this is not an ink resolution."
}
```

Path: `inventory.10.first_words_or_objects`

```json
{
  "before": "et \\Gamma=\\Gamma_{\\bar K/K}^{\\unsure{can|\\illegible{}}}",
  "after": "et \\Gamma=\\Gamma_{\\bar K/K}^{\\unsure{can}}"
}
```

Path: `notation.5.evidence`

```json
{
  "before": "The complete insertion leader attaches et and the Gamma equality before baseline sont des. Both indexed letters have angular capital K arms, matching the adjacent pi subscript; the kernel pi is small relative to those capitals. A raised cluster, clipped at the top of the frozen b11 rectangle, is independently visible in the full lower half and the single supplementary scope crop. It has an open left curve, faint middle trace and right hooked descent, permitting tentative can but not a certain reading. Its height and position above the index support superscript placement on the right Gamma. Record the cluster explicitly; the second reader’s illegible{1} is a placeholder, not evidence for the numeral 1.",
  "after": "The complete insertion leader attaches et and the Gamma equality before baseline sont des. Both indexed letters have angular capital K arms, matching the adjacent pi subscript; the kernel pi is small relative to those capitals. A raised cluster, clipped at the top of the frozen b11 rectangle, is independently visible in the full lower half and the single supplementary scope crop. It has an open left curve, faint middle trace and right hooked descent, permitting tentative can but not a certain reading. Its height and position above the index support superscript placement on the right Gamma. Record the cluster explicitly; the second reader’s illegible{1} is a placeholder, not evidence for the numeral 1. Current formula serialization uses \\unsure{can}: the unresolved raised traces remain a low-confidence cluster, not a securely recovered word. The former empty \\illegible{} alternative is removed only because that macro is not permitted for a symbol inside a formula; this is not an ink resolution."
}
```

Path: `notation.5.rendering`

```json
{
  "before": "\\inserted{et $\\Gamma=\\Gamma_{\\bar K/K}^{\\unsure{can|\\illegible{}}}$}",
  "after": "\\inserted{et $\\Gamma=\\Gamma_{\\bar K/K}^{\\unsure{can}}$}"
}
```

Path: `notation.5.written`

```json
{
  "before": "\\Gamma=\\Gamma_{\\bar K/K}^{\\unsure{can|\\illegible{}}}",
  "after": "\\Gamma=\\Gamma_{\\bar K/K}^{\\unsure{can}}"
}
```

Path: `notes`

```json
{
  "before": [
    "Scan017 is a handwritten continuation sheet bearing the author’s page number 8 at the top and separate thin foliation 16 at the lower left. No date or title is present. The latter number is treated as another or uncertain hand, not as the author’s numbering.",
    "The opening continuation describes an exterior action of Gamma on pi and shows its pullback from the universal extension in diagram (15). The diagram has five objects in its upper row, four rightward arrows, and Gamma below Aut ext(pi) with an upward arrow labelled phi on its right. All endpoints and labels were inspected; this is transcription, not a mathematical verification.",
    "The main paragraph discusses the choices of a fixed Gamma, a universal cover and a pair (K, K-bar), then describes these through triples (pi, Gamma, phi). The last sentence continues beyond the leaf. The source abbreviations alg., rev. and ext. are retained.",
    "The literal wording signifie inserted est qu’on and the phrase avec une fidélité qui met à cœur are retained. The clear insertion and letterforms are not repaired for grammatical sense. The independent audit reads décrivons, agreeing with H at that verb; the following word remains cœur, not examiner.",
    "Four interlinear additions are separately retained: un, est, K after ext., and et Gamma=Gamma_{K-bar/K} with a doubtful raised can/unreadable cluster on the right Gamma. Their leaders were traced to their attachment points. In the last addition, sont des belongs to the main baseline. Its capital K subscript forms match the neighbouring pi equality; the source notation is not silently reconciled with the earlier Gamma_{Q-bar/k}. No mathematical consistency claim is made.",
    "All three listed C marks were examined: M1006 resolves to est, M1007 to met, and M1008 remains a dash/arrow doubt. Three further C doubts inside cancellations, absent from marks.tsv, were also cropped: the first now retains ain/un/une alternatives, the second compatible/correspond alternatives, and S K-bar is resolved from the two visible glyphs and the overbar. No expansion to Spec is supplied in that cancelled fragment.",
    "The final map shaft retains a limited terminal-shape doubt. Its complete formula is in the audit boxes. The two unresolved cancelled prose runs retain ain/un/une and compatible/correspond alternatives in place; compatible is not asserted as a certain recovery of the obscured word.",
    "The initial differences file was malformed and contained later-page rows. Reading stopped once the contamination was recognized; root supplied a corrected file containing exactly 18 proper scan017 rows. Coverage below follows that corrected row order. No later-page material was used for this page.",
    "Reading coverage: whole image once and each supplied full-resolution half once; then twelve saved crops. The 26 manuscript line units comprise three opening prose lines, two diagram rows, fifteen main-paragraph baseline lines, four insertion lines, and two folio-number lines. All agreed words and signs were checked against the ink. The retained crop paths and original boxes are stable.",
    "Reader: /root/reader_b; model GPT-6 Astra Pro; effort not exposed; run SP84_C13_149. No OCR, external research, TeX compilation, proof check, or formal computation was performed.",
    "Independent audit: all12 differing boxes and34 token spans personally inspected. Four boxes changed: the two cancelled words gain alternatives, décrivons replaces décrirons, and a previously omitted raised cluster is recorded tentatively as can or unreadable. The frozen b11 rectangle clipped its top; one supplementary full-formula scope crop is documented, preserving the original rectangle. No mathematical check was added."
  ],
  "after": [
    "Scan017 is a handwritten continuation sheet bearing the author’s page number 8 at the top and separate thin foliation 16 at the lower left. No date or title is present. The latter number is treated as another or uncertain hand, not as the author’s numbering.",
    "The opening continuation describes an exterior action of Gamma on pi and shows its pullback from the universal extension in diagram (15). The diagram has five objects in its upper row, four rightward arrows, and Gamma below Aut ext(pi) with an upward arrow labelled phi on its right. All endpoints and labels were inspected; this is transcription, not a mathematical verification.",
    "The main paragraph discusses the choices of a fixed Gamma, a universal cover and a pair (K, K-bar), then describes these through triples (pi, Gamma, phi). The last sentence continues beyond the leaf. The source abbreviations alg., rev. and ext. are retained.",
    "The literal wording signifie inserted est qu’on and the phrase avec une fidélité qui met à cœur are retained. The clear insertion and letterforms are not repaired for grammatical sense. The independent audit reads décrivons, agreeing with H at that verb; the following word remains cœur, not examiner.",
    "Four interlinear additions are separately retained: un, est, K after ext., and et Gamma=Gamma_{K-bar/K} with a doubtful raised can cluster with unresolved traces on the right Gamma. Their leaders were traced to their attachment points. In the last addition, sont des belongs to the main baseline. Its capital K subscript forms match the neighbouring pi equality; the source notation is not silently reconciled with the earlier Gamma_{Q-bar/k}. No mathematical consistency claim is made.",
    "All three listed C marks were examined: M1006 resolves to est, M1007 to met, and M1008 remains a dash/arrow doubt. Three further C doubts inside cancellations, absent from marks.tsv, were also cropped: the first now retains ain/un/une alternatives, the second compatible/correspond alternatives, and S K-bar is resolved from the two visible glyphs and the overbar. No expansion to Spec is supplied in that cancelled fragment.",
    "The final map shaft retains a limited terminal-shape doubt. Its complete formula is in the audit boxes. The two unresolved cancelled prose runs retain ain/un/une and compatible/correspond alternatives in place; compatible is not asserted as a certain recovery of the obscured word.",
    "The initial differences file was malformed and contained later-page rows. Reading stopped once the contamination was recognized; root supplied a corrected file containing exactly 18 proper scan017 rows. Coverage below follows that corrected row order. No later-page material was used for this page.",
    "Reading coverage: whole image once and each supplied full-resolution half once; then twelve saved crops. The 26 manuscript line units comprise three opening prose lines, two diagram rows, fifteen main-paragraph baseline lines, four insertion lines, and two folio-number lines. All agreed words and signs were checked against the ink. The retained crop paths and original boxes are stable.",
    "Reader: /root/reader_b; model GPT-6 Astra Pro; effort not exposed; run SP84_C13_149. No OCR, external research, TeX compilation, proof check, or formal computation was performed.",
    "Independent audit: all12 differing boxes and34 token spans personally inspected. Four boxes changed: the two cancelled words gain alternatives, décrivons replaces décrirons, and a previously omitted raised cluster is recorded tentatively as can with unresolved raised traces. The frozen b11 rectangle clipped its top; one supplementary full-formula scope crop is documented, preserving the original rectangle. No mathematical check was added.",
    "Convention-only repair after the completed audit: the tentative Gamma superscript now uses \\unsure{can}, with its unresolved traces still described in the doubts record. The formula no longer uses an empty illegible macro. Diagram(15) is placed in text mode with \\noindent (15)\\quad\\diagram{...}, matching scans010–011, because the supplied diagram macro contains paragraph/center commands. The number, objects, arrows, labels and all source readings are unchanged. Frozen first/second readings, adjudications and audit counts retain their historical values."
  ]
}
```

## Scan 018

Path: `abbreviations.0.expansion`

```json
{
  "before": "ensemble",
  "after": "ensemble if ens is the written form; en remains an unresolved alternative"
}
```

Path: `abbreviations.0.form`

```json
{
  "before": "\\unsure{ens}",
  "after": "\\unsure{ens|en}"
}
```

Path: `abbreviations.0.place`

```json
{
  "before": "line 8, after l' at the end of line 7; expansion explanatory only",
  "after": "line8, after l' at the end of line7; expansion explanatory and conditional only"
}
```

## Scan 019

Path: `abbreviations`

```json
{
  "before": [
    {
      "form": "pts",
      "expansion": "points",
      "place": "L7, item 2"
    },
    {
      "form": "rev.",
      "expansion": "revêtements",
      "place": "L8, item 2"
    },
    {
      "form": "pro-gr",
      "expansion": "pro-groupe",
      "place": "L11, item 3"
    },
    {
      "form": "i.e.",
      "expansion": "id est",
      "place": "L13, item 4"
    },
    {
      "form": "hom",
      "expansion": "homomorphisme",
      "place": "L15, item 4"
    },
    {
      "form": "ss-groupe",
      "expansion": "sous-groupe",
      "place": "L16, cancelled line"
    },
    {
      "form": "alg.",
      "expansion": "algébrique",
      "place": "L17 and L20, item 5"
    },
    {
      "form": "néc.",
      "expansion": "nécessairement",
      "place": "left margin, rotated row 2"
    }
  ],
  "after": [
    {
      "form": "pts",
      "expansion": "points",
      "place": "L7, item 2"
    },
    {
      "form": "rev.",
      "expansion": "revêtements",
      "place": "L8, item 2"
    },
    {
      "form": "pro-gr",
      "expansion": "pro-groupe",
      "place": "L11, item 3"
    },
    {
      "form": "i.e.",
      "expansion": "id est",
      "place": "L13, item 4"
    },
    {
      "form": "hom",
      "expansion": "homomorphisme",
      "place": "L15, item 4"
    },
    {
      "form": "ss-groupe",
      "expansion": "sous-groupe",
      "place": "L16, cancelled line"
    },
    {
      "form": "alg.",
      "expansion": "algébrique",
      "place": "L17 and L20, item 5"
    },
    {
      "form": "néc.",
      "expansion": "nécessairement",
      "place": "left margin, rotated row 2"
    },
    {
      "form": "\\unsure{gr.-oïde|gr.-oïdes}",
      "expansion": "groupoïde(s)",
      "place": "left margin, rotated row1; singular/plural ending remains uncertain"
    }
  ]
}
```

## Scan 021

Path: `abbreviations.2.expansion`

```json
{
  "before": "théorème",
  "after": "théorème if th./Th. is written; H. remains unresolved"
}
```

Path: `abbreviations.2.form`

```json
{
  "before": "\\unsure{th.|Th.}",
  "after": "\\unsure{th.|Th.|H.}"
}
```

Path: `abbreviations.2.place`

```json
{
  "before": "line 5; case uncertain",
  "after": "line5; the letter sequence and case remain uncertain"
}
```

## Scan 022

Path: `abbreviations`

```json
{
  "before": [
    {
      "form": "t.f.",
      "expansion": "type fini",
      "place": "theorem"
    },
    {
      "form": "hom. / hom",
      "expansion": "homomorphisme(s)",
      "place": "proof opening and lower reformulations; the stop is local"
    },
    {
      "form": "car",
      "expansion": "caractéristique",
      "place": "upper marginal note"
    },
    {
      "form": "démon.",
      "expansion": "démonstration",
      "place": "upper marginal note"
    },
    {
      "form": "alg.",
      "expansion": "algébrique(s)",
      "place": "lower paragraph and middle marginal note"
    },
    {
      "form": "d'exten",
      "expansion": "d'extension(s)",
      "place": "cancelled phrase after live que"
    },
    {
      "form": "chgt",
      "expansion": "changement",
      "place": "bottom marginal cancellation"
    },
    {
      "form": "i.e.",
      "expansion": "id est",
      "place": "parenthetical explanation before the square"
    }
  ],
  "after": [
    {
      "form": "t.f.",
      "expansion": "type fini",
      "place": "theorem"
    },
    {
      "form": "hom. / hom",
      "expansion": "homomorphisme(s)",
      "place": "proof opening and lower reformulations; the stop is local"
    },
    {
      "form": "dém.",
      "expansion": "démonstration",
      "place": "upper marginal note, la dém. montre bien"
    },
    {
      "form": "pr",
      "expansion": "pour (proposed)",
      "place": "upper marginal parenthesis, bien que pr la"
    },
    {
      "form": "\\unsure{démon.|démonstr.}",
      "expansion": "démonstration",
      "place": "upper marginal parenthesis; the abbreviated ending remains uncertain"
    },
    {
      "form": "alg.",
      "expansion": "algébrique(s)",
      "place": "lower paragraph and middle marginal note"
    },
    {
      "form": "d'exten",
      "expansion": "d'extension(s)",
      "place": "cancelled phrase after live que"
    },
    {
      "form": "chgt",
      "expansion": "changement",
      "place": "bottom marginal cancellation"
    },
    {
      "form": "i.e.",
      "expansion": "id est",
      "place": "parenthetical explanation before the square"
    }
  ]
}
```

## Exact scan017 page replacements

Before:
```tex
\unsure{can|\illegible{}}
```
After:
```tex
\unsure{can}
```

Before:
```tex
\[
(15)\qquad
\diagram{\begin{tikzcd}[ampersand replacement=\&]
1\arrow[r]\&\pi\arrow[r]\&\operatorname{Aut}(\pi)\arrow[r]\&\operatorname{Aut\,ext}(\pi)\arrow[r]\&1\\
\&\&\&\Gamma\arrow[u,"\varphi"']\&
\end{tikzcd}}
\]
```
After:
```tex
\noindent (15)\quad\diagram{\begin{tikzcd}[ampersand replacement=\&]
1\arrow[r]\&\pi\arrow[r]\&\operatorname{Aut}(\pi)\arrow[r]\&\operatorname{Aut\,ext}(\pi)\arrow[r]\&1\\
\&\&\&\Gamma\arrow[u,"\varphi"']\&
\end{tikzcd}}
```
