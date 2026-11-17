"""Actual note-by-note searches of supplied context; no scans are read."""
from pathlib import Path
import hashlib
import json
import re
from datetime import datetime, timezone

base = Path(__file__).resolve().parents[2]
context = base / 'context'
queries = {
 'NH01': r'Legendre|chif|factoriel|valuation|page 34|page 42',
 'NH02': r'Homomorphismes homogènes|adjonction|adjoint|nonnegative unit|nonnegative degrees',
 'NH03': r'Cayley|tête-bêche|tubulure|MPL_121_001-048',
 'NH04': r'c_\{d,j\}|beta -.*alpha|beta.*alpha|weighted rigidity|threshold',
 'NH05': r'beta-d-1|beta - d - 1|dernière équation|endpoint',
 'NH06': r'characteristic.two|characteristic 2|F_2|mathbb\{F\}_2|endpoint|dernière équation',
 'NH07': r'degré négatif|negative.degree|p\^s - d|Homomorphismes homogènes|p\. 298',
 'NH08': r'base.*p|chiffre|digit|p.typ|tau_\{p\^r\}',
 'NH09': r'syzyg|cross.generator|les relations|relations.*T_s|T_s\^\{p-1\}',
 'NH10': r'divisible|divisib|divisions successives|coherent|Ulm',
 'NH11': r'bigcap.*nN|largest divisible|grand sous.module.*divisible|Ulm|p.primary',
 'NH12': r'divisible|mathbb\{Z\}_\{\(p\)\}|localis|localiz|global',
 'NH13': r'indépendant|independence|adjonction|nonnegative unit|Homomorphismes homogènes',
 'NH14': r'k.*torsion|anneau.*torsion|ring.*torsion|divisible|bounded.exponent',
 'NH15': r'deux membres|identiques|N_\{0|Homomorphismes homogènes',
}
files = sorted(p for p in context.rglob('*') if p.is_file() and p.suffix in {'.md','.tex'})
report = {'created_utc':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
 'scope':'All supplied textual context files only; no scans; no external files mentioned by these sources opened.',
 'source_files':{str(p.relative_to(context)):{'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'lines':len(p.read_text().splitlines())} for p in files},
 'notes':{}}
for ident, pattern in queries.items():
    compiled = re.compile(pattern, re.I)
    found = {}
    for p in files:
        hits = [{'line':n,'text':line[:260]} for n,line in enumerate(p.read_text().splitlines(),1) if compiled.search(line)]
        found[str(p.relative_to(context))]={'count':len(hits),'hits':hits}
    report['notes'][ident]={'pattern':pattern,'files':found}
(Path(__file__).parent/'negative_hom_searches.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(f"Recorded {len(queries)} note searches across {len(files)} supplied context texts.")
