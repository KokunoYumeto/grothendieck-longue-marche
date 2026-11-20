from pathlib import Path
from datetime import datetime, timezone
import json

out = Path('/workspace/scratch/94548b74fbe0/out/readers/014/C')
reading = r'''\scanpage{14}
\unsure{décompositions} \inserted{et découpages} $n$-aires d'\unsure{espaces} topologiques

% archive sheet number: 13
'''
(out/'reading.tex').write_text(reading, encoding='utf-8')
end = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
report = {
    'scan':14, 'reader':'C', 'start_utc':'2026-11-20 14:55:36 UTC', 'end_utc':end,
    'full_image_viewed':True, 'halves_viewed':True, 'complete_visual_read':True,
    'image_view_record':{
        'whole':'J81-02_81_scan014.jpg viewed once for layout',
        'a':'J81-02_81_scan014_a.jpg viewed once, all writing and field examined',
        'b':'J81-02_81_scan014_b.jpg viewed once, field and foot number examined',
        'dimensions':{'full':[1760,2470],'a':[1760,1315],'b':[1760,1315]},
        'coordinate_origin':'All boxes in this report use original full-scan pixels, top-left origin; x increases right and y increases down.',
        'half_offsets':{'a':[0,0],'b':[0,1155]},
        'timing_note':'UTC start was returned in the initial batch alongside packet and brief reads, before any image viewing.'
    },
    'differences':[
        {
            'id':'014-C-D01','location':'first main title word, full scan [881,96,1268,188]',
            'C':r'\unsure{décompositions}','H':None,'reading':r'\unsure{décompositions}',
            'evidence':'The tall looped initial d, raised curved accent, low co-like opening, long descending p, later tall loop and terminal low waves support the supplied candidate. The long compressed medial run and several joins remain insufficiently separated to remove the qualification.',
            'confidence':'medium','kind':'other','diff_C':False,'diff_H':False,
            'C_doubt_status':'retained','C_source_row':'C_doubts.txt / Doubtful readings / first main word',
            'readers_crop':'01_first_word.png','bbox':[881,96,1268,188]
        },
        {
            'id':'014-C-D02','location':"second main title line, word after d', full scan [1003,214,1167,274]",
            'C':r'\unsure{espaces}','H':None,'reading':r'\unsure{espaces}',
            'evidence':'The opening low shoulder, long descending p-shaped stroke, following open curved stroke and low final joined waves support espaces. The compact opening and joined interior/ending do not settle all individual letters on this enlargement; no stronger alternative word is visible.',
            'confidence':'medium','kind':'other','diff_C':False,'diff_H':False,
            'C_doubt_status':'retained','C_source_row':"C_doubts.txt / Doubtful readings / after d'",
            'readers_crop':'03_second_line.png','bbox':[1003,214,1167,274]
        }
    ],
    'doubts':[
        {'location':'first main title word','reading':'décompositions','alternatives':[], 'confidence':'medium','reason':'Compressed medial joins remain unresolved; retained original C source doubt 014-C-D01. No additional candidate word is supplied.','crop':'01_first_word.png','bbox':[881,96,1268,188]},
        {'location':"word after d' on second main line",'reading':'espaces','alternatives':[], 'confidence':'medium','reason':'Several low joined strokes remain unresolved; retained original C source doubt 014-C-D02. No additional candidate word is supplied.','crop':'03_second_line.png','bbox':[1003,214,1167,274]}
    ],
    'inventory':[
        {'sheet_kind':'cover','hand':'his hand','element':'014.02','kind':'insertion','position':'upper right, above main title; long curved lead-in ends in the gap before n','first_words_or_objects':'et découpages','transcribed':'yes','provenance':'C_inventory.json 014.02; original hand designation Grothendieck. Wording and guide personally checked in half a and crop 02.','source_component':r'\inserted{et découpages}'},
        {'sheet_kind':'cover','hand':'his hand','element':'014.01','kind':'text','position':'upper right, two physical main lines','first_words_or_objects':"qualified décompositions; n-aires d'qualified espaces topologiques",'transcribed':'yes','provenance':'C_inventory.json 014.01; original hand designation Grothendieck. Both word qualifications retained from C; all remaining title writing personally checked.'},
        {'sheet_kind':'cover','hand':'undetermined hand','element':'014.03','kind':'text','position':'lower left foot, full scan approximately [79,2412,124,2447]','first_words_or_objects':'archive numeral 13','transcribed':'yes','provenance':'Added inventory entry for archive number already present in C.tex. Recorded only as the required source comment.','source_component':'% archive sheet number: 13'}
    ],
    'notes':{
        'page_content':"Short title on otherwise substantially empty cover: qualified décompositions, inserted et découpages, n-aires d'qualified espaces topologiques; archive number 13 at foot.",
        'authors_own_uncertainty':[],'editorial_uncertainty':'The two unsure markers are retained C editorial doubts. No written question mark or authorial uncertainty phrase is present in the title.',
        'title_date_page_counts':'No date or authorial page count observed. Archive numeral 13 is commented, without mspage.',
        'mathematics_led_reading_decisions':[],
        'H_status':'metadata.json says hua_has=nothing; H.tex is empty (0 bytes). H=null and diff_H=false throughout.',
        'punctuation_and_state':"Apostrophe after d and the hyphen in n-aires are retained. No endpoint full stop is supplied. The upper added words and long return to the gap before n are preserved by inserted. No deletion, separate underline, margin prose, diagram or labelled drawing was identified.",
        'new_character_proposals':[],
        'surface_observations':[
            {'bbox':[1537,50,1549,62],'crop':'02_insertion_and_naires.png','observation':'Small isolated dark point above/right of the insertion. No alphabetic candidate or secure punctuation attachment; hand and origin unestablished. Documented for root review; no character supplied.'},
            {'bbox':[1309,161,1323,174],'crop':'02_insertion_and_naires.png','observation':'Faint small point below n. No alphabetic candidate or secure relation to the title; hand and origin unestablished. Documented for root review; no character supplied.'},
            {'bbox':[939,219,952,231],'crop':'03_second_line.png','observation':"Small isolated gray point to the left of d'. No alphabetic candidate or secure punctuation attachment; hand and origin unestablished. Documented for root review; no character supplied."},
            {'bbox':[1566,1789,1582,1805],'crop':None,'observation':'Two minute dark flecks in the open lower-right field, seen in half b around [1566,634,1582,650]. No legible character or drawn connection identified. No character supplied.'}
        ],
        'source_component_map':{
            'original_C_TikZ_paths':[],
            'final_TikZ_paths':[],
            'graphical_variants':[],
            'insertion':{'source':r'\inserted{et découpages}','full_scan_guide_bbox':[1272,79,1503,167],'record':'Same attached insertion reading as C; no new source path or graphical variant proposed.'},
            'archive_number':{'source':'% archive sheet number: 13','full_scan_bbox':[79,2412,124,2447]},
            'coordinate_or_dimension_maps':'No TikZ fragments combined. All reported boxes refer directly to the original 1760 by 2470 scan.'
        },
        'structural_validation':'Final reading is text-identical to C.tex. Its macros are scanpage, unsure and inserted from PREAMBLE.tex; braces and math delimiters checked directly. Report qualifications and reading.tex agree. No compiler, renderer, format builder or installation was used.',
        'scope':'Only the assigned brief, preamble, scan014 packet, three scan014 source images and this reader directory were read. No other reader output, other-page image, OCR or external source was used.'
    },
    'notation':[
        {'location':'first main title line','written_form':'rounded n followed by one short horizontal stroke and aires','latex':r'$n$-aires','evidence':'Crop 02 shows the rounded letter, independent short hyphen, a-like oval, raised i stroke and remaining joined letters.'},
        {'location':'raised title addition','written_form':'et découpages','latex':r'\inserted{et découpages}','evidence':'Crop 02 shows e and tall t, d and accented e opening, rounded joined cou, descending p, following a/g region and final es; the long curved guide enters the gap before n.'},
        {'location':'second main line opening','written_form':"d'",'latex':"d'",'evidence':'Crop 03 shows looped d and separate raised oblique apostrophe.'},
        {'location':'second main line ending','written_form':'topologiques','latex':'topologiques','evidence':'Tall initial t, descending p, tall l, long returning g-descender and later q-descender are visible, followed by the terminal joined ues run. No terminal point supplied.'}
    ],
    'check_events':[],
    'crops':[
        {'path':'01_first_word.png','bbox':[860,90,1295,195],'rotation':0,'purpose':'Original C doubt: first main title word. Whole target retained; tiny neighboring second-line ascender enters at bottom edge.','enlargement':6,'processing':'PIL autocontrast, LANCZOS; output 2610x630'},
        {'path':'02_insertion_and_naires.png','bbox':[1135,28,1565,180],'rotation':0,'purpose':'Read crowded addition, complete guide and n-aires; contains title-adjacent isolated points.','enlargement':6,'processing':'PIL autocontrast, LANCZOS; output 2580x912'},
        {'path':'03_second_line.png','bbox':[930,182,1565,305],'rotation':0,'purpose':"Original C doubt espaces; whole second line gives d', topologiques and endpoint context.",'enlargement':5,'processing':'PIL autocontrast, LANCZOS; output 3175x615'}
    ],
    'brief_feedback':[
        'The supplied rules distinguish supported marks from paper texture but leave a practical attribution limit for minute isolated page specks. Exact observed points are reported without a supplied character or semantic relation; root can inspect the same crops.',
        'H-absent handling and the two source doubt identities were unambiguous.'
    ]
}
(out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
audit = '''# Scan 014 — independent reader C

Start: **2026-11-20 14:55:36 UTC**. End: **ENDTIME**. The start clock was obtained in the initial read batch, before visual inspection. Only this page's packet and permitted context were read.

## Visual audit

Whole image viewed once for layout; upper half a and lower half b each viewed once. All three local crops were viewed once. No OCR, external research, compiler, renderer, format builder or installation was used. H is empty and `hua_has` is `nothing`.

| Physical item | Direct reading and state | Evidence / outcome |
| --- | --- | --- |
| Addition above first line | `et découpages`, attached before n | `02_insertion_and_naires.png`, full box [1135,28,1565,180]. Raised accent and descending letters checked. The long lead-in curves down into the gap immediately before n; C's insertion is retained. |
| First main line, first word | `\\unsure{décompositions}` | C doubt **first main word**, retained. `01_first_word.png`, [860,90,1295,195]; target [881,96,1268,188]. Initial d, raised accent, co-like low strokes, long p-descender and later tall loop support the candidate; compressed medial joins remain unresolved. No alternative word supplied. |
| First main line, ending | `$n$-aires` | Crop 02: rounded n, single short hyphen, a and raised i stroke, joined ending. Same reading as C. |
| Second main line, opening | `d'\\unsure{espaces}` | C doubt **after d'**, retained. `03_second_line.png`, [930,182,1565,305]; word target [1003,214,1167,274]. Apostrophe, low initial shoulder, long p-descender and low joined final strokes checked; internal letter separation remains unresolved. |
| Second main line, ending | `topologiques` | Crop 03 contains full descenders and blank endpoint space. Tall t/l, descending p/g/q, terminal joined letters checked. No final full stop supplied. |
| Page field | No additional legible text, diagram, deletion or margin note identified | Both halves inspected. Minute isolated point-like spots are recorded separately below; no word or mathematical relation assigned. |
| Lower left foot | Archive numeral `13` | Half b, [79,1257,124,1292], maps to full [79,2412,124,2447] by adding y=1155. Clear 1 followed by 3. Retained comment; archive item added to the inventory. |

## Witness / doubt account

C has two actual doubtful-reading rows; both are retained once, with their original primary readings. Both `diff_C` values are false. No lexical, punctuation, insertion-state or cancellation-state change is proposed. H has no page text, so every H entry is null and every `diff_H` value is false.

The complete proposed `reading.tex` is text-identical to C. Its two `unsure` markers agree with the report. No mathematical check was performed; `check_events` is empty.

## Small surface observations for root review

Three isolated point-like shapes appear in the title crops: [1537,50,1549,62] above/right of the insertion; [1309,161,1323,174] under n; and [939,219,952,231] left of d'. The lower-half open field also contains two minute dark flecks around full [1566,1789,1582,1805]. No letter candidate, secure punctuation attachment, hand or origin was established for these spots. They are documented without a supplied character. Their coordinates are explicit so root can inspect them; they are not presented as lexical additions.

## Final source-component map

There are no original C TikZ paths and no proposed graphical variants. The checked insertion and guide are represented by the unchanged source component `\\inserted{et découpages}`; guide bbox [1272,79,1503,167]. The archive number remains `% archive sheet number: 13`. No local TikZ fragments, dimension maps, path combinations or new path components occur. Inventory order follows the addition, main title, then archive foot numeral, with original inventory identifiers retained in provenance.

## Direct source verification

Macros are confined to `scanpage`, `unsure`, and `inserted` from PREAMBLE, plus ordinary inline math. Braces, math delimiters, crop filenames, C source-row mapping, H-empty state and report/reading agreement checked directly. All generated files are within this reader's assigned directory.
'''.replace('ENDTIME',end)
(out/'reading.md').write_text(audit,encoding='utf-8')
print('Wrote reading.tex, reading.md, report.json at', end)
