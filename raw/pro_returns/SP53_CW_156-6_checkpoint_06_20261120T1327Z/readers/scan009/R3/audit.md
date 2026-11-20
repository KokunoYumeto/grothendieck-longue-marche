# Scan 009 — independent reader R3 audit

## Scope and timing

Read only this page packet, the two exact supplied preambles, the current notation table, and the three exact scan-009 images named by inputs.json. No other page, reader output, consolidated decision, external research, OCR, text recognition, or PDF text extraction was used. No subagent was spawned.

The start timestamp is the earliest recorded UTC clock check after the packet read (2026-11-20 10:02:07 UTC), not an invented second for the initial brief opening.

## Image-view sequence

Each entry below was actually emitted with the image helper. Whole image once for layout; half a once and half b once for line-by-line reading; each of 17 tight crops once. No whole or half was re-viewed or enlarged as a whole. No crop was remade or re-viewed.

- 2026-11-20T10:02:16Z — whole — `/workspace/scratch/42e661864e98/source/SP53_CW_156-6_scans/J156-6-01_156-6_scan009.jpg`
- 2026-11-20T10:02:22Z — half_a — `/workspace/scratch/42e661864e98/source/SP53_CW_156-6_scans/J156-6-01_156-6_scan009_a.jpg`
- 2026-11-20T10:03:05Z — half_b — `/workspace/scratch/42e661864e98/source/SP53_CW_156-6_scans/J156-6-01_156-6_scan009_b.jpg`
- 2026-11-20T10:05:12Z — crop — `/workspace/scratch/42e661864e98/out/readers/scan009/R3/01_family_F.jpg`
- 2026-11-20T10:05:12Z — crop — `/workspace/scratch/42e661864e98/out/readers/scan009/R3/02_equivalence_correction.jpg`
- 2026-11-20T10:05:12Z — crop — `/workspace/scratch/42e661864e98/out/readers/scan009/R3/03_au_sens.jpg`
- 2026-11-20T10:05:12Z — crop — `/workspace/scratch/42e661864e98/out/readers/scan009/R3/04_disjoints_terminal.jpg`
- 2026-11-20T10:06:07Z — crop — `/workspace/scratch/42e661864e98/out/readers/scan009/R3/05_ie_points.jpg`
- 2026-11-20T10:06:07Z — crop — `/workspace/scratch/42e661864e98/out/readers/scan009/R3/06_live_om_equality.jpg`
- 2026-11-20T10:06:07Z — crop — `/workspace/scratch/42e661864e98/out/readers/scan009/R3/07_element.jpg`
- 2026-11-20T10:06:07Z — crop — `/workspace/scratch/42e661864e98/out/readers/scan009/R3/08_elt.jpg`
- 2026-11-20T10:06:07Z — crop — `/workspace/scratch/42e661864e98/out/readers/scan009/R3/09_lieu_communs.jpg`
- 2026-11-20T10:07:08Z — crop — `/workspace/scratch/42e661864e98/out/readers/scan009/R3/10_tout_or_forall.jpg`
- 2026-11-20T10:07:08Z — crop — `/workspace/scratch/42e661864e98/out/readers/scan009/R3/11_disjoint_insertions.jpg`
- 2026-11-20T10:07:08Z — crop — `/workspace/scratch/42e661864e98/out/readers/scan009/R3/12_la_theorie.jpg`
- 2026-11-20T10:07:08Z — crop — `/workspace/scratch/42e661864e98/out/readers/scan009/R3/13_tout_lieu.jpg`
- 2026-11-20T10:07:59Z — crop — `/workspace/scratch/42e661864e98/out/readers/scan009/R3/14_disj_compatibilite.jpg`
- 2026-11-20T10:07:59Z — crop — `/workspace/scratch/42e661864e98/out/readers/scan009/R3/15_sous_ensembles.jpg`
- 2026-11-20T10:07:59Z — crop — `/workspace/scratch/42e661864e98/out/readers/scan009/R3/16_ateliers.jpg`
- 2026-11-20T10:07:59Z — crop — `/workspace/scratch/42e661864e98/out/readers/scan009/R3/17_barred_m.jpg`

## Open loci after the halves and crop decisions

The halves left the following localized questions open. Each received exactly one tight crop; related letters or intervention states within the same local word/formula were kept together. Other discrepancies already settled from the halves (first G, final om(G) and parenthesis, tjrs, quotation-stroke forms, leading dash) have source coordinates in report.json and were not cropped.

### 01_family_F

Reason: Opening family F: identity clear, typographic alphabet undecided.

Source: `/workspace/scratch/42e661864e98/source/SP53_CW_156-6_scans/J156-6-01_156-6_scan009_a.jpg`; original-source box [558, 56, 680, 174]; rotation 0°; output 3000 × 2902 px.

Transform: Pillow crop; autocontrast cutoff 0; LANCZOS resize to 3000 px wide; UnsharpMask radius 1.5, percent 130, threshold 3; JPEG quality 95, subsampling 0.

Reading evidence: One upright and a broad returning top arm establish family F; exact mathcal/fraktur alphabet remains uncertain.

### 02_equivalence_correction

Reason: Inserted pair and canceled original expression; presence/absence of canceled equality in H.

Source: `/workspace/scratch/42e661864e98/source/SP53_CW_156-6_scans/J156-6-01_156-6_scan009_a.jpg`; original-source box [1015, 453, 1664, 575]; rotation 0°; output 3000 × 564 px.

Transform: Pillow crop; autocontrast cutoff 0; LANCZOS resize to 3000 px wide; UnsharpMask radius 1.5, percent 130, threshold 3; JPEG quality 95, subsampling 0.

Reading evidence: Raised omb(F) et omb(G); a separate small lower dash at the canceled formula ending may be an equality bar, but no empty-set glyph follows.

### 03_au_sens

Reason: Preposition before sens: C au versus H en un.

Source: `/workspace/scratch/42e661864e98/source/SP53_CW_156-6_scans/J156-6-01_156-6_scan009_a.jpg`; original-source box [1445, 563, 1668, 616]; rotation 0°; output 3000 × 713 px.

Transform: Pillow crop; autocontrast cutoff 0; LANCZOS resize to 3000 px wide; UnsharpMask radius 1.5, percent 130, threshold 3; JPEG quality 95, subsampling 0.

Reading evidence: One short curved-plus-arch group before sens, not two words; au/un remains uncertain.

### 04_disjoints_terminal

Reason: Final s of disjoints at page edge.

Source: `/workspace/scratch/42e661864e98/source/SP53_CW_156-6_scans/J156-6-01_156-6_scan009_a.jpg`; original-source box [1458, 603, 1668, 670]; rotation 0°; output 3000 × 957 px.

Transform: Pillow crop; autocontrast cutoff 0; LANCZOS resize to 3000 px wide; UnsharpMask radius 1.5, percent 130, threshold 3; JPEG quality 95, subsampling 0.

Reading evidence: Final tall t reaches the photographed edge; no independent s can be isolated.

### 05_ie_points

Reason: Separate dots in i.e. after ensemblistement.

Source: `/workspace/scratch/42e661864e98/source/SP53_CW_156-6_scans/J156-6-01_156-6_scan009_a.jpg`; original-source box [1490, 650, 1643, 710]; rotation 0°; output 3000 × 1176 px.

Transform: Pillow crop; autocontrast cutoff 0; LANCZOS resize to 3000 px wide; UnsharpMask radius 1.5, percent 130, threshold 3; JPEG quality 95, subsampling 0.

Reading evidence: Dot over i, separate intermediate point and separate final point are all present.

### 06_live_om_equality

Reason: Right om/omb and actual equality punctuation.

Source: `/workspace/scratch/42e661864e98/source/SP53_CW_156-6_scans/J156-6-01_156-6_scan009_a.jpg`; original-source box [987, 705, 1663, 781]; rotation 0°; output 3000 × 337 px.

Transform: Pillow crop; autocontrast cutoff 0; LANCZOS resize to 3000 px wide; UnsharpMask radius 1.5, percent 130, threshold 3; JPEG quality 95, subsampling 0.

Reading evidence: The right m is followed by a distinct opening parenthesis with no b; left omb provides a local tall-b comparison.

### 07_element

Reason: Full element versus abbreviated elem superscript t.

Source: `/workspace/scratch/42e661864e98/source/SP53_CW_156-6_scans/J156-6-01_156-6_scan009_a.jpg`; original-source box [1113, 772, 1325, 834]; rotation 0°; output 3000 × 877 px.

Transform: Pillow crop; autocontrast cutoff 0; LANCZOS resize to 3000 px wide; UnsharpMask radius 1.5, percent 130, threshold 3; JPEG quality 95, subsampling 0.

Reading evidence: Tall l and two accent traces, then compressed ending with a raised loop; full element versus abbreviated ending remains uncertain.

### 08_elt

Reason: Abbreviated elt versus element and accents.

Source: `/workspace/scratch/42e661864e98/source/SP53_CW_156-6_scans/J156-6-01_156-6_scan009_a.jpg`; original-source box [1422, 828, 1667, 902]; rotation 0°; output 3000 × 906 px.

Transform: Pillow crop; autocontrast cutoff 0; LANCZOS resize to 3000 px wide; UnsharpMask radius 1.5, percent 130, threshold 3; JPEG quality 95, subsampling 0.

Reading evidence: Short e-l-t group with no separate acute above e; not the full element word.

### 09_lieu_communs

Reason: Number of lieu and commun(s).

Source: `/workspace/scratch/42e661864e98/source/SP53_CW_156-6_scans/J156-6-01_156-6_scan009_a.jpg`; original-source box [945, 1092, 1518, 1171]; rotation 0°; output 3000 × 414 px.

Transform: Pillow crop; autocontrast cutoff 0; LANCZOS resize to 3000 px wide; UnsharpMask radius 1.5, percent 130, threshold 3; JPEG quality 95, subsampling 0.

Reading evidence: No x after lieu; the terminal joined run of commun(s) does not isolate a final s decisively.

### 10_tout_or_forall

Reason: Word tout or universal sign before lieu de lune.

Source: `/workspace/scratch/42e661864e98/source/SP53_CW_156-6_scans/J156-6-01_156-6_scan009_b.jpg`; original-source box [238, 118, 578, 215]; rotation 0°; output 3000 × 856 px.

Transform: Pillow crop; autocontrast cutoff 0; LANCZOS resize to 3000 px wide; UnsharpMask radius 1.5, percent 130, threshold 3; JPEG quality 95, subsampling 0.

Reading evidence: Two terminal t stems, a shared long crossbar and a lower ou-like trace support tout.

### 11_disjoint_insertions

Reason: Canceled com/co and corrected disjoint above original disjoint.

Source: `/workspace/scratch/42e661864e98/source/SP53_CW_156-6_scans/J156-6-01_156-6_scan009_b.jpg`; original-source box [1148, 57, 1447, 210]; rotation 0°; output 3000 × 1535 px.

Transform: Pillow crop; autocontrast cutoff 0; LANCZOS resize to 3000 px wide; UnsharpMask radius 1.5, percent 130, threshold 3; JPEG quality 95, subsampling 0.

Reading evidence: Canceled base disjoint; canceled c-o-m on an intermediate line; live disjoint above it.

### 12_la_theorie

Reason: Deletion boundaries and surviving l apostrophe before atelier.

Source: `/workspace/scratch/42e661864e98/source/SP53_CW_156-6_scans/J156-6-01_156-6_scan009_b.jpg`; original-source box [515, 195, 1190, 312]; rotation 0°; output 3000 × 520 px.

Transform: Pillow crop; autocontrast cutoff 0; LANCZOS resize to 3000 px wide; UnsharpMask radius 1.5, percent 130, threshold 3; JPEG quality 95, subsampling 0.

Reading evidence: Single surviving l loop; heavily blackened a-like ending of uncertain canceled state; added apostrophe; distinct strike through theorie.

### 13_tout_lieu

Reason: Possible strike through tout and final lieu/lieux.

Source: `/workspace/scratch/42e661864e98/source/SP53_CW_156-6_scans/J156-6-01_156-6_scan009_b.jpg`; original-source box [1190, 202, 1667, 304]; rotation 0°; output 3000 × 642 px.

Transform: Pillow crop; autocontrast cutoff 0; LANCZOS resize to 3000 px wide; UnsharpMask radius 1.5, percent 130, threshold 3; JPEG quality 95, subsampling 0.

Reading evidence: The horizontal through tout is the common t crossbar, not a second cancellation; lieu has no separate x.

### 14_disj_compatibilite

Reason: Underlying canceled start at compatibilite.

Source: `/workspace/scratch/42e661864e98/source/SP53_CW_156-6_scans/J156-6-01_156-6_scan009_b.jpg`; original-source box [235, 533, 724, 641]; rotation 0°; output 3000 × 663 px.

Transform: Pillow crop; autocontrast cutoff 0; LANCZOS resize to 3000 px wide; UnsharpMask radius 1.5, percent 130, threshold 3; JPEG quality 95, subsampling 0.

Reading evidence: Canceled d-i-s readable; proposed j cannot be separated from the live p descender.

### 15_sous_ensembles

Reason: Canceled en de/en des and inserted sous-.

Source: `/workspace/scratch/42e661864e98/source/SP53_CW_156-6_scans/J156-6-01_156-6_scan009_b.jpg`; original-source box [1165, 607, 1636, 715]; rotation 0°; output 3000 × 688 px.

Transform: Pillow crop; autocontrast cutoff 0; LANCZOS resize to 3000 px wide; UnsharpMask radius 1.5, percent 130, threshold 3; JPEG quality 95, subsampling 0.

Reading evidence: Canceled en followed by d-e and a possible final s; raised sous- is clear.

### 16_ateliers

Reason: Retraced ending of ateliers and whether a deletion is visible.

Source: `/workspace/scratch/42e661864e98/source/SP53_CW_156-6_scans/J156-6-01_156-6_scan009_b.jpg`; original-source box [550, 816, 837, 930]; rotation 0°; output 3000 × 1192 px.

Transform: Pillow crop; autocontrast cutoff 0; LANCZOS resize to 3000 px wide; UnsharpMask radius 1.5, percent 130, threshold 3; JPEG quality 95, subsampling 0.

Reading evidence: Live ers with overlapping lower diagonal/loop and reinforced upper contour; simple retracing versus prior erased er not resolved.

### 17_barred_m

Reason: Barred m versus equals and alleged quotes around modere.

Source: `/workspace/scratch/42e661864e98/source/SP53_CW_156-6_scans/J156-6-01_156-6_scan009_b.jpg`; original-source box [972, 1144, 1415, 1240]; rotation 0°; output 3000 × 650 px.

Transform: Pillow crop; autocontrast cutoff 0; LANCZOS resize to 3000 px wide; UnsharpMask radius 1.5, percent 130, threshold 3; JPEG quality 95, subsampling 0.

Reading evidence: Straight upper bar with a lower trough-and-hump letter supports barred m; terminal punctuation is comma, not a quotation mark.

## Line-by-line comparisons

**Header.** The isolated handwritten 8 is included as mspage{8}; no separate archive pencil number was found.

**Opening two lines.** Read inf dans F ... le plus petit élément de F ou figure vide. Ainsi against both drafts. Figure vide has one underline. Family F alphabet is marked once; the emphasis/uline distinction alone is not counted as a substantive discrepancy.

**First implication.** Read both F/G operands, disjoints, right implication and compatibles plus its final point. First left G is settled by its basal return and short downward terminal, with coordinates but no crop.

**On a line.** Read On a, par les axiomes: including the comma and terminal colon. Coordinates [265,402,1130,491] in half a are supplied for S.

**(1.13), top correction.** Read deleted tout, raised live omb(F) et omb(G), canceled original intersection. The possible short terminal equality bar stays uncertain; no empty-set glyph is supplied after the canceled expression.

**(1.13), first prose line.** Read sont, the paired quotation strokes around disjoints, then a single short au/un group before sens. H en un is not supported as two words.

**(1.13), second prose line.** Read suivant: ils sont and the page-edge disjoint(s); retain singular/plural uncertainty without adding a grammatical s.

**(1.13), third prose line.** Read ensemblistement i.e.; the middle and final points of i.e. are individually visible in the crop.

**(1.13), equality line.** Read omb(F) cap om(G)=varnothing, et. Right om has no b; both parentheses, the intersection, equality and comma are included.

**(1.13), element line.** Read tout, the uncertain full/abbreviated élément group, de omb(F) est. Preserve the uncertainty at the actual word.

**(1.13), compatibility and last line.** Read compatible avec tout elt de om(G). The abbreviation is short and has no separate initial acute. Last om lacks b, and only the argument’s closing parenthesis is present.

**Restatement first line.** Read the short leading dash, i.e., deux figures sont disjointes ssi. The short dash has source coordinates and is represented by --.

**Restatement second line.** Read elles n’ont pas de lieu commun(s), et. No x after lieu; retain the adjective’s final-s uncertainty.

**Restatement third line.** Read tout lieu de l’une est. Two t stems and low ou settle tout against the proposed universal sign. Include canceled base disjoint, canceled interlinear com and higher inserted disjoint; H co omits the m humps.

**Restatement parenthesis and last two lines.** Read (au sens de ... atelier) de tout lieu de l’autre;. A single l survives before the uncertain state of its a-like ending and an added apostrophe; théorie is crossed out. Later tout is live, with a shared t crossbar, and lieu has no x. The closing parenthesis and final semicolon are present.

**Final paragraph first line.** Read Cela montre que les relations de, with no independent marginal note.

**Final paragraph second line.** Read canceled dis/disj and compatibilité et de disjonction sont. The proposed old j cannot be separated from the live p descender.

**Final paragraph third and fourth lines.** Read importantes aussi dans les, canceled en des/en de, inserted sous-, then ensembles M,L de F. Dans le. The inserted hyphen is retained in sous-ensembles.

**Final paragraph fifth line.** Read cas des ateliers ensemblistes, ces. Retain the uncertain overwritten/retraced state of the ateliers ending instead of asserting a prior fragment as certain.

**Final paragraph sixth line.** Read relations sont, paired quotation strokes around triviales, sur L: deux. The colon and literal quotation glyph shapes are recorded.

**Final paragraph seventh line.** Read lieux sont tjrs, canceled disjoints and raised inserted compatibles, et disjoints. H omits tjrs.

**Final paragraph eighth line.** Read ssi ils sont distincts. Par contre, même, including the point and comma.

**Final paragraph last line.** Read dans le cas ensembliste et barred m modéré, la relation. The curved lower m under its separate bar is clear; no quotes surround modéré. Preserve the unfinished sentence at the page boundary.

## Mathematical reading and actual check events

The page’s mathematical sentences were followed and summarized. No proof, independent re-proof, countermodel computation or formal certificate was attempted. The report’s check_events are only the permitted background category and explicitly say that no mathematical verification was performed. Purely visual sign decisions are recorded as visual evidence, not as proof checks.

S row SA21-K6-07 is partly confirmed only in the sense that the page really attributes (1.13) to “les axiomes” and states the displayed equivalence. The column literally says compatible; the prose uses disjoint with the atelier qualification. The proposed At 1–At 8 failure, four-element model and At 9 refinement require pages or axioms outside this packet, so their mathematical validity is neither affirmed nor denied here.

## Completeness, uncertainty and limitations

All 13 distinct C doubt loci are individually included in c_doubts: 8 resolved, 5 retained. There is 1 S row. The complete reading includes every visible text block and all identified interventions. The inventory contains 27 entries, including nested correction elements; this is not a claim of 27 independent paragraphs.

There are 17 actual evidence crops, all high-quality JPEGs at full enlarged resolution. Ten unresolved loci remain explicitly marked: family F alphabet; possible canceled equality bar; au/un; disjoint/disjoints at the right edge; élément/élém superscript t; communs/commun; the canceled/live state of the old article a; canceled dis/disj; canceled en des/en de; and the overwritten/retraced ateliers ending. The edge cannot reveal ink absent from the photograph, and enlargement cannot assign a unique typographic alphabet to handwriting.

H’s underline/emphasis representation is credited as equivalent where it records the same underline. Its literal guillemets are separately collated because the manuscript has paired raised strokes. Ordinary H strikes/additions are not treated as doubt marks; only the actual ill placeholder at the canceled words before sous-ensembles is marked_in_H=yes.

report.json, reading.tex and the crop manifest were checked for required fields, counts, file existence and transcription-macro brace balance. These are output-integrity checks, not mathematical check events. No further images were opened for validation.
