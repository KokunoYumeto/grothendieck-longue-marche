import json
from pathlib import Path

ROOT=Path('/workspace/scratch/d7279cb02214')
WORK=ROOT/'SP92_C13_150+151_work'
P=json.loads((ROOT/'reading_packets/151_scan003/packet.json').read_text())
R=json.loads((WORK/'records/151_scan003.json').read_text())
T=(WORK/'records/151_scan003.tex').read_text()
CR={x['name']:x for x in R['crop_manifest']}
R['line_count']=65
R['line_count_convention']='Count written baselines within each separate block, including diagram label/object/relation bands, brace-label bands, raised replacement and author/later numbering. Ordinary indices and exponents stay with their parent baseline. Adjacent material sharing a baseline is counted once. Breakdown: upper diagram 9 plus cancelled arrow labels 3; delta coordinates 3; upper-margin cancelled row/equality/live product 3; author number 1; p-sigma row 1; projection coordinates 3 plus raised replacement 1; rho margin 1; cancelled p relation 1; p-rho identities 3; sigma-projection identities 3; cancelled coordinates 1; delta-rho identities 3; prose 3; first identity plus adjacent cancellation 1; main chain plus underlabels 2; sigma-delta0 box 1; cancelled i.e. chain plus underlabels 2; cancelled inequality plus question band and underlabels 3; three-value box plus two brace-label bands 5; right-margin boxes 2; cancelled Ens 1; lower diagram 4; final boxed identity 1; final formula plus upper/lower label bands 3; later foliation 1. Total65.'

def audit(place,crop,state,attachment,reading):
    R['deletion_insertion_review'].append({'place':place,'crop':CR[crop]['crop'],'box':CR[crop]['box'],'state':state,'attachment':attachment,'reading':reading})
audit('Upper three-arc draft','top_cancel_arrows','All three paths and their labels are cancelled by diagonal hatching.','Separate draft beneath the live E diagram; no object names are supplied for its blank endpoints.',r'\deleted{\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=large] {}\arrow[r,bend right=40,"\unsure{\delta_1}"\prime]\arrow[r,bend right=55,"\unsure{\delta_2}"\prime]\arrow[r,bend right=70,"\delta_3"\prime]\&{} \end{tikzcd}}}')
audit('Upper-right coordinate trial','top_margin','The full old expression is struck by two long rules; the separate equality and lower product remain live.','The curved leader reaches the separate equality below the cancelled expression; it is not another algebraic slash.',r'\deleted{$\delta_1\sigma(x,y)=(y,y,x)$}\quad $=$\\$\unsure{\sigma|\delta}_3\delta_3$')
audit('Old projection subscript','projection_cancel','The old lower digit pair is cancelled; uncertainty retained.','Attaches to the p of the second coordinate row, before the argument (x,y,z).',r'p_{\deleted{\unsure{21}}\inserted{23}}')
audit('Replacement projection subscript','projection_cancel','Fresh23 is raised and live.','Replaces the struck lower pair on the same p; it does not belong to the first coordinate row.',r'p_{\deleted{\unsure{21}}\inserted{23}}')
audit('Cancelled p12=p23','p_rho_relations','Both terms and equality are struck together.','Separate trial immediately above the live boxed three p-rho identities.',r'\deleted{\[p_{12}=p_{23}\]}')
audit('Cancelled coordinate chain','cancelled_coordinates','All three tuples and the two connecting arrows are cancelled.','Independent horizontal draft between the two three-row blocks.',r'\deleted{\[(x,y,z)\longrightarrow(y,z,x)\longrightarrow(y,z)\]}')
audit('Small cancelled initial glyph','prose_cancel','The small old a-like glyph is struck; the following Il is live.','Precedes the prose opening and is not part of its first word.',r'\deleted{\unsure{a}} Il')
audit('Draft beside first identity box','cancelled_p1','Entire small p-index/delta0 draft is cancelled; index remains uncertain.','Beside the right box edge; box p0 delta0=idE0 remains live. There is no secure independent separating comma.',r'\deleted{\unsure{p_1\delta_0|p_{12}\delta_0}}')
audit('Raised old exponent in main-chain annotation','chain_cancel1','Only the raised2/sigma-like glyph is separately cancelled.','Superscript position on rho in the underannotation of the first main delta3; rho and following delta1 stay live.',r'\rho^{\deleted{\unsure{2|\sigma}}}\delta_1')
audit('Cancelled underlabel after p23','chain_cancel2','The rho-like underlabel is separately struck.','Short bracket below the main delta1 immediately after p23; neighbouring underwritten p12 rho is live.',r'\underbrace{\delta_1}_{\deleted{\unsure{\rho}}}')
audit('Cancelled i.e. equality chain','cancelled_ie','Complete second equality chain and its lower annotations are cancelled by long diagonals and enclosure.','Separate from the upper live chain and the nearby boxed sigma identity.',r'\deleted{\[\text{i.e.}\quad\underbrace{\delta_0p_0}=\underbrace{p_{12}\delta_1}_{\sigma}=\underbrace{p_{12}\rho\delta_1}_{\mathrm{id}}=\underbrace{p_{12}\rho^2\delta_1}\]}')
audit('Cancelled inequality','cancelled_inequality','Full inequality, its parentheses and lower annotations are within the cancellation.','The authorial ?? sits above the not-equal sign; the p22-first index uncertainty remains unresolved.',r'\deleted{\[\underbrace{(p_{12}\rho)}_{p_{23}}\delta_1\overset{??}{\ne}\unsure{p_{22}|p_{12}|p_{23}}(\underbrace{\rho\delta_1}_{\delta_2})\]}')
audit('Newly identified cancelled rho subscript','values_rho','Independent small upright is crossed by two short strokes; its identity is tentatively1.','Below/right of rho on the second row of the three-value box; distinct from live superscript2. Rho retracing is not a separately recoverable old glyph.',r'\rho_{\deleted{\unsure{1}}}^{2}')
audit('Cancelled Ens-like label','cancelled_Ens','The whole old label is crossed; capitalization/parentheses remain uncertain.','Above the top edge of the lower diagram box, not part of a live object name.',r'\deleted{$\unsure{(\mathrm{Ens})|\mathrm{ens}}$}')
audit('Cancelled lower group/index','cancelled_group1','The left group-like glyph and its index are both struck.','Above E0 in the lower box; the live G2 and G3 to its right are not struck.',r'\deleted{\unsure{\mathcal G|\mathfrak S}_{\unsure{2|1}}}')
audit('Cancelled sigma-like glyph in final formula','final_cancel','Only the old sigma-like glyph is densely crossed.','Between p12 and rho2 inside the inner underbrace; the following rho2 and final sigma2 are live.',r'p_{12}\deleted{\unsure{\sigma}}\rho^2')

coverage={}
def diff(num,cl,ids,why): coverage[f'D{num:04d}']={'diff_id':f'D{num:04d}','classification':cl,'change_ids':ids,'reason':why}
diff(855,'editorial-only',[],'C scan marker versus H opening synopsis; neither is manuscript prose.')
for n in [856,857]: diff(n,'macro-only',[],'TikZ column/row/ampersand layout syntax; no different written object or word.')
for n in [858,859]: diff(n,'macro-only',[],'Different bend-angle values for the same upper delta0 curve; no new reading by angle alone.')
diff(860,'reading',['C01'],'The source return shaft is straight and one of two parallel arrows; H uses one curved path.')
diff(861,'reading',['C01'],'The second E1-to-E0 return arrow is omitted from H drawing.')
diff(862,'macro-only',[],'The numerical bend parameter alone is layout syntax; actual arrow-count loss is covered by C01.')
diff(863,'macro-only',[],'Quote delimiter in the TikZ label.')
for n in [864,865,866]: diff(n,'reading',['C01'],'H replaces extra live arrow paths/labels with editorial prose; the complete ink diagram is retained.')
diff(867,'reading',['C01','C02','C03'],'All three return arrows are present; middle p23 is resolved from ink, and the lower written label is p13, not H named p31.')
diff(868,'reading',['C04'],'Upper G2 glyph differs from the S2 name in H editorial description.')
diff(869,'alignment-only',[],'The displayed group subscript2 is aligned against the object index1 in H prose; these are distinct objects, not a 2-to-1 reading.')
diff(870,'reading',['C06'],'The upward-opening vertical membership glyph has to be retained, independently of H prose description.')
diff(871,'reading',['C05'],'Upper G3 glyph differs from the S3 name in H editorial description.')
diff(872,'alignment-only',[],'Group subscript3 is aligned against the object index2 in H prose; no substitution of one written numeral for the other.')
diff(873,'reading',['C07'],'The vertical group/element membership relation is omitted by H prose layout; its source opening faces upward.')
diff(874,'editorial-only',[],'H comma belongs to its editorial list of elements; rho squared is separately written below the group elements in the source.')
for n in range(875,883): diff(n,'reading',['C08'],'Fragments of the omitted cancelled three-arc draft; H note describes it but does not reproduce paths and cancelled labels. One actual diagram row covers these fragments.')
diff(883,'macro-only',[],'Aligned display wrapper.')
for n,cid in [(884,'C09'),(885,'C10'),(886,'C11')]: diff(n,'reading',[cid],'H supplies a comma after a coordinate row whose closing parenthesis is the last written mark.')
diff(887,'reading',['C12','C13','C14'],'Reordered coordinate boxes and upper-margin trial; the trial is cancelled, followed by a separate equals and retraced sigma/delta product.')
diff(888,'reading',['C13','C14'],'Separate equality is omitted and the first lower live glyph is sigma-first, narrowly uncertain against H delta.')
diff(889,'reading',['C15'],'Source authorial circled1 is not H editorial sentence punctuation.')
diff(890,'reading',['C16','C17','C18','C19','C20','C21'],'Reordered p relations and coordinate blocks collated by place: replacement subscript preserved and supplied commas/stops removed.')
diff(891,'macro-only',[],'Display closing delimiter only.')
diff(892,'macro-only',[],'Aligned/cases wrapper for the same three p-rho identities; all symbols independently checked.')
diff(893,'reading',['C25'],'Blocks are reordered; the cancelled coordinate chain between them is missing from H.')
diff(894,'reading',['C22'],'The first sigma-projection row is the same formula but H adds terminal punctuation.')
diff(895,'reading',['C23','C24','C26'],'H reorders sigma rows and omits the small raised a-like terminal in the third delta-rho row; punctuation is separately collated.')
diff(896,'reading',['C27'],'Small struck initial glyph before live Il is omitted by H.')
diff(897,'reading',['C28'],'Avoir is visible, with no preceding se; C doubt resolved and H se donner rejected from strokes.')
diff(898,'reading',['C29'],'Entre has a visible crossed t and terminal re; H avec is not the written word.')
diff(899,'reading',['C30'],'Prose G2 glyph resolved by its recurring open bowl and inward return.')
diff(900,'reading',['C31'],'Prose G3 glyph resolved by the same recurring contour.')
diff(901,'reading',['C33'],'H aligns its relocated sigma identity against the omitted cancelled p-index/delta0 draft.')
diff(902,'reading',['C41'],'The sigma identity itself is a relocated equal reading; H following comma is absent from the ink.')
diff(903,'reading',['C34'],'H interchanges the main delta3 with the rho-delta1 underannotation.')
diff(904,'reading',['C34'],'Continuation of the same main-term/underlabel displacement, not a missing equality in C.')
diff(905,'reading',['C35'],'The independently cancelled raised2/sigma-like annotation is absent from H; its doubt is retained.')
diff(906,'reading',['C36','C37'],'H omits the p23 underlabel and the separate cancelled rho-like label under the following delta1.')
diff(907,'reading',['C38','C39'],'H omits the p31 underlabel and interchanges final main delta2 with its underannotation.')
diff(908,'alignment-only',[],'Relocated sigma identity/display boundary aligns against a lower-annotation delimiter; actual readings collated at their source places.')
diff(909,'reading',['C40','C41'],'H final full stop and relocated-box comma are absent; the equal sigma-delta0 formula is preserved in its source position.')
diff(910,'editorial-only',[],'H explanatory note introduction and quotation marks are not written manuscript prose.')
diff(911,'reading',['C42'],'H description replaces the full cancelled second equality chain; complete source chain retained.')
diff(912,'reading',['C42'],'Underwritten sigma in the cancelled i.e. chain is source math; the aligned H comma belongs to editorial prose.')
diff(913,'reading',['C42','C43','C44','C45','C46','C47','C48'],'Long alignment crosses cancelled trials and value box: full chains, question placement, index doubts, brace direction and new crossed rho subscript are collated by actual place.')
for n in [914,915]: diff(n,'macro-only',[],'Apparent comma token is H TeX thin-space command, not written punctuation.')
diff(916,'macro-only',[],'Aligned/cases display wrapper; box/brace layout is represented in candidate and actual over/under annotation difference logged separately.')
diff(917,'macro-only',[],'Display opening delimiter.')
diff(918,'reading',['C49','C50'],'H adds separators after the two margin boxes; neither independent comma is written.')
diff(919,'reading',['C51','C52','C55'],'Cancelled Ens-like label and beginning of the omitted lower diagram, including cancelled left group/index.')
diff(920,'reading',['C52','C53','C54','C55'],'The lower boxed diagram and its group row are omitted. H following rho identity is a different source block, not an alternate diagram label.')
diff(921,'alignment-only',[],'TikZ right-arrow key aligns against rho in the following H boxed formula; no r/rho glyph substitution.')
diff(922,'reading',['C52'],'Remaining lower diagram maps and objects omitted by H.')
diff(923,'macro-only',[],'H thin-space command after sigma1, not a written comma.')
diff(924,'reading',['C56'],'H actual comma after the final boxed identity is not present in the source.')
diff(925,'macro-only',[],'Spacing between p0 and p12; no comma is written or required by the source.')
diff(926,'reading',['C57'],'The left underlabel exists; clipped numeral favors2 but remains2|1.')
diff(927,'macro-only',[],'H TeX thin-space command, not punctuation.')
diff(928,'reading',['C58'],'Separately cancelled sigma-like glyph omitted by H.')
diff(929,'reading',['C59','C60','C61'],'Live sigma2 and the outer upper p12 bracket are absent from H, which also adds a final full stop.')
diff(930,'reading',['C62'],'Later thin foliation2 is omitted by H.')
R['diff_coverage']=[coverage[d['diff_id']] for d in P['differences']]

def inv(element,kind,position,first,hand='author',sheet='text'):
    R['inventory'].append({'sheet_kind':sheet,'hand':hand,'element':element,'kind':kind,'position':position,'first_words_or_objects':first,'transcribed':'yes'})
inv('Upper live three-object diagram','diagram','upper left','E0, E1, E2; delta0; three delta arrows; p0,p1 and p12,p23,p13; G2,G3 and elements')
inv('Cancelled three-arc draft','deletion','beneath upper live diagram','delta1?, delta2?, delta3','author','cancelled_draft')
inv('Delta coordinate box','display','upper centre','delta3(x,y)=(x,x,y); delta1; delta2')
inv('Cancelled coordinate trial','deletion','upper right margin','delta1 sigma(x,y)=(y,y,x)','author','cancelled_draft')
inv('Separate equality linked below trial','margin note','below upper-right cancellation','=')
inv('Live retraced product','margin note','lower part of upper-right note','sigma|delta subscript3, delta3')
inv('Author page number','margin note','upper right edge','circled1')
inv('Two p-sigma relations','display','left below upper diagram','p_{1|0}=p0 sigma, p0=p1 sigma')
inv('Projection coordinate box','display','upper middle','p12(x,y,z)=(x,y); revised p23; p31')
inv('Cancelled old projection index','deletion','second coordinate row','21?','author','cancelled_draft')
inv('Raised new projection index','insertion','above cancelled pair on second-row p','23')
inv('Rho coordinate action','margin note','right of projection box','rho(x,y,z)=(y,z,x)')
inv('Cancelled p equality','deletion','above left boxed identities','p12=p23','author','cancelled_draft')
inv('Three p-rho identities','display','left centre','p23=p12 rho; p31; p12')
inv('Three sigma-projection identities','display','below left box','sigma p12=p12 sigma3; sigma p23; sigma p31')
inv('Cancelled coordinate arrow chain','deletion','centre between live identity groups','(x,y,z) to (y,z,x) to (y,z)','author','cancelled_draft')
inv('Three delta-rho identities','display','right centre','delta1=rho delta2=rho2 delta3; delta2; delta3')
inv('Small raised terminal mark','margin note','end of third delta-rho row','a-like raised mark')
inv('Cancelled initial glyph','deletion','before Il in central prose','a?','author','cancelled_draft')
inv('Three-line prose statement','text','centre','Il suffit de avoir p0,p12,delta0,delta1 entre les trois ensembles')
inv('First identity box','display','left below prose','p0 delta0=idE0')
inv('Cancelled adjacent short expression','deletion','right of first identity box','p1 delta0 | p12 delta0','author','cancelled_draft')
inv('Main equality chain','display','across middle below prose','delta0 p0=p12 delta3=p23 delta1=p31 delta2')
inv('Main-chain five underannotations','insertion','below the individual terms of main chain','rho with cancelled exponent delta1; p12 rho; cancelled rho; p12 rho2; rho2 delta1')
inv('Cancelled raised annotation glyph','deletion','under first main delta3, on rho','2|sigma','author','cancelled_draft')
inv('Cancelled rho-like underlabel','deletion','under main delta1 after p23','rho?','author','cancelled_draft')
inv('Sigma delta0 box','display','left beneath first identity','sigma delta0=delta0')
inv('Cancelled i.e. chain and brackets','deletion','middle lower trial zone','i.e. delta0 p0=p12 delta1=p12 rho delta1=p12 rho2 delta1','author','cancelled_draft')
inv('Cancelled inequality and underlabels','deletion','below cancelled i.e. chain','(p12 rho)delta1 != p_{22|12|23}(rho delta1)','author','cancelled_draft')
inv('Author question marks','margin note','above inequality sign','??')
inv('Three-value boxed system','display','lower centre right','delta0 p0=p12 rho delta1; idE1=p12 rho2 delta1; sigma=p12 delta1')
inv('Value-system brace annotations','insertion','above first and below second row products','delta3 above; delta2 below')
inv('Cancelled tiny rho subscript','deletion','second row of three-value box','1? below rho','author','cancelled_draft')
inv('Upper right-margin relation box','margin note','right of three-value box','sigma3 delta1=delta1')
inv('Lower right-margin relation box','margin note','below preceding margin box','p12 sigma3=sigma p12')
inv('Cancelled Ens-like label','deletion','above lower left box','(Ens)|ens','author','cancelled_draft')
inv('Lower live boxed diagram','diagram','lower left','G2,G3; E0 leftarrow E1 leftarrow E2; delta0 and delta1 return curves')
inv('Cancelled group/index above E0','deletion','upper-left cell of lower box','G|S, index2|1','author','cancelled_draft')
inv('Final rho/sigma identity box','display','lower right','rho delta1 delta0=sigma1 delta1 delta0=delta1 delta0')
inv('Bottom formula with three brackets','display','bottom right, partially at sheet edge','p0 p12=p0 p12 [cancelled sigma] rho2 sigma2')
inv('Cancelled sigma-like factor','deletion','inside bottom formula','sigma?','author','cancelled_draft')
inv('Bottom formula annotations','insertion','above/below bottom products','left p_{2|1}; inner p31; outer p12')
inv('Later foliation','margin note','lower left edge','2','other hand (later thin foliation)')

R['notes']=r'''## Content and literal transcription

This autograph leaf develops a three-object system E0,E1,E2 with forward delta maps, returning p maps, two group labels read from their repeated G-shaped contours, and elements sigma, rho and sigma1,sigma2,sigma3. It supplies coordinate realizations for three delta maps, three projections and rho; records p-rho, sigma-projection and delta-rho identities; then states that it suffices to have four indicated maps between the three ensembles with the displayed relations. A lower boxed diagram repeats a smaller selection of maps. The page is densely revised, including a cancelled diagram, coordinate trial, equality and inequality trials, and individual replaced/cancelled indices.

The prose is literally “Il suffit de avoir … entre les trois ensembles”. No “se” is visible and avoir is not replaced by the more grammatical donor wording in H. All six live group glyphs have an open rounded bowl, curled top and inward return and are transcribed calligraphic G. This is a reading of the written shape, not a claim that the groups differ from symmetric groups. H's bridging sentences, synopsis and explanatory notes are editorial and are excluded from source text.

## Mathematical triggers for rereading, without a proof claim

The upper diagram's lowest return is plainly p13, while the later coordinate box has p31. Both literal labels stand. The middle upper return p23 was resolved from its tight crop together with the full diagram. The main equality's baseline delta3 and delta2, and their lower rho annotations, were checked as complete products because H exchanges the baseline and underlabel roles. The two vertical membership signs open upward; the diagram encoding preserves that orientation.

The boxed right-margin sigma3 delta1=delta1 was reread, including both delta indices and sigma's subscript, after root flagged a possible conflict with the coordinate realization and nearby transposition identity. The written3 is clear, as are the two1 indices, and is preserved. This reader did not perform an independent coordinate computation or proof check; any mathematical check supplied by root is to be logged separately. The authorial inequality has a literal not-equal and two question marks directly above it. Its crossed right-hand projection index remains p22-first with p12/p23 alternatives; no index is chosen by associativity or an expected identity.

The final formula was read with both nested brackets and all their labels: p31 belongs below the inner right product, p12 above the larger right product, and a partly clipped p_{2|1} below the left product. The final live sigma2 is present. The boxed identity immediately above has sigma1, whose serifed upright is distinct from a bent2. The lowest paper edge clips the tip of the left lower index; it is not completed by mathematical expectation.

## Revisions and physical state

The replacement23 is raised over a crossed old pair tentatively21 in the projection coordinate box. The first main-chain underannotation contains a separately cancelled raised2/sigma-like mark on rho, and the next delta1 carries a separately cancelled rho-like underlabel. A short upright below/right of rho in the three-value box is independently crossed by two transverse strokes and is retained as a cancelled doubtful1, separate from the live superscript2. The rho body itself is merely retraced as far as the surviving ink shows. The cancellation of the large i.e. and inequality trials does not extend into the clean value box. The upper-right lower product remains sigma|delta at its first retraced letter. The old lower group/index remains doubly uncertain, with G|S and2|1; the live G occurrences do not certify the crossed glyph.

No title, date or formula numbering is written. The author's dark circled1 at upper right is distinct from thin grey foliation2 at lower left, assigned to another hand. There is no typescript or reused typed text on this face. The 65-baseline count includes diagram label bands, annotations, separate margins and both foliations under the stated convention; ordinary attached indices and exponents are not counted as independent lines.
'''
R['check_events']=[]
R['notation']=[
 {'sign':r'\mathcal G_2,\mathcal G_3','reading':'The written group labels use a G-shaped capital.','evidence':'All six live occurrences: open round bowl, curled upper tip, inward return/loop. Group identification is kept separate from shape.'},
 {'sign':r'\in rotated +90 degrees','reading':'Vertical membership glyph opening upward.','evidence':'Both signs beneath the upper group labels have three upward tines; preserve direction in diagram.'},
 {'sign':r'\rho','reading':'Rho with oval upper loop and long descending stem.','evidence':'Coordinate action and three-value box; its separate crossed small subscript is not part of the rho body.'},
 {'sign':r'p_{13} versus p_{31}','reading':'Both orders occur literally at different places.','evidence':'Upper lowest return reads1 then3; projection coordinate row reads3 then1.'},
 {'sign':r'\sigma_3\delta_1=\delta_1','reading':'Literal boxed margin relation, preserved despite mathematical trigger.','evidence':'Sigma subscript3 has two lobes; both delta subscripts are simple1.'},
 {'sign':'Nested bracket labels','reading':'Main formula terms and under/overlabels remain in their written positions.','evidence':'Main chain, value box and bottom formula distinguish vertical annotation from baseline product.'}
]
R['hand_log']=[
 {'habit':'Calligraphic G has a broad open bowl, upper curl and inward looped return.','places':['151_scan003 upper groups','151_scan003 prose groups','151_scan003 lower groups'],'scope':'All six live group glyphs on this page; the separately cancelled group is not certified.','witness_errors':'C first alternatives and H names use S; live contours support G.'},
 {'habit':'Small2 can have an angular cap followed by a low hooked foot;3 retains a double turn.','places':['151_scan003 projection indices','151_scan003 cancelled inequality','151_scan003 final underlabels'],'scope':'Clear examples support local comparisons; saturated and clipped indices retain doubts.','witness_errors':'C first23 in crossed inequality is reordered to22-first; final left underlabel1-first becomes2-first.'},
 {'habit':'A small1 may be serifed and have a base, so a base alone does not prove2.','places':['151_scan003 final boxed sigma1','151_scan003 first p relation'],'scope':'Final sigma1 is clear; first p subscript is saturated and remains1|0.','witness_errors':'Agreed p1 in first p relation receives a local uncertainty only.'},
 {'habit':'Retracing inside a letter is distinguished from an independent cancellation stroke.','places':['151_scan003 upper-right sigma/delta','151_scan003 three-value rho','151_scan003 final sigma-like deletion'],'scope':'Occurrence-specific: dense letter bodies do not by themselves prove a deleted earlier symbol.','witness_errors':'Both witnesses omit the separate crossed tiny rho subscript; no additional old letter is invented inside rho.'},
 {'habit':'Brackets and leaders carry attachment information and do not themselves supply punctuation.','places':['151_scan003 upper-right equality leader','151_scan003 first identity edge','151_scan003 main and bottom brackets'],'scope':'Distinct full formulas and local lines traced separately.','witness_errors':'H changes under/over and baseline/annotation roles; both witnesses supply an insecure comma after the first identity box.'},
 {'habit':'Dark author numbering differs from later thin lower foliation.','places':['151_scan003 circled1','151_scan003 lower2'],'scope':'Two separate hands on this leaf.','witness_errors':'H omits both numbers; neither is a formula number.'}
]
R['abbreviations']=[{'form':'i.e.','expansion':'id est (that is)'},{'form':'id','expansion':'identité / identity map'},{'form':'(Ens)|ens, cancelled and uncertain','expansion':'ensembles, if the uncertain cancelled label is correctly identified'}]

def doubt(place,read,alts,conf,reason,crop):
    R['doubts'].append({'place':place,'reading':read,'alternatives':alts,'confidence':conf,'reason':reason,'crop':CR[crop]['crop'],'box':CR[crop]['box']})
doubt('Cancelled upper arrow labels',r'\unsure{\delta_1},\unsure{\delta_2}',[],'low','Hatching obscures the first two label joins and indices. The exposed lowest delta3 is clear.','top_cancel_arrows')
doubt('Upper-right lower product',r'\unsure{\sigma|\delta}_3\delta_3',[r'\sigma_3\delta_3',r'\delta_3\delta_3'],'medium','Top bar and low closed loop favor sigma; dense retracing leaves a delta-like spine. No certainty beyond that glyph.','top_margin')
doubt('First left p subscript',r'p_{\unsure{1|0}}',['1','0'],'low','Saturated rounded numeral has a short descending right tail, differing from the thin1 and open0 in nearby terms. Added uncertainty alone does not create a change row.','p_relations')
doubt('Cancelled old projection subscript',r'\deleted{\unsure{21}}',['21'],'low','Strike traverses the old pair; raised replacement23 is clear. Old reading remains unconfirmed.','projection_cancel')
doubt('Small raised terminal in third delta-rho identity',r'{}^{\unsure{a}}',['a'],'low','Tiny loop-and-return is raised; exact letter/function is not settled.','delta_relations')
doubt('Cancelled initial a-like glyph',r'\deleted{\unsure{a}}',['a'],'low','Loop and descending return survive, but cancellation prevents full identification.','prose_cancel')
doubt('Alleged comma beside first identity box','no independent comma',['no independent comma','comma'],'medium','Nearby downstroke belongs to cancelled p draft or box junction; no independent punctuation can be separated. Omission is preferred without introducing an extra mark.','p0_identity')
doubt('Cancelled expression beside identity box',r'\deleted{\unsure{p_1\delta_0|p_{12}\delta_0}}',[r'p_1\delta_0',r'p_{12}\delta_0'],'low','A low footed trace before delta may be an extra2. Strike prevents certain index length. Alternative broadening alone is not counted against C.','cancelled_p1')
doubt('Cancelled raised annotation after rho',r'\rho^{\deleted{\unsure{2|\sigma}}}\delta_1',['2',r'\sigma'],'low','Small raised contour is independently crossed and remains2/sigma.','chain_cancel1')
doubt('Cancelled underlabel below main delta1',r'\deleted{\unsure{\rho}}',[r'\rho'],'low','The loop and stem are largely overwritten by short crossing strokes; no new certainty.','chain_cancel2')
doubt('Cancelled inequality RHS index',r'\unsure{p_{22}|p_{12}|p_{23}}',[r'p_{22}',r'p_{12}',r'p_{23}'],'low','Angled first entry with hooked foot favors2, second digit favors2; the strike leaves12/23 possible. No algebraic expectation decides it.','cancelled_inequality')
doubt('New cancelled subscript below rho2',r'\rho_{\deleted{\unsure{1}}}^{2}',['1'],'low','Separate upright crossed by two transverse marks is certain as a deletion; exact numeral is tentative.','values_rho')
doubt('Cancelled Ens-like label',r'\deleted{$\unsure{(\mathrm{Ens})|\mathrm{ens}}$}',[r'(\mathrm{Ens})',r'\mathrm{ens}'],'low','Opening parenthesis-like trace and E/e, n, s remnants are crossed; both parentheses/case not certified.','cancelled_Ens')
doubt('Cancelled lower group/index',r'\deleted{\unsure{\mathcal G|\mathfrak S}_{\unsure{2|1}}}',[r'\mathcal G_2',r'\mathfrak S_2',r'\mathcal G_1',r'\mathfrak S_1'],'low','Left glyph is inseparable from crossing, while long diagonal and low rightward foot favor index2;1 remains possible.','cancelled_group1')
doubt('Bottom cancelled sigma-like glyph',r'\deleted{\unsure{\sigma}}',[r'\sigma'],'low','Dense crossed oval and top bar support only a tentative sigma; neighbouring rho2 stays live.','final_cancel')
doubt('Bottom left underlabel',r'p_{\unsure{2|1}}',['2','1'],'medium','Bent upper stroke, oblique descent and rightward foot favor2, but the paper edge clips the lowest tip.','final_formula')

def take(start,end): return T[T.index(start):T.index(end)].strip()
def b(kind,coords,reading):
    R['second_boxes'].append({'box':f'B{len(R["second_boxes"])+1:02d}','kind':kind,'x0':coords[0],'y0':coords[1],'x1':coords[2],'y1':coords[3],'reading':reading})
def cb(kind,crop,reading): b(kind,CR[crop]['box'],reading)
b('whole live and cancelled diagrams; all numbers; resolved group/label doubts',[155,0,688,410],take(r'\diagram{\begin{tikzcd}',r'\[\boxed{\begin{aligned}'))
cb('whole numbered coordinate formula','delta_coordinates',take(r'\[\boxed{\begin{aligned}',r'\margin{\deleted'))
cb('whole margin trial, deletion, equality and doubtful live product','top_margin',take(r'\margin{\deleted',r'\mspage'))
cb('author handwritten page number','circled1',r'\mspage{\textcircled{1}}')
cb('whole formula with agreed-reading index doubt and numbers','p_relations',r'\[p_{\unsure{1|0}}=p_0\sigma,\quad p_0=p_1\sigma\]')
cb('whole coordinate box; struck and inserted indices','projection_coordinates',take(r'\[\boxed{\begin{aligned}'+'\n'+r'p_{12}(x,y,z)',r'\margin{$\rho'))
cb('numbered coordinate margin formula','rho_margin',r'\margin{$\rho(x,y,z)=(y,z,x)$}')
cb('cancelled equality and whole three-row numbered system','p_rho_relations',take(r'\deleted{\[p_{12}=p_{23}',r'\[\begin{aligned}'+'\n'+r'\sigma p_{12}'))
cb('three numbered sigma-projection relations','sigma_relations',take(r'\[\begin{aligned}'+'\n'+r'\sigma p_{12}',r'\deleted{\[(x,y,z)'))
cb('whole cancelled coordinate formula','cancelled_coordinates',r'\deleted{\[(x,y,z)\longrightarrow(y,z,x)\longrightarrow(y,z)\]}')
cb('whole formula with terminal doubt and all indices','delta_relations',take(r'\[\left\{\begin{aligned}',r'\deleted{\unsure{a}} Il'))
cb('all prose; differing words; cancelled initial; all numbered group names','prose_full',take(r'\deleted{\unsure{a}} Il',r'\[\boxed{p_0\delta_0'))
b('whole first identity and adjacent cancelled expression; punctuation doubt',[169,1164,644,1350],take(r'\[\boxed{p_0\delta_0',r'\[\delta_0p_0='))
cb('whole equality chain; every underannotation and two local cancellations','main_chain',take(r'\[\delta_0p_0=',r'\[\boxed{\sigma\delta_0'))
cb('whole numbered boxed identity','sigma_delta0',r'\[\boxed{\sigma\delta_0=\delta_0}\]')
cb('whole cancelled i.e. chain and underlabels','cancelled_ie',take(r'\deleted{\[\text{i.e.}',r'\deleted{\[\underbrace{(p_{12}\rho)}'))
cb('whole cancelled inequality; question marks and all index doubts','cancelled_inequality',take(r'\deleted{\[\underbrace{(p_{12}\rho)}',r'\[\boxed{\begin{aligned}'+'\n'+r'\delta_0p_0'))
cb('whole three-value box; under/overlabels and new cancelled subscript','values_box',take(r'\[\boxed{\begin{aligned}'+'\n'+r'\delta_0p_0',r'\margin{$\boxed{\sigma_3'))
cb('both complete numbered margin boxes','margin_values',take(r'\margin{$\boxed{\sigma_3',r'\deleted{$\unsure{(\mathrm{Ens})'))
cb('whole lower diagram; cancelled Ens and group; all labels/numbers','lower_diagram',take(r'\deleted{$\unsure{(\mathrm{Ens})',r'\[\boxed{\rho\delta_1'))
cb('whole final boxed identity; all indices','final_box',take(r'\[\boxed{\rho\delta_1',r'\[\underbrace{p_0p_{12}}'))
cb('whole bottom formula with all brackets, numbers and deletion/doubt','final_formula',take(r'\[\underbrace{p_0p_{12}}',r'\margin{2}'))
cb('later handwritten foliation','folio2',r'\margin{2}')

R['status']='complete candidate, awaiting root finalization'
R['validation']={'complete_diff_rows':len(R['diff_coverage']),'marks_in_supplied_order':[d['id'] for d in R['decisions']],'changes':len(R['changes']),'saved_and_viewed_crops':len(R['crop_manifest']),'deletion_insertion_items':len(R['deletion_insertion_review']),'inventory_items':len(R['inventory']),'blind_regions':len(R['second_boxes']),'mathematical_check_events':0,'tex_compiled':False,'ocr_used':False,'external_research_used':False}
(WORK/'records/151_scan003.json').write_text(json.dumps(R,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(R['validation'],ensure_ascii=False))
