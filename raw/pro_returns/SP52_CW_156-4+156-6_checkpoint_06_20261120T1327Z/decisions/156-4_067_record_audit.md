# Administrative record audit — 156-4 scan 067

Run: `/root/audit_067_records`. This is a text-only comparison of the three reader returns, C.tex, H.tex, and C_context.md. It is not a fourth reading. No manuscript image was opened, no ink decision was made, and no mathematical statement was checked. The audit does not alter any reader return or the consolidated page.

## Additions to an R1-based record

1. **Punctuation between the first saturated definition and the next Partie** is a previously unlisted disagreement in R1. R2-D057 reads `\unsure{-|.}`; C, H, R1, and R3 have a period. R2 cites `readers/156-4_067/R2/crops/16_saturee_heading.jpg` and describes a separate short horizontal stroke after the closing parenthesis. This needs root adjudication and a three-reader dispute entry even if the final retains the period. If the doubt survives, add a remaining-doubt and C/H difference row.
2. **Accent in déterminent in the left note**: R2-D025 and R3-D030 retain `\unsure{déterminent|determinent}`, while R1, C, and H have definite déterminent. Root has already flagged this. R1 has no difference row for this separate locus. R3 cites `readers/156-4_067/R3/crops/05_left_note.jpg`; R2 cites its crop 06.
3. **The M₀ insertion leader**: R2-D059 and inventory I39 record a curved diagonal insertion stroke that R1/R3 omit from their drawings and inventories. R2 cites `readers/156-4_067/R2/crops/17_saturee_second.jpg`. Root has already flagged this. Add a drawing difference against both witnesses and a drawing inventory element, with the adjoining words present only once.

The other R2/R3 additions are splits or refinements of loci already present in R1: separate top enclosure and long continuation curve; separate right enclosure/underline/subject placement; separate Sup punctuation; separate singular sous-figure; separate final row placement and missing punctuation. They can remain consolidated if the final row explicitly covers every component and supplies the final drawing rather than merely its unchanged text label.

## Three-reader disagreements to preserve

| Locus | R1 | R2 | R3 |
|---|---|---|---|
| Second disjoint article | definite de | de/des | de/des |
| Second top phi | Phi/varphi | varphi/Phi | varphi/Phi |
| Second top closure | one brace | parenthesis+brace / brace | brace / parenthesis+brace |
| Left déterminent accent | definite accent | accented/unaccented | accented/unaccented |
| Left pointer | definite arrow | definite arrow | uncertain arrow / terminal hook |
| Top enclosure and long continuation | two curves, short descending branch; simpler geometry | explicit enclosing contour, branch and long bent continuation | contour, branch and long bent continuation; different geometry |
| Right marginal enclosure | angular arm plus two curves | angular arm plus two curves | angular arm plus one enclosing continuation |
| Sup/Supp | Sup first | Supp first | Sup first |
| After passage | colon/à | definite colon | à/colon |
| Two points after lower altered subscript | `..`/colon, inside subscript | uncertain colon outside subscript | two points/colon outside subscript |
| Lower tt/forall sign | tt first | tt first | forall first |
| Before constructions | ramené/revenu | ramené/revenu | definite ramené |
| Old M under first heading family | uncertain M | definite M | uncertain M |
| Punctuation after first saturated definition | period | dash/period | period |
| M₀ insertion leader | omitted | drawn | omitted |
| Second saturée accent | accented first | accented first | unaccented first |
| Final mutuellement | uncertain | uncertain | definite |

Geometry differences should be adjudicated as differences in the reproduced strokes and their attachment, not merely as different numerical coordinates in otherwise equivalent TikZ.

## C-doubt and context coverage

R1 has all **26 explicit C.tex doubt occurrences**, plus **30 C_context rows**. R2 and R3 contain no additional C-doubt locus absent from this union. Their smaller counts reflect grouped or omitted duplicate context dispositions, not a new substantive C question.

When changing a final decision, also update the repeated context rows. The main duplicated groups are:

- Second closure: C.tex doubt 06; context rows 06 and 29.
- Second phi: C.tex doubt 05; context row 22.
- Second article: C.tex doubt 04; context row 28, which combines both clauses.
- tt/forall: C.tex doubt 20; context rows 05 and 15.
- Sup/Supp and passage: C.tex doubts 15–16; context row 25 combines them.
- Ramené: C.tex doubt 21; context row 16.
- Old heading M: C.tex doubt 23; context row 18.
- Second saturée: C.tex doubt 24; context row 19.
- Final mutuellement: C.tex doubt 25; context row 20.

R1 context row 27 gives only `\operatorname{cosup}` as its reading, despite a source location covering operators in the cancelled and lower definitions. Qualify the disposition so that it does not imply one p everywhere: the renewed cancelled family-prime equation and the live family-double-prime definition retain two-p cosupp, and both right-hand support operators retain supp. The reading.tex itself already makes these distinctions.

The context's earlier audit prose claims an acute in déterminent and describes some operators as cosupp or passage aux sous-figures. These are draft observations, not additional authoritative readings. Root's final record can explicitly supersede the old accent claim if the local ink leaves it uncertain.

## Inventory union

R1's 39 elements cover all other physical groups identified by R2/R3. Add the **M₀ leader drawing** from R2 I39. The remaining count differences arise from granularity:

- R3 I28 lists the inline union as a display, whereas R1 includes it in the middle paragraph element I24.
- R2/R3 list the section sign separately, whereas R1 includes it in concluding text I31.
- R3 splits the two cancelled middle-row equations and the two final displayed rows; R1 groups each pair.
- R2 lists the added third equation and its insertion state separately; R1 lists the whole inserted equation once.
- R2 divides the first saturated heading and its continuation into two text rows; R1 groups them.

No extra textual block absent from R1 was found. A dedicated inline-union row and separate final-equation rows are optional granularity improvements; they should not introduce duplicated transcription. Update R1 I17's definite arrow description if root keeps the pointer uncertain. Likewise update descriptions of the old heading M and uncertain accents to match the final text.

## Record accuracy and consistency

- **R1 D042 misquotes C**: its shortened C field drops both primes and C's uncertainty on mutuellement. Replace it with the exact C margin text or use an empty field specifically scoped to the omitted pointer. H does explicitly describe the arrow in an editorial note; avoid saying H has no mention of it, although H does not draw it.
- **R1 D031 has identical C and reading snippets but change_c=true** because the added connector is absent from C. Make that graphic difference explicit in the final-reading field or split out the connector; otherwise the count appears unsupported. D026 and D047 similarly need the actual consolidated figure or a precise figure reference, not only the unchanged labels.
- **R1 D051** has a reading including the comma but a C snippet excluding it, even though C already has that comma. Quote matching scopes or split the word and punctuation so change_c=false remains clear.
- **R1 D053 marked_in_h=yes** is supportable through H's editorial note calling “passage aux sous-figures” a probable reading, even though the transcription itself has no uncertainty macro. State that source of the flag if needed.
- **R1 D036** already covers the isolated cancelled phi's form and displaced position; R2-D067 and R3-D026 do not require a duplicate row. R3-D026's abbreviated C snippet omits the intervening cancelled equation and line break, so use exact source text if quoting placement.
- **R1 D073** combines final placement and the absence of a terminal period; R3 D083/D085 and R2 D064/D066 split them. The consolidated row must cite evidence for both. Root has already noted that the earlier tight bottom crop did not expose all space after the brace.
- Preserve the differing confidence judgments in reader returns, but use root confidence in the consolidated table. Counts of reader differences are not directly comparable because one report groups several operators or alphabet occurrences while another splits them.

All three reports have empty `check_events` lists. Their notes describe transcription, attention prompted by formula structure, and authorial revisions; none claims a proof or computation. This audit adds no check event.
