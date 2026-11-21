from pathlib import Path
from datetime import datetime, timezone
import json

dest = Path('/workspace/scratch/94548b74fbe0/out/readers/017/C')
report = json.loads((dest/'report.json').read_text())
literal_rows = {
    1: ('first line directly under on ait',['Eᵢ; est; rare','Σᵢ; dense']),
    3: ('third equality, first join',['∪','⨿']),
    4: ('left note',['Πⱼ; crossed Σ','πⱼ; underlying form uncertain']),
    7: ('under Eⱼ and after later Eⱼ',['Σ; E','∈ for the later shape']),
    8: ('Π_J above de, and binary partition name',['upper circle','0']),
    11: ('first complement after inserted Π_J',['bar on ⋃','plain ⋃']),
}
for n, (place, columns) in literal_rows.items():
    report['C_source_row_map'][n-1]['original_place'] = place
    report['C_source_row_map'][n-1]['original_reading_columns'] = columns
for event in report['processing_events']:
    if event['type'] == 'structural source validation' and not event['results']['passed']:
        event['interpretation'] = 'The first checker converted comment-only lines to empty lines and omitted standard circ from its reviewed macro set. These flags came from the checker. The checker was corrected to remove comment-only lines and include circ; reading.tex was unchanged between the two checks.'
report['notes']['scope_of_validation'] = 'The structural source check passed. The complete reading.tex and report.json contents were read together, including all local path declarations, words, punctuation, source-row parts, inventories and archive-number comment. Two oversized text outputs truncated the report; bounded text sections supplied every remaining field. No image was reopened. No compiler, renderer, OCR, external research, package installation or delegated reading was used.'
report['final_validation']['complete_tex_report_joint_read'] = True
report['final_validation']['read_method'] = 'Complete TeX was delivered in the first combined source read. Report head and tail were delivered in the long reads; the remaining D28-D37/source-row map and doubts/inventory/notes were delivered in bounded sections and read completely. Final metadata and literal source-row spelling updates are displayed by finalize_report.py.'
report['end_utc'] = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
report['processing_events'].append(dict(type='final source-review metadata update',script='finalize_report.py',operations='Preserve literal original C table spellings in the row map; annotate the first checker flags; record completed joint source review and current UTC clock time.',scope='Metadata update and JSON serialization only; no manuscript reading, image processing or mathematical check is rerun.'))
(dest/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
audit = dest/'reading.md'
text = audit.read_text()
text += '\n## Completed source review\n\nEnd recorded at **'+report['end_utc']+'**. The structural check passed and the complete TeX/report contents were read together. Two oversized text outputs truncated portions of the report; bounded text sections then delivered every remaining field. The first checker flags came from its treatment of comment-only lines and its omitted standard `\\circ` entry; both checker issues were corrected, with no TeX change between those checks. The report preserves both actual check results and their scope.\n'
audit.write_text(text)
print(json.dumps({'end_utc':report['end_utc'],'literal_source_row_map':report['C_source_row_map'],'scope_of_validation':report['notes']['scope_of_validation'],'first_checker_interpretation':[e['interpretation'] for e in report['processing_events'] if 'interpretation' in e],'final_validation':report['final_validation'],'last_processing_event':report['processing_events'][-1]},ensure_ascii=False,indent=2))
