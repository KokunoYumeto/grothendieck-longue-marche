"""Reconstruct the supplied pre-pass source from documented script differences."""
from pathlib import Path
import ast,re,csv,json
ROOT=Path(__file__).resolve().parents[2]
def constant(path,name):
 tree=ast.parse(path.read_text())
 for x in tree.body:
  if isinstance(x,ast.Assign) and any(isinstance(y,ast.Name) and y.id==name for y in x.targets):
   return ast.literal_eval(x.value)
t=(ROOT/'sources/draft_readers/LaLongueMarche_English.tex').read_text()
start=t.index('\n% ---- typesetting pass');end=t.index('% ---- end of the typesetting pass ----')+len('% ---- end of the typesetting pass ----\n')
t=t[:start]+t[end:]
new=constant(ROOT/'sources/en/scripts/build.py','NOTE');old=constant(ROOT/'sources/en/scripts/build_before_typeset_pass_20261113.py','NOTE')
assert new in t
t=t.replace(new,old)
t=re.sub(r'\\LMcote\{140-[1-4]\}\n','',t)
ls=t.splitlines();rows=[];bad=[]
for i,r in enumerate(csv.DictReader((ROOT/'sources/typeset/OVERFULL_BEFORE.tsv').open(),delimiter='\t'),1):
 a,b=int(r['first_line']),int(r['last_line']);snippet=' '.join(ls[a-1:b])[:300]
 # Source report normalizes spaces after assembling rows.
 before='\n'.join(ls[:b]);pk=list(re.finditer(r'% package (\S+)',before));sc=list(re.finditer(r'\\scanpage\{(\d+)',before));co=list(re.finditer(r'\\section\*\{Cote (140-\d)\}',before))
 test=' '.join(snippet.split())==' '.join(r['source'].split())
 if not test:bad.append((i,a,b,repr(snippet[:60]),repr(r['source'][:60])))
 rows.append(dict(record=i,**r,package=pk[-1][1],cote=co[-1][1],scan=int(sc[-1][1]),source_line=a-int(before[:pk[-1].end()].count('\n'))-1,anchor_exact=test))
(ROOT/'work/data/layout_before_sites.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
(ROOT/'work/layout_probes/English_before_reconstructed.tex').write_text(t)
print('mapped',len(rows),'anchor mismatches',len(bad));print(bad[:15])
