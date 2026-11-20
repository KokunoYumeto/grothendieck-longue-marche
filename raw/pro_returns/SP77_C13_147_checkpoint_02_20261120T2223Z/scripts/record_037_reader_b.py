from pathlib import Path
import json
base=Path('/workspace/scratch/88012a0a2bcc/SP77_C13_147_work')
C=Path('/workspace/scratch/88012a0a2bcc/inputs/SP77_C13_147_texts/pages/147_scan037.tex').read_text()
draft=C.replace(r'\unsure{\to|{-}}', '-').replace(r'$\forall$ flèche', 'tt flèche').replace(r'\unsure{définie|défini}',r'\unsure{défini|définie}')
(base/'drafts/147_scan037.tex').write_text(draft)
specs=[
('01_topformula',[285,155,1095,287]),('02_piG',[280,430,650,565]),('03_arcG',[1090,404,1668,542]),
('04_appelant',[565,685,1460,825]),('05_elementaryclause',[260,850,1675,1000]),('06_insertion',[1220,920,1485,1010]),
('07_arc',[260,1000,975,1135]),('08_ellipsis',[690,1120,1280,1245]),('09_plural',[655,1250,1240,1405]),
('10_pluralG',[1300,1245,1668,1400]),('11_twoPi',[1010,1390,1680,1535]),('12_fls',[810,1560,1465,1695]),
('13_singular',[275,2165,935,2320]),('14_lastformula',[940,2170,1300,2290]),('15_definie',[1290,2170,1650,2300]),('16_footer',[17,2295,105,2350])]
sp=dict(specs)
def cp(n): return f'crops/147_scan037_{n}.jpg'
changes=[]
def ch(place,c,h,f,n,kind,category,evidence,diffc=False,conf='high',conseq=False):
 changes.append(dict(id=f'037-{len(changes)+1:02d}',place=place,C=c,H=h,final=f,diff_C=diffc,diff_H=True,kind=kind,evidence=evidence,crop=cp(n),box=sp[n],confidence=conf,consequential=conseq,error_category=category))
gcancel=r"G^{\deleted{\unsure{'}}}"
ch('line 2, relation between the two groupoids',r'\unsure{\to|{-}}',r'\to','-','01_topformula','misread symbol or index','Symbols and indices','The relation is one level horizontal stroke. Its right endpoint is slightly thickened but has neither an upper nor a lower arrowhead stroke. The complete formula and its adjacent symbols have been read.',True,conseq=True)
ch('line 2, target of the first groupoid formula',gcancel,"G''",gcancel,'01_topformula','deletion state','Struck text','Immediately above and to the right of the target G is a dark overworked hook, distinct from the single clean source prime. It cannot be read as two separate live primes. C’s cancelled, uncertain underlying prime is retained; its exact original stroke is not recovered.',conf='medium',conseq=True)
ch('line 4, groupoid after en une flèche de',r'\Pi_1(G)',r"\Pi_1(G'')",r'\Pi_1(G)','02_piG','misread symbol or index','Symbols and indices','Between G and the closing parenthesis there is clear blank paper. The small downward feature belongs to the upper end of G itself, not to a separate prime. The lowered 1 is present.',conseq=True)
ch('line 4, un arc de target graph',gcancel,"G''",gcancel,'03_arcG','deletion state','Struck text','The raised sign after G is an angular zigzag with crossing/retracing, not two parallel prime strokes. The erased short superscript remains tentatively a prime, as in C.',conf='medium',conseq=True)
ch('line 6, verb introducing flèche élémentaire','appelant','notant','appelant','04_appelant','misread word','Words','The word has the two long descending strokes of pp, followed by the looped l and the compressed ending ant; it is appreciably longer than notant.')
ch('line 6, underlined noun','flèche','flèches','flèche','04_appelant','misread word','Words','The underlined noun ends at the low rightward e stroke before the gap. There is no separate final s.')
ch('line 6, underlined adjective','élémentaire','élémentaires','élémentaire','04_appelant','misread word','Words','The adjective ends with the small terminal e-shaped rise and horizontal finish. No additional s follows before de on the main line.')
ch('line 7, abbreviated quantifying expression',r'$\forall$ flèche','les flèches','tt flèche','05_elementaryclause','abbreviation expanded or spelling modernised','Abbreviations expanded, spelling modernised','The short sign has two joined t stems and a hooked common cross stroke; it is the double-t abbreviation. The following word is singular flèche with no final s. This local shape agrees with the tt habit supplied in the notation snapshot.',True)
ch('line 7, verb after qui','est','sont','est','05_elementaryclause','misread word','Words','The compressed verb starts with a low e-shaped stroke and ends in the angular crossed t; it lacks the initial s and medial n needed for sont.')
ch('line 7, adjective after soit','identique','identiques','identique','05_elementaryclause','misread word','Words','The word finishes at a low e stroke and the comma. There is no intervening s.')
ch('line 8, soit un arc de G prime','arc',r'\struck{arc} arc','arc','07_arc','text not on the page','Text that is not on the page','There is one connected arc between un and de. Its initial a and final c are locally retraced, but there is no second word, no separate cancelled arc, and no cancellation stroke crossing a second group.')
plural=r'\deleted{\unsure{générisation}}\inserted{\unsure{généralisés}}'
ch('line 10, overwritten designation after morphismes',plural,'générisation',plural,'09_plural','deletion state','Struck text','After the struck de, the word has old low strokes and a newer tall l with raised strokes over its ending. The corrected reading généralisés is probable, but overlap prevents full recovery of both old and new letter sequences. The visible alteration is absent from H’s live générisation.',conf='medium',conseq=True)
ch('line 10, target graph after de G prime dans',gcancel,"G''",gcancel,'10_pluralG','deletion state','Struck text','The source prime is a clean long slanted stroke; the target superscript is instead a compact series of overlapping loops/zigzags. The latter is cancelled ink, with the underlying prime still uncertain.',conf='medium',conseq=True)
ch('line 11, final groupoid after dans',r'\Pi_1(G)',r"\Pi_1(G'')",r'\Pi_1(G)','11_twoPi','misread symbol or index','Symbols and indices','The source G prime has a clearly isolated raised prime. The target G is followed directly by the parenthesis with no intervening raised stroke. Both groupoids have a lowered 1.',conseq=True)
ch('line 12, object of transforment','fls','flèches','fls','12_fls','abbreviation expanded or spelling modernised','Abbreviations expanded, spelling modernised','The word consists of tall joined f/l followed immediately by a short baseline s. There are no written èche letters to expand.')
singular=r'\deleted{\unsure{générisation}}\inserted{\unsure{généralisé}}'
ch('line 17, overwritten designation after morphisme',singular,'générisation',singular,'13_singular','deletion state','Struck text','The old word’s low final strokes are overwritten by a tall looped l and raised i/s/é-like strokes. Généralisé is the likely replacement, but the superposed strokes do not allow every letter of either layer to be certified. H leaves the original candidate as live text.',conf='medium',conseq=True)
ch('line 17, target of final map',gcancel,"G''",gcancel,'14_lastformula','deletion state','Struck text','The final target has a crossed zigzag in the superscript position. It contrasts with the clean source prime at the left. Two live primes are not visible; the underlying cancelled prime remains doubtful.',conf='medium',conseq=True)
ch('lower left footer',r'\mspage{36}','[absent]',r'\mspage{36}','16_footer','omission','Omissions','The faint footer consists of the two open right lobes of 3 followed by a top-curved descending 6 with a closed lower bowl. It is the handwritten number 36, not the editorial scan label.')

def decision(id,dec,reading,n,evidence,conf):
 return {'id':id,'cote':'147','scan':'37','decision':dec,'reading':reading,'what the ink shows':evidence,'crop':cp(n)+' ('+','.join(map(str,sp[n]))+')','confidence':conf}
decisions=[
 decision('M0967','alternative','-','01_topformula','Only a horizontal shaft is visible, with a rounded/thickened right endpoint but no arrowhead. The whole formula was inspected.','high'),
 decision('M0968','undecided',r'\unsure{généralisés}','09_plural','The replacement has a conspicuous tall l and raised ending over the older word. Généralisés is probable, but overlapping old and new strokes leave the middle and plural ending incompletely separable.','medium'),
 decision('M0969','undecided',r'\unsure{généralisé}','13_singular','New looped l and raised final strokes support généralisé. The overwritten segment still prevents a letter-by-letter certification.','medium'),
 decision('M0970','undecided',r'\unsure{défini|définie}','15_definie','After the tall f, two dots accompany low compressed strokes. The final hook has no distinct e loop; défini is visually preferable, but an extremely compressed terminal e cannot be excluded. Agreement with donnée has not supplied an e.','medium')]
supp=[]
for label,n,reading,ev in [
 ('U037-01','01_topformula',r"\deleted{\unsure{'}}",'The superscript is dark and overworked; the original prime stroke cannot be isolated.'),
 ('U037-02','03_arcG',r"\deleted{\unsure{'}}",'A raised zigzag crosses/retraces the short superscript; a single original prime is plausible but not fully recoverable.'),
 ('U037-03','09_plural',r'\deleted{\unsure{générisation}}','The earlier word is overlapped by the corrected middle and ending; not every letter of générisation survives distinctly.'),
 ('U037-04','10_pluralG',r"\deleted{\unsure{'}}",'Several compact overlapping loops obscure the target superscript; the underlying prime is still tentative.'),
 ('U037-05','13_singular',r'\deleted{\unsure{générisation}}','The old middle and ending are entangled with the new raised strokes; generating the complete old word would require inference.'),
 ('U037-06','13_singular',r'\deleted{\unsure{de}}','The short crossed group before G prime has a surviving rising loop and low strokes consistent with de, but the heavy diagonal/horizontal cancellation hides the whole sequence.'),
 ('U037-07','14_lastformula',r"\deleted{\unsure{'}}",'The superscript is a compact crossed mark; the original prime is not independently clear.')]:
 supp.append(decision(label,'undecided',reading,n,ev,'medium'))

boxes=[]
def bx(n,kind,reading,coords=None):
 q=coords or sp[n]
 boxes.append(dict(box=f'037-B{len(boxes)+1:02d}',kind=kind,x0=q[0],y0=q[1],x1=q[2],y1=q[3],reading=reading))
bx('01_topformula','full doubtful formula; two handwritten subscripts 1; cancelled superscript',r"$\Pi_1(G')-\Pi_1(G^{\deleted{\unsure{'}}})$")
bx('02_piG','handwritten subscript 1; disputed target',r'$\Pi_1(G)$')
bx('03_arcG','cancelled superscript; disputed target',r"un arc de $G^{\deleted{\unsure{'}}}$")
bx('04_appelant','three disputed words; underline',r'appelant \uline{flèche élémentaire}')
bx('05_elementaryclause','handwritten subscript 1; abbreviated quantifier; disputed singular words',r"$\Pi_1(G')$ tt flèche qui est, soit identique,",[260,850,1675,1000])
bx('06_insertion','interlinear insertion',r'\inserted{de flèches}')
bx('07_arc','disputed cancellation state',r"soit un arc de $G'$")
bx('09_plural','struck word; overwritten word and replacement',r'\deleted{de} '+plural+' de')
bx('10_pluralG','cancelled superscript; disputed target',r"$G'$ dans $G^{\deleted{\unsure{'}}}$")
bx('11_twoPi','two handwritten subscripts 1; disputed target',r"$\Pi_1(G')$ dans $\Pi_1(G)$")
bx('12_fls','disputed abbreviated word','fls élémentaires',[810,1560,1380,1695])
bx('13_singular','struck words; overwritten word and replacement',r'\deleted{de} '+singular+r' \deleted{\unsure{de}}')
bx('14_lastformula','full doubtful formula; cancelled superscript',r"$G'\longrightarrow G^{\deleted{\unsure{'}}}$")
bx('15_definie','unresolved word ending',r'est \unsure{défini|définie}')
bx('16_footer','handwritten page number',r'\mspage{36}')

inventory=[]
def inv(kind,pos,words):
 inventory.append(dict(scan=37,sheet_kind='text',hand='his hand',element=f'037-E{len(inventory)+1:02d}',kind=kind,position=pos,first_words_or_objects=words,transcribed='yes'))
inv('text','main text, lines 1–15','comme étant les morphismes de groupoïdes; ends stable par composition.')
inv('deletion','line 2, target superscript','cancelled uncertain prime after the target G')
inv('deletion','line 4, target graph after un arc de','cancelled uncertain prime')
inv('insertion','interline above stable par, attached after ensemble','de flèches')
inv('deletion','line 10, after morphismes','de and the overwritten candidate générisation')
inv('insertion','line 10, over the ending of the old designation','uncertain replacement généralisés')
inv('deletion','line 10, target graph after dans','cancelled uncertain prime')
inv('text','bottom paragraph, lines 16–17',"Pratiquement, la donnée d'un morphisme ... est défini(e)")
inv('deletion','line 17, around the overwritten designation','de; candidate générisation; uncertain de before G prime')
inv('insertion','line 17, over the ending of the old designation','uncertain replacement généralisé')
inv('deletion','line 17, final target superscript','cancelled uncertain prime')
inv('text','bottom-left footer','36')

doubts=[]
def doubt(place,reading,alts,reason,conf='medium'):
 doubts.append(dict(place=place,reading=reading,alternatives=alts,confidence=conf,reason=reason))
for place,n in [('line 2 target','01_topformula'),('line 4 target after un arc de','03_arcG'),('line 10 target after dans','10_pluralG'),('line 17 final target','14_lastformula')]:
 doubt(place,gcancel,'underlying prime; exact earlier superscript unrecovered','The cancellation/overworking is visible, but its short underlying stroke is not separable. The crop '+cp(n)+' does not support H’s two clean live primes.')
doubt('line 10 overwritten designation',plural,'probable générisation → généralisés; exact letter layers unresolved','Visible corrected middle/ending; both old text and replacement remain tentative because the strokes overlap.')
doubt('line 17 overwritten designation',singular,'probable générisation → généralisé; exact letter layers unresolved','Visible correction, but old and new middle/ending cannot be fully separated.')
doubt('line 17 cancelled word before G prime',r'\deleted{\unsure{de}}','de; obscured short word','Heavy crossing obscures the letter sequence; retaining C’s uncertainty rather than certifying H’s de.')
doubt('line 17 final word',r'\unsure{défini|définie}','défini | définie','The ending has no independently identifiable final e. The visually preferred reading is moved first, but both C alternatives remain. This is a change in preference/certainty only, not a separate substantive collation row.')

record=dict(scan=37,reader='reader_b',line_count=19,changes=changes,decisions=decisions,supplemental_unindexed_C_doubts=supp,inventory=inventory,boxes=boxes,doubts=doubts,
 notation=[
 {'form':r'\Pi_1(G)', 'meaning':'Groupoid associated with the graph G in the author’s discussion.', 'evidence':'Six Π symbols with lowered 1 on lines 2, 4, 7 and 11.', 'scope':'All six subscript-1 occurrences on scan 037 were visually checked; the source and target letters are not regularised.'},
 {'form':'tt','meaning':'Abbreviation for tout/toute, here before flèche.', 'evidence':'Line 7, joined double-t form with hooked common cross stroke.', 'scope':'This one occurrence is confirmed locally; notation snapshot supplied the same habit from scan 034.'},
 {'form':'-','meaning':'Literal horizontal relation stroke in the first morphism formula.', 'evidence':'Line 2, complete formula crop 01_topformula.', 'scope':'Only this top relation lacks an arrowhead; the bottom map retains its visible right-hand head.'}
 ],
 abbreviations=[{'form':'tt','expansion':'toute (contextual; written abbreviation retained)'},{'form':'fls','expansion':'flèches'},{'form':'fl.','expansion':'flèches'}],
 hand_log=[
 {'habit':'Joined double-t abbreviation can resemble a universal quantifier.', 'pages':'037','scope':'The single tt before flèche, checked locally.','misread_places':r'C $\forall$ and H les flèches on line 7.'},
 {'habit':'A cancelled small superscript is compactly retraced into a zigzag/looped blot.', 'pages':'037','scope':'All four target-graph superscripts on this page; the exact underlying prime remains tentative.','misread_places':'H reads G double-prime at all four cancelled positions.'},
 {'habit':'Word endings are flattened to horizontal strokes, so a grammatical ending is not guaranteed.', 'pages':'037','scope':'The final défini/définie remains unresolved; singular flèche, élémentaire and identique were individually checked.','misread_places':'H pluralises the definition phrase and certifies définie.'},
 {'habit':'The numeral 1 in Π subscript is a short slanted downstroke distinct from a prime above G.', 'pages':'037','scope':'All six Π subscripts on this sheet.','misread_places':'No differing 1 reading; all included in blind boxes.'}
 ],
 notes=[
 {'id':'147-037-N01','text':'The page continues the description of graph morphisms through morphisms of the associated groupoids. The author calls identities and graph arcs elementary arrows, states preservation of elementary arrows, and says this makes stability under composition evident. The designation is visibly revised from a candidate générisation to probable généralisés/généralisé, but both superposed letter layers remain uncertain. The last paragraph begins a practical description of the data and breaks off after the uncertain défini/définie. Handwritten footer: 36; editorial scan identifier: 37. No diagram or margin prose occurs.'},
 {'id':'147-037-N02','text':'The first displayed-in-line relation is retained as the literal horizontal stroke - because the crop contains no arrowhead; its morphism context is not used to add one. Four target superscripts are overworked/cancelled, whereas two other target groupoids have plainly bare G. H’s uniform G double-prime is therefore not adopted. The last word is left uncertain with défini first because no distinct final e can be separated from the terminal hook; the feminine subject does not settle the ink.'}
 ],
 check_events=[{'statement_id':'147-037-N01','date':'2026-11-20','who':'GPT-6 Astra Pro; inherited effort; SP77_C13_147 reader_b','type':'carried as background without fault found','outcome':'Reading only, no proof claim. The author’s assertion of compositional stability was recorded; no mathematical proof verification was performed.'}],
 coverage={'whole_viewed':True,'halves_viewed':['top','bottom'],'all_tokens_read':True,'all_deletions_insertions_checked':True,'differences_accounted':'All 18 packet rows were examined. Editorial scan 37 is metadata; C \\ldots and H … encode the same visible three dots; underline/emphasis, struck/deleted and inserted/add macros are syntax equivalents. The four MARKS entries are in packet order, with seven nested unindexed C doubts in the supplemental array. Eighteen substantive collation rows cover every actual differing place, including the double-t form not exposed by the token packet and the handwritten footer. Reordering the retained final-word alternatives is reported in doubts only. All 16 saved crops were inspected. Nineteen physical lines comprise 17 principal text/formula lines, the interlinear de flèches, and the footer.'},
 unresolved=['Four cancelled target superscripts: the cancellation/overworking is visible, but underlying primes remain tentative.','Plural and singular overwritten designations: générisation and généralisés/généralisé remain uncertain as superposed letter sequences.','Cancelled de before the final map remains uncertain.','Final défini/définie remains unresolved, with défini visually preferred.','Main visual review and independent blind second reading are pending.'],
 crop_files=[cp(n) for n,_ in specs])
(base/'records/147_scan037.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print('draft:',base/'drafts/147_scan037.tex')
print('record:',base/'records/147_scan037.json')
print('changes',len(changes),'decisions',len(decisions),'supplemental',len(supp),'boxes',len(boxes),'crops',len(specs),'lines',record['line_count'])
