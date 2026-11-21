from pathlib import Path
import csv,json,hashlib
from datetime import datetime,timezone
R=Path(__file__).resolve().parents[1];p='148_scan072'
assert hashlib.sha256((R/'second'/f'{p}_second.tsv').read_bytes()).hexdigest()=='3fd47736b2739d0bd5b8fb3cdb3509295606663bd931912e04cad2a6ae65622b'
C={x['box']:x for x in json.loads((R/'second'/f'{p}_comparison.json').read_text())}
a=r'\boldsymbol{15}';b=r'\unsure{\boldsymbol{15}|\boldsymbol{25}}'
old=C['B01']['first'];assert a in old;new=old.replace(a,b)
pp=R/'pages'/f'{p}.tex';s=pp.read_text();assert old in s;pp.write_text(s.replace(old,new))
E1='The complete two-drawing crop was viewed through its verified lossless WebP, followed by the existing caption and number details. The first detailed red outline preserves the irregular local openings and retraced lines and is retained rather than the simplified continuous second paths. Both drawings have the same finite endpoint incidence; the first preserves the two visible c--f pencil traces. The isolated short curved mark in the left drawing remains doubtful as 1, rather than acquiring a definite numerical role. The caption ending -esque is clear but the joined low arches after lo still do not settle one n versus two. All 23 numeric labels of the right graph were inspected. The retraced first digit of the left heavy two-digit weight has an angled cap, upright and low foot favouring 1, but the thick upper mass admits the independent 2 reading: 15 remains leading with 25 added as a doubt. The separate heavy 1 below the upper vertex has a straight stem and a long foot; its value is retained, with the adjacent looped 9 separately placed. The small enclosures around 1,2,3 and the loop at the lower-right vertex remain in their observed positions. No numerical compatibility rule determines a weight.'
E2='The folio crop shows 71, with a crossed descending 7 and angled cap on the following upright 1. The mspage and margin wrappers differ only in markup.'
D={'B01':dict(choice='reading',reading=new,viewed=True,evidence=E1),'B02':dict(choice='keep_first',viewed=True,evidence=E2)}
(R/'second'/f'{p}_main_decisions.json').write_text(json.dumps(D,ensure_ascii=False,indent=2)+'\n')
rp=R/'records'/f'{p}.json';r=json.loads(rp.read_text())
for x in r['changes']:
 x['final']=x['final'].replace(a,b)
 if x['id'].endswith('-05'):
  x['evidence']+=' The independent audit leaves the retraced weight at the left vertex doubtful as 15/25; its leading value remains 15. This added uncertainty is not another witness-change row.'
  x['confidence']='medium'
r['doubts'].append(dict(place='Right graph, heavy two-digit weight beside the left upper vertex',reading=b,alternatives='25',confidence='low',reason='The heavily retraced first digit has an angled cap and low foot favouring 1, but its upper mass also admits 2. The second digit has the clear top bar and lower bowl of 5. No graph-weight rule is imposed.'))
r['notes'].append(dict(id=p+'-N-audit',text='The blind second reading was frozen before comparison. Both unequal boxes were viewed. Detailed first geometry and the single/double n caption doubt are retained. The two-digit weight previously set confidently as 15 now retains 25 as an alternative after comparison with the independent reading; its first digit remains unresolved. This certainty change does not increase material witness-change counts. The nearby upper-vertex 1 and 9 are still separate annotations.'))
extra=[f'crops/{p}_second_B01_{n}.png' for n in ['caption','numbers']]
r['second_main_review']=dict(viewed_boxes=['B01','B02'],reviewed_at=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),decisions=f'second/{p}_main_decisions.json',additional_existing_crops_viewed=extra,lossless_display_path=f'transport/{p}_second_B01.webp')
r['main_reader_crops']=list(dict.fromkeys(r.get('main_reader_crops',[])+extra))
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
