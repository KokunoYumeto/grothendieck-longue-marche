#!/usr/bin/env python3
"""Native-text research searches only; never opens manuscript scan images."""
from pathlib import Path
import json, re, hashlib
ROOT=Path(__file__).resolve().parents[1]
WORK=ROOT.parent
REC=ROOT/'records'
ODA=WORK/'research_tmp/oda1969.txt'
CON=WORK/'context_sources'
def lines_for(path):
    page=1
    cote=scan=None
    result=[]
    for i,line in enumerate(path.read_text(encoding='utf-8').split('\n'),1):
        page+=line.count('\f')
        m=re.search(r'\\cotefile\{(\d+)\}',line)
        if m:cote=int(m.group(1))
        m=re.search(r'\\scanpage\{(\d+)\}',line)
        if m:scan=int(m.group(1))
        entry={'line':i,'text':line.replace('\f','').strip()}
        if path==ODA:entry.update(pdf_page=page,printed_page=page+61 if page>1 else None)
        elif cote is not None:entry.update(cote=cote,scan=scan)
        result.append(entry)
    return result
paths=sorted(p for p in CON.rglob('*') if p.is_file() and p.suffix in ('.md','.tex'))+[ODA]
indexed={str(p.relative_to(WORK)):lines_for(p) for p in paths}
hashes={str(p.relative_to(WORK)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
def query(note,pattern,selected):
    regex=re.compile(pattern,re.I)
    out={'note_id':note,'pattern':pattern,'files':[]}
    for f in selected:
        hits=[x for x in indexed[f] if regex.search(x['text'])]
        out['files'].append({'file':f,'total_matching_lines':len(hits),'shown_hits':hits[:12]})
    return out
root_queries=json.loads((REC/'root_note_queries.json').read_text())
root_queries += [
 {'id':'R37','pattern':r'Nori|Andr|M23|M28a|semi.simple|motivat'},
 {'id':'R38','pattern':r'cyclotom|\\chi|ker|noyau|caractère|caractere|extension'},
 {'id':'STANDING_FLAGS','pattern':r'vérifier|revoir|conj|question|doute|à prouver|à démontrer|A-t-on|Peut-on|problème|on aimerait|il faudrait|faux|fausse'}]
oda_key=str(ODA.relative_to(WORK))
report={'source_file':'Oda_1969_first_de_Rham_cohomology_Dieudonne_modules.pdf',
 'method':'Search of pre-existing embedded PDF text extraction; no OCR. PDF page1 is wrapper; printed page=PDF page+61 thereafter.',
 'source_text_sha256':hashes[oda_key],
 'queries':[query(x['id'],x['pattern'],[oda_key]) for x in root_queries]}
(REC/'research_root_oda_searches.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
lef=[
 ('RL01',r'Lefschet|correspond|project|motif|motivic'),
 ('RL02',r'Lefschet|sl_?2|sl₂|M04|Tate|graduat'),
 ('RL03',r'graduat|grading|cochar|B04|poids|centr|Tate'),
 ('RL04',r'factor|factoriel|binom|divided|S28|intégr|integr|puissance'),
 ('RL05',r'conject|standard|standart|C_\\ell|D_\\ell|A_\\ell|B_\\ell'),
 ('RL06',r'singul|hypersurf'),
 ('RL07',r'semi.simple|semisimp|numer|numér|homolog|M09|S15'),
 ('RL08',r'ab[eé]lien|abelian|Lefschet|Fourier|M24a|M10|B16')]
report={'method':'Per-note terms searched through all five supplied text files and the embedded text of the supplied Oda PDF.',
 'source_sha256':hashes,'queries':[query(n,p,list(indexed)) for n,p in lef]}
(REC/'research_lefschetz_context_searches.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'root_and_standing_oda_queries':len(root_queries),'lefschetz_queries':len(lef),'files_per_lefschetz_query':len(indexed)}))
