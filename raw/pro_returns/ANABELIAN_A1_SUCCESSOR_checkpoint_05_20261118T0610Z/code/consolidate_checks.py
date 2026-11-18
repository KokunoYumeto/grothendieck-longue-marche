"""Merge explicit check events and statement metadata without inferring checks."""
import csv, json
from pathlib import Path
W=Path(__file__).resolve().parents[1]
reg=json.loads((W/'notes/statement_registry.json').read_text())
for v in reg.values():
    v['review_state']='pending'
    v['check_record']='Not yet checked in this writing. Prior check events are preserved separately.'
events=[]
for rel in ['notes/ROOT_CHECK_EVENTS.tsv','configuration/CHECK_EVENTS.tsv','finite_checks/CHECK_EVENTS.tsv','arithmetic_notes/CHECK_EVENTS.tsv']:
    p=W/rel
    if not p.exists(): continue
    for row in csv.DictReader(p.open(),delimiter='\t'):
        events.append(row)
        key=row.get('statement_id','')
        if key in reg and row.get('type') in ['targeted proof check','independent re-proof','used and rechecked in this run']:
            reg[key]['review_state']='proof_checked'
            msg='Also checked in this writing, '+row['date']+': '+row['who']+'. '+row['outcome']
            if reg[key]['check_record'].startswith('Not yet checked'):
                reg[key]['check_record']=msg
            elif msg not in reg[key]['check_record']: reg[key]['check_record'] += ' | '+msg
p=W/'arithmetic_notes/arithmetic_checks.tsv'
if p.exists():
    for r in csv.DictReader(p.open(),delimiter='\t'):
        events.append({'statement_id':r['target_id'],'date':r['date'],'who':r['checker'],'type':'targeted proof check','outcome':r['method']+'. '+r['scope']+'. '+r['outcome']+'. '+r['evidence']})
meta={}
p=W/'configuration/configuration_metadata.json'
if p.exists():
    a=json.loads(p.read_text())
    for key,v in a.get('new_and_replacement_statements',{}).items():
        v=dict(v); v['id']=key; meta[key]=v
    for key,v in a.get('corrected_carried_dependencies',{}).items():
        if key in reg:
            reg[key]['depends_on']=';'.join(v.get('depends_on',[])) if isinstance(v,dict) else ';'.join(v)
        if isinstance(v,dict):
            vv=dict(v); vv['id']=key; meta.setdefault(key,{}).update(vv)
for rel in ['finite_checks/new_statement_metadata.json','arithmetic_notes/new_statement_metadata.json']:
    p=W/rel
    if p.exists():
        a=json.loads(p.read_text())
        if isinstance(a,dict): a=a.get('statements',list(a.values()))
        for v in a:
            if isinstance(v,dict) and 'id' in v: meta[v['id']]=v
p=W/'arithmetic_notes/arithmetic_results_metadata.json'
if p.exists():
    for v in json.loads(p.read_text()):
        key=v['target_id'];vv=dict(v)
        ac=v.get('author_check',{})
        cr=ac.get('scope','Checked only in this writing')+', '+ac.get('date','2026-11-18')+': '+ac.get('who','GPT-6 Astra Pro')+'. '+ac.get('method','Complete proof written and read')+'. '+v.get('root_second_reading','')
        vv.update({'id':key,'answers':v.get('item',''),'depends_on':v.get('direct_dependencies',[]),'manuscript_passages':v.get('manuscript',{}),'check_record':cr})
        meta[key]=vv
root={
 'A.42':([],'G1(i)','Full central inertia and primitive class; cocycle construction with actual Kummer orientation.'),
 'A.43':(['A.17','A.42'],'G1(i)','Same-label evaluation in the relative cuspidal quotient.'),
 'A.44':(['A.42','A.43'],'G1(i)','Finite exceptional-support Kummer endgame, isolated from construction.'),
 'A.49':(['A.14','A.15'],'A1;G1(i)','Recognition of every noncuspidal point through finite covers and compactness.'),
 'B.68':([], 'N1;A1','Generalized-Jacobian Kummer compatibility with positive sign; characteristic-prime exclusions and modulus conventions stated explicitly.')}
for key,(deps,items,note) in root.items():
    meta[key]={'id':key,'depends_on':deps,'answers':items,'hypotheses_and_where_they_hold':note+' Full hypotheses are displayed in the numbered statement.','check_record':'Checked only in this writing, GPT-6 Astra Pro, 18 November 2026: complete proof written, root targeted reading and configuration-reader second reading; separate effort setting not exposed.','manuscript_passages':'149;32–36; 43;113,132–133' if key=='B.68' else '149;35–36','notes':note}
for key,dep,note in [
    ('B.124',['B.102'],'All characteristic-zero Artin elementary towers with smooth proper relative pairs and finite etale boundaries, including all four exceptional low-genus types. Proves full topology on every finitely generated abelian subgroup; this is stronger than residual finiteness.'),
    ('B.125',['B.97','B.99','B.100','B.101','B.102','B.104','B.124'],'All valuation groups and all dimensions in the standard Artin good-pair convention. Exact finite relation-lattice and Smith divisibility determination. Finite discrete bundle/clutching data are inputs; no uniform equation-to-presentation algorithm is claimed.')
]:
    meta[key]={'id':key,'depends_on':dep,'answers':'N3',
       'check_record':'Checked only in this writing, 18 November 2026: GPT-6 Astra (OpenAI), ChatGPT Pro mode, root complete proof and reading; arithmetic-notes reader full second proof reading with local comparison and finite Kummer joins incorporated. Separate effort setting not exposed. B125 arithmetic certificate: 23863 exact comparisons in23 cases.',
       'manuscript_passages':'149;011,075,079,120 (manuscript page59)',
       'notes':note}
meta['B.130']={'id':'B.130','depends_on':['B.9','B.85','B.86'],'answers':'B2;B4',
    'check_record':'Checked only in this writing,18November2026: GPT-6 Astra (OpenAI), ChatGPT Pro mode. Root complete proof written and read; finite-checks reader separately checked the prime-power primitive factor, arbitrary pointing and finite-field transfer. Separate effort setting not exposed.',
    'hypotheses_and_where_they_hold':'Geometric cyclic ell-power cover, ell different from characteristic and degree greater than one, with primitive p-rank zero. B85 andB86 provide the entire ordinary cubic and two-rank-one quintic loci in characteristic two. Every finite-field form, extension and rational pointing is included.',
    'manuscript_passages':'149;35–36',
    'notes':'Strictly removes two complete nonempty geometric genus-two families from the universal B2 gate. Does not include degree-one covers or claim the remaining loci settled.'}
p=W/'notes/ROOT_ADDITIONAL_METADATA.json'
if p.exists():
    meta.update(json.loads(p.read_text()))
for key,v in meta.items():
    if key in reg and 'depends_on' in v:
        dep=v['depends_on']; reg[key]['depends_on']=';'.join(dep) if isinstance(dep,list) else dep
reg['A.13']['depends_on']='A.45;A.46;A.48'
for ident, additions in {
    'A.28':['A.53','A.54','A.55','A.56','A.57','A.58','A.59','A.60','A.61'],
    'B.5':['B.89','B.141','B.145'], 'B.12':['B.130'],
    'B.32':['B.145'],
    'B.24':['B.85','B.86','B.87'],
    'B.52':['B.119','B.120','B.121','B.122','B.123','B.126','B.127','B.128','B.129','B.131','B.132','B.133','B.134','B.135','B.136','B.137','B.138','B.139','B.140','B.142','B.143','B.144','B.146','B.147'],
    'B.67':['B.85','B.86']}.items():
    previous=[x for x in reg[ident]['depends_on'].split(';') if x]
    reg[ident]['depends_on']=';'.join(dict.fromkeys(previous+additions))
(W/'notes/statement_registry.json').write_text(json.dumps(reg,ensure_ascii=False,indent=2)+'\n')
(W/'notes/consolidated_metadata.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')
with (W/'CHECK_EVENTS.tsv').open('w',newline='') as f:
    wr=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t',extrasaction='ignore');wr.writeheader()
    for event in events:
        for typ in event['type'].split(';'):
            row=dict(event);row['type']=typ.strip();wr.writerow(row)
print(json.dumps({'events':len(events),'metadata':len(meta),'checked_original':sum(v['review_state']=='proof_checked' for v in reg.values())}))
