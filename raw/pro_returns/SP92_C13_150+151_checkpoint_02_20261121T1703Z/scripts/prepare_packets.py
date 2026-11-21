from pathlib import Path
from PIL import Image
import csv,json

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'SP92_C13_150+151_work'
SRC=ROOT/'source'
TX=SRC/'SP92_C13_150+151_texts'
PK=ROOT/'reading_packets'
PK.mkdir(exist_ok=True)
prompt=(ROOT/'upload/PROMPT(20261121-153212).md').read_text()
errors=prompt[prompt.index('## The errors that recur'):prompt.index('## Method')]
diffs=list(csv.DictReader((SRC/'SP92_C13_150+151_C_H_differences.tsv').open(),delimiter='\t',quoting=csv.QUOTE_NONE))
for i,r in enumerate(diffs,1):r['diff_id']=f'D{i:04}'
marks=list(csv.DictReader((TX/'MARKS.tsv').open(),delimiter='\t'))
common=r'''# Page-reader task
Read ONLY the assigned page and its page packet. Do not inspect other pages, other witnesses, other readers' output, root notes, or the global difference list. No OCR, text recognition, browser or external research. Use the image tool yourself. No TeX compilation. Do not delegate further: all three reader slots are in use.

Workflow: view the whole page once for layout; then view its two supplied native-resolution overlapping halves once each, read every line against C and H. Independently inspect agreed text, all math, numbering, abbreviations, accents, deletions, insertions, margins and drawings. Explicitly check every C deletion/insertion's bounds and attachment. Start with the C/H differences but do not stop there. Every different WORD reading gets a tight enlarged crop, as does every C doubt you resolve. Also crop any unresolved reading, crowded/struck/slanted passage or decisive small symbol. Make each needed crop once with Pillow LANCZOS to roughly 2200-3000 px across, autocontrast and sharpen if helpful. Save it under OUT/crops/<page>_<place>.png; log ORIGINAL image pixel box. You may use the helper `scripts/make_crop.py`. Inspect every crop with view_image. Never infer strokes from witness agreement. Do not add text the mathematics wants. For unresolved ink retain narrow uncertainty; no guessed certainty. Do not silently expand short forms or normalize spelling. Running text is LaTeX, never a drawing. Genuine diagrams/drawings must be fully set in TikZ/tikz-cd.

Output the complete candidate page, using the provided preamble's conventions only, to OUT/records/<page>.tex. This is a candidate: root will inspect all changes and then write pages/. Do not edit the common logs or notation table.

Write OUT/records/<page>.json containing these keys:
- page, cote, scan, reader, line_count (actual manuscript lines), half_review (brief truthful coverage note), deletion_insertion_review (every such C item and exact state/attachment).
- changes: one object per actual reading/place differing from either witness (same-reading macro differences and editorial H notes are excluded). Keys: id (local e.g. C01), place, C, H (null if absent witness page), final, evidence (specific visible letters/strokes, not plausibility), crop (relative crops/... filename), box ([x0,y0,x1,y1]), confidence (high/medium/low), kind (allowed collation kind), error_kind (one of 1 symbols/indices;2 words;3 omissions;4 drawing/diagram;5 readable left illegible;6 insertion placement;7 struck state;8 abbreviation/spelling;9 not on page;10 other), against_C (boolean), against_H (boolean), consequential (boolean). Every changed reading needs exact C/H text and evidence. For a change settled on a half, crop/box can be null; root will crop if needed. Different-word readings always need crops. Adding uncertainty alone is only a doubts entry.
- diff_coverage: one entry for EVERY supplied diff_id: diff_id, classification (reading / macro-only / editorial-only / alignment-only), change_ids (list), reason. Differences list may split a real place into several rows; map all to the actual change(s).
- decisions: one per supplied mark in its supplied order. Keys: id,cote,scan,decision (first/alternative/other/undecided),reading,ink,crop,box,confidence. C's MARKS excludes some struck doubts, but those too must be reviewed. Any resolved mark MUST have its crop.
- inventory: one per page element, keys sheet_kind (text/reused_typed/typescript/letter/list/cancelled_draft/cover),hand,element,kind (text/display/diagram/drawing/margin note/insertion/deletion),position,first_words_or_objects,transcribed ('yes'). Include every block, display, diagram, drawing, margin note, insertion and deletion top to bottom.
- notes (English Markdown): what page states/asks; every math-triggered rereading with readings and locations; author's explicit doubts/slips; title/date/page counts. Do not claim proof verification merely from transcription.
- check_events: [] unless an actual mathematical use/check happens; then statement_id,date,who,type,outcome. Permitted types: targeted proof check / independent re-proof / computation or formal certificate / used and rechecked in this run / carried as background without fault found / refuted, with refined statement id. Be exact about what occurred.
- notation: list of {sign,reading,evidence}; hand_log: list of {habit,places,scope,witness_errors}; abbreviations: list of {form,expansion}; doubts: list of {place,reading,alternatives,confidence,reason}.
- second_boxes: one object per hard region for later BLIND independent reread: box (B01 etc),kind,x0,y0,x1,y1,reading (candidate in our LaTeX conventions). Must cover EVERY insertion, margin note, struck passage, whole formula with a C or final doubt, EVERY handwritten number (including page/formula labels and mathematical digits), EVERY handwritten word on a typescript, EVERY C/H different-word place, and every below-high-confidence departure from C. Use practical distinct regions; can combine nearby related targets and label kinds. Coordinates original page. Readings exact and region-scoped, no expected prose. The blind reader will not see this reading.

Save work as you go; no false claims of completeness. In final message give output paths, count changes/crops, unresolved issues and notation discoveries. Root will handle publishing and final assembly. Do not ask user anything. Follow the full error sheet and conventions below.
'''
for page in (OUT/'page_order.txt').read_text().splitlines():
    d=PK/page;d.mkdir(exist_ok=True)
    im=Image.open(SRC/'SP92_C13_150+151_scans'/f'{page}.jpg')
    w,h=im.size
    if h>=w:
        bounds=[(0,0,w,int(h*.55)),(0,int(h*.45),w,h)]
    else:
        bounds=[(0,0,int(w*.55),h),(int(w*.45),0,w,h)]
    for i,b in enumerate(bounds,1):
        p=d/f'half{i}.png'
        if not p.exists():im.crop(b).save(p)
    cote,scan=page.split('_scan')
    data={'page':page,'image':str(SRC/'SP92_C13_150+151_scans'/f'{page}.jpg'),'size':[w,h],'halves':[str(d/'half1.png'),str(d/'half2.png')],'half_boxes':bounds,'witness_C':(TX/'pages'/f'{page}.tex').read_text(),'witness_H':(TX/'hua'/f'hua_{page}.tex').read_text() if (TX/'hua'/f'hua_{page}.tex').exists() else None,'differences':[r for r in diffs if r['page']==page],'marks':[r for r in marks if r['cote']==cote and int(r['scan'])==int(scan)],'preamble':(TX/'PREAMBLE.tex').read_text()}
    (d/'packet.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
    (d/'instructions.md').write_text(common.replace('OUT/',str(OUT)+'/')+'\n'+errors)
    (d/'notation.md').write_text((OUT/'notation.md').read_text())
print('Prepared',len(list(PK.glob('*/packet.json'))),'isolated page packets and native halves.')
