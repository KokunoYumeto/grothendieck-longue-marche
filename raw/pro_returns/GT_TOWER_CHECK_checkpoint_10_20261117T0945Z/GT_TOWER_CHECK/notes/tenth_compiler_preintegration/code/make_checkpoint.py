#!/usr/bin/env python3
"""Make one immutable hourly checkpoint, retaining all authored deliverables."""
from pathlib import Path
import argparse,hashlib,json,shutil,zipfile,datetime
parser=argparse.ArgumentParser()
parser.add_argument('number',type=int)
args=parser.parse_args()
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT.parent
number=args.number
name=f'GT_TOWER_CHECK_checkpoint_{number:02d}.zip'
target=BASE/name
assert not target.exists(), 'Never overwrite a checkpoint'
# Copy newly received work as a source snapshot without changing the checked PDF.
work=BASE/'work'
for p in work.iterdir():
    if p.is_file() and p.suffix in {'.tex','.md','.bib'}:
        shutil.copy2(p,ROOT/'notes/source_fragments'/p.name)
for dirname in ['centralizer_code','tower_code','ghost_code']:
    for p in (work/dirname).iterdir():
        if p.is_file():shutil.copy2(p,ROOT/'code'/p.name)
# Preserve the additional coefficient-four computations, including failed lifts.
for dirname in ("ghost_mod4","centralizer_mod4"):
    if (work/dirname).exists():
        shutil.copytree(work/dirname,ROOT/"code"/dirname,dirs_exist_ok=True,
                        ignore=shutil.ignore_patterns("__pycache__"))
# Bytecode and runtime caches are reproducible intermediates, not deliverables.
excluded_parts={'__pycache__','tex_cache','.texruntime','.gapruntime'}
files=[p for p in sorted(ROOT.rglob('*')) if p.is_file() and not any(x in excluded_parts for x in p.relative_to(ROOT).parts)]
previous=BASE/f'GT_TOWER_CHECK_checkpoint_{number-1:02d}.zip'
comparison={'previous_checkpoint':previous.name,'omitted':[],'superseded':[],'unchanged':0,
            'preserved_prior_bytes':[]}
# Preserve each changed earlier version byte for byte.  This includes proof
# passages, programs, their actual output, and an earlier checked PDF.  We
# create no additional ZIP and never modify any earlier checkpoint.
for prior_number in range(1,number):
    prior=BASE/f'GT_TOWER_CHECK_checkpoint_{prior_number:02d}.zip'
    if not prior.exists():continue
    with zipfile.ZipFile(prior) as z:
        for info in z.infolist():
            if info.is_dir():continue
            rel=Path(info.filename).relative_to(ROOT.name)
            if rel.parts[:2]==('notes','checkpoint_history'):continue
            data=z.read(info.filename)
            local=ROOT/rel
            if local.exists() and local.read_bytes()==data:continue
            retained=ROOT/'notes/checkpoint_history'/f'{prior_number:02d}'/rel
            retained.parent.mkdir(parents=True,exist_ok=True)
            if retained.exists():assert retained.read_bytes()==data
            else:retained.write_bytes(data)
            comparison['preserved_prior_bytes'].append({
                'checkpoint':prior.name,'file':info.filename,
                'retained_as':str(retained.relative_to(BASE)),
                'reason':'Exact earlier version retained; current path carries the updated version'})
if previous.exists():
    with zipfile.ZipFile(previous) as z:
        for info in z.infolist():
            if info.is_dir():continue
            old=info.filename
            local=BASE/old
            if not local.exists():comparison['omitted'].append({'file':old,'reason':'Missing: requires explicit resolution before archive'})
            elif hashlib.sha256(z.read(old)).digest()!=hashlib.sha256(local.read_bytes()).digest():
                comparison['superseded'].append({'file':old,'replacement':old,'reason':'Updated proof, ledger, report, bibliography, build output or working source snapshot'})
            else:comparison['unchanged']+=1
    assert not comparison['omitted'],comparison['omitted']
record=ROOT/'notes'/f'checkpoint_{number:02d}_retention.json'
record.write_text(json.dumps(comparison,indent=2)+'\n')
files=[p for p in sorted(ROOT.rglob('*')) if p.is_file() and not any(x in excluded_parts for x in p.relative_to(ROOT).parts)]
manifest=ROOT/'notes'/f'checkpoint_{number:02d}_manifest.tsv'
manifest.write_text('path\tbytes\tsha256\n'+'\n'.join(f'{p.relative_to(BASE)}\t{p.stat().st_size}\t{hashlib.sha256(p.read_bytes()).hexdigest()}' for p in files if p!=manifest)+'\n')
files=[p for p in sorted(ROOT.rglob('*')) if p.is_file() and not any(x in excluded_parts for x in p.relative_to(ROOT).parts)]
with zipfile.ZipFile(target,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for p in files:z.write(p,p.relative_to(BASE))
with zipfile.ZipFile(target) as z:assert z.testzip() is None
sha=hashlib.sha256(target.read_bytes()).hexdigest()
metadata={'checkpoint':name,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'files':len(files),'bytes':target.stat().st_size,'sha256':sha,'previous_omissions':len(comparison['omitted'])}
# The ZIP hash cannot be a member of its own byte-identical archive.
(BASE/(name+'.json')).write_text(json.dumps(metadata,indent=2)+'\n')
print(json.dumps(metadata,indent=2))
