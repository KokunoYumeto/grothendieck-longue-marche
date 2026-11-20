from pathlib import Path
import csv,re
root=Path(__file__).resolve().parents[2]
out=root/'deliverable'
current=(root/'upload/PROMPT(20261120-181616).md').read_text()
err=current[current.index('## The errors that recur'):current.index('## Our conventions')]
conv=current[current.index('## Our conventions'):current.index('## Method')]
base=root/'source/SP114_CW_156-5_witnesses'
old=(base/'codex/J156-5-04/PROMPT.md').read_text()
absolute=old[old.index('## Absolute rules'):old.index('## Reading handwriting')]
pre=(base/'codex/J156-5-04/PREAMBLE.tex').read_text()
h=(base/'hua/transcripts/156-5/batch-02.fr.tex').read_text()
parts=re.split(r'(?m)^\\page\{(\d+)\}\s*$',h)
hpages={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
diffs=list(csv.DictReader((root/'source/SP114_CW_156-5_C_H_differences.tsv').open(),delimiter='\t',quoting=csv.QUOTE_NONE))
doubts=(base/'codex/J156-5-04/J156-5-04_doubts.md').read_text()
for scan in range(26,34):
    name=f'J156-5-04_156-5_scan{scan:03}'
    d=root/'packets'/f'{scan:03}'; d.mkdir(exist_ok=True)
    (d/'C.tex').write_text((base/'codex/J156-5-04/pages'/f'{name}.tex').read_text())
    (d/'H.tex').write_text(hpages[scan-1])
    rows=[r for r in diffs if r['page']==name]
    with (d/'differences.tsv').open('w') as f:
        w=csv.DictWriter(f,fieldnames=list(diffs[0]),delimiter='\t');w.writeheader();w.writerows(rows)
    (d/'C_doubts.md').write_text('\n'.join(line for line in doubts.splitlines() if re.match(rf'\|\s*{scan}\s*\|',line))+'\n')
    (d/'rules.md').write_text(err+'\n'+conv+'\n'+absolute+'\n## PREAMBLE.tex\n```latex\n'+pre+'\n```\n')
print('Prepared eight page-local packets.')
