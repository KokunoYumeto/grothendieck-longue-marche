from pathlib import Path
from datetime import datetime, timezone
import csv, json, re

R=Path(__file__).resolve().parent
WORK=R.parents[2]
date=datetime.now(timezone.utc).isoformat()
who='GPT-6 Astra Pro; effort not exposed; primary run MPL_118/root'
fields=['statement_id','date','who','type','outcome']
rows=[]
ledger=json.loads((R/'context_search_ledger.json').read_text())
targeted={
 'MPL118-C06':'Targeted application of the supplied finite-fence example: contractible factors, finite zigzag coordinate bound, and disconnected strict product checked; prior PATHS result not re-proved.',
 'MPL118-C08':'Explicit Z=BC2 or BZ specialization of the scan023 suspension example checked using nonzero suspension H2; not the later acyclic reverse-excision counterexample.',
 'MPL118-C09':'Only the final even/odd telescope implication checked assuming the displayed sequence and filtration hypotheses; missing fraction and factorization dependencies identified, not certified.',
}
for n in ledger['rows']:
    sid=n['id']
    typ='targeted proof check' if sid in targeted else 'carried as background without fault found'
    outcome=targeted.get(sid,'Frozen-text/context comparison and source-locator use recorded; no mathematical proof validation is implied by this row. Mathematical checks, if any, are separately identified by this note ID in the peer event files.')
    outcome+=' Note: '+n['title']+'. Per-note context search: context_search_ledger.json#'+sid
    rows.append(dict(statement_id=sid,date=date,who=who,type=typ,outcome=outcome))

# Log each actually referenced RESULTS_STATE item by its own ID as requested.
state=(WORK/'context/notes/RESULTS_STATE.md').read_text()
known=set(re.findall(r'\*\*((?:[A-Z][A-Z0-9_-]* [A-Z]\.[A-Za-z0-9.]+|118-[a-z0-9-]+|FINMON))\*\*',state))
used=set()
for fn in ['strata_paths_mapping.json','bisite_mapping.json','residue_mapping.json','new_results_mapping.json']:
    d=json.loads((R/fn).read_text())
    for n in d.get('rows',d.get('records',[])):
        used.update(n.get('results_state_ids',[]))
        used.update(v['id'] for v in n.get('results_state_references',[]))
roottext='\n'.join(p.read_text() for p in R.glob('root_*.md'))
used.update(k for k in known if k in roottext)
assert all(k in state for k in used), sorted(k for k in used if k not in state)
for sid in sorted(used):
    rows.append(dict(statement_id=sid,date=date,who=who,
        type='carried as background without fault found',
        outcome='Supplied RESULTS_STATE item used as an explicitly attributed prior-run claim/review label; no re-proof, omitted return-file access, or status upgrade. See associated manuscript note or mapping for relation and exact locator.'))

# Source reading verifies the attribution/formulation, not the source theorem's proof.
for sid,scope in {
 'SOURCE:PS:64':'Read primary L1/L3/L4/L5 formulations at manuscript pp. 164–165; separated absolute L4 from additional fibrewise L5.',
 'SOURCE:DER:II:36-36ter':'Located question, withdrawn Proposition 2.19 and renewed conjecture; no chronological priority proof.',
 'SOURCE:DER:XII:75-78':'Read W7bis/W7 formulations and self-stated formal-verification gap; carried reviewed NR8 counterexample as supplied.',
 'SOURCE:DER:XII:88-89':'Read supplied totality definition and its explicit distinction from Pursuing Stacks; did not identify it with product totality in 118.',
 'SOURCE:DER:XII:107-and-appendix14-15':'Located primary historical pushout-failure assertions and finite inclusion; companion corrected S3 calculation carried as background.',
 'SOURCE:CISINSKI:4.2.4':'Read published strong-saturation statement; no full proof audit.',
 'SOURCE:CISINSKI:4.3.2':'Read product conditions and the printed equivalence; mathematical counterexample application separately checked under C04.',
 'SOURCE:CISINSKI:MO516223':'Directly read author response of 2026-10-21 confirming need for an additional hypothesis; no Lean certificate executed.',
 'SOURCE:MALTSINIOTIS:1.7':'Read product/totality definitions and statement for contextual comparison; not a new proof audit.',
 'SOURCE:COYNE-NOOHI:8.1':'Read groupoid model-structure definitions and Proposition 8.4; C07 is the separately logged application.',
 'SOURCE:REZK:2':'Read sharp-map quantifier and later simplex-test remark for Hua comparison; no historical influence claim.',
 'SOURCE:THOMASON:1980':'Read introduction infinite-product warning and Proposition 4.3/Corollary 4.4 Dwyer pushout statements; no whole-paper validation.',
 'SOURCE:THOMASON:1979':'Bibliographic record only verified; full homotopy-colimit proof not inspected.',
 'SOURCE:MONTPELLIER:117-118':'Catalogue dates/page counts checked; actual cote 117 contents not read.',
}.items():
    rows.append(dict(statement_id=sid,date=date,who=who,type='carried as background without fault found',outcome=scope))

with (R/'root_events.tsv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
print(json.dumps({'root_note_events':len(ledger['rows']),'results_state_ids':len(used),'total_root_events':len(rows)}))
