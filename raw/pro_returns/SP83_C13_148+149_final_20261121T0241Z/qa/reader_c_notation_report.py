"""Create reader_c's read-only notation QA report from recorded observations."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT.parent

def p(path):
    return str((ROOT / path).resolve())

def evidence(*names):
    return [p('crops/' + name) for name in names]

viewed = evidence(
    '148_scan067_second_B05.png', '148_scan067_second_B11.png',
    '148_scan053_lower_diagram.png', '148_scan056_second_B11.png',
    '148_scan064_second_B18.png', '148_scan064_second_B08.png',
    '148_scan056_old_para3.png', '148_scan061_item2_title.png',
    '148_scan061_item2_body.png', '148_scan061_second_B09.png',
    '148_scan061_second_B03.png', '148_scan067_second_B06_upper.png',
    '148_scan067_second_B09.png',
)

findings = [
    {
        'id': 'NQ01',
        'kind': 'confirmed consistency with local uncertainty',
        'priority': 'retain current source readings',
        'pages': ['148_scan053', '148_scan067'],
        'title': 'Gamma on 067 is consistent; 053 remains a local sigma/gamma doubt',
        'current_readings': [r'\gamma_s,\gamma_t;\ \gamma=4', r'\mathbb Z/\unsure{\gamma|\gamma_t}', r'\unsure{\sigma|\gamma}'],
        'observation': 'The clear gamma=4 has a low closed loop and a raised right arm. The edge labels and dark algebra show the same family with variable arm height; some gamma-prime forms have a nearly flat upper return. The 053 side-note symbol has a low oval and long flat upper return. That local shape does not exclude gamma when compared with 067; it also remains sigma-like. The overwritten mark beside the 067 quotient divisor is a separate unresolved feature.',
        'recommendation': 'Keep gamma consistently on 067 and retain the quotient/index doubt. Do not globally replace the 053 sigma/gamma alternatives. Qualify the consolidated gamma row so its inclusion of 053 explicitly refers to an unresolved sigma/gamma occurrence, rather than seeming to certify gamma there.',
        'confidence': 'high for the consistency assessment on 067; medium for the 053 local assessment',
        'source_files': [p('pages/148_scan053.tex'), p('pages/148_scan067.tex'), p('notation_final.md')],
        'evidence_crops': evidence('148_scan067_second_B05.png', '148_scan067_second_B06_upper.png', '148_scan067_second_B09.png', '148_scan067_second_B11.png', '148_scan053_lower_diagram.png'),
        'new_material_correction_proposed': False,
    },
    {
        'id': 'NQ02',
        'kind': 'stale notation summary',
        'priority': 'metadata update',
        'pages': ['148_scan056', '148_scan064'],
        'title': 'The Sigma summary omits the 064 bar alternative and the 056 live accent doubt',
        'current_readings': [r'\widetilde\Sigma\setminus R', r'\pi_0(\unsure{\widetilde\Sigma|\Sigma})', r'(X,[\unsure{\widetilde{\Sigma}|\Sigma}],R)', r'\unsure{\widetilde{\Sigma}|\overline{\Sigma}|\Sigma}'],
        'observation': 'The cancelled 056 opening has a visibly separated wavy accent. The live 056 pi-zero formula has an extra curved upper run close to the main top bar, supporting the existing tilde/plain doubt. In 064 the tuple has crowded bracket and accent strokes; its local doubt remains appropriate. The marginal opening has a flatter detached upper run, consistent with retaining the bar as an explicit alternative. Accepted 064 TeX and final record doubts already include that bar alternative, but the 064 notation row and generated working/hand rows still list only tilde/plain and describe both locations together. The consolidated decoration row omits 056 and does not mention the 064 bar alternative.',
        'recommendation': 'Refresh the 064 notation/hand row to distinguish the tuple from the marginal sign. Add the bar alternative for the margin and mention the 056 live tilde/plain doubt in the consolidated decoration summary. Preserve the accepted TeX and final local doubts.',
        'confidence': 'high for the metadata mismatch; local source doubts remain unresolved',
        'source_files': [p('pages/148_scan056.tex'), p('records/148_scan056.json'), p('pages/148_scan064.tex'), p('records/148_scan064.json'), p('notation_working.md'), p('SP83_C13_148+149_hand_log.md'), p('notation_final.md')],
        'evidence_crops': evidence('148_scan056_old_para3.png', '148_scan056_second_B11.png', '148_scan064_second_B08.png', '148_scan064_second_B18.png'),
        'new_material_correction_proposed': False,
    },
    {
        'id': 'NQ03',
        'kind': 'confirmed occurrence-specific forms',
        'priority': 'preserve; optional consolidated-table clarification',
        'pages': ['148_scan061'],
        'title': '061 dotted divisibility, primes, lower indices and item number are separate readings',
        'current_readings': [r'd_a\mathrel{:\!|}r_a', r"r'_a\mid r_a", r'\raisebox{-.4ex}{\unsure{2|?}}', r'\mathbb Z_a/r_a\mathbb Z', r"\mathbb Z_a/r'_a\mathbb Z_a", r'\mathbb Z/\unsure{d|d_a}r_a\mathbb Z', r'\unsure{4^\circ|1^\circ}'],
        'observation': 'The raised item-2 heading has two small dots to the left of an upright; the lower main divisor relation has no corresponding pair of dots. The r-primes are detached upper-right strokes, while the a indices are separate low loops. The small 2-like mark after the divisor condition sits below the relation baseline and is not a secure exponent. In item 3 the target first and last Z have no separate a; the multiplier has a long lower exit without a securely separable a, hence d/d_a. The first main item digit is heavily retraced and may look like 4 despite its sequential place; the current 4-degree/1-degree doubt is appropriate. These forms all have final doubt mappings where needed.',
        'recommendation': 'Keep the local dotted and undotted relation forms and literal uneven indices. Do not infer extra a indices or resolve the item digit by sequence. The working notation and hand logs already describe the dotted divisor; adding it to notation_final would make that local exception easier to find, but no accepted-source correction is proposed.',
        'confidence': 'high for dots, prime placement and unindexed target Z forms; retained uncertainty for d/d_a, isolated 2-like mark and first item digit',
        'source_files': [p('pages/148_scan061.tex'), p('records/148_scan061.json'), p('notation_working.md'), p('SP83_C13_148+149_hand_log.md'), p('notation_final.md')],
        'evidence_crops': evidence('148_scan061_item2_title.png', '148_scan061_item2_body.png', '148_scan061_second_B09.png', '148_scan061_second_B03.png'),
        'new_material_correction_proposed': False,
    },
    {
        'id': 'NQ04',
        'kind': 'missing individual final doubt mapping in a changing page',
        'priority': 'metadata follow-up after 067 adjudication',
        'pages': ['148_scan067'],
        'title': 'The small-triangle b_3 doubt needs its own final record entry',
        'current_readings': [r'\unsure{b_3}'],
        'observation': 'The current accepted page contains a standalone unsure b_3 on the small triangle right side. No individual final doubts entry addresses that same local label. The existing b_3^1 entry belongs to an inter-hole label and does not cover this different ink. Whole drawing uncertainty entries concern connectivity rather than this letter/index reading.',
        'recommendation': 'When 067 adjudication is finalized, add an individual final doubt entry for the small-triangle b_3, or record an explicit resolution if root independently settles it. Do not treat the separate b_3^1 mapping as coverage for this label.',
        'confidence': 'high as a metadata snapshot; no new glyph adjudication',
        'source_files': [p('pages/148_scan067.tex'), p('records/148_scan067.json')],
        'evidence_crops': evidence('148_scan067_second_B12.png'),
        'crops_reopened_in_this_qa': False,
        'snapshot_warning': '067 was actively undergoing root adjudication while this review ran; this item may be addressed before report delivery.',
        'new_material_correction_proposed': False,
    },
    {
        'id': 'NQ05',
        'kind': 'stale alternatives field in a changing page',
        'priority': 'metadata follow-up after 067 adjudication',
        'pages': ['148_scan067'],
        'title': 'Loop interval alternatives still name gamma after the final reading changed to alpha',
        'current_readings': [r'\unsure{[0,\alpha][1,\beta)|[1,\alpha][1,\beta)}'],
        'observation': 'The final page and the loop-interval doubt reading both use alpha in the second alternative. The accompanying alternatives field still says [1,gamma][1,beta), inherited from the earlier reading. This is an internal metadata mismatch, not a new claim about the ink.',
        'recommendation': 'Align the alternatives description with the final alpha reading after 067 adjudication. Preserve the frozen independent second TSV.',
        'confidence': 'high as a metadata snapshot',
        'source_files': [p('pages/148_scan067.tex'), p('records/148_scan067.json')],
        'evidence_crops': evidence('148_scan067_second_B08.png'),
        'crops_reopened_in_this_qa': False,
        'snapshot_warning': '067 was actively undergoing root adjudication while this review ran; this item may be addressed before report delivery.',
        'new_material_correction_proposed': False,
    },
    {
        'id': 'NQ06',
        'kind': 'older notation certainty superseded by explicit final doubts',
        'priority': 'metadata update after 067 adjudication',
        'pages': ['148_scan067'],
        'title': 'The c_i^0/c_i^1 summaries should reflect the retained c/a/b alternatives',
        'current_readings': [r'\unsure{c_i^0|a_i^0}', r'\unsure{c_i^1|b_i^1}'],
        'observation': 'The current page and final doubts retain eight c/a or c/b alternatives at the inter-hole labels. An appended notation row acknowledges the mixed outer/inner strokes and low-confidence c primary, but the earlier record/working/hand row still describes all eight as clearly open c forms, and notation_final still says the eight labels use the visible c forms without the alternatives. The literal pi(j) note is separate and remains correctly qualified.',
        'recommendation': 'Qualify or explicitly supersede the older c_i row and refresh the consolidated row to say c primary with a/b alternatives. This is a summary-consistency update; no further source decision is proposed.',
        'confidence': 'high as a metadata comparison',
        'source_files': [p('pages/148_scan067.tex'), p('records/148_scan067.json'), p('notation_working.md'), p('SP83_C13_148+149_hand_log.md'), p('notation_final.md')],
        'evidence_crops': evidence('148_scan067_second_B04.png'),
        'crops_reopened_in_this_qa': False,
        'snapshot_warning': '067 was actively undergoing root adjudication while this review ran; this item may be addressed before report delivery.',
        'new_material_correction_proposed': False,
    },
]

inventory = json.loads((ROOT/'qa/reader_c_notation_inventory.json').read_text())
records = sorted((ROOT/'records').glob('*_scan*.json'))
now = datetime.now(timezone.utc).isoformat()
report = {
    'reviewer': 'reader_c',
    'review_type': 'read-only cross-page notation QA; advisory findings only',
    'generated_at_utc': now,
    'scope': {
        'accepted_page_count': len(inventory['pages']),
        'unsure_occurrences_at_inventory_snapshot': sum(x['unsure_occurrences'] for x in inventory['pages']),
        'unique_page_local_unsure_at_inventory_snapshot': sum(len(x['unique_unsure']) for x in inventory['pages']),
        'final_doubt_entries_at_coverage_check': 266,
        'record_to_compiled_doubt_table_missing_readings': 0,
        'method': 'All accepted pages scanned for recurring notation controls and balanced unsure units; all page-record notation and final doubt fields compared; ambiguous coverage candidates reviewed in context. Targeted visual review of 13 existing crops on five pages. This is not a fresh full-page transcription pass.',
        'files_modified': ['result/qa/reader_c_notation_inventory.py', 'result/qa/reader_c_notation_inventory.json', 'result/qa/reader_c_notation_report.py', 'result/qa/reader_c_notation_findings.md', 'result/qa/reader_c_notation_findings.json'],
        'accepted_pages_records_and_tsvs_modified_by_reviewer': False,
        'new_crops_created': False,
        'ocr_research_or_tex_compilation_used': False,
    },
    'findings': findings,
    'coverage_notes': [
        '049, 051, 063 and 065 exact-string candidates are semantically covered by separate leading-reading and alternatives fields; they are not missing doubts.',
        'Whole-unit unsure wrappers on 067 are described by cancellation-state or drawing-connectivity entries; internal individual labels still require their own coverage where applicable.',
        'After normalizing HTML line breaks and escaped table pipes, all 266 current final record readings occur in the compiled doubts table.',
        'Other recurring forms inspected in text/records include phi-shaped empty set, l/ell, p/rho map names, category letter order, plus/minus, vector/underline distinctions, primes, local abbreviations, equality shorthand and handwritten numbers. No additional unsupported global replacement is recommended.',
    ],
    'existing_crops_viewed': viewed,
    'input_page_hashes_at_inventory_snapshot': {x['page']: x['sha256'] for x in inventory['pages']},
    'record_hashes_at_report_generation': {f.stem: hashlib.sha256(f.read_bytes()).hexdigest() for f in records},
    'root_adjudication_required': True,
}

qa = ROOT/'qa'
(qa/'reader_c_notation_findings.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')

lines = [
    '# Reader C: cross-page notation findings',
    '',
    f'Read-only advisory review, generated {now}.',
    '',
    'The requested comparisons do not justify a global change of the accepted source readings. Gamma on 067 is internally consistent; 053 remains a local sigma/gamma doubt. The decorated Sigma and 061 divisor/index forms require occurrence-specific treatment. The actionable findings chiefly concern stale notation summaries and two 067 metadata fields during its active adjudication.',
    '',
    '## Scope and verification',
    '',
    'All 23 accepted TeX pages were scanned for recurring notation controls and balanced `\\unsure` units, and their record notation/final-doubt fields were compared. The inventory snapshot contained 296 uncertainty occurrences, representing 275 unique page-local forms. All 266 current final record doubt readings were found in the compiled doubts table after normalizing HTML line breaks and escaped table pipes. Thirteen existing crops on five pages were directly viewed for the requested visual comparisons. This was a notation review, not a fresh full-page transcription pass.',
    '',
    'Accepted pages, records and TSVs were not edited. No new crops, OCR, outside research or TeX compilation were used. The 067 findings are snapshot observations: root was actively adjudicating that page during this review.',
    '',
    '| ID | Finding | Suggested root action |',
    '|---|---|---|',
    '| NQ01 | 067 gamma is consistent; 053 sigma/gamma remains local | Keep source readings; qualify the final gamma summary for 053. |',
    '| NQ02 | 064 bar alternative and 056 live accent doubt are missing from the consolidated decoration summary | Refresh notation/hand summaries, retaining the local accepted alternatives. |',
    '| NQ03 | 061 dotted divisor, primes, indices and item digit are occurrence-specific | Preserve current readings; optionally add the dotted relation to the consolidated table. |',
    '| NQ04 | 067 small-triangle `b_3` lacks an individual final doubt mapping | Add or explicitly resolve that local mapping after adjudication. |',
    '| NQ05 | 067 loop alternatives still say gamma after the final reading changed to alpha | Align the alternatives field with the final reading. |',
    '| NQ06 | Older 067 c-label summaries overstate certainty relative to retained c/a/b doubts | Qualify or supersede the old rows and refresh the final table. |',
    '',
]
for item in findings:
    lines += [f"## {item['id']}: {item['title']}", '', item['observation'], '', '**Suggested root action.** '+item['recommendation'], '', '**Confidence.** '+item['confidence']+'.', '']
    lines += ['**Current forms:** '+ '; '.join('`'+x+'`' for x in item['current_readings'])+'.', '', '**Existing evidence crops:**', '']
    for crop in item['evidence_crops']:
        suffix = '' if crop in viewed else ' — existing audit evidence; not reopened for this metadata-only finding'
        lines.append(f'- [{Path(crop).name}](sandbox:{crop}){suffix}')
    lines += ['', '**Files to consult:**', '']
    for file in item['source_files']:
        lines.append(f'- [{str(Path(file).relative_to(ROOT))}](sandbox:{file})')
    lines.append('')

lines += [
    '## Coverage results and limits',
    '',
    'The apparent exact-string coverage failures on 049, 051, 063 and 065 are accounted for by record fields that store a plain leading reading and its alternatives separately. These are semantic mappings, not missing entries. Whole-unit uncertainty wrappers on 067 are covered by its cancellation-state and drawing-connectivity entries; they do not automatically cover an independently doubtful local label such as the small-triangle b_3.',
    '',
    'Other recurring forms inspected in the accepted text and records include the phi-shaped empty set, l/ell, p/rho map names, category letter order, plus/minus, vector/underline distinctions, primes, literal abbreviations, equality shorthand and handwritten numbers. No additional cross-page substitution is recommended. The source’s local differences remain evidence, and a recurring mathematical role alone does not resolve a damaged glyph.',
    '',
    'The JSON report records the exact crops directly viewed and the input page hashes at the inventory snapshot. The retained inventory and generator are work documentation. Root remains responsible for any material correction and for synchronizing final summaries after the changing 067 adjudication.',
    '',
]
(qa/'reader_c_notation_findings.md').write_text('\n'.join(lines))
print(json.dumps({'markdown':str(qa/'reader_c_notation_findings.md'),'json':str(qa/'reader_c_notation_findings.json'),'findings':len(findings),'crops_directly_viewed':len(viewed)},indent=2))
