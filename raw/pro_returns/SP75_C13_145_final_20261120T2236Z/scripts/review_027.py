from pathlib import Path
import json
E=Path(__file__).resolve().parents[1]
r=json.loads((E/'reader_reports/145_scan027.json').read_text())
r['reader']='/root/reader_b';r['main_reader_reviewed']=True;r['crop_count']=14
r['root_review']={'whole_image':True,'crops_viewed':'All fourteen saved crops inspected directly. Root confirmed the three capital Pi signs and clear -bar j, the brace-shaped final delimiter, bracket-shaped S index, inserted éventuelles and à P, actual 1/2/3 stabilizer indices, undotted rho, insertion attachment after6, Pi-conjugués local doubt, punctuation/abbreviations, lower-case on after cet élément, one retraced les, the singular corrections and both source page numbers. All doubtful struck words remain doubtful unless each letter is plain. Full comparison/report and inventory reviewed before finalization; no source symbol was repaired from the finite-action calculations.'}
for c in r['changes']:
    if c['id']=='s027-11':
        for k in ['C','H','final']:c[k]=c[k].replace("\\'", "'")
    if c['id'] in ['s027-02','s027-04']:c['marked_in_H']='no'
for x in r['inventory']:
    x['first_words_or_objects']=x['first_words_or_objects'].replace("\\'", "'")
a=json.loads((E/'scripts/root_additions_026_027.json').read_text())['27']
r['notes'].extend(a['notes']);r.setdefault('check_events',[]).extend(a['check_events'])
(E/'reader_reports/145_scan027_reviewed.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
(E/'pages/145_scan027.tex').write_text((E/'reader_reports/145_scan027.tex').read_text())
