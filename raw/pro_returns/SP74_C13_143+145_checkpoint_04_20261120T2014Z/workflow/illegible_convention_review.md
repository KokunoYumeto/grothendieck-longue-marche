# Static review of `\illegible` conventions

## Scope

Reader A inspected the accepted `pages/*.tex` files as text only. At the time of this check, the directory contained **22 accepted page files**. Searches included `\illegible` with optional whitespace before its argument and the possible short form `\ill`.

There are **five occurrences of `\illegible{1}` in four files**. No `\ill` occurrence was found. No page image or crop was opened, no page text was changed, and no TeX compilation or page audit was performed. This report records convention candidates, not new readings of the ink.

The relevant distinction is between an unread mathematical symbol and an unread prose word. Being inside a TikZ drawing does not by itself make a text-node annotation mathematical. Conversely, text mode alone does not establish that missing ink was a prose word.

## Loci requiring root or auditor inspection

### 143_scan029.tex, line 40 — formula (2 bis), cancelled material over the equality

```tex
_{\overset{\deleted{\illegible{1}}}{=}\mathcal T_{g,\nu}\ (\text{Teichmüller})}
```

**Needs root/auditor inspection; highest-priority convention candidate.** The placeholder is inside displayed mathematics, in the superscript of an equality that forms part of an underbrace annotation. The TeX does not identify the struck material as a prose word. If it represents a mathematical symbol, the current `\illegible{1}` conflicts with the instruction to retain an explicit uncertain reading for such symbols. A cancelled prose annotation remains possible, so a replacement cannot be chosen statically.

### 143_scan030.tex, line 30 — second placeholder in the deleted TikZ annotation

```tex
\unsure{abélien} $*$ \unsure{est} \illegible{1}
```

**Needs root/auditor inspection to classify the missing content.** This occurrence is outside the node's explicit math delimiters; the only explicit inline mathematics in this excerpt is `$*$`. Nevertheless, the complement after `est` could be a prose word or a mathematical expression. The surrounding TeX does not settle that distinction. Its location inside a drawing is not itself a violation.

### 143_scan031.tex, line 46 — marginal condition

```tex
\margin{(Sans doute il faut condition \unsure{sur le} \illegible{1}, cf NB.}
```

**Needs root/auditor inspection if the missing object has not already been classified.** This is a prose margin annotation, outside displayed mathematics and diagrams. However, the object after `condition sur le` could be a prose noun or a named mathematical parameter. It is therefore not a definite formal-context violation, but the missing ink cannot confidently be labelled an unread prose word from the TeX alone.

## Prose occurrences with no apparent convention conflict

### 143_scan030.tex, line 30 — first placeholder in the deleted TikZ annotation

```tex
\deleted{\unsure{(cas} \illegible{1} \unsure{abélien}
```

**Prose annotation slot.** The placeholder lies between the prose words `(cas` and `abélien`, outside math delimiters, in a deleted sentence placed in a text node. It is not a diagram object or an index. On the static evidence this is an unread prose word, and no convention change is indicated. This classification does not claim to identify the underlying word.

### 143_scan025.tex, line 18 — cancelled word before `suppose`

```tex
\deleted{\unsure{Dans}} \inserted{On} \deleted{\illegible{1}} suppose de plus
```

**Prose word slot.** The placeholder is a cancelled item within an ordinary sentence, between the inserted `On` and `suppose`. It is outside the adjacent inline mathematical expressions. No mathematical-symbol convention conflict is apparent.

## Files covered

`143_scan008.tex`, `143_scan009.tex`, `143_scan010.tex`, `143_scan012.tex`, `143_scan014.tex`, `143_scan015.tex`, `143_scan016.tex`, `143_scan017.tex`, `143_scan018.tex`, `143_scan019.tex`, `143_scan021.tex`, `143_scan022.tex`, `143_scan023.tex`, `143_scan024.tex`, `143_scan025.tex`, `143_scan026.tex`, `143_scan027.tex`, `143_scan028.tex`, `143_scan029.tex`, `143_scan030.tex`, `143_scan031.tex`, and `143_scan034.tex`.

The other 18 files in this snapshot contain neither `\illegible` nor `\ill`. This check does not cover pages accepted after the snapshot; the search should be repeated when all 24 accepted page files are present. No readings or page edits are proposed here.
