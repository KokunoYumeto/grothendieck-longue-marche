from pathlib import Path
import json,datetime
W=Path(__file__).resolve().parents[1];pg='150_scan081'
rp=W/'records'/f'{pg}.json';r=json.loads(rp.read_text())
c=json.loads((W/'second'/f'{pg}_comparison.json').read_text());b={x['box']:x for x in c['results']}
notes={}
def put(box,evidence,final=None):
    notes[box]=dict(viewed=True,evidence=evidence)
    if final is not None: notes[box].update(changed=True,final=final)
oldheader=r"\deleted{le cas \unsure{de|où} $V$}"
header=r"\deleted{Le cas ou $V$}"
oldright=r"\deleted{d'où} \deleted{\unsure{considérons|voisinage}}"
right=r"\deleted{\unsure{disposition}}"
oldformula=r"\deleted{$\unsure{V_J\cap V_L=V_{J\cap L}|V_J\cap V_{J'}=V_{J\cap J'}}$}"
formula=r"\deleted{\unsure{NB} $V_J^{\unsure{L}}\cap V_{J'}^{L'}=V_{J\cap J'}^{L\cap L'}$}"
p=W/'pages'/f'{pg}.tex';s=p.read_text()
replacements=[(oldheader,header),(oldright,right),(oldformula,formula),
 (r'\mathrm{déf}',r'\mathrm{def}'),
 (r'qui majorent un élément de $J$',r'qui majorent un \unsure{élém|élément} de $J$'),
 ('qui minorent un',r'qui mino-\\rent un'),
 (r'de $L$, tt élément de $L$ majore',r'de $L$, tt \unsure{élément|élémt} de $L$ majore'),
 ('\nde\n', '\n'+r'\unsure{de|donc}'+'\n')]
for old,new in replacements:
    assert s.count(old)==1,(old,s.count(old));s=s.replace(old,new)
p.write_text(s);(W/'records'/p.name).write_text(s)
changes={x['id']:x for x in r['changes']}
changes['C01']['confidence']='medium'
changes['C01']['evidence']='The full formula was reopened during blind adjudication. The horizontal rule has a small pointed thickening at the right with a short upward arm and a lower return converging at its end. This supports the arrow reading, although the head is compact. Both indices and both arguments were read with it.'
changes['C04'].update(place='right margin, cancelled word after de bandes',C=oldright,final=right,against_C=True,
 evidence='The cancellation crosses one connected sequence beginning with a looped d and ending in the clearly dotted i/t/i/on sequence. A descending p and following round o are visible in the middle. The former division into d’où plus a second word is not supported. Disposition is the favoured reading, but the crossed middle letters remain uncertain.',confidence='low',kind='misread word',error_kind='2 words',crop=f'crops/{pg}_blind_B05.png',box=b['B05']['coordinates'])
changes['C10'].update(final=formula,against_C=True,
 evidence='On the existing crop rotated clockwise 60 degrees, raised L-like strokes occur above both first V terms and L cap L-prime above the last; the last lower line reads J cap J-prime. The second superscript has a separate prime. The initial NB and the first raised L remain partly covered and uncertain. The full superscripted formula, not a formula without superscripts, is present.',crop=f'crops/{pg}_blind_B11.png',box=b['B11']['coordinates'])
changes['C28'].update(final=header,against_C=True,confidence='medium',unresolved=False,
 evidence='The initial L has a straight tall upright and foot, followed by e; the middle word has the open c, round a and returning s. The last word has a low o and joined u, without a d ascender, terminal s or detached accent. All letters lie below the long cancellation. Read Le cas ou V.',crop=f'crops/{pg}_blind_B02.png',box=b['B02']['coordinates'])
r['changes']=[x for x in r['changes'] if x['id'] not in ['C05','C25']]
for ident,place,old,new,box,why in [
 ('C30','(63), definition label','déf','def','B06','The small label has connected d/e/f strokes, but no detached acute above e. The upper half was reopened because the box clips the tall f; it confirms blank paper above the e. Preserve the unaccented label.'),
 ('C31','definition of J_0, line-end word division','minorent',r'mino-\\rent','B13','A detached short horizontal stroke follows mino at the right edge of its line. The next line starts rent. Both the hyphen and the word division are written and were joined away in both drafts.')]:
    r['changes'].append(dict(id=ident,place=place,C=old,H=old,final=new,evidence=why,crop=f'crops/{pg}_blind_{box}.png',box=b[box]['coordinates'],confidence='high',kind='abbreviation expanded or spelling modernised',error_kind='8 abbreviation/spelling',against_C=True,against_H=True,consequential=False,marked_in_H=False,phase='blind audit'))
for d in r['diff_coverage']:
    if 'C05' in d['change_ids']:d['change_ids']=[x for x in d['change_ids'] if x!='C05'];d['reason']='The whole canceled sequence now reads uncertain disposition; its former segmentation is withdrawn after the blind crop review.'
    if 'C25' in d['change_ids']:d.update(change_ids=[],classification='unresolved doubt',reason='The blind review leaves de/donc uncertain. This is a doubt entry, not a certified departure from either witness.')
    if 'C28' in d['change_ids']:d['reason']='The blind crop review resolves the canceled header as Le cas ou V, with no written accent on ou.'
r['doubts']=[x for x in r['doubts'] if x['place']!='struck header']
for d in r['doubts']:
    if d['place']=='right-margin struck word':d.update(reading=r'\unsure{disposition}',alternatives=['disposition; crossed middle letters uncertain'],reason=changes['C04']['evidence'],crop=f'crops/{pg}_blind_B05.png',box=b['B05']['coordinates'])
    if d['place']=='left-margin struck formula':d.update(reading=formula,alternatives=['NB partly covered','first superscript L partly covered'],reason=changes['C10']['evidence'],crop=f'crops/{pg}_blind_B11.png',box=b['B11']['coordinates'])
for place,reading,box,reason in [
 ('first element in definition of L_0',r'\unsure{élém|élément}','B13','The short ending is a low horizontal join with a small terminal turn. It is shorter than the following full élément; the final ent cannot be separately certified.'),
 ('third element in lower-right note',r'\unsure{élément|élémt}','B19','The ending is compressed into a rule and a final t-like upstroke. It may include ent or be the abbreviation mt; no stop is added.'),
 ('isolated final body fragment',r'\unsure{de|donc}','B20','The initial looped d is clear. The following low connected strokes are too dense to distinguish e from onc securely. The blind alors has no supporting separate a/l sequence.')]:
    r['doubts'].append(dict(place=place,reading=reading,alternatives=reading,confidence='low',reason=reason,crop=f'crops/{pg}_blind_{box}.png',box=b[box]['coordinates']))
for d in r['decisions']:
    if d['id']=='M0662':d.update(confidence='medium',ink=changes['C01']['evidence'])
for x in r['inventory']:
    if x['element']=='E02':x['first_words_or_objects']='Le cas ou V'
    if x['element']=='E09':x.update(first_words_or_objects=r'\unsure{disposition}',position='right margin, entire cancelled sequence y540–578')
    if x['element']=='E11':x['first_words_or_objects']='(63) V_J^L def = V_J cap X_L^*'
    if x['element']=='E17':x['first_words_or_objects']=formula
    if x['element']=='E23':x['first_words_or_objects']=r'\unsure{de|donc}'
r['inventory']=[x for x in r['inventory'] if x['element']!='E10']
for d in r['deletion_insertion_review']:
    if d['item']=='header':d['reading_status']='Blind review resolves Le cas ou V; cancellation unchanged.'
    if d['item']=='right-margin d’où':d.update(item='right-margin cancelled disposition',attachment='One connected canceled word after de bandes; the former two-word segmentation is withdrawn.',reading_status='Disposition is favoured; crossed middle letters uncertain.')
    if d['item']=='left-margin cancelled formula':d['reading_status']='Blind review restores superscripts and narrow NB / first-L doubts. See final crop adjudication.'
    if d['item']=='other raised material':d['state']='Unaccented def is above the equality; subset L is raised after L_0. Neither is cancelled.'
r['deletion_insertion_review']=[x for x in r['deletion_insertion_review'] if x['item']!='right-margin second cancelled word']
r['notes']+='\n### Blind crop adjudication\n\nThe canceled header is Le cas ou V, with unaccented ou. The right cancellation is best read as one uncertain disposition, replacing the former two-word segmentation. The slanted canceled identity has L/L-prime superscripts and J/J-prime subscripts; its initial NB and first raised L remain uncertain. The label of (63) is unaccented def. The written mino- / rent line division is restored. Three certainty-only doubts are added for compressed element endings and the isolated de/donc fragment; the old certified de-versus-donc change is withdrawn. The arrow under lim in (62) is retained at medium confidence after full-formula reinspection. No mathematical test determined any of these readings.\n\nThe neutral boxes omit a short stretch between B17 and B18: ramené au cas de bandes dans la relation. It contains no disputed word, number, revision, or other mandatory blind target and was read in the complete first pass. B06 clips the tall f; the existing upper half was reopened to inspect the space above the label, without making a new crop.\n'
r['hand_log'].append(dict(habit='A superscript may remain readable above a dense cancellation even when the baseline is obscured.',places='Left cancelled identity below the inclusion diagram',scope='Both raised L forms and the final L cap L-prime were reread with the whole formula.',witness_errors='The first pass and C omitted these superscripts; the blind reading recovered them.'))
put('B02',changes['C28']['evidence'],header)
put('B03',changes['C01']['evidence']+' The gap after pro is not larger than internal pen lifts and no separator is written; retain provoisinage. Display wrappers, index placement and tag syntax do not add source text; retain the number at the left.')
put('B04','The tall crossed/looped t and second descending p support protopos. There is no long langage sequence; the word matches the marginal protopos.')
put('B05',changes['C04']['evidence']+' The separate K and caret replace J-prime; bandes has the low a/n and raised d, not b.o.-ens. Both argument stars have radial strokes; the single black sloping wedge is setminus, not a two-rule equals. The initial pour is overlapping body text already represented above. Margin wrapper and spacing differences add no text.',b['B05']['first'].replace(oldright,right))
put('B06','The connected def label has no acute above e; the existing upper half confirms this beyond the clipped top edge. The equality, indices, star and final comma agree. Tag and display wrappers are equivalent.',b['B06']['first'].replace('déf','def'))
put('B07','The slanted word has pro, a tall t, a second descending p and terminal os: protopos, not problème. The following raccord is clear. The extra diagram fragment is overlap with B09 and is already transcribed there; its final subscript is L. The margin wrapper is representational.')
put('B08','The cropped left edge preserves the accented où. The following word ends in a separate x-like mark, hence deux; bandes has the b and d ascenders, not b.-ens. After Par the connected sequence has an x and later tall l, hence exemple rather than contre. The next line begins on and continues retrouve, without a separate comma.')
put('B09','All three rightward objects and the lower object are present. The lower subscript has a hooked return and no bilateral I foot, hence J. The initial prose is overlap with B07. Spacing options and line breaks are layout only.')
put('B10','Both raised and lowered J, the equality, radial star and left-hand64 agree. Only display/tag syntax differs.')
put('B11',changes['C10']['evidence']+' The vertical arrow and lower V at the top of the box overlap B09 and are already present; do not duplicate them.',formula)
put('B12','The raised open inclusion curve is followed by an angular L; it is not an ordinal1. The long following curve may be l or a closing parenthesis, so retain the narrow existing l’ens/parenthesis doubt. The short high stroke after it is an apostrophe; no extra full word un is established.')
put('B13','The first element ending is compressed and shorter than the later full word, so add a local élém/élément doubt. The next l’ens has a looped l, a high apostrophe and low ens; no independent un. A detached dash ends mino at the right edge, and rent starts the next line: preserve the written division. The remaining words and punctuation agree.',b['B13']['first'].replace('élément de $J$',r'\unsure{élém|élément} de $J$',1).replace('minorent',r'mino-\\rent'))
put('B14','All four terms and all three equality signs agree; the small zero loops are subscripts on L/J as in the first reading. The only difference is number/display encoding.')
put('B15','The word after sous- has an ascender b, low a/n and tall d followed by es: bandes, not b.-ens. The two short parallel strokes after est are the written equality; math delimiters around it change representation only.')
put('B16','The closely linked co/idéal has no marked separator; retain coidéal. The word after the closing parenthesis has t, two l-like uprights and terminal es, supporting telles rather than Noter. The element endings have a low extended join and a terminal t return; the blind abbreviated alternatives are not independently established here. The paired tt stems, following est and all indices agree.')
put('B18','The words de domination, the left-hand66, angular J, curved precedence sign and L all agree. Only tag placement differs.')
put('B19','The third element ending is compressed into a low rule and final t-like upstroke: retain both élément/élémt readings locally. The other element forms and the final short él. remain as read; the four-line margin wrapper does not add text.',b['B19']['first'].replace('tt élément de $L$',r'tt \unsure{élément|élémt} de $L$'))
put('B20','The initial looped d is visible, but the following dark joins do not establish e against onc with sufficient confidence. Retain de/donc; the blind alors would require a separate initial a/l sequence not present.',r'\unsure{de|donc}')
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
(W/'second'/f'{pg}_root_crop_notes.json').write_text(json.dumps(notes,ensure_ascii=False,indent=2)+'\n')
print('081: all18 differing boxes observed; seven changed boxes, with three certainty-only doubts.')
