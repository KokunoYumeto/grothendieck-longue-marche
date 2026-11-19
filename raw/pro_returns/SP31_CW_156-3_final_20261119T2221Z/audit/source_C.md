# Source C mechanical audit worksheet

Mechanical alignment is a review aid, not a reading decision or proof check.

Grouped decisions are not assigned to individual occurrences by ordinal. A candidate unmarked alignment is not an ink-resolution judgment. Add ink dispositions and crop links to the TSV; those review fields survive regeneration.

## Summary

```json
{
  "pages_examined_mechanically": 24,
  "final_pages_present": 24,
  "source_c_unsure_occurrences": 517,
  "mechanical_states": {
    "no unsure token in aligned span; inspect replacement": 195,
    "unsure token(s) overlap changed alignment; inspect": 38,
    "same unsure token in equal alignment": 284
  },
  "workflow_gap_count": 0,
  "root_evidence_complete_occurrences": 517,
  "root_evidence_complete_pages": 24,
  "ink_dispositions_filled": 517,
  "alignment_rechecks_flagged": 0
}
```

## Workflow gaps

None detected mechanically.

## Source C doubts

### C-002-U001 (C line 5)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 5.

Source C token:

```tex
\unsure{\ldots}
```

Source C context:

```tex
\cotefile{156-3}
\scanpage{2}
\mspage{1}

\uline{Réseaux}\unsure{\ldots} via découpages.

(8 Juin 86)

% slanted
\margin{\unsure{CF|CH|Cf|Ch}\,\uline{III}}

% slanted
\marg
```

Aligned final span:

```tex
\ldots\
```

Final context (up to 100 characters either side):

```tex
\cotefile{156-3}
\scanpage{2}
\mspage{1}

\uline{Réseaux}\ldots\ via découpages.

(8 Juin 86)

% slanted; within the drawn corner enclosure
\margin{\figure{\begin{t
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/002_header.jpg

Alignment requires recheck: no flag

Review note: Three separate rising dots are visible; retain ellipsis without doubt.

### C-002-U002 (C line 10)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 10.

Source C token:

```tex
\unsure{CF|CH|Cf|Ch}
```

Source C context:

```tex
npage{2}
\mspage{1}

\uline{Réseaux}\unsure{\ldots} via découpages.

(8 Juin 86)

% slanted
\margin{\unsure{CF|CH|Cf|Ch}\,\uline{III}}

% slanted
\margin{\deleted{\unsure{Les ensembles}} \unsure{Parties|Ensembles} \delet
```

Aligned final span:

```tex
\figure{\begin{tikzpicture}[scale=.65]
\draw (.05,1.65) .. controls (-.10,.90) and (-.25,.20) .. (-.35,0) .. controls (.20,-.04) and (.70,.14) .. (1.45,.12);
\node[rotate=25] at (.65,.67) {GF
```

Final context (up to 100 characters either side):

```tex
{Réseaux}\ldots\ via découpages.

(8 Juin 86)

% slanted; within the drawn corner enclosure
\margin{\figure{\begin{tikzpicture}[scale=.65]
\draw (.05,1.65) .. controls (-.10,.90) and (-.25,.20) .. (-.35,0) .. controls (.20,-.04) and (.70,.14) .. (1.45,.12);
\node[rotate=25] at (.65,.67) {GF\,\uline{III}};
\end{tikzpicture}}}

% slanted
\margin{\deleted{Ensembles} Parties \unsure{finies} d
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/002_corner.jpg

Alignment requires recheck: no flag

Review note: G has an inward terminal foot; F has the crossbar; three numeral strokes follow. Alignment recheck: The new TikZ wrapper shifts the mechanical span; the reviewed label is GF III, inside the curved corner (002_corner.jpg).

### C-002-U003 (C line 13)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 16.

Source C token:

```tex
\unsure{Les ensembles}
```

Source C context:

```tex
ges.

(8 Juin 86)

% slanted
\margin{\unsure{CF|CH|Cf|Ch}\,\uline{III}}

% slanted
\margin{\deleted{\unsure{Les ensembles}} \unsure{Parties|Ensembles} \deleted{\unsure{des}} de lieux \unsure{modérés|modérées}}

Je voudrais
```

Aligned final span:

```tex

```

Final context (up to 100 characters either side):

```tex
);
\node[rotate=25] at (.65,.67) {GF\,\uline{III}};
\end{tikzpicture}}}

% slanted
\margin{\deleted{Ensembles} Parties \unsure{finies} de lieux \unsure{modérés|modérées}}

Je voudrais définir une autr
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: revised

Crop links: crops/002_margin_top.jpg

Alignment requires recheck: no flag

Review note: Crossed Ensembles and live Parties are distinguishable. The intervening finies remains doubtful; the previous Les/des segmentation is unsupported.

### C-002-U004 (C line 13)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 16.

Source C token:

```tex
\unsure{Parties|Ensembles}
```

Source C context:

```tex
nted
\margin{\unsure{CF|CH|Cf|Ch}\,\uline{III}}

% slanted
\margin{\deleted{\unsure{Les ensembles}} \unsure{Parties|Ensembles} \deleted{\unsure{des}} de lieux \unsure{modérés|modérées}}

Je voudrais définir une autre axiomatiq
```

Aligned final span:

```tex
Ensembles}
```

Final context (up to 100 characters either side):

```tex
);
\node[rotate=25] at (.65,.67) {GF\,\uline{III}};
\end{tikzpicture}}}

% slanted
\margin{\deleted{Ensembles} Parties \unsure{finies} de lieux \unsure{modérés|modérées}}

Je voudrais définir une autre axiomati
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: revised

Crop links: crops/002_margin_top.jpg

Alignment requires recheck: no flag

Review note: Crossed Ensembles and live Parties are distinguishable. The intervening finies remains doubtful; the previous Les/des segmentation is unsupported.

### C-002-U005 (C line 13)

Mechanical state: **unsure token(s) overlap changed alignment; inspect**. Final aligned line: 16.

Source C token:

```tex
\unsure{des}
```

Source C context:

```tex
uline{III}}

% slanted
\margin{\deleted{\unsure{Les ensembles}} \unsure{Parties|Ensembles} \deleted{\unsure{des}} de lieux \unsure{modérés|modérées}}

Je voudrais définir une autre axiomatique
\deleted{des réseau
```

Aligned final span:

```tex
\unsure{finies
```

Final context (up to 100 characters either side):

```tex
 at (.65,.67) {GF\,\uline{III}};
\end{tikzpicture}}}

% slanted
\margin{\deleted{Ensembles} Parties \unsure{finies} de lieux \unsure{modérés|modérées}}

Je voudrais définir une autre axiomatique des \deleted{réseau
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: revised

Crop links: crops/002_margin_top.jpg

Alignment requires recheck: no flag

Review note: Crossed Ensembles and live Parties are distinguishable. The intervening finies remains doubtful; the previous Les/des segmentation is unsupported.

### C-002-U006 (C line 13)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 16.

Source C token:

```tex
\unsure{modérés|modérées}
```

Source C context:

```tex
\margin{\deleted{\unsure{Les ensembles}} \unsure{Parties|Ensembles} \deleted{\unsure{des}} de lieux \unsure{modérés|modérées}}

Je voudrais définir une autre axiomatique
\deleted{des réseaux,} \deleted{\unsure{l}}la structure
```

Aligned final span:

```tex
\unsure{modérés|modérées}
```

Final context (up to 100 characters either side):

```tex
{III}};
\end{tikzpicture}}}

% slanted
\margin{\deleted{Ensembles} Parties \unsure{finies} de lieux \unsure{modérés|modérées}}

Je voudrais définir une autre axiomatique des \deleted{réseaux,}
\deleted{\unsure{l}}\unsure{la|a
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/002_margin_top.jpg

Alignment requires recheck: no flag

Review note: Final gender ending remains compressed under slanted writing.

### C-002-U007 (C line 16)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 19.

Source C token:

```tex
\unsure{l}
```

Source C context:

```tex
nsure{modérés|modérées}}

Je voudrais définir une autre axiomatique
\deleted{des réseaux,} \deleted{\unsure{l}}la structure de réseaux
sur un ens. $\unsure{\mathcal L|L}$ (\deleted{\unsure{d}}ens. des ``lieux''
```

Aligned final span:

```tex
\unsure{l}
```

Final context (up to 100 characters either side):

```tex
nsure{modérés|modérées}}

Je voudrais définir une autre axiomatique des \deleted{réseaux,}
\deleted{\unsure{l}}\unsure{la|a} structures de réseaux
sur un ens. $\mathcal L$ (\deleted{\unsure{d}}ens. des ``lieux'
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/002_opening.jpg

Alignment requires recheck: no flag

Review note: Dense overwritten ascenders do not securely recover the old letters.

### C-002-U008 (C line 17)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 20.

Source C token:

```tex
\unsure{\mathcal L|L}
```

Source C context:

```tex
e autre axiomatique
\deleted{des réseaux,} \deleted{\unsure{l}}la structure de réseaux
sur un ens. $\unsure{\mathcal L|L}$ (\deleted{\unsure{d}}ens. des ``lieux'').

\textcircled{\scriptsize a}\quad $S_0\deleted{\unsure{(
```

Aligned final span:

```tex
\mathcal L
```

Final context (up to 100 characters either side):

```tex
matique des \deleted{réseaux,}
\deleted{\unsure{l}}\unsure{la|a} structures de réseaux
sur un ens. $\mathcal L$ (\deleted{\unsure{d}}ens. des ``lieux'').

\textcircled{\scriptsize a}\quad $S_0\deleted{\unsure{(
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/002_opening.jpg

Alignment requires recheck: no flag

Review note: Lower loop and crossing sweep identify script L.

### C-002-U009 (C line 17)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 20.

Source C token:

```tex
\unsure{d}
```

Source C context:

```tex
réseaux,} \deleted{\unsure{l}}la structure de réseaux
sur un ens. $\unsure{\mathcal L|L}$ (\deleted{\unsure{d}}ens. des ``lieux'').

\textcircled{\scriptsize a}\quad $S_0\deleted{\unsure{(L)|L}}\subset\unsure{P
```

Aligned final span:

```tex
\unsure{d}
```

Final context (up to 100 characters either side):

```tex
éseaux,}
\deleted{\unsure{l}}\unsure{la|a} structures de réseaux
sur un ens. $\mathcal L$ (\deleted{\unsure{d}}ens. des ``lieux'').

\textcircled{\scriptsize a}\quad $S_0\deleted{\unsure{(L)|L}}\subset P_2(L)$ 
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/002_opening.jpg

Alignment requires recheck: no flag

Review note: Dense overwritten ascenders do not securely recover the old letters.

### C-002-U010 (C line 19)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 22.

Source C token:

```tex
\unsure{(L)|L}
```

Source C context:

```tex
hcal L|L}$ (\deleted{\unsure{d}}ens. des ``lieux'').

\textcircled{\scriptsize a}\quad $S_0\deleted{\unsure{(L)|L}}\subset\unsure{P|\mathcal P}_2(L)$ \unsure{l'ens} des \uline{0-sphères}
\uline{plongées}, ou des \u
```

Aligned final span:

```tex
\unsure{(L)|L}
```

Final context (up to 100 characters either side):

```tex
mathcal L$ (\deleted{\unsure{d}}ens. des ``lieux'').

\textcircled{\scriptsize a}\quad $S_0\deleted{\unsure{(L)|L}}\subset P_2(L)$ l'ens des \uline{0-sphères}
\uline{plongées}, ou des \uline{paires} \deleted{\unsur
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/002_a.jpg

Alignment requires recheck: no flag

Review note: Crossed forms remain obscured; do not restore from expected notation.

### C-002-U011 (C line 19)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 22.

Source C token:

```tex
\unsure{P|\mathcal P}
```

Source C context:

```tex
unsure{d}}ens. des ``lieux'').

\textcircled{\scriptsize a}\quad $S_0\deleted{\unsure{(L)|L}}\subset\unsure{P|\mathcal P}_2(L)$ \unsure{l'ens} des \uline{0-sphères}
\uline{plongées}, ou des \uline{paires} \deleted{\unsure
```

Aligned final span:

```tex
 P
```

Final context (up to 100 characters either side):

```tex
unsure{d}}ens. des ``lieux'').

\textcircled{\scriptsize a}\quad $S_0\deleted{\unsure{(L)|L}}\subset P_2(L)$ l'ens des \uline{0-sphères}
\uline{plongées}, ou des \uline{paires} \deleted{\unsure{mod.}} (
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/002_a.jpg

Alignment requires recheck: no flag

Review note: Single-staff P, l apostrophe ens, abbreviated st and ending of modérée are legible.

### C-002-U012 (C line 19)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 22.

Source C token:

```tex
\unsure{l'ens}
```

Source C context:

```tex
).

\textcircled{\scriptsize a}\quad $S_0\deleted{\unsure{(L)|L}}\subset\unsure{P|\mathcal P}_2(L)$ \unsure{l'ens} des \uline{0-sphères}
\uline{plongées}, ou des \uline{paires} \deleted{\unsure{mod.}} (de
lieux) mo
```

Aligned final span:

```tex
l'ens
```

Final context (up to 100 characters either side):

```tex
}ens. des ``lieux'').

\textcircled{\scriptsize a}\quad $S_0\deleted{\unsure{(L)|L}}\subset P_2(L)$ l'ens des \uline{0-sphères}
\uline{plongées}, ou des \uline{paires} \deleted{\unsure{mod.}} (de
lieux) mo
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/002_a.jpg

Alignment requires recheck: no flag

Review note: Single-staff P, l apostrophe ens, abbreviated st and ending of modérée are legible.

### C-002-U013 (C line 20)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 23.

Source C token:

```tex
\unsure{mod.}
```

Source C context:

```tex
hcal P}_2(L)$ \unsure{l'ens} des \uline{0-sphères}
\uline{plongées}, ou des \uline{paires} \deleted{\unsure{mod.}} (de
lieux) modérées. \inserted{si $\{a,b\}\in S_0$ ; on dit aussi que $a,b$ \unsure{st} \uline{dis
```

Aligned final span:

```tex
\unsure{mod.}
```

Final context (up to 100 characters either side):

```tex
(L)|L}}\subset P_2(L)$ l'ens des \uline{0-sphères}
\uline{plongées}, ou des \uline{paires} \deleted{\unsure{mod.}} (de
lieux) modérées. \inserted{si $\{a,b\}\in S_0$ ; on dit aussi que $a,b$ st \uline{disjoints} o
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/002_a.jpg

Alignment requires recheck: no flag

Review note: Crossed forms remain obscured; do not restore from expected notation.

### C-002-U014 (C line 21)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 24.

Source C token:

```tex
\unsure{st}
```

Source C context:

```tex
\deleted{\unsure{mod.}} (de
lieux) modérées. \inserted{si $\{a,b\}\in S_0$ ; on dit aussi que $a,b$ \unsure{st} \uline{disjoints} ou en position relative \unsure{modérée}.}

% slanted
\margin{Mais, \unsure{on} d
```

Aligned final span:

```tex
st
```

Final context (up to 100 characters either side):

```tex
\deleted{\unsure{mod.}} (de
lieux) modérées. \inserted{si $\{a,b\}\in S_0$ ; on dit aussi que $a,b$ st \uline{disjoints} ou en position relative modérée.}

% slanted
\margin{Mais, on dit aussi que $a,b$
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/002_a.jpg

Alignment requires recheck: no flag

Review note: Single-staff P, l apostrophe ens, abbreviated st and ending of modérée are legible.

### C-002-U015 (C line 21)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 24.

Source C token:

```tex
\unsure{modérée}
```

Source C context:

```tex
{si $\{a,b\}\in S_0$ ; on dit aussi que $a,b$ \unsure{st} \uline{disjoints} ou en position relative \unsure{modérée}.}

% slanted
\margin{Mais, \unsure{on} dit aussi que $a,b$ en position rel. modérée si $a=b$ \uline
```

Aligned final span:

```tex
modérée
```

Final context (up to 100 characters either side):

```tex
\inserted{si $\{a,b\}\in S_0$ ; on dit aussi que $a,b$ st \uline{disjoints} ou en position relative modérée.}

% slanted
\margin{Mais, on dit aussi que $a,b$ en position rel. modérée si $a=b$ \uline{ou} $\{a
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/002_a.jpg

Alignment requires recheck: no flag

Review note: Single-staff P, l apostrophe ens, abbreviated st and ending of modérée are legible.

### C-002-U016 (C line 24)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 27.

Source C token:

```tex
\unsure{on}
```

Source C context:

```tex
$ \unsure{st} \uline{disjoints} ou en position relative \unsure{modérée}.}

% slanted
\margin{Mais, \unsure{on} dit aussi que $a,b$ en position rel. modérée si $a=b$ \uline{ou} $\{a,b\}\in S_0$}

[En termes de
l
```

Aligned final span:

```tex
on
```

Final context (up to 100 characters either side):

```tex
dit aussi que $a,b$ st \uline{disjoints} ou en position relative modérée.}

% slanted
\margin{Mais, on dit aussi que $a,b$ en position rel. modérée si $a=b$ \uline{ou} $\{a,b\}\in S_0$}

[En termes de l
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/002_margin_mid.jpg

Alignment requires recheck: no flag

Review note: Rotated short on is visible after Mais comma.

### C-002-U017 (C line 28)

Mechanical state: **unsure token(s) overlap changed alignment; inspect**. Final aligned line: 30.

Source C token:

```tex
\unsure{a|à|}
```

Source C context:

```tex
el. modérée si $a=b$ \uline{ou} $\{a,b\}\in S_0$}

[En termes de
l'axiomatique par les segments,
cel\unsure{a|à|} signifie que \deleted{$a,b$ \unsure{sont} ou bien} \inserted{(à \unsure{part} $a,b$ \uline{distinct
```

Aligned final span:

```tex
\unsure{cela|celà}
```

Final context (up to 100 characters either side):

```tex
n rel. modérée si $a=b$ \uline{ou} $\{a,b\}\in S_0$}

[En termes de l'axiomatique par les segments,
\unsure{cela|celà} signifie que \deleted{$a,b$ \unsure{sont} ou bien} \inserted{(à part $a,b$ \uline{distincts}},
\uns
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: revised

Crop links: crops/002_segments.jpg

Alignment requires recheck: no flag

Review note: Doubt belongs to the accent on final a of cela; empty alternative removed without guessing.

### C-002-U018 (C line 28)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 30.

Source C token:

```tex
\unsure{sont}
```

Source C context:

```tex
n S_0$}

[En termes de
l'axiomatique par les segments,
cel\unsure{a|à|} signifie que \deleted{$a,b$ \unsure{sont} ou bien} \inserted{(à \unsure{part} $a,b$ \uline{distincts}},
\unsure{contenu} dans $\{a,b\}\in\del
```

Aligned final span:

```tex
\unsure{sont}
```

Final context (up to 100 characters either side):

```tex
S_0$}

[En termes de l'axiomatique par les segments,
\unsure{cela|celà} signifie que \deleted{$a,b$ \unsure{sont} ou bien} \inserted{(à part $a,b$ \uline{distincts}},
\unsure{contenu} dans $\{a,b\}\in\deleted{\uns
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/002_segments.jpg

Alignment requires recheck: no flag

Review note: Overwriting and abbreviated compressed groups remain insufficient to settle the listed alternatives or old letters.

### C-002-U019 (C line 28)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 30.

Source C token:

```tex
\unsure{part}
```

Source C context:

```tex
 par les segments,
cel\unsure{a|à|} signifie que \deleted{$a,b$ \unsure{sont} ou bien} \inserted{(à \unsure{part} $a,b$ \uline{distincts}},
\unsure{contenu} dans $\{a,b\}\in\deleted{\unsure{S_0}}P_2(\mathcal L)$, 
```

Aligned final span:

```tex
part
```

Final context (up to 100 characters either side):

```tex
ar les segments,
\unsure{cela|celà} signifie que \deleted{$a,b$ \unsure{sont} ou bien} \inserted{(à part $a,b$ \uline{distincts}},
\unsure{contenu} dans $\{a,b\}\in\deleted{\unsure{S_0}}P_2(\mathcal L)$, 
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/002_segments.jpg

Alignment requires recheck: no flag

Review note: Part, comma, three-stroke same-line shorthand and que are distinguishable in the enlarged strokes.

### C-002-U020 (C line 29)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 31.

Source C token:

```tex
\unsure{contenu}
```

Source C context:

```tex
ifie que \deleted{$a,b$ \unsure{sont} ou bien} \inserted{(à \unsure{part} $a,b$ \uline{distincts}},
\unsure{contenu} dans $\{a,b\}\in\deleted{\unsure{S_0}}P_2(\mathcal L)$, que
ou bien $\{a\unsure{;|,}b\}\cap\mathcal
```

Aligned final span:

```tex
\unsure{contenu}
```

Final context (up to 100 characters either side):

```tex
elà} signifie que \deleted{$a,b$ \unsure{sont} ou bien} \inserted{(à part $a,b$ \uline{distincts}},
\unsure{contenu} dans $\{a,b\}\in\deleted{\unsure{S_0}}P_2(\mathcal L)$, que
ou bien $\{a,b\}\cap\mathcal L_s\ne\var
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/002_segments.jpg

Alignment requires recheck: no flag

Review note: Overwriting and abbreviated compressed groups remain insufficient to settle the listed alternatives or old letters.

### C-002-U021 (C line 29)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 31.

Source C token:

```tex
\unsure{S_0}
```

Source C context:

```tex
ien} \inserted{(à \unsure{part} $a,b$ \uline{distincts}},
\unsure{contenu} dans $\{a,b\}\in\deleted{\unsure{S_0}}P_2(\mathcal L)$, que
ou bien $\{a\unsure{;|,}b\}\cap\mathcal L_s\ne\varnothing$ ($a$ ou $b$ est un
```

Aligned final span:

```tex
\unsure{S_0}
```

Final context (up to 100 characters either side):

```tex
ont} ou bien} \inserted{(à part $a,b$ \uline{distincts}},
\unsure{contenu} dans $\{a,b\}\in\deleted{\unsure{S_0}}P_2(\mathcal L)$, que
ou bien $\{a,b\}\cap\mathcal L_s\ne\varnothing$ ($a$ ou $b$ est un
nœud \unsu
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/002_segments.jpg

Alignment requires recheck: no flag

Review note: Overwriting and abbreviated compressed groups remain insufficient to settle the listed alternatives or old letters.

### C-002-U022 (C line 30)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 32.

Source C token:

```tex
\unsure{;|,}
```

Source C context:

```tex
stincts}},
\unsure{contenu} dans $\{a,b\}\in\deleted{\unsure{S_0}}P_2(\mathcal L)$, que
ou bien $\{a\unsure{;|,}b\}\cap\mathcal L_s\ne\varnothing$ ($a$ ou $b$ est un
nœud \unsure{sg$_r$|sg} du réseau) \uline{ou} 
```

Aligned final span:

```tex
,
```

Final context (up to 100 characters either side):

```tex
stincts}},
\unsure{contenu} dans $\{a,b\}\in\deleted{\unsure{S_0}}P_2(\mathcal L)$, que
ou bien $\{a,b\}\cap\mathcal L_s\ne\varnothing$ ($a$ ou $b$ est un
nœud \unsure{sg$_r$|sg} du réseau) \uline{ou} 
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/002_segments.jpg

Alignment requires recheck: no flag

Review note: Part, comma, three-stroke same-line shorthand and que are distinguishable in the enlarged strokes.

### C-002-U023 (C line 31)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 33.

Source C token:

```tex
\unsure{sg$_r$|sg}
```

Source C context:

```tex
mathcal L)$, que
ou bien $\{a\unsure{;|,}b\}\cap\mathcal L_s\ne\varnothing$ ($a$ ou $b$ est un
nœud \unsure{sg$_r$|sg} du réseau) \uline{ou} \uline{bien} \deleted{$a,b$}
(si \deleted{\unsure{st|sont}} \inserted{$a,b$} 
```

Aligned final span:

```tex
\unsure{sg$_r$|sg}
```

Final context (up to 100 characters either side):

```tex
{S_0}}P_2(\mathcal L)$, que
ou bien $\{a,b\}\cap\mathcal L_s\ne\varnothing$ ($a$ ou $b$ est un
nœud \unsure{sg$_r$|sg} du réseau) \uline{ou} \uline{bien} \deleted{$a,b$}
(si \deleted{\unsure{st|sont}} \inserted{$a,b$} 
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/002_segments.jpg

Alignment requires recheck: no flag

Review note: Overwriting and abbreviated compressed groups remain insufficient to settle the listed alternatives or old letters.

### C-002-U024 (C line 32)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 34.

Source C token:

```tex
\unsure{st|sont}
```

Source C context:

```tex
 $b$ est un
nœud \unsure{sg$_r$|sg} du réseau) \uline{ou} \uline{bien} \deleted{$a,b$}
(si \deleted{\unsure{st|sont}} \inserted{$a,b$} réguliers) que $a,b$ \inserted{\unsure{doivt|doit}} \unsure{appartiennent|apparti
```

Aligned final span:

```tex
\unsure{st|sont}
```

Final context (up to 100 characters either side):

```tex
 $b$ est un
nœud \unsure{sg$_r$|sg} du réseau) \uline{ou} \uline{bien} \deleted{$a,b$}
(si \deleted{\unsure{st|sont}} \inserted{$a,b$} réguliers) que $a,b$ \inserted{\unsure{doivt|doit}} \unsure{appartiennent|apparti
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/002_segments.jpg

Alignment requires recheck: no flag

Review note: Overwriting and abbreviated compressed groups remain insufficient to settle the listed alternatives or old letters.

### C-002-U025 (C line 32)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 34.

Source C token:

```tex
\unsure{doivt|doit}
```

Source C context:

```tex
ien} \deleted{$a,b$}
(si \deleted{\unsure{st|sont}} \inserted{$a,b$} réguliers) que $a,b$ \inserted{\unsure{doivt|doit}} \unsure{appartiennent|appartient} :
des lignes différentes, \unsure{soit|sont|sauf}, s'ils sont
da
```

Aligned final span:

```tex
\unsure{doivt|doit}
```

Final context (up to 100 characters either side):

```tex
ien} \deleted{$a,b$}
(si \deleted{\unsure{st|sont}} \inserted{$a,b$} réguliers) que $a,b$ \inserted{\unsure{doivt|doit}} \unsure{appartiennent|appartient} :
des lignes différentes, \unsure{soit|sont}, s'ils sont
dans un
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/002_segments.jpg

Alignment requires recheck: no flag

Review note: Overwriting and abbreviated compressed groups remain insufficient to settle the listed alternatives or old letters.

### C-002-U026 (C line 32)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 34.

Source C token:

```tex
\unsure{appartiennent|appartient}
```

Source C context:

```tex
(si \deleted{\unsure{st|sont}} \inserted{$a,b$} réguliers) que $a,b$ \inserted{\unsure{doivt|doit}} \unsure{appartiennent|appartient} :
des lignes différentes, \unsure{soit|sont|sauf}, s'ils sont
dans une $\unsure{\bar{=}|=}$ ligne, 
```

Aligned final span:

```tex
\unsure{appartiennent|appartient}
```

Final context (up to 100 characters either side):

```tex
(si \deleted{\unsure{st|sont}} \inserted{$a,b$} réguliers) que $a,b$ \inserted{\unsure{doivt|doit}} \unsure{appartiennent|appartient} :
des lignes différentes, \unsure{soit|sont}, s'ils sont
dans une $\bar{=}$ ligne, que $\{a,b\}=\pa
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/002_segments.jpg

Alignment requires recheck: no flag

Review note: Overwriting and abbreviated compressed groups remain insufficient to settle the listed alternatives or old letters.

### C-002-U027 (C line 33)

Mechanical state: **unsure token(s) overlap changed alignment; inspect**. Final aligned line: 35.

Source C token:

```tex
\unsure{soit|sont|sauf}
```

Source C context:

```tex
ue $a,b$ \inserted{\unsure{doivt|doit}} \unsure{appartiennent|appartient} :
des lignes différentes, \unsure{soit|sont|sauf}, s'ils sont
dans une $\unsure{\bar{=}|=}$ ligne, \unsure{pour|que} $\{a,b\}=\partial I$,
pour $I\in
```

Aligned final span:

```tex
\unsure{soit|sont}
```

Final context (up to 100 characters either side):

```tex
ue $a,b$ \inserted{\unsure{doivt|doit}} \unsure{appartiennent|appartient} :
des lignes différentes, \unsure{soit|sont}, s'ils sont
dans une $\bar{=}$ ligne, que $\{a,b\}=\partial I$,
pour $I\in S$].

\deleted{\unsure{b
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: revised

Crop links: crops/002_segments.jpg

Alignment requires recheck: no flag

Review note: No f descender supports sauf; soit/sont remain competing readings.

### C-002-U028 (C line 34)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 36.

Source C token:

```tex
\unsure{\bar{=}|=}
```

Source C context:

```tex
e{appartiennent|appartient} :
des lignes différentes, \unsure{soit|sont|sauf}, s'ils sont
dans une $\unsure{\bar{=}|=}$ ligne, \unsure{pour|que} $\{a,b\}=\partial I$,
pour $I\in S$].

\deleted{\unsure{b)}} Une partie \
```

Aligned final span:

```tex
\bar{=}
```

Final context (up to 100 characters either side):

```tex
unsure{appartiennent|appartient} :
des lignes différentes, \unsure{soit|sont}, s'ils sont
dans une $\bar{=}$ ligne, que $\{a,b\}=\partial I$,
pour $I\in S$].

\deleted{\unsure{b)}} Une partie \uline{finie} \
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/002_segments.jpg

Alignment requires recheck: no flag

Review note: Part, comma, three-stroke same-line shorthand and que are distinguishable in the enlarged strokes.

### C-002-U029 (C line 34)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 36.

Source C token:

```tex
\unsure{pour|que}
```

Source C context:

```tex
 :
des lignes différentes, \unsure{soit|sont|sauf}, s'ils sont
dans une $\unsure{\bar{=}|=}$ ligne, \unsure{pour|que} $\{a,b\}=\partial I$,
pour $I\in S$].

\deleted{\unsure{b)}} Une partie \uline{finie} \inserted{$T$
```

Aligned final span:

```tex
que
```

Final context (up to 100 characters either side):

```tex
nent|appartient} :
des lignes différentes, \unsure{soit|sont}, s'ils sont
dans une $\bar{=}$ ligne, que $\{a,b\}=\partial I$,
pour $I\in S$].

\deleted{\unsure{b)}} Une partie \uline{finie} \inserted{$T$
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/002_segments.jpg

Alignment requires recheck: no flag

Review note: Part, comma, three-stroke same-line shorthand and que are distinguishable in the enlarged strokes.

### C-002-U030 (C line 37)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 39.

Source C token:

```tex
\unsure{b)}
```

Source C context:

```tex
s une $\unsure{\bar{=}|=}$ ligne, \unsure{pour|que} $\{a,b\}=\partial I$,
pour $I\in S$].

\deleted{\unsure{b)}} Une partie \uline{finie} \inserted{$T$} est dite \deleted{\unsure{admissible}} \inserted{``\uline{
```

Aligned final span:

```tex
\unsure{b)}
```

Final context (up to 100 characters either side):

```tex
oit|sont}, s'ils sont
dans une $\bar{=}$ ligne, que $\{a,b\}=\partial I$,
pour $I\in S$].

\deleted{\unsure{b)}} Une partie \uline{finie} \inserted{$T$} est dite \deleted{admissible} \inserted{``\uline{modérée}'
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/002_b.jpg

Alignment requires recheck: no flag

Review note: Scribbled label and crossed on a remain partly covered by cancellation.

### C-002-U031 (C line 37)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 39.

Source C token:

```tex
\unsure{admissible}
```

Source C context:

```tex
$,
pour $I\in S$].

\deleted{\unsure{b)}} Une partie \uline{finie} \inserted{$T$} est dite \deleted{\unsure{admissible}} \inserted{``\uline{modérée}''}
si \deleted{$\forall\,a,b\in T$, \unsure{on a} \unsure{$a,b$}} $P_2
```

Aligned final span:

```tex
admissible
```

Final context (up to 100 characters either side):

```tex
$,
pour $I\in S$].

\deleted{\unsure{b)}} Une partie \uline{finie} \inserted{$T$} est dite \deleted{admissible} \inserted{``\uline{modérée}''}
si \deleted{$\forall\,a,b\in T$, \unsure{on a} $a,b$} $P_2(T)\subse
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/002_b.jpg

Alignment requires recheck: no flag

Review note: Admissible, a comma b, full éléments, cancelled des and the two 2s around à can be read.

### C-002-U032 (C line 38)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 40.

Source C token:

```tex
\unsure{on a}
```

Source C context:

```tex
 dite \deleted{\unsure{admissible}} \inserted{``\uline{modérée}''}
si \deleted{$\forall\,a,b\in T$, \unsure{on a} \unsure{$a,b$}} $P_2(T)\subset S_0$
i.e. deux \unsure{éléments|élémts|elements} quelc. de $T$ sont 
```

Aligned final span:

```tex
\unsure{on a}
```

Final context (up to 100 characters either side):

```tex
{$T$} est dite \deleted{admissible} \inserted{``\uline{modérée}''}
si \deleted{$\forall\,a,b\in T$, \unsure{on a} $a,b$} $P_2(T)\subset S_0$
i.e. deux éléments quelc. de $T$ sont en
position relative modérée (\del
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/002_b.jpg

Alignment requires recheck: no flag

Review note: Scribbled label and crossed on a remain partly covered by cancellation.

### C-002-U033 (C line 38)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 40.

Source C token:

```tex
\unsure{$a,b$}
```

Source C context:

```tex
{\unsure{admissible}} \inserted{``\uline{modérée}''}
si \deleted{$\forall\,a,b\in T$, \unsure{on a} \unsure{$a,b$}} $P_2(T)\subset S_0$
i.e. deux \unsure{éléments|élémts|elements} quelc. de $T$ sont en
position rel
```

Aligned final span:

```tex
$a,b$
```

Final context (up to 100 characters either side):

```tex
 \deleted{admissible} \inserted{``\uline{modérée}''}
si \deleted{$\forall\,a,b\in T$, \unsure{on a} $a,b$} $P_2(T)\subset S_0$
i.e. deux éléments quelc. de $T$ sont en
position relative modérée (\deleted{d
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/002_b.jpg

Alignment requires recheck: no flag

Review note: Admissible, a comma b, full éléments, cancelled des and the two 2s around à can be read.

### C-002-U034 (C line 39)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 41.

Source C token:

```tex
\unsure{éléments|élémts|elements}
```

Source C context:

```tex
ée}''}
si \deleted{$\forall\,a,b\in T$, \unsure{on a} \unsure{$a,b$}} $P_2(T)\subset S_0$
i.e. deux \unsure{éléments|élémts|elements} quelc. de $T$ sont en
position relative modérée (\deleted{\unsure{des}} \unsure{2 st|sont} ``disjoi
```

Aligned final span:

```tex
éléments
```

Final context (up to 100 characters either side):

```tex
ine{modérée}''}
si \deleted{$\forall\,a,b\in T$, \unsure{on a} $a,b$} $P_2(T)\subset S_0$
i.e. deux éléments quelc. de $T$ sont en
position relative modérée (\deleted{des} 2 à 2 ``disjoints'').

% paper water
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/002_b.jpg

Alignment requires recheck: no flag

Review note: Admissible, a comma b, full éléments, cancelled des and the two 2s around à can be read.

### C-002-U035 (C line 40)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 42.

Source C token:

```tex
\unsure{des}
```

Source C context:

```tex
e. deux \unsure{éléments|élémts|elements} quelc. de $T$ sont en
position relative modérée (\deleted{\unsure{des}} \unsure{2 st|sont} ``disjoints'').

% paper watermark
\rotatebox{90}{\textsc{\unsure{x}tra Strong 
```

Aligned final span:

```tex
des}
```

Final context (up to 100 characters either side):

```tex
$} $P_2(T)\subset S_0$
i.e. deux éléments quelc. de $T$ sont en
position relative modérée (\deleted{des} 2 à 2 ``disjoints'').

% paper watermark; faint outline impression
\rotatebox{90}{\textsc{\unsure{x
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/002_b.jpg

Alignment requires recheck: no flag

Review note: Admissible, a comma b, full éléments, cancelled des and the two 2s around à can be read.

### C-002-U036 (C line 40)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 42.

Source C token:

```tex
\unsure{2 st|sont}
```

Source C context:

```tex
e{éléments|élémts|elements} quelc. de $T$ sont en
position relative modérée (\deleted{\unsure{des}} \unsure{2 st|sont} ``disjoints'').

% paper watermark
\rotatebox{90}{\textsc{\unsure{x}tra Strong Ext}}

```

Aligned final span:

```tex
2 à 2
```

Final context (up to 100 characters either side):

```tex
_2(T)\subset S_0$
i.e. deux éléments quelc. de $T$ sont en
position relative modérée (\deleted{des} 2 à 2 ``disjoints'').

% paper watermark; faint outline impression
\rotatebox{90}{\textsc{\unsure{xtra St
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/002_b.jpg

Alignment requires recheck: no flag

Review note: Admissible, a comma b, full éléments, cancelled des and the two 2s around à can be read.

### C-002-U037 (C line 43)

Mechanical state: **unsure token(s) overlap changed alignment; inspect**. Final aligned line: 45.

Source C token:

```tex
\unsure{x}
```

Source C context:

```tex
\deleted{\unsure{des}} \unsure{2 st|sont} ``disjoints'').

% paper watermark
\rotatebox{90}{\textsc{\unsure{x}tra Strong Ext}}

```

Aligned final span:

```tex
\unsure{x
```

Final context (up to 100 characters either side):

```tex
eted{des} 2 à 2 ``disjoints'').

% paper watermark; faint outline impression
\rotatebox{90}{\textsc{\unsure{xtra Strong Ext}}}

```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: revised

Crop links: crops/002_watermark.jpg

Alignment requires recheck: no flag

Review note: Uncertainty applies to the entire faint watermark fragment, not only its initial x.

### C-003-U001 (C line 4)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 4.

Source C token:

```tex
\unsure{implique}
```

Source C context:

```tex
\scanpage{3}
\mspage{2}

\deleted{De plus, on veut que la structure \unsure{implique}}

\deleted{\textcircled{\scriptsize b}\quad $\forall\,T\in\unsure{P|\mathcal P}_{f\,\mathrm{mod}}(\
```

Aligned final span:

```tex
implique
```

Final context (up to 100 characters either side):

```tex
\scanpage{3}
\mspage{2}

\deleted{De plus, on veut que la structure implique}

\deleted{\textcircled{\scriptsize b}\quad $\forall\,T\in P_{f\,\mathrm{mod}}(\mathcal L)$, on se 
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/003_cancel.jpg

Alignment requires recheck: no flag

Review note: The cancelled opening retains legible implique, single-staff P, looped L and ordinary R; cancellation does not conceal these forms.

### C-003-U002 (C line 6)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 6.

Source C token:

```tex
\unsure{P|\mathcal P}
```

Source C context:

```tex
n veut que la structure \unsure{implique}}

\deleted{\textcircled{\scriptsize b}\quad $\forall\,T\in\unsure{P|\mathcal P}_{f\,\mathrm{mod}}(\unsure{\mathcal L|L})$, on se donne une
relation d'équivalence $\unsure{\mathcal
```

Aligned final span:

```tex
 P
```

Final context (up to 100 characters either side):

```tex
e plus, on veut que la structure implique}

\deleted{\textcircled{\scriptsize b}\quad $\forall\,T\in P_{f\,\mathrm{mod}}(\mathcal L)$, on se donne une
relation d'équivalence $R_T$ dans l'ens
\unsure{où}
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/003_cancel.jpg

Alignment requires recheck: no flag

Review note: The cancelled opening retains legible implique, single-staff P, looped L and ordinary R; cancellation does not conceal these forms. Alignment recheck: A TeX command delimiter space was added; the image-reviewed plain P is unchanged.

### C-003-U003 (C line 6)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 6.

Source C token:

```tex
\unsure{\mathcal L|L}
```

Source C context:

```tex
}}

\deleted{\textcircled{\scriptsize b}\quad $\forall\,T\in\unsure{P|\mathcal P}_{f\,\mathrm{mod}}(\unsure{\mathcal L|L})$, on se donne une
relation d'équivalence $\unsure{\mathcal R|R}_T$ dans l'ens
\unsure{où}}

Si $T$
```

Aligned final span:

```tex
\mathcal L
```

Final context (up to 100 characters either side):

```tex
a structure implique}

\deleted{\textcircled{\scriptsize b}\quad $\forall\,T\in P_{f\,\mathrm{mod}}(\mathcal L)$, on se donne une
relation d'équivalence $R_T$ dans l'ens
\unsure{où}}

Si $T$ est une partie fini
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/003_cancel.jpg

Alignment requires recheck: no flag

Review note: The cancelled opening retains legible implique, single-staff P, looped L and ordinary R; cancellation does not conceal these forms.

### C-003-U004 (C line 7)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 7.

Source C token:

```tex
\unsure{\mathcal R|R}
```

Source C context:

```tex
re{P|\mathcal P}_{f\,\mathrm{mod}}(\unsure{\mathcal L|L})$, on se donne une
relation d'équivalence $\unsure{\mathcal R|R}_T$ dans l'ens
\unsure{où}}

Si $T$ est une partie finie
modérée\unsure{,|;}, on \deleted{\unsure{dé
```

Aligned final span:

```tex
R
```

Final context (up to 100 characters either side):

```tex
ze b}\quad $\forall\,T\in P_{f\,\mathrm{mod}}(\mathcal L)$, on se donne une
relation d'équivalence $R_T$ dans l'ens
\unsure{où}}

Si $T$ est une partie finie
modérée\unsure{,|;}, on \deleted{\unsure{dé
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/003_cancel.jpg

Alignment requires recheck: no flag

Review note: The cancelled opening retains legible implique, single-staff P, looped L and ordinary R; cancellation does not conceal these forms.

### C-003-U005 (C line 8)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 8.

Source C token:

```tex
\unsure{où}
```

Source C context:

```tex
unsure{\mathcal L|L})$, on se donne une
relation d'équivalence $\unsure{\mathcal R|R}_T$ dans l'ens
\unsure{où}}

Si $T$ est une partie finie
modérée\unsure{,|;}, on \deleted{\unsure{désignera|désigne} par} \ins
```

Aligned final span:

```tex
\unsure{où}
```

Final context (up to 100 characters either side):

```tex
all\,T\in P_{f\,\mathrm{mod}}(\mathcal L)$, on se donne une
relation d'équivalence $R_T$ dans l'ens
\unsure{où}}

Si $T$ est une partie finie
modérée\unsure{,|;}, on \deleted{\unsure{désignera|désigne} par} \ins
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/003_cancel.jpg

Alignment requires recheck: no flag

Review note: The clipped final short group remains doubtful.

### C-003-U006 (C line 11)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 11.

Source C token:

```tex
\unsure{,|;}
```

Source C context:

```tex
d'équivalence $\unsure{\mathcal R|R}_T$ dans l'ens
\unsure{où}}

Si $T$ est une partie finie
modérée\unsure{,|;}, on \deleted{\unsure{désignera|désigne} par} \inserted{pose}

\[
 C\deleted{\unsure{\mathrm{omp}^{r
```

Aligned final span:

```tex
\unsure{,|;}
```

Final context (up to 100 characters either side):

```tex
 donne une
relation d'équivalence $R_T$ dans l'ens
\unsure{où}}

Si $T$ est une partie finie
modérée\unsure{,|;}, on \deleted{\unsure{désignera|désigne} par} \inserted{pose}

\[
 C\deleted{\unsure{\mathrm{omp}^{r
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty after final crop recheck

Crop links: crops/003_def.jpg

Alignment requires recheck: no

Review note: The first descending punctuation mark has a nearby upper point of uncertain attachment; comma/semicolon remains unresolved before the second comma. Earlier removal of the doubt was reversed before freeze.

### C-003-U007 (C line 11)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 11.

Source C token:

```tex
\unsure{désignera|désigne}
```

Source C context:

```tex
thcal R|R}_T$ dans l'ens
\unsure{où}}

Si $T$ est une partie finie
modérée\unsure{,|;}, on \deleted{\unsure{désignera|désigne} par} \inserted{pose}

\[
 C\deleted{\unsure{\mathrm{omp}^{r}|\mathrm{omp}}}_{\mathcal L}(T)=
 \{\,t
```

Aligned final span:

```tex
\unsure{désignera|désigne}
```

Final context (up to 100 characters either side):

```tex
valence $R_T$ dans l'ens
\unsure{où}}

Si $T$ est une partie finie
modérée\unsure{,|;}, on \deleted{\unsure{désignera|désigne} par} \inserted{pose}

\[
 C\deleted{\unsure{\mathrm{omp}^{r}|\mathrm{omp}}}_{\mathcal L}(T)=
 \{\,t
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/003_def.jpg

Alignment requires recheck: no flag

Review note: Crossed verb, old Comp superscript and the compressed final gender ending remain uncertain.

### C-003-U008 (C line 14)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 14.

Source C token:

```tex
\unsure{\mathrm{omp}^{r}|\mathrm{omp}}
```

Source C context:

```tex
nie
modérée\unsure{,|;}, on \deleted{\unsure{désignera|désigne} par} \inserted{pose}

\[
 C\deleted{\unsure{\mathrm{omp}^{r}|\mathrm{omp}}}_{\mathcal L}(T)=
 \{\,t\in\mathcal L\setminus T\mid \{T\cup\{t\}\}\ \text{\unsure{modéré|modérée}}
```

Aligned final span:

```tex
\unsure{\mathrm{omp}^{r}|\mathrm{omp}}
```

Final context (up to 100 characters either side):

```tex
nie
modérée\unsure{,|;}, on \deleted{\unsure{désignera|désigne} par} \inserted{pose}

\[
 C\deleted{\unsure{\mathrm{omp}^{r}|\mathrm{omp}}}_{\mathcal L}(T)=
 \{\,t\in\mathcal L\setminus T\mid \{T\cup\{t\}\}\ \text{\unsure{modéré|modérée}}
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/003_def.jpg

Alignment requires recheck: no flag

Review note: Crossed verb, old Comp superscript and the compressed final gender ending remain uncertain.

### C-003-U009 (C line 15)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 15.

Source C token:

```tex
\unsure{modéré|modérée}
```

Source C context:

```tex
m{omp}^{r}|\mathrm{omp}}}_{\mathcal L}(T)=
 \{\,t\in\mathcal L\setminus T\mid \{T\cup\{t\}\}\ \text{\unsure{modéré|modérée}}\,\}
\]

% slanted
\margin{\uline{le complémentaire} \uline{modéré} de $T$.
Question : $T$ est-il c
```

Aligned final span:

```tex
\unsure{modéré|modérée}
```

Final context (up to 100 characters either side):

```tex
m{omp}^{r}|\mathrm{omp}}}_{\mathcal L}(T)=
 \{\,t\in\mathcal L\setminus T\mid \{T\cup\{t\}\}\ \text{\unsure{modéré|modérée}}\,\}
\]

% slanted
\margin{\uline{le complémentaire} \uline{modéré} de $T$.
Question : $T$ est-il c
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/003_def.jpg

Alignment requires recheck: no flag

Review note: Crossed verb, old Comp superscript and the compressed final gender ending remain uncertain.

### C-003-U010 (C line 20)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 20.

Source C token:

```tex
\unsure{connait|connaît}
```

Source C context:

```tex
anted
\margin{\uline{le complémentaire} \uline{modéré} de $T$.
Question : $T$ est-il connu quand on \unsure{connait|connaît} $C_{\mathcal L}(T)$ ? Plus précisément,
si $T'\subset T$, on a $C(T)\subset C(T')$, l'inverse est-i
```

Aligned final span:

```tex
\unsure{connait|connaît}
```

Final context (up to 100 characters either side):

```tex
anted
\margin{\uline{le complémentaire} \uline{modéré} de $T$.
Question : $T$ est-il connu quand on \unsure{connait|connaît} $C_{\mathcal L}(T)$ ? Plus précisément,
si $T'\subset T$, on a $C(T)\subset C(T')$, l'inverse est-i
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/003_margin.jpg

Alignment requires recheck: no flag

Review note: Rotated marginal question is readable but accent and the crossed proof fragments are not securely recoverable.

### C-003-U011 (C line 22)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 22.

Source C token:

```tex
\unsure{$t$ est gén.}
```

Source C context:

```tex
(T)\subset C(T')$, l'inverse est-il vrai ? Oui,
Donc, si \inserted{$t\in T'$} $t\notin T$, \deleted{\unsure{$t$ est gén.} \unsure{tel} ($T\cup\{t\}$ modéré) \unsure{puisque} \unsure{on a toujours} \unsure{$s\notin T$,}} a
```

Aligned final span:

```tex
\unsure{$t$ est gén.}
```

Final context (up to 100 characters either side):

```tex
(T)\subset C(T')$, l'inverse est-il vrai ? Oui,
Donc, si \inserted{$t\in T'$} $t\notin T$, \deleted{\unsure{$t$ est gén.} \unsure{tel} ($T\cup\{t\}$ modéré) \unsure{puisque} \unsure{on a toujours} \unsure{$s\notin T$,}} a
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/003_margin.jpg

Alignment requires recheck: no flag

Review note: Rotated marginal question is readable but accent and the crossed proof fragments are not securely recoverable.

### C-003-U012 (C line 22)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 22.

Source C token:

```tex
\unsure{tel}
```

Source C context:

```tex
nverse est-il vrai ? Oui,
Donc, si \inserted{$t\in T'$} $t\notin T$, \deleted{\unsure{$t$ est gén.} \unsure{tel} ($T\cup\{t\}$ modéré) \unsure{puisque} \unsure{on a toujours} \unsure{$s\notin T$,}} alors $t\in C(
```

Aligned final span:

```tex
\unsure{tel}
```

Final context (up to 100 characters either side):

```tex
nverse est-il vrai ? Oui,
Donc, si \inserted{$t\in T'$} $t\notin T$, \deleted{\unsure{$t$ est gén.} \unsure{tel} ($T\cup\{t\}$ modéré) \unsure{puisque} \unsure{on a toujours} \unsure{$s\notin T$,}} alors $t\in C(
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/003_margin.jpg

Alignment requires recheck: no flag

Review note: Rotated marginal question is readable but accent and the crossed proof fragments are not securely recoverable.

### C-003-U013 (C line 22)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 22.

Source C token:

```tex
\unsure{puisque}
```

Source C context:

```tex
\inserted{$t\in T'$} $t\notin T$, \deleted{\unsure{$t$ est gén.} \unsure{tel} ($T\cup\{t\}$ modéré) \unsure{puisque} \unsure{on a toujours} \unsure{$s\notin T$,}} alors $t\in C(T)$ et $t\notin C(T')$}

\unsure{ou mie
```

Aligned final span:

```tex
\unsure{puisque}
```

Final context (up to 100 characters either side):

```tex
\inserted{$t\in T'$} $t\notin T$, \deleted{\unsure{$t$ est gén.} \unsure{tel} ($T\cup\{t\}$ modéré) \unsure{puisque} \unsure{on a toujours} \unsure{$s\notin T$,}} alors $t\in C(T)$ et $t\notin C(T')$}

ou mieux, l'en
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/003_margin.jpg

Alignment requires recheck: no flag

Review note: Rotated marginal question is readable but accent and the crossed proof fragments are not securely recoverable.

### C-003-U014 (C line 22)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 22.

Source C token:

```tex
\unsure{on a toujours}
```

Source C context:

```tex
'$} $t\notin T$, \deleted{\unsure{$t$ est gén.} \unsure{tel} ($T\cup\{t\}$ modéré) \unsure{puisque} \unsure{on a toujours} \unsure{$s\notin T$,}} alors $t\in C(T)$ et $t\notin C(T')$}

\unsure{ou mieux|ou même}, l'ens des 
```

Aligned final span:

```tex
\unsure{on a toujours}
```

Final context (up to 100 characters either side):

```tex
'$} $t\notin T$, \deleted{\unsure{$t$ est gén.} \unsure{tel} ($T\cup\{t\}$ modéré) \unsure{puisque} \unsure{on a toujours} \unsure{$s\notin T$,}} alors $t\in C(T)$ et $t\notin C(T')$}

ou mieux, l'ens des $t\in L\setminus 
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/003_margin.jpg

Alignment requires recheck: no flag

Review note: Rotated marginal question is readable but accent and the crossed proof fragments are not securely recoverable.

### C-003-U015 (C line 22)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 22.

Source C token:

```tex
\unsure{$s\notin T$,}
```

Source C context:

```tex
ed{\unsure{$t$ est gén.} \unsure{tel} ($T\cup\{t\}$ modéré) \unsure{puisque} \unsure{on a toujours} \unsure{$s\notin T$,}} alors $t\in C(T)$ et $t\notin C(T')$}

\unsure{ou mieux|ou même}, l'ens des $t\in L\setminus T$ en
```

Aligned final span:

```tex
\unsure{$s\notin T$,}
```

Final context (up to 100 characters either side):

```tex
ed{\unsure{$t$ est gén.} \unsure{tel} ($T\cup\{t\}$ modéré) \unsure{puisque} \unsure{on a toujours} \unsure{$s\notin T$,}} alors $t\in C(T)$ et $t\notin C(T')$}

ou mieux, l'ens des $t\in L\setminus T$ en
position modérée
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/003_margin.jpg

Alignment requires recheck: no flag

Review note: Rotated marginal question is readable but accent and the crossed proof fragments are not securely recoverable.

### C-003-U016 (C line 24)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 24.

Source C token:

```tex
\unsure{ou mieux|ou même}
```

Source C context:

```tex
nsure{puisque} \unsure{on a toujours} \unsure{$s\notin T$,}} alors $t\in C(T)$ et $t\notin C(T')$}

\unsure{ou mieux|ou même}, l'ens des $t\in L\setminus T$ en
position modérée p.r. à $T$.

[\uline{NB}\quad deux parties finie
```

Aligned final span:

```tex
ou mieux
```

Final context (up to 100 characters either side):

```tex
nsure{puisque} \unsure{on a toujours} \unsure{$s\notin T$,}} alors $t\in C(T)$ et $t\notin C(T')$}

ou mieux, l'ens des $t\in L\setminus T$ en
position modérée p.r. à $T$.

[\uline{NB}\quad deux parties finie
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/003_bracket.jpg

Alignment requires recheck: no flag

Review note: Ou mieux, the small hyphen in leur-réunion, and the comma after the old si are distinguishable.

### C-003-U017 (C line 29)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 29.

Source C token:

```tex
\unsure{-| }
```

Source C context:

```tex
 $T$.

[\uline{NB}\quad deux parties finies modérées
sont dites en position relative
modérée si leur\unsure{-| }réunion est
modérée ; $t$ est dit en pos. rel.
modérée p.r. à $T$ si $\{t\}$ l'est ;
$s$ et $t$ sont
```

Aligned final span:

```tex
-
```

Final context (up to 100 characters either side):

```tex
 $T$.

[\uline{NB}\quad deux parties finies modérées
sont dites en position relative
modérée si leur-réunion est
modérée ; $t$ est dit en pos. rel.
modérée p.r. à $T$ si $\{t\}$ l'est ;
$s$ et $t$ sont
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/003_bracket.jpg

Alignment requires recheck: no flag

Review note: Ou mieux, the small hyphen in leur-réunion, and the comma after the old si are distinguishable.

### C-003-U018 (C line 33)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 33.

Source C token:

```tex
\unsure{si}
```

Source C context:

```tex
 si $\{t\}$ l'est ;
$s$ et $t$ sont dits en pos. rel. modérée
si $\{s,t\}$ est modéré i.e. \deleted{\unsure{si}}\unsure{,}
$s\ne t$ ou $\{s;t\}\in S_0$ \ldots\ ]

% slanted
\margin{\uline{NB} $T$\deleted{\unsure
```

Aligned final span:

```tex
\unsure{si}
```

Final context (up to 100 characters either side):

```tex
 si $\{t\}$ l'est ;
$s$ et $t$ sont dits en pos. rel. modérée
si $\{s,t\}$ est modéré i.e. \deleted{\unsure{si}},
$s\ne t$ ou $\{s;t\}\in S_0$ \ldots\ ]

% slanted
\margin{\uline{NB} $T$\deleted{\unsure{est}} es
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/003_bracket.jpg

Alignment requires recheck: no flag

Review note: Short crossed word remains a plausible si, not securely legible.

### C-003-U019 (C line 33)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 33.

Source C token:

```tex
\unsure{,}
```

Source C context:

```tex
l'est ;
$s$ et $t$ sont dits en pos. rel. modérée
si $\{s,t\}$ est modéré i.e. \deleted{\unsure{si}}\unsure{,}
$s\ne t$ ou $\{s;t\}\in S_0$ \ldots\ ]

% slanted
\margin{\uline{NB} $T$\deleted{\unsure{est}} est 
```

Aligned final span:

```tex
,
```

Final context (up to 100 characters either side):

```tex
l'est ;
$s$ et $t$ sont dits en pos. rel. modérée
si $\{s,t\}$ est modéré i.e. \deleted{\unsure{si}},
$s\ne t$ ou $\{s;t\}\in S_0$ \ldots\ ]

% slanted
\margin{\uline{NB} $T$\deleted{\unsure{est}} est 
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/003_bracket.jpg

Alignment requires recheck: no flag

Review note: Ou mieux, the small hyphen in leur-réunion, and the comma after the old si are distinguishable.

### C-003-U020 (C line 37)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 37.

Source C token:

```tex
\unsure{est}
```

Source C context:

```tex
ure{si}}\unsure{,}
$s\ne t$ ou $\{s;t\}\in S_0$ \ldots\ ]

% slanted
\margin{\uline{NB} $T$\deleted{\unsure{est}} est connu quand on \unsure{connait|connaît} $C(T)$}

\textcircled{\scriptsize b}\quad $\forall\,T\
```

Aligned final span:

```tex
\unsure{est}
```

Final context (up to 100 characters either side):

```tex
eted{\unsure{si}},
$s\ne t$ ou $\{s;t\}\in S_0$ \ldots\ ]

% slanted
\margin{\uline{NB} $T$\deleted{\unsure{est}} est connu quand on \unsure{connait|connaît} $C(T)$}

\textcircled{\scriptsize b}\quad $\forall\,T\
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/003_bottom.jpg

Alignment requires recheck: no flag

Review note: Crossed est, connaître accent, tiny subscript-like mark and closing curved sign remain unresolved.

### C-003-U021 (C line 37)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 37.

Source C token:

```tex
\unsure{connait|connaît}
```

Source C context:

```tex
{s;t\}\in S_0$ \ldots\ ]

% slanted
\margin{\uline{NB} $T$\deleted{\unsure{est}} est connu quand on \unsure{connait|connaît} $C(T)$}

\textcircled{\scriptsize b}\quad $\forall\,T\in\underbrace{\mathrm{Mod}_{f}}_{\substack{\t
```

Aligned final span:

```tex
\unsure{connait|connaît}
```

Final context (up to 100 characters either side):

```tex
{s;t\}\in S_0$ \ldots\ ]

% slanted
\margin{\uline{NB} $T$\deleted{\unsure{est}} est connu quand on \unsure{connait|connaît} $C(T)$}

\textcircled{\scriptsize b}\quad $\forall\,T\in\underbrace{\mathrm{Modf}}_{\substack{\text
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/003_bottom.jpg

Alignment requires recheck: no flag

Review note: Crossed est, connaître accent, tiny subscript-like mark and closing curved sign remain unresolved.

### C-003-U022 (C line 39)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 39.

Source C token:

```tex
\unsure{.|}
```

Source C context:

```tex
circled{\scriptsize b}\quad $\forall\,T\in\underbrace{\mathrm{Mod}_{f}}_{\substack{\text{parties mod\unsure{.|}}\\\text{finies}}}(\mathcal L)$, une relation
d'équivalence $\mathcal R_T$ dans $C_{\unsure{\checkma
```

Aligned final span:

```tex

```

Final context (up to 100 characters either side):

```tex
extcircled{\scriptsize b}\quad $\forall\,T\in\underbrace{\mathrm{Modf}}_{\substack{\text{parties mod}\\\text{finies}}}(\mathcal L)$, une relation
d'équivalence $R_T$ dans $C_{\unsure{\checkmark|\mathc
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/003_bottom.jpg

Alignment requires recheck: no flag

Review note: No separate point follows mod in the handwritten explanatory label.

### C-003-U023 (C line 40)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 40.

Source C token:

```tex
\unsure{\checkmark|\mathcal L|}
```

Source C context:

```tex
s mod\unsure{.|}}\\\text{finies}}}(\mathcal L)$, une relation
d'équivalence $\mathcal R_T$ dans $C_{\unsure{\checkmark|\mathcal L|}}(T\unsure{)|\}}$ (dont
les classes s'appellent les \uline{comp. connexes} \inserted{de $C(T)$}

% p
```

Aligned final span:

```tex
\unsure{\checkmark|\mathcal L|}
```

Final context (up to 100 characters either side):

```tex
ubstack{\text{parties mod}\\\text{finies}}}(\mathcal L)$, une relation
d'équivalence $R_T$ dans $C_{\unsure{\checkmark|\mathcal L|}}(T\unsure{)|\}}$ (dont
les classes s'appellent les \uline{comp. connexes} \inserted{de $C(T)$}

% p
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/003_bottom.jpg

Alignment requires recheck: no flag

Review note: Crossed est, connaître accent, tiny subscript-like mark and closing curved sign remain unresolved.

### C-003-U024 (C line 40)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 40.

Source C token:

```tex
\unsure{)|\}}
```

Source C context:

```tex
(\mathcal L)$, une relation
d'équivalence $\mathcal R_T$ dans $C_{\unsure{\checkmark|\mathcal L|}}(T\unsure{)|\}}$ (dont
les classes s'appellent les \uline{comp. connexes} \inserted{de $C(T)$}

% paper watermark, 
```

Aligned final span:

```tex
\unsure{)|\}}
```

Final context (up to 100 characters either side):

```tex
finies}}}(\mathcal L)$, une relation
d'équivalence $R_T$ dans $C_{\unsure{\checkmark|\mathcal L|}}(T\unsure{)|\}}$ (dont
les classes s'appellent les \uline{comp. connexes} \inserted{de $C(T)$}

% paper watermark, 
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/003_bottom.jpg

Alignment requires recheck: no flag

Review note: Crossed est, connaître accent, tiny subscript-like mark and closing curved sign remain unresolved.

### C-003-U025 (C line 44)

Mechanical state: **unsure token(s) overlap changed alignment; inspect**. Final aligned line: 44.

Source C token:

```tex
\unsure{x}
```

Source C context:

```tex
 connexes} \inserted{de $C(T)$}

% paper watermark, visible from the reverse
\rotatebox{90}{\textsc{\unsure{x}tra Strong Ext}}

```

Aligned final span:

```tex
\unsure{x
```

Final context (up to 100 characters either side):

```tex
 connexes} \inserted{de $C(T)$}

% paper watermark, visible from the reverse
\rotatebox{90}{\textsc{\unsure{xtra Strong Ext}}}

```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: revised

Crop links: crops/003_watermark.jpg

Alignment requires recheck: no flag

Review note: Faint outlined watermark fragment is wholly doubtful; no certainty transferred from another page.

### C-004-U001 (C line 4)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 4.

Source C token:

```tex
\unsure{\mathcal L|L}
```

Source C context:

```tex
\scanpage{4}
\mspage{3}

\textcircled{\scriptsize c}\quad $\forall\,T\in\mathrm{Mod}_{f}(\unsure{\mathcal L|L})$, et $A\in C(T)/\unsure{R|\mathcal R}_T$
une classe suivant $R_T$, une partie
\unsure{de} $\dot A\
```

Aligned final span:

```tex
\mathcal L
```

Final context (up to 100 characters either side):

```tex
\scanpage{4}
\mspage{3}

\textcircled{\scriptsize c}\quad $\forall\,T\in\mathrm{Modf}(\mathcal L)$, et $A\in C(T)/R_T$
une classe suivant $R_T$, une partie
de $\dot A\subset T$, appelée \uline{fro
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/004_top.jpg

Alignment requires recheck: no flag

Review note: Script L, ordinary R, the extra de and initial Ces are visible; the surplus de is preserved despite the syntax.

### C-004-U002 (C line 4)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 4.

Source C token:

```tex
\unsure{R|\mathcal R}
```

Source C context:

```tex
xtcircled{\scriptsize c}\quad $\forall\,T\in\mathrm{Mod}_{f}(\unsure{\mathcal L|L})$, et $A\in C(T)/\unsure{R|\mathcal R}_T$
une classe suivant $R_T$, une partie
\unsure{de} $\dot A\subset T$, appelée \uline{frontière} de
```

Aligned final span:

```tex
R
```

Final context (up to 100 characters either side):

```tex
mspage{3}

\textcircled{\scriptsize c}\quad $\forall\,T\in\mathrm{Modf}(\mathcal L)$, et $A\in C(T)/R_T$
une classe suivant $R_T$, une partie
de $\dot A\subset T$, appelée \uline{frontière} de $A$.

Ce
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/004_top.jpg

Alignment requires recheck: no flag

Review note: Script L, ordinary R, the extra de and initial Ces are visible; the surplus de is preserved despite the syntax.

### C-004-U003 (C line 6)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 6.

Source C token:

```tex
\unsure{de}
```

Source C context:

```tex
unsure{\mathcal L|L})$, et $A\in C(T)/\unsure{R|\mathcal R}_T$
une classe suivant $R_T$, une partie
\unsure{de} $\dot A\subset T$, appelée \uline{frontière} de $A$.

\unsure{Ces|Les} données \textcircled{\script
```

Aligned final span:

```tex
de
```

Final context (up to 100 characters either side):

```tex
d $\forall\,T\in\mathrm{Modf}(\mathcal L)$, et $A\in C(T)/R_T$
une classe suivant $R_T$, une partie
de $\dot A\subset T$, appelée \uline{frontière} de $A$.

Ces données \textcircled{\scriptsize a} \text
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/004_top.jpg

Alignment requires recheck: no flag

Review note: Script L, ordinary R, the extra de and initial Ces are visible; the surplus de is preserved despite the syntax.

### C-004-U004 (C line 8)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 8.

Source C token:

```tex
\unsure{Ces|Les}
```

Source C context:

```tex
 classe suivant $R_T$, une partie
\unsure{de} $\dot A\subset T$, appelée \uline{frontière} de $A$.

\unsure{Ces|Les} données \textcircled{\scriptsize a} \textcircled{\scriptsize b}, \textcircled{\scriptsize c} étant 
```

Aligned final span:

```tex
Ces
```

Final context (up to 100 characters either side):

```tex
/R_T$
une classe suivant $R_T$, une partie
de $\dot A\subset T$, appelée \uline{frontière} de $A$.

Ces données \textcircled{\scriptsize a} \textcircled{\scriptsize b}, \textcircled{\scriptsize c} étant 
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/004_top.jpg

Alignment requires recheck: no flag

Review note: Script L, ordinary R, the extra de and initial Ces are visible; the surplus de is preserved despite the syntax.

### C-004-U005 (C line 8)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 8.

Source C token:

```tex
\unsure{assujetties}
```

Source C context:

```tex
 données \textcircled{\scriptsize a} \textcircled{\scriptsize b}, \textcircled{\scriptsize c} étant \unsure{assujetties}
à satisfaire certains axiomes.

Je prévois que les axiomes impliquent
\deleted{Soit \illegible{1} $
```

Aligned final span:

```tex
\unsure{assujetties}
```

Final context (up to 100 characters either side):

```tex
 données \textcircled{\scriptsize a} \textcircled{\scriptsize b}, \textcircled{\scriptsize c} étant \unsure{assujetties}
à satisfaire certains axiomes.

Je prévois que les axiomes impliquent
\deleted{Soit \illegible{1} $
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/004_top.jpg

Alignment requires recheck: no flag

Review note: Far-right clipped assujetties and crossed start remain incompletely legible.

### C-004-U006 (C line 12)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 12.

Source C token:

```tex
\unsure{t|U}
```

Source C context:

```tex

à satisfaire certains axiomes.

Je prévois que les axiomes impliquent
\deleted{Soit \illegible{1} $\unsure{t|U}\in C(T)$, \unsure{on pose}}
ceci

1°) que la donnée \textcircled{\scriptsize c} résulte déjà de \te
```

Aligned final span:

```tex
\unsure{t|U}
```

Final context (up to 100 characters either side):

```tex

à satisfaire certains axiomes.

Je prévois que les axiomes impliquent
\deleted{Soit \illegible{1} $\unsure{t|U}\in C(T)$, \unsure{on pose}}
ceci

1°) que la donnée \textcircled{\scriptsize c} résulte déjà de \te
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/004_top.jpg

Alignment requires recheck: no flag

Review note: Far-right clipped assujetties and crossed start remain incompletely legible.

### C-004-U007 (C line 12)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 12.

Source C token:

```tex
\unsure{on pose}
```

Source C context:

```tex
axiomes.

Je prévois que les axiomes impliquent
\deleted{Soit \illegible{1} $\unsure{t|U}\in C(T)$, \unsure{on pose}}
ceci

1°) que la donnée \textcircled{\scriptsize c} résulte déjà de \textcircled{\scriptsize b}

2
```

Aligned final span:

```tex
\unsure{on pose}
```

Final context (up to 100 characters either side):

```tex
axiomes.

Je prévois que les axiomes impliquent
\deleted{Soit \illegible{1} $\unsure{t|U}\in C(T)$, \unsure{on pose}}
ceci

1°) que la donnée \textcircled{\scriptsize c} résulte déjà de \textcircled{\scriptsize b}

2
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/004_top.jpg

Alignment requires recheck: no flag

Review note: Far-right clipped assujetties and crossed start remain incompletely legible.

### C-004-U008 (C line 18)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 18.

Source C token:

```tex
\unsure{pour}
```

Source C context:

```tex
riptsize b}

2°) que la donnée \textcircled{\scriptsize b} résulte de
la donnée des $R_T$, \deleted{\unsure{pour}} dans le cas
particulier où $T\in S_0$. Donc
les seules \unsure{donnée|données} essentielles \unsur
```

Aligned final span:

```tex
\unsure{pour}
```

Final context (up to 100 characters either side):

```tex
riptsize b}

2°) que la donnée \textcircled{\scriptsize b} résulte de
la donnée des $R_T$, \deleted{\unsure{pour}} dans le cas
particulier où $T\in S_0$. Donc
les seules \unsure{donnée|données} essentielles \unsur
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/004_middle.jpg

Alignment requires recheck: no flag

Review note: Cancelled pour and compressed singular/plural endings remain doubtful.

### C-004-U009 (C line 20)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 20.

Source C token:

```tex
\unsure{donnée|données}
```

Source C context:

```tex
la donnée des $R_T$, \deleted{\unsure{pour}} dans le cas
particulier où $T\in S_0$. Donc
les seules \unsure{donnée|données} essentielles \unsure{serait|seraient}
\textcircled{\scriptsize a} \unsure{celles|celle} des 0-sphèr
```

Aligned final span:

```tex
\unsure{donnée|données}
```

Final context (up to 100 characters either side):

```tex
la donnée des $R_T$, \deleted{\unsure{pour}} dans le cas
particulier où $T\in S_0$. Donc
les seules \unsure{donnée|données} essentielles \unsure{serait|seraient}
\textcircled{\scriptsize a} \unsure{celles|celle} des 0-sphèr
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/004_middle.jpg

Alignment requires recheck: no flag

Review note: Cancelled pour and compressed singular/plural endings remain doubtful.

### C-004-U010 (C line 20)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 20.

Source C token:

```tex
\unsure{serait|seraient}
```

Source C context:

```tex
{pour}} dans le cas
particulier où $T\in S_0$. Donc
les seules \unsure{donnée|données} essentielles \unsure{serait|seraient}
\textcircled{\scriptsize a} \unsure{celles|celle} des 0-sphères i.e. la notion
de \deleted{\unsure{
```

Aligned final span:

```tex
\unsure{serait|seraient}
```

Final context (up to 100 characters either side):

```tex
{pour}} dans le cas
particulier où $T\in S_0$. Donc
les seules \unsure{donnée|données} essentielles \unsure{serait|seraient}
\textcircled{\scriptsize a} \unsure{celles|celle} des 0-sphères i.e. la notion
de \deleted{pos.} li
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/004_middle.jpg

Alignment requires recheck: no flag

Review note: Cancelled pour and compressed singular/plural endings remain doubtful.

### C-004-U011 (C line 21)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 21.

Source C token:

```tex
\unsure{celles|celle}
```

Source C context:

```tex
es seules \unsure{donnée|données} essentielles \unsure{serait|seraient}
\textcircled{\scriptsize a} \unsure{celles|celle} des 0-sphères i.e. la notion
de \deleted{\unsure{pos.}} lieux en pos. relative modérée
(\unsure{rel
```

Aligned final span:

```tex
\unsure{celles|celle}
```

Final context (up to 100 characters either side):

```tex
es seules \unsure{donnée|données} essentielles \unsure{serait|seraient}
\textcircled{\scriptsize a} \unsure{celles|celle} des 0-sphères i.e. la notion
de \deleted{pos.} lieux en pos. relative modérée
(condition \inserted{
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/004_middle.jpg

Alignment requires recheck: no flag

Review note: Cancelled pour and compressed singular/plural endings remain doubtful.

### C-004-U012 (C line 22)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 22.

Source C token:

```tex
\unsure{pos.}
```

Source C context:

```tex
eraient}
\textcircled{\scriptsize a} \unsure{celles|celle} des 0-sphères i.e. la notion
de \deleted{\unsure{pos.}} lieux en pos. relative modérée
(\unsure{relation|condition} \inserted{réflexive et} symétrique) et
```

Aligned final span:

```tex
pos.
```

Final context (up to 100 characters either side):

```tex
eraient}
\textcircled{\scriptsize a} \unsure{celles|celle} des 0-sphères i.e. la notion
de \deleted{pos.} lieux en pos. relative modérée
(condition \inserted{réflexive et} symétrique) et \textcircled{\scr
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/004_middle.jpg

Alignment requires recheck: no flag

Review note: Crossed pos. and live condition can be distinguished.

### C-004-U013 (C line 23)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 23.

Source C token:

```tex
\unsure{relation|condition}
```

Source C context:

```tex
lles|celle} des 0-sphères i.e. la notion
de \deleted{\unsure{pos.}} lieux en pos. relative modérée
(\unsure{relation|condition} \inserted{réflexive et} symétrique) et \textcircled{\scriptsize b} La donnée,
pour \deleted{\unsure
```

Aligned final span:

```tex
condition
```

Final context (up to 100 characters either side):

```tex
unsure{celles|celle} des 0-sphères i.e. la notion
de \deleted{pos.} lieux en pos. relative modérée
(condition \inserted{réflexive et} symétrique) et \textcircled{\scriptsize b} La donnée,
pour \figure{\begin{t
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/004_middle.jpg

Alignment requires recheck: no flag

Review note: Crossed pos. and live condition can be distinguished.

### C-004-U014 (C line 24)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 24.

Source C token:

```tex
\unsure{tout}
```

Source C context:

```tex
dition} \inserted{réflexive et} symétrique) et \textcircled{\scriptsize b} La donnée,
pour \deleted{\unsure{tout}} $\unsure{\varepsilon|\epsilon|E}\in S_0$, de la relation
d'équivalence $R_{\varepsilon}$ \unsure{d
```

Aligned final span:

```tex
figure{\begin{tikzpicture}[x=1cm,y=1cm,baseline=-.4ex]
\draw (0,.12)--(.03,-.18) (0.07,.10)--(.09,-.16);
\draw (.90,.12)--(.92,-.15) (.96,.09)--(.97,-.12);
\draw (.04,-.01) to[out=-8,in=187] (.92,-.01);
\draw (.05,-.10)--(.48,-.22)--(.94,-.06);
\end{tikzpicture}
```

Final context (up to 100 characters either side):

```tex
érée
(condition \inserted{réflexive et} symétrique) et \textcircled{\scriptsize b} La donnée,
pour \figure{\begin{tikzpicture}[x=1cm,y=1cm,baseline=-.4ex]
\draw (0,.12)--(.03,-.18) (0.07,.10)--(.09,-.16);
\draw (.90,.12)--(.92,-.15) (.96,.09)--(.97,-.12);
\draw (.04,-.01) to[out=-8,in=187] (.92,-.01);
\draw (.05,-.10)--(.48,-.22)--(.94,-.06);
\end{tikzpicture}} $\varepsilon\in S_0$, de la relation
d'équivalence $R_{\varepsilon}$ dans $C(\varepsilon)$.

\dele
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: revised

Crop links: crops/004_bottom.jpg

Alignment requires recheck: no flag

Review note: The shape is a two-ended connecting sketch, not the cancelled word tout; reproduced in TikZ.

### C-004-U015 (C line 24)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 29.

Source C token:

```tex
\unsure{\varepsilon|\epsilon|E}
```

Source C context:

```tex
d{réflexive et} symétrique) et \textcircled{\scriptsize b} La donnée,
pour \deleted{\unsure{tout}} $\unsure{\varepsilon|\epsilon|E}\in S_0$, de la relation
d'équivalence $R_{\varepsilon}$ \unsure{dans} $C(\varepsilon)$.

\deleted{\
```

Aligned final span:

```tex
\varepsilon
```

Final context (up to 100 characters either side):

```tex
4,-.01) to[out=-8,in=187] (.92,-.01);
\draw (.05,-.10)--(.48,-.22)--(.94,-.06);
\end{tikzpicture}} $\varepsilon\in S_0$, de la relation
d'équivalence $R_{\varepsilon}$ dans $C(\varepsilon)$.

\deleted{On va} \ul
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/004_bottom.jpg

Alignment requires recheck: no flag

Review note: Epsilon form, dans, old On va, crossed X, and two l stems in Appellons are visible.

### C-004-U016 (C line 25)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 30.

Source C token:

```tex
\unsure{dans}
```

Source C context:

```tex
ure{tout}} $\unsure{\varepsilon|\epsilon|E}\in S_0$, de la relation
d'équivalence $R_{\varepsilon}$ \unsure{dans} $C(\varepsilon)$.

\deleted{\unsure{On va|Donc on}} \uline{Axiomes provisoires :}

\deleted{Soit \u
```

Aligned final span:

```tex
dans
```

Final context (up to 100 characters either side):

```tex
(.94,-.06);
\end{tikzpicture}} $\varepsilon\in S_0$, de la relation
d'équivalence $R_{\varepsilon}$ dans $C(\varepsilon)$.

\deleted{On va} \uline{Axiomes provisoires :}

\deleted{Soit $X$} Appellons les 
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/004_bottom.jpg

Alignment requires recheck: no flag

Review note: Epsilon form, dans, old On va, crossed X, and two l stems in Appellons are visible.

### C-004-U017 (C line 27)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 32.

Source C token:

```tex
\unsure{On va|Donc on}
```

Source C context:

```tex
}\in S_0$, de la relation
d'équivalence $R_{\varepsilon}$ \unsure{dans} $C(\varepsilon)$.

\deleted{\unsure{On va|Donc on}} \uline{Axiomes provisoires :}

\deleted{Soit \unsure{$X$}} \unsure{Appellons|Appelons} les $U$ de 
```

Aligned final span:

```tex
On va
```

Final context (up to 100 characters either side):

```tex
varepsilon\in S_0$, de la relation
d'équivalence $R_{\varepsilon}$ dans $C(\varepsilon)$.

\deleted{On va} \uline{Axiomes provisoires :}

\deleted{Soit $X$} Appellons les $U$ de la forme
$C(\deleted{\unsur
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/004_bottom.jpg

Alignment requires recheck: no flag

Review note: Epsilon form, dans, old On va, crossed X, and two l stems in Appellons are visible.

### C-004-U018 (C line 29)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 34.

Source C token:

```tex
\unsure{$X$}
```

Source C context:

```tex
s} $C(\varepsilon)$.

\deleted{\unsure{On va|Donc on}} \uline{Axiomes provisoires :}

\deleted{Soit \unsure{$X$}} \unsure{Appellons|Appelons} les $U$ de la forme
$C(\deleted{\unsure{L}}T)$ \uline{parties modérées
```

Aligned final span:

```tex
$X$}
```

Final context (up to 100 characters either side):

```tex
{\varepsilon}$ dans $C(\varepsilon)$.

\deleted{On va} \uline{Axiomes provisoires :}

\deleted{Soit $X$} Appellons les $U$ de la forme
$C(\deleted{\unsure{L}}T)$ \uline{parties modérées cofinies}. On

% p
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/004_bottom.jpg

Alignment requires recheck: no flag

Review note: Epsilon form, dans, old On va, crossed X, and two l stems in Appellons are visible.

### C-004-U019 (C line 29)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 34.

Source C token:

```tex
\unsure{Appellons|Appelons}
```

Source C context:

```tex
lon)$.

\deleted{\unsure{On va|Donc on}} \uline{Axiomes provisoires :}

\deleted{Soit \unsure{$X$}} \unsure{Appellons|Appelons} les $U$ de la forme
$C(\deleted{\unsure{L}}T)$ \uline{parties modérées cofinies}. On

% paper water
```

Aligned final span:

```tex
Appellons
```

Final context (up to 100 characters either side):

```tex
epsilon}$ dans $C(\varepsilon)$.

\deleted{On va} \uline{Axiomes provisoires :}

\deleted{Soit $X$} Appellons les $U$ de la forme
$C(\deleted{\unsure{L}}T)$ \uline{parties modérées cofinies}. On

% paper water
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/004_bottom.jpg

Alignment requires recheck: no flag

Review note: Epsilon form, dans, old On va, crossed X, and two l stems in Appellons are visible.

### C-004-U020 (C line 30)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 35.

Source C token:

```tex
\unsure{L}
```

Source C context:

```tex
isoires :}

\deleted{Soit \unsure{$X$}} \unsure{Appellons|Appelons} les $U$ de la forme
$C(\deleted{\unsure{L}}T)$ \uline{parties modérées cofinies}. On

% paper watermark
\rotatebox{90}{\textsc{\unsure{S}trong
```

Aligned final span:

```tex
\unsure{L}
```

Final context (up to 100 characters either side):

```tex
{On va} \uline{Axiomes provisoires :}

\deleted{Soit $X$} Appellons les $U$ de la forme
$C(\deleted{\unsure{L}}T)$ \uline{parties modérées cofinies}. On

% paper watermark
\rotatebox{90}{\textsc{\unsure{Strong 
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/004_bottom.jpg

Alignment requires recheck: no flag

Review note: Old letter above T remains heavily overwritten.

### C-004-U021 (C line 33)

Mechanical state: **unsure token(s) overlap changed alignment; inspect**. Final aligned line: 38.

Source C token:

```tex
\unsure{S}
```

Source C context:

```tex
eted{\unsure{L}}T)$ \uline{parties modérées cofinies}. On

% paper watermark
\rotatebox{90}{\textsc{\unsure{S}trong Extra St}}

```

Aligned final span:

```tex
\unsure{S
```

Final context (up to 100 characters either side):

```tex
eted{\unsure{L}}T)$ \uline{parties modérées cofinies}. On

% paper watermark
\rotatebox{90}{\textsc{\unsure{Strong Extra St}}}

```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: revised

Crop links: crops/004_bottom.jpg

Alignment requires recheck: no flag

Review note: Watermark lettering remains wholly uncertain; certainty is not transferred from neighbouring sheets.

### C-005-U001 (C line 4)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 4.

Source C token:

```tex
\unsure{)(|(}
```

Source C context:

```tex
\scanpage{5}
\mspage{4}

veut que si $U$ \deleted{$(=C\unsure{)(|(}T)$} est à la fois modéré fini
et modéré cofini, donc si $S$ et $T$
sont \deleted{\unsure{deux}} par
```

Aligned final span:

```tex
\unsure{)(|(}
```

Final context (up to 100 characters either side):

```tex
\scanpage{5}
\mspage{4}

veut que si $U$ \deleted{$(=C\unsure{)(|(}T)$} est à la fois modéré fini
et modéré cofini, donc si $S$ et $T$
sont \deleted{deux} parties modé
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/005_top.jpg

Alignment requires recheck: no flag

Review note: Crossed parenthesis/tout, small s/S, abbreviation ending and semicolon/comma remain compressed or overwritten.

### C-005-U002 (C line 6)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 6.

Source C token:

```tex
\unsure{deux}
```

Source C context:

```tex
{$(=C\unsure{)(|(}T)$} est à la fois modéré fini
et modéré cofini, donc si $S$ et $T$
sont \deleted{\unsure{deux}} parties modérées finies
\deleted{\unsure{telles}} disjointes telles que \deleted{\unsure{tout}} \i
```

Aligned final span:

```tex
deux
```

Final context (up to 100 characters either side):

```tex
{$(=C\unsure{)(|(}T)$} est à la fois modéré fini
et modéré cofini, donc si $S$ et $T$
sont \deleted{deux} parties modérées finies
\deleted{telles} disjointes telles que \deleted{\unsure{tout}} \inserted{a
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/005_top.jpg

Alignment requires recheck: no flag

Review note: Crossed deux and telles, two-staff tt abbreviation and looped L are legible.

### C-005-U003 (C line 7)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 7.

Source C token:

```tex
\unsure{telles}
```

Source C context:

```tex

et modéré cofini, donc si $S$ et $T$
sont \deleted{\unsure{deux}} parties modérées finies
\deleted{\unsure{telles}} disjointes telles que \deleted{\unsure{tout}} \inserted{a)} $S\cup T$
modéré i.e. \deleted{\unsure
```

Aligned final span:

```tex
telles
```

Final context (up to 100 characters either side):

```tex
déré fini
et modéré cofini, donc si $S$ et $T$
sont \deleted{deux} parties modérées finies
\deleted{telles} disjointes telles que \deleted{\unsure{tout}} \inserted{a)} $S\cup T$
modéré i.e. \figure{\begin{t
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/005_top.jpg

Alignment requires recheck: no flag

Review note: Crossed deux and telles, two-staff tt abbreviation and looped L are legible.

### C-005-U004 (C line 7)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 7.

Source C token:

```tex
\unsure{tout}
```

Source C context:

```tex
ted{\unsure{deux}} parties modérées finies
\deleted{\unsure{telles}} disjointes telles que \deleted{\unsure{tout}} \inserted{a)} $S\cup T$
modéré i.e. \deleted{\unsure{tout}} $\unsure{s|S}\in S$ modéré p.r. à \uns
```

Aligned final span:

```tex
\unsure{tout}
```

Final context (up to 100 characters either side):

```tex
 et $T$
sont \deleted{deux} parties modérées finies
\deleted{telles} disjointes telles que \deleted{\unsure{tout}} \inserted{a)} $S\cup T$
modéré i.e. \figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw (0,.16)--(.02,-
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/005_top.jpg

Alignment requires recheck: no flag

Review note: Crossed parenthesis/tout, small s/S, abbreviation ending and semicolon/comma remain compressed or overwritten.

### C-005-U005 (C line 8)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 8.

Source C token:

```tex
\unsure{tout}
```

Source C context:

```tex
telles}} disjointes telles que \deleted{\unsure{tout}} \inserted{a)} $S\cup T$
modéré i.e. \deleted{\unsure{tout}} $\unsure{s|S}\in S$ modéré p.r. à \unsure{tt}
$t\in T$, et b) Tout $u\in\unsure{\mathcal L|L}$ \un
```

Aligned final span:

```tex
figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw (0,.16)--(.02,-.13) (.91,.17)--(.94,-.12);
\draw (.01,-.02) to[out=0,in=197] (.92,.04);
\draw (.28,-.13)--(.79,-.06)--(.91,.08);
\end{tikzpicture}
```

Final context (up to 100 characters either side):

```tex
\deleted{telles} disjointes telles que \deleted{\unsure{tout}} \inserted{a)} $S\cup T$
modéré i.e. \figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw (0,.16)--(.02,-.13) (.91,.17)--(.94,-.12);
\draw (.01,-.02) to[out=0,in=197] (.92,.04);
\draw (.28,-.13)--(.79,-.06)--(.91,.08);
\end{tikzpicture}} $\unsure{s|S}\in S$ modéré p.r. à tt
$t\in T$, et b) Tout $u\in\mathcal L$ \unsure{modér.|modéré} 
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: revised

Crop links: crops/005_top.jpg

Alignment requires recheck: no flag

Review note: The second apparent tout is a connecting sketch with terminal strokes, not a word; TikZ preserves the shape.

### C-005-U006 (C line 8)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 12.

Source C token:

```tex
\unsure{s|S}
```

Source C context:

```tex
tes telles que \deleted{\unsure{tout}} \inserted{a)} $S\cup T$
modéré i.e. \deleted{\unsure{tout}} $\unsure{s|S}\in S$ modéré p.r. à \unsure{tt}
$t\in T$, et b) Tout $u\in\unsure{\mathcal L|L}$ \unsure{modér.|mod
```

Aligned final span:

```tex
\unsure{s|S}
```

Final context (up to 100 characters either side):

```tex
(.01,-.02) to[out=0,in=197] (.92,.04);
\draw (.28,-.13)--(.79,-.06)--(.91,.08);
\end{tikzpicture}} $\unsure{s|S}\in S$ modéré p.r. à tt
$t\in T$, et b) Tout $u\in\mathcal L$ \unsure{modér.|modéré} p.r. à
$S$ est 
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/005_top.jpg

Alignment requires recheck: no flag

Review note: Crossed parenthesis/tout, small s/S, abbreviation ending and semicolon/comma remain compressed or overwritten.

### C-005-U007 (C line 8)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 12.

Source C token:

```tex
\unsure{tt}
```

Source C context:

```tex
out}} \inserted{a)} $S\cup T$
modéré i.e. \deleted{\unsure{tout}} $\unsure{s|S}\in S$ modéré p.r. à \unsure{tt}
$t\in T$, et b) Tout $u\in\unsure{\mathcal L|L}$ \unsure{modér.|modéré} p.r. à
$S$ est dans $T$\uns
```

Aligned final span:

```tex
tt
```

Final context (up to 100 characters either side):

```tex
.04);
\draw (.28,-.13)--(.79,-.06)--(.91,.08);
\end{tikzpicture}} $\unsure{s|S}\in S$ modéré p.r. à tt
$t\in T$, et b) Tout $u\in\mathcal L$ \unsure{modér.|modéré} p.r. à
$S$ est dans $T$\unsure{;|,}, \
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/005_top.jpg

Alignment requires recheck: no flag

Review note: Crossed deux and telles, two-staff tt abbreviation and looped L are legible.

### C-005-U008 (C line 9)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 13.

Source C token:

```tex
\unsure{\mathcal L|L}
```

Source C context:

```tex
.e. \deleted{\unsure{tout}} $\unsure{s|S}\in S$ modéré p.r. à \unsure{tt}
$t\in T$, et b) Tout $u\in\unsure{\mathcal L|L}$ \unsure{modér.|modéré} p.r. à
$S$ est dans $T$\unsure{;|,}, \deleted{alors $S\cup T=\mathcal L$} e
```

Aligned final span:

```tex
\mathcal L
```

Final context (up to 100 characters either side):

```tex
-.06)--(.91,.08);
\end{tikzpicture}} $\unsure{s|S}\in S$ modéré p.r. à tt
$t\in T$, et b) Tout $u\in\mathcal L$ \unsure{modér.|modéré} p.r. à
$S$ est dans $T$\unsure{;|,}, \deleted{alors $S\cup T=\mathcal L$} e
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/005_top.jpg

Alignment requires recheck: no flag

Review note: Crossed deux and telles, two-staff tt abbreviation and looped L are legible.

### C-005-U009 (C line 9)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 13.

Source C token:

```tex
\unsure{modér.|modéré}
```

Source C context:

```tex
ut}} $\unsure{s|S}\in S$ modéré p.r. à \unsure{tt}
$t\in T$, et b) Tout $u\in\unsure{\mathcal L|L}$ \unsure{modér.|modéré} p.r. à
$S$ est dans $T$\unsure{;|,}, \deleted{alors $S\cup T=\mathcal L$} et
à fortiori $S\cup T$ e
```

Aligned final span:

```tex
\unsure{modér.|modéré}
```

Final context (up to 100 characters either side):

```tex
.08);
\end{tikzpicture}} $\unsure{s|S}\in S$ modéré p.r. à tt
$t\in T$, et b) Tout $u\in\mathcal L$ \unsure{modér.|modéré} p.r. à
$S$ est dans $T$\unsure{;|,}, \deleted{alors $S\cup T=\mathcal L$} et
à fortiori $S\cup T$ e
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/005_top.jpg

Alignment requires recheck: no flag

Review note: Crossed parenthesis/tout, small s/S, abbreviation ending and semicolon/comma remain compressed or overwritten.

### C-005-U010 (C line 10)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 14.

Source C token:

```tex
\unsure{;|,}
```

Source C context:

```tex
{tt}
$t\in T$, et b) Tout $u\in\unsure{\mathcal L|L}$ \unsure{modér.|modéré} p.r. à
$S$ est dans $T$\unsure{;|,}, \deleted{alors $S\cup T=\mathcal L$} et
à fortiori $S\cup T$ est partie \inserted{finie} modérée
m
```

Aligned final span:

```tex
\unsure{;|,}
```

Final context (up to 100 characters either side):

```tex
odéré p.r. à tt
$t\in T$, et b) Tout $u\in\mathcal L$ \unsure{modér.|modéré} p.r. à
$S$ est dans $T$\unsure{;|,}, \deleted{alors $S\cup T=\mathcal L$} et
à fortiori $S\cup T$ est partie \inserted{finie} modérée
m
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/005_top.jpg

Alignment requires recheck: no flag

Review note: Crossed parenthesis/tout, small s/S, abbreviation ending and semicolon/comma remain compressed or overwritten.

### C-005-U011 (C line 13)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 17.

Source C token:

```tex
\unsure{{}^{\cdot\cdot}S_0|S_0}
```

Source C context:

```tex

à fortiori $S\cup T$ est partie \inserted{finie} modérée
maximale, alors $S\cup T=\mathcal L$, et
$\unsure{{}^{\cdot\cdot}S_0|S_0}=\unsure{P|\mathcal P}_2(\mathcal L)$, enfin les relations
d'équivalence sont discrètes, et les
$\un
```

Aligned final span:

```tex
\unsure{{}^{\cdot\cdot}S_0|S_0}
```

Final context (up to 100 characters either side):

```tex
t
à fortiori $S\cup T$ est partie \inserted{finie} modérée
maximale, donc $S\cup T=\mathcal L$, et
$\unsure{{}^{\cdot\cdot}S_0|S_0}=P_2(\mathcal L)$, enfin les relations
d'équivalence sont discrètes, et les
$\dot A$ sont vides. Pou
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/005_middle.jpg

Alignment requires recheck: no flag

Review note: Two small marks near S and the article after définit cannot be securely classified.

### C-005-U012 (C line 13)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 17.

Source C token:

```tex
\unsure{P|\mathcal P}
```

Source C context:

```tex
 \inserted{finie} modérée
maximale, alors $S\cup T=\mathcal L$, et
$\unsure{{}^{\cdot\cdot}S_0|S_0}=\unsure{P|\mathcal P}_2(\mathcal L)$, enfin les relations
d'équivalence sont discrètes, et les
$\unsure{\dot A|\bar A}$ s
```

Aligned final span:

```tex
P
```

Final context (up to 100 characters either side):

```tex
e \inserted{finie} modérée
maximale, donc $S\cup T=\mathcal L$, et
$\unsure{{}^{\cdot\cdot}S_0|S_0}=P_2(\mathcal L)$, enfin les relations
d'équivalence sont discrètes, et les
$\dot A$ sont vides. Pour 
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/005_middle.jpg

Alignment requires recheck: no flag

Review note: Single-staff P, point above A, le, crossed Déf and capital R in Réseau are visible.

### C-005-U013 (C line 15)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 19.

Source C token:

```tex
\unsure{\dot A|\bar A}
```

Source C context:

```tex
_0}=\unsure{P|\mathcal P}_2(\mathcal L)$, enfin les relations
d'équivalence sont discrètes, et les
$\unsure{\dot A|\bar A}$ sont vides. Pour \unsure{le|la} formuler,
on définit \unsure{la|a}

\deleted{\unsure{Déf}} \insert
```

Aligned final span:

```tex
\dot A
```

Final context (up to 100 characters either side):

```tex
{}^{\cdot\cdot}S_0|S_0}=P_2(\mathcal L)$, enfin les relations
d'équivalence sont discrètes, et les
$\dot A$ sont vides. Pour le formuler,
on définit \unsure{la|a}

\deleted{Déf} \inserted{Ex 1} \uline{struc
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/005_middle.jpg

Alignment requires recheck: no flag

Review note: Single-staff P, point above A, le, crossed Déf and capital R in Réseau are visible.

### C-005-U014 (C line 15)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 19.

Source C token:

```tex
\unsure{le|la}
```

Source C context:

```tex
 enfin les relations
d'équivalence sont discrètes, et les
$\unsure{\dot A|\bar A}$ sont vides. Pour \unsure{le|la} formuler,
on définit \unsure{la|a}

\deleted{\unsure{Déf}} \inserted{Ex 1} \uline{structure \insert
```

Aligned final span:

```tex
le
```

Final context (up to 100 characters either side):

```tex
_2(\mathcal L)$, enfin les relations
d'équivalence sont discrètes, et les
$\dot A$ sont vides. Pour le formuler,
on définit \unsure{la|a}

\deleted{Déf} \inserted{Ex 1} \uline{structure \inserted{de Rés
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/005_middle.jpg

Alignment requires recheck: no flag

Review note: Single-staff P, point above A, le, crossed Déf and capital R in Réseau are visible.

### C-005-U015 (C line 16)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 20.

Source C token:

```tex
\unsure{la|a}
```

Source C context:

```tex
ont discrètes, et les
$\unsure{\dot A|\bar A}$ sont vides. Pour \unsure{le|la} formuler,
on définit \unsure{la|a}

\deleted{\unsure{Déf}} \inserted{Ex 1} \uline{structure \inserted{de \unsure{Réseau|réseau}} discr
```

Aligned final span:

```tex
\unsure{la|a}
```

Final context (up to 100 characters either side):

```tex
es relations
d'équivalence sont discrètes, et les
$\dot A$ sont vides. Pour le formuler,
on définit \unsure{la|a}

\deleted{Déf} \inserted{Ex 1} \uline{structure \inserted{de Réseau} discrète} sur $\mathcal L$

\[
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/005_middle.jpg

Alignment requires recheck: no flag

Review note: Two small marks near S and the article after définit cannot be securely classified.

### C-005-U016 (C line 18)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 22.

Source C token:

```tex
\unsure{Déf}
```

Source C context:

```tex
unsure{\dot A|\bar A}$ sont vides. Pour \unsure{le|la} formuler,
on définit \unsure{la|a}

\deleted{\unsure{Déf}} \inserted{Ex 1} \uline{structure \inserted{de \unsure{Réseau|réseau}} discrète} sur $\mathcal L$


```

Aligned final span:

```tex
Déf
```

Final context (up to 100 characters either side):

```tex
ce sont discrètes, et les
$\dot A$ sont vides. Pour le formuler,
on définit \unsure{la|a}

\deleted{Déf} \inserted{Ex 1} \uline{structure \inserted{de Réseau} discrète} sur $\mathcal L$

\[
 S_0=P_2(\mat
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/005_middle.jpg

Alignment requires recheck: no flag

Review note: Single-staff P, point above A, le, crossed Déf and capital R in Réseau are visible.

### C-005-U017 (C line 18)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 22.

Source C token:

```tex
\unsure{Réseau|réseau}
```

Source C context:

```tex
ler,
on définit \unsure{la|a}

\deleted{\unsure{Déf}} \inserted{Ex 1} \uline{structure \inserted{de \unsure{Réseau|réseau}} discrète} sur $\mathcal L$

\[
 S_0=P_2(\mathcal L)\ \Longrightarrow\
 \left\{\begin{aligned}
 &\m
```

Aligned final span:

```tex
Réseau
```

Final context (up to 100 characters either side):

```tex
 le formuler,
on définit \unsure{la|a}

\deleted{Déf} \inserted{Ex 1} \uline{structure \inserted{de Réseau} discrète} sur $\mathcal L$

\[
 S_0=P_2(\mathcal L)\ \Longrightarrow\
 \left\{\begin{aligned}
 &\m
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/005_middle.jpg

Alignment requires recheck: no flag

Review note: Single-staff P, point above A, le, crossed Déf and capital R in Réseau are visible.

### C-005-U018 (C line 23)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 27.

Source C token:

```tex
\unsure{\mathcal L|\mathcal L_0}
```

Source C context:

```tex
ur $\mathcal L$

\[
 S_0=P_2(\mathcal L)\ \Longrightarrow\
 \left\{\begin{aligned}
 &\mathrm{Mod}_f(\unsure{\mathcal L|\mathcal L_0})=\deleted{\unsure{\mathrm{Mod}}}P_f(\mathcal L)\\
 &C_T=\mathcal L\setminus T\qquad\text{si }T\in P
```

Aligned final span:

```tex
\unsure{\mathcal L|\mathcal L_0}
```

Final context (up to 100 characters either side):

```tex
sur $\mathcal L$

\[
 S_0=P_2(\mathcal L)\ \Longrightarrow\
 \left\{\begin{aligned}
 &\mathrm{Modf}(\unsure{\mathcal L|\mathcal L_0})=\deleted{\unsure{\mathrm{Mod}}}P_f(\mathcal L)\\
 &C_T=\mathcal L\setminus T\qquad\text{si }T\in P
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/005_bottom.jpg

Alignment requires recheck: no flag

Review note: Tiny possible subscript, crossed Mod and formula start, and irregular R subscript remain uncertain.

### C-005-U019 (C line 23)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 27.

Source C token:

```tex
\unsure{\mathrm{Mod}}
```

Source C context:

```tex
Longrightarrow\
 \left\{\begin{aligned}
 &\mathrm{Mod}_f(\unsure{\mathcal L|\mathcal L_0})=\deleted{\unsure{\mathrm{Mod}}}P_f(\mathcal L)\\
 &C_T=\mathcal L\setminus T\qquad\text{si }T\in P_f(\mathcal L)
 \end{aligned}\ri
```

Aligned final span:

```tex
\unsure{\mathrm{Mod}}
```

Final context (up to 100 characters either side):

```tex
\Longrightarrow\
 \left\{\begin{aligned}
 &\mathrm{Modf}(\unsure{\mathcal L|\mathcal L_0})=\deleted{\unsure{\mathrm{Mod}}}P_f(\mathcal L)\\
 &C_T=\mathcal L\setminus T\qquad\text{si }T\in P_f(\mathcal L)
 \end{aligned}\ri
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/005_bottom.jpg

Alignment requires recheck: no flag

Review note: Tiny possible subscript, crossed Mod and formula start, and irregular R subscript remain uncertain.

### C-005-U020 (C line 30)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 34.

Source C token:

```tex
\unsure{\subset|\mathcal L}
```

Source C context:

```tex
 T\qquad\text{si }T\in P_f(\mathcal L)
 \end{aligned}\right.
\]

\[
\begin{aligned}
 &\deleted{C(T)=\unsure{\subset|\mathcal L}}\\
 &\unsure{R|\mathcal R}_{\unsure{T|T\rceil|\Pi}}=\text{relation d'équivalence \unsure{discrète|d
```

Aligned final span:

```tex
\unsure{\subset|\mathcal L}
```

Final context (up to 100 characters either side):

```tex
 T\qquad\text{si }T\in P_f(\mathcal L)
 \end{aligned}\right.
\]

\[
\begin{aligned}
 &\deleted{C(T)=\unsure{\subset|\mathcal L}}\\
 &R_{\unsure{T|T\rceil|\Pi}}=\text{relation d'équivalence discrète}\\
 &\hspace{3em}\text{dans }
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/005_bottom.jpg

Alignment requires recheck: no flag

Review note: Tiny possible subscript, crossed Mod and formula start, and irregular R subscript remain uncertain.

### C-005-U021 (C line 31)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 35.

Source C token:

```tex
\unsure{R|\mathcal R}
```

Source C context:

```tex
al L)
 \end{aligned}\right.
\]

\[
\begin{aligned}
 &\deleted{C(T)=\unsure{\subset|\mathcal L}}\\
 &\unsure{R|\mathcal R}_{\unsure{T|T\rceil|\Pi}}=\text{relation d'équivalence \unsure{discrète|discrèt}}\\
 &\hspace{3em}\t
```

Aligned final span:

```tex
R
```

Final context (up to 100 characters either side):

```tex
al L)
 \end{aligned}\right.
\]

\[
\begin{aligned}
 &\deleted{C(T)=\unsure{\subset|\mathcal L}}\\
 &R_{\unsure{T|T\rceil|\Pi}}=\text{relation d'équivalence discrète}\\
 &\hspace{3em}\text{dans }\mathca
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/005_bottom.jpg

Alignment requires recheck: no flag

Review note: Ordinary R, ending of discrète, composantes and cancelled Pour Donc can be read despite the deletion strokes.

### C-005-U022 (C line 31)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 35.

Source C token:

```tex
\unsure{T|T\rceil|\Pi}
```

Source C context:

```tex
ght.
\]

\[
\begin{aligned}
 &\deleted{C(T)=\unsure{\subset|\mathcal L}}\\
 &\unsure{R|\mathcal R}_{\unsure{T|T\rceil|\Pi}}=\text{relation d'équivalence \unsure{discrète|discrèt}}\\
 &\hspace{3em}\text{dans }\mathcal L\set
```

Aligned final span:

```tex
\unsure{T|T\rceil|\Pi}
```

Final context (up to 100 characters either side):

```tex
L)
 \end{aligned}\right.
\]

\[
\begin{aligned}
 &\deleted{C(T)=\unsure{\subset|\mathcal L}}\\
 &R_{\unsure{T|T\rceil|\Pi}}=\text{relation d'équivalence discrète}\\
 &\hspace{3em}\text{dans }\mathcal L\setminus T,\quad\tex
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/005_bottom.jpg

Alignment requires recheck: no flag

Review note: Tiny possible subscript, crossed Mod and formula start, and irregular R subscript remain uncertain.

### C-005-U023 (C line 31)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 35.

Source C token:

```tex
\unsure{discrète|discrèt}
```

Source C context:

```tex
subset|\mathcal L}}\\
 &\unsure{R|\mathcal R}_{\unsure{T|T\rceil|\Pi}}=\text{relation d'équivalence \unsure{discrète|discrèt}}\\
 &\hspace{3em}\text{dans }\mathcal L\setminus T,\quad\text{donc les \unsure{composantes}}\\
 &\h
```

Aligned final span:

```tex
discrète
```

Final context (up to 100 characters either side):

```tex
leted{C(T)=\unsure{\subset|\mathcal L}}\\
 &R_{\unsure{T|T\rceil|\Pi}}=\text{relation d'équivalence discrète}\\
 &\hspace{3em}\text{dans }\mathcal L\setminus T,\quad\text{donc les composantes}\\
 &\hspace{4em
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/005_bottom.jpg

Alignment requires recheck: no flag

Review note: Ordinary R, ending of discrète, composantes and cancelled Pour Donc can be read despite the deletion strokes.

### C-005-U024 (C line 32)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 36.

Source C token:

```tex
\unsure{composantes}
```

Source C context:

```tex
ce \unsure{discrète|discrèt}}\\
 &\hspace{3em}\text{dans }\mathcal L\setminus T,\quad\text{donc les \unsure{composantes}}\\
 &\hspace{4em} \inserted{A}\ \text{sont réduites à un pt}\\
 &\deleted{\text{\unsure{Pour Donc}}
```

Aligned final span:

```tex
composantes
```

Final context (up to 100 characters either side):

```tex
ation d'équivalence discrète}\\
 &\hspace{3em}\text{dans }\mathcal L\setminus T,\quad\text{donc les composantes}\\
 &\hspace{4em} \inserted{A}\ \text{sont réduites à un pt}\\
 &\deleted{\text{Pour Donc}}\\
 &\do
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/005_bottom.jpg

Alignment requires recheck: no flag

Review note: Ordinary R, ending of discrète, composantes and cancelled Pour Donc can be read despite the deletion strokes.

### C-005-U025 (C line 34)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 38.

Source C token:

```tex
\unsure{Pour Donc}
```

Source C context:

```tex
unsure{composantes}}\\
 &\hspace{4em} \inserted{A}\ \text{sont réduites à un pt}\\
 &\deleted{\text{\unsure{Pour Donc}}}\\
 &\dot A=\varnothing
\end{aligned}
\]

\uline{Axiome}\quad Si $T$ est partie finie modérée
maxi
```

Aligned final span:

```tex
Pour Donc
```

Final context (up to 100 characters either side):

```tex
onc les composantes}\\
 &\hspace{4em} \inserted{A}\ \text{sont réduites à un pt}\\
 &\deleted{\text{Pour Donc}}\\
 &\dot A=\varnothing
\end{aligned}
\]

\uline{Axiome}\quad Si $T$ est partie finie modérée
maxi
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/005_bottom.jpg

Alignment requires recheck: no flag

Review note: Ordinary R, ending of discrète, composantes and cancelled Pour Donc can be read despite the deletion strokes.

### C-005-U026 (C line 40)

Mechanical state: **unsure token(s) overlap changed alignment; inspect**. Final aligned line: 44.

Source C token:

```tex
\unsure{discrèt|discrète|discret}
```

Source C context:

```tex
uline{Axiome}\quad Si $T$ est partie finie modérée
maximale, alors $T=\mathcal L$, $\mathcal L$ est \unsure{discrèt|discrète|discret}.

% paper watermark, visible from the reverse
\rotatebox{90}{\textsc{\unsure{S}trong Extra St}}

```

Aligned final span:

```tex
\unsure{discrêt|discrèt|discret}
```

Final context (up to 100 characters either side):

```tex
uline{Axiome}\quad Si $T$ est partie finie modérée
maximale, alors $T=\mathcal L$, $\mathcal L$ est \unsure{discrêt|discrèt|discret}.

% paper watermark, visible from the reverse
\rotatebox{90}{\textsc{\unsure{Strong Extra St}}}

```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: revised

Crop links: crops/005_bottom.jpg

Alignment requires recheck: no flag

Review note: Final word has an ambiguous accent above e and no secure final e; retain discrêt/discrèt/discret rather than regularize.

### C-005-U027 (C line 43)

Mechanical state: **unsure token(s) overlap changed alignment; inspect**. Final aligned line: 47.

Source C token:

```tex
\unsure{S}
```

Source C context:

```tex
sure{discrèt|discrète|discret}.

% paper watermark, visible from the reverse
\rotatebox{90}{\textsc{\unsure{S}trong Extra St}}

```

Aligned final span:

```tex
\unsure{S
```

Final context (up to 100 characters either side):

```tex
nsure{discrêt|discrèt|discret}.

% paper watermark, visible from the reverse
\rotatebox{90}{\textsc{\unsure{Strong Extra St}}}

```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: revised

Crop links: crops/005_top.jpg

Alignment requires recheck: no flag

Review note: The watermark fragment remains wholly doubtful beneath the handwriting.

### C-006-U001 (C line 4)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 4.

Source C token:

```tex
\unsure{hyp.thèses|hypothèses}
```

Source C context:

```tex
\scanpage{6}
\mspage{5}

On va faire des \unsure{hyp.thèses|hypothèses} de
finitude \unsure{draconiennes|draconniennes}, peut-être
provisoires

% slanted
\margin{Finitude}
```

Aligned final span:

```tex
hyp.thèses
```

Final context (up to 100 characters either side):

```tex
\scanpage{6}
\mspage{5}

On va faire des hyp.thèses de
finitude \unsure{draconniennes|draconiennes}, peut-être
provisoires

% slanted
\margin{Finitude}
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/006_top.jpg

Alignment requires recheck: no flag

Review note: The point after hyp is separate and the following thèses is written without o; retain hyp.thèses.

### C-006-U002 (C line 5)

Mechanical state: **unsure token(s) overlap changed alignment; inspect**. Final aligned line: 5.

Source C token:

```tex
\unsure{draconiennes|draconniennes}
```

Source C context:

```tex
\scanpage{6}
\mspage{5}

On va faire des \unsure{hyp.thèses|hypothèses} de
finitude \unsure{draconiennes|draconniennes}, peut-être
provisoires

% slanted
\margin{Finitude}

$\underline{\mathrm{Dec}}_1$\quad \deleted{\un
```

Aligned final span:

```tex
\unsure{draconniennes|draconiennes}
```

Final context (up to 100 characters either side):

```tex
\scanpage{6}
\mspage{5}

On va faire des hyp.thèses de
finitude \unsure{draconniennes|draconiennes}, peut-être
provisoires

% slanted
\margin{Finitude}

$\underline{\mathrm{Dec}}_1$\quad \deleted{\un
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: revised

Crop links: crops/006_top.jpg

Alignment requires recheck: no flag

Review note: The middle group more nearly supports doubled n, but the count remains ambiguous; first alternative reordered without regularization.

### C-006-U003 (C line 11)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 11.

Source C token:

```tex
\unsure{l}
```

Source C context:

```tex
es}, peut-être
provisoires

% slanted
\margin{Finitude}

$\underline{\mathrm{Dec}}_1$\quad \deleted{\unsure{l}}l'ens des comp. connexes
de tout $U$ est \uline{fini}.

\deleted{\uline{Définition} Partie modérée 
```

Aligned final span:

```tex
\unsure{l}
```

Final context (up to 100 characters either side):

```tex
es}, peut-être
provisoires

% slanted
\margin{Finitude}

$\underline{\mathrm{Dec}}_1$\quad \deleted{\unsure{l}}l'ens des comp. connexes
de tout $U$ est \uline{fini}.

\deleted{\uline{Définition} Partie modérée 
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/006_main.jpg

Alignment requires recheck: no flag

Review note: Overwritten l, Soit/Soient with old ending, swapped old indices and partie ending remain obscured.

### C-006-U004 (C line 16)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 16.

Source C token:

```tex
\unsure{Soit|Soient}
```

Source C context:

```tex
ni}.

\deleted{\uline{Définition} Partie modérée \uline{fermée}}

$\underline{\mathrm{Dec}}_2$\quad \unsure{Soit|Soient}\deleted{\unsure{ent}} $U$\inserted{$=C(\deleted{\unsure{T}}S), V=C(\deleted{\unsure{S}}T)$} \unsure
```

Aligned final span:

```tex
\unsure{Soit|Soient}
```

Final context (up to 100 characters either side):

```tex
ni}.

\deleted{\uline{Définition} Partie modérée \uline{fermée}}

$\underline{\mathrm{Dec}}_2$\quad \unsure{Soit|Soient}\deleted{\unsure{ent}} $U$\inserted{$=C(\deleted{\unsure{T}}S), V=C(\deleted{\unsure{S}}T)$} \unsure
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/006_main.jpg

Alignment requires recheck: no flag

Review note: Overwritten l, Soit/Soient with old ending, swapped old indices and partie ending remain obscured.

### C-006-U005 (C line 16)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 16.

Source C token:

```tex
\unsure{ent}
```

Source C context:

```tex
ion} Partie modérée \uline{fermée}}

$\underline{\mathrm{Dec}}_2$\quad \unsure{Soit|Soient}\deleted{\unsure{ent}} $U$\inserted{$=C(\deleted{\unsure{T}}S), V=C(\deleted{\unsure{S}}T)$} \unsure{partie|parties} modé
```

Aligned final span:

```tex
\unsure{ent}
```

Final context (up to 100 characters either side):

```tex
ion} Partie modérée \uline{fermée}}

$\underline{\mathrm{Dec}}_2$\quad \unsure{Soit|Soient}\deleted{\unsure{ent}} $U$\inserted{$=C(\deleted{\unsure{T}}S), V=C(\deleted{\unsure{S}}T)$} \unsure{partie|parties} modé
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/006_main.jpg

Alignment requires recheck: no flag

Review note: Overwritten l, Soit/Soient with old ending, swapped old indices and partie ending remain obscured.

### C-006-U006 (C line 16)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 16.

Source C token:

```tex
\unsure{T}
```

Source C context:

```tex
nderline{\mathrm{Dec}}_2$\quad \unsure{Soit|Soient}\deleted{\unsure{ent}} $U$\inserted{$=C(\deleted{\unsure{T}}S), V=C(\deleted{\unsure{S}}T)$} \unsure{partie|parties} modérée
cofinies, avec $U\subset V$ i.e. $
```

Aligned final span:

```tex
\unsure{T}
```

Final context (up to 100 characters either side):

```tex
nderline{\mathrm{Dec}}_2$\quad \unsure{Soit|Soient}\deleted{\unsure{ent}} $U$\inserted{$=C(\deleted{\unsure{T}}S), V=C(\deleted{\unsure{S}}T)$} \unsure{partie|parties} modérée
cofinies, avec $U\subset V$ i.e. $
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/006_main.jpg

Alignment requires recheck: no flag

Review note: Overwritten l, Soit/Soient with old ending, swapped old indices and partie ending remain obscured.

### C-006-U007 (C line 16)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 16.

Source C token:

```tex
\unsure{S}
```

Source C context:

```tex
ad \unsure{Soit|Soient}\deleted{\unsure{ent}} $U$\inserted{$=C(\deleted{\unsure{T}}S), V=C(\deleted{\unsure{S}}T)$} \unsure{partie|parties} modérée
cofinies, avec $U\subset V$ i.e. $T\subset S$.
Alors \unsure{t
```

Aligned final span:

```tex
\unsure{S}
```

Final context (up to 100 characters either side):

```tex
ad \unsure{Soit|Soient}\deleted{\unsure{ent}} $U$\inserted{$=C(\deleted{\unsure{T}}S), V=C(\deleted{\unsure{S}}T)$} \unsure{partie|parties} modérée
cofinies, avec $U\subset V$ i.e. $T\subset S$.
Alors tte compo
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/006_main.jpg

Alignment requires recheck: no flag

Review note: Overwritten l, Soit/Soient with old ending, swapped old indices and partie ending remain obscured.

### C-006-U008 (C line 16)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 16.

Source C token:

```tex
\unsure{partie|parties}
```

Source C context:

```tex
Soient}\deleted{\unsure{ent}} $U$\inserted{$=C(\deleted{\unsure{T}}S), V=C(\deleted{\unsure{S}}T)$} \unsure{partie|parties} modérée
cofinies, avec $U\subset V$ i.e. $T\subset S$.
Alors \unsure{tte} composante connexe \inser
```

Aligned final span:

```tex
\unsure{partie|parties}
```

Final context (up to 100 characters either side):

```tex
Soient}\deleted{\unsure{ent}} $U$\inserted{$=C(\deleted{\unsure{T}}S), V=C(\deleted{\unsure{S}}T)$} \unsure{partie|parties} modérée
cofinies, avec $U\subset V$ i.e. $T\subset S$.
Alors tte composante connexe \inserted{$A$} 
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/006_main.jpg

Alignment requires recheck: no flag

Review note: Overwritten l, Soit/Soient with old ending, swapped old indices and partie ending remain obscured.

### C-006-U009 (C line 18)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 18.

Source C token:

```tex
\unsure{tte}
```

Source C context:

```tex
unsure{S}}T)$} \unsure{partie|parties} modérée
cofinies, avec $U\subset V$ i.e. $T\subset S$.
Alors \unsure{tte} composante connexe \inserted{$A$} de
$U$ est contenue dans une comp.
connexe (unique bien \unsure{s
```

Aligned final span:

```tex
tte
```

Final context (up to 100 characters either side):

```tex
unsure{S}}T)$} \unsure{partie|parties} modérée
cofinies, avec $U\subset V$ i.e. $T\subset S$.
Alors tte composante connexe \inserted{$A$} de
$U$ est contenue dans une comp.
connexe (unique bien sur) $B$ 
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/006_main.jpg

Alignment requires recheck: no flag

Review note: The abbreviation tte is visible; sur has no clear circumflex.

### C-006-U010 (C line 20)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 20.

Source C token:

```tex
\unsure{sur|sûr}
```

Source C context:

```tex
sure{tte} composante connexe \inserted{$A$} de
$U$ est contenue dans une comp.
connexe (unique bien \unsure{sur|sûr}) $B$ de $V$.

De plus, on a

\diagram{\begin{tikzcd}[ampersand replacement=\&,row sep=0.35ex,column
```

Aligned final span:

```tex
sur
```

Final context (up to 100 characters either side):

```tex
Alors tte composante connexe \inserted{$A$} de
$U$ est contenue dans une comp.
connexe (unique bien sur) $B$ de $V$.

De plus, on a

\diagram{\begin{tikzcd}[ampersand replacement=\&,row sep=0.35ex,column
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/006_main.jpg

Alignment requires recheck: no flag

Review note: The abbreviation tte is visible; sur has no clear circumflex.

### C-006-U011 (C line 31)

Mechanical state: **unsure token(s) overlap changed alignment; inspect**. Final aligned line: 31.

Source C token:

```tex
\unsure{S|s}
```

Source C context:

```tex
.south east);
}]
|[alias=aa]| \dot A \& \cap\,T\,\subset \& |[alias=bb]| \dot B\\
\cap \& \& \cap\\
\unsure{S|s} \& \& T
\end{tikzcd}}

% paper watermark; read from foot to head; clipped at the two sheet edges
\r
```

Aligned final span:

```tex
\unsure{s|S}
```

Final context (up to 100 characters either side):

```tex
.south east);
}]
|[alias=aa]| \dot A \& \cap\,T\,\subset \& |[alias=bb]| \dot B\\
\cap \& \& \cap\\
\unsure{s|S} \& \& T
\end{tikzcd}}

% paper watermark; read from foot to head; clipped at the two sheet edges
\r
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: revised

Crop links: crops/006_formula.jpg

Alignment requires recheck: no flag

Review note: Lower sign is s-shaped and smaller than the nearby T, but capital/lowercase distinction remains uncertain.

### C-006-U012 (C line 35)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 35.

Source C token:

```tex
\unsure{t}
```

Source C context:

```tex
}

% paper watermark; read from foot to head; clipped at the two sheet edges
\rotatebox{90}{\textsc{\unsure{t}rong Extra Str}}

```

Aligned final span:

```tex
\unsure{t}
```

Final context (up to 100 characters either side):

```tex
}

% paper watermark; read from foot to head; clipped at the two sheet edges
\rotatebox{90}{\textsc{\unsure{t}rong Extra Str}}

```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/006_watermark.jpg

Alignment requires recheck: no flag

Review note: The clipped beginning may be t; rest of this particular outline fragment is readable.

### C-007-U001 (C line 4)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 4.

Source C token:

```tex
\unsure{1}
```

Source C context:

```tex
\scanpage{7}
\mspage{6}

\uline{Ex \deleted{\unsure{1}}\unsure{2|1}}\quad Soit $\deleted{\unsure{S|E}}$ $\unsure{\mathcal L|L}$ un ens ordonné,
on suppose
```

Aligned final span:

```tex
\unsure{1}
```

Final context (up to 100 characters either side):

```tex
\scanpage{7}
\mspage{6}

\uline{Ex \deleted{\unsure{1}}2}\quad Soit $\deleted{\unsure{S|E}}$ $\mathcal L$ un ens ordonné,
on suppose $\mathcal L$ filtrant
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/007_top.jpg

Alignment requires recheck: no flag

Review note: Old example number, cancelled set letter and abbreviated element ending remain unresolved.

### C-007-U002 (C line 4)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 4.

Source C token:

```tex
\unsure{2|1}
```

Source C context:

```tex
\scanpage{7}
\mspage{6}

\uline{Ex \deleted{\unsure{1}}\unsure{2|1}}\quad Soit $\deleted{\unsure{S|E}}$ $\unsure{\mathcal L|L}$ un ens ordonné,
on suppose $\mathcal L$
```

Aligned final span:

```tex
2
```

Final context (up to 100 characters either side):

```tex
\scanpage{7}
\mspage{6}

\uline{Ex \deleted{\unsure{1}}2}\quad Soit $\deleted{\unsure{S|E}}$ $\mathcal L$ un ens ordonné,
on suppose $\mathcal L$ filtrant c
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/007_top.jpg

Alignment requires recheck: no flag

Review note: Live numeral 2, looped L, and only one l in appelera are visible.

### C-007-U003 (C line 4)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 4.

Source C token:

```tex
\unsure{S|E}
```

Source C context:

```tex
\scanpage{7}
\mspage{6}

\uline{Ex \deleted{\unsure{1}}\unsure{2|1}}\quad Soit $\deleted{\unsure{S|E}}$ $\unsure{\mathcal L|L}$ un ens ordonné,
on suppose $\mathcal L$ filtrant croissant, filtrant
décr
```

Aligned final span:

```tex
\unsure{S|E}
```

Final context (up to 100 characters either side):

```tex
\scanpage{7}
\mspage{6}

\uline{Ex \deleted{\unsure{1}}2}\quad Soit $\deleted{\unsure{S|E}}$ $\mathcal L$ un ens ordonné,
on suppose $\mathcal L$ filtrant croissant, filtrant
décroissant, sa
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/007_top.jpg

Alignment requires recheck: no flag

Review note: Old example number, cancelled set letter and abbreviated element ending remain unresolved.

### C-007-U004 (C line 4)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 4.

Source C token:

```tex
\unsure{\mathcal L|L}
```

Source C context:

```tex
page{7}
\mspage{6}

\uline{Ex \deleted{\unsure{1}}\unsure{2|1}}\quad Soit $\deleted{\unsure{S|E}}$ $\unsure{\mathcal L|L}$ un ens ordonné,
on suppose $\mathcal L$ filtrant croissant, filtrant
décroissant, sans plus grand 
```

Aligned final span:

```tex
\mathcal L
```

Final context (up to 100 characters either side):

```tex
\scanpage{7}
\mspage{6}

\uline{Ex \deleted{\unsure{1}}2}\quad Soit $\deleted{\unsure{S|E}}$ $\mathcal L$ un ens ordonné,
on suppose $\mathcal L$ filtrant croissant, filtrant
décroissant, sans plus grand 
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/007_top.jpg

Alignment requires recheck: no flag

Review note: Live numeral 2, looped L, and only one l in appelera are visible.

### C-007-U005 (C line 7)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 7.

Source C token:

```tex
\unsure{élémt|élément}
```

Source C context:

```tex
né,
on suppose $\mathcal L$ filtrant croissant, filtrant
décroissant, sans plus grand ni
plus petit \unsure{élémt|élément}, loc. filtrant croissant
et filtrant décroissant, divisible.

On \unsure{appelera|appellera} un tel
```

Aligned final span:

```tex
\unsure{élémt|élément}
```

Final context (up to 100 characters either side):

```tex
né,
on suppose $\mathcal L$ filtrant croissant, filtrant
décroissant, sans plus grand ni
plus petit \unsure{élémt|élément}, loc. filtrant croissant
et filtrant décroissant, divisible.

On appelera un tel ensemble une
\ulin
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/007_top.jpg

Alignment requires recheck: no flag

Review note: Old example number, cancelled set letter and abbreviated element ending remain unresolved.

### C-007-U006 (C line 10)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 10.

Source C token:

```tex
\unsure{appelera|appellera}
```

Source C context:

```tex

plus petit \unsure{élémt|élément}, loc. filtrant croissant
et filtrant décroissant, divisible.

On \unsure{appelera|appellera} un tel ensemble une
\uline{ligne ordonnée}

\[
S_0\subset\unsure{P|\mathcal P}_2(\mathcal L)\qquad

```

Aligned final span:

```tex
appelera
```

Final context (up to 100 characters either side):

```tex

plus petit \unsure{élémt|élément}, loc. filtrant croissant
et filtrant décroissant, divisible.

On appelera un tel ensemble une
\uline{ligne ordonnée}

\[
S_0\subset P_2(\mathcal L)\qquad
\deleted{\text{Soit
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/007_top.jpg

Alignment requires recheck: no flag

Review note: Live numeral 2, looped L, and only one l in appelera are visible.

### C-007-U007 (C line 14)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 14.

Source C token:

```tex
\unsure{P|\mathcal P}
```

Source C context:

```tex
divisible.

On \unsure{appelera|appellera} un tel ensemble une
\uline{ligne ordonnée}

\[
S_0\subset\unsure{P|\mathcal P}_2(\mathcal L)\qquad
\deleted{\text{\unsure{Soit} }\{x,y\}\in P_2(\mathcal L)}
\]

\textquotedbl\qua
```

Aligned final span:

```tex
 P
```

Final context (up to 100 characters either side):

```tex
trant décroissant, divisible.

On appelera un tel ensemble une
\uline{ligne ordonnée}

\[
S_0\subset P_2(\mathcal L)\qquad
\deleted{\text{Soit }\{x,y\}\in P_2(\mathcal L)}
\]

\textquotedbl\quad \unsure
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/007_middle.jpg

Alignment requires recheck: no flag

Review note: Single-staff P, crossed Soit and tot without a following point in the Modf line are legible. Alignment recheck: A TeX command delimiter space was added; the image-reviewed plain P is unchanged.

### C-007-U008 (C line 15)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 15.

Source C token:

```tex
\unsure{Soit}
```

Source C context:

```tex
e une
\uline{ligne ordonnée}

\[
S_0\subset\unsure{P|\mathcal P}_2(\mathcal L)\qquad
\deleted{\text{\unsure{Soit} }\{x,y\}\in P_2(\mathcal L)}
\]

\textquotedbl\quad \unsure{partie|parties} \deleted{qui} de card. 
```

Aligned final span:

```tex
Soit
```

Final context (up to 100 characters either side):

```tex
lera un tel ensemble une
\uline{ligne ordonnée}

\[
S_0\subset P_2(\mathcal L)\qquad
\deleted{\text{Soit }\{x,y\}\in P_2(\mathcal L)}
\]

\textquotedbl\quad \unsure{partie|parties} \deleted{qui} de card. 
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/007_middle.jpg

Alignment requires recheck: no flag

Review note: Single-staff P, crossed Soit and tot without a following point in the Modf line are legible.

### C-007-U009 (C line 18)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 18.

Source C token:

```tex
\unsure{partie|parties}
```

Source C context:

```tex
(\mathcal L)\qquad
\deleted{\text{\unsure{Soit} }\{x,y\}\in P_2(\mathcal L)}
\]

\textquotedbl\quad \unsure{partie|parties} \deleted{qui} de card. 2 \deleted{\unsure{une}} qui sont \uline{tot.} ordonnées

\[
\begin{aligned}
```

Aligned final span:

```tex
\unsure{partie|parties}
```

Final context (up to 100 characters either side):

```tex
ubset P_2(\mathcal L)\qquad
\deleted{\text{Soit }\{x,y\}\in P_2(\mathcal L)}
\]

\textquotedbl\quad \unsure{partie|parties} \deleted{qui} de card. 2 \deleted{\unsure{une}} qui sont \uline{tot.} ordonnées

\[
\begin{aligned}
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/007_middle.jpg

Alignment requires recheck: no flag

Review note: Partie ending, crossed une, first subscript and the second variable in the inequality remain uncertain.

### C-007-U010 (C line 18)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 18.

Source C token:

```tex
\unsure{une}
```

Source C context:

```tex
n P_2(\mathcal L)}
\]

\textquotedbl\quad \unsure{partie|parties} \deleted{qui} de card. 2 \deleted{\unsure{une}} qui sont \uline{tot.} ordonnées

\[
\begin{aligned}
&\mathrm{Mod}_f(\mathcal L)=\text{parties fini
```

Aligned final span:

```tex
\unsure{une}
```

Final context (up to 100 characters either side):

```tex
n P_2(\mathcal L)}
\]

\textquotedbl\quad \unsure{partie|parties} \deleted{qui} de card. 2 \deleted{\unsure{une}} qui sont \uline{tot.} ordonnées

\[
\begin{aligned}
&\mathrm{Modf}(\mathcal L)=\text{parties finie
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/007_middle.jpg

Alignment requires recheck: no flag

Review note: Partie ending, crossed une, first subscript and the second variable in the inequality remain uncertain.

### C-007-U011 (C line 22)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 22.

Source C token:

```tex
\unsure{tot|tot.}
```

Source C context:

```tex
ui sont \uline{tot.} ordonnées

\[
\begin{aligned}
&\mathrm{Mod}_f(\mathcal L)=\text{parties finies \unsure{tot|tot.} ordonnées}\\
&\hspace{8em}\deleted{\text{i.e. telles que}}
\end{aligned}
\]

\[
\begin{aligned}
 \t
```

Aligned final span:

```tex
tot
```

Final context (up to 100 characters either side):

```tex
qui sont \uline{tot.} ordonnées

\[
\begin{aligned}
&\mathrm{Modf}(\mathcal L)=\text{parties finies tot ordonnées}\\
&\hspace{8em}\deleted{\text{i.e. telles que}}
\end{aligned}
\]

\[
\begin{aligned}
 \t
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/007_middle.jpg

Alignment requires recheck: no flag

Review note: Single-staff P, crossed Soit and tot without a following point in the Modf line are legible.

### C-007-U012 (C line 29)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 29.

Source C token:

```tex
\unsure{p|1}
```

Source C context:

```tex
e}}
\end{aligned}
\]

\[
\begin{aligned}
 \text{Soit }T\in\mathrm{Mod}_f(\mathcal L),\qquad &T=\{t_{\unsure{p|1}},t_2,\ldots,t_{\unsure{n|m}}\}\\
 &\quad t_1<\unsure{t|l|1}_2<\ldots<t_n
\end{aligned}
\]

Alors le
```

Aligned final span:

```tex
\unsure{p|1}
```

Final context (up to 100 characters either side):

```tex
ue}}
\end{aligned}
\]

\[
\begin{aligned}
 \text{Soit }T\in\mathrm{Modf}(\mathcal L),\qquad &T=\{t_{\unsure{p|1}},t_2,\ldots,t_{n}\}\\
 &\quad t_1<\unsure{t|l|1}_2<\ldots<t_n
\end{aligned}
\]

Alors les composant
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/007_middle.jpg

Alignment requires recheck: no flag

Review note: Partie ending, crossed une, first subscript and the second variable in the inequality remain uncertain.

### C-007-U013 (C line 29)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 29.

Source C token:

```tex
\unsure{n|m}
```

Source C context:

```tex
gin{aligned}
 \text{Soit }T\in\mathrm{Mod}_f(\mathcal L),\qquad &T=\{t_{\unsure{p|1}},t_2,\ldots,t_{\unsure{n|m}}\}\\
 &\quad t_1<\unsure{t|l|1}_2<\ldots<t_n
\end{aligned}
\]

Alors les composantes connexes sont

```

Aligned final span:

```tex
n
```

Final context (up to 100 characters either side):

```tex
egin{aligned}
 \text{Soit }T\in\mathrm{Modf}(\mathcal L),\qquad &T=\{t_{\unsure{p|1}},t_2,\ldots,t_{n}\}\\
 &\quad t_1<\unsure{t|l|1}_2<\ldots<t_n
\end{aligned}
\]

Alors les composantes connexes sont

```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/007_bottom.jpg

Alignment requires recheck: no flag

Review note: Final subscript n, closing right bracket, plus in n+1 and composantes are readable; no plus is supplied before infinity.

### C-007-U014 (C line 30)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 30.

Source C token:

```tex
\unsure{t|l|1}
```

Source C context:

```tex
\mathrm{Mod}_f(\mathcal L),\qquad &T=\{t_{\unsure{p|1}},t_2,\ldots,t_{\unsure{n|m}}\}\\
 &\quad t_1<\unsure{t|l|1}_2<\ldots<t_n
\end{aligned}
\]

Alors les composantes connexes sont

\[
\underbrace{\mathopen{]}-\in
```

Aligned final span:

```tex
\unsure{t|l|1}
```

Final context (up to 100 characters either side):

```tex
t{Soit }T\in\mathrm{Modf}(\mathcal L),\qquad &T=\{t_{\unsure{p|1}},t_2,\ldots,t_{n}\}\\
 &\quad t_1<\unsure{t|l|1}_2<\ldots<t_n
\end{aligned}
\]

Alors les composantes connexes sont

\[
\underbrace{\mathopen{]}-\in
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/007_middle.jpg

Alignment requires recheck: no flag

Review note: Partie ending, crossed une, first subscript and the second variable in the inequality remain uncertain.

### C-007-U015 (C line 41)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 41.

Source C token:

```tex
\unsure{]|[}
```

Source C context:

```tex
\mathopen{]}t_{n-1},t_n\mathclose{[}}_{t_{n-1}\,t_n},\
\underbrace{\mathopen{]}t_n,\infty\mathclose{\unsure{]|[}}}_{t_n}
\]

% slanted
\margin{\unsure{pts|Pts} frontière}

($n\unsure{+|-}1$ \unsure{composantes} c
```

Aligned final span:

```tex
]
```

Final context (up to 100 characters either side):

```tex
\mathopen{]}t_{n-1},t_n\mathclose{[}}_{t_{n-1}\,t_n},\
\underbrace{\mathopen{]}t_n,\infty\mathclose{]}}_{t_n}
\]

% slanted
\margin{Pts frontière}

($n+1$ composantes connexes)

% paper watermark; mirr
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/007_bottom.jpg

Alignment requires recheck: no flag

Review note: Final subscript n, closing right bracket, plus in n+1 and composantes are readable; no plus is supplied before infinity.

### C-007-U016 (C line 45)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 45.

Source C token:

```tex
\unsure{pts|Pts}
```

Source C context:

```tex
-1}\,t_n},\
\underbrace{\mathopen{]}t_n,\infty\mathclose{\unsure{]|[}}}_{t_n}
\]

% slanted
\margin{\unsure{pts|Pts} frontière}

($n\unsure{+|-}1$ \unsure{composantes} connexes)

% paper watermark; mirror impression 
```

Aligned final span:

```tex
Pts
```

Final context (up to 100 characters either side):

```tex
e{[}}_{t_{n-1}\,t_n},\
\underbrace{\mathopen{]}t_n,\infty\mathclose{]}}_{t_n}
\]

% slanted
\margin{Pts frontière}

($n+1$ composantes connexes)

% paper watermark; mirror impression across the letters
\
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/007_margin.jpg

Alignment requires recheck: no flag

Review note: Rotated Pts starts with a capital P.

### C-007-U017 (C line 47)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 47.

Source C token:

```tex
\unsure{+|-}
```

Source C context:

```tex
n{]}t_n,\infty\mathclose{\unsure{]|[}}}_{t_n}
\]

% slanted
\margin{\unsure{pts|Pts} frontière}

($n\unsure{+|-}1$ \unsure{composantes} connexes)

% paper watermark; mirror impression across the letters
\rotatebo
```

Aligned final span:

```tex
+
```

Final context (up to 100 characters either side):

```tex
},\
\underbrace{\mathopen{]}t_n,\infty\mathclose{]}}_{t_n}
\]

% slanted
\margin{Pts frontière}

($n+1$ composantes connexes)

% paper watermark; mirror impression across the letters
\rotatebox{90}{\te
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/007_bottom.jpg

Alignment requires recheck: no flag

Review note: Final subscript n, closing right bracket, plus in n+1 and composantes are readable; no plus is supplied before infinity.

### C-007-U018 (C line 47)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 47.

Source C token:

```tex
\unsure{composantes}
```

Source C context:

```tex
mathclose{\unsure{]|[}}}_{t_n}
\]

% slanted
\margin{\unsure{pts|Pts} frontière}

($n\unsure{+|-}1$ \unsure{composantes} connexes)

% paper watermark; mirror impression across the letters
\rotatebox{90}{\textsc{\unsure{t
```

Aligned final span:

```tex
composantes
```

Final context (up to 100 characters either side):

```tex
\underbrace{\mathopen{]}t_n,\infty\mathclose{]}}_{t_n}
\]

% slanted
\margin{Pts frontière}

($n+1$ composantes connexes)

% paper watermark; mirror impression across the letters
\rotatebox{90}{\textsc{\unsure{t
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/007_bottom.jpg

Alignment requires recheck: no flag

Review note: Final subscript n, closing right bracket, plus in n+1 and composantes are readable; no plus is supplied before infinity.

### C-007-U019 (C line 50)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 50.

Source C token:

```tex
\unsure{t}
```

Source C context:

```tex
posantes} connexes)

% paper watermark; mirror impression across the letters
\rotatebox{90}{\textsc{\unsure{t}rong Extra Str}}

```

Aligned final span:

```tex
\unsure{t}
```

Final context (up to 100 characters either side):

```tex
mposantes connexes)

% paper watermark; mirror impression across the letters
\rotatebox{90}{\textsc{\unsure{t}rong Extra Str}}

```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/007_bottom.jpg

Alignment requires recheck: no flag

Review note: Clipped first watermark letter remains uncertain.

### C-008-U001 (C line 5)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 5.

Source C token:

```tex
\unsure{de}
```

Source C context:

```tex
\scanpage{8}
\mspage{7}

Cette structure ne change pas si
\deleted{\unsure{de}}on change l'ordre \unsure{par} ordre opposé,
i.e. elle ne dépend que du
biordre.

\deleted{Partie m
```

Aligned final span:

```tex
\unsure{de}
```

Final context (up to 100 characters either side):

```tex
\scanpage{8}
\mspage{7}

Cette structure ne change pas si
\deleted{\unsure{de}}on change l'ordre par ordre opposé,
i.e. elle ne dépend que du
biordre.

\deleted{Partie modérée} \
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/008_heads.jpg

Alignment requires recheck: no flag

Review note: Cancelled de and the old/new heading endings remain compressed or overwritten.

### C-008-U002 (C line 5)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 5.

Source C token:

```tex
\unsure{par}
```

Source C context:

```tex
\scanpage{8}
\mspage{7}

Cette structure ne change pas si
\deleted{\unsure{de}}on change l'ordre \unsure{par} ordre opposé,
i.e. elle ne dépend que du
biordre.

\deleted{Partie modérée} \deleted{\unsure{Segmen
```

Aligned final span:

```tex
par
```

Final context (up to 100 characters either side):

```tex
\scanpage{8}
\mspage{7}

Cette structure ne change pas si
\deleted{\unsure{de}}on change l'ordre par ordre opposé,
i.e. elle ne dépend que du
biordre.

\deleted{Partie modérée} \deleted{\unsure{Segmen
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/008_top.jpg

Alignment requires recheck: no flag

Review note: Par is visibly written between ordre and ordre opposé.

### C-008-U003 (C line 9)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 9.

Source C token:

```tex
\unsure{Segments|Segment}
```

Source C context:

```tex
e \unsure{par} ordre opposé,
i.e. elle ne dépend que du
biordre.

\deleted{Partie modérée} \deleted{\unsure{Segments|Segment}}

% slanted
\margin{refaire, sans se borner à une ligne : \unsure{sous tronçon|son tronçon} fermé d
```

Aligned final span:

```tex
\unsure{Segments|Segment}
```

Final context (up to 100 characters either side):

```tex
ge l'ordre par ordre opposé,
i.e. elle ne dépend que du
biordre.

\deleted{Partie modérée} \deleted{\unsure{Segments|Segment}}

% slanted
\margin{refaire, sans se borner à une ligne : sous tronçon fermé d'un tronçon. C'est un
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/008_heads.jpg

Alignment requires recheck: no flag

Review note: Cancelled de and the old/new heading endings remain compressed or overwritten.

### C-008-U004 (C line 12)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 12.

Source C token:

```tex
\unsure{sous tronçon|son tronçon}
```

Source C context:

```tex
dérée} \deleted{\unsure{Segments|Segment}}

% slanted
\margin{refaire, sans se borner à une ligne : \unsure{sous tronçon|son tronçon} fermé d'un tronçon. C'est un tronçon \unsure{p.|pour} le biordre induit. D'autre part, le bord d'un
```

Aligned final span:

```tex
sous tronçon
```

Final context (up to 100 characters either side):

```tex
dérée} \deleted{\unsure{Segments|Segment}}

% slanted
\margin{refaire, sans se borner à une ligne : sous tronçon fermé d'un tronçon. C'est un tronçon \unsure{p.|pour} le biordre induit. D'autre part, le bord d'un
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/008_margin.jpg

Alignment requires recheck: no flag

Review note: Rotated note has sous tronçon and final Comme des; no completion of the unfinished clause is added.

### C-008-U005 (C line 12)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 12.

Source C token:

```tex
\unsure{p.|pour}
```

Source C context:

```tex
sans se borner à une ligne : \unsure{sous tronçon|son tronçon} fermé d'un tronçon. C'est un tronçon \unsure{p.|pour} le biordre induit. D'autre part, le bord d'un tronçon est défini \unsure{comme|Ens} des}

\unsure{T
```

Aligned final span:

```tex
\unsure{p.|pour}
```

Final context (up to 100 characters either side):

```tex
ted
\margin{refaire, sans se borner à une ligne : sous tronçon fermé d'un tronçon. C'est un tronçon \unsure{p.|pour} le biordre induit. D'autre part, le bord d'un tronçon est défini Comme des}

\unsure{Tronçons|Tronç
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/008_margin.jpg

Alignment requires recheck: no flag

Review note: Short linking abbreviation is p.-shaped, but a compressed pour cannot be excluded.

### C-008-U006 (C line 12)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 12.

Source C token:

```tex
\unsure{comme|Ens}
```

Source C context:

```tex
 C'est un tronçon \unsure{p.|pour} le biordre induit. D'autre part, le bord d'un tronçon est défini \unsure{comme|Ens} des}

\unsure{Tronçons|Tronçon} de la ligne : parties
de la forme

\[
\left\{\begin{aligned}
 &[s,t
```

Aligned final span:

```tex
Comme
```

Final context (up to 100 characters either side):

```tex
 C'est un tronçon \unsure{p.|pour} le biordre induit. D'autre part, le bord d'un tronçon est défini Comme des}

\unsure{Tronçons|Tronçon} de la ligne : parties
de la forme

\[
\left\{\begin{aligned}
 &[s,t
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/008_margin.jpg

Alignment requires recheck: no flag

Review note: Rotated note has sous tronçon and final Comme des; no completion of the unfinished clause is added.

### C-008-U007 (C line 14)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 14.

Source C token:

```tex
\unsure{Tronçons|Tronçon}
```

Source C context:

```tex
{p.|pour} le biordre induit. D'autre part, le bord d'un tronçon est défini \unsure{comme|Ens} des}

\unsure{Tronçons|Tronçon} de la ligne : parties
de la forme

\[
\left\{\begin{aligned}
 &[s,t] &&s\leq t\\
 &\mathopen{]}-\in
```

Aligned final span:

```tex
\unsure{Tronçons|Tronçon}
```

Final context (up to 100 characters either side):

```tex
onçon \unsure{p.|pour} le biordre induit. D'autre part, le bord d'un tronçon est défini Comme des}

\unsure{Tronçons|Tronçon} de la ligne : parties
de la forme

\[
\left\{\begin{aligned}
 &[s,t] &&s\leq t\\
 &\mathopen{]}-\in
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/008_heads.jpg

Alignment requires recheck: no flag

Review note: Cancelled de and the old/new heading endings remain compressed or overwritten.

### C-008-U008 (C line 21)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 21.

Source C token:

```tex
\unsure{\mathcal L|L}
```

Source C context:

```tex
igned}
 &[s,t] &&s\leq t\\
 &\mathopen{]}-\infty,s],\quad\text{ou}\quad [s,+\infty\mathclose{[}\\
 &\unsure{\mathcal L|L}=\mathopen{]}-\infty,+\infty\mathclose{[}
\end{aligned}\right.
\]

Bord du tronçon : $\{s,t\}$ dans 
```

Aligned final span:

```tex
\mathcal L
```

Final context (up to 100 characters either side):

```tex
igned}
 &[s,t] &&s\leq t\\
 &\mathopen{]}-\infty,s],\quad\text{ou}\quad [s,+\infty\mathclose{[}\\
 &\mathcal L=\mathopen{]}-\infty,+\infty\mathclose{[}
\end{aligned}\right.
\]

Bord du tronçon : $\{s,t\}$ dans 
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/008_formula.jpg

Alignment requires recheck: no flag

Review note: Ground-set L has the same looped sweep as the surrounding script forms.

### C-008-U009 (C line 30)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 30.

Source C token:

```tex
\unsure{:|}
```

Source C context:

```tex
nothing$ \inserted{troisième}

Deux tronçons sont dits en
position relative modérée, si leurs
bords \unsure{:|} \unsure{le|les} sont.

\uline{Partie} \uline{modérée} :
réunion \inserted{finie} de tronçons \inser
```

Aligned final span:

```tex
:
```

Final context (up to 100 characters either side):

```tex
nothing$ \inserted{troisième}

Deux tronçons sont dits en
position relative modérée, si leurs
bords : le sont.

\uline{Partie} \uline{modérée} :
réunion \inserted{finie} de tronçons \inserted{en positi
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/008_bottom.jpg

Alignment requires recheck: no flag

Review note: Colon after bords, singular le, crossed Donc and accented définition are distinguishable.

### C-008-U010 (C line 30)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 30.

Source C token:

```tex
\unsure{le|les}
```

Source C context:

```tex
serted{troisième}

Deux tronçons sont dits en
position relative modérée, si leurs
bords \unsure{:|} \unsure{le|les} sont.

\uline{Partie} \uline{modérée} :
réunion \inserted{finie} de tronçons \inserted{en position}
```

Aligned final span:

```tex
le
```

Final context (up to 100 characters either side):

```tex
thing$ \inserted{troisième}

Deux tronçons sont dits en
position relative modérée, si leurs
bords : le sont.

\uline{Partie} \uline{modérée} :
réunion \inserted{finie} de tronçons \inserted{en position}
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/008_bottom.jpg

Alignment requires recheck: no flag

Review note: Colon after bords, singular le, crossed Donc and accented définition are distinguishable.

### C-008-U011 (C line 34)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 34.

Source C token:

```tex
\unsure{Donc}
```

Source C context:

```tex
éunion \inserted{finie} de tronçons \inserted{en position} mutuelle
modérée, et disjoints. \deleted{\unsure{Donc}} Par
\unsure{définition|definition}, son bord est la réunion
(disjointe) des bords.

% paper waterm
```

Aligned final span:

```tex
Donc
```

Final context (up to 100 characters either side):

```tex
éunion \inserted{finie} de tronçons \inserted{en position} mutuelle
modérée, et disjoints. \deleted{Donc} Par
définition, son bord est la réunion
(disjointe) des bords.

% paper watermark; clipped at the 
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/008_bottom.jpg

Alignment requires recheck: no flag

Review note: Colon after bords, singular le, crossed Donc and accented définition are distinguishable.

### C-008-U012 (C line 35)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 35.

Source C token:

```tex
\unsure{définition|definition}
```

Source C context:

```tex
nie} de tronçons \inserted{en position} mutuelle
modérée, et disjoints. \deleted{\unsure{Donc}} Par
\unsure{définition|definition}, son bord est la réunion
(disjointe) des bords.

% paper watermark; clipped at the two sheet edges

```

Aligned final span:

```tex
définition
```

Final context (up to 100 characters either side):

```tex
serted{finie} de tronçons \inserted{en position} mutuelle
modérée, et disjoints. \deleted{Donc} Par
définition, son bord est la réunion
(disjointe) des bords.

% paper watermark; clipped at the two sheet edges

```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/008_bottom.jpg

Alignment requires recheck: no flag

Review note: Colon after bords, singular le, crossed Donc and accented définition are distinguishable.

### C-008-U013 (C line 39)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 39.

Source C token:

```tex
\unsure{r}
```

Source C context:

```tex
on
(disjointe) des bords.

% paper watermark; clipped at the two sheet edges
\rotatebox{90}{\textsc{\unsure{r}ong Extra Stro}}

```

Aligned final span:

```tex
\unsure{r}
```

Final context (up to 100 characters either side):

```tex
on
(disjointe) des bords.

% paper watermark; clipped at the two sheet edges
\rotatebox{90}{\textsc{\unsure{r}ong Extra Stro}}

```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/008_top.jpg

Alignment requires recheck: no flag

Review note: Clipped first outline letter of the watermark remains doubtful.

### C-009-U001 (C line 10)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 10.

Source C token:

```tex
\unsure{\mathcal L|L}
```

Source C context:

```tex
(comme structure de réseau).}
\deleted{Segment}

\uline{Définition}\quad Un ens. ordonné \inserted{$\unsure{\mathcal L|L}$} est appelé un \uline{tronçon} \uline{ordonné} si

\unsure{a}) $\forall\,a\in\mathcal L$ tel que $
```

Aligned final span:

```tex
\mathcal L
```

Final context (up to 100 characters either side):

```tex
(comme structure de réseau).}
\deleted{Segment}

\uline{Définition}\quad Un ens. ordonné \inserted{$\mathcal L$} est appelé un \uline{tronçon} \uline{ordonné} si

\unsure{a}) $\forall\,a\in\mathcal L$ tel que $
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/009_top.jpg

Alignment requires recheck: no flag

Review note: Inserted ground-set symbol has the looped script-L form.

### C-009-U002 (C line 12)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 12.

Source C token:

```tex
\unsure{a}
```

Source C context:

```tex
n ens. ordonné \inserted{$\unsure{\mathcal L|L}$} est appelé un \uline{tronçon} \uline{ordonné} si

\unsure{a}) $\forall\,a\in\mathcal L$ tel que $\mathcal L_{>a}\deleted{\unsure{\sim|=}}\unsure{\ne|=}\varnothi
```

Aligned final span:

```tex
\unsure{a}
```

Final context (up to 100 characters either side):

```tex
ion}\quad Un ens. ordonné \inserted{$\mathcal L$} est appelé un \uline{tronçon} \uline{ordonné} si

\unsure{a}) $\forall\,a\in\mathcal L$ tel que $\mathcal L_{>a}\deleted{\unsure{\sim|=}}\unsure{\ne|=}\varnothi
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/009_a.jpg

Alignment requires recheck: no flag

Review note: Dense label and equality/inequality overlay remain unclear; old variable cannot be confidently separated from the strike.

### C-009-U003 (C line 12)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 12.

Source C token:

```tex
\unsure{\sim|=}
```

Source C context:

```tex
tronçon} \uline{ordonné} si

\unsure{a}) $\forall\,a\in\mathcal L$ tel que $\mathcal L_{>a}\deleted{\unsure{\sim|=}}\unsure{\ne|=}\varnothing$, $\mathcal L_{>a}$ est filtrant décroissant
\deleted{i.e. $\forall\,x,y$
```

Aligned final span:

```tex
\unsure{\sim|=}
```

Final context (up to 100 characters either side):

```tex
tronçon} \uline{ordonné} si

\unsure{a}) $\forall\,a\in\mathcal L$ tel que $\mathcal L_{>a}\deleted{\unsure{\sim|=}}\unsure{\ne|=}\varnothing$, $\mathcal L_{>a}$ est filtrant décroissant
\deleted{i.e. $\forall\,x,y$
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/009_a.jpg

Alignment requires recheck: no flag

Review note: Dense label and equality/inequality overlay remain unclear; old variable cannot be confidently separated from the strike.

### C-009-U004 (C line 12)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 12.

Source C token:

```tex
\unsure{\ne|=}
```

Source C context:

```tex
ordonné} si

\unsure{a}) $\forall\,a\in\mathcal L$ tel que $\mathcal L_{>a}\deleted{\unsure{\sim|=}}\unsure{\ne|=}\varnothing$, $\mathcal L_{>a}$ est filtrant décroissant
\deleted{i.e. $\forall\,x,y$ $\unsure{a|x},
```

Aligned final span:

```tex
\unsure{\ne|=}
```

Final context (up to 100 characters either side):

```tex
ordonné} si

\unsure{a}) $\forall\,a\in\mathcal L$ tel que $\mathcal L_{>a}\deleted{\unsure{\sim|=}}\unsure{\ne|=}\varnothing$, $\mathcal L_{>a}$ est filtrant décroissant
\deleted{i.e. $\forall\,x,y$ $\unsure{a|x},
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/009_a.jpg

Alignment requires recheck: no flag

Review note: Dense label and equality/inequality overlay remain unclear; old variable cannot be confidently separated from the strike.

### C-009-U005 (C line 13)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 13.

Source C token:

```tex
\unsure{a|x}
```

Source C context:

```tex
unsure{\ne|=}\varnothing$, $\mathcal L_{>a}$ est filtrant décroissant
\deleted{i.e. $\forall\,x,y$ $\unsure{a|x},y$ tels que} \inserted{si $a,y,a\in\mathcal L$ tels que}
$a>a$, $y>a$ alors $\exists\,z\in\mathcal 
```

Aligned final span:

```tex
\unsure{a|x}
```

Final context (up to 100 characters either side):

```tex
unsure{\ne|=}\varnothing$, $\mathcal L_{>a}$ est filtrant décroissant
\deleted{i.e. $\forall\,x,y$ $\unsure{a|x},y$ tels que} \inserted{si $a,y,\unsure{a|x}\in\mathcal L$ tels que}
$a>a$, $y>a$ alors $\exists\,z\
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/009_a.jpg

Alignment requires recheck: no flag

Review note: Dense label and equality/inequality overlay remain unclear; old variable cannot be confidently separated from the strike.

### C-009-U006 (C line 16)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 16.

Source C token:

```tex
\unsure{b|a}
```

Source C context:

```tex
\in\mathcal L$ tels que}
$a>a$, $y>a$ alors $\exists\,z\in\mathcal L$ avec $x,y\geq z>a$

$\deleted{\unsure{b|a}}a'$) Axiome dual : si $a,x,y\in\mathcal L$ tels \unsure{q|que}
$\unsure{x|a}<a$, $y<a$ alors $\exis
```

Aligned final span:

```tex
\unsure{b|a}
```

Final context (up to 100 characters either side):

```tex
\in\mathcal L$ tels que}
$a>a$, $y>a$ alors $\exists\,z\in\mathcal L$ avec $x,y\geq z>a$

$\deleted{\unsure{b|a}}a'$) Axiome dual : si $a,x,y\in\mathcal L$ tels q
$\unsure{x|a}<a$, $y<a$ alors $\exists\,z\in\math
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/009_dual.jpg

Alignment requires recheck: no flag

Review note: Old label and the first variable in the dual inequality remain ambiguous.

### C-009-U007 (C line 16)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 16.

Source C token:

```tex
\unsure{q|que}
```

Source C context:

```tex
thcal L$ avec $x,y\geq z>a$

$\deleted{\unsure{b|a}}a'$) Axiome dual : si $a,x,y\in\mathcal L$ tels \unsure{q|que}
$\unsure{x|a}<a$, $y<a$ alors $\exists\,z\in\mathcal L$ avec $a,y\leq z<a$

b) $\mathcal L$ est fil
```

Aligned final span:

```tex
q
```

Final context (up to 100 characters either side):

```tex
thcal L$ avec $x,y\geq z>a$

$\deleted{\unsure{b|a}}a'$) Axiome dual : si $a,x,y\in\mathcal L$ tels q
$\unsure{x|a}<a$, $y<a$ alors $\exists\,z\in\mathcal L$ avec $a,y\leq z<a$

b) $\mathcal L$ est fil
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/009_dual.jpg

Alignment requires recheck: no flag

Review note: Only the single abbreviated q is present at the clipped line ending; no ue added.

### C-009-U008 (C line 17)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 17.

Source C token:

```tex
\unsure{x|a}
```

Source C context:

```tex
,y\geq z>a$

$\deleted{\unsure{b|a}}a'$) Axiome dual : si $a,x,y\in\mathcal L$ tels \unsure{q|que}
$\unsure{x|a}<a$, $y<a$ alors $\exists\,z\in\mathcal L$ avec $a,y\leq z<a$

b) $\mathcal L$ est filt\unsure{ant|r
```

Aligned final span:

```tex
\unsure{x|a}
```

Final context (up to 100 characters either side):

```tex
al L$ avec $x,y\geq z>a$

$\deleted{\unsure{b|a}}a'$) Axiome dual : si $a,x,y\in\mathcal L$ tels q
$\unsure{x|a}<a$, $y<a$ alors $\exists\,z\in\mathcal L$ avec $a,y\leq z<a$

b) $\mathcal L$ est filt\unsure{ant|r
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/009_dual.jpg

Alignment requires recheck: no flag

Review note: Old label and the first variable in the dual inequality remain ambiguous.

### C-009-U009 (C line 19)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 19.

Source C token:

```tex
\unsure{ant|rant}
```

Source C context:

```tex
$\unsure{x|a}<a$, $y<a$ alors $\exists\,z\in\mathcal L$ avec $a,y\leq z<a$

b) $\mathcal L$ est filt\unsure{ant|rant} croissant et filtrant décroissant i.e.
$x,y\in\mathcal L\Rightarrow\exists\,a,b\in\mathcal L$ avec 
```

Aligned final span:

```tex
\unsure{ant|rant}
```

Final context (up to 100 characters either side):

```tex
$\unsure{x|a}<a$, $y<a$ alors $\exists\,z\in\mathcal L$ avec $a,y\leq z<a$

b) $\mathcal L$ est filt\unsure{ant|rant} croissant et filtrant décroissant i.e.
$x,y\in\mathcal L\Rightarrow\exists\,a,b\in\mathcal L$ avec 
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/009_bc.jpg

Alignment requires recheck: no flag

Review note: The compact middle strokes do not settle whether r is written in filtrant.

### C-009-U010 (C line 24)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 24.

Source C token:

```tex
\unsure{\ne|=}
```

Source C context:

```tex


c) Si $x,y\in\mathcal L$ tels que $x<y$, $\exists\,z$ tel que $x<z<y$ .

d) $\deleted{\mathcal L\,\unsure{\ne|=}}$ $\operatorname{Card}\mathcal L>1$ \deleted{\unsure{(imp.|(}}

% slanted
\margin{\uline{NB} les co
```

Aligned final span:

```tex
\unsure{\ne|=}
```

Final context (up to 100 characters either side):

```tex


c) Si $x,y\in\mathcal L$ tels que $x<y$, $\exists\,z$ tel que $x<z<y$ .

d) $\deleted{\mathcal L\,\unsure{\ne|=}}$ $\operatorname{Card}\mathcal L>1$ \deleted{\unsure{(imp.|(}}

% slanted
\margin{\uline{NB} les co
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/009_bottom.jpg

Alignment requires recheck: no flag

Review note: Cancelled relation and the two short parenthetic starts remain partly overwritten.

### C-009-U011 (C line 24)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 24.

Source C token:

```tex
\unsure{(imp.|(}
```

Source C context:

```tex
que $x<z<y$ .

d) $\deleted{\mathcal L\,\unsure{\ne|=}}$ $\operatorname{Card}\mathcal L>1$ \deleted{\unsure{(imp.|(}}

% slanted
\margin{\uline{NB} les cond\unsure{.|} $a\ a'\ b)\ c)$ sont satisfaites si $\operatorna
```

Aligned final span:

```tex
\unsure{(imp.|(}
```

Final context (up to 100 characters either side):

```tex
que $x<z<y$ .

d) $\deleted{\mathcal L\,\unsure{\ne|=}}$ $\operatorname{Card}\mathcal L>1$ \deleted{\unsure{(imp.|(}}

% slanted
\margin{\uline{NB} les cond $a\ a'\ b)\ c)$ sont satisfaites si $\operatorname{card}\ma
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/009_bottom.jpg

Alignment requires recheck: no flag

Review note: Cancelled relation and the two short parenthetic starts remain partly overwritten.

### C-009-U012 (C line 27)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 27.

Source C token:

```tex
\unsure{.|}
```

Source C context:

```tex
 $\operatorname{Card}\mathcal L>1$ \deleted{\unsure{(imp.|(}}

% slanted
\margin{\uline{NB} les cond\unsure{.|} $a\ a'\ b)\ c)$ sont satisfaites si $\operatorname{card}\mathcal L\leq1$ !}

On dit que $\mathcal L
```

Aligned final span:

```tex

```

Final context (up to 100 characters either side):

```tex
 $\operatorname{Card}\mathcal L>1$ \deleted{\unsure{(imp.|(}}

% slanted
\margin{\uline{NB} les cond $a\ a'\ b)\ c)$ sont satisfaites si $\operatorname{card}\mathcal L\leq1$ !}

On dit que $\mathcal L
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/009_margin.jpg

Alignment requires recheck: no flag

Review note: No separate point follows cond in the rotated note.

### C-009-U013 (C line 30)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 30.

Source C token:

```tex
\unsure{(p.|(}
```

Source C context:

```tex
dit que $\mathcal L$ est un \uline{segment} si de plus $\mathcal L$ admet un plus petit et
\deleted{\unsure{(p.|(}} un plus grand élément, un \uline{intervalle} s'il n'admet ni l'un ni l'autre,

% paper watermark, 
```

Aligned final span:

```tex
\unsure{(p.|(}
```

Final context (up to 100 characters either side):

```tex
dit que $\mathcal L$ est un \uline{segment} si de plus $\mathcal L$ admet un plus petit et
\deleted{\unsure{(p.|(}} un plus grand élément, un \uline{intervalle} s'il n'admet ni l'un ni l'autre,

% paper watermark, 
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/009_bottom.jpg

Alignment requires recheck: no flag

Review note: Cancelled relation and the two short parenthetic starts remain partly overwritten.

### C-009-U014 (C line 33)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 33.

Source C token:

```tex
\unsure{n}
```

Source C context:

```tex
'il n'admet ni l'un ni l'autre,

% paper watermark, visible from the reverse
\rotatebox{90}{\textsc{\unsure{n}g Extra Stro}}

```

Aligned final span:

```tex
\unsure{n}
```

Final context (up to 100 characters either side):

```tex
'il n'admet ni l'un ni l'autre,

% paper watermark, visible from the reverse
\rotatebox{90}{\textsc{\unsure{n}g Extra Stro}}

```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/009_top.jpg

Alignment requires recheck: no flag

Review note: Initial watermark letter remains clipped and uncertain.

### C-010-U001 (C line 4)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 3.

Source C token:

```tex
\unsure{élément}
```

Source C context:

```tex
page{10}\mspage{9}
% ink top, lines 1–3
un \uline{demi}-\uline{intervalle} s'il admet un plus petit \unsure{élément} mais pas un plus grand, ou bien l'inverse.

% ink upper middle, NB, lines 1–4
\deleted{\unsure{L'op
```

Aligned final span:

```tex
élément
```

Final context (up to 100 characters either side):

```tex
page{10}\mspage{9}
% ink top, lines 1–3
un \uline{demi}-\uline{intervalle} s'il admet un plus petit élément mais pas un plus grand, ou bien l'inverse.

% ink upper middle, NB, lines 1–4
\deleted{\unsure{L'op
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/010_top.jpg

Alignment requires recheck: no flag

Review note: Full élément and inversement are legible at the line endings.

### C-010-U002 (C line 7)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 6.

Source C token:

```tex
\unsure{L'opposé|L'oppo}
```

Source C context:

```tex
ure{élément} mais pas un plus grand, ou bien l'inverse.

% ink upper middle, NB, lines 1–4
\deleted{\unsure{L'opposé|L'oppo}}\inserted{\uline{NB}} L'opposé d'un tronçon, segment, intervalle, demi-intervalle est itou. L'oppos
```

Aligned final span:

```tex
\unsure{L'opposé|L'oppo}
```

Final context (up to 100 characters either side):

```tex
etit élément mais pas un plus grand, ou bien l'inverse.

% ink upper middle, NB, lines 1–4
\deleted{\unsure{L'opposé|L'oppo}}\inserted{\uline{NB}} L'opposé d'un tronçon, segment, intervalle, demi-intervalle est itou. L'oppos
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/010_top.jpg

Alignment requires recheck: no flag

Review note: Cancelled L’opposé start remains partly crossed and may be abbreviated.

### C-010-U003 (C line 7)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 6.

Source C token:

```tex
\unsure{inversement}
```

Source C context:

```tex
ervalle, demi-intervalle est itou. L'opposé d'un $1/2$ intervalle fermé à g. est fermé à droite, et \unsure{inversement}.
% ink left, slanting upwards beside NB
% slanted
\margin{Dans \unsure{ma|sa} \unsure{actuelle|init
```

Aligned final span:

```tex
inversement
```

Final context (up to 100 characters either side):

```tex
ervalle, demi-intervalle est itou. L'opposé d'un $1/2$ intervalle fermé à g. est fermé à droite, et inversement.
% ink left, slanting upwards beside NB
% slanted
\margin{Dans ma actuelle terminologie, tronçon \u
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/010_top.jpg

Alignment requires recheck: no flag

Review note: Full élément and inversement are legible at the line endings.

### C-010-U004 (C line 10)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 9.

Source C token:

```tex
\unsure{ma|sa}
```

Source C context:

```tex
mé à droite, et \unsure{inversement}.
% ink left, slanting upwards beside NB
% slanted
\margin{Dans \unsure{ma|sa} \unsure{actuelle|initiale} \unsure{terminologie}, tronçon \unsure{est|être|était|etre} \unsure{``en
```

Aligned final span:

```tex
ma
```

Final context (up to 100 characters either side):

```tex
. est fermé à droite, et inversement.
% ink left, slanting upwards beside NB
% slanted
\margin{Dans ma actuelle terminologie, tronçon \unsure{est|être|était|etre} \unsure{``ens|ens|un|équiv} \uline{bior
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/010_margin.jpg

Alignment requires recheck: no flag

Review note: Rotated margin supports ma actuelle terminologie and the complete underlined biordre.

### C-010-U005 (C line 10)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 9.

Source C token:

```tex
\unsure{actuelle|initiale}
```

Source C context:

```tex
 \unsure{inversement}.
% ink left, slanting upwards beside NB
% slanted
\margin{Dans \unsure{ma|sa} \unsure{actuelle|initiale} \unsure{terminologie}, tronçon \unsure{est|être|était|etre} \unsure{``ens|ens|un|équiv} \uline{\uns
```

Aligned final span:

```tex
actuelle
```

Final context (up to 100 characters either side):

```tex
st fermé à droite, et inversement.
% ink left, slanting upwards beside NB
% slanted
\margin{Dans ma actuelle terminologie, tronçon \unsure{est|être|était|etre} \unsure{``ens|ens|un|équiv} \uline{biordre}}

% 
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/010_margin.jpg

Alignment requires recheck: no flag

Review note: Rotated margin supports ma actuelle terminologie and the complete underlined biordre.

### C-010-U006 (C line 10)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 9.

Source C token:

```tex
\unsure{terminologie}
```

Source C context:

```tex
k left, slanting upwards beside NB
% slanted
\margin{Dans \unsure{ma|sa} \unsure{actuelle|initiale} \unsure{terminologie}, tronçon \unsure{est|être|était|etre} \unsure{``ens|ens|un|équiv} \uline{\unsure{biordre|biordonné}
```

Aligned final span:

```tex
terminologie
```

Final context (up to 100 characters either side):

```tex
à droite, et inversement.
% ink left, slanting upwards beside NB
% slanted
\margin{Dans ma actuelle terminologie, tronçon \unsure{est|être|était|etre} \unsure{``ens|ens|un|équiv} \uline{biordre}}

% ink middle, T
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/010_margin.jpg

Alignment requires recheck: no flag

Review note: Rotated margin supports ma actuelle terminologie and the complete underlined biordre.

### C-010-U007 (C line 10)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 9.

Source C token:

```tex
\unsure{est|être|était|etre}
```

Source C context:

```tex
 NB
% slanted
\margin{Dans \unsure{ma|sa} \unsure{actuelle|initiale} \unsure{terminologie}, tronçon \unsure{est|être|était|etre} \unsure{``ens|ens|un|équiv} \uline{\unsure{biordre|biordonné}}}

% ink middle, Tout, lines 1–3
\del
```

Aligned final span:

```tex
\unsure{est|être|était|etre}
```

Final context (up to 100 characters either side):

```tex
nt.
% ink left, slanting upwards beside NB
% slanted
\margin{Dans ma actuelle terminologie, tronçon \unsure{est|être|était|etre} \unsure{``ens|ens|un|équiv} \uline{biordre}}

% ink middle, Tout, lines 1–3
\deleted{\unsure{Lorsqu
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/010_margin.jpg

Alignment requires recheck: no flag

Review note: The copula and the following compact quoted/abbreviated group remain unresolved.

### C-010-U008 (C line 10)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 9.

Source C token:

```tex
\unsure{``ens|ens|un|équiv}
```

Source C context:

```tex
nsure{ma|sa} \unsure{actuelle|initiale} \unsure{terminologie}, tronçon \unsure{est|être|était|etre} \unsure{``ens|ens|un|équiv} \uline{\unsure{biordre|biordonné}}}

% ink middle, Tout, lines 1–3
\deleted{\unsure{Lorsque|Lorsqu.
```

Aligned final span:

```tex
\unsure{``ens|ens|un|équiv}
```

Final context (up to 100 characters either side):

```tex
rds beside NB
% slanted
\margin{Dans ma actuelle terminologie, tronçon \unsure{est|être|était|etre} \unsure{``ens|ens|un|équiv} \uline{biordre}}

% ink middle, Tout, lines 1–3
\deleted{\unsure{Lorsque|Lorsqu.}}\inserted{Tout} t
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/010_margin.jpg

Alignment requires recheck: no flag

Review note: The copula and the following compact quoted/abbreviated group remain unresolved.

### C-010-U009 (C line 10)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 9.

Source C token:

```tex
\unsure{biordre|biordonné}
```

Source C context:

```tex
ale} \unsure{terminologie}, tronçon \unsure{est|être|était|etre} \unsure{``ens|ens|un|équiv} \uline{\unsure{biordre|biordonné}}}

% ink middle, Tout, lines 1–3
\deleted{\unsure{Lorsque|Lorsqu.}}\inserted{Tout} tronçon est l'un
```

Aligned final span:

```tex
biordre
```

Final context (up to 100 characters either side):

```tex
s ma actuelle terminologie, tronçon \unsure{est|être|était|etre} \unsure{``ens|ens|un|équiv} \uline{biordre}}

% ink middle, Tout, lines 1–3
\deleted{\unsure{Lorsque|Lorsqu.}}\inserted{Tout} tronçon est l'un
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/010_margin.jpg

Alignment requires recheck: no flag

Review note: Rotated margin supports ma actuelle terminologie and the complete underlined biordre.

### C-010-U010 (C line 13)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 12.

Source C token:

```tex
\unsure{Lorsque|Lorsqu.}
```

Source C context:

```tex
ure{``ens|ens|un|équiv} \uline{\unsure{biordre|biordonné}}}

% ink middle, Tout, lines 1–3
\deleted{\unsure{Lorsque|Lorsqu.}}\inserted{Tout} tronçon est l'un des trois (segment, $1/2$ intervalle, intervalle) à l'exclusion \u
```

Aligned final span:

```tex
\unsure{Lorsque|Lorsqu.}
```

Final context (up to 100 characters either side):

```tex
re|était|etre} \unsure{``ens|ens|un|équiv} \uline{biordre}}

% ink middle, Tout, lines 1–3
\deleted{\unsure{Lorsque|Lorsqu.}}\inserted{Tout} tronçon est l'un des trois (segment, $1/2$ intervalle, intervalle) à l'exclusion de
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/010_tout.jpg

Alignment requires recheck: no flag

Review note: The old word is crossed and its final letter/point cannot be settled.

### C-010-U011 (C line 13)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 12.

Source C token:

```tex
\unsure{des}
```

Source C context:

```tex
.}}\inserted{Tout} tronçon est l'un des trois (segment, $1/2$ intervalle, intervalle) à l'exclusion \unsure{des} deux autres.

% ink lower middle, Si L
Si $\mathcal L$ est un tronçon, on pose $\deleted{\unsure{\p
```

Aligned final span:

```tex
des
```

Final context (up to 100 characters either side):

```tex
.}}\inserted{Tout} tronçon est l'un des trois (segment, $1/2$ intervalle, intervalle) à l'exclusion des deux autres.

% ink lower middle, Si L
Si $\mathcal L$ est un tronçon, on pose $\deleted{\unsure{\p
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/010_tout.jpg

Alignment requires recheck: no flag

Review note: Des is visible before deux autres.

### C-010-U012 (C line 16)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 15.

Source C token:

```tex
\unsure{\partial L}
```

Source C context:

```tex
nsure{des} deux autres.

% ink lower middle, Si L
Si $\mathcal L$ est un tronçon, on pose $\deleted{\unsure{\partial L}=}$
\[
\begin{aligned}
\unsure{\partial L|\partial}&=\bigl\{\,x\in L\mid
\begin{aligned}&x\text{ est
```

Aligned final span:

```tex
\unsure{\partial L}
```

Final context (up to 100 characters either side):

```tex
lusion des deux autres.

% ink lower middle, Si L
Si $\mathcal L$ est un tronçon, on pose $\deleted{\unsure{\partial L}=}$
\[
\begin{aligned}
\unsure{\partial|\partial L}&=\bigl\{\,x\in L\mid
\begin{aligned}&x\text{ est
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/010_boundary.jpg

Alignment requires recheck: no flag

Review note: The crossed boundary symbol and whether the live partial has a ground-set L remain uncertain.

### C-010-U013 (C line 19)

Mechanical state: **unsure token(s) overlap changed alignment; inspect**. Final aligned line: 18.

Source C token:

```tex
\unsure{\partial L|\partial}
```

Source C context:

```tex
e, Si L
Si $\mathcal L$ est un tronçon, on pose $\deleted{\unsure{\partial L}=}$
\[
\begin{aligned}
\unsure{\partial L|\partial}&=\bigl\{\,x\in L\mid
\begin{aligned}&x\text{ est plus petit élément}\\
&\text{ou plus grand \unsure
```

Aligned final span:

```tex
\unsure{\partial|\partial L}
```

Final context (up to 100 characters either side):

```tex
e, Si L
Si $\mathcal L$ est un tronçon, on pose $\deleted{\unsure{\partial L}=}$
\[
\begin{aligned}
\unsure{\partial|\partial L}&=\bigl\{\,x\in L\mid
\begin{aligned}&x\text{ est plus petit élément}\\
&\text{ou plus grand élément
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/010_boundary.jpg

Alignment requires recheck: no flag

Review note: The crossed boundary symbol and whether the live partial has a ground-set L remain uncertain.

### C-010-U014 (C line 21)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 20.

Source C token:

```tex
\unsure{élément|élt}
```

Source C context:

```tex
artial}&=\bigl\{\,x\in L\mid
\begin{aligned}&x\text{ est plus petit élément}\\
&\text{ou plus grand \unsure{élément|élt}}\end{aligned}\,\bigr\}
\end{aligned}
\]
\deleted{\illegible{1}}

% ink bottom, Soit and first equal
```

Aligned final span:

```tex
élément
```

Final context (up to 100 characters either side):

```tex
tial L}&=\bigl\{\,x\in L\mid
\begin{aligned}&x\text{ est plus petit élément}\\
&\text{ou plus grand élément}\end{aligned}\,\bigr\}
\end{aligned}
\]
\deleted{\illegible{1}}

% ink bottom, Soit and first equal
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/010_boundary.jpg

Alignment requires recheck: no flag

Review note: Full élément, not an abbreviation, is visible in the set description.

### C-010-U015 (C line 30)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 29.

Source C token:

```tex
\unsure{\mathscr S|S}
```

Source C context:

```tex
ible{1}}

% ink bottom, Soit and first equality
Soit $\mathcal L$ un tronçon, et
\[
\begin{aligned}
\unsure{\mathscr S|S}_0(L)=\mathrm{Drap}_2(L)&=\{\,\unsure{E|\mathcal E}\in\unsure{\mathrm P|\mathscr P}_2(L)\mid E\text{
```

Aligned final span:

```tex
S_0(\mathcal 
```

Final context (up to 100 characters either side):

```tex
ible{1}}

% ink bottom, Soit and first equality
Soit $\mathcal L$ un tronçon, et
\[
\begin{aligned}
S_0(\mathcal L)=\mathrm{Drap}_2(\mathcal L)&=\{\,\unsure{\varepsilon|\mathcal E|E}\in P_2(\mathcal L)\mid \unsure
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/010_bottom.jpg

Alignment requires recheck: no flag

Review note: Rounded plain S, single-staff angular P and full-height f after Mod are distinguishable.

### C-010-U016 (C line 30)

Mechanical state: **unsure token(s) overlap changed alignment; inspect**. Final aligned line: 29.

Source C token:

```tex
\unsure{E|\mathcal E}
```

Source C context:

```tex
t $\mathcal L$ un tronçon, et
\[
\begin{aligned}
\unsure{\mathscr S|S}_0(L)=\mathrm{Drap}_2(L)&=\{\,\unsure{E|\mathcal E}\in\unsure{\mathrm P|\mathscr P}_2(L)\mid E\text{ tot ordonné}\,\}\\
&=\{\,\{x,y\}\mid x<y\,\}
\end{
```

Aligned final span:

```tex
\unsure{\varepsilon|\mathcal E|E}
```

Final context (up to 100 characters either side):

```tex
oit $\mathcal L$ un tronçon, et
\[
\begin{aligned}
S_0(\mathcal L)=\mathrm{Drap}_2(\mathcal L)&=\{\,\unsure{\varepsilon|\mathcal E|E}\in P_2(\mathcal L)\mid \unsure{\varepsilon|\mathcal E|E}\text{ tot ordonné}\,\}\\
&=\{\,\{x,y\}\mid
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: revised

Crop links: crops/010_bottom.jpg

Alignment requires recheck: no flag

Review note: The two occurrences share a rounded epsilon/E shape; epsilon is retained first, with E/script E alternatives.

### C-010-U017 (C line 30)

Mechanical state: **unsure token(s) overlap changed alignment; inspect**. Final aligned line: 29.

Source C token:

```tex
\unsure{\mathrm P|\mathscr P}
```

Source C context:

```tex
n, et
\[
\begin{aligned}
\unsure{\mathscr S|S}_0(L)=\mathrm{Drap}_2(L)&=\{\,\unsure{E|\mathcal E}\in\unsure{\mathrm P|\mathscr P}_2(L)\mid E\text{ tot ordonné}\,\}\\
&=\{\,\{x,y\}\mid x<y\,\}
\end{aligned}
\]
% ink bottom, final 
```

Aligned final span:

```tex
 P_2(\mathcal L)\mid \unsure{\varepsilon|\mathcal
```

Final context (up to 100 characters either side):

```tex
begin{aligned}
S_0(\mathcal L)=\mathrm{Drap}_2(\mathcal L)&=\{\,\unsure{\varepsilon|\mathcal E|E}\in P_2(\mathcal L)\mid \unsure{\varepsilon|\mathcal E|E}\text{ tot ordonné}\,\}\\
&=\{\,\{x,y\}\mid x<y\,\}
\end{aligned}
\]
% ink bottom, final equali
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/010_bottom.jpg

Alignment requires recheck: no flag

Review note: Rounded plain S, single-staff angular P and full-height f after Mod are distinguishable. Alignment recheck: A TeX command delimiter space was added; the image-reviewed P_2 remains unchanged.

### C-010-U018 (C line 36)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 35.

Source C token:

```tex
\unsure{\mathrm{Modf}|\mathrm{Mod}_{f}}
```

Source C context:

```tex
\,\}\\
&=\{\,\{x,y\}\mid x<y\,\}
\end{aligned}
\]
% ink bottom, final equality
\[
\text{D'où}\qquad \unsure{\mathrm{Modf}|\mathrm{Mod}_{f}}(L)=\mathrm{Drap}(L)
=\{\,S\subset\mathrm P_f(L)\mid S\,\substack{\text{tot}\\\text{ord}}\,\}
\]

```

Aligned final span:

```tex
\mathrm{Modf}(\mathcal 
```

Final context (up to 100 characters either side):

```tex
\,\}\\
&=\{\,\{x,y\}\mid x<y\,\}
\end{aligned}
\]
% ink bottom, final equality
\[
\text{D'où}\qquad \mathrm{Modf}(\mathcal L)=\mathrm{Drap}(\mathcal L)
=\{\,S\subset P_f(\mathcal L)\mid S\,\substack{\text{tot}\\\text{ord}}\
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/010_bottom.jpg

Alignment requires recheck: no flag

Review note: Rounded plain S, single-staff angular P and full-height f after Mod are distinguishable.

### C-011-U001 (C line 3)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 3.

Source C token:

```tex
\unsure{\mathrm{Modf}|\mathrm{Mod}_{f}}
```

Source C context:

```tex
\scanpage{11}\mspage{10}
% ink top, Si S and C(S)
Si $S\in\unsure{\mathrm{Modf}|\mathrm{Mod}_{f}}(L)$, on a donc $\deleted{C(S)=}$
\[
C(S)=\{\,\deleted{\unsure{s|x}}t\in L\mid\deleted{\unsure{S\cup
```

Aligned final span:

```tex
\mathrm{Modf}(\mathcal 
```

Final context (up to 100 characters either side):

```tex
\scanpage{11}\mspage{10}
% ink top, Si S and C(S)
Si $S\in\mathrm{Modf}(\mathcal L)$, on a donc $\deleted{C(S)=}$
\[
C(S)=\{\,\deleted{\unsure{s|x}}t\in\mathcal L\mid\deleted{\unsur
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/011_top.jpg

Alignment requires recheck: no flag

Review note: Full-height f continues Mod on the baseline.

### C-011-U002 (C line 5)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 5.

Source C token:

```tex
\unsure{s|x}
```

Source C context:

```tex
 $S\in\unsure{\mathrm{Modf}|\mathrm{Mod}_{f}}(L)$, on a donc $\deleted{C(S)=}$
\[
C(S)=\{\,\deleted{\unsure{s|x}}t\in L\mid\deleted{\unsure{S\cup\{t\}}}\ t\notin S,\quad S\cup\{t\}\ \text{tot. ord}\,\}
\]

% ink 
```

Aligned final span:

```tex
\unsure{s|x}
```

Final context (up to 100 characters either side):

```tex
 Si S and C(S)
Si $S\in\mathrm{Modf}(\mathcal L)$, on a donc $\deleted{C(S)=}$
\[
C(S)=\{\,\deleted{\unsure{s|x}}t\in\mathcal L\mid\deleted{\unsure{S\cup\{t\}}}\ t\notin S,\quad S\cup\{t\}\ \text{tot. ord}\,\}
\]
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/011_top.jpg

Alignment requires recheck: no flag

Review note: Overwritten variable/set term and clipped final short group remain uncertain.

### C-011-U003 (C line 5)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 5.

Source C token:

```tex
\unsure{S\cup\{t\}}
```

Source C context:

```tex
hrm{Mod}_{f}}(L)$, on a donc $\deleted{C(S)=}$
\[
C(S)=\{\,\deleted{\unsure{s|x}}t\in L\mid\deleted{\unsure{S\cup\{t\}}}\ t\notin S,\quad S\cup\{t\}\ \text{tot. ord}\,\}
\]

% ink upper third, On a dit
On a dit comment 
```

Aligned final span:

```tex
\unsure{S\cup\{t\}}
```

Final context (up to 100 characters either side):

```tex
thcal L)$, on a donc $\deleted{C(S)=}$
\[
C(S)=\{\,\deleted{\unsure{s|x}}t\in\mathcal L\mid\deleted{\unsure{S\cup\{t\}}}\ t\notin S,\quad S\cup\{t\}\ \text{tot. ord}\,\}
\]

% ink upper third, On a dit
On a dit comment 
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/011_top.jpg

Alignment requires recheck: no flag

Review note: Overwritten variable/set term and clipped final short group remain uncertain.

### C-011-U004 (C line 9)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 9.

Source C token:

```tex
\unsure{où|à|.}
```

Source C context:

```tex


% ink upper third, On a dit
On a dit comment on décomposait en ``composantes connexes'' un $C(S)$ \unsure{où|à|.}
\[
 S=\{s_{\deleted{\unsure{0}}1},\ldots s_n\},\qquad s_{\deleted{\unsure{0}}1}<s_2,\!<\cdots<s_n\,
```

Aligned final span:

```tex
\unsure{où|à|.}
```

Final context (up to 100 characters either side):

```tex


% ink upper third, On a dit
On a dit comment on décomposait en ``composantes connexes'' un $C(S)$ \unsure{où|à|.}
\[
 S=\{s_{\unsure{p|1|0}},\ldots s_n\},\qquad s_{\unsure{p|1|0}}<s_2,\!<\cdots<s_n\,.
\]
Les comp.
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/011_top.jpg

Alignment requires recheck: no flag

Review note: Overwritten variable/set term and clipped final short group remain uncertain.

### C-011-U005 (C line 11)

Mechanical state: **unsure token(s) overlap changed alignment; inspect**. Final aligned line: 11.

Source C token:

```tex
\unsure{0}
```

Source C context:

```tex
it comment on décomposait en ``composantes connexes'' un $C(S)$ \unsure{où|à|.}
\[
 S=\{s_{\deleted{\unsure{0}}1},\ldots s_n\},\qquad s_{\deleted{\unsure{0}}1}<s_2,\!<\cdots<s_n\,.
\]
Les comp. connexes sont le
```

Aligned final span:

```tex
unsure{p|1|0}
```

Final context (up to 100 characters either side):

```tex
t
On a dit comment on décomposait en ``composantes connexes'' un $C(S)$ \unsure{où|à|.}
\[
 S=\{s_{\unsure{p|1|0}},\ldots s_n\},\qquad s_{\unsure{p|1|0}}<s_2,\!<\cdots<s_n\,.
\]
Les comp. connexes sont les ens non
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: revised

Crop links: crops/011_components.jpg

Alignment requires recheck: no flag

Review note: Four small first-index forms are p/1/0-like, without secure evidence of a separately cancelled zero and replacement one; uncertainty is kept at each occurrence.

### C-011-U006 (C line 11)

Mechanical state: **unsure token(s) overlap changed alignment; inspect**. Final aligned line: 11.

Source C token:

```tex
\unsure{0}
```

Source C context:

```tex
nexes'' un $C(S)$ \unsure{où|à|.}
\[
 S=\{s_{\deleted{\unsure{0}}1},\ldots s_n\},\qquad s_{\deleted{\unsure{0}}1}<s_2,\!<\cdots<s_n\,.
\]
Les comp. connexes sont les ens non vides parmi
\[
L_{<s_{\deleted{\unsu
```

Aligned final span:

```tex
unsure{p|1|0}
```

Final context (up to 100 characters either side):

```tex
composantes connexes'' un $C(S)$ \unsure{où|à|.}
\[
 S=\{s_{\unsure{p|1|0}},\ldots s_n\},\qquad s_{\unsure{p|1|0}}<s_2,\!<\cdots<s_n\,.
\]
Les comp. connexes sont les ens non vides parmi
\[
\mathcal L_{<s_{\unsure
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: revised

Crop links: crops/011_components.jpg

Alignment requires recheck: no flag

Review note: Four small first-index forms are p/1/0-like, without secure evidence of a separately cancelled zero and replacement one; uncertainty is kept at each occurrence.

### C-011-U007 (C line 15)

Mechanical state: **unsure token(s) overlap changed alignment; inspect**. Final aligned line: 15.

Source C token:

```tex
\unsure{0}
```

Source C context:

```tex
re{0}}1}<s_2,\!<\cdots<s_n\,.
\]
Les comp. connexes sont les ens non vides parmi
\[
L_{<s_{\deleted{\unsure{0}}1}},\quad \deleted{\unsure{L}}[s_{\deleted{\unsure{0}}1},s_2],\quad\ldots,\ [s_{n-1},s_n],\quad L_{
```

Aligned final span:

```tex
\unsure{p|1|0}
```

Final context (up to 100 characters either side):

```tex
{p|1|0}}<s_2,\!<\cdots<s_n\,.
\]
Les comp. connexes sont les ens non vides parmi
\[
\mathcal L_{<s_{\unsure{p|1|0}}},\quad \deleted{\unsure{L}}[s_{\unsure{p|1|0}},s_2],\quad\ldots,\ [s_{n-1},s_n],\quad \mathcal L_{
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: revised

Crop links: crops/011_components.jpg

Alignment requires recheck: no flag

Review note: Four small first-index forms are p/1/0-like, without secure evidence of a separately cancelled zero and replacement one; uncertainty is kept at each occurrence.

### C-011-U008 (C line 15)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 15.

Source C token:

```tex
\unsure{L}
```

Source C context:

```tex
\]
Les comp. connexes sont les ens non vides parmi
\[
L_{<s_{\deleted{\unsure{0}}1}},\quad \deleted{\unsure{L}}[s_{\deleted{\unsure{0}}1},s_2],\quad\ldots,\ [s_{n-1},s_n],\quad L_{>s_n}
\]
% ink middle, bracket
```

Aligned final span:

```tex
\unsure{L}
```

Final context (up to 100 characters either side):

```tex

Les comp. connexes sont les ens non vides parmi
\[
\mathcal L_{<s_{\unsure{p|1|0}}},\quad \deleted{\unsure{L}}[s_{\unsure{p|1|0}},s_2],\quad\ldots,\ [s_{n-1},s_n],\quad \mathcal L_{>s_n}
\]
% ink middle, brack
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/011_components.jpg

Alignment requires recheck: no flag

Review note: Crossed letter at the first interval remains L-like but obscured.

### C-011-U009 (C line 15)

Mechanical state: **unsure token(s) overlap changed alignment; inspect**. Final aligned line: 15.

Source C token:

```tex
\unsure{0}
```

Source C context:

```tex
nt les ens non vides parmi
\[
L_{<s_{\deleted{\unsure{0}}1}},\quad \deleted{\unsure{L}}[s_{\deleted{\unsure{0}}1},s_2],\quad\ldots,\ [s_{n-1},s_n],\quad L_{>s_n}
\]
% ink middle, bracketed cases
\[
\begin{align
```

Aligned final span:

```tex
unsure{p|1|0}
```

Final context (up to 100 characters either side):

```tex
xes sont les ens non vides parmi
\[
\mathcal L_{<s_{\unsure{p|1|0}}},\quad \deleted{\unsure{L}}[s_{\unsure{p|1|0}},s_2],\quad\ldots,\ [s_{n-1},s_n],\quad \mathcal L_{>s_n}
\]
% ink middle, bracketed cases
\[
\begi
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: revised

Crop links: crops/011_components.jpg

Alignment requires recheck: no flag

Review note: Four small first-index forms are p/1/0-like, without secure evidence of a separately cancelled zero and replacement one; uncertainty is kept at each occurrence.

### C-011-U010 (C line 21)

Mechanical state: **unsure token(s) overlap changed alignment; inspect**. Final aligned line: 21.

Source C token:

```tex
\unsure{cas|en}
```

Source C context:

```tex
cases
\[
\begin{aligned}
\bigl[\quad&\text{cas }n=0:\quad\text{une seule comp. }\mathcal L\\
&\text{\unsure{cas|en} }n=1:\quad\deleted{\text{\unsure{une}}}\ \text{deux composantes}\quad L_{<s},\ L_{>s}\\
&\hspace{7e
```

Aligned final span:

```tex
\unsure{en|cas}
```

Final context (up to 100 characters either side):

```tex
cases
\[
\begin{aligned}
\bigl[\quad&\text{cas }n=0:\quad\text{une seule comp. }\mathcal L\\
&\text{\unsure{en|cas} }n=1:\quad\deleted{\text{\unsure{une}}}\ \text{deux composantes}\quad \mathcal L_{<s},\ \mathcal L_
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/011_cases.jpg

Alignment requires recheck: no flag

Review note: Short case label, cancelled une and compressed la/le/ce suite/suit remain unresolved.

### C-011-U011 (C line 21)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 21.

Source C token:

```tex
\unsure{une}
```

Source C context:

```tex
t{cas }n=0:\quad\text{une seule comp. }\mathcal L\\
&\text{\unsure{cas|en} }n=1:\quad\deleted{\text{\unsure{une}}}\ \text{deux composantes}\quad L_{<s},\ L_{>s}\\
&\hspace{7em}\text{(celles qui sont non vides)}\\
```

Aligned final span:

```tex
\unsure{une}
```

Final context (up to 100 characters either side):

```tex
t{cas }n=0:\quad\text{une seule comp. }\mathcal L\\
&\text{\unsure{en|cas} }n=1:\quad\deleted{\text{\unsure{une}}}\ \text{deux composantes}\quad \mathcal L_{<s},\ \mathcal L_{>s}\\
&\hspace{7em}\text{(celles qui 
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/011_cases.jpg

Alignment requires recheck: no flag

Review note: Short case label, cancelled une and compressed la/le/ce suite/suit remain unresolved.

### C-011-U012 (C line 23)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 23.

Source C token:

```tex
\unsure{la|le|ce}
```

Source C context:

```tex
<s},\ L_{>s}\\
&\hspace{7em}\text{(celles qui sont non vides)}\\
&\text{cas }n\geq2:\quad\text{voir \unsure{la|le|ce} \unsure{suite|suit} plus haut}\quad\bigr]
\end{aligned}
\]
% ink below cases, two extreme component
```

Aligned final span:

```tex
\unsure{la|le|ce}
```

Final context (up to 100 characters either side):

```tex
thcal L_{>s}\\
&\hspace{7em}\text{(celles qui sont non vides)}\\
&\text{cas }n\geq2:\quad\text{voir \unsure{la|le|ce} \unsure{suite|suit} plus haut}\quad\bigr]
\end{aligned}
\]
% ink below cases, two extreme component
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/011_cases.jpg

Alignment requires recheck: no flag

Review note: Short case label, cancelled une and compressed la/le/ce suite/suit remain unresolved.

### C-011-U013 (C line 23)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 23.

Source C token:

```tex
\unsure{suite|suit}
```

Source C context:

```tex
space{7em}\text{(celles qui sont non vides)}\\
&\text{cas }n\geq2:\quad\text{voir \unsure{la|le|ce} \unsure{suite|suit} plus haut}\quad\bigr]
\end{aligned}
\]
% ink below cases, two extreme components
les seules non vid
```

Aligned final span:

```tex
\unsure{suite|suit}
```

Final context (up to 100 characters either side):

```tex
space{7em}\text{(celles qui sont non vides)}\\
&\text{cas }n\geq2:\quad\text{voir \unsure{la|le|ce} \unsure{suite|suit} plus haut}\quad\bigr]
\end{aligned}
\]
% ink below cases, two extreme components
les seules non vid
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/011_cases.jpg

Alignment requires recheck: no flag

Review note: Short case label, cancelled une and compressed la/le/ce suite/suit remain unresolved.

### C-011-U014 (C line 27)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 27.

Source C token:

```tex
\unsure{éventuelles}
```

Source C context:

```tex
us haut}\quad\bigr]
\end{aligned}
\]
% ink below cases, two extreme components
les seules non vides \unsure{éventuelles} étant $L_{<s_1}$ (\inserted{si} $s_1$ plus petit élément) et $L_{>s_n}$ (\inserted{si} $s_n$ \unsur
```

Aligned final span:

```tex
éventuelles
```

Final context (up to 100 characters either side):

```tex
us haut}\quad\bigr]
\end{aligned}
\]
% ink below cases, two extreme components
les seules non vides éventuelles étant $\mathcal L_{<s_1}$ (\inserted{si} $s_1$ plus petit élément) et $\mathcal L_{>s_n}$ (\inserte
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/011_extremes.jpg

Alignment requires recheck: no flag

Review note: Éventuelles and plus grd are visible; no expansion or correction of the surprising non vides clause.

### C-011-U015 (C line 27)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 27.

Source C token:

```tex
\unsure{plus grd}
```

Source C context:

```tex
elles} étant $L_{<s_1}$ (\inserted{si} $s_1$ plus petit élément) et $L_{>s_n}$ (\inserted{si} $s_n$ \unsure{plus grd} élément). Les bords \deleted{sont} respectivement
% ink lower third, bords
\[
\underset{\substack{\
```

Aligned final span:

```tex
plus grd
```

Final context (up to 100 characters either side):

```tex
hcal L_{<s_1}$ (\inserted{si} $s_1$ plus petit élément) et $\mathcal L_{>s_n}$ (\inserted{si} $s_n$ plus grd élément). Les bords \deleted{sont} respectivement
% ink lower third, bords
\[
\underset{\substack{\
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/011_extremes.jpg

Alignment requires recheck: no flag

Review note: Éventuelles and plus grd are visible; no expansion or correction of the surprising non vides clause.

### C-011-U016 (C line 30)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 30.

Source C token:

```tex
\unsure{s_1}
```

Source C context:

```tex
4pt}{.6ex}\rule{4.8em}{.4pt}\rule{.4pt}{.6ex}\\\text{si comp. existe}}}{\{s_1\}\ \substack{\deleted{\unsure{s_1}}\\\deleted{\unsure{\text{donc }\varnothing}}\\\deleted{\unsure{\varnothing}}}},
\quad\{s_1,s_2\},\q
```

Aligned final span:

```tex
\unsure{s_1}
```

Final context (up to 100 characters either side):

```tex
4pt}{.6ex}\rule{4.8em}{.4pt}\rule{.4pt}{.6ex}\\\text{si comp. existe}}}{\{s_1\}\ \substack{\deleted{\unsure{s_1}}\\\deleted{\unsure{\text{donc }\varnothing}}\\\deleted{\unsure{\varnothing}}}},
\quad\{s_1,s_2\},\q
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/011_borders.jpg

Alignment requires recheck: no flag

Review note: Three crossed fragments around the first boundary label remain partly hidden by scribbling.

### C-011-U017 (C line 30)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 30.

Source C token:

```tex
\unsure{\text{donc }\varnothing}
```

Source C context:

```tex
4pt}\rule{.4pt}{.6ex}\\\text{si comp. existe}}}{\{s_1\}\ \substack{\deleted{\unsure{s_1}}\\\deleted{\unsure{\text{donc }\varnothing}}\\\deleted{\unsure{\varnothing}}}},
\quad\{s_1,s_2\},\quad\ldots,\quad\{s_{n-1},s_n\},\quad
\unders
```

Aligned final span:

```tex
\unsure{\text{donc }\varnothing}
```

Final context (up to 100 characters either side):

```tex
4pt}\rule{.4pt}{.6ex}\\\text{si comp. existe}}}{\{s_1\}\ \substack{\deleted{\unsure{s_1}}\\\deleted{\unsure{\text{donc }\varnothing}}\\\deleted{\unsure{\varnothing}}}},
\quad\{s_1,s_2\},\quad\ldots,\quad\{s_{n-1},s_n\},\quad
\unders
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/011_borders.jpg

Alignment requires recheck: no flag

Review note: Three crossed fragments around the first boundary label remain partly hidden by scribbling.

### C-011-U018 (C line 30)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 30.

Source C token:

```tex
\unsure{\varnothing}
```

Source C context:

```tex
}}}{\{s_1\}\ \substack{\deleted{\unsure{s_1}}\\\deleted{\unsure{\text{donc }\varnothing}}\\\deleted{\unsure{\varnothing}}}},
\quad\{s_1,s_2\},\quad\ldots,\quad\{s_{n-1},s_n\},\quad
\underset{\substack{\rule{.4pt}{.6ex}\r
```

Aligned final span:

```tex
\unsure{\varnothing}
```

Final context (up to 100 characters either side):

```tex
}}}{\{s_1\}\ \substack{\deleted{\unsure{s_1}}\\\deleted{\unsure{\text{donc }\varnothing}}\\\deleted{\unsure{\varnothing}}}},
\quad\{s_1,s_2\},\quad\ldots,\quad\{s_{n-1},s_n\},\quad
\underset{\substack{\rule{.4pt}{.6ex}\r
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/011_borders.jpg

Alignment requires recheck: no flag

Review note: Three crossed fragments around the first boundary label remain partly hidden by scribbling.

### C-011-U019 (C line 36)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 36.

Source C token:

```tex
\unsure{dé|de}
```

Source C context:

```tex
}\\\text{si comp. existe}}}{\{s_n\}}
\]

% ink bottom, Je dis
Je dis que l'on récupère la structure \unsure{dé|de} \deleted{\unsure{ordr|ordre}} biordre du tronçon (donc aussi \unsure{les structures|la structure} \
```

Aligned final span:

```tex
dé
```

Final context (up to 100 characters either side):

```tex
}\\\text{si comp. existe}}}{\{s_n\}}
\]

% ink bottom, Je dis
Je dis que l'on récupère la structure dé \deleted{\unsure{ordr|ordre}} biordre du tronçon (donc aussi la structure \textcircled{a}. \textcir
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/011_bottom.jpg

Alignment requires recheck: no flag

Review note: Accent over dé, singular la structure and the point after circled a are visibly present.

### C-011-U020 (C line 36)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 36.

Source C token:

```tex
\unsure{ordr|ordre}
```

Source C context:

```tex
}}}{\{s_n\}}
\]

% ink bottom, Je dis
Je dis que l'on récupère la structure \unsure{dé|de} \deleted{\unsure{ordr|ordre}} biordre du tronçon (donc aussi \unsure{les structures|la structure} \textcircled{a}\unsure{.} \tex
```

Aligned final span:

```tex
\unsure{ordr|ordre}
```

Final context (up to 100 characters either side):

```tex
comp. existe}}}{\{s_n\}}
\]

% ink bottom, Je dis
Je dis que l'on récupère la structure dé \deleted{\unsure{ordr|ordre}} biordre du tronçon (donc aussi la structure \textcircled{a}. \textcircled{b} \textcircled{c}) en t
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/011_bottom.jpg

Alignment requires recheck: no flag

Review note: Cancelled ordre ending and final S alphabet are not securely distinguishable.

### C-011-U021 (C line 36)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 36.

Source C token:

```tex
\unsure{les structures|la structure}
```

Source C context:

```tex
n récupère la structure \unsure{dé|de} \deleted{\unsure{ordr|ordre}} biordre du tronçon (donc aussi \unsure{les structures|la structure} \textcircled{a}\unsure{.} \textcircled{b} \textcircled{c}) en termes de la seule structure \textcir
```

Aligned final span:

```tex
la structure
```

Final context (up to 100 characters either side):

```tex
 dis que l'on récupère la structure dé \deleted{\unsure{ordr|ordre}} biordre du tronçon (donc aussi la structure \textcircled{a}. \textcircled{b} \textcircled{c}) en termes de la seule structure \textcircled{a}, 
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/011_bottom.jpg

Alignment requires recheck: no flag

Review note: Accent over dé, singular la structure and the point after circled a are visibly present.

### C-011-U022 (C line 36)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 36.

Source C token:

```tex
\unsure{.}
```

Source C context:

```tex
ure{ordr|ordre}} biordre du tronçon (donc aussi \unsure{les structures|la structure} \textcircled{a}\unsure{.} \textcircled{b} \textcircled{c}) en termes de la seule structure \textcircled{a}, $+$ \textcircled{
```

Aligned final span:

```tex
.
```

Final context (up to 100 characters either side):

```tex
ructure dé \deleted{\unsure{ordr|ordre}} biordre du tronçon (donc aussi la structure \textcircled{a}. \textcircled{b} \textcircled{c}) en termes de la seule structure \textcircled{a}, $+$ \textcircled{
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/011_bottom.jpg

Alignment requires recheck: no flag

Review note: Accent over dé, singular la structure and the point after circled a are visibly present.

### C-011-U023 (C line 36)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 36.

Source C token:

```tex
\unsure{\mathscr S|S}
```

Source C context:

```tex
{b} \textcircled{c}) en termes de la seule structure \textcircled{a}, $+$ \textcircled{b} pour $T\in\unsure{\mathscr S|S}_0$.

```

Aligned final span:

```tex
\unsure{\mathscr S|S}
```

Final context (up to 100 characters either side):

```tex
{b} \textcircled{c}) en termes de la seule structure \textcircled{a}, $+$ \textcircled{b} pour $T\in\unsure{\mathscr S|S}_0$.

% pale watermark seen through the paper
\rotatebox{90}{\textsc{\unsure{ng Extra Stro}}}

```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/011_bottom.jpg

Alignment requires recheck: no flag

Review note: Cancelled ordre ending and final S alphabet are not securely distinguishable.

### C-012-U001 (C line 3)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 3.

Source C token:

```tex
\unsure{qu'une str}
```

Source C context:

```tex
\scanpage{12}\mspage{11}
% ink opening line
Pour ceci, on note \deleted{\unsure{qu'une str}}\inserted{d'abord}

% ink Lemme, first four lines
\uline{Lemme} Une structure de \deleted{biordre} 
```

Aligned final span:

```tex
\unsure{qu'une str}
```

Final context (up to 100 characters either side):

```tex
\scanpage{12}\mspage{11}
% ink opening line
Pour ceci, on note \deleted{\unsure{qu'une str}}\inserted{d'abord}

% ink Lemme, first four lines
\uline{Lemme} Une structure de \deleted{biordre} 
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/012_top.jpg

Alignment requires recheck: no flag

Review note: Crossed opening fragment and abbreviated/plural element ending remain uncertain.

### C-012-U002 (C line 6)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 6.

Source C token:

```tex
\unsure{biordonnien|biordonnier}
```

Source C context:

```tex
ed{d'abord}

% ink Lemme, first four lines
\uline{Lemme} Une structure de \deleted{biordre} tronçon \unsure{biordonnien|biordonnier} est connue quand on connaît la relation en \deleted{$\{a,b,c\}$} trois \unsure{élémt|éléments} $a,b
```

Aligned final span:

```tex
biordonnien
```

Final context (up to 100 characters either side):

```tex
ed{d'abord}

% ink Lemme, first four lines
\uline{Lemme} Une structure de \deleted{biordre} tronçon biordonnien est connue quand on connaît la relation en \deleted{$\{a,b,c\}$} trois \unsure{élémt|éléments} $a,b
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/012_top.jpg

Alignment requires recheck: no flag

Review note: Final n of biordonnien is visible; not r.

### C-012-U003 (C line 6)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 6.

Source C token:

```tex
\unsure{élémt|éléments}
```

Source C context:

```tex
ure{biordonnien|biordonnier} est connue quand on connaît la relation en \deleted{$\{a,b,c\}$} trois \unsure{élémt|éléments} $a,b,c$
% ink relation R, first display
\[
\begin{aligned}
\left.\vphantom{\substack{X\\X}}\right|\
```

Aligned final span:

```tex
\unsure{élémt|éléments}
```

Final context (up to 100 characters either side):

```tex
biordre} tronçon biordonnien est connue quand on connaît la relation en \deleted{$\{a,b,c\}$} trois \unsure{élémt|éléments} $a,b,c$
% ink relation R, first display
\[
\begin{aligned}
\left.\vphantom{\substack{X\\X}}\right|\
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/012_top.jpg

Alignment requires recheck: no flag

Review note: Crossed opening fragment and abbreviated/plural element ending remain uncertain.

### C-012-U004 (C line 15)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 15.

Source C token:

```tex
\unsure{e}
```

Source C context:

```tex
tement entre}}\\
&\qquad\qquad\text{\uline{$a$ et $c$}}
\end{aligned}
\]
(au sens que $a<b<\deleted{\unsure{e}}c$ \uline{ou} $a>b>c$)
% ink left, short diagonal note beside the three strokes
% slanted
\margin{r
```

Aligned final span:

```tex
\unsure{e}
```

Final context (up to 100 characters either side):

```tex
tement entre}}\\
&\qquad\qquad\text{\uline{$a$ et $c$}}
\end{aligned}
\]
(au sens que $a<b<\deleted{\unsure{e}}c$ \uline{ou} $a>b>c$)
% ink left, short diagonal note beside the three strokes
% slanted
\margin{r
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/012_relation.jpg

Alignment requires recheck: no flag

Review note: Old letter below the corrected c remains obscured.

### C-012-U005 (C line 21)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 21.

Source C token:

```tex
\unsure{On a de}
```

Source C context:

```tex
margin{relation sym. en $a,c$}
% ink left, NB, diagonal block
% slanted
\margin{\uline{NB} \deleted{\unsure{On a de}}\inserted{La \unsure{conn.} de} \unsure{Cette|cette} relation $R$ implique la relation $\bar R$ non
```

Aligned final span:

```tex
\unsure{On a de}
```

Final context (up to 100 characters either side):

```tex
margin{relation sym. en $a,c$}
% ink left, NB, diagonal block
% slanted
\margin{\uline{NB} \deleted{\unsure{On a de}}\inserted{La conn. de} Cette relation $R$ implique la relation $\bar R$ non stricte \deleted{\unsur
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/012_margin.jpg

Alignment requires recheck: no flag

Review note: Crossed starts and inequalities retain their local uncertainty under multiple strikes.

### C-012-U006 (C line 21)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 21.

Source C token:

```tex
\unsure{conn.}
```

Source C context:

```tex

% ink left, NB, diagonal block
% slanted
\margin{\uline{NB} \deleted{\unsure{On a de}}\inserted{La \unsure{conn.} de} \unsure{Cette|cette} relation $R$ implique la relation $\bar R$ non stricte \deleted{\unsure{($
```

Aligned final span:

```tex
conn.
```

Final context (up to 100 characters either side):

```tex

% ink left, NB, diagonal block
% slanted
\margin{\uline{NB} \deleted{\unsure{On a de}}\inserted{La conn. de} Cette relation $R$ implique la relation $\bar R$ non stricte \deleted{\unsure{($a=b=c$} \unsure
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/012_margin.jpg

Alignment requires recheck: no flag

Review note: Inserted conn. and initial capital C of Cette are legible.

### C-012-U007 (C line 21)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 21.

Source C token:

```tex
\unsure{Cette|cette}
```

Source C context:

```tex
agonal block
% slanted
\margin{\uline{NB} \deleted{\unsure{On a de}}\inserted{La \unsure{conn.} de} \unsure{Cette|cette} relation $R$ implique la relation $\bar R$ non stricte \deleted{\unsure{($a=b=c$} \unsure{ou}}\ \de
```

Aligned final span:

```tex
Cette
```

Final context (up to 100 characters either side):

```tex
t, NB, diagonal block
% slanted
\margin{\uline{NB} \deleted{\unsure{On a de}}\inserted{La conn. de} Cette relation $R$ implique la relation $\bar R$ non stricte \deleted{\unsure{($a=b=c$} \unsure{ou}}\ \de
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/012_margin.jpg

Alignment requires recheck: no flag

Review note: Inserted conn. and initial capital C of Cette are legible.

### C-012-U008 (C line 21)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 21.

Source C token:

```tex
\unsure{($a=b=c$}
```

Source C context:

```tex
ure{conn.} de} \unsure{Cette|cette} relation $R$ implique la relation $\bar R$ non stricte \deleted{\unsure{($a=b=c$} \unsure{ou}}\ \deleted{$\unsure{a=b<c}$}\ $a\leq b\leq c$ ou $a\geq b\geq c$ \deleted{$\unsure{a\le
```

Aligned final span:

```tex
\unsure{($a=b=c$}
```

Final context (up to 100 characters either side):

```tex
 a de}}\inserted{La conn. de} Cette relation $R$ implique la relation $\bar R$ non stricte \deleted{\unsure{($a=b=c$} \unsure{ou}}\ \deleted{$\unsure{a=b<c}$}\ $a\leq b\leq c$ ou $a\geq b\geq c$ \deleted{$\unsure{a\le
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/012_margin.jpg

Alignment requires recheck: no flag

Review note: Crossed starts and inequalities retain their local uncertainty under multiple strikes.

### C-012-U009 (C line 21)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 21.

Source C token:

```tex
\unsure{ou}
```

Source C context:

```tex
sure{Cette|cette} relation $R$ implique la relation $\bar R$ non stricte \deleted{\unsure{($a=b=c$} \unsure{ou}}\ \deleted{$\unsure{a=b<c}$}\ $a\leq b\leq c$ ou $a\geq b\geq c$ \deleted{$\unsure{a\leq b\leq c}$}
```

Aligned final span:

```tex
\unsure{ou}
```

Final context (up to 100 characters either side):

```tex
a conn. de} Cette relation $R$ implique la relation $\bar R$ non stricte \deleted{\unsure{($a=b=c$} \unsure{ou}}\ \deleted{$\unsure{a=b<c}$}\ $a\leq b\leq c$ ou $a\geq b\geq c$ \deleted{$\unsure{a\leq b\leq c}$}
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/012_margin.jpg

Alignment requires recheck: no flag

Review note: Crossed starts and inequalities retain their local uncertainty under multiple strikes.

### C-012-U010 (C line 21)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 21.

Source C token:

```tex
\unsure{a=b<c}
```

Source C context:

```tex
on $R$ implique la relation $\bar R$ non stricte \deleted{\unsure{($a=b=c$} \unsure{ou}}\ \deleted{$\unsure{a=b<c}$}\ $a\leq b\leq c$ ou $a\geq b\geq c$ \deleted{$\unsure{a\leq b\leq c}$} \deleted{$(\unsure{\Leftri
```

Aligned final span:

```tex
\unsure{a=b<c}
```

Final context (up to 100 characters either side):

```tex
on $R$ implique la relation $\bar R$ non stricte \deleted{\unsure{($a=b=c$} \unsure{ou}}\ \deleted{$\unsure{a=b<c}$}\ $a\leq b\leq c$ ou $a\geq b\geq c$ \deleted{$\unsure{a\leq b\leq c}$} $(\unsure{\rightleftarrows
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/012_margin.jpg

Alignment requires recheck: no flag

Review note: Crossed starts and inequalities retain their local uncertainty under multiple strikes.

### C-012-U011 (C line 21)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 21.

Source C token:

```tex
\unsure{a\leq b\leq c}
```

Source C context:

```tex
re{($a=b=c$} \unsure{ou}}\ \deleted{$\unsure{a=b<c}$}\ $a\leq b\leq c$ ou $a\geq b\geq c$ \deleted{$\unsure{a\leq b\leq c}$} \deleted{$(\unsure{\Leftrightarrow})$} \deleted{$\{a,b,c\}$} $b$ entre $a$ et $c$ \inserted{\ulin
```

Aligned final span:

```tex
\unsure{a\leq b\leq c}
```

Final context (up to 100 characters either side):

```tex
re{($a=b=c$} \unsure{ou}}\ \deleted{$\unsure{a=b<c}$}\ $a\leq b\leq c$ ou $a\geq b\geq c$ \deleted{$\unsure{a\leq b\leq c}$} $(\unsure{\rightleftarrows|\Leftrightarrow})$ \deleted{$\{a,b,c\}$} $b$ entre $a$ et $c$ \inserte
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/012_margin.jpg

Alignment requires recheck: no flag

Review note: Crossed starts and inequalities retain their local uncertainty under multiple strikes.

### C-012-U012 (C line 21)

Mechanical state: **unsure token(s) overlap changed alignment; inspect**. Final aligned line: 21.

Source C token:

```tex
\unsure{\Leftrightarrow}
```

Source C context:

```tex
$\unsure{a=b<c}$}\ $a\leq b\leq c$ ou $a\geq b\geq c$ \deleted{$\unsure{a\leq b\leq c}$} \deleted{$(\unsure{\Leftrightarrow})$} \deleted{$\{a,b,c\}$} $b$ entre $a$ et $c$ \inserted{\uline{strict}} ou $\{a,b,c\}$ est un drape
```

Aligned final span:

```tex
\unsure{\rightleftarrows|\Leftrightarrow}
```

Final context (up to 100 characters either side):

```tex
\deleted{$\unsure{a=b<c}$}\ $a\leq b\leq c$ ou $a\geq b\geq c$ \deleted{$\unsure{a\leq b\leq c}$} $(\unsure{\rightleftarrows|\Leftrightarrow})$ \deleted{$\{a,b,c\}$} $b$ entre $a$ et $c$ \inserted{\uline{strict}} ou $\{a,b,c\}$ est un drapea
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: revised

Crop links: crops/012_margin_arrow.jpg

Alignment requires recheck: no flag

Review note: Opposed horizontal arrows are live; two separate arrows are more likely, but double-arrow form cannot be excluded.

### C-012-U013 (C line 24)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 24.

Source C token:

```tex
\unsure{Dém|Dém.}
```

Source C context:

```tex
ict}} ou $\{a,b,c\}$ est un drapeau de cardinal $\leq 2$}

% ink middle, Dém and équivalence
\uline{\unsure{Dém|Dém.}} \deleted{Choisissons} On en déduit la relation (i.e. \inserted{la \unsure{conn.} de} $\unsure{\mat
```

Aligned final span:

```tex
Dém
```

Final context (up to 100 characters either side):

```tex
ict}} ou $\{a,b,c\}$ est un drapeau de cardinal $\leq 2$}

% ink middle, Dém and équivalence
\uline{Dém} \deleted{Choisissons} On en déduit la relation (i.e. \inserted{la conn. de} $S_0(\mathcal L)$\dele
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/012_proof.jpg

Alignment requires recheck: no flag

Review note: Dém has no separate point, conn. is readable and S is the plain recurring form.

### C-012-U014 (C line 24)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 24.

Source C token:

```tex
\unsure{conn.}
```

Source C context:

```tex
valence
\uline{\unsure{Dém|Dém.}} \deleted{Choisissons} On en déduit la relation (i.e. \inserted{la \unsure{conn.} de} $\unsure{\mathscr S|S}_0(L)$\deleted{\unsure{)}} i.e. de $\mathrm{Drap}(L)$)
\[
\begin{aligned}
```

Aligned final span:

```tex
conn.
```

Final context (up to 100 characters either side):

```tex
, Dém and équivalence
\uline{Dém} \deleted{Choisissons} On en déduit la relation (i.e. \inserted{la conn. de} $S_0(\mathcal L)$\deleted{\unsure{)}} i.e. de $\mathrm{Drap}(\mathcal L)$)
\[
\begin{aligned}
\
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/012_proof.jpg

Alignment requires recheck: no flag

Review note: Dém has no separate point, conn. is readable and S is the plain recurring form.

### C-012-U015 (C line 24)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 24.

Source C token:

```tex
\unsure{\mathscr S|S}
```

Source C context:

```tex
re{Dém|Dém.}} \deleted{Choisissons} On en déduit la relation (i.e. \inserted{la \unsure{conn.} de} $\unsure{\mathscr S|S}_0(L)$\deleted{\unsure{)}} i.e. de $\mathrm{Drap}(L)$)
\[
\begin{aligned}
\deleted{\unsure{a}}\,a\te
```

Aligned final span:

```tex
S_0(\mathcal 
```

Final context (up to 100 characters either side):

```tex
quivalence
\uline{Dém} \deleted{Choisissons} On en déduit la relation (i.e. \inserted{la conn. de} $S_0(\mathcal L)$\deleted{\unsure{)}} i.e. de $\mathrm{Drap}(\mathcal L)$)
\[
\begin{aligned}
\deleted{\unsure{a}}
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/012_proof.jpg

Alignment requires recheck: no flag

Review note: Dém has no separate point, conn. is readable and S is the plain recurring form.

### C-012-U016 (C line 24)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 24.

Source C token:

```tex
\unsure{)}
```

Source C context:

```tex
On en déduit la relation (i.e. \inserted{la \unsure{conn.} de} $\unsure{\mathscr S|S}_0(L)$\deleted{\unsure{)}} i.e. de $\mathrm{Drap}(L)$)
\[
\begin{aligned}
\deleted{\unsure{a}}\,a\text{ et }b\ \text{``disjoi
```

Aligned final span:

```tex
\unsure{)}
```

Final context (up to 100 characters either side):

```tex
eleted{Choisissons} On en déduit la relation (i.e. \inserted{la conn. de} $S_0(\mathcal L)$\deleted{\unsure{)}} i.e. de $\mathrm{Drap}(\mathcal L)$)
\[
\begin{aligned}
\deleted{\unsure{a}}\,a\text{ et }b\ \text
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/012_proof.jpg

Alignment requires recheck: no flag

Review note: Cancelled closing mark and overwritten initial a remain uncertain.

### C-012-U017 (C line 27)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 27.

Source C token:

```tex
\unsure{a}
```

Source C context:

```tex
ure{\mathscr S|S}_0(L)$\deleted{\unsure{)}} i.e. de $\mathrm{Drap}(L)$)
\[
\begin{aligned}
\deleted{\unsure{a}}\,a\text{ et }b\ \text{``disjoints''}\quad&
\text{i.e. distincts et comparables}\\
&\text{(i.e. }\{
```

Aligned final span:

```tex
\unsure{a}
```

Final context (up to 100 characters either side):

```tex
0(\mathcal L)$\deleted{\unsure{)}} i.e. de $\mathrm{Drap}(\mathcal L)$)
\[
\begin{aligned}
\deleted{\unsure{a}}\,a\text{ et }b\ \text{``disjoints''}\quad&
\text{i.e. distincts et comparables}\\
&\text{(i.e. }\{
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/012_proof.jpg

Alignment requires recheck: no flag

Review note: Cancelled closing mark and overwritten initial a remain uncertain.

### C-012-U018 (C line 34)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 34.

Source C token:

```tex
\unsure{par|puis|pour}
```

Source C context:

```tex
b\}\in\mathrm{Drap}_2(L)\\
&\text{pour le biordre}
\end{aligned}
\]
% ink lower middle, formule ssi
\unsure{par|puis|pour} 
\[
\begin{aligned}
a\text{ et }b\ \text{\unsure{disjts}}\quad \text{ssi}\quad
\exists\,c\ \text{te
```

Aligned final span:

```tex
par
```

Final context (up to 100 characters either side):

```tex
thrm{Drap}_2(\mathcal L)\\
&\text{pour le biordre}
\end{aligned}
\]
% ink lower middle, formule ssi
par 
\[
\begin{aligned}
a\text{ et }b\ \text{disjts}\quad \text{ssi}\quad
\exists\,c\ \text{tel que }c\
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/012_ssi.jpg

Alignment requires recheck: no flag

Review note: Par, disjts and divisibilité with exclamation mark are readable; abbreviated word is not expanded.

### C-012-U019 (C line 37)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 37.

Source C token:

```tex
\unsure{disjts}
```

Source C context:

```tex

\]
% ink lower middle, formule ssi
\unsure{par|puis|pour} 
\[
\begin{aligned}
a\text{ et }b\ \text{\unsure{disjts}}\quad \text{ssi}\quad
\exists\,c\ \text{tel que }c\text{ entre}\\
a\text{ et }b
\end{aligned}
\]
(u
```

Aligned final span:

```tex
disjts
```

Final context (up to 100 characters either side):

```tex
rdre}
\end{aligned}
\]
% ink lower middle, formule ssi
par 
\[
\begin{aligned}
a\text{ et }b\ \text{disjts}\quad \text{ssi}\quad
\exists\,c\ \text{tel que }c\text{ entre}\\
a\text{ et }b
\end{aligned}
\]
(u
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/012_ssi.jpg

Alignment requires recheck: no flag

Review note: Par, disjts and divisibilité with exclamation mark are readable; abbreviated word is not expanded.

### C-012-U020 (C line 42)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 42.

Source C token:

```tex
\unsure{divisibilité !}
```

Source C context:

```tex
\text{ssi}\quad
\exists\,c\ \text{tel que }c\text{ entre}\\
a\text{ et }b
\end{aligned}
\]
(utilise \unsure{divisibilité !} d\deleted{\unsure{es}}\unsure{u} \deleted{\unsure{drap. le ré}} biordre)

% ink bottom, Choisissons
```

Aligned final span:

```tex
divisibilité !
```

Final context (up to 100 characters either side):

```tex
\text{ssi}\quad
\exists\,c\ \text{tel que }c\text{ entre}\\
a\text{ et }b
\end{aligned}
\]
(utilise divisibilité ! d\deleted{\unsure{es}}\unsure{u} \deleted{\unsure{drap. le ré}} biordre)

% ink bottom, Choisissons
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/012_ssi.jpg

Alignment requires recheck: no flag

Review note: Par, disjts and divisibilité with exclamation mark are readable; abbreviated word is not expanded.

### C-012-U021 (C line 42)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 42.

Source C token:

```tex
\unsure{es}
```

Source C context:

```tex
tel que }c\text{ entre}\\
a\text{ et }b
\end{aligned}
\]
(utilise \unsure{divisibilité !} d\deleted{\unsure{es}}\unsure{u} \deleted{\unsure{drap. le ré}} biordre)

% ink bottom, Choisissons
\deleted{\illegible{1
```

Aligned final span:

```tex
\unsure{es}
```

Final context (up to 100 characters either side):

```tex
c\ \text{tel que }c\text{ entre}\\
a\text{ et }b
\end{aligned}
\]
(utilise divisibilité ! d\deleted{\unsure{es}}\unsure{u} \deleted{\unsure{drap. le ré}} biordre)

% ink bottom, Choisissons
\deleted{\illegible{1
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/012_ssi.jpg

Alignment requires recheck: no flag

Review note: Overwritten de/du and crossed phrase remain too crowded to resolve.

### C-012-U022 (C line 42)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 42.

Source C token:

```tex
\unsure{u}
```

Source C context:

```tex
ext{ entre}\\
a\text{ et }b
\end{aligned}
\]
(utilise \unsure{divisibilité !} d\deleted{\unsure{es}}\unsure{u} \deleted{\unsure{drap. le ré}} biordre)

% ink bottom, Choisissons
\deleted{\illegible{1}} Choisiss
```

Aligned final span:

```tex
\unsure{u}
```

Final context (up to 100 characters either side):

```tex
 que }c\text{ entre}\\
a\text{ et }b
\end{aligned}
\]
(utilise divisibilité ! d\deleted{\unsure{es}}\unsure{u} \deleted{\unsure{drap. le ré}} biordre)

% ink bottom, Choisissons
\deleted{\illegible{1}} Choisiss
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/012_ssi.jpg

Alignment requires recheck: no flag

Review note: Overwritten de/du and crossed phrase remain too crowded to resolve.

### C-012-U023 (C line 42)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 42.

Source C token:

```tex
\unsure{drap. le ré}
```

Source C context:

```tex
{ et }b
\end{aligned}
\]
(utilise \unsure{divisibilité !} d\deleted{\unsure{es}}\unsure{u} \deleted{\unsure{drap. le ré}} biordre)

% ink bottom, Choisissons
\deleted{\illegible{1}} Choisissons $\unsure{E|\mathcal E}\in\
```

Aligned final span:

```tex
\unsure{drap. le ré}
```

Final context (up to 100 characters either side):

```tex
\\
a\text{ et }b
\end{aligned}
\]
(utilise divisibilité ! d\deleted{\unsure{es}}\unsure{u} \deleted{\unsure{drap. le ré}} biordre)

% ink bottom, Choisissons
\deleted{\illegible{1}} Choisissons $\unsure{\varepsilon|\math
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/012_ssi.jpg

Alignment requires recheck: no flag

Review note: Overwritten de/du and crossed phrase remain too crowded to resolve.

### C-012-U024 (C line 45)

Mechanical state: **unsure token(s) overlap changed alignment; inspect**. Final aligned line: 45.

Source C token:

```tex
\unsure{E|\mathcal E}
```

Source C context:

```tex
eted{\unsure{drap. le ré}} biordre)

% ink bottom, Choisissons
\deleted{\illegible{1}} Choisissons $\unsure{E|\mathcal E}\in\mathscr S_0$ (existe, car \deleted{si $x,y\in$} par \unsure{hyp} $\exists\,x,y\in L,\quad x\ne y
```

Aligned final span:

```tex
\unsure{\varepsilon|\mathcal E|E}
```

Final context (up to 100 characters either side):

```tex
eted{\unsure{drap. le ré}} biordre)

% ink bottom, Choisissons
\deleted{\illegible{1}} Choisissons $\unsure{\varepsilon|\mathcal E|E}\in S_0$ (existe, car \deleted{si $x,y\in$} par hyp $\exists\,x,y\in\mathcal L,\quad x\ne y$, donc $
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: revised

Crop links: crops/012_bottom.jpg

Alignment requires recheck: no flag

Review note: Rounded epsilon/E form is shared with neighbouring pages; preserve all locally supported alphabet alternatives.

### C-012-U025 (C line 45)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 45.

Source C token:

```tex
\unsure{hyp}
```

Source C context:

```tex
gible{1}} Choisissons $\unsure{E|\mathcal E}\in\mathscr S_0$ (existe, car \deleted{si $x,y\in$} par \unsure{hyp} $\exists\,x,y\in L,\quad x\ne y$, donc $a\leq x,y\leq b$, et on a $a\leq b$ et $a\ne b$ \deleted{\u
```

Aligned final span:

```tex
hyp
```

Final context (up to 100 characters either side):

```tex
e{1}} Choisissons $\unsure{\varepsilon|\mathcal E|E}\in S_0$ (existe, car \deleted{si $x,y\in$} par hyp $\exists\,x,y\in\mathcal L,\quad x\ne y$, donc $a\leq x,y\leq b$, et on a $a\leq b$ et $a\ne b$ \de
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/012_bottom.jpg

Alignment requires recheck: no flag

Review note: Hyp without point, car and aurait are visible.

### C-012-U026 (C line 45)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 45.

Source C token:

```tex
\unsure{)}
```

Source C context:

```tex
p} $\exists\,x,y\in L,\quad x\ne y$, donc $a\leq x,y\leq b$, et on a $a\leq b$ et $a\ne b$ \deleted{\unsure{)}} \deleted{\unsure{c|p}}\unsure{car} sinon on \unsure{aurait} $x=y$)
% ink lower left, four short ob
```

Aligned final span:

```tex
\unsure{)}
```

Final context (up to 100 characters either side):

```tex
sts\,x,y\in\mathcal L,\quad x\ne y$, donc $a\leq x,y\leq b$, et on a $a\leq b$ et $a\ne b$ \deleted{\unsure{)}} \deleted{\unsure{c|p}}car sinon on aurait $x=y$)
% ink lower left, four short oblique lines
% slan
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/012_bottom.jpg

Alignment requires recheck: no flag

Review note: Crossed closing parenthesis and short c/p remain uncertain.

### C-012-U027 (C line 45)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 45.

Source C token:

```tex
\unsure{c|p}
```

Source C context:

```tex
,\quad x\ne y$, donc $a\leq x,y\leq b$, et on a $a\leq b$ et $a\ne b$ \deleted{\unsure{)}} \deleted{\unsure{c|p}}\unsure{car} sinon on \unsure{aurait} $x=y$)
% ink lower left, four short oblique lines
% slanted
\
```

Aligned final span:

```tex
\unsure{c|p}
```

Final context (up to 100 characters either side):

```tex
,\quad x\ne y$, donc $a\leq x,y\leq b$, et on a $a\leq b$ et $a\ne b$ \deleted{\unsure{)}} \deleted{\unsure{c|p}}car sinon on aurait $x=y$)
% ink lower left, four short oblique lines
% slanted
\margin{Il existe $
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/012_bottom.jpg

Alignment requires recheck: no flag

Review note: Crossed closing parenthesis and short c/p remain uncertain.

### C-012-U028 (C line 45)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 45.

Source C token:

```tex
\unsure{car}
```

Source C context:

```tex
$, donc $a\leq x,y\leq b$, et on a $a\leq b$ et $a\ne b$ \deleted{\unsure{)}} \deleted{\unsure{c|p}}\unsure{car} sinon on \unsure{aurait} $x=y$)
% ink lower left, four short oblique lines
% slanted
\margin{\unsur
```

Aligned final span:

```tex
car
```

Final context (up to 100 characters either side):

```tex
$, donc $a\leq x,y\leq b$, et on a $a\leq b$ et $a\ne b$ \deleted{\unsure{)}} \deleted{\unsure{c|p}}car sinon on aurait $x=y$)
% ink lower left, four short oblique lines
% slanted
\margin{Il existe $=$ d
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/012_bottom.jpg

Alignment requires recheck: no flag

Review note: Hyp without point, car and aurait are visible.

### C-012-U029 (C line 45)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 45.

Source C token:

```tex
\unsure{aurait}
```

Source C context:

```tex
 b$, et on a $a\leq b$ et $a\ne b$ \deleted{\unsure{)}} \deleted{\unsure{c|p}}\unsure{car} sinon on \unsure{aurait} $x=y$)
% ink lower left, four short oblique lines
% slanted
\margin{\unsure{Il} existe $=$ des \uns
```

Aligned final span:

```tex
aurait
```

Final context (up to 100 characters either side):

```tex
q x,y\leq b$, et on a $a\leq b$ et $a\ne b$ \deleted{\unsure{)}} \deleted{\unsure{c|p}}car sinon on aurait $x=y$)
% ink lower left, four short oblique lines
% slanted
\margin{Il existe $=$ des \unsure{drap.
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/012_bottom.jpg

Alignment requires recheck: no flag

Review note: Hyp without point, car and aurait are visible.

### C-012-U030 (C line 48)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 48.

Source C token:

```tex
\unsure{Il}
```

Source C context:

```tex
e{car} sinon on \unsure{aurait} $x=y$)
% ink lower left, four short oblique lines
% slanted
\margin{\unsure{Il} existe $=$ des \unsure{drap.} de \unsure{long.} arbitraire}

```

Aligned final span:

```tex
Il
```

Final context (up to 100 characters either side):

```tex
unsure{c|p}}car sinon on aurait $x=y$)
% ink lower left, four short oblique lines
% slanted
\margin{Il existe $=$ des \unsure{drap.} de long. arbitraire}

% pale vertical watermark
\rotatebox{90}{\texts
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/012_lowmargin.jpg

Alignment requires recheck: no flag

Review note: Il and long. are legible in the rotated margin.

### C-012-U031 (C line 48)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 48.

Source C token:

```tex
\unsure{drap.}
```

Source C context:

```tex
ait} $x=y$)
% ink lower left, four short oblique lines
% slanted
\margin{\unsure{Il} existe $=$ des \unsure{drap.} de \unsure{long.} arbitraire}

```

Aligned final span:

```tex
\unsure{drap.}
```

Final context (up to 100 characters either side):

```tex
non on aurait $x=y$)
% ink lower left, four short oblique lines
% slanted
\margin{Il existe $=$ des \unsure{drap.} de long. arbitraire}

% pale vertical watermark
\rotatebox{90}{\textsc{\unsure{ra Strong Extra}}}

```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/012_lowmargin.jpg

Alignment requires recheck: no flag

Review note: Abbreviated drap. remains compressed; no expansion in the text.

### C-012-U032 (C line 48)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 48.

Source C token:

```tex
\unsure{long.}
```

Source C context:

```tex
lower left, four short oblique lines
% slanted
\margin{\unsure{Il} existe $=$ des \unsure{drap.} de \unsure{long.} arbitraire}

```

Aligned final span:

```tex
long.
```

Final context (up to 100 characters either side):

```tex
$)
% ink lower left, four short oblique lines
% slanted
\margin{Il existe $=$ des \unsure{drap.} de long. arbitraire}

% pale vertical watermark
\rotatebox{90}{\textsc{\unsure{ra Strong Extra}}}

```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/012_lowmargin.jpg

Alignment requires recheck: no flag

Review note: Il and long. are legible in the rotated margin.

### C-013-U001 (C line 1)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 1.

Source C token:

```tex
\unsure{..|.}
```

Source C context:

```tex
\scanpage{13}\mspage{12\unsure{..|.}}
% ink top, first two lines
\unsure{et|Et} choisissons une ``origine'' $a$ dans $\unsure{E|\mathcal
```

Aligned final span:

```tex
\unsure{..|.}
```

Final context (up to 100 characters either side):

```tex
\scanpage{13}\mspage{12\unsure{..|.}}
% ink top, first two lines
et choisissons une ``origine'' $a$ dans $\unsure{\varepsilon|\mathcal E
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/013_top.jpg

Alignment requires recheck: no flag

Review note: Page-number points, shortened entièrement and crossed de/la paire remain uncertain.

### C-013-U002 (C line 3)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 3.

Source C token:

```tex
\unsure{et|Et}
```

Source C context:

```tex
\scanpage{13}\mspage{12\unsure{..|.}}
% ink top, first two lines
\unsure{et|Et} choisissons une ``origine'' $a$ dans $\unsure{E|\mathcal E}=\{a,b\}$ (ce qui va déterminer la relat
```

Aligned final span:

```tex
et
```

Final context (up to 100 characters either side):

```tex
\scanpage{13}\mspage{12\unsure{..|.}}
% ink top, first two lines
et choisissons une ``origine'' $a$ dans $\unsure{\varepsilon|\mathcal E|E}=\{a,b\}$ (ce qui va détermi
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/013_top.jpg

Alignment requires recheck: no flag

Review note: Lowercase et, définissant, déterminée and live du are legible.

### C-013-U003 (C line 3)

Mechanical state: **unsure token(s) overlap changed alignment; inspect**. Final aligned line: 3.

Source C token:

```tex
\unsure{E|\mathcal E}
```

Source C context:

```tex
ge{12\unsure{..|.}}
% ink top, first two lines
\unsure{et|Et} choisissons une ``origine'' $a$ dans $\unsure{E|\mathcal E}=\{a,b\}$ (ce qui va déterminer la relation d'ordre).

% ink upper third, Considérons
\deleted{Soit}
```

Aligned final span:

```tex
\unsure{\varepsilon|\mathcal E|E}
```

Final context (up to 100 characters either side):

```tex
age{13}\mspage{12\unsure{..|.}}
% ink top, first two lines
et choisissons une ``origine'' $a$ dans $\unsure{\varepsilon|\mathcal E|E}=\{a,b\}$ (ce qui va déterminer la relation d'ordre).

% ink upper third, Considérons
\deleted{Soit}
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: revised

Crop links: crops/013_top.jpg

Alignment requires recheck: no flag

Review note: The rounded epsilon/E symbol retains the same alternatives used for this sign on neighbouring pages.

### C-013-U004 (C line 6)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 6.

Source C token:

```tex
\unsure{définissant}
```

Source C context:

```tex
 third, Considérons
\deleted{Soit} \deleted{Alors} Considérons sur $\mathcal L$ la relation d'ordre \unsure{définissant} le biordre, telle que $a<b$. On va voir qu'elle est \unsure{entièmt|entièrement} \unsure{déterminée
```

Aligned final span:

```tex
définissant
```

Final context (up to 100 characters either side):

```tex
 third, Considérons
\deleted{Soit} \deleted{Alors} Considérons sur $\mathcal L$ la relation d'ordre définissant le biordre, telle que $a<b$. On va voir qu'elle est \unsure{entièmt|entièrement} déterminée par la 
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/013_top.jpg

Alignment requires recheck: no flag

Review note: Lowercase et, définissant, déterminée and live du are legible.

### C-013-U005 (C line 6)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 6.

Source C token:

```tex
\unsure{entièmt|entièrement}
```

Source C context:

```tex
cal L$ la relation d'ordre \unsure{définissant} le biordre, telle que $a<b$. On va voir qu'elle est \unsure{entièmt|entièrement} \unsure{déterminée} par la conn. \deleted{\unsure{de}}\unsure{du} \deleted{\unsure{la paire}}\inser
```

Aligned final span:

```tex
\unsure{entièmt|entièrement}
```

Final context (up to 100 characters either side):

```tex
ur $\mathcal L$ la relation d'ordre définissant le biordre, telle que $a<b$. On va voir qu'elle est \unsure{entièmt|entièrement} déterminée par la conn. \deleted{\unsure{de}}du \deleted{\unsure{la paire}}\inserted{couple} $(a,b)
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/013_top.jpg

Alignment requires recheck: no flag

Review note: Page-number points, shortened entièrement and crossed de/la paire remain uncertain.

### C-013-U006 (C line 6)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 6.

Source C token:

```tex
\unsure{déterminée}
```

Source C context:

```tex
nsure{définissant} le biordre, telle que $a<b$. On va voir qu'elle est \unsure{entièmt|entièrement} \unsure{déterminée} par la conn. \deleted{\unsure{de}}\unsure{du} \deleted{\unsure{la paire}}\inserted{couple} $(a,b)$

```

Aligned final span:

```tex
déterminée
```

Final context (up to 100 characters either side):

```tex
'ordre définissant le biordre, telle que $a<b$. On va voir qu'elle est \unsure{entièmt|entièrement} déterminée par la conn. \deleted{\unsure{de}}du \deleted{\unsure{la paire}}\inserted{couple} $(a,b)$

% ink up
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/013_top.jpg

Alignment requires recheck: no flag

Review note: Lowercase et, définissant, déterminée and live du are legible.

### C-013-U007 (C line 6)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 6.

Source C token:

```tex
\unsure{de}
```

Source C context:

```tex
a<b$. On va voir qu'elle est \unsure{entièmt|entièrement} \unsure{déterminée} par la conn. \deleted{\unsure{de}}\unsure{du} \deleted{\unsure{la paire}}\inserted{couple} $(a,b)$

% ink upper middle, On aura, thre
```

Aligned final span:

```tex
\unsure{de}
```

Final context (up to 100 characters either side):

```tex
lle que $a<b$. On va voir qu'elle est \unsure{entièmt|entièrement} déterminée par la conn. \deleted{\unsure{de}}du \deleted{\unsure{la paire}}\inserted{couple} $(a,b)$

% ink upper middle, On aura, three definin
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/013_top.jpg

Alignment requires recheck: no flag

Review note: Page-number points, shortened entièrement and crossed de/la paire remain uncertain.

### C-013-U008 (C line 6)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 6.

Source C token:

```tex
\unsure{du}
```

Source C context:

```tex
voir qu'elle est \unsure{entièmt|entièrement} \unsure{déterminée} par la conn. \deleted{\unsure{de}}\unsure{du} \deleted{\unsure{la paire}}\inserted{couple} $(a,b)$

% ink upper middle, On aura, three defining s
```

Aligned final span:

```tex
du
```

Final context (up to 100 characters either side):

```tex
$. On va voir qu'elle est \unsure{entièmt|entièrement} déterminée par la conn. \deleted{\unsure{de}}du \deleted{\unsure{la paire}}\inserted{couple} $(a,b)$

% ink upper middle, On aura, three defining s
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/013_top.jpg

Alignment requires recheck: no flag

Review note: Lowercase et, définissant, déterminée and live du are legible.

### C-013-U009 (C line 6)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 6.

Source C token:

```tex
\unsure{la paire}
```

Source C context:

```tex
ure{entièmt|entièrement} \unsure{déterminée} par la conn. \deleted{\unsure{de}}\unsure{du} \deleted{\unsure{la paire}}\inserted{couple} $(a,b)$

% ink upper middle, On aura, three defining sets
On \unsure{aura|a} \uns
```

Aligned final span:

```tex
\unsure{la paire}
```

Final context (up to 100 characters either side):

```tex
r qu'elle est \unsure{entièmt|entièrement} déterminée par la conn. \deleted{\unsure{de}}du \deleted{\unsure{la paire}}\inserted{couple} $(a,b)$

% ink upper middle, On aura, three defining sets
On aura \unsure{.}
% sl
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/013_top.jpg

Alignment requires recheck: no flag

Review note: Page-number points, shortened entièrement and crossed de/la paire remain uncertain.

### C-013-U010 (C line 9)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 9.

Source C token:

```tex
\unsure{aura|a}
```

Source C context:

```tex
ed{\unsure{la paire}}\inserted{couple} $(a,b)$

% ink upper middle, On aura, three defining sets
On \unsure{aura|a} \unsure{.}
% slanted
\margin{déterminés par $R$}
\[
\left\{\begin{aligned}
\mathcal L_{\deleted{\un
```

Aligned final span:

```tex
aura
```

Final context (up to 100 characters either side):

```tex
ed{\unsure{la paire}}\inserted{couple} $(a,b)$

% ink upper middle, On aura, three defining sets
On aura \unsure{.}
% slanted
\margin{déterminés par $R$}
\[
\left\{\begin{aligned}
\mathcal L_{\deleted{\un
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/013_sets.jpg

Alignment requires recheck: no flag

Review note: Aura includes its r stroke, not only a.

### C-013-U011 (C line 9)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 9.

Source C token:

```tex
\unsure{.}
```

Source C context:

```tex
ire}}\inserted{couple} $(a,b)$

% ink upper middle, On aura, three defining sets
On \unsure{aura|a} \unsure{.}
% slanted
\margin{déterminés par $R$}
\[
\left\{\begin{aligned}
\mathcal L_{\deleted{\unsure{>}}\ge
```

Aligned final span:

```tex
\unsure{.}
```

Final context (up to 100 characters either side):

```tex
nsure{la paire}}\inserted{couple} $(a,b)$

% ink upper middle, On aura, three defining sets
On aura \unsure{.}
% slanted
\margin{déterminés par $R$}
\[
\left\{\begin{aligned}
\mathcal L_{\deleted{\unsure{>}}\ge
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/013_sets.jpg

Alignment requires recheck: no flag

Review note: Detached point and crossed relation/letters around the three set definitions remain uncertain.

### C-013-U012 (C line 14)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 14.

Source C token:

```tex
\unsure{>}
```

Source C context:

```tex
|a} \unsure{.}
% slanted
\margin{déterminés par $R$}
\[
\left\{\begin{aligned}
\mathcal L_{\deleted{\unsure{>}}\geq b}&=\{\,x\in L\mid\deleted{x=b\text{ ou}}\ \inserted{x=b\text{ ou}}\ b\text{ entre }a\text{ et
```

Aligned final span:

```tex
\unsure{>}
```

Final context (up to 100 characters either side):

```tex
ura \unsure{.}
% slanted
\margin{déterminés par $R$}
\[
\left\{\begin{aligned}
\mathcal L_{\deleted{\unsure{>}}\geq b}&=\{\,x\in\mathcal L\mid\deleted{x=b\text{ ou}}\ \inserted{x=b\text{ ou}}\ b\text{ entre }a\
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/013_sets.jpg

Alignment requires recheck: no flag

Review note: Detached point and crossed relation/letters around the three set definitions remain uncertain.

### C-013-U013 (C line 14)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 14.

Source C token:

```tex
\unsure{a,b|a<b}
```

Source C context:

```tex
mid\deleted{x=b\text{ ou}}\ \inserted{x=b\text{ ou}}\ b\text{ entre }a\text{ et }x\,\}\quad\deleted{\unsure{a,b|a<b}.}\\
\mathcal L_{\leq a}&=\{\,x\in L\mid\inserted{x=a\text{ ou}}\ a\text{ entre }\deleted{\unsure{a}
```

Aligned final span:

```tex
\unsure{a,b|a<b}
```

Final context (up to 100 characters either side):

```tex
mid\deleted{x=b\text{ ou}}\ \inserted{x=b\text{ ou}}\ b\text{ entre }a\text{ et }x\,\}\quad\deleted{\unsure{a,b|a<b}.}\\
\mathcal L_{\leq a}&=\{\,x\in\mathcal L\mid\inserted{x=a\text{ ou}}\ a\text{ entre }\deleted{\u
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/013_sets.jpg

Alignment requires recheck: no flag

Review note: Detached point and crossed relation/letters around the three set definitions remain uncertain.

### C-013-U014 (C line 15)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 15.

Source C token:

```tex
\unsure{a}
```

Source C context:

```tex
e{a,b|a<b}.}\\
\mathcal L_{\leq a}&=\{\,x\in L\mid\inserted{x=a\text{ ou}}\ a\text{ entre }\deleted{\unsure{a}}b\text{ et }x\,\}\\
\deleted{\unsure{\mathcal L}}\mathopen{]}\deleted{\unsure{x}}a,b\mathclose{[}&=
```

Aligned final span:

```tex
\unsure{a}
```

Final context (up to 100 characters either side):

```tex
b}.}\\
\mathcal L_{\leq a}&=\{\,x\in\mathcal L\mid\inserted{x=a\text{ ou}}\ a\text{ entre }\deleted{\unsure{a}}b\text{ et }x\,\}\\
\deleted{\unsure{\mathcal L}}\mathopen{]}\deleted{\unsure{x}}a,b\mathclose{[}&=
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/013_sets.jpg

Alignment requires recheck: no flag

Review note: Detached point and crossed relation/letters around the three set definitions remain uncertain.

### C-013-U015 (C line 16)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 16.

Source C token:

```tex
\unsure{\mathcal L}
```

Source C context:

```tex
x\in L\mid\inserted{x=a\text{ ou}}\ a\text{ entre }\deleted{\unsure{a}}b\text{ et }x\,\}\\
\deleted{\unsure{\mathcal L}}\mathopen{]}\deleted{\unsure{x}}a,b\mathclose{[}&=\{\,x\in L\mid x\text{ entre }a\text{ et }b\,\}
\
```

Aligned final span:

```tex
\unsure{\mathcal L}
```

Final context (up to 100 characters either side):

```tex
hcal L\mid\inserted{x=a\text{ ou}}\ a\text{ entre }\deleted{\unsure{a}}b\text{ et }x\,\}\\
\deleted{\unsure{\mathcal L}}\mathopen{]}\deleted{\unsure{x}}a,b\mathclose{[}&=\{\,x\in\mathcal L\mid x\text{ entre }a\text{ et 
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/013_sets.jpg

Alignment requires recheck: no flag

Review note: Detached point and crossed relation/letters around the three set definitions remain uncertain.

### C-013-U016 (C line 16)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 16.

Source C token:

```tex
\unsure{x}
```

Source C context:

```tex
t{ entre }\deleted{\unsure{a}}b\text{ et }x\,\}\\
\deleted{\unsure{\mathcal L}}\mathopen{]}\deleted{\unsure{x}}a,b\mathclose{[}&=\{\,x\in L\mid x\text{ entre }a\text{ et }b\,\}
\end{aligned}\right.
\]
% ink lef
```

Aligned final span:

```tex
\unsure{x}
```

Final context (up to 100 characters either side):

```tex
t{ entre }\deleted{\unsure{a}}b\text{ et }x\,\}\\
\deleted{\unsure{\mathcal L}}\mathopen{]}\deleted{\unsure{x}}a,b\mathclose{[}&=\{\,x\in\mathcal L\mid x\text{ entre }a\text{ et }b\,\}
\end{aligned}\right.
\]
%
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/013_sets.jpg

Alignment requires recheck: no flag

Review note: Detached point and crossed relation/letters around the three set definitions remain uncertain.

### C-013-U017 (C line 21)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 21.

Source C token:

```tex
\unsure{donc}
```

Source C context:

```tex
 x\text{ entre }a\text{ et }b\,\}
\end{aligned}\right.
\]
% ink left, below brace
% slanted
\margin{\unsure{donc}}

% ink middle, question
\deleted{Quand}\inserted{Soient} $u,v\in L$, quand a-t-on
\[
u\leq v\qquad
```

Aligned final span:

```tex
donc
```

Final context (up to 100 characters either side):

```tex
 x\text{ entre }a\text{ et }b\,\}
\end{aligned}\right.
\]
% ink left, below brace
% slanted
\margin{donc}

% ink middle, question
\deleted{Quand}\inserted{Soient} $u,v\in\mathcal L$, quand a-t-on
\[
u\leq
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/013_donc.jpg

Alignment requires recheck: no flag

Review note: Rotated small word reads donc.

### C-013-U018 (C line 26)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 26.

Source C token:

```tex
\unsure{\mathord{?}|.}
```

Source C context:

```tex
}

% ink middle, question
\deleted{Quand}\inserted{Soient} $u,v\in L$, quand a-t-on
\[
u\leq v\qquad\unsure{\mathord{?}|.}
\]
Il faut et suffit qu'il existe
\[
\begin{aligned}
&\deleted{x\in}\quad x,y\in L\quad\text{tels q
```

Aligned final span:

```tex
\unsure{\mathord{?}|.}
```

Final context (up to 100 characters either side):

```tex
 middle, question
\deleted{Quand}\inserted{Soient} $u,v\in\mathcal L$, quand a-t-on
\[
u\leq v\qquad\unsure{\mathord{?}|.}
\]
Il faut et suffit qu'il existe
\[
\begin{aligned}
&\deleted{x\in}\quad x,y\in\mathcal L\quad\tex
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/013_question.jpg

Alignment requires recheck: no flag

Review note: The detached terminal sign may be a question mark or point; uncertainty preserved.

### C-013-U019 (C line 40)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 40.

Source C token:

```tex
\unsure{x}
```

Source C context:

```tex
{aligned}
\]
% ink bottom, i.e., left bracket
\[
\text{i.e.}\quad
\left[\begin{aligned}
&\deleted{\{\unsure{x},y,\unsure{u|b},v\}\ \text{est }\in\mathrm{Drap}(\mathcal L)}\\
&\qquad\deleted{x,y\in}\quad x\in L_
```

Aligned final span:

```tex
\unsure{x}
```

Final context (up to 100 characters either side):

```tex
{aligned}
\]
% ink bottom, i.e., left bracket
\[
\text{i.e.}\quad
\left[\begin{aligned}
&\deleted{\{\unsure{x},y,\unsure{u|b},v\}\ \text{est }\in\mathrm{Drap}(\mathcal L)}\\
&\qquad\deleted{x,y\in}\quad x\in\ma
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/013_bottom.jpg

Alignment requires recheck: no flag

Review note: Crossed finite-set variables remain partly covered by the cancellation line.

### C-013-U020 (C line 40)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 40.

Source C token:

```tex
\unsure{u|b}
```

Source C context:

```tex
% ink bottom, i.e., left bracket
\[
\text{i.e.}\quad
\left[\begin{aligned}
&\deleted{\{\unsure{x},y,\unsure{u|b},v\}\ \text{est }\in\mathrm{Drap}(\mathcal L)}\\
&\qquad\deleted{x,y\in}\quad x\in L_{\leq a},\ y\in
```

Aligned final span:

```tex
\unsure{u|b}
```

Final context (up to 100 characters either side):

```tex
% ink bottom, i.e., left bracket
\[
\text{i.e.}\quad
\left[\begin{aligned}
&\deleted{\{\unsure{x},y,\unsure{u|b},v\}\ \text{est }\in\mathrm{Drap}(\mathcal L)}\\
&\qquad\deleted{x,y\in}\quad x\in\mathcal L_{\leq a
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/013_bottom.jpg

Alignment requires recheck: no flag

Review note: Crossed finite-set variables remain partly covered by the cancellation line.

### C-013-U021 (C line 41)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 41.

Source C token:

```tex
\unsure{<|\leq}
```

Source C context:

```tex
ap}(\mathcal L)}\\
&\qquad\deleted{x,y\in}\quad x\in L_{\leq a},\ y\in L_{\geq b}\quad(\text{donc }x\unsure{<|\leq}y)\\
&\deleted{\text{avec }x\text{ plus petit élément}}\\
&\deleted{u\text{ est entre}}\quad u,v\tex
```

Aligned final span:

```tex
<
```

Final context (up to 100 characters either side):

```tex
\\
&\qquad\deleted{x,y\in}\quad x\in\mathcal L_{\leq a},\ y\in\mathcal L_{\geq b}\quad(\text{donc }x<y)\\
&\deleted{\text{avec }x\text{ plus petit élément}}\\
&\deleted{u\text{ est entre}}\quad u,v\tex
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/013_bottom.jpg

Alignment requires recheck: no flag

Review note: Strict < has no equality stroke; final point beside the u-between clause is visible.

### C-013-U022 (C line 44)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 44.

Source C token:

```tex
\unsure{.}
```

Source C context:

```tex
est entre}}\quad u,v\text{ sont entre }x\text{ et }y\\
&\quad u\text{ est entre }x\text{ et }v\qquad\unsure{.}\\
&\quad v\text{ est entre }u\text{ et }y
\end{aligned}\right.
\]

```

Aligned final span:

```tex
.
```

Final context (up to 100 characters either side):

```tex
est entre}}\quad u,v\text{ sont entre }x\text{ et }y\\
&\quad u\text{ est entre }x\text{ et }v\qquad.\\
&\quad v\text{ est entre }u\text{ et }y
\end{aligned}\right.
\]

% pale vertical watermark
\rotat
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/013_bottom.jpg

Alignment requires recheck: no flag

Review note: Strict < has no equality stroke; final point beside the u-between clause is visible.

### C-014-U001 (C line 5)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 5.

Source C token:

```tex
\unsure{élémts|éléments}
```

Source C context:

```tex
 il faut simplement vérifier le

\uline{Lemme} Soit $\mathcal L$ un ens ordonné, et $x,y,u,v$ trois \unsure{élémts|éléments}, tels que
% ink upper third, clauses a–d and brace at right
\[
\begin{aligned}
&\text{a)}\quad u,v\
```

Aligned final span:

```tex
\unsure{élémts|éléments}
```

Final context (up to 100 characters either side):

```tex
 il faut simplement vérifier le

\uline{Lemme} Soit $\mathcal L$ un ens ordonné, et $x,y,u,v$ trois \unsure{élémts|éléments}, tels que
% ink upper third, clauses a–d and brace at right
\[
\begin{aligned}
&\text{a)}\quad u,v\
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/014_top.jpg

Alignment requires recheck: no flag

Review note: Ending of élémts/éléments is compressed; literal trois before four variables is clear and unchanged.

### C-014-U002 (C line 12)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 12.

Source C token:

```tex
\unsure{(}
```

Source C context:

```tex
t entre }x\text{ et }y\\
&\left.\begin{aligned}
&\text{b)}\quad u\text{ est entre }x\text{ et }v\\
&\unsure{(}[\,\text{c)}\quad v\text{ est entre }u\text{ et }y\,]\deleted{\unsure{)}}
\end{aligned}\ \right\}\qu
```

Aligned final span:

```tex
(
```

Final context (up to 100 characters either side):

```tex
t entre }x\text{ et }y\\
&\left.\begin{aligned}
&\text{b)}\quad u\text{ est entre }x\text{ et }v\\
&([\,\text{c)}\quad v\text{ est entre }u\text{ et }y\,]\deleted{\unsure{)}}
\end{aligned}\ \right\}\qu
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/014_conditions.jpg

Alignment requires recheck: no flag

Review note: Opening parenthesis and small en in the brace annotation are visible.

### C-014-U003 (C line 12)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 12.

Source C token:

```tex
\unsure{)}
```

Source C context:

```tex
est entre }x\text{ et }v\\
&\unsure{(}[\,\text{c)}\quad v\text{ est entre }u\text{ et }y\,]\deleted{\unsure{)}}
\end{aligned}\ \right\}\quad
\begin{aligned}&\text{une des deux}\\&\text{\unsure{en} suffit}\end{a
```

Aligned final span:

```tex
\unsure{)}
```

Final context (up to 100 characters either side):

```tex
 u\text{ est entre }x\text{ et }v\\
&([\,\text{c)}\quad v\text{ est entre }u\text{ et }y\,]\deleted{\unsure{)}}
\end{aligned}\ \right\}\quad
\begin{aligned}&\text{une des deux}\\&\text{en suffit}\end{aligned}\\
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/014_conditions.jpg

Alignment requires recheck: no flag

Review note: Old closing mark is crossed and remains uncertain.

### C-014-U004 (C line 14)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 14.

Source C token:

```tex
\unsure{en}
```

Source C context:

```tex
 }y\,]\deleted{\unsure{)}}
\end{aligned}\ \right\}\quad
\begin{aligned}&\text{une des deux}\\&\text{\unsure{en} suffit}\end{aligned}\\
&\text{d)}\quad x<y\quad,
\end{aligned}
\]
alors on a
\[
x\leq u\leq v\leq y
```

Aligned final span:

```tex
en
```

Final context (up to 100 characters either side):

```tex
 }y\,]\deleted{\unsure{)}}
\end{aligned}\ \right\}\quad
\begin{aligned}&\text{une des deux}\\&\text{en suffit}\end{aligned}\\
&\text{d)}\quad x<y\quad,
\end{aligned}
\]
alors on a
\[
x\leq u\leq v\leq y
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/014_conditions.jpg

Alignment requires recheck: no flag

Review note: Opening parenthesis and small en in the brace annotation are visible.

### C-014-U005 (C line 24)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 24.

Source C token:

```tex
\unsure{Dém|Dém.}
```

Source C context:

```tex
,
\end{aligned}
\]
alors on a
\[
x\leq u\leq v\leq y
\]

% ink middle, Dém, first four lines
\uline{\unsure{Dém|Dém.}} \deleted{\unsure{L'ass|L'assert}} \unsure{les|Les} conditions b)\unsure{,} c) d) impliquent que $I
```

Aligned final span:

```tex
Dém
```

Final context (up to 100 characters either side):

```tex
,
\end{aligned}
\]
alors on a
\[
x\leq u\leq v\leq y
\]

% ink middle, Dém, first four lines
\uline{Dém} \deleted{\unsure{L'ass|L'assert}} \unsure{les|Les} conditions b) c) d) impliquent que $I\deleted{\
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/014_proof.jpg

Alignment requires recheck: no flag

Review note: Dém has no point, and no comma is visible after b) in the proof sentence.

### C-014-U006 (C line 24)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 24.

Source C token:

```tex
\unsure{L'ass|L'assert}
```

Source C context:

```tex
a
\[
x\leq u\leq v\leq y
\]

% ink middle, Dém, first four lines
\uline{\unsure{Dém|Dém.}} \deleted{\unsure{L'ass|L'assert}} \unsure{les|Les} conditions b)\unsure{,} c) d) impliquent que $I\deleted{\unsure{\{x}}=\{x,y,u,v\}
```

Aligned final span:

```tex
\unsure{L'ass|L'assert}
```

Final context (up to 100 characters either side):

```tex
}
\]
alors on a
\[
x\leq u\leq v\leq y
\]

% ink middle, Dém, first four lines
\uline{Dém} \deleted{\unsure{L'ass|L'assert}} \unsure{les|Les} conditions b) c) d) impliquent que $I\deleted{\unsure{\{x}}=\{x,y,u,v\}$ est un d
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/014_proof.jpg

Alignment requires recheck: no flag

Review note: Crossed starts, letter case, old set fragment, abbreviation SPG and element ending remain uncertain.

### C-014-U007 (C line 24)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 24.

Source C token:

```tex
\unsure{les|Les}
```

Source C context:

```tex
\]

% ink middle, Dém, first four lines
\uline{\unsure{Dém|Dém.}} \deleted{\unsure{L'ass|L'assert}} \unsure{les|Les} conditions b)\unsure{,} c) d) impliquent que $I\deleted{\unsure{\{x}}=\{x,y,u,v\}$ est un drapeau, 
```

Aligned final span:

```tex
\unsure{les|Les}
```

Final context (up to 100 characters either side):

```tex
u\leq v\leq y
\]

% ink middle, Dém, first four lines
\uline{Dém} \deleted{\unsure{L'ass|L'assert}} \unsure{les|Les} conditions b) c) d) impliquent que $I\deleted{\unsure{\{x}}=\{x,y,u,v\}$ est un drapeau, \deleted{\
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/014_proof.jpg

Alignment requires recheck: no flag

Review note: Crossed starts, letter case, old set fragment, abbreviation SPG and element ending remain uncertain.

### C-014-U008 (C line 24)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 24.

Source C token:

```tex
\unsure{,}
```

Source C context:

```tex
our lines
\uline{\unsure{Dém|Dém.}} \deleted{\unsure{L'ass|L'assert}} \unsure{les|Les} conditions b)\unsure{,} c) d) impliquent que $I\deleted{\unsure{\{x}}=\{x,y,u,v\}$ est un drapeau, \deleted{\unsure{Prouvon
```

Aligned final span:

```tex

```

Final context (up to 100 characters either side):

```tex
, Dém, first four lines
\uline{Dém} \deleted{\unsure{L'ass|L'assert}} \unsure{les|Les} conditions b) c) d) impliquent que $I\deleted{\unsure{\{x}}=\{x,y,u,v\}$ est un drapeau, \deleted{\unsure{Prouvon
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/014_proof.jpg

Alignment requires recheck: no flag

Review note: Dém has no point, and no comma is visible after b) in the proof sentence.

### C-014-U009 (C line 24)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 24.

Source C token:

```tex
\unsure{\{x}
```

Source C context:

```tex
d{\unsure{L'ass|L'assert}} \unsure{les|Les} conditions b)\unsure{,} c) d) impliquent que $I\deleted{\unsure{\{x}}=\{x,y,u,v\}$ est un drapeau, \deleted{\unsure{Prouvons|Prenons}} et \unsure{SPG} $\mathcal L=I$ es
```

Aligned final span:

```tex
\unsure{\{x}
```

Final context (up to 100 characters either side):

```tex
m} \deleted{\unsure{L'ass|L'assert}} \unsure{les|Les} conditions b) c) d) impliquent que $I\deleted{\unsure{\{x}}=\{x,y,u,v\}$ est un drapeau, \deleted{\unsure{Prouvons|Prenons}} et \unsure{SPG} $\mathcal L=I$ es
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/014_proof.jpg

Alignment requires recheck: no flag

Review note: Crossed starts, letter case, old set fragment, abbreviation SPG and element ending remain uncertain.

### C-014-U010 (C line 24)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 24.

Source C token:

```tex
\unsure{Prouvons|Prenons}
```

Source C context:

```tex
ns b)\unsure{,} c) d) impliquent que $I\deleted{\unsure{\{x}}=\{x,y,u,v\}$ est un drapeau, \deleted{\unsure{Prouvons|Prenons}} et \unsure{SPG} $\mathcal L=I$ est un ens tot. ordonné \deleted{que $x$ en} à 2, 3, ou 4 \unsure{é
```

Aligned final span:

```tex
\unsure{Prouvons|Prenons}
```

Final context (up to 100 characters either side):

```tex
} conditions b) c) d) impliquent que $I\deleted{\unsure{\{x}}=\{x,y,u,v\}$ est un drapeau, \deleted{\unsure{Prouvons|Prenons}} et \unsure{SPG} $\mathcal L=I$ est un ens tot. ordonné \deleted{que $x$ en} à 2, 3, ou 4 \unsure{é
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/014_proof.jpg

Alignment requires recheck: no flag

Review note: Crossed starts, letter case, old set fragment, abbreviation SPG and element ending remain uncertain.

### C-014-U011 (C line 24)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 24.

Source C token:

```tex
\unsure{SPG}
```

Source C context:

```tex
nt que $I\deleted{\unsure{\{x}}=\{x,y,u,v\}$ est un drapeau, \deleted{\unsure{Prouvons|Prenons}} et \unsure{SPG} $\mathcal L=I$ est un ens tot. ordonné \deleted{que $x$ en} à 2, 3, ou 4 \unsure{élémts|éléments}.

```

Aligned final span:

```tex
\unsure{SPG}
```

Final context (up to 100 characters either side):

```tex
nt que $I\deleted{\unsure{\{x}}=\{x,y,u,v\}$ est un drapeau, \deleted{\unsure{Prouvons|Prenons}} et \unsure{SPG} $\mathcal L=I$ est un ens tot. ordonné \deleted{que $x$ en} à 2, 3, ou 4 \unsure{élémts|éléments}.

```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/014_proof.jpg

Alignment requires recheck: no flag

Review note: Crossed starts, letter case, old set fragment, abbreviation SPG and element ending remain uncertain.

### C-014-U012 (C line 24)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 24.

Source C token:

```tex
\unsure{élémts|éléments}
```

Source C context:

```tex
|Prenons}} et \unsure{SPG} $\mathcal L=I$ est un ens tot. ordonné \deleted{que $x$ en} à 2, 3, ou 4 \unsure{élémts|éléments}.
% ink middle, crossed proof and interlinear replacement
\deleted{Alors \unsure{Prouvons|Prenons}} 
```

Aligned final span:

```tex
\unsure{élémts|éléments}
```

Final context (up to 100 characters either side):

```tex
|Prenons}} et \unsure{SPG} $\mathcal L=I$ est un ens tot. ordonné \deleted{que $x$ en} à 2, 3, ou 4 \unsure{élémts|éléments}.
% ink middle, crossed proof and interlinear replacement
\deleted{Alors \unsure{Prouvons|Prenons}} 
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/014_proof.jpg

Alignment requires recheck: no flag

Review note: Crossed starts, letter case, old set fragment, abbreviation SPG and element ending remain uncertain.

### C-014-U013 (C line 26)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 26.

Source C token:

```tex
\unsure{Prouvons|Prenons}
```

Source C context:

```tex
 4 \unsure{élémts|éléments}.
% ink middle, crossed proof and interlinear replacement
\deleted{Alors \unsure{Prouvons|Prenons}} \inserted{Comme $u,v$ sont} \deleted{que $x$ est le plus petit élément, donc (comme $x<y$) que l'o
```

Aligned final span:

```tex
\unsure{Prouvons|Prenons}
```

Final context (up to 100 characters either side):

```tex
 4 \unsure{élémts|éléments}.
% ink middle, crossed proof and interlinear replacement
\deleted{Alors \unsure{Prouvons|Prenons}} \inserted{Comme $u,v$ sont} \deleted{que $x$ est le plus petit élément, donc (comme $x<y$) que l'o
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/014_cancel.jpg

Alignment requires recheck: no flag

Review note: Crossed Prouvons/Prenons and the overwritten inequality fragment remain unresolved.

### C-014-U014 (C line 26)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 26.

Source C token:

```tex
\unsure{Supposons}
```

Source C context:

```tex
leted{que $x$ est le plus petit élément, donc (comme $x<y$) que l'on ne peut avoir $u<x$, ni $v<x$. \unsure{Supposons} $u<x$ ($<y$) ; comme $u$ est entre $x$ et $v$, on aurait \unsure{$v\leq u<$}\ $v<u<x<y$} \inserted{
```

Aligned final span:

```tex
Supposons
```

Final context (up to 100 characters either side):

```tex
leted{que $x$ est le plus petit élément, donc (comme $x<y$) que l'on ne peut avoir $u<x$, ni $v<x$. Supposons $u<x$ ($<y$) ; comme $u$ est entre $x$ et $v$, on aurait \unsure{$v\leq u<$}\ $v<u<x<y$} \inserted{
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/014_cancel.jpg

Alignment requires recheck: no flag

Review note: Supposons can be read through the broad cancellation.

### C-014-U015 (C line 26)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 26.

Source C token:

```tex
\unsure{$v\leq u<$}
```

Source C context:

```tex
 avoir $u<x$, ni $v<x$. \unsure{Supposons} $u<x$ ($<y$) ; comme $u$ est entre $x$ et $v$, on aurait \unsure{$v\leq u<$}\ $v<u<x<y$} \inserted{entre $x$ et $y$ et $x<y$,} on doit avoir $x\leq u,v\leq y$, \deleted{il rest
```

Aligned final span:

```tex
\unsure{$v\leq u<$}
```

Final context (up to 100 characters either side):

```tex
n ne peut avoir $u<x$, ni $v<x$. Supposons $u<x$ ($<y$) ; comme $u$ est entre $x$ et $v$, on aurait \unsure{$v\leq u<$}\ $v<u<x<y$} \inserted{entre $x$ et $y$ et $x<y$,} on doit avoir $x\leq u,v\leq y$, \deleted{il rest
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/014_cancel.jpg

Alignment requires recheck: no flag

Review note: Crossed Prouvons/Prenons and the overwritten inequality fragment remain unresolved.

### C-014-U016 (C line 32)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 32.

Source C token:

```tex
\unsure{rel.}
```

Source C context:

```tex
m, NB and lettered lines
\uline{NB} On a utilisé
\[
\begin{aligned}
&\text{a) la divisibilité de la \unsure{rel.} d'ordre}\\
&\text{b) le fait que }\mathcal L\text{ soit \unsure{filtrant}}\\
&\hspace{2em}\text{\un
```

Aligned final span:

```tex
rel.
```

Final context (up to 100 characters either side):

```tex
m, NB and lettered lines
\uline{NB} On a utilisé
\[
\begin{aligned}
&\text{a) la divisibilité de la rel. d'ordre}\\
&\text{b) le fait que }\mathcal L\text{ soit filtrant}\\
&\hspace{2em}\text{croissant et
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/014_nb.jpg

Alignment requires recheck: no flag

Review note: Rel., filtrant, croissant and décroissant are readable in the uncancelled NB.

### C-014-U017 (C line 33)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 33.

Source C token:

```tex
\unsure{filtrant}
```

Source C context:

```tex
text{a) la divisibilité de la \unsure{rel.} d'ordre}\\
&\text{b) le fait que }\mathcal L\text{ soit \unsure{filtrant}}\\
&\hspace{2em}\text{\unsure{croissant} et filtrant \unsure{décroissant}.}
\end{aligned}
\]
% ink 
```

Aligned final span:

```tex
filtrant
```

Final context (up to 100 characters either side):

```tex
igned}
&\text{a) la divisibilité de la rel. d'ordre}\\
&\text{b) le fait que }\mathcal L\text{ soit filtrant}\\
&\hspace{2em}\text{croissant et filtrant décroissant.}
\end{aligned}
\]
% ink last two lines
Et 
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/014_nb.jpg

Alignment requires recheck: no flag

Review note: Rel., filtrant, croissant and décroissant are readable in the uncancelled NB.

### C-014-U018 (C line 34)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 34.

Source C token:

```tex
\unsure{croissant}
```

Source C context:

```tex
l.} d'ordre}\\
&\text{b) le fait que }\mathcal L\text{ soit \unsure{filtrant}}\\
&\hspace{2em}\text{\unsure{croissant} et filtrant \unsure{décroissant}.}
\end{aligned}
\]
% ink last two lines
Et a) n'a servi qu'à montr
```

Aligned final span:

```tex
croissant
```

Final context (up to 100 characters either side):

```tex
é de la rel. d'ordre}\\
&\text{b) le fait que }\mathcal L\text{ soit filtrant}\\
&\hspace{2em}\text{croissant et filtrant décroissant.}
\end{aligned}
\]
% ink last two lines
Et a) n'a servi qu'à montrer que la
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/014_nb.jpg

Alignment requires recheck: no flag

Review note: Rel., filtrant, croissant and décroissant are readable in the uncancelled NB.

### C-014-U019 (C line 34)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 34.

Source C token:

```tex
\unsure{décroissant}
```

Source C context:

```tex
t que }\mathcal L\text{ soit \unsure{filtrant}}\\
&\hspace{2em}\text{\unsure{croissant} et filtrant \unsure{décroissant}.}
\end{aligned}
\]
% ink last two lines
Et a) n'a servi qu'à montrer que la relation ``$a$ et $b$ d
```

Aligned final span:

```tex
décroissant
```

Final context (up to 100 characters either side):

```tex
\
&\text{b) le fait que }\mathcal L\text{ soit filtrant}\\
&\hspace{2em}\text{croissant et filtrant décroissant.}
\end{aligned}
\]
% ink last two lines
Et a) n'a servi qu'à montrer que la relation ``$a$ et $b$ d
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/014_nb.jpg

Alignment requires recheck: no flag

Review note: Rel., filtrant, croissant and décroissant are readable in the uncancelled NB.

### C-015-U001 (C line 6)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 6.

Source C token:

```tex
\unsure{\underline R|R}
```

Source C context:

```tex
page{14}
% ink top, relations
Si on se donne à la fois les deux relations
\[
\left\{\begin{aligned}
\unsure{\underline R|R}(a,b)&\qquad \{a,b\}\in\mathrm{Drap}_2(L)\\
R(a,b,c)&\qquad b\text{ est str. entre }a\text{ et }c
\e
```

Aligned final span:

```tex
\unsure{\underline R|R}
```

Final context (up to 100 characters either side):

```tex
page{14}
% ink top, relations
Si on se donne à la fois les deux relations
\[
\left\{\begin{aligned}
\unsure{\underline R|R}(a,b)&\qquad \{a,b\}\in\mathrm{Drap}_2(\mathcal L)\\
R(a,b,c)&\qquad b\text{ est str. entre }a\text{
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/015_top.jpg

Alignment requires recheck: no flag

Review note: Short stroke below first R may be an underline or part of its leg.

### C-015-U002 (C line 10)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 10.

Source C token:

```tex
\unsure{récupérer}
```

Source C context:

```tex
ap}_2(L)\\
R(a,b,c)&\qquad b\text{ est str. entre }a\text{ et }c
\end{aligned}\right.
\]
alors pour \unsure{récupérer} le biordre, il suffit de supposer $\mathcal L$ filtrant croissant et filtrant décroissant, \deleted
```

Aligned final span:

```tex
récupérer
```

Final context (up to 100 characters either side):

```tex
thcal L)\\
R(a,b,c)&\qquad b\text{ est str. entre }a\text{ et }c
\end{aligned}\right.
\]
alors pour récupérer le biordre, il suffit de supposer $\mathcal L$ filtrant croissant et filtrant décroissant, \deleted
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/015_top.jpg

Alignment requires recheck: no flag

Review note: Récupérer is readable with its final r.

### C-015-U003 (C line 10)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 10.

Source C token:

```tex
\unsure{Si|si}
```

Source C context:

```tex
ffit de supposer $\mathcal L$ filtrant croissant et filtrant décroissant, \deleted{et les relations \unsure{Si|si}, \unsure{Cet|cet|Oct} \unsure{sur les}, filtrant \unsure{cr.} et \unsure{décr.} \unsure{sont} de \u
```

Aligned final span:

```tex
\unsure{Si|si}
```

Final context (up to 100 characters either side):

```tex
ffit de supposer $\mathcal L$ filtrant croissant et filtrant décroissant, \deleted{et les relations \unsure{Si|si}, \unsure{Cet|cet|Oct} \unsure{sur les}, filtrant \unsure{cr.} et \unsure{décr.} \unsure{sont} de \u
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/015_cancel.jpg

Alignment requires recheck: no flag

Review note: The multiply crossed three-line draft remains only partly recoverable; all existing alternatives are preserved.

### C-015-U004 (C line 10)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 10.

Source C token:

```tex
\unsure{Cet|cet|Oct}
```

Source C context:

```tex
 $\mathcal L$ filtrant croissant et filtrant décroissant, \deleted{et les relations \unsure{Si|si}, \unsure{Cet|cet|Oct} \unsure{sur les}, filtrant \unsure{cr.} et \unsure{décr.} \unsure{sont} de \unsure{qque|toutes} \un
```

Aligned final span:

```tex
\unsure{Cet|cet|Oct}
```

Final context (up to 100 characters either side):

```tex
 $\mathcal L$ filtrant croissant et filtrant décroissant, \deleted{et les relations \unsure{Si|si}, \unsure{Cet|cet|Oct} \unsure{sur les}, filtrant \unsure{cr.} et \unsure{décr.} \unsure{sont} de \unsure{qque|toutes} \un
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/015_cancel.jpg

Alignment requires recheck: no flag

Review note: The multiply crossed three-line draft remains only partly recoverable; all existing alternatives are preserved.

### C-015-U005 (C line 10)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 10.

Source C token:

```tex
\unsure{sur les}
```

Source C context:

```tex
t croissant et filtrant décroissant, \deleted{et les relations \unsure{Si|si}, \unsure{Cet|cet|Oct} \unsure{sur les}, filtrant \unsure{cr.} et \unsure{décr.} \unsure{sont} de \unsure{qque|toutes} \unsure{comp.|faç.} 
```

Aligned final span:

```tex
\unsure{sur les}
```

Final context (up to 100 characters either side):

```tex
t croissant et filtrant décroissant, \deleted{et les relations \unsure{Si|si}, \unsure{Cet|cet|Oct} \unsure{sur les}, filtrant \unsure{cr.} et \unsure{décr.} \unsure{sont} de \unsure{qque|toutes} \unsure{comp.|faç.} 
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/015_cancel.jpg

Alignment requires recheck: no flag

Review note: The multiply crossed three-line draft remains only partly recoverable; all existing alternatives are preserved.

### C-015-U006 (C line 10)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 10.

Source C token:

```tex
\unsure{cr.}
```

Source C context:

```tex
roissant, \deleted{et les relations \unsure{Si|si}, \unsure{Cet|cet|Oct} \unsure{sur les}, filtrant \unsure{cr.} et \unsure{décr.} \unsure{sont} de \unsure{qque|toutes} \unsure{comp.|faç.} \unsure{connexes|connue
```

Aligned final span:

```tex
\unsure{cr.}
```

Final context (up to 100 characters either side):

```tex
roissant, \deleted{et les relations \unsure{Si|si}, \unsure{Cet|cet|Oct} \unsure{sur les}, filtrant \unsure{cr.} et \unsure{décr.} \unsure{sont} de \unsure{qque|toutes} \unsure{comp.|faç.} \unsure{connexes|connue
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/015_cancel.jpg

Alignment requires recheck: no flag

Review note: The multiply crossed three-line draft remains only partly recoverable; all existing alternatives are preserved.

### C-015-U007 (C line 10)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 10.

Source C token:

```tex
\unsure{décr.}
```

Source C context:

```tex
ed{et les relations \unsure{Si|si}, \unsure{Cet|cet|Oct} \unsure{sur les}, filtrant \unsure{cr.} et \unsure{décr.} \unsure{sont} de \unsure{qque|toutes} \unsure{comp.|faç.} \unsure{connexes|connues en} \unsure{$S_0
```

Aligned final span:

```tex
\unsure{décr.}
```

Final context (up to 100 characters either side):

```tex
ed{et les relations \unsure{Si|si}, \unsure{Cet|cet|Oct} \unsure{sur les}, filtrant \unsure{cr.} et \unsure{décr.} \unsure{sont} de \unsure{qque|toutes} \unsure{comp.|faç.} \unsure{connexes|connues en} \unsure{$S_0
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/015_cancel.jpg

Alignment requires recheck: no flag

Review note: The multiply crossed three-line draft remains only partly recoverable; all existing alternatives are preserved.

### C-015-U008 (C line 10)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 10.

Source C token:

```tex
\unsure{sont}
```

Source C context:

```tex
ions \unsure{Si|si}, \unsure{Cet|cet|Oct} \unsure{sur les}, filtrant \unsure{cr.} et \unsure{décr.} \unsure{sont} de \unsure{qque|toutes} \unsure{comp.|faç.} \unsure{connexes|connues en} \unsure{$S_0$|$v_0$|$0$}} 
```

Aligned final span:

```tex
\unsure{sont}
```

Final context (up to 100 characters either side):

```tex
ions \unsure{Si|si}, \unsure{Cet|cet|Oct} \unsure{sur les}, filtrant \unsure{cr.} et \unsure{décr.} \unsure{sont} de \unsure{qque|toutes} \unsure{comp.|faç.} \unsure{connexes|connues en} \unsure{$S_0$|$v_0$|$0$}} 
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/015_cancel.jpg

Alignment requires recheck: no flag

Review note: The multiply crossed three-line draft remains only partly recoverable; all existing alternatives are preserved.

### C-015-U009 (C line 10)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 10.

Source C token:

```tex
\unsure{qque|toutes}
```

Source C context:

```tex
i}, \unsure{Cet|cet|Oct} \unsure{sur les}, filtrant \unsure{cr.} et \unsure{décr.} \unsure{sont} de \unsure{qque|toutes} \unsure{comp.|faç.} \unsure{connexes|connues en} \unsure{$S_0$|$v_0$|$0$}} 

% ink middle, On va vo
```

Aligned final span:

```tex
\unsure{qque|toutes}
```

Final context (up to 100 characters either side):

```tex
i}, \unsure{Cet|cet|Oct} \unsure{sur les}, filtrant \unsure{cr.} et \unsure{décr.} \unsure{sont} de \unsure{qque|toutes} \unsure{comp.|faç.} \unsure{connexes|connues en} \unsure{$S_0$|$v_0$|$0$}} 

% ink middle, On va vo
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/015_cancel.jpg

Alignment requires recheck: no flag

Review note: The multiply crossed three-line draft remains only partly recoverable; all existing alternatives are preserved.

### C-015-U010 (C line 10)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 10.

Source C token:

```tex
\unsure{comp.|faç.}
```

Source C context:

```tex
ct} \unsure{sur les}, filtrant \unsure{cr.} et \unsure{décr.} \unsure{sont} de \unsure{qque|toutes} \unsure{comp.|faç.} \unsure{connexes|connues en} \unsure{$S_0$|$v_0$|$0$}} 

% ink middle, On va voir
\deleted{\unsure{
```

Aligned final span:

```tex
\unsure{comp.|faç.}
```

Final context (up to 100 characters either side):

```tex
ct} \unsure{sur les}, filtrant \unsure{cr.} et \unsure{décr.} \unsure{sont} de \unsure{qque|toutes} \unsure{comp.|faç.} \unsure{connexes|connues en} \unsure{$S_0$|$v_0$|$0$}} 

% ink middle, On va voir
\deleted{\unsure{
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/015_cancel.jpg

Alignment requires recheck: no flag

Review note: The multiply crossed three-line draft remains only partly recoverable; all existing alternatives are preserved.

### C-015-U011 (C line 10)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 10.

Source C token:

```tex
\unsure{connexes|connues en}
```

Source C context:

```tex
, filtrant \unsure{cr.} et \unsure{décr.} \unsure{sont} de \unsure{qque|toutes} \unsure{comp.|faç.} \unsure{connexes|connues en} \unsure{$S_0$|$v_0$|$0$}} 

% ink middle, On va voir
\deleted{\unsure{On va}} On va voir maintenant
```

Aligned final span:

```tex
\unsure{connexes|connues en}
```

Final context (up to 100 characters either side):

```tex
, filtrant \unsure{cr.} et \unsure{décr.} \unsure{sont} de \unsure{qque|toutes} \unsure{comp.|faç.} \unsure{connexes|connues en} \unsure{$S_0$|$v_0$|$0$}} 

% ink middle, On va voir
\deleted{\unsure{On va}} On va voir maintenant
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/015_cancel.jpg

Alignment requires recheck: no flag

Review note: The multiply crossed three-line draft remains only partly recoverable; all existing alternatives are preserved.

### C-015-U012 (C line 10)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 10.

Source C token:

```tex
\unsure{$S_0$|$v_0$|$0$}
```

Source C context:

```tex
nsure{décr.} \unsure{sont} de \unsure{qque|toutes} \unsure{comp.|faç.} \unsure{connexes|connues en} \unsure{$S_0$|$v_0$|$0$}} 

% ink middle, On va voir
\deleted{\unsure{On va}} On va voir maintenant comment la connaissance\
```

Aligned final span:

```tex
\unsure{$S_0$|$v_0$|$0$}
```

Final context (up to 100 characters either side):

```tex
nsure{décr.} \unsure{sont} de \unsure{qque|toutes} \unsure{comp.|faç.} \unsure{connexes|connues en} \unsure{$S_0$|$v_0$|$0$}} 

% ink middle, On va voir
\deleted{\unsure{On va}} On va voir maintenant comment la connaissance\
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/015_cancel.jpg

Alignment requires recheck: no flag

Review note: The multiply crossed three-line draft remains only partly recoverable; all existing alternatives are preserved.

### C-015-U013 (C line 13)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 13.

Source C token:

```tex
\unsure{On va}
```

Source C context:

```tex
p.|faç.} \unsure{connexes|connues en} \unsure{$S_0$|$v_0$|$0$}} 

% ink middle, On va voir
\deleted{\unsure{On va}} On va voir maintenant comment la connaissance\inserted{ de $\mathrm{Drap}_2(L)$, et} pour $\unsure
```

Aligned final span:

```tex
\unsure{On va}
```

Final context (up to 100 characters either side):

```tex
p.|faç.} \unsure{connexes|connues en} \unsure{$S_0$|$v_0$|$0$}} 

% ink middle, On va voir
\deleted{\unsure{On va}} On va voir maintenant comment la connaissance\inserted{ de $\mathrm{Drap}_2(\mathcal L)$, et} pour
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/015_middle.jpg

Alignment requires recheck: no flag

Review note: Old On va, letter before L, crossed x, cup/comma, old relation and terminal punctuation remain uncertain.

### C-015-U014 (C line 13)

Mechanical state: **unsure token(s) overlap changed alignment; inspect**. Final aligned line: 13.

Source C token:

```tex
\unsure{E|\mathcal E}
```

Source C context:

```tex
{On va}} On va voir maintenant comment la connaissance\inserted{ de $\mathrm{Drap}_2(L)$, et} pour $\unsure{E|\mathcal E}\in\mathrm{Drap}_2(\deleted{\unsure{I}}L)$, de la \unsure{décomp.} de
% ink middle, C(E) and continu
```

Aligned final span:

```tex
\unsure{\varepsilon|\mathcal E|E}
```

Final context (up to 100 characters either side):

```tex
On va voir maintenant comment la connaissance\inserted{ de $\mathrm{Drap}_2(\mathcal L)$, et} pour $\unsure{\varepsilon|\mathcal E|E}\in\mathrm{Drap}_2(\deleted{\unsure{I}}\mathcal L)$, de la décomp. de
% ink middle, C(\unsure{\varep
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: revised

Crop links: crops/015_middle.jpg

Alignment requires recheck: no flag

Review note: Rounded epsilon/E form is recorded consistently; the old exclusion symbol itself remains unresolved.

### C-015-U015 (C line 13)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 13.

Source C token:

```tex
\unsure{I}
```

Source C context:

```tex
sance\inserted{ de $\mathrm{Drap}_2(L)$, et} pour $\unsure{E|\mathcal E}\in\mathrm{Drap}_2(\deleted{\unsure{I}}L)$, de la \unsure{décomp.} de
% ink middle, C(E) and continuation
\[
 C(E)=\{\,t\in L\deleted{\uns
```

Aligned final span:

```tex
\unsure{I}
```

Final context (up to 100 characters either side):

```tex
mathrm{Drap}_2(\mathcal L)$, et} pour $\unsure{\varepsilon|\mathcal E|E}\in\mathrm{Drap}_2(\deleted{\unsure{I}}\mathcal L)$, de la décomp. de
% ink middle, C(\unsure{\varepsilon|\mathcal E|E}) and continuation

```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/015_middle.jpg

Alignment requires recheck: no flag

Review note: Old On va, letter before L, crossed x, cup/comma, old relation and terminal punctuation remain uncertain.

### C-015-U016 (C line 13)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 13.

Source C token:

```tex
\unsure{décomp.}
```

Source C context:

```tex
athrm{Drap}_2(L)$, et} pour $\unsure{E|\mathcal E}\in\mathrm{Drap}_2(\deleted{\unsure{I}}L)$, de la \unsure{décomp.} de
% ink middle, C(E) and continuation
\[
 C(E)=\{\,t\in L\deleted{\unsure{\notin E|\smallsetminus 
```

Aligned final span:

```tex
décomp.
```

Final context (up to 100 characters either side):

```tex
} pour $\unsure{\varepsilon|\mathcal E|E}\in\mathrm{Drap}_2(\deleted{\unsure{I}}\mathcal L)$, de la décomp. de
% ink middle, C(\unsure{\varepsilon|\mathcal E|E}) and continuation
\[
 C(\unsure{\varepsilon|\m
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/015_middle.jpg

Alignment requires recheck: no flag

Review note: Décomp. is legible and remains abbreviated.

### C-015-U017 (C line 16)

Mechanical state: **unsure token(s) overlap changed alignment; inspect**. Final aligned line: 16.

Source C token:

```tex
\unsure{\notin E|\smallsetminus E}
```

Source C context:

```tex
e{I}}L)$, de la \unsure{décomp.} de
% ink middle, C(E) and continuation
\[
 C(E)=\{\,t\in L\deleted{\unsure{\notin E|\smallsetminus E}}\mid
 \deleted{\unsure{x}}\{E\unsure{\cup|,}t\}\deleted{\unsure{=|-}}\in\mathrm{Drap}_3(L)\,\}
\]
e
```

Aligned final span:

```tex
\unsure{\notin\varepsilon|\smallsetminus\varepsilon}
```

Final context (up to 100 characters either side):

```tex
\mathcal E|E}) and continuation
\[
 C(\unsure{\varepsilon|\mathcal E|E})=\{\,t\in\mathcal L\deleted{\unsure{\notin\varepsilon|\smallsetminus\varepsilon}}\mid
 \deleted{\unsure{x}}\{\unsure{\varepsilon|\mathcal E|E}\unsure{\cup|,}t\}\deleted{\unsure{=|-
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: revised

Crop links: crops/015_middle.jpg

Alignment requires recheck: no flag

Review note: Rounded epsilon/E form is recorded consistently; the old exclusion symbol itself remains unresolved.

### C-015-U018 (C line 17)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 17.

Source C token:

```tex
\unsure{x}
```

Source C context:

```tex
C(E) and continuation
\[
 C(E)=\{\,t\in L\deleted{\unsure{\notin E|\smallsetminus E}}\mid
 \deleted{\unsure{x}}\{E\unsure{\cup|,}t\}\deleted{\unsure{=|-}}\in\mathrm{Drap}_3(L)\,\}
\]
en composantes connexes, im
```

Aligned final span:

```tex
\unsure{x}
```

Final context (up to 100 characters either side):

```tex
|E})=\{\,t\in\mathcal L\deleted{\unsure{\notin\varepsilon|\smallsetminus\varepsilon}}\mid
 \deleted{\unsure{x}}\{\unsure{\varepsilon|\mathcal E|E}\unsure{\cup|,}t\}\deleted{\unsure{=|-}}\in\mathrm{Drap}_3(\math
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/015_middle.jpg

Alignment requires recheck: no flag

Review note: Old On va, letter before L, crossed x, cup/comma, old relation and terminal punctuation remain uncertain.

### C-015-U019 (C line 17)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 17.

Source C token:

```tex
\unsure{\cup|,}
```

Source C context:

```tex
nuation
\[
 C(E)=\{\,t\in L\deleted{\unsure{\notin E|\smallsetminus E}}\mid
 \deleted{\unsure{x}}\{E\unsure{\cup|,}t\}\deleted{\unsure{=|-}}\in\mathrm{Drap}_3(L)\,\}
\]
en composantes connexes, implique la connaissa
```

Aligned final span:

```tex
\unsure{\cup|,}
```

Final context (up to 100 characters either side):

```tex
\varepsilon|\smallsetminus\varepsilon}}\mid
 \deleted{\unsure{x}}\{\unsure{\varepsilon|\mathcal E|E}\unsure{\cup|,}t\}\deleted{\unsure{=|-}}\in\mathrm{Drap}_3(\mathcal L)\,\}
\]
en composantes connexes, implique la 
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/015_middle.jpg

Alignment requires recheck: no flag

Review note: Old On va, letter before L, crossed x, cup/comma, old relation and terminal punctuation remain uncertain.

### C-015-U020 (C line 17)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 17.

Source C token:

```tex
\unsure{=|-}
```

Source C context:

```tex
\deleted{\unsure{\notin E|\smallsetminus E}}\mid
 \deleted{\unsure{x}}\{E\unsure{\cup|,}t\}\deleted{\unsure{=|-}}\in\mathrm{Drap}_3(L)\,\}
\]
en composantes connexes, implique la connaissance de la relation
\[
 R
```

Aligned final span:

```tex
\unsure{=|-}
```

Final context (up to 100 characters either side):

```tex
varepsilon}}\mid
 \deleted{\unsure{x}}\{\unsure{\varepsilon|\mathcal E|E}\unsure{\cup|,}t\}\deleted{\unsure{=|-}}\in\mathrm{Drap}_3(\mathcal L)\,\}
\]
en composantes connexes, implique la connaissance de la relat
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/015_middle.jpg

Alignment requires recheck: no flag

Review note: Old On va, letter before L, crossed x, cup/comma, old relation and terminal punctuation remain uncertain.

### C-015-U021 (C line 21)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 21.

Source C token:

```tex
\unsure{\mathord{:}|\mathord{?}}
```

Source C context:

```tex
thrm{Drap}_3(L)\,\}
\]
en composantes connexes, implique la connaissance de la relation
\[
 R(a,b,c)\unsure{\mathord{:}|\mathord{?}}\quad b\text{ strict entre }a\text{ et }c.
\]
% ink lower third, Première condition
\unsure{Première
```

Aligned final span:

```tex
\unsure{\mathord{:}|\mathord{?}}
```

Final context (up to 100 characters either side):

```tex
}_3(\mathcal L)\,\}
\]
en composantes connexes, implique la connaissance de la relation
\[
 R(a,b,c)\unsure{\mathord{:}|\mathord{?}}\quad b\text{ strict entre }a\text{ et }c.
\]
% ink lower third, Première condition
Première conditi
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/015_middle.jpg

Alignment requires recheck: no flag

Review note: Old On va, letter before L, crossed x, cup/comma, old relation and terminal punctuation remain uncertain.

### C-015-U022 (C line 24)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 24.

Source C token:

```tex
\unsure{Première}
```

Source C context:

```tex
{:}|\mathord{?}}\quad b\text{ strict entre }a\text{ et }c.
\]
% ink lower third, Première condition
\unsure{Première} condition : $\{a,b,c\}\in\mathrm{Drap}_3(L)$ (\unsure{résulte} de la donnée de $\mathrm{Drap}_2(L)$
```

Aligned final span:

```tex
Première
```

Final context (up to 100 characters either side):

```tex
{:}|\mathord{?}}\quad b\text{ strict entre }a\text{ et }c.
\]
% ink lower third, Première condition
Première condition : $\{a,b,c\}\in\mathrm{Drap}_3(\mathcal L)$ (résulte de la donnée de $\mathrm{Drap}_2(\ma
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/015_bottom.jpg

Alignment requires recheck: no flag

Review note: Première, résulte and the descending J in the cancelled final formula are visible.

### C-015-U023 (C line 24)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 24.

Source C token:

```tex
\unsure{résulte}
```

Source C context:

```tex
ink lower third, Première condition
\unsure{Première} condition : $\{a,b,c\}\in\mathrm{Drap}_3(L)$ (\unsure{résulte} de la donnée de $\mathrm{Drap}_2(L)$)
\figure{\begin{tikzpicture}[x=1cm,y=1cm,line cap=round]
\fill
```

Aligned final span:

```tex
résulte
```

Final context (up to 100 characters either side):

```tex
ink lower third, Première condition
Première condition : $\{a,b,c\}\in\mathrm{Drap}_3(\mathcal L)$ (résulte de la donnée de $\mathrm{Drap}_2(\mathcal L)$)
\figure{\begin{tikzpicture}[x=1cm,y=1cm,line cap=rou
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/015_bottom.jpg

Alignment requires recheck: no flag

Review note: Première, résulte and the descending J in the cancelled final formula are visible.

### C-015-U024 (C line 36)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 36.

Source C token:

```tex
\unsure{J|I}
```

Source C context:

```tex
ottom, final sentence and cancelled display
Si $b$ est entre $a$ et $c$, regardons les
\[
 \deleted{\unsure{J|I}_{abc}=\text{composante de }C(\{a,b\}}\unsure{,|)}
\]

```

Aligned final span:

```tex
J
```

Final context (up to 100 characters either side):

```tex
ottom, final sentence and cancelled display
Si $b$ est entre $a$ et $c$, regardons les
\[
 \deleted{J_{abc}=\text{composante de }C(\{a,b\}}\unsure{,|)}
\]

% pale vertical watermark
\rotatebox{90}{\tex
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/015_bottom.jpg

Alignment requires recheck: no flag

Review note: Première, résulte and the descending J in the cancelled final formula are visible.

### C-015-U025 (C line 36)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 36.

Source C token:

```tex
\unsure{,|)}
```

Source C context:

```tex
 est entre $a$ et $c$, regardons les
\[
 \deleted{\unsure{J|I}_{abc}=\text{composante de }C(\{a,b\}}\unsure{,|)}
\]

```

Aligned final span:

```tex
\unsure{,|)}
```

Final context (up to 100 characters either side):

```tex
play
Si $b$ est entre $a$ et $c$, regardons les
\[
 \deleted{J_{abc}=\text{composante de }C(\{a,b\}}\unsure{,|)}
\]

% pale vertical watermark
\rotatebox{90}{\textsc{\unsure{ng Extra Stro}}}

```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/015_bottom.jpg

Alignment requires recheck: no flag

Review note: Final small mark is comma-like but may be a closing parenthesis.

### C-016-U001 (C line 3)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 3.

Source C token:

```tex
\unsure{donné|donnée}
```

Source C context:

```tex
canpage{16}\mspage{15}
% ink top, heading of the three equalities
trois composantes (relatives à la \unsure{donné|donnée} de $\{a,b,c\}$)
\[
\begin{aligned}
\deleted{\unsure{C}}X_{\{a,b\}}&=\deleted{\unsure{C(a,b,c)}}=(\t
```

Aligned final span:

```tex
\unsure{donné|donnée}
```

Final context (up to 100 characters either side):

```tex
canpage{16}\mspage{15}
% ink top, heading of the three equalities
trois composantes (relatives à la \unsure{donné|donnée} de $\{a,b,c\}$)
\[
\begin{aligned}
\deleted{\unsure{C}}X_{\{a,b\}}&=\deleted{\unsure{C(a,b,c)}}=(\t
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/016_top.jpg

Alignment requires recheck: no flag

Review note: Donnée ending and crossed old C expressions/ground-set letter remain unresolved.

### C-016-U002 (C line 6)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 6.

Source C token:

```tex
\unsure{C}
```

Source C context:

```tex
trois composantes (relatives à la \unsure{donné|donnée} de $\{a,b,c\}$)
\[
\begin{aligned}
\deleted{\unsure{C}}X_{\{a,b\}}&=\deleted{\unsure{C(a,b,c)}}=(\text{comp. de }C(\{a,b\})\text{ contenant }c)=L_{>b}\\
X
```

Aligned final span:

```tex
\unsure{C}
```

Final context (up to 100 characters either side):

```tex
trois composantes (relatives à la \unsure{donné|donnée} de $\{a,b,c\}$)
\[
\begin{aligned}
\deleted{\unsure{C}}X_{\{a,b\}}&=\deleted{\unsure{C(a,b,c)}}=(\text{comp. de }C(\{a,b\})\text{ contenant }c)=\mathcal L
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/016_top.jpg

Alignment requires recheck: no flag

Review note: Donnée ending and crossed old C expressions/ground-set letter remain unresolved.

### C-016-U003 (C line 6)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 6.

Source C token:

```tex
\unsure{C(a,b,c)}
```

Source C context:

```tex
 \unsure{donné|donnée} de $\{a,b,c\}$)
\[
\begin{aligned}
\deleted{\unsure{C}}X_{\{a,b\}}&=\deleted{\unsure{C(a,b,c)}}=(\text{comp. de }C(\{a,b\})\text{ contenant }c)=L_{>b}\\
X_{\{b,c\}}\deleted{\unsure{C(b,c,a)}}&=(
```

Aligned final span:

```tex
\unsure{C(a,b,c)}
```

Final context (up to 100 characters either side):

```tex
 \unsure{donné|donnée} de $\{a,b,c\}$)
\[
\begin{aligned}
\deleted{\unsure{C}}X_{\{a,b\}}&=\deleted{\unsure{C(a,b,c)}}=(\text{comp. de }C(\{a,b\})\text{ contenant }c)=\mathcal L_{>b}\\
X_{\{b,c\}}\deleted{\unsure{C(b,
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/016_top.jpg

Alignment requires recheck: no flag

Review note: Donnée ending and crossed old C expressions/ground-set letter remain unresolved.

### C-016-U004 (C line 7)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 7.

Source C token:

```tex
\unsure{C(b,c,a)}
```

Source C context:

```tex
ted{\unsure{C(a,b,c)}}=(\text{comp. de }C(\{a,b\})\text{ contenant }c)=L_{>b}\\
X_{\{b,c\}}\deleted{\unsure{C(b,c,a)}}&=(\rule{1.45cm}{.4pt}\ C(\{b,c\})\ \rule{1.1cm}{.4pt}\ a)=L_{<b}\\
X_{\{c,a\}}\deleted{C(c,a,b)}&=
```

Aligned final span:

```tex
\unsure{C(b,c,a)}
```

Final context (up to 100 characters either side):

```tex
re{C(a,b,c)}}=(\text{comp. de }C(\{a,b\})\text{ contenant }c)=\mathcal L_{>b}\\
X_{\{b,c\}}\deleted{\unsure{C(b,c,a)}}&=(\rule{1.45cm}{.4pt}\ C(\{b,c\})\ \rule{1.1cm}{.4pt}\ a)=\mathcal L_{<b}\\
X_{\{c,a\}}\deleted{C(
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/016_top.jpg

Alignment requires recheck: no flag

Review note: Donnée ending and crossed old C expressions/ground-set letter remain unresolved.

### C-016-U005 (C line 8)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 8.

Source C token:

```tex
\unsure{\mathcal L}
```

Source C context:

```tex
b}\\
X_{\{c,a\}}\deleted{C(c,a,b)}&=\rule{1.2cm}{.4pt}\ C(\{c,a\})\ \rule{.85cm}{.4pt}\ b)=\deleted{\unsure{\mathcal L}}\mathopen{]}a,c\mathclose{[}
\end{aligned}
\]

% ink middle, On trouve and three intersections
On t
```

Aligned final span:

```tex
\unsure{\mathcal L}
```

Final context (up to 100 characters either side):

```tex
b}\\
X_{\{c,a\}}\deleted{C(c,a,b)}&=\rule{1.2cm}{.4pt}\ C(\{c,a\})\ \rule{.85cm}{.4pt}\ b)=\deleted{\unsure{\mathcal L}}\mathopen{]}a,c\mathclose{[}
\end{aligned}
\]

% ink middle, On trouve and three intersections
On t
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/016_top.jpg

Alignment requires recheck: no flag

Review note: Donnée ending and crossed old C expressions/ground-set letter remain unresolved.

### C-016-U006 (C line 16)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 16.

Source C token:

```tex
\unsure{c}
```

Source C context:

```tex
ddle, On trouve and three intersections
On trouve
\[
\begin{aligned}
&\deleted{C}X_{\{a,b\}\deleted{\unsure{c}}}\cap\deleted{C}X_{\{b,c\}\deleted{\unsure{a}}}=\varnothing\\
&\left.\begin{aligned}
&\deleted{C}X_
```

Aligned final span:

```tex
\unsure{c}
```

Final context (up to 100 characters either side):

```tex
ddle, On trouve and three intersections
On trouve
\[
\begin{aligned}
&\deleted{C}X_{\{a,b\}\deleted{\unsure{c}}}\cap\deleted{C}X_{\{b,c\}\deleted{\unsure{a}}}=\varnothing\\
&\left.\begin{aligned}
&\deleted{C}X_
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/016_middle.jpg

Alignment requires recheck: no flag

Review note: Small cancelled subscript letters and the b/c-shaped live index remain obscured.

### C-016-U007 (C line 16)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 16.

Source C token:

```tex
\unsure{a}
```

Source C context:

```tex
uve
\[
\begin{aligned}
&\deleted{C}X_{\{a,b\}\deleted{\unsure{c}}}\cap\deleted{C}X_{\{b,c\}\deleted{\unsure{a}}}=\varnothing\\
&\left.\begin{aligned}
&\deleted{C}X_{\{a,b\}\deleted{\unsure{c}}}\cap\deleted{C}X_
```

Aligned final span:

```tex
\unsure{a}
```

Final context (up to 100 characters either side):

```tex
uve
\[
\begin{aligned}
&\deleted{C}X_{\{a,b\}\deleted{\unsure{c}}}\cap\deleted{C}X_{\{b,c\}\deleted{\unsure{a}}}=\varnothing\\
&\left.\begin{aligned}
&\deleted{C}X_{\{a,b\}\deleted{\unsure{c}}}\cap\deleted{C}X_
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/016_middle.jpg

Alignment requires recheck: no flag

Review note: Small cancelled subscript letters and the b/c-shaped live index remain obscured.

### C-016-U008 (C line 18)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 18.

Source C token:

```tex
\unsure{c}
```

Source C context:

```tex
X_{\{b,c\}\deleted{\unsure{a}}}=\varnothing\\
&\left.\begin{aligned}
&\deleted{C}X_{\{a,b\}\deleted{\unsure{c}}}\cap\deleted{C}X_{\{c,\deleted{\unsure{b}}a\}\deleted{\unsure{b}}}=\mathopen{]}b,c\mathclose{[}\ne
```

Aligned final span:

```tex
\unsure{c}
```

Final context (up to 100 characters either side):

```tex
X_{\{b,c\}\deleted{\unsure{a}}}=\varnothing\\
&\left.\begin{aligned}
&\deleted{C}X_{\{a,b\}\deleted{\unsure{c}}}\cap\deleted{C}X_{\{c,\deleted{\unsure{b}}a\}\deleted{\unsure{b}}}=\mathopen{]}b,c\mathclose{[}\ne
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/016_middle.jpg

Alignment requires recheck: no flag

Review note: Small cancelled subscript letters and the b/c-shaped live index remain obscured.

### C-016-U009 (C line 18)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 18.

Source C token:

```tex
\unsure{b}
```

Source C context:

```tex
\\
&\left.\begin{aligned}
&\deleted{C}X_{\{a,b\}\deleted{\unsure{c}}}\cap\deleted{C}X_{\{c,\deleted{\unsure{b}}a\}\deleted{\unsure{b}}}=\mathopen{]}b,c\mathclose{[}\ne\varnothing\\
&X_{\unsure{(\,|\,\{}b,\unsur
```

Aligned final span:

```tex
\unsure{b}
```

Final context (up to 100 characters either side):

```tex
\\
&\left.\begin{aligned}
&\deleted{C}X_{\{a,b\}\deleted{\unsure{c}}}\cap\deleted{C}X_{\{c,\deleted{\unsure{b}}a\}\deleted{\unsure{b}}}=\mathopen{]}b,c\mathclose{[}\ne\varnothing\\
&X_{(b,\unsure{c|b}\}}\cap X_
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/016_middle.jpg

Alignment requires recheck: no flag

Review note: Small cancelled subscript letters and the b/c-shaped live index remain obscured.

### C-016-U010 (C line 18)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 18.

Source C token:

```tex
\unsure{b}
```

Source C context:

```tex
d}
&\deleted{C}X_{\{a,b\}\deleted{\unsure{c}}}\cap\deleted{C}X_{\{c,\deleted{\unsure{b}}a\}\deleted{\unsure{b}}}=\mathopen{]}b,c\mathclose{[}\ne\varnothing\\
&X_{\unsure{(\,|\,\{}b,\unsure{c|b}\}}\cap X_{\{c,a\
```

Aligned final span:

```tex
\unsure{b}
```

Final context (up to 100 characters either side):

```tex
d}
&\deleted{C}X_{\{a,b\}\deleted{\unsure{c}}}\cap\deleted{C}X_{\{c,\deleted{\unsure{b}}a\}\deleted{\unsure{b}}}=\mathopen{]}b,c\mathclose{[}\ne\varnothing\\
&X_{(b,\unsure{c|b}\}}\cap X_{\{c,a\}}=\mathopen{]}a
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/016_middle.jpg

Alignment requires recheck: no flag

Review note: Small cancelled subscript letters and the b/c-shaped live index remain obscured.

### C-016-U011 (C line 19)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 19.

Source C token:

```tex
\unsure{(\,|\,\{}
```

Source C context:

```tex
_{\{c,\deleted{\unsure{b}}a\}\deleted{\unsure{b}}}=\mathopen{]}b,c\mathclose{[}\ne\varnothing\\
&X_{\unsure{(\,|\,\{}b,\unsure{c|b}\}}\cap X_{\{c,a\}}=\mathopen{]}a,b\mathclose{[}\ne\varnothing
\end{aligned}\right\}
\
```

Aligned final span:

```tex
(
```

Final context (up to 100 characters either side):

```tex
_{\{c,\deleted{\unsure{b}}a\}\deleted{\unsure{b}}}=\mathopen{]}b,c\mathclose{[}\ne\varnothing\\
&X_{(b,\unsure{c|b}\}}\cap X_{\{c,a\}}=\mathopen{]}a,b\mathclose{[}\ne\varnothing
\end{aligned}\right\}
\
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/016_middle.jpg

Alignment requires recheck: no flag

Review note: The first subscript delimiter is a curved opening parenthesis, followed by a closing brace as written.

### C-016-U012 (C line 19)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 19.

Source C token:

```tex
\unsure{c|b}
```

Source C context:

```tex
ure{b}}a\}\deleted{\unsure{b}}}=\mathopen{]}b,c\mathclose{[}\ne\varnothing\\
&X_{\unsure{(\,|\,\{}b,\unsure{c|b}\}}\cap X_{\{c,a\}}=\mathopen{]}a,b\mathclose{[}\ne\varnothing
\end{aligned}\right\}
\end{aligned}
\
```

Aligned final span:

```tex
\unsure{c|b}
```

Final context (up to 100 characters either side):

```tex
{c,\deleted{\unsure{b}}a\}\deleted{\unsure{b}}}=\mathopen{]}b,c\mathclose{[}\ne\varnothing\\
&X_{(b,\unsure{c|b}\}}\cap X_{\{c,a\}}=\mathopen{]}a,b\mathclose{[}\ne\varnothing
\end{aligned}\right\}
\end{aligned}
\
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/016_middle.jpg

Alignment requires recheck: no flag

Review note: Small cancelled subscript letters and the b/c-shaped live index remain obscured.

### C-016-U013 (C line 26)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 26.

Source C token:

```tex
\unsure{parties}
```

Source C context:

```tex
dle, donc b
donc $b$ est distingué, dans $J=\{a,b,c\}$, par la propriété que pour les deux \deleted{\unsure{parties}} ${\unsure{E|\mathcal E|\varepsilon}}',E'$ \deleted{de} $\in\unsure{\mathrm P|\mathscr P}_2(J)$ qui
```

Aligned final span:

```tex
parties
```

Final context (up to 100 characters either side):

```tex
dle, donc b
donc $b$ est distingué, dans $J=\{a,b,c\}$, par la propriété que pour les deux \deleted{parties} ${\unsure{\varepsilon|\mathcal E|E}}',\unsure{\varepsilon|\mathcal E|E}'$ \deleted{de} $\in\unsure
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/016_bottom.jpg

Alignment requires recheck: no flag

Review note: The crossed word parties is readable.

### C-016-U014 (C line 26)

Mechanical state: **unsure token(s) overlap changed alignment; inspect**. Final aligned line: 26.

Source C token:

```tex
\unsure{E|\mathcal E|\varepsilon}
```

Source C context:

```tex
 est distingué, dans $J=\{a,b,c\}$, par la propriété que pour les deux \deleted{\unsure{parties}} ${\unsure{E|\mathcal E|\varepsilon}}',E'$ \deleted{de} $\in\unsure{\mathrm P|\mathscr P}_2(J)$ qui le \unsure{contient|contiennent}, on
```

Aligned final span:

```tex
\unsure{\varepsilon|\mathcal E|E}}',\unsure{\varepsilon|\mathcal E|E}
```

Final context (up to 100 characters either side):

```tex

donc $b$ est distingué, dans $J=\{a,b,c\}$, par la propriété que pour les deux \deleted{parties} ${\unsure{\varepsilon|\mathcal E|E}}',\unsure{\varepsilon|\mathcal E|E}'$ \deleted{de} $\in\unsure{P|\mathscr P|\mathfrak P}_2(J)$ qui le \unsure{contient|contiennent}, on
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: revised

Crop links: crops/016_bottom.jpg

Alignment requires recheck: no flag

Review note: Epsilon/E and P alphabet alternatives remain local doubts; both prose epsilon signs visibly carry primes, and the first final subscript has a small unresolved 0/comma mark.

### C-016-U015 (C line 26)

Mechanical state: **unsure token(s) overlap changed alignment; inspect**. Final aligned line: 26.

Source C token:

```tex
\unsure{\mathrm P|\mathscr P}
```

Source C context:

```tex
pour les deux \deleted{\unsure{parties}} ${\unsure{E|\mathcal E|\varepsilon}}',E'$ \deleted{de} $\in\unsure{\mathrm P|\mathscr P}_2(J)$ qui le \unsure{contient|contiennent}, on a
\[
 X_{\unsure{E_{0}|E_{,}|E}}\unsure{\wedge|\cap}
```

Aligned final span:

```tex
\unsure{P|\mathscr P|\mathfrak P}
```

Final context (up to 100 characters either side):

```tex
parties} ${\unsure{\varepsilon|\mathcal E|E}}',\unsure{\varepsilon|\mathcal E|E}'$ \deleted{de} $\in\unsure{P|\mathscr P|\mathfrak P}_2(J)$ qui le \unsure{contient|contiennent}, on a
\[
 X_{\unsure{\varepsilon_{0}|\varepsilon_{,}|\va
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: revised

Crop links: crops/016_bottom.jpg

Alignment requires recheck: no flag

Review note: Epsilon/E and P alphabet alternatives remain local doubts; both prose epsilon signs visibly carry primes, and the first final subscript has a small unresolved 0/comma mark.

### C-016-U016 (C line 26)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 26.

Source C token:

```tex
\unsure{contient|contiennent}
```

Source C context:

```tex
\unsure{E|\mathcal E|\varepsilon}}',E'$ \deleted{de} $\in\unsure{\mathrm P|\mathscr P}_2(J)$ qui le \unsure{contient|contiennent}, on a
\[
 X_{\unsure{E_{0}|E_{,}|E}}\unsure{\wedge|\cap}X_{E'}=\varnothing\,.\qquad\text{On gagne !
```

Aligned final span:

```tex
\unsure{contient|contiennent}
```

Final context (up to 100 characters either side):

```tex
\unsure{\varepsilon|\mathcal E|E}'$ \deleted{de} $\in\unsure{P|\mathscr P|\mathfrak P}_2(J)$ qui le \unsure{contient|contiennent}, on a
\[
 X_{\unsure{\varepsilon_{0}|\varepsilon_{,}|\varepsilon}}\wedge X_{\unsure{\varepsilon|\ma
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/016_bottom.jpg

Alignment requires recheck: no flag

Review note: The terminal verb ending does not settle contient/contiennent.

### C-016-U017 (C line 28)

Mechanical state: **unsure token(s) overlap changed alignment; inspect**. Final aligned line: 28.

Source C token:

```tex
\unsure{E_{0}|E_{,}|E}
```

Source C context:

```tex
leted{de} $\in\unsure{\mathrm P|\mathscr P}_2(J)$ qui le \unsure{contient|contiennent}, on a
\[
 X_{\unsure{E_{0}|E_{,}|E}}\unsure{\wedge|\cap}X_{E'}=\varnothing\,.\qquad\text{On gagne !}
\]

% ink bottom, NB
\uline{NB} On
```

Aligned final span:

```tex
\unsure{\varepsilon_{0}|\varepsilon_{,}|\varepsilon}
```

Final context (up to 100 characters either side):

```tex
d{de} $\in\unsure{P|\mathscr P|\mathfrak P}_2(J)$ qui le \unsure{contient|contiennent}, on a
\[
 X_{\unsure{\varepsilon_{0}|\varepsilon_{,}|\varepsilon}}\wedge X_{\unsure{\varepsilon|\mathcal E|E}'}=\varnothing\,.\qquad\text{On gagne !}
\]

% ink botto
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: revised

Crop links: crops/016_bottom.jpg

Alignment requires recheck: no flag

Review note: Epsilon/E and P alphabet alternatives remain local doubts; both prose epsilon signs visibly carry primes, and the first final subscript has a small unresolved 0/comma mark.

### C-016-U018 (C line 28)

Mechanical state: **unsure token(s) overlap changed alignment; inspect**. Final aligned line: 28.

Source C token:

```tex
\unsure{\wedge|\cap}
```

Source C context:

```tex
mathrm P|\mathscr P}_2(J)$ qui le \unsure{contient|contiennent}, on a
\[
 X_{\unsure{E_{0}|E_{,}|E}}\unsure{\wedge|\cap}X_{E'}=\varnothing\,.\qquad\text{On gagne !}
\]

% ink bottom, NB
\uline{NB} On a à nouveau utilisé 
```

Aligned final span:

```tex
\wedge X_{\unsure{\varepsilon|\mathcal E|E}
```

Final context (up to 100 characters either side):

```tex
 le \unsure{contient|contiennent}, on a
\[
 X_{\unsure{\varepsilon_{0}|\varepsilon_{,}|\varepsilon}}\wedge X_{\unsure{\varepsilon|\mathcal E|E}'}=\varnothing\,.\qquad\text{On gagne !}
\]

% ink bottom, NB
\uline{NB} On a à nouveau utilisé la d
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/016_intersection.jpg

Alignment requires recheck: no flag

Review note: The final operator has a pointed apex, so wedge is retained rather than rounded intersection. Alignment recheck: A TeX command delimiter space was added after wedge; the reviewed pointed operator remains unchanged.

### C-017-U001 (C line 3)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 3.

Source C token:

```tex
\unsure{Considér|Considé}
```

Source C context:

```tex
\scanpage{17}\mspage{16}
% ink heading and first remark
\uline{Remarques} \textcircled{1} \deleted{\unsure{Considér|Considé}} sur la notion de tronçon. On cherche une sous-cat. pleine \inserted{$\unsure{\mathscr T|\mathcal T
```

Aligned final span:

```tex
\unsure{Considér|Considé}
```

Final context (up to 100 characters either side):

```tex
\scanpage{17}\mspage{16}
% ink heading and first remark
\uline{Remarques} \textcircled{1} \deleted{\unsure{Considér|Considé}} sur la notion de tronçon. On cherche une sous-cat. pleine \inserted{$\mathscr T$} de celle des ens
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/017_top.jpg

Alignment requires recheck: no flag

Review note: Cancelled short Considér/Considé remains incomplete.

### C-017-U002 (C line 3)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 3.

Source C token:

```tex
\unsure{\mathscr T|\mathcal T}
```

Source C context:

```tex
ted{\unsure{Considér|Considé}} sur la notion de tronçon. On cherche une sous-cat. pleine \inserted{$\unsure{\mathscr T|\mathcal T}$} de celle des ens. ordonnés, satisfaisant

% ink item a, two lines and qualification at the right

```

Aligned final span:

```tex
\mathscr T
```

Final context (up to 100 characters either side):

```tex
ted{\unsure{Considér|Considé}} sur la notion de tronçon. On cherche une sous-cat. pleine \inserted{$\mathscr T$} de celle des ens. ordonnés, satisfaisant

% ink item a, two lines and qualification at the right

```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/017_top.jpg

Alignment requires recheck: no flag

Review note: Long curved top and looped descent identify the recurring script category T.

### C-017-U003 (C line 6)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 6.

Source C token:

```tex
\unsure{S}
```

Source C context:

```tex
des ens. ordonnés, satisfaisant

% ink item a, two lines and qualification at the right
a) \deleted{\unsure{S}}Tout $\mathcal L\in\mathrm{Ob}\,\mathscr T$ est filtrant croissant et filtrant décroissant, et \del
```

Aligned final span:

```tex
\unsure{S}
```

Final context (up to 100 characters either side):

```tex
des ens. ordonnés, satisfaisant

% ink item a, two lines and qualification at the right
a) \deleted{\unsure{S}}Tout $\mathcal L\in\mathrm{Ob}\,\mathscr T$ est filtrant croissant et filtrant décroissant, et \del
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/017_a.jpg

Alignment requires recheck: no flag

Review note: Old initial letter beneath Tout remains obscured.

### C-017-U004 (C line 9)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 9.

Source C token:

```tex
\unsure{T}
```

Source C context:

```tex
\deleted{non vide} \inserted{de cardinal $\ne1$} (donc $\geq2$)

% ink item b
b) Si $x,y\in\deleted{\unsure{T}}\mathcal L_{\deleted{\unsure{,|g}}}\in\deleted{\unsure{O}}\mathrm{Ob}\,\mathscr T$, et $x<y$, $\exi
```

Aligned final span:

```tex
\unsure{T}
```

Final context (up to 100 characters either side):

```tex
\deleted{non vide} \inserted{de cardinal $\ne1$} (donc $\geq2$)

% ink item b
b) Si $x,y\in\deleted{\unsure{T}}\mathcal L_{\deleted{\unsure{,|g}}}\in\deleted{\unsure{O}}\mathrm{Ob}\,\mathscr T$, et $x<y$, $\exi
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/017_bc.jpg

Alignment requires recheck: no flag

Review note: Old T, trailing lower mark, old O and angular Ob/D form remain ambiguous.

### C-017-U005 (C line 9)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 9.

Source C token:

```tex
\unsure{,|g}
```

Source C context:

```tex
cardinal $\ne1$} (donc $\geq2$)

% ink item b
b) Si $x,y\in\deleted{\unsure{T}}\mathcal L_{\deleted{\unsure{,|g}}}\in\deleted{\unsure{O}}\mathrm{Ob}\,\mathscr T$, et $x<y$, $\exists$
\[
 z\in L,\qquad x<z<y\qquad
```

Aligned final span:

```tex
\unsure{,|g}
```

Final context (up to 100 characters either side):

```tex
cardinal $\ne1$} (donc $\geq2$)

% ink item b
b) Si $x,y\in\deleted{\unsure{T}}\mathcal L_{\deleted{\unsure{,|g}}}\in\deleted{\unsure{O}}\mathrm{Ob}\,\mathscr T$, et $x<y$, $\exists$
\[
 z\in\mathcal L,\qquad x<z
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/017_bc.jpg

Alignment requires recheck: no flag

Review note: Old T, trailing lower mark, old O and angular Ob/D form remain ambiguous.

### C-017-U006 (C line 9)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 9.

Source C token:

```tex
\unsure{O}
```

Source C context:

```tex
eq2$)

% ink item b
b) Si $x,y\in\deleted{\unsure{T}}\mathcal L_{\deleted{\unsure{,|g}}}\in\deleted{\unsure{O}}\mathrm{Ob}\,\mathscr T$, et $x<y$, $\exists$
\[
 z\in L,\qquad x<z<y\qquad\text{(divisibilité)}
\]
```

Aligned final span:

```tex
\unsure{O}
```

Final context (up to 100 characters either side):

```tex
eq2$)

% ink item b
b) Si $x,y\in\deleted{\unsure{T}}\mathcal L_{\deleted{\unsure{,|g}}}\in\deleted{\unsure{O}}\mathrm{Ob}\,\mathscr T$, et $x<y$, $\exists$
\[
 z\in\mathcal L,\qquad x<z<y\qquad\text{(divisibil
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/017_bc.jpg

Alignment requires recheck: no flag

Review note: Old T, trailing lower mark, old O and angular Ob/D form remain ambiguous.

### C-017-U007 (C line 15)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 15.

Source C token:

```tex
\unsure{\mathrm{Ob}|\mathrm D}
```

Source C context:

```tex
x<y$, $\exists$
\[
 z\in L,\qquad x<z<y\qquad\text{(divisibilité)}
\]

% ink item c
c) Si $x\in L\in\unsure{\mathrm{Ob}|\mathrm D}\,\mathscr T$, \deleted{alors} et si
\[
 L_{>x}\ne\varnothing,\quad\text{alors}\quad L_{>x}\in\mathr
```

Aligned final span:

```tex
\unsure{\mathrm{Ob}|\mathrm D}
```

Final context (up to 100 characters either side):

```tex
\[
 z\in\mathcal L,\qquad x<z<y\qquad\text{(divisibilité)}
\]

% ink item c
c) Si $x\in\mathcal L\in\unsure{\mathrm{Ob}|\mathrm D}\,\mathscr T$, \deleted{alors} et si
\[
 \mathcal L_{>x}\ne\varnothing,\quad\text{alors}\quad \mathc
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/017_bc.jpg

Alignment requires recheck: no flag

Review note: Old T, trailing lower mark, old O and angular Ob/D form remain ambiguous.

### C-017-U008 (C line 24)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 24.

Source C token:

```tex
\unsure{ordonnés}
```

Source C context:

```tex
 $\mathscr T$ est stable par passage à l'ordre opposé. Les objets de $\mathscr T$ sont les tronçons \unsure{ordonnés}.

% ink bottom, second remark
\textcircled{2} Il faudrait expliciter \unsure{quelle|quelles} \unsur
```

Aligned final span:

```tex
ordonnés
```

Final context (up to 100 characters either side):

```tex
 $\mathscr T$ est stable par passage à l'ordre opposé. Les objets de $\mathscr T$ sont les tronçons ordonnés.

% ink bottom, second remark
\textcircled{2} Il faudrait expliciter \unsure{quelle|quelles} \unsur
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/017_claim.jpg

Alignment requires recheck: no flag

Review note: Ordonnés has a visible accented ending and final tail.

### C-017-U009 (C line 27)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 27.

Source C token:

```tex
\unsure{quelle|quelles}
```

Source C context:

```tex
les tronçons \unsure{ordonnés}.

% ink bottom, second remark
\textcircled{2} Il faudrait expliciter \unsure{quelle|quelles} \unsure{condition|conditions} la relation $R(a,b,c)$ doit satisfaire, pour définir une structure de
```

Aligned final span:

```tex
\unsure{quelle|quelles}
```

Final context (up to 100 characters either side):

```tex
 T$ sont les tronçons ordonnés.

% ink bottom, second remark
\textcircled{2} Il faudrait expliciter \unsure{quelle|quelles} \unsure{condition|conditions} la relation $R(a,b,c)$ doit satisfaire, pour définir une structure de
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/017_bottom.jpg

Alignment requires recheck: no flag

Review note: Clipped adjective/noun endings and two tiny comma marks remain unresolved.

### C-017-U010 (C line 27)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 27.

Source C token:

```tex
\unsure{condition|conditions}
```

Source C context:

```tex
onnés}.

% ink bottom, second remark
\textcircled{2} Il faudrait expliciter \unsure{quelle|quelles} \unsure{condition|conditions} la relation $R(a,b,c)$ doit satisfaire, pour définir une structure de tronçon \unsure{biordonné|bio
```

Aligned final span:

```tex
\unsure{condition|conditions}
```

Final context (up to 100 characters either side):

```tex
donnés.

% ink bottom, second remark
\textcircled{2} Il faudrait expliciter \unsure{quelle|quelles} \unsure{condition|conditions} la relation $R(a,b,c)$ doit satisfaire, pour définir une structure de \unsure{\deleted{tr.}}tronçon
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/017_bottom.jpg

Alignment requires recheck: no flag

Review note: Clipped adjective/noun endings and two tiny comma marks remain unresolved.

### C-017-U011 (C line 27)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 27.

Source C token:

```tex
\unsure{biordonné|biordonnien}
```

Source C context:

```tex
condition|conditions} la relation $R(a,b,c)$ doit satisfaire, pour définir une structure de tronçon \unsure{biordonné|biordonnien}\unsure{,} et itou pour la donnée de $\unsure{\mathscr S|S}_0\subset\unsure{\mathrm P|\mathscr P}_2(
```

Aligned final span:

```tex
\unsure{biordonné|biordonnien}
```

Final context (up to 100 characters either side):

```tex
la relation $R(a,b,c)$ doit satisfaire, pour définir une structure de \unsure{\deleted{tr.}}tronçon \unsure{biordonné|biordonnien}\unsure{,} et itou pour la donnée de $S_0\subset\unsure{P|\mathscr P|\mathfrak P}_2(\mathcal L)$ et 
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/017_bottom.jpg

Alignment requires recheck: no flag

Review note: Clipped adjective/noun endings and two tiny comma marks remain unresolved.

### C-017-U012 (C line 27)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 27.

Source C token:

```tex
\unsure{,}
```

Source C context:

```tex
ion $R(a,b,c)$ doit satisfaire, pour définir une structure de tronçon \unsure{biordonné|biordonnien}\unsure{,} et itou pour la donnée de $\unsure{\mathscr S|S}_0\subset\unsure{\mathrm P|\mathscr P}_2(L)$ et les
```

Aligned final span:

```tex
\unsure{,}
```

Final context (up to 100 characters either side):

```tex
tisfaire, pour définir une structure de \unsure{\deleted{tr.}}tronçon \unsure{biordonné|biordonnien}\unsure{,} et itou pour la donnée de $S_0\subset\unsure{P|\mathscr P|\mathfrak P}_2(\mathcal L)$ et les $R_{\u
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/017_bottom.jpg

Alignment requires recheck: no flag

Review note: Clipped adjective/noun endings and two tiny comma marks remain unresolved.

### C-017-U013 (C line 27)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 27.

Source C token:

```tex
\unsure{\mathscr S|S}
```

Source C context:

```tex
éfinir une structure de tronçon \unsure{biordonné|biordonnien}\unsure{,} et itou pour la donnée de $\unsure{\mathscr S|S}_0\subset\unsure{\mathrm P|\mathscr P}_2(L)$ et les $R_{\unsure{E|\mathcal E}}$\unsure{,} ($E\in\mat
```

Aligned final span:

```tex
S
```

Final context (up to 100 characters either side):

```tex
e \unsure{\deleted{tr.}}tronçon \unsure{biordonné|biordonnien}\unsure{,} et itou pour la donnée de $S_0\subset\unsure{P|\mathscr P|\mathfrak P}_2(\mathcal L)$ et les $R_{\unsure{\varepsilon|\mathcal E|
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/017_bottom.jpg

Alignment requires recheck: no flag

Review note: Both S₀ signs use the ordinary rounded S form.

### C-017-U014 (C line 27)

Mechanical state: **unsure token(s) overlap changed alignment; inspect**. Final aligned line: 27.

Source C token:

```tex
\unsure{\mathrm P|\mathscr P}
```

Source C context:

```tex
n \unsure{biordonné|biordonnien}\unsure{,} et itou pour la donnée de $\unsure{\mathscr S|S}_0\subset\unsure{\mathrm P|\mathscr P}_2(L)$ et les $R_{\unsure{E|\mathcal E}}$\unsure{,} ($E\in\mathscr S_0$) sur les $C(E)$ \ldots

```

Aligned final span:

```tex
\unsure{P|\mathscr P|\mathfrak P}
```

Final context (up to 100 characters either side):

```tex
\deleted{tr.}}tronçon \unsure{biordonné|biordonnien}\unsure{,} et itou pour la donnée de $S_0\subset\unsure{P|\mathscr P|\mathfrak P}_2(\mathcal L)$ et les $R_{\unsure{\varepsilon|\mathcal E|E}}$\unsure{,} ($\unsure{\varepsilon|\math
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: revised

Crop links: crops/017_bottom.jpg

Alignment requires recheck: no flag

Review note: P alphabet remains uncertain and pair sign uses epsilon/E alternatives, consistently across its three occurrences.

### C-017-U015 (C line 27)

Mechanical state: **unsure token(s) overlap changed alignment; inspect**. Final aligned line: 27.

Source C token:

```tex
\unsure{E|\mathcal E}
```

Source C context:

```tex
tou pour la donnée de $\unsure{\mathscr S|S}_0\subset\unsure{\mathrm P|\mathscr P}_2(L)$ et les $R_{\unsure{E|\mathcal E}}$\unsure{,} ($E\in\mathscr S_0$) sur les $C(E)$ \ldots

```

Aligned final span:

```tex
\unsure{\varepsilon|\mathcal E|E}
```

Final context (up to 100 characters either side):

```tex
,} et itou pour la donnée de $S_0\subset\unsure{P|\mathscr P|\mathfrak P}_2(\mathcal L)$ et les $R_{\unsure{\varepsilon|\mathcal E|E}}$\unsure{,} ($\unsure{\varepsilon|\mathcal E|E}\in S_0$) sur les $C(\unsure{\varepsilon|\mathcal E|
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: revised

Crop links: crops/017_bottom.jpg

Alignment requires recheck: no flag

Review note: P alphabet remains uncertain and pair sign uses epsilon/E alternatives, consistently across its three occurrences.

### C-017-U016 (C line 27)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 27.

Source C token:

```tex
\unsure{,}
```

Source C context:

```tex
\unsure{\mathscr S|S}_0\subset\unsure{\mathrm P|\mathscr P}_2(L)$ et les $R_{\unsure{E|\mathcal E}}$\unsure{,} ($E\in\mathscr S_0$) sur les $C(E)$ \ldots

```

Aligned final span:

```tex
\unsure{,}
```

Final context (up to 100 characters either side):

```tex
ubset\unsure{P|\mathscr P|\mathfrak P}_2(\mathcal L)$ et les $R_{\unsure{\varepsilon|\mathcal E|E}}$\unsure{,} ($\unsure{\varepsilon|\mathcal E|E}\in S_0$) sur les $C(\unsure{\varepsilon|\mathcal E|E})$ \ldots

```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/017_bottom.jpg

Alignment requires recheck: no flag

Review note: Clipped adjective/noun endings and two tiny comma marks remain unresolved.

### C-018-U001 (C line 3)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 2.

Source C token:

```tex
\unsure{L|\mathscr{L}}
```

Source C context:

```tex
-3}
\scanpage{18}\mspage{17}
Sous tronçon \deleted{\illegible{1}}\inserted{fermé $I$} d'un tronçon $\unsure{L|\mathscr{L}}$ : sous ens. de la forme $[a,b]$ (avec $a<b$) ou $L_{\leq a}$ (avec $a$ pas le plus petit élément) 
```

Aligned final span:

```tex
\mathcal L
```

Final context (up to 100 characters either side):

```tex
\scanpage{18}\mspage{17}
Sous tronçon \deleted{\illegible{1}}\inserted{fermé $I$} d'un tronçon $\mathcal L$ : sous ens. de la forme $[a,b]$ (avec $a<b$) ou $L_{\leq a}$ (avec $a$ pas le plus petit élément) 
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/018_top.jpg

Alignment requires recheck: no flag

Review note: Looped initial L and full tronçons are visible.

### C-018-U002 (C line 3)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 2.

Source C token:

```tex
\unsure{b}
```

Source C context:

```tex
forme $[a,b]$ (avec $a<b$) ou $L_{\leq a}$ (avec $a$ pas le plus petit élément) ou $L_{\geq\deleted{\unsure{b}}a}$ (avec $b$ pas un plus grand élément), \inserted{ou $L$} : ce sont donc des \unsure{tronçons}, p
```

Aligned final span:

```tex
\unsure{b}
```

Final context (up to 100 characters either side):

```tex
forme $[a,b]$ (avec $a<b$) ou $L_{\leq a}$ (avec $a$ pas le plus petit élément) ou $L_{\geq\deleted{\unsure{b}}a}$ (avec $b$ pas un plus grand élément), \inserted{ou $L$} : ce sont donc des tronçons, pour la st
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/018_top.jpg

Alignment requires recheck: no flag

Review note: Old b under the replacement a remains overwritten.

### C-018-U003 (C line 3)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 2.

Source C token:

```tex
\unsure{tronçons}
```

Source C context:

```tex
q\deleted{\unsure{b}}a}$ (avec $b$ pas un plus grand élément), \inserted{ou $L$} : ce sont donc des \unsure{tronçons}, pour la structure de \unsure{biordre|biordonnés|bi-ordre} induite.
\inserted{On a $\partial I=\{a,
```

Aligned final span:

```tex
tronçons
```

Final context (up to 100 characters either side):

```tex
q\deleted{\unsure{b}}a}$ (avec $b$ pas un plus grand élément), \inserted{ou $L$} : ce sont donc des tronçons, pour la structure de \unsure{biordre|biordonnien|biordonnés|bi-ordre} induite.
\inserted{On a $\pa
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/018_top.jpg

Alignment requires recheck: no flag

Review note: Looped initial L and full tronçons are visible.

### C-018-U004 (C line 3)

Mechanical state: **unsure token(s) overlap changed alignment; inspect**. Final aligned line: 2.

Source C token:

```tex
\unsure{biordre|biordonnés|bi-ordre}
```

Source C context:

```tex
n plus grand élément), \inserted{ou $L$} : ce sont donc des \unsure{tronçons}, pour la structure de \unsure{biordre|biordonnés|bi-ordre} induite.
\inserted{On a $\partial I=\{a,b\}$ resp $\{a\}$ resp. $\{b\}$, resp $\emptyset$}
% slante
```

Aligned final span:

```tex
\unsure{biordre|biordonnien|biordonnés|bi-ordre}
```

Final context (up to 100 characters either side):

```tex
$b$ pas un plus grand élément), \inserted{ou $L$} : ce sont donc des tronçons, pour la structure de \unsure{biordre|biordonnien|biordonnés|bi-ordre} induite.
\inserted{On a $\partial I=\{a,b\}$ resp $\{a\}$ resp. $\{b\}$, resp $\emptyset$}
% slante
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: revised

Crop links: crops/018_biordre.jpg

Alignment requires recheck: no flag

Review note: Compressed biord- ending may include onnien; the added alternative records the visible uncertainty rather than expected terminology.

### C-018-U005 (C line 6)

Mechanical state: **unsure token(s) overlap changed alignment; inspect**. Final aligned line: 5.

Source C token:

```tex
\unsure{de|abs}
```

Source C context:

```tex
nted
\margin{Attention il s'agit de frontière \uline{relative} de $I$ dans $L$, et non du bord abs, \unsure{de|abs} $I$.}
\deleted{Donc \unsure{deux} Deux} Deux sous-tronçons fermés sont \deleted{\unsure{disjts|disj
```

Aligned final span:

```tex
\unsure{d'|de}
```

Final context (up to 100 characters either side):

```tex
nted
\margin{Attention il s'agit de frontière \uline{relative} de $I$ dans $L$, et non du bord abs, \unsure{d'|de} $I$.}
\deleted{Donc deux Deux} Deux sous-tronçons fermés sont \deleted{\unsure{disjts|disj.}} en po
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: revised

Crop links: crops/018_margin1_full.jpg

Alignment requires recheck: no flag

Review note: The short group after bord abs is d-prime/de-shaped, not a second abs; ambiguity remains.

### C-018-U006 (C line 7)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 6.

Source C token:

```tex
\unsure{deux}
```

Source C context:

```tex
frontière \uline{relative} de $I$ dans $L$, et non du bord abs, \unsure{de|abs} $I$.}
\deleted{Donc \unsure{deux} Deux} Deux sous-tronçons fermés sont \deleted{\unsure{disjts|disj.}} en pos. rel. modérée si leurs 
```

Aligned final span:

```tex
deux
```

Final context (up to 100 characters either side):

```tex
 frontière \uline{relative} de $I$ dans $L$, et non du bord abs, \unsure{d'|de} $I$.}
\deleted{Donc deux Deux} Deux sous-tronçons fermés sont \deleted{\unsure{disjts|disj.}} en pos. rel. modérée si leurs 
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/018_rel.jpg

Alignment requires recheck: no flag

Review note: Crossed deux, tt, point, en and later lieu are distinguishable.

### C-018-U007 (C line 7)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 6.

Source C token:

```tex
\unsure{disjts|disj.}
```

Source C context:

```tex
bs, \unsure{de|abs} $I$.}
\deleted{Donc \unsure{deux} Deux} Deux sous-tronçons fermés sont \deleted{\unsure{disjts|disj.}} en pos. rel. modérée si leurs frontières le sont, i.e. si \unsure{tt|les} \deleted{\unsure{él}} \u
```

Aligned final span:

```tex
\unsure{disjts|disj.}
```

Final context (up to 100 characters either side):

```tex
 du bord abs, \unsure{d'|de} $I$.}
\deleted{Donc deux Deux} Deux sous-tronçons fermés sont \deleted{\unsure{disjts|disj.}} en pos. rel. modérée si leurs frontières le sont, i.e. si tt \deleted{\unsure{él}} point frontière
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/018_rel.jpg

Alignment requires recheck: no flag

Review note: Crossed abbreviation and old él remain uncertain.

### C-018-U008 (C line 7)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 6.

Source C token:

```tex
\unsure{tt|les}
```

Source C context:

```tex
rmés sont \deleted{\unsure{disjts|disj.}} en pos. rel. modérée si leurs frontières le sont, i.e. si \unsure{tt|les} \deleted{\unsure{él}} \unsure{point|lieu} frontière de l'un est \unsure{en} pos. rel. modérée à tt 
```

Aligned final span:

```tex
tt
```

Final context (up to 100 characters either side):

```tex
rmés sont \deleted{\unsure{disjts|disj.}} en pos. rel. modérée si leurs frontières le sont, i.e. si tt \deleted{\unsure{él}} point frontière de l'un est en pos. rel. modérée à tt lieu frontière de l'aut
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/018_rel.jpg

Alignment requires recheck: no flag

Review note: Crossed deux, tt, point, en and later lieu are distinguishable.

### C-018-U009 (C line 7)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 6.

Source C token:

```tex
\unsure{él}
```

Source C context:

```tex
e{disjts|disj.}} en pos. rel. modérée si leurs frontières le sont, i.e. si \unsure{tt|les} \deleted{\unsure{él}} \unsure{point|lieu} frontière de l'un est \unsure{en} pos. rel. modérée à tt \unsure{lieu|point} f
```

Aligned final span:

```tex
\unsure{él}
```

Final context (up to 100 characters either side):

```tex
eleted{\unsure{disjts|disj.}} en pos. rel. modérée si leurs frontières le sont, i.e. si tt \deleted{\unsure{él}} point frontière de l'un est en pos. rel. modérée à tt lieu frontière de l'autre.
\inserted{Sous-tr
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/018_rel.jpg

Alignment requires recheck: no flag

Review note: Crossed abbreviation and old él remain uncertain.

### C-018-U010 (C line 7)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 6.

Source C token:

```tex
\unsure{point|lieu}
```

Source C context:

```tex
.}} en pos. rel. modérée si leurs frontières le sont, i.e. si \unsure{tt|les} \deleted{\unsure{él}} \unsure{point|lieu} frontière de l'un est \unsure{en} pos. rel. modérée à tt \unsure{lieu|point} frontière de l'autre.

```

Aligned final span:

```tex
point
```

Final context (up to 100 characters either side):

```tex
e{disjts|disj.}} en pos. rel. modérée si leurs frontières le sont, i.e. si tt \deleted{\unsure{él}} point frontière de l'un est en pos. rel. modérée à tt lieu frontière de l'autre.
\inserted{Sous-tronçon f
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/018_rel.jpg

Alignment requires recheck: no flag

Review note: Crossed deux, tt, point, en and later lieu are distinguishable.

### C-018-U011 (C line 7)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 6.

Source C token:

```tex
\unsure{en}
```

Source C context:

```tex
es le sont, i.e. si \unsure{tt|les} \deleted{\unsure{él}} \unsure{point|lieu} frontière de l'un est \unsure{en} pos. rel. modérée à tt \unsure{lieu|point} frontière de l'autre.
\inserted{Sous-tronçon fermé large
```

Aligned final span:

```tex
en
```

Final context (up to 100 characters either side):

```tex
. modérée si leurs frontières le sont, i.e. si tt \deleted{\unsure{él}} point frontière de l'un est en pos. rel. modérée à tt lieu frontière de l'autre.
\inserted{Sous-tronçon fermé large : soit un sous
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/018_rel.jpg

Alignment requires recheck: no flag

Review note: Crossed deux, tt, point, en and later lieu are distinguishable.

### C-018-U012 (C line 7)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 6.

Source C token:

```tex
\unsure{lieu|point}
```

Source C context:

```tex
 \deleted{\unsure{él}} \unsure{point|lieu} frontière de l'un est \unsure{en} pos. rel. modérée à tt \unsure{lieu|point} frontière de l'autre.
\inserted{Sous-tronçon fermé large : soit un sous-tronçon, soit une partie un
```

Aligned final span:

```tex
lieu
```

Final context (up to 100 characters either side):

```tex
res le sont, i.e. si tt \deleted{\unsure{él}} point frontière de l'un est en pos. rel. modérée à tt lieu frontière de l'autre.
\inserted{Sous-tronçon fermé large : soit un sous-tronçon, soit une partie un
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/018_rel.jpg

Alignment requires recheck: no flag

Review note: Crossed deux, tt, point, en and later lieu are distinguishable.

### C-018-U013 (C line 9)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 8.

Source C token:

```tex
\unsure{est}
```

Source C context:

```tex
partie uniponctuelle $\{a\}$, dans ce cas, sa frontière est $a$.}
\deleted{Alors leur int} \deleted{\unsure{est} \unsure{partie}, \unsure{relat.} modérée, \unsure{au cas où}} Deux tronçons fermés larges sont en p
```

Aligned final span:

```tex
\unsure{est}
```

Final context (up to 100 characters either side):

```tex
partie uniponctuelle $\{a\}$, dans ce cas, sa frontière est $a$.}
\deleted{Alors leur int} \deleted{\unsure{est} \unsure{partie}, \unsure{relat.} modérée, \unsure{au cas où}} Deux tronçons fermés larges sont en p
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/018_middle.jpg

Alignment requires recheck: no flag

Review note: Multiple local cancellations obscure these old words and abbreviations; live text between the strikes is kept separate.

### C-018-U014 (C line 9)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 8.

Source C token:

```tex
\unsure{partie}
```

Source C context:

```tex
ctuelle $\{a\}$, dans ce cas, sa frontière est $a$.}
\deleted{Alors leur int} \deleted{\unsure{est} \unsure{partie}, \unsure{relat.} modérée, \unsure{au cas où}} Deux tronçons fermés larges sont en pos. gén. \delete
```

Aligned final span:

```tex
\unsure{partie}
```

Final context (up to 100 characters either side):

```tex
ctuelle $\{a\}$, dans ce cas, sa frontière est $a$.}
\deleted{Alors leur int} \deleted{\unsure{est} \unsure{partie}, \unsure{relat.} modérée, \unsure{au cas où}} Deux tronçons fermés larges sont en pos. gén. \delete
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/018_middle.jpg

Alignment requires recheck: no flag

Review note: Multiple local cancellations obscure these old words and abbreviations; live text between the strikes is kept separate.

### C-018-U015 (C line 9)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 8.

Source C token:

```tex
\unsure{relat.}
```

Source C context:

```tex
dans ce cas, sa frontière est $a$.}
\deleted{Alors leur int} \deleted{\unsure{est} \unsure{partie}, \unsure{relat.} modérée, \unsure{au cas où}} Deux tronçons fermés larges sont en pos. gén. \deleted{\unsure{sss|ssi
```

Aligned final span:

```tex
\unsure{relat.}
```

Final context (up to 100 characters either side):

```tex
dans ce cas, sa frontière est $a$.}
\deleted{Alors leur int} \deleted{\unsure{est} \unsure{partie}, \unsure{relat.} modérée, \unsure{au cas où}} Deux tronçons fermés larges sont en pos. gén. \deleted{\unsure{sss|ssi
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/018_middle.jpg

Alignment requires recheck: no flag

Review note: Multiple local cancellations obscure these old words and abbreviations; live text between the strikes is kept separate.

### C-018-U016 (C line 9)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 8.

Source C token:

```tex
\unsure{au cas où}
```

Source C context:

```tex
 est $a$.}
\deleted{Alors leur int} \deleted{\unsure{est} \unsure{partie}, \unsure{relat.} modérée, \unsure{au cas où}} Deux tronçons fermés larges sont en pos. gén. \deleted{\unsure{sss|ssi}} leurs frontières \deleted
```

Aligned final span:

```tex
\unsure{au cas où}
```

Final context (up to 100 characters either side):

```tex
 est $a$.}
\deleted{Alors leur int} \deleted{\unsure{est} \unsure{partie}, \unsure{relat.} modérée, \unsure{au cas où}} Deux tronçons fermés larges sont en pos. gén. \deleted{\unsure{sss|ssi}} leurs frontières \deleted
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/018_middle.jpg

Alignment requires recheck: no flag

Review note: Multiple local cancellations obscure these old words and abbreviations; live text between the strikes is kept separate.

### C-018-U017 (C line 9)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 8.

Source C token:

```tex
\unsure{sss|ssi}
```

Source C context:

```tex
\unsure{relat.} modérée, \unsure{au cas où}} Deux tronçons fermés larges sont en pos. gén. \deleted{\unsure{sss|ssi}} leurs frontières \deleted{\unsure{donc son} s'il \unsure{le} est en \unsure{pos.} \unsure{gén.} mo
```

Aligned final span:

```tex
\unsure{sss|ssi}
```

Final context (up to 100 characters either side):

```tex
\unsure{relat.} modérée, \unsure{au cas où}} Deux tronçons fermés larges sont en pos. gén. \deleted{\unsure{sss|ssi}} leurs frontières \deleted{\unsure{donc son} s'il \unsure{le} est en \unsure{pos.} \unsure{gén.} mo
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/018_middle.jpg

Alignment requires recheck: no flag

Review note: Multiple local cancellations obscure these old words and abbreviations; live text between the strikes is kept separate.

### C-018-U018 (C line 9)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 8.

Source C token:

```tex
\unsure{donc son}
```

Source C context:

```tex
 Deux tronçons fermés larges sont en pos. gén. \deleted{\unsure{sss|ssi}} leurs frontières \deleted{\unsure{donc son} s'il \unsure{le} est en \unsure{pos.} \unsure{gén.} modérée ou si} le sont.
% slanted
\margin{$(I\c
```

Aligned final span:

```tex
\unsure{donc son}
```

Final context (up to 100 characters either side):

```tex
 Deux tronçons fermés larges sont en pos. gén. \deleted{\unsure{sss|ssi}} leurs frontières \deleted{\unsure{donc son} s'il \unsure{le} est en \unsure{pos.} \unsure{gén.} modérée ou si} le sont.
% slanted
\margin{$(I\c
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/018_middle.jpg

Alignment requires recheck: no flag

Review note: Multiple local cancellations obscure these old words and abbreviations; live text between the strikes is kept separate.

### C-018-U019 (C line 9)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 8.

Source C token:

```tex
\unsure{le}
```

Source C context:

```tex
arges sont en pos. gén. \deleted{\unsure{sss|ssi}} leurs frontières \deleted{\unsure{donc son} s'il \unsure{le} est en \unsure{pos.} \unsure{gén.} modérée ou si} le sont.
% slanted
\margin{$(I\cap J)^{\unsure{\c
```

Aligned final span:

```tex
\unsure{le}
```

Final context (up to 100 characters either side):

```tex
arges sont en pos. gén. \deleted{\unsure{sss|ssi}} leurs frontières \deleted{\unsure{donc son} s'il \unsure{le} est en \unsure{pos.} \unsure{gén.} modérée ou si} le sont.
% slanted
\margin{$(I\cap J)^{\unsure{\p
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/018_middle.jpg

Alignment requires recheck: no flag

Review note: Multiple local cancellations obscure these old words and abbreviations; live text between the strikes is kept separate.

### C-018-U020 (C line 9)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 8.

Source C token:

```tex
\unsure{pos.}
```

Source C context:

```tex
gén. \deleted{\unsure{sss|ssi}} leurs frontières \deleted{\unsure{donc son} s'il \unsure{le} est en \unsure{pos.} \unsure{gén.} modérée ou si} le sont.
% slanted
\margin{$(I\cap J)^{\unsure{\cdot|\prime|\circ}}\su
```

Aligned final span:

```tex
\unsure{pos.}
```

Final context (up to 100 characters either side):

```tex
gén. \deleted{\unsure{sss|ssi}} leurs frontières \deleted{\unsure{donc son} s'il \unsure{le} est en \unsure{pos.} \unsure{gén.} modérée ou si} le sont.
% slanted
\margin{$(I\cap J)^{\unsure{\prime|\cdot|\circ}}\su
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/018_middle.jpg

Alignment requires recheck: no flag

Review note: Multiple local cancellations obscure these old words and abbreviations; live text between the strikes is kept separate.

### C-018-U021 (C line 9)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 8.

Source C token:

```tex
\unsure{gén.}
```

Source C context:

```tex
\unsure{sss|ssi}} leurs frontières \deleted{\unsure{donc son} s'il \unsure{le} est en \unsure{pos.} \unsure{gén.} modérée ou si} le sont.
% slanted
\margin{$(I\cap J)^{\unsure{\cdot|\prime|\circ}}\subset I\cup J^{
```

Aligned final span:

```tex
\unsure{gén.}
```

Final context (up to 100 characters either side):

```tex
\unsure{sss|ssi}} leurs frontières \deleted{\unsure{donc son} s'il \unsure{le} est en \unsure{pos.} \unsure{gén.} modérée ou si} le sont.
% slanted
\margin{$(I\cap J)^{\unsure{\prime|\cdot|\circ}}\subset I^{\cdot}
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/018_middle.jpg

Alignment requires recheck: no flag

Review note: Multiple local cancellations obscure these old words and abbreviations; live text between the strikes is kept separate.

### C-018-U022 (C line 11)

Mechanical state: **unsure token(s) overlap changed alignment; inspect**. Final aligned line: 10.

Source C token:

```tex
\unsure{\cdot|\prime|\circ}
```

Source C context:

```tex
unsure{le} est en \unsure{pos.} \unsure{gén.} modérée ou si} le sont.
% slanted
\margin{$(I\cap J)^{\unsure{\cdot|\prime|\circ}}\subset I\cup J^{\cdot}$ est vrai par argument topologique,}
Alors leur intersection est vide, \del
```

Aligned final span:

```tex
\unsure{\prime|\cdot|\circ}
```

Final context (up to 100 characters either side):

```tex
unsure{le} est en \unsure{pos.} \unsure{gén.} modérée ou si} le sont.
% slanted
\margin{$(I\cap J)^{\unsure{\prime|\cdot|\circ}}\subset I^{\cdot}\cup J^{\cdot}$ est vrai par argument topologique,}
Alors leur intersection est vi
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: revised

Crop links: crops/018_margin2_full.jpg

Alignment requires recheck: no flag

Review note: Raised first boundary mark is prime/dot/circle-like; a separate point over the right-hand I is visible and restored.

### C-018-U023 (C line 12)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 11.

Source C token:

```tex
\unsure{ou un}
```

Source C context:

```tex
set I\cup J^{\cdot}$ est vrai par argument topologique,}
Alors leur intersection est vide, \deleted{\unsure{ou un}} ou un \deleted{\illegible{1}} tronçon large, dont la frontière est contenue dans \deleted{\unsure{
```

Aligned final span:

```tex
\unsure{ou un}
```

Final context (up to 100 characters either side):

```tex
cdot}\cup J^{\cdot}$ est vrai par argument topologique,}
Alors leur intersection est vide, \deleted{\unsure{ou un}} ou un \deleted{\illegible{1}} tronçon large, dont la frontière est contenue dans \deleted{\unsure{
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/018_cross.jpg

Alignment requires recheck: no flag

Review note: Old starts and crossed definition fragments remain partly unreadable.

### C-018-U024 (C line 12)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 11.

Source C token:

```tex
\unsure{frontière}
```

Source C context:

```tex
e{ou un}} ou un \deleted{\illegible{1}} tronçon large, dont la frontière est contenue dans \deleted{\unsure{frontière} \unsure{large en pos. rel. modérée}} la réunion des frontières.
\deleted{\unsure{enfin|afin} \unsur
```

Aligned final span:

```tex
\unsure{frontière}
```

Final context (up to 100 characters either side):

```tex
e{ou un}} ou un \deleted{\illegible{1}} tronçon large, dont la frontière est contenue dans \deleted{\unsure{frontière} \unsure{large en pos. rel. modérée}} la réunion des frontières.
\deleted{\unsure{enfin|afin} tt pts
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/018_cross.jpg

Alignment requires recheck: no flag

Review note: Old starts and crossed definition fragments remain partly unreadable.

### C-018-U025 (C line 12)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 11.

Source C token:

```tex
\unsure{large en pos. rel. modérée}
```

Source C context:

```tex
leted{\illegible{1}} tronçon large, dont la frontière est contenue dans \deleted{\unsure{frontière} \unsure{large en pos. rel. modérée}} la réunion des frontières.
\deleted{\unsure{enfin|afin} \unsure{tt|les} pts frontière. \unsure{qui
```

Aligned final span:

```tex
\unsure{large en pos. rel. modérée}
```

Final context (up to 100 characters either side):

```tex
leted{\illegible{1}} tronçon large, dont la frontière est contenue dans \deleted{\unsure{frontière} \unsure{large en pos. rel. modérée}} la réunion des frontières.
\deleted{\unsure{enfin|afin} tt pts frontière. \unsure{qui} \unsure{est
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/018_cross.jpg

Alignment requires recheck: no flag

Review note: Old starts and crossed definition fragments remain partly unreadable.

### C-018-U026 (C line 13)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 12.

Source C token:

```tex
\unsure{enfin|afin}
```

Source C context:

```tex
deleted{\unsure{frontière} \unsure{large en pos. rel. modérée}} la réunion des frontières.
\deleted{\unsure{enfin|afin} \unsure{tt|les} pts frontière. \unsure{qui} \unsure{est} fermés deux tronçon fermé large : tout par
```

Aligned final span:

```tex
\unsure{enfin|afin}
```

Final context (up to 100 characters either side):

```tex
deleted{\unsure{frontière} \unsure{large en pos. rel. modérée}} la réunion des frontières.
\deleted{\unsure{enfin|afin} tt pts frontière. \unsure{qui} \unsure{est} fermés deux tronçon fermé large : tout partie de $L$}


```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/018_cross.jpg

Alignment requires recheck: no flag

Review note: Old starts and crossed definition fragments remain partly unreadable.

### C-018-U027 (C line 13)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 12.

Source C token:

```tex
\unsure{tt|les}
```

Source C context:

```tex
tière} \unsure{large en pos. rel. modérée}} la réunion des frontières.
\deleted{\unsure{enfin|afin} \unsure{tt|les} pts frontière. \unsure{qui} \unsure{est} fermés deux tronçon fermé large : tout partie de la}

$\bi
```

Aligned final span:

```tex
tt
```

Final context (up to 100 characters either side):

```tex
tière} \unsure{large en pos. rel. modérée}} la réunion des frontières.
\deleted{\unsure{enfin|afin} tt pts frontière. \unsure{qui} \unsure{est} fermés deux tronçon fermé large : tout partie de $L$}

$\b
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/018_cross.jpg

Alignment requires recheck: no flag

Review note: Two short t strokes support tt, not les.

### C-018-U028 (C line 13)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 12.

Source C token:

```tex
\unsure{qui}
```

Source C context:

```tex
l. modérée}} la réunion des frontières.
\deleted{\unsure{enfin|afin} \unsure{tt|les} pts frontière. \unsure{qui} \unsure{est} fermés deux tronçon fermé large : tout partie de la}

$\bigl[$\uline{Partie fermée} \u
```

Aligned final span:

```tex
\unsure{qui}
```

Final context (up to 100 characters either side):

```tex
ge en pos. rel. modérée}} la réunion des frontières.
\deleted{\unsure{enfin|afin} tt pts frontière. \unsure{qui} \unsure{est} fermés deux tronçon fermé large : tout partie de $L$}

$\bigl[$\uline{Partie fermée} \
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/018_cross.jpg

Alignment requires recheck: no flag

Review note: Old starts and crossed definition fragments remain partly unreadable.

### C-018-U029 (C line 13)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 12.

Source C token:

```tex
\unsure{est}
```

Source C context:

```tex
la réunion des frontières.
\deleted{\unsure{enfin|afin} \unsure{tt|les} pts frontière. \unsure{qui} \unsure{est} fermés deux tronçon fermé large : tout partie de la}

$\bigl[$\uline{Partie fermée} \uline{modérée}
```

Aligned final span:

```tex
\unsure{est}
```

Final context (up to 100 characters either side):

```tex
l. modérée}} la réunion des frontières.
\deleted{\unsure{enfin|afin} tt pts frontière. \unsure{qui} \unsure{est} fermés deux tronçon fermé large : tout partie de $L$}

$\bigl[$\uline{Partie fermée} \uline{modérée
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/018_cross.jpg

Alignment requires recheck: no flag

Review note: Old starts and crossed definition fragments remain partly unreadable.

### C-018-U030 (C line 15)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 14.

Source C token:

```tex
\unsure{ss-tronçons|ss.-tronçons}
```

Source C context:

```tex
rmée} \uline{modérée} de $I$ : toute partie qui se met sous forme de réunion d'une famille finie de \unsure{ss-tronçons|ss.-tronçons} fermés larges mutuellement disjoints. et mut. \deleted{\unsure{en position}} rel. modérée.$\bigr]$

```

Aligned final span:

```tex
\unsure{ss-tronçons|ss.-tronçons}
```

Final context (up to 100 characters either side):

```tex
rmée} \uline{modérée} de $I$ : toute partie qui se met sous forme de réunion d'une famille finie de \unsure{ss-tronçons|ss.-tronçons} fermés larges mutuellement disjoints. et mut. \deleted{\unsure{en position}} rel. modérée.$\bigr]$

```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/018_definition.jpg

Alignment requires recheck: no flag

Review note: Abbreviation point and cancelled en position remain unresolved.

### C-018-U031 (C line 15)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 14.

Source C token:

```tex
\unsure{en position}
```

Source C context:

```tex
e finie de \unsure{ss-tronçons|ss.-tronçons} fermés larges mutuellement disjoints. et mut. \deleted{\unsure{en position}} rel. modérée.$\bigr]$

\unsure{Top.|Tp.} de $L$ \unsure{ici} : Prenant comme base d'ouverts les \u
```

Aligned final span:

```tex
\unsure{en position}
```

Final context (up to 100 characters either side):

```tex
e finie de \unsure{ss-tronçons|ss.-tronçons} fermés larges mutuellement disjoints. et mut. \deleted{\unsure{en position}} rel. modérée.$\bigr]$

\unsure{Top.|Tp.} de $L$ \unsure{ici} : Prenant comme base d'ouverts les \u
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/018_definition.jpg

Alignment requires recheck: no flag

Review note: Abbreviation point and cancelled en position remain unresolved.

### C-018-U032 (C line 17)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 16.

Source C token:

```tex
\unsure{Top.|Tp.}
```

Source C context:

```tex
fermés larges mutuellement disjoints. et mut. \deleted{\unsure{en position}} rel. modérée.$\bigr]$

\unsure{Top.|Tp.} de $L$ \unsure{ici} : Prenant comme base d'ouverts les \unsure{«|``} $]a,b[$ pour $a<b$, et les $L_
```

Aligned final span:

```tex
\unsure{Top.|Tp.}
```

Final context (up to 100 characters either side):

```tex
fermés larges mutuellement disjoints. et mut. \deleted{\unsure{en position}} rel. modérée.$\bigr]$

\unsure{Top.|Tp.} de $L$ \unsure{ici} : Prenant comme base d'ouverts les \unsure{«|``} $]a,b[$ pour $a<b$, et les $L_
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/018_foot.jpg

Alignment requires recheck: no flag

Review note: Topology label, ici, quote, stray curved mark, old I and possible hat remain uncertain amid the crossing margin.

### C-018-U033 (C line 17)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 16.

Source C token:

```tex
\unsure{ici}
```

Source C context:

```tex
t disjoints. et mut. \deleted{\unsure{en position}} rel. modérée.$\bigr]$

\unsure{Top.|Tp.} de $L$ \unsure{ici} : Prenant comme base d'ouverts les \unsure{«|``} $]a,b[$ pour $a<b$, et les $L_{>a}$ et $L_{<a}$ \u
```

Aligned final span:

```tex
\unsure{ici}
```

Final context (up to 100 characters either side):

```tex
t disjoints. et mut. \deleted{\unsure{en position}} rel. modérée.$\bigr]$

\unsure{Top.|Tp.} de $L$ \unsure{ici} : Prenant comme base d'ouverts les \unsure{«|``} $]a,b[$ pour $a<b$, et les $L_{>a}$ et $L_{<a}$ \u
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/018_foot.jpg

Alignment requires recheck: no flag

Review note: Topology label, ici, quote, stray curved mark, old I and possible hat remain uncertain amid the crossing margin.

### C-018-U034 (C line 17)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 16.

Source C token:

```tex
\unsure{«|``}
```

Source C context:

```tex
n}} rel. modérée.$\bigr]$

\unsure{Top.|Tp.} de $L$ \unsure{ici} : Prenant comme base d'ouverts les \unsure{«|``} $]a,b[$ pour $a<b$, et les $L_{>a}$ et $L_{<a}$ \unsure{(}. Alors \deleted{$\unsure{I}$} pour un so
```

Aligned final span:

```tex
\unsure{«|``}
```

Final context (up to 100 characters either side):

```tex
n}} rel. modérée.$\bigr]$

\unsure{Top.|Tp.} de $L$ \unsure{ici} : Prenant comme base d'ouverts les \unsure{«|``} $]a,b[$ pour $a<b$, et les $L_{>a}$ et $L_{<a}$ \unsure{(}. Alors \deleted{$\unsure{I}$} pour un so
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/018_foot.jpg

Alignment requires recheck: no flag

Review note: Topology label, ici, quote, stray curved mark, old I and possible hat remain uncertain amid the crossing margin.

### C-018-U035 (C line 17)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 16.

Source C token:

```tex
\unsure{(}
```

Source C context:

```tex
i} : Prenant comme base d'ouverts les \unsure{«|``} $]a,b[$ pour $a<b$, et les $L_{>a}$ et $L_{<a}$ \unsure{(}. Alors \deleted{$\unsure{I}$} pour un sous-ps. tronçon \inserted{fermé}, $\partial\unsure{I|\wideha
```

Aligned final span:

```tex
\unsure{(}
```

Final context (up to 100 characters either side):

```tex
i} : Prenant comme base d'ouverts les \unsure{«|``} $]a,b[$ pour $a<b$, et les $L_{>a}$ et $L_{<a}$ \unsure{(}. Alors \deleted{$\unsure{I}$} pour un sous-ps. tronçon \inserted{fermé}, $\partial\unsure{I|\wideha
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/018_foot.jpg

Alignment requires recheck: no flag

Review note: Topology label, ici, quote, stray curved mark, old I and possible hat remain uncertain amid the crossing margin.

### C-018-U036 (C line 17)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 16.

Source C token:

```tex
\unsure{I}
```

Source C context:

```tex
verts les \unsure{«|``} $]a,b[$ pour $a<b$, et les $L_{>a}$ et $L_{<a}$ \unsure{(}. Alors \deleted{$\unsure{I}$} pour un sous-ps. tronçon \inserted{fermé}, $\partial\unsure{I|\widehat I}$ est la frontière
% sla
```

Aligned final span:

```tex
\unsure{I}
```

Final context (up to 100 characters either side):

```tex
verts les \unsure{«|``} $]a,b[$ pour $a<b$, et les $L_{>a}$ et $L_{<a}$ \unsure{(}. Alors \deleted{$\unsure{I}$} pour un sous-ps. tronçon \inserted{fermé}, $\partial\unsure{I|\widehat I}$ est la frontière
% sla
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/018_foot.jpg

Alignment requires recheck: no flag

Review note: Topology label, ici, quote, stray curved mark, old I and possible hat remain uncertain amid the crossing margin.

### C-018-U037 (C line 17)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 16.

Source C token:

```tex
\unsure{I|\widehat I}
```

Source C context:

```tex
_{<a}$ \unsure{(}. Alors \deleted{$\unsure{I}$} pour un sous-ps. tronçon \inserted{fermé}, $\partial\unsure{I|\widehat I}$ est la frontière
% slanted
\margin{\uline{NB} Il n'y a pas besoin d'introduire les $L_{>a}$ \unsur
```

Aligned final span:

```tex
\unsure{I|\widehat I}
```

Final context (up to 100 characters either side):

```tex
_{<a}$ \unsure{(}. Alors \deleted{$\unsure{I}$} pour un sous-ps. tronçon \inserted{fermé}, $\partial\unsure{I|\widehat I}$ est la frontière
% slanted
\margin{\uline{NB} Il n'y a pas besoin d'introduire les $L_{>a}$ \unsur
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/018_foot.jpg

Alignment requires recheck: no flag

Review note: Topology label, ici, quote, stray curved mark, old I and possible hat remain uncertain amid the crossing margin.

### C-018-U038 (C line 19)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 18.

Source C token:

```tex
\unsure{et}
```

Source C context:

```tex
hat I}$ est la frontière
% slanted
\margin{\uline{NB} Il n'y a pas besoin d'introduire les $L_{>a}$ \unsure{et} si $L$ \unsure{n'a} pas de plus grand élément, et \unsure{itou|idem} pour $L_{<a}$ si \unsure{$a$|$
```

Aligned final span:

```tex
\unsure{et}
```

Final context (up to 100 characters either side):

```tex
hat I}$ est la frontière
% slanted
\margin{\uline{NB} Il n'y a pas besoin d'introduire les $L_{>a}$ \unsure{et} si $L$ \unsure{n'a} pas de plus grand élément, et itou pour $L_{<a}$ si \unsure{$a$|$L$} n'a pas de
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/018_nb_full.jpg; crops/018_nb_end.jpg

Alignment requires recheck: no flag

Review note: Crowded NB words and variable remain doubtful; the final short unreadable span is not completed from meaning.

### C-018-U039 (C line 19)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 18.

Source C token:

```tex
\unsure{n'a}
```

Source C context:

```tex
tière
% slanted
\margin{\uline{NB} Il n'y a pas besoin d'introduire les $L_{>a}$ \unsure{et} si $L$ \unsure{n'a} pas de plus grand élément, et \unsure{itou|idem} pour $L_{<a}$ si \unsure{$a$|$L$} n'a pas de \unsu
```

Aligned final span:

```tex
\unsure{n'a}
```

Final context (up to 100 characters either side):

```tex
tière
% slanted
\margin{\uline{NB} Il n'y a pas besoin d'introduire les $L_{>a}$ \unsure{et} si $L$ \unsure{n'a} pas de plus grand élément, et itou pour $L_{<a}$ si \unsure{$a$|$L$} n'a pas de \unsure{plus} petit
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/018_nb_full.jpg; crops/018_nb_end.jpg

Alignment requires recheck: no flag

Review note: Crowded NB words and variable remain doubtful; the final short unreadable span is not completed from meaning.

### C-018-U040 (C line 19)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 18.

Source C token:

```tex
\unsure{itou|idem}
```

Source C context:

```tex
 pas besoin d'introduire les $L_{>a}$ \unsure{et} si $L$ \unsure{n'a} pas de plus grand élément, et \unsure{itou|idem} pour $L_{<a}$ si \unsure{$a$|$L$} n'a pas de \unsure{plus} petit élément. \unsure{Dans ce cas|Dans}
```

Aligned final span:

```tex
itou
```

Final context (up to 100 characters either side):

```tex
 pas besoin d'introduire les $L_{>a}$ \unsure{et} si $L$ \unsure{n'a} pas de plus grand élément, et itou pour $L_{<a}$ si \unsure{$a$|$L$} n'a pas de \unsure{plus} petit élément. \unsure{Dans ce cas|Dans}
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved

Crop links: crops/018_nb_start.jpg

Alignment requires recheck: no flag

Review note: Itou is legible in the rotated note.

### C-018-U041 (C line 19)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 18.

Source C token:

```tex
\unsure{$a$|$L$}
```

Source C context:

```tex
$ \unsure{et} si $L$ \unsure{n'a} pas de plus grand élément, et \unsure{itou|idem} pour $L_{<a}$ si \unsure{$a$|$L$} n'a pas de \unsure{plus} petit élément. \unsure{Dans ce cas|Dans} \illegible{2} $]a,b[$ \unsure{eux
```

Aligned final span:

```tex
\unsure{$a$|$L$}
```

Final context (up to 100 characters either side):

```tex
re les $L_{>a}$ \unsure{et} si $L$ \unsure{n'a} pas de plus grand élément, et itou pour $L_{<a}$ si \unsure{$a$|$L$} n'a pas de \unsure{plus} petit élément. \unsure{Dans ce cas|Dans} \illegible{2} $]a,b[$.}

% pale v
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/018_nb_full.jpg; crops/018_nb_end.jpg

Alignment requires recheck: no flag

Review note: Crowded NB words and variable remain doubtful; the final short unreadable span is not completed from meaning.

### C-018-U042 (C line 19)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 18.

Source C token:

```tex
\unsure{plus}
```

Source C context:

```tex
{n'a} pas de plus grand élément, et \unsure{itou|idem} pour $L_{<a}$ si \unsure{$a$|$L$} n'a pas de \unsure{plus} petit élément. \unsure{Dans ce cas|Dans} \illegible{2} $]a,b[$ \unsure{eux} \illegible{2} $]a,b[$.}
```

Aligned final span:

```tex
\unsure{plus}
```

Final context (up to 100 characters either side):

```tex
si $L$ \unsure{n'a} pas de plus grand élément, et itou pour $L_{<a}$ si \unsure{$a$|$L$} n'a pas de \unsure{plus} petit élément. \unsure{Dans ce cas|Dans} \illegible{2} $]a,b[$.}

% pale vertical watermark
\rotate
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/018_nb_full.jpg; crops/018_nb_end.jpg

Alignment requires recheck: no flag

Review note: Crowded NB words and variable remain doubtful; the final short unreadable span is not completed from meaning.

### C-018-U043 (C line 19)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 18.

Source C token:

```tex
\unsure{Dans ce cas|Dans}
```

Source C context:

```tex
nt, et \unsure{itou|idem} pour $L_{<a}$ si \unsure{$a$|$L$} n'a pas de \unsure{plus} petit élément. \unsure{Dans ce cas|Dans} \illegible{2} $]a,b[$ \unsure{eux} \illegible{2} $]a,b[$.}

```

Aligned final span:

```tex
\unsure{Dans ce cas|Dans}
```

Final context (up to 100 characters either side):

```tex
us grand élément, et itou pour $L_{<a}$ si \unsure{$a$|$L$} n'a pas de \unsure{plus} petit élément. \unsure{Dans ce cas|Dans} \illegible{2} $]a,b[$.}

% pale vertical watermark
\rotatebox{90}{\textsc{\unsure{ra Strong Extra}}
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained

Crop links: crops/018_nb_full.jpg; crops/018_nb_end.jpg

Alignment requires recheck: no flag

Review note: Crowded NB words and variable remain doubtful; the final short unreadable span is not completed from meaning.

### C-018-U044 (C line 19)

Mechanical state: **unsure token(s) overlap changed alignment; inspect**. Final aligned line: 20.

Source C token:

```tex
\unsure{eux}
```

Source C context:

```tex
re{$a$|$L$} n'a pas de \unsure{plus} petit élément. \unsure{Dans ce cas|Dans} \illegible{2} $]a,b[$ \unsure{eux} \illegible{2} $]a,b[$.}

```

Aligned final span:

```tex
pale vertical watermark
\rotatebox{90}{\textsc{\unsure{ra Strong Extra}
```

Final context (up to 100 characters either side):

```tex
$|$L$} n'a pas de \unsure{plus} petit élément. \unsure{Dans ce cas|Dans} \illegible{2} $]a,b[$.}

% pale vertical watermark
\rotatebox{90}{\textsc{\unsure{ra Strong Extra}}}

```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: removed as misplaced

Crop links: crops/018_bottom_layers.jpg; crops/018_nb_end.jpg

Alignment requires recheck: no flag

Review note: The apparent eux belongs to the crossing horizontal main-text region. C also counted its larger ]a,b[ again; NB has only the smaller oblique terminal interval formula. Alignment recheck: Removal makes the mechanical replacement span drift to the watermark; that is not a reading of eux. Root decision: no NB counterpart; crossing main-line material was wrongly duplicated.

### C-019-U001 (C line 2)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 2.

Source C token:

```tex
\unsure{L|\mathscr{L}}
```

Source C context:

```tex
\scanpage{19}\mspage{18}
\uline{Th} Soit $\unsure{L|\mathscr{L}}$ un tronçon \unsure{biordonné|bien donné}\unsure{;|,} soit $\deleted{\unsure{U}}X\subset L$, tel qu
```

Aligned final span:

```tex
\mathcal L
```

Final context (up to 100 characters either side):

```tex
\scanpage{19}\mspage{18}
\uline{Th} Soit $\mathcal L$ un tronçon biordonné, soit $\deleted{\unsure{U}}X\subset\mathcal L$, tel qu'il existe $I\subset\ma
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved from ink

Crop links: crops/019_top.jpg

Alignment requires recheck: no flag

Review note: Looped ground-set L, the written biordonné, comma, compressed Pstrf and the cancelled formé remain legible under enlargement.

### C-019-U002 (C line 2)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 2.

Source C token:

```tex
\unsure{biordonné|bien donné}
```

Source C context:

```tex
\scanpage{19}\mspage{18}
\uline{Th} Soit $\unsure{L|\mathscr{L}}$ un tronçon \unsure{biordonné|bien donné}\unsure{;|,} soit $\deleted{\unsure{U}}X\subset L$, tel qu'il existe $I\subset\unsure{\mathrm{Pstrf}
```

Aligned final span:

```tex
biordonné
```

Final context (up to 100 characters either side):

```tex
\scanpage{19}\mspage{18}
\uline{Th} Soit $\mathcal L$ un tronçon biordonné, soit $\deleted{\unsure{U}}X\subset\mathcal L$, tel qu'il existe $I\subset\mathrm{Pstrf}(\mathcal L
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved from ink

Crop links: crops/019_top.jpg

Alignment requires recheck: no flag

Review note: Looped ground-set L, the written biordonné, comma, compressed Pstrf and the cancelled formé remain legible under enlargement.

### C-019-U003 (C line 2)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 2.

Source C token:

```tex
\unsure{;|,}
```

Source C context:

```tex
age{19}\mspage{18}
\uline{Th} Soit $\unsure{L|\mathscr{L}}$ un tronçon \unsure{biordonné|bien donné}\unsure{;|,} soit $\deleted{\unsure{U}}X\subset L$, tel qu'il existe $I\subset\unsure{\mathrm{Pstrf}|\mathrm{Ps\
```

Aligned final span:

```tex
,
```

Final context (up to 100 characters either side):

```tex
\scanpage{19}\mspage{18}
\uline{Th} Soit $\mathcal L$ un tronçon biordonné, soit $\deleted{\unsure{U}}X\subset\mathcal L$, tel qu'il existe $I\subset\mathrm{Pstrf}(\mathcal L)
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved from ink

Crop links: crops/019_top.jpg

Alignment requires recheck: no flag

Review note: Looped ground-set L, the written biordonné, comma, compressed Pstrf and the cancelled formé remain legible under enlargement.

### C-019-U004 (C line 2)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 2.

Source C token:

```tex
\unsure{U}
```

Source C context:

```tex
} Soit $\unsure{L|\mathscr{L}}$ un tronçon \unsure{biordonné|bien donné}\unsure{;|,} soit $\deleted{\unsure{U}}X\subset L$, tel qu'il existe $I\subset\unsure{\mathrm{Pstrf}|\mathrm{Ps\,tr\,f}}(L)$ (ens des ps-t
```

Aligned final span:

```tex
\unsure{U}
```

Final context (up to 100 characters either side):

```tex
\scanpage{19}\mspage{18}
\uline{Th} Soit $\mathcal L$ un tronçon biordonné, soit $\deleted{\unsure{U}}X\subset\mathcal L$, tel qu'il existe $I\subset\mathrm{Pstrf}(\mathcal L)$ (ens des ps-tronçons fer
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/019_top.jpg

Alignment requires recheck: no flag

Review note: The overwritten U is partly covered by X; the cancellation is retained without a firmer letter claim.

### C-019-U005 (C line 2)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 2.

Source C token:

```tex
\unsure{\mathrm{Pstrf}|\mathrm{Ps\,tr\,f}}
```

Source C context:

```tex
{biordonné|bien donné}\unsure{;|,} soit $\deleted{\unsure{U}}X\subset L$, tel qu'il existe $I\subset\unsure{\mathrm{Pstrf}|\mathrm{Ps\,tr\,f}}(L)$ (ens des ps-tronçons fermés de $L$), $I$ fini, \deleted{\unsure{formé} de} tel que
\[
\begin{al
```

Aligned final span:

```tex
\mathrm{Pstrf}(\mathcal 
```

Final context (up to 100 characters either side):

```tex
l L$ un tronçon biordonné, soit $\deleted{\unsure{U}}X\subset\mathcal L$, tel qu'il existe $I\subset\mathrm{Pstrf}(\mathcal L)$ (ens des ps-tronçons fermés de $\mathcal L$), $I$ fini, \deleted{formé de} tel que
\[
\begin{ali
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved from ink

Crop links: crops/019_top.jpg

Alignment requires recheck: no flag

Review note: Looped ground-set L, the written biordonné, comma, compressed Pstrf and the cancelled formé remain legible under enlargement.

### C-019-U006 (C line 2)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 2.

Source C token:

```tex
\unsure{formé}
```

Source C context:

```tex
sure{\mathrm{Pstrf}|\mathrm{Ps\,tr\,f}}(L)$ (ens des ps-tronçons fermés de $L$), $I$ fini, \deleted{\unsure{formé} de} tel que
\[
\begin{aligned}
\text{a)}\quad \forall i,j\in I,\ i\ne j,\quad
\left\{\begin{aligned
```

Aligned final span:

```tex
formé
```

Final context (up to 100 characters either side):

```tex
\subset\mathrm{Pstrf}(\mathcal L)$ (ens des ps-tronçons fermés de $\mathcal L$), $I$ fini, \deleted{formé de} tel que
\[
\begin{aligned}
\text{a)}\quad \forall i,j\in I,\ i\ne j,\quad
\left\{\begin{aligned
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved from ink

Crop links: crops/019_top.jpg

Alignment requires recheck: no flag

Review note: Looped ground-set L, the written biordonné, comma, compressed Pstrf and the cancelled formé remain legible under enlargement.

### C-019-U007 (C line 9)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 9.

Source C token:

```tex
\unsure{\partial}
```

Source C context:

```tex
igned}
&T_i\cap T_j=\emptyset\\
&T_i\text{ et }T_j\text{ en pos. rel. mod.}\\
&\text{i.e. }\deleted{\unsure{\partial}}T_i^{\unsure{\cdot|\prime}}\cup \deleted{\unsure{\partial}}T_j^{\cdot}\ \text{\deleted{est} partie}
```

Aligned final span:

```tex
\unsure{\partial}
```

Final context (up to 100 characters either side):

```tex
igned}
&T_i\cap T_j=\emptyset\\
&T_i\text{ et }T_j\text{ en pos. rel. mod.}\\
&\text{i.e. }\deleted{\unsure{\partial}}T_i^{\cdot}\cup \deleted{\unsure{\partial}}T_j^{\cdot}\ \text{\deleted{est} partie}\\
&\qquad\text{
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/019_condition.jpg

Alignment requires recheck: no flag

Review note: The old boundary signs are crossed and partly blackened; their possible ∂ remains marked.

### C-019-U008 (C line 9)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 9.

Source C token:

```tex
\unsure{\cdot|\prime}
```

Source C context:

```tex
ptyset\\
&T_i\text{ et }T_j\text{ en pos. rel. mod.}\\
&\text{i.e. }\deleted{\unsure{\partial}}T_i^{\unsure{\cdot|\prime}}\cup \deleted{\unsure{\partial}}T_j^{\cdot}\ \text{\deleted{est} partie}\\
&\qquad\text{finie modér
```

Aligned final span:

```tex
\cdot
```

Final context (up to 100 characters either side):

```tex
ptyset\\
&T_i\text{ et }T_j\text{ en pos. rel. mod.}\\
&\text{i.e. }\deleted{\unsure{\partial}}T_i^{\cdot}\cup \deleted{\unsure{\partial}}T_j^{\cdot}\ \text{\deleted{est} partie}\\
&\qquad\text{finie modér
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved from ink

Crop links: crops/019_condition.jpg

Alignment requires recheck: no flag

Review note: The elevated mark is a dot; the abbreviation has ra followed by a p descender, hence Drap.

### C-019-U009 (C line 9)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 9.

Source C token:

```tex
\unsure{\partial}
```

Source C context:

```tex
 pos. rel. mod.}\\
&\text{i.e. }\deleted{\unsure{\partial}}T_i^{\unsure{\cdot|\prime}}\cup \deleted{\unsure{\partial}}T_j^{\cdot}\ \text{\deleted{est} partie}\\
&\qquad\text{finie modérée (ou}\\
&\text{encore }\forall
```

Aligned final span:

```tex
\unsure{\partial}
```

Final context (up to 100 characters either side):

```tex
et }T_j\text{ en pos. rel. mod.}\\
&\text{i.e. }\deleted{\unsure{\partial}}T_i^{\cdot}\cup \deleted{\unsure{\partial}}T_j^{\cdot}\ \text{\deleted{est} partie}\\
&\qquad\text{finie modérée (ou}\\
&\text{encore }\forall
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/019_condition.jpg

Alignment requires recheck: no flag

Review note: The old boundary signs are crossed and partly blackened; their possible ∂ remains marked.

### C-019-U010 (C line 11)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 11.

Source C token:

```tex
\unsure{\partial}
```

Source C context:

```tex
\text{\deleted{est} partie}\\
&\qquad\text{finie modérée (ou}\\
&\text{encore }\forall a\in\deleted{\unsure{\partial}}T_i^{\cdot},\ b\in\deleted{\unsure{\partial}}T_j^{\cdot},\\
&a\ne b,\ \text{on a}\quad\{a,b\}\in\un
```

Aligned final span:

```tex
\unsure{\partial}
```

Final context (up to 100 characters either side):

```tex
\text{\deleted{est} partie}\\
&\qquad\text{finie modérée (ou}\\
&\text{encore }\forall a\in\deleted{\unsure{\partial}}T_i^{\cdot},\ b\in\deleted{\unsure{\partial}}T_j^{\cdot},\\
&a\ne b,\ \text{on a}\quad\{a,b\}\in\un
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/019_condition.jpg

Alignment requires recheck: no flag

Review note: The old boundary signs are crossed and partly blackened; their possible ∂ remains marked.

### C-019-U011 (C line 11)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 11.

Source C token:

```tex
\unsure{\partial}
```

Source C context:

```tex
nie modérée (ou}\\
&\text{encore }\forall a\in\deleted{\unsure{\partial}}T_i^{\cdot},\ b\in\deleted{\unsure{\partial}}T_j^{\cdot},\\
&a\ne b,\ \text{on a}\quad\{a,b\}\in\underset{\substack{\Vert\\\unsure{\mathrm{Disp}
```

Aligned final span:

```tex
\unsure{\partial}
```

Final context (up to 100 characters either side):

```tex
nie modérée (ou}\\
&\text{encore }\forall a\in\deleted{\unsure{\partial}}T_i^{\cdot},\ b\in\deleted{\unsure{\partial}}T_j^{\cdot},\\
&a\ne b,\ \text{on a}\quad\{a,b\}\in\underset{\substack{\Vert\\\mathrm{Drap}_2(\math
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/019_condition.jpg

Alignment requires recheck: no flag

Review note: The old boundary signs are crossed and partly blackened; their possible ∂ remains marked.

### C-019-U012 (C line 12)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 12.

Source C token:

```tex
\unsure{\mathrm{Disp}|\mathrm{Dsp}}
```

Source C context:

```tex
ted{\unsure{\partial}}T_j^{\cdot},\\
&a\ne b,\ \text{on a}\quad\{a,b\}\in\underset{\substack{\Vert\\\unsure{\mathrm{Disp}|\mathrm{Dsp}}_2(L)}}{B_{\unsure{0|o}}(L)}
\end{aligned}\right.
\end{aligned}
\]
\deleted{\illegible{1}}
\[
\text{
```

Aligned final span:

```tex
\mathrm{Drap}_2(\mathcal 
```

Final context (up to 100 characters either side):

```tex
ted{\unsure{\partial}}T_j^{\cdot},\\
&a\ne b,\ \text{on a}\quad\{a,b\}\in\underset{\substack{\Vert\\\mathrm{Drap}_2(\mathcal L)}}{\unsure{B|S}_{0}(\mathcal L)}
\end{aligned}\right.
\end{aligned}
\]
\deleted{\illegible{1}}
\[

```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved from ink

Crop links: crops/019_condition.jpg

Alignment requires recheck: no flag

Review note: The elevated mark is a dot; the abbreviation has ra followed by a p descender, hence Drap.

### C-019-U013 (C line 12)

Mechanical state: **unsure token(s) overlap changed alignment; inspect**. Final aligned line: 12.

Source C token:

```tex
\unsure{0|o}
```

Source C context:

```tex
 \text{on a}\quad\{a,b\}\in\underset{\substack{\Vert\\\unsure{\mathrm{Disp}|\mathrm{Dsp}}_2(L)}}{B_{\unsure{0|o}}(L)}
\end{aligned}\right.
\end{aligned}
\]
\deleted{\illegible{1}}
\[
\text{b)}\quad \deleted{U}X=\
```

Aligned final span:

```tex
\unsure{B|S}_{0
```

Final context (up to 100 characters either side):

```tex
ot},\\
&a\ne b,\ \text{on a}\quad\{a,b\}\in\underset{\substack{\Vert\\\mathrm{Drap}_2(\mathcal L)}}{\unsure{B|S}_{0}(\mathcal L)}
\end{aligned}\right.
\end{aligned}
\]
\deleted{\illegible{1}}
\[
\text{b)}\quad \dele
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved index; new initial uncertainty

Crop links: crops/019_condition.jpg

Alignment requires recheck: no flag

Review note: The index is a small closed zero. The upper initial remains B/S; this separate uncertainty was added rather than inferred from the notation.

### C-019-U014 (C line 23)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 24.

Source C token:

```tex
\unsure{d'unique|unique}
```

Source C context:

```tex
\]
\deleted{\illegible{1}}
\[
\text{b)}\quad \deleted{U}X=\bigcup T_i
\]

Alors

$1^\circ$) $I$ est \unsure{d'unique|unique} [\unsure{$=$|.} les $T_i$ sont les comp. conn. de $U$]
\margin{NB $U=\emptyset$ sss $I=\emptyset$}

```

Aligned final span:

```tex
\unsure{d'unique|unique}
```

Final context (up to 100 characters either side):

```tex
\text{b)}\quad \deleted{U}X=\bigcup T_i
\]
\margin{\unsure{un|en} disj.}

Alors

$1^\circ$) $I$ est \unsure{d'unique|unique} [\unsure{$=$|.} les $T_i$ sont les comp. conn. de $U$]
\margin{NB $U=\emptyset$ sss $I=\emptyset$}

```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/019_unique.jpg

Alignment requires recheck: no flag

Review note: The entry stroke before unique and the small bracket mark cannot be distinguished securely.

### C-019-U015 (C line 23)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 24.

Source C token:

```tex
\unsure{$=$|.}
```

Source C context:

```tex

\[
\text{b)}\quad \deleted{U}X=\bigcup T_i
\]

Alors

$1^\circ$) $I$ est \unsure{d'unique|unique} [\unsure{$=$|.} les $T_i$ sont les comp. conn. de $U$]
\margin{NB $U=\emptyset$ sss $I=\emptyset$}
\[
\text{$2^\cir
```

Aligned final span:

```tex
\unsure{$=$|.}
```

Final context (up to 100 characters either side):

```tex
X=\bigcup T_i
\]
\margin{\unsure{un|en} disj.}

Alors

$1^\circ$) $I$ est \unsure{d'unique|unique} [\unsure{$=$|.} les $T_i$ sont les comp. conn. de $U$]
\margin{NB $U=\emptyset$ sss $I=\emptyset$}
\[
\text{$2^\cir
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/019_unique.jpg

Alignment requires recheck: no flag

Review note: The entry stroke before unique and the small bracket mark cannot be distinguished securely.

### C-019-U016 (C line 26)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 27.

Source C token:

```tex
\unsure{\partial U|\partial X}
```

Source C context:

```tex
 comp. conn. de $U$]
\margin{NB $U=\emptyset$ sss $I=\emptyset$}
\[
\text{$2^\circ$)}\quad \deleted{\unsure{\partial U|\partial X}}\deleted{U}X^{\cdot}=\bigcup_{i\in I}T_i^{\cdot}
\]
\[
(\text{donc }\deleted{U}X^{\cdot}=\emptyset\
```

Aligned final span:

```tex
\unsure{\partial U|\partial X}
```

Final context (up to 100 characters either side):

```tex
 comp. conn. de $U$]
\margin{NB $U=\emptyset$ sss $I=\emptyset$}
\[
\text{$2^\circ$)}\quad \deleted{\unsure{\partial U|\partial X}}\deleted{U}X^{\cdot}=\bigcup_{i\in I}T_i^{\cdot}
\]
\[
(\text{donc }\deleted{U}X^{\cdot}=\emptyset\
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/019_unique.jpg; crops/019_definition.jpg

Alignment requires recheck: no flag

Review note: Crossed old U/∂U/∂X, the old empty-set clause and old V remain under later lettering.

### C-019-U017 (C line 29)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 30.

Source C token:

```tex
\unsure{I=\emptyset\ \text{ou}}
```

Source C context:

```tex
p_{i\in I}T_i^{\cdot}
\]
\[
(\text{donc }\deleted{U}X^{\cdot}=\emptyset\quad\text{sss}\quad\deleted{\unsure{I=\emptyset\ \text{ou}}}\quad\deleted{U}X=L\text{ ou }\deleted{U}X=\emptyset
\]
(On dit que $\deleted{\unsure{U}}X$ est une
```

Aligned final span:

```tex
\unsure{I=\emptyset\ \text{ou}}
```

Final context (up to 100 characters either side):

```tex
p_{i\in I}T_i^{\cdot}
\]
\[
(\text{donc }\deleted{U}X^{\cdot}=\emptyset\quad\text{sss}\quad\deleted{\unsure{I=\emptyset\ \text{ou}}}\quad\deleted{U}X=L\text{ ou }\deleted{U}X=\emptyset
\]
(On dit que $\deleted{\unsure{U}}X$ est une
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/019_unique.jpg; crops/019_definition.jpg

Alignment requires recheck: no flag

Review note: Crossed old U/∂U/∂X, the old empty-set clause and old V remain under later lettering.

### C-019-U018 (C line 31)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 32.

Source C token:

```tex
\unsure{U}
```

Source C context:

```tex
\emptyset\ \text{ou}}}\quad\deleted{U}X=L\text{ ou }\deleted{U}X=\emptyset
\]
(On dit que $\deleted{\unsure{U}}X$ est une \uline{partie} \uline{modérée}) \uline{fermée}.

\uline{Def} Si $\deleted{U}X,\deleted{\
```

Aligned final span:

```tex
\unsure{U}
```

Final context (up to 100 characters either side):

```tex
\emptyset\ \text{ou}}}\quad\deleted{U}X=L\text{ ou }\deleted{U}X=\emptyset
\]
(On dit que $\deleted{\unsure{U}}X$ est une \uline{partie} \uline{modérée}) \uline{fermée}.

\uline{Def} Si $\deleted{U}X,\deleted{\
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/019_unique.jpg; crops/019_definition.jpg

Alignment requires recheck: no flag

Review note: Crossed old U/∂U/∂X, the old empty-set clause and old V remain under later lettering.

### C-019-U019 (C line 33)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 34.

Source C token:

```tex
\unsure{V}
```

Source C context:

```tex
}}X$ est une \uline{partie} \uline{modérée}) \uline{fermée}.

\uline{Def} Si $\deleted{U}X,\deleted{\unsure{V}}Y$ sont deux parties \uline{fermées} modérées, on dit que $X$ et $Y$ sont en pos. \unsure{relative|
```

Aligned final span:

```tex
\unsure{V}
```

Final context (up to 100 characters either side):

```tex
}}X$ est une \uline{partie} \uline{modérée}) \uline{fermée}.

\uline{Def} Si $\deleted{U}X,\deleted{\unsure{V}}Y$ sont deux parties \uline{fermées} modérées, on dit que $X$ et $Y$ sont en pos. relative modérée 
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/019_unique.jpg; crops/019_definition.jpg

Alignment requires recheck: no flag

Review note: Crossed old U/∂U/∂X, the old empty-set clause and old V remain under later lettering.

### C-019-U020 (C line 33)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 34.

Source C token:

```tex
\unsure{relative|relation}
```

Source C context:

```tex
eleted{\unsure{V}}Y$ sont deux parties \uline{fermées} modérées, on dit que $X$ et $Y$ sont en pos. \unsure{relative|relation} modérée $X^{\cdot}$ et $Y^{\cdot}$ le sont, i.e
\[
\forall x\in X^{\cdot},\ y\in Y^{\cdot},\ \inser
```

Aligned final span:

```tex
relative
```

Final context (up to 100 characters either side):

```tex
eleted{\unsure{V}}Y$ sont deux parties \uline{fermées} modérées, on dit que $X$ et $Y$ sont en pos. relative modérée $X^{\cdot}$ et $Y^{\cdot}$ le sont, i.e
\[
\forall x\in X^{\cdot},\ y\in Y^{\cdot},\ \inser
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved from ink

Crop links: crops/019_definition.jpg

Alignment requires recheck: no flag

Review note: The complete ending relative is visible.

### C-019-U021 (C line 35)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 36.

Source C token:

```tex
\unsure{a|x}
```

Source C context:

```tex
t}$ et $Y^{\cdot}$ le sont, i.e
\[
\forall x\in X^{\cdot},\ y\in Y^{\cdot},\ \inserted{\text{avec }}\unsure{a|x}\ne y,\ \text{on a }\{x,y\}\in\mathrm{Disp}_2
\]
% margin note written sideways
\margin{\uline{Ex} S
```

Aligned final span:

```tex
a
```

Final context (up to 100 characters either side):

```tex
t}$ et $Y^{\cdot}$ le sont, i.e
\[
\forall x\in X^{\cdot},\ y\in Y^{\cdot},\ \inserted{\text{avec }}a\ne y,\ \text{on a }\{a,y\}\in\mathrm{Drap}_2
\]
% margin note written sideways
\margin{\uline{Ex} S
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved from ink

Crop links: crops/019_last_formula.jpg

Alignment requires recheck: no flag

Review note: The inequality and pair both have a bowl-shaped a, distinct from the quantified crossed x. The variable mismatch is preserved.

### C-019-U022 (C line 38)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 39.

Source C token:

```tex
\unsure{modérées|modérés}
```

Source C context:

```tex
 }\{x,y\}\in\mathrm{Disp}_2
\]
% margin note written sideways
\margin{\uline{Ex} Si $X$ et $Y$ sont \unsure{modérées|modérés}, avec $X\subset Y$, alors $X^{\cdot}\unsure{\subset|\in}Y$ donc tt pt de $X^{\cdot}$ est en pos. re
```

Aligned final span:

```tex
\unsure{modérées|modérés}
```

Final context (up to 100 characters either side):

```tex
 }\{a,y\}\in\mathrm{Drap}_2
\]
% margin note written sideways
\margin{\uline{Ex} Si $X$ et $Y$ sont \unsure{modérées|modérés}, avec $X\subset Y$, alors $X^{\cdot}\subset Y$ donc tt pt de $X^{\cdot}$ est en pos. rel. modérée p
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/019_margin_full.jpg; crops/019_margin_90.jpg

Alignment requires recheck: no flag

Review note: Rotation separates the side note, but the crowded words and ending still overlap the main writing and stay explicitly uncertain.

### C-019-U023 (C line 38)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 39.

Source C token:

```tex
\unsure{\subset|\in}
```

Source C context:

```tex
\margin{\uline{Ex} Si $X$ et $Y$ sont \unsure{modérées|modérés}, avec $X\subset Y$, alors $X^{\cdot}\unsure{\subset|\in}Y$ donc tt pt de $X^{\cdot}$ est en pos. rel. modérée par \unsure{$X$ et $Y$} (\unsure{i.e.|lire} \u
```

Aligned final span:

```tex
\subset 
```

Final context (up to 100 characters either side):

```tex
\margin{\uline{Ex} Si $X$ et $Y$ sont \unsure{modérées|modérés}, avec $X\subset Y$, alors $X^{\cdot}\subset Y$ donc tt pt de $X^{\cdot}$ est en pos. rel. modérée par \unsure{$Y$} (\unsure{i.e.|lire} \unsure{p
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved from ink

Crop links: crops/019_margin_full.jpg

Alignment requires recheck: no flag

Review note: The open two-arm relation is an inclusion sign. Alignment recheck: A TeX command delimiter space was added after subset; the reviewed inclusion remains unchanged.

### C-019-U024 (C line 38)

Mechanical state: **unsure token(s) overlap changed alignment; inspect**. Final aligned line: 39.

Source C token:

```tex
\unsure{$X$ et $Y$}
```

Source C context:

```tex
t Y$, alors $X^{\cdot}\unsure{\subset|\in}Y$ donc tt pt de $X^{\cdot}$ est en pos. rel. modérée par \unsure{$X$ et $Y$} (\unsure{i.e.|lire} \unsure{p.r. à} $Y^{\cdot}$) \unsure{donc} \unsure{sont|sont en} en pos. modéré
```

Aligned final span:

```tex
\unsure{$Y$}
```

Final context (up to 100 characters either side):

```tex
vec $X\subset Y$, alors $X^{\cdot}\subset Y$ donc tt pt de $X^{\cdot}$ est en pos. rel. modérée par \unsure{$Y$} (\unsure{i.e.|lire} \unsure{p.r. à} $Y^{\cdot}$) \unsure{donc} $X$ et $Y$ \unsure{sont|sont en} en 
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: revised placement; uncertainty retained

Crop links: crops/019_margin_full.jpg

Alignment requires recheck: no flag

Review note: The X et Y group belongs to the concluding lower line; only the crowded Y following par belongs at the earlier locus.

### C-019-U025 (C line 38)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 39.

Source C token:

```tex
\unsure{i.e.|lire}
```

Source C context:

```tex
}\unsure{\subset|\in}Y$ donc tt pt de $X^{\cdot}$ est en pos. rel. modérée par \unsure{$X$ et $Y$} (\unsure{i.e.|lire} \unsure{p.r. à} $Y^{\cdot}$) \unsure{donc} \unsure{sont|sont en} en pos. modérée.}

```

Aligned final span:

```tex
\unsure{i.e.|lire}
```

Final context (up to 100 characters either side):

```tex
Y$, alors $X^{\cdot}\subset Y$ donc tt pt de $X^{\cdot}$ est en pos. rel. modérée par \unsure{$Y$} (\unsure{i.e.|lire} \unsure{p.r. à} $Y^{\cdot}$) \unsure{donc} $X$ et $Y$ \unsure{sont|sont en} en pos. modérée.}

% pa
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/019_margin_full.jpg; crops/019_margin_90.jpg

Alignment requires recheck: no flag

Review note: Rotation separates the side note, but the crowded words and ending still overlap the main writing and stay explicitly uncertain.

### C-019-U026 (C line 38)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 39.

Source C token:

```tex
\unsure{p.r. à}
```

Source C context:

```tex
n}Y$ donc tt pt de $X^{\cdot}$ est en pos. rel. modérée par \unsure{$X$ et $Y$} (\unsure{i.e.|lire} \unsure{p.r. à} $Y^{\cdot}$) \unsure{donc} \unsure{sont|sont en} en pos. modérée.}

```

Aligned final span:

```tex
\unsure{p.r. à}
```

Final context (up to 100 characters either side):

```tex
}\subset Y$ donc tt pt de $X^{\cdot}$ est en pos. rel. modérée par \unsure{$Y$} (\unsure{i.e.|lire} \unsure{p.r. à} $Y^{\cdot}$) \unsure{donc} $X$ et $Y$ \unsure{sont|sont en} en pos. modérée.}

% pale vertical wate
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/019_margin_full.jpg; crops/019_margin_90.jpg

Alignment requires recheck: no flag

Review note: Rotation separates the side note, but the crowded words and ending still overlap the main writing and stay explicitly uncertain.

### C-019-U027 (C line 38)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 39.

Source C token:

```tex
\unsure{donc}
```

Source C context:

```tex
$ est en pos. rel. modérée par \unsure{$X$ et $Y$} (\unsure{i.e.|lire} \unsure{p.r. à} $Y^{\cdot}$) \unsure{donc} \unsure{sont|sont en} en pos. modérée.}

```

Aligned final span:

```tex
\unsure{donc}
```

Final context (up to 100 characters either side):

```tex
{\cdot}$ est en pos. rel. modérée par \unsure{$Y$} (\unsure{i.e.|lire} \unsure{p.r. à} $Y^{\cdot}$) \unsure{donc} $X$ et $Y$ \unsure{sont|sont en} en pos. modérée.}

% pale vertical watermark
\rotatebox{90}{\texts
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/019_margin_full.jpg; crops/019_margin_90.jpg

Alignment requires recheck: no flag

Review note: Rotation separates the side note, but the crowded words and ending still overlap the main writing and stay explicitly uncertain.

### C-019-U028 (C line 38)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 39.

Source C token:

```tex
\unsure{sont|sont en}
```

Source C context:

```tex
rel. modérée par \unsure{$X$ et $Y$} (\unsure{i.e.|lire} \unsure{p.r. à} $Y^{\cdot}$) \unsure{donc} \unsure{sont|sont en} en pos. modérée.}

```

Aligned final span:

```tex
\unsure{sont|sont en}
```

Final context (up to 100 characters either side):

```tex
 modérée par \unsure{$Y$} (\unsure{i.e.|lire} \unsure{p.r. à} $Y^{\cdot}$) \unsure{donc} $X$ et $Y$ \unsure{sont|sont en} en pos. modérée.}

% pale vertical watermark
\rotatebox{90}{\textsc{\unsure{ng Extra Strong}}}

```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/019_margin_full.jpg; crops/019_margin_90.jpg

Alignment requires recheck: no flag

Review note: Rotation separates the side note, but the crowded words and ending still overlap the main writing and stay explicitly uncertain.

### C-020-U001 (C line 3)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 3.

Source C token:

```tex
\unsure{Th}
```

Source C context:

```tex
\scanpage{20}\mspage{19}
% slanted
\margin{partie de \deleted{\unsure{Th}} \unsure{th.}}
\deleted{\uline{\unsure{Prop}}}\inserted{\uline{Prop} Soit $X,Y$} Deux parties fermé
```

Aligned final span:

```tex
\unsure{Th}
```

Final context (up to 100 characters either side):

```tex
\scanpage{20}\mspage{19}
% slanted
\margin{partie de \deleted{\unsure{Th}} \unsure{th.}}
\deleted{\uline{\unsure{Prop}}}\inserted{\uline{Prop} Soit $X,Y$} Deux parties fermé
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/020_title_margin.jpg; crops/020_top.jpg

Alignment requires recheck: no flag

Review note: The crossed heading and slanted short labels remain crowded or overwritten.

### C-020-U002 (C line 3)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 3.

Source C token:

```tex
\unsure{th.}
```

Source C context:

```tex
\scanpage{20}\mspage{19}
% slanted
\margin{partie de \deleted{\unsure{Th}} \unsure{th.}}
\deleted{\uline{\unsure{Prop}}}\inserted{\uline{Prop} Soit $X,Y$} Deux parties fermées modérées, \
```

Aligned final span:

```tex
\unsure{th.}
```

Final context (up to 100 characters either side):

```tex
\scanpage{20}\mspage{19}
% slanted
\margin{partie de \deleted{\unsure{Th}} \unsure{th.}}
\deleted{\uline{\unsure{Prop}}}\inserted{\uline{Prop} Soit $X,Y$} Deux parties fermées modérées, e
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/020_title_margin.jpg; crops/020_top.jpg

Alignment requires recheck: no flag

Review note: The crossed heading and slanted short labels remain crowded or overwritten.

### C-020-U003 (C line 4)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 4.

Source C token:

```tex
\unsure{Prop}
```

Source C context:

```tex
page{20}\mspage{19}
% slanted
\margin{partie de \deleted{\unsure{Th}} \unsure{th.}}
\deleted{\uline{\unsure{Prop}}}\inserted{\uline{Prop} Soit $X,Y$} Deux parties fermées modérées, \unsure{en} pos. rel. modérée. A
```

Aligned final span:

```tex
\unsure{Prop}
```

Final context (up to 100 characters either side):

```tex
page{20}\mspage{19}
% slanted
\margin{partie de \deleted{\unsure{Th}} \unsure{th.}}
\deleted{\uline{\unsure{Prop}}}\inserted{\uline{Prop} Soit $X,Y$} Deux parties fermées modérées, en pos. rel. modérée. Alors $X\c
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/020_title_margin.jpg; crops/020_top.jpg

Alignment requires recheck: no flag

Review note: The crossed heading and slanted short labels remain crowded or overwritten.

### C-020-U004 (C line 4)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 4.

Source C token:

```tex
\unsure{en}
```

Source C context:

```tex
}}
\deleted{\uline{\unsure{Prop}}}\inserted{\uline{Prop} Soit $X,Y$} Deux parties fermées modérées, \unsure{en} pos. rel. modérée. Alors $X\cap Y$ est une partie \inserted{fermée} modérée, et
\[
\boxed{(X\cap Y)
```

Aligned final span:

```tex
en
```

Final context (up to 100 characters either side):

```tex
}}
\deleted{\uline{\unsure{Prop}}}\inserted{\uline{Prop} Soit $X,Y$} Deux parties fermées modérées, en pos. rel. modérée. Alors $X\cap Y$ est une partie \inserted{fermée} modérée, et
\[
\boxed{(X\cap Y)
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved from ink

Crop links: crops/020_top.jpg

Alignment requires recheck: no flag

Review note: The two joined en letters, elevated boundary dot and cancelled parmi are legible; De plus stays live around the first formula box.

### C-020-U005 (C line 6)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 6.

Source C token:

```tex
\unsure{\cdot|\prime}
```

Source C context:

```tex
os. rel. modérée. Alors $X\cap Y$ est une partie \inserted{fermée} modérée, et
\[
\boxed{(X\cap Y)^{\unsure{\cdot|\prime}}\subset X^{\cdot}\cup Y^{\cdot}}
\]
De plus, \inserted{$X$ et $Y$ ont une borne sup. \unsure{dans|e
```

Aligned final span:

```tex
\cdot
```

Final context (up to 100 characters either side):

```tex
os. rel. modérée. Alors $X\cap Y$ est une partie \inserted{fermée} modérée, et
\[
\boxed{(X\cap Y)^{\cdot}\subset X^{\cdot}\cup Y^{\cdot}}
\]
De plus, \inserted{$X$ et $Y$ ont une borne sup. \unsure{dans|e
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved from ink

Crop links: crops/020_top.jpg

Alignment requires recheck: no flag

Review note: The two joined en letters, elevated boundary dot and cancelled parmi are legible; De plus stays live around the first formula box.

### C-020-U006 (C line 8)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 8.

Source C token:

```tex
\unsure{dans|en}
```

Source C context:

```tex
{\cdot|\prime}}\subset X^{\cdot}\cup Y^{\cdot}}
\]
De plus, \inserted{$X$ et $Y$ ont une borne sup. \unsure{dans|en}} \deleted{\unsure{parmi} \unsure{toutes les} parties} l'ens des parties modérées ordonnées par \del
```

Aligned final span:

```tex
\unsure{dans|en}
```

Final context (up to 100 characters either side):

```tex
\cap Y)^{\cdot}\subset X^{\cdot}\cup Y^{\cdot}}
\]
De plus, \inserted{$X$ et $Y$ ont une borne sup. \unsure{dans|en}} \deleted{parmi \unsure{toutes les} parties} l'ens des parties modérées ordonnées par \deleted{ferm
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/020_top.jpg

Alignment requires recheck: no flag

Review note: The interlinear preposition and crossed groups remain incompletely separable.

### C-020-U007 (C line 8)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 8.

Source C token:

```tex
\unsure{parmi}
```

Source C context:

```tex
cdot}\cup Y^{\cdot}}
\]
De plus, \inserted{$X$ et $Y$ ont une borne sup. \unsure{dans|en}} \deleted{\unsure{parmi} \unsure{toutes les} parties} l'ens des parties modérées ordonnées par \deleted{fermées modérées qui
```

Aligned final span:

```tex
parmi
```

Final context (up to 100 characters either side):

```tex
cdot}\cup Y^{\cdot}}
\]
De plus, \inserted{$X$ et $Y$ ont une borne sup. \unsure{dans|en}} \deleted{parmi \unsure{toutes les} parties} l'ens des parties modérées ordonnées par \deleted{fermées modérées qui
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved from ink

Crop links: crops/020_top.jpg

Alignment requires recheck: no flag

Review note: The two joined en letters, elevated boundary dot and cancelled parmi are legible; De plus stays live around the first formula box.

### C-020-U008 (C line 8)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 8.

Source C token:

```tex
\unsure{toutes les}
```

Source C context:

```tex
dot}}
\]
De plus, \inserted{$X$ et $Y$ ont une borne sup. \unsure{dans|en}} \deleted{\unsure{parmi} \unsure{toutes les} parties} l'ens des parties modérées ordonnées par \deleted{fermées modérées qui \unsure{contient} $
```

Aligned final span:

```tex
\unsure{toutes les}
```

Final context (up to 100 characters either side):

```tex
cup Y^{\cdot}}
\]
De plus, \inserted{$X$ et $Y$ ont une borne sup. \unsure{dans|en}} \deleted{parmi \unsure{toutes les} parties} l'ens des parties modérées ordonnées par \deleted{fermées modérées qui \unsure{contient} $
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/020_top.jpg

Alignment requires recheck: no flag

Review note: The interlinear preposition and crossed groups remain incompletely separable.

### C-020-U009 (C line 8)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 8.

Source C token:

```tex
\unsure{contient}
```

Source C context:

```tex
\unsure{toutes les} parties} l'ens des parties modérées ordonnées par \deleted{fermées modérées qui \unsure{contient} $X$} l'inclusion.
% slanted
\margin{\deleted{\unsure{Dém}} \uline{Dém} double récurrence sur nb de 
```

Aligned final span:

```tex
\unsure{contient}
```

Final context (up to 100 characters either side):

```tex
\unsure{toutes les} parties} l'ens des parties modérées ordonnées par \deleted{fermées modérées qui \unsure{contient} $X$} l'inclusion.
% slanted
\margin{\deleted{\unsure{D|Dém}} \uline{Dém} double récurrence sur nb d
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/020_top.jpg

Alignment requires recheck: no flag

Review note: The interlinear preposition and crossed groups remain incompletely separable.

### C-020-U010 (C line 10)

Mechanical state: **unsure token(s) overlap changed alignment; inspect**. Final aligned line: 10.

Source C token:

```tex
\unsure{Dém}
```

Source C context:

```tex
es par \deleted{fermées modérées qui \unsure{contient} $X$} l'inclusion.
% slanted
\margin{\deleted{\unsure{Dém}} \uline{Dém} double récurrence sur nb de comp. conn. de $X$ et de $Y$ (pour l'existence du \unsure{
```

Aligned final span:

```tex
\unsure{D|Dém}
```

Final context (up to 100 characters either side):

```tex
es par \deleted{fermées modérées qui \unsure{contient} $X$} l'inclusion.
% slanted
\margin{\deleted{\unsure{D|Dém}} \uline{Dém} double récurrence sur nb de comp. conn. de $X$ et de $Y$ (pour l'existence du Sup et l
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: revised uncertainty

Crop links: crops/020_margin1.jpg

Alignment requires recheck: no flag

Review note: The cancelled heading may be only D rather than the complete Dém; both alternatives are retained.

### C-020-U011 (C line 10)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 10.

Source C token:

```tex
\unsure{Sup|sup}
```

Source C context:

```tex
ure{Dém}} \uline{Dém} double récurrence sur nb de comp. conn. de $X$ et de $Y$ (pour l'existence du \unsure{Sup|sup} et la \unsure{question des frontières})}
\deleted{$X$ et $Y$, et on} On écrit cette partie $X\under
```

Aligned final span:

```tex
Sup
```

Final context (up to 100 characters either side):

```tex
e{D|Dém}} \uline{Dém} double récurrence sur nb de comp. conn. de $X$ et de $Y$ (pour l'existence du Sup et la question des frontières)}
\deleted{$X$ et $Y$, et on} On écrit cette partie $X\underset{\math
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved from ink

Crop links: crops/020_margin1.jpg

Alignment requires recheck: no flag

Review note: The capital S and following up give Sup; question des frontières can be followed through the oblique line.

### C-020-U012 (C line 10)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 10.

Source C token:

```tex
\unsure{question des frontières}
```

Source C context:

```tex
ouble récurrence sur nb de comp. conn. de $X$ et de $Y$ (pour l'existence du \unsure{Sup|sup} et la \unsure{question des frontières})}
\deleted{$X$ et $Y$, et on} On écrit cette partie $X\underset{\mathrm{mod}}{\cup}Y$, On a
\[
\box
```

Aligned final span:

```tex
question des frontières
```

Final context (up to 100 characters either side):

```tex
\uline{Dém} double récurrence sur nb de comp. conn. de $X$ et de $Y$ (pour l'existence du Sup et la question des frontières)}
\deleted{$X$ et $Y$, et on} On écrit cette partie $X\underset{\mathrm{mod}}{\cup}Y$, On a
\[
\box
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved from ink

Crop links: crops/020_margin1.jpg

Alignment requires recheck: no flag

Review note: The capital S and following up give Sup; question des frontières can be followed through the oblique line.

### C-020-U013 (C line 17)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 17.

Source C token:

```tex
\unsure{tte}
```

Source C context:

```tex
 slanted
% Two nearly parallel strokes separate the left notes, immediately above Rem.
\margin{Rem, \unsure{tte} partie modérée $Z$ en pos. rel. \unsure{mod.} avec $X$ et $Y$, l'est aussi avec $X\cap Y$ et $X\und
```

Aligned final span:

```tex
\unsure{tte}
```

Final context (up to 100 characters either side):

```tex
ure}[x=1cm,y=1cm]\draw (0,0)--(2.1,0.03);\draw (0,0.08)--(2.1,0.11);\end{tikzpicture}}
\margin{Rem, \unsure{tte} partie modérée $Z$ en pos. rel. \unsure{mod.} avec $X$ et $Y$, l'est aussi avec $X\cap Y$ et $X\und
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/020_margin2.jpg

Alignment requires recheck: no flag

Review note: The crowded abbreviated groups remain uncertain despite rotation.

### C-020-U014 (C line 17)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 17.

Source C token:

```tex
\unsure{mod.}
```

Source C context:

```tex
te the left notes, immediately above Rem.
\margin{Rem, \unsure{tte} partie modérée $Z$ en pos. rel. \unsure{mod.} avec $X$ et $Y$, l'est aussi avec $X\cap Y$ et $X\underset{\mathrm{mod}}{\cup}Y$}

\uline{Cor} Soit
```

Aligned final span:

```tex
\unsure{mod.}
```

Final context (up to 100 characters either side):

```tex
w (0,0.08)--(2.1,0.11);\end{tikzpicture}}
\margin{Rem, \unsure{tte} partie modérée $Z$ en pos. rel. \unsure{mod.} avec $X$ et $Y$, l'est aussi avec $X\cap Y$ et $X\underset{\mathrm{mod}}{\cup}Y$}

\uline{Cor} Soit
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/020_margin2.jpg

Alignment requires recheck: no flag

Review note: The crowded abbreviated groups remain uncertain despite rotation.

### C-020-U015 (C line 19)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 19.

Source C token:

```tex
\unsure{partie|parties}
```

Source C context:

```tex
ap Y$ et $X\underset{\mathrm{mod}}{\cup}Y$}

\uline{Cor} Soit $(X_i)_{i\in I}$ une famille finie de \unsure{partie|parties} fermées modérées mutuellement en pos. \deleted{rel} modérée. Alors $\bigcap_i X_i$ est une partie m
```

Aligned final span:

```tex
parties
```

Final context (up to 100 characters either side):

```tex
ap Y$ et $X\underset{\mathrm{mod}}{\cup}Y$}

\uline{Cor} Soit $(X_i)_{i\in I}$ une famille finie de parties fermées modérées mutuellement en pos. \deleted{rel} modérée. Alors $\bigcap_i X_i$ est une partie m
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved from ink

Crop links: crops/020_middle.jpg

Alignment requires recheck: no flag

Review note: Plural parties and the full written dans are legible in the corollary.

### C-020-U016 (C line 19)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 19.

Source C token:

```tex
\unsure{ds|dans}
```

Source C context:

```tex
deleted{rel} modérée. Alors $\bigcap_i X_i$ est une partie modérée, et les $X_i$ ont une borne sup. \unsure{ds|dans} l'ens des parties fermées modérées. On a
% slanted
\margin{\uline{Attention} pour une partie \uline
```

Aligned final span:

```tex
dans
```

Final context (up to 100 characters either side):

```tex
deleted{rel} modérée. Alors $\bigcap_i X_i$ est une partie modérée, et les $X_i$ ont une borne sup. dans l'ens des parties fermées modérées. On a
% slanted
\margin{\uline{Attention} pour une partie \uline
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved from ink

Crop links: crops/020_middle.jpg

Alignment requires recheck: no flag

Review note: Plural parties and the full written dans are legible in the corollary.

### C-020-U017 (C line 21)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 21.

Source C token:

```tex
\unsure{quelc|seule}
```

Source C context:

```tex
l'ens des parties fermées modérées. On a
% slanted
\margin{\uline{Attention} pour une partie \uline{\unsure{quelc|seule}} $A$ de $\unsure{L|\mathscr{L}}$, il n'y a \uline{pas} en général d'\unsure{adh.} modérée fermée, i
```

Aligned final span:

```tex
quelc
```

Final context (up to 100 characters either side):

```tex
l'ens des parties fermées modérées. On a
% slanted
\margin{\uline{Attention} pour une partie \uline{quelc} $A$ de $\mathcal L$, il n'y a \uline{pas} en général d'adh. modérée fermée, i.e. de ``plus petit''
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved from ink

Crop links: crops/020_margin3.jpg

Alignment requires recheck: no flag

Review note: The underlined quelc, looped ground-set L, adh., f. and initial closed zero are supported by the rotated margin.

### C-020-U018 (C line 21)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 21.

Source C token:

```tex
\unsure{L|\mathscr{L}}
```

Source C context:

```tex
rées. On a
% slanted
\margin{\uline{Attention} pour une partie \uline{\unsure{quelc|seule}} $A$ de $\unsure{L|\mathscr{L}}$, il n'y a \uline{pas} en général d'\unsure{adh.} modérée fermée, i.e. de ``plus petit'' ens \unsur
```

Aligned final span:

```tex
\mathcal L
```

Final context (up to 100 characters either side):

```tex
es fermées modérées. On a
% slanted
\margin{\uline{Attention} pour une partie \uline{quelc} $A$ de $\mathcal L$, il n'y a \uline{pas} en général d'adh. modérée fermée, i.e. de ``plus petit'' ens f. modéré $X$ t
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved from ink

Crop links: crops/020_margin3.jpg

Alignment requires recheck: no flag

Review note: The underlined quelc, looped ground-set L, adh., f. and initial closed zero are supported by the rotated margin.

### C-020-U019 (C line 21)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 21.

Source C token:

```tex
\unsure{adh.}
```

Source C context:

```tex
tie \uline{\unsure{quelc|seule}} $A$ de $\unsure{L|\mathscr{L}}$, il n'y a \uline{pas} en général d'\unsure{adh.} modérée fermée, i.e. de ``plus petit'' ens \unsure{f.} modéré $X$ tel que $X\supset A$. C'est déjà 
```

Aligned final span:

```tex
adh.
```

Final context (up to 100 characters either side):

```tex
ine{Attention} pour une partie \uline{quelc} $A$ de $\mathcal L$, il n'y a \uline{pas} en général d'adh. modérée fermée, i.e. de ``plus petit'' ens f. modéré $X$ tel que $X\supset A$. C'est déjà faux ds l
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved from ink

Crop links: crops/020_margin3.jpg

Alignment requires recheck: no flag

Review note: The underlined quelc, looped ground-set L, adh., f. and initial closed zero are supported by the rotated margin.

### C-020-U020 (C line 21)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 21.

Source C token:

```tex
\unsure{f.}
```

Source C context:

```tex
cr{L}}$, il n'y a \uline{pas} en général d'\unsure{adh.} modérée fermée, i.e. de ``plus petit'' ens \unsure{f.} modéré $X$ tel que $X\supset A$. C'est déjà faux ds le cas standart $L=[0,1]$ ! (Prendre $A=\{\unsu
```

Aligned final span:

```tex
f.
```

Final context (up to 100 characters either side):

```tex
 de $\mathcal L$, il n'y a \uline{pas} en général d'adh. modérée fermée, i.e. de ``plus petit'' ens f. modéré $X$ tel que $X\supset A$. C'est déjà faux ds le cas standart $L=[0,1]$ ! (Prendre $A=\{0,1/2
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved from ink

Crop links: crops/020_margin3.jpg

Alignment requires recheck: no flag

Review note: The underlined quelc, looped ground-set L, adh., f. and initial closed zero are supported by the rotated margin.

### C-020-U021 (C line 21)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 21.

Source C token:

```tex
\unsure{0|1}
```

Source C context:

```tex
e{f.} modéré $X$ tel que $X\supset A$. C'est déjà faux ds le cas standart $L=[0,1]$ ! (Prendre $A=\{\unsure{0|1},1/2,1/3\ldots\}$}
\[
\left(\bigcup_{\substack{\mathrm{mod}\\ i}} X_i\right)^{\cdot}\subset\bigcup_i
```

Aligned final span:

```tex
0
```

Final context (up to 100 characters either side):

```tex
ns f. modéré $X$ tel que $X\supset A$. C'est déjà faux ds le cas standart $L=[0,1]$ ! (Prendre $A=\{0,1/2,1/3\ldots\}$}
\[
\left(\bigcup_{\substack{\mathrm{mod}\\ i}} X_i\right)^{\cdot}\subset\bigcup_i
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved from ink

Crop links: crops/020_margin3.jpg

Alignment requires recheck: no flag

Review note: The underlined quelc, looped ground-set L, adh., f. and initial closed zero are supported by the rotated margin.

### C-020-U022 (C line 34)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 34.

Source C token:

```tex
\unsure{prendre|quand}
```

Source C context:

```tex
}
\[
[a,b]\underset{\mathrm{mod}}{\cup}[b,c]=[a,c]
\]
mais en général
\[
[a,b]\cup[b,c]\ne[a,c]
\]
(\unsure{prendre|quand} $a$ plus \unsure{c|e} petit élément, $c$ plus grand élément \deleted{\unsure{et}} \unsure{qqconq} \
```

Aligned final span:

```tex
\unsure{prendre|quand}
```

Final context (up to 100 characters either side):

```tex
}
\[
[a,b]\underset{\mathrm{mod}}{\cup}[b,c]=[a,c]
\]
mais en général
\[
[a,b]\cup[b,c]\ne[a,c]
\]
(\unsure{prendre|quand} $a$ plus \unsure{c|e} petit élément, $c$ plus grand élément \deleted{\unsure{et}} \unsure{qqconq} \
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/020_bottom.jpg

Alignment requires recheck: no flag

Review note: The last lines are clipped and heavily revised; the extra short letter before petit and old crossed words remain explicit doubts.

### C-020-U023 (C line 34)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 34.

Source C token:

```tex
\unsure{c|e}
```

Source C context:

```tex
}{\cup}[b,c]=[a,c]
\]
mais en général
\[
[a,b]\cup[b,c]\ne[a,c]
\]
(\unsure{prendre|quand} $a$ plus \unsure{c|e} petit élément, $c$ plus grand élément \deleted{\unsure{et}} \unsure{qqconq} \deleted{\unsure{Et en 
```

Aligned final span:

```tex
\unsure{c|e}
```

Final context (up to 100 characters either side):

```tex
}{\cup}[b,c]=[a,c]
\]
mais en général
\[
[a,b]\cup[b,c]\ne[a,c]
\]
(\unsure{prendre|quand} $a$ plus \unsure{c|e} petit élément, $c$ plus grand élément \deleted{\unsure{et}} \unsure{qqconq} \deleted{\unsure{Et en 
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/020_bottom.jpg

Alignment requires recheck: no flag

Review note: The last lines are clipped and heavily revised; the extra short letter before petit and old crossed words remain explicit doubts.

### C-020-U024 (C line 34)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 34.

Source C token:

```tex
\unsure{et}
```

Source C context:

```tex
,c]
\]
(\unsure{prendre|quand} $a$ plus \unsure{c|e} petit élément, $c$ plus grand élément \deleted{\unsure{et}} \unsure{qqconq} \deleted{\unsure{Et en ce} $\unsure{=}$}, $b$ \deleted{\unsure{est}} comp. à tout 
```

Aligned final span:

```tex
\unsure{et}
```

Final context (up to 100 characters either side):

```tex
,c]
\]
(\unsure{prendre|quand} $a$ plus \unsure{c|e} petit élément, $c$ plus grand élément \deleted{\unsure{et}} \unsure{qqconq} \deleted{\unsure{Et en ce} $\unsure{=}$}, $b$ \deleted{\unsure{est}} comp. à tout 
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/020_bottom.jpg

Alignment requires recheck: no flag

Review note: The last lines are clipped and heavily revised; the extra short letter before petit and old crossed words remain explicit doubts.

### C-020-U025 (C line 34)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 34.

Source C token:

```tex
\unsure{qqconq}
```

Source C context:

```tex
re{prendre|quand} $a$ plus \unsure{c|e} petit élément, $c$ plus grand élément \deleted{\unsure{et}} \unsure{qqconq} \deleted{\unsure{Et en ce} $\unsure{=}$}, $b$ \deleted{\unsure{est}} comp. à tout \inserted{élément
```

Aligned final span:

```tex
\unsure{qqconq}
```

Final context (up to 100 characters either side):

```tex
re{prendre|quand} $a$ plus \unsure{c|e} petit élément, $c$ plus grand élément \deleted{\unsure{et}} \unsure{qqconq} \deleted{\unsure{Et en ce} $\unsure{=}$}, $b$ \deleted{\unsure{est}} comp. à tout \inserted{élément
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/020_bottom.jpg

Alignment requires recheck: no flag

Review note: The last lines are clipped and heavily revised; the extra short letter before petit and old crossed words remain explicit doubts.

### C-020-U026 (C line 34)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 34.

Source C token:

```tex
\unsure{Et en ce}
```

Source C context:

```tex
s \unsure{c|e} petit élément, $c$ plus grand élément \deleted{\unsure{et}} \unsure{qqconq} \deleted{\unsure{Et en ce} $\unsure{=}$}, $b$ \deleted{\unsure{est}} comp. à tout \inserted{élément de $L$.} Si c'est

```

Aligned final span:

```tex
\unsure{Et en ce}
```

Final context (up to 100 characters either side):

```tex
s \unsure{c|e} petit élément, $c$ plus grand élément \deleted{\unsure{et}} \unsure{qqconq} \deleted{\unsure{Et en ce} $\unsure{=}$}, $b$ \deleted{\unsure{est}} comp. à tout \inserted{élément de $\mathcal L$.} Si c'est
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/020_bottom.jpg

Alignment requires recheck: no flag

Review note: The last lines are clipped and heavily revised; the extra short letter before petit and old crossed words remain explicit doubts.

### C-020-U027 (C line 34)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 34.

Source C token:

```tex
\unsure{=}
```

Source C context:

```tex
t élément, $c$ plus grand élément \deleted{\unsure{et}} \unsure{qqconq} \deleted{\unsure{Et en ce} $\unsure{=}$}, $b$ \deleted{\unsure{est}} comp. à tout \inserted{élément de $L$.} Si c'est

```

Aligned final span:

```tex
\unsure{=}
```

Final context (up to 100 characters either side):

```tex
t élément, $c$ plus grand élément \deleted{\unsure{et}} \unsure{qqconq} \deleted{\unsure{Et en ce} $\unsure{=}$}, $b$ \deleted{\unsure{est}} comp. à tout \inserted{élément de $\mathcal L$.} Si c'est

% pale ver
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/020_bottom.jpg

Alignment requires recheck: no flag

Review note: The last lines are clipped and heavily revised; the extra short letter before petit and old crossed words remain explicit doubts.

### C-020-U028 (C line 34)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 34.

Source C token:

```tex
\unsure{est}
```

Source C context:

```tex
lément \deleted{\unsure{et}} \unsure{qqconq} \deleted{\unsure{Et en ce} $\unsure{=}$}, $b$ \deleted{\unsure{est}} comp. à tout \inserted{élément de $L$.} Si c'est

```

Aligned final span:

```tex
\unsure{est}
```

Final context (up to 100 characters either side):

```tex
lément \deleted{\unsure{et}} \unsure{qqconq} \deleted{\unsure{Et en ce} $\unsure{=}$}, $b$ \deleted{\unsure{est}} comp. à tout \inserted{élément de $\mathcal L$.} Si c'est

% pale vertical watermark
\rotatebox{90
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/020_bottom.jpg

Alignment requires recheck: no flag

Review note: The last lines are clipped and heavily revised; the extra short letter before petit and old crossed words remain explicit doubts.

### C-021-U001 (C line 2)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 2.

Source C token:

```tex
\unsure{L|\mathscr{L}}
```

Source C context:

```tex
\scanpage{21}\mspage{20}
vrai pour tt $b$, alors $\unsure{L|\mathscr{L}}$ est \unsure{ttt|tt} ordonné. Plus \unsure{précisém$^{\mathrm t}$|précisément|généralem$^{\mathrm t
```

Aligned final span:

```tex
\mathcal L
```

Final context (up to 100 characters either side):

```tex
\scanpage{21}\mspage{20}
vrai pour tt $b$, alors $\mathcal L$ est \unsure{ttt|tt} ordonné. Plus précisém$^{\mathrm t}$, pour que $\mathcal L$ ttt ordonné, il f 
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved from ink

Crop links: crops/021_top.jpg

Alignment requires recheck: no flag

Review note: The ground-set L is looped; précisém has a separately elevated final t, with no initial général group.

### C-021-U002 (C line 2)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 2.

Source C token:

```tex
\unsure{ttt|tt}
```

Source C context:

```tex
\scanpage{21}\mspage{20}
vrai pour tt $b$, alors $\unsure{L|\mathscr{L}}$ est \unsure{ttt|tt} ordonné. Plus \unsure{précisém$^{\mathrm t}$|précisément|généralem$^{\mathrm t}$}, pour que $L$ ttt
```

Aligned final span:

```tex
\unsure{ttt|tt}
```

Final context (up to 100 characters either side):

```tex
\scanpage{21}\mspage{20}
vrai pour tt $b$, alors $\mathcal L$ est \unsure{ttt|tt} ordonné. Plus précisém$^{\mathrm t}$, pour que $\mathcal L$ ttt ordonné, il f et s. que pour tt $b\
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/021_top.jpg

Alignment requires recheck: no flag

Review note: The compact repeated t strokes cannot be counted securely.

### C-021-U003 (C line 2)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 2.

Source C token:

```tex
\unsure{précisém$^{\mathrm t}$|précisément|généralem$^{\mathrm t}$}
```

Source C context:

```tex
e{21}\mspage{20}
vrai pour tt $b$, alors $\unsure{L|\mathscr{L}}$ est \unsure{ttt|tt} ordonné. Plus \unsure{précisém$^{\mathrm t}$|précisément|généralem$^{\mathrm t}$}, pour que $L$ ttt ordonné, il f et s. que pour tt $b\in L$, $b$ soit comparable à tt autre élément,
```

Aligned final span:

```tex
précisém$^{\mathrm t}$
```

Final context (up to 100 characters either side):

```tex
\scanpage{21}\mspage{20}
vrai pour tt $b$, alors $\mathcal L$ est \unsure{ttt|tt} ordonné. Plus précisém$^{\mathrm t}$, pour que $\mathcal L$ ttt ordonné, il f et s. que pour tt $b\in\mathcal L$, $b$ soit comparable à 
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved from ink

Crop links: crops/021_top.jpg

Alignment requires recheck: no flag

Review note: The ground-set L is looped; précisém has a separately elevated final t, with no initial général group.

### C-021-U004 (C line 10)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 10.

Source C token:

```tex
\unsure{ent}
```

Source C context:

```tex

\begin{center}\rule{2.5cm}{0.35pt}\end{center}

Partie loc. fermée modérée

\uline{Th} Soi\deleted{\unsure{ent}}t $X\deleted{\unsure{\subset|\supset}},Y$ deux parties fermées modérées, avec $X\supset Y$ (donc $X
```

Aligned final span:

```tex
\unsure{ent}
```

Final context (up to 100 characters either side):

```tex

\begin{center}\rule{2.5cm}{0.35pt}\end{center}

Partie loc. fermée modérée

\uline{Th} Soi\deleted{\unsure{ent}}t $X\deleted{\unsure{\subset|\supset}},Y$ deux parties fermées modérées, avec $X\supset Y$ (donc $X
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/021_theorem.jpg

Alignment requires recheck: no flag

Review note: The plural ending, old inclusion and old complement sign are cancelled or overwritten.

### C-021-U005 (C line 10)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 10.

Source C token:

```tex
\unsure{\subset|\supset}
```

Source C context:

```tex
}{0.35pt}\end{center}

Partie loc. fermée modérée

\uline{Th} Soi\deleted{\unsure{ent}}t $X\deleted{\unsure{\subset|\supset}},Y$ deux parties fermées modérées, avec $X\supset Y$ (donc $X$ et $Y$ en pos. relative modérée)
\de
```

Aligned final span:

```tex
\unsure{\subset|\supset}
```

Final context (up to 100 characters either side):

```tex
}{0.35pt}\end{center}

Partie loc. fermée modérée

\uline{Th} Soi\deleted{\unsure{ent}}t $X\deleted{\unsure{\subset|\supset}},Y$ deux parties fermées modérées, avec $X\supset Y$ (donc $X$ et $Y$ en pos. \unsure{relation|rela
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/021_theorem.jpg

Alignment requires recheck: no flag

Review note: The plural ending, old inclusion and old complement sign are cancelled or overwritten.

### C-021-U006 (C line 14)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 14.

Source C token:

```tex
\unsure{\complement_X|C_X|\partial X}
```

Source C context:

```tex
s$ une plus petite partie fermée modérée \inserted{$Z$} contenant $X\setminus Y$.}
Soit
\[
\deleted{\unsure{\complement_X|C_X|\partial X}} C_{\mathrm{mod}}(Y,X)=\left\{x\in X\ \middle|\ 
\begin{aligned}&x\notin Y,\ x\text{ en pos. rel.}\
```

Aligned final span:

```tex
\unsure{\complement_X|C_X|\partial X}
```

Final context (up to 100 characters either side):

```tex
s$ une plus petite partie fermée modérée \inserted{$Z$} contenant $X\setminus Y$.}
Soit
\[
\deleted{\unsure{\complement_X|C_X|\partial X}} C_{\mathrm{mod}}(Y,X)=\left\{x\in X\ \middle|\ 
\begin{aligned}&x\notin Y,\ x\text{ en pos. rel.}\
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/021_theorem.jpg

Alignment requires recheck: no flag

Review note: The plural ending, old inclusion and old complement sign are cancelled or overwritten.

### C-021-U007 (C line 17)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 17.

Source C token:

```tex
\unsure{contenant}
```

Source C context:

```tex
}Y\end{aligned}\right\}
\]
Alors $\exists$ plus petit ens. fermé modéré $Z$ \deleted{tel} \inserted{\unsure{contenant}} \deleted{\unsure{tt|te}} $C_{\mathrm{mod}}(Y,X)$, \deleted{\unsure{a}}\inserted{Ce} $Z$ \inserted{
```

Aligned final span:

```tex
\unsure{contenant}
```

Final context (up to 100 characters either side):

```tex
}Y\end{aligned}\right\}
\]
Alors $\exists$ plus petit ens. fermé modéré $Z$ \deleted{tel} \inserted{\unsure{contenant}} \deleted{\unsure{tt|te}} $C_{\mathrm{mod}}(Y,X)$, \deleted{\unsure{a}}\inserted{Ce} $Z$ \inserted{
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/021_end.jpg

Alignment requires recheck: no flag

Review note: The interlinear containing-word, cancelled short forms and added relative-position abbreviation remain crowded by revision strokes.

### C-021-U008 (C line 17)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 17.

Source C token:

```tex
\unsure{tt|te}
```

Source C context:

```tex
ors $\exists$ plus petit ens. fermé modéré $Z$ \deleted{tel} \inserted{\unsure{contenant}} \deleted{\unsure{tt|te}} $C_{\mathrm{mod}}(Y,X)$, \deleted{\unsure{a}}\inserted{Ce} $Z$ \inserted{est $\subset X$, et} cont
```

Aligned final span:

```tex
\unsure{tt|te}
```

Final context (up to 100 characters either side):

```tex
ors $\exists$ plus petit ens. fermé modéré $Z$ \deleted{tel} \inserted{\unsure{contenant}} \deleted{\unsure{tt|te}} $C_{\mathrm{mod}}(Y,X)$, \deleted{\unsure{a}}\inserted{Ce} $Z$ \inserted{est $\subset X$, et} cont
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/021_end.jpg

Alignment requires recheck: no flag

Review note: The interlinear containing-word, cancelled short forms and added relative-position abbreviation remain crowded by revision strokes.

### C-021-U009 (C line 17)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 17.

Source C token:

```tex
\unsure{a}
```

Source C context:

```tex
leted{tel} \inserted{\unsure{contenant}} \deleted{\unsure{tt|te}} $C_{\mathrm{mod}}(Y,X)$, \deleted{\unsure{a}}\inserted{Ce} $Z$ \inserted{est $\subset X$, et} contient \deleted{\unsure{tt}} partie fermée modér
```

Aligned final span:

```tex
\unsure{a}
```

Final context (up to 100 characters either side):

```tex
leted{tel} \inserted{\unsure{contenant}} \deleted{\unsure{tt|te}} $C_{\mathrm{mod}}(Y,X)$, \deleted{\unsure{a}}\inserted{Ce} $Z$ \inserted{est $\subset X$, et} contient \deleted{\unsure{tt}} partie fermée modér
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/021_end.jpg

Alignment requires recheck: no flag

Review note: The interlinear containing-word, cancelled short forms and added relative-position abbreviation remain crowded by revision strokes.

### C-021-U010 (C line 17)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 17.

Source C token:

```tex
\unsure{tt}
```

Source C context:

```tex
mod}}(Y,X)$, \deleted{\unsure{a}}\inserted{Ce} $Z$ \inserted{est $\subset X$, et} contient \deleted{\unsure{tt}} partie fermée modérée $T$ de $L$ telle que $T\subset X$, $T\cap Y=\emptyset$, $T$ en pos. rel. mod
```

Aligned final span:

```tex
\unsure{tt}
```

Final context (up to 100 characters either side):

```tex
mod}}(Y,X)$, \deleted{\unsure{a}}\inserted{Ce} $Z$ \inserted{est $\subset X$, et} contient \deleted{\unsure{tt}} partie fermée modérée $T$ de $\mathcal L$ telle que $T\subset X$, $T\cap Y=\emptyset$, $T$ en pos.
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/021_end.jpg

Alignment requires recheck: no flag

Review note: The interlinear containing-word, cancelled short forms and added relative-position abbreviation remain crowded by revision strokes.

### C-021-U011 (C line 17)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 17.

Source C token:

```tex
\unsure{rapt|rel.}
```

Source C context:

```tex
modérée $T$ de $L$ telle que $T\subset X$, $T\cap Y=\emptyset$, $T$ en pos. rel. mod par. \inserted{\unsure{rapt|rel.}} à $Y$, \inserted{\unsure{De plus}} $Z$ est en position modérée avec $Y$.
% slanted
\margin{\uline{
```

Aligned final span:

```tex
\unsure{rapt|rel.}
```

Final context (up to 100 characters either side):

```tex
T$ de $\mathcal L$ telle que $T\subset X$, $T\cap Y=\emptyset$, $T$ en pos. rel. mod par. \inserted{\unsure{rapt|rel.}} à $Y$, \inserted{De plus} $Z$ est en position modérée avec $Y$.
% slanted
\margin{\uline{On pose} 
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/021_end.jpg

Alignment requires recheck: no flag

Review note: The interlinear containing-word, cancelled short forms and added relative-position abbreviation remain crowded by revision strokes.

### C-021-U012 (C line 17)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 17.

Source C token:

```tex
\unsure{De plus}
```

Source C context:

```tex
t X$, $T\cap Y=\emptyset$, $T$ en pos. rel. mod par. \inserted{\unsure{rapt|rel.}} à $Y$, \inserted{\unsure{De plus}} $Z$ est en position modérée avec $Y$.
% slanted
\margin{\uline{On pose} $Z=X\underset{\mathrm{mod}
```

Aligned final span:

```tex
De plus
```

Final context (up to 100 characters either side):

```tex
t X$, $T\cap Y=\emptyset$, $T$ en pos. rel. mod par. \inserted{\unsure{rapt|rel.}} à $Y$, \inserted{De plus} $Z$ est en position modérée avec $Y$.
% slanted
\margin{\uline{On pose} $Z=X\underset{\mathrm{mod}
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved from ink

Crop links: crops/021_end.jpg

Alignment requires recheck: no flag

Review note: The elevated De plus is read as a live insertion introducing Z est; surrounding strokes are the overlapping baseline and retraced Z.

### C-022-U001 (C line 2)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 2.

Source C token:

```tex
\unsure{S|J}
```

Source C context:

```tex
\scanpage{22}\mspage{21}
Si on pose $\deleted{\unsure{S|J}}F=$ frontière relative de $Y$ dans $X$, \deleted{\unsure{c.} F} Alors $F$ est fini, \inserted{modér
```

Aligned final span:

```tex
\unsure{S|J}
```

Final context (up to 100 characters either side):

```tex
\scanpage{22}\mspage{21}
Si on pose $\deleted{\unsure{S|J}}F=$ frontière relative de $Y$ dans $X$, \deleted{\unsure{c.} F} Alors $F$ est fini, \inserted{modér
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/022_top.jpg

Alignment requires recheck: no flag

Review note: The old initials and crossed fragments remain obscured by revision; no reading is supplied from the formula.

### C-022-U002 (C line 2)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 2.

Source C token:

```tex
\unsure{c.}
```

Source C context:

```tex
e{22}\mspage{21}
Si on pose $\deleted{\unsure{S|J}}F=$ frontière relative de $Y$ dans $X$, \deleted{\unsure{c.} F} Alors $F$ est fini, \inserted{modéré,} en pos. mod. \unsure{p.r.} à $Y$, \deleted{\unsure{dans}}
```

Aligned final span:

```tex
\unsure{c.}
```

Final context (up to 100 characters either side):

```tex
e{22}\mspage{21}
Si on pose $\deleted{\unsure{S|J}}F=$ frontière relative de $Y$ dans $X$, \deleted{\unsure{c.} F} Alors $F$ est fini, \inserted{modéré,} en pos. mod. p.r. à $Y$, \deleted{\unsure{donc|dans}} $F\
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/022_top.jpg

Alignment requires recheck: no flag

Review note: The old initials and crossed fragments remain obscured by revision; no reading is supplied from the formula.

### C-022-U003 (C line 2)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 2.

Source C token:

```tex
\unsure{p.r.}
```

Source C context:

```tex
lative de $Y$ dans $X$, \deleted{\unsure{c.} F} Alors $F$ est fini, \inserted{modéré,} en pos. mod. \unsure{p.r.} à $Y$, \deleted{\unsure{dans}} $F\subset Z$, \deleted{$\unsure{F\cap Z}$} \deleted{\unsure{est}} $F
```

Aligned final span:

```tex
p.r.
```

Final context (up to 100 characters either side):

```tex
lative de $Y$ dans $X$, \deleted{\unsure{c.} F} Alors $F$ est fini, \inserted{modéré,} en pos. mod. p.r. à $Y$, \deleted{\unsure{donc|dans}} $F\subset Z$, \deleted{$\unsure{F\cap Z}$} \deleted{\unsure{est
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved from ink

Crop links: crops/022_top.jpg

Alignment requires recheck: no flag

Review note: The separate p.r. abbreviation and crossed Comp letter shapes are readable.

### C-022-U004 (C line 2)

Mechanical state: **unsure token(s) overlap changed alignment; inspect**. Final aligned line: 2.

Source C token:

```tex
\unsure{dans}
```

Source C context:

```tex
ed{\unsure{c.} F} Alors $F$ est fini, \inserted{modéré,} en pos. mod. \unsure{p.r.} à $Y$, \deleted{\unsure{dans}} $F\subset Z$, \deleted{$\unsure{F\cap Z}$} \deleted{\unsure{est}} $F$ ne \deleted{$\unsure{Z}$} co
```

Aligned final span:

```tex
\unsure{donc|dans}
```

Final context (up to 100 characters either side):

```tex
$, \deleted{\unsure{c.} F} Alors $F$ est fini, \inserted{modéré,} en pos. mod. p.r. à $Y$, \deleted{\unsure{donc|dans}} $F\subset Z$, \deleted{$\unsure{F\cap Z}$} \deleted{\unsure{est}} $F$ ne \deleted{$\unsure{Z}$} co
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: expanded alternatives

Crop links: crops/022_top.jpg

Alignment requires recheck: no flag

Review note: The crossed short word may be donc or dans; the middle letter is obscured, so the additional alternative is explicit.

### C-022-U005 (C line 2)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 2.

Source C token:

```tex
\unsure{F\cap Z}
```

Source C context:

```tex
inserted{modéré,} en pos. mod. \unsure{p.r.} à $Y$, \deleted{\unsure{dans}} $F\subset Z$, \deleted{$\unsure{F\cap Z}$} \deleted{\unsure{est}} $F$ ne \deleted{$\unsure{Z}$} contient pas de pts isolé de $Z$.
\deleted{e
```

Aligned final span:

```tex
\unsure{F\cap Z}
```

Final context (up to 100 characters either side):

```tex
i, \inserted{modéré,} en pos. mod. p.r. à $Y$, \deleted{\unsure{donc|dans}} $F\subset Z$, \deleted{$\unsure{F\cap Z}$} \deleted{\unsure{est}} $F$ ne \deleted{$\unsure{Z}$} contient pas de pts isolé de $Z$.
\deleted{e
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/022_top.jpg

Alignment requires recheck: no flag

Review note: The old initials and crossed fragments remain obscured by revision; no reading is supplied from the formula.

### C-022-U006 (C line 2)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 2.

Source C token:

```tex
\unsure{est}
```

Source C context:

```tex
d. \unsure{p.r.} à $Y$, \deleted{\unsure{dans}} $F\subset Z$, \deleted{$\unsure{F\cap Z}$} \deleted{\unsure{est}} $F$ ne \deleted{$\unsure{Z}$} contient pas de pts isolé de $Z$.
\deleted{et on a}
\[
\deleted{\uns
```

Aligned final span:

```tex
\unsure{est}
```

Final context (up to 100 characters either side):

```tex
. mod. p.r. à $Y$, \deleted{\unsure{donc|dans}} $F\subset Z$, \deleted{$\unsure{F\cap Z}$} \deleted{\unsure{est}} $F$ ne \deleted{$\unsure{Z}$} contient pas de pts isolé de $Z$.
\deleted{et on a}
\[
\deleted{\mat
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/022_top.jpg

Alignment requires recheck: no flag

Review note: The old initials and crossed fragments remain obscured by revision; no reading is supplied from the formula.

### C-022-U007 (C line 2)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 2.

Source C token:

```tex
\unsure{Z}
```

Source C context:

```tex
d{\unsure{dans}} $F\subset Z$, \deleted{$\unsure{F\cap Z}$} \deleted{\unsure{est}} $F$ ne \deleted{$\unsure{Z}$} contient pas de pts isolé de $Z$.
\deleted{et on a}
\[
\deleted{\unsure{\mathrm{Comp}}}\ C_{\math
```

Aligned final span:

```tex
\unsure{Z}
```

Final context (up to 100 characters either side):

```tex
sure{donc|dans}} $F\subset Z$, \deleted{$\unsure{F\cap Z}$} \deleted{\unsure{est}} $F$ ne \deleted{$\unsure{Z}$} contient pas de pts isolé de $Z$.
\deleted{et on a}
\[
\deleted{\mathrm{Comp}}\ C_{\mathrm{mod}}(
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/022_top.jpg

Alignment requires recheck: no flag

Review note: The old initials and crossed fragments remain obscured by revision; no reading is supplied from the formula.

### C-022-U008 (C line 5)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 5.

Source C token:

```tex
\unsure{\mathrm{Comp}}
```

Source C context:

```tex
est}} $F$ ne \deleted{$\unsure{Z}$} contient pas de pts isolé de $Z$.
\deleted{et on a}
\[
\deleted{\unsure{\mathrm{Comp}}}\ C_{\mathrm{mod}}(Y,X)=C_{\mathrm{mod}}(\deleted{\unsure{Z}}F,Z)
\]
\figure{\tikz{\draw (0,0) .. c
```

Aligned final span:

```tex
\mathrm{Comp}
```

Final context (up to 100 characters either side):

```tex
est}} $F$ ne \deleted{$\unsure{Z}$} contient pas de pts isolé de $Z$.
\deleted{et on a}
\[
\deleted{\mathrm{Comp}}\ C_{\mathrm{mod}}(Y,X)=C_{\mathrm{mod}}(\deleted{\unsure{Z}}F,Z)
\]
\figure{\tikz{\draw (0,0) .. c
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved from ink

Crop links: crops/022_top.jpg

Alignment requires recheck: no flag

Review note: The separate p.r. abbreviation and crossed Comp letter shapes are readable.

### C-022-U009 (C line 5)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 5.

Source C token:

```tex
\unsure{Z}
```

Source C context:

```tex
leted{et on a}
\[
\deleted{\unsure{\mathrm{Comp}}}\ C_{\mathrm{mod}}(Y,X)=C_{\mathrm{mod}}(\deleted{\unsure{Z}}F,Z)
\]
\figure{\tikz{\draw (0,0) .. controls (.07,.02) and (.15,.10) .. (.21,.08) .. controls (.24
```

Aligned final span:

```tex
\unsure{Z}
```

Final context (up to 100 characters either side):

```tex
 $Z$.
\deleted{et on a}
\[
\deleted{\mathrm{Comp}}\ C_{\mathrm{mod}}(Y,X)=C_{\mathrm{mod}}(\deleted{\unsure{Z}}F,Z)
\]
\figure{\tikz{\draw (0,0) .. controls (.07,.02) and (.15,.10) .. (.21,.08) .. controls (.24
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/022_top.jpg

Alignment requires recheck: no flag

Review note: The old initials and crossed fragments remain obscured by revision; no reading is supplied from the formula.

### C-022-U010 (C line 9)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 9.

Source C token:

```tex
\unsure{L|\mathscr{L}}
```

Source C context:

```tex
 (3.32,.12) .. (3.42,.06) .. controls (3.50,-.08) and (3.80,-.02) .. (4.10,-.01);}}

(9 juin) Soit $\unsure{L|\mathscr{L}}$ un tronçon ordonné.

\deleted{Un sous-segment \unsure{d'un|dans} \uline{sous-tronçon} \uline{fermé
```

Aligned final span:

```tex
\mathcal L
```

Final context (up to 100 characters either side):

```tex
 (3.32,.12) .. (3.42,.06) .. controls (3.50,-.08) and (3.80,-.02) .. (4.10,-.01);}}

(9 juin) Soit $\mathcal L$ un tronçon ordonné.

\deleted{Un sous-segment dans \uline{sous-tronçon} \uline{fermé} de $\mathcal
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved from ink

Crop links: crops/022_deleted.jpg

Alignment requires recheck: no flag

Review note: The looped L and the written dans in the cancelled draft are visible, notwithstanding the awkward syntax.

### C-022-U011 (C line 11)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 11.

Source C token:

```tex
\unsure{d'un|dans}
```

Source C context:

```tex
4.10,-.01);}}

(9 juin) Soit $\unsure{L|\mathscr{L}}$ un tronçon ordonné.

\deleted{Un sous-segment \unsure{d'un|dans} \uline{sous-tronçon} \uline{fermé} de $L$ est un sous ens de la forme $[a,$}

\textcircled{1} Topol
```

Aligned final span:

```tex
dans
```

Final context (up to 100 characters either side):

```tex
0,-.02) .. (4.10,-.01);}}

(9 juin) Soit $\mathcal L$ un tronçon ordonné.

\deleted{Un sous-segment dans \uline{sous-tronçon} \uline{fermé} de $\mathcal L$ est un sous ens de la forme $[a,$}

\textcircled
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved from ink

Crop links: crops/022_deleted.jpg

Alignment requires recheck: no flag

Review note: The looped L and the written dans in the cancelled draft are visible, notwithstanding the awkward syntax.

### C-022-U012 (C line 13)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 13.

Source C token:

```tex
\unsure{,}
```

Source C context:

```tex
a,$}

\textcircled{1} Topologie sur $L$ : base d'ouverts les $]a,b[$ (pour $a<b$), $L_{<a}$\deleted{\unsure{,}}, $L_{>b}$
[NB si $L$ n'a pas de plus petit élément (resp. de plus grand élément) on peut \unsure{o
```

Aligned final span:

```tex
\unsure{,}
```

Final context (up to 100 characters either side):

```tex
{1} Topologie sur $\mathcal L$ : base d'ouverts les $]a,b[$ (pour $a<b$), $\mathcal L_{<a}$\deleted{\unsure{,}}, $\mathcal L_{>b}$
[NB si $\mathcal L$ n'a pas de plus petit élément (resp. de plus grand élément)
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/022_nb.jpg; crops/022_foot.jpg

Alignment requires recheck: no flag

Review note: Small cancelled punctuation and the revised NB fragments remain unclear.

### C-022-U013 (C line 14)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 14.

Source C token:

```tex
\unsure{omettre}
```

Source C context:

```tex
unsure{,}}, $L_{>b}$
[NB si $L$ n'a pas de plus petit élément (resp. de plus grand élément) on peut \unsure{omettre} les $L_{<a}$ (resp. les $L_{>b}$). \inserted{\unsure{Une} extrémité de} \deleted{Pour que $\unsure{
```

Aligned final span:

```tex
omettre
```

Final context (up to 100 characters either side):

```tex
cal L_{>b}$
[NB si $\mathcal L$ n'a pas de plus petit élément (resp. de plus grand élément) on peut omettre les $\mathcal L_{<a}$ (resp. les $\mathcal L_{>b}$). \inserted{Une extrémité de} \deleted{Pour que 
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved from ink

Crop links: crops/022_nb.jpg

Alignment requires recheck: no flag

Review note: The full omettre and initial Une of the insertion are legible.

### C-022-U014 (C line 14)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 14.

Source C token:

```tex
\unsure{Une}
```

Source C context:

```tex
(resp. de plus grand élément) on peut \unsure{omettre} les $L_{<a}$ (resp. les $L_{>b}$). \inserted{\unsure{Une} extrémité de} \deleted{Pour que $\unsure{\{a\}}$ soit} $L$ \unsure{—|(} (s'il y en a) est fermé, ma
```

Aligned final span:

```tex
Une
```

Final context (up to 100 characters either side):

```tex
 plus grand élément) on peut omettre les $\mathcal L_{<a}$ (resp. les $\mathcal L_{>b}$). \inserted{Une extrémité de} \deleted{Pour que $\unsure{\{a\}}$ soit} $\mathcal L$ \unsure{—|(} (s'il y en a) est 
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved from ink

Crop links: crops/022_nb.jpg

Alignment requires recheck: no flag

Review note: The full omettre and initial Une of the insertion are legible.

### C-022-U015 (C line 14)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 14.

Source C token:

```tex
\unsure{\{a\}}
```

Source C context:

```tex
omettre} les $L_{<a}$ (resp. les $L_{>b}$). \inserted{\unsure{Une} extrémité de} \deleted{Pour que $\unsure{\{a\}}$ soit} $L$ \unsure{—|(} (s'il y en a) est fermé, mais \deleted{fermé, il f et \unsure{suff} s. que}
```

Aligned final span:

```tex
\unsure{\{a\}}
```

Final context (up to 100 characters either side):

```tex
les $\mathcal L_{<a}$ (resp. les $\mathcal L_{>b}$). \inserted{Une extrémité de} \deleted{Pour que $\unsure{\{a\}}$ soit} $\mathcal L$ \unsure{—|(} (s'il y en a) est fermé, mais \deleted{fermé, il f et \unsure{suff
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/022_nb.jpg; crops/022_foot.jpg

Alignment requires recheck: no flag

Review note: Small cancelled punctuation and the revised NB fragments remain unclear.

### C-022-U016 (C line 14)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 14.

Source C token:

```tex
\unsure{—|(}
```

Source C context:

```tex
p. les $L_{>b}$). \inserted{\unsure{Une} extrémité de} \deleted{Pour que $\unsure{\{a\}}$ soit} $L$ \unsure{—|(} (s'il y en a) est fermé, mais \deleted{fermé, il f et \unsure{suff} s. que}
On fera attention qu'en
```

Aligned final span:

```tex
\unsure{—|(}
```

Final context (up to 100 characters either side):

```tex
mathcal L_{>b}$). \inserted{Une extrémité de} \deleted{Pour que $\unsure{\{a\}}$ soit} $\mathcal L$ \unsure{—|(} (s'il y en a) est fermé, mais \deleted{fermé, il f et \unsure{suff} s. que}
On fera attention qu'en
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/022_nb.jpg; crops/022_foot.jpg

Alignment requires recheck: no flag

Review note: Small cancelled punctuation and the revised NB fragments remain unclear.

### C-022-U017 (C line 14)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 14.

Source C token:

```tex
\unsure{suff}
```

Source C context:

```tex
r que $\unsure{\{a\}}$ soit} $L$ \unsure{—|(} (s'il y en a) est fermé, mais \deleted{fermé, il f et \unsure{suff} s. que}
On fera attention qu'en général, \deleted{les $\unsure{\{a\}}$} \deleted{\unsure{si $a$ est
```

Aligned final span:

```tex
\unsure{suff}
```

Final context (up to 100 characters either side):

```tex
nsure{\{a\}}$ soit} $\mathcal L$ \unsure{—|(} (s'il y en a) est fermé, mais \deleted{fermé, il f et \unsure{suff} s. que}
On fera attention qu'en général, \deleted{les $\unsure{\{a\}}$} \deleted{\unsure{si $a$ est
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/022_nb.jpg; crops/022_foot.jpg

Alignment requires recheck: no flag

Review note: Small cancelled punctuation and the revised NB fragments remain unclear.

### C-022-U018 (C line 15)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 15.

Source C token:

```tex
\unsure{\{a\}}
```

Source C context:

```tex
, mais \deleted{fermé, il f et \unsure{suff} s. que}
On fera attention qu'en général, \deleted{les $\unsure{\{a\}}$} \deleted{\unsure{si $a$ est|si $a$ et}} pour $a\in L$ $\{a\}$ \uline{n'est pas} \inserted{\uline{
```

Aligned final span:

```tex
\unsure{\{a\}}
```

Final context (up to 100 characters either side):

```tex
, mais \deleted{fermé, il f et \unsure{suff} s. que}
On fera attention qu'en général, \deleted{les $\unsure{\{a\}}$} \deleted{\unsure{si $a$ est|si $a$ et}} pour $a\in\mathcal L$ $\{a\}$ \uline{n'est pas} \inserted
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/022_nb.jpg; crops/022_foot.jpg

Alignment requires recheck: no flag

Review note: Small cancelled punctuation and the revised NB fragments remain unclear.

### C-022-U019 (C line 15)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 15.

Source C token:

```tex
\unsure{si $a$ est|si $a$ et}
```

Source C context:

```tex
f et \unsure{suff} s. que}
On fera attention qu'en général, \deleted{les $\unsure{\{a\}}$} \deleted{\unsure{si $a$ est|si $a$ et}} pour $a\in L$ $\{a\}$ \uline{n'est pas} \inserted{\uline{\unsure{néct|néct$^{\mathrm t}$}}} \uline
```

Aligned final span:

```tex
\unsure{si $a$ est|si $a$ et}
```

Final context (up to 100 characters either side):

```tex
f et \unsure{suff} s. que}
On fera attention qu'en général, \deleted{les $\unsure{\{a\}}$} \deleted{\unsure{si $a$ est|si $a$ et}} pour $a\in\mathcal L$ $\{a\}$ \uline{n'est pas} \inserted{\uline{néc$^{\mathrm t}$}} \uline{fermé}
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/022_nb.jpg; crops/022_foot.jpg

Alignment requires recheck: no flag

Review note: Small cancelled punctuation and the revised NB fragments remain unclear.

### C-022-U020 (C line 15)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 15.

Source C token:

```tex
\unsure{néct|néct$^{\mathrm t}$}
```

Source C context:

```tex
$} \deleted{\unsure{si $a$ est|si $a$ et}} pour $a\in L$ $\{a\}$ \uline{n'est pas} \inserted{\uline{\unsure{néct|néct$^{\mathrm t}$}}} \uline{fermé}. Si $L$ est l'ens des lieux d'une \deleted{\unsure{segm}} ficelle topologique\unsur
```

Aligned final span:

```tex
néc$^{\mathrm t}$
```

Final context (up to 100 characters either side):

```tex
ted{\unsure{si $a$ est|si $a$ et}} pour $a\in\mathcal L$ $\{a\}$ \uline{n'est pas} \inserted{\uline{néc$^{\mathrm t}$}} \uline{fermé}. Si $\mathcal L$ est l'ens des lieux d'une \deleted{\unsure{segm}} ficelle topologi
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved from ink

Crop links: crops/022_foot.jpg

Alignment requires recheck: no flag

Review note: Only one elevated t follows néc; no duplicate baseline t is written.

### C-022-U021 (C line 15)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 15.

Source C token:

```tex
\unsure{segm}
```

Source C context:

```tex
{\uline{\unsure{néct|néct$^{\mathrm t}$}}} \uline{fermé}. Si $L$ est l'ens des lieux d'une \deleted{\unsure{segm}} ficelle topologique\unsure{$^{x}$|,}, \deleted{et} alors $\deleted{\unsure{a}}b\in\overline{\{\del
```

Aligned final span:

```tex
\unsure{segm}
```

Final context (up to 100 characters either side):

```tex
serted{\uline{néc$^{\mathrm t}$}} \uline{fermé}. Si $\mathcal L$ est l'ens des lieux d'une \deleted{\unsure{segm}} ficelle topologique$^{\ast}$, et alors $\deleted{\unsure{a}}b\in\overline{\{\deleted{\unsure{b}}a\
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/022_foot.jpg

Alignment requires recheck: no flag

Review note: The cancelled segm and old variable letters remain overlain; the last H alphabet cannot be chosen securely at the clipped edge.

### C-022-U022 (C line 15)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 15.

Source C token:

```tex
\unsure{$^{x}$|,}
```

Source C context:

```tex
m t}$}}} \uline{fermé}. Si $L$ est l'ens des lieux d'une \deleted{\unsure{segm}} ficelle topologique\unsure{$^{x}$|,}, \deleted{et} alors $\deleted{\unsure{a}}b\in\overline{\{\deleted{\unsure{b}}a\}}$ i.e. $\overline{
```

Aligned final span:

```tex
$^{\ast}$
```

Final context (up to 100 characters either side):

```tex
\uline{fermé}. Si $\mathcal L$ est l'ens des lieux d'une \deleted{\unsure{segm}} ficelle topologique$^{\ast}$, et alors $\deleted{\unsure{a}}b\in\overline{\{\deleted{\unsure{b}}a\}}$ i.e. $\overline{\{b\}}\sub
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved from ink

Crop links: crops/022_foot.jpg; crops/022_et.jpg

Alignment requires recheck: no flag

Review note: A raised asterisk and a separate baseline comma both occur, rather than alternatives. The transcription now has one of each. Alignment recheck: Root rechecked the raised star plus baseline comma. A duplicated transcription comma was removed; one star and one comma remain.

### C-022-U023 (C line 15)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 15.

Source C token:

```tex
\unsure{a}
```

Source C context:

```tex
ux d'une \deleted{\unsure{segm}} ficelle topologique\unsure{$^{x}$|,}, \deleted{et} alors $\deleted{\unsure{a}}b\in\overline{\{\deleted{\unsure{b}}a\}}$ i.e. $\overline{\{b\}}\subset\overline{\{a\}}$, équivaut 
```

Aligned final span:

```tex
\unsure{a}
```

Final context (up to 100 characters either side):

```tex
 est l'ens des lieux d'une \deleted{\unsure{segm}} ficelle topologique$^{\ast}$, et alors $\deleted{\unsure{a}}b\in\overline{\{\deleted{\unsure{b}}a\}}$ i.e. $\overline{\{b\}}\subset\overline{\{a\}}$, équivaut 
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/022_foot.jpg

Alignment requires recheck: no flag

Review note: The cancelled segm and old variable letters remain overlain; the last H alphabet cannot be chosen securely at the clipped edge.

### C-022-U024 (C line 15)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 15.

Source C token:

```tex
\unsure{b}
```

Source C context:

```tex
elle topologique\unsure{$^{x}$|,}, \deleted{et} alors $\deleted{\unsure{a}}b\in\overline{\{\deleted{\unsure{b}}a\}}$ i.e. $\overline{\{b\}}\subset\overline{\{a\}}$, équivaut à $b\supset a$ (en tt que parties de
```

Aligned final span:

```tex
\unsure{b}
```

Final context (up to 100 characters either side):

```tex
\unsure{segm}} ficelle topologique$^{\ast}$, et alors $\deleted{\unsure{a}}b\in\overline{\{\deleted{\unsure{b}}a\}}$ i.e. $\overline{\{b\}}\subset\overline{\{a\}}$, équivaut à $b\supset a$ (en tt que parties de
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/022_foot.jpg

Alignment requires recheck: no flag

Review note: The cancelled segm and old variable letters remain overlain; the last H alphabet cannot be chosen securely at the clipped edge.

### C-022-U025 (C line 15)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 15.

Source C token:

```tex
\unsure{$\mathscr H$|$\mathcal H$|$H$}
```

Source C context:

```tex
a\}}$ i.e. $\overline{\{b\}}\subset\overline{\{a\}}$, équivaut à $b\supset a$ (en tt que parties de \unsure{$\mathscr H$|$\mathcal H$|$H$})

```

Aligned final span:

```tex
\unsure{$\mathscr H$|$\mathcal H$|$H$}
```

Final context (up to 100 characters either side):

```tex
a\}}$ i.e. $\overline{\{b\}}\subset\overline{\{a\}}$, équivaut à $b\supset a$ (en tt que parties de \unsure{$\mathscr H$|$\mathcal H$|$H$})

% pale vertical watermark
\rotatebox{90}{\textsc{\unsure{Strong Extra}}}

```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/022_foot.jpg

Alignment requires recheck: no flag

Review note: The cancelled segm and old variable letters remain overlain; the last H alphabet cannot be chosen securely at the clipped edge.

### C-023-U001 (C line 2)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 2.

Source C token:

```tex
\unsure{b}
```

Source C context:

```tex
\scanpage{23}\mspage{22}
Il en résulte que $\overline{\{\deleted{\unsure{b}}a\}}=\overline{\{b\}}\Longleftrightarrow a=b$ \unsure{(donc|donc|Alors} l'espace top $\unsure{L|\ma
```

Aligned final span:

```tex
\unsure{b}
```

Final context (up to 100 characters either side):

```tex
\scanpage{23}\mspage{22}
Il en résulte que $\overline{\{\deleted{\unsure{b}}a\}}=\overline{\{b\}}\Longleftrightarrow a=b$ (donc l'espace top $\mathcal L$ satisfait l'axiome $T
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/023_top.jpg

Alignment requires recheck: no flag

Review note: The old b under a is blackened and remains marked.

### C-023-U002 (C line 2)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 2.

Source C token:

```tex
\unsure{(donc|donc|Alors}
```

Source C context:

```tex
2}
Il en résulte que $\overline{\{\deleted{\unsure{b}}a\}}=\overline{\{b\}}\Longleftrightarrow a=b$ \unsure{(donc|donc|Alors} l'espace top $\unsure{L|\mathscr{L}}$ satisfait l'axiome $T_0$, il est ``présobre'' i.e. s'injecte 
```

Aligned final span:

```tex
(donc
```

Final context (up to 100 characters either side):

```tex
2}
Il en résulte que $\overline{\{\deleted{\unsure{b}}a\}}=\overline{\{b\}}\Longleftrightarrow a=b$ (donc l'espace top $\mathcal L$ satisfait l'axiome $T_0$, il est ``présobre'' i.e. s'injecte dans le prés
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved from ink

Crop links: crops/023_top.jpg

Alignment requires recheck: no flag

Review note: An opening parenthesis precedes donc; the ground-set L has the looped form, and dans is written in full.

### C-023-U003 (C line 2)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 2.

Source C token:

```tex
\unsure{L|\mathscr{L}}
```

Source C context:

```tex
ed{\unsure{b}}a\}}=\overline{\{b\}}\Longleftrightarrow a=b$ \unsure{(donc|donc|Alors} l'espace top $\unsure{L|\mathscr{L}}$ satisfait l'axiome $T_0$, il est ``présobre'' i.e. s'injecte \unsure{dans|ds} le présobrifié) -- j
```

Aligned final span:

```tex
\mathcal L
```

Final context (up to 100 characters either side):

```tex
 $\overline{\{\deleted{\unsure{b}}a\}}=\overline{\{b\}}\Longleftrightarrow a=b$ (donc l'espace top $\mathcal L$ satisfait l'axiome $T_0$, il est ``présobre'' i.e. s'injecte dans le présobrifié) -- je ne sais si
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved from ink

Crop links: crops/023_top.jpg

Alignment requires recheck: no flag

Review note: An opening parenthesis precedes donc; the ground-set L has the looped form, and dans is written in full.

### C-023-U004 (C line 2)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 2.

Source C token:

```tex
\unsure{dans|ds}
```

Source C context:

```tex
 l'espace top $\unsure{L|\mathscr{L}}$ satisfait l'axiome $T_0$, il est ``présobre'' i.e. s'injecte \unsure{dans|ds} le présobrifié) -- je ne sais si c'est
le cas pour tout tronçon, \unsure{ni|ni même} si un tronçon,
```

Aligned final span:

```tex
dans
```

Final context (up to 100 characters either side):

```tex
w a=b$ (donc l'espace top $\mathcal L$ satisfait l'axiome $T_0$, il est ``présobre'' i.e. s'injecte dans le présobrifié) -- je ne sais si c'est
le cas pour tout tronçon, ni si un tronçon, avec sa top. can
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved from ink

Crop links: crops/023_top.jpg

Alignment requires recheck: no flag

Review note: An opening parenthesis precedes donc; the ground-set L has the looped form, and dans is written in full.

### C-023-U005 (C line 3)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 3.

Source C token:

```tex
\unsure{ni|ni même}
```

Source C context:

```tex
'' i.e. s'injecte \unsure{dans|ds} le présobrifié) -- je ne sais si c'est
le cas pour tout tronçon, \unsure{ni|ni même} si un tronçon, avec sa top. canonique, est sobre (donc, de plus, tte partie fermée \uline{irréducti
```

Aligned final span:

```tex
ni
```

Final context (up to 100 characters either side):

```tex
t ``présobre'' i.e. s'injecte dans le présobrifié) -- je ne sais si c'est
le cas pour tout tronçon, ni si un tronçon, avec sa top. canonique, est sobre (donc, de plus, tte partie fermée \uline{irréducti
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved from ink

Crop links: crops/023_question.jpg; crops/023_middle.jpg

Alignment requires recheck: no flag

Review note: There is ni without même; a comma follows voir. The quoted noun has no final s, and the elevated reference mark is a dagger.

### C-023-U006 (C line 5)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 5.

Source C token:

```tex
\unsure{A|À}
```

Source C context:

```tex
p-shaped double vertical stroke joins the underline above to the end of the preceding line.
\margin{\unsure{A|À} voir\unsure{.|,}}
les ``\unsure{segment|segments}'' $[a,b]$ ne sont pas néc. fermés pour la top. ca
```

Aligned final span:

```tex
\unsure{A|À}
```

Final context (up to 100 characters either side):

```tex
]\draw (0,0)--(1.25,-.03)--(1.56,1)--(3.4,1);\draw (1.18,-.01)--(1.49,1);\end{tikzpicture}}
\margin{\unsure{A|À} voir,}
les ``segment'' $[a,b]$ ne sont pas néc. fermés pour la top. canonique$^{\dagger}$\unsure{,|
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/023_question.jpg; crops/023_middle.jpg

Alignment requires recheck: no flag

Review note: The accent in A/À, clipped punctuation, extra equality-like sign and overwritten subscript remain uncertain.

### C-023-U007 (C line 5)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 5.

Source C token:

```tex
\unsure{.|,}
```

Source C context:

```tex
ertical stroke joins the underline above to the end of the preceding line.
\margin{\unsure{A|À} voir\unsure{.|,}}
les ``\unsure{segment|segments}'' $[a,b]$ ne sont pas néc. fermés pour la top. canonique\unsure{$^
```

Aligned final span:

```tex
,
```

Final context (up to 100 characters either side):

```tex
25,-.03)--(1.56,1)--(3.4,1);\draw (1.18,-.01)--(1.49,1);\end{tikzpicture}}
\margin{\unsure{A|À} voir,}
les ``segment'' $[a,b]$ ne sont pas néc. fermés pour la top. canonique$^{\dagger}$\unsure{,|.}
Ce 
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved from ink

Crop links: crops/023_question.jpg; crops/023_middle.jpg

Alignment requires recheck: no flag

Review note: There is ni without même; a comma follows voir. The quoted noun has no final s, and the elevated reference mark is a dagger.

### C-023-U008 (C line 6)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 6.

Source C token:

```tex
\unsure{segment|segments}
```

Source C context:

```tex
 the underline above to the end of the preceding line.
\margin{\unsure{A|À} voir\unsure{.|,}}
les ``\unsure{segment|segments}'' $[a,b]$ ne sont pas néc. fermés pour la top. canonique\unsure{$^{\dagger}$|$^{+}$|!}\unsure{,|.}

```

Aligned final span:

```tex
segment
```

Final context (up to 100 characters either side):

```tex
-(1.56,1)--(3.4,1);\draw (1.18,-.01)--(1.49,1);\end{tikzpicture}}
\margin{\unsure{A|À} voir,}
les ``segment'' $[a,b]$ ne sont pas néc. fermés pour la top. canonique$^{\dagger}$\unsure{,|.}
Ce n'est que lorsq
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved from ink

Crop links: crops/023_question.jpg; crops/023_middle.jpg

Alignment requires recheck: no flag

Review note: There is ni without même; a comma follows voir. The quoted noun has no final s, and the elevated reference mark is a dagger.

### C-023-U009 (C line 6)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 6.

Source C token:

```tex
\unsure{$^{\dagger}$|$^{+}$|!}
```

Source C context:

```tex
nsure{.|,}}
les ``\unsure{segment|segments}'' $[a,b]$ ne sont pas néc. fermés pour la top. canonique\unsure{$^{\dagger}$|$^{+}$|!}\unsure{,|.}
Ce n'est que lorsque $L$ est \uline{tot} ordonné qu'on peut conclure que les pts sont f
```

Aligned final span:

```tex
$^{\dagger}$
```

Final context (up to 100 characters either side):

```tex
}
\margin{\unsure{A|À} voir,}
les ``segment'' $[a,b]$ ne sont pas néc. fermés pour la top. canonique$^{\dagger}$\unsure{,|.}
Ce n'est que lorsque $\mathcal L$ est \uline{tot} ordonné qu'on peut conclure que les p
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved from ink

Crop links: crops/023_question.jpg; crops/023_middle.jpg

Alignment requires recheck: no flag

Review note: There is ni without même; a comma follows voir. The quoted noun has no final s, and the elevated reference mark is a dagger.

### C-023-U010 (C line 6)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 6.

Source C token:

```tex
\unsure{,|.}
```

Source C context:

```tex
ent|segments}'' $[a,b]$ ne sont pas néc. fermés pour la top. canonique\unsure{$^{\dagger}$|$^{+}$|!}\unsure{,|.}
Ce n'est que lorsque $L$ est \uline{tot} ordonné qu'on peut conclure que les pts sont fermés (récip
```

Aligned final span:

```tex
\unsure{,|.}
```

Final context (up to 100 characters either side):

```tex
nsure{A|À} voir,}
les ``segment'' $[a,b]$ ne sont pas néc. fermés pour la top. canonique$^{\dagger}$\unsure{,|.}
Ce n'est que lorsque $\mathcal L$ est \uline{tot} ordonné qu'on peut conclure que les pts sont ferm
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/023_question.jpg; crops/023_middle.jpg

Alignment requires recheck: no flag

Review note: The accent in A/À, clipped punctuation, extra equality-like sign and overwritten subscript remain uncertain.

### C-023-U011 (C line 7)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 7.

Source C token:

```tex
\unsure{=|\simeq}
```

Source C context:

```tex
\uline{tot} ordonné qu'on peut conclure que les pts sont fermés (réciproque ?) et en fait, $L$ est $\unsure{=|\simeq}$ \uline{séparé}, et de plus les $[a,b]$, $L_{\geq a}$, $L_{\leq\deleted{\unsure{b}}a}$ sont fermés.
```

Aligned final span:

```tex
\unsure{=|\simeq}
```

Final context (up to 100 characters either side):

```tex
t} ordonné qu'on peut conclure que les pts sont fermés (réciproque ?) et en fait, $\mathcal L$ est $\unsure{=|\simeq}$ \uline{séparé}, et de plus les $[a,b]$, $\mathcal L_{\geq a}$, $\mathcal L_{\leq\deleted{\unsure{b
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/023_question.jpg; crops/023_middle.jpg

Alignment requires recheck: no flag

Review note: The accent in A/À, clipped punctuation, extra equality-like sign and overwritten subscript remain uncertain.

### C-023-U012 (C line 7)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 7.

Source C token:

```tex
\unsure{b}
```

Source C context:

```tex
 $L$ est $\unsure{=|\simeq}$ \uline{séparé}, et de plus les $[a,b]$, $L_{\geq a}$, $L_{\leq\deleted{\unsure{b}}a}$ sont fermés.

On peut définir une autre topologie, ayant comme base fondamentale de fermés les 
```

Aligned final span:

```tex
\unsure{b}
```

Final context (up to 100 characters either side):

```tex
=|\simeq}$ \uline{séparé}, et de plus les $[a,b]$, $\mathcal L_{\geq a}$, $\mathcal L_{\leq\deleted{\unsure{b}}a}$ sont fermés.

On peut définir une autre topologie, ayant comme base fondamentale de fermés les 
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/023_question.jpg; crops/023_middle.jpg

Alignment requires recheck: no flag

Review note: The accent in A/À, clipped punctuation, extra equality-like sign and overwritten subscript remain uncertain.

### C-023-U013 (C line 9)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 9.

Source C token:

```tex
\unsure{quelc\textsuperscript{on}|quelc.}
```

Source C context:

```tex
ase fondamentale de fermés les $[a,b]$, $L_{\geq a}$, $L_{\leq a}$ (dont on prend les intersections \unsure{quelc\textsuperscript{on}|quelc.} de réunions finies, pour avoir tous les fermés)

```

Aligned final span:

```tex
quelc.
```

Final context (up to 100 characters either side):

```tex
e fermés les $[a,b]$, $\mathcal L_{\geq a}$, $\mathcal L_{\leq a}$ (dont on prend les intersections quelc. de réunions finies, pour avoir tous les fermés)

% pale vertical watermark
\rotatebox{90}{\textsc{\
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved from ink

Crop links: crops/023_bottom.jpg

Alignment requires recheck: no flag

Review note: The abbreviation ends quelc. at the baseline; nearby strokes do not supply an additional elevated on.

### C-024-U001 (C line 2)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 2.

Source C token:

```tex
\unsure{ennuyé}
```

Source C context:

```tex
\scanpage{24}\mspage{23}
Mais maintenant, on est \unsure{ennuyé}, car $]a,b[$ n'a plus envie d'être ouvert !

\deleted{\unsure{ici|on}} On peut bien sûr prendre la 
```

Aligned final span:

```tex
ennuyé
```

Final context (up to 100 characters either side):

```tex
\scanpage{24}\mspage{23}
Mais maintenant, on est ennuyé, car $]a,b[$ n'a plus envie d'être ouvert !

\deleted{\unsure{ici|on}} On peut bien sûr prendre la 
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved from ink

Crop links: crops/024_top.jpg

Alignment requires recheck: no flag

Review note: The ending ennuyé and looped ground-set L are legible; the two displayed conditions both use a<b.

### C-024-U002 (C line 4)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 4.

Source C token:

```tex
\unsure{ici|on}
```

Source C context:

```tex
e{23}
Mais maintenant, on est \unsure{ennuyé}, car $]a,b[$ n'a plus envie d'être ouvert !

\deleted{\unsure{ici|on}} On peut bien sûr prendre la topologie borne sup. des deux, ayant comme base d'ouverts

\[
\begin{a
```

Aligned final span:

```tex
\unsure{ici|on}
```

Final context (up to 100 characters either side):

```tex
24}\mspage{23}
Mais maintenant, on est ennuyé, car $]a,b[$ n'a plus envie d'être ouvert !

\deleted{\unsure{ici|on}} On peut bien sûr prendre la topologie borne sup. des deux, ayant comme base d'ouverts

\[
\begin{a
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/024_top.jpg; crops/024_middle.jpg

Alignment requires recheck: no flag

Review note: Old overwritten words, the cancelled inequality and cramped endpoint punctuation/index remain uncertain; the text is not repaired to fit the questions.

### C-024-U003 (C line 8)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 8.

Source C token:

```tex
\unsure{L|\mathscr{L}}
```

Source C context:

```tex
 bien sûr prendre la topologie borne sup. des deux, ayant comme base d'ouverts

\[
\begin{aligned}
 \unsure{L|\mathscr{L}}_{<a},\,L_{>a},\quad &]a,b[ && (a<b)\\
 \complement L_{\deleted{\unsure{\leq|>}}\geq a},\,\complemen
```

Aligned final span:

```tex
\mathcal L
```

Final context (up to 100 characters either side):

```tex
 bien sûr prendre la topologie borne sup. des deux, ayant comme base d'ouverts

\[
\begin{aligned}
 \mathcal L_{<a},\,\mathcal L_{>a},\quad &]a,b[ && (a<b)\\
 \complement \mathcal L_{\deleted{\unsure{\leq|>}}\g
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved from ink

Crop links: crops/024_top.jpg

Alignment requires recheck: no flag

Review note: The ending ennuyé and looped ground-set L are legible; the two displayed conditions both use a<b.

### C-024-U004 (C line 9)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 9.

Source C token:

```tex
\unsure{\leq|>}
```

Source C context:

```tex
gin{aligned}
 \unsure{L|\mathscr{L}}_{<a},\,L_{>a},\quad &]a,b[ && (a<b)\\
 \complement L_{\deleted{\unsure{\leq|>}}\geq a},\,\complement L_{\leq a},\quad &[a,b] && (a<b)
\end{aligned}
\]

\deleted{De sorte que $]a,
```

Aligned final span:

```tex
\unsure{\leq|>}
```

Final context (up to 100 characters either side):

```tex
igned}
 \mathcal L_{<a},\,\mathcal L_{>a},\quad &]a,b[ && (a<b)\\
 \complement \mathcal L_{\deleted{\unsure{\leq|>}}\geq a},\,\complement \mathcal L_{\leq a},\quad &[a,b] && (a<b)
\end{aligned}
\]

\deleted{De sorte
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/024_top.jpg; crops/024_middle.jpg

Alignment requires recheck: no flag

Review note: Old overwritten words, the cancelled inequality and cramped endpoint punctuation/index remain uncertain; the text is not repaired to fit the questions.

### C-024-U005 (C line 13)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 13.

Source C token:

```tex
\unsure{est|est un}
```

Source C context:

```tex
q a},\,\complement L_{\leq a},\quad &[a,b] && (a<b)
\end{aligned}
\]

\deleted{De sorte que $]a,b[$ \unsure{est|est un}} \deleted{Sera-t-il vrai, si $a\unsure{\nless|\leq|<}b$, et} \deleted{Mais} \deleted{$b$ n'est pas 
```

Aligned final span:

```tex
\unsure{est|est un}
```

Final context (up to 100 characters either side):

```tex
omplement \mathcal L_{\leq a},\quad &[a,b] && (a<b)
\end{aligned}
\]

\deleted{De sorte que $]a,b[$ \unsure{est|est un}} \deleted{Sera-t-il vrai, si $a\unsure{\nless|\leq|<}b$, et} \deleted{Mais} \deleted{$b$ n'est pas 
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/024_top.jpg; crops/024_middle.jpg

Alignment requires recheck: no flag

Review note: Old overwritten words, the cancelled inequality and cramped endpoint punctuation/index remain uncertain; the text is not repaired to fit the questions.

### C-024-U006 (C line 13)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 13.

Source C token:

```tex
\unsure{\nless|\leq|<}
```

Source C context:

```tex

\end{aligned}
\]

\deleted{De sorte que $]a,b[$ \unsure{est|est un}} \deleted{Sera-t-il vrai, si $a\unsure{\nless|\leq|<}b$, et} \deleted{Mais} \deleted{$b$ n'est pas plus grand élément, que}

Aura-t-on \deleted{$b\in [a,
```

Aligned final span:

```tex
\unsure{\nless|\leq|<}
```

Final context (up to 100 characters either side):

```tex

\end{aligned}
\]

\deleted{De sorte que $]a,b[$ \unsure{est|est un}} \deleted{Sera-t-il vrai, si $a\unsure{\nless|\leq|<}b$, et} \deleted{Mais} \deleted{$b$ n'est pas plus grand élément, que}

Aura-t-on \deleted{$b\in [a,
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/024_top.jpg; crops/024_middle.jpg

Alignment requires recheck: no flag

Review note: Old overwritten words, the cancelled inequality and cramped endpoint punctuation/index remain uncertain; the text is not repaired to fit the questions.

### C-024-U007 (C line 19)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 19.

Source C token:

```tex
\unsure{n'|est}
```

Source C context:

```tex
 \overline{]a,b[}&=[a,b]\quad ?\\
 \overline{L_{<a}}&=L_{\leq a}\quad ?\quad \text{(si $a$ \deleted{\unsure{n'|est}} n'est pas plus petit élément\unsure{—|)}} \quad \inserted{(a\ne\unsure{o|0}_{L})}\\
 \overline{L_{
```

Aligned final span:

```tex
\unsure{n'|est}
```

Final context (up to 100 characters either side):

```tex
=[a,b]\quad ?\\
 \overline{\mathcal L_{<a}}&=\mathcal L_{\leq a}\quad ?\quad \text{(si $a$ \deleted{\unsure{n'|est}} n'est pas plus petit élément\unsure{—|)}} \quad \inserted{(a\ne\unsure{o|0}_{L})}\\
 \overline{\ma
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/024_top.jpg; crops/024_middle.jpg

Alignment requires recheck: no flag

Review note: Old overwritten words, the cancelled inequality and cramped endpoint punctuation/index remain uncertain; the text is not repaired to fit the questions.

### C-024-U008 (C line 19)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 19.

Source C token:

```tex
\unsure{—|)}
```

Source C context:

```tex
L_{<a}}&=L_{\leq a}\quad ?\quad \text{(si $a$ \deleted{\unsure{n'|est}} n'est pas plus petit élément\unsure{—|)}} \quad \inserted{(a\ne\unsure{o|0}_{L})}\\
 \overline{L_{>a}}&=L_{\geq a}\quad ?\quad \text{(si $a$
```

Aligned final span:

```tex
\unsure{—|)}
```

Final context (up to 100 characters either side):

```tex
\mathcal L_{\leq a}\quad ?\quad \text{(si $a$ \deleted{\unsure{n'|est}} n'est pas plus petit élément\unsure{—|)}} \quad \inserted{(a\ne\unsure{o|0}_{L})}\\
 \overline{\mathcal L_{>a}}&=\mathcal L_{\geq a}\quad ?\
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/024_top.jpg; crops/024_middle.jpg

Alignment requires recheck: no flag

Review note: Old overwritten words, the cancelled inequality and cramped endpoint punctuation/index remain uncertain; the text is not repaired to fit the questions.

### C-024-U009 (C line 19)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 19.

Source C token:

```tex
\unsure{o|0}
```

Source C context:

```tex
xt{(si $a$ \deleted{\unsure{n'|est}} n'est pas plus petit élément\unsure{—|)}} \quad \inserted{(a\ne\unsure{o|0}_{L})}\\
 \overline{L_{>a}}&=L_{\geq a}\quad ?\quad \text{(si $a$ n'est pas plus grand élément ?)}
\
```

Aligned final span:

```tex
\unsure{o|0}
```

Final context (up to 100 characters either side):

```tex
xt{(si $a$ \deleted{\unsure{n'|est}} n'est pas plus petit élément\unsure{—|)}} \quad \inserted{(a\ne\unsure{o|0}_{L})}\\
 \overline{\mathcal L_{>a}}&=\mathcal L_{\geq a}\quad ?\quad \text{(si $a$ n'est pas plus g
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/024_top.jpg; crops/024_middle.jpg

Alignment requires recheck: no flag

Review note: Old overwritten words, the cancelled inequality and cramped endpoint punctuation/index remain uncertain; the text is not repaired to fit the questions.

### C-024-U010 (C line 25)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 25.

Source C token:

```tex
\unsure{Donc|D'où}
```

Source C context:

```tex
{$a$};\node[below] at (3.07,.02) {$b$};\node[below] at (3.96,.03) {$y$};\end{tikzpicture}}
\deleted{\unsure{Donc|D'où}} On est ramené, dans le premier cas, à prouver (p. ex.) $a\in\overline{]a,b[}$, et pour ceci, \inse
```

Aligned final span:

```tex
\unsure{Donc|D'où}
```

Final context (up to 100 characters either side):

```tex
{$a$};\node[below] at (3.07,.02) {$b$};\node[below] at (3.96,.03) {$y$};\end{tikzpicture}}
\deleted{\unsure{Donc|D'où}} On est ramené, dans le premier cas, à prouver (p. ex.) $a\in\overline{]a,b[}$, et pour ceci, \inse
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/024_bottom.jpg

Alignment requires recheck: no flag

Review note: The old introductory word and short crossed/end fragments remain partly obscured or clipped.

### C-024-U011 (C line 25)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 25.

Source C token:

```tex
\unsure{On|que}
```

Source C context:

```tex
cas, à prouver (p. ex.) $a\in\overline{]a,b[}$, et pour ceci, \inserted{il suffit de voir} \deleted{\unsure{On|que}} que \unsure{tt|tte} ouvert ``élémentaire'' qui contient $a$, contient un $]a,\varepsilon[$, avec $
```

Aligned final span:

```tex
On
```

Final context (up to 100 characters either side):

```tex
cas, à prouver (p. ex.) $a\in\overline{]a,b[}$, et pour ceci, \inserted{il suffit de voir} \deleted{On} que tte ouvert ``élémentaire'' qui contient $a$, contient un $]a,\varepsilon[$, avec $a<\varepsilo
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved from ink

Crop links: crops/024_bottom.jpg

Alignment requires recheck: no flag

Review note: The crossed On is a clear capital O with n; tte has a visible final e, retained despite its agreement with ouvert.

### C-024-U012 (C line 25)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 25.

Source C token:

```tex
\unsure{tt|tte}
```

Source C context:

```tex
.) $a\in\overline{]a,b[}$, et pour ceci, \inserted{il suffit de voir} \deleted{\unsure{On|que}} que \unsure{tt|tte} ouvert ``élémentaire'' qui contient $a$, contient un $]a,\varepsilon[$, avec $a<\varepsilon<b$. Mai
```

Aligned final span:

```tex
tte
```

Final context (up to 100 characters either side):

```tex
rouver (p. ex.) $a\in\overline{]a,b[}$, et pour ceci, \inserted{il suffit de voir} \deleted{On} que tte ouvert ``élémentaire'' qui contient $a$, contient un $]a,\varepsilon[$, avec $a<\varepsilon<b$. Mai
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved from ink

Crop links: crops/024_bottom.jpg

Alignment requires recheck: no flag

Review note: The crossed On is a clear capital O with n; tte has a visible final e, retained despite its agreement with ouvert.

### C-024-U013 (C line 25)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 25.

Source C token:

```tex
\unsure{en}
```

Source C context:

```tex
repsilon<b$. Mais c'est faux déjà pour un ens. de lieux associé à une ficelle topologique, \deleted{\unsure{en}} [prendre ouvert él. $\complement[x,y]$\unsure{—|.}

% slanted
\margin{Il \unsure{faut avoir|faudra
```

Aligned final span:

```tex
\unsure{en}
```

Final context (up to 100 characters either side):

```tex
repsilon<b$. Mais c'est faux déjà pour un ens. de lieux associé à une ficelle topologique, \deleted{\unsure{en}} [prendre ouvert él. $\complement[x,y]$\unsure{—|.}

% slanted
\margin{Il faut avoir que $a\in\comp
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/024_bottom.jpg

Alignment requires recheck: no flag

Review note: The old introductory word and short crossed/end fragments remain partly obscured or clipped.

### C-024-U014 (C line 25)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 25.

Source C token:

```tex
\unsure{—|.}
```

Source C context:

```tex
ieux associé à une ficelle topologique, \deleted{\unsure{en}} [prendre ouvert él. $\complement[x,y]$\unsure{—|.}

% slanted
\margin{Il \unsure{faut avoir|faudrait avoir} que $a\in\complement[x,y]$ mais $]a,b[\,\s
```

Aligned final span:

```tex
\unsure{—|.}
```

Final context (up to 100 characters either side):

```tex
ieux associé à une ficelle topologique, \deleted{\unsure{en}} [prendre ouvert él. $\complement[x,y]$\unsure{—|.}

% slanted
\margin{Il faut avoir que $a\in\complement[x,y]$ mais $]a,b[\,\subset [x,y]$}

% pale ve
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/024_bottom.jpg

Alignment requires recheck: no flag

Review note: The old introductory word and short crossed/end fragments remain partly obscured or clipped.

### C-024-U015 (C line 28)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 28.

Source C token:

```tex
\unsure{faut avoir|faudrait avoir}
```

Source C context:

```tex
que, \deleted{\unsure{en}} [prendre ouvert él. $\complement[x,y]$\unsure{—|.}

% slanted
\margin{Il \unsure{faut avoir|faudrait avoir} que $a\in\complement[x,y]$ mais $]a,b[\,\subset [x,y]$}

```

Aligned final span:

```tex
faut avoir
```

Final context (up to 100 characters either side):

```tex
que, \deleted{\unsure{en}} [prendre ouvert él. $\complement[x,y]$\unsure{—|.}

% slanted
\margin{Il faut avoir que $a\in\complement[x,y]$ mais $]a,b[\,\subset [x,y]$}

% pale vertical watermark
\rotatebox{90}{\
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved from ink

Crop links: crops/024_margin.jpg

Alignment requires recheck: no flag

Review note: Rotation gives faut avoir; no extra drai strokes appear.

### C-025-U001 (C line 2)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 2.

Source C token:

```tex
\unsure{L|\mathscr{L}}
```

Source C context:

```tex
base formée avec les ``intervalles''), et on appellera néanmoins par abus de langage, les $[a,b]$, $\unsure{L|\mathscr{L}}_{\leq a}$, $L_{\geq b}$ (ainsi que $L$) \uline{sous-tronçons} ordinaires (ou \unsure{biordonnés|bie
```

Aligned final span:

```tex
\mathcal L
```

Final context (up to 100 characters either side):

```tex
base formée avec les ``intervalles''), et on appellera néanmoins par abus de langage, les $[a,b]$, $\mathcal L_{\leq a}$, $\mathcal L_{\geq b}$ (ainsi que $\mathcal L$) \uline{sous-tronçons} \unsure{ordonnés|or
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved from ink

Crop links: crops/025_top.jpg

Alignment requires recheck: no flag

Review note: Looped ground-set L, the rounded non group and live b with tall stem are legible; or/ex are kept as the written abbreviations.

### C-025-U002 (C line 2)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 2.

Source C token:

```tex
\unsure{biordonnés|bien donnés|bien disons|binominés}
```

Source C context:

```tex
\unsure{L|\mathscr{L}}_{\leq a}$, $L_{\geq b}$ (ainsi que $L$) \uline{sous-tronçons} ordinaires (ou \unsure{biordonnés|bien donnés|bien disons|binominés}) ``fermés'', [NB on les suppose \unsure{non|ici} réduits à un pt, i.e.
\[
\deleted{\unsure{[|i}} a<
```

Aligned final span:

```tex
\unsure{biordonnés|bien donnés|bien disons|binominés}
```

Final context (up to 100 characters either side):

```tex
mathcal L_{\geq b}$ (ainsi que $\mathcal L$) \uline{sous-tronçons} \unsure{ordonnés|ordinaires} (ou \unsure{biordonnés|bien donnés|bien disons|binominés}) ``fermés'', [NB on les suppose non réduits à un pt, i.e.
\[
\deleted{\unsure{[|i}} a<b\quad \text{
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/025_top.jpg

Alignment requires recheck: no flag

Review note: The parenthetic descriptor and old opening/variable strokes remain compressed or crossed.

### C-025-U003 (C line 2)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 2.

Source C token:

```tex
\unsure{non|ici}
```

Source C context:

```tex
rdinaires (ou \unsure{biordonnés|bien donnés|bien disons|binominés}) ``fermés'', [NB on les suppose \unsure{non|ici} réduits à un pt, i.e.
\[
\deleted{\unsure{[|i}} a<b\quad \text{resp.}\quad a\ne\mathrm{or}(L)\quad 
```

Aligned final span:

```tex
non
```

Final context (up to 100 characters either side):

```tex
dinaires} (ou \unsure{biordonnés|bien donnés|bien disons|binominés}) ``fermés'', [NB on les suppose non réduits à un pt, i.e.
\[
\deleted{\unsure{[|i}} a<b\quad \text{resp.}\quad a\ne\mathrm{or}(\mathcal
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved from ink

Crop links: crops/025_top.jpg

Alignment requires recheck: no flag

Review note: Looped ground-set L, the rounded non group and live b with tall stem are legible; or/ex are kept as the written abbreviations.

### C-025-U004 (C line 4)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 4.

Source C token:

```tex
\unsure{[|i}
```

Source C context:

```tex
isons|binominés}) ``fermés'', [NB on les suppose \unsure{non|ici} réduits à un pt, i.e.
\[
\deleted{\unsure{[|i}} a<b\quad \text{resp.}\quad a\ne\mathrm{or}(L)\quad \text{resp.}\quad \deleted{\unsure{a}}\unsure{b
```

Aligned final span:

```tex
\unsure{[|i}
```

Final context (up to 100 characters either side):

```tex
donnés|bien disons|binominés}) ``fermés'', [NB on les suppose non réduits à un pt, i.e.
\[
\deleted{\unsure{[|i}} a<b\quad \text{resp.}\quad a\ne\mathrm{or}(\mathcal L)\quad \text{resp.}\quad \deleted{\unsure{a}}
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/025_top.jpg

Alignment requires recheck: no flag

Review note: The parenthetic descriptor and old opening/variable strokes remain compressed or crossed.

### C-025-U005 (C line 4)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 4.

Source C token:

```tex
\unsure{a}
```

Source C context:

```tex
deleted{\unsure{[|i}} a<b\quad \text{resp.}\quad a\ne\mathrm{or}(L)\quad \text{resp.}\quad \deleted{\unsure{a}}\unsure{b|a}\ne\mathrm{ex}(L)\;]
\]

Un \uline{sous-tronçon \inserted{fermé} large} est une \delete
```

Aligned final span:

```tex
\unsure{a}
```

Final context (up to 100 characters either side):

```tex
unsure{[|i}} a<b\quad \text{resp.}\quad a\ne\mathrm{or}(\mathcal L)\quad \text{resp.}\quad \deleted{\unsure{a}}b\ne\mathrm{ex}(\mathcal L)\;]
\]

Un \uline{sous-tronçon \inserted{fermé} large} est une \deleted{
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/025_top.jpg

Alignment requires recheck: no flag

Review note: The parenthetic descriptor and old opening/variable strokes remain compressed or crossed.

### C-025-U006 (C line 4)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 4.

Source C token:

```tex
\unsure{b|a}
```

Source C context:

```tex
sure{[|i}} a<b\quad \text{resp.}\quad a\ne\mathrm{or}(L)\quad \text{resp.}\quad \deleted{\unsure{a}}\unsure{b|a}\ne\mathrm{ex}(L)\;]
\]

Un \uline{sous-tronçon \inserted{fermé} large} est une \deleted{sous-tronço
```

Aligned final span:

```tex
b
```

Final context (up to 100 characters either side):

```tex
} a<b\quad \text{resp.}\quad a\ne\mathrm{or}(\mathcal L)\quad \text{resp.}\quad \deleted{\unsure{a}}b\ne\mathrm{ex}(\mathcal L)\;]
\]

Un \uline{sous-tronçon \inserted{fermé} large} est une \deleted{so
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved from ink

Crop links: crops/025_top.jpg

Alignment requires recheck: no flag

Review note: Looped ground-set L, the rounded non group and live b with tall stem are legible; or/ex are kept as the written abbreviations.

### C-025-U007 (C line 7)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 7.

Source C token:

```tex
\unsure{ss-tronçon|s-tronçon}
```

Source C context:

```tex
n \uline{sous-tronçon \inserted{fermé} large} est une \deleted{sous-tronçon} partie qui est soit un \unsure{ss-tronçon|s-tronçon}, soit \unsure{réduit|réduite} à un pt.

Pour une telle partie, $T$, on
% Widely spaced strokes cros
```

Aligned final span:

```tex
ss-tronçon
```

Final context (up to 100 characters either side):

```tex
n \uline{sous-tronçon \inserted{fermé} large} est une \deleted{sous-tronçon} partie qui est soit un ss-tronçon, soit \unsure{réduit|réduite} à un pt.

Pour une telle partie, $T$, on
% Widely spaced strokes cros
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved from ink

Crop links: crops/025_large.jpg

Alignment requires recheck: no flag

Review note: Two initial s strokes precede the hyphen in ss-tronçon.

### C-025-U008 (C line 7)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 7.

Source C token:

```tex
\unsure{réduit|réduite}
```

Source C context:

```tex
é} large} est une \deleted{sous-tronçon} partie qui est soit un \unsure{ss-tronçon|s-tronçon}, soit \unsure{réduit|réduite} à un pt.

Pour une telle partie, $T$, on
% Widely spaced strokes cross the whole lower block, from 
```

Aligned final span:

```tex
\unsure{réduit|réduite}
```

Final context (up to 100 characters either side):

```tex
nçon \inserted{fermé} large} est une \deleted{sous-tronçon} partie qui est soit un ss-tronçon, soit \unsure{réduit|réduite} à un pt.

Pour une telle partie, $T$, on
% Widely spaced strokes cross the whole lower block, from 
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/025_large.jpg

Alignment requires recheck: no flag

Review note: The terminal e of réduit/réduite cannot be securely separated from the exit stroke.

### C-025-U009 (C line 16)

Mechanical state: **same unsure token in equal alignment**. Final aligned line: 16.

Source C token:

```tex
\unsure{frontière dans la top.|frontière dans la top}
```

Source C context:

```tex
&\deleted{\{t\in T\mid t\in \overline{L\setminus T}\}}\quad\text{\deleted{bord}}\\
 &\text{\deleted{\unsure{frontière dans la top.|frontière dans la top}}}\\
 &\text{\deleted{absolu de $T$ $=$ ensemble}}\\
 &\text{\deleted{\unsure{canonique}}}\\
 \delet
```

Aligned final span:

```tex
\unsure{frontière dans la top.|frontière dans la top}
```

Final context (up to 100 characters either side):

```tex
{\{t\in T\mid t\in \overline{\mathcal L\setminus T}\}}\quad\text{\deleted{bord}}\\
 &\text{\deleted{\unsure{frontière dans la top.|frontière dans la top}}}\\
 &\text{\deleted{absolu de $T$ $=$ ensemble}}\\
 &\text{\deleted{canonique}}\\
 \deleted{={}\un
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/025_cancelled.jpg

Alignment requires recheck: no flag

Review note: The old frontier wording and crossed T intersection expression remain under broad and local cancellation strokes.

### C-025-U010 (C line 18)

Mechanical state: **no unsure token in aligned span; inspect replacement**. Final aligned line: 18.

Source C token:

```tex
\unsure{canonique}
```

Source C context:

```tex
la top.|frontière dans la top}}}\\
 &\text{\deleted{absolu de $T$ $=$ ensemble}}\\
 &\text{\deleted{\unsure{canonique}}}\\
 \deleted{={}\unsure{T\cap L|T\cap\overline{L}}}&\quad\text{\deleted{fermé de ses extrémités}}\
```

Aligned final span:

```tex
canonique
```

Final context (up to 100 characters either side):

```tex
la top.|frontière dans la top}}}\\
 &\text{\deleted{absolu de $T$ $=$ ensemble}}\\
 &\text{\deleted{canonique}}\\
 \deleted{={}\unsure{T\cap\mathcal L|T\cap\overline{\mathcal L}}}&\quad\text{\deleted{fermé de 
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: resolved from ink

Crop links: crops/025_cancelled.jpg

Alignment requires recheck: no flag

Review note: The letters canonique remain readable under their local cancellation.

### C-025-U011 (C line 19)

Mechanical state: **unsure token(s) overlap changed alignment; inspect**. Final aligned line: 19.

Source C token:

```tex
\unsure{T\cap L|T\cap\overline{L}}
```

Source C context:

```tex
&\text{\deleted{absolu de $T$ $=$ ensemble}}\\
 &\text{\deleted{\unsure{canonique}}}\\
 \deleted{={}\unsure{T\cap L|T\cap\overline{L}}}&\quad\text{\deleted{fermé de ses extrémités}}\\
 &\deleted{(\mathrm{NB}\ \mathrm{card}\,\partial T
```

Aligned final span:

```tex
\unsure{T\cap\mathcal L|T\cap\overline{\mathcal L}}
```

Final context (up to 100 characters either side):

```tex
op}}}\\
 &\text{\deleted{absolu de $T$ $=$ ensemble}}\\
 &\text{\deleted{canonique}}\\
 \deleted{={}\unsure{T\cap\mathcal L|T\cap\overline{\mathcal L}}}&\quad\text{\deleted{fermé de ses extrémités}}\\
 &\deleted{(\mathrm{NB}\ \mathrm{card}\,\partial T
```

Recorded decision at the same ordinal: NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping

Ink disposition: retained uncertainty

Crop links: crops/025_cancelled.jpg

Alignment requires recheck: no flag

Review note: The old frontier wording and crossed T intersection expression remain under broad and local cancellation strokes.

