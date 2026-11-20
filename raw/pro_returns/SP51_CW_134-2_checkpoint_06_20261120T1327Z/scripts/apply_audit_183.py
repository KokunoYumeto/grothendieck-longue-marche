"""Record two text-audit refinements from already inspected scan183 evidence."""
from pathlib import Path
from datetime import datetime,timezone
import json
root=Path(__file__).resolve().parents[1]
p=root/'records/scan183/decision.json'
d=json.loads(p.read_text())
page=root/'pages/H134-06_134-2_scan183.tex'
t=page.read_text()
old=r'\uline{non abé}l'
new=r'n\raisebox{0pt}[0pt][0pt]{\parbox{0pt}{\figure{\begin{tikzpicture}[overlay,x=1em,y=1em]\draw[line width=0.35pt] (-0.28,-0.16) -- (0,-0.16);\end{tikzpicture}}}}\uline{on abé}l'
if old not in t:raise RuntimeError('Expected original first-n underline encoding absent')
t=t.replace(old,new)
t=t.replace('% The gap lies mainly under l; a short overlay preserves the second stroke\'s beginning under l\'s terminal extent.','% The first rule begins inside n: a short overlay preserves its terminal covered extent.\n% The gap lies mainly under l; another short overlay preserves the second rule\'s beginning under l\'s terminal extent.')
page.write_text(t)
extra=' The first stroke also begins inside the initial n (the n begins near x304, while the rule starts near x318); the final encoding uses a partial-n overlay followed by uline on abé, rather than extending the rule to the n’s left edge. This refinement uses the same already inspected crop, with no new image view.'
d['differences'][28]['final']='n [short rule under terminal extent] '+r'\uline{on abé}l [short rule under its terminal extent] \uline{ien}'
d['differences'][28]['evidence']+=extra
for q in d['reader_comparisons']:
 if q['place']=='L13 older fragment':q['B']='sou|m|de'
 if q['place']=='L21 underline gap':q['decision']+=extra
for q in d['doubt_review']:
 if q['place'].startswith('L20–23 parenthesis'):q['evidence']+=extra
for x in d['inventory']:
 if x['element']=='interrupted emphasis rule':x['first_words_or_objects']='two same-level rule segments; partial initial n, gap mainly under l, partial resumed l'
d['notes']=d['notes'].replace('The underline beneath non abélien consists of two strokes separated mainly beneath l.','The underline beneath non abélien begins inside the first n and consists of two strokes separated mainly beneath l.').replace('the small partial-letter span is drawn without filling the gap.','both partial-letter spans are drawn without extending the start or filling the gap.')
d['workflow_note']+=' A later text-only comparison caught B’s old-fragment alternative order misstated in the comparison table and the first underline endpoint represented at whole-letter granularity. Both were refined from the complete returns and the same already inspected underline crop, without a new image view or crop. See records/audit_183_disposition.md.'
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
notation=root/'notation.md'
s=notation.read_text().replace(r'\uline{non abé}l [short partial-l rule] \uline{ien}',r'n [partial-n rule] \uline{on abé}l [partial-l rule] \uline{ien}').replace('183 L21: physical gap mainly under l; same-level second segment begins under its terminal extent. Do not extend the rule through the gap.','183 L21: first segment begins within initial n; physical gap mainly under l; second starts under its terminal extent. Preserve both partial-letter endpoints and the gap.')
notation.write_text(s)
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (root/'progress.log').open('a') as f:f.write(f'scan 183 record/underline endpoint refinement {stamp}; existing inspected crop only, no new crop or view; counts unchanged\n')
(root/'records/audit_183_disposition.md').write_text('''# Scan183 text-audit refinements

The main reader compared the completed A/B readings with the consolidated record. Two refinements were made before freeze:

1. B’s old fragment before multiplicative is `sou|m|de`, not `sou|de|m`. The comparison table now quotes its actual order. The consolidated m-first reading is unchanged.
2. A’s full return explicitly located the first underline start inside the first n. The main reader’s already inspected C/21_non_abelien_underline.png likewise shows the first n beginning near x304, with the rule beginning near x318. The consolidated rule previously began at the whole n’s left edge. It now uses a short partial-n overlay followed by `uline{on abé}`, in addition to the already preserved partial-l resumption and gap. The observed endpoint coordinates remain unchanged. This is a refinement of the existing underline difference row, not an additional C/H change.

The original reports are unchanged. No image was reopened or recropped, and no new visual inspection is claimed. Notes, inventory, notation and comparison evidence have been aligned with the exact endpoint encoding. No TeX engine or rendering was used. The static structure check is rerun after assembly.
''')
