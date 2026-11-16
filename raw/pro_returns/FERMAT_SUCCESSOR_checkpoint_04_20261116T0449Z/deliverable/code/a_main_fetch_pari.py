"""Fetch the official PARI source archive and verify its published digest."""
from pathlib import Path
import hashlib, urllib.request
url="https://pari.math.u-bordeaux.fr/pub/pari/unix/pari-2.19.1.tar.gz"
target=Path(__file__).resolve().parents[2]/"work/pari-2.19.1.tar.gz"
expected="419553b11ff8c3ecb8e9031b7d91d7cee003a5d721e685fcb499565c96fe2943"
with urllib.request.urlopen(url,timeout=25) as response:
    data=response.read()
actual=hashlib.sha256(data).hexdigest()
print("url",url,flush=True)
print("bytes",len(data),"sha256",actual,flush=True)
assert actual==expected
target.write_bytes(data)
print("Archive verified and saved.",flush=True)
