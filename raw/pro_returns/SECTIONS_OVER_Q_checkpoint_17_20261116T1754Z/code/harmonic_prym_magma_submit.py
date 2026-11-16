"""Submit a retained, public mathematical input to the official Magma API.

The endpoint is literally advertised by https://magma-maths.org/calc/.
The exact API request and complete response are retained alongside the input.
No local/environment data is sent apart from the specified .m input.
"""
from pathlib import Path
import datetime
import json
import urllib.request
import urllib.error
import sys

base = Path(__file__).resolve().parent
input_path = Path(sys.argv[1]).resolve() if len(sys.argv)>1 else base/'harmonic_prym_rank_magma.m'
stem = input_path.with_suffix('')
payload = {'code': input_path.read_text()}
endpoint = 'https://calculator.magma-maths.org/execute'
request_record = {'endpoint': endpoint,
                  'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
                  'payload': payload}
stem.with_name(stem.name+'_request.json').write_text(json.dumps(request_record,indent=2)+'\n')
req = urllib.request.Request(endpoint, data=json.dumps(payload).encode(),
                             headers={'Content-Type':'application/json'}, method='POST')
try:
    with urllib.request.urlopen(req, timeout=330) as response:
        raw = response.read().decode()
except urllib.error.HTTPError as error:
    raw = error.read().decode()
    stem.with_name(stem.name+'_response.txt').write_text(raw)
    print('HTTP ERROR', error.code)
    print(raw)
    raise SystemExit(1)
try:
    result = json.loads(raw)
except json.JSONDecodeError:
    stem.with_name(stem.name+'_response.txt').write_text(raw)
    print(raw)
    raise
stem.with_name(stem.name+'_response.json').write_text(json.dumps(result,indent=2)+'\n')
output = result.get('stdout','')
stem.with_name(stem.name+'_output.txt').write_text(output)
print(json.dumps({k:v for k,v in result.items() if k!='stdout'},indent=2))
print(output)
