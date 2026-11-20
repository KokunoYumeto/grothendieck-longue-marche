import json
from pathlib import Path
from datetime import datetime, timezone
from PIL import Image

base=Path('out/readers/scan016/R3')
source='/workspace/scratch/8db4dde48936/sp53_recovery/source/SP53_CW_156-6_scans/J156-6-02_156-6_scan016.jpg'
metadata=json.loads((base/'crop_metadata.json').read_text())
for m in metadata:
    with Image.open(Path('out')/m['output']) as im:
        m['output_size']=list(im.size)
    m['source_size']=[1682,2362]
    m['scale_after_rotation']=m['target_width']/((m['box'][2]-m['box'][0]) if m['rotation']==0 else 310)
    if m['rotation']:
        m.pop('scale_after_rotation')
        m['scale_note']='Width set to 3000 after the permitted crop script rotated the 288 by 168 pixel source rectangle by -8 degrees with an expanded canvas.'
    else:
        m['scale_note']='Horizontal scale is output width divided by original box width; vertical output rounding is recorded in output_size.'
    m['viewed']=True
(base/'crop_metadata.json').write_text(json.dumps(metadata,ensure_ascii=False,indent=2)+'\n')
M={int(m['id'].split('_')[0]):m for m in metadata}
D=[]
def difference(place,c,h,reading,ac,ah,kind,evidence,box,cp=None,confidence='high',marked='no',mathematical=False):
    d={'id':'R3-016-D%02d'%(len(D)+1),'place':place,'c':c,'h':h,'reading':reading,'against_C':ac,'against_H':ah,'kind':kind,'marked_in_H':marked,'confidence':confidence,'evidence':evidence,'crop':M[cp]['output'] if cp else None,'crop_box':M[cp]['box'] if cp else box,'crop_source':source,'mathematical':mathematical}
    if cp and box!=M[cp]['box']:d['locus_box']=box
    D.append(d)

# All recurring alphabet disagreements are separate, located occurrences.
difference('Opening, first word','par','Par','par',False,True,'abbreviation expanded or spelling modernised','Lowercase p has a descending stem and short right arch; no capital upper bowl. Settled from half_a.',[285,153,366,223])
difference('Opening, adjective after simple','directe','évidente','directe',False,True,'misread word','Initial d-like double return joins the dotted i; a short separate r follows, then ecte. There is no separate medial ascending d required by évidente.',[500,220,782,310],1,confidence='medium')
difference('Opening interlinear insertion',r'\inserted{\unsure{déployements|déploiements}}',r'\add{déploiements}',r'\inserted{déployements}',True,True,'abbreviation expanded or spelling modernised','The middle y descends distinctly below the word; the terminal ts and initial acute are visible. The curved insertion guide belongs to this word.',[1205,162,1510,226],2)
difference('Opening, M after tilde F subset',r'M',r'\mathcal{M}',r'\unsure{\mathcal{M}|M}',True,True,'misread symbol or index','Two high peaks, curved trough and long rising entry agree with the cursive M family. The alphabet is underdetermined at this first occurrence; both established candidates are retained. Settled as far as possible from half_a.',[1523,204,1609,286],confidence='medium',mathematical=True)
difference('Opening, compound before first Fig(F)',r'\unsure{multidéployement|multidéployements|multidéploiement|multidéploiements}','multidéploiements','multidéployement',True,True,'abbreviation expanded or spelling modernised','The y has a deep left-returning descender. The word ends with a crossed t and its short foot; there is no distinct following s. The preceding des is retained without grammatical repair.',[948,299,1582,381],3)
difference('Opening, index of Fig(G)',r'M',r'\mathcal{M}',r'\mathcal{M}',True,False,'misread symbol or index','Small M below the g has two peaks and a rising left entry. This occurrence was inspected in half_a; the first-occurrence alphabet doubt governs its typesetting.',[747,585,810,635],mathematical=True)
difference('Opening, index of Fig(F) to the right of <<',r'M',r'\mathcal{M}',r'\mathcal{M}',True,False,'misread symbol or index','Two small peaks below the second Fig are separate from its descending g. Settled from half_a.',[1084,565,1138,615],mathematical=True)
difference('Opening, index of Fig(F) after equals sign',r'M',r'\mathcal{M}',r'\mathcal{M}',True,False,'misread symbol or index','The index is a cursive two-peaked M at the lower right of Fig, not an extra prose letter. Settled from half_a.',[1441,621,1497,672],mathematical=True)
difference('Introductory En termes de M before (1.33)',r'M',r'\mathcal{M}',r'\mathcal{M}',True,False,'misread symbol or index','Large two-peaked cursive M, with rising left entry and curved trough. Settled from half_a.',[856,829,944,912],mathematical=True)
difference('Frame surrounding (1.33)',r'\boxed{...}',r'\boxed{...}','Separate top, left, and bottom strokes; open right side; gaps at both left corners.',True,True,'drawing or diagram','The top stroke extends rightward from above the left side, while the left stroke starts below it. The bottom starts to the right of the left side. No right edge exists. The two halves settle the frame; no crop was needed.',[594,943,1662,1308])
difference('(1.33), initial family F',r'\unsure{\mathcal{F}|\mathscr{F}}',r'\mathfrak{F}',r'\unsure{\mathcal{F}|\mathfrak{F}}',True,True,'misread symbol or index','Broad returning cap with small upper loop, crossing middle arm and left-turning foot. Identity F is clear; mathcal/fraktur remain the established alphabet candidates. The crop does not warrant silently selecting a typeface.',[652,1026,731,1115],4,confidence='medium',mathematical=True)
difference('(1.33), powerset P',r'\unsure{\mathcal{P}|\mathrm{P}}',r'\mathfrak{P}',r'\unsure{\mathcal{P}|\mathscr{P}|\mathfrak{P}}',True,True,'misread symbol or index','Long stem, broad angular descending bowl, small upper loop and lower-left return support the ornamental family rather than a plain roman P. Exact calligraphic/script/fraktur alphabet remains unresolved.',[781,1029,860,1119],4,confidence='medium',mathematical=True)
difference('(1.33), M inside powerset parentheses',r'M',r'\mathcal{M}',r'\mathcal{M}',True,False,'misread symbol or index','Two tall stems with a curved trough and extended rising entry; compared locally with the opening M.',[876,1034,941,1099],4,mathematical=True)
difference('(1.33), ens before de parties','ens','ens.','ens',False,True,'abbreviation expanded or spelling modernised','No period occurs after the terminal stroke of ens before the separated de. The body occurrence ens. has an actual point. Settled from half_a.',[993,1041,1112,1104])
difference('(1.33), M after de parties de',r'M',r'\mathcal{M}',r'\mathcal{M}',True,False,'misread symbol or index','Two high peaks, curved central return and long entrance are separately visible here. Settled from half_a.',[1486,1018,1589,1093],mathematical=True)
difference('(1.33), family F after dans',r'\mathcal{F}',r'\mathfrak{F}',r'\mathcal{F}',False,True,'misread symbol or index','Raised hooked cap, middle arm and returning foot match the first family letter; this is a distinct written occurrence. Settled from half_a.',[1323,1104,1396,1178],mathematical=True)
difference('(1.33), underlining of impliquée',r'\uline{impliquée}','impliquée',r'\uline{impliquée}',False,True,'omission','One separate horizontal line lies under impliquée only. H does not mark or note this underline. Both halves contain the locus.',[1427,1106,1658,1212])
difference('(1.33), opening parenthesis and underlying F',r'(\deleted{\unsure{F}}notée',r'(notée',r'\unsure{\mathord{\rlap{$\deleted{F}$}(}|\mathord{\rlap{$F$}(}}\text{notée}',True,True,'deletion state','A capital F has a stem and two right arms at the same position as the opening curved parenthesis. The F is recoverable, but the heavy overlap does not securely distinguish a canceled F from a live retraced F. Both states preserve the overlap; sequential F and parenthesis would misplace the strokes.',[1233,1189,1284,1244],5,confidence='medium',mathematical=True)
difference('Below (1.33), state of d’interprétation directe','d\'interprétation directe',r'\add{d\'interprétation directe}','d\'interprétation directe',False,True,'insertion or placement','The phrase sits on the main baseline. The curved guide starts with the interlinear à première vue and inserts that phrase before d’interprétation; it does not mark d’interprétation directe itself as an insertion.',[1046,1484,1657,1569],6)
difference('Below (1.33), en termes de / d’','de',"d'",'de',False,True,'misread word','After the looped d, a small separate baseline e survives before the canceled phrase; it is not merely an apostrophe.',[954,1572,1048,1646],6,confidence='medium')
difference('Below (1.33), canceled terminology',r'\deleted{\unsure{notions}\ \unsure{de structure|de théorie}}',r'\struck{\ill{}}',r'\deleted{\unsure{notions}\ \unsure{de structure|de théorie}}',False,True,r'readable ink left as \ill{}','The canceled baseline retains part of notions and tall/crossing strokes in the second component, with structure the first candidate. The horizontal cancellation and superscript replacement obscure enough letters that both C doubts remain. H’s single ill token covers this entire canceled locus and is not split into two substitutions.',[1039,1562,1518,1651],6,confidence='low',marked='yes')
difference('Below (1.33), inserted replacement',r'\inserted{notions ensemblistes}',r'\add{ensemblistes}',r'\inserted{notions ensemblistes}',False,True,'omission','The higher replacement starts with notions and continues through ensemblistes. H supplies only the latter word.',[1093,1547,1656,1625],6)
difference('Below (1.33), word before Mais','familières',r'\ill{}','familières',False,True,r'readable ink left as \ill{}','Long descending initial f, medial l and dotted i, and final ères are readable in half_b. The following full stop is present.',[282,1668,693,1778],marked='yes')
difference('End of paragraph, (grandes) ombres',r'\unsure{ombres}','ombres','ombres',True,False,'misread word','Initial o, compressed m, tall b with lower bowl, then res and the exclamation point are separable in the crop.',[1047,1752,1328,1828],7)
difference('Small parenthetical above lower citation',r'\margin{(et avant d\'introduire $\ll$)}',r'(et avant d\'introduire $\ll$) appended to preceding paragraph',r'\margin{(et avant d\'introduire $\ll$)}',False,True,'insertion or placement','The smaller note is written independently above and to the right of the lower citation, outside the preceding prose baseline. H correctly transcribes its words and parentheses. There is no visible connector establishing a more precise attachment than its proximity to the first donnée.',[1202,1776,1660,1858])
difference('Lower citation, dot after 33',r'\unsure{.}','no dot','.',True,True,'misread symbol or index','A detached dark point is plainly present between the last 3 and the closing vertical/curved stroke.',[1374,1893,1399,1923],8)
difference('Lower citation, closing sign',r'\unsure{)|]}',')',r'\unsure{)|]}',False,True,'misread symbol or index','The long almost straight closing stroke curves left only at its bottom. It lacks an unequivocal top bracket cap, but its nearly vertical body does not decide between ) and ].', [1386,1860,1410,1934],8,confidence='medium')
difference('Lower paragraph, deleted word before premier',r'\deleted{\unsure{tout}}',r'\struck{\ill{}}',r'\deleted{\unsure{tout}}',False,True,r'readable ink left as \ill{}','A tall initial t, a low rounded middle and final upright survive the diagonal strike. Tout is the supported candidate, but the canceled middle is not secure enough to remove the doubt.',[309,1980,430,2038],9,confidence='medium',marked='yes')
difference('Lower paragraph, family F after que',r'\mathcal{F}',r'\mathfrak{F}',r'\mathcal{F}',False,True,'misread symbol or index','Broad hooked cap, crossing arm and leftward lower return identify the same family glyph in half_b.',[468,2033,549,2104],mathematical=True)
difference('Lower paragraph, une famille d’',r'\inserted{une famille d\'}',r'\struck{une famille d\'}',r'\inserted{une famille d\'}',False,True,'deletion state','Une famille d’ is written above the deleted une figure without a cancellation through its own baseline. The heavy strike below crosses une figure. H’s note correctly warns of intertwined interventions, but its formal struck state for the upper wording is not supported.',[684,1995,1026,2061])
difference('Lower paragraph, inserted préadmissibles',r'\inserted{\uuline{pré}admissibles}',r'\add{\emph{préadmissible}}',r'\inserted{\uuline{pré}admissibles}',False,True,'misread word','The final curved/downturned stroke supplies the plural s. Two short underline strokes belong to pré. H’s explicit note already correctly records the double underline under pré; the substantive disagreement here is its missing final s, not the macro used for emphasis.',[1122,1983,1404,2053],10)
difference('Lower paragraph, canceled dans',r'\deleted{\unsure{dans}}',r'\struck{dans}',r'\deleted{dans}',True,False,'misread word','Looped d and the low a/n/s sequence remain below the insertion guide, with a dark cancellation across their lower body.',[1187,2040,1301,2088],10)
difference('Lower paragraph, M after canceled dans',r'M',r'\mathcal{M}',r'\mathcal{M}',True,False,'misread symbol or index','Two narrow peaks joined by a rounded trough; the extended entrance is independent of the deleted dans. This occurrence is also included as adjacent context in crop 10.',[1326,2026,1403,2088],10,mathematical=True)
difference('Left margin, quotation marks around pré',r'``\uuline{pré}\'\'',r'« pré »',r'``\uuline{pré}\'\'',False,True,'other','The marks are raised paired short strokes on either side of pré, not lateral guillemets. Two short underline strokes occur below pré; H’s note accurately records that emphasis.',[98,2063,216,2134])
difference('Lower paragraph, deleted Axiome',r'\deleted{\unsure{Axiome}}',r'\struck{Axiome}',r'\deleted{Axiome}',True,False,'misread word','The capital A and crossed x survive on the left, with the dotted i and rounded ome portions visible between the two heavy cancellation lines.',[308,2106,501,2162],11,confidence='medium')
difference('Lower paragraph, support M','support',r'\uncertain{parties de}','support',False,True,'misread word','The word starts with low s/u, has paired descending p strokes and ends with rt. It occupies one word before M, not parties de. Settled from half_b.',[311,2146,552,2214],marked='yes')
difference('Lower paragraph, M after support',r'M',r'\mathcal{M}',r'\mathcal{M}',True,False,'misread symbol or index','Long rising entry and two peaks with a curved trough, followed by a separate comma. Settled from half_b.',[577,2127,677,2195],mathematical=True)
difference('Lower paragraph, canceled d’où then donc',r'\deleted{\unsure{d\'où}} donc',r'\uncertain{donc} dans',r'\deleted{\unsure{d\'où}} donc',False,True,'deletion state','The canceled word retains a looped d and two raised marks, supporting but not proving d’où. A separate live donc follows. H’s uncertain donc aligns with that live word; its following dans has no corresponding ink. The missing canceled word and extra dans are recorded together, without assigning the one H token to two loci.',[755,2124,1064,2176],12,confidence='medium',marked='yes')
difference('Canceled left marginal note, prose',r'\deleted{\unsure{un ens.|un ensemble} de parties \unsure{fermées} de ...}',r'Note: another marginal note is canceled by hatching; no words transcribed',r'\deleted{un ens de parties \unsure{fermées} de ...}',True,True,'omission','The top line is short un ens, with no further ble sequence or separate point after ens. The middle de parties is recoverable; fermées remains partly obscured by the oblique hatch. H’s note is credited for correctly identifying the canceled physical state.',[42,2182,278,2321],13,confidence='medium')
difference('Canceled left marginal note, final sign',r'\unsure{F|\mathcal{F}|\lbrace}',r'No sign transcribed; canceled note described',r'\unsure{F|\mathcal{F}|\lbrace}',False,True,'omission','Narrow bent stem, short upper hook and middle branch survive at the right of the hatching. An F is first, but ornamental F and an opening brace remain plausible. This separate glyph occurrence is not silently normalized to the body family F.',[277,2207,307,2275],13,confidence='low',mathematical=True)
difference('Last two lines, family F before implies',r'\mathcal{F}',r'\mathfrak{F}',r'\mathcal{F}',False,True,'misread symbol or index','The left body symbol has a wide returning cap, a middle arm and lower leftward foot. It is distinct from the cramped uncertain sign in the adjacent margin. Settled from half_b.',[315,2207,404,2288],mathematical=True)
difference('Last two lines, deleted revient ... d’',r'\deleted{\unsure{revient à|revient} la donnée d\'}',r'\struck{revient à la donnée} d\'',r'\deleted{\unsure{revient à|revient} la donnée d\'}',False,True,'deletion state','The horizontal cancellation extends through the final d and its apostrophe. La donnée is readable; the short à-position before la remains obscured, so the alternative without à is retained. The replacement implique is written above, as both witnesses recognize.',[435,2200,1121,2279],14,confidence='medium')
difference('Last line, M after dans',r'M',r'\mathcal{M}',r'\mathcal{M}',True,False,'misread symbol or index','Two high peaks and a long rising entrance at the final main-text M. Settled from half_b; a portion also appears at the lower edge of crop 14.',[809,2251,880,2311],mathematical=True)
difference('Last line, parenthetical wording','ce sera',r'la rel.',r'ce \unsure{sera|ser.}',True,True,'misread word','The first word is ce. The second resembles the compressed sera at the line end, but its last mark is pointlike; literal ser. remains possible. There is a plain less-than sign with one straight lower bar following it.',[947,2261,1259,2323],15,confidence='medium')
difference('Foot, overlapped closing mark, obliques and numeral',r')\unsure{$\big/\!6\!\big/$}',r') plus note: 16 written below an accolade',r'\unsure{$\mathord{\rlap{$)$}\underset{16}{\big/}}\!\big/$|$\mathord{\rlap{$)$}\underset{6}{\big/}}\!\big/$}',True,True,'misread symbol or index','A large closing curved stroke is crossed/touched by a short upper oblique and is next to a much lighter long oblique. A lower stem and a looped 6-like numeral appear underneath. The stem may be a separate 1, giving 16 as H’s note observes, or an extension of the closing stroke, giving 6. The alternatives preserve this overlap instead of adding sequential independent symbols.',[1263,2243,1342,2346],16,confidence='low',mathematical=False)
difference('Last words on page','lequel sera','lequel se','lequel sera',False,True,'misread word','After lequel, the s/e form is followed by a separate r-like low return and a final short a stroke. The sentence continues off this page; there is no full stop.',[1568,2263,1653,2312],17)

C=[]
def doubt(place,c,reading,disposition,evidence,cp,box=None):
    row={'place':place,'c':c,'reading':reading,'disposition':disposition,'evidence':evidence,'crop':M[cp]['output'],'crop_box':M[cp]['box'],'crop_source':source}
    if box:row['locus_box']=box
    C.append(row)
doubt('Opening insertion',r'\unsure{déployements|déploiements}','déployements','resolved','Deep returning y descender, initial acute and terminal ts.',2)
doubt('Opening compound',r'\unsure{multidéployement|multidéployements|multidéploiement|multidéploiements}','multidéployement','resolved','Deep y; final crossed t has no separate following s. Des is left unchanged.',3)
doubt('(1.33), first family F',r'\unsure{\mathcal{F}|\mathscr{F}}',r'\unsure{\mathcal{F}|\mathfrak{F}}','retained','Family F identity clear; cap, crossing arm and return do not uniquely choose a printed alphabet. Established alternatives used.',4,[652,1026,731,1115])
doubt('(1.33), powerset P',r'\unsure{\mathcal{P}|\mathrm{P}}',r'\unsure{\mathcal{P}|\mathscr{P}|\mathfrak{P}}','retained','Ornamental broad bowl and returning foot oppose plain roman P, while exact ornamental alphabet remains open.',4,[781,1029,860,1119])
doubt('(1.33), F at opening parenthesis',r'\deleted{\unsure{F}}',r'\unsure{\mathord{\rlap{$\deleted{F}$}(}|\mathord{\rlap{$F$}(}}','retained','F is recoverable; its canceled versus live retraced state remains open. Both states overlap the parenthesis.',5)
doubt('Canceled terminology, first word',r'\unsure{notions}',r'\unsure{notions}','retained','Cancellation and interlinear replacement obscure the middle; surviving n/t/i-like components support notions.',6,[1039,1577,1220,1651])
doubt('Canceled terminology, second component',r'\unsure{de structure|de théorie}',r'\unsure{de structure|de théorie}','retained','Tall crossed strokes and ending support structure first, but overwritten middle is insufficient to exclude théorie.',6,[1202,1557,1518,1651])
doubt('End of upper paragraph',r'\unsure{ombres}','ombres','resolved','Initial o, compressed m, tall b, then res are visible.',7)
doubt('Lower citation, point',r'\unsure{.}','.','resolved','Separate dark dot lies after the last 3.',8,[1374,1893,1399,1923])
doubt('Lower citation, closing stroke',r'\unsure{)|]}',r'\unsure{)|]}','retained','Nearly vertical body with a curved left foot; no decisive top cap.',8,[1386,1860,1410,1934])
doubt('Lower paragraph, first cancellation',r'\deleted{\unsure{tout}}',r'\deleted{\unsure{tout}}','retained','Initial t and final upright remain; the middle is crossed and compressed.',9)
doubt('After axiome est',r'\deleted{\illegible{1}}',r'\deleted{\illegible{1}}','retained','Dense repeated horizontal black cancellation leaves no defensible word, even at the one enhanced crop.',10,[1223,1968,1341,1998])
doubt('After ens.',r'\deleted{\unsure{dans}}',r'\deleted{dans}','resolved','Looped d and a/n/s lower strokes are visible beneath the insertion guide.',10,[1187,2040,1301,2088])
doubt('Above support',r'\deleted{\unsure{Axiome}}',r'\deleted{Axiome}','resolved','Capital A, crossed x, i point and rounded ome can be followed between cancellation lines.',11)
doubt('After support M',r'\deleted{\unsure{d\'où}}',r'\deleted{\unsure{d\'où}}','retained','Looped d and two raised marks survive, but the lower ou body lies in the heavy strike.',12)
doubt('Canceled margin opening',r'\unsure{un ens.|un ensemble}','un ens','resolved','The abbreviated ens ends immediately after its s; there is neither a ble sequence nor a separate period.',13,[46,2184,258,2250])
doubt('Canceled margin, third line',r'\unsure{fermées}',r'\unsure{fermées}','retained','Initial f and parts of the ending are readable; diagonal hatching obscures the central and accent sequence.',13,[75,2245,242,2320])
doubt('Canceled margin, last sign',r'\unsure{F|\mathcal{F}|\lbrace}',r'\unsure{F|\mathcal{F}|\lbrace}','retained','Short upper hook, bent stem and middle branch leave all three candidates possible.',13,[277,2207,307,2275])
doubt('Under implique',r'\unsure{revient à|revient}',r'\unsure{revient à|revient}','retained','Revient is largely recoverable; an à immediately before la cannot be securely separated from replacement descenders and the strike.',14,[435,2200,729,2279])
doubt('Closing marker at foot',r'\unsure{$\big/\!6\!\big/$}',r'16|6, below and overlapping the closing stroke, with obliques','retained','Looped 6 survives; adjacent stem can be read as 1 or as continuation of the closing mark. H’s 16 note is plausible, not silently adopted as certainty.',16)

inventory=[]
def item(element,kind,position,first):
    inventory.append({'element':element,'kind':kind,'position':position,'first_words_or_objects':first,'sheet_kind':'text','hand':'his hand','transcribed':'yes'})
item('Manuscript page number','text','top centre, x775–842 y44–96','15')
item('Opening paragraph','text','x285–1658 y125–799','par contre la relation << ... un peu bidon !')
item('Opening word insertion and guide','insertion','x1180–1532 y166–239','déployements')
item('Introductory paragraph before display','text','x306–1468 y832–1021','En termes de M, la structure est donnée par')
item('Numbered definitions, three written rows','display','x311–1658 y1021–1254','(1.33); family F subset P(M); << relation d’ordre; par l’inclusion')
item('Open three-sided display frame','drawing','x596–1659 y950–1299','top, left, bottom strokes, open right side and left-corner gaps')
item('Overlapped F and opening parenthesis','deletion','x1233–1284 y1189–1244','F/(: canceled and live alternatives preserved')
item('Underline in display','text','x1438–1645 y1130–1198','impliquée, one underline')
item('Paragraph following display','text','x284–1659 y1310–1840','Ça a l’air moins sympathique ... (grandes) ombres !')
item('Qualification inserted above interpretation clause','insertion','x949–1334 y1441–1514','à première vue')
item('Canceled terminology after en termes de','deletion','x1039–1518 y1562–1651','notions de structure / de théorie')
item('Replacement terminology','insertion','x1093–1656 y1547–1625','notions ensemblistes')
item('Small independent parenthesis above lower citation','margin note','x1202–1660 y1776–1858',"(et avant d’introduire <<)")
item('Lower paragraph, continuing off page','text','x303–1658 y1860–2344','En termes de la première donnée ... lequel sera')
item('First qualification of donnée','insertion','x945–1122 y1829–1900','première')
item('Canceled first adjective/adverb before premier','deletion','x309–430 y1980–2038','tout, uncertain')
item('Blackened word after est','deletion','x1223–1341 y1968–1998','one illegible canceled word')
item('Canceled original family description','deletion','x678–1002 y2044–2104','une figure')
item('Replacement family description','insertion','x684–1026 y1995–2061',"une famille d’")
item('Inserted qualification after ens.','insertion','x1122–1404 y1983–2053','préadmissibles; pré doubly underlined')
item('Canceled preposition','deletion','x1187–1301 y2040–2088','dans')
item('Left warning note','margin note','x27–239 y2028–2136','attention au ``pré\'\' !; pré doubly underlined')
item('Canceled heading-like word above support','deletion','x308–501 y2106–2162','Axiome')
item('Canceled connective before donc','deletion','x755–891 y2124–2176',"d’où, uncertain")
item('Canceled slanted marginal note','margin note','x23–311 y2171–2339','un ens de parties fermées de F, with stated doubts and diagonal hatching')
item('Cancellation of old implication wording','deletion','x435–1121 y2200–2279',"revient à / revient la donnée d’")
item('Replacement implication verb','insertion','x530–729 y2180–2243','implique')
item('Final parenthetical comparison and attached marker','text','x947–1342 y2243–2346','(ce sera / ser. ≤), overlapped 16 / 6 and oblique marks')
item('Final continuation after dash','text','x1335–1658 y2258–2324','— lequel sera')

unresolved=[
 {'place':'First M after tilde F subset','reading':r'\mathcal{M}','alternatives':['M'],'confidence':'medium','evidence':'Family-like rising entry and paired peaks; exact printed alphabet is not determined by this handwriting.'},
 {'place':'First family F in (1.33)','reading':r'\mathcal{F}','alternatives':[r'\mathfrak{F}'],'confidence':'medium','evidence':'Returning cap and foot establish a family letter, not a unique printed alphabet.'},
 {'place':'Powerset P in (1.33)','reading':r'\mathcal{P}','alternatives':[r'\mathscr{P}',r'\mathfrak{P}'],'confidence':'medium','evidence':'Broad returning ornamental bowl; exact typeface unresolved.'},
 {'place':'Opening parenthesis in last row of (1.33)','reading':'Canceled F overlapped by (','alternatives':['Live/retraced F overlapped with ('],'confidence':'medium','evidence':'Both arms of F survive at the parenthesis stem; no decisive independent cancellation stroke.'},
 {'place':'Canceled terminology, first word','reading':'notions','alternatives':[],'confidence':'low','evidence':'Partly hidden by a horizontal cancellation and the interlinear replacement.'},
 {'place':'Canceled terminology, second component','reading':'de structure','alternatives':['de théorie'],'confidence':'low','evidence':'Crowded tall/crossed strokes remain compatible with both proposed readings.'},
 {'place':'Closing lower citation sign','reading':')','alternatives':[']'],'confidence':'medium','evidence':'Nearly vertical body, left-curving foot, no decisive cap.'},
 {'place':'Deleted word before premier','reading':'tout','alternatives':[],'confidence':'medium','evidence':'Two tall end strokes and a faint/canceled rounded middle.'},
 {'place':'Deleted word after axiome est','reading':r'\illegible{1}','alternatives':[],'confidence':'low','evidence':'Dense black cancellation prevents a word reading at the deepest permitted crop.'},
 {'place':'Deleted word after support M','reading':"d’où",'alternatives':[],'confidence':'low','evidence':'Only d and two raised marks remain distinguishable above the strike.'},
 {'place':'Canceled margin, third line','reading':'fermées','alternatives':[],'confidence':'low','evidence':'Initial and terminal traces survive, but diagonal hatch covers the middle.'},
 {'place':'Canceled margin, last sign','reading':'F','alternatives':[r'\mathcal{F}',r'\lbrace'],'confidence':'low','evidence':'Narrow hooked stem and short middle branch do not settle identity/alphabet.'},
 {'place':'Canceled wording below implique','reading':'revient à','alternatives':['revient'],'confidence':'medium','evidence':'Possible à is crossed by replacement descender/cancellation; la donnée d’ is otherwise recoverable.'},
 {'place':'Final parenthesis, second word','reading':'sera','alternatives':['ser.'],'confidence':'medium','evidence':'Compressed form resembles final sera, but its last mark is pointlike.'},
 {'place':'Foot marker below/at closing stroke','reading':'16','alternatives':['6'],'confidence':'low','evidence':'Looped numeral plus adjacent stem; the latter may belong to closing mark instead of an independent 1. Oblique marks retained.'}
]
notes=[{
 'content':'The page questions the direct interpretability of << in terms of deployments and multideployments, and specifically says that G << F does not imply the corresponding comparison of Fig objects. It then records the data in terms of M: a family of subsets with an order implied by inclusion. The author finds that description less immediately congenial, announces the use of the grandes ombres, and begins a revised first axiom: a family of préadmissible sets of support M gives a preorder in M. The last sentence continues onto another page; that continuation was not consulted.',
 'math_reading_decisions':[
  'The first Fig(F) has no index. The two following Fig terms and the final = Fig(F) each have their own M index.',
  'All ten main-text M occurrences, all four main-text family F occurrences, the single powerset P and the separate uncertain marginal F were recorded individually where witnesses differ.',
  'Subset has no lower equality bar; << has two left-pointing angle components; the two displayed/final non-strict comparisons use a straight lower bar.',
  'The adjective impliquée is underlined, and the order is said to be implied by inclusion, not conversely. This is a reading, not a proof check.',
  'The (1.33) frame is open on the right with separate strokes and left-corner gaps. It is an aligned definition list, not a diagram of relationships.',
  'The lower citation literally has a point after 33; its closing sign remains )/].',
  'Overlapped F/parenthesis alternatives and the foot numeral/closing-stroke alternatives are represented in place; no unsupported predecessor letter was invented.',
  'H is credited for its notes correctly describing double underlining of pré, diagonal cancellation of the lower margin note, and a plausible 16 at the foot.'
 ],
 'author_doubts':[
  "n’a pas d’interprétation simple directe",
  "sont-ils finalement un peu bidon !",
  "Ça a l’air moins sympathique du point de vue simplicité des données",
  "il n’y a pas à première vue d’interprétation directe de << en termes de notions ensemblistes familières",
  "attention au ``pré'' !"
 ],
 'titles_dates_counts':{'manuscript_page':'15','scan':16,'title':None,'date':None,'archive_sheet_number':'No separate archive pencil number identified','display_label':'(1.33)','lower_citation':'(1.33.) or (1.33.]','foot_marker':'16 or 6; not classified as a date or archive number','main_prose_paragraphs':4,'marginal_notes':3,'insertions':7,'definite_canceled_loci':9,'additional_uncertain_canceled_locus':'F overlapped with opening parenthesis in (1.33)','relationship_diagrams':0,'drawings':1,'drawings_description':'three-sided display frame','actual_crops':17,'actual_images_emitted':20}
}]
check_events=[
 {'statement_id':'scan016-opening-Fig-nonimplication','type':'carried as background without fault found','outcome':"read as the author's assertion; no mathematical verification performed"},
 {'statement_id':'scan016-1.33-order-implied-by-inclusion','type':'carried as background without fault found','outcome':"read as the author's assertion; no mathematical verification performed"},
 {'statement_id':'scan016-first-axiom-preorder','type':'carried as background without fault found','outcome':"read as the author's assertion; no mathematical verification performed"}
]
notation=[
 {'sign':'cursive M','latex':r'\unsure{\mathcal{M}|M} at first occurrence; \mathcal{M} thereafter','ink':'Two high peaks, curved trough and long rising entry, including the smaller Fig indices. Ten main-text occurrences inspected.','alternatives':['M']},
 {'sign':'family F','latex':r'\unsure{\mathcal{F}|\mathfrak{F}} at first occurrence; \mathcal{F} thereafter','ink':'Returning cap, crossing middle arm and lower return; four clear main-text occurrences.','alternatives':[r'\mathfrak{F}']},
 {'sign':'powerset P','latex':r'\unsure{\mathcal{P}|\mathscr{P}|\mathfrak{P}}','ink':'Long stem, large angular bowl and lower-left return. One occurrence.','alternatives':[r'\mathscr{P}',r'\mathfrak{P}']},
 {'sign':'ordinary F underlying opening parenthesis','latex':r'\unsure{\mathord{\rlap{$\deleted{F}$}(}|\mathord{\rlap{$F$}(}}','ink':'Two F arms share the parenthesis position.','alternatives':['F canceled beneath (','F live/retraced at (']},
 {'sign':'order symbol','latex':r'\ll','ink':'Two open left-pointing angular components.','alternatives':[]},
 {'sign':'non-strict comparison','latex':r'\leq','ink':'Single left angle with a separate straight lower bar in F ≤ G and in the final parenthesis.','alternatives':[]},
 {'sign':'terminal marker','latex':'Overlapped closing stroke, upper and right obliques, 16/6 below','ink':'One large closing curve, a short oblique above/right, a lighter long oblique on the right, and lower numeral strokes.','alternatives':['16','6; adjacent stem belongs to closing stroke']}
]
report={
 'scan':16,'reader':'R3','started_utc':'2026-11-20T13:11:44Z','finished_utc':datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
 'view_log':json.loads((base/'view_log.json').read_text()),'differences':D,'c_doubts':C,'s_rows':[],
 'inventory':inventory,'notes':notes,'check_events':check_events,'notation_proposals':notation,
 'abbreviations':[{'form':'ens','expansion':'ensemble(s)'},{'form':'ens.','expansion':'ensembles'},{'form':'ser. (uncertain alternative)','expansion':'sera'}],
 'unresolved':unresolved,'brief_feedback':[],
 'crop_count':17,'image_count':20,'coordinate_convention':'All crop_box and locus_box coordinates are [left, top, right, bottom] in the original 1682 by 2362 whole image. For an actual crop, crop_box is the full evidence crop; locus_box, when supplied, is the tighter occurrence within it. For a half-settled locus, crop is null and crop_box is the tight adjudication rectangle.',
 'limitations':['One enhanced crop per still-open locus, with no second crop or second view of a settled image.','Typography and several heavily canceled or overlapped states remain ambiguous and are marked in reading.tex.','No OCR, external research, other pages, other reader files, proof verification or LaTeX compilation was used.','The permitted existing crop_locus.py was called through its documented CLI; its source was not read because it lies outside the packet. Crop coordinates, requested rotation, requested width and resulting pixel dimensions are recorded.'],
 'status':'complete'
}
(base/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'differences':len(D),'c_doubts':len(C),'inventory':len(inventory),'unresolved':len(unresolved),'c_doubts_resolved':sum(x['disposition']=='resolved' for x in C),'crops':len(metadata),'view_log':len(report['view_log'])}))
