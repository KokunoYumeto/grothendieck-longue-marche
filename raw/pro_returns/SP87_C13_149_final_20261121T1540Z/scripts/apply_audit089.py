from pathlib import Path
import json,csv
w=Path('/workspace/scratch/b8c6ff258063/SP87_C13_149_work');p='149_scan089';rp=w/'review'/f'{p}_reviewed.json';r=json.loads(rp.read_text());pp=w/'pages'/f'{p}.tex';t=pp.read_text()
oldref=r'(2\deleted{\unsure{5}}\inserted{6})';newref=r'(2\deleted{\unsure{6|5}}\inserted{\unsure{5|6}})'
oldf=r'\inserted{$f_{\unsure{K}}$}';newf=r'\inserted{$f_{\deleted{\unsure{K}}}$}'
repls={oldref:newref,oldf:newf,r'\pi\unsure{\longrightarrow|-}E_{U_s}':r'\pi\unsure{-|\longrightarrow}E_{U_s}',r'\inserted{sur les $\pi_1$}':r'\inserted{sur \unsure{les|le} $\pi_1$}',"$E_{\\widetilde K}$ peut d'ailleurs":r"$E_{\widetilde K}$ \unsure{peut|par} d'ailleurs","s'identifier au groupe":r"\unsure{s'identifier|s'identifie} au groupe",'codim $1$, définit':'codim $1$, '+r'\unsure{définit|definit}'}
for a,b in repls.items():assert a in t,a;t=t.replace(a,b)
pp.write_text(t)
mf={x['box']:x for x in json.loads((w/'second'/f'{p}_crop_manifest.json').read_text())}
def upd(place,box,**kw):next(x for x in r['changes'] if x['place']==place).update(crop=f'crops/second_{p}_{box}.png',box=mf[box]['coordinates'],**kw)
eref='The faint lower oval and ascending entry support an underlying 6, while the darker long top bar and descending hooked stroke support an overwritten 5. The superposed parts cannot be fully separated: retain 6|5 underneath and 5|6 above. Only one initial 2 and one pair of parentheses are present. The expected reference to (26) does not settle the live digit.'
upd('corrected_reference26','B006',final=newref,evidence=eref,confidence='low')
upd('sur_les_pi_insertion','B008',final=r'\inserted{sur \unsure{les|le} $\pi_1$}',evidence='The smaller line is inserted after the hom description. Its article has a tall l and low e followed by a terminal curl that may be s or the e return; keep les first with le as alternative. The pi subscript 1 and attachment are clear.',confidence='medium')
efk='The tall crossed f is live. At its lower right, a K-like branched group is crossed by two short heavy oblique strokes distinct from the long curved insertion leader. Preserve the tentative K as cancelled within the inserted formula; the leader attaches the whole addition after rationnelle and is not a literal slash.'
upd('fK_subscript_and_leader','B010',final=newf,evidence=efk,against_c=True,confidence='medium',kind='deletion state')
upd('peut_dailleurs','B016',final=r"\unsure{peut|par} d'ailleurs",evidence='A long descending p is clear and the right end makes a triangular upward return, favoring t and hence peut; the intervening letters are flattened into a long stroke, leaving par possible. There is no initial q bowl. The next word has an independent d and apostrophe before ailleurs.',confidence='medium')
upd('sidentifier','B017',final=r"\unsure{s'identifier|s'identifie}",evidence='The letters through identifi and a low e are legible. The final rightward return has a small downward ending but is too compressed to establish an independent r securely. Keep the infinitive first with the unextended ending as an explicit alternative.',confidence='medium')
# Reversal of an already doubtful connector changes the preferred ink reading,
# not a lexical witness count; retain it in the doubts and adjudication record.
for m in r['marks']:
 if m['id']=='M1243':m.update(decision='undecided',reading=newref,evidence=eref,crop=f'crops/second_{p}_B006.png',box=mf['B006']['coordinates'],confidence='low')
 if m['id']=='M1245':m.update(reading=r'\deleted{\unsure{K}}',evidence=efk,crop=f'crops/second_{p}_B010.png',box=mf['B010']['coordinates'])
for u in r['unresolved']:
 if u['place']=='reference_under5':u.update(place='overwritten_reference_digit',reading=newref,alternatives='underlying 6|5; live overstroke 5|6',confidence='low')
 if u['place']=='inserted_f_subscript':u.update(reading=r'f_{\deleted{\unsure{K}}}',alternatives='K-like subscript crossed separately from insertion leader')
 if u['place']=='27_internal_pi_link':u.update(reading=r'\pi\unsure{-|\longrightarrow}E_{U_s}',alternatives='plain shaft first; right arrow alternative')
r['unresolved'] += [dict(place='inserted article before pi_1',reading=r'\unsure{les|le}',alternatives='s or terminal e return',confidence='medium'),dict(place='peut d’ailleurs',reading=r'\unsure{peut|par}',alternatives='compressed internal letters; terminal t-like turn favors peut',confidence='medium'),dict(place='s’identifier ending',reading=r"\unsure{s'identifier|s'identifie}",alternatives='independent r or e terminal return',confidence='medium'),dict(place='accent of définit',reading=r'\unsure{définit|definit}',alternatives='accent near e/f join is not independently distinct',confidence='medium')]
for i in r['inventory']:
 if i['element']=='reference_underdigit':i['first_words_or_objects']=r'\deleted{\unsure{6|5}}'
 if i['element']=='reference_live_digit':i['first_words_or_objects']=r'\inserted{\unsure{5|6}}'
 if i['element']=='fK_added':i['first_words_or_objects']=newf
 if i['element']=='pi_words_added':i['first_words_or_objects']=r'sur \unsure{les|le} \pi_1'
r['inventory'].append(dict(element='fK_subscript_cancelled',kind='deletion',position='lower right of raised f after rationnelle',first_words_or_objects=r'\deleted{\unsure{K}}',sheet_kind='text',hand='his hand',transcribed='yes'))
r['notes'] += '\n\nBlind crop adjudication revises the overwritten reference to underlying 6|5 and live 5|6, both explicitly doubtful; the darker top bar favors a 5 even though the nearby diagram sequence would suggest 26. The small K-like subscript beside the inserted f has cancellation strokes distinct from its leader and is now recorded as cancelled. The pi-to-E connector in (27) has only a rounded endpoint and now prefers a shaft; the clear next arrow remains headed. The article les/le, accent in définit, flattened peut/par and infinitive ending remain local doubts. Diagram (28) retains its upward arrow: a chevron is visible at the upper endpoint beside a wavy label. The lower E is retraced but no distinct underlying letter is readable. All fourteen differing boxes were inspected; 44 remains author pagination and 88 separate foliation.\n'
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
cs={x['box']:x for x in csv.DictReader((w/'second'/f'{p}_comparison.tsv').open(),delimiter='\t')}
e={
'B001':'Two angular 4s are clear. Whole-page position at the head and heavier author hand establish author number 44; keep mspage in the page, not marginal foliation.',
'B002':'The first and last shafts retain their existing dash-first doubts. The pi-to-E shaft has only a small rounded terminal rather than a separated barb, so change its preferred reading to dash with arrow alternative. The next connector has a clear angled head. U has a curved basin and no independent middle diagonal of N; retain U_s, both endpoint 1s, and (27). E/cal-E is a typographic convention, not another alphabet inferred from this crop.',
'B006':eref,
'B008':'The article’s final low curl is not independent of the e return, so retain les first and add le. The tall l, inserted sur, pi with low footed 1, correspondant and colon remain.',
'B009':'The top line is headless and the bottom horizontal has a clear head. The left vertical has a tiny bent end without a secure barb; keep its existing shaft/down-arrow doubt. The lower-left symbol’s retraced upper stroke and low bend still admit s or k. Retain the right downward arrow and the full Spec O-tilde term.',
'B010':efk,
'B012':'The inserted capital has the two curved bowls and middle turn of the E used throughout the diagram; no independent epsilon alphabet is established. The high wave belongs to f and the curved leader attaches after section. Keep E_tilde f with its insertion state.',
'B014':'The upper end of the vertical shaft has a two-sided chevron; a separate wave lies to its right. Retain an upward arrow with tilde label, not a bare rotated equivalence. The lower E is heavily retraced but has a readable upper bowl and lower return, with no separable underlying cancelled letter. Lambda stays above the rightward arrow and (28) at the left.',
'B015':'The subscript before (s) is a small low k with one short upright and branches, unlike the larger K under the first E. Retain k(s), the left-pointing arrow and its independent upper wave. The outer E_tilde K to E_tilde O arrow is rightward.',
'B016':'The first word starts with a long descending p and a narrow upper entry, not a closed q. Its final triangular rise favors t, but the middle is a flattened stroke, so retain peut first with par possible. The following d and apostrophe are separate. The small K has an oblique branch and short right foot rather than the independent uprights of N.',
'B017':'The word through identifi and low e is readable. Its final rightward curl may be r or the e exit; add explicit infinitive/present-ending doubt instead of resolving it from the preceding verb.',
'B018':'The upper oval remains open, admitting O or rounded U. Underline and subscript S,s are clear. Keep the existing doubt; moving the wrapper or clipped de at the box edge does not change the source reading.',
'B019':'Two thin looped 8s lie at the bottom edge in the separate foliation hand. Keep margin 88, distinct from the author’s head number 44.',
'B021':'The complete paragraph confirms a single overwritten second digit, handled as underlying 6|5 and live 5|6. At définit the possible accent merges with the tall f entry and cannot be isolated, so retain accented/unaccented doubt. Résumons underline, La capital, literal codim without stop, inserted underlined pas, struck l’inclusion and live l’hom remain unchanged.'}
changed=['B002','B006','B008','B010','B016','B017','B021'];d={b:dict(evidence=v,changed=b in changed) for b,v in e.items()}
for b in changed:
 f=cs[b]['first']
 for a,z in repls.items():f=f.replace(a,z)
 if b=='B017':f=f.replace("s'identifier",r"\unsure{s'identifier|s'identifie}")
 if b=='B016':f=f.replace("peut d'ailleurs",r"\unsure{peut|par} d'ailleurs")
 if b=='B021':f=f.replace('définit',r'\unsure{définit|definit}') if r'\unsure{définit|definit}' not in f else f
 d[b]['final']=f
(w/'review'/f'{p}_audit_decisions.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
