#!/usr/bin/env python3
"""Record per-item searches of the supplied research context; never edit TeX."""
from pathlib import Path
import json
import subprocess

ROOT = Path(__file__).resolve().parents[1]
CONTEXT = ROOT.parent / 'context'
QUERIES = {
'C01': r'affine|noeth|lissité|simple|N070',
'C02': r'étale|formel|lissité|nilpotent',
'C03': r'section|séparé|connexe|relèvement',
'C04': r'maximum|uniform|composantes connexes|noeth',
'C05': r'dimension|D\x27|nD|rang',
'C06': r'dimension|deux points|composantes|D\x27',
'C07': r'g_1|g_2|étale|dimension',
'C08': r'lambda|exactement|sections|degré|fini',
'C09': r'91-weil-restriction-finite-etale-criterion|localement constante|homogène|Corollaire 3',
'C10': r'91-weil-restriction-finite-etale-criterion|deux copies|amalg|coprod|nu\(s\)',
'C11': r'homogène|composition|extension de la base|base change',
'C12': r'D\.11|mu2|mu_2|μ₂|homogène|fibre',
'C13': r'principal|torseur|surject|N91-13|N91-14',
'C14': r'nilpotent|dimension|lambda|Greenberg|épais',
'C15': r'groupe fini|groupe|torseur|A\.185|restriction',
'C16': r'exact|Hom.*Ens|foncteur|A\(T\)|petit raisonnement',
'C17': r'base|géométrique|connexe|pi_1|fondamental',
'C18': r'exact à gauche|left.exact|Hom.*pi|91-weil-restriction-finite-etale-criterion',
'C19': r'compatibilité|bifoncteur|adjoint|Hom|Rev',
'C20': r'localement constante|composantes connexes|pi_0|f_.*ét|f_.*mathrm',
'C21': r'page 58|pages 54|surject|connex|prend.*section',
'C22': r'plutôt|résumé|notion|principal homogène|lecture mince',
'C23': r'A\.185|Weil|isogen|norme|Prym',
'C24': r'Greenberg|Néron|S19|Book I|résidu|dualité|intersection',
'C25': r'dimension|local|connexe|D\x27|section',
'C26': r'Hom|sections|hensél|connexe|compatibilité',
'P01': r'91-hom-unramified-rigidification|91-res-representable-by-scheme|91-weil-restriction-finite-etale-criterion',
'P02': r'E\.23|B9|D\.11|D\.12|F\.7|Open',
'P03': r'couverture|titre|pages|plan|N°|Greenberg|Néron',
}

records = []
for item, query in QUERIES.items():
    proc = subprocess.run(['rg','-n','-i','--glob','*.md','--glob','*.tex',query,str(CONTEXT)], text=True, capture_output=True)
    if proc.returncode not in (0,1):
        raise RuntimeError(proc.stderr)
    matches = proc.stdout.replace(str(CONTEXT) + '/', '')
    records.append({'id':item,'query':query,'scope':'All supplied .md and .tex files in the extracted context','matches':matches.splitlines()})

out = ROOT / 'research' / 'root_context_searches.jsonl'
out.write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in records),encoding='utf-8')
md = ['# Per-item supplied-context searches: C01–C26 and synthesis P01–P03', '',
      'Executed after the recorded transcription freeze and context opening. Search matches are leads; the final notes cite the passages actually read and compared. Broad words deliberately catch cross-project homonyms, which are not treated as mathematical identifications.', '']
for r in records:
    md.extend([f"## {r['id']}",'',f"Query: `{r['query']}`",'',f"Scope: {r['scope']}",'',f"Matches: {len(r['matches'])}",'','```text',*r['matches'],'```',''])
(ROOT/'research'/'root_context_searches.md').write_text('\n'.join(md),encoding='utf-8')
print(f'Recorded {len(records)} searches; no transcription files read or changed.')
