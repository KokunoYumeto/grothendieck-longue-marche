#!/usr/bin/env python3
"""Render the independent source audit, using only workspace-relative references."""
from pathlib import Path
import collections
import csv
import json

ROOT = Path(__file__).resolve().parents[2]
WORK = ROOT/'work'
J = json.loads((WORK/'data/source_integrity.json').read_text())
R = WORK/'records'


def main():
    raw = J['raw_manifest_checks']
    pk = J['packages']
    us = J['units']
    scans = J['per_scan_marks']
    f = J['independent_formula_totals']
    h = J['historical_formula_totals']
    classes = collections.Counter(d['classification'] for d in J['independent_formula_differences'])
    assert not J['integrity_failures']
    assert classes['UNCLASSIFIED'] == 0
    assert all(e['french_fragment_occurrences_on_scan'] and e['english_fragment_occurrences_on_scan'] for e in J['nine_historical_formula_contextual_audits'])
    L = [
        '# Independent source integrity audit', '',
        'Audit date: 13 November 2026. Scope: the attached French, English and typesetting source bundles; all 116 package pairs and all 245 translation units. No source file was modified.', '',
        '## Finding', '',
        '**No source package, unit or scan is omitted, duplicated or reordered.** All 1,022 files match the byte lengths and SHA-256 digests in the three attached archive manifests. Every French unit is the exact recorded character slice, and every English package is reproduced byte for byte by the documented unit assembly algorithm. All 1,588 scans occur once, in manuscript order, in both languages.', '',
        '**The English mathematical content is not literally byte-identical to the French source.** The supplied checks explicitly mask translated prose, exclude the written-out m-bar shorthand and accept recorded exceptions. The nine residual changed/missing-formula cases are accounted for below. Independent comparison found no additional unexplained mathematical difference; this is a structural integrity finding, not a new scholarly certification of every translated assertion.', '',
        'Two metadata qualifications matter: 44 French packages use CRLF while their exported units use LF, and the source record for the formula in `LM_P018_s171-180` incorrectly says scan 172; its actual location is scan 179. Neither qualification changes or drops manuscript content.', '',
        '## Evidence and reproducibility', '',
        'Primary supplied records: `LM_FR_MANIFEST.tsv`, `LM_EN_MANIFEST.tsv`, `LM_TYPESET_MANIFEST.tsv`; `en/MANIFEST.json`; `fr/records/CURRENT_TEXT_INDEX.tsv`; `en/checks/CHECKS.json`, `FIXES.jsonl` and `WAIVERS.jsonl`; and the visible algorithms in `en/scripts/prepare.py`, `assemble.py` and `check_units.py`. Original manuscript package text is in `fr/texts/` and `en/packages/`; translation inputs and outputs are in `en/french_units/` and `en/units/`.', '',
        'Run `python work/scripts/source_integrity.py`, then `python work/scripts/write_source_integrity_report.py`. The first script reads source files and writes `work/data/source_integrity.json`; the second creates this report and two tabular inventories. Neither invokes the network or imports the original machine-specific configuration. All emitted paths are relative source references.', '',
        'The original `check_units.py` cannot be executed unchanged from this attachment: its `scripts/der/check_units.py`, comparison `cmp/` library and external glossary `common.py` are absent. Its `common_lm.py` also points to the originating machine. The visible assembly, annotation-count, m-bar and raised-ending algorithms were reproduced directly; the new formula segmenter and text-box comparison are independent. Historical results are identified separately throughout this report.', '',
        '## 1. Raw bytes, slice identity and complete assembly', '',
        '| Check | Result |', '|---|---|',
        f'| Attached raw manifest rows | {len(raw):,} verified; zero byte/hash discrepancies |',
        f'| French source packages | {len(pk)} / {len(pk)} match their `en/MANIFEST.json` raw hashes |',
        f'| French unit slices | {len(us)} / {len(us)} match recorded offsets, normalized UTF-8 hashes and character lengths |',
        '| English package assembly | 116 / 116 match both normalized text and raw bytes |',
        f'| French raw unit concatenation | {sum(p["french_unit_raw_concatenation_identical"] for p in pk)} / 116 raw-byte-identical; 44 differ only by CRLF versus LF |',
        '| French normalized concatenation | 116 / 116 exact after the original text reader’s newline normalization |',
        '| Manifest unit inventory | 245 present; no extra unit files, missing units or repeated unit uses |',
        '| Package order | Exactly the order of the supplied current-text index |',
        '| Unit order | Exactly each package’s recorded order and the manifest’s global unit order |',
        '| Historical CHECKS inventory | Exactly the same 245 unit IDs; all recorded PASS |', '',
        'The current-text index raw SHA-256 is `' + J['global_checks']['index_hash_actual'] + '`, exactly the digest recorded by the translation manifest. Raw source hashes remain authoritative: line-ending normalization is used only to reproduce the explicitly text-based slice and assembly algorithms.', '',
        'For each French unit, the audit verifies `package[start:end] == unit`, contiguous cut offsets, first offset zero, final offset equal to package length, the recorded unit digest, and every scan and manuscript-page anchor. English assembly uses the original algorithm exactly: `lead + english_unit.strip("\\n") + trail`, followed by concatenation in the package’s recorded unit order. This is stronger than checking only that all unit filenames exist.', '',
        'The full assembly order, scan ranges, offsets and both unit hashes are in `SOURCE_UNIT_ASSEMBLY.tsv`; the JSON contains all individual checks and every manifest hash.', '',
        '### Scan coverage', '', '| Cote | Scans | Continuity | Missing / repeated |', '|---|---:|---|---:|',
    ]
    for cote, r in J['scan_coverage'].items():
        L.append(f'| {cote} | {r["scan_count"]} | 1–{r["last"]}, in order | 0 / 0 |')
    L += ['',
        'All 245 units have matching French/English scan and manuscript-page anchor sequences, matching comment sequences, matching tag arguments, identical illegible-word-count arguments, and matching environment-name counts. Balanced braces, matched environment counts and closed outer math segments were independently checked in both languages. The simple per-scan blank-line split yields 8,842 nonempty blocks on each side, with no scan-level block-count mismatch; this differs from the historical checker’s 7,623 prose paragraphs because its missing comparison library applies a different prose filter.', '',
        '## 2. Annotation preservation by scan', '',
        'The seven primary apparatus macros were counted directly on every scan, with comments excluded and no macro expansion. Every primary macro count agrees between French and English. The bars inside balanced `\\unsure{...}` arguments differ only in the three already recorded cases where the translation keeps two possible completions of a damaged French negation.', '',
        '| Primary macro | French | English |', '|---|---:|---:|',
    ]
    for name in ('deleted', 'inserted', 'unsure', 'illegible', 'margin', 'uline', 'uuline'):
        L.append(f'| `\\{name}` | {sum(s["french_marks"][name] for s in scans):,} | {sum(s["english_marks"][name] for s in scans):,} |')
    L += ['',
        '| Cote / scan | Source count → English count | Approved reason |', '|---|---|---|',
        '| 140-3 / 148 | unsure bars 3 → 4 | `does not occur` / `only occurs`: damaged second half of the negation |',
        '| 140-2 / 396 | unsure bars 7 → 8 | `cannot` / `can only`: damaged second half of the negation |',
        '| 140-3 / 210 | unsure bars 4 → 5 | `does not cover` / `covers only`: damaged second half of the negation |', '',
        'The total is 6,850 French uncertainty bars and 6,853 English bars. These are explicit source-record waivers, not additions made during this edition. Both alternatives and all illegible spans are retained. The audit does not select a reading.', '',
        'Among the secondary presentation macros, only five `\\textsuperscript` occurrences disappear: two at 140-3:629, two at 140-4:267 and one at 140-4:268. They are raised endings of French abbreviations that are written out in English; the supplied checks list exactly these review points. Counts of `\\diagram`, `\\figure`, `\\texttt`, `\\textit`, `\\textbf`, `\\textcircled` and `\\fbox` agree on every scan.', '',
        '`SOURCE_SCAN_MARKS.tsv` contains all 1,588 paired per-scan counts, source lines and differences. Counts establish preservation of marker incidence; they do not by themselves prove semantic equality of everything inside a marker. The formula and glossary audits provide the additional checks described here and in `GLOSSARY_INCONSISTENCIES.md`.', '',
        '## 3. Formula comparison: what “identical” means', '',
        '### Supplied historical results', '',
        '| Historical field | Count | Interpretation |', '|---|---:|---|',
        f'| French formulas | {h["french"]:,} | After the standalone m-bar exclusion |',
        f'| English formulas | {h["english"]:,} | Same historical comparison |',
        f'| Identical | {h["identical"]:,} | After the checker’s prose-box masking; not literal source bytes |',
        f'| Text-only differences | {h["text_only"]} | Additional wording/marked-word cases retained for review |',
        f'| Changed | {h["changed"]} | The six explicitly waived display/formula cases below |',
        f'| Missing | {h["missing"]} | Three formulas changed into prose or an ordinary equals sign |',
        f'| Raised abbreviation endings | {h["raised_endings"]} | Written out with their French abbreviations |',
        '| Added / moved / spacing-only | 0 / 0 / 0 | Historical fields |', '',
        'The 476 standalone m-bar forms excluded from comparison are the author’s shorthand for “même”, rendered according to the supplied notation policy. No matching shorthand formula remains in English. These exclusions are not evidence that 476 mathematical variables were dropped. Conversely, saying “every formula is byte-identical” would conceal the documented translation convention and the nine cases below.', '',
        '### Independent comparison', '',
        f'The new parser finds {f["french"]:,} French and {f["english"]:,} English outer mathematical/drawing segments after the same 476 exclusions. It pairs {f["structurally_identical"]:,} by exact structure after masking translated text boxes and pure-word apparatus arguments. Of these, {f["raw_identical"]:,} are literally identical after comments are blanked; the other {len(J["independent_formula_text_or_space_pairs"]):,} matching pairs have wording or whitespace differences, retained in the JSON.', '',
        'The parser deliberately treats an entire TikZ picture as one outer segment and preserves nested mathematics in its prose labels. Its total is seven lower than the historical checker’s on each side. That difference in segmentation is reported, not rounded away or presented as a rerun of the missing library.', '',
        'There are 23 nonmatching groups, all classified: the nine recorded exceptions; nine raised abbreviation endings grouped at seven sites; and seven additional groups whose differences are confined to TikZ node or parbox prose. For those seven groups, the geometry and code outside prose regions match, embedded mathematics matches, and primary apparatus counts inside changed regions match. They occur at 140-1:19 and 32; 140-2:237 and 419; 140-3:600; and 140-4:34 and 35. All changed prose regions and their checks are retained in the JSON.', '',
        'For each of the six historical changed-formula cases, applying only the recorded exact French→English fragment transformation reproduces the English structural target; the remaining equation and diagram tokens then match after prose masking. For each missing-formula case, the supposedly missing segment is exactly the segment deliberately converted by the recorded wording convention. No additional algebraic correction is introduced or authorized by this audit.', '',
        '## 4. The nine residual historical formula differences', '',
        'All nine retain the supplied English wording. The audit supplies the actual cote, scan and source line, and distinguishes mathematical TeX encoding from mathematical content. Each has a corresponding `WAIVERS.jsonl` entry by Claude (Opus 5.5), dated 12 November 2026. The complete original waiver records are preserved in the machine results.', '',
    ]
    for e in J['nine_historical_formula_contextual_audits']:
        L += [f'### {e["id"]}: {e["cote"]}, scan {e["scan"]}', '',
              f'**Classification:** {e["class"]}.', '',
              f'French: `{e["french_source"]}`, line {e["french_line"]}; English: `{e["english_source"]}`, line {e["english_line"]}.', '',
              'French source fragment:', '', '```tex', e['french_fragment'], '```', '',
              'Supplied English fragment:', '', '```tex', e['english_fragment'], '```', '',
              e['assessment'], '', '**Disposition:** '+e['disposition'], '']
    L += [
        '## 5. Approved fixes and waivers', '',
        'The attachment contains 41 historical fixes, all literal replacements with required count one. Every final English unit contains its recorded replacement; none still contains its recorded old literal. All these changes are therefore present in the English package reconstruction. The raw model outputs preceding those fixes are not supplied, so this audit cannot replay and independently certify the original execution-time occurrence count. The result is an applied-text witness check, not an invented reconstruction of unavailable raw outputs.', '',
        'All 34 historical waivers are included verbatim in the JSON, associated with their unit and relevant scan. They cover formula wording and shorthand, expanded abbreviation endings, the three negation alternatives, and glossary matching failures caused by preserved markup or context. A PASS in the historical CHECKS file means these recorded waivers have been applied; it does not erase the underlying review entries.', '',
        'One location error is independently demonstrated: historical fix 30 and its formula waiver describe scan 172, but their exact old/new formula occurs at scan 179 in `LM_P018`. Both original records are preserved; this report and its machine contextual audit use the verified scan 179. No source wording is altered to repair metadata.', '',
        'The present edition has one separately proposed, unmarked glossary correction: `EN-GLOSS-140-2-296-001`, `structure with loops` → `loop structure` at `LM_P030`, 140-2:296, English package line 96. It is recorded in `glossary_edits.json` and is not applied to the attached source files. Mathematical notation and all apparatus are untouched. Layout and mechanical changes made in generated edition bodies are governed by the separate build/change records; this audit is of their original source baseline.', '',
        '## 6. Public source-of-record provenance and its limits', '',
        'The attached `en/README.md`, in its “Input (source of record)” section, reports a comparison with the public repository at abbreviated commit `671d2cf`: 22 texts identical in `raw/second_pass/`, 18 equal apart from line endings, 50 identical elsewhere in the tree, and 26 not found as identical blobs. These are historical statements in the supplied README, not conclusions newly verified here.', '',
        'The attached `source_of_record.py` performs `git fetch` and reads a checkout on the originating machine. Its generated `SOURCE_OF_RECORD.json` is not included in any attached bundle, and the referenced checkout is not available. Consequently the independently established provenance is the complete raw-file manifest and exact current-text-index/translation-manifest chain. This report does not substitute an unverified contemporary repository snapshot for the user-supplied source of record.', '',
        '## 7. Deliverables and limitations', '',
        '- `source_integrity.json`: every raw hash, package reconstruction, unit order and cut, per-scan annotation count, independent formula pair/difference, historical waiver and contextual exception.',
        '- `SOURCE_UNIT_ASSEMBLY.tsv`: 245 rows in assembly order with offsets and hashes.',
        '- `SOURCE_SCAN_MARKS.tsv`: 1,588 per-scan rows with paired counts and differences.',
        '- `source_integrity_differences.json`: the 23 independently reviewed nonmatching groups, as a compact companion to the full data.', '',
        'This audit does not claim that a source count proves a printed PDF is complete. Actual PDF links, shipped uncertainty spans, all-page ink bounds, log diagnostics and visual review are checked separately by `verify_pdf.py` and the edition’s verification records. It also does not claim a new reading of the manuscript scans or an independent proof of Grothendieck’s mathematical arguments. Uncertain readings and the source’s mathematical assertions remain preserved.', '',
    ]
    (R/'SOURCE_INTEGRITY.md').write_text('\n'.join(L))
    unit_fields = ['global_order','package_order','unit_order_within_package','cote','package','unit','scans','start','end',
                   'recorded_unit_sha256','actual_normalized_sha256','french_raw_sha256','english_raw_sha256',
                   'offsets_contiguous','source_slice_exact','unit_sha_exact','scans_exact','anchors_exact','comments_sequence_exact','tags_exact','illegible_arguments_exact']
    with (R/'SOURCE_UNIT_ASSEMBLY.tsv').open('w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=unit_fields, delimiter='\t'); w.writeheader()
        for u in us:
            row = {k: u[k] for k in unit_fields}; row['scans'] = ','.join(row['scans']); w.writerow(row)
    marks = list(scans[0]['french_marks'])
    scan_fields = ['cote','scan','package','unit','french_line','english_line'] + [language+'_'+mark for mark in marks for language in ('fr','en')] + ['differences']
    with (R/'SOURCE_SCAN_MARKS.tsv').open('w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=scan_fields, delimiter='\t'); w.writeheader()
        for s in scans:
            row = {k: s[k] for k in scan_fields[:6]}
            for mark in marks:
                row['fr_'+mark], row['en_'+mark] = s['french_marks'][mark], s['english_marks'][mark]
            row['differences'] = json.dumps(s['differences'], ensure_ascii=False)
            w.writerow(row)
    print(json.dumps({'report': 'work/records/SOURCE_INTEGRITY.md', 'unit_rows': len(us), 'scan_rows': len(scans), 'unclassified_formula_groups': 0}))


if __name__ == '__main__':
    main()
