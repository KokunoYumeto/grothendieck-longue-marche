from pathlib import Path
import json
base=Path('SP87_C13_149_work')
page=base/'readers/149_scan096'
manifest=json.loads((page/'crop_manifest.json').read_text())
changes=[]
def add(place,c,h,final,evidence,crop,kind,confidence='high',against_c=False,against_h=True,marked_in_h=False,consequential=False):
    changes.append(dict(place=place,c=c,h=h,final=final,evidence=evidence,crop='crops/149_scan096_'+crop+'.png',box=manifest[crop][0],confidence=confidence,kind=kind,against_c=against_c,against_h=against_h,marked_in_h=marked_in_h,consequential=consequential))
add('initial_pour','pour',r'\ill{}','pour','The word has a tall initial p with a long descender, a small closed o, and two low joined returning strokes for ur. These letters occupy the space between question and des; it is not unreadable material.','pour',r'readable ink left as \ill{}',marked_in_h=True)
add('globales_underline',r'\uline{globales}','globales',r'\uline{globales}','A separate horizontal ink line runs beneath the word, below the letter baseline and independently of the g descender. The source emphasis is retained.','globales','omission')
add('base_B',r'$X/B$',r'$X/S$',r'$X/B$','After the slash is a capital with an upright looped left member and two returning right portions. The additional left member excludes a standalone S.','XB','misread symbol or index',consequential=True)
add('section_g',r'$g$',r'$g_i$',r'$\unsure{g|g_i}$','The g has a closed upper loop and a long descending return. At its upper right are a tiny hooked continuation and a dot, but they do not securely form an independent lowered i. Plain g is preferred; g_i remains possible from those small traces. The later comma is a separate, lower curved stroke.','g_section','misread symbol or index',confidence='medium',consequential=True)
add('avec_live','avec',r'\add{ou}','avec','The baseline word begins with a small closed a-like mark, a low v-shaped return, and a longer joined ec run. It has more than the two strokes of ou and sits on the regular text baseline before le, with no insertion leader.','avec','misread word',confidence='medium')
add('clipped_distingu','distingué','distinguée','distingu','The d/i/s/t/i/n/g sequence and the following short u-shaped continuation are visible. That continuation meets the right paper edge; the remaining ending is clipped. No complete é or extra e can be established from the visible ink, so neither witness’s completed ending is supplied.','distingue','text not on the page',against_c=True,confidence='high')
add('de_une','de une',"d'une",'de une','After part the d has its own joined low e-shaped curl, followed by a clear space and the three low letters of une. No apostrophe replaces that e. The uncontracted wording is retained.','de_une','abbreviation expanded or spelling modernised')
add('donc_after_assoc','donc','(nothing)','donc','At the beginning of the next source line is a looped d followed by a low rounded and returning onc run, then a separate accented à. The whole word donc is present.','donc','omission')
add('pouvait_word','pouvait','pourrait','pouvait','After p and the small o, the low u is followed by one open v-shaped curve before the closed a and dotted i. There are not two independently written r shoulders. The final t has its own upper loop/crossing.','pouvait','misread word')
add('en_tant_que',r'en \unsure{tant|\deleted{tant}} que',r'\struck{\ill{}} en',r'en \unsure{tant|\deleted{tant}} que','The baseline has en, then a word with two tall t strokes enclosing low a/n traces, followed by a separately legible que. A broad upper horizontal stroke can be the common t crossbar; the descender of lequel above ends separately. Live tant is preferred, but cancellation is retained as an alternative because the broad stroke cannot be fully separated from possible striking. H’s unreadable cancelled material and omission of que do not represent this visible run.','en_tant','deletion state',confidence='medium',marked_in_h=True)
add('formula_placement',r"sur $\mathcal E_K$ \inserted{$(29)\quad\unsure{\mathcal E f_K|f_K}=\psi:\mathcal E_K\longrightarrow\mathcal E_{U_K}$} définit",r"que [(29) \varphi=\mathcal E_{f_K}:\mathcal E_K\longrightarrow\mathcal E_{U_K}] la dite section",r"sur $\mathcal E_K$ \inserted{$(29)\quad\unsure{\mathcal E f_K|f_K}=\psi:\mathcal E_K\longrightarrow\mathcal E_{U_K}$} définit",'The numbered formula is a smaller interlinear run between the line ending section de and the line containing E_{U_K} sur E_K définit. Its letter run lies above the gap by E_K/définit, while (29) is far to its left. No leader fixes a unique verbal anchor. C’s placement before définit is retained provisionally, with the physical interline and the possible earlier anchor explicitly noted; H’s placement is not asserted impossible.','formula','insertion or placement',confidence='low')
add('formula_reading',r'\unsure{\mathcal E f_K|f_K}=\psi:\mathcal E_K\longrightarrow\mathcal E_{U_K}',r'\varphi=\mathcal E_{f_K}:\mathcal E_K\longrightarrow\mathcal E_{U_K}',r'\unsure{\mathcal E f_K|f_K}=\psi:\mathcal E_K\longrightarrow\mathcal E_{U_K}','The equals sign follows the crowded f-containing term. To its right is a letter with two open upper arms and a central descending stem: ψ, not the closed oval of φ. A two-dot colon follows, then E_K and a shaft with a clear two-arm right arrowhead toward E_{U_K}. The initial f is full-height relative to this run; a faint curved trace immediately left of it may be an E but is not separable with certainty. Thus neither H’s reversed order nor its certain E with all of f_K as a subscript is imposed.','formula','misread symbol or index',confidence='medium',consequential=True)
add('short_form_tt',r'\unsure{tte|tt}','toute',r'\unsure{tt|tte}','The short form consists of two tall stems with a shared horizontal stroke. Its right end turns downward in a short hook, without a separately traceable e loop. Hence tt is preferred, while tte remains possible if the hook compresses the last letter; the full word toute is not written.','tte','abbreviation expanded or spelling modernised',confidence='medium',against_c=True)
add('no_comma_after_GammaQ',r'\Gamma_{\mathbf Q} ou',r'\Gamma_{\mathbf Q}, ou',r'\Gamma_{\mathbf Q} ou','After the subscript Q there is blank space before the two small strokes of ou. The diagonal through Q belongs to Q itself; no detached comma is present in the gap.','ou_sur','text not on the page')
add('ou_sur','ou sur','ou plutôt sur','ou sur','Immediately after the two small ou strokes comes the curved initial s and low ur run of sur. The intervening space contains no p descender, l/t ascenders, accent, or other letters of plutôt.','ou_sur','text not on the page',marked_in_h=True)
add('folio95',r'\margin{95}','(nothing)',r'\margin{95}','The bottom-left annotation consists of a looped 9 with a long descending stem followed by a 5 with a flat upper bar and a lower rightward bend. It is separate from the running text.','folio95','omission')

marks=[]
def mark(id,decision,reading,evidence,crop,confidence='medium'):
    marks.append(dict(id=id,decision=decision,reading=reading,evidence=evidence,crop='crops/149_scan096_'+crop+'.png',box=manifest[crop][0],confidence=confidence))
mark('M1280','first','associée','After the dotted i, whose low stroke joins the preceding c run, there are two separated small terminal elements: a hooked low element and a final slanted return beneath the accent stroke. They support the two e letters of associée. The reading is medium confidence because of the small pale hand.','assoc')
mark('M1281','undecided',r'\unsure{rationnel|rationnelle}','The ending has one conspicuous tall l-like member followed by a low loop/return. It does not securely distinguish a terminal flourish from compressed extra l/e material. Rationnel remains preferred, without using agreement with pt to settle it.','rational_point')
mark('M1282','undecided',r'\unsure{tant|\deleted{tant}}','The upper horizontal stroke may be the broad shared crossbar of the two t stems; the q descender from lequel ends separately. Live tant is preferred, but an additional cancelling function cannot be excluded from the remaining trace.','en_tant')
mark('M1283','first','de','A small d bowl and its upright are followed by a low e-like joining stroke. The vertical touching that upright can be followed continuously to the final f of relatif above. The dark horizontal follows the d-e join rather than forming a separately identifiable strike. Live de is preferred at medium confidence.','section_de')
mark('M1284','undecided',r'\unsure{\mathcal E f_K|f_K}','The whole formula was checked: =ψ:, E_K, the right arrow and E_{U_K} are visible. The full-height f and its small K are crowded with a faint leading curved trace, which may be E or part of the f/adjacent pen movement. Neither alternative can be eliminated.','formula')
mark('M1285','undecided',r'\unsure{tt|tte}','There are two upright stems and one shared horizontal stroke with a short downward terminal hook. No independent e loop is clear, so tt is now preferred, with tte retained as the unresolved alternative.','tte')

inventory=[]
def inv(element,kind,position,first,hand='main manuscript hand'):
    inventory.append(dict(element=element,kind=kind,position=position,first_words_or_objects=first,sheet_kind='text',hand=hand,transcribed='yes'))
inv('first_paragraph','text','upper body, seven principal baselines','plus une question … dans la structure.')
inv('second_paragraph','text','middle and lower body, twelve principal baselines','Je vais plutôt … une section')
inv('underlined_globales','text','second principal baseline','globales, with one underline')
inv('possible_tant_cancellation','deletion','fifteenth principal baseline, after en','tant; live preferred, cancellation state unresolved')
inv('numbered_formula29','display','interline between principal baselines sixteen and seventeen, with number at far left','(29) E f_K|f_K = ψ : E_K → E_{U_K}')
inv('formula29_insertion','insertion','same interline; provisionally anchored after sur E_K before définit','numbered formula (29)')
inv('Gamma_prime_insertion','insertion','above last principal baseline, leader entering the gap after ouvert','Γ′')
inv('folio95','margin note','bottom-left corner','95','separate foliation hand, unattributed')

second_boxes=[]
def sb(n,key,kind,reading):
    x0,y0,x1,y1=manifest[key][0]
    second_boxes.append(dict(box='149096-B%02d'%n,kind=kind,x0=x0,y0=y0,x1=x1,y1=y1,reading=reading))
sb(1,'pour','text','pour')
sb(2,'globales','underlined text',r'\uline{globales}')
sb(3,'XB','formula',r'$X/B$')
sb(4,'g_section','doubtful formula',r"$\unsure{g|g_i}$,")
sb(5,'avec','text','avec le')
sb(6,'distingue','clipped text','section distingu')
sb(7,'dans','retraced text','dans la')
sb(8,'de_une','text','part de une')
sb(9,'assoc','text','associée')
sb(10,'first_group','formula',r'$\mathcal E_{U_K}$ sur $\mathcal E_K$,')
sb(11,'rational_point','text and formula',r'\unsure{rationnel|rationnelle} $f_K$ de $U_K$ sur $K$.')
sb(12,'donc','text','donc à un')
sb(13,'pouvait','text','pouvait')
sb(14,'en_tant','possible deletion',r'en \unsure{tant|\deleted{tant}} que')
sb(15,'section_de','text with crossing descender','section de')
sb(16,'formula','inserted doubtful formula and handwritten number',r'\inserted{$(29)\quad\unsure{\mathcal E f_K|f_K}=\psi:\mathcal E_K\longrightarrow\mathcal E_{U_K}$}')
sb(17,'tte','short form',r'\unsure{tt|tte} section')
sb(18,'ou_sur','formula and text',r'$\mathcal E_{\mathbf Q}=\Gamma_{\mathbf Q}$ ou sur un sous-')
sb(19,'Gamma_insert','insertion',r"ouvert \inserted{$\Gamma'$} de")
sb(20,'folio95','handwritten number',r'\margin{95}')

notes=("The page moves from global relative curves to formal curve elements along a distinguished section, then returns to a section associated with a K-rational point f_K of U_K. It writes the induced map in formula (29) and begins the statement that composing with a section of E_K over the rational-field Galois group, or over an open subgroup, gives another section. The sentence continues beyond this leaf; no conclusion has been supplied. The formal section identities were checked by reader A as recorded below. The classification implicit in première espèce and the existence of any arithmetic section are not proved here. "
"The whole image and both supplied full-resolution halves were read once against both witnesses, including all agreed words and formula labels; twenty unique crops were then inspected, without recropping any place. The base is B. Globales has one visible underline. The first paragraph’s word at the right edge is transcribed only through the visible prefix distingu; neither the expected é nor H’s extra e is completed, and no illegibility marker is added for missing paper. Dans is heavily retraced but has no separately established deletion or recoverable earlier wording. The noncontracted de une is retained. Associée is resolved at medium confidence from the two small ending elements; rationnel/rationnelle remains open. "
"The small K forms throughout this leaf have a joined, n-like return: direct comparison of E_{U_K} with E_K on the same line, and of f_K/U_K with the explicit standalone K in sur K, supports K locally. They were not changed to eta merely because the latest notation table records an eta-like form elsewhere. The word tant remains uncertain in deletion state. The de after section is retained live: the vertical touching it belongs to the f descender of relatif above, and the dark horizontal is not independently distinguishable from the d-e join. The leading E f_K/f_K in (29), the small mark next to g, and tt/tte remain doubtful. Formula (29) definitely has ψ on the right of the equals sign, a colon, and an ordinary right arrow. Its smaller interlinear placement is certain, but no leader uniquely fixes its linear attachment: C’s anchor before définit is provisional. Γ′ is a genuine insertion attached by a curved leader to the gap after ouvert; the leader is not an opening parenthesis. No comma is supplied after Γ_Q, and plutôt is absent. "
"There are nineteen principal body baselines, one interlinear formula line including its number, one separate Γ′ insertion line, and one foliation line: twenty-two source lines under the inclusive count. There is no separate author page number at the head, and no drawing or standalone diagram. Source line division is reflected in the TeX; the mechanical break in élémentaire is recorded in a comment, and the compound hyphen of sous-groupe is retained. Double quotation marks, dash encoding, Q font choices and editorial alternative separators are handled as macro/editorial differences where they do not change a reading. H’s final note about another use of (29) is editorial, is not transcribed, and was not checked against any other leaf.")

check_events=[
 dict(statement_id='149096-rational-point-section',type='targeted proof check',who='reader A (/root/reader_a)',outcome="Conditional pointed-functoriality check: if u:U_K→Spec K is the structure morphism and f_K:Spec K→U_K is the stated K-rational point, then u∘f_K=id. For compatible geometric base points, applying the fundamental-group functor gives u_*∘(f_K)_*=id_{E_K}; thus the displayed arrow E_K→E_{U_K} has the section direction. Without fixed base points the usual conjugacy qualification remains. This checks the formal consequence of the assumed rational point, not the assertion that an arbitrary section of première espèce comes from one, and it does not resolve the crowded initial E by mathematical expectation."),
 dict(statement_id='149096-composition-of-sections',type='targeted proof check',who='reader A (/root/reader_a)',outcome="Conditional group calculation: let p:E_{U_K}→E_K and r:E_K→Γ_Q be continuous homomorphisms, with pψ=id_{E_K}. If s:Γ_Q→E_K satisfies rs=id, then (rp)(ψs)=r(pψ)s=rs=id, so ψs is a continuous section of rp. For an open subgroup j:Γ′↪Γ_Q and s:Γ′→E_K with rs=j, the same calculation gives (rp)(ψs)=j; hence ψs lands in the pullback over Γ′ and supplies its section. This verifies the formal mechanism suggested by the unfinished final sentence, without asserting the existence of s or a particular continuation of the manuscript."),
 dict(statement_id='149096-geometric-background',type='carried as background without fault found',who='reader A (/root/reader_a)',outcome="The interpretation of E as the relevant fundamental/Galois group, the category of formal curve elements with a distinguished section divisor, the meaning of première espèce, and the geometric relation to a model S are carried as the author's background. No proof of a section classification, model-independent geometric theorem, or arithmetic section existence is claimed from this isolated leaf.")
]
hand_observations=[
 dict(habit='Small K indices can have a joined n-like outline on this leaf.',pages='149_scan096',evidence='The first E_{U_K} and the adjacent E_K have the same joined small return; f_K and U_K repeat it next to a clear full-size K after sur.',witness_errors='No correction of either witness is made at these indices. The local comparisons prevent importing an eta reading merely from a similar outline in the supplied notation table.'),
 dict(habit='Long descenders can meet letters on the next baseline without cancelling them.',pages='149_scan096',evidence='The f of relatif descends to the upright of de below; the q of lequel ends separately above the first t of tant.',witness_errors='C flags the state of de and tant; H treats nearby material as cancelled and unreadable.'),
 dict(habit='A shared t crossbar can end in a hook that resembles a small final letter.',pages='149_scan096',evidence='The short form before section has two uprights and a shared horizontal ending in a downward hook; tant likewise has a broad upper crossbar.',witness_errors='C prefers tte; the visible short form now favors tt while retaining tte. H expands it to toute.'),
 dict(habit='A source word meeting the page edge cannot be completed from grammatical agreement.',pages='149_scan096',evidence='Only distingu remains verifiable before the paper edge.',witness_errors='C completes distingué and H completes distinguée.'),
 dict(habit='ψ is distinguished from φ by open upper arms and a descending central stem.',pages='149_scan096',evidence='The symbol after the equals sign in (29) has two open arms and no closed enclosing oval.',witness_errors='H reads φ and places it before the equals sign.'),
 dict(habit='Heavier retracing is not by itself deletion.',pages='149_scan096',evidence='Dans has darkened a/n/s strokes that follow its own letter forms without a separate crossing stroke.',witness_errors='Both witnesses correctly retain dans; no cancelled predecessor is invented.')
]
notation_additions=[
 dict(written='joined n-like small K after E, U and f',transcription='K in these locally matched indices',evidence='The first_group and rational_point crops link this form to the same named K written fully after sur; the form is not automatically eta.'),
 dict(written='open fork with descending stem after = in (29)',transcription=r'\psi',evidence='The two open upper arms and central descender exclude H’s closed-oval φ.'),
 dict(written='two tall stems with a shared hooked crossbar before section',transcription=r'\unsure{tt|tte}',evidence='The right hook is not separately readable as e; neither abbreviation is expanded in the text.')
]
abbreviations=[dict(form='pt',expansion='point'),dict(form='tt',expansion='toute'),dict(form='tte',expansion='toute')]
unresolved=[
 dict(place='section_g',reading=r'\unsure{g|g_i}',alternatives='Plain g preferred; a tiny hooked return and dot might instead be a small i.',confidence='medium'),
 dict(place='clipped_distingu',reading='distingu',alternatives='The visible prefix is secure; the missing ending beyond the paper edge cannot be recovered from this image. No é or ée is transcribed.',confidence='low'),
 dict(place='rationnel_ending',reading=r'\unsure{rationnel|rationnelle}',alternatives='rationnel preferred; the low return after the tall ending may conceal compressed extra l/e material.',confidence='medium'),
 dict(place='tant_state',reading=r'\unsure{tant|\deleted{tant}}',alternatives='Live tant preferred; the broad horizontal may also have a cancelling function.',confidence='medium'),
 dict(place='formula_initial',reading=r'\unsure{\mathcal E f_K|f_K}',alternatives='E f_K preferred, but the faint leading curve cannot be separated securely from the f/adjacent pen movement.',confidence='medium'),
 dict(place='formula_attachment',reading='Insertion provisionally after sur E_K and before définit.',alternatives='The formula lies between the two physical baselines; no leader uniquely excludes an anchor before la dite section.',confidence='low'),
 dict(place='short_form_tt',reading=r'\unsure{tt|tte}',alternatives='tt preferred; tte remains possible if the terminal hook compresses e.',confidence='medium')
]

coverage=[]
def cov(id,place=None,reason=''):
    coverage.append(dict(diff_id=id,disposition='substantive' if place else 'macro/editorial only',change_place=place or '',reason=reason))
cov('D0442',reason='96 is the scan macro, not source handwriting.')
cov('D0443','initial_pour','H leaves the visible word pour as illegible.')
cov('D0444',reason='Both witnesses mark the same quotation opening; the source has double marks, encoded under the supplied two-backtick convention rather than typographic guillemets.')
cov('D0445',reason='The same quoted words and closing double marks are represented by different quotation typography; there is no lexical addition or omission.')
cov('D0446',reason='Both full witnesses include the source dash, as TeX --- and a Unicode em dash. The extraction loses H’s dash token.')
cov('D0447','base_B','The source has B after the slash.')
cov('D0448','section_g','The index i is not secure; plain g remains the preferred reading with g_i retained under doubt.')
cov('D0449','avec_live','The baseline word is avec, not an inserted ou.')
cov('D0450','clipped_distingu','Neither completed witness ending is visible beyond the paper edge; only distingu is transcribed.')
cov('D0451','de_une','The source writes separate de une without contraction.')
cov('D0452','donc_after_assoc','Donc is source text omitted by H. C’s alternative associé is editorial doubt syntax; M1280 resolves its preferred associée at medium confidence.')
cov('D0453',reason='The extra rationnelle token is C’s unresolved alternative, not a second source word. Both preferred readings remain rationnel; M1281 and the unresolved list retain the ending doubt.')
cov('D0454','pouvait_word','The low v-shaped member supports pouvait rather than the two r letters of pourrait.')
cov('D0455','en_tant_que','The visible en tant que run includes que and a tentatively live tant; H’s unreadable cancelled material does not preserve its wording/state.')
cov('D0456','formula_placement','H places the formula earlier in the linear text. Its exact source anchor is unresolved, with C’s anchor retained provisionally; the distinct substantive symbol/order errors are separately recorded under formula_reading.')
cov('D0457',reason='H has de in the full witness; the apparent difference is the extra copy in C’s state alternative. M1283 resolves live de, matching both preferred readings.')
cov('D0458','formula_reading','The formula has the crowded f-containing term before =ψ:, not H’s φ=E_{f_K}. Physical placement is separately recorded under formula_placement.')
cov('D0459','short_form_tt','The actual short form is retained, now with tt preferred and tte possible; H expands it to toute.')
cov('D0460','no_comma_after_GammaQ','No detached comma occurs after the subscript Q.')
cov('D0461','ou_sur','The source goes directly from ou to sur; plutôt is not present.')
cov('D0462','folio95','The lower foliation 95 is visible. H’s concluding claim about another occurrence of (29) is editorial and creates no source-text row.')

report=dict(scan=96,line_count=22,changes=changes,marks=marks,inventory=inventory,second_boxes=second_boxes,notes=notes,check_events=check_events,hand_observations=hand_observations,notation_additions=notation_additions,abbreviations=abbreviations,unresolved=unresolved,diff_coverage=coverage)
(page/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'changes':len(changes),'against_C':sum(c['against_c'] for c in changes),'against_H':sum(c['against_h'] for c in changes),'marks':len(marks),'inventory':len(inventory),'second_boxes':len(second_boxes),'unresolved':len(unresolved),'diffs':len(coverage)},indent=2))
