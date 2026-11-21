#!/usr/bin/env python3
"""Exact scan020 source correspondence; root alone supplies ink and counts."""
from pathlib import Path
import copy
import hashlib
import json
import re
import sys
sys.dont_write_bytecode=True
from scan020_prepare_sources import span, object_at

BASE=Path('/workspace/scratch/94548b74fbe0')
OUT=BASE/'out/checks'
U=json.loads((OUT/'scan020_source_union.json').read_text())
assert U['released_readers']==list('ABC')
T={r:(BASE/f'out/readers/020/{r}/reading.tex').read_text() for r in 'ABC'}
R={r:json.loads((BASE/f'out/readers/020/{r}/report.json').read_text()) for r in 'ABC'}


def source(r,literal,occurrence=0,within=None):
    text=T[r]
    start,end=(0,len(text)) if within is None else (SCOPES[r][within]['char_start'],SCOPES[r][within]['char_end'])
    matches=list(re.finditer(re.escape(literal),text[start:end]))
    assert len(matches)>occurrence,(r,within,literal,occurrence)
    at=start+matches[occurrence].start()
    return span(f'out/readers/020/{r}/reading.tex',text,at,at+len(literal))


def obj(r,pointer):
    return dict(value=copy.deepcopy(object_at(R[r],pointer)),
        source=copy.deepcopy(U['reader_sources'][r]['report_json_pointer_index'][pointer]))


SCOPES={}
for r,text in T.items():
    displays=list(re.finditer(r'\\\[(.*?)\\\]',text,re.S))
    assert len(displays)==2,r
    lemma=text.index(r'\uline{Lemme}')
    formula=text.index('est de la forme',lemma)+len('est de la forme')
    insert=text.index('où $K$ est une',formula)
    margin=text.index('% slanted',insert)
    membership=text.index(r'$\forall\alpha\in K$',margin)
    final=text.index('tels que',membership)
    archive=text.index('% archive sheet number: 19')
    head=text.index('\n')+1
    bounds=[('header',0,head),('opening',head,displays[0].start()),
        ('paired',displays[0].start(),displays[0].end()),
        ('upper',displays[0].end(),displays[1].start()),
        ('nonempty',displays[1].start(),displays[1].end()),
        ('count',displays[1].end(),lemma),('lemma_heading',lemma,formula),
        ('lemma_formula',formula,insert),('lemma_insertion',insert,margin),
        ('margin',margin,membership),('membership',membership,final),
        ('final',final,archive),('archive',archive,len(text))]
    assert ''.join(text[a:b] for _,a,b in bounds)==text
    SCOPES[r]={key:span(f'out/readers/020/{r}/reading.tex',text,a,b) for key,a,b in bounds}


def choice(r,literal=None,description=None,scope=None,occurrence=0):
    ptr=source(r,literal,occurrence,scope) if literal is not None else copy.deepcopy(SCOPES[r][scope])
    return dict(description=description or literal,literal_source=ptr)


def choices(literal,scope,description=None):
    return {r:choice(r,literal,description,scope) for r in 'ABC'}


def difference_ids(r,numbers):
    return [f'020A-{n:02d}' if r=='A' else f'B020-D{n:02d}' if r=='B' else f'020C-D{n:02d}' for n in numbers]


LOCI=[]


def add(key,location,ids,scope,c_rows=(),qs=None,text_choices=None,supplemental=None,component_scope=None):
    ids={r:difference_ids(r,nums) for r,nums in zip('ABC',ids)}
    qs=qs or ([],[],[])
    qs=dict(zip('ABC',qs))
    text_choices=text_choices or {}
    supplemental=supplemental or {}
    locus=dict(source_locus_id='SRC020-'+key,location=location,source_C_doubt_rows=list(c_rows),
        readers={},readers_report_only={},reader_difference_rows={},reader_doubt_rows={},reader_tex_scopes={},
        reader_tex_choices={},reader_provenance={},reader_supplemental_sources={},report_silent_choices=[],
        root_decision_id=None,root_status=None,diff_C=None,diff_H=None,main_approved=False,
        count_status='Source correspondence only; physical count and confidence await root.')
    for r in 'ABC':
        raw=U['reader_sources'][r]['raw_rows']
        ds=[copy.deepcopy(item) for item in raw['differences'] if item['value']['id'] in ids[r]]
        assert len(ds)==len(ids[r]),(key,r,ids[r])
        doubtful=[copy.deepcopy(raw['doubts'][i]) for i in qs[r]]
        full=copy.deepcopy(SCOPES[r][scope])
        extras=[copy.deepcopy(item) for item in supplemental.get(r,[])]
        selected=text_choices.get(r)
        public=[item['value']['reading'] for item in ds]
        if selected:
            public.append(selected['description'])
            locus['reader_tex_choices'][r]=copy.deepcopy(selected)
            if not ds:
                locus['report_silent_choices'].append(dict(reader=r,**copy.deepcopy(selected),
                    complete_inspected_tex_scope=full,
                    scope='Literal choice or source absence within the exact complete source span; no uninspected ink assertion.'))
        for row in doubtful:
            public.append('Original local doubt reading: '+row['value']['reading']+'; alternatives: '+json.dumps(row['value']['alternatives'],ensure_ascii=False))
        for item in extras:
            value=item['value']
            if isinstance(value,str): public.append(value)
            elif isinstance(value,dict) and 'reading' in value: public.append(value['reading'])
        assert public,(key,r)
        locus['readers'][r]=public
        locus['readers_report_only'][r]=[item['value']['reading'] for item in ds]
        locus['reader_difference_rows'][r]=ds
        locus['reader_doubt_rows'][r]=doubtful
        locus['reader_tex_scopes'][r]=full
        locus['reader_supplemental_sources'][r]=extras
        locus['reader_provenance'][r]=[item['source'] for item in ds+doubtful+extras]+[full]
        if selected:locus['reader_provenance'][r].append(selected['literal_source'])
    if component_scope:locus['component_scope']=component_scope
    LOCI.append(locus)


add('CONVENTION','Scan header convention',([28],[],[]),'header',
    text_choices=choices(r'\scanpage{20}','header'),
    supplemental={'A':[obj('A','/notes/source_only_administration')],
        'B':[obj('B','/notes/source_choices/0')],'C':[obj('C','/notes/source_administration')]},
    component_scope='Administrative header component of raw 020A-28; archive numeral has its own source locus.')
add('RING1','First opening Pi_I superscript',([1],[1],[1]),'opening',['C020-R01'],([0],[0],[0]),
    choices(r'\Pi_I^{\unsure{\circ|0}}','opening'))
add('RING2','Second opening Pi_J superscript',([2],[2],[2]),'opening',['C020-R01'],([1],[1],[1]),
    choices(r'\Pi_J^\circ','opening'),component_scope='Later recurring primary is printed; every actual local zero alternative remains in its original doubt row.')
add('PI-PREDECESSOR','Pi beneath opening U with indices and following comma',([3],[3],[3]),'opening',
    text_choices=choices(r'\deleted{\Pi}U_{J,i}$,','opening'))
add('CLAS-WORD','Word between les and parmi',([4],[4],[4]),'opening',['C020-R02'],([2],[2],[3]),
    {r:choice(r,r'\unsure{clas.|deux.}' if r in 'AB' else r'\unsure{deux|clas}.',scope='opening') for r in 'ABC'},
    component_scope='Lexical candidates only. The separate terminal point has SRC020-CLAS-POINT; raw 020A-04 includes both.')
add('CLAS-POINT','Separate terminal point after word before parmi',([4],[5],[5]),'opening',
    text_choices={r:choice(r,r'\unsure{clas.|deux.} parmi' if r in 'AB' else r'\unsure{deux|clas}. parmi',
        'A definite terminal point follows each candidate in the exact source: '+(r'\unsure{clas.|deux.} parmi' if r in 'AB' else r'\unsure{deux|clas}. parmi'),scope='opening') for r in 'ABC'},
    component_scope='Punctuation component. Raw 020A-04 wording/flags remain one original record; root chooses the physical count once.')
add('PAIR-INDEX','First positive Sigma index, including overwritten-state alternatives',([5],[6],[6]),'paired',['C020-R03'],([3],[3],[4]),
    {r:choice(r,r'\Sigma_{\unsure{j|\deleted{J}i|i}}^+' if r=='A' else r'\Sigma_{\unsure{\deleted{J}i|j|i}}^+',scope='paired') for r in 'ABC'})
add('POSITIVE-SIGMA-HEAD','Root-identified separate upper run at first positive Sigma head',([],[],[]),'paired',
    text_choices={r:choice(r,r'\Sigma_{\unsure{j|\deleted{J}i|i}}^+' if r=='A' else r'\Sigma_{\unsure{\deleted{J}i|j|i}}^+',
        'Ordinary Sigma macro with the exact local index alternatives; no separately drawn upper-run path in the complete paired-display source.',scope='paired') for r in 'ABC'},
    supplemental={'A':[obj('A','/notation/2')],'B':[obj('B','/notes/source_choices/1')],'C':[obj('C','/notation/2')]},
    component_scope='Root journal L020-07 identifies this component. Original reader source forms and bounded source absence are recorded; no extra original C doubt row is created.')
add('PAIRED-REMAINDER','Paired intersections, second index, signs and separator',([],[],[]),'paired',
    text_choices={r:choice(r,scope='paired',description='Complete paired-display source retained; both U_{J,i}, positive/negative signs, comma and second Sigma_i index are literal here. '+SCOPES[r]['paired']['excerpt']) for r in 'ABC'},
    supplemental={'B':[obj('B','/notes/source_choices/1')]},
    component_scope='Complete agreed context; first positive Sigma index has its own independently attributed locus. No extra overline command appears in any complete paired-display span.')
add('NEGATIVE-SIGMA-HEAD','Root-identified negative Sigma whole-glyph and separate upper run',([],[],[]),'paired',
    text_choices={r:choice(r,r'\Sigma_i^-',r'\Sigma_i^-; no separately drawn head, upper-run, raised-point or lower-hook path in this complete paired-display source.',scope='paired') for r in 'ABC'},
    supplemental={'A':[obj('A','/notation/2'),obj('A','/notation/4')],'B':[obj('B','/notes/source_choices/1')],'C':[obj('C','/notation/2')]},
    component_scope='Root journal L020-08 identifies the complete negative-glyph component. Source index i remains literal; root supplies the observed graphical selection and count.')
add('UPPER-PROSE','Prose following first paired display',([],[],[]),'upper',
    text_choices=choices('qui sont non vides. Or les deux classes en question sont non vides, car','upper'),
    supplemental={'B':[obj('B','/notes/source_choices/2')]})
add('CANCELLED-SIGMA','Cancelled Sigma/index and all its cancellation strokes before U',([6],[7],[7]),'upper',['C020-R04'],([4],[4],[5]),
    {r:choice(r,scope='upper',description=(
        r'A020-G01 supplies one visible \Sigma_{\unsure{j|i}}, its invisible deletion annotation and two literal crossing paths; following U lies outside.' if r=='A' else
        r'B_G01 supplies one visible \unsure{\Sigma_j|\Sigma_i}, its invisible deletion annotation and two literal crossing paths; following U lies outside.' if r=='B' else
        r'\deleted{\Sigma_{\unsure{j|i}}}; no separately drawn cancellation path in this complete upper-prose source.')) for r in 'ABC'},
    supplemental={'A':[obj('A','/graphics/0')],'B':[obj('B','/graphic_groups/0')]},
    component_scope='One whole cancelled Sigma/index graphic candidate; H020-ILL-01 is the available shared-placeholder parent. Raw reader counts remain proposals.')
add('CANCELLED-SIGMA-HEAD','Root-identified upper-run component at cancelled Sigma',([],[],[]),'upper',
    text_choices={'A':choice('A',r'\rlap{$\Sigma_{\unsure{j|i}}$}',r'A020-G01 uses an ordinary \Sigma_{\unsure{j|i}} as its visible letter node, with two separate cancellation paths; no additional literal upper-head run appears in the complete group.','upper'),
        'B':choice('B',r'\rlap{$\unsure{\Sigma_j|\Sigma_i}$}',r'B_G01 uses ordinary \Sigma_j/\Sigma_i as its visible letter node, with two separate cancellation paths; no additional literal upper-head run appears in the complete group.','upper'),
        'C':choice('C',r'\deleted{\Sigma_{\unsure{j|i}}}',r'\deleted{\Sigma_{\unsure{j|i}}}; the complete source supplies no separately drawn upper-head run.','upper')},
    supplemental={'A':[obj('A','/graphics/0')],'B':[obj('B','/graphic_groups/0')]},
    component_scope='Root journal L020-10 identifies this component within the cancelled-Sigma cluster at L020-09. No extra C row or separate clerk count is introduced.')
add('VOISINAGE-POINT','Small shape below gap after voisinage',([7],[],[]),'upper',qs=([6],[],[]),
    text_choices={'A':choice('A',scope='upper',description='A020-G02 is a qualified gray round point; voisinage and de remain outside the group.'),
        'B':choice('B',r'est un voisinage de $\deleted{\Sigma}E_{\unsure{i|j}}$',r'The complete upper-prose source prints est un voisinage de $\deleted{\Sigma}E_{\unsure{i|j}}$ with no separate point/path between voisinage and de.','upper'),
        'C':choice('C',r'est un voisinage de $\deleted{\Sigma}E_i$',r'The complete upper-prose source prints est un voisinage de $\deleted{\Sigma}E_i$ with no separate point/path between voisinage and de.','upper')},
    supplemental={'A':[obj('A','/graphics/1')]},
    component_scope='B/C source absence is limited to the complete inspected upper-prose source; no B/C local ink judgment is inferred.')
add('E-INDEX','E index after voisinage de',([8],[8],[8]),'upper',['C020-R05'],([5],[5],[]),
    {r:choice(r,r'E_{\unsure{i|j}}' if r in 'AB' else 'E_i',scope='upper') for r in 'ABC'})
add('E-PREDECESSOR','Sigma predecessor beneath E after voisinage de',([9],[9],[9]),'upper',
    text_choices={r:choice(r,r'\deleted{\Sigma}E_{\unsure{i|j}}' if r in 'AB' else r'\deleted{\Sigma}E_i',scope='upper') for r in 'ABC'})
add('E-COMMA','Comma after voisinage E index before et',([10],[10],[10]),'upper',
    text_choices={r:choice(r,r'E_{\unsure{i|j}}$, et' if r in 'AB' else r'E_i$, et',scope='upper') for r in 'ABC'})
add('BAR1','First nonemptiness overbar',([],[],[]),'nonempty',
    text_choices=choices(r'\overline{\Sigma_i^+}','nonempty'),
    supplemental={r:[obj(r,'/notes/S_coverage')] for r in 'ABC'},
    component_scope='Existing first overbar; exact S scope and root S selection remain separate.')
add('BAR1-SIGMA-HEAD','Root-identified short head run inside first long-barred Sigma group',([],[],[]),'nonempty',
    text_choices={r:choice(r,r'\overline{\Sigma_i^+}',r'\overline{\Sigma_i^+}: long outer overbar present; the ordinary Sigma macro has no separately drawn short-head run in this complete source.',scope='nonempty') for r in 'ABC'},
    supplemental={'A':[obj('A','/notation/3')],'B':[obj('B','/notation/2')],'C':[obj('C','/notation/3')]},
    component_scope='Root journal L020-17 identifies the short-head component beneath the separately confirmed long outer rule. It creates no additional original C doubt row.')
add('BAR2','Second nonemptiness overbar',([],[],[]),'nonempty',
    text_choices=choices(r'\overline{\deleted{E}\Sigma_i^-}','nonempty'),
    supplemental={r:[obj(r,'/notes/S_coverage')] for r in 'ABC'},
    component_scope='Existing second overbar; the E predecessor is independently cross-referenced at BAR2-SIGMA-PREDECESSOR.')
add('BAR1-E-PREDECESSOR','Sigma predecessor under first nonempty E',([11],[11],[11]),'nonempty',
    text_choices={r:choice(r,r'\overline{\Sigma_i^+}\cap\deleted{\Sigma}E_i',scope='nonempty') for r in 'ABC'})
add('BAR2-SIGMA-PREDECESSOR','E predecessor under second barred Sigma',([12],[12],[12]),'nonempty',
    text_choices=choices(r'\overline{\deleted{E}\Sigma_i^-}','nonempty'))
add('BAR2-E-PREDECESSOR','Sigma predecessor under second nonempty E',([13],[13],[13]),'nonempty',
    text_choices=choices(r'\overline{\deleted{E}\Sigma_i^-}\cap\deleted{\Sigma}E_i','nonempty'))
add('NONEMPTY-ENDPOINTS','Nonemptiness relations and comma/period endpoints',([],[],[]),'nonempty',
    text_choices={r:choice(r,scope='nonempty',description=SCOPES[r]['nonempty']['excerpt']) for r in 'ABC'},
    supplemental={'B':[obj('B','/notes/source_choices/3')]})
add('VOIT','Verb in On ... donc',([14],[14],[14]),'count',['C020-R10'],
    text_choices=choices('On sait donc','count'))
add('EN','Live en before cancelled count word',([15],[15],[15]),'count',
    text_choices=choices('est en','count'),component_scope='Live en only; the cancelled word and H020-ILL-02 have their separate count locus.')
add('COUNT-WORD','Cancelled tout/est before count, including cancellation geometry',([16],[16],[16]),'count',['C020-R06'],([7],[6],[6]),
    {'A':choice('A',scope='count',description=r'A020-G03 prints one qualified tout/est with its invisible deletion annotation and two literal crossing paths; en and the count lie outside.'),
     'B':choice('B',r'\deleted{\unsure{tout|est}}',scope='count'),
     'C':choice('C',r'\deleted{\unsure{tout|est}}',scope='count')},
    supplemental={'A':[obj('A','/graphics/2')]},
    component_scope='One cancelled-word/crossing cluster; H020-ILL-02 is the available shared-placeholder parent.')
add('COUNT','Written count with adjoining parenthesis',([],[],[]),'count',
    text_choices=choices(r'$(n-1)+2=n+1=\operatorname{card} I+1$ (ce qui achève','count'),
    supplemental={'B':[obj('B','/notes/source_choices/4')]},
    component_scope='Attributed manuscript source only; no arithmetic or proof check is supplied by this correspondence.')
add('ACHEVE','Achève accent and adjoining ce qui',([],[],[]),'count',
    text_choices=choices('ce qui achève','count'),
    supplemental={'A':[obj('A','/notes/report_silent_source_choices/3')],'B':[obj('B','/notes/source_choices/5')],'C':[obj('C','/notes/source_silent_choices')]})
add('AUSSI','Adverb before la',([17],[17],[17]),'count',['C020-R11'],([8],[7],[10]),
    choices(r'\unsure{aussi|ainsi}','count'))
add('LA-POINT','Small component above/right of la and its attachment',([18],[18],[]),'count',qs=([9],[8],[]),
    text_choices={'A':choice('A',scope='count',description='A020-G04 contains one qualified triangular point; the source word la precedes the group outside its boundary.'),
        'B':choice('B',scope='count',description='B_G02 contains la once and one qualified point in its translated inner TikZ group; its attachment to la is locally unresolved.'),
        'C':choice('C',r'\unsure{aussi|ainsi} la \unsure{dèm.|dém.|dem.}',r'The complete count source prints \unsure{aussi|ainsi} la \unsure{dèm.|dém.|dem.}; it emits no separate point/path at la. C attributes the small terminal component to the existing word once.','count')},
    supplemental={'A':[obj('A','/graphics/3')],'B':[obj('B','/graphic_groups/1')],'C':[obj('C','/notes/source_silent_choices')]},
    component_scope='A group excludes la; B group includes la once; C represents the described terminal component through la. Exact attachment remains root’s decision.')
add('DEM','Abbreviation before par, including accent alternatives',([19],[19],[18]),'count',['C020-R07'],([10],[9],[7]),
    {r:choice(r,r'\unsure{dém.|dem.}' if r=='A' else r'\unsure{dèm.|dém.|dem.}',scope='count') for r in 'ABC'})
add('PAR','Compressed par/p before récurrence',([20],[],[]),'count',qs=([11],[],[]),
    text_choices={r:choice(r,r'\unsure{par|p}' if r=='A' else 'par récurrence',scope='count') for r in 'ABC'},
    supplemental={'A':[obj('A','/notes/report_silent_source_choices/5')],'B':[obj('B','/notes/source_choices/6')],'C':[obj('C','/notes/source_silent_choices')]})
add('RECURRENCE','Récurrence spelling and acute',([],[],[]),'count',text_choices=choices('récurrence','count'),
    supplemental={'A':[obj('A','/notes/report_silent_source_choices/3')],'B':[obj('B','/notes/source_choices/6')],'C':[obj('C','/notes/source_silent_choices')]})
add('NB1','First nb, in class-count lead-in',([],[],[]),'count',text_choices=choices('le nb des classes est','count'))
add('NB2','Second nb, at parenthesis end',([],[],[]),'count',text_choices=choices('sur le nb des classes).','count'))
add('CARD','Lowercase card in written count',([],[],[]),'count',text_choices=choices(r'\operatorname{card} I+1','count'))
add('LEMMA-HEADING','Underlined Lemme and following words',([],[],[]),'lemma_heading',
    text_choices=choices(r'\uline{Lemme} Toute classe de','lemma_heading'))
add('RING3','Lemma Pi_I superscript',([21],[20],[19]),'lemma_heading',['C020-R01'],([12],[10],[2]),
    choices(r'\Pi_I^\circ','lemma_heading'))
add('UNION','Large indexed union sign and complete containing formula group',([],[21],[21]),'lemma_formula',
    text_choices={'A':choice('A',r'\bigcup_{\alpha\in\deleted{I}K}',r'A020-G05 uses \bigcup_{\alpha\in\deleted{I}K}; its complete group contains X, setminus, body, hatted label and two literal brace paths. It supplies no separate literal union path.','lemma_formula'),
        'B':choice('B',scope='lemma_formula',description='B_G03 U01/U02/U03 are the three literal union commands; X setminus remains outside this group in the containing math source.'),
        'C':choice('C',scope='lemma_formula',description='G01.1/G01.2 are the two literal union commands; the complete G01--G02 group contains X and setminus as its first two nodes.')},
    supplemental={'A':[obj('A','/graphics/4')],'B':[obj('B','/graphic_groups/2')],'C':[obj('C','/notes/graphic_groups/0')]},
    component_scope='Complete group boundary and union component; brace/index/hat remain separately cross-referenced without any clerk count.')
add('UNION-INDEX','Union index under K',([22],[22],[20]),'lemma_formula',['C020-R08'],([],[11],[8]),
    {r:choice(r,r'\alpha\in\deleted{I}K' if r=='A' else r'\alpha\in\unsure{\deleted{I}K|K}',scope='lemma_formula') for r in 'ABC'})
add('BRACE','Complete upper brace and left return/loop',([23],[23],[22]),'lemma_formula',
    text_choices={r:choice(r,scope='lemma_formula',description={
        'A':'A020-G05 supplies the complete main brace path and separate closed left retrace beside its body and inserted hatted label.',
        'B':'B_G03 supplies BR01 main brace/turn, BR02 left loop and BR03 left retrace beside its body and inserted hatted label.',
        'C':'G01--G02 supplies G02.1 complete brace/step/right hook and G02.2 left closed loop/dark return beside its body and inserted hatted label.'}[r]) for r in 'ABC'},
    supplemental={'A':[obj('A','/graphics/4')],'B':[obj('B','/graphic_groups/2')],'C':[obj('C','/notes/graphic_groups/0')]})
add('HAT-LABEL','Inserted hatted Sigma label above brace',([],[],[]),'lemma_formula',
    text_choices=choices(r'\inserted{\widehat{\Sigma}_\alpha^+}','lemma_formula'),
    supplemental={'A':[obj('A','/notes/H_apparatus')],'B':[obj('B','/notes/H_collation')],'C':[obj('C','/notes/source_administration')]},
    component_scope='One inserted label. The exact H note describing its position is preserved as witness apparatus in the source union.')
add('NONVIDE','Inserted cancelled non vide and its cancellation path',([24],[24],[23]),'lemma_insertion',
    text_choices={r:choice(r,scope='lemma_insertion',description={
        'A':'A020-G06 contains inserted non vide, an invisible inserted/deleted annotation, one literal cancellation run and adjoining de I,; partie and et lie outside.',
        'B':'B_G04 contains partie, inserted non vide with invisible deleted annotation, de I, et, and cancellation path NV01 with its right return.',
        'C':'G03--G04 contains partie, inserted non vide with invisible deleted annotation, and de I followed by its comma; cancellation path G03 carries its hooked right return; et lies outside.'}[r]) for r in 'ABC'},
    supplemental={'A':[obj('A','/graphics/5')],'B':[obj('B','/graphic_groups/3')],'C':[obj('C','/notes/graphic_groups/1')]},
    component_scope='Cancellation component within each complete insertion group; adjoining words and separate guide remain exact.')
add('GUIDE','Curved guide to inserted non vide with adjoining words',([24],[25],[24]),'lemma_insertion',
    text_choices={r:choice(r,scope='lemma_insertion',description={
        'A':'A020-G06: one curved guide; words inside are non vide and de I,; partie and et remain outside.',
        'B':'B_G04 NV02: one curved guide; words inside are partie, non vide and de I, et.',
        'C':'G03--G04 G04: one curved guide; words inside are partie, non vide and de I,; et remains outside.'}[r]) for r in 'ABC'},
    supplemental={'A':[obj('A','/graphics/5')],'B':[obj('B','/graphic_groups/3')],'C':[obj('C','/notes/graphic_groups/1')]},
    component_scope='Guide component. Raw 020A-24 contains both cancellation and guide, and remains unchanged; root assigns any shared parent.')
add('LEMMA-PROSE','où K est une and exact words around insertion',([],[],[]),'lemma_insertion',
    text_choices={r:choice(r,'où $K$ est une',scope='lemma_insertion') for r in 'ABC'},
    supplemental={'B':[obj('B','/notes/source_choices/7')]},
    component_scope='The exact full span retains the grave on où and placement of partie/de I,/et, including words inside each graphical group.')
add('MARGIN','Complete slanted two-line marginal note',([],[],[]),'margin',
    text_choices={r:choice(r,scope='margin',description=SCOPES[r]['margin']['excerpt']) for r in 'ABC'},
    component_scope='Both written conditions remain literal. Recorded angles/origins are copied from source without geometric calculation.')
add('ONA','Cancelled on a after first universal alpha in K',([25],[26],[25]),'membership',
    text_choices=choices(r'\deleted{on a}','membership'),
    component_scope='One readable cancelled prose cluster corresponding to H020-ILL-03.')
add('MEMBERSHIP','Reworked membership/arrow cluster before pi_0',([26],[27],[26]),'membership',['C020-R09'],([13],[12],[9]),
    {'A':choice('A',scope='membership',description=r'A020-G07 prints one locally qualified literal relation. Complete states \deleted{\Rightarrow}\in|\deleted{\to}\in|\in are preserved in its comment and invisible overlay annotation.'),
     'B':choice('B',scope='membership',description=r'B_G05 prints one locally qualified literal relation with complete states \deleted{\Rightarrow}\in|\deleted{\to}\in|\in explicitly following inside the same unsure wrapper.'),
     'C':choice('C',r'\unsure{\deleted{\Rightarrow}\in|\deleted{\rightarrow}\in|\in}',scope='membership')},
    supplemental={'A':[obj('A','/graphics/6')],'B':[obj('B','/graphic_groups/4')]},
    component_scope='One full glyph/state cluster; complete-candidate alternatives and literal paths are not additional manuscript occurrences.')
add('MEMBERSHIP-E','E inside X setminus E_alpha in pi_0 argument',([27],[],[]),'membership',qs=([14],[],[]),
    text_choices={r:choice(r,r'X\setminus{\unsure{E|\deleted{\Sigma}E}}_\alpha' if r=='A' else r'X\setminus E_\alpha',scope='membership') for r in 'ABC'},
    component_scope='A qualifies an E/Sigma-E predecessor state; B/C complete membership sources print E_alpha with no predecessor qualifier here.')
add('FINAL-CLAUSES','Final quantified hatted and parenthesized unhatted clauses',([],[],[]),'final',
    text_choices={r:choice(r,scope='final',description=SCOPES[r]['final']['excerpt']) for r in 'ABC'},
    supplemental={'B':[obj('B','/notes/source_choices/8')]},
    component_scope='Written double-implication and adjoining prose retained as attributed manuscript assertions; no equivalence/proof check.')
add('ARCHIVE','Archive numeral 19 comment',([28],[],[]),'archive',
    text_choices=choices('% archive sheet number: 19','archive'),
    supplemental={'A':[obj('A','/inventory/37')],'B':[obj('B','/inventory/31')],'C':[obj('C','/inventory/29')]},
    component_scope='Archive component of raw 020A-28; all original hand attributions remain in inventory provenance.')
add('S-AUDIT','S row identity, stated scope and local source correspondence',([],[],[]),'nonempty',
    text_choices={r:choice(r,scope='nonempty',description='Complete nonemptiness source preserves both local overbars. Exact S review remains attributed to this reader in the linked report note.') for r in 'ABC'},
    supplemental={r:[obj(r,'/notes/S_coverage')] for r in 'ABC'},
    component_scope='Source-only S coverage candidate; root source-audit choice and any local ink confirmations require separate exact journal sources.')

REMAINDER_KEYS=['PAIRED-REMAINDER','UPPER-PROSE','NONEMPTY-ENDPOINTS','COUNT','ACHEVE','RECURRENCE','NB1','NB2','CARD','LEMMA-HEADING','LEMMA-PROSE','FINAL-CLAUSES']
remainder=[l for key in REMAINDER_KEYS for l in LOCI if l['source_locus_id']=='SRC020-'+key]
aggregate=dict(source_locus_id='SRC020-AGREED-REMAINDER',location='Twelve agreed source scopes, subject to root local replacements',
    source_C_doubt_rows=[],readers={},readers_report_only={r:[] for r in 'ABC'},
    reader_difference_rows={r:[] for r in 'ABC'},reader_doubt_rows={r:[] for r in 'ABC'},reader_tex_scopes={},
    reader_tex_choices={},reader_provenance={},reader_supplemental_sources={r:[] for r in 'ABC'},report_silent_choices=[],
    aggregate_source_locus_ids=[l['source_locus_id'] for l in remainder],component_scopes={},
    root_decision_id=None,root_status=None,diff_C=None,diff_H=None,main_approved=False,
    count_status='Source-only aggregate; exact root authorization is L020-42, without a new ink view.')
for r in 'ABC':
    full=copy.deepcopy(U['reader_sources'][r]['complete_tex'])
    descriptions=[l['reader_tex_choices'][r]['description'] for l in remainder]
    description='Twelve original complete-source choices: '+'; '.join(descriptions)
    aggregate['readers'][r]=descriptions
    aggregate['reader_tex_scopes'][r]=full
    aggregate['reader_tex_choices'][r]=dict(description=description,literal_source=full)
    aggregate['component_scopes'][r]=[dict(source_locus_id=l['source_locus_id'],choice=copy.deepcopy(l['reader_tex_choices'][r]),complete_scope=copy.deepcopy(l['reader_tex_scopes'][r])) for l in remainder]
    aggregate['reader_provenance'][r]=[copy.deepcopy(l['reader_tex_choices'][r]['literal_source']) for l in remainder]
    aggregate['report_silent_choices'].append(dict(reader=r,description=description,literal_source=full,
        complete_inspected_tex_scope=full,scope='Aggregate of twelve exact original source scopes; previously selected root replacements govern final text.'))
LOCI.append(aggregate)

for locus in LOCI:
    locus['source_C_part_ids']=[
        (f'C020-R01-{dict(RING1=1,RING2=2,RING3=3)[locus["source_locus_id"].removeprefix("SRC020-")]}'
         if row=='C020-R01' else row+'-1') for row in locus['source_C_doubt_rows']]
    if locus['source_locus_id'] in ['SRC020-BAR1','SRC020-BAR2','SRC020-S-AUDIT']:
        locus['S_id']='SA01-K81-06'
        locus['S_status']='Pending root selection; raw source and reader coverage retained.'
        locus['S_source']=copy.deepcopy(U['sources']['packets/020/S_rows.json'])
ROOT_NEW={'SRC020-POSITIVE-SIGMA-HEAD':'L020-07','SRC020-NEGATIVE-SIGMA-HEAD':'L020-08',
    'SRC020-CANCELLED-SIGMA-HEAD':'L020-10','SRC020-BAR1-SIGMA-HEAD':'L020-17','SRC020-AGREED-REMAINDER':'L020-42'}
journal_path='out/checks/scan020_main_decisions.md'
journal=(BASE/journal_path).read_text()
for locus in LOCI:
    if locus['source_locus_id'] in ROOT_NEW:
        did=ROOT_NEW[locus['source_locus_id']]
        match=re.search(r'^'+re.escape(did)+r'\b',journal,re.M)
        assert match,did
        following=re.search(r'^L020-\d+\b|^## ',journal[match.end():],re.M)
        end=match.end()+following.start() if following else len(journal)
        locus['root_locus_introduction']=span(journal_path,journal,match.start(),end,
            source_sha256_utf8=hashlib.sha256(journal.encode()).hexdigest(),root_decision_id=did)

row_map={r:{} for r in 'ABC'}
doubt_map={r:{} for r in 'ABC'}
for locus in LOCI:
    for r in 'ABC':
        for item in locus['reader_difference_rows'][r]:
            row_map[r].setdefault(item['value']['id'],[]).append(locus['source_locus_id'])
        for item in locus['reader_doubt_rows'][r]:
            doubt_map[r].setdefault(item['source']['pointer'],[]).append(locus['source_locus_id'])
for r in 'ABC':
    assert set(row_map[r])=={v['id'] for v in R[r]['differences']},r
    assert set(doubt_map[r])=={f'/doubts/{i}' for i in range(len(R[r]['doubts']))},r

INVENTORY_SPECS=[
    ('TOP','Opening three prose lines',[0],[0],[0],[0]),
    ('PI-PREDECESSOR','Pi overwritten by opening U',[1],[1],[1],[1]),
    ('PAIRED','Paired intersections',[2],[2],[2],[2]),
    ('PAIR-INDEX','First positive Sigma index/predecessor',[3],[3],[3],[3]),
    ('UPPER-PROSE','Prose beneath pair through voisinage line',[4],[4,7],[4],[4]),
    ('CANCELLED-SIGMA','Cancelled Sigma/index and crossing paths',[5],[5,6],[5,6],[5]),
    ('VOISINAGE-POINT','Gray point after voisinage',[],[8],[],[]),
    ('E-PREDECESSOR','Sigma predecessor beneath voisinage E',[6],[9],[7],[6]),
    ('NONEMPTY','Two nonemptiness formulas',[7],[10],[8],[7]),
    ('BAR1-E-PREDECESSOR','First nonempty E predecessor',[8],[11],[9],[8]),
    ('BAR2-SIGMA-PREDECESSOR','Second barred Sigma predecessor',[9],[12],[10],[9]),
    ('BAR2-E-PREDECESSOR','Second nonempty E predecessor',[10],[13],[11],[10]),
    ('COUNT','Count and parenthesis prose',[11],[14,17],[12],[11]),
    ('COUNT-WORD','Cancelled tout/est and crossing paths',[12],[15,16],[13],[12]),
    ('LA-POINT','Upper-right component at la',[],[18],[14],[]),
    ('LEMMA-PROSE','Lemma heading and prose through conditions',[13],[19,24,29,34],[15,16,17],[13,14,20]),
    ('LEMMA-FORMULA','First lemma formula',[],[20],[18],[15]),
    ('UNION','Literal union paths',[],[],[19],[16]),
    ('UNION-INDEX','Possible old I beneath union-index K',[14],[21],[20],[17]),
    ('HAT-LABEL','Inserted hatted Sigma label',[15],[22],[21],[18]),
    ('BRACE','Complete upper brace',[],[23],[22],[19]),
    ('NONVIDE','Inserted/deleted non vide',[16,17],[25,26],[23,24],[21,22]),
    ('GUIDE','Cancellation/guide drawing inventory component',[],[27],[25],[23]),
    ('MARGIN','Slanted two-line marginal note',[18],[28],[26],[24]),
    ('ONA','Cancelled on a',[19],[30],[27],[25]),
    ('MEMBERSHIP','Reworked relation graphic and possible predecessor',[20],[31,32],[28,29],[26]),
    ('MEMBERSHIP-E','Possible Sigma predecessor in pi_0 argument E',[],[33],[],[]),
    ('FINAL','Final hatted and parenthesized unhatted clauses',[],[35,36],[30],[27,28]),
    ('ARCHIVE','Archive 19',[],[37],[31],[29]),
]
inventory=[]; seen={r:[] for r in ['witness C','A','B','C']}
for key,scope,c,a,b,cr in INVENTORY_SPECS:
    group=dict(source_inventory_id='SRC020-INV-'+key,scope=scope,source_rows={},selected=None,main_approved=False)
    for reader,indices in [('witness C',c),('A',a),('B',b),('C',cr)]:
        candidates=[item for item in U['candidate_inventory'] if item['reader']==reader]
        group['source_rows'][reader]=[copy.deepcopy(candidates[i]) for i in indices]
        seen[reader].extend(indices)
    inventory.append(group)
for reader,indices in seen.items():
    assert sorted(indices)==list(range(len([x for x in U['candidate_inventory'] if x['reader']==reader]))),(reader,indices)

graphics={
    'A':[obj('A',f'/graphics/{i}') for i in range(len(R['A']['graphics']))],
    'B':[obj('B',f'/graphic_groups/{i}') for i in range(len(R['B']['graphic_groups']))],
    'C':[obj('C',f'/notes/graphic_groups/{i}') for i in range(len(R['C']['notes']['graphic_groups']))],
}
candidate_path=OUT/'scan020_tex_candidates.json'
candidate=json.loads(candidate_path.read_text())
candidate_ref=dict(path=candidate_path.relative_to(BASE).as_posix(),sha256=hashlib.sha256(candidate_path.read_bytes()).hexdigest())
output=dict(scan=20,scope='Complete released-source correspondence; root supplies ink, physical counts, confidence and approval.',
    source_union=dict(path='out/checks/scan020_source_union.json',sha256=hashlib.sha256((OUT/'scan020_source_union.json').read_bytes()).hexdigest()),
    loci=LOCI,original_difference_row_crosswalk=row_map,original_doubt_row_crosswalk=doubt_map,
    original_C_rows=copy.deepcopy(U['C_doubt_crosswalk']),inventory_source_groups=inventory,
    complete_reader_source_scopes=SCOPES,original_graphic_group_metadata=graphics,
    tex_candidate_catalog=candidate_ref,
    complete_graphical_candidate_scopes=copy.deepcopy(candidate['graphic_groups']),
    exact_textual_candidate_scopes=copy.deepcopy(candidate['textual_and_qualifier_loci']),
    literal_graphical_sources={r:copy.deepcopy(U['reader_sources'][r]['tex_index']) for r in 'ABC'},
    all_original_difference_rows_mapped=True,all_original_doubt_rows_mapped=True,all_original_inventory_rows_mapped=True,
    main_adjudicated=False,count_scope_note='Source-locus and raw-row cardinalities supply no physical difference count.',
    original_C_source_rows=11,original_C_primary_parts=13)
path=OUT/'scan020_source_crosswalk.json'
path.write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n')
md=['# Scan020 — exact source crosswalk','',
    'Every source row retains its original identifier, fields and exact source span. Root supplies all ink/count/approval outcomes.','',
    '| Source locus | Scope | A difference IDs | B difference IDs | C difference IDs | Original C rows |',
    '| --- | --- | --- | --- | --- | --- |']
for locus in LOCI:
    cols=[locus['source_locus_id'],locus['location']]
    for r in 'ABC':
        cols.append(', '.join(item['value']['id'] for item in locus['reader_difference_rows'][r]) or 'complete TeX / source note')
    cols.append(', '.join(locus['source_C_doubt_rows']) or '—')
    md.append('| '+' | '.join(str(c).replace('|','\\|') for c in cols)+' |')
md.extend(['','The JSON supplies every public A/B/C reading, all local doubt alternatives, exact complete-source scopes, report-silent source choices, graphical boundaries, original C identities and inventory correspondence. Raw combined records can appear at their distinct source components; only root assigns their physical count parents.'])
(OUT/'scan020_source_crosswalk.md').write_text('\n'.join(md)+'\n')
fingerprints=json.loads((OUT/'scan020_source_fingerprints.json').read_text())
fingerprints.update(source_crosswalk=dict(path=path.relative_to(BASE).as_posix(),sha256=hashlib.sha256(path.read_bytes()).hexdigest()),
    tex_candidate_catalog=candidate_ref,record_stage=f'Complete source union and {len(LOCI)}-locus crosswalk; root selections/attachments pending.')
(OUT/'scan020_source_fingerprints.json').write_text(json.dumps(fingerprints,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(path=path.relative_to(BASE).as_posix(),sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
    source_loci=len(LOCI),original_difference_rows={r:len(v) for r,v in row_map.items()},
    original_doubt_rows={r:len(v) for r,v in doubt_map.items()},inventory_source_groups=len(inventory),
    raw_inventory_rows=sum(len(v) for v in seen.values()),main_adjudicated=False),ensure_ascii=False))
