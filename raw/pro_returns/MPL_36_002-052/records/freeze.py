from pathlib import Path
import csv,datetime,hashlib,json,re,shutil
root=Path(__file__).resolve().parents[1]
stamp=lambda:datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
state=json.loads((root/'records/run_state.json').read_text()); scans=state['expected_scans']
combined=root/'MPL_36_002-052_transcription.tex'
assert not (root/'records/frozen_hashes.json').exists()
files=[root/'pages'/f'MPL_36_002-052_36_scan{n:03}.tex' for n in scans]+[combined]
assert len(list((root/'pages').glob('*.tex')))==31
s=combined.read_text(); assert s.startswith('\\cotefile{36}\n\\scanpage{3}')
assert list(map(int,re.findall(r'\\scanpage\{(\d+)\}',s)))==scans
assert '\\documentclass' not in s and '\\newcommand' not in s and '\\includegraphics' not in s
assert '[...]' not in s
inventory=list(csv.DictReader((root/'MPL_36_002-052_inventory.csv').open()))
assert {int(r['scan']) for r in inventory}==set(scans)
assert all(r['transcribed']=='yes' for r in inventory)
assert all(r['sheet_kind'] in ('text','cover','cancelled_draft','reused_typed') for r in inventory)
assert all(r['kind'] in ('text','display','diagram','drawing','margin note','insertion','deletion') for r in inventory)
log=(root/'progress.log').read_text()
for n in scans:
 assert re.search(fr'36 scan {n:03} done ',log)
 assert re.search(fr'scan {n:03} audited ',log)
assert 'context opened ' not in log
qa=Path('/workspace/scratch/60a038f0158e/qa')
compiler=(qa/'validation_wrapper.log').read_text()
assert 'Output written on ' in compiler
assert not re.search(r'^!|Overfull|LaTeX Warning|Package .* Warning',compiler,re.M)
validation=root/'records/validation'; validation.mkdir(exist_ok=True)
shutil.copyfile(qa/'validation_wrapper.log',validation/'validation_wrapper.log')
shutil.copyfile(qa/'compile_console.txt',validation/'compile_console.txt')
(root/'records/validation_report.md').write_text(f'''# Pre-context validation report

Completed: {stamp()}.

- All 31 actual supplied scan pages were read in order, using each whole image and its two supplied halves; a separate visual audit of all 31 pages was logged before this report.
- The prompt's later reference to 49 pages conflicts with its opening count and the archive contents: 31 distinct scan numbers and 93 supplied images are present, and all 31 are included.
- All {len(inventory)} inventory entries have `transcribed=yes`; all required scan numbers occur once in the combined fragment and have individual files.
- The notation table and doubt list were rebuilt from the final page texts: 324 `unsure` occurrences and five `illegible` occurrences, the latter confined to physically obscured prose (approximately ten words), not mathematics.
- All 31 pages compile under pdfLaTeX with AMS mathematics, TikZ and tikz-cd. No LaTeX error, overfull box or package warning appears in the final log.
- The compilation fixture is a syntax and diagram placement check, not a proposed edition: it uses a deliberately large page, color for insertion/deletion state, identity definitions for underline commands, and displays the full contents of uncertainty macros. The delivered transcription is the preamble-free fragment; the fixture is retained separately as a record.
- A local TeX format was built because the installed TeX distribution had no usable format cache; font search paths were supplied explicitly. The fixture and shell script document the environment. Generated QA PDFs, temporary image crops and the TeX format cache are excluded from deliverables.
- Rendered checks of the large table (036), boxed comparison (041), derived-Picard sketch (043), and rigidity diagram (052) caught and resolved placement issues before freezing. These checks supplement, rather than replace, the page-by-page image audits.
- No OCR was used. No context content was read before this report. No helper agent was used.

The source's unfinished formulas, headless strokes, anomalous letters, duplicate labels and repeated formula are retained. Successful compilation does not eliminate palaeographic uncertainty; the doubt table identifies the least secure readings.
''')
with (root/'records/precontext_observations.md').open('a') as f:
 f.write('''\n## Corrections from the completed pre-context audit and integration\n\nThese supersede provisional readings above without deleting the history. Scan005 has primary subscript eta rather than s at the kernel-dimension question. Scan007 has primary `l’indép.` (alternative `l’insép.`), so an inseparability interpretation is not warranted. Scan039 retains tau/2 uncertainty while scan040 gives tau more clearly. Scan041 now integrates the enclosure with its formula; scan043 positions the cancelled R Gamma fragment, double stroke and exclamation mark at their source locations. Scan036 now integrates its two-row brace and vertical marginal title with the table. The repeated oval at the second xi membership in scan034 was removed because only the first occurrence is circled. Scan048 continues on050, not049. Scan052 has the lower torsor argument B/A uncertain, a vertical curl `wr`/i uncertain, and one H0 product integrated with the adjacent vertical identifications rather than duplicated.\n''')
freeze_time=stamp()
hashes={str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
(root/'records/frozen_hashes.json').write_text(json.dumps({'frozen_utc':freeze_time,'algorithm':'SHA-256','files':hashes},indent=2)+'\n')
with (root/'progress.log').open('a') as f:
 f.write(f'notation reconciliation and compilation verified {freeze_time}; 31 pages, {len(inventory)} inventory elements, 329 doubt entries\n')
 for p,h in hashes.items():f.write(f'SHA-256 {h} {p}\n')
 f.write(f'transcription frozen {freeze_time}\n')
print('FROZEN',freeze_time,len(files),'hashes',len(inventory),'inventory rows')
