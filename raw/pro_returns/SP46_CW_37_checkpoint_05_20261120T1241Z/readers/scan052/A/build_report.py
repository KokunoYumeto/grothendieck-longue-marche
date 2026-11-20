import json
from pathlib import Path
root=Path('/workspace/scratch/006c0e32b2af')
out=root/'out/readers/scan052/A'
c=(root/'packets/scan052/C.tex').read_text()
r=(out/'reading.tex').read_text()
crops=json.loads((out/'crop_manifest.json').read_text())
byname={Path(x['file']).stem:x for x in crops}
decisions=[]
def add(id,place,c_reading,h_reading,reading,diff_c,diff_h,c_doubt,unresolved,alternatives,confidence,kind,scan_shows,bbox,crop=''):
    decisions.append(dict(id=id,place=place,c_reading=c_reading,h_reading=h_reading,reading=reading,diff_c=diff_c,diff_h=diff_h,c_doubt=c_doubt,unresolved=unresolved,alternatives=alternatives,confidence=confidence,kind=kind,scan_shows=scan_shows,crop=(byname[crop]['file'] if crop else ''),bbox=bbox))
add('A052-01','First entry, abbreviation before de Lefschetz','th','th.','th',False,True,False,False,[],'high','text not on the page','The t and h are followed by a gap before de; no separate abbreviation point is present.',[491,42,560,101])
add('A052-02','First entry, supposer','supposer',r'\uncertain{supposer}','supposer',False,True,False,False,[],'high','other','The long descending p strokes and the joined o-s-e-r ending are visible in the right half; H uncertainty is not retained.',[1203,41,1422,111])
add('A052-03','First entry, connector between X and Y','ni','et','ni',False,True,False,False,[],'high','misread word','After X the ink has a short n-shaped arch followed by an i stroke, not the loop and cross-stroke of et.',[1497,45,1579,91])
add('A052-04','Second entry, exposé numeral',r'\unsure{\mathrm{V}|\mathrm{VI}}',r'\emph{V}\uncertain{I}',r'\unsure{\mathrm{V}|\mathrm{VI}}',False,False,True,True,['V','VI'],'medium','misread symbol or index','A V-shaped pair of converging strokes is strong; a further lighter upright/right limb remains distinguishable but cannot securely be assigned to an independent I rather than retracing. Upper and lower rules are present.',[372,217,454,303],'c01_second_numeral')
add('A052-05','Second entry, first faisceau ending','faisceau','faisceaux','faisceau',False,True,False,False,[],'high','misread word','After the a and u, the terminal stroke bends slightly down and stops. There is no independent crossed x before the colon.',[530,211,859,326],'c02_q_faisceau')
add('A052-06','Second entry, word immediately after colon',r'\unsure{rajouter}','signaler',r'\unsure{signaler|rajouter}',True,True,True,True,['signaler','rajouter'],'medium','misread word','The beginning has a small isolated upright/curved group, a detached dot, and a loop with a long leftward descender; the later tall ascender has no decisive crossbar. This favours signaler, but the reduced joins still permit rajouter.',[885,221,1075,313],'c03_rajouter')
add('A052-07','Second entry, raisonnable',r'\unsure{raisonnable}','raisonnable','raisonnable',True,False,True,False,[],'high','other','The initial r-a-i-s, a looped o, the two low n groups, an a loop, and the two tall b/l strokes with the final tail can be followed in the crop.',[1350,221,1605,294],'c04_raisonnable')
add('A052-08','Third entry, cancelled exposé numeral',r'\deleted{\overline{\underline{\unsure{\mathrm{IV}|\mathrm{V}|\mathrm{VI}}}}}',r'\struck{\ill{}}',r'\deleted{\overline{\underline{\unsure{\mathrm{IV}|\mathrm{V}|\mathrm{VI}}}}}',False,True,True,True,['IV','V','VI'],'low',r'readable ink left as \ill{}','Upper and lower horizontal rules and portions of upright and converging strokes survive several heavy diagonal cancellation strokes. IV is the best partial reading, but the cancellation prevents deciding it over V or VI.',[399,386,486,467],'c05_cancelled_numeral')
c_start=c.index(r'\(\deleted',c.index(r'\noindent SGA 5.'))
c_end=c.index(r'\quad Reprendre',c_start)
r_start=r.index(r'\tikz[baseline=(cancel.base)]')
r_end=r.index(r'\quad Reprendre',r_start)
add('A052-09','Third entry, replacement VI and enclosing stroke',c[c_start:c_end],None,r[r_start:r_end],True,False,False,False,[],'high','insertion or placement','The replacement VI is physically below the blackened numeral. A single U-like stroke descends beside its left edge, passes below it, and rises farther on the right toward the old numeral. The reading stacks the replacement below the cancellation. H gives only a prose description of this placement.',[391,421,521,560],'c05_cancelled_numeral')
add('A052-10','Third entry, ending of Z-ell-faisceaux',r'\unsure{faisceaux|faisceau}','faisceaux','faisceaux',True,False,True,False,[],'high','misread word','The right half shows a short rising then crossing terminal stroke after the u, before the page margin; the x is present.',[1435,389,1668,476])
add('A052-11','Third entry, connector before Q-ell-faisceaux','ou','et','ou',False,True,False,False,[],'high','misread word','The first character is a closed low oval, followed by a shallow u-shaped join; no t ascender or crossbar occurs in this word.',[547,489,599,525])
add('A052-12','Third entry, small mark above ou',r'\inserted{\unsure{+|*}}','',r'\inserted{\unsure{*|+}}',True,True,True,True,['*','+'],'medium','omission','The raised mark has crossing diagonals and a faint further lateral arm. An asterisk is favoured over a plus, but the short faint arms do not fully settle the glyph.',[557,470,587,497],'c06_cross_above_ou')
add('A052-13','Third entry, mark after opening parenthesis',r'\unsure{,|.}','','comma: ,',True,True,True,False,[],'high','omission','A separate dark head with a narrow downward taper lies between the opening parenthesis and the capital A. It is comma-shaped, rather than a round full stop.',[584,627,607,657],'c07_mark_after_parenthesis')
add('A052-14','Third entry, N with raised underlined o',r'N\textsuperscript{\uline{o}}','N°',r'N\textsuperscript{\uline{o}}',False,True,False,False,[],'high','omission','The o is raised and has a short separate horizontal line below it; it is not only a degree-circle form.',[1058,589,1129,647])
add('A052-15','Fourth entry, abbreviation before les constructions','ttes','toutes','ttes',False,True,False,False,[],'high','abbreviation expanded or spelling modernised','Two tall t strokes lead directly into a compressed e-s ending; there is no intervening ou sequence.',[755,790,873,850])
add('A052-16','Projective-systems entry, first word',r'\unsure{Systèmes|Système}','Systèmes',r'\unsure{Systèmes|Système}',False,True,True,True,['Systèmes','Système'],'medium','misread word','S-y-s-t and the grave-accent stroke can be followed. The last joined e/s portion is a low extended line with a small downward end, insufficient to decide singular or plural from the ink alone.',[616,895,806,980],'c08_systemes')
add('A052-17','Projective-systems entry, inserted word',r'\unsure{adiques}',r'\add{-adiques}','adiques',True,True,True,False,[],'high','misread word','The first small shape is a closed a loop, followed by the looped d, an i trace, the round q with descender, and the u-e-s continuation. No separate leading hyphen precedes the a.',[1019,864,1175,913],'c09_adiques_connector')
add('A052-18','Projective-systems entry, stroke before dans','dans','(dans','dans',False,True,False,False,[],'high','drawing or diagram','The apparent opening parenthesis continues as one unbroken long stroke beneath the inserted adiques and turns upward at the far right; it is the insertion connector, not a parenthesis before dans.',[997,872,1226,955],'c09_adiques_connector')
add('A052-19','Projective-systems entry, dérivées',r'\unsure{dérivées}','dérivées',r'\unsure{dérivées}',False,True,True,True,['dérivées'],'medium','other','The initial looped d and final looped s are visible, but the middle pale strokes and accent marks remain compressed and partly merged with the graph-paper ruling. The tentative word is retained.',[1382,890,1601,969],'c10_derivees')
add('A052-20','Below the parenthetical placement note, left faint mark','','',r'\unsure{\tikz{\draw[gray,thin] (0,0)--(.08,.04)--(.14,-.01)..controls(.17,.06)and(.17,.14)..(.24,.20);}}',True,True,False,True,['small pencil tick or zigzag','incidental pencil mark'],'low','drawing or diagram','A short low left stroke rises slightly, bends down, then turns into a longer rising right stroke. It has no secure letter or word reading and is reproduced as a faint mark.',[692,1056,730,1085],'c22_faint_left_tick')
add('A052-21','Below the parenthetical placement note, central faint mark','','',r'\unsure{\tikz{\draw[gray,thin] (0,0)--(.05,.08)--(.10,.02)--(.12,.17);\draw[gray,thin](.10,.02)--(.18,-.03);\draw[gray,thin](.08,-.10)--(.14,-.07);}}',True,True,False,True,['small angular pencil/surface mark','incidental smudge'],'low','drawing or diagram','A very pale angular cluster has an upright segment, two oblique lower branches, and short separate traces below. It does not support a verbal reading; the reading preserves an uncertain graphic approximation.',[844,1083,874,1110],'c23_faint_central_mark')
add('A052-22','Right of the space below (ou dans thèse)',r'\margin{\unsure{:}}','',r'\margin{\unsure{\tikz[baseline=-.3ex]{\fill (0,0) circle[radius=.35pt];\fill (.07,.10) circle[radius=.35pt];}}}',True,True,True,True,['colon-like pair of oblique dots','incidental dot pair'],'low','drawing or diagram','Two separate dark round marks run from lower left to upper right. Their oblique separation is certain; whether they constitute authorial punctuation is not. They are retained graphically.',[1511,1078,1547,1114],'c11_margin_dots')
add('A052-23','Sixth entry, word after introduction du','livre','Hom',r'\unsure{livre|Hom}',True,True,False,True,['livre','Hom'],'medium','misread word','The crop shows one tall initial downstroke with a long low return, a faint second upright, a rounded middle bend, and a reduced final wave. These favour livre but do not securely separate every letter from the H-o-m possibility.',[1181,1133,1312,1204],'c12_livre')
add('A052-24','Sixth entry, end of exposé',"l'exposé",r"l'expo\supplied{sé}",r"l'expo\unsure{sé}",True,True,False,True,['sé'],'medium','other','The right edge contains a rounded upright continuation after expo, a low final stroke, and a long rising accent-like stroke. The ending has ink and is not silently supplied, but its reduced s/e joins remain uncertain.',[1514,1127,1715,1211],'c13_expose')
add('A052-25','Sixth entry, punctuation after exposé','',',','',False,True,False,False,[],'high','text not on the page','No detached low comma follows the terminal word strokes at the right edge before the next line starts with signaler.',[1674,1184,1710,1210],'c13_expose')
add('A052-26','Sixth entry, object of signaler',"l'ennui","l'emploi","l'ennui",False,True,False,False,[],'high','misread word','After the l/apostrophe there is a run of low arches ending in a short i with a detached dot. No p descender occurs in the word.',[797,1200,1009,1265])
add('A052-27','Sixth entry, trop','trop',r'\uncertain{trop}','trop',False,True,False,False,[],'high','other','The t ascender, short r, round o, and descending p are distinct in the right half; the word can be read without H doubt.',[1364,1204,1477,1276])
add('A052-28','Sixth entry, raised coefficient exponent',r'\unsure{n|\nu}','n',r'\nu',True,True,True,False,[],'high','misread symbol or index','The raised glyph descends from its upper-left start to a lower bend and then rises on the right. It has the v-shaped stroke order of nu, not the arch of n. The separate slash and looped ell are also visible.',[1216,1274,1254,1310],'c14_coefficient')
add('A052-29','Sixth entry, marks before closing coefficient parenthesis',r'\unsure{-\,-|\ldots}',r'\ldots',r'-\,-',True,True,True,False,[],'high','misread symbol or index','The right half shows two separated short horizontal marks after the final Z and before the closing parenthesis; a third point is not present.',[1312,1304,1399,1331])
add('A052-30','Last prose entry, separator after i',r'\unsure{{:}|{<}|{\in}}',':',r'\unsure{{:}|{<}|{\in}}',False,True,True,True,[':', '<', r'\in'],'medium','misread symbol or index','Two heavy angular lobes are separated vertically, with a much lighter trace near their left edges. Their small scale prevents deciding a colon against an angular or membership-like joined mark; the arrow is separately right-pointing.',[777,1438,798,1473],'c15_i_generic_arrow')
add('A052-31','Last prose entry, generic-point glyph after separator',r'\unsure{\eta|y}','y',r'\unsure{\eta|y}',False,True,True,True,[r'\eta','y'],'medium','misread symbol or index','A short left upright joins a rounded shoulder and a long right descender curving left below the line. Eta is favoured, but the loop form also admits y; the recurring ambiguity is marked here.',[799,1439,832,1494],'c15_i_generic_arrow')
add('A052-32','Last prose entry, point abbreviation',r'\mathrm{pt}','pt',r'p\textsuperscript{t}',True,True,False,False,[],'high','misread symbol or index','The small t with its crossing stroke sits substantially above the baseline of the p and to its upper right. The raised placement is preserved.',[1257,1416,1323,1491],'c20_pt_abbreviation')
add('A052-33','Last prose entry, comma after générique','générique, et','générique et','générique, et',False,True,False,False,[],'high','omission','A short detached low oblique stroke appears after the final e of générique, at the end of the first line; it is kept as the comma.',[1503,1459,1547,1486])
add('A052-34','Last prose entry, subscript on F',r'F_{\eta}','F_y',r'F_{\eta}',False,True,False,True,[r'\eta','y'],'medium','misread symbol or index','The lowered glyph has a short left arm, a rounded rise, and a long right descender sweeping left. It repeats the eta/y ambiguity first marked after i; the F itself has a single stem and two bars.',[601,1478,656,1543],'c16_text_F_generic')
add('A052-35','Last prose entry, libre','libre','libre',r'\unsure{libre}',True,True,False,True,['libre'],'medium','other','After the clear loc. the word has a tall looped l and a second tall b-like stroke, but the intervening i and final r/e run are reduced. Libre is retained with a local doubt.',[928,1478,1024,1514],'c21_loc_libre')
add('A052-36','Last prose entry, isolated glyph after sur',r'\eta','y',r'\eta',False,True,False,True,[r'\eta','y'],'medium','misread symbol or index','The isolated glyph repeats the short left arm and curved descending right stroke seen in the first occurrence. It is rendered eta under the first-occurrence ambiguity convention, without asserting a new resolution.',[1118,1485,1167,1532],'c17_isolated_generic')
add('A052-37','Last prose entry, punctuation after isolated generic-point glyph','',',','',False,True,False,False,[],'high','text not on the page','There is no separate comma to the right of the isolated glyph. Its long low leftward tail belongs to the glyph itself.',[1147,1493,1189,1532],'c17_isolated_generic')
add('A052-38','Display, first F subscript',r'F_{\eta}','F_y',r'F_{\eta}',False,True,False,True,[r'\eta','y'],'medium','misread symbol or index','This lowered form has a particularly visible rounded arch and long hooked right descender. It supports eta while the page-wide eta/y identity remains conservatively marked at the first occurrence.',[801,1530,897,1600],'c18_display_left_generic')
add('A052-39','Display, second F subscript',r'F_{\eta}','F_y',r'F_{\eta}',False,True,False,True,[r'\eta','y'],'medium','misread symbol or index','A short left upright and rounded shoulder lead into the long left-turning right descender; this is the same recurring eta/y form, rendered with the first candidate.',[1112,1534,1178,1601],'c19_display_right_generic')

inventory=[]
def item(element,kind,position,first,hand='unnamed hand'):
    inventory.append(dict(sheet_kind='text',hand=hand,element=element,kind=kind,position=position,first_words_or_objects=first,transcribed='yes'))
item('First SGA 5 entry','text block','top, two manuscript lines','SGA 5 VII; th de Lefschetz faible')
item('Rules bracketing first numeral','drawing','top left beside SGA 5','upper and lower rules around VII')
item('Second SGA 5 entry','text block','upper quarter, two manuscript lines','SGA 5 V/VI; Q-ell-faisceau')
item('Rules and retracing of second numeral','drawing','upper left at second heading','V/VI between dark horizontal rules')
item('Underlines in second entry','drawing','end of the second entry','separate lines under champ and associé')
item('Third SGA 5 entry','text block','upper middle, four manuscript lines','SGA 5.; Reprendre en langage')
item('Cancelled numeral','deletion','after SGA 5. in third heading','IV/V/VI with diagonal cancellation and upper/lower rules')
item('Replacement numeral','insertion','below cancelled numeral','VI between upper and lower rules')
item('Stroke around replacement','drawing','around and below replacement VI','asymmetric U-like enclosing stroke')
item('Raised cross-like sign','insertion','above ou before Q-ell-faisceaux','asterisk/plus-like mark')
item('Number abbreviation decoration','drawing','end of parenthesis in third entry','short underline beneath raised o of N')
item('Fourth SGA 5 entry','text block','middle above first divider','SGA 5 IV; Essayer de faire')
item('Rules bracketing fourth numeral','drawing','left of fourth entry','upper and lower rules around IV')
item('First horizontal divider','drawing','across page below constructions essentielles','long slightly curved horizontal line')
item('Projective-systems entry','text block','middle below first divider','VI; Systèmes projectifs')
item('Rules bracketing projective-systems numeral','drawing','left of projective-systems entry','upper and lower rules around VI')
item('Adiques addition','insertion','above line after projectifs','adiques')
item('Adiques connecting stroke','drawing','below adiques, turning down before dans','long connector with a right upturn')
item('Alternative-placement parenthesis','text block','below projective-systems line','(ou dans thèse)')
item('Faint left tick','drawing','below the parenthesis, left of centre','small uncertain pencil zigzag')
item('Faint central cluster','drawing','below the parenthesis, near centre','small uncertain angular mark and short traces')
item('Oblique dot pair','margin note','right of blank space below the parenthesis','two dots, colon-like')
item('Coefficient entry','text block','lower middle, three manuscript lines','SGA 5 V; dans introduction du livre/Hom')
item('Second horizontal divider','drawing','below coefficient parenthesis','long slightly wavy horizontal line')
item('Final I § 5 entry','text block','bottom, two manuscript lines above display','I § 5; Donner, si i ...')
item('Duality formula','display','bottom centre','D(i_*(F_eta)) = i_*(D(F_eta))')
item('Archive number','archive pagination comment','bottom left corner','51')

report={
 'scan':52,
 'reader':'A',
 'image_views':[
 str(root/'source/SP46_CW_37_scans/H37-01_37_scan052.jpg'),
 str(root/'source/SP46_CW_37_scans/H37-01_37_scan052_a.jpg'),
 str(root/'source/SP46_CW_37_scans/H37-01_37_scan052_b.jpg')],
 'reading_path':str(out/'reading.tex'),
 'crops':crops,
 'decisions':decisions,
 'inventory':inventory,
 'notes':('One wholly handwritten graph-paper sheet containing seven entries: weak Lefschetz without assuming X or Y smooth; a Q-ell sheaf definition in terms of champ associé; restating SGA 4 notions in Z-ell/Q-ell sheaf language; constructions in the relatively smooth case; adic projective systems in derived categories with the separate alternative-placement note (ou dans thèse); concern about overly particular coefficients; and a requested duality formula for the inclusion of the generic point. The page is a list of tasks or proposals, not a written proof of those claims. Explicit authorial openness is expressed by Essayer de faire and by (ou dans thèse); the cancelled exposé number and inserted adiques are also retained. There is no separate overall title, no date, and no authorial manuscript page number identified on this sheet. The visible 51 at bottom left is treated only as the archive number, consistent with the packet; the scan identifier is 52 and the cote marker is 37. Body handwriting attribution is left unnamed because the assigned packet does not independently establish authorship. Two horizontal rules, the numeral rules, the VI enclosing stroke, the adiques connector, two faint isolated marks, and the oblique right-hand dot pair are included. Every requested source image was viewed once in whole/a/b order; every listed crop was viewed once. Macro-only witness differences and H editorial prose describing the paper were not counted as transcription disagreements. No mathematical proof, computation, or external-background check was performed.'),
 'math_reading_decisions':[
  'The extra strokes in Q and Z support blackboard/double-stroke capitals; the lowered loop is ell, and D and F remain ordinary single-stem capitals.',
  'The coefficient exponent has a descending left branch and an ascending right branch; it is read as nu, without replacing it by an expected n.',
  'Two short horizontal marks after the final coefficient Z are kept as two dashes rather than normalized to an ellipsis.',
  'The separator after i remains colon/less-than/membership ambiguous; the inclusion wording was not used to force a colon.',
  'The generic-point glyph is retained as eta/y at its first occurrence. The four repetitions are rendered eta under the supplied recurring-glyph convention; each has its own crop and decision.',
  'The final formula retains both inner pairs of parentheses, equality, and the two lower star subscripts on i exactly as visible.',
  'The point abbreviation has a raised t and is transcribed as p with superscript t, not as a mathematical exponent to be interpreted.',
  'The long stroke before dans belongs to the adiques insertion connector; no extra opening parenthesis is introduced there.'
 ],
 'check_events':[],
 'notation':[
  dict(sign='Q with additional stroke and lowered loop',latex=r'\mathbb{Q}_{\ell}',evidence='The circular capital has a second left stroke/loop and a separate lower looped ell.',place='Second and third entries'),
  dict(sign='Z with additional diagonal',latex=r'\mathbb{Z}',evidence='Two diagonal strokes are visible in each coefficient capital.',place='Third entry and coefficient parenthesis'),
  dict(sign='Raised v-shaped coefficient letter',latex=r'\nu',evidence='The stroke falls to a low bend then rises at the right; it is not an n arch.',place='Coefficient parenthesis, over ell'),
  dict(sign='Generic-point letter, recurring ambiguity',latex=r'\unsure{\eta|y}',evidence='Short left arm and rounded shoulder with a long right descender turning left. All five instances were inspected; only the first is marked in the text.',place='After i, on prose F, after sur, and on both display F letters'),
  dict(sign='Separator after i',latex=r'\unsure{{:}|{<}|{\in}}',evidence='Two dark angular lobes with an inconclusive pale left trace.',place='Final prose entry'),
  dict(sign='Lower many-pointed mark on i',latex=r'i_{*}',evidence='Both star-shaped marks sit below and to the right of the dotted i stems.',place='Final display'),
  dict(sign='Exposé numeral rules',latex=r'\overline{\underline{\mathrm{VII}}}',evidence='Separate straight upper and lower strokes bracket the early exposé numerals; the later V is unbarred.',place='First through fifth entries as individually transcribed'),
  dict(sign='Raised crossing above ou',latex=r'\unsure{*|+}',evidence='Crossing strokes plus a possible faint lateral arm.',place='Third entry')
 ],
 'abbreviations':[
  dict(form='SGA',expansion='Séminaire de Géométrie Algébrique'),
  dict(form='th',expansion='théorème'),
  dict(form=r'N\textsuperscript{\uline{o}}',expansion='numéro'),
  dict(form='ttes',expansion='toutes'),
  dict(form='coeff.',expansion='coefficients'),
  dict(form=r'p\textsuperscript{t}',expansion='point'),
  dict(form='loc.',expansion='localement'),
  dict(form='§',expansion='paragraphe')
 ],
 'slips':['The comma-shaped stroke immediately after the opening parenthesis in (, Ajouter nouveau N...) is preserved as written; its unusual punctuation is not corrected.'],
 'completion':'Complete independent diplomatic reading of scan 052: all seven text entries, the display, visible deletions and insertions, underlining/rules, connecting strokes, faint isolated marks, marginal dots, and archive-number comment are covered. All fifteen C doubt locations (including the recurring-glyph entry) have explicit decisions; all observed substantive C/H disagreements and new uncertainties have whole-image bboxes. The three supplied source images and twenty-three unique one-per-open-place crops were each viewed once. No other reader, page, OCR, published text, or external source was consulted.'
}
(out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print('Saved report:',len(decisions),'decisions,',len(inventory),'inventory rows,',len(crops),'crops.')
