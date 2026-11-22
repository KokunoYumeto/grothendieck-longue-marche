import json,re
from pathlib import Path
b=Path('/workspace/scratch/d7279cb02214');w=b/'SP92_C13_150+151_work';page='150_scan097'
p=json.loads((b/'reading_packets'/page/'packet.json').read_text());f=w/'records'/f'{page}.json';r=json.loads(f.read_text());tex=(w/'records'/f'{page}.tex').read_text()
mc={Path(q['crop']).stem.removeprefix(page+'_'):q for q in r['crop_manifest']}
def ev(n):return dict(crop=mc[n]['crop'],box=mc[n]['box'])
r['deletion_insertion_review']=[
 dict(place='fermé after si Z est',source_state='C deletion',final_state='deleted, fermé retained',attachment='An abandoned predicate before the live une partie loc! fermée.',evidence='The tall f and compressed remaining word are crossed by an independent heavy stroke. The following une partie is live and outside the cancellation.',**ev('cancelled_ferme')),
 dict(place='Old words before live X_i_n*',source_state='C deletion containing two unreadable words',final_state=r'\deleted{\illegible{1} \unsure{du|de}}',attachment='Cancelled group on the lower condition line, followed by the separate live X_i_n*.',evidence='The long strike obscures the left group almost completely. The right d oval/ascender survives, with its ending uncertain. The dot below the struck group belongs to the dotted X in the lower cancelled formula, not to these old words.',**ev('cancelled_contient')),
 dict(place='Raised parenthesis de sorte que and two connectors',source_state='C insertion',final_state='live inserted parenthesis; words resolved, first X/star and first label remain uncertain; connector bodies read separately',attachment='After the live X_i_n* and before the following alors on a; physically above the long cancelled formula, ending without a comma.',evidence='Opening and closing parentheses enclose the raised words and maps. The long strike below crosses the old formula, not this replacement. The previous line’s descender crowds the first label but is not a new deletion of it.',**ev('insertion_full')),
 dict(place='Full X_i_n minus dotted-X formula and NB definition',source_state='C deleted display',final_state='whole formula remains deleted, with both literal minus bars retained',attachment='An abandoned restriction expression below the live condition and raised parenthesis.',evidence='One long, slightly rising cancellation traverses the entire first difference and the NB through its final closing parenthesis. Stars, dotted X symbols, union indices and the accented déf remain distinguishable. The first dot over X_i_0 is visible above the tight beginning crop in the whole formula view.',**ev('cancelled_formula')),
 dict(place='Separate curved question above alors',source_state='Not transcribed in C; described in H’s location note',final_state='authorial raised question preserved over alors',attachment='Above the l/o area of alors, separate from the left-margin question by (100).',evidence='The dark curved stroke has a gap from the l ascender and is therefore an independent mark. No separate lower dot is exposed; the question-shaped mark is preserved without treating it as a letter return.',**ev('alors'))]
co={}
def dc(n,kind,ids,why):co[f'D{n:04}']=dict(diff_id=f'D{n:04}',classification=kind,change_ids=[f'C{i:02}' for i in ids],reason=why)
dc(716,'editorial-only',[],'C’s scan marker and H’s introductory location words are editorial apparatus; the source’s upper number45 is preserved independently.')
dc(717,'editorial-only',[],'H’s de sa main and closing editorial quote describe the shared authorial number; they are not source prose.')
for n in [718,719]:dc(n,'macro-only',[],'The Z superscript is serialized before or after the same index. Independent continuation-count corrections are recorded in C01–C03, not inferred from this macro difference.')
dc(720,'reading',[5],'M0726 resolves to loc!, C’s alternative, from the upright plus detached dot.')
dc(721,'alignment-only',[],'C’s illegible count2 and H’s uncounted ill macro shift the neighboring X/star tokens. The live X_i_n* agrees. The newly recovered cancelled right-hand fragment is independently collated in C06.')
dc(722,'reading',[7,8,9,10,12],'The long alignment shift moves the raised insertion across the old cancelled formula. Within those spans, the resolved de sorte que, inserted X/star reading, connector geometry/labels, and literal first minus are actual source readings.')
for n in [723,724,725]:dc(n,'macro-only',[],'The starred X terms in the cancelled NB are the same despite superscript/subscript ordering. Their stars and indices were inspected directly.')
dc(726,'alignment-only',[],'H serializes the parenthetical insertion after the cancelled NB; C gives it before. H’s location note also places it above the cancellation. The actual insertion readings are collated in C07–C10.')
dc(727,'alignment-only',[],'Tokens from H’s moved inserted V^Z align against the end of C’s cancelled union. They are different physical places, not a Z-versus-star reading.')
dc(728,'reading',[11],'Most tokens are moved insertion/display closures; H additionally supplies a comma after the inserted parenthesis, absent on the page.')
for n in [729,730]:dc(n,'macro-only',[],'The Z superscript in (100) is serialized in a different order. The two source continuation marks at each index are independently corrected in C15–C16.')
dc(731,'alignment-only',[],'Both witnesses preserve ? à vérifier! as a margin note but serialize it on different sides of the parenthesis. The actual underline-extent disagreement is recorded in C18.')
dc(732,'reading',[19],'The parenthesis says métrisable, not unibranche.')
dc(733,'reading',[14,18],'H’s long editorial span contains two source observations: the raised question omitted by C and the underline extent, described incompletely by H. Those are collated; its other location/uncertainty prose is not transcribed.')
dc(734,'reading',[23],'The live est between the flag and un is present and omitted in H.')
dc(735,'reading',[24],'The opening quotation is made of paired high ticks, not a guillemet.')
dc(736,'reading',[24],'The closing quotation has two high ticks, not an angular guillemet.')
dc(737,'macro-only',[],'aligned is a layout environment, not a manuscript word.')
for n in [738,739]:dc(n,'macro-only',[],'Star and J are serialized in a different order for the same X_J^* in (101).')
dc(740,'reading',[25],'H quotes the caption later in a note. Its real reading difference is the added hyphen in pro-voisinage; the source has provoisinage.')
for n in [741,742]:dc(n,'macro-only',[],'C’s explicit lim with a right arrow and H’s varinjlim encode the same visible directed-limit sign. Its distinct pointed head was inspected.')
dc(743,'macro-only',[],'The closing aligned token is a TeX environment delimiter, not source ink.')
dc(744,'reading',[25],'The caption is present in H’s note, but its pro-voisinage hyphen differs from the continuous source word. The surrounding location and uncertainty words are editorial.')
for n in [745,746]:dc(n,'macro-only',[],'Superscript Z and subscript J are serialized in a different order in (102); both are present on the page.')
for n in [747,748]:dc(n,'macro-only',[],'Star and subscript J are reordered in TeX for the same term in (103); the star is clear and retained.')
dc(749,'macro-only',[],'tikzcd and its layout options are C’s diagram wrapper, not extra source words.')
dc(750,'macro-only',[],'The supplied difference is star/subscript serialization. Independent inspection of this shared star reading gives the h|* doubt and changed first reading in C28.')
dc(751,'macro-only',[],'The star and arrow-option tokens are TeX serialization; the actual superscript and label readings are independently collated in C28–C29.')
dc(752,'reading',[29,30],'The diagram serializations shift the middle object and lower equality. H omits the separate tilde in each homotopy label; C29–C30 record those actual missing strokes.')
dc(753,'macro-only',[],'C lays out the lower object with a vertical equal connector; H uses an underbrace shorthand and explicitly describes the vertical equal in its note. The same objects and relation are therefore not counted again merely for wrapper/layout syntax.')
dc(754,'reading',[31],'There is no separate stop after hom in the (104) caption. The stop in (103) is a distinct, retained occurrence.')
dc(755,'reading',[32],'H omits the later foliation96. Its note correctly describes double-underlined si and the vertical equal relation; those editorial descriptions are not additional manuscript words.')
r['diff_coverage']=[co[d['diff_id']] for d in p['differences']]
r['decisions']=[
 dict(id='M0726',cote='150',scan='97',decision='alternative',reading='loc!',ink='An uncrossed upright stands above a separate low dark dot. No connected t foot or side crossbar is visible.',confidence='high',**ev('loc')),
 dict(id='M0727',cote='150',scan='97',decision='first',reading='de sorte que',ink='Looped ascending d; low s/o/r sequence with tall t; separate q descender and ue. The old on sait que alternative does not match these letters.',confidence='high',**ev('insertion_words')),
 dict(id='M0728',cote='150',scan='97',decision='undecided',reading=r'\overset{\unsure{(\overset h\sim)}}{\relbar}',ink='The connector body is a plain short horizontal shaft without separately visible hook or head. Parenthesis curves and h/tilde-like residues above it remain crowded by a descender from the preceding line. The body is corrected, but the label portion of the C mark is not fully resolved.',confidence='medium',whole_formula_crop=mc['insertion_full']['crop'],whole_formula_box=mc['insertion_full']['box'],**ev('insertion_first_map')),
 dict(id='M0729',cote='150',scan='97',decision='other',reading='marche-\\\\\nront',ink='The first line exposes marche followed by an independent hyphen. The next line begins ront before encore. Both pieces are included and the written division is preserved.',confidence='high',additional_crops=[mc['marche_end'],mc['ront_encore']],**ev('NB_full'))]
inv=[]
def it(el,kind,pos,words,hand='author'):inv.append(dict(sheet_kind='text',hand=hand,element=el,kind=kind,position=pos,first_words_or_objects=words,transcribed='yes'))
it('Authorial foliation','margin note','upper-left y30–91','45')
it('Opening sentence','text','top main line y70–135','On pose, si Z est une partie de X,')
it('Definition (99)','display','y146–271','V_{i_0,..,i_n}^Z=V_{i_0..i_n} cap Z; parenthetical connector')
it('Condition on Z','text','two written levels y288–427','si Z est ... une partie loc! fermée qui contient ... X_i_n*')
it('Abandoned predicate','deletion','after si Z est, y306–387','fermé')
it('Cancelled lower word group','deletion','before live X_i_n*, y367–431','unreadable group; tentative du|de')
it('Raised parenthetical maps','insertion','above long cancelled formula, y333–419','de sorte que X_i_n|X_i_n* — V_i_n^Z hooked-shaft V_i_n')
it('Cancelled difference and NB definition','deletion','full line y382–492','X_i_n - dotted X_i_0; NB dotted X_i_0 déf=...')
it('Independent raised question','margin note','above alors, y536–580','?')
it('Transition to (100)','text','y570–622','alors on a')
it('Homotopy statement (100)','display','y557–741','V_{i_0..i_n}^Z hookrightarrow V_{i_0..i_n}')
it('Caption of (100)','text','right side, two short baselines y610–725','équiv. d’ / homotopie')
it('Authorial verification note','margin note','left of (100), y615–828, slanted','? / à vérifier!; underline excludes !')
it('Metrizability parenthesis','text','y740–869','on suppose X métrisable...')
it('Generalization paragraph','text','four sloping principal lines y840–1321','On va généraliser la définition des V_i ... drapeau de bandes')
it('Definition and formulas (101)','display','two main rows y1293–1571','V_J=V(X_J*,X); union over j; directed limit over d in Drap(J)')
it('Tubular-neighborhood caption','text','right of first row of (101), y1289–1401','provoisinage tubulaire')
it('NB on arbitrary J','text','two lines y1572–1848','NB la définition et les deux formules marche- / ront encore...')
it('Restriction definition (102)','display','y1840–1958','V_J^Z=V_J cap Z')
it('Transition to homotopy maps','text','y1980–2045','On a donc')
it('Homotopy statement (103)','display','y1973–2169','X_J* hookrightarrow V_J; équiv. d’hom.')
it('Diagram (104)','diagram','bottom y2154–2347','X_J^{h|*} -> V_J^Z -> V_J; vertical equal to V(X_J*,Z)')
it('Diagram caption and condition','text','right of main (104) row y2170–2267','équiv. d’hom; double-underlined si Z superset X_J')
it('Later foliation','margin note','lower-left y2281–2348','96','later, thin grey hand')
r['inventory']=inv
r['notes']='''## Source content and physical page

The authorial foliation is **45** and the thin later foliation is **96**. No title or date is written. The page defines restriction of the indexed pro-neighborhoods to Z in (99), then gives a condition that Z be written **loc! fermée** and contain the stratum. An old difference expression and its NB are cancelled below a raised replacement parenthesis. The resulting map in (100) is described as a homotopy equivalence under the parenthetical assumption **X métrisable**. The author places a separate question above alors and the marginal **? à vérifier!** beside this statement. These are authorial reservations, not editorial additions.

The next paragraph generalizes the indexed neighborhoods to bands J and flags of bands. Formula (101) gives the tubular pro-neighborhood description, union over j in J, and the directed limit over Drap(J). The following NB says that the definition and two formulas **marche- / ront encore** for an arbitrary subset J of I. Formula (102) restricts V_J to Z; (103) and the diagram (104) give the annotated maps. The final condition is written Z⊃X_J with no star. In (104), the middle object is related vertically by two parallel strokes to V(X_J^*,Z). The lower comma and closing-parenthesis foot touch the scan’s lower cut, but both characters and the formula remain identifiable; no following text is supplied.

## Rereadings prompted by the notation and mathematical context

The index sequences were counted occurrence by occurrence. There are two continuation marks in all three (99) indices, in both (100) indices, in the i-indexed V in the generalization paragraph, and between the two precedence signs of the written flag. The J-indexed V in that paragraph has three marks. The first index in (99) additionally has explicit commas on both sides of its two continuation marks. None of these counts is regularized to a uniform ellipsis.

The final capital in the flag has bilateral bars and is read literally **I_n**, contrasted on the same line with J_0’s left-turning foot. The band-flag context would suggest J_n; that expectation prompted the local comparison but does not replace the visible I. Likewise, the first X superscript in (104) is h-shaped, with an upright and short right branches, unlike the radial stars in (103) and in the lower object of (104). The source therefore retains **h|*** with h first. The surrounding stratum notation suggests a star as a possible intended form, not a reason to erase the glyph uncertainty.

The raised parenthesis was inspected as a whole and in its crowded parts. **de sorte que** is clear. No independent star can be isolated on its first X, so the unstarred term stands first with the starred term retained as an alternative. The first connector is a plain shaft; its label remains uncertain where a descender from the previous line overlaps it. The second connector has a left hook/loop but no pointed right head. In (99), a blunt upturned endpoint leaves a narrow headless/headed alternative. The clear heads of (100), (103), both (104) arrows, and the directed-limit arrow provide local contrasts; their actual heads are retained. The tilde beneath h is a separate mark wherever it is clear, not merely H’s (h) label.

Both subtraction signs in the cancelled line are short nearly horizontal bars. The dot above its first X_i_0 is visible in the whole formula even though it lies above the tighter beginning crop. The cancelled NB’s déf has a separate accent stroke. The first digits of (103) initially looked like a single bent shape; a tight crop shows a 1 joined to the flattened0, followed by3. The label is retained as103 from that geometry rather than from the numbering sequence.

## Words, punctuation and revisions

The two-line NB visibly divides **marche-** and **ront**, with an independent line-end hyphen. This resolves C’s marchent doubt to another reading; neither the tense nor the division is silently smoothed. The following encore is legible. The caption writes **provoisinage** without a hyphen. The word est before un drapeau is live. Quotation marks are paired high ticks rather than guillemets.

The loc terminal is an uncrossed upright plus a detached dot, hence literal **loc!**, unlike a raised t. The marginal underline spans **à vérifier** and ends before the exclamation. The small independent question above alors is separated from the l ascender; no detached lower dot is exposed. In (103), d’hom. has its final stop; in (104), d’hom has none. The parenthesis after métrisable has three distinct ellipsis points. The pale patch before métrisable is not transcribed; a separate dark accent-like mark over the e and the later i dot are visible.

All three C deletions and its raised insertion were reviewed for bounds and attachment. The first cancelled word remains fermé. The old lower word group permits only an unreadable left group and a tentative **du|de** on the right, where d is exposed but its ending is crossed. The long strike traverses the entire old mathematical line and leaves the raised replacement live. No comma follows that replacement’s closing parenthesis.

This reader performed transcription and local glyph comparisons, including the mathematical triggers described above, but no independent homotopy proof or other mathematical validation. No proof-check event is asserted; check_events remains empty.
'''
r['notation']=[
 dict(sign=r'i_0,..,i_n / i_0..i_n',reading='Two literal continuation marks; commas only in the first (99) index.',evidence='Counted on (99), (100) and the i-indexed generalization term; the nearby J-indexed term has three marks.'),
 dict(sign=r'J_0\prec..\prec I_n',reading='Written flag ends in capital I_n and has two continuation marks.',evidence='Last capital has top and bottom right projections; preceding J_0’s lower foot turns only left.'),
 dict(sign='loc!',reading='Literal upright plus detached dot in the locally closed condition.',evidence='Tight loc crop shows no t crossbar or connected foot.'),
 dict(sign=r'\mathrel{\lhook\joinrel\relbar}',reading='Headless hooked connector where the right endpoint is blunt.',evidence='Second raised connector clearly has a left loop and a flat right end; (99) retains a narrow headed alternative.'),
 dict(sign=r'\overset{(\overset h\sim)}{\hookrightarrow}',reading='Hooked arrow with a distinct parenthesized tilde beneath h.',evidence='Clear labels in (100), (103), and both diagram arrows; the first inserted label remains crowded and uncertain.'),
 dict(sign='-',reading='Literal difference bar in both places of the cancelled formula.',evidence='Short nearly horizontal blunt-ended strokes, distinct from the long cancellation.'),
 dict(sign=r'\lim_{\longrightarrow}',reading='Directed limit with a visible right-pointing arrow.',evidence='The lower stroke has two converging head arms in the tight limit crop.'),
 dict(sign=r'X_J^{\unsure{h|*}}',reading='Uncertain h-shaped superscript in the first object of (104), not normalized to star.',evidence='Tall filled upright with short right branches; local clear stars are radial.'),
 dict(sign='vertical equal relation',reading='Two short parallel vertical strokes between V_J^Z and V(X_J^*,Z).',evidence='Both strokes are individually visible above the lower object; no underbrace is written.')]
r['hand_log']=[
 dict(habit='Continuation marks vary in count and may mix compact dots and short strokes.',places='(99), (100), generalization paragraph and flag.',scope='Counted separately on this leaf; i-index chains have two, the V_J chain has three.',witness_errors='Both witnesses routinely substitute three-dot macros for two written marks.'),
 dict(habit='Capital I has bilateral bars, while J turns its lower foot leftward.',places='Final I_n and preceding J_0 in the flag, compared with standalone I.',scope='Local distinction; the source’s unexpected I is preserved.',witness_errors='Both witnesses normalize the final flag capital to J_n.'),
 dict(habit='A small h-shaped superscript can differ from nearby radial stars.',places='First X of (104), compared with (103) and lower (104).',scope='Only this small heavily inked glyph remains h|*.',witness_errors='Both witnesses state a star without uncertainty.'),
 dict(habit='Hook, shaft and head must be read independently.',places='(99); two raised connectors; (100), (103), (104).',scope='Headless, plain-shaft and clearly headed forms coexist on this page.',witness_errors='Both witnesses give headed hooked arrows uniformly, including the plain/headless raised connectors.'),
 dict(habit='The h annotation is raised over a separate parenthesized tilde.',places='Clear second insertion label and numbered homotopy maps.',scope='Clear occurrences agree; first inserted label remains obscured.',witness_errors='H repeatedly reduces the label to (h).'),
 dict(habit='A question-shaped mark may be written separately above prose without an exposed lower dot.',places='Above alors.',scope='Independent from the left-margin complete question mark.',witness_errors='C omits the raised mark; H identifies its location in a note.'),
 dict(habit='Abbreviation stops and underline extents are occurrence-specific.',places='d’hom. in (103), d’hom in (104), à vérifier! in margin.',scope='Only detached strokes are included.',witness_errors='H supplies the final hom stop in (104); C extends the underline through ! while H limits it to vérifier.'),
 dict(habit='The digits1 and0 may join into a single bent stem-and-loop group.',places='Label (103).',scope='Resolved locally by the tight number crop.',witness_errors='No witness change; the shape was independently checked rather than accepted from agreement.'),
 dict(habit='Later foliation is thin grey ink, distinct from the author’s heavier number.',places='Lower96 and upper45.',scope='Two numbering hands on this leaf.',witness_errors='H omits the later96.')]
r['abbreviations']=[
 dict(form='loc!',expansion='localement (literal terminal kept)'),
 dict(form='NB',expansion='nota bene'),
 dict(form='déf',expansion='définition'),
 dict(form='resp.',expansion='respectivement'),
 dict(form='équiv.',expansion='équivalence / équivalent, according to construction'),
 dict(form="d'hom.",expansion='d’homotopie'),
 dict(form="d'hom",expansion='d’homotopie; no final stop supplied'),
 dict(form='Drap',expansion='drapeaux, as suggested by the surrounding terminology; not expanded in the source text')]
d=[]
def doubt(place,reading,alts,conf,why,crop):d.append(dict(place=place,reading=reading,alternatives=alts,confidence=conf,reason=why,**ev(crop)))
doubt('(99) parenthetical connector',r'\unsure{\mathrel{\lhook\joinrel\relbar}|\hookrightarrow}',[r'\hookrightarrow'],'medium','The endpoint is an upward blunt nub, unlike clearly separated arrowhead arms elsewhere. Headless is ink-favored, but an abbreviated head cannot be excluded.','arrow99')
doubt('Cancelled old word group before X_i_n*',r'\deleted{\illegible{1} \unsure{du|de}}',['de'],'low','The left group remains unreadable. On the right, d is exposed; the low crossed ending favors u but permits e. Neither complete right-hand word is certified.','cancelled_contient')
doubt('First X in raised parenthesis',r'\unsure{X_{i_n}|X_{i_n}^*}',[r'X_{i_n}^*'],'medium','No star can be isolated independently of the adjacent crowded label, but the overlap prevents ruling it out absolutely.','insertion_first_map')
doubt('First raised connector label, M0728',r'\unsure{(\overset h\sim)}',[],'medium','Parenthesis curves and h/tilde-like strokes remain entangled with a descender from the preceding line. The connector body itself is a visible plain shaft.','insertion_first_map')
doubt('(104), first X superscript',r'X_J^{\unsure{h|*}}',['*'],'medium','The small filled glyph is h-shaped, with an upright and right branches, but a compressed star remains possible. Nearby stars have a different radial construction.','diagram_labels')
r['doubts']=d
boxes=[]
def bx(n,kind,coords,reading):
 assert re.sub(r'\s+',' ',reading).strip() in re.sub(r'\s+',' ',tex),(n,reading)
 boxes.append(dict(box=f'B{n:02}',kind=kind,x0=coords[0],y0=coords[1],x1=coords[2],y1=coords[3],reading=reading))
def part(start,end,inc=True):
 a=tex.index(start);z=tex.index(end,a);return tex[a:z+len(end) if inc else z]
bx(1,'authorial handwritten number',[45,30,124,91],r'\mspage{45}')
bx(2,'whole formula (99), all digits and uncertain connector',[266,146,1551,271],part(r'\[(99)',r'\]'))
bx(3,'complete condition with both word cancellations and raised uncertain insertion',[280,288,1587,427],part('si $Z$ est',r'\mathcal V_{i_n}$)}'))
bx(4,'entire cancelled formula, all zero indices, stars and difference bars',[299,382,1630,492],part(r'\[\deleted{X_{i_n}',r'*)}\]'))
bx(5,'authorial raised question and transition',[286,536,620,622],r'$\overset{?}{\text{alors}}$ on a')
bx(6,'whole formula (100), labels, zero indices and caption',[275,557,1642,741],part(r'\[(100)',r'\]'))
bx(7,'slanted margin question and underlined words',[40,615,246,828],r'\margin{?\quad\uline{à vérifier}!}')
bx(8,'different word métrisable and three ellipsis points',[277,740,1043,869],r'(on suppose $X$ métrisable\ldots)')
bx(9,'generalization paragraph first two lines with indexed expressions',[288,840,1624,1075],part('On va généraliser','où $J$ est une'))
bx(10,'flag, changed capital and continuation count, est and quotation form',[275,1045,1613,1321],part('bande de $I$, resp.','On définit'))
bx(11,'complete formula (101), number, caption and directed limit',[244,1293,1648,1571],part('\\[\n(101)',r'\]'))
bx(12,'complete two-line NB and resolved split verb',[270,1572,1640,1848],part('(NB la définition','partie quelconque de $I$)'))
bx(13,'whole numbered formula (102)',[246,1840,1094,1958],part(r'\[(102)',r'\]'))
bx(14,'On a donc and whole numbered formula (103)',[251,1973,1523,2169],part('On a donc',r"(\text{équiv. d'hom.})\]"))
bx(15,'complete diagram (104), uncertain superscript, vertical equal, caption and condition',[247,2154,1642,2347],part(r'\[(104)',r'$Z\supset X_J$'))
bx(16,'later handwritten foliation',[21,2281,85,2348],r'\margin{96}')
r['second_boxes']=boxes
r['review_status']='Reader complete: candidate, all differences and marks, revisions, inventory, notation, doubts and blind boxes assembled; awaiting root finalization.'
r['validation']=dict(candidate_braces_balanced=None,all_40_diff_ids_in_order=None,all_4_marks_in_order=None,all_37_crops_viewed=True,exact_witness_snippets_checked=True,second_box_readings_checked_as_candidate_substrings=True,no_compilation=True)
f.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
print('Saved full record:',len(r['changes']),'rows;',len(r['diff_coverage']),'differences;',len(r['decisions']),'marks;',len(boxes),'blind boxes;',len(inv),'inventory elements')
