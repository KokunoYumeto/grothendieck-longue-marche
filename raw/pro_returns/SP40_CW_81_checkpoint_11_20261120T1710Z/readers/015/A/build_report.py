from pathlib import Path
import json
base=Path('/workspace/scratch/94548b74fbe0/out/readers/015/A')
crops=json.loads((base/'crops.json').read_text())
cp={x['path'].split('_',1)[0]:x for x in crops}
diff=[]
def add(id,loc,C,H,reading,evidence,confidence,kind,dc,dh,status=None,crop=None,bbox=None,row=None,**extra):
 d=dict(id=id,location=loc,C=C,H=H,reading=reading,evidence=evidence,confidence=confidence,kind=kind,diff_C=dc,diff_H=dh,C_doubt_status=status,readers_crop=cp[crop]['path'] if crop else None,bbox={'coordinate_system':'full scan; origin upper left','xyxy':bbox} if bbox else cp[crop]['bbox'] if crop else None)
 if row is not None:d['C_source_row']=row
 d.update(extra);diff.append(d)
# Every physical sublocus of the twenty-one actual C source rows.
add('D01a','heading: overwritten predecessor','deleted unsure I|V','struck V',r'\deleted{\unsure{I|V}}','An internal near-upright survives between two transverse strokes; the adjoining V-shaped return overlaps it. The predecessor remains I primary with V retained. H overlaps the alternative, so this is a qualified primary-reading difference.','low','misread symbol or index',False,True,'retained','01',row=1,source_part='predecessor')
add('D01b','heading: word Version','unsure Version','Version','Version','After the crowded initial, the e-r run, raised s turn, i stem, and joined o-n ending are readable.','high','other',True,False,'resolved','01',row=1,source_part='Version')
add('D02','opening indexed family: overwritten letter','deleted unsure Sigma|S before E_i','E_i',r'\deleted{\unsure{\Sigma|S}}E_i','The E has a heavy upright and three bars; a thinner returning diagonal/curved middle remains inside it. Its curvature leaves Sigma/S open. H omits that predecessor.','medium','omission',False,True,'retained','02',row=2)
add('D03','upper-left note: between pour and comp.','tte|toute|tt','uncertain toute',r'\unsure{tte|toute|tt}','The small group has two tall, close strokes and a compressed termination. The joined strokes leave the full and contracted readings open. H toute remains an alternative.','low','abbreviation expanded or spelling modernised',False,True,'retained','04',bbox=[57,526,132,618],row=3)
add('D04','upper-left note: before fermé','unsure non',"uncertain n'est pas",'non','A short two-humped run is visible directly after Sigma_i and beside the intruding main NB; there are no separated apostrophe/tall-t/second-word strokes in this short run.','medium','misread word',True,True,'resolved','04',bbox=[270,583,324,636],row=4)
add('D05','upper-right NB: second Sigma exponent','+|-|*','-',r'\Sigma_i^{\unsure{+|-|\ast}}','The dark patch has a horizontal body and a downward protrusion; the covered centre leaves plus/minus/star candidates. Minus, H’s reading, remains explicitly retained.','low','misread symbol or index',False,True,'retained','05',bbox=[1408,377,1445,409],row=5)
add('D06','upper-right NB: complement after X','Sigma_i|E_i','E_i',r'X\setminus\Sigma_i','The glyph has a top horizontal, a diagonal returning through the middle, and a lower horizontal; its left edge stays open. No upright E stem is visible at this locus.','high','misread symbol or index',True,True,'resolved','05',bbox=[1519,379,1641,430],row=6)
add('D07','condition (b), final E: predecessor','deleted unsure Sigma','E_i',r'X\setminus\deleted{\Sigma}E_i.','Two thin diagonals meet at the right-middle under the heavy E bars, preserving the angular Sigma. The final full stop is also visible farther right.','high','omission',True,True,'resolved','06',row=7)
add('D08','main NB: automatiquement','unsure automatiquement','automatiquement','automatiquement','The pale initial run leads into the crossed t, dotted i, descending q and connected -ment termination. The final t reaches the right scan edge; no extra word is supported after it.','medium','other',True,False,'resolved','07',row=8)
add('D09a','case heading: cancelled parenthetical','deleted unsure (de)','omitted',r'\deleted{\unsure{(\mathrm{de})}}','A small looped upright and low return survive under/at the left of the new (I); crowding prevents a secure complete predecessor.','low','omission',False,True,'retained','08',bbox=[752,1010,817,1068],row=9,source_part='parenthetical')
add('D09b','case heading: overwritten relation','deleted unsure <=|=','omitted',r'\deleted{\unsure{\leq|=}}=2','Two heavy horizontal strokes cover a shorter slanted return between them. The older <= or = cannot be separated securely.','low','omission',False,True,'retained','08',bbox=[821,1027,887,1062],row=9,source_part='relation')
add('D10','drawing: crossed upper-left label','deleted unsure Sigma_1^+|Sigma_2^+','omitted',r'\deleted{\unsure{\Sigma_1^+|\Sigma_2^+}}','The angular base and raised cross are visible; diagonal cancellations cross the lower numeral and its descending return. Neither 1 nor 2 is secure. The actual crossing geometry is logged at G04.','low','omission',False,True,'retained','09',row=10)
add('D11','drawing: right label exponent','deleted unsure + followed by unsure -','Sigma_1^-',r'\Sigma_1^{\deleted{\unsure{+}}\unsure{-}}','A heavy horizontal body overlies vertical and diagonal remnants in a rectangular blot. The live minus and overwritten plus remain qualified; H omits the covered predecessor.','low','omission',False,True,'retained','10',bbox=[521,1203,562,1229],row=11)
add('D12','first equivalence wording after (1)','unsure équivaut','équivaut','équivaut','The initial e, long descending q, dotted i, joined vau and terminal t-like extension are visible before the separate à.','medium','other',True,False,'resolved','11',bbox=[1095,1391,1328,1465],row=12)
add('D13','beneath drawing: cancelled car si','deleted unsure car si','omitted',r'\deleted{\unsure{car si|Car si}}','The open initial c/C, a-like loop and final s plus dotted i survive two cancellation strokes; the intervening r and capitalization remain uncertain. Geometry is logged at G06.','low','omission',False,True,'retained','12',row=13)
add('D14','before symétriquement','unsure et','omitted',r'\unsure{et}','Only a small left mark and a low pale curved run remain in the word position. They support the tentative et without settling it.','low','omission',False,True,'retained','13',bbox=[230,1897,290,1923],row=14)
add('D15','above bottom inclusion: cancelled wording','deleted unsure vois. ouvert','struck vois. ouvert',r'\deleted{vois. ouvert}','The v/o loop, i dot, short s, abbreviation point, and ouvert ending with a tall crossed t remain visible through the single crossing line. Placement is logged at P07.','medium','other',True,False,'resolved','14',row=15)
add('D16','lower slanted note: à signaler / à sign.ler','à signaler|à sign.ler','ill{} after first formula',r'\unsure{à signaler|à sign.ler} avant','The accented à, initial si run, descending g and later tall l are visible. The crop reaches the rightmost ending; its continuation cannot be fully assessed from this enlargement. Retain both source readings. H’s whole tail placeholder is counted once at H17.','low','other',False,False,'retained','15',bbox=[258,1975,460,2104],row=16,grouped_H_difference='H17',boundary_limit='Crop ends at x=432; the rightmost continuation of the slanted ending extends toward x=460 in the half.')
add('D17','last line: insertion above fermé','inserted unsure un|une','omitted',r'\inserted{un}','The raised short u and following low n run end before the tall f; no additional terminal e loop is visible.','medium','omission',True,True,'resolved','16',bbox=[384,2250,447,2281],row=17)
add('D18','last line: connector before crossed group','donc|puis','donc',r'\unsure{donc|puis}','The first loop has a long fine descender, followed by compressed low humps; the internal strokes do not settle donc/puis. H agrees with the primary candidate.','low','other',False,False,'retained','16',bbox=[833,2272,946,2341],row=18)
add('D19','last line: cancelled mathematical/verbal group','deleted unsure Sigma_1^+ serait','struck Sigma_1^+ != emptyset',r'\deleted{\unsure{\Sigma_1^+\text{ serait}}}','A Sigma with lower 1 and raised cross precedes a low connected run ending in a tall crossed/hooked stroke. The run supports serait tentatively; the dense cancellations prevent a secure full recovery. The primary differs from H; this is not asserted as a conclusive H error.','low','misread symbol or index',False,True,'retained','16',bbox=[927,2238,1095,2295],row=19)
add('D20','opening insertion above de X','fermés|fermées','fermées',r'\inserted{\unsure{fermés|fermées}}','The raised accent and terminal s are clear. The small vowel run before s is compressed and does not securely distinguish one e from two. H’s fermées remains the alternate.','medium','misread word',False,True,'retained','03',row=20)
add('D21a','upper-left note: component abbreviation','conn.|connex.','conn.','conn.','The rotated line shows c-o followed by two low n runs and a separate terminal point; no distinct x stroke extends beyond them.','medium','other',True,False,'resolved','04',bbox=[27,599,127,692],row=21,source_part='component abbreviation')
add('D21b','upper-left note: first Sigma index','unsure i; source alternative no index','Sigma_i',r'\unsure{\Sigma_i|\Sigma}','A dot lies at the right of the first Sigma, but a separate lowered stem cannot be recovered confidently. Later indexed occurrences have fuller dot-and-stem forms. Both local states remain supported.','low','other',False,False,'retained','04',bbox=[128,531,185,594],row=21,source_part='first Sigma index')
# Further witness differences, punctuation, placement, and distinct graphic components.
add('H01','upper-left note: opening words','On suppose','Supposons','On suppose','A separate open initial O/n group precedes a space and the descending double-p run of suppose.','high','misread word',False,True,None,'04',bbox=[26,401,206,570])
add('H02','condition (a): Card capitalization','Card','card','Card','The first character has a tall open capital-sized loop before ard.','high','misread word',False,True,bbox=[621,373,732,423])
add('H03','condition (a): covered Sigma','deleted Sigma before E_i','E_i',r'\deleted{\Sigma}E_i','The half shows the angular return within the heavy E stem and bars.','medium','omission',False,True,bbox=[900,373,947,425])
add('H04','upper-right note: NB underline','uline NB','NB',r'\uline{NB}','A separate straight horizontal rule lies directly below the two letters.','high','omission',False,True,None,'05',bbox=[1244,331,1315,385])
add('H05','condition (b): first corrected E_j','deleted Sigma before E_j','E_j',r'\deleted{\Sigma}E_j','The half shows two angular returns under the E bars, with the j descending independently to the right.','medium','omission',False,True,bbox=[816,455,895,531])
add('H06','main NB: Cette capitalization','Cette','cette','Cette','The initial C is tall and open, rising above the following low e/t run.','high','misread word',False,True,bbox=[332,632,443,695])
add('H07','main NB: immediately after automatiquement','automatiquement les','automatiquement ill{} si les','automatiquement les','The final t reaches the right edge; the next physical line begins les. The half and crop support no intervening si or separate unreadable word.','high','text not on the page',False,True,None,'07',bbox=[1190,619,1683,799])
add('H08','main NB: corrected first E_i','deleted Sigma E_i','E_i',r'\deleted{\Sigma}E_i','The large E has an internal angular predecessor crossing its central bar.','medium','omission',False,True,bbox=[441,745,515,805])
add('H09','main NB: after mutuellement','mutuellement','mutuellement.','mutuellement','The final tall t and its return end the line; no separate full stop follows in the open space.','medium','text not on the page',False,True,bbox=[1124,763,1469,824])
add('H10','case heading: Card capitalization','Card','card','Card','The large looped first letter rises above the a/r run and aligns with the tall final d.','high','misread word',False,True,None,'08',bbox=[640,1022,734,1070])
add('P01','below (1): first crossed inclusion and équivaut à','équivaut à before both crossed inclusions','first crossed inclusion before équivaut à','First crossed inclusion on the left of équivaut à, then second crossed inclusion on the following line.','The crop shows the first crossed inclusion and équivaut à sharing one physical line, with the crossed inclusion left of the wording.','high','insertion or placement',True,False,None,'11')
add('H11','after first équivaut à','à','à :','à','The last low a-like mark has a separate raised accent; no colon pair follows it.','high','text not on the page',False,True,None,'11',bbox=[1345,1400,1414,1457])
add('P02','Si on avait cancellation','before comme','after cela équivaut','Deleted Si on avait at the left of the same line as comme.','The half shows a long crossed phrase at x236–642, with comme beginning farther right around x733.','high','insertion or placement',False,True,bbox=[228,1578,960,1666])
add('H12','continuation aussi à','aussi à','aussi à :','aussi à','The crop shows the dotted i, then a separate low à with its accent; the right-hand space contains no colon.','high','text not on the page',False,True,None,'22')
add('H13','after symétriquement, à','à','à :','à','A comma precedes the separate à; the raised accent and low body account for the two marks at the end, without a following colon.','high','text not on the page',False,True,None,'13',bbox=[858,1866,977,1932])
add('P07','cancelled vois. ouvert placement','above/before Sigma_2^-','after the inclusion','Cancelled vois. ouvert above the first Sigma_2^- of the bottom paragraph.','The phrase lies over the first Sigma around x425–625; the inclusion continues below toward E_1 at x645.','high','insertion or placement',False,True,None,'14')
add('P08','bottom replacement clause and cancelled il contient les','deleted il contient les followed by inserted i.e. clause','i.e. clause followed by struck il contient les','Cancelled il contient les below the inserted i.e. clause, before the continuing on a.','The i.e. clause occupies the raised line; the crossed il contient les remains directly beneath it. H also leaves the raised clause without an insertion state.','high','insertion or placement',False,True,None,'21')
add('H14','underline span under vois. in inserted clause','uline vois.','emph vois.',r'\uline{vois}.','The separate underline ends before the isolated abbreviation point; the point is outside the ruled span.','medium','other',True,True,None,'21',bbox=[1192,2013,1287,2071])
add('H15','bottom paragraph: on a ending','on a','on a :',r'on \unsure{a}','The separate final small mark supports a tentatively but has no recoverable full loop. No two-point colon follows it. The new qualification changes certainty, not the primary letter.','low','other',True,True,None,'21',bbox=[1264,2067,1403,2101],qualification_change='New local doubt on a; primary unchanged.')
add('H17','lower slanted note: tail after first formula','i.e. barred Sigma_1^+ != Sigma_1^+ à signaler|à sign.ler avant','ill{}',r'i.e. $\overline{\Sigma_1^+}\ne\Sigma_1^+$ \unsure{à signaler|à sign.ler} avant','The i.e., the second barred/unbarred pair and inequality, and avant are readable. The intermediate slanted word remains doubtful as recorded at D16. One placeholder is counted for this whole passage.','medium','readable ink left as \\ill{}',False,True,None,'15',bbox=[25,1975,460,2316])
add('H18','last argument: Car capitalization','Car','car','Car','The large open C rises well above the joined a/r run.','high','misread word',False,True,None,'18',bbox=[699,2174,794,2225])
add('P09','insertion before last Sigma_1^+ and guide','inserted l’ouvert before Sigma; no explicit guide','Sigma_1^+, inserted ouvert,',"inserted l'ouvert before Sigma_1^+, with the curved guide GUIDE04",'A tall looped l and the following word sit above the symbol. A curve starts in the gap before Sigma, rises above it and ends in a hooked tip to the right. H changes the wording, moves the insertion and adds commas absent here.','high','insertion or placement',True,True,None,'17',bbox=[1436,2102,1610,2229])
# Exact local path additions/geometry corrections, independently locatable.
add('G01','left of opening Soient','omitted','omitted','MARK01: small detached tilted filled oval','A discrete dark tilted spot is visible around (191,141)-(195,145), separate from the opening S. Its role, character, hand and surface origin remain unsettled.','high','drawing or diagram',True,True,None,'19',bbox=[191,141,195,145],interpretation_confidence='low')
add('G02','guide beneath opening insertion','insertion text only','insertion text only','GUIDE01: rising curved guide with upturned right end','The line begins in the gap after parties, bends upward over de, then travels right below the added word and turns up at its endpoint.','high','drawing or diagram',True,True,None,'03',bbox=[369,213,478,263])
add('G03','case-heading underline','single continuous uline','single emph span','RULE01: wavy long run, gap, short separate rule under 2','The underline runs beneath Cas through the crowded relation, stops before 2, and resumes as a short distinct segment under the numeral.','high','drawing or diagram',True,True,None,'08',bbox=[558,1064,932,1095])
add('G04','crossing geometry over upper-left drawing label','generic deleted strike','label omitted','CANCEL01: oblique dark and pale crossing runs over retained label','Two diagonal runs extend across and beyond the labelled angular glyph; the upper pale return forms a pointed excursion. These are reproduced as explicit paths, without adding a generic horizontal strike. H’s omitted label/cluster is counted at D10.','medium','drawing or diagram',True,False,None,'09',bbox=[155,1055,220,1119],grouped_H_difference='D10')
add('G05','right drawing label: detached dot','omitted','omitted','MARK02: detached small filled spot above the exponent','The enlarged label shows a separate dark spot at (528,1193)-(531,1197), above and clear of the overwritten exponent. Its role and hand remain unresolved.','high','drawing or diagram',True,True,None,'10',bbox=[528,1193,531,1197],interpretation_confidence='low')
add('G06','car si cancellation geometry','single generic deleted strike','passage omitted','CANCEL03: two distinct cancellation lines','The upper stroke runs nearly level through the letters; a second lower run remains visibly separate along the middle and turns out to the right. H’s whole omission is counted at D13.','high','drawing or diagram',True,False,None,'12',bbox=[241,1468,425,1488],grouped_H_difference='D13')
add('G07','above first crossed inclusion relation','omitted','omitted','MARK03: two small detached points','Two separate dark points lie above the curved inclusion sign, at full-scan bbox (859,1404)-(863,1411). No punctuation or mathematical role is supplied.','medium','drawing or diagram',True,True,None,'11',bbox=[859,1404,863,1411],interpretation_confidence='low')
add('G08','far right of display (2)','omitted','omitted','MARK04: detached rising pair of spots','The isolated two dark spots are diagonal relative to one another, at full bbox (1603,1778)-(1610,1786). Their character, role, hand and origin remain open.','high','drawing or diagram',True,True,None,'20',bbox=[1603,1778,1610,1786],interpretation_confidence='low')
add('G09','between crossed vois. ouvert and bottom Sigma','omitted','omitted','MARK05: short detached rising slant','A discrete slant is visible below the cancellation and above the base symbol; it is retained graphically without naming a bar, accent or operation.','high','drawing or diagram',True,True,None,'14',bbox=[509,2059,529,2076],interpretation_confidence='low')
add('G10','lower slanted note: two guide paths','text only','tail placeholder','GUIDE02: short curved arrow; GUIDE03: separate longer bent curve','The rotated crop exposes a short curved arrow beside the slanted wording and a separate longer curved run above the left display. Their shapes are drawn with the note. H’s tail placeholder is counted once at H17.','medium','drawing or diagram',True,False,None,'15',bbox=[183,2067,305,2202],grouped_H_difference='H17')
add('G11','underline in last Car formula','underline of full barred Sigma intersect E_1','no underline','RULE02: short curved underline with both ends hooked upward','The rule begins beneath the right part of Sigma, spans the intersection and part of E, and ends before the lowered index. Both ends turn upward. It is shorter than C’s full-expression underline.','high','drawing or diagram',True,True,None,'18',bbox=[896,2226,1038,2245])
add('G12','last cancelled group: crossing paths','generic deleted strike','different struck group','CANCEL04: explicit oblique runs over initial Sigma and low cross-run','Oblique strokes cross the initial symbol and an additional low line crosses the following run. The selected qualified glyph/text is drawn once. H’s reading difference is counted at D19.','medium','drawing or diagram',True,False,None,'16',bbox=[927,2238,1095,2295],grouped_H_difference='D19')
add('G13','drawing: lower-right contour','continuous oval contour','disk with no contour interruption described','Visible short interruption in the lower-right outline','Half b shows a short pale/open interval in the oval below the lower chord, followed by the lower curved run. The proposed contour uses two paths at this locus.','medium','drawing or diagram',True,True,bbox=[394,1278,413,1308])
add('G14','first crossed inclusion: cancellation-line geometry','generic horizontal deleted strike','struck inclusion','CANCEL02: slightly rising cancellation run','The crossing line begins near the lower left of Sigma and ends higher at the right of the second Sigma; explicit coordinates retain its slant.','high','drawing or diagram',True,True,None,'11',bbox=[704,1424,1033,1445])
# Doubts include all retained source loci plus locally qualified graphical roles and a.
doubts=[]
for d in diff:
 if d['C_doubt_status']=='retained':
  doubts.append(dict(location=d['location'],reading=d['reading'],alternatives={
   'D01a':['V'],'D02':['S'],'D03':['toute','tt'],'D05':['-','*'],'D09a':[],
   'D09b':['='],'D10':['Sigma_2^+'],'D11':['covered + and live - both tentative'],
   'D13':['Car si'],'D14':[],'D16':['à sign.ler'],'D18':['puis'],'D19':[],
   'D20':['fermées'],'D21b':['Sigma without index']
  }.get(d['id'],[]),confidence=d['confidence'],reason=d['evidence'],crop=d['readers_crop'],C_source_row=d.get('C_source_row'),difference_id=d['id']))
doubts.append(dict(location='bottom paragraph: on a',reading='a',alternatives=[],confidence='low',reason='The final letter position contains a small separate dark mark without a complete recoverable loop.',crop=cp['21']['path'],difference_id='H15'))
for id in ['G01','G05','G07','G08','G09']:
 d=next(x for x in diff if x['id']==id)
 doubts.append(dict(location=d['location'],reading=d['reading'],alternatives=['character/role/hand/surface origin unresolved'],confidence='low',reason='Shape preserved under a local unsure; the qualification concerns its interpretation.',crop=d['readers_crop'],difference_id=id))
# Inventory follows source order and adds the physically distinct components.
inventory=[]
def inv(kind,pos,text,hand='his hand',component=None):
 d=dict(sheet_kind='text',hand=hand,element='015.A.%02d'%(len(inventory)+1),kind=kind,position=pos,first_words_or_objects=text,transcribed='yes')
 if component:d['component']=component
 inventory.append(d)
inv('text','heading','Version I, single underline')
inv('deletion','heading initial','unsure I|V')
inv('drawing','left of first prose line','detached small oval', 'undetermined hand','MARK01')
inv('text','opening paragraph, three physical lines','Soient X un espace topologique … telles que l’on ait')
inv('deletion','first indexed family','unsure Sigma|S beneath E_i')
inv('insertion','above de X','unsure fermés|fermées')
inv('drawing','gap after parties','curved guide','his hand','GUIDE01')
inv('margin note','upper-left, slanted','On suppose de plus … non fermé … connexe')
inv('drawing','end of upper-left note opening','arrow toward (a)')
inv('display','condition (a)','forall i in I, Card pi_0(X minus E_i)=2')
inv('deletion','condition (a)','Sigma beneath E_i')
inv('margin note','upper right beside (a)','NB les comp. conn. … X minus Sigma_i … ouvertes dans X')
inv('text','upper-right NB','underline under NB')
inv('display','condition (b), two lines','forall (i,j) in I times I … composantes connexes')
inv('deletion','condition (b), first line','Sigma beneath E_j')
inv('deletion','condition (b), second line','Sigma beneath final E_i')
inv('text','NB paragraph below (b)','NB Cette condition (b) est vérifiée automatiquement les …')
inv('deletion','main NB, first E_i','Sigma beneath E_i')
inv('text','purpose paragraph','On se propose d’étudier le double-quoted découpage …')
inv('text','case heading','Cas Card (I)=2')
inv('deletion','case heading before/under (I)','unsure (de)')
inv('deletion','case heading relation','unsure <=|=')
inv('drawing','under case heading','wavy underline and separate short run under 2','his hand','RULE01')
inv('text','three lines beside upper drawing','Soit Sigma_i^+ la comp. conn. … (si I={1,2})')
inv('drawing','middle left','oval outline with lower-right interruption, two chords, two left brace runs and one right brace')
inv('text','drawing labels','E_1, E_2, Sigma_1^+, Sigma_1 with qualified altered sign, Sigma_2^-, Sigma_2^+')
inv('deletion','drawing upper-left label','unsure Sigma_1^+|Sigma_2^+')
inv('drawing','over crossed drawing label','two oblique crossing runs','his hand','CANCEL01')
inv('deletion','drawing right-label exponent','unsure covered + before unsure live -')
inv('drawing','above drawing right label','detached spot','undetermined hand','MARK02')
inv('display','formula (1)','Sigma_1^+ intersect Sigma_2^+=emptyset')
inv('text','right of (1)','ce qui')
inv('deletion','after ce qui','résulte de')
inv('deletion','next line left','Sigma_1^- superset Sigma_2^+')
inv('drawing','crossing first deleted inclusion','rising cancellation line','his hand','CANCEL02')
inv('drawing','above its inclusion sign','two detached points','undetermined hand','MARK03')
inv('text','same line right','équivaut à')
inv('deletion','following line left','Sigma_2^- superset Sigma_1^+')
inv('display','same line right','Sigma_1^+ subset Sigma_2^- union E_2, et')
inv('deletion','under drawing','unsure car si|Car si')
inv('drawing','across car si','two separate cancellation strokes','his hand','CANCEL03')
inv('deletion','left of comme line','Si on avait')
inv('text','line beside cancellation and next pale line','comme Sigma_1^+ intersect E_2=emptyset, cela équivaut aussi à')
inv('display','formula (2)','Sigma_1^+ subset Sigma_2^-')
inv('drawing','far right beside (2)','two detached spots','undetermined hand','MARK04')
inv('text','before (2 prime)','unsure et symétriquement, à')
inv('display','formula (2 prime)','Sigma_2^+ subset Sigma_1^-')
inv('text','bottom paragraph','Comme Sigma_2^- superset E_1, … on unsure a')
inv('deletion','above first bottom Sigma','vois. ouvert')
inv('drawing','between deleted wording and Sigma','short detached slant','undetermined hand','MARK05')
inv('deletion','below raised replacement','il contient les')
inv('insertion','above cancelled clause','i.e. Sigma_2^- est un vois. ouvert de E_1,')
inv('text','within raised clause','underline under vois, excluding following point')
inv('margin note','bottom-left, slanted','barred Sigma_1^+ intersect E_1 != emptyset i.e. barred Sigma_1^+ != Sigma_1^+ unsure à signaler|à sign.ler avant')
inv('drawing','beside lower slanted wording','short curved arrow','his hand','GUIDE02')
inv('drawing','below lower slanted formula','separate longer bent guide','his hand','GUIDE03')
inv('display','bottom left','Sigma_2^- intersect Sigma_1^+ != emptyset')
inv('text','last two lines','Car barred Sigma_1^+ intersect E_1 != emptyset (sinon … disconnexe),')
inv('drawing','under first Car expression','short underline with two hooked ends','his hand','RULE02')
inv('insertion','before final Sigma_1^+ in parenthesis',"l'ouvert")
inv('drawing','beneath l’ouvert','curved guide with hooked right endpoint','his hand','GUIDE04')
inv('insertion','above fermé','un')
inv('deletion','bottom centre','unsure Sigma_1^+ serait')
inv('drawing','across final deleted group','oblique and low cancellation runs','his hand','CANCEL04')
inv('text','bottom-left pencil numeral','archive sheet number 14, recorded only in comment','undetermined hand')
notes={
 'page_content':'A handwritten Version I page introduces X, the indexed family E_i, conditions (a) and (b), two marginal notes, the case Card(I)=2, a labelled oval drawing, and the written relations (1), (2), (2 prime). The final parenthesis continues to the page end with a comma.',
 'author_uncertainty':'No explicit verbal uncertainty phrase or question mark was identified on this sheet. Cancellations, overwritten glyphs and added wording are preserved; editorial unsure markers describe this reader’s unresolved ink.',
 'title_date_counts':'Heading Version I. No date or author page count read. The pencil 14 is recorded only as an archive-sheet comment; writer attribution is unresolved.',
 'mathematics_led_reading_decisions':'No mathematical result or expected formula selected a glyph. The repeated indexed symbols were tracked while reading, and the crossed signs, written complement Sigma_i, unbarred intersections, closure bars, and literal automatically les wording were kept from their local strokes.',
 'workflow':'UTC clock and initial packet-read calls were issued together at 2026-11-20 15:15:26 UTC. The first combined text output was truncated; the brief and every packet file were subsequently read in complete outputs before the image pass. Whole image opened once, a once, b once, then one enlargement per listed unresolved locus. All 22 crop PNGs were displayed successfully; none was reopened or recropped. Root’s shared source-row reminder was read after crop 22.',
 'coordinate_map':'Full scan is 1691x2360; both supplied halves are 1691x1260. Half a starts at full y=0; half b starts at full y=1100 (2360-1260), with 160-pixel overlap. Bboxes in the report use full-scan top-left origin.',
 'boundary_limit':'Crop 15 was planned too narrowly at the right end of the slanted à signaler/à sign.ler phrase (x=432 boundary; half shows continuation toward x=460). It is not recropped. That source doubt remains explicit. The drawn note guide paths are approximations and carry separate observed boxes and path-coordinate envelopes.',
 'witness_classification':'H has full text for its page 14, our scan 15. Its drawing description is apparatus; its emptyset macro and typographic quote/emphasis macro choices have no separate reading differences. Its single lower-note ill placeholder is collated once at H17; local doubts and graphic details there refer back to that row.',
 'verification_scope':'Source-only structural and reading/report checks. No OCR, external sources, compiler, TeX format builder, rendering, installation, or delegation.',
 'source_doubt_accounting':{'actual_source_rows':21,'local_decisions':24,'resolved_local_decisions':9,'retained_local_decisions':15,'compound_rows':{'1':['D01a','D01b'],'9':['D09a','D09b'],'21':['D21a','D21b']}},
 'drawing_component_map':[
  {'component':'GUIDE01','origin_full':[372,177],'units_cm':[.013,-.013],'observed_bbox':[369,213,478,263],'control_point_envelope_local':[-8,39,102,83]},
  {'component':'RULE01','origin_full':[501,996],'units_cm':[.013,-.013],'observed_bbox':[558,1064,932,1095],'control_point_envelope_local':[63,74,426,103]},
  {'component':'main oval','origin_full_approx':[24,1069],'units_cm':[.013,-.013],'source_paths':'C upper contour plus revised right/lower split; C two-chord command; C two left-brace commands; C right-brace command. All six live labels and the crossed label individually compared with the halves.'},
  {'component':'CANCEL01','origin_full_approx':[24,1069],'units_cm':[.013,-.013],'observed_bbox':[155,1055,220,1119],'path_envelope_local':[135,-12,185,37]},
  {'component':'CANCEL02','origin_full':[704,1388],'units_cm':[.013,-.013],'observed_bbox':[704,1424,1033,1445],'control_point_envelope_local':[2,37,325,54]},
  {'component':'CANCEL03','origin_full':[202,1435],'units_cm':[.013,-.013],'observed_bbox':[241,1468,425,1488],'control_point_envelope_local':[43,34,220,51]},
  {'component':'GUIDE02','origin_full':[17,1962],'units_cm':[.009,-.009],'observed_bbox':[233,2067,277,2133],'control_point_envelope_local':[211,103,257,168]},
  {'component':'GUIDE03','origin_full':[17,1962],'units_cm':[.009,-.009],'observed_bbox':[183,2149,305,2202],'control_point_envelope_local':[155,187,282,238]},
  {'component':'RULE02','formula_local_origin_full_approx':[854,2217],'units_cm':[.013,-.013],'observed_bbox':[896,2226,1038,2245],'control_point_envelope_local':[42,10,183,23]},
  {'component':'GUIDE04','origin_full':[1455,2104],'units_cm':[.013,-.013],'observed_bbox':[1460,2151,1605,2200],'control_point_envelope_local':[6,40,147,95]},
  {'component':'CANCEL04','origin_full_approx':[927,2250],'units_cm':[.013,-.013],'observed_bbox':[927,2238,1095,2295],'control_point_envelope_local':[10,-10,156,22]}
 ]
}
notation=[
 {'location':'opening family and conditions (a),(b)','sign':'E and covered Sigma','latex':r'\deleted{\Sigma}E_i, \deleted{\Sigma}E_j','evidence':'Heavy upright/three bars over angular internal returns; first predecessor separately qualified Sigma/S.'},
 {'location':'condition (a)','sign':'Card and pi_0','latex':r'\operatorname{Card}\pi_0','evidence':'Capital-height open C; topped pi and a low small oval index.'},
 {'location':'upper-right NB','sign':'complement glyph','latex':r'X\setminus\Sigma_i','evidence':'Open left edge and diagonal central return of Sigma.'},
 {'location':'formulas (1),(2),(2 prime)','sign':'plus/minus, inclusion/intersection/union','latex':r'\Sigma_1^+,\Sigma_2^-,\subset,\supset,\cap,\cup','evidence':'Each plus shows a cross; each minus a horizontal; inclusion sides are curved without lower bars; intersections open down and union opens up.'},
 {'location':'two slanted notes and final Car formula','sign':'closure bars','latex':r'\overline{\Sigma}_i; \overline{\Sigma_1^+}','evidence':'Separate horizontal strokes above the Sigma groups, distinct from their top arms.'},
 {'location':'purpose paragraph','sign':'double quotation ticks','latex':chr(96)*2+'découpage'+"''",'evidence':'Paired ticks at each side of the word.'},
 {'location':'opening prose and notes','sign':'abbreviations','latex':'ens.; comp. conn.; NB; i.e.; vois.','evidence':'Punctuation read locally, including the point after ens. and the point outside the vois underline.'},
 {'location':'formula label (2 prime)','sign':'prime','latex':r"(2')",'evidence':'One short raised stroke after the numeral inside the closing parenthesis.'},
 {'location':'pale continuation before (2)','sign':'aussi à','latex':'aussi à','evidence':'Enlargement shows the final i dot and separate accented à. No remaining reading doubt or C change at this crop target.'}
]
report=dict(scan=15,reader='A',start_utc='2026-11-20 15:15:26 UTC',end_utc=None,full_image_viewed=True,halves_viewed=True,complete_visual_read=True,differences=diff,doubts=doubts,inventory=inventory,notes=notes,notation=notation,check_events=[],crops=crops,brief_feedback=[
 'The actual C doubtful-reading row mapping is preserved separately from local decisions and graphic component changes; this avoids conflating the three compound rows.',
 'Graphical shape confidence and unresolved role/hand are reported separately for the five detached-mark clusters.',
 'The too-narrow crop-15 ending is disclosed and stays doubtful; no second crop was made.',
 'Path coordinates are approximate reconstructions; observed locus boxes, local origins, and control-point envelopes are listed separately. No rendered layout verification is claimed.'
])
(base/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
audit="""# Scan 015 — independent reader A

Start: **2026-11-20 15:15:26 UTC**. Whole scan viewed once; half a once; half b once. All 22 single local crops were then viewed once. Full image: 1691 × 2360; lower-half origin is full y = 1100. The first combined packet output was truncated and was followed by complete reads of every required file.

## Line-by-line audit

| Physical passage | Readable ink and retained state | Unresolved ink |
| --- | --- | --- |
| Top heading | Version I, one long underline | Cancelled predecessor I / V |
| Opening line | Soient X un espace topologique, indexed E family, un ens. de | Covered first letter Sigma / S |
| Opening second and third lines | parties de X (noté indiciellement), telles que l’on ait; raised insertion and curved guide | fermés / fermées |
| Upper-left note, opening | On suppose de plus que pour … comp. conn. | tte / toute / tt |
| Same note, component | Sigma … de X minus E_i, on ait | First Sigma lower index i / absent |
| Same note, formulas | Both closure inequalities and both i.e. groups | None in the displayed signs |
| Same note, ending | Sigma_i non fermé dans X (ce qui est le cas si X est connexe) | None retained on non |
| Condition (a) | forall i in I, Card pi_0(X minus E_i)=2; covered Sigma retained | None |
| Upper-right NB | NB underlined; comp. conn.; X minus Sigma_i; sont ouvertes dans X | Second exponent + / − / star |
| Condition (b), first line | Quantified pair, i unequal j, corrected E_j est contenu dans l’une | None |
| Condition (b), second line | des deux composantes connexes de X minus corrected E_i. | None; final covered Sigma resolved |
| Main NB, first line | NB Cette condition (b) est vérifiée automatiquement | None; word ends at right edge |
| Main NB, following lines | les corrected E_i (i in I) sont connexes, dès lors que les E_i sont supposés disjoints mutuellement | No extra si, unreadable word, or endpoint period is supplied |
| Purpose paragraph | On se propose d’étudier le double-quoted découpage de X par la famille (E_i). | None |
| Case heading | Cas Card (I)=2; underline has a gap before its separate run under 2 | Cancelled (de); overwritten ≤ / = |
| Three lines introducing two components | Soit Sigma_i^+ la comp. conn. de X minus E_i … (j unequal i), alors on a (si I={1,2}) | None |
| Oval drawing | Two chords; live E_1/E_2 and four Sigma labels; two left brace runs, right brace, lower-right contour interruption | Crossed upper label index 1 / 2; right exponent’s covered + and live − |
| Formula (1) and right-hand text | Sigma_1^+ intersect Sigma_2^+=emptyset; ce qui; deleted résulte de | None |
| First crossed-inclusion row | Deleted Sigma_1^- superset Sigma_2^+ at left; équivaut à at right | Two detached points retained graphically; no mathematical role |
| Second crossed-inclusion row | Deleted Sigma_2^- superset Sigma_1^+; live Sigma_1^+ subset Sigma_2^- union E_2, et | None |
| Left cancellation beneath drawing | Two actual crossing lines over car si | car si / Car si; compressed middle letters |
| Next prose line | Deleted Si on avait at left; comme Sigma_1^+ intersect E_2=emptyset, cela équivaut | None |
| Pale continuation | aussi à | None; no following colon |
| Formula (2) | Sigma_1^+ subset Sigma_2^- | Separate far-right two-spot cluster kept graphical |
| Before (2 prime) | symétriquement, à | Faint et |
| Formula (2 prime) | Sigma_2^+ subset Sigma_1^-; a single prime in label | None |
| Bottom paragraph opening | Comme Sigma_2^- superset E_1; cancelled vois. ouvert above | Detached slant above Sigma retained graphically |
| Raised replacement | i.e. Sigma_2^- est un vois. ouvert de E_1,; vois underlined without its point | None |
| Cancelled baseline and continuation | il contient les; on … | Final a is a new local doubt; no colon supplied |
| Lower slanted note | First closure/intersection inequality; i.e.; second closure inequality; avant; two curved guides | à signaler / à sign.ler; rightmost ending reaches crop boundary |
| Bottom left display | Sigma_2^- intersect Sigma_1^+ unequal emptyset | None |
| Last argument, first line | Car barred Sigma_1^+ intersect E_1 unequal emptyset; short hooked underline; (sinon | None |
| Raised insertion over last Sigma | l’ouvert before Sigma_1^+, curved guide with hooked right end | None |
| Last physical line | serait; raised un; fermé dans X; final X serait disconnexe), | donc / puis; cancelled Sigma_1^+ serait |
| Foot | Pencil archive 14, comment only | Writer attribution unsettled |

Five discrete mark clusters are preserved under local graphical doubt: before Soient; above the drawing’s right exponent; above the first crossed inclusion; far right of (2); between cancelled vois. ouvert and Sigma. Their shapes have separate confidence from their unresolved roles and hands.

## Source doubts and witness collation

The report maps **21 actual C source rows to 24 local decisions**. Rows 1, 9 and 21 each retain their two separate physical questions. **Nine local decisions resolve a C doubt; fifteen retain one.** Notation, slips, and abbreviation tables are kept in their source categories.

The principal lexical/symbol differences from H concern On suppose, the missing corrected predecessors, the tentative abbreviation tte, non, the written marginal complement Sigma_i, the uncertain second marginal sign, the omitted cancelled car si, faint et, inserted un, and the final cancelled group. The proposed text retains automatiquement les as written. It also preserves the actual placement of the cancelled and raised lines, l’ouvert before its Sigma, capital Card / Cette / Car, and observed endpoint punctuation.

Each difference has its own original-image bbox and either a successfully displayed crop or half-image evidence. H’s lower-note ill placeholder is counted once; local C doubts and graphical details refer back to that passage.

## Crop boundary and graphical maps

The crop for the lower slanted note is **15_lower_margin.png**, full bbox **(17, 1962, 432, 2345)**, rotated **−40°**. Its right boundary reaches the ending of à signaler / à sign.ler; the half shows continuation toward x=460. That ending remains doubtful. There was no recrop.

The original drawing coordinates are mapped approximately by **full = local + (24, 1069)**. New guides, rules, and cancellations have named components in reading.tex and separate observed bboxes / local origins / path envelopes in report.json. Existing contour, chord, brace, and label components were individually compared with the halves; visible lower-right interruption and added crossing details are explicit.

## Checks

The mathematical check-events list is empty. Reading the mathematical expressions and matching their visible indices and signs did not supply a proof check, reconstructed statement, or repair.

A single final source/report cross-check checks braces, environments, delimiters, required keys, source-row coverage, crop references, and selected text consistency. No compiler or renderer is used.
"""
(base/'reading.md').write_text(audit)
print('Wrote report.json and reading.md; differences',len(diff),'inventory',len(inventory),'doubts',len(doubts))
