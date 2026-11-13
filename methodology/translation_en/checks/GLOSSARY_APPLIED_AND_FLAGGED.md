# The glossary and notation tables in this translation

Tables: `C:\Users\user\Documents\translation_glossary_20261110` (GLOSSARY_LM.csv, NOTATION_LM.csv, TYPESETTING.csv;
built from `scripts\entries_LM.txt`, `notation_LM.txt`, `typesetting.txt`; decisions of 10 and 11 Nov 2026).

## Applied

- **Glossary (all 116 entries of entries_LM.txt).** Every request carries the term lines (`scripts/terms_LM.txt`) of
  the entries whose French occurs on its scans, found with the glossary's own patterns (word start, longest match).
  The check (`scripts/check_units.py`) looks for the English form on the same scan: 100 entries at level "fail", 16 at
  level "review" (the 7 of section E, his abbreviations, of which "m̄ (même)" has no pattern and is checked as a
  formula instead; and 9 whose pattern also catches ordinary senses: carte, centre, genre/bord, transitif, tordre,
  chemin, échelon, champ, extérieurement). Includes the two decisions of 11 Nov
  ("action effective" opposed to the outer action: "actual action"; "sans doute": "probably").
- **NOTATION_LM, the decisions that act on the prose**: his abbreviations written out ("ssi" is "iff"); his "même"
  written m with a bar, which the transcription sets as a formula of its own ($\overline{\mathrm m}$), written out as
  "same", "even" or "itself" (only where the formula is nothing but the shorthand; inside a larger formula it is
  copied); his underlining kept as `\uline` (and `\uuline`); the apparatus macros kept with their content translated;
  quotation marks written ``...'' (TYPESETTING, LM: quotation marks).

## Listed, not applied

**Flagged in the tables (PENDING, "not decided": to be settled on the scans once for the whole manuscript):**

1. NOTATION_LM "the letters script S and script G" (and TYPESETTING "the script capital read as Fraktur S or
   calligraphic G"): `\mathfrak{S}`, `\mathcal{G}`, `\mathcal{S}`, `\mathfrak{G}`. The English keeps each reading as the
   French has it, with its doubt marks.
2. NOTATION_LM "the signs natural and sharp as exponents" (and TYPESETTING "the exponent sign read as natural or
   sharp"): `\natural`, `\sharp` (683 doubt marks). The English keeps the French readings.

**Decided, but acting inside formulas, which this translation keeps character for character** (the method of the
Dérivateurs translation: "Do not change the notation in formulas: it is unified later, in both languages"; TYPESETTING
says its forms are unified in both languages):

- NOTATION_LM: Sl, Gl to `\mathrm{SL}`, `\mathrm{GL}`; GP(n) with "= PGL(2)" at the first occurrence; "equal by
  definition" as `\overset{\mathrm{def}}{=}` (the French word "déf" inside `\text{...}` of a formula is translated as
  wording, where it is in a text box); Centr/Cent to `\operatorname{Centr}`; Norm, Transp; Aut, Autext,
  `\operatorname{Aut}_{\mathrm{lac}}`; int(g); the Teichmüller groups `\mathcal{T}_{g,\nu}`; `\ell` for the loops;
  `\mathbb{Z}`, `\widehat{\mathbb{Z}}`; `\mathbb{G}_m`, `\mathbb{P}^1`, `\mathbb{D}_n`, `\mathbb{S}`; `\simeq` and
  `\xrightarrow{\sim}`; `\varnothing`, `\setminus`; congruences `\pmod{n}`; equation numbers `\tag{n}` (the
  transcription has `\tag{n}` 1,256 times and `(n)\qquad` 1,401 times).
- TYPESETTING (LM): the doubled Gamma as one macro `\GQ`; `\widetilde`/`\overline`; `\operatorname` for operators;
  `\ell`; `\to` in the text and `\longrightarrow` in displays; `\mathbb` for doubled capitals; `\varepsilon`,
  `\varphi`; `\varnothing`, `\setminus`; `\xrightarrow{\sim}`; `\tag{n}`; `\mathcal` for calligraphic capitals;
  `\text{...}` for words inside formulas; `\underline{\underline{...}}` only for doubly underlined symbols.
- NOTATION_LM entries whose English form is "as he writes" or "unchanged" need nothing: Π_1/π_1, the groups with
  loops (Π, Π-hat, π), the profinite completions (single and double hat), M_{g,ν} and its variants, the absolute Galois
  group (doubled Γ against Γ: kept as written), the other exponents (!, +, circle, tilde, wedge).
