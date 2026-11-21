"""Exclude certainty-only rows and align counts with accepted primary readings.

The original row snapshots stay in the canonical report as excluded_witness_rows.
Page files, doubts, supplied-mark decisions, blind comparisons and audit counts
are untouched. This is a one-time accounting correction, not a reading pass.
"""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib

ROOT=Path(__file__).resolve().parents[1]
receipt=ROOT/'review/witness_count_reconciliation.json'
assert not receipt.exists(),'Accounting reconciliation has already been applied.'
exclusions={
 114:{17:'C and H explicitly recognize the full brace scope; H states it in its explanatory note. Treat this as an accurate stated graphic reading, consistently with112, rather than counting its partial display wrapper as another source-reading error.'},
 122:{22:'The primary number188 is unchanged; only its last digit becomes uncertain.',23:'The inserted primary label s_i and insertion state are unchanged; delta_i is an added alternative.'},
 123:{24:'The primary canceled relation remains greater-than-or-equal; the strict alternative only adds uncertainty.'},
 124:{24:'At the stated locus the second argument remains d-prime primary; its uncertainty is new. The first-argument correction in the contextual snippet is already counted in original rows[2].',25:'The primary terminal point is unchanged; comma is an added alternative.'},
 126:{17:'The primary word remains croisements; only its ending becomes uncertain.'},
 127:{22:'The primary pronoun remains elle; elles is an added alternative.'},
 129:{39:'The primary terminal point is unchanged; dash is an added alternative.'},
 130:{33:'The primary preposition remains de; du is an added alternative.',34:'The primary label remains210; uncertainty is localized to its middle digit.'},
}
flag_changes={
 123:{18:{'against_C':False}},
 126:{11:{'against_C':True,'against_H':False}},
 127:{0:{'against_C':False}},
 130:{2:{'against_C':False}},
}
hashes={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (ROOT/'pages').glob('*.tex')}
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
record={'applied_at':now,'excluded_rows':[],'flag_changes':[],'scope':'Witness-row accounting only. All page readings, doubts, audit changes/counts and frozen evidence are unchanged.'}
for scan in sorted(set(exclusions)|set(flag_changes)):
 p=ROOT/'review'/f'147_scan{scan}_reviewed.json';d=json.loads(p.read_text())
 for index,fields in flag_changes.get(scan,{}).items():
  row=d['rows'][index]
  for key,value in fields.items():
   record['flag_changes'].append({'scan':scan,'original_row_index':index,'place':row['place'],'field':key,'old':row[key],'new':value})
   row[key]=value
 removed=exclusions.get(scan,{})
 for index,reason in sorted(removed.items()):
  row=d['rows'][index]
  item={'original_row_index':index,'excluded_at':now,'reason':reason,'row':row}
  d.setdefault('excluded_witness_rows',[]).append(item)
  record['excluded_rows'].append({'scan':scan,**item})
 d['rows']=[row for i,row in enumerate(d['rows']) if i not in removed]
 p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
record['previously_applied_flag_change']={'scan':131,'original_row_index':6,'field':'against_H','old':True,'new':False,'reason':'The final primary se réduisant agrees with H; the added alternatives alone are not a witness change.'}
assert all(hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==h for name,h in hashes.items())
receipt.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
with (ROOT/'review/administrative_audit_corrections.md').open('a') as f:
 f.write('\n## Final witness-count reconciliation — '+now+'\n\n')
 f.write('Excluded ten certainty-only/duplicate-locus rows from the witness-change tables, retaining their complete snapshots in `excluded_witness_rows`, their doubts, and all blind audit changes. Excluded one additional brace-scope row because H explicitly described that scope correctly. Five witness-specific flags were corrected here, plus the earlier131 agreement flag. No manuscript reading, mark decision or blind-audit count changed. Original pre-removal indices and complete evidence are in `review/witness_count_reconciliation.json`.\n')
with (ROOT/'progress.log').open('a') as f:
 f.write(f'witness-count reconciliation {now}: eleven rows excluded from substantive counts with snapshots retained; primary-reading flags aligned; page bytes and blind-audit counts unchanged\n')
print(json.dumps({'excluded_rows':len(record['excluded_rows']),'flags_changed_now':len(record['flag_changes']),'earlier_flag_correction':1}))
