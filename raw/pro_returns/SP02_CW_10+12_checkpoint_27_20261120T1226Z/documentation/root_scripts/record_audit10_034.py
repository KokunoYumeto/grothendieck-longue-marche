from pathlib import Path
import json,sys,copy
sys.path.insert(0,str(Path('SP02_CW_10+12/scripts').resolve()))
from record_audit import stable_changes,build_revision
key='B10-01_10_scan034';out=Path('SP02_CW_10+12')
s=json.loads((out/f'documentation/audit_sessions/{key}_audit001.json').read_text())
r=json.loads((out/f'documentation/page_records/{key}.json').read_text());c=stable_changes(r,key)
p=dict(audit_id=s['audit_id'],baseline_page_sha256=s['baseline_page_sha256'],audit_reading_complete=True,audit_inventory_confirmed=True)
p['edits']=[dict(old=r"ainsi \deleted{\unsure{pour}}",new=r"ainsi \deleted{\unsure{par|pour}}"),dict(old=r'\operatorname{Hom}_{\mathbb{S}_i\text{-gr.}}',new=r'\operatorname{Hom}_{\unsure{S|\mathbb{S}}_i\text{-gr.}}')]
p['upsert_changes']=[]
for n,final,shows,crop in [
 (1,r'\deleted{\unsure{par|pour}}','The enlarged word has the descending p followed by approximately two typewriter positions, a rounded middle body and an r-like final shoulder. This favors par; crossing strokes obscure the middle, so pour remains an alternative. The first-pass pour-only doubt is broadened.','audit-pour-first;audit-upper'),
 (10,r'\unsure{S|\mathbb{S}}_i','Two vertically displaced S-shaped impressions are visible, with overlapping bowls; the next Hom has one S. The ink establishes a doubled impression but does not securely establish a distinct mathematical alphabet. Plain S is retained as the first alternative, with the doubled form marked uncertain.','audit-HomS;audit-HomS-second')]:
 z=copy.deepcopy(c[n]);z.update(final=final,shows=shows,crop=crop,confidence='medium',against_C=True,against_H=True);p['upsert_changes'].append(z)
p['remaining_doubts']=copy.deepcopy(r['remaining_doubts'])
p['remaining_doubts'][0].update(reading='deleted par',alternatives='pour')
p['remaining_doubts'].insert(5,dict(line='10.2 first Hom base',reading='S',alternatives=r'\mathbb{S}; doubled typewriter impression',confidence='medium'))
p['notation_updates_replace']=copy.deepcopy(r['notation_updates'])
p['notation_updates_replace'][1].update(form=r'\unsure{S|\mathbb{S}}',status='uncertain',attestations='10/034 §10.2 first Hom base: two vertically displaced S-shaped impressions; a distinct alphabet is not securely established.')
p['inventory_patches']={x['element']:{'hand':'another unnamed hand'} for x in r['inventory_resolved'] if x['hand']=='unknown'}
p['inventory_patches']['pour1']={'first_words_or_objects':r'\unsure{par|pour}'}
p['inventory_extra']=[dict(scan='10:034',sheet_kind='typescript',hand='another unnamed hand',element='audit-archive',kind='margin note',position='bottom left',first_words_or_objects='archive folio33 retained in comment',transcribed='yes')]
p['crops_upsert']=json.loads(Path('work/audit10_034_crops.json').read_text())
p['observations']='Root ordered second reading: whole and both actual supplied halves were viewed before the image-first receipt and text-open event. All prose, accents, punctuation, symbols, indices, products, arrows, inequalities, underlines, replacements and cancellation states were compared against the consolidated page. All27 fresh audit crops were personally viewed. The isolated faint acute in fermée is retained; inversible is read as typed. The first cancelled pour is broadened to par|pour from its letter spacing and surviving forms. The first Hom base is now uncertain between plain S and a distinct doubled alphabet: the double impression itself is clear. All nine earlier doubtful loci were reexamined; obscured a)/b), the mark before fidèlement, the second cancelled pour, cancelled G, unreadable cancelled word and first 2|1 reference remain unresolved. The preliminary image-first impression that all lower text was ordinary reverse show-through was corrected on closer inspection: the four covered cancelled passages are retained, including the last vertically reflected line. Their physically obscured text remains explicitly doubtful. Top2 is manuscript numbering; bottom33 is archival and remains a comment. No context or mathematical proof check was used.'
Path('work/audit10_034.json').write_text(json.dumps(p,ensure_ascii=False,indent=2))
_,t=build_revision(p,s,r,(out/f'pages/{key}.tex').read_text());Path('work/audited10_034.tex').write_text(t)
