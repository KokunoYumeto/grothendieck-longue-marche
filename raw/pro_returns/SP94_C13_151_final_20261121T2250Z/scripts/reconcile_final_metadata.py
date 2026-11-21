"""Reconcile final metadata after the independent audits; preserve stage history."""
from pathlib import Path
from datetime import datetime,timezone
from collections import Counter
import json,csv,re,copy
W=Path(__file__).resolve().parents[1];state=json.loads((W/'run_state.json').read_text());stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');history={};out=[]
for p in state['order']:
 f=W/'reports'/f'{p}.json';r=json.loads(f.read_text());before=copy.deepcopy(r);ids={q['id']:q for q in r['changes']}
 # Declared tentative classifications for new or newly qualified readings.
 for ident in {'151_scan052':['r20','r49'],'151_scan055':['r84','r85'],'151_scan059':['r010','r040','r061','r072'],'151_scan060':['r62']}.get(p,[]):
  ids[ident]['tentative']=True
 for q in r['changes']:q['substantive']=bool(q.get('diff_c') or q.get('diff_h'))
 # Scope excerpts to the actual independently counted physical feature.
 scopes={
 '151_scan054':{'r01':{'h':r'\textbf{Question}'}},
 '151_scan055':{'r56':{'c':'superscript star on the final X','h':'overdot on the final X','final':'superscript star on the final X'}},
 '151_scan058':{'r23':{'c':'single underline under the final equality chain','h':'no underline','final':'single underline under the final equality chain'}},
 '151_scan059':{'r056':{'c':'underline present under top','h':'no underline under top','final':'underline present under top'}},
 '151_scan061':{'r18':{'c':'live','h':'struck','final':'live'}}}
 for ident,fields in scopes.get(p,{}).items():ids[ident].update(fields)
 def change_note(nid,fun):
  nonlocal_placeholder=None
  for i,n in enumerate(r['notes']):
   if re.match(re.escape(nid)+r'(?=[.:\s])',n):r['notes'][i]=fun(n);return
  raise AssertionError((p,nid))
 # Numerical claims belong explicitly to their original reading stage.
 count_notes={'151_scan039':['scan039.N10'],'151_scan040':['scan040.N12'],'151_scan045':['scan045.N10'],'151_scan046':['scan046.N11'],'151_scan048':['scan048.N11'],'151_scan052':['scan052.N10'],'151_scan055':['scan055.N10'],'151_scan059':['scan059.N10'],'151_scan060':['scan060.N11']}
 for nid in count_notes.get(p,[]):
  change_note(nid,lambda n,nid=nid:re.sub(r'^'+re.escape(nid)+r'[.:]?\s*',nid+'. First-pass accounting, retained as history; the final reconciled totals are in the changes summary and this report’s counts object. ',n,count=1))
 if p=='151_scan043':change_note('scan043.N6',lambda n:n.replace('C first readings are substantively retained throughout.','At the first-pass stage, C first readings were substantively retained throughout. Blind adjudication subsequently added the tentative comma correction in r10; see N11.'))
 if p=='151_scan052':change_note('scan052.N3',lambda n:n.replace('The assertion was not proved.','The first reader did not prove the assertion; the later main-reader targeted proof is recorded in scan052.N13.'))
 if p=='151_scan055':
  change_note('scan055.N1',lambda n:n.replace("Root is recording the independent proposition and I' reduction checks separately.",'The later main-reader checks are recorded in scan055.N13 and scan055.N14.'))
  change_note('scan055.N5',lambda n:n.replace('interlinear comparison','interlinear cancelled trial (now the doubtful x in Xi cap Xj = span; see scan055.N15)'))
 if p=='151_scan056':change_note('scan056.N4',lambda n:n.replace('General étaleness, preservation, and the warning','At the first-reader stage, general étaleness, preservation, and the warning')+' The subsequent main-reader preservation check and starred-family counterexample are recorded in scan056.N11; étaleness remains unproved here.')
 if p=='151_scan057':change_note('scan057.N6',lambda n:n.replace('Parent is separately auditing the globally permitted noninjective case and will attach its cross-page counterexample/refinement.','The subsequent cross-page counterexample and sufficient refinement are recorded in scan057.N12 and scan057.N13.'))
 if p=='151_scan058':change_note('scan058.N3',lambda n:n.replace('No independent proof of these premises or their index range is claimed here; no contextual regularisation is made.','This describes the isolated first reader’s status. The later cross-page proof, counterexample and inclusion checks are recorded in scan058.N8–N10. No contextual regularisation is made in the transcription.'))
 if p=='151_scan059':
  ids['r010']['consequential']='The N accent is now explicitly check/tilde, with check preferred; the alternative remains unresolved.'
  change_note('scan059.N2',lambda n:n.replace('a checked N','an N with the preferred check and an explicit tilde alternative').replace('check accent','preferred check/tilde accent'))
  # The first sentence may use another original spelling; append an explicit final qualifier.
  change_note('scan059.N2',lambda n:n+' Blind adjudication leaves the top V/dotted-V and N check/tilde forms explicitly uncertain; see N13.')
  for q in r['notation']:
   if q['form']==r'\check N':q.update(form=r'\unsure{\check N|\widetilde N}',evidence='An angular valley favors a check, but the short hooked entry and compact scale permit tilde; the final audit retains both.')
  for q in r['hand']:
   if q['habit']=='Reduced à resembles a colon':q.update(evidence='The tiny lower bodies and detached upper strokes favor reduced à, but three occurrences remain explicitly à/colon after blind review. The larger lower curve before fibre un cylindre is clearer.',every_occurrence='No; local certainty varies.',misread_places='H proposes colons after the two homéomorphe forms. These are final unresolved comparisons, not unqualified errors; the preferred à is recorded with its alternative.')
 if p=='151_scan060':
  change_note('scan060.N6',lambda n:re.sub(r'Parent[^.]*will[^.]*\.', 'The completed main-reader endpoint check is recorded in scan060.N16.',n))
  change_note('scan060.N8',lambda n:n.replace('uses succ.','uses the short form now retained as succ./success.').replace('succ. has','the preferred succ. short form has'))
  for q in r.get('notation',[]):
   if 'succ.' in q.get('form','') or 'succ.' in q.get('evidence',''):q['evidence']=q.get('evidence','')+' The blind audit now leaves the abbreviated form succ./success. explicit.'
 if p=='151_scan061':
  for q in r.get('additional_h_mark_reviews',[]):
   if q.get('reading')==r'\unsure{sans}':q.update(reading=r'\unsure{sans|dans}',evidence='The first word remains preferred as sans; the tall angular entry also permits the blind dans. Final adjudication retains both.')
 if p=='151_scan049':
  for q in r.get('representation_decisions',[]):
   if q.get('place')=='Remarques':q.update(final=r'\uline{Remarques}\unsure{.}',reason='Actual underline retained; bold is treated as its representation. The terminal point was qualified during the blind audit and remains doubtful.')
 # Preserve old count schemas instead of allowing them to look final.
 old_counts=r.pop('counts',{})
 if old_counts:r['historical_counts_before_final_reconciliation']=old_counts
 legacy_keys=['reading_change_count','substantive_departures_c','substantive_departures_h','secure_c_departures','tentative_c_departures','secure_h_departures','tentative_h_departures','certainty_only_entries']
 legacy={k:r.pop(k) for k in legacy_keys if k in r}
 if legacy:r['historical_first_reader_count_fields']=legacy
 if 'open_parent_review' in r:r['historical_first_reader_review_requests']=r.pop('open_parent_review')
 active=[q for q in r['changes'] if q.get('diff_c') or q.get('diff_h')]
 dc=Counter(q['confidence'] for q in active if q.get('diff_c'));dh=Counter(q['confidence'] for q in active if q.get('diff_h'));dec=Counter(q['decision'] for q in r['decisions'])
 r['counts']={'stage':'final after blind adjudication and physical-place reconciliation','comparison_records':len(r['changes']),'disagreement_places':len(active),'differences_from_c':sum(dc.values()),'differences_from_h':sum(dh.values()),'confidence_against_c':{k:dc[k] for k in ['high','medium','low']},'confidence_against_h':{k:dh[k] for k in ['high','medium','low']},'places_against_both':sum(bool(q.get('diff_c') and q.get('diff_h')) for q in active),'certainty_only_comparison_records':len(r['changes'])-len(active),'supplied_marks':len(r['decisions']),'mark_decisions':{k:dec[k] for k in ['first','alternative','other','undecided']},'remaining_doubt_records':len(r['doubts']),'inventory_elements':len(r['inventory']),'audit_boxes':r['audit_summary']['boxes'],'audit_token_differences':r['audit_summary']['differences'],'audit_changed_boxes':r['audit_summary']['changed']}
 r['final_metadata_reconciled_utc']=stamp
 r['record_scope']='Counts and main change/decision fields describe the final adjudication. Scope, line/crop inspection records, audit-box first readings, workflow and explicitly historical fields document their original reading stages. Original first/second TSVs and neutral box lists remain immutable.'
 history[p]={'counts_before':before.get('counts',{}),'legacy_count_fields':legacy,'notes_before':before['notes']}
 f.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');out.append({'page':p,**r['counts']})
(W/'audit/metadata_reconciliation_history.json').write_text(json.dumps({'utc':stamp,'original_readings_changed':False,'before':history},ensure_ascii=False,indent=2)+'\n')
(W/'audit/final_page_counts.json').write_text(json.dumps({'utc':stamp,'pages':out},ensure_ascii=False,indent=2)+'\n')
with (W/'progress.log').open('a') as f:f.write('final metadata reconciled '+stamp+': uniform final per-page counts; historical counts/stage notes labelled; comparison excerpts scoped; original first/second and box files unchanged\n')
print('Reconciled final metadata for',len(out),'pages.')
