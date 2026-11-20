## Reader A

\scanpage{8}
Supposons que $q\alpha-\alpha'\ne0$ alors
\[
\begin{aligned}
(1)\ \Longrightarrow\quad &p\mid\sum_{i=1}^{q-1}C_q^i\,a^i b'^{\,q-i-1}+b'^{\,q-1}\\
\Longrightarrow\quad &p\mid q\,a^{q-1}\qquad\text{Car }p\mid b'\ \text{et pour }i\ne q-1\quad q-i-1\deleted{\ne0}>0
\end{aligned}
\]
or $p\mid b'$ et $b'\mid b^q$ donc $b'\mathrel{\underset{1}{\smile}}a$ donc $p\mathrel{\underset{1}{\smile}}a$

\deleted{donc si $\unsure{p\ne1|p\ne q}$}
\[
(1)\ \Longrightarrow\quad p\mid q\qquad\text{donc }\deleted{p=1\ \text{ou }}p=q\quad(\text{si }q\alpha-\alpha'\ne0)
\]
Donc si $p\ne q$ \quad
\begin{tikzpicture}[baseline=(p.base)]
\node[inner sep=0pt] (p) at (0,0) {$p$ premier};
\node[inner sep=0pt,anchor=north] at (0,-.28) {\inserted{ou $p=1$}};
% Small dark triangular mark above the addition; its guiding function is uncertain.
\fill (-.32,-.20) -- (-.16,-.15) -- (-.16,-.25) -- cycle;
\end{tikzpicture}
et $p\mid b'$ alors $\alpha'=q\alpha$
\begin{tikzpicture}[baseline=(u.base)]
\node[inner sep=0pt,anchor=west] (u) at (.22,0)
 {\rlap{on l'impose sans risque}\phantom{\deleted{on l'impose sans risque}}};
\node[inner sep=0pt,anchor=west] (v) at (.72,-.42)
 {\rlap{si $p=1$}\phantom{\deleted{si $p=1$}}};
\node[inner sep=0pt] at (0,-.20)
 {\rlap{$\Bigg($}\phantom{\deleted{$\Bigg($}}};
\node[inner sep=0pt] at (5.2,-.20)
 {\rlap{$\Bigg)$}\phantom{\deleted{$\Bigg)$}}};
% Two separate oblique cancellations over the two-line parenthesis.
\draw[line width=.45pt] (.06,-.62) -- (2.48,.16);
\draw[line width=.45pt] (2.45,-.62) -- (5.13,.16);
\end{tikzpicture}

Donc $\exists\,b_0\in\mathbb N^*$ et $\exists\,\gamma\in\mathbb N$ tel que $b'=q^\gamma b_0^q$ \margin{$q\nmid b_0$}

de plus $b_0\mid b$ et si $b=b_0 b''$ alors $b_0\mathrel{\underset{1}{\smile}}b''$ ?

De même $\exists\,a_0\in\mathbb N^*$ et $\exists\,\unsure{\zeta|\delta}\in\mathbb N$ tel que $a'=q^\zeta a_0^q$ avec $a_0\mid a$ et si $a=a_0a''$ alors $a_0\mathrel{\underset{1}{\smile}}a''$ ?

or $a\mathrel{\underset{1}{\smile}}b\Longrightarrow a_{\deleted{\unsure{0}}}'\mathrel{\underset{1}{\smile}}b'\Longrightarrow\zeta\times\gamma=0$ (et aussi $a_0\mathrel{\underset{1}{\smile}}b_0$)

Je suppose désormais que $\zeta=0$ donc $a'=a_0^q$

\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\node[anchor=west,inner sep=0pt,font=\small] at (0,.80)
 {Donc \quad $c=b+a_0^q=a+q^\gamma b_0^q$};
\node[anchor=north west,inner sep=0pt,font=\footnotesize] at (6.68,1.43)
 {\begin{tabular}{@{}l@{}}
 pour $q=2$ on a, $a_0=b_0=1$,\\
 $\gamma=1$, $b=4$, $a=3$, $c=5$
 \end{tabular}};
% Open right border; the left edge meets the shared long upper rule.
\draw[line width=.35pt] (12.12,1.66) -- (6.50,1.66) -- (6.50,.03);
\draw[line width=.35pt] (0,.22) -- (6.50,.03) -- (12.12,-.06);
\node[anchor=west,inner sep=0pt,font=\footnotesize] at (0,-.43)
 {Je fais l'hypothése suivante};
\node[anchor=west,inner sep=0pt,font=\footnotesize] at (5.58,-.43)
 {si $q$ premier et $1\leqslant i<q$ alors $q\mid C_q^i$};
\draw[line width=.35pt] (0,-.83) -- (12.12,-1.08);
\end{tikzpicture}}
alors Si $q\geqslant3$ et $q\alpha-\alpha'\geqslant2$ \deleted{\unsure{alors}} on a \inserted{$p=q,\ {\unsure{a|\alpha}}'=\gamma$}
\[
\begin{aligned}
(1)\ \Longrightarrow\quad
 &\deleted{\unsure{p^{2}|p}}q^2\mid q\,a^{q-1}\quad
 \begin{tikzpicture}[baseline=(d.base)]
 \node[inner sep=0pt] (d) at (0,0)
  {\rlap{ou $p=1$}\phantom{\deleted{ou $p=1$}}};
 \draw[line width=.45pt] (d.west) -- (d.east)
  .. controls +(0.22,-.04) and +(0.22,-.06) ..
  ([yshift=-2pt]d.east) -- ([yshift=-2pt]d.west);
 \end{tikzpicture}\\[.8ex]
\Longrightarrow\quad
 &q\mid a^{q-1}\quad
 \begin{tikzpicture}[baseline=(d.base)]
 \node[inner sep=0pt] (d) at (0,0)
  {\rlap{ou $p=1\Longrightarrow p=1$}\phantom{\deleted{ou $p=1\Longrightarrow p=1$}}};
 \draw[line width=.45pt] ([xshift=-2pt,yshift=-2pt]d.west)
  -- ([xshift=2pt,yshift=4pt]d.east);
 \node[inner sep=0pt,anchor=south] at (0,.23)
  {\inserted{absurde car $q\nmid a$}};
 \end{tikzpicture}
\end{aligned}
\]
Donc $\gamma=0$ ou $\gamma=$
\begin{tikzpicture}[baseline=(q.base)]
\node[inner sep=0pt] (q) at (0,0)
 {$\rlap{$q$}\phantom{\deleted{q}}$};
% The live entry is physically raised above and to the right of the cancelled q.
\node[inner sep=0pt,anchor=south west] at (-.01,.22) {$q\alpha-1$};
\draw[line width=.45pt] (-.20,-.02) -- (.33,.28)
 .. controls (.48,.32) and (-.26,-.17) .. (-.20,-.02);
\draw[line width=.45pt] (-.18,-.22) -- (.30,.10)
 .. controls (.39,.16) and (-.29,-.34) .. (-.18,-.22);
\draw[line width=.45pt] (.02,-.24) -- (-.03,-.40);
\end{tikzpicture}
(sous réserve que l'hypothése est vraie)%
\margin{\begin{tikzpicture}[baseline=(n.base)]
\node[inner sep=0pt,text width=.85\marginparwidth] (n)
 {C'est peut-être interessant car ici $2$ est mis à part dans
 \(\mathord{\overset{\scriptscriptstyle\unsure{/}}{\vphantom{l}}}\)l'ensemble des nombres premiers};
% Small detached rising stroke before l'ensemble: role and hand unresolved.
% Return arrow rises at the right from the final parenthesis toward this note.
\draw[->] ([yshift=-.25cm]n.south east) -- ++(.16,0) |- (n.north east);
\end{tikzpicture}}
% archive sheet number: 7



{
  "differences": [
    {
      "id": "A01",
      "location": "Second implication: Car",
      "C": "\\text{car }",
      "H": null,
      "reading": "\\text{Car }",
      "evidence": "Initial open C rises well above following a and r; its capital curve is visible on half a. Nearby final c in donc is shorter.",
      "confidence": "high",
      "kind": "misread word",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "source": "full",
        "xyxy": [
          546,
          225,
          634,
          276
        ]
      }
    },
    {
      "id": "A02",
      "location": "First isolated struck line",
      "C": "\\deleted{donc si $\\unsure{p\\ne1|p\\ne q}$}",
      "H": null,
      "reading": "\\deleted{donc si $\\unsure{p\\ne1|p\\ne q}$}",
      "evidence": "Tall d, onc and si survive. The p-like descending stem and comparison strokes survive, but the final upright/angled group is crossed repeatedly. Its lower shape does not settle 1 versus q.",
      "confidence": "low",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "02_first_struck_line.png",
      "bbox": {
        "source": "full",
        "xyxy": [
          94,
          383,
          482,
          455
        ]
      }
    },
    {
      "id": "A03",
      "location": "Mark above ou p=1, below p premier",
      "C": "\\inserted{ou $p=1$}",
      "H": null,
      "reading": "Same addition below premier, with small filled triangular mark immediately above",
      "evidence": "Half a shows a compact dark left-pointing wedge above ou. The triangle is reproduced while its guiding function remains uncertain.",
      "confidence": "medium",
      "kind": "omission",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "source": "full",
        "xyxy": [
          580,
          543,
          757,
          634
        ]
      }
    },
    {
      "id": "A04",
      "location": "Deleted parenthesis on l'impose sans risque / si p=1",
      "C": "\\deleted{(on l'impose sans risque si $p=1$)}",
      "H": null,
      "reading": "Same deleted words and parentheses, with two rising diagonal cancellation strokes",
      "evidence": "Half a shows two separate obliques, one crossing the left/lower si area toward impose and another from the lower middle toward the right end of risque. Underlying words and both tall parentheses are legible.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "source": "full",
        "xyxy": [
          891,
          594,
          1345,
          709
        ]
      }
    },
    {
      "id": "A05",
      "location": "Second existential line: second letter",
      "C": "\\unsure{\\zeta|\\delta}",
      "H": null,
      "reading": "\\unsure{\\zeta|\\delta}",
      "evidence": "Sloping upper stroke turns sharply into a rounded lower hook with a small closed end. Its raised repetition has the same form. Zeta remains the first candidate, delta survives as an alternative.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "03_second_letter.png",
      "bbox": {
        "source": "full",
        "xyxy": [
          575,
          875,
          1152,
          981
        ]
      }
    },
    {
      "id": "A06",
      "location": "Cancelled subscript under a prime",
      "C": "a_{\\deleted{\\unsure{0}}}'",
      "H": null,
      "reading": "a_{\\deleted{\\unsure{0}}}'",
      "evidence": "The a and prime are clear. A compact filled black patch at the right foot of a occupies subscript height; an independent zero contour cannot be isolated. Zero remains a doubtful candidate.",
      "confidence": "low",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "04_cancelled_subscript.png",
      "bbox": {
        "source": "full",
        "xyxy": [
          267,
          1043,
          708,
          1146
        ]
      }
    },
    {
      "id": "A07",
      "location": "Numerical example bracket and long rules",
      "C": "Three-sided border in separate margin picture; two independent rules",
      "H": null,
      "reading": "Open-right bracket whose left edge meets the shared upper long rule, with second rule below hypothesis",
      "evidence": "Half b shows a top boundary reaching toward the right edge and left vertical down to the first page-wide rule. This rule continues across the example's bottom. The lower hypothesis rule is separate. The shared geometry is drawn explicitly.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "source": "full",
        "xyxy": [
          17,
          1205,
          1386,
          1436
        ]
      }
    },
    {
      "id": "A08",
      "location": "Cancelled word before on a",
      "C": "\\deleted{\\unsure{alors}}",
      "H": null,
      "reading": "\\deleted{\\unsure{alors}}",
      "evidence": "Tall l and rounded/angled remnants survive below zigzag crossings. The group supports alors; overlapping black strokes still obscure initial and terminal contours.",
      "confidence": "low",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "06_on_a_addition.png",
      "bbox": {
        "source": "full",
        "xyxy": [
          547,
          1384,
          994,
          1470
        ]
      }
    },
    {
      "id": "A09",
      "location": "Pale equation after on a",
      "C": "\\inserted{$p=q,\\ {\\unsure{a|\\alpha}}'=\\gamma$}",
      "H": null,
      "reading": "\\inserted{$p=q,\\ {\\unsure{a|\\alpha}}'=\\gamma$}",
      "evidence": "Pale p=q and comma are legible. Under the prime is a small oval with short right continuation; a remains primary, alpha remains possible. Equality and looped gamma follow clearly.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "06_on_a_addition.png",
      "bbox": {
        "source": "full",
        "xyxy": [
          547,
          1384,
          994,
          1470
        ]
      }
    },
    {
      "id": "A10",
      "location": "Cancelled p-like entry before lower q squared",
      "C": "\\deleted{\\unsure{p^{2}|p}}",
      "H": null,
      "reading": "\\deleted{\\unsure{p^{2}|p}}",
      "evidence": "Descending stem and right bowl support p. A compact group above/right could preserve exponent 2 but merges with cancellation. The enlarged strokes do not settle p squared versus p.",
      "confidence": "low",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "07_lower_cancelled_p.png",
      "bbox": {
        "source": "full",
        "xyxy": [
          96,
          1444,
          451,
          1545
        ]
      }
    },
    {
      "id": "A11",
      "location": "Pale absurde car q nondivisibility a",
      "C": "\\deleted{\\text{ou }p=1\\Longrightarrow p=1}\\ \\inserted{\\text{absurde car }q\\nmid a}",
      "H": null,
      "reading": "Same insertion placed above cancelled ou p=1 implies p=1",
      "evidence": "Pale absurde car runs directly above the rising cancellation; q crossed-bar a stands above final dark p=1. The transcription places this addition above its target.",
      "confidence": "high",
      "kind": "insertion or placement",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": null,
      "readers_crop": "08_lower_overlap.png",
      "bbox": {
        "source": "full",
        "xyxy": [
          450,
          1448,
          837,
          1598
        ]
      }
    },
    {
      "id": "A12",
      "location": "First lower ou p=1 cancellation",
      "C": "\\deleted{\\text{ou }p=1}",
      "H": null,
      "reading": "Same deleted wording with paired cancellation passes and hooked return",
      "evidence": "Two close passes through the phrase join in a rounded return at the right of 1. Both passes and the return are drawn.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": null,
      "readers_crop": "08_lower_overlap.png",
      "bbox": {
        "source": "full",
        "xyxy": [
          450,
          1448,
          837,
          1598
        ]
      }
    },
    {
      "id": "A13",
      "location": "Final cancelled q and raised q alpha minus 1",
      "C": "{\\deleted{q}}^{q\\alpha-1}",
      "H": null,
      "reading": "Cancelled q with intact q alpha minus 1 raised above and right",
      "evidence": "Cancelled glyph has a round head and long descending right stem crossed by two rising looped strokes. Above, q, tall alpha, minus and 1 are individually legible. Their physical raised placement is drawn without mathematical reconstruction.",
      "confidence": "high",
      "kind": "other",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": "resolved",
      "readers_crop": "09_final_replacement.png",
      "bbox": {
        "source": "full",
        "xyxy": [
          516,
          1577,
          739,
          1700
        ]
      }
    },
    {
      "id": "A14",
      "location": "Detached stroke upper-left of l'ensemble",
      "C": "No separate mark",
      "H": null,
      "reading": "\\unsure{/} immediately before and above l'ensemble",
      "evidence": "A short detached rising dark stroke is visible just left of the tall initial l. Its slash-like shape is supported; its attachment to the letter, role and hand remain unresolved.",
      "confidence": "low",
      "kind": "omission",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": null,
      "readers_crop": "10_right_note.png",
      "bbox": {
        "source": "full",
        "xyxy": [
          847,
          1533,
          870,
          1554
        ]
      }
    }
  ],
  "doubts": [
    {
      "location": "First isolated struck line",
      "reading": "\\deleted{donc si $\\unsure{p\\ne1|p\\ne q}$}",
      "alternatives": [
        "p\\ne q"
      ],
      "confidence": "low",
      "reason": "Tall d, onc and si survive. The p-like descending stem and comparison strokes survive, but the final upright/angled group is crossed repeatedly. Its lower shape does not settle 1 versus q.",
      "crop": "02_first_struck_line.png"
    },
    {
      "location": "Second existential line: second letter",
      "reading": "\\unsure{\\zeta|\\delta}",
      "alternatives": [
        "\\delta"
      ],
      "confidence": "medium",
      "reason": "Sloping upper stroke turns sharply into a rounded lower hook with a small closed end. Its raised repetition has the same form. Zeta remains the first candidate, delta survives as an alternative.",
      "crop": "03_second_letter.png"
    },
    {
      "location": "Cancelled subscript under a prime",
      "reading": "a_{\\deleted{\\unsure{0}}}'",
      "alternatives": [
        "unrecovered subscript; zero only a candidate"
      ],
      "confidence": "low",
      "reason": "The a and prime are clear. A compact filled black patch at the right foot of a occupies subscript height; an independent zero contour cannot be isolated. Zero remains a doubtful candidate.",
      "crop": "04_cancelled_subscript.png"
    },
    {
      "location": "Cancelled word before on a",
      "reading": "\\deleted{\\unsure{alors}}",
      "alternatives": [
        "word obscured by cancellation"
      ],
      "confidence": "low",
      "reason": "Tall l and rounded/angled remnants survive below zigzag crossings. The group supports alors; overlapping black strokes still obscure initial and terminal contours.",
      "crop": "06_on_a_addition.png"
    },
    {
      "location": "Pale equation after on a",
      "reading": "\\inserted{$p=q,\\ {\\unsure{a|\\alpha}}'=\\gamma$}",
      "alternatives": [
        "\\alpha'=\\gamma"
      ],
      "confidence": "medium",
      "reason": "Pale p=q and comma are legible. Under the prime is a small oval with short right continuation; a remains primary, alpha remains possible. Equality and looped gamma follow clearly.",
      "crop": "06_on_a_addition.png"
    },
    {
      "location": "Cancelled p-like entry before lower q squared",
      "reading": "\\deleted{\\unsure{p^{2}|p}}",
      "alternatives": [
        "p without recovered exponent"
      ],
      "confidence": "low",
      "reason": "Descending stem and right bowl support p. A compact group above/right could preserve exponent 2 but merges with cancellation. The enlarged strokes do not settle p squared versus p.",
      "crop": "07_lower_cancelled_p.png"
    },
    {
      "location": "Detached stroke upper-left of l'ensemble",
      "reading": "\\unsure{/} immediately before and above l'ensemble",
      "alternatives": [
        "detached onset of l; role unresolved"
      ],
      "confidence": "low",
      "reason": "A short detached rising dark stroke is visible just left of the tall initial l. Its slash-like shape is supported; its attachment to the letter, role and hand remain unresolved.",
      "crop": "10_right_note.png"
    }
  ],
  "notes": {
    "page_content": "Handwritten divisibility deductions and factorizations, queried coprimality expressions, the writer's assumption, a numerical example, ruled hypothesis, altered lower implications, qualified final line and right note.",
    "authors_own_uncertainty": [
      "alors $b_0\\mathrel{\\underset{1}{\\smile}}b''$ ?",
      "alors $a_0\\mathrel{\\underset{1}{\\smile}}a''$ ?",
      "Je suppose désormais que",
      "Je fais l'hypothése suivante",
      "(sous réserve que l'hypothése est vraie)",
      "C'est peut-être interessant"
    ],
    "title_date_page_counts": "No title, date or manuscript page numeral supplied. Bottom-left archive numeral 7 is retained only in a comment.",
    "hand_attribution": "Main dark hand follows packet attribution as another unnamed hand; identity was not independently established. Pale additions and the detached stroke use undetermined hand.",
    "mathematics_led_reading_decisions": "No mathematical calculation, proof check or correspondence was used to settle ink. Written statements and qualifications are transcribed without repair. Formula placements were inspected visually.",
    "C_doubt_map": {
      "First isolated struck line": "A02 retained",
      "Second existential line": "A05 retained",
      "Before second bowl in or a…": "A06 retained",
      "Above last two implications": "A08 retained",
      "After (1)⇒ in lower left": "A10 retained",
      "End of final line": "A13 resolved",
      "Lower line, light addition after on a": "A09 retained"
    },
    "source_section_accounting": "Six notation rows are not additional doubts. Repeated zeta/delta notation maps to A05. Final cancelled-q row is an actual doubt despite no unsure macro. Interessant and hypothése rows are slips retained, not original doubts, per section metadata supplied by root.",
    "slips_checked": [
      "Crop 05: rising acute in first hypothése retained.",
      "Crop 11: rising acute in final hypothése and réserve retained.",
      "Crop 10: no detached acute over interessant; unaccented spelling retained. Peut-être and à preserved."
    ],
    "physical_features": "Horizontal fold crosses between existential passages. Bracket, rules, cancellations, additions, return arrow and archive numeral are recorded. No supported character was recovered from the small irregular dark area at extreme upper right.",
    "view_attestation": {
      "whole_image_views": 1,
      "half_a_views": 1,
      "half_b_views": 1,
      "crop_images_created": 11,
      "crop_views": 11,
      "recrops": 0,
      "full_dimensions": [
        1404,
        1721
      ],
      "half_a_dimensions": [
        1404,
        940
      ],
      "half_b_dimensions": [
        1404,
        941
      ],
      "half_a_origin_in_full": [
        0,
        0
      ],
      "half_b_origin_in_full": [
        0,
        780
      ],
      "order": "UTC start, assigned textual packet/preamble/notation, whole once, a once, b once, eleven local crops each once. No OCR, internet, other pages/readers or delegation."
    },
    "validation": "Final TeX/report consistency checked: seven original doubt decisions, seven unsure loci, H absent throughout, all eleven crop paths exist, 41 inventory items, balanced braces and paired drawing/display environments. A pdflatex syntax attempt could not start because pdflatex.fmt is unavailable; no compilation success is claimed."
  },
  "notation": [
    {
      "location": "first expansion",
      "sign": "sum and binomial indices",
      "latex": "\\sum_{i=1}^{q-1}C_q^i a^i b'^{q-i-1}+b'^{q-1}",
      "evidence": "Dotted i at each position; q below C; both prime marks inspected on half a."
    },
    {
      "location": "coprimality expressions",
      "sign": "shallow bowl over small hooked 1",
      "latex": "\\mathrel{\\underset{1}{\\smile}}",
      "evidence": "Open bowl and separate low hooked numeral visible at each occurrence."
    },
    {
      "location": "existential lines",
      "sign": "double-stroked N with and without star",
      "latex": "\\mathbb N^*,\\mathbb N",
      "evidence": "Doubled left stroke; star after a_0,b_0 memberships, absent after Greek-letter memberships."
    },
    {
      "location": "first existential statement and repetitions",
      "sign": "gamma",
      "latex": "\\gamma",
      "evidence": "Forked top returns into narrow lower loop."
    },
    {
      "location": "second existential statement",
      "sign": "qualified zeta/delta",
      "latex": "\\unsure{\\zeta|\\delta}",
      "evidence": "Sloping top and rounded hooked lower part; A05 remains qualified."
    },
    {
      "location": "pale notes",
      "sign": "crossed divisibility bar",
      "latex": "\\nmid",
      "evidence": "Separate oblique crosses upright bar."
    },
    {
      "location": "ruled hypothesis",
      "sign": "inequality and binomial indices",
      "latex": "1\\leqslant i<q,\\ C_q^i",
      "evidence": "Lower diagonal under first comparison; dotted i; q below C."
    },
    {
      "location": "second implication endpoint",
      "sign": "cancelled comparison",
      "latex": "\\deleted{\\ne0}>0",
      "evidence": "Crop 01 supports overwritten two-bar/crossed-stem sign and oval zero; live >0 follows. Confirmation creates no invented C difference."
    },
    {
      "location": "factorization continuations",
      "sign": "double primes",
      "latex": "b'',a''",
      "evidence": "Two distinct raised strokes after each letter."
    },
    {
      "location": "two hypothése occurrences",
      "sign": "acute",
      "latex": "hypothése",
      "evidence": "Separate rising accents in crops 05 and 11."
    }
  ],
  "check_events": [],
  "brief_feedback": [
    "Original C_doubts section headers were absent; root's section-metadata clarification was applied.",
    "Final raised q alpha minus 1 is drawn physically rather than assigning an unestablished algebraic role to its placement.",
    "Detached stroke by l'ensemble supports a shape candidate; attachment to l remains uncertain."
  ]
}

## Reader B

\scanpage{8}
Supposons que $q\alpha-\alpha'\ne0$ alors
\[
\begin{aligned}
(1)\ \Longrightarrow\quad &p\mid\sum_{i=1}^{q-1}C_q^i\,a^i b'^{\,q-i-1}+b'^{\,q-1}\\
\Longrightarrow\quad &p\mid q\,a^{q-1}\qquad\text{car }p\mid b'\ \text{et pour }i\ne q-1\quad q-i-1\deleted{\ne0}>0
\end{aligned}
\]
or $p\mid b'$ et $b'\mid b^q$ donc $b'\mathrel{\underset{1}{\smile}}a$ donc $p\mathrel{\underset{1}{\smile}}a$

\deleted{donc si $\unsure{p\ne1|p\ne q}$}
\[
(1)\ \Longrightarrow\quad p\mid q\qquad\text{donc }\deleted{p=1\ \text{ou }}p=q\quad(\text{si }q\alpha-\alpha'\ne0)
\]
Donc si $p\ne q$ \quad $p$ premier \inserted{ou $p=1$} et $p\mid b'$ alors $\alpha'=q\alpha$
\begin{flushright}
\begin{tikzpicture}[baseline=(p.base)]
\node[inner sep=0pt] (p) at(0,0) {$\left(\begin{aligned}
&\text{\rlap{on l'impose sans risque}\phantom{\deleted{on l'impose sans risque}}}\\
&\quad\text{\rlap{si $p=1$}\phantom{\deleted{si $p=1$}}}
\end{aligned}\right)$};
\draw ([xshift=.05cm,yshift=-.03cm]p.south west) -- ([xshift=.08cm,yshift=.03cm]p.north);
\draw ([xshift=.22cm,yshift=-.04cm]p.south) -- ([xshift=-.04cm,yshift=.03cm]p.north east);
\end{tikzpicture}
\end{flushright}

Donc $\exists\,b_0\in\mathbb N^*$ et $\exists\,\gamma\in\mathbb N$ tel que $b'=q^\gamma b_0^q$ \margin{$q\nmid b_0$}

de plus $b_0\mid b$ et si $b=b_0 b''$ alors $b_0\mathrel{\underset{1}{\smile}}b''$ ?

De même $\exists\,a_0\in\mathbb N^*$ et $\exists\,\unsure{\zeta|\delta}\in\mathbb N$ tel que $a'=q^\zeta a_0^q$ avec $a_0\mid a$ et si $\overset{\unsure{\cdot|\prime}}{a}=a_0a''$ alors $a_0\mathrel{\underset{1}{\smile}}a''$ ?
% The small detached mark above a is positioned as seen; its role and hand remain open.

or $a\mathrel{\underset{1}{\smile}}b\Longrightarrow a_{\deleted{\unsure{0}}}'\mathrel{\underset{1}{\smile}}b'\Longrightarrow\zeta\times\gamma=0$ (et aussi $a_0\mathrel{\underset{1}{\smile}}b_0$)

Je suppose désormais que $\zeta=0$ donc $a'=a_0^q$

\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\node[anchor=west,inner sep=0pt] at(0,.75) {Donc \quad $c=b+a_0^q=a+q^\gamma b_0^q$};
\node[anchor=west,inner sep=0pt,align=left,font=\footnotesize] at(6.75,1.05) {pour $q=2$ on a, $a_0=b_0=1$,\\$\gamma=1$, $b=4$, $a=3$, $c=5$};
\draw (12.0,1.60) -- (6.65,1.63) .. controls(6.58,1.63) and(6.55,1.55) .. (6.55,1.45) -- (6.55,.08);
\draw (0,.30) .. controls(2.6,.30) and(4.8,.17) .. (6.55,.10) .. controls(8.6,-.05) and(10.6,.02) .. (12.0,-.06);
\node[anchor=west,inner sep=0pt,font=\footnotesize] at(.05,-.32) {Je fais l'hypothése suivante \quad si $q$ premier et $1\leqslant i<q$ alors $q\mid C_q^i$};
\draw (.12,-.62) .. controls(4.2,-.57) and(8.9,-.80) .. (11.95,-.84);
\end{tikzpicture}}

alors Si $q\geqslant3$ et $q\alpha-\alpha'\geqslant2$ \deleted{alors} on a \inserted{$p=q,\ {\unsure{a|\alpha}}'=\gamma$}
\[
\begin{aligned}
(1)\ \Longrightarrow\quad &\deleted{\unsure{p^{2}|p}}q^2\mid q\,a^{q-1}\quad
\begin{tikzpicture}[baseline=(d.base)]
\node[inner sep=0pt] (d) {\rlap{$\text{ou }p=1$}\phantom{$\deleted{\text{ou }p=1}$}};
\draw ([yshift=.03cm]d.west) -- ([yshift=.11cm,xshift=-.06cm]d.east)
 .. controls([xshift=.15cm,yshift=.04cm]d.east) and([xshift=.02cm,yshift=-.14cm]d.east)
 .. ([xshift=.24cm,yshift=-.10cm]d.center) -- ([xshift=-.06cm,yshift=-.06cm]d.center);
\end{tikzpicture}\\[.7ex]
\Longrightarrow\quad&q\mid a^{q-1}\quad
\begin{tikzpicture}[baseline=(d.base)]
\node[inner sep=0pt] (d) {\rlap{$\text{ou }p=1\Longrightarrow p=1$}\phantom{$\deleted{\text{ou }p=1\Longrightarrow p=1}$}};
\draw ([xshift=-.03cm,yshift=-.02cm]d.west) -- ([xshift=.05cm,yshift=.22cm]d.east);
\node[anchor=south,inner sep=0pt] at([yshift=.11cm]d.north) {$\inserted{\text{absurde car }q\nmid a}$};
\end{tikzpicture}
\end{aligned}
\]
Donc $\gamma=0$ ou $\gamma=
\begin{tikzpicture}[baseline=(q.base)]
\node[inner sep=0pt] (q) at(0,0) {\rlap{$q$}\phantom{$\deleted{q}$}};
\node[anchor=base west,inner sep=0pt] at(-.03,.38) {$q\alpha-1$};
\draw (-.16,-.02) .. controls(-.38,-.18) and(-.31,-.27) .. (-.18,-.18) -- (.30,.17)
 -- (-.24,-.34) .. controls(-.34,-.45) and(-.22,-.45) .. (.24,-.20) -- (-.03,-.47);
\end{tikzpicture}$ (sous réserve que l'hypothése est vraie)%
% The raised q alpha - 1 and the cancelled lower q are reproduced geometrically.
\margin{\begin{tikzpicture}[baseline=(n.base)]
\node[inner sep=0pt,text width=.85\marginparwidth] (n) {C'est peut-être interessant car ici $2$ est mis à part dans l'ensemble des nombres premiers};
\fill ([xshift=.07cm,yshift=-.47cm]n.south east) circle(.022cm);
\draw ([xshift=.15cm,yshift=-.47cm]n.south east) -- ([xshift=.31cm,yshift=-.47cm]n.south east)
 -- ([xshift=.35cm,yshift=-.16cm]n.north east)
 .. controls([xshift=.35cm,yshift=-.03cm]n.north east) and([xshift=.19cm,yshift=-.01cm]n.north east)
 .. ([xshift=.06cm,yshift=.01cm]n.north east);
\draw ([xshift=.19cm,yshift=.14cm]n.north east) .. controls([xshift=.00cm,yshift=.04cm]n.north east) and([xshift=-.01cm,yshift=-.06cm]n.north east) .. ([xshift=.15cm,yshift=-.10cm]n.north east);
\end{tikzpicture}}
% archive sheet number: 7



{
  "differences": [
    {
      "id": "B008_D01",
      "location": "Isolated struck line between the upper coprimality prose and the next (1)",
      "C": "\\deleted{donc si $\\unsure{p\\ne1|p\\ne q}$}",
      "H": null,
      "reading": "\\deleted{donc si $\\unsure{p\\ne1|p\\ne q}$}",
      "evidence": "The d ascender, final c, si and a descending p remain visible under the long cancellation. The final character has a right-hand upright and an upper slant favouring 1; intersecting cancellation strokes continue to obscure its head, leaving q supported as the alternative.",
      "confidence": "low",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "02_isolated_cancel.png",
      "bbox": [
        90,
        379,
        483,
        453
      ],
      "C_doubt_source": "Doubtful readings: First isolated struck line"
    },
    {
      "id": "B008_D02",
      "location": "Second existential line: letter after the second existential sign",
      "C": "\\unsure{\\zeta|\\delta}",
      "H": null,
      "reading": "\\unsure{\\zeta|\\delta}",
      "evidence": "A descending upper diagonal turns at the left into a rounded lower stroke with a closed little return. The same form is visible as the exponent in this line and in the later product and assumption. The return does not settle the supplied zeta/delta alternatives.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "04_zeta.png",
      "bbox": [
        548,
        880,
        1160,
        978
      ],
      "C_doubt_source": "Doubtful readings: Second existential line"
    },
    {
      "id": "B008_D03",
      "location": "Small cancelled subscript below a prime before the second bowl relation",
      "C": "a_{\\deleted{\\unsure{0}}}'",
      "H": null,
      "reading": "a_{\\deleted{\\unsure{0}}}'",
      "evidence": "The lowered cluster has a rounded outside edge but a substantially filled dark interior. The cancellation is clear; no open oval or alternative complete glyph can be recovered. The candidate 0 remains qualified.",
      "confidence": "low",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "06_a_subscript.png",
      "bbox": [
        403,
        1052,
        652,
        1135
      ],
      "C_doubt_source": "Doubtful readings: Before second bowl in or a…"
    },
    {
      "id": "B008_D04",
      "location": "Struck word immediately before on a below the ruled hypothesis",
      "C": "\\deleted{\\unsure{alors}}",
      "H": null,
      "reading": "\\deleted{alors}",
      "evidence": "Beneath the oblique zigzag, the initial low a, the tall l, a round o, and the final r/s strokes can be followed. The enlargement supports all five letters, with the cancellation retained.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": "resolved",
      "readers_crop": "08_lower_alors.png",
      "bbox": [
        313,
        1387,
        775,
        1455
      ],
      "C_doubt_source": "Doubtful readings: Above last two implications"
    },
    {
      "id": "B008_D05",
      "location": "Cancelled predecessor before q squared in the first lower implication",
      "C": "\\deleted{\\unsure{p^{2}|p}}",
      "H": null,
      "reading": "\\deleted{\\unsure{p^{2}|p}}",
      "evidence": "The lower portion has a p-like descending stem and right bowl. A separate raised cluster survives above it, but the original digit and the cancellation strokes cannot be disentangled. The p-squared candidate and p alternative are retained.",
      "confidence": "low",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "10_lower_p.png",
      "bbox": [
        92,
        1454,
        550,
        1535
      ],
      "C_doubt_source": "Doubtful readings: After (1)⇒ in lower left"
    },
    {
      "id": "B008_D06",
      "location": "Final equality after the second gamma equals sign",
      "C": "{\\deleted{q}}^{q\\alpha-1}",
      "H": null,
      "reading": "A cancelled lower q, crossed by a returning zigzag, with the live q alpha minus 1 drawn above; reading.tex preserves the stack in TikZ.",
      "evidence": "The lower oval and right descending q stem are separately visible beneath the crossing strokes. Above, q, alpha, a horizontal minus and 1 are all readable. The upper initial q starts almost directly above the lower q. The physical glyphs and cancellation are resolved; the drawing leaves the algebraic attachment of the raised entry unassigned.",
      "confidence": "high",
      "kind": "insertion or placement",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": "resolved",
      "readers_crop": "12_final_gamma.png",
      "bbox": [
        199,
        1579,
        735,
        1699
      ],
      "C_doubt_source": "Doubtful readings: End of final line; this is a table doubt despite the absence of an unsure macro in C.tex"
    },
    {
      "id": "B008_D07",
      "location": "Pale formula after on a below the ruled hypothesis",
      "C": "p=q,\\ {\\unsure{a|\\alpha}}'=\\gamma",
      "H": null,
      "reading": "p=q,\\ {\\unsure{a|\\alpha}}'=\\gamma",
      "evidence": "The primed letter has a small closed bowl and a short right-hand stroke. These favour a, while the pale join continues to admit alpha. p=q, its comma, the prime, equality and gamma are readable. The lower comma-like mark visible at the edge of this crop belongs to the C'est apostrophe on the following line, as its placement in the lower half shows.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "09_pale_formula.png",
      "bbox": [
        760,
        1382,
        1014,
        1457
      ],
      "C_doubt_source": "Doubtful readings: Lower line, light addition after on a"
    },
    {
      "id": "B008_D08",
      "location": "Detached mark above a in et si a=a0 a-double-prime",
      "C": "a=a_0a''",
      "H": null,
      "reading": "\\overset{\\unsure{\\cdot|\\prime}}{a}=a_0a''",
      "evidence": "A short dark upright, with a small thickening at its foot, is detached above the left/central portion of a. It survives the enlargement distinctly from the surrounding paper. A dot made with a short stroke and a prime-shaped tick are supported candidates; the mark's role and hand remain open.",
      "confidence": "low",
      "kind": "omission",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": null,
      "readers_crop": "05_a_overmark.png",
      "bbox": [
        456,
        959,
        849,
        1043
      ],
      "mathematical_consequence": "The extra mark is retained without choosing a mathematical operation or changing the base a."
    },
    {
      "id": "B008_D09",
      "location": "Two-line cancelled parenthesis after alpha-prime=q alpha",
      "C": "\\deleted{(on l'impose sans risque si $p=1$)}",
      "H": null,
      "reading": "Same words and cancellation state, arranged on two lines and crossed by two separate rising diagonal paths in TikZ.",
      "evidence": "The left diagonal runs from below the left parenthesis through si and impose. A distinct parallel diagonal runs from below the second row through risque to the top of the closing parenthesis. Both full paths are visible in the complete local crop.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": null,
      "readers_crop": "03_parenthesis_cancel.png",
      "bbox": [
        877,
        579,
        1358,
        709
      ]
    },
    {
      "id": "B008_D10",
      "location": "First lower ou p=1 cancellation",
      "C": "\\deleted{\\text{ou }p=1}",
      "H": null,
      "reading": "Same cancelled words, with the visible long crossing and its curved lower return drawn explicitly.",
      "evidence": "The stroke crosses ou and p=1, curves around the right end, then returns beneath the equality and numeral. The distinct lower return is represented in addition to the crossing.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": null,
      "readers_crop": "11_lower_cancellations.png",
      "bbox": [
        452,
        1458,
        835,
        1595
      ]
    },
    {
      "id": "B008_D11",
      "location": "Second lower cancelled continuation and pale absurde addition",
      "C": "\\deleted{\\text{ou }p=1\\Longrightarrow p=1}\\ \\inserted{\\text{absurde car }q\\nmid a}",
      "H": null,
      "reading": "The pale inserted absurde car q nondivides a is positioned above the cancelled ou p=1 implies p=1; the crossing rises to the right.",
      "evidence": "The pale phrase sits between the two implication baselines, directly above the second crossed continuation. Its q, crossed upright and final a are all visible. A single long ascending crossing traverses the old continuation.",
      "confidence": "high",
      "kind": "insertion or placement",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": null,
      "readers_crop": "11_lower_cancellations.png",
      "bbox": [
        452,
        1458,
        835,
        1595
      ]
    },
    {
      "id": "B008_D12",
      "location": "Right-hand return arrow beside the final parenthesis and note",
      "C": "Continuous TikZ return arrow from the note's south-east corner to its north-east corner; no detached point.",
      "H": null,
      "reading": "Return arrow starting below the note beside the closing final parenthesis, with a detached round point before its lower horizontal stroke and an explicit left-pointing hooked head.",
      "evidence": "The small round mark sits just to the right of the final closing parenthesis and is separated from the lower horizontal arrow segment by a visible gap. The shaft rises on the far right and turns left into two curved head strokes. The dot is reproduced graphically, without a punctuation assignment.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": null,
      "readers_crop": "14_right_note.png",
      "bbox": [
        840,
        1446,
        1374,
        1646
      ]
    }
  ],
  "doubts": [
    {
      "location": "Isolated struck donc si line",
      "reading": "p non-equals 1",
      "alternatives": [
        "p non-equals q"
      ],
      "confidence": "low",
      "reason": "The final character is crossed through its head; the final upright supports 1 most strongly.",
      "crop": "02_isolated_cancel.png"
    },
    {
      "location": "Second existential letter",
      "reading": "zeta",
      "alternatives": [
        "delta"
      ],
      "confidence": "medium",
      "reason": "Angled top and closed lower return admit both supplied candidates.",
      "crop": "04_zeta.png"
    },
    {
      "location": "Cancelled subscript below a-prime",
      "reading": "0",
      "alternatives": [],
      "confidence": "low",
      "reason": "Rounded blacked-out patch; no further recoverable mathematical glyph.",
      "crop": "06_a_subscript.png"
    },
    {
      "location": "Cancelled predecessor before lower q squared",
      "reading": "p squared",
      "alternatives": [
        "p"
      ],
      "confidence": "low",
      "reason": "Raised cluster survives but its original numeral is inseparable from crossing strokes.",
      "crop": "10_lower_p.png"
    },
    {
      "location": "Pale primed letter after p=q",
      "reading": "a prime",
      "alternatives": [
        "alpha prime"
      ],
      "confidence": "medium",
      "reason": "Small closed body and short right-hand stroke remain insufficiently distinct.",
      "crop": "09_pale_formula.png"
    },
    {
      "location": "Detached mark above a in et si a=a0 a-double-prime",
      "reading": "short upright dot",
      "alternatives": [
        "prime-shaped tick"
      ],
      "confidence": "low",
      "reason": "The mark is visible but its glyph identity, hand and role remain unsettled.",
      "crop": "05_a_overmark.png"
    }
  ],
  "notes": {
    "page_content": "Handwritten divisibility calculations, two factorization passages with question marks, a numerical q=2 example, a sentence between rules labelled an hypothesis by the writer, corrected lower implications, and a concluding right-hand comment. All are transcribed as visible.",
    "author_uncertainty": [
      "A question mark follows each of the two coprimality questions: b0 with b-double-prime, and a0 with a-double-prime.",
      "The writer says “Je suppose désormais que” before zeta=0.",
      "The ruled sentence begins “Je fais l’hypothése suivante”.",
      "The last parenthesis reads “sous réserve que l’hypothése est vraie”.",
      "The right note begins “C’est peut-être interessant”."
    ],
    "title_date_page_numbers": "No title or date is visible. The lower-left archive numeral is 7 and is recorded only as the required comment. The scan marker is 8. H is an empty file and metadata says nothing.",
    "C_doubt_accounting": "Seven actual rows under the source heading Doubtful readings are mapped individually in B008_D01–D07. D04 and D06 are resolved; the other five are retained. The six notation rows and the two Slips retained rows are recorded as notation/audit material, without invented C-doubt statuses.",
    "mathematics_led_reading_decisions": "No formula was repaired. The final lower q and raised q alpha minus 1 are drawn with their actual relative placement; the algebraic attachment of the raised text is left unassigned. The added mark above a likewise receives no algebraic role. One arithmetic substitution check of the written numerical example was performed and is recorded below; no general proof check was performed.",
    "physical_details": "The example has an open right edge; its bottom is continuous with the upper hypothesis rule. The cancelled parenthesis has two distinct diagonal strokes. The first lower ou p=1 cancellation returns beneath the words. The pale absurde phrase is above the second cancelled continuation. The final return arrow has a detached round point beside its lower start.",
    "crop_boundary_disclosure": "All target loci and their relevant cancellation extents are included. Crop 14 begins within the high apostrophe of C’est and clips part of that already-read contextual stroke; its full reading was available on half b and the overlapping lower edge of crop 09. The target interesting spelling and the complete return arrow are included. No crop was repeated or enlarged a second time.",
    "inspection_limit": "A few pale interior specks within the cancelled parenthesis do not support a further character reading. The mottled upper-right trace was inspected in crop 15; its irregular dispersed dark patches and pale central region supply no coherent glyph candidate. No character has been supplied for these areas.",
    "technical_validation": "A LuaLaTeX compilation attempt stopped before processing reading.tex because the runtime has no lualatex.fmt. No successful compilation or rendered-page validation is claimed; the source and report received a consistency check."
  },
  "notation": [
    {
      "location": "Upper implications and both coprimality passages",
      "sign": "shallow bowl with separately lowered hooked 1",
      "latex": "\\mathrel{\\underset{1}{\\smile}}"
    },
    {
      "location": "First expansion",
      "sign": "capital C with raised dotted i and lowered q; matching dotted i in sum and exponents",
      "latex": "C_q^i,\\ \\sum_{i=1}^{q-1},\\ a^i,\\ b'^{\\,q-i-1}"
    },
    {
      "location": "First existential line and numerical example",
      "sign": "forked gamma with rounded lower loop",
      "latex": "\\gamma"
    },
    {
      "location": "Both existential lines",
      "sign": "doubled N and raised star where present; lowered small zero",
      "latex": "\\mathbb N^*,\\ \\mathbb N,\\ a_0,\\ b_0"
    },
    {
      "location": "End of upper second implication, crop 01",
      "sign": "cancelled nonzero followed by a live greater-than and zero; no witness change",
      "latex": "\\deleted{\\ne0}>0"
    },
    {
      "location": "Ruled hypothesis, crop 07",
      "sign": "rising acute stroke above the e in hypothése",
      "latex": "hypothése"
    },
    {
      "location": "Final parenthesis, crop 13",
      "sign": "rising acute stroke above the e in hypothése; closing round parenthesis",
      "latex": "hypothése"
    },
    {
      "location": "Right note, crop 14",
      "sign": "interessant without a discernible acute over its first e",
      "latex": "interessant"
    },
    {
      "location": "Right note and final line",
      "sign": "peut-être with lexical hyphen and circumflex; à and réserve carry their visible accents",
      "latex": "peut-être, à, réserve"
    },
    {
      "location": "Below hypothesis and in hypothesis",
      "sign": "separate lower slant on comparison signs",
      "latex": "\\geqslant,\\ \\leqslant"
    },
    {
      "location": "Pale lower correction, crop 11",
      "sign": "absurde car q crossed upright a, above the crossed old continuation",
      "latex": "\\inserted{\\text{absurde car }q\\nmid a}"
    },
    {
      "location": "Final equality, crop 12",
      "sign": "cancelled lower q and live raised q alpha minus 1, retained geometrically",
      "latex": "\\begin{tikzpicture}...\\end{tikzpicture}"
    },
    {
      "location": "Lower start of return arrow, crops 13–14",
      "sign": "detached round point aligned with the initial horizontal stroke; no punctuation role assigned",
      "latex": "\\fill ... circle(.022cm);"
    }
  ],
  "check_events": [
    {
      "statement": "The numerical example q=2, a0=b0=1, gamma=1, b=4, a=3, c=5 beside c=b+a0^q=a+q^gamma b0^q",
      "location": "Right of the Donc c equality, full scan approximately [792,1205,1376,1346]",
      "type": "exact arithmetic substitution",
      "result": "Using precisely the written assignments, 4+1^2=5 and 3+2^1*1^2=5; both expressions equal the written c=5. This local computation supplies no repair or proof of the surrounding assertions."
    }
  ],
  "brief_feedback": [
    "The supplied C_doubts.txt excerpt omits source-section headings. The parent clarified the seven actual Doubtful readings rows and the two Slips retained rows; this report records that mapping explicitly.",
    "A known upper/lower arrangement can remain algebraically unassigned. For the final q stack, explicit TikZ preserves the ink without forcing an exponent/replacement interpretation."
  ]
}

## Reader C

\scanpage{8}
Supposons que $q\alpha-\alpha'\ne0$ alors
\[
\begin{aligned}
(1)\ \Longrightarrow\quad &p\mid\sum_{i=1}^{q-1}C_q^i\,a^i b'^{\,q-i-1}+b'^{\,q-1}\\
\Longrightarrow\quad &p\mid q\,a^{q-1}\qquad\text{car }p\mid b'\ \text{et pour }i\ne q-1\quad q-i-1\deleted{\ne0}>0
\end{aligned}
\]
or $p\mid b'$ et $b'\mid b^q$ donc $b'\mathrel{\underset{1}{\smile}}a$ donc $p\mathrel{\underset{1}{\smile}}a$

\deleted{donc si $\unsure{p\ne1|p\ne q}$}
\[
(1)\ \Longrightarrow\quad p\mid q\qquad\text{donc }\deleted{p=1\ \text{ou }}p=q\quad(\text{si }q\alpha-\alpha'\ne0)
\]
Donc si $p\ne q$ \quad $p$ premier \inserted{ou $p=1$} et $p\mid b'$ alors $\alpha'=q\alpha$
% The parenthetical cancellation has two distinct oblique strokes.
\begin{tikzpicture}[baseline=(n.north)]
\node[inner sep=0pt,align=left] (n) {\rlap{\begin{tabular}{@{}l@{}}(on l'impose sans risque\\\quad si $p=1$)\end{tabular}}\phantom{\begin{tabular}{@{}l@{}}\deleted{(on l'impose sans risque}\\\quad\deleted{si $p=1$)}\end{tabular}}};
\draw[line width=.45pt] ([xshift=.12cm,yshift=-.03cm]n.south west) -- ([xshift=2.65cm,yshift=-.04cm]n.north west);
\draw[line width=.45pt] ([xshift=2.35cm,yshift=-.03cm]n.south west) -- ([xshift=-.18cm,yshift=-.04cm]n.north east);
\end{tikzpicture}

Donc $\exists\,b_0\in\mathbb N^*$ et $\exists\,\gamma\in\mathbb N$ tel que $b'=q^\gamma b_0^q$ \margin{$q\nmid b_0$}

de plus $b_0\mid b$ et si $b=b_0 b''$ alors $b_0\mathrel{\underset{1}{\smile}}b''$ ?

De même $\exists\,a_0\in\mathbb N^*$ et $\exists\,\unsure{\zeta|\delta}\in\mathbb N$ tel que $a'=q^\zeta a_0^q$ avec $a_0\mid a$ et si $a=a_0a''$ alors $a_0\mathrel{\underset{1}{\smile}}a''$ ?

or $a\mathrel{\underset{1}{\smile}}b\Longrightarrow a_{\deleted{\unsure{0}}}'\mathrel{\underset{1}{\smile}}b'\Longrightarrow\zeta\times\gamma=0$ (et aussi $a_0\mathrel{\underset{1}{\smile}}b_0$)

Je suppose désormais que $\zeta=0$ donc $a'=a_0^q$

Donc \quad $c=b+a_0^q=a+q^\gamma b_0^q$
\margin{\begin{tikzpicture}[baseline=(n.base)]
\node[inner sep=2pt,text width=.85\marginparwidth] (n) {pour $q=2$ on a, $a_0=b_0=1$, $\gamma=1$, $b=4$, $a=3$, $c=5$};
\draw (n.north east) -- (n.north west) -- (n.south west) -- (n.south east);
\end{tikzpicture}}

\noindent\rule{\linewidth}{.35pt}\par
Je fais l'hypothése suivante \quad si $q$ premier et $1\leqslant i<q$ alors $q\mid C_q^i$
\par\noindent\rule{\linewidth}{.35pt}\par
alors Si $q\geqslant3$ et $q\alpha-\alpha'\geqslant2$ \deleted{\unsure{alors}} on a
% Two separate curved marks follow the pale p=q. The lower one's role is unresolved.
\inserted{$p=q\,\underset{\hspace{.2em}\unsure{,}}{,}\ {\unsure{a|\alpha}}'=\gamma$}
\[
\begin{aligned}
(1)\ \Longrightarrow\quad &\deleted{\unsure{p^{2}|p}}q^2\mid q\,a^{q-1}\quad
\text{\begin{tikzpicture}[baseline=(n.base)]
\node[inner sep=0pt] (n) {\rlap{ou $p=1$}\phantom{\deleted{ou $p=1$}}};
\draw[line width=.5pt] ([xshift=-.04cm,yshift=.02cm]n.west) -- ([xshift=.08cm,yshift=.01cm]n.east) .. controls ([xshift=.03cm,yshift=-.12cm]n.east) and ([xshift=-.3cm,yshift=-.12cm]n.east) .. ([xshift=.50cm,yshift=-.08cm]n.west);
\end{tikzpicture}}
\quad
% Faint residual strokes and points in the interline gap; no character is supplied.
\begin{tikzpicture}[baseline=-.05cm,x=1cm,y=1cm]
\draw[gray,line width=.35pt] (0,.12) .. controls (.10,.02) and (.18,-.02) .. (.31,.02);
\draw[gray,line width=.35pt] (.21,.13) -- (.27,.10);
\draw[gray,line width=.35pt] (.34,.02) .. controls (.40,.17) and (.42,.26) .. (.52,.24);
\draw[gray,line width=.35pt] (.49,.15) -- (.64,.14);
\fill[gray] (.58,.31) circle (.5pt);
\fill[gray] (.64,.04) circle (.45pt);
\fill[gray] (.69,-.02) circle (.45pt);
\end{tikzpicture}
\\
\Longrightarrow\quad&q\mid a^{q-1}\quad
\overset{\inserted{\text{absurde car }q\nmid a}}{\text{\begin{tikzpicture}[baseline=(n.base)]
\node[inner sep=0pt] (n) {\rlap{ou $p=1\Longrightarrow p=1$}\phantom{\deleted{ou $p=1\Longrightarrow p=1$}}};
\draw[line width=.6pt] ([xshift=-.05cm,yshift=-.06cm]n.west) -- ([xshift=.04cm,yshift=.12cm]n.east);
\end{tikzpicture}}}
\end{aligned}
\]
Donc $\gamma=0$ ou $\gamma=
% Cancelled q, raised q alpha minus one, and repeated oblique return strokes.
\begin{tikzpicture}[baseline=(q.base),x=1ex,y=1ex]
\node[inner sep=0pt] (q) at (0,0) {\rlap{$q$}\phantom{\deleted{$q$}}};
\node[inner sep=0pt,anchor=south west] at (.15,.75) {$\scriptstyle q\alpha-1$};
\draw[gray,line width=.45pt] (-.55,-.05) .. controls (-.77,-.29) and (-.90,-.39) .. (-.70,-.35) -- (.95,.82) -- (-.77,-.63) .. controls (-.90,-.81) and (-.87,-.90) .. (-.70,-.86) -- (.65,.12);
\draw[gray,line width=.45pt] (.40,-.56) .. controls (-.10,-.95) and (-.35,-1.16) .. (-.34,-1.43) .. controls (-.35,-1.53) and (-.31,-1.57) .. (-.25,-1.60);
\end{tikzpicture}$ (sous réserve que l'hypothése est vraie)%
\margin{\begin{tikzpicture}[baseline=(n.base)]
\node[inner sep=0pt,text width=.85\marginparwidth] (n) {C'est peut-être interessant car ici $2$ est mis à part dans l'ensemble des nombres premiers};
% A small detached point is visible at the lower start of the return arrow.
\fill (n.south east) circle (.45pt);
\draw[->] ([xshift=.07cm]n.south east) -- ([xshift=.16cm]n.south east) |- (n.north east);
\end{tikzpicture}}
% archive sheet number: 7



{
  "differences": [
    {
      "id": "008-C-01",
      "location": "Upper isolated cancelled line",
      "C": "\\deleted{donc si $\\unsure{p\\ne1|p\\ne q}$}",
      "H": null,
      "reading": "\\deleted{donc si $\\unsure{p\\ne1|p\\ne q}$}",
      "evidence": "The initial d, the dotted i, a descending p and crossed relation survive. The rightmost narrow upright with an upper turn supports 1; several oblique cancellation strokes prevent a secure exclusion of the q candidate.",
      "confidence": "low",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "02_struck_donc_si.png",
      "bbox": [
        94,
        375,
        483,
        455
      ]
    },
    {
      "id": "008-C-02",
      "location": "Second existential line, after the second existential sign",
      "C": "\\unsure{\\zeta|\\delta}",
      "H": null,
      "reading": "\\unsure{\\zeta|\\delta}",
      "evidence": "An upper slant turns left into a waist, followed by a rounded lower return. The raised recurrence in the same crop has the same form. Zeta remains the leading candidate; the strokes do not settle the letter identity against delta.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "03_zeta_forms.png",
      "bbox": [
        548,
        879,
        1167,
        981
      ]
    },
    {
      "id": "008-C-03",
      "location": "Coprimality chain, small lower-right patch under a prime",
      "C": "a_{\\deleted{\\unsure{0}}}'",
      "H": null,
      "reading": "a_{\\deleted{\\unsure{0}}}'",
      "evidence": "A compact, substantially black patch sits below and right of a, beneath the independent prime. Its rounded outer edge supports a cancelled 0, but the internal strokes are obscured. No alternative mathematical symbol is established.",
      "confidence": "low",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "04_cancelled_subscript.png",
      "bbox": [
        449,
        1044,
        723,
        1139
      ]
    },
    {
      "id": "008-C-04",
      "location": "Below ruled hypothesis, cancellation before on a",
      "C": "\\deleted{\\unsure{alors}}",
      "H": null,
      "reading": "\\deleted{\\unsure{alors}}",
      "evidence": "A tall l-like upright and adjoining rounded strokes survive beneath several oblique crossings. The whole word remains compatible with alors, but the initial and final letters cannot be isolated securely.",
      "confidence": "low",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "05_lower_alors_and_pale.png",
      "bbox": [
        545,
        1378,
        1005,
        1467
      ]
    },
    {
      "id": "008-C-05",
      "location": "First lower implication, cancelled item before q squared",
      "C": "\\deleted{\\unsure{p^{2}|p}}",
      "H": null,
      "reading": "\\deleted{\\unsure{p^{2}|p}}",
      "evidence": "The lower cluster has a descending stem and right-hand bowl; a second compact cluster stands above it. A separate 2 cannot be read securely through the cancellation. Both supplied readings remain supported.",
      "confidence": "low",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "06_cancelled_p_power.png",
      "bbox": [
        98,
        1446,
        551,
        1540
      ]
    },
    {
      "id": "008-C-06",
      "location": "Final equality, cancelled q and raised q alpha minus one",
      "C": "{\\deleted{q}}^{q\\alpha-1}",
      "H": null,
      "reading": "{\\deleted{q}}^{q\\alpha-1} (glyph and raised placement retained; explicit cancellation drawing in reading.tex)",
      "evidence": "The lower glyph retains a rounded q body and long descending stem. Above and to its right, q, alpha, minus and 1 remain separately visible and uncrossed. This resolves the actual C doubt-table locus even though C.tex did not carry an unsure macro there. No algebraic interpretation or writing chronology is inferred.",
      "confidence": "high",
      "kind": "other",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": "resolved",
      "readers_crop": "08_final_cancelled_q.png",
      "bbox": [
        518,
        1576,
        733,
        1699
      ]
    },
    {
      "id": "008-C-07",
      "location": "Pale addition after on a, letter carrying the prime",
      "C": "{\\unsure{a|\\alpha}}'=\\gamma",
      "H": null,
      "reading": "{\\unsure{a|\\alpha}}'=\\gamma",
      "evidence": "The pale letter has a small oval body and an upper-right turn, with a separate raised prime. The local small shape supports a as first candidate; the upper-right turn also admits alpha. The mathematical context has not been used to choose between them.",
      "confidence": "medium",
      "kind": "other",
      "diff_C": false,
      "diff_H": false,
      "C_doubt_status": "retained",
      "readers_crop": "05_lower_alors_and_pale.png",
      "bbox": [
        545,
        1378,
        1005,
        1467
      ]
    },
    {
      "id": "008-C-08",
      "location": "Pale addition, immediately after p=q",
      "C": "p=q,",
      "H": null,
      "reading": "p=q\\,\\underset{\\hspace{.2em}\\unsure{,}}{,}",
      "evidence": "Two separate curved strokes are visible after q, the second lower and slightly to the right. C records one comma. The proposed reading preserves the additional comma-shaped mark without assigning it a mathematical role; the pair may be punctuation treated jointly, but its intended role and hand remain unresolved.",
      "confidence": "low",
      "kind": "omission",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": null,
      "readers_crop": "05_lower_alors_and_pale.png",
      "bbox": [
        859,
        1408,
        891,
        1466
      ]
    },
    {
      "id": "008-C-09",
      "location": "Cancelled parenthesis below alpha prime equals q alpha",
      "C": "\\deleted{(on l'impose sans risque si $p=1$)}",
      "H": null,
      "reading": "Same deleted wording, in two visible lines, crossed by two distinct ascending-right strokes in TikZ",
      "evidence": "Half a shows one oblique stroke through the left portion and another through the right portion of the two-line parenthesis. The words and cancellation state are retained; the two separate physical strokes are now drawn.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": null,
      "readers_crop": null,
      "bbox": {
        "image": "a",
        "origin": "top-left of supplied half a",
        "xyxy": [
          887,
          588,
          1348,
          705
        ]
      }
    },
    {
      "id": "008-C-10",
      "location": "First lower implication, cancelled ou p=1",
      "C": "\\deleted{\\text{ou }p=1}",
      "H": null,
      "reading": "Same deleted text with a long crossing stroke and lower returning stroke",
      "evidence": "Crop 07 shows a long stroke through ou p=1 and a distinct lower return under the latter part. The proposed drawing preserves both rather than adding a second generic strike over the words. Cancellation state and text are unchanged.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": null,
      "readers_crop": "07_lower_cancellations.png",
      "bbox": [
        561,
        1468,
        709,
        1523
      ]
    },
    {
      "id": "008-C-11",
      "location": "Second lower implication, pale absurde car q nondivides a",
      "C": "\\deleted{\\text{ou }p=1\\Longrightarrow p=1}\\ \\inserted{\\text{absurde car }q\\nmid a}",
      "H": null,
      "reading": "\\overset{\\inserted{\\text{absurde car }q\\nmid a}}{\\text{cancelled }\\mathrm{ou}\\ p=1\\Longrightarrow p=1}",
      "evidence": "The words absurde car are above the cancelled continuation; q nondivides a stands above its right end. reading.tex puts the insertion above the cancelled span. All words and symbols agree with C.",
      "confidence": "high",
      "kind": "insertion or placement",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": null,
      "readers_crop": "07_lower_cancellations.png",
      "bbox": [
        470,
        1498,
        830,
        1588
      ]
    },
    {
      "id": "008-C-12",
      "location": "Second lower implication, cancellation across ou p=1 implies p=1",
      "C": "\\deleted{\\text{ou }p=1\\Longrightarrow p=1}",
      "H": null,
      "reading": "Same deleted span, crossed by a single long ascending-right path in TikZ",
      "evidence": "The dark cancellation begins through ou at the left and rises through the remainder of the expression, passing the upper part of the right p=1. The explicit drawing retains that direction and span; it does not assert a chronology for the pale addition.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": null,
      "readers_crop": "07_lower_cancellations.png",
      "bbox": [
        461,
        1518,
        811,
        1583
      ]
    },
    {
      "id": "008-C-13",
      "location": "Final cancelled q",
      "C": "\\deleted{q}",
      "H": null,
      "reading": "Same cancelled q with repeated oblique returns and the long lower hook drawn explicitly",
      "evidence": "Crop 08 shows repeated diagonal sweeps returning across the q, with a final trace extending below its descender and turning at the bottom. Those visible paths are retained around the readable q and below the unchanged raised entry.",
      "confidence": "high",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": null,
      "readers_crop": "08_final_cancelled_q.png",
      "bbox": [
        604,
        1613,
        669,
        1690
      ]
    },
    {
      "id": "008-C-14",
      "location": "Faint interline area to right of the first lower cancelled ending",
      "C": null,
      "H": null,
      "reading": "Small gray drawing of residual curved strokes and detached points, without a supplied character",
      "evidence": "Crop 07 contains a pale curved residual line, short strokes, and several darker points in the gap above q nondivides a. Their source, hand, and former textual identity are unresolved. The drawing is an approximation of the visible traces; no word, symbol, or cancellation target has been reconstructed.",
      "confidence": "low",
      "kind": "omission",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": null,
      "readers_crop": "07_lower_cancellations.png",
      "bbox": [
        748,
        1458,
        832,
        1503
      ]
    },
    {
      "id": "008-C-15",
      "location": "Return arrow from final parenthesis to lower-right note",
      "C": "\\draw[->] (n.south east) -- ++(.16,0) |- (n.north east);",
      "H": null,
      "reading": "Same returning arrow, with a small detached point at its lower start",
      "evidence": "The lower start near the closing parenthesis has a small detached dark point, then a short line leading to the right-hand return. Crop 10 catches the point; the complete arrow and its upper left-pointing end were read on half b.",
      "confidence": "medium",
      "kind": "drawing or diagram",
      "diff_C": true,
      "diff_H": false,
      "C_doubt_status": null,
      "readers_crop": "10_final_hypothese.png",
      "bbox": {
        "image": "b",
        "origin": "top-left of supplied half b",
        "xyxy": [
          1327,
          685,
          1372,
          865
        ]
      }
    }
  ],
  "doubts": [
    {
      "location": "Upper isolated cancelled line",
      "reading": "\\deleted{donc si $\\unsure{p\\ne1|p\\ne q}$}",
      "alternatives": [
        "p\\ne q"
      ],
      "confidence": "low",
      "reason": "The initial d, the dotted i, a descending p and crossed relation survive. The rightmost narrow upright with an upper turn supports 1; several oblique cancellation strokes prevent a secure exclusion of the q candidate.",
      "crop": "02_struck_donc_si.png"
    },
    {
      "location": "Second existential line, after the second existential sign",
      "reading": "\\unsure{\\zeta|\\delta}",
      "alternatives": [
        "\\delta"
      ],
      "confidence": "medium",
      "reason": "An upper slant turns left into a waist, followed by a rounded lower return. The raised recurrence in the same crop has the same form. Zeta remains the leading candidate; the strokes do not settle the letter identity against delta.",
      "crop": "03_zeta_forms.png"
    },
    {
      "location": "Coprimality chain, small lower-right patch under a prime",
      "reading": "a_{\\deleted{\\unsure{0}}}'",
      "alternatives": [],
      "confidence": "low",
      "reason": "A compact, substantially black patch sits below and right of a, beneath the independent prime. Its rounded outer edge supports a cancelled 0, but the internal strokes are obscured. No alternative mathematical symbol is established.",
      "crop": "04_cancelled_subscript.png"
    },
    {
      "location": "Below ruled hypothesis, cancellation before on a",
      "reading": "\\deleted{\\unsure{alors}}",
      "alternatives": [],
      "confidence": "low",
      "reason": "A tall l-like upright and adjoining rounded strokes survive beneath several oblique crossings. The whole word remains compatible with alors, but the initial and final letters cannot be isolated securely.",
      "crop": "05_lower_alors_and_pale.png"
    },
    {
      "location": "First lower implication, cancelled item before q squared",
      "reading": "\\deleted{\\unsure{p^{2}|p}}",
      "alternatives": [
        "p"
      ],
      "confidence": "low",
      "reason": "The lower cluster has a descending stem and right-hand bowl; a second compact cluster stands above it. A separate 2 cannot be read securely through the cancellation. Both supplied readings remain supported.",
      "crop": "06_cancelled_p_power.png"
    },
    {
      "location": "Pale addition after on a, letter carrying the prime",
      "reading": "{\\unsure{a|\\alpha}}'=\\gamma",
      "alternatives": [
        "\\alpha"
      ],
      "confidence": "medium",
      "reason": "The pale letter has a small oval body and an upper-right turn, with a separate raised prime. The local small shape supports a as first candidate; the upper-right turn also admits alpha. The mathematical context has not been used to choose between them.",
      "crop": "05_lower_alors_and_pale.png"
    },
    {
      "location": "Pale addition, immediately after p=q",
      "reading": "p=q\\,\\underset{\\hspace{.2em}\\unsure{,}}{,}",
      "alternatives": [
        "The pair may have one punctuation function; no such function is assigned."
      ],
      "confidence": "low",
      "reason": "Two separate curved strokes are visible after q, the second lower and slightly to the right. C records one comma. The proposed reading preserves the additional comma-shaped mark without assigning it a mathematical role; the pair may be punctuation treated jointly, but its intended role and hand remain unresolved.",
      "crop": "05_lower_alors_and_pale.png"
    },
    {
      "location": "Faint interline area to right of the first lower cancelled ending",
      "reading": "Small gray drawing of residual curved strokes and detached points, without a supplied character",
      "alternatives": [],
      "confidence": "low",
      "reason": "Crop 07 contains a pale curved residual line, short strokes, and several darker points in the gap above q nondivides a. Their source, hand, and former textual identity are unresolved. The drawing is an approximation of the visible traces; no word, symbol, or cancellation target has been reconstructed.",
      "crop": "07_lower_cancellations.png"
    }
  ],
  "notes": {
    "page_content": "Handwritten divisibility calculations, two existential decompositions, coprimality expressions, the stated assumption zeta=0, a q=2 numerical example, a ruled hypothesis, lower implications, and a lower-right note. These statements were transcribed, not checked as mathematical claims.",
    "authors_own_uncertainty": [
      "? after b0 bowl-1 b double prime",
      "? after a0 bowl-1 a double prime",
      "Je fais l'hypothése suivante",
      "(sous réserve que l'hypothése est vraie)",
      "C'est peut-être interessant car ici 2 est mis à part dans l'ensemble des nombres premiers"
    ],
    "title_date_page_counts": "No separate title or date is written. The lower-left pencilled archive numeral is 7, recorded only as an archive comment. No manuscript page-number macro is supplied.",
    "mathematics_led_reading_decisions": [],
    "physical_features": "Horizontal paper fold, upper-right damage/puncture, and image border were observed as substrate features. Written rules, three-sided example frame, all recorded cancellations, pale additions, return arrow and detached point are represented. The faint interline residue is drawn without an assigned character or mathematical role.",
    "slips_checked": [
      {
        "reading": "interessant",
        "location": "Lower-right note, first line",
        "evidence": "Half b shows the dotted i and no detached acute above the first e. C spelling retained.",
        "C_doubt_status": null
      },
      {
        "reading": "hypothése",
        "location": "Ruled hypothesis",
        "evidence": "Crop 09 shows a rising acute over e. C spelling retained.",
        "C_doubt_status": null
      },
      {
        "reading": "hypothése",
        "location": "Final parenthesis",
        "evidence": "Crop 10 independently shows a rising acute over e. C spelling retained.",
        "C_doubt_status": null
      }
    ],
    "additional_loci_resolved_without_witness_change": [
      {
        "location": "Upper q-i-1 followed by cancelled nonzero and >0",
        "crop": "01_top_cancelled_neq0.png",
        "result": "The two bars/crossing of the cancelled nonzero sign and its rounded zero remain sufficiently visible; retained C reading."
      },
      {
        "location": "Lower pair of cancelled endings and pale absurde car q nondivides a",
        "crop": "07_lower_cancellations.png",
        "result": "All supplied words and symbols retained; geometry and placement recorded separately."
      }
    ],
    "H_status": "metadata hua_has=nothing; H.tex is empty (0 bytes). Every H field is null and every diff_H is false.",
    "transcription_source_validation": "The current reading.tex and report decisions were read together. A control-character typo was repaired. Braces, dollar delimiters, TikZ environment counts, crop references, seven C-doubt mappings, and H-null fields passed structural checks. A pdfLaTeX syntax compile was attempted, but the environment lacked pdflatex.fmt, so no rendering validation was completed."
  },
  "notation": [
    {
      "location": "Upper and middle coprimality relations",
      "sign": "Shallow bowl with separate small upright 1 beneath",
      "latex": "\\mathrel{\\underset{1}{\\smile}}"
    },
    {
      "location": "All divisibility lines; two pale nondivisibility additions",
      "sign": "Upright bar, or upright crossed by short oblique stroke",
      "latex": "\\mid,\\nmid"
    },
    {
      "location": "First expansion and ruled hypothesis",
      "sign": "Capital C, lowered q, raised dotted i",
      "latex": "C_q^i"
    },
    {
      "location": "First sum",
      "sign": "Lower i=1 and upper q-1; dotted i in a exponent and b exponent",
      "latex": "\\sum_{i=1}^{q-1}C_q^i a^i b\\prime^{q-i-1}"
    },
    {
      "location": "First existential line and repeated gamma signs",
      "sign": "Forked upper strokes with a lower loop",
      "latex": "\\gamma"
    },
    {
      "location": "Second existential line and its later recurrences",
      "sign": "Upper slant, left waist and rounded lower hook; identity remains qualified",
      "latex": "\\unsure{\\zeta|\\delta}"
    },
    {
      "location": "Both existential lines",
      "sign": "Double-stroked N with separate raised star where present",
      "latex": "\\mathbb N,\\mathbb N^*"
    },
    {
      "location": "Coprimality questions",
      "sign": "Two separate upper ticks on double-prime letters; small lower ovals as zeros",
      "latex": "a_0,b_0,a\\prime\\prime,b\\prime\\prime"
    },
    {
      "location": "Ruled hypothesis and lower condition",
      "sign": "Comparison with separate lower stroke",
      "latex": "\\leqslant,\\geqslant"
    },
    {
      "location": "Final equality",
      "sign": "Cancelled lower q with uncrossed q alpha minus one raised to its right",
      "latex": "{\\deleted{q}}^{q\\alpha-1}"
    },
    {
      "location": "Pale p=q addition",
      "sign": "Two comma-shaped strokes, lower stroke slightly right; role unresolved",
      "latex": "\\underset{\\hspace{.2em}\\unsure{,}}{,}"
    }
  ],
  "check_events": [],
  "brief_feedback": [
    "The additional lower curved stroke after pale p=q may belong to a compound punctuation sign or be an independent mark. I preserved the visible comma-shaped candidate with unresolved role and hand.",
    "Faint residual strokes in the lower interline gap support a small drawing but no character. Their source and cancellation target are unestablished.",
    "The final cancelled-q locus is an actual doubt-table row although C.tex has no unsure macro; its resolution is therefore explicitly counted."
  ]
}

--- A
+++ B
@@ -3,7 +3,7 @@
 \[
 \begin{aligned}
 (1)\ \Longrightarrow\quad &p\mid\sum_{i=1}^{q-1}C_q^i\,a^i b'^{\,q-i-1}+b'^{\,q-1}\\
-\Longrightarrow\quad &p\mid q\,a^{q-1}\qquad\text{Car }p\mid b'\ \text{et pour }i\ne q-1\quad q-i-1\deleted{\ne0}>0
+\Longrightarrow\quad &p\mid q\,a^{q-1}\qquad\text{car }p\mid b'\ \text{et pour }i\ne q-1\quad q-i-1\deleted{\ne0}>0
 \end{aligned}
 \]
 or $p\mid b'$ et $b'\mid b^q$ donc $b'\mathrel{\underset{1}{\smile}}a$ donc $p\mathrel{\underset{1}{\smile}}a$
@@ -12,98 +12,71 @@
 \[
 (1)\ \Longrightarrow\quad p\mid q\qquad\text{donc }\deleted{p=1\ \text{ou }}p=q\quad(\text{si }q\alpha-\alpha'\ne0)
 \]
-Donc si $p\ne q$ \quad
+Donc si $p\ne q$ \quad $p$ premier \inserted{ou $p=1$} et $p\mid b'$ alors $\alpha'=q\alpha$
+\begin{flushright}
 \begin{tikzpicture}[baseline=(p.base)]
-\node[inner sep=0pt] (p) at (0,0) {$p$ premier};
-\node[inner sep=0pt,anchor=north] at (0,-.28) {\inserted{ou $p=1$}};
-% Small dark triangular mark above the addition; its guiding function is uncertain.
-\fill (-.32,-.20) -- (-.16,-.15) -- (-.16,-.25) -- cycle;
+\node[inner sep=0pt] (p) at(0,0) {$\left(\begin{aligned}
+&\text{\rlap{on l'impose sans risque}\phantom{\deleted{on l'impose sans risque}}}\\
+&\quad\text{\rlap{si $p=1$}\phantom{\deleted{si $p=1$}}}
+\end{aligned}\right)$};
+\draw ([xshift=.05cm,yshift=-.03cm]p.south west) -- ([xshift=.08cm,yshift=.03cm]p.north);
+\draw ([xshift=.22cm,yshift=-.04cm]p.south) -- ([xshift=-.04cm,yshift=.03cm]p.north east);
 \end{tikzpicture}
-et $p\mid b'$ alors $\alpha'=q\alpha$
-\begin{tikzpicture}[baseline=(u.base)]
-\node[inner sep=0pt,anchor=west] (u) at (.22,0)
- {\rlap{on l'impose sans risque}\phantom{\deleted{on l'impose sans risque}}};
-\node[inner sep=0pt,anchor=west] (v) at (.72,-.42)
- {\rlap{si $p=1$}\phantom{\deleted{si $p=1$}}};
-\node[inner sep=0pt] at (0,-.20)
- {\rlap{$\Bigg($}\phantom{\deleted{$\Bigg($}}};
-\node[inner sep=0pt] at (5.2,-.20)
- {\rlap{$\Bigg)$}\phantom{\deleted{$\Bigg)$}}};
-% Two separate oblique cancellations over the two-line parenthesis.
-\draw[line width=.45pt] (.06,-.62) -- (2.48,.16);
-\draw[line width=.45pt] (2.45,-.62) -- (5.13,.16);
-\end{tikzpicture}
+\end{flushright}
 
 Donc $\exists\,b_0\in\mathbb N^*$ et $\exists\,\gamma\in\mathbb N$ tel que $b'=q^\gamma b_0^q$ \margin{$q\nmid b_0$}
 
 de plus $b_0\mid b$ et si $b=b_0 b''$ alors $b_0\mathrel{\underset{1}{\smile}}b''$ ?
 
-De même $\exists\,a_0\in\mathbb N^*$ et $\exists\,\unsure{\zeta|\delta}\in\mathbb N$ tel que $a'=q^\zeta a_0^q$ avec $a_0\mid a$ et si $a=a_0a''$ alors $a_0\mathrel{\underset{1}{\smile}}a''$ ?
+De même $\exists\,a_0\in\mathbb N^*$ et $\exists\,\unsure{\zeta|\delta}\in\mathbb N$ tel que $a'=q^\zeta a_0^q$ avec $a_0\mid a$ et si $\overset{\unsure{\cdot|\prime}}{a}=a_0a''$ alors $a_0\mathrel{\underset{1}{\smile}}a''$ ?
+% The small detached mark above a is positioned as seen; its role and hand remain open.
 
 or $a\mathrel{\underset{1}{\smile}}b\Longrightarrow a_{\deleted{\unsure{0}}}'\mathrel{\underset{1}{\smile}}b'\Longrightarrow\zeta\times\gamma=0$ (et aussi $a_0\mathrel{\underset{1}{\smile}}b_0$)
 
 Je suppose désormais que $\zeta=0$ donc $a'=a_0^q$
 
 \figure{\begin{tikzpicture}[x=1cm,y=1cm]
-\node[anchor=west,inner sep=0pt,font=\small] at (0,.80)
- {Donc \quad $c=b+a_0^q=a+q^\gamma b_0^q$};
-\node[anchor=north west,inner sep=0pt,font=\footnotesize] at (6.68,1.43)
- {\begin{tabular}{@{}l@{}}
- pour $q=2$ on a, $a_0=b_0=1$,\\
- $\gamma=1$, $b=4$, $a=3$, $c=5$
- \end{tabular}};
-% Open right border; the left edge meets the shared long upper rule.
-\draw[line width=.35pt] (12.12,1.66) -- (6.50,1.66) -- (6.50,.03);
-\draw[line width=.35pt] (0,.22) -- (6.50,.03) -- (12.12,-.06);
-\node[anchor=west,inner sep=0pt,font=\footnotesize] at (0,-.43)
- {Je fais l'hypothése suivante};
-\node[anchor=west,inner sep=0pt,font=\footnotesize] at (5.58,-.43)
- {si $q$ premier et $1\leqslant i<q$ alors $q\mid C_q^i$};
-\draw[line width=.35pt] (0,-.83) -- (12.12,-1.08);
+\node[anchor=west,inner sep=0pt] at(0,.75) {Donc \quad $c=b+a_0^q=a+q^\gamma b_0^q$};
+\node[anchor=west,inner sep=0pt,align=left,font=\footnotesize] at(6.75,1.05) {pour $q=2$ on a, $a_0=b_0=1$,\\$\gamma=1$, $b=4$, $a=3$, $c=5$};
+\draw (12.0,1.60) -- (6.65,1.63) .. controls(6.58,1.63) and(6.55,1.55) .. (6.55,1.45) -- (6.55,.08);
+\draw (0,.30) .. controls(2.6,.30) and(4.8,.17) .. (6.55,.10) .. controls(8.6,-.05) and(10.6,.02) .. (12.0,-.06);
+\node[anchor=west,inner sep=0pt,font=\footnotesize] at(.05,-.32) {Je fais l'hypothése suivante \quad si $q$ premier et $1\leqslant i<q$ alors $q\mid C_q^i$};
+\draw (.12,-.62) .. controls(4.2,-.57) and(8.9,-.80) .. (11.95,-.84);
 \end{tikzpicture}}
-alors Si $q\geqslant3$ et $q\alpha-\alpha'\geqslant2$ \deleted{\unsure{alors}} on a \inserted{$p=q,\ {\unsure{a|\alpha}}'=\gamma$}
+
+alors Si $q\geqslant3$ et $q\alpha-\alpha'\geqslant2$ \deleted{alors} on a \inserted{$p=q,\ {\unsure{a|\alpha}}'=\gamma$}
 \[
 \begin{aligned}
-(1)\ \Longrightarrow\quad
- &\deleted{\unsure{p^{2}|p}}q^2\mid q\,a^{q-1}\quad
- \begin{tikzpicture}[baseline=(d.base)]
- \node[inner sep=0pt] (d) at (0,0)
-  {\rlap{ou $p=1$}\phantom{\deleted{ou $p=1$}}};
- \draw[line width=.45pt] (d.west) -- (d.east)
-  .. controls +(0.22,-.04) and +(0.22,-.06) ..
-  ([yshift=-2pt]d.east) -- ([yshift=-2pt]d.west);
- \end{tikzpicture}\\[.8ex]
-\Longrightarrow\quad
- &q\mid a^{q-1}\quad
- \begin{tikzpicture}[baseline=(d.base)]
- \node[inner sep=0pt] (d) at (0,0)
-  {\rlap{ou $p=1\Longrightarrow p=1$}\phantom{\deleted{ou $p=1\Longrightarrow p=1$}}};
- \draw[line width=.45pt] ([xshift=-2pt,yshift=-2pt]d.west)
-  -- ([xshift=2pt,yshift=4pt]d.east);
- \node[inner sep=0pt,anchor=south] at (0,.23)
-  {\inserted{absurde car $q\nmid a$}};
- \end{tikzpicture}
+(1)\ \Longrightarrow\quad &\deleted{\unsure{p^{2}|p}}q^2\mid q\,a^{q-1}\quad
+\begin{tikzpicture}[baseline=(d.base)]
+\node[inner sep=0pt] (d) {\rlap{$\text{ou }p=1$}\phantom{$\deleted{\text{ou }p=1}$}};
+\draw ([yshift=.03cm]d.west) -- ([yshift=.11cm,xshift=-.06cm]d.east)
+ .. controls([xshift=.15cm,yshift=.04cm]d.east) and([xshift=.02cm,yshift=-.14cm]d.east)
+ .. ([xshift=.24cm,yshift=-.10cm]d.center) -- ([xshift=-.06cm,yshift=-.06cm]d.center);
+\end{tikzpicture}\\[.7ex]
+\Longrightarrow\quad&q\mid a^{q-1}\quad
+\begin{tikzpicture}[baseline=(d.base)]
+\node[inner sep=0pt] (d) {\rlap{$\text{ou }p=1\Longrightarrow p=1$}\phantom{$\deleted{\text{ou }p=1\Longrightarrow p=1}$}};
+\draw ([xshift=-.03cm,yshift=-.02cm]d.west) -- ([xshift=.05cm,yshift=.22cm]d.east);
+\node[anchor=south,inner sep=0pt] at([yshift=.11cm]d.north) {$\inserted{\text{absurde car }q\nmid a}$};
+\end{tikzpicture}
 \end{aligned}
 \]
-Donc $\gamma=0$ ou $\gamma=$
+Donc $\gamma=0$ ou $\gamma=
 \begin{tikzpicture}[baseline=(q.base)]
-\node[inner sep=0pt] (q) at (0,0)
- {$\rlap{$q$}\phantom{\deleted{q}}$};
-% The live entry is physically raised above and to the right of the cancelled q.
-\node[inner sep=0pt,anchor=south west] at (-.01,.22) {$q\alpha-1$};
-\draw[line width=.45pt] (-.20,-.02) -- (.33,.28)
- .. controls (.48,.32) and (-.26,-.17) .. (-.20,-.02);
-\draw[line width=.45pt] (-.18,-.22) -- (.30,.10)
- .. controls (.39,.16) and (-.29,-.34) .. (-.18,-.22);
-\draw[line width=.45pt] (.02,-.24) -- (-.03,-.40);
-\end{tikzpicture}
-(sous réserve que l'hypothése est vraie)%
+\node[inner sep=0pt] (q) at(0,0) {\rlap{$q$}\phantom{$\deleted{q}$}};
+\node[anchor=base west,inner sep=0pt] at(-.03,.38) {$q\alpha-1$};
+\draw (-.16,-.02) .. controls(-.38,-.18) and(-.31,-.27) .. (-.18,-.18) -- (.30,.17)
+ -- (-.24,-.34) .. controls(-.34,-.45) and(-.22,-.45) .. (.24,-.20) -- (-.03,-.47);
+\end{tikzpicture}$ (sous réserve que l'hypothése est vraie)%
+% The raised q alpha - 1 and the cancelled lower q are reproduced geometrically.
 \margin{\begin{tikzpicture}[baseline=(n.base)]
-\node[inner sep=0pt,text width=.85\marginparwidth] (n)
- {C'est peut-être interessant car ici $2$ est mis à part dans
- \(\mathord{\overset{\scriptscriptstyle\unsure{/}}{\vphantom{l}}}\)l'ensemble des nombres premiers};
-% Small detached rising stroke before l'ensemble: role and hand unresolved.
-% Return arrow rises at the right from the final parenthesis toward this note.
-\draw[->] ([yshift=-.25cm]n.south east) -- ++(.16,0) |- (n.north east);
+\node[inner sep=0pt,text width=.85\marginparwidth] (n) {C'est peut-être interessant car ici $2$ est mis à part dans l'ensemble des nombres premiers};
+\fill ([xshift=.07cm,yshift=-.47cm]n.south east) circle(.022cm);
+\draw ([xshift=.15cm,yshift=-.47cm]n.south east) -- ([xshift=.31cm,yshift=-.47cm]n.south east)
+ -- ([xshift=.35cm,yshift=-.16cm]n.north east)
+ .. controls([xshift=.35cm,yshift=-.03cm]n.north east) and([xshift=.19cm,yshift=-.01cm]n.north east)
+ .. ([xshift=.06cm,yshift=.01cm]n.north east);
+\draw ([xshift=.19cm,yshift=.14cm]n.north east) .. controls([xshift=.00cm,yshift=.04cm]n.north east) and([xshift=-.01cm,yshift=-.06cm]n.north east) .. ([xshift=.15cm,yshift=-.10cm]n.north east);
 \end{tikzpicture}}
 % archive sheet number: 7

--- A
+++ C
@@ -3,7 +3,7 @@
 \[
 \begin{aligned}
 (1)\ \Longrightarrow\quad &p\mid\sum_{i=1}^{q-1}C_q^i\,a^i b'^{\,q-i-1}+b'^{\,q-1}\\
-\Longrightarrow\quad &p\mid q\,a^{q-1}\qquad\text{Car }p\mid b'\ \text{et pour }i\ne q-1\quad q-i-1\deleted{\ne0}>0
+\Longrightarrow\quad &p\mid q\,a^{q-1}\qquad\text{car }p\mid b'\ \text{et pour }i\ne q-1\quad q-i-1\deleted{\ne0}>0
 \end{aligned}
 \]
 or $p\mid b'$ et $b'\mid b^q$ donc $b'\mathrel{\underset{1}{\smile}}a$ donc $p\mathrel{\underset{1}{\smile}}a$
@@ -12,26 +12,12 @@
 \[
 (1)\ \Longrightarrow\quad p\mid q\qquad\text{donc }\deleted{p=1\ \text{ou }}p=q\quad(\text{si }q\alpha-\alpha'\ne0)
 \]
-Donc si $p\ne q$ \quad
-\begin{tikzpicture}[baseline=(p.base)]
-\node[inner sep=0pt] (p) at (0,0) {$p$ premier};
-\node[inner sep=0pt,anchor=north] at (0,-.28) {\inserted{ou $p=1$}};
-% Small dark triangular mark above the addition; its guiding function is uncertain.
-\fill (-.32,-.20) -- (-.16,-.15) -- (-.16,-.25) -- cycle;
-\end{tikzpicture}
-et $p\mid b'$ alors $\alpha'=q\alpha$
-\begin{tikzpicture}[baseline=(u.base)]
-\node[inner sep=0pt,anchor=west] (u) at (.22,0)
- {\rlap{on l'impose sans risque}\phantom{\deleted{on l'impose sans risque}}};
-\node[inner sep=0pt,anchor=west] (v) at (.72,-.42)
- {\rlap{si $p=1$}\phantom{\deleted{si $p=1$}}};
-\node[inner sep=0pt] at (0,-.20)
- {\rlap{$\Bigg($}\phantom{\deleted{$\Bigg($}}};
-\node[inner sep=0pt] at (5.2,-.20)
- {\rlap{$\Bigg)$}\phantom{\deleted{$\Bigg)$}}};
-% Two separate oblique cancellations over the two-line parenthesis.
-\draw[line width=.45pt] (.06,-.62) -- (2.48,.16);
-\draw[line width=.45pt] (2.45,-.62) -- (5.13,.16);
+Donc si $p\ne q$ \quad $p$ premier \inserted{ou $p=1$} et $p\mid b'$ alors $\alpha'=q\alpha$
+% The parenthetical cancellation has two distinct oblique strokes.
+\begin{tikzpicture}[baseline=(n.north)]
+\node[inner sep=0pt,align=left] (n) {\rlap{\begin{tabular}{@{}l@{}}(on l'impose sans risque\\\quad si $p=1$)\end{tabular}}\phantom{\begin{tabular}{@{}l@{}}\deleted{(on l'impose sans risque}\\\quad\deleted{si $p=1$)}\end{tabular}}};
+\draw[line width=.45pt] ([xshift=.12cm,yshift=-.03cm]n.south west) -- ([xshift=2.65cm,yshift=-.04cm]n.north west);
+\draw[line width=.45pt] ([xshift=2.35cm,yshift=-.03cm]n.south west) -- ([xshift=-.18cm,yshift=-.04cm]n.north east);
 \end{tikzpicture}
 
 Donc $\exists\,b_0\in\mathbb N^*$ et $\exists\,\gamma\in\mathbb N$ tel que $b'=q^\gamma b_0^q$ \margin{$q\nmid b_0$}
@@ -44,66 +30,56 @@
 
 Je suppose désormais que $\zeta=0$ donc $a'=a_0^q$
 
-\figure{\begin{tikzpicture}[x=1cm,y=1cm]
-\node[anchor=west,inner sep=0pt,font=\small] at (0,.80)
- {Donc \quad $c=b+a_0^q=a+q^\gamma b_0^q$};
-\node[anchor=north west,inner sep=0pt,font=\footnotesize] at (6.68,1.43)
- {\begin{tabular}{@{}l@{}}
- pour $q=2$ on a, $a_0=b_0=1$,\\
- $\gamma=1$, $b=4$, $a=3$, $c=5$
- \end{tabular}};
-% Open right border; the left edge meets the shared long upper rule.
-\draw[line width=.35pt] (12.12,1.66) -- (6.50,1.66) -- (6.50,.03);
-\draw[line width=.35pt] (0,.22) -- (6.50,.03) -- (12.12,-.06);
-\node[anchor=west,inner sep=0pt,font=\footnotesize] at (0,-.43)
- {Je fais l'hypothése suivante};
-\node[anchor=west,inner sep=0pt,font=\footnotesize] at (5.58,-.43)
- {si $q$ premier et $1\leqslant i<q$ alors $q\mid C_q^i$};
-\draw[line width=.35pt] (0,-.83) -- (12.12,-1.08);
+Donc \quad $c=b+a_0^q=a+q^\gamma b_0^q$
+\margin{\begin{tikzpicture}[baseline=(n.base)]
+\node[inner sep=2pt,text width=.85\marginparwidth] (n) {pour $q=2$ on a, $a_0=b_0=1$, $\gamma=1$, $b=4$, $a=3$, $c=5$};
+\draw (n.north east) -- (n.north west) -- (n.south west) -- (n.south east);
 \end{tikzpicture}}
-alors Si $q\geqslant3$ et $q\alpha-\alpha'\geqslant2$ \deleted{\unsure{alors}} on a \inserted{$p=q,\ {\unsure{a|\alpha}}'=\gamma$}
+
+\noindent\rule{\linewidth}{.35pt}\par
+Je fais l'hypothése suivante \quad si $q$ premier et $1\leqslant i<q$ alors $q\mid C_q^i$
+\par\noindent\rule{\linewidth}{.35pt}\par
+alors Si $q\geqslant3$ et $q\alpha-\alpha'\geqslant2$ \deleted{\unsure{alors}} on a
+% Two separate curved marks follow the pale p=q. The lower one's role is unresolved.
+\inserted{$p=q\,\underset{\hspace{.2em}\unsure{,}}{,}\ {\unsure{a|\alpha}}'=\gamma$}
 \[
 \begin{aligned}
-(1)\ \Longrightarrow\quad
- &\deleted{\unsure{p^{2}|p}}q^2\mid q\,a^{q-1}\quad
- \begin{tikzpicture}[baseline=(d.base)]
- \node[inner sep=0pt] (d) at (0,0)
-  {\rlap{ou $p=1$}\phantom{\deleted{ou $p=1$}}};
- \draw[line width=.45pt] (d.west) -- (d.east)
-  .. controls +(0.22,-.04) and +(0.22,-.06) ..
-  ([yshift=-2pt]d.east) -- ([yshift=-2pt]d.west);
- \end{tikzpicture}\\[.8ex]
-\Longrightarrow\quad
- &q\mid a^{q-1}\quad
- \begin{tikzpicture}[baseline=(d.base)]
- \node[inner sep=0pt] (d) at (0,0)
-  {\rlap{ou $p=1\Longrightarrow p=1$}\phantom{\deleted{ou $p=1\Longrightarrow p=1$}}};
- \draw[line width=.45pt] ([xshift=-2pt,yshift=-2pt]d.west)
-  -- ([xshift=2pt,yshift=4pt]d.east);
- \node[inner sep=0pt,anchor=south] at (0,.23)
-  {\inserted{absurde car $q\nmid a$}};
- \end{tikzpicture}
+(1)\ \Longrightarrow\quad &\deleted{\unsure{p^{2}|p}}q^2\mid q\,a^{q-1}\quad
+\text{\begin{tikzpicture}[baseline=(n.base)]
+\node[inner sep=0pt] (n) {\rlap{ou $p=1$}\phantom{\deleted{ou $p=1$}}};
+\draw[line width=.5pt] ([xshift=-.04cm,yshift=.02cm]n.west) -- ([xshift=.08cm,yshift=.01cm]n.east) .. controls ([xshift=.03cm,yshift=-.12cm]n.east) and ([xshift=-.3cm,yshift=-.12cm]n.east) .. ([xshift=.50cm,yshift=-.08cm]n.west);
+\end{tikzpicture}}
+\quad
+% Faint residual strokes and points in the interline gap; no character is supplied.
+\begin{tikzpicture}[baseline=-.05cm,x=1cm,y=1cm]
+\draw[gray,line width=.35pt] (0,.12) .. controls (.10,.02) and (.18,-.02) .. (.31,.02);
+\draw[gray,line width=.35pt] (.21,.13) -- (.27,.10);
+\draw[gray,line width=.35pt] (.34,.02) .. controls (.40,.17) and (.42,.26) .. (.52,.24);
+\draw[gray,line width=.35pt] (.49,.15) -- (.64,.14);
+\fill[gray] (.58,.31) circle (.5pt);
+\fill[gray] (.64,.04) circle (.45pt);
+\fill[gray] (.69,-.02) circle (.45pt);
+\end{tikzpicture}
+\\
+\Longrightarrow\quad&q\mid a^{q-1}\quad
+\overset{\inserted{\text{absurde car }q\nmid a}}{\text{\begin{tikzpicture}[baseline=(n.base)]
+\node[inner sep=0pt] (n) {\rlap{ou $p=1\Longrightarrow p=1$}\phantom{\deleted{ou $p=1\Longrightarrow p=1$}}};
+\draw[line width=.6pt] ([xshift=-.05cm,yshift=-.06cm]n.west) -- ([xshift=.04cm,yshift=.12cm]n.east);
+\end{tikzpicture}}}
 \end{aligned}
 \]
-Donc $\gamma=0$ ou $\gamma=$
-\begin{tikzpicture}[baseline=(q.base)]
-\node[inner sep=0pt] (q) at (0,0)
- {$\rlap{$q$}\phantom{\deleted{q}}$};
-% The live entry is physically raised above and to the right of the cancelled q.
-\node[inner sep=0pt,anchor=south west] at (-.01,.22) {$q\alpha-1$};
-\draw[line width=.45pt] (-.20,-.02) -- (.33,.28)
- .. controls (.48,.32) and (-.26,-.17) .. (-.20,-.02);
-\draw[line width=.45pt] (-.18,-.22) -- (.30,.10)
- .. controls (.39,.16) and (-.29,-.34) .. (-.18,-.22);
-\draw[line width=.45pt] (.02,-.24) -- (-.03,-.40);
-\end{tikzpicture}
-(sous réserve que l'hypothése est vraie)%
+Donc $\gamma=0$ ou $\gamma=
+% Cancelled q, raised q alpha minus one, and repeated oblique return strokes.
+\begin{tikzpicture}[baseline=(q.base),x=1ex,y=1ex]
+\node[inner sep=0pt] (q) at (0,0) {\rlap{$q$}\phantom{\deleted{$q$}}};
+\node[inner sep=0pt,anchor=south west] at (.15,.75) {$\scriptstyle q\alpha-1$};
+\draw[gray,line width=.45pt] (-.55,-.05) .. controls (-.77,-.29) and (-.90,-.39) .. (-.70,-.35) -- (.95,.82) -- (-.77,-.63) .. controls (-.90,-.81) and (-.87,-.90) .. (-.70,-.86) -- (.65,.12);
+\draw[gray,line width=.45pt] (.40,-.56) .. controls (-.10,-.95) and (-.35,-1.16) .. (-.34,-1.43) .. controls (-.35,-1.53) and (-.31,-1.57) .. (-.25,-1.60);
+\end{tikzpicture}$ (sous réserve que l'hypothése est vraie)%
 \margin{\begin{tikzpicture}[baseline=(n.base)]
-\node[inner sep=0pt,text width=.85\marginparwidth] (n)
- {C'est peut-être interessant car ici $2$ est mis à part dans
- \(\mathord{\overset{\scriptscriptstyle\unsure{/}}{\vphantom{l}}}\)l'ensemble des nombres premiers};
-% Small detached rising stroke before l'ensemble: role and hand unresolved.
-% Return arrow rises at the right from the final parenthesis toward this note.
-\draw[->] ([yshift=-.25cm]n.south east) -- ++(.16,0) |- (n.north east);
+\node[inner sep=0pt,text width=.85\marginparwidth] (n) {C'est peut-être interessant car ici $2$ est mis à part dans l'ensemble des nombres premiers};
+% A small detached point is visible at the lower start of the return arrow.
+\fill (n.south east) circle (.45pt);
+\draw[->] ([xshift=.07cm]n.south east) -- ([xshift=.16cm]n.south east) |- (n.north east);
 \end{tikzpicture}}
 % archive sheet number: 7

--- B
+++ C
@@ -13,70 +13,73 @@
 (1)\ \Longrightarrow\quad p\mid q\qquad\text{donc }\deleted{p=1\ \text{ou }}p=q\quad(\text{si }q\alpha-\alpha'\ne0)
 \]
 Donc si $p\ne q$ \quad $p$ premier \inserted{ou $p=1$} et $p\mid b'$ alors $\alpha'=q\alpha$
-\begin{flushright}
-\begin{tikzpicture}[baseline=(p.base)]
-\node[inner sep=0pt] (p) at(0,0) {$\left(\begin{aligned}
-&\text{\rlap{on l'impose sans risque}\phantom{\deleted{on l'impose sans risque}}}\\
-&\quad\text{\rlap{si $p=1$}\phantom{\deleted{si $p=1$}}}
-\end{aligned}\right)$};
-\draw ([xshift=.05cm,yshift=-.03cm]p.south west) -- ([xshift=.08cm,yshift=.03cm]p.north);
-\draw ([xshift=.22cm,yshift=-.04cm]p.south) -- ([xshift=-.04cm,yshift=.03cm]p.north east);
+% The parenthetical cancellation has two distinct oblique strokes.
+\begin{tikzpicture}[baseline=(n.north)]
+\node[inner sep=0pt,align=left] (n) {\rlap{\begin{tabular}{@{}l@{}}(on l'impose sans risque\\\quad si $p=1$)\end{tabular}}\phantom{\begin{tabular}{@{}l@{}}\deleted{(on l'impose sans risque}\\\quad\deleted{si $p=1$)}\end{tabular}}};
+\draw[line width=.45pt] ([xshift=.12cm,yshift=-.03cm]n.south west) -- ([xshift=2.65cm,yshift=-.04cm]n.north west);
+\draw[line width=.45pt] ([xshift=2.35cm,yshift=-.03cm]n.south west) -- ([xshift=-.18cm,yshift=-.04cm]n.north east);
 \end{tikzpicture}
-\end{flushright}
 
 Donc $\exists\,b_0\in\mathbb N^*$ et $\exists\,\gamma\in\mathbb N$ tel que $b'=q^\gamma b_0^q$ \margin{$q\nmid b_0$}
 
 de plus $b_0\mid b$ et si $b=b_0 b''$ alors $b_0\mathrel{\underset{1}{\smile}}b''$ ?
 
-De même $\exists\,a_0\in\mathbb N^*$ et $\exists\,\unsure{\zeta|\delta}\in\mathbb N$ tel que $a'=q^\zeta a_0^q$ avec $a_0\mid a$ et si $\overset{\unsure{\cdot|\prime}}{a}=a_0a''$ alors $a_0\mathrel{\underset{1}{\smile}}a''$ ?
-% The small detached mark above a is positioned as seen; its role and hand remain open.
+De même $\exists\,a_0\in\mathbb N^*$ et $\exists\,\unsure{\zeta|\delta}\in\mathbb N$ tel que $a'=q^\zeta a_0^q$ avec $a_0\mid a$ et si $a=a_0a''$ alors $a_0\mathrel{\underset{1}{\smile}}a''$ ?
 
 or $a\mathrel{\underset{1}{\smile}}b\Longrightarrow a_{\deleted{\unsure{0}}}'\mathrel{\underset{1}{\smile}}b'\Longrightarrow\zeta\times\gamma=0$ (et aussi $a_0\mathrel{\underset{1}{\smile}}b_0$)
 
 Je suppose désormais que $\zeta=0$ donc $a'=a_0^q$
 
-\figure{\begin{tikzpicture}[x=1cm,y=1cm]
-\node[anchor=west,inner sep=0pt] at(0,.75) {Donc \quad $c=b+a_0^q=a+q^\gamma b_0^q$};
-\node[anchor=west,inner sep=0pt,align=left,font=\footnotesize] at(6.75,1.05) {pour $q=2$ on a, $a_0=b_0=1$,\\$\gamma=1$, $b=4$, $a=3$, $c=5$};
-\draw (12.0,1.60) -- (6.65,1.63) .. controls(6.58,1.63) and(6.55,1.55) .. (6.55,1.45) -- (6.55,.08);
-\draw (0,.30) .. controls(2.6,.30) and(4.8,.17) .. (6.55,.10) .. controls(8.6,-.05) and(10.6,.02) .. (12.0,-.06);
-\node[anchor=west,inner sep=0pt,font=\footnotesize] at(.05,-.32) {Je fais l'hypothése suivante \quad si $q$ premier et $1\leqslant i<q$ alors $q\mid C_q^i$};
-\draw (.12,-.62) .. controls(4.2,-.57) and(8.9,-.80) .. (11.95,-.84);
+Donc \quad $c=b+a_0^q=a+q^\gamma b_0^q$
+\margin{\begin{tikzpicture}[baseline=(n.base)]
+\node[inner sep=2pt,text width=.85\marginparwidth] (n) {pour $q=2$ on a, $a_0=b_0=1$, $\gamma=1$, $b=4$, $a=3$, $c=5$};
+\draw (n.north east) -- (n.north west) -- (n.south west) -- (n.south east);
 \end{tikzpicture}}
 
-alors Si $q\geqslant3$ et $q\alpha-\alpha'\geqslant2$ \deleted{alors} on a \inserted{$p=q,\ {\unsure{a|\alpha}}'=\gamma$}
+\noindent\rule{\linewidth}{.35pt}\par
+Je fais l'hypothése suivante \quad si $q$ premier et $1\leqslant i<q$ alors $q\mid C_q^i$
+\par\noindent\rule{\linewidth}{.35pt}\par
+alors Si $q\geqslant3$ et $q\alpha-\alpha'\geqslant2$ \deleted{\unsure{alors}} on a
+% Two separate curved marks follow the pale p=q. The lower one's role is unresolved.
+\inserted{$p=q\,\underset{\hspace{.2em}\unsure{,}}{,}\ {\unsure{a|\alpha}}'=\gamma$}
 \[
 \begin{aligned}
 (1)\ \Longrightarrow\quad &\deleted{\unsure{p^{2}|p}}q^2\mid q\,a^{q-1}\quad
-\begin{tikzpicture}[baseline=(d.base)]
-\node[inner sep=0pt] (d) {\rlap{$\text{ou }p=1$}\phantom{$\deleted{\text{ou }p=1}$}};
-\draw ([yshift=.03cm]d.west) -- ([yshift=.11cm,xshift=-.06cm]d.east)
- .. controls([xshift=.15cm,yshift=.04cm]d.east) and([xshift=.02cm,yshift=-.14cm]d.east)
- .. ([xshift=.24cm,yshift=-.10cm]d.center) -- ([xshift=-.06cm,yshift=-.06cm]d.center);
-\end{tikzpicture}\\[.7ex]
+\text{\begin{tikzpicture}[baseline=(n.base)]
+\node[inner sep=0pt] (n) {\rlap{ou $p=1$}\phantom{\deleted{ou $p=1$}}};
+\draw[line width=.5pt] ([xshift=-.04cm,yshift=.02cm]n.west) -- ([xshift=.08cm,yshift=.01cm]n.east) .. controls ([xshift=.03cm,yshift=-.12cm]n.east) and ([xshift=-.3cm,yshift=-.12cm]n.east) .. ([xshift=.50cm,yshift=-.08cm]n.west);
+\end{tikzpicture}}
+\quad
+% Faint residual strokes and points in the interline gap; no character is supplied.
+\begin{tikzpicture}[baseline=-.05cm,x=1cm,y=1cm]
+\draw[gray,line width=.35pt] (0,.12) .. controls (.10,.02) and (.18,-.02) .. (.31,.02);
+\draw[gray,line width=.35pt] (.21,.13) -- (.27,.10);
+\draw[gray,line width=.35pt] (.34,.02) .. controls (.40,.17) and (.42,.26) .. (.52,.24);
+\draw[gray,line width=.35pt] (.49,.15) -- (.64,.14);
+\fill[gray] (.58,.31) circle (.5pt);
+\fill[gray] (.64,.04) circle (.45pt);
+\fill[gray] (.69,-.02) circle (.45pt);
+\end{tikzpicture}
+\\
 \Longrightarrow\quad&q\mid a^{q-1}\quad
-\begin{tikzpicture}[baseline=(d.base)]
-\node[inner sep=0pt] (d) {\rlap{$\text{ou }p=1\Longrightarrow p=1$}\phantom{$\deleted{\text{ou }p=1\Longrightarrow p=1}$}};
-\draw ([xshift=-.03cm,yshift=-.02cm]d.west) -- ([xshift=.05cm,yshift=.22cm]d.east);
-\node[anchor=south,inner sep=0pt] at([yshift=.11cm]d.north) {$\inserted{\text{absurde car }q\nmid a}$};
-\end{tikzpicture}
+\overset{\inserted{\text{absurde car }q\nmid a}}{\text{\begin{tikzpicture}[baseline=(n.base)]
+\node[inner sep=0pt] (n) {\rlap{ou $p=1\Longrightarrow p=1$}\phantom{\deleted{ou $p=1\Longrightarrow p=1$}}};
+\draw[line width=.6pt] ([xshift=-.05cm,yshift=-.06cm]n.west) -- ([xshift=.04cm,yshift=.12cm]n.east);
+\end{tikzpicture}}}
 \end{aligned}
 \]
 Donc $\gamma=0$ ou $\gamma=
-\begin{tikzpicture}[baseline=(q.base)]
-\node[inner sep=0pt] (q) at(0,0) {\rlap{$q$}\phantom{$\deleted{q}$}};
-\node[anchor=base west,inner sep=0pt] at(-.03,.38) {$q\alpha-1$};
-\draw (-.16,-.02) .. controls(-.38,-.18) and(-.31,-.27) .. (-.18,-.18) -- (.30,.17)
- -- (-.24,-.34) .. controls(-.34,-.45) and(-.22,-.45) .. (.24,-.20) -- (-.03,-.47);
+% Cancelled q, raised q alpha minus one, and repeated oblique return strokes.
+\begin{tikzpicture}[baseline=(q.base),x=1ex,y=1ex]
+\node[inner sep=0pt] (q) at (0,0) {\rlap{$q$}\phantom{\deleted{$q$}}};
+\node[inner sep=0pt,anchor=south west] at (.15,.75) {$\scriptstyle q\alpha-1$};
+\draw[gray,line width=.45pt] (-.55,-.05) .. controls (-.77,-.29) and (-.90,-.39) .. (-.70,-.35) -- (.95,.82) -- (-.77,-.63) .. controls (-.90,-.81) and (-.87,-.90) .. (-.70,-.86) -- (.65,.12);
+\draw[gray,line width=.45pt] (.40,-.56) .. controls (-.10,-.95) and (-.35,-1.16) .. (-.34,-1.43) .. controls (-.35,-1.53) and (-.31,-1.57) .. (-.25,-1.60);
 \end{tikzpicture}$ (sous réserve que l'hypothése est vraie)%
-% The raised q alpha - 1 and the cancelled lower q are reproduced geometrically.
 \margin{\begin{tikzpicture}[baseline=(n.base)]
 \node[inner sep=0pt,text width=.85\marginparwidth] (n) {C'est peut-être interessant car ici $2$ est mis à part dans l'ensemble des nombres premiers};
-\fill ([xshift=.07cm,yshift=-.47cm]n.south east) circle(.022cm);
-\draw ([xshift=.15cm,yshift=-.47cm]n.south east) -- ([xshift=.31cm,yshift=-.47cm]n.south east)
- -- ([xshift=.35cm,yshift=-.16cm]n.north east)
- .. controls([xshift=.35cm,yshift=-.03cm]n.north east) and([xshift=.19cm,yshift=-.01cm]n.north east)
- .. ([xshift=.06cm,yshift=.01cm]n.north east);
-\draw ([xshift=.19cm,yshift=.14cm]n.north east) .. controls([xshift=.00cm,yshift=.04cm]n.north east) and([xshift=-.01cm,yshift=-.06cm]n.north east) .. ([xshift=.15cm,yshift=-.10cm]n.north east);
+% A small detached point is visible at the lower start of the return arrow.
+\fill (n.south east) circle (.45pt);
+\draw[->] ([xshift=.07cm]n.south east) -- ([xshift=.16cm]n.south east) |- (n.north east);
 \end{tikzpicture}}
 % archive sheet number: 7
