from pathlib import Path
import json, csv, difflib

root = Path('/workspace/scratch/6d55c8c3e5a7')
out = root / 'work/readers/021/C'
src = root / 'source/SP49_CW_109_scans'
a = str(src / 'H109-02_109_scan021_a.jpg')
b = str(src / 'H109-02_109_scan021_b.jpg')
whole = str(src / 'H109-02_109_scan021.jpg')
c_text = (root / 'work/inputs/021/C.tex').read_text()
reading = c_text

changes = []
def change(id, place, old, new, kind, confidence, evidence, crop=None, source=None, bbox=None, replace=True):
    global reading
    if replace:
        assert old in c_text, (id, 'literal not found in C', old)
        assert old in reading, (id, 'literal not found in current reading', old)
        reading = reading.replace(old, new, 1)
    changes.append(dict(id=id, place=place, c=old, h=None, reading=new,
                        diff_c=True, diff_h=False, kind=kind, marked_in_H=False,
                        confidence=confidence, evidence=evidence,
                        crop=('crops/'+crop+'.jpg') if crop else None,
                        source=source, bbox=bbox))

change('top-dash', 'Clipped first line, after the second contraction',
       r'\unsure{is\'nt|isn\'t} --'.replace('\\\'', "'"),
       r'\unsure{is\'nt|isn\'t} \unsure{--}'.replace('\\\'', "'"),
       'misread symbol or index', 'low',
       'Only pale horizontal remnants survive at the start of the erased band. A dash is possible, but the surviving stroke cannot be separated securely from the word remnants. It is now explicitly doubtful.',
       '02_top_right', a, [837,52,1475,140])

change('p88-period', 'p.88 reference, period after p', 'p.88 line 2', r'p\unsure{.}88 line 2',
       'misread symbol or index', 'low',
       'A separate pale rounded spot is present between p and 88 at the expected baseline. Its much weaker impression does not securely distinguish punctuation from a blemish, so the period is retained with doubt.',
       '20_p88_reference', a, [244,250,367,316])

change('p88-live-a', 'p.88 line 2, live article before bit',
       r'\deleted{\unsure{a|a l}}\unsure{a} bit', r'\deleted{\unsure{a|a l}}a bit',
       'misread word', 'high',
       'The rightmost small oval has an a-shaped exit into the following space before bit. The overwritten left loops remain uncertain; only the live article is resolved.',
       '03_article', a, [1207,243,1665,315])

change('p89-opener', 'p.89 line 8, mark before is', r'\unsure{``}is', r'\unsure{``|`}is',
       'misread symbol or index', 'low',
       'The heavy opening mark has two uneven downward projections but is fused; a double opener is favoured, while a single thick opener remains possible.',
       '04_line8_opener', a, [540,370,1000,442])

change('p89-deleted-p', 'p.89 line -15, cancelled left reference',
       r'\deleted{\unsure{p.}} line -15', r'\deleted{p.} line -15',
       'misread word', 'high',
       'The half shows a long p descender, a right upper bowl and a separate following dot. Two oblique deletion strokes cross the letter without obscuring those features.',
       None, a, [231,452,292,521])

change('p90-occurences', 'p.90 marginal parenthesis, word after 4',
       r'\unsure{occurences|occurrences}', 'occurences',
       'misread word', 'medium',
       'After the second c, the small joined group has the two turns of u followed by one r shoulder before the e loop. I read one r and retain the nonstandard spelling occurences.',
       '05_occurrences', a, [1305,550,1611,694])

change('p90-strike-start', 'p.90 cancelled not -- neither, initial mark',
       r'\deleted{\unsure{(}not -- neither}', r'\deleted{not -- neither}',
       'text not on the page', 'high',
       'The upright at the left turns sharply into the first long rising cancellation stroke. It is continuous with the zigzag deletion, not a separate curved opening parenthesis.',
       '06_not_neither', a, [520,681,897,750])

change('p91-stop', 'p.91 unnumbered line, after English',
       r'English\unsure{.}', 'English.', 'misread symbol or index', 'high',
       'A discrete dark horizontal point is separated by white space from the terminal downstroke of h and precedes the crossed-out only. It is a period.',
       '09_english_stop', a, [1052,1072,1321,1146])

change('p99-ha', 'p.99, cancelled letters between X and Y',
       r'\deleted{\unsure{ha}}', r'\deleted{ha}', 'misread word', 'medium',
       'A tall looped h ascender and its low shoulder remain visible at left, and an a oval with its exit remains visible at right. Only ha is read; no further letters are supplied.',
       '12_deleted_ha', b, [470,270,567,340])

change('p102-opener', 'p.102 line -1, opening quotation before commute',
       'p.102 line -1, ``commute', r'p.102 line -1, \unsure{`|``}commute',
       'misread symbol or index', 'low',
       'The opener is a single connected upright with a left spur and a lower rightward hook. A single quote is favoured; a fused double quote cannot be excluded. The closing pair remains double.',
       '18_p102_opener', b, [545,462,676,530])

change('p107-cancelled-supralinear', 'p.107 line -3, cancelled mark above a in Kan',
       r'K\deleted{\unsure{h}}an',
       r'K\raisebox{1.1ex}[0pt][0pt]{\makebox[0pt][l]{\deleted{\unsure{h}}}}an',
       'insertion or placement', 'high',
       'The black cancelled cluster is visibly above a, not on the word baseline between K and a. The reading h remains doubtful because the repeated horizontal crossing strokes cover its interior. The raised zero-width placement preserves that position without asserting an insertion caret.',
       '14_kan_old_letter', b, [596,708,761,789])

change('p115-colon', 'p.115 final entry, punctuation after 115',
       r'p.115\unsure{:}', 'p.115:', 'misread symbol or index', 'medium',
       'Two separate marks occur between 115 and line: an upper short curved stroke and a lower point. They form a colon; the lower mark has no descending comma tail.',
       '17_p115_punctuation', b, [270,1085,640,1168])

top_anchors = r'''\tikz[remember picture,overlay]{
\coordinate (scxxivlefttop) at (-.8em,1ex);
\coordinate (scxxivrighttop) at (.94\linewidth,1ex);
}'''
bottom_anchors = r'''\par\noindent\tikz[remember picture,overlay]{
\coordinate (scxxivleftbottom) at (-.8em,-2ex);
\coordinate (scxxivrightbottom) at (.94\linewidth,-2ex);
}'''
reading = reading.replace(r'\scanpage{21}', r'\scanpage{21}'+'\n\n'+top_anchors, 1)
reading = reading.replace('% archive sheet number: 20', bottom_anchors+'\n\n% archive sheet number: 20', 1)
left_rule = r'\draw[overlay,thin] (scxxivlefttop) -- (scxxivleftbottom);'
right_rule = r'\draw[overlay,thin] (scxxivrighttop) -- (scxxivrightbottom);'
anchor = r'\draw[overlay,gray,thin] (scxxib) to[bend left=2] (scxxid);'
reading = reading.replace(anchor, anchor+'\n'+left_rule+'\n'+right_rule, 1)
change('left-vertical-rule', 'Left vertical rule from clipped opening through final entries',
       '', left_rule, 'drawing or diagram', 'high',
       'A thin continuous, slightly irregular vertical ruling stands just to the left of the reference column, from the upper clipped line to below the final entry. Its textual anchoring is supplied by scxxivlefttop and scxxivleftbottom in reading.tex.',
       None, whole, [233,88,260,2301], replace=False)
change('right-vertical-rule', 'Right vertical rule through both sections',
       '', right_rule, 'drawing or diagram', 'high',
       'A thin continuous vertical ruling stands near the right edge, crossing the marginal note and the horizontal separator and continuing to the lower border. Its textual anchoring is supplied by scxxivrighttop and scxxivrightbottom in reading.tex.',
       None, whole, [1509,85,1541,2333], replace=False)

doubts = []
def doubt(place, old, new, resolved, confidence, evidence, crop=None, source=None, bbox=None):
    doubts.append(dict(place=place, c=old, reading=new, resolved=resolved,
                       confidence=confidence, evidence=evidence,
                       crop=('crops/'+crop+'.jpg') if crop else None,
                       source=source, bbox=bbox))

doubt('Clipped first line, page indicator', r'\unsure{p.}', r'\unsure{p.}', False, 'low',
      'Only a long lower vertical survives; the bowl and any period lie in the missing band. The p. hypothesis is retained without filling its absent upper strokes.', '01_top_left', a, [242,61,842,135])
doubt('Clipped first line, page number', r'\unsure{77|11}', r'\unsure{77|11}', False, 'low',
      'Two slanting lower strokes survive; their upper parts are lost. Neither 77 nor 11 is decided by the extant ink.', '01_top_left', a, [242,61,842,135])
doubt('Clipped first line, first contraction', r"\unsure{isn't|is'nt}", r"\unsure{isn't|is'nt}", False, 'low',
      'The low i/s/n/t remnants do not retain the high apostrophe. Both placements remain possible independently of the later example.', '01_top_left', a, [242,61,842,135])
doubt('Clipped first line, comparison word', r'\unsure{not}', r'\unsure{not}', False, 'low',
      'Only a pale rounded base and a short following foot survive. They permit not but do not supply the complete letter tops.', '01_top_left', a, [242,61,842,135])
doubt('Clipped first line, second contraction', r"\unsure{is'nt|isn't}", r"\unsure{is'nt|isn't}", False, 'low',
      'The second occurrence also loses its apostrophe height; it is marked independently of the first occurrence.', '01_top_left', a, [242,61,842,135])
doubt('Clipped first line, erased words before the final remnant', r'\illegible{3}', r'\illegible{3}', False, 'low',
      'About three word positions occupy the pale erased band. Small isolated remnants do not support a complete lexical reading; no remembered wording has been supplied.', '02_top_right', a, [837,52,1475,140])
doubt('Clipped first line, remnant before form', r'\unsure{er}', r'\unsure{er}', False, 'low',
      'A small lower loop and an upturned ending permit er. The missing left and upper strokes do not support a complete word.', '02_top_right', a, [837,52,1475,140])
doubt('p.88 line 2, overwritten old article', r'\unsure{a|a l}', r'\unsure{a|a l}', False, 'low',
      'The older left loops are covered by the final article; a short extra upright cannot be assigned securely. Deletion/overwriting extent is clearer than its interior letters.', '03_article', a, [1207,243,1665,315])
doubt('p.88 line 2, live article', r'\unsure{a}', 'a', True, 'high',
      'The right small closed oval and outgoing stroke identify the live a before bit.', '03_article', a, [1207,243,1665,315])
doubt('p.89 line 8, opener before is', r'\unsure{``}', r'\unsure{``|`}', False, 'low',
      'The heavy connected mark does not cleanly separate its two projections; a single opener is retained as an explicit alternative.', '04_line8_opener', a, [540,370,1000,442])
doubt('p.89 line -15, cancelled reference', r'\unsure{p.}', 'p.', True, 'high',
      'A descending stem, right bowl and following separate point survive the crossing strokes.', None, a, [231,452,292,521])
doubt('p.90 margin, occurences/occurrences', r'\unsure{occurences|occurrences}', 'occurences', True, 'medium',
      'One r shoulder follows the small u group before the e loop. The spelling with one r is read from that group, not normalized.', '05_occurrences', a, [1305,550,1611,694])
doubt('p.90 cancelled not -- neither, initial parenthesis hypothesis', r'\unsure{(}', '', True, 'high',
      'The mark joins the deletion zigzag continuously and has its sharp turn; no independent opening parenthesis is visible.', '06_not_neither', a, [520,681,897,750])
doubt('p.90 line -9, old digit(s)', r'\unsure{4|14}', r'\unsure{4|14}', False, 'low',
      'Heavy crossing forms a rectangular cluster. A right upright and low cross stroke permit 4; the tall left upright may be either part of the cancellation or a preceding 1.', '07_old_digit', a, [1160,680,1320,754])
doubt('p.91 after English, period', r'\unsure{.}', '.', True, 'high',
      'The dark isolated point is distinct from the h downstroke.', '09_english_stop', a, [1052,1072,1321,1146])
doubt('p.91 cancelled example, final word', r'\unsure{or}', r'\unsure{or}', False, 'low',
      'An o-like loop survives to the left of a steep cancellation; the next letter is covered. or remains a hypothesis, not a recovery of the buried strokes.', '10_deleted_example', a, [573,1123,1053,1204])
doubt('p.91 line -16, cancelled p', r'\unsure{p}', r'\unsure{p}', False, 'low',
      'A long stem with a small right loop permits p, but the upper loop is merged with the cancellation strokes.', '11_deleted_p', b, [248,148,327,216])
doubt('p.99, cancelled ha', r'\unsure{ha}', 'ha', True, 'medium',
      'The tall loop and low shoulder of h and the separate a oval survive the strike. No unseen continuation is reconstructed.', '12_deleted_ha', b, [470,270,567,340])
doubt('p.107 line 14, cancelled character after saturation', r'\unsure{t}', r'\unsure{t}', False, 'low',
      'The narrow crossed vertical cluster may include t, but the old character cannot be detached from the repeated loops and crossing stroke. The following separate dash is clear.', '13_deleted_t', b, [859,648,950,724])
doubt('p.107 line -3, cancelled character above a in Kan', r'\unsure{h}', r'\unsure{h}', False, 'low',
      'The tiny cluster is struck repeatedly and no complete h contour is recoverable; h remains tentative. Its supralinear position is certain and is reproduced separately.', '14_kan_old_letter', b, [596,708,761,789])
doubt('p.107 line -3, rejected name', r'\unsure{Khan|Khân}', r'\unsure{Khan|Khân}', False, 'low',
      'K, the tall h and the last n are legible. The crowded a region has an extra high upright/crossed shape, so plain versus marked a cannot be settled.', '15_khan', b, [846,709,1033,789])
doubt('p.115 after page number, colon', r'\unsure{:}', ':', True, 'medium',
      'A separate upper mark over a lower point forms the colon. The lower mark lacks a comma tail.', '17_p115_punctuation', b, [270,1085,640,1168])
doubt('C_context spelling contrast, p.88 line 2', "``does'nt'' should be ``doesn't''", "``does'nt'' should be ``doesn't''", True, 'high',
      'The first apostrophe stands between s and n; the replacement apostrophe stands between n and t. The literal C text is confirmed, so this context decision is not a change.', None, a, [526,240,1119,303])
doubt('C_context spelling contrast, p.107 line 5', "``is'nt'' again replace by ``isn't''", "``is'nt'' again replace by ``isn't''", True, 'high',
      'The two apostrophe placements are independently visible in the lower half, with the first after s and the second after n.', None, b, [553,591,1120,660])
doubt('C_context spelling contrast, p.91 line -16', "``avatars'' not ``avators''", "``avatars'' not ``avators''", True, 'high',
      'The first word has a after t and the second has o after t. C already has the contrast in that order.', None, b, [556,150,1167,211])

remaining = []
for d in doubts:
    if not d['resolved']:
        remaining.append(dict(place=d['place'], reading=d['reading'], alternatives=d['reading'],
                              confidence=d['confidence'], reason=d['evidence']))
for id in ['top-dash','p88-period','p102-opener']:
    ch = next(x for x in changes if x['id']==id)
    remaining.append(dict(place=ch['place'],reading=ch['reading'],alternatives=ch['reading'],
                          confidence=ch['confidence'],reason=ch['evidence']))

inventory=[]
def inv(element, kind, position, words, hand='his hand'):
    inventory.append(dict(sheet_kind='list',hand=hand,element=element,kind=kind,
                          position=position,first_words_or_objects=words,transcribed='yes'))
inv('01','text','Clipped opening, first two written lines',r'\unsure{p.} \unsure{77|11} line 12; continuation later (i.e ...)')
inv('02','text','Upper block, p.87 line 8',r"p.87 line 8 ``we \uline{have} only got to''")
inv('02u','text','Nested underline in p.87 quoted phrase',r'\uline{have}')
inv('03','text','Upper block, p.88 line 2',"does'nt should be doesn't; occurs ... bit further down")
inv('03d','deletion','Nested overwritten article after occurs',r'\deleted{\unsure{a|a l}}')
inv('04','text','Upper block, p.89 line 3','to have got me; or alternatively to have made me')
inv('05','text','Upper block, line 8','is very necessary?')
inv('06','text','Upper block, line -15, two physical lines','last not least; last but not least; an alternative would be last, not least,')
inv('06d','deletion','Left reference of line -15',r'\deleted{p.}')
inv('07','text','Upper block, p.90 line -15','compare takes with as does commute')
inv('07m','margin note','Right of p.90 line -15, in two lines','(4 occurences on this page)')
inv('07r','drawing','Below and to the left of the parenthetical count','Curved left hook continuing as a long low horizontal rule')
inv('08','deletion','Upper block, full crossed line below p.90 line -15',r'\deleted{also this line -15 has a double negative}')
inv('09','text','Next line, live continuation after cancelled words',"``isn't line -...9 (twice)")
inv('09d','deletion','Left part of that line',r'\deleted{not -- neither}')
inv('09n','deletion','Nested old reference numeral before live 9',r'\deleted{\unsure{4|14}}')
inv('10','text','Upper block, line -8, continued onto short line words','replace comma by that - would give better flow of words')
inv('11','text','Upper block, p.91 line 1','in view of indicates a result of previous happenings')
inv('12','text','Next line in p.91 entry','with the view to indicates future hopes & expectations.')
inv('13','text','p.91 unnumbered line and parenthesized example over four lines',"we've got or we have got; We got; conditional if we ... always takes have")
inv('13d1','deletion','Nested after English.',r'\deleted{only}')
inv('13d2','deletion','Nested following like, before the live loaf-of-bread example',r"\deleted{``we got into the car'' \unsure{or}}")
inv('14','text','Upper block, line -16','avatars not avators')
inv('14d','deletion','Left reference of line -16',r'\deleted{\unsure{p}}')
inv('15','text','Upper block, p.92 quoted line -16','probably informal (repeated line -3)')
inv('16','text','Upper block, p.99',r'$X$ ... $Y$ have got changed to $F,G$ it seems.')
inv('16d','deletion','Between X and Y',r'\deleted{ha}')
inv('17','text','Upper block, p.100 line -16','having the same objects')
inv('17u','text','Nested underline in p.100',r'\uline{the}')
inv('18','margin note','Right, below p.100 and above separator','Sent 19/12/83')
inv('19','deletion','Long diagonal cancellation descending from p.88 toward p.99','First thin oblique cancellation line, reproduced in TikZ')
inv('20','deletion','Long diagonal cancellation descending from p.90 toward p.100','Second thin oblique cancellation line, reproduced in TikZ')
inv('21','drawing','Across sheet below p.100 and Sent date','Long slightly wavy horizontal separator')
inv('22','drawing','Left of reference column from top to bottom','Thin vertical rule','undetermined (rule)')
inv('23','drawing','Near right edge from top to bottom','Thin vertical rule','undetermined (rule)')
inv('24','text','Lower block, p.102 line -1','commute with again')
inv('24u','text','Nested underline in p.102',r'\uline{with}')
inv('25','text','Lower block, p.105 line 7','developing (single p.)')
inv('26','text','Lower block, p.107 line 5',"is'nt again replace by isn't also in line -5.")
inv('26i','insertion','Above the line between also and line -5, with caret',r'\inserted{in}')
inv('27','text','Lower block, line 14','saturation ... -')
inv('27d','deletion','Following saturation, before separate dash',r'\deleted{\unsure{t}}')
inv('28','text','Lower block, line -3','Kan not Khan/Khân')
inv('28d','deletion','Above the a in first Kan',r'\deleted{\unsure{h}} (raised in reading.tex)')
inv('29','text','Lower block, p109 line -9',"isn't")
inv('30','text','Lower block, p.111 line 19','relationships.')
inv('30u','text','Below medial s in relationships',r'\uuline{s}')
inv('31','text','Lower block, p.112 line 14',"we'll say we've got")
inv('32','text','Lower block, p.113 line 15','commute with repeat line -15')
inv('33','text','Lower block, line -14',"we've got or simply we have")
inv('34','text','Final entry, p.115 lines -5 & 6','commute with')
inv('35','margin note','Lower-left archive corner','20 (comment only)','another unnamed hand (archive pencil)')

notes = [
 'An English editorial correction list. The upper section has an extensively clipped/erased opening reference and then entries citing pp.87–100; two thin diagonal strokes cancel across that section. A horizontal rule separates the continuation citing pp.102–115.',
 'At p.89 line 3 the writer offers “or alternatively” before “to have made me”; line 8 asks whether “very” is necessary, and line -15 gives both the more usual “last but not least” and another possible formulation “last, not least,”.',
 'The right-hand note beside p.90 line -15 says “(4 occurences on this page)”, enclosed below/left by a curved rule. The next full sentence about a double negative and the words “not -- neither” are cancelled.',
 'The p.90 line -8 replacement is qualified by “would give better flow of words”. The p.91 note distinguishes previous happenings from future hopes and expectations, then discusses have got and a conditional example.',
 'The p.92 recommendation is qualified by “probably”, and the p.99 change of X and Y to F, G ends “it seems.” The p.105 note explicitly says “single p.” after developing.',
 '“Sent 19/12/83” is written at the right above the horizontal separator. There is no title, author manuscript pagination or stated page count; the page and line numerals in the list are references. The lower-left archive number is 20 and is reproduced only as a comment.',
 'The continuation includes the insertion in at p.107 line 5, a cancelled character after saturation, a supralinear cancelled character over a in Kan, and double underlining beneath the medial s of relationships.'
]

notation = [
 dict(sign='p., line, -',location='Reference column throughout; p109',reading='p.87 line 8; line -15; p109 line -9',evidence='Minus-like short strokes introduce negative line references. The p109 reference visibly has no stop after p; p.88 has a separate but pale doubtful point.'),
 dict(sign='Apostrophe positions',location='Clipped opening; p.88; p.107; p109',reading="does'nt / doesn't; is'nt / isn't",evidence='The uncut occurrences separately show the apostrophe before or after n. The clipped first-line occurrences are both independently marked doubtful.'),
 dict(sign='Quotation strokes',location='p.89 line 8; p.102 opening; p.105 opening',reading=r'\unsure{``|`}; \unsure{`|``}; ``',evidence='Crop 04 leaves a fused mark; crop 18 leaves a single upright with a spur; crop 19 has two descending legs joined across the top and confirms the double opener.'),
 dict(sign='Paired quotes around comma and that',location='p.90 line -8',reading="``,'' by ``that''",evidence='Crop 08 separates two small high legs at each opener/closer; the signs confirm literal C.'),
 dict(sign='Two terminal low marks',location='p.87 final quoted wording',reading="``we have only to..''",evidence='Crop 21 shows two separated low marks after to, the second drawn out horizontally; the final high pair is separate. C’s two terminal dots are retained.'),
 dict(sign='Ordinary capitals',location='p.99',reading='$X$, $Y$, $F, G$',evidence='The lower half has single ordinary capital contours, without double striking or indices.'),
 dict(sign='Underlining',location='p.87, p.100, p.102, p.111',reading=r'\uline{have}; \uline{the}; \uline{with}; relation\uuline{s}hips',evidence='The first three are single baseline rules confined to the named word. Crop 16 confirms two short separated strokes under the medial s.'),
 dict(sign='Rule/cancellation geometry',location='Margins and upper block',reading='Two vertical rules, two oblique cancellation lines, one horizontal separator; one curved marginal rule',evidence='Whole-page layout and half images independently expose the positions. All are rendered by actual TikZ draw commands.'),
 dict(sign='Inserted in',location='p.107 line 5',reading=r'also \inserted{in} line -5.',evidence='The word in sits above a small caret at the gap between also and line.'),
 dict(sign='Cancelled glyph above a',location='p.107 line -3, first quoted name',reading=r'K\raisebox{1.1ex}[0pt][0pt]{\makebox[0pt][l]{\deleted{\unsure{h}}}}an',evidence='Crop 14 places the cancelled cluster above the a; no independent insertion caret is discernible.')
]

report = dict(scan=21,reader='C',model='GPT-6 Astra Pro',effort='not exposed',
 viewed=[whole,a,b],
 layout='One handwritten list sheet, with its topmost written line clipped/erased. A long upper section and shorter lower continuation are divided by a horizontal rule. The upper section is crossed by two long light diagonal cancellation strokes. Two long vertical rules flank the writing; a right marginal parenthetical count has a curved under-rule, and a Sent date stands above the horizontal separator. Small local cancellations, an interlinear in with caret, four underlined spans and the archive pencil corner number are inventoried separately. No mathematical display or commutative diagram is present.',
 changes=changes,c_doubts=doubts,remaining_doubts=remaining,inventory=inventory,notes=notes,
 math_checks=[],notation=notation,
 abbreviations=[
  dict(form='p.',expansion='page (reference abbreviation)',place='Most reference entries'),
  dict(form='p',expansion='page (reference indicator without point)',place='p109; clipped/cancelled references remain uncertain where marked'),
  dict(form='i.e',expansion='that is (tentative expansion only)',place='Opening continuation'),
  dict(form='p.',expansion='letter p, as stated by single p.',place='p.105 parenthesis')],
 brief_feedback='Read brief_v06, conventions, PREAMBLE, metadata, C.tex, H.tex, C_context.md and notation.md. Received and read C_context_addendum.md during crop review; it introduced no need to repeat an image or a settled crop. H is description-only, so no H collation rows are manufactured. The whole and each half were displayed exactly once; 21 enhanced tight crops were each displayed once. One mistyped crop command had an invalid coordinate order and produced no file or image; the corrected command produced crop 20. The clipped opening and buried cancellation letters remain explicitly doubtful. All differences were checked against literal C strings, and the final unified diff is saved. Inventory covers all text entries, nested deletions/insertion/underlines, six line drawings (including two oblique cancellations), the marginal count and Sent date, and the archive comment. No substantive mathematical check was performed on this editorial list; math_checks is intentionally empty.')

out.mkdir(parents=True,exist_ok=True)
(out/'reading.tex').write_text(reading)
(out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
with (out/'inventory.tsv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=list(inventory[0]),delimiter='\t')
    writer.writeheader();writer.writerows(inventory)
(out/'notes.md').write_text('# Reader C — scan 021\n\n'+'\n\n'.join(notes)+'\n')
diff=''.join(difflib.unified_diff(c_text.splitlines(True),reading.splitlines(True),fromfile='C.tex',tofile='reading.tex'))
(out/'literal_C_diff.patch').write_text(diff)
crop_rows=[json.loads(x) for x in (out/'crops/crops.jsonl').read_text().splitlines()]
crop_rows.sort(key=lambda x:Path(x['output']).name)
view_log=[dict(sequence=1,path=whole,view='whole layout',displayed=True),
          dict(sequence=2,path=a,view='full-resolution half a',displayed=True),
          dict(sequence=3,path=b,view='full-resolution half b',displayed=True)]
for i,row in enumerate(crop_rows,4):
    path=Path(row['output'])
    if not path.is_absolute():path=root/path
    view_log.append(dict(sequence=i,path=str(path),view='single enhanced tight crop',displayed=True,
                         source=row['source'],bbox=row['box'],reason=row['reason']))
(out/'view_log.json').write_text(json.dumps(dict(views=view_log,failed_crop_attempt=dict(output='crops/20_p88_reference.jpg',box=[244,367,367,316],reason='Mistyped y coordinate; source crop failed before saving or displaying.',produced_image=False),addendum_received='work/inputs/021/C_context_addendum.md'),ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(changes=len(changes),c_doubts=len(doubts),remaining_doubts=len(remaining),inventory=len(inventory),crops=len(crop_rows)),indent=2))
