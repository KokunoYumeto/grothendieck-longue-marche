from pathlib import Path
import json,csv
w=Path('/workspace/scratch/b8c6ff258063/SP87_C13_149_work');p='149_scan090';rp=w/'review'/f'{p}_reviewed.json';r=json.loads(rp.read_text());pp=w/'pages'/f'{p}.tex';t=pp.read_text()
oldnested=r'E_{U_{\unsure{\widetilde\eta|\widetilde K}}}';newnested=r'E_{U_{\widetilde K}}'
oldloc=r'\unsure{loc.|\deleted{les}}';newloc=r'\unsure{\deleted{alors}|loc.|\deleted{les}}'
repls={'cet hom à':'cet hom :',oldnested:newnested,r'E_{U_\eta}':r'E_{U_K}',r'\deleted{\unsure{se déduit|se déduise}}':r'\deleted{\unsure{se déduit|se déduise|question}}',oldloc:newloc,r'\unsure{ns|nous}':r'\unsure{ns|on|nous}'}
for a,b in repls.items():assert a in t,a;t=t.replace(a,b)
pp.write_text(t)
mf={x['box']:x for x in json.loads((w/'second'/f'{p}_crop_manifest.json').read_text())}
def upd(place,box,**kw):next(x for x in r['changes'] if x['place']==place).update(crop=f'crops/second_{p}_{box}.png',box=mf[box]['coordinates'],**kw)
upd('090.b_hom','B003',final='cet hom :',evidence='Two separate dark points are vertically aligned before I_s-prime. There is no closed a bowl or baseline letter stroke beneath an accent. Read a colon, despite the unusual restriction de cet hom : syntax. No stop follows hom.',against_c=True,against_h=True,kind='other')
upd('090.d_deleted','B008',final=r'\deleted{\unsure{se déduit|se déduise|question}}',evidence='The crossed lower run has a small initial curved group, a possible word gap, tall looped/ascending middle strokes, and a later i dot. These continue to favor se déduit/déduise, but the strike merges the first group and middle tall strokes enough that the blind question reading cannot be excluded. Provient is separately live above; ne remains below the insertion leader.')
upd('090.f_after','B014',final=newloc,evidence='A low initial loop is joined to a taller l-like loop, then an o-like oval and terminal r/s-like knot. An oblique crossing stroke supports cancelled alors more strongly than the former loc./les guesses, but the crowded letters and state remain ambiguous. The separate following comma stays live.',against_c=True,confidence='low')
upd('090.ns_pouvons','B018',final=r'\uline{\unsure{ns|on|nous} pouvons donc identifier le groupe de décomposition}',evidence='The pronoun is compressed into a short initial rise and almost horizontal return, admitting ns, on, or a compressed nous. The following word has a descending p, round o, and several low u/v/o/n/s turns; no isolated tall r or final a supports pourra. Preserve pouvons and the continuous underline.')
ek='The very small index has a short high left stroke, joined rising branch, and short right foot. It matches the compressed K controls on 086/088/093/096 and the adjacent larger K; the clearer eta on 102 has a substantially longer descending return curling left. The shared field notation resolves the ambiguous small-scale form as K.'
upd('090.final_eta','B021',final=r'E_{U_K}',evidence=ek,confidence='medium',against_c=True,against_h=False)
upd('090.final_no_de','B021',final=r'\inserted{$E_{U_K}$ sur $E_K$, ou}',evidence='The raised note begins directly with E, with no de before it. A brace-like leader joins it after scindage; the original de remains on the baseline after the leader. The short closing word has a small o and a low open u, with no independent n hump. Its small field index is K by the cross-leaf handwriting comparison.')
# The corrected nested K readings now agree with both witnesses. They remain
# documented in the second-pass change table rather than false witness rows.
r['changes']=[x for x in r['changes'] if x['place'] not in {'090.d_nested_index','090.final_nested_index'}]
for m in r['marks']:
 if m['id']=='M1249':m.update(reading=newloc,evidence='Low initial loop, taller l-like loop and later o/r/s traces favor cancelled alors; crossing strokes still leave loc. or cancelled les possible.',crop=f'crops/second_{p}_B014.png',box=mf['B014']['coordinates'])
 if m['id']=='M1250':m.update(reading=r'\unsure{ns|on|nous}',evidence='The short initial rise and long low return do not distinguish ns, on or compressed nous. Pouvons and its underline remain clear.',crop=f'crops/second_{p}_B018.png',box=mf['B018']['coordinates'])
r['unresolved']=[u for u in r['unresolved'] if u['place'] not in {'090.d_nested_index','090.final_nested_index'}]
for u in r['unresolved']:
 if u['place']=='090.d_deleted':u.update(reading=r'\unsure{se déduit|se déduise|question}',alternatives='two-word phrase or question under horizontal cancellation')
 if u['place']=='090.f_after':u.update(reading=newloc,alternatives='cancelled alors preferred; loc. or cancelled les remain')
 if u['place']=='090.ns_pouvons':u.update(reading=r'\unsure{ns|on|nous}',alternatives='short form ns / on / compressed nous')
for h in r['hand_observations']:
 if h['habit'].startswith('Nested eta'):h.update(habit='Very small K can have a joined n-like branch and short foot.',pages='086, 088, 090, 093, 096',evidence=ek,witness_errors='The first consolidation read eta in three nested positions on 090. Both witnesses have K in two; H also has K in the final raised insertion.')
for n in r['notation_additions']:
 if n['written'].startswith('low arch'):n.update(written='small joined branch with short right foot below U',transcription=r'\widetilde K',evidence=ek)
for i in r['inventory']:
 if i['element']=='condition_b':i['first_words_or_objects']=r'b) La restriction de cet hom : I_{s\prime}'
 if i['element']=='d_group_insertion':i['first_words_or_objects']=r'E_{\widetilde f} de E_{U_{\widetilde K}} sur E_{\widetilde K}'
 if i['element']=='d_cancelled_verb':i['first_words_or_objects']=r'se déduit|se déduise|question'
 if i['element']=='uncertain_loc':i['first_words_or_objects']=newloc
 if i['element']=='underlined_identification':i['first_words_or_objects']=r'ns|on|nous pouvons donc identifier le groupe de décomposition'
 if i['element']=='inserted_global_scindage':i['first_words_or_objects']='E_UK sur E_K, ou'
r['notes'] += '\n\nBlind adjudication reads a literal colon after cet hom in b): two separate points, with no a bowl. It is retained despite the odd syntax. Three small field indices are K after comparison across 086/088/090/093/096 with the long-returning eta on 102; this supersedes the earlier local eta preference. Two nested-K places consequently cease to be differences from either witness, while the final raised K differs from C. The cancelled verb now also admits question beneath the strike. The crossed word after tilde f favors cancelled alors but retains the older loc./les alternatives. The compressed pronoun also admits on; pouvons stays. Both levels of the cancelled existence condition are crossed, so its inserted upper line remains inside the deletion wrapper. All fifteen token-different boxes were inspected.\n'
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
cs={x['box']:x for x in csv.DictReader((w/'second'/f'{p}_comparison.tsv').open(),delimiter='\t')}
e={
'B003':'The two vertically separated points have no connecting bowl or a-shaped baseline stroke. Change à to the literal colon; retain hom without a stop and I_s-prime with the isomorphism sign.',
'B004':'Both k-like symbols have stems and two branches with independent small i indices. Their unlooped construction does not securely distinguish Greek kappa and Latin k, so preserve the established kappa|k doubt; relative height alone does not establish a separate capital K notation. Both composition operators are hollow circles, and id_T is unchanged.',
'B005':'The first letter after hom is a tall closed loop, matching l rather than an open c. Low a/c/e turns lead to a high crossed t. Keep lacet, the headed T-to-pi connector and comma. The blind cont does not account for the tall initial loop.',
'B006':'Mu has its descending first limb; membership, double N and superscript star are clear. Braces around the star are only TeX syntax. No final stop is present.',
'B007':'A single upright restriction bar stands between lambda and serifed I. Both readings represent it. The complete n’est pas l’hom trivial and absence of stops agree.',
'B008':'The n-like small field indices match compressed K with short feet, not the long-returning eta control; change the nested doubtful eta/K to K while retaining the outer K. U has a retraced curved basin, not a new K alphabet. The cancelled phrase remains se déduit/déduise preferred with question newly admitted, because the strike obscures the separation and middle tall strokes. Ne and inserted provient remain in their own layers.',
'B009':'The two round characters belong to the recurring local-ring notation O-tilde. Each has a near-round bowl under a wave; there is no independent numeral-zero role on this line. Keep both O symbols and the retraced U, without inventing a cancelled underlying letter.',
'B012':'The crop contains the small s and closing parenthesis, plus the clipped right end of en at its left edge. Preserve the complete en from the page reading; clipping does not remove it. No point follows the parenthesis.',
'B013':'Several extra transverse strokes cross the f) label and the Si group, distinct from their loops. Keep both cancelled with Désignons par added above. The cancellation hides parts of désigne/désignons and aussi; the blind confident wording does not expose every letter, so retain the existing doubts.',
'B014':'A small lower loop before the tall l-like loop, an o-like turn and a crossed terminal knot favor alors. The oblique crossing may be a strike; record cancelled alors first while retaining loc. and cancelled les alternatives. The following comma is separate and live.',
'B015':'A lower i with dot follows the existential sign and has no independent f hook. A second i begins the upper condition i in I(k). One long strike crosses the lower row and another crosses the upper row through the relation, so the upper insertion remains cancelled as well. The relation’s lower bar coincides with cancellation; retain simeq|sim. The two punctuation marks are aligned like colon, not a secure comma tail. Retain existing doubts in the obscured condition and tel que.',
'B017':'The full formula has tilde f(s), membership, serifed I, equality, X_s, a diagonal set-minus and U_s, followed by a point. The difference is display delimiters only; keep the complete formula.',
'B018':'The short pronoun has only a low initial rise and long return, so ns, on and compressed nous remain possible. Pouvons has several successive low letter turns and a terminal n/s trace; the proposed pourra lacks an independent r/a sequence. Preserve the underline, which continues on the next source line.',
'B019':'The cancelled pi-like cap/two uprights and lowered s-like curve remain doubtful pi_s; the lower curve matches neighboring s and does not establish a numeral 3. The inserted ext. note contains a small lower-case k before (s), and its leader ends after E_Xs, before qui est. Keep the explicit pi and comma. The extra upper line in the blind excerpt is context already present.',
'B021':ek+' The raised note starts with E, then sur E_K, comma and ou; the low open u has no second n hump. Its brace leader is attachment ink. The later raised E_Xs is separate, with no strike through the underlying EU term, so both live layers remain.'}
changed=['B003','B008','B014','B018','B021'];d={b:dict(evidence=v,changed=b in changed) for b,v in e.items()}
for b in changed:
 f=cs[b]['first']
 for a,z in repls.items():f=f.replace(a,z)
 d[b]['final']=f
(w/'review'/f'{p}_audit_decisions.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
