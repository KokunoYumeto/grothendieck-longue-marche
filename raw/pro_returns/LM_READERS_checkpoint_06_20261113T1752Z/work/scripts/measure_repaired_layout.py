"""Regenerate isolated diagrams after explicit layout patches."""
from pathlib import Path
import json,re,sys
from layout_repairs import repair
ROOT=Path(__file__).resolve().parents[2];D=ROOT/'work/layout_probes'
allrows=json.loads((D/'diagrams.json').read_text());packs={}
only=set(map(int,sys.argv[1:]))
for lang in ('fr','en'):
 t=(D/f'measure_{lang}.tex').read_text();pre=t[:t.index('\\typeout{LMSTART')];parts=[pre]
 for r in allrows:
  if r['lang']!=lang or (only and r['id'] not in only):continue
  key=(lang,r['package']);folder='fr/texts' if lang=='fr' else 'en/packages';suf='' if lang=='fr' else '_en'
  orig=(ROOT/'sources'/folder/(r['package']+suf+'.tex')).read_text()
  if key not in packs:packs[key]=repair(orig,r['package'],lang)[0]
  raw=packs[key];sc=next(s for s in re.split(r'(?=\\scanpage\{)',raw) if s.startswith('\\scanpage{'+str(r['scan'])+'}'))
  origsc=next(s for s in re.split(r'(?=\\scanpage\{)',orig) if s.startswith('\\scanpage{'+str(r['scan'])+'}'))
  pat=r'\\begin\{'+r['environment']+r'\}.*?\\end\{'+r['environment']+r'\}'
  oldms=list(re.finditer(pat,origsc,re.S));ordn=next(i for i,m in enumerate(oldms) if m[0]==r['old']);ms=list(re.finditer(pat,sc,re.S));block=ms[ordn][0]
  parts+=['\\typeout{LMSTART '+str(r['id'])+'}\n',r'\setbox0=\hbox\bgroup'+'\n',block,'\n\\egroup\n\\typeout{LMWIDTH '+str(r['id'])+r' \the\wd0 HEIGHT \the\ht0 DEPTH \the\dp0}'+'\n']
 parts+=['\\end{document}\n'];name=f'measure_final_{lang}' if only else f'measure_repaired_{lang}';(D/(name+'.tex')).write_text(''.join(parts))
 print(name, 'prepared',flush=True)
