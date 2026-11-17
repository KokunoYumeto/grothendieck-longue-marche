"""Pre-context structural check and immutable transcription manifest.

This is not a replacement for visual reading or a claim of TeX compilation.
"""
from pathlib import Path
from datetime import datetime,timezone
import re,csv,hashlib,json
ROOT=Path(__file__).resolve().parent
PREFIX='MPL_68_033-056+162-1+162-6'
expected=[33,34,36,37,38,39,40,41,42,43,44,45,46,48,50,51,52,53,54,55,56]
pages=sorted((ROOT/'pages').glob('*.tex'))
combined=ROOT/f'{PREFIX}_transcription.tex'
s=combined.read_text()
assert s=='\n'.join(p.read_text().rstrip()+'\n' for p in pages)
assert [int(x) for x in re.findall(r'\\scanpage\{(\d+)\}',s)]==expected
assert s.startswith('\\cotefile{68}\n\\scanpage{33}\n')
assert s.count('\\cotefile{')==1
level=0; stack=[]
for m in re.finditer(r'\\(?:begin|end)\{[^}]+\}|\\[A-Za-z]+|\\.|[{}]',s,re.S):
    t=m[0]
    if t=='{': level+=1
    elif t=='}': level-=1
    elif t.startswith('\\begin{'):stack.append(t[7:-1])
    elif t.startswith('\\end{'):
        name=t[5:-1]
        assert stack and stack.pop()==name,(name,stack)
    assert level>=0,(m.start(),t)
assert level==0 and not stack,(level,stack)
rows=list(csv.DictReader((ROOT/f'{PREFIX}_inventory.csv').open()))
assert len(rows)==510 and all(r['transcribed']=='yes' for r in rows)
assert sorted({int(r['scan']) for r in rows})==expected
assert len({r['element'] for r in rows})==len(rows)
log=(ROOT/'progress.log').read_text()
assert all(f'scan {n:03} audited ' in log for n in expected)
assert 'transcription frozen ' not in log
hashes={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in pages+[combined]}
(ROOT/'checksums.sha256').write_text(''.join(f'{h}  {p}\n' for p,h in hashes.items()))
report={
 'included_scans':expected,'page_files':len(pages),'inventory_rows':len(rows),
 'inventory_all_transcribed':True,'combined_matches_page_files':True,
 'balanced_braces_and_environments':True,'diagram_macros':s.count('\\diagram{'),
 'figure_macros':s.count('\\figure{'),'doubt_macros':s.count('\\unsure{'),
 'illegible_word_estimates':re.findall(r'\\illegible\{(\d+)\}',s),
 'full_tex_compilation':'unavailable: installed engine has no pdflatex.fmt, latex.ltx, article.cls or tikz-cd.sty',
 'context_contents_opened':False,
}
(ROOT/'records'/'validation_before_freeze.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (ROOT/'progress.log').open('a') as f:
    f.write('pre-freeze validation: 21 ordered page files; 510 inventory rows all yes; combined matches pages exactly; braces and environments balanced. TeX compilation unavailable because the installed engine lacks its formats and packages; no successful compilation is claimed.\n')
    for p,h in hashes.items():f.write(f'SHA-256 {h}  {p}\n')
    f.write(f'transcription frozen {now}\n')
print('Transcription frozen',now,'with',len(hashes),'SHA-256 hashes.')
