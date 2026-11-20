from pathlib import Path
import json,datetime
O=Path(__file__).resolve().parents[1];r=[json.loads((O/f'readers/R{i}/scan027.json').read_text()) for i in (1,2,3)]
t=(O/'readers/R2/scan027.tex').read_text()
t=t.replace(r'\deleted{Alors $F$}',r'\deleted{\unsure{Alors} $F$}').replace(r'\deleted{\uline{\unsure{toute}}}',r'\deleted{\uline{toute}}').replace(r'\inserted{figure}',r'\inserted{\unsure{fig.|figure|ferm.}}').replace(r'\unsure{tautologiq\(^t\)|topologiq\(^t\)}',r'\unsure{tautologiq\(^t\)|topologiq\(^t\)|de tte façon}')
fn='J156-5-04_156-5_scan027.tex';(O/'pages'/fn).write_text(t)
m1={1:1,2:2,3:18,4:19,5:3,6:20,7:4,8:5,9:6,10:21,11:22,15:24,16:9,17:25,18:26,19:11,20:28,21:12,22:29,24:30,25:31,26:13,27:14,28:15,30:32,31:16,32:17}
m3={1:1,2:2,3:3,4:4,5:5,6:5,7:6,8:7,9:8,10:8,11:9,14:10,15:11,16:12,17:13,18:14,19:15,20:16,21:17,22:18,23:19,24:20,25:21,26:22,27:23,28:24,29:30,30:25,31:26,32:27}
finals={1:r'\unsure{Alors}',7:r'\deleted{\uline{toute}}',9:r'\inserted{\unsure{fig.|figure|ferm.}}',31:r'\unsure{tautologiq\(^t\)|topologiq\(^t\)|de tte façon}'}
cc={1,2,3,7,8,9,14,18,21,24,27,28,31,32}
hh={3,4,6,7,8,9,10,11,14,15,16,17,18,19,20,21,22,23,24,25,26,29,30,31,32}
rows=[]
for i,x in enumerate(r[1]['differences'],1):
 if i in (12,13):continue
 cr='top' if i<=4 else 'argument' if i<=14 else 'gloss' if i==15 else 'proof' if i<=18 else 'bottom'
 if i==9:cr='figure'
 if i==16:cr='deletedformula'
 if i==24:cr='with'
 if i==31:cr='C7_word'
 if i==32:cr='C8'
 y={'id':f'027-{i:02}','place':x['place'],'C':x['C'],'H':x['H'],'final':finals.get(i,x['reading']),'ink':x['ink'],'crop':f'Main crop crops/root/027_{cr}.png; recipe in documentation/crops.jsonl.','confidence':x['confidence'],'kind':x['kind'],'against_C':i in cc,'against_H':i in hh,'marked_in_H':'yes' if '\\ill' in x['H'] or '\\uncertain' in x['H'] else 'no'}
 y['readers']=[r[0]['differences'][m1[i]-1]['reading'] if i in m1 else x['reading'],x['reading'],r[2]['differences'][m3[i]-1]['reading'] if i in m3 else x['reading']]
 if i==1:y['ink']+=' Main sees the l of Alors but retains uncertainty beneath the crossing line; Ainsi is not supported by that tall medial stem.';y['confidence']='medium'
 if i==3:y['ink']+=' Main keeps R2’s calligraphic/plain distinction uncertain: this live F has a sweeping leftward top unlike the short straight top of the cancelled F above. H’s J is excluded by the middle arm.'
 if i==5:y['readers'][2]='Il'
 if i==6:y['readers'][2]='faudra'
 if i==7:y['ink']+=' Main resolves toute from both t stems and final e under the cancellation, matching R1/R3.';y['confidence']='high'
 if i==9:y['ink']+=' Main does not resolve the full ending: the short f/i/g group runs directly into a long tail. The abbreviated fig. is placed first, with figure and ferm. retained; R2 alone writes figure without doubt.';y['confidence']='low'
 if i==14:y['C']=r'donc \unsure{OK|on} est \unsure{ramené} à ceci.';y['readers'][0]=y['final'];y['ink']+=' Main retains on/OK ambiguity but sees the continuous r-a-m-en-é run; this row also adjudicates the two C doubts separately reported as reader loci 12 and 13.'
 if i==15:y['consequential']='The gloss says H comp. à G (compatibility), not H’s H raffine G; changing the word changes the stated definition of disjointness.'
 if i==19:y['final']=r'\deleted{\uline{Famille \unsure{intersection|intersections}}}'
 if i==24:y['ink']+=' Main retains R2’s added doubt: the reduced low group has too few separable strokes to exclude ou, although avec remains the leading reading.'
 if i==31:y['ink']+=' Main inspected the isolated fourfold crop: the g-like descender and final short q/t group favour a contracted -logiq^t word. No early p descender is clear, so tautologiq^t is first. The separated de tte façon remains possible, following R1/R3; tantôt infra/itou do not account for the visible g-like loop. None is silently expanded.'
 if i==32:y['ink']+=' Main favours a double-loop 8 but cannot exclude crossed ∅/φ; all readers see the separate small low oval. It is preserved as subscript 0.'
 if i in {1,2,3,5,7,8,9,14,16,18,19,21,24,26,27,28,31,32}:y['review_type']='C doubt reviewed' if i not in (3,24) else 'new in-place doubt'
 if y['kind']=='deletion state':y['kind']='deletion state (struck given live or live given struck)'
 rows.append(y)
for id,place,C,H,cr in [('33','NB displayed conclusion','F=G','F=G.','NB'),('34','C5 support equation final punctuation',r'|H|\cap|H\prime|=\varnothing',r'|H|\cap|H\prime|=\emptyset.','bottom')]:
 rows.append({'id':'027-'+id,'place':place,'C':C,'H':H,'readers':[C]*3,'final':C,'ink':'No separate full stop is visible after the final formula; all three submitted page files omit it.','crop':f'crops/root/027_{cr}.png','confidence':'high','kind':'other','against_C':False,'against_H':True,'marked_in_H':'no'})
dds=[('top cancelled word','Alors','','medium','Medial tall l supports Alors; cancellation still obscures the run.'),('opening live collection letter',r'\mathcal F','F','medium','Long sweeping top arm; plain F remains possible.'),('argument first word','Il','','medium','Two heavily retraced stems.'),('interlinear word above non vide','fig.','figure; ferm.','low','Short f/i/g group with a long tail; full word is not assured.'),('before est ramené','on','OK','low','Closed initial loop and retraced tall/humped final group.'),('cancelled small formula',r'i.e. R_G |H|','','low','Thin double strike obscures the punctuated group and alphabet.'),('cancelled heading','intersection','intersections','low','Zigzag obscures the last letter.'),('C5 connective','avec','ou','low','Few separable strokes in reduced low group.'),('C6 cancelled initial','R','S','low','Overwritten loop and shaft.'),('C7 ending',r'tautologiq\(^t\)',r'topologiq\(^t\); de tte façon','low','Unresolved word/phrase; final abbreviated group and initial strokes are reduced.'),('bottom axiom label',r'C8_0',r'C\varphi_0; C\varnothing_0','low','Central glyph retraced and underline clipped; low zero distinct.')]
doubts=[dict(zip(['place','reading','alternatives','confidence','reason'],x)) for x in dds]
now=datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds').replace('+00:00','Z')
checks=[]
for i,dd in enumerate(r,1):
 for e in dd.get('checks',dd.get('mathematical_checks',dd.get('check_events',[]))):
  e=dict(e);e.setdefault('date',dd['end_utc']);e.setdefault('who',f'GPT-6 Astra Pro; R{i}; inherited effort not exposed; SP34 second pass');checks.append(e)
notes='[TXT027-order] Manuscript page 26 says refinement and subdivision determine each other given the subfigure order. It asks “Peut-on de = exprimer ≤ en termes de ≪ et de ≼ ?”; the margin contains “??”.\n\n[TXT027-NB] The NB states F≤G and F≼G imply F=G. The next sentence is “Il faudra que ceci soit vrai”, with toute cancelled before contrée. The argument posits a nonempty H disjoint from F refining G when F<G; C5 would then transfer disjointness from F to G, leading to H empty. The existence assertion for H is not proved here. The readers checked this conditional reduction only, with the factorization and interpretation of disjointness as assumptions. The handwritten gloss says H comp. à G; H’s raffine changes its meaning and is rejected on the visible c-o-m-p abbreviation.\n\n[TXT027-axioms] C5 is called trivial and justified by equal supports; the set-theoretic equality-of-intersections step was checked. C6 says “on la verra tantôt”. C7 says “on le vérifiera” with an unresolved contracted ending; the isolated enlargement favours tautologiq^t / topologiq^t but does not exclude de tte façon. The final label is not secure as plain C8: it has a distinct low zero. The cancelled heading reads Famille intersection(s). No date, title sheet, or page-count statement is present; handwritten page number 26.'
d={'scan':27,'folder':'J156-5-04','filename':fn,'manuscript':'26','overview':'Whole and both halves read; opening cancellation, interlinear words and formula, gloss, cancelled heading and bottom axiom line enlarged. All 17 inherited C doubt occurrences are adjudicated below; two additional uncertainties concern the live collection alphabet and avec/ou.','rows':rows,'inventory':r[2]['inventory'],'doubts':doubts,'unresolved':[x['place']+': '+x['reading']+(' | '+x['alternatives'] if x['alternatives'] else '') for x in doubts],'notes':notes,'checks':checks,'notation':[{'sign':r'\mathcal F / F','form':'Live collection F has a long sweeping top; ordinary figure F has short rightward arms.','evidence':'027_top: live line 2 versus cancelled line.','ambiguity':'First live occurrence marked calligraphic/plain; H’s J excluded by middle arm.'},{'sign':r'\varnothing_F','form':'Slashed oval with low F; ordinary slashed oval in subsequent conclusion.','evidence':'027_gloss and 027_proof.','ambiguity':''},{'sign':'contrée / contrées','form':'Single t stem, no x or g, acute/reduced ée ending.','evidence':'027_argument and 027_bottom.','ambiguity':''},{'sign':'bottom axiom label','form':'C, double-loop or crossed central glyph, distinct low oval.','evidence':'027_C8 at 4×.','ambiguity':r'C8_0 / C\varphi_0 / C\varnothing_0.'}],'abbreviations':{'NB':'nota bene','comp. à':'compatible à / avec','ssi':'si et seulement si','dis. / disj.':'disjointe','Ext.':'Extension','fig.':'figure (uncertain insertion)','tautologiqᵗ / topologiqᵗ':'tautologiquement / topologiquement (uncertain reading and contraction)'}}
(O/'decisions/scan027.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
with (O/'progress.log').open('a') as f:f.write('scan 027 done '+now+'\n')
p=O/'documentation/run.json';s=json.loads(p.read_text());s['completed_scans'].append(27);p.write_text(json.dumps(s,indent=2)+'\n')
