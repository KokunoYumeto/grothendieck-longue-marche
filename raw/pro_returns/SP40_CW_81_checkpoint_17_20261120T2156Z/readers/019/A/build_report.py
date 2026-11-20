"""Assemble the independent reader record from recorded human observations."""
from pathlib import Path
import json

base = Path(__file__).parent
manifest_path = base / 'crops' / 'manifest.json'
crops = json.loads(manifest_path.read_text())
for ordinal, crop in enumerate(crops, 4):
    crop['viewed'] = True
    crop['successful_deliveries'] = 1
    crop['delivery_ordinal'] = ordinal
manifest_path.write_text(json.dumps(crops, indent=2, ensure_ascii=False)+'\n')

ledger = [
    {'ordinal': 1, 'path': '/workspace/scratch/94548b74fbe0/source/SP40_CW_81_scans/J81-03_81_scan019.jpg', 'role': 'whole scan', 'size': [1692,2362], 'successful_deliveries': 1, 'viewed': True},
    {'ordinal': 2, 'path': '/workspace/scratch/94548b74fbe0/source/SP40_CW_81_scans/J81-03_81_scan019_a.jpg', 'role': 'half a', 'size': [1692,1261], 'full_scan_offset': [0,0], 'successful_deliveries': 1, 'viewed': True},
    {'ordinal': 3, 'path': '/workspace/scratch/94548b74fbe0/source/SP40_CW_81_scans/J81-03_81_scan019_b.jpg', 'role': 'half b', 'size': [1692,1261], 'full_scan_offset': [0,1101], 'successful_deliveries': 1, 'viewed': True},
]
ledger += [{'ordinal': c['delivery_ordinal'], 'path': c['path'], 'role': 'one planned tight enlargement', 'bbox': c['bbox'], 'successful_deliveries': 1, 'viewed': True} for c in crops]
(base/'image_ledger.json').write_text(json.dumps({'start_utc': '2026-11-20 19:48:18 UTC', 'failed_unseen_deliveries': [], 'reopens': 0, 'items': ledger}, indent=2, ensure_ascii=False)+'\n')

def bbox(values):
    return {'coordinates': 'original full scan, upper-left origin, pixels', 'xyxy': values}

differences = []
def add(identifier, location, C, H, reading, evidence, confidence, kind,
        diff_C, diff_H, status=None, crop=None, box=None, row=None, **extra):
    d = dict(id=identifier, location=location, C=C if C is not None else '(omitted at this locus)', H=H if H is not None else '(omitted at this locus)', reading=reading,
             evidence=evidence, confidence=confidence, kind=kind,
             diff_C=diff_C, diff_H=diff_H, C_doubt_status=status,
             readers_crop=crop, bbox=bbox(box) if box else None)
    if row:
        d['C_source_row'] = row
    d.update(extra)
    differences.append(d)

add('A01','Top text, line 5, before paired display',r'\unsure{ens.}','ens.','ens.',
    'Half a shows an initial small e return, joined low n/s run and a separate terminal point; the whole abbreviation can be read.',
    'high','other',True,False,'resolved',box=[270,505,390,545],row='R01')
add('A02','After Par hyp. de récurrence',r'\unsure{on a}','on a',r'\unsure{on a}',
    'Crop05 shows a short detached dark dash, a low longer returning stroke, then a point. These support the supplied compressed on a candidate without resolving its letters.',
    'low','other',False,False,'retained','crops/05_ona_recurrence.png',[1130,875,1260,925],'R02')
add('A03','First large union sign in the middle equality',r'\mathop{\unsure{\coprod|\bigsqcup}}',r'\coprod',
    'G03: qualified literal footed rounded-U graphic; coprod primary, bigsqcup retained',
    'Crop06 shows a rounded inner bowl, an extended sloping foot, a straight left supporting/retraced run and a straight right retrace. Four local paths preserve these components. The glyph-name uncertainty remains.',
    'medium','drawing or diagram',True,True,'retained','crops/06_first_union.png',[897,975,1017,1048],'R03',
    qualification='The witness glyph-name primary is retained; the difference is explicit preservation of the rounded return and retraced components.',
    graphic='G03')
add('A04','Lower index of first large union, overwritten at K0',r'\alpha\in\deleted{\unsure{J}}K_0',r'\alpha\in K_0',
    r'\alpha\in\deleted{\unsure{J|j}}K_0',
    'Crop06 has a finer upright and loop under the heavy K; a small nearby point leaves a lowercase j reading possible. The current K0 is legible. The predecessor remains doubtful.',
    'low','omission',False,True,'retained','crops/06_first_union.png',[974,1040,1057,1108],'R04',
    qualification='C primary J and its uncertainty retained; j is an explicitly recorded supported alternative. H omits the whole predecessor.')
add('A05','Lead-in below the brace, before donc',r'\unsure{On a}',r'\struck{On} \uncertain{On a}',
    r'\unsure{On a|\deleted{On}On a}',
    'Crop09 shows one overlapped capital cluster, one long low n-like continuation and a separate small lozenge before donc. The cluster supports On a; the overlapping capital also leaves H’s cancelled-On state possible. A second independent complete On cannot be isolated from these strokes.',
    'low','deletion state (struck given live or live given struck)',False,True,'retained','crops/09_ona_donc.png',[285,1510,430,1575],'R05',
    qualification='H survives as the complete-state alternative; this is a qualified primary-state difference, not a conclusive rejection of H.')
add('A06','Struck word after dans la',r'\deleted{\unsure{somme|réunion}}',r'\struck{\ill{}}',
    r'\deleted{\unsure{somme|réunion}}',
    'Crop11 shows an initial small rising hook and a low sequence of humps under one long strike. The middle and ending are substantially crossed; somme remains the strongest candidate, réunion remains supported at low confidence.',
    'low','readable ink left as \\ill{}',False,True,'retained','crops/11_struck_word.png',[1305,1785,1565,1845],'R06',
    qualification='One H ill placeholder counted once; the replacement is still explicitly doubtful.')
add('A07','After se borner à / colon',r'\unsure{sommer}',r'\ill{}','sommer',
    'Crop12 exposes the initial curled s, low o, two linked m groups, small e return and final low r hook. All belong to the one word between the small preceding sign and sur les.',
    'medium','readable ink left as \\ill{}',True,True,'resolved','crops/12_borner_sommer.png',[765,2020,1040,2085],'R07')
add('A08','After K1 in final prose',r'\unsure{cet}','cet','cet',
    'Crop13 shows a small open/looped c-e entry and the tall final t with its right cross return; the following ens. is separate.',
    'high','other',True,False,'resolved','crops/13_cet.png',[540,2210,640,2270],'R08')
add('A09','Line 3, before card',r'\unsure{avec}',None,r'\unsure{avec}',
    'Crop02 shows three separate low groups: short initial point/stroke, shallow bar, and a curved longer return. A compressed avec remains a candidate; the individual letters remain unsettled.',
    'low','omission',False,True,'retained','crops/02_avec.png',[275,294,405,336],'R09',
    H_anchor='Cas général $\\operatorname{card}I\\geq 3$')
add('A10','First U of the paired display',r'\unsure{U|\deleted{=}U}',r'U',
    'G01: qualified full U graphic, with entrance-flourish primary and cancelled-equality alternative retained',
    'Crop03 shows the U body and two additional near-horizontal entrance runs meeting its upper-left turn. The three selected paths reproduce those connected strokes once. Their character/old-sign attachment remains unresolved.',
    'low','drawing or diagram',True,True,'retained','crops/03_first_u.png',[582,544,696,600],'R10',
    qualification='The original C uncertainty is retained; the witness change is the literal entrance geometry. H shares the U primary.',graphic='G01')
add('A11','Below the paired display, before des deux',r"\unsure{l'une|l'un}","l'un",r"\unsure{l'une|l'un}",
    'Crop04 shows l with a raised apostrophe, a low u/n run and a final extended return. That return supports a final e without settling it; the primary l’une and alternative l’un remain.',
    'medium','misread word',False,True,'retained','crops/04_lune.png',[952,752,1170,811],'R11',
    qualification='H’s l’un remains the explicit alternative. The point below the ending is separately recorded as A15 and is not counted as another word.')
add('A12','Brace first line, predecessor beneath K0',r'\deleted{\Sigma_{\unsure{\alpha|0}}}K_0',r'K_0',
    r'\deleted{\Sigma_{\unsure{\alpha|0}}}K_0',
    'Crop07 gives the angular upper, diagonal and lower Sigma strokes beneath the heavy K. The lower small overlapping loop remains compatible with alpha or zero; K0 is clear.',
    'medium','omission',False,True,'retained','crops/07_brace_predecessor.png',[690,1183,797,1268],'R12')
add('A13','After Au, before the written equality sign','deuxième',r'\uncertain{dernier}',
    r'\unsure{dernier|deuxième}',
    'Crop10 shows a small d, a long low middle run, a narrow upright/dotted group and two final low bends. I read dernier first; the compressed middle and raised marks leave deuxième possible. No expected ordinal from the formula was used to settle it.',
    'low','misread word',True,False,None,'crops/10_ordinal.png',[595,1790,878,1847],
    qualification='H has the same primary with editorial doubt. C’s deuxième remains an explicit alternative.')
add('A14','Small sign between borner and sommer','à',':',r'\unsure{à|:}',
    'Crop12 shows a small upper oblique dot and a lower open curved hook. The lower hook supports a compressed a with detached accent; the two-level form also supports a colon reading.',
    'low','other',True,True,None,'crops/12_borner_sommer.png',[625,2032,661,2074],
    qualification='C’s primary à is retained with newly explicit doubt. H’s colon remains the alternative.')
add('A15','Small point under the terminal l’une/l’un run',None,None,
    r"\underset{\phantom{\text{l'un}}\unsure{\cdot}}{\text{\unsure{l'une|l'un}}}",
    'Crop04 shows a distinct dark small point just below the right-hand terminal run. It is reproduced once below the word; attachment to the word, role and hand remain open. A still lower diffuse gray fleck supplies no additional character candidate.',
    'medium','omission',True,True,None,'crops/04_lune.png',[1153,788,1168,803],
    qualification='Visible point shape has medium confidence; punctuation/letter-attachment and hand remain undetermined.',graphic='G02')
add('A16','Footed union in U = U_J,i cap Sigma_i^- display',r'\coprod',r'\coprod',
    'G04: literal second footed rounded-U graphic, primary coprod with local bigsqcup alternative retained in report',
    'Half b shows the second bowl, short extending foot and both straighter supporting/retraced uprights. Four selected paths reproduce this local form. Its glyph-name qualification is covered by the first-occurrence wrapper at G03.',
    'medium','drawing or diagram',True,True,None,None,[824,1615,891,1688],
    qualification='Independently inspected on half b, coordinates [824,514,891,587] in that half. No extra crop was required for this settled path geometry; glyph-name interpretation remains qualified.',graphic='G04')
add('A17','Beginning of line 2','Le','le','Le',
    'Half a shows a tall upright initial L reaching well above the following cas; capital form retained.',
    'high','misread word',False,True,None,None,[277,164,490,231])
add('A18','End of line 1, after card I = 0,1',r'0,1$ Le',r'0,1$, le',r'0,1$ Le',
    'Crop01 reaches the physical right edge. The last numeral’s base reaches that edge; no further punctuation can be recovered. The transcription ends the visible group at 1 and starts the next line with Le.',
    'low','other',False,True,None,'crops/01_top_endpoint.png',[1600,92,1692,165],
    qualification='Qualified selected-text difference only: the edge prevents a decisive statement about a comma beyond the surviving image.')

row_specs = [
 ('R01','line 5, before paired display','ens.','—','resolved','A01'),
 ('R02','after Par hyp. de récurrence','on a','—','retained','A02'),
 ('R03','first large union sign',r'\coprod',r'\bigsqcup','retained','A03'),
 ('R04','under large union, overwritten index','J','—','retained','A04'),
 ('R05','lead-in above U = …','On a','—','retained','A05'),
 ('R06','struck word after dans la','somme','réunion','retained','A06'),
 ('R07','after se borner à','sommer','—','resolved','A07'),
 ('R08','after K₁','cet','—','resolved','A08'),
 ('R09','line 3, before card','avec','—','retained','A09'),
 ('R10','first U of the paired formula','U with an entrance flourish','a cancelled = before U','retained','A10'),
 ('R11','below first display','l’une','l’un','retained','A11'),
 ('R12','brace line 1, underneath K₀','Σ with lower α','Σ with lower 0','retained','A12'),
]
source_rows = [dict(id=r[0], source_ordinal=i, source_section='Doubtful readings',
                    exact_source_location=r[1], source_reading=r[2], source_other_readings=r[3],
                    status=r[4], local_decision_ids=[r[5]]) for i,r in enumerate(row_specs,1)]

local_alternatives = {
 'A02': [], 'A03': [r'\bigsqcup'], 'A04': ['j'], 'A05': [r'\deleted{On}On a'],
 'A06': ['réunion'], 'A09': [], 'A10': [r'\deleted{=}U'], 'A11': ["l'un"],
 'A12': [r'\Sigma_0'], 'A13': ['deuxième'], 'A14': [':'],
 'A15': ['point attached to the word ending', 'independent trace'],
 'A16': [r'\bigsqcup'], 'A18': [],
}
doubts = [
 dict(location=d['location'], reading=d['reading'], alternatives=local_alternatives.get(d['id'], []),
      confidence=d['confidence'], reason=d['evidence'], crop=d['readers_crop'], decision_id=d['id'],
      C_source_row=d.get('C_source_row'))
 for d in differences if d['C_doubt_status']=='retained' or d['id'] in ['A13','A14','A15','A16','A18']
]

inventory=[]
def inv(element, kind, position, words, hand='his hand', **extra):
    inventory.append(dict(sheet_kind='text',hand=hand,element=element,kind=kind,
                          position=position,first_words_or_objects=words,transcribed='yes',**extra))
inv('019.A.01','text','top, physical lines 1–5','Dém. par récurrence … les ens.')
inv('019.A.02','display','upper third','U_J,i cap Sigma_i^+, U_J,i cap Sigma_i^-')
inv('019.A.G01','drawing','first U of paired display','U body and its two entrance runs',components=['body/upper loop','arched upper entrance','lower near-horizontal entrance'],uncertainty='entrance flourish / cancelled equality before U')
inv('019.A.03','text','below paired intersections','ont la forme précédente … l’une / l’un des deux.')
inv('019.A.G02','drawing','below terminal run of l’une/l’un','one small point','undetermined hand',uncertainty='attachment and role unestablished; no extra prose punctuation assigned')
inv('019.A.04','text','above first equality','Par hyp. de récurrence, on a')
inv('019.A.05','display','middle, first equality','U_J,i = X setminus footed union hat Sigma_alpha^+')
inv('019.A.G03','drawing','operator in first equality','rounded U, extended foot and two supporting/retraced runs',components=['bowl','foot','left retrace','right retrace'],uncertainty='coprod / bigsqcup')
inv('019.A.06','deletion','under first union, overwritten at K0','doubtful J / j predecessor')
inv('019.A.07','text','left of brace','où')
inv('019.A.08','display','three lines under left brace','K0 subset J; Sigma_alpha^+ in pi0(X setminus E_alpha); hat Sigma_alpha^+ = Sigma_alpha^+ cup E_alpha.')
inv('019.A.09','deletion','brace line 1','Sigma with doubtful alpha / zero index overwritten by K0')
inv('019.A.10','text','below brace','On a donc')
inv('019.A.11','deletion','overlapped opening capital below brace','possible cancelled On in complete-state alternative',uncertainty='On a primary / deleted On plus On a alternative')
inv('019.A.12','display','start of lower third','U = U_J,i cap Sigma_i^- = X setminus (...)')
inv('019.A.G04','drawing','footed union inside lower display','rounded U, short extending foot and two retraces',components=['bowl','foot','left retrace','right retrace'],uncertainty='same coprod / bigsqcup local ambiguity; first printed qualifier at G03')
inv('019.A.13','deletion','lower paragraph beginning','Soit')
inv('019.A.14','text','lower paragraph through final donc','Au dernier / deuxième =, dans la … soit K1 cet ens., donc')
inv('019.A.15','deletion','after dans la','somme / réunion under long strike')
inv('019.A.16','deletion','after sur les','Sigma')
inv('019.A.17','display','bottom edge','U = X setminus (union indexed alpha in K1 hat Sigma_alpha^+ cup hat Sigma_i^+)')
inv('019.A.18','text','bottom left','archive numeral 18, comment only','undetermined hand')

graphics = [
 {'id':'G01','source_origin':[580,535],'source_locus':[582,544,696,600], 'local_rectangle':[0,0,120,70], 'baseline_y':60,'scale_cm_per_source_pixel':0.008,'paths':3,'description':'one connected U body and two entrance runs; qualified whole glyph'},
 {'id':'G02','source_locus':[1153,788,1168,803],'representation':'standard underset and one qualified dot; positioned beneath right end through phantom l’un','paths':0,'description':'one point, no extra character role assigned'},
 {'id':'G03','source_origin':[895,965],'source_locus':[897,975,1017,1048], 'local_rectangle':[0,0,125,90], 'baseline_y':80,'scale_cm_per_source_pixel':0.008,'paths':4,'description':'bowl, sloped foot, left supporting run and right retrace'},
 {'id':'G04','source_origin':[820,1605],'source_locus':[824,1615,891,1688], 'local_rectangle':[0,0,95,93], 'baseline_y':80,'scale_cm_per_source_pixel':0.008,'paths':4,'description':'second bowl, short foot, left and right retraces'},
]

report = dict(
 scan='019', reader='A', start_utc='2026-11-20 19:48:18 UTC',end_utc='2026-11-20 20:01:00 UTC',
 full_image_viewed=True,halves_viewed=True,complete_visual_read=True,
 differences=differences,doubts=doubts,inventory=inventory,
 notes={
   'page_content':'Handwritten continuation of a recurrence proof: paired intersections, a complement expression with indexed roofed Sigmas, a three-line brace, and restriction to K1 in the final expression.',
   'author_uncertainty':'No explicit author question mark or verbal statement of doubt was found on this sheet. Reader unsure wrappers are editorial.',
   'title_date_page_counts':'One handwritten text sheet; no title or date; pale archive numeral 18 at lower left. No author page number was added.',
   'H_apparatus':'H’s page number and two note macros are editorial apparatus. Notes about the lemma and continuation on another page are not additional manuscript text and create no collation rows.',
   'metadata_conventions':'C’s repeated cotefile{81} is removed under the current convention. scanpage{19} and the archive-number comment are retained. This metadata adjustment is excluded from physical ink difference counts.',
   'mathematics_led_reading':'Read all indices, signs, hats, joins and relations locally. The rightmost E index in the brace is alpha (crop08); the final lower union index reads alpha in K1 despite clipping at the sheet edge (crop14). No expression was repaired from an expected argument. No theorem or proof was checked.',
   'sigma_heads':'Crop03 and crop06 show the plain and roofed Sigma forms with a separated horizontal head and lower zigzag. Roofed occurrences retain widehat; plain occurrences retain Sigma. This page’s upper strokes were read as local handwriting components, without adding a closure operation.',
   'boundary_limits':'First-line numeral 1 reaches the physical right boundary; punctuation beyond it cannot be recovered. Final K1 lower index reaches the physical bottom boundary; its visible parts support K1. Crop13 includes part of the long descender belonging to que on the preceding line, retained through that existing word rather than duplicated as a new mark.',
   'graphical_accuracy':'G01/G03/G04 are manual local path approximations, with declared source origins, baselines and scales. No render, compiler, pixel alignment, extrema calculation or metric validation was run. Source loci and drawing rectangles are separately given.',
   'point_scope':'One clearly separated dark point under l’une/l’un is retained as G02. Its attachment, role and hand remain undetermined. A still lower diffuse gray fleck does not yield a further character candidate.',
   'structural_audit':'Final source-only audit passed. Its first blank-line assertion crossed separate display pairs and falsely failed; the audit was corrected to inspect each display independently, with no transcription change for that script correction.',
   'C_row_scope':'R01–R12 are assigned positional IDs for the twelve physical rows of C_doubts.txt under Doubtful readings, in their exact supplied order. The notation table is not counted as additional doubt rows.',
 },
 notation=[
   {'location':'top cardinality expressions','sign':'I, J, card, sloped lower inequality stroke','latex':r'I, J, \operatorname{card}, \geqslant','note':'geqslant records the visible oblique lower stroke; same inequality reading as witness geq, no separate macro-syntax count'},
   {'location':'paired and repeated displays','sign':'U; hooked J and dotted i subscripts; cap; angular Sigma; raised plus/minus','latex':r'U_{J,i}, \cap, \Sigma_i^+, \Sigma_i^-'},
   {'location':'first and second footed unions','sign':'rounded bowl with extending foot and retraces','latex':'G03 / G04, coprod primary; bigsqcup alternative','note':'second occurrence locally inspected and recorded; first-occurrence printed qualifier retained'},
   {'location':'all roofed Sigmas','sign':'separate angular roof over Sigma','latex':r'\widehat{\Sigma}'},
   {'location':'brace','sign':'pi with two legs and small lower zero; alpha at E','latex':r'\pi_0(X\setminus E_\alpha)','note':'final E_alpha independently settled by crop08'},
   {'location':'lower two inclusion clauses','sign':'open inclusion crossed by a separate oblique stroke','latex':r'\not\subset'},
   {'location':'last display','sign':'ordinary curved union; alpha in K1 below it','latex':r'\bigcup_{\alpha\in K_1}','note':'crop14: K1 lower extremity meets the physical sheet boundary; no unseen continuation supplied'},
   {'location':'prose abbreviations','sign':'Dém., hyp., ens., i.e.; card without point','latex':r'Dém., hyp., ens., i.e.; \operatorname{card}','note':'literal forms retained; no expansion in transcription'},
 ],
 check_events=[],
 coordinate_bookkeeping={'full_size':[1692,2362],'half_sizes':{'a':[1692,1261],'b':[1692,1261]},'half_a_offset':[0,0],'half_b_offset':[0,1101], 'derivation':'2362 - 1261 = 1101; dimensions read from supplied files, no image-difference or alignment computation', 'crop_transform':'Pillow crop in original coordinates, autocontrast, LANCZOS resize to 2800 pixels wide, proportional height rounded, UnsharpMask radius 1.1 / percent 120 / threshold 3; no rotation'},
 crops=crops,graphics=graphics,source_C_doubt_rows=source_rows,
 S_page_scope={'id':'SA01-K81-06','source_range':'81/15–22','source_author_viewed_scan':False,'local_finding':'The cited example expressions do not occur verbatim on scan019. Every roof over Sigma on this sheet was inspected; current C/H already retain those widehat marks. No closure-bar correction is proposed from this broad row. Plain Sigma heads were read from this page’s actual stroke construction; no cross-page inference or S-driven additional bar was made.','changes_proposed':0},
 image_ledger=ledger,
 brief_feedback=[
   'The first-line punctuation is bounded by the physical sheet edge. This return distinguishes a selected reading without an extra comma from a claim that no comma was originally written.',
   'For a named mathematical glyph with a distinctive rounded return and retraces, literal graphics preserve the observed form; the glyph-name candidates remain in comments and the report, with a local unsure wrapper on the first graphic.',
 ],
 counts={'original_C_doubt_rows':12,'covered_original_C_doubt_rows':12,'resolved_original_C_doubt_rows':3,'retained_original_C_doubt_rows':9,
         'difference_records':len(differences),'diff_C':sum(d['diff_C'] for d in differences),'diff_H':sum(d['diff_H'] for d in differences),
         'remaining_local_uncertainty_records':len(doubts),'crop_images':len(crops),'successful_image_deliveries':len(ledger),'image_reopens':0,'inventory_items':len(inventory),'literal_draw_paths':11,'graphical_groups':4,'manuscript_mathematical_checks':0}
)
(base/'report.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(report['counts'],ensure_ascii=False))
