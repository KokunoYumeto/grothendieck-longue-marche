from pathlib import Path
import json
R=Path('/workspace/scratch/8f839dff4bf0/SP74_C13_143+145_work')
p=R/'reviews/143_scan033_readerA.json'; t=R/'reviews/143_scan033_readerA.tex';d=json.loads(p.read_text());s=t.read_text();assert 'main_adjudication' not in d
old=r'\unsure{g|\xi}';new=r'\unsure{\xi|g}'
s=s.replace(old,new).replace(r'\unsure{-}S_\nu',r'S_\nu')
for r in d['changes']:
 r['final']=r['final'].replace(old,new).replace(r'\unsure{-}S_\nu',r'S_\nu')
 if r['place']=='Upper diagram, first X: low index':
  r['ink']='The low graph has an open upper c/e-like turn and a long curved descender. The page\'s g indices have a more clearly closed bowl. Xi is therefore preferred, but the reduced graph does not exclude g. Reordering C\'s alternatives is certainty-only; H\'s xi is no longer a material disagreement.'
  r['against_H']=False
 if r['place']=='Upper diagram, second X: separator before S':
  r.update(against_C=True,against_H=True,kind='text not on the page',confidence='medium',ink='Between the low X index and S there is only an extremely pale horizontal trace with tiny dark ends, lacking the blue ink and weight of either neighboring graph. Main treats this as non-textual show-through/print rather than a source separator. Neither C\'s minus nor H\'s diagonal set-minus is supplied, even as doubtful ink.')
 if r['place']=='Lower diagram: middle Gamma to right 1':r['final']=r'\Gamma \arrow[r]'
# Certainty alone is not a material row.
d['changes']=[r for r in d['changes'] if r['against_C'] or r['against_H']]
for r in d['decisions']:
 if r['id']=='M0748':
  r['reading']=new;r['ink']='Open upper turn and long curved descender, contrasted with closed-bowl local g indices, favor xi. The reduced shape still leaves g possible; main changes preference without claiming resolution.'
for r in d['remaining_doubts']:
 if r['place']=='Upper diagram: first X index':
  r['reading']=new;r['alternatives']='xi / g';r['reason']='The open upper turn favors xi against the closed local g bowls, but the reduced graph remains ambiguous.'
d['remaining_doubts']=[r for r in d['remaining_doubts'] if r['place']!='Upper diagram: second-object separator']
d['certainty_resolutions']=[r for r in d['certainty_resolutions'] if r['place']!='Upper diagram: certainty of C horizontal separator']
d['certainty_resolutions'].append(dict(place='Upper diagram: first-X index preference',C=old,final=new,ink='Open upper turn versus closed g bowls elsewhere on this page favors xi; both alternatives remain. This preference change is excluded from material counts.',crop='crops/143_scan033_A_top_left_object.png',box=[800,295,1120,425]))
d['unresolved_for_main']=[]
refs={
 'Upper diagram: auxiliary top 1 number 1, descending link':('upper_aux',[675,170,1320,315]),
 'Upper diagram: auxiliary top 1 number 2, descending link':('upper_aux',[675,170,1320,315]),
 'Lower diagram: first auxiliary top 1, descending link':('lower_aux',[850,750,1320,900]),
 'Lower diagram: top right 1 down to middle Gamma':('lower_one_down',[1630,940,1815,1050]),
 'Printed lower-left sequence':('printed_numbers',[155,1890,205,2165]),
 'Printed lower-right code':('printed_code',[2580,1970,2700,2170]),
 'Pencil lower-left pagination':('page_number',[10,2150,330,2227])}
for r in d['changes']:
 if r['place'] in refs:
  n,b=refs[r['place']];r['crop']=f'crops/143_scan033_main_{n}.png';r['box']=b
for r in d['inventory']:
 r['sheet_kind']='text'
 if r['hand']=='printed':r['hand']='print'
 elif r['hand']=='main blue-ink hand':r['hand']='his hand (blue ink)'
d['main_adjudication']=dict(original_seen=True,existing_crops_seen=21,main_crops_seen=6,decision='Every returned difference/open locus inspected. Consistent pi retained; xi/g reordered without resolving; pale separator excluded; remaining arrow and cancellation alternatives retained. Six page-only discrepancy crops confirm auxiliary bare shafts, lower 1-to-Gamma shaft, printed numerals/code and pencil 32.',failed_emissions='gamma_double_link was re-emitted after earlier output truncation. The tall printed-number crop was omitted by the image channel; it was then viewed as a rotated, scaled copy of that same crop, with no recrop. The copy is outside the packaged work tree.')
d['notes'].append(dict(id='143_scan033-N8',text='Main excludes the pale horizontal trace between the second X index and S as non-textual. The first expression has an inked set-minus; the second has no secure blue separator. Mathematical parallelism is not used to fill the gap. The first-X index preference is xi/g because its open upper turn differs from the page\'s closed-bowl g indices; uncertainty remains. The second reduced index retains j/xi.'))
d['hand_log'].append(dict(habit='A pale listing trace can imitate a separator between mathematical terms.',places='Upper diagram, second X and S.',scope='This single gap only; the first object has a blue diagonal set-minus.',misreadings='C supplies a minus and H a set-minus. Neither has secure ink weight/color at this gap.'))
p.write_text(json.dumps(d,ensure_ascii=False,indent=2));t.write_text(s)
(R/'reviews/143_scan033_main.md').write_text('''# Main-reader adjudication — 143_scan033

Main viewed the original once, all 21 existing tight crops, and six additional crops of differences that the first reader had settled from the page. Every material row and retained uncertainty was adjudicated. The six additional boxes are in main_crop_manifest.jsonl. The tall printed-numeral crop initially exceeded the image channel limit; a rotated and scaled viewing copy of the same saved crop was then inspected. No second crop was made.

The ten live group graphs and cancelled predecessor use pi consistently with the previously inspected flat-cap pi hand. The first-X index is now xi/g, still undecided: the upper turn is open while the nearby g bowls are closed. This preference-only change is not counted. The second X retains j/xi. The separator after it is omitted: the very pale trace is not securely blue source ink, so neither witness's separator is supplied. This is a material omission against both witnesses, recorded with medium confidence.

Small heads on the horizontal edges are preserved individually. The upper middle Gamma–1 edge remains left/right uncertain; the upper bottom exit remains headed/bare uncertain. The two lower Gamma strokes have blunt ends and interior projections; their literal TikZ approximation is retained. The upper two auxiliary links, lower first auxiliary link and lower 1-to-Gamma link are plain shafts. The lower final exit is also bare. No conventional exact-sequence pattern is used to change them.

The word is traces, with a closed third-letter bowl and an open following c. Its connected lower letter strokes do not form a separate brace. Its placement under the operator-to-Gamma span is retained. K is uppercase; the first membership line has no terminal comma. The bottom cancelled symbol keeps its g index and uncertainty, and the separate superscript wave is not nested under the live hat.

The printed sequence 6–0, 2975–132, 31 IBM logos and pencil 32 are retained. Inventory categories are normalized only to the permitted vocabulary: this face is classified as text, the printed marks as print, and pencil attribution remains unnamed. No mathematical proof or computation was performed.
''')
