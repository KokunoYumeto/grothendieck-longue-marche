from pathlib import Path
import json
w=Path(__file__).resolve().parents[1];page='147_scan060';c={e['box']:e for e in json.loads((w/'second'/f'{page}_comparison.json').read_text())}
ev={
'B01':'The first word has a distinct dense crossing at its beginning before the recoverable multiplicités; retain the illegible deleted prefix and the live word. Modu- / laires is a physical line division, not a lexical hyphen. The small M has a separate hat and G, and its curved guide attaches after modulaires, before de dim2.',
'B02':'The five rows,29/74, M hats/exclamations, numerical indices, right arrows, double-struck Z, fraktur S, live I hats and unmatched opening parenthesis agree. The first repetition mark is one continuous stroke and the two lower marks are separated dashes; the first encoding --- denotes repetition and is not expanded into words. On the focused cancellation crop the product-like top bar/legs and alpha-in-opening-brace-alpha-zero-comma survive. No second alpha-one or closing brace is independently visible after that comma. Narrow the doubtful cancelled product to this actual fragment. The small crossed subscript still admits hat-I, and the small crossed superscript remains4/*; the alternatives suggested by the blind reader are not established by separate surviving strokes.',
'B03':'The small crossed item after underlined NB is looped below but too overdrawn to establish a capital D; retain the first tentative à. Both bare-exponent hat-M factors, Gamma, cancelled opère and raised s’envoie are visible. Only the degree-closing-parenthesis delimiter scope otherwise differs.',
'B04':'Gamma, rightward shaft/end, double-struck Z/2, separate multiplication dot, both S4 and the lower prod.1/2 direct agree. The lower label has no connecting underbrace; the first array preserves its vertical placement. The isolated distant tick remains unassigned punctuation, as already documented.',
'B05':'The main words and the hat-M insertion with G agree. On the focused crop the lower cancelled bodies are obscured enough to permit qui sont or savoir; retain both. The upper first short group has a dot and low joined strokes near the long insertion guide, leaving ils/qui uncertain; the last d-led group has a compressed low tail leaving deux/donc uncertain. Sont and the terminal colon are clear. Mark those two short groups rather than certify either reader’s phrase.',
'B06':'The short upper word is cas: a curved entry and low a/s-like bodies; the long descending stem crossing nearby belongs to the l of the lower word, not a p that would establish plus. The lower word has the ending s-like hook before the exclamation. Retain (cas élémentaires!).',
'B07':'Both M hats and exclamation dots, the two numerical pairs, number75, rightward map and bare I-alpha-zero agree. Trivialt is visibly short, followed by a comma. The differences are delimiter placement and math wrappers only.',
'B08':'The group before74 has a d loop and a low e-like return, without distinct a/n/s bodies for dans; retain de. Three quotation groups are visible, but the middle direction remains compressed and ambiguous, so do not resolve its opening/closing doubt. Both decorated M formulas and terminal point agree.',
'B11':'After pour the article has a looped l with a low e ending but no separate terminal s, supporting le cas. The later de/des tail remains ambiguous, so retain that doubt; dim. and plural modulaires, inequality2 and J’ai agree.',
'B13':'The small inserted discrets and analytic parenthesis, and the main impliqués dans ces cas, agree. The donner- sequence is clear, but its separated compressed final strokes do not expose every letter. Donnera is plausible, yet the crop does not certify it against the existing donnerait/donnera doubt; keep the first qualified reading.'}
d={b:{'root_viewed':True,'changed':False,'evidence':e} for b,e in ev.items()}
old=r'\deleted{\unsure{\prod_{\alpha\in\{\alpha_0,\alpha_1\}}}}';new=r'\deleted{\unsure{\prod_{\alpha\in\{\alpha_0,}}}'
d['B02'].update(changed=True,final=c['B02']['first'].replace(old,new),crop=f'{page}_second_root_B02_cancel.png')
oldphrase=r"\deleted{\unsure{qui sont}}\inserted{ils sont deux :}";newphrase=r"\deleted{\unsure{qui sont|savoir}}\inserted{\unsure{ils|qui} sont \unsure{deux|donc} :}"
d['B05'].update(changed=True,final=c['B05']['first'].replace(oldphrase,newphrase),crop=f'{page}_second_root_B05_words.png')
(w/'second'/f'{page}_root_decisions.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
p=w/'pages'/f'{page}.tex';t=p.read_text()
for a,b in [(old,new),(oldphrase,newphrase)]:assert a in t;t=t.replace(a,b,1)
p.write_text(t)
p=w/'reviewed'/f'{page}.json';r=json.loads(p.read_text());ch=next(x for x in r['changes'] if x['id']=='060-04');ch.update(final=new,evidence=ev['B02'],crop=f'{page}_second_root_B02_cancel.png',box=[1150,195,1460,385])
ch=next(x for x in r['changes'] if x['id']=='060-15');ch.update(final=r'\deleted{\unsure{qui sont|savoir}}',evidence=ev['B05'],crop=f'{page}_second_root_B05_words.png',box=[1300,975,1675,1128],confidence='low')
ch=next(x for x in r['changes'] if x['id']=='060-16');ch.update(final=r'\inserted{\unsure{ils|qui} sont \unsure{deux|donc} :}',evidence=ev['B05'],crop=f'{page}_second_root_B05_words.png',box=[1300,975,1675,1128],confidence='low')
for x in r['doubts']:
 if 'large cancelled row-3' in x['place']:x.update(reading=new,reason=ev['B02'],alternatives='Product-like fragment only; following alpha-one and closing brace are not visible and are no longer supplied')
 if x['place']=='Before (75), cancelled words after dim 1':x.update(reading=r'\deleted{\unsure{qui sont|savoir}}',reason=ev['B05'],alternatives='qui sont; savoir',confidence='low')
r['doubts'].append({'place':'Interlinear replacement before(75)','reading':r'\unsure{ils|qui} sont \unsure{deux|donc} :','alternatives':'ils/qui and deux/donc','confidence':'low','reason':ev['B05']})
r['unresolved'].append('Before(75), short upper replacement groups ils/qui and deux/donc; lower cancellation qui sont/savoir.')
r['notes'][-1]+=' The completed blind audit narrows the large cancelled product to its visible alpha-zero/comma fragment; the full first-stage index in the frozen first TSV is retained as historical evidence, not current text. The crowded interlinear replacement before(75) now marks its short-word uncertainties.'
r['notes'][-1]=r['notes'][-1].replace('the blind independent reading remains pending.','the blind independent reading has now been adjudicated.')
r['root_review_notes']+=' All ten differing boxes and two focused crops personally viewed; the cancelled product was not completed from the expected two-element index set.'
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
p=w/'workflow/root_audit_views.json';v=json.loads(p.read_text());v['60']={'crops':[f'{page}_second_{b}.png' for b in ev]+[f'{page}_second_root_B02_cancel.png',f'{page}_second_root_B05_words.png'],'observations':ev};p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
