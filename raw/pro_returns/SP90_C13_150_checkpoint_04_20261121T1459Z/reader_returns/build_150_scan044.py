from pathlib import Path
import json, re

BASE = Path('/workspace/scratch/481648fc487b/SP90_C13_150_work')
PACKET = Path('/workspace/scratch/481648fc487b/reader_packets/150_scan044')
OUT = BASE / 'reader_returns'
C = (PACKET / 'C.tex').read_text()
H = (PACKET / 'H.tex').read_text()
T = (OUT / '150_scan044.tex').read_text()
CROPS = {}
for p in sorted((BASE / 'crops').glob('150_scan044_*.json')):
    v = json.loads(p.read_text())
    CROPS[p.stem.removeprefix('150_scan044_')] = v

def cs(name):
    return CROPS[name]['file']

def box(name):
    return CROPS[name]['box']

def fragment(start, end):
    a = T.index(start)
    return T[a:T.index(end, a)+len(end)]

bar_a = r'\draw[line width=.45pt] (0,0) .. controls (-.025,-.35) and (.025,-.65) .. (0,-.95) .. controls (-.03,-1.35) and (.025,-1.8) .. (-.015,-2.3);'
bar_b = r'\draw[line width=.45pt] (0,0) .. controls (-.015,-.5) and (.02,-1.1) .. (0,-2);'
leader_ij = r'\draw[line width=.4pt] (.6,.25) .. controls (.3,.15) and (.1,.1) .. (0,0);'
leader_cyl = r'\draw[line width=.4pt] (0,0) .. controls (-.05,.2) and (.1,.34) .. (.4,.34) -- (1.6,.34) .. controls (1.82,.34) and (1.9,.43) .. (1.85,.57);'
changes = []
def ch(place, c, h, final, evidence, crop, kind, error_kind,
       change_C=False, change_H=True, confidence='high', marked=False, consequential=''):
    changes.append(dict(place=place,C=c,H=h,final=final,evidence=evidence,
        crop=cs(crop),box=box(crop),confidence=confidence,kind=kind,error_kind=error_kind,
        marked_in_H=marked,change_C=change_C,change_H=change_H,consequential=consequential))

ch('opening / croiss.', 'croiss.', 'croissante', 'croiss.',
   'The low croiss run ends in a separate dark point. No ante ending follows. This is the written abbreviation, not an expansion.',
   'croiss', 'abbreviation expanded or spelling modernised', 'abbreviation/spelling')
ch('first display / item number', r'(2^\circ)', '[absent]', r'(2^\circ)',
   'A curved 2, raised hollow ring, and two enclosing curves occur to the left of the equation label. H mentions them only in editorial commentary, excluded from its source transcription here.',
   'formula25', 'omission', 'omissions')
ch('top decompositions / corrected summation sign',
   r'\Sigma_{**}=\underset{i\leq j}{\deleted{\sum}\inserted{\coprod}}\Sigma_{ij}',
   r'\Sigma_{**}=\coprod_{i\le j}\Sigma_{ij}',
   r'\Sigma_{**}=\underset{i\leq j}{\deleted{\sum}\inserted{\unsure{\coprod}}}\Sigma_{ij}',
   'The older angular Sigma/sum has a top, diagonal, and extended base. Dark right-hand downward overtracing suggests a replacement coproduct, but a separate left upright is not secure. The correction state is visible; the replacement glyph remains doubtful. The new uncertainty alone is not counted against C.',
   'coproduct_correction', 'deletion state (struck given live or live given struck)', 'struck text', confidence='medium',
   consequential='Preserves an authorial correction in the decomposition rather than presenting only an unqualified coproduct.')
ch('cancelled line below decompositions', r'\deleted{\unsure{avec} $\Sigma_{ii}\simeq\Sigma_i$)}',
   '[absent]', r'\deleted{\unsure{avec} $\Sigma_{ii}\simeq\Sigma_i$)}',
   'The line is crossed. The tentative word avec cannot be separated letter by letter; both Sigmas and their ii/i indices survive. The relation has an upper wavy run and a lower bar, not a single equality pair. A terminal closing curve survives. H has only an editorial report of a crossed formula; that report is not quoted as source transcription.',
   'cancelled_avec_formula', 'omission', 'omissions', confidence='medium')
ch('left margin / Condition circled a', r'Condition \unsure{\textcircled{a}}', 'condition (a)',
   r'Condition \textcircled{a}',
   'A capital C starts the label. The small overtraced a has a closed bowl and right-hand exit, enclosed by a complete circular stroke. Parentheses do not reproduce that enclosure. The C doubt on the circled letter is resolved at medium confidence.',
   'condition_a', 'misread symbol or index', 'symbols and indices', change_C=True, confidence='medium')
ch('left margin / first vertical marking stroke', '[absent]', '[absent]', bar_a,
   'A separate slightly wavering upright stands to the right of Condition circled a, from beside the Et line to beside the est un line. The drawing is reproduced by a graphic-only path. H mentions a vertical stroke editorially but does not reproduce it in source transcription.',
   'condition_a', 'drawing or diagram', 'drawings and diagrams', change_C=True)
ch('condition opening / Et', 'Et on', 'et on', 'Et on',
   'The first word has the large tall initial form, much higher than the following on; the high return and crosswise terminal stroke support capital Et.',
   'Et_case', 'other', 'words')
ch('condition opening / cancelled demande', r'\deleted{\unsure{demande}}', r'\struck{\ill{}}',
   r'\deleted{\unsure{demande}}',
   'There is a crossed word between on and suppose. The surviving late tall loop and trailing run permit demande, but the blackened beginning does not separate every letter. This is a tentative recovery, not a resolved cancellation.',
   'cancelled_demande', r'readable ink left as \ill{}', 'readable ink left as illegible', confidence='low', marked=True)
ch('above main line / inserted i leq j', r'\inserted{$i\leq j$}', r'\add{($i\le j$)},',
   r'\inserted{$i\leq j$}',
   'The small i, two-level order sign, and hooked j are written above the line, with a leader down before le. No enclosing parentheses surround them. The main-line comma is after the preceding i,j, not a new comma after this insertion.',
   'ij_insert', 'insertion or placement', 'insertion placement')
ch('inserted i leq j / curved leader', '[absent]', '[absent]', leader_ij,
   'The curved attachment stroke descends from the small insertion toward the position before le. It is reproduced separately from the ordinary LaTeX formula; it is not a mathematical relation sign.',
   'ij_insert', 'drawing or diagram', 'drawings and diagrams', change_C=True)
ch('right edge / le morphisme but', 'le morphisme but', "l'application but", 'le morphisme but',
   'The word begins with a low m run and has a p descender, an h loop, and a dotted i. These strokes do not form application. The compressed final me is present near the edge. The preceding le is separately written.',
   'morphisme_edge', 'misread word', 'words')
ch('cylindrique / attachment to plongement ferme', r'\inserted{``cylindrique\'\'}',
   r'\qquad\text{« cylindrique »}', r'\inserted{``cylindrique\'\'}',
   'The quoted word is above the prose, with one continuous curved leader landing after fermé. It is not a label attached to the displayed map. The two written quotation ticks at each end are retained.',
   'cylindrique_insert', 'insertion or placement', 'insertion placement')
ch('after ferme / punctuation supplied from the leader', ', (-- ce qui', '(-- ce qui', '-- ce qui',
   'The curve beginning before the dash continues under the inserted word and up to its right curl. There is no independent opening parenthesis or comma at this point. The written dash is retained. The later parentheses around par injectivité are separate genuine marks.',
   'cylindrique_insert', 'text not on the page', 'text not on page', change_C=True)
ch('cylindrique / continuous curved insertion leader', '[absent]', '[absent]', leader_cyl,
   'The same single continuous curve has a descending left end near the position after fermé and a rising curled right end under the insertion. A path reproduces this graphic without treating either end as punctuation.',
   'cylindrique_insert', 'drawing or diagram', 'drawings and diagrams', change_C=True)
ch('condition / first au dessus', 'au dessus', 'au-dessus', 'au dessus',
   'There is a word space between au and dessus, with no independent hyphen. The accented or dotted-looking a is part of the handwriting, not an intervening dash.',
   'au_dessus', 'abbreviation expanded or spelling modernised', 'abbreviation/spelling')
ch('condition / second au dessus', r'\unsure{\deleted{au}|au} \unsure{dessus|dessous} de $i$',
   r'au-dessus de $i$', r'\unsure{\deleted{au}|au} \unsure{dessus|dessous} de $i$',
   'No separate hyphen lies between the words. The heavy run through au may be cancellation or overtracing; the final low run of the next word remains compressed, so the original deletion-state and dessus/dessous doubts remain. Only the supplied hyphen is counted as a departure here.',
   'au_struck_dessus', 'abbreviation expanded or spelling modernised', 'abbreviation/spelling', confidence='medium')
ch('slanted margin note / initial word or abbreviation', r'\unsure{i.e.|via}', '[absent]',
   r'\unsure{i.e.|via}',
   'Several small written strokes precede the Sigma expression. They are not merely whitespace and cannot be omitted, but their compressed shape does not securely distinguish i.e. from via. H begins the note with the formula.',
   'margin_injectif', 'omission', 'omissions', confidence='low')
ch('Cela implique aussi / terminal punctuation', 'Cela implique aussi', 'Cela implique aussi :', 'Cela implique aussi',
   'The small detached mark belongs to the final i of aussi. No independent two-level colon follows the word.',
   'aussi_punctuation', 'text not on the page', 'text not on page')
ch('display 26 / terminal punctuation', r'(26)\qquad\Sigma_{ii}=\Sigma_i',
   r'(26)\qquad \Sigma_{ii}=\Sigma_i .', r'(26)\qquad\Sigma_{ii}=\Sigma_i',
   'The small terminal stroke is the subscript i. There is no separately placed sentence point after the formula.',
   'formula26', 'text not on the page', 'text not on page')
ch('cancelled clause / suppose and de plus', r'\deleted{suppose de plus que pour $z\in$}',
   r'\struck{\ill{} de plus, que pour $z\in$}',
   r'\deleted{\unsure{suppose} de plus que pour $z\in$}',
   'The crossed first word permits suppose through its low initial run, two descenders, and surviving end, but the overstrike obscures enough letter structure to retain a narrow doubt. De plus que pour and z followed by membership are readable. The end of plus is connected to the letter, without an independent comma. C receives uncertainty only, not a counted correction.',
   'cancelled_suppose', 'other', 'struck text', confidence='medium', marked=True)
ch('left margin / cancelled condition b', r'\deleted{condition \unsure{b)}}',
   r'\uncertain{condition} (b)', r'\deleted{condition \unsure{b)}}',
   'A long diagonal strike passes through the margin words and small final label. The final b/closing-curve cluster is still doubtful; the crossed state itself is plain. No separately secure opening parenthesis precedes that label.',
   'condition_b', 'deletion state (struck given live or live given struck)', 'struck text', marked=True)
ch('left margin / second vertical marking stroke', '[absent]', '[absent]', bar_b,
   'A live near-vertical stroke stands to the right of the crossed margin label and beside the cancelled clause and first definition. It is independent of the diagonal cancellation and runs down to the separately crossed Sigma_i level. H mentions it only editorially.',
   'condition_b', 'drawing or diagram', 'drawings and diagrams', change_C=True)
ch('first definition / live label 27', r'(27)\qquad \Sigma(n)',
   r'\struck{(27) $i<j<k$,}', r'(27)\qquad \Sigma(n)',
   'The parenthesized 27 is written above the crossed chain. The cancellation crosses the chain below, not the 27. The live label belongs spatially with the live definition that follows. The strict/nonstrict order signs in the crossed chain remain unresolved separately.',
   'cancelled_order_first27', 'deletion state (struck given live or live given struck)', 'struck text')
ch('first definition / ens', 'ens des drapeaux', r'ens.\ des drapeaux', 'ens des drapeaux',
   'The final s exits into the following space; no separate point follows ens. The abbreviation is retained without adding punctuation.',
   'definition27', 'text not on the page', 'text not on page')
ch('second display 27 / cancelled symbol before Drap', r'\deleted{\unsure{I}}', '[absent]',
   r'\deleted{\unsure{I|\Sigma}}',
   'A crossed symbol occurs between the map shaft and Drap. Top and bottom bars with a central upright or loop support I; the diagonal cancellation can create a Sigma-like outline, so I/Sigma remains open under the strict cancellation rule. H omits it from the source display and only reports a Sigma editorially. The added alternative alone is not a C correction.',
   'map27', 'omission', 'omissions', confidence='low')
ch('bottom coproduct / lower-limit continuation', r'(i_0<\unsure{\cdots}<i_n)',
   r'(i_0<\cdots<i_n)', r'(i_0<<i_n)',
   'There are two adjacent left-facing angle signs. Between them there is no third, intermediate, or dotted continuation run. The uncertain ellipsis in C and certain ellipsis in H are removed; the visible pair is retained without mathematical normalization.',
   'bottom_identity', 'text not on the page', 'text not on page', change_C=True,
   consequential='The literal written chain has adjacent < signs; no intervening terms or ellipsis are supplied.')
ch('bottom coproduct / Sigma index', r'\Sigma_{i_0- i_n}', r'\Sigma_{i_0\cdots i_n}',
   r'\Sigma_{i_0- i_n}',
   'A single continuous headless dash lies between the first and last index groups. It is not three points or multiple separated continuation strokes. The small filled loops in the lower positions are the written zeros.',
   'bottom_identity', 'misread symbol or index', 'symbols and indices',
   consequential='Preserves the written single-dash index rather than replacing it by a sequence ellipsis.')
ch('bottom coproduct / drapeau strict en I', r'\text{ drapeau strict en}\\ I\text{ de longueur }n',
   r'\text{drapeau strict}\\ \text{de } I \text{ de longueur } n',
   r'\text{ drapeau strict en}\\ I\text{ de longueur }n',
   'The preposition after strict has a small rounded e and a low n exit. It has no high d ascender. En is written before the separate next-line I.',
   'bottom_identity', 'misread word', 'words')
ch('lower left / OK placement', r'\margin{OK}', r'\qquad\text{OK}', r'\margin{OK}',
   'The closed oval O and two-armed K stand to the left of the coproduct, outside the displayed formula. H places OK to the right in its source TeX, although its editorial note reports the left position.',
   'OK', 'insertion or placement', 'insertion placement')
ch('lower left margin / note about condition',
   r"\unsure{permet ainsi l'énoncé de la condition (\unsure{b})}",
   r'\uncertain{revenir} \ill{} \uncertain{à la} condition (\ill{})',
   r"\unsure{permet ainsi l'énoncé} de la condition (\unsure{b})",
   'The top word has a p descender, a low er/m run, and a final tall t, supporting permet rather than revenir, but the flattened center remains doubtful. The next row permits ainsi l\'énoncé, with the tall l and detached accent-like marks, without separating every letter. The lower de la condition is substantially legible and has de, not à; the tiny parenthesized final letter remains doubtful. Nearby paired strokes belong to the main display\'s vertical identity, not quotation marks in this note.',
   'bottom_margin', 'misread word', 'words', change_C=True, confidence='medium', marked=True)
ch('bottom left / foliation 43', r'\mspage{43}', '[absent]', r'\margin{43}',
   'A thin grey 4 and 3 stand at the bottom left, unlike the darker main writing. Their identity is clear, but attribution to the author is not established. They are retained as a marginal foliation rather than asserted to be his own page number.',
   'folio43', 'insertion or placement', 'other', change_C=True, confidence='medium')

# Replace Python quoting used to keep doubled source quote marks readable.
for row in changes:
    for field in ('C','H','final'):
        row[field] = row[field].replace("\\'", "'")

MARK_DATA = {
 r'\unsure{avec}': ('undecided',r'\unsure{avec}','cancelled_avec_formula','low','The crossed low letter run is compatible with avec, but the stroke obscures the internal letter junctions. No complete resolution of a cancelled word is claimed.'),
 r'\unsure{demande}': ('undecided',r'\unsure{demande}','cancelled_demande','low','The late high loop and end survive; the beginning is too blackened to separate each letter.'),
 r'\unsure{immersion|immersement}': ('undecided',r'\unsure{immersion|immersement}','immersion','low','The crossed middle is dense. Both original possibilities are retained because their differentiating letters are not individually plain.'),
 r'\unsure{\deleted{au}|au}': ('undecided',r'\unsure{\deleted{au}|au}','au_struck_dessus','medium','The closed a and flattened u can be read, but the heavy horizontal run cannot securely be separated into cancellation versus letter overtracing.'),
 r'\unsure{dessus|dessous}': ('undecided',r'\unsure{dessus|dessous}','au_struck_dessus','medium','The outline resembles the earlier dessus, but the final low letters are compressed enough that the alternative is not excluded.'),
 r'\unsure{\textcircled{a}}': ('first',r'\textcircled{a}','condition_a','medium','The overtraced small bowl with a right-hand exit supports a and the enclosing stroke forms a circle, not two separate parentheses.'),
 r'\unsure{i.e.|via}': ('undecided',r'\unsure{i.e.|via}','margin_injectif','low','Several small strokes precede the formula, but the tilted crowded sequence does not securely distinguish i.e. from via.'),
 r'\unsure{injectif}': ('undecided',r'\unsure{injectif}','margin_injectif','medium','The initial dotted stroke and late tall exit support injectif; the flattened intervening letters remain insufficiently separated.'),
 r'\unsure{On|Car}': ('undecided',r'\unsure{Car|On}','On_Car','medium','An open capital C, a low loop, and long r-like exit favor Car; the compressed outline does not fully exclude On. Reordering alternatives is not counted as a correction.'),
 r'\unsure{i}': ('undecided',r'\unsure{i}','cancelled_order_first27','low','The initial short stroke is crossed and lacks a securely assignable detached dot; i remains tentative.'),
 r'\unsure{b)}': ('undecided',r'\unsure{b)}','condition_b','low','The small terminal loop and curve lie under the diagonal strike. They do not securely separate the letter from the closing curve.'),
 r'\unsure{I}': ('undecided',r'\unsure{I|\Sigma}','map27','low','Upper and lower bars with a central upright favor I, while the cancel stroke creates a Sigma-like diagonal. The cancelled glyph is not fully recovered.'),
 r'\unsure{\cdots}': ('other',r'(i_0<<i_n)','bottom_identity','high','The whole lower-limit tuple has two adjacent < signs and no intervening continuation marks. The putative ellipsis is absent, not merely a different kind of ellipsis.'),
 r"\unsure{permet ainsi l'énoncé de la condition (\unsure{b})}": ('other',r"\unsure{permet ainsi l'énoncé} de la condition (\unsure{b})",'bottom_margin','medium','The lower de la condition can be read from separate letter forms. The first two rows remain compressed and the final letter stays separately doubtful; this is a partial narrowing of the original large mark.'),
 r'\unsure{b}': ('undecided',r'\unsure{b}','bottom_margin','low','The parenthesized very low mark does not provide a clearly separate bowl and upright; b is retained only as a tentative reading.')
}

marks=[]
for m in re.finditer(r'\\(?:unsure|illegible)\{', C):
    depth=1; end=m.end()
    while depth:
        if C[end]=='{': depth+=1
        if C[end]=='}': depth-=1
        end+=1
    mark=C[m.start():end]
    decision,reading,crop,confidence,evidence=MARK_DATA[mark]
    a=max(C.rfind('\n',0,m.start())+1,m.start()-50)
    b=C.find('\n',end)
    if b<0:b=len(C)
    b=min(b,end+55)
    marks.append(dict(mark=mark,context=C[a:b],decision=decision,reading=reading,evidence=evidence,
                      crop=cs(crop),box=box(crop),confidence=confidence))

inventory=[]
def inv(element,kind,position,words,hand='his hand'):
    inventory.append(dict(element=element,kind=kind,position=position,
        first_words_or_objects=words,sheet_kind='text',hand=hand,transcribed='yes'))
inv('T01','text','top / physical rows 1–2', 'précisément, on a de plus une application croiss. et continue')
inv('D01','display','upper page / row 3',r'(2^\circ), (\unsure{1|2}5), \Sigma_*\longrightarrow I')
inv('T02','text','row 4 opening',"(d'où")
inv('D02','display','row 4 / two decompositions',r'\Sigma_*=\coprod_{i\in I}\Sigma_i ; \Sigma_{**}=\underset{i\leq j}{\deleted{\sum}\inserted{\unsure{\coprod}}}\Sigma_{ij})')
inv('X01','deletion','below right-hand decomposition',r'\unsure{avec} \Sigma_{ii}\simeq\Sigma_i)')
inv('M01','margin note','left margin / beside rows 5–7','Condition circled a')
inv('G01','drawing','right of M01 / x approximately 280, y 603–860','slightly wavering vertical marking stroke')
inv('T03','text','rows 5–6','Et on ... suppose que ... le morphisme but')
inv('X02','deletion','row 5 / between on and suppose',r'\unsure{demande}')
inv('I01','insertion','above row 5 / after the comma following i,j and before le',r'i\leq j')
inv('G02','drawing','below I01 / before le','short curved insertion leader')
inv('D03','display','row 6 / after but',r'\Sigma_{ij}\unsure{-|\longrightarrow}\Sigma_j')
inv('T04','text','rows 7–11','est un ... plongement fermé ... -- ce qui implique ... au plus ... avec y≤z.')
inv('X03','deletion','row 7 / after est un',r'\unsure{immersion|immersement}')
inv('I02','insertion','above row 7 / attached after fermé',"``cylindrique''")
inv('G03','drawing','beneath I02 / left end before the main dash','one continuous insertion curve with a right curl')
inv('X04','deletion','row 11 / after y∈Σ_*; deletion state itself unresolved',r'\unsure{\deleted{au}|au}')
inv('M02','margin note','left margin / tilted up to the right beside rows 9–12',r'\unsure{i.e.|via} \Sigma_*^{\leq z}\longrightarrow I^{\leq j} \unsure{injectif}')
inv('T05','text','row 12','Cela implique aussi')
inv('D04','display','row 13',r'(26)\quad\Sigma_{ii}=\Sigma_i')
inv('T06','text','row 14 / opening',r'\unsure{Car|On}')
inv('X05','deletion','row 14 / after live opening',r'\unsure{suppose} de plus que pour z\in')
inv('X06','deletion','below row 14 and below the live first (27)',r'\unsure{i}\unsure{\leq|<}j\unsure{\leq|<}k,')
inv('M03','margin note','left margin / beside rows 14–17; crossed label',r'\deleted{condition \unsure{b)}}')
inv('G04','drawing','right of M03 / x approximately 278, y 1580–1790','separate live near-vertical marking stroke')
inv('D05','display','rows 15–16 / first live (27)',r'\Sigma(n)=ens des drapeaux stricts de longueur n de \Sigma')
inv('X07','deletion','row 17 / below definition, toward its left',r'\Sigma_i')
inv('T07','text','row 18 / left of second (27)',r'\unsure{ou|et}')
inv('D06','display','rows 19–23 / complete map and vertical identity',r'(27), \Sigma(n)\to\operatorname{Drap}_n(I), \Vert, \coprod_{(i_0<<i_n)}\Sigma_{i_0-i_n}; drapeau strict en I de longueur n')
inv('X08','deletion','row 19 / between the arrow and Drap',r'\unsure{I|\Sigma}')
inv('M04','margin note','lower left / immediately left of the coproduct','OK')
inv('M05','margin note','lower left / tilted three-row annotation beside the vertical identity',r"\unsure{permet ainsi l'énoncé} de la condition (\unsure{b})")
inv('M06','margin note','bottom left / thin foliation','43','thin different-looking ink; attribution uncertain')

doubts=[]
def doubt(place,reading,alternatives,confidence='medium'):
    doubts.append(dict(place=place,reading=reading,alternatives=alternatives,confidence=confidence))
doubt('first displayed equation label',r'(\unsure{1|2}5)','First digit: narrow bent upright supports 1; 2 remains possible. Later prose (25*) has a clear curved 2.')
doubt('replacement for crossed sum',r'\deleted{\sum}\inserted{\unsure{\coprod}}','Coproduct-like overtrace; separate left upright not secure.','low')
doubt('crossed line under decomposition',r'\deleted{\unsure{avec} $\Sigma_{ii}\simeq\Sigma_i$)}','avec remains tentative; relation and indices readable.','low')
doubt('crossed word before suppose',r'\deleted{\unsure{demande}}','demande remains tentative under the strike.','low')
doubt('but-map connector',r'\Sigma_{ij}\unsure{-|\longrightarrow}\Sigma_j','A long shaft ending in a nearly vertical blob: dash or very small-headed arrow. No paired arrowhead is required, but no decisive terminal head is separable.')
doubt('crossed noun before plongement',r'\deleted{\unsure{immersion|immersement}}','immersion | immersement; differentiating letters remain obscured.','low')
doubt('au deletion state',r'\unsure{\deleted{au}|au}','cancelled au | live au; the heavy run could be cancellation or overtracing.')
doubt('following dessus/dessous',r'\unsure{dessus|dessous}','dessus favored by the earlier comparison, but compressed terminal letters leave dessous possible.')
doubt('tilted margin note / initial token',r'\unsure{i.e.|via}','i.e. | via','low')
doubt('tilted margin note / final word',r'\unsure{injectif}','injectif, with compressed middle')
doubt('opening before cancelled clause',r'\unsure{Car|On}','Car favored from open C and long r-like exit; On not fully excluded.')
doubt('cancelled suppose',r'\deleted{\unsure{suppose} de plus que pour $z\in$}','suppose tentative; no completion after z∈.','low')
doubt('crossed margin label',r'\deleted{condition \unsure{b)}}','b plus closing curve, still merged by the cancellation.','low')
doubt('crossed order formula',r'\deleted{$\unsure{i}\unsure{\leq|<}j\unsure{\leq|<}k$,}','Initial i doubtful; each order sign may have a genuine lower bar or only the crossing stroke. Whole chain retained with narrow doubts.','low')
doubt('word before second display',r'\unsure{ou|et}','ou favored, et not excluded by the oval and rising-loop outline.')
doubt('cancelled symbol before Drap',r'\deleted{\unsure{I|\Sigma}}','I | Sigma; overlaid diagonal prevents a complete cancelled-glyph reading.','low')
doubt('right-edge word ending',r'\text{(drapeaux stric}\unsure{\text{t|ts}}\unsure{)}','The terminal C-like cluster may be t or ts; no separately secure final s. A tiny edge curve may be the remaining bottom of the closing parenthesis. No additional letters are supplied.')
doubt('lower margin note / first two rows',r"\unsure{permet ainsi l'énoncé}",'permet ainsi l’énoncé is supported but the flattened runs remain compressed.','low')
doubt('lower margin note / final letter',r'(\unsure{b})','b remains tentative within the visible parentheses.','low')

notes=[
 'The page reports an increasing continuous map from Sigma_* to I, its decompositions, and a closed cylindrical embedding condition on the but map. It states an at-most-one predecessor consequence, writes Sigma_ii=Sigma_i, then introduces strict flags and a vertically displayed coproduct expression. This is a report of the manuscript, not a proof check.',
 'The first equation label has a genuine narrow 1|2 doubt before 5. The later prose reference (25*) and the two later labels (27), as well as (26), are read independently. No numbering repair is made.',
 'The lower-limit chain literally has two adjacent < signs without continuation dots. The lower Sigma index contains a single dash. Neither feature has been normalized by mathematical expectation.',
 'The crossed top relation is simeq, not a simple equality. Because H reports that line only inside an editorial note, its note is excluded from source quotations and is not counted as a source equality reading.',
 'The sum-to-coproduct-looking correction is retained with its older sum and a doubtful replacement. The but-map connector is left as dash/arrow. These are reading reservations, not claims of mathematical error.',
 'The continuous curve beneath cylindrique is an insertion leader, with no independent comma or opening parenthesis after fermé. The short i≤j leader attaches before le after the comma following i,j. Graphic-only TikZ paths reproduce both leaders; all words and formulas remain ordinary LaTeX.',
 'The first marginal vertical stroke extends approximately from the Et line to the est un line (x≈280, y603–860). The second live upright extends beside the cancelled clause/first definition down to the separately cancelled Sigma_i level (x≈278, y1580–1790). They are distinct from cancellation strokes and are reproduced separately.',
 'The original physical line count is 23, counting the displayed-map row, vertical-identity row, coproduct row, and its two lower-limit rows separately; margin annotations and between-line insertions are inventoried separately.',
 'The right edge contains a terminal t/ts-like cluster and a possible small bottom of a closing parenthesis. No certain full stricts) ending or extra lost letters are supplied.',
 'The lower margin note is three tilted rows; its de la condition is read, while the first two rows and final parenthesized letter remain doubtful. The nearby paired marks are part of the main vertical identity and are not transcribed as quotation marks in the note.',
 'The thin bottom-left 43 is retained as a marginal foliation of uncertain attribution. There is no authorial upper page number visible on this sheet.',
 'Whole image and both supplied native halves were read once, including agreed tokens, all cancellations, and all insertions. Thirty-three distinct crop places produced thirty-three saved crop images; all were actually viewed. The final three images were viewed after an earlier batched output was truncated; the unsettled right-edge crop was reused to answer the editor’s edge question without making another crop.',
 'Source witness quotes exclude all H editorial notes. Adding uncertainty or retaining/reordering alternatives alone is excluded from substantive change counts, including the first label, replacement coproduct, but-map connector, Car/On, cancelled order signs, ou/et, cancelled I/Sigma, and the right-edge ending. H’s insertion wrapper around the separately crossed Sigma_i is treated as markup rather than evidence of a separate visible insertion leader.',
 'Second-reading boxes are preparation for the independent audit only; this reader has not begun a second reading or any other page. No OCR, TeX compilation, or mathematical verification was performed.'
]

notation=[
 dict(form=r'\Sigma_*,\Sigma_{**}',meaning_or_shape='Small star forms may be compressed; the detached cap belongs to the angular Sigma and is not separately promoted to an overbar.',places='top map/decompositions and main condition'),
 dict(form=r'I',meaning_or_shape='Serifed capital I has top and bottom strokes; central upright and cancel overtracing can mimic Sigma in the cancelled target.',places='first display, margin formula, Drap_n(I), cancelled symbol before Drap'),
 dict(form=r'\Vert',meaning_or_shape='Two separate vertical strokes, preserved as a vertical identity rather than turned into a horizontal equals sign.',places='bottom aligned display'),
 dict(form=r'(i_0<<i_n)',meaning_or_shape='Two literal adjacent less-than signs; no dots between them.',places='bottom coproduct lower limit'),
 dict(form=r'\Sigma_{i_0- i_n}',meaning_or_shape='One single dash separates the endpoint groups in the written subscript.',places='bottom coproduct'),
 dict(form=r'\operatorname{Drap}_n(I)',meaning_or_shape='Drap with lower n and parenthesized serif I; used here for the displayed flag target.',places='second (27)')
]
abbreviations=[
 dict(form='croiss.',expansion='croissante (expansion supplied only in this record; not in the transcription)'),
 dict(form='ens',expansion='ensemble (no manuscript stop follows ens)'),
 dict(form=r'\unsure{i.e.|via}',expansion='If i.e. is the reading, id est; the token remains unresolved against via and is not expanded in the page.')
]
hand_log=[
 dict(habit='Tall capital initial in Et',places='condition opening',consistent='single local occurrence, directly cropped',witness_errors='H lowercases Et to et.'),
 dict(habit='Abbreviations may end in a full point or have no point',places='croiss.; ens',consistent='croiss. has a separate point; ens does not',witness_errors='H expands croiss. and adds a point after ens.'),
 dict(habit='A narrow first label digit differs from the clearly curved later 2 forms',places='first displayed 15/25; prose 25*; 26; both 27 labels',consistent='first digit remains an explicit local exception, not normalized from later forms',witness_errors='Both witnesses print certain 25 in the first label; this is uncertainty-only, not counted as an established error.'),
 dict(habit='Dark correction strokes can manufacture apparent lower relation bars or Sigma diagonals',places='crossed order chain; cancelled symbol before Drap; sum correction',consistent='several crossed places; each remains independently judged',witness_errors='No certain strict/nonstrict or I/Sigma correction is claimed; H omits the cancelled target from source transcription.'),
 dict(habit='Very small arrow terminal returns can resemble a vertical blob',places='but map compared with top and bottom maps',consistent='but connector remains exceptional and doubtful',witness_errors='Both witnesses give an arrow; no certain change is counted.'),
 dict(habit='Insertion leaders can resemble punctuation at their descending ends',places='i≤j insertion; cylindrique insertion',consistent='two attached insertions; cylindrique has one continuous curve',witness_errors='C and H infer an opening parenthesis after fermé; C also supplies a comma. H places cylindrique beside the map.'),
 dict(habit='Continuation marks must be counted literally',places='bottom lower-limit chain and Sigma subscript',consistent='two adjacent < signs in the bound; one dash in the subscript',witness_errors='C and H supply an ellipsis in the lower-limit chain; H supplies an ellipsis in the subscript.'),
 dict(habit='Low runs in sloping marginal prose may not separate every letter',places='i.e./via and injectif margin; lower permet note',consistent='both notes contain unresolved compressed runs',witness_errors='H omits the initial token of the upper note and proposes revenir/à la in the lower note.'),
 dict(habit='A thin different-looking foliation occurs at the bottom left',places='43',consistent='single local numeral',witness_errors='C labels it as his page number; H source transcription omits it; authorship is not established.')
]

# Audit readings use complete source blocks. They are not a second visual pass.
second_boxes=[]
def sb(num,kind,coords,reading,reason):
    second_boxes.append(dict(box=f'b{num:02d}',kind=kind,coords=coords,reading=reading,reason=reason))

sb(1,'C/H word difference',[300,165,962,244], 'croiss. et continue',
   'Complete second physical row; covers the written abbreviation versus H expansion.')
sb(2,'doubt formula|handwritten number',[170,245,1000,370],
   r'(2^\circ)\quad (\unsure{1|2}5)\qquad\Sigma_*\longrightarrow I',
   'Whole displayed map with both handwritten labels and the new first-digit doubt.')
sb(3,'insertion|struck passage|doubt formula',[295,380,1668,580],
   r"(d'où \Sigma_*=\coprod_{i\in I}\Sigma_i,\quad \Sigma_{**}=\underset{i\leq j}{\deleted{\sum}\inserted{\unsure{\coprod}}}\Sigma_{ij})\quad\deleted{\unsure{avec} $\Sigma_{ii}\simeq\Sigma_i$)}",
   'Whole decomposition row, its correction, and the entire crossed line below its right-hand side. Includes every doubtful formula and the insertion/cancellation state.')
sb(4,'margin note|struck passage|insertion|C/H word difference|doubt formula',[20,545,1682,805],
   r'\margin{Condition \textcircled{a}} [live vertical marking stroke, continuing below this box] Et on \deleted{\unsure{demande}} suppose que $\forall i,j$, \inserted{$i\leq j$} [curved leader before le] le morphisme but $\Sigma_{ij}\unsure{-|\longrightarrow}\Sigma_j$',
   'Complete condition opening, inserted inequality and leader, margin label, cancelled demande, and whole doubtful but map. Covers Et/et and morphisme/application disagreements. The vertical bar continues below the box, so its full extent is additionally covered in b05.')
sb(5,'margin note|struck passage|insertion|C/H word difference|low-confidence departure',[20,565,1682,1002],
   r'\margin{Condition \textcircled{a}} [complete live vertical marking stroke] Et on \deleted{\unsure{demande}} suppose que $\forall i,j$, \inserted{$i\leq j$} [curved leader before le] le morphisme but $\Sigma_{ij}\unsure{-|\longrightarrow}\Sigma_j$ est un \deleted{\unsure{immersion|immersement}} plongement fermé \inserted{``cylindrique\'\'} [continuous curved leader] -- ce qui implique (par injectivité) que (25$^*$) a',
   'Complete rows from Et through the prose reference, including all coherent content inside the rectangle. Covers both insertions, full first marking stroke, all cancellations there, the whole doubtful map, H injectivité doubt, and handwritten 25*.')
sb(6,'handwritten number|C/H word difference',[296,890,1668,1204],
   r'implique (par injectivité) que (25$^*$) a la propriété que si $z\in\Sigma_*$ est au dessus de $j$ et si $i\leq j$, alors il existe \uline{au plus}',
   'Complete three main prose rows. Includes the whole reference 25*, first au dessus spelling, and explicit underline of au plus.')
sb(7,'margin note|struck passage|doubt formula|C/H word difference',[20,1010,1675,1432],
   r'la propriété que si $z\in\Sigma_*$ est au dessus de $j$ et si $i\leq j$, alors il existe \uline{au plus} un $y\in\Sigma_*$ \unsure{\deleted{au}|au} \unsure{dessus|dessous} de $i$, avec $y\leq z$. \margin{\unsure{i.e.|via} $\Sigma_*^{\leq z}\longrightarrow I^{\leq j}$ \unsure{injectif}} Cela implique aussi',
   'Whole corresponding main prose rows plus the whole tilted margin formula/note and complete Cela line. Covers uncertain au deletion state, dessus/dessous, margin initials/final word, and the missing H initial token; no target-only fragment is substituted for a full formula.')
sb(8,'handwritten number',[282,1425,1048,1542],r'(26)\qquad\Sigma_{ii}=\Sigma_i',
   'Entire displayed equality, both ii/i indices, handwritten 26, and absence of an independent final point.')
sb(9,'margin note|struck passage|doubt formula|handwritten number|C/H word difference|low-confidence departure',[52,1515,1674,1817],
   r'\margin{\deleted{condition \unsure{b)}}} [complete live vertical marking stroke] \unsure{Car|On} \deleted{\unsure{suppose} de plus que pour $z\in$} \deleted{$\unsure{i}\unsure{\leq|<}j\unsure{\leq|<}k$,} $(27)\quad\Sigma(n)=\text{ens des drapeaux stricts de longueur }n\text{ de }\Sigma$ \deleted{$\Sigma_i$}',
   'Complete cancelled clause, margin cancellation and independent bar, whole cancelled order formula, live first 27, full definition including de Sigma on the next row, and separately crossed Sigma_i. Covers suppose/ill, absence of comma after plus, ens/ens., and every doubt/cancellation in the block.')
sb(10,'margin note|struck passage|doubt formula|handwritten number|C/H word difference|low-confidence departure',[20,1818,1685,2235],
   r'\unsure{ou|et}\quad (27)\qquad\begin{aligned}\Sigma(n)&\longrightarrow\deleted{\unsure{I|\Sigma}}\operatorname{Drap}_n(I)\quad\text{(drapeaux stric}\unsure{\text{t|ts}}\unsure{)}\\\Vert\quad&\\\coprod_{\substack{(i_0<<i_n)\text{ drapeau strict en}\\ I\text{ de longueur }n}}\Sigma_{i_0- i_n}&\end{aligned}\quad\margin{OK}\margin{\unsure{permet ainsi l\'énoncé} de la condition (\unsure{b})}',
   'Whole final map/vertical identity/coproduct block, including the handwritten label, numeric subscripts, crossed target, edge ending, unresolved ou/et disagreement, exact continuation marks, en/de I disagreement, OK, and complete lower-left note. The full-width rectangle prevents partial margin fragments or isolated formula labels.')
sb(11,'margin note|handwritten number|low-confidence departure',[15,2285,88,2348],r'\margin{43}',
   'Entire thin foliation, including both digits and its nonauthorial/uncertain-attribution placement classification.')
for row in second_boxes:
    row['reading']=row['reading'].replace("\\'", "'")

# Crowded margins overlap adjacent text. Merge those boxes rather than leave
# unreported complete words at a rectangle's side or a formula fragment above it.
second_boxes[0]['coords']=[290,165,1670,244]
top_block=second_boxes[2]
top_block['coords']=[20,380,1682,1002]
top_block['kind']='insertion|margin note|struck passage|doubt formula|handwritten number|C/H word difference|low-confidence departure'
top_block['reading'] += ' ' + second_boxes[4]['reading']
top_block['reason']='Complete source block from the two decompositions through the prose reference (25*): includes the corrected sum, complete cancelled formula, Condition circled a and full bar, whole condition opening, both insertions and leaders, both cancelled words, the full doubtful but map, and every complete prose row inside the rectangle. The wider box avoids cutting the sloping cancellation and insertions into target-only fragments.'
middle_block=second_boxes[5]
middle_block['coords']=[20,890,1675,1432]
middle_block['kind']='margin note|struck passage|doubt formula|handwritten number|C/H word difference'
middle_block['reading']=r'implique (par injectivité) que (25$^*$) a '+second_boxes[6]['reading']
middle_block['reason']='Complete main prose from implique through Cela implique aussi, together with the whole tilted margin formula/note. Covers handwritten 25*, both au dessus spellings, underline, uncertain au deletion state, dessus/dessous, the entire doubtful margin formula and its words, and absence of a colon after aussi. Full width avoids leaving the upper-right end of the sloped note unreported.'
second_boxes[8]['coords']=[52,1515,1674,1820]
second_boxes=[second_boxes[i] for i in [0,1,2,5,7,8,9,10]]
for i,row in enumerate(second_boxes,1):
    row['box']=f'b{i:02d}'

data=dict(scan=44,reader='reader_a',line_count=23,changes=changes,marks=marks,inventory=inventory,
    doubts=doubts,notes=notes,check_events=[],notation=notation,abbreviations=abbreviations,
    hand_log=hand_log,second_boxes=second_boxes,
    crop_register=[dict(place=k,file=v['file'],box=v['box'],rotation_degrees=v['rotation_degrees'],viewed=True)
                   for k,v in CROPS.items()],
    coverage=dict(whole_viewed_once=True,top_half_viewed_once=True,bottom_half_viewed_once=True,
                  agreed_tokens_read=True,all_insertions_and_cancellations_inspected=True,
                  crop_places=len(CROPS),crop_images=len(CROPS),all_crops_viewed=True,
                  original_C_marks=len(marks),second_reading_started=False))

def norm(s):
    return re.sub(r'\s+', ' ', s).strip()

def without_macro(text,name):
    pat='\\'+name+'{'
    while pat in text:
        a=text.index(pat); p=a+len(pat); depth=1
        while depth:
            if text[p]=='{':depth+=1
            if text[p]=='}':depth-=1
            p+=1
        text=text[:a]+text[p:]
    return text

H_source=without_macro(H,'note')
errors=[]
for i,row in enumerate(changes,1):
    for key,src in [('C',C),('H',H_source)]:
        if row[key]!='[absent]' and norm(row[key]) not in norm(src):
            errors.append(f'change {i}: {key} quote not exact: {row[key]}')
    if norm(row['final']) not in norm(T):
        errors.append(f"change {i}: final not in TeX: {row['final']}")
    if not (BASE/'crops'/row['crop']).exists():errors.append(f'change {i}: missing crop')
for row in marks:
    if row['mark'] not in C or row['context'] not in C:errors.append('mark/context not exact')
    if norm(row['reading']) not in norm(T):errors.append('mark final not in TeX: '+row['reading'])
    if not (BASE/'crops'/row['crop']).exists():errors.append('missing mark crop')
depth=0
for c in T:
    if c=='{':depth+=1
    elif c=='}':depth-=1
    if depth<0:errors.append('premature closing TeX brace');break
if depth:errors.append('unbalanced TeX braces')
if len(CROPS)!=33:errors.append(f'crop count {len(CROPS)} != 33')
if len(marks)!=15:errors.append(f'C mark count {len(marks)} != 15')
if errors:
    raise SystemExit('\n'.join(errors))
data['validation']=dict(exact_C_quotes=True,exact_H_source_quotes_excluding_notes=True,
    all_change_finals_present=True,all_original_C_marks_accounted=True,all_crops_exist=True,
    tex_braces_balanced=True,tex_compiled=False)
(OUT/'150_scan044.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(scan=44,changes=len(changes),marks=len(marks),inventory=len(inventory),
                     doubts=len(doubts),second_boxes=len(second_boxes),crops=len(CROPS)),ensure_ascii=False))
