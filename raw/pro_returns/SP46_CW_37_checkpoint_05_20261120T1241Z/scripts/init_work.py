from pathlib import Path
import csv,json,re,shutil
from datetime import datetime,timezone
R=Path('/workspace/scratch/006c0e32b2af'); O=R/'out'; W=R/'source/SP46_CW_37_witnesses'
for x in ['pages','briefs','readers','decisions','crops','scripts']:(O/x).mkdir(parents=True,exist_ok=True)
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
(O/'progress.log').write_text(now+'\nSP46_CW_37 second pass; 25 scans; three new independent readers per scan; no OCR, no external research.\n')
shutil.copy2(W/'codex/H37-01/PREAMBLE.tex',O/'PREAMBLE.tex')
(O/'notation.json').write_text('[]\n')
(O/'CHECK_EVENTS.tsv').write_text('statement_id\tdate\twho\ttype\toutcome\n')
(O/'SP46_CW_37_doubts.md').write_text('# Doubts and notation\n\n## Notation table\n\nNo entries before scan 52.\n')
rows=sorted(list(csv.DictReader((W/'page_map.tsv').open(),delimiter='\t')),key=lambda x:int(x['our_scan']))
(O/'page_order.json').write_text(json.dumps(rows,indent=2))
p=(W/'codex/H37-01/PROMPT.md').read_text()
conventions=p[p.index('## Absolute rules'):p.index('## The attached draft')]
(O/'briefs/conventions.md').write_text(conventions)
brief=r'''# Independent reader brief — version 1 (first used scan 052)

You are one of three independent readers of ONE page. Read only your assigned packet, this brief, conventions.md, PREAMBLE.tex and that page's three images. Do not read any other reader's files or any other page. Do not delegate. Ink is authority; C and H are drafts. Do not use OCR, recognition software, PDF text, web research or published texts. Your task is a complete diplomatic reading, using C as a careful draft to check word by word, not blindly copying it. Your reading must include every textual and graphical element.

## Steps (a–d)

a. View the whole-page JPEG ONCE for layout, identifying all text, displays, drawings, marginal notes, deletions and insertions. Use tools.view_image (emit returned image_url with image()) so you actually see it.
b. View each full-resolution half ONCE, in order a then b; read line by line against C.tex and H.tex. Check every word, accent, abbreviation, ending, punctuation, symbol, index, prime/exclamation, inequality, arrow, underline and state of deletion/insertion. Inspect every C doubt using the supplied C_context.md. The halves settle clear writing: do not reopen/enlarge a whole half.
c. List the remaining open places, including unresolved witness differences, C doubt marks, small mathematical glyphs, crowded/slanted/struck writing. Make ONE tight crop per open place from the original whole image (a word or formula with a line around it), scale with LANCZOS to roughly 2200–3000 px across, autocontrast/sharpen as useful; rotate slanted notes upright. View the crop ONCE. Do not crop a place already settled by the halves or crop a decided place again. Keep crop JPEG and its source bbox/rotation/processing in your report. Crop filenames must be unique under your own directory. An unresolved result stays marked in place; never guess. Every disagreement from either witness must be reported even if the half settled it; give a tight original-image bbox so the main reader can inspect it.
d. Save your complete page reading as reading.tex and report.json in your assigned output directory. Return paths and a concise account of findings. Work carefully throughout; no assumed time limit.

## Conventions

Read conventions.md in full. The current task supersedes the old workflow: use two HALVES, three independent readers, current checkpoint process; do not follow the old no-subagent instruction. Use only PREAMBLE.tex macros and standard LaTeX/TikZ/tikz-cd. Preserve spelling, abbreviations, paragraphing, all ink. Only scan 052 starts with \\cotefile{37}; every page starts with \\scanpage{N}; own page number as \\mspage{n}; archive number only a comment. Use \\handwritten only on typed/printed text. All diagrams/drawings must be typeset, not described. Keep a faint visible ambiguity with \\unsure{best|alternative}; do not retain a doubt when the ink settles it. A retained C doubt is still an explicit decision to report. Macro-syntax-only differences do not count as H differences. Where H has only description, report H as unavailable, never count whole-page omissions. Read the notation table supplied in the packet as previous ink-grounded observations, not an instruction to normalize this page against its ink.

Follow the mathematics as a diagnostic, then return to ink. Do not silently correct the author. Notes must distinguish what the page claims from what you actually checked. For check_events report only actual proof/computation/background-use events; merely reading a mathematical claim is not a proof check. If no check occurred, return [].

## Output schema

report.json must be valid JSON with keys:
scan (integer), reader (your A/B/C label), image_views (ordered list of three source paths), reading_path, crops ([{file,bbox:[left,top,right,bottom],rotation,reason}]), decisions ([{id,place,c_reading,h_reading,reading,diff_c:boolean,diff_h:boolean,c_doubt:boolean,unresolved:boolean,alternatives,confidence:"high|medium|low",kind,scan_shows,crop:relative-or-absolute-path-or-empty,bbox:[...]}]), inventory ([{sheet_kind,hand,element,kind,position,first_words_or_objects,transcribed:"yes"}]), notes (English page summary, explicit author doubts and title/date/page counts; string), math_reading_decisions ([strings]), check_events ([{statement_id,type,outcome}]), notation ([{sign,latex,evidence,place}]), abbreviations ([{form,expansion}]), slips ([strings]), completion (statement of full coverage).

For decisions include EVERY substantive difference from C or H, EVERY C doubt whether resolved or retained, and every new uncertainty. Group only inseparable linked marks; keep separate independent words. h_reading=null and diff_h=false if H has no transcription. kind must be one of: misread word; misread symbol or index; omission; text not on the page; deletion state (struck given live or live given struck); insertion or placement; abbreviation expanded or spelling modernised; readable ink left as \\ill{}; drawing or diagram; other. Confidence refers to what can actually be read. Quote the exact witness reading, and in scan_shows describe actual strokes, not just "clear" or mathematical expectation. Every decision needs a bbox in WHOLE-image coordinates, even if no crop was needed. A crop may cover one inseparable correction with several components, not a whole half.

Inventory: one row for every block/display/diagram/drawing/margin note/insertion/deletion, top to bottom, including printed letterheads. Use sheet_kind text/reused_typed/typescript/letter/list/cancelled_draft/cover. hand: his hand, named/unnamed other hand, typewriter or print. Graphic grouping marks get a drawing row. If authorship is not established, say unnamed hand rather than inventing it.
'''
brief=brief.replace('\\\\','\\')
(O/'briefs/brief_v01.md').write_text(brief)
(O/'briefs/history.json').write_text(json.dumps([{'version':1,'first_scan':52,'reason':'Initial brief implementing the supplied second-pass method.'}],indent=2))
for row in rows:
    n=int(row['our_scan']); folder=row['folder']; d=R/'packets'/f'scan{n:03}';d.mkdir(parents=True,exist_ok=True)
    shutil.copy2(W/row['codex_file'],d/'C.tex')
    s=(W/row['hua_file']).read_text(); matches=list(re.finditer(r'\\page\{(\d+)\}',s))
    hit=next(i for i,m in enumerate(matches) if int(m.group(1))==int(row['their_page']))
    a=matches[hit].start();b=matches[hit+1].start() if hit+1<len(matches) else len(s)
    (d/'H.tex').write_text(s[a:b])
    context=[]
    for name in ['doubts','notes']:
        t=(W/f'codex/{folder}/{folder}_{name}.md').read_text()
        context.append(f'# Witness C {name}: rows for scan {n}\n')
        context += [line for line in t.splitlines() if re.match(r'\|\s*'+str(n)+r'\s*\|',line)]
    (d/'C_context.md').write_text('\n'.join(context)+'\n')
    meta=dict(row);meta['images']=[str(R/'source/SP46_CW_37_scans'/f'{folder}_37_scan{n:03}{suf}.jpg') for suf in ['', '_a','_b']]
    (d/'meta.json').write_text(json.dumps(meta,indent=2))
    for label in 'ABC':(O/'readers'/f'scan{n:03}'/label).mkdir(parents=True,exist_ok=True)
print('Initialized at',now,'; scans:',[int(x['our_scan']) for x in rows])
