"""Count adjudicated physical loci by the requested error-sheet categories."""
from pathlib import Path
import collections,json

root=Path(__file__).resolve().parents[1]
records=[json.loads(p.read_text()) for p in sorted((root/'review').glob('scan*_adjudicated.json'))]
kinds=[
 ('Symbols and indices','misread symbol or index'),
 ('Words','misread word'),
 ('Omissions','omission'),
 ('Drawings and diagrams','drawing or diagram'),
 ('Readable ink left as illegible','readable ink left as `'+chr(92)+'ill{}`'),
 ('Insertion or placement','insertion or placement'),
 ('Deletion state','deletion state (struck given live or live given struck)'),
 ('Abbreviation expanded or spelling modernised','abbreviation expanded or spelling modernised'),
 ('Text not on the page','text not on the page'),
 ('Other','other')]
rows=[(d['scan'],c) for d in records for c in d['changes'] if not c.get('certainty_only') and (c.get('against_C') or c.get('against_H'))]
lines=['# Error-sheet feedback — SP114_CW_156-5','',
 'Counts concern adjudicated physical loci on these eight pages. Each locus has one primary kind and is counted once in the total; a locus can differ from both witnesses. A reading with unresolved alternatives is counted by its preferred reading and retains its confidence. Certainty-only decisions, agreements, and differences of macro syntax alone are excluded. These are correction counts, not error rates: the number of opportunities for each kind was not measured.','',
 '| Error-sheet kind | Loci | Against C | Against H | High | Medium | Low |',
 '| --- | ---: | ---: | ---: | ---: | ---: | ---: |']
for label,kind in kinds:
 rr=[c for _,c in rows if c['kind']==kind]
 vals=[len(rr),sum(bool(c.get('against_C')) for c in rr),sum(bool(c.get('against_H')) for c in rr)]+[sum(c['confidence']==v for c in rr) for v in ('high','medium','low')]
 lines.append('| '+label+' | '+' | '.join(map(str,vals))+' |')
tot=[len(rows),sum(bool(c.get('against_C')) for _,c in rows),sum(bool(c.get('against_H')) for _,c in rows)]+[sum(c['confidence']==v for _,c in rows) for v in ('high','medium','low')]
lines+=['| **Total** | '+' | '.join(f'**{v}**' for v in tot)+' |','',
 '## Distribution by scan','',
 '| Scan | Symbols | Words | Omissions | Drawings | Readable ink | Placement | Deletion state | Abbreviations | Absent text | Other |',
 '| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |']
for d in records:
 cc=collections.Counter(c['kind'] for s,c in rows if s==d['scan'])
 lines.append('| '+str(d['scan'])+' | '+' | '.join(str(cc[k]) for _,k in kinds)+' |')
lines+=['','## Patterns to add to the next run’s working sheet','',
 'No additional general error category was established. The following recurring, more specific mechanisms deserve explicit reminders because the supplied sheet does not name them at this level of detail. Their final readings and crop coordinates are in the changes log and the corresponding adjudicated records.','',
 '| Mechanism | Places | Operational lesson supported by these pages |',
 '| --- | --- | --- |',
 '| A long grouping or callout stroke can be mistaken for cancellation or an arrow. | 026 left of proposition a); 030 paired and stepped borders of right-margin notes; 032 oblique note and its long curve; 033 long left-margin separator. | Inspect the complete stroke, its endpoint, and its relation to several lines. Preserve a headless or grouping stroke in TikZ; do not invent an arrowhead. Where its function remains ambiguous, keep that uncertainty. |',
 '| A local correction and a later broad cancellation are separate visible states. | 028 cancelled construction, including struck words and an inserted d’équiv; 029 cancelled property; 031 cancelled first attempt with an interlinear replacement; 032 cancelled item a); 033 cancelled b⇒c argument. | Record the local deletion or insertion inside the larger cancellation. For a narrow excerpt, carry its inherited cancellation state explicitly. A broad strike need not intersect each letter to cancel the passage. |',
 '| A superscript-like residue may belong to an overwritten character rather than a current exponent. | 028 overwritten diagram letters and lower K; 031 extra marks after G′ and A°(G′); 033 the two overwritten A superscripts. | Distinguish surviving text from old strokes. Keep local doubt where the overlap prevents separation; do not propagate a contextual exponent merely because it would parse. |',
 '| Compressed short forms can resemble full words even when their endings are raised. | 026 évident/Invers shortened endings; 031 repeated élément-like forms and seult; 032 plus grand élément-like form and oblique précédemment ending. | Compare the baseline and raised ending separately. An expansion belongs only in the abbreviation list. A readable beginning does not establish every crowded letter of the ending. |','',
 'The supplied sheet already covers ordinary symbol confusions, prime slips, empty-set phi, literal equals for même, short forms, watermark/speck exclusion, and unsupported grammatical repairs; they are therefore not presented as new discoveries here.','',
 '## Counting safeguards from this run','',
 'Witness H sometimes acknowledges a broad cancellation or an insertion in editorial prose. Such acknowledgment is treated as agreement about the visible state; the absence of the edition’s particular macro is not itself a correction. An uncertain original preferred reading retained with another alternative is a certainty decision, unless the preferred text or its deletion/placement state changes. Overlapping crop boxes do not create additional substantive loci.','',
 'The independent-reading comparison retains raw token differences, including equivalent LaTeX encodings and different excerpt boundaries. Only the main reader’s ink-based decisions can change the transcription; harmless comparison differences do not enter the category counts.']
(root/'SP114_CW_156-5_sheet_feedback.md').write_text('\n'.join(lines)+'\n')
print(json.dumps({'loci':len(rows),'categories':len(kinds)},ensure_ascii=False))
