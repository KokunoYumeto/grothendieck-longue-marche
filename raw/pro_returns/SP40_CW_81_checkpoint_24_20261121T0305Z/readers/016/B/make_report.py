from pathlib import Path
import json
R=Path('/workspace/scratch/94548b74fbe0/out/readers/016/B')
crops=json.loads((R/'crop_plan.json').read_text())
bycrop={x['path']:x for x in crops}
diffs=[]
def add(id,location,C,H,reading,evidence,confidence,kind,diff_C,diff_H,status=None,crop=None,bbox=None,row=None,part=None,**extra):
    d=dict(id=id,location=location,C=C,H=H,reading=reading,evidence=evidence,confidence=confidence,kind=kind,diff_C=diff_C,diff_H=diff_H,C_doubt_status=status,readers_crop=crop,bbox=bbox,mathematical_consequence=None)
    if row: d['C_source_row']=row
    if part: d['C_source_sublocus']=part
    d.update(extra)
    diffs.append(d)
add('B016-D01','Opening union: corrected subscript of the second Sigma',r'\Sigma_{\deleted{\unsure{2}}1}^+',r'\Sigma_1^+',r'\Sigma_{\deleted{\unsure{2}}1}^+','A thick upright 1 and a broad foot sit over a darker hooked cluster. The remaining hook supports the supplied 2 candidate; its independent outline stays unresolved.','low','omission',False,True,'retained','01_first_sigma_verb.png',[877,117,920,154],'CD01')
add('B016-D02','Opening line: verb before un ouvert',r'\deleted{\unsure{sera|sont}} est','serait',r'\deleted{\unsure{sera|sont}} est','The cluster has superposed low loops and horizontal remnants, with a darker terminal crossed stem. The live est reading is retained; sera and sont remain alternatives for the overlain word. H gives the whole cluster live as serait.','low','deletion state (struck given live or live given struck)',False,True,'retained','01_first_sigma_verb.png',[970,96,1080,137],'CD02')
add('B016-D03','Opening line: far-right connexe',r'\unsure{connexe}','connexe','connexe','The c opening, rounded o, two low n runs and terminal xe run remain visible above the separate lower rule. The word ending is recovered.','high','other',True,False,'resolved','02_top_right_insertion.png',[1460,113,1664,147],'CD03')
add('B016-D04','Right-hand top insertion: sign between X and E',r'X\unsure{/|\setminus}E_{\unsure{2}}',r'X\setminus E_2',r'X\unsure{/|\setminus}E_{\unsure{2}}','The narrow stroke after X is nearly upright and has a slight rising-right inclination. Slash remains the first candidate; the setminus candidate remains supported by the compression. H has the retained alternative as its sole reading.','low','misread symbol or index',False,True,'retained','02_top_right_insertion.png',[1596,176,1656,223],'CD04','a: sign',qualified_H_difference=True)
add('B016-D05','Right-hand top insertion: E subscript at the edge',r'E_{\unsure{2}}',r'E_2',r'E_{\unsure{2}}','A lowered rounded hook reaches the physical right edge. The 2 candidate is retained with the boundary limitation.','low','other',False,False,'retained','02_top_right_insertion.png',[1645,185,1685,225],'CD04','b: subscript 2')
add('B016-D06','Opening third line: cancelled wording after donc',r"\deleted{\unsure{c'est}}",r'\struck{\ill{}}',r"\deleted{\unsure{c'est}}",'An apostrophe-like upright remains above the crossing rule, followed by a low bump and a clear terminal t stem. c\'est remains a qualified recovered reading.','low','readable ink left as \\ill{}',False,True,'retained','03_opening_cancelled_equal.png',[421,281,591,332],'CD05')
add('B016-D07','Opening third line: live word after the cancellation','égale','égal',r'\unsure{égal|égale}','After the acute e, descending g and compressed a, a tall l continues into one low tail and a downhook. This supports égal first; the compact terminal movement leaves égale as a supported alternative.','medium','misread word',True,False,None,'03_opening_cancelled_equal.png',[635,279,777,367])
add('B016-D08','Opening third line: small sign after égal/égale',r'\unsure{à|:}','à',r'\unsure{:|à}','Two discrete dark components are vertically separated. Their visible arrangement supports : first; a contracted à remains an alternative. H\'s à survives in the qualification.','medium','misread symbol or index',True,True,'retained','03_opening_cancelled_equal.png',[811,297,843,335],'CD10','a: sign after égale',qualified_H_difference=True)
add('B016-D09','Opening third line: connective before the final inclusion',r"\unsure{donc|d'où}",'donc',r"\unsure{donc|d'où}",'The d loop and upright are followed by a long low run with a small terminal rise. The inner contracted letters remain unresolved.','low','other',False,False,'retained','04_opening_connective.png',[1108,299,1216,344],'CD10','b: connective')
add('B016-D10','Opening conclusion: abbreviation on its own physical line',r'\unsure{cqfd|qfd}','cqfd',r'\unsure{qfd|cqfd}','One open bowl joins directly to the long descender before f and d. qfd is the first reading; the possible compressed c plus q remains as cqfd.','medium','misread word',True,True,'retained','05_cqfd.png',[241,374,401,525],'CD06',qualified_H_difference=True)
add('B016-D11','First of the two partitions: predecessor in the first Sigma',r'\deleted{\unsure{E}}\Sigma_1^+',r'\Sigma_1^+',r'\deleted{\unsure{E}}\Sigma_1^+','A thin inner upright links the top and bottom portions through the live Sigma. Its middle arm is not separately secure; E remains qualified.','low','omission',False,True,'retained','06_first_partition_overwrite.png',[644,607,708,665],'CD07','a: first partition E')
add('B016-D12','Five-term partition: predecessor in Sigma12',r'\deleted{\unsure{E}}\Sigma_{12}',r'\Sigma_{12}',r'\deleted{E}\Sigma_{12}','The inner upright and a distinct short middle horizontal arm survive beneath the heavier live Sigma diagonals and base. They establish the overwritten E.','high','omission',True,True,'resolved','07_brace_partition_overwrite.png',[1005,889,1078,945],'CD07','b: brace-display E')
add('B016-D13','Lower argument: predecessor below the bar in Sigma12',r'\overline{\deleted{\unsure{E}}\Sigma_{12}}',r'\overline{\Sigma_{12}}',r'\overline{\deleted{\unsure{E}}\Sigma_{12}}','The upper and lower strokes are heavily retraced, with a faint secondary lower run. An independent E outline stays unresolved beneath the live Sigma.','low','omission',False,True,'retained','11_lower_overwrites.png',[1030,2029,1106,2088],'CD07','c: lower-argument E')
add('B016-D14','Lower argument: predecessor in E1 after the cap',r'\deleted{\unsure{\Sigma}}E_1',r'E_1',r'\deleted{\unsure{\Sigma}}E_1','A diagonal joins the top-left part to an inner upper corner, over the live E middle arm. The lower predecessor diagonal is obscured; Sigma remains qualified.','low','omission',False,True,'retained','11_lower_overwrites.png',[1223,2032,1287,2093],'CD07','d: lower-argument Sigma')
add('B016-D15','Initial D of Dans',r'\deleted{\unsure{O}}Dans','Dans',r'\deleted{\unsure{O}}Dans','Several overlapping loops surround the main upright and right bowl. An oval O predecessor remains a candidate; the loop cluster does not settle its full independent form.','low','omission',False,True,'retained','09_dans.png',[274,1211,329,1296],'CD08')
add('B016-D16','Raised word above the cancelled lower expression',r'\unsure{conclurait}','considérant','conclurait','The sequence has a low co opening, compressed nc, one tall l loop, a low u run, and the separated rait ending with the terminal t. The raised word is read conclurait.','medium','misread word',True,True,'resolved','12_conclurait_cancellation.png',[456,2120,794,2170],'CD09')
add('B016-D17','Raised word before conclurait',r'\unsure{en|on}','en',r'\unsure{en|on}','The first letter is a shallow open trough followed by the low n movement. en remains first, with on retained because the initial enclosure is unresolved.','medium','other',False,False,'retained','12_conclurait_cancellation.png',[320,2137,406,2168],'CD11')
add('B016-D18','Final long overbar: first join, predecessor/state',r'\deleted{\unsure{\amalg}}\unsure{\cup|\amalg}',r'\sqcup',r'\deleted{\amalg}\cup','Two uprights and an overhanging straight baseline remain behind a darker rounded lower return. The square join predecessor and the superposed cup are both retained, with the precursor marked deleted.','high','deletion state (struck given live or live given struck)',True,True,'resolved','13_bottom_unions.png',[754,2250,799,2287],'CD12','a: first square-join predecessor',physical_cluster='U1',count_as_C_locus=True,count_as_H_locus=True)
add('B016-D19','Final long overbar: first join, live sign',r'\unsure{\cup|\amalg}',r'\sqcup',r'\cup','A visibly rounded lower curve passes beneath the old straight baseline and returns into the right upright. The live cup is resolved. The H correction for this physical cluster is counted in B016-D18.','high','other',True,False,'resolved','13_bottom_unions.png',[754,2250,799,2287],'CD12','b: first live join',physical_cluster='U1',count_as_C_locus=False,count_as_H_locus=False,parent_difference='B016-D18')
add('B016-D20','Final long overbar: second join, predecessor/state',r'\deleted{\unsure{\amalg}}\cup',r'\sqcup',r'\deleted{\amalg}\cup','The straight baseline projects left from two thin earlier uprights; the darker rounded lower return is separately visible. The predecessor square join is resolved.','high','deletion state (struck given live or live given struck)',True,True,'resolved','13_bottom_unions.png',[875,2249,919,2287],'CD12','c: second square-join predecessor',physical_cluster='U2',count_as_C_locus=True,count_as_H_locus=True)
add('B016-D21','Final long overbar: second join, live sign',r'\cup; doubtful-readings row permits final \amalg',r'\sqcup',r'\cup','The lower return is rounded, with the older straight join still separately traceable. C.tex already prints cup here; the compound doubt-table row is explicitly resolved for this local live sign. The H correction is counted in B016-D20.','high','other',True,False,'resolved','13_bottom_unions.png',[875,2249,919,2287],'CD12','d: second live join',physical_cluster='U2',count_as_C_locus=False,count_as_H_locus=False,parent_difference='B016-D20')
add('B016-D22','Foot: rightmost closing bracket candidate',r'\unsure{\big]}',None,r'\unsure{\big]}','An upper rightward rule with a small upturn and a lower rightward return meet the physical image edge. The joining upright lies at or beyond that edge, so the closing-bracket reading remains qualified.','low','omission',False,True,'retained','14_bottom_rhs_closing.png',[1626,2209,1685,2336],'CD13')
add('B016-D23','First partition row endpoint',r'\Sigma_1^-',r'\Sigma_1^-,',r'\Sigma_1^-','Half a shows the final Sigma1 minus followed by clear paper at the first row endpoint. No comma is retained.','high','other',False,True,None,None,{'image':'half a','origin':[0,0],'box':[940,598,1085,686]})
add('B016-D24','Definition label over equality','def','déf','def','The small e has no separate accent stroke above it. The d ascender and f ascender remain distinct.','high','abbreviation expanded or spelling modernised',False,True,None,'08_definition.png',[794,1033,863,1091])
add('B016-D25','Definition formula endpoint',r'\Sigma_2^-',r'\Sigma_2^- .',r'\Sigma_2^-','The final Sigma2 minus and its subscript are followed by clear paper inside the enlargement. No terminal point is retained.','high','other',False,True,None,'08_definition.png',[1062,1038,1225,1146])
add('B016-D26','Right endpoint of sont ouverts','ouverts','ouverts,','ouverts','The tall terminal t and low s hook finish close to the physical page edge. No separate comma is visible in the supplied image; material beyond the edge cannot be examined.','medium','other',False,True,None,'10_ouverts_endpoint.png',[1485,1216,1685,1293],boundary_limit='Physical right edge prevents inspection beyond the terminal writing.')
add('B016-D27','Top insertion: bent guide below la comp. conn.','Insertion words, no guide path','Insertion words, no guide path','G01 path, with unchanged inserted la comp. conn.','The thin line begins with a downward curve at the left, runs below the raised words, then bends down just before Sigma2. One explicit curved path reproduces it.','high','drawing or diagram',True,True,None,'02_top_right_insertion.png',[1165,174,1401,236],source_components=['G01'])
add('B016-D28','Top right insertion: upper/lower rules and detached return','Inserted de X/E2, no rules','Inserted de X\\setminus E2, no rules','G02a1, G02a2, G02b and G02c around the inserted note','The upper rule has a small interruption; a curved lower rule turns up at the left and reaches the right edge; a detached short return sits below its left end. Four explicit path commands preserve these components. Their precise guiding or framing role remains unassigned.','high','drawing or diagram',True,True,None,'02_top_right_insertion.png',[1524,148,1685,267],source_components=['G02a1','G02a2','G02b','G02c'],role='undetermined guide/frame relation',boundary_limit='Upper and lower rule continuations reach the physical right edge.')
add('B016-D29','Lower cancelled alors and expression: actual crossing curve','Generic deleted annotation','Generic struck annotation','G03 curve across the readable deleted phrase; insertion placed above','A single long curve starts below alors, rises into the formula and continues through the remaining symbols. The TeX draws that curve and uses an invisible deleted copy for its annotation; no extra generic strike is drawn.','high','drawing or diagram',True,True,None,'12_conclurait_cancellation.png',[300,2178,1055,2218],source_components=['G03'])
add('B016-D30','Below/right of avec: detached point','No mark','No mark',r'M01: \unsure{\cdot}, placed below/right of avec','One compact dark round point appears at approximately (429.5,1128.5). The dot candidate is retained locally; its hand, role and surface origin stay unresolved.','high','drawing or diagram',True,True,None,'17_dot_below_avec.png',[426,1125,434,1133],source_components=['M01'],shape_confidence='high',interpretation_confidence='low',hand='undetermined hand')
add('B016-D31','Right margin alongside the third closure row: paired points','No marks','No marks','M02a and M02b: locally unsure graphical cluster','Two separated dark points are visible: an upper oval at about (1625.5,1730.5), and a lower irregular point at about (1620.8,1737.5). Both are drawn once; character, role, hand and surface origin stay unresolved.','high','drawing or diagram',True,True,None,'15_right_pair_marks.png',[1617,1727,1629,1743],source_components=['M02a','M02b'],shape_confidence='high',interpretation_confidence='low',hand='undetermined hand')
add('B016-D32','Above/right of the second cap after Notons aussi que: detached point','No mark','No mark',r'M03: \unsure{\cdot}, positioned above/right of the cap','A compact pointed dark spot is separated from the closure bar below-left and from the E top stroke below-right. Its local dot candidate is preserved; its hand, role and surface origin stay unresolved.','high','drawing or diagram',True,True,None,'16_dot_above_closure.png',[925,1889,934,1901],source_components=['M03'],shape_confidence='high',interpretation_confidence='low',hand='undetermined hand')
# H is a full-text witness. Null in D22 denotes omission of this token, not absent H text.
for d in diffs:
    if d['id']=='B016-D22': d['H']='No closing bracket supplied'

inv=[]
def item(n,kind,pos,words,hand='his hand',**extra):
    d=dict(sheet_kind='text',hand=hand,element=f'B016.I{n:02d}',kind=kind,position=pos,first_words_or_objects=words,transcribed='yes')
    d.update(extra);inv.append(d)
item(1,'text','opening paragraph, four physical lines','et par suite … qfd/cqfd')
item(2,'deletion','opening second Sigma subscript','qualified 2 beneath live 1')
item(3,'deletion','opening verb cluster','qualified sera/sont beneath est')
item(4,'insertion','above contenant and Sigma2 minus','la comp. conn.')
item(5,'drawing','below the preceding insertion','G01 bent guide',source_components=['G01'])
item(6,'insertion','opening second line, right edge','de X / or setminus E, qualified subscript 2')
item(7,'drawing','around the right-edge inserted wording','G02 upper rule in two runs, lower rule, detached lower return',source_components=['G02a1','G02a2','G02b','G02c'])
item(8,'deletion','opening third line after donc','qualified c\'est')
item(9,'text','opening conclusion, separate physical line','qualified qfd/cqfd')
item(10,'text','paragraph before paired partitions',"L'intersection des deux partitions")
item(11,'display','upper middle, two rows','X = Sigma1+ amalg E1 amalg Sigma1-; X = Sigma2+ amalg E2 amalg Sigma2-')
item(12,'deletion','first Sigma of first partition','qualified E predecessor')
item(13,'text','before five-term display','de X est')
item(14,'display','central five-term partition','X = Sigma1+ amalg E1 amalg Sigma12 amalg E2 amalg Sigma2+; overlapping braces Sigma2- above, Sigma1- below')
item(15,'deletion','central Sigma12','resolved E predecessor')
item(16,'text','left of definition','avec')
item(17,'drawing','below/right of avec','M01 locally qualified dot candidate','undetermined hand',source_components=['M01'])
item(18,'display','definition row','Sigma12 def= Sigma1- cap Sigma2-')
item(19,'text','next two physical lines','Dans cette partition … sont fermés, et on a')
item(20,'deletion','initial D of Dans','qualified O predecessor')
item(21,'display','first closure row','Sigma1+ subsetneq its closure subset Sigma1+ cup E1')
item(22,'display','second closure row','closure of Sigma12 subset two closures intersected … subset Sigma12 cup E1 cup E2')
item(23,'display','third closure row','Sigma2+ subsetneq its closure subset Sigma2+ cup E2')
item(24,'drawing','right margin beside third closure row','M02a upper oval point and M02b lower irregular point, locally unsure','undetermined hand',source_components=['M02a','M02b'])
item(25,'text','lower paragraph heading','Notons aussi que')
item(26,'drawing','above/right of second cap in nonempty-intersection display','M03 locally qualified point candidate','undetermined hand',source_components=['M03'])
item(27,'display','lower quarter, two expressions','closure Sigma12 cap E1 ne empty; closure Sigma12 cap E2 ne empty')
item(28,'text','last argument, before and after cancelled phrase','Car si on avait p. ex. … on … closure Sigma1- cap E1 = empty,')
item(29,'deletion','first term of lower hypothesis','qualified E beneath Sigma12')
item(30,'deletion','second factor in lower hypothesis','qualified Sigma beneath E1')
item(31,'insertion','above the cancelled lower phrase','qualified en/on; resolved conclurait')
item(32,'deletion','lower cancelled line','alors Sigma12 amalg E2 amalg Sigma2')
item(33,'drawing','over the preceding cancelled line','G03 single rising cancellation curve',source_components=['G03'])
item(34,'display','foot, bracketed closure calculation','[car closure Sigma1- = … qualified closing bracket')
item(35,'deletion','first join under the long final bar','resolved amalg predecessor beneath cup')
item(36,'deletion','second join under the long final bar','resolved amalg predecessor beneath cup')
item(37,'insertion','underbrace below first component closure in final display','subset Sigma2+ cup E2')
item(38,'text','foot left',"ce qui n'est pas.")
item(39,'text','lower-left archive numbering','15, retained only as archive sheet number comment','undetermined hand')

doubts=[]
for ids,reading,alts,reason in [
(['B016-D01'],'deleted 2 beneath 1',[], 'The hooked predecessor outline is crowded by the live digit.'),
(['B016-D02'],'deleted sera',['sont'],'Superposed lettering obscures the cancelled word.'),
(['B016-D04'],'/',['setminus'],'The nearly upright stroke has only a slight visible inclination.'),
(['B016-D05'],'2',[],'The subscript runs into the physical right edge.'),
(['B016-D06'],"c'est",[],'The cancellation leaves only part of the word visible.'),
(['B016-D07'],'égal',['égale'],'The terminal compressed tail is unresolved.'),
(['B016-D08'],':',['à'],'Two small components permit both the punctuation and contracted-letter readings.'),
(['B016-D09'],'donc',["d'où"],'The inner letters are compressed to a low run.'),
(['B016-D10'],'qfd',['cqfd'],'One visible bowl joins the descender; a compressed initial c remains possible.'),
(['B016-D11'],'E',[],'The surviving upright lacks a separately secure middle arm.'),
(['B016-D13'],'E',[],'Heavy retracing prevents an independent predecessor outline.'),
(['B016-D14'],'Sigma',[],'The upper diagonal remains visible but the lower predecessor portion is obscured.'),
(['B016-D15'],'O',[],'The initial overwritten loops are not separately recoverable.'),
(['B016-D17'],'en',['on'],'The first trough has no secure enclosure.'),
(['B016-D22'],']',[],'The joining upright reaches or lies beyond the physical right edge.'),
(['B016-D30'],'point shape',[],'The shape is supported; hand, role and surface origin remain unresolved.'),
(['B016-D31'],'two point shapes',[],'The two shapes are supported; character, hand, role and surface origin remain unresolved.'),
(['B016-D32'],'point shape',[],'The shape is supported; hand, role and surface origin remain unresolved.')]:
    d=next(d for d in diffs if d['id']==ids[0])
    doubts.append(dict(location=d['location'],reading=reading,alternatives=alts,confidence=d['confidence'] if 'shape_confidence' not in d else 'low',reason=reason,crop=d['readers_crop'],difference_ids=ids))

rowlabels={
'CD01':'first line, subscript', 'CD02':'same line, old word','CD03':'far right line 1',
'CD04':'first insertion at right boundary','CD05':'after donc','CD06':'after inclusion',
'CD07':'first partition, brace display and lower argument','CD08':'before Dans',
'CD09':'above alors','CD10':'after égale and before last inclusion of opening',
'CD11':'above struck alors','CD12':'under long final bar','CD13':'foot, right edge'}
source_rows=[]
for row,label in rowlabels.items():
    local=[dict(difference_id=d['id'],part=d.get('C_source_sublocus','single locus'),status=d['C_doubt_status'],reading=d['reading']) for d in diffs if d.get('C_source_row')==row]
    source_rows.append(dict(source_row_id=row,source_place=label,source_row_count=1,local_decisions=local))
report=dict(
 scan=16,reader='B',start_utc='2026-11-20 16:05:27 UTC',end_utc='2026-11-20 16:23:42 UTC',
 full_image_viewed=True,halves_viewed=True,complete_visual_read=True,
 differences=diffs,doubts=doubts,inventory=inv,
 notes={
  'page_content':'The page continues an argument, sets out two partitions and a five-term partition with overlapping braces, defines Sigma12, then writes closure inclusions and two nonempty-intersection assertions followed by a lower argument. This is an account of the written content only.',
  'author_uncertainty':'No separate authorial question mark or explicit verbal uncertainty was identified on this page. Editorial unsure qualifications identify unresolved ink.',
  'title_date_page_counts':'No title or date is present. The lower-left 15 is retained only as % archive sheet number: 15. H has page{15}; packet metadata identifies our scan 16. No manuscript-page command is supplied.',
  'mathematics_led_reading_decisions':'All signs and words were selected from the visible strokes. No mathematical computation, proof check, equivalence check or repair was performed. The page\'s own lower argument is transcribed without reconstruction.',
  'H_apparatus':'H\'s notes describing the two braces and the lower underbrace are editorial descriptions of drawn content. Their wording is not supplied as manuscript prose. The braces and their labels are retained in the TeX.',
  'square_join_typography':'The live square-bottomed joins of the two partitions and cancelled lower expression have two uprights and an overhanging baseline; reading.tex uses amalg. H\'s sqcup tokens for those same witness loci are handled as typographical notation rather than separate lexical corrections. At the final two overwritten joins the deleted/live states and rounded cup shapes receive separate physical-locus records U1 and U2.',
  'graphical_qualification':'The added M01/M02/M03 point candidates are locally unsure. Their positions are preserved; their hand, character or role and surface origin remain unresolved. G02 preserves observed rule components without assigning a precise framing or guiding role.',
  'placement':'The containing clause and its two inserted phrases are held in a local figure so the guide paths can be retained once. The lower cancelled phrase and raised replacement are likewise one local figure. Every word is present once as visible content; the extra deletion copy is phantom only.',
  'image_delivery':'The full scan was opened once, then half a once, then half b once. The 17 planned crop files were each opened once and delivered successfully. No viewed image was reopened; no locus was recropped.',
  'boundary_limits':'The top right inserted subscript and guide continuations, ouverts endpoint, final bracket and bottom underbrace label approach physical page edges. The crop files include the available source boundary. The mark-only crops intentionally contain their complete isolated clusters and available surrounding blank paper; no nearby text lies within those tight rectangles.',
  'structural_validation':'Direct source checks passed: balanced braces and environments, six paired display delimiters, even dollar delimiters, allowed macro names, 17 existing crop files, all 13 source doubt rows and 21 local statuses, and matching chosen tokens and graphical components. The final TeX body and report comparison fields were also read together. No compilation or render was attempted.',
  'model_effort':'No claim is made about model effort settings.'
 },
 notation=[
  dict(location='opening and all indexed Sigma expressions',sign='Sigma with plus/minus and subscript 1, 2 or 12',latex=r'\Sigma_1^\pm,\Sigma_2^\pm,\Sigma_{12}',evidence='Crossed plus; simple horizontal minus; lowered single 1, curved 2, and paired 12.'),
  dict(location='two partitions and central partition',sign='square join with extended baseline',latex=r'\amalg',evidence='Two uprights with the bottom horizontal extending to each side.'),
  dict(location='central partition',sign='overlapping braces',latex=r'\overbrace{\cdots}^{\Sigma_2^-},\underbrace{\cdots}_{\Sigma_1^-}',evidence='Upper brace reaches through the central component; lower brace begins at that component and extends through the right pair.'),
  dict(location='definition',sign='def over equals',latex=r'\overset{\text{def}}{=}',evidence='d, low e, tall f; two equality bars. No separate accent on e.'),
  dict(location='definition first Sigma12',sign='Sigma top stroke',latex=r'\Sigma_{12}',evidence='The detached upper stroke and lower zigzag form the visible Sigma; no additional closure bar was identified in this crop.'),
  dict(location='three closure rows',sign='closure, strict inclusion, inclusion',latex=r'\overline{\Sigma},\subsetneq,\subset',evidence='Separate horizontal closure rules; outer-row inclusion signs have an added lower crossed stroke; remaining inclusions are curved single signs.'),
  dict(location='nonempty intersections and lower hypothesis',sign='empty-set glyph',latex=r'\varnothing',evidence='Small loop crossed by a long rising-right diagonal.'),
  dict(location='opening insertions',sign='comp. conn.',latex='comp. conn.',evidence='Both abbreviated words have their own trailing points; no expansion is supplied.'),
  dict(location='lower prose',sign='p. ex.',latex=r'p.\,ex.',evidence='Points after p and after ex, with a small intervening gap.'),
  dict(location='final overbar, first and second joins',sign='overwritten square join and cup',latex=r'\deleted{\amalg}\cup',evidence='Old extended straight baselines and uprights survive beneath darker rounded lower returns.'),
 ],
 check_events=[],crops=[{k:v for k,v in c.items() if k!='size'} for c in crops],
 brief_feedback=[
  'A source doubt row can combine predecessor glyph and live replacement state at two nearby joins. CD12 is mapped here to four local decisions under one source-row identity and two physical witness-change clusters.',
  'The right-hand insertion includes a top rule that also lies below connexe. The path is preserved without deciding its exact guiding/framing relation.',
  'Tiny isolated dark points support local dot/graphic candidates but supply no hand, semantic role or surface-origin identification. The available conventions permit their qualified positional retention.'
 ],
 source_doubt_rows=source_rows,
 source_doubt_row_count=len(source_rows),
 local_C_doubt_decision_count=sum(len(x['local_decisions']) for x in source_rows),
 image_log=dict(full=dict(path='J81-02_81_scan016.jpg',views=1,size=[1685,2362]),half_a=dict(path='J81-02_81_scan016_a.jpg',views=1,size=[1685,1261],full_scan_origin=[0,0]),half_b=dict(path='J81-02_81_scan016_b.jpg',views=1,size=[1685,1261],full_scan_origin=[0,1101]),crops=dict(count=17,views_per_file=1,failed_unseen_attempts=0,reopens=0,recrops=0)),
 source_coordinate_policy='All numeric bbox arrays are original full-scan pixel coordinates. Explicit image/box objects identify half coordinates. Path origins and rendering units are declared in reading.tex; observed loci remain separate from drawing rectangles and font extents.'
)
(R/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'differences':len(diffs),'source_doubt_rows':len(source_rows),'local_C_doubt_decisions':report['local_C_doubt_decision_count'],'inventory_items':len(inv),'remaining_doubts':len(doubts)},ensure_ascii=False))
