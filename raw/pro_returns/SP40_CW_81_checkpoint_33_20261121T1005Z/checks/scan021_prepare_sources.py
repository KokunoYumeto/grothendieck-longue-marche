#!/usr/bin/env python3
"""Index explicitly released scan021 text returns; root alone selects ink/counts."""
from pathlib import Path
import argparse
import copy
import hashlib
import json
import re
import sys

sys.dont_write_bytecode = True
BASE = Path('/workspace/scratch/94548b74fbe0')
OUT = BASE / 'out/checks'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def read(path):
    return (BASE / path).read_text(encoding='utf-8')


def span(path, text, start=0, end=None, **extra):
    end = len(text) if end is None else end
    literal = text[start:end]
    return dict(path=path, manifest=path, char_start=start, char_end=end,
                offset_convention='zero-based Unicode code points; end exclusive',
                line_start=text.count('\n', 0, start)+1,
                line_end=text.count('\n', 0, max(start, end-1))+1,
                excerpt=literal, literal_sha256_utf8=sha(literal.encode('utf-8')), **extra)


def json_spans(path, text):
    decoder = json.JSONDecoder()
    result = {}

    def ws(i):
        while i < len(text) and text[i].isspace():
            i += 1
        return i

    def walk(i, pointer):
        i = ws(i)
        start = i
        value, end = decoder.raw_decode(text, i)
        result[pointer] = span(path, text, start, end, pointer=pointer)
        if isinstance(value, dict):
            i = ws(i+1)
            while i < end and text[i] != '}':
                key, key_end = decoder.raw_decode(text, i)
                i = ws(key_end)
                assert text[i] == ':'
                escaped = key.replace('~', '~0').replace('/', '~1')
                i = ws(walk(i+1, pointer+'/'+escaped))
                if text[i] != ',':
                    break
                i = ws(i+1)
        elif isinstance(value, list):
            i = ws(i+1)
            k = 0
            while i < end and text[i] != ']':
                i = ws(walk(i, pointer+'/'+str(k)))
                k += 1
                if text[i] != ',':
                    break
                i = ws(i+1)
        return end

    walk(0, '')
    return result


def literal_span(path, text, literal, occurrence=0):
    positions = [m.start() for m in re.finditer(re.escape(literal), text)]
    assert len(positions) > occurrence, (path, literal, occurrence)
    start = positions[occurrence]
    return span(path, text, start, start+len(literal))


def tex_index(path, text):
    blocks = []
    cursor = 0
    for i, match in enumerate(re.finditer(r'\\\[(.*?)\\\]', text, re.S)):
        if match.start() > cursor:
            blocks.append(dict(kind='complete inter-display source', source=span(path, text, cursor, match.start())))
        blocks.append(dict(id=f'display-{i+1:02d}', kind='complete display source', source=span(path, text, match.start(), match.end())))
        cursor = match.end()
    if cursor < len(text):
        blocks.append(dict(kind='complete trailing source', source=span(path, text, cursor, len(text))))
    comments = [span(path, text, m.start(), m.end()) for m in re.finditer(r'^%[^\n]*', text, re.M)]
    commands = []
    for i, match in enumerate(re.finditer(r'\\(?:draw|fill|path|node|coordinate|useasboundingbox)\b', text)):
        depth = 0
        for k in range(match.start(), len(text)):
            char = text[k]
            if char in '{}' and (k == 0 or text[k-1] != '\\'):
                depth += 1 if char == '{' else -1
            if char == ';' and depth == 0:
                commands.append(dict(command_id=f'command-{i+1:03d}', kind=match.group()[1:], source=span(path, text, match.start(), k+1)))
                break
        else:
            raise AssertionError((path, match.start(), 'unterminated literal command'))
    environments = []
    stack = []
    for match in re.finditer(r'\\(begin|end)\{(tikzpicture|tikzcd|scope)\}', text):
        if match[1] == 'begin':
            stack.append((match[2], match.start()))
        else:
            assert stack and stack[-1][0] == match[2], (path, match.start(), stack)
            environment, start = stack.pop()
            environments.append(dict(environment=environment, depth=len(stack), source=span(path, text, start, match.end())))
    assert not stack, (path, stack)
    environments.sort(key=lambda row: row['source']['char_start'])
    return dict(complete_blocks=blocks, complete_comment_lines=comments,
                literal_graphical_commands=commands, complete_graphical_environments=environments,
                indexing_scope='Literal source boundaries only; coordinate declarations and path strings copied without coordinate arithmetic or rendering.')


def source_categories(path, text):
    heads = list(re.finditer(r'^## .*$', text, re.M))
    return [dict(category=m.group()[3:], source=span(path, text, m.start(), heads[i+1].start() if i+1<len(heads) else len(text))) for i,m in enumerate(heads)]


def a_source_choices(tp, tt, report, group_sources):
    displays = list(re.finditer(r'\\\[.*?\\\]', tt, re.S))
    # Exact supplied source order and literal anchors; these spans supply readings,
    # including report-silent choices, without inferring from an absent report row.
    regions = [
        (tt.index('Soit '), displays[0].start()),
        (displays[0].start(), displays[0].end()),
        (displays[0].end(), displays[1].start()),
        (displays[1].start(), displays[1].end()),
        (displays[1].end(), displays[2].start()),
        (displays[2].start(), displays[2].end()),
        (displays[2].end(), displays[3].end()),
        (tt.index("d'autre part "), displays[4].end()),
        (tt.index('ce qui $'), tt.index('\\uline{Corollaire')),
        (tt.index('\\uline{Corollaire'), displays[5].start()),
        (displays[5].end(), displays[6].start()),
        (displays[6].start(), displays[6].end()),
    ]
    assert len(regions) == len(report['source_silent_choices'])
    complete = [dict(value=copy.deepcopy(value), tex_source=span(tp,tt,*bounds),
                     source_basis='Actual complete TeX region; report wording retained separately.')
                for value,bounds in zip(report['source_silent_choices'],regions)]
    lit = lambda s: literal_span(tp, tt, s)
    grp = lambda s: copy.deepcopy(group_sources[s])
    readings = {
        'A021-R01': lit(r"\unsure{l'on a|on a}"),
        'A021-R02': lit(r'\unsure{i.e|i.e.}'),
        'A021-R03': lit(r'(ce qui ach\unsure{è|é|e}vera la d\unsure{è|é}monstration, car on aura'),
        'A021-R04': grp('A021G19'), 'A021-R05': lit(r'\unsure{comme|\deleted{co}mme}'),
        'A021-R06': grp('A021G20'), 'A021-R07': grp('A021D05'), 'A021-R08': grp('A021D03'),
        'A021-R09': lit(r'\unsure{signifie|signifi}'), 'A021-R10': grp('A021G21'),
        'A021-R11': lit('$ signifie aussi que'), 'A021-R12': grp('A021G22'),
        'A021-R13': grp('A021G23'), 'A021-R14': grp('A021G06'), 'A021-R15': grp('A021G09'),
    }
    extra_groups = {4:'A021M01',5:'A021G18',6:'A021G19',9:'A021M02',10:'A021G07',
                    12:'A021DG',13:'A021DG',14:'A021DG',15:'A021DG',16:'A021M04',
                    17:'A021G11',18:'A021G21',19:'A021G22',20:'A021M03',23:'A021G25',
                    24:'A021G24',25:'A021G23',26:'A021G17'}
    for ordinal,gid in extra_groups.items():
        readings[f'A021-X{ordinal:02d}'] = grp(gid)
    for ordinal,region in [(1,0),(7,4),(8,4)]:
        readings[f'A021-X{ordinal:02d}'] = span(tp,tt,*regions[region])
    for ordinal,literal in [(2,r'ach\unsure{è|é|e}vera'),(3,r'd\unsure{è|é}monstration'),
                            (11,'cela implique que'),(21,r'pr\unsure{é|ê|e}c\unsure{é|e}dent'),
                            (22,r'pr\unsure{é|ê|e}c\unsure{é|e}dent')]:
        readings[f'A021-X{ordinal:02d}'] = lit(literal)
    for row in report['differences']:
        if row['id'].startswith('A021-S'):
            readings[row['id']] = grp(row['location'].split(' ',1)[0])
    assert set(readings) == {row['id'] for row in report['differences']}
    return complete, readings


def b_source_choices(tp, tt, report, audit, group_sources):
    lit = lambda s: literal_span(tp, tt, s)
    grp = lambda s: copy.deepcopy(group_sources[s])
    displays = list(re.finditer(r'\\\[.*?\\\]', tt, re.S))
    spans = [
        lit("Soit $\\alpha_0\\in K_1$, je dis que \\unsure{l'on a|on a}\n"),
        grp('B021-G01'),
        lit(r'(ce qui \unsure{achèvera|achévera} la démonstration, car on aura'),
        grp('B021-G02'),
        lit('comme dans le lemme.'),
        span(tp,tt,displays[2].start(),displays[2].end()),
        lit('cela implique que'),
        grp('B021-G06'),
        span(tp,tt,tt.index("d'autre part "),displays[5].end()),
        grp('B021-G10'),grp('B021-G10'),lit('% archive sheet number: 20'),
    ]
    assert len(spans)==len(audit['report_silent_choices'])
    complete=[dict(value=copy.deepcopy(value),tex_source=source,
                   source_basis='Actual complete TeX region; report wording retained separately.')
              for value,source in zip(audit['report_silent_choices'],spans)]
    readings={}
    for row in report['differences']:
        group=row.get('source_group')
        if group:
            readings[row['id']]=grp(group)
    readings.update({
        'B021-D01':lit(r"\unsure{l'on a|on a}"),
        'B021-D03':spans[2],
        'B021-D09':lit(r'\unsure{signifi|signifie}'),
        'B021-D11':lit(' signifie aussi que'),
        'B021-D16':spans[0],
        'B021-D17':lit(r'\unsure{achèvera|achévera}'),
        'B021-D20':span(tp,tt,tt.index('Or % BEGIN B021-G03'),displays[2].start()),
        'B021-D21':lit('cela implique que'),
        'B021-D31':span(tp,tt),
    })
    local={4:'B021-G02-cancelled-Sigma',6:'B021-G06-lead-in',8:'B021-G06-middle-row',
           13:'B021-G10-overwritten-V-E',15:'B021-G05-index',22:'B021-G06-lead-in',
           23:'B021-G06-lower-trace',24:'B021-G04-point',25:'B021-G10-V-speck'}
    for number,group in local.items():
        readings[f'B021-D{number:02d}']=grp(group)
    assert set(readings)=={row['id'] for row in report['differences']}
    return complete,readings


def c_source_choices(tp, tt, report, audit, group_sources):
    lit=lambda s:literal_span(tp,tt,s)
    grp=lambda s:copy.deepcopy(group_sources[s])
    displays=list(re.finditer(r'\\\[.*?\\\]',tt,re.S))
    paragraph=lit(r'(ce qui ach\unsure{è|é|e}vera la \unsure{demonstration|démonstration}, car on aura')
    spans=[
        lit("Soit $\\alpha_0\\in K_1$, je dis que \\unsure{l'on a|on a}\n"),grp('C021-G01'),paragraph,
        span(tp,tt,displays[1].start(),tt.index('\nOr ')),lit(r'Or \unsure{comme} on a'),grp('C021-G03'),
        span(tp,tt,tt.index('cela implique que'),displays[3].end()),grp('C021-G05'),
        span(tp,tt,tt.index("d'autre part "),displays[4].end()),
        span(tp,tt,tt.index('ce qui % BEGIN C021-G07'),tt.index('\\uline{Corollaire')),
        lit(r'\uline{Corollaire du lemme} Pour une classe'),
        lit(r'\node at (300,1915) {$V$ de $\Pi_I^{\unsure{\circ|0}}$, son expression};'),
        span(tp,tt,tt.index(r'\node at (602,2005)'),tt.index(r'\node at (300,2145)')),
        span(tp,tt,tt.index(r'\node at (300,2145)'),tt.index('% Main bottom brace:')),
        span(tp,tt,tt.index('% Main bottom brace:'),tt.index('% Final Sigma head/body')),
        span(tp,tt,tt.index('% Final Sigma head/body'),tt.index('% END C021-G09\n')),
        lit('% archive sheet number: 20'),
    ]
    assert len(spans)==len(audit['source_choices_including_report_silent'])
    complete=[dict(value=copy.deepcopy(value),tex_source=source,
                   source_basis='Actual complete TeX region; report wording retained separately.')
              for value,source in zip(audit['source_choices_including_report_silent'],spans)]
    readings={row['id']:grp(row['source_group']) for row in report['differences'] if row.get('source_group')}
    readings.update({
        'C021-R01':lit(r"\unsure{l'on a|on a}"),'C021-R02':grp('C021-G01'),'C021-R03':paragraph,
        'C021-R04':grp('C021-G02'),'C021-R05':lit(r'\unsure{comme}'),'C021-R06':grp('C021-G05a'),
        'C021-R07':grp('C021-G05b'),'C021-R08':grp('C021-G05'),
        'C021-R09':lit(r"d'autre part $\alpha_0\in K_1$ signifie"),'C021-R10':grp('C021-G07'),
        'C021-R11':lit(' signifie aussi que $'),'C021-R12':lit(r'\Pi_I^{\unsure{\circ|0}}'),
        'C021-R13':grp('C021-G09b'),'C021-R14':grp('C021-G03'),'C021-R15':grp('C021-G04'),
        'C021-D01':spans[0],'C021-D02':spans[4],'C021-D08':lit(r'ach\unsure{è|é|e}vera'),
        'C021-D09':lit(r'\unsure{demonstration|démonstration}'),'C021-D10':lit('cela implique que'),
        'C021-D12':lit(r'pr\unsure{é|ê}cédent'),'C021-D13':spans[15],
    })
    assert set(readings)=={row['id'] for row in report['differences']}
    return complete,readings


def sigma_head_crosswalk(readers, graphical_groups):
    texts={r:read(f'out/readers/021/{r}/reading.tex') for r in readers}
    groups={(g['reader'],g['group_id']):g['tex_source'] for g in graphical_groups}

    def cut(r,begin,end):
        text=texts[r];start=text.index(begin);stop=text.index(end,start)
        return span(f'out/readers/021/{r}/reading.tex',text,start,stop)

    def lit(r,literal):
        return literal_span(f'out/readers/021/{r}/reading.tex',texts[r],literal)

    def group(r,gid):
        return copy.deepcopy(groups[(r,gid)])

    a_ids=['A021G01','A021G02','A021G03','A021G04','A021G05','A021G07','A021G08',
           'A021G09','A021G10','A021G12','A021G13','A021G14','A021G15','A021G16','A021G17',
           'A021D01','A021D02','A021D03','A021D04']
    labels=['first intersection, roofed Sigma alpha0','first intersection, roofed Sigma i plus',
            'right first intersection, Sigma alpha0','right first intersection, Sigma i',
            'upper U expression, roofed Sigma alpha plus','central inclusion, roofed Sigma alpha plus',
            'second inclusion, left roofed Sigma alpha0 plus','second inclusion, right Sigma alpha0/alpha minus',
            'exclusion, left Sigma alpha0 plus','exclusion, right Sigma i plus',
            'conclusion, first Sigma i plus','conclusion, second Sigma alpha plus',
            'corollary V expression, roofed Sigma alpha plus','last condition, leading Sigma alpha plus',
            'last condition, X complement Sigma alpha','marginal top Sigma i plus','marginal top Sigma i minus',
            'marginal third row Sigma i-alpha','marginal bottom Sigma alpha0 plus']
    b_sources=[
        cut('B','% First complete hatted Sigma:',r'\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (698,233)'),
        cut('B','% Second complete hatted Sigma,',r'\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (863,230)'),
        cut('B',r'\draw[line width=.4pt] (1244,185)',r'\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1318,225)'),
        cut('B',r'\draw[line width=.4pt] (1349,186)',r'\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1428,228)'),
        cut('B',r'\draw[line width=.4pt] (957,487)','% Complete brace with'),
        cut('B','% Complete hatted Sigma group,','% END B021-G04'),
        cut('B',r'\draw[line width=.35pt] (930,1103)',r'\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1080,1147)'),
        cut('B',r'\draw[line width=.35pt] (1142,1110)','% END B021-G05'),
        cut('B',r'\draw[line width=.35pt] (632,1347)',r'\draw[line width=.4pt] (832,1352)'),
        cut('B',"% The right Sigma has",'% END B021-G07'),
        cut('B',r'\draw[line width=.35pt] (311,1582)',r'\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (417,1620)'),
        cut('B',r'\draw[line width=.35pt] (462,1577)',r'\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (576,1625)'),
        cut('B',r'\draw[line width=.4pt] (995,1931)',r'\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (303,2145)'),
        cut('B','% Second condition.',r'\node[anchor=base west,inner sep=0pt,outer sep=0pt,font=\fontsize{6}{6}'),
        lit('B',r"\node[anchor=base west,inner sep=0pt,outer sep=0pt,font=\fontsize{6}{6}\selectfont] at (661,2338) {est l'unique comp. de $X\setminus\Sigma_\alpha$ contenue dans $X\setminus V$};"),
        lit('B',r'\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1507,1002) {$\scriptstyle\Sigma_i^+\ \text{ou}\ \Sigma_i^-$};'),
        lit('B',r'\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1507,1002) {$\scriptstyle\Sigma_i^+\ \text{ou}\ \Sigma_i^-$};'),
        group('B','B021-G06-middle-row'),
        lit('B',r'\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1524,1259) {$\scriptstyle\Sigma_{\alpha_0}^+$};'),
    ]
    c_sources=[
        group('C','C021-G01a'),
        cut('C','% second roofed Sigma owns',r'\node at (861,229)'),
        cut('C','% right first Sigma:',r'\node at (1318,233)'),
        cut('C',r'\draw (1347,185)',r'\node at (1426,223)'),
        lit('C',r'\node at (520,555) {$U=X\setminus\bigcup_{\alpha\in K}\widehat{\Sigma}_\alpha^+$};'),
        cut('C','% Complete roofed Sigma group:','% END C021-G03'),
        cut('C',r'\draw (925,1104)',r'\node at (1080,1150)'),
        cut('C',r'\draw (1142,1110)','% END C021-G04'),
        cut('C',r'\draw (633,1344)',r'\node at (778,1388)'),
        cut('C',r'\draw (870,1332)','% END C021-G06'),
        cut('C',r'\draw (310,1574)',r'\node at (412,1611)'),
        cut('C',r'\draw (464,1577)',r'\node at (574,1610)'),
        lit('C',r'\node at (952,1986) {$\widehat{\Sigma}_\alpha^+$};'),
        cut('C','% Final Sigma head/body',r'\node at (663,2341)'),
        cut('C',r'\node at (1116,2332)',r'\node at (1240,2334)'),
        cut('C','% Top signed Sigmas',r'\node at (1568,1003)'),
        cut('C',r'\node at (1608,1006)',r'\node at (1530,1064)'),
        cut('C','% Full third label,',r'\node at (1516,1184)'),
        cut('C',r'\node at (1525,1266)','% Both braces retain'),
    ]
    c_ids=['C021-H01','C021-H02','C021-H03','C021-H04',None,'C021-H05','C021-H06','C021-H07',
           'C021-H08','C021-H09','C021-H10','C021-H11',None,'C021-H16','C021-H17',
           'C021-H12','C021-H13','C021-H14','C021-H15']
    result=[]
    for i,(gid,label,bs,cs,cid) in enumerate(zip(a_ids,labels,b_sources,c_sources,c_ids)):
        mapping={}
        for reader,source,ident in [('A',group('A',gid),f'A021-S{i+1:02d}'),('B',bs,'B021-D31'),('C',cs,cid)]:
            raw=[copy.deepcopy(r) for r in readers[reader]['raw_rows']['differences'] if r['value']['id']==ident]
            mapping[reader]=dict(actual_tex_source=source,raw_report_sources=raw,
                report_silent_local_choice=ident is None or (reader=='B' and i in [15,16,17,18]),
                report_scope='B D31 is a broad same-reading source-syntax record; the actual local TeX excerpt supplies this occurrence.' if reader=='B'
                    else ('No dedicated head-role report row; actual complete local source is retained.' if ident is None
                          else 'Dedicated original local head-role row, preserved without root adoption.'),
                actual_source_form='ordinary Sigma macro in the supplied text node' if (reader=='B' and i in [14,15,16,18]) or (reader=='C' and i in [4,12])
                    else 'complete literal source paths/nodes at this occurrence',
                main_approved=False)
        result.append(dict(id=f'SIG021-{i+1:02d}',location=label,readers=mapping,selected=None,
            source_correspondence_basis='Each original source occurrence identified by its exact surrounding words, signs and supplied group ownership. No ink or mathematical role adjudication.',main_approved=False))
    return result


def collect(released):
    assert all(r in 'ABC' for r in released) and len(set(released)) == len(released)
    paths = ['out/briefs/source_record_brief_v03.md']
    paths += [p.relative_to(BASE).as_posix() for p in sorted((BASE/'packets/021').iterdir()) if p.suffix in ('.tex','.json','.md','.txt')]
    paths += ['out/checks/scan021_C_doubt_catalog.json']
    for reader in released:
        paths += [p.relative_to(BASE).as_posix() for p in sorted((BASE/f'out/readers/021/{reader}').iterdir())
                  if p.is_file() and p.suffix in ('.tex','.json','.md','.txt','.py','.diff','.patch')]
    sources, fingerprints, indices, parsed = {}, {}, {}, {}
    for path in paths:
        data = (BASE/path).read_bytes()
        text = data.decode('utf-8')
        fingerprints[path] = dict(sha256=sha(data), bytes=len(data))
        sources[path] = dict(complete_source=span(path,text))
        if path.endswith('.json'):
            parsed[path] = json.loads(text)
            indices[path] = json_spans(path,text)
            sources[path].update(value=parsed[path],top_level_sources={k:v for k,v in indices[path].items() if k.count('/')==1})
    readers, candidates, graphical_groups, issues = {}, [], [], []
    cp = 'packets/021/C_inventory.json'
    for i,row in enumerate(parsed[cp]):
        candidates.append(dict(reader='witness C',value=copy.deepcopy(row),source=indices[cp][f'/{i}'],selected=None,main_approved=False))
    for reader in released:
        rp=f'out/readers/021/{reader}/report.json'; tp=f'out/readers/021/{reader}/reading.tex'
        report=parsed[rp]; tt=read(tp); raw={}; extra={}
        for key,value in report.items():
            ptr='/'+key.replace('~','~0').replace('/','~1')
            if isinstance(value,list):
                raw[key]=[dict(value=copy.deepcopy(row),source=indices[rp][f'{ptr}/{i}']) for i,row in enumerate(value)]
            else:
                extra[key]=dict(value=copy.deepcopy(value),source=indices[rp][ptr])
        map_field={'A':'C_outcome_map','B':'actual_C_outcome_map','C':'actual_C_outcome_map'}[reader]
        original_maps=copy.deepcopy(raw[map_field])
        ap=f'out/readers/021/{reader}/source_audit.json'
        group_file={'A':'groups.json','B':'source_groups.json','C':'graphical_groups.json'}[reader]
        gp=f'out/readers/021/{reader}/{group_file}'
        group_sources={}
        group_field='/graphical_groups' if reader=='C' else '/groups'
        group_records=[(group_field,i,group) for i,group in enumerate(parsed[ap][group_field[1:]])]
        group_records.extend(('/nested_local_groups',i,group) for i,group in enumerate(parsed[ap].get('nested_local_groups',[])))
        for field,i,group in group_records:
            literal=group['reading_tex_exact_excerpt'] if reader=='C' else group['exact_source']
            assert tt.count(literal)==1,(reader,group['id'],'source occurrence')
            start=tt.index(literal)
            source=span(tp,tt,start,start+len(literal))
            if reader=='A':
                assert tt.encode()[group['start_byte_utf8']:group['end_byte_utf8_exclusive']].decode()==literal,(reader,group['id'],'byte range')
            elif reader=='B':
                assert tt[group['source_start_char']:group['source_end_char_exclusive']]==literal,(reader,group['id'],'character range')
            else:
                declared_start,declared_end=group['reading_tex_character_span']
                assert tt[declared_start:declared_end]==literal,(reader,group['id'],'character range')
                assert tt.count(group['source'])==1,(reader,group['id'],'raw source body')
            group_sources[group['id']]=source
            original_sources={}
            if field==group_field:
                original_group=[(j,g) for j,g in enumerate(parsed[gp]) if g['id']==group['id']]
                assert len(original_group)==1
                j,g=original_group[0]
                literal_key={'A':'tex_fragment','B':'exact_source','C':'reading_tex_exact_excerpt'}[reader]
                assert g[literal_key]==literal
                original_sources=dict(original_group_source=indices[gp][f'/{j}'],original_group_value=copy.deepcopy(g))
            graphical_groups.append(dict(reader=reader,group_id=group['id'],
                value=copy.deepcopy(group),source=indices[ap][f'{field}/{i}'],tex_source=source,
                **original_sources,selected=None,main_approved=False))
        reader_groups=[g for g in graphical_groups if g['reader']==reader]
        for group in reader_groups:
            s=group['tex_source']
            group['lexical_parent_groups']=[g['group_id'] for g in reader_groups if g['group_id']!=group['group_id']
                and g['tex_source']['char_start']<=s['char_start'] and g['tex_source']['char_end']>=s['char_end']]
            group['ownership_scope']='Source containment and original owner fields only; no geometric overlap computation.'
        if reader=='A':
            silent,readings=a_source_choices(tp,tt,report,group_sources)
            silent_path=rp;silent_field='/source_silent_choices'
        elif reader=='B':
            silent,readings=b_source_choices(tp,tt,report,parsed[ap],group_sources)
            silent_path=ap;silent_field='/report_silent_choices'
        else:
            silent,readings=c_source_choices(tp,tt,report,parsed[ap],group_sources)
            silent_path=ap;silent_field='/source_choices_including_report_silent'
        for i,row in enumerate(silent):
            row['report_source']=indices[silent_path][f'{silent_field}/{i}']
        readers[reader]=dict(report_path=rp,complete_report=sources[rp]['complete_source'],
            complete_tex=sources[tp]['complete_source'],complete_prose_audit=sources[f'out/readers/021/{reader}/reading.md']['complete_source'],
            original_top_level_keys=list(report),raw_rows=raw,extra_source_fields=extra,
            original_C_doubt_maps=original_maps,tex_index=tex_index(tp,tt),report_json_pointer_index=indices[rp],
            actual_tex_reading_sources=readings,reported_silent_choices_with_complete_TeX=silent,
            original_report_flags_preserved=True,
            source_audits={p:sources[p] for p in paths if p.startswith(f'out/readers/021/{reader}/') and p.endswith('.json') and ('audit' in p or 'check' in p)})
        for row in raw.get('inventory',[]):
            candidates.append(dict(reader=reader,**copy.deepcopy(row),selected=None,main_approved=False))
        if '$overset{' in tt:
            issue=literal_span(tp,tt,'$overset{')
            issues.append(dict(id='A021-SOURCE-01',kind='literal macro spelling',source=issue,
                observation='Original source has $overset{ without a backslash before overset.',
                action='Original preserved unchanged; root received this issue for selected-source assembly.',root_decision=None))
        display_blanks=[]
        for display in re.finditer(r'\\\[.*?\\\]',tt,re.S):
            for blank in re.finditer(r'(?m)^[ \t]*\n',display.group()):
                start=display.start()+blank.start();end=display.start()+blank.end()
                display_blanks.append(span(tp,tt,start,end))
        if display_blanks:
            issues.append(dict(id=f'{reader}021-SOURCE-DISPLAY-BLANKS',kind='physical blank lines inside display delimiters',
                sources=display_blanks,observation='Original complete source contains the listed physical blank lines inside display delimiters.',
                action='Original preserved unchanged; selected-source assembly must keep physical paragraph blanks outside math delimiters.',root_decision=None))
    catalog_path='out/checks/scan021_C_doubt_catalog.json';catalog=parsed[catalog_path]
    doubt_path='packets/021/C_doubts.txt';doubt_text=read(doubt_path);crosswalk=[]
    assert len(catalog['rows'])==catalog['actual_source_rows']==15
    for i,original in enumerate(catalog['rows']):
        assert doubt_text[original['char_start']:original['char_end']]==original['literal']
        row=copy.deepcopy(original)
        row['catalog_source']=copy.deepcopy(indices[catalog_path][f'/rows/{i}'])
        row['actual_table_source']=span(doubt_path,doubt_text,original['char_start'],original['char_end'])
        row['reader_original_maps']={};row['reader_difference_sources']={};row['reader_identifier_correspondence']={}
        for reader,source in readers.items():
            raw_field={'A':'raw_row','B':'raw_source_row','C':'raw_source_row'}[reader]
            part_field={'A':'physical_local_parts','B':'local_parts','C':'local_parts'}[reader]
            matches=[m for m in source['original_C_doubt_maps'] if m['value'][raw_field]==original['literal']]
            assert len(matches)==1,(reader,original['source_id'])
            m=matches[0];value=m['value']
            original_identifier=value['source_row_id'] if reader=='C' else value['id']
            assert original_identifier==original['source_id']
            row['reader_original_maps'][reader]=[copy.deepcopy(m)]
            row['reader_identifier_correspondence'][reader]=original_identifier
            ids=[p['difference_id'] for p in value[part_field]]
            diffs=[copy.deepcopy(d) for d in source['raw_rows']['differences'] if d['value']['id'] in ids]
            assert len(diffs)==len(ids)
            row['reader_difference_sources'][reader]=diffs
            row.setdefault('reader_actual_tex_sources',{})[reader]=[copy.deepcopy(source['actual_tex_reading_sources'][ident]) for ident in ids]
            related=value.get('related_component_rows',[])
            row.setdefault('reader_related_component_sources',{})[reader]=[
                copy.deepcopy(d) for d in source['raw_rows']['differences'] if d['value']['id'] in related]
        for part in row['source_parts']:
            part['original_decision_status']=part['decision_status']
            part['reader_source_ids']={r:[d['value']['id'] for d in row['reader_difference_sources'][r]] for r in released}
            part['root_status']=None;part['main_approved']=False
        crosswalk.append(row)
    ht=read('packets/021/H.tex');hp='packets/021/H.tex'
    placeholders=[]
    for i,m in enumerate(re.finditer(r'\\struck\{\\ill\{\}\}|\\ill\{\}',ht)):
        start=ht.rfind('\n',0,m.start())+1;end=ht.find('\n',m.end());end=len(ht) if end<0 else end
        placeholders.append(dict(id=f'H021-ILL-{i+1:02d}',source=span(hp,ht,m.start(),m.end()),
            enclosing_line=span(hp,ht,start,end),count_parent=None,main_approved=False))
    return dict(scan=21,scope='Source-only bookkeeping; no image view, ink/count decision, rendering, compilation, research or optional mathematical/coordinate computation.',
        released_readers=released,pending_readers=[r for r in 'ABC' if r not in released],main_adjudicated=False,
        source_fingerprints=fingerprints,sources=sources,source_categories=source_categories(doubt_path,doubt_text),
        witness_tex_indices={r:tex_index(f'packets/021/{r}.tex',read(f'packets/021/{r}.tex')) for r in 'CH'},
        H_shared_ill_placeholders=placeholders,reader_sources=readers,C_doubt_crosswalk=crosswalk,
        canonical_C_catalog=dict(path=catalog_path,sha256=fingerprints[catalog_path]['sha256'],actual_rows=15,actual_parts=15),
        candidate_inventory=candidates,candidate_graphical_groups=graphical_groups,source_issues=issues,
        recurring_Sigma_head_source_crosswalk=sigma_head_crosswalk(readers,graphical_groups) if released==list('ABC') else [],
        root_decisions_applied=False,root_decision_source='out/checks/scan021_main_decisions.md',
        source_indexer=dict(path='out/checks/scan021_prepare_sources.py',sha256=sha(Path(__file__).read_bytes())),
        preparation_history=['All work before explicit root post-checkpoint18 write release was read-only. Reader A alone was released for initial indexing.',
            'The initial source-indexer execution stopped during Python parsing because of one extra closing parenthesis; no staging output was written. That source typo was repaired before the successful A-only staging write.',
            'Reader B was added only after its explicit root release; original A/B returns remain unchanged.',
            'Reader C was added only after its explicit root release; original A/B/C returns remain unchanged.'],
        selection_status='Pending root; raw reader flags, counts, source outcomes and inventory transcribed values are original proposals.')


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--released',required=True)
    parser.add_argument('--final-union',action='store_true')
    args=parser.parse_args();released=list(args.released)
    if args.final_union:
        assert released==list('ABC')
    result=collect(released)
    name='scan021_source_union.json' if args.final_union else 'scan021_source_staging.json'
    (OUT/name).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    if args.final_union:
        readers=dict(scan=21,released_readers=released,
            files={p:dict(path=p,**v) for p,v in result['source_fingerprints'].items() if p.startswith('out/readers/021/')},
            scope='Released original text/JSON returns, original source-generation scripts and audits; no image bytes read or hashed.')
        (OUT/'scan021_reader_fingerprints.json').write_text(json.dumps(readers,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        fps=dict(scan=21,source_fingerprints=result['source_fingerprints'],source_union=dict(path='out/checks/'+name,sha256=sha((OUT/name).read_bytes())),
            selected_draft=None,selected_map=None,record_stage='Complete released source union; selected ink/count choices pending root.',root_approval_flags=False)
        (OUT/'scan021_source_fingerprints.json').write_text(json.dumps(fps,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(dict(output='out/checks/'+name,sha256=sha((OUT/name).read_bytes()),released=released,
        pending=result['pending_readers'],reader_source_rows={r:{k:len(v) for k,v in s['raw_rows'].items()} for r,s in result['reader_sources'].items()},
        candidate_inventory=len(result['candidate_inventory']),candidate_graphical_groups=len(result['candidate_graphical_groups']),source_issues=result['source_issues']),ensure_ascii=False))
