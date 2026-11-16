#!/usr/bin/env python3
"""Assemble post-freeze research only; never writes transcription files."""
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
REC=ROOT/'records'

def sections(filename):
    s=(REC/filename).read_text()
    out={}
    for m in re.finditer(r'^## ((?:P|O|A|E)\d\d)\b[^\n]*\n',s,re.M):
        nxt=re.search(r'^## ',s[m.end():],re.M)
        end=m.end()+nxt.start() if nxt else len(s)
        out[m.group(1)]=s[m.start():end].strip()
    return out

def add(title,items):
    parts.append('## '+title+'\n\n'+'\n\n'.join(re.sub(r'^## ', '### ',x,flags=re.M) for x in items))

parts=[(REC/'research_intro.md').read_text().strip()]
p=sections('research_plans.md')
add('Treatise plans, later chapters and the questions actually listed',[p[x] for x in ['P01','P02','P03','P04','P05','P09']])
for title,fn,prefix,count in [
 ('Jouanolou offprints and reused trace/norm typescripts','research_offprints.md','O',17),
 ('Cohen constructions, formal simplicity and differential kernels','research_algebra.md','A',30),
 ('Projective differential calculations, discriminants and exponentials','research_exponentials.md','E',23)]:
    d=sections(fn)
    add(title,[d[f'{prefix}{i:02}'] for i in range(1,count+1)])
flags=(REC/'research_self_flags_summary.md').read_text().strip()
flags=re.sub(r'^# [^\n]+\n','',flags,count=1).strip()
parts.append('## Steps the sources themselves mark as unverified\n\n'+flags)
add('Title sheets, page counts, pagination and dates',[p[x] for x in ['P06','P07','P08']])
parts.append((REC/'research_sources.md').read_text().strip())
parts.append('## Supporting records\n\nThe per-note context searches are in `records/research_plans_searches.txt`, `research_offprints_searches.txt`, `research_algebra_searches.txt` and `research_root_searches.txt`. Detailed algebra verifications are in `records/research_power_series_review.md` and `records/research_calculation_review.md`; the inventory and exponential-note review is in `records/research_final_review.md`. The separate doubts file contains the shared notation table, abbreviation expansions and legibility assessment. `progress.log`, `records/frozen_hashes.json` and the validation reports document the transcription sequence, freeze and final integrity checks.')
out=ROOT/'MPL_22+23_002-016_notes.md'
out.write_text('\n\n'.join(parts)+'\n')
print(f'{out.name}: {len(out.read_text().split())} whitespace-separated words; {out.stat().st_size} bytes')
