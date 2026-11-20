#!/usr/bin/env python3
"""Text-only source assembly for scan013, under explicit root decisions.

Reads source TeX/JSON/Markdown only. Opens no image and invokes no compiler,
renderer, OCR, package installer or research tool. Writes only the three
assigned draft/mapping/audit outputs beside this script. No page/record write.
"""
from pathlib import Path
from datetime import datetime, timezone
from decimal import Decimal
import hashlib
import json
import re

BASE = Path('/workspace/scratch/94548b74fbe0')
OUT = BASE / 'out/checks'
ROOT_LOG = OUT / 'scan013_main_decisions.md'
TEX = OUT / 'scan013_final_draft.tex'
MAP = OUT / 'scan013_tex_mapping.json'
AUDIT = OUT / 'scan013_tex_assembly.md'
reader_tex = {r: (BASE / f'out/readers/013/{r}/reading.tex').read_text() for r in 'ABC'}
reader_reports = {r: json.loads((BASE / f'out/readers/013/{r}/report.json').read_text()) for r in 'ABC'}
reader_prose = {r: (BASE / f'out/readers/013/{r}/reading.md').read_text() for r in 'ABC'}
packet = {n: (BASE / f'packets/013/{n}').read_text() for n in ['C.tex','H.tex','metadata.json','C_doubts.txt','C_notes.txt','C_inventory.json']}
root_log = ROOT_LOG.read_text()
preamble = (BASE / 'out/PREAMBLE.tex').read_text()
brief = (BASE / 'out/briefs/brief_v11_scan013.md').read_text()

def sha(s):
    return hashlib.sha256(s.encode()).hexdigest()

def line_span(s, start, end):
    return [s.count('\n', 0, start) + 1, s.count('\n', 0, end) + 1]

def matching_brace(s, start):
    assert s[start] == '{'
    depth = 1
    i = start + 1
    while i < len(s):
        if s[i] == '\\':
            i += 2
            continue
        if s[i] == '{':
            depth += 1
        elif s[i] == '}':
            depth -= 1
            if depth == 0:
                return i
        i += 1
    raise ValueError('unclosed group')

def commands(s, reader, offset=0):
    """Top-level TikZ statements, retaining literal bytes and local children.

    A node containing a local picture is one placement candidate. Every child
    statement is retained as a component with its own literal source pointer.
    """
    result = []
    pattern = re.compile(r'\\(node|draw|fill|path|useasboundingbox)\b')
    consumed = 0
    for m in pattern.finditer(s):
        if m.start() < consumed:
            continue
        before = s[s.rfind('\n', 0, m.start()) + 1:m.start()]
        if '%' in before:
            continue
        depth = 0
        i = m.start()
        while i < len(s):
            c = s[i]
            if c == '\\':
                i += 2
                continue
            if c == '{': depth += 1
            elif c == '}': depth -= 1
            elif c == ';' and depth == 0:
                i += 1
                break
            i += 1
        else:
            raise ValueError((reader, 'unterminated statement', m.start()))
        consumed = i
        body = s[m.start():i]
        whole = reader_tex[reader]
        start, end = offset + m.start(), offset + i
        l1, l2 = line_span(whole, start, end)
        prefix = whole[:start]
        comments = re.findall(r'^%+\s*(.*?)\s*$', prefix, re.M)
        comment = comments[-1] if comments else ''
        label = comment.split(':')[0].strip()
        node_name = re.search(r'\]\s*\(([^)]+)\)\s+at\s*\(', body)
        if node_name:
            label = node_name[1]
        candidate_id=f'{reader}:L{l1:03d}'+(f':C{start}' if offset else '')
        item = {'id': candidate_id, 'reader': reader,
                'path': f'out/readers/013/{reader}/reading.tex',
                'line_start': l1, 'line_end': l2,
                'char_start': start, 'char_end': end,
                'command': m[1], 'source_label': label,
                'source_comment': comment, 'tex_exact': body,
                'sha256': sha(body), 'groups': []}
        if m[1] == 'node':
            loc = re.search(r'\bat\s*\(([-.\d]+),([-.\d]+)\)\s*\{', body)
            if loc:
                opening = loc.end()-1
                close = matching_brace(body, opening)
                item['node_body_exact'] = body[opening+1:close]
                item['node_at_exact'] = [loc[1],loc[2]]
                item['node_body_offset'] = [opening+1, close]
                children = commands(body[opening+1:close], reader,
                                    start+opening+1)
                if children:
                    item['local_components'] = children
                    for child in children:child['parent_id']=candidate_id
                box = re.search(r'\\useasboundingbox\s*\(([-.\d]+),([-.\d]+)\)\s*rectangle\s*\(([-.\d]+),([-.\d]+)\)', body)
                if box:
                    item['local_declared_box_exact'] = list(box.groups())
        result.append(item)
    return result

candidates = {r:commands(s,r) for r,s in reader_tex.items()}
by_id = {v['id']:v for seq in candidates.values() for v in seq}
by_line = {r:{v['line_start']:v for v in seq} for r,seq in candidates.items()}
by_b_label = {v['source_label']:v for v in candidates['B']}
groups = {}

def gid(id, title=None):
    if id not in groups:
        groups[id] = {'id':id,'location':title or id,'candidate_ids':[],
                      'source_rows':[], 'selection':None}
    return groups[id]

def add_source(group, reader, lines):
    g = gid(group)
    for n in lines:
        item = by_line[reader][n]
        if item['id'] not in g['candidate_ids']:
            g['candidate_ids'].append(item['id'])
        if group not in item['groups']:
            item['groups'].append(group)
        for child in item.get('local_components',[]):
            if group not in child['groups']:child['groups'].append(group)

def bgroup(group, label=None, a=(), c=(), title=None):
    g=gid(group,title)
    v=by_b_label[label or group]
    add_source(group,'B',[v['line_start']])
    add_source(group,'A',a)
    add_source(group,'C',c)
    return g

def interval(group,reader,lo,hi):
    add_source(group,reader,[n for n in by_line[reader] if lo<=n<=hi])

# The numeric source coordinates share the readers' stated original-pixel frame.
# Source rendering scales remain recorded separately, never silently rewritten.
source_frames = {
 'A': {'x':'0.00635cm','y':'-0.00635cm','margin_separate':True},
 'B': {'x':'0.01cm','y':'-0.01cm','margin_separate':False},
 'C': {'x':'1pt','y':'-1pt','margin_separate':False}}

# Every uncontroversial manuscript word/date/label still has exact A/B/C bodies.
for i in range(1,7):
    bgroup(f'heading{i}',a=[41+i],c=[27+2*i])
    bgroup(f'notes-number{i}',a=[47+i],c=[39+2*i])
    bgroup(f'letter{i}',a=[87+i],c=[54+2*i])
    bgroup(f'date{i}',a=[93+i],c=[66+2*i])
for key,al,cl in [
 ('title1a',108,116),('title1b',109,118),('title1c',112,120),
 ('title2a',113,122),('title2b',114,124),('title2c',116,126),
 ('title3a',124,128),('title3b',125,130),('title4a',126,132),
 ('title4b',127,134),('title5a',128,136),('title5b',129,138),
 ('title6a',130,140),('lower-title1',205,179),('lower-title2',206,181),
 ('lower-title3',207,183),('lower-trans3',208,185),('lower-title4',209,187),
 ('lower-trans4',210,189),('lower-title5',211,191),('lower-trans5',212,193),
 ('lower-title6',213,195)]:
    bgroup(key,a=[al],c=[cl])
for i,cl in enumerate([163,165,169,173,175,177],1):
    bgroup(f'live-sub{i}',a=[198+i],c=[cl])
for i in range(1,7):
    bgroup(f'foot{i}',a=[229+i],c=[195+2*i])
bgroup('cancelled-date',a=[55],c=[53])
bgroup('old-A',a=[85],c=[55])
bgroup('old-C-Ca',a=[115],c=[126])
bgroup('upper-question',a=[17],c=[94])
bgroup('lower-question',a=[191],c=[154])
bgroup('old-sub-A',a=[196],c=[161])
bgroup('old-sub-C-left',a=[197],c=[167])
bgroup('old-sub-D',a=[198],c=[171])
for tag,al,cl in [('A',132,142),('B',144,144),('C',154,146),('D',162,148),('E20',172,150),('E23',182,152)]:
    bgroup('cancel-'+tag,a=[al],c=[cl])
    gid('hatch-'+tag,'oblique hatching over subdivision '+tag)
    for v in candidates['B']:
        if v['source_label'].startswith('hatch-'+tag+'-'):
            add_source('hatch-'+tag,'B',[v['line_start']])
for tag,lo,hi in [('A',134,142),('B',146,152),('C',156,160),('D',164,170),('E20',174,180),('E23',184,190)]:
    interval('hatch-'+tag,'A',lo,hi)
for r,lo,hi in [('A',57,83),('B',72,100)]:
    interval('cancelled-date-hatching',r,lo,hi)

# Twelve horizontal-rule positions and the separately disputed vertical traces.
for i,bl in enumerate([123,209,285,555,639,752,839,930,1089,1204,1299,1564],1):
    bgroup(f'rule-h{i:02d}',f'G-grid-horizontal-{bl}',a=[26+i],c=[9+i])
for r,lo,hi in [('A',40,41),('B',10,18),('C',22,22)]:
    interval('rule-verticals',r,lo,hi)
bgroup('rule-lower-thickening','G-grid-thickening-2227',a=[228])
add_source('rule-live-thickening','A',[229])

# The left marginal drawing is represented inside the common page frame.
for r,lo,hi in [('A',8,20),('B',134,154),('C',81,91)]:
    interval('margin-core',r,lo,hi)
# Question text is an independent body in the same cluster.
for v in by_id.values():
    if v['id'] in groups['upper-question']['candidate_ids'] and 'margin-core' in v['groups']:
        v['groups'].remove('margin-core')
        groups['margin-core']['candidate_ids'].remove(v['id'])

bgroup('G-margin-point',a=[22],c=[96])
bgroup('G-old-A-curves',a=[86,87])
bgroup('G-bent-upper',a=[101],c=[100])
bgroup('G-bent-lower',a=[102],c=[101])
bgroup('G-bent-lower-retrace',a=[103],c=[102])
bgroup('G-bent-upper-arch',a=[105],c=[104])
bgroup('G-bent-upper-dash',a=[106],c=[108])
bgroup('G-bent-upper-dot',a=[107],c=[112])
bgroup('G-date-hook',c=[245])
add_source('title1-residuals','A',[111])
add_source('title1-residuals','C',[25])
bgroup('G-Reveil-diagonal',a=[119,120,121,122,123])
add_source('Cascades-hook','A',[117])
bgroup('G-Baumeister-upper-gray',c=[255])
bgroup('G-Baumeister-upper-black',c=[259])
bgroup('G-Baumeister-left-gray',c=[264])
bgroup('G-Baumeister-right-gray')
bgroup('cancel-C-terminal-hook')
bgroup('cancel-E23-terminal-hook')
bgroup('G-cancel-C-gray-point')
bgroup('G-lower-A-arrow',a=[193],c=[156])
bgroup('G-lower-B-arrow',a=[195],c=[158,159])
bgroup('G-live-C-gray-dot')
bgroup('G-live-C-right-curve')
bgroup('G-long-dot',a=[215],c=[220])
bgroup('G-Jeu-overmark')
bgroup('G-Spiel-lower-spot')
bgroup('G-A-blank-trace',a=[217,218,219],c=[224])
bgroup('G-A-foot-trace',a=[221,222,223,224],c=[230])
bgroup('G-E23-dash',a=[227],c=[272])
bgroup('G-E20-blot',a=[226],c=[250])
bgroup('G-D-point')
bgroup('G-A-edge-slant',c=[236])
add_source('G-Decouverte-point','C',[268])
for i in range(1,11):
    bgroup(f'G-edge-{i:02d}',a=[235+2*i],c=[208+i])
gid('archive-number','archive number 12, comment-only')
for r,lines in [('A',[6,25]),('B',[7]),('C',[7])]:
    add_source('render-frame',r,lines)

# Compact physical-group mapping for every source report difference.
local14 = ['old-A','title1c','old-C-Ca','cancel-A','cancel-B','cancel-C',
           'cancel-D','cancel-E20','cancel-E23','lower-question','old-sub-D',
           'lower-title2','old-sub-A','old-sub-C-left']
diff_groups = {r:{} for r in 'ABC'}
for r in 'ABC':
    for d,g in zip(reader_reports[r]['differences'][:14],local14):
        diff_groups[r][d['id']] = [g]
for r in 'AB':
    diff_groups[r][reader_reports[r]['differences'][0]['id']] += ['G-old-A-curves']
for r in 'AB':
    for j,t in enumerate(['A','B','C','D','E20','E23'],3):
        diff_groups[r][reader_reports[r]['differences'][j]['id']] += ['hatch-'+t]
diff_groups['B']['B-C09'] += ['cancel-E23-terminal-hook']
diff_groups['B']['B-C13b'] += ['G-live-C-gray-dot','G-live-C-right-curve']
grid_ids = [f'rule-h{i:02d}' for i in range(1,13)]+['rule-verticals']
edges = [f'G-edge-{i:02d}' for i in range(1,11)]
diff_groups['A'].update({
 'A-G01':grid_ids,'A-G02':['cancelled-date','cancelled-date-hatching'],
 'A-G03':['margin-core','upper-question'],'A-G04':['G-margin-point'],
 'A-G05':['G-bent-upper','G-bent-lower','G-bent-lower-retrace'],
 'A-G06':['G-bent-upper-arch','G-bent-upper-dash','G-bent-upper-dot'],
 'A-G07':['title1-residuals'],'A-G08':['G-Reveil-diagonal'],
 'A-G09':['G-long-dot'],'A-G10':['G-A-blank-trace'],'A-G11':['G-A-foot-trace'],
 'A-G12':['G-E20-blot'],'A-G13':['G-E23-dash'],'A-G14':['rule-lower-thickening'],
 'A-G15':['rule-live-thickening'],'A-G16':edges,
 'A-G17':['G-lower-A-arrow','G-lower-B-arrow'],
 'A-G18':['old-C-Ca','Cascades-hook'],
 'A-G19':['cancel-A','hatch-A'],'A-G20':['cancel-C','hatch-C'],
 'A-G21':['cancel-E20','hatch-E20'],'A-G22':['cancel-E23','hatch-E23']})
diff_groups['B'].update({
 'B-G01':grid_ids+['rule-lower-thickening'],
 'B-G02':['cancelled-date','cancelled-date-hatching'],
 'B-G03':['margin-core','upper-question'],
 'B-G04':['G-bent-upper','G-bent-lower','G-bent-lower-retrace',
          'G-bent-upper-arch','G-bent-upper-dash','G-bent-upper-dot'],
 'B-G05':['G-lower-A-arrow'],'B-G06':['G-lower-B-arrow'],
 'B-G07':['G-margin-point'],'B-G08':['G-date-hook'],
 'B-G09':['G-Reveil-diagonal'],'B-G10':['G-Baumeister-upper-gray'],
 'B-G11':['G-Baumeister-upper-black'],'B-G12':['G-Baumeister-left-gray'],
 'B-G13':['G-Baumeister-right-gray'],'B-G14':['G-cancel-C-gray-point'],
 'B-G15':['G-long-dot'],'B-G16':['G-Jeu-overmark'],'B-G17':['G-Spiel-lower-spot'],
 'B-G18':['G-A-blank-trace'],'B-G19':['G-A-foot-trace'],
 'B-G20':['G-E23-dash'],'B-G21':['G-E20-blot'],'B-G22':['G-D-point'],
 'B-G23':['G-A-edge-slant']})
diff_groups['C'].update({
 'C013.d15':['old-sub-A'],'C013.g15':['margin-core','upper-question','G-margin-point'],
 'C013.g16':['G-bent-upper','G-bent-lower','G-bent-lower-retrace',
             'G-bent-upper-arch','G-bent-upper-dash','G-bent-upper-dot'],
 'C013.g02':['title1-residuals'],'C013.g12':['G-long-dot'],
 'C013.edge5':['G-edge-05'],'C013.edge10':['G-edge-10'],
 'C013.g23':['G-A-blank-trace'],'C013.g24':['G-A-foot-trace'],
 'C013.g25':['G-A-edge-slant'],'C013.g26':['G-date-hook'],
 'C013.g27':['G-E20-blot'],'C013.g29':['G-Decouverte-point'],
 'C013.g28a':['G-Baumeister-upper-gray'],'C013.g28b':['G-Baumeister-upper-black'],
 'C013.g28c':['G-Baumeister-left-gray'],'C013.gHalfB':['G-E23-dash'],
 'C013.g10':['G-lower-A-arrow'],'C013.g30':['G-lower-B-arrow']})

def common_inventory(index):
    """The first 49 A/C entries preserve packet inventory order exactly."""
    if index==0: return grid_ids
    if index==1: return edges
    if 2<=index<=7: return [f'heading{index-1}',f'notes-number{index-1}']
    if index==8: return ['cancelled-date','cancelled-date-hatching']
    if index==9: return ['margin-core','upper-question']
    if index==10: return ['old-A','G-old-A-curves']
    if 11<=index<=16: return [f'letter{index-10}',f'date{index-10}']
    if index==17: return ['G-bent-upper','G-bent-lower','G-bent-lower-retrace']
    if 18<=index<=23:
        col=index-17
        return [f'title{col}{x}' for x in ({1:'abc',2:'abc',3:'ab',4:'ab',5:'ab',6:'a'}[col])]
    if index==24: return ['old-C-Ca','Cascades-hook']
    if 25<=index<=30:
        t=['A','B','C','D','E20','E23'][index-25]
        return ['cancel-'+t,'hatch-'+t]
    if index==31: return ['lower-question','G-lower-A-arrow']
    if index==32: return ['G-lower-B-arrow']
    if 33<=index<=35: return [['old-sub-A'],['old-sub-C-left','G-live-C-gray-dot','G-live-C-right-curve'],['old-sub-D']][index-33]
    if 36<=index<=41:
        c=index-35
        return [f'live-sub{c}',f'lower-title{c}']+([f'lower-trans{c}'] if c in [3,4,5] else [])
    if 42<=index<=47: return [f'foot{index-41}']
    if index==48: return ['archive-number']
    raise KeyError(index)

inventory_groups={r:{} for r in 'ABC'}
for r in 'AC':
    for i in range(49): inventory_groups[r][i]=common_inventory(i)
a_extra=[grid_ids[:-1],['rule-verticals'],['G-old-A-curves'],['title1-residuals'],
 ['G-margin-point'],['margin-core'],['G-bent-upper-arch','G-bent-upper-dash','G-bent-upper-dot'],
 ['G-Reveil-diagonal'],['G-long-dot'],['G-A-blank-trace'],['G-A-foot-trace'],
 ['G-E20-blot'],['G-E23-dash'],['rule-lower-thickening'],['rule-live-thickening']]
c_extra=[['title1-residuals'],['G-margin-point'],['G-bent-upper-arch'],
 ['G-bent-upper-dash'],['G-bent-upper-dot'],['G-long-dot'],['G-A-blank-trace'],
 ['G-A-foot-trace'],['G-A-edge-slant'],['G-date-hook'],['G-E20-blot'],
 ['G-Baumeister-upper-gray'],['G-Baumeister-upper-black'],['G-Baumeister-left-gray'],
 ['G-Decouverte-point'],['G-E23-dash']]
for r,seq in [('A',a_extra),('C',c_extra)]:
    for i,g in enumerate(seq,49): inventory_groups[r][i]=g
for i,item in enumerate(reader_reports['B']['inventory']):
    e=item['element']
    short=e.removeprefix('B013.')
    if short=='table': gs=grid_ids+['rule-lower-thickening']
    elif re.fullmatch(r'heading[1-6]',short):
        n=short[-1]; gs=[short,'notes-number'+n]
    elif short=='cancelled-date': gs=['cancelled-date','cancelled-date-hatching']
    elif short.startswith('letter-date'):
        n=short[-1];gs=['letter'+n,'date'+n]
    elif short=='margin': gs=['margin-core','upper-question']
    elif short=='bent-arrows': gs=['G-bent-upper','G-bent-lower','G-bent-lower-retrace']
    elif re.fullmatch(r'title[1-6]',short):
        n=int(short[-1]);gs=[short+x for x in {1:'abc',2:'abc',3:'ab',4:'ab',5:'ab',6:'a'}[n]]
    elif short in ['cancel-A','cancel-B','cancel-C','cancel-D','cancel-E20','cancel-E23']:
        gs=[short,short.replace('cancel-','hatch-')]
    elif short in ['cancel-C-hook','cancel-E23-hook']:
        gs=[short.replace('-hook','-terminal-hook')]
    elif short=='lower-question-arrow': gs=['lower-question','G-lower-A-arrow']
    elif short=='lower-B-arrow': gs=['G-lower-B-arrow']
    elif re.fullmatch(r'lower-title[1-6]',short):
        n=short[-1];gs=[short]+(['lower-trans'+n] if n in '345' else [])
    elif short.startswith('edge'):gs=['G-edge-'+short[4:]]
    elif short=='archive':gs=['archive-number']
    else: gs=[short]
    inventory_groups['B'][i]=gs

doubt_groups={r:{} for r in 'ABC'}
a_u=['old-A','old-C-Ca','cancel-A','cancel-C','cancel-E20','cancel-E23','old-sub-D','old-sub-A','old-sub-C-left']
for i,g in enumerate(a_u):doubt_groups['A'][i]=[g]
for i,d in enumerate(reader_reports['A']['doubts'][9:],9):
    doubt_groups['A'][i]=diff_groups['A'][d['id'].removeprefix('U-role-')]
for r in 'BC':
    for i,d in enumerate(reader_reports[r]['doubts']):
        name=d['id'].removesuffix('-role')
        doubt_groups[r][i]=diff_groups[r].get(name,[name])

crosswalk={k:[] for k in ['differences','doubts','inventories','packet_inventory','C_source_doubts']}
def source_row(r,kind,i,gs):
    source=reader_reports[r][kind][i]
    key='inventories' if kind=='inventory' else kind
    row={'reader':r,'path':f'out/readers/013/{r}/report.json',
         'pointer':f'/{kind}/{i}','source_id':source.get('id',source.get('element')),
         'sha256':sha(json.dumps(source,ensure_ascii=False,sort_keys=True)),
         'groups':gs, 'candidate_ids':[]}
    for g in gs:
        if g not in groups:
            raise KeyError((r,kind,i,g))
        own=[c for c in groups[g]['candidate_ids'] if c.startswith(r+':')]
        row['candidate_ids'].extend(c for c in own if c not in row['candidate_ids'])
        groups[g]['source_rows'].append({'reader':r,'pointer':row['pointer'],'source_id':row['source_id']})
    crosswalk[key].append(row)
for r in 'ABC':
    for i,d in enumerate(reader_reports[r]['differences']):source_row(r,'differences',i,diff_groups[r][d['id']])
    for i,d in enumerate(reader_reports[r]['doubts']):source_row(r,'doubts',i,doubt_groups[r][i])
    for i,d in enumerate(reader_reports[r]['inventory']):source_row(r,'inventory',i,inventory_groups[r][i])

packet_inventory=json.loads(packet['C_inventory.json'])
if isinstance(packet_inventory,dict):
    packet_inventory=packet_inventory.get('inventory',packet_inventory.get('items'))
for i,row in enumerate(packet_inventory):
    crosswalk['packet_inventory'].append({'path':'packets/013/C_inventory.json',
       'pointer':f'/{i}','source_id':row.get('element'),'groups':common_inventory(i),
       'sha256':sha(json.dumps(row,ensure_ascii=False,sort_keys=True))})
source_doubt_map=json.loads((OUT/'scan013_source_map.json').read_text())
for row in source_doubt_map['source_doubt_rows']:
    n=row['source_row']
    gs=[local14[n-1]] if n<13 else ['old-sub-A','old-sub-C-left']
    crosswalk['C_source_doubts'].append({'source_row':n,'path':'packets/013/C_doubts.txt',
      'line':row['source_line'],'exact':row['exact'],'groups':gs,
      'local_loci':2 if n==13 else 1})

# Exact packet-TeX line bodies provide a source correspondence for every label,
# date, title, reference, qualification and physical right-edge fragment.
packet_line_groups={
 2:['margin-core','upper-question'],
 7:[f'heading{i}' for i in range(1,7)],
 8:[f'notes-number{i}' for i in range(1,7)],
 9:['cancelled-date'],10:['old-A']+[f'letter{i}' for i in range(1,7)],
 11:[f'date{i}' for i in range(1,7)],
 12:['G-bent-upper'],13:['G-bent-lower'],
 14:[f'title{i}a' for i in range(1,7)],15:['title1b','title2b'],
 16:['title1c'],17:['old-C-Ca','title2c'],
 18:['title3b','title4b','title5b'],
 19:['cancel-A','cancel-B'],20:['cancel-C','cancel-D'],
 21:['cancel-E20','cancel-E23'],22:['lower-question','G-lower-A-arrow','G-lower-B-arrow'],
 23:['old-sub-A','old-sub-C-left','old-sub-D']+[f'live-sub{i}' for i in range(1,7)],
 24:['lower-title1','lower-title2','lower-title3'],
 25:['lower-title4','lower-title5','lower-title6'],
 26:['lower-trans3','lower-trans4','lower-trans5'],
 27:['foot1','foot2','foot3'],28:['foot4','foot5'],29:['foot6'],
 45:['archive-number']}
packet_tex_lines=packet['C.tex'].splitlines()
packet_tex_correspondence=[]
for line,gs in packet_line_groups.items():
    packet_tex_correspondence.append({'path':'packets/013/C.tex','line':line,
       'tex_exact':packet_tex_lines[line-1],'groups':gs,
       'sha256':sha(packet_tex_lines[line-1])})
edge_components=next(d['components'] for d in reader_reports['A']['differences'] if d['id']=='A-G16')
for i,component in enumerate(edge_components,1):
    exact=component['C_source_path']
    assert packet['C.tex'].count(exact)==1,exact
    start=packet['C.tex'].index(exact)
    packet_tex_correspondence.append({'path':'packets/013/C.tex',
       'line':packet['C.tex'].count('\n',0,start)+1,
       'tex_exact':exact,'groups':[f'G-edge-{i:02d}'],'sha256':sha(exact)})

# Selection entries are added below only after explicit root-log directions.
sections={}
starts=list(re.finditer(r'^(?:##\s+)?(\d+(?:[–-]\d+)?)\.\s+',root_log,re.M))
for i,m in enumerate(starts):
    end=starts[i+1].start() if i+1<len(starts) else len(root_log)
    sections[m[1]]=root_log[m.start():end].strip()

selections={}

def select(group,entry,reader=None,source_lines=None,source_ids=None,body=None,note='',qualification=None):
    assert entry in sections,(group,entry)
    g=groups[group]
    ids=[v for v in g['candidate_ids'] if reader and v.startswith(reader+':')]
    if source_lines is not None:
        ids=[by_line[reader][n]['id'] for n in source_lines]
        assert all(v in g['candidate_ids'] for v in ids),(group,ids)
    if source_ids is not None:
        ids=source_ids
        assert all(v in g['candidate_ids'] for v in ids),(group,ids)
    if body is None:
        body='\n'.join(by_id[v]['tex_exact'] for v in ids)
    assert body.strip(),group
    s={'root_entry':entry,'root_entry_sha256':sha(sections[entry]),
       'candidate_ids':ids,'tex_body':body,'note':note,
       'qualification':qualification,'status':'root-selected; final-page approval pending'}
    selections[group]=s
    g['selection']=s

transforms=[]

def dimensional_to_B(body,reader):
    """Exact unit map for source pen dimensions in the common B coordinate frame.

    A: (0.01 cm)/(0.00635 cm) = 200/127.
    C: (0.01 cm)/(1 pt) = 7227/25400, using 1 in=2.54 cm=72.27 pt.
    Numeric pixel coordinates are untouched. TeX performs the explicit rational
    dimension multiplication; no decimal pen-width substitution is introduced.
    """
    if reader=='B':return body
    num,den=(200,127) if reader=='A' else (7227,25400)
    def replace(m):
        return r'\dimexpr '+m[1]+m[2]+'*'+str(num)+'/'+str(den)+r'\relax'
    return re.sub(r'(?<![\w.])([.\d]+)(pt|cm)\b',replace,body)

def fixed_uncertain_full(body,reader,box,empty=False):
    """Literal full-pixel paths with a fixed local uncertainty origin.

    Inner map (u,v)->(u-x0,v-y0); outer map adds (x0,y0).
    Their composition fixes every source point, control point and endpoint.
    """
    x0,y0,x1,y1=box
    rendered=dimensional_to_B(body,reader)
    tail='|{}' if empty else ''
    wrapper=(rf'\node[anchor=base west,inner sep=0pt,outer sep=0pt] at ({x0},{y0}) '+'{'+
      r'\unsure{\begin{tikzpicture}[baseline={(0,0)},x=.01cm,y=-.01cm,line cap=round,line join=round]'+'\n'+
      rf'\useasboundingbox (0,0) rectangle ({x1-x0},{y1-y0});'+'\n'+
      r'\begin{pgfinterruptboundingbox}'+'\n'+
      rf'\begin{{scope}}[shift={{(-{x0},-{y0})}},draw=black,fill=black]'+'\n'+rendered+'\n'+
      r'\end{scope}'+'\n'+r'\end{pgfinterruptboundingbox}'+'\n'+
      r'\end{tikzpicture}'+tail+'}};')
    transforms.append({'reader':reader,'source_body_sha256':sha(body),
      'kind':'fixed full-to-local-to-full placement', 'origin':[x0,y0],
      'box':box,'coordinate_map':f'(u,v) -> (u-{x0},v-{y0}) -> (u,v)',
      'pen_dimension_ratio':'1' if reader=='B' else ('200/127' if reader=='A' else '7227/25400'),
      'empty_alternative':empty,'rendered_body_sha256':sha(wrapper)})
    return wrapper

def source_body(group,reader):
    return '\n'.join(by_id[x]['tex_exact'] for x in groups[group]['candidate_ids'] if x.startswith(reader+':'))

def fixed_B_local(group,extra_full_paths=''):
    item=next(by_id[x] for x in groups[group]['candidate_ids'] if x.startswith('B:'))
    assert 'local_components' in item and 'local_declared_box_exact' in item
    x,y=map(Decimal,item['node_at_exact'])
    x0,y0,w,h=map(Decimal,item['local_declared_box_exact'])
    assert x0==y0==0
    origin=[x,y-h]
    body='\n'.join(v['tex_exact'] for v in item['local_components'] if v['command']!='useasboundingbox')
    # Local coordinates remain literal; only the explicit origin and baseline
    # replace the bbox-dependent source placement. B's inventory gives this box.
    if extra_full_paths:
        body+='\n'+rf'\begin{{scope}}[shift={{(-{origin[0]},-{origin[1]})}}]'+'\n'+extra_full_paths+'\n'+r'\end{scope}'
    wrapper=(rf'\node[anchor=base west,inner sep=0pt,outer sep=0pt] at ({origin[0]},{origin[1]}) '+'{'+
      r'\unsure{\begin{tikzpicture}[baseline={(0,0)},x=.01cm,y=-.01cm,line cap=round,line join=round]'+'\n'+
      rf'\useasboundingbox (0,0) rectangle ({w},{h});'+'\n'+
      r'\begin{pgfinterruptboundingbox}'+'\n'+body+'\n'+
      r'\end{pgfinterruptboundingbox}'+'\n'+r'\end{tikzpicture}}};')
    transforms.append({'reader':'B','source_id':item['id'],
       'kind':'fixed local origin from declared B box','source_at':item['node_at_exact'],
       'source_declared_box':item['local_declared_box_exact'],
       'origin':[str(v) for v in origin],
       'coordinate_map':f'(u,v) -> ({origin[0]}+u,{origin[1]}+v)',
       'literal_child_source_ids':[v['id'] for v in item['local_components'] if v['command']!='useasboundingbox'],
       'pen_dimension_ratio':'1','rendered_body_sha256':sha(wrapper)})
    return wrapper

def fixed_C_local(group,origin,size):
    item=next(by_id[x] for x in groups[group]['candidate_ids'] if x.startswith('C:'))
    assert [Decimal(v) for v in item['node_at_exact']]==[Decimal(v) for v in origin]
    body='\n'.join(v['tex_exact'] for v in item['local_components'] if v['command']!='useasboundingbox')
    wrapper=(rf'\node[anchor=base west,inner sep=0pt,outer sep=0pt] at ({origin[0]},{origin[1]}) '+'{'+
      r'\unsure{\begin{tikzpicture}[baseline={(0,0)},x=.01cm,y=-.01cm,line cap=round,line join=round]'+'\n'+
      rf'\useasboundingbox (0,0) rectangle ({size[0]},{size[1]});'+'\n'+
      r'\begin{pgfinterruptboundingbox}'+'\n'+dimensional_to_B(body,'C')+'\n'+
      r'\end{pgfinterruptboundingbox}'+'\n'+r'\end{tikzpicture}}};')
    transforms.append({'reader':'C','source_id':item['id'],'kind':'root-explicit local origin',
       'origin':origin,'local_body_exact':body,
       'coordinate_map':f'(u,v) -> ({origin[0]}+u,{origin[1]}+v)',
       'pen_and_radius_dimension_ratio':'7227/25400','rendered_body_sha256':sha(wrapper)})
    return wrapper

def select_literal(group,entry,reader,note='',qualification=None):
    body=source_body(group,reader)
    select(group,entry,reader=reader,body=dimensional_to_B(body,reader),
       note=note or f'{reader} literal source body in the B frame; pixel coordinates unchanged.',
       qualification=qualification)

def represented_within(group,entry,target,note):
    select(group,entry,reader='B',body=f'% {group}: source component evidence represented within {target}; no separate path.',
      note=note)
    selections[group]['status']='component evidence represented within selected form'
    selections[group]['represented_within']=target

# ROOT-SELECTED ASSEMBLY INSERTION POINT
if '01–10' in sections:
    entry='01–10'
    assert 'A\'s R01–R12 coordinates' in sections[entry]
    for i in range(1,13):
        name=f'rule-h{i:02d}'
        body=source_body(name,'A')
        note='A literal coordinate path; common-frame pen dimensions mapped by 200/127.'
        qualification=None
        if i==3:
            assert '(30,286)--(357,288)' in body
            body=body.replace('(30,286)--(357,288)','(30,286)--(620,288)')
            rendered=fixed_uncertain_full(body,'A',[30,286,2340,292])
            note+=' Root extends only the first visible span endpoint from (357,288) to (620,288). Right span retained literally.'
            qualification='low confidence in pale endpoints and intervening continuation'
        elif i==8:
            rendered=fixed_uncertain_full(body,'A',[23,928,2338,934])
            note+=' Three source spans retained under local uncertainty.'
            qualification='medium confidence; continuity qualified'
        else:
            rendered=dimensional_to_B(body,'A')
        select(name,entry,reader='A',body=rendered,note=note,qualification=qualification)
    vparts=[]
    vids=[]
    vcomponents=[]
    for reader,line,box,empty in [
      ('A',40,[391,195,410,1664],False),('A',41,[1565,23,1575,1666],False),
      ('B',12,[790,207,792,1667],True),('B',14,[1184,207,1186,1667],True),
      ('B',18,[1967,207,1970,1667],True)]:
        item=by_line[reader][line]
        body=item['tex_exact']
        if reader=='B':
            assert 'black!18' in body
            body=body.replace('black!18','black!8')
        vparts.append(fixed_uncertain_full(body,reader,box,empty))
        vids.append(item['id'])
        vcomponents.append({'source_id':item['id'],'origin':box[:2],
             'confidence':'low' if empty else 'medium',
             'empty_alternative':empty,'root_tone':'black!8' if empty else None})
    select('rule-verticals',entry,source_ids=vids,body='\n'.join(vparts),
      note='A V01/V02 plus only B x792/x1186/x1967, the latter black!8 with an explicit empty alternative; no B x403/x1566 duplicate.',
      qualification='hand, surface origin and function unresolved; component extent/continuity qualified')
    selections['rule-verticals']['components']=vcomponents

if '11' in sections:
    select_literal('old-A','11','A',qualification='A glyph resolved; deleted/live state remains explicit')
    body=source_body('G-old-A-curves','A')
    select('G-old-A-curves','11',reader='A',
      body=fixed_uncertain_full(body,'A',[173,555,234,585]),
      note='Both A exterior curves, exact control points; each remains separate.',
      qualification='medium shape confidence; role/hand/surface origin unresolved')
if '12' in sections:
    select_literal('title1c','12','B',note='Exact B body Méditation; root resolves the singular ending.')
    body=source_body('title1-residuals','A')
    assert '(141,790)--(149,837) (164,792)--(168,823)' in body
    body=body.replace('(141,790)--(149,837) (164,792)--(168,823)',
                      '(137,749)--(141,790)--(149,837) (160,749)--(164,792)--(168,823)')
    select('title1-residuals','12',reader='A',
      body=fixed_uncertain_full(body,'A',[137,749,292,837]),
      note='A five subpaths; root prepends (137,749) and (160,749) only to the first two. R07 remains separate and unique.',
      qualification='medium visible shape; low character/state/origin; first two paths reach the inspected upper boundary')
if '13' in sections:
    select_literal('old-C-Ca','13','B',note='Exact cancelled C|Ca body; deleted annotation remains inside phantom.',
      qualification='medium reading confidence; C|Ca retained')
    select_literal('Cascades-hook','13','A',note='A entrance/return curve exact at (497,833) through its source controls to (514,839).')
    body=source_body('G-Reveil-diagonal','A')
    select('G-Reveil-diagonal','13',reader='A',body=fixed_uncertain_full(body,'A',[500,694,558,749]),
      note='Five literal A commands carry six components: last draw command contains two disconnected slants. No B duplicate.',
      qualification='cancellation role, hand and surface origin unresolved; Réveil remains live')
    selections['G-Reveil-diagonal']['components']=[
      {'source_id':'A:L119','subpath':'entire fill'},
      {'source_id':'A:L120','subpath':'entire draw'},
      {'source_id':'A:L121','subpath':'entire draw'},
      {'source_id':'A:L122','subpath':'entire fill'},
      {'source_id':'A:L123','subpath':'(549,739)--(552,742)'},
      {'source_id':'A:L123','subpath':'(554,744)--(558,749)'}]
if '14' in sections:
    select_literal('cancel-A','14','B',qualification='crossed i candidate retained; medium confidence')
    select_literal('hatch-A','14','A',note='A XA.H1–H5: five approximation commands, without a pen-stroke-count assertion.')
    select_literal('lower-question','14','B',note='Exact B question-mark body, resolved by root with high confidence.')
    select('G-lower-A-arrow','14',reader='A',
      body=fixed_uncertain_full(source_body('G-lower-A-arrow','A'),'A',[149,910,176,1001]),
      note='Exact A L01 hooked entry, curved shaft and downward point.',
      qualification='medium geometry confidence; role/hand unresolved')
if '15' in sections:
    select_literal('cancel-B','15','A',qualification='crossed ii resolved; medium confidence')
    select_literal('hatch-B','15','A',note='Four literal A XB hatch commands.')
    assert 'starts at (526,984)' in root_log
    select('G-lower-B-arrow','15',reader='C',
      body=fixed_uncertain_full(source_body('G-lower-B-arrow','C'),'C',[526,984,542,1055]),
      note='Exact C G30 two commands; source-only addendum withdraws y937 and selects (526,984) as the first endpoint. C pen dimension ratio 7227/25400.',
      qualification='medium geometry confidence; role/hand unresolved')
    selections['G-lower-B-arrow']['supplemental_root_entries']=['24']
if '16' in sections:
    select_literal('cancel-C','16','B',qualification='i|ii retained; medium confidence')
    select_literal('hatch-C','16','B',note='Four literal B hatch-C commands, including the low fourth run.')
    select_literal('cancel-C-terminal-hook','16','B')
    select('G-cancel-C-gray-point','16',reader='B',body=fixed_B_local('G-cancel-C-gray-point'),
      note='Exact B local polygon at its declared full origin (938,892).',
      qualification='medium shape; low role/hand/origin confidence')
if '17' in sections:
    select_literal('cancel-D','17','A',qualification='i resolved; medium confidence')
    select_literal('hatch-D','17','A',note='Four literal A XD hatch commands, including the low fourth slant.')
if '18' in sections:
    select_literal('cancel-E20','18','A',qualification='i|ii retained; medium confidence')
    select_literal('hatch-E20','18','A',note='Four literal A XE20 hatch commands, including the low fourth run.')
if '19' in sections:
    select_literal('cancel-E23','19','B',qualification='iii|iv with low confidence; qualified primary reversal retains C iv alternative')
    select_literal('hatch-E23','19','B',note='Four literal B hatch-E23 commands.')
    select_literal('cancel-E23-terminal-hook','19','B')
if '20' in sections:
    select_literal('old-sub-A','20','A',qualification='pale lower i glyph resolved; deleted/live state retained')
if '21' in sections:
    select_literal('old-sub-C-left','21','A',qualification='full (i)|( alternatives plus cancelled/live qualification, exact A nesting')
    represented_within('G-live-C-gray-dot','21','old-sub-C-left',
       'B raised gray stroke is component evidence for the selected A fuller pale form; no second graphical copy.')
    represented_within('G-live-C-right-curve','21','old-sub-C-left',
       'B right curve is component evidence for the selected A fuller pale form; no second graphical copy.')
if '22' in sections:
    select_literal('old-sub-D','22','A',qualification='upper displaced (i) glyph resolved high; deleted/live state remains qualified medium')
if '23' in sections:
    select_literal('lower-title2','23','B',note='Exact full B body Vers un plus long Voyage; plus resolved high.')
    select('G-long-dot','23',reader='A',
      body=fixed_uncertain_full(source_body('G-long-dot','A'),'A',[590,1237,596,1243]),
      note='Exact A G01 filled detached dash below long; no ellipse or thin-line substitution.',
      qualification='high visible shape; local role/hand/origin uncertainty medium')
if '24' in sections:
    select_literal('cancelled-date','24','A',note='Exact A date body and position with invisible deleted annotation.')
    select_literal('cancelled-date-hatching','24','A',note='All fourteen A T01 hatch commands, including curved lower turns; no independent pen-stroke-count assertion.')
if '25' in sections:
    select_literal('margin-core','25','A',note='All ten A M01–M03 path commands placed in the common full-pixel frame; A question node excluded.',
      qualification='main dark geometry high confidence; exact pale retracing medium')
    select_literal('upper-question','25','B',note='B upper-question body, baseline and position retained literally.')
    select('G-margin-point','25',reader='A',
      body=fixed_uncertain_full(source_body('G-margin-point','A'),'A',[46,402,48,406]),
      note='A M04 isolated gray oval; exact center and radius values.',
      qualification='medium shape confidence; role/hand/origin undetermined')
if '26' in sections:
    for name in ['G-bent-upper','G-bent-lower','G-bent-lower-retrace']:
        select_literal(name,'26','A',note='Literal component of A A02 complete three-command bent-arrow group.',
          qualification='main bends/heads high confidence; detailed curvature medium')
    for name,box in [('G-bent-upper-arch',[257,657,278,665]),
                     ('G-bent-upper-dash',[307,652,311,654]),
                     ('G-bent-upper-dot',[303,671,305,675])]:
        select(name,'26',reader='A',body=fixed_uncertain_full(source_body(name,'A'),'A',box),
          note='Exact A A03 residual component, with its own fixed uncertainty origin.',
          qualification='medium shape confidence; role/hand/origin undetermined')
if '27' in sections:
    root_foot=r'\draw[black!70,line width=.50pt] (404,639)--(417,640);'
    assert root_foot in sections['27']
    select('G-date-hook','27',reader='B',body=fixed_B_local('G-date-hook',root_foot),
      note='Both literal B local hook paths plus root exact full-coordinate dark foot path, in one locally qualified graphic.',
      qualification='medium shape confidence; character/role/hand/origin undetermined')
    selections['G-date-hook']['root_added_components']=[{
      'root_entry':'27','tex_exact':root_foot,'sha256':sha(root_foot),
      'coordinate_map':'literal root full path, translated by (-401,-616) inside node origin (401,616)'}]
if '28' in sections:
    for name,conf in [('G-Baumeister-upper-gray','medium'),('G-Baumeister-upper-black','high'),
                      ('G-Baumeister-left-gray','medium'),('G-Baumeister-right-gray','low')]:
        select(name,'28',reader='B',body=fixed_B_local(name),
          note='Exact B local components at the declared fixed origin; no source shape substitution.',
          qualification=f'{conf} visible shape confidence; character/role/hand/origin undetermined')
if '29' in sections:
    for name in ['G-Jeu-overmark','G-Spiel-lower-spot']:
        select(name,'29',reader='B',body=fixed_B_local(name),
          note='Exact B local triangular/oval body and fixed source origin.',
          qualification='medium shape; low function/hand/origin confidence')
if '30' in sections:
    select('G-A-blank-trace','30',reader='B',body=fixed_B_local('G-A-blank-trace'),
      note='All five literal B filled components; their gaps remain unchanged.',
      qualification='medium shape; low function/hand/origin confidence')
if '31' in sections:
    select('G-A-foot-trace','31',reader='B',body=fixed_B_local('G-A-foot-trace'),
      note='All seven literal B spot components; interrupted descending slant retained.',
      qualification='medium shape confidence; no character/surface origin assigned')
if '32' in sections:
    select('G-E23-dash','32',reader='A',
      body=fixed_uncertain_full(source_body('G-E23-dash','A'),'A',[2252,1343,2268,1344]),
      note='Exact A G05 slightly sloping segment, replacing B/C source alternatives.',
      qualification='high shape; medium role/hand/origin uncertainty')
    select('rule-lower-thickening','32',reader='A',
      body=fixed_uncertain_full(source_body('rule-lower-thickening','A'),'A',[2221,1300,2235,1305]),
      note='Exact A G06 filled wedge; B thick straight segment is not emitted. Same one grid physical cluster.',
      qualification='high shape confidence; role/hand undetermined')
if '33' in sections:
    select('G-E20-blot','33',reader='B',body=fixed_B_local('G-E20-blot'),
      note='Exact B irregular filled polygon and declared fixed origin.',
      qualification='medium shape; low function/hand/origin confidence')
if '34' in sections:
    select('G-D-point','34',reader='B',body=fixed_B_local('G-D-point'),
      note='Exact B isolated point and declared fixed origin; no punctuation reading.',
      qualification='medium shape; low function/hand/origin confidence')
if '35' in sections:
    select('G-A-edge-slant','35',reader='B',body=fixed_B_local('G-A-edge-slant'),
      note='All six literal B components, including the separate upper-right point.',
      qualification='medium shape; low character/role/hand/origin confidence')
if '36' in sections:
    select('G-Decouverte-point','36',reader='C',
      body=fixed_C_local('G-Decouverte-point',[240,751],[3,4]),
      note='Root-explicit origin (240,751); C ellipse center (1,2), original-coordinate radii 1.3/1.8 retained by exact dimension ratio.',
      qualification='medium shape; low role/hand/origin confidence')
for entry,nums in [('37',range(1,5)),('38',range(5,7)),('39',range(7,10)),('40',[10])]:
    if entry not in sections:continue
    for i in nums:
        name=f'G-edge-{i:02d}'
        box=edge_components[i-1]['bbox']
        select(name,entry,reader='A',body=fixed_uncertain_full(source_body(name,'A'),'A',box),
          note=f'Exact A E{i:02d} arms/returns/endpoints with its source component identity; no unseen continuation.',
          qualification='medium exact geometry; function beyond sheet edge undetermined')
if '39' in sections:
    select('rule-live-thickening','39',reader='A',
      body=fixed_uncertain_full(source_body('rule-live-thickening','A'),'A',[2308,1088,2321,1093]),
      note='Exact A G07 filled wedge; root crop03 and A23 jointly support this one grid component, separate from ten edge groups.',
      qualification='medium geometry confidence; role/hand undetermined')

record_keys={
 'pale_A':['old-A','G-old-A-curves'],'meditation':['title1c'],
 'cascades':['old-C-Ca','Cascades-hook'],
 **{f'crossed_{t}':['cancel-'+t,'hatch-'+t]+(['cancel-C-terminal-hook','G-cancel-C-gray-point'] if t=='C' else ['cancel-E23-terminal-hook'] if t=='E23' else []) for t in ['A','B','C','D','E20','E23']},
 'lower_question':['lower-question'],'pale_D':['old-sub-D'],'plus':['lower-title2'],
 'pale_sub_A':['old-sub-A'],'pale_sub_C':['old-sub-C-left','G-live-C-gray-dot','G-live-C-right-curve'],
 'grid':grid_ids,'top_cancellation':['cancelled-date','cancelled-date-hatching'],
 'margin':['margin-core','upper-question'],'margin_point':['G-margin-point'],
 'bent_arrows':['G-bent-upper','G-bent-lower','G-bent-lower-retrace'],
 'bent_residuals':['G-bent-upper-arch','G-bent-upper-dash','G-bent-upper-dot'],
 'meditation_residuals':['title1-residuals'],'reveil_residuals':['G-Reveil-diagonal'],
 'long_dash':['G-long-dot'],'lower_A_trace':['G-A-blank-trace'],
 'foot_A_trace':['G-A-foot-trace'],'Fringale_spot':['G-E20-blot'],
 'lower_E23_dash':['G-E23-dash'],'rule_thickening_1303':['rule-lower-thickening'],
 'rule_thickening_1091':['rule-live-thickening'],'right_edge':edges,
 'lower_A_arrow':['G-lower-A-arrow'],'lower_B_arrow':['G-lower-B-arrow'],
 'date_hook':['G-date-hook'],'Baumeister_upper_gray':['G-Baumeister-upper-gray'],
 'Baumeister_upper_dark':['G-Baumeister-upper-black'],'Baumeister_left':['G-Baumeister-left-gray'],
 'Baumeister_right':['G-Baumeister-right-gray'],'crossed_C_patch':['G-cancel-C-gray-point'],
 'Jeu_overmark':['G-Jeu-overmark'],'Spiel_spot':['G-Spiel-lower-spot'],
 'SchI_point':['G-D-point'],'A_lower_slant':['G-A-edge-slant'],
 'Decouverte_point':['G-Decouverte-point']}

# Common B typographical shell is authorized by the assembly task. Exact
# manuscript content bodies are retained; affected uncertainty loci stay pending.
pending_text=set(local14+['old-C-Ca','cancelled-date','upper-question'])
common_text=[]
for name,g in groups.items():
    b=[by_id[x] for x in g['candidate_ids'] if x.startswith('B:')]
    if len(b)==1 and b[0]['command']=='node' and 'local_components' not in b[0]:
        if name not in pending_text and name not in selections:
            common_text.append(name)

header=r'''\scanpage{13}
% Text-only scan013 assembly draft under the explicit root decisions.
% Full-scan coordinate positions use the integrated reader-B frame.
% archive sheet number: 12
\figure{\resizebox{\linewidth}{!}{%
\begin{tikzpicture}[x=.01cm,y=-.01cm,line cap=round,line join=round,
  every node/.style={inner sep=0pt,font=\fontsize{12}{14}\selectfont}]
\useasboundingbox (20,18) rectangle (2354,1668);
'''
tex_parts=[header]
emitted=[]
# Selected ruling and residual background paths precede all text nodes.
order=list(groups)
def order_key(name):
    if name.startswith('rule-'):return (0,order.index(name))
    if name=='title1-residuals':return (1,0)
    ids=groups[name]['candidate_ids']
    b=[by_id[x]['line_start'] for x in ids if x.startswith('B:')]
    return (2,min(b) if b else 1000+order.index(name))
for name in sorted(set(common_text)|set(selections),key=order_key):
    if name in selections:
        s=selections[name]
        body=s['tex_body']
        tag=f'root entry {s["root_entry"]}'
    else:
        cid=next(x for x in groups[name]['candidate_ids'] if x.startswith('B:'))
        body=by_id[cid]['tex_exact']
        tag='reader-B typography; exact common source content'
    tex_parts.extend([f'% assembly group {name}; {tag}\n',body+'\n'])
    emitted.append(name)
pending=[name for name in groups if name not in emitted and name not in ['render-frame','archive-number']]
if pending:
    tex_parts.append('% Pending root-selection groups (candidates remain in the mapping):\n')
    tex_parts.extend('% PENDING '+name+'\n' for name in pending)
tex_parts.append('\\end{tikzpicture}}}\n')
tex=''.join(tex_parts)
for name in emitted:
    marker='% assembly group '+name+'; '
    start=tex.index(marker)
    body_start=tex.index('\n',start)+1
    body=selections[name]['tex_body'] if name in selections else by_id[next(x for x in groups[name]['candidate_ids'] if x.startswith('B:'))]['tex_exact']
    end=body_start+len(body)
    groups[name]['output']={'path':'out/checks/scan013_final_draft.tex',
      'line_start':tex.count('\n',0,body_start)+1,'line_end':tex.count('\n',0,end)+1,
      'char_start':body_start,'char_end':end,'body_sha256':sha(body),
      'status':'root-selected' if name in selections else 'common B typographical shell'}
for collection in crosswalk.values():
    for row in collection:
        gs=row['groups']
        row['root_entries']=list(dict.fromkeys(selections[g]['root_entry'] for g in gs if g in selections))
        row['pending_groups']=[g for g in gs if g in pending]

def structural_checks(text):
    errors=[]
    clean=re.sub(r'(?<!\\)%[^\n]*','',text)
    depth=0
    for m in re.finditer(r'\\[{}]|[{}]',clean):
        if m[0] in ['\\{','\\}']:continue
        depth+=1 if m[0]=='{' else -1
        if depth<0:errors.append('closing brace before opener');break
    if depth:errors.append(f'brace balance {depth}')
    stack=[]
    for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',clean):
        if m[1]=='begin':stack.append(m[2])
        elif not stack or stack.pop()!=m[2]:errors.append('environment mismatch '+m[2])
    if stack:errors.append('unclosed environments '+repr(stack))
    for a,b in [('\\(','\\)'),('\\[','\\]')]:
        if clean.count(a)!=clean.count(b):errors.append('math delimiter mismatch '+a)
    if re.search(r'\\(?:newcommand|renewcommand|def|gdef|providecommand)\b',clean):errors.append('new macro')
    if clean.count('\\scanpage{13}')!=1:errors.append('scan marker count')
    if '\\margin{' in clean:errors.append('separate margin placement')
    if clean.count('\\figure{')!=1:errors.append('figure count')
    if clean.count('$')%2:errors.append('odd dollar count')
    invisible=[]
    for m in re.finditer(r'\\phantom\{',clean):
        p=m.end()-1
        invisible.append((p,matching_brace(clean,p)))
    for m in re.finditer(r'\\deleted\{',clean):
        if not any(a<m.start()<b for a,b in invisible):
            errors.append('visible generic deletion at character '+str(m.start()))
    allowed={'scanpage','figure','resizebox','linewidth','begin','end','useasboundingbox',
       'node','draw','fill','path','fontsize','selectfont','scriptsize','unsure','deleted',
       'rlap','phantom','color','mathrm','mathord','overline','underline','dimexpr','relax',
       'big','Big','bigg','Bigg','text','sout','hspace','quad'}
    unknown=sorted(set(re.findall(r'\\([A-Za-z]+)\b',clean))-allowed)
    if unknown:errors.append('unlisted source macros '+','.join(unknown))
    return errors

errors=structural_checks(tex)
fingerprints=json.loads((OUT/'scan013_reader_fingerprints.json').read_text())
for r in 'ABC':
    for name,body in [('reading.tex',reader_tex[r]),('reading.md',reader_prose[r]),
                      ('report.json',(BASE/f'out/readers/013/{r}/report.json').read_text())]:
        if sha(body)!=fingerprints[r][name]:errors.append('source fingerprint mismatch '+r+'/'+name)
if 'current bounding box' in tex:errors.append('bbox-dependent local origin remains')
body_checks=[]
for name,selection in selections.items():
    if 'represented_within' in selection:
        body_checks.append({'group':name,'result':'source component evidence attached to '+selection['represented_within']})
        continue
    for cid in selection['candidate_ids']:
        item=by_id[cid]
        pieces=[v for v in item.get('local_components',[]) if v['command']!='useasboundingbox'] if 'local_components' in item else [item]
        for piece in pieces:
            expected_body=piece['tex_exact']
            if cid=='A:L029':expected_body=expected_body.replace('(30,286)--(357,288)','(30,286)--(620,288)')
            if cid=='A:L111':expected_body=expected_body.replace('(141,790)--(149,837) (164,792)--(168,823)',
                 '(137,749)--(141,790)--(149,837) (160,749)--(164,792)--(168,823)')
            if cid in ['B:L012','B:L014','B:L018']:expected_body=expected_body.replace('black!18','black!8')
            expected_body=dimensional_to_B(expected_body,item['reader'])
            if selection['tex_body'].count(expected_body)!=1:
                errors.append('selected source body occurrence '+name+'/'+piece['id'])
        body_checks.append({'group':name,'source_candidate':cid,'source_components_checked':len(pieces),'result':'literal selected body retained through documented frame/root amendments'})
unmapped=[v['id'] for v in by_id.values() if not v['groups']]
if unmapped:errors.append('unmapped source statements '+','.join(unmapped))
expected={'differences':106,'doubts':78,'inventories':218,'packet_inventory':48,'C_source_doubts':13}
for k,n in expected.items():
    if len(crosswalk[k])!=n:errors.append(f'{k} count {len(crosswalk[k])} != {n}')
if sum(v['local_loci'] for v in crosswalk['C_source_doubts'])!=14:errors.append('C sublocus count')
for r in 'ABC':
    if any(d.get('H') is not None or d.get('diff_H') for d in reader_reports[r]['differences']):errors.append('H flags '+r)
for g in groups.values():
    if any(c not in by_id for c in g['candidate_ids']):errors.append('missing candidate '+g['id'])
for n in emitted:
    body=selections[n]['tex_body'] if n in selections else by_id[next(x for x in groups[n]['candidate_ids'] if x.startswith('B:'))]['tex_exact']
    if tex.count(body)!=1:errors.append('emitted body multiplicity '+n)
assert errors==[],errors

mapping={
 'scan':13,'built_utc':datetime.now(timezone.utc).isoformat(),
 'authority':'out/checks/scan013_main_decisions.md',
 'root_log_sha256':sha(root_log),'root_entries':{str(k):sha(v) for k,v in sections.items()},
 'scope':'text-only draft assembly; no ink adjudication, compilation, rendering or final page/record write',
 'base_frame':'B; full numeric coordinates shared by source statements',
 'source_frames':source_frames,
 'packet_tex_correspondence':packet_tex_correspondence,
 'coordinate_and_dimension_maps':transforms,
 'frame_adjustment':{'box':[20,18,2354,1668], 'root_entry':'01–10',
      'reason':'include the explicitly retained A V02 extension to y23'},
 'record_key_crosswalk':record_keys,
 'text_body_catalog':[{ 'group':g['id'],
      'sources':[{'candidate_id':c,'body_exact':by_id[c].get('node_body_exact')}
                 for c in g['candidate_ids'] if 'node_body_exact' in by_id[c]]}
      for g in groups.values() if any('node_body_exact' in by_id[c] and 'local_components' not in by_id[c] for c in g['candidate_ids'])],
 'fingerprints':{r:{'reading_tex_sha256':sha(reader_tex[r]),
                    'report_json_sha256':sha((BASE/f'out/readers/013/{r}/report.json').read_text()),
                    'reading_md_sha256':sha(reader_prose[r])} for r in 'ABC'},
 'candidates':list(by_id.values()),'groups':list(groups.values()),'crosswalk':crosswalk,
 'common_text_groups':common_text,'selected_groups':list(selections),
 'emitted_groups':emitted,'pending_root_actions':pending,
 'counts':{**{k:len(v) for k,v in crosswalk.items()},
           'source_top_level_statements':len(by_id),'physical_groups':len(groups),
           'selected_groups':len(selections),'pending_groups':len(pending)},
 'structural_validation':{'errors':errors,'brace_environment_delimiter_checks':'direct source only',
                          'compile_attempted':False,'render_attempted':False,
                          'complete_under_root_choices':not pending},
 'selected_body_checks':body_checks,
 'draft_sha256':sha(tex)}
TEX.write_text(tex)
MAP.write_text(json.dumps(mapping,ensure_ascii=False,indent=2)+'\n')
audit=['# Scan013 text-only TeX assembly\n',
       'The draft uses the integrated B coordinate frame. Every retained manuscript body and graphical candidate has an exact source statement in the mapping. No image was opened or processed; no compilation, rendering, installation, or ink adjudication was performed.\n',
       f'Root-log SHA256: `{sha(root_log)}`. Root decision entries indexed: {len(sections)}.\n',
       '## Source accounting\n',
       '| Source set | Rows |\n|---|---:|\n']
audit += [f'| {k} | {len(v)} |\n' for k,v in crosswalk.items()]
audit += [f'\nC source doubts cover 13 original rows and 14 local loci. Source statements: {len(by_id)}. Physical groups: {len(groups)}.\n',
          '\n## Selected source bodies\n']
if selections:
    audit+=['| Group | Root entry | Exact candidates | Assembly note |\n|---|---:|---|---|\n']
    for name,s in selections.items():
        audit.append(f'| {name} | {s["root_entry"]} | {", ".join(s["candidate_ids"])} | {s["note"].replace("|"," / ")} |\n')
else:audit.append('No ink selections have yet been applied.\n')
audit+=['\n## Pending root actions\n']
audit += ['- '+name+'\n' for name in pending] if pending else ['None. Every selected group has an explicit root disposition.\n']
audit += ['\n## Direct structural checks\n',
          f'Errors: `{json.dumps(errors)}`. Brace/environment/math delimiters, source coverage, row counts, H-absent flags, exact emitted-body multiplicities, single page marker, common-frame placement, and absence of new macros were checked directly.\n',
          '\nThis remains the assembly draft for root approval. No compiler or render validation is claimed.\n']
AUDIT.write_text(''.join(audit))
print(json.dumps({'files':[str(TEX),str(MAP),str(AUDIT)],'counts':mapping['counts'],
                  'structural_errors':errors,'pending_root_actions':pending},ensure_ascii=False))
