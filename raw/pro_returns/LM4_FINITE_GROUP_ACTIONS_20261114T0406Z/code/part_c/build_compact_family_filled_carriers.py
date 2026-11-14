#!/usr/bin/env python3
"""Build the separate unnumbered carrier note and preserve its exact edit map."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import difflib
import json
import os
import subprocess

ROOT=Path(__file__).resolve().parents[3]
SOURCE=ROOT/'work/part_c/compact_family_filled_carriers_and_expansions.tex'
BUILD=ROOT/'work/part_c/compact_family_filled_carriers_and_expansions_build'
BUILD.mkdir(exist_ok=True)

def bind(p):
    b=p.read_bytes()
    return {'path':str(p.relative_to(ROOT)),'bytes':len(b),'sha256':sha256(b).hexdigest()}

before=BUILD/'before_clarifications.tex'
assert bind(before)['sha256']=='5f604e24a2b49487207b9a0c88a3cc86aab790e6e82f3d889576b0ecdee3522b'
before_text=before.read_text()
source=SOURCE.read_text()
replacements=[
    ('functions on the bounded ranges of the metrics by','functions for every $a\\geq0$ by'),
    ('second inclusion; the two factors prove the third.\n',
     'second inclusion; the two factors prove the third.\nHere $S$ is closed in $O$ by local finiteness of the\nclosed disks, and $h_uS$ is closed by the homeomorphism\n$h_u$. Thus taking closure in $O$ preserves the third\ninclusion.\n'),
    ('at most1.','at most $1$.'),
    ('the accumulation point0','the accumulation point $0$'),
    ('Identifying0 and1','Identifying $0$ and $1$'),
    ('joint continuity at0.','joint continuity at $0$.'),
]
transport=before_text
for old,new in replacements:
    assert transport.count(old)==1
    transport=transport.replace(old,new,1)
assert transport==source
inverse=source
for old,new in reversed(replacements):
    assert inverse.count(new)==1
    inverse=inverse.replace(new,old,1)
assert inverse==before_text
diff=''.join(difflib.unified_diff(before_text.splitlines(True),source.splitlines(True),
        fromfile='before_clarifications.tex',tofile=SOURCE.name))
(BUILD/'clarifications.diff').write_text(diff)

template=(ROOT/'work/part_c/compact_family_displacement_graph_build/note.tex').read_text()
preamble=template.split(r'\begin{document}',1)[0]
preamble=preamble.replace('LM4: Finite group actions, loop structures, and profinite extensions',
                           'LM4: Actual filled carriers and finite controlled expansions')
wrapper=preamble+'\\begin{document}\n'+source+'\\end{document}\n'
(BUILD/'note.tex').write_text(wrapper)
assert (BUILD/'note.tex').read_text().split('\\begin{document}\n',1)[1].rsplit('\\end{document}\n',1)[0]==source
env=os.environ.copy()
cache=ROOT/'work/tex_cache'
env['TEXMF']='{'+','.join([str(cache/'texmf'),str(cache/'var'),
    '/usr/share/texlive/texmf-dist','/usr/share/texmf','/etc/texmf'])+'}'
env['TEXMFVAR']=str(cache/'var')
env['TEXMFCONFIG']=str(cache/'config')
env['TEXMFCACHE']=str(cache/'cache')
commands=[]
for stage in (1,2):
    cmd=['lualatex','-interaction=nonstopmode','-halt-on-error','note.tex']
    run=subprocess.run(cmd,cwd=BUILD,env=env,capture_output=True)
    stdout=BUILD/f'stage_{stage}_stdout.txt'
    stderr=BUILD/f'stage_{stage}_stderr.txt'
    stdout.write_bytes(run.stdout);stderr.write_bytes(run.stderr)
    commands.append({'stage':stage,'command':cmd,'exit_code':run.returncode,
                     'stdout':bind(stdout),'stderr':bind(stderr)})
    (BUILD/'build_commands.json').write_text(json.dumps(commands,indent=2)+'\n')
    assert run.returncode==0,(stage,run.stdout.decode(errors='replace')[-3000:])
log=(BUILD/'note.log').read_text()
qa={name:log.count(pattern) for name,pattern in {
    'overfull_boxes':'Overfull \\', 'underfull_boxes':'Underfull \\',
    'missing_characters':'Missing character:',
    'undefined_control_sequences':'Undefined control sequence',
    'fatal_errors':'Fatal error',
}.items()}
render=['pdftoppm','-png','-scale-to','1500',str(BUILD/'note.pdf'),str(BUILD/'page')]
run=subprocess.run(render,cwd=BUILD,capture_output=True)
(BUILD/'render_stdout.txt').write_bytes(run.stdout)
(BUILD/'render_stderr.txt').write_bytes(run.stderr)
assert run.returncode==0
record={'created_utc':datetime.now(timezone.utc).isoformat(),'before':bind(before),
        'source':bind(SOURCE),'source_lines':len(source.splitlines()),
        'clarification_replacements':[{'old':a,'new':b} for a,b in replacements],
        'entire_forward_and_inverse_text_equalities':True,'diff':bind(BUILD/'clarifications.diff'),
        'wrapper':bind(BUILD/'note.tex'),'source_is_exact_wrapper_body':True,
        'build_commands':bind(BUILD/'build_commands.json'),'log':bind(BUILD/'note.log'),
        'pdf':bind(BUILD/'note.pdf'),'qa_counts':qa,
        'render_command':render,'render_exit_code':0,
        'rendered_images':[bind(p) for p in sorted(BUILD.glob('page-*.png'))],
        'rendering_does_not_certify_visual_review':True,'build_script':bind(Path(__file__).resolve())}
(BUILD/'build_result.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'source':record['source'],'source_lines':record['source_lines'],
                  'pdf':record['pdf'],'qa_counts':qa,'image_count':len(record['rendered_images'])},indent=2))
