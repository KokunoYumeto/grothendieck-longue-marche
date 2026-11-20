from pathlib import Path
import json
P='C123-02_123_scan022'
base=Path('/workspace/scratch/d27bd2a88bca')
M={x['id']:x for x in json.loads((base/'out/work'/f'{P}_crop_manifest.json').read_text())}
R={'page':P,'line_count':26,'changes':[],'doubts':[],'inventory':[],'notes':[],'reading_notes':[],'check_events':[],'visual_audit_events':[],'notation':[],'hand_log':[],'boxes':[]}
def ch(id,line,c,h,final,scan,crop,conf,kind,C,H,marked=False,cons=False,certainty=False):
 m=M[crop]; R['changes'].append(dict(id=id,line=line,c=c,h=h,final=final,scan_shows=scan,crop=m['crop'],box=m['box'],confidence=conf,kind=kind,changed_C=C,changed_H=H,marked_in_H=marked,consequential=cons,certainty_only=certainty))
ch('r01','date heading',r'\unsure{Massy}','Massy',r'\unsure{Massy}','M, a and final y are distinct; the two compressed middle strokes do not permit a fully certain place reading. Date is clear.','b01','medium','other',False,True,False,False,True)
ch('r02','L01',r'\unsure{Maer.|Amer.}','Amer.',r'\unsure{Maer.|Amer.}','The first two letter cells are densely overstruck. The visible first contour is M-like and the second a-like; possible Amer. superposition/order cannot be settled. The journal context is not used to normalize them.','b02','low','misread word',False,True)
ch('r03','L01',r'\deleted{t}\handwritten{T}he','The',r'\deleted{t}\handwritten{T}he','The machine lower-case t remains below a pen capital T, with a new top bar. H omits this original state.','b03','high','deletion state (struck given live or live given struck)',False,True)
ch('r04','L03','polynomail with handwritten transposition curve across ai','polynomial','polynomail with handwritten transposition curve across ai','The typed sequence is a then i. A pen curve descends across the a, passes under i and turns up between i and l. It is a correction mark, not replacement typed letters; C’s TikZ representation is retained.','b05','high','misread word',False,True)
ch('r05','L06',r'appea\deleted{\unsure{k|r}}\handwritten{r}ed','appeared',r'appea\deleted{\unsure{k|r}}\handwritten{r}ed','The retouched cell contains the r body plus angled strokes. Underlying k/r and the correction mechanism remain uncertain; H omits the correction state.','b06','low','deletion state (struck given live or live given struck)',False,True)
ch('r06','L07',r'\deleted{\unsure{a|A}}\handwritten{A}lg.','Alg.',r'\deleted{\unsure{a|A}}\handwritten{A}lg.','A low oval body and added narrow upper stroke are visible. Original a is preferred, but original A reinforced by pen cannot be excluded.','b07','medium','deletion state (struck given live or live given struck)',False,True)
ch('r07','L10',r'quadr\deleted{\unsure{a|u}}uples','quadruples',r'quadr\deleted{\unsure{a|u}}uples','A distinct extra canceled typewriter cell lies between r and the following live u. Its surviving lower contour favors a, but the x overstrike prevents certainty.','b08','medium','omission',False,True)
ch('r08','L13',r'$\deleted{\unsure{\mathrm H|\mathrm W}}\handwritten W$','$W$',r'$\deleted{\unsure{\mathrm H|\mathrm W}}\handwritten W$','The corrected W has a squared lower/interior impression compatible with H or a multiply struck W. Both under-readings remain explicit, without inferring them from Weyl group.','b10','low','deletion state (struck given live or live given struck)',False,True)
ch('r09','L14',r'\operatorname{card}(\underline{\mathrm Z}/h\underline{\mathrm Z})^{\handwritten *}',r'\operatorname{card}(\mathbb Z/h\mathbb Z)^*',r'\operatorname{card}(\underline{\mathrm Z}/h\underline{\mathrm Z})^{\handwritten *}','The two Zs are single machine capitals, each with a separate short underline. The star is pen. No double-struck construction is present in this typed formula.','b12','high','misread symbol or index',False,True,False,True)
ch('r10','L15 and insertion',r'a\deleted n \inserted{generating}','a generating',r'a\deleted n \inserted{g\deleted{\unsure{a|e}}enerating}','The n of an is canceled with x. Generating is typed above the line with a pen callout; its first e shows a second, a-like or repeated-e impression with an exposed lower-right foot. The proposed underletter remains explicitly doubtful.','b13','low','deletion state (struck given live or live given struck)',True,True)
ch('r11','L18','stability','stablity [sic]','stablity','The machine sequence is s-t-a-b-l-i-t-y: no i appears between b and l. H’s sic is editorial and is not transcribed.','b16','high','misread word',True,False,True)
ch('r12','L26',r'automorph\deleted{\unsure{k|i}}isms','automorphisms',r'automorph\deleted{k}isms','A complete tall k stem, right arm and diagonal leg remain beneath the dotted upright i. The deleted k is distinguishable independently of the intended word.','b20','high','omission',True,True)
ch('r13','L26',r'quadr\deleted a uples','quadruples',r'quadr\deleted a uples','An additional canceled a cell is visible between r and u; its lower bowl survives the x overstrike.','b21','high','omission',False,True)
ch('r14','bottom note after Z',r'\deleted{\unsure{(G)|(\widetilde G)}}',r'\struck{\ill{}}',r'\deleted{\unsure{(G)|(\widetilde G)}}','Heavy pen scribble obscures most of the canceled suffix. A lower curved G-like trace survives, but neither the exact parentheses nor a tilde is secure. C’s tentative alternatives remain; no claim of a fully recovered reading is made.','b23','low','other',False,True,True)
R['doubts']=[
 {'line':'date heading','reading':'Massy','alternatives':[],'confidence':'medium','reason':'Compressed middle two strokes; place remains unsure. Date 22.10.1969 is clear.'},
 {'line':'L01','reading':'Maer.','alternatives':['Amer.','unestablished overtyping sequence of the first two cells'],'confidence':'low','reason':'Dense overlapping machine contours. No journal identification was consulted.'},
 {'line':'L06','reading':r'appea\deleted{\unsure{k|r}}\handwritten{r}ed','alternatives':['original r with retouch rather than original k'],'confidence':'low','reason':'Angled strokes cross the r cell; layer identity/chronology remains uncertain.'},
 {'line':'L07','reading':r'\deleted{\unsure{a|A}}\handwritten A','alternatives':['original A reinforced'],'confidence':'medium','reason':'Lower oval favors a, but the pen upper stroke and light original type prevent a certain separation.'},
 {'line':'L10','reading':r'quadr\deleted{\unsure{a|u}}uples','alternatives':['extra canceled u'],'confidence':'medium','reason':'Extra cell is certain; its lower contour is only partly visible.'},
 {'line':'L13','reading':r'\deleted{\unsure{H|W}}\handwritten W','alternatives':['multiply struck W without a separate H'],'confidence':'low','reason':'Squared lower body under the final W cannot be assigned securely.'},
 {'line':'L15 insertion','reading':r'g\deleted{\unsure{a|e}}enerating','alternatives':['repeated e impression','ordinary uneven e impression without a different underlying letter'],'confidence':'low','reason':'First e has an exposed foot/extra contour; a-like underprint is proposed cautiously. Root adjudication needed.'},
 {'line':'bottom note after Z','reading':r'\deleted{\unsure{(G)|(\widetilde G)}}','alternatives':['unrecoverable canceled suffix'],'confidence':'low','reason':'Scribble conceals nearly all internal strokes; separate lower annotation clearly has G with tilde.'}
]
def inv(y,el,kind,txt,hand='typewriter',pos=None):
 R['inventory'].append(dict(scan=22,sheet_kind='typescript',hand=hand,element=el,kind=kind,position=pos or f'y≈{y}',first_words_or_objects=txt,transcribed='yes',_y=y))
inv(140,'D01','text','Massy [uncertain] 22. 10. 1969','pen hand 1','top right handwritten place/date')
inv(243,'S01','text','Dear Kostant,','typewriter','salutation, upper left')
starts=[
(310,'I read again through your papers in the Maer./Amer. Journ. on The'),
(377,'principal three-dimensional subgroup ... and Lie group representations'),
(444,'on polynomail rings, prompted by some nice work of Brieskorn on Klein sin-'),
(510,'gularities. I very much appreciate this work of yours, and would appreciate'),
(577,'getting reprints of any later work you may have available. As I already'),
(643,'felt when your work appeared, it cries for careful reconsideration in the'),
(710,'framework of Alg. Geometry, and suggests number of interesting problems. I'),
(776,'wonder if you know the answer to some of them. For instance, I feel it would'),
(843,'be of interest to classify (for a given complex simple adjoint Lie group,'),
(909,"say) quadruples (T,B,T',B'), where T and T' are maximal tori in apposition"),
(976,"(in your terminology), and B and B' Borel subgroups of G containing T resp."),
(1042,"T'. The number of conjugacy classes of such animals is equal to"),
(1109,'card(W)^2/hzφ(h), where W is the Weyl group, h the Coxeter number, z the or-'),
(1175,'der of the center, and φ(h)=card(underlined Z/h underlined Z)^* is the Euler indicatrix; if you'),
(1242,'want to classify such data with moreover an element (principal regular in'),
(1308,"your terminology) given for the finite group of order h T∩N(T'), then we"),
(1375,'get card(W)^2/hz choices. One of the reasons I think this question is inte-'),
(1441,"resting is that the stablity subgroup in G of such a quadruple is T∩T'=e,"),
(1508,'hence such a structure makes G entirely rigid up to exterior automorphisms.'),
(1574,'Among the first questions one may wish to ask in this direction are the'),
(1641,"following: is it true that for some, or for all, such quadruples, B and B'"),
(1707,"are in general position i.e. B∩B' is a torus (necessarily maximal), so"),
(1774,"that B and B' are opposite to each other with respect to the latter ?"),
(1840,'Is there in any sense a distinguished conjugacy class of such quadruples'),
(1907,'(which should then be, of course, invariant by action of exterior automor-'),
(1959,'phisms) ? What are the groups of automorphisms of such quadruples (they')]
for n,(y,t) in enumerate(starts,1):inv(y,f'L{n:02}','text',t,'typewriter with separately inventoried corrections',f'L{n:02}; main baseline y≈{y}')
inv(299,'I01','insertion','opening double quotation mark','pen hand 1','above corrected The on L01')
inv(310,'I02','deletion','t','typewriter under pen correction','L01 initial letter of first quoted title')
inv(310,'I03','insertion','T','pen hand 1','L01 over the original t')
inv(364,'I04','insertion','closing double quotation mark','pen hand 1','after subgroup ... on L02')
inv(364,'I05','insertion','opening double quotation mark','pen hand 1','before Lie group on L02')
inv(441,'I06','insertion','transposition stroke across typed ai in polynomail','pen hand 1','L03; descends through a, loops below i, turns up before l')
inv(421,'I07','insertion','closing double quotation mark','pen hand 1','after rings on L03')
inv(643,'I08','deletion','uncertain k/r under final r of appeared','typewriter with pen-like retouch','L06')
inv(643,'I09','insertion','r retouch in appeared','pen hand 1, mechanism uncertain','L06')
inv(710,'I10','deletion','uncertain a/A in Alg.','typewriter with pen correction','L07')
inv(710,'I11','insertion','A in Alg.','pen hand 1','L07')
inv(909,'I12','deletion','extra a/u between r and u in quadruples','typewriter x cancellation','L10')
inv(909,'I13','insertion','closing double quotation mark after apposition','pen hand 1','L10 far right edge')
inv(1086,'I14','insertion','superscript 2','handwritten, pale stroke','above first card(W) on L13')
inv(1109,'I15','text','φ(h)','pen φ; typed h and parentheses','L13 quotient formula')
inv(1109,'I16','deletion','uncertain H/W beneath W','typewriter overprint/pen reinforcement uncertain','L13 after where')
inv(1109,'I17','insertion','W','pen hand 1 or reinforced typewriter glyph','L13 after where')
inv(1143,'I18','insertion','of G with tilde','pen hand 1','between L13/L14; callout after center')
inv(1175,'I19','text','φ(h)=card(underlined Z/h underlined Z)^*','mixed typewriter and pen φ/star','L14 Euler formula')
inv(1213,'I20','insertion','generating, with uncertain first-e overprint','typewriter with pen leader','between L14/L15; inserted before element')
inv(1213,'I21','deletion','uncertain a/e beneath first e of generating','typewriter overprint proposed','within I20')
inv(1242,'I22','deletion','n of an','typewriter x cancellation','L15 before element')
inv(1308,'I23','text',"T∩N(T')",'typewriter with pen intersection','L16')
inv(1350,'I24','insertion','superscript 2','pen hand 1','above second card(W) on L17')
inv(1441,'I25','text',"T∩T'=e",'typewriter with pen intersection','L18 right')
inv(1428,'I26','insertion','asterisk note call','pen hand 1','after the comma following e, L18 far right')
inv(1707,'I27','text',"B∩B'",'typewriter with pen intersection','L22')
inv(1864,'I28','insertion','underline below distinguished','pen hand 1','L24')
inv(1959,'I29','deletion','k beneath i in automorphisms','typewriter overprint','L26')
inv(1959,'I30','deletion','extra a in quadruples','typewriter x cancellation','L26')
inv(2078,'M01','margin note',"* NB: N(T)∩N(T') is an extension of (Z/hZ)^* by Z/hZ×Z ... , hence of order hzφ(h)",'pen hand 1','full bottom margin note, across foot of sheet')
inv(2082,'M02','deletion','uncertain (G)/(G with tilde) after final Z','pen hand 1, heavily scribbled','within bottom note')
inv(2117,'M03','insertion','center of G with tilde','pen hand 1','below final Z, connected by short oblique stroke')
inv(2113,'M04','text','hzφ(h)','pen hand 1','below hence of order, bottom right; continuation of M01')
inv(2099,'A01','margin note','21','archive hand; not attributed','bottom-left foliation; comment only')
R['inventory'].sort(key=lambda x:x['_y'])
for x in R['inventory']:x.pop('_y')
reads={
'b01':r'\handwritten{\unsure{Massy} 22. 10. 1969}',
'b02':r'in the \unsure{Maer.|Amer.} Journ.',
'b03':r'on \handwritten{``}\deleted{t}\handwritten{T}he',
'b04':r'...\handwritten{\qclose} and \handwritten{``}Lie group',
'b05':r'on polynom\begin{tikzpicture}[baseline=(letters.base),x=1em,y=1em]\node[inner sep=0pt] (letters) at (0,0) {ai};\handwritten{\draw[line width=.6pt] (-.30,.72) .. controls (-.04,.55) and (-.16,-.55) .. (.19,-.48) .. controls (.34,-.46) and (.44,-.22) .. (.42,-.16);}\end{tikzpicture}l rings\handwritten{\qclose},',
'b06':r'appea\deleted{\unsure{k|r}}\handwritten{r}ed,',
'b07':r'of \deleted{\unsure{a|A}}\handwritten{A}lg. Geometry,',
'b08':r'say) quadr\deleted{\unsure{a|u}}uples $(\mathrm T,\mathrm B,\mathrm T\prime,\mathrm B\prime)$,',
'b09':r'``in apposition\handwritten{\qclose}',
'b10':r'$\operatorname{card}(\mathrm W)^{\handwritten 2}/\mathrm{hz}\handwritten\phi(\mathrm h)$, where $\deleted{\unsure{\mathrm H|\mathrm W}}\handwritten W$ is the Weyl group,',
'b11':r'center\inserted{\handwritten{of $\widetilde G$}}, and',
'b12':r'$\handwritten\phi(\mathrm h)=\operatorname{card}(\underline{\mathrm Z}/\mathrm h\underline{\mathrm Z})^{\handwritten *}$',
'b13':r'a\deleted n \inserted{g\deleted{\unsure{a|e}}enerating} element',
'b14':r'$\mathrm h$ $\mathrm T\handwritten\cap\mathrm N(\mathrm T\prime)$,',
'b15':r'$\operatorname{card}(\mathrm W)^{\handwritten 2}/\mathrm{hz}$',
'b16':r'the stablity subgroup',
'b17':r'$\mathrm T\handwritten\cap\mathrm T\prime=\mathrm e$,\handwritten{\textsuperscript{*}}',
'b18':r'i.e. $\mathrm B\handwritten\cap\mathrm B\prime$ is',
'b19':r'\uline{distinguished}',
'b20':r'automorph\deleted{k}isms',
'b21':r'quadr\deleted{a}uples',
'b22':r'\handwritten{* NB: $N(T)\cap N(T\prime)$ is an extension of $(\mathbb Z/h\mathbb Z)^*$}',
'b23':r'\handwritten{by $\mathbb Z/h\mathbb Z\times\underset{\substack{\tikz[scale=.2]{\draw (0,0)--(.2,.6);}\text{center of }\widetilde G}}Z\deleted{\unsure{(G)|(\widetilde G)}}$,}',
'b24':r'\handwritten{hence of order $hz\varphi(h)$}',
'b25':r'% archive sheet number: 21'
}
# Replace helper escapes used only to keep Python string delimiters clear.
for k,v in list(reads.items()): reads[k]=v.replace(r'\qclose',"''").replace(r'\prime',"'")
kinds={k:'text' for k in reads}
for k in ['b03','b06','b07','b08','b13','b20','b21']:kinds[k]='deletion'
for k in ['b04','b05','b09','b11','b19']:kinds[k]='insertion'
for k in ['b22','b23','b24','b25']:kinds[k]='margin note'
for k,m in M.items():
 x0,y0,x1,y1=m['box'];R['boxes'].append(dict(box=k,kind=kinds[k],x0=x0,y0=y0,x1=x1,y1=y1,reading=reads[k]))
R['reading_notes']=[
'This is an English letter opening, addressed “Dear Kostant,” and dated 22 October 1969. The handwritten place remains uncertain as Massy. There is no author page number or total page count; 21 is the archive foliation.',
'The writer says that Brieskorn’s work on Klein singularities prompted rereading two papers of Kostant, requests later reprints, and proposes reconsidering the work within algebraic geometry. The two paper names are references quoted within the letter, not a title supplied for the sheet.',
'L09–L17 propose classifying quadruples (T,B,T\u2032,B\u2032) in a complex simple adjoint Lie group, with the tori in apposition and the Borel subgroups containing them. The source writes the counts as card(W)^2/hzφ(h) and, after adding a generating element of T∩N(T\u2032), card(W)^2/hz. These assertions are transcribed without checking them or silently changing denominator scope.',
'L18–L19 assert T∩T\u2032=e and describe the resulting structure as rigid up to exterior automorphisms. The text uses the misspelling stablity; it is retained.',
'L20–L26 ask whether some or all such quadruples have opposite Borel subgroups, whether a distinguished conjugacy class exists that is invariant under exterior automorphisms, and what their automorphism groups are. The last question continues beyond this sheet; it is not completed here.',
'The bottom note asserts an extension description for N(T)∩N(T\u2032), involving (Z/hZ)^* and Z/hZ times the central factor, and gives order hzφ(h). The separate annotation “center of G with tilde” is linked to the final Z. The heavily canceled suffix after Z remains uncertain.',
'Source corrections and slips remain visible: doubtful Maer./Amer.; original polynomail plus its transposition mark; suggests number without an added article; extra canceled letters in both quadruples occurrences; an with deleted n; and the corrected title initial. No external bibliography, place information or mathematical proof was used to regularize them.'
]
R['notes']=[
'Whole sheet viewed once for layout; each half viewed once line by line against both C and H. All 25 saved crops were displayed and inspected. No OCR, recognition library, web lookup or TeX compilation was used.',
'Line count is the 26 principal body baselines. The salutation, handwritten place/date and bottom note are separately inventoried. There is no mathematical display or diagram; the transposition stroke is reproduced as a small inline TikZ correction, and the lower note has an annotation leader.',
'H’s introductory note, title attribution and reference to a signature on another sheet are editorial. They are not ink on this page and have not been imported into the candidate or used as evidence from another page.',
'Every visible deletion was inspected: t beneath T; appeared correction; a/A beneath A; first extra a/u in quadruples; H/W beneath W; n of an; proposed underprint in generating; k in automorphisms; last extra a in quadruples; and the scribbled suffix after the final Z in the note.',
'The first-e overprint in generating is a low-confidence proposal. The extra lower-right foot is visible, but repeated e or irregular impression remains an alternative. C and H do not record this state, so the proposal is explicitly marked for root adjudication.',
'The last automorphisms cell exposes a full k arm/leg together with a separate dotted i. C’s k/i uncertainty is resolved to deleted k on crop b20; the final word itself was not used to infer the lower glyph.',
'The canceled bottom-note suffix remains tentative (G)/(G with tilde); the surrounding assertion does not make its letters readable. H’s illegibility mark is not treated as proof of absence of ink.',
'Opening/closing double quotes, operator fonts and equivalent spacing conventions are retained according to the source and preamble; markup equivalence alone is not entered as a textual change. Main-body phi has an oval crossed by an oblique stem; the bottom-note phi is a loop with descender. The retained phi/varphi distinction describes visible forms.',
'Original pixel boxes are unchanged after crop processing. Each box reading specifies the complete target content; adjacent clipped context in the image is for location. B24 was rotated clockwise 6 degrees from its saved crop to make the lower formula upright.',
'No mathematical calculation or proof check was performed or needed to decide a transcription. Assertions and open questions are summarized in reading_notes and are not placed in check_events as verified results.'
]
R['visual_audit_events']=[
 {'statement_id':'022-layout','type':'used and rechecked in this run','outcome':'visual transcription check only: full page and both halves read against both witnesses.'},
 {'statement_id':'022-corrections','type':'used and rechecked in this run','outcome':'visual transcription check only: all additions, deletions, different words, and C doubts inspected on saved crops.'},
 {'statement_id':'022-formulas','type':'used and rechecked in this run','outcome':'visual transcription check only: complete inline formula spans and the bottom-note formulas boxed; no proof or calculation claimed.'}
]
R['notation']=[
'In the Euler formula, Z is a single typewritten capital with a separate underline. Do not substitute mathbb Z for that visibly mechanical construction.',
'The first and second square exponents on card(W) are both handwritten; the first is paler. Both are 2. The unit-group exponent is a handwritten star.',
'Handwritten intersections are small inverted-u arches. The starred note call after e is distinct from the unit-group star.',
'The main-body phi signs are closed ovals with a crossing oblique stem; the bottom-note sign has an open/looped form with descender. C’s phi in the body and varphi in the note are retained as glyph encodings.',
'Footnote Z forms have repeated/parallel pen strokes, compatible with the witnesses’ mathbb Z rendering; the isolated final central-factor Z is plain and is explained by the lower annotation.',
'Source abbreviations Journ., Alg., resp., NB and i.e. are retained. Typed ai order in polynomail is retained with the pen transposition curve, without supplying reordered letters.'
]
R['hand_log']=[
'Typescript letter with one principal pen hand for date/place, quoted-title corrections, mathematical signs, note call and bottom note. Identity is not inferred from a signature not present on this sheet.',
'Generating is typed, with a pen leader. H’s claim that this word is handwritten is contradicted by its matching machine letterforms; this attribution is recorded here rather than counted as a lexical change.',
'Both superscript 2s are handwritten. C marks only the second as handwritten; the candidate marks both. This hand-attribution adjustment does not change the formula’s content.',
'Of G with tilde is a pen insertion. The phi signs, cap signs and footnote star are also pen; ordinary variables and primes elsewhere remain typewritten.',
'Original t is mechanically typed beneath pen T. Appeared, Alg. and the Weyl-group W have mixed or retouched impressions, whose uncertain lower readings are explicitly retained.',
'Archive numeral 21 is a separate bottom-left annotation and is not treated as the letter’s own page number.'
]
R['crop_transforms']=[{'crop':M['b24']['crop'],'box_id':'b24','original_box':M['b24']['box'],'rotation_clockwise_degrees':6,'source':'existing saved crop, no recrop','resampling':'BICUBIC','expanded_canvas':True,'fill':'white','purpose':'upright lower handwritten order formula'}]
R['crop_processing']={'source_size':[1686,2152],'width_pixels':2500,'resize':'LANCZOS','autocontrast_cutoff':0.2,'sharpen':'UnsharpMask radius 1.2 percent 110 threshold 3','displayed_crop_ids':list(M)}
(base/'out/work'/f'{P}_report.json').write_text(json.dumps(R,ensure_ascii=False,indent=2)+'\n')
print('Saved',len(R['changes']),'changes;',len(R['inventory']),'inventory elements;',len(R['boxes']),'boxes;',len(R['doubts']),'open readings.')
