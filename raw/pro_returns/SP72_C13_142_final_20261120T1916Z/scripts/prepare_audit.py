from pathlib import Path
import json,sys,shutil,csv,re

out=Path(__file__).resolve().parents[1]
root=out.parent
assert len(list((out/'documentation/decided').glob('scan*.json')))==24, 'Complete all first readings before audits.'
n=int(sys.argv[1]);auditor=sys.argv[2]
report=json.loads((out/'documentation/decided'/f'scan{n:03}.json').read_text())
with (out/'documentation/assignments.tsv').open() as f:
    assignments={int(r['scan']):r for r in csv.DictReader(f,delimiter='\t')}
first_reader=assignments[n]['first_reader']
auditor=re.search(r'reader_[abc]',auditor)[0]
assert first_reader!=auditor, 'Auditor must differ from first reader.'
dest=root/'audit_packets'/f'scan{n:03}'
dest.mkdir(parents=True,exist_ok=True)
for filename in ['source.json','C.tex','H.tex','marks.json']:
    shutil.copyfile(root/'packets'/f'scan{n:03}'/filename,dest/filename)
shutil.copyfile(out/'pages'/f'142_scan{n:03}.tex',dest/'consolidated.tex')
shutil.copyfile(out/'notation.md',dest/'notation.md')
(dest/'apparatus.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
manifest=[json.loads(s) for s in (out/'crops/crop_manifest.jsonl').read_text().splitlines()]
(dest/'existing_crops.json').write_text(json.dumps([m for m in manifest if m['scan']==n],ensure_ascii=False,indent=2)+'\n')
(dest/'assignment.json').write_text(json.dumps({'scan':n,'auditor':auditor,'first_reader':first_reader,'halves_directory':str(root/'packets'/f'scan{n:03}')},indent=2)+'\n')
print(dest)
