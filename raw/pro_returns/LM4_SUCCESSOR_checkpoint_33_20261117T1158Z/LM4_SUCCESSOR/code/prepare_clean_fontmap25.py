"""Comment nine stray font-family headings in an isolated derived map."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

root = Path(__file__).resolve().parents[1]
runtime = root.parent/'tex_runtime'
source = runtime/'maps/pdftex.map'
original = source.read_bytes()
headings = {'Bookman','Courier','Helvetica','New Century Schoolbook',
            'Palatino','Symbol','Times','Zapf','Helvetica-Narrow'}
lines = original.decode().splitlines(keepends=True)
changed = []
for i,line in enumerate(lines):
    if line.strip() in headings:
        changed.append({'line':i+1,'original':line.rstrip('\n')})
        lines[i] = '% Retained non-map heading:'+line
assert len(changed)==9
target = root/'tex_cache/clean_fontmaps/pdftex.map'
target.parent.mkdir(parents=True,exist_ok=True)
target.write_text(''.join(lines))
environment = json.loads((runtime/'env.json').read_text())
environment['TEXFONTMAPS'] = str(target.parent)+'//:'+environment['TEXFONTMAPS']
(root/'records/checkpoint25_tex_env.json').write_text(json.dumps(environment,indent=2)+'\n')
logs = [root/'LM4_SUCCESSOR_paper.log']
logs += sorted((root/'checkpoint_history').rglob('LM4_SUCCESSOR_paper.log'))
logs += sorted((root/'records/pdf_qa').glob('checkpoint*_before_integration/LM4_SUCCESSOR_paper.log'))
audits = []
for path in logs:
    s = path.read_text(errors='replace')
    engine = re.findall(r'^warning\s+\(file .*$',s,re.M|re.I)
    audits.append({'path':str(path.relative_to(root)),
                   'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
                   'engine_fontmap_warning_count':len(engine),
                   'previous_case_sensitive_warning_count':len(re.findall(r'^.*Warning.*$',s,re.M))})
record = {'recorded_at':datetime.now(timezone.utc).isoformat(),
 'source':str(source),'source_sha256':hashlib.sha256(original).hexdigest(),
 'derived_map':str(target),'derived_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),
 'original_runtime_changed':False,'commented_headings':changed,
 'prior_log_audit':audits,
 'correction':'Earlier Warning-only counts missed lowercase engine font-map warnings. Confirmed logs and exact counts are listed; the archived logs/PDFs remain unchanged. This correction does not change the separately checked overfull counts. The derived map comments only the nine malformed family headings, retaining every font mapping.'}
(root/'records/checkpoint25_fontmap_warning_audit.json').write_text(json.dumps(record,indent=2)+'\n')
print('Prepared isolated clean map; nine malformed headings retained as comments.')
print('Audited',len(audits),'available prior final-log paths; original runtime unchanged.')
