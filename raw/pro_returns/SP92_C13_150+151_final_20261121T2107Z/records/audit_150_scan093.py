from pathlib import Path
import json
W=Path(__file__).resolve().parents[1];pg='150_scan093';rp=W/'records'/f'{pg}.json';r=json.loads(rp.read_text());c=json.loads((W/'second'/f'{pg}_comparison.json').read_text());b={x['box']:x for x in c['results']};notes={}
reps=[('aux unions et intersections','aux unions, et intersections'),(r'X_I^*=X.',r'X_I^*=X'),('Si on a (Strat 5), alors',r'Si on a (Strat 5), \unsure{alors|les}'),(r'saturé de la forme $X_?^*$, qui',r'saturé (i.e. de la forme $X_?^*$) qui')]
p=W/'pages'/f'{pg}.tex';s=p.read_text()
for a,z in reps:assert s.count(a)==1,(a,s.count(a));s=s.replace(a,z)
p.write_text(s);(W/'records'/p.name).write_text(s)
for x in r['changes']:
 for a,z in reps:x['final']=x['final'].replace(a,z)
for ident,place,C,H,final,box,why,kind,ek in [
 ('C24','Opening prose, punctuation after unions','aux unions et','réunions et','aux unions, et','B03','A detached low curled comma lies after the last n/s stroke of unions and before the separate et.','other','10 other'),
 ('C25','Unnumbered total-set equality, final punctuation',r'X_I^*=X.',r'X_I^*=X.',r'X_I^*=X','B05','The full exact crop has blank space after the final X with no detached stop. The comma between the two equalities is present and retained.','text not on the page','9 not on page'),
 ('C26','Diagonal margin, explanation of saturé',r'saturé de la forme $X_?^*$, qui',r'\ill{} de la forme $X_?^*$, \ill{}',r'saturé (i.e. de la forme $X_?^*$) qui','B13','The rotated whole note shows an opening parenthesis after saturé, then i.e. with its dots, followed by de la forme. A closing parenthesis follows the literal question-indexed X; it is not a comma. The main97 label crosses the same area but belongs to the display.','omission','3 omissions')]:
 r['changes'].append(dict(id=ident,place=place,C=C,H=H,final=final,evidence=why,crop=f'crops/{pg}_blind_{box}.png',box=b[box]['coordinates'],confidence='high',kind=kind,error_kind=ek,against_C=True,against_H=True,consequential=False,marked_in_H=ident=='C26',phase='blind audit'))
r['doubts'].append(dict(place='After Si on a (Strat5)',reading=r'\unsure{alors|les}',alternatives=['alors','les'],confidence='medium',reason='A large looped tall stroke and two low groups can encode compressed alors, but the opening a and internal r cannot be isolated securely from l/e/s. Keep the local word unresolved.',crop=f'crops/{pg}_blind_B10.png',box=b['B10']['coordinates']))
for x in r['inventory']:
 if 'first_words_or_objects' in x:
  for a,z in reps:x['first_words_or_objects']=x['first_words_or_objects'].replace(a,z)
r['notes']+='\n### Blind reading corrections\n\nA comma follows unions in the opening prose. The unnumbered equality X_I*=X has no final stop. The diagonal explanation of saturé is parenthetical and begins i.e.; its closing parenthesis after the question-indexed X replaces the drafts\' comma. The word after Si on a (Strat5) is now left alors/les. The relation in95 remains membership/inclusion, the crossed middle X remains canceled without extending the strike over its barred-J subscript, and the literal question mark in the margin stays resolved. No formula was altered to fit the already recorded set-theoretic check.\n'
def put(box,why,changed=False):
 notes[box]=dict(viewed=True,evidence=why)
 if changed:
  f=b[box]['first']
  for a,z in reps:f=f.replace(a,z)
  notes[box].update(changed=True,final=f)
put('B02','The full old equality is crossed, with star on the left term and a separate bar over the right J. Dollars and overline-versus-bar syntax do not change its reading or deletion scope.')
put('B03','The left group has a rounded capital O, low n and separate reduced a; keep On a, without an invented cap sign. The assignment has a tailbar and blunt endpoint with no chevron. A detached low comma follows unions and is restored. The entire remaining sentence agrees.',True)
put('B04','Both union/intersection identities agree, including each alpha index and all four stars. The handwritten94 is at the left; tag placement in the blind TeX is only an encoding choice.')
put('B05','Both empty-set glyphs have the oblique shaft and small bowl of phi. The full crop leaves blank space after the final X, with no period; remove that stop. The comma between the two equalities is clear.',True)
put('B06','The whole95 formula shows a single clustered star; its small upper dot is part of that cluster, not a separately continuous prime. The thick relation retains in/subset ambiguity. Extra oblique strokes cross the middle X only, leaving its barred-J index live. The last equality and starred barred-J term agree.')
put('B07','The margin has a clear hooked J after si. The low o/n run is partly at the crop edge but its n stroke and separate a are present before the equality. Keep on a. Both equalities/closedness phrases and comma agree.')
put('B08','The lower bracket has a central downward cusp, so the existing underbrace is faithful here. Its J0 label, both set differences, all stars and96 agree. The preceding et is already transcribed outside the display.')
put('B10','The tiny upper fragment does not provide a complete extra l/apostrophe on the Si on a baseline, so do not supply it. The final looped word leaves alors/les uncertain; retain that local uncertainty. Strat5 and its punctuation are clear.',True)
put('B11','The separator between the two final terms is a bottom horizontal bar with two short rising strokes, extending beyond them: amalg. No uncertainty between union shapes is needed. The closure bar, parentheses, stars and all indices agree. Display grouping differs only.')
put('B13','Viewed the full exact crop and its36-degree rotation. The opening has the d/u/a/l and compressed e/m/e/n/t run of dualement, not the proposed short fragments. The parenthesis and i.e. after saturé are present and recovered. Its closing parenthesis is after the literal question-indexed X; no comma is written there. The final contienne has the low double-n/e ending, without a terminal t. The main97 label is not marginal prose.',True)
put('B14','The entire definition is canceled by one long wavy stroke. Its first X has a dot and no star; def has no detached accent. The right closure and difference expressions agree. Overset grouping and math delimiters are encoding differences.')
put('B15','The first canceled barred X_J and small upper star remain visible; a second X-shaped form survives under the zigzag. The middle relation and final index remain uncertain as a whole formula, not an illegible word placeholder. The live tail reads est fermé i.e. with i/e and their dots, not ici.')
put('B16','The first word retains its g descender and final tall l; the following reduced à has the familiar two-mark form. Both ssi groups are the same compressed short form; the final one has two independent underlines. The small opening parenthesis before si strat and its closing mate are visible. Both phi forms, all bars/stars and the exact closedness chain agree. The lower insertion belongs to B17 and is already transcribed there.')
put('B17','The crossed capital has a tall left side and right loops, retaining A/B uncertainty; its shape is unlike the following clean hooked J in the insertion. The comma is on the main baseline after ouvert. The curved insertion leader attaches before alors and has no independent final comma.')
put('B18','The entire98 expression, complement-X sign, canceled f, open condition and the two-line parenthetical statement agree. Setting est/open prose inside or outside the display does not change the written text or placement.')
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');(W/'second'/f'{pg}_root_crop_notes.json').write_text(json.dumps(notes,ensure_ascii=False,indent=2)+'\n')
print('093: all15 differing boxes observed; four changed boxes.')
