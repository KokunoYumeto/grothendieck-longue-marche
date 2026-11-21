import json,re
from pathlib import Path
base=Path('/workspace/scratch/d7279cb02214'); work=base/'SP92_C13_150+151_work'; page='150_scan095'
p=json.loads((base/'reading_packets'/page/'packet.json').read_text())
r=json.loads((work/'records'/f'{page}.json').read_text()); tex=(work/'records'/f'{page}.tex').read_text()
mc={Path(q['crop']).stem.removeprefix(page+'_'):q for q in r['crop_manifest']}
def ev(name):
 q=mc[name];return dict(crop=q['crop'],box=q['box'])
def revision(place,source_state,final_state,attachment,evidence,crop):
 return dict(place=place,source_state=source_state,final_state=final_state,attachment=attachment,evidence=evidence,**ev(crop))
r['deletion_insertion_review']=[
 revision('First line, old word after la','C deletion','deleted; physically unreadable word retained as \\illegible{1}','The raised réciproque replaces this word between la and est vraie.','A heavy horizontal cancellation crosses the old word; isolated residual strokes do not expose all letters. No guessed completion is promoted to readable text.','reciproque'),
 revision('First line, raised réciproque','C insertion','inserted; live réciproque','Replacement for the cancelled word after la; followed by est vraie.','The raised r/é/c/i/p/r/o/q/u/e sequence is legible above the cancelled group. No strike traverses the replacement.','reciproque'),
 revision('Opening paragraph, raised equality','C insertion','inserted; live =X_{bar J setminus J}^*','The leader returns after the baseline second X_J^* and before soit fermé.','Equality has two separate bars; the inserted X, star and barred J minus J are above the line. The long curved stroke descends beside soit as an attachment leader, not an underline or deletion.','top_math_insertion'),
 revision('Opening paragraph, old i.e. after soit fermé','C deletion','deleted; i.e. readable','After the comma following soit fermé and before the next line’s il f et s.','The strike passes through the short i/e group; the live first condition on the following line is separate. The insertion leader does not cancel soit.','top_math_insertion'),
 revision('Cancelled opening before Soit maintenant','C deletion with doubt','deleted; \\unsure{Sur les|Soient les}','Abandoned start above the live Soit maintenant line; not joined to its grammar.','One strike traverses the older word group. Initial S and les are visible; obscured middle letters do not justify resolving the C/H disagreement.','cancelled_sur'),
 revision('Old numeral below first (95)','C deletion with doubt','deleted; \\unsure{96}','Immediately below the live first display label, distinct from the formula’s terms.','Intersecting cancelling strokes obscure the two numeral-sized bodies. Live (95) remains separate and readable by local digit comparison.','number95_cancel'),
 revision('Before the unnumbered equivalence','C deletion with doubt','deleted; \\unsure{cela revient}','The cancelled two-word group precedes live on a to the left of the equivalence on the same baseline.','The strike covers the two groups only; the separate on a to its right is live. H’s relocation after the display is corrected.','cancelled_cela_ona'),
 revision('After the pair (i,j)','C deletion with doubt','deleted; \\unsure{comme}','Between the baseline comma and live donc n’a pas.','The cancelling stroke is confined to the low word group; it does not cross the following donc or n’a.','cancelled_comme')]
coverage={}
def dc(n,cl,ids,reason):coverage[f'D{n:04}']=dict(diff_id=f'D{n:04}',classification=cl,change_ids=[f'C{i:02}' for i in ids],reason=reason)
dc(648,'editorial-only',[],'C’s scan marker and H’s opening editorial location phrase are not differing manuscript words. Authorial 44 is present in both descriptions and is separately inventoried.')
dc(649,'editorial-only',[],'H’s continuation and cross-page numbering commentary is editorial; it is not manuscript text and no claims about unassigned pages were checked.')
dc(650,'macro-only',[],'The 1 is C’s illegible-word count; H uses an uncounted ill macro for the same cancelled unreadable group.')
for n in [651,652,655,656,657,662]:dc(n,'macro-only',[],'Superscript/subscript order and brace serialization differ; the same X, star and letter subscript are present. The actual ink was independently checked.')
dc(653,'reading',[1],'The manuscript has the literal equality sign as a short form, not the expanded word mêmes.')
dc(654,'reading',[2],'H adds a comma after hypothèses that is not a separate mark on the page.')
for n in [658,659,660,661]:dc(n,'alignment-only',[],'Token alignment shifts X and the inserted equality across different TeX orders. The same baseline difference and raised equality are present with the attachment confirmed.')
dc(663,'reading',[3],'The first necessary-condition verb is the written f, not H’s expansion faut.')
dc(664,'reading',[4],'The written s. is not H’s expanded il suffit.')
dc(665,'reading',[7],'M0722 resolves C’s first reading loc with raised t; the rejected exclamation alternative is not retained.')
dc(666,'reading',[8],'The cancelled C/H Sur/Soient disagreement remains uncertain; the ink-favored shorter reading stands first, with both alternatives retained.')
dc(667,'reading',[9],'The written tt is preserved rather than H’s expanded tout.')
dc(668,'reading',[10],'The word after pro- is voisinage; the late descending g and long word body rule out espace.')
dc(669,'editorial-only',[],'H’s à droite and quotation wrapper locate its margin transcription; those words are not on the page.')
dc(670,'reading',[12],'The margin has the short form équiv. rather than équivalence.')
dc(671,'reading',[13],'The marginal parenthesis reads X métrisable; H’s unibranche and unresolved remainder are not supported.')
dc(672,'editorial-only',[],'H’s declaration of uncertainty and closing editorial quote are commentary; the actual disputed parenthesis is handled in C13.')
dc(673,'reading',[14],'The live on a replaces H’s unread word and added terminal period.')
dc(674,'macro-only',[],'aligned is a TeX layout environment, not a source word. The first label’s independent doubt resolution is recorded under M0723/C15.')
dc(675,'alignment-only',[],'C embeds the first arrow caption; H quotes the same équiv. si strat. dense in a note and substitutes its explicitly editorial label (a). The caption itself is read and retained.')
dc(676,'alignment-only',[],'H’s explicitly editorial (b), the relocated endpoint and its caption-introducing prose shift the alignment; no manuscript letter (a) or (b) is inserted.')
dc(677,'reading',[20],'The shared first caption is aligned through H’s note; the extra stop after strat in H’s second caption is a real punctuation difference.')
dc(678,'reading',[20,21],'H adds a stop after fid and replaces the separately cancelled numeral by an editorial description. The number remains narrowly doubtful; editorial arrow labels are excluded.')
dc(679,'reading',[22,23],'The cancelled two-word reading and live on a occur before the equivalence on the same baseline, not after it as in H.')
dc(680,'reading',[23],'H’s extra period belongs to its misplaced unread on a group. The source has no stop after on a; the genuine period after the equivalence’s j remains.')
dc(681,'reading',[26],'C’s tentative cancelled comme is retained against H’s unread group; the strike prevents resolution.')
dc(682,'reading',[27],'The live verb is n’a, with one a body after the apostrophe; it is not n’est.')
dc(683,'reading',[28],'The source word chance is fully readable between de and d’être.')
dc(684,'reading',[29],'H’s opening quotation mark is absent; the small marks belong to é.')
dc(685,'reading',[29,30],'The source has no closing quotation mark and does have a two-dot colon. C’s à is corrected.')
dc(686,'reading',[32],'M0724 resolves to 95, the first C alternative; H’s 96 is contradicted by the straight top of the second digit.')
dc(687,'macro-only',[],'C’s array describes the stacked implication arrows; H substitutes its explicitly editorial (c) label. Neither token is source text.')
dc(688,'reading',[34,35],'The source captions are restored to their arrows. H’s later note misreads the forward caption and adds a stop in strat fidèle; those actual readings are collated.')
dc(689,'reading',[34,35],'H’s prose explanation of the reverse arrow and location notes are editorial. Within the quoted source captions, C34 and C35 record the actual word/punctuation differences. On posera and (97) are present in both; their apparent long shift is alignment only.')
dc(690,'reading',[37],'H omits the thin later foliation 94; it is preserved as a margin number distinct from the author’s 44.')
r['diff_coverage']=[coverage[d['diff_id']] for d in p['differences']]
r['decisions']=[
 dict(id='M0722',cote='150',scan='95',decision='first',reading=r'loc\textsuperscript{t}',ink='Connected raised upright, side crossbar and turned foot; no separate lower dot. The glyph is a superscript t.',confidence='high',**ev('loc')),
 dict(id='M0723',cote='150',scan='95',decision='first',reading='95',ink='First digit’s compressed angular cap and long descending stem match the 9 in (97); that label’s 7 has a different mid-crossed construction. Second digit has a top bar and lower bowl. The crossed group below is not part of this live label.',confidence='medium',comparison_crop=mc['formula97']['crop'],comparison_box=mc['formula97']['box'],**ev('number95_cancel')),
 dict(id='M0724',cote='150',scan='95',decision='first',reading='95',ink='The second digit’s long straight horizontal top and lower bowl identify 5, without the rounded upper approach of 6. Duplicate 95 is preserved.',confidence='high',**ev('number96'))]
inv=[]
def item(element,kind,position,first,hand='author'):
 inv.append(dict(sheet_kind='text',hand=hand,element=element,kind=kind,position=position,first_words_or_objects=first,transcribed='yes'))
item('Authorial page number','margin note','upper-left, y25–84','44')
item('Opening paragraph','text','upper body, six principal baselines y54–690','et moyennant densité et fidélité')
item('First cancelled word','deletion','first line, after la','unreadable old word')
item('Replacement réciproque','insertion','raised above first-line cancellation','réciproque')
item('Raised equality','insertion','above the difference in opening paragraph, y269–447','=X_{bar J setminus J}^*')
item('Cancelled i.e.','deletion','right end of line with soit fermé, y365–447','i.e.')
item('Abandoned opening','deletion','above live Soit maintenant, y716–787','Sur les | Soient les')
item('Pro-neighborhood definition prose','text','body y729–827','Soit maintenant, pour tt i in I')
item('Homotopy margin note','margin note','right of (94), four short baselines within y798–1046','donc X_i^* hookrightarrow V_i; équiv. d’homotopie (X métrisable)')
item('Definition (94)','display','body y872–999','(94) V_i=V(X_i^*,X)')
item('Introduction to intersections','text','body y1006–1072','et considérons V_i cap X_j^*, on a')
item('First display (95)','display','body y1088–1426, two main rows with arrow captions','(95) V_i cap X_j^* neq phi iff ... implies i leq j')
item('Cancelled display number','deletion','below first live (95), y1180–1257','96, uncertain and struck')
item('First implication caption','text','under first forward implication in (95), two baselines y1321–1418','équiv. si / strat. dense')
item('Second implication caption','text','under second forward implication in (95), two baselines y1293–1404','équiv. si / strat fid')
item('Dense and faithful case','text','body before unnumbered equivalence, around y1450–1537','donc dans le cas d’une strat. dense et fidèle,')
item('Cancelled transitional phrase','deletion','left of unnumbered equivalence, y1591–1689','cela revient, uncertain')
item('Live transition','text','same baseline after cancellation, y1591–1689','on a')
item('Unnumbered equivalence','display','right of live on a, y1537–1659','V_i cap X_j^* neq phi iff i leq j.')
item('Asymmetry paragraph','text','body y1675–1942, three principal baselines','On fera attention que cette relation n’est pas symétrique')
item('Cancelled comme','deletion','after (i,j), y1773–1833','comme, uncertain')
item('Second display labelled (95)','display','body y1911–2194, main comparison and stacked reverse arrow','(95) V_i cap V_j neq phi; i et j comparables')
item('Forward-arrow caption','text','above lower display arrow, two baselines y1911–1989','si X métrisable, donc tt|tte / partie ouverte de X est normale')
item('Reverse-arrow caption','text','below left-pointing arrow, y2092–2194','strat fidèle')
item('Introduction to pairwise intersection notation','text','body y2180–2240','On posera')
item('Definition (97)','display','body y2235–2327','(97) V_{i,j} def=V_i cap V_j,')
item('Later foliation','margin note','lower-left edge y2299–2344','94','later, thin grey hand')
r['inventory']=inv
r['notes']='''## Content and numbering

The leaf has the authorial number **44** at the upper left and the later foliation **94** at the lower left. No title or date is written. It continues a discussion of dense and faithful stratifications: the opening asserts the converse for openness and gives the locally closed/band condition. It then introduces the pro-neighborhood V_i=V(X_i^*,X), gives a chain comparing nonempty intersections, states the dense-and-faithful equivalence with i≤j, notes its asymmetry, and writes a comparison involving V_i∩V_j with a normality caption above the forward arrow and a faithfulness caption below the reverse arrow. The last definition names the pairwise intersection V_{i,j}. These are descriptions of the source, not independently checked assertions.

## Ink-led rereadings

The grammatical interruption at the end of the opening paragraph prompted a return to the line junction. The line ends **i.e que** with no second stop; the next line visibly begins **f et s que** before J. Both witnesses omit this live repetition. It is retained without smoothing the sentence. The first **il f et s.** has a stop after s; the repeated **f et s que** does not. The raised terminal in **locᵗ** has an upright and crossbar, so this occurrence is t rather than an exclamation mark.

The local number sequence prompted comparison of the first live label with the later (97). The compressed angular 9 has the same cap and long stem in both; (97)’s 7 has a different crossed construction. Thus the first label is read (95) at medium confidence. The lower comparability display also reads (95), with a straight-topped final 5, despite the expected consecutive numbering. The separately cancelled numeral below the first label remains uncertain as 96. No sequence has been repaired.

The notation prompted inspection of every empty-set occurrence. All seven have a small high loop on a long axial descender and are encoded as the written phi glyph. In these nonemptiness comparisons its use is the empty-set sign; that meaning does not justify substituting the witnesses’ conventional empty-set typography. In the last definition a separate small comma is visible between i and j. This is restored as V_{i,j}, without changing the intended pair of indices.

The lower forward caption is readable as **si X métrisable, donc tt / partie ouverte de X est normale**. A small return after the second t could be its foot or an e; the narrow **tt|tte** doubt remains, and grammatical agreement with partie is not used to settle it. The prose before the lower display has **n’a pas de chance** and a literal colon after équivalente, with no quotation marks. The word pro-voisinage and the marginal métrisable are read from their letter sequences, not supplied from the mathematical setting.

## Revisions and physical form

The two raised insertions replace the unreadable opening word and attach the equality after the baseline X_J^* respectively. The curved equality leader does not strike or underline soit. Six cancelled groups are preserved: the unreadable first word, i.e., the Sur les/Soient les opening, the tentative numeral 96, cela revient, and comme. The last four remain uncertain because cancellation obscures internal strokes. The live on a after cela revient is on the left of the unnumbered equivalence; H’s placement after that display is not followed. The right-margin homotopy note has a parenthesized tilde beneath h and uses the abbreviation équiv.

There is no separate drawing or diagram. The aligned formulas, their arrow captions and the small marginal map are mathematical writing. No explicit authorial question mark or dated proof-check entry was identified. This reader performed visual transcription and local glyph comparisons only; check_events is therefore empty.
'''
r['notation']=[
 dict(sign=r'\phi',reading='Written empty-set sign in nonemptiness conditions; seven occurrences.',evidence='Every occurrence has a small high loop traversed axially by a long descending stem, including the isolated inline specimen.'),
 dict(sign=r'=',reading='Literal short form for mêmes in Sous les = hypothèses.',evidence='Two parallel bars; no word bodies.'),
 dict(sign=r'loc\textsuperscript{t}',reading='Localement, with a raised t rather than an exclamation mark on this leaf.',evidence='Raised upright with side crossbar and connected foot; no detached lower dot.'),
 dict(sign=r'\mathcal V_i',reading='Pro-voisinage V(X_i^*,X).',evidence='The defining prose explicitly says pro-voisinage; (94) gives the equality.'),
 dict(sign=r'\overset{(\overset{h}{\sim})}{\hookrightarrow}',reading='Hook arrow annotated by a parenthesized tilde with h above.',evidence='Separate h, wavy stroke, parentheses and arrow shaft visible in the marginal crop.'),
 dict(sign=r'\mathcal V_{i,j}',reading='Pairwise intersection notation with a written subscript comma.',evidence='Comma is a distinct curved stroke below the subscript baseline between i and j in (97).'),
 dict(sign='95, 95, 97',reading='Written labels of the main chain, lower comparison and final definition.',evidence='The first 9 is compared with the local (97); the lower 5 has a straight top bar. The repeated 95 is not normalized.')]
r['hand_log']=[
 dict(habit='A tiny high loop on a very long axial descender represents the empty-set sign.',places='Four positions in the first (95), unnumbered equivalence, inline prose formula, lower (95).',scope='All seven occurrences on this leaf; independently compared to the supplied notation table.',witness_errors='Both C and H normalize the written form to standard empty-set glyphs.'),
 dict(habit='A 9 may have a compressed, almost triangular cap; the 7 has a transverse middle stroke.',places='First (95) and final (97).',scope='Local digit comparison on this leaf only.',witness_errors='C leaves the first95 doubtful; the comparison supports its first reading at medium confidence.'),
 dict(habit='A raised t retains a crossbar and a connected return.',places='loc before fermé in the opening paragraph.',scope='This occurrence; no transfer of another leaf’s loc! form.',witness_errors='C offers an exclamation alternative, here excluded by the connected terminal.'),
 dict(habit='Two compressed t stems can share a crossbar; the final pen return is small.',places='pour tt before the definition and the lower forward caption.',scope='The first occurrence is clear tt; the second retains tt|tte.',witness_errors='H expands the clear occurrence to tout and does not recover the later short form.'),
 dict(habit='Abbreviation stops are variable and require individual reading.',places='f et s.; repeated f et s; équiv.; strat. dense; strat fid; strat fidèle; i.e que.',scope='Only the visible punctuation at each occurrence.',witness_errors='H expands short forms and supplies stops in the two fidelity captions; both witnesses supply a stop after the junction e and omit the repeated condition.'),
 dict(habit='Long curved insertion leaders can enclose the beginning of a live baseline word.',places='Raised equality above soit fermé.',scope='This leader and its attachment.',witness_errors='No new witness error in the attachment; the bounds are confirmed explicitly.'),
 dict(habit='Thin grey later foliation differs from the author’s heavy brown-black numbering.',places='Lower-left94 versus upper-left44.',scope='Two numbering hands on this leaf.',witness_errors='H omits the later foliation.'),
 dict(habit='Cancellation strokes obscure internal letters even where a word outline is plausible.',places='Opening old word; Sur les/Soient les; cancelled96; cela revient; comme.',scope='All unresolved cancellations on this leaf.',witness_errors='H’s definite Soient les is too strong; the other cancelled lexical hypotheses remain narrowly marked.')]
r['abbreviations']=[
 dict(form='=',expansion='mêmes (explanation only; literal sign retained)'),
 dict(form='ssi',expansion='si et seulement si'),
 dict(form='il f et s.',expansion='il faut et suffit'),
 dict(form='f et s',expansion='faut et suffit; written repetition retained'),
 dict(form=r'loc\textsuperscript{t}',expansion='localement'),
 dict(form='loc.',expansion='localement'),
 dict(form='tt',expansion='tout; later caption retains narrow tt|tte ambiguity'),
 dict(form='équiv.',expansion='équivalent / équivalence, according to its construction'),
 dict(form='strat.',expansion='stratification'),
 dict(form='strat',expansion='stratification; no stop supplied'),
 dict(form='fid',expansion='fidèle; no stop supplied'),
 dict(form='i.e.',expansion='id est'),
 dict(form='i.e',expansion='id est; missing final stop retained at line junction'),
 dict(form='déf',expansion='définition')]
doubts=[]
def doubt(place,reading,alts,conf,reason,crop):doubts.append(dict(place=place,reading=reading,alternatives=alts,confidence=conf,reason=reason,**ev(crop)))
doubt('Old word under réciproque',r'\deleted{\illegible{1}}',[],'low','Thick cancellation leaves disconnected traces but not all letters; no lexical reconstruction is adopted.','reciproque')
doubt('Cancelled opening above Soit',r'\deleted{\unsure{Sur les|Soient les}}',['Soient les'],'low','Short Sur remains ink-favored; middle strokes under the cancellation do not exclude the longer H reading. This is a continuing actual C/H disagreement, not a resolved word.','cancelled_sur')
doubt('Cancelled numeral below first (95)',r'\deleted{$\unsure{96}$}',[],'low','Intersecting cancellation strokes obscure the digit heads and return; 96 is retained tentatively rather than resolved.','number95_cancel')
doubt('Cancelled phrase before live on a',r'\deleted{\unsure{cela revient}}',[],'low','Several internal connections, especially in the second word, are covered by the strike; visible first-word bodies and re-like opening support only a tentative reading.','cancelled_cela_ona')
doubt('Cancelled word after (i,j)',r'\deleted{\unsure{comme}}',[],'low','The low outline and initial c support the retained hypothesis, but crossing obscures the middle letters.','cancelled_comme')
doubt('Lower forward-arrow caption, after donc',r'\unsure{tt|tte}',['tte'],'medium','Two crossed t stems are clear. The small final return could be a foot or a separate e. Added uncertainty alone does not count as a change against C; H’s different caption words are separately collated.','caption96')
r['doubts']=doubts
boxes=[]
def box(n,kind,coords,reading):
 assert re.sub(r'\s+',' ',reading).strip() in re.sub(r'\s+',' ',tex), (n,reading)
 boxes.append(dict(box=f'B{n:02}',kind=kind,x0=coords[0],y0=coords[1],x1=coords[2],y1=coords[3],reading=reading))
def part(start,end,include_end=True):
 a=tex.index(start);b=tex.index(end,a);return tex[a:b+len(end) if include_end else b]
box(1,'authorial handwritten number',[42,25,116,84],r'\mspage{44}')
box(2,'cancelled word and raised replacement',[1285,54,1648,149],r'\deleted{\illegible{1}} \inserted{réciproque}')
box(3,'different-word reading, punctuation, raised equality and cancelled i.e.',[299,249,1640,447],part('Sous les',r'\deleted{i.e.}'))
box(4,'abbreviations, repeated omitted words and resolved superscript doubt',[299,462,1640,690],part('il f et s.','soit une bande.'))
box(5,'cancelled opening and differing tt/pro-voisinage readings',[295,705,1655,838],part(r'\deleted{\unsure{Sur les|Soient les}}','le pro-voisinage'))
box(6,'whole numbered formula (94)',[267,872,1117,999],r'\[(94)\qquad\mathcal V_i=\mathcal V(X_i^*,X)\]')
box(7,'entire right-margin note and differing words',[1205,798,1655,1046],part(r'\margin{donc',"($X$ métrisable)}"))
box(8,'readable words on a',[295,1006,1237,1072],r'et considérons $\mathcal V_i\cap X_j^*$, on a')
box(9,'whole first formula (95), resolved label, all captions and separately cancelled numeral',[280,1088,1552,1426],part('\\[\n(95)\\quad',r'\deleted{$\unsure{96}$}'))
box(10,'cancelled phrase, live on a and complete unnumbered equivalence',[295,1537,1536,1689],part(r'\deleted{\unsure{cela revient}}',r'\[\mathcal V_i\cap X_j^*\neq\phi\Longleftrightarrow i\leq j.\]'))
box(11,'asymmetry prose, cancelled comme, n’a/chance, colon and inline formula',[299,1675,1640,1942],part('On fera attention','$. On a'))
box(12,'whole lower formula (95), all captions including tt|tte and reverse arrow',[295,1911,1653,2194],part('\\[\n(95)\\qquad','\\]\nOn posera',False)+'\\]')
box(13,'On posera and whole numbered formula (97) with subscript comma',[329,2180,1115,2327],part('On posera',r'\mathcal V_j,\]'))
box(14,'later handwritten foliation',[20,2299,75,2344],r'\margin{94}')
r['second_boxes']=boxes
r['review_status']='Reader complete: candidate, all supplied differences and marks, revisions, inventory, doubts, notation and blind boxes assembled; awaiting root finalization.'
r['validation']={'candidate_braces_balanced':None,'all_43_diff_ids_in_order':None,'all_3_marks_in_order':None,'all_crops_viewed':True,'exact_witness_snippets_checked':True,'second_box_readings_checked_as_candidate_substrings':True,'no_compilation':True}
(work/'records'/f'{page}.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
print('Saved complete record:',len(r['changes']),'changes;',len(r['diff_coverage']),'differences;',len(r['decisions']),'mark decisions;',len(boxes),'blind boxes;',len(inv),'inventory items')
