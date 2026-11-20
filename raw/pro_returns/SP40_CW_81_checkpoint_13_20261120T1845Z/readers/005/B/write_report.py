from pathlib import Path
from datetime import datetime, timezone
import json

out = Path('/workspace/scratch/94548b74fbe0/out/readers/005/B')
def box(coords):
    return {'coordinate_system':'original full scan','xyxy':coords}

def difference(id, location, C, H, reading, evidence, confidence, kind,
               diff_C, diff_H, status=None, crop=None, coords=None, **extra):
    row = {
        'id':id, 'location':location, 'C':C, 'H':H, 'reading':reading,
        'evidence':evidence, 'confidence':confidence, 'kind':kind,
        'diff_C':diff_C, 'diff_H':diff_H, 'C_doubt_status':status,
        'readers_crop':crop, 'bbox':box(coords) if coords else None,
        'mathematical_consequence':None,
    }
    row.update(extra)
    return row

differences = [
    difference('005.B.01', 'Line 1, final word', r'\unsure{automorphisme}', 'automorphisme',
        'automorphisme',
        'Opening closed oval a, compressed low u/o/m/r joins, tall t, descending p, tall h, detached i dot, and final isme strokes are visible. The enlarged complete word supports the existing candidate.',
        'high', 'other', False, False, 'resolved', 'crops/01_automorphisme.png', [676,77,1136,169],
        qualification_only_C=True),
    difference('005.B.02', 'Line 3, after f sigma est', r'\unsure{égalmt|également}', 'également',
        r'\unsure{égalmt|également}',
        'Detached accent, small opening e, descending looped g, tall l and crossed terminal t are clear. The very low continuous run between l and the last t does not separate all intermediate letters; the abbreviated candidate remains first.',
        'medium', 'abbreviation expanded or spelling modernised', False, True, 'retained',
        'crops/02_egalmt.png', [1026,276,1188,365], H_reading_retained_as_alternative=True),
    difference('005.B.03', 'Line 4, after Aut(C)', r'\unsure{opere|opère}', 'opère',
        'opere',
        'The o loop, p downstroke and low linked remainder are visible. The open space above the e region has no detached accent stroke; the distinct grave accent on the second occurrence in line 6 was also read on half a.',
        'high', 'abbreviation expanded or spelling modernised', False, True, 'resolved',
        'crops/03_opere.png', [912,375,1037,455]),
    difference('005.B.04', 'Line 5, abbreviation immediately after the line beginning', "l'ens", "l'ens.",
        "l'ens",
        'After the final down-turn of ens, the gap before des contains no point. The abbreviation and following word are clearly separated on half a.',
        'high', 'text not on the page', False, True, None, None, [148,478,429,556]),
    difference('005.B.05', 'Line 5, plural after f', r'\unsure{spèciaux|spéciaux}', 'spéciaux',
        'spèciaux',
        'The detached accent is a short bent stroke descending to the right above the e region. The final x-like kink and following period are visible.',
        'high', 'abbreviation expanded or spelling modernised', False, True, 'resolved',
        'crops/04_speciaux.png', [541,477,762,558]),
    difference('005.B.06', 'Line 7, barred Q inside Aut', r'\unsure{\overline{\mathrm Q}|\overline{\mathbb Q}}',
        r'\overline{\mathbb Q}', r'\unsure{\overline{\mathrm Q}|\overline{\mathbb Q}}',
        'The horizontal overbar is separate. The oval has a largely single upper and left contour, a short doubled/retraced portion near the lower left, and a dark crossed tail with more than one visible stroke. These traces leave ordinary versus double-stroked Q unresolved.',
        'medium', 'misread symbol or index', False, True, 'retained',
        'crops/05_barred_Q.png', [298,690,354,768], H_reading_retained_as_alternative=True),
    difference('005.B.07', 'Line 8, below the right end of coeff.', 'No detached lower mark', 'No detached lower mark',
        r'\underset{\hspace{1.5em}\unsure{=|-}}{\text{coeff.}}',
        'Below the abbreviation point and terminal f is a short blurred darker horizontal trace; a shorter still fainter trace lies above it. The two levels are visible in crop 06. Their status as autograph writing, offset impression or surface trace remains unresolved.',
        'low', 'omission', True, True, None, 'crops/06_coeff.png', [405,881,439,906],
        C_anchor='les coeff. de', H_anchor='les coeff. de'),
    difference('005.B.08', 'Line 9, between Il and au', r'\unsure{revient}', 'revient',
        'revient',
        'Connected opening strokes, a detached dot over i, a low continuation and terminal crossed t are visible. The complete group reads revient without an additional recoverable word or cancellation.',
        'high', 'other', False, False, 'resolved', 'crops/08_revient.png', [786,916,940,974],
        qualification_only_C=True),
    difference('005.B.09', 'Line 9, between au and de', 'au $=$ de', 'au même de',
        'au $=$ de',
        'Two separate roughly horizontal strokes are drawn between au and de, with no letter bodies for meme. The upper line is lighter and the lower line darker and slightly curved.',
        'high', 'abbreviation expanded or spelling modernised', False, True, None,
        'crops/08_revient.png', [1037,922,1104,956]),
    difference('005.B.10', 'Detached mark below le, to the right of the final prose line', 'No mark', 'No mark',
        r'\unsure{\cdot\!\cdot}',
        'Two very small adjacent compact spots lie on approximately the same horizontal level near x864,y1263. Grey material surrounds them. Their physical shape is preserved as a doubtful dot pair; no punctuation function or author attribution is assigned.',
        'low', 'omission', True, True, None, 'crops/10_faint_detached_mark.png', [850,1250,879,1276]),
    difference('005.B.11', 'First isolated lower mark', r'\unsure{-|=}', 'No mark',
        r'\unsure{-|=}',
        'A dark short lower stroke and a shorter, much paler upper trace are visible. The blurred upper trace cannot be assigned securely to the same written sign. Both candidates remain.',
        'low', 'omission', False, True, 'retained', 'crops/09_first_isolated_mark.png', [352,1402,395,1438]),
    difference('005.B.12', 'Short pale trace immediately right of the first lower group', 'No mark', 'No mark',
        r'\unsure{-}',
        'Crop 09 shows a pale, slightly bent short horizontal trace around x436,y1420, separate from the first lower group. Its origin and function remain unresolved.',
        'low', 'omission', True, True, None, 'crops/09_first_isolated_mark.png', [419,1408,452,1435]),
    difference('005.B.13', 'Second dark isolated lower mark, at the right', '-', 'No mark',
        '-',
        'Half b shows a single short dark horizontal stroke around x920,y1425. Its half-b box is (902,653) to (939,678), with full-scan vertical offset 759.',
        'high', 'omission', False, True, None, None, [902,1412,939,1437]),
]

doubts = [
    {'location':'Line 3, after f sigma est','reading':'égalmt','alternatives':['également'],
     'confidence':'medium','reason':'The run following l is too compressed to separate all the intermediate letters.','crop':'crops/02_egalmt.png'},
    {'location':'Line 7, Aut barred Q','reading':r'\overline{\mathrm Q}','alternatives':[r'\overline{\mathbb Q}'],
     'confidence':'medium','reason':'Short retracing at the lower oval and tail leaves the alphabet unresolved.','crop':'crops/05_barred_Q.png'},
    {'location':'Below right end of coeff. in line 8','reading':'=','alternatives':['-'],
     'confidence':'low','reason':'Two blurred levels are visible; the upper trace and the mark origin remain uncertain.','crop':'crops/06_coeff.png'},
    {'location':'Detached small mark near full-scan (864,1263)','reading':r'\cdot\!\cdot','alternatives':[],
     'confidence':'low','reason':'Two tiny spots are visible, but no textual or mathematical intention is established.','crop':'crops/10_faint_detached_mark.png'},
    {'location':'First isolated lower mark near full-scan (375,1425)','reading':'-','alternatives':['='],
     'confidence':'low','reason':'The fainter upper stroke may or may not belong to the same sign; both written-shape candidates are retained.','crop':'crops/09_first_isolated_mark.png'},
    {'location':'Pale trace near full-scan (436,1420)','reading':'-','alternatives':[],
     'confidence':'low','reason':'Short curved horizontal trace with unresolved origin and function.','crop':'crops/09_first_isolated_mark.png'},
]

def inventory(element, kind, position, first, hand='his hand'):
    return {'sheet_kind':'text','hand':hand,'element':element,'kind':kind,
            'position':position,'first_words_or_objects':first,'transcribed':'yes'}

report = {
    'scan':5, 'reader':'B', 'start_utc':'2026-11-20 10:05:16 UTC',
    'end_utc':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
    'full_image_viewed':True, 'halves_viewed':True, 'complete_visual_read':True,
    'differences':differences, 'doubts':doubts,
    'inventory':[
        inventory('005.B.I01','text','Twelve physical lines in the main paragraph','NB Si sigma est un automorphisme ... de f est'),
        inventory('005.B.I02','text','Upper left, under NB','One short underline under NB'),
        inventory('005.B.I03','text','Line 9, under nbs algébriques','One continuous underline, ending before the stop'),
        inventory('005.B.I04','drawing','Below the right end of coeff. in line 8','Two faint short strokes, uncertain = / -','unnamed hand'),
        inventory('005.B.I05','drawing','Right of final prose line, below le','Faint adjacent dot pair','unnamed hand'),
        inventory('005.B.I06','drawing','Lower area, left group','Dark dash and faint upper trace, uncertain - / =','unnamed hand'),
        inventory('005.B.I07','drawing','Immediately right of the first lower group','Faint short curved dash-like trace','unnamed hand'),
        inventory('005.B.I08','drawing','Lower area, right group','One short dark dash','unnamed hand'),
        inventory('005.B.I09','text','Lower left sheet edge','Archive sheet number 4, comment only','unnamed hand'),
    ],
    'notes':{
        'page_content':'A handwritten NB paragraph, twelve physical lines, ending with the unfinished words de f est. Two emphasized spans are underlined. Detached marks are present below and beside the paragraph.',
        'authors_own_uncertainty':{'exact_words':None,'observation':'No explicit author question mark or verbal uncertainty was observed. All unsure macros are reader qualifications.'},
        'title_date_page_counts':'No title or date is present. The lower-left 4 is retained only as archive sheet number; H page 4 is witness indexing. One assigned scan was read.',
        'mathematics_led_reading_decisions':'The written order and grouping of sigma, f superscript sigma, Aut(C), Aut(barred Q), P/Q, P,Q and the isolated equals sign were followed. No expected theorem or mathematical repair determined a reading.',
        'deletion_and_insertion_states':'No secure insertion guide, recoverable deletion or cancellation was observed. The thick sont strokes on line 8 were inspected in crop 07 and retained live.',
        'emphasis_and_H_apparatus':'H emph and our uline encode the same exact two emphasized spans. H note about the unfinished phrase is apparatus and is not manuscript prose. No difference row was made for either matter.',
        'difference_flag_semantics':'diff_C records an actual changed candidate, omitted mark or added mark. Removing a C doubt while retaining its first candidate is recorded in C_doubt_status and a qualification_only_C field or evidence, without setting diff_C. At two unresolved loci H supplies the retained second alternative; diff_H flags the differing proposed first candidate and H_reading_retained_as_alternative records that overlap.',
        'faint_mark_origin':'The shapes below coeff., near (864,1263), and near (436,1420) were retained as uncertain detached marks. Their handwriting, transfer/impression or surface origin is unresolved; unnamed hand in the inventory records no established authorship.',
        'workflow_timing':'The start time was recorded after initial packet text reading and immediately before the first image view.',
    },
    'notation':[
        {'location':'Lines 1 and 3','visible_sign':'Low open arched sigma and repeated raised sign over f','proposed_LaTeX':r'\sigma, f^\sigma'},
        {'location':'Line 3, around spécial','visible_sign':'Two short upright ticks at each side','proposed_LaTeX':"``spécial''"},
        {'location':'Line 4, Aut(C)','visible_sign':'C with an inner left stroke forming a narrow loop','proposed_LaTeX':r'\operatorname{Aut}(\mathbb C)'},
        {'location':'Line 7, Aut barred Q','visible_sign':'Overbar, oval and retraced crossed tail; alphabet unresolved','proposed_LaTeX':r'\operatorname{Aut}(\unsure{\overline{\mathrm Q}|\overline{\mathbb Q}})'},
        {'location':'Line 7, quotient','visible_sign':'Plain capitals P and Q with slash, equality has two bars','proposed_LaTeX':'f=P/Q'},
        {'location':'Line 9, after au','visible_sign':'Two separate horizontal bars','proposed_LaTeX':'='},
        {'location':'Line 5','visible_sign':'ens without a following point','proposed_LaTeX':"l'ens"},
        {'location':'Lines 8–11','visible_sign':'coeff. with point; nbs without point; i.e. with both points','proposed_LaTeX':'coeff., nbs, i.e.'},
        {'location':'Lines 4 and 6','visible_sign':'First opere lacks detached accent; second opère has grave','proposed_LaTeX':'opere; opère'},
        {'location':'Line 5, plural','visible_sign':'Accent slopes down to the right','proposed_LaTeX':'spèciaux'},
    ],
    'check_events':[],
    'crops':json.loads((out/'crop_manifest.json').read_text()),
    'brief_feedback':[
        'The boundary between an intentional detached manuscript mark and a faint transfer or surface trace remains unspecified. I preserved the three newly noticed trace groups with explicit uncertainty, recorded their coordinates and made no semantic assignment.',
        'The requested diff_C/diff_H flags do not specify the treatment of overlapping uncertainty alternatives. This report states its flag semantics explicitly so that retained H alternatives cannot be mistaken for an exclusive rejection.',
    ],
    'image_view_attestation':{
        'full_scan_view_count':1,'half_a_view_count':1,'half_b_view_count':1,
        'each_listed_crop_view_count':1,
        'full_scan_dimensions':[1231,1678], 'half_dimensions':[1231,919],
        'half_a_origin_in_full_scan':[0,0], 'half_b_origin_in_full_scan':[0,759],
        'half_b_offset_evidence':'Pixel-difference comparison of full-scan rows against half b has its minimum at vertical offset 759 among offsets 750 through 759.',
        'every_prose_line_visually_read':True,
        'no_OCR':True, 'no_other_page_images':True, 'no_other_reader_files':True,
        'no_external_research':True, 'no_delegation':True,
    },
}
(out/'report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
print(json.dumps({'differences':len(differences),'doubts':len(doubts),'C_doubt_rows':sum(r['C_doubt_status'] is not None for r in differences),'crops':len(report['crops'])},ensure_ascii=False))
