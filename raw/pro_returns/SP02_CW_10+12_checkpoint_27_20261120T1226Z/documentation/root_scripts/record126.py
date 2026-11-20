from pathlib import Path
import sys,json
sys.path.insert(0,str(Path('SP02_CW_10+12/scripts').resolve()))
from root_record import Record
r=Record('B10-09',10,126);ch=r.change
def hd(body):
 return r'\handwritten{\begin{tikzpicture}[x=.4cm,y=.4cm,baseline=-.2ex]'+body+r'\end{tikzpicture}}'
def guide(n):
 return hd(r'\draw (0,-.45) .. controls (.06,-.08) and (.14,.17) .. (.42,.19)--('+str(n)+r',.18) .. controls ('+format(n+.2,'.2f')+r',.18) and ('+format(n+.35,'.2f')+r',.25) .. ('+format(n+.32,'.2f')+r',.43);')
gt=guide(1.4);ge=guide(1.8);gu=guide(5.8);gd=guide(1.1)
est=hd(r'\draw (0,-.12) .. controls (.04,-.01) and (.13,.18) .. (.27,.31);')
firstM=r'\rlap{(}M\mathrm{o}\rlap{\(\mathrm r\)}\mathrm{df}'
clipped=r'corresp\rlap{p}o\unsure{n|r}'
toutes=r'to\unsure{$\mathbb{u}$|u}tes'
admet=r'a\unsure{\rlap{s}d|\rlap{e}d}\rlap{t}met'
margin=r'[Dans le cas du nº 6, gr\uline{.dué}, on aura $\sigma=\pi^+\unsure{\ominus|\otimes}\pi^++\pi^+\otimes\pi^-+\pi^-\ominus\pi^+-\pi^-\ominus\pi^-$]'
r.edit(r'\unsure{cogitations|cohitations}',r'co\rlap{h}gitations')
r.edit(r'\deleted{\unsure{F}}',r'\deleted{F}')
r.edit(r'\unsure{\mathbb{M}|M}\mathrm{odf}',firstM)
r.edit(r'\unsure{correspond}',clipped)
r.edit('cf nº6',r'cf nº\handwritten{6}')
r.edit(r'une opération $\otimes$',r'une opération $\unsure{\otimes|\Omega}$')
r.edit(r'un\deleted{\unsure{e}}',r'un\deleted{e}')
r.edit(r'\inserted{\uline{toutes}}',r'\inserted{\uline{'+toutes+'}'+gt+'}')
r.edit('celles compatibles',r'celles c\rlap{i}ompatibles')
r.edit(r"qu'\unsure{illes|elles}",r"qu'\rlap{i}elles")
r.edit(r'[Dans le cas du nº 6, \uline{\unsure{gr. deux|gr. deu.}}, on aura $\sigma=\pi^+\otimes\pi^++\pi^+\otimes\pi^-+\pi^-\otimes\pi^+-\pi^-\otimes\pi^-$]',margin)
r.edit(r"\handwritten{\sigma'\sigma}",r"\handwritten{\sigma}'\handwritten{\sigma}")
r.edit(r"\handwritten{\sigma\sigma'}",r"\handwritten{\sigma\sigma}'")
r.edit(r"\handwritten{\sigma'}",r"\handwritten{\sigma}'",3)
r.edit(r"\handwritten{)'}",r"\handwritten{)}'")
r.edit(r'\text{ est supposé inversible)}',r'\text{ es'+est+r't supposé inversible)}')
r.edit(r'\handwritten{\leftrightarrow}',r'\handwritten{\mapsto}')
r.edit(r"\handwritten{\Delta'}",r"\handwritten{\Delta}'",4)
r.edit(r"\handwritten{'}","'")
r.edit(r'\inserted{\handwritten{en disant}}',r'\inserted{\handwritten{en disant}'+ge+'}')
r.edit(r'\inserted{i.e. $A$ admet une unité bilatère,}',r'\inserted{i.e. $A$ '+admet+' une unité bilatère,'+gu+'}')
oldcancel=r"\handwritten{\deleted{\unsure{\sigma}_1\unsure{\sigma}_2\unsure{\sigma}_3\unsure{\sigma'}_1\unsure{\sigma'}_2\unsure{\sigma'}_3=1\unsure{\sigma}}\quad(\mathrm{id}_U\widehat{\otimes}\Delta)(\sigma)\deleted{\unsure{\sigma^{23}\sigma^{12}|\sigma^{12}\sigma^{13}}}=\deleted{1}\sigma^{12}\sigma^{13}}"
newcancel=r"\deleted{\handwritten{\sigma}_1\handwritten{\sigma}_2\handwritten{\sigma}_3\handwritten{\sigma}'_1\handwritten{\sigma}'_2\handwritten{\sigma}'_3=1\handwritten{\unsure{\sigma}}}\quad\handwritten{(\mathrm{id}_U\widehat{\otimes}\Delta)(\sigma)\deleted{\sigma^{\unsure{23|13}}\sigma^{12}}=\deleted{1}\sigma^{12}\sigma^{13}}"
r.edit(oldcancel,newcancel)
r.edit(r'\inserted{\unsure{divers}}',r'\inserted{\unsure{divers}'+gd+'}')
r.edit(r'images de $\sigma$ dans $U\otimes U\otimes U$ par $x\otimes y\mapsto x\otimes y\otimes1$',r"images de $\sigma'$ dans $U\ominus U\ominus U$ par $x\ominus y\mapsto x\ominus y\ominus1$")
# Every C/H disagreement and every altered or retained C doubt has its own ink account.
ch('opening cogitations',r'\unsure{cogitations|cohitations}','cogitations',r'co\rlap{h}gitations','The third cell contains both the h ascender/shoulder and the g bowl with a descending loop. Both physical impressions are retained.','cog','misread word','high',True,True)
for place,crop in [('opening C est muni','C1'),('C in F:C','Fformula'),('C after unité de','unitpsiC')]:
 ch(place,'plain C','underlined C','plain C','The capital has an ordinary open curve and no detached lower rule.',''+crop,'misread symbol or index','high',False,True,False,True)
ch('deleted capital after fidèle',r'\deleted{\unsure{F}}','omitted',r'\deleted{F}','A tall upright and top/middle bars of F remain beneath crossing typewriter x strokes. The preceding cancellation strokes do not reveal another secure letter. C doubt resolved.','fidele','omission','high',True,True)
ch('first Modf initial',r'\unsure{\mathbb M|M}','plain M',r'\rlap{(}M','A long opening-parenthesis curve extends above and below the M, while the ordinary M stems remain visible. The extra curve is not a second M impression. C doubt resolved to physical overlap.','Modf; Mparen','misread symbol or index','high',True,True,False,True)
ch('first Modf d cell','d','d',r'\rlap{r}d','The d ascender and bowl coexist with an r upright, shoulder and low foot inside the same cell.','Modf; d-over','misread word','high',True,True)
ch('right-clipped word after et',r'\unsure{correspond}',r'correspon\supplied{dant}',clipped,'The image contains correspo followed by a partly clipped n/r-shaped cell; no final d is visible. The o also contains a separate p descender. Neither missing letters nor the grammatical ending are supplied.','clip','text not on the page','medium',True,True,True)
ch('ass un. punctuation','ass un.','ass. un.','ass un.','No dot stands between the last s and the following space; the dot after un is visible.','asscf','other','high',False,True)
ch('cf punctuation','cf','cf.','cf','The f is followed by space and nº, without a separate dot.','asscf','other','high',False,True)
ch('cross-reference number 6','unmarked 6','unmarked 6','handwritten 6','The numeral is a thin continuous loop/curve contrasting with the surrounding typewritten nº and punctuation.','asscf','other','medium',True,True)
ch('deleted wording after On','voit que la donnée d',"voit que la donnée d'",'voit que la donnée d, canceled','All words survive the x strikes; no detached apostrophe follows the final d.','cancelvoit','text not on the page','high',False,True)
ch('suppose donné','donné',r'donné\supplied{e}','donné','The accented é ends the word and is followed by a space. No e is supplied to repair agreement.','donne','abbreviation expanded or spelling modernised','high',False,True,True)
ch('un with canceled e',r'un\deleted{\unsure e}',r'un\struck e',r'un\deleted{e}','The upper curved body and middle bar of e are visible under its x strike. C doubt resolved.','une','misread word','high',True,False)
typed=[('operation','tensor1'),('diagonal U completed tensor U','diag'),('composition A tensor A','comp'),('symétrie psi pour','tensor4'),('display (0)','zero'),('automorphisme of U completed tensor U','tensor6'),('loi opposée','loi'),('unité bilatère pour','unitfirst'),('display (2), left tensor','twoleft'),('display (2), second tensor','twoleft'),('display (2), completed tensor','tworight'),('associativité ordinaire','Modf3tensor')]
for i,(place,crop) in enumerate(typed):
 ch('typed operator '+place,r'\otimes',r'\otimes',r'\unsure{\otimes|\Omega}' if i==0 else r'\otimes','The typed operator has a rounded high outer body with crossing internal strokes and a broad foot. Tensor is favored, with an Omega-shaped alternative registered at the first of these twelve occurrences; the remaining occurrences use that first candidate.',''+crop,'misread symbol or index','medium',i==0,True,False,True)
ch('inserted toutes u cell','toutes','toutes',toutes,'The u has distinct closely offset right uprights and faint inner upright traces. A repeated u strike is favored and encoded with mathbb; a single damaged u remains possible.','toutes; toutesu','misread word','medium',True,True)
ch('toutes underline','underlined toutes','no underline','underline retained','An independent line runs directly beneath the letters of the typed insertion.','toutes','other','high',False,True)
ch('toutes insertion guide','omitted','omitted','curved guide drawn','A separate hand line rises before les, passes beneath the inserted word and curls at the right.','toutes','drawing or diagram','high',True,True)
ch('pas seulement emphasis','underlined','italic','underlined','A lower straight rule spans both words.','passeul','other','high',False,True)
ch('compatibles after celles','compatibles','compatibles',r'c\rlap{i}ompatibles','The o cell contains an independent i dot, upright and lower foot as well as its closed oval.','compat','misread word','high',True,True)
ch("qu'illes/elles",r"qu'\unsure{illes|elles}","qu'elles",r"qu'\rlap{i}elles",'An i dot and vertical stem share the first vowel cell with an e loop and middle bar. Both layers are visible, resolving C\'s alternative-letter doubt.','illes','misread word','high',True,True)
ch('right marginal abbreviation',r'\uline{\unsure{gr. deux|gr. deu.}}','gradué',r'gr\uline{.dué}','The small word has g, r, a distinct period, then d-u-é with an acute accent. The underline begins under the period and extends through dué. It is neither deux nor a written-out gradué.','marginwords; marginword','abbreviation expanded or spelling modernised','high',True,True)
ch('right marginal brackets','square brackets','no brackets','square brackets retained','A large opening bracket and closing bracket enclose the two-line hand note.','marginfull','omission','high',False,True)
for i,crop in [(1,'mtensor1-corrected'),(3,'mtensor3'),(4,'mtensor4')]:
 ch('marginal operator '+str(i),r'\otimes',r'\otimes',r'\unsure{\ominus|\otimes}' if i==1 else r'\ominus','The outline is a circle/oval with a nearly horizontal inner bar; the latter two have a small right internal loop. A diagonal cross is not securely separable. Circled minus is the first ink candidate, tensor the alternative. The second marginal operator, which has a visible cross, remains otimes.','marginformula; '+crop,'misread symbol or index','medium',True,True,False,True)
ch('box around last equality of (1)','boxed equality','no box','hand-drawn box retained','Four irregular hand lines enclose the last equality and its pour tout clause.','box','drawing or diagram','high',False,True)
ch('small stroke within est in (1)','omitted','omitted','rising hand stroke drawn between s and t','A thin curved stroke rises from low at the right of s toward the middle of t. The typed est remains live and legible.','onelower','drawing or diagram','medium',True,True)
prime_loci=[('first sigma-prime sigma','oneupper'),('sigma-prime after et in (1)','oneupper'),('second sigma sigma-prime','onelower'),('prime after boxed closing parenthesis','box'),('Delta-prime after symétrique','dprime'),('Delta-prime defining equality','defining'),('prime after Delta(u)','defining'),('sigma-prime in relations entre','sigmas'),('Delta-prime after first transforme','transforme'),('sigma-prime before second transforme','transforme'),('Delta-prime after second transforme','transforme')]
for place,crop in prime_loci:
 ch('production of '+place,'prime enclosed in handwritten scope','unmarked prime','typed prime adjacent to handwritten Greek letter or parenthesis','The prime has a dense typewriter teardrop head and short tail matching the typed apostrophes, unlike the thin blue/grey hand letter. Its mathematical position is unchanged.',''+crop,'other','medium',True,False)
ch('symétrie tordue quotation marks','paired high double quotes','guillemets','paired high double quotes','Two short high strokes enclose each side of tordue; they are not angular guillemets.','symnote','other','high',False,True)
ch('symétrie tordue note punctuation','final period','no final period','final period retained','A small separate point follows diagonale in the upright enlargement.','symnote','other','high',False,True)
ch('arrow after stable sous',r'\leftrightarrow',r'\mapsto',r'\mapsto','The left end is a nearly vertical bent bar, with one right arrowhead. There is no separate left-pointing head.','stablearrow','misread symbol or index','high',True,False,False,True)
ch('opposée emphasis','underlined','italic','underlined','A separate rule lies below the word.','loi','other','high',False,True)
ch('en disant guide','omitted','omitted','curved guide drawn','The hand line rises at the insertion point before que, runs below en disant and curls upward at its right. The slanted insertion was viewed upright.','endisant; endisant-upright','drawing or diagram','high',True,True)
ch('admet in inserted unit clause','admet','admet',admet,'The d cell contains a second curved middle stroke favoring s/d, with e/d retained as an alternative. The m cell also contains a tall t ascender, crossbar and low return. The initial a has no securely separable extra letter.','unitinsert; admet','misread word','medium',True,True)
ch('typed unit insertion guide','omitted','omitted','long curved guide drawn','The hand line bends upward before alors and runs below the inserted unit clause, ending in an upward curl.','unitinsert','drawing or diagram','high',True,True)
ch('alors following unit insertion','live alors','canceled alors','live alors','The long insertion guide runs above the letter bodies; it does not cancel the typed word.','unitinsert','deletion state','high',False,True)
ch('sur before phi',r'\deleted{sur}','omitted',r'\deleted{sur}','All three typed letters remain under separate crossing x strikes.','surphi','omission','high',False,True)
ch('flattened typed operator after phi',r'\unsure{\otimes|\varpi}',r'\otimes',r'\unsure{\otimes|\varpi}','This distinct low glyph has a flattened outline with horizontal upper/lower traces and internal crossing strokes. The tensor candidate is favored, while varpi cannot be excluded. C doubt retained locally.','flat','misread symbol or index','medium',False,True,False,True)
for i in range(6):
 name=('sigma_'+str(i+1)) if i<3 else ('sigma-prime_'+str(i-2))
 ch('first cancellation of (3), '+name,'qualified '+name,'struck illegible',name+', canceled','The horizontal sigma bar and low loop survive the zigzag; the subscript '+str(i+1 if i<3 else i-2)+' is separately legible'+('; the raised prime is also visible.' if i>=3 else '.')+' C glyph doubt resolved without reconstructing an identity.','firstsigmas' if i<3 else 'firstsigmas; lastsigmas',r'readable ink left as \ill{}','medium',True,True,True)
ch('first cancellation typed scaffold','whole formula marked handwritten','struck illegible','typed indices 1,2,3,1,2,3, three primes, equals and 1; hand sigma letters','The serif numerals, dense primes and two straight equals strokes are typewritten and differ from the blue/grey hand sigma bars and loops. The cancellation crosses both layers.','firstsigmas; lastsigmas','other','high',True,True,True)
ch('last symbol of first cancellation',r'\unsure{\sigma}','struck illegible',r'\unsure{\sigma}, canceled','A horizontal bar and crowded lower loops favor sigma, but the heavy overlapping cancellation prevents complete separation. C doubt retained.','lastsigmas',r'readable ink left as \ill{}','low',False,True,True)
ch('second cancellation of (3)',r'\unsure{\sigma^{23}\sigma^{12}|\sigma^{12}\sigma^{13}}','struck illegible',r'\sigma^{\unsure{23|13}}\sigma^{12}, canceled','Both sigma loops/bars survive. The second raised pair is 12; the first ends in 3 and has an obscured leading digit, with 2 favored over 1. H\'s blank is replaced only as far as the visible strokes allow.','cancel2; cancel2full',r'readable ink left as \ill{}','low',True,True,True,True)
ch('deleted 1 after equals in (3)','deleted 1','omitted','deleted 1','The upright and foot of 1 are covered by a separate cancellation immediately after the equals sign.','rhs','omission','high',False,True)
ch('bottom divers insertion',r'\unsure{divers}','omitted',r'\unsure{divers}','The small rising word has a d-like initial loop, dotted i, v-shaped junction and an ers-like ending. It overlaps the cancellation above and remains qualified after upright enlargement.','divers; divers-upright','omission','medium',False,True)
ch('bottom divers insertion guide','omitted','omitted','curved guide drawn','A separate thin curve leaves the position after sigma-ij, runs under the small word and turns upward at the right.','divers-upright','drawing or diagram','high',True,True)
ch('sigma after images de',r'\sigma',r'\sigma',r"\sigma'",'A separate raised upright with a rounded head stands immediately after sigma. It is a prime, not ij; the following dans begins lower and farther right.','bottom-sigma; bottom-upright','misread symbol or index','high',True,True,False,True)
for place,crop in [('first U separator','bottom-triple'),('second U separator','bottom-triple'),('x/y on left of map','bottom-map'),('x/y on right of map','bottom-map'),('y/1 on right of map','bottom-map')]:
 ch('bottom annotation '+place,r'\otimes',r'\otimes',r'\ominus','The circle contains a nearly horizontal middle bar rather than a securely separated diagonal cross. It repeats the circled-bar form qualified as ominus/otimes at the first marginal occurrence; the same first candidate is used here.',''+crop,'misread symbol or index','medium',True,True,False,True)
ch('bottom abbreviation before analogues','appl.','types','appl.','The word has a, two descending p strokes, a tall looped l and a dot. The final analogues and its period are also visible at the page edge.','bottomwords2; bottom-upright','misread word','high',False,True)
# Local doubts, including image clipping, remain explicit.
r.doubt('right edge of opening paragraph',clipped,'final visible cell may be r rather than n; missing continuation unknown','medium','The last cell is cut by the black right border. No d or dant is supplied; the p/o overlap is visible before the clipped cell.')
r.doubt('toutes, u cell',r'\mathbb u','u','medium','Closely offset uprights favor a repeated typed strike, but a damaged single impression remains possible.')
r.doubt('twelve regular typed operators',r'\otimes',r'\Omega','medium','High rounded outer body with internal crossing strokes. First occurrence qualified, eleven repetitions use the first candidate; the separate flattened operator retains its own doubt.')
r.doubt('hand circled-bar operators',r'\ominus',r'\otimes','medium','First, third and fourth marginal operators and five bottom-annotation separators show circle plus horizontal bar; the second marginal and the hatted operator in (3) show a clearer cross and remain otimes.')
r.doubt('admet, d cell',r'\rlap{s}d',r'\rlap{e}d','medium','The additional middle curve is visible but does not uniquely distinguish the overlapping s/e layer.')
r.doubt('flattened operator after phi',r'\otimes',r'\varpi','medium','Low horizontal outline differs from the regular typed operators; C qualification retained.')
r.doubt('end of first canceled formula',r'\sigma','','low','The bar and lower loops are heavily crossed; the final sigma remains qualified, unlike the six separately readable initial sigmas.')
r.doubt('second canceled formula, first superscript','23','13','low','Final 3 and the second factor\'s 12 are legible; hatching hides enough of the first digit to retain the alternative.')
r.doubt('bottom inserted word','divers','','medium','The word remains crowded against the cancellation above after rotation upright.')
r.notation('ordinary category and field letters','C, F, k, U, A; M in later Modf','10:126 all positions; no independent category underline or repeated-strike capital established')
r.notation('first Modf initial and d overlap',firstM,'10:126 displayed opening functor')
r.notation('regular typed tensor-like operator',r'first \unsure{\otimes|\Omega}, subsequent \otimes','10:126 twelve occurrences listed individually in changes','uncertain')
r.notation('hand circled-bar operator',r'first \unsure{\ominus|\otimes}, seven later \ominus','10:126 right margin operators 1,3,4; bottom annotation five separators','uncertain')
r.notation('hand operators with visible cross',r'\otimes; \widehat{\otimes}','10:126 right margin operator 2; live (id_U tensor Delta)(sigma) in (3)')
r.notation('flattened typed operator',r'\unsure{\otimes|\varpi}','10:126 after phi pour','uncertain')
r.notation('symmetry and associativity hand letters',r'\psi; \phi','10:126 psi after données, unit compatibility and final compatibility; phi after canceled sur and final compatibility')
r.notation('Delta and sigma primes','hand letters with typed primes in mixed body; sigma-prime in hand bottom annotation','10:126 eleven production attributions listed in changes; three primes in canceled formula; newly recovered bottom prime')
r.notation('unit relation leading letter',r'\varepsilon\in1+U^+\widehat\otimes U^+','10:126 display (2); two curved epsilon lobes visible, retained without mathematical emendation')
r.notation('bottom superscripts',r'\sigma^{ij}; \sigma^{12}\sigma^{13}','10:126 bottom note and uncanceled right-hand side of (3)')
r.notation('archive pencil folio','comment only','10:126 lower-left pencil 125; retained as base PROMPT rule 4 requires')
r.r['abbreviations']=[{'abbreviation':a,'expansion':b,'attestations':c} for a,b,c in [('ass un.','associative unitaire','10:126 opening profinite algebra'),('ass. unit.','associative unitaire','10:126 coalgèbre'),('resp.','respectivement','10:126 opening'),('cf','confer','10:126 opening reference'),('hom.','homomorphisme','10:126 diagonal'),('i.e.','id est','10:126 several body/display positions'),('gr.dué','gradué','10:126 right marginal note'),('appl.','applications','10:126 bottom annotation')]]
r.r['crops']=json.loads(Path('work/crops126.json').read_text())
ov={}
for i in range(1,79):
 if i not in {1,2,4,5,9,32,53,54,66,67}:
  ov[f'126-E{i:03d}']={'hand':'his hand'}
ov.update({
 '126-E001':{'first_words_or_objects':'Voici quelques co(h/g overlap)itations; complete opening paragraph with clipped right-edge word'},
 '126-E002':{'first_words_or_objects':'F'},'126-E005':{'first_words_or_objects':'e'},
 '126-E009':{'first_words_or_objects':toutes+'; underlined typed insertion'},
 '126-E011':{'hand':'his hand','first_words_or_objects':margin},'126-E012':{'hand':'his hand','first_words_or_objects':margin},
 '126-E019':{'hand':'his hand','first_words_or_objects':'sigma, sigma; intervening prime typed'},
 '126-E021':{'hand':'his hand','first_words_or_objects':'sigma; following prime typed'},
 '126-E022':{'hand':'his hand','first_words_or_objects':'sigma sigma; following prime typed'},
 '126-E027':{'hand':'his hand','first_words_or_objects':'closing parenthesis; following prime typed'},
 '126-E036':{'hand':'his hand','first_words_or_objects':r'\mapsto'},
 '126-E041':{'hand':'typewriter','kind':'text','first_words_or_objects':'prime after Delta(u)'},
 '126-E054':{'first_words_or_objects':'i.e. A '+admet+' une unité bilatère,'},
 '126-E071':{'hand':'unnamed hand','first_words_or_objects':'mixed typed/hand display (3); first canceled six sigma factors and =1 sigma; live id/Delta formula and canceled second product'},
 '126-E072':{'hand':'his hand','first_words_or_objects':'hand sigma letters and cancellation over typed scaffold; live id/Delta formula and right-hand side'},
 '126-E073':{'hand':'unnamed hand','first_words_or_objects':r'canceled mixed formula: sigma_1 sigma_2 sigma_3 sigma-prime_1 sigma-prime_2 sigma-prime_3=1 qualified sigma'},
 '126-E074':{'hand':'his hand','first_words_or_objects':r'\sigma^{\unsure{23|13}}\sigma^{12}'},
 '126-E077':{'hand':'his hand','first_words_or_objects':r"où les sigma^{ij}; divers insertion; 3 images de sigma-prime; five circled-bar operators; appl. analogues."}
})
for i in [38,39,49,51]:ov[f'126-E{i:03d}']={'hand':'his hand','first_words_or_objects':'Delta; following prime typed'}
for i in [44,50]:ov[f'126-E{i:03d}']={'hand':'his hand','first_words_or_objects':'sigma; following prime typed'}
r.r['inventory_overrides']=ov
extras=[('typewriter','text','opening first Modf','overlapping opening parenthesis/M and r/d'),('his hand','text','opening cross-reference','6'),('his hand','drawing','toutes insertion','curved insertion guide'),('his hand','drawing','display (1)','box around final equality'),('his hand','drawing','est in display (1)','small rising curve between s and t'),('typewriter','text','display (1) and middle prose','eleven typed primes at positions individually listed in changes'),('his hand','drawing','en disant','curved insertion guide'),('his hand','drawing','unit clause insertion','long curved guide before live alors'),('typewriter','text','first canceled formula in (3)','indices 1,2,3,1,2,3; three primes; equals; 1'),('his hand','drawing','bottom divers insertion','curved insertion guide')]
r.r['inventory_extra']=[dict(scan='10:126',sheet_kind='typescript',hand=h,element=f'126-E{i:03d}',kind=k,position=p,first_words_or_objects=t,transcribed='yes') for i,(h,k,p,t) in enumerate(extras,79)]
r.r['inspection_note']='Root alone viewed whole, then both halves, then C/H and C doubts/inventory, followed by all 81 recorded crops. The whole-image output truncated in the preceding segment was repeated at 01:13:46 UTC; a truncated doubts/inventory batch was repeated fully. The four mtensor crops whose output was lost at compaction were re-viewed; mtensor1 and mtensor2 targeted adjacent pi/superscript strokes, so corrected crop recipes were generated and viewed before deciding their operators. All other extra crops and two later bottom-operator enlargements were viewed. Slanted margin and bottom insertions were inspected upright. Every C uncertainty and witness difference was accounted for, including retained clipped letters and obscured cancellations. Typed overstrikes, same-letter repetition versus dark ink, all mathematical signs/indices/primes, hand/type scopes, insertion guides, box and archival folio were checked against pixels. The lower-corner pencil 125 remains an archive comment. A provisional metadata validation rejected a backticked H-kind label; only that label formatting was corrected before successful preview. No next page was viewed during the correction. No OCR, parallel transcription, mathematical verification, context access, ordered audit, or freeze occurred.'
r.save('work/record126.json')
print('record126 saved:',len(r.r['changes']),'changes;',len(r.r['crops']),'viewed crops')
