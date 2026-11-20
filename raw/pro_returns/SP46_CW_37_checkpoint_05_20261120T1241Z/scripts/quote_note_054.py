"""Supply the writer's own words for the doubts already recorded on scan 054."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
O=Path(__file__).resolve().parents[1]
page=O/'pages/H37-01_37_scan054.tex';before=hashlib.sha256(page.read_bytes()).hexdigest()
p=O/'decisions/scan054.json';d=json.loads(p.read_text())
d['notes']="""First leaf of a handwritten English letter on Harvard University stationery, dated ‘Aug 4, 1969’ and addressed ‘Dear Grothendieck,’. The printed address is Cambridge, Massachusetts 02138, Department of Mathematics, 2 Divinity Avenue. The quoted title is ‘Exposé V. Systèmes projectifs J-adiques, par J.P. Jouanolou.’ The pencil instruction ‘Faire copie / pour Jouanolou’ is framed; a vertical pencil mark, a dark mark beside the date and an oblique pair beside pro-A are preserved. There is no signature, closing, authorial page number or stated total count on this leaf; 53 is archival. The signed continuation on scan 055 supports attribution of the letter body to R. Hartshorne. The annotations remain unnamed.

The writer qualifies the seminar attribution with ‘I suppose’ and asks ‘to which seminar they belong, and whether there is a more recent edition?’ His central reservation is ‘I do not understand the proof’ of the ‘Theorem of Shih’, A.3.1 on p.46. He writes ‘It seems to me that the lemma on p. 45 is valid only for’ r>p and says the equivalence of (i) and (ii) ‘is not clear’. He adds ‘I do agree, however, with the weaker statement’ ‘(resp....)’ in parentheses. ‘This casts doubt’ on A.3.2, p.47, and Prop.5.3.1, p.40. He proposes that ‘These difficulties would disappear’ with the usual equivalence in pro-A rather than the finer category P_AR. His further questions are ‘Isn’t the spectral sequence actually biregular in case of a finite filtration?’ and ‘I think the hypothesis should be stated for’ n and n+1, ‘instead of’ n and n−1. These quotations report his doubts and proposed corrections; none is independently proved here.

Two cancellations are retained. The retraced throughout|throughtout is a reader uncertainty, not a demonstrated authorial slip. The stop after p.40 and the dot over the first minus are resolved. H supplies description only and has no collation rows."""
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
assert before==hashlib.sha256(page.read_bytes()).hexdigest()
t=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
p=O/'global_check_events.json';events=json.loads(p.read_text())
events.append(dict(statement_id='S054-NOTE-QUOTATIONS',date=t,who='GPT-6 Astra Pro; effort not exposed; main second-pass run',type='used and rechecked in this run',outcome='Compared the already-adjudicated scan 054 page text with its notes and added the writer’s exact phrases for each stated doubt, question and proposed correction. Source reporting only; no image was reopened and no mathematical proof was checked. Page SHA-256 unchanged.'))
p.write_text(json.dumps(events,ensure_ascii=False,indent=2)+'\n')
with (O/'progress.log').open('a') as f:f.write(f'scan 054 note quotations made explicit {t}; page SHA-256 unchanged\n')
print('Scan 054 notes now quote the writer’s stated doubts; page bytes unchanged.')
