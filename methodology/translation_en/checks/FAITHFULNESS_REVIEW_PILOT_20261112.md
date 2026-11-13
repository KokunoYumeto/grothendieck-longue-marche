# Faithfulness review of the English pilot of *La Longue Marche* (12 Nov 2026)

Reviewer: Claude Opus 5.5 (Claude Code, a subagent), 12 Nov 2026, 19:50 UTC. Read only: no translation file, prompt or
script was changed, no API run was started, nothing was published.

**What was read.** The seven pilot units (48 scans), each French unit (`source/units/<unit>.tex`) beside its English
(`translation/units/<package>/<unit>.tex`, the output plus the one fix of `checks/FIXES.jsonl`), sentence by sentence,
with the deletions, insertions and margin notes; the seven prompts as sent (`prompt/system/<unit>.txt`, from
`prompt/PROMPT_TEMPLATE.txt` and `prompt/PROMPT_PARTS_LM_pilot.txt`); the glossary and notation decisions
(`checks/GLOSSARY_APPLIED_AND_FLAGGED.md`; `translation_glossary_20261110\GLOSSARY_LM.csv`, `NOTATION_LM.csv`,
`README.md`). The scripted checks (formulas, anchors, paragraphs, marks) were not repeated. The scans were not looked
at. To judge whether a finding will recur, the 245 French units were searched by pattern; the counts are given where
they bear on the verdict.

**Severity.** *Medium*: the English drops, adds or alters content, or a term or a completion could make a mathematician
read a different statement. *Low*: a term, wording or apparatus detail that a reader would most likely see through, or
a consistency point.

## Summary

17 findings in 48 scans: 6 medium, 11 low. Sentence by sentence the English is complete and in order, and keeps his
hesitations and the status of each claim: "sans doute" is "probably" (three places), "il devrait y avoir" "there should be",
"conjecturalement" "conjecturally", "(pro-fini ???)" "(pro-finite ???)", "\unsure{??|?!}" kept, "Théorème (!)",
"Lemme (!)" and "Corollaire au lemme dubitatif" kept as such, "On doit avoir en effet ceci" "We should indeed have
this", "que nous laissons en suspens" "which we leave open", the margin "Ce n'est \uline{démontré} pour le moment dans
\uline{aucun} cas anabélien profini !" with both underlinings. Quantifiers ("tt", "pour tt $\bar s$, il existe",
$\forall$, "tant ... que") and the referents of pronouns ("cette dernière", "en", "lui") are right everywhere. Where his
French is broken, the English is broken the same way ("il devrait y avoir encore y avoir": "there should be still be";
"me limiter ... le cas": "restrict myself ... the case"). His opération and action are kept apart throughout.

One finding touches a statement (a negation completed across an illegible gap, scan 148). Twelve come from gaps in
what the prompt covers, which will recur in the remaining units unless the prompt says more: his "même" (m with a bar)
inside a two-reading doubt (3); "hom" written out as "homomorphism" where the maps are morphisms of schemes, pairs or
sheaves of sets (5); "loc. cit.", "soit" and "autom. à lacets" (3); a French word inside a formula (1). The other four
are one-offs. The scripts' review points (scan 133 "extérieurement", scan 11 "dévissages", scans 114 and 120 terms
found fewer times) are not faults (see the units).

## The units

### 1. LM_P012_s111-120 (cote 140-2, scans 111-120)

**Verdict: faithful; 6 low findings.** The loop structure (§13 bis), the degree $d$, the Kummer data and Artin's
description of étale sheaves come through with their hypotheses, quantifiers and doubts. The scripts' two review points
are not faults: on scan 114 "(pro-fini ???)" became "(pro-finite ???)", which the pattern for "profinite" misses; on
scan 120 the French pattern "topos étale" matched "\deleted{topos} étales", whose English is "\deleted{topoi} étale".

| scan | French | English | problem | proposed English |
|---|---|---|---|---|
| 111 | `Les hom $(X',S')\xrightarrow{f}(X,S)$ [$S'\supset f^{-1}(S)$, $f$ dominant]` | `The homomorphisms $(X',S')\xrightarrow{f}(X,S)$` | Term (low). These are dominant morphisms of pairs of schemes; the glossary's one rule writes every "hom" out as "homomorphism". | `The morphisms $(X',S')\xrightarrow{f}(X,S)$` |
| 114 | `le groupe des autom \unsure{gal.\|ext.} à lacets de $\pi$` | `the group of \unsure{Galois\|outer} automorphisms with loops of $\pi$` | Term (low). The glossary has no entry for "autom. à lacets"; the C3 units write "loop automorphism" (5 places); "automorphisms with loops" reads as automorphisms that carry loops. | `the group of \unsure{Galois\|outer} loop automorphisms of $\pi$` |
| 116 | `$g=1$, $\nu\unsure{\le\|=}0\deleted{\unsure{ou 1}}$]` | the same, character for character | Content (low). His struck "ou 1" (or 1) stands inside the formula, outside `\text`, so the formula rule kept it in French. | `$\nu\unsure{\le\|=}0\deleted{\unsure{\text{or }1}}$` (the formula check then needs a waiver) |
| 117 | `Notons que [si $\nu\ne0$, \inserted{et]} sauf les cas` | `Note that [if $\nu\ne0$, \inserted{and}] except for the` | Apparatus (low). The closing bracket is part of what he inserted; the English moves it out of the insertion. | `Note that [if $\nu\ne0$, \inserted{and]} except for the` |
| 119 | `et $\varphi$ un hom` (from the sheaf $F_S$ to $j^{*}i_{*}(F_U)$; sheaves of sets, "d'ens." inserted above) | `and $\varphi$ a homomorphism` | Term (low): a morphism of sheaves of sets. | `and $\varphi$ a morphism` |
| 120 | `un hom. de faisceaux $F_D\to\sigma_{*}\rho^{*}F_U$` | `a homomorphism of sheaves $F_D\to\sigma_{*}\rho^{*}F_U$` | Term (low), as on scan 119. | `a morphism of sheaves $F_D\to\sigma_{*}\rho^{*}F_U$` |

### 2. LM_C3-131-149_s131-138 (cote 140-3, scans 131-138)

**Verdict: faithful; no findings.** The setting-up of the equations in $\mathrm{Sl}(2,\widehat{\mathbb Z})$, the
change of letters ($g_0$ to $f_0$, $p$ to $\mu$, $f_0$ to $f_0^{-1}$) with his reasons, the loop relation (11) and the
parametrization (13)-(16) are exact. The script's review point: "commutant extérieurement" (scan 133) became "commuting
up to inner automorphisms", which says exactly what the French means and follows the glossary's decision (an English
phrase, no adverb). His insertion that turns "prend" into "prendrait" became "\inserted{\unsure{would}} therefore take",
which carries the change of mood.

### 3. LM_C3-131-149_s139-144 (cote 140-3, scans 139-144)

**Verdict: faithful; 1 low finding.** The equations in $\varphi,\xi$ and in $\psi,\eta$, the condition on the
"principal family", the remarks on the indeterminacy of $f$ and on the multiplier $-\mu$ are exact; the subjunctive
"\unsure{appartient|appartienne}" is even kept as "\unsure{belongs|belong}".

| scan | French | English | problem | proposed English |
|---|---|---|---|---|
| 141 | `soit (en passant à l'inverse)` ... `=1 \quad\text{soit}\quad \underbrace{\ell_0^{-\nu}\psi}_{\eta}` ... `\deleted{soit}` | `or (passing to the inverse)` ... `=1 \quad\text{or}\quad` ... `\deleted{or}` | Misleading wording (low). His "soit" restates the equation just written ("that is"); "or" between two displayed equations can be read as a disjunction. Scan 136 renders the same "soit" as "that is". | `i.e. (passing to the inverse)` ... `\quad\text{i.e.}\quad` ... `\deleted{i.e.}` |

### 4. LM_C3-131-149_s145-149 (cote 140-3, scans 145-149)

**Verdict: faithful except one margin note; 1 medium, 1 low.** The sign questions in $\mathrm{Gl}(2,\widehat{\mathbb
Z})$ (the question "sont elles vraies sans \uline{signe} correcteur ??|?!", the equivalence of the two sign questions,
the formulas (45)-(56)) are exact; "or $\xi$ donné par (42)" is rightly "now $\xi$ given by (42)"; his m with a bar is
written out four times ("same letters", "Likewise", "and likewise $g$", "\deleted{likewise}").

| scan | French | English | problem | proposed English |
|---|---|---|---|---|
| 145 | `Dans le choix des \deleted{\unsure{repr}} représentants` | `In the choice of the \deleted{\unsure{representatives}} representatives` | Normalizes (low). He broke the word off and struck it; the English completes it. | `In the choice of the \deleted{\unsure{repr}} representatives` |
| 148 (margin) | `--- \unsure{le signe} \illegible{1} \unsure{n'intervient} \illegible{3} \unsure{dans} $\xi=\varepsilon\ell_0^\nu\varphi$.` | `--- \unsure{the sign} \illegible{1} \unsure{does not occur} \illegible{3} \unsure{in} $\xi=\varepsilon\ell_0^\nu\varphi$.` | Negation (medium). The second half of "ne" is among the three illegible words: "n'intervient pas" (does not occur) or "n'intervient que" (occurs only). The English decides for "not", although the formula he names contains the sign $\varepsilon$. | Read the three words on scan 148; if they stay illegible, `\unsure{does not occur\|only occurs}` (one bar more than the French: the bar count needs a waiver) |

### 5. LM_C4-001-019_s1-8 (cote 140-4, scans 1-8)

**Verdict: faithful except his "même" in a two-reading doubt; 3 medium findings, to fix.** The table of contents
(deletions and insertions of the titles included), the definitions of unipotent and quasi-unipotent sections, the
descent argument and the reduction to a trait are exact; the printed footers and comment lines are copied. The three
findings have one cause: this unit's three m-bar formulas are all of the form `$\unsure{\overline{\mathrm m}|=}$`,
which `scripts/common_lm.py` (`MBAR`) does not recognize, so `prepare.py` did not put the m-bar line in this unit's
prompt, the model kept the formulas, and the check counted them as ordinary formulas.

| scan | French | English | problem | proposed English |
|---|---|---|---|---|
| 6 | `alors $\varphi$ existe (sur $S$ lui $\unsure{\overline{\mathrm m}\|=}$).` | `then $\varphi$ exists (over $S$ itself $\unsure{\overline{\mathrm m}\|=}$).` | Content (medium). "lui même" is written out as "itself", and his shorthand for "même" is left beside it as a formula: the word twice, once in French shorthand. | `then $\varphi$ exists (over $S$ \unsure{itself\|=}).` |
| 8 | `En fait, on n'est pas $\unsure{\overline{\mathrm m}\|=}$ sûr que` | `In fact, we are not $\unsure{\overline{\mathrm m}\|=}$ sure that` | Content (medium). "même" (even) is not translated; the reader of the English gets "not m̄ sure". | `In fact, we are not \unsure{even\|=} sure that` |
| 8 | `il pourrait $\unsure{\overline{\mathrm m}\|=}$ être l'hom trivial` | `it could $\unsure{\overline{\mathrm m}\|=}$ be the trivial homomorphism` | Content (medium), as above. | `it could \unsure{even\|=} be the trivial homomorphism` |

### 6. LM_C4-001-019_s9-13 (cote 140-4, scans 9-13)

**Verdict: faithful; no findings.** The case $n=4$ in residual characteristic 2, the "Théorème (!)" on quasi-unipotent
sections, the "Lemme (!)", the logarithm argument in the margin and the "Corollaire au lemme \unsure{dubitatif}" are
exact; "lui-$\overline{\mathrm m}$" is "itself", "inégales caractéristiques" "mixed characteristic". The script's review
point: "dévissages" is kept in French, as the glossary decides.

### 7. LM_C4-001-019_s14-19 (cote 140-4, scans 14-19)

**Verdict: faithful; 2 medium and 3 low findings.** The proposition on extending $\varphi_U\circ u_m$, its proof, the
corollary and the construction of $\underline{\mathfrak S}$ are exact; "OPS" is "We may assume", "il f et s." "it is
necessary and sufficient", the "Groupe" with a capital kept.

| scan | French | English | problem | proposed English |
|---|---|---|---|---|
| 15 | `il suffit de prouver que $\varphi_U$ se prolonge en un hom de schémas \deleted{en groupes} -- \inserted{ce} prolongement sera automatiquement un hom de sch. en groupes.` | `it suffices to prove that $\varphi_U$ extends to a homomorphism of \deleted{group} schemes -- \inserted{this} extension will automatically be a homomorphism of group schemes.` | Term (medium). The deletion records his point: it is enough to extend $\varphi_U$ as a morphism of schemes, the group structure then follows. "homomorphism of schemes" blurs the two. | `it suffices to prove that $\varphi_U$ extends to a morphism of \deleted{group} schemes -- \inserted{this} extension will automatically be a homomorphism of group schemes.` |
| 16 | `(il n'est plus question de structure de groupes), et $\varphi_U:\mathbb E^1_U\longrightarrow G_U$ un hom de schémas,` | `(there is no longer any question of a group structure), and $\varphi_U:\mathbb E^1_U\longrightarrow G_U$ a homomorphism of schemes,` | Term (medium). Right after he sets the group structure aside, the English calls the map a homomorphism. | `... and $\varphi_U:\mathbb E^1_U\longrightarrow G_U$ a morphism of schemes,` |
| 16 | `le "théorème" \unsure{dubitatif} p.\unsure{662\|652}'` | `the \unsure{tentative} ``theorem'' on page \unsure{662\|652}'` | Doubt (low). "dubitatif" says that he doubts it; "tentative" says only that it is provisional. Scan 13 renders the same word "dubious". | `the \unsure{dubious} ``theorem'' on page \unsure{662\|652}'` |
| 19 | `de loc. cit. Par la construction \unsure{du\|de} loc. cit., on construit` | `of the passage cited. By the construction \unsure{of the\|of} passage cited, we construct` | Normalizes (low). "loc. cit." is used as it is in English; the second rendering also reads badly. | `of loc. cit. By the construction \unsure{of\|of} loc. cit., we construct` |
| 19 | `\unsure{contr. foncteur\|contre-foncteur}` | `\unsure{contravariant functor\|counter-functor}` | Term (low). "counter-functor" is a new word; his coinage "contrafoncteur" is "contrafunctor" in the English of Les Dérivateurs (GLOSSARY_DER). | `\unsure{contravariant functor\|contrafunctor}` |

## Doubt marks with two readings

Every `\unsure{A|B}` keeps both readings, in order. Where English can show the difference it does: "appartient|appartienne"
belongs|belong, "défini|définit" defined|defines, "natures différentes|nature différente" different natures|a different
nature, "où|ou" where|or, "dont|donc" of which|thus, "trouvera|trouve" shall find|find, "aura|a" will have|have. In 12
places the two French readings differ only in French grammar or spelling and give the same English (des|du, les|le,
néc.|nécess., exprimé|exprimée, lacets|lacet, tjrs|tjs, unipotente|unipotent, id°|idem, ait|a, Soient|Soit,
premier|prem., constante|const.): the English writes the word twice ("of the|of the"). That is correct, since the doubt
does not bear on the English; it follows from the check that counts the bars.

## Observations not counted as findings

- **Raised endings of his abbreviations.** The prompt keeps every macro and writes his abbreviations out, so the English
  grafts his raised ending onto an English word: "essential\textsuperscript{ly}" (scan 120),
  "necessaril\textsuperscript{y}" (scan 12), "characterizatio\textsuperscript{n}" (scan 3). Not misleading; the book has
  131 such abbreviations. For a plain word, the prompt would say to write the abbreviation out without
  `\textsuperscript`, and the macro count of `check_units.py` would allow it.
- "id" in the table of contents is "same" (scans 3, 4); "idem" would keep his Latin.
- "jauge" is "gauge" (scans 9, 12): literal, as the method requires for his wording (or a reading to settle on the scan).
- "déf" and "dfn" over equals signs stay inside the formulas (scans 15, 16, 141, 148): deferred to the notation
  unification, as `GLOSSARY_APPLIED_AND_FLAGGED.md` says.

## Findings by kind

| kind | scans | count |
|---|---|---|
| changes the mathematics (a negation completed) | 148 | 1 |
| drops or adds content | 116 ("ou 1" left in French); 6, 8, 8 (his "même") | 4 |
| technical term | 111, 114, 119, 120 (LM_P012); 15, 16, 19 (LM_C4) | 7 |
| flattens a doubt | 16 ("dubitatif") | 1 |
| normalizes his wording or the apparatus | 117 (bracket), 145 ("repr"), 19 ("loc. cit.") | 3 |
| misleading wording | 141 ("soit") | 1 |
| **all** | 6 medium (148, 6, 8, 8, 15, 16), 11 low | **17** |

## Overall verdict

**Not as is. After the three required changes below (and preferably the two recommended ones), yes.** The model, the
effort, the template and the handling of the apparatus need no change: in 48 scans no sentence, clause or mark is left
out or added, and only one statement is touched, by a completion across an illegible gap. The words lost, doubled or
left in French (his "même" three times, "ou 1" once) come from what the prompt covers, and that is what needs
changing. Searched over all 245 French units, the gaps the pilot shows recur in the remaining 238:

- his m with a bar where the prompt's rule does not reach it: 31 places in the book, 3 of them in the pilot (all 3
  wrong); 22 are `$\unsure{\overline{\mathrm m}|=}$` and the like (19 in the remaining units), 4 sit inside a larger
  formula (three of them with a plural ending, $\overline{\mathrm m}^{s}$), 5 stand inside a display formula beside
  `\text{...}`. Without a change, the English keeps the French shorthand there or loses the word; the 449 standalone
  ones are covered (the pilot wrote all 7 out correctly);
- "hom" for morphisms of schemes, topoi, pairs $(X,S)$ and sheaves of sets (about 840 "hom" outside formulas in the
  book; by pattern at least "hom de topos" in LM_P011 and LM_P014 besides the pilot's 5). His own English says
  "morphism of topoi" (Pursuing Stacks, 17 times) and never "homomorphism of topoi";
- "loc. cit." (17 more places), "\text{soit}" between formulas (24 more), "autom./hom. à lacets" (20 more).

The 7 pilot units need no re-run: the 17 proposed English strings above can go into `checks/FIXES.jsonl` as replace
entries once approved. The fixes of scans 6 and 8 pass the formula check only after the `MBAR` change below; those of
scans 116 and 148 (if given two readings) need a waiver.

## Changes to the prompt

### Change 1 (required): his "même" in every form

`prompt/PROMPT_PARTS_LM.txt`, section `@@ SLOT MBAR`. Replace the line

```
- His "même" is written m with a bar, which the transcription sets as a formula of its own ($\overline{\mathrm m}$, also \(\overline{\mathrm m}\) or $\unsure{\overline{\mathrm m}}$): write it out as the English word the sentence needs (same, even, itself), without the formula; where the formula has \unsure, keep \unsure around the word. Inside a larger formula the shorthand is copied with the formula.
```

with

```
- His "même" is written m with a bar, which the transcription sets as a formula of its own ($\overline{\mathrm m}$, also \(\overline{\mathrm m}\) or $\unsure{\overline{\mathrm m}}$; in the plural $\overline{\mathrm m}^{s}$ or $\overline{\mathrm m}\mathrm{s}$; or as one of two readings, $\unsure{\overline{\mathrm m}|=}$): write it out as the English word the sentence needs (same, even, itself, likewise), without the formula. Never leave the formula beside the word, and never drop the word. Where the formula has \unsure, keep \unsure around the word; where the m with a bar is one of two readings, keep both readings in their order, the word for the m with a bar and the other reading as plain text: $\unsure{\overline{\mathrm m}|=}$ becomes \unsure{even|=} (or same, itself, likewise). "lui $\overline{\mathrm m}$" and "lui-$\overline{\mathrm m}$" are "itself"; "de $\overline{\mathrm m}$" is "likewise". Inside any other formula the shorthand is copied with the formula.
```

This change works only with the matching change of the scripts (not made here): in `scripts/common_lm.py`, `MBAR` must
also match a formula that is nothing but `\unsure{` m-bar `|` a sign `}` or `\unsure{` a sign `|` m-bar `}` (the sign
`=` or `\simeq`), and m-bar with a plural ending (`^{s}`, `^{\mathrm s}`, `\mathrm{s}`). Then `prepare.py` sends the
m-bar line to the units that have only these forms (LM_C4-001-019_s1-8 was sent without it), and `check_units.py`
leaves them out of the formula comparison on both sides. The `\unsure` and bar counts already include formulas and
text, so `\unsure{even|=}` keeps them equal.

### Change 2 (required): "soit" and Latin

`prompt/PROMPT_PARTS_LM.txt`, section `@@ LM STYLE`. After `"ssi" is "iff".` and before `<<MORE_STYLE>>`, insert a line
break and these two lines:

```
- "soit" that restates the formula before it ("; soit", "soit (en passant à l'inverse)", \text{soit} between two formulas) is "i.e." or "that is", never "or"; "soit X ..." that introduces an object is "let X be".
- Latin stays Latin: loc. cit., op. cit., a priori, cf., i.e. ("loc." alone is local or locally).
```

### Change 3 (required): "hom" for morphisms

`scripts/terms_LM.txt`, entry `hom, isom, autom` (and the note of the same entry in
`translation_glossary_20261110\scripts\entries_LM.txt`). Replace the prompt line

```
hom, isom, autom, endom → homomorphism, isomorphism, automorphism, endomorphism
```

with

```
hom, isom, autom, endom → homomorphism, isomorphism, automorphism, endomorphism; but "hom" between schemes, preschemes, pairs (X,S), spaces, topoi or sheaves of sets is a morphism ("hom de schémas" morphism of schemes, "hom de topos" morphism of topoi, as in his Pursuing Stacks); "hom de schémas en groupes" stays homomorphism of group schemes
```

and its English pattern `(homo|iso|auto|endo)morph\w*` with `(homo|iso|auto|endo)?morph\w*` (the entry stays at
level review).

### Change 4 (recommended): automorphisms "à lacets"

A new entry, after `sous-groupe à lacets`, in `scripts/terms_LM.txt`:

```
automorphisme à lacets ;; automorphisme (homomorphisme, isomorphisme) à lacets, autom. à lacets → loop automorphism (loop homomorphism, loop isomorphism), as loop structure and loop subgroup; not "automorphism with loops" ;; \bloop[- ](auto|homo|iso)morphisms?\b ;; fail
```

and in `translation_glossary_20261110\scripts\entries_LM.txt` (then `build_glossary.py LM`):

```
automorphisme à lacets ;; \b(autom|automorphismes?|hom|homom|homomorphismes?|isom|isomorphismes?)\b\.?\s+(\S+\s+){0,2}?(à|a)\s+lacets ;; loop automorphism (loop homomorphism, loop isomorphism) ;; ours, as "loop structure", "loop subgroup" ;; PROPOSED (pilot review, 12 Nov): the pilot had "automorphisms with loops" (P012) and "loop automorphisms" (C3).
```

### Change 5 (recommended): what a mark holds

`prompt/PROMPT_PARTS_LM.txt`, section `@@ LM APPARATUS`. After the line that begins `- \unsure{...} is a reading`,
insert:

```
- A mark holds exactly what it holds in the French: a word he broke off stays broken off (\deleted{repr} stays repr), and a bracket or other sign inside a mark stays inside it (\inserted{et]} becomes \inserted{and]}).
```

After the changes, `prepare.py` writes the prompts of the remaining units again; the seven pilot prompts stay as sent.

## Places in the remaining units to look at after the run

Changes 1-5 do not reach these, or the formula check would refuse the right English; each is a hand fix or a waiver:

- French words inside formulas outside `\text`: LM_C3-454-472_s467-472 (`$(\inserted{et}\ \mu,\varepsilon,\varepsilon')$`),
  LM_P018_s171-180 (`$U\simeq\unsure{\mathbb C^*} \unsure{ou} S^1\times S^1$`).
- His m with a bar inside a display beside `\text{...}`, or in a reading of its own: LM_C3-454-472_s454-458,
  LM_C3-492-510_s497-501, LM_C3-587-605_s591-595, LM_C4-134-152_s134-139, LM_P056_s551-560,
  LM_C3-663-681_s672-675 (`$\unsure{\underset{=}{\mathrm m}|\overline{\mathrm m}}$`), LM_P044_s431-440
  (`\unsure{$\mathrm m^{\mathrm s}$|$\overline{\mathrm m}^{\mathrm s}$}`).
- A negation cut by an illegible gap, as on scan 148: LM_C3-207-225_s207-212 (`\unsure{ne couvre} \illegible{2}`),
  LM_P040_s391-400 (`\deleted{On \unsure{ne peut} \illegible{2}}`).
