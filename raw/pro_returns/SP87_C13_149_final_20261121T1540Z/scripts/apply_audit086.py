from pathlib import Path
import json,csv
w=Path('/workspace/scratch/b8c6ff258063/SP87_C13_149_work');p='149_scan086';rp=w/'readers'/p/'report.json';r=json.loads(rp.read_text());pp=w/'pages'/f'{p}.tex';t=pp.read_text()
t=t.replace(r'U=X\setminus T',r'U\unsure{=|:}X\setminus T').replace(r'E_{U_\eta}',r'E_{U_K}').replace(r'\overline m',r'=');pp.write_text(t)
for c in r['changes']:
 if c['place']=='C086_09_eta_subscript':c.update(final=r'E_{U_K}',against_c=True,against_h=False,confidence='medium',evidence='Blind audit and cross-leaf comparison: the tiny index has a high left limb, a rising branch and a short retraced right foot. It matches the compressed K forms in 088/090/093/096; the clear eta on 102 instead has a longer descending left-returning tail. The immediately preceding full-size K alone was an insufficient control in the first pass. Read K, without changing the visibly headless second connector.',crop='second_149_scan086_B008.png',box=[805,1250,1380,1405])
 if c['place']=='C086_11_meme_short_form':c.update(final='=',against_c=True,confidence='medium',evidence='The lower stroke has a short hooked entry followed by one level stroke, with a separate upper horizontal. There are no independent m humps. This is the same written equals short form as 083 and 091, distinct from the unmistakable barred capital M on 097. Retain the written = without expanding même.',crop='second_149_scan086_B009.png',box=[300,1525,855,1658])
for m in r['marks']:
 if m['id']=='M1236':m.update(decision='other',reading='=',evidence='Two level strokes; the hooked entry of the lower one does not form separate m humps. Same equals short form as 083/091, distinct from barred M on 097.',crop='second_149_scan086_B009.png',box=[300,1525,855,1658],confidence='medium')
for h in r['hand_observations']:
 if 'flattened m' in h['habit']:h.update(habit='The equals short form for même may have a hooked entry on its lower stroke.',evidence='The two separated strokes in second_149_scan086_B009.png match 083/091; the lower one remains level after its entry, without m humps.',witness_errors='C offered barred m or superscript m over equals; H expanded même. The source has =.')
r['unresolved'].append(dict(place='opening definition sign',reading=r'\unsure{=|:}',alternatives=['=',':'],confidence='medium'))
r['notes'] += '\n\nBlind adjudication: the opening definition sign has two extremely short, partly faded horizontal traces with dark right ends; retain = first but mark colon as an alternative. The nested generic-fibre index is K after comparison of its short branched foot with 088/090/093/096 and the longer eta return on 102; the mathematics identifies the notation but does not supply a missing stroke. The written même short form is =, not barred m. The final phrase remains fibré en, with a tall f, looped b and accented e, not générique. All ten token-different boxes were inspected.\n'
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
cs={x['box']:x for x in csv.DictReader((w/'second'/f'{p}_comparison.tsv').open(),delimiter='\t')}
e={
'B001':'The two tiny traces after U have faint short leftward shafts and dark right ends. Equals is preferred, but their near-point length warrants colon as an alternative. Between X and T the descending oblique stroke remains a setminus, distinct from the level connector later on the page.',
'B004':'Under the strike there is an opening c-like curve and compressed low middle turns; there is no independently legible tall d and dotted i sequence establishing codim. Keep the existing doubtful car. rather than resolve the struck letters.',
'B007':'The left I has both serifs and its s-prime is clear. E is the ordinary cursive E throughout this passage. Dark K overwrites lighter upper and lower S/s curves; no independent old prime can be isolated. Preserve the uncertain old subscript and replacement K.',
'B008':'The middle nested index has the short rising branch and retraced right foot of the compressed K on 088/090/093/096, rather than the long returning eta tail on 102. Change eta to K. The first connector has an angled head; the second has only a level shaft and thickened end and remains a dash. Cursive E is not a separate alphabet here.',
'B009':'The first sign has two strokes; the lower one is level after a hooked left entry and has no m humps, as on 083/091. Change it to =. The word before L_i has a tall looped l followed by low joined e/s turns; it does not show the separate branching K and e/r of Ker. Keep les.',
'B011':'The cancellation crosses the low n/u group and the two tall looped l stems, but their tops and the final small e survive distinctly. Retain nulle under deletion. Triviale, its live point, Considérons and the tall l in alors agree.',
'B012':'A large opening parenthesis precedes the small c loop and descending f. It is not a capital C standing alone before f. The following suite exacte and (7), agree, and there is no independent stop after cf.',
'B014':'Jauge has an initial descending j and a later loop with g descender, unlike anneau. The O has its visible underline; its first index is a larger S followed by the smaller s. At the right the tall looped f and b, accent over e, and separate en are visible: fibré en, not générique. Retain the complete first reading.',
'B015':'Both readings give 85 from the two-loop 8 and top-bar/lower-curve 5. Its lower-edge position is foliation; retain the margin wrapper.',
'B017':'Both readings give g_i(s)=f(s); the left g has its long descender, the index i is short and dotted, and two equality strokes are distinct. Keep the display placement from the whole-page layout.'}
d={k:dict(evidence=v,changed=k in ['B001','B008','B009']) for k,v in e.items()}
d['B001']['final']=cs['B001']['first'].replace('U=',r'U\unsure{=|:}')
d['B008']['final']=cs['B008']['first'].replace(r'\eta','K')
d['B009']['final']=cs['B009']['first'].replace(r'\overline m','=')
(w/'review'/f'{p}_audit_decisions.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
