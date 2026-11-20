import json,csv
from pathlib import Path
base=Path('/workspace/scratch/18ee30ea2ccf')
rows=[]
def row(i,decision,reading,evidence,crop,confidence):
 rows.append({'id':f'M{i:04d}','scan':67,'decision':decision,'reading':reading,'what the ink shows':evidence,'crop':crop,'confidence':confidence})
row(1294,'undecided',r'à mettre \unsure{au net|au point|après}',"An accented à, the initial m humps and paired tall t strokes of mettre remain visible in black. The continuation is crossed by the separate red Ajout annotation and its strokes; the surviving low curves and terminal upright do not distinguish net, point or après.",[330,18,780,114],'low')
row(1295,'undecided',r'sur les \unsure{propriétés}',"Sur has a small initial turn, shallow u and terminal hook; les has its high l and joined low ending. The last word has two p-like descending strokes and a later upright, but its compressed intervening letters, acute accent and final plural ending are not separately secure.",[875,20,1300,110],'low')
row(1296,'undecided',r'\unsure{Hilbert|hilbertiens}',"The initial tall stem and following i/l/b-like uprights are visible; the latter half runs into a thin horizontal trace and an indistinct terminal loop. Those ending strokes do not securely separate the short Hilbert form from the additional letters of hilbertiens.",[1340,25,1640,125],'low')
row(1297,'first','développer',"A looped d is followed by an acute mark over é, the shallow v/e sequence, a tall l, then the low o and descending p group. The joined final er extends to the right beneath the diagonal cancellation crossing.",[30,1070,85,1410],'medium')
row(1298,'undecided',r'\unsure{Conséquences|Conséquence}',"The large open C is clear, but much of the following sequence is flattened by thick horizontal ink; the q-like descent meets the underline. The small terminal group before the comma cannot establish an additional plural s, and the acute mark is not independently distinct.",[12,1770,85,2040],'low')
row(1299,'undecided',r'\unsure{changement de notation}',"A dense initial ch-like cluster and a long barred word precede a short low cluster and a final group with tall t-like strokes. Cancellation and underlining merge the interiors, so changement, de and notation cannot each be verified as complete words.",[12,1470,97,1830],'low')
row(1300,'undecided',r'\unsure{notations}',"Several low separated strokes lead into a long horizontal run and a dark t-like upright near its end. The o/a loops and the final i-o-n-s sequence are not separately distinguishable in this compressed word.",[42,1380,123,1650],'low')
row(1301,'undecided',r'\unsure{répétées|ordonnées|comptées}',"The word between u and suivant contains a short initial curved group, a long dipping upright and a later hooked tall stroke, followed by an elevated dot and low tail. These features do not securely establish the opening letters or the accents required to select répétées, ordonnées or comptées.",[95,470,182,665],'low')
row(1302,'undecided',r'\unsure{de}',"The small deleted group is a dense low bowl with an upright left edge and a triangular overstroke. Its possible d ascender and e loop are merged with the cancellation, so de remains unconfirmed.",[135,1745,180,1910],'low')
row(1303,'undecided',r'\unsure{la suite en module|leur suite en module}',"After que, the first group is a compact tall curved sign; the following low word is crossed diagonally, then a short double curve precedes a longer group with d/l-like rises. I cannot separately verify the article, suite, en and every letter of module, or distinguish la from leur.",[130,750,202,1390],'low')
row(1304,'undecided',r'\unsure{cette liste}',"The first group has crowded upright strokes and a long low exit; the second has a tall initial stroke, a detached dot and a descending terminal hook. The t/e sequence in cette and s/t/e sequence in liste remain too compressed to confirm both whole words.",[145,110,230,500],'low')
row(1305,'undecided',r'\unsure{contient}',"The group before the line-ending qu'un has a low curved beginning and an upright obscured by the heavy diagonal slash. The internal n-t-i-e-n sequence and terminal t cannot be counted separately through that stroke.",[155,16,240,530],'low')
row(1306,'undecided',r'\unsure{d\'une infinité de valeurs nulles}',"Above and below the continuous deletion bar survive a loop, short uprights, dots and long low joins. The five proposed words d'une, infinité, de, valeurs and nulles, including the apostrophe and acute accent, cannot each be verified; the existing deleted layer is retained.",[180,16,290,1060],'low')
row(1307,'undecided',r'\unsure{$\lambda_i(u)=0$ pour les autres $i$}',"The crowded struck band preserves small upright and lowered strokes, while short horizontals merge with its long cancellation line. I cannot independently confirm lambda, its index i, both parentheses around u, the equality and zero, the words pour/les/autres, or the final i; the whole proposed sequence remains uncertain.",[170,16,290,1100],'low')
row(1308,'undecided',r'\illegible{2}',"At the end of the crossed line before the next formula, low clusters with a dot, a rising stroke and a hooked end survive among the cancellation curves. They do not support a reliable lexical reading or an independently verified two-word count; the original count is preserved.",[190,16,285,530],'low')
row(1309,'undecided',r'\unsure{$(\rho_i(u)=(\lambda_i((u^*u)^{1/2}))$|$\rho_i(u)=(\lambda_i(uu^*u)^{1/2})$}',"The leading rho group and equals are followed by an opening curve, lambda with a lowered i, then a tall opening curve and a dark doubled trough before the raised star; one further u is visible after the star. A closing curve, elevated 1/2 and two final closing curves are visible, but the initial u count and exact allocation of all parentheses remain unresolved; the narrower same-line u-star-u example does not settle the fused trough.",[195,1485,285,2055],'low')
row(1310,'first','propres',"The word shows a long first p descent, a small rounded middle group and a second, shorter p-like downward stroke. The following r/e/s run ends in a long low rightward stroke, matching the same-page shape of propres without an added upright.",[250,1600,335,1820],'medium')
views=[{'path':'source/DM01_1_001-160_scans/1_scan067.jpg','box':[0,0,1679,2162],'scale':1,'contrast':1,'purpose':'Full-page locator for top and sideways margin marks.'}]
specs=[
('top',[300,15,1655,128],2,0,1,'Top annotation context.'),
('margin',[22,16,390,2125],1.5,90,1,'First rotation locator; text was inverted.'),
('margin_cw',[22,16,390,2125],1.5,-90,1,'Correctly oriented margin locator.'),
('top_detail',[325,20,1660,116],3,0,1,'Top annotation words and red overlay.'),
('top_left',[330,18,780,114],4,0,1,'M1294 black phrase under red annotation.'),
('top_right',[870,20,1660,125],3,0,1,'M1295–M1296 top words.'),
('margin_lower',[22,1060,390,2070],3,-90,1,'Lower margin heading and formula context.'),
('margin_upper',[22,16,390,1090],3,-90,1,'Upper margin line continuations.'),
('heading',[0,1470,97,2070],4,-90,1,'M1298–M1299 heading and underline.'),
('notations',[65,1350,125,1700],5,-90,1,'M1300 initial detail; upper edge clipped some neighboring ink.'),
('repetees',[100,570,175,1000],5,-90,1,'Locator for repeated-word line; shows preceding propres.'),
('phrase_mod',[140,490,218,1910],3,-90,1,'M1302–M1305 line context.'),
('lambda_zero',[175,80,257,770],4,-90,1,'Crossed sequence containing M1306–M1308.'),
('formula',[195,1485,285,2055],5,-90,1,'M1309 whole formula.'),
('propres',[250,1420,302,1810],5,-90,1,'M1310 initial location.'),
('formula_inner',[210,1530,272,1805],8,-90,1,'M1309 factors, star, exponent and closing curves.'),
('formula_comparison',[220,700,285,1180],5,-90,1,'Same-page unmarked u-star-u comparison.'),
('after_formula_lower',[250,1070,335,2070],3,-90,1,'M1310 line context and nearby deletion.'),
('after_formula_upper',[245,16,335,1110],3,-90,1,'Continuation locator after M1309.'),
('margin_topword',[30,1070,85,1410],5,-90,1,'M1297 accent and letter group.'),
('short_de',[135,1745,180,1910],6,-90,1,'M1302 cancelled short group.'),
('top_properties',[1020,20,1300,110],5,0,1,'M1295 final word and accent uncertainty.'),
('top_hilbert',[1340,25,1640,125],5,0,1,'M1296 terminal letter uncertainty.'),
('notations_full',[42,1380,123,1650],6,-90,1,'M1300 complete word-height detail.'),
('repetees_full',[96,700,175,990],6,-90,1,'Preceding propres/de location comparison.'),
('suite_module',[130,750,195,1390],5,-90,1,'M1303 phrase and article.'),
('cette_liste',[145,110,210,500],6,-90,1,'M1304 initial word-group detail.'),
('contient_wrap',[165,1700,230,2070],6,-90,1,'Following line start for M1305 boundary location.'),
('deleted_nulles',[185,40,255,735],4,-90,1,'M1306–M1308 cancelled band.'),
('propres_full',[260,1630,307,1795],7,-90,1,'M1310 detail; descender required larger box.'),
('repetees_location',[100,145,165,730],5,-90,1,'M1301 actual location between u and suivant.'),
('cette_contient',[160,20,230,530],5,-90,1,'M1304–M1305 phrase boundaries.'),
('deleted_nulles_full',[190,20,290,1060],4,-90,1,'M1306–M1308 wider deletion context.'),
('lambda_sentence',[175,20,250,800],5,-90,1,'M1307 proposed symbols and word sequence under bar.'),
('heading_letters',[12,1770,85,2040],6,-90,1,'M1298 ending before comma.'),
('heading_notation',[12,1470,85,1830],5,-90,1,'M1299 three proposed word groups.'),
('repetees_word',[110,480,170,660],8,-90,1,'M1301 distinguishing opening and accent marks.'),
('cette_liste_words',[165,180,227,365],8,-90,1,'M1304 internal letters.'),
('contient_word',[170,22,233,180],8,-90,1,'M1305 diagonal slash and residual strokes.'),
('nulles_line',[185,40,260,700],5,-90,1.7,'M1306–M1308 contrast check of struck line.'),
('formula_intro',[190,22,263,410],6,-90,1,'M1308 residual line-ending clusters.'),
('propres_word',[270,1625,310,1805],8,-90,1,'M1310 letter sequence; descender still tight.'),
('line4_lower',[165,1320,270,2075],4,-90,1,'Crossed paragraph lower-line context.'),
('line4_middle',[165,640,270,1390],4,-90,1,'Middle line leading into M1306–M1308.'),
('line4_upper',[165,0,270,710],4,-90,1,'Full continuation of M1306–M1308 band.'),
('propres_complete',[250,1600,335,1820],7,-90,1,'M1310 full decisive ink including both descents.'),
('top_surles',[875,30,1050,105],6,0,1,'M1295 separate sur and les.'),
('top_start_complete',[305,14,790,122],5,0,1,'M1294 common words and separate red layer.'),
('suite_article',[135,1170,202,1390],7,-90,1,'M1303 article curve and next word start.'),
('repetees_complete',[95,470,182,665],7,-90,1,'M1301 complete height including marks above baseline.')]
for n,b,s,r,c,p in specs:
 views.append({'path':f'work/scan067_a_views/{n}.png','box':b,'scale':s,'contrast':c,'rotation_degrees':r,'purpose':p})
report={'scan':67,'reader':'GPT-6 Astra Pro; effort not exposed; run /root/scan067_a','started_utc':'2026-11-20 04:46:45 UTC','finished_utc':'2026-11-20 04:50:51 UTC','rows':rows,'views':views,'other_errors':[],'patterns':[{'name':'Compressed p-bearing word','marks':['M1310'],'description':'The local propres has two uneven descents and a long low final join; it was compared only to the visible earlier propres on this same page.'}],'notes':['All current page mark boundaries were read before considering outside errors; no unmarked corrections proposed.','M1309 requires independent factor/parenthesis review. M1294 carries a separate red Ajout overlay; no added lexical reading was forced into its marked black-text alternatives.','M1306–M1308 remain damaged; retained word counts and component proposals are not verified. Their broad boxes preserve all candidate ink rather than implying exact segmentation under the cancellation.','Initial own-ink interval ends at the actual clock check immediately following final inspected views. Subsequent report serialization is text-only annotation work.','The inverted first margin view is included because it was actually inspected. All 50 crop images and the source page were viewed.']}
assert [r['id'] for r in rows]==[f'M{i:04d}' for i in range(1294,1311)]
assert len(views)==51
for p in ('work/scan067_a.json','work/scan067_a_initial.json'):
 (base/p).write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
from collections import Counter
print('work/scan067_a.json',dict(Counter(r['decision'] for r in rows)),len(views))
