from pathlib import Path
import json
W=Path(__file__).resolve().parents[1];pg='150_scan095';rp=W/'records'/f'{pg}.json';r=json.loads(rp.read_text());c=json.loads((W/'second'/f'{pg}_comparison.json').read_text());b={x['box']:x for x in c['results']};notes={}
reps=[(r'\inserted{réciproque}',r'\inserted{récipro}que'),(r'\unsure{Sur les|Soient les}',r'\unsure{Sous les|Sur les|donc les}'),(r'\margin{donc $X_i^*',r'\margin{donc $X_i^{\unsure{*|\prime}}'),(r'$, on a',r'$, \unsure{on a|$\mathord{\cdot}\mathord{-}\mathord{\cdot}$}'),(r'\deleted{$\unsure{96}$}',r'\deleted{\unsure{$96$|Or|Où}}'),(r'\deleted{\unsure{cela revient}} on a',r'\deleted{cela \unsure{revient|veut|vaut}} \unsure{on a|$\mathord{\cdot}\mathord{-}\mathord{\cdot}$}'),("pas de chance d'être",r"pas de \unsure{chance|chances} d'être")]
p=W/'pages'/f'{pg}.tex';s=p.read_text()
for a,z in reps:assert s.count(a)==1,(a,s.count(a));s=s.replace(a,z)
p.write_text(s);(W/'records'/p.name).write_text(s)
for x in r['changes']:
 for a,z in reps:x['final']=x['final'].replace(a,z)
 if x['id']=='C08':x['evidence']='The tall initial, low middle and looped l of les are crossed. The first group resembles the uncanceled Sous above but can also be Sur or compressed donc; no independent tall t supports full Soient.'
 if x['id']=='C21':x['evidence']='The crossed group has two looping/angular bodies with a low return. It may be96 or a short Or/Où; its exact sign identity remains unresolved, while the cancellation itself is clear.'
 if x['id']=='C22':x.update(final=r'\deleted{cela \unsure{revient|veut|vaut}}',against_C=True,change_type='doubt resolution',confidence='medium',evidence='The first canceled word has separate c/e, tall looped l and rounded a; cela is resolved. The second low group ends in a tall t, but its crossed middle still admits revient, veut or vaut.')
 if x['id']=='C28':x.update(final=r'\unsure{chance|chances}',confidence='medium',evidence='The c, tall h and low a/n/c/e run form one word. The last small return cannot securely exclude a terminal s; leave the ending doubtful.')
r['changes'].append(dict(id='C38',place='Scope of the first-line replacement',C=r'\inserted{réciproque}',H=r'\add{\uncertain{réciproque}}',final=r'\inserted{récipro}que',evidence='Ré-c-i-pro is raised above the thick canceled group. The following q descender and u/e run stay on the original baseline to its right, outside that cancellation; only the prefix is the insertion.',crop=f'crops/{pg}_blind_B02.png',box=b['B02']['coordinates'],confidence='high',kind='insertion or placement',error_kind='6 insertion placement',against_C=True,against_H=True,consequential=False,marked_in_H=True,phase='blind audit'))
for x in r['doubts']:
 for a,z in reps:x['reading']=x['reading'].replace(a,z)
 if x['place']=='Cancelled opening above Soit':x.update(alternatives=['Sous les','Sur les','donc les'],reason='The crossed low run cannot distinguish these short forms; no full independent t certifies Soient.')
 if x['place']=='Cancelled numeral below first (95)':x.update(alternatives=['96','Or','Où'],reason='Looping residues under the intersecting strokes permit a number or short word; neither is certain.')
 if x['place']=='Cancelled phrase before live on a':x.update(reading=r'\deleted{cela \unsure{revient|veut|vaut}}',alternatives=['revient','veut','vaut'],reason='Cela has separately exposed c/e/l/a bodies; the second word is still partly hidden by the strike.')
for place,reading,alts,box,why in [
 ('Superscript of the marginal hook source',r'\unsure{*|\prime}',[r'*',r'\prime'],'B07','The thick oblique mark has a slight side protrusion, compatible with a compact star, but the separate crossing arms are not secure enough to exclude a prime.'),
 ('After et considérons formula',r'\unsure{on a|$\mathord{\cdot}\mathord{-}\mathord{\cdot}$}',['on a','point-rule-point'],'B08','Three tiny marks are compatible with compressed on a and with a point-rule-point group; retain the local ambiguity.'),
 ('After canceled cela phrase',r'\unsure{on a|$\mathord{\cdot}\mathord{-}\mathord{\cdot}$}',['on a','point-rule-point'],'B10','The low isolated dot, horizontal run and last dot do not independently identify complete letters.'),
 ('Before d\'être équivalente',r'\unsure{chance|chances}',['chance','chances'],'B12','A low final return may be the last e finish or a compressed s; the beginning chance is plain.')]:r['doubts'].append(dict(place=place,reading=reading,alternatives=alts,confidence='medium',reason=why,crop=f'crops/{pg}_blind_{box}.png',box=b[box]['coordinates']))
r['notes']+='\n### Blind reading corrections\n\nOnly récipro is raised as the first-line replacement; que remains on the baseline. Cela is readable beneath its strike; the following verb remains uncertain. Several low on-a groups, the small marginal superscript, the canceled group below the first95 and the ending of chance have been left locally uncertain. Both live formula labels remain95; no sequential renumbering was introduced.\n'
for x in r['inventory']:
 if 'first_words_or_objects' in x:
  for a,z in reps:x['first_words_or_objects']=x['first_words_or_objects'].replace(a,z)
def put(box,why,changed=False,extra=None):
 notes[box]=dict(viewed=True,evidence=why)
 if changed:
  f=b[box]['first']
  repairs=json.loads((W/'records/v_encoding_repairs.json').read_text()).get(pg,{})
  f=repairs.get(box,f)
  for a,z in reps:f=f.replace(a,z)
  if extra:
   for a,z in extra:f=f.replace(a,z)
  notes[box].update(changed=True,final=f)
put('B02','The first boundary group belongs to la in the preceding text. The raised letters read récipro, while q/ue continues on the baseline to the right: narrow the insertion accordingly. Beneath the thick strike an initial dotted trace survives but not a defensible full inverse/immédiat sequence, so retain illegible1 for the old word.',True)
put('B03','The first tall slanted letter has the looped form of S used in Si, followed by the low ous run; keep Sous. The separate les, literal equality sign, whole difference formula and inserted barred-J-minus-J expression agree. The final i.e. is crossed.')
put('B04','The complete repeated f et s is present. The first s has a stop, the second does not; the line-end i.e lacks its second stop. The raised loc terminal is a crossed t. All literal repeated wording and the final bande remain.')
put('B05','The crossed first word has a tall initial and low connecting run; Sous/Sur/donc remain possible, while the expected tall t of Soient is absent. The live Soit maintenant, pour and pro-voisinage are clear. Two linked crossed uprights form tt rather than a mathematical universal sign.',True)
put('B06','The whole94 definition is clear, with plain handwritten V, i subscript, starred X_i, comma, second X and balanced parentheses. The repaired command delimiter supplies the missing space after qquad only.')
put('B07','The marginal note is fully present: donc, hook map, parenthesized h-over-wave and equivalence words. The tiny source superscript is one thick oblique mark with a slight side branch; star/prime remains uncertain. The parentheses enclose the X métrisable qualification.',True)
put('B08','The formula, its comma and the visible remainder of considérons agree. After the comma lie three tiny low marks; retain on a/point-rule-point uncertainty. The clipped opening is already covered by the first-pass line reading.',True)
put('B09','Both complete implication rows were viewed. Their stars, closure bars, phi glyphs and double arrowheads agree; the short caption reads strat. dense and the other strat fid. The canceled group below the live95 has loops that could be96 or Or/Où, so broaden the local doubt. It is not an additional live word.',True)
put('B10','Cela has separately visible c/e, tall l and a. The following canceled verb has a long low run and terminal t, leaving revient/veut/vaut unresolved. The subsequent low three-mark group remains on a/point-rule-point. The entire unnumbered equivalence and its final stop agree.',True)
put('B11','The complete sentence, (i,j), colon after équivalente, phi formula and final On a are visible. The canceled low word permits comme but is not fully readable. Chance is present on the next overlapping region; its final return leaves chance/chances uncertain, rather than omitting the word as in the blind row.',True)
put('B12','The complete display has live95: the second glyph has a straight top and lower bowl, without the rounded upper approach of6. Both opposed double arrows and their captions agree, with the tt/tte ending remaining doubtful. The upper-left chance fragment was considered with B11 and its ending made uncertain there.')
put('B13','On posera,97, the comma between i and j in the subscript, accented déf, intersection and final comma all agree. Math font and spacing changes are representation only.')
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');(W/'second'/f'{pg}_root_crop_notes.json').write_text(json.dumps(notes,ensure_ascii=False,indent=2)+'\n')
print('095: all12 differing boxes viewed; seven changed boxes.')
