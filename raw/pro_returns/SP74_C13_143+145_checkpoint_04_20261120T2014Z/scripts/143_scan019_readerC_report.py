from pathlib import Path
import json
root = Path('/workspace/scratch/8f839dff4bf0/SP74_C13_143+145_work')
packet = json.loads(Path('/workspace/scratch/8f839dff4bf0/reader_packets/143_scan019.json').read_text())
C, H = packet['witness_C'], packet['witness_H']
tex = r'''\scanpage{19}
\uline{Définition de $\beta$}\qquad On définit
\[
\beta(\Pi,\widetilde\Pi,p,\mathcal G,\unsure{\sim|a})=(\unsure{\mathcal E|\Sigma},\mathcal G,\pi,\mathfrak Z)\quad\text{ainsi :}
\]
$\unsure{\mathcal E|\Sigma}=$ groupe des couples $(g,\bar g)$, avec $g\in\mathcal G$, $\bar g\in\operatorname{Aut}(\widetilde\Pi)$ compatible avec $g$
\[
\pi=\operatorname{Aut}(\widetilde\Pi/\Pi)
\]
$\unsure{\mathcal E|\Sigma}\longrightarrow\mathcal G$ par $(g,\bar g)\longmapsto g$, d'où
\diagram{\begin{tikzcd}[ampersand replacement=\&]
1 \arrow[r,dash] \& \pi \arrow[r] \& \unsure{\mathcal E|\Sigma} \arrow[r,dash] \& \mathcal G \arrow[r] \& 1
\end{tikzcd}}
$\mathfrak Z=\operatorname{Ob}\widetilde\Pi$, avec opération évidente de $\unsure{\mathcal E|\Sigma}$ sur $\mathfrak Z\ldots$

Variantes profinies\ldots

\textcircled{8} Considérons, avec notations \deleted{\unsure{du|de}} \S 7,
\[
\left(\diagram{\begin{tikzcd}[ampersand replacement=\&]
1 \arrow[r,dash] \& \pi \arrow[r,dash] \& \unsure{\mathcal E|\Sigma} \arrow[r] \& \mathcal G \arrow[r,dash] \& 1
\end{tikzcd}}
\quad\text{et }\mathfrak Z\quad\unsure{\mathcal E|\Sigma}\text{-ens}\ne\varnothing\text{ sur lequel }\pi\text{ opère librement}\right)
\]
$\longleftrightarrow(\Pi,\widetilde\Pi,p,\mathcal G,\unsure{\sim|a})$. On va interpréter la donnée d'un triple $(\inserted{\chi,}\unsure{\tau|\mathcal T},T,\Phi)$, \inserted{$\chi:$} où $\unsure{\tau|\mathcal T}$ est un $\unsure{\mathcal E|\Sigma}$-ens, $T$ un groupe $(\simeq\widehat{\mathbf Z}\;?)$, \inserted{$\chi:\mathcal G\longrightarrow\operatorname{Aut}(T)$ \unsure{$(\simeq\widehat{\mathbf Z}^{*}\;\text{canon.}?)$}} et
\diagram{\begin{tikzcd}[ampersand replacement=\&]
\Phi:\unsure{\tau|\mathcal T} \arrow[r] \& \operatorname{Hom}_{\mathrm{gr}}(T,\pi)
\end{tikzcd}}
compatible avec op. de $\unsure{\mathcal E|\Sigma}$ (opérant
\mspage{18}
'''
boxes = {
'beta-formula':[245,195,1335,350],
'pair-where':[1000,340,1615,535],
'pi-identity':[330,475,1050,612],
'upper-extension':[565,737,1240,869],
'section-deletion':[1015,1345,1620,1474],
'lower-extension':[325,1485,1000,1617],
'lower-tuple':[555,1690,1230,1840],
'triple-insertions':[590,1868,1538,2065],
'group-question':[803,2037,1635,2178],
'chi-parenthesis-map':[300,2125,1415,2290],
}
def crop(name):
    return 'page' if name is None else 'crops/143_scan019_readerC_'+name+'.png'
changes=[]
def add(place, c, h, final, ac, ah, kind, ink, confidence='high', locus=None, marked=False, consequential=False):
    assert c == '[no witness]' or c in C, (place,'C',c)
    assert h == '[no witness]' or h in H, (place,'H',h)
    assert final in tex, (place,'final',final)
    changes.append(dict(place=place,C=c,H=h,final=final,against_C=ac,against_H=ah,kind=kind,ink=ink,confidence=confidence,crop=crop(locus),box=boxes.get(locus),marked_in_H=marked,consequential=consequential))
add('Heading: punctuation after beta',r'\uline{Définition de $\beta$}\qquad On définit',r'\emph{Définition de $\beta$}. On définit',r'\uline{Définition de $\beta$}\qquad On définit',False,True,'text not on the page','The underlining ends with the heading; the gap before On définit contains no full stop.')
add('Beta input tuple: final component',r'p,\mathcal G,a)',r'p, G, \sim)',r'p,\mathcal G,\unsure{\sim|a})',True,False,'misread symbol or index','A short low undulating stroke follows the last comma. There is no closed bowl or separate upright establishing a; the wave reading is first, with the compressed-a alternative retained.','medium','beta-formula',consequential=True)
add('Beta output tuple: rounded group glyph and ornate Z',r'(\mathcal E,\mathcal G,\pi,Z)',r'(\Sigma, G, \pi, \mathfrak{Z})',r'(\unsure{\mathcal E|\Sigma},\mathcal G,\pi,\mathfrak Z)',True,True,'misread symbol or index','The first output glyph has two rounded lobes. The final glyph has an angular upper turn and a long curled lower tail, encoded as mathfrak Z. Group-glyph uncertainty follows the supplied notation table; these are alphabet encodings.','medium','beta-formula')
add('Pair definition: initial group glyph',r'$\mathcal E=$',r'$\Sigma$ =',r'$\unsure{\mathcal E|\Sigma}=$',False,True,'misread symbol or index','The rounded two-lobed group glyph precedes the equals sign; its E/Sigma identity remains the shared provisional reading.','medium')
add('Pair definition: connective following the ordered pair',r'$(g,\bar g)$, où',r'$(g, \bar g)$, avec',r'$(g,\bar g)$, avec',True,False,'misread word','The punctiform first oval, short rising central stroke and final shallow wave repeat the compressed avec immediately below in compatible avec g. The word is longer and more segmented than a simple ou.','high','pair-where')
add('Projection to G: initial group glyph',r'$\mathcal E\longrightarrow\mathcal G$',r'$\Sigma \to G$',r'$\unsure{\mathcal E|\Sigma}\longrightarrow\mathcal G$',False,True,'misread symbol or index','The same rounded group glyph starts the projection. Its following shaft has a small right-facing head; only the alphabet identification remains provisional.','medium')
add('Upper extension: connector shapes',r'1 \arrow[r,dash] \& \pi \arrow[r] \& \mathcal E \arrow[r,dash] \& \mathcal G \arrow[r] \& 1',r'1 \to \pi \longrightarrow \Sigma \longrightarrow G \to 1',r'1 \arrow[r,dash] \& \pi \arrow[r] \& \unsure{\mathcal E|\Sigma} \arrow[r,dash] \& \mathcal G \arrow[r] \& 1',False,True,'drawing or diagram','The first and third links end in rounded pen stops without angular heads. The second has a compact pointed end and the fourth a raised black head before the terminal 1. Confidence here concerns connectors; the group alphabet is still provisional.','high','upper-extension',consequential=True)
add('Object-set definition: ornate Z',r'$Z=\operatorname{Ob}\widetilde\Pi$',r'$\mathfrak{Z} = \mathrm{Ob}\,\widetilde{\Pi}$',r'$\mathfrak Z=\operatorname{Ob}\widetilde\Pi$',True,False,'misread symbol or index','The object-set letter repeats the 3-like upper turn and deep curling tail of the beta output. Mathfrak Z encodes this handwriting without changing the object-set label.','medium')
add('Action on the object set: group and set alphabets',r'$\mathcal E$ sur $Z\ldots$',r'$\Sigma$ sur $\mathfrak{Z}$…',r'$\unsure{\mathcal E|\Sigma}$ sur $\mathfrak Z\ldots$',True,True,'misread symbol or index','The action-group glyph is the same rounded two-lobed form; the following set letter has the same long curled tail. The continuation dots are present in both full witnesses.','medium')
add('Paragraph number 8',r'\textcircled{8} Considérons',r'(8) Considérons',r'\textcircled{8} Considérons',False,True,'other','A near-continuous rounded enclosure surrounds the 8, including its top; it is not a pair of textual parentheses.')
add('Before section 7: cancelled preposition',r'\deleted{\unsure{du|de}}',r'notations de (7)',r'\deleted{\unsure{du|de}}',False,True,'deletion state','A dense horizontal cancellation crosses a surviving d-like ascender. The following vowel is covered; du/de remains unresolved. The word is cancelled, whereas H prints a live de.','medium','section-deletion')
add('Reference to section 7',r'\S 7',r'(7)',r'\S 7',False,True,'misread symbol or index','A vertical double-curving section sign immediately precedes 7; there are no surrounding parentheses at this reference.','high','section-deletion')
add('Lower extension: connector shapes',r'1 \arrow[r,dash] \& \pi \arrow[r,dash] \& \mathcal E \arrow[r] \& \mathcal G \arrow[r,dash] \& 1',r'1 \to \pi \to \Sigma \to G \to 1',r'1 \arrow[r,dash] \& \pi \arrow[r,dash] \& \unsure{\mathcal E|\Sigma} \arrow[r] \& \mathcal G \arrow[r,dash] \& 1',False,True,'drawing or diagram','The first two links are horizontal shafts with blunt stops. Only the middle group-to-G link has a convergent pointed head. The terminal link has a short return of the pen but no right-pointing head. The isolated tiny mark above the first shaft is not a legible added symbol.','high','lower-extension',consequential=True)
add('Lower recap: ornate Z and action-group alphabet',r'\text{et }Z\quad\mathcal E\text{-ens}',r'et $\mathfrak{Z}$ $\Sigma$-ens.',r'\text{et }\mathfrak Z\quad\unsure{\mathcal E|\Sigma}\text{-ens}',True,True,'misread symbol or index','The large set letter has the same 3-shaped head and sweeping bottom curl; the action-group label again has the two rounded lobes. Alphabet encodings only.','medium')
add('Lower recap: punctuation of ens',r'\text{-ens}\ne\varnothing',r'$\Sigma$-ens.',r'\text{-ens}\ne\varnothing',False,True,'text not on the page','The final s of ens is followed directly by the non-equality sign across a normal gap. No period is visible before the sign.')
add('Lower groupoid tuple: final component',r'(\Pi,\widetilde\Pi,p,\mathcal G,a)',r'(\Pi, \widetilde{\Pi}, p, G, \sim)',r'(\Pi,\widetilde\Pi,p,\mathcal G,\unsure{\sim|a})',True,False,'misread symbol or index','The last component is an open two-humped wave without a closed bowl. It resembles the short wave in the beta input, but a highly compressed a is not excluded.','medium','lower-tuple',consequential=True)
add('Tuple called triple: inserted chi and comma',r'\inserted{\chi,}',r"donnée d'un triple $(\mathcal{T}, T, \Phi)$",r'\inserted{\chi,}',False,True,'omission','A small crossed stem with a long descending hook, followed by a comma, is squeezed between the left parenthesis and the large round set-label glyph. It is a chi insertion, not a superscript on the following letter.','high','triple-insertions',marked=True,consequential=True)
add('Tuple called triple: round set-label glyph',r'\tau,T,\Phi',r'\mathcal{T}, T, \Phi',r'\unsure{\tau|\mathcal T},T,\Phi',False,True,'misread symbol or index','The letter has a long top cross-stroke, left downward hook and round lower limb; the first occurrence has a loop at the top crossing. These strokes admit tau or a round calligraphic T. Both encodings are retained for the same source label.','medium','triple-insertions')
add('Isolated interlinear chi-colon above ou',r'où $\tau$ est un',r'\marginal{interligne : « $\chi$ : »}',r'\inserted{$\chi:$} où $\unsure{\tau|\mathcal T}$ est un',True,True,'insertion or placement','A separate small crossed descending chi and two vertically aligned dots stand above où, after the tuple. It is distinct from the tiny chi inside the tuple and from the full chi map below. No attachment arrow is present; it is retained at its visible interlinear position.','high','triple-insertions',consequential=True)
add('Description after ou: round set-label glyph',r'où $\tau$ est',r'où $\mathcal{T}$ est',r'où $\unsure{\tau|\mathcal T}$ est',False,True,'misread symbol or index','This occurrence repeats the top bar, left hook and rounded lower stroke, here without the closed top loop. Tau versus calligraphic T remains an alphabet-reading doubt.','medium','triple-insertions')
add('Description after ou: action-group glyph',r'un $\mathcal E$-ens',r'un $\Sigma$-ens.',r'un $\unsure{\mathcal E|\Sigma}$-ens',False,True,'misread symbol or index','The two-lobed group glyph repeats the extension label, with no new feature settling E against Sigma.','medium')
add('Description after ou: no period after ens',r'$\mathcal E$-ens, $T$',r'$\Sigma$-ens., $T$',r'$\unsure{\mathcal E|\Sigma}$-ens, $T$',False,True,'text not on the page','A single descending comma follows ens; there is no separate period before it.')
add('After T: H supposed cancelled text',r'$T$ un groupe',r'$T$'+'\n'+r'\struck{\ill{}} un groupe',r'$T$ un groupe',False,True,'text not on the page','The apparent crossing below the start of un belongs to the hat on Z in the inserted lower line. No independent cancelled word lies between T and un groupe.','high','group-question',marked=True)
add('After groupe: H supposed unreadable text',r'un groupe $(\simeq\widehat{\mathbf Z}\;?)$',r'un groupe \uncertain{\ill{}} ($\simeq \widehat{\mathbb{Z}}$ ?)',r'un groupe $(\simeq\widehat{\mathbf Z}\;?)$',False,True,'text not on the page','The final low stroke of groupe is followed by the opening parenthesis of the displayed comparison. No extra word or separate cancelled/unreadable segment occupies the gap.','high','group-question',marked=True)
add('Inserted Aut(T) parenthesis: canon. and unresolved punctuation',r'\unsure{$(\simeq\widehat{\mathbf Z}^{*}\;\text{canon.}?)$}',r'($\simeq \widehat{\mathbb{Z}}^{*}$'+'\n'+r'\uncertain{\ill{}})',r'\unsure{$(\simeq\widehat{\mathbf Z}^{*}\;\text{canon.}?)$}',False,True,'readable ink left as \\ill{}','The insert has a hat on Z, a raised star, then a tall curved stroke and a compressed c-a-n-o-n sequence with a stop and a raised question-like mark. Canon. is readable, but the intervening curved stroke and exact parenthesis extent remain unsecured, so the whole C proposal stays unsure.','medium','group-question',marked=True,consequential=True)
add('After inserted parenthesis: H comma before et',r'\text{canon.}?)$}} et',r'\uncertain{\ill{}}), et',r'\text{canon.}?)$}} et',False,True,'text not on the page','The small closing curve ends the insertion; no separate comma is visible after it before et starts on the next baseline.','high','group-question')
add('Phi map: round domain glyph',r'\Phi:\tau',r'\Phi : \mathcal{T}',r'\Phi:\unsure{\tau|\mathcal T}',False,True,'misread symbol or index','The map domain repeats the curved T/tau graph, with its left hook and round lower limb. The arrow has a distinct filled triangular right head; the glyph identity alone remains doubtful.','medium','chi-parenthesis-map')
add('Final compatibility line: action-group glyph',r'op. de $\mathcal E$',r'op.\ de $\Sigma$',r'op. de $\unsure{\mathcal E|\Sigma}$',False,True,'misread symbol or index','The same rounded two-lobed group letter follows de in the last line; the sentence ends with the open parenthetical opérant.','medium')
add('Lower-left pencil numeral',r'\mspage{18}','[no witness]',r'\mspage{18}',False,True,'omission','Two faint pencil digits sit at the lower left: a slanted 1 and an 8 with two closed bowls. The writing hand is not attributed.')

inventory=[]
def inv(e, kind, pos, words, hand='his hand'):
    inventory.append(dict(sheet_kind='text',hand=hand,element=e,kind=kind,position=pos,first_words_or_objects=words,transcribed='yes'))
inv('E01','text','top heading','Underlined Définition de beta; On définit')
inv('E02','display','first displayed line','beta(Pi, tilde Pi, p, G, wave) = (rounded group glyph, G, pi, ornate Z), ainsi :')
inv('E03','text','upper quarter, two lines','Group of pairs (g, bar g), avec g in G; bar g in Aut(tilde Pi), compatible avec g')
inv('E04','display','upper quarter below pair definition','pi = Aut(tilde Pi/Pi)')
inv('E05','text','above first extension','Rounded group glyph to G, par (g, bar g) maps to g, d’où')
inv('E06','diagram','upper-middle extension','1 — pi → rounded group glyph — G → 1')
inv('E07','text','middle, before profinite variants','Ornate Z = Ob tilde Pi, avec opération évidente de rounded group glyph sur ornate Z…')
inv('E08','text','middle, above circled 8','Variantes profinies…')
inv('E09','text','lower-half opening','Circled 8; Considérons, avec notations [cancelled word] §7,')
inv('E10','deletion','between notations and §7','Cancelled du/de under a thick horizontal stroke')
inv('E11','diagram','beginning of parenthesized lower recap','1 — pi — rounded group glyph → G — 1')
inv('E12','text','remainder of parenthesized lower recap','et ornate Z, rounded-group-ens nonempty, sur lequel pi opère librement')
inv('E13','display','below recap','Double-headed equivalence shaft and (Pi, tilde Pi, p, G, wave)')
inv('E14','text','lower third, following recap','On va interpréter la donnée d’un triple (...)')
inv('E15','insertion','inside left parenthesis of tuple','Small chi and comma before the round T/tau glyph')
inv('E16','insertion','interline above où following tuple','Separate chi and colon; no explicit attachment stroke')
inv('E17','text','description of tuple data','où round T/tau est un rounded-group-ens, T un groupe (simeq hat Z ?)')
inv('E18','insertion','squeezed between data-description line and Phi map','chi : G → Aut(T), with uncertain hat-Z-star / canon.? parenthesis')
inv('E19','diagram','near foot, beginning with et','Phi : round T/tau → Hom_gr(T, pi)')
inv('E20','text','last ink line','compatible avec op. de rounded group glyph (opérant; unfinished at page end')
inv('E21','margin note','bottom-left pencil','18',hand='unnamed hand')

report = dict(
key='143_scan019',reader='C',stage='first',image_views=['original','half1','half2'],changes=changes,
decisions=[dict(id='M0698',decision='undecided',reading=r'\unsure{$(\simeq\widehat{\mathbf Z}^{*}\;\text{canon.}?)$}',ink='Hat, raised star and the letters canon. are visible. A tall curved stroke directly after the star might close a parenthesis or belong to an unresolved question-like sign; the final small mark and parenthesis grouping are not secure. Retain the whole proposed parenthesis as uncertain.',crop=crop('group-question'),box=boxes['group-question'],confidence='medium')],
inventory=inventory,
remaining_doubts=[
 dict(place='Beta input tuple, final component',reading=r'\unsure{\sim|a}',alternatives='Wave/sim versus a very compressed a',confidence='medium',reason='Short wave with no closed bowl; the role of an action parameter was not used to complete the letter. See crops/143_scan019_readerC_beta-formula.png.'),
 dict(place='Lower groupoid tuple, final component',reading=r'\unsure{\sim|a}',alternatives='Wave/sim versus a very compressed a',confidence='medium',reason='Open double-humped mark repeats the upper parameter but is not an unambiguous a. See crops/143_scan019_readerC_lower-tuple.png.'),
 dict(place='Rounded extension/action-group glyph, all nine occurrences',reading=r'\unsure{\mathcal E|\Sigma}',alternatives=r'\mathcal E or \Sigma',confidence='medium',reason='The current shared notation decision preserves this alphabet identification. All nine local occurrences were visually checked; no occurrence settles the graph independently.'),
 dict(place='Cancelled word before section 7',reading=r'\deleted{\unsure{du|de}}',alternatives='du or de under cancellation',confidence='low',reason='The d-like ascender survives, but a dense horizontal strike hides the vowel. See crops/143_scan019_readerC_section-deletion.png.'),
 dict(place='Round set-label glyph in tuple, after où, and in Phi domain',reading=r'\unsure{\tau|\mathcal T}',alternatives='Greek tau or round calligraphic capital T',confidence='medium',reason='All three occurrences share a left hooked top stroke and rounded lower limb. The first has an extra loop at its top crossing; this does not establish a unique alphabet. See triple-insertions and chi-parenthesis-map crops.'),
 dict(place='Isolated chi-colon above où: attachment',reading=r'\inserted{$\chi:$}',alternatives='Unattached inserted start, perhaps a first start of the chi definition subsequently written below',confidence='medium',reason='The chi and colon themselves are legible. No insertion caret or deletion connects them to a precise phrase; they are retained immediately before où to preserve the visible position, not silently merged with the full map below.'),
 dict(place='M0698: dense inserted comparison with Aut(T)',reading=r'\unsure{$(\simeq\widehat{\mathbf Z}^{*}\;\text{canon.}?)$}',alternatives='The original proposed parenthesis; possibly a close/question-like stroke immediately after Z-star, with different parenthesis grouping',confidence='medium',reason='Canon. is readable but a tall curved stroke after the star remains unidentified and the punctuation is crowded by the line above. See crops/143_scan019_readerC_group-question.png; left portion and map location also in chi-parenthesis-map crop.')
],
certainty_resolutions=[
 dict(place='Rounded extension/action-group glyph, nine instances',C=r'\mathcal E',final=r'\unsure{\mathcal E|\Sigma}',ink='The shared notation table calls for the E/Sigma uncertainty; local rounded forms do not settle it. This certainty downgrade alone is not counted as a change against C.'),
 dict(place='Round set-label glyph, three instances',C=r'\tau',final=r'\unsure{\tau|\mathcal T}',ink='The top hook/crossbar and rounded limb admit either tau or a calligraphic T. C’s first reading is retained, with the competing alphabet encoding explicitly marked.')
],
notation=[
 dict(form=r'\unsure{\mathcal E|\Sigma}',meaning='Group of compatible pairs, used as the extension/action group',evidence='Defined explicitly as pairs (g, bar g) in the top block and repeated nine times. Shared provisional notation retained.'),
 dict(form=r'\mathcal G',meaning='The group serving as the quotient/action group in the displayed data',evidence='The large open G has a long descending right stem in both tuples and the two diagrams. C’s encoding is retained; H’s ordinary G is a font alternative.'),
 dict(form=r'\mathfrak Z',meaning='The object-set label',evidence='Defined as Ob tilde Pi and drawn with a 3-like upper part plus long curling tail in all four occurrences. Fraktur versus plain Z is an alphabet encoding only.'),
 dict(form=r'\unsure{\tau|\mathcal T}',meaning='The set label in the inserted data and the domain of Phi',evidence='Three occurrences with the same hooked crossbar and rounded lower stroke; the Greek/Latin font identification is unestablished.'),
 dict(form=r'\Phi',meaning='Map from the round-labelled set to Hom_gr(T, pi)',evidence='Large loop crossed by a central upright in the tuple and the displayed map.'),
 dict(form=r'\chi',meaning='Added datum with visible map G to Aut(T)',evidence='Small crossed descender in tuple, a separate interlinear chi-colon, and the full inserted map.'),
 dict(form=r'\widehat{\mathbf Z}',meaning='The hatted integer-group notation in the author’s questions',evidence='The large T-group question and the small Aut(T) insertion have a visible hat. C’s bold rendering and H’s blackboard rendering are treated as the same handwritten notation.'),
 dict(form=r'\sim / a',meaning='Unresolved final label of each groupoid tuple',evidence='Both positions contain a low wave. Its mathematical role was not used to replace it with a definite letter.'),
 dict(form='bare shaft / right-headed shaft',meaning='Distinct visible connector forms',evidence='Upper links: bare, headed, bare, headed. Lower links: bare, bare, headed, bare. Projection, pair map, equivalence, and Phi-map heads were also inspected.')
],
abbreviations=[
 dict(form='ens',expansion='ensemble; left without an added period'),
 dict(form='op.',expansion='opération(s), according to context'),
 dict(form='Aut',expansion='automorphismes'),
 dict(form='Ob',expansion='objets'),
 dict(form='gr',expansion='groupes, in Hom_gr'),
 dict(form='canon.',expansion='canonique / canoniquement; punctuation and attachment remain uncertain')
],
hand_log=[
 dict(habit='Compressed avec begins with a tiny oval or dot, then a short low stroke and a final ripple.',places='Pair definition; compatible avec g; avec opération; avec notations; compatible avec op.',scope='All five occurrences on this page inspected; the first and second directly compared in one crop.',misreadings='C gave où at the pair-definition occurrence; the immediately lower repeated form supports H’s avec.'),
 dict(habit='The rounded extension glyph can look like a cursive E, epsilon-like form, or Sigma.',places='Nine group-label occurrences on scan019.',scope='All nine inspected; shared alphabet uncertainty retained.',misreadings='C chooses mathcal E; H chooses Sigma; neither is silently promoted to certainty.'),
 dict(habit='The object-set letter has a 3-like top and long curling tail.',places='Beta output, Ob definition, action on Z, lower recap.',scope='All four occurrences inspected.',misreadings='C’s ordinary Z and H’s mathfrak Z refer to the same graph; medium-confidence encoding only.'),
 dict(habit='Round T/tau graph varies between a looped and an unlooped top crossing.',places='Triple, où clause, Phi domain.',scope='All three occurrences inspected.',misreadings='C gives tau and H calligraphic T; the report retains both alphabet readings.'),
 dict(habit='A very small chi has a crossed upper stem and long descending hook.',places='Inserted tuple component; separate interlinear chi-colon; inserted full map.',scope='All three local chi graphs compared.',misreadings='H omits the tuple insertion and comments on an unreadable small sign; C omits the separate chi-colon.'),
 dict(habit='Crowded inserted hats can cross an adjacent prose stroke.',places='Hat on Z-star below the start of un in T un groupe.',scope='This occurrence only; no general deletion rule inferred.',misreadings='H inserts a struck illegible segment after T, but the crossing belongs to the lower mathematical insertion.'),
 dict(habit='Black pen stops and short retraces do not alone establish an arrowhead.',places='Upper and lower extension diagrams.',scope='All eight links inspected in native half and relevant crops.',misreadings='H supplies heads to all links; C’s mixture of bare shafts and heads is retained.')
],
notes=[
 dict(id='143_scan019-N1',text='The upper block gives the source’s definition of beta: a group of compatible pairs (g, bar g), pi = Aut(tilde Pi/Pi), a projection to G and an object set Ob tilde Pi with an evident action. The arrow/shaft diagram is transcribed as ink, without a proof of exactness. The separate phrase Variantes profinies… follows.'),
 dict(id='143_scan019-N2',text='Circled paragraph 8 recalls an extension and a nonempty set on which pi acts freely, then places a double-headed correspondence next to the groupoid tuple. It proposes interpreting data called a triple. The small inserted chi makes the written tuple contain four entries; the word triple is retained without correction.'),
 dict(id='143_scan019-N3',text='The source asks whether T is isomorphic to the hatted integer group, with an explicit question mark. It adds chi : G to Aut(T), and a crowded comparison involving hatted Z-star and canon.?. The latter remains wholly marked unsure because its intermediate curved stroke and punctuation cannot be fixed. No canonical identification is asserted by this review.'),
 dict(id='143_scan019-N4',text='A separate chi-colon is visibly interlinear above où. It is retained at that position independently of the complete chi map below; the source provides no caret settling its intended grammatical attachment. Phi maps the round-labelled set to Hom_gr(T, pi). The last line ends mid-parenthesis at opérant; no completion is supplied.'),
 dict(id='143_scan019-N5',text='The two final tuple components are low waves. Their role does not establish whether the intended symbol is sim or a compressed a, so both alternatives remain. The round set label likewise remains tau/calligraphic T. The current E/Sigma convention is applied consistently. Alphabet-only choices are medium confidence and non-consequential.'),
 dict(id='143_scan019-N6',text='The bottom-left 18 is in pencil and is assigned to an unnamed hand. H’s long editorial notation note is not source text. Small detached pen taps and paper marks without a legible textual form are not promoted to superscripts, punctuation, or cancelled words.')
],
check_events=[
 dict(statement_id='143_scan019-beta-definition',type='carried as background without fault found',outcome='Visual transcription of the stated construction only. No group-law, kernel, surjectivity, or exactness proof was performed; the diagram’s mathematical role did not add missing arrowheads.'),
 dict(statement_id='143_scan019-paragraph8-correspondence',type='carried as background without fault found',outcome='The displayed correspondence and free-action assertion were read as source statements. No equivalence was proved, and its expected inputs were not used to replace the written wave-shaped parameter.'),
 dict(statement_id='143_scan019-character-and-Phi-data',type='carried as background without fault found',outcome='No proof or computation identifying T with hatted Z or Aut(T) with hatted Z-star was attempted. The question marks and uncertain canon. parenthesis remain source questions.')
],
unresolved_for_main=[
 'Two wave-shaped tuple components: crops/143_scan019_readerC_beta-formula.png and crops/143_scan019_readerC_lower-tuple.png.',
 'Round T/tau label and exact placement of isolated chi-colon: crops/143_scan019_readerC_triple-insertions.png; third label occurrence in chi-parenthesis-map crop.',
 'Cancelled du/de before section 7: crops/143_scan019_readerC_section-deletion.png.',
 'M0698: tall curved stroke after Z-star and canon.? parenthesis grouping: crops/143_scan019_readerC_group-question.png, with the left side of the complete map in chi-parenthesis-map crop.',
 'Rounded E/Sigma identification remains the shared notation-table uncertainty; nine occurrences retained.'
],
raw_difference_disposition='All '+str(len(packet['differences']))+' packet difference entries were inspected against the original once, each native half, and one crop for each unresolved locus. All page text, signs, indices, underlining, insertions, cancellation, diagrams and footer were checked, including C/H agreements. Markup-only scan labels, tikzcd scaffolding, math spacing, Ob thinspace parsed as a comma, mapsto extraction artifacts, semicolon math-spacing artifacts, and ellipsis encoding differences are excluded. H’s editorial note is excluded as editorial text. Plain versus calligraphic G and bold versus blackboard Z are rendering choices; reported alphabet-only Z and T/tau choices carry medium confidence and consequential false. The only original packet MARK is M0698; new doubts are confined to remaining_doubts. The pi-identity crop confirms the tilde and slash without generating a change row. The first half2 display attempt did not return a viewable image because output was truncated; the subsequent successful display was the actual half2 inspection.'
)
assert [d['id'] for d in report['decisions']] == [m['id'] for m in packet['marks']]
assert tex.count(r'\unsure{\mathcal E|\Sigma}') == 9
assert tex.count(r'\unsure{\tau|\mathcal T}') == 3
assert tex.count(r'\unsure{\sim|a}') == 2
assert len({x['element'] for x in inventory}) == len(inventory)
for item in changes:
    if item['crop'] != 'page': assert (root/item['crop']).exists()
(root/'reviews'/'143_scan019_readerC.tex').write_text(tex)
(root/'reviews'/'143_scan019_readerC.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'changes':len(changes),'decisions':len(report['decisions']),'inventory':len(inventory),'remaining_doubts':len(report['remaining_doubts']),'raw_differences':len(packet['differences']),'literal_excerpt_validation':'passed','tex':'reviews/143_scan019_readerC.tex','json':'reviews/143_scan019_readerC.json'}))
