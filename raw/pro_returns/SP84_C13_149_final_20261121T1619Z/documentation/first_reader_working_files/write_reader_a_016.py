from pathlib import Path
import json
p=Path('/workspace/scratch/4644e52611c0')
tex=r'''\scanpage{16}
$E_{\bar K'/K'}\longrightarrow E_{\bar K/K}$ associés à des hom \inserted{$K\longrightarrow K'$} d'extensions de type fini de $\mathbb Q$, ayant une image ouverte donc un centralisateur réduit à $1$, on voit de $=$ que l'hom de topos $B_{K'}-B_K$ ou de groupoïdes $\Pi_{K'}-\Pi_K$, sont déterminés à \deleted{\unsure{iso}\illegible{}}\unsure{équivalence} près (définis à isom unique près) par l'hom correspondant des groupes extérieurs. Il en sera en particulier ainsi du morphisme structural $B_K\longrightarrow B_{\mathbb Q}$ ou $\Pi_K-\Pi_{\mathbb Q}$, qu'on peut interpréter \inserted{intrinsiquement} comme un hom de groupes \inserted{profinis} extérieurs $E_K-E_{\mathbb Q}$. Mais nous préférons suivre un point de vue un peu affiné, en exploitant le fait que $\pi_{\bar K/K}$ est lui aussi à centre trivial. Cela signifie que l'extension de $\unsure{E|\Gamma}=\Gamma_{\bar K/K}$ par $\pi_{\bar K/K}$ est entièrement connue, \inserted{à isom unique près,} pour $\pi_{\bar K/K}$ \inserted{et $\Gamma$} fixés,
\margin{15}
'''
(p/'edition/reviews/149_scan016.tex').write_text(tex,encoding='utf-8')
boxes={
'c01':[1160,410,1580,491], 'c02':[310,575,590,654], 'c03':[1275,525,1600,624],
'c04':[309,675,555,770], 'c05':[964,655,1488,762], 'c06':[760,774,1115,920],
'c07':[285,1140,1410,1266], 'c08':[282,1253,1120,1389], 'c09':[1164,1242,1645,1338],
'c10':[273,1390,870,1508], 'c11':[265,1490,723,1622], 'c12':[276,1652,709,1748],
'c13':[1260,1709,1648,1837], 'c14':[985,2051,1295,2168], 'c15':[985,2125,1650,2328], 'c16':[22,2309,72,2357]}
def crop(c): return f'crops/149_scan016_{c}.png'
changes=[]
def ch(i,place,C,H,final,evidence,c,confidence='high',against_C=False,against_H=True,kind='misread word',error_category='Words',marked_in_H=False,mathematical=False):
 changes.append(dict(id=f'c{i:02d}',place=place,C=C,H=H,final=final,evidence=evidence,crop=crop(c),box=boxes[c],confidence=confidence,against_C=against_C,against_H=against_H,kind=kind,error_category=error_category,marked_in_H=marked_in_H,mathematical=mathematical))
ch(1,'Main line 4, after on','voit','sait','voit','The first letter has a broad open lower sweep with a rightward upturn, followed by a reduced rounded o, a separate i dot, and a tall crossed t. The crop supports voit rather than the initial s and a of sait.','c01')
ch(2,'Main line 5, sign after de',r'\unsure{=|\overline m}',r'\uncertain{même}','=', 'Two separate nearly horizontal bars are present. The lower one has only a small entry curl and no m humps. The literal sign is retained; même is its expansion, not the written word.','c02',kind='abbreviation expanded or spelling modernised',error_category='Abbreviations expanded, spelling modernised',marked_in_H=True)
ch(3,'Main line 5, topos link',r'B_{K\prime}\unsure{-|\longrightarrow}B_K',r'B_{K\prime}\to B_K',r'B_{K\prime}-B_K','The connecting line has a plain left end and a thickened downward terminal nib at the right. It has no two-branch arrowhead. Both B letters and the first index prime are clear.','c03',kind='misread symbol or index',error_category='Symbols and indices',mathematical=True)
ch(4,'Main line 6, before de groupoïdes','ou','et','ou','The word is two low reduced strokes: a small rounded first mark and a longer low u-like run. There is no tall or crossed t. The following de is separate.','c04')
ch(5,'Main line 6, groupoid link',r'\Pi_{K\prime}\unsure{-|\longrightarrow}\Pi_K',r'\Pi_{K\prime}\to\Pi_K',r'\Pi_{K\prime}-\Pi_K','The shaft ends in a small rounded ink thickening with no separate upper and lower arrowhead branches. Each Pi has a long roof and two distinct tall legs. The first K alone has a prime.','c05',kind='misread symbol or index',error_category='Symbols and indices',mathematical=True)
ch(6,'Main line 7, overwritten wording after déterminés à',r'\unsure{équivalence}',r'\struck{isomorphisme}\ill{}',r'\deleted{\unsure{iso}\illegible{}}\unsure{équivalence}','The beginning contains overlapping older and newer strokes, unlike the clear final lence. An i-like entry and rounded s/o-like traces make iso a tentative underlying prefix; the rest of the older text cannot be separated. H’s full isomorphisme is therefore not completed. The newer word has the long descending q-like stroke and clear lence ending supporting tentative équivalence. The overwritten state is retained, with neither layer claimed fully legible.','c06',confidence='low',against_C=True,against_H=True,kind='deletion state',error_category='Struck text',marked_in_H=True)
ch(7,'Main line 10, continuation after Il en','sera','est','sera','The reduced word begins with a curved s-like entry and continues in several low short strokes. There is no tall final t of est. The word occupies the start of the line before the separate en.','c07')
ch(8,'Main lines 10–11, singular structural morphism phrase','du morphisme structural','des morphismes structurels','du morphisme structural','Crop c07 shows du: a looped d followed by one low u-run, with no separate s. Crop c08 shows morphisme ending in its low final e-run and structural ending in a tall looped l; neither word has a following s. The terminal sequence is al, not els.','c08')
ch(9,'Main line 11, after structural B map','ou','et','ou','After B_Q are a small rounded o-like mark and a low horizontal u-run, matching the first ou in c04. There is no t stem or crossbar. The nearby map has a separate curved rightward head, unlike the headless links elsewhere.','c09')
ch(10,'Main line 12, structural Pi link',r'\Pi_K-\Pi_{\mathbb Q}',r'\Pi_K\to\Pi_{\mathbb Q}',r'\Pi_K-\Pi_{\mathbb Q}','A single horizontal stroke joins the two Pi terms. Its right end is only a short terminal turn; no arrowhead branches are present. The Q index has its own inner/downward stroke.','c10',kind='misread symbol or index',error_category='Symbols and indices',mathematical=True)
ch(11,'Insertion above main line 13','intrinsiquement','intrinsèquement','intrinsiquement','A separate dot sits above the short stroke immediately before q. That stroke is the written i of -siquement; there is no clearly written è loop with a grave accent here. The insertion leader runs from before comme beneath the raised word. The literal spelling intrinsiquement is retained.','c11',kind='abbreviation expanded or spelling modernised',error_category='Abbreviations expanded, spelling modernised',marked_in_H=True)
ch(12,'Main line 14, E link',r'E_K-E_{\mathbb Q}',r'E_K\to E_{\mathbb Q}',r'E_K-E_{\mathbb Q}','The shaft has a blunt left start and a small upright terminal nib at the right. There is no pointed two-branch head. The terminal nib is reported rather than converted to an arrow; the source’s literal shaft is retained.','c12',kind='misread symbol or index',error_category='Symbols and indices',mathematical=True)
ch(13,'Main line 15, after un peu','affiné','différent','affiné','The word begins with a small closed a body and two very tall f stems sharing a cross stroke. A dot marks the following i; the low ending is né. The initial d/i sequence and final rent required by différent are absent.','c13')
ch(14,'Main line 18, left member of identification',r'\unsure{\Gamma|E}=\Gamma_{\bar K/K}',r'\Gamma=\Gamma_{\bar K/K}',r'\unsure{E|\Gamma}=\Gamma_{\bar K/K}','The left glyph has a visible middle rightward stroke and a longer lower rightward stroke, making E the first graphic reading. Those two strokes are lighter than the dark roof and upright, so a Gamma-like overtracing remains possible. The sequence of any correction cannot be established. No old/new correction sequence is invented; E and Gamma remain explicit alternatives.','c14',confidence='medium',against_C=True,against_H=True,kind='misread symbol or index',error_category='Symbols and indices',mathematical=True)
ch(15,'Main line 19, supposed parentheses around final condition',r'pour $\pi_{\bar K/K}$ \inserted{et $\Gamma$} fixés,',r'(pour $\pi_{\bar K/K}$ \add{et $\Gamma$} fixés)',r'pour $\pi_{\bar K/K}$ \inserted{et $\Gamma$} fixés,','The tall curve before pour continues rightward beneath the added à isom unique près, so it is an insertion leader, not an opening parenthesis. The smaller lower leader attaches et Gamma before fixés. The final separate mark after fixés is a short low comma, not a tall closing parenthesis.','c15',kind='insertion or placement',error_category='Insertions put in the wrong place',marked_in_H=True)
ch(16,'Lower-left marginal number',r'\margin{15}','(omitted)',r'\margin{15}','The first digit has an angled entry and narrow vertical stem. The second has a long top stroke, inward middle bend and rounded lower return: 5. The separate marginal number is retained.','c16',kind='omission',error_category='Omissions')

def dec(id,decision,reading,evidence,c,confidence):
 return dict(id=id,decision=decision,reading=reading,evidence=evidence,crop=crop(c),box=boxes[c],confidence=confidence)
decisions=[
 dec('M1001','first','=','Two distinct horizontal bars with no m humps settle the literal equals sign. The expansion même belongs only in the abbreviation list.','c02','high'),
 dec('M1002','first','-','The right terminal is a thick nib turn, without an upper/lower arrowhead pair. The complete B formula is inspected in c03.','c03','high'),
 dec('M1003','first','-','The horizontal line ends bluntly with a slight ink thickening; no pointed head is visible. The complete Pi formula and first index prime are clear.','c05','high'),
 dec('M1004','undecided',r'\unsure{équivalence}','The final lence is clear and a q-like descender supports équivalence, but the first part is overwritten and its strokes cannot all be allocated to one layer. The underlying older text is separately retained only in a qualified partial reading.','c06','low'),
 dec('M1005','undecided',r'\unsure{E|\Gamma}','Middle and lower rightward strokes favor E as the graphic first reading, but their lighter weight beside the heavy roof/stem leaves a Gamma-like overtrace possible. Both readings remain; no correction sequence is asserted.','c14','medium')]

inventory=[]
def inv(e,kind,pos,first,hand='main manuscript hand'):
 inventory.append(dict(scan=16,sheet_kind='text',hand=hand,element=e,kind=kind,position=pos,first_words_or_objects=first,transcribed='yes'))
inv('e01','text','continuous text, 19 main manuscript lines',r'E_{\bar K\prime/K\prime} to E_{\bar K/K} associés')
inv('e02','insertion','above main line 2, after hom',r'K\longrightarrow K\prime')
inv('e03','deletion','under the rewritten word in main line 7',r'\unsure{iso}\illegible{}')
inv('e04','insertion','above comme in main line 13','intrinsiquement')
inv('e05','insertion','above extérieurs in main line 13','profinis')
inv('e06','insertion','above main line 19, between connue, and pour','à isom unique près,')
inv('e07','insertion','below main line 19, before fixés',r'et \Gamma')
inv('e08','margin note','extreme lower-left edge','15','hand not established from this small number')

notes=[
'This leaf has no visible author folio at the top and carries marginal 15 at the lower left. It consists of one continuing paragraph, without a title, date, display, drawing or diagram. The first formula continues the incoming sentence; the final comma leaves the paragraph open.',
'The text discusses how the written group homomorphisms determine topos/groupoid homomorphisms, then turns to the structural morphism and the extension by pi. These statements are transcribed only; none was mathematically checked or used to force a reading.',
'The full page and both prepared halves were personally read once, followed by 16 targeted crops. The count 25 comprises 19 main manuscript lines, five separately placed short insertions, and the marginal-number line. All 18 supplied difference rows and all five C marks are covered.',
'The literal equals sign after de is the written short form; même is recorded only as its expansion. Likewise the two first B/Pi links and the later Pi/E links remain headless shafts. The structural B map and the opening E map visibly have heads; no rule from the map’s expected meaning was used to supply one elsewhere.',
'The beginning of équivalence is overwritten. The older text cannot be independently recovered as all of isomorphisme. Only an iso-like prefix is offered tentatively, with the rest left unreadable; the live équivalence remains doubtful. The report does not claim a fully recoverable two-word correction.',
'The left glyph in the final identification is now printed E-first with Gamma as an alternative. Its middle and lower strokes support E, while their lighter weight leaves an overtracing question. The resulting written identification is retained without replacing it by an expected mathematical letter or inventing a correction history.',
'All five agreed insertions were checked for attachment: K to K-prime follows hom; intrinsiquement precedes comme; profinis precedes extérieurs; à isom unique près follows connue,; et Gamma precedes fixés. The long leader before pour is not punctuation. The final mark is a comma.',
'Agreed ink was checked as well, including donc (H doubts it), the initial prime/bar placements, the written singular du morphisme structural, the abbreviations hom and isom without supplied stops, and every extension index. The inline numeral 1 was settled from the half and receives audit coordinates without an extra crop.',
'No OCR, external research, other page text, other reader return, mathematical proof check or TeX compilation was used. Model identification: GPT-6 Astra Pro, effort not exposed, run SP84_C13_149.'
]
hand=[
 dict(habit='The sign = is used within prose as a short form for même.',pages=[16],consistency='One clear local occurrence after de; two separate bars.',misread='H expands the sign to même. The page preserves =.'),
 dict(habit='Headless shafts may end in a thickened or short upright nib turn.',pages=[16],consistency='The two first B/Pi links and the later Pi/E links lack a two-branch head; c03, c05, c10, c12.',misread='H turns all four into arrows. The structural B map provides a clear local contrast with a separately drawn head.'),
 dict(habit='The word ou can be reduced to a tiny rounded first mark and one low horizontal run.',pages=[16],consistency='Both occurrences before alternative groupoid maps agree; c04 and c09.',misread='H reads et despite the absence of any t stem or crossbar.'),
 dict(habit='Long curved insertion leaders can resemble opening parentheses.',pages=[16],consistency='Visible at intrinsiquement, profinis and the final two additions.',misread='H treats the long curve before pour as an opening parenthesis; tracing its horizontal continuation shows attachment to the insertion.'),
 dict(habit='Heavy retracing can obscure the order of letter correction.',pages=[16],consistency='The overwritten word in c06 and the final capital in c14 have separable light/heavy strokes but uncertain layer order.',misread='The final capital cannot safely be normalized to Gamma or assigned a confident E-to-Gamma correction sequence.')]
notation=[
 dict(written='=',rendering='=',meaning='Written short form for même in prose.',evidence='c02: two distinct nearly parallel bars after de; no m humps.'),
 dict(written='headless horizontal shaft',rendering='-',meaning='Literal connecting sign between the named objects; no arrowhead supplied.',evidence='c03, c05, c10, c12; the terminal thickening is distinguishable from the explicit head in c09.'),
 dict(written=r'\Pi_{K\prime},\Pi_K,\Pi_{\mathbb Q}',rendering=r'\Pi_{K\prime},\Pi_K,\Pi_{\mathbb Q}',meaning='Groupoid symbols named in the prose.',evidence='c05 and c10 have broad roofs and two separate tall legs.'),
 dict(written=r'\pi_{\bar K/K}',rendering=r'\pi_{\bar K/K}',meaning='Object said in the text to have trivial centre and to occur in the extension.',evidence='Three lower-paragraph occurrences have low pi and a full extension index with the first K barred.'),
 dict(written=r'\unsure{E|\Gamma}=\Gamma_{\bar K/K}',rendering=r'\unsure{E|\Gamma}=\Gamma_{\bar K/K}',meaning='Written identification in the extension sentence; left glyph remains uncertain.',evidence='c14: middle/lower rightward strokes favor E, but heavy roof/stem and lighter lateral strokes leave overtracing unresolved.')]
abbreviations=[
 dict(form='hom',expansion='homomorphismes / homomorphisme, according to occurrence',place='opening sentence, topos/groupoid discussion and structural-map sentence'),
 dict(form='=',expansion='même',place='main line 5, after de'),
 dict(form='isom',expansion='isomorphisme',place='main line 8 and final raised insertion')]
doubts=[
 dict(place='Main line 7, older overwritten text, c06',reading=r'\deleted{\unsure{iso}\illegible{}}',alternatives=['iso-like initial traces with unreadable continuation','unseparated older word'],confidence='low',reason='The beginning is overwritten. Initial short/dotted and rounded traces are visible, but the remainder cannot be allocated to an older word independently of the newer strokes.'),
 dict(place='Main line 7, live rewritten word, c06',reading=r'\unsure{équivalence}',alternatives=['équivalence','partly unresolved rewritten word ending lence'],confidence='low',reason='The lence ending and descending q-like stroke support the candidate, but the overwritten initial letters are not all plain.'),
 dict(place='Main line 18, left capital, c14',reading=r'\unsure{E|\Gamma}',alternatives=['E',r'\Gamma'],confidence='medium',reason='Middle and lower rightward strokes are visible but lighter than the dark Gamma-like roof/stem; possible retracing order cannot be settled.')]
audit=[]
def ab(i,kind,b,reading):
 audit.append(dict(box=f'b{i:02d}',kind=kind,x0=b[0],y0=b[1],x1=b[2],y1=b[3],reading=reading))
ab(1,'insertion',[455,174,657,268],r'\inserted{$K\longrightarrow K\prime$}')
ab(2,'handwritten number',[1050,426,1096,481],'1')
ab(3,'prose',boxes['c01'],'on voit de')
ab(4,'formula',[327,594,388,641],'=')
ab(5,'formula',boxes['c03'],r'B_{K\prime}-B_K')
ab(6,'prose',boxes['c04'],'ou de')
ab(7,'formula',boxes['c05'],r'\Pi_{K\prime}-\Pi_K,')
ab(8,'deletion',boxes['c06'],r'\deleted{\unsure{iso}\illegible{}}\unsure{équivalence}')
ab(9,'prose',boxes['c07'],'sera en particulier ainsi du')
ab(10,'prose',boxes['c08'],'morphisme structural')
ab(11,'formula',boxes['c09'],r'$B_K\longrightarrow B_{\mathbb Q}$ ou')
ab(12,'formula',boxes['c10'],r'\Pi_K-\Pi_{\mathbb Q},')
ab(13,'insertion',boxes['c11'],r'\inserted{intrinsiquement} comme un')
ab(14,'insertion',[1240,1455,1480,1565],r'\inserted{profinis}')
ab(15,'formula',boxes['c12'],r'E_K-E_{\mathbb Q}.')
ab(16,'prose',boxes['c13'],'peu affiné,')
ab(17,'formula',boxes['c14'],r'\unsure{E|\Gamma}=\Gamma_{\bar K/K}')
ab(18,'insertion',boxes['c15'],r'\inserted{à isom unique près,} pour $\pi_{\bar K/K}$ \inserted{et $\Gamma$} fixés,')
ab(19,'margin note',boxes['c16'],r'\margin{15}')

diff=[]
def dc(row,cl,cid,reason): diff.append(dict(row=row,classification=cl,change_id=cid,reason=reason))
dc(1,'editorial-only',None,'The scan header is editorial metadata, not a manuscript numeral.')
dc(2,'macro-only',None,'Both bar/prime constructions place the prime after the barred K; the tokenizer splits them differently.')
dc(3,'material','c01','The source reads voit; its v/o-like low strokes precede the dotted i and crossed t.')
dc(4,'material','c02','The written sign is =; même is an expansion and is kept out of the page text.')
dc(5,'material','c03','The complete B formula has a headless shaft.')
dc(6,'material','c04','The connective is ou, with no t stem.')
dc(7,'material','c05','The complete Pi formula also has a headless shaft.')
dc(8,'material','c06','The old and new layers must both be represented; the older word is not fully separable and the live équivalence stays doubtful.')
dc(9,'material','c07','The initial word of the line is sera, without the final t needed for est.')
dc(10,'material','c08','The source has singular du morphisme structural; du is in c07 and the two nouns/adjective forms are in c08.')
dc(11,'material','c09','The second connective is again ou.')
dc(12,'material','c10','The structural Pi link is a literal shaft without a head.')
dc(13,'material','c11','The inserted spelling has dotted i before q: intrinsiquement.')
dc(14,'material','c12','The E link lacks an arrowhead; its small terminal nib is not silently made into one.')
dc(15,'material','c13','The a body and paired tall f stems support affiné.')
dc(16,'material','c14','E is now the first graphic reading, with Gamma retained because of possible overtracing.')
dc(17,'material','c15','The apparent opening parenthesis is the long insertion leader beneath the added phrase.')
dc(18,'material','c16','The marginal 15 is source ink missing from H; the comma versus closing parenthesis is separately recorded in c15.')
report=dict(scan=16,reader='reader_a',lines_read=25,changes=changes,decisions=decisions,inventory=inventory,notes=notes,checks=[],hand=hand,notation=notation,abbreviations=abbreviations,doubts=doubts,audit_boxes=audit,diff_coverage=diff)
(p/'edition/reviews/149_scan016.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'tex':'edition/reviews/149_scan016.tex','json':'edition/reviews/149_scan016.json','changes':len(changes),'C_departures':sum(x['against_C'] for x in changes),'decisions':len(decisions),'inventory':len(inventory),'audit_boxes':len(audit),'diff_rows':len(diff)},ensure_ascii=False))
