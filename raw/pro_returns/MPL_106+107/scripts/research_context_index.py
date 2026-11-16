"""Research-only context searches. Never reads scan images or writes transcription."""
from pathlib import Path
import json, re, subprocess

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'MPL_106+107' / 'records'
queries = {
    'CF-AXIOMS': r'Brown|Baues|weak lifting|C1.{0,12}C3|cofibration categor',
    'CF-REPLACEMENT': r'catégories de fractions|catégories de fibrants|cofibrant|quasi-inverse|replacement',
    'CF-CANCELLATION': r'fidélité|fidèle|faithful|indépendance|independence|sections',
    'CF-COMPOSITION': r'composition des chemins|associativ|pi_0|pi0|Ch_.*Sigma',
    'CF-COUNIVERSAL': r'counivers|cof_W|cof.*W|W_0|W_\{0\}',
    'CF-SECTION': r'section|rétraction|retraction|factorisation|factorization',
    'HOM-RELATIVE': r'Hom.*_A|Hom.*_B|Hom.*!!|Hom.*!|produit extérieur|external product',
    'HOM-CONTINUITY': r'4\.2\.3|Pas prouvé|peut-être faux|également faux|separately|séparément',
    'HOM-TENSOR': r'tensor|cotensor|boxtimes|X\^M|X\^\{M\}',
    'HOT-LIMIT': r'limites filtrantes|filtering direct limits|filtered colimit|sequential|lim.*pi_0|lim.*pi0',
    'HOT-RECTIFY': r'Quillen|homotopies compatibles|compatible homotop|rectif|homotopy lifting',
    'HISTORICAL': r'1983|13\.10|W\(7|W ?7|totalement.*filtr|asph.*filtr',
    'PRINTED': r'PREDONTA|DOCUGRA2|PLOTEDIT|GRAPHI2|06/04/82|08/25/82',
}

report = {}
for name, pattern in queries.items():
    proc = subprocess.run(['rg', '-n', '-i', '--glob', '*.tex', '--glob', '*.md', pattern, str(ROOT/'context')], text=True, capture_output=True)
    if proc.returncode not in (0,1):
        raise RuntimeError(proc.stderr)
    lines = proc.stdout.splitlines()
    matches = []
    for row in lines:
        path, num, text = row.split(':',2)
        p = Path(path)
        content = p.read_text().splitlines()
        prior = '\n'.join(content[:int(num)])
        ms = re.findall(r'\\msp\{([^}]+)', prior)
        ps = re.findall(r'\\pspage\{([^}]+)', prior)
        sec = re.findall(r'\\label\{sec:([^}]+)', prior)
        # The exact line and page marker are evidence locators, not an assertion
        # that the matched line belongs to the manuscript rather than commentary.
        matches.append({'file':str(p.relative_to(ROOT)), 'line':int(num), 'nearest_ms_page':ms[-1] if ms else None, 'nearest_ps_page':ps[-1] if ps else None, 'nearest_ps_section':sec[-1] if sec else None, 'text':text})
    # Retain a bounded locator sample, rather than duplicating the supplied
    # sources inside the deliverable. Notes give the specifically read locators.
    locators = [{k:v for k,v in m.items() if k != 'text'} for m in matches[:80]]
    report[name] = {'query':pattern, 'locator_sample':locators, 'count':len(matches), 'sample_limit':80}

(OUT/'context_search_root.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
md=['# Research context searches — root', '', 'These searches were run only after the transcription was frozen. Hits include both manuscript-text layers and commentary; the notes identify which layer is used. A keyword hit alone does not establish a mathematical match.', '']
for name,r in report.items():
    md += [f'## {name}', '', f'Query: `{r["query"]}`. Matches: {r["count"]}. A bounded sample of up to 80 file/line/page locators is in `context_search_root.json`; source text is deliberately not duplicated. The research notes separately name the passages actually read and used.', '']
(OUT/'context_search_root.md').write_text('\n'.join(md)+'\n')
print(json.dumps({k:v['count'] for k,v in report.items()},ensure_ascii=False))
