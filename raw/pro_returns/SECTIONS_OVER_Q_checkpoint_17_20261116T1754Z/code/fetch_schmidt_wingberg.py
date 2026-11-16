"""Retrieve and retain the primary Schmidt--Wingberg source used by A.122."""
from pathlib import Path
from hashlib import sha256
import urllib.request
import subprocess
url="https://arxiv.org/pdf/math/9809211"
p=Path("work/sources/schmidt_wingberg1998.pdf")
if not p.exists():
    data=urllib.request.urlopen(url,timeout=30).read()
    assert data.startswith(b"%PDF")
    p.write_bytes(data)
data=p.read_bytes()
assert data.startswith(b"%PDF")
subprocess.run(["pdftotext","-layout",str(p),str(p.with_suffix(".txt"))],check=True)
print("Primary URL:",url)
print("Retained bytes:",len(data))
print("SHA256:",sha256(data).hexdigest())
print("Theorem13, printed14--19: exact unramified local input and cyclic output.")
