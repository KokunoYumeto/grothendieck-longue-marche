from pathlib import Path
import json

base=Path('/workspace/scratch/006c0e32b2af')
out=base/'out/readers/scan070/B'
packet=base/'packets/scan070'
source=base/'source/SP46_CW_37_scans/B37-04_37_scan070.jpg'
reading=(packet/'C.tex').read_text()
replacements=[
 (r'\mspage{\handwritten{5}}',r'\mspage{\handwritten{- 5 -}}'),
 (r'trait\handwritten{(7.15)}.',r'trait\handwritten{(7\unsure{-|.}15)\unsure{.}}'),
 (r'\handwritten{p.13, li.10 du bas : (IV 2.12) au lieu de (III 2.12).}',r'\handwritten{p.13, li.10 du bas : ($\overline{\underline{\mathrm{IV}}}$ 2.12) au lieu de ($\overline{\underline{\mathrm{III}}}$ 2.12).}'),
 (r"``on trouve''\unsure{:|.}",r"``on trouve\unsure{.}''\unsure{:|.}"),
 (r'_{\handwritten{\chi}}',r'_{\chi}')
]
for old,new in replacements:
 if old not in reading:
  raise ValueError('Missing replacement target '+old)
 reading=reading.replace(old,new)
(out/'reading.tex').write_text(reading)
manifest=json.loads((out/'crop_manifest.json').read_text())
for c in manifest['crops']:
 c['view_count']=1
manifest['image_views']=[str(source),str(source.with_name(source.stem+'_a.jpg')),str(source.with_name(source.stem+'_b.jpg'))]
manifest['source_view_counts']={p:1 for p in manifest['image_views']}
manifest['half_geometry']={'a_bbox':[0,0,1686,1158],'b_bbox':[0,998,1686,2157],'overlap_y':[998,1158]}
manifest['open_places_before_cropping']=[
 'Handwritten (7.15): separator, possible underprint and final-point state.',
 'First lowered point index: o versus 0.',
 'Second lowered point index: l versus 1.',
 'Punctuation adjoining the closing quotation after on trouve.',
 'Alphabet and writing state of the lowered class subscript in (i).',
 'Alphabet and writing state of the two lowered class subscripts in (ii).'
]
(out/'crop_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
cs={n['file'].split('/')[-1]:n['file'] for n in manifest['crops']}
def decision(id,place,c,reading,bbox,**kw):
 d={'id':id,'place':place,'c_reading':c,'h_reading':None,'reading':reading,'diff_c':False,'diff_h':False,'c_doubt':False,'unresolved':False,'alternatives':[],'confidence':'high','kind':'other','scan_shows':'','crop':'','bbox':bbox}
 d.update(kw)
 return d
D=[]
D.append(decision('B070-01','Manuscript page number, top centre',r'\mspage{\handwritten{5}}',r'\mspage{\handwritten{- 5 -}}',[842,45,953,91],diff_c=True,kind='omission',scan_shows='A handwritten 5 is flanked by two separate short, nearly horizontal strokes, one to the lower left and one to the lower right. Both flanking strokes are visible in the prescribed source views.'))
D.append(decision('B070-02','p.11, li.9 du bas: end of the question','je me canule','je me canule',[715,625,943,660],scan_shows='The typed sequence has c, a, a single n with one arch, u, l, e. There is no second n and no cancellation. This is an unmarked C-context inspection target, not an explicit unsure/illegible place in C.',kind='other'))
D.append(decision('B070-03','p.12,li.6: separator in the handwritten reference after trait',r'\handwritten{(7.15)}',r'\handwritten{(7\unsure{-|.}15)}',[1536,764,1558,786],diff_c=True,unresolved=True,alternatives=['-','.'],confidence='medium',kind='misread symbol or index',scan_shows='Between the crossed handwritten 7 and the upright 1 there is a short, low, horizontally elongated stroke. Its width exceeds its height; a dash is the preferred literal reading, but an elongated handwritten point remains possible. It is not normalized from the apparent reference function.',crop=cs['B070_01_added_reference.jpg']))
D.append(decision('B070-04','p.12,li.6: final point following handwritten reference',r'.',r'\handwritten{\unsure{.}}',[1612,764,1633,790],diff_c=True,unresolved=True,alternatives=[r'\handwritten{.}',r'.'],confidence='medium',kind='other',scan_shows='The final low mark is a compact tapering triangular point, with an irregular hand-like outline. Its position after the pen-written parenthesis and its outline favour a handwritten full stop, but its writing operation is not established from shape alone. The doubt concerns handwritten versus typed state, not the presence of the point. No separate recoverable underprint is asserted beneath the opening parenthesis.',crop=cs['B070_01_added_reference.jpg']))
D.append(decision('B070-05','Handwritten p.13, li.10 du bas: first Roman numeral',r'IV',r'\overline{\underline{\mathrm{IV}}}',[744,1053,789,1088],diff_c=True,kind='omission',scan_shows='The I upright and the two legs of V lie between a separate upper horizontal stroke and a lower horizontal stroke; the rules extend across the numeral. The lower-half overlap settled these strokes without a crop.'))
D.append(decision('B070-06','Handwritten p.13, li.10 du bas: second Roman numeral',r'III',r'\overline{\underline{\mathrm{III}}}',[1113,1055,1155,1090],diff_c=True,kind='omission',scan_shows='Three short upright strokes are bounded by an upper and a lower horizontal rule. The horizontal strokes span the three uprights and are retained independently of the numeral value.'))
D.append(decision('B070-07','p.13, li.3 du bas: first x index',r'x_{\unsure{o|0}s}',r'x_{\unsure{o|0}s}',[807,1158,867,1207],c_doubt=True,unresolved=True,alternatives=['o','0'],confidence='medium',kind='misread symbol or index',scan_shows='The lowered first glyph is a closed oval, approximately the body height of the neighbouring s. It has no slash or other distinguishing internal stroke. The oval favours the literal o-shaped impression but does not securely establish alphabetic versus numeric identity; the original alternatives are retained.',crop=cs['B070_02_first_x_index.jpg']))
D.append(decision('B070-08','p.13, li.3 du bas: second x index',r'x_{\unsure{l|1}s}',r'x_{\unsure{l|1}s}',[933,1158,994,1207],c_doubt=True,unresolved=True,alternatives=['l','1'],confidence='medium',kind='misread symbol or index',scan_shows='The lowered first glyph has a tall upright, a short left-projecting top cap with a rounded corner, and a broad horizontal foot. No separately decisive diagonal lead-in distinguishes 1 from the l-shaped type impression. The following lowered s is clear.',crop=cs['B070_03_second_x_index.jpg']))
D.append(decision('B070-09','Handwritten p.16, li.8 du bas: low mark at the closing quotation after trouve',r"``on trouve''",r"``on trouve\unsure{.}''",[867,1651,886,1683],diff_c=True,unresolved=True,alternatives=['a separate full stop before the closing quotation','part of the closing-quotation/separator cluster'],confidence='medium',kind='omission',scan_shows='A dark short horizontal point lies below and slightly left of the two elevated closing-quotation strokes. It is distinct from the farther-right low point used by the possible separator. Its assignment as a separate full stop before the closing quotation is preferred but remains marked. A paler intervening trace is not securely established as an additional authored mark.',crop=cs['B070_04_trouve_separator.jpg']))
D.append(decision('B070-10','Handwritten p.16, li.8 du bas: separator after closing quotation',r'\unsure{:|.}',r'\unsure{:|.}',[887,1660,905,1685],c_doubt=True,unresolved=True,alternatives=[':','.'],confidence='medium',kind='misread symbol or index',scan_shows='There is a definite low dark point to the right of the quotation strokes and a faint trace above it. The faint upper trace is insufficient to establish a second authored dot, so colon and full stop remain alternatives. The text ajouter is not used to decide the sign.',crop=cs['B070_04_trouve_separator.jpg']))
D.append(decision('B070-11','Display (i): lowered class subscript on c at the right',r'c^i_{\handwritten{\chi}}(x)',r'c^i_{\chi}(x)',[1042,1770,1067,1809],diff_c=True,kind='other',scan_shows='The cross-shaped subscript has a left top serif, a descending stem ending in a long right foot, and a rising diagonal crossing that stem. The dark, uniform, serifed impression matches the repeated subscript forms in (ii), while the handwritten psi is thin and freely curved. I read a typewritten chi, possibly a composite typescript glyph; no independent cancelled l or prior reading is established.',crop=cs['B070_05_first_chi.jpg']))
D.append(decision('B070-12','Display (ii): first lowered class subscript on the right',r'c^i_{\handwritten{\chi}}(x)',r'c^i_{\chi}(x)',[1240,1832,1267,1871],diff_c=True,kind='other',scan_shows='A short top-left horizontal, descending stem, bottom-right horizontal foot and rising diagonal form the same serifed cross-shaped type impression as the other class subscripts. These strokes have the weight and regularity of the surrounding typescript, not of the thin pen-written psi.',crop=cs['B070_06_second_chi_pair.jpg']))
D.append(decision('B070-13','Display (ii): second lowered class subscript on the right',r'c^j_{\handwritten{\chi}}(y)',r'c^j_{\chi}(y)',[1331,1832,1358,1871],diff_c=True,kind='other',scan_shows='The lowered sign repeats the top-left serif, long right-projecting foot and crossing diagonal of the preceding class subscript, with the same heavy typescript impression. I retain chi but do not mark this impression as handwritten.',crop=cs['B070_06_second_chi_pair.jpg']))

I=[]
def inv(hand,element,kind,position,first):
 I.append({'sheet_kind':'typescript','hand':hand,'element':element,'kind':kind,'position':position,'first_words_or_objects':first,'transcribed':'yes'})
inv('unnamed hand','Manuscript page number','text','Top centre, x842–953 y45–91','- 5 -')
inv('typewriter','First correction entry','text','Upper body, x372–1084 y153–194',r'p.11, li.7 du bas : K^{\bullet}(T) et non K_{\bullet}(T).')
inv('typewriter','Second correction entry','text','Upper body, x373–1607 y222–325','p.11, li.18 : il devrait y avoir une référence')
inv('typewriter','Third correction entry','text','Upper body, x373–1538 y355–457','p.11, li.11 du bas : référer à (3.1)')
inv('typewriter','Fourth correction entry','text','Upper body, x373–1638 y488–658','p.11, li.9 du bas : “ci-dessus” et non “ci-dessous”.')
inv('typewriter','Fifth correction entry','text','Upper middle, x373–1578 y687–794','p.12,li.6 : “on se ramène immédiatement ...”')
inv('unnamed hand','Reference appended after trait','insertion','Right end of fifth entry, x1498–1633 y749–792',r'(7\unsure{-|.}15)\unsure{.}')
inv('typewriter','Sixth correction entry','text','Upper middle, x373–1420 y819–859','p.12, li.6 du bas : “donc il existe (cf. EGA IV 2.8) ...”')
inv('typewriter','Seventh correction entry','text','Middle, x373–1630 y887–991','p.12, li.3 du bas : “on peut choisir pour C un schéma régulier”')
inv('typewriter','Eighth correction entry','text','Middle, x373–1324 y1021–1057','p.13, li.2 : “il est bien connu (SGA ou EGA ? ) ...”')
inv('unnamed hand','Handwritten additional p.13 reference entry','insertion','Between typed entries, x375–1262 y1053–1091','p.13, li.10 du bas : (ruled IV 2.12) au lieu de (ruled III 2.12).')
inv('typewriter','Ninth typed correction entry','text','Middle, x373–1581 y1091–1206','p.13, li.3 du bas : il semble qu’on utilise le fait déjà cité(sans référence)')
inv('typewriter','Tenth typed correction entry','text','Middle, x373–1286 y1222–1258','p.14, li.10 : “propre et lisse” ne suffit-il pas ?')
inv('typewriter','Eleventh typed correction entry','text','Middle, x373–1473 y1288–1326','p.15, li.10 : “donne naissance à ” plutôt que “provient de”.')
inv('typewriter','Twelfth typed correction entry','text','Lower middle, x373–1635 y1354–1459','p.16, li.14 : au lieu de “par Krull-Akizuki”')
inv('typewriter','Thirteenth typed correction entry','text','Lower middle, x373–1609 y1490–1658','p.16, li.16 : X n’étant pas supposé plat')
inv('unnamed hand','Handwritten additional p.16 entry','insertion','Between typed entries, x375–1199 y1646–1696','p.16, li.8 du bas : “on trouve” ... ajouter “(cf. 7.16)”.')
inv('typewriter','Introduction to two displayed identities','text','Lower body, x373–1249 y1691–1728','p.17, 7.13.6 : les points importants, à savoir :')
inv('typewriter','First displayed identity, including label and comma','display','Lower body, x463–1177 y1736–1810',r'(i) \psi_i(c^i(x)) = (-1)^{i-1}(i-1)!c^i_{\chi}(x),')
inv('unnamed hand','Psi supplied at start of first display','insertion','Within first display, x548–580 y1746–1804',r'\psi')
inv('typewriter','Second displayed identity, including label and comma','display','Lower body, x463–1482 y1806–1875',r'(ii) \psi_{i+j}(c^i(x)c^j(y)) = (-1)^{i+j-1}(i+j-1)!c^i_{\chi}(x)c^j_{\chi}(y),')
inv('unnamed hand','Psi supplied at start of second display','insertion','Within second display, x563–593 y1819–1870',r'\psi')
inv('typewriter','Unfinished continuation sentence after displays','text','Bottom body, x372–1520 y1906–1949','pour lesquels on peut référer à (V 6.5.3 et 6.6.4), ne sont pas')
inv('unnamed hand','Archive sheet number, recorded only as comment','text','Lower left corner, x45–112 y2073–2129','69')

math=[
 r'Confirmed from the upper half: K^{\bullet}(T) versus K_{\bullet}(T). Each K has one upright and two arms, each T one upright and top bar; the marks on K are filled points, raised in the first occurrence and lowered in the second. No double alphabet is inferred.',
 r'Confirmed the ordinary single-outline C in the two prose conditions, S in the two relevant entries, and both X occurrences in the p.16, li.16 entry. None shows independent double striking.',
 r'The typed exposé V in Exp.V, the typed EGA IV, and the final typed V are ordinary Roman capitals without the separate upper and lower rules seen in the handwritten IV and III.',
 r'Confirmed all line and section numbers from the ink, including 3.1, 2.8, 7.13.6, V 6.5.3 and 6.6.4. The only new numerical separator doubt is in the handwritten added reference after trait.',
 r'Both displayed psi letters are handwritten: a freely curved upper bowl is crossed by a long central descending stroke. The lower indices i and i+j are typed. The shape is psi rather than phi; no closed circular bowl is present.',
 r'Display (i), checked symbol by symbol: \psi_i(c^i(x)) = (-1)^{i-1}(i-1)!c^i_{\chi}(x), with an i exponent on each c, the exponent i-1 on (-1), a factorial after the parenthesized i-1, and a separate terminal comma. These are reading checks only.',
 r'Display (ii), checked symbol by symbol: \psi_{i+j}(c^i(x)c^j(y)) = (-1)^{i+j-1}(i+j-1)!c^i_{\chi}(x)c^j_{\chi}(y), with j (a dotted descender) in the second c power and i+j where written. No product dot or extra sign is inserted.',
 r'All three lowered class signs read as chi from their crossing strokes; their typewritten appearance, rather than C’s handwritten classification, is recorded separately in decisions B070-11 through B070-13.',
 r'The paired x indices remain explicitly uncertain as o|0 and l|1. Their mathematical pairing has not been used to resolve the ink.',
 r'No arrow, inequality, commutative diagram, independent drawing, grouping bracket, underlined prose, or deleted passage is present on this page. The Roman-numeral rules are retained as notation. No mathematical assertion has been proved or externally checked.'
]
notation=[
 {'sign':'Filled upper and lower points on K','latex':r'K^{\bullet}(T); K_{\bullet}(T)','evidence':'Small filled points stand respectively above and below the K baseline; each is round rather than a prime or star.','place':'First entry, p.11 li.7 du bas'},
 {'sign':'Ordinary typed mathematical capitals','latex':'K, T, C, S, X','evidence':'Each occurrence has one typewritten outline; no independent doubled stroke is visible.','place':'First entry and prose conditions on p.11, p.12 and p.16'},
 {'sign':'Ruled handwritten Roman numerals','latex':r'\overline{\underline{\mathrm{IV}}}; \overline{\underline{\mathrm{III}}}','evidence':'Upper and lower horizontal rules span, respectively, the I plus V strokes and the three uprights.','place':'Handwritten p.13, li.10 du bas entry'},
 {'sign':'First ambiguous lowered x index','latex':r'x_{\unsure{o|0}s}','evidence':'Closed lowered oval followed by a clear low s; alphabetic versus numeric identity remains unsettled.','place':'p.13, li.3 du bas'},
 {'sign':'Second ambiguous lowered x index','latex':r'x_{\unsure{l|1}s}','evidence':'Tall lowered upright with a short top-left cap and wide bottom foot, followed by s.','place':'p.13, li.3 du bas'},
 {'sign':'Handwritten psi and typed lower indices','latex':r'\handwritten{\psi}_i; \handwritten{\psi}_{i+j}','evidence':'Thin curved bowl with a long central descender; typed i and i+j lie below and to the right.','place':'Beginning of displays (i) and (ii)'},
 {'sign':'Typewritten class chi','latex':r'c^i_{\chi}(x); c^j_{\chi}(y)','evidence':'Repeated serifed cross-shaped impressions with a top-left arm, bottom-right foot and crossing rising diagonal; no independent cancellation is established.','place':'Right side of (i), both factors on right side of (ii)'},
 {'sign':'Superscript i and j; factorials','latex':r'c^i; c^j; (-1)^{i-1}; (-1)^{i+j-1}; (i-1)!; (i+j-1)!','evidence':'The i has a dot and no descender; the j has a dot and a hooked descender. Minus signs are single horizontals, plus signs cross, and each factorial has a vertical stroke and low point.','place':'Both displays'},
 {'sign':'Uncertain short separator in handwritten added reference','latex':r'7\unsure{-|.}15','evidence':'Short low horizontal stroke; a dash is preferred, an elongated point remains possible.','place':'After trait in p.12,li.6'},
 {'sign':'Uncertain low point and separator adjoining closing quotation','latex':r"``on trouve\unsure{.}''\unsure{:|.}",'evidence':'A dark low point below and slightly left of the high quote pair is separate from a farther-right low point with only a faint upper trace.','place':'Handwritten p.16, li.8 du bas'}
]
report={
 'scan':70,'reader':'B','image_views':manifest['image_views'],'reading_path':str(out/'reading.tex'),
 'crops':[{'file':c['file'],'bbox':c['bbox'],'rotation':c['rotation'],'reason':c['reason'],'processing':c['processing']} for c in manifest['crops']],
 'decisions':D,'inventory':I,
 'notes':('One typescript sheet with pen additions, carrying the handwritten manuscript number “- 5 -” and the archival number 69. No title or date appears. It contains fourteen typed correction/reference entries addressing pages 11–17, two handwritten additional entries, an appended handwritten reference, and two displayed identities with pen-written psi signs. The author asks for a reference in Exp.V; wonders whether connectedness of C alone would preserve the definitions; asks SGA or EGA for a known assertion; calls attention to an uncited connected-curve assertion; asks whether “propre et lisse” is sufficient; and questions the inference of smoothness for an X not assumed flat. These are the page’s claims and doubts, not verified results. The final sentence stops after “ne sont pas”, without a final punctuation mark. H supplies only a description and is unavailable as a transcription: every decision has h_reading=null and diff_h=false, and no descriptive omission is counted. The unusual typed single-n form “canule” is confirmed without normalization. The two lowered point indices and the separator after “on trouve” remain explicit C doubts. New in-place uncertainties concern the dash/point separator and final-point writing state in the added reference, and the assignment of the extra low point by the closing quotation after “trouve”. The three class subscripts are read as typewritten chi impressions; their serifed shape could be a composite typewriter construction, but no readable cancelled underlying l is asserted. No proof, computation or external background check was performed.'),
 'math_reading_decisions':math,'check_events':[],'notation':notation,
 'abbreviations':[{'form':'p.','expansion':'page'},{'form':'li.','expansion':'ligne'},{'form':'Exp.','expansion':'exposé'},{'form':'cf.','expansion':'confer / voir'},{'form':'EGA','expansion':'not expanded on this page'},{'form':'SGA','expansion':'not expanded on this page'}],
 'slips':['The unusual typed form “canule”, with a single n, is preserved without correction; no further spelling slip is asserted.'],
 'completion':('Complete independent diplomatic second pass of scan 070: the whole source image was viewed once for layout, then halves a and b once each in that order. Every typed and handwritten word, accent, reference, punctuation mark, mathematical letter, index, sign, and visible state was checked from those views. Six remaining open places received one retained enlarged crop each, viewed once. Every substantive C difference, every explicit C doubt, and every new uncertainty has a decision row with a whole-image bbox; H was treated as description-only. The full reading, inventory, notation, crops and manifest are saved. No OCR, other pages, peer files, external sources, delegation or TeX compilation was used. Only source balance/schema checks follow this writing step.')
}
(out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'reading':str(out/'reading.tex'),'report':str(out/'report.json'),'manifest':str(out/'crop_manifest.json'),'decisions':len(D),'diff_c':sum(d['diff_c'] for d in D),'explicit_c_doubts':sum(d['c_doubt'] for d in D),'inventory_rows':len(I),'crops':len(manifest['crops'])},indent=2))
