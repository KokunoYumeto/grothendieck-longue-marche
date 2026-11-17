"""Record post-freeze supplied-context searches for each documentary note."""
from pathlib import Path
import subprocess, json, hashlib
from datetime import datetime, timezone

root = Path(__file__).resolve().parents[1]
context = root.parent/'context'
assert 'context opened' in (root/'progress.log').read_text()
queries = {
 'D001': r'Historique|Plan.*conf|conférence.*1976|pages.*375',
 'D002': r'H05|ombres des modules|ombres virtuelles|foncteurs.*ombres',
 'D003': r'tubulure|Q1-06|q.ième ombre|Les ombres|N21|N22',
 'D004': r'Chern|Fourier|abéloïde|abelo.d|R057|N16',
 'D005': r'13\.4|tore|torus|Lie|R057',
 'D006': r'abéloïde|abelo.d|13\.4|R09',
 'D007': r'DELIGNE|Néron|R35|reference numbers|bibliograph',
 'D008': r'Hodge|13\.4\.6|filtration|175|174',
 'D009': r'base.change|changements de base|13\.4|R036|R041',
 'D010': r'1975|1976|feuillets|reused|tapuscrit',
 'D011': r'topos de De Rham|condition de De Rham|faisceaut|GALOIS G\.6|BISITE D\.12',
 'D012': r'tapuscrit|reused|N61|R055|IX',
 'D013': r'pagin|feuillets|H05|page n',
}
records = []
for note, pattern in queries.items():
    result = subprocess.run(['rg','-n','-i','--json',pattern,str(context)],capture_output=True,text=True)
    assert result.returncode in (0,1), result.stderr
    hits=[]
    for line in result.stdout.splitlines():
        item=json.loads(line)
        if item['type']!='match': continue
        d=item['data']; path=Path(d['path']['text'])
        hits.append({'file':str(path.relative_to(context)), 'line':d['line_number'],
                     'excerpt':d['lines']['text'].strip()[:500]})
    records.append({'note':note,'pattern':pattern,'match_lines':len(hits),
                    'displayed_hits':hits[:40], 'truncated':len(hits)>40})
frozen = root/'MPL_136_002-046_transcription.tex'
text=frozen.read_text()
negative_terms={term:term.casefold() in text.casefold() for term in ['tubulure','Chern','Fourier']}
report={'time_utc':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
        'scope':'Supplied context only; hits are leads, selected passages checked before citation. No Library search or external bibliography retrieval.',
        'source_sha256':{str(p.relative_to(context)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(context.rglob('*')) if p.is_file()},
        'notes':records, 'literal_frozen_transcription_term_presence':negative_terms}
out=root/'research/documentary_context_searches.json'
out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(f'{len(records)} per-note searches recorded; frozen term results: {negative_terms}')
