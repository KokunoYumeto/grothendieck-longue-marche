from pathlib import Path
from datetime import datetime,timezone
import json
root=Path(__file__).resolve().parents[1];page='147_scan133'
rp=root/'work'/f'{page}_final.json';r=json.loads(rp.read_text());pp=root/'pages'/f'{page}.tex';s=pp.read_text()
s=s.replace('trivialité --','trivialité. --').replace('de la théorie de Galois',r'de la \unsure{théorie|Théorie} de Galois');pp.write_text(s)
for c in r['changes']:
 if c['id']==page+'-09':
  c['final']=c['final'].replace('trivialité --','trivialité. --');c['differs_C']=True
  c['evidence']+=' Blind second-reading crop B05 exposes a separate dark dot immediately after trivialité and before the detached dash; the dot is in a punctuation position and matches the adjoining ink. The period is restored.'
  c['crop']=page+'_second_B05.png';c['box']=[300,1038,1668,1358]
r['doubts'].append(dict(place='L10, initial letter of théorie',reading=r'\unsure{théorie|Théorie}',alternatives='théorie; Théorie',confidence='medium',reason='The initial tall joined strokes admit the lower-case preferred reading and the blind reader’s capital. Their precise t/T form remains open in second B05; no lexical expansion is made.'))
r['notes']+='\n\nBlind audit: a separate dark point before the dash after trivialité is restored. The t/T case in théorie is locally marked. The complete phrase after hypothèses was re-inspected in second_B06b_completion [1125,1705,1680,1880], because the first and blind broad crops placed its upper edge too close to the crop boundary. Compressed joins still favor de voisinages, with the original local doubt retained; the terminal return of s’exprimant remains read as t. No mathematical claim was checked by this audit.'
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
evidence={
'B01':('Raised semble y has the exposed tall b/l strokes and separate terminal y; the dark patch is confined to the ending after jouer. The deleted a|ait remains uncertain. The lower small group favors et with a tall crossing; no separate terminal c is securely exposed, so the existing local alternatives and dot remain.','low'),
'B02':('The prose has one deep medial descender and tall crossed stem in systèmes; it does not expose the two p descenders proposed by applications. The right d-zero has a low trailing comma stroke before the dash. The connector has a thickened upper terminal and no clearly separate lower head arm, so the existing head doubt is retained. Both objects and all indices were re-read.','medium'),
'B03':('The compressed ending has a long high loop and terminal crossed upright. The exact run of lower letters remains unresolved; the first reading preserves the raised abbreviated ending with its full-form alternative instead of supplying extra baseline letters.','low'),
'B04':('A detached raised crossed stroke follows the abbreviation point after cepend and precedes examiner. It is preserved as the raised t. The beginning of examiner has its angular x and following joined run; the initial mark before l’occasion remains locally doubtful.','medium'),
'B05':('A dark separate dot stands immediately after trivialité and before the detached dash. It has the same darkness as adjacent letters and a syntactic punctuation position, so a period is added. The joined tall initial strokes of théorie leave t/T case unresolved; its lower-case reading remains first. The question-like mark and terminal dot/dash sequence retain their existing doubts. The other lexical readings remain exposed despite the second reader’s additional caution.','medium'),
'B06a':('The thickened word has a descending q, short joined u and terminal i stroke; qui is retained. The remaining wording agrees apart from the blind uncertainty wrapper.','high'),
'B06b':('The complete upper word was additionally inspected in crops/147_scan133_second_B06b_completion.png [1125,1705,1680,1880] after noticing its edge in both broad crops. Shallow initial joins and the low terminal hooked run continue to favor de voisinages; no independent tall t establishes croisements. The final word ends in a raised returning t-shaped stroke, favoring s’exprimant over the proposed -era ending. Existing doubt on the upper phrase remains.','medium'),
'B06c':('Both readings preserve the same Pi objects, contrast in the parenthesis, and one-half coefficient. The source fraction has a diagonal division stroke. Braces around widetilde and fraction macro choices do not alter this reading.','high')}
comp=json.loads((root/'second'/f'{page}_comparison.json').read_text());choices=[]
for d in comp['differences']:
 box=d['box'];e,conf=evidence[box];x=dict(box=box,choice='first',changed=False,evidence=e,confidence=conf)
 if box=='B05':x.update(choice='literal',changed=True,final=d['first'].replace('trivialité --','trivialité. --').replace('de la théorie',r'de la \unsure{théorie|Théorie}'))
 choices.append(x)
(root/'work'/f'{page}_audit_choices.json').write_text(json.dumps(dict(reader='audit_b',choices=choices),ensure_ascii=False,indent=2)+'\n')
with (root/'work/root_views.tsv').open('a') as f:
 for box in evidence:f.write(datetime.now(timezone.utc).isoformat()+'\t'+page+'_second_'+box+'.png\tRoot blind-difference crop inspection\n')
 f.write(datetime.now(timezone.utc).isoformat()+'\t'+page+'_second_B06b_completion.png\tRoot complete upper phrase after boundary issue\n')
