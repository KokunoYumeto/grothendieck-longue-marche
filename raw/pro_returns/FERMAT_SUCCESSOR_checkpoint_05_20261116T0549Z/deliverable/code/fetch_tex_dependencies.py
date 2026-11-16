"""Fetch the four absent LuaLaTeX runtime packages from the official CTAN mirror.

This records the command used during the run; upstream versions may change.
The exact downloaded archive digests are recorded in fetch_tex_dependencies.out.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib, io, json, tarfile, urllib.request

ROOT = Path(__file__).resolve().parents[2]
DEST = ROOT / 'work' / 'texformat' / 'texmf'
DEST.mkdir(parents=True, exist_ok=True)

def fetch(name):
    url = ('https://mirror.math.princeton.edu/pub/CTAN/systems/texlive/'
           f'tlnet/archive/{name}.tar.xz')
    data = urllib.request.urlopen(url, timeout=60).read()
    with tarfile.open(fileobj=io.BytesIO(data), mode='r:xz') as archive:
        archive.extractall(DEST, filter='data')
    return dict(name=name, bytes=len(data), sha256=hashlib.sha256(data).hexdigest(), url=url)

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=4) as pool:
        for result in pool.map(fetch, ['luaotfload','lualibs','lua-uni-algos','luatexbase']):
            print(json.dumps(result), flush=True)
