"""Build final feedback counts from the recorded, root-read differing places."""
from workflow import ROOT, assemble, mdtable, utc
from collections import Counter
import json

D = [json.loads(p.read_text()) for p in sorted((ROOT / 'records').glob('*.json'))]
R = [r for d in D for r in d['rows']]
kinds = [
    'misread symbol or index', 'misread word', 'omission', 'drawing or diagram',
    r'readable ink left as `\ill{}`', 'insertion or placement',
    'deletion state (struck given live or live given struck)',
    'abbreviation expanded or spelling modernised', 'text not on the page', 'other']
rows = []
for kind in kinds:
    rr = [r for r in R if r['kind'] == kind]
    rows.append([kind, len(rr), sum(r['C'] for r in rr), sum(r['H'] for r in rr)])
rows.append(['TOTAL', len(R), sum(r['C'] for r in R), sum(r['H'] for r in R)])
text = '# Error-sheet feedback\n\n'
text += ('Counts refer to the substantive places recorded in the change log. Each place has one primary '
         'kind; a row differing from both witnesses counts once in the places column and once in each '
         'witness column. Certainty-only decisions, macro/font equivalents and H editorial material '
         'about other pages are excluded. H has no text for scans 157, 160, 162, 164 and 172.\n\n')
text += mdtable(['Error-sheet kind', 'Unique places', 'Against C', 'Against H'], rows)
text += '\n## Confidence and supplied marks\n\n'
conf = [[level, sum(r['confidence'] == level for r in R),
         sum(r['confidence'] == level and r['C'] for r in R),
         sum(r['confidence'] == level and r['H'] for r in R)]
        for level in ['high', 'medium', 'low']]
text += mdtable(['Confidence', 'Unique places', 'Against C', 'Against H'], conf)
dc = Counter(x['decision'] for d in D for x in d['decisions'])
text += '\n' + mdtable(['Decision on supplied mark', 'Count'], [[k, dc[k]] for k in ['first', 'alternative', 'other', 'undecided']])
text += ('\nThe 77 marks and the 434 differing places are different reporting units. In particular, '
         'resolving Div on 176 changes certainty without adding a C difference. The 75 remaining-doubt '
         'entries include unmarked passages and groups of related tokens.\n')
text += r'''
## Recurring patterns to add to future reading prompts

These specify recurrent subcases encountered within the ten kinds above. Each is tied to observed places.

| Pattern | Places and observed consequence |
|---|---|
| Short terminal pen returns read as complete arrowheads | 139 upper squares and first concluding connector; 149 bottom chain; 150 character map; 161 opening sequence; 174 localization rows; 176 both maps; 177 short and long sequences. Several connectors end in a cap or return stroke while others on the same sheet have a separate head. |
| A whole-block cancellation containing earlier local cancellations | 142 abandoned paragraph; 148 boxed field-of-definition draft; 163 two lower blocks; 179 opening draft. The nested local states carry readable words and replacements even though the whole passage is later cancelled. |
| A later insertion lying beside the border of a cancelled block | 143 centrality/quotient additions; 148 reciprocal sentence beside the cancelled Galois restart; 179 noetherian condition below the brown draft boundary. Extending the boundary across adjacent live ink changes its state. |
| Retracing interpreted as deletion without an independent cancelling stroke | 151 ss-groupe; 159 union des sections; 177 isolated μ. The retraced letter strokes themselves must be kept separate from the transverse strikes visible elsewhere on the same pages. |
| Literal scope of brackets and braces | 173 grouped coefficient formulas and the lower n≠0 leaders; 174 brace enclosing only the first two rows; 177 right bracket enclosing only degrees 1, 2 and 3. A well-formed inferred grouping can extend beyond the written delimiter. |
| Reference strokes or small drawn fragments omitted as decoration | 143 curved diagonal inclusion; 173 two circle-and-rule references and the hatched mark beneath si; 174 point-line terminal tick and marginal vertical rule; 177 damaged tail fragments and diagonal separator. Their visible strokes are retained with role uncertainty where necessary. |
| A source label surviving only in a witness's editorial description | 177 margin degree pairs, bracket, and lower somme des inv. caption; 179 underlined Div labels. Such descriptions supplied search cues; the image supplied the content and placement. |
| Short letters attached to a cancellation boundary | 141 deleted prefix épi followed by live morphisme; 149 deleted E immediately before live K in an insertion; 176 live un followed by deleted e extension. A boundary can divide a word or a compact replacement sequence. |

## Reading practice supported by this run

The native halves settled many agreed readings and small clear marks. The single-crop rule left explicit doubts where crossings destroyed stroke information; repeating a crop would not restore that ink. The later Div definition supplied a useful cross-page comparison. The same approach left G⁰/G* on 165 and the raised K-bar appendages on 147 unresolved because their covered or unexplained marks did not become visible elsewhere.

The change counts include both transcription content and diplomatic state. Underlining, arrow endpoints, added words, and deletion boundaries account for many H rows. C retained more of that structure, but its unmarked words, formulas, and diagrams still required comparison. Both witnesses omitted the extra tensor mark on 161 and some minor drawn elements on the later sheets. The page-by-page evidence and confidence should accompany any use of the counts.

All 25 first readings and all 25 second audits are recorded in order. Mathematical checks are restricted to CHECK_EVENTS.tsv and the corresponding numbered notes. No external research, OCR, or TeX compilation was performed.
'''
(ROOT / 'feedback_final.txt').write_text(text)
assemble()
with (ROOT / 'progress.log').open('a') as f:
    f.write('final feedback and legibility assessment assembled ' + utc() + '\n')
