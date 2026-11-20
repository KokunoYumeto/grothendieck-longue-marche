"""Root adjudication, scan029. Independent reader returns are immutable."""
from common import *
R=load_page(29)
T={r:(W/f'readers/029/{r}/reading.tex').read_text() for r in 'ABC'}
CH={r:{x['id']:x for x in R[r]['changes']} for r in 'ABC'}
def a(n):return CH['A'][f'A29-{n:02}']
def b(i):return CH['B'][i]
def c(i):return CH['C'][i]
def ap(i):return f'readers/029/A/crops/{i:02}.jpg'
def bp(i):return f'readers/029/B/crops/{i:02}.jpg'
def cp(i):return f'readers/029/C/crops/{i:02}.jpg'
text=T['C'];replacements=[]
def repl(old,new):
 global text
 assert old in text,old
 text=text.replace(old,new,1);replacements.append((old,new))
repl(c('upper-right-stroke')['reading'],a(2)['reading'])
indop=r"\unsure{``|'}"
repl(r'l-10 ``\unsure{\uuline{i}|\uline{i}}',r'l-10 '+indop+r'\unsure{\uuline{i}|\uline{i}}')
repl("do you mean ``from",r"do you mean \unsure{``|'}from")
repl(r'\unsure{s|?}',r'\unsure{?|s}')
repl("p362 l.7 'interpret''",r"p362 l.7 \unsure{'|``}interpret''")
# The detached low gray point is not silently identified as a baseline full stop.
perhaps=r'\tikz[baseline=(perhaps29.base)]{\node[inner sep=0pt] (perhaps29) {perhaps};\fill[black!45] ([xshift=1.55em,yshift=-1.0ex]perhaps29.base east) circle (.045ex);}'
repl('``and even\'\' perhaps\n',"``and even'' "+perhaps+'\n')
foot=r'''\margin{\begin{tikzpicture}[x=1ex,y=1ex]
\node[rotate=24,inner sep=0pt] (end29) at (0,0) {\deleted{\unsure{end|ed}}};
\draw[black!45,line width=.22pt] (-1.7,-.55)--(1.5,.90);
\draw[black!40,line width=.20pt] (-1.6,-.35)--(1.35,.60);
\draw[line width=.22pt] (-.45,-.95)--(-.40,-.65);
\draw[line width=.22pt] (.35,-.82)--(.42,-.57);
\end{tikzpicture}}'''
repl(r'\margin{\deleted{\unsure{end|ed}}}',foot)
D=[]
def add(i,place,old,final,abc,evidence,crops,confidence='medium',kind='other',diff=True):
 D.append(dict(id='029-'+i,place=place,c=old,h=None,final=final,readers=dict(zip('ABC',abc)),evidence=evidence,crops=crops if isinstance(crops,list) else [crops],confidence=confidence,kind=kind,diff_c=diff,diff_h=False,marked_in_H=False))
def pick(ci,ai,bi,crops,evidence=None,final=None,confidence=None):
 x=c(ci);av=a(ai)['reading'] if ai else 'retains witness C';bv=b(bi)['reading'] if bi else 'retains witness C'
 add(ci,x['place'],x['c'],x['reading'] if final is None else final,[av,bv,x['reading']],evidence or x['evidence'],crops,confidence or x['confidence'])
pick('top-material',1,'top-mark',cp(1),
 'The angular dark patch has an ochre/orange continuation and irregular material edge. Root follows A/C in treating it as a surface blemish, not the written apostrophe in witness C or B’s unassigned drawing. The nearby left points are separately preserved.',confidence='medium')
pick('left-points',None,None,cp(1),'Two discrete dark points lie left of the p336 reference, below the material patch. Root retains C reader’s separated geometry, with origin unassigned.')
pick('upper-right-stroke',2,'upper-right-trace',ap(15),
 'A distinct short bowed dark vertical core and two detached paler remnants stand to its upper-right. Root retains A’s three-part geometry, not a continuous connection; physical origin and letter value remain unassigned.',a(2)['reading'])
pick('perhaps-stop',None,'perhaps-stop',ap(1),
 'There is no dark baseline stop immediately following s. A small gray point lies substantially lower and farther right. A treats it as the terminal stop; B/C omit it. Root preserves the point geometrically at its lower position without identifying a sentence stop.',perhaps,'medium')
pick('better-stop',3,'better-mark',ap(3),
 'The filled low body has an oblique descending left tail. Root favors comma but does not regard its very short tail as sufficient to exclude an oblique period, retaining B/C’s uncertainty against A’s certain comma.')
pick('341-opener',4,'doesnt-opener',ap(4))
pick('342-reference',5,'342-reference-point',ap(5),confidence='high')
pick('again-tail',6,'again-terminal',ap(8),confidence='high')
pick('350-short-word',7,'also-short-word',ap(9))
add('350-opener','p350 l-10, opener before independent','``',indop,['``']*3,
 'Root observes one joined upright mass and a short left branch before the separately dotted i. The original count is not securely separable. A local double/single doubt is added rather than transferring a confident pair from another occurrence.',ap(10),'medium')
pick('351-overwrite-placement',8,'overwritten-a',ap(11),confidence='high')
pick('353-opener',9,'353-opener',ap(12))
add('355-opener','p355 l-3, opener before from','``',r"\unsure{``|'}",['``',b('from-opener')['reading'],'``'],
 'Two short downward legs meet at a pointed apex. The fused pair is favored but a single bent mark is possible. Root adopts B’s local uncertainty; the parenthesized six-rayed asterisk and closing pair are clear.',bp(12),'medium')
add('Formulae-retain','p356 cancelled word',r'\unsure{Formulae|Formulæ}',r'\unsure{Formulae|Formulæ}',[a(10)['reading'],b('formulae-ending')['reading'],r'\unsure{Formulae|Formulæ}'],
 'The final rounded bodies are discernible but the joining area is crossed densely. Root agrees with C reader that ordinary connected ae and a ligature cannot be securely distinguished; A/B’s resolution is not adopted.',ap(16),'medium','other',False)
pick('356-B',11,'formula-reference-B',ap(17),confidence='high')
pick('357-page',None,'page-357',ap(20),
 'The last digit retains a faint short top ending at the right corner and an independent descending leg. These visible contours decide 7 despite the faded material strip. Root adopts B/C’s resolution over A’s retained uncertainty. Adjacent numbering does not supply the digit.',confidence='medium')
D[-1]['readers']['A']=r'p\unsure{357}'
pick('357-star',None,'f-star',[ap(19),cp(19)],
 'Two distinct short oblique upper rays survive above the broad cancellation, in addition to a vertical component and transverse arm. Root agrees with B/C that these extra rays distinguish the asterisk from a simple plus; A retains the alternative.',confidence='medium')
D[-1]['readers']['A']=r'f^{\unsure{*|+}}'
add('357-terminal','p357 cancelled formula, final sign',r'\unsure{s|?}',r'\unsure{?|s}',[a(12)['reading'],r'\unsure{s|?}',r'\unsure{s|?}'],
 'A small curved surviving body has a distinct low point beneath it. Root follows A’s question-mark-first order, but the overwritten upper contour still permits an s-like remnant. No mathematical completion is inferred.',[ap(19),cp(19)],'low')
pick('358-been-opener',13,'been-opener',ap(21))
pick('358-commutes-opener',14,'commutes-opener',ap(22),
 'One dark upright is followed by a distinct paler high point. A/B count it as the second quotation stroke. Root follows C’s uncertainty because the short pale body can be a degraded second quote or an isolated point; it is not silently omitted.')
pick('358-commutes-point',15,'commutes-point',ap(22),
 'The small separate black point above the first m is distinct from both opening marks and from any normal i dot. It is drawn once at its observed position, with function unassigned.')
pick('359-page',None,'page-359',ap(23),
 'The last numeral retains an upper bowl fragment and a descending right stem. Root agrees with B/C that these strokes support 9 despite the faded middle; A’s doubt is recorded but not retained. No sequence-based completion is used.',confidence='medium')
D[-1]['readers']['A']=r'p\unsure{359}'
pick('360-reference-points',16,'360-reference-marks',ap(25),confidence='high')
pick('360-quote-point',17,'360-opening-point',[ap(24),cp(23)])
pick('361-opener',18,'361-opener',ap(27),
 'One dominant hook has a joined shorter oblique prong. Root favors single/fused-double, as A/C, rather than B’s reversed candidate order. The count itself remains unresolved.')
add('362-opener','p362 l.7, opener before interpret',"'",r"\unsure{'|``}",[a(19)['reading'],b('362-opener')['reading'],"'interpret''"],
 'A tall left arm and a short joined right branch form a single connected body. Root follows A/B in leaving one versus fused two uncertain, against C reader’s confident single.',ap(28),'medium')
pick('right-points',20,'right-margin-dots',ap(14))
pick('365-opener',21,None,ap(29))
pick('369-opener',22,'369-opener',ap(31),
 'A long bent stem has a shorter joined right prong. The preceding low comma belongs to the line reference, not this high group. Root keeps A/C’s single-first uncertainty; B’s double-first alternative is recorded.')
add('bottom-placement','Extreme bottom right, cancelled end/ed',r'\margin{\deleted{\unsure{end|ed}}}',foot,[r'\margin{\deleted{\unsure{end|ed}}}']*3,
 'The faint letter group slopes upward to the right beneath multiple oblique returned crossings. The low edge clips short dark tails. Root preserves slant, repeated crossings and visible low remnants; end/ed remains uncertain and no clipped completion is invented.',ap(32),'medium','insertion or placement')
add('vertical-material','Two pale near-vertical surface traces','','',['material creases']*3,
 'The local crops show narrow bright strips bordered by gray shadows and irregular weakening of crossed ink. These support the readers’ material-crease interpretation; root does not add ink rules or count a C change.',[ap(13),ap(14)],'medium','other',False)
# Explicit C doubts and supplied context are recorded independently of change counts.
cr=copy.deepcopy(R['C'])
for x in cr['c_doubts']:
 if (x.get('crop') or '').startswith('work/'):x['crop']=str(W/x['crop'][5:])
cd=doubt_decisions(cr,29,'C')
cd[7].update(reading=r'\unsure{?|s}',evidence='Root A19/C19: distinct low point favors question mark; crossed upper curve still permits s.',decision=r'Retained/reordered: \unsure{?|s}')
for j in [18,19,20,21,22,23]:
 x=copy.deepcopy(R['A']['c_doubts'][j])
 if j==18:x.update(reading="? ``and even'' "+perhaps,resolved=False,evidence='Root A01 distinguishes no baseline period from a lower detached gray point; question and perhaps remain certain.')
 if j==19:x.update(reading=r'is perhaps better\unsure{,|.}',resolved=False,evidence='Root A03: comma-shaped low stroke still permits period.')
 if j==21:x.update(reading=r"do you mean \unsure{``|'}from $(*)$''",resolved=False,evidence='Root B12: question wording and star clear; joined opener count uncertain.')
 if j==23:x.update(reading=r'\deleted{\unsure{Formulae|Formulæ} $(2)$ and $(B)$ are unreadable. Are they}',resolved=False,evidence='Root A16–18: full cancelled complaint retained, B resolved, ae/ligature unresolved.')
 x['decision']=('Resolved/confirmed: ' if x.get('resolved') else 'Retained/revised: ')+x['reading'];cd.append(x)
doubts=copy.deepcopy(R['C']['remaining_doubts'])
doubts[7].update(reading=r'\unsure{?|s}',alternatives='?; s',reason='A separate low point favors question mark; the overwritten upper curve remains ambiguous.')
for place,reading,alternatives,reason in [
 ('p350 l-10, opener before independent',indop,'double; single','Joined upright mass and small side branch.'),
 ('p355 l-3, opener before from',r"\unsure{``|'}",'double; single','Two legs joined at one apex; stroke count uncertain.'),
 ('p362 l.7, opener before interpret',r"\unsure{'|``}",'single; double','Tall arm and shorter connected branch.'),
 ('p338, detached low point after perhaps',perhaps,'sentence stop; unassigned isolated point','Point lies well below/right of the final word, so punctuation function is not assigned.'),
 ('p345, bar joined to closing parenthesis',c('again-tail')['reading'],'punctuating extension; nonpunctuating pen stroke','Geometry is certain; textual function is not established.')]:
 doubts.append(dict(place=place,reading=reading,alternatives=alternatives,confidence='medium',reason=reason))
# C inventory is already ordered by physical entries; insert nested additions in place.
inv=copy.deepcopy(R['C']['inventory'])
for x in inv:
 for old,new in replacements:x['first_words_or_objects']=x['first_words_or_objects'].replace(old,new)
 if x['kind']=='drawing' and 'right margin below' in x['position']:x['first_words_or_objects']='Short bowed dark vertical and two detached paler remnants; origin unassigned'
 if x['position']=='nested in bottom-right marginal note':x['first_words_or_objects']='Multiple oblique returned crossings and two low clipped traces'
for anchor,entry in [('upper group, entry 3',dict(kind='drawing',position='below/right of perhaps in p338 entry',first_words_or_objects='Detached low gray point, function unassigned')),('nested in p351 inadequacies',dict(kind='text',position='same glyph space over old a/o in p351',first_words_or_objects='live a overlapping cancelled old vowel')),('inside p357 entry',dict(kind='display',position='nested cancelled mathematical expression in p357',first_words_or_objects=r'$(2)\quad f^{*}(\unsure{\beta|g|S}_{\unsure{M|m}})\unsure{=|-}\unsure{?|s}$'))]:
 ix=next(i for i,x in enumerate(inv) if anchor in x['position'])
 entry.update(sheet_kind='list',hand='another unnamed hand',element='added',transcribed='yes');inv.insert(ix+1,entry)
for i,x in enumerate(inv,1):x['element']=f'{i:02}'
notes=copy.deepcopy(R['C']['notes'])
notes += ['The crossed reference (B), page references357 and359, and the raised asterisk on f are resolved from surviving strokes. The formula remains cancelled and its argument, subscript, relation and last sign remain physically uncertain; the final candidate order is ?/s because a separate low point survives.',
 'The joined bar after again is reproduced as part of the closing delimiter. The lower isolated point after perhaps is preserved without calling it a sentence stop. Fused quotation groups are judged individually, including the root-added uncertainty before independent.',
 'The top-left orange-black blemish and two pale vertical creases are treated as material features. Discrete marginal points and short traces are drawn with physical origin and textual function unassigned. The bottom-right cancelled word is slanted and clipped at the low paper edge.',
 'This is an editorial list in an unnamed hand; no named writer is inferred. Sent6/2/84 is a dispatch annotation, not an asserted composition date. No title or total page count is supplied; archive28 is a comment only.',
 'H has description only and contributes no textual collation rows. Undefined cancelled formula fragments provide no complete mathematical claim to verify; there is no actual mathematical check event on this page.']
notation=copy.deepcopy(R['C']['notation'])
notation[2]['reading']=notation[2]['reading'].replace(r'\unsure{s|?}',r'\unsure{?|s}')
notation[2]['evidence']+=' Root A19/C19 places ? first because of the detached low point.'
notation[5]['reading']='Literal pairs/singles retained; fused openers locally uncertain at p341,350,353,355,358 twice,361,362,365 and369.'
notation += [dict(sign='ae/æ under cancellation',location='p356',reading=r'\unsure{Formulae|Formulæ}',evidence='Root A16 retains the joined ending against A/B resolution; cancellation crosses the relevant junction.'),dict(sign='detached low point after perhaps',location='p338',reading=perhaps,evidence='Root A01: its low/right location is retained without assigning a stop. No normalization to scan028.')]
viewed=json.loads((W/'records/root_029_viewed.json').read_text())
if cp(23) not in viewed:viewed.append(cp(23))
(W/'records/root_029_viewed.json').write_text(json.dumps(viewed,indent=2))
coverage='Three final full readings, literal changes, explicit C doubts, context decisions, notes and complete inventories were compared. Root viewed all33 A crops plus C01/C19/C23 and B12,37 distinct existing crops in total; no new crop was necessary. All reader/witness and reader/reader differences were adjudicated, including rejected ae resolution, candidate-order differences, material/ink treatment and quotation counts. All14 explicit C uncertainty macros have recorded decisions; four are resolved, one is reordered, the others retained. The shared upper text was judged independently from scan028. No recognition, outside research or compilation was used.'
rec=write_record(29,'C','brief_v14.md',text,D,cd,doubts,notes,coverage,viewed=viewed,events=[],inventory=inv,notation=notation)
print('scan029',len(D),'decisions',sum(x['diff_c'] for x in D),'Cchanges',len(doubts),'doubts',len(inv),'inventory',rec['crop_counts'])
