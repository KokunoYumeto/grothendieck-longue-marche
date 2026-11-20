#!/usr/bin/env python3
"""Index released scan018 source candidates, without an ink selection.

This is text-only assembly preparation. It does not read image bytes, invoke a
compiler, calculate drawing geometry, or write a record/approval/page commit.
"""
from pathlib import Path
import hashlib
import json
import re

BASE = Path('/workspace/scratch/94548b74fbe0')
OUT = BASE / 'out/checks'


def sha(value):
    return hashlib.sha256(value.encode('utf-8')).hexdigest()


def span(path, text, a, b, **extra):
    def position(k):
        return {'line': text.count('\n', 0, k) + 1,
                'column_zero_based': k - (text.rfind('\n', 0, k) + 1)}
    value = text[a:b]
    return {'file': path, 'file_sha256_utf8': sha(text),
            'character_start': a, 'character_end_exclusive': b,
            'offset_convention': 'zero-based Unicode code-point offsets in UTF-8 decoded file; end-exclusive',
            'start': position(a), 'end_exclusive': position(b),
            'covering_lines_inclusive': [position(a)['line'], position(max(a, b-1))['line']],
            'literal_tex': value, 'literal_sha256_utf8': sha(value), **extra}


def command_end(text, start):
    depth = 0
    for i in range(start, len(text)):
        c = text[i]
        escaped = i > 0 and text[i-1] == '\\'
        if c == '{' and not escaped:
            depth += 1
        elif c == '}' and not escaped:
            depth -= 1
        elif c == ';' and depth == 0:
            return i + 1
    raise ValueError(('unterminated source command', start))


def brace_end(text, brace):
    depth = 0
    for i in range(brace, len(text)):
        escaped = i > 0 and text[i-1] == '\\'
        if text[i] == '{' and not escaped:
            depth += 1
        elif text[i] == '}' and not escaped:
            depth -= 1
            if depth == 0:
                return i+1
    raise ValueError(('unterminated source brace', brace))


BOUNDARIES = {
 'A': {
  'G01': (['l\'une','(unique), inserted','des|de','ces n'], ['est dans before','classes after']),
  'G02': (['complete lemma','Lemme underline state in phantom'], ['blank paragraph boundaries']),
  'G03': (['qu\'une, inserted','la, deleted via phantom'], ['Dire before','classe donnée after']),
  'G04': (['U_alpha|x, inserted','de Pi_J^circ, inserted','ne'], ['classe donnée before','contient pas after']),
  'G05': (['choisi|choisie, deleted via phantom','two additional qualified points'], ['closed formula before','quoted composant after']),
  'G06': (['éléments','(soit Sigma_i^-), inserted','de'], ['l\'un des before','pi_0(X setminus Sigma_i) and comma after']),
  'G07': (['deux, deleted via phantom','card I=2, inserted','comma'], ['cas before','cancelled cela|OK after']),
  'G08': (['OK, locally qualified state with phantom deleted annotation','period','qualified gray spot'], ['final formula comma before','archive comment after']),
 },
 'B': {
  'G01': (['l\'une','(unique), inserted','des|de ces n'], ['est dans before','classes after']),
  'G02': (['complete lemma','Lemme underline state in phantom'], ['blank paragraph boundaries']),
  'G03': (['qu\'une, inserted','la, ordinary deleted macro','classe donnée','U_alpha|x de Pi_J^circ, inserted','ne contient'], ['Dire before','pas after']),
  'G04': (['live E_i','complete qualified upper-rule group with right retrace'], ['pas and deleted Sigma before','i.e. est after']),
  'G05': (['choisi|choisie, ordinary deleted macro','complete qualified two-point group'], ['closed formula before','quoted composant|composante after']),
  'G06': (['éléments','(soit Sigma_i^-), inserted','de'], ['l\'un des before','pi_0(X setminus Sigma_i) and comma after']),
  'G07': (['deux, deleted via phantom','card I=2, inserted'], ['cas before','comma after']),
  'G08': (['OK, complete outer unsure with phantom deleted annotation','one rising transverse stroke'], ['final formula comma before','period after']),
 },
 'C': {
  'G01': (['l\'une','(unique), inserted','de|des','ces n'], ['est dans before','classes after']),
  'G02': (['complete lemma','Lemme underline state in phantom'], ['blank paragraph boundaries']),
  'G03': (['qu\'une, inserted','la, deleted via phantom','classe'], ['Dire before','donnée is in G04']),
  'G04': (['donnée','U_alpha|x quad de Pi_J^circ, inserted','ne'], ['classe is in G03','contient pas after']),
  'G05': (['choisi|choisie, deleted via phantom','complete qualified two-point group'], ['closed formula before','quoted composant after']),
  'G06': (['first-accent-qualified éléments','(soit Sigma_i^-), inserted','de','pi_0(X setminus Sigma_i)'], ['l\'un des before','comma and d\'après l\'étude du after']),
  'G07': (['cas','deux, deleted via phantom','card I=2, inserted','complete qualified lower hook'], ['d\'après l\'étude du before','comma after']),
 },
}

COMPONENT_IDS = {
 'A': {'G01':['G01.P1'],'G02':['G02.P1','G02.P2'],'G03':['G03.P1','G03.P2'],
       'G04':['G04.P1','G04.P2'],'G05':['G05.P1','G05.P2','G05.P3'],
       'G06':['G06.P1'],'G07':['G07.P1'],'G08':['G08.P1','G08.P2']},
 'B': {'G01':['G01'],'G02':['G02-underline','G02-left-rule'],
       'G03':['G03a','G03b-main','G03b-hook'],'G04':['G04-upper-rule'],
       'G05':['G05-point1','G05-point2'],'G06':['G06'],'G07':['G07-cancellation'],
       'G08':['G08-rising-stroke']},
 'C': {'G01':['G01a'],'G02':['G02a','G02b'],'G03':['G03a','G03b','G03c'],
       'G04':['G04a','G04b'],'G05':['G05a','G05b','G05c'],'G06':['G06a'],
       'G07':['G07a','G07b']},
}


def source_groups(reader, path, text):
    stack = []
    pictures = []
    for m in re.finditer(r'\\(begin|end)\{tikzpicture\}', text):
        if m.group(1) == 'begin':
            stack.append(m.start())
        else:
            a = stack.pop()
            if not stack:
                pictures.append((a, m.end()))
    groups = []
    previous_end = 0
    for number, (picture_start, picture_end) in enumerate(pictures, 1):
        group = f'G{number:02d}'
        heading = re.search(r'^% '+group+r':[^\n]*', text[previous_end:picture_end], re.M)
        heading_start = previous_end+heading.start()
        # B.G04's title is inside its outer picture; B.G08's unsure is outside.
        wrapper_start = picture_start
        wrapper = None
        for macro in [r'\figure{',r'\unsure{']:
            if text[:picture_start].endswith(macro):
                wrapper_start = picture_start-len(macro)
                wrapper = macro[:-1]
                break
        a = min(heading_start, wrapper_start)
        b = picture_end + (1 if wrapper else 0)
        source = span(path, text, a, b, reader=reader)
        nodes = []
        for m in re.finditer(r'\\node\b', text[picture_start:picture_end]):
            start = picture_start+m.start()
            nodes.append((start, command_end(text,start)))
        dependencies = []
        for m in re.finditer(r'\\(unsure|phantom|rlap|deleted|inserted|uline)\{', text[a:b]):
            start = a+m.start(); end=brace_end(text,a+m.end()-1)
            dependencies.append({'macro':m.group(1),'source':span(path,text,start,end)})
        components = []
        path_matches = list(re.finditer(r'\\(?:draw|fill)\b', text[picture_start:picture_end]))
        for component_id, m in zip(COMPONENT_IDS[reader][group], path_matches, strict=True):
            start=picture_start+m.start(); end=command_end(text,start)
            enclosing_nodes=[n for n in nodes if n[0]<=start and end<=n[1]]
            enclosing_nodes.sort(key=lambda n:n[1]-n[0])
            support=span(path,text,*enclosing_nodes[0]) if enclosing_nodes else source
            components.append({'component_id':component_id,'candidate_component_id':reader+'.'+component_id,
                'source':span(path,text,start,end),'complete_support_source':support,
                'enclosing_qualifier_state_sources':[d for d in dependencies if
                    d['source']['character_start']<=start and end<=d['source']['character_end_exclusive']],
                'copy_policy':'Keep this literal component once, with its enclosing node/qualifier and source origin dependencies.'})
        declarations=[]
        for m in re.finditer(r'^.*(?:\\begin\{tikzpicture\}|\\begin\{scope\}|\\coordinate|\\path\[use as bounding box\]).*$',text[a:b],re.M):
            declarations.append(span(path,text,a+m.start(),a+m.end()))
        included, external=BOUNDARIES[reader][group]
        groups.append({'candidate_id':reader+'.'+group,'reader':reader,'original_group_id':group,
            'source':source,'outer_picture_source':span(path,text,picture_start,picture_end),
            'outer_wrapper':wrapper,'included_word_state_boundaries':included,
            'external_word_boundaries':external,'wrapper_state_dependencies':dependencies,
            'literal_path_components':components,'literal_coordinate_declarations':declarations,
            'left_source_context':span(path,text,max(0,a-150),a),
            'right_source_context':span(path,text,b,min(len(text),b+150)),
            'selected':None,'selection_authority':'Root only; no ink choice made by assembler.'})
        previous_end=b
    segments=[]; last=0
    for g in groups:
        a=g['source']['character_start'];b=g['source']['character_end_exclusive']
        if a>last: segments.append({'kind':'intergroup_source','source':span(path,text,last,a)})
        segments.append({'kind':'complete_group','candidate_id':g['candidate_id'],'source':g['source']})
        last=b
    if last<len(text):segments.append({'kind':'intergroup_source','source':span(path,text,last,len(text))})
    return groups,segments


def main():
    candidates=[]; sources={}; partitions={}
    for reader in 'ABC':
        path=f'out/readers/018/{reader}/reading.tex';text=(BASE/path).read_text()
        sources[path]={'sha256_utf8':sha(text),'complete_source':span(path,text,0,len(text))}
        groups,segments=source_groups(reader,path,text)
        candidates.extend(groups);partitions[reader]=segments
    for path in ['packets/018/C.tex','packets/018/H.tex']:
        text=(BASE/path).read_text();sources[path]={'sha256_utf8':sha(text),'complete_source':span(path,text,0,len(text))}
    result={'scan':18,'status':'Source-only complete candidates; root selections pending.',
        'main_adjudicated':False,'sources':sources,'group_candidates':candidates,
        'complete_reader_source_partitions':partitions,
        'first_occurrence_dependencies':[
            {'locus':'raised Pi ring','first':'lemma Pi','later':'inserted Pi',
             'rule':'Selected first glyph qualification appears at lemma; later primary is printed unqualified, with local retained doubt attached in record.'},
            {'locus':'U alpha/x subscript','first':'raised U after donnée','later':'final U',
             'rule':'Selected first glyph qualification appears in raised U; final primary is printed unqualified, with final local decision separately retained.'}],
        'scope':'Exact text selection preparation only. No images, ink decisions, optional calculations, compilation, rendering or approval.',
        'structural_review':'Deferred until root-selected draft is complete; indexing is assembly preparation.'}
    (OUT/'scan018_tex_candidates.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    rows=['# Scan018 complete source candidates','',
          'No source candidate is selected. Every JSON source locator contains the exact original excerpt, UTF-8 SHA-256, Unicode offsets and line span. Complete outer wrappers, phantom state annotations, nested qualified nodes, source baselines and scopes are preserved.','',
          '| Candidate | Words / state inside the complete group | Adjacent source outside | Literal components |',
          '|---|---|---|---|']
    for g in candidates:
        inside='; '.join(g['included_word_state_boundaries']).replace('|',' / ')
        outside='; '.join(g['external_word_boundaries']).replace('|',' / ')
        parts=', '.join(p['component_id'] for p in g['literal_path_components'])
        rows.append(f"| {g['candidate_id']} | {inside} | {outside} | {parts} |")
    rows += ['', '## Assembly dependencies','',
             '- A G03/G04, B G03, and C G03/G04 use different complete word boundaries; selecting one requires consuming the corresponding adjoining source words once.',
             '- B G04 begins before its internal `% G04:` comment. Its complete outer group contains live E_i and the qualified retraced upper-rule node. The preceding deleted Sigma remains outside.',
             '- B G08 has an outer `\\unsure` wrapper. Its final period remains outside; A G08 contains its final period and the separate qualified gray spot.',
             '- C G07 contains the qualified lower hook and cas. A/B G07 omit that hook in their exact complete source blocks; these source scopes do not decide ink absence.',
             '- Choosing a full nested shape preserves its enclosing node, local unsure, baseline, bounds, coordinate units and applicable outer scope. Literal stroke bodies alone do not supply those dependencies.',
             '- In A/C G03, G05 and G07, phantom deletion annotations carry state while the separately selected literal path supplies the visible strike. A/B G08 also retains its phantom deletion state annotation.',
             '- The first-occurrence Pi-ring and U-index qualifiers remain bound to their first printed loci; each later independently inspected locus remains separately attached in the record.', '']
    (OUT/'scan018_tex_candidates.md').write_text('\n'.join(rows))
    print(json.dumps({'group_candidates':len(candidates),'json':'out/checks/scan018_tex_candidates.json','inventory':'out/checks/scan018_tex_candidates.md','selected':False}))


if __name__ == '__main__':
    main()
