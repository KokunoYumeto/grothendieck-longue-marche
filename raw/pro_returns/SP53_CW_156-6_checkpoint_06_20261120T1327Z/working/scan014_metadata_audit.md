# Scan014 metadata/text audit

Scope: text and metadata only. Read the three readers' report.json, audit.md and reading.tex, the main crop notes, the locked draft hash file, and packet scan014 C.tex/H.tex. No image was opened, emitted or inspected; no OCR, web research, LaTeX compilation or further-page work occurred. No reader file, decision or script was edited.

## Result

No additional unadjudicated textual discrepancy was found. All 98 reader difference rows (31 R1, 35 R2, 32 R3) are covered by the 28 sections of scan014_main_crop_notes.md. The seven differences among the final reader texts—pair enclosure, upper compatibility construction, suffira certainty, d'apres accent, comma before mais, conceptuel certainty, and reflexivité accent—each have an explicit main disposition.

All three reading.tex hashes match scan014_draft_reading_hashes.json:

| Reader | SHA-256 |
|---|---|
| R1 | 10ef74acc5aae6e783e43a72cf3d9cd0cd6a4c9e6f169b2fcf622dbf72ec40e0 |
| R2 | 071539dce39a7136a5fae3e624b7fb1742790a5c0b50127fd9ba7956c7eaae04 |
| R3 | fd21a75885b28993414a5d5c2cb146a43b1b35c0890480920b1ec206d022fc4b |

## Complete difference coverage

Entries are report difference-ID suffixes (D01 etc.); R2 uses the prefix 014-R2-, while R1/R3 use R1-014-/R3-014-. Multiple report rows can share one inspected crop scope.

| Main note | Scope | R1 | R2 | R3 |
|---|---|---|---|---|
| 01 | optima/optimes | D02 | D02 | D02 |
| 02 | definir | D03 | D03 | D03 |
| 03 | family F alphabet | D04 | D04 | D04 |
| 04 | right note subject, verb and accent | D08–D09 | D07–D09 | D07–D08 |
| 05 | upper compatibility | D07 | D06 | D06 |
| 06 | live initial ll, est, préordre | D11–D12 | D10–D11 | D09–D10 |
| 07 | complete slanted note and punctuation | D14 | D14a–D14d | D13–D15 |
| 08 | deleted and inserted adjectives | D18–D19 | D19–D20 | D19–D20 |
| 09 | reflexivity accent and surtout | D23; S row | S row | S row |
| 10 | tantôt | D29 | D30 | D30 |
| 11 | comme | D01 | D01 | D01 |
| 12 | capital Soit | D05 | D05 | D05 |
| 13 | enclosure gaps | D06 | — | — |
| 14 | ou encore | D13 | D12 | D11 |
| 15 | three-line brace scope | D10 | D13 | D12 |
| 16 | Cela correspond; opening bracket | D15 | D15 | D16; D22 |
| 17 | centre | D16 | D17 | D17 |
| 18 | gravité | D17 | D18 | D18 |
| 19 | et intuitif; closing bracket | D20 | D16; D21 | D21–D22 |
| 20 | sur la | D21 | D22 | D23 |
| 21 | que sur | D22 | D23 | D24 |
| 22 | cela | D24 | D24 | D25 |
| 23 | mettre des | D25 | D25–D26 | D26 |
| 24 | surnombre | D26 | D27 | D27 |
| 25 | de partir | D27 | D28 | D28 |
| 26 | qui | D28 | D29 | D29 |
| 27 | lower compatibility | D30 | D31 | D31 |
| 28 | terminal comma | D31 | D32 | D32 |

Packet C/H introduces no additional substantive textual locus outside that coverage. H's explicit notes are editorial material; its bare body brackets are separately addressed by main notes 16/19 rather than automatically counted as literal manuscript ink. Macro and spacing equivalents do not create extra word or symbol disagreements.

## Ten C doubts

Every reader has ten individual c_doubts records. Their dispositions differ only at suffira and conceptuel. R1 resolves five, R2 six, and R3 four.

| C locus | R1 | R2 | R3 | Main notes |
|---|---|---|---|---|
| optima/optimes | retained | retained | retained | retained |
| definir/définir | resolved | resolved | resolved | definir |
| family mathcal/mathscr F | retained with mathcal/fraktur candidates | same | same | retained with mathcal/fraktur candidates |
| sa/ça | retained | retained | retained | retained |
| suffira/suffit | suffira | suffira | retained | suffira |
| changerai/changeai | changerai | changerai | changerai | changerai |
| pt | resolved | resolved | resolved | pt |
| supposerai | retained | retained | retained | retained |
| deleted conceptuel | retained | resolved | retained | retained |
| tantôt | resolved | resolved | resolved | tantôt |

Main therefore retains five C doubts and resolves five. Four additional uncertainties are explicit: the grave accent in d'apres/d'après, the comma/no-comma before mais in the slanted note, the inserted adjective's second acute, and the initial acute in reflexivité/réflexivité. This gives nine retained uncertainty loci in the planned consolidated reading.

## Inventory and mathematical occurrences

Each reader inventories eleven elements, all marked transcribed: page number 13; opening continuation; display (1.28); upper right caveat; introduction to the former choice; display (1.29); slanted note; lower continuous paragraph; deleted adjective; replacement adjective; and surtout insertion. The texts contain two independent margin macros, one deletion and two insertions. No reader reports a separate diagram, missing block, heading or date.

The sole family-F occurrence is the opening capital, where all readers retain mathcal/fraktur uncertainty. It must not spread to ordinary formula operands. All three texts have the identical formula:

    G\ll F \Longleftrightarrow \exists F' \text{ avec } G\leq F'\preccurlyeq F

That formula contains two plain G occurrences, two unprimed plain F occurrences, and two plain F-prime occurrences. The opening family F is a seventh letter occurrence, separate from those six formula operands.

All three texts have exactly eight leq, nine ll, six preccurlyeq, one equivalence and one existential command. Both compatibility occurrences are present and locally distinguished in the main notes: the display occurrence retains retracing, while the lower occurrence uses the simpler two-path construction. The upper pair enclosure is separately refined to three gaps. No missing or extra prime, family-font propagation, changed relation order, or lost compatibility occurrence was found.

Each reader records the sole S row as only partly confirmed: literal reflexivity and surtout are preserved, and antisymmetry is not substituted. Reader check-events explicitly claim no mathematical verification; any main mathematical check must keep its own provenance.

## Metadata cautions communicated to main

1. The disputed accent of d'après is grave, not acute. The initial main crop note's terminology needed correction.
2. R2's narrative says "three other F operands"; the formula itself correctly has two unprimed F, two F-primes and two G. This is a narrative count error, not a transcription disagreement.
3. R3's S-row box uses the half_b image as its stated source; it must not be interpreted as whole-image coordinates.

Main subsequently reported that the first two cautions were addressed in the final records. This audit did not reopen or review the committed decision.

View-log metadata is internally consistent: R1 has one whole, two halves and ten crops (13 entries); R2/R3 each have one whole, two halves and nine crops (12 entries). Each reader's image paths are unique within its log. This is a metadata check, not an independent verification of historical image viewing.

