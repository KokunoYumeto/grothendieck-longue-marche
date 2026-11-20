from pathlib import Path
import json

out=Path(__file__).resolve().parents[1]
p=out/'documentation/reviews/scan099/report.json'
r=json.loads(p.read_text())
rows={c['id']:c for c in r['changes']}
merges=[]
for keep,remove in [('099-10','099-11'),('099-13','099-14')]:
    a,b=rows[keep],rows[remove]
    merges.append({'kept':keep,'merged':remove,'reason':'One written locus, counted once; reading and state are recorded together.'})
    a['scan_shows']+=' '+b['scan_shows']
    a['c']=b['c'];a['h']=b['h'];a['final']=b['final']
    a['category']=b['category'];a['kind']=b['kind']
    a['place']='Heading: singular live underlined Remarque.' if keep=='099-10' else 'Inserted explanatory parenthesis: i.e. and insertion state'
    del rows[remove]
rows['099-16']['final']=r'des paramètres \deleted{\unsure{comme}} \inserted{tels que} ceux désignés par'
rows['099-16']['c']=r'des paramètres \deleted{\unsure{comme}} \inserted{tels que} ceux désignés par'
for num,u in enumerate(r['unresolved_comparisons'],24):
    d=next(d for d in r['decisions'] if d['id']==('D099-02' if num==24 else 'D099-03'))
    rows[f'099-{num}']={
        'id':f'099-{num}','place':u['place'],'c':u['c'],'h':u['h'],'final':u['final'],
        'c_changed':True,'h_changed':num==25,'category':'Symbols and indices' if num==24 else 'Other',
        'kind':'misread symbol or index' if num==24 else 'other','marked_in_H':False,
        'confidence':d['confidence'],'scan_shows':d['what_the_ink_shows']+' This is a retained disagreement with the preferred reading; it does not establish that the witness alternative is impossible.',
        'box':u['box'],'crop':u['crop'],'consequential':False,'math_note':'','unresolved_comparison':True
    }
r['changes']=list(rows.values())
r['main_adjudication_merges']=merges
for c in r['changes']:
    c['main_review']='Main reader inspected the saved crop and confirms the stated ink evidence; surviving alternatives remain marked in the page.'
r['notes'].append('The two newly localized uncertainties are entered in the comparison apparatus because their preferred readings differ from C (and the opening delimiter also differs from H). These are retained disagreements, not established errors excluding all witness alternatives. The heading and inserted explanatory parenthesis each count once, with their reading and state recorded together.')
r['certainty_decisions'] += [
    {'place':'on pourrait','reading':'pourrait','confidence':'high','reason':'First C alternative confirmed; the low ou-rr-ai sequence and final t exclude prendrait at this locus.'},
    {'place':'final word','reading':'le','confidence':'high','reason':'Native half shows a looped l and open e. This is the first C alternative, retained without supplied continuation.'}
]
r['main_review_complete']=True;r['inventory_review_complete']=True
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
p=out/'documentation/root_view_ledger.json';d=json.loads(p.read_text())
d['99']['crops_seen']=sorted(set(d['99']['crops_seen']+[f'crops/scan099_root_099-{i:02}.jpg' for i in [3,5,9,10,15,17,18]]))
p.write_text(json.dumps(d,indent=2)+'\n')
