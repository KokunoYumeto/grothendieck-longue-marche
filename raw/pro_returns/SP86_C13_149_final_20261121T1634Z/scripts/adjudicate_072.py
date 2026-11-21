"""Root adjudication of the fixed blind return for scan 072."""
from pathlib import Path
import json
from write_audit_decisions import main
from record_audit import record
from assign_audit import assign
B=Path(__file__).resolve().parents[1];page='149_scan072';rp=B/'reviews'/f'{page}.json'
r=json.loads(rp.read_text());assert not r.get('audit');p=B/'pages'/f'{page}.tex';t=p.read_text()
word=r'relati\unsure{ve}ment';assert t.count('relativement')==1;t=t.replace('relativement',word);p.write_text(t)
ev='The opening r has a descending entry joined into the small e, tall looped l and compressed a. The short crossings remain within those joined bodies; no independent cancellation traverses the opening run. The tall t and separate i dot are visible. The following low bend and tall returning loop are crowded and leave ve tentative, followed by the low m/e/n run and terminal t return. Retain the live word with only that middle pair doubtful. The two separated following marks remain à/colon.'
c={x['id']:x for x in r['changes']};c['P01'].update(final=word,evidence=ev,confidence='medium')
r['doubts'].append(dict(place='line 3, middle of relativement (P01/B01)',reading=word,alternatives='tentative ve; overlapping medial strokes',confidence='medium',reason=ev))
for h in r['hand']:
 if h['form']=='Crowded joins in relativement':h['observation']=ev
r['notes'].append('The independent audit retains the live state of relativement while marking its crowded middle ve as tentative. The first initials OPS remain live: the left narrow closed oval, middle P bowl and final S are separately traceable. The final codimension numeral retains 1 after comparison with the blind 2/1 alternatives. No additional mathematical check was performed during this audit.')
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
D={}
def keep(b,title,e):D[b]=dict(keep_first=True,changed=False,decision=title,evidence=e)
D['B01']=dict(final=word+r' \unsure{à|:}',changed=True,decision='Keep the word live and qualify its crowded middle',evidence=ev)
keep('B03','Retain live en before canceled U','The initial e retains a small closed lower counter and an upper returning entry despite its dark retracing; it joins the shallow n rise and long tail. Both cancellation strokes begin at the later U and cross its lower stems, leaving en to the left of their extent. The uncertainty suggested for e does not remove its visible counter and connecting exit.')
keep('B07','Retain the same dimension numeral','The 1 has a long descending upright and broad transverse base, followed by a separately curved comma. The blind math delimiters surround exactly that same numeral. The low mark between l and t remains a/point; no change is made to its uncertainty or to the surrounding literal dim. rel...tive.')
keep('B08','Retain live OPS, the canceled tentative le and barred m','The crossed word has a tall l loop, while its low e counter is partly hidden by the two strikes, so le remains tentative. The next live group has a narrow closed oval at the left, then an independently descending P stem with an upper right bowl. The final S has its upper loop and lower sloping return at the same baseline as the initial oval. These bodies support O/P/S rather than a subscripted S. The following sign has one upper bar and a lower pointed cup, cusp and flat return, preserving barred m. The large separate T stands at the right.')
keep('B09','Retain the bound and numeral','The relation has two strokes meeting in a rightward angle with a separate lower slanted bar. Both geq and geqslant encodings map to these same three strokes. The following numeral has one short descending upright and the comma is separate. Retain the recorded ≥1.')
keep('B10','Retain the source numeral 1','In the complete codim(Z,S) relation the final digit starts with a short curved entry, descends along one upright and ends in a tiny right hook. It has no return diagonal across the numeral body and no broad lower horizontal foot. The closing parenthesis is independently placed to its right. These local strokes support 1; the ≥ encoding maps to the same angled relation and separate lower bar in both readings. No expected codimension bound is substituted.')
main(dict(page=page,root_viewed=[f'crops/{page}_{b}_second.png' for b in D],decisions=D));record(page);assign('reader_a')
