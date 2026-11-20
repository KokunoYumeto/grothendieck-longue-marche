from pathlib import Path
import json

ROOT = Path('/workspace/scratch/006c0e32b2af/out/readers/scan076/C')
reading = (ROOT/'reading.tex').read_text()
insertion = reading[reading.index(r'\makebox[2em]'):reading.index(r" de \(U_i\)")]
pair = reading[reading.index(r'\margin{'):reading.index('% archive sheet number:')].strip()
manifest = json.loads((ROOT/'crop_manifest_c76.json').read_text())
for row in manifest:
    row['requested_deliveries'] = 1
    row['actual_visual_views'] = 1
(ROOT/'crop_manifest_c76.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+'\n')

def decision(id, place, c, final, diff, doubt, unresolved, alternatives, confidence, kind, shows, bbox, crop=''):
    return {'id':id, 'place':place, 'c_reading':c, 'h_reading':None, 'reading':final,
            'diff_c':diff, 'diff_h':False, 'c_doubt':doubt, 'unresolved':unresolved,
            'alternatives':alternatives, 'confidence':confidence, 'kind':kind,
            'scan_shows':shows, 'crop':str(ROOT/crop) if crop else '', 'bbox':bbox}

decisions = [
 decision('C76-01','Insertion above the gap between extensions and de',r"\(\inserted{U'_i}\)",insertion,True,False,False,[], 'high','drawing or diagram',
          'The primed U and short lowered i stand above the line. Beneath them a separate pen stroke curves down from a high left end into a low central cusp, then rises into a longer right shoulder. There is no arrowhead. C marks the insertion but does not reproduce this curved pointer.',
          [1287,179,1349,247]),
 decision('C76-02','First transition symbol after soit',r'\unsure{\eta|n|\gamma}_{ij}',r'\unsure{\eta|n}_{ij}',True,True,True,[r'\eta',r'n'],'medium','misread symbol or index',
          'A high curved entry leads to a first downstroke; a rising link reaches a second high stem whose downstroke extends lower. These two successive stems support eta or an overlong cursive n. They do not form the single converging fork and stem of gamma. The lowered suffix has a short i and a separately dotted, loop-descending j. Removing gamma changes the recorded alternatives.',
          [594,380,644,438],'c76_01_transition.jpg'),
 decision('C76-03','Subscript of the source primed U',r"U'_{\unsure{j|i}}",r"U'_j",True,True,False,[],'high','misread symbol or index',
          'Below the raised prime, the dark retraced index has a long downstroke, a low oval loop and a terminal descending stroke. This matches the independently visible j at the end of the same restriction; the long lower loop rules out a short i. Retracing is visible, but no separate earlier character can be recovered.',
          [942,375,985,440],'c76_02_source_index.jpg'),
 decision('C76-04','Subscript of the target primed U',r"U'_{\unsure{i|j}}",r"U'_{\unsure{i|j|k}}",True,True,True,['i','j','k'],'medium','misread symbol or index',
          'The small index has a dark upright, a short upper-right branch and a broad retraced low foot enclosing a narrow white space. The short rightward foot favours i, but an overwritten or shortened j loop remains possible; the upper branch also permits k, though it could belong to an underletter. The individual stroke order and an independent underletter cannot be established. Adding k changes the recorded alternatives.',
          [1211,374,1255,433],'c76_03_target_index.jpg'),
 decision('C76-05','Correction at the beginning of tels',r'\deleted{\unsure{d}}tels',r'\deleted{d}tels',True,True,False,[],'high','misread symbol or index',
          'A closed bowl survives to the lower left of the tall initial stem, forming a readable d underneath. A distinct dark crossbar and retraced upright supply the live t. The following e, looped l and terminal s remain live. No earlier whole word is recoverable.',
          [948,462,993,501],'c76_04_tels_correction.jpg'),
 decision('C76-06','Obstruction paragraph, est ... par',r'\unsure{donné|donnée}','donné',True,True,False,[],'high','misread word',
          'After the d bowl and ascender, a small o and two low n arches lead to one final e loop. A rising acute stroke stands above that e. Its terminal stroke rises directly out of the final loop; there is no second e body.',
          [1383,466,1475,503],'c76_05_donne.jpg'),
 decision('C76-07','First remark heading',r'\uline{Rmq} \unsure{1|s}',r'\uline{Rmq} 1',True,True,False,[],'high','misread symbol or index',
          'After the underlined q, the detached mark is a short almost upright stroke with a slight lower hook. It has no pair of opposed curves for s. The underline stops before this numeral, and a separate vertical pair of colon points follows.',
          [313,970,393,1019],'c76_06_rmq_heading.jpg'),
 decision('C76-08','First word after the remark colon',r'\unsure{itou}','itou',True,True,False,[],'high','misread word',
          'Half b shows a low i with its detached dot, a tall t with a rightward cross-stroke, then a small closed o and the linked down-and-up strokes of u. The letters are distinct enough to remove the C doubt without a crop.',
          [431,968,501,1009]),
 decision('C76-09','Cancelled second remark heading',r'\deleted{\uline{\unsure{Rmq 2|Rmqs}}}',r'\deleted{\uline{\unsure{Rmq 2|Rmqs}}}',False,True,True,['Rmq 2','Rmqs'],'medium','misread word',
          'R retains its upper bowl and descending leg; the following low arches and q bowl/descender survive beneath the diagonal cancellation strokes. The last hooked, low-ending character favours 2, but the crossing lines mask the middle and leave s possible. A lower underline survives. The following colon is outside the cancellation; there is no continuation after it.',
          [310,1047,388,1095],'c76_07_cancelled_heading.jpg'),
 decision('C76-10','Slanted signature',r'P. Deligne',r'P. Deligne',False,False,False,[],'high','other',
          'After rotation, the initial shows a capital-sized upper bowl and a long stem, followed by a separate low point. The name has a capital D, low e, tall looped l, dotted i, descending g, n and terminal e. The initial P and the complete signature in C are confirmed.',
          [821,1210,960,1280],'c76_08_signature_initial.jpg'),
 decision('C76-11','Detached marks below and right of the signature',r'\margin{\unsure{:}}',pair,True,True,True,['unassigned pair of marks','colon-like punctuation','incidental marks unrelated to the letter'],'low','drawing or diagram',
          'Two separate dark shapes lie on a rising left-to-right diagonal: a compact nearly round lower-left spot and a narrower oblique oval above and right. The upper spot is not vertically aligned over the lower spot. Their shape is reproduced without asserting punctuation or authorship; surrounding faint gray paper traces are not assigned as authored ink.',
          [1402,1375,1417,1391],'c76_09_detached_pair.jpg'),
]

def inventory(element,kind,position,first,hand='P. Deligne (named other hand)'):
    return {'sheet_kind':'letter','hand':hand,'element':element,'kind':kind,'position':position,'first_words_or_objects':first,'transcribed':'yes'}

report = {
 'scan':76, 'reader':'C',
 'image_views':[
  '/workspace/scratch/006c0e32b2af/source/SP46_CW_37_scans/H37-01_37_scan076.jpg',
  '/workspace/scratch/006c0e32b2af/source/SP46_CW_37_scans/H37-01_37_scan076_a.jpg',
  '/workspace/scratch/006c0e32b2af/source/SP46_CW_37_scans/H37-01_37_scan076_b.jpg'],
 'reading_path':str(ROOT/'reading.tex'),
 'crops':[{k:r[k] for k in ('file','bbox','rotation','reason','processing')} for r in manifest],
 'decisions':decisions,
 'inventory':[
  inventory('Opening continuation','text','Upper line, x376–1283 y61–116','Soit donc U_i un recouvrement affine de X_0, et'),
  inventory('Element and cohomology group','display','Upper display, x553–940 y115–192',r'e\in H^{0^{(\mathrm{alg})}}(X_0,\mathscr{E}xt^1(K,\mathscr{N}))'),
  inventory('Local extensions and agreement of classes','text','Two lines, x365–1605 y222–345',"représenté par des classes d'isomorphies"),
  inventory('Name of the local extension','insertion','Above extensions/de, x1297–1342 y180–217',r"U'_i"),
  inventory('Curved insertion pointer','drawing','Under inserted U, x1287–1349 y213–247','Curved left shoulder, low central cusp, rising right shoulder'),
  inventory('Local isomorphism','display','x486–1441 y374–439',r"soit \unsure{\eta|n}_{ij} ... U'_j\mid U_i\cap U_j\xrightarrow{\sim}U'_{\unsure{i|j|k}}\mid U_i\cap U_j"),
  inventory('Cocycle obstruction','text','Two lines, x358–1535 y457–587',r"L'obstruction à construire des \eta_{ij}"),
  inventory('Initial d overwritten by t','deletion','In tels, x948–975 y462–501',r'\deleted{d}tels'),
  inventory('Obstruction map','display','x516–1319 y652–711',r'd_2:H^0(X_0,\mathscr{E}xt^1(K,\mathscr{N}))\longrightarrow H^2(X_0,\mathscr{H}om(K,\mathscr{N}))'),
  inventory('Analytic case and GAGA conclusion','text','Two lines, x351–1482 y772–898','La même construction marche dans le cas analytique'),
  inventory('First remark','text','x313–1606 y967–1018','Rmq 1 : itou pour les espaces algébriques'),
  inventory('Cancelled second remark heading','deletion','x310–388 y1047–1095',r'\uline{\unsure{Rmq 2|Rmqs}}'),
  inventory('Uncancelled colon after the second heading','text','x399–408 y1065–1084',':'),
  inventory('Closing','text','x737–901 y1123–1167','Bien à toi'),
  inventory('Signature','text','Upward-slanting line, x821–960 y1210–1280','P. Deligne'),
  inventory('Detached dark pair','drawing','Lower-right blank area, x1402–1417 y1375–1391','Lower round point and upper-right oblique oval','unnamed hand; origin of marks uncertain'),
  inventory('Archive sheet number','text','Lower left, x62–123 y1909–1969','75, recorded only in a TeX comment','unnamed other hand'),
 ],
 'notes':('Handwritten continuation and closing of a letter signed P. Deligne. It describes local extensions, transition isomorphisms, the written cocycle condition and an obstruction arrow, then says the construction also works analytically and invokes GAGA. The first remark mentions algebraic spaces, rigid analytic spaces and formal schemes. A second underlined heading is cancelled, while its colon remains live; no text follows that colon. No title, date, salutation or manuscript page number appears on this sheet. The only page-like numeral is archive 75 at lower left, kept solely as a comment. No explicit author question mark or stated doubt occurs. H provides description only and is unavailable for collation: every h_reading is null and diff_h is false. The whole image was viewed once for layout, followed by half a then half b once each. Half b begins at whole-image y=920. Nine retained crops were each delivered and visually inspected once in batches of three; requested and actual views are recorded in crop_manifest_c76.json. No OCR, external source, other page, peer reading or TeX engine was used.'),
 'math_reading_decisions':[
  r'The unmarked C-context cover and restriction targets are confirmed: U_i, X_0, inserted U\prime_i, and \mathscr{N}\mid U_i. Primes are short raised strokes; i is a short low suffix; restriction bars are tall single vertical strokes.',
  r'The first H has one ordinary upright-and-crossbar structure, followed by a raised 0 and a still higher parenthesized alg. The first display is H^{0^{(\mathrm{alg})}}, with actual parentheses around alg.',
  r'The sheaf-functor initials have looped/curling forms, transcribed \mathscr{E}xt^1 and \mathscr{H}om. The cohomology H and each K are ordinary single-stroke capitals. The ideal letter is looped \mathscr{N}. Each occurrence was checked on this page.',
  r'The transition arrow has one shaft, a right arrowhead, and a single wavy stroke above. Both restrictions show U_i\cap U_j with an arched intersection sign. The source suffix resolves to j; the target remains i|j|k from its own merged strokes.',
  r'The recurring transition glyph is marked \unsure{\eta|n} at its first appearance and written \eta thereafter. The first symbol and all later copies have two stems, one descending farther; gamma is excluded from the alternatives. Lowered ij, jk and ik are independently read in the cocycle line.',
  r'The inline expression after par is d_2\eta as written, although the opening element is named e. The glyph after d_2 has the same descending two-stem shape as the transition symbols, not the small loop of the opening e. It has not been corrected to d_2e.',
  r'The last display has low numeral 2 after d, H^0 at the source, \mathscr{E}xt^1 inside it, and H^2 at the target with \mathscr{H}om. The long arrow points right and both outer expressions close with two parentheses.',
 ],
 'check_events':[
  {'statement_id':'local-transition-cocycle','type':'local domain-and-codomain check','outcome':r'Under the preferred reading U\prime_j to U\prime_i, composing \eta_{ij} with \eta_{jk} has source U\prime_k and target U\prime_i, matching the written \eta_{ik}. This is only a consistency check; it does not decide the obscured target subscript and does not prove existence or vanishing of the obstruction.'}
 ],
 'notation':[
  {'sign':'Cover and local-extension symbols','latex':r"U_i; U'_i; U'_j",'evidence':'U is formed by two upright sides joined low; the prime is a separate raised slant and the indices are below.','place':'Opening line, interlinear insertion, and isomorphism'},
  {'sign':'Parenthesized high qualifier','latex':r'H^{0^{(\mathrm{alg})}}','evidence':'Ordinary H, small raised oval 0, and a yet higher alg enclosed by two curved parentheses.','place':'First display'},
  {'sign':'Script sheaf notation','latex':r'\mathscr{N}; \mathscr{E}xt^1; \mathscr{H}om','evidence':'Looped N, curled E and crossing looped H; the following lower-case letters sit on the baseline.','place':'Extension prose and cohomology displays'},
  {'sign':'Recurring transition glyph','latex':r'\unsure{\eta|n} at first occurrence; \eta thereafter','evidence':'Two linked high-to-low stems, the right one longer; eta is preferred, while cursive n remains allowed.','place':'First isomorphism and obstruction paragraph'},
  {'sign':'Transition decoration','latex':r'\xrightarrow{\sim}','evidence':'Right-pointing head at the end of one shaft and a separate upper wave.','place':'Local-isomorphism display'},
  {'sign':'Target-index uncertainty','latex':r"U'_{\unsure{i|j|k}}",'evidence':'Upright, short upper-right branch and broad right foot are crossed by retraced lower strokes, preventing a definite i/j/k separation.','place':'Target of the local isomorphism'},
  {'sign':'Obstruction map','latex':r'd_2; H^0; H^2','evidence':'Small numeral 2 is lowered after d; the cohomology numerals are raised, with 0 a loop and 2 a hooked upper turn and foot.','place':'Obstruction paragraph and final display'},
  {'sign':'Short obstruction expression after par','latex':r'd_2\eta','evidence':'From the completed half-a reading: d has a tall ascender and low bowl, followed by a small lowered 2. The next glyph has two linked slanting stems with the right descending farther, matching the recurring eta/n form rather than the small loop of opening e. This settled locus was not reopened or recropped.','place':'After par, before où; whole-image bbox [357, 539, 442, 585]'},
  {'sign':'Detached pair of uncertain function','latex':pair,'evidence':'One lower round point and an upper-right oblique oval; their diagonal relation is certain, their textual role is not.','place':'Blank area below and right of the signature'},
 ],
 'abbreviations':[
  {'form':'Rmq','expansion':'remarque'},
  {'form':'Rmqs','expansion':'remarques, only as the alternative reading of the cancelled heading'},
  {'form':'alg','expansion':'algébrique'},
  {'form':'P.','expansion':'Initial before Deligne; the forename is not written'},
 ],
 'slips':[
  'The page writes donné after the feminine subject L\'obstruction; the single final e is preserved without grammatical correction.',
  'The written obstruction is d_2 eta, while the displayed element at the top is e; the notation is preserved without a claim that it is a proved error.'
 ],
 'completion':'Complete diplomatic reading of the assigned page: all visible body text, three displays, interlinear insertion and pointer, overwritten initial, underlined live remark, fully recoverable cancelled heading and live colon, closing, signature, detached marks and archive numeral are covered. Every explicit C doubt has a decision, as do the additional graphic difference and the inspected signature. Remaining uncertainty is marked in place. H is descriptive only. Balance checks, without TeX compilation, follow file creation.'
}
(ROOT/'report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
print(json.dumps({'reading_path':report['reading_path'],'report_path':str(ROOT/'report.json'),'decisions':len(decisions),'unresolved':sum(d['unresolved'] for d in decisions)},ensure_ascii=False))
