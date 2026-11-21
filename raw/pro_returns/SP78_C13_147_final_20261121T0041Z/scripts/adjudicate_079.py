"""Record root's personally viewed final-scan decisions; run once only."""
from pathlib import Path
import csv,json
w=Path(__file__).resolve().parents[1];page='147_scan079'
ev={
'B01':'The first M has a clean two-arm roof. Above the second M, several angular strokes cross the roof; no separate arrow shaft is isolated. Retain the uncertain canceled-roof reading and the independently placed stars. The prime/underline macro variants do not change the visible indices.',
'B02':'The arching, horizontal and vertical cancellation strokes cover the whole main trial; its parenthetical phrase is not a live insertion. Enlevant remains visible. The quoted word is too crossed to distinguish l’infini from l’âme, and the short group after les traces cannot securely distinguish de la réunion from sur le germe. Qualify each whole group. The M formulas, resp., uncertain Gamma groups and existing formula-level doubts remain. No independent additional à l’infini is established inside this small canceled passage.',
'B03':'The slanted live replacement reads enlevant les traces des diviseurs à l’infini in its physical order. The earlier trial and non seuls remain canceled and qualified. The M after qui contiennent has an independent roof; its G bar remains doubtful. On prend la has a low a return; the underlined trace has t/r/a/c/e and no g descender. Sur has a short low opening, not a p descender. The replacement belongs to the revised definition, not an independent margin paragraph.',
'B04':'The live line is distinct from the cancellation above it, but the compact middle strokes of Ils sont donc do not expose every letter independently. Qualify the whole prefix while keeping des, filtres d’ouverts de la multiplicité and the following words. The live M has a bare G-prime: the space under its body has no independent underline.',
'B05':'The first word has two descending components, the initial looped g and later p, with the reduced rou run between them; comparison with the final groupoïdes on this sheet supports one groupoïdes, not an added pro. prefix. A separate multiple-crossing mark follows the connected tail of fondamentaux and precedes the canceled Pi-like group. Retain the prose asterisk and the qualified canceled Pi.',
'B06':'Both M bodies have blank space directly above them. The small signs sit to their upper right. Each is retraced, with left-pointing branches and a short rightward shaft; neither exposes a fully independent set of star rays. Retain star/left-arrow alternatives for both, without supplying an M roof. The two barred G indices and the primes remain visible.',
'B07':'The complete saved crop19 shows the low uni opening, v/e/r/s run, tall looped l and final s of universels, followed by a separate comma and reduced ou-like group. No q descender establishes microscopiques. A second ou starts the next line before comme. The abbreviated revêtts has a compact t/t group and no ements continuation. Preserve the capital Catégories and the rightward arrow below lim.',
'B08':'The separate d-like prefix and flattened connexe run remain a whole unresolved phrase. Desdits has a d loop, the des run and tall t before s. The word multiplicités is physically split after multi, with an independent short hyphen at the right edge; preserve multi-plicités. The reference has one 5 and a closing upright/foot bracket, not a second numeral3. The n°5 and p.768-prime are separate.',
'B09':'The upper shaft ends in a rounded thick point without two arrowhead arms. The downward arrow targets the lower two-index M; the parenthesized M_G is to its left, with a separate rightward arrow to the same target. The lower-left G has a bar and no independent prime. Both canceled groups remain provisional. Équiv is abbreviated without a detached period. The extra closing curve is above/right of the caption’s ordinary closing parenthesis and remains separately positioned with unresolved attachment.',
'B10':'The mark after lieu has a short curved upper part and a detached lower point; it does not expose a full lower letter body. Retain the à/colon alternative. The retraced d of des is live and intersects the descending caption parenthesis; no separate canceled word is supplied.'}
first={r['box']:r['reading'] for r in csv.DictReader((w/'second'/f'{page}_first.tsv').open(),delimiter='\t')}
d={b:{'root_viewed':True,'changed':False,'evidence':e} for b,e in ev.items()}
repls={
'B02':[("(``l'infini'')",r"(``\unsure{l'infini|l'âme}'')"),(r'de la \unsure{réunion}',r'\unsure{de la réunion|sur le germe}')],
'B04':[('Ils sont donc',r'\unsure{Ils sont donc}')],
'B06':[(r'M^{\unsure{*}}',r'M^{\unsure{*|\leftarrow}}'),(r'M^*',r'M^{\unsure{*|\leftarrow}}')],
'B08':[('multiplicités','multi-plicités')]}
p=w/'pages'/f'{page}.tex';t=p.read_text();assert not (w/'second'/f'{page}_root_decisions.json').exists()
for k,pairs in repls.items():
 f=first[k]
 for a,b in pairs:assert a in f;f=f.replace(a,b)
 d[k].update(changed=True,final=f);assert first[k] in t;t=t.replace(first[k],f)
p.write_text(t)
(w/'second'/f'{page}_root_decisions.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
p=w/'reviewed'/f'{page}.json';r=json.loads(p.read_text())
byid={x['id']:x for x in r['changes']}
byid['079-02'].update(final=r"enlevant (``\unsure{l'infini|l'âme}'')",confidence='medium',evidence='The initial enlevant run and enclosing punctuation survive in the canceled main baseline. The letters within the quotation are crossed and now remain l’infini/l’âme alternatives; this row retains only the independently readable verb and the separate physical location as established differences from H.')
byid['079-06'].update(final=r'(les traces \unsure{de la réunion|sur le germe}',confidence='low',evidence='The opening parenthesis and les traces are visible beneath the strike. The following short words and central noun are not separately secure; the whole de la réunion/sur le germe group remains unresolved. The opening parenthesis and canceled placement are recorded independently of that unresolved wording.')
byid['079-18'].update(final=r'\unsure{Ils sont donc} des',confidence='low',evidence='The opening live prefix is compatible with Ils sont donc, but the compressed middle letters remain qualified. The following des is independently readable below the canceled block; H leaves this entire live opening as illegible.')
byid['079-03']['evidence']=byid['079-03']['evidence'].replace('parenthesized l’infini','parenthesized uncertain l’infini/l’âme group')
for x in r['inventory']:
 for pairs in repls.values():
  for a,b in pairs:
   # Formula changes are local to display (100), and hyphen local to the definition paragraph.
   if pairs is repls['B06'] and x['element']!='13':continue
   if pairs is repls['B08'] and x['element']!='14':continue
   x['first_words_or_objects']=x['first_words_or_objects'].replace(a,b)
r['inventory'][12]['position']='Display (100), with both raised signs unresolved between star and leftward arrow'
r['doubts'][2].update(place='Small canceled parenthetical: whole group after les traces',reading=r'\unsure{de la réunion|sur le germe}',alternatives='de la réunion; sur le germe',reason=ev['B02'])
r['doubts'][10].update(place='Both raised signs in (100)',reading=r"\Pi M^{\unsure{*|\leftarrow}}_{\underline G,\underline G'}",alternatives='Retraced star or leftward arrow; neither M has an independent roof.',reason=ev['B06'])
r['doubts'].extend([
 {'place':'Quoted phrase in the large canceled main trial','reading':r"\unsure{l'infini|l'âme}",'alternatives':'l’infini; l’âme','confidence':'low','reason':ev['B02']},
 {'place':'Live prefix below the canceled block','reading':r'\unsure{Ils sont donc}','alternatives':'The whole prefix is provisionally retained; internal letters are not independently clear.','confidence':'low','reason':ev['B04']},
 {'place':'Second raised sign in (100)','reading':r'\unsure{*|\leftarrow}','alternatives':'star; leftward arrow','confidence':'medium','reason':ev['B06']}])
for x in r['decisions']:
 if x['id']=='M1074':x.update(reading=r"\Pi M^{\unsure{*|\leftarrow}}_{\underline G,\underline G'}",ink='The space immediately above the first M body is blank, so the no-hat choice is resolved. Its raised sign lies to the upper right and remains star/left-arrow uncertain; this does not resolve the exponent shape.',crop='147_scan079_second_B06.png (291,780,1355,907)')
r['notation'][2].update(reading=r'\unsure{*|\leftarrow}',evidence=ev['B06'],scope='Both raised signs in (100); both M bodies lack an independent roof.')
r['unresolved'][0]='The crossed second opening roof, quoted l’infini/l’âme, whole de la réunion/sur le germe group, and other formulas/words inside the large cancellation remain doubtful.'
r['unresolved'][2]='Both raised signs in (100) remain star/left-arrow alternatives; the absence of independent M roofs is resolved.'
r['unresolved'].append('The live prefix Ils sont donc is retained with whole-group uncertainty.')
r['notes'][2]=r['notes'][2].replace('The first star alone remains locally doubtful.','Both raised signs remain star/left-arrow alternatives after the blind audit.')
r['notes'].append('Blind audit: all ten differing boxes were personally inspected by root. Four boxes changed: crossed word groups and the live prefix were qualified, both signs in(100) retain star/left-arrow alternatives, and the visible multi-plicités line-end hyphen was restored. The slanted replacement, prose asterisk, universels, two ou groups, abbreviated revêtts/équiv, bracketed reference, diagram geometry and final à/colon doubt were retained. These are visual reading decisions, not new mathematical proof checks.')
r['changes'].append({'id':'079-39','place':'Definition paragraph: line-end hyphen inside multiplicités','C':'multiplicités','H':'multiplicités','final':'multi-plicités','evidence':'A short independent hyphen follows multi at the right end of the baseline; plicités begins the next line. Both pieces and the hyphen are visible in blind crop B08. The transcription preserves the drawn hyphen without imposing a new line-layout rule.','crop':f'{page}_second_B08.png','box':[328,1205,1672,1464],'confidence':'high','against_C':True,'against_H':True,'kind':'other','marked_in_H':False,'error_sheet_kind':'other','consequential':False})
r['root_review_notes']='Historical first-reading review: '+r.get('root_review_notes','')+' Final blind audit: all ten differing boxes inspected. The crossed quotation and short-word group, live prefix, and both raised signs are now explicitly qualified. The physical line-end hyphen in multi-plicités is restored. Previous first-pass descriptions of only one doubtful star and an unqualified prefix are superseded by these final records.'
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
p=w/'workflow/root_audit_views.json';v=json.loads(p.read_text());v['79']={'crops':[f'{page}_second_{k}.png' for k in ev]+[f'{page}_place19.png']+[f'{page}_second_root_{k}.png' for k in ['B04_prefix','B05_prefix','B05_end']],'extra_boxes':{'B04_prefix':[330,455,960,545],'B05_prefix':[330,680,705,795],'B05_end':[725,635,1210,785]},'observations':ev,'failed_view_note':'An earlier combined B04/B05 display was truncated before either image was visible. Neither was counted then; each was subsequently opened individually and personally viewed.'};p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
