from pathlib import Path
import json
r=Path(__file__).resolve().parents[1]
p=r/'records/root_note_items.json'; a=json.loads(p.read_text()); d={x['id']:x for x in a}
d['C64-N15']['ledger']='No settled RESULTS_STATE entry for this finite subgroup-poset request; local computation only.'
d['C64-N19']['ledger']='LM7 D.45 mentions S4 among its order24 marked bases; carried only as background, with its relative pro2-completion assertions unchecked here.'
d['C64-N19']['query']+='|D\\.45|even bases'
p.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
p=r/'records/question_note_items.json'; a=json.loads(p.read_text()); d={x['id']:x for x in a}
d['C64-Q07']['scans']='002–039, whole-packet scope; literature comparison for S20'
p.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
p=r/'records/assemble_notes.py';s=p.read_text()
s=s.replace("r'\\b(scans?|pages?|cotes?|on|at|all|order|orders|Table|from|before|after|formula|formulas|Part|part|Theorem|Corollary|Remark|Definition|Corollaire|lines?|rg|modulo)(?=\\d)',r'\\1 ',s)","r'\\b(scans?|pages?|cotes?|on|at|all|order|orders|Table|from|before|after|formula|formulas|Part|Theorem|Corollary|Remark|Definition|Corollaire|lines?|rg|modulo|and|levels?|especially|labell?ing|rank|of|to|sections?)(?=\\d)',r'\\1 ',s,flags=re.I)")
s=s.replace("s=s.replace('characteristicp'", "s=re.sub(r'\\bTable(?=[A-Z]\\b)','Table ',s)\n s=s.replace('determinant+1','determinant +1').replace('modulo±1','modulo ±1')\n s=re.sub(r'(?<=\\d)\\((?=Katz|Ledet|Hoshi|Ogus|Bouw)',' (',s)\n s=s.replace('characteristicp'")
s=s.replace("'## I. Answers to the requested research questions','']", "'Current scan numbers refer to the PDF64.pdf numbering; the author’s numbers are listed separately in TableB. Hua’s page n corresponds to the present scan n+1, as stated in notes/RESULTS_STATE.md, so each current-scan locator also identifies the leaf being compared with his subsection unless another context scan is specified.','',\n'## I. Answers to the requested research questions','']")
s=s.replace('PDF64.pdf','PDF 64.pdf').replace('TableB. Hua','Table B. Hua')
p.write_text(s)
p=r/'records/assemble_check_events.py';s=p.read_text()
s=s.replace("event(id,typ,'Source-place pointer to actual check(s) recorded under '+notes_id+'; see those rows for method, checker, evidence and restrictions. This is the same check indexed by primary-text place, not another independent run.')", "event(id,typ,'Source-place pointer to actual check(s) recorded under '+notes_id+'; see those rows for method, checker, evidence and restrictions. This is the same check indexed by primary-text place, not another independent run.', groupwho if notes_id.startswith(('C64-N21','C64-N23','C64-N25','C64-N27','C64-N30','C64-N32')) else rootwho)")
p.write_text(s)
print('Final text precision and formatting adjustments applied')
