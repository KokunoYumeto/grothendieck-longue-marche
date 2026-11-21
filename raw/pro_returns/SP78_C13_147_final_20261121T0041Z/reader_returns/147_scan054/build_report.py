from pathlib import Path
import json
base=Path('/workspace/scratch/ea90d891106a/SP78_C13_147_work')
ret=base/'reader_returns/147_scan054'
boxes=json.loads((ret/'crop_boxes.json').read_text())
changes=[]
def ch(n,place,C,H,final,evidence,crop,confidence='high',against_C=False,against_H=True,kind='misread word',sheet='words',marked=False,consequential=False):
    changes.append(dict(id=f'054-{n:02}',place=place,C=C,H=H,final=final,evidence=evidence,crop=f'147_scan054_place{crop}.png',box=boxes[crop],confidence=confidence,against_C=against_C,against_H=against_H,kind=kind,marked_in_H=marked,error_sheet_kind=sheet,consequential=consequential))
ch(1,'physical line 1, dimension formula',r'\dim\operatorname{amb}G=\nu',r'\operatorname{dimmod}G=\nu',r'\dim\operatorname{mod}G=\nu','After dim, the suffix has compressed low m/o strokes followed by a separate rising d with a short descending return. It has neither the initial rounded a nor the looped final b visible in amb in the three lower formulas.','01',against_C=True,against_H=False,kind='misread symbol or index',sheet='symbols and indices',consequential=True)
ch(2,'physical line 4, cancellation immediately before Mais',r'\deleted{\unsure{Et}}',r'\struck{\ill{}}',r'\deleted{\unsure{Et}}','A left vertical with several horizontal remnants and a taller right stroke are compatible with Et. Multiple diagonal and horizontal cancellation strokes cross both letters; the complete letter shapes are not plain, so the C doubt is retained.','02',confidence='low',kind='other',sheet='struck text',marked=True)
ch(3,'insertion above physical line 5, after graphe',r'\inserted{\unsure{(top, compact)}}',r'(\add{top.\ connexe})',r'\inserted{\unsure{(top compact)|(top. compact)}}','The second word begins with an open c, has a descending p in the middle, and ends in a tall t before the closing parenthesis. Those strokes support compact rather than connexe. No independent comma is visible after top; a possible abbreviation point cannot be separated confidently from the insertion leader below. The leader bends down immediately after graphe.','03',confidence='medium',against_C=True,kind='misread word',sheet='words')
ch(4,'physical line 6, est homéom. à','homéom.','homéomorphe','homéom.','The word ends after the low m stroke with a separate dark point. There are no following r-p-h-e letters before à.','04',kind='abbreviation expanded or spelling modernised',sheet='abbreviations expanded spelling modernised')
ch(5,'physical line 7, replacement after et si',r"et si \deleted{il n'y a pas} \inserted{$G$ n'a pas} de",r"et s'il \struck{\ill{}} \add{n'a pas de}",r"et si \deleted{\unsure{il n'y a pas}} \inserted{$G$ n'a pas} de",'The unstruck si ends before the cancellation. The line crosses the following i/l uprights and the descending y and p of the old phrase, stopping before the baseline de. Above it the inserted initial is a large open G followed by n\'a pas; de remains at the baseline to its right. Portions of a/pas are hidden by the cancellation, so the old phrase is newly marked uncertain.','05',confidence='medium',kind='insertion or placement',sheet='insertions put in wrong place',marked=True)
ch(6,'physical line 7, de sommets d’ordre 2','sommets','sommet',r'\unsure{sommets|sommet}','The final connected upward-and-return stroke can be the compressed ts ending used in sommets elsewhere on the page, but it does not provide a separately legible s. The plural remains the first reading with the singular explicitly retained as an alternative.','05',confidence='medium')
ch(7,'insertion above physical line 8 and following au graphe',r'\inserted{isom.} au graphe',r'\add{\uncertain{le}} graphe',r'\inserted{isom\unsure{.}} au graphe','The small added group contains i-s-o-m above a curved leader that descends just before the baseline au. The baseline word has a closed a-like loop followed by a low u return, not a tall l. A separate point after isom is not securely distinguishable, so only that point is newly doubted.','05',confidence='medium',kind='omission',sheet='omissions',marked=True)
ch(8,'physical line 8, canceled word after graphe',r'\deleted{\unsure{qui}}',r'\struck{\ill{}}',r'\deleted{\unsure{qui}}','A long q descender remains below the cancellation at the left. The following low strokes are covered by a thick horizontal crossing, so qui is retained only as a tentative reading; the uncertainty is not resolved.','05',confidence='low',kind='other',sheet='struck text',marked=True)
ch(9,'physical line 11, qu’il est homéom. au cercle','homéom.','homéomorphe','homéom.','The final low m is followed immediately by a dark period and the separate au group; no r-p-h-e continuation is present.','06',kind='abbreviation expanded or spelling modernised',sheet='abbreviations expanded spelling modernised')
ch(10,'physical line 14, parenthetical words',r'(il doit être au moins $1$)',r'(il doit y en avoir au moins~1)',r'(il doit être au moins $1$)','After doit there is one compact word with an initial loop, a tall crossed/returning t stroke, and a short trailing re group. The following au moins is separate. There is no descending y, separate en, or long avoir group.','07')
ch(11,'physical line 14, location of the parenthesis',r'\deleted{de} (il doit être au moins $1$) est \inserted{donc} $1$ \unsure{ou} $2$',r'\struck{de} est \add{dans} $1\ldots2$, (il doit y en avoir au moins~1)',r'\deleted{de} (il doit être au moins $1$) est \inserted{donc} $1$ \unsure{ou} $2$','The parenthesis begins at the left margin on the next physical line after the canceled de and closes before est. The count 1 [ou] 2 is to the right of est on that same ascending line. H moves the parenthesis after the count.','07',kind='insertion or placement',sheet='insertions put in wrong place')
ch(12,'insertion above physical line 14, between est and 1','donc','dans','donc','The added word has an initial d loop and upright, followed by a low continuous o/n group and a final up-and-down c-like flick. There is no second closed a loop. Its curved leader descends between est and 1.','07',confidence='medium')
ch(13,'physical line 14, between the numbers 1 and 2',r'\unsure{ou}',r'\ldots',r'\unsure{ou}','There is a short raised initial tick followed by a long low connected stroke, not three distinct points. This can be the writer’s compressed ou, but the low stroke could also be a dash; the existing C doubt remains.','07',confidence='medium',kind='misread symbol or index',sheet='symbols and indices')
ch(14,'physical line 15, before the two small circles','ce qui donne','on a pour graphe','ce qui donne','The first group begins with a small open c/e loop; the next has the long q descender of qui; the last begins with the looped d and continues in two low connected groups. There is no tall p descender followed by the distinct graphe group seen earlier on the page.','08')
ch(15,'physical line 16, after En at end of previous line','résumé','somme','résumé','The word has the initial r stroke followed by a raised accent and the s/u/m sequence before the final low e stroke; it is longer than somme and starts with r rather than s.','09')
ch(16,'physical line 16, on trouve encore trois cas','encore','exactement','encore','The word begins in a small low e/n group and continues through a visible rounded o before the final r/e return. There is no x crossing, tall t, or the long additional -tement sequence.','09')
ch(17,'physical line 16, immediately after trois cas',':',', résumés en',':','The only writing after cas is a short punctuation group near the right end of the line. No letters for résumés en follow it before the drawings below.','09',kind='text not on the page',sheet='text not on page')
ch(18,'display (65), third row dimension formula',r'\nu=2-\dim\operatorname{amb}G',r'\nu=2=\dim\operatorname{amb}G',r'\nu=2-\dim\operatorname{amb}G','Between 2 and dim there is one dark horizontal stroke. A much paler short ghost lies below it, unlike both dark parallel strokes of the preceding equals sign. The dark ink supports the single minus kept by C; no second dark bar is supplied.','10',kind='misread symbol or index',sheet='symbols and indices',consequential=True)
ch(19,'bottom left foliation','53','[absent]',r'\margin{53}','The pale separate bottom-left hand shows a top-barred 5 with lower bowl, followed by a 3 with two right-hand lobes. It is distinct from the author’s black 26 at the top.','12',kind='omission',sheet='omissions')

inv=[]
def item(n,kind,pos,text,hand='his hand'):
    inv.append(dict(scan=54,sheet_kind='text',hand=hand,element=f'{n:02}',kind=kind,position=pos,first_words_or_objects=text,transcribed='yes'))
item(1,'margin note','top center','26')
item(2,'text','physical lines 1–4','b) h_1=1, donc dim mod G=ν; 0≤ν≤2; at most one end')
item(3,'deletion','line 4, before Mais','[Et?]')
item(4,'text','lines 4–6','Mais un graphe ... bout top. est homéom. à')
item(5,'insertion','above line 5, attached after graphe','(top [.] compact)')
item(6,'drawing','right end of line 6','one loop attached to a segment, with two marked vertices')
item(7,'text','line 7','et si ... de sommets [or sommet] d’ordre 2,')
item(8,'deletion','line 7','[il n’y a pas?]')
item(9,'insertion','above line 7','$G$ n’a pas')
item(10,'insertion','above line 8, attached before au','isom[.]')
item(11,'deletion','line 8, after graphe','[qui?]')
item(12,'text','lines 8–13','c’est qu’il est ... combinatoire ... au cercle ... de poids marqué 1, le nb de ces sommets')
item(13,'deletion','end of line 13','de')
item(14,'text','line 14','(il doit être au moins 1) est ... 1 [ou?] 2,')
item(15,'insertion','above line 14, before 1','donc')
item(16,'text','line 15','ce qui donne ... et ... . En')
item(17,'drawing','line 15','two circles, first with one marked vertex, second with two')
item(18,'text','line 16','résumé, on trouve encore trois cas :')
item(19,'display','lower left, spanning three rows','(65) and a left brace grouping the three cases')
item(20,'drawing','display row 1, left','one loop; vertex labelled 1')
item(21,'display','display row 1, middle','ν=1=dim amb G')
item(22,'drawing','display row 1, right','open nodal loop with two left branches and transverse mark labelled a')
item(23,'drawing','display row 2, left','two vertices labelled 1, joined by two arcs')
item(24,'display','display row 2, middle','ν=2=dim amb G')
item(25,'drawing','display row 2, right','two curves meeting twice, with separate transverse marks labelled a and b')
item(26,'drawing','display row 3, left','loop with one attached segment; free end labelled 2')
item(27,'display','display row 3, middle','ν=2−dim amb G')
item(28,'drawing','display row 3, right','crossing upper branches, a lower loop and an attached straight branch carrying a and b')
item(29,'margin note','bottom left','53',hand='unidentified pale foliation hand')

second=[]
def box(label,kind,b,reading):
    second.append(dict(box=label,kind=kind,x0=b[0],y0=b[1],x1=b[2],y1=b[3],reading=reading))
box('B01','handwritten number',[845,18,942,65],r'\mspage{26}')
box('B02','handwritten number',boxes['01'],r'b) $h_1=1$, donc $\dim\operatorname{mod}G=\nu$,')
box('B03','handwritten number',[296,166,537,236],r'$0\leq\nu\leq2$.')
box('B04','struck passage',[875,337,1450,423],r"d'ordre $3$. \deleted{\unsure{Et}} Mais")
box('B05','insertion',boxes['03'],r'\inserted{\unsure{(top compact)|(top. compact)}} avec $h_1=1$')
box('B06','word disagreement',boxes['04'],r'est homéom. à')
box('B07','struck passage',boxes['05'],r"et si \deleted{\unsure{il n'y a pas}} \inserted{$G$ n'a pas} de \unsure{sommets|sommet} d'ordre $2$, c'est qu'il est \inserted{isom\unsure{.}} au graphe \deleted{\unsure{qui}} combinatoire")
box('B08','word disagreement',boxes['06'],'homéom.')
box('B09','handwritten number',[780,1125,1082,1220],r"d'ordre $2$,")
box('B10','word disagreement',boxes['07'],r"marqué $1$, le nb de ces sommets \deleted{de} (il doit être au moins $1$) est \inserted{donc} $1$ \unsure{ou} $2$,")
smallfig=(ret/'proposed.tex').read_text().split('ce qui donne\n',1)[1].split('\nEn résumé',1)[0]
box('B11','word disagreement',boxes['08'],'ce qui donne\n'+smallfig+' En')
box('B12','word disagreement',boxes['09'],'résumé, on trouve encore trois cas :')
box('B13','handwritten number',[237,1845,385,1940],r'$(65)$')
box('B14','handwritten number',[565,1660,1255,1813],r'loop with one marked vertex labelled $1$; $\nu=1=\dim\operatorname{amb}G$')
box('B15','handwritten number',[570,1815,1274,1955],r'two vertices labelled $1$ and $1$, joined by two arcs; $\nu=2=\dim\operatorname{amb}G$')
box('B16','handwritten number',[560,1930,1285,2105],r'loop with a tail, free end labelled $2$; $\nu=2-\dim\operatorname{amb}G$')
box('B17','margin note',boxes['12'],r'\margin{53}')

report=dict(scan=54,reader='reader_a',physical_lines_read=19,changes=changes,
 decisions=[
 dict(id='M1026',cote=147,scan=54,decision='other',reading=r'\inserted{\unsure{(top compact)|(top. compact)}}',ink='The descending p and final tall t identify compact; connexe would have neither stroke. The presence of a point after top remains undecided; C’s comma is not independently visible.',crop='147_scan054_place03.png (470,420,852,548)',confidence='medium'),
 dict(id='M1027',cote=147,scan=54,decision='undecided',reading=r'$1$ \unsure{ou} $2$',ink='A raised initial tick precedes a low connected horizontal stroke. It can be compressed ou, but a dash cannot be excluded. H’s three-point ellipsis is not visible.',crop='147_scan054_place07.png (260,1220,1640,1480)',confidence='medium'),
 dict(id='D054-Et',cote=147,scan=54,decision='undecided',reading=r'\deleted{\unsure{Et}}',ink='Two letter-sized remnants survive, but crossing strokes hide parts of both; not every letter can be established.',crop='147_scan054_place02.png (1180,335,1450,416)',confidence='low'),
 dict(id='D054-qui',cote=147,scan=54,decision='undecided',reading=r'\deleted{\unsure{qui}}',ink='The q descender survives; the following strokes are merged into the horizontal cancellation.',crop='147_scan054_place05.png (280,640,1560,864)',confidence='low')],
 inventory=inv,
 doubts=[
 dict(place='line 4, struck word before Mais',reading='Et',alternatives='unreadable word',confidence='low',reason='Cancellation strokes cover portions of both proposed letters; C’s uncertainty is retained.'),
 dict(place='insertion above line 5',reading='(top compact)',alternatives='(top. compact)',confidence='medium',reason='The letters of compact are readable; a point after top cannot be isolated from the nearby insertion leader.'),
 dict(place='line 7, canceled phrase',reading="il n'y a pas",alternatives='parts of the canceled phrase unreadable',confidence='medium',reason='The y and p descenders and i/l uprights support the phrase, but the strike crosses the a/pas bodies; this doubt is added to C.'),
 dict(place='line 7, noun after de',reading='sommets',alternatives='sommet',confidence='medium',reason='The terminal ts can be compressed into the final rising-and-returning stroke, but a separate s is not certain; this doubt is added to C.'),
 dict(place='insertion above line 8',reading='isom.',alternatives='isom',confidence='medium',reason='Four letters are visible; a separate final abbreviation point is not secure. Only the point is newly doubted.'),
 dict(place='line 8, canceled word after graphe',reading='qui',alternatives='unreadable completion after q',confidence='low',reason='The long q descender survives; the following letters lie in the thick crossing stroke. C’s doubt is retained.'),
 dict(place='line 14, between 1 and 2',reading='ou',alternatives='a dash',confidence='medium',reason='The ink has a tiny leading tick and one flattened stroke, insufficient to decide cursive ou versus a dash. C’s doubt is retained.')],
 notes=[
 'All 16 physical body-text lines were read against the full-resolution halves, along with the three rows of display (65): physical_lines_read=19. The top page number 26, bottom foliation 53, four inserted spans, cancellations, and drawings were read separately and are inventoried rather than counted as additional physical lines.',
 'The manuscript treats the case h_1=1 under the stated bound 0≤ν≤2. It claims that a graph has at most one end, discusses the one-end graph as a circle with an attached segment, and discusses the end-free graph as a circle with one or two marked vertices. These are accounts of manuscript claims, not an independent proof of its classification.',
 'The first dimension formula is read dim mod G=ν, while the three case labels below read dim amb G. The difference is supported by the final d versus final b letter shapes and has not been normalized away.',
 'The third row reads ν=2−dim amb G. This may be an author slip, since the preceding rows have chained equalities, but the single dark bar is preserved. No claim that the minus equation is mathematically correct is made.',
 'The three combinatorial drawings have respectively (V,E)=(1,1),(2,2),(2,2), where the third has a self-loop plus a tail edge. Reading their displayed connectivity gives E−V+1=1 in each case. This small count checks consistency of the drawings with h_1=1 only; it does not prove the classification or the stated dimensions.',
 'The third curve drawing was cropped and traced visually once at place11. The lower straight branch carries a above b and continues upward only into the loop; the two curved branches cross farther above and continue separately. C’s TikZ connectivity and label order reproduce this, so no substantive drawing change is proposed.',
 'H’s editorial page label and drawing descriptions are treated as editorial surrogates, not source words. The descriptions were compared for objects and labels; their literal prose is not added to the transcription. Pure macro/wrapper differences, including the label add on baseline combinatoire, are not counted as text errors.',
 'All C deletions and insertions were checked for extent: Et is crossed before Mais; the line through il n’y a pas stops before baseline de; G n’a pas is above that line; isom is attached before au; the q-descender cancellation lies between graphe and combinatoire; de at the end of line 13 is crossed; donc is inserted before the count. The four insertion leaders are not mistaken for word punctuation.',
 '12 original-image crops were generated once each using Pillow autocontrast, LANCZOS scaling to 2200 or 2600 pixels wide, and modest sharpening; every crop was viewed. One view_image transport failure occurred before place08 returned an image; the already-saved crop was then viewed successfully without recropping.',
 'Proposed page only: the parent still needs to review disputed crops. There are 19 substantive final-versus-C/H change rows, of which 2 depart substantively from C; three additional C departures are certainty-only added doubts.'] ,
 check_events=[
 dict(statement_id='147-054-N1',date='2026-11-20 21:00:15 UTC',who='reader_a; GPT-6 Astra Pro, inherited effort not separately exposed',type='used and rechecked in this run',outcome='Read all body lines, display rows, insertions, cancellations, numbers, and drawings from scan/halves and the saved crops. This is a transcription check, not an independent proof.'),
 dict(statement_id='147-054-N2',date='2026-11-20 21:00:15 UTC',who='reader_a; GPT-6 Astra Pro, inherited effort not separately exposed',type='targeted proof check',outcome='Counted vertices and edges of the three left-side drawings and obtained E−V+1=1 for each. Did not verify completeness of the manuscript classification, marked-weight rules, or dimension formulas.')],
 notation=[
 dict(sign=r'\dim\operatorname{mod}G',reading='dim mod G in opening formula',evidence='Opening suffix ends with an ascending d; lower amb suffixes end with looped b.',scope='scan 54 opening line only'),
 dict(sign=r'\dim\operatorname{amb}G',reading='dim amb G in the three displayed cases',evidence='Rounded initial a and tall final b with small low loop are visible in all three lower formulas.',scope='scan 54 display (65)'),
 dict(sign=r'\nu',reading='Greek nu',evidence='Pointed lower join and long curved right arm, distinct from the straight handwritten digit 1.',scope='all five ν occurrences on scan 54')],
 hand_log=[
 dict(habit='Capital G is very open and can resemble C, with a short lower-right return.',pages=[54],all_occurrences='Consistent in the opening formula, body G, inserted G, and three lower formulas (six occurrences).',witness_misreadings='No G/C witness disagreement here; this is a local reading aid.'),
 dict(habit='Compressed mod can be mistaken for amb unless the final upright d is compared with the looped b.',pages=[54],all_occurrences='mod occurs once in the opening formula; amb occurs three times in display (65). The suffix distinction is consistent in these four formulas.',witness_misreadings='C reads amb in the first formula; H preserves mod.'),
 dict(habit='Short function words can collapse into a tiny raised initial stroke plus a low horizontal trace.',pages=[54],all_occurrences='The ou between 1 and 2 remains uncertain; no universal letter-identification rule is asserted.',witness_misreadings='C tentatively reads ou; H renders an ellipsis. The ink does not settle ou versus a dash.')],
 abbreviations=[dict(written='top / top.',expansion='topologique'),dict(written='homéom.',expansion='homéomorphe'),dict(written='isom[.]',expansion='isomorphe'),dict(written='nb',expansion='nombre'),dict(written='dim',expansion='dimension'),dict(written='amb',expansion='ambiante')],
 second_boxes=second,
 unresolved=['Punctuation after top in the insertion.','Full readings of canceled Et, il n’y a pas, and qui.','Final s of sommets in line 7.','Presence of an abbreviation point after inserted isom.','ou versus a dash between the count values 1 and 2.'],
 witness_comparison='C is substantially closer to the prose, actual abbreviations, location of the parenthesis, drawn objects, and final single minus. H correctly distinguishes opening dim mod from the lower dim amb, but expands homéom., changes compact to connexe, alters replacement wording and several later phrases, and regularizes the final minus to equals. Neither witness settles the heavily canceled words or the flattened count connector.')
(ret/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print('report.json:',len(changes),'change rows;',len(inv),'inventory elements;',len(second),'second boxes')
