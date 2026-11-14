#!/usr/bin/env python3
"""Freeze the complete reviewed E.118 proof and owned evidence."""
from pathlib import Path
import hashlib
import json

root=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
ledger=root/'ledger'
peer=root.parent/'bc_e118_audit'
assert sha(peer/'audit.json')=='c5446f85955b5e46e44dec25583aaefd62ff395ed39dddc0013d3ad8f3850a3f'
assert sha(peer/'audit.md')=='14f1aec7ba0710dbf3c8e6f7c86ff48c85bd839e5c87aa72ba4ab5bab89787a2'
audit=json.loads((peer/'audit.json').read_text())
assert audit['status']=='PASS' and audit['fresh_replay']['exit_code']==0
assert audit['fresh_replay']['exclusions']==[]
assert audit['proof_sha256']==sha(root/'sections/E_quartic_five_numerical.tex')
for name,row in audit['fresh_replay']['comparisons'].items():
    assert row['byte_identical'] and sha(root/'code'/name)==row['sha256']
    assert sha(peer/'code'/name)==row['sha256']
record={'status':'PASS','statement':'E.118','peer':'/root/bc_fermat',
        'audit_json':{'path':'bc_e118_audit/audit.json','sha256':sha(peer/'audit.json')},
        'audit_md':{'path':'bc_e118_audit/audit.md','sha256':sha(peer/'audit.md')},
        'scope':'Complete corrected proof and source read, exact E112/E115 dependency-map reread, fresh no-input GP/Python reconstruction with complete byte identity and zero exclusions, plus separately written order800 corestriction/cocycle calculation.',
        'root_receipt':'Root read both complete audit records and the entire independent corestriction program with its actual output.',
        'correction':'The literal tensor-extension map and its inverse are written explicitly; the actual rational slice is proved separately through the finite-support correcting cochain.'}
(ledger/'e_quartic_five_numerical_peer.json').write_text(json.dumps(record,indent=2)+'\n')
p=ledger/'e_quartic_five_numerical_report.md'
t=p.read_text();t+='\n## Completed independent review\n\nThe complete corrected proof and both mathematical sources passed independent review. A fresh reconstruction with no input certificate reproduced all six source/output/JSON files byte-for-byte, with no excluded fields. A separately written program checked25,600 corestriction terms,800 representative-change formulas and640,000 cocycle identities in the actual order800 semidirect product. Root read the complete audit and this additional program/output. Exact proof and audit hashes are in the peer ledger.\n'
p.write_text(t)
manifest_path=ledger/'e_quartic_five_numerical_manifest.json'
assert not manifest_path.exists()
files=[]
for folder in ['sections','code','ledger','inputs']:
    for p in sorted((root/folder).rglob('*')):
        if not p.is_file() or p==manifest_path or '__pycache__' in p.parts:continue
        if p in [Path(__file__).with_suffix('.out'),Path(__file__).with_suffix('.err')]:continue
        files.append({'path':str(p.relative_to(root)),'bytes':p.stat().st_size,'sha256':sha(p)})
manifest={'statement':'E.118','status':'FROZEN_AUTHOR_AND_INDEPENDENT_PEER_PASS','files':files,
          'excluded_own_outputs':['code/e_quartic_five_numerical_freeze.out','code/e_quartic_five_numerical_freeze.err'],
          'render_evidence':'Final and historical page hashes plus actual viewing scopes are recorded in the visual ledger. Owned QA images are integrated separately.',
          'portable_rebuild':'python code/e_quartic_five_numerical_verify.py --gp /absolute/path/to/gp'}
manifest_path.write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({'status':'PASS','statement':'E.118','files':len(files),'manifest_sha256':sha(manifest_path),'proof_sha256':audit['proof_sha256']},indent=2))
