#!/usr/bin/env python3
from pathlib import Path
import argparse,json,shutil
p=argparse.ArgumentParser();p.add_argument('page');p.add_argument('version');a=p.parse_args()
b=Path(__file__).resolve().parent.parent.parent; out=b/'out';dest=b/'work/inputs'/a.page
shutil.copyfile(out/'notation.md',dest/'notation.md')
shutil.copyfile(out/'briefs'/('reader_brief_'+a.version+'.md'),dest/'brief.md')
shutil.copyfile(out/'PREAMBLE.tex',dest/'PREAMBLE.tex')
(out/'briefs'/(a.page+'_notation.md')).write_text((dest/'notation.md').read_text())
for reader in ['R1','R2','R3']:(out/'readers'/a.page/reader).mkdir(parents=True,exist_ok=True)
with (out/'records/reader_runs.tsv').open('a') as f:f.write(a.page+'\t'+a.version+'\n')
print('Prepared '+a.page+' with '+a.version)
