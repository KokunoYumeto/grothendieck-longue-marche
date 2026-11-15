#!/usr/bin/env python3
"""Check the actual included paper statements against the delivered CSV."""
from pathlib import Path
import csv,json,re
root=Path(__file__).resolve().parents[1]
visited=set()
def read_tex(path):
    path=path.resolve()
    if path in visited:return ''
    visited.add(path)
    text=path.read_text()
    chunks=[text]
    for match in re.finditer(r'\\input\{([^}]+)\}',text):
        child=root/match[1]
        if child.suffix!='.tex':child=child.with_suffix('.tex')
        if child.exists():chunks.append(read_tex(child))
    return '\n'.join(chunks)
text=read_tex(root/'LM8_PUSH_paper.tex')
statements=re.findall(r'\\begin\{statement\}\{([^}]+)\}\{([^}]+)\}',text)
rows=list(csv.DictReader((root/'LM8_PUSH_results.csv').open()))
paper={key:status for key,status in statements}
register={row['id']:row['status'] for row in rows}
report={
 'included_tex_files':len(visited),'paper_statements':len(statements),
 'register_rows':len(rows),
 'duplicate_paper_ids':sorted(k for k in paper if sum(a==k for a,b in statements)>1),
 'unregistered_statements':sorted(set(paper)-set(register)),
 'rows_without_statement':sorted(set(register)-set(paper)),
 'status_mismatches':{key:[paper[key],register[key]] for key in paper.keys()&register.keys() if paper[key]!=register[key]},
}
out=json.dumps(report,indent=2)+'\n'
(root/'code/verify_register.out').write_text(out)
print(out,end='')
assert not any(report[key] for key in ['duplicate_paper_ids','unregistered_statements','rows_without_statement','status_mismatches'])
