"""Mechanical assembly of root's recorded scan 003 decisions; no image reads."""
from pathlib import Path
from copy import deepcopy
import json
import re

R = Path(__file__).resolve().parents[1]
reports = {role: json.loads((R / 'readers/003' / role / 'report.json').read_text()) for role in 'ABC'}
rows = {role: {d['id']: d for d in report['differences']} for role, report in reports.items()}
texts = {role: (R / 'readers/003' / role / 'reading.tex').read_text() for role in 'ABC'}
metadata = json.loads((R.parent / 'packets/003/metadata.json').read_text())

B_MAP = {
    1:[1],2:[2],3:[3],4:[4],5:[5],6:[6],7:[7],8:[8],9:[9,10,11],
    10:[12],11:[13],12:[14],13:[15],14:[16],15:[17],16:[18],17:[19],18:[20],19:[21],
    20:[22],21:[23],22:[24],23:[25],24:[26],25:[27,28,29],26:[],27:[30],28:[31],29:[32],
    30:[36],31:[37],32:[38],33:[39],34:[41],35:[42],36:[43],37:[44],38:[44],39:[45],
    40:[46],41:[47],42:[48],43:[49],44:[50],45:[51],46:[52],47:[53],48:[54],49:[55],
    50:[56],51:[57,58],52:[59],53:[60,62],54:[61],55:[63],56:[64,65],57:[66],58:[67,69],59:[68],60:[71],
}
C_MAP = {
    1:[1],2:[2],3:[4],4:[5],5:[6],6:[7],7:[8],8:[9],9:[10],
    10:[11],11:[12],12:[13],13:[14],14:[15],15:[16],16:[17],17:[18],18:[19],19:[20],
    20:[21],21:[22],22:[23],23:[24],24:[25],25:[27,28],26:[],27:[26],28:[29],29:[30],
    30:[31],31:[32],32:[34],33:[35],34:[37],35:[],36:[38],37:[39],38:[39],39:[40],
    40:[41],41:[42],42:[43],43:[44],44:[45],45:[46],46:[48],47:[47],48:[49],49:[50],
    50:[51],51:[52,53],52:[54],53:[55],54:[56],55:[55,60],56:[57],57:[58],58:[59],59:[59],60:[3],
}

def source_readings(role, ids):
    prefix = 'B003-' if role == 'B' else 'D'
    return '; '.join(f"{prefix}{n:02d}: {rows[role][f'{prefix}{n:02d}']['reading']}" for n in ids)

crop = {
    1:'readers/003/A/01_title_insertion.png',2:'readers/003/A/02_title_ending.png',
    3:'readers/003/A/03_morphism.png',4:'readers/003/A/03_morphism.png',5:'readers/003/A/03_morphism.png',
    6:'readers/003/A/03_morphism.png',7:'readers/003/A/03_morphism.png',8:'crops/003/01_etale_phrase.png',
    9:'crops/003/02_singular_opening.png',10:'readers/003/A/04_f0_overwrite.png',
    **{n:'readers/003/C/05_critical_conditions.png' for n in range(11,17)},
    17:'readers/003/A/06_ramification.png',18:'crops/003/03_couple_insertion.png',19:'crops/003/03_couple_insertion.png',
    20:'readers/003/A/07_polynomials.png',21:'readers/003/A/07_polynomials.png',22:'crops/003/04_polynomial_comma.png',
    23:'readers/003/A/08_resp.png',24:'readers/003/A/19_degree_punctuation.png',
    25:'readers/003/B/07_oblique_note.png',26:'readers/003/B/07_oblique_note.png',
    27:'crops/003/05_normalises_restated_condition.png',28:'crops/003/05_normalises_restated_condition.png',
    29:'readers/003/A/10_fraction_cancellation.png',30:'crops/003/06_NB_insertion_anchor.png',
    31:'readers/003/C/19_nb_insertion_punctuation.png',32:'crops/003/06_NB_insertion_anchor.png',
    33:'readers/003/A/11_deleted_word.png',34:'crops/003/07_underlined_si.png',
    35:'readers/003/A/13_question_insertion.png',36:'readers/003/A/12_question_parenthesis.png',
    **{n:'readers/003/A/13_question_insertion.png' for n in range(37,40)},
    **{n:'readers/003/A/14_struck_start.png' for n in range(40,43)},
    43:'readers/003/A/15_cond_abbreviation.png',44:'readers/003/C/14_degree_and_factor.png',
    45:'readers/003/C/14_degree_and_factor.png',46:'readers/003/A/16_TP0.png',
    47:'readers/003/C/14_degree_and_factor.png',48:'crops/003/08_last_insertion_anchor.png',
    49:'readers/003/C/15_example_ending.png',50:'readers/003/C/15_example_ending.png',
    **{n:'readers/003/A/17_sideways_note.png' for n in range(51,56)},
    **{n:'readers/003/C/17_sideways_continuation.png' for n in range(56,60)},
    60:'crops/003/10_separator_one.png',
}

decisions = {}
for n in range(1,61):
    a = rows['A'][f'A{n:02d}']
    d = {k:deepcopy(a[k]) for k in ['location','C','H','confidence','kind','diff_C','diff_H','C_doubt_status']}
    d['id'] = f'003-{n:02d}'
    d['final'] = a['reading']
    d['readers'] = {'A':f"A{n:02d}: {a['reading']}", 'B':source_readings('B',B_MAP[n]), 'C':source_readings('C',C_MAP[n])}
    d['evidence'] = f"Root crop adjudication recorded at checks/scan003_main_decisions.md, A{n:02d}: " + a['evidence']
    d['crop'] = crop[n]
    d['marked_in_H'] = 'yes' if '\\ill{' in (d['H'] or '') or '\\uncertain{' in (d['H'] or '') else 'no'
    if 'mathematical_consequence' in a:
        d['mathematical_consequence'] = a['mathematical_consequence']
    decisions[n] = d

def update(n, **kwargs):
    decisions[n].update(kwargs)

update(2, evidence="Root retained plural first and singular as a supported alternative. The trailing curl favours the plural, but the compressed terminal does not settle it. A02 and D02 put plural first; B003-02 puts singular first. Same-word doubt status alone supplies no H collation difference.")
update(3, final=r'\unsure{morphisme|morphismes}', confidence='low', C_doubt_status='retained',
       evidence="Root retained both readings: the compressed terminal stroke does not securely isolate the ending. A03 resolves morphisme; B003-03 and D04 retain morphisme/morphismes.")
update(4, final=r'\overset{f}{\unsure{-|\longrightarrow}}', diff_C=False, diff_H=True,
       evidence="Root retained the short horizontal stroke first. Right-end thickening does not establish two arrowhead legs. A04 puts the arrow first; B003-04 and D05 put the stroke first. The final reading matches witness C.")
update(6, C="``\\unsure{spécial}''")
update(16, final=r'$\}$',
       evidence="Root read the final right brace separately from the doubtful cancelled interior in reader C’s critical-conditions crop. The tall, doubly curved closing stroke remains live; the cancellation crosses the interior and stops before this brace.")
update(25, evidence="Root used reader B’s complete oblique-note crop. The note begins On and includes par Q(0)=1, ou P unitaire, ou Q unitaire. The terminal cel/cela remains doubtful. A25, B003-27–29 and D27–28 preserve these readings.")
decisions[26]['readers']['B'] = 'reading.tex: the slanted margin note is placed between the degree-condition parenthesis and normalisés; report.json has no separate placement row.'
decisions[26]['readers']['C'] = 'reading.tex comment: slanted, left margin beside the degree and normalization lines.'
update(30, C='Inserted after donc si, before cette quantité', H='Placed before donc si cette quantité',
       final='Inserted after donc si, before cette quantité',
       evidence="Root read the guide in root crop 06: the nonzero insertion attaches after donc si and before cette. This row records placement; the internal semicolon and trailing comma have separate rows.")
decisions[30]['readers'] = {
    'A':'A30: insertion after si and before cette (placement; punctuation recorded separately).',
    'B':'B003-36: insertion after donc si and before cette quantité (placement; punctuation recorded separately).',
    'C':source_readings('C',[31]),
}
update(35, H=r'$P(z)=Q(z)$ \add{donc $P\prime(z)=Q\prime(z)$}. Mais',
       final=r'$P(z)=Q(z)$ !',
       evidence="Root read a pale vertical shaft above a detached dark dot immediately after Q(z), supporting an exclamation mark. A35 reads !; B003-42 retains !/period; reader C’s reading.tex retains a period. The misplaced equality insertion has its own wording and placement rows.")
decisions[35]['readers']['C'] = r"reading.tex: $P(z)=Q(z)$. Mais; no separate report row for this mark."
update(40, location='Struck preliminary line: verb', C=r'\deleted{\unsure{Réfléchissons}}',
       H=r'\struck{Prenons}', final=r'\deleted{\unsure{Réfléchissons}}', diff_C=False,
       evidence="Root retained the doubtful cancelled word Réfléchissons. The initial capital and tall internal stems support that candidate; the cancellation crosses the compact middle. This row covers the verb alone; the proposed à is treated separately.")
decisions[40]['readers']['A'] = r'A40 / reading.tex, verb only: \deleted{\unsure{Réfléchissons}}'
update(41, C=r'\deleted{\unsure{à}}', H='No separate à', final='No separate à',
       evidence="Root adopted A41: the cancellation line crosses an otherwise blank gap before Q. A41 omits a separate à; B003-47 and D42 retain the doubtful particle. The final transcription removes it.")
update(43, evidence="Root adopted A43 at medium confidence: a d ascender is followed by a second tall t stroke, and ions runs along the baseline. A43 reads conditions; B003-49 retains doubtful cond with raised ns; D44 resolves that abbreviation. The main text has conditions.")
update(46, final=r'\unsure{T}P_0(T)', confidence='medium', diff_C=False, diff_H=False, C_doubt_status='retained',
       evidence="Root retained the doubtful T before P_0(T), following witness C and D48. Reinforcement of the top bar and upright prevents certainty. A46 and B003-52 resolve T. The same T with a retained doubt supplies no H collation difference.")
update(47, final=r'Single reinforced live $P(T)=\unsure{T}P_0(T)$',
       evidence="Root read one reinforced live P(T)= in reader C’s degree-and-factor crop. A separately cancelled duplicate P(T)= is absent. The following factor retains its own doubt in the separate factor row.")
update(49, marked_in_H='yes', diff_H=False,
       evidence="Root read certes in reader C’s bottom-example crop. A49, B003-55 and D50 all read certes. H carries the same word with a doubt mark; removal of that mark alone is excluded from H collation counts.")
update(51, evidence="Root adopted the derivative followed by qui est nul, inserted (supposons a nonzero), and pour z from A’s sideways crop. Root also viewed crops/003/09_sideways_supposons.png to include the top strokes of supposons that the earlier strip clipped. Both crop paths were recorded by root; this row keeps the written wording and insertion position.")
update(52, final=r'\deleted{\unsure{sera}}', confidence='low', diff_C=False, C_doubt_status='retained',
       evidence="Root retained doubtful cancelled sera. The latter letters lie beneath a heavy cancellation. A52 resolves sera; B003-59 and D54 retain the doubt, as does witness C.")
update(53, C=r'\ne\left\{\begin{smallmatrix}0\\-\frac{b}{a}\end{smallmatrix}\right.',
       final=r'\ne\left\{\begin{smallmatrix}0\\-\frac{b}{a}\end{smallmatrix}\right.',
       evidence="Root retained the inequality, left brace and stacked 0 and -b/a in A’s sideways crop. The written brace has no closing counterpart. The following les deux zéros de P, si b nonzero and et are preserved in the continuation; the black cancelled word has its own row.")
update(55, evidence="Root retained les deux zéros de P si b nonzero, et before the value calculation. A55 and B003-63 record the placement; D55 and D60 jointly record the zero description, b condition and connective. H places b nonzero later in its parenthesis.")
update(56, evidence="Root retained doubtful cancelled peut être in reader C’s sideways-continuation crop. Cancellation and crossing main-text strokes obscure portions of the phrase; the live wording qui ... est non-equal to 1 remains in the transcription.")
update(57, evidence="Root retained doubtful cancelled en prenant in reader C’s sideways-continuation crop. The long cancellation and crossing main-text strokes obscure parts of the phrase. The proposed cancelled wording is preserved with doubt.")
update(58, final=r'si $b^2\ne-4a$',
       evidence="Root retained the final si followed by b with raised 2, the inequality sign, minus, 4 and a in reader C’s continuation crop. The preceding live wording and cancellations are separately retained. A58 and B003-67 supply the condition; B003-69 explicitly rejects the added prenons une valeur phrase; D59 includes the condition and terminal dash.")
update(59, C=r'\unsure{---}.', H=r'\ill{} (terminal portion of the sideways note)', final='--- (dash; no terminal full stop)', confidence='high', diff_C=True,
       C_doubt_status='resolved',
       evidence="Root resolved the detached trailing stroke as a plain dash and removed the following full stop, using reader C’s continuation crop. A59 and A’s reading.tex retain a doubtful dash followed by a period. B003-68 and the current B reading.tex agree on a dash without a period; D59 and C’s reading.tex also agree on that ending.")
decisions[59]['readers']['A'] = r'A59: \unsure{---}; reading.tex: \unsure{---}.'
decisions[59]['readers']['B'] += r'; current reading.tex: $---} (no period).'
decisions[59]['readers']['C'] += r'; reading.tex: $---} (no period).'

# H uncertainty markers are recorded at the relevant transcribed locus, including
# unreadable placeholders. Editorial notes are never added as manuscript rows.
for n in [15,16,25,33,38,39,49,57,58,59]:
    decisions[n]['marked_in_H'] = 'yes'
decisions[11]['marked_in_H'] = 'yes'

singular = []
for suffix, location, c, h, b_id in [
    ('a','Rational-function paragraph: opening nouns','fonction rationnelle','fonctions rationnelles',9),
    ('b','Rational-function paragraph: first telle','telle que','telles que',10),
    ('c','Rational-function paragraph: second telle','et telle que','et telles que',11),
]:
    d=deepcopy(decisions[9])
    d.update(id=f'003-09{suffix}',location=location,C=c,H=h,final=c)
    d['readers']={'A':f'A09 / reading.tex, this locus: {c}', 'B':source_readings('B',[b_id]), 'C':f'D10 / reading.tex, this locus: {c}'}
    d['evidence']=f'Root crop 02 records singular {c} at this locus. A09, the corresponding B003-{b_id:02d} row, and D10 preserve that singular wording.'
    singular.append(d)

trailing_comma = {
    'id':'003-31b', 'location':'NB nonzero insertion: trailing punctuation',
    'C':r'pour $P(z);Q(z)\ne0$,', 'H':r'pour $P(z),Q(z)\neq0$,',
    'final':r'pour $P(z);Q(z)\ne0$',
    'readers':{
        'A':r'A30 / reading.tex: \inserted{pour $P(z);Q(z)\ne0$,}',
        'B':r'B003-36 / reading.tex: \inserted{pour $P(z);Q(z)\ne0$,}',
        'C':source_readings('C',[33]),
    },
    'evidence':'Root found no isolated comma after the zero in reader C’s insertion-punctuation crop. The lower curve belongs to the insertion guide. A and B retain a comma; reader C omits it. Witnesses C and H both print the comma. Placement and the P/Q separator have separate rows.',
    'crop':'readers/003/C/19_nb_insertion_punctuation.png', 'confidence':'high', 'kind':'other',
    'diff_C':True, 'diff_H':True, 'C_doubt_status':None, 'marked_in_H':'no',
}
second_ie = {
    'id':'003-33b', 'location':'NB sentence: i.e after the cancelled au/ou',
    'C':'i.e', 'H':'i.e.', 'final':'i.e',
    'readers':{'A':'reading.tex: i.e (no separate A report row).','B':source_readings('B',[40]),'C':source_readings('C',[36])},
    'evidence':'Root retained i.e with no terminal period in A’s cancelled-word crop. B003-40 and D36 explicitly report the missing terminal dot; A’s reading.tex likewise has i.e. This is separate from the preceding doubtful cancelled word.',
    'crop':'readers/003/A/11_deleted_word.png', 'confidence':'medium', 'kind':'other',
    'diff_C':False, 'diff_H':True, 'C_doubt_status':None, 'marked_in_H':'no',
}
separators=[]
for suffix, ordinal, root_crop in [('a','First','10_separator_one.png'),('b','Second','11_separator_two.png'),('c','Third','12_separator_three.png')]:
    d=deepcopy(decisions[60])
    d.update(id=f'003-60{suffix}', location=f'{ordinal} vertical block separator',crop=f'crops/003/{root_crop}')
    d['evidence']=f'Root viewed the {ordinal.lower()} separator separately: a wavy upright stroke on the left and a straight upright stroke on the right. The rotated sign is retained as in witness C; H prints it horizontally.'
    d['readers']={'A':r'A60: \rotatebox{90}{$\simeq$} at all three block separators.', 'B':source_readings('B',[71]), 'C':source_readings('C',[3])}
    separators.append(d)

assembled=[]
for n in range(1,61):
    if n == 9:
        assembled.extend(singular)
    elif n == 60:
        assembled.extend(separators)
    else:
        assembled.append(decisions[n])
    if n == 31:
        assembled.append(trailing_comma)
    if n == 33:
        assembled.append(second_ie)

remaining = [
    (2,'isotopiques',['isotopique']),
    (3,'morphisme',['morphismes']),
    (4,'horizontal stroke',['right arrow']),
    (10,'cancelled 1 behind live 0',[]),
    (15,r'cancelled $\{0,1,\infty$',[]),
    (25,'au lieu de cel',['au lieu de cela']),
    (33,'cancelled au',['cancelled ou']),
    (39,'right brace',['right parenthesis']),
    (40,'cancelled Réfléchissons',[]),
    (46,'T before P_0(T)',[]),
    (52,'cancelled sera',[]),
    (54,'one physically unreadable cancelled word',[]),
    (56,'cancelled peut être',[]),
    (57,'cancelled en prenant',[]),
]
doubts=[]
for n,reading,alternatives in remaining:
    d=decisions[n]
    doubts.append({'location':d['location'],'reading':reading,'alternatives':alternatives,'confidence':d['confidence'],'reason':d['evidence'],'crop':d['crop']})

inventory = deepcopy(reports['C']['inventory'])
for item in inventory:
    if item['element'] == 'Underlining of si':
        item['kind']='text'
        item['first_words_or_objects']='si, with underlining'
    if item['element'] == 'Cancelled initial attempt':
        item['first_words_or_objects']='Réfléchissons Q(T)='
inventory.sort(key=lambda item:int(re.search(r'y(\d+)',item['position']).group(1)))

notes = r'''Scan 003 corresponds to H page 2. Its heading is “Carte sphérique (orientée) avec repère (dans cat. isotopiques|isotopique)”. Three upright separators connect the heading, the morphism description, the rational-function description and the polynomial-pair description. The page includes values at 0, 1 and infinity, first- and second-derivative restrictions, normalization alternatives in an oblique margin note, a bracketed NB calculation, and a quadratic example continued sideways in the left margin. No written date or manuscript page number is established. The archive sheet numeral is 2; it is kept as a comment. There are two margin notes and no drawing or diagram.

The author asks “Mais peut-on avoir” $P'(z)=0$ with the parenthetic “d'où aussi” $Q'(z)=0$, the inserted “avec” $P'(z)=Q'(z)$ and the unresolved closing hook, followed by “sans avoir” $P(z)=Q(z)$ and a question mark. The later text asks whether “on peut avoir”, with inserted “(pour” $P(z)\ne0$ “)”, $P'(z)=0$ “sans avoir” $P(z)=1$, and continues “certes oui p.ex.” The crossed trial $P(T)=T^2$ and the written example $P(T)=T(aT+b)=aT^2+bT$, $a+b=1$, are preserved, together with the sideways insertion “(supposons” $a\ne0$ “)”. These questions and qualifications are the author's wording.

The written round delimiters in $\mathbb C(z)$ are preserved beside “polynômes”. The derivative signs and both NB right-hand sides remain as transcribed. Root's recorded algebra checks at 2026-11-20 09:02:50 UTC give residual 0 for both NB expansions, the quadratic derivative, and the rational critical-value identity; see checks/scan003_algebra.md and scripts/check_scan003_algebra.py. In explicit expansions, $Q(P'-P)+P(Q-Q')=QP'-QP+PQ-PQ'=QP'-PQ'$ and $(Q-P)P'+P(P'-Q')=QP'-PP'+PP'-PQ'=QP'-PQ'$. Formal differentiation of $aT^2+bT$ gives $2aT+b$, and the recorded rational substitution gives $-b^2/(4a)$. The cancelled NB expression and its replacement are both retained. These computations settle the recorded identities; root's crop decisions govern the reading.

Reader A reports direct symbolic expansion and formal differentiation/substitution; reader C reports manual algebraic expansion and rational-expression multiplication. Reader B reports no mathematical check. Their exact check timestamps were not recorded. H's explanatory notes are kept as witness apparatus in the source files; their prose generates no manuscript collation rows. Same-word doubt removal, including certes, generates no H difference. Fourteen ink doubts remain in this record; conditions, the removed à, supposons and the final dash are settled by root's recorded decisions.'''

who = lambda run: f'GPT-6 Astra Pro; effort inherited, separately verifiable setting not exposed; run {run}'
check_events=[]
for statement_id, outcome in [
    ('003-NB-live',r'SymPy expansion of (Q-P)Pprime+P(Pprime-Qprime)-(QPprime-PQprime) returned residual 0.'),
    ('003-NB-struck',r'SymPy expansion of Q(Pprime-P)+P(Q-Qprime)-(QPprime-PQprime) returned residual 0; cancellation state was preserved.'),
    ('003-margin-derivative',r'SymPy formal differentiation of a*T^2+b*T minus (2*a*T+b) returned residual 0.'),
    ('003-margin-critical-value',r'SymPy rational simplification of (a*T^2+b*T) at T=-b/(2*a), plus b^2/(4*a), returned residual 0.'),
]:
    check_events.append({'statement_id':statement_id,'date':'2026-11-20 09:02:50 UTC','who':who('/root'),'type':'computation or formal certificate','outcome':outcome+' Source: checks/scan003_algebra.md and scripts/check_scan003_algebra.py.'})
for role, ids in [('A',['003-NB-live + 003-NB-struck','003-margin-derivative + 003-margin-critical-value']),('C',['003-NB-live + 003-NB-struck','003-margin-critical-value'])]:
    for index, event in enumerate(reports[role]['check_events']):
        check_events.append({
            'statement_id':ids[index], 'date':'2026-11-20', 'who':who('/root/scan003_'+role.lower()),
            'type':'computation or formal certificate',
            'outcome':f"Reported {event['type']} at {event['location']}: {event['result']} Exact check time was not recorded. Source: readers/003/{role}/report.json, check_events[{index}].",
        })

record={
    'scan':3,'folder':metadata['folder'],'their_page':int(metadata['their_page']),'hua_has':metadata['hua_has'],
    'filename':'J81-01_81_scan003.tex','brief_version':'v02','main_adjudicated':False,
    'decisions':assembled,'doubts':doubts,'inventory':inventory,'notes':notes,
    'abbreviations':[
        {'form':'cat.','expansion':'catégorie'},
        {'form':'i.e / i.e.','expansion':'id est'},
        {'form':r'resp\textsuperscript{t}','expansion':'respectivement'},
        {'form':'NB','expansion':'nota bene'},
        {'form':'p.ex.','expansion':'par exemple'},
        {'form':r'\deg','expansion':'degré'},
    ],
    'check_events':check_events,
    'workflow_note':"Three independent readers used brief v02 and each reports one whole-page view and one view of each supplied half. Their retained targeted crop counts are A 19, B 17 and C-reader 19. Root compared the returns and viewed targeted crops, including twelve root crops, without opening the whole scan or supplied halves. The first attempted display of four root crops was truncated before inspection; root subsequently viewed them successfully. No settled locus was recropped. A’s 60-row report supplies the backbone; the rational-function wording and three separators are each split into three loci, with separate new rows for the NB trailing comma and the second i.e terminal period. Root overrides and all three actual reader readings are recorded, including disagreements on morphisme(s), the joining stroke, the question punctuation, the proposed à, conditions, the factor T and cancelled sera. The current B report and TeX agree on a final dash without a period. The fine-grained C-reader inventory is sorted by full-page starting y coordinate with its original positions retained; its underlining uses kind text and its cancelled-line summary follows the removed à. H editorial prose and same-word H doubt removal generate no collation rows. Model: GPT-6 Astra Pro throughout; effort is inherited and not separately exposed. Mechanical assembly was performed by /root/record003 from the recorded decisions without viewing images or making ink decisions. This is a draft for root review; main_adjudicated remains false. Next-page brief feedback concerns complete slanted/sideways crop extents, H apparatus, report/TeX punctuation consistency, and continued logging of every witness C doubt.",
}

required={'id','location','C','H','final','readers','evidence','crop','confidence','kind','diff_C','diff_H','C_doubt_status','marked_in_H'}
kind_enum={'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised',r'readable ink left as \ill{}','drawing or diagram','other'}
inventory_enum={'text','display','diagram','drawing','margin note','insertion','deletion'}
assert len(assembled)==66
assert len({d['id'] for d in assembled})==66
assert len(doubts)==14
assert len([d for d in assembled if d['C_doubt_status']=='retained'])==14
assert len(inventory)==50
for d in assembled:
    assert required <= set(d), d['id']
    assert d['kind'] in kind_enum, d['id']
    assert set(d['readers'])==set('ABC') and all(d['readers'].values()), d['id']
    assert (R/d['crop']).is_file(),d['crop']
for d in doubts:
    assert (R/d['crop']).is_file(),d['crop']
for item in inventory:
    assert item['kind'] in inventory_enum,item['element']
    assert item['transcribed']=='yes',item['element']
assert (R/'crops/003/09_sideways_supposons.png').is_file()
target=R/'checks/scan003_record_draft.json'
target.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'draft':str(target),'decisions':len(assembled),'diff_C':sum(d['diff_C'] for d in assembled),'diff_H':sum(d['diff_H'] for d in assembled),'remaining_doubts':len(doubts),'inventory_rows':len(inventory),'check_events':len(check_events)},ensure_ascii=False))
