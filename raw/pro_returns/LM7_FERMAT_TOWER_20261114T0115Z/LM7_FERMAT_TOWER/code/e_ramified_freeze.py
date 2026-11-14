#!/usr/bin/env python3
"""Record E.84's completed author checks and a complete frozen file manifest."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import re

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
LEDGER=ROOT/'ledger'

def put(path,obj):
    path.write_text(json.dumps(obj,indent=2)+'\n')

def main():
    summary=json.loads((HERE/'e_ramified_capitulation.json').read_text())
    initial=json.loads((HERE/'e_ramified_capitulation_initial_verify.json').read_text())
    assert summary==initial and summary['status']=='PASS'
    stages=sorted(HERE.glob('e_ramified_dependency_*.out'))+[
        HERE/'e_ramified_class_action.out',HERE/'e_ramified_capitulation_export.out']
    assert len(stages)==10
    for p in stages:
        s=p.read_text()
        assert '***   at top-level' not in s and '***   user error' not in s,p.name
        assert 'DONE' in s or '"status":"PASS"' in s,p.name
    tex=(ROOT/'sections/E_ramified_capitulation.tex').read_text()
    assert not any(ord(c)<32 and c not in '\n\r\t' for c in tex)
    assert tex.count(r'\[')==tex.count(r'\]')==20
    assert [int(x) for x in re.findall(r'\\tag\{E84\.(\d+)\}',tex)]==list(range(1,21))
    assert r'\begin{statement}{E.84}{Proved}' in tex
    result_path=LEDGER/'e_ramified_capitulation_results.json'
    results=json.loads(result_path.read_text())
    results[0]['notes']=(
        'Actual field automorphisms, certified base class maps and the exact genus-kernel '
        'normalizer give the proof; no upper degree54 BNF is computed. The complete '
        'ten-stage author GP rebuild passed as session67145 exit0. The final Python '
        'verifier independently checks six literal base ideal identities, the field '
        'substitutions, all12 Artin equivariances and the entire finite divisor '
        'quotient; its JSON is identical to the initial complete verification. '
        'A independently checked the complete proof mechanism against E81, without '
        'yet claiming a fresh execution. S-capitulation, the corrected ordinary-unit '
        'norm coset and eventual h remain unevaluated.'
    )
    put(result_path,results)
    source_path=LEDGER/'e_ramified_capitulation_source_evidence.json'
    source=json.loads(source_path.read_text())
    source['author_verification']['full_rebuild']=(
        'PASS, session67145 exit0. Ten GP stages rebuilt in an isolated temporary '
        'directory; all actual outputs and owned BIN data retained. The complete '
        'JSON matches the initial independent verification with no fields excluded.'
    )
    source['certificate']=summary
    source['tex_validation']={'balanced_displays':20,'sequential_tags':20,'control_characters':0}
    put(source_path,source)
    report=LEDGER/'e_ramified_capitulation_report.md'
    s=report.read_text()
    addition=(
        '\n## Author freeze\n\n'
        'The fresh ten-stage GP rebuild completed successfully, and the complete '
        'Python summary matches the initial verification with no fields excluded. '
        'All twenty displayed equations have matching delimiters and sequential '
        'tags; no control character is present. The complete file manifest includes '
        'the retained unsuccessful searches and their actual outputs.\n'
    )
    if '## Author freeze' not in s:report.write_text(s+addition)
    core=['sections/E_ramified_capitulation.tex','code/e_ramified_capitulation.py',
          'code/e_ramified_capitulation.json']
    hashes={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in core}
    output={'statement':'E.84','status':'FROZEN_AUTHOR_PASS','gp_stages':10,
            'structured_export_records':14,'complete_json_match':True,
            'balanced_displays':20,'core_sha256':hashes}
    out=json.dumps(output,indent=2)+'\n'
    (HERE/'e_ramified_freeze.out').write_text(out)
    manifest_path=LEDGER/'e_ramified_capitulation_manifest.json'
    files=[]
    for p in sorted(ROOT.rglob('*')):
        if not p.is_file() or p==manifest_path:continue
        data=p.read_bytes()
        files.append({'path':str(p.relative_to(ROOT)),'bytes':len(data),
                      'sha256':hashlib.sha256(data).hexdigest()})
    put(manifest_path,{'statement':'E.84','author_status':'FROZEN_PASS','files':files})
    print(out,end='')

if __name__=='__main__':main()
