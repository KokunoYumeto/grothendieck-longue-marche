from pathlib import Path
import subprocess, json, datetime

BASE = Path(__file__).resolve().parents[2]
ROOT = Path(__file__).resolve().parents[1]
queries = {
    'I01': r'S19|T01|T04|N41|dualisant|monodrom',
    'I02': r'résolution|Künneth|N15|N20|N21|N41|S19',
    'I03': r'Verdier|Illusie|N41|S19|chronolog|dat',
    'I04': r'N35|N37|isomorph|compatib|S19',
    'I05': r'LM7 E\.23|LM7_PUSH C\.6|INTAKE LM7|section|centrale|métabél|metabel',
    'I06': r'LM4 D\.12|GT_0|torsion|inertie|racines',
    'I07': r'LM4 F\.7|centralizer|centralisateur|complét|completion|hens',
    'I08': r'WG H9|Mordell|Hodge|Lefschetz|pinceau',
    'I09': r'WG2|MPL_14_002-044|projecteur|endomorph|intégraux|Lefschetz',
    'I10': r'MPL_91_099-143|Néron|Neron|Greenberg|Tate',
}
rows = []
for note, query in queries.items():
    result = subprocess.run(['rg','-n','-i',query,str(BASE/'context')], capture_output=True, text=True)
    if result.returncode not in (0,1):
        raise RuntimeError(result.stderr)
    hits = []
    for line in result.stdout.splitlines():
        path, number, excerpt = line.split(':',2)
        hits.append({'file':str(Path(path).relative_to(BASE/'context')), 'line':int(number), 'excerpt':excerpt[:360]})
    rows.append({'note':note, 'query':query, 'hits':hits})
out = {'searched_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(), 'context':'all four supplied context Markdown files', 'records':rows}
(ROOT/'records/integration_context_search.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print({r['note']:len(r['hits']) for r in rows})

