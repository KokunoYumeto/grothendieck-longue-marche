"""Mechanical scan005 evidence assembly; every ink decision is supplied by root."""
from pathlib import Path
import json

OUT=Path(__file__).resolve().parents[1]
PACKET=OUT.parent/'packets'/'005'

def read_json(path):
    return json.loads(path.read_text())

reports={role:read_json(OUT/'readers'/'005'/role/'report.json') for role in 'ABC'}
rows={role:{d['id']:d for d in reports[role]['differences']} for role in 'ABC'}
texts={role:(OUT/'readers'/'005'/role/'reading.tex').read_text() for role in 'ABC'}
metadata=read_json(PACKET/'metadata.json')

def item(role,n):
    return rows[role][f'005.{role}.{n:02d}' if role in 'AB' else f'005-C-{n:02d}']

def ref(role,d):
    return f"{d['id']}: {d['reading']}"

def outcrop(role,path):
    return f"readers/005/{role}/{path}" if path else ''

# A,B,C report row numbers per manuscript locus. A missing report row is mapped
# explicitly to the relevant complete reading.tex span, without inventing a row.
slots=[
    ('Above the B of NB, line 1',None,None,1,'C'),
    ('Line 1, automorphisme',1,1,2,'A'),
    ('Detached dot below automorphisme, between lines 1 and 2',2,None,3,'A'),
    ('Line 3, after f superscript sigma est',3,2,4,'A'),
    ('Line 4, first opere after Aut(C)',4,3,5,'A'),
    ('Line 5, l\'ens before des',5,4,6,'B'),
    ('Line 5, spèciaux',6,5,7,'A'),
    ('Line 7, barred Q inside Aut',7,6,8,'A'),
    ('Below the right end of coeff. on line 8',8,7,None,'A'),
    ('Line 9, revient between Il and au',9,8,9,'A'),
    ('Line 9, au = de',10,9,10,'A'),
    ('Detached paired mark to the right of the final prose line',None,10,11,'B'),
    ('First isolated lower dark mark',11,11,12,'A'),
    ('Pale trace immediately right of the first lower mark',12,12,13,'A'),
    ('Second isolated lower dark mark at the right',13,13,14,'A'),
]
missing={
    (1,'A'):r'reading.tex (opening): \uline{NB}; no raised hook/dot token',
    (1,'B'):r'reading.tex (opening): \uline{NB}; no raised hook/dot token',
    (3,'B'):r'reading.tex (line 1): automorphisme; no detached point token below it',
    (9,'C'):r'reading.tex (line 8): les coeff. de; no detached lower trace token',
    (12,'A'):r'reading.tex (final prose and lower display): no paired-dot token at this position',
}
decisions=[]
for n,(location,ai,bi,ci,primary) in enumerate(slots,1):
    mapping=dict(zip('ABC',(ai,bi,ci)))
    primary_item=item(primary,mapping[primary])
    d={
        'id':f'005-{n:02d}', 'location':location,
        'C':primary_item.get('C'), 'H':primary_item.get('H'),
        'final':primary_item['reading'],
        'readers':{},
        'evidence':'PROVISIONAL '+primary+' reading; ROOT ADJUDICATION PENDING. '+primary+' reports: '+primary_item['evidence'],
        'crop':outcrop(primary,primary_item.get('readers_crop')),
        'confidence':primary_item['confidence'], 'kind':primary_item['kind'],
        'diff_C':primary_item['diff_C'], 'diff_H':primary_item['diff_H'],
        'C_doubt_status':primary_item.get('C_doubt_status'),
        'marked_in_H':'no',
        'source_map':{}, 'reader_bbox':{}, 'reader_crops':{},
    }
    for role,number in mapping.items():
        if number is None:
            d['readers'][role]=missing[(n,role)]
            d['source_map'][role]=[]
            continue
        x=item(role,number)
        d['readers'][role]=ref(role,x)
        d['source_map'][role]=[x['id']]
        d['reader_bbox'][role]=x.get('bbox')
        d['reader_crops'][role]=outcrop(role,x.get('readers_crop'))
    decisions.append(d)

byid={d['id']:d for d in decisions}
# Actual manuscript character omissions are represented by empty source strings.
for n in [3,9,12,14]:
    byid[f'005-{n:02d}']['C']=''
    byid[f'005-{n:02d}']['H']=''
for n in [13,15]:byid[f'005-{n:02d}']['H']=''
# H emphasis conversion is explained in checks/macro_correspondences.md and is
# not counted. The added upper trace remains a separate omission at 005-01.
byid['005-01']['C']=r'\uline{NB}'
byid['005-01']['H']=r'\emph{NB}'
# Root supplied counting convention: removal/resolution of an actual C doubt
# counts against C, independently of B's qualification-only flag.
for d in decisions:
    if d.get('C_doubt_status')=='resolved':d['diff_C']=True
# Root supplied: the differing primary ordinary Q is an uncertain H difference;
# H's double-stroked Q remains an explicit alternative.
byid['005-08']['diff_H']=True
byid['005-08']['kind']='misread symbol or index'
byid['005-08']['qualification']='The differing primary ordinary Q is recorded as an uncertain H difference; H\'s double-stroked Q remains an explicit alternative.'
byid['005-08']['evidence']+=' The final primary glyph and its retained alternative require root adjudication; H is among the alternatives.'
byid['005-04']['qualification']='The differing primary contracted reading is recorded as an uncertain H difference; H\'s également remains an explicit alternative.'
byid['005-06']['kind']='text not on the page'

# Direct root messages are the sole source of these adjudications. No image has
# been opened by this mechanical clerk.
ROOT_DECISIONS={
    '005-01':{
        'final':r'\overset{\hspace{0.55em}\unsure{?}}{\text{\uline{NB}}}',
        'confidence':'low','kind':'omission','diff_C':True,'diff_H':True,
        'evidence':'Root personally viewed this crop. A pale bent hook lies above a separate dark dot over the right side of NB. Retain the unsure question-mark shape; its function and hand remain uncertain.',
        'crop':'readers/005/C/01_nb_sigma.png',
    },
    '005-02':{
        'final':'automorphisme','confidence':'medium','kind':'other','diff_C':True,'diff_H':False,'C_doubt_status':'resolved',
        'evidence':'Root personally viewed this crop. The auto opening, descending p, tall h, dotted i and compressed final isme support automorphisme. Resolve the C doubt at medium confidence.',
        'crop':'readers/005/A/crops/01_automorphisme.png',
    },
    '005-03':{
        'final':r'\unsure{\cdot}','confidence':'low','kind':'omission','diff_C':True,'diff_H':True,
        'evidence':'Root personally viewed this crop. A detached round point is visible below automorphisme without a fixed textual function. Include the unsure dot reported by A and C.',
        'crop':'readers/005/A/crops/01_automorphisme.png',
    },
    '005-04':{
        'final':r'\unsure{égalmt|également}','confidence':'medium','kind':'abbreviation expanded or spelling modernised','diff_C':False,'diff_H':True,'C_doubt_status':'retained',
        'evidence':'Root personally viewed this crop. The abbreviated form is strongest, but the low run after l does not distinguish each intermediate letter. Retain égalmt/également; C-reader\'s resolution is not adopted.',
        'crop':'readers/005/A/crops/02_egalmt.png',
    },
    '005-05':{
        'final':'opere','confidence':'high','kind':'misread word','diff_C':True,'diff_H':True,'C_doubt_status':'resolved',
        'evidence':'Root personally viewed this crop. No detached accent stands above ere in the first opere. Resolve it as unaccented opere.',
        'crop':'readers/005/A/crops/03_autc_opere.png',
    },
    '005-07':{
        'final':'spèciaux','confidence':'high','kind':'misread word','diff_C':True,'diff_H':True,'C_doubt_status':'resolved',
        'evidence':'Root personally viewed this crop. The detached accent descends to the right. Resolve the word as spèciaux, retaining its written grave accent.',
        'crop':'readers/005/A/crops/04_speciaux.png',
    },
    '005-08':{
        'final':r'\unsure{\overline{\mathrm Q}|\overline{\mathbb Q}}','confidence':'medium','kind':'misread symbol or index','diff_C':False,'diff_H':True,'C_doubt_status':'retained',
        'evidence':'Root personally viewed this crop. A single upper oval and crowded or retraced lower-left and tail strokes leave ordinary versus double-stroked barred Q unresolved. Retain both candidates. The primary ordinary Q differs from H; H\'s double-stroked Q remains an explicit alternative.',
        'crop':'readers/005/A/crops/05_autq.png',
    },
    '005-09':{
        'final':r'\unsure{-|=}','confidence':'low','kind':'omission','diff_C':True,'diff_H':True,
        'evidence':'Root personally viewed this crop. A lower uneven horizontal trace is clear below and right of coeff.; upper traces are fragmented. Keep the dash as primary and B\'s equals candidate as an alternative. The mark\'s intention and origin remain uncertain.',
        'crop':'readers/005/B/crops/06_coeff.png',
    },
    '005-10':{
        'final':'revient','confidence':'medium','kind':'other','diff_C':True,'diff_H':False,'C_doubt_status':'resolved',
        'evidence':'Root personally viewed this crop. The connected opening, dotted i and terminal crossed t support revient. Resolve the C doubt at medium confidence.',
        'crop':'readers/005/A/crops/06_revient.png',
    },
    '005-11':{
        'final':r'au $=$ de','confidence':'high','kind':'misread symbol or index','diff_C':False,'diff_H':True,
        'evidence':'Root personally viewed this crop. Two separate horizontal bars stand between au and de. Retain the literal written equals sign.',
        'crop':'readers/005/A/crops/06_revient.png',
    },
    '005-12':{
        'final':r'\unsure{\cdot\,\cdot|-}','confidence':'low','kind':'omission','diff_C':True,'diff_H':True,
        'evidence':'Root personally viewed this crop. Two close points lie within a pale short trace to the right of the final prose line. Retain the paired-dot candidate and fragmented-dash alternative; no function or hand is assigned. Root will use the reported spatial TikZ layout for placement.',
        'crop':'readers/005/C/09_detached_mark.png',
    },
    '005-13':{
        'final':r'\unsure{-|=}','confidence':'low','kind':'omission','diff_C':False,'diff_H':True,'C_doubt_status':'retained',
        'evidence':'Root personally viewed this crop. The first lower mark has a dark uneven lower stroke and a faint broken upper trace. Retain dash/equals alternatives.',
        'crop':'readers/005/C/10_lower_left_marks.png',
    },
    '005-14':{
        'final':r'\unsure{\frown|-}','confidence':'low','kind':'omission','diff_C':True,'diff_H':True,
        'evidence':'Root personally viewed this crop. The adjacent pale trace has a visible shallow rise. Retain C-reader\'s arch candidate with the A/B dash alternative; intention and origin remain uncertain.',
        'crop':'readers/005/C/10_lower_left_marks.png',
    },
    '005-06':{
        'final':r"l'ens",'confidence':'high','kind':'text not on the page','diff_C':False,'diff_H':True,
        'evidence':'Root personally viewed this crop. The terminal hook of ens is followed by a clear gap before des, with no detached point. Retain l\'ens without a terminal point.',
        'crop':'crops/005/01_ens_punctuation.png',
    },
    '005-15':{
        'final':'-','confidence':'high','kind':'omission','diff_C':False,'diff_H':True,
        'evidence':'Root personally viewed this crop. The isolated right mark is a dark horizontal dash; no second continuous bar is visible.',
        'crop':'crops/005/02_lower_right_dash.png',
    },
}
for key,update in ROOT_DECISIONS.items():
    byid[key].update(update)
    byid[key]['root_decided']=True

# Doubts are generated from the provisional/current chosen reading, with their
# alternatives preserved explicitly. Root updates decide every marked locus.
doubt_specs=[
    ('005-01',['uninterpreted hook and detached dot']),
    ('005-03',['unassigned isolated point']),
    ('005-04',['également']),
    ('005-08',[r'\overline{\mathbb Q}']),
    ('005-09',['=','unassigned surface or transferred trace']),
    ('005-12',['-','unassigned mark']),
    ('005-13',['=']),
    ('005-14',['-','unassigned pale trace']),
]
doubts=[]
for key,alternatives in doubt_specs:
    d=byid[key]
    doubts.append({'location':d['location'],'reading':d['final'],'alternatives':alternatives,
                   'confidence':d['confidence'],'reason':d['evidence'],'crop':d['crop']})

# Every small reported object has its own inventory row. Their intention and
# attribution remain explicit; these are provisional until root checks page text.
inventory=[
    {'sheet_kind':'text','hand':'his hand','element':'005.01','kind':'text','position':'twelve physical lines in upper and middle sheet','first_words_or_objects':'NB Si sigma est un automorphisme ... de f est','transcribed':'yes'},
    {'sheet_kind':'text','hand':'his hand','element':'005.02','kind':'text','position':'upper left, directly beneath NB','first_words_or_objects':'single underline beneath NB','transcribed':'yes'},
    {'sheet_kind':'text','hand':'undetermined hand','element':'005.03','kind':'text','position':'above the B of NB','first_words_or_objects':'pale hook and detached dot; unsure question-mark shape','transcribed':'yes'},
    {'sheet_kind':'text','hand':'undetermined hand','element':'005.04','kind':'text','position':'below the middle of automorphisme','first_words_or_objects':'detached round point, function uncertain','transcribed':'yes'},
    {'sheet_kind':'text','hand':'undetermined hand','element':'005.05','kind':'text','position':'below the right end of coeff. on line 8','first_words_or_objects':'faint detached dash/equals candidate, intention uncertain','transcribed':'yes'},
    {'sheet_kind':'text','hand':'his hand','element':'005.06','kind':'text','position':'line 9, beneath nbs algébriques','first_words_or_objects':'single underline beneath nbs algébriques','transcribed':'yes'},
    {'sheet_kind':'text','hand':'undetermined hand','element':'005.07','kind':'drawing','position':'right of the final prose line, slightly above its baseline','first_words_or_objects':'paired tiny points / short fragmented rule, function uncertain','transcribed':'yes'},
    {'sheet_kind':'text','hand':'undetermined hand','element':'005.08','kind':'drawing','position':'lower area, first dark group','first_words_or_objects':'dark lower short rule with faint upper trace, unsure dash/equals','transcribed':'yes'},
    {'sheet_kind':'text','hand':'undetermined hand','element':'005.09','kind':'drawing','position':'immediately right of the first lower mark','first_words_or_objects':'pale shallow arch/dash candidate, intention uncertain','transcribed':'yes'},
    {'sheet_kind':'text','hand':'undetermined hand','element':'005.10','kind':'drawing','position':'lower area, right dark group','first_words_or_objects':'one short dark horizontal rule','transcribed':'yes'},
    {'sheet_kind':'text','hand':'another unnamed hand','element':'005.11','kind':'text','position':'bottom left sheet edge','first_words_or_objects':'archive numeral 4, comment only','transcribed':'yes'},
]

notes='''The NB asserts an Aut(C) action on the special f, acting through Aut of barred Q. It says the coefficients of P,Q in f=P/Q spécial are algebraic and writes “Il revient au = de dire” for the algebraicity of their zeros. The divisor sentence stops at est. These are the manuscript's assertions; no proof or calculation was performed in this reading. The paragraph occupies twelve physical lines. Archive numeral 4 is recorded in a comment; the readers report no title, date or authorial page number.

Four of seven C doubts are resolved: automorphisme, the first unaccented opere, spèciaux with a grave accent, and revient. Three remain: égalmt/également, ordinary/double-stroked barred Q, and the first lower dash/equals mark. The uncertainty at égalmt and barred Q retains H's reading as an alternative while recording the differing primary reading. The literal au = de sign and l'ens without a point are preserved.

Five newly retained mark groups remain uncertain in role and hand: the hook/dot above NB, the point below automorphisme, the lower trace at coeff., the tiny paired marks beside the final line and the pale arch beside the first lower mark. No secure authorial verbal doubt is present; the question-like shape above NB is not assigned an authorial function. The final text has eight unsure loci and one figure preserving the relative positions of four lower groups.

H's emphasis macros mark the same two word spans, NB and nbs algébriques. Its final note about the unfinished sentence is editorial apparatus. Those correspondences contribute no collation rows. All three readers report no mathematical proof or calculation, so CHECK_EVENTS receives no event for this page.'''

record={
    'scan':5,'folder':metadata['folder'],'their_page':int(metadata['their_page']),
    'hua_has':metadata['hua_has'],'filename':'J81-01_81_scan005.tex',
    'brief_version':'v04 (with supplied-preamble emphasis clarification)',
    'main_adjudicated':False,'decisions':decisions,'doubts':doubts,'inventory':inventory,
    'notes':notes,
    'abbreviations':[
        {'form':'NB','expansion':'nota bene'},
        {'form':'égalmt','expansion':'également'},
        {'form':'Aut','expansion':'automorphismes'},
        {'form':'ens','expansion':'ensemble'},
        {'form':'coeff.','expansion':'coefficients'},
        {'form':'nbs','expansion':'nombres'},
        {'form':'i.e.','expansion':'id est'},
    ],
    'check_events':[],
    'workflow_note':'Three independent fresh readers returned complete page readings, with 9, 10 and 10 targeted crops. All 40 report rows map to 15 local decisions. The mechanical clerk read no images. Root has supplied all fifteen ink decisions. The mechanical clerk checked all eleven inventory entries against root\'s final candidate page; main approval remains pending. Root personally viewed ten retained reader crops and made and viewed two additional crops. The supplied H emphasis convention was sent to each reader independently. No TeX compilation was performed.',
}

# Exhaustive source-row mapping and existing crop-path checks are mechanical.
coverage={role:[] for role in 'ABC'}
for d in decisions:
    for role,ids in d['source_map'].items():coverage[role].extend(ids)
for role in 'ABC':
    assert len(coverage[role])==len(set(coverage[role])),(role,'duplicate row mapping')
    assert set(coverage[role])==set(rows[role]),(role,'missing or invented report mapping')
for d in decisions:
    for crop in [d['crop'],*d['reader_crops'].values()]:
        assert not crop or (OUT/crop).is_file(),crop
(OUT/'checks'/'scan005_record_draft.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')

mapping=['# Scan 005 reader-to-decision mapping\n',
         'Mechanical assembly only. No image has been opened by the clerk. The root decides all ink readings.\n',
         '| Decision | Locus | A | B | C | Root status |',
         '| --- | --- | --- | --- | --- | --- |']
for d in decisions:
    cells=[d['id'],d['location'],*(', '.join(d['source_map'][role]) or 'reading.tex, no separate row' for role in 'ABC'), 'decided' if d.get('root_decided') else 'pending']
    mapping.append('| '+' | '.join(cells)+' |')
mapping+=['\n## Important divergences\n',
          '- égalmt: A/B retain égalmt/également; C removes the doubt. Root retains the alternatives.',
          '- NB hook/dot: C alone supplies the upper shape. Root retains an unsure question-mark candidate.',
          '- Point below automorphisme: A/C include it; B supplies no token. Root retains an unsure detached dot.',
          '- Below coeff.: A gives a doubtful dash, B gives =/−, C supplies no token. Root retains dash/equals, dash primary.',
          '- Right of final prose line: B gives paired dots, C paired dots/dash, A supplies no token. Root retains paired dots/dash with spatial placement.',
          '- Pale lower trace: A/B give doubtful dash, C gives shallow arch/dash. Root retains shallow arch/dash.',
          '- H barred Q: all retain ordinary/double-stroked alternatives. Per root, the differing primary ordinary Q is an uncertain H difference; H remains an alternative.',
          '\n## Excluded representation/apparatus\n',
          '- H emph versus uline marks the same two emphasized spans. No macro-only collation row.',
          '- H note describing the unfinished sentence is editorial apparatus, not manuscript text.',
          '- Quote-character encoding, en/em dash TeX encoding, Aut operator macros, and separated math-mode P,Q punctuation encode the same reported readings; no independent row.',
          '\n## Inventory\n',
          'Eleven entries checked against root\'s final page candidate cover the paragraph, both underlines, five extra small mark groups, two lower dark groups and the archive numeral. The small trace entries deliberately leave attribution unresolved. All eleven entries are represented in the final candidate. Main approval remains pending.',
          '\n## Checks\n',
          'A: 13 rows; B: 13 rows; C: 14 rows. Each maps exactly once. All cited crop files exist. All three check_events arrays are empty.']
(OUT/'checks'/'scan005_mapping.md').write_text('\n'.join(mapping)+'\n')
print(json.dumps({'decisions':len(decisions),'mapped_report_rows':{r:len(coverage[r]) for r in 'ABC'},'root_decided':len(ROOT_DECISIONS),'remaining_root':sum(not d.get('root_decided') for d in decisions),'doubts':len(doubts),'inventory':len(inventory)},ensure_ascii=False))
