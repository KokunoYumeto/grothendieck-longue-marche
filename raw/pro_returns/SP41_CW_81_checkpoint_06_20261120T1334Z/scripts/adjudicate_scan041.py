"""Manual title-sheet decisions after three complete returns and one actual root crop view."""
from pathlib import Path
import copy,datetime,json
w=Path(__file__).resolve().parents[1]
rs=[json.loads((w/f'readers/scan041/R{k}/return.json').read_text()) for k in (1,2,3)]
obs=[
'The tall t leads into a connected rounded low return before o. No separate i dot or independently isolated i body settles that turn. Retain relations/relatons, without using another page or lexical expectation to supply i.',
'A thin high stroke beside the initial e descends to the right, favoring the grave-accent first reading of R1/R3. Its lower end approaches the e body. The final shallow turn before the detached point does not securely isolate v. Retain all supplied alternatives and R1’s additional èqui. The grave preference and final-letter uncertainty each follow visible strokes.',
'A full p descent and tall h lead into tightly joined low turns under a broad rising accent, then a final s hook. Those turns leave the extra e unresolved. Retain panachées/panachés without supplying a letter from agreement.'
]
d={'scan':41,'folder':'J81-05','their_page':40,'hua_has':'nothing','filename':'J81-05_81_scan041.tex','status':'decided','findings':[]}
for i,f in enumerate(copy.deepcopy(rs[0]['findings']),1):
 f.update(id=f'SP41-041-{i:03d}',crop='readers/scan041/R1/crop01_title.png',marked_in_H='no',evidence='Main reader, personally viewed complete local title crop: '+obs[i-1],main_adjudication=obs[i-1])
 f['readers']={f'R{k}':rs[k-1]['findings'][i-1]['reading'] for k in (1,2,3)}
 f['reader_source_ids']={f'R{k}':[rs[k-1]['findings'][i-1]['id']] for k in (1,2,3)}
 d['findings'].append(f)
d['reader_finding_coverage']={f'R{k}':{'raw_findings':3,'mapped_findings':3,'all_mapped':True} for k in (1,2,3)}
d['inventory']=copy.deepcopy(rs[1]['inventory'])
for e in d['inventory']:e['sheet_kind']='cover'
d['inventory'][0]['first_words_or_objects']="relations d'èquiv. / non panachées, with the three retained uncertainties"
d['unresolved']=copy.deepcopy(rs[0]['unresolved'])
d['notation']=copy.deepcopy(rs[0]['notation']);d['abbreviations']=copy.deepcopy(rs[0]['abbreviations'])
notes=[
'The sheet carries a two-line topic title at upper right, relations/relatons d’èquiv. (with the retained accent and final-letter alternatives), then non panachées/panachés. The rest of the writing area has no further authorial text. It is catalogued as a title/cover sheet in this inventory; the raw readers used the broader text category.',
'The long q descender reaches the second line and returns left near its middle; the p descent below that line is also complete. These strokes are included in the single coherent crop. No independent insertion leader, cancellation or underline is supplied.',
'Pencil archive number 40 is retained only as a comment. No authorial page number or date is observed. H has no page text, so there are no H collation rows. No mathematical argument, computation, explicit question or author check is present.',
'All three complete texts and every detailed return field were read. All three C doubts remain retained. The final abbreviation is grave-accent-first with R1/R3, recording R2’s unaccented preference and R1’s additional èqui. alternative. Root inspected one existing local title crop and made no new crop; each reader made one crop with complete long descenders. No OCR, outside research, compilation or mathematical proof check was used.'
]
d['notes']=[{'id':f'scan041-note-{i:02d}','text':s} for i,s in enumerate(notes,1)]
d['check_events']=[{'statement_id':n['id'],'date':'2026-11-20','who':'GPT-6 Astra Pro; inherited effort not exposed; main reader scan041','type':'carried as background without fault found','outcome':'Source-account, metadata classification and ink comparison only; no mathematical verification is claimed.'} for n in d['notes']]
d['sweep']=[];d['crop_counts']={'R1':1,'R2':1,'R3':1,'main':0,'total':3};d['main_crop_views']={'R1':[1],'R2':[],'R3':[],'main_new':0,'distinct_total':1,'total':1}
d['decided_utc']=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
t=(w/'readers/scan041/R1/reading.tex').read_text();assert r'\clearpage' not in t;t+='\n\\clearpage\n'
(w/'pages'/d['filename']).write_text(t);(w/'decisions/scan041.json').write_text(json.dumps(d,ensure_ascii=False,indent=2))
p=w/'decisions/drafts/scan041_actual_crop_observations.json';o=json.loads(p.read_text());o.update(status='Decided after complete text and detailed-return comparison.',complete_text_review={f'R{k}':'Complete reading.tex and every detailed return field personally read.' for k in (1,2,3)},final_findings='decisions/scan041.json');p.write_text(json.dumps(o,ensure_ascii=False,indent=2))
(w/'decisions/scan041_main_observations.md').write_text('# Scan041 main-reader observations\n\nAll three complete texts and detailed returns were read. One existing local crop was personally viewed: readers/scan041/R1/crop01_title.png. No whole page or half was viewed by root.\n\n'+'\n\n'.join(f'{i}. {s}' for i,s in enumerate(obs,1))+'\n')
print('Saved scan041: 3 retained C doubts, 1 C editing difference, no H differences.')
