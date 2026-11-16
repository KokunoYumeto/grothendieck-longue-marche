#!/usr/bin/env python3
"""Reproduce the independent D77 audit without changing owner outputs."""
from pathlib import Path
import ast,hashlib,json
root=Path(__file__).resolve().parents[1]
src=root/'notes/de_local_boundary_certificate.py'
tree=ast.parse(src.read_text());body=[]
for node in tree.body:
    if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='path' for t in node.targets):
        break
    body.append(node)
namespace={'__file__':str(src)}
exec(compile(ast.Module(body=body,type_ignores=[]),str(src),'exec'),namespace)
expected=json.loads(src.with_suffix('.json').read_text())
assert namespace['out']==expected
print(json.dumps({'PASS':True,'all_certificate_fields_equal':True,
    'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),
    'source_write_statements_not_executed':True,'result':namespace['out']},indent=2))
