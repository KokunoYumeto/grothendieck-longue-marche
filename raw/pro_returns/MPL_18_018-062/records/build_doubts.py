from pathlib import Path
import json,re

b=Path(__file__).resolve().parents[1]
ledger=[json.loads(l) for l in (b/'records/doubts.jsonl').read_text().splitlines()]

def arguments(s, name):
    for m in re.finditer(r'\\'+re.escape(name)+r'\{',s):
        depth=1; j=m.end()
        while j<len(s) and depth:
            c=s[j]
            escaped=j>0 and s[j-1]=='\\' and (j<2 or s[j-2]!='\\')
            if not escaped:
                if c=='{':depth+=1
                elif c=='}':depth-=1
            j+=1
        assert depth==0,(name,m.start())
        yield m.start(),j,s[m.end():j-1]

def split_reading(s):
    depth=0
    for i,c in enumerate(s):
        if c=='{':depth+=1
        elif c=='}':depth-=1
        elif c=='|' and depth==0:return s[:i],s[i+1:]
    return s,''

def cell(s):return str(s).replace('|','\\|').replace('\n',' ')

out=(b/'records/notation.md').read_text()
out+='\n# Doubts in the final transcription\n\n'
out+='Every occurrence of `\\unsure` in the page files is indexed below, including repetitions. “TeX line” locates the supplied page file rather than counting the manuscript’s physical lines; a physical position is supplied where the reading ledger records one. Confidence concerns the preferred reading, with **low** used for unresolved overwriting and cancelled ink.\n\n'
out+='| Cote | Scan | Approximate line / position | Reading | Alternatives | Confidence |\n|---|---:|---|---|---|---|\n'
count=0
for p in sorted((b/'pages').glob('*.tex')):
    n=int(p.stem[-3:]); s=p.read_text()
    cancelled=[(a,z) for a,z,_ in arguments(s,'deleted')]
    for a,z,arg in arguments(s,'unsure'):
        first,alt=split_reading(arg)
        confidence='low' if any(x<=a<y for x,y in cancelled) else 'medium'
        pos=f'TeX line {s[:a].count(chr(10))+1}'
        matches=[d for d in ledger if int(d['scan'])==n and d['reading'].strip() in (first.strip(),arg.strip())]
        if matches:
            d=matches[-1];confidence=d['confidence'];pos=d['position']+'; '+pos
        out+='| '+' | '.join(cell(v) for v in [18,n,pos,'`'+first+'`','`'+alt+'`' if alt else '',confidence])+' |\n'
        count+=1
out+=f'\n**Indexed doubtful occurrences: {count}.** No `\\illegible` placeholder is used; each difficult passage has an attempted reading in place. The complete working reading ledger and audit notes are retained under `records/`; earlier readings there are revision history, while this table indexes the final fragment.\n'
out+='\n# Abbreviations\n\n'+(b/'records/abbreviations.md').read_text()
out+='\n# Legibility and trust\n\n'
out+='The reused typescripts are generally clear, though faint underlines, typewriter subscripts and unfinished references require care. The autograph pages are much less uniform: fast connecting strokes often suppress word endings, and overwriting can make a Greek letter or a short condition indecisive.\n\n'
out+='The least secure passages are the compressed comparison labels on scans 019–025; the word and alphabet choices on 029 and 033–036; the large inserted paragraph on 039; the first-line condition and cancelled foot on 045; phi/xi choices on 047; cancelled prose on 053 and 055; the erased exponents on 057; and the short prose and altered formulas on 059–062. In particular, the opening of 053 and the opening and margin of 062 remain low-confidence readings, not completed sentences supplied by an editor.\n\n'
out+='All 45 whole pages and their supplied halves were inspected personally during the sequential first reading, and all 45 were subsequently read again against the transcription. Enlargements and rotations were used for small writing; OCR and transcription subagents were not used. The drawings reproduce visible relative geometry in TikZ, with less assurance about minute pen-stroke shape than about the counted segments and written labels. The transcription was frozen before the contextual material was opened; any later context-based reading question belongs in the research notes.\n'
(b/'MPL_18_018-062_doubts.md').write_text(out)
print('Indexed',count,'doubtful occurrences')
