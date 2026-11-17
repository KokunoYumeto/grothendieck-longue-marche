from pathlib import Path
import json
from record_page import ROOT,combine,now
changes={
33:[(r'\widehat A_\unsure{\mathcal{T}|\tau}',r'\widehat A_{\unsure{\mathcal{T}|\tau}}')],
36:[(r'\widehat \unsure{\mathcal{S}|S}_{ab}',r'\widehat{\unsure{\mathcal{S}|S}}_{ab}')],
44:[(r"\text{\'\'}",r"\text{''}")]
}
for scan,reps in changes.items():
 p=ROOT/'pages'/f'MPL_137_002-044_137_scan{scan:03}.tex';s=p.read_text()
 for old,new in reps:
  assert old in s,(scan,old)
  s=s.replace(old,new)
 p.write_text(s)
 rpath=ROOT/'records'/f'{scan:03}.json';r=json.loads(rpath.read_text())
 r['audit_notes'].append({'utc':now(),'note':'Pre-freeze notation serialization: braces around a multi-token math argument, or literal apostrophes for the visually audited ditto strokes; no new reading.','replacements':reps})
 rpath.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
combine()
with (ROOT/'progress.log').open('a') as f:
 f.write('notation comparison completed '+now()+'; first-pass and audited notation compared across all pages before context access. Stars, raised solid dots, true primes, exclamation marks, script/Greek alternatives, quotation marks, subset/dash/arrow distinctions, alphabet variants and abbreviation spellings retained according to local ink. No context used.\n')
 f.write('pre-freeze TeX serialization repairs '+now()+'; grouped multi-token subscript/hat arguments on 033/036 and wrote literal ditto apostrophes on 044.\n')
print('Notation serialization finalized.')
