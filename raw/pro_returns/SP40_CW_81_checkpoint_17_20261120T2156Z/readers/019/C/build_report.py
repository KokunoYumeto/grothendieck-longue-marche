from pathlib import Path
import json

ROOT = Path('/workspace/scratch/94548b74fbe0/out/readers/019/C')
crops = json.loads((ROOT / 'crops/manifest.json').read_text())
crop_by_num = {int(x['path'].split('/')[1][:2]): x for x in crops}

def diff(id, location, C, H, reading, evidence, confidence, kind, dc, dh,
         row=None, status=None, crop=None, bbox=None, **extra):
    c = crop_by_num[crop] if crop is not None else None
    r = dict(id=id, location=location, C='omitted' if C is None else C,
             H='omitted' if H is None else H, reading=reading,
             evidence=evidence, confidence=confidence, kind=kind,
             diff_C=dc, diff_H=dh, C_doubt_status=status,
             readers_crop=c['path'] if c else None,
             bbox={'coordinate_system':'original full scan, upper-left origin, pixels',
                   'box':bbox if bbox is not None else (c['bbox'] if c else None)})
    if row: r['source_C_doubt_row'] = row
    r.update(extra)
    return r

D = [
 diff('D00','Source opening convention',r'\cotefile{81}',None,
      r'\scanpage{19} only at the opening; archive 18 remains a comment',
      'The page carries the proof continuation and the lower-left archival 18. The supplied brief reserves cotefile for scan002; no cote-title ink occurs on this sheet.',
      'high','other',True,False,bbox=[20,20,1670,2345],administrative=True),
 diff('D01','First physical line, right edge after card I=0,1',r'0,1',r'0,1,',r'0,1',
      'The surviving 1 reaches the physical right paper edge. No further comma survives inside that edge. This records the extant scan, with no assertion about any lost material beyond the edge.',
      'medium','text not on the page',False,True,crop=1,qualification='Right-edge limit: absence outside the scanned paper is unassessed.'),
 diff('D02','Second physical line, first word',r'Le',r'le',r'Le',
      'Half a shows a tall initial upright with a long returning foot, followed by the low continuation; initial L is capital height.',
      'high','misread word',False,True,bbox=[276,166,342,233],half_reference={'half':'a','box':[276,166,342,233],'origin':'half a upper-left; full y=half y'}),
 diff('D03','Third physical line, before card I>=3',r'\unsure{avec}','omitted',r'\unsure{avec}',
      'Three separated short components survive: an oblique point, a low horizontal run, and a shallow curved run. They do not independently settle the compressed word; avec remains the marked candidate.',
      'low','omission',False,True,row='C019.R09',status='retained',crop=2),
 diff('D04','Fifth physical line, before the paired display',r'\unsure{ens.}',r'ens.',r'ens.',
      'The enlargement shows an initial small loop/entry, the joined low letter run, and a separate terminal ink point. I read ens. without a remaining word doubt.',
      'medium','other',True,False,row='C019.R01',status='resolved',crop=3,bbox=[270,506,390,549]),
 diff('D05','Paired display, first U entrance strokes',r'\unsure{U|\deleted{=}U}',r'U',r'\unsure{U|\deleted{=}U}',
      'Two near-horizontal entrance strokes and an upper curved return enter the first U stem. Their attachment is visible; a predecessor equality/cancellation remains unestablished. Both complete candidates are retained.',
      'low','other',False,False,row='C019.R10',status='retained',crop=3,bbox=[578,529,698,603]),
 diff('D06','Below the paired display, l’une/l’un',r"\unsure{l'une|l'un}",r"l'un",r"\unsure{l'une|l'un}",
      'The word has the looped l/apostrophe group, low joined humps, and a long final return. That return supports the final-e candidate without settling it. H’s l’un survives as the alternative.',
      'medium','misread word',False,True,row='C019.R11',status='retained',crop=4,bbox=[962,750,1173,804],qualification='Different primary reading; H survives as an explicit alternative.'),
 diff('D07','Immediately below the end of l’une/l’un',None,None,
      'M01: one dark point below the ending, with a much fainter short lower-left trace',
      'A separate dark approximately round point is visible below the terminal return, near (1159,797). A short pale trace lies lower-left, near (1130,808). They are copied once as a locally qualified two-component graphic; their role, hand and surface origin remain unassigned.',
      'medium','omission',True,True,crop=4,bbox=[1124,790,1166,813],graphic='M01',
      component_confidence={'dark_point':'high','pale_short_trace':'low','role_hand_surface_origin':'unresolved'}),
 diff('D08','After Par hyp. de récurrence,',r'\unsure{on a}',r'on a',r'\unsure{on a}',
      'After the comma are a small dark point, a light horizontal curved run with dark return, and another point. The small group does not settle complete letter bodies. The supplied on a candidate remains uncertain.',
      'low','other',False,False,row='C019.R02',status='retained',crop=5),
 diff('D09','First single equality, large join',r'\unsure{\coprod|\bigsqcup}',r'\coprod',r'\unsure{\coprod|\bigsqcup}',
      'The glyph has two upright sides, a separately extended foot bar, and a rounded interior return. Those visible components support the retained candidates; the surrounding mathematics has not been used to select one. The second occurrence is separately logged in notation and prints the first primary unmarked.',
      'medium','other',False,False,row='C019.R03',status='retained',crop=6,bbox=[896,969,1020,1048]),
 diff('D10','First single equality, predecessor under the join',r'\deleted{\unsure{J}}K_0',r'K_0',
      r'\overset{\unsure{\cdot}}{\deleted{\unsure{J|\jmath}}}K_0',
      'Thin hooked/looped predecessor strokes survive below the live K, and a small separated high point appears near (989,1047). J remains uncertain. A dotless-j body is retained as a supported alternative under the separately copied point; this avoids drawing a second dot. The point’s attachment to that predecessor or another nearby stroke remains unresolved.',
      'low','omission',True,True,row='C019.R04',status='retained',crop=6,bbox=[975,1040,1058,1109],graphic='M02',
      qualification='One physical predecessor/point cluster; the point qualification is not counted again.'),
 diff('D11','Middle brace, first condition under live K0',r'\deleted{\Sigma_{\unsure{\alpha|0}}}K_0',r'K_0',
      r'\deleted{\Sigma_{\unsure{\alpha|0}}}K_0',
      'The thin predecessor has two left-pointed turns and a diagonal consistent with Sigma. Its small lower loop is crossed by the heavier live K strokes. Alpha and zero remain supported lower-index candidates; neither is supplied from the later lines.',
      'medium','omission',False,True,row='C019.R12',status='retained',crop=7,bbox=[690,1190,795,1269]),
 diff('D12','Left of the middle brace, near the first/second-condition gap',None,None,
      'M03: pale bowed trace with a short separated upper segment and lower-left return',
      'The enlargement shows a faint near-upright curved trace bending down-left, plus a short separated upper segment. It yields no established character. The complete visible candidate is drawn under unsure; character, role, hand and surface origin remain unassigned.',
      'low','omission',True,True,crop=16,bbox=[488,1276,516,1316],graphic='M03',
      qualification='The crop fully contains the isolated trace but has no adjacent text line inside its bounds; its page position is documented.'),
 diff('D13','Lead-in below the brace, before donc',r'\unsure{On a}',r'\struck{On} \uncertain{On a}',
      r'\unsure{On a|\deleted{On}On a}',
      'One crowded tall looped group, a low following run, and a separate small oval point precede donc. Several crossing strokes remain inside the initial group. The crop does not settle a separate cancelled On versus retracing/overwriting within the visible On. The complete H state is retained as the alternative; no chronology is asserted.',
      'low','deletion state (struck given live or live given struck)',True,True,row='C019.R05',status='retained',crop=8,
      qualification='C’s primary words remain; the supported full-state alternative is added. H’s state is retained, not conclusively rejected.'),
 diff('D14','Long U display, immediately before X',None,None,r'\unsure{\cdot}',
      'A small detached dark point is visible immediately left of X near (728,1661). It is preserved as a qualified point, without an asserted multiplication, punctuation, hand or surface origin.',
      'medium','omission',True,True,crop=9,bbox=[723,1656,733,1667],graphic='M05'),
 diff('D15','Long U display, to the right and below the closing parenthesis',None,None,
      'M04: two small dark points, the lower one offset left',
      'The complete-context enlargement shows two distinct dark points near (1628,1690) and (1623,1697), separated from the closing parenthesis. Their visible positions are copied literally. A punctuation role, writer and surface origin remain unresolved.',
      'high','omission',True,True,crop=14,bbox=[1618,1684,1634,1703],graphic='M04',
      component_confidence={'two_shapes':'high','punctuation_role_hand_surface_origin':'unresolved'}),
 diff('D16','Lower paragraph, after Au and before =',r'deuxième',r'\uncertain{dernier}',r'\unsure{deuxième|deuxieme|dernier}',
      'The long word has an initial looped/raised component, several separated low runs, a narrow upright with a raised mark, and a final run of humps. Deuxième remains my primary; the attachment of the raised mark leaves the accent unsettled, and dernier remains a supported word alternative. Au and the following equality/comma are readable.',
      'medium','misread word',False,True,crop=10,
      qualification='C’s primary spelling is unchanged but newly qualified. H’s word remains an explicit alternative; this is not a conclusive H error.'),
 diff('D17','Lower paragraph, struck word after dans la',r'\deleted{\unsure{somme|réunion}}',r'\struck{\ill{}}',
      r'\deleted{\unsure{somme|réunion}}',
      'A long cancellation covers almost the entire low letter body. A raised initial remnant, low humps, and a returning terminal stroke survive. Somme and réunion remain uncertain; the following live réunion has not been used to manufacture the predecessor.',
      'low',r'readable ink left as \ill{}',False,True,row='C019.R06',status='retained',crop=11,bbox=[1310,1788,1555,1830],
      qualification='Candidate recovery from surviving ink; neither word is claimed certain.'),
 diff('D18','Lower paragraph, mark immediately after borner',r'à',r':',r'\unsure{à|:}',
      'The mark comprises a high short dark stroke and a lower open curved component. The lower component has a short return, which supports the à candidate; the separation also supports H’s colon reading. Both remain explicit.',
      'low','misread symbol or index',False,True,crop=12,bbox=[631,2036,656,2070],
      qualification='C’s primary à remains; H’s colon remains an alternative. No grammar-based repair is made.'),
 diff('D19','Lower paragraph, after the borner mark',r'\unsure{sommer}',r'\ill{}',r'sommer',
      'The enlarged word shows the initial bent s-like stroke, the connected low o/m runs, a small loop near the ending, and the returning r termination. I read sommer, retaining the written word without expansion.',
      'medium',r'readable ink left as \ill{}',True,True,row='C019.R07',status='resolved',crop=12,bbox=[772,2028,1029,2069]),
 diff('D20','Last prose line, after K1',r'\unsure{cet}',r'cet',r'cet',
      'A low initial rounded entry and following join lead to a tall final t with a rightward cross/return. The enlarged group settles cet. The following ens. and separate comma are independently visible.',
      'high','other',True,False,row='C019.R08',status='resolved',crop=13,bbox=[546,2214,633,2261]),
]

doubt_specs = [
 ('D03',['avec'],'Three shortened components do not settle full letters.'),
 ('D05',['U with entrance return','cancelled equality before U'],'Attachment/cancellation of entrance strokes remains open.'),
 ('D06',["l’une","l’un"],'The last low return may be the final e or a word-ending flourish.'),
 ('D07',['dark point with pale lower-left trace'],'Shapes retained; role, hand and surface origin remain open.'),
 ('D08',['on a'],'The tiny components do not settle complete letter bodies.'),
 ('D09',[r'\coprod',r'\bigsqcup'],'Foot bar and rounded return coexist in the visible glyph.'),
 ('D10',['cancelled J body with separate high point','cancelled dotless-j body with separate high point'],'Predecessor body and attachment of the high point remain open.'),
 ('D11',[r'\deleted{\Sigma_\alpha}',r'\deleted{\Sigma_0}'],'Heavier live K obscures the predecessor’s lower loop.'),
 ('D12',['pale curved trace'],'No character, hand, role or surface origin established.'),
 ('D13',['On a','cancelled On followed by On a'],'Crossings do not settle full cancellation/overwriting state.'),
 ('D14',['detached point'],'Point shape retained, with role, hand and surface origin open.'),
 ('D15',['paired points'],'The two shapes are clear; punctuation role, hand and surface origin remain open.'),
 ('D16',['deuxième','deuxieme','dernier'],'Compressed word and raised mark attachment remain unsettled.'),
 ('D17',['somme','réunion'],'Cancellation masks most letter bodies.'),
 ('D18',['à',':'],'The high stroke and low open return support both candidates.'),
]
by_id = {x['id']:x for x in D}
doubts = []
for id, alternatives, reason in doubt_specs:
    d=by_id[id]
    doubts.append(dict(id=id,location=d['location'],reading=d['reading'],alternatives=alternatives,
                       confidence=d['confidence'],reason=reason,crop=d['readers_crop'],
                       bbox=d['bbox'],source_C_doubt_row=d.get('source_C_doubt_row')))
doubts.append(dict(id='N-JOIN2',location='Long U display, second large join',
                   reading=r'\coprod',alternatives=[r'\coprod',r'\bigsqcup'],confidence='medium',
                   reason='The second glyph was independently enlarged. Its upright sides, foot stroke and rounded return leave the same local glyph interpretation open. Printed primary is unmarked by the recurring-glyph rule.',
                   crop=crop_by_num[9]['path'],bbox={'coordinate_system':'original full scan, upper-left origin, pixels','box':[822,1606,893,1685]},source_C_doubt_row=None))

def inv(element,kind,position,words,hand='his hand',**extra):
    return dict(sheet_kind='text',hand=hand,element=element,kind=kind,position=position,
                first_words_or_objects=words,transcribed='yes',**extra)

inventory = [
 inv('019.C.01','text','Top, physical lines 1–5','Dém. par récurrence … les ens.'),
 inv('019.C.02','display','Upper third, paired intersections',r'U_{J,i}\cap\Sigma_i^+, U_{J,i}\cap\Sigma_i^-'),
 inv('019.C.03','deletion','First U entrance strokes','Possible cancelled = before U',state='Uncertain; U-flourish primary, cancelled-equality alternative.'),
 inv('019.C.04','text','Two prose lines below paired display',"ont la forme précédente … l’une/l’un des deux."),
 inv('019.C.05','drawing','Below final return of l’une/l’un, bbox [1124,790,1166,813]','M01: dark point and pale short trace',hand='undetermined hand',components=['one dark filled point','one short pale lower-left trace']),
 inv('019.C.06','text','Above first single equality','Par hyp. de récurrence, on a'),
 inv('019.C.07','display','First single equality',r'U_{J,i}=X\setminus …'),
 inv('019.C.08','deletion','Lower limit of first large join','Cancelled J/dotless-j predecessor before live K0',state='Predecessor glyph uncertain; high point attachment uncertain.'),
 inv('019.C.09','drawing','High point over predecessor near [989,1047]','M02: separate point, drawn once above J/dotless-j alternatives',hand='undetermined hand'),
 inv('019.C.10','text','Left above middle brace','où'),
 inv('019.C.11','drawing','Left of middle brace, bbox [488,1276,516,1316]','M03: pale bowed trace and short separated segment',hand='undetermined hand',components=['short upper segment','curved descending trace with lower-left return']),
 inv('019.C.12','display','Middle, three conditions under one brace',r'K_0\subset J; \Sigma_\alpha^+\in\pi_0(X\setminus E_\alpha); \widehat\Sigma_\alpha^+=\Sigma_\alpha^+\cup E_\alpha.'),
 inv('019.C.13','deletion','Brace first condition under live K0',r'\Sigma_{\alpha|0}',state='Sigma predecessor visible; small lower index unresolved.'),
 inv('019.C.14','text','Below brace','On a donc',state='Whole-state alternatives explicitly retained.'),
 inv('019.C.15','deletion','Crowded initial On group','Possible cancelled On underlying/followed by live On a',state='Uncertain, retained only as the full-state alternative; no chronology asserted.'),
 inv('019.C.16','display','Below On a donc',r'U=U_{J,i}\cap\Sigma_i^-=X\setminus( … )'),
 inv('019.C.17','drawing','Immediately left of X, near [728,1661]','M05: detached point',hand='undetermined hand'),
 inv('019.C.18','drawing','After lower display right parenthesis, bbox [1618,1684,1634,1703]','M04: two offset points',hand='undetermined hand',components=['upper-right point','lower-left point']),
 inv('019.C.19','deletion','Lower paragraph opening','Soit'),
 inv('019.C.20','text','Lower paragraph, five physical lines','Au deuxième/deuxieme/dernier =, dans la … soit K1 cet ens., donc'),
 inv('019.C.21','deletion','After dans la','somme/réunion',state='Cancelled; word reading remains low confidence.'),
 inv('019.C.22','deletion','After sur les',r'\Sigma'),
 inv('019.C.23','display','Bottom edge',r'U=X\setminus(\bigcup_{\alpha\in K_1}\widehat\Sigma_\alpha^+\cup\widehat\Sigma_i^+)'),
 inv('019.C.24','text','Lower-left paper corner','Archive number 18; represented only by the prescribed comment',hand='undetermined hand'),
]

row_sources = [
 ('C019.R01','line 5, before paired display','ens.','D04','resolved'),
 ('C019.R02','after Par hyp. de récurrence','on a','D08','retained'),
 ('C019.R03','first large union sign',r'\coprod | \bigsqcup','D09','retained'),
 ('C019.R04','under large union, overwritten index','J','D10','retained'),
 ('C019.R05','lead-in above U = …','On a','D13','retained'),
 ('C019.R06','struck word after dans la','somme | réunion','D17','retained'),
 ('C019.R07','after se borner à','sommer','D19','resolved'),
 ('C019.R08','after K₁','cet','D20','resolved'),
 ('C019.R09','line 3, before card','avec','D03','retained'),
 ('C019.R10','first U of the paired formula','U entrance flourish | cancelled = before U','D05','retained'),
 ('C019.R11','below first display','l’une | l’un','D06','retained'),
 ('C019.R12','brace line 1, underneath K₀','Sigma lower alpha | Sigma lower zero','D11','retained'),
]
source_rows=[]
for id,location,reading,did,status in row_sources:
    source_rows.append(dict(id=id,source_location=location,source_reading=reading,physical_loci=[did],
                            status=status,crop=by_id[did]['readers_crop'],covered=True))

notation = [
 {'location':'Top lines 1–3','reading':r'\operatorname{card} I; J; \geq','evidence':'Serifed I, hooked J and two-part comparison sign inspected on half a.'},
 {'location':'Paired display, both occurrences','reading':r'U_{J,i}\cap\Sigma_i^+, U_{J,i}\cap\Sigma_i^-','evidence':'Both low J/i groups, both intersections and separate high plus/minus inspected; no hat is supplied to either Sigma.'},
 {'location':'First large join','reading':r'\unsure{\coprod|\bigsqcup}','evidence':'Two upright sides, an extended foot bar and rounded return; crop06. Qualification retained as D09.'},
 {'location':'Second large join','reading':r'\coprod','alternatives':[r'\coprod',r'\bigsqcup'],'evidence':'Independent crop09 shows the short extended foot and lower curved return. Primary printed unmarked after first-occurrence qualification; local uncertainty remains in N-JOIN2.'},
 {'location':'Plain joins in prose, middle definition and final display','reading':r'\bigcup, \cup','evidence':'Open rounded bowls at their separately inspected positions; no foot bar supplied at these positions.'},
 {'location':'Raised signs over nine Sigma occurrences across first equality, brace definition, lower display, prose union, hatted noninclusion pair and last display','reading':r'\widehat{\Sigma}','evidence':'Each has an angular raised roof. Current C and H already supply these roofs. No closure bar is inferred from S’s broad page range.'},
 {'location':'Middle brace, second condition','reading':r'\pi_0(X\setminus E_\alpha)\quad(\forall\alpha\in K_0)','evidence':'Pi has two uprights and a low oval; E, alpha and the parenthesized quantifier inspected on half b.'},
 {'location':'Lower noninclusion line, both relations','reading':r'\not\subset','evidence':'Each open inclusion has its own oblique crossing stroke, independently inspected on half b.'},
 {'location':'Last lower limit at paper edge','reading':r'\alpha\in K_1','evidence':'Crop15 preserves enough of the alpha, membership and K/1 strokes for the reading. Their bottom ends meet the physical edge; unseen continuation is not supplied.'},
 {'location':'Contractions throughout','reading':'Dém.; hyp.; ens.; i.e.; card','evidence':'Stops retained at the individually read abbreviation positions; card has no added abbreviation point.'},
]

report = dict(
 scan=19, reader='C', start_utc='2026-11-20 19:48:32 UTC', end_utc=None,
 full_image_viewed=True, halves_viewed=True, complete_visual_read=True,
 differences=D, doubts=doubts, inventory=inventory,
 notes={
   'page_content':'Continuation headed Dém. par récurrence. The text gives cardinality cases, the written U expressions and three braced conditions, then names K1 in the lower prose and ends with another complement-of-union expression. These statements are transcribed; no proof check is claimed.',
   'authors_own_uncertainty':[],
   'title_date_page_counts':{'title':None,'date':None,'manuscript_page_number':None,'archive_sheet_number':'18','scan':19,'H_page_label':18},
   'paragraph_order':'Opening proof prose, paired display, following prose, recurrence lead-in and equality, où and brace, On a donc and display, lower paragraph and final display.',
   'mathematics_led_reading_decisions':'The mathematical expressions identified the local targets: large join glyphs, predecessor indices, hats, lower limits and noninclusion strokes. No expected identity, theorem, grammatical repair or mathematical correction was used to settle an unreadable mark.',
   'S_row_handling':{'id':'SA01-K81-06','status':'locally inspected as a witness proposal only','result':'The three quoted examples in the supplied broad-range row do not occur verbatim on this page. The visible raised signs at this page’s nine hatted Sigma occurrences are angular roofs already represented in current C/H. No new closure bar is inferred.'},
   'H_apparatus':'H’s two note macros concerning neighboring sheets and its page label are apparatus. No prose is invented from them, and no H collation count is assigned merely for their omission.',
   'C_notes':'The supplied C_notes.txt was empty.',
   'image_order':'Whole once, a once, b once; then crop01 through crop16 once each. All deliveries succeeded. No image was reopened.',
   'image_processing':'PIL crop, autocontrast, LANCZOS resize to width 2800 and UnsharpMask only. No OCR or recognition, no source pixel matching, no image difference calculation, no optional geometry calculation.',
   'coordinate_maps':'Full scan 1692x2362; each half 1692x1261. a uses y_full=y_a; b uses y_full=y_b+1101, with 1101=2362-1261. Crop boxes all use the original full scan upper-left origin.',
   'graphical_representation':'M01, M03 and M04 use fixed local rectangles and literal paths/fills with their full-scan origins written in the TeX comments. M02 and M05 use qualified dot candidates. These preserve observed shapes without assigning a character role, mathematical operation, hand or surface origin. Font extents and surrounding TeX placement are manual approximations, not rendered or metrically validated.',
   'crop_boundaries':'Crop01 and crop15 include the physical right/bottom paper boundaries. Crop13 contains the entire target K1/cet/ens./donc group; its upper boundary cuts only the preceding line’s long descender. Crop16 contains the whole isolated pale trace but no adjacent text line. No repeat crop was made.',
   'validation':'Only structural source checks are authorized: braces, delimiters, environments, macro names, file references and reading/report consistency. No compilation, rendering or installation is performed.',
 },
 notation=notation, check_events=[], crops=crops,
 brief_feedback=[
   'The brief supplies no explicit layout rule for a tiny anonymous trace below a prose-word ending or beside a mathematical display. I use small standard-TikZ glyph fragments at the local attachment, with fixed origin/rectangle and locally marked uncertainty, so the adjacent word/formula occurs only once. They are not presented as mathematical operations.',
   'At the physical right and bottom sheet edges, report absence only within surviving paper; the lost continuation beyond the edge is unassessed.',
 ],
 source_C_doubt_rows=source_rows,
 source_C_doubt_coverage={'original_rows':12,'covered_rows':12,'resolved_rows':3,'retained_rows':9,'duplicates':0,'uncovered_rows':0},
 image_ledger_file='image_ledger.json',
 counts={'difference_records':len(D),'diff_C_true':sum(x['diff_C'] for x in D),
         'diff_C_true_ink_only':sum(x['diff_C'] and not x.get('administrative',False) for x in D),
         'diff_H_true':sum(x['diff_H'] for x in D),'doubt_records':len(doubts),
         'inventory_elements':len(inventory),'crops':len(crops),'base_image_views':3,
         'successful_image_views':19,'failed_unseen_deliveries':0,'reopened_images':0,
         'new_graphical_clusters':5,'literal_tikz_components':6,'standard_dot_components':2},
 scope={'allowed_reads_only':True,'other_readers_or_root_decisions_read':False,'other_pages_read':False,
        'delegation':False,'internet_or_research':False,'OCR':False,'compilation_or_rendering':False,
        'installations':False,'optional_mathematical_or_geometry_computations':False},
)
(ROOT/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report['counts'],ensure_ascii=False))
