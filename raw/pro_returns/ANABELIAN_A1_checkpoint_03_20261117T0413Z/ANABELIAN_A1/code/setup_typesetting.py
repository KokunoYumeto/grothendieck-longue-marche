"""Install the verified portable TinyTeX bundle in the task workspace only.

The pre-existing /usr/bin/lualatex has no format or latex.ltx files.
This auxiliary program repairs the local typesetting runtime; it does not
alter system directories or shell startup files.
"""
from pathlib import Path
import urllib.request
import hashlib
import tarfile

root=Path(__file__).resolve().parents[2]
url=("https://github.com/rstudio/tinytex-releases/releases/download/v2026.11/"
     "TinyTeX-1-linux-x86_64-v2026.11.tar.xz")
expected="5b75befa848deae702ae6fa12ff0eef3f110d7e4e2a979ae99f101eba3c9c70d"
dest=root/"runtime_tex"
dest.mkdir(exist_ok=True)
archive=dest/"TinyTeX-1.tar.xz"
urllib.request.urlretrieve(url,archive)
actual=hashlib.sha256(archive.read_bytes()).hexdigest()
assert actual==expected,(actual,expected)
with tarfile.open(archive) as tar:
    tar.extractall(dest,filter="data")
print("Portable bundle SHA256:",actual)
print("Installed inside:",dest)
print("LuaLaTeX paths:",[str(p) for p in dest.glob("*/bin/*/lualatex")])
