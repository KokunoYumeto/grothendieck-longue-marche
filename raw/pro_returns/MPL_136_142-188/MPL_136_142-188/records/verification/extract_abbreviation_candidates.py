"""List literal letter tokens ending in a dot without classifying their meaning."""
from pathlib import Path
from collections import defaultdict
import re,csv,json,hashlib
from tex_macro_extract import mask_comments
ROOT=Path('/workspace/scratch/fce80d805cc4/MPL_136_142-188')
OUT=Path('/workspace/scratch/fce80d805cc4/verification')
# Unicode letters, retaining original case/accents and internal dots/hyphens.
# Control-word names and suffixes inside longer words are excluded.
LETTER=r'[^\W\d_]'
pattern=re.compile(r'(?<![\\\w])('+LETTER+r'+(?:[.\-]+'+LETTER+r'+)*\.)(?!'+LETTER+r')',re.UNICODE)
occ=[];hashes={}
for path in sorted((ROOT/'pages').glob('*.tex')):
 data=path.read_bytes();raw=data.decode();s=mask_comments(raw)
 scan=int(re.search(r'scan(\d+)\.tex$',path.name)[1])
 hashes[path.name]=hashlib.sha256(data).hexdigest()
 for match in pattern.finditer(s):
  token=raw[match.start(1):match.end(1)]
  occ.append({'token':token,'scan':scan,'tex_line':s.count('\n',0,match.start(1))+1,'page_file':path.name})
grouped=defaultdict(list)
for r in occ:grouped[r['token']].append((r['scan'],r['tex_line']))
rows=[]
for token,refs in sorted(grouped.items()):
 rows.append({'token':token,'occurrences':len(refs),'scan_line_locations':'; '.join(f'{scan}:{line}' for scan,line in sorted(set(refs)))})
with (OUT/'abbreviation_candidate_occurrences.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['token','scan','tex_line','page_file']);w.writeheader();w.writerows(occ)
with (OUT/'abbreviation_candidates_deduplicated.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['token','occurrences','scan_line_locations']);w.writeheader();w.writerows(rows)
md=['# Literal abbreviation candidates','','Mechanically extracted letter tokens ending in a dot, retaining exact case, accents, internal dots and hyphens. These candidates include sentence-ending words and mathematical letters; no abbreviation meaning is assigned. TeX comments and control-word names are excluded. Locations are scan:TeX-source-line. Tokens are taken literally from source, without typeset-text reconstruction.','',f'{len(occ)} occurrences; {len(rows)} distinct exact tokens.','', '| Token | Occurrences | Scan:line locations |','|---|---:|---|']
for r in rows:md.append(f"| `{r['token']}` | {r['occurrences']} | {r['scan_line_locations']} |")
(OUT/'abbreviation_candidates.md').write_text('\n'.join(md)+'\n')
(OUT/'abbreviation_source_hashes.json').write_text(json.dumps(hashes,indent=2)+'\n')
changed=[]
for name,digest in hashes.items():
 if hashlib.sha256((ROOT/'pages'/name).read_bytes()).hexdigest()!=digest:changed.append(name)
summary={'pages':len(hashes),'occurrences':len(occ),'distinct_exact_tokens':len(rows),'sources_changed_during_extraction':changed}
(OUT/'abbreviation_extraction_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
