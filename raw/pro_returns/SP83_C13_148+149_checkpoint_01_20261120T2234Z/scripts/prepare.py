from pathlib import Path
import csv, json, shutil
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT/'source'
OUT = ROOT/'result'
PROMPT = (ROOT/'upload/PROMPT(20261120-214818).md').read_text()
pages = sorted(p.stem for p in (SOURCE/'SP83_C13_148+149_scans').glob('*.jpg'))
marks = list(csv.DictReader((SOURCE/'SP83_C13_148+149_texts/MARKS.tsv').open(), delimiter='\t'))
diffs = list(csv.DictReader((SOURCE/'SP83_C13_148+149_C_H_differences.tsv').open(), delimiter='\t'))
guide = PROMPT[PROMPT.index('## The witnesses are drafts'):PROMPT.index('## Method')]
guide += '''
## First reader's assignment and outputs

Read only the single assigned page's packet. Do not browse, use OCR, or consult other page files. The ink is the authority. The original image and both full-resolution halves have been prepared once; view the original once for layout, and each half once line by line. Do not enlarge a whole half. Compare ALL ink against both witnesses including all agreements. Explicitly check the scope of every deletion and insertion. Then create exactly one tight, enlarged crop for each open place and each mandatory place (every C/H DIFFERENT WORD and every C doubt you resolve). A shared crop may include adjacent issues of the same word/formula, but give each distinct issue its evidence. Use Pillow, LANCZOS to a few thousand pixels wide, autocontrast and optional sharpening/rotation. Save crops to result/crops/<page>_<place>.png and record ORIGINAL pixel boxes. View every crop you cite. Do not compile TeX.

Write your proposed whole diplomatic page to proposed/<page>.tex, using C's macros and only standard LaTeX/TikZ additions. The main reader, not you, writes the final pages/. Preserve legible surprises, uncertainties, spelling and abbreviations. Every symbol and drawing must be rendered in LaTeX/TikZ, not replaced by a description.

Write proposed/<page>.json with this structure (all prose notes in English; transcribed readings in source language):
{
 "page":"148_scan048", "reader":"reader_a", "lines_read":0,
 "changes":[{"id":"<page>-01", "place":"line ... / display ...", "c":"exact C reading or absent", "h":"exact H reading or absent", "final":"final reading", "diff_c":true, "diff_h":true, "kind":"one permitted collation kind", "error_kind":"one of the ten error-sheet categories", "evidence":"specific visible letters/strokes, identifying what is clear and what is not", "crop":"crops/<page>_...png", "box":[0,0,0,0], "confidence":"high|medium|low", "marked_in_h":false, "consequential":false}],
 "decisions":[{"id":"M....", "decision":"first|alternative|other|undecided", "reading":"exact final reading including retained unsure macro", "evidence":"specific ink", "crop":"crops/..png or page if undecided", "box":[0,0,0,0], "confidence":"high|medium|low"}],
 "doubts":[{"place":"...", "reading":"...", "alternatives":"...", "confidence":"medium|low", "reason":"..."}],
 "inventory":[{"element":"E01", "sheet_kind":"text|reused_typed|typescript|letter|list|cancelled_draft|cover", "hand":"his hand|typewriter|print|another hand", "kind":"text|display|diagram|drawing|margin note|insertion|deletion", "position":"...", "first_words_or_objects":"...", "transcribed":"yes"}],
 "notes":[{"id":"<page>-N01", "text":"what it states/computes/asks, mathematical reading reasons, slips, dates etc."}],
 "check_events":[{"statement_id":"...", "type":"targeted proof check|independent re-proof|computation or formal certificate|used and rechecked in this run|carried as background without fault found|refuted, with the refined statement id", "outcome":"what actually happened; mere transcription is not a proof check"}],
 "notation":[{"sign":"...", "meaning_or_form":"...", "places":"...", "universality":"...", "witness_errors":"..."}],
 "abbreviations":[{"form":"...", "expansion":"..."}],
 "second_boxes":[{"box":"B01", "kind":"insertion|margin note|struck passage|doubtful formula|handwritten number|handwritten on typescript|different words|low-confidence departure", "x0":0,"y0":0,"x1":0,"y1":0,"reading":"complete verbatim proposed reading of all target ink in this box, in our macros"}]
}

Permitted collation kinds: misread word; misread symbol or index; omission; text not on the page; deletion state (struck given live or live given struck); insertion or placement; abbreviation expanded or spelling modernised; readable ink left as \\ill{}; drawing or diagram; other.

Changes must include every material departure from either witness. Ignore pure macro syntax or editorial H headings/synopses. Certainty-only changes go in decisions/doubts, not the changes counts. Preserve actual macros in excerpts. Need one decision for EVERY supplied MARKS row. Capture implicit uncertainty inside deleted passages even when MARKS does not include it. A resolved C mark always needs an actually viewed crop and specific deciding strokes. Do not resolve a deleted unsure word unless every letter is clear.

The second_boxes list must cover EVERY insertion, margin note, struck passage, entire formula with a C or proposed doubt, handwritten number (including dates, item numbers and numeric indices, which may be covered by a whole formula box), handwritten word on a typescript, differing C/H word, and non-high-confidence departure from C. A box should delimit a complete readable unit. The reading must cover exactly its target ink and include cancellation/insertion macros when visible. These boxes will be independently read by another reader with no text/witness access. Do not make second-pass crops now.

Count physical text/formula lines actually read. Return a concise summary and the file paths. Do not claim main-reader approval or completion. Keep all outputs confined to your assigned page. If you need extra time, continue; do not omit hard material to save time.
'''
notation = '# Working notation table\n\nNo habits have yet been established from these pages. Read symbols from the assigned ink; propose page-grounded entries.\n'
if (OUT/'notation_working.md').exists():
    notation = (OUT/'notation_working.md').read_text()
else:
    (OUT/'notation_working.md').write_text(notation)
if not (OUT/'SP83_C13_148+149_hand_log.md').exists(): (OUT/'SP83_C13_148+149_hand_log.md').write_text('# Hand log\n\nStarted before the first page. Entries will be added only from observed ink.\n')
if not (OUT/'progress.log').exists(): (OUT/'progress.log').write_text('2026-11-20 21:49:02 UTC\nRun started; latest attached prompt PROMPT(20261120-214818).md governs.\n')
(OUT/'page_order.txt').write_text('\n'.join(pages)+'\n')
(OUT/'scripts/reader_guide.md').write_text(guide)
for page in pages:
    packet = ROOT/'packets'/page
    packet.mkdir(exist_ok=True, parents=True)
    for src,dst in [(SOURCE/f'SP83_C13_148+149_texts/pages/{page}.tex','C.tex'),(SOURCE/f'SP83_C13_148+149_texts/hua/hua_{page}.tex','H.tex'),(SOURCE/'SP83_C13_148+149_texts/PREAMBLE.tex','PREAMBLE.tex')]:
        shutil.copyfile(src,packet/dst)
    (packet/'guide.md').write_text(guide)
    (packet/'notation.md').write_text(notation)
    cote,scan=page.split('_scan')
    for name,rows,fieldnames in [('MARKS.tsv',[r for r in marks if r['cote']==cote and int(r['scan'])==int(scan)],marks[0].keys()),('differences.tsv',[r for r in diffs if r['page']==page],diffs[0].keys())]:
        with (packet/name).open('w') as f:
            w=csv.DictWriter(f,fieldnames=fieldnames,delimiter='\t');w.writeheader();w.writerows(rows)
    imgpath=SOURCE/f'SP83_C13_148+149_scans/{page}.jpg'
    image=Image.open(imgpath);w,h=image.size
    if w>h:
        boxes=[(0,0,round(w*.55),h),(round(w*.45),0,w,h)]
    else:
        boxes=[(0,0,w,round(h*.55)),(0,round(h*.45),w,h)]
    halves=[]
    for i,box in enumerate(boxes,1):
        path=ROOT/'halves'/f'{page}_half{i}.png'
        path.parent.mkdir(exist_ok=True, parents=True)
        if not path.exists(): image.crop(box).save(path)
        halves.append({'path':str(path),'box':box})
    (packet/'images.json').write_text(json.dumps({'original':str(imgpath),'size':[w,h],'halves':halves},indent=2))
print('Prepared',len(pages),'page packets; first:',pages[:3])
