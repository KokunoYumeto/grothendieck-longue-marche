from pathlib import Path
import csv,json
W=Path(__file__).resolve().parents[1];n=26
base=W/'second'/f'147_scan{n:03d}'
with Path(str(base)+'_comparison.tsv').open() as f:comp={r['box']:r for r in csv.DictReader(f,delimiter='\t')}
p=W/'pages/147_scan026.tex';t=p.read_text()
old=r'\deleted{\unsure{MD}}';new=r'\unsure{\deleted{\unsure{MD}}|M\deleted{\unsure{D}}}'
assert old in t
t=t.replace(old,new).replace(r'\mathcal M','M').replace(r'\mathcal{M}','M');p.write_text(t)
rp=W/'records/147_scan026.json';r=json.loads(rp.read_text())
r['changes'][0]['final']=new+'-graphes';r['changes'][0]['confidence']='medium'
r['changes'][0]['evidence']='The D-shaped right cluster is crossed by diagonal and looping cancellation strokes. The bottom heavy stroke reaches toward the M, but the upper M body remains clear. Root blind review retains cancellation of MD first while explicitly allowing M to remain live; the right letter itself remains tentative. The following hyphen and graphes are live.'
r['changes'][0]['audit']='Fresh audit crop 026-B03 makes the reach of the cancellation onto M uncertain.'
for c in r['changes']:c['final']=c['final'].replace(r'\mathcal M','M').replace(r'\mathcal{M}','M')
r['decisions'][0]['reading']=new;r['decisions'][0]['what the ink shows']=r['changes'][0]['evidence'];r['decisions'][0]['crop']='crops/147_scan026_audit_B03.jpg (275,1080,1125,1220)'
r['doubts'][0].update(reading=new,alternatives='Cancelled MD, or live M followed by cancelled D; the right letter remains tentative.',reason='The cancellation clearly crosses the right cluster, but its reach onto the left M is not certain.')
r['unresolved'][0]='The letters under the cancellation and its reach onto M remain explicitly doubtful.'
for q in r['notation']:
 q['form']=q['form'].replace(r'\mathcal M','M').replace(r'\mathcal{M}','M')
r['audit_note']='The second reading prompted explicit uncertainty about whether the cancellation reaches M in the MD prefix. The intact d and upper e loop still favour only a final cancelled s in the later de(s). The G indices have visible lower return strokes and the first has a separate prime. Plain Latin M is used consistently: both upright and swept-foot forms occur within the same formula, with no separate alphabet indicated. The first/second files preserve their original typefaces.'
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
plan={}
evidence={
'026-B02':('consistent capital M','Both M glyphs have the same two upright peaks and central valley; the variation from curved to straight feet does not establish a second alphabet. The hook at the left and pointed right arrowhead, 26, lower g/nu and terminal stop are visible. Adopt plain M consistently; math delimiters and the second reader\'s edge comment are editorial.'),
'026-B03':('retain first with explicit scope uncertainty',r['changes'][0]['evidence']),
'026-B04':('retain first','The short n and separate high bent b are clear; no dot follows nb. The second reading agrees and adds only an editorial crop-edge comment.'),
'026-B06':('retain first','There is one de group. Its d and upper e loop remain intact, while the thick low cancellation covers the small final sign. Retain de with uncertain cancelled s; no separate second des is visible. The second reading agrees textually and comments on the strike.'),
'026-B07':('retain letters and bar; consistent capital M','Each lower G has a short inward/lower return, distinguishing it from the open inclusion curve; the first G has one detached prime. The long bar covers M and its G index. Plain M is the consistent rendering of this capital; the second reader\'s C alternative and edge comments do not displace these visible strokes.')}
for b,(decision,ev) in evidence.items():
 final=comp[b]['first'].replace(r'\mathcal M','M').replace(r'\mathcal{M}','M')
 if b=='026-B03':final=final.replace(old,new)
 plan[b]={'decision':decision,'evidence':ev,'final_reading':final,'changed':'yes' if final!=comp[b]['first'] else 'no','crop':f'crops/147_scan026_audit_{b.split("-")[1]}.jpg','viewed_by':'root'}
(W/'review/026_reconciliation_plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n')
