from pathlib import Path
import csv,json
from datetime import datetime,timezone
R=Path(__file__).resolve().parents[1];p='148_scan058'
C={x['box']:x for x in json.loads((R/'second'/f'{p}_comparison.json').read_text())}
boxes={x['box']:[int(x[k]) for k in ('x0','y0','x1','y1')] for x in csv.DictReader((R/'second'/f'{p}_boxes.tsv').open(),delimiter='\t')}
E={
'B01':'The first digit is a single upright with an entry stroke; the second has a diagonal, crossbar and right upright: 14. The mspage wrapper records the same number.',
'B02':'The old d-like loop and ascender are covered by several overstrikes. The terminal dark hooked mass may include s, so de remains primary but des is added as an explicit alternative. Neither is resolved.',
'B06':'The old run is short: an oval entry, angular joined middle, one looped ascender and a separate small point. It does not expose the long -inaires continuation required for ordinaires. Ord. is preferred provisionally, with the independent sol. as an alternative. The replacement has one tall l, short i and accented e-like ending, favouring liees over libres. The closing parenthesis meets the strike at its bottom, but the curve itself is not clearly cancelled.',
'B07':'The short horizontal stroke before fois is at the height of the tall f cross-stroke and is close to that f. It is not securely a separate hyphen between cette and fois. There is no hyphen before ci. The first spacing is retained.',
'B08':'The quoted verbs, contracter, un point and decouper agree. The closing mark after gommer is a small joined stroke whose individual ticks cannot be counted securely, so one/two closing ticks are now uncertain. After the e of the first i.e there is no separate terminal point; only its exit stroke is present. The intervening point and dotted i are retained.',
'B09':'The old opening has a large I, a small c and short i, then the low e/n/c/o/r/e run ending before a comma: Ici encore, not Les or Je. Pour has a descending p and un has its two low joins. At the far end two small surviving upper traces include an a-like body and a raised accent-like stroke, now tentatively a-grave rather than wholly illegible. The whole abandoned line is cancelled.',
'B10':'The word has a low a/n/o sequence, looped d, short i and n/e ending: anodine. The longer consideree does not fit those strokes. The separate en C lies above the following gap, with its curved leader returning before the dash.',
'B11':'In the cancelled tail the first tall/short joins and the following ascender are more compatible with lieu de, followed by a low marquer-like run, than with the previous bel et bien/tel et un alternatives; lieu de marquer is now a doubtful leading reading. The small a after the descending y falls low, directly above the next Sigma, and is part of il y a rather than a cc index. The replacement marque remains live despite its q descender crossing the lower strike. The raised verbal replacement is kept separately from the continuing live i.e. formula: the image does not establish that the latter was itself an added revision. Phi keeps its oval/stem form. After the next dash the descending first letter and short u/i support qui, not sauf. The terminal s in choses remains.',
'B12':'The first short group ends with a hooked s and an independent point: ens. The next word has a tall descending f and two short dotted i positions around the low n, supporting fini rather than fois. The following comma is separate from the large looped-over closing parenthesis. The first reading is retained.',
'B13':'The faint first group has a small e-like entry and low n run. The second has p, a short r-like middle, accented e-like body and final s; there is no tall l for plus. En pres remains doubtful, while the plus alternative is dropped. The clipped descender does not justify supplying a longer phrase.',
'B14':'The first group and raised mark still admit r-e-acute or i-n. The following low open v-like group, small e and compressed r/s/e/r run support reverser/inverser more than recreer/recrire. No quotation ticks surround the verb. The existing uncertainty is retained.',
'B18':'The first numeral has an open lower bowl and upper bar; the second has an upper bar, descending stroke and crossing bar: 57. The number agrees.'}
D={b:dict(choice='keep_first',viewed=True,evidence=e) for b,e in E.items()}
repls={
'B02':[(r'\unsure{de}',r'\unsure{de|des}')],
'B06':[(r'\unsure{ordinaires}',r'\unsure{ord.|sol.}')],
'B08':[("``gommer''",r"``gommer\unsure{''|'}"),('i.e. de contracter','i.e de contracter')],
'B09':[(r'\illegible{1}',r'\unsure{à}')],
'B11':[(r'\unsure{bel et bien|tel et un}',r'\unsure{lieu de marquer|bel et bien}')],
'B13':[(r'\unsure{en près|en plus}',r'\unsure{en près}')]}
pp=R/'pages'/f'{p}.tex';s=pp.read_text()
for b,rs in repls.items():
 v=C[b]['first']
 for a,z in rs:
  assert a in v and a in s,(b,a);v=v.replace(a,z);s=s.replace(a,z)
 D[b].update(choice='reading',reading=v)
pp.write_text(s)
(R/'second'/f'{p}_main_decisions.json').write_text(json.dumps(D,ensure_ascii=False,indent=2)+'\n')
rp=R/'records'/f'{p}.json';r=json.loads(rp.read_text())
def update(n,b,**kw):
 x=next(x for x in r['changes'] if x['id']==f'{p}-{n:02d}')
 x.update(evidence=E[b],crop=f'crops/{p}_second_{b}.png',box=boxes[b],**kw)
update(1,'B06',final=r'\deleted{\unsure{ord.|sol.}} \inserted{liées}',diff_c=True,kind='abbreviation expanded or spelling modernised',error_kind='Abbreviations expanded, spelling modernised',confidence='low')
update(3,'B08',final=r"``gommer\unsure{''|'}; ``découper''",confidence='medium')
update(5,'B09',final=r'Le \uline{marquage suit}. \deleted{Ici encore, pour un \unsure{à}} Mais il y',confidence='low')
update(11,'B11',final=r'où \deleted{il y a \unsure{lieu de marquer|bel et bien}} \inserted{$C$ est effectivement marqué}',confidence='low')
update(12,'B11',final=r'\deleted{il y a \unsure{lieu de marquer|bel et bien}}',diff_c=True,confidence='low')
update(19,'B13',final=r'\unsure{en près}')
for n,place,c,h,final,b,kind,err in [
 (26,'First i.e abbreviation terminal punctuation','i.e.','i.e.',r'i.e','B08','other','Other'),
 (27,'First cancelled line final surviving group',r'\illegible{1}',r'\ill{}',r'\unsure{à}','B09',r'readable ink left as \ill{}','Readable ink left as illegible')]:
 r['changes'].append(dict(id=f'{p}-{n:02d}',place=place,c=c,h=h,final=final,diff_c=True,diff_h=True,kind=kind,error_kind=err,evidence=E[b],crop=f'crops/{p}_second_{b}.png',box=boxes[b],confidence='low' if b=='B09' else 'high',marked_in_h=b=='B09',consequential=False))
for x in r['decisions']:
 if x['id']=='M0746':x.update(reading=r'\unsure{en près}',evidence=E['B13'],crop=f'crops/{p}_second_B13.png',box=boxes['B13'])
for x in r['doubts']:
 if x['place']=='Heading, cancelled preposition':x.update(reading=r'\deleted{\unsure{de|des}}',alternatives='de; des',reason=E['B02'])
 if x['place']=='Upper paragraph, cancelled edge adjective':x.update(reading=r'\deleted{\unsure{ord.|sol.}}',alternatives='ord.; sol.; short cancelled abbreviation',reason=E['B06'])
 if x['place']=='First long cancelled line, final group':x.update(reading=r'\unsure{à}',alternatives='tentative à; lower body heavily covered',reason=E['B09'])
 if x['place']=='Marked case, cancelled tail':x.update(reading=r'\unsure{lieu de marquer|bel et bien}',alternatives='lieu de marquer; bel et bien',reason=E['B11'])
 if x['place']=='Parenthesis after fini':x.update(reading=r'\unsure{en près}',alternatives='en près; faint first word and compressed middle',reason=E['B13'])
r['doubts'].append(dict(place='Closing quote ticks after gommer',reading=r"\unsure{''|'}",alternatives='two joined ticks; one stroke',confidence='medium',reason=E['B08']))
for x in r['inventory']:
 if x['element']=='E03':x['first_words_or_objects']='de / des'
 if x['element']=='E06':x['first_words_or_objects']='ord. / sol.'
 if x['element']=='E10':x['first_words_or_objects']='Ici encore, pour un, tentative à'
 if x['element']=='E13':x['first_words_or_objects']='il y a lieu de marquer / bel et bien'
 if x['element']=='E17':x['first_words_or_objects']='en près ... peut se réverser / inverser ... à l’aide du produit de cette opération'
r['abbreviations'].append({'form':'ord.','expansion':'ordinaires (tentative reading of cancelled abbreviation)'}) if isinstance(r.get('abbreviations'),list) else None
r['notes'].append(dict(id=p+'-N-audit',text='Every unequal blind-reading box was adjudicated from its crop. The old edge adjective exposes a short abbreviation, provisionally ord./sol., rather than the full ordinaires. The cancelled tail now favours lieu de marquer, without resolving every letter. The displaced low a of il y a is not a cc index above Sigma. The live anodine, ens. fini, qui, plural choses and doubtful réverser/inverser are retained against the independent alternatives. A tiny final cancelled à and closing quote count remain expressly tentative; en près is preserved without grammatical normalization.'))
r['second_main_review']={'viewed_boxes':list(E),'reviewed_at':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),'decisions':f'second/{p}_main_decisions.json'}
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
