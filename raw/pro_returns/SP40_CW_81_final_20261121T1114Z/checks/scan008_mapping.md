# Scan008 — merged decision and inventory map

This is a text-only consolidation. Root-supplied ink decisions are applied; `main_adjudicated` remains false pending root approval. Every report row and every source inventory entry is retained verbatim in the JSON. No image was opened and no mathematical check or TeX compilation was performed by the clerk.

## Coverage and counts

{
  "decision_loci": 21,
  "C_difference_loci": 13,
  "H_difference_loci": 0,
  "actual_C_doubt_loci": 7,
  "actual_C_doubts_retained": 6,
  "actual_C_doubts_resolved": 1,
  "remaining_doubt_or_graphic_uncertainty_loci": 10,
  "inventory_elements": 45,
  "source_difference_rows": {
    "A": 14,
    "B": 12,
    "C": 15
  },
  "source_inventory_rows": {
    "A": 41,
    "B": 42,
    "C": 42
  },
  "check_events": 4
}

There are21 distinct decision components and13 C-difference loci under the explicit counting policy below. H supplies no text: every H value is null and every diff_H is false. The seven actual C doubts produce six retentions and one resolution. The10 remaining entries include6 original reading doubts and4 additional mark/graphic uncertainties.

## Decisions and reader differences

| Decision | Locus | Source row IDs A / B / C | Root decision | C difference | Confidence |
| --- | --- | --- | --- | --- | --- |
| 008-01 | Second implication: Car/car | A01 / TeX/audit / TeX/audit | \text{Car } | True | high |
| 008-02 | First isolated struck line | A02 / B008_D01 / 008-C-01 | \deleted{donc si $\unsure{p\ne1\|p\ne q}$} | False | low |
| 008-03 | ou p=1 insertion below p premier and triangular mark | A03 / TeX/audit / TeX/audit | ou p=1 below p premier, with a small filled left-pointing triangle above the insertion; function unassigned. | True | medium |
| 008-04 | Cancelled parenthesis on l'impose sans risque / si p=1 | A04 / B008_D09 / 008-C-09 | Same deleted words and tall parentheses, in two physical lines, crossed by two separate rising diagonal strokes. | True | high |
| 008-05 | Second existential line: ζ/δ | A05 / B008_D02 / 008-C-02 | \unsure{\zeta\|\delta} | False | medium |
| 008-06 | Detached mark above a in et si a=a0 a-double-prime | TeX/audit / B008_D08 / TeX/audit | \overset{\unsure{\cdot\|\prime}}{a}=a_0a'' | True | low |
| 008-07 | Cancelled lower item under a prime | A06 / B008_D03 / 008-C-03 | a_{\deleted{\unsure{0}}}' | False | low |
| 008-08 | Numerical-example frame and shared upper hypothesis rule | A07 / TeX/audit / TeX/audit | Open-right example frame whose left side reaches a shared page-wide upper rule along the example bottom; separate lower rule beneath the hypothesis. | True | high |
| 008-09 | Cancelled alors immediately before on a | A08 / B008_D04 / 008-C-04 | \deleted{\unsure{alors}} | False | low |
| 008-10 | Pale primed letter in addition after on a | A09 / B008_D07 / 008-C-07 | \inserted{$p=q,\ {\unsure{a\|\alpha}}'=\gamma$} | False | medium |
| 008-11 | Curved mark below the pale p=q comma and the apostrophe of C’est | TeX/audit / B008_D07 / 008-C-08 | One pale formula comma and one apostrophe in C’est; no additional duplicate mark. | False | high |
| 008-12 | Cancelled p²/p before the lower q squared | A10 / B008_D05 / 008-C-05 | \deleted{\unsure{p^{2}\|p}} | False | low |
| 008-13 | First lower ou p=1 cancellation and returning stroke | A12 / B008_D10 / 008-C-10 | Same cancelled ou p=1, with crossing stroke and lower return drawn explicitly. | True | high |
| 008-14 | Second lower ou p=1 implies p=1 cancellation direction | A11 / B008_D11 / 008-C-12 | Same cancelled ou p=1 implies p=1, crossed by one long rising stroke. | True | high |
| 008-15 | Pale absurde car q nondivides a above the second cancelled continuation | A11 / B008_D11 / 008-C-11 | Pale inserted absurde car q∤a physically above the cancelled ou p=1⇒p=1. | True | high |
| 008-16 | Faint residual strokes and points above the right end of the lower implications | TeX/audit / TeX/audit / 008-C-14 | Approximate gray drawing of the pale curved strokes, short strokes and detached points; no character, source or hand assigned. | True | low |
| 008-17 | Final cancelled q and raised qα−1: glyphs and relative placement | A13 / B008_D06 / 008-C-06 | Cancelled lower q with uncrossed qα−1 physically raised above and to its right; no algebraic attachment or chronology assigned. | True | high |
| 008-18 | Repeated oblique cancellation returns and lower tail around final q | A13 / B008_D06 / 008-C-13 | Explicit repeated oblique returns crossing the lower q, with lower extending tail/hook. | False | high |
| 008-19 | Detached rising stroke upper-left of l'ensemble | A14 / TeX/audit / TeX/audit | \unsure{/} immediately above and left of l'ensemble; role, hand and attachment unresolved. | True | low |
| 008-20 | Return arrow: below-note start, detached point and curved left-pointing head | TeX/audit / B008_D12 / 008-C-15 | Detached point before the lower shaft beside the final parenthesis, below the note; rising right shaft and explicit curved left-pointing head. | True | high |
| 008-21 | Upper-right mottled trace: root-only drawing | TeX/audit / TeX/audit / TeX/audit | Tiny gray approximation of separate dark patches, short curves and pale intervals at upper right; no character, source, hand or role assigned. | True | low |


### 008-01 — Second implication: Car/car

A has Car; B and C-reader retain car in their TeX and audits.

**Root evidence:** Root supplied decision: the tall open C rises substantially above a/r; adopt capital Car.

**Crop:** `crops/008/01_car_case.png`.

| Reader | Exact returned reading / source excerpt | Source |
| --- | --- | --- |
| A | \text{Car } | A01 |
| B | \Longrightarrow\quad &p\mid q\,a^{q-1}\qquad\text{car }p\mid b'\ \text{et pour }i\ne q-1\quad q-i-1\deleted{\ne0}>0 | readers/008/B/reading.tex or audit (exact excerpt/provenance in JSON) |
| C | \Longrightarrow\quad &p\mid q\,a^{q-1}\qquad\text{car }p\mid b'\ \text{et pour }i\ne q-1\quad q-i-1\deleted{\ne0}>0 | readers/008/C/reading.tex or audit (exact excerpt/provenance in JSON) |


### 008-02 — First isolated struck line

All three preserve the same p≠1/p≠q alternatives and cancellation.

**Root evidence:** Root supplied decision: crossing strokes merge the last head and upper turn; retain both candidates.

**Crop:** `readers/008/B/02_isolated_cancel.png`.

| Reader | Exact returned reading / source excerpt | Source |
| --- | --- | --- |
| A | \deleted{donc si $\unsure{p\ne1\|p\ne q}$} | A02 |
| B | \deleted{donc si $\unsure{p\ne1\|p\ne q}$} | B008_D01 |
| C | \deleted{donc si $\unsure{p\ne1\|p\ne q}$} | 008-C-01 |


### 008-03 — ou p=1 insertion below p premier and triangular mark

A explicitly draws the triangle and the vertical placement. B preserves the words and describes them below premier. C-reader audit mentions a small attachment mark, but its TeX has no separate mark. No extra difference is counted for ordinary line wrapping.

**Root evidence:** Root supplied decision: adopt the small triangular patch and the below-premier insertion placement.

**Crop:** `crops/008/02_insert_mark.png`.

Shape/placement is retained without assigning an unestablished role or hand.

| Reader | Exact returned reading / source excerpt | Source |
| --- | --- | --- |
| A | Same addition below premier, with small filled triangular mark immediately above | A03 |
| B | Donc si $p\ne q$ \quad $p$ premier \inserted{ou $p=1$} et $p\mid b'$ alors $\alpha'=q\alpha$ | readers/008/B/reading.tex or audit (exact excerpt/provenance in JSON) |
| C | Donc si $p\ne q$ \quad $p$ premier \inserted{ou $p=1$} et $p\mid b'$ alors $\alpha'=q\alpha$ | readers/008/C/reading.tex or audit (exact excerpt/provenance in JSON) |


### 008-04 — Cancelled parenthesis on l'impose sans risque / si p=1

All three preserve the words and two diagonal strokes; exact boxing, alignment and TikZ coordinates vary and create no further reading count.

**Root evidence:** Root supplied decision confirms the readable words, two-line placement and two distinct diagonals.

**Crop:** `readers/008/B/03_parenthesis_cancel.png`.

| Reader | Exact returned reading / source excerpt | Source |
| --- | --- | --- |
| A | Same deleted words and parentheses, with two rising diagonal cancellation strokes | A04 |
| B | Same words and cancellation state, arranged on two lines and crossed by two separate rising diagonal paths in TikZ. | B008_D09 |
| C | Same deleted wording, in two visible lines, crossed by two distinct ascending-right strokes in TikZ | 008-C-09 |


### 008-05 — Second existential line: ζ/δ

All three retain ζ/δ at the first occurrence.

**Root evidence:** Root supplied decision: upper oblique/waist and lower return retain both candidates; subsequent occurrences retain the first candidate as returned.

**Crop:** `readers/008/B/04_zeta.png`.

| Reader | Exact returned reading / source excerpt | Source |
| --- | --- | --- |
| A | \unsure{\zeta\|\delta} | A05 |
| B | \unsure{\zeta\|\delta} | B008_D02 |
| C | \unsure{\zeta\|\delta} | 008-C-02 |


### 008-06 — Detached mark above a in et si a=a0 a-double-prime

B preserves dot/prime candidates above a. A and C-reader leave a without an overmark in their TeX. No algebraic role is assigned.

**Root evidence:** Root supplied decision: detached short upright with thicker foot; preserve dot/prime candidates above a, with role and hand unresolved.

**Crop:** `readers/008/B/05_a_overmark.png`.

Shape/placement is retained without assigning an unestablished role or hand.

| Reader | Exact returned reading / source excerpt | Source |
| --- | --- | --- |
| A | De même $\exists\,a_0\in\mathbb N^*$ et $\exists\,\unsure{\zeta\|\delta}\in\mathbb N$ tel que $a'=q^\zeta a_0^q$ avec $a_0\mid a$ et si $a=a_0a''$ alors $a_0\mathrel{\underset{1}{\smile}}a''$ ? | readers/008/A/reading.tex or audit (exact excerpt/provenance in JSON) |
| B | \overset{\unsure{\cdot\|\prime}}{a}=a_0a'' | B008_D08 |
| C | De même $\exists\,a_0\in\mathbb N^*$ et $\exists\,\unsure{\zeta\|\delta}\in\mathbb N$ tel que $a'=q^\zeta a_0^q$ avec $a_0\mid a$ et si $a=a_0a''$ alors $a_0\mathrel{\underset{1}{\smile}}a''$ ? | readers/008/C/reading.tex or audit (exact excerpt/provenance in JSON) |


### 008-07 — Cancelled lower item under a prime

All three retain the doubtful cancelled zero candidate; A explicitly mentions an unrecovered subscript as the open alternative.

**Root evidence:** Root supplied decision: substantially filled subscript patch; retain doubtful cancelled 0.

**Crop:** `readers/008/B/06_a_subscript.png`.

| Reader | Exact returned reading / source excerpt | Source |
| --- | --- | --- |
| A | a_{\deleted{\unsure{0}}}' | A06 |
| B | a_{\deleted{\unsure{0}}}' | B008_D03 |
| C | a_{\deleted{\unsure{0}}}' | 008-C-03 |


### 008-08 — Numerical-example frame and shared upper hypothesis rule

A and B draw the shared frame/rule connection. B records it in reading.tex, reading.md and B008.23/B008.25, without a separate differences row. C-reader keeps separate frame and rules in TeX.

**Root evidence:** Root supplied decision confirms the shared connection. Root crop03 clips the lower-right portion of the separate lower rule; that complete feature is supported by all three complete-half audits. No recrop.

**Crop:** `crops/008/03_frame_rules.png`.

Root crop boundary limit is recorded. Full lower-rule coverage is provided by the three complete-half audits; the clerk viewed no images.

| Reader | Exact returned reading / source excerpt | Source |
| --- | --- | --- |
| A | Open-right bracket whose left edge meets the shared upper long rule, with second rule below hypothesis | A07 |
| B | \figure{\begin{tikzpicture}[x=1cm,y=1cm]<br>\node[anchor=west,inner sep=0pt] at(0,.75) {Donc \quad $c=b+a_0^q=a+q^\gamma b_0^q$};<br>\node[anchor=west,inner sep=0pt,align=left,font=\footnotesize] at(6.75,1.05) {pour $q=2$ on a, $a_0=b_0=1$,\\$\gamma=1$, $b=4$, $a=3$, $c=5$};<br>\draw (12.0,1.60) -- (6.65,1.63) .. controls(6.58,1.63) and(6.55,1.55) .. (6.55,1.45) -- (6.55,.08);<br>\draw (0,.30) .. controls(2.6,.30) and(4.8,.17) .. (6.55,.10) .. controls(8.6,-.05) and(10.6,.02) .. (12.0,-.06);<br>\node[anchor=west,inner sep=0pt,font=\footnotesize] at(.05,-.32) {Je fais l'hypothése suivante \quad si $q$ premier et $1\leqslant i<q$ alors $q\mid C_q^i$};<br>\draw (.12,-.62) .. controls(4.2,-.57) and(8.9,-.80) .. (11.95,-.84);<br>\end{tikzpicture}} | readers/008/B/reading.tex or audit (exact excerpt/provenance in JSON) |
| C | Donc \quad $c=b+a_0^q=a+q^\gamma b_0^q$<br>\margin{\begin{tikzpicture}[baseline=(n.base)]<br>\node[inner sep=2pt,text width=.85\marginparwidth] (n) {pour $q=2$ on a, $a_0=b_0=1$, $\gamma=1$, $b=4$, $a=3$, $c=5$};<br>\draw (n.north east) -- (n.north west) -- (n.south west) -- (n.south east);<br>\end{tikzpicture}}<br><br>\noindent\rule{\linewidth}{.35pt}\par<br>Je fais l'hypothése suivante \quad si $q$ premier et $1\leqslant i<q$ alors $q\mid C_q^i$<br>\par\noindent\rule{\linewidth}{.35pt}\par | readers/008/C/reading.tex or audit (exact excerpt/provenance in JSON) |


### 008-09 — Cancelled alors immediately before on a

A and C-reader retain doubtful alors. B returns deleted alors without an uncertainty marker and reports a resolution.

**Root evidence:** Root supplied decision: tall l and rounded remnants survive, but initial/final outlines remain merged with the zigzag. Retain the doubt; B’s resolution is not adopted.

**Crop:** `readers/008/C/05_lower_alors_and_pale.png`.

| Reader | Exact returned reading / source excerpt | Source |
| --- | --- | --- |
| A | \deleted{\unsure{alors}} | A08 |
| B | \deleted{alors} | B008_D04 |
| C | \deleted{\unsure{alors}} | 008-C-04 |


### 008-10 — Pale primed letter in addition after on a

All three retain a/α; differences in the quoted substring boundaries create no additional locus.

**Root evidence:** Root supplied decision retains a/α beneath the distinct prime, with a first; the original pale formula remains inserted.

**Crop:** `readers/008/C/05_lower_alors_and_pale.png`.

| Reader | Exact returned reading / source excerpt | Source |
| --- | --- | --- |
| A | \inserted{$p=q,\ {\unsure{a\|\alpha}}'=\gamma$} | A09 |
| B | p=q,\ {\unsure{a\|\alpha}}'=\gamma | B008_D07 |
| C | {\unsure{a\|\alpha}}'=\gamma | 008-C-07 |


### 008-11 — Curved mark below the pale p=q comma and the apostrophe of C’est

A retains one formula comma. B008_D07 identifies the lower comma-like trace as the C’est apostrophe. C-reader 008-C-08 adds a second, lower uncertain comma-shaped mark to the formula; that duplication is not adopted.

**Root evidence:** Root supplied decision: the lower curved mark in C05 occupies the same source coordinates as the complete apostrophe above C’est in A10. B’s apostrophe explanation is adopted.

**Crop:** `readers/008/C/05_lower_alors_and_pale.png`.

C-reader’s extra comma-shaped token is rejected as a duplicate representation of the C’est apostrophe; the mark itself remains represented in that word.

| Reader | Exact returned reading / source excerpt | Source |
| --- | --- | --- |
| A | alors Si $q\geqslant3$ et $q\alpha-\alpha'\geqslant2$ \deleted{\unsure{alors}} on a \inserted{$p=q,\ {\unsure{a\|\alpha}}'=\gamma$} | readers/008/A/reading.tex or audit (exact excerpt/provenance in JSON) |
| B | p=q,\ {\unsure{a\|\alpha}}'=\gamma | B008_D07 |
| C | p=q\,\underset{\hspace{.2em}\unsure{,}}{,} | 008-C-08 |


### 008-12 — Cancelled p²/p before the lower q squared

All three retain p²/p and the cancellation.

**Root evidence:** Root supplied decision: descending body plus raised cluster remain obscured by crossing strokes; retain both candidates.

**Crop:** `readers/008/A/07_lower_cancelled_p.png`.

| Reader | Exact returned reading / source excerpt | Source |
| --- | --- | --- |
| A | \deleted{\unsure{p^{2}\|p}} | A10 |
| B | \deleted{\unsure{p^{2}\|p}} | B008_D05 |
| C | \deleted{\unsure{p^{2}\|p}} | 008-C-05 |


### 008-13 — First lower ou p=1 cancellation and returning stroke

A describes paired passes and hooked return; B describes a long crossing with curved lower return; C-reader describes crossing and lower returning stroke. The exact returned paths are retained in provenance; this is one drawing locus.

**Root evidence:** Root supplied decision confirms the returning lower stroke.

**Crop:** `readers/008/C/07_lower_cancellations.png`.

| Reader | Exact returned reading / source excerpt | Source |
| --- | --- | --- |
| A | Same deleted wording with paired cancellation passes and hooked return | A12 |
| B | Same cancelled words, with the visible long crossing and its curved lower return drawn explicitly. | B008_D10 |
| C | Same deleted text with a long crossing stroke and lower returning stroke | 008-C-10 |


### 008-14 — Second lower ou p=1 implies p=1 cancellation direction

All three draw a rising cancellation. C-reader supplies a separate source row; A11/B008_D11 combine this evidence with insertion placement. This row covers the crossing direction only.

**Root evidence:** Root supplied decision confirms the second cancellation rises across its chain.

**Crop:** `readers/008/C/07_lower_cancellations.png`.

| Reader | Exact returned reading / source excerpt | Source |
| --- | --- | --- |
| A | Same insertion placed above cancelled ou p=1 implies p=1 | A11 |
| B | The pale inserted absurde car q nondivides a is positioned above the cancelled ou p=1 implies p=1; the crossing rises to the right. | B008_D11 |
| C | Same deleted span, crossed by a single long ascending-right path in TikZ | 008-C-12 |


### 008-15 — Pale absurde car q nondivides a above the second cancelled continuation

All three preserve the wording and above-chain placement. overset versus a positioned TikZ node is a rendering implementation difference. The separate crossing-direction decision is 008-14.

**Root evidence:** Root supplied decision confirms the pale phrase sits above the second cancelled continuation.

**Crop:** `readers/008/C/07_lower_cancellations.png`.

| Reader | Exact returned reading / source excerpt | Source |
| --- | --- | --- |
| A | Same insertion placed above cancelled ou p=1 implies p=1 | A11 |
| B | The pale inserted absurde car q nondivides a is positioned above the cancelled ou p=1 implies p=1; the crossing rises to the right. | B008_D11 |
| C | \overset{\inserted{\text{absurde car }q\nmid a}}{\text{cancelled }\mathrm{ou}\ p=1\Longrightarrow p=1} | 008-C-11 |


### 008-16 — Faint residual strokes and points above the right end of the lower implications

C-reader supplies the residue drawing and 008-C-14. A and B supply no separate drawing or character for this interline group.

**Root evidence:** Root supplied decision adopts the residual traces as a drawing, with role, source and hand unresolved.

**Crop:** `readers/008/C/07_lower_cancellations.png`.

Shape/placement is retained without assigning an unestablished role or hand.

| Reader | Exact returned reading / source excerpt | Source |
| --- | --- | --- |
| A | No separate residue drawing in reading.tex. | readers/008/A/reading.tex or audit (exact excerpt/provenance in JSON) |
| B | No separate residue drawing in reading.tex. | readers/008/B/reading.tex or audit (exact excerpt/provenance in JSON) |
| C | Small gray drawing of residual curved strokes and detached points, without a supplied character | 008-C-14 |


### 008-17 — Final cancelled q and raised qα−1: glyphs and relative placement

All three resolve the cancelled q and raised entry. C-reader’s report retains the witness-style superscript string in its reading description, while its actual TeX uses explicit geometry. All three code snippets are retained; no algebraic attachment is supplied.

**Root evidence:** Root supplied decision resolves the q body/right descender and the raised qα−1 glyphs; reproduce their physical arrangement.

**Crop:** `readers/008/A/09_final_replacement.png`.

| Reader | Exact returned reading / source excerpt | Source |
| --- | --- | --- |
| A | Cancelled q with intact q alpha minus 1 raised above and right | A13 |
| B | A cancelled lower q, crossed by a returning zigzag, with the live q alpha minus 1 drawn above; reading.tex preserves the stack in TikZ. | B008_D06 |
| C | {\deleted{q}}^{q\alpha-1} (glyph and raised placement retained; explicit cancellation drawing in reading.tex) | 008-C-06 |


### 008-18 — Repeated oblique cancellation returns and lower tail around final q

A draws two looped rising paths and a lower tail; B draws a returning zigzag; C-reader draws repeated returns and a longer lower hook. Exact source paths remain available; coordinate and stroke-width choices do not create further loci.

**Root evidence:** Root supplied decision confirms repeated returns around the final q. This drawing detail and the resolved cancelled-q doubt concern the same original C-doubt locus, counted once under 008-17.

**Crop:** `readers/008/A/09_final_replacement.png`.

| Reader | Exact returned reading / source excerpt | Source |
| --- | --- | --- |
| A | Cancelled q with intact q alpha minus 1 raised above and right | A13 |
| B | A cancelled lower q, crossed by a returning zigzag, with the live q alpha minus 1 drawn above; reading.tex preserves the stack in TikZ. | B008_D06 |
| C | Same cancelled q with repeated oblique returns and the long lower hook drawn explicitly | 008-C-13 |


### 008-19 — Detached rising stroke upper-left of l'ensemble

A preserves a qualified slash-shaped candidate; B and C-reader leave no separate mark in the note’s TeX.

**Root evidence:** Root supplied decision adopts the short detached rising slash-shaped candidate, without attaching it to the letter.

**Crop:** `readers/008/A/10_right_note.png`.

Shape/placement is retained without assigning an unestablished role or hand.

| Reader | Exact returned reading / source excerpt | Source |
| --- | --- | --- |
| A | \unsure{/} immediately before and above l'ensemble | A14 |
| B | \margin{\begin{tikzpicture}[baseline=(n.base)]<br>\node[inner sep=0pt,text width=.85\marginparwidth] (n) {C'est peut-être interessant car ici $2$ est mis à part dans l'ensemble des nombres premiers};<br>\fill ([xshift=.07cm,yshift=-.47cm]n.south east) circle(.022cm);<br>\draw ([xshift=.15cm,yshift=-.47cm]n.south east) -- ([xshift=.31cm,yshift=-.47cm]n.south east)<br> -- ([xshift=.35cm,yshift=-.16cm]n.north east)<br> .. controls([xshift=.35cm,yshift=-.03cm]n.north east) and([xshift=.19cm,yshift=-.01cm]n.north east)<br> .. ([xshift=.06cm,yshift=.01cm]n.north east);<br>\draw ([xshift=.19cm,yshift=.14cm]n.north east) .. controls([xshift=.00cm,yshift=.04cm]n.north east) and([xshift=-.01cm,yshift=-.06cm]n.north east) .. ([xshift=.15cm,yshift=-.10cm]n.north east);<br>\end{tikzpicture}} | readers/008/B/reading.tex or audit (exact excerpt/provenance in JSON) |
| C | \margin{\begin{tikzpicture}[baseline=(n.base)]<br>\node[inner sep=0pt,text width=.85\marginparwidth] (n) {C'est peut-être interessant car ici $2$ est mis à part dans l'ensemble des nombres premiers};<br>% A small detached point is visible at the lower start of the return arrow.<br>\fill (n.south east) circle (.45pt);<br>\draw[->] ([xshift=.07cm]n.south east) -- ([xshift=.16cm]n.south east) \|- (n.north east);<br>\end{tikzpicture}} | readers/008/C/reading.tex or audit (exact excerpt/provenance in JSON) |


### 008-20 — Return arrow: below-note start, detached point and curved left-pointing head

A lowers the arrow start in TeX but adds no detached point and uses a generic arrow head. B explicitly draws point, lowered start and curved head. C-reader adds a detached point while retaining a generic arrow path/head at the note corner. All exact implementations are preserved.

**Root evidence:** Root supplied decision adopts the detached point, below-note starting position and hooked leftward head.

**Crop:** `readers/008/B/14_right_note.png`.

| Reader | Exact returned reading / source excerpt | Source |
| --- | --- | --- |
| A | \margin{\begin{tikzpicture}[baseline=(n.base)]<br>\node[inner sep=0pt,text width=.85\marginparwidth] (n)<br> {C'est peut-être interessant car ici $2$ est mis à part dans<br> \(\mathord{\overset{\scriptscriptstyle\unsure{/}}{\vphantom{l}}}\)l'ensemble des nombres premiers};<br>% Small detached rising stroke before l'ensemble: role and hand unresolved.<br>% Return arrow rises at the right from the final parenthesis toward this note.<br>\draw[->] ([yshift=-.25cm]n.south east) -- ++(.16,0) \|- (n.north east);<br>\end{tikzpicture}} | readers/008/A/reading.tex or audit (exact excerpt/provenance in JSON) |
| B | Return arrow starting below the note beside the closing final parenthesis, with a detached round point before its lower horizontal stroke and an explicit left-pointing hooked head. | B008_D12 |
| C | Same returning arrow, with a small detached point at its lower start | 008-C-15 |


### 008-21 — Upper-right mottled trace: root-only drawing

All three reader returns supply no character and no drawing for this area. A and B explicitly record the unsuccessful character inspection; C-reader describes upper-right damage/puncture among physical features. The drawing is root-only.

**Root evidence:** Root supplied decision after viewing B15: no complete character is recovered; preserve an approximate drawing of the visible patches.

**Crop:** `readers/008/B/15_upper_right_trace.png`.

Shape/placement is retained without assigning an unestablished role or hand.

| Reader | Exact returned reading / source excerpt | Source |
| --- | --- | --- |
| A | Horizontal fold crosses between existential passages. Bracket, rules, cancellations, additions, return arrow and archive numeral are recorded. No supported character was recovered from the small irregular dark area at extreme upper right. | readers/008/A/reading.tex or audit (exact excerpt/provenance in JSON) |
| B | A few pale interior specks within the cancelled parenthesis do not support a further character reading. The mottled upper-right trace was inspected in crop 15; its irregular dispersed dark patches and pale central region supply no coherent glyph candidate. No character has been supplied for these areas. | readers/008/B/reading.tex or audit (exact excerpt/provenance in JSON) |
| C | Horizontal paper fold, upper-right damage/puncture, and image border were observed as substrate features. Written rules, three-sided example frame, all recorded cancellations, pale additions, return arrow and detached point are represented. The faint interline residue is drawn without an assigned character or mathematical role. | readers/008/C/reading.tex or audit (exact excerpt/provenance in JSON) |


## Seven actual C doubts

| Source line and locus | Merged decision | A | B | C-reader | Root |
| --- | --- | --- | --- | --- | --- |
| 7: First isolated struck line | 008-02 | retained | retained | retained | retained |
| 8: Second existential line | 008-05 | retained | retained | retained | retained |
| 9: Before second bowl in or a… | 008-07 | retained | retained | retained | retained |
| 10: Above last two implications | 008-09 | retained | resolved | retained | retained |
| 11: After (1)⇒ in lower left | 008-12 | retained | retained | retained | retained |
| 12: End of final line | 008-17 | resolved | resolved | resolved | resolved |
| 13: Lower line, light addition after on a | 008-10 | retained | retained | retained | retained |

The first six source rows are notation entries, and the final two table rows retain spellings. They are preserved as audit material, without invented C-doubt statuses.


## Exhaustive report-row crosswalk


### Reader A

| Original row | Merged decision(s) | Original diff_C | Original C-doubt status |
| --- | --- | --- | --- |
| A01 | 008-01 | True | None |
| A02 | 008-02 | False | retained |
| A03 | 008-03 | True | None |
| A04 | 008-04 | True | None |
| A05 | 008-05 | False | retained |
| A06 | 008-07 | False | retained |
| A07 | 008-08 | True | None |
| A08 | 008-09 | False | retained |
| A09 | 008-10 | False | retained |
| A10 | 008-12 | False | retained |
| A11 | 008-14, 008-15 | True | None |
| A12 | 008-13 | True | None |
| A13 | 008-17, 008-18 | True | resolved |
| A14 | 008-19 | True | None |


### Reader B

| Original row | Merged decision(s) | Original diff_C | Original C-doubt status |
| --- | --- | --- | --- |
| B008_D01 | 008-02 | False | retained |
| B008_D02 | 008-05 | False | retained |
| B008_D03 | 008-07 | False | retained |
| B008_D04 | 008-09 | True | resolved |
| B008_D05 | 008-12 | False | retained |
| B008_D06 | 008-17, 008-18 | True | resolved |
| B008_D07 | 008-10, 008-11 | False | retained |
| B008_D08 | 008-06 | True | None |
| B008_D09 | 008-04 | True | None |
| B008_D10 | 008-13 | True | None |
| B008_D11 | 008-14, 008-15 | True | None |
| B008_D12 | 008-20 | True | None |


### Reader C

| Original row | Merged decision(s) | Original diff_C | Original C-doubt status |
| --- | --- | --- | --- |
| 008-C-01 | 008-02 | False | retained |
| 008-C-02 | 008-05 | False | retained |
| 008-C-03 | 008-07 | False | retained |
| 008-C-04 | 008-09 | False | retained |
| 008-C-05 | 008-12 | False | retained |
| 008-C-06 | 008-17 | True | resolved |
| 008-C-07 | 008-10 | False | retained |
| 008-C-08 | 008-11 | True | None |
| 008-C-09 | 008-04 | True | None |
| 008-C-10 | 008-13 | True | None |
| 008-C-11 | 008-15 | True | None |
| 008-C-12 | 008-14 | True | None |
| 008-C-13 | 008-18 | True | None |
| 008-C-14 | 008-16 | True | None |
| 008-C-15 | 008-20 | True | None |


## Inventory coverage

The45 merged inventory elements cover all41 A entries,42 B entries and42 C-reader entries. The root page text was read for reconciliation; all45 elements are represented in that page. The C-reader’s extra curved-mark inventory entry maps to the apostrophe already present in C’est and creates no duplicate object. B’s detached a overmark, C-reader’s residual strokes and second cancellation geometry, and root’s upper-right drawing are included. The archive7 remains a comment.

| Merged element | Kind and position | Content / object | A source | B source | C source |
| --- | --- | --- | --- | --- | --- |
| 008.I.01 | drawing; extreme upper right | Approximate gray drawing of mottled patches and short curves; no character, source or role assigned |  |  |  |
| 008.I.02 | text; top | Supposons que q alpha-alpha prime ne 0 alors | 008.A.01 | B008.01 | 008.C.01 |
| 008.I.03 | display; first two implications | (1) implies p divides sum; implies p divides q a^(q-1) | 008.A.02 | B008.02, B008.03 | 008.C.02 |
| 008.I.04 | deletion; endpoint of second implication | ne 0 before >0 | 008.A.03 | B008.04 | 008.C.03 |
| 008.I.05 | text; below first implications | or p divides b prime et b prime divides b^q | 008.A.04 | B008.05 | 008.C.04 |
| 008.I.06 | deletion; isolated struck line | donc si p ne 1 / p ne q | 008.A.05 | B008.06 | 008.C.05 |
| 008.I.07 | display; next implication | (1) implies p divides q donc ... p=q | 008.A.06 | B008.07 | 008.C.06 |
| 008.I.08 | deletion; within preceding display | p=1 ou | 008.A.07 | B008.08 | 008.C.07 |
| 008.I.09 | text; Donc si line | Donc si p ne q p premier ... alpha prime=q alpha | 008.A.08 | B008.09 | 008.C.08 |
| 008.I.10 | insertion; below premier | ou p=1 | 008.A.09 | B008.10 | 008.C.09 |
| 008.I.11 | drawing; above ou p=1 | small filled triangle | 008.A.10 |  |  |
| 008.I.12 | deletion; upper-right two-line parenthesis | (on l'impose sans risque si p=1) | 008.A.11 | B008.11 | 008.C.10 |
| 008.I.13 | drawing; over that parenthesis | two separate oblique cancellations | 008.A.12 | B008.12 | 008.C.11 |
| 008.I.14 | text; first existential line | Donc exists b_0 in N star et exists gamma in N | 008.A.13 | B008.13 | 008.C.12 |
| 008.I.15 | margin note; right of first existential line | q nondivisibility b_0 | 008.A.14 | B008.14 | 008.C.13 |
| 008.I.16 | text; above fold | de plus b_0 divides b et si b=b_0 b double prime | 008.A.15 | B008.15 | 008.C.14 |
| 008.I.17 | text; below fold first line | De meme exists a_0 in N star et exists zeta/delta in N | 008.A.16 | B008.16 | 008.C.15 |
| 008.I.18 | text; continuation below fold | avec a_0 divides a et si a=a_0 a double prime | 008.A.17 | B008.16 | 008.C.15 |
| 008.I.19 | text; above the a in et si a=a0 a-double-prime | detached short upright, dot/prime candidate |  | B008.17 |  |
| 008.I.20 | text; product and coprimality line | or a bowl_1 b implies a prime bowl_1 b prime | 008.A.18 | B008.18 | 008.C.16 |
| 008.I.21 | deletion; under a prime | black patch with doubtful zero candidate | 008.A.19 | B008.19 | 008.C.17 |
| 008.I.22 | text; before c display | Je suppose desormais que zeta=0 donc a prime=a_0^q | 008.A.20 | B008.20 | 008.C.18 |
| 008.I.23 | display; above upper rule, left | Donc c=b+a_0^q=a+q^gamma b_0^q | 008.A.21 | B008.21 | 008.C.19 |
| 008.I.24 | margin note; right of c display | pour q=2 on a, a_0=b_0=1, gamma=1, b=4, a=3, c=5 | 008.A.22 | B008.22 | 008.C.20 |
| 008.I.25 | drawing; example and hypothesis | open-right bracket, connected upper rule, separate lower rule | 008.A.23 | B008.23, B008.25 | 008.C.21, 008.C.22 |
| 008.I.26 | text; between rules | Je fais l'hypothese suivante si q premier et 1<=i<q alors q divides C_q^i | 008.A.24 | B008.24 | 008.C.23 |
| 008.I.27 | text; below lower rule | alors Si q>=3 et q alpha-alpha prime>=2 ... on a | 008.A.25 | B008.26 | 008.C.24 |
| 008.I.28 | deletion; before on a | doubtful alors | 008.A.26 | B008.27 | 008.C.25 |
| 008.I.29 | insertion; pale text after on a | p=q, a prime / alpha prime=gamma | 008.A.27 | B008.28 | 008.C.26 |
| 008.I.30 | display; lower pair of implications | q^2 divides q a^(q-1); q divides a^(q-1) | 008.A.28 | B008.29, B008.33 | 008.C.28 |
| 008.I.31 | deletion; before lower q squared | p squared / p | 008.A.29 | B008.30 | 008.C.29 |
| 008.I.32 | deletion; after first lower q a^(q-1) | ou p=1 | 008.A.30 | B008.31 | 008.C.30 |
| 008.I.33 | drawing; through first lower ou p=1 | paired cancellation passes with hooked return | 008.A.31 | B008.32 | 008.C.31 |
| 008.I.34 | drawing; Faint gap above right end of lower implications | Residual curved strokes and detached points; no character supplied |  |  | 008.C.35 |
| 008.I.35 | deletion; second lower implication endpoint | ou p=1 implies p=1 | 008.A.32 | B008.34 | 008.C.32 |
| 008.I.36 | drawing; Across second bottom cancelled continuation | One rising long cancellation stroke | 008.A.32 | B008.34 | 008.C.33 |
| 008.I.37 | insertion; above second lower cancellation | absurde car q nondivisibility a | 008.A.33 | B008.35 | 008.C.34 |
| 008.I.38 | text; last line | Donc gamma=0 ou gamma=... (sous reserve que l'hypothese est vraie) | 008.A.34 | B008.36 | 008.C.36 |
| 008.I.39 | deletion; after final gamma equality | q | 008.A.35 | B008.37 | 008.C.37 |
| 008.I.40 | text; raised above cancelled q | q alpha - 1 | 008.A.36 | B008.38 | 008.C.38 |
| 008.I.41 | drawing; through final q | two rising looped strokes and lower tail | 008.A.37 | B008.39 | 008.C.39 |
| 008.I.42 | margin note; lower right | C'est peut-etre interessant car ici 2 est mis a part dans l'ensemble des nombres premiers | 008.A.38 | B008.40 | 008.C.40, 008.C.27 |
| 008.I.43 | text; upper-left of l'ensemble | qualified detached slash-like mark | 008.A.39 |  |  |
| 008.I.44 | drawing; right of final parenthesis and note | Detached point, below-note lower shaft, rising return shaft and explicit curved left-pointing head | 008.A.40 | B008.41 | 008.C.41 |
| 008.I.45 | text; bottom left | archive 7, retained only as a comment | 008.A.41 | B008.42 | 008.C.42 |


## Counting and rendering choices

Each content/placement/drawing component is documented, with one C-difference count per adjudicated locus. Final cancelled-q resolution and its repeated cancellation geometry share the original C-doubt locus: 008-18 is logged and counted under 008-17. Ordinary line wraps, font sizes, control-point values, boxing, overset versus TikZ, and macro-only changes contribute no additional count. Source A11/B11 combine the independent second crossing and insertion components. Source A13/B06 combine final glyph/placement and cancellation details, mapped to 008-17/18 but counted once.

The second lower cancellation direction and pale insertion placement remain separate independently decided components (008-14/15). The final-q glyph/placement and cancellation paths are separately documented (008-17/18) and contribute one C-difference count, under008-17. Source rows spanning components are linked to both and preserved once in source_reports.

## Existing mathematical events

The three root event objects are copied unchanged. B’s actual event is mapped to the delivery columns without recalculation, with date2026-11-20 and unknown exact time. A/C-reader contribute no mathematical events.

| Statement ID | Actor | Date | Type | Actual recorded outcome |
| --- | --- | --- | --- | --- |
| 008-binomial-fixed-coefficients | GPT-6 Astra Pro; effort inherited, separately verifiable setting not exposed; run /root | 2026-11-20 11:25:04 UTC | computation or formal certificate | For q=2,3,5,7, every listed internal binomial coefficient has remainder0 modulo that q. Explicit coefficient-reduction morphisms and complete finite rows are recorded in checks/scan008_polynomials.md. This does not verify the writer’s hypothesis for all primes. |
| 008-bracket-fixed-residues | GPT-6 Astra Pro; effort inherited, separately verifiable setting not exposed; run /root | 2026-11-20 11:25:04 UTC | computation or formal certificate | Under B→qV and coefficient reduction modulo q², the written bracket minus q*A^(q−1) has residue2V for q=2 and0 for q=3,5,7. All four concrete substitution and quotient morphisms and exact polynomials are in checks/scan008_polynomials.md. No general implication or handwritten correction is inferred. |
| 008-marginal-example | GPT-6 Astra Pro; effort inherited, separately verifiable setting not exposed; run /root | 2026-11-20 11:25:04 UTC | computation or formal certificate | The written q=2,a0=b0=1,gamma=1,a=3,b=4,c=5 values give b-prime=2, a-prime=1 and c=4+1=3+2=5. The associated concrete factorizations a=1*3,b=1*4 have gcd values1. Values from007-arithmetic-instance are explicitly re-evaluated here; scope is this example only. Source checks/scan008_polynomials.md. |
| 008-marginal-example-reader-B | Independent reader B; scan008 return; exact agent/run identifier not recorded in supplied report | 2026-11-20 | exact arithmetic substitution | Using precisely the written assignments, 4+1^2=5 and 3+2^1*1^2=5; both expressions equal the written c=5. This local computation supplies no repair or proof of the surrounding assertions. |


## Workflow exceptions and timing

| Reader | Attempt | Recorded outcome |
| --- | --- | --- |
| A | pdfLaTeX | Unavailable pdflatex.fmt; no successful compile or rendered-page validation. |
| B | LuaLaTeX | Unavailable lualatex.fmt; no successful compile or rendered-page validation. |
| C | pdfLaTeX | Unavailable pdflatex.fmt; no successful compile or rendered-page validation. |

All three returned documents acknowledge an unsuccessful compiler attempt. The initial assignment described C-reader confirmation as pending; the current C-reader report and root adjudication notes explicitly record the failed attempt. Root used structural validation only. The clerk did not invoke a compiler or inspect compiler scratch.

B report end remains exactly `2026-11-20 11:36:55 UTC`. Root reports a later final-message value of `2026-11-20 11:36:55 UTC`. Neither is substituted for the unknown arithmetic event time.


## Root evidence limitations and approval

Root used15 local crop views, comprising3 root-created and12 existing reader crops; no root whole/half views. The shared-frame crop clips the lower-right part of the separate lower rule; all three complete-half audits cover that rule. The source coordinate systems are retained as returned, including C-reader half-specific boxes; the clerk performed no coordinate conversion or image comparison.

Main approval remains pending. No approved record, cumulative output or page was edited by the clerk. The source reports, exact TeX and Markdown returns, root notes/page text, event objects and file hashes are preserved in the draft for review.
