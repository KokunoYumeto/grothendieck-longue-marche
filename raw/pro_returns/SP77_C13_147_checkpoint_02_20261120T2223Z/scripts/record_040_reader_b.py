from pathlib import Path
import json,csv
base=Path('/workspace/scratch/88012a0a2bcc/SP77_C13_147_work')
C=Path('/workspace/scratch/88012a0a2bcc/inputs/SP77_C13_147_texts/pages/147_scan040.tex').read_text()
H=Path('/workspace/scratch/88012a0a2bcc/inputs/SP77_C13_147_texts/hua/hua_147_scan040.tex').read_text()
specs=json.loads((base/'records/147_scan040_crop_specs.json').read_text())
sp={n:box for n,box,rot in specs}
rot={n:rotation for n,box,rotation in specs}
def cp(n):return f'crops/147_scan040_{n}.jpg'
new_fragment=r'\margin{\unsure{\deleted{$\operatorname{card}I_\beta$}}}'
draft=C.replace(r'\unsure{\widetilde B\'_\alpha}',r'\widetilde B\'_\alpha') if False else C
for old,new in [
 (r"\unsure{\widetilde B'_\alpha}",r"\widetilde B'_\alpha"),
 (r'\unsure{tous}','tous'),
 (r'\unsure{car la condition est aut. assur.}',r'car la condition est \unsure{aut. assur.}'),
 (r"\unsure{g'_\beta|\gamma'_\beta}",r"g'_\beta"),
 (r"$g':S'",r"$\unsure{g'|f'}:S'")
]:
 assert old in draft,old
 draft=draft.replace(old,new,1)
needle=r'\deleted{\unsure{qui a priori}'
assert needle in draft
draft=draft.replace(needle,new_fragment+'\n\n'+needle,1)
(base/'drafts/147_scan040.tex').write_text(draft)

def between(s,a,b):return s.split(a,1)[1].split(b,1)[0]
def inclusive(s,a,b):return a+between(s,a,b)+b
main_diagram=inclusive(C,r'b) \diagram{',r'\end{tikzcd}} commutatif')
h_main=inclusive(H,r"b) $I'",r'\end{tikzcd}')
margin_diagram=inclusive(C,r'\margin{donc ',r'\end{tikzcd}} est comm.}')
h_margin=inclusive(H,r'\marginal{donc ',r'commutent.}')
nb=inclusive(C,r'\margin{\uline{NB} ',r'\widetilde A_\alpha$}')
h_nb=inclusive(H,r'\marginal{\emph{NB} ',r'\tilde{A}_\alpha$}')
main_formula=between(C,r'\node[anchor=west] (eq) at (0,0) {$',r'$};')
h_formula=between(H,r'\[',r'\]').strip()
right_margin=inclusive(C,r'\margin{\unsure{car la condition est aut. assur.}',r'\end{tikzpicture}}}')
final_right=right_margin.replace(r'\unsure{car la condition est aut. assur.}',r'car la condition est \unsure{aut. assur.}')
struck=inclusive(C,r'\deleted{\unsure{qui a priori}',r'\ldots}')
changes=[]
def ch(place,c,h,f,n,kind,cat,ev,dc=False,dh=True,conf='high',conseq=False):
 changes.append(dict(id=f'040-{len(changes)+1:02d}',place=place,C=c,H=h,final=f,diff_C=dc,diff_H=dh,kind=kind,evidence=ev,crop=cp(n),box=sp[n],confidence=conf,consequential=conseq,error_category=cat))
ch('a), target of S prime map',r"S^{\deleted{\unsure{'}}}","S''",r"S^{\deleted{\unsure{'}}}",'02_a','deletion state','Struck text','The target superscript is a dark retraced hooked mark, unlike the clean separate source prime. The erased prime is still only a candidate; neither one nor two original primes can be certified from the blot.',conf='medium',conseq=True)
ch('a), target of B tilde prime map',r"\widetilde A^{\deleted{\unsure{'}}}",r"\tilde{A}''",r"\widetilde A^{\deleted{\unsure{'}}}",'02_a','deletion state','Struck text','The raised mark after tilded A is an angular overwritten zigzag, not two separated live primes. C’s cancelled uncertain superscript is retained, with its original prime count unresolved.',conf='medium',conseq=True)
ch('b), square and commutatif',main_diagram,h_main,main_diagram,'03_b','text not on the page','Text that is not on the page','There is one four-object square, with I prime and I above S prime and S, two down arrows, two rightward edges and a tilde over the top edge. Commutatif is written once to the right. H repeats the four relations as a prefatory formula list which has no separate written counterpart.')
ch('upper-left marginal square',margin_diagram,h_margin,margin_diagram,'04_margindiagram','drawing or diagram','Drawings and diagrams','The rotated crop shows a four-corner square: B-tilde prime amalg I prime, A-tilde amalg I, S prime and S; the top edge is marked tilde. Donc precedes it and the separate lower wording is est comm., including the abbreviation point. H flattens this into two chains and changes the wording to commutent.')
ch('c), cancelled sign before s prime in S prime',r'\deleted{\unsure{$S$}}',r'\struck{\ill{}}',r'\deleted{\unsure{$S$}}','05_cancelS',r'readable ink left as \ill{}','Readable ink left as illegible','A large upper curve and lower curved turn remain under the dense cross-hatching, supporting a tentative S. The crossed sign cannot be certified, so the C candidate remains doubtful.',conf='low')
ch('c), first au dessus before alpha','au dessus','au-dessus','au dessus','25_audessus_1','abbreviation expanded or spelling modernised','Abbreviations expanded, spelling modernised','The short au strokes are followed by a clear gap and then the looped d of dessus. No intervening hyphen is written.')
ch('c), second au dessus before id alpha','au dessus','au-dessus','au dessus','26_audessus_2','abbreviation expanded or spelling modernised','Abbreviations expanded, spelling modernised','The second occurrence also has a gap after au and no connecting hyphen before dessus.')
ch('c), comma following the square bracket before muni de',',','[absent]',',','08_deletedmuni','omission','Omisisons' if False else 'Omissions','A separate descending comma is visible just before the following muni de continuation; H omits this punctuation.')
old_muni=r'\deleted{\unsure{$\widetilde A$}\unsure{ et }\unsure{$A$}}'
ch('c), struck cluster after muni de',old_muni,r'\struck{\ill{}}',old_muni,'08_deletedmuni',r'readable ink left as \ill{}','Readable ink left as illegible','The cluster is cancelled by heavy oblique strokes. A tilded angular capital and another final A-like capital survive, with compressed intervening and preceding strokes. The complete C parsing A-tilde et A is not certified; all its doubt wrappers remain.',conf='low')
old_amap=r"I'_\alpha\inserted{\amalg\unsure{\widetilde B'_\alpha}}\longrightarrow S'_\alpha"
new_amap=r"I'_\alpha\inserted{\amalg\widetilde B'_\alpha}\longrightarrow S'_\alpha"
ch('c), marked-point map over alpha',old_amap,r"\add{$\tilde{B}' \sqcup$} $I'_\alpha \hookrightarrow S'_\alpha",new_amap,'09_alphaMap','insertion or placement','Insertions put in the wrong place','The insertion leader runs from amalg B-tilde prime alpha into the gap after I prime alpha. B has two lobes, a separate tilde and prime, and a low alpha. The leader’s curved lower end is separate from the straight arrow shaft; it is not an inclusion hook. H moves the summand before I, omits its alpha, and gives a hooked map.',conseq=True)
ch('c), label of the map from S prime alpha to N',r'\gamma_\alpha',r'g_\alpha',r'\gamma_\alpha','11_gamma','misread symbol or index','Symbols and indices','The label has two upper arms meeting above a narrow closed lower loop. This is the gamma form on the page, visibly different from the round-headed g in the nearby g prime beta clauses.',conseq=True)
old_type=r'\deleted{\unsure{de type|de genre} $\unsure{g=g(\alpha)|(g_\alpha,\nu_\alpha)}$\unsure{, i.e.}}'
ch('c), cancelled designation after the inserted G prime alpha',old_type,'[absent]',old_type,'13_typecorrection','omission','Omissions','A long crossed passage remains after the inserted underlined G prime alpha. The tall descenders and g-like loops support the recorded alternatives, but the cross-strokes conceal whole letter segments. H’s live transcription omits this cancelled passage; the uncertain C reconstruction is preserved.',conf='low',conseq=True)
old_nb=r'\deleted{[NB il \unsure{satisfait automatiquement}}'
ch('c), crossed NB clause after connexe',old_nb,'[absent]',old_nb,'14_connexe','omission','Omissions','The opening square bracket, NB and il are visible under the two long strike strokes. The following word has the tall stems of satisfait and a long automatically-like continuation, but not every letter is recoverable. H only mentions this passage in an editorial note.',conf='medium')
ch('c), inserted replacement below the crossed NB',r'\inserted{et [il satisfait \unsure{tous}}',r'et [il satisfait \ill{}]',r'\inserted{et [il satisfait tous}','14_connexe',r'readable ink left as \ill{}','Readable ink left as illegible','The lower live line reads et [il satisfait tous. The final word has the crossed initial t, low ou strokes and terminal s; there is no final te. A closing square bracket after tous is not present. The masculine tous is retained rather than changed to agree with conditions.')
ch('c), cancelled les after tous',r'\deleted{\unsure{les}}','[absent]',r'\deleted{\unsure{les}}','14_connexe','omission','Omissions','A short looped word is scribbled over immediately after tous. It is compatible with les but cannot be fully separated from the scribble. H does not preserve this cancelled word.',conf='medium')
ch('c), replacement article and following noun',r'\inserted{les} conditions','à la condition',r'\inserted{les} conditions','15_conditions','misread word','Words','The new small les is written at the left of the continuing line, followed by conditions. There is no separate à la. The source’s replacement and plural noun are retained; the correction leader above belongs to this rewritten passage.')
ch('c), adjective after rigidité','relatives','relative','relatives','15_conditions','misread word','Words','The adjective ends in an additional short terminal turn after the e-like stroke before the gap to aux. The plural relatives is retained.')
ch('c), cancelled alpha before g prime beta',r', \deleted{\unsure{$\alpha$}}','[absent]',r', \deleted{\unsure{$\alpha$}}','16_beta','omission','Omissions','Between tels que and g prime beta is a short punctuation-like turn followed by a heavily scribbled small symbol. Its exposed loop and right arm support the tentative alpha; the cancelled symbol is not absent.',conf='medium')
ch('left NB, arrow above a prime',r"\vec a'",r"a'",r"\vec a'",'17_NB','misread symbol or index','Symbols and indices','A separate short rightward arrow is written over the a prime in the membership clause. Its horizontal shaft and right point are visible after rotating the margin.',conseq=True)
ch('left NB, membership set for a prime',r"\widetilde B'_\alpha",r"\tilde{B}'",r"\widetilde B'_\alpha",'17_NB','misread symbol or index','Symbols and indices','The B after the membership sign has a separate prime and an alpha below and to the right. The alpha is inked here even though it repeats the index of the set being described.',conseq=True)
ch('left NB, phrase between S prime alpha and donc',r"i.e. dans $G'(\alpha)$",r'\ill{}',r"i.e. dans $G'(\alpha)$",'17_NB',r'readable ink left as \ill{}','Readable ink left as illegible','After S prime alpha, the small i.e. dots and the low dans strokes lead to a clear G prime with parenthesized alpha. This phrase is readable in the rotated margin.')
ch('main rigidity inequality and its altered terms',main_formula,h_formula,main_formula,'18_maincondition','omission','Omissions','The full inequality visibly includes an inserted + card B-tilde prime beta and its closing parenthesis, followed by another + card term. In that last term a C-shaped outer stroke replaces B, the former alpha index is crossed, and beta survives; the inequality ends at 3. The underbrace beneath card I prime beta has a scribbled candidate poids. H’s displayed inequality lacks the entire last cardinality term and does not preserve these ink states.',conf='medium',conseq=True)
ch('slanting crossed words left of the main inequality',r'\deleted{\unsure{pour chaque}}','[absent]',r'\deleted{\unsure{pour chaque}}','18_maincondition','omission','Omissions','Small slanting letters beneath a long diagonal strike are compatible with pour chaque. The strike obscures several letters, so the candidate stays tentative.',conf='low')
ch('annotation pointed to by the final cardinality term',r"ordre de\\$\beta$ dans $\underline G'(\alpha)$",'[absent]',r"ordre de\\$\beta$ dans $\underline G'(\alpha)$",'18_maincondition','omission','Omissions','A curved arrow from the altered last cardinality term points to two live lines reading ordre de / beta dans underlined G prime alpha. H describes this in an editorial note rather than transcribing the annotation.')
ch('lower-left weight annotation',r"poids marqué en $\beta$\\dans la maquette\\$\underline G'(\alpha)$",r"poids marqué en $\beta$ \ill{} dans le \ill{} graphe $\underline{G}'(\alpha)$",r"poids marqué en $\beta$\\dans la maquette\\$\underline G'(\alpha)$",'19_leftweight','misread word','Words','The three sloping lines read poids marqué en beta / dans la maquette / underlined G prime alpha. The q descender and double tall t strokes in maquette are clear. There is no extra word graphe and the article is la.')
ch('right marginal condition note, cancellations and bracketed formula',right_margin,'[absent]',final_right,'20_rightmargin','omission','Omissions','The margin contains a live car la condition est line with uncertain abbreviated ending, two cancelled lines, an equiv-like continuation, and the sum 2g prime beta + card I prime beta + card B-tilde prime beta. A lower bracket points to poids ≥ 3. H’s editorial synopsis gives only portions of this writing and does not transcribe the full note or its cancellation states.',conf='medium',conseq=True)
ch('fragment below and left of the right marginal bracket','[absent]','[absent]',r'\unsure{\deleted{$\operatorname{card}I_\beta$}}','20_rightmargin','omission','Omissions','Below the marginal formula, the strokes card followed by a serifed I and lowered beta are visible at the left end of the bracket/strike network. C does not encode this separate fragment. Its exact prime status, cancellation state and attachment to the neighbouring struck block cannot be certified, so the entire proposed deleted fragment is inside an uncertainty wrapper.',dc=True,conf='low',conseq=True)
ch('large cancelled block below the inequality',struck,'[absent]',struck,'21_struckblock','omission','Omissions','The lower crossed block contains the two explicit inequalities with coefficients 2 and bounds 3, the I prime beta and A-tilde prime beta terms, and the sentence ending une condition plus faible (puisque underlined G prime est un MD-graphe)… . The preceding qui a priori and + car fragments remain uncertain. Long horizontal and oblique strokes cancel the block. H describes selected portions in a note but leaves the block out of its transcription.',conf='medium',conseq=True)
ch('d), initial article','le','Le','le','22_d','misread word','Words','The article is a cursive l joined to a small e, in the same running hand as the sentence. C’s lowercase le is retained; the handwritten l does not supply a separate display-capital form.',conf='medium')
ch('lower-left footer',r'\mspage{39}','[absent]',r'\mspage{39}','24_footer','omission','Omissions','The faint footer has the two open lobes of 3 and the upper oval with descending tail of 9. This written 39 is separate from the darker heading 19.')

def dec(id,choice,reading,n,evidence,conf='medium'):
 return {'id':id,'cote':'147','scan':'40','decision':choice,'reading':reading,'what the ink shows':evidence,'crop':cp(n)+' ('+','.join(map(str,sp[n]))+')'+(f'; rotation {rot[n]} degrees' if rot[n] else ''),'confidence':conf}
decisions=[
 dec('M0982','first',r"\widetilde B'_\alpha",'09_alphaMap','The inserted capital has the two B lobes, a separate tilde and prime, and a recognizable low alpha. The insertion leader attaches after I prime alpha.','high'),
 dec('M0983','undecided',r'\unsure{\to|{-}}','10_globalMap','The horizontal stroke ends in a short downward nub. It may be a highly abbreviated one-sided arrowhead, but a clear two-sided point is absent. Whole map, including the inserted B-tilde prime amalg, inspected.'),
 dec('M0984','undecided',r'\unsure{\to|{-}}','12_gprime','The relation has a short terminal downward corner but no full chevron. The whole map and its label have been read; the label now separately records a g/f doubt.'),
 dec('M0985','first','tous','14_connexe','The new line’s last live word shows initial t, joined low ou and terminal s, followed by the separately scribbled les. No terminal te is written.','high'),
 dec('M0986','other',r'car la condition est \unsure{aut. assur.}','20_rightmargin','The first four words are readable. The two very compressed abbreviated groups at the right remain uncertain; only the scope of the doubt is narrowed.'),
 dec('M0987','undecided',r'\unsure{équiv à}','20_rightmargin','An accented e and descending q are followed by compressed low strokes before the colon. The exact abbreviation and final à are not fully separable.'),
 dec('M0988','first',r"g'_\beta",'23_sum','The summand has a closed, retraced round head and a long descending stem with left hook, plus a separate prime and beta. It contrasts with the forked gamma and lower loop in the restricted-map label.','high')]

supp_specs=[
 ('02_a',r"\deleted{\unsure{'}}",'a), cancelled superscript of S','Dark retracing hides the original short superscript; prime count remains unrecovered.'),
 ('02_a',r"\deleted{\unsure{'}}",'a), cancelled superscript of A tilde','The angular dark blot is crossed/overworked; a prime is plausible but not independently recoverable.'),
 ('05_cancelS',r'\deleted{\unsure{$S$}}','c), sign before s prime','A possible S-shaped upper/lower curve survives under dense hatching.'),
 ('08_deletedmuni',r'\unsure{$\widetilde A$}','c), first candidate in the struck cluster after muni de','The angular tilded capital is partly visible, but dense preceding/crossing strokes prevent complete identification.'),
 ('08_deletedmuni',r'\unsure{ et }','c), middle of the struck cluster after muni de','The compressed connective is crossed and cannot be read letter by letter.'),
 ('08_deletedmuni',r'\unsure{$A$}','c), end of the struck cluster after muni de','An A-like final capital survives, but the cancelled group is not fully recoverable.'),
 ('13_typecorrection',r'\unsure{de type|de genre}','c), cancelled designation after MD-graphe','Long descenders favour type, but crossing strokes hide enough letters that genre cannot be excluded.'),
 ('13_typecorrection',r'\unsure{g=g(\alpha)|(g_\alpha,\nu_\alpha)}','c), cancelled type/genus formula','Several g-like loops and parentheses survive, but the superseding zigzag obscures the full sequence.'),
 ('13_typecorrection',r'\unsure{, i.e.}','c), end of cancelled designation','Small dotted/short strokes are compatible with i.e.; the crossing prevents certification of punctuation and letters.'),
 ('14_connexe',r'\unsure{satisfait automatiquement}','c), cancelled NB line','Tall word stems and the long continuation support the candidate, but several bodies are crossed through.'),
 ('14_connexe',r'\deleted{\unsure{les}}','c), scribbled les after tous','A short looped word is heavily overwritten; les remains tentative.'),
 ('16_beta',r'\deleted{\unsure{$\alpha$}}','c), cancelled symbol before g prime beta','A loop with an exposed right arm suggests alpha, but the scribble is dense.'),
 ('18_maincondition',r'\deleted{\unsure{poids}}','main inequality, underbrace label','The compact crossed label may read poids; its middle letters cannot be separated from the hatching.'),
 ('18_maincondition',r'\deleted{\unsure{pour chaque}}','main inequality, slanting struck words at left','The diagonal strike obscures the short letter sequence; the candidate is not promoted.'),
 ('20_rightmargin',r'\unsure{a priori}','right margin, first cancelled line','The long strike overlays the word bodies; only portions of a priori remain distinct.'),
 ('20_rightmargin',r"\unsure{2g'_\beta}",'right margin, numerical expression in the cancelled line','A 2 and long descending letter with low beta are plausible, but superposed letters and strikes prevent full certification.'),
 ('20_rightmargin',r'\unsure{est}','right margin, end of first cancelled line','Short crossed strokes at the end could be est; not all letters are recoverable.'),
 ('20_rightmargin',r"\unsure{puisqu'il est}",'right margin, second cancelled line','A descending initial p and later tall strokes survive beneath a long line; the full words remain tentative.'),
 ('21_struckblock',r'\unsure{qui a priori}','large cancelled block, initial upper line','The first crossed line is overlapped by annotation leaders. Its surviving descenders support the candidate without making all letters readable.'),
 ('21_struckblock',r'\unsure{$+\operatorname{car}$}','large cancelled block, short mathematical fragment','The plus and car-like letters are visible; a final d is not independently recoverable. The truncated candidate remains uncertain.')]
supp=[]
for i,(n,read,place,ev) in enumerate(supp_specs,1):
 item=dec(f'U040-{i:02d}','undecided',read,n,ev,'low' if n in ['08_deletedmuni','13_typecorrection'] else 'medium')
 item['place']=place
 supp.append(item)

# Exact target readings for blind boxes; adjacent contextual scraps at a crop edge
# are not promoted into the target transcription.
boxes=[]
def bx(n,kind,reading,coords=None):
 q=coords or sp[n]
 item=dict(box=f'040-B{len(boxes)+1:02d}',kind=kind,x0=q[0],y0=q[1],x1=q[2],y1=q[3],reading=reading)
 if rot[n]:item['suggested_rotation']=rot[n]
 boxes.append(item)
bx('01_header','handwritten page heading',r'\mspage{19}')
bx('02_a','two full formulas with cancelled superscripts',r"$S'\longrightarrow S^{\deleted{\unsure{'}}}$ surjectif, $\widetilde B'\longrightarrow\widetilde A^{\deleted{\unsure{'}}}$ \uline{bijectif}")
bx('03_b','complete diagram; disputed extra witness wording',main_diagram.removeprefix('b) '))
bx('04_margindiagram','marginal diagram and words',margin_diagram)
bx('05_cancelS','struck sign and adjacent full membership formula',r"\deleted{\unsure{$S$}} $s'\in S'$")
bx('06_arcs','struck word with replacement',r"\deleted{flèches} arcs $a'\in\widetilde A'$")
bx('07_insertC','inserted equality and surrounding formula',r"$\inserted{\widetilde C'=}\widetilde A'\setminus\widetilde B'$ (i.e.")
bx('08_deletedmuni','struck formula/word cluster; comma',', '+old_muni)
bx('09_alphaMap','full formula with uncertain C insertion now read',f'${new_amap}$')
bx('10_globalMap','full doubtful map with insertion',r"$\inserted{\widetilde B'\amalg}I'\unsure{\to|{-}}S'$")
bx('11_gamma','disputed letter in complete map',r'$\gamma_\alpha:S\prime_\alpha\longrightarrow\mathbb N$'.replace(r'S\prime',"S'"))
bx('12_gprime','full formula with arrow and new label doubts',r"$\unsure{g'|f'}:S'\unsure{\to|{-}}\mathbb N$")
bx('13_typecorrection','inserted graph label and entire cancelled doubtful formula',r"\inserted{$\underline G'(\alpha)$} "+old_type)
bx('14_connexe','struck clause and replacement insertion',old_nb+r' \inserted{et [il satisfait tous}\deleted{\unsure{les}}')
bx('15_conditions','inserted article; disputed noun and adjective',r'\inserted{les} conditions de rigidité relatives aux sommets')
bx('16_beta','struck symbol; full numerical set condition',r"$\beta$ tels que, \deleted{\unsure{$\alpha$}} $g'_\beta\in\{0,1\}$, à savoir que")
bx('17_NB','complete marginal note; vector and index differences',nb)
bx('18_maincondition','whole inequality; handwritten 2 and 3; altered/inserted terms; struck words and annotations',r'\deleted{\unsure{pour chaque}}'+'\n$'+main_formula+'$\n'+r"ordre de $\beta$ dans $\underline G'(\alpha)$")
bx('19_leftweight','marginal weight annotation',r"poids marqué en $\beta$ dans la maquette $\underline G'(\alpha)$")
bx('20_rightmargin','whole marginal note; cancellations; handwritten coefficients 2 and bound 3',final_right)
bx('21_struckblock','full cancelled block with both numerical inequalities',struck)
bx('22_d','word case difference','d) le',[450,1842,630,1940])
bx('23_sum','full doubtful sum now read; handwritten subscript 1',r"$\sum_{\beta\in S'_\alpha}g'_\beta+h_1(G(\alpha))=g_\alpha.$")
bx('24_footer','handwritten footer number',r'\mspage{39}')
bx('25_audessus_1','orthographic witness difference',r'au dessus de $\alpha$')
bx('26_audessus_2','orthographic witness difference',r'au dessus de $\operatorname{id}_\alpha$)')
bx('20_rightmargin','new uncertain mathematical fragment; cancellation and attachment uncertain',r'\unsure{\deleted{$\operatorname{card}I_\beta$}}',[1150,1615,1415,1725])

inventory=[]
def inv(kind,pos,words):
 inventory.append(dict(scan=40,sheet_kind='text',hand='his hand',element=f'040-E{len(inventory)+1:02d}',kind=kind,position=pos,first_words_or_objects=words,transcribed='yes'))
for kind,pos,words in [
 ('text','top centre','19'),('text','top main line, a)','two maps, surjectif and underlined bijectif'),
 ('deletion','a), two target superscripts','uncertain original prime marks'),('diagram','upper centre, b)','I prime/I over S prime/S, commutatif'),
 ('margin note','upper-left sloping square','donc ... est comm.'),('text','main c) paragraph','forall alpha in S, le sous-graphe G prime alpha ...'),
 ('deletion','c), after formé des','uncertain capital S'),('deletion','c), before arcs','flèches'),
 ('insertion','c), above A-tilde prime set difference','C-tilde prime ='),('deletion','c), after muni de','uncertain A-tilde et A cluster'),
 ('insertion','c), above I prime alpha map','amalg B-tilde prime alpha'),('insertion','c), above I prime map','B-tilde prime amalg'),
 ('insertion','c), above cancelled designation','underlined G prime alpha'),('deletion','c), after MD-graphe','uncertain de type/de genre and type/genus expression'),
 ('deletion','c), after connexe','NB il satisfait automatiquement candidate'),('insertion','c), replacement below crossed NB','et [il satisfait tous'),
 ('deletion','c), after tous','uncertain les'),('insertion','c), beginning next line','les'),('deletion','c), before g prime beta','uncertain alpha'),
 ('margin note','left middle, sloping NB','definition of B-tilde prime alpha and map to A-tilde alpha'),
 ('display','main lower inequality','2g prime beta + marked cardinalities + altered last cardinality ≥ 3'),
 ('insertion','above main inequality','+ card B-tilde prime beta and closing parenthesis'),('deletion','underbrace of card I prime beta','uncertain poids'),
 ('deletion','last cardinality term','B superseded by C; uncertain alpha index crossed'),('insertion','last cardinality term','C'),
 ('deletion','sloping words left of inequality','uncertain pour chaque'),('margin note','below/right of last cardinality term','ordre de beta dans underlined G prime alpha'),
 ('margin note','lower-left slope','poids marqué en beta dans la maquette underlined G prime alpha'),
 ('margin note','right lower margin','car la condition est ... equiv-like continuation, bracketed weight sum and poids ≥ 3'),
 ('deletion','inside right note','candidate a priori 2g prime beta est; candidate puisqu’il est'),
 ('deletion','below/left of right bracket; state itself uncertain','new tentative card I beta fragment'),
 ('deletion','large block across the page under the main inequality','candidate qui a priori and + car; two inequalities; condition plus faible sentence'),
 ('text','bottom d) paragraph','le genre du MD-graphe underlined G alpha ...'),('display','bottom formula','sum of g prime beta plus h subscript 1 of G alpha equals g alpha'),('text','bottom-left footer','39')]:inv(kind,pos,words)

doubts=[]
for x in supp:
 doubts.append(dict(place=x['place'],reading=x['reading'],alternatives='Candidate retained; cancelled letters not fully recoverable.',confidence=x['confidence'],reason=x['what the ink shows']))
for x in decisions:
 if x['decision'] in ('undecided','other'):
  doubts.append(dict(place=x['id'],reading=x['reading'],alternatives='Recorded alternatives or abbreviated ending remain open.',confidence=x['confidence'],reason=x['what the ink shows']))
doubts.extend([
 {'place':'c), isolated label of the map S prime to N','reading':r"\unsure{g'|f'}",'alternatives':"g' | f'",'confidence':'medium','reason':'The isolated label has a tiny flattened upper loop, long hooked descender, and conspicuous transverse stroke, making f-like and g-like readings possible. The context and other genus labels favour g prime, but the shape is not made certain by that context. This newly added doubt changes certainty only.'},
 {'place':'below/left of the right marginal bracket','reading':r'\unsure{\deleted{$\operatorname{card}I_\beta$}}','alternatives':'card I beta or card I prime beta; cancellation and attachment to the struck block are uncertain','confidence':'low','reason':'A card I beta-like fragment is visibly present, but overlapping bracket and strike strokes prevent secure determination of its exact state or affiliation. The outer uncertainty wrapper applies to the proposed deletion as well as the letters.'}
])

record=dict(scan=40,reader='reader_b',line_count=47,changes=changes,decisions=decisions,supplemental_unindexed_C_doubts=supp,inventory=inventory,boxes=boxes,doubts=doubts,
 notation=[
 {'form':r'\gamma_\alpha','meaning':'Restricted genus-map label from S prime alpha to N.','evidence':'c), complete map in crop 11_gamma.','scope':'One clear forked-gamma occurrence here, distinguished locally from the round-headed g labels.'},
 {'form':r"I'_\alpha\amalg\widetilde B'_\alpha\longrightarrow S'_\alpha",'meaning':'Marked-point map supplied to the subgraph.','evidence':'c), inserted B-tilde prime alpha follows I prime alpha.','scope':'Actual summand order, alpha index and ordinary arrow retained; insertion leader is not a map hook.'},
 {'form':r"\widetilde B'_\alpha",'meaning':'Indexed set named in the left NB.','evidence':'Both the defined set and the membership set a prime belongs to carry alpha.','scope':'The repeated alpha is retained as written, without replacing the membership set by unindexed B prime.'},
 {'form':r"\underline G'(\alpha),\underline G(\alpha),G(\alpha)",'meaning':'The primed graph label occurs in c) and annotations; the final genus clause and h subscript 1 argument use unprimed G.','evidence':'Inserted c) label and weight/degree annotations contrasted with d) and final sum.','scope':'No prime is added to either unprimed occurrence in d).'},
 {'form':r"g'_\beta",'meaning':'Genus summand in the final sum.','evidence':'Whole final formula, crop 23_sum.','scope':'Round retraced head and long hooked descender support g, not gamma, in this summand; the isolated g prime map label remains separately doubtful.'}
 ],
 abbreviations=[{'form':'comm.','expansion':'commutatif'},{'form':'NB','expansion':'nota bene'},{'form':'ens','expansion':'ensemble'},{'form':'i.e.','expansion':'id est'},{'form':r'\unsure{aut.}','expansion':'automatiquement, probable only'},{'form':r'\unsure{assur.}','expansion':'assurée, probable only'},{'form':r'\unsure{équiv}','expansion':'équivalent(e), abbreviated candidate'},{'form':'card','expansion':'cardinal'}],
 hand_log=[
 {'habit':'The gamma label has forked upper arms and a loop below their junction; g has a round upper head and long lower stem.','pages':'040','scope':'One clear gamma map label and the final g prime beta summand; the isolated g prime/f prime label remains unresolved.','misread_places':'H g alpha for gamma alpha; C final g/gamma choice resolved locally.'},
 {'habit':'A curved insertion leader can be mistaken for the hook of an inclusion map.','pages':'040','scope':'The leader below inserted amalg B-tilde prime alpha ends separately from the ordinary arrow.','misread_places':'H hooked I prime alpha to S prime alpha and wrong summand order.'},
 {'habit':'Some horizontal relation strokes end only in a very short downward nub.','pages':'040','scope':'The two marked arrow/dash choices remain unresolved; the strong arrows in a) and the alpha map have clear heads.','misread_places':'M0983 and M0984; no uniform arrow rule imposed.'},
 {'habit':'Short cancelled superscripts are retraced into dark hooks or zigzags.','pages':'040','scope':'The two target superscripts in a); their underlying prime count is not certified.','misread_places':'H live double primes for these overworked targets.'},
 {'habit':'Compressed unhyphenated au dessus is written in two groups.','pages':'040','scope':'Both occurrences in the defining c) paragraph.','misread_places':'H adds a hyphen at each occurrence.'}
 ],
 notes=[
 {'id':'147-040-N01','text':'The page carries conditions a)–d) for the graph-morphism data: a surjection on vertices and a bijection on the indicated oriented-edge set; commuting squares; a fibre subgraph with its marked-point map and genus map; rigidity conditions; and a final genus-sum formula. The text is heavily revised. The last cardinality term of the main rigidity inequality is present and altered from B to C, with a cancelled alpha index; it must not be omitted as in H’s displayed formula. Two crossed lower inequalities, marginal weight/degree explanations and all cancellation candidates are preserved. The handwritten heading is 19 and the faint footer is 39.'},
 {'id':'147-040-N02','text':'The author writes tous before conditions, repeats the alpha index on the membership-set B prime alpha in the NB, and uses unprimed G(alpha) in both parts of d), although c) introduces G prime(alpha). These are retained as ink, without grammatical or mathematical repair. The page’s assertions were transcribed, not proved.'},
 {'id':'147-040-N03','text':'A previously unencoded card I beta-like fragment lies below and left of the right marginal bracket, overlapping the strike network of the lower block. It is offered only as an uncertain deleted fragment: letter/prime details, cancellation state and attachment remain open for main and blind review. The isolated map label g prime also has an f-like transverse stroke, so a g prime/f prime doubt was added. No certainty is inferred from agreement between C and H.'}
 ],
 check_events=[{'statement_id':'147-040-N01','date':'2026-11-20','who':'GPT-6 Astra Pro; inherited effort; SP77_C13_147 reader_b','type':'carried as background without fault found','outcome':'Reading only, no proof claim. The diagrams, labels, inequalities and author’s stated genus relation were transcribed from the page; no mathematical proof verification was performed.'}],
 coverage={'whole_viewed':True,'halves_viewed':['top','bottom'],'all_tokens_read':True,'all_deletions_insertions_checked':True,'differences_accounted':'Every packet difference was examined against both witnesses and ink. Scan metadata, H editorial notes, LaTeX/TikZ coordinates, spacing, tilde/widetilde, emph/underline, struck/deleted and sqcup/amalg conventions are not independent content rows. Actual extra prose in H, graph-prime states, placement, words, punctuation, abbreviations, missing marginal/cancelled matter and the omitted last cardinality term are logged. All 27 saved crops were visually inspected. The final raised-stroke check confirms that the apparent superscript over l’extrémité is the end of the sloping NB’s G prime(alpha), already included in that note; it is not a new insertion into the main word. The seven decisions follow MARKS order; twenty nested C doubts are separately recorded. All handwritten numeral occurrences, full doubtful formulas, insertions, cancellations, margins and word differences are included in blind boxes.','line_count_basis':'47 physical text/formula lines: 23 in the main column including heading, both rows of b), cancelled lower block, final sum and footer; 3 in the upper-left marginal square/wording; 4 in the left NB; 5 interlinear insertion levels; 4 for the slanting cancelled pour chaque, cancelled poids, and two-line degree annotation; 3 in the lower-left weight note; 5 in the right condition note. Formula indices do not count as extra lines.'},
 unresolved=['Two cancelled target superscripts in a): original prime count unresolved.','Struck S and struck A-tilde/et/A cluster remain uncertain.','Cancelled designation after MD-graphe and crossed NB/les/alpha remain tentative.','M0983 and M0984 arrow/dash choices remain undecided.','M0986 is only partly settled; aut. assur. remains uncertain; M0987 equiv-like ending remains uncertain.','New isolated g prime/f prime doubt in the map to N.','New card I beta-like fragment: letters, prime status, cancellation state and attachment remain uncertain.','All other doubtful cancelled fragments retain their uncertainty.','Main visual approval and independent blind second reading remain pending.'],
 crop_files=[cp(n) for n,box,rotation in specs])
(base/'records/147_scan040.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print('draft and record written')
print('changes',len(changes),'decisions',len(decisions),'supplemental',len(supp),'boxes',len(boxes),'crops',len(specs),'inventory',len(inventory),'lines',record['line_count'])
