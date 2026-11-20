"""Main-reader adjudication after the three complete scan-151 returns and 18 crop views."""
from pathlib import Path
import copy,json,re
from adjudication_io import PageDecision,OUT

p=PageDecision('134-2_scan151','v06',base='r1')
r1,r2,r3=(p.readers[r] for r in ('r1','r2','r3'))
cm={
1:'r1/01_opening_noun.png',2:'r1/01_opening_noun.png',
3:'main/chaines.jpg',4:'r1/02_comm.png',
5:'r3/chain_subscript.png',6:'r3/chain_subscript.png',7:'r3/chain_subscript.png',
8:'main/chain_late_links.jpg',9:'main/chain_late_links.jpg',
10:'r1/04_action_theta.png',11:'main/opening_quote.jpg',
12:'r1/07_addition_end.png',13:'r1/07_addition_end.png',
14:'r1/05_addition_start.png',15:'r1/05_addition_start.png',
16:'r1/06_addition_middle.png',17:'r1/06_addition_middle.png',
19:'r1/07_addition_end.png',20:'r1/07_addition_end.png',
21:'r2/07_note_guide.png',22:'r2/08_candidates.png',
23:'main/separator.jpg',24:'r1/09_initial_dot.png',
25:'main/homology_guide.jpg',26:'r1/10_existent_comma.png',
27:'r1/10_existent_comma.png',28:'r1/10_existent_comma.png',
29:'r1/11_ouvrent.png',30:'r1/12_naives.png'}
for n,crop in cm.items():
    p.change(n,crop=p.crop(crop),decision='Main reader inspected this crop and accepts the reading and visible state described here.')

p.change(1,readers={'r1':r'\unsure{groupe|groupes}','r2':'groupe','r3':r'\unsure{groupe|groupes}'},
    decision='Retain the uncertainty: the long low exit after p has a downturned end but does not securely separate e from a compressed es. Singular is the first ink reading; the preceding page is not used to force agreement.')
p.change(2,readers={'r1':r'\unsure{formel|formels}','r2':'formel','r3':r'\unsure{formel|formels}'},
    decision='Retain the uncertainty: a clear l loop runs into a long horizontal exit with a hooked end, which does not securely establish or exclude a final s.')
p.change(3,evidence='The i has one compact detached point. No two-sided roof stroke appears above it; chaines is unaccented.',
    decision='Keep the unaccented C reading against H’s circumflex.')
p.change(4,evidence='The abbreviated word has c, a closed o and two flattened m groups. The last exit bends down without a following baseline point. Two separate low specks lie beneath the word rather than at its end.',
    decision='Resolve C’s punctuation doubt as comm, without expanding the abbreviation.')
for n in (5,7,8,9):
    p.change(n,decision='Keep the actual single hooked shaft. The right end turns upward once; it does not have the two diagonal legs of the separately visible final arrowhead.',
        math_consequential=True,
        consequence='Preserves the drawn hooked connector instead of substituting a complete arrowhead; this does not infer a different mathematical direction.')
p.change(6,confidence='medium',
    evidence='After n and the short minus is a small curved descending tick. It is much shorter and more curved than the independently visible subscript 1 farther right. A reduced numeral remains possible.',
    decision='Place comma first and 1 second in the doubt, following the shape rather than the expected descending index sequence.',
    math_consequential=True,
    consequence='The second chain subscript remains uncertain; the comma-like mark is now first rather than silently regularising it to 1.')
p.change(10,decision='Retain the same case doubt recorded locally by all three readers: a broad barred oval with an open upper-left join does not securely distinguish Theta from theta.',
    math_consequential=True,consequence='Retains the unresolved case of the action letter instead of H’s unqualified lowercase theta.')
p.change(11,evidence='Two separate raised strokes precede types, one longer and curved and the other shorter; they do not form guillemets.')
p.change(12,evidence='Two separate nearly upright raised strokes follow n. Their paired quotation form is clear in the existing addition-end crop.')
p.change(14,final=r'\unsure{mesurant}',against_c=True,against_h=False,confidence='medium',
    readers={'r1':r'\unsure{mesurant}','r2':r'\unsure{mesurant|ou encore}','r3':r'\unsure{ou encore}'},
    evidence='The first group has a descending left stem and two humps, favouring m; the following low groups support es/ur and a compressed ending. There is no clear initial closed o. The complete final letters remain insufficiently separated.',
    decision='Prefer mesurant with a doubt, as H and r1, rather than carrying ou encore as the first reading. The uncertainty concerns the compressed whole word.')
p.change(15,crop=p.crop('r1/05_addition_start.png')+'; '+p.crop('r2/07_note_guide.png'),
    evidence='The margin immediately before the first small word is blank: no ellipsis or separate opening parenthesis occurs there. The curved form before As-tu joins continuously to the long insertion guide.',
    decision='Do not duplicate the guide’s curved left end as a literal opening parenthesis. Preserve the continuous graphic and the separately written final ellipsis and closing parenthesis.')
p.change(16,decision='Keep hom without a point: the low terminal exit belongs to m and is followed by a clear gap.')
trunc=r'\unsure{tronqués|tronques|tr. \deleted{qués}}'
p.change(17,final=trunc,confidence='low',
    readers={'r1':r'\unsure{tronqués|tr. \deleted{qués}}','r2':r'tronqu\unsure{é|e}s','r3':r'\unsure{tronqués|tr. \deleted{qués}}'},
    evidence='A crossed t and r-like shoulder are followed by a small round low mark, a horizontal continuation and small q/u/e/s-like strokes. The long descender from the full-size q above crosses the same region. The horizontal continuation can belong to compressed live writing or a cancellation; a separate acute cannot be established securely.',
    decision='Keep the live word first, include the unaccented live alternative prompted by r2, and preserve the possible abbreviated-plus-deleted state as an alternative inside the outer unsure. No definite deletion is asserted.')
p.change(19,evidence='The small word has t, o and a descending p. The long stroke above and to its right comes from the g in the full-size line above; there is no separate terminal point.',
    decision='Keep top without H’s added full stop.')
p.change(20,final=r'ponctu\unsure{e|é}s',confidence='medium',
    readers={'r1':r'ponctu\unsure{e|é}s','r2':r'ponctu\unsure{é|e}s','r3':r'\unsure{ponctues|ponctués}'},
    evidence='After p/o, low n/c groups lead to a tall t and a u group before the final vowel and s. This supports ponctues rather than pointés. No independent acute is clearly separated above the last vowel.',
    decision='Keep unaccented e first and accented é as an alternative, following r1/r3’s ordering; the word itself remains ponctues/ponctués.')
guide1=r"""\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw (0,0) .. controls (-0.08,0.30) and (-0.05,0.48) .. (0.20,0.53) .. controls (0.90,0.64) and (2.90,0.47) .. (3.30,0.60) -- (3.32,0.72);
\node[inner sep=0pt] at (0.27,0.38) {\unsure{.}};
\end{tikzpicture}}"""
p.change(21,final=guide1,readers={
    'r1':'Continuous guide, before As-tu; small internal point treated as nontextual.',
    'r2':'Continuous guide, before As-tu; uncertain point retained at its position inside the figure.',
    'r3':'Continuous guide after the question; uncertain point rendered before As-tu.'},
    decision='Use the continuous left curve, long rule and short right upturn. Put the figure before As-tu, matching its vertical source position. Keep the small point spatially inside the figure; its separate doubt is recorded in its own entry. Numerical TikZ scale differences are not separate readings.')
p.change(22,final=r'\unsure{candïdats|candidats}',against_c=False,against_h=True,confidence='medium',
    readers={'r1':'candïdats','r2':r'\unsure{candïdats|candidats}','r3':r'\unsure{candïdats|candidats}'},
    evidence='Two close dark upper dots are visible near the i position, but there is a third close mark and another isolated dot over the earlier part of the word. Their intentional status cannot be made certain.',
    decision='Retain the C doubt rather than r1’s certain diaeresis; candïdats remains first from the paired upper marks.')
p.change(23,evidence='One separate long, gently bowed horizontal pen stroke lies in the blank band between paragraphs; no heading words occur with it.',
    decision='Preserve C’s drawn separator, omitted from H.')
p.change(24,decision='Retain the uncertainty of intention: a detached short thick mark stands to the left of Tes, without enough structure to establish a deliberate textual point.')
guide2=r"""\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw (0,0) -- (0.24,0.64) .. controls (1.20,0.68) and (2.68,0.56) .. (3.45,0.53) -- (3.44,0.65);
\end{tikzpicture}}"""
p.change(25,final=guide2,readers={
    'r1':'Guide reproduced after the lower paragraph; attachment to the gap after bidualité stated in a comment.',
    'r2':'Guide reproduced before the lower paragraph, under the inserted words; attachment after bidualité stated in a comment.',
    'r3':'Guide reproduced after the lower paragraph; attachment after bidualité stated in a comment.'},
    evidence='A slanted left leg descends into the gap after bidualité, joining a long nearly horizontal guide under et d’homologie and a short upturn at the far right. The g descender meets this line but is not an additional underline.',
    decision='Reproduce the guide before the lower paragraph, in its source vertical order, and identify its actual attachment in the adjacent comment. Keep the inserted words at the text insertion point.')
p.change(26,final=r'\unsure{,}',against_c=False,against_h=True,confidence='medium',
    readers={'r1':',','r2':r'\unsure{,}','r3':r'\unsure{,}'},
    evidence='The low detached mark after existent has a dark angular head, a descending left spur and a rightward protrusion. Its position supports a comma, but its thick irregular shape does not settle its deliberate punctuation status.',
    decision='Retain C’s comma uncertainty instead of adopting r1’s certainty.')
p.change(27,final=r'd\unsure{è|é}s',readers={'r1':r'\unsure{dès|dés}','r2':r'd\unsure{è|é}s','r3':'dès'},
    decision='Retain the direction doubt: the detached accent is compact and nearly vertical. Grave is first, but its outline does not exclude acute.')
p.change(28,readers={'r1':r'\unsure{â|à}','r2':'à','r3':'à'},
    decision='Keep the roof-like accent first: a short rising left side joins a longer falling right side. A hooked grave remains possible; spelling does not decide it.')
p.change(29,final='ouvrent',evidence='The final-line verb starts with o, followed by low u/v strokes, an ascending r shoulder, then e/n and a crossed terminal t. No internal i dot supports envoient.',
    decision='Resolve C’s word doubt as ouvrent. The unchanged m’ on the preceding physical line was independently read by all three readers and is not a disputed addition or deletion.')
p.change(30,final=r'\unsure{noïves|naïves}',readers={'r1':r'\unsure{noïves|naïves}','r2':r'\unsure{noïves|naïves}','r3':r'\unsure{noïves|naïves|noires}'},
    evidence='The second letter is a closed oval without a distinct a stem. Two dark marks stand above the next short i. The following letter is a low rounded v, unlike the ascending r shoulder in the adjacent verb crop.',
    decision='Keep noïves first and naïves second. Do not retain noires as an additional preferred reading: it does not account for the two upper marks and the rounded v.')

# The two leq/leqslant entries represent the same inequality and are excluded
# from both difference tables. All readers inspected both actual bounds.
p.data['changes']=[x for i,x in enumerate(p.data['changes'],1) if i not in (13,18)]
point=copy.deepcopy(r2['changes'][18])
point.update(final=r'\unsure{.} at its position inside the first insertion-guide figure',
    crop=p.crop('r2/07_note_guide.png'),
    readers={'r1':'Point seen but not transcribed; judged off-baseline/nontextual.',
             'r2':r'\unsure{.} inside the guide figure',
             'r3':r'\unsure{.} before As-tu in the reading sequence'},
    decision='Retain the small mark with uncertain intent and preserve its position under the left bend, without turning it into certain baseline punctuation.')
p.add(point)

# Assemble the full page from the complete r1 reading, with all decisions above.
p.text=p.text.replace(r'\unsure{tronqués|tr. \deleted{qués}}',trunc)
p.text=p.text.replace('As-tu des candïdats à proposer ?',r'As-tu des \unsure{candïdats|candidats} à proposer ?')
p.text=p.text.replace(r'existent, \unsure{dès|dés}',r'existent\unsure{,} d\unsure{è|é}s')
p.text=p.text.replace(r1['changes'][20]['final'],guide1)
oldguide2=r1['changes'][24]['final']
p.text=p.text.replace("% Guide of et d'homologie: descending left segment meets the gap after bidualité.\n"+oldguide2+'\n','')
p.text=p.text.replace(r'\unsure{.} Tes réflexions',
    "% Guide beneath et d'homologie; the left leg attaches after bidualité.\n"+guide2+'\n'+r'\unsure{.} Tes réflexions')

# One doubt row for each unresolved locus, including state and point questions.
doubts=[]
for x in p.data['changes']:
    if r'\unsure' not in x['final'] or x['location'].startswith('Graphic joining'):
        continue
    if x['location'].startswith('Connecting graphic'):
        continue
    if x['location'].startswith('Final construction'):
        continue
    doubts.append({'location':x['location'],'reading':x['final'],
                   'alternatives':{
                       'Opening noun':['groupes'],
                       'Opening adjective':['formels'],
                       'Display, second object, final subscript':['reduced numeral 1'],
                       'After du type':['lowercase theta'],
                       'Interlinear addition, first word':['ou encore proposed by r3, but initial m-like form favours mesurant'],
                       'Interlinear addition, construction after hom':['unaccented live tronques','tr. with possibly cancelled qués'],
                       'Interlinear addition, adjective after top':['ponctués'],
                       'Question, candïdats':['ordinary single-dot candidats'],
                       'Left of Tes':['nontextual copy or pen mark'],
                       'Punctuation after existent':['no intentional punctuation'],
                       'Accent in the word after existent':['acute accent'],
                       'Accent in à présent':['hooked grave à'],
                       'Final adjective before questions':['naïves'],
                       'Small isolated mark under the left bend of the interlinear guide':['nontextual mark']
                   }.get(x['location'],[]),
                   'confidence':x['confidence'],'reason':x['evidence'],'crop':x['crop']})
p.data['doubts']=doubts

inv=p.data['inventory']
inv.insert(7,copy.deepcopy(r2['inventory'][6]))
for x in inv:
    if x['element']=='Opening continuation of the letter':
        x['first_words_or_objects']='groupe/groupes formel/formels ... La question que je voudrais soulever ...'
    if x['element']=='Possible cancelled suffix in the long addition':
        x['first_words_or_objects']='Live tronqués/tronques preferred; alternative tr. with deleted qués stays inside the outer unsure'
    if x['element']=='Guide for the homology addition':
        x['position']='Above the lower paragraph, under et d’homologie; left end attaches after bidualité'
# Keep source vertical order within and between the two prose blocks.
def first_y(x):
    b=x.get('source_bbox',[0,9999,0,9999])
    return min(z[1] for z in b) if isinstance(b[0],list) else b[1]
p.data['inventory']=sorted(inv,key=first_y)
p.data['slips']=[]
p.data['notes']="""Continuation of the letter, author page 6, archive folio 151. No new date, salutation, signature or title occurs. The opening continues the formal-group sentence and attributes a discovery to Dieudonné with the qualification “semble-t-il”; its singular/plural endings remain uncertain. No closing quotation is supplied where the manuscript does not show one.

The author asks about generalising to groups in (n-cat), expects noncommutative chain complexes, and asks what extra structures are needed: “on s’attend”, “sans doute du type”, “mais lesquelles ?”, and “As-tu des … à proposer ?” retain the question’s provisional character. The chain’s first four connectors are single hooked shafts; only the last has a complete arrowhead. The second object’s final subscript is comma-like, with a reduced 1 retained as an alternative. Expected index order prompted inspection but did not settle the glyph. The action letter keeps the local Theta/theta case doubt.

The main prose describes homotopy types truncated in dimension ≤ n of topological groups. The small addition gives dimension ≤ n+1 for connected espaces top ponctues/ponctués. All readers inspected the two bounds independently. The root’s narrowly targeted check, recorded separately as 134-2.151.check.degree_shift, uses based maps and their homotopies to identify homotopy groups of a loop space with those one degree higher in the underlying pointed space. It confirms that degree shift under the stated interpretation. It neither constructs the proposed algebraic structures nor proves their classification or the opening formal-group assertion. The exact argument and its limits are in mathchecks/134-2_scan151.md.

The interlinear opening favours mesurant, with residual doubt, over C’s ou encore. The crowded truncation word retains both live spellings and the possible abbreviated/deleted state; no definite cancellation is asserted. The addition’s curved left guide is continuous with its horizontal arm, so it is reproduced graphically rather than duplicated as a textual opening parenthesis. Its final ellipsis and closing parenthesis remain written. The tiny point beneath the guide is kept uncertain at its actual position. The homology addition also has a reproduced guide attached after bidualité; both guides are placed in source vertical order.

After the independent pen separator, the author relates biduality and the inserted homology topic to developments already existing and others requiring considerable elaboration, then introduces reminiscences prompted by the correspondent’s questions. Ouvrent is resolved from the o/u/v/r/e/n/t strokes. The final adjective is noïves/naïves; H’s noires does not account for the paired upper marks and the rounded v. The accents in the small added adjective, in dès, and above à/â remain ink doubts. The apparent extra dotting in candïdats and the low mark after existent also remain uncertain. These forms are not silently modernised.

The reader returns contain no mathematical verification events. Their inspections are visual collation. H’s leqslant and C’s leq represent the same inequality here; r1’s two encoding-only flags are excluded from the change and collation counts. H’s note about another reproduction is not evidence for any reading."""
p.data['checks']=[
    {'statement_id':'134-2.151.author.formal_groups','type':'carried as background without fault found',
     'outcome':'The continued formal-group assertion and qualified Dieudonné attribution were used only to describe the author’s subject; neither the theorem nor attribution was independently established.'},
    {'statement_id':'134-2.151.author.higher_structures','type':'carried as background without fault found',
     'outcome':'The request for structures on noncommutative chains and the proposed topological interpretation were carried as the author’s questions/claims. Only the separate degree-shift check was performed; no classification proof was attempted.'},
    {'statement_id':'134-2.151.document.continuation','type':'carried as background without fault found',
     'outcome':'The author page number 6, archive folio 151, two additions, two guides, separator and lower-paragraph subject were used as documentary context, not labelled mathematical proof checks.'}]

review=json.loads((OUT/'reviews/134-2_scan151_main_review.json').read_text())
p.save(main_viewed=[p.crop(x) for x in review['main_viewed']])
p.notation([
    '| 134-2 / 151 | Chain connectors | First four hooked shafts; final full right arrow | Each connector was inspected separately. The last head alone has two diagonals; earlier upturns are reproduced literally. |',
    '| 134-2 / 151 | Second chain index | <code>L_{n-\\unsure{,&#124;1}}</code> | A very short curved tick follows the minus; comma-like shape first, reduced numeral alternative. Later L₁ has a longer straight subscript. |',
    '| 134-2 / 151 | Action letter | <code>\\unsure{\\Theta&#124;\\theta}</code> | Broad barred oval with open upper-left join, retaining the same local case uncertainty. |',
    '| 134-2 / 151 | Dimension bounds | <code>\\leq n</code>; <code>\\leq n+1</code> | Both lower bars and indices inspected independently; H’s leqslant encoding is not counted as a different inequality. |',
    '| 134-2 / 151 | Abbreviations and accent | comm, hom, top; chaines | No terminal points in these three abbreviations; chaines has a single i point and no circumflex. |',
    '| 134-2 / 151 | Added-line guides | Two continuous guides in TikZ | First curved left descent and long arm lie before As-tu; second oblique leg attaches after bidualité. A tiny point inside the first guide has uncertain intent. |'])
p.observation("""All three complete readings were compared, including all TeX content differences. The main reader inspected 13 existing reader crops and made five new tight crops for half-settled witness disagreements; all 18 were viewed once, with no failed image delivery. Existing crops covered the first two chain hooks, the closing quotation and multiple adjacent accent questions, so no duplicate crops were needed.

The readers agreed on the hook geometry and the clear word ouvrent, but differed in uncertainty, small accents, possible cancellation, the interlinear opening and the placement of guides/isolated marks. The main decision kept those distinctions explicit. The two leq/leqslant flags from r1 were encoding-only and excluded. The guide shapes were correctly reproduced by all three under v06; r1/r3 placed the second guide after the paragraph in reading order, whereas the source places it above. This motivates a brief reminder about graphic order and maintaining a point’s position inside a graphic. No proof checking is attributed to the readers. The root’s actual degree-shift check is separately recorded.""")
review['status']='adjudication saved; awaiting page commitment'
(OUT/'reviews/134-2_scan151_main_review.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n')
print('C/H',sum(x['against_c'] for x in p.data['changes']),sum(x['against_h'] for x in p.data['changes']),'doubts',len(doubts),'inventory',len(p.data['inventory']))
