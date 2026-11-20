from pathlib import Path
from datetime import datetime, timezone
import json, re, hashlib
base=Path('/workspace/scratch/42e661864e98/out/readers/scan012/R2')
source='/workspace/scratch/42e661864e98/source/SP53_CW_156-6_scans/J156-6-02_156-6_scan012.jpg'
crops=json.loads((base/'crop_log.json').read_text())
view_times=['11:22:23','11:23:02','11:24:01','11:24:10','11:24:21','11:24:26','11:24:48','11:25:00','11:25:19','11:25:26','11:25:29','11:26:01']
views=[{'image':source,'role':'whole','viewed_utc':'2026-11-20 11:20:03 UTC'},
{'image':source[:-4]+'_a.jpg','role':'half_a','viewed_utc':'2026-11-20 11:20:09 UTC'},
{'image':source[:-4]+'_b.jpg','role':'half_b','viewed_utc':'2026-11-20 11:20:33 UTC'}]
for c,t in zip(crops,view_times):
 c['viewed_utc']='2026-11-20 '+t+' UTC'
 c['relative_to_out']='readers/scan012/R2/'+Path(c['output']).name
 views.append({'image':c['output'],'role':'crop','viewed_utc':c['viewed_utc']})

def location(n=None,box=None):
 if n is None:
  return {'crop':None,'crop_box':box,'crop_source':source}
 c=crops[n-1]
 return {'crop':c['relative_to_out'],'crop_box':c['box'],'crop_source':source}

diffs=[]
def diff(place,c,h,reading,against_C,against_H,kind,marked_in_H,confidence,evidence,n=None,box=None,mathematical=False):
 row={'id':f'D012-R2-{len(diffs)+1:02d}','place':place,'c':c,'h':h,'reading':reading,'against_C':against_C,'against_H':against_H,'kind':kind,'marked_in_H':marked_in_H,'confidence':confidence,'evidence':evidence,'mathematical':mathematical}
 row.update(location(n,box)); diffs.append(row)

# Diagram geometry and signs; the other five objects and all arrows agree.
diff('(1.18), frame surrounding the middle and lower-left objects',
 r'closed quadrilateral via -- cycle',
 r'explicit note: un cadre oblique ... entoure G\leq F et G\ll F',
 'Oblique frame with distinct small gaps at the upper-left and lower-left corners and a short upper-right overhang.',
 True,False,'drawing or diagram','no','high',
 'Crop 01 shows white breaks between the left side and both its neighboring sides. The right/bottom junction is joined. H explicitly recognizes the oblique enclosure and is credited for it; its note does not assert closed corners.',1,mathematical=False)
diff('(1.18), lower-right relation sign',
 'two opposed three-segment zigzags, without an upright',r'\between',
 'two opposed zigzags with a heavy extra upright stroke, reproduced directly in inline TikZ',
 True,True,'misread symbol or index','no','medium',
 'The enlarged sign has four diagonal tips and a distinct central-left upright extending from the upper tips to the lower knot. The ink is heavily retraced. No readable earlier sign or secure cancellation history is inferred.',1,mathematical=True)
diff('first paragraph, relation after parallel',
 'two opposed zigzags',r'\between',
 'two opposed zigzags with four free diagonal tips, no horizontal caps or upright',
 False,True,'misread symbol or index','no','high',
 'Half a resolves the thin clean sign: two crossing angular paths with free diagonal tips. The manuscript geometry is retained instead of the standard between glyph.',box=[1130,901,1202,970],mathematical=True)

# Slanting marginal note.
diff('left margin, after non réflexive',
 'non réflexive, car', 'non réflexive, followed directly by the formula',
 'non réflexive, car', False,True,'omission','no','medium',
 'The rotated marginal reading retains the short causal word at the end of the prose line; it precedes the self-incidence equivalence.',2)
diff('left margin, membership sign in the first equivalence',
 r'\unsure{\in|\overset{\prime}{\in}}',r'\in',r'\in',
 True,False,'misread symbol or index','no','high',
 'The raised curved stroke is aligned with the comma ending réflexive on the preceding marginal line. The membership itself has the ordinary open curved form and middle bar; no separate prime is attached to it.',2,mathematical=True)
diff('left margin, final M in the first equivalence (first occurrence)',
 'M',r'\mathcal{M}',r'\unsure{\mathcal{M}|M}',
 True,True,'misread symbol or index','no','medium',
 'Two high peaks and a rounded left return identify M. The ornamental versus ordinary handwritten alphabet cannot be fixed from the ink; the existing mathcal/ordinary candidates are retained at the first occurrence.',2,mathematical=True)
diff('left margin, punctuation after the first equivalence',
 'no period after M', 'period after M', 'no period after M',
 False,True,'text not on the page','no','medium',
 'No terminal point is visible after the final M before the following Pour line. The nearby higher stroke belongs to the previous prose line.',2)
diff('left margin, beginning of the proposed repair',
 'Pour avoir une',r'Pour \ill{} une','Pour avoir une',
 False,True,r'readable ink left as \ill{}','yes','medium',
 'After Pour, the reduced rounded entry, v turn, dotted i and final r support avoir. The following une is separately visible.',2)
diff('left margin, noun in the proposed repair',
 "une relation d'ordre", "une rel. d'ordre", "une relation d'ordre",
 False,True,'misread word','no','medium',
 'The second noun runs through the full reduced relation form; unlike the earlier rel. it is not stopped by a baseline abbreviation point.',2)
diff('left margin, final prose before the proposed definition',
 'il faudrait écrire',r'\ill{} avoir écrit','il faudrait écrire',
 False,True,r'readable ink left as \ill{}','yes','medium',
 'The rotated line shows the initial il, a long f with the reduced faudrait sequence, then écrire. H’s locally aligned phrase is different, not simply one omitted word.',2)
diff('left margin, canceled symbols before the proposed definition',
 r'\deleted{\unsure{F\triangleleft|F}}','omitted',r'\deleted{$F\triangleleft$}',
 True,True,'deletion state','no','high',
 'Under the dark diagonal cancellation the F stem and arms remain, followed by a separate left-pointing closed wedge. The wedge is not merely a crossing of the F.',2,mathematical=True)
diff('left margin, ou in the proposed definition',
 r'\uuline{ou}','ou',r'\uuline{ou}',
 False,True,'omission','no','high',
 'Two distinct short underline strokes lie below ou. They are separate from the underline belonging to the preceding triangle.',2)
diff('left margin, final punctuation',
 'F=F.', 'F=F', 'F=F.',
 False,True,'omission','no','medium',
 'A small terminal mark immediately follows the last F, separated from the nearby body line. It is retained as a point.',2)
diff('left margin, supposed extra standalone underlined-triangle formula',
 'one occurrence as the left side of the proposed definition',
 'note additionally says the last F trianglelefteq F is also carried alone at the bottom',
 'one occurrence as the left side of the proposed definition',
 False,True,'text not on the page','no','high',
 'The low F trianglelefteq F continues into the déf equivalence to its upper right. There is no second copy of the formula in the crop. H’s recognition of the underbar itself is correct.',2,mathematical=True)

# Second body paragraph and (1.19).
diff('start of the paragraph La relation',
 'La relation',r'\struck{Les} La relation','La relation',
 False,True,'text not on the page','no','medium',
 'The start of the body line is La relation. The nearby canceled ink belongs to the slanted marginal formula; no independently struck Les can be identified before La.',2)
diff('La relation, compatibility sign',
 'two opposed zigzags',r'\between','two opposed zigzags',
 False,True,'misread symbol or index','no','high',
 'Half a shows the same thin two-zigzag sign as the previous line, without the extra upright present in the diagram.',box=[656,987,727,1060],mathematical=True)
diff('above est réflexive, inserted phrase',
 r'\inserted{de plus}',r'\add{de plus,}',r'\inserted{de plus,}',
 True,False,'insertion or placement','no','high',
 'The added words have a separate short comma-shaped stroke after plus. A curved insertion leader reaches the space between est and réflexive.',3)
diff('before (1.19), first collection F',
 r'\unsure{\mathcal{F}|\mathscr{F}}',r'\mathfrak{F}',r'\unsure{\mathcal{F}|\mathfrak{F}}',
 True,True,'misread symbol or index','no','medium',
 'The long upper arm, central crossing and curled foot identify the collection F rather than the plain operands. Exact font is not determined. Existing mathcal/frak alternatives from the notation table are used, not a confidently normalized font.',2,mathematical=True)
diff('before (1.19), word after son seul',
 r'\unsure{élémt|élément}','élément',r'\unsure{élémt|élément}',
 False,True,'abbreviation expanded or spelling modernised','no','low',
 'The two acute marks and tall l are visible, followed by one long reduced middle and an upright terminal. That middle does not distinguish the shorter élémt from a rapidly written élément; both remain.',4)
diff('before (1.19), subscript of the inline empty figure',
 r'\varnothing_{\mathcal{F}}',r'\emptyset_{\mathfrak{F}}',r'\varnothing_{\mathcal{F}}',
 False,True,'misread symbol or index','no','medium',
 'The subscript repeats the collection F’s upper arm and foot. The first-occurrence alphabet doubt governs this subsequent occurrence; emptyset versus varnothing macro syntax is not counted separately.',4,mathematical=True)
diff('(1.19), subscript of the empty figure',
 r'\varnothing_{\mathcal{F}}',r'\emptyset_{\mathfrak{F}}',r'\varnothing_{\mathcal{F}}',
 False,True,'misread symbol or index','no','medium',
 'Half b resolves an open slashed oval with the small collection F below it. The outer two F operands are plain. Only the unresolved family-alphabet choice differs from H.',box=[1082,1224,1191,1316],mathematical=True)

# Remarques, (1.20), and the following line.
diff('Remarques a), initial word', 'Les','les','Les',
 False,True,'misread word','no','high',
 'A tall straight L descends to a substantial baseline foot before the reduced es; it is not the looped lower-case l form.',5)
diff('Remarques, M in M subset F',
 'M',r'\mathcal{M}',r'\mathcal{M}',
 True,False,'misread symbol or index','no','medium',
 'The two high peaks and broad return repeat the M identified in the margin. The page-level mathcal/ordinary doubt is marked at that first occurrence.',box=[1486,1450,1557,1528],mathematical=True)
diff('Remarques, family in M subset F',
 r'\mathcal{F}',r'\mathfrak{F}',r'\mathcal{F}',
 False,True,'misread symbol or index','no','medium',
 'Half b shows the collection F after an open subset sign. Its alphabet follows the explicitly uncertain first occurrence.',box=[1545,1444,1650,1533],mathematical=True)
diff('(1.20), initial M',
 'M',r'\mathcal{M}',r'\mathcal{M}',
 True,False,'misread symbol or index','no','medium',
 'The large M has a sweeping entry and two high peaks; it repeats the first-occurrence alphabet uncertainty rather than introducing another object.',6,mathematical=True)
diff('(1.20), F after membership',
 r'\mathcal{F}',r'\mathfrak{F}',r'\mathcal{F}',
 False,True,'misread symbol or index','no','medium',
 'The collection F has a long arched top and returning foot, distinct from the later ordinary indexed F_i. The page-level alphabet doubt remains applicable.',6,mathematical=True)
diff('(1.20), abbreviation before irréductible',
 r'\mathrm{str}^{\mathrm{t}}.', 'strict.',r'\mathrm{str}^{\mathrm{t}}.',
 False,True,'abbreviation expanded or spelling modernised','no','high',
 'The baseline letters are str, followed by a separately raised small t and a point. There are no baseline ic strokes.',6)
diff('(1.20), supremum operator',
 r'\mathop{\mathrm{Sup}}\limits_i',r'\sup_i',r'\mathop{\mathrm{Sup}}\limits_i',
 False,True,'misread symbol or index','no','high',
 'The initial S is a large capital; u and the long p follow. A dotted i is below the operator, and the two F indices are also i. Lower-case sup changes the drawn capitalization.',6,mathematical=True)
diff('before D’autre part, canceled opening group',
 r'\deleted{\unsure{Et|En}}',r'\struck{D\text{’}autre}',r'\deleted{\unsure{Et|En}}',
 False,True,'deletion state','no','low',
 'Only a short crossed group sits above the live D. The first curved capital can be E; a short terminal upright favors t, but the crossing and upper reduced stroke leave n possible. A complete second D’autre is not visible.',7)
diff('D’autre part, M after on définit',
 'M',r'\mathcal{M}',r'\mathcal{M}',
 True,False,'misread symbol or index','no','medium',
 'Half b shows the same two-peaked M, with the recurring alphabet uncertainty already marked in the margin.',box=[1460,1759,1553,1842],mathematical=True)

# The last three displays and concluding revision.
diff('(1.21), initial M',
 'M',r'\mathcal{M}',r'\mathcal{M}',
 True,False,'misread symbol or index','no','medium',
 'Half b resolves the repeated M with a broad entry and two high peaks. Its identity is certain and its typographic alphabet remains a page-level doubt.',box=[564,1855,682,1944],mathematical=True)
diff('(1.21), family F after membership',
 r'\mathcal{F}',r'\mathfrak{F}',r'\mathcal{F}',
 False,True,'misread symbol or index','no','medium',
 'The long curved upper arm and lower return repeat the collection F. The first-occurrence uncertainty, not a new confident font assignment, applies.',box=[737,1853,893,1944],mathematical=True)
diff('puis, pour F in F, collection letter',
 r'\mathcal{F}',r'\mathfrak{F}',r'\mathcal{F}',
 False,True,'misread symbol or index','no','medium',
 'Half b distinguishes the plain operand F from the returned collection F after membership. The latter follows the page-level alphabet choice.',box=[554,1913,714,1993],mathematical=True)
diff('word immediately before (1.22)',
 r'\unsure{déployement|déploiement}','déploiement','deployement',
 True,True,'abbreviation expanded or spelling modernised','no','medium',
 'Crop 08 shows a long medial descender belonging to y, not a dotted i. The initial d has its connected upper loop; there is no separate acute above the following reduced e in the available vertical context. The spelling and absence of that accent are retained.',8)
diff('(1.22), M in X in M',
 'M',r'\mathcal{M}',r'\mathcal{M}',
 True,False,'misread symbol or index','no','medium',
 'Half b shows the repeated two-peaked M. This occurrence carries forward the first marked alphabet uncertainty.',box=[818,1972,914,2056],mathematical=True)
diff('(1.22), final F after incidence',
 r'\unsure{\mathcal{F}|F}',r'body: F; note: page writes \mathfrak{F}, for F',r'\mathcal{F}',
 True,True,'misread symbol or index','no','high',
 'The terminal letter has a large arched upper arm, central crossing and fully closed returning foot. It is the collection letter, unlike the plain F carrying the tilde at the start. H’s note correctly observes this literal form and is credited; H’s body substitutes the mathematical correction.',9,mathematical=True)
diff('final display label',
 r'\unsure{(1,23)|(1.23)}','(1.23)','(1,23)',
 True,True,'other','no','high',
 'The separator has an extended bent descending tail below the digit bases. It is a comma, unlike the dots in the preceding labels.',10)
diff('bottom deletion, final word',
 r'\unsure{équivalent}','équivalent',r'\unsure{équivalent}',
 False,True,'other','no','medium',
 'The broad reading équivalent fits surviving loops, q descender, dot and tall final strokes, but the horizontal cancellation crosses its middle and the inserted line interferes above. The original doubt is not removed.',11)
diff('bottom insertion, adjective after les données',
 r'\unsure{minima|minimes}',r'\uncertain{minimales}',r'\unsure{minima|minimes}',
 False,True,'misread word','yes','low',
 'The middle and final letters reduce to shallow waves, consistent with minima or minimes. There is no distinct tall l supporting the longer minimales. The ink does not settle the shorter alternatives.',11)
diff('last words at the page edge',
 "d'y","de s'y","d'y",
 False,True,'misread word','no','high',
 'The final group shows the looped d and its long exit, a separate apostrophe, then y. There is no separately written s between d and the apostrophe.',12)

cd=[]
def doubt(place,c,reading,disposition,evidence,n):
 row={'place':place,'c':c,'reading':reading,'disposition':disposition,'evidence':evidence}
 row.update(location(n));cd.append(row)
doubt('left margin, first equivalence membership',r'\unsure{\in|\overset{\prime}{\in}}',r'\in','resolved','The upper stroke aligns with the preceding prose comma, not a prime on membership.',2)
doubt('left margin, canceled F and wedge',r'\unsure{F\triangleleft|F}',r'\deleted{$F\triangleleft$}','resolved','Both the stem-and-arms of F and the following closed wedge survive the cancellation.',2)
doubt('first collection F in body',r'\unsure{\mathcal{F}|\mathscr{F}}',r'\unsure{\mathcal{F}|\mathfrak{F}}','retained','Letter identity is clear; exact font remains underdetermined. The established mathcal/frak candidates are used.',2)
doubt('body before (1.19), word after son seul',r'\unsure{élémt|élément}',r'\unsure{élémt|élément}','retained','Two accents and l are visible, but the long middle does not separate the abbreviation from a fully reduced spelling.',4)
doubt('canceled group before D’autre part',r'\unsure{Et|En}',r'\deleted{\unsure{Et|En}}','retained','Cancellation merges the terminal upright and its crossbar; Et is first, En remains possible.',7)
doubt('word before (1.22)',r'\unsure{déployement|déploiement}','deployement','resolved','Long medial y descender; no separate acute over the following e of the initial de group.',8)
doubt('(1.22), final collection letter',r'\unsure{\mathcal{F}|F}',r'\mathcal{F}','resolved','A closed returning foot and broad curved upper arm identify the collection letter. The separate first-occurrence font doubt still applies.',9)
doubt('final display label',r'\unsure{(1,23)|(1.23)}','(1,23)','resolved','The separator has a bent descending tail below the digit bases.',10)
doubt('bottom canceled word',r'\unsure{équivalent}',r'\unsure{équivalent}','retained','The cancellation and nearby insertion obscure enough of the word to prevent confident uncertainty removal.',11)
doubt('bottom inserted adjective',r'\unsure{minima|minimes}',r'\unsure{minima|minimes}','retained','Low reduced waves support both endings; no confident distinction is possible at the one enhanced crop.',11)

inventory=[]
def inv(element,kind,position,first):
 inventory.append({'element':element,'kind':kind,'position':position,'first_words_or_objects':first,'sheet_kind':'text','hand':'his hand','transcribed':'yes'})
inv('author page number','text','top center','11')
inv('(1.18), implication diagram including frame and label','diagram','upper quarter',r'G\triangleleft F; G\preccurlyeq F; G\leq F; G\parallel F; G\ll F; G compatibility F; five downward implications; open-corner oblique frame')
inv('classification paragraph','text','below diagram','Parmi les six relations, il y a quatre relations d’ordre')
inv('slanted critical note','margin note','left margin beside the first two body paragraphs','Non, triangleleft n’est pas rel. d’ordre')
inv('self-incidence equivalence in margin','display','middle of slanted note',r'F\triangleleft F\Longleftrightarrow F\in M')
inv('canceled opening of marginal definition','deletion','right part of the slanted note',r'F\triangleleft')
inv('proposed reflexive relation in margin','display','bottom of slanted note',r'F\trianglelefteq F déf iff F\triangleleft F; doubly underlined ou; F=F.')
inv('symmetry and reflexivity paragraph','text','middle upper body','La relation [zigzags] est ... réflexive, mais parallel ne l’est que si')
inv('extra reflexivity qualification','insertion','above est réflexive','de plus,')
inv('(1.19)','display','below reflexivity paragraph',r'F\parallel F\Longleftrightarrow F=\varnothing_{\mathcal{F}} figure vide.')
inv('Remarques a) introductory paragraph','text','start of lower half','Remarques a) Les relations triangleleft et leq se déterminent mutuellement')
inv('(1.20)','display','middle lower body',r'M={X in F | X str^t. irréductible, i.e. X leq Sup_i F_i implies exists i avec X leq F_i}; pour leq below the property')
inv('reference to incidence definition','text','below (1.20)','puis triangleleft par (1.17).')
inv('canceled opening above D','deletion','start of following line','Et|En')
inv('reverse construction paragraph','text','between (1.20) and (1.21)','D’autre part, connaissant triangleleft on définit M par')
inv('(1.21)','display','lower body',r'M={X in F | X triangleleft X}')
inv('deployment introduction','text','between (1.21) and (1.22)','puis, pour F in F, son deployement')
inv('(1.22)','display','lower body',r'tilde F={X in M | X triangleleft collection F}')
inv('last connective','text','above last display','et enfin')
inv('(1,23)','display','above bottom revision',r'F leq G iff tilde F subset tilde G')
inv('concluding sentence continued off page','text','bottom two body lines','Donc, pour déterminer ... fixent la structure d’atelier, il est indifférent d’y')
inv('replaced bottom phrase','deletion','bottom, after déterminer','la structure, il est équivalent')
inv('replacement above bottom phrase','insertion','above bottom deletion','les données minima|minimes qui')

notes=[{
 'content':'The page gives a six-relation implication diagram, states which relations are orders or symmetric, and qualifies reflexivity. A slanting note rejects the claim that incidence is an order. Remark a) explains how the order and incidence determine one another through the distinguished collection and deployment. The last sentence revises its wording toward the data fixing an atelier structure and continues beyond the sheet.',
 'math_reading_decisions':[
  'All five diagram arrows point down, with the two central implications reaching the lower-left and lower-right objects. The enclosure surrounds the middle and lower-left objects, with visible left-corner gaps.',
  'The proposed reflexive repair literally repeats F on both sides and ends F=F. No G is supplied, although H’s note suggests one.',
  'The last object in (1.22) is literally the collection F with a turned foot. It is not silently replaced by the ordinary F that the deployment formula might be expected to use.',
  '(1.20) has capital Sup and dotted i in all three indexed positions; the terminal relation is a reinforced leq, not membership. The inclusion in the final equivalence is open subset, with no lower bar.',
  'No proof, independent re-proof, or formal mathematical computation was performed. Visual comparison is recorded separately from the background statement events.'
 ],
 'author_doubts':[
  r'Non, $\triangleleft$ n’est pas rel. d’ordre, elle est transitive mais non réflexive, car $F\triangleleft F\Longleftrightarrow F\in M$',
  'Pour avoir une relation d’ordre il faudrait écrire'
 ],
 'titles_dates_counts':'Author page number 11. Underlined heading Remarques, subdivision a). Labels (1.18), (1.19), (1.20), (1.21), (1.22), and literal (1,23). The body says six relations and four order relations; the marginal note challenges the latter classification. No date, archive pencil number, separate title sheet, or manuscript page-count statement is visible.'
}]

checks=[]
for sid in ['S012-118','S012-orders-and-margin','S012-119','S012-120','S012-121','S012-122','S012-123']:
 checks.append({'statement_id':sid,'type':'carried as background without fault found','outcome':"read as the author's assertion; no mathematical verification performed"})

notation=[
 {'sign':'collection M','latex':r'\unsure{\mathcal{M}|M} at first occurrence, then \mathcal{M}','ink':'Two tall peaks, rounded trough and broad entering/returning stroke, first in the marginal equivalence.','alternatives':['M']},
 {'sign':'collection F','latex':r'\unsure{\mathcal{F}|\mathfrak{F}} at first occurrence, then \mathcal{F}','ink':'Long curved upper arm, central crossing and turned or closed lower foot. The foot is especially clear at the end of (1.22).','alternatives':[r'\mathfrak{F}']},
 {'sign':'compatibility-like sign','latex':'inline TikZ: two opposed zigzags','ink':'Clean body occurrences have four free diagonal tips and a central open diamond; the diagram occurrence is heavily retraced and includes an additional upright stroke.','alternatives':['No secure earlier canceled character identified in the diagram.']},
 {'sign':'empty figure','latex':r'\varnothing_{\mathcal{F}}','ink':'A small slashed open oval, with the collection letter placed below; plain F operands flank the equivalence.','alternatives':[]},
 {'sign':'supremum','latex':r'\mathop{\mathrm{Sup}}\limits_i','ink':'Capital initial S, reduced u, descending p; dotted i beneath.','alternatives':[]},
 {'sign':'strict abbreviation','latex':r'\mathrm{str}^{\mathrm{t}}.','ink':'Baseline str, separately raised t, then a point.','alternatives':[]},
 {'sign':'incidence and proposed reflexive version','latex':r'\triangleleft; \trianglelefteq','ink':'Closed left-pointing triangle; proposed version has a separate lower stroke. The note’s ou has two underlines.','alternatives':[]}
]

unresolved=[
 {'place':'first M in margin, then recurring','reading':r'\mathcal{M}','alternatives':['M'],'confidence':'medium','evidence':'The M identity is clear, but handwriting alone does not determine the calligraphic versus ordinary typeset alphabet.'},
 {'place':'first collection F, then recurring','reading':r'\mathcal{F}','alternatives':[r'\mathfrak{F}'],'confidence':'medium','evidence':'Distinct collection shape with returned upper and lower strokes; exact alphabet remains underdetermined.'},
 {'place':'before (1.19), sole element word','reading':'élémt','alternatives':['élément'],'confidence':'low','evidence':'Middle letters collapse into a single long stroke after the two visible acute marks and tall l.'},
 {'place':'canceled group before D’autre part','reading':'Et','alternatives':['En'],'confidence':'low','evidence':'Heavy cancellation crosses the small terminal group.'},
 {'place':'bottom deleted phrase, final word','reading':'équivalent','alternatives':[],'confidence':'medium','evidence':'Likely full word, but cancellation and the insertion obscure enough strokes to retain C’s doubt.'},
 {'place':'bottom inserted adjective','reading':'minima','alternatives':['minimes'],'confidence':'low','evidence':'Reduced shallow middle and terminal waves do not decide the ending.'}
]

report={
 'scan':12,'reader':'R2','started_utc':'2026-11-20 11:20:03 UTC','finished_utc':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
 'view_log':views,'differences':diffs,'c_doubts':cd,'s_rows':[],
 'inventory':inventory,'notes':notes,'check_events':checks,'notation_proposals':notation,
 'abbreviations':[{'form':'rel.','expansion':'relation'},{'form':'élémt (uncertain)','expansion':'élément'},{'form':r'str^t.','expansion':'strictement'},{'form':'i.e.','expansion':'id est'},{'form':'déf','expansion':'définition'}],
 'unresolved':unresolved,'brief_feedback':[], 'crop_log':crops,
 'counts':{'whole_views':1,'half_views':2,'crop_views':12,'actual_crops_created':12,'differences':len(diffs),'c_doubt_loci':len(cd),'s_rows':0,'inventory_elements':len(inventory),'check_events':len(checks),'unresolved_loci':len(unresolved)},
 'status':'complete'
}
(base/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
(base/'crop_log.json').write_text(json.dumps(crops,ensure_ascii=False,indent=2)+'\n')

lines=['# Scan 012 — independent reader R2 audit','',
 'Scope: only the assigned scan 012 packet, its authorized current-page conventions, the supplied current-page whole/halves, and R2’s own crops. No other page, reader result, consolidated decision, OCR, external research, PDF extraction, or LaTeX compilation was used.',
 '', 'The first logged UTC time is the whole-image session start; packet reads preceded that clock event. Whole and half images were emitted exactly once each. The page has been transcribed completely, including its ending continuation.',
 '', '## Actual image-view sequence','']
for i,v in enumerate(views,1):
 lines.append(f'{i}. {v["viewed_utc"]} — {v["role"]}: `{Path(v["image"]).name}` (emitted through tools.view_image).')
lines += ['', '## Open loci after the two half views','',
 'The following twelve locus groups remained open. The margin was treated as one connected slanting locus because its prose, two formulas, cancellation and nearby body-line start interlock. The bottom replacement was likewise one physical correction locus. Each received one crop only; no crop was remade or re-viewed.']
for c in crops:
 lines.append(f'- {c["name"]}: {c["reason"]}')
lines += ['', '## Crop transforms and decisions','',
 'All original-source coordinates below refer to the full 1681 × 2361 scan. All crops received autocontrast, UnsharpMask(radius=1.2, percent=120, threshold=3), LANCZOS resizing and JPEG quality 95. Only crop 02 was rotated, using bicubic resampling and white fill before enlargement.']
results=[
 'Both left corners of the frame have gaps. The lower-right sign includes a heavy extra upright; no specific deleted predecessor was invented.',
 'Read the slanting note in its own direction; retained car, avoir, full relation, il faudrait écrire, the canceled F plus wedge, double-underlined ou and terminal point. Resolved the apparent membership prime as neighboring-line punctuation. The alleged extra standalone formula and struck Les were not found. Alphabet choices remain explicitly uncertain.',
 'The insertion ends with a separate comma and enters between est and réflexive.',
 'Retained élémt|élément because the middle collapses to a line; confirmed the slashed empty sign and its collection subscript.',
 'Resolved the tall straight initial with its foot as capital L in Les.',
 'Read str with raised t and a point, capital Sup, all dotted i indices, and the reinforced terminal leq. No old character can be isolated under that reinforcement.',
 'Retained Et|En under cancellation; rejected a full canceled D’autre.',
 'Read a long descending y; no separate acute appears above the reduced e of initial de. Transcribed deployement.',
 'Resolved the last object as the collection F by its closed foot and curved top; H’s observational note is credited while its body correction is rejected.',
 'Resolved the separator as a comma: (1,23).',
 'Kept the bottom équivalent and minima|minimes doubts. The longer minimales is unsupported by a tall l. The deletion and its replacement were both transcribed.',
 'Resolved d’y; no separate s is present.'
]
for c,res in zip(crops,results):
 lines.append(f'- `{Path(c["output"]).name}`: source `{Path(c["source"]).name}`; box {c["box"]}; rotation {c["rotation"]}°; output {c["output_size"][0]} × {c["output_size"][1]} pixels. {res}')
lines += ['', '## Line-by-line comparison record','',
 '- Header and diagram: read author number 11; compared every G/F object, six relations and five double arrows against both witnesses. All arrow directions agree. Recorded the frame gaps and the additional upright in the dark lower-right sign. The body’s two clean compatibility signs were compared separately and are not normalized to H’s between glyph.',
 '- First three body lines: compared Parmi les six relations, il y a quatre relations d’ordre, the four listed signs, and et les deux autres relations ... sont symétriques, including commas and final point. The marginal criticism was read at crop 02 rather than silently harmonized with this assertion.',
 '- Slanted margin, top to bottom: compared Non ... n’est pas rel. d’ordre; elle est transitive mais non réflexive, car; the self-incidence equivalence; Pour avoir une relation d’ordre il faudrait écrire; the canceled F/wedge; the underlined-triangle definition, déf, doubly underlined ou, F=F and its terminal point. Kept the literal repeated F operands. No second standalone left-hand formula is supplied.',
 '- Next body paragraph: compared La relation, compatibility sign, est, inserted de plus with its comma, réflexive, mais parallel ne l’est que si, first family F, est réduit à son seul, the uncertain element word, empty-family sign, comma, and car. No struck Les was identifiable. Family F’s alphabet is marked once.',
 '- (1.19): compared the two plain F operands, parallel, two-headed implication, equality, slashed oval and subscript, figure vide and point. Only the family alphabet differs substantively from H; emptyset/varnothing macro choice is not independently counted.',
 '- Remarques a): compared underline, capital Les, relations, triangle, et leq, se déterminent mutuellement, point, Connaissant leq, on définit M subset F comme. The open inclusion is retained. M and family F follow their explicitly uncertain first occurrences.',
 '- (1.20): compared both braces, every X, membership, family F, vertical separator, abbreviated str with raised t and point, irréductible and comma, the lower pour leq gloss, i.e., leq, capital Sup with lower i, both ordinary F_i, rightward implication, exists i, avec and final leq. The last leq is retraced; no deleted predecessor is added. H’s inline gloss layout is not counted as a textual discrepancy by itself.',
 '- Following line: compared puis triangleleft par (1.17). The short canceled group was inspected separately from the live D’autre part, connaissant triangleleft on définit M par.',
 '- (1.21): compared M, equality, braces, X membership family F, separator and X triangleleft X. Introductory line of (1.22): puis, pour ordinary F in family F, son deployement; the y descender and absent separate acute were checked at crop 08.',
 '- (1.22): compared tilde F, equality, braces, X membership M, separator, X triangleleft and final collection F. Kept this literal terminal family symbol despite the tempting mathematical replacement.',
 '- Final transition and display: read et enfin; compared F leq G, equivalence, both tildes and the open subset sign. Checked the label’s comma at crop 10.',
 '- Bottom revision: compared Donc, pour déterminer, the complete canceled la structure, il est équivalent phrase, its above-line replacement les données minima|minimes qui, then fixent la structure d’atelier, il est indifférent d’y. Kept the page continuation open. No footer, date or archive pencil number was found.',
 '', '## Doubts, mathematical check limits, and counts','',
 f'- C has {len(cd)} distinct unsure loci on this page. All are individually accounted for in report.json; duplicate context-table references were not counted again.',
 f'- Actual images: 1 whole, 2 halves, {len(crops)} newly made crops, {len(crops)} crop views; {len(views)} view events total.',
 f'- The report has {len(diffs)} difference loci, {len(inventory)} inventory elements and {len(unresolved)} remaining doubt loci. S.json is an empty array, so there are no S adjudications to confirm or overturn.',
 '- Mathematical statements were followed and summarized, but not proved. The seven check events explicitly say that the author’s assertions were read as background without mathematical verification. Pure visual decisions are in the collation and above, not inflated into proof checks.',
 '- The remaining limits are reduced cursive endings, a short heavily canceled group, and the typographic alphabet of recurring collection letters. The marginal crop was rotated approximately upright once; no additional rotation/crop search was performed.',
 '- Structural checks are recorded below after output generation. No compilation or format-building attempt occurred.'
]
(base/'audit.md').write_text('\n'.join(lines)+'\n')
print(json.dumps(report['counts'],ensure_ascii=False))
