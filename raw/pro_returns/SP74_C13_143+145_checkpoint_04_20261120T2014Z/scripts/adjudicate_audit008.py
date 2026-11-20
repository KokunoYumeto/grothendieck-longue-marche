from pathlib import Path
import json,copy
R=Path(__file__).resolve().parents[1]
key='143_scan008';reader='B'
r=json.loads((R/'reviews'/f'{key}_accepted.json').read_text())
a=json.loads((R/'reviews'/f'{key}_audit{reader}.json').read_text())
by={x['place']:x for x in r['changes']}
p={'key':key,'reader':reader,'findings':[
 {'index':1,'decision':'accept','reason':'Main re-inspected the existing donnee/reference crop: the lower return is continuous with the small phi; no detached i dot or independent index stem is secure. Preserve varphi first with indexed alternative, without asserting a definite authorial omission.'},
 {'index':2,'decision':'accept','reason':'Main re-inspected the rotated margin crop: two dark points and three diminishing but aligned short marks support five, with the smallest terminal mark not secure enough to exclude four. Preserve the explicit count alternative.'}],
 'change_operations':[],'remaining_doubts_add':a['remaining_doubts'][-3:],
 'notes_remove':['143_scan008-N1','143_scan008-N4'],'notes_add':[],
 'check_events_add':[],
 'hand_log_add':[{'habit':'Small phi can end in a continuous rising lower return which resembles an index.','places':'143_scan008, small varphi before (17)','scope':'Only this index is newly doubtful; the separately visible indices on capital Phi are preserved.','misreadings':'Both C and H assert varphi_i; the final text prefers unindexed varphi with the indexed form retained as an alternative.'}],
 'main_summary':'Main inspected the existing donnee/reference, rotated marginal-note, and Phi-punctuation crops. Accepted both local uncertainties. Kept the composite action-group rows against both witnesses because the decorated X subscript still differs from C, even though preferred E itself agrees. All other accepted readings and nine original MARKS decisions stand.'}
f=a['findings'][0]
p['change_operations'].append({'operation':'append','row':{
 'place':f['place'],'C':r'\varphi_i','H':r'\varphi_i','final':r'\unsure{\varphi|\varphi_i}',
 'against_C':True,'against_H':True,'kind':f['kind'],'ink':f['reason'],'confidence':'low','crop':f['crop'],'box':f['box'],'marked_in_H':False,'consequential':True}})
old='reference after varphi_i';z=copy.deepcopy(by[old]);z.update(place='reference after small varphi',C='(17)',H='de (17)',final='(17)')
p['change_operations'].append({'operation':'replace','place':old,'row':z})
old='margin final X(I) and suspension points';z=copy.deepcopy(by[old]);z['final']=a['findings'][1]['after'];z['ink']=z['ink'].split('The prime and parenthesized I')[0]+'The prime and parenthesized I are present. Two strong points and three diminishing aligned traces follow; five is preferred with four retained as a count alternative. The simpler X does not establish a different variable.'
p['change_operations'].append({'operation':'replace','place':old,'row':z})
old='punctuation after family name Phi';z=copy.deepcopy(by[old]);z['ink']='A single dark point lies separately at baseline to the right of Phi. There is no upper point for a colon and no descending comma tail. The thick hooked foot includes a short upright and cross-stroke; it may be retracing or an obscured canceled small index. No independent index can be read, so none is supplied.'
p['change_operations'].append({'operation':'replace','place':old,'row':z})
for old in ['first action-group occurrence after (23)','second action-group occurrence before sur le mb','third action-group occurrence before sur T']:
 z=copy.deepcopy(by[old]);z['ink']+=' The preferred E matches C, but C has ordinary X where the visible decorated subscript is encoded mathfrak X; therefore this composite locus remains against both witnesses.'
 p['change_operations'].append({'operation':'replace','place':old,'row':z})
for n in r['notes']:
 if n['id']=='143_scan008-N1':
  z=copy.deepcopy(n);z['text']=z['text'].replace('varphi_i in (17)','the small varphi (index uncertain: varphi|varphi_i) in (17)');p['notes_add'].append(z)
 if n['id']=='143_scan008-N4':
  z=copy.deepcopy(n);z['text']+=' The different-reader audit and main reinspection leave the physical segmentation of the thickened foot open: a canceled small index is not excluded, but no separate character can be read.';p['notes_add'].append(z)
for e in a['check_events']:
 z=copy.deepcopy(e);z.update(date='2026-11-20',who='GPT-6 Astra Pro; inherited effort not exposed; SP74 second pass; second reader B');p['check_events_add'].append(z)
(R/'reviews'/f'{key}_main_audit_plan.json').write_text(json.dumps(p,ensure_ascii=False,indent=2))
