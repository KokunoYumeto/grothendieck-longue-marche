from pathlib import Path
import csv,json,hashlib
from datetime import datetime,timezone
R=Path(__file__).resolve().parents[1];p='148_scan069'
assert hashlib.sha256((R/'second'/f'{p}_second.tsv').read_bytes()).hexdigest()=='d1d420cbb7476ce00904a46b5b89d54a14199d627f61377df975d6678309a422'
C={x['box']:x for x in json.loads((R/'second'/f'{p}_comparison.json').read_text())}
old=C['B01']['first'];new=old
repl={r'at (859,349) {$\unsure{\infty}$}':r'at (859,349) {$\unsure{\infty|0}$}',r'at (989,335) {$\unsure{\infty}$}':r'at (989,335) {$\unsure{0|\infty}$}',r'at (980,501) {$\unsure{1}$}':r'at (980,501) {$\unsure{1|\infty}$}'}
for a,b in repl.items():
 assert a in new,a
 new=new.replace(a,b)
pp=R/'pages'/f'{p}.tex';s=pp.read_text();assert old in s;s=s.replace(old,new);pp.write_text(s)
E1='The complete graph crop was viewed through its pixel-identical lossless WebP, then the existing upper, left and inner label details were examined. Sixteen vertices, ten rays, the grey g--h edge and six black rightward turns are visible. The first filled-outline tracing preserves the irregular red ink and pen gaps more closely than the simplified second paths and is retained. At a, the pale two-lobed trace is crossed by a graph line, so infinity remains leading with 0 possible. At b, the darkest upper trace is a single closed oblique oval; the lower grey trace merges with the graph, making 0 the better leading reading while infinity remains possible. At d, both low loop-like remnants are crossed by other ink, so the first doubtful infinity remains unresolved despite the second reader certainty. At e, the short capped slant favours 1, but crossing strokes prevent excluding infinity. No proper colouring is assumed. Other individual labels agree. Geometry coding and wrappers alone are not additional witness errors.'
E2='The complete folio crop shows the descending bowl of 6 followed by two joined loops of 8: 68. The page-number macro versus bare digits is only markup.'
D={'B01':dict(choice='reading',reading=new,viewed=True,evidence=E1),'B02':dict(choice='keep_first',viewed=True,evidence=E2)}
(R/'second'/f'{p}_main_decisions.json').write_text(json.dumps(D,ensure_ascii=False,indent=2)+'\n')
rp=R/'records'/f'{p}.json';r=json.loads(rp.read_text())
q=r['changes'][4]
for a,b in repl.items():q['final']=q['final'].replace(a,b)
q['evidence']=q['evidence'].replace('two upper doubtful infinity forms','two upper doubtful labels').replace('All sixteen label values were read separately; the four obscured values remain doubtful.','All sixteen label values were read separately; four obscured values remain doubtful, with b now leading 0 and the local alternatives recorded individually. This row counts placement, not the separate value correction at b.')
r['changes'].append(dict(id=p+'-07',place='Upper vertex label b at (989,335)',c=r'\unsure{\infty}',h='No individual vertex-label mapping supplied',final=r'\unsure{0|\infty}',diff_c=True,diff_h=True,kind='misread symbol or index',error_kind='Symbols and indices',evidence='A dark oblique single oval is visible in the upper part of the small red loop. The grey mark beneath is entangled with the crossing graph lines and does not securely complete a second lobe. The independent reader also leads with 0. The final reading therefore leads with 0 but retains infinity as an alternative; the graph colouring does not settle it.',crop=f'crops/{p}_upper_labels.png',box=[825,285,1040,409],confidence='low',marked_in_h=False,consequential=True))
dr=[(r'\unsure{\infty|0}','0','The pale vertical two-loop form is crossed by a graph edge; infinity remains leading but a single loop cannot be excluded.'),(r'\unsure{0|\infty}',r'\infty','The darkest upper part is a single closed oval; the lower grey trace is inseparable from the graph, so 0 leads without resolving the mark.'),(r'\unsure{\infty}','No secure alternative','Low oblique loop remnants suggest infinity, but the right lobe merges with red and grey strokes; the independent confident reading does not settle the complete form.'),(r'\unsure{1|\infty}',r'\infty','The short capped slant favours 1; crossing graph strokes prevent excluding the independent infinity reading.')]
for x,(reading,alt,reason) in zip(r['doubts'],dr):x.update(reading=reading,alternatives=alt,reason=reason)
for x,(reading,alt,reason) in zip(r['decisions'],dr):x.update(decision='undecided',reading=reading,evidence=reason)
r['notes'][2]['text']='No proper 0/1/infinity colouring is assumed. Four labels remain obscured. The independent audit changes the leading reading at b from infinity to 0, adds 0 as an alternative at a and infinity as an alternative at e, and retains the doubtful infinity at d. These decisions follow the surviving individual strokes; the leaf gives no colouring rule that can resolve them.'
r['notes'].append(dict(id=p+'-N-audit',text='The blind second reading was frozen before comparison. Both unequal boxes were viewed by the main reader. The detailed first geometric tracing is retained: the second approximation omits the visible g--h edge and represents only four of the six black turns. Label alternatives were adjudicated on existing tight crops. The 68 folio agrees. No new mathematical assertion is inferred from the drawing.'))
extra=[f'crops/{p}_{z}.png' for z in ['upper_labels','left_label','inner_labels']]
r['second_main_review']=dict(viewed_boxes=['B01','B02'],reviewed_at=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),decisions=f'second/{p}_main_decisions.json',additional_existing_crops_viewed=extra,lossless_display_path=f'transport/{p}_second_B01.webp')
r['main_reader_crops']=list(dict.fromkeys(r.get('main_reader_crops',[])+extra))
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
