from pathlib import Path
from datetime import datetime, timezone
import json
out=Path('/workspace/scratch/94548b74fbe0/out/readers/014/B')
tex=r'''\scanpage{14}
\unsure{décompositions} \inserted{et découpages} $n$-aires d'\unsure{espaces} topologiques

% archive sheet number: 13
'''
(out/'reading.tex').write_text(tex)
report={
 'scan':14,
 'reader':'B',
 'start_utc':'2026-11-20 14:55:27 UTC',
 'end_utc':None,
 'full_image_viewed':True,
 'halves_viewed':True,
 'complete_visual_read':True,
 'differences':[
  {
   'id':'B014-01',
   'location':'Upper-right title, first main word; C_doubts.txt / Doubtful readings / first main word',
   'C':r'\unsure{décompositions}',
   'H':None,
   'reading':r'\unsure{décompositions}',
   'evidence':'The enlargement shows the initial looped d, raised curved acute over the following e, open c/o forms, a compressed low run, the deep p descender, a tall internal ascender and the final low joined strokes. These support décompositions, but the compressed interior does not independently separate every letter. No further word candidate is supported.',
   'confidence':'medium',
   'kind':'other',
   'diff_C':False,
   'diff_H':False,
   'C_doubt_status':'retained',
   'readers_crop':'01_first_word.png',
   'bbox':{'image':'J81-02_81_scan014.jpg','origin':'upper-left','xyxy':[860,83,1292,195]},
   'source_doubt_row':'C_doubts.txt, Doubtful readings, row 1: first main word'
  },
  {
   'id':'B014-02',
   'location':"Upper-right title, second main line, word immediately after d'; C_doubts.txt / Doubtful readings / after d'",
   'C':r'\unsure{espaces}',
   'H':None,
   'reading':r'\unsure{espaces}',
   'evidence':'A short initial low stroke and wave precede the long descending p-shaped stroke; the following short open/rounded joins support the remaining aces. The very compressed low joins leave the word qualified after enlargement. The preceding d and detached apostrophe are readable independently.',
   'confidence':'medium',
   'kind':'other',
   'diff_C':False,
   'diff_H':False,
   'C_doubt_status':'retained',
   'readers_crop':'02_second_line.png',
   'bbox':{'image':'J81-02_81_scan014.jpg','origin':'upper-left','xyxy':[995,195,1175,279]},
   'source_doubt_row':"C_doubts.txt, Doubtful readings, row 2: after d'"
  }
 ],
 'doubts':[
  {'location':'First main title word, full scan x=880–1268, y=96–189','reading':'décompositions','alternatives':[],'confidence':'medium','reason':'Several internal connected strokes remain compressed; same C candidate retained after the one enlarged crop.','crop':'01_first_word.png'},
  {'location':"Second main title line, after d', full scan x=1000–1168, y=201–274",'reading':'espaces','alternatives':[],'confidence':'medium','reason':'The deep p is visible, but the low adjoining joins do not independently isolate every letter; same C candidate retained.','crop':'02_second_line.png'}
 ],
 'inventory':[
  {'sheet_kind':'cover','hand':'his hand','element':'014.B.01','kind':'insertion','position':'Upper right, above the first main title line; guide bends down to the gap before n-aires','first_words_or_objects':'et découpages','transcribed':'yes','provenance':'C inventory 014.02; independently checked on half a and crop 03.','source_component':'reading.tex: \\inserted{et découpages}; conventional insertion representation attaches at the observed gap.'},
  {'sheet_kind':'cover','hand':'his hand','element':'014.B.02','kind':'text','position':'Upper right, two main handwritten lines','first_words_or_objects':"décompositions [qualified] n-aires d'espaces [qualified] topologiques",'transcribed':'yes','provenance':'C inventory 014.01; both original local word doubts retained.','source_component':"reading.tex: main title sentence; no physical-line-wrap command added."},
  {'sheet_kind':'cover','hand':'another unnamed hand','element':'014.B.03','kind':'text','position':'Lower left, close to bottom paper edge, full scan x=77–128, y=2408–2451','first_words_or_objects':'Archive sheet number 13','transcribed':'yes','provenance':'Archive numeral is present in C.tex as a comment but absent from C_inventory.json. Numeral read directly on half b.','source_component':'reading.tex: % archive sheet number: 13'}
 ],
 'notes':{
  'page_content':'A near-empty title sheet with a two-line handwritten title at upper right, an insertion above it, and archive number 13 at the lower-left foot.',
  'author_uncertainty':{'exact_words':None,'observation':'No written expression of authorial uncertainty identified.'},
  'title_date_page_counts':{'title':"décompositions ⟨et découpages⟩ n-aires d'espaces topologiques",'qualified_words':['décompositions','espaces'],'date':None,'manuscript_page_number':None,'archive_number':'13','terminal_punctuation':'No terminal punctuation read after topologiques.'},
  'mathematics_led_reading_decisions':'None. The n and its hyphen were read from ink. No mathematical correspondence, theorem, repair, or computation was used.',
  'H_status':'metadata hua_has=nothing; H.tex is empty. All H fields are null and all diff_H flags false.',
  'small_surface_observations':[
   {'bbox':[940,220,950,232],'crop':'02_second_line.png','description':"A tiny gray fleck lies left of the second-line d. It does not yield a supported letter or word candidate. Its hand, role, and surface origin remain undetermined; no supplied character is transcribed."},
   {'bbox':[1308,160,1324,174],'crop':'03_insertion_guide.png','description':'A tiny pale detached patch lies below the n. Its hand, role, and surface origin remain undetermined; no supplied character is transcribed.'}
  ],
  'source_component_map':[
   {'component':'main title text','source':'C.tex title text','final_source':'reading.tex line 2','status':'Retained after direct visual reading; two original word qualifications retained.'},
   {'component':'upper insertion and attachment','source':'C.tex \\inserted{et découpages}','final_source':'reading.tex line 2, immediately before $n$-aires','status':'Retained; the guide is represented by the conventional insertion macro at its observed attachment. No separate graphical variant proposed.'},
   {'component':'archive numeral','source':'C.tex archive-number comment','final_source':'reading.tex line 4','status':'13 retained; added to the updated inventory.'}
  ],
  'graphical_variants':[],
  'original_graphical_paths':'C.tex contains no TikZ paths or drawing components; no original source path was removed.',
  'image_view_order':['whole scan once','half a once','half b once','01_first_word.png once','02_second_line.png once','03_insertion_guide.png once'],
  'half_dimensions':{'full':[1760,2470],'a':[1760,1315],'b':[1760,1315]},
  'coordinates':'All report crop/decision boxes refer to the full scan with origin at upper left. The lower half begins at full y=1155, derived from full height 2470 minus half height 1315.',
  'crop_boundary_notes':'Crop 01 includes only the start of the next-line tall t at its lower edge; crop 02 includes a small terminal remnant of the first-line p at its top edge. Neither remnant is a separately supplied mark. The target words, lower descenders, and the insertion guide are fully contained in their respective crops.',
  'validation':'Structural source checks only. No OCR, external source, compiler, renderer, format builder, installation, or mathematical proof check was used.'
 },
 'notation':[
  {'location':'First main title line, right of insertion attachment; crop 03, full bbox [1300,113,1480,155]','sign':'n followed by a short horizontal hyphen','latex':'$n$-aires','evidence':'One low rounded n-shaped form precedes an independently visible short horizontal dash; the following letters read aires.'},
  {'location':'Upper inserted phrase; crop 03, full bbox [1160,40,1505,165]','sign':'curved insertion guide','latex':r'\inserted{et découpages}','evidence':'The long run beneath the inserted phrase turns downward at its left end to the gap before n. The text has readable et, looped d, raised acute and following découpages strokes.'},
  {'location':'Beginning of second main title line; crop 02, full bbox [958,194,1014,242]','sign':'detached apostrophe after d','latex':"d'",'evidence':'Short raised oblique following the tall d; retained without a space before the following word.'},
  {'location':'Lower-left foot; half b x=77–128, y=1253–1296','sign':'archive numeral 13','latex':'% archive sheet number: 13','evidence':'Upright/slant 1 followed by two-bow 3; comment convention retained.'}
 ],
 'check_events':[],
 'crops':[
  {'path':'01_first_word.png','bbox':{'image':'J81-02_81_scan014.jpg','origin':'upper-left','xyxy':[860,83,1292,195]},'rotation':0,'purpose':'Original C doubt: first main title word.','enlarged_size':[3000,778]},
  {'path':'02_second_line.png','bbox':{'image':'J81-02_81_scan014.jpg','origin':'upper-left','xyxy':[925,180,1565,305]},'rotation':0,'purpose':"Original C doubt after d', with the complete second title line and its endpoint as context.",'enlarged_size':[3200,625]},
  {'path':'03_insertion_guide.png','bbox':{'image':'J81-02_81_scan014.jpg','origin':'upper-left','xyxy':[1138,28,1515,175]},'rotation':0,'purpose':'Insertion phrase, complete hooked guide and n-aires attachment/letter details.','enlarged_size':[3000,1170]}
 ],
 'brief_feedback':'The brief supplies a conventional insertion macro and also requires preserved marks. Here the single hooked guide is recorded as an attachment and described with exact crop coordinates; no independent emphasis or cancellation is inferred from the run beneath the insertion. No other convention gap encountered.'
}
(out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
md=r'''# Scan 014 — independent reader B

Start: **2026-11-20 14:55:27 UTC**, obtained before reading the packet. H is empty (`hua_has=nothing`). Only scan014 and its supplied packet were inspected.

## Visual reading audit

| Physical line or element | Direct reading and state | Decision / evidence |
|---|---|---|
| Whole sheet | Title at upper right; extensive blank field; archive numeral at lower left | Whole image viewed once for layout. No date or manuscript page number read. |
| Upper addition | `et découpages` | Readable; acute retained. Crop **03_insertion_guide.png**, full bbox **[1138,28,1515,175]**, preserves the complete guide. Its left end bends down to the gap before n-aires. The insertion macro remains attached there. |
| First main line, first word | `\unsure{décompositions}` | **C doubt retained**, medium confidence. Initial d, curved acute, c/o, descending p and tall internal stroke are visible; compressed intervening joins leave the full word qualified. Crop **01_first_word.png**, full bbox **[860,83,1292,195]**. |
| First main line, end | `$n$-aires` | Readable n, separate short hyphen, and aires. Checked on half a and crop 03. No exponent or index supplied. |
| Second main line, opening | `d'\unsure{espaces}` | d and detached apostrophe readable. **C espaces doubt retained**, medium confidence: long p descender and surrounding low joins support the word but do not independently isolate every letter. Crop **02_second_line.png**, full bbox **[925,180,1565,305]**; local word bbox **[995,195,1175,279]**. |
| Second main line, end | `topologiques` | Readable t, descending p, tall l, long lower g return and q descender with compressed final joins. No terminal punctuation read. Crop 02 contains the full endpoint. |
| Lower half | Archive `13` at foot | Half b read once. Full bbox **[77,2408,128,2451]**, or half-b bbox **[77,1253,128,1296]**. Preserved as the required comment, and added to the inventory. |

Ordinary wrapping of the two main title lines is joined in the transcription. The insertion remains marked and attached before n-aires. No deletion, independent margin note, displayed formula, diagram, or separate drawing was identified. The apparent rule beneath the upper addition is the continuous insertion guide whose left end descends to the insertion gap.

## C doubt map and witness changes

- **C source doubtful row 1**, “first main word”: `décompositions` retained under `\unsure`; report **B014-01**, `diff_C=false`.
- **C source doubtful row 2**, “after d'”: `espaces` retained under `\unsure`; report **B014-02**, `diff_C=false`.
- The two notation-table rows are notation entries, not additional source doubts.
- No C textual reading change is proposed. H supplies no text; no H collation row or claim of an H omission is made.
- C's archive-number comment is already correct; its omission from C's inventory is repaired in the updated inventory.

## Small observed patches

Crop 02 shows a tiny gray fleck left of d at full bbox **[940,220,950,232]**. Crop 03 shows a tiny pale detached patch below n at **[1308,160,1324,174]**. Neither yields a supported letter or word candidate. Their hand, role and surface origin remain undetermined. They are documented for adjudication without a supplied character. The bits touching crop 01's lower edge and crop 02's upper edge belong to the neighboring title lines already transcribed.

## Final source-component map

| Visible component | Final source | Status |
|---|---|---|
| Main title | `reading.tex`, line 2 | All words retained after viewing; both C word doubts retained. |
| Upper insertion text and attachment | `\inserted{et découpages}`, immediately before `$n$-aires` | Conventional insertion representation; the guide's attachment is recorded by crop 03. No separate graphical variant proposed. |
| Archive numeral | `% archive sheet number: 13` | Read directly and inventoried. |

C has no TikZ paths. No source drawing path was removed or substituted; the final graphical-variant map is empty.

## Method and validation

Whole image, half a and half b were each viewed once. One tight crop was made for each of the two original doubtful words, plus one for the insertion guide and adjacent title-ending detail. Each resulting crop was viewed once, with no recrop. Crops use PIL LANCZOS enlargement, autocontrast and light unsharp masking; `make_crops.py` records exact source boxes.

All decisions use visible ink. No mathematical check was performed (`check_events=[]`). No OCR, internet, external source, other reader file, other-page image, compiler, renderer, format builder or installation was used. Structural source checks and agreement of the final reading/report were performed before return.
'''
(out/'reading.md').write_text(md)
print('Wrote reading.tex, reading.md, report.json')
