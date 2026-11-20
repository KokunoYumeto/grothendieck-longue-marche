from pathlib import Path
import json
root=Path('/workspace/scratch/8f839dff4bf0/SP74_C13_143+145_work')
packet=json.loads(Path('/workspace/scratch/8f839dff4bf0/reader_packets/143_scan022.json').read_text())
C,H=packet['witness_C'],packet['witness_H']
tex=r'''\scanpage{22}
\mspage{11}
un syst. transitif d'iso. entre les $\pi_t$ $(t\in\unsure{\tau|\mathcal T})$, permettant de les identifier tous à un $=T$. Ainsi $\langle\unsure{\tau|\mathcal T},\pi\rangle$ devient un $T$-groupoïde, c.àd. un groupoïde (pas néc. connexe) où les grpes fondamentaux des comp. conn. sont comm. et tous identifiés à $T$.
De plus, $\unsure{\mathcal E|\Sigma}$ opère sur ce $T$-groupoïde (en opérant également sur $T$) via ses opérations sur le système $(\unsure{\tau|\mathcal T},\pi)$ ($\pi$-espace à gauche) en opérant sur $\unsure{\tau|\mathcal T}$ par l'op. donnée et sur $\pi$ via autom int. de $\unsure{\mathcal E|\Sigma}$, enfin sur $T$ via $\mathcal G$ via $\chi\ldots.$

[Si $\unsure{\mathcal E|\Sigma}$ opère sur $\unsure{\tau|\mathcal T}$, restreignant cette op. à $\pi$ on trouve un groupoïde $\langle\unsure{\tau|\mathcal T},\pi\rangle$ sur lequel $\unsure{\mathcal E|\Sigma}$ opère. Supposant ce groupoïde abélien, on a donc une famille de grpes abéliens \inserted{$(T_j)_{j\in J}$} indexée par $J=\unsure{\tau|\mathcal T}/\pi$, sur laquelle opère $\unsure{\mathcal E|\Sigma}$ via $\unsure{\mathcal E|\Sigma}/\pi=\mathcal G$. Ceci dit, on suppose donné une trivialisation de cette famille $(T_j)$ par $T\simeq T_j$, compatible avec op. de
\mspage{21}
'''
boxes={
'iso-abbreviation':[917,40,1151,123],
'common-identification':[283,241,912,343],
'ie-abbreviation':[1136,354,1388,474],
'grpes-abbreviation':[266,625,1045,746],
'pi-space':[318,1196,1067,1324],
'autom-abbreviation':[1372,1311,1642,1422],
'inner-automorphisms':[302,1443,680,1563],
'restriction':[1109,1552,1641,1694],
'supposing-abelian':[480,1728,1638,1933],
'family-insertion':[847,1860,1627,2021],
'quotient-label':[631,2014,963,2123],
'donne-ending':[476,2204,805,2304],
'parameter-glyph':[289,130,657,237],
}
def crop(name):return 'page' if name is None else 'crops/143_scan022_readerC_'+name+'.png'
changes=[]
def add(place,c,h,final,ac,ah,kind,ink,confidence='high',locus=None,marked=False,consequential=False):
 assert c=='[no witness]' or c in C,(place,'C',c)
 assert h=='[no witness]' or h in H,(place,'H',h)
 assert final in tex,(place,'final',final)
 changes.append(dict(place=place,C=c,H=h,final=final,against_C=ac,against_H=ah,kind=kind,ink=ink,confidence=confidence,crop=crop(locus),box=boxes.get(locus),marked_in_H=marked,consequential=consequential))
add('Beginning of body: H leading ellipsis',"un syst. transitif",r'\ldots\ un syst.\ transitif',"un syst. transitif",False,True,'text not on the page','The first body line begins with un at the left writing margin. No continuation dots precede it on the sheet.')
add('First line: abbreviation of isomorphisms',"d'iso",r"d'isom.","d'iso.",True,True,'abbreviation expanded or spelling modernised','After the dotted i the s and small curled o are visible, followed by a separate short dark stop. There is no additional m before the stop.','high','iso-abbreviation')
add('First formula: t belongs to the round-labelled set',r'(t\in\tau)',r't \in \mathcal{T}',r'(t\in\unsure{\tau|\mathcal T})',False,True,'misread symbol or index','The set glyph has a broad looped top cross-stroke and a rounded lower limb. It is not the 3-like ornate Z graph described in the notation table. Tau versus calligraphic T remains a rendering/identification doubt.','medium','parameter-glyph')
add('Identification of all pi_t with T',r'tous à un $=T$',r'tous : \ill{} $T$',r'tous à un $=T$',False,True,'readable ink left as \\ill{}','The punctiform a with its small upper accent is followed by a low un. Two heavily retraced horizontal bars precede the straight T. The bars are retained as equals, not expanded into a word.','high','common-identification',marked=True,consequential=True)
add('First action-groupoid expression: round set glyph',r'\langle\tau,\pi\rangle',r'\langle \mathcal{T}, \pi'+'\n'+r'\rangle',r'\langle\unsure{\tau|\mathcal T},\pi\rangle',False,True,'misread symbol or index','Inside the first angle brackets the top of the round set letter forms two small loops over a descending curved limb; the second entry is a separate pi. The alphabet identity remains tau/T, not Z.','medium')
add('M0700: explanatory abbreviation',r'\unsure{i.e.|c.àd.}',r'i.e.\ un groupoïde','c.àd.',True,True,'misread word','The first graph is a curved c-like form with retracing, followed by a stop; the middle a is reduced to a small dark mark with an upper accent, and the last letter has a short raised d-stem before the final stop. The sequence supports c.àd. rather than i.e.','medium','ie-abbreviation')
add('Fundamental groups: abbreviated grpes','grpes fondamentaux','groupes fondamentaux','grpes fondamentaux',False,True,'abbreviation expanded or spelling modernised','A looped descending g leads directly to the short r, a downward p-angle and low es tail; there are no separate o-u bodies. The abbreviation has no following stop.','medium','grpes-abbreviation')
add('Connected components: abbreviated conn.','comp. conn.',r'comp.\ connexes','comp. conn.',False,True,'abbreviation expanded or spelling modernised','After comp. the final word is a short c-on-n run followed by a visible stop. There is no written exes ending.')
add('Commutativity and conjunction omitted by H','sont comm. et tous','sont tous','sont comm. et tous',False,True,'omission','A separate short comm. with a dark terminal stop and then the raised t of et appear between sont and tous.','high',consequential=True)
add('De plus: action-group alphabet',r'$\mathcal E$ opère sur ce',r'$\Sigma$ opère sur ce',r'$\unsure{\mathcal E|\Sigma}$ opère sur ce',False,True,'misread symbol or index','The group glyph is rounded with two lobes. The supplied notation table leaves E/Sigma provisional; this row changes no mathematical object.','low')
add('Parenthetical action on T: egalement versus trivialement','en opérant également',r'en opérant trivialement','en opérant également',False,True,'misread word','The word begins with an accented small e and a prominent descending looped g. Those initial strokes support également; there is no initial tr sequence.','high',consequential=True)
add('System pair: round set glyph',r'$(\tau,\pi)$',r'$(\mathcal{T}, \pi)$',r'$(\unsure{\tau|\mathcal T},\pi)$',False,True,'misread symbol or index','The first entry repeats the hooked crossbar and rounded lower limb, followed by its comma and a separately written pi. Tau/calligraphic-T encoding remains uncertain.','medium')
add('M0701 and following words: pi-space on the left',r'($\pi$-\unsure{espace|ens} à gauche)',r'($\pi$-\ill{}'+'\n'+r'\uncertain{prolongeant})',r'($\pi$-espace à gauche)',False,True,'readable ink left as \\ill{}','Following pi and the dash, the e-s start is followed by a distinct descending p, then the punctiform a and low ce strokes. The next word has the small accented a, and gauche has its descending g and tall h. This is espace à gauche, not an ens or prolongeant reading.','high','pi-space',marked=True,consequential=True)
add('After gauche parenthesis: H added comma','à gauche) en',r'\uncertain{prolongeant}), en','à gauche) en',False,True,'text not on the page','The closing parenthesis is followed by a blank gap and en; no separate comma is visible.')
add('Given operation on the round-labelled set',r'sur $\tau$ par',r'sur $\mathcal{T}$ par',r'sur $\unsure{\tau|\mathcal T}$ par',False,True,'misread symbol or index','This line begins with the same round T/tau graph, here with a hooked left top and darkened bottom curve. It is a repeat of the set label, not the straight-stem group T.','medium')
add('Operation on pi: autom abbreviation','via autom',r'via \ill{} \ill{}','via autom',False,True,'readable ink left as \\ill{}','The line-end word consists of a tiny oval a, a low u stroke, a tall angular t and a long low om run. No final period follows autom on the sheet.','high','autom-abbreviation',marked=True)
add('Operation on pi: inner abbreviation','int. de',r'ext.\ de','int. de',False,True,'misread word','At the next line start a small upright i is followed by the stretched n and a final raised t-like turn, then a separate stop. There is no looped e or crossed x supporting ext.','high','inner-automorphisms',consequential=True)
add('Inner automorphisms: action-group alphabet',r'de $\mathcal E$',r'de $\Sigma$',r'de $\unsure{\mathcal E|\Sigma}$',False,True,'misread symbol or index','The same two-lobed group graph follows de; the lower lobe is retraced but does not establish a unique alphabet. Shared E/Sigma uncertainty retained.','low','inner-automorphisms')
add('End of first paragraph: via chi and continuation points',r'via $\chi\ldots.$',r'\uncertain{via} \ill{}\ldots',r'via $\chi\ldots.$',False,True,'readable ink left as \\ill{}','Via is followed by a crossed upper stroke with a long sweeping descender, the same shape of chi used for the map label. Four continuation points follow.','high',marked=True,consequential=True)
add('Lower paragraph: opening square bracket','[Si','Si','[Si',False,True,'omission','A tall left bracket with short horizontal upper and lower returns stands beside Si and the following line. No closing bracket occurs before the page ends.')
add('Conditional clause: action-group alphabet',r'Si $\mathcal E$ opère',r'Si $\Sigma$ opère',r'Si $\unsure{\mathcal E|\Sigma}$ opère',False,True,'misread symbol or index','The conditional starts with the same rounded group letter. E/Sigma remains provisional and non-consequential.','low')
add('Conditional clause: round set label',r'sur $\tau$,',r'sur $\mathcal{T}$,',r'sur $\unsure{\tau|\mathcal T}$,',False,True,'misread symbol or index','The set label has the familiar left hooked top and round lower limb, followed by a comma. No 3-like Z outline is present.','medium')
add('M0702: restricting the action to pi',r'\unsure{restreignant} cette op. à $\pi$',r'\ill{} \ill{}, et \ill{} : $\pi$ \ill{},',r'restreignant cette op. à $\pi$',False,True,'readable ink left as \\ill{}','The word has an initial r/e run, tall t, small dotted i and a large descending g followed by the compressed nant ending. The following cette has two tall t strokes. Op. à pi is present on the next line.','high','restriction',marked=True,consequential=True)
add('After restricted pi: H comma',r'à $\pi$ on',r'$\pi$ \ill{},',r'à $\pi$ on',False,True,'text not on the page','The first tiny dark mark after pi is the o of on, with its low n continuation. There is no descending comma between pi and on.')
add('Lower action-groupoid expression: round set glyph',r'\langle\tau,\pi\rangle',r'\langle \mathcal{T}, \pi \rangle',r'\langle\unsure{\tau|\mathcal T},\pi\rangle',False,True,'misread symbol or index','Inside the lower angle brackets the first glyph has the hooked top and round lower limb, whereas the following pi has two short legs. The same tau/T uncertainty is retained.','medium','supposing-abelian')
add('Action on the resulting groupoid: group alphabet',r'sur lequel $\mathcal E$ opère',r'sur lequel $\Sigma$'+'\n'+'opère',r'sur lequel $\unsure{\mathcal E|\Sigma}$ opère',False,True,'misread symbol or index','The recurring rounded two-lobed group glyph stands between lequel and opère. No new feature settles E versus Sigma.','low','supposing-abelian')
add('Supposing clause: Supposant ce','Supposant ce',r'Supposons \ill{} un','Supposant ce',False,True,'misread word','The line-end verb has S, low u, two descending p strokes and a compressed sant ending with a final raised t turn. The next line begins with a short open ce, rather than un.','medium','supposing-abelian')
add('Supposing clause: abelian groupoid','groupoïde abélien,',r'groupoïde \ill{},','groupoïde abélien,',False,True,'readable ink left as \\ill{}','After groupoïde the punctiform a, rising b, tall l and dotted i with the low en ending precede a comma. The word is abélien.','high','supposing-abelian',marked=True,consequential=True)
add('Consequence of the abelian hypothesis','on a donc une famille',r'\ill{} donné \uncertain{par une}'+'\n'+'famille','on a donc une famille',False,True,'misread word','A short o-n run, isolated small a, a looped initial d of donc, and the low three-part une are separately visible before famille. There is no donné par wording.','high','supposing-abelian',marked=True,consequential=True)
add('Family of groups: abbreviation repeated against both witnesses','groupes abéliens',r'groupes \ill{}','grpes abéliens',True,True,'abbreviation expanded or spelling modernised','The lower word repeats the upper grpes graph: long descending g, stretched r, a single downward p turn and low es tail. No separate o-u bodies are written; grpes is retained at both occurrences.','medium','family-insertion')
add('Family of groups: abeliens readable in H gap','abéliens',r'\ill{} $(T_j)_{j \in J}$','abéliens',False,True,'readable ink left as \\ill{}','The word after grpes has the punctiform a, rising b and l, a dotted i, and the low ens ending. The final s is retained.','high','family-insertion',marked=True,consequential=True)
add('Component index quotient: round set glyph',r'$J=\tau/\pi$',r'$J = \mathcal{T}/\pi$',r'$J=\unsure{\tau|\mathcal T}/\pi$',False,True,'misread symbol or index','J is followed by two equal bars, the same loop-topped round set glyph, a slash and pi. The two tiny detached specks above-right of J do not form a legible prime and are not promoted to one.','medium','quotient-label')
add('Action on the family: group alphabet',r'opère $\mathcal E$ via',r'opère $\Sigma$ via',r'opère $\unsure{\mathcal E|\Sigma}$ via',False,True,'misread symbol or index','The two-lobed group graph starts the line before via; shared E/Sigma uncertainty remains.','low')
add('Quotient group acting on family: alphabet',r'$\mathcal E/\pi=\mathcal G$',r'$\Sigma/\pi = G$',r'$\unsure{\mathcal E|\Sigma}/\pi=\mathcal G$',False,True,'misread symbol or index','The numerator repeats the rounded group letter above slash-pi; the equality and G are visible. Only the E/Sigma alphabet remains unresolved.','low')
add('Final premise: donne ending','suppose donné','suppose donnée','suppose donné',False,True,'misread word','The end of the word has one final low e stroke and its raised acute accent, followed by a wide gap before une. There is no additional final e. The masculine ending is retained.','high','donne-ending')
add('Page-ending compatibility phrase','compatible avec op. de',r'compatible'+'\n'+r'avec \ill{} \ill{}','compatible avec op. de',False,True,'readable ink left as \\ill{}','The last baseline reads compatible, compressed avec, then op. with a descending p and stop, followed by de at the right edge. The sentence remains incomplete at that point.','high',marked=True)
add('Lower-left pencil page numeral',r'\mspage{21}','[no witness]',r'\mspage{21}',False,True,'omission','A pale pencil 2 with a low return is followed by a slender 1 in the lower-left margin. The hand is unnamed.')

inventory=[]
def inv(e,kind,pos,words,hand='his hand'):
 inventory.append(dict(sheet_kind='text',hand=hand,element=e,kind=kind,position=pos,first_words_or_objects=words,transcribed='yes'))
inv('E01','margin note','upper-right margin','Pencil 11',hand='unnamed hand')
inv('E02','text','top three lines','un syst. transitif d’iso. entre les pi_t (t in round-labelled set), permitting identification à un =T')
inv('E03','text','upper quarter','Ainsi angle-bracket groupoid becomes a T-groupoïde; c.àd.; fundamental grpes of comp. conn. are comm. and all identified with T')
inv('E04','text','middle-upper block','De plus, rounded group glyph acts on T-groupoïde, en opérant également sur T, via operations on the pair')
inv('E05','text','middle block','pi-espace à gauche; operations on the round-labelled set, on pi via autom int., and on T via G via chi, with continuation points')
inv('E06','text','lower bracketed opening','Opening square bracket, Si rounded group glyph opère sur round-labelled set; restreignant cette op. à pi; resulting angle-bracket groupoid and action')
inv('E07','text','lower-middle conditional and family statement','Supposant ce groupoïde abélien, on a donc une famille de grpes abéliens, indexée')
inv('E08','insertion','above the line between abéliens and indexée','(T_j) indexed by j in J; not cancelled')
inv('E09','text','lower block below insertion','par J = round-labelled set / pi, sur laquelle opère rounded group glyph via rounded group glyph / pi = G')
inv('E10','text','last three written lines','Ceci dit, on suppose donné une trivialisation de cette famille (T_j) par T simeq T_j, compatible avec op. de; continuing beyond sheet')
inv('E11','margin note','bottom-left margin','Pencil 21',hand='unnamed hand')

report=dict(
 key='143_scan022',reader='C',stage='first',image_views=['original','half1','half2'],changes=changes,
 decisions=[
 dict(id='M0700',decision='alternative',reading='c.àd.',ink='A curved/retraced c-like opening is followed by a stop, then a punctiform a with an upper accent and a short raised d-stem before the final stop. This supports the alternative c.àd.; the opening mark is part of the abbreviation, not a separate deletion.',crop=crop('ie-abbreviation'),box=boxes['ie-abbreviation'],confidence='medium'),
 dict(id='M0701',decision='first',reading='espace',ink='The small e-s start is followed by a distinct descending p, a punctiform a and a low ce ending; the whole parenthesis reads pi-espace à gauche.',crop=crop('pi-space'),box=boxes['pi-space'],confidence='high'),
 dict(id='M0702',decision='first',reading='restreignant',ink='Initial r/e strokes lead to tall t, dotted i and a round g with a long descending loop, then the compressed nant ending. The following cette has two tall t strokes.',crop=crop('restriction'),box=boxes['restriction'],confidence='high')
 ],
 inventory=inventory,
 remaining_doubts=[
 dict(place='Rounded extension/action group, six occurrences',reading=r'\unsure{\mathcal E|\Sigma}',alternatives=r'\mathcal E or \Sigma',confidence='low',reason='The supplied notation table keeps this identification provisional. All six local occurrences have rounded lobes and supply no decisive new feature. Pure alphabet rows are non-consequential.'),
 dict(place='Round set label, seven occurrences',reading=r'\unsure{\tau|\mathcal T}',alternatives='Greek tau or calligraphic capital T',confidence='medium',reason='The top stroke is looped or hooked and the lower limb is rounded. It is consistently distinct from the straight T group label, but the Greek/Latin encoding cannot be established from these forms. No ornate Z encoding is imposed. Crops parameter-glyph, supposing-abelian and quotient-label show representative local variants.')
 ],
 certainty_resolutions=[
 dict(place='M0701',C=r'\unsure{espace|ens}',final='espace',ink='A descending p and following a-ce strokes distinguish espace from the short ens alternative.'),
 dict(place='M0702',C=r'\unsure{restreignant}',final='restreignant',ink='The tall t, dotted i, long g descender and nant ending are visible in the crop.'),
 dict(place='Action-group alphabet, six occurrences',C=r'\mathcal E',final=r'\unsure{\mathcal E|\Sigma}',ink='Shared provisional notation retained at low confidence; adding the uncertainty alone is not counted as a reading change against C.'),
 dict(place='Round set-label alphabet, seven occurrences',C=r'\tau',final=r'\unsure{\tau|\mathcal T}',ink='The recurring hooked/looped top and rounded lower limb admit both tau and calligraphic T. C’s primary reading is retained with the alternative explicit.')
 ],
 notation=[
 dict(form=r'\unsure{\tau|\mathcal T}',meaning='Set on which pi and the extension group act; object label of the associated action groupoid',evidence='Seven occurrences in the t-membership condition, groupoid brackets, pair, action clauses and quotient J. The graph is round with a hooked or looped top, unlike the earlier ornate Z description supplied by main.'),
 dict(form=r'\pi_t',meaning='The indexed groups to be identified with T',evidence='First formula has a two-legged pi and a small crossed t; the membership condition repeats t.'),
 dict(form=r'\langle\tau,\pi\rangle',meaning='The source’s angle-bracket notation for the action groupoid, with the tau/T alphabet unresolved',evidence='Two angle-bracket pairs on the page, each containing the round set label then pi.'),
 dict(form=r'\unsure{\mathcal E|\Sigma}',meaning='The extension/action group',evidence='Six rounded two-lobed occurrences; provisional identity kept at low confidence according to main’s instruction.'),
 dict(form='T',meaning='The group used to identify the fundamental groups and trivialize the family',evidence='A broad straight cap and short downward stem distinguish T from the round set label.'),
 dict(form=r'(T_j)_{j\in J}',meaning='Inserted notation for the abelian group family',evidence='Written above the family line before indexée; j in J is lowered to the right of the closing parenthesis. No cancellation crosses it.'),
 dict(form='J',meaning='The quotient index set, round-labelled set divided by pi',evidence='The source writes a broad J, equals, round set label/slash/pi. Two tiny specks above-right are not a legible prime.'),
 dict(form=r'\chi',meaning='Map through which the action on T is said to pass',evidence='A crossed top with a long curved descender follows the second via at the end of the first paragraph.'),
 dict(form='$=$ in à un =T',meaning='Two-bar shorthand, possibly for même; retained literally',evidence='Both bars are visibly retraced. No word is supplied between un and T.'),
 dict(form=r'\mathcal G',meaning='Quotient group through which the action is said to pass',evidence='Large G with long descending right limb; C’s calligraphic versus H’s plain rendering is not treated as a separate source variable.')
 ],
 abbreviations=[
 dict(form='syst.',expansion='système'),
 dict(form='iso.',expansion='isomorphismes; source has no m'),
 dict(form='c.àd.',expansion='c’est-à-dire'),
 dict(form='néc.',expansion='nécessairement'),
 dict(form='grpes',expansion='groupes; abbreviation retained at both occurrences'),
 dict(form='comp.',expansion='composantes'),
 dict(form='conn.',expansion='connexes'),
 dict(form='comm.',expansion='commutatifs'),
 dict(form='op.',expansion='opération(s), by context'),
 dict(form='autom',expansion='automorphismes; no final dot added'),
 dict(form='int.',expansion='intérieurs')
 ],
 hand_log=[
 dict(habit='The round set graph has a looped or hooked top and a curved lower limb.',places='All seven set-label occurrences on scan022.',scope='All seven visually checked; several local variants shown in crops.',misreadings='C encodes tau and H calligraphic T. They are preserved as alternatives; the form is not forced into the earlier ornate Z encoding.'),
 dict(habit='Small a can be punctiform, leaving its accent to look like a colon.',places='à un =T; middle of c.àd.; à gauche; à pi.',scope='These four examples inspected, with the first three enlarged.',misreadings='H reads a colon in the identification phrase; the local accented-a form supports à.'),
 dict(habit='The abbreviation grpes runs g-r-p-es without separate o/u bodies.',places='grpes fondamentaux; famille de grpes abéliens.',scope='Both occurrences directly compared in their crops.',misreadings='H expands the first occurrence; both witnesses expand the second to groupes.'),
 dict(habit='Dots and short terminal strokes distinguish abbreviated forms.',places='d’iso.; comm.; conn.; autom; int.',scope='All these occurrences inspected individually; iso and autom/int cropped.',misreadings='C omits the stop after iso; H adds m in isom. and expands conn.; no dot is added to autom.'),
 dict(habit='The initial g descender can make a long word’s identity visible even when its middle is compressed.',places='également; restreignant.',scope='Both inspected; restreignant enlarged.',misreadings='H gives trivialement for également and gaps for restreignant; the descending g and other letter strokes support C’s words.'),
 dict(habit='T and its indexed occurrences may have a slightly curved cap while retaining a straight short stem.',places='Group T throughout, inserted (T_j) family, and final T simeq T_j.',scope='All local T occurrences inspected; inserted family enlarged.',misreadings='No hat or extra decoration is supplied from a curved T cap.'),
 dict(habit='Very small detached dark specks do not by themselves establish primes.',places='Above-right of J in J = round set/pi.',scope='This occurrence only.',misreadings='Neither witness gives a prime; the crop shows two tiny isolated specks rather than a legible prime stroke.')
 ],
 notes=[
 dict(id='143_scan022-N1',text='The source continues with a transitive system of isomorphisms between pi_t, used to identify all these groups with a common T, written literally à un =T. It calls the resulting angle-bracket object a T-groupoïde and explains that the fundamental groups of its connected components are commutative and all identified with T. No missing antecedent or preceding-page content is supplied.'),
 dict(id='143_scan022-N2',text='The page says the extension group acts on this T-groupoid en opérant également sur T, through its actions on the pi-espace à gauche, on pi via autom int. of the extension group, and on T through G and chi. These are source statements; the reading également is supported by its initial accented e and descending g, and int. is not regularized to ext.'),
 dict(id='143_scan022-N3',text='The lower bracketed paragraph restricts the action to pi, forms the action groupoid, assumes that groupoid abelian, and describes a family of abelian groups indexed by J equal to the round-labelled set modulo pi. The family notation (T_j) indexed by j in J is interlinear and retained as an insertion. The page says the extension-group action passes through its quotient G.'),
 dict(id='143_scan022-N4',text='The final premise is written on suppose donné une trivialisation, with donné lacking the extra feminine e. It gives T simeq T_j and ends mid-phrase at compatible avec op. de. The opening square bracket remains unclosed on this sheet; no continuation or grammatical repair is added.'),
 dict(id='143_scan022-N5',text='Both pencil numerals, 11 in the upper-right and 21 in the lower-left, are transcribed but their hand is unnamed. H’s phrase de l’auteur is editorial and is not used to attribute the pencil. The round tau/T label remains distinct from any earlier ornate Z, while E/Sigma remains the shared provisional notation at low confidence.')
 ],
 check_events=[
 dict(statement_id='143_scan022-T-groupoid-description',type='carried as background without fault found',outcome='Read as the source’s description. No proof of the transitive identification system or equivalence of the T-groupoid description was performed; source spelling and shorthand were preserved.'),
 dict(statement_id='143_scan022-extension-action',type='carried as background without fault found',outcome='No compatibility or descent proof was undertaken. The choices également, pi-espace à gauche and autom int. were decided from visible letters, not from what an action should require.'),
 dict(statement_id='143_scan022-abelian-family-and-trivialization',type='carried as background without fault found',outcome='The asserted family, quotient action and trivialization were carried as source background only. No proof that the action factors through G or that a compatible trivialization exists was attempted.')
 ],
 unresolved_for_main=[
 'Tau/calligraphic-T alphabet remains explicit at all seven positions. Representative crops: crops/143_scan022_readerC_parameter-glyph.png, crops/143_scan022_readerC_supposing-abelian.png, and crops/143_scan022_readerC_quotient-label.png.',
 'Shared rounded E/Sigma alphabet remains provisional at all six positions; all pure group-alphabet rows are low confidence and consequential false.'
 ],
 raw_difference_disposition='All '+str(len(packet['differences']))+' packet difference entries and the full text were inspected against the original once and each native half once. Every word, mathematical sign/index, punctuation mark, insertion, bracket and both pencil numerals was checked, including C/H agreements. One crop per unresolved locus was made; no decided locus was recropped. Original MARKS M0700, M0701 and M0702 are the only decision IDs. Macro wrappers, mathematical spacing, H’s editorial page note and plain-versus-calligraphic G rendering are excluded from material rows. Tau/T alphabet-only rows are medium and non-consequential; pure E/Sigma rows are low and non-consequential. The insertion wrapper for the otherwise shared family formula is recorded in the inventory rather than counted as a macro-only difference. No diagram, genuine drawing or cancelled text was found. No OCR, web research or TeX compilation was used.'
)
assert [d['id'] for d in report['decisions']]==[m['id'] for m in packet['marks']]
assert tex.count(r'\unsure{\mathcal E|\Sigma}')==6
assert tex.count(r'\unsure{\tau|\mathcal T}')==7
assert len({i['element'] for i in inventory})==len(inventory)
for row in changes:
 if row['crop']!='page': assert (root/row['crop']).exists()
for row in changes:
 if row['confidence']=='low': assert not row['consequential']
(root/'reviews'/'143_scan022_readerC.tex').write_text(tex)
(root/'reviews'/'143_scan022_readerC.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'changes':len(changes),'decisions':len(report['decisions']),'inventory':len(inventory),'remaining_doubts':len(report['remaining_doubts']),'raw_differences':len(packet['differences']),'literal_excerpt_validation':'passed','tex':'reviews/143_scan022_readerC.tex','json':'reviews/143_scan022_readerC.json'}))
