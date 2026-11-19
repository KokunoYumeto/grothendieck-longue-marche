from pathlib import Path
import subprocess,json,sys,datetime,hashlib
OUT=Path(__file__).resolve().parents[1]
local=Path(sys.argv[1]).resolve()
helper=OUT/'scripts/library_helpers/library_upload.py'
payload={'uploads':[{'local_path':str(local),'purpose':'create_library_file','library_artifact_type':'other'}]}
r=subprocess.run([sys.executable,str(helper)],input=json.dumps(payload),text=True,capture_output=True)
# The helper owns preparation, PUT, finalization and xattrs. Preserve its safe report.
try: result=json.loads(r.stdout)
except Exception:
 print(json.dumps({'exit_code':r.returncode,'stdout':r.stdout[:3000],'stderr':r.stderr[:3000]}));sys.exit(r.returncode or 1)
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
record={'name':local.name,'utc':now,'bytes':local.stat().st_size,'sha256':hashlib.sha256(local.read_bytes()).hexdigest(),'exit_code':r.returncode,'result':result}
registry=OUT/'upload_records';registry.mkdir(exist_ok=True)
(registry/(local.stem+'.json')).write_text(json.dumps(record,ensure_ascii=False,indent=2))
print(json.dumps(record,ensure_ascii=False))
sys.exit(r.returncode)
