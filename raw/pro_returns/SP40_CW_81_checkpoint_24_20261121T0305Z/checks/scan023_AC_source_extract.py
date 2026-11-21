"""Exact source-only extraction of the explicitly released A and C returns."""
from pathlib import Path
import ast
import hashlib
import json
import re

ROOT = Path('/workspace/scratch/94548b74fbe0')
OUT = ROOT / 'out/checks'
# Reuse only pure text helper definitions; never execute the B extraction script.
helper_tree = ast.parse((OUT/'scan023_B_source_extract.py').read_text())
helper_names = {'ref', 'json_spans', 'jref', 'command_end'}
exec(compile(ast.Module(body=[n for n in helper_tree.body if isinstance(n, ast.FunctionDef) and n.name in helper_names], type_ignores=[]), '<source-only helpers>', 'exec'))
catalog_path = 'out/checks/scan023_C_doubt_catalog.json'
witness_path = 'out/checks/scan023_witness_source_coverage.json'
files = [catalog_path, witness_path, 'packets/023/C_doubts.txt']
release_names = {
    'A': ['reading.tex','report.json','reading.md','graphics_map.json','source_check.json','view_audit.json','crop_plan.json','freeze_manifest.json'],
    'C': ['reading.tex','report.json','reading.md','source_map.json','source_checks.json','view_audit.json','crop_manifest.json','freeze_manifest.json'],
}
for reader, names in release_names.items():
    files.extend(f'out/readers/023/{reader}/{n}' for n in names)
texts = {p:(ROOT/p).read_text(encoding='utf-8') for p in files}
hashes = {p:hashlib.sha256(t.encode('utf-8')).hexdigest() for p,t in texts.items()}
data = {p:json.loads(t) for p,t in texts.items() if p.endswith('.json')}
jspan = {p:json_spans(texts[p]) for p in data}
catalog = data[catalog_path]
witnesses = data[witness_path]
summaries = {}

for reader in ['A','C']:
    base = f'out/readers/023/{reader}/'
    TEX, REPORT = base+'reading.tex', base+'report.json'
    exec(compile(ast.Module(body=[n for n in helper_tree.body if isinstance(n, ast.FunctionDef) and n.name in {'exact','extent'}], type_ignores=[]), '<reader text helpers>', 'exec'))
    MAP = base+('graphics_map.json' if reader=='A' else 'source_map.json')
    tex = texts[TEX]
    report = data[REPORT]
    raw_map = data[MAP]
    errors = []
    groups = {}
    items = list(raw_map.items()) if reader=='A' else [(g['group_id'],g) for g in raw_map['groups']]
    for index,(gid,g) in enumerate(items):
        if reader=='A':
            s,e = g['source_span']['start_char'],g['source_span']['end_char']
            expected = g['source_span']['sha256']
            pointer = '/'+gid
        else:
            encoded=tex.encode('utf-8')
            s=len(encoded[:g['start_byte_utf8']].decode('utf-8'))
            e=len(encoded[:g['end_byte_utf8']].decode('utf-8'))
            expected=g['span_sha256']
            pointer=f'/groups/{index}'
        actual=hashlib.sha256(tex[s:e].encode('utf-8')).hexdigest()
        if expected!=actual: errors.append({'type':'group_source_hash_mismatch','id':gid})
        groups[gid]=dict(id=gid,raw=g,map_ref=jref(MAP,pointer),tex_ref=ref(TEX,s,e),source_selected=False)
    def gr(gid): return groups[gid]['tex_ref']

    if reader=='A':
        named={
          'opening':extent('Soit maintenant ','=\\varnothing$.'),
          'upper_paragraph':extent('En effet, ','% END A023-S01\n$,'),
          'continued_assertion':extent('je dis que si ','% END A023-G03'),
          'first_display':extent('\\[\nE_\\beta','\\]\n'),
          'margin':extent('\\reversemarginpar\\margin{\\makebox','\\normalmarginpar'),
          'upper_argument':extent('\\unsure{qui|ce qui}','Cela revient \\unsure{au}'),
          'lemma_intro':extent('\\uline{Lemme}','\\unsure{tels} que'),
          'lemma_condition':extent('\\[\n\\alpha','\\]\n'),
          'lemma_hypothesis':extent('Soit $i\\in I\\setminus K$','$, alors'),
          'lemma_correction':exact('\\deleted{$E_i$ est \\unsure{contenu|contenue}} \\inserted{$\\exists\\alpha\\in K$ tel que}'),
          'lemma_endpoint':extent('$E_i\\subset\n% BEGIN A023-S08','$.'),
          'unfinished':extent('Cela \\deleted{signifie que}','% END A023-M04\n}'),
          'corollary_heading':extent('\\uline{Corollaire}',')_{\\alpha\\in K}$,'),
          'corollary_statement':gr('A023-G07'),
          'last_sentence':exact('\\unsure{Immédiat|Immèdiat|Immediat} par \\unsure{récurrence|rècurrence|recurrence} sur $\\operatorname{card} K\\geqslant 0$.'),
          'archive_comment':exact('% archive sheet number: 22\n'),
        }
        manual={
          2:exact('V$ ne \\deleted{contient} \\inserted{rencontre}'),6:exact('\\deleted{\\unsure{donc si}}'),
          9:exact("C'est trivial,"),10:exact('\\deleted{\\illegible{1}}'),11:named['margin'],
          12:exact('\\unsure{qui|ce qui}'),13:exact('\\unsure{prouvera|prouve}'),
          15:exact('Cela revient \\unsure{au}'),16:exact('\\unsure{au}'),17:exact('\\deleted{et}'),18:exact('\\unsure{tels}'),
          23:named['lemma_correction'],24:named['lemma_correction'],25:named['lemma_correction'],26:named['lemma_correction'],
          28:exact('\\unsure{precise|précise|provient|precise le|précise le}'),29:named['unfinished'],
          31:exact('hyp. \\unsure{préc.} sur'),33:named['corollary_heading'],
          40:exact('\\unsure{Immédiat|Immèdiat|Immediat}'),41:exact('\\unsure{récurrence|rècurrence|recurrence}'),
        }
        inv={
          '01':'opening','02':'upper_paragraph','02a':exact('\\deleted{contient}'),'02b':exact('\\inserted{rencontre}'),
          '04a':gr('A023-G02'),'05a':gr('A023-S01'),'06':exact('\\deleted{\\unsure{donc si}}'),
          '07':'continued_assertion','08':'first_display','09':'margin','09a':exact('\\deleted{\\illegible{1}}'),
          '10':'upper_argument','11':'upper_argument','12':'lemma_intro','12a':exact('\\deleted{tel que les}'),
          '12b':exact('\\deleted{et}'),'13':'lemma_condition',
          '14':extent('Soit $i\\in I\\setminus K$','% END A023-S08\n$.'),
          '14b':'lemma_correction','14c':'lemma_correction','15':'unfinished','15a':exact('\\deleted{signifie que}'),
          '16':'corollary_heading','17':'corollary_statement','17a':'corollary_statement','17d':'corollary_statement',
          '18':'last_sentence','19':'archive_comment',
        }
        diff_scopes={}
        for ns,scope in [([1,2,3,4,5,6,7,8],'opening'),([9,10,11],'margin'),([12,13,14,15,16],'upper'),
                         ([17,18],'lemma_intro'),([19,20,21],'lemma_condition'),([22,23,24,25,26,27],'lemma_conclusion'),
                         ([28,29,30],'unfinished'),([31,32,33],'corollary_heading'),([34,35,36,37,38,39],'corollary_statement'),
                         ([40,41],'last')]:
            for n in ns:diff_scopes[n]=scope
    else:
        named={
          'opening':extent('Soit maintenant ','=\\varnothing$.'),
          'upper_paragraph':extent('En effet, ','% END GROUP C023-G03\n$,'),
          'continued_assertion':extent('je dis que si ',' en fait\n'),
          'first_display':extent('\\[\nE_\\beta','\\]\n'),
          'margin':extent('\\reversemarginpar\\margin{\\makebox','\\normalmarginpar'),
          'upper_argument':extent('ce qui \\unsure{prouvera}','Cela revient \\unsure{au}'),
          'lemma_intro':extent('\\uline{Lemme}','\\unsure{tels} que'),
          'lemma_condition':extent('\\[\n\\alpha','\\]\n'),
          'lemma_hypothesis':extent('Soit $i\\in I\\setminus K$','$, alors'),
          'lemma_correction':gr('C023-G11'),
          'lemma_endpoint':extent('$E_i\\subset\n% BEGIN GROUP C023-G12','$.'),
          'unfinished':extent('Cela \\deleted{signifie que}','% END GROUP C023-G13'),
          'corollary_heading':extent('\\uline{Corollaire}','% END GROUP C023-G14'),
          'corollary_statement':gr('C023-G15'),
          'last_sentence':extent('% BEGIN GROUP C023-G20','sur $\\operatorname{card} K\\geq 0$.'),
          'archive_comment':exact('% archive sheet number: 22\n'),
        }
        manual={
          1:exact('V$ ne \\deleted{contient} \\inserted{rencontre}'),5:exact('\\deleted{\\unsure{donc si}}'),
          7:exact("C'est trivial,"),8:exact('\\deleted{\\illegible{1}}'),9:named['margin'],
          10:exact('ce qui \\unsure{prouvera}'),11:exact('\\unsure{prouvera}'),13:exact('Cela revient \\unsure{au}'),
          14:exact('\\unsure{au}'),15:exact('\\deleted{et}'),17:exact('\\unsure{tels}'),
          26:exact('\\unsure{précise|precise|provient|précise le|precise le}'),29:exact('hyp. préc. sur'),
          39:exact('\\unsure{récurrence|rècurrence|recurrence}'),
        }
        inv={
          '01':extent('Soit maintenant ',' en fait\n'),'02':exact('\\deleted{contient}'),'03':exact('\\inserted{rencontre}'),
          '09':exact('\\deleted{\\unsure{donc si}}'),'11':'continued_assertion','12':'first_display','13':'margin',
          '14':exact('\\deleted{\\illegible{1}}'),'15':'upper_argument','17':exact('\\uline{Lemme}'),'18':'lemma_intro',
          '19':exact('\\deleted{tel que les}'),'20':exact('\\deleted{et}'),'22':'lemma_condition',
          '27':extent('Soit $i\\in I\\setminus K$','% END GROUP C023-G12\n$.'),
          '33':'unfinished','34':exact('\\deleted{signifie que}'),'36':'corollary_heading','45':'last_sentence','47':'archive_comment',
        }
        diff_scopes={}
        for ns,scope in [([1,2,3,4,5,6],'opening'),([7,8,9],'margin'),([10,11,12,13,14],'upper'),
                         ([15,16,17],'lemma_intro'),([18,19,20],'lemma_condition'),([21,22,23,24,25],'lemma_conclusion'),
                         ([26,27,28],'unfinished'),([29,30,31],'corollary_heading'),([32,33,34,35,36,37],'corollary_statement'),
                         ([38,39,40],'last')]:
            for n in ns:diff_scopes[n]=scope

    differences=[]
    for i,raw in enumerate(report['differences']):
        n=int(raw['id'].split('D')[-1])
        group_ids=([raw['graphic_ref']] if raw.get('graphic_ref') else []) if reader=='A' else raw.get('source_groups',[])
        refs=[gr(g) for g in group_ids]
        if n in manual:refs.append(manual[n])
        assert refs,(reader,raw['id'])
        scope=diff_scopes[n]
        differences.append(dict(id=raw['id'],reader=reader,raw=raw,source_ref=jref(REPORT,f'/differences/{i}'),
                                own_tex_refs=refs,source_selected=False,
                                actual_witness_contexts={w:witnesses['C_and_H_named_contexts'][w][scope] for w in ['C','H']}))
    by_diff={d['id']:d for d in differences}
    doubts=[]
    for i,raw in enumerate(report['doubts']):
        did=raw['id'] if reader=='A' else raw['id'].removeprefix('Q-')
        doubts.append(dict(id=raw['id'],raw=raw,source_ref=jref(REPORT,f'/doubts/{i}'),
                           difference_id=did,own_tex_refs=by_diff[did]['own_tex_refs'],source_selected=False))
    inventory=[]
    for i,raw in enumerate(report['inventory']):
        suffix=raw['element'].split('.')[1]
        refs=[]
        if reader=='A':
            refs=[gr(g) for g in raw.get('components',[]) if g in groups]
        else:
            g=raw.get('source_group')
            if g in groups:refs=[gr(g)]
        if suffix in inv:
            v=inv[suffix]
            refs.append(named[v] if isinstance(v,str) else v)
        assert refs,(reader,raw['element'])
        inventory.append(dict(id=raw['element'],raw=raw,source_ref=jref(REPORT,f'/inventory/{i}'),
                              complete_tex_refs=refs,source_selected=False,selected_transcribed_status=None))
    notation=[]
    for i,raw in enumerate(report['notation']):
        g=raw.get('source_group',raw.get('proposed_LaTeX'))
        refs=[gr(g)] if g in groups else []
        if raw.get('source_anchor'):refs.append(exact(raw['source_anchor']))
        if not refs:
            loc=raw.get('location','')
            scope = ('opening' if 'Opening' in loc or loc=='opening' else 'first_display' if loc=='S02' else
                     'upper_argument' if loc=='S03' else 'lemma_condition' if 'implication' in loc else
                     'last_sentence' if 'final' in loc.lower() else 'corollary_heading' if 'family' in loc or 'lead' in loc or 'abbreviation' in loc else
                     'corollary_statement' if 'Pi' in loc else 'upper_paragraph')
            refs=[named[scope]]
            if 'unions' in loc:refs.append(named['corollary_statement'])
            if loc=='Each difference set':refs.append(named['lemma_hypothesis'])
            if loc=='Opening a; on a; la partition':refs.extend([named['continued_assertion'],named['corollary_statement']])
        notation.append(dict(id=raw.get('id',f'{reader}-notation-index-{i}'),raw=raw,
                             source_ref=jref(REPORT,f'/notation/{i}'),own_tex_refs=refs,source_selected=False))

    key='source_C_doubt_rows' if reader=='A' else 'C_doubt_source_rows'
    original=[]
    for i,raw in enumerate(report[key]):
        cid=raw['source_id'] if reader=='A' else raw['source_row_id']
        c=next(x for x in catalog['rows'] if x['source_id']==cid)
        if raw['raw_source_row']!=c['literal']:errors.append({'type':'actual_C_row_mismatch','id':cid})
        original.append(dict(id=cid,canonical_parts=[p['part_id'] for p in c['source_parts']],raw_reader_return=raw,
                             reader_source_ref=jref(REPORT,f'/{key}/{i}'),canonical_root_catalog_row=c,
                             actual_C_source_ref=ref(c['source_path'],c['char_start'],c['char_end']),selected_outcome=None))
    ordered=sorted(groups.values(),key=lambda g:g['tex_ref']['char_start_zero_based'])
    top=[]
    for g in ordered:
        s,e=g['tex_ref']['char_start_zero_based'],g['tex_ref']['char_end_exclusive']
        parents=[h['id'] for h in ordered if h['id']!=g['id'] and h['tex_ref']['char_start_zero_based']<=s and e<=h['tex_ref']['char_end_exclusive']]
        g['containing_text_groups']=parents
        if not parents:top.append(g)
    partition=[];cursor=0
    for g in top:
        s,e=g['tex_ref']['char_start_zero_based'],g['tex_ref']['char_end_exclusive']
        assert cursor<=s
        if cursor<s:partition.append(dict(id=f'{reader}023-T{len(partition)+1:03}',kind='literal_interstice',tex_ref=ref(TEX,cursor,s)))
        partition.append(dict(id=g['id'],kind='complete_graphical_group',tex_ref=g['tex_ref']))
        cursor=e
    if cursor<len(tex):partition.append(dict(id=f'{reader}023-T{len(partition)+1:03}',kind='literal_interstice',tex_ref=ref(TEX,cursor,len(tex))))
    assert ''.join(x['tex_ref']['literal'] for x in partition)==tex
    commands=[]
    for m in re.finditer(r'\\(draw|fill|path|coordinate|node)\b',tex):
        s=m.start();line_start=tex.rfind('\n',0,s)+1
        if '%' in tex[line_start:s]:continue
        e=command_end(s)
        containers=[g for g in groups.values() if g['tex_ref']['char_start_zero_based']<=s and e<=g['tex_ref']['char_end_exclusive']]
        containers.sort(key=lambda g:g['tex_ref']['char_end_exclusive']-g['tex_ref']['char_start_zero_based'])
        commands.append(dict(id=f'{reader}023-CMD{len(commands)+1:03}',command=m.group(1),tex_ref=ref(TEX,s,e),
                             text_containment_groups=[g['id'] for g in containers],narrowest_text_group=containers[0]['id'] if containers else None))
    component_checks=[]
    lines=tex.splitlines()
    for g in groups.values():
        if reader=='A':
            for r in g['raw'].get('path_and_label_components',[]):
                sp=r['source_span'];literal=tex[sp['start_char']:sp['end_char']]
                okay=r['command'] in literal
                component_checks.append(dict(owner=r['component_id'],source_ref=ref(TEX,sp['start_char'],sp['end_char']),raw=r,literal_matches=okay))
                if not okay:errors.append({'type':'component_command_mismatch','id':r['component_id']})
        else:
            for r in g['raw']['path_owners']:
                refs=[]
                for cmd in r['commands']:
                    line=cmd['line'];s=sum(len(x) for x in tex.splitlines(keepends=True)[:line-1]);e=s+len(lines[line-1])
                    okay=cmd['exact_source']==lines[line-1]
                    refs.append(ref(TEX,s,e))
                    if not okay:errors.append({'type':'component_command_mismatch','id':r['path_id'],'line':line})
                component_checks.append(dict(owner=r['path_id'],raw=r,source_refs=refs))
    freeze=data[base+'freeze_manifest.json'];freeze_entries=[]
    allowed=set(release_names[reader])-{'freeze_manifest.json'}
    for i,entry in enumerate(freeze['files']):
        name=entry.get('name',entry.get('path'))
        if name in allowed:
            match=entry['sha256']==hashes[base+name]
            freeze_entries.append(dict(raw=entry,source_ref=jref(base+'freeze_manifest.json',f'/files/{i}'),hash_matches=match))
            if not match:errors.append({'type':'text_freeze_hash_mismatch','path':base+name})
    md=[];cursor=0
    for i,line in enumerate(texts[base+'reading.md'].splitlines(keepends=True)):
        if line.strip():md.append(dict(line_one_based=i+1,source_ref=ref(base+'reading.md',cursor,cursor+len(line))))
        cursor+=len(line)
    excluded={'differences','doubts','inventory','notation',key}
    support=dict(scan='023',reader=reader,source_only=True,source_selected=False,main_adjudicated=False,main_approved=False,
                 selected_counts=None,selected_record=None,
                 release_provenance='Root explicitly released the frozen return; raw checkpoint pause honored before creating this extraction.',
                 method='Exact text indexing, original JSON values and literal path/label preservation. No image, image-file metadata, coordinate or mathematical calculation, rendering or ink adjudication.',
                 source_files=[dict(path=base+n,sha256_utf8=hashes[base+n],character_count=len(texts[base+n]),utf8_byte_count=len(texts[base+n].encode('utf-8'))) for n in release_names[reader]],
                 differences=differences,doubts=doubts,inventory=inventory,notation=notation,original_C_rows=original,
                 graphical_groups=list(groups.values()),graphical_component_records=component_checks,exact_graphical_commands=commands,
                 complete_TeX_partition=partition,named_complete_source_spans=named,reading_md_entries=md,
                 remaining_report_fields={k:dict(raw=v,source_ref=jref(REPORT,'/'+k)) for k,v in report.items() if k not in excluded},
                 released_audit_files={n:dict(raw=data[base+n],source_ref=jref(base+n,'')) for n in release_names[reader] if n in ['source_check.json','source_checks.json','view_audit.json','crop_plan.json','crop_manifest.json']},
                 freeze_manifest_text_entries=freeze_entries,freeze_manifest_other_header={k:v for k,v in freeze.items() if k!='files'},
                 report_silent_source_coverage='The exhaustive TeX partition and named complete spans preserve every report-silent source choice. Absence from a difference list contributes no reading.',
                 assembly_attention=[dict(subject='Raw parent/child hand scopes',detail='All raw whole-region and component hand fields are retained; containing references confer no new hand attribution.'),
                                     dict(subject='Original identifiers and field names',detail='Raw source IDs, selected/proposed wording, flags, count suggestions and complete local role/state candidates are preserved as reader provenance only.')],
                 source_verification=dict(errors=errors,complete_tex_partition_exact=True,group_and_component_text_checks_pass=not errors,
                                          released_text_freeze_hashes_match=all(x['hash_matches'] for x in freeze_entries),no_public_count_calculation=True))
    path=OUT/f'scan023_{reader}_source_coverage.json'
    path.write_text(json.dumps(support,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    summaries[reader]=dict(path=str(path.relative_to(ROOT)),sha256_utf8=hashlib.sha256(path.read_bytes()).hexdigest(),
                           source_text_counts=dict(differences=len(differences),doubts=len(doubts),inventory=len(inventory),notation=len(notation),
                                                   original_C_rows=len(original),graphical_groups=len(groups),component_records=len(component_checks),
                                                   graphical_commands=len(commands),complete_TeX_partition_spans=len(partition)),
                           source_verification=support['source_verification'])
(OUT/'scan023_AC_source_extraction_summary.json').write_text(json.dumps(summaries,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(summaries,ensure_ascii=False,indent=2))
