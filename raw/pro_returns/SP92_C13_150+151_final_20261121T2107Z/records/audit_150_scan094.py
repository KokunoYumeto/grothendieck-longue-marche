from pathlib import Path
import json
W=Path(__file__).resolve().parents[1];pg='150_scan094';rp=W/'records'/f'{pg}.json';r=json.loads(rp.read_text());c=json.loads((W/'second'/f'{pg}_comparison.json').read_text());b={x['box']:x for x in c['results']};notes={}
reps=[(r'\text{ on a }',r'\quad\unsure{\text{on a}|\mathord{\cdot}\mathord{-}\mathord{\cdot}}\quad'),('alors on aura donc',r'alors on aura \unsure{donc|même}'),(r'\unsure{ens.}',r'\unsure{ens.|fam.}'),('loc fini',r'loc \unsure{fini|finie}'),('Si on veut Strat 5',r'Si on \unsure{veut|est} Strat 5'),('Alors on aura',r'Alors on \unsure{aura|va}')]
p=W/'pages'/f'{pg}.tex';s=p.read_text()
for a,z in reps:assert s.count(a)==1,(a,s.count(a));s=s.replace(a,z)
old=b['B14']['first'];new=old.replace(r'\margin{',r'\margin{\fbox{\parbox{0.88\linewidth}{',1)+'}}';assert old in s;s=s.replace(old,new);reps.append((old,new))
p.write_text(s);(W/'records'/p.name).write_text(s)
for x in r['changes']:
 for a,z in reps:x['final']=x['final'].replace(a,z)
 if x['id']=='C11':x['evidence']='A rounded initial bowl and short low humps survive beneath the strike. They permit ens. or abbreviated fam.; no full famille with two independently tall l stems is visible.'
 if x['id']=='C13':x['final']=r'\inserted{loc \unsure{fini|finie}}';x['confidence']='medium';x['evidence']='Loc has no independent stop. Two i dots are clear in fini; the rightmost low return lies against the rising leader and does not securely exclude a final e. The punctuation difference loc/loc. remains, while the ending is now doubtful.'
 if x['id']=='C19':x['confidence']='medium';x['evidence']='The word has a low loop and a long connected run ending at a short crossed upright. Veut is possible, but est cannot be excluded in the compressed hand; neither is an isolated a.'
 if x['id']=='C36':x['final']=r'\unsure{aura|va}';x['confidence']='low';x['evidence']='Only the initial low mark, intervening horizontal run and final rounded return survive distinctly under the cancellation. Aura and va remain possible; not all letters are plain.'
r['changes'].append(dict(id='C38',place='Enclosure of the diagonal NB note',C='Unframed marginal NB text',H='NB note described as encadrée',final=new,evidence='An enclosing line runs around the whole diagonal NB note, with a left side, upper sloping side, curved right corner and lower sloping side. Preserve that enclosure around the words and formulas.',crop=f'crops/{pg}_blind_B14.png',box=b['B14']['coordinates'],confidence='high',kind='drawing or diagram',error_kind='4 drawings/diagrams',against_C=True,against_H=False,consequential=False,marked_in_H=True,phase='blind audit'))
for x in r['doubts']:
 for a,z in reps:x['reading']=x['reading'].replace(a,z)
 if x['place']=='Cancelled baseline noun':x.update(alternatives=['ens.','fam.'],reason='The first loop and low humps are crossed; the outline does not decide between these short forms.')
for place,reading,alts,box,why in [
 ('Opening second implication, low group',r'\unsure{\text{on a}|\mathord{\cdot}\mathord{-}\mathord{\cdot}}',['on a','point-rule-point'],'B01','Three low separated marks can be a compressed on a or the literal point-rule-point group; no complete letter boundaries certify either.'),
 ('Last word before92',r'\unsure{donc|même}',['donc','même'],'B02','The low beginning and long middle run permit donc; the possible m humps and absence of a clear independent ascender also permit même. No detached circumflex is certain.'),
 ('Inserted local finiteness ending',r'\unsure{fini|finie}',['fini','finie'],'B06','Two i dots are visible, but the final small return and curved leader overlap, preventing a secure decision on e.'),
 ('Condition before the unfinished paragraph',r'\unsure{veut|est}',['veut','est'],'B10','The low opening loop and long fused middle are too compressed to separate v/e/u from e/s. The final crossed t is clear.'),
 ('Canceled final verb',r'\unsure{aura|va}',['aura','va'],'B16','Cancellation covers the low internal strokes; the rounded terminal return does not certify all letters.')]:r['doubts'].append(dict(place=place,reading=reading,alternatives=alts,confidence='low',reason=why,crop=f'crops/{pg}_blind_{box}.png',box=b[box]['coordinates']))
r['notes']+='\n### Blind reading corrections\n\nThe whole diagonal NB note is enclosed; that frame is now represented. Its last union identity still ends literally at X_J*, without completing the expected union. The low group in the opening implication, the word before92, the ending of the inserted fini, the verb before Strat5 and the canceled final verb remain uncertain after the independent reading. The crossed short noun now admits ens./fam.; no complete famille is supplied. The final main sentence remains unfinished as written.\n'
for x in r['inventory']:
 if 'first_words_or_objects' in x:
  for a,z in reps:x['first_words_or_objects']=x['first_words_or_objects'].replace(a,z)
def put(box,why,changed=False):
 notes[box]=dict(viewed=True,evidence=why)
 if changed:
  f=b[box]['first']
  for a,z in reps:f=f.replace(a,z)
  notes[box].update(changed=True,final=f)
put('B01','The whole chain was viewed. The first i strokes are retraced but retain the dotted i form, and each prime is single. The literal nonempty glyph is0. The low group after it consists of three separated tiny marks: leave compressed on a versus point-rule-point uncertain. All bars, relations and the final i-prime-leq-j remain.',True)
put('B02','Viewed the full exact crop. The last word is too compressed to settle donc/même; no detached circumflex is certain. The right stroke of92 remains joined to the2, so the independent closing delimiter stays doubtful. Both double arrows, all three terms and the parenthesized lower qualification agree.',True)
put('B03','A rounded capital O and low n are followed by a separate e/n group; keep On en. No initial D stem or extra nc group warrants Donc.')
put('B04','The complete words and formula agree. The sole final curved stroke closes P(X), followed by a comma; the mathematical delimiter syntax is immaterial.')
put('B05','The final n ends in a low turned return without an independently formed e. Keep d\'un. The separate de la, abbreviated str. and fidèle are visible; the baseline has no extra equivalence verb.')
put('B06','Viewed the full exact crop. The tiny raised group permits rec with uncertain stop and has no independently clear cancellation. The older crossed baseline word has a bowl and low humps, admitting ens./fam.; it is too short to certify full famille. Loc is clear; the two i dots in fini survive but its last return overlaps the leader, leaving fini/finie. The large curve carries this replacement to the baseline; it is not a parenthesis or another canceled word. The small low mark near de lies on that curve, not an independent certified comma.',True)
put('B07','The raised non vides has both word groups and a curved attachment after fermées. The blind extra boundary fragments belong to neighboring baseline words already transcribed, not extra insertion text.')
put('B08','The paired high quotation ticks, comma after fermées and de réunion X are present. The insertion leader originates after baseline X, comma. The baseline satisfaisant la has a looped a, not les; no additional comma is visible after the inserted X at the edge.')
put('B09','The inserted sur l\'intersection has its own final comma above the leader. The curve attaches after Strat3 and before et la. The blind boundary fragments are already part of the main line.')
put('B10','A long fused low run and final crossed t permit veut or est; neither middle sequence is individually secure. Strat5 and its following comma are clear. Keep the local verb doubtful.',True)
put('B12','Two upright strokes share a cross-return, with no independently rounded final e: tt. The next two words are singular strate fermée and have a separate final stop. The first group is not a mathematical universal quantifier.')
put('B13','Both complete rows, brace, number93, stars, union indices and qualifiers agree. Pas néc remains abbreviated and unpunctuated; text/mathematical placement of its parentheses is only encoding.')
put('B14','The whole diagonal note was viewed. Its enclosing upper, left, lower and curved right sides are visible, and the frame is restored. The map tailbar is certain but the thick curled endpoint still does not isolate two arrowhead arms. The union identity ends at X_J*; the following upright belongs to the border, not a slash or missing union term. The cap identity retains its written left-to-right order.',True)
put('B15','The long line crosses the entire prose. Several low letter runs and the initial capital meet the note border or strike, so Nous/On, utiliserons/utilisera, notation/notations and surtout cannot all be certified. The blind certainty is not adopted. Cette and final si are independently legible.')
put('B16','The first J, est une bande and Alors on are visible despite the straight strike. The final small rounded groups do not expose all internal letters: aura/va remains doubtful. The full stop after bande is independent of the strike.',True)
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');(W/'second'/f'{pg}_root_crop_notes.json').write_text(json.dumps(notes,ensure_ascii=False,indent=2)+'\n')
print('094: 15 differing boxes observed; six changed boxes.')
