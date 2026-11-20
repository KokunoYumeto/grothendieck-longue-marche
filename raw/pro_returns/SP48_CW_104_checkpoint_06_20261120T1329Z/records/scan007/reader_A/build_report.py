from pathlib import Path
from datetime import datetime, timezone
import json

base=Path('SP48_CW_104/records/scan007/reader_A')
root=Path('/workspace/scratch/7178efd1cfac')
cropmeta=json.loads((base/'crop_metadata.json').read_text())
for item in cropmeta:
    item['path']='crops/'+Path(item['path']).name
    item['source']=str(root/item['source'])
    item['viewed_once']=True
    if item['path'].endswith('02_fleche.png'):
        item['coverage_note']='The lower end of the long f descender meets the crop edge. The accent and baseline letters are fully included; the complete word was seen on half a. No recrop or second view was made.'
issues=[]
def add(id,location,C,H,reading,evidence,confidence,diff_C,diff_H,kind,crop,bbox,unresolved=False,marked='no'):
    issues.append(dict(id=id,location=location,C=C,H=H,reading=reading,evidence=evidence,confidence=confidence,diff_C=diff_C,diff_H=diff_H,kind=kind,marked_in_H=marked,crop=('crops/'+crop+'.png') if crop else '',bbox=bbox,unresolved=unresolved))

add('A01','Opening line, modèles accent',r'\unsure{modèles|modeles|modéles}','modèles',r'\unsure{modèles|modéles}',
    'A separate short, almost horizontal arch is plainly present over the e after d. Its direction does not securely distinguish grave from acute; the unaccented candidate is excluded. Final s has a downturned terminal.', 'medium',True,True,'misread word','01_modeles',[774,120,1011,199],True)
add('A02','Opening line, quotation marks around modèles','Two opening and two closing ticks','Guillemets','Two opening and two closing ticks',
    'Each side has two separate short near-vertical strokes; no angle-shaped guillemets are drawn.', 'high',False,True,'other','01_modeles',[783,126,1009,197])
add('A03','Item (i), flèche accent','flèche','flèche',r'\unsure{flèche|fléche}',
    'The detached accent over the first e is a compact near-vertical dark mark. An accent is present, but its grave/acute direction cannot be distinguished securely. The f, looped l, c, high h and terminal e are visible.', 'medium',True,True,'misread word','02_fleche',[432,209,591,317],True)
add('A04','Item (i), final word',r'\unsure{monomorphique}','monomorphique','monomorphique',
    'Half a shows the successive mono/mor humps, p descender, tall h, dotted i, q descender and joined terminal ue. The ending is readable without a further crop.', 'high',True,False,'misread word','',[870,226,1268,349])
add('A05','Item (ii), canceled word',r'\deleted{\unsure{autom|autom.}}','Deleted automorphisme',r'\deleted{autom}',
    'The short canceled group has a initial loop, low u, tall t, small o and final m humps. The stroke ends after that short group; no morphisme sequence survives. No separate terminal stop is visible apart from the deletion stroke.', 'medium',True,True,'abbreviation expanded or spelling modernised','03_autom_end',[402,283,621,369])
add('A06','Item (ii), interlinear replacement end','Inserted end','Inserted end.','Inserted end',
    'Above the strike are a looped e, low n and high d with a right tail; the adjacent blank contains no detached stop.', 'high',False,True,'other','03_autom_end',[449,284,584,331])
add('A07','Example, after définie',r'\unsure{par}','par','par',
    'A long descending p is followed by a very compressed low a stroke and a separate right-curled r. The visible short group supports par; no abbreviation expansion is introduced.', 'medium',True,False,'misread word','04_par',[948,432,1062,538])
add('A08','Definition of tilde D, quotation marks around inclusion','Two pairs of ticks','Guillemets','Two pairs of ticks',
    'Half a shows two small opening strokes before inclusion and two closing strokes before the parenthesis, with no angled chevrons.', 'high',False,True,'other','',[190,659,490,736])
add('A09','Definition of tilde D, first sous objets','sous objets','sous-objets','sous objets',
    'There is a blank gap between sous and objets. The later occurrence below the map has a visible separate hyphen; this first occurrence does not.', 'high',False,True,'abbreviation expanded or spelling modernised','',[648,665,934,752])
add('A10','End of identification sentence, before Soient','No stop after tilde D','Period after tilde D','No stop after tilde D',
    'The final tilded D has its own long baseline; the following blank carries no independent period before the new Soient line.', 'high',False,True,'other','',[1090,716,1184,784])
add('A11','Starred map display','Two rows; M directly below Hom; label at left','Both maps in one row, comma between; M as ordinary subscript','Two rows; M directly below Hom; label at left',
    'Hom(D′,D) points right to tilde D on the upper row. M is directly underneath Hom. The lower row begins u, has a vertical initial bar on its rightward arrow, and ends u(D′). The star label sits separately at the left between row levels. No comma separates the two rows.', 'high',False,True,'insertion or placement','',[198,885,961,1075])
add('A12','After injective par, first reference',r'\unsure{(i)|[i]}','(i)',r'\unsure{[i]|(i)}',
    'The first closing delimiter has a strong horizontal upper return, upright middle and lower left return, making a bracket reading preferable. The opening delimiter is more curved/oblique, so round parentheses remain possible. The following (ii) and comma are clear.', 'medium',True,True,'misread symbol or index','05_references',[680,1126,837,1207],True)
add('A13','Image description, l’ens before canceled fragment','l’ens','l’ens.','l’ens',
    'The final s ends in a connected downturned stroke; the gap before the canceled fragment contains no separate point.', 'high',False,True,'other','',[214,1224,370,1307])
add('A14','Immediately after l’ens, small canceled fragment',r'\deleted{\unsure{de}}',r'Deleted \ill{}',r'\deleted{\unsure{de}}',
    'A very small crossed group retains a small upper counter, a larger lower counter and a rightward terminal. These permit de, but the overstroke obscures the letter junction. The doubt is retained; no word count is invented.', 'low',False,True,'readable ink left as \ill{}','06_cancelled_de',[369,1227,445,1310],True,'yes')
add('A15','Principal symbol in the image subset',r'\unsure{\mathscr L|\Phi|L}_{D\prime}(D)',r'\Phi_{D\prime}(D)',r'\Phi_{D\prime}(D)',
    'A completely closed oval is bisected by a central upright that continues down to a projecting horizontal foot. Both halves of the oval are visible. This is Phi rather than an open script-L loop. D has one prime in the subscript; the argument is plain D.', 'high',True,False,'misread symbol or index','07_phi_M_attachment',[466,1203,710,1309])
add('A16','Small M- and leader beneath Phi / before isomorphes','M inserted below the subset symbol; no M- before isomorphes','M-isomorphes, without an insertion mark',r'\inserted{\(M\)-}isomorphes',
    'The small M is followed by a distinct horizontal hyphen. A curved oblique leader descends from beside it to the gap immediately before isomorphes. The M- is an insertion attached to that word, not a second index below Phi.', 'high',True,True,'insertion or placement','07_phi_M_attachment',[476,1288,807,1407])
add('A17','New paragraph, N after Soit','Plain N',r'\mathbb N','Plain N',
    'The N has one ascending left stroke, one diagonal and one long right stroke. There is no second separated stem. The crossed glyph to its right is a separate character.', 'high',False,True,'misread symbol or index','08_cancelled_I_K',[466,1497,527,1599])
add('A18','Canceled character immediately after that N',r'\deleted{\unsure{I|K}}','Omitted',r'\deleted{I}',
    'Under the crossing zigzags, a long top bar, a central upright and a long bottom bar remain. The diagonals form the cancellation; no separate K branches are needed for the underlying glyph.', 'high',True,True,'deletion state','08_cancelled_I_K',[516,1509,589,1604])
add('A19','Class-set definition, l’ens','l’ens','l’ens.','l’ens',
    'The s ends as a low joined wave. There is no independent point between it and the insertion attachment for préordonné.', 'high',False,True,'other','',[641,1510,806,1598])
add('A20','Interlinear préordonné','Inserted préordonné','Parenthesized (préordonné) in line','Inserted préordonné without parentheses',
    'The word stands above the line. A low curved attachment leads into the space between l’ens and des. There are no paired punctuation parentheses enclosing the word.', 'high',False,True,'insertion or placement','',[786,1488,1010,1588])
add('A21','Class-set definition, classes',r'\unsure{classes}','classes','classes',
    'The close view has an open c joined to a tall l and low a loop, followed by compressed double-s contours and a low terminal es group. The whole sequence is readable as classes.', 'medium',True,False,'misread word','09_classes',[1007,1508,1210,1598])
add('A22','Interlinear sentence after d’objets de M',r'\inserted{Il est en fait \uline{ordonné}, \unsure{grâce} à (ii).}','Editorial note: il est en fait ordonné, grâce à (ii), with explanation of interlinearity; no period after preceding M in main text',r'\inserted{Il est en fait \uline{ordonné}, grâce à (ii).}',
    'Half b shows the sentence above Pour, attached after the point following M. Ordonné has its own straight underline. Crop 10 shows the g descender, r/a group, separate curved circumflex and ce terminal in grâce. The sentence ends with a point after (ii). The note is manuscript text, not just editorial commentary.', 'high',True,True,'insertion or placement','10_grace',[720,1572,1558,1655])
add('A23','After Pour, quantifier-like sign',r'\unsure{\forall|\mathrm H}',r'\forall',r'\unsure{\forall|\mathrm H}',
    'There are two outer uprights, a diagonal rising from the lower left to the upper right, and a low horizontal crossbar. The extra right descending stroke leaves the forall/H identity unresolved. The alternatives are retained without relying on the following n.', 'low',False,True,'misread symbol or index','11_quantifier',[990,1622,1082,1704],True)
add('A24','In n membership N, first doubled N',r'\unsure{\mathbb N|N}',r'\mathbb N',r'\mathbb N',
    'Half b shows a separated extra upright/return beside the left stem, with projecting upper and lower bars and the diagonal/right stem still visible. This occurrence is doubled, unlike the N after Soit.', 'high',True,False,'misread symbol or index','',[1235,1624,1300,1703])
add('A25','Canceled letter between un and objet',r'\deleted{\unsure{e}}',r'\struck{s}',r'\deleted{\unsure{e|s}}',
    'The crossed character retains an upper loop and a lower loop with a rightward foot; two diagonals cross it. The lower loop permits e, while the surviving double curvature also permits s. It is not safely resolved to either letter.', 'low',True,True,'deletion state','12_cancelled_e',[1323,1628,1476,1720],True)
add('A26','D_n de [overwritten group] de classe','Deleted D followed by live M','Deleted M, with no live replacement','Deleted D followed by live M',
    'The composite has the curved outer bowl and projecting baseline of D, crossed by an oblique stroke. A superposed M has two high uprights and a low central return. Both contours are retained, with M as the live replacement.', 'medium',False,True,'deletion state','13_D_M',[461,1715,550,1801])
add('A27','Small mark above n after classe',r'\overset{\unsure{\ast|\prime}}{n}','Plain n',r'\overset{\ast}{n}',
    'The detached upper mark has several joined projections: a short upright, a right upper prong, a transverse connection and a lower-left projection. It is not a single prime tick. It sits over the n rather than at the usual far-right prime position.', 'medium',True,True,'omission','14_n_mark',[838,1717,920,1808])
add('A28','First à isom unique près, abbreviation ending','isom without point','isom.','isom without point',
    'The word at the right edge ends in the final m stroke; the remaining gap before the next-line unique has no separate point.', 'high',False,True,'other','',[1435,1736,1607,1804])
add('A29','After first unique près, phrase before donc',r'\unsure{à} cause de (ii),',r'\uncertain{\therefore comme dans (ii)}','à cause de (ii),',
    'The initial à is compressed to a detached accent and a low small body, as elsewhere on this page. The next word has the open c, closed a, low u and terminal se contours of cause. Half b shows the following short de and a comma after (ii). There is no comme dans sequence.', 'medium',True,True,'misread word','15_a_cause',[673,1813,1230,1903],False,'yes')
add('A30','Below the gap between à and cause','Omitted','Omitted','Small isolated down-right stroke, represented literally below the gap',
    'Crop 15 contains one detached, dark oblique stroke below and to the right of the compact à, before the following tilde-D line. It is distinct from the tilde. No linguistic or mathematical role is assigned.', 'high',True,True,'omission','15_a_cause',[741,1878,774,1901])
add('A31','Before the defining equality, l’ens ordonné','l’ens','l’ens.','l’ens',
    'Half b shows no independent point after the final s, before ordonné.', 'high',False,True,'other','',[216,1907,379,1982])
add('A32','Right side of tilde D_n equals',r'\unsure{\mathbb J|\mathbb I}_n','I_n',r'\mathbb J_n',
    'The complete symbol has a long projecting top bar, separated returning stems and a lower curve that turns left and upward. The leftward hook distinguishes J from a straight-foot I; the interior returning contours establish doubling. The following subscript is n. The left D also has a small flattened n joined to its baseline.', 'high',True,True,'misread symbol or index','16_D_J',[778,1881,1035,1996])
add('A33','After the defining equality, défini',r'\unsure{défini}','défini','défini',
    'Half b shows the tall d, separate accent on e, high f with descender, dotted i, low n and final dotted i. The joined middle does not hide a competing letter sequence.', 'high',True,False,'misread word','',[1160,1898,1338,1997])
add('A34','Second à isom unique près, abbreviation ending','isom without point','isom.','isom without point',
    'The second isom ends in a long connected m stroke, with blank space afterward; no detached abbreviation point is visible before the next-line unique.', 'high',False,True,'other','',[1371,1908,1593,1980])
add('A35','Canceled words before live une famille',r'\deleted{\unsure{plus|choisi}, une}\inserted{une}',r'\struck{\ill{}} une',r'\deleted{\unsure{plui|plus}, une}\inserted{une}',
    'The first canceled word has a long initial descender, a tall closed second loop, a low u-like turn and a final short upright with a detached dot above it. This supports plui as the literal first candidate, while plus remains possible if the dot is incidental. Choisi is not supported by the initial contour. A comma and the old une are also crossed; a separate une is written above the old une. The horizontal strike crosses the whole old group.', 'low',True,True,'readable ink left as \ill{}','17_plus_une',[1116,1992,1436,2098],True,'yes')
add('A36','Live word famille',r'\unsure{famille}','famille','famille',
    'Half b shows the long initial f, joined a/m group, i point, two tall l contours and the terminal e stroke. The cancellation belongs to the preceding old phrase, not the live word.', 'high',True,False,'misread word','',[1361,1984,1596,2100])
add('A37','Displayed family at foot',r'(\mathbb J_n)_{n\in\mathbb N}',r'(\widetilde D_n)_{n\in\mathbb N}, inline',r'(\mathbb J_n)_{n\in\mathbb N}, displayed',
    'The family symbol has a top bar, two separated main contours and a large lower hook turning up to the left. There is no D bowl or separate tilde. The index n, the parentheses, and the lower n membership doubled N are all visible. This is independently clear at this occurrence.', 'high',False,True,'misread symbol or index','18_family',[573,2085,862,2199])
add('A38','Footer, d’ens ordonnés','d’ens','d’ens.','d’ens',
    'The terminal s has its own downstroke; the wide gap before ordonnés has no independent point.', 'high',False,True,'other','',[207,2184,419,2260])
add('A39','Footer, indexés',r'\unsure{indexés}','indexés','indexés',
    'Half b shows the initial i point, joined n, high d, crossed x, separate acute stroke over e and terminal s. The plural ending is visible.', 'high',True,False,'misread word','',[748,2193,946,2267])

inventory=[]
def inv(element,kind,position,words,hand='his hand'):
    inventory.append(dict(element=element,kind=kind,position=position,first_words_or_objects=words,sheet_kind='text',hand=hand,transcribed='yes'))
inv('Manuscript folio','text','top centre [827,43,853,84]','1')
inv('Opening sentence','text','upper line [188,111,1438,218]','Soit M une catégorie')
inv('Assumption (i)','text','upper left to centre [202,209,1272,350]','(i) Toute flèche de M')
inv('Replacement of autom','insertion','above item (ii) [449,284,584,331]','end')
inv('Assumption (ii)','text','second assumption line [200,306,1642,396]','(ii) Tout ... d’un élément de M')
inv('Short canceled term in (ii)','deletion','within item (ii) [410,318,619,365]','autom')
inv('Example','text','below assumptions [201,418,1654,539]','Ex : M une catégorie définie')
inv('Subobject-set definition','text','upper middle, three lines [194,549,1658,783]','Pour tout D ∈ Ob M')
inv('Introduction of the map','text','above display [199,770,1336,883]','Soient D′,D ∈ Ob M')
inv('Starred map','display','centre [198,885,961,1075]','Hom_M(D′,D) → tilde D; u ↦ u(D′)')
inv('Injectivity and image description','text','centre below map [211,1120,1589,1421]','est injective par ...')
inv('Canceled fragment after l’ens','deletion','within image description [369,1227,445,1310]','de (uncertain)')
inv('M- prefix insertion','insertion','between subset formula and isomorphes [476,1288,807,1407]','M- with curved attachment before isomorphes')
inv('Canceled first class-set start','deletion','lower middle [324,1432,1163,1501]','Soit K un ens. ordonné')
inv('Préordonné insertion','insertion','above class-set definition [786,1488,1010,1588]','préordonné')
inv('Class-set definition','text','lower middle, two lines [213,1500,1520,1712]','Soit N ... l’ens ... des classes d’isom.')
inv('Canceled I after N','deletion','after first live N [516,1509,589,1604]','I')
inv('Orderedness sentence','insertion','between class-set and Pour lines [720,1572,1558,1655]','Il est en fait ordonné, grâce à (ii).')
inv('Choice and family paragraph','text','lower paragraph [210,1620,1607,2101]','Pour ... n ∈ doubled N, un ... objet D_n')
inv('Canceled letter after un','deletion','before objet [1391,1637,1457,1706]','e/s')
inv('Overwritten D','deletion','after D_n de [461,1715,550,1801]','D')
inv('Live M replacing D','insertion','over the D contour [476,1726,545,1794]','M')
inv('Detached oblique mark','drawing','below gap before cause [741,1878,774,1901]','short down-right stroke')
inv('Canceled words before famille','deletion','near end of paragraph [1116,1992,1436,2098]','plui/plus, une')
inv('Live une above old une','insertion','above canceled group [1243,2012,1370,2049]','une')
inv('Indexed family','display','near foot [573,2085,862,2199]','(doubled J_n) indexed n ∈ doubled N')
inv('Final sentence continuation','text','bottom line [205,2185,1660,2287]','d’ens ordonnés, indexés par l’ensemble ordonné')
inv('Archive sheet number','margin note','bottom left [47,2285,92,2344]','6','unattributed hand (archive numbering)')

notes=[
 'Observation: the page opens with a category M and two numbered assumptions: every arrow is monomorphique, and the corrected end of an object is the identity. These are transcribed statements, not checked mathematical results.',
 'Observation: the author defines the ordered set of subobjects of D, writes the two-row map Hom_M(D′,D) to tilde D, and states that its image is Phi_{D′}(D). The inserted M- belongs before isomorphes.',
 'Observation: the lower paragraph introduces classes of objects, inserts that the resulting set is in fact ordonné thanks to (ii), and states that the family of ordered sets is defined up to unique isomorphism. No proof check was performed.',
 'Own folio 1 is at top centre. A lighter archive number 6 is at bottom left. No date or title is visible.',
 'No explicit verbal author doubt or question mark was found. The above uncertainty marks are reader uncertainty, not manuscript question marks.',
 'The sheet is handwritten throughout. Pale background traces do not supply recoverable additional text; no typed reuse is established.',
 'The old words before famille are retained as plui|plus because the final short upright has a detached dot. No expected French wording was substituted.',
 'A small isolated descending stroke below the gap before cause is preserved as a literal backslash-shaped mark in the transcription, without assigning it a semantic role.',
 'Own crop coverage limitation: in crop 02 the lower end of the f descender meets the lower edge. Half a supplied the complete word; the accent itself is fully within the crop. No extra view or recrop was made.',
 'Text consistency check: reading.tex was compared once with C as text after image viewing. Every substantive change in that diff is covered by the issue register. The final period after doubled N agrees with C and H.',
 'The context row primarily labeled scan 8 was read before the parent removed it; it was excluded from scan-7 evidence. Historical comparisons to scan 6 in the supplied audit were not used as source evidence. No other page was opened.'
]
notation=[
 dict(sign='M, D, D′, Ob',reading='plain capitals and one prime where present',evidence='M has two peaks; D has an upright and right bowl with extended foot; the primes after the first map argument and in the subset index are distinct single strokes.'),
 dict(sign='Tilde D',reading='separate tilde above D',evidence='A detached broad wave stands above each relevant D. In the defining equality the small n is a flattened attached lower-right form.'),
 dict(sign='Subset symbol',reading=r'\Phi_{D\prime}(D)',evidence='Closed oval bisected by a central upright ending on a long foot; no open L loop.'),
 dict(sign='M-',reading='inserted prefix to isomorphes',evidence='A separate hyphen follows M and a descending curved attachment enters immediately before isomorphes.'),
 dict(sign='First N / later N',reading='plain N after Soit; doubled N in the three later set positions',evidence='The first has single stems. Later occurrences have extra returning stems/white channels and projecting bars; each occurrence was checked.'),
 dict(sign='J family',reading=r'\mathbb J_n',evidence='Both defining and displayed occurrences have separate returning stems, a top bar and a lower curve turning left/up. The family occurrence has an especially clear hook.'),
 dict(sign='Quantifier-like sign',reading=r'\unsure{\forall|\mathrm H}',evidence='Two outer uprights, rising diagonal and low crossbar; identity remains ambiguous.'),
 dict(sign='References',reading=r'\unsure{[i]|(i)} followed by (ii)',evidence='The first closing delimiter has an upper horizontal return; first opening is more curved. Other (ii) references have rounded delimiters.'),
 dict(sign='Abbreviations and hyphens',reading='Ex :; end; ens; isom; first sous objets, later sous-objets',evidence='No stop after end, the four live ens groups or either à isom group. A point is visible after ens in the canceled K line and after d’isom. before d’objets. Only the later sous-objets has a hyphen.'),
 dict(sign='Accents',reading='modèles/modéles and flèche/fléche remain locally uncertain; grâce has a visible circumflex',evidence='First accent is nearly horizontal; flèche accent is compact and near-vertical. The grâce accent is a distinct curved cap.'),
 dict(sign='Mark above n',reading=r'\overset{\ast}{n}',evidence='Several short projections are joined in a detached upper mark; it is not a single prime.'),
 dict(sign='Isolated mark',reading='literal down-right stroke below gap before cause',evidence='One detached oblique stroke occurs left of the following tilde and below the phrase; no function inferred.')
]

c_doubts=[
 ('modèles','A01','refined; accent retained, unaccented alternative removed'),
 ('monomorphique','A04','resolved'),('autom / autom.','A05','resolved to visible autom without separate point'),
 ('par','A07','resolved'),('(i) / [i]','A12','retained with bracket candidate first'),
 ('canceled de','A14','retained unchanged'),('script L / Phi / L','A15','resolved to Phi'),
 ('canceled I / K','A18','resolved to I'),('classes','A21','resolved'),('grâce','A22','resolved'),
 ('forall / H','A23','retained unchanged'),('doubled N / N after membership','A24','resolved to doubled N'),
 ('canceled e','A25','refined to e/s'),('star / prime above n','A27','resolved to star-shaped mark'),
 ('à before cause','A29','resolved'),('doubled J / doubled I','A32','resolved to doubled J'),
 ('défini','A33','resolved'),('plus / choisi','A35','refined to plui/plus'),
 ('famille','A36','resolved'),('indexés','A39','resolved')
]
finished=datetime.now(timezone.utc).isoformat()
report=dict(
 scan=7,reader='A',model='GPT-6 Astra Pro',effort='inherited/not exposed',
 started_utc='2026-11-20T12:01:43.882386+00:00',finished_utc=finished,
 views=[str(root/'source/SP48_CW_104_scans'/f'H104-01_104_scan007{x}.jpg') for x in ('','_a','_b')]+[str(root/base/x['path']) for x in cropmeta],
 issues=issues,inventory=inventory,notes=notes,notation=notation,checks=[],crop_count=len(cropmeta),
 brief_feedback='No substantive omission in the brief. The mislabelled scan-8 context row was excluded in accordance with the scan-6 clarification and parent correction. The complete-word crop requirement is useful: the long f in crop 02 reached the edge, which is recorded as a coverage limitation rather than repaired by a forbidden repeat view.',
 source_image_dimensions=[1689,2375],half_image_dimensions={'a':[1689,1267],'b':[1689,1268]},
 crop_metadata=cropmeta,view_delivery_failures=[],
 C_doubt_resolutions=[dict(doubt=d,issue=i,status=s) for d,i,s in c_doubts],
 workflow=dict(independent=True,other_pages_opened=False,other_reader_files_read=False,ocr_used=False,pdf_text_used=False,web_used=False,latex_compiled_or_rendered=False,additional_agents_spawned=False,whole_views=1,half_a_views=1,half_b_views=1,decision_crop_views=18,source_images_preserved=True)
)
assert len(issues)==39
assert len(cropmeta)==18
assert len(report['views'])==21
assert len({x['id'] for x in issues})==len(issues)
for issue in issues:
    l,t,r,b=issue['bbox']
    assert 0<=l<r<=1689 and 0<=t<b<=2375
    if issue['crop']:
        assert (base/issue['crop']).exists()
(base/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
(base/'crop_metadata.json').write_text(json.dumps(cropmeta,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'issues':len(issues),'unresolved':sum(x['unresolved'] for x in issues),'crops':len(cropmeta),'views':len(report['views']),'finished_utc':finished},ensure_ascii=False))
