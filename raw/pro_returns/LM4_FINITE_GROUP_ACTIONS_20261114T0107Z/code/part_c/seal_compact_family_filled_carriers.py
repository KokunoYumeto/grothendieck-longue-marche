#!/usr/bin/env python3
"""Seal the actual finite-carrier source, its four-page QA and provenance."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json
import re
import struct

ROOT=Path(__file__).resolve().parents[3]
STEM='compact_family_filled_carriers_and_expansions'
SOURCE=ROOT/f'work/part_c/{STEM}.tex'
REPORT=ROOT/f'work/part_c/{STEM}_report.txt'
BUILD=ROOT/f'work/part_c/{STEM}_build'
TARGET=ROOT/f'work/part_c/{STEM}_result.json'

def bind(p):
    p=ROOT/p if isinstance(p,str) else p
    data=p.read_bytes()
    return {'path':str(p.relative_to(ROOT)),'bytes':len(data),'sha256':sha256(data).hexdigest()}

assert not TARGET.exists(), 'Do not overwrite a frozen note record.'
assert bind(SOURCE)['sha256']=='7a88ef1bdfa3fe3fc4a4c2588db43be9047ff6ea3d7ef6c0ab2c02a01f22f098'
source=SOURCE.read_text()
assert len(source.splitlines())==348
assert re.findall(r'\\tag\{FCE\.(\d+)\}',source)==[str(i) for i in range(1,16)]
assert sum(line.strip()==r'\[' for line in source.splitlines())==15
assert sum(line.strip()==r'\]' for line in source.splitlines())==15
build=json.loads((BUILD/'build_result.json').read_text())
for key in ['before','source','diff','wrapper','build_commands','log','pdf','build_script']:
    assert bind(build[key]['path'])==build[key]
assert build['entire_forward_and_inverse_text_equalities']
before=(ROOT/build['before']['path']).read_text()
forward=before
for row in build['clarification_replacements']:
    assert forward.count(row['old'])==1
    forward=forward.replace(row['old'],row['new'],1)
assert forward==source
backward=source
for row in reversed(build['clarification_replacements']):
    assert backward.count(row['new'])==1
    backward=backward.replace(row['new'],row['old'],1)
assert backward==before

dependencies={
    'work/part_b/c81.tex':'d24ec0b95c132e56b14f1775339b64799c02f032589a3cd9d0f05379f5846267',
    'work/part_b/c83.tex':'33c766356d2124a148167158c326bdcf70757088ebc2f9a9a913aba09b9550e1',
    'work/part_b/c88.tex':'683ee6d104493c2945aa9af7e6e37c7770e39f0827c7cf42b1aa3e29612a2166',
    'work/part_b/c89.tex':'fdb210d491cb66ebb4ab9f1fef1b41427d4b7d0e3b2a77bea197d261d6191299',
    'work/part_c/c91.tex':'0b5db75c25411d069d4316995b410faab63b5c624bed7f4044a963e27d1952ff',
    'work/part_c/c92.tex':'e978d4c54fa14090d67e1fd0620561bd251a8e3673132284aa144030b129ad7c',
    'work/part_c/compact_family_displacement_graph.tex':'e3f724056664f2e1e2ae164b2e046b1dd8f5cd4495a66b45866b88191ef58338',
}
for path,digest in dependencies.items():
    assert bind(path)['sha256']==digest
previous_qa=json.loads((ROOT/'work/part_c/render_review_611.json').read_text())
assert bind(previous_qa['pdf']['path'])['sha256']==previous_qa['pdf']['sha256']

log=(BUILD/'note.log').read_text()
stages=[(BUILD/f'stage_{i}_stdout.txt').read_text() for i in (1,2)]
patterns={
    'overfull_boxes':r'Overfull \\[hv]box',
    'underfull_boxes':r'Underfull \\[hv]box',
    'missing_characters':r'Missing character:',
    'undefined_control_sequences':r'Undefined control sequence',
    'undefined_references_or_citations':r'^.*(?:Reference|Citation).*undefined.*$',
    'fatal_errors':r'^!|Fatal error|Emergency stop',
    'latex_warnings':r'LaTeX Warning:',
    'package_warnings':r'^Package .* Warning:',
    'luaotfload_fallback_events':r'Error in luaotfload: reverting to OT1',
}
def counts(text):
    return {name:len(re.findall(pattern,text,re.M)) for name,pattern in patterns.items()}
final_counts=counts(log)
assert final_counts=={k:(1 if k=='luaotfload_fallback_events' else 0) for k in patterns}
assert len(log.splitlines())==692 and '4 pages, 182031 bytes' in log
assert 'has not changed' in log
commands=json.loads((BUILD/'build_commands.json').read_text())
assert len(commands)==2 and all(row['exit_code']==0 for row in commands)
for row in commands:
    for key in ['stdout','stderr']:
        assert bind(row[key]['path'])==row[key]
assert counts(stages[0])['package_warnings']==1
assert counts(stages[1])['package_warnings']==0

observations={
    1:'Metric comparisons for all nonnegative arguments, the actual envelopes and all Fill identities are clear; every tag and footer fits.',
    2:'Actual arc-family bound and the full finite expansion/inverse formulas are legible, including the entire disk-boundary pasting and based fixed-region statement.',
    3:'Both-stage correction, inverse displacement bounds and closed support-carrier inclusion are clear; the explicit radial maps and inverses fit without clipping.',
    4:'Uniform estimates, dyadic actual loop and nullhomotopy, deck-step obstruction proof and exact retained global scope are legible.',
}
images=[]
for page,row in enumerate(build['rendered_images'],1):
    assert bind(row['path'])==row
    raw=(ROOT/row['path']).read_bytes()
    assert raw[:8]==b'\x89PNG\r\n\x1a\n'
    width,height=struct.unpack('>II',raw[16:24])
    images.append({**row,'page':page,'pixel_width':width,'pixel_height':height,
                   'actually_viewed':True,'result':'PASS','observation':observations[page]})
assert len(images)==4

record={
    'title':'Actual filled carriers and finite controlled expansions',
    'status':'PROVED_UNNUMBERED_CONTINUATION; author full self-review and complete standalone visual/build QA PASS; final independent acceptance pending',
    'author':'/root/c89_review_and_general_c','sealed_utc':datetime.now(timezone.utc).isoformat(),
    'source':bind(SOURCE),'source_lines':348,'report':bind(REPORT),
    'equation_tags':[f'FCE.{i}' for i in range(1,16)],'standalone_display_pairs':15,
    'full_source_self_review':True,'prior_root_full_read_lines':344,
    'prior_root_acceptance_scope':'Mathematics accepted subject to comparison-modulus domain and carrier-closedness clarifications; both now explicit. Final exact-source acceptance pending.',
    'clarification_provenance':{'before':build['before'],'after':bind(SOURCE),'diff':build['diff'],
        'exact_replacements':build['clarification_replacements'],
        'entire_forward_and_inverse_equalities_verified':True,
        'mathematical_clarifications':2,'adjacent_number_spacing_fixes':4},
    'proved_results':[
        'Both exact identity-map topology comparisons between the original d and fixed-coordinate Euclidean e metrics, including all original operator sup metrics.',
        'Actual compact-family forward and inverse C0 displacement envelopes and common positive C0 majorant.',
        'Exact q Fill(A)=Fill(qA), compact connected filled sets, and diam_eQ Fill(A)=diam_eQ A.',
        'Diameter bound for the filled union of an actual arc and all given-family images, uniformly over every original q.',
        'Explicit local fixed-region expansion with both branch inverses, equivariant paste, original-circle continuity and based conjugation deformation.',
        'Exact two-family correction and inverse, forward/inverse displacement bounds and closed interior support-carrier inclusion.',
        'Actual radial cylinder example, explicit small-displacement based loop and nullhomotopy, and proof that one specified disk-paste stage cannot perform its deck-step correction.',
    ],
    'exact_family_deformation':'H_(u,t)=tau_t h_u tau_t^(-1)',
    'exact_left_correction':'A_(u,t)=tau_t (h_u tau_t^(-1) h_u^(-1))',
    'original_uniform_bound':'D_e(H_(u,t),h_u)<=4 s_D+2 alpha_D^++2 alpha_D^-; separate original d bounds use omega_(e,d) on each map/inverse bound.',
    'frozen_dependencies_and_scope_sources_unchanged':[bind(p) for p in dependencies],
    'new_primary_literature_used':False,'no_prior_frozen_sources_changed':True,
    'current_manuscript_pdf_unchanged':{k:previous_qa['pdf'][k] for k in ['path','bytes','sha256']},
    'build':{'record':bind(BUILD/'build_result.json'),'wrapper':build['wrapper'],'source_is_exact_wrapper_body':True,
        'pdf':{**build['pdf'],'pages':4},'commands':commands,'full_final_log':{**bind(BUILD/'note.log'),'lines':692,'read_in_full':True},
        'both_stage_outputs_read_in_full':True,'final_notice_counts':final_counts,
        'stage_notice_counts':[{'stage':i+1,**counts(s)} for i,s in enumerate(stages)],
        'notices':'Inherited luaotfload fallback once per TeX pass. First pass requested outline rerun; final pass has no warning and reports unchanged outline.',
        'initial_runtime_failure':{'reason':'Initial TEXMFVAR pointed to texmf instead of the existing project var tree, so lualatex.fmt was not found. Reused the project TeX search/cache paths; mathematical source unchanged.',
            'records':[bind(BUILD/name) for name in ['initial_format_failure_build_commands.json','initial_format_failure_stage_1_stdout.txt','initial_format_failure_stage_1_stderr.txt']]},
        'builder':build['build_script']},
    'visual_review':{'pages_actually_viewed':[1,2,3,4],'actual_view_groups':[[1,2],[3,4]],
        'maximum_images_per_call':2,'all_pages_clear':True,'defects':[],'images':images},
    'unresolved':[
        'Construction of an initial common fixed region for every original compact based family.',
        'Compatible controlled fixing stages across all graph edges and essential cycles.',
        'An infinite composition with joint original map-and-inverse continuity and exact deck labels.',
        'A full noncompact contraction or positive-homotopy conclusion for the general C12 target.'
    ],
    'C83_infinite_evaluation_obstruction_retained':True,'new_numbered_claim_proposed':False,
    'sealer':bind(Path(__file__).resolve()),
}
TARGET.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'source':bind(SOURCE),'report':bind(REPORT),'metadata':bind(TARGET),
                  'pdf':build['pdf'],'diff':build['diff']},indent=2))
