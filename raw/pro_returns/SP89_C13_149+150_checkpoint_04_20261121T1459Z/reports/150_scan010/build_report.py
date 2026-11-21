from pathlib import Path
import json
R=Path('/workspace/scratch/8759b8008681')
D=R/'work/reports/150_scan010'
C=(R/'packets/150_scan010/C.tex').read_text()
H=(R/'packets/150_scan010/H.tex').read_text()
F=(D/'draft.tex').read_text()
boxes=json.loads((D/'crop_boxes.json').read_text())
def chunk(s,a,b):
 i=s.index(a);return s[i:s.index(b,i)+len(b)]
figure_c=chunk(C,r'\figure{',r'\end{tikzpicture}}')
figure_f=chunk(F,r'\figure{',r'\end{tikzpicture}}')
figure_h=chunk(H,r'\drawing{',r'« $X_{12}$ ».}')
changes=[]
def change(id,p,place,c,h,f,evidence,kind,ac,ah,confidence='high',consequential=False):
 assert c in C,(id,'C',c)
 assert h in H,(id,'H',h)
 assert f in F,(id,'F',f)
 cats={'drawing or diagram':4,'misread symbol or index':1,'omission':3,'other':10}
 changes.append(dict(id=id,place=place,c=c,h=h,final=f,evidence=evidence,crop=f'crops/150_scan010_{p}.png',box=boxes[p],confidence=confidence,kind=kind,against_c=ac,against_h=ah,marked_in_h=('\\uncertain' in h or '\\ill' in h),consequential=consequential,error_category=cats[kind]))
change('P01a','P01','Complete drawing: pen gap, point shapes, contour return and line geometry',figure_c,figure_h,figure_f,'The central filled point is vertically oval and separated from the radial stroke by a small white gap. The outer contour has a short inward pen return at its upper-left side. Three distinct right-going strokes meet the oval at different heights; the middle exterior stroke is substantially heavier than the interior radius and the two outer strokes. The slightly uneven paths and rounded ends are preserved. H gives the broad incidence in prose; this collation records its omission of the pen gap, vertically oval point and contour return. The stated error concerns those material drawing details, not the broad incidence described by H.','drawing or diagram',True,True)
change('P02a','P02','Underline beneath the right-hand X of the central equality',r'\uline{X}_0^*',r'X_0^{*}',r'\uline{X}_0^*','A separate dark horizontal stroke lies beneath the right-hand X, with a short upward return at its left end. It is distinct from both the equals sign and the zero. Both X symbols in the equality are underlined; H omits the second underline.','misread symbol or index',False,True,consequential=True)
change('P03a','P03','Underline retained in the starred candidate for the retraced right-hand label',r'\uline{X}_1^*',r'\uncertain{$X_1^*$}',r'\uline{X}_1^*','The horizontal bar below X is clear independently of the blackened group above and beside the final 1. Therefore both the unstarred and starred candidates keep the underline. This collation concerns H’s un-underlined starred alternative, not a resolution of the doubtful star.','misread symbol or index',False,True,consequential=True)
change('P04a','P04','Thin lower-left foliation and its short lower stroke',r'\margin{9}','',r'\margin{\unsure{\uline{9}|9}}','The thin hand forms a closed upper loop and a long descending hooked tail, giving 9. A short horizontal graphite-like stroke lies separately below the tail; it is differently oriented from the diagonal corner crease. It is retained as an underline at medium confidence. H omits the foliation.','omission',True,True,confidence='medium')

decisions=[
 dict(id='M0305',cote='150',scan='10',decision='undecided',reading=r'\unsure{0}',evidence='The first lowered body has a rounded filled contour compatible with 0, but the overtracing leaves no stable inner loop. The adjacent clear zero supports the candidate without making the obscured digit certain. The whole equality, its two underlines and right-hand star were inspected together.',crop='crops/150_scan010_P02.png',box=boxes['P02'],confidence='low'),
 dict(id='M0306',cote='150',scan='10',decision='undecided',reading=r'\unsure{\uline{X}_{\unsure{}1}|\uline{X}_1^*}',evidence='Underlined X and the final 1 are secure. The large blackened mass above and to the left of the 1 does not separate into a distinct star or a securely identifiable cancelled token. A present unreadable group is explicitly retained before the final 1, with a comment recording its extension above/left and the lack of an established cancellation state. The starred whole-label reading remains the alternative; neither uncertain form is resolved.',crop='crops/150_scan010_P03.png',box=boxes['P03'],confidence='low'),
]

inventory=[]
def inv(e,k,pos,words,hand='his hand'):
 inventory.append(dict(scan='150_scan010',sheet_kind='reused_typed',hand=hand,element=e,kind=k,position=pos,first_words_or_objects=words,transcribed='yes'))
inv('E01','drawing','upper part of sheet, approximately [334,126,857,405]','Irregular closed oval; vertically oval central filled point; radial stroke with a small pen gap; filled boundary junction; three right-going strokes, the middle one thick')
inv('E02','text','above drawing, [671,29,735,108]',r'X_2^*')
inv('E03','text','inside oval beneath the central point, [382,261,501,314]',r'\uline{X}_{\unsure{0}}=\uline{X}_0^*')
inv('E04','text','just below the middle boundary junction, [589,265,645,299]',r'X_{01}')
inv('E05','text','above upper exterior stroke, [704,188,768,220]',r'X_{12}')
inv('E06','text','below thick exterior stroke, [720,266,792,305]',r'\unsure{\uline{X}_{\unsure{}1}|\uline{X}_1^*}')
inv('E07','text','below lower exterior stroke, [704,324,768,359]',r'X_{12}')
inv('E08','margin note','extreme lower left, [131,2147,176,2205]',r'\unsure{\uline{9}|9}',hand='another or undetermined hand: thin grey foliation')

audits=[
 dict(box='B01',kind='drawing|handwritten number|doubtful formula',xyxy=boxes['P01'],reading=figure_f),
 dict(box='B02',kind='doubtful formula|handwritten number',xyxy=[382,261,501,314],reading=r'\uline{X}_{\unsure{0}}=\uline{X}_0^*'),
 dict(box='B03',kind='doubtful formula|handwritten number|less than high confidence departure',xyxy=[720,266,792,305],reading=r'\unsure{\uline{X}_{\unsure{}1}|\uline{X}_1^*}'),
 dict(box='B04',kind='margin note|handwritten number|less than high confidence departure',xyxy=[131,2147,176,2205],reading=r'\unsure{\uline{9}|9}'),
 dict(box='B05',kind='handwritten number',xyxy=[671,29,735,108],reading=r'X_2^*'),
 dict(box='B06',kind='handwritten number',xyxy=[589,265,645,299],reading=r'X_{01}'),
 dict(box='B07',kind='handwritten number',xyxy=[704,188,768,220],reading=r'X_{12}'),
 dict(box='B08',kind='handwritten number',xyxy=[704,324,768,359],reading=r'X_{12}'),
]
doubts=[
 dict(place='P02 / M0305, first index of the central equality',reading=r'\uline{X}_{\unsure{0}}=\uline{X}_0^*',alternatives='The first lowered digit is obscured by filling/retracing; no alternative digit is securely recoverable.',confidence='low',reason='The outer rounded body is compatible with 0, but the inner opening is filled. The clear zero on the right is not used to force a source repair.'),
 dict(place='P03 / M0306, right-hand label beneath thick stroke',reading=r'\unsure{\uline{X}_{\unsure{}1}|\uline{X}_1^*}',alternatives='A star may lie within the blackened mass, or the mass may be retracing of an earlier index/mark. Exact earlier state is unrecoverable.',confidence='low',reason='There is no distinct star outline or independent cancellation stroke. The underlined X and final 1 survive. Empty-content unsure records the intervening unreadable group, with the starred whole-label alternative retained.'),
 dict(place='P04, stroke beneath thin foliation 9',reading=r'\unsure{\uline{9}|9}',alternatives='Un-underlined 9 if the lower short stroke is associated with the corner crease rather than the foliation.',confidence='medium',reason='The lower horizontal segment has a graphite-like tone and is separate from the numeral’s tail, but lies near a folded corner. The preferred underlined reading remains below high confidence.'),
]
notes=[
 dict(id='N01',text='The foreground of this portrait leaf contains one drawing with six mathematical labels and a separate thin lower-left foliation 9. The broad black diagram ink is distinct from the pale mirrored reverse-side typescript visible through the paper. That show-through, the perforations, stains, folds and loose paper edge are not additional foreground writing. No source prose, title or theorem statement appears on this face. H’s descriptive notes, its comparison with another page and its following section heading are editorial and are not transcribed or used to inspect any other page.'),
 dict(id='N02',text='The drawing is reconstructed as an irregular closed oval with three right-going exterior strokes attached at distinct heights. The middle exterior stroke is much thicker and continues the thinner interior radial segment through a filled boundary junction. The interior central point is a vertically elongated filled mark separated from the radial segment by a small actual pen gap; that gap is preserved without inferring that the intended mathematical object is disconnected. The upper-left contour has a short inward return, and the finite drawn ends have no secure arrowheads.'),
 dict(id='N03',text='Geometric diagnostic: the only closed path explicitly drawn is the oval contour. The two exterior flank strokes and the middle exterior stroke do not return or connect at their visible ends, so they add no second closed loop. There are two filled geometric points, at the interior marked location and the middle boundary junction. The stars in X_2-star and the central right-hand X_0-star are label characters rather than additional points. This is a check of the depicted incidence and ink, not a verification of a theorem or a definition of the X notation.'),
 dict(id='N04',text='The labels use the written indices 0, 1 and 2, including X_{01} beside the middle boundary junction and X_{12} beside each flank stroke. The central equation has two underlined X symbols; the right-hand exterior label also has a clear underline despite its obscured higher/lowered mass. The page supplies no definition of the underline, star or indexed X objects. Their apparent relation to geometric strata is not used to resolve the blackened first zero or to supply a star in the right-hand label.'),
 dict(id='N05',text='The original image dimensions are 1708 by 2305 pixels. The whole image and each supplied native half were read once. Four stable crops P01–P04 were created and inspected; no OCR, recognition library, outside research, other page image/witness/report, TeX compilation or recropping was used. All 13 page-specific TSV rows were read as literal tab-separated physical rows. Line_count=6 counts the six written mathematical label units; the separate foliation and picture strokes are not running text lines.'),
]
checks=[
 dict(statement_id='150_scan010.N03',type='used and rechecked in this run',outcome='Manually checked the source incidence and reconstruction: one closed oval contour, three distinct exterior attachments, one interior radial segment, two filled geometric points, and no secure arrowheads. Label stars were excluded from the point count.'),
 dict(statement_id='150_scan010.N04',type='carried as background without fault found',outcome='The suggested stratified-space interpretation is not promoted to a proved assertion: this leaf supplies labels and a drawing but no definitions or theorem to establish. Both obscured label readings remain doubtful.'),
]
notation=[
 dict(form=r'\uline{X}_{\unsure{0}}=\uline{X}_0^*',meaning='central equation written beneath the interior filled point; first lowered digit remains doubtful',evidence='P02: separate lower strokes beneath both X bodies; clear right-hand round zero and crossed star; first index almost solidly filled.'),
 dict(form=r'X_2^*',meaning='label above the entire drawing; no local definition supplied',evidence='P01: two crossing X diagonals, lowered hooked 2 with a base, and a separate raised crossed/starred mark.'),
 dict(form=r'X_{01};\ X_{12}',meaning='written labels beside the middle boundary junction and the two flank strokes respectively; no construction is defined on this leaf',evidence='P01: 01 has a small oval followed by upright 1; each 12 has an upright 1 followed by a curved 2 with a base.'),
 dict(form=r'\unsure{\uline{X}_{\unsure{}1}|\uline{X}_1^*}',meaning='uncertain label beneath the thick right-going stroke; underlined X and final 1 secure, intervening overtraced group unrecoverable, starred whole-label alternative unresolved',evidence='P03: distinct horizontal underline, legible terminal 1, and a substantial blackened body extending above/left of 1. An empty-content doubt marker records its presence and location without supplying a token or cancellation state.'),
]
hand=[
 dict(habit='Retracing can fill a digit or merge a possible raised mark with a lowered index',places='P02 first zero; P03 mass beside final 1',consistency='Both occurrences remain doubtful; the adjacent clear zero, one and stars provide comparisons but do not recover the blackened original strokes.',witness_errors='H gives the central first zero without a doubt; C correctly retains a doubt. Both witnesses acknowledge the right-label ambiguity in different forms.'),
 dict(habit='Underlining may be attached to the lower return of a letter or drawn separately below it',places='P02 both central X symbols; P03 exterior X',consistency='Three underlined X bodies are visible; the underbars are kept independently of index and star uncertainty.',witness_errors='H omits the right central X underline and omits the underline in its speculative starred exterior alternative.'),
 dict(habit='Separate thin grey foliation differs from the broad diagram hand',places='P04 lower-left 9',consistency='The numeral’s closed upper loop and descending tail are clear; its short lower stroke is retained with a separate medium-confidence note.',witness_errors='H omits the foliation; C omits the possible underline.'),
 dict(habit='Pen lifts and terminal thickening are not automatically graph disconnections or arrowheads',places='P01–P02 central point/radius gap; three exterior ends',consistency='The small gap is drawn literally, and no unambiguous arrowhead is added.',witness_errors='C joins the radial segment directly to the filled central point; its straight segments and circular point smooth away small source features.'),
]
reviews=[
 dict(text=r'\uline{X}_{\unsure{0}}',scope_attachment='The first subscript is heavily filled/retraced, but no independent cancellation line or separate replacement digit is recoverable.',evidence='P02: dark rounded lowered body beside a live underlined X; the uncertainty stays on the digit.'),
 dict(text=r'\unsure{\uline{X}_{\unsure{}1}|\uline{X}_1^*}',scope_attachment='The blackened mass is explicitly marked by empty-content unsure before 1 within the preferred whole-label candidate. Its extension above/left of 1 is stated in a TeX comment. No cancellation state or old digit is inferred.',evidence='P03: no distinct traversing strike or legible prior symbol separates from the mass; underbar and terminal 1 are clear.'),
 dict(text='Three underlined X symbols and the thin foliation’s lower stroke',scope_attachment='The X underbars lie below live letters and are not cancellations. The lower stroke at 9 is provisionally read as an underline, with its crease-related alternative retained.',evidence='P02, P03 and P04: vertical placement and separation from the relevant character bodies.'),
]
rows=[line.split('\t') for line in (R/'packets/150_scan010/differences.tsv').read_text().splitlines()[1:] if line]
assert len(rows)==13 and all(row[0]=='150_scan010' for row in rows)
coverage={
 1:'Editorial scan marker versus H’s descriptive note; no manuscript prose or cross-page comparison is added.',
 2:'TikZ scale/source-code syntax versus descriptive prose; not a source-text difference.',
 3:'P01a records the actual geometric refinements; code versus prose alone is not counted as an error.',
 4:'P02a: both central X symbols underlined; complete central equation audited in B02. Coordinates are layout code.',
 5:'X_{01} retained beside the boundary junction; coordinate syntax versus description.',
 6:'Same middle-junction/radial/thick-exterior configuration; P01a preserves the actual pen gap and weights.',
 7:'All six labels kept at the written positions, including upper X_{12}; coordinate syntax is not a missing word.',
 8:'M0306 remains undecided; P03a preserves the clear underline, and P03b records the unreadable overtraced group explicitly.',
 9:'H editorial parenthesis about retracing is not source punctuation; the uncertainty is retained in the label.',
 10:'Lower X_{12} retained; coordinate syntax versus descriptive phrase.',
 11:'Two flank strokes retained with their two X_{12} labels; no source prose added.',
 12:'H repeats its diagram description; this is not a second source drawing or extra label.',
 13:'P04a: lower-left foliation 9 retained with its preferred underline; H descriptive repetition and following editorial section heading excluded.',
}
report=dict(page='150_scan010',reader='reader_c',line_count=6,changes=changes,decisions=decisions,inventory=inventory,audit_boxes=audits,doubts=doubts,notes=notes,check_events=checks,notation=notation,abbreviations=[],hand=hand,diff_coverage=[dict(row=i,disposition=coverage[i]) for i in range(1,14)],deletion_insertion_review=reviews)
(D/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print('Report written:',len(changes),'changes,',len(decisions),'marks,',len(audits),'audit boxes,',len(rows),'diff rows')
change('P03b','P03','Explicit location of the unrecoverable overtraced group before the final 1',r'\unsure{\uline{X}_1|\uline{X}_1^*}',r"$\underline{X}_1$ (l'indice est repassé, \uncertain{$X_1^*$})",r'\unsure{\uline{X}_{\unsure{}1}|\uline{X}_1^*}','The substantial blackened body extends above and to the left of the secure final 1, down into its index zone. It cannot be adequately located by a bare star-present/star-absent choice. The preferred candidate explicitly records present unreadable ink before 1; the comment gives its broader vertical extent. The starred whole-label reading remains an alternative. No former digit or established cancellation state is inferred.','omission',True,True,confidence='low',consequential=True)
notes.append(dict(id='N06',text='For the right-hand label, an empty-content doubt marker explicitly records a substantial present overtraced group before the final 1; it does not denote a blank. The adjacent TeX comment states that the group extends above/left of 1 and that no cancellation state is established. The outer doubt retains the starred whole-label alternative. This records the ink without drawing a textual symbol as a picture or inventing a deleted zero. The foliation’s possible underline is also marked in place, with underlined 9 preferred to plain 9.'))
notation.append(dict(form=r'\unsure{} within \uline{X}_{\unsure{}1}',meaning='present unreadable group beside the final index 1, with location and state described in the adjacent TeX comment',evidence='P03: broad overtraced mass extends above/left of the separately legible final 1; no candidate token or cancellation state can be recovered.'))
for row in changes:
 assert row['c'] in C and row['h'] in H and row['final'] in F,row['id']
for d in decisions:
 assert d['reading'] in F,d['id']
report.update(changes=changes,notes=notes,notation=notation)
(D/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print('Final report:',len(changes),'changes,',len(decisions),'marks,',len(audits),'audit boxes,',len(rows),'diff rows')
