from pathlib import Path
import csv, json, re
R = Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work')
P = R/'packets/145_scan027'
O = R/'edition/reader_reports/145_scan027.json'
C = (P/'C.tex').read_text()
H = (P/'H.tex').read_text()
T = (R/'edition/reader_reports/145_scan027.tex').read_text()
manifest = json.loads((R/'edition/crops/145_scan027_crop_meta.json').read_text())
D = {
 'scan':27, 'reader':'reader_b', 'lines_read':35,
 'layout':'One text sheet in his hand: manuscript number 12 at the top, an opening extension line with an underbrace label and a three-line note at upper right, a fundamental-group display with its own underbrace label, a long paragraph over nineteen further text/formula baselines, six interlinear insertions, cancellations, and manuscript number 26 at lower left. The final paragraph continues at the physical bottom without terminal punctuation. The count of 35 includes 21 main baselines, two page numerals, two underbrace labels, three note lines, the separate struck au dessus des line, and six insertion baselines.',
 'changes':[], 'decisions':[], 'unlisted_decisions':[], 'doubts':[], 'inventory':[],
 'second_boxes':[], 'notation':[], 'hand':[], 'abbreviations':[], 'notes':[],
 'check_events':[], 'diff_coverage':[], 'crop_manifest':manifest,
 'reading_protocol':{'whole_page_views':1,'native_half_views':{'top':1,'bottom':1},'saved_first_reading_crops':14,'ocr_used':False,'external_research_used':False,'tex_compiled':False,'other_page_inputs_read_for_this_assignment':False,'blind_second_reading_performed':False,'blind_exclusion':'reader_b remains excluded from scans025–027 in the blind phase because of the earlier documented TSV-parser exposure; this authorized first reading is not a blind reading.'}
}
def save():
    O.write_text(json.dumps(D, ensure_ascii=False, indent=2)+'\n')
def add(place,c,h,f,ink,confidence,kind,cc,hc,marked,crop,cats,math='',extra=()):
    m=manifest[crop-1]
    row={'id':f's027-{len(D["changes"])+1:02d}','place':place,'C':c,'H':h,'final':f,'ink':ink,'confidence':confidence,'kind':kind,'c_changed':cc,'h_changed':hc,'marked_in_H':marked,'crop':m['crop'],'box':m['box'],'error_category':cats,'math_consequence':math}
    if extra: row['additional_crops']=[manifest[i-1]['crop'] for i in extra]
    D['changes'].append(row)
Sindex = r'\unsure{\mathfrak S|\mathcal S}_{\unsure{[|\{}0,1,\infty]}'
cf = C.split('\\[',1)[1].split('\\]',1)[0].strip()
hf = H.split('\\[',1)[1].split('\\]',1)[0].strip()
tf = T.split('\\[',1)[1].split('\\]',1)[0].strip()
add('Opening extension: delimiters around the three indices of the ornate S',r'\unsure{\mathfrak S_{\{0,1,\infty\}}|\mathcal S_{\{0,1,\infty\}}}',r'\mathfrak{S}_{\{0,1,\infty\}}',Sindex,'The right sign is a nearly straight descending stroke with a leftward foot, hence ]. The left short downstroke and foot favor [, but its top is entangled with the large S flourish; retain a local [|{ alternative. The ornate S alphabet itself remains unresolved.','medium','misread symbol or index',True,True,'no',1,[1],'Preserves the written subscript delimiters without replacing them by conventional set braces.')
add('Fundamental-group display: all three initial Pi letters',cf,hf,tf,'Each of the three letters has a horizontal cap and two substantial descending legs. Their full right legs distinguish them from the nearby Gamma signs with only a short right cap. This row records letter case; the base point and final delimiter are separately audited below.','high','misread symbol or index',True,True,'no',2,[1],'Preserves the capital group notation Π, Π0,3 and Π1.')
add('Fundamental-group display: base point after the last comma',r'-\bar j',r'\ill{}',r'-\bar j','A separate short minus precedes the long j stem and lower left loop; a short horizontal bar stands above that stem. These strokes are all visible.','high',r'readable ink left as \ill{}',False,True,'yes',2,[5],'Restores the written base point -bar j.')
add('Fundamental-group display: right delimiter after the base point',r'-\bar j)',r'\ill{})',r'-\bar j\}','The final delimiter has a middle kink and a leftward lower foot, unlike the broad opening parenthesis preceding P. The literal closing brace is retained even though the opening delimiter is a parenthesis.','high','misread symbol or index',True,True,'yes',2,[1],'Leaves the authorial mismatch of opening parenthesis and closing brace visible.')
add('After conjugaison: the cancelled interlinear phrase',r'\deleted{\unsure{au dessus des}}',r'\struck{\uncertain{au-dessus}}',r'\deleted{\unsure{au dessus des}}','The line contains an initial au, a longer dessus, and a separate final des-shaped group. The strike and the descender of conjugaison entangle some letters, so the whole cancelled phrase remains doubtful. No separate hyphen is visible between au and dessus.','medium','omission',False,True,'yes',3,[3,8])
add('After et and before aux comp.: inserted parenthetical word',r'\inserted{(éventuelles)}',r'(\uncertain{éventuellement})',r'\inserted{(éventuelles)}','The ending has two tall l strokes followed by a short es-shaped ending; there is no ment cluster. The surrounding parentheses are visible. A long insertion curve brings the phrase down before aux.','high','misread word',False,True,'yes',4,[2,6])
add('Invariant list: cancelled sign before the first tau',r'\deleted{\unsure{\dot\rho}}\tau',r'\dot\rho\tau',r'\deleted{\unsure{\dot\rho}}\tau','The rho-shaped descender is traversed by dense cancellation strokes, with additional zigzags above and to the right. The underlying body and any separate dot cannot all be isolated; retain the whole C doubt, but record the cancellation state. The following tau is live.','medium','deletion state',False,True,'no',5,[7],'The preferred live list begins with tau alone; the cancelled prefix remains visible and doubtful.')
add('Les pts fixes de rho: absence of over-dot on the live rho',r'Les pts fixes de $\rho$',r'Les pts fixes de $\dot\rho$',r'Les pts fixes de $\rho$','The large rho has an open upper loop and a long descender, with clear white space above its loop. The nearby inserted word is to its right, not an over-dot.','high','misread symbol or index',False,True,'no',6,[1],'Preserves the undotted rho of this occurrence.')
add('Between rho and P: inserted sont',r'\inserted{\unsure{sont}}',r'\uncertain{sont}',r'\inserted{\unsure{sont}}','The small word is above the baseline after rho, with compressed initial and middle strokes and a conspicuous final crossing. Its placement is an insertion; its complete letter sequence remains doubtful.','medium','insertion or placement',False,True,'yes',6,[6])
add('After ordre 6: insertion savoir phi(S3)',r'\inserted{savoir $\varphi(\unsure{\mathfrak S_3|\mathcal S_3})$}',r'(savoir $\varphi(\mathfrak{S}_3)$)',r'\inserted{savoir $\varphi(\unsure{\mathfrak S_3|\mathcal S_3})$}','Savoir and phi(S3) occupy a separate line above ordre 6. The long lower insertion bracket turns down after the numeral and its comma. There is only the pair of parentheses belonging to phi; no additional outer pair encloses savoir. H places the phrase before P instead.','high','insertion or placement',False,True,'no',6,[6,9])
add('P et Pbar dont ... formé de ...: H outer parentheses',r'$P$ et $\bar P$ dont le stabilisateur est d\'ordre $6$, \inserted{savoir $\varphi(\unsure{\mathfrak S_3|\mathcal S_3})$} formé de $1,\dot\rho,\dot\rho^2,\dot\sigma_1\tau,\dot\sigma_2\tau,\dot\sigma_3\tau$.',r'$P$ et $\overline{P}$ (dont le stabilisateur est d\'ordre 6, formé de $1, \dot\rho, \dot\rho^2, \dot\sigma_0\tau, \dot\sigma_1\tau, \dot\sigma_\infty\tau$).',r'$P$ et $\bar P$ dont le stabilisateur est d\'ordre $6$, \inserted{savoir $\varphi(\unsure{\mathfrak S_3|\mathcal S_3})$} formé de $1,\dot\rho,\dot\rho^2,\dot\sigma_1\tau,\dot\sigma_2\tau,\dot\sigma_3\tau$.','No opening parenthesis stands between Pbar and dont. At the end of the six-element list there is a dot, with no closing parenthesis. The long curve above ordre 6 is the insertion bracket for savoir, not a parenthesis enclosing this prose. This row concerns the supplied outer parentheses; the indices are separately audited.','high','text not on the page',False,True,'no',7,[9],extra=(6,))
add('Stabilizer list after formé de: three sigma indices',r'1,\dot\rho,\dot\rho^2,\dot\sigma_1\tau,\dot\sigma_2\tau,\dot\sigma_3\tau',r'1, \dot\rho, \dot\rho^2, \dot\sigma_0\tau, \dot\sigma_1\tau, \dot\sigma_\infty\tau',r'1,\dot\rho,\dot\rho^2,\dot\sigma_1\tau,\dot\sigma_2\tau,\dot\sigma_3\tau','The first subscript is an upright 1, the second is a curved 2, and the third has the two curved lobes of 3. All three sigma over-dots are separate and visible. The two preceding rho over-dots are also visible.','high','misread symbol or index',False,True,'no',7,[1],'Retains the written indices 1,2,3 despite the 0,1,infinity convention used elsewhere on this same sheet.')
add('Relèvement correspondant: inserted à P and following punctuation',r'correspondant \inserted{à $P$} (de $\varphi(\unsure{\mathfrak S_3|\mathcal S_3})$), on trouve',r'correspondant (de $\varphi(\mathfrak{S}_3)$) : $P$ ; on trouve',r'correspondant \inserted{à $P$} (de $\varphi(\unsure{\mathfrak S_3|\mathcal S_3})$), on trouve','Above the opening parenthesis there are the small accented a body and P; their insertion curve returns after correspondant. A comma follows the closing parenthesis of de phi(S3). The accented a is not a colon and the comma is not a semicolon.','high','insertion or placement',False,True,'no',7,[6,9])
add('Parenthetical Pi-conjugués: the group letter',r'$\pi$-conjugués',r'\uncertain{$\pi$-conjugués}',r'$\unsure{\Pi|\pi}$-conjugués','The letter has a horizontal cap and two full descending legs, favoring capital Pi as in the opening display. The feet and lower crossings are heavily retraced, so a local lower-case alternative remains. The large oblique stroke beneath conjugués is the g descender, not an underline.','medium','misread symbol or index',True,True,'yes',8,[1],'Preserves the preferred capital group letter with a local case doubt.')
add('Entre eux: insertion at end of the conjugacy parenthesis',r'\inserted{entre eux}',r'\uncertain{entre eux}',r'\inserted{entre eux}','The two words stand above the end of conjugués. A hooked insertion line leads to the space immediately before the closing parenthesis; it does not place the words after on trouve.','high','insertion or placement',False,True,'yes',8,[6])
add('After relatifs à Pbar: comma before s\'obtiennent',r'$\bar P$,',r'$\overline{P}$',r'$\bar P$,','A separate dark comma lies after Pbar and before the initial s and apostrophe of s\'obtiennent.','high','omission',False,True,'no',9,[3])
add('Cancelled conj: absence of a separate abbreviation stop',r'\deleted{\unsure{conj.}}',r'\struck{conj}',r'\deleted{\unsure{conj}}','The strike runs through the middle letters. The initial co and the final descending j-shaped stroke favor conj, but not every letter is plain. No independent stop follows the cancelled group before prenant.','medium','text not on the page',True,False,'no',9,[9])
add('First élémt, after prenant un',r'élémt',r'élément',r'élémt','The compact word retains the abbreviated middle and final t; it does not contain the complete ment sequence of élément. The uppermost strokes meet the crop09 edge; the overlapping saved crop08 and the already-read native half supply those same source strokes.','high','abbreviation expanded or spelling modernised',False,True,'no',9,[8],extra=(8,))
add('After E: cancelled qui before the live qui',r'\deleted{\unsure{qui}}',r'\struck{\ill{}}',r'\deleted{\unsure{qui}}','A q-like loop and descending stroke remain amid retraced small strokes. These support qui provisionally, but the inner letters cannot all be separated from the cancellation. The following live qui is distinct.','medium',r'readable ink left as \ill{}',False,True,'yes',10,[5])
add('Live au dessus, after the doubtful soit',r'au dessus',r'au-dessus',r'au dessus','There is open space between au and dessus and no connecting hyphen.','high','abbreviation expanded or spelling modernised',False,True,'no',10,[8])
add('Second élémt, after d\'un',r'élémt',r'élément',r'élémt','The same compressed abbreviated form ends with a t stroke; no full ment cluster is visible. Its upper edge is covered by the overlapping saved crop09, together with crop10 and the already-read native half.','high','abbreviation expanded or spelling modernised',False,True,'no',10,[8],extra=(9,))
add('After cet élément: no stop and lower-case on',r'cet élément. On peut',r'cet élément. On peut',r'cet élément on peut','The space after the final t of élément is blank. The next line begins with a small o whose height matches the following n, unlike the distinctly taller O in On a étudié and On a un relèvement on this page.','high','text not on the page',True,True,'no',11,[9,10])
add('After prendre: cancelled two-symbol formula',r'\deleted{$\unsure{\sigma_0,\tau}$}',r'\struck{\ill{}}',r'\deleted{$\unsure{\sigma_0,\tau}$}','A capped sigma-like first body, a low dark index mass, a comma-shaped stroke and a tau-like second body remain under crossing lines. The index and parts of both bodies are occluded, so the entire formula remains doubtful.','low',r'readable ink left as \ill{}',False,True,'yes',11,[5])
add('Before produits: one retraced les, no separate extra cancelled token',r'les',r'\struck{\ill{}} les',r'\unsure{les}','There is one continuous l-e-s word. Its last s has dense retracing or possible rewriting, but no distinct earlier token can be isolated before it. Keep the local surface-state doubt on this single les; do not manufacture a second inscription.','medium','text not on the page',False,True,'yes',12,[9])
add('After par and before rho: cancelled tau-shaped group',r'\deleted{\unsure{$\tau$}}',r'\struck{\ill{}}',r'\deleted{\unsure{$\tau$}}','The group has a left curl, a long dark crossing/bar, and a short right downturn. Tau is a tentative recovery; the crossing prevents complete separation of the original body from the cancelling stroke.','low',r'readable ink left as \ill{}',False,True,'yes',12,[5])
add('After rho squared: continuation dots and final stop',r'\ldots','….',r'\ldots.','Three small closely spaced dots are followed by a separate, larger final dot farther to the right.','high','omission',True,False,'no',12,[3])
add('Opening of final paragraph: Le with cancelled terminal s and inserted seul',r'\unsure{Le|Les} \inserted{seul}',r'Le \add{seul} \struck{les}',r'Le\deleted{\unsure{s}} \inserted{seul}','The large L and light e remain live. Cancellation ink occupies the terminal s position; the small underlying form is not fully separable. Seul is clearly interlinear above the gap before pt. There is no second complete les after seul.','medium','deletion state',True,True,'no',13,[7,9])
add('Final paragraph: pt with cancelled s',r'\unsure{pts|pt}',r'pt\struck{s}',r'pt\deleted{\unsure{s}}','The p and tall t remain live. A short lower s-shaped group is crossed and retraced at the end; retain doubt on that underlying cancelled letter rather than flattening the correction to a live pts or an unmarked pt.','medium','deletion state',True,False,'no',13,[7])
add('Lower-left handwritten page numeral',r'\mspage{26}','',r'\mspage{26}','The lower-left inscription consists of a curved 2 followed by a closed-loop 6. It is a handwritten page number, separate from the final text line.','high','omission',False,True,'no',14,[3])
save()
print('Checkpoint:',len(D['changes']),'changes saved to',O)

def decide(identifier,decision,reading,ink,crop,confidence,source_mark=None):
    m=manifest[crop-1]
    row={'id':identifier,'decision':decision,'reading':reading,'ink':ink,'crop':m['crop'],'box':m['box'],'confidence':confidence}
    if source_mark is None: D['decisions'].append(row)
    else:
        row['source_mark']=source_mark
        D['unlisted_decisions'].append(row)
decide('M0868','undecided',Sindex,'The multi-loop S form cannot distinguish the two conventional alphabet labels. The subscript right delimiter is bracket-shaped; the short left delimiter is partly merged with the S flourish and retains its own local [|{ doubt.',1,'medium')
decide('M0869','undecided',r'\unsure{\mathfrak S_3|\mathcal S_3}','The underbrace label has a looped ornamental S with a clear small 3. Its particular pen form does not settle the typographical alphabet.',1,'medium')
decide('M0870','undecided',r'\unsure{sont}','The inserted small word has compressed initial/middle strokes and a large terminal crossing; sont remains plausible, but all four letters are not independently plain.',6,'medium')
decide('M0871','undecided',r'\unsure{\mathfrak S_3|\mathcal S_3}','The S within inserted phi(S3) has a low loop and an upper sweep. The numeral 3 and parentheses are clear, but the alphabet distinction is not.',6,'medium')
decide('M0872','undecided',r'\unsure{\mathfrak S_3|\mathcal S_3}','The S in de phi(S3) has a broad upper loop and a lower return, without a decisive graphic distinction between the two font labels.',7,'medium')
decide('M0873','undecided',r'\unsure{soit|sont}','The first part is retraced. A small middle upright favors soit, but the compressed connected middle can also be read as the n of sont; the final t-shaped crossing is clearer.',10,'low')
decide('M0874','other',r'Le\deleted{\unsure{s}}','L and e remain live. A short terminal letter is cancelled, rather than an uncorrected plural Les; its underlying s is still entangled with the dark stroke. Seul is separately inserted above the following space.',13,'medium')
decide('M0875','other',r'pt\deleted{\unsure{s}}','The p and tall t remain live, followed by a low crossed/retraced final letter in the s position. The correction state is visible, while the original s contour is not fully separate.',13,'medium')
decide('U027-01','undecided',r'\deleted{\unsure{au dessus des}}','The apparent three words remain intersected by the strike and the descender from conjugaison. The final des-shaped group is present, but the whole cancelled phrase cannot be cleared.',3,'medium',r'\unsure{au dessus des}')
decide('U027-02','undecided',r'\deleted{\unsure{\dot\rho}}','The rho-like descender is visible, but the upper body and any dot are merged with cancelling zigzags. Do not recover additional symbols from those over-strokes.',5,'low',r'\unsure{\dot\rho}')
decide('U027-03','undecided',r'\deleted{\unsure{conj}}','Initial co and a final descending j-like stroke support conj, with inner letters still occluded. The C stop is removed because no independent dot follows the group.',9,'medium',r'\unsure{conj.}')
decide('U027-04','undecided',r'\deleted{\unsure{qui}}','A q-like loop/descender and compressed following strokes suggest qui; the internal strokes remain crossed and retraced.',10,'medium',r'\unsure{qui}')
decide('U027-05','undecided',r'\deleted{$\unsure{\sigma_0,\tau}$}','The two bodies and intervening comma are only partly recoverable. In particular the low index mass cannot be separated from the strike, so uncertainty covers the whole cancelled formula.',11,'low',r'\unsure{\sigma_0,\tau}')
decide('U027-06','undecided',r'\deleted{\unsure{$\tau$}}','A tau-shaped bar and turn are plausible, but cancellation is superposed on the same strokes. The complete underlying symbol is not plain.',12,'low',r'\unsure{$\tau$}')

def doubt(place,reading,alts,confidence,reason,crop):
    D['doubts'].append({'place':place,'reading':reading,'alternatives':alts,'confidence':confidence,'reason':reason,'crop':manifest[crop-1]['crop']})
doubt('Opening ornate S alphabet',r'\unsure{\mathfrak S|\mathcal S}',[r'\mathfrak S',r'\mathcal S'],'medium','The pen form is ornate and looped; assigning a typographical alphabet would go beyond the distinguishable ink.',1)
doubt('Opening S subscript left delimiter',r'\unsure{[|\{}',[r'[',r'\{'],'medium','The short downstroke and foot favor a bracket, but its top is partly entangled with the S flourish. The right delimiter is clearly ].',1)
doubt('Underbrace S3 alphabet',r'\unsure{\mathfrak S_3|\mathcal S_3}',[r'\mathfrak S_3',r'\mathcal S_3'],'medium','The small ornamental S form is compatible with both alphabet labels.',1)
doubt('Cancelled phrase after conjugaison',r'\deleted{\unsure{au dessus des}}',['au dessus des','partly unrecovered cancelled wording'],'medium','The strike and a descender cross the central and final letters; the whole phrase therefore remains doubtful.',3)
doubt('Cancelled sign before first invariant-list tau',r'\deleted{\unsure{\dot\rho}}',[r'\dot\rho','partly unrecovered cancelled sign'],'low','The apparent rho and its possible dot cannot be completely separated from the over-strokes.',5)
doubt('Inserted sont after live rho',r'\unsure{sont}',['sont','unresolved compressed inserted word'],'medium','Compressed middle strokes and a large final crossing prevent a fully certain lexical reading.',6)
doubt('Inserted savoir phi(S3): S alphabet',r'\unsure{\mathfrak S_3|\mathcal S_3}',[r'\mathfrak S_3',r'\mathcal S_3'],'medium','The pen form does not decide the alphabet; insertion placement and numeral are clear.',6)
doubt('De phi(S3): S alphabet',r'\unsure{\mathfrak S_3|\mathcal S_3}',[r'\mathfrak S_3',r'\mathcal S_3'],'medium','The broad ornamental S cannot settle the conventional alphabet name.',7)
doubt('Pi in Pi-conjugués',r'\unsure{\Pi|\pi}',[r'\Pi',r'\pi'],'medium','The cap and two legs favor capital Pi, but the retraced lower strokes leave case locally uncertain.',8)
doubt('Cancelled conj',r'\deleted{\unsure{conj}}',['conj','partly unrecovered cancelled abbreviation'],'medium','The inner strokes remain covered; no final abbreviation stop is independently visible.',9)
doubt('Cancelled qui after E',r'\deleted{\unsure{qui}}',['qui','partly unrecovered cancelled word'],'medium','The q-like loop and descender are suggestive, but the following strokes are entangled.',10)
doubt('Live soit/sont after qui',r'\unsure{soit|sont}',['soit','sont'],'low','The middle upright/connection is retraced and does not decide i versus n.',10)
doubt('Cancelled sigma0,tau formula after prendre',r'\deleted{$\unsure{\sigma_0,\tau}$}',[r'\sigma_0,\tau','partly unrecovered cancelled two-symbol formula'],'low','Both symbols and especially the first index are crossed; uncertainty is retained over the complete formula.',11)
doubt('Les before produits: final-letter surface state',r'\unsure{les}',['les with retraced final s','les with a cancelled/re-written final s'],'medium','Only one word is visible. The dense final s does not separate retracing from a local rewrite; it does not support an additional preceding cancelled token.',12)
doubt('Cancelled tau before rho',r'\deleted{\unsure{$\tau$}}',[r'\tau','partly unrecovered cancelled sign'],'low','The underlying bar and turn overlap the cancellation.',12)
doubt('Cancelled terminal s after Le',r'Le\deleted{\unsure{s}}',['Le with cancelled s','Le with a partly unrecovered cancelled terminal letter'],'medium','The cancellation occupies the terminal-s position, but the original small contour is entangled.',13)
doubt('Cancelled s after pt',r'pt\deleted{\unsure{s}}',['pt with cancelled s','pt with a partly unrecovered cancelled final letter'],'medium','The live p and t are clear; the crossed final small letter is not fully recoverable.',13)
save()
print('Checkpoint:',len(D['decisions']),'listed and',len(D['unlisted_decisions']),'unlisted decisions;',len(D['doubts']),'doubts')

def inv(kind,position,objects,box):
    row={'element':f'E{len(D["inventory"])+1:02d}','kind':kind,'position':position,'first_words_or_objects':objects,'box':box,'sheet_kind':'text','hand':'his hand','transcribed':'yes'}
    D['inventory'].append(row)
inv('text','Top centre','12',[760,28,823,76])
inv('text','Opening main baseline',r"L'extension $\mathcal E=\mathcal E_{0,3}$ de $\Gamma=\Gamma_{0,3}$",[281,83,1608,206])
inv('margin note','Below the ornate S in the opening line',r'Underbrace and $=\unsure{\mathfrak S_3|\mathcal S_3}$',[1188,177,1379,246])
inv('margin note','Upper right, below Z/2Z, three short lines',r'engendré par $\tau:\ z\mapsto\bar z$',[1418,162,1602,283])
inv('display','Second main baseline, preceded at left by par',tf,[278,244,1645,354])
inv('margin note','Under the punctured projective-line expression',r'Underbrace and $U=U_{0,3}$',[1244,350,1472,412])
inv('text','Main prose baseline 1','Les classes de conjugaison ... de scindages partiels',[277,397,1648,500])
inv('deletion','Below conjugaison',r'\deleted{\unsure{au dessus des}}',[609,460,976,511])
inv('text','Main prose baseline 2','maximaux correspondent aux points fixes de',[277,486,1644,596])
inv('insertion','Above aux comp., with long return curve',r'\inserted{(éventuelles)}',[1174,552,1518,649])
inv('text','Main prose baseline 3',r'$\dot\rho,\dot\sigma_0,\dot\sigma_1,\dot\sigma_\infty$ opérant sur $X_{0,3}$, et aux comp.',[280,601,1571,714])
inv('text','Main prose baseline 4',"connexes des ens. d'invariants de",[274,704,1320,801])
inv('text','Main prose baseline 5',r'$\deleted{\unsure{\dot\rho}}\tau,\dot\sigma_0\tau,\dot\sigma_1\tau,\dot\sigma_\infty\tau$. Les pts fixes de $\rho$',[268,793,1627,923])
inv('deletion','At the start of the invariant list',r'\deleted{\unsure{\dot\rho}}',[278,829,349,915])
inv('insertion','Above and just to the right of the live rho',r'\inserted{\unsure{sont}}',[1406,779,1518,835])
inv('insertion','Above ordre 6, attached by a large downturned bracket',r'\inserted{savoir $\varphi(\unsure{\mathfrak S_3|\mathcal S_3})$}',[1340,811,1624,933])
inv('text','Main prose baseline 6',r'$P$ et $\bar P$ dont le stabilisateur est d\'ordre $6$,',[276,890,1513,999])
inv('text','Main prose baseline 7',r'formé de $1,\dot\rho,\dot\rho^2,\dot\sigma_1\tau,\dot\sigma_2\tau,\dot\sigma_3\tau$. On a étudié',[275,976,1640,1111])
inv('insertion','Above the gap between correspondant and its parenthesis',r'\inserted{à $P$}',[969,1066,1059,1137])
inv('text','Main prose baseline 8',r'le relèvement correspondant (de $\varphi(\unsure{\mathfrak S_3|\mathcal S_3})$), on trouve',[274,1080,1644,1185])
inv('insertion','Above the end of conjugués; hook before closing parenthesis',r'\inserted{entre eux}',[1037,1143,1262,1244])
inv('text','Main prose baseline 9',r'des relèvements ($\unsure{\Pi|\pi}$-conjugués \inserted{entre eux}) relatifs à',[275,1173,1553,1300])
inv('text','Main prose baseline 10',r'$\bar P$, s\'obtiennent en \deleted{\unsure{conj}} prenant un élémt de',[275,1274,1634,1412])
inv('deletion','Between en and prenant',r'\deleted{\unsure{conj}}',[833,1321,985,1397])
inv('text','Main prose baseline 11',r'$\mathcal E$ \deleted{\unsure{qui}} qui \unsure{soit|sont} au dessus d\'un élémt de',[278,1390,1608,1525])
inv('deletion','Between E and the live qui',r'\deleted{\unsure{qui}}',[391,1453,452,1525])
inv('text','Main prose baseline 12',r'$\Gamma$ envoyant $P$ en $\bar P$ (savoir $\dot\sigma_0,\dot\sigma_1,\dot\sigma_\infty,\tau,\tau\rho,\tau\rho^2$)',[278,1503,1648,1635])
inv('text','Main prose baseline 13','et en conjuguant par cet élément',[276,1623,1330,1757])
inv('text','Main prose baseline 14',r'on peut donc prendre \deleted{$\unsure{\sigma_0,\tau}$} un des élé-',[278,1718,1640,1865])
inv('deletion','Between prendre and un des',r'\deleted{$\unsure{\sigma_0,\tau}$}',[1011,1752,1135,1811])
inv('text','Main prose baseline 15',r'ments $\sigma_0,\sigma_1,\sigma_\infty$ (ou $\varepsilon_0,\varepsilon_1,\varepsilon_\infty$) ou $\tau_0,\tau_1,\tau_\infty$ ou',[268,1846,1645,1973])
inv('text','Main prose baseline 16',r'\unsure{les} produits des précédents par \deleted{\unsure{$\tau$}} $\rho$ ou $\rho^2$\ldots.',[270,1934,1645,2074])
inv('text','Start of baseline 16: retraced final s in one word',r'\unsure{les}',[278,1984,407,2066])
inv('deletion','Between par and rho',r'\deleted{\unsure{$\tau$}}',[1208,1958,1305,2016])
inv('text','Final paragraph baseline 1',r'Le\deleted{\unsure{s}} \inserted{seul} pt\deleted{\unsure{s}} fixe de $\sigma_0$ est $2$, dont le',[270,2048,1459,2172])
inv('deletion','Final paragraph: terminal letter after Le',r'\deleted{\unsure{s}}',[315,2114,365,2171])
inv('insertion','Above the gap between corrected Le and pt',r'\inserted{seul}',[340,2070,436,2133])
inv('deletion','Final paragraph: final letter after pt',r'\deleted{\unsure{s}}',[470,2103,512,2149])
inv('text','Final paragraph baseline 2',r'stabilisateur est le groupe $\simeq\mathbb Z/2\times\mathbb Z/2$ engendré',[276,2143,1649,2269])
inv('text','Final paragraph baseline 3',r'par $\sigma_0$ et $\tau$. On a un relèvement de ce sous-groupe',[272,2237,1655,2343])
inv('text','Lower left, separate from final baseline','26',[38,2279,124,2343])
save()
print('Checkpoint:',len(D['inventory']),'inventory elements saved')

def second(kind,coords,reading):
    D['second_boxes'].append({'box':f'B{len(D["second_boxes"])+1:02d}','kind':kind,'coords':coords,'reading':reading})
opening = T[T.index("L'extension"):T.index('Les classes')].strip()
second('Handwritten top page number',[760,28,823,76],r'\mspage{12}')
second('Complete opening formulas, all indices and numerals, uncertain S alphabets/delimiter, both underbrace labels, upper-right marginal note, capital Pi, base point and unmatched final brace',[278,82,1645,414],opening)
second('Whole cancelled phrase and complete containing source line; lexical discrepancy au dessus des',[274,397,1648,516],r'Les classes de conjugaison \deleted{\unsure{au dessus des}} de scindages partiels')
second('Inserted éventuelles; full fixed-point list and X0,3 formula; complete intervening prose',[269,486,1645,804],r"maximaux correspondent aux points fixes de $\dot\rho,\dot\sigma_0,\dot\sigma_1,\dot\sigma_\infty$ opérant sur $X_{0,3}$, et \inserted{(éventuelles)} aux comp. connexes des ens. d'invariants de")
second('Whole invariant list containing the cancelled doubtful rho; undotted live rho; doubtful sont and savoir insertions; P/Pbar, numeral6 and complete phi(S3) formula',[268,779,1632,1000],r"$\deleted{\unsure{\dot\rho}}\tau,\dot\sigma_0\tau,\dot\sigma_1\tau,\dot\sigma_\infty\tau$. Les pts fixes de $\rho$ \inserted{\unsure{sont}} $P$ et $\bar P$ dont le stabilisateur est d'ordre $6$, \inserted{savoir $\varphi(\unsure{\mathfrak S_3|\mathcal S_3})$}")
second('Complete six-element stabilizer formula and indices 1,2,3; inserted à P; entire doubtful phi(S3) and Pi-conjugués expressions; entre eux insertion and full source context',[272,976,1648,1301],r'formé de $1,\dot\rho,\dot\rho^2,\dot\sigma_1\tau,\dot\sigma_2\tau,\dot\sigma_3\tau$. On a étudié le relèvement correspondant \inserted{à $P$} (de $\varphi(\unsure{\mathfrak S_3|\mathcal S_3})$), on trouve des relèvements ($\unsure{\Pi|\pi}$-conjugués \inserted{entre eux}) relatifs à')
second('Pbar comma; cancelled conj and qui; both élémt abbreviations and au dessus lexical differences; unresolved soit/sont; all complete element formulas and source prose',[274,1274,1648,1635],r"$\bar P$, s'obtiennent en \deleted{\unsure{conj}} prenant un élémt de $\mathcal E$ \deleted{\unsure{qui}} qui \unsure{soit|sont} au dessus d'un élémt de $\Gamma$ envoyant $P$ en $\bar P$ (savoir $\dot\sigma_0,\dot\sigma_1,\dot\sigma_\infty,\tau,\tau\rho,\tau\rho^2$)")
second('No stop before lower-case on; whole cancelled sigma0,tau formula; full live sigma, epsilon and tau lists with every index; complete source prose across the line-break word éléments',[268,1623,1648,1973],r'et en conjuguant par cet élément on peut donc prendre \deleted{$\unsure{\sigma_0,\tau}$} un des éléments $\sigma_0,\sigma_1,\sigma_\infty$ (ou $\varepsilon_0,\varepsilon_1,\varepsilon_\infty$) ou $\tau_0,\tau_1,\tau_\infty$ ou')
second('One retraced les; whole cancelled tau and complete rho/rho2 alternative; all four terminal dots',[270,1934,1646,2074],r'\unsure{les} produits des précédents par \deleted{\unsure{$\tau$}} $\rho$ ou $\rho^2$\ldots.')
second('Full final paragraph: Le and pt cancellations, inserted seul, both sigma0 occurrences, numeral2, complete Z/2 times Z/2 formula and tau; continuation without terminal stop',[264,2048,1655,2344],r'Le\deleted{\unsure{s}} \inserted{seul} pt\deleted{\unsure{s}} fixe de $\sigma_0$ est $2$, dont le stabilisateur est le groupe $\simeq\mathbb Z/2\times\mathbb Z/2$ engendré par $\sigma_0$ et $\tau$. On a un relèvement de ce sous-groupe')
second('Handwritten lower page number',[38,2279,124,2343],r'\mspage{26}')

def macros(text,name):
    out=[]
    for m in re.finditer(r'\\'+name+r'\{',text):
        depth=1; i=m.end()
        while i<len(text) and depth:
            if text[i]=='\\':
                if i+1<len(text) and text[i+1] in '{}': i+=2; continue
            if text[i]=='{': depth+=1
            elif text[i]=='}': depth-=1
            i+=1
        if depth: raise ValueError((name,m.start(),'unbalanced'))
        out.append(text[m.start():i])
    return out
mapping={
 'deleted': [('E08','B03',r'\deleted{\unsure{au dessus des}}',3),('E14','B05',r'\deleted{\unsure{\dot\rho}}',5),('E24','B07',r'\deleted{\unsure{conj}}',9),('E26','B07',r'\deleted{\unsure{qui}}',10),('E30','B08',r'\deleted{$\unsure{\sigma_0,\tau}$}',11),('E34','B09',r'\deleted{\unsure{$\tau$}}',12)],
 'inserted':[('E10','B04',r'\inserted{(éventuelles)}',4),('E15','B05',r'\inserted{\unsure{sont}}',6),('E16','B05',r'\inserted{savoir $\varphi(\unsure{\mathfrak S_3|\mathcal S_3})$}',6),('E19','B06',r'\inserted{à $P$}',7),('E21','B06',r'\inserted{entre eux}',8),('E37','B10',r'\inserted{seul}',13)]
}
audit={'source_counts':{},'items':[],'newly_recorded_cancellations':[{'element':'E36','second_box':'B10','reading':r'Le\deleted{\unsure{s}}'},{'element':'E38','second_box':'B10','reading':r'pt\deleted{\unsure{s}}'}]}
for name in ('deleted','inserted'):
    found=macros(C,name)
    audit['source_counts'][name]=len(found)
    assert len(found)==len(mapping[name])
    for n,(source,(el,bx,reading,cr)) in enumerate(zip(found,mapping[name]),1):
        audit['items'].append({'kind':name,'ordinal':n,'source_span':source,'inventory_element':el,'second_box':bx,'reading':reading,'crop':manifest[cr-1]['crop'],'accounted_for':True})
D['c_markup_audit']=audit
save()
print('Checkpoint:',len(D['second_boxes']),'complete second-reading selections and all',len(audit['items']),'C markup spans saved')

D['notation']=[
 {'observation':'The three group letters in the opening display have full horizontal caps and two descending legs and are transcribed as capital Pi. The same case is preferred, with a local doubt, in Pi-conjugués.','places':['opening display','Pi-conjugués'],'qualification':'The fourth occurrence is retraced, so its capital/lower-case distinction remains explicitly open.'},
 {'observation':'The Gamma letters in the extension and before envoyant have a long left leg and only a short right cap, distinct from the full right legs of the opening Pi signs.','places':['opening extension','Gamma envoyant P en Pbar'],'qualification':'This observation is confined to these visible forms on this sheet.'},
 {'observation':'The ornate S forms remain represented by mathfrak-S/mathcal-S alternatives. The opening subscript has a clear right square bracket and a bracket-first, curly-brace alternative at left.','places':['opening S','underbrace S3','inserted savoir phi(S3)','de phi(S3)'],'qualification':'No alphabet is chosen solely because the group is conventionally a symmetric group.'},
 {'observation':'Over-dots are individually visible on rho and all three sigmas in the initial fixed-point list, on the three live sigmas in the invariant list, on both rhos and three sigmas in the stabilizer list, and on the three sigmas in the later savoir list. The rho before inserted sont is undotted.','places':['fixed-point list','invariant list','Les pts fixes de rho','stabilizer list','later savoir list'],'qualification':'The dot on the cancelled first rho is not independently recoverable; it remains within the cancelled whole-sign doubt.'},
 {'observation':'The stabilizer list literally writes sigma indices 1,2,3, whereas the later list and the live lift choices use 0,1,infinity.','places':['formé de six-element list','savoir list after Pbar','on peut donc prendre choices'],'qualification':'The difference is recorded as written, without replacing indices from mathematical expectations.'},
 {'observation':'The fundamental-group expression ends with a right brace even though its opening delimiter is a parenthesis. The base point is -bar j. Both underbrace labels, =S3 and U=U0,3, are present.','places':['fundamental-group display','two opening underbrace labels'],'qualification':'The unmatched delimiter is retained literally; the U label is legible despite its retraced second U.'},
 {'observation':'The terminal continuation after rho squared contains three small adjacent dots and a separate larger final stop.','places':['end of the long paragraph'],'qualification':'It is represented by \\ldots. rather than reduced to three dots.'}
]
D['hand']=[
 {'observation':'Large returning curves mark insertion placement.','affected_places':['éventuelles before aux','savoir after ordre6','àP before the parenthesis','entre eux before the closing conjugacy parenthesis'],'universal_on_page':False,'witness_misreadings_caused':'H relocates savoir, àP and entre eux; some insertion curves are liable to be taken for prose parentheses.'},
 {'observation':'The initial O of the two clear On a clauses is distinctly taller than the small o of on peut.','affected_places':['On a étudié','on peut donc prendre','On a un relèvement'],'universal_on_page':False,'witness_misreadings_caused':'Both witnesses supplied a stop and upper-case On at on peut, although neither feature is supported there.'},
 {'observation':'Long descenders can traverse neighboring text or extend obliquely beneath a word.','affected_places':['conjugaison above the cancelled phrase','g of conjugués'],'universal_on_page':False,'witness_misreadings_caused':'The conjugaison descender complicates recovery of the struck wording; the conjugués descender is not an underline.'},
 {'observation':'Cancellation and retracing sometimes occupy the same strokes as the original letter or symbol.','affected_places':['cancelled rho','cancelled qui','cancelled sigma0,tau','cancelled tau','terminal s of les before produits','cancelled s after Le and pt'],'universal_on_page':False,'witness_misreadings_caused':'H leaves several recoverable outlines wholly illegible and posits an extra struck token before les; C flattens the last two singular corrections into alternatives.'},
 {'observation':'The handwritten abbreviations élémt, comp., ens. and pts are compact, with selective stops.','affected_places':['both élémt occurrences','comp. connexes','ens. d’invariants','Les pts fixes'],'universal_on_page':False,'witness_misreadings_caused':'H expands both élémt occurrences to élément. No uniform punctuation is inferred for the cancelled conj.'}
]
D['abbreviations']=[
 {'form':'comp.','expansion':'composantes','place':'aux comp. connexes'},
 {'form':'ens.','expansion':'ensembles','place':"des ens. d'invariants"},
 {'form':'pts','expansion':'points','place':'Les pts fixes de rho'},
 {'form':'élémt','expansion':'élément','place':'prenant un élémt de E'},
 {'form':'élémt','expansion':'élément','place':"d'un élémt de Gamma"},
 {'form':'conj (cancelled and doubtful)','expansion':'conjuguant (probable, not inserted into the text)','place':'en [cancelled conj] prenant'},
 {'form':'pt','expansion':'point','place':'final paragraph, with a cancelled terminal s'}
]
D['notes']=[
 'The author presents E=E0,3 as an extension of Gamma=Gamma0,3, written as a symmetric-group-type factor times Z/2Z, by the group capital Pi=Pi0,3. He writes the generators l0,l1,linfinity with relation linfinity l1 l0=1 and identifies the group with the fundamental group of the three-punctured complex projective line at -bar j. The two underbrace labels and the note engendré par tau: z maps to bar z are part of the inscription.',
 'The author says that conjugacy classes of maximal partial splittings correspond to fixed points of dotted rho and the three dotted sigmas acting on X0,3, and to possible connected components of invariant sets for the listed tau-containing involutions. The inserted word is éventuelles, not the alternative witness’s adverb éventuellement. The cancelled prefix before the first tau remains visible and doubtful.',
 'The author identifies P and Pbar as the fixed points of the undotted rho occurrence, gives their stabilizer order as 6, inserts savoir phi(S3), and writes an explicit six-element list. Its sigma indices are visibly 1,2,3. Later on this same sheet he writes 0,1,infinity in the list of elements carrying P to Pbar and in the lift choices. The unexplained index shift is retained; this first reader has not repaired it from the mathematical context.',
 'The author refers to the previously studied lift attached to P and describes conjugating by an element of E whose image in Gamma sends P to Pbar to obtain lifts related to Pbar. The inserted entre eux belongs inside the Pi-conjugués parenthesis. The literal comma before s’obtiennent and the absence of a stop before lower-case on are preserved, without grammatical rewriting.',
 'The final paragraph corrects the opening to singular Le and pt by cancelling the terminal s letters and inserting seul. It states that sigma0 has the sole fixed point 2, whose stabilizer is isomorphic to Z/2 times Z/2 and generated by sigma0 and tau. The page ends while introducing a lift of this subgroup; no concluding punctuation is supplied.',
 'There is no explicit authorial question or phrase such as j’ignore on this sheet. Éventuelles is an authorial qualification. The handwritten numbers are 12 at the top and 26 at lower left; no date is present. The closing right brace after the base point is visibly mismatched with the opening parenthesis and is transcribed literally.',
 'This first page reader performed no targeted proof, independent re-proof, computation, or mathematical verification. No mathematical expectation was used to settle an ambiguous stroke. The parent’s separate mathematical checks are not claimed here. All fourteen saved local crops were reviewed by the parent, which agreed the stated preferred readings and retained local uncertainties.',
 'Each native half and the whole page were successfully displayed once. An initial tool attempt to display the whole page returned only a context-truncation message and no visible image; the subsequent successful display is the single counted whole-page reading. The existing crop01 was revisited for the parent’s specific delimiter prompt; no replacement or additional crop was generated. The two abbreviated élémt words meet crop edges, but their strokes are covered jointly by the saved overlaps (08/09 and 09/10) and by the original native-half reading. No additional page input was inspected for this assignment.'
]

with (P/'differences.tsv').open(newline='') as f:
    raw=list(csv.DictReader(f,delimiter='\t',quoting=csv.QUOTE_NONE))
assert len(raw)==37
assert {x['page'] for x in raw}=={'145_scan027'}
substantive={8:3,9:3,10:5,11:5,12:6,13:10,14:11,15:10,16:12,17:12,18:12,19:13,21:13,22:15,23:15,24:16,25:17,26:18,27:19,29:20,30:21,31:23,32:25,33:26,34:27,35:27,36:28,37:29}
editorial={
 1:'The scan identifier 27 versus H’s editorial p. prefix is metadata, not an inscription disagreement; the actual top numeral12 is independently read and selected in B01.',
 2:'H’s words de l’auteur are an editorial page-number explanation, absent from the manuscript by design.',
 3:'The token mismatch combines C’s explicit alphabet alternatives and inline underbrace with H’s separately worded note. Both witnesses report the =S3 label. Alphabet uncertainty remains; the newly observed subscript-delimiter departure common to both witnesses is s027-01.',
 4:'The note engendré par tau: z maps to bar z is reported in full by H below the display; this row is displacement caused by editorial note placement, not missing manuscript content.',
 5:'The difference 1l versus 1 l is TeX/token spacing in the same written relation.',
 6:'This token stretch crosses H’s end of display and opening editorial note. The real missing base point is separately covered by s027-03; the brace correction common to C and H is s027-04.',
 7:'H’s long editorial note describes the two underbraces and the upper-right tau note. The source confirms U=U0,3; H’s uncertainty there is a confidence difference, with no change from C. The full source block is selected in B02.',
 20:'Only the alternative alphabet label in C’s de phi(S3) doubt is tokenized as an extra. M0872 remains undecided; H’s confident font label does not justify normalizing the ink.',
 28:'The extra alternative sont is C’s uncertainty apparatus. The underlying soit/sont ink remains unresolved in M0873, not a lexical departure from the shared first reading soit.'
}
for n,row in enumerate(raw,1):
    x={'row':n,'source_page':row['page'],'source_C':row['witness C'],'source_H':row['witness H']}
    if n in substantive:
        x.update(status='substantive',change_id=f's027-{substantive[n]:02d}')
        if n==18: x['related_change_ids']=['s027-11']
        if n in (34,35): x['related_change_ids']=['s027-28']
    else:
        x.update(status='macro/editorial',explanation=editorial[n])
        if n==3: x['related_change_ids']=['s027-01']
        if n==6: x['related_change_ids']=['s027-03','s027-04']
    D['diff_coverage'].append(x)
D['layout']='One text sheet in his hand: manuscript number 12 at the top, an opening extension line with an underbrace label and a three-line note at upper right, a fundamental-group display with its own underbrace label, and nineteen prose/formula baselines below the display, ending in a separate final paragraph. There are six interlinear insertions, cancellations, and manuscript number 26 at lower left. The final paragraph continues at the physical bottom without terminal punctuation. The count of 35 includes 21 main baselines, two page numerals, two underbrace labels, three note lines, the separate struck au dessus des line, and six insertion baselines.'
# Raw Python strings used to quote apostrophes are made literal source strings.
def clean(value):
    if isinstance(value,str): return value.replace("\\'", "'")
    if isinstance(value,list): return [clean(x) for x in value]
    if isinstance(value,dict): return {k:clean(v) for k,v in value.items()}
    return value
D=clean(D)
save()
print('Checkpoint: all 37 target-only raw rows covered; final report sections saved')

# Non-compiling structural and source-reference checks only.
from collections import Counter
assert [x['id'] for x in D['changes']]==[f's027-{i:02d}' for i in range(1,30)]
assert all(x['c_changed'] or x['h_changed'] for x in D['changes'])
assert len({x['id'] for x in D['changes']})==29
with (P/'marks.tsv').open(newline='') as f:
    mark_rows=list(csv.DictReader(f,delimiter='\t',quoting=csv.QUOTE_NONE))
assert [x['id'] for x in D['decisions']]==[x['id'] for x in mark_rows]
c_doubts=Counter(macros(C,'unsure'))
listed=Counter(x['the mark as written'] for x in mark_rows)
unlisted=Counter(x['source_mark'] for x in D['unlisted_decisions'])
assert c_doubts==listed+unlisted,(c_doubts,listed,unlisted)
assert len(macros(T,'unsure'))==len(D['doubts'])==17
assert len(macros(T,'deleted'))==8
assert len(macros(T,'inserted'))==6
assert [x['row'] for x in D['diff_coverage']]==list(range(1,38))
ids={x['id'] for x in D['changes']}
for x in D['diff_coverage']:
    if x['status']=='substantive': assert x['change_id'] in ids
    else: assert x['status']=='macro/editorial' and x['explanation']
    for related in x.get('related_change_ids',[]): assert related in ids
for group in ('changes','decisions','unlisted_decisions','crop_manifest'):
    for x in D[group]:
        assert (R/'edition'/x['crop']).is_file(),x['crop']
        for other in x.get('additional_crops',[]): assert (R/'edition'/other).is_file(),other
        a,b,c,d=x['box']; assert 0<=a<c<=1677 and 0<=b<d<=2364,(group,x['box'])
for x in D['doubts']: assert (R/'edition'/x['crop']).is_file()
for x in D['inventory']:
    a,b,c,d=x['box']; assert 0<=a<c<=1677 and 0<=b<d<=2364
    assert x['sheet_kind']=='text' and x['hand']=='his hand' and x['transcribed']=='yes'
assert len({x['element'] for x in D['inventory']})==41
assert len({x['box'] for x in D['second_boxes']})==11
for x in D['second_boxes']:
    a,b,c,d=x['coords']; assert 0<=a<c<=1677 and 0<=b<d<=2364

def tex_structure(s):
    depth=0; dollars=0
    for i,ch in enumerate(s):
        j=i-1; slashes=0
        while j>=0 and s[j]=='\\': slashes+=1; j-=1
        escaped=slashes%2
        if not escaped:
            if ch=='{': depth+=1
            elif ch=='}':
                depth-=1
                assert depth>=0,('early closing brace',i,s[max(0,i-30):i+30])
            elif ch=='$': dollars+=1
    assert depth==0,('brace depth',depth)
    assert dollars%2==0,('odd dollar count',dollars)
tex_structure(T)
for x in D['second_boxes']: tex_structure(x['reading'])
compact=lambda s:re.sub(r'\s+','',s)
ct,ht,tt=compact(C),compact(H),compact(T)
for x in D['changes']:
    assert compact(x['C']) in ct,('C span not found',x['id'],x['C'])
    assert compact(x['H']) in ht,('H span not found',x['id'],x['H'])
    assert compact(x['final']) in tt,('final span not found',x['id'],x['final'])
for x in D['second_boxes']:
    assert compact(x['reading']) in tt,('second selection not exact final excerpt',x['box'])
else:
    pass
inventory_ids={x['element'] for x in D['inventory']}
second_ids={x['box'] for x in D['second_boxes']}
for x in D['c_markup_audit']['items']:
    assert x['inventory_element'] in inventory_ids and x['second_box'] in second_ids
    bx=next(b for b in D['second_boxes'] if b['box']==x['second_box'])
    assert compact(x['reading']) in compact(bx['reading'])
assert D['check_events']==[]
D['validation']={'method':'non-compiling structural and source-reference checks','passed':True,'changes':29,'c_departures':sum(x['c_changed'] for x in D['changes']),'h_departures':sum(x['h_changed'] for x in D['changes']),'listed_marks':8,'unlisted_C_doubts':6,'remaining_doubts':17,'inventory_elements':41,'second_boxes':11,'source_difference_rows':37,'source_C_deletions':6,'source_C_insertions':6,'final_deletions':8,'final_insertions':6,'saved_crops':14,'checks':['valid JSON round-trip','unique sequential change, inventory and second-box identifiers','no change row with both flags false','MARKS IDs in exact source order','every C uncertainty accounted for by listed or unlisted decisions','every raw source difference row covered exactly once','all crop references exist and all boxes are in bounds','TeX and every complete second selection have balanced unescaped braces and math delimiters','every C/H change quote occurs in its source witness after whitespace normalization','every final change reading and complete second selection occurs in the proposed TeX','all twelve C insertion/deletion spans mapped to inventory and complete second selections'],'tex_compilation_performed':False}
save()
assert json.loads(O.read_text())==D
print(json.dumps(D['validation'],ensure_ascii=False,indent=2))
