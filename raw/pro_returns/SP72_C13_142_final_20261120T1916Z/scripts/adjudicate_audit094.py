"""Main-reader adjudication of three points and a reopened label doubt."""
import json
from audit_support import load,replace_exact,commit,OUT

r,a,s=load(94)
ad=[]
for i,c in enumerate(a['changes'],1):
    s=replace_exact(s,c['before'],c['after'])
    if i<=3:
        r['changes'].append({'id':f'094-A{i:02}','place':c['place'],
            'c':c['c'],'h':c['h'],'final':c['after'].strip(),
            'c_changed':True,'h_changed':False,'category':c['category'],'kind':c['kind'],
            'marked_in_H':i>1,'confidence':'medium','scan_shows':c['scan_shows'],
            'box':c['box'],'crop':c['crop'],'consequential':False,
            'math_note':c['witness_effect']+' H’s different or unrecovered wording is already collated at '+c['affected_existing_comparison']+'; this punctuation change adds no second H count.'})
    ad.append({'id':c['id'],'decision':'accepted' if i<=3 else 'certainty-only reopening',
               'reading':c['after'].replace(r'\qquad','').strip(),
               'evidence':c['scan_shows'],'crop':c['crop'],'confidence':'medium'})

row=next(x for x in r['changes'] if x['id']=='094-31')
row['final']=row['final'].replace('endom.','endom')
row=next(x for x in r['changes'] if x['id']=='094-34')
row['final']=row['final'].replace('endom. ext.,','endom ext,')
row['scan_shows']=row['scan_shows'].replace('comme endom. / ext.,','comme endom / ext,')

d=next(x for x in r['decisions'] if x['id']=='M0406')
d.update(decision='other',reading='comme endom ext, en dépend',
    what_the_ink_shows='The words and singular ending can be followed across the two short lines. The second reading finds no independent point after endom and only a comma after ext; the earlier supplied points are removed.')
for x in r['certainty_decisions']:
    if x['place']=='Outer note clause':
        x['reading']=d['reading'];x['reason']=d['what_the_ink_shows']
r['certainty_decisions']=[x for x in r['certainty_decisions'] if x['place']!='First display number']
c=a['changes'][3]
d=next(x for x in r['decisions'] if x['id']=='M0401')
d.update(decision='undecided',reading=r'\unsure{(47)|47)}',
         what_the_ink_shows=c['scan_shows'],crop=c['crop'],confidence='medium')
r['doubts'].append({'scan':94,'decision_id':'M0401','place':c['place'],
    'reading':d['reading'],'alternatives':['(47)','47)'],'confidence':'medium',
    'reason':c['scan_shows'],'crop':c['crop']})
r['hand_log'].extend(a['hand_log_additions'])
for x in r['abbreviations']:
    if x['form']=='ext.':x['form']='ext. / ext'
r['notes'].extend([
    'The complete second reading removes three unsupported abbreviation points in the outer note: first endom before underlined ext., second endom after comme, and the point before the comma in the following ext, en dépend. The first ext. and later endom. ord. retain their distinct points. Main reader and auditor independently reused the outer-note crop.',
    'M0401 is reopened with (47) preferred and 47) as the alternative. The low upreturning hook touches the 4 and cannot securely be separated from its terminal stroke. The digits and right parenthesis are clear; only the left parenthesis is doubtful. This certainty change adds no substantive count.',
    'The new audit crop of i.e. confirms both separate abbreviation points and causes no change. All 31 inventory elements, 65 inherited comparison loci and 15 assigned marks were reviewed; 30 inherited doubts plus the reopened label remain. No missing element or new mathematical check event.'
])
p=OUT/'documentation/root_view_ledger.json';ledger=json.loads(p.read_text())
for crop in ['crops/scan094_audit_label47.jpg','crops/scan094_audit_ie.jpg']:
    if crop not in ledger['94']['crops_seen']:ledger['94']['crops_seen'].append(crop)
p.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n')
commit(94,r,a,s,
    'Complete independent second reading by reader_b. All 65 inherited comparison loci, 15 assigned marks and 31 inventory elements were reviewed. Main reader inspected the existing outer-note crop and both new audit crops, accepting three C-only punctuation corrections, confirming unchanged i.e., and reopening M0401 as a certainty-only opening-parenthesis doubt. Thirty inherited doubts plus the reopened label remain. No new inventory element or mathematical check event.',ad)
