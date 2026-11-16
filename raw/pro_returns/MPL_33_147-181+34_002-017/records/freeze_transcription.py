from pathlib import Path
import sys,csv,re,hashlib,shutil
sys.path.insert(0,str(Path(__file__).parent))
from workflow import ROOT,PREFIX,utc,update_doubts
from latex_scan import escaped,macro_arguments
log=ROOT/'progress.log';assert 'transcription frozen ' not in log.read_text()
files=sorted((ROOT/'pages').glob('*.tex'))
expected=[(33,n) for n in range(147,182) if n!=169]+[(34,n) for n in range(3,18)]
assert [tuple(map(int,re.search(r'_(\d+)_scan(\d+)',p.name).groups())) for p in files]==expected
for p in files:
 t=p.read_text();stack=[]
 for i,c in enumerate(t):
  if escaped(t,i):continue
  if c=='{':stack.append(i)
  elif c=='}':assert stack,p.name;stack.pop()
 assert not stack,p.name
 assert len(macro_arguments(t,'scanpage'))==1
 assert '\\includegraphics' not in t
for c,n in expected:
 assert re.search(rf'^scan {n:03d} audited .+\[cote {c}\]$',log.read_text(),re.M),(c,n)
rows=list(csv.DictReader((ROOT/f'{PREFIX}_inventory.csv').open()))
assert {(int(r['cote']),int(r['scan'])) for r in rows}==set(expected)
assert all(r['transcribed']=='yes' for r in rows)
assert len({r['element'] for r in rows})==len(rows)
assert {r['kind'] for r in rows}<={'text','display','diagram','drawing','margin note','insertion','deletion'}
combined=ROOT/f'{PREFIX}_transcription.tex'
assert combined.read_text()=='\n'.join(p.read_text().rstrip() for p in files)+'\n'
assert combined.read_text().startswith('\\cotefile{33}\n\\scanpage{147}')
update_doubts()
shutil.copy2('/tmp/mpl_latex_qa/compile_check.log',ROOT/'records/compile_validation.log')
shutil.copy2('/tmp/mpl_latex_qa/compile_stdout.txt',ROOT/'records/compile_validation_stdout.txt')
assert 'Output written on' in Path('/tmp/mpl_latex_qa/compile_stdout.txt').read_text()
assert not re.search(r'^!|Missing character|Warning:|Overfull',Path('/tmp/mpl_latex_qa/compile_check.log').read_text(),re.M)
with (ROOT/'records/audit_observations.md').open('a') as f:
 f.write('\n## LaTeX validation before freeze\n\nThe combined fragment compiled successfully with a validation wrapper: 49 source leaves plus a wrapper heading produce 50 validation pages. No LaTeX warnings, missing characters or overfull boxes remained. Technical source changes were explicit ampersand replacement in 26 tikz-cd environments nested in macro arguments; removal of redundant dollar delimiters around the circled alpha on 33/152 and the underlined 2d−1 on 33/176; text-mode encoding of ét on 33/165; and a relax token before the literal opening bracket in the gathered expression on 33/170. No mathematical content or unfinished expression was completed. The wrapper prints edit/doubt contents for syntax validation and is not a finished diplomatic edition layout. The initial system format and font caches were absent; local format initialization and explicit installed font maps enabled validation.\n')
manifest=[]
for p in files+[combined]:manifest.append(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+str(p.relative_to(ROOT)))
(ROOT/'records/frozen_sha256.txt').write_text('\n'.join(manifest)+'\n')
with log.open('a') as f:
 f.write(f'pre-freeze validation passed: 49 page files, 49 second audits, {len(rows)} inventory elements, successful full LaTeX compilation {utc()}\n')
 for x in manifest:f.write('SHA-256 '+x+'\n')
 f.write(f'transcription frozen {utc()}\n')
print('TRANSCRIPTION FROZEN',utc(),'; 50 SHA-256 hashes written')
