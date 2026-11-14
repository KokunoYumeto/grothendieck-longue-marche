#!/usr/bin/env python3
"""Build the separate initial-fixed-region note with exact source provenance."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import difflib
import json
import os
import re
import subprocess

ROOT = Path(__file__).resolve().parents[3]
BUILD = Path(__file__).resolve().parent
SOURCE = ROOT/'work/part_c/compact_family_initial_fixed_region.tex'

def bind(p):
    raw = p.read_bytes()
    return {'path':str(p.relative_to(ROOT)), 'bytes':len(raw),
            'sha256':sha256(raw).hexdigest()}

source = SOURCE.read_text()
before = BUILD/'before_self_review.tex'
before_text = before.read_text()
edits = [
    (r'\qquad \phi_f(g)f=g,qquad \phi_f(f)=\id_M.',
     r'\qquad \phi_f(g)f=g,\qquad \phi_f(f)=\id_M.'),
    (r'\sum_i\alpha_i=1,qquad \operatorname{supp}\alpha_i\subset U_i.',
     r'\sum_i\alpha_i=1,\qquad \operatorname{supp}\alpha_i\subset U_i.'),
    (r'\phi_{i,k}(e_{u,t_{i-1}})^{-1}quad(u\in U_i),',
     r'\phi_{i,k}(e_{u,t_{i-1}})^{-1}\quad(u\in U_i),'),
    (r'\qquad A_0(f)=\id,qquad A_t(f)^{-1}=A_t(f^{-1}).',
     r'\qquad A_0(f)=\id,\qquad A_t(f)^{-1}=A_t(f^{-1}).'),
    ('For $z=qc$ with $c=sx\\in C$ and $G_{u,t}^{\\pm1}(c)=tx\\in C\'$, one has\n'
     '\\[\n G_{u,t}^{\\pm1}(z)=qtx=ts^{-1}(z),\\qquad\n'
     ' G_{u,t}^{\\pm1}(z)\\in\\mathcal P(z)quad(z\\in O).',
     'For $z=qc$ choose $a\\in S$, $b\\in T$ with\n'
     '$c=ax\\in C$ and $G_{u,t}^{\\pm1}(c)=bx\\in C\'$. Then\n'
     '\\[\n G_{u,t}^{\\pm1}(z)=qbx=ba^{-1}(z),\\qquad\n'
     ' G_{u,t}^{\\pm1}(z)\\in\\mathcal P(z)\\quad(z\\in O).'),
]
forward = before_text
for old,new in edits:
    assert forward.count(old) == 1
    forward = forward.replace(old,new,1)
assert forward == source
inverse = source
for old,new in reversed(edits):
    assert inverse.count(new) == 1
    inverse = inverse.replace(new,old,1)
assert inverse == before_text
diff = ''.join(difflib.unified_diff(before_text.splitlines(True),source.splitlines(True),
    fromfile='before_self_review.tex',tofile=SOURCE.name))
(BUILD/'self_review_edits.diff').write_text(diff)
assert not re.search(r'(?<![\\A-Za-z])(?:q?quad)\b',source)
assert sum(line == r'\[' for line in source.splitlines()) == 19
assert sum(line == r'\]' for line in source.splitlines()) == 19
assert re.findall(r'\\tag\{IFR\.(\d+)\}',source) == [str(i) for i in range(1,20)]

template_path = ROOT/'work/part_c/compact_family_filled_carriers_and_expansions_build/note.tex'
preamble = template_path.read_text().split(r'\begin{document}',1)[0]
preamble = preamble.replace('LM4: Actual filled carriers and finite controlled expansions',
    'LM4: Compactly supported corrections to a common fixed region')
bib_path = ROOT/'deliverable/LM4_FINITE_GROUP_ACTIONS_references.bib'
bib_text = bib_path.read_text()
start = bib_text.index('@misc{A_Yagasaki2000,')
end = bib_text.index('\n}',start)+2
original_record = bib_text[start:end]
standalone_record = original_record.replace('@misc{A_Yagasaki2000,','@misc{C_Yagasaki2000,',1)
assert standalone_record.replace('@misc{C_Yagasaki2000,','@misc{A_Yagasaki2000,',1) == original_record
(BUILD/'registered_yagasaki_record.bib').write_text(original_record+'\n')
(BUILD/'note_references.bib').write_text(standalone_record+'\n')
suffix = '\n\\bibliographystyle{plain}\n\\bibliography{note_references}\n\\end{document}\n'
wrapper = preamble+'\\begin{document}\n'+source+suffix
(BUILD/'note.tex').write_text(wrapper)
assert wrapper[len(preamble+'\\begin{document}\n'):-len(suffix)] == source

env = os.environ.copy()
cache = ROOT/'work/tex_cache'
env['TEXMF'] = '{'+','.join([str(cache/'texmf'),str(cache/'var'),
    '/usr/share/texlive/texmf-dist','/usr/share/texmf','/etc/texmf'])+'}'
env['TEXMFVAR'] = str(cache/'var')
env['TEXMFCONFIG'] = str(cache/'config')
env['TEXMFCACHE'] = str(cache/'cache')
commands = []
for stage,cmd in enumerate([
        ['lualatex','-interaction=nonstopmode','-halt-on-error','note.tex'],
        ['bibtex','note'],
        ['lualatex','-interaction=nonstopmode','-halt-on-error','note.tex'],
        ['lualatex','-interaction=nonstopmode','-halt-on-error','note.tex']],1):
    run = subprocess.run(cmd,cwd=BUILD,env=env,capture_output=True)
    stdout,stderr = BUILD/f'stage_{stage}_stdout.txt',BUILD/f'stage_{stage}_stderr.txt'
    stdout.write_bytes(run.stdout)
    stderr.write_bytes(run.stderr)
    commands.append({'stage':stage,'command':cmd,'exit_code':run.returncode,
        'stdout':bind(stdout),'stderr':bind(stderr)})
    (BUILD/'build_commands.json').write_text(json.dumps(commands,indent=2)+'\n')
    assert run.returncode == 0,(stage,run.stdout.decode(errors='replace')[-4000:])
log = (BUILD/'note.log').read_text()
patterns = {
    'overfull_boxes':r'Overfull \\[hv]box',
    'underfull_boxes':r'Underfull \\[hv]box',
    'missing_characters':r'Missing character:',
    'undefined_control_sequences':r'Undefined control sequence',
    'undefined_reference_or_citation_lines':r'^.*(?:Reference|Citation).*undefined.*$',
    'latex_warnings':r'LaTeX Warning:',
    'package_warning_lines':r'^Package .* Warning:',
    'fatal_error_lines':r'^!|Fatal error|Emergency stop',
    'luaotfload_fallback_events':r'Error in luaotfload: reverting to OT1',
}
qa = {k:len(re.findall(v,log,re.M)) for k,v in patterns.items()}
render = ['pdftoppm','-png','-scale-to','1500',str(BUILD/'note.pdf'),str(BUILD/'page')]
run = subprocess.run(render,cwd=BUILD,capture_output=True)
(BUILD/'render_stdout.txt').write_bytes(run.stdout)
(BUILD/'render_stderr.txt').write_bytes(run.stderr)
assert run.returncode == 0
info = subprocess.run(['pdfinfo',str(BUILD/'note.pdf')],capture_output=True,check=True)
(BUILD/'pdfinfo.txt').write_bytes(info.stdout)
page_count = int(re.search(rb'^Pages:\s+(\d+)',info.stdout,re.M).group(1))
record = {
    'created_utc':datetime.now(timezone.utc).isoformat(),
    'source':bind(SOURCE),'source_lines':len(source.splitlines()),
    'before_self_review':bind(before),'self_review_exact_edits':[{'old':x,'new':y} for x,y in edits],
    'complete_forward_and_inverse_edit_equalities':True,'self_review_diff':bind(BUILD/'self_review_edits.diff'),
    'wrapper':bind(BUILD/'note.tex'),'wrapper_preamble_source':bind(template_path),
    'source_is_exact_wrapper_body':True,'source_display_pairs':19,'source_tags':list(range(1,20)),
    'registered_bibliography_source':bind(bib_path),'registered_record':bind(BUILD/'registered_yagasaki_record.bib'),
    'standalone_bibliography':bind(BUILD/'note_references.bib'),
    'bibliography_key_map':{'registered':'A_Yagasaki2000','source_and_standalone':'C_Yagasaki2000',
        'only_entry_heading_changed':True,'complete_forward_and_inverse_record_equality':True},
    'build_commands':bind(BUILD/'build_commands.json'),'log':bind(BUILD/'note.log'),
    'bibtex_log':bind(BUILD/'note.blg'),'pdf':bind(BUILD/'note.pdf'),'pdf_pages':page_count,
    'qa_counts':qa,'render_command':render,'render_exit_code':0,
    'rendered_images':[bind(p) for p in sorted(BUILD.glob('page-*.png'))],
    'rendering_does_not_certify_visual_review':True,'build_script':bind(Path(__file__).resolve()),
}
(BUILD/'build_result.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'source':record['source'],'source_lines':record['source_lines'],
    'pdf':record['pdf'],'pdf_pages':page_count,'qa_counts':qa},indent=2))
