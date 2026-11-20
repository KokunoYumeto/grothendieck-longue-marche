## Reader A

\scanpage{7}
\deleted{\illegible{1}} Soit $a\in\mathbb N^*,b\in\mathbb N^*,c\in\mathbb N^*,\ q\in\mathbb N^*$ \quad $q$ nombre premier $(q\ne1)$

On suppose que $a\mathrel{\underset{1}{\smile}}b$, $a\mathrel{\underset{1}{\smile}}c$, $b\mathrel{\underset{1}{\smile}}c$ (premiers entre eux deux à deux)
\inserted{et $a^q+b^q=c^q$}

On a $c>a$ et $c>b$ car $a\in\mathbb N^*$ et $b\in\mathbb N^*$

On pose $c=a+b'=b+a'$ avec $b'\in\mathbb N^*$ et $a'\in\mathbb N^*$
\[
\begin{aligned}
\text{alors}\qquad a^q+b^q=c^q&=(a+b')^q=\sum_{i=0}^{q}C_q^i\,a^i b'^{\,q-i}\qquad\text{(Newton)}\\
 &=b'^{\,q}+\sum_{i=1}^{q-1}C_q^i\,a^i b'^{\,q-i}+a^q\qquad(\text{car }q\geqslant2)
\end{aligned}
\]
\[
\text{donc}\qquad b^q=\sum_{i=1}^{q-1}C_q^i\,a^i b'^{\,q-i}+b'^{\,q}\tag*{(1)}
\]
la puissance de $b'$ n'étant jamais nulle on peut mettre $b'$ en facteur dans le second membre de (1), donc $b'\mid b^q$ ($b'$ divise $b^q$)

Soit $p$ un nombre premier \deleted{ou $p=1$} et tel que : $p\mid b'$ donc $p\mid b$. Soit $\alpha\in\mathbb N^*$ et $\alpha'\in\mathbb N^*$ tels que
\[
\begin{aligned}
 &p^{\alpha'}\mid b'\quad\text{et}\quad p^{\alpha'+1}\nmid b'\\
 \text{et}\quad &p^\alpha\mid b\quad\text{et}\quad p^{\alpha+1}\nmid b
\end{aligned}
\]
\margin{$\unsure{a|\alpha}$ \unsure{n'exist|n'existe} pas si on avait $p=1$}
On a $\alpha'\leqslant q\alpha$ car $b'\mid b^q$

\[
\begin{aligned}
(1)\ \Longrightarrow\quad&p^{q\alpha}\mid\sum_{i=1}^{q-1}C_q^i\,a^i b'^{\,q-i}+b'^{\,q}\\
\Longrightarrow\quad&p^{q\alpha}\mid b'\left(\sum_{i=1}^{q-1}C_q^i\,a^i b'^{\,q-i-1}+b'^{\,q-1}\right)\qquad(\text{car }q\geqslant2)
\end{aligned}
\]
posons $b'=p^{\alpha'}b''$ donc $b''\mathrel{\underset{1}{\smile}}p$ (propriété de $\alpha'$)
\[
\begin{aligned}
\Longrightarrow\quad&p^{q\alpha}\mid p^{\alpha'}b''\left(\sum_{i=1}^{q-1}C_q^i\,a^i b'^{\,q-i-1}+b'^{\,q-1}\right)\\
\Longrightarrow\quad&p^{q\alpha-\alpha'}\mid b''\left(\sum_{i=1}^{q-1}C_q^i\,a^i b'^{\,q-i-1}+b'^{\,q-1}\right)\quad\text{car }q\alpha\geqslant\alpha'\\
\Longrightarrow\quad&p^{q\alpha-\alpha'}\mid\sum_{i=1}^{q-1}C_q^i\,a^i b'^{\,q-i-1}+b'^{\,q-1}\quad\text{car }b''\mathrel{\underset{1}{\smile}}p
\end{aligned}
\]
% archive sheet number: 6




{
  "differences": [
    {
      "id": "007-A-01",
      "location": "Opening blacked-out mark immediately before Soit, upper left",
      "C": "\\deleted{\\illegible{1}}",
      "H": null,
      "reading": "\\deleted{\\illegible{1}}",
      "evidence": "The enlargement shows a densely blackened compact patch with overlapping loops and short projections. The internal pale gaps do not yield a recoverable character sequence. The full height of the patch and the following Soit are present in the crop.",
      "confidence": "high",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "crops/01_opening_deletion.png",
      "bbox": {
        "coordinate_system": "original full scan, top-left origin",
        "xyxy": [
          20,
          18,
          180,
          88
        ]
      }
    },
    {
      "id": "007-A-02",
      "location": "Pale two-line marginal note at right of divisibility pairs, first character",
      "C": "\\unsure{a|\\alpha}",
      "H": null,
      "reading": "\\unsure{a|\\alpha}",
      "evidence": "A small closed loop joins a rightward falling tail. Its short top contact and tail support a as the first candidate; the same visible form also supports alpha in this small pale hand. The crop supplies no separate longer stem that settles the choice. No character is inferred from the adjacent main-hand formulas.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "crops/02_pale_note.png",
      "bbox": {
        "coordinate_system": "original full scan, top-left origin",
        "xyxy": [
          990,
          950,
          1348,
          1064
        ]
      }
    },
    {
      "id": "007-A-03",
      "location": "Pale marginal note, ending of n’exist / n’existe",
      "C": "\\unsure{n'exist|n'existe}",
      "H": null,
      "reading": "\\unsure{n'exist|n'existe}",
      "evidence": "After the low angular s-like turn, the final tall stroke descends and bends right. No independent final e is securely separated from that bend. The first candidate n’exist is retained, with n’existe preserved as the supported alternative. The continuation pas si and the complete second line on avait p=1 are within the crop.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "crops/02_pale_note.png",
      "bbox": {
        "coordinate_system": "original full scan, top-left origin",
        "xyxy": [
          990,
          950,
          1348,
          1064
        ]
      }
    }
  ],
  "doubts": [
    {
      "location": "Opening deletion",
      "reading": "\\deleted{\\illegible{1}}",
      "alternatives": [],
      "confidence": "low",
      "reason": "Physically blacked out; no recoverable original sequence after the single enlargement.",
      "crop": "crops/01_opening_deletion.png"
    },
    {
      "location": "Pale note, first character",
      "reading": "a",
      "alternatives": [
        "\\alpha"
      ],
      "confidence": "medium",
      "reason": "Small loop with rightward falling tail; Latin a and alpha remain supported.",
      "crop": "crops/02_pale_note.png"
    },
    {
      "location": "Pale note, first-line verb ending",
      "reading": "n'exist",
      "alternatives": [
        "n'existe"
      ],
      "confidence": "medium",
      "reason": "Terminal bend merges with tall last stroke; no independent e is securely separated.",
      "crop": "crops/02_pale_note.png"
    }
  ],
  "notes": {
    "page_content": "Handwritten French number-theoretic working. The page states positive-integer and pairwise-coprimality conditions, inserts a^q+b^q=c^q, expands (a+b′)^q, then writes divisibility statements involving p, alpha and alpha prime. These are descriptions of the transcribed writing.",
    "authors_own_uncertainty": [],
    "title_date_page_counts": "No title or date is written. Pencilled archive sheet number 6 appears at the bottom left and is retained solely as a TeX comment. No manuscript page number is assigned.",
    "mathematics_led_reading_decisions": "No mathematical computation or proof check was performed. Formula glyphs, indices, exponents, divisibility strokes and inequalities were compared directly with their visible ink. The crowded penultimate summation was enlarged because its small curled body and bounds were compressed; the upper q-1 and lower i=1 are legible and the C reading is retained.",
    "witness_scope": "H status is nothing for this page. All H values are null and diff_H is false. No H collation rows are invented.",
    "C_doubt_accounting": "The actual C uncertainties comprise three unique loci: the opening blacked-out mark, the pale initial a/alpha, and the ending n’exist/n’existe. The last locus is listed twice in C_doubts.txt and is covered by 007-A-03. The six preceding notation-table rows are recorded as notation, without creating C-doubt rows.",
    "view_attestation": "The whole image was opened once, then supplied half a once, then supplied half b once. All three created crops were opened once each. No other image, other page or reader was inspected. No OCR, recognition tool, internet or external source was used. All remaining uncertain loci are retained explicitly.",
    "image_geometry": "Whole scan dimensions are 1405 by 1720 pixels. Both supplied halves are 1405 by 940. Half a starts at full-scan y=0; the bottom-aligned half b starts at y=1720-940=780. All crop boxes use original full-scan coordinates.",
    "physical_states": "The insertion et a^q+b^q=c^q lies between the pairwise-coprimality sentence and On a c>a. The phrase ou p=1 is crossed by two close rising diagonal strokes; its text and deleted state are retained. The opening mark is heavily blacked out. No diagram or separate drawing is present.",
    "hand_attribution": "The main text uses the upright segmented hand identified as another hand in the supplied inventory; no personal identity is assigned. The pale marginal note remains of undetermined hand.",
    "crop_bounds": "The three target loci are complete within their crops. The crowded-sum crop includes nearby fragments of adjacent lines at its top and bottom edges; the entire target summation, its bounds, factors and right parenthesis are present.",
    "collation_outcome": "No changed C reading was established. All three unique original C doubts remain; the complete proposed text has the same reading as C."
  },
  "notation": [
    {
      "location": "Top conditions; conditions on b prime, a prime and both alphas",
      "sign_or_abbreviation": "N with doubled left strokes and raised asterisk",
      "proposed_latex": "\\mathbb N^*",
      "evidence": "Two upright/oblique strokes at the N left and a separate small raised crossed asterisk."
    },
    {
      "location": "Pairwise-coprimality line; posons line; final reason",
      "sign_or_abbreviation": "Shallow bowl with small hooked 1 below",
      "proposed_latex": "\\mathrel{\\underset{1}{\\smile}}",
      "evidence": "Bowl and lower hooked numeral are separately visible at each occurrence."
    },
    {
      "location": "All binomial sums",
      "sign_or_abbreviation": "C with upper i and lower q; indexed summation",
      "proposed_latex": "C_q^i,\\sum_{i=0}^{q},\\sum_{i=1}^{q-1}",
      "evidence": "Dotted upper i and descending lower q are visible. The first lower bound is i=0; all subsequent lower bounds read i=1. The crowded penultimate sum is resolved by crop 03."
    },
    {
      "location": "c=a+b prime=b+a prime onward",
      "sign_or_abbreviation": "Prime and double prime",
      "proposed_latex": "a',b',b''",
      "evidence": "Separate short raised strokes occur above a and b; b double prime has two raised strokes."
    },
    {
      "location": "Alpha conditions and all subsequent p exponents",
      "sign_or_abbreviation": "Main-hand alpha and alpha prime",
      "proposed_latex": "\\alpha,\\alpha',p^{q\\alpha-\\alpha'}",
      "evidence": "Rounded curled head with continuing tail; prime is a separate upper stroke. The pale-note initial remains independently doubtful."
    },
    {
      "location": "Divisibility pairs and implication chain",
      "sign_or_abbreviation": "Vertical and crossed vertical; broad double-line arrows; angled inequalities",
      "proposed_latex": "\\mid,\\nmid,\\Longrightarrow,\\geqslant,\\leqslant",
      "evidence": "Plain upright divisibility strokes, crossing diagonal on the two negative divisibility strokes, and two arrow shafts are visible. Inequalities include their short second slant."
    }
  ],
  "check_events": [],
  "brief_feedback": "The supplied C doubt list repeats the n’exist/n’existe locus. A single local decision with an explicit duplicate-accounting note was used. No other convention ambiguity arose."
}

## Reader B

\scanpage{7}
\deleted{\illegible{1}} Soit $a\in\mathbb N^*,b\in\mathbb N^*,c\in\mathbb N^*,\ q\in\mathbb N^*$ \quad $q$ nombre premier $(q\ne1)$

On suppose que $a\mathrel{\underset{1}{\smile}}b$, $a\mathrel{\underset{1}{\smile}}c$, $b\mathrel{\underset{1}{\smile}}c$ (premiers entre eux deux à deux)
\inserted{et $a^q+b^q=c^q$}

On a $c>a$ et $c>b$ car $a\in\mathbb N^*$ et $b\in\mathbb N^*$

On pose $c=a+b'=b+a'$ avec $b'\in\mathbb N^*$ et $a'\in\mathbb N^*$
\[
\begin{aligned}
\text{alors}\qquad a^q+b^q=c^q&=(a+b')^q=\sum_{i=0}^{q}C_q^i\,a^i b'^{\,q-i}\qquad\text{(Newton)}\\
 &=b'^{\,q}+\sum_{i=1}^{q-1}C_q^i\,a^i b'^{\,q-i}+a^q\qquad(\text{car }q\geqslant2)
\end{aligned}
\]
\[
\text{donc}\qquad b^q=\sum_{i=1}^{q-1}C_q^i\,a^i b'^{\,q-i}+b'^{\,q}\tag*{(1)}
\]
la puissance de $b'$ n'étant jamais nulle on peut mettre $b'$ en facteur dans le second membre de (1), donc $b'\mid b^q$ ($b'$ divise $b^q$)

Soit $p$ un nombre premier
% Explicit pair of rising cancellation strokes; the semantic deletion macro's
% generic horizontal rule is suppressed locally so that no third rule is added.
\begingroup
\renewcommand{\ULthickness}{0pt}
\begin{tikzpicture}[baseline=(cancelled.base)]
\node[inner sep=0pt,outer sep=0pt] (cancelled) {\deleted{ou $p=1$}};
\draw[line width=.55pt] ([xshift=-1.5mm,yshift=-1.5mm]cancelled.south west) -- ([xshift=3mm,yshift=4mm]cancelled.north east);
\draw[line width=.25pt] ([xshift=-1.5mm,yshift=-2mm]cancelled.south west) -- ([xshift=3mm,yshift=3.65mm]cancelled.north east);
\end{tikzpicture}
\endgroup
et tel que : $p\mid b'$ donc $p\mid b$. Soit $\alpha\in\mathbb N^*$ et $\alpha'\in\mathbb N^*$ tels que
\[
\begin{aligned}
 &p^{\alpha'}\mid b'\quad\text{et}\quad p^{\alpha'+1}\nmid b'\\
 \text{et}\quad &p^\alpha\mid b\quad\text{et}\quad p^{\alpha+1}\nmid b
\end{aligned}
\]
\margin{$\unsure{a|\alpha}$ \unsure{n'exist|n'existe} pas si on avait $p=1$}
On a $\alpha'\leqslant q\alpha$ car $b'\mid b^q$

\[
\begin{aligned}
(1)\ \Longrightarrow\quad&p^{q\alpha}\mid\sum_{i=1}^{q-1}C_q^i\,a^i b'^{\,q-i}+b'^{\,q}\\
\Longrightarrow\quad&p^{q\alpha}\mid b'\left(\sum_{i=1}^{q-1}C_q^i\,a^i b'^{\,q-i-1}+b'^{\,q-1}\right)\qquad(\text{car }q\geqslant2)
\end{aligned}
\]
posons $b'=p^{\alpha'}b''$ donc $b''\mathrel{\underset{1}{\smile}}p$ (propriété de $\alpha'$)
\[
\begin{aligned}
\Longrightarrow\quad&p^{q\alpha}\mid p^{\alpha'}b''\left(\sum_{i=1}^{q-1}C_q^i\,a^i b'^{\,q-i-1}+b'^{\,q-1}\right)\\
\Longrightarrow\quad&p^{q\alpha-\alpha'}\mid b''\left(\sum_{i=1}^{q-1}C_q^i\,a^i b'^{\,q-i-1}+b'^{\,q-1}\right)\quad\text{car }q\alpha\geqslant\alpha'\\
\Longrightarrow\quad&p^{q\alpha-\alpha'}\mid\sum_{i=1}^{q-1}C_q^i\,a^i b'^{\,q-i-1}+b'^{\,q-1}\quad\text{car }b''\mathrel{\underset{1}{\smile}}p
\end{aligned}
\]
% archive sheet number: 6



{
  "differences": [
    {
      "id": "B007-D01",
      "location": "First line, immediately before Soit",
      "C": "\\deleted{\\illegible{1}}",
      "H": null,
      "reading": "\\deleted{\\illegible{1}}",
      "evidence": "The enlargement shows a dense dark patch with overlaid loops and short projecting top strokes. The internal traces do not yield a defensible character sequence. C’s unreadable cancelled unit is retained.",
      "confidence": "low",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "crops/01_initial_deletion.png",
      "bbox": {
        "image": "full",
        "xyxy": [
          24,
          15,
          174,
          88
        ]
      }
    },
    {
      "id": "B007-D02",
      "location": "Pale note at right of the divisibility conditions, first sign",
      "C": "\\unsure{a|\\alpha}",
      "H": null,
      "reading": "\\unsure{a|\\alpha}",
      "evidence": "A small closed loop is followed by a single descending rightward tail. Its top is crowded and the faint strokes do not isolate a second alpha shoulder. Both a and alpha remain supported; the candidate order is retained.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "crops/02_pale_note.png",
      "bbox": {
        "image": "full",
        "xyxy": [
          1006,
          981,
          1053,
          1013
        ]
      }
    },
    {
      "id": "B007-D03",
      "location": "Pale note, word after the first sign",
      "C": "\\unsure{n'exist|n'existe}",
      "H": null,
      "reading": "\\unsure{n'exist|n'existe}",
      "evidence": "After the n and detached apostrophe, a low letter run ends in a tall stroke with a rightward curved return. The final return supports n’exist; its weak joined portion also leaves n’existe possible. No distinct terminal e is established. The duplicate C_doubts entry refers to this same locus.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "crops/02_pale_note.png",
      "bbox": {
        "image": "full",
        "xyxy": [
          1046,
          967,
          1182,
          1010
        ]
      }
    },
    {
      "id": "B007-D04",
      "location": "Cancellation of ou p=1 in the Soit p sentence",
      "C": "\\deleted{ou $p=1$}",
      "H": null,
      "reading": "\\deleted{ou $p=1$}, with two explicit rising diagonal strokes in TikZ",
      "evidence": "Half a at x=823–1068, y=817–918 shows a long dark rising diagonal and a thinner nearly parallel lower stroke, extending below ou at the left and above the equality at the right. Both strokes are also visible in half b at x=823–1068, y=37–138 (origin of b is full y=780). The words ou p=1 remain readable. The deletion state already agrees with C; the added detail is the paired stroke geometry.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "image": "full",
        "xyxy": [
          823,
          817,
          1068,
          918
        ]
      }
    }
  ],
  "doubts": [
    {
      "location": "First line, blacked-out unit before Soit",
      "reading": "\\deleted{\\illegible{1}}",
      "alternatives": [],
      "confidence": "low",
      "reason": "Overlapping black strokes obscure the internal sequence; the single-unit placeholder is retained.",
      "crop": "crops/01_initial_deletion.png"
    },
    {
      "location": "Pale note, first character",
      "reading": "a",
      "alternatives": [
        "\\alpha"
      ],
      "confidence": "medium",
      "reason": "Small loop and descending tail remain compatible with the two candidates; hand attribution remains undetermined.",
      "crop": "crops/02_pale_note.png"
    },
    {
      "location": "Pale note, word after first sign",
      "reading": "n'exist",
      "alternatives": [
        "n'existe"
      ],
      "confidence": "medium",
      "reason": "Terminal tall stroke has a curved rightward continuation; a separate final e cannot be isolated, and the joined reading remains possible.",
      "crop": "crops/02_pale_note.png"
    }
  ],
  "notes": {
    "page_content": "The page writes hypotheses using a,b,c,q, a binomial expansion, a numbered equality (1), two p-power divisibility pairs using alpha and alpha prime, and a descending divisibility chain. A faint two-line note stands at the right.",
    "authors_own_uncertainty": "No explicit authorial question, doubt word, or question mark was read. The pale note is transcribed with editorial uncertainty as “a/alpha n’exist/n’existe pas si on avait p=1”.",
    "title_date_page_counts": "No title or date was read. The pencilled bottom-left 6 is retained only in the archive-sheet-number comment. There is one manuscript sheet and the numbered equation (1).",
    "mathematics_led_reading_decisions": "Final crowded exponents and summation bounds were enlarged and read stroke by stroke: upper q−1, lower i=1, q−i−1 in the summand and q−1 in the final term. All these readings agree with C. No algebraic computation, theorem verification, or proof check was performed.",
    "hands": "The dark main writing forms a consistent upright hand, recorded as another unnamed hand in accordance with the supplied packet’s other-hand designation. Attribution of the paler note remains undetermined.",
    "view_attestation": "The current UTC time was recorded before the brief and packet were read. The full image was viewed exactly once; supplied half a exactly once; supplied half b exactly once. The three generated crops were each viewed exactly once. No other readers, other page images, OCR, internet, or text-recognition outputs were used.",
    "half_geometry": "Full image 1405×1720; both halves 1405×940. Half a begins at full y=0; half b begins at full y=780, with 160 pixels of overlap.",
    "H_status": "metadata.json states hua_has=nothing; H.tex is empty. Every report row has H=null and diff_H=false.",
    "boundary_note": "The final-two-sums crop retains both target rows’ full summation bounds and exponents. It includes clipped fragments of the preceding row at its top, and only the beginning of the final car at its right; those are contextual fragments. The complete preceding row and both car explanations were read in half b. No target was recropped.",
    "report_tex_alignment": "All original C doubts remain in reading.tex. The main text, formulas, insertion and cancellation state agree with C. The only added transcription detail is the explicitly drawn pair of cancellation strokes over ou p=1."
  },
  "notation": [
    {
      "location": "Top line; repeated membership statements",
      "sign": "Doubled left/upward strokes of N and small raised asterisk",
      "latex": "\\mathbb N^*"
    },
    {
      "location": "Second main line; posons line; final explanation",
      "sign": "Shallow bowl with a detached short hooked 1 below",
      "latex": "\\mathrel{\\underset{1}{\\smile}}"
    },
    {
      "location": "All binomial sums",
      "sign": "Open C with raised dotted i and lowered q",
      "latex": "C_q^i"
    },
    {
      "location": "First expansion and subsequent sums",
      "sign": "First upper q and lower i=0; later upper q−1 and lower i=1",
      "latex": "\\sum_{i=0}^{q},\\sum_{i=1}^{q-1}"
    },
    {
      "location": "On pose line and later factors",
      "sign": "Single or paired detached rising ticks",
      "latex": "a',b',b''"
    },
    {
      "location": "Soit alpha line and later p powers",
      "sign": "Main-hand looped alpha with taller returning right stroke, and separate prime",
      "latex": "\\alpha,\\alpha',p^{q\\alpha-\\alpha'}"
    },
    {
      "location": "Divisibility conditions and chain",
      "sign": "Plain upright relation; crossed upright; broad two-line rightward implication arrows",
      "latex": "\\mid,\\nmid,\\Longrightarrow"
    },
    {
      "location": "car q≥2 twice; On a; penultimate car",
      "sign": "Angled inequality strokes with separate lower equality stroke",
      "latex": "\\geqslant,\\leqslant"
    },
    {
      "location": "Pale note",
      "sign": "Small loop with diagonal tail; faint final word termination",
      "latex": "\\unsure{a|\\alpha}\\ \\unsure{n'exist|n'existe}"
    }
  ],
  "check_events": [],
  "brief_feedback": [
    "The record vocabulary gives no dedicated class for a deletion whose wording/state agrees but whose two visible cancellation strokes need explicit geometry. It is recorded as drawing or diagram, with diff_C=true only for the added paired-stroke detail.",
    "C_doubts.txt repeats the pale n’exist/n’existe locus. Both supplied entries are covered by one local decision B007-D03.",
    "For the inline deletion drawing, a local zero-thickness ulem rule keeps the required deleted macro while the two actual diagonal cancellation strokes are rendered in TikZ; this avoids adding a generic horizontal stroke."
  ]
}

## Reader C

\scanpage{7}
\deleted{\illegible{1}} Soit $a\in\mathbb N^*,b\in\mathbb N^*,c\in\mathbb N^*,\ q\in\mathbb N^*$ \quad $q$ nombre premier $(q\ne1)$

On suppose que $a\mathrel{\underset{1}{\smile}}b$, $a\mathrel{\underset{1}{\smile}}c$, $b\mathrel{\underset{1}{\smile}}c$ (premiers entre eux deux à deux)
\inserted{et $a^q+b^q=c^q$}

On a $c>a$ et $c>b$ car $a\in\mathbb N^*$ et $b\in\mathbb N^*$

On pose $c=a+b'=b+a'$ avec $b'\in\mathbb N^*$ et $a'\in\mathbb N^*$
\[
\begin{aligned}
\text{alors}\qquad a^q+b^q=c^q&=(a+b')^q=\sum_{i=0}^{q}C_q^i\,a^i b'^{\,q-i}\qquad\text{(Newton)}\\
 &=b'^{\,q}+\sum_{i=1}^{q-1}C_q^i\,a^i b'^{\,q-i}+a^q\qquad(\text{car }q\geqslant2)
\end{aligned}
\]
\[
\text{donc}\qquad b^q=\sum_{i=1}^{q-1}C_q^i\,a^i b'^{\,q-i}+b'^{\,q}\tag*{(1)}
\]
la puissance de $b'$ n'étant jamais nulle on peut mettre $b'$ en facteur dans le second membre de (1), donc $b'\mid b^q$ ($b'$ divise $b^q$)

Soit $p$ un nombre premier \deleted{ou $p=1$} et tel que : $p\mid b'$ donc $p\mid b$. Soit $\alpha\in\mathbb N^*$ et $\alpha'\in\mathbb N^*$ tels que
\[
\begin{aligned}
 &p^{\alpha'}\mid b'\quad\text{et}\quad p^{\alpha'+1}\nmid b'\\
 \text{et}\quad &p^\alpha\mid b\quad\text{et}\quad p^{\alpha+1}\nmid b
\end{aligned}
\]
\margin{$\unsure{a|\alpha}$ \unsure{n'exist|n'existe} pas si on avait $p=1$}
On a $\alpha'\leqslant q\alpha$ car $b'\mid b^q$

\[
\begin{aligned}
(1)\ \Longrightarrow\quad&p^{q\alpha}\mid\sum_{i=1}^{q-1}C_q^i\,a^i b'^{\,q-i}+b'^{\,q}\\
\Longrightarrow\quad&p^{q\alpha}\mid b'\left(\sum_{i=1}^{q-1}C_q^i\,a^i b'^{\,q-i-1}+b'^{\,q-1}\right)\qquad(\text{car }q\geqslant2)
\end{aligned}
\]
posons $b'=p^{\alpha'}b''$ donc $b''\mathrel{\underset{1}{\smile}}p$ (propriété de $\alpha'$)
\[
\begin{aligned}
\Longrightarrow\quad&p^{q\alpha}\mid p^{\alpha'}b''\left(\sum_{i=1}^{q-1}C_q^i\,a^i b'^{\,q-i-1}+b'^{\,q-1}\right)\\
\Longrightarrow\quad&p^{q\alpha-\alpha'}\mid b''\left(\sum_{i=1}^{q-1}C_q^i\,a^i b'^{\,q-i-1}+b'^{\,q-1}\right)\quad\text{car }q\alpha\geqslant\alpha'\\
\Longrightarrow\quad&p^{q\alpha-\alpha'}\mid\sum_{i=1}^{q-1}C_q^i\,a^i b'^{\,q-i-1}+b'^{\,q-1}\quad\text{car }b''\mathrel{\underset{1}{\smile}}p
\end{aligned}
\]
% archive sheet number: 6



{
  "differences": [
    {
      "id": "007-C-01",
      "location": "Opening black cancellation immediately before Soit",
      "C": "\\deleted{\\illegible{1}}",
      "H": null,
      "reading": "\\deleted{\\illegible{1}}",
      "evidence": "The enlarged black patch contains dense overlapping loops, short top projections and a rounded lower outline. No internal character sequence can be recovered. The original unreadability is retained; one placeholder denotes the single compact unreadable item.",
      "confidence": "low",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "01_top_cancel.png",
      "bbox": [
        22,
        18,
        180,
        94
      ]
    },
    {
      "id": "007-C-02",
      "location": "Pale marginal note, initial character",
      "C": "\\unsure{a|\\alpha}",
      "H": null,
      "reading": "\\unsure{a|\\alpha}",
      "evidence": "The complete pale note was enlarged. Its initial character has a low oval at left and a rightward descending tail. The strokes support the existing a and alpha candidates without settling their choice; a remains first.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "04_pale_note.png",
      "bbox": [
        1006,
        961,
        1326,
        1053
      ]
    },
    {
      "id": "007-C-03",
      "location": "Pale marginal note, ending of n’exist / n’existe",
      "C": "\\unsure{n'exist|n'existe}",
      "H": null,
      "reading": "\\unsure{n'exist|n'existe}",
      "evidence": "After n and its apostrophe, the word ends in a tall stem with a short rightward curved continuation. The continuation has insufficient independent structure to settle the presence of a final e. Retain n’exist first and n’existe as the supported alternative. The two uncertainty-table entries in C_doubts concern this single locus.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "04_pale_note.png",
      "bbox": [
        1006,
        961,
        1326,
        1053
      ]
    }
  ],
  "doubts": [
    {
      "location": "Opening black cancellation",
      "reading": "\\deleted{\\illegible{1}}",
      "alternatives": [],
      "confidence": "low",
      "reason": "Dense overlapping ink prevents recovery of a character sequence.",
      "crop": "01_top_cancel.png"
    },
    {
      "location": "Pale note, initial character",
      "reading": "a",
      "alternatives": [
        "\\alpha"
      ],
      "confidence": "medium",
      "reason": "Low oval and falling right tail support both existing shapes.",
      "crop": "04_pale_note.png"
    },
    {
      "location": "Pale note, word ending",
      "reading": "n'exist",
      "alternatives": [
        "n'existe"
      ],
      "confidence": "medium",
      "reason": "Terminal tall stroke and short rightward continuation do not settle a separate final e.",
      "crop": "04_pale_note.png"
    }
  ],
  "notes": {
    "page_content": "Handwritten arithmetic argument beginning Soit a∈ℕ* and introducing a prime q, pairwise bowl/1 signs, the interlinear equality a^q+b^q=c^q, a binomial expansion, the numbered expression (1), divisibility pairs and a final implication chain. This describes the written content only.",
    "author_own_uncertainty": {
      "exact_words": null,
      "comment": "No explicit authorial words of uncertainty were observed. Editorial uncertainty remains at the opening cancellation and two loci in the pale note."
    },
    "pale_note_exact_reading": "\\unsure{a|\\alpha} \\unsure{n'exist|n'existe} pas si on avait p=1",
    "title_date_page_counts": {
      "title": null,
      "date": null,
      "manuscript_page_number": null,
      "archive_sheet_number": "6",
      "scan_pages_read": 1
    },
    "mathematics_led_reading_decisions": "No mathematical derivation was used to choose or repair ink. The comparison marks, summation limits, primes and dotted i forms were read from their visible strokes.",
    "source_status": {
      "C": "Complete supplied witness, visually checked throughout",
      "H": "nothing; H has no full text and contributes no collation rows"
    },
    "view_attestation": {
      "whole_views": 1,
      "half_a_views": 1,
      "half_b_views": 1,
      "crop_views": 6,
      "crops_created": 6,
      "no_recrops": true,
      "whole_dimensions": [
        1405,
        1720
      ],
      "half_dimensions": [
        1405,
        940
      ],
      "half_a_full_scan_origin": [
        0,
        0
      ],
      "half_b_full_scan_origin": [
        0,
        780
      ]
    },
    "actual_order": "Read brief; recorded current UTC start; read assigned packet, notation snapshot and preamble; checked image dimensions; viewed whole once; viewed a once; viewed b once; read crop helper; made six crops; viewed each crop once; wrote and cross-checked local outputs.",
    "visual_resolutions_without_witness_difference": [
      "Crop 02: main comparison angle plus separate lower oblique stroke supports C’s geqslant.",
      "Crop 03: mark left below the summation is the dot above the lower-limit i; all upper and lower limits agree with C.",
      "Crop 05: crowded lower-limit i, coefficient indices and two exponent minus strokes agree with C; the dot under the sum belongs to i.",
      "Crop 06: the mark above the a factor is the dot of its raised i; the last bowl/1 sign and double prime are visible."
    ],
    "physical_marks": "Opening black cancellation; two rising cancellation strokes over ou p=1; interlinear et a^q+b^q=c^q; pale two-line marginal note; archive pencil 6. The remaining small dots inspected are constituents of dotted i forms. No independent drawing or diagram was observed.",
    "crop_bounds": "All intended crop targets retain complete ink bounds. Crops 05 and 06 intersect incidental neighboring-line fragments; crop 04 includes tips of adjacent darker writing. Those peripheral fragments are not used as evidence for the target readings.",
    "independence": "No other reader or other page was read. No OCR, internet, external source, or delegation was used."
  },
  "notation": [
    {
      "location": "Top line and conditions on b′, a′, α, α′",
      "sign": "Doubled left N strokes with a raised star",
      "latex": "\\mathbb N^*"
    },
    {
      "location": "Second line and both lower coprimality expressions",
      "sign": "Shallow bowl with separate hooked 1 below",
      "latex": "\\mathrel{\\underset{1}{\\smile}}"
    },
    {
      "location": "All expansions and sums",
      "sign": "C with dotted i above and q below; summation with independently placed limits",
      "latex": "C_q^i,\\sum_{i=1}^{q-1}"
    },
    {
      "location": "Upper comparison and lower implication comments",
      "sign": "Main angle with a separate oblique lower stroke",
      "latex": "\\geqslant"
    },
    {
      "location": "Right of second divisibility pair",
      "sign": "Left-pointing angle with separate lower oblique stroke",
      "latex": "\\leqslant"
    },
    {
      "location": "Divisibility pairs",
      "sign": "Long vertical stroke; crossed form with diagonal stroke",
      "latex": "\\mid,\\nmid"
    },
    {
      "location": "Implication chain",
      "sign": "Two horizontal strokes with right-pointing head",
      "latex": "\\Longrightarrow"
    },
    {
      "location": "Introduced exponents and later powers of p",
      "sign": "Curled alpha, separate raised prime stroke on alpha-prime",
      "latex": "\\alpha,\\alpha'"
    },
    {
      "location": "Definition of b′ and final lines",
      "sign": "One or two separate short raised strokes after b",
      "latex": "b',b''"
    },
    {
      "location": "Numbered sum and final two rows",
      "sign": "Separated dot plus short lower stem in i; last raised i dot is high above a",
      "latex": "i"
    }
  ],
  "check_events": [],
  "brief_feedback": [
    "The opening black cancellation has no surviving word boundary. The existing illegible{1} is retained to designate one compact unreadable item, without claiming recovery of a one-word text.",
    "C_doubts repeats the n’exist/n’existe uncertainty in two rows; the report records one local decision for that physical locus."
  ]
}

--- A
+++ B
@@ -18,7 +18,18 @@
 \]
 la puissance de $b'$ n'étant jamais nulle on peut mettre $b'$ en facteur dans le second membre de (1), donc $b'\mid b^q$ ($b'$ divise $b^q$)
 
-Soit $p$ un nombre premier \deleted{ou $p=1$} et tel que : $p\mid b'$ donc $p\mid b$. Soit $\alpha\in\mathbb N^*$ et $\alpha'\in\mathbb N^*$ tels que
+Soit $p$ un nombre premier
+% Explicit pair of rising cancellation strokes; the semantic deletion macro's
+% generic horizontal rule is suppressed locally so that no third rule is added.
+\begingroup
+\renewcommand{\ULthickness}{0pt}
+\begin{tikzpicture}[baseline=(cancelled.base)]
+\node[inner sep=0pt,outer sep=0pt] (cancelled) {\deleted{ou $p=1$}};
+\draw[line width=.55pt] ([xshift=-1.5mm,yshift=-1.5mm]cancelled.south west) -- ([xshift=3mm,yshift=4mm]cancelled.north east);
+\draw[line width=.25pt] ([xshift=-1.5mm,yshift=-2mm]cancelled.south west) -- ([xshift=3mm,yshift=3.65mm]cancelled.north east);
+\end{tikzpicture}
+\endgroup
+et tel que : $p\mid b'$ donc $p\mid b$. Soit $\alpha\in\mathbb N^*$ et $\alpha'\in\mathbb N^*$ tels que
 \[
 \begin{aligned}
  &p^{\alpha'}\mid b'\quad\text{et}\quad p^{\alpha'+1}\nmid b'\\
@@ -43,4 +54,3 @@
 \end{aligned}
 \]
 % archive sheet number: 6
-

--- A
+++ C
@@ -43,4 +43,3 @@
 \end{aligned}
 \]
 % archive sheet number: 6
-

--- B
+++ C
@@ -18,18 +18,7 @@
 \]
 la puissance de $b'$ n'étant jamais nulle on peut mettre $b'$ en facteur dans le second membre de (1), donc $b'\mid b^q$ ($b'$ divise $b^q$)
 
-Soit $p$ un nombre premier
-% Explicit pair of rising cancellation strokes; the semantic deletion macro's
-% generic horizontal rule is suppressed locally so that no third rule is added.
-\begingroup
-\renewcommand{\ULthickness}{0pt}
-\begin{tikzpicture}[baseline=(cancelled.base)]
-\node[inner sep=0pt,outer sep=0pt] (cancelled) {\deleted{ou $p=1$}};
-\draw[line width=.55pt] ([xshift=-1.5mm,yshift=-1.5mm]cancelled.south west) -- ([xshift=3mm,yshift=4mm]cancelled.north east);
-\draw[line width=.25pt] ([xshift=-1.5mm,yshift=-2mm]cancelled.south west) -- ([xshift=3mm,yshift=3.65mm]cancelled.north east);
-\end{tikzpicture}
-\endgroup
-et tel que : $p\mid b'$ donc $p\mid b$. Soit $\alpha\in\mathbb N^*$ et $\alpha'\in\mathbb N^*$ tels que
+Soit $p$ un nombre premier \deleted{ou $p=1$} et tel que : $p\mid b'$ donc $p\mid b$. Soit $\alpha\in\mathbb N^*$ et $\alpha'\in\mathbb N^*$ tels que
 \[
 \begin{aligned}
  &p^{\alpha'}\mid b'\quad\text{et}\quad p^{\alpha'+1}\nmid b'\\
