from pathlib import Path
import json
base=Path('/workspace/scratch/be39e9f81d6d/out/readings/scan013/R2')
findings=[]
def add(id,place,c,h,final,evidence,confidence,kind,bbox,crop='',doubt_action='',diff_c=False,diff_h=False,marked_in_H=False,math_note='',s_id=''):
    findings.append(dict(id=id,place=place,c=c,h=h,final=final,evidence=evidence,confidence=confidence,kind=kind,marked_in_H=marked_in_H,diff_c=diff_c,diff_h=diff_h,bbox=bbox,crop=('readings/scan013/R2/'+crop+'.png') if crop else '',doubt_action=doubt_action,s_id=s_id,math_note=math_note))
add('C01','Top diagram, label right of Z-to-Z upward arrow',r'\unsure{2|\wr}',r'\mathrm{id}',r'\unsure{2|\wr}','One hooked upright with a low right return; no second letter d. Numeral versus vertical wave is not settled. Label stands on the right of the arrow.','medium','misread symbol or index',[560,134,600,186],'01_vertical_label','retain',False,True,False,'The splitting sentence does not decide the kernel-map label.')
add('C02','Sentence after the diagram',r'\unsure{splitte}','splittée','splitte','Final short e is at the baseline; there is no detached acute accent or second final e.','high','misread word',[805,323,947,382],'02_splitte','resolve',True,True)
add('C03','Raised label before Toute',r'\inserted{\unsure{Rmq}}',r'\emph{Remarque}',r'\inserted{Rmq}, raised with curved connector','Upper half: R, low m and descending q are legible. The curved stroke runs below the label toward the beginning of Toute. It is reproduced, not replaced by a full word.','high','abbreviation expanded or spelling modernised',[290,404,410,497],'','resolve',True,True)
add('C04','After image inverse',r"d'\deleted{\unsure{une}}l'ext.",r"d'une ext.",r"d'\deleted{\unsure{une}}l'ext.",'A dark crossing/baseline stroke obscures the small old word; the following tall l and apostrophe remain live. The underform une is still doubtful.','medium','deletion state (struck given live or live given struck)',[968,544,1214,591],'03_cancelled_une','retain',False,True)
add('C05','After torseur',r'\unsure{sur|sous}','sous',r'\unsure{sur|sous}','The low waves end in a short downstroke. Sur is the closer reading, but the compressed middle does not exclude sous.','medium','misread word',[1455,1086,1534,1135],'04_torseur_sur','retain',False,True)
add('C06','Canceled word in the underlined phrase',r'\deleted{\unsure{sous}}','sur',r'\deleted{\unsure{sous|sur}}','A crossing horizontal stroke runs through the small word. Initial sinuous stroke and a low loop favor sous; the canceled middle also permits sur.','low','deletion state (struck given live or live given struck)',[1014,1191,1090,1240],'05_cancelled_sous','retain',True,True)
add('C07','Overwritten symbol before the first affine field subscript',r'\deleted{\unsure{\mathbb{Z}}}\mathbb{F}_2',r'\mathbf{F}_2',r'\deleted{\unsure{\mathbb{Z}|Z}}\mathbb{F}_2','The live double upright F is clear. A diagonal and low base survive underneath; the number of old Z strokes is obscured by the overwrite.','low','omission',[1109,1187,1157,1244],'06_overwritten_field','retain',True,True,False,'This is an alphabet/state difference, not H’s declared bold-versus-blackboard macro encoding.')
add('C08','Canceled word after the second ou encore comma',r'(ou encore, \deleted{\illegible{1}}',r'\struck{\ill{}} ou encore,',r'(ou encore, \deleted{\illegible{1}}','Only an initial hook and one lower protrusion survive a long horizontal cancellation. No defensible complete word can be recovered. The cancellation follows ou encore, rather than preceding it.','low','insertion or placement',[1197,1188,1546,1245],'07_deleted_word','retain',False,True,True)
add('C09','Decorative S in the box',r'\unsure{\mathfrak{S}|\mathcal{S}}',r'\mathfrak{S}',r'\unsure{\mathfrak{S}|\mathcal{S}}','Broad outer curl, inner return and raised right tip are secure; they do not settle the font classification. Later S uses the same primary alphabet without repeating the doubt.','medium','misread symbol or index',[1143,1592,1219,1658],'08_box_S_subscript','retain',False,False)
add('C10','Index following the boxed S',r'\unsure{2|n}','2',r'\unsure{2|n}','A shallow falling curve with an upturned foot favors 2; the abbreviated form still allows n. The section heading is not used to decide it.','medium','misread symbol or index',[1215,1637,1248,1664],'08_box_S_subscript','retain',False,False)
add('C11','First A, in the parenthesis below the box',r'\unsure{\mathcal{A}|A}_2',r'\mathfrak{A}_2',r'\unsure{\mathcal{A}|A}_2','Rounded open bowl with a narrow right stem favors calligraphic A over plain A; it does not show the angular/internal construction assumed by H’s Fraktur reading. The same primary alphabet is used in the bottom A3.','medium','misread symbol or index',[943,1717,1007,1779],'09_A2','retain',False,True)
add('C12','Vertical relation below F3 plus',r'\rotatebox{90}{$\unsure{\simeq|=}$}',r'\simeq vertical',r'\rotatebox{90}{$\simeq$}','The left stroke has a visible bent/wavy head and return; the neighboring right stroke is straighter. This differs from the two straight strokes below F3 star.','medium','misread symbol or index',[735,2058,767,2092],'10_field_stack','resolve',True,False)
add('C13','Old symbol underneath the bottom live F',r'\deleted{\unsure{\mathbb{Z}}}\mathbb{F}_3^{+}',r'\mathbf{F}_3^{+}',r'\deleted{\mathbb{Z}}\mathbb{F}_3^{+}','Parallel old diagonals with their top/base survive beneath the live double upright and middle bar of F. The old doubled Z can be read here.','medium','omission',[721,2155,818,2224],'11_bottom_correction','resolve',True,True)
add('N01','Toute extension sentence',r'de un $\Gamma$ par un $Z$',r'de $\Gamma$ par $Z$',r'de un $\Gamma$ par un $Z$','Upper half shows two separate, full-width un groups, one after de and one after par.','high','omission',[1046,450,1484,513],diff_h=True)
add('N02','Z.Aut(Z) line',r'Z.\operatorname{Aut}(Z)',r'Z.\operatorname{Aut}(Z)',r'Z.\operatorname{Aut}(Z).','Upper half shows a detached final baseline point after the closing parenthesis. The expression is on its own line, beginning at the paragraph’s left edge.','high','omission',[282,659,532,719],diff_c=True,diff_h=True)
add('N03','Divider before section 4',r'two separately drawn rules','absent',r'two separately drawn rules','Upper half: two detached near-horizontal strokes of unequal length; the upper one slopes upward to the right.','high','drawing or diagram',[779,760,1028,804],diff_h=True)
add('N04','Torsor noun in a)',r'torseur','torseurs','torseur','The final small r shoulder is followed by a gap; no further s is present.','high','misread word',[1260,1080,1432,1134],'04_torseur_sur',diff_h=True)
add('N05','Opening parenthesis in a)',r'Z_2 ou encore, ... F_2 (ou encore,',r'Z_2 (ou encore, ... F_2 ... ou encore,',r'Z_2 ou encore, ... F_2 (ou encore,','Both halves show no opening curve before the first ou. A separate high opening curve precedes the second ou.','high','insertion or placement',[340,1182,1258,1264],'07_deleted_word',diff_h=True)
add('N06','Extent of espace affine underline',r'\uline{espace affine \deleted{\unsure{sous}}}',r'\emph{espace affine sur $\mathbf{F}_2$}',r'\uline{espace affine \deleted{\unsure{sous|sur}}} followed by the field symbol','The underline ends just to the left of the overwritten field. It runs beneath the canceled word, but not beneath the final field and its index.','high','insertion or placement',[654,1184,1163,1264],'06_overwritten_field',diff_h=True)
add('N07','Parenthesis with A2',r'separate centered display',r'\qquad (\mathfrak{A}_2=\{1\}) on the box baseline',r'parenthesis beneath the right half of the box','Lower half and crop: the whole parenthesis occupies a lower line, starting well to the right of the frame’s left edge.','high','insertion or placement',[895,1709,1191,1800],'09_A2',diff_c=True,diff_h=True)
add('N08','Frame around the cardinal-2 identity',r'\boxed{...}',r'\boxed{...}',r'TikZ frame with open upper-left and lower-right corners','Lower half shows the upper-left pen gap; the crop also shows the right vertical ending above the bottom stroke. The unequal sloping stroke geometry is retained.','high','drawing or diagram',[525,1560,1286,1718],'08_box_S_subscript',diff_c=True,diff_h=True)
add('N09','Vertical relation immediately below Aff(1,F3)',r'\rotatebox{90}{$\simeq$}',r'\wr',r'\rotatebox{90}{$\simeq$}','There are two separate upright components: a wavy left stroke and a straighter right stroke. This is more than a single wr/wavy sign.','high','misread symbol or index',[797,1954,831,1990],'10_field_stack',diff_h=True)
add('N10','Top diagram, Z-to-G horizontal connector',r'\arrow[r,dash]',r'\arrow[r]',r'\unsure{-|\to}, shown as an uncertain connector in tikz-cd','The shaft has a tiny pointed/downturned end but no confidently distinct paired head. Preserve both headless and right-arrow readings.','low','drawing or diagram',[625,94,689,117],'12_top_shafts',diff_c=True,diff_h=True)
add('N11','Top diagram, lower 1-to-Z connector',r'\arrow[r,dash]',r'\arrow[r]',r'\unsure{-|\to}, shown as an uncertain connector in tikz-cd','A short downward terminal spur is visible. It may be an incomplete head or a blunt hooked termination; no paired wings are resolved.','low','drawing or diagram',[449,222,514,244],'13_bottom_shafts',diff_c=True,diff_h=True)
add('N12','Top row, G-to-Gamma and Gamma-to-1 connectors',r'\arrow[r,dash] for both',r'\arrow[r] for both',r'headless shafts for both','The ends have nib thickening but no separate arrowhead strokes. The first 1-to-Z arrow, in contrast, has two clear wings in the upper half.','high','drawing or diagram',[788,89,966,122],'12_top_shafts',diff_h=True)
add('N13','Lower row, final three horizontal connectors',r'\arrow[r,dash] for all three',r'\arrow[r] for all three',r'headless shafts for all three','All three are continuous blunt shafts without head strokes. Upward arrows remain clearly headed.','high','drawing or diagram',[621,209,1000,249],'13_bottom_shafts',diff_h=True)
add('N14','Detached trace above and right of Z.Aut(Z)',r'absent',r'absent',r'uncertain two-lobed trace, drawn without lexical value','The enlargement shows two touching dark lobes. Their separation from all writing leaves pen trace versus surface matter unresolved.','low','other',[1148,647,1163,668],'14_detached_pair_upper',diff_c=True,diff_h=True)
add('N15','Detached point to the right of the divider',r'absent',r'absent',r'uncertain isolated point, drawn without punctuation value','A dark compact point is visible in surrounding surface texture. It cannot be securely assigned to handwriting.','low','other',[1305,780,1321,800],'15_detached_point_rule',diff_c=True,diff_h=True)
add('N16','Detached pair to the right of the cardinal-2 box',r'absent',r'absent',r'uncertain oblique pair, drawn without punctuation value','Two dark separated spots lie on a short diagonal, away from the formula. Writing versus surface trace remains unresolved.','low','other',[1498,1638,1522,1664],'16_detached_pair_box',diff_c=True,diff_h=True)
add('N17','Final A3 identity and the cardinal-3 chain',r'two independently centered displays',r'two independently centered displays',r'common display block with A3 line beginning slightly right of the chain start','Lower half: A3 starts near the left end of the main S3 chain, not beneath its center. The two vertical decompositions retain their positions under Aff and GP.','high','insertion or placement',[522,1874,1540,2231],diff_c=True,diff_h=True)

inventory=[]
def inv(element,kind,position,words,hand='his hand'):
    inventory.append(dict(sheet_kind='text',hand=hand,element=element,kind=kind,position=position,first_words_or_objects=words,transcribed='yes'))
inv('Two-row extension diagram','diagram','top, x400–1290 y75–260','1, Z, G, Gamma, 1; 1, Z, G prime, Gamma prime, 1; (E), (E prime)')
inv('Splitting sentence','text','x302–1329 y323–386',"Si l'extension (E) splitte")
inv('Raised remark abbreviation','insertion','x294–397 y408–449','Rmq')
inv('Curved remark connector','drawing','x298–396 y434–489','curved stroke below Rmq toward Toute')
inv('Remark paragraph','text','x322–1482 y450–619','Toute extension splittée G de un Gamma par un Z')
inv('Canceled old word in remark','deletion','x1011–1094 y548–579','une, doubtful')
inv('Remark concluding expression','display','x285–527 y666–717','Z.Aut(Z).')
inv('Detached upper trace','drawing','x1148–1163 y647–668','two lobes; writing/surface uncertain')
inv('Double divider','drawing','x781–1025 y765–802','two unequal horizontal strokes')
inv('Detached divider point','drawing','x1305–1321 y780–800','isolated point; writing/surface uncertain')
inv('Section heading','text','x300–1148 y900–973','4) Ens. de petit cardinal')
inv('Cardinal-2 heading and opening text','text','x292–1624 y1078–1142','a) Cardinal 2; Ens de cardinal 2; torseur')
inv('Cardinal-2 continuation','text','x348–1545 y1190–1563','ou encore, espace affine; (ou encore, espace affine de dim 1')
inv('Underlined affine phrase','text','x657–1118 y1184–1280','espace affine and canceled sous/sur; underline')
inv('Canceled preposition','deletion','x1014–1090 y1191–1240','sous|sur')
inv('Old field-symbol underform','deletion','x1109–1157 y1187–1244','double-stroked or plain Z beneath F')
inv('Canceled unrecoverable word','deletion','x1430–1546 y1214–1245','one illegible word after ou encore comma')
inv('Cardinal-2 identity','display','x576–1248 y1591–1675','Aff(1,F2) simeq Aff(Z2) simeq decorative S index 2|n')
inv('Identity frame','drawing','x525–1286 y1560–1718','slanting frame; two pen gaps')
inv('Detached box pair','drawing','x1498–1522 y1638–1664','oblique pair; writing/surface uncertain')
inv('Alternating-group parenthesis','display','x895–1191 y1709–1800','(A2={1}) beneath right part of box')
inv('Cardinal-3 heading','text','x328–676 y1784–1858','b) Cardinal 3, underlined')
inv('Cardinal-3 main chain','display','x522–1487 y1874–1964','S3 simeq Aff(1,F3) simeq Gl(2,F2) simeq GP(1,F2)')
inv('Affine group decomposition','display','x728–879 y1954–2132','vertical simeq; F3 plus . F3 star; vertical simeq and equals; Z3 Z2')
inv('Projective quotient decomposition','display','x1266–1540 y1954–2054','vertical equals; Gl(2,F2)/F2 star')
inv('Last alternating-group identity','display','x557–987 y2155–2231','A3 simeq corrected F3 plus (simeq Z3)')
inv('Old Z at bottom','deletion','x721–786 y2155–2224','double-stroked Z beneath F')
inv('Archive foliation','margin note','lower left, x45–121 y2275–2328','12, recorded only as archive-sheet comment','unnamed hand')

unresolved=[
 {'place':'C01: label on first upward arrow','reading':r'\unsure{2|\wr}','alternatives':'2 | vertical wave (wr)','confidence':'medium'},
 {'place':'C04: canceled word after image inverse','reading':r'\deleted{\unsure{une}}','alternatives':'une; not securely recoverable beneath cancellation','confidence':'medium'},
 {'place':'C05: after torseur','reading':r'\unsure{sur|sous}','alternatives':'sur | sous','confidence':'medium'},
 {'place':'C06: canceled underlined preposition','reading':r'\deleted{\unsure{sous|sur}}','alternatives':'sous | sur','confidence':'low'},
 {'place':'C07: old symbol beneath first F2','reading':r'\deleted{\unsure{\mathbb{Z}|Z}}','alternatives':'double-stroked Z | plain Z','confidence':'low'},
 {'place':'C08: canceled word after second ou encore comma','reading':r'\deleted{\illegible{1}}','alternatives':'one word; no defensible complete reading','confidence':'low'},
 {'place':'C09: first decorative S','reading':r'\unsure{\mathfrak{S}|\mathcal{S}}','alternatives':'Fraktur S | calligraphic S','confidence':'medium'},
 {'place':'C10: boxed S index','reading':r'\unsure{2|n}','alternatives':'2 | n','confidence':'medium'},
 {'place':'C11: first A','reading':r'\unsure{\mathcal{A}|A}','alternatives':'calligraphic A | plain A','confidence':'medium'},
 {'place':'N10: top Z-to-G shaft','reading':r'\unsure{-|\to}','alternatives':'headless shaft | right arrow with tiny head','confidence':'low'},
 {'place':'N11: lower 1-to-Z shaft','reading':r'\unsure{-|\to}','alternatives':'headless hooked shaft | right arrow with incomplete head','confidence':'low'},
 {'place':'N14: upper detached two-lobed trace','reading':'drawn with uncertainty','alternatives':'pen trace | surface trace','confidence':'low'},
 {'place':'N15: point right of divider','reading':'drawn with uncertainty','alternatives':'pen point | surface trace','confidence':'low'},
 {'place':'N16: pair right of box','reading':'drawn with uncertainty','alternatives':'pen points | surface trace','confidence':'low'}
]
report={
 'scan':'013','reader':'R2','start_utc':'2026-11-20 03:35:42 UTC','end_utc':'PENDING',
 'images_viewed':[
 '/workspace/scratch/be39e9f81d6d/source/SP38_CW_75_scans/J75-02_75_scan013.jpg',
 '/workspace/scratch/be39e9f81d6d/source/SP38_CW_75_scans/J75-02_75_scan013_a.jpg',
 '/workspace/scratch/be39e9f81d6d/source/SP38_CW_75_scans/J75-02_75_scan013_b.jpg'],
 'reading_file':str(base/'reading.tex'),'crop_count':16,
 'findings':findings,'inventory':inventory,
 'notation':[
 {'sign':'Z / double-stroked Z','reading':r'Z at top; \mathbb{Z} in cardinal examples','ink':'The top Z has one diagonal; the small cardinal-group Z has visibly parallel diagonals. Under the first F correction the old alphabet remains uncertain.','place':'top diagram and Z.Aut(Z); cardinal 2 and 3 displays'},
 {'sign':'F','reading':r'\mathbb{F}','ink':'Two upright strokes with a shared top and middle bar; checked at individual visible occurrences.','place':'cardinal-2 prose and both sets of examples'},
 {'sign':'G, Gamma and primes','reading':r'G,\Gamma,G\prime,\Gamma\prime','ink':'G has a round open bowl and short right ledge; Gamma has an angular top. Primes are detached raised single strokes.','place':'top diagram'},
 {'sign':'vertical label','reading':r'\unsure{2|\wr}','ink':'One small hooked upright with a low right foot; no second letter.','place':'right of first upward arrow'},
 {'sign':'horizontal connector ends','reading':r'\unsure{-|\to} at two locally doubtful shafts; other shafts headless','ink':'Tiny downward terminal spurs at top Z-to-G and lower 1-to-Z; distinct paired wings only on top 1-to-Z.','place':'top diagram'},
 {'sign':'decorative S','reading':r'\unsure{\mathfrak{S}|\mathcal{S}}, then \mathfrak{S}','ink':'Broad outer curl and inner return, with a raised right tip.','place':'boxed expression and cardinal-3 chain'},
 {'sign':'rounded A','reading':r'\unsure{\mathcal{A}|A}, then \mathcal{A}','ink':'Open round bowl with a narrow low right stem.','place':'parenthesis A2 and last A3'},
 {'sign':'simeq / equals','reading':r'\simeq and rotated \simeq; rotated =','ink':'Wave plus straight stroke are distinct from two straight uprights; the lower-left rotated relation is overinked but retains a wavy left stroke.','place':'boxed identity and cardinal-3 display'},
 {'sign':'raised plus and star','reading':r'^{+}, ^{*}','ink':'The plus over F3 is heavily reinforced but has a continuous cross; the star has extra oblique strokes.','place':'cardinal-3 field groups'},
 {'sign':'multiplication point','reading':r'Z.\operatorname{Aut}(Z); \mathbb{F}_3^{+}\mathbin{.}\mathbb{F}_3^{*}','ink':'The product points sit low, near the baseline.','place':'remark expression and field decomposition'},
 {'sign':'boxed S index','reading':r'\unsure{2|n}','ink':'A shallow falling-and-rising trace; 2 is primary, not forced from Cardinal 2.','place':'right end of boxed identity'}
 ],
 'abbreviations':[
 {'written':'Rmq','expansion':'Remarque'}, {'written':'ext.','expansion':'extension'},
 {'written':'Ens.','expansion':'Ensembles'}, {'written':'Ens','expansion':'Ensembles'},
 {'written':'dim','expansion':'dimension'}, {'written':'vect.','expansion':'vectoriels'},
 {'written':'can.','expansion':'canoniquement'}
 ],
 'notes':[
 'The upper block continues an extension diagram, gives a splitting sentence, and adds a raised Rmq about split extensions and Z.Aut(Z). No date is present.',
 'Internal heading 4) Ens. de petit cardinal is followed by a) Cardinal 2 and b) Cardinal 3. The two Cardinal phrases and espace affine phrase are underlined; these are not promoted to editorial headings.',
 'The literal de un Gamma and par un Z are retained. The first verb is splitte without an acute accent, while the later extension adjectives are splittée.',
 'The author’s own explicit doubt words or question marks were not observed. All question marks introduced by unsure are editorial reading doubts.',
 'The index on the boxed decorative S remains uncertain; order calculations did not choose it. Likewise the splitting claim did not choose the small label beside the kernel arrow.',
 'The A2 parenthesis lies below the right portion of the box. The bottom A3 line starts slightly to the right of the main S3 line. The diagram’s upward arrows and headless or uncertain horizontal shafts are preserved.',
 'Three isolated dark traces are included without lexical or punctuation meaning because writing versus surface matter could not be settled. They are not counted as manuscript punctuation.',
 'Archive foliation 12 is a comment only; its hand is unnamed. No repeated cotefile marker or manuscript page number has been added.',
 'S.json is an empty array. There are no S statements to confirm or overturn. No H drawing supplement exists in the supplied page packet.',
 'H bold number-field macros are treated as equivalent to mathbb when the local ink is doubled. H page 12 is editorial archive identification, not a collation difference.'
 ],
 'checks':[
 {'statement':'Orders in the cardinal-2 and cardinal-3 affine/linear group expressions','event_type':'actual order calculation','reasoning':'For a field of q elements, a map x -> ax+b has q(q-1) choices with a nonzero. Thus the two affine orders are 2 and 6. An invertible 2 by 2 matrix over F2 has 3 choices for its first nonzero column and 2 for the second independent column, so its order is 6. F2 star has one element, so the written quotient also has order 6.','outcome':'The written examples have compatible orders. This does not prove every displayed isomorphism and was not used to settle the ambiguous boxed index.'},
 {'statement':'The prose claim about one-dimensional spaces over F2 being canonically isomorphic','event_type':'actual uniqueness check','reasoning':'Each such space has exactly one nonzero vector. A linear isomorphism must send that vector to the unique nonzero vector in the other space, so there is exactly one possible isomorphism.','outcome':'The can. isomorphes claim is mathematically consistent as written.'},
 {'statement':'Bottom A3, additive F3 and Z3 identification','event_type':'actual group check','reasoning':'The even permutations of three elements are the identity and the two 3-cycles, generated by a 3-cycle. The additive group of F3 is generated by 1 and also has order 3.','outcome':'The final live formula is consistent. The canceled Z underform is transcribed from visible strokes, not supplied by this check.'}
 ],
 'unresolved':unresolved,
 'c_doubt_map':{f'C{i:02d}':desc for i,desc in enumerate(['vertical arrow label','splitte','Rmq','canceled une','sur|sous','canceled sous','old Z before first F2','canceled illegible word','S alphabet','boxed S index','A alphabet','lower-left vertical relation','old Z before last F3'],1)},
 'workflow':{'whole_views':1,'upper_half_views':1,'lower_half_views':1,'crop_views':16,'recropped_settled_loci':0,'external_sources_used':False,'ocr_or_recognition_used':False,'compiled':False},
 'self_check':{'all_C_doubts_mapped':True,'C_doubt_count_including_illegible':13,'S_rows':0,'all_inventory_entries_transcribed':True,'latex_balance':'PENDING','report_reading_synchronization':'PENDING'}
}
(base/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
manifest=json.loads((base/'crop_manifest.json').read_text())
for item in manifest['crops']:
    item['visually_inspected']=True
manifest['viewing_order']=['whole image','upper half','lower half']+[v['id'] for v in manifest['crops']]
manifest['crop_count']=16
manifest['no_recrops_of_settled_loci']=True
(base/'crop_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print('Wrote reading.tex, report.json and updated crop_manifest.json.')
print('Findings:',len(findings),'Inventory:',len(inventory),'Unresolved:',len(unresolved))
