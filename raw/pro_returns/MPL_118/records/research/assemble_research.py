from pathlib import Path
import csv, re, json

R = Path(__file__).resolve().parent
ROOT = R.parents[1]
parts = [
    'root_notes.md', 'root_additional_checks.md', 'root_claims.md',
    'root_self_flags.md', 'root_reading_questions.md', 'root_titles.md',
    'root_bibliography.md',
    'strata_paths_mapping.md', 'bisite_mapping.md',
    'residue_mapping.md', 'new_results_mapping.md',
]
available = [p for p in parts if (R/p).exists()]
missing = [p for p in parts if not (R/p).exists()]
chunks = []
for p in available:
    text = (R/p).read_text()
    if p.endswith('_mapping.md'):
        text = re.sub(r'^(#{1,5}) ',r'\1# ',text,flags=re.M)
    chunks.append(text)
(ROOT/'MPL_118_notes.md').write_text('\n\n'.join(chunks))

allowed = {
    'targeted proof check', 'independent re-proof',
    'computation or formal certificate', 'used and rechecked in this run',
    'carried as background without fault found',
}
rows = []
for p in sorted(R.glob('*events.tsv')):
    with p.open() as f:
        for x in csv.DictReader(f, delimiter='\t'):
            sid = x['statement_id']
            if re.match(r'^C\d', sid): sid = 'MPL118-'+sid
            rawtype = x.get('type', x.get('event_type'))
            typ = rawtype
            if typ not in allowed and not typ.startswith('refuted,'):
                if any(k in typ.lower() for k in ('check', 'proof', 'application')):
                    typ = 'targeted proof check'
                else:
                    raise ValueError((p, typ))
            who = x['who']
            if 'model' in x:
                who = '; '.join([x['model'], 'effort '+x['effort'], who, 'run '+x['run']])
            elif 'run ' not in who:
                agents = {
                    'residue_new_events.tsv':'/root/residue_new_mapping',
                    'targeted_proof_peer_events.tsv':'/root/residue_new_mapping',
                    'groupoid_pushout_peer_events.tsv':'/root/residue_new_mapping',
                    'weak_sieve_pushout_peer_events.tsv':'/root/residue_new_mapping',
                    'strata_paths_events.tsv':'/root/checkpoint_support',
                }
                who += '; run MPL_118 '+agents.get(p.name,p.stem)
            outcome = x['outcome']
            if rawtype != typ: outcome = rawtype+': '+outcome
            if x.get('scope'): outcome += ' Scope: '+x['scope']
            outcome += ' Event record: records/research/'+p.name
            if x.get('evidence_record'): outcome += '; evidence '+x['evidence_record']
            rows.append(dict(statement_id=sid,date=x.get('date',x.get('date_utc')),who=who,type=typ,outcome=outcome))
fields = ['statement_id','date','who','type','outcome']
with (ROOT/'CHECK_EVENTS.tsv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n')
    w.writeheader();w.writerows(rows)
print(json.dumps({'notes_bytes':(ROOT/'MPL_118_notes.md').stat().st_size,
                  'events':len(rows), 'missing_note_parts':missing}, ensure_ascii=False))
