from pathlib import Path
import json
W=Path(__file__).resolve().parents[1];pg='150_scan088';rp=W/'records'/f'{pg}.json';r=json.loads(rp.read_text());c=json.loads((W/'second'/f'{pg}_comparison.json').read_text());b={x['box']:x for x in c['results']};notes={}
dbd=r'\mathord{\cdot}\mathord{-}\mathord{\cdot}';db=r'\mathord{\cdot}\mathord{-}';dd=r'\mathord{-}\mathord{-}';ddb=r'\mathord{\cdot}\mathord{\cdot}\mathord{-}'
reps=[(r'(j_1\ldots j_p\ l_1\ldots l_q)',r'(j_{\unsure{1|q}}'+dbd+r'j_p\ l_1'+db+r'l_q)'),
 (r'i_{\unsure{0|q}}\ldots i_p',r'i_{\unsure{q|0}}'+dd+r'i_p'),
 (r'l_1\ldots l_q\in L',r'l_1'+dd+r'l_q\in L'),
 (r'\Sigma_{j_1\ldots j_p\,l_1\ldots l_q}',r'\Sigma_{j_1'+dd+r'j_p\,l_1'+dd+r'l_q}'),
 (r'\Sigma_{l_1\ldots l_q}',r'\Sigma_{l_1'+ddb+r'l_q}'),
 (r'\Sigma_{j_1,\ldots,j_p}',r'\Sigma_{j_1,'+db+r',j_p}'),
 ('(dans une catégorie isotopique convenable)','(d.s une catégorie isotopique convenable)')]
p=W/'pages'/f'{pg}.tex';s=p.read_text()
for a,z in reps:assert s.count(a)==1,(a,s.count(a));s=s.replace(a,z)
p.write_text(s);(W/'records'/p.name).write_text(s)
ch={x['id']:x for x in r['changes']};r['changes']=[x for x in r['changes'] if x['id']!='C01']
ch['C02'].update(final=r'i_{\unsure{q|0}}'+dd+r'i_p\in J',evidence=ch['C02']['evidence']+' The loop and long right return favour q, but the ambiguity with0 remains. The continuation has two short horizontal strokes.',crop=f'crops/{pg}_blind_B02.png',box=b['B02']['coordinates'])
ch['C05'].update(final=r'\Sigma_{j_1,'+db+r',j_p}',against_C=True,evidence='The lower index has a comma after j1 and a comma before jp. Between them lie one separate point and one short horizontal rule, not three points.',crop=f'crops/{pg}_blind_B04.png',box=b['B04']['coordinates'])
ch['C07']['final']=ch['C07']['final'].replace('(dans','(d.s')
newrows=[
 ('C22','(80), j continuation in the parenthesized flag',r'j_{\unsure{1}}\ldots j_p',r'j_1\ldots j_p',r'j_{\unsure{1|q}}'+dbd+r'j_p','B02','The continuation consists of a point, one short horizontal rule, and a second point. The separate index uncertainty is recorded in doubts.'),
 ('C23','(80), l continuation in the parenthesized flag',r'l_1\ldots l_q',r'l_1\ldots l_q',r'l_1'+db+r'l_q','B02','One separate point and one short horizontal rule lie between l1 and lq; there is no third mark.'),
 ('C24','(80), right-hand i continuation',r'i_0\ldots i_p',r'j_1\ldots j_p',r'i_{\unsure{q|0}}'+dd+r'i_p','B02','Both continuation marks are short horizontal strokes, visibly wider than the adjacent i dots. The bases remain i.'),
 ('C25','(80), right-hand l continuation',r'l_1\ldots l_q',r'l_1\ldots l_q',r'l_1'+dd+r'l_q','B02','Two separated short rules connect the endpoints, matching the upper right-hand condition.'),
 ('C26','(81), upper-left source j continuation',r'j_1\ldots j_p',r'j_1\ldots j_p',r'j_1'+dd+r'j_p','B04','The source j-index group contains two separated short horizontal strokes.'),
 ('C27','(81), upper-left source l continuation',r'l_1\ldots l_q',r'l_1\ldots l_q',r'l_1'+dd+r'l_q','B04','The following l-index group also contains two separated short rules, not three dots.'),
 ('C28','(81), right-hand target continuation',r'l_1\ldots l_q',r'l_1\ldots l_q',r'l_1'+ddb+r'l_q','B04','The target has two separate points followed by a short horizontal rule; all three marks are distinct.'),
 ('C29','Encircled insertion, abbreviated opening word','dans','dans','d.s','B05','After the initial d there is a detached dark point, then a separate short s-like return. The full a/n sequence is not written. Preserve the short form d.s and expand it only in the abbreviation list.')]
for ident,place,C,H,final,box,why in newrows:
 r['changes'].append(dict(id=ident,place=place,C=C,H=H,final=final,evidence=why,crop=f'crops/{pg}_blind_{box}.png',box=b[box]['coordinates'],confidence='high',kind='abbreviation expanded or spelling modernised' if ident=='C29' else 'misread symbol or index',error_kind='8 abbreviation/spelling' if ident=='C29' else '1 symbols/indices',against_C=True,against_H=True,consequential=False,marked_in_H=False,phase='blind audit'))
for d in r['decisions']:
 if d['id']=='M0705':d.update(decision='undecided',reading=r'\unsure{1|q}',ink='The small capped upright is heavily retraced at its top, leaving a tiny loop-like opening. The larger q in the right-hand condition makes that alternative possible; the earlier certainty for1 is withdrawn.',crop=f'crops/{pg}_blind_B02.png',box=b['B02']['coordinates'],confidence='medium')
 if d['id']=='M0706':d.update(reading=r'i_{\unsure{q|0}}'+dd+r'i_p',ink='The two bases are short dotted i forms, unlike the descending j at left. The first subscript has a loop and long right return favouring q, but0 remains possible. Both continuation strokes are horizontal rules.',crop=f'crops/{pg}_blind_B02.png',box=b['B02']['coordinates'])
for d in r['doubts']:
 if 'first subscript in right-hand' in d['place']:d.update(reading=r'i_{\unsure{q|0}}',alternatives=['q','0'],reason='The loop and descending right return favour q; the heavy small form still leaves0 possible. The i bases and two horizontal continuation rules are clear.')
r['doubts'].append(dict(place='(80), first j subscript in the parenthesized flag, M0705',reading=r'j_{\unsure{1|q}}',alternatives=['1','q'],confidence='medium',reason='The small upright has a heavily retraced cap with a minute loop-like opening. Its shape does not securely exclude q; restore local uncertainty.',crop=f'crops/{pg}_blind_B02.png',box=b['B02']['coordinates']))
for x in r['inventory']:
 if 'first_words_or_objects' in x:
  for a,z in reps:x['first_words_or_objects']=x['first_words_or_objects'].replace(a,z)
r['abbreviations'].append({'form':'d.s','expansion':'dans','place':'Encircled insertion after un sens','note':'A detached point lies between d and the final s-like short stroke; expansion is not placed in the transcription.'})
r['notes']+='\n### Blind reading corrections\n\nThe continuation marks in80–81 vary locally: the main flag has point–rule–point and point–rule, the right-hand conditions have two rules, the diagram source has two rules in each group, its target has two points then a rule, and its lower object has point–rule between commas. These replace normalized ellipses. The first j index in80 is again locally uncertain1/q; the right-hand i index favours q over0 but remains uncertain. The encircled insertion begins with the abbreviation d.s, not the expanded dans. Its attachment after un sens and the word convenable are retained. The revision reads fibrations above crossed structures, and both later occurrences of côniques have visible circumflexes. The final prose reads et dans le cas équisingulier; the blind en équisingularité is not supported by the ending or the word division.\n'
def put(box,why,changed=False):
 notes[box]=dict(viewed=True,evidence=why)
 if changed:
  f=b[box]['first']
  for a,z in reps:f=f.replace(a,z)
  notes[box].update(changed=True,final=f)
put('B02','The entire exact80 crop was viewed at2600 pixels. The first j index has a retraced cap with a minute loop-like opening, so restore1/q uncertainty. The following l1 is retraced but its looped l and separate upright1 remain traceable. The right-hand bases are i, not j; their first index favours q but0 remains possible. Read the literal continuations: dot-rule-dot after j, dot-rule after l in the flag, and two rules in each right condition. The three right conditions have no supplied commas; p,q and the inequality agree.',True)
put('B03','The canceled word has remaining en-like low joins, an i dot and the taller t region; keep uncertain ensuite rather than replace all candidate letters by illegible. The following article has a looped d ascender and an ending s return, supporting des rather than les.')
put('B04','The source has two rules in each index group. The right target has two dots and a rule. The bottom object has comma, dot-rule, comma between its j endpoints. The horizontal shaft has a hook and one head; the vertical shaft has one downward head. All three objects,81 and their layout agree.',True)
put('B05','The full exact crop shows d, a detached point and a short s return: d.s. The following une, catégorie, isotopique and convenable are traceable, including the final b/l stems. The enclosing curve ends in a leader toward the line after un sens, so keep it as an attached insertion. The wrapper margin in the blind reading would not preserve that attachment.',True)
put('B07','After the d loop and e there is a short separate terminal s return before the wide word gap. Retain des rétractions, with the final s of rétractions also visible.')
put('B08','The first letter has an ascender loop much taller than the low e/s run, supporting les rather than car. The final downturned return matches s, and both Sigma subscripts and the hooked headed arrow agree.')
put('B10','The raised live word begins with tall f, a dotted i and a separate b stem, followed by rations; keep fibrations. Structures below is crossed. The short higher de ri.-like addition is separately crossed and remains uncertain. The lower crossed adjective has a detached circumflex over o and no extra a/n sequence of canoniques. The upper structure/Sigma fragment is overlap with the preceding live line.')
put('B11','The relation between dispose and des is two independent horizontal bars. The following article ends in an s return. Côniques has a visible circumflex and the compact n/i/q/u/e/s run, not canoniques. The lower modérée fragment is overlap with the following line.')
put('B12','The full exact crop at2600 pixels shows the looped d at the upper right, followed by the low ans group and tall l of le. Cas starts the next line. The following word ends in l/ier, with no final accented té; keep le cas équisingulier. The boundary fragments locales, Quand on dispose, ce qui and il est plus commode are already transcribed in the complete paragraph.')
put('B13','The two short opening strokes and paired closing strokes around anodine, followed by a closing parenthesis and comma, agree. Use the required two-backtick/two-apostrophe convention instead of Unicode curly quotes; no textual change.')
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');(W/'second'/f'{pg}_root_crop_notes.json').write_text(json.dumps(notes,ensure_ascii=False,indent=2)+'\n')
# Correct stale inventory labels after the earlier083 audit, without touching sealed readings.
p83=W/'records/150_scan083.json';r83=json.loads(p83.read_text())
for x in r83['inventory']:
 if x['element']=='restricted union':x['first_words_or_objects']='(69) '+x['first_words_or_objects']
 if x['element']=='cancelled ending of (68)':x['first_words_or_objects']='et + uncertain où/aussi/ainsi under cancellation'
 if x['element']=='cancelled word after drapeau':x['first_words_or_objects']='de / dont / donc (unresolved)'
p83.write_text(json.dumps(r83,ensure_ascii=False,indent=2)+'\n')
print('088: all10 differing boxes observed; three changed boxes.')
