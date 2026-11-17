from pathlib import Path
import json
import subprocess

ROOT = Path('/workspace/scratch/ac2bec4f7edd')
CONTEXT = ROOT / 'context'
OUT = ROOT / 'MPL_57_226-270' / 'records'
queries = {
    'SC01': r'57-analytic-pic|finite length|longueur finie|analytic iff',
    'SC02': r'hens[eé]l|bon anneau|good.*ring',
    'SC03': r'hens[eé]l|[eé]tale|r[eé]sidu|Mumford',
    'SC04': r'isol[eé]|singular|r[eé]gular|r[eé]gulier',
    'SC05': r'Mumford|blue paper|p\.16',
    'SC06': r'p-divis|sp[eé]cialis|Mittag|MLAR|characteristic',
    'SC07': r'N[eé]ron|torsion|Picard-tau|pi_0|component',
    'SC08': r'repr[eé]sentab|principal homog|descent|unipotent|E\.23|E\.21',
    'SC09': r'rigoureux|expliciter|Čech|descent|repr[eé]sentab',
    'SC10': r'univers|ample|projectif|projectivity',
    'SC11': r'projectif|factoriel|[eé]clat|pushout',
    'SC12': r'Gaga|GAGA|N[eé]ron|formal|hens[eé]l',
    'SC13': r'unit[eé]|pinching|B11|g[eé]n[eé]ralis[eé]',
    'SC14': r'fondamental|pi_1|centralizer|Tate|E\.23|E\.21',
    'SC15': r'g[eé]n[eé]ralis[eé]|non compl[eè]tes|E\.23|E\.21|H1',
    'SC16': r'limite|varprojlim|filtrant|Mittag|finite generation',
    'SC17': r'Murre|Oort|repr[eé]sentab|existence',
    'SC18': r'227|Syst[eè]mes lin[eé]aires|diviseur|printed page',
    'SC19': r'1962|1957|1964|Octobre|24\.6|Aiguines|Hironaka',
    'SC20': r'271.315|the end|folio|scan minus one|page count',
    'SC21': r'Oort|Oda|Igusa|non.?reduced|characteristic p',
}

files = sorted(str(p) for p in CONTEXT.rglob('*') if p.suffix in ('.md', '.tex'))
records = []
for ident, pattern in queries.items():
    cmd = ['rg', '-n', '--no-heading', '-i', '-e', pattern, *files]
    result = subprocess.run(cmd, text=True, capture_output=True, check=False)
    if result.returncode not in (0, 1):
        raise RuntimeError(f'{ident}: {result.stderr}')
    hits = result.stdout.splitlines()
    excerpts = []
    for hit in hits:
        parts = hit.split(':', 2)
        if len(parts) == 3:
            body = parts[2]
            hit = ':'.join(parts[:2]) + ':' + body[:220] + ('…' if len(body) > 220 else '')
        excerpts.append(hit)
    records.append({'id': ident, 'pattern': pattern, 'files_searched': len(files), 'matches': len(hits), 'hits': excerpts})

(OUT / 'context_samecote_searches.json').write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n')
lines = ['# Item-level context searches for context_samecote.md', '', 'All searches use rg -n --no-heading -i over the eight supplied .md/.tex contextual files; no scans, OCR or unsupplied files. Every match locator and a short excerpt is preserved in context_samecote_searches.json. Excerpts below show relevant same-cote hits when available, plus RS where helpful.', '']
for rec in records:
    lines += [f"## {rec['id']}", '', f"Pattern: `{rec['pattern']}`. Matches: {rec['matches']} across {rec['files_searched']} files.", '']
    preferred = [h for h in rec['hits'] if 'same_cote_57' in h]
    others = [h for h in rec['hits'] if 'RESULTS_STATE' in h]
    shown = preferred[:4] + others[:2]
    if not shown:
        shown = rec['hits'][:6]
    for hit in shown:
        relative = hit.replace(str(ROOT) + '/', '')
        lines.append('- ' + relative)
    lines.append('')
(OUT / 'context_samecote_searches.md').write_text('\n'.join(lines) + '\n')
print(json.dumps([{'id': r['id'], 'matches': r['matches'], 'files': r['files_searched']} for r in records]))
