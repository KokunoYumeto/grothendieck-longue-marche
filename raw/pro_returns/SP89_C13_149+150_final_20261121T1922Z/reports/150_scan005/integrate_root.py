from pathlib import Path
import json

p=Path(__file__).with_name('report.json')
r=json.loads(p.read_text())
assert not r.get('main_reviewed')
for n in r['notes']:
    if n['id']=='N02':
        n['text']=n['text'].replace('not a possible standing hypothesis on an unexamined leaf','not the standing continuity hypothesis explicitly visible on the preceding scan004, which the main reader has checked')
    if n['id']=='N08':
        n['text']+=' The main reader separately checked the preceding leaf’s definitions of conditions1,2,3 bis; see N12 below.'
r['notes'].extend([
    {'id':'N12','text':'Main-reader check against scan004: its final 3 bis condition says the cumulative X_i are nonempty. Conditions1 and2 together with that condition do not imply the order-reflecting faithfulness asserted here. On the two-element chain0<1 take the one-point space X and X_0=X_1=X. These closed pieces are increasing and cover X, their intersection equals the union over common predecessors for each pair, and both are nonempty; nevertheless X_1 subset X_0 while1 is not <=0. Thus the stated implication fails under the transcribed definitions. Nonempty strata (condition3) would imply faithfulness by the disjoint-strata argument, but the written3 bis is retained. This check neither changes the source nor claims the author intended an emendation.'},
    {'id':'N13','text':'Main-reader strengthening of the local boundary check: for closed F and arbitrary A, F union A is closed if and only if closure(A) minus A is contained in F. Indeed closure(F union A)=F union closure(A). With F=X_{J_0} and A=X_j-star this checks the local boundary equivalence, subject to the displayed closedness of F. It does not prove the full concluding three-condition equivalence or remove the source’s finiteness hypotheses.'}
])
r['check_events'].extend([
    {'statement_id':'150_scan005.N06','type':'targeted proof check','outcome':'Main reader checked the stated down-set proof: the chosen principal down-set intersects J nonclosed, hence contains J; applying the same premise to any other offending j-prime contradicts antisymmetry. The finite enumeration remains the first reader’s separately recorded computation.'},
    {'statement_id':'150_scan005.N12','type':'refuted, with refined id','outcome':'Main reader checked all conditions in the explicit two-element-chain/one-point-space counterexample against scan004. The 1+2+3 bis faithfulness implication fails; the diagnostic valid stronger premise uses nonempty strata (condition3), without emending the source.'},
    {'statement_id':'150_scan005.N13','type':'targeted proof check','outcome':'Main reader proved the closed-union boundary criterion by distributing closure over a finite union.'}
])
for e in r['check_events']:
    if e['statement_id']=='150_scan005.N08' and e['type']=='carried as background without fault found':
        e['outcome']='The full concluding three-condition equivalence and the restriction-stability claims are carried without a full verification claim. The distinct faithfulness implication is checked and refuted under the preceding page’s definitions in N12.'
r['notation'].append({'form':r'\unsure{}','meaning':'Present unreadable mathematical ink with no recoverable candidate; an adjacent TeX comment identifies the location and cancellation state. Empty payload does not mean blank or absent ink.','evidence':'150_scan005 P18, crossed token after the inner equals.'})
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
