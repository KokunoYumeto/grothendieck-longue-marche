"""Request the exact open PDF advertised in the publisher's public metadata."""
from pathlib import Path
from urllib.request import urlopen
from urllib.error import HTTPError
import hashlib
import json

root=Path(__file__).resolve().parent
url=('https://projecteuclid.org/ebooks/advanced-studies-in-pure-mathematics/'
     'Algebraic-Number-Theory--in-honor-of-K-Iwasawa/chapter/'
     'AndersonIhara-Theory-Gauss-Sums-and-Circular-Units/10.2969/aspm/01710055.pdf')
result={'url':url,'method':'Plain public HTTPS GET; no authentication, special headers, '
        'challenge handling or access-control bypass.'}
try:
    with urlopen(url,timeout=35) as response:
        data=response.read(20_000_001)
        result.update(status_code=response.status,final_url=response.url,
                      content_type=response.headers.get('Content-Type'))
    assert len(data)<=20_000_000
    result.update(bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
    if data.startswith(b'%PDF-'):
        path=root/'source_route_raw'/'Coleman1989_original.pdf'
        path.parent.mkdir(exist_ok=True)
        path.write_bytes(data)
        result.update(status='PDF retrieved',source_file=str(path))
    else:
        result.update(status='Non-PDF response; no retry or challenge handling',
                      prefix=data[:180].decode('utf-8',errors='replace'))
except HTTPError as error:
    result.update(status='HTTP failure; no retry or bypass',status_code=error.code,
                  reason=str(error))
except Exception as error:
    result.update(status='Retrieval failure',reason=type(error).__name__+': '+str(error))
(root/'root_coleman_exact_public_pdf.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
