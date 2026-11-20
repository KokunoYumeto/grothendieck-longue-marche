"""Root adjudication of scan030; original independent returns remain unchanged."""
from common import *
R=load_page(30)
T={r:(W/f'readers/030/{r}/reading.tex').read_text() for r in 'ABC'}
CH={r:{x['id']:x for x in R[r]['changes']} for r in 'ABC'}
def a(i):return next(x for x in R['A']['changes'] if x['id'].startswith(f'030-A-{i:02}-'))
def b(i):return CH['B'][f'030B-{i:02}']
def c(i):return CH['C'][i]
def rel(p):
 p=Path(p)
 if p.is_absolute():return str(p.relative_to(W))
 return str(p)[5:] if str(p).startswith('work/') else str(p)
def ac(i):return rel(a(i)['crop'])
def cc(i):return rel(c(i)['crop'])
def bc(i):return rel(b(i)['crop'])
text=T['C']
def repl(old,new):
 global text
 assert text.count(old)==1,(old,text.count(old))
 text=text.replace(old,new,1)
ref371=r'l\unsure{-|.}14'
repl('p. 371 l.14','p. 371 '+ref371)
word=r'\unsure{unverse|inverse|universe}'
repl(r'\unsure{inverse|unverse|universe}',word)
repl('p 374 l 10','p.374 l 10')
ref377=r'l.-\tikz[baseline=(ref377.base)]{\node[inner sep=0pt] (ref377) {15};\fill[overlay,black!65] ([xshift=.53em,yshift=.60ex]ref377.base west) circle (.035ex);}'
repl('p 377 l.-15','p 377 '+ref377)
mark377=a(4)['reading'].split('\\tikz',1)[1]
repl("l-3 `don't''\n","l-3 `don't'' \\tikz"+mark377+'\n')
closer380=r"\unsure{'|''}"
repl("p 380 l.15 ``don't''","p 380 l.15 ``don't"+closer380)
cross=r"\unsure{\raisebox{1.1ex}[0pt][0pt]{$+$}|``|`}"
repl(c('385-raised-cross')['reading'],cross)
repl(c('386-low-point')['reading'],'l.-11')
repl("l-3 `commuting with''","l.-3 `commuting with''")
repl("p 393 l-10 ``didn't''","p 393 l-10 ``didn't''"+b(8)['reading']+b(9)['reading'])
repl(r"l.-11 \unsure{``|`}\tikz",r"l.-11 \unsure{`|``}\tikz")
text=text.replace('\\scanpage{30}\n','\\scanpage{30}\n% Pale near-vertical strips and the rimmed lower-right spot are material features.\n% Isolated dark marks are reproduced without assigning a writer or textual function.\n',1)
D=[]
def add(i,place,old,final,abc,evidence,crops,confidence='medium',diff=True,kind='other'):
 if isinstance(crops,str):crops=[crops]
 D.append(dict(id='030-'+i,place=place,c=old,h=None,final=final,readers=dict(zip('ABC',abc)),evidence=evidence,crops=crops,confidence=confidence,kind=kind,diff_c=diff,diff_h=False,marked_in_H=False))
def pick(i,ai,bi,evidence=None,final=None,confidence=None):
 x=c(i)
 add(i,x['place'],x['c'],x['reading'] if final is None else final,[a(ai)['reading'] if ai else 'retains witness C',b(bi)['reading'] if bi else 'retains witness C',x['reading']],evidence or x['evidence'],cc(i),confidence or x['confidence'])
add('371-separator','p371 first line reference','l.14',ref371,['l.14']*3,
 'The short group after the looped l consists of two touching lobes at midheight, with appreciable horizontal spread. Root retains a dash/elongated-stop doubt rather than assigning an abbreviation stop from the reference pattern. The point after p is independently clear.', 'readers/030/A/crops/01_ref371.jpg','low')
pick('371-faint-mark',None,None,
 'A faint hooked horizontal and crossing curved upright lie below the opening quotes and immediately before d. Source coordinates distinguish this group around x323–345 from the already transcribed black4 around x283–308. Root initially confused the two in working notes, then corrected that observation by comparing the existing crops. C reader’s separate geometry is retained; origin and character value are unassigned.')
pick('372-reference-point',1,15,
 'A separate low point lies between the upright1 and6, not in the l-to-1 gap. Root follows A/C in preserving that location; B removes the point from its final text. The literal 1.6 is a positional transcription, not a decimal interpretation.',confidence='high')
add('372-word',a(2)['place'],a(2)['c'],word,[a(2)['reading'],b(1)['reading'],r'\unsure{inverse|unverse|universe}'],
 'The joined undotted first strokes most resemble un, while the remaining verse-like ending is readable. Root adopts A/B’s candidate order but retains all three possibilities; grammar does not supply an absent i.',ac(2),'low')
pick('373-recommendation-opener',None,None)
add('374-point',a(3)['place'],a(3)['c'],a(3)['reading'],[a(3)['reading'],'p 374 l 10','p 374 l 10'],
 'A detached low gray-dark point stands between p and3. Root follows A in preserving it.',ac(3),'high')
add('377-reference-point','p377 l.-15, small middle-height mark between digits','l.-15',ref377,['l.-15']*3,
 'The existing B03 crop shows a separate small dark body with a paler short tail between1 and5, above the ordinary baseline point after l. Root preserves the additional visible body once as geometry, without making it a decimal or changing the digits. It is distinct from the low stop already in C.', 'readers/030/B/crops/03.jpg','medium')
add('377-isolated-point',a(4)['place'],'',r'\tikz'+mark377,[a(4)['reading'],b(2)['reading'],'omitted'],
 'A compact upright dark point lies in the blank at the right of the377 row. Root retains A/B’s isolated geometry, with origin and punctuation role unassigned.',ac(4),'high')
add('380-closer','p380 dont, right quotation edge',"don't''","don't"+closer380,["don't''","don't","don't''"],
 'The two long strokes above/right continue from ff in insufficient on the preceding row. A separate short slant lies farther right, outside the reader crops that targeted the opener. Root’s one crop of the previously uncovered closing area shows that slant: neither a confident pair nor complete absence is supported. One visible closer is placed first, a second potentially merged with the neighbouring descender remains possible.', ['readers/030/B/crops/06.jpg','readers/030/C/crops/09_p380_dont_quotes.jpg','crops/030/01_p380_closer_and_ff.jpg'],'medium')
pick('381-reference',5,4,
 'The heavy live numeral has two open-left bowls and a low return, deciding3. The older closed remnants remain compatible with8 but do not settle it. Old/new occupy one glyph space. The preceding short bent horizontal mark favors a dash but still permits an extended stop; root retains B/C uncertainty against A’s certain dash.',confidence='medium')
pick('383-bothering-closer',None,5)
pick('383-suggest-opener',None,None)
pick('385-resp-dots',6,6,confidence='high')
pick('385-raised-cross',None,None,
 'The high cluster has a short stem crossed transversely by another stroke. Root puts the raised plus-shaped reading first, as C’s geometry suggests, but retains the fused double/single quotation alternatives left by A/B. Position is preserved even for the plus candidate; no arithmetic function or missing Formula7 content is supplied.',cross,'low')
D[-1]['readers']['A']=D[-1]['readers']['B']=r'\unsure{``|`|$+$}'
add('386-point-retained',c('386-low-point')['place'],'l.-11','l.-11',['l.-11','l.-11',c('386-low-point')['reading']],
 'The pale low point is separate from l and precedes the higher minus. Its position supports retaining the literal stop already in C. C reader’s geometric encoding does not establish a different reading and is not counted as a change.', 'readers/030/B/crops/14.jpg','medium',False)
add('387-reference',a(7)['place'],a(7)['c'],a(7)['reading'],[a(7)['reading'],a(7)['c'],a(7)['c']],
 'A distinct low point precedes the independent horizontal dash after the looped l. Root follows A in adding the omitted point.',ac(7),'high')
pick('388-terminal-punctuation',8,7,
 'The terminal detached body is oblique and has a curved low end. Comma is favored, but the short heavy contour does not completely exclude an elongated stop. Root retains C reader’s local comma/period doubt against A/B’s certain comma.')
for i in [8,9]:
 x=b(i);add(x['id'],x['place'],x['c'],x['reading'],['omitted',x['reading'],'omitted'],x['evidence'],bc(i),'high')
pick('394-isolated-point',9,10,confidence='high')
D[-1]['c']='' # The actual change is the detached point, not the already present phrase.
pick('395-first-opener',None,None)
pick('395-first-closer',None,None)
pick('396-margin-points',10,11,confidence='high')
op401=r'\unsure{`|``}'
pick('401-formula-opener',11,12,
 'The high opener is one continuous curled body with a small interior prong. Root follows B’s single-first candidate order while retaining fused double as possible. The closing pair and formula letters are independently clear.',op401,'medium')
pick('401-parenthesis-point',12,13,confidence='high')
pick('archive-corner-order',13,14)
add('material-features','Two long pale vertical strips and lower-right rimmed spot','','',['material features']*3,
 'The vertical crops show narrow dark/light bands with pale flanks and uneven fading, distinct from the heavy handwritten strokes; the readers’ once-viewed layout records their continuation. The lower-right two-lobed spot has a diffuse discolored halo and light rim, with no pen trajectory. These are documented as material features, not invented ink rules or text.', ['readers/030/B/crops/10.jpg','readers/030/B/crops/11.jpg','readers/030/A/crops/24_bottom_mark.jpg'],'medium',False)
# All explicit C doubts and the complete contextual decisions are retained and updated.
cd=doubt_decisions(copy.deepcopy(R['A']),30,'A')
updates={0:(word,False,'Undotted joined strokes favor unverse; inverse and universe remain possible.'),
 3:(cross,False,'Raised crossing strokes favor the plus-shaped candidate, but quotation identity remains unresolved.'),
 7:('p. 371 '+ref371,False,'Point after p is clear; the compact horizontal separator after l permits dash or stop.'),
 12:(r"bothering\unsure{''|'}",False,'The fused terminal group leaves paired versus single stroke count uncertain.')}
for i,(rd,res,ev) in updates.items():
 cd[i].update(reading=rd,resolved=res,evidence=ev+' Crop: '+rel(R['A']['c_doubts'][i]['crop']),decision=('Resolved/confirmed: ' if res else 'Retained/revised: ')+rd)
# Explicitly record the 381 separator independently of the buried numeral.
cd.append(dict(place='p381 separator after l',c='l.',reading=r'l\unsure{-|.}',resolved=False,confidence='medium',decision=r'Retained/revised: l\unsure{-|.}',evidence='Short bent horizontal/low body permits dash or elongated stop. Crop: readers/030/A/crops/08_ref381.jpg',crop='readers/030/A/crops/08_ref381.jpg'))
doubts=[]
def doubt(place,rd,alt,why,conf='medium'):
 doubts.append(dict(place=place,reading=rd,alternatives=alt,confidence=conf,reason=why))
doubt('p371 reference separator',ref371,'dash; elongated stop','Two touching lobes are short and horizontal.','low')
doubt('p372 final word',word,'unverse; inverse; universe','Initial joined minims lack a decisive independent dot.','low')
doubt('p373 recommendation opener',r'\unsure{``|`}','double; single','Two limbs share one apex.')
doubt('p380 closing mark',closer380,'one visible closer; possible fused second closer','One detached slant survives to right of ff descenders; no distinct second partner.')
doubt('p381 separator',r'\unsure{-|.}','dash; elongated stop','Low short bent horizontal group.')
doubt('p381 old digit',r'\deleted{\unsure{8}}','8 favored; hidden old contour','Live3 obscures the older loops.','low')
doubt('p383 bothering closer',r"\unsure{''|'}",'double; single','A thick joined patch has unequal pendant branches.')
doubt('p383 suggest opener',r'\unsure{``|`}','double; single','One unbroken arch with two low ends.')
doubt('Formula7 preceding mark',cross,'raised plus-shaped cross; double quotation; single quotation','Transverse strokes decide visible cross shape, but not the underlying sign identity.','low')
doubt('p387 cancelled ending',r'\deleted{\unsure{s}}','s favored; interior hidden','Oblique cancellation covers the lower curve.','low')
doubt('p388 terminal mark',r'\unsure{,|.}','comma; period','Short descending oblique with curved foot.')
doubt('p395 interpreted opener',r'\unsure{``|`}','double; single','Unequal limbs meet at top.')
doubt('p395 saying closer',r"\unsure{''|'}",'double; single','Two lower tips share one angled upper mass.')
doubt('page reference after396',r'p.39\unsure{7|1}','397;391','Short top hook and descending stem do not exclude1.')
doubt('p401 formula opener',op401,'single; double','One continuous body with short interior prong.')
doubt('archive corner, comment only','23 (possibly29)','23;29','Open upper turn favors3 but blurred closure permits9.')
# Inventory: all59 distinct entries, then nested items at their actual positions.
base=copy.deepcopy(R['C']['inventory'][:59]); nested={}
def ins(i,x):nested.setdefault(i,[]).append(copy.deepcopy(x))
for ai,anchor in [(59,17),(60,22),(61,22),(62,38),(63,40),(64,42),(65,14),(66,47),(67,51),(68,58)]:ins(anchor,R['A']['inventory'][ai])
ins(0,R['C']['inventory'][66]);ins(37,R['C']['inventory'][62])
for anchor,position,label in [(12,'within p377 reference, between1 and5','small separate middle-height dark point'),(46,'right and above p393','small isolated round point'),(46,'farther right of p393','short isolated descending slant')]:
 ins(anchor,dict(sheet_kind='list',hand='origin unassigned',element='added',kind='drawing',position=position,first_words_or_objects=label,transcribed='yes'))
inv=[]
for i,x in enumerate(base):
 inv.append(x);inv.extend(nested.get(i,[]))
inv.append(copy.deepcopy(R['A']['inventory'][69]))
for i,x in enumerate(inv,1):
 x['element']=f'{i:02}'
 if x['hand']=='his hand':x['hand']='another unnamed hand'
 if x['kind']=='drawing':x['hand']='origin unassigned'
 if x['position']=='nested in the Formula (7) row, raised before congruence sign':x['first_words_or_objects']=cross
 if x['position'].startswith('386 l-11'):x['position']=x['position'].replace('l-11','l.-11',1)
notes=copy.deepcopy(R['C']['notes'])
notes[4]='At p385, Formula (7) is followed by a raised cross-shaped mark with plus/quotation identity unresolved, the congruence sign, a closing quote pair and missing. The referenced formula is absent; no inference about its intended contents is made.'
notes += ['The point in the first372 reference is physically between1 and6. The377 reference has an additional small midheight point between1 and5. These positions do not assert decimal page/line references.',
 'At380, the two long nearby strokes belong to ff on the preceding row. One additional closing slant is separately visible; the possibility of a second merged stroke stays marked. Several other joined quotation groups remain locally uncertain and are not normalized to a page-wide pattern.',
 'The faint low group before the first correction, several separate points and a short marginal slant are drawn with origin and textual function unassigned. Gray vertical strips and the rimmed bottom-right spot are documented as material features.',
 'This is a correction list in an unnamed hand, with no secure named attribution on the sheet. There is no title, composition date, signature, own manuscript pagination or stated page total. Archive23/29 remains comment-only.',
 'All three readers and root treated the supplied formula fragments as not constituting a checkable mathematical argument. No proof/computation/check event is claimed; H has description only and produces no textual collation rows.']
notation=[dict(sign='l and point/dash position',location='p371,372,377,381,386,387',reading=ref371+'; l 1.6; l.17; l.21; l.-15 with separate middle point; '+r'l\unsure{-|.}'+' before overwritten3; l.-11; l.-3',evidence='Individual crops distinguish physical points, numeral strokes and short horizontal marks; no uniform punctuation is imposed.'),
 dict(sign='overwritten reference',location='p381',reading=c('381-reference')['reading'],evidence='One physical glyph space: clear live3 over tentative old8.'),
 dict(sign='raised cross before congruence',location='Formula7',reading=cross+r'$\cong$',evidence='Cross-shaped high mark remains plus/quotation uncertain; relation has one wave over two bars.'),
 dict(sign='continuation points',location='p372 and385',reading=r'\ldots{}; (resp. with....)',evidence='Three dots after small and first with; four separated low bodies after inner with.'),
 dict(sign='underlines',location='p379;386',reading=r'\uuline{with}; \uline{is}',evidence='Two rules under with; one confined to is.'),
 dict(sign='single/double quotation counts',location='individual edges throughout030',reading=r"Local doubles and genuine singles retained; uncertainties at373,380,383 twice,395 twice,401. The380 closer is \unsure{'|''} and401 opener \unsure{`|``}.",evidence='Each crop read independently; ff descenders, i dots and material strips are not duplicated as quotation marks.'),
 dict(sign='ordinary formula letters',location='p401',reading=r'$(k-M)$',evidence='Plain lowercase k, minus, ordinary capital M, round parentheses; no interpretation inferred.'),
 dict(sign='section mark',location='second101 reference in p373 block',reading=r'line 3 of 101; \S101 l.11',evidence='Only second101 has the linked curved section sign.'),
 dict(sign='terminal punctuation',location='p388',reading=r'usual\unsure{,|.}',evidence='Descending low body favors comma, but an elongated stop remains possible.')]
root_crop_map={'030-372-reference-point': '02_ref372.jpg', '030-373-recommendation-opener': '05_quote373.jpg', '030-381-reference': '08_ref381.jpg', '030-383-bothering-closer': '09_quote383_bothering.jpg', '030-383-suggest-opener': '10_quote383_suggest.jpg', '030-385-resp-dots': '11_dots385.jpg', '030-385-raised-cross': '12_formula385.jpg', '030-388-terminal-punctuation': '25_punctuation388.jpg', '030-394-isolated-point': '22_mark394.jpg', '030-396-margin-points': '23_marks396.jpg', '030-401-formula-opener': '19_formula401.jpg', '030-401-parenthesis-point': '19_formula401.jpg', '030-archive-corner-order': '20_corner.jpg'}
for x in D:
 if x['id'] in root_crop_map:x['crops']=['readers/030/A/crops/'+root_crop_map[x['id']]]
viewed=json.loads((W/'records/root_030_viewed.json').read_text())
coverage='All three final readings, changes, six explicit C uncertainty loci, archive uncertainty, contextual decisions, notes and inventories compared. Root viewed39 existing reader crops and one new crop covering the previously uncovered p380 closer and connecting ff descenders; all actual disputes were adjudicated. Every separate correction entry and nested mark is inventoried in physical order. C_context extraction was corrected equally for all readers without reopening page/half images. No OCR, outside research or compilation was used.'
rec=write_record(30,'A','brief_v14.md',text,D,cd,doubts,notes,coverage,viewed=viewed,events=[],inventory=inv,notation=notation)
print('scan030',len(D),'decisions',sum(x['diff_c'] for x in D),'Cchanges',len(doubts),'doubts',len(inv),'inventory',rec['crop_counts'])
