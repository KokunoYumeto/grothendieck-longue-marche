"""Validate the final deliverables and create one complete final ZIP."""
from pathlib import Path
import json
from validate_package import Validator

root=Path(__file__).resolve().parents[1]
destination=root.parent/'MPL_43_094-142.zip'
validator=Validator(root,'final')
report=validator.validate()
(root/'records/final_validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2,sort_keys=True)+'\n',encoding='utf-8')
if not report['ok']:
    print(json.dumps(report,ensure_ascii=False,indent=2))
    raise SystemExit(1)
validator.package(destination)
print(json.dumps({'ok':report['ok'],'errors':report['errors'],'warnings':report['warnings'],'zip':report.get('zip')},ensure_ascii=False,indent=2))
raise SystemExit(0 if report['ok'] else 1)
