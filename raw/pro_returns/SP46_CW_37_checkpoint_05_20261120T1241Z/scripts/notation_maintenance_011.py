from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
O=Path(__file__).resolve().parents[1]
t=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
files=list((O/'pages').glob('*.tex'))+[O/'SP46_CW_37_transcription.tex']
before={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
p=O/'notation_review.json';r=json.loads(p.read_text())
r['reviewed_through_scan']=76;r['reviewed_utc']=t
for g in r['groups']:
    if g['group']=='Ruled Roman numerals':
        g['scans'] += [74,75]
        g['finding']+=' The separately penned VI and II in the pencil note on 075 retain both rules; the typed XI in the 074 letter has neither rule. These different physical constructions remain distinct.'
    if g['group']=='Detached marginal points':
        g['scans'] += [74,75,76]
        g['finding']+=' The 074 hook is a single unassigned curve. The 075 pair has two visible faint companions preserved with its irregular lobes; the 076 pair has its own irregular contours, without treating the surrounding pale processing halo as additional authored punctuation. Main inspected each retained local crop; no cross-page colon normalization is made.'
r['groups'] += [
    {'group':'Deligne letter alphabets','scans':[75,76],'finding':'The signed two-leaf letter consistently distinguishes script N and script initials in Hom/Ext from ordinary cohomology H and formula K. The introductory K on 075 alone has a doubtful doubled left stem and remains K/blackboard K; plain later copies do not erase that local ink ambiguity.'},
    {'group':'Elevated algebraic/analytic qualifiers','scans':[75,76],'finding':'Both leaves place alg/an above the cohomological degree. Parentheses are present around alg in the first display of 076 and are preserved there; they are not supplied to the unparenthesized qualifiers in 075. The upper-right H^0 in the 075 diagram remains without alg because the three half readings agree on its absence.'},
    {'group':'Recurring uncertain eta-like letters','scans':[52,76],'finding':'The 052 eta/y uncertainty and the 076 eta/n transition glyph belong to different local contexts and pen constructions. Each is marked at its first repeated occurrence under the same convention, with its own supported alternatives. The 076 two-stem crop excludes gamma; that decision does not alter the different 052 locus.'},
    {'group':'Local indices and arrow decorations','scans':[75,76],'finding':'The letter keeps superscript cohomological degrees, subscript d_2 and X_0, upper primes on local extensions, and tall restriction bars distinct. The 075 comparison has its observed vertical and horizontal arrows; the 076 local-isomorphism arrow has a single wave above. The 076 target index remains ambiguous despite the conditional composition check.'}
]
r['remaining_scope']='Scan 077 is being read; scans 085–098 follow in the prescribed page list. Extend this review through all 25 pages before freezing.'
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
leg=O/'legibility.txt';s=leg.read_text().replace('Provisional assessment through scan 074;','Provisional assessment through scan 076;')
s+='\nThe two-leaf Deligne letter has mostly readable flowing blue handwriting, but doubled or retraced stems, a crowded target index and a possible overwritten d/t remain less secure. Mathematical context was useful as a diagnostic, yet it did not decide those shapes. The source records also preserve d_2 eta beside an earlier class e and the grammatical donné exactly as read. Its sparse pencil annotations and detached grey or dark marks need more caution than the body.\n'
leg.write_text(s)
ep=O/'global_check_events.json';events=json.loads(ep.read_text());events.append(dict(statement_id='NOTATION-REVIEW-THROUGH-076',date=t,who='GPT-6 Astra Pro; effort not exposed; main second-pass run',type='used and rechecked in this run',outcome='Extended cumulative notation comparison through 11 committed pages using the completed independent visual records and retained main-adjudicated crops. Confirmed script/plain letters, double-raised qualifiers, ruled/unruled Roman references and page-specific graphical shapes. Preserved local uncertainties rather than normalizing from context. No transcription bytes changed and no theorem proof was performed.'));ep.write_text(json.dumps(events,ensure_ascii=False,indent=2)+'\n')
assert before=={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
with (O/'progress.log').open('a') as f:
    f.write(f'notation review through scan 076 {t}; 11 page files and combined source hashes unchanged\n')
    f.write(f'scan 077 readers A/B/C launched fresh under brief v08 {t}\n')
print('Notation review extended through 076; transcription bytes unchanged.')
