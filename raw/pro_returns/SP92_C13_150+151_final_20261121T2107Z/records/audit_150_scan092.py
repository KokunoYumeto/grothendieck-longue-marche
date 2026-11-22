from pathlib import Path
import json
W=Path(__file__).resolve().parents[1];pg='150_scan092';rp=W/'records'/f'{pg}.json';r=json.loads(rp.read_text());c=json.loads((W/'second'/f'{pg}_comparison.json').read_text());b={x['box']:x for x in c['results']};notes={}
reps=[(r'\deleted{\unsure{X_j}}',r'\deleted{\unsure{\bigcup|X_j}}'),(r'\deleted{\unsure{la}}',r'\deleted{\unsure{la|r}}'),(r'X_i\neq\phi\Rightarrow X_i^*\neq\phi',r'X_i\neq\phi\unsure{\Rightarrow|\rightarrow}X_i^*\neq\phi'),(r'\unsure{Stratifications|Cet axiome}',r'\unsure{Cet axiome|Stratifications}')]
p=W/'pages'/f'{pg}.tex';s=p.read_text()
for a,z in reps:assert s.count(a)==1,(a,s.count(a));s=s.replace(a,z)
p.write_text(s);(W/'records'/p.name).write_text(s)
for x in r['changes']:
 for a,z in reps:x['final']=x['final'].replace(a,z)
 if x['id']=='C01':x['evidence']+=' The blind crop shows a U-shaped outer contour beneath the diagonal cancellation, making a canceled union a viable first alternative; the exact old sign remains uncertain.'
for d in r['doubts']:
 for a,z in reps:d['reading']=d['reading'].replace(a,z)
 if d['place']=='(90), cancelled group':d.update(alternatives=[r'\bigcup','X_j'],reason='The outer contour has two uprights and a rounded lower join, favoring a union sign. Internal diagonal cancellation also permits the earlier X/index reconstruction; the old sign is not certified.')
 if d['place']=='restriction paragraph, cancelled article':d.update(alternatives=['la','r'],reason='A small upright and lower loop remain under two diagonal strokes; neither the full article nor a single r-like abandoned start can be certified.')
 if d['place']=='cancelled clause, opening':d.update(alternatives=['Cet axiome','Stratifications'],reason='The capital-like initial and separate tall t-like stroke favor Cet before the longer low group; the broad cancellation still prevents certification of every letter.')
r['doubts'].append(dict(place='Margin, implication after X_i not equal phi',reading=r'\unsure{\Rightarrow|\rightarrow}',alternatives=[r'\Rightarrow',r'\rightarrow'],confidence='medium',reason='The right head is visible, but the short shaft is a filled retraced block with no continuously separable pair of lines. Keep single/double-shaft uncertainty.',crop=f'crops/{pg}_blind_B06.png',box=b['B06']['coordinates']))
for x in r['inventory']:
 if 'first_words_or_objects' in x:
  for a,z in reps:x['first_words_or_objects']=x['first_words_or_objects'].replace(a,z)
r['notes']+='\n### Blind reading adjudication\n\nThe literal J in On a pour tt i-in-J and in the last i,j-in-J remains: both have the hooked lower foot of J rather than the two-sided I serif. The first canceled sign in90 now admits a union sign as well as X_j. The canceled clause favors Cet axiome without resolving its obscured lettering. The short filled marginal arrow remains uncertain as to one or two shafts; its rightward direction is clear. Supposera, voire, the semicolon after the density insertion, and the absence of a detached comma after fort were confirmed. These are uncertainty refinements and confirmations; no new C/H correction row is added solely for changed certainty.\n'
def put(box,why,changed=False):
 notes[box]=dict(viewed=True,evidence=why)
 if changed:
  f=b[box]['first']
  for a,z in reps:f=f.replace(a,z)
  notes[box].update(changed=True,final=f)
put('B01','The whole90 crop shows a U-shaped outer contour beneath diagonal cancellation, so include union as the preferred old-sign candidate while retaining X_j as an alternative. The live X_i, difference, union, j<i index and right X_j agree. Display and dollar delimiters do not change the ink.',True)
put('B03','The quantifier, I, comma, X_i star, not-equal, literal phi and final stop are clear. Only mathematical delimiter and ne/neq syntax differ.')
put('B04','The crossed tiny form can be la or an abandoned r-like start; retain both locally. The ending of fort is a connected looping t return with no detached comma. The remaining prose and line sequence agree.',True)
put('B05','The full exact crop shows a detached upper dot and a separate curved lower mark after the inserted closure equality: semicolon. Both leaders attach to Strat5, and the first includes the full for-all-i-in-I condition. The implication has two thin parallel traces around its dark central return and a right head, so retain the double shaft. The entire closure and rare-in-X_i clause agrees. The upper encore fragment belongs to the preceding line.')
put('B06','Viewed the full exact margin and its45-degree rotation. The words, quantifier after X_i nonempty, all phi forms, whole parenthetical equality and rightward implication agree. The implication shaft is a short filled block, so single/double remains uncertain. The neighboring i.e. is main-text overlap, not additional marginal wording.',True)
put('B07','The right-edge verb has visible low e/r/a continuation after the suppos- group: supposera. Inside the next parenthesis, the opening v, rounded o, dotted i and later r/e distinguish voire from ou. All four main lines and the final stop agree.')
put('B08','The opening capital-like loop and tall t-like remnant favor Cet axiome; the cancellation still obscures enough joins to retain Stratifications as an alternative. The final descender supports impliq, while terminal traces remain hidden, so do not certify the full implique.',True)
put('B09','The whole91 crop shows two joined raised t stems in tt, unlike the separate universal sign in Strat4/5. The following capital has a top cap, right descent and leftward bottom hook: literal J, not I. The entire union and lower i.e. j<=i annotation agree; no parentheses surround that annotation.')
put('B10','The final membership again has a hooked J, matching B09 and contrasting with the two-serif I in Strat4/5. Retain the literal J. The very compressed on aura remains uncertain rather than certified from the blind reading; donc, comma and si agree.')
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');(W/'second'/f'{pg}_root_crop_notes.json').write_text(json.dumps(notes,ensure_ascii=False,indent=2)+'\n')
print('092: all9 differing boxes observed; four uncertainty-only changed boxes.')
