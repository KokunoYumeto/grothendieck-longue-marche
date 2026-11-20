from pathlib import Path
import json,copy,csv
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'out';stem='H97-01_97_scan019'
rs={r:json.loads((OUT/'readers'/stem/r/'report.json').read_text()) for r in ['R1','R2','R3']}
t=(OUT/'readers'/stem/'R3/reading.tex').read_text()
t=t.replace(r'\deleted{\unsure{qu}}',r'\deleted{\unsure{en|qu}}')
for word in ['sans','hyp.','noeth.']:t=t.replace('\\unsure{'+word+'}',word)
t=t.replace(r'\handwritten{\sum}^{\handwritten{\prime}}',r'\handwritten{\sum}^{\handwritten{\unsure{\prime}}}')
ds=copy.deepcopy(rs['R3']['differences'])
for d in ds:
 d['final']=d.pop('reading');d['readers']='R1, R2 and R3: same textual reading/state, apart from equivalent macro spelling.'
 d['marked_in_H']='yes' if '\\ill' in d['H'] or '\\uncertain' in d['H'] else 'no'
 if d['id']=='R3-D02':
  d['final']=r'\unsure{D\prime|D}'
  d['readers']=r'R1: D^{\unsure{\prime}}; R2: \unsure{D^{\prime}|D}; R3: \unsure{D\prime|D}. All retain the same prime/no-prime uncertainty; final explicitly lists both.'
  d['c_changed']=False
 if d['id'] in ['R3-D07','R3-D14']:
  d['final']=r'\deleted{\unsure{en|qu}}';d['c_changed']=True
  d['readers']=r'R1: \unsure{en|qu}; R2: \unsure{qu}; R3: \unsure{qu}. Final adopts R1’s expanded alternatives, still low confidence.'
  d['evidence']='Two covered positions have rounded/upright remnants at the baseline and no exposed q descender. This weakly favours en, but qu remains possible under the cancellation. No confident restoration is made.'
  d['crop']='readers/'+stem+'/R1/crops/'+('05_first_two_deletions.jpg' if d['id']=='R3-D07' else '12_second_qu.jpg')
 if d['id']=='R3-D17':
  d['readers']=r'R1 and R2: live er unmarked, earlier re doubtful; R3: both layers doubtful. Final retains R3’s caution on the overwritten live pair.'
  d['crop']='readers/'+stem+'/R1/crops/14_regulier.jpg'
 if d['id']=='R3-D20':
  d['c_changed']=False;d['crop']='decisions/'+stem+'_crops/bracket.jpg'
  d['evidence']='Main-reader crop shows a thin nearly vertical bracket from beside est un sous-préschéma to beside the concluding Gamma formula; its bottom hooks right and has no arrowhead. The same bracket reading is present in C; the new TikZ coordinates support the corrected note layout.'
 if d['id']=='R3-D21':d['crop']='readers/'+stem+'/R1/crops/15_codim.jpg'
 if d['id']=='R3-D24':
  d['readers']=r'R1 and R3: \illegible{2} \unsure{partie} \illegible{1}; R2: \illegible{4}. Final retains partie solely as a low-confidence candidate, not recovered text.'
  d['crop']='readers/'+stem+'/R1/crops/16_deleted_long_phrase.jpg'
 if d['id']=='R3-D26':d['crop']='decisions/'+stem+'_crops/artinien_stalk.jpg';d['evidence']='Main-reader crop confirms a plain typewriter oval O with a separate short underline and lower Y(D),x; no script lead-in or terminal.'
 if d['id']=='R3-D28':d['crop']='decisions/'+stem+'_crops/zero_stalk.jpg';d['evidence']='Main-reader crop confirms a plain underlined O with lower Y(D),x and an equals sign followed by a typed zero.'
 if d['id']=='R3-D29':
  d['final']=r'\handwritten{\sum}^{\handwritten{\unsure{\prime}}}';d['c_changed']=False;d['confidence']='medium'
  d['readers']=r'R1: doubtful prime/terminal; R2: doubtful prime/terminal; R3: prime without doubt. Final keeps the detached stroke but does not settle prime versus a disconnected terminal.'
  d['evidence']='A short downward-sloping stroke is white-separated from the upper-right end of the summation bar. Its presence is certain; its function as a prime rather than a detached pen terminal is not. Mathematical expectation does not settle it.'
  d['crop']='readers/'+stem+'/R1/crops/18_sum.jpg'
 if d['id']=='R3-D33':d['readers']='R1, R2 and R3: comma outside the deletion. R1 rated the boundary less confidently; main crop confirms the comma lies beyond the terminal cancellation stroke.'
 if d['id']=='R3-D12':d['readers']=r'R1=R2=R3: \unsure{positif|préschéma}; C orders the candidates oppositely. The roughly seven-character width favours positif, with both retained.'

# Replace one compound marginal-note entry by separately identified loci.
old=next(d for d in ds if d['id']=='R3-D19');i=ds.index(old);ds.pop(i)
margin=[
 ('M1','Margin, first word',r'\unsure{devrait}','devrait',r'\unsure{devrait}',False,True,'low','R1=R2=R3: devrait, doubtful. The main reader also leaves the compressed internal strokes unresolved.','Initial tall d and terminal ait-like group are visible; the joined middle is compressed.'),
 ('M2','Margin, verb before dans',r'\unsure{figurer|passer}','figurer',r'\unsure{figurer|passer}',False,True,'low','R1: doubtful figurer, removes passer; R2 and R3: figurer|passer. Final retains both because the long initial loop and compressed middle do not decisively exclude either.','Long looped descender favours figurer, but the middle letter sequence remains merged; no word is promoted to certainty.'),
 ('M3','Margin, staggered hyp.',r'\unsure{hyp.} on same line as (sans',r'\ill{}',r'hyp. on its separate staggered line above/right of (sans',True,True,'medium','R1: hyp. doubtful, linear phrase; R2: hyp. clear, linear phrase; R3: hyp. doubtful, staggered. Final chooses R2’s lettering and R3’s geometry.','The tall first stroke, y-like descent, final p-like turn and period support hyp. It lies above/right of sans, not on the same baseline; separate TikZ nodes preserve the placement.'),
 ('M4','Margin, sans',r'\unsure{sans}','sans','sans',True,False,'medium','R1: sans clear; R2 and R3: sans doubtful. Main crop supports the initial s, bowl of a, joined n and final s.','The opening parenthesis and s-a-n-s sequence are visible on the lower left slanted line.'),
 ('M5','Margin, noeth.',r'\unsure{noeth.}',r'\uncertain{noeth.}','noeth.',True,True,'medium','R1: noeth. clear; R2 and R3: doubtful. Main crop supports the no/e sequence, crossed t, tall h and period before closing parenthesis.','Final line has small rounded n/o/e traces followed by t-h strokes, a point and the closing parenthesis.')
]
for j,(id,place,c,h,final,cc,hh,conf,readers,evidence) in enumerate(margin):
 d=copy.deepcopy(old);d.update(id=id,place=place,C=c,H=h,final=final,c_changed=cc,h_changed=hh,confidence=conf,readers=readers,evidence=evidence,kind='insertion or placement' if id=='M3' else 'other',marked_in_H='yes' if '\\ill' in h or '\\uncertain' in h else 'no')
 ds.insert(i+j,d)

# R1 separately identified the first prose underline's extent and a case question.
d=copy.deepcopy(rs['R1']['differences'][6]);d['final']=d.pop('reading');d['crop']='readers/'+stem+'/R3/02_ideal_alphabets.jpg';d['readers']='R1 explicitly distinguishes the prose rule from the O sheaf rule; R2 and R3 retain C’s same underline scope in their complete readings.';d['marked_in_H']='no';ds.insert(6,d)
d=copy.deepcopy(next(d for d in rs['R1']['differences'] if d['id']=='R1-D32'))
d.update(final='Z^1(X)',c_changed=False,h_changed=False,confidence='high',readers=r'R1: \unsure{z|Z}; R2: Z; R3: Z. Main-reader decision: Z.',evidence='The narrower Div/Z crop shows the letter at the cap-height of the adjacent D and X, above the x-height of a/n/s in dans. There is no reason to substitute lowercase z.',marked_in_H='no')
d.pop('reading',None);ds.append(d)
for d in ds:
 if not d.get('crop'):raise ValueError('Missing decided crop '+d['id'])

cd=copy.deepcopy(rs['R3']['c_doubts'])
for d in cd:
 p=d['place']
 if p in ['First line-start cancellation','Second line-start cancellation']:d['decision']=r'\unsure{en|qu}; see three-reader decision in differences.'
 if p=='Margin sans':d['decision']='sans, without doubt';d['confidence']='medium'
 if p=='Margin hyp.':d['decision']='hyp., without doubt, retained in its separate staggered position';d['confidence']='medium'
 if p=='Margin noeth.':d['decision']='noeth., without doubt';d['confidence']='medium'
 if p=='Summation upper-right stroke':d['decision']=r'\unsure{\prime}, retaining uncertainty between prime and detached terminal';d['confidence']='medium'
 if p=='Overwritten régulier ending':d['decision']=r'\deleted{\unsure{re}}\handwritten{\unsure{er}}'

rem=[
 ('Opening divisor',r"D'",'D','low'),('Earlier letter in étant','n','covered earlier letter','low'),('After définit','Cela signifie','unreadable earlier phrase','low'),('Before first tout','en','qu','low'),('Before il y a','que,','unreadable covered group','low'),('Margin first word','devrait','compressed middle','low'),('Margin verb','figurer','passer','low'),('Before de codimension','est','unreadable covered word','low'),('After seul','positif','préschéma','low'),('After car','cela signifie','unreadable phrase','low'),('Before second tout','en','qu','low'),('Earlier régulier ending','re','covered earlier pair','low'),('Live régulier ending','er','overlapping strokes','low'),('Long deleted passage','[illeg. 2] partie [illeg. 1]','all four estimated words illegible (R2)','low'),('Summation upper-right mark','prime','detached terminal of summation sign','medium'),('Low dot at first Z^1','visible point','stray impression rather than notation','medium'),('After cyc(D) in proposition','deleted ;','overwritten punctuation','low'),('After mais puisque','x','covered letter','low'),('Before aussitôt','résulte','covered word','low')]
rem=[dict(place=p,reading=r,alternatives=a,confidence=c) for p,r,a,c in rem]
inventory=copy.deepcopy(rs['R3']['inventory'])
for x in inventory:
 if 'first_words_or_objects' in x:x['first_words_or_objects']=x['first_words_or_objects'].replace('qu before','en|qu before')
notes="""The reused typescript carries **− IV− 1102 −**, with 1102 entered by hand; its archive number is 18. No date or total page count appears. Section (21.6.5) describes the positive divisor and its closed subscheme, the converse regular codimension-one immersion, and the cycle defined by local lengths. Proposition (21.6.6) states additivity. The final sentence stops at “on”. [Source: 97/019; heading and body, reader reports and crops.]

The margin explicitly asks **“réf !”**, underlined. The other note tentatively says **“devrait figurer|passer dans 21.2.”**; the groups **hyp.**, **(sans**, **noeth.)** are physically staggered and are laid out accordingly. This is a relocation/commentary note, not a proof completed here.

Mathematical consistency prompted checks of the opening possible D-prime, the bare singleton in codim, the barred singleton in the cycle, the detached summation stroke, and the wavy arrow. The codim expression has no overbar; H's added bar is rejected from the tighter crop. The opening D-prime and summation stroke remain uncertain, despite the unprimed D elsewhere. The duplicate = and + are physical line-continuation signs and remain in the diplomatic text.

**N97-019-length-additivity:** the main reader checked the multiplication-by-t isomorphism A/t′A → tA/tt′A and the short exact sequence with quotient A/tA. Regularity of t gives injectivity; additivity of finite lengths gives the written equation. The geometric correspondence and cited sections (21.2.7), (19.1.4), (21.2.5) were carried as background, not independently re-proved. Readers also recorded their own explicitly limited algebraic checks.

The covered cancellations remain tentative or illegible. They are not claimed as recovered merely because C and two readers propose the same word. The lower g in points and the double impression of O are visually resolved; the live comma following the deleted hypothesis is restored outside the deletion."""
record=dict(cote='97',scan=19,folder='H97-01',their_page=18,stem=stem,brief='reader_v01.md',differences=ds,c_doubts=cd,remaining_doubts=rem,inventory=inventory,notes=notes,abbreviations=rs['R3']['abbreviations'],consequential=['Against H: the codim singleton has no overbar; the separate cycle singleton is barred.','Against H: the proposition uses a wavy leadsto arrow. The summation has a detached stroke retained with doubt; its role is not silently supplied.'],crop_counts={r:rs[r]['crop_count'] for r in rs}|{'main_new':3},s_decisions=['No supplied S correction row names 97/019; the 97/005 row lies outside this package and is not transferred to this leaf.'])
(OUT/'pages'/(stem+'.tex')).write_text(t)
(OUT/'decisions'/(stem+'.json')).write_text(json.dumps(record,ensure_ascii=False,indent=2))
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (OUT/'CHECK_EVENTS.tsv').open('a') as f:
 f.write('N97-019-geometric-background\t'+now+'\tGPT-6 Astra Pro; effort not exposed; main reader, this run\tcarried as background without fault found\tEffective-divisor/regular-immersion correspondence and cited ideal product read on 97/019; not independently proved; no external cited sections consulted.\n')
for reader in ['R1','R2','R3']:
 with (OUT/'CHECK_EVENTS.tsv').open('a') as f:
  f.write('N97-019-length-additivity\t'+now+'\tGPT-6 Astra Pro; effort not exposed; '+reader+', fresh page-1 run\ttargeted proof check\tIndependent reader report records multiplication-by-t kernel calculation and finite-length additivity; detailed performed steps and limits retained in readers/'+stem+'/'+reader+'/report.json.\n')
with (OUT/'progress.log').open('a') as f:f.write('scan 019 done '+now+' cote 97; three fresh readers compared; differences decided on crops\n')
print('Saved decided page',stem,'with',len(ds),'recorded loci')
