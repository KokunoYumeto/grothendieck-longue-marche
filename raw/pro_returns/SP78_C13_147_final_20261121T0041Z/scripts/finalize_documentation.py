"""Close the completed review descriptions without changing any manuscript reading."""
from pathlib import Path
from datetime import datetime,timezone
import json
w=Path(__file__).resolve().parents[1]
p=w/'workflow/notation_concordance.md';s=p.read_text()
a=s.index('## Pending source checks');b=s.index('## Alphabets',a)
s=s[:a]+r'''## Completed source checks

Root has personally checked all three remaining decoration contrasts. The dated resolutions and historical findings are preserved in `workflow/notation_crosspage_review.json`. These checks confirmed local differences; no page text was regularized.

| ID | Source finding | Crops personally checked by root, relative to `crops/` |
| --- | --- | --- |
| NCR-01 | The serifed I at060:26 has no detached roof. The earlier targets at060:6–9 and058:5 have roofs. Preserve the bare I in(75). | `147_scan060_second_B07.png`, `147_scan060_second_B02.png`, `147_scan058_second_B03.png`, `147_scan058_second_B04.png` |
| NCR-02 | Both NB M factors at060:14 have roofs without bang stems/dots; both factors at060:8 have distinct bangs. The notation entry is scoped to actual bang-bearing occurrences. | `147_scan060_second_B03.png`, `147_scan060_second_B02.png` |
| NCR-03 | At077:4–7 the M-factor I has a roof, the upper T-factor I is bare, and the lower T-factor nu is bare. Both earlier072 nu indices have roofs. | `147_scan077_second_B02.png`, `147_scan072_second_B14.png` |

'''+s[b:]
s=s.replace('**Source checks NCR-01–03 remain pending root’s personal crop review.** No source reading was changed or new source interpretation certified.','**Source checks NCR-01–03 are complete.** Root confirmed the local source variations listed above; no page text changed in that final notation check.')
s=s.replace('The original cross-page source checks and historical hashes remain in `workflow/notation_crosspage_review.json`.','The original cross-page findings and historical hashes, together with the later dated root source resolutions, remain in `workflow/notation_crosspage_review.json`.')
p.write_text(s)
p=w/'notation.md';s=p.read_text();s+='\n| Local I roof in symmetric-group indices | Bare I in060(75); hatted I in060(74) and058(72) | Root’s final source check distinguishes the serifed I from a detached two-arm roof. No accent is supplied to(75). |\n| Local M bang omission in the NB | Both060 NB factors have M roofs without bangs | Root checked060 B03 against B02: no raised stem/dot beside either NB factor, while row3 of(74) has both bangs. |\n';p.write_text(s)
p=w/'run_state.json';j=json.loads(p.read_text());j['stage']='all24 readings and audits complete; final structural validation and transcription freeze';j['notation_review_complete']=True;j['audit_box_totals']={'boxes':372,'differing_boxes':296,'changed_boxes':57};p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
print('Final documentary descriptions reconciled.')

# The two060 rows were subsequently moved into the existing notation table, before the pencil-foliation prose.
