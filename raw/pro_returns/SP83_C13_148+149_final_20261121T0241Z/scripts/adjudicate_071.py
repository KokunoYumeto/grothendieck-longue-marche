from pathlib import Path
import csv,json,hashlib
from datetime import datetime,timezone
R=Path(__file__).resolve().parents[1];p='148_scan071'
assert hashlib.sha256((R/'second'/f'{p}_second.tsv').read_bytes()).hexdigest()=='b6a9e60c0590b3339abfaba5f384c083083833efd6711eed0ff4fbf4b1ed26f6'
C={x['box']:x for x in json.loads((R/'second'/f'{p}_comparison.json').read_text())}
E={
'B01':'The title ends with the low e and returning terminal s run of Groupoïdes. The underline lies under the ending of Teichmüller and continues rightward. The first wording and underline are retained; the second omission of underlining is not supported.',
'B02':'The category enclosure has the two upright sides and lower stroke, with no visible joining upper stroke; the first open-top tracing is retained. The heading, final point, and two underlined caption lines otherwise agree. The existing first_heading crop was also inspected. The second closed boxed macro would regularize the visible enclosure.',
'B04':'The empty-set form has an oval crossed by a long oblique descending stem, consistent with the phi form retained in both occurrences on this page. The old word before orienté is covered through its middle. Its final tall surviving stroke supports the first orient candidate, while the short run admits the independent non candidate. Both are retained as alternatives, without resolving the cancellation. Text and subcase order otherwise agree.',
'B05':'The retraced numeral has a curved diagonal upper part and low foot, favouring 2 but not securely excluding 1. The first 2/1 doubt remains. The category enclosure has a short upper stroke and an open upper-right join; the first tracing retains this gap. The struck Vari, underlined Variantes, pair isomorphism arrow and orientation sentence agree.',
'B06':'The complete functor, cancelled target and three-line group description were read. The label has superposed crossing upper strokes, a small left double bend and a heavy long hooked return. Neither chi/epsilon nor the independent fraktur-s suggestion can be isolated securely, so the latter is added as an alternative. The extended cancelled target includes a B-like first outline and lower brace/plus/loop strokes; its uncertain geometric transcription is retained instead of asserting a complete symbolic identity. The old ponctuel has the p ascender and n-c-t/u-e-l traces around the strike; the final l is incompatible with transitif. The live word groupe is written as a full run, and the signature caption lacks a closing parenthesis.',
'B07':'The old noyau and separate est are crossed; the tall t and short preceding run of est remain visible. The parenthetical opening is a curved stroke followed by a compressed low run: the first la/equality doubt is retained with en as an additional possible reading. The live fibre sentence and its unpunctuated final category agree.',
'B08':'The complete dark lower block and the existing definition, name and NB crops were read; three focused audit details were also inspected. Above cancelled fermée the replacement reads compacte: the left tall descender belongs to the old f, and the live c/o, m, p and c/t/e run provides no separate pas. The replacement noun has dé-vi-ss-age and the two later adjectives have dé-vi-ss-é; divisé lacks the visible doubled s sequence. The isolated crossed 6-like cluster is retained graphically without assigning a numeral. The revised D over the old S-like ink, point after de, quotation marks, and omitted dot after homéom remain as in the first reading. In the NB cancelled word, an internal raised hooked stroke favours an l-containing inclusion over immersion, but the strike masks too many middle letters for resolution: inclusion leads with immersion retained. The raised imm. ouverte is outside the lower parentheses. Two short parallel uprights below the left category form a vertical equality, without an arrowhead. Both empty-set signs share the phi form. The pale nested contours and brown dots under the dark text remain classified as show-through, not an additional recto figure; no exact verso match is claimed. The final category really has S, not normalized D.',
'B09':'The folio is 70: crossed descending 7 followed by a closed oval zero. Bare digits versus the mspage wrapper is only markup.'}
V={
'B04':C['B04']['first'].replace(r'\unsure{orient}',r'\unsure{orient|non}'),
'B06':C['B06']['first'].replace(r'\unsure{\chi|\varepsilon}',r'\unsure{\chi|\varepsilon|\mathfrak{s}}'),
'B07':C['B07']['first'].replace(r'\unsure{la|$=$}',r'\unsure{la|$=$|en}'),
'B08':C['B08']['first'].replace(r'\text{immersion pleine}',r'\text{\unsure{inclusion|immersion} pleine}')}
pp=R/'pages'/f'{p}.tex';s=pp.read_text()
for b,v in V.items():assert C[b]['first'] in s;s=s.replace(C[b]['first'],v)
pp.write_text(s)
D={b:dict(choice='keep_first',viewed=True,evidence=e) for b,e in E.items()}
for b,v in V.items():D[b].update(choice='reading',reading=v)
(R/'second'/f'{p}_main_decisions.json').write_text(json.dumps(D,ensure_ascii=False,indent=2)+'\n')
rp=R/'records'/f'{p}.json';r=json.loads(rp.read_text())
subs={r'\unsure{orient}':r'\unsure{orient|non}',r'\unsure{\chi|\varepsilon}':r'\unsure{\chi|\varepsilon|\mathfrak{s}}',r'\unsure{la|$=$}':r'\unsure{la|$=$|en}',r'\text{immersion pleine}':r'\text{\unsure{inclusion|immersion} pleine}'}
for x in r['changes']:
 for a,b in subs.items():x['final']=x['final'].replace(a,b)
 if x['id'].endswith('-09'):x['evidence']=E['B04']
 if x['id'].endswith('-28'):
  x['evidence']='The raised imm. ouverte is outside the parentheses around the cancelled lower phrase. The cancelled first word now remains doubtful as inclusion/immersion; the placement itself is clear.'
 if x['id'].endswith('-29'):
  x.update(final=r'\unsure{inclusion|immersion}',diff_c=True,confidence='low',kind='misread word',error_kind='Words',crop=f'crops/{p}_main_audit_nb_old_word.png',box=[1170,1710,1610,1810],evidence='A raised hooked internal stroke favours the l-containing inclusion, also proposed independently. The strong horizontal cancellation conceals most intervening letters. The earlier confident immersion is not justified; inclusion leads while immersion remains an explicit alternative. The following pleine has a clear descending p and high looped l.')
for x in r['doubts']:
 for a,b in subs.items():x['reading']=x['reading'].replace(a,b)
 if x['place']=='M0949':x.update(alternatives=r'\chi; \varepsilon; \mathfrak{s}',reason=E['B06'])
 if x['place']=='old orient candidate':x.update(alternatives='orient; non',reason=E['B04'])
 if x['place']=='fibre parenthetical opening':x.update(alternatives='la; =; en',reason=E['B07'])
r['doubts'].append(dict(place='NB cancelled first word',reading=r'\unsure{inclusion|immersion}',alternatives='immersion',confidence='low',reason='The internal raised hook favours an l, but the horizontal strike masks the middle letters. Neither full candidate is resolved.'))
for x in r['decisions']:
 if x['id']=='M0949':x.update(reading=r'\unsure{\chi|\varepsilon|\mathfrak{s}}',evidence=E['B06'],crop=f'crops/{p}_second_B06.png')
r['notes'][1]['text']=r['notes'][1]['text'].replace('cancelled full-immersion phrase','cancelled inclusion/immersion pleine phrase, whose first word remains uncertain')
r['notes'].append(dict(id=p+'-N-audit',text='The independent second reading was frozen before comparison. Eight unequal boxes were visually adjudicated. The second suggestions pas compacte and divisé are not supported by the local lettering. The revised NB cancelled word leads with inclusion but remains doubtful against immersion; its uncertainty prevents treating the prose as a secure statement of a full immersion. Added alternatives in other unresolved runs do not add witness-change rows. The pale lower contours remain treated as show-through after independent review; their exact source is unproved.'))
details=R/'second'/f'{p}_main_audit_details.json';ds=json.loads(details.read_text())
for x in ds:x['viewed']=True
details.write_text(json.dumps(ds,ensure_ascii=False,indent=2)+'\n')
extra=[f'crops/{p}_{n}.png' for n in ['first_heading','triple_definition','definition_words','nb','signature_functor','fibre']]+[x['path'] for x in ds]
r['second_main_review']=dict(viewed_boxes=list(E),reviewed_at=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),decisions=f'second/{p}_main_decisions.json',additional_existing_crops_viewed=extra,lossless_display_path=f'transport/{p}_second_B08.webp')
r['supporting_evidence']+=ds
r['main_reader_crops']=list(dict.fromkeys(r.get('main_reader_crops',[])+extra))
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
