"""Record the precise additional A.121 page-review requirements."""
from pathlib import Path
import datetime,difflib,hashlib,json
root=Path(__file__).resolve().parents[1]
rows=[]
for name in ('render_checkpoint37_pdf.py','finalize_checkpoint37_visual_record.py'):
    old=root/'records/checkpoint37_before_A121_correction/code'/name
    new=root/'code'/name
    diff=''.join(difflib.unified_diff(old.read_text().splitlines(True),new.read_text().splitlines(True),fromfile=str(old.relative_to(root)),tofile=str(new.relative_to(root))))
    out=root/'records'/('checkpoint37_A121_QA_'+name+'.diff')
    with out.open('x') as stream:stream.write(diff)
    rows.append({'source':str(new.relative_to(root)),'bytes':new.stat().st_size,
                 'sha256':hashlib.sha256(new.read_bytes()).hexdigest(),
                 'diff':str(out.relative_to(root)), 'diff_sha256':hashlib.sha256(out.read_bytes()).hexdigest()})
record={'recorded_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'scope':'Require individual review of the entire actual A.121 correction interval in addition to every new37 mathematical page. No render or approval is performed.',
        'sources':rows}
with (root/'records/checkpoint37_A121_QA_source_changes.json').open('x') as stream:
    json.dump(record,stream,indent=2);stream.write('\n')
print(json.dumps(record,indent=2))
