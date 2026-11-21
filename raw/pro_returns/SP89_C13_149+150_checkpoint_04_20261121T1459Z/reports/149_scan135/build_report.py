from pathlib import Path
import json
out=Path('work/reports/149_scan135')
boxes=json.loads((out/'crop_boxes.json').read_text())
diagram=r'''\begin{tikzcd}[row sep=large,column sep=large]
\deleted{\unsure{(38)|(37)}} & 1 \arrow[r,dash] & T^J \arrow[r] \arrow[d] & \mathcal E_{U_{J,\alpha}}^{\bar L} \arrow[r] \arrow[d] & \mathcal E_{D_{J,\alpha}}^{\tilde D_{J,\alpha}} \arrow[r] \arrow[d] & 1 \\
(38) & 1 \arrow[r,dash] & \pi_{U/K}^{\bar L} \arrow[r] & \mathcal E_U^{\bar L} \arrow[r] & \mathcal E_K^{\bar K} \arrow[r] & 1
\end{tikzcd}'''
draft=r'''\scanpage{135}
\mspage{67}

On va donc admettre que (37) définit bien une structure d'extensions, et on aura un hom de suites exactes

\diagram{'''+diagram+r'''}

--- où on a rectifié le tir, en faisant attention que (37) n'a de sens telle quelle que si $D_J$ est connexe, \inserted{i.e. $X_J$ connexe} que sinon il faut regarder les composantes connexes $X_{J,\alpha}$ de $X_J$, induisant les composantes conn $D_{J,\alpha}$ de $D_J$, et $U_{J,\alpha}$ de $U_J$, et écrire la suite exacte pour chaque composante. Bien sûr, il y a des choses plus intrinsèques : écrire avec les topos \deleted{étales \unsure{galoisiens|géométriques}}\inserted{multigaloisiens}, et leurs groupoïdes fondamentaux....\deleted{\unsure{classes de} $\mathcal E_U^{\bar L}$ \unsure{conjugués|conjugaison}}

On voit ainsi que les hom
\[
\tag{39}
T^J\longrightarrow\pi_{U/K}^{\bar L}
\]
induits par les différents $x\in D_J$ --- chacun n'étant en fait, quand on reprend la définition précise, que \inserted{défini} modulo \unsure{opérat|opérations} \unsure{directes|induites} par autom intérieurs de $\mathcal E_U^{\bar L}$, induits par

\margin{134}
'''
(out/'draft.tex').write_text(draft)
r=dict(page='149_scan135',reader='reader_a',line_count=21,changes=[],decisions=[],inventory=[],audit_boxes=[],doubts=[],notes=[],check_events=[],notation=[],abbreviations=[],hand=[],diff_coverage=[],deletion_insertion_review=[])
def ch(id,place,c,h,final,evidence,crop,confidence='high',kind='misread word',against_c=False,against_h=True,marked_in_h=False,consequential=False,error_category=2):
 r['changes'].append(dict(id=id,place=place,c=c,h=h,final=final,evidence=evidence,crop='crops/149_scan135_'+crop+'.png',box=boxes[crop],confidence=confidence,kind=kind,against_c=against_c,against_h=against_h,marked_in_h=marked_in_h,consequential=consequential,error_category=error_category))
ch('P01','L1 after (37)','(37) définit',r'(37) a, \uncertain{définit}','(37) définit','The small loop after the closing parenthesis is the initial d/é group of définit, followed by its long f descender. No separate a or comma precedes that word.','P01',kind='text not on the page',marked_in_h=True,error_category=9)
ch('P02','L2, extensions',r"d'\unsure{extensions|extension}","d'extensions","d'extensions",'A distinct terminal s curls below the baseline after the flattened -ion group; the comma is a separate lower stroke. This resolves C\'s plural/singular choice.','P02',against_c=True,against_h=False)
ch('P03','L2, on aura','on aura',r'on a \uncertain{aussi}','on aura','After on there is one continuous short group: low a/u strokes, an angular r and a terminal a-like loop. No second word or pair of s strokes follows a.','P02',marked_in_h=True)
ch('P04','Diagram (38), two initial horizontal strokes',r'1 \arrow[r,dash] & T^J; 1 \arrow[r,dash] & \pi_{U/K}^{\bar L}',r'1 \arrow[r] & T^{J}; 1 \arrow[r] & \pi_{U/K}^{\overline{L}}',r'1 \arrow[r,dash] & T^J; 1 \arrow[r,dash] & \pi_{U/K}^{\bar L}','Both initial connectors end in short blunt pen returns without a forked arrowhead. The following connectors have visible pointed heads. All objects, three vertical arrows, bars, tildes and indices are retained.','P03',kind='drawing or diagram',error_category=4)
ch('P05','L6, correction of the preceding claim','--- où on a rectifié le tir, en faisant attention',r'— où, pour \uncertain{simplifier} la \uncertain{diction}, on \uncertain{fait} \uncertain{abstraction} \uncertain{du} \uncertain{fait}','--- où on a rectifié le tir, en faisant attention','The long f descender and following accent belong to rectifié; the next words are le and a short crossed-t/dotted-i tir. The later looped f begins faisant, followed by the tall t strokes of attention. H\'s longer introductory phrase has no corresponding ink.','P04',marked_in_h=True,consequential=True)
ch('P06','L7, n\'a','que (37) n\'a de sens',r'que (37) \ill{} de sens','que (37) n\'a de sens','After (37) a low n stroke is followed by an elevated apostrophe and a separate small a loop.','P05',kind='readable ink left as \\ill{}',marked_in_h=True,error_category=5)
ch('P07','L8, interlinear qualification',r'$D_J$ est connexe, \inserted{i.e. $X_J$ connexe}',r'\add{i.e.\ $X_J$ connexe} $D_J$ est connexe,',r'$D_J$ est connexe, \inserted{i.e. $X_J$ connexe}','The smaller i.e. X_J connexe is written over the interval after the main-line connexe/comma and before que sinon. It qualifies that completed clause, rather than preceding D_J.','P06',kind='insertion or placement',error_category=6)
ch('P08','L10, conn',r'\unsure{conn|conn.} $D_{J,\alpha}$',r'conn.\ $D_{J,\alpha}$',r'conn $D_{J,\alpha}$','The final n ends in a connected dark return. The space before D is blank; there is no independent stop. C\'s first alternative is retained without a doubt mark.','P07',kind='abbreviation expanded or spelling modernised',against_c=True,error_category=8)
ch('P09','L14, écrire avec','écrire avec',r'ici \uncertain{avec}','écrire avec','The first word continues beyond é/c through a dotted i and the final r/e low strokes; it is longer than ici. The following small word has the a/v/e/c sequence of avec.','P08',marked_in_h=True)
ch('P10','L14, topos and cancelled qualification',r'topos \deleted{étales \unsure{galoisiens|géométriques}}',r'\uncertain{types} \struck{et les \uncertain{groupoïdes}}',r'topos \deleted{étales \unsure{galoisiens|géométriques}}','The live word has a tall t and a p descender, with low round strokes giving topos. In the cancelled text é and the tall t/l strokes support étales rather than et les. The following crossed word remains uncertain because its loops overlap the replacement; no certainty is inferred from mathematical coherence.','P09',confidence='medium',marked_in_h=True)
ch('P11','L14, replacement terminology',r'\inserted{multigaloisiens}',r'\add{multiplicatifs}',r'\inserted{multigaloisiens}','Above the cancellation, multi is followed by a large descending g loop and an l stem, then dotted i strokes and the -siens ending. The insertion is multigaloisiens, not multiplicatifs.','P09',consequential=True)
ch('P12','L15, location and punctuation of fondamentaux',r'et leurs groupoïdes fondamentaux....',r'\uncertain{fondamentaux}… et leurs groupoïdes',r'et leurs groupoïdes fondamentaux....','The live baseline reads et leurs groupoïdes, then the large f of fondamentaux. Four separately inked points follow its final x. The cancellation below belongs to another phrase.','P10',kind='insertion or placement',marked_in_h=True,error_category=6)
ch('P13','Cancelled phrase after fondamentaux',r'\deleted{\unsure{classes de} $\mathcal E_U^{\bar L}$ \unsure{conjugaison|conjugués}}',r'\struck{classes de $\mathcal{E}_U^{\overline{L}}$-conjugaison}',r'\deleted{\unsure{classes de} $\mathcal E_U^{\bar L}$ \unsure{conjugués|conjugaison}}','A detached accent-like mark near the end and the terminal curl favour conjugués, but the strike hides internal letters, so the alternative conjugaison remains. The line between E_U and the word is the continuous cancellation, not an independently written hyphen; classes de remains doubtful.','P11',confidence='medium',against_c=True)
ch('P14','Formula (39), target symbol',r'T^J\longrightarrow\unsure{\pi|\mathcal E}_{U/K}^{\bar L}',r'T^{J} \longrightarrow \pi_{U/K}^{\overline{L}}',r'T^J\longrightarrow\pi_{U/K}^{\bar L}','The target has a flat roof and two overworked descending legs, rather than the two open lobes of the E symbols. The same target/subscript occurs clearly in the lower row of (38). The full arrow, exponent J, bar L and subscript U/K were checked together.','P12',confidence='medium',kind='misread symbol or index',against_c=True,against_h=False,consequential=True,error_category=1)
ch('P15','L18, chacun',r'\unsure{chacun}','chacun','chacun','An open c is followed by a tall h, small a/c shapes and two flattened u/n strokes. The complete word is readable, resolving C\'s doubt.','P13',against_c=True,against_h=False)
ch('P16','L20, défini',r'\inserted{défini}','défini',r'\inserted{défini}','The compact word has a d loop, long f and two dotted i strokes; it sits slightly above the surrounding que/modulo continuation. Its interlinear placement is retained, although there is no explicit insertion leader.','P14',confidence='medium',kind='insertion or placement',error_category=6)
ch('P17','L20, compressed word following modulo','opérations','opération',r'\unsure{opérat|opérations}','The prefix opérat is readable through the tall t-form. Two detached marks and a flat terminal stroke could complete a very compressed i/on(s) group, but do not securely establish the full spelling. The draft explicitly retains the short/full-form uncertainty instead of silently expanding the possible abbreviation.','P14',confidence='low',kind='abbreviation expanded or spelling modernised',against_c=True,error_category=8)
ch('P18','L21, directes/induites',r'\unsure{induites|directes} par','(nothing)',r'\unsure{directes|induites} par','The initial overtraced loop looks like d followed by an early dotted i; no second i-dot is clear before the tall t. This favours directes, but the first strokes remain overworked, so the order of alternatives changes without resolving the doubt.','P15',confidence='medium',against_c=True,kind='omission',consequential=True,error_category=3)
ch('P19','L21, par autom','par autom.',r"d'automorphismes",'par autom','A separate p descender begins par. autom has a tall t and an attached low terminal m return; there is no detached full stop before intérieurs. The full automorphismes ending is not written.','P15',kind='abbreviation expanded or spelling modernised',against_c=True,error_category=8)
ch('P20','Lower-left foliation',r'\margin{134}','(nothing)',r'\margin{134}','Thin sloping digits show 1, a double-bowed 3 and an angular open 4. They are separate from the dark 67 at the head of the sheet.','P16',kind='omission',error_category=3)
for ident,decision,reading,evidence,crop,confidence in [
 ('M0212','first','extensions','A distinct terminal s precedes a separate comma.','P02','high'),
 ('M0213','first','conn','The dark terminal mark joins the final n; there is no detached stop in the gap before D.','P07','high'),
 ('M0214','first',r'\pi','Flat roof plus two retraced legs, compared with the matching lower-row target in (38); the rest of formula (39) is intact.','P12','medium'),
 ('M0215','first','chacun','Open c, high h, small a/c and low u/n strokes are individually present.','P13','high'),
 ('M0216','undecided',r'\unsure{directes|induites}','The first d-like loop and early i-dot favour the second original alternative, but overtracing prevents a settled reading.','P15','medium')]:
 r['decisions'].append(dict(id=ident,cote='149',scan='135',decision=decision,reading=reading,evidence=evidence,crop='crops/149_scan135_'+crop+'.png',box=boxes[crop],confidence=confidence))
def inv(n,kind,position,first,hand='his hand'):
 r['inventory'].append(dict(scan='149_scan135',sheet_kind='text',hand=hand,element=n,kind=kind,position=position,first_words_or_objects=first,transcribed='yes'))
inv('E01','margin note','top centre; 782,20–863,74','67','dark handwritten pagination')
inv('E02','text','top three lines; 271,64–1585,310',"On va donc admettre que (37) définit bien une structure d'extensions...")
inv('E03','diagram','upper middle; 267,317–1483,635','Two five-object rows, initial dash connectors, three downward arrows; labels (38) and a cancelled number')
inv('E04','deletion','left of upper diagram row; within P03','(38) or (37), crossed out')
inv('E05','text','middle paragraph; 282,660–1661,1681','— où on a rectifié le tir ... écrire avec les topos')
inv('E06','insertion','above D_J est connexe clause; 729,846–1115,911','i.e. X_J connexe')
inv('E07','deletion','after topos; 1074,1534–1589,1610','étales followed by an uncertain cancelled qualification')
inv('E08','insertion','above preceding deletion; 1119,1479–1532,1550','multigaloisiens')
inv('E09','text','lower middle; 312,1614–1647,1776','et leurs groupoïdes fondamentaux....')
inv('E10','deletion','below fondamentaux; 1070,1666–1660,1772','classes de E_U^bar L, then uncertain conjugués/conjugaison')
inv('E11','text','lower paragraph opening; 390,1770–1250,1885','On voit ainsi que les hom')
inv('E12','display','lower middle; 303,1862–1098,2008','(39) T^J → pi_U/K^bar L')
inv('E13','text','last four main lines; 301,1967–1659,2338',"induits par les différents x∈D_J — chacun n'étant en fait ... induits par")
inv('E14','insertion','last-but-one main line; 972,2140–1137,2248','défini')
inv('E15','margin note','lower-left corner; 20,2290–96,2345','134','thin sloping foliation, hand not confidently identified')
def audit(id,kind,box,reading):r['audit_boxes'].append(dict(box=id,kind=kind,xyxy=box,reading=reading))
audit('B01','handwritten number',boxes['P17'],'67')
audit('B02','handwritten number; C/H different words',boxes['P01'],'(37) définit bien')
audit('B03','C/H different words',boxes['P02'],"d'extensions, et on aura un")
audit('B04','struck passage; doubtful formula; handwritten number; C/H different words',boxes['P03'],diagram)
audit('B05','C/H different words',boxes['P04'],'--- où on a rectifié le tir, en faisant attention')
audit('B06','handwritten number; C/H different words',boxes['P05'],"que (37) n'a")
audit('B07','insertion',[729,846,1115,911],r'\inserted{i.e. $X_J$ connexe}')
audit('B08','C/H different words',boxes['P07'],r'conn $D_{J,\alpha}$ de')
audit('B09','C/H different words',boxes['P08'],'écrire avec les topos')
audit('B10','struck passage; insertion; C/H different words',boxes['P09'],r'\deleted{étales \unsure{galoisiens|géométriques}}\inserted{multigaloisiens},')
audit('B11','struck passage; C/H different words; less than high confidence departure',boxes['P10'],r'et leurs groupoïdes fondamentaux....\deleted{\unsure{classes de} $\mathcal E_U^{\bar L}$ \unsure{conjugués|conjugaison}}')
audit('B12','doubtful formula; handwritten number; less than high confidence departure',boxes['P12'],r'(39)\quad T^J\longrightarrow\pi_{U/K}^{\bar L}')
audit('B13','insertion; C/H different words; less than high confidence departure',boxes['P14'],r'\inserted{défini} modulo \unsure{opérat|opérations}')
audit('B14','C/H different words; less than high confidence departure',boxes['P15'],r'\unsure{directes|induites} par autom intérieurs')
audit('B15','margin note; handwritten number',boxes['P16'],'134')
r['doubts']=[
 dict(place='Cancelled number beside upper diagram row',reading=r'\deleted{\unsure{(38)|(37)}}',alternatives='(38), (37); H editorial note suggests (38\')',confidence='medium',reason='The crossing stroke runs through the final numeral; (38) is favoured, but no full certainty is claimed for the struck label.'),
 dict(place='Cancelled qualification following étales',reading=r'\deleted{étales \unsure{galoisiens|géométriques}}',alternatives='galoisiens; géométriques; H suggests groupoïdes',confidence='low',reason='The replacement g-loop overlaps the original word. A further descending loop could belong to the crossed word or overlap, and the individual letters cannot all be separated.'),
 dict(place='Cancelled phrase under fondamentaux',reading=r'\deleted{\unsure{classes de} $\mathcal E_U^{\bar L}$ \unsure{conjugués|conjugaison}}',alternatives='conjugués preferred; conjugaison retained',confidence='medium',reason='A detached accent-like mark and terminal curl favour conjugués, but the long strike hides internal minims. classes de is likewise not resolved under the strike.'),
 dict(place='Formula (39), target',reading=r'\pi_{U/K}^{\bar L}',alternatives='calligraphic E rejected as the working reading',confidence='medium',reason='Roof and legs favour pi and match the corresponding target in (38), but the lower strokes are retraced; departure from C certainty is flagged for audit.'),
 dict(place='Status of défini',reading=r'\inserted{défini}',alternatives='Interlinear addition preferred; ordinary continuation possible',confidence='medium',reason='The word is smaller and slightly higher than the adjacent continuation, but has no insertion leader.'),
 dict(place='Word after modulo',reading=r'\unsure{opérat|opérations}',alternatives='A short opérat-like written form; compressed full opérations (singular opération is H\'s reading)',confidence='low',reason='Only the prefix through the t is secure. Detached marks and the final flat group may form a short i and on(s); abbreviation and full spelling remain unresolved. No terminal stop or superscript is supplied.'),
 dict(place='First word of last main line',reading=r'\unsure{directes|induites}',alternatives='directes preferred; induites retained',confidence='medium',reason='An initial d-like loop and early dotted i favour directes, but the opening has been retraced.')]
r['notes']=[
 dict(id='N01',text='English: The page assumes that (37) defines an extension structure and displays a morphism of two exact sequences. It then “rectifié le tir” by requiring D_J to be connected, with the insertion “i.e. X_J connexe”; otherwise it passes to components indexed by alpha and writes the sequence component by component. This describes the manuscript\'s argument, not an independently verified exactness result.'),
 dict(id='N02',text='English: The proposed intrinsic formulation changes cancelled terminology to “multigaloisiens” and refers to the fundamental groupoids. The page next records maps T^J → pi_{U/K}^{bar L} induced by x in D_J, with qualifications about inner automorphisms. The uncertain final wording is retained and the page ends at “induits par”; no continuation has been supplied.'),
 dict(id='N03',text='English: The diagram has ten mathematical objects, three downward arrows and eight horizontal connectors; the first connector in each row is drawn as a dash. The cancelled and live formula numbers are placed in a separate left label column, preserving their upper/lower positions without nesting the diagram macro inside display math. There are no independent drawings.'),
 dict(id='N04',text='English: 67 is the dark page number at the head and 134 is thin lower-left foliation. line_count counts 21 principal text/display baselines, including the two diagram rows, while excluding marginal and interlinear additions. The whole page and both supplied halves were read, including agreed words. No OCR, outside research or TeX compilation was used.')]
r['notation']=[
 dict(form=r'X_{J,\alpha},\ D_{J,\alpha},\ U_{J,\alpha}',meaning='Component-indexed objects used to replace a disconnected component-free sequence',evidence='Main paragraph explicitly names composantes connexes X_{J,alpha}, inducing the D and U components.'),
 dict(form=r'T^J\longrightarrow\pi_{U/K}^{\bar L}',meaning='Map singled out as (39), corresponding to the left vertical arrow in (38)',evidence='Diagram P03 and whole formula P12; roof and legs identify the working pi reading.'),
 dict(form=r'\mathcal E_{D_{J,\alpha}}^{\tilde D_{J,\alpha}}',meaning='Upper-right nonterminal object in (38); definitions are not supplied on this page',evidence='Diagram crop P03 has a wave above superscript D and repeated J,alpha indices.'),
 dict(form='Four points after fondamentaux',meaning='Literal source punctuation, retained as four points',evidence='P10 shows four separated dark dots after the final x.')]
r['abbreviations']=[dict(form='hom',expansion='homomorphisme(s)'),dict(form='i.e.',expansion='id est'),dict(form='conn',expansion='connexe(s); no stop is written'),dict(form='autom',expansion='automorphismes; no stop is written'),dict(form='opérat (doubtful)',expansion='Possible abbreviation of opération(s); full/short form unresolved')]
r['hand']=[
 dict(habit='n, u and word interiors can become long flat linking strokes; an attached terminal dark return is not necessarily a full stop.',places='149_scan135 conn, autom and the compressed word after modulo',consistency='Clearly relevant to this page; the opérat/opérations ending is left unresolved.',witness_errors='H supplies conn.; C supplies autom.; both expand or interpret the compressed final word more confidently than the crop warrants.'),
 dict(habit='A separate descending final s can be distinguished from the following comma.',places='149_scan135 extensions, P02',consistency='One decisive occurrence used here.',witness_errors='Resolves C\'s extensions/extension uncertainty.'),
 dict(habit='The pi in (39) is retraced below a horizontal roof; matching pi in (38) has clearer two-leg form.',places='149_scan135 P03 and P12',consistency='Same target subscript and superscript on this page; resolution kept at medium confidence.',witness_errors='C offers calligraphic E as an alternative.'),
 dict(habit='Replacement ascenders and descenders can overlap the cancelled word beneath them.',places='149_scan135 étales qualification and multigaloisiens, P09',consistency='One locally dense revision.',witness_errors='C and H disagree on the cancelled word; neither reading is made certain by the replacement\'s meaning.'),
 dict(habit='A small detached stroke at a cancelled word ending can be an accent rather than an i-dot.',places='149_scan135 cancelled conjugués/conjugaison, P11',consistency='The strike prevents a categorical rule; uncertainty retained.',witness_errors='Both witnesses favour conjugaison; crop evidence shifts the tentative preference to conjugués.')]
dis={1:'macro-only: scan marker versus H page note',2:'H editorial page-note wording, not source text; page number 67 retained',3:'P01',4:'P02 / M0212',5:'P03',6:'H editorial diagram-number note is not source text; both physical labels retained, crossed label remains doubtful',7:'same label issue as row 6; C alternative retained; live (38) placed left of lower row',8:'macro-only: row-spacing option',9:'macro-only: column-spacing option',10:'P04, upper initial connector',11:'P04, lower initial connector',12:'macro-only: diagram closing syntax and same dash',13:'P05; no pour simplifier la diction in the ink',14:'P05',15:'P06',16:'P07; main clause stays before inserted qualification',17:'P07; no duplication of the main clause',18:'P08 / M0213',19:'P09',20:'P10 and P11; cancelled qualification remains doubtful',21:'P12; H places fondamentaux on the wrong side of et leurs',22:'P12; four points retained',23:'P13; no separate hyphen under the continuous strike',24:'P13; tentative order conjugués|conjugaison, not full resolution',25:'macro-only: display numbering syntax',26:'macro-only: display numbering syntax',27:'P14 / M0214',28:'macro-only: same dash',29:'P17–P19 and M0216; short/full form and directes/induites remain doubtful, autom retained without stop',30:'P20'}
r['diff_coverage']=[dict(row=i,disposition=dis[i]) for i in range(1,31)]
r['deletion_insertion_review']=[
 dict(text=r'\deleted{\unsure{(38)|(37)}}',scope_attachment='Only the upper formula number is struck; the lower (38) is live. The cancellation does not extend into the row.',evidence='P03, left of both diagram rows.'),
 dict(text=r'\inserted{i.e. $X_J$ connexe}',scope_attachment='Interlinear clarification after D_J est connexe, before que sinon.',evidence='P06: smaller baseline directly above that interval.'),
 dict(text=r'\deleted{étales \unsure{galoisiens|géométriques}}\inserted{multigaloisiens}',scope_attachment='The strike crosses étales and the following original word. multigaloisiens is above, live; the comma to the right survives.',evidence='P09: one long cancellation under the new word; overlapping descenders keep the old second word doubtful.'),
 dict(text=r'\deleted{\unsure{classes de} $\mathcal E_U^{\bar L}$ \unsure{conjugués|conjugaison}}',scope_attachment='Entire small phrase below fondamentaux is cancelled, including its formula. The live main phrase and all four following dots are outside this strike.',evidence='P10–P11: separate baselines and a long horizontal cancellation through the lower phrase.'),
 dict(text=r'\inserted{défini}',scope_attachment='Small raised word after que and before modulo, retained as an insertion at medium confidence.',evidence='P14 and lower half: compact slightly raised baseline, no independent insertion leader.')]
# Match the literal permitted collation kind.
for x in r['changes']:
 if x['kind']==r'readable ink left as \\ill{}':x['kind']=r'readable ink left as \ill{}'
(out/'report.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
print('Saved draft.tex and report.json:',len(r['changes']),'changes,',len(r['decisions']),'marks,',len(r['audit_boxes']),'audit boxes,',len(boxes),'crops.')
