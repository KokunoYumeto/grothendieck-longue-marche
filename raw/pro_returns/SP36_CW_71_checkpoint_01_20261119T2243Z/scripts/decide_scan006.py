from pathlib import Path
import json,copy,datetime
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'out';R=OUT/'readers/scan006';A=OUT/'adjudication/scan006'
r={k:json.loads((R/k/'report.json').read_text()) for k in ['R1','R2','R3']}
fs=copy.deepcopy(r['R2']['findings'])
# Main adjudication after comparison of all three complete texts and all reports.
map1={1:1,2:2,3:3,4:4,5:5,6:6,8:7,9:8,10:9,11:10,12:11,13:12,15:15,16:17,17:18,18:16,20:20,21:21,22:22,23:23,24:24,25:25,26:26,27:27,28:28,29:29,30:30,31:31,32:33,33:34,34:32,35:35,36:36,37:38,44:14,45:37}
map3={1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:15,11:16,12:17,13:18,15:19,16:20,17:21,19:23,20:24,21:25,22:27,23:28,24:29,25:30,26:31,27:32,28:33,29:34,30:35,31:36,32:38,33:39,34:37,35:40,36:41,37:43,45:42}
for n,f in enumerate(fs,1):
 f['id']=f'D006-{n:02d}'
 f['readers']={'R1':r['R1']['findings'][map1[n]-1]['reading'] if n in map1 else f['reading'],'R2':f['reading'],'R3':r['R3']['findings'][map3[n]-1]['reading'] if n in map3 else f['reading']}
 f['consequential']=False
# Exact full-reading proposals at places without a separate finding.
fs[6]['readers']['R1']=fs[6]['reading']
for k in ['R1','R3']:
 fs[13]['readers'][k]=r'\draw[->] (.38,.25) to[bend right=12] (0,0);'
 fs[45]['readers'][k]='[omitted]'
fs[43]['readers']['R3']='[second return edge omitted]'
fs[21]['readers']['R3']='par rapport au remplacement de'
fs[16]['readers']['R1']=fs[16]['readers']['R3']='imm fermée'
fs[18]['readers']['R1']=r'$\coprod C_i$ [no period]'
for n in range(38,44):
 for k in ['R1','R3']:fs[n-1]['readers'][k]=fs[n-1]['reading']
# The final page uses R2's complete drawing and loop-headed gloss arrow, with these decisions.
t=(R/'R2/reading.tex').read_text()
t=t.replace(r'\deleted{L\'application naturelle}',r'\deleted{L\'application \unsure{naturelle}}') if False else t.replace("\\deleted{L'application naturelle}","\\deleted{L'application \\unsure{naturelle}}")
t=t.replace(r"\inserted{$U_i'{}^{\unsure{*|\wedge}}=U'_i\cap K^*$}",r"\inserted{$U_i'{}^{\unsure{\wedge|*}}=U'_i\cap K^\wedge$}")
t=t.replace(r"\unsure{K'|\dot K'}",r"\unsure{\dot K'|K'}")
t=t.replace('% slanted\n','% slanted left-margin note, three lines in its own orientation\n')
t=t.replace(r'\draw (0,0) .. controls (-.23,-.96)',r'% The descending divider stops short-left of the lower outer cusp.'+'\n'+r'\draw (0,0) .. controls (-.23,-.96)')
(OUT/'pages/J71-01_71_scan006.tex').write_text(t)

def upd(n,**kw):fs[n-1].update(kw)
def cp(reader,name):return str(R/reader/name)
def main(name):return str(A/(name+'.jpg'))
# All attached crop references below were personally viewed once by the main reader.
used={1:cp('R3','opening.jpg'),2:cp('R3','opening.jpg'),3:cp('R3','opening.jpg'),4:cp('R1','02_de_endings.jpg'),5:cp('R1','02_de_endings.jpg'),6:cp('R2','04_sur.jpg'),7:main('span_diagram'),8:cp('R2','05_cancelled_heading.jpg'),9:cp('R3','cancelled_map.jpg'),10:cp('R3','main_operator.jpg'),11:cp('R2','08_coproduct_suffix.jpg'),12:cp('R2','09_side_formula_gloss.jpg'),13:cp('R2','09_side_formula_gloss.jpg'),14:cp('R2','09_side_formula_gloss.jpg'),15:main('points_and_complement'),16:cp('R1','10_cest_une.jpg'),17:cp('R2','11_imm.jpg'),18:main('points_and_complement'),19:main('map_end'),20:main('invariance_heading'),21:main('invariance_heading'),22:main('replacement_words'),23:cp('R2','12_inserted_superscripts.jpg'),24:main('pourvu'),25:cp('R2','13_slanted_margin.jpg'),26:cp('R2','13_slanted_margin.jpg'),27:cp('R2','13_slanted_margin.jpg'),28:cp('R2','14_replaced_condition.jpg'),29:cp('R2','14_replaced_condition.jpg'),30:cp('R2','15_cancelled_parenthesis.jpg'),31:cp('R2','15_cancelled_parenthesis.jpg'),32:cp('R2','16_sufficient_condition.jpg'),33:cp('R2','16_sufficient_condition.jpg'),34:main('sufficiency_dash'),35:cp('R2','16_sufficient_condition.jpg'),36:main('div_hypotheses'),37:cp('R2','17_page_number.jpg'),44:cp('R1','09_drawing_ticks.jpg'),45:main('vertical_stroke'),46:cp('R2','17_page_number.jpg')}
for n in range(38,44):used[n]=cp('R1','09_drawing_ticks.jpg')
for n,path in used.items():
 upd(n,crop=path)
 fs[n-1]['evidence']=fs[n-1]['evidence'].replace('Half a shows','The main crop confirms').replace('Half b shows','The main crop confirms').replace('Half a ends','The main crop ends').replace('Half b gives','The main crop gives').replace('Half b places','The crop and all three full readings place').replace('Half b has','The main crop has').replace('Half b and the close crop','The main-viewed close crop')+' Main reader inspected the cited crop once and accepts this decision unless qualified here.'
upd(8,reading=r"\deleted{L'application \unsure{naturelle}}",diff_c=False,diff_h=True,unresolved=True,confidence='medium',kind='other',evidence='The strike runs through the low early letters and part of the middle run. Tall t and the final looped l/l/e sequence support naturelle, but the compressed n/a strokes are not independently separable. R2 resolves it; R1/R3 and the main reader retain uncertainty. H gives the word without doubt.')
upd(23,reading=r"\inserted{$U_i'{}^{\unsure{\wedge|*}}=U'_i\cap K^\wedge$}",diff_c=True,diff_h=True,confidence='low',evidence='Both tiny raised marks have a peaked pair of limbs and a short upper spur/retrace, without the distinct multi-ray crossing of the larger stars elsewhere in item 6. The main reader follows R3 in ranking wedge first, but star remains possible. The later unmarked K-wedge inherits precisely the same unresolved status. The line underneath leads into the insertion point; H linearizes it.',consequential=True,consequence='The candidate order of two ambiguous superscripts changes; this is not a correction to the mathematics, and both alternatives remain explicit in the record.')
upd(28,reading=r"\deleted{$\unsure{\dot K'|K'}\subset\bigcup U_i$, et}",diff_c=True,evidence='A thick dark point lies above the original K, at the high part of the opening cancellation stroke; a separate right prime survives. Its local darkening favours a pre-existing dot (R1), but it cannot be detached securely from the cancellation (R2/R3 prefer plain K-prime). The main reader ranks dotted K-prime first with plain K-prime retained.',confidence='low',unresolved=True)
upd(30,confidence='medium',evidence='The main crop shows a thick horizontal raised stroke just beyond the closing parenthesis. Thinner slanting cancellation lines cross the surrounding region, but this short heavy bar has its own horizontal track. The main reader follows R2 in resolving the raised minus; R1/R3 retained uncertainty. No mathematical meaning is inferred from this recovery.')
upd(33,consequential=True,consequence='C’s live prose soit is replaced by the written interior operator int, so the sufficient condition refers to int K-prime containing the union of C_i. All three readers and the main crop support int from the dotted i, low n and final tall t; sufficiency itself is not proved.')
upd(21,consequential=True,consequence='H’s immersion is corrected to the written invariance. The page proposes invariance under replacement of K and explicitly asks to verify the precise statement.')
upd(29,consequential=True,consequence='The inserted condition contains an unindexed union of U_i; H omits the union sign.')
upd(31,consequential=True,consequence='H’s equals V_i is the handwritten universal quantifier followed by i, introducing the condition for every i.')
# Add the actual H drawing's closed lower join, observed separately by R3 and confirmed in its crop.
gap=copy.deepcopy(r['R3']['findings'][13]);gap.update(id='D006-47',readers={k:r'\draw (0,0) .. controls (-.23,-.96) and (-.51,-2.12) .. (-.75,-2.78);' for k in ['R1','R2','R3']},crop=cp('R3','drawing_cusp.jpg'),evidence='The descending interior line ends to the left of the outer cusp, leaving a narrow white gap. All three complete readings retain C’s separated endpoint; R3 explicitly noted H’s connected path, and the main crop confirms the gap.',consequential=False)
fs.append(gap)
# Keep remaining uncertainty by distinct local group, not by repetition count.
ds=copy.deepcopy(r['R2']['doubts'])
ds.insert(3,copy.deepcopy(r['R3']['doubts'][3]))
for q in ds:
 if 'small raised marks' in q['place']:
  q.update(reading=r"U_i'{}^{\unsure{\wedge|*}}=U'_i\cap K^\wedge",alternatives='star for both small raised marks',confidence='low',reason='Peaked limbs with short extra strokes favour wedge; lack of clear crossing rays does not rule out a compressed star. Later unmarked repetition is equally unresolved.')
 if 'Original cancelled' in q['place']:
  q.update(reading=r"\unsure{\dot K'|K'}",alternatives="K'",reason='Dark point above K favours a dot but lies on the cancellation stroke; prime is distinct.')
inv=copy.deepcopy(r['R2']['inventory'])
for i,row in enumerate(inv,1):row['element']=f'006-{i:02d}';row['transcribed']='yes'
inv[13]['first_words_or_objects']='U-prime_i^{wedge|star}=U-prime_i intersect K^{wedge|star}; interlinear insertion'
inv[15]['first_words_or_objects']='dotted K-prime or K-prime subset union U_i, et; cancelled'
notes=[
{'id':'N006-01','text':r'The opening identifies script X as an amalgamated sum of barred W and the disjoint union of barred U_i, over the disjoint union of B_i. A second display identifies it with a coproduct of X_i, with an uncertain parenthesized w/W index; the side display relates an uncertain X_{w/i} to script X_i and Im X_i, glossed as open in script X. The three-lobed sketch has six transverse marks and a narrow return loop. The page does not define the full gluing data, so these assertions were carried without a universal-property proof.'},
{'id':'N006-02','text':r'The map script X to X is stated to be étale away from the coproduct of C_i and an “imm fermée” at its points. The abbreviation is preserved. The prose connective is “c’est une”, not H’s “i.e.”; no local geometric proof is supplied here.'},
{'id':'N006-03','text':r'Item 6 proposes an “Énoncé d’invariance” under replacement of K by K-star, with replacement formulas and edited conditions. The slanted note is “vérifier l’énoncé précis...”. The two tiny superscripts in the interlinear primed-U equation remain wedge/star, with wedge first on visual grounds; larger stars are unchanged. The crossed K condition and crossed K-like group remain uncertain. The live sufficient condition reads int K-prime containing the union of C_i, agreeing with H against C’s soit. The dotted i and final t, not mathematical expectation, decide this word. The unclosed parenthesis and live prime are retained; invariance and sufficiency are not proved.'},
{'id':'N006-04','text':r'The final question is “vérifier si dans les div. hypothèses précédentes, il n’y avait pas lieu d’exiger” union C_i subset int K, followed by the i.e. condition C_i intersect dotted K empty for every i in I. The main reader checked only the conditional set-theoretic equivalence: if K is closed, each C_i lies in K, and dotted K denotes its frontier, then frontier K = K minus int K, hence the two stated conditions are equivalent. This does not establish the missing standing assumptions, the earlier hypotheses, or the proposed invariance. The author’s own page numeral is 5; the separate archive 5 remains a comment.'}]
checks=[]
for key,d in r.items():
 for c in d['checks']:
  checks.append(dict(statement_id=c['statement_id'],date=d['finished_utc'],who=f'GPT-6 Astra Pro; effort inherited, not independently exposed; scan006 {key}',type=c['type'],outcome=c['statement']+' '+c['outcome']))
for n in notes:
 checks.append(dict(statement_id=n['id'],date=datetime.datetime.now(datetime.timezone.utc).isoformat(),who='GPT-6 Astra Pro; effort not independently exposed; main reader',type='carried as background without fault found',outcome='Page-content account from the three readings and adjudicated crops; no proof is asserted by transcription. For N006-04 only the explicit conditional frontier equivalence has a separate targeted event M006-main-frontier-condition.'))
notation=copy.deepcopy(r['R2']['notation'])
notation[8].update(sign='Small raised wedge/star',tex=r"U_i'{}^{\unsure{\wedge|*}};K^\wedge",alternatives='star; repeated K mark remains unresolved even though unmarked.')
notation.append(dict(sign='int before K-prime',tex=r"\operatorname{int}K'",place='sufficiency line after cancelled K-like group',ink='A detached dot above i, low n and final tall t; no initial s or o.',alternatives='C soit rejected'))
d=dict(scan=6,folder='J71-01',their_page=5,hua_has='text',filename='J71-01_71_scan006.tex',brief='briefs/v003_scan006.md',findings=fs,inventory=inv,doubts=ds,notes=notes,checks=checks,notation=notation,abbreviations=r['R2']['abbreviations'],reader_crops={'R1':17,'R2':17,'R3':17},main_new_crops=9,main_reused_crops=18,decided_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),sweep='No S correction row applies to scan 006.')
(OUT/'decisions/scan006.json').write_text(json.dumps(d,ensure_ascii=False,indent=2))
m=json.loads((A/'new_crops.json').read_text())
for c in m:c['viewed_once']=True
(A/'new_crops.json').write_text(json.dumps(m,indent=2))
print('scan006 page and decision written:',len(fs),'findings;',len(ds),'doubt groups;',len(inv),'inventory elements')
