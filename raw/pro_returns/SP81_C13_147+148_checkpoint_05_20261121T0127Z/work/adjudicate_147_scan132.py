from pathlib import Path
import json
from datetime import datetime, timezone

root=Path(__file__).resolve().parents[1]
page='147_scan132'
p=root/'pages'/f'{page}.tex'
t=p.read_text()
old=r'\uuline{tel que}'
assert old in t
t=t.replace(old,r'tel \uuline{que}')
t=t.replace(r'\unsure{suit|vient}',r'\unsure{suit|vient|fait}')
t=t.replace('normaux, et sans que le remplacement des',r'normaux, et \unsure{sans|disons} que le \unsure{remplacement|morphisme} des')
p.write_text(t)
f=root/'work'/f'{page}_final.json'
r=json.loads(f.read_text())
c=r['changes'][0]
c.update(final=r'tel \uuline{que} $\alpha(0)=0$',differs_C=True,
 evidence='The two parallel underline strokes begin to the right of tel and run below que only; alpha(0)=0 is outside both strokes. Blind audit corrects the earlier extent.',
 crop=page+'_second_B02.png',box=[275,340,1435,452],confidence='high')
c=r['changes'][2]
c['final']=c['final'].replace(r'\unsure{suit|vient}',r'\unsure{suit|vient|fait}')
c['evidence']+=' Blind rereading adds fait as an unresolved candidate: a tall loop and lower crossing strokes survive, but cancellation prevents a letter-by-letter decision. The raised connected group remains doubtful both as a separate insertion and as letters.'
c=r['changes'][16]
c['final']=r'et \unsure{sans|disons} que le \unsure{remplacement|morphisme} des'
c['evidence']+=' Blind audit retains the preferred words but marks the two compressed groups as uncertain; the scan itself cuts the lowest descenders at the sheet edge. Completion crop '+page+'_second_B07_completion.png [315, 2255, 1685, 2363] checks all available ink.'
c['confidence']='low'
for d in r['doubts']:
 if d['place']=='body line 8, cancelled verb':
  d.update(reading=r'\deleted{\unsure{suit|vient|fait}}',alternatives='suit; vient; fait',reason='Tall loop, low joined strokes and crossing cancellation leave all three candidates open; upper strokes may belong to the same word.')
r['doubts'] += [
 dict(place='last line, after et',reading=r'\unsure{sans|disons}',alternatives='sans; disons',confidence='low',reason='A curved initial stroke and compressed horizontal middle survive; no independent i dot securely distinguishes the second candidate.'),
 dict(place='last line, before des',reading=r'\unsure{remplacement|morphisme}',alternatives='remplacement; morphisme',confidence='low',reason='Low initial joined run, one tall middle stroke and long terminal return are visible, but the original scan cuts the lower descenders at its bottom edge.')]
r['notes']+=' Blind audit narrows the double underline to que. It preserves the separately visible marginal word sont, the separate cancelled Pi clusters, and the unheaded lower Pi connector. The last line remains preferred sans ... remplacement with alternatives shown; its completion crop reaches the original scan edge. No mathematical claim was checked during these palaeographic decisions.'
f.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
comp=json.loads((root/'second'/f'{page}_comparison.json').read_text())
ds={x['box']:x for x in comp['differences']}
evidence={
 'B02':('The two parallel underlines start after tel and extend only below que. The letters t-e-l themselves are readable. The whole alpha display and alpha(0)=0 agree.', 'high'),
 'B03':('The joined word reads induit, without a separate se; au begins the next line. A large curved closing parenthesis follows the D-star expression. The connector has only a small terminal upturn, so the original local arrow doubt remains.', 'medium'),
 'B04a':('The repeated aussi agrees with the earlier a/low-middle/dotted-i form on this sheet. Cancellation obscures the preceding verb: a tall loop permits fait as an additional candidate without settling suit/vient. A raised connected group is present, but its independence from the cancelled ascenders remains explicitly doubtful.', 'low'),
 'B04b':('Four Pi objects, two upper tildes, four right/down shafts with heads, and the central 2-cart. are present. The two encodings give the same square; the closing parenthesis is visible.', 'high'),
 'B04c':('After the second plain Pi, the low joined run and terminal upright form the prose word sont, continuing with connus quand on on the next line; they do not supply a separate r-minus-one label. Projections and locales have a visible word break. Two cancelled left d-subscripts occur at different heights, one in et les Pi_d and one on the next diagram object. The lowest shaft begins separately, without a secure source label. Crossed right labels remain doubtful; the live star and exclamation are both raised above D_d. The original arrow doubts and source blank are retained.', 'low'),
 'B04d':('Sur is separately visible at the right under induisent; les starts the next baseline before pi_1. The low loop and tall stems of induisent remain readable despite the crossing marginal strokes.', 'high'),
 'B06':('Both ends of the short horizontal connector are blunt, with no separate arrowhead arm. The four Pi subscripts and the final closing parenthesis agree.', 'high'),
 'B07':('Relations has the expected visible tall l/t sequence. Before hypothèse the short final mark has no tall or descending f-stem, supporting sans. The final line is cut by the original scan edge; completion crop [315,2255,1685,2363] confirms the available ink but does not settle sans/disons or remplacement/morphisme, so both receive local doubt with the original readings first.', 'low')}
choices=[]
for box,d in ds.items():
 final=d['first']
 if box=='B02': final=final.replace(r'\uuline{tel que}',r'tel \uuline{que}')
 if box=='B04a': final=final.replace(r'\unsure{suit|vient}',r'\unsure{suit|vient|fait}')
 if box=='B07': final=final.replace('et sans que le remplacement des',r'et \unsure{sans|disons} que le \unsure{remplacement|morphisme} des')
 item=dict(box=box,choice='literal' if final!=d['first'] else 'first',changed=final!=d['first'],evidence=evidence[box][0],confidence=evidence[box][1])
 if item['choice']=='literal': item['final']=final
 choices.append(item)
(root/'work'/f'{page}_audit_choices.json').write_text(json.dumps(dict(reader='audit_a',choices=choices),ensure_ascii=False,indent=2)+'\n')
stamp=datetime.now(timezone.utc).isoformat()
with (root/'work/root_views.tsv').open('a') as v:
 for b in ds: v.write(f'{stamp}\t{page}_second_{b}.png\troot blind-audit adjudication\n')
 v.write(f'{stamp}\t{page}_second_B07_completion.png\toriginal bottom edge completion\n')
