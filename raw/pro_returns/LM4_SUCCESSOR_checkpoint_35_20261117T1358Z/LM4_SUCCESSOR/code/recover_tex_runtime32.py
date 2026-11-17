"""Root-authorized private TeX infrastructure recovery from genuine inputs."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
import os
import subprocess
import urllib.request
import zipfile

root = Path(__file__).resolve().parents[1]
runtime = root.parent / 'tex_runtime'
logs = root / 'records/tex_recovery32'
logs.mkdir(exist_ok=True)
for name in ('vendor', 'downloads', 'formats', 'maps', 'var', 'config'):
    (runtime / name).mkdir(parents=True, exist_ok=True)
env_values = json.loads((root / 'records/tex_recovery/env.json').read_text())
env_values['TEXMF'] = '{' + str(runtime / 'vendor') + ',/usr/share/texlive/texmf-dist,/usr/share/texmf}'
env_values['TEXMFVAR'] = str(runtime / 'var')
env_values['TEXMFCONFIG'] = str(runtime / 'config')
env_values['TEXFORMATS'] = str(runtime / 'formats') + '//:'
env_values['TEXINPUTS'] = '.:' + str(runtime / 'vendor') + '//:/usr/share/texlive/texmf-dist/tex//:/usr/share/texmf/tex//:'
env_values['LUAINPUTS'] = env_values['TEXINPUTS']
env_values['TEXFONTMAPS'] = str(runtime / 'maps') + '//:/usr/share/texlive/texmf-dist/fonts/map//:/usr/share/texmf/fonts/map//:'
(runtime / 'env.json').write_text(json.dumps(env_values, indent=2) + '\n')
(logs / 'env.json').write_text(json.dumps(env_values, indent=2) + '\n')
env = dict(os.environ, **env_values)
packages = ['lua-uni-algos', 'lualibs', 'luaotfload', 'luatexbase']
mirrors = ['https://mirrors.mit.edu/CTAN/', 'https://mirrors.ibiblio.org/CTAN/',
           'https://ctan.math.washington.edu/tex-archive/', 'https://mirrors.ctan.org/']


def download(name):
    archive = runtime / 'downloads' / (name + '.zip')
    attempts = []
    for mirror in mirrors:
        url = mirror + 'macros/luatex/generic/' + name + '.zip'
        try:
            with urllib.request.urlopen(url, timeout=12) as response:
                data = response.read()
            archive.write_bytes(data)
            with zipfile.ZipFile(archive) as z:
                assert z.testzip() is None
                for info in z.infolist():
                    p = Path(info.filename)
                    assert not p.is_absolute() and '..' not in p.parts
                z.extractall(runtime / 'vendor')
            result = dict(name=name, url=url, bytes=len(data),
                          sha256=hashlib.sha256(data).hexdigest(), attempts=attempts)
            (logs / (name + '_download.json')).write_text(json.dumps(result, indent=2) + '\n')
            return result
        except Exception as exc:
            attempts.append({'url':url, 'error':repr(exc)})
            (logs / (name + '_download_failures.json')).write_text(json.dumps(attempts, indent=2) + '\n')
    raise RuntimeError('All official mirrors failed: ' + name)


def command(label, args, cwd):
    run = subprocess.run(args, cwd=cwd, env=env, capture_output=True)
    (logs / (label + '.out')).write_bytes(run.stdout)
    (logs / (label + '.err')).write_bytes(run.stderr)
    (logs / (label + '.json')).write_text(json.dumps({'args':args, 'cwd':str(cwd),
                                                   'returncode':run.returncode}, indent=2) + '\n')
    if run.returncode:
        raise RuntimeError(label + ' failed, see retained output')
    return run


with ThreadPoolExecutor(max_workers=4) as pool:
    results = list(pool.map(download, packages))
(logs / 'official_archives.json').write_text(json.dumps(results, indent=2) + '\n')
for package, source in [('lualibs', 'lualibs.dtx'), ('luatexbase', 'luatexbase.ins')]:
    files = list((runtime / 'vendor').rglob(source))
    assert len(files) == 1, (source, files)
    command(package + '_docstrip', ['tex', '--ini', '--interaction=nonstopmode',
                                  '\\input plain \\input ' + source], files[0].parent)

# Use genuine installed font map entries. Omit prose headings (the exact
# source of the nine old warnings), comments and duplicate font names.
maps, chosen, omitted = [], {}, []
for tree in (Path('/usr/share/texlive/texmf-dist/fonts/map/dvips'),
             Path('/usr/share/texmf/fonts/map/dvips')):
    if tree.exists():
        for source in sorted(tree.rglob('*.map')):
            maps.append(str(source))
            for raw in source.read_text(errors='replace').splitlines():
                line = raw.strip()
                if not line or line.startswith(('%', '#', ';')):
                    continue
                parts = line.split()
                if len(parts) < 2 or ('<' not in line and '"' not in line):
                    omitted.append({'source':str(source), 'line':raw})
                    continue
                chosen.setdefault(parts[0], line)
map_data = ('\n'.join(chosen.values()) + '\n').encode()
for name in ('pdftex.map', 'psfonts.map'):
    (runtime / 'maps' / name).write_bytes(map_data)
(logs / 'fontmap_sources.json').write_text(json.dumps({'sources':maps, 'entries':len(chosen),
    'omitted_headings':omitted, 'map_sha256':hashlib.sha256(map_data).hexdigest()}, indent=2) + '\n')
command('format_setup', ['luahbtex', '--ini', '--interaction=nonstopmode',
                        '--jobname=lualatex', '--progname=lualatex', 'lualatex.ini'], runtime / 'formats')
assert (runtime / 'formats/lualatex.fmt').is_file()
command('format_discovery', ['kpsewhich', '--progname=lualatex', 'lualatex.fmt'], root)
record = dict(completed_at=datetime.now(timezone.utc).isoformat(), env=str(runtime / 'env.json'),
              format_sha256=hashlib.sha256((runtime / 'formats/lualatex.fmt').read_bytes()).hexdigest(),
              packages=results, map_entries=len(chosen), main_paper_build_performed=False)
(logs / 'runtime_ready.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
