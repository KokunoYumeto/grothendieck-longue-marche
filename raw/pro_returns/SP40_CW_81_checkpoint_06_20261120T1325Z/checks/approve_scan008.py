from pathlib import Path
from datetime import datetime,timezone
import json
R=Path(__file__).resolve().parents[1]
r=json.loads((R/'checks/scan008_record_draft.json').read_text())
r['main_adjudicated']=True;r['main_approved_utc']=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
r['draft_status']='Approved by root after personal crop adjudication and source/record reconciliation.'
r['approval_followups']=[]
for d in r['decisions']:
 d['main_approval_pending']=False
 d['evidence']=d['evidence'].replace('Root supplied decision: ','Root crop inspection: ').replace('Root supplied decision ','Root crop inspection ').replace('root-supplied','root-approved')
 if d['id']=='008-11':d['crop']='readers/008/C/05_lower_alors_and_pale.png; readers/008/A/10_right_note.png'
 if d['id']=='008-19':d['final']=r'\unsure{/} immediately above and left of l’ensemble; role, hand and attachment unresolved.'
dec={d['id']:d for d in r['decisions']}
for d in r['doubts']:
 # Exact source reports and report-row provenance remain in full. The former crop-only
 # join also included neighbouring doubt rows; use explicit local mappings below.
 d.pop('source_doubts',None)
 d['crop']=dec[d['decision_id']]['crop']
 d['reason']=dec[d['decision_id']]['evidence']
 if d['decision_id']=='008-19':d['reading']=r'\unsure{/}'
exact_locs={
 '008-02':{'A':'First isolated struck line','B':'Isolated struck donc si line','C':'Upper isolated cancelled line'},
 '008-05':{'A':'Second existential line: second letter','B':'Second existential letter','C':'Second existential line, after the second existential sign'},
 '008-07':{'A':'Cancelled subscript under a prime','B':'Cancelled subscript below a-prime','C':'Coprimality chain, small lower-right patch under a prime'},
 '008-09':{'A':'Cancelled word before on a','C':'Below ruled hypothesis, cancellation before on a'},
 '008-10':{'A':'Pale equation after on a','B':'Pale primed letter after p=q','C':'Pale addition after on a, letter carrying the prime'},
 '008-12':{'A':'Cancelled p-like entry before lower q squared','B':'Cancelled predecessor before lower q squared','C':'First lower implication, cancelled item before q squared'},
 '008-06':{'B':'Detached mark above a in et si a=a0 a-double-prime'},
 '008-16':{'C':'Faint interline area to right of the first lower cancelled ending'},
 '008-19':{'A':"Detached stroke upper-left of l'ensemble"}}
reports={x:json.loads((R/f'readers/008/{x}/report.json').read_text()) for x in 'ABC'}
for d in r['doubts']:
 d['source_doubts']=[]
 for role,loc in exact_locs.get(d['decision_id'],{}).items():
  hits=[z for z in reports[role]['doubts'] if z['location']==loc]
  if len(hits)==1:d['source_doubts'].append({'reader':role,'doubt_exact':hits[0]})
  else:d.setdefault('source_doubt_mapping_note',[]).append(f'{role}: source preserved in complete report; no exact location match for {loc}')
alt={'008-02':[r'p\ne q'],'008-05':[r'\delta'],'008-07':['unrecovered cancelled subscript'],'008-09':['word obscured by cancellation'],'008-10':[r"\alpha'"],'008-12':['p without recovered exponent'],'008-06':[r'\prime'],'008-16':['source and former identity unresolved'],'008-19':['attachment to l unresolved'],'008-21':['source and identity unresolved']}
for d in r['doubts']:d['alternatives']=alt[d['decision_id']]
for i in r['inventory']:
 if i['element']=='008.I.11':i['hand']='undetermined hand'
 replacements={'De meme':'De même','desormais':'désormais','hypothese':'hypothése','sous reserve':'sous réserve','peut-etre':'peut-être','mis a part':'mis à part'}
 for a,b in replacements.items():i['first_words_or_objects']=i['first_words_or_objects'].replace(a,b)
r['check_events'][-1]['who']='GPT-6 Astra Pro; effort inherited, separately verifiable setting not exposed; run /root/scan008_b'
r['check_events'][-1]['type']='computation or formal certificate'
r['check_events'][-1]['outcome']='Manual exact arithmetic substitution reported by reader B: '+r['check_events'][-1]['outcome']
r['check_events'][-1]['outcome']+=' The written assignments evaluate the two integer expressions at q=2,a0=b0=1,gamma=1,a=3,b=4,c=5; no exact event time was reported.'
r['notes']=r'''The page continues the handwritten divisibility calculation in another unnamed hand. It applies the displayed binomial bracket to prime divisors of b′, writes p=q in the upper chain, and records α′=qα in the following sentence. It then writes the decompositions b′=q^γ b₀^q and a′=q^ζ a₀^q. The initial ζ retains δ as an alternative. The two assertions about b₀ with b″ and a₀ with a″ each end with the writer’s question mark. The bowl with its separate lower1 is retained. The pale marginal addition reads q∤b₀.

The writer marks an assumption with “Je suppose désormais que ζ=0” and writes c=b+a₀^q=a+q^γb₀^q. The right-hand example supplies q=2, a₀=b₀=1, γ=1, b=4, a=3, c=5. Its open-right frame meets the upper long rule. Between the rules the writer introduces “Je fais l’hypothése suivante” and the coefficient divisibility statement. The lower work contains two cancelled continuations and the pale addition “absurde car q∤a” above the second one. The final equality has a cancelled lower q with the separately raised qα−1, followed by “sous réserve que l’hypothése est vraie”. The relative positions and cancellation paths are reproduced; no algebraic attachment or chronology is supplied. The right note begins “C’est peut-être interessant” and discusses the place of2 among prime numbers. The two acute spellings hypothése and unaccented interessant remain unchanged.

Seven actual C-doubt loci were inspected: the final cancelled q and raised entry are resolved; the isolated p≠1/p≠q, ζ/δ, cancelled lower0, cancelled alors, cancelled p²/p, and pale primed a/α remain qualified. The original notation and retained-spelling rows contribute no extra doubt count. Root’s crop decides Car with a tall initial capital, the insertion triangle, the shared frame/rule connection, the mark above a, and the cancellation/arrow geometry. The alleged extra comma below pale p=q occupies the same source coordinates as the apostrophe of C’est and is represented once. Detached marks and residual shapes are retained with unsettled roles and hand attribution.

Mathematical checks did not select an ink candidate. Three concrete root computations, executed at11:25:04UTC, are documented with their exact substitution and coefficient-reduction maps in checks/scan008_polynomials.md. The internal coefficient rows for q=2,3,5,7 reduce to0 modulo the respective q. The bracket calculation under B→qV and reduction modulo q² gives residual2V at q=2, and0 at each of q=3,5,7. The marginal assignments give c=4+1=3+2=5 and the two listed gcd values1. These results concern the four stated values and the single written example. Reader B separately performed the example’s arithmetic substitution; its exact event time is unrecorded, and the event is dated2026-11-20. A and C-reader reported no mathematical checks. No general proof of the writer’s claims was performed.

No title or manuscript date appears in the independent returns. The lower-left archive numeral7 is retained only as a comment. H supplies no text, so this page has no H collation rows. All original reports and source-row mappings remain preserved.'''
r['workflow_note']='Three fresh independent readers viewed the whole image once and each half once; A/B/C made11/15/10 local crops. Root compared every return and personally viewed15 crops, comprising3 new root crops and12 existing reader crops, with no whole/half view. All reader disagreements and proposed witness differences were adjudicated. One actual C doubt is resolved and six remain. The final-q resolution/geometry is counted once under008-17; the extra lower comma proposal maps to the C’est apostrophe and is not added. All three reader compiler attempts stopped for unavailable format files; no successful compile or render check occurred. Root used structural validation only and v08 prohibits further compiler invocations. Mechanical draft assembly viewed no images and performed no mathematics. Root reconciled its source-doubt links by exact local identity because a shared crop can contain several independent loci. The B report/final-message completion-time discrepancy is disclosed, and neither supplies an invented arithmetic event time. Main crop03 clips part of the lower-right lower rule; the complete agreed feature is attested by the three half audits.'
r['root_page_text_exact']=(R/'pages'/r['filename']).read_text()
(R/'records/scan008.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
print({'decisions':len(r['decisions']),'C':sum(d['diff_C'] for d in r['decisions']),'H':sum(d['diff_H'] for d in r['decisions']),'inventory':len(r['inventory']),'doubts':len(r['doubts']),'events':len(r['check_events'])})
