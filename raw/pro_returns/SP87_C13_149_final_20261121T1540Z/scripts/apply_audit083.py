from pathlib import Path
import json,csv
w=Path('/workspace/scratch/b8c6ff258063/SP87_C13_149_work');p='149_scan083';rp=w/'readers'/p/'report.json';r=json.loads(rp.read_text());pp=w/'pages'/f'{p}.tex';t=pp.read_text()
t=t.replace(r'$\overline m$',r'$=$').replace(r'\deleted{ce qui \unsure{donne|devra}}',r'\deleted{\unsure{ce|et} qui \unsure{donne|devra|leur}}').replace(r'$N_x$ dans le $E_K$',r'$N_x$ dans \unsure{le|$E$} $E_K$');pp.write_text(t)
for c in r['changes']:
 if c['place']=='C083_11_meme_short_form':c.update(final='=',against_c=True,confidence='medium',evidence='Blind and cross-leaf review: the sign has an upper horizontal bar and a lower bar with a hooked entry; there is no distinct sequence of m humps. It matches the small two-stroke shorthand on 086/091 and differs from the clearly barred capital M on 097. Transcribe the written equals sign, retaining its expansion only in the abbreviation list.',crop='second_149_scan083_B009.png',box=[290,1160,570,1265])
 if c['place']=='C083_13_cancelled_phrase':c.update(final=r'\deleted{\unsure{ce|et} qui \unsure{donne|devra|leur}}.',evidence='The strike crosses the entire phrase but stops before the live point. The q descender and i mark of qui survive. The initial small curved/tall group is compatible with ce or et; the last word has an ascender and obscured low turns, admitting donne/devra and the blind reader’s leur. Keep those limits explicit instead of resolving covered letters.',crop='second_149_scan083_B011.png',box=[300,1760,865,1900])
 if c['place']=='C083_15_le':c.update(final=r'\unsure{le|$E$}',confidence='low',evidence='The compact retraced group after dans has a looped rising entry and low return compatible with le, but its merged strokes also admit a cursive E. No independent cancellation stroke can be isolated from those strokes. Keep le first with E as an alternative, live, rather than claiming certain letters or a certain deletion.',crop='second_149_scan083_B013.png',box=[1330,1985,1667,2115])
for m in r['marks']:
 if m['id']=='M1231':m.update(decision='other',reading='=',confidence='medium',evidence='Two principal strokes: an upper bar and a hooked lower bar, without independent m humps. Cross-leaf comparison confirms the same equals shorthand on 086/091, distinct from barred capital M on 097.',crop='second_149_scan083_B009.png',box=[290,1160,570,1265])
for h in r['hand_observations']:
 if h['habit'].startswith('The shorthand for même'):
  h.update(habit='The equals shorthand for même can have a hooked lower-bar entry.',evidence='B009: upper straight bar, hooked entry and nearly straight lower bar; compare 086/091. No independent m hump sequence.',witness_errors='H expands the shorthand; C and the first consolidation read a barred m. Blind/cross-leaf review selects the written equals sign.')
for n in r['notation_additions']:
 if n['transcription']==r'\overline m':n.update(written='Two horizontal strokes, lower entry hooked',transcription='=',evidence='After ce qui revient au. Cross-leaf review distinguishes the equals shorthand from an independently lettered barred M.')
for u in r['unresolved']:
 if u['place'].startswith('last word in cancelled'):u['alternatives']='devra | leur'
r['unresolved'] += [dict(place='opening of cancelled phrase',reading=r'\unsure{ce|et}',alternatives=['ce','et'],confidence='low'),dict(place='after N_x dans',reading=r'\unsure{le|$E$}',alternatives=['le','E'],confidence='low')]
r['notes'] += '\n\nBlind adjudication changes the small barred-m reading to the written equals shorthand after comparison with the same hooked lower bar on 086/091; this does not expand the abbreviation in the text. The cancelled phrase now also marks ce/et and admits leur beside donne/devra. The retraced group after N_x dans retains le/E doubt, with no securely independent strike. The first and final affine E exponents remain the short prime forms, visibly unlike the footed 1 in the middle occurrence. All 14 token-different boxes were inspected.\n'
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
cs={x['box']:x for x in csv.DictReader((w/'second'/f'{p}_comparison.tsv').open(),delimiter='\t')}
e={
'B001':'The dark upper number has angled 4 and straight 1. Both readings agree on 41; retain the manuscript-page wrapper for its head position.',
'B002':'The opening group contains O, the loop and descender of P, and a separate final S; it is OPS, not OK. Between à and localiser a low separate s/e group is present. Retain se rather than dropping it.',
'B003':'The tiny U subscript has a compressed looping S form; it is read consistently with the named base S on this line, without multiplying an e base. The doubled E has a short unfooted upper stroke matching the adjacent T prime. The middle occurrence B004 has a visibly footed 1. Preserve the first prime-shaped mark and the oblique set-difference slash, not a horizontal minus.',
'B004':'Both readings agree on the footed exponent 1, base S, two S primes, i.e., underlined O and comma. The underlining command differs only in syntax; retain the established math underline.',
'B005':'The fragment after live 2 has a tall narrow stem crossed by cancellation, compatible with 1. No independent pair of S curves is recoverable. Retain the doubtful cancelled 1; comma and S prime normal agree.',
'B006':'The initial section is clipped by the box and was read in full at first pass. The upper stroke after doubled E is short and unfooted, like the first prime and unlike the explicit footed 1 in B004. Retain E prime and the final point.',
'B008':'A long upright with short upper and lower arms forms the opening bracket. It precedes the single uncancelled Considérons. Donc is above the baseline and its leader attaches before les; the lower stroke is a leader, not a second bracket or cancellation.',
'B009':'The upper line is straight; the lower line has a hooked entry and then a long near-horizontal run. There is no independent two-hump m. Cross-leaf controls 086/091 use the same sign, whereas 097 has a distinct capital M under a bar. Change to the written equals sign; retain the following comma.',
'B010':'The compact final return after tel supports the short terminal s. Underlined O has index x_i. Anneau ends with a hyphen at the line break, followed by jauge and the complete parenthesis with final stop. Retain tels and the compound; line wrapping is not an extra textual difference.',
'B011':'The q descender and i dot in qui survive the strike. The initial group could be ce or et, and the last word’s ascender/low turns do not decide donne/devra/leur under the line. Broaden the explicit doubts but retain the complete cancellation and live point beyond it.',
'B012':'The raised au dessus de x has its leading/enclosing curve bending to the gap after barred K and before the closing parenthesis. This attachment agrees. The omitted pts du norma- in the blind row lies outside or at the edge of this crop; preserve the complete phrase read in the full source.',
'B013':'The group after dans has a compact rising loop and heavily retraced low return. Le is plausible, but cursive E also fits; a separate deletion stroke cannot be established. Record live le/E uncertainty instead of certifying le or cancelled E.',
'B014':'The insertion donc and its endpoint before dans agree, as do tilde x, equality, the bar over all k(x), comma and et. Only braces differ. Preserve the first reading.',
'B016':'Both readings give 82, with a two-loop 8 and curved 2 with long foot. Thin lower-left foliation remains a margin number, distinct from the dark head number 41.'}
d={k:dict(evidence=v,changed=k in ['B009','B011','B013']) for k,v in e.items()}
d['B009']['final']=r'$=$, les'
d['B011']['final']=cs['B011']['first'].replace(r'ce qui \unsure{donne|devra}',r'\unsure{ce|et} qui \unsure{donne|devra|leur}')
d['B013']['final']=r'$N_x$ dans \unsure{le|$E$}'
(w/'review'/f'{p}_audit_decisions.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
