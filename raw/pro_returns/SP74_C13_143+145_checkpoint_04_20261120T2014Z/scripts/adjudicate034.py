from pathlib import Path
import json
R=Path('/workspace/scratch/8f839dff4bf0/SP74_C13_143+145_work')
p=R/'reviews/143_scan034_readerC.json';d=json.loads(p.read_text());assert not d['changes'] and 'main_adjudication' not in d
for x in d['inventory']:
 x['sheet_kind']='list'
 if x['hand'].startswith('machine'):x['hand']='print'
d['main_adjudication']=dict(original_seen=True,existing_crops_seen=3,main_crops_seen=0,decision='No material change to C. Both unit forms remain uncertain. Retained visible shortened 25.939 separately from arithmetic 25.9398; confirmed no extra operator signs or named column headings. Inventory uses allowed list category for the computer printout.')
d['notes'].append(dict(id='143_scan034-N6',text='The main reader inspected the original orientation and all three existing crops. The first post-decimal digit of the first stack is a short upright with a left entry stroke; the final 7 has a broader curved top and transverse stroke. The numerical check corroborates the preferred 1 but does not supply unseen digits. The list inventory category denotes this computer-produced numerical sheet, not an attribution to the notebook author.'))
d['check_events'].append(dict(statement_id='143_scan034-N6',who='GPT-6 Astra Pro; inherited effort not exposed; SP74 second pass; main reader',type='carried as background without fault found',outcome='Reviewed the existing visual and exact-decimal evidence; no independent recomputation or validation of the generating model was performed.'))
p.write_text(json.dumps(d,ensure_ascii=False,indent=2))
(R/'reviews/143_scan034_main.md').write_text('''# Main-reader adjudication — 143_scan034

The original scan was viewed once in its supplied orientation and all three existing rotated crops were inspected. The printed numerical list and blue annotations are upside down relative to the pencil 33. The two unit endings are small loops and remain m/s|m/o. The heavily retraced U subscript supports m but no independently legible prior character. The written value 25.939 is not completed to the separate stack's 25.9398.

The first stack's ambiguous-looking post-decimal upright is retained as 1, distinguished from the broader-topped crossed 7 and corroborated by the reader's explicitly logged exact subtraction. No arithmetic operator or column description is supplied where the source has none. The first reader's full row collation found no change against C; H is absent. The allowed inventory category list is used for the computer printout, and print/unnamed blue/unnamed pencil hands remain distinct. The independent second reader will inspect the complete sheet again after all first readings are accepted.
''')
