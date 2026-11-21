from pathlib import Path
import json,hashlib,sys,subprocess

ROOT=Path(__file__).resolve().parent
utc=sys.argv[1]
report=json.loads(ROOT.joinpath('report.json').read_text())
report['end_utc']=utc
report['provenance']['source_only_checks']='Completed: source_checks.json. Braces, environments, display delimiters, source spans, literal witness anchors, references and permitted kind values pass; no blank physical lines inside display math. No compile/render or mathematical check.'
report['provenance']['submission_state']='Frozen after final source-only verification; reader will not modify submitted files after final return.'
report['provenance']['source_syntax_repairs']=['The invisible defining-label annotation uses text for accented déf; its visible def body and raised point remain unchanged.','The raised crossed et has an invisible inserted/deleted state annotation at its own native placement; no second visible et or added visible strike was introduced.']
ROOT.joinpath('report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
with ROOT.joinpath('reading.md').open('a') as out:
    out.write('\n## Final source verification\n\n')
    out.write('Completed and frozen at **'+utc+'**. Braces, environment nesting, display delimiters, absence of blank lines in displays, all 55 exact source excerpts, literal witness excerpts and file/group references pass the source-only audit. No compilation or rendering was performed. The 39 Sigma occurrences and eight ring loci remain individually mapped.\n')
with ROOT.joinpath('progress.log').open('a') as out:
    out.write(utc+' — reader C complete; complete reading, report, inventory, exact source map and audits written. Source-only verification passed. No mathematical check performed.\n')
    out.write(utc+' — submitted files frozen; no later reader modification authorized by this return.\n')
subprocess.run([sys.executable,str(ROOT/'verify_source.py')],check=True)
checks=json.loads(ROOT.joinpath('source_checks.json').read_text())
if not checks['passed']:raise SystemExit('Source audit did not pass; freeze stopped.')
files=[]
for path in sorted(ROOT.rglob('*')):
    if not path.is_file() or path.name in ['frozen_manifest.json','SHA256SUMS']:continue
    data=path.read_bytes()
    files.append({'path':str(path.relative_to(ROOT)),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
manifest={'scan':26,'reader':'C','start_utc':report['start_utc'],'frozen_utc':utc,'files':files,'self_hash_policy':'This manifest excludes itself and SHA256SUMS. SHA256SUMS additionally includes this manifest. The final chat supplies SHA256SUMS hash.','view_counts':report['provenance']['view_counts'],'source_checks_passed':checks['passed'],'submitted_files_frozen':True}
ROOT.joinpath('frozen_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
lines=[]
for path in sorted(ROOT.rglob('*')):
    if not path.is_file() or path.name=='SHA256SUMS':continue
    lines.append(hashlib.sha256(path.read_bytes()).hexdigest()+'  '+str(path.relative_to(ROOT)))
ROOT.joinpath('SHA256SUMS').write_text('\n'.join(lines)+'\n')
print('Frozen artifact files:',len(lines),'plus SHA256SUMS')
for name in ['reading.tex','reading.md','report.json','source_map.json','image_audit.json','crop_audit.json','source_checks.json','frozen_manifest.json','SHA256SUMS']:
    print(hashlib.sha256(ROOT.joinpath(name).read_bytes()).hexdigest(),name)
