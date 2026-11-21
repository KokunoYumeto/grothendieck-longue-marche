from pathlib import Path
import json
W=Path(__file__).resolve().parents[1];pg='150_scan083';rp=W/'records'/f'{pg}.json';r=json.loads(rp.read_text())
c=json.loads((W/'second'/f'{pg}_comparison.json').read_text());b={x['box']:x for x in c['results']};notes={}
word=r'\unsure{proespace|\deleted{t}proespace}'
oldtail=r'\deleted{\unsure{\text{et où}}}'
tail=r'\deleted{\text{et }\unsure{\text{où}|\text{aussi}|\text{ainsi}}}'
oldbrace=r"\overbrace{\left(\bigcup_{l\in L}V_{\deleted{j}\inserted{l}}^{X'}\right)}^{\substack{\inserted{X_L^*\ \text{car }X_L^*\text{ ouvert dans }X'}\\\Vert}}"
brace=r"\left(\overbrace{\bigcup_{l\in L}V_{\deleted{j}\inserted{l}}^{X'}}^{\substack{\inserted{X_L^*\ \text{car }X_L^*\text{ ouvert dans }X'}\\\Vert}}\right)"
oldlast=r'\deleted{\unsure{de|dont}}';last=r'\deleted{\unsure{de|dont|donc}}'
p=W/'pages'/f'{pg}.tex';s=p.read_text()
for old,new in [(r'\text{le proespace de la forme }',r'\text{le '+word+' de la forme }'),(oldtail,tail),(oldbrace,brace),(oldlast,last),(r'&X_i\'=X_i',r'&X_i\'\doteq X_i')]:
    if old.startswith('&X'):continue
    assert s.count(old)==1,old;s=s.replace(old,new)
old="&X_i'=X_i";assert s.count(old)==1;s=s.replace(old,"&X_i'\\doteq X_i")
old="V_J^L=\\bigcup_{\\substack{j\\in J\\\\l\\in L\\\\j\\leq l}}";assert s.count(old)==1;s=s.replace(old,'(69)\\qquad '+old)
assert s.count('on a (69) (équiv.')==1;s=s.replace('on a (69) (équiv.','on a (équiv.')
p.write_text(s);(W/'records'/p.name).write_text(s)
ch={x['id']:x for x in r['changes']}
ch['C02']['final']=word;ch['C02']['evidence']+=' The blind crop review also records uncertainty whether the reworked initial includes an older canceled t; no such older letter is asserted as certain.'
ch['C06'].update(final=tail,evidence='The initial e and tall crossed t are plain. The remaining low letters lie under the cancellation; the detached stroke near the end may be an accent or i dot. Keep the final word uncertain between où/aussi/ainsi rather than treating the whole phrase or H’s donc as established.')
ch['C09'].update(final=brace,evidence=ch['C09']['evidence']+' The blind review also corrects the brace extent: its two ends lie inside the large parentheses, above the union itself, rather than above the parentheses.',crop=f'crops/{pg}_blind_B06.png',box=b['B06']['coordinates'])
ch['C08']['confidence']='medium'
for d in r['decisions']:
    if d['id']=='M0674':d['confidence']='medium';d['ink']+=' Blind crop review confirms the lower descending hooked j and the separate upper looped l; the heavily crossed old index merits medium confidence.'
r['changes']=[x for x in r['changes'] if x['id']!='C31']
for ident,place,C,H,final,box,why,kind,conseq in [
 ('C36','(68), definition of X_i-prime','=', '=',r'\doteq','B02','Two short equality rules have a separate dark point immediately above their right half. The dot of the preceding subscript i lies lower and to the left; it is a different mark. Preserve the dotted equality.','misread symbol or index',True),
 ('C37','Handwritten formula number69','on a (69) in marginal prose','on a (69) in marginal prose','(69) at the left of the main restricted-union formula','B13','The number is written horizontally at the same height as the main restricted-union formula. The surrounding NB prose and marginal diagram run diagonally. The number belongs to the main formula, not to the diagonal words on a.','insertion or placement',False)]:
    r['changes'].append(dict(id=ident,place=place,C=C,H=H,final=final,evidence=why,crop=f'crops/{pg}_blind_{box}.png',box=b[box]['coordinates'],confidence='high',kind=kind,error_kind='1 symbols/indices' if ident=='C36' else '6 insertion placement',against_C=True,against_H=True,consequential=conseq,marked_in_H=False,phase='blind audit'))
for d in r['diff_coverage']:
    if 'C31' in d['change_ids']:d.update(change_ids=[x for x in d['change_ids'] if x!='C31'],classification='unresolved doubt',reason='The canceled word remains de/dont/donc. Widening uncertainty alone is recorded in doubts, not counted as a certified reading change.')
for d in r['doubts']:
    if d['place']=='End of (68), struck phrase':d.update(reading=tail,alternatives=['où','aussi','ainsi'],reason=ch['C06']['evidence'],crop=f'crops/{pg}_blind_B04.png',box=b['B04']['coordinates'])
    if d['place']=='Bottom paragraph, cancelled word after drapeau':d.update(reading=last,alternatives=['de','dont','donc'],reason='The d is visible; the final loop and short rising stroke could belong to nt or c, while the middle is hidden. None is certified.',crop=f'crops/{pg}_blind_B15.png',box=b['B15']['coordinates'])
r['doubts'].append(dict(place='Reworked initial of proespace',reading=word,alternatives=['retraced p','older canceled t before/under p'],confidence='low',reason='A tall stroke and transverse crossing at the initial may be reworking of p or an older t; the separate older letter cannot be certified. The rest of proespace is clear.',crop=f'crops/{pg}_blind_B03.png',box=b['B03']['coordinates']))
for x in r['inventory']:
    text=x.get('first_words_or_objects','')
    if 'on a (69)' in text:x['first_words_or_objects']=text.replace('on a (69)','on a')
    if 'substack' in text and 'j\\leq l' in text:x['first_words_or_objects']='(69) '+text
r['notes']+='\n### Blind reading corrections\n\nThe definition of X_i-prime uses a dotted equality: its upper point is distinct from the preceding i dot. The explanatory overbrace of the union sits inside the large parentheses. The horizontal handwritten69 belongs to the main restricted-union display, while the NB note and its diagram are slanted; both drafts placed69 in the marginal prose. A possible older t at the initial of proespace and the final words of two cancellations remain uncertain. The prior de-versus-dont row is withdrawn because the final result is uncertainty alone. The opening Car on a, the reminder où on se rappellera, the starred sous réserve que note and the live donc are retained after crop review. The lower replacement sentence follows the canceled line on a normal baseline; unlike the raised distincts and ceux-ci, it has no independent insertion leader.\n'
r['hand_log'].append(dict(habit='A formula number may be surrounded by later diagonal marginal writing while retaining its horizontal attachment.',places='69 and the adjacent restricted union',scope='Compared the baseline and orientation in the whole blind B13 crop.',witness_errors='Both drafts attached69 to the margin; corrected to the main display.'))
def put(box,evidence,final=None):
    notes[box]=dict(viewed=True,evidence=evidence)
    if final is not None:notes[box].update(changed=True,final=final)
put('B02','The first relation has a wavy upper stroke and straight lower rule, supporting simeq. In the X_i-prime definition, the distinct point above the two equals bars is not the preceding i dot: use doteq. The reworked initial of proespace may include an old t, so mark that state locally. The final canceled phrase starts with clear et but its last word remains uncertain. Prime placement, text/math spans and aligned wrappers are representation differences.',b['B02']['first'].replace('le proespace','le '+word).replace("&X_i'=X_i","&X_i'\\doteq X_i").replace(oldtail,tail))
put('B03','The rest of proespace reads clearly, but the tall initial and transverse crossing cannot distinguish a retraced p from an older canceled t with certainty. Add that narrow local state doubt.',b['B03']['first'].replace('proespace',word))
put('B04','The e and crossed t are legible; subsequent low strokes are covered, and the detached upper stroke may be an accent or dot. Keep only the final word uncertain among où/aussi/ainsi.',r'\deleted{et \unsure{où|aussi|ainsi}}')
put('B05','The curved parenthesis is followed by the looped capital C and connected a/r, then a separate low on group and compact a. The blind On en would omit the first word’s distinct a/r sequence. Retain Car on a.')
put('B06','The brace ends are inside the large parentheses, over the union, so move its extent inside them. The two upright bars connect the raised X_L-star annotation to the brace; retain that attachment and the inserted explanatory words. The lower canceled j has a descender and hooked foot, with a distinct upper replacement l. The blind ell and l are equivalent encodings of the same looped letter. Opening en/a and the last empty-set line are overlapping text already transcribed in their own locations.',b['B06']['first'].replace(oldbrace,brace))
put('B07','The bottom old index has a descending stroke and leftward hook, whereas the replacement above it has the l loop and rightward foot. Keep deleted j / inserted l at medium confidence. Dollar spans and ell versus l are encoding differences.')
put('B08','All four cases and both standard words agree. The left brace ends above the separate parenthetical consequence; keep that parenthesis outside the cases. Its final punctuation has a straight upright and lower dot, supporting the exclamation mark. The extra membership fragments at the top belong to the preceding union; do not duplicate them. The l/ell and column grouping differences are representational.')
put('B09','The rotated crop has three groups sous / réserve / que: the second has an acute and the compressed s/e/r/v/e run, while the third descends as q. The next line has soient with a dotted i and terminal t, followed by normaux with crossed x. The four terminal points after métrisable are separately visible. Reject du moins and étant; retain the first reading.')
put('B10','The slanted marginal stroke touches the initial d but does not traverse the later o/n/c baseline letters. The word donc is live; no deletion is added.')
put('B11','The union and its three index conditions agree. The final mark has a p-like descender and low connected letter remnants crossed by a horizontal stroke: it is canceled uncertain prose, not a geometric figure. Keep uncertain pour; do not draw it. Display delimiters and ell are representational.')
put('B12','The opening curve, low où and detached accent precede the separate on and se groups. Rappellera has two descending p strokes, two tall l strokes and the low e/r/a ending; it is not rappelant. The final parenthesis and complete identity agree.')
put('B13','The horizontal69 is aligned with the main restricted union, while NB prose and its diagram are diagonal: remove69 from marginal prose and attach it to the main display. The curved precedence sign has two curved arms, supporting prec, not subset. The final slanted words include on a. Parenthesis strokes flank h; the separate tilde and plain headed arrow remain. Extra metric-note, donc, formula and body fragments overlap other boxes and are not repeated.',b['B13']['first'].replace('on a (69)','on a')+'\n(69)\\quad V_J^L [main display attachment]')
put('B14','The h has a tall ascender and lower arch, with parenthesis strokes on either side; retain (h). The plain rightward arrow, tilde, vertical equals and underbrace all agree. The initial dans ce is overlap with the marginal prose. Spacing, text/roman wrappers and line breaks are layout only.')
put('B15','The looped initial d is clear; the thick canceled middle and terminal loop do not establish de, dont or donc independently. Broaden the existing narrow uncertainty without certifying another word.',last)
put('B16','The same canceled word remains de/dont/donc. Distincts and ceux-ci sit above the baseline with attachment leaders; the later moins un sentence lies on the next regular baseline without a leader, so it remains live continuation rather than an added insertion wrapper. The comma after the termes/inserted phrase is retained, and the entire old moins deux ... line remains canceled.',b['B16']['first'].replace(oldlast,last))
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');(W/'second'/f'{pg}_root_crop_notes.json').write_text(json.dumps(notes,ensure_ascii=False,indent=2)+'\n')
print('083: all15 differing crops observed and adjudicated.')
