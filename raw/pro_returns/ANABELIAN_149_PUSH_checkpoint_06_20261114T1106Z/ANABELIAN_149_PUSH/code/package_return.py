#!/usr/bin/env python3
"""Create immutable source checkpoints or the final audited return archive."""
from pathlib import Path
import argparse
import hashlib
import json
import zipfile

ROOT=Path(__file__).resolve().parents[1]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--checkpoint',type=int)
    ap.add_argument('--include-pdf',action='store_true')
    args=ap.parse_args()
    if args.checkpoint:
        destination=ROOT.parent/'checkpoints'/f'ANABELIAN_149_PUSH_checkpoint_{args.checkpoint:02d}.zip'
    else:
        destination=ROOT.parent/'ANABELIAN_149_PUSH.zip'
    destination.parent.mkdir(exist_ok=True)
    if destination.exists(): raise FileExistsError(f'Refusing to overwrite {destination}')
    excluded={'.aux','.toc','.out','.blg','.bbl','.synctex.gz'}
    files=[]
    for path in sorted(ROOT.rglob('*')):
        if not path.is_file(): continue
        rel=path.relative_to(ROOT)
        if '__pycache__' in rel.parts or '.git' in rel.parts: continue
        if 'build' in rel.parts and not (path.name in {'lualatex-final.log','bibtex.log'} and args.include_pdf): continue
        if path.suffix in excluded or path.name.endswith('.log'): 
            if not ('build' in rel.parts and args.include_pdf and path.name in {'lualatex-final.log','bibtex.log'}): continue
        if path.suffix=='.pdf' and not args.include_pdf: continue
        files.append(path)
    manifest=[{'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in files]
    info={'checkpoint':args.checkpoint,'pdf_included':args.include_pdf,'status':'INCOMPLETE','files':manifest}
    with zipfile.ZipFile(destination,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as archive:
        for path in files: archive.write(path,ROOT.name+'/'+str(path.relative_to(ROOT)))
        archive.writestr(ROOT.name+'/archive_manifest.json',json.dumps(info,indent=2)+'\n')
    result={'archive':str(destination),'bytes':destination.stat().st_size,'files':len(files),'sha256':hashlib.sha256(destination.read_bytes()).hexdigest(),'pdf_included':args.include_pdf}
    out=ROOT/'code'/('package_checkpoint_'+str(args.checkpoint).zfill(2)+'_output.json' if args.checkpoint else 'package_return_output.json')
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__': main()
