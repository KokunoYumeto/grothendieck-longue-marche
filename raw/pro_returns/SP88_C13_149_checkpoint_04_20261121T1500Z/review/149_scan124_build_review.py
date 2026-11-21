from pathlib import Path
import json

ROOT=Path('/workspace/scratch/0cab6a548abb')
OUT=ROOT/'edition/review'
PAGE='149_scan124'
G={g['id']:g for g in json.loads((OUT/f'{PAGE}_crop_geometry.json').read_text(encoding='utf-8'))}

first=r'''$O'$ de $O$ dans $\overline L$ i.e. $S'$ de $S$ dans $L$, et pour $x'$ au dessus de $x$, un groupe de décomposition $N_{x'}$, d'inertie $I_{x'}$, ayant les interprétations qu'on a signalé plus haut dans le cas particulier d'un $O$ qui est un anneau jauge.'''
valuation=r'''L'idée, c'est que prenant $O$ de valuation (pas néc. une jauge) $\supset K$, on trouve des groupes d'inertie à structure simple ---'''
margin_formula=r'''\margin{$T_\infty=T_\infty(\overline L)$}'''
inertia=r'''des $T_\infty^\alpha$ essentiellement, où $\alpha$ est la ``codim'' du $x\in\mathfrak X$ correspondant --- et si $a$ est de dim $0$, on aur. une extension de $\mathcal E_{k(x)}^{\overline{k(a)}}$ --- ss-groupe ouvert de $\mathcal E_K$, puisque'''
margin_note=r'''\margin{on le\newline supposera\newline du moins\newline ici}'''
ending=r'''$k(a)$ est \inserted{\uline{fini}} alg. sur $K$ --- \deleted{\unsure{de}}\unsure{par} $T^\alpha$, qu'on aura une chance de pouvoir scinder sans trop de mal. Ceci donne-'''
folio=r'''\margin{123}'''
candidate='\\scanpage{124}\n'+first+' '+valuation+'\n'+margin_formula+'\n'+inertia+'\n'+margin_note+'\n'+ending+'\n'+folio+'\n'
(OUT/f'{PAGE}.tex').write_text(candidate,encoding='utf-8')

changes=[]
def add(place,C,H,final,evidence,crop,confidence='high',vs_C=False,vs_H=True,
        kind='misread word',category='Words',H_marked=False,consequential=False,**extra):
    row={'id':f'p{len(changes)+1:02d}','place':place,'C':C,'H':H,'final':final,
         'evidence':evidence,'crop':G[crop]['file'],'bbox':G[crop]['bbox'],
         'confidence':confidence,'vs_C':vs_C,'vs_H':vs_H,'kind':kind,
         'error_category':category,'H_marked':H_marked,'consequential':consequential}
    row.update(extra)
    changes.append(row)

add('main line 1, first two O forms', r"$O'$ de $O$",r"$\underline{O}'$ de $\underline{O}$",r"$O'$ de $O$",
    'Both O forms are single rounded loops with no separate lower stroke. The first has a short raised prime at its right. The return at the top of the second O belongs to its loop; it is not an underline.',
    'p01',kind='misread symbol or index',category='Symbols and indices')
add('main line 1, last field after S',r'$S$ dans $L$',r'$S$ dans $\overline{L}$',r'$S$ dans $L$',
    'The earlier L in this same line has a clear detached bar. The final L after S has only its vertical and basal strokes, with open blank paper above it. No overbar is written there.',
    'p01',kind='misread symbol or index',category='Symbols and indices',consequential=True)
add('main line 2, location phrase', 'au dessus','au-dessus','au dessus',
    'The small au is separated from dessus by open space. No hyphen joins the words. The short written strokes belong within au and at the start of dessus.',
    'p02',kind='abbreviation expanded or spelling modernised',category='Abbreviations expanded, spelling modernised')
add('main line 4, word following I-subscript comma','ayant',r'\uncertain{mais}','ayant',
    'The word has a long descending y after the low a entry, then the reduced ant movement ending in a tall angled t. A mais reading cannot account for the descender. p11 completes the y tail clipped at the bottom of p02.',
    'p11',H_marked=True)
add('transition from main line 4 to line 5',r"les interprétations qu'on a signalé",r"les interprétations \ill{} qu'on a \uncertain{signalé}",r"les interprétations qu'on a signalé",
    'interprétations ends at the right of line 4. The next line begins directly with qu’on a signalé; there is no intervening word or cancelled group. signalé has a g loop whose descending stroke curves left beneath the word, not a separate underline.',
    'p03',kind='text not on the page',category='Text that is not on the page',H_marked=True,
    scope='The extra illegible placeholder is not supported by intervening ink; the matching base word signalé is not counted as a separate error.')
add('main line 6, O after d’un',r"d'un $O$",r"d'un $\underline{O}$",r"d'un $O$",
    'The O is a loop with a rightward return at its top. Its underside is blank; there is no lower bar. The neighboring q descender belongs to qui.',
    'p03',kind='misread symbol or index',category='Symbols and indices')
add('main lines 7–8, transition after c’est que','prenant',r'\uncertain{pour} \uncertain{prenant}','prenant',
    'The line ending que is followed on the next line directly by prenant. The only word at the left of that next baseline has the p descender and the full prenant sequence. There is no separate pour between them.',
    'p04',kind='text not on the page',category='Text that is not on the page',H_marked=True)
add('main line 8, O before de valuation',r'$O$ de valuation',r'$\underline{O}$ de valuation',r'$O$ de valuation',
    'This O has the same plain loop and upper return as the preceding plain O. No independent horizontal stroke sits below it.',
    'p04',kind='misread symbol or index',category='Symbols and indices')
add('main line 8, first word of parenthesis','pas','par','pas',
    'After the opening parenthesis the p descender is followed by a reduced a and a low final s movement. The terminal does not show a separate r upturn.',
    'p04',consequential=True)
add('main line 8, abbreviation in parenthesis','néc.','ex.','néc.',
    'The group begins with a low n movement, followed by a small accented e and an open final c before a separate dark stop. It has neither the initial e of ex. nor crossed x diagonals.',
    'p04',consequential=True)
add('main line 8, article at the line end','une','un','une',
    'The low joined word continues past the n into a final e-like return. Its shape agrees with the written une later before extension and before chance on this page.',
    'p04')
add('main line 9, end of valuation parenthesis','jauge)',r'\uncertain{jauge}-$\underline{O}$)','jauge)',
    'The word jauge is followed directly by the closing parenthesis, then the superset sign and K. Its looped g descender and terminal e account for the marks before the parenthesis; no hyphen or separate O follows it.',
    'p04',kind='text not on the page',category='Text that is not on the page',H_marked=True)
add('main line 9, verb after on','trouve','trouvera','trouve',
    'The word has the tall crossed t and compact rouve sequence. It ends in a small terminal stroke before the separate des group. No additional ra sequence is written.',
    'p04')
add('main line 12, quotation marks around the short form',"``codim''",'« codim »',"``codim''",
    'Two short raised strokes precede codim and a compact paired raised closing mark follows it. These are upper double-quote marks, not lateral angled guillemets. No stop is supplied after codim.',
    'p05',kind='misread symbol or index',category='Symbols and indices')
add('main line 13, point after et si',r'$\unsure{a|x}$',r'$x$',r'$a$',
    'The point letter has a small left bowl and a right descending return. It lacks the two opposing open/crossing strokes of x in the preceding x∈X and in the E subscript below. The closed-bowl a form is repeated in both later k(a) occurrences.',
    'p06',kind='misread symbol or index',category='Symbols and indices',consequential=True)
add('main line 14, abbreviated future verb',r'\unsure{aur.|aura}',r'\uncertain{on a}', 'aur.',
    'The cropped word has a compact a entry, a long low u movement, a final r flick and a detached dark stop. There is no final a bowl. The fully written aura on line 17 has an additional terminal a shape and supplies a local comparison.',
    'p06',H_marked=True,scope='Only the verb is collated; on at the end of line 13 is already written in both witnesses.')
add('main line 14, one extension phrase and one E expression',
    r'une extension de $\mathcal E_{k(x)}^{\overline{k(\unsure{a|x})}}$',
    r'$\mathcal{E}_{k(x)}^{\overline{k(x)}}$ --- \ill{} une extension de $\mathcal{E}_{k(x)}$',
    r'une extension de $\mathcal E_{k(x)}^{\overline{k(a)}}$',
    'After aur. the ink runs une extension de and then one E expression, with its subscript and barred exponent together. No E expression precedes une, and no extra separating dash or illegible group is written there. The sole following dash is after the complete formula.',
    'p06',kind='text not on the page',category='Text that is not on the page',H_marked=True,
    scope='Duplicate formula/order only. The exponent argument a versus x is collated separately.',consequential=True)
add('main line 14, exponent argument in complete E expression',
    r'$\mathcal E_{k(x)}^{\overline{k(\unsure{a|x})}}$',
    r'$\mathcal{E}_{k(x)}^{\overline{k(x)}}$',
    r'$\mathcal E_{k(x)}^{\overline{k(a)}}$',
    'The complete formula shows an open/crossing x in the lower k(x), but a small closed left bowl with a right return in the upper k(a). The exponent has an independent overbar spanning its k(a). The distinction between the two arguments is visible and is not harmonized.',
    'p06',kind='misread symbol or index',category='Symbols and indices',consequential=True)
add('main line 15, short prefix before groupe','ss-groupe',r'\uncertain{sous}-groupe','ss-groupe',
    'Two compact s forms stand before the hyphen. There are no intervening ou letters and no abbreviation stops. groupe begins after that written hyphen.',
    'p07',kind='abbreviation expanded or spelling modernised',category='Abbreviations expanded, spelling modernised',H_marked=True)
add('main line 16, argument in k before est',r'$k(\unsure{a|x})$',r'$k(x)$',r'$k(a)$',
    'Inside the two parentheses the argument has the same closed left bowl and short right return as the prose a and the exponent a. It differs from the open/crossing x read in the E subscript. The whole k(a) is present in the crop.',
    'p07',kind='misread symbol or index',category='Symbols and indices',consequential=True)
add('insertion above alg. on main line 16',r'\inserted{fini}',r'\add{fini}',r'\inserted{\uline{fini}}',
    'Two lower strokes are distinct. The upper short wavy stroke begins left of the f stem and runs below all of fini, ending beneath the last i. The lower continuous curved stroke reaches the gap before alg. and is the attachment leader. The f descender intersects the upper stroke but does not account for its independent left arm. The word itself is live and inserted, not struck.',
    'p13',vs_C=True,kind='drawing or diagram',category='Drawings and diagrams',
    scope='An observed underline omitted by both witnesses, not merely a change of macro syntax.')
add('main line 16, layered word before T-alpha',r'\unsure{par}','par',r'\deleted{\unsure{de}}\unsure{par}',
    'The long p-like descender and rightward r-like ending coexist with extra lower/upper strokes: a lower left bowl, a tall stem to its right, and a short low e-like return. Those extra strokes support a tentative overwritten de, but the layers cannot be isolated letter by letter. The current par is also left doubtful. The adjoining T has an alpha exponent and no infinity subscript.',
    'p12',confidence='low',vs_H=False,kind='other',category='Struck text',unresolved=True,
    scope='No settled C or H correction is counted from the newly proposed underlayer; both its reading and the current reading remain explicit doubts.')
add('main line 17, opening phrase',r"qu'on aura",r'qui \ill{} avec',r"qu'on aura",
    'The first word has the q descender, a high apostrophe and the joined on group. The next word starts with a closed a, continues through ur, and has a final a shape. It is aura, with no separate avec group after it.',
    'p14',kind='readable ink left as \\ill{}',category='Readable ink left as illegible',H_marked=True)
add('main line 17, phrase before de pouvoir','une chance','un choix','une chance',
    'The article contains the final e return. The following word has c, a tall looped h and the low ance continuation, without a final crossed x. The whole phrase reads une chance.',
    'p14')
add('main line 17, word at right end','pouvoir',r'\uncertain{paramètres}','pouvoir',
    'The word has a long p descender, a compact ou group, a v movement, a separate i dot and a short r ending. There is no tall t or long mètres ending. The complete upper part is visible in the p14 repair.',
    'p14',H_marked=True)
add('main line 18, opening verb','scinder',r'\uncertain{scindées}','scinder',
    'The word has the initial sc, dotted i, reduced n, a tall d, then a low e and short r return. It lacks an added accented é and terminal s group.',
    'p14',H_marked=True)
add('main line 18, phrase after scinder','sans trop de mal',r"\uncertain{sous l'effet} du modèle",'sans trop de mal',
    'The source has the short sans group, then a separate trop with a tall t and p descender, followed by de and the short mal ending in one l loop. There is no l’effet group, and mal does not contain the extra syllables of modèle.',
    'p14',H_marked=True)
add('lower oblique margin, four baselines', 'on le supposera du moins ici',r'on a \ill{} $W$ \uncertain{nécessaires} \ill{} ici',
    r'\margin{on le\newline supposera\newline du moins\newline ici}',
    'The rotated note has four baselines: on le, supposera, du moins, ici. The tall loop in le is a written l. The doubled descending p strokes within supposera can resemble a W but belong inside that word. du moins is a separate line, and the last line has two i dots around c.',
    'p09',kind='readable ink left as \\ill{}',category='Readable ink left as illegible',H_marked=True)
add('lower left edge, thin foliation',r'\margin{123}','[absent]',r'\margin{123}',
    'The thin figures are a long-stemmed 1, a curved 2 with basal foot, and a two-curved 3. They are separate from the main hand at the lower left. No author page number is written at the head.',
    'p10',kind='omission',category='Omissions')

byplace={row['place']:row for row in changes}
def mark(ident,decision,reading,place):
    ch=byplace[place]
    return {'id':ident,'cote':'149','scan':'124','decision':decision,'reading':reading,
            'evidence':ch['evidence'],'crop':ch['crop'],'bbox':ch['bbox'],'confidence':ch['confidence']}
decisions=[
    mark('M0135','first','a','main line 13, point after et si'),
    mark('M0136','first','aur.','main line 14, abbreviated future verb'),
    mark('M0137','first','a','main line 14, exponent argument in complete E expression'),
    mark('M0138','first','a','main line 16, argument in k before est'),
    mark('M0139','undecided',r'\unsure{par}','main line 16, layered word before T-alpha'),
]
unlisted=[{'place':'main line 16, possible overwritten word beneath par','C':'[absent]',
           'decision':'undecided','reading':r'\deleted{\unsure{de}}',
           'evidence':'A lower left bowl, taller stem and short e-like return suggest an earlier de beneath the current p/r-shaped strokes. The exact layer allocation is uncertain, and no letters are silently supplied as resolved.',
           'crop':G['p12']['file'],'bbox':G['p12']['bbox'],'confidence':'low',
           'reason_outside_decisions':'Newly proposed underlayer absent from marks.tsv; only the supplied M0135–M0139 IDs are used in decisions.'}]

inventory=[]
def item(kind,position,text,hand='his hand',**extra):
    row={'sheet_kind':'text','hand':hand,'element':f'e{len(inventory)+1:02d}',
         'kind':kind,'position':position,'first_words_or_objects':text,'transcribed':'yes'}
    row.update(extra)
    inventory.append(row)
item('text','main lines 1–7 through anneau jauge',"O' de O dans L-bar ... les interprétations")
item('text','main lines 7–12 from L’idée',"L'idée, c'est que prenant O de valuation ... codim")
item('margin note','left of main line 11',r'$T_\infty=T_\infty(\overline L)$',logical_lines=1)
item('text','main lines 13–18','et si a est de dim 0 ... Ceci donne-')
item('insertion','above alg. on main line 16','fini',logical_lines=1,decoration='one short wavy underline; separate lower curved leader attaches before alg.')
item('deletion','overwritten underlayer before T-alpha on main line 16',r'\unsure{de}',status='Tentative old word; layer reading remains uncertain.')
item('text','current layered word before T-alpha on main line 16',r'\unsure{par}',status='Current reading still uncertain.')
item('margin note','lower left beside the k(a) and fini clause','on le / supposera / du moins / ici',logical_lines=4)
item('margin note','lower-left foliation','123',hand='thin foliation hand, not assigned to author',logical_lines=1)

doubts=[
    {'place':'main line 16, current layered word before T-alpha','reading':r'\unsure{par}',
     'alternatives':'par remains provisional; no unsupported alternative word proposed','confidence':'low',
     'crop':G['p12']['file'],'bbox':G['p12']['bbox']},
    {'place':'main line 16, possible overwritten underlayer','reading':r'\deleted{\unsure{de}}',
     'alternatives':'de as an earlier overwritten word; exact old/current stroke allocation uncertain','confidence':'low',
     'crop':G['p12']['file'],'bbox':G['p12']['bbox']},
]

main_lines=[
    r"$O'$ de $O$ dans $\overline L$ i.e. $S'$ de $S$ dans $L$,",
    r"et pour $x'$ au dessus de $x$, un",
    r"groupe de décomposition $N_{x'}$, d'inertie",
    r"$I_{x'}$, ayant les interprétations",
    r"qu'on a signalé plus haut dans le",
    r"cas particulier d'un $O$ qui est un",
    r"anneau jauge. L'idée, c'est que",
    r'prenant $O$ de valuation (pas néc. une',
    r'jauge) $\supset K$, on trouve des',
    r"groupes d'inertie à structure simple ---",
    r'des $T_\infty^\alpha$ essentiellement, où $\alpha$ est la',
    r"``codim'' du $x\in\mathfrak X$ correspondant ---",
    r'et si $a$ est de dim $0$, on',
    r'aur. une extension de $\mathcal E_{k(x)}^{\overline{k(a)}}$ ---',
    r'ss-groupe ouvert de $\mathcal E_K$, puisque',
    r'$k(a)$ est alg. sur $K$ --- \deleted{\unsure{de}}\unsure{par} $T^\alpha$,',
    r"qu'on aura une chance de pouvoir",
    r'scinder sans trop de mal. Ceci donne-',
]
line_inventory=[{'label':f'main_{i:02d}','class':'main','reading':s} for i,s in enumerate(main_lines,1)]
for i,s in enumerate([r'$T_\infty=T_\infty(\overline L)$','on le','supposera','du moins','ici'],1):
    line_inventory.append({'label':f'margin_{i:02d}','class':'margin','reading':s})
line_inventory.append({'label':'insertion_01','class':'insertion','reading':r'\uline{fini}'})
line_inventory.append({'label':'number_01','class':'standalone_number','reading':'123'})

# Readings are manuscript transcription only. Broad boxes preserve complete context
# rather than describing clipped ascenders/descenders in English.
audit_boxes=[
    {'box':'b01','kind':'C/H word difference; symbol or decoration difference','bbox':[340,65,1640,200],
     'reading':main_lines[0]},
    {'box':'b02','kind':'C/H word difference; symbol or decoration difference','bbox':[320,210,1665,880],
     'reading':'\n'.join(main_lines[1:6])},
    {'box':'b03','kind':'insertion; deletion; margin note; handwritten number; doubtful formula; C/H word difference; less-than-high C departure',
     'bbox':[15,880,1665,2355],
     'reading':r"anneau jauge. "+valuation+'\n'+margin_formula+'\n'+inertia+'\n'+margin_note+'\n'+ending+'\n'+folio},
]

report={
    'page':PAGE,'scan':124,'reader':'reader_a','line_count':25,
    'line_count_detail':{'main':18,'margin':5,'insertion':1,'standalone_numbers':1},
    'line_inventory':line_inventory,'changes':changes,'decisions':decisions,
    'unlisted_doubt_decisions':unlisted,'inventory':inventory,'doubts':doubts,'audit_boxes':audit_boxes,
    'notes':[
        'The page continues a discussion of decomposition and inertia groups for valuation rings, then suggests simple inertia groups of T type and a possible splitting of an extension. It starts mid-sentence and ends with the written incomplete word donne-.',
        'No author page number is visible. The thin lower-left 123 is retained as foliation, not as an author mspage number.',
        'All four O occurrences on this page are plain, with no underline. The initial L is barred, while the final L in S-prime de S dans L is plain. This apparent mismatch is preserved; no closure bar is supplied from the intended construction.',
        'The point after et si and both upper/later k arguments are read a from their closed-bowl shape. The preceding x in x∈X and the lower argument of E are read x. The written E formula therefore has subscript k(x) and exponent bar(k(a)); the two arguments are not normalized to match.',
        'aur. is a written short form with a stop. Its expansion is kept in the abbreviations list only. The later aura is fully written and has a terminal a shape absent from aur.',
        'The main T expression and both T forms in the upper marginal identity have two-lobed infinity subscripts. The last T-alpha before the closing discussion is written without an infinity subscript; none is supplied.',
        'The stroke below signalé follows directly from its g descender and is not an independent underline. By contrast, fini has a distinct short wavy underline and a lower curved insertion leader; the two are represented separately by an underline on the inserted word and a placement note.',
        'The layer before the last T-alpha is retained as a tentative overwritten de followed by a tentative current par. The two readings remain doubtful, and M0139 is undecided. The new underlayer has no invented supplied-mark ID.',
        'The upper marginal equation sits beside the main T-infinity-alpha phrase. The four-line lower note sits beside the k(a)/fini clause. No separate long leader fixes a unique grammatical attachment for that note, so its proximity is recorded without inserting its words into the running sentence.',
        'Audit box b03 includes the full lower contextual block from anneau jauge to foliation 123. This includes both marginal notes, all a/x occurrences, the entire E formula, the inserted underlined fini, the layered de/par and the complete neighboring T-alpha. Its reading contains manuscript text and notation only.',
        'No proof verification, computation, external research or independent audit was undertaken in this first reading. The mathematical comments record the literal local forms and possible source mismatches only.',
    ],
    'checks':[],
    'hand_observations':[
        {'habit':'A plain O may have an upper right return that does not constitute an underline.',
         'places':'main line 1 twice, main line 6, main line 8','holds':'All four O occurrences here are plain.',
         'witness_errors':'H adds underlines at all four places; C preserves the plain forms.'},
        {'habit':'The a-like point form has a small closed left bowl with a right return; the x-like form is open/crossing.',
         'places':'prose a after et si; exponent k(a); later k(a); comparisons x∈X and E subscript k(x)',
         'holds':'All three questioned point forms are a locally; the two comparison x forms remain distinct.',
         'witness_errors':'C marks a|x; H reads x in all three questioned positions.'},
        {'habit':'A short future verb aur. ends with a detached stop; the fully written aura has an additional terminal a.',
         'places':'main lines 14 and 17','holds':'One abbreviation and one full form on this page.',
         'witness_errors':'C offers aur.|aura; H reads on a and dislocates the following formula.'},
        {'habit':'Long g descenders can sweep left below their words without creating underlining.',
         'places':'signalé on line 5 and jauge on line 7','holds':'Both strokes are continuous with their g loops.',
         'witness_errors':'No extra underline is added at these places.'},
        {'habit':'Two descending p strokes within a small marginal word can resemble a separate W.',
         'places':'supposera in the lower margin','holds':'One occurrence, read within the word and its four-line note.',
         'witness_errors':'H places a W-like object in its largely illegible marginal reading.'},
        {'habit':'An inserted word can carry its own short underline above a separate curved attachment stroke.',
         'places':'fini before alg.','holds':'The two strokes are separately visible in p13.',
         'witness_errors':'Both C and H omit the underline on inserted fini.'},
    ],
    'notation':[
        {'written':r"$O'$, $O$",'meaning_or_use':'Plain O forms used for the rings in the continuation; no underline is written on this page.','places':'main lines 1, 6, 8'},
        {'written':r"$S'$ de $S$ dans $L$",'meaning_or_use':'Literal plain final L, despite a barred L earlier on the same line.','places':'main line 1'},
        {'written':r"$N_{x'}$, $I_{x'}$",'meaning_or_use':'Decomposition and inertia labels named in the running text; both have the small x-prime index.','places':'main lines 3–4'},
        {'written':r'$T_\infty^\alpha$','meaning_or_use':'Groups described as essentially supplying simple inertia structure.','places':'main line 11'},
        {'written':r'$T_\infty=T_\infty(\overline L)$','meaning_or_use':'Written marginal identity with two infinity subscripts and a barred argument L.','places':'left margin beside main line 11'},
        {'written':r'$\mathcal E_{k(x)}^{\overline{k(a)}}$','meaning_or_use':'Literal extension-group expression with different lower and upper point letters; both are preserved.','places':'main line 14'},
        {'written':r'$a$, $k(a)$','meaning_or_use':'Point and field-argument forms actually written in the dimension-zero/finite-algebraic clause.','places':'main lines 13, 14 exponent, 16'},
        {'written':r'$T^\alpha$','meaning_or_use':'Final T expression has no written infinity subscript.','places':'main line 16'},
    ],
    'abbreviations':[
        {'written':'i.e.','expansion':'id est'},
        {'written':'néc.','expansion':'nécessairement'},
        {'written':'codim','expansion':'codimension'},
        {'written':'dim','expansion':'dimension'},
        {'written':'aur.','expansion':'aura'},
        {'written':'ss-','expansion':'sous-'},
        {'written':'alg.','expansion':'algébrique'},
    ],
    'inspection':{
        'whole':True,'halves':['top','bottom'],'crops':[g['file'] for g in G.values()],
        'crop_count':len(G),'deletions_insertions_checked':True,
        'source_dimensions':[1680,2364],'native_half_dimensions':[1680,1300],
        'crop_geometry_file':f'review/{PAGE}_crop_geometry.json','crop_script':f'review/{PAGE}_make_crops.py',
        'inspection_notes':[
            'The full page was inspected once for layout, then top.png and bottom.png each once at native resolution against C and H.',
            'All fourteen saved crops were visually inspected. No OCR, external research, PDF text extraction, other-page access or TeX compilation was used.',
            'p12 focuses the still-open layered de/par; p13 focuses the still-open lower strokes and attachment of fini. They were made before those places were decided.',
            'p02 clipped the bottom of the y descender in ayant. p11 is the single repair with that target complete. p08 touched/cut the upper boundary of pouvoir, and p07 clipped unrelated upper E_K/puisque context; p14 is the declared single lower-block repair completing those targets/context. These repairs are documented as incomplete-view repairs, not new independent evidence.',
            'Some focused crops retain fragments of adjoining lines at their edges. Blind-audit rectangles are broader complete contextual regions; their reading fields contain actual manuscript transcription, without English descriptions of clipped fragments.',
            'The independent audit has not begun; this is the first-reader candidate and evidence return only.',
        ]
    }
}

assert len(changes)==29
assert len(decisions)==5
assert {d['id'] for d in decisions}=={'M0135','M0136','M0137','M0138','M0139'}
assert sum(report['line_count_detail'].values())==report['line_count']==len(line_inventory)
assert len(G)==14 and len(doubts)==2
assert all((ROOT/'edition'/g['file']).is_file() for g in G.values())
(OUT/f'{PAGE}.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'page':PAGE,'lines':report['line_count'],'changes':len(changes),'decisions':len(decisions),
                  'crops':len(G),'remaining_doubts':len(doubts),'audit_boxes':len(audit_boxes)},ensure_ascii=False))
