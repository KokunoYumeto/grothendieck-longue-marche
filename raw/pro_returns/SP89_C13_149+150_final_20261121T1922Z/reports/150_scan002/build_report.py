import json
from pathlib import Path

root = Path('/workspace/scratch/8759b8008681')
out = root / 'work/reports/150_scan002'
boxes = json.loads((out / 'crop_boxes.json').read_text())
page = '150_scan002'
qword = chr(96) * 2 + "âme''"
changes = []

def change(id, crop_id, place, c, h, final, evidence, confidence, kind,
           against_c, against_h, error_category, marked_in_h=False,
           consequential=False):
    changes.append(dict(
        id=id, place=place, c=c, h=h, final=final, evidence=evidence,
        crop=f'crops/{page}_{crop_id}.png' if crop_id else '../source/SP89_C13_149+150_scans/150_scan002.jpg',
        box=boxes[crop_id] if crop_id else [0, 0, 1916, 2552],
        confidence=confidence, kind=kind, against_c=against_c,
        against_h=against_h, marked_in_h=marked_in_h,
        consequential=consequential, error_category=error_category))

change('P01','P01','L1, date, first abbreviation',
       'déc. 81--janv. 82',r'\uncertain{déc.} 81 -- janv. 82',
       'dec. 81--janv. 82',
       'The d has a tall dark stem, followed by two low joined letters e and c and a separate stop. The space over the e contains no acute stroke. The following numerals have the two loops of 8, a single upright 1, then 8 and the curved-top, flat-foot 2. The unaccented abbreviation is preserved.',
       'high','abbreviation expanded or spelling modernised',True,True,8,True)
change('P02','P02','L2–L3, title and parenthetical subtitle',
       r'\uline{Espaces stratifiés et voisinages côniques}'+'\n\n'+r'(ou : \uline{déploiement} \uline{des espaces stratifiés})',
       '',
       r'\uline{Espaces stratifiés et voisinages côniques}'+'\n\n'+r'(ou : \uline{déploiement} \uline{des espaces stratifiés})',
       'Both title lines are present in the upper right. The first has one continuous underline; the parenthetical second line has separate underlines below déploiement and des espaces stratifiés. The circumflex over côniques is visible. H only refers editorially to a title, without supplying these source words in this packet.',
       'high','omission',False,True,3)
change('P05','P05','L10, second occurrence of the pair of numerals',
       'des strates 2 à 2.','des strates 2 : 2.','des strates 2 : 2.',
       'Between the two flat-foot 2s are two detached compact dots, one directly above the other. There is no lower a body or rightward letter exit. This is a colon; the earlier legend has a different, filled a body with a slanted accent.',
       'high','misread symbol or index',True,False,1)
change('P06a','P06','L13, parenthetical qualification',
       r'(cas \unsure{équisingulier})','(cas équisingulier)','(cas équisingulier)',
       'The initial small e has its acute stroke; the q has an oval and descending stem, and the later g has its separate long descender. The intervening ui/si joins and the final ulier sequence are present. The descending f from fibrations above crosses the q area but is not a cancellation. C certainty resolution.',
       'high','misread word',True,False,2)
change('P06b','P06','Above L12, after fibrations',
       r'fibrations \inserted{(propres)}','fibrations (propres)',
       r'fibrations \inserted{(propres)}',
       'The smaller (propres) lies above the end of fibrations. A long curved leader beneath it terminates downward at the insertion point after that word; it does not strike or underline the text.',
       'high','insertion or placement',False,True,6)
change('P07','P07','L14, coined compound after the fibre formula',
       r'\unsure{fibro-jonction}','fibre-jonction',
       r'\unsure{fibro-jonction|fibre-jonction}',
       'The tall f, dotted i, b stem, short r join, hyphen and jonction are identifiable. The last small vowel before the hyphen is compressed into a dark angular body, so its closure does not safely distinguish o from e. The C first candidate is retained with H explicitly recorded as an alternative; this is an unresolved word disagreement, not a certain correction.',
       'medium','misread word',False,True,2)
change('P08','P08','L16, quotation marks around âme',
       qword,'« âme »',qword,
       'There are two separate upper pen ticks before â and two upper ticks after e. No angular guillemet bodies are drawn. The circumflex of â is separate from the opening quotation ticks.',
       'high','other',False,True,10)
change('P09','P09','L16, formula at the right paper edge and following punctuation',
       r'$\unsure{\Sigma_{ij}}$',r'$\Sigma_{ij}$,',r'$\Sigma_{ij}$',
       'A short dotted i follows the three-stroke capital Sigma. A second, longer descending trace turns left below it, identifying j, although its outer shaft runs at the paper edge. There is no separate comma after this index; the low left-returning stroke belongs to j. C certainty resolution at medium because of the edge.',
       'medium','misread symbol or index',True,True,1,consequential=True)
change('P10a','P10','L20, domain index in the nonsingular b item',
       r'$\Sigma_{\unsure{ik|jk}}\longrightarrow\Sigma_k$',
       r'$\Sigma_{ik}\to\Sigma_k$',
       r'$\Sigma_{ik}\longrightarrow\Sigma_k$',
       'The first subscript character is a short isolated upright with a dot above it. The following k has the long stem and its own low return, which can imitate a preceding j tail. The arrow and target Sigma_k are also visible. C certainty resolution to ik.',
       'high','misread symbol or index',True,False,1,consequential=True)
change('P10b','P10','L20, noun following the arrow formula',
       'fibration :','fibrations :','fibration :',
       'After the t and dotted i the on ending runs to a short downturned terminal. There is no separate s loop before the two dots of the colon. The singular ending differs visibly from the looped final s in fibrations on L12.',
       'high','misread word',False,True,2)
change('P11','P11','L23, punctuation and raised item label after généralement',
       'Plus généralement : a)','Plus généralement, a)',
       r'Plus généralement \unsure{;|:} a)',
       'The compact upper dot is followed below by a larger hooked, left-returning curl, favouring a semicolon over a colon. The a) is a separate raised group to its right. The lower curl could also incorporate an overwritten earlier label. Punctuation and state remain uncertain; neither deletion nor insertion chronology is asserted merely from the dark curl.',
       'medium','other',True,True,10)
change('P13','P13','L29, predicate following the general b formula',
       r'est \unsure{fibrant|fibré},','est fibrant,','est fibrant,',
       'After the f loop and small b belly the low a/n joins continue to a final rising t-like turn before the comma. There is no terminal é loop or acute. The first reading fibrant is resolved at medium because these final joins are compressed.',
       'medium','misread word',True,False,2)
change('P14','P14','L31, last word at the paper edge',
       r'\unsure{initial}','initial',r'\unsure{initia|initial}',
       'The dotted i, low n join, next dotted i and tall t are visible; another dot and a low a-like arch follow. The final curve runs into the paper edge, without an independently visible final l stem. The first candidate records the visible initia-like ending; completion to initial remains only the alternative.',
       'medium','misread word',True,True,2)
change('P15','P15','L33, first upper interval endpoint, revision state',
       r'I_{i_p<\cdot<\unsure{i_{p+1}}}',
       r'I_{i_p<\cdot<i_{p+1}}',
       r'I_{i_p<\cdot<i_{\unsure{\deleted{n}\inserted{p+1}|p+1}}}',
       'After the endpoint i there is a distinct dark upper n-like body and, below it, a p with descender followed by a thick plus/1 group. This may be an upper n cancelled and p+1 inserted below; simple overworking of p+1 remains possible. The outer doubt explicitly retains the revision-state alternative. Neither the upper character nor the chronology is treated as certain.',
       'medium','deletion state (struck given live or live given struck)',True,True,7,consequential=True)
change('P16','P16','L34, faint bottom-left numeral',
       r'\mspage{1}','',r'\margin{1}',
       'A thin pale upper lead and long upright form the numeral 1. Its tone and narrow ductus differ from the dark mathematical writing; authorship is not established by this sheet. The numeral is preserved as a marginal element. C has the same digit; its page-number wrapper is not counted as a textual error.',
       'high','omission',False,True,3)
change('P17',None,'After the last formula, H-only section heading',
       '',r'\section*{Espaces et ensembles préordonnés ; pseudo-partitions}','',
       'The whole-sheet layout and lower native half show the final interval formula and the faint lower-left 1, followed by the paper edge. No words of this section heading occur elsewhere on this sheet. It belongs to H framing, not to this facsimile page.',
       'high','text not on the page',False,True,9)

decision_data = [
 ('M0232','first','équisingulier','P06','high',
  'The initial accented e, descending q, second descending g and final ulier are distinguishable. The upper f descender crossing the q area is not a strike.'),
 ('M0233','undecided',r'\unsure{fibro-jonction|fibre-jonction}','P07','medium',
  'The final vowel before the hyphen is a compressed dark angular body; o/e closure is not secure.'),
 ('M0234','undecided',r'\unsure{en}','P07','medium',
  'The isolated continuation before i,j,k has a low e/n-like join, but its initial body is heavily retraced. No separate crossing stroke proves deletion; neither letter is secure enough to remove the doubt.'),
 ('M0235','first',r'\Sigma_{ij}','P09','medium',
  'A separate short dotted i precedes the longer j descender and leftward bottom return. The outer part of j meets the paper edge.'),
 ('M0236','first','ik','P10','high',
  'The dotted short first stem is i. The long low return belongs to the following k, not to a first-letter j. The entire Sigma_ik to Sigma_k formula was read.'),
 ('M0237','undecided',r'\unsure{I_{i_{n-1}<\cdot<i_n}}','P12','medium',
  'The full j-membership formula is visible. In the last interval the small n, dash and 1-like trace are crowded below i and near the edge; n−1 is plausible but its individual boundaries remain insecure.'),
 ('M0238','first','fibrant','P13','medium',
  'The final low a/n joins and rising t-like end favour fibrant; no terminal é loop or acute is visible. The complete preceding map formula was also read.'),
 ('M0239','undecided',r'\unsure{initia|initial}','P14','medium',
  'The visible ending reaches a low a-like arch, then the paper edge; there is no independent final l shaft. The complete-word alternative stays uncertain.'),
 ('M0240','undecided',r'i_{\unsure{\deleted{n}\inserted{p+1}|p+1}}','P15','medium',
  'The whole last formula shows a dark upper n-like body above a lower p+1-like group. Both the reading and possible cancellation/replacement state remain under the explicit outer doubt.')
]
decisions = [dict(id=i,cote='150',scan='2',decision=d,reading=r,evidence=e,
                  crop=f'crops/{page}_{p}.png',box=boxes[p],confidence=c)
             for i,d,r,p,c,e in decision_data]

inventory_data = [
 ('E01','text','top left, x407–789 y42–157','dec. 81--janv. 82','his hand'),
 ('E02','text','upper right, x986–1916 y58–157','Espaces stratifiés et voisinages côniques; continuous underline','his hand'),
 ('E03','text','under title, x1090–1916 y157–246','(ou : déploiement des espaces stratifiés); two underline spans','his hand'),
 ('E04','diagram','centre-left, x422–1210 y330–859','Seven Sigma objects; nine arrows, five with hooks; three parenthesised F labels; two cart. labels','his hand'),
 ('E05','display','right of diagram, x1215–1916 y588–940','(i<j<k), brace grouping three legend entries, including des strates 2 à 2','his hand'),
 ('E06','text','below legend, x1172–1916 y930–1057','fibres Fij,Fjk,Fik : fibres de raccord / des strates 2 : 2.','his hand'),
 ('E07','text','right, y1060–1177','les flèches hooked arrow sont bordantes; les flèches plain arrow sont des fibrations','his hand'),
 ('E08','insertion','above end of L12, x1760–1916 y1092–1150','(propres), attached after fibrations by a curved leader','his hand'),
 ('E09','text','right, y1147–1205','(cas équisingulier)','his hand'),
 ('E10','text','right, x1165–1916 y1196–1325','(Fijk, fibré sur Fij, fibre Fjk : fibro-/fibre-jonction; uncertain en i,j,k continuation','his hand'),
 ('E11','text','right, y1330–1447','Sigma_i est la strate ... âme ... Sigma_ij; Sigma_j en est la strate déployée ambiante','his hand'),
 ('E12','insertion','above strate in L16, x1346–1472 y1276–1331','déployée, attached between strate and opening quotation ticks','his hand'),
 ('E13','text','right, y1480–1593','Cas non singulier : a) Sigma_i variété à bord ... Sigma_ji (j<i)','his hand'),
 ('E14','text','right, x1244–1916 y1584–1758','b) Sigma_ik to Sigma_k fibration ... réunion des Sigma_ijk pour i<j<k','his hand'),
 ('E15','insertion','between L20–L21, x1515–1665 y1623–1690','compactes, attached after variétés à bord and before the comma/clause','his hand'),
 ('E16','text','right, x1031–1916 y1752–2062','Plus généralement [uncertain punctuation] a) ... cofinal à d ... interval union','his hand'),
 ('E17','text','right, x1047–1916 y2057–2336','b) Sigma_i0...in=Sigma_d to Sigma_i0...ip=Sigma_delta est fibrant ... segment initia/initial','his hand'),
 ('E18','display','lower right, x1014–1748 y2344–2424','j in the union of intervals; first endpoint has uncertain n / p+1 revision','his hand'),
 ('E19','deletion','within first endpoint in final formula, x1228–1283 y2368–2409','Possible upper n cancellation; revision state explicitly uncertain','his hand'),
 ('E20','insertion','same endpoint, lower index group, x1237–1290 y2385–2417','Possible lower p+1 replacement; same outer state doubt as E19','his hand'),
 ('E21','margin note','bottom left, x137–258 y2451–2536','1','thin pale hand; attribution indeterminate')
]
inventory = [dict(scan=page,sheet_kind='text',hand=h,element=e,kind=k,position=p,
                  first_words_or_objects=w,transcribed='yes')
             for e,k,p,w,h in inventory_data]

audit_data = [
 ('B01','handwritten number; C/H different words',[407,42,789,157],'dec. 81--janv. 82'),
 ('B02','C/H different words',[986,58,1916,246],
  r'\uline{Espaces stratifiés et voisinages côniques}'+'\n'+r'(ou : \uline{déploiement} \uline{des espaces stratifiés})'),
 ('B03','handwritten number',[1602,812,1878,866],'des strates 2 à 2'),
 ('B04','handwritten number; C/H different words',[1602,1000,1885,1057],'des strates 2 : 2.'),
 ('B05','insertion',[1760,1092,1916,1150],r'\inserted{(propres)}'),
 ('B06','resolved C doubt',[1547,1147,1916,1205],'(cas équisingulier)'),
 ('B07','C/H different words',[1666,1196,1916,1269],r'\unsure{fibro-jonction|fibre-jonction}'),
 ('B08','retained C doubt',[1678,1272,1762,1319],r'\unsure{en}'),
 ('B09','insertion',[1346,1276,1472,1331],r'\inserted{déployée}'),
 ('B10','C/H different words',[1438,1335,1540,1387],qword),
 ('B11','doubtful formula; less than high confidence departure',[1858,1326,1916,1389],r'$\Sigma_{ij}$'),
 ('B12','doubtful formula; C/H different words; insertion',[1245,1591,1916,1758],
  r'b) $\Sigma_{ik}\longrightarrow\Sigma_k$ fibration : fibres des variétés à bord \inserted{compactes}, le fibré des bords est la réunion des $\Sigma_{ijk}$ pour $i<j<k$.'),
 ('B13','C/H different words; less than high confidence departure',[1031,1752,1379,1820],
  r'Plus généralement \unsure{;|:} a)'),
 ('B14','handwritten number',[1376,1752,1707,1820],
  r'$\Sigma_{i_0i_1\ldots i_n}=\Sigma_d$'),
 ('B15','doubtful formula; handwritten number',[1179,1980,1916,2062],
  r'$j\in I_{<i_0}\amalg I_{i_0<\cdot<i_1}\amalg\cdots\amalg\unsure{I_{i_{n-1}<\cdot<i_n}}$)'),
 ('B16','handwritten number',[1302,2057,1916,2125],
  r'b) $\Sigma_{i_0\ldots i_n}=\Sigma_d\longrightarrow\Sigma_{i_0\ldots i_p}=\Sigma_\delta$'),
 ('B17','C/H different words; less than high confidence departure',[1128,2115,1270,2173],'fibrant,'),
 ('B18','less than high confidence departure',[1812,2218,1916,2286],r'\unsure{initia|initial}'),
 ('B19','doubtful formula; handwritten number; struck passage; insertion; less than high confidence departure',[1014,2344,1748,2424],
  r'$j\in I_{i_p<\cdot<i_{\unsure{\deleted{n}\inserted{p+1}|p+1}}}\amalg\cdots\amalg I_{i_{n-1}<\cdot<i_n}$.'),
 ('B20','margin note; handwritten number',[137,2451,258,2536],'1')
]
audit_boxes = [dict(box=b,kind=k,xyxy=x,reading=r) for b,k,x,r in audit_data]

doubts = [
 dict(place='L14 / P07',reading=r'\unsure{fibro-jonction|fibre-jonction}',alternatives='fibro-jonction | fibre-jonction',
      confidence='medium',reason='The dark final vowel before the hyphen does not separate o from e.'),
 dict(place='L15 / P07',reading=r'\unsure{en}',alternatives='en; exact first letter unresolved',
      confidence='medium',reason='The first body is strongly retraced; no distinct strike establishes a deletion.'),
 dict(place='L23 / P11',reading=r'Plus généralement \unsure{;|:} a)',alternatives='semicolon | colon; lower curl may incorporate an earlier overwritten item label',
      confidence='medium',reason='A compact upper dot and lower hooked mass favour semicolon, but the lower state is not separable. Raised a) is certain; chronology is not.'),
 dict(place='L27 / P12',reading=r'\unsure{I_{i_{n-1}<\cdot<i_n}}',alternatives='I indexed by i_(n−1)<dot<i_n; small internal index remains unresolved',
      confidence='medium',reason='The n, short horizontal and 1-like trace are crowded at the right edge. No mathematical completion is used.'),
 dict(place='L31 / P14',reading=r'\unsure{initia|initial}',alternatives='visible initia-like ending | initial',
      confidence='medium',reason='Final l cannot be independently followed at the paper edge.'),
 dict(place='L33 / P15',reading=r'i_{\unsure{\deleted{n}\inserted{p+1}|p+1}}',
      alternatives='upper n cancelled and lower p+1 inserted | one overworked p+1 without separately established earlier state',
      confidence='medium',reason='Upper and lower bodies are distinct but their order and cancelled reading are not certain.')
]

notes = [
 dict(id='N01',text='The sheet is dated “dec. 81–janv. 82”. This is a mathematical text sheet, not a cover. Its title concerns stratified spaces and conical neighbourhoods, with déploiement as the parenthetical reformulation. The diagram, legend and prose specify deployed strata, connecting tubes, connecting fibres and general flag-indexed boundary/fibration conditions. This reports the source; no theorem has been verified.'),
 dict(id='N02',text='A source-level tension is preserved: the nonsingular b item calls Sigma_ik to Sigma_k a fibration, whereas the diagram gives that arrow a hook and labels the plain arrow from Sigma_ik to Sigma_i by (F_ik). The literal target k is clear and has not been regularised. The Sigma_ji (j<i) boundary expression in the a item is also retained as written.'),
 dict(id='N03',text='The parenthetical F_ijk sentence has no visible closing parenthesis. Its fibro-/fibre-jonction term and the retraced en remain doubtful. In the final interval formula, a possible upper n cancellation and lower p+1 insertion are recorded within a single explicit uncertainty of reading and state; no definite chronology is claimed.'),
 dict(id='N04',text='The lower-left 1 is transcribed as a margin element. Its pale narrow stroke does not establish that it is the author’s own pagination or that it was written with the dated main notes (“dec. 81–janv. 82”). H’s section heading Espaces et ensembles préordonnés ; pseudo-partitions is absent from the whole sheet and is excluded as editorial framing.'),
 dict(id='N05',text='Read the whole source image once, then both supplied native halves line by line against both witnesses, including agreed words. The first half2 tool response was context-truncated before visual receipt; its reissued response supplied the one actual half2 reading. All sixteen saved crops were inspected. Line count 34 counts date, title, subtitle, 30 other textual/display baselines and the marginal numeral; diagram rows and three above-line qualifier insertions are not additional baselines. No OCR, outside research or compilation was used.')
]

notation = [
 dict(form=r'\Sigma_i',meaning='deployed stratum',evidence='The first legend entry calls Sigma_i, Sigma_j, Sigma_k strates déployées.'),
 dict(form=r'\Sigma_{ij},\Sigma_{jk},\Sigma_{ik}',meaning='connecting tubes of pairs of strata',evidence='Second brace entry: tubes de raccord / des strates 2 à 2.'),
 dict(form=r'\Sigma_{ijk}',meaning='junction for i,j,k',evidence='Third brace entry: jonction en i,j,k.'),
 dict(form=r'F_{ij},F_{jk},F_{ik}',meaning='connecting fibres',evidence='The explicit fibre legend names these three, providing clear F forms beside heavily retraced diagram labels.'),
 dict(form=r'\hookrightarrow',meaning='bordante arrow',evidence='L11 explicitly says les flèches [hooked arrow] sont bordantes. Five diagram arrows carry source hooks.'),
 dict(form=r'\longrightarrow',meaning='fibration arrow, with properness inserted and equisingular parenthesis',evidence='L12–L13 give fibrations, inserted (propres), and (cas équisingulier). Four diagram arrows are plain.'),
 dict(form=r'\Sigma_{i_0i_1\ldots i_n}=\Sigma_d',meaning='flag-indexed generalised stratum',evidence='General a) identifies the indexed Sigma with Sigma_d and subsequently calls d a drapeau.'),
 dict(form=r'\delta',meaning='initial segment of the flag, with the word ending at the edge',evidence='General b) maps to Sigma_delta and later says delta segment initia/initial.'),
 dict(form=r'\amalg',meaning='disjoint-union sign in interval decompositions',evidence='Both final membership formulas have two short upright strokes on a common horizontal base between interval terms.')
]
abbreviations = [
 dict(form='dec.',expansion='décembre'),
 dict(form='janv.',expansion='janvier'),
 dict(form='cart.',expansion='cartésien; labels of the two right-hand diagram squares')
]
hand = [
 dict(habit='Short dotted i versus long left-returning j; k can extend below an adjacent i.',
      places='150_scan002 diagram, P09 and P10',consistency='The distinction recurs in clear diagram and prose indices; the final j in P09 is clipped at the edge.',
      witness_errors='C doubted ik|jk in P10; crop shows the low return belongs to k.'),
 dict(habit='A filled small a with a detached slanted accent can resemble a colon.',
      places='150_scan002 P04 and P05',consistency='P04 has the filled letter body plus accent; P05 has two compact separate dots.',
      witness_errors='C supplies à in the second numeral phrase where the source shows a colon.'),
 dict(habit='Curved under-word leaders carry inserted qualifiers to a lower baseline.',
      places='150_scan002 P06, P08 and P10',consistency='All three leaders terminate at their attachment point and do not cancel text.',
      witness_errors='H gives propres in-line without indicating its inserted state.'),
 dict(habit='Several diagram F stems and an en-like word are heavily retraced.',
      places='150_scan002 P03 and P07',consistency='The diagram F identification is supported by the clear F forms in P05; no underlying cancelled letter is independently legible.',
      witness_errors='No definite error assigned solely from blackness; en remains uncertain.'),
 dict(habit='Double quotation marks are pairs of upper ticks.',
      places='150_scan002 P08',consistency='Both opening and closing pairs around âme have this form.',
      witness_errors='H substitutes guillemets.'),
 dict(habit='Very compressed terminal joins and physical clipping obscure complete endings.',
      places='150_scan002 P07, P13 and P14',consistency='No general ending is inferred from grammar; the final l of initial is not independently visible.',
      witness_errors='H states the complete initial; the draft retains a visible partial-word alternative.')
]

coverage = {
 1:'Source scan marker is metadata. Date is transcribed directly; P01 removes the unsupported acute. H’s introductory editorial prose is excluded.',
 2:'P02 preserves the source title, subtitle and their underlines; H does not give these words directly in this packet.',
 3:'Macro-only diagram column separation; no source-reading difference.',
 4:'Macro-only diagram spacing; no source-reading difference.',
 5:'Same hook arrow, reordered TikZ options; all ends checked in P03.',
 6:'Same hook arrow, reordered TikZ options; all ends checked in P03.',
 7:'Both source cart. labels are set inside the diagram as in C; H describes them editorially. P03 confirms both.',
 8:'H’s explanatory diagram note is not source prose. Seven objects, nine arrows, five hooks and three F labels are retained in the diagram. The parenthesised i<j<k and legend are transcribed.',
 9:'The manuscript has a brace grouping the legend; C’s array/brace preserves that layout. H’s list wrappers are editorial, not words.',
 10:'Continuation of the same brace-versus-list wrapper difference; no source words dropped.',
 11:'P05: the second numeral phrase has 2 : 2. The earlier legend 2 à 2 is separately checked in P04.',
 12:'P07: unresolved fibro-/fibre-jonction difference, both candidates retained in place.',
 13:'P08: double quotation ticks, not guillemets.',
 14:'P09: no separate comma after the edge Sigma_ij; j’s low return is part of the index.',
 15:'The above-line déployée is retained with insertion state and correct attachment; H’s explanatory note is not copied.',
 16:'Sigma_ji (j<i) is read literally. H’s explanatory editorial note is not source text.',
 17:'P10a / M0236: dotted short i and following k; resolve ik.',
 18:'P10b: singular fibration; no s before the colon.',
 19:'P11: source punctuation is a compact upper dot and lower hooked mass; retain unsure semicolon/colon, not H’s bare comma.',
 20:'Macro-only spacing in i_0 i_1; the actual numeric indices are included in B14.',
 21:'P13 / M0238: resolve fibrant at medium from the terminal letter joins.',
 22:'P16 preserves the marginal 1 without attributing authorship. P17 excludes the H-only section heading, absent from this sheet.'
}
diff_coverage = [dict(row=i,disposition=coverage[i]) for i in range(1,23)]

deletion_insertion_review = [
 dict(text=r'\inserted{(propres)}',scope_attachment='The entire parenthetical qualifier is inserted after fibrations on L12.',
      evidence='P06: smaller above-line word and downward-pointing curved leader. The leader is not a strike or underline.'),
 dict(text=r'\inserted{déployée}',scope_attachment='Inserted after strate and before the opening quotation marks around âme on L16.',
      evidence='P08: leader runs beneath the small word and bends down immediately after strate. The later déployée in the Sigma_j sentence is ordinary live baseline text.'),
 dict(text=r'\inserted{compactes}',scope_attachment='Inserted after variétés à bord in nonsingular b), before the comma and le fibré des bords.',
      evidence='P10: curved leader begins at the bord/comma junction and passes beneath the above-line compactes. No part of the following clause is deleted.'),
 dict(text=r'\unsure{;|:} a)',scope_attachment='Punctuation after généralement, followed by a raised a); earlier-state status of the lower curl remains uncertain.',
      evidence='P11: compact upper dot, hooked lower mass, separate raised a). There is not enough separation to assert a cancelled earlier label or a chronological insertion.'),
 dict(text=r'i_{\unsure{\deleted{n}\inserted{p+1}|p+1}}',
      scope_attachment='Possible cancellation/replacement is confined to the subscript of the first upper interval endpoint in the final formula. The parent i, surrounding inequalities and interval union stay live.',
      evidence='P15: distinct dark upper n-like body and lower p+1-like group. The outer doubt includes the no-separate-revision alternative.'),
 dict(text='Diagram F labels; isolated en-like continuation',
      scope_attachment='No certain cancelled text is inferred under the thick F strokes or en-like word.',
      evidence='P03 and P07: retracing follows the letter bodies; no independent crossing stroke or readable abandoned letter establishes a deletion.')
]

check_events = [
 dict(statement_id='150_scan002.N02',type='used and rechecked in this run',
      outcome='Limited internal source comparison: visually compared the diagram’s five source hooks and four plain arrows, its (F_ik) label, the arrow-role sentences, and the later b) formula. The diagram’s Sigma_ik to Sigma_k hook and plain F_ik arrow to Sigma_i differ from the b) wording that calls Sigma_ik to Sigma_k a fibration. This checks the transcribed source roles and identifies an internal tension; it is not a theorem proof, independent re-proof, computation or external validation.')
]

report = dict(page=page,reader='reader_a',line_count=34,changes=changes,
              decisions=decisions,inventory=inventory,audit_boxes=audit_boxes,
              doubts=doubts,notes=notes,check_events=check_events,notation=notation,
              abbreviations=abbreviations,hand=hand,diff_coverage=diff_coverage,
              deletion_insertion_review=deletion_insertion_review)
(out / 'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(crops=len(boxes),changes=len(changes),marks=len(decisions),
                      inventory=len(inventory),audit_boxes=len(audit_boxes),
                      doubts=len(doubts),diff_rows=len(diff_coverage))))
