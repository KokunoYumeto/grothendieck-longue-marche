from pathlib import Path
import csv,json
r=Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work')
out=r/'edition/reader_reports'
tex=r'''\scanpage{7}
\mspage{2}
$\tau$, dont l'opération sur $\unsure{\pi_{0,3}|\Pi_{0,3}}$ peut se décrire par
\[
\tau(l_0)=l_0^{-1},\quad\tau(l_1)=l_1^{-1},\quad\tau(l_\infty)=l_1l_0=\operatorname{int}(l_1)l_\infty^{-1}
\]
C'est donc un autom du groupe à lacets, de signature $-1$, satisfaisant
\[
\tau^2=1
\]
On vérifie qu'il commute à l'action de $\unsure{\mathfrak S_3|\mathcal S_3}$ mod autom extérieurs --- ce qui donne une op. extérieure de $\unsure{\mathfrak S_3|\mathcal S_3}\times\{\pm1\}=\Gamma_{0,3}$, qui n'est autre que l'action canonique.

On s'intéresse maintenant aux autom extérieurs qui commutent à $\rho$. Notons que tout autom extérieur \inserted{qui normalise la classe de conj. de $l_0$} provient d'un autom $u$ qui normalise \deleted{\unsure{un}} $L_0$ ($\simeq\hat{\mathbb Z}$ engendré par $l_0$) et $u$ est unique mod composition par un $\lambda\in L_0$. Si $p$ \inserted{$=\chi(u)$,} $\in\hat{\mathbb Z}^{*}$ \deleted{\unsure{est}} est le multiplicateur de $u$, on aura donc
\[
(*)\qquad u(l_0)=l_0^p
\]
Soit $g\in\pi$ tel que :
\[
(**)\qquad u\rho=\deleted{\rho u}\operatorname{int}(g)\rho u,
\]
ce qui détermine $g$ de façon unique, $u$ étant
\mspage{6}
'''
(out/'145_scan007.tex').write_text(tex)
boxes=json.loads((r/'edition/crops/145_scan007_crop_boxes.json').read_text())
def loc(n):
 k=next(k for k in boxes if k.startswith(f'145_scan007_{n:02d}_'))
 return {'crop':'crops/'+k+'.png','box':boxes[k]}
changes=[]
def ch(i,place,C,H,final,ink,confidence,kind,c,h,n,cat,math='',marked='no'):
 d=dict(id=f's007-{i:02d}',place=place,C=C,H=H,final=final,ink=ink,confidence=confidence,kind=kind,c_changed=c,h_changed=h,marked_in_H=marked,error_category=cat,math_consequence=math)
 d.update(loc(n));changes.append(d)
ch(1,"C'est donc un autom",'autom','autom.','autom','The short word ends in a low m and is followed by a clear blank before du. No terminal stop is written. The small incidental points away from the baseline are not punctuation.','high','text not on the page',False,True,2,[9,8])
ch(2,'de … -1, satisfaisant','signature',r'\uncertain{multiplicateur}','signature','The initial s-i is followed by a conspicuous descending g loop, then n-a, a tall t, and the low ure ending. This cannot be multiplicateur. The following sign is a minus and the digit is 1.','high','misread word',False,True,2,[2],marked='yes')
ch(3,'after the first symmetric-group symbol','mod. autom','mod autom.','mod autom','The low m, separated o-like point and small upright d form mod; there is no stop after d. The following autom also ends without a stop. Thus C adds a stop after mod and H adds one after autom.','high','text not on the page',True,True,3,[9,8])
ch(4,"On s'intéresse maintenant aux autom",'autom','autom.','autom','At the right end of the line the final m ends in a low curved stroke. The space after it contains no terminal full stop.','high','text not on the page',False,True,5,[9,8])
ch(5,'Notons que tout autom extérieur','autom','autom.','autom','Between the final low m of autom and the following ext- there is blank paper, not a stop. Both words are written on the lower main line beneath the added class-normalizing phrase.','high','text not on the page',False,True,6,[9,8])
ch(6,'class-normalizing phrase between two main prose lines',r"tout autom extérieur \inserted{qui normalise la classe de conj. de $l_0$} provient d'un autom",r"tout autom. extérieur provient d'un autom $u$ qui normalise $L_0$ ($=\hat{\mathbb Z}$ engendré par $l_0$) \marginal{qui normalise la classe de conj. de $l_0$}",r"tout autom extérieur \inserted{qui normalise la classe de conj. de $l_0$} provient d'un autom",'The smaller, darker phrase is between the line ending Notons que and the line beginning tout autom extérieur. Its left edge lies above the end of extérieur and its continuation spans the area above provient d’un autom. No insertion guide is visible. C’s attachment after extérieur is retained as the most direct placement; H’s marginal position after the L_0 parenthesis is not the physical placement.','medium','insertion or placement',False,True,6,[6],math='The phrase specifies the exterior automorphism whose representative is being chosen.')
ch(7,'crossed word immediately before L_0',r'\deleted{\unsure{un}}',r'',r'\deleted{\unsure{un}}','A small crossed cluster stands before the capital L. Low u/n-like curves survive below and through the heavy horizontal stroke, but not every original letter is plain. The cluster must be transcribed as deleted and its uncertainty retained.','medium','omission',False,True,7,[3,7])
ch(8,'parenthetical description of L_0',r'\simeq\hat{\mathbb Z}',r'=\hat{\mathbb{Z}}',r'\simeq\hat{\mathbb Z}','The upper component of the relation bends up and down as a tilde, and a separate straight short bar lies below it. It is not two straight equals strokes. The hat over Z is visible.','high','misread symbol or index',False,True,7,[1],math='The manuscript uses an isomorphism sign, not an equality sign.')
ch(9,'u est unique … par','mod composition','mod. conjugaison','mod composition','After the unpunctuated mod, the word has a long descending p after com, then a small round o, dotted i, and a conspicuous tall t in the later part. Those strokes support composition; there is no descending g of conjugaison. No stop follows mod.','high','misread word',False,True,8,[2,9])
ch(10,'added character value above p in the multiplier sentence',r'Si $p$ \inserted{$=\chi(u)$}, $\in\hat{\mathbb Z}^{*}$',r'Si $p\in\hat{\mathbb{Z}}^{*}$ \marginal{$=\chi(u)$,}',r'Si $p$ \inserted{$=\chi(u)$,} $\in\hat{\mathbb Z}^{*}$','The equality =chi(u) is above the main line. A long curved guide starts directly after p and before the membership sign. A small comma-like stroke lies at the upper-line right edge, separated from the lower membership expression; it is included within the addition. The guide’s upper endpoint and this small comma are close, so their separation merits root review.','medium','insertion or placement',True,True,9,[6],math='The addition identifies p with chi(u); it attaches before the membership statement.')
ch(11,'after Soit g in pi tel que',' :',r'',r' :','Two dark, separated points occupy the normal end-of-clause position after que, before the following display. Their paired placement is a colon, unlike isolated paper specks.','high','omission',False,True,10,[3])
ch(12,'end of final prose line',r'$u$ étant',r'\uncertain{u} \uncertain{étant}\n\ill{}',r'$u$ étant','The last visible words are a low u followed by étant, whose tall strokes and final rightward t are present. After the final word there is blank paper; no additional unreadable word or character block appears. H’s illegibility placeholder has no source ink.','high','text not on the page',False,True,11,[9])
ch(13,'bottom-left source number',r'\mspage{6}',r'',r'\mspage{6}','The lower-left margin contains a plainly looped 6, with an open upper entry and closed lower bowl. H’s editorial page marker is not a transcription of this physical footer.','high','omission',False,True,11,[3])

decisions=[]
for id,n,read in [('M0780',3,r'\unsure{\mathfrak S_3|\mathcal S_3}'),('M0781',4,r'\unsure{\mathfrak S_3|\mathcal S_3}')]:
 d=dict(id=id,decision='undecided',reading=read,ink='The large rounded S-like sign has an outer curved stroke, a rising top-right hook and an inward lower curve. The digit 3 is visible. The strokes do not securely distinguish the calligraphic from the Fraktur alphabet on this page.',confidence='medium');d.update(loc(n));decisions.append(d)
doubts=[
 {'place':'indexed group symbol in the opening sentence','reading':r'\unsure{\pi_{0,3}|\Pi_{0,3}}','alternatives':[r'\pi_{0,3}',r'\Pi_{0,3}'],'confidence':'medium','reason':'The horizontal head and two upright stems are clear; the second stem curves slightly at its foot. C gives pi and H gives Pi. Case cannot be securely inferred from graphic height alone. The index 0,3 remains as in both witnesses.'},
 {'place':'first symmetric-group symbol','reading':r'\unsure{\mathfrak S_3|\mathcal S_3}','alternatives':[r'\mathfrak S_3',r'\mathcal S_3'],'confidence':'medium','reason':'The rounded S-like form does not by itself settle the typographic alphabet; retain M0780.'},
 {'place':'symmetric-group symbol in the product defining Gamma_0,3','reading':r'\unsure{\mathfrak S_3|\mathcal S_3}','alternatives':[r'\mathfrak S_3',r'\mathcal S_3'],'confidence':'medium','reason':'Same local graphic form as the earlier symbol; the whole product formula was read in its crop, but the alphabet remains unresolved.'},
 {'place':'crossed word before L_0','reading':r'\deleted{\unsure{un}}','alternatives':['un','unresolved crossed short word'],'confidence':'low','reason':'The heavy strike obscures the original low letter strokes. The reading un remains plausible but is not plain letter for letter.'},
 {'place':'crossed word before live est le multiplicateur','reading':r'\deleted{\unsure{est}}','alternatives':['est','unresolved crossed short word'],'confidence':'low','reason':'A dense short cancellation precedes the legible live est. Individual original e/s/t strokes cannot all be separated confidently; C’s nested doubt is retained.'},
 {'place':'small upper-line stroke following the inserted =chi(u)','reading':r'\inserted{$=\chi(u)$,}','alternatives':[r'\inserted{$=\chi(u)$,}',r'\inserted{$=\chi(u)$}'],'confidence':'medium','reason':'Both witnesses read a comma. A comma-like stroke is visible just above the right endpoint of the curved insertion guide. Their near contact leaves a genuine placement/status question for root review; the proposed reading retains the comma within the upper-line addition.'}
]
inv=[]
def it(i,kind,pos,txt,b):inv.append(dict(element=f'007-{i:02d}',kind=kind,position=pos,first_words_or_objects=txt,box=b,sheet_kind='text',hand='his hand',transcribed='yes'))
it(1,'margin note','top centre','2',[806,22,855,69])
it(2,'text','opening two lines',r"tau, dont l’opération sur pi_0,3 peut se décrire par",[271,82,1563,255])
it(3,'display','first formula row',r'\tau(l_0)=l_0^{-1},\tau(l_1)=l_1^{-1},\tau(l_\infty)=l_1l_0=\operatorname{int}(l_1)l_\infty^{-1}',[503,259,1631,371])
it(4,'text','two lines below first display',"C’est donc un autom du groupe à lacets, de signature -1, satisfaisant",[277,391,1520,584])
it(5,'display','below signature paragraph',r'\tau^2=1',[638,582,814,649])
it(6,'text','four-line canonical-action paragraph',"On vérifie qu’il commute",[236,682,1634,1109])
it(7,'text','seven main lines leading to the first starred display',"On s’intéresse maintenant aux autom",[211,1140,1649,1895])
it(8,'insertion','between the Notons que and tout autom lines',r'qui normalise la classe de conj. de l_0',[816,1297,1570,1379])
it(9,'deletion','immediately before L_0',r'\unsure{un}',[826,1484,878,1519])
it(10,'insertion','above p and its membership statement',r'=\chi(u),',[874,1634,1016,1710])
it(11,'deletion','before live est le multiplicateur',r'\unsure{est}',[1082,1717,1137,1766])
it(12,'display','first left-starred formula',r'(*)\quad u(l_0)=l_0^p',[220,1905,889,1996])
it(13,'text','line before double-starred formula',r'Soit g\in\pi tel que :',[202,2010,928,2124])
it(14,'display','double-starred formula',r'(**)\quad u\rho=\deleted{\rho u}\operatorname{int}(g)\rho u,',[291,2114,1222,2215])
it(15,'deletion','after equals in double-starred formula',r'\rho u',[797,2140,872,2209])
it(16,'text','final line',r'ce qui détermine g de façon unique, u étant',[207,2228,1586,2327])
it(17,'margin note','bottom left','6',[34,2277,74,2327])
second=[]
def sb(i,kind,b,reading):second.append(dict(box=f'B{i:02d}',kind=kind,coords=b,reading=reading))
sb(1,'handwritten page number',[806,22,855,69],r'\mspage{2}')
sb(2,'opening indexed group symbol and case doubt',[271,82,1563,255],r"$\tau$, dont l'opération sur $\unsure{\pi_{0,3}|\Pi_{0,3}}$ peut se décrire par")
sb(3,'complete numeric generator-action display, including all indices and exponents',[503,259,1631,371],r'\tau(l_0)=l_0^{-1},\quad\tau(l_1)=l_1^{-1},\quad\tau(l_\infty)=l_1l_0=\operatorname{int}(l_1)l_\infty^{-1}')
sb(4,'autom-stop and signature lexical disputes, with numeric sign -1',[275,383,1520,585],r"C'est donc un autom du groupe à lacets, de signature $-1$, satisfaisant")
sb(5,'complete numeric involution display',[638,582,814,649],r'\tau^2=1')
sb(6,'first C group-symbol doubt and abbreviation stops',[239,783,1137,885],r'$\unsure{\mathfrak S_3|\mathcal S_3}$ mod autom extérieurs')
sb(7,'whole product formula carrying C doubt, with all numeric indices',[936,867,1405,980],r'$\unsure{\mathfrak S_3|\mathcal S_3}\times\{\pm1\}=\Gamma_{0,3}$,')
sb(8,'terminal stop disagreement after aux autom',[1260,1133,1565,1240],r'autom')
sb(9,'class-normalizing insertion, its l_0 index and adjoining autom-stop dispute',[210,1264,1630,1467],r"extérieurs qui commutent à $\rho$. Notons que tout autom extérieur \inserted{qui normalise la classe de conj. de $l_0$} provient d'un autom")
sb(10,'crossed doubtful word and entire numeric L_0 description',[812,1440,1577,1587],r'\deleted{\unsure{un}} $L_0$ ($\simeq\hat{\mathbb Z}$ engendré par $l_0$)')
sb(11,'composition versus conjugaison and mod punctuation',[776,1570,1482,1675],r'mod composition par')
sb(12,'character insertion, cancelled est, numeric L_0 membership and full multiplier expression',[213,1638,1645,1800],r'un $\lambda\in L_0$. Si $p$ \inserted{$=\chi(u)$,} $\in\hat{\mathbb Z}^{*}$ \deleted{\unsure{est}} est le multiplicateur')
sb(13,'complete starred formula, including both zero indices and p exponent',[220,1905,889,1996],r'(*)\qquad u(l_0)=l_0^p')
sb(14,'clause with the colon omitted by H',[202,2010,928,2124],r'Soit $g\in\pi$ tel que :')
sb(15,'whole double-starred formula and its cancelled factors',[291,2114,1222,2215],r'(**)\qquad u\rho=\deleted{\rho u}\operatorname{int}(g)\rho u,')
sb(16,'last line, absence of extra illegible text and handwritten footer number',[33,2202,1630,2337],r'ce qui détermine $g$ de façon unique, $u$ étant\quad\mspage{6}')

rows=list(csv.DictReader((r/'packets/145_scan007/differences.tsv').open(),delimiter='\t'))
sub={5:1,6:2,8:3,9:3,12:4,13:5,14:6,15:6,16:9,17:10,18:10,19:11,22:12}
ex={1:'Scan number versus H editorial page marker; not source text.',2:'H’s note p. 2 de l’auteur is editorial. The visible top number 2 is transcribed using C’s mspage syntax.',3:'Juxtaposed l_1 l_0 versus LaTeX thinspace tokenization; the same product is present.',4:'The comma token comes from a LaTeX thinspace command, not source punctuation.',7:'C’s alphabet alternative versus H’s certainty only; retained as unresolved M0780 in decisions/doubts.',10:'ASCII triple-hyphen versus Unicode em dash; the manuscript has a horizontal dash.',11:'C’s alphabet alternative versus H’s certainty only; retained as unresolved M0781 in decisions/doubts.',20:'TeX semicolon-spacing command, not a manuscript semicolon.',21:'TeX thinspace command, not a manuscript comma.'}
coverage=[]
for i,row in enumerate(rows,1):
 if i in sub:
  d={'row':i,'status':'substantive','change_id':f's007-{sub[i]:02d}'}
  if i in (14,15):d['explanation']='These alignment rows arise from relocating the class-normalizing insertion. The deleted un and isomorphism sign within the displaced passage are additionally logged as s007-07 and s007-08.'
  if i==22:d['explanation']='H’s explanatory note is editorial and excluded. Its trailing illegibility placeholder is unsupported (s007-12), while the manuscript footer 6 is retained separately (s007-13).'
  coverage.append(d)
 else:coverage.append({'row':i,'status':'macro/editorial','explanation':ex[i]})
assert len(rows)==22
rep={
'scan':7,'reader':'/root/reader_b','lines_read':25,
'layout':'Portrait subject-note sheet, 1678 × 2363 pixels. A handwritten 2 stands at top centre and 6 at bottom left. The page starts mid-discussion with tau. It contains four independent displays: three generator images, tau squared, a single-starred formula and a double-starred formula. Two smaller interlinear additions occur in the lower paragraph; three cancellation loci occur before L_0, before est le multiplicateur and within the double-starred display. No independent prose margin note, drawing or diagram is present. The 25-line count includes the two page numbers and two interlinear lines; the overlapping halves were not counted twice.',
'changes':changes,'decisions':decisions,'doubts':doubts,'inventory':inv,'second_boxes':second,
'notation':[
 {'observation':r'Tau is defined by the three displayed generator images and satisfies tau^2=1.','places':['opening display','involution display'],'qualification':'These are the author’s formulas. Every written 0, 1, infinity and minus-one exponent was read; no group computation was performed.'},
 {'observation':r'The permutation-group name is an S-like rounded sign with subscript 3.','places':['mod autom extérieurs sentence','product with {±1} defining Gamma_0,3'],'qualification':'The local form recurs, but Fraktur versus calligraphic alphabet is unresolved at both C marks.'},
 {'observation':r'The relation before the hatted Z in the L_0 parenthesis is simeq.','places':['L_0 parenthesis'],'qualification':'The upper stroke is visibly wavy and the lower one straight; H’s equals sign is rejected locally.'},
 {'observation':r'Lower-case p names the multiplier and appears as the exponent in the single-starred display; the inserted equality gives p=chi(u).','places':['multiplier paragraph','single-starred display'],'qualification':'Do not read the Latin p exponent as rho. The rho in the double-starred formula has a longer descending stem and its locally repeated looped head.'},
 {'observation':r'int(g) is written without a separate multiplication dot in the double-starred expression.','places':['last display'],'qualification':'Juxtaposition is preserved. TeX spacing differences in H are not punctuation.'},
 {'observation':'The unindexed pi in Soit g in pi has the same broad head-and-two-stem family as the indexed opening symbol.','places':['opening sentence','Soit g line'],'qualification':'No global case convention is inferred; the indexed witness disagreement is left as a local doubt.'}
],
'hand':[
 {'habit':'The letters of mod are low and can be separated, with an o-like dot before a small upright d.','places':['first mod autom clause','mod composition clause'],'universal_on_this_page':'Both observed occurrences have this form and no terminal stop.','witness_misreadings':'C adds a stop to the first mod; H adds one to the second.'},
 {'habit':'The abbreviation autom can end without a full stop.','places':['C’est donc un autom','aux autom extérieurs','tout autom extérieur','d’un autom u','mod autom extérieurs'],'universal_on_this_page':'No terminal stop is visible at these occurrences.','witness_misreadings':'H adds stops at three lexical occurrences and after autom in the mod clause.'},
 {'habit':'The g in signature has a long low loop; the p and t in composition have distinct descending and ascending strokes.','places':['signature -1','mod composition'],'universal_on_this_page':'These two diagnostic words were each cropped; no general claim about all letters is made.','witness_misreadings':'H offers multiplicateur for signature and conjugaison for composition.'},
 {'habit':'An interlinear addition need not have an insertion guide.','places':['qui normalise la classe de conj. de l_0'],'universal_on_this_page':'This phrase has no guide; the p=chi(u) addition has a long curved guide.','witness_misreadings':'H places the first phrase as a marginal item after the L_0 parenthesis, although its physical position is above the main tout autom line.'},
 {'habit':'Short prose cancellations obscure most of the original low-letter strokes.','places':['crossed un before L_0','crossed est before live est'],'universal_on_this_page':'Both remain uncertain; the longer-stemmed rho u cancellation is substantially clearer.','witness_misreadings':'H omits the first cancellation; neither witness’s certainty warrants clearing the second.'}
],
'abbreviations':[
 {'form':'autom','expansion':'automorphisme / automorphismes','place':'all autom occurrences on this sheet'},
 {'form':'mod','expansion':'modulo','place':'mod autom extérieurs; mod composition'},
 {'form':'op.','expansion':'opération','place':'une op. extérieure'},
 {'form':'conj.','expansion':'conjugaison','place':'class-normalizing interlinear phrase'},
 {'form':'int','expansion':'automorphisme intérieur','place':'first and last displays'}
],
'notes':[
 'The author describes the action of tau on the three generators and calls it an automorphism of the loop group of signature -1, satisfying tau^2=1. He states that it commutes with the permutation-group action “mod autom extérieurs”, and that this gives the canonical outer action of the product with {±1}, denoted Gamma_0,3. These assertions and the terminology extérieurs are transcribed without correction or verification.',
 'He then considers exterior automorphisms commuting with rho. An interlinear qualification says that the relevant exterior automorphism normalizes the conjugacy class of l_0. He chooses a representative u normalizing L_0, describes L_0 as isomorphic to the profinite integers generated by l_0, and states that u is unique “mod composition par un lambda in L_0”. The word composition is clear and is not changed to H’s conjugaison.',
 'The author introduces the multiplier p, with an added p=chi(u), writes u(l_0)=l_0^p, and introduces g through u rho=int(g) rho u after cancelling an earlier rho u immediately after the equals sign. The last line begins an explanation of the uniqueness of g and ends at u étant. No continuation is supplied.',
 'There is no date and no explicit authorial doubt phrase on this sheet. The top page number is 2 and the bottom-left number is 6. No authorial mathematical slip was established by this reading. No targeted proof, independent re-proof or computation was performed.',
 'The two supplied C marks M0780 and M0781 remain unresolved alphabet distinctions. The nested doubtful deletions un and est were both cropped and retained as uncertain because their original letters are not all plain. The separate mathematical deletion rho u was read in a whole-display crop: the rho head and long stem, followed by the small u, are visible beneath the cancellation.',
 'The class-normalizing phrase is physically between the Notons que line and the tout autom extérieur provient line, in smaller darker writing, with no visible guide. Its attachment after extérieur follows the most immediate local placement but should be reviewed as an insertion-location decision. The equality chi(u) has a guide that starts after p. Its small comma-like upper-line mark and the guide endpoint are close; the proposed comma stays with the added text rather than the main membership expression.',
 'H’s uncertainties for groupe and n’est autre do not require substantive change rows because the textual readings agree; those words were read on the image. H’s trailing illegibility placeholder corresponds to no further ink. The final line and lower margin are preserved in a shared adjudication crop.',
 'The whole image and the two supplied halves were each inspected once. Twelve distinct first-reading crops were made for witness disagreements, open readings and the mathematical cancellation. No OCR, external research, other scan packet or other reader report was consulted. No TeX compilation was run.'
],
'check_events':[],
'diff_coverage':coverage
}
assert all(x['c_changed'] or x['h_changed'] for x in changes)
for x in changes+decisions:assert (r/'edition'/x['crop']).is_file()
assert [x['row'] for x in coverage]==list(range(1,23))
assert all(x['sheet_kind']=='text' and x['hand']=='his hand' for x in inv)
(out/'145_scan007.json').write_text(json.dumps(rep,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'tex':str(out/'145_scan007.tex'),'json':str(out/'145_scan007.json'),'lines':25,'crops':len(boxes),'changes':len(changes),'C_mark_decisions':len(decisions),'doubts':len(doubts),'inventory':len(inv),'second_boxes':len(second),'diff_rows':len(coverage)}))
