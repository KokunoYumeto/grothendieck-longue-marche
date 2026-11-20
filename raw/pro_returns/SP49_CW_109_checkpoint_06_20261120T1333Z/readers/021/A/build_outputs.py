from pathlib import Path
import json, re, difflib
out=Path('work/readers/021/A')
C=Path('work/inputs/021/C.tex').read_text()
reading=C
replacements=[
 (r'\deleted{\unsure{a|a l}}\unsure{a} bit',r'\deleted{\unsure{a|a l}}a bit'),
 (r'line 8 \unsure{``}is',r'line 8 ``is'),
 (r'\deleted{\unsure{p.}} line -15',r'\deleted{p.} line -15'),
 (r'\unsure{occurences|occurrences}',r'occurences'),
 (r'English\unsure{.}',r'English.'),
 (r'\deleted{\unsure{p}} line -16',r'\deleted{p} line -16'),
 (r'\deleted{\unsure{ha}}',r'\deleted{ha}'),
 (r'K\deleted{\unsure{h}}an',r'K\makebox[0pt][l]{\raisebox{1.1ex}{\deleted{\unsure{h}}}}an'),
]
for a,b in replacements:
 assert reading.count(a)==1,(a,reading.count(a))
 reading=reading.replace(a,b)
# Zero-size anchors preserve the confirmed running text and locate the visible ruled lines.
reading=reading.replace(r'\unsure{p.} \unsure{77|11}',r'\tikz[remember picture,overlay]\coordinate (scxxitop);\unsure{p.} \unsure{77|11}',1)
reading=reading.replace('p.87 line 8',r'\tikz[remember picture,overlay]\coordinate (scxxifainttop);p.87 line 8',1)
reading=reading.replace(r'\deleted{p} line -16',r'\tikz[remember picture,overlay]\coordinate (scxxifaintbottom);\deleted{p} line -16',1)
reading=reading.replace(r'p.115\unsure{:}',r'\tikz[remember picture,overlay]\coordinate (scxxibottom);p.115\unsure{:}',1)
extra_rules=r'''% Visible side rules and the fainter partial rule at far left.
\coordinate (scxxileftedge) at ([xshift=-.5em]scxxitop);
\coordinate (scxxirightedge) at ([xshift=.92\linewidth]scxxitop);
\coordinate (scxxifaredge) at ([xshift=-5em]scxxitop);
\draw[overlay,thin] ([yshift=1ex]scxxileftedge) -- ([yshift=-2ex]scxxileftedge |- scxxibottom);
\draw[overlay,thin] ([yshift=1ex]scxxirightedge) -- ([yshift=-3ex]scxxirightedge |- scxxibottom);
\draw[overlay,gray,very thin] (scxxifaredge |- scxxifainttop) -- ([yshift=3ex]scxxifaredge |- scxxifaintbottom);
'''
reading=reading.replace('% archive sheet number: 20',r'\figure{\begin{tikzpicture}[remember picture,overlay]'+'\n'+extra_rules+r'\end{tikzpicture}}'+'\n\n% archive sheet number: 20',1)
(out/'reading.tex').write_text(reading)
(out/'C_to_reading.diff').write_text(''.join(difflib.unified_diff(C.splitlines(True),reading.splitlines(True),fromfile='work/inputs/021/C.tex',tofile='work/readers/021/A/reading.tex')))

root='/workspace/scratch/6d55c8c3e5a7/'
whole=root+'source/SP49_CW_109_scans/H109-02_109_scan021.jpg'
ha=root+'source/SP49_CW_109_scans/H109-02_109_scan021_a.jpg'
hb=root+'source/SP49_CW_109_scans/H109-02_109_scan021_b.jpg'
crop_defs=[
 ('01_top_reference',[245,58,839,177]),('02_top_erasure',[839,57,1475,177]),('03_have_underlining',[545,181,800,250]),('04_overwritten_article',[1258,237,1518,318]),('05_is_opener',[535,368,785,443]),('06_cancelled_page_indicator',[225,446,399,524]),('07_occurrences_note',[1305,555,1610,695]),('08_not_neither',[517,674,898,752]),('09_cancelled_digit',[1069,676,1464,757]),('10_english_punctuation',[1058,1059,1345,1136]),('11_cancelled_or',[865,1124,1176,1208]),('12_cancelled_p',[251,1255,433,1323]),('13_cancelled_ha',[424,1375,669,1454]),('14_saturation_mark',[716,1759,966,1832]),('15_kan_deletion',[597,1815,771,1883]),('16_khan_spelling',[837,1809,1030,1887]),('17_relationships_underlining',[661,1954,894,2035]),('18_p115_punctuation',[266,2205,511,2274])]
def loc(n):
 name,box=crop_defs[n-1]
 return {'crop':root+str(out/'crops'/f'{name}.jpg'),'source':whole,'bbox':box}
def change(cid,place,c,new,kind,confidence,evidence,n=None,box=None):
 d={'id':cid,'place':place,'c':c,'h':None,'reading':new,'diff_c':True,'diff_h':False,'kind':kind,'marked_in_H':False,'confidence':confidence,'evidence':evidence}
 d.update(loc(n) if n else {'crop':None,'source':whole,'bbox':box})
 return d
changes=[
 change('p88-live-article','p.88 line 2, live article before bit',r'\deleted{\unsure{a|a l}}\unsure{a} bit',r'\deleted{\unsure{a|a l}}a bit','misread word','high','The live right-hand loop closes and exits along the baseline into the space before bit. It is a; uncertainty about the buried earlier group is retained separately.',4),
 change('p89-is-opener','p.89 line 8, sign before is',r'line 8 \unsure{``}is',r'line 8 ``is','misread symbol or index','high','The dark raised mark has two downward legs separated at their lower ends, matching a joined pair of opening quotation strokes. No closing quotation is supplied after is.',5),
 change('p89-deleted-p','p.89 line -15, cancelled page indicator',r'\deleted{\unsure{p.}} line -15',r'\deleted{p.} line -15','misread word','high','A long descender and an upper right oval survive beneath two oblique cancellation strokes. The independent low dot to the right is clear.',6),
 change('p90-occurences','p.90 line -15, right marginal note',r'\unsure{occurences|occurrences}',r'occurences','misread word','medium','After the two open c curves, the compressed u is followed by one small r shoulder and then a closed e. I read one r and retain the manuscript spelling occurences.',7),
 change('p91-english-period','p.91 unnumbered line, after English',r'English\unsure{.}',r'English.','misread symbol or index','high','A separate dark low point stands to the right of the h terminal, with a visible white gap; it is not connected to h.',10),
 change('p91-deleted-p','p.91 line -16, cancelled page indicator',r'\deleted{\unsure{p}} line -16',r'\deleted{p} line -16','misread word','high','The lower upright descender and small right bowl remain visible through the crossing diagonal; no separate dot follows it.',12),
 change('p99-deleted-ha','p.99, cancelled group between X and Y',r'\deleted{\unsure{ha}}',r'\deleted{ha}','misread word','high','The cancelled group retains a looped ascender with low h shoulder followed by a closed a bowl and its exit. The reading comes from these two letter shapes.',13),
 change('p107-raised-deletion','p.107 line -3, cancelled mark above a of first name',r'K\deleted{\unsure{h}}an',r'K\makebox[0pt][l]{\raisebox{1.1ex}{\deleted{\unsure{h}}}}an','insertion or placement','high','The cancelled patch is above the a rather than on the live baseline between K and a. Its placement is clear; the interior letter remains doubtful. There is no visible caret requiring insertion markup.',15),
 change('left-side-rule','Long rule just left of the reference column','',r'\draw[overlay,thin] ([yshift=1ex]scxxileftedge) -- ([yshift=-2ex]scxxileftedge |- scxxibottom);','drawing or diagram','high','A thin nearly vertical black rule runs from beside the top faded reference past the divider to below the final entry. C has no corresponding side-rule command.',box=[232,88,258,2295]),
 change('right-side-rule','Long rule near the right side of the sheet','',r'\draw[overlay,thin] ([yshift=1ex]scxxirightedge) -- ([yshift=-3ex]scxxirightedge |- scxxibottom);','drawing or diagram','high','A thin nearly vertical black rule begins beside the top line, crosses the marginal note and horizontal divider, and continues down the sheet. C has no corresponding side-rule command.',box=[1507,82,1543,2323]),
 change('far-left-partial-rule','Faint partial rule farther left of the reference column','',r'\draw[overlay,gray,very thin] (scxxifaredge |- scxxifainttop) -- ([yshift=3ex]scxxifaredge |- scxxifaintbottom);','drawing or diagram','medium','A separate faint vertical trace stands well left of the main reference-column rule, beginning around p.87 height and ending in the p.91 example paragraph. It is reproduced without assigning a function to it.',box=[61,199,82,1202]),
]

def doubt(place,c,new,resolved,confidence,evidence,n):
 return {'place':place,'c':c,'reading':new,'resolved':resolved,'confidence':confidence,'evidence':evidence,**loc(n)}
D=[]
D.append(doubt('top washed line, initial reference',r'\unsure{p.}',r'\unsure{p.}',False,'low','Only a lower sloping upright survives. Neither the bowl nor the punctuation can be independently recovered; the supplied tentative reading remains explicitly doubtful.',1))
D.append(doubt('top washed line, page number',r'\unsure{77|11}',r'\unsure{77|11}',False,'low','Two short oblique numeral feet survive; the lost upper strokes do not distinguish 77 from 11. Sequence is not used as evidence.',1))
D.append(doubt('top washed line, first quoted-form position',r"\unsure{isn't|is'nt}",r"\unsure{isn't|is'nt}",False,'low','Low i/s/n/t-like remnants are present, but the apostrophe-height region is washed out. Its position cannot be read.',1))
D.append(doubt('top washed line, intervening word',r'\unsure{not}',r'\unsure{not}',False,'low','The low rounded and hooked remnants are compatible with not but insufficient to make the word certain.',1))
D.append(doubt('top washed line, second quoted-form position',r"\unsure{is'nt|isn't}",r"\unsure{is'nt|isn't}",False,'low','Only lower letter strokes are visible, independently of the first occurrence; the apostrophe is again lost.',1))
D.append(doubt('top washed continuation, erased words',r'\illegible{3}',r'\illegible{3}',False,'low','The long washed band contains scattered baseline traces and one lower upright but no recoverable whole words; three is an approximate count, not a reconstruction.',2))
D.append(doubt('top washed continuation, remnants before form',r'\unsure{er}',r'\unsure{er}',False,'low','A small loop and rightward rising hook survive before form; er is retained as a fragment, with no missing beginning supplied.',2))
D.append(doubt('p.88 line 2, cancelled article',r'\deleted{\unsure{a|a l}}',r'\deleted{\unsure{a|a l}}',False,'low','The old rounded group is crossed and merged with the live a. An additional upright cannot be securely separated from the superposed letter, so the old group is not resolved by the replacement.',4))
D.append(doubt('p.88 line 2, live article',r'\unsure{a}',r'a',True,'high','The right closed loop and baseline exit distinguish the live a from the overwritten strokes to its left.',4))
D.append(doubt('p.89 line 8, opening quotation',r'\unsure{``}',r'``',True,'high','Two lower pendant legs are visible in the joined raised mark.',5))
D.append(doubt('p.89 line -15, cancelled reference',r'\deleted{\unsure{p.}}',r'\deleted{p.}',True,'high','The descender, right bowl and independent following dot are separately visible beneath the cancellation.',6))
D.append(doubt('p.90 line -15, marginal spelling',r'\unsure{occurences|occurrences}',r'occurences',True,'medium','The enlarged medial group shows one r shoulder between u and e; no second r is distinguishable as a written stroke.',7))
D.append(doubt('p.90 cancelled not -- neither, possible initial parenthesis',r'\unsure{(}',r'\unsure{(}',False,'low','The upright at the left joins a sweeping cancellation stroke. A prior parenthesis cannot be separated from it with confidence, and its possible presence remains marked.',8))
D.append(doubt('p.90 line -9, old cancelled figure',r'\unsure{4|14}',r'\unsure{4|14}',False,'low','An old right descending stem and crossbar suggest 4; the additional left upright may be an earlier 1 or part of the dense cancellation. The live 9 is clear.',9))
D.append(doubt('p.91 unnumbered line, after English',r'\unsure{.}',r'.',True,'high','A distinct low dot lies beyond a white gap to the right of the h terminal.',10))
D.append(doubt('p.91 cancelled example, conjunction after car',r'\unsure{or}',r'\unsure{or}',False,'low','The initial rounded stroke is visible, but the right-hand letter is entangled with a tall cancelling zigzag; or is a candidate, not a recovered certain word.',11))
D.append(doubt('p.91 line -16, cancelled reference',r'\unsure{p}',r'p',True,'high','The descender and right-hand bowl remain identifiable beneath the diagonal cancellation.',12))
D.append(doubt('p.99, cancelled group before Y',r'\unsure{ha}',r'ha',True,'high','There is a looped h ascender and shoulder, then a closed low a; the crop resolves both letters independently of have following Y.',13))
D.append(doubt('p.107 line 14, cancelled letter after saturation',r'\unsure{t}',r'\unsure{t}',False,'low','The cancelled vertical and crossing strokes permit t, but the dense zigzag masks its outline. A separate short dash to its right is clear.',14))
D.append(doubt('p.107 line -3, raised cancelled letter',r'\unsure{h}',r'\unsure{h}',False,'low','Only a black stack of small crossing strokes survives above a. The h reading remains tentative; it is not inferred from the name in the following quotation.',15))
D.append(doubt('p.107 line -3, second name',r'\unsure{Khan|Khân}',r'\unsure{Khan|Khân}',False,'low','K and the tall h stem are visible; the following a and raised marks are overdrawn. A separate circumflex cannot be established or excluded.',16))
D.append(doubt('p.115, punctuation after page number',r'\unsure{:}',r'\unsure{:}',False,'low','There is a lower point and a higher slanting short stroke before line; their uneven spacing and shape do not securely establish a colon.',18))
# Context alternatives that are not literal changes to C.
D.extend([
 {'place':'p.88 line 2, context apostrophe alternatives','c':r"``does'nt'' should be ``doesn't''",'reading':r"``does'nt'' should be ``doesn't''",'resolved':True,'confidence':'high','evidence':'The half shows the raised apostrophe before n in the first form and after n in the replacement; the misplaced form is quoted, not silently regularized.','crop':None,'source':ha,'bbox':[529,238,1106,314]},
 {'place':'p.107 line 5, context apostrophe alternatives','c':r"``is'nt'' again replace by ``isn't''",'reading':r"``is'nt'' again replace by ``isn't''",'resolved':True,'confidence':'high','evidence':'The lower half independently shows the first apostrophe before n and the replacement apostrophe after n.','crop':None,'source':hb,'bbox':[560,584,1120,671]},
 {'place':'p.91 line -16, context spelling alternatives','c':r"``avatars'' not ``avators''",'reading':r"``avatars'' not ``avators''",'resolved':True,'confidence':'high','evidence':'The first quoted word has a after t and the second has o after t. The spelling opposition is plainly visible in the lower half.','crop':None,'source':hb,'bbox':[550,148,1169,210]}
])

remaining=[]
for d in D:
 if not d['resolved']:
  m=re.search(r'\\unsure\{([^{}]*)\}',d['reading'])
  remaining.append({'place':d['place'],'reading':d['reading'],'alternatives':m.group(1) if m else 'approximately three unreadable words; no lexical candidates recovered','confidence':d['confidence'],'reason':d['evidence']})

inventory=[]
def inv(e,kind,pos,words,hand='another unnamed hand',sheet='list'):
 inventory.append({'sheet_kind':sheet,'hand':hand,'element':e,'kind':kind,'position':pos,'first_words_or_objects':words,'transcribed':'yes'})
for args in [
 ('01','text','Top washed line and continuation','p. 77|11 line 12 ... later (i.e ...'),
 ('02','text','Upper block, p.87 line 8','we have only got to'),
 ('03','text','Within p.87 entry, underlined span','have — one underline'),
 ('04','text','Upper block, p.88 line 2',"does'nt should be doesn't"),
 ('05','deletion','p.88 before live a bit','cancelled a|a l'),
 ('06','text','Upper block, p.89 line 3','to have got me'),
 ('07','text','p.89 line 8','is very necessary?'),
 ('08','text','p.89 line -15 and its continuation','last not least ... an alternative would be'),
 ('09','deletion','Left of p.89 line -15','p.'),
 ('10','text','p.90 line -15','compare takes with as does commute'),
 ('11','margin note','Right of p.90 line -15','(4 occurences on this page)'),
 ('12','drawing','Around left and lower edge of the occurrence note','rounded left return continuing into long low rule'),
 ('13','text','Below p.90 line -15, entire cancelled line','also this line -15 has a double negative'),
 ('14','deletion','Same full line','cancellation through also this line -15 has a double negative'),
 ('15','text','Next p.90 line','not -- neither; isn\'t line -9 (twice)'),
 ('16','deletion','Left portion of that line','possible ( and not -- neither'),
 ('17','deletion','Within line reference before live 9','4|14'),
 ('18','text','p.90 line -8, with wrapped words','replace comma by that - would give better flow of words'),
 ('19','text','p.91 line 1','in view of indicates a result of previous happenings'),
 ('20','text','Next line, separate quoted comparison','with the view to indicates future hopes & expectations.'),
 ('21','text','p.91 unnumbered line and following parenthetical','we\'ve got or we have got; We got is used in standardish English.'),
 ('22','deletion','After English.','only'),
 ('23','deletion','After in phrases like','we got into the car'),
 ('24','deletion','Between cancelled car example and live We got example','or, doubtful'),
 ('25','text','p.91 line -16','avatars not avators'),
 ('26','deletion','Left of p.91 line -16','p'),
 ('27','text','p.92 entry','line -16 probably informal (repeated line -3)'),
 ('28','text','p.99 entry','X ... Y have got changed to F, G it seems.'),
 ('29','deletion','Between X and Y','ha'),
 ('30','text','p.100 line -16','having the same objects'),
 ('31','text','Within p.100 phrase, underlined span','the — one underline'),
 ('32','margin note','Right below p.100 entry, above horizontal rule','Sent 19/12/83'),
 ('33','deletion','Large upper block above the horizontal divider','block crossed by two long oblique strokes'),
 ('34','drawing','Upper cancellation, left diagonal','oblique stroke from around p.88 toward p.99'),
 ('35','drawing','Upper cancellation, right diagonal','oblique stroke from around p.90 toward p.100'),
 ('36','drawing','Below p.100 and Sent note','long slightly undulating horizontal divider'),
 ('37','drawing','Left side beside reference column','thin long vertical side rule'),
 ('38','drawing','Right side of sheet','thin long vertical side rule'),
 ('39','drawing','Far left, partial upper-page trace','faint partial vertical rule'),
 ('40','text','Below divider, p.102 line -1','commute with again'),
 ('41','text','Within p.102 phrase, underlined span','with — one underline'),
 ('42','text','p.105 line 7','developing (single p.)'),
 ('43','text','p.107 line 5',"is'nt again replace by isn't also in line -5."),
 ('44','insertion','Above also / line -5, with caret below','in'),
 ('45','text','p.107 line 14','saturation, cancelled short mark, dash'),
 ('46','deletion','After saturation closing quotation','t, doubtful'),
 ('47','text','p.107 line -3','Kan not Khan|Khân'),
 ('48','deletion','Raised above a of first Kan','h, doubtful, cancelled'),
 ('49','text','p109 line -9',"isn't"),
 ('50','text','p.111 line 19','relationships.'),
 ('51','text','Medial s within relationships','two short underlining strokes'),
 ('52','text','p.112 line 14',"we'll say we've got"),
 ('53','text','p.113 line 15','commute with repeat line -15'),
 ('54','text','Following line -14',"we've got or simply we have"),
 ('55','text','Final p.115 entry','line -5 & 6, commute with'),
]:inv(*args)
inv('56','text','Bottom left archive corner, comment only','archive sheet number: 20','another unnamed pencil hand')

notes=[
 'The sheet is an English list of wording and spelling remarks. The top reference and part of its first line are washed out; only fragments are recoverable. There is no title and no stated page count.',
 'The upper list runs through p.100 and is crossed by two long oblique strokes. A horizontal rule separates the continuing entries for pp.102–115 below. The exact drawn marks, local cancellations and the later supralinear in are retained.',
 'At p.89 the writer offers or alternatively to have made me, asks whether very is necessary, and gives an alternative would be last, not least,. At p.90 line -8 the proposed replacement would give better flow of words.',
 'The right note at p.90 states 4 occurences on this page. The same region has a cancelled double-negative remark and an entry ending (twice).',
 'At p.91 the two phrases in view of and with the view to are distinguished by previous happenings versus future hopes & expectations; the parenthetical examples contain two local cancellations.',
 'The p.92 suggestion remains qualified by probably and records repetition at line -3. The p.99 notation remark reads X, cancelled ha, Y have got changed to F, G it seems.; its final qualification is retained.',
 'Sent 19/12/83 appears at the right above the horizontal rule. It is a dispatch note, not a heading or an inferred composition date.',
 'The lower block revisits commute with, contractions and spellings, including developing (single p.), the Kan / Khan|Khân comparison, and the short repeated underline under the medial s of relationships. The numbered page/line references are references to a text being corrected, not this sheet’s pagination.',
 'The lower-left 20 is an archive sheet number and is represented only as a TeX comment. No mathematical claim appears that warranted a substantive mathematical check.'
]
notation=[
 {'sign':'page and line references','location':'throughout, especially p109 and negative line references','reading':r'p.87 line 8; p109 line -9','evidence':'The page labels have variable punctuation; p109 has no visible stop after p. Short horizontal strokes precede bottom-counted line numerals. C is confirmed.'},
 {'sign':'double opening quotation strokes','location':'p.89 line 8, before is','reading':'``','evidence':'Crop 05 separates the two lower legs of the compact raised opening mark.'},
 {'sign':'apostrophe position','location':'p.88 line 2 and p.107 line 5','reading':r"does'nt / doesn't; is'nt / isn't",'evidence':'Both halves independently show the apostrophe before or after the low n as quoted. The lost top occurrence remains uncertain on its own ink.'},
 {'sign':'ordinary capitals','location':'p.99 notation remark','reading':r'$X$, $Y$, $F, G$','evidence':'The lower half shows ordinary single-stroke capitals with no changed alphabet, subscript, superscript or extra operation. The comma between F and G is present.'},
 {'sign':'single underlines','location':'p.87 have; p.100 the; p.102 with','reading':r'\uline{have}; \uline{the}; \uline{with}','evidence':'Crop 03 shows one broad single underline below have; the lower half clearly confines the other two lines to the respective words.'},
 {'sign':'repeated short underline','location':'p.111, medial s of relationships','reading':r'relation\uuline{s}hips','evidence':'Crop 17 shows a short retraced upper mark and a separate lower horizontal mark under the medial s; their short extent does not reach the full word.'},
 {'sign':'missing closing delimiters','location':'p.88 parenthetical beginning; p.90 isn\'t quotation','reading':r"(``is'nt'' occurs ...; ``isn't line -9 (twice)",'evidence':'The upper half supplies no closing parenthesis for the p.88 comment and no closing quote after the p.90 isn\'t. They are not supplied editorially.'},
 {'sign':'raised cancelled mark','location':'p.107 first Kan','reading':r'K\makebox[0pt][l]{\raisebox{1.1ex}{\deleted{\unsure{h}}}}an','evidence':'Crop 15 places the cancelled group above a. Placement is certain, interior h is not.'},
]
abbreviations=[
 {'form':'p. / p','expansion':'page (tentative expansion only)','place':'reference column'},
 {'form':'i.e','expansion':'id est / that is (interpretation only)','place':'top continuation'},
 {'form':'p.','expansion':'letter p (interpretation, not page)','place':'p.105 entry, (single p.)'}
]
report={
 'scan':21,'reader':'A','model':'GPT-6 Astra Pro','effort':'not exposed',
 'viewed':[whole,ha,hb],
 'layout':'One handwritten correction list on an unheaded sheet. A washed top line continues on the following line. The upper block has page/line references at left, a right-side parenthetical occurrence note with a drawn return rule, numerous local cancellations, and two long oblique cancellation strokes. A right-hand Sent 19/12/83 note precedes a slightly undulating horizontal divider. The lower block continues the corrections through p.115; in is added above the p.107 line with a caret, and a cancelled patch is raised above the a of Kan. Two long near-vertical side rules flank the principal text; a fainter partial rule lies farther left. No typescript, formula display, mathematical diagram, title or manuscript pagination is present. A pencilled archive 20 is at the lower-left corner.',
 'changes':changes,'c_doubts':D,'remaining_doubts':remaining,'inventory':inventory,'notes':notes,'math_checks':[],
 'notation':notation,'abbreviations':abbreviations,
 'brief_feedback':'Read the complete brief, conventions, preamble, C, H description, C_context and shared notation supplied for scan 021. Received and read C_context_addendum.md after the halves and first crops; it introduced no new unresolved locus. The whole and each supplied half were displayed exactly once, followed by exactly one enhanced tight crop per planned unresolved locus (18 crops); no crop was repeated. H is descriptive only, so all h fields are null and there are no H collation rows. No OCR, web, other scan, peer reading or subagent was used. Existing line wording, absent closing delimiters and punctuation were compared literally with C before reporting a difference. Zero-size TeX anchors support the drawings and are not counted as text differences. The ruled-line placement is an approximation relative to the transcribed blocks, not a claim that these traces have a specific editorial function. The full inventory includes every list entry, the independent marginal notes, each local deletion and insertion, underline spans, the broad upper cancellation, its strokes and divider, and the visible rules. C_to_reading.diff records all source changes. Parent handles persistence.'
}
(out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
# Standalone readable inventory and content notes complement the structured fields.
lines=['# Scan 021 — reader A inventory','', '| Element | Kind | Position | First words / object | State |', '| --- | --- | --- | --- | --- |']
for r in inventory:
 lines.append('| '+ ' | '.join(str(r[k]).replace('|',' / ') for k in ['element','kind','position','first_words_or_objects','transcribed'])+' |')
(out/'inventory.md').write_text('\n'.join(lines)+'\n')
(out/'notes.md').write_text('# Scan 021 — reader A notes\n\n'+'\n\n'.join(notes)+'\n')
viewlog=json.loads((out/'view_log.json').read_text())[:3]
for i,(name,box) in enumerate(crop_defs,4):
 viewlog.append({'order':i,'source':root+str(out/'crops'/f'{name}.jpg'),'purpose':'single enhanced tight inspection of an unresolved locus','display_count':1,'original_source':whole,'bbox':box})
(out/'view_log.json').write_text(json.dumps(viewlog,indent=2)+'\n')
# Literal witness excerpts must really occur, and all proposed replacements must occur.
for ch in changes:
 assert ch['c']=='' or ch['c'] in C,('nonliteral C',ch['id'])
 assert ch['reading'] in reading,('missing reading',ch['id'])
assert len(re.findall(r'\\unsure\{',C))==21
assert len(re.findall(r'\\unsure\{',reading))==14
assert len(changes)==11
assert len(D)==25
assert len(remaining)==15
assert len(inventory)==56
assert len(viewlog)==21
print(json.dumps({'changes':len(changes),'c_doubt_decisions':len(D),'core_C_doubts_resolved':7,'context_confirmations':3,'remaining_doubts':len(remaining),'inventory_elements':len(inventory),'crops_viewed':len(crop_defs),'math_checks':0},indent=2))
