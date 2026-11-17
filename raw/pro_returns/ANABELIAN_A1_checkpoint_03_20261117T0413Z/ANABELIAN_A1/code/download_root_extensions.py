"""Additional primary sources opened during the third-hour mathematical search."""
from pathlib import Path
import json
from download_literature import fetch

rows=[
 fetch(('Yang2016_newordinary',
        'https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1844.pdf',
        'root turn723446581view0 and turn507259707view0')),
 fetch(('Tsujimura2023_cyclotomes',
        'https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1975.pdf',
        'root turn288881679view0')),
]
out=json.dumps(rows,indent=2)
Path(__file__).with_suffix('.json').write_text(out+'\n')
print(out)
