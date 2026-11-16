from pathlib import Path
from datetime import datetime,timezone
from collections import Counter
import json,hashlib,csv,re
root=Path('/workspace/scratch/b8e2c31cadf4/work')
base='MPL_36_053-085+39'
freeze=json.loads((root/'qa/freeze.json').read_text())
checks=[]
for relative,expected in freeze['sha256'].items():
 p=root/relative
 actual=hashlib.sha256(p.read_bytes()).hexdigest()
 checks.append({'file':relative,'expected':expected,'actual':actual,'unchanged':actual==expected})
assert len(checks)==50 and all(x['unchanged'] for x in checks)
pages=sorted((root/'pages').glob('*.tex'));assert len(pages)==49
with (root/(base+'_inventory.csv')).open(newline='')as f:inv=list(csv.DictReader(f))
assert len(inv)==1020 and all(x['transcribed']=='yes'for x in inv)
items=json.loads((root/'research_items.json').read_text());assert [x['id']for x in items]==[f'N{i:02}'for i in range(1,98)]
assert all(x['kind']=='own idea' or '“'in x['note']for x in items)
assert all(x['confidence'] and x['reason']for x in items if x['kind']=='own idea')
searches=json.loads((root/'qa/context_searches.json').read_text());assert len(searches)==97
assert all(x['id']==y['id']and x['query']==y['query']for x,y in zip(items,searches))
assert len(json.loads((root/'qa/context_comparison_searches.json').read_text()))==16
bib=(root/'notes_bibliography.md').read_text()
for b in {b for x in items for b in x['bib']}:assert len(re.findall(r'^\*\*'+b+r'\.',bib,re.M))==1
struct=json.loads((root/'qa/structural_qa.json').read_text())
assert not any(x['severity']=='error'for x in struct['issues'])
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
report={'checked_utc':now,'frozen_utc':freeze['frozen_utc'],'all_50_transcription_hashes_unchanged':True,'checks':checks,'page_count':49,'inventory_elements':1020,'inventory_all_yes':True,'research_items':97,'own_ideas':sum(x['kind']=='own idea'for x in items),'kind_counts':dict(Counter(x['kind']for x in items)),'per_item_context_searches':97,'context_comparison_searches':16,'structural_errors':0,'structural_review_dispositions':[{'source':'36/065, line19','disposition':'The illegible token is inside a text argument and represents two prose words, not a mathematical symbol; retained as audited.'},{'source':'39/020, inventory element7','disposition':'The drawing spans the cancelled upper block; coarse top-to-bottom metadata ranking does not warrant moving it past its content; retained as audited.'}],'tex_compiled':False,'tex_limit':'TeX formats, class and required packages are absent; only structural checks were possible.'}
(root/'qa/final_verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
verification=f'''## Verification and delivery scope

The final integrity check at **{now}** verified that **all 49 page-file hashes and the combined-transcription hash are unchanged** from the freeze at **2026-11-16 17:26:43 UTC**. The combined SHA-256 is `{freeze['sha256'][base+'_transcription.tex']}`. Context file contents were first accessed at **17:26:48 UTC**, after the freeze. The exact hashes, timestamps and final comparison are recorded in `progress.log`, `transcription_hashes.sha256`, `qa/freeze.json` and `qa/final_verification.json`.

The primary transcriber personally inspected all 49 whole-page images and all 98 halves, saved each page before proceeding, and carried out the second complete visual audit and global notation comparison. No OCR or delegated manuscript transcription was used. Delegated assistance was confined to mechanical metadata checks, primary-reference research and critical review of the already written research notes; it did not supply or revise manuscript readings.

The inventory has **1,020 elements**, all marked `yes`, with coverage of all 49 retained scans. The combined fragment exactly equals the ordered page-file concatenation. Mechanical checks found no structural error in page markers, braces, mathematical delimiters, environments or the permitted macro usage. Two coarse review flags were checked: the `\\illegible{{2}}` inside a text argument on 36/065 represents prose words, and the overlapping cancellation drawing on 39/020 explains its inventory position. Their dispositions are retained in the final QA record.

The notes contain **97 numbered items**, including **22 explicitly labelled own ideas**, each with confidence and reason. Actual context searches are recorded for every item; 87 yielded literal matches and 10 did not. A keyword hit is only a location lead, and broad incidental hits are not treated as mathematical evidence. The ten no-hit cases either add material absent from the supplied plan/excerpts or add a zero-cycle hypothesis missing from the truncated H1 finding; the comparison matrix separately addresses all 16 substantive entries and the three run-state IDs. The short entries and their context metadata were checked independently.

**No compiled TeX rendering is claimed.** The installed executables lacked the TeX formats, class and required packages, including TikZ and tikz-cd. Structural validation is consequently distinct from rendering validation and does not certify every reading or the eventual layout of user-defined macros. The text remains a fragment without a preamble, as requested. The final doubts file identifies the least secure handwritten and cancelled passages.

Historical first-pass leads, the audit journal, inventory records, scripts and QA reports are retained as work documentation. The final page files, final doubts table and these research notes take precedence over preliminary reading questions in those logs. Source scans, image crops, supplied attachments and context files are excluded from the archive.
'''
(root/'notes_verification.md').write_text(verification)
with (root/'progress.log').open('a')as f:
 f.write('research notes complete '+now+'; 97 notes, 22 own ideas with confidence/reason, 97 per-item context searches, 16 substantive context comparisons; self-flags and titles/page-count sections complete\n')
 f.write('final hash check '+now+'; all 49 page files and combined transcription SHA-256 unchanged from freeze; combined '+freeze['sha256'][base+'_transcription.tex']+'\n')
 f.write('final structural QA '+now+'; 49 pages, 1020 inventory elements all yes, ordered combined match, zero structural errors; two review flags resolved as prose-word illegibility and overlapping drawing; no compiled TeX rendering claimed\n')
print(json.dumps({k:v for k,v in report.items() if k!='checks'},ensure_ascii=False,indent=2))
