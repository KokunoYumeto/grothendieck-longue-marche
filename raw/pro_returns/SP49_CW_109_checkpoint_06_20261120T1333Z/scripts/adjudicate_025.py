"""Root decisions for scan025 after three independent final returns."""
from common import *
R=load_page(25)
ch={r:{x['id']:x for x in R[r]['changes']} for r in 'ABC'}
T={r:(W/f'readers/025/{r}/reading.tex').read_text() for r in 'ABC'}
text=T['A'];Q=chr(96)*2
def a(i):return ch['A'][i]
def b(i):return ch['B'][i]
def c(i):return ch['C'][i]
def ap(i):return f'readers/025/A/crops/crop_{i:02}.jpg'
def cp(i):return f'readers/025/C/crops/{i:02}.jpg'
def repl(old,new):
 global text
 assert old in text,old
 text=text.replace(old,new,1)
repl(r"\deleted{\unsure{''}} ... of",c('p234-high-cancel')['reading']+' '+c('p234-wave')['reading']+' of')
repl('neither...','neither'+c('p243-high-point')['reading']+'...')
repl(r'i_0\colon N_0\to N',r'i_0\colon N_{\unsure{0|i}}\to N')
repl(r'\colon N)$\unsure',r'\colon N\unsure{)}$\unsure')
repl(r'\deleted{\unsure{2}} 255',r'\deleted{2} 255')
repl(r'-\deleted{\unsure{13}}',r'-\deleted{\unsure{13|l13}}')
repl('slightly confusing here!}',r'slightly confusing here}\unsure{\deleted{!}|!}')
# The insertion is physically raised and has a visible low caret.
old=r"\node at (274,1940) {l.2 ``developed'' l-2 ``amounts to \inserted{it} being contractible''};"
new=r"""\node at (274,1940) {l.2 ``developed'' l-2 ``amounts to};
\node[font=\tiny] at (975,1904) {\inserted{it}};
\node at (996,1940) {being contractible''};
\draw[line width=.3pt] (977,1953) -- (983,1940) -- (990,1953);"""
repl(old,new)
repl('% entry-29',b('p269-margin-marks')['reading']+'\n\n% entry-29')

viewed=json.loads((W/'records/root_025_viewed.json').read_text())
viewed=list(dict.fromkeys(viewed+['crops/025/03_p267_it.jpg']))
(W/'records/root_025_viewed.json').write_text(json.dumps(viewed,indent=2))
decisions=[]
def add(id,place,old,final,abc,evidence,crops,confidence='medium',kind='other',diff=True,consequential=None):
 d=dict(id='025-'+id,place=place,c=old,h=None,final=final,readers=dict(zip('ABC',abc)),evidence=evidence,crops=crops if isinstance(crops,list) else [crops],confidence=confidence,kind=('misread symbol or index' if kind=='readable ink left as \\ill{}' else kind),diff_c=diff,diff_h=False,marked_in_H=False)
 if consequential:d['consequential']=consequential
 decisions.append(d)
def pick(r,id,abc,evidence,crops,confidence=None):
 x=ch[r][id]
 add(id,x['place'],x['c'],x['reading'],abc,evidence,crops,confidence or x['confidence'],x.get('kind','other'))
for id,cid,n in [('left-rule','rules-left',1),('right-rule','rules-right',2)]:
 pick('A',id,[a(id)['reading'],b(id)['reading'],c(cid)['reading']],
 'The root narrow crop confirms the continuous near-vertical course. '+a(id)['evidence'],f'crops/025/0{n}_'+('left' if n==1 else 'right')+'_rule.jpg','high')
pick('A','far-left-trace',[a('far-left-trace')['reading'],'omitted',c('rules-faint-left')['reading']],
 'Root confirms a faint vertical gray trace and dark terminal point beside p245. Its geometry is reproduced without attributing a hand, medium or purpose.',ap(28))
pick('A','p234-opener',[a('p234-opener')['reading'],b('p234-opener')['reading'],Q+'surely'],
 'The high angular group is connected, with a short return but no clean separation into two ticks. Root preserves the double/single uncertainty; the single alternative is represented as an upright bent tick, not inferred from its opening function.',ap(2))
pick('C','p234-high-cancel',[a('p234-opener')['c'].replace(Q+'surely',r"\deleted{\unsure{''}}")]*2+[c('p234-high-cancel')['reading']],
 'Root confirms that the blackened quote-like cluster is raised above the low continuation groups. Its identity/count remains uncertain; only the omitted vertical placement is corrected.',ap(3))
pick('C','p234-wave',['...','...',c('p234-wave')['reading']],
 'The second low group begins with a connected wavy stroke and an upward nib, followed by two separate points. Root follows C reader in drawing the actual contour instead of three round stops; no mathematical meaning is assigned.',ap(3))
pick('A','p234-old-reference',[r'\deleted{p23}']*3,
 'The p descender, angular lower return of2 and the two rightward lobes of3 survive the crossing. Root resolves23 at medium confidence; no third digit is supplied.',ap(4))
pick('A','p243-not',['not']*3,
 'The final short upright carries a long rightward cross stroke, deciding t rather than r. All readers and root retain the literal neither... not.... despite the grammar.',ap(9),'high')
pick('C','p243-high-point',['omitted','omitted',c('p243-high-point')['reading']],
 'The crop shows a separate small upright point above/right of the terminal r, before the low three-mark continuation. It is separate from the earlier i and is drawn once at its observed height.',ap(9))
pick('A','p245-angular-mark',[a('p245-angular-mark')['reading'],'p245.','p245.'],
 'The mark at the rule has two short legs and an angular notch, not a simple round stop. Root preserves that geometry without assigning it a punctuation function.',ap(10))
pick('A','p247-old-line',['l.14']*3,
 'The initial loop, low point, narrow1 and angular4 survive between the zigzag diagonals. Root resolves the reference at medium confidence; this does not resolve the adjacent buried word.',ap(11))
pick('A','p247-upper-index',['i_0']*3,
 'The first lowered companion is a closed small oval, distinct from the high dot of its main i. The raised mapping index is therefore0. Its neighbouring N index is decided independently.',ap(12),'high')
pick('C','p247-live-N-index',['N_0','N_0',c('p247-live-N-index')['reading']],
 'This separate lowered glyph has an open lower cup and a small detached upper touch. Root follows reader C: a broken0 is favoured but a small dotted i remains possible. The preceding clear0 does not supply this glyph.',ap(12),'low')
decisions[-1]['consequential']='The raised N subscript acquires an independent0/i doubt; it is not made certain by the adjacent clear i_0.'
pick('A','p247-lower-index',[a('p247-lower-index')['reading'],b('p247-old-index')['reading'],r'$(i_{\unsure{0|i}}\colon N\unsure{)}$'],
 'The old lower companion is merged with cancellation diagonals; a small loop and upright do not separate0 from i. Root retains both alternatives, independently of the replacement above.',ap(13),'low')
pick('C','p247-old-closer',[')',')',r'\unsure{)}'],
 'The final curving trace merges with the zigzag return and cannot securely be separated as an old closing parenthesis. Root adds the independent uncertainty, without supplying a missing delimiter from the formula.',ap(13),'low')
add('old-quotes-retained','p247 cancelled mapping terminal ticks',r"\unsure{''}",r"\unsure{''}",[r"\unsure{''}",r"\unsure{''}","''"],
 'Two upper tips are visible, but the cancellation itself turns through this group. Root retains the original doubt against C reader’s resolution; the number of original quote strokes is not independently established.',ap(13),'low',diff=False)
pick('A','p247-also-placement',[a('p247-also-placement')['reading'],b('p247-also-position')['reading'],c('p247-also')['reading']],
 'The word also is physically level with l12 is aspheric, below the cancelled proposal and beside the descending curve. Root preserves that location and insertion markup, without deciding its logical attachment.',ap(13),'high')
curve=r'''\draw[line width=0.35pt] (596,1153) .. controls (611,1182) and (673,1188) .. (645,1248) .. controls (641,1253) and (638,1246) .. (642,1234);
\draw[line width=0.3pt] (814,1196) -- (789,1248);'''
add('p247-curves','p247 below the cancelled proposal','',curve,[curve,b('p247-connectors')['reading'],c('p247-curved-rule')['reading']+'\n'+c('p247-descending-tail')['reading']],
 'The first long stroke bows downward and turns back at the foot beside also; the other is an oblique continuation below the old opening parenthesis. Root reproduces both at this block without adding arrowheads.',ap(13),'high','drawing or diagram')
pick('A','p247-insertion-arc',[a('p247-insertion-arc')['reading'],b('p247-raised-index')['reading'],c('p247-live-i0')['reading']],
 'Root confirms a tall arc extending well below the slanting raised wording. Its drawn curve replaces the ordinary-height opening glyph, so the same parenthesis is represented once.',ap(12),'high')
pick('A','p248-opener',[a('p248-opener')['reading'],b('p248-opener')['reading'],Q+r'\uline{handwritten}'],
 'The compact high body has a bent return, but the count of independent quote strokes cannot be securely separated. Root retains the double/single uncertainty; the underline remains unchanged.',ap(15))
add('p250-opener-retained','p250 l.13 before its',Q+"its''",Q+"its''",[Q+"its''",b('p250-l13-opener')['reading'],Q+"its''"],
 'The left curved high stroke and small dark right companion are separable above the independent i-dot. Root follows A/C and retains the double opener against B’s new doubt.',ap(17),'medium',diff=False)
pick('C','p255-old-digit',[r'\unsure{2}','2','2'],
 'The old upper curve, diagonal descent and low foot are visible separately from the crossing slash. Root follows B/C and resolves2, with medium confidence because the overwrite is heavy.',ap(18),'medium')
pick('C','p262-old-ref',[r'-\deleted{\unsure{13}}',r'-\deleted{\unsure{13}}',c('p262-old-ref')['reading']],
 'The short dash lies left of the crossing and stays live. The crossed group has a final double-lobed3 and multiple narrow vertical/loop remnants;13 is favoured, while an earlier l before13 cannot be excluded.',ap(19),'low')
pick('A','p262-no-second-minus',[r'\& 2']*3,
 'The gap after the ampersand has no separate horizontal minus. Its terminal arm and the contour of2 are not an independent sign. All three and root remove the conjectural minus.',ap(19),'high')
pick('A','p263-terminal-letter',[r'allow\unsure{e|s}']*3,
 'A separate small loop follows w, with a visible counter and rightward exit favouring e. A compact s remains possible. The expected English ending is not used to decide it.',ap(20),'low')
pick('A','p263-detached-marks',[a('p263-detached-marks')['reading'],b('p263-marks')['reading'],c('p263-marks')['reading']],
 'Root confirms three separate dark groups: a fine rising oblique, a heavier descending oblique farther right, and a lower compact point. Each is drawn once without assigning punctuation.',ap(21),'high')
pick('A','p264-single-mark',["'l12"]*3,
 'One detached high upright stands to the left of the l loop. It has no second tick and is not part of the ascender. Root resolves the one-stroke reading without inferring its grammatical role.',ap(22),'high')
add('p267-insertion-placement','p267 l-2, it and its caret',r'\inserted{it}',new,
 [r'\inserted{it}',T['B'].split('% BEGIN p267')[1].split('% END p267')[0].strip(),r'\inserted{it}'],
 'The root crop confirms it above the gap between to and being and a narrow two-legged caret below the baseline. The final raises the word and draws the caret at the gap, rather than leaving the insertion inline.','crops/025/03_p267_it.jpg','high','insertion or placement')
pick('A','p269-cancelled-contraction',[a('p269-cancelled-contraction')['reading'],"isn't the use","isn't the use"],
 'The cancellation follows the high region around n and t; no original apostrophe can be separated securely on either side of n. Root retains A’s apostrophe-position uncertainty rather than recovering conventional spelling from expectation.',ap(25),'low')
add('p269-exclamation-state','p269 end of cancelled question',r'\deleted{!}',r'\unsure{\deleted{!}|!}',[r'\deleted{!}',r'\deleted{!}','!'],
 'The stem and lower dot are clear, but the cancellation passes through their gap and continues well to the right. This is not securely a punctuation mark outside the cancellation’s extent. Root favours inclusion in the cancelled phrase, while preserving the uncrossed-live alternative; identity and deletion state are separated.',[ap(25),cp(19)],'low','deletion state (struck given live or live given struck)')
pick('A','p269-not',[r'not $\pi_0,\pi_1$']*3,
 'The n shoulder, low oval of o, and t upright with a rightward crossbar remain traceable beneath the crossing. Root resolves not at medium confidence.',ap(26),'medium')
pick('B','p269-margin-marks',['omitted',b('p269-margin-marks')['reading'],c('p269-margin-marks')['reading']],
 'Root confirms two separated points and a lower short nearly horizontal stroke outside the right rule. They are represented geometrically without attaching them to sentence punctuation.',cp(21),'high')
pick('A','p273-point',[a('p273-point')['reading'],b('p273-point')['reading'],c('p273-point')['reading']],
 'A small dark raised point is separate from both the reference and following l. Root preserves its height without converting it to a baseline stop.',ap(27),'high')

# Align code fields with the final code when several decisions affect one span.
next(x for x in decisions if x['id']=='025-p247-lower-index')['final']=r'$(i_{\unsure{0|i}}\colon N\unsure{)}$'
next(x for x in decisions if x['id']=='025-p247-insertion-arc')['final']=a('p247-insertion-arc')['reading'].replace(r'N_0',r'N_{\unsure{0|i}}')
next(x for x in decisions if x['id']=='025-p247-also-placement')['final']=r'''\node at (291,1242) {l12 ``is aspheric''};
\node at (665,1242) {\inserted{also}};
\node at (845,1242) {l-2 ``didn't''};'''
cd=doubt_decisions(R['A'],25,'A')
cd[3].update(reading=r'i_0\colon N_{\unsure{0|i}}\to N',resolved=False,decision='The i index is resolved as0; the independent N index remains0/i.',evidence='Root inspected A12. The first lowered glyph is closed; the second has an open lower cup and detached upper touch. C reader independently flagged the latter.')
cd[9]['evidence']='Raised cancelled quote-like group remains uncertain. The second low continuation group is drawn as a wavy stroke and two points, not normalized to an ellipsis. Root A03 decision supersedes the reader description.'
cd[16].update(reading=r'\deleted{2}',resolved=True,confidence='medium',decision='Resolved2 from curved head, diagonal and low foot; crossing remains clear.',evidence='Root A18 agrees with readers B/C against A’s retained doubt.')
cd[17].update(reading=r'-\deleted{\unsure{13|l13}}',resolved=False,decision='Live minus settled; old13/l13 remains doubtful.',evidence='A19: multiple surviving vertical/loop traces do not exclude initial l; final3 is double-lobed.')
cd[15]['reading']=r"\deleted{should it be $(i_{\unsure{0|i}}\colon N\unsure{)}$\unsure{''}}"
cd[21]['confidence']='medium'
doubts=copy.deepcopy(R['B']['remaining_doubts'])
doubts=[x for x in doubts if x['place']!='p.250 l.13 opener']
for d in doubts:
 d['reading']=d['reading'].replace(r'\unsure{``|`}',r"\unsure{``|'}").replace(r'i_{\unsure{0}}',r'i_{\unsure{0|i}}').replace(r'\unsure{13}',r'\unsure{13|l13}')
 if 'old reference' in d['place']:d.update(alternatives='13; l13',reason='Multiple old vertical/loop strokes survive under the crossing; leading minus is certainly live.')
 if 'after allow' in d['place']:d['confidence']='low'
for ix in [3,5]:doubts.append(copy.deepcopy(R['C']['remaining_doubts'][ix]))
doubts.append(copy.deepcopy(R['A']['remaining_doubts'][12]))
doubts.append(dict(place='p269 final exclamation deletion state',reading=r'\unsure{\deleted{!}|!}',alternatives='included in the cancelled phrase; live uncrossed punctuation',confidence='low',reason='Cancellation passes between stem and point and continues beyond both; no direct intersection settles state.'))
inventory=copy.deepcopy(R['A']['inventory'])
inventory[56]['first_words_or_objects']='2, resolved from surviving numeral contours'
inventory[57]['first_words_or_objects']=r'\unsure{13|l13}, with preceding dash live'
inventory[55]['first_words_or_objects']=cd[15]['reading']
inventory[58]['first_words_or_objects']=r"\unsure{isn't|is'nt} the use of pi0,pi1 slightly confusing here; exclamation state separately uncertain"
inventory[60]['first_words_or_objects']=r'Cond\textsuperscript{n} (ii) should it be i_0:N_{\unsure{0|i}}\to N'
extra=[('drawing','p234 second low continuation group','Wavy stroke followed by two points'),('drawing','p243 above/right of neither','Isolated high point'),('drawing','p267 below insertion gap','Narrow two-legged caret'),('text','p269 end of cancelled question','Exclamation identity certain; deletion state uncertain'),('drawing','p269 outside right rule','Two separated points and lower short horizontal stroke')]
for kind,pos,words in extra:
 inventory.append(dict(sheet_kind='list',hand=inventory[0]['hand'],element='added',kind=kind,position=pos,first_words_or_objects=words,transcribed='yes'))
for i,x in enumerate(inventory,1):x['element']=f'{i:02}'
notes=copy.deepcopy(R['A']['notes'])
notes[3]=notes[3].replace('i_0:N_0 to N','i_0:N with independently uncertain0/i subscript, to N')
notes.append('The raised p234 cancelled cluster and wavy continuation, the p243 high point, the p245 angular mark, long rules, faint left trace and detached right-side marks are reproduced in their relation to the text. Their purpose is not inferred. The lower p247 closing parenthesis and ticks remain doubtful, and also is kept at its observed lower level without deciding its logical attachment. At p269 the terminal ! has a separate live/cancelled state uncertainty.')
notes.append('Scope check S025-aspheric-biconditional (three readers): the four Boolean assignments for independent P and Q make P iff Q false in the two unequal cases. This only checks the bare logical form; no relation between x and u or definition of aspheric is supplied, so it does not refute the contextual claim A tautology it surely is as it stands!. No letter was chosen from this calculation.')
notes.append('Conditional check S025-preimage-formula (reader B): for a map f:X→Y and S⊆Y, f⁻¹(S) consists of x∈X with f(x)∈S and is a subset of X. Thus the displayed notation can be typed as inverse image without requiring an inverse bijection, provided the unavailable definitions give the corresponding domains. This does not prove the written W equality or the complaint that pi_0,pi_1 are undefined here.')
events=[]
for r in 'ABC':
 for e in R[r]['math_checks']:
  pre='preimage' in e['statement_id'];sid='S025-preimage-formula' if pre else 'S025-aspheric-biconditional'
  events.append(dict(statement_id=sid,date='2026-11-20',who_model_effort_run=f'GPT-6 Astra Pro; effort not exposed; /root/scan025_{r.lower()}',type=e['type'] if pre or r!='C' else 'computation or formal certificate',outcome=e['outcome']+f' Note N025.{10 if pre else 9}.'))
notation=copy.deepcopy(R['C']['notation'])
notation=[x for x in notation if x['sign'] not in ['quotation pairs','uncrossed exclamation']]
notation.extend([dict(sign='quotation openers',location='p234 surely; p248 handwritten; p250 l13 its',reading=r"\unsure{``|'}; \unsure{``|'}; ``its''",evidence='Root A02/A15/A17: first two fused counts remain uncertain; final pair has separately formed left stroke and right point.'),dict(sign='cancelled phrase edge',location='p269 terminal exclamation',reading=r'\unsure{\deleted{!}|!}',evidence='A25/C19: continuous cancellation runs through stem/dot gap and beyond the sign. State remains uncertain despite clear exclamation identity.'),dict(sign='old reference minus',location='262',reading=r'-\deleted{\unsure{13|l13}}; \&2',evidence='A19: first dash outside cancellation; no second independent minus after ampersand.'),dict(sign='last small loop',location='263 l19',reading=r'allow\unsure{e|s}',evidence='A20 favours e from loop and exit, retains compact s.')])
coverage='All three final full readings, changes, C doubts/context decisions and inventories compared. Root inspected31 distinct existing crops and3 new crops (two long rules and the p267 insertion geometry). Every reader/witness and reader/reader disagreement was decided on a retained crop; re-displays are not new crops. The inventory has84 rows. Thirteen textual/state doubts remain; unassigned purposes of certain geometric marks are separately explained. H has description only and contributes no rows. Four actual limited mathematical check events are retained; the root performed no additional independent mathematical check. No OCR, external research or compilation.'
rec=write_record(25,'A','brief_v10.md',text,decisions,cd,doubts,notes,coverage,viewed=viewed,events=events,inventory=inventory,notation=notation)
print('Scan025:',len(decisions),'decisions;',sum(x['diff_c'] for x in decisions),'C changes;',len(doubts),'doubts;',len(inventory),'inventory;',len(events),'check events.')
