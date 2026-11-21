from pathlib import Path
import json
base=Path('SP87_C13_149_work')
page=base/'readers/149_scan093'
manifest=json.loads((page/'crop_manifest.json').read_text())
changes=[]
def add(place,c,h,final,evidence,crop,kind,confidence='high',against_c=False,against_h=True,marked_in_h=False,consequential=False):
    changes.append(dict(place=place,c=c,h=h,final=final,evidence=evidence,crop='crops/149_scan093_'+crop+'.png',box=manifest[crop][0],confidence=confidence,kind=kind,against_c=against_c,against_h=against_h,marked_in_h=marked_in_h,consequential=consequential))
add('body_double_tilde',r'$\widetilde{\widetilde K}$',r'$\widetilde K$',r'$\widetilde{\widetilde K}$','Above the body K after the first comma are two separately traceable wavy strokes at different heights. The inserted group immediately to the left has only one tilde; its spelling has not been harmonized with this one.','double_tilde','misread symbol or index',consequential=True)
add('strict_parentheses',r'(\deleted{\illegible{2}} strict)',r'\struck{\ill{}} strict',r'(\deleted{\illegible{2}} strict)','A separate opening curved stroke stands to the left of the lower crossed ink, and a long closing curve follows strict. Both curves are independent of the cancellation strokes. The illegibility extent is editorial, not a manuscript numeral.','strict','omission')
add('crossed_corps_de',r'\deleted{est celui du corps de}',r'\struck{est celui du complété}',r'\deleted{est celui du \unsure{corps de|complété}}','After du the surviving start is an open c and low rounded letters, followed by a descending p-like stroke and a separate final tall d-like stem with low continuation. That favors corps de; the crossing obscures the small interior letters, so the whole phrase remains doubtful. The l/t sequence required by complété is not separately visible.','Ns_replacement','misread word',confidence='medium')
add('literal_equal',r"s'identifie de $=$ à",r"s'identifie de même à",r"s'identifie de $=$ à",'Between de and à stand two short parallel horizontal bars with clear separation, rather than written letters. The sign is retained literally; même is recorded only as its expansion.','Ns_replacement','abbreviation expanded or spelling modernised')
add('strict_no_stop','pas strict)','pas strict).','pas strict)','After the long closing parenthesis the remaining visible right-hand space is blank; no detached dot follows it.','strict_end','text not on the page')
add('cancelled_de',r'\deleted{de}','(nothing)',r'\deleted{de}','The small crossed word has a tall looped d joined to a low e. An oblique stroke passes across those letters; the deletion is present between composé and the formula.','de_composite','omission')
add('composite_connectors',r'\mathrel{\text{---}} ... \mathrel{\text{---}}',r'\to ... \to',r'\mathrel{\text{---}} ... \mathrel{\text{---}}','Both horizontal connectors have a short terminal return, but neither has an independently traceable pair of arrowhead arms. They are retained as plain shafts, in contrast to the unmistakable two-arm arrowhead in the later local-comparison formula.','composite','misread symbol or index',confidence='medium',consequential=True)
add('composite_nested_index',r'\mathcal E_{U_K}',r'\mathcal E_{U_K}',r'\mathcal E_{U_{\unsure{\eta|K}}}','The small nested character has a low start, a rounded high hump, and a descending right return. It lacks the distinct separated branching strokes of the larger K at the left of this same formula. Eta is preferred, but the return can resemble a compressed k/K, so both readings remain.','composite','misread symbol or index',confidence='medium',against_c=True,consequential=True)
add('a_priori_word','a priori,','lequel','a priori,','The insertion begins with a separate low a, then a long descending p, a short r, two visible i dots in priori, and a comma. There is no initial l ascender or qu sequence.','a_priori','misread word',marked_in_h=True)
add('a_priori_placement',r"s'annule sur $I_{s'}$ \inserted{(a priori, il envoie $I_{s'}$ dans $\pi$)}",r"(lequel il envoie $I_{s'}$ dans $\pi$) s'annule sur $I_{s'}$",r"s'annule sur $I_{s'}$ \inserted{(a priori, il envoie $I_{s'}$ dans $\pi$)}",'The parenthetical is a smaller interlinear run above the s’annule line, beginning over its right-hand I/subsequent gap and continuing over the following parenthesis. There is no leader moving the baseline s’annule clause to its right. The C anchor after I is retained as the closest linear representation; the physical interline is recorded separately.','a_priori','insertion or placement',confidence='medium')
add('cancelled_pour',r'\deleted{\unsure{pour}}','(nothing)',r'\deleted{\unsure{pour}}','Beneath the inserted parenthetical lies a separately cancelled short word: a descending initial loop and a small lower rounded bowl remain beneath a long strike. They favor pour, but the strike conceals the interior and final letters. No certainty is added.','pour','omission',confidence='low')
add('first_que_state',r'\unsure{\deleted{que}|que}','que',r'\unsure{\deleted{que}|que}','The first que has a long horizontal trace crossing its low letter run, unlike the clearly separated low curves of the later que. The first q also has an unusually angular return; the trace could partly be the natural joining stroke. Cancellation remains the preferred but unresolved state.','first_que','deletion state',confidence='medium')
add('s_prime',r"$s'\in S'$",r"$s\in S'$",r"$s'\in S'$",'A short detached raised curved mark sits immediately to the upper right of the small s before the membership sign. The larger S also has its own separate prime.','first_que','misread symbol or index',consequential=True)
add('second_que',r'\unsure{que|\deleted{que}}',"qu'on a",'que','The second word consists of a closed q bowl with a long descender followed by two low joined letter curves. There is no apostrophe, separate on, or final a. No independent cancelling stroke crosses this word.','second_que_hom','misread word',marked_in_h=True)
add('hom_no_stop','hom','hom.','hom','The final m ends in a connected downward return; the space after it is blank. There is no separate abbreviation point.','second_que_hom','text not on the page')
add('leftward_isomorphism',r'\xleftarrow{\sim}',r'\simeq',r'\xleftarrow{\sim}','The lower stroke is a horizontal shaft with an explicit left-pointing two-arm head. A separate wavy sign lies above its center. It is an isomorphism-marked leftward arrow, not a bare inline relation.','local_arrow','misread symbol or index',consequential=True)
add('peut_donc_state',r'\deleted{peut} \inserted{donc}','peut',r'\deleted{peut} \inserted{donc}','A straight stroke crosses the p/e/u/t run. Above the following gap stands donc, with a tall d and low continuation; a curved leader rises from the gap after the cancelled word to this inserted run. The leader does not cancel s’inter.','peut_donc','deletion state',consequential=True)
add('interpretation_ending',r'\unsure{prète|préter}','préter',r'\unsure{prète|préter}','After the tall medial stroke is a small low loop and a long ending with a short downward return. The final return does not securely separate terminal e from er, and the accent shape is also compressed. The C preferred ending is retained with both alternatives rather than inferred from grammar.','prete','misread word',confidence='medium')
add('cancelled_Alors',r'\deleted{\unsure{Alors}}',r'\struck{\ill{}}',r'\deleted{\unsure{Alors}}','A densely crossed tall initial complex is followed by surviving low rounded letters and an r/s-like tail before On. This supports the tentative Alors, but the cancelled initial and interior are not fully recoverable.','Alors_vu',r'readable ink left as \ill{}',confidence='low',marked_in_h=True)
add('On_a_vu','On a vu','On sait','On a vu','After On there is a separate small closed a, then a low v-shaped entry and u-like return. There is no dotted i followed by the tall terminal t that sait would require.','Alors_vu','misread word')
add('reciprocal_word','réciproque','inverse',r'\unsure{réciproque|inverse}','The compressed word begins with a short upright r-like stroke followed by a largely horizontal low letter run; no distinct medial v of inverse is visible. The opening and extent favor réciproque, but several interior letters cannot be separately traced, so the alternative remains in the diplomatic text.','reciproque','misread word',confidence='medium')
add('fonction_word','fonction','section','fonction','The first letter has a tall loop, a long descender, and a crossbar, matching the separate mathematical f immediately to the right. A later tall crossed stroke and i dot support the tion ending. An initial s is excluded by the tall looped stem.','fonction','misread word',consequential=True)
add('conditions',r'si $g\geq1$ ou si $S$ de dim $1\ldots$',r'hors codim. $\geq2$ …',r'si $g\geq1$ ou si $S$ de dim $1\ldots$','The run starts with a small s and dotted i, then a descending g. The inequality has an upper chevron and a separate lower stroke and is followed by a single upright 1. Farther right are distinct ou, dotted si, a large S, de dim, and a second upright 1 with foot, then three dots. There is no 2 or written hors codim in this run.','conditions','misread word',marked_in_h=True,consequential=True)
add('no_extra_ink_before_en_fait','en fait',r'\ill{} en fait','en fait','The final baseline begins with the small en followed by the tall looped/crossed f of fait. The margin before en is blank; no separate unreadable word or cancellation precedes it. The previous line ends at the visible closing parenthesis.','en_fait','text not on the page',marked_in_h=True)
add('tantot_word',r'\unsure{tantôt}',"tout à l'heure",'tantot','One compact word has a tall initial t, low joined a/n traces, another t, a small closed o, and a final tall t, followed by a comma. There are no separate à or l’heure words, and no independent circumflex is visible above the o. The written unaccented form is retained.','tantot','abbreviation expanded or spelling modernised',confidence='medium',against_c=True)
add('lower_folio',r'\margin{92}','(nothing)',r'\margin{92}','At the bottom left is a separate 9 with a long descending stem followed by an angular 2 with a horizontal foot. It is an isolated marginal number, not part of the running sentence.','folio92','omission')

marks=[]
def mark(id,decision,reading,evidence,crop,confidence):
    marks.append(dict(id=id,decision=decision,reading=reading,evidence=evidence,crop='crops/149_scan093_'+crop+'.png',box=manifest[crop][0],confidence=confidence))
mark('M1268','undecided',r'\unsure{\deleted{que}|que}','The long horizontal trace traverses the first que, but it cannot be fully distinguished from joining strokes around the unusually angular q return. The preferred cancellation is retained without resolving the state.','first_que','medium')
mark('M1269','first','que','The q bowl and descender and following low u/e curves remain unobscured. No separate strike crosses this word and no additional apostrophe or on a letters follow it.','second_que_hom','high')
mark('M1270','undecided',r'\unsure{prète|préter}','The short final downward return can be an e flourish or a compressed final r. The crop does not warrant deciding between the two spellings.','prete','medium')
mark('M1271','other','tantot','The crop supports a single tantot run with three tall t strokes and a low closed o. There is no detached circumflex over the o; C’s accented spelling is not silently supplied.','tantot','medium')

inventory=[]
def inv(element,kind,position,first,hand='main manuscript hand'):
    inventory.append(dict(element=element,kind=kind,position=position,first_words_or_objects=first,sheet_kind='text',hand=hand,transcribed='yes'))
inv('main_text_1','text','upper body, four principal baselines','où I_s′ … hensélisé pas strict)')
inv('main_text_2','text','middle and lower body, fourteen principal baselines','Ceci posé … relatif à')
inv('author_page_number','margin note','top, near center','46','numbering hand; heavier ink than the body')
inv('lower_folio','margin note','bottom left','92','separate numbering annotation; attribution undetermined')
inv('first_deleted_phrase','deletion','first principal baseline after I_s′','est le groupe')
inv('first_inserted_identification','insertion','above first principal baseline, attached to replacement of est le groupe','≃ E with single-tilded K subscript')
inv('strict_cancelled_fragments','deletion','before strict within parentheses, with one crossed fragment above and another on the principal baseline','illegible crossed material in two vertical zones')
inv('Ns_deleted_phrase','deletion','third principal baseline after N_s′','est celui du corps de|complété')
inv('Ns_inserted_identification','insertion','above third principal baseline','s’identifie de = à')
inv('deleted_de','deletion','sixth principal baseline between composé and the composite','de')
inv('a_priori_parenthetical','insertion','above seventh principal baseline, over I_s′ and following gap','(a priori, il envoie I_s′ dans π)')
inv('deleted_pour','deletion','seventh principal baseline beneath the insertion','pour, doubtful')
inv('first_que_possible_deletion','deletion','eighth principal baseline after justement','que; cancellation state unresolved')
inv('peut_deletion','deletion','tenth principal baseline after qui','peut')
inv('donc_insertion','insertion','above tenth principal baseline, with curved leader from after cancelled peut','donc')
inv('Alors_deletion','deletion','thirteenth principal baseline before On a vu','Alors, doubtful')

second_boxes=[]
def sb(n,key,kind,reading):
    x0,y0,x1,y1=manifest[key][0]
    second_boxes.append(dict(box='149093-B%02d'%n,kind=kind,x0=x0,y0=y0,x1=x1,y1=y1,reading=reading))
sb(1,'first_identification','deletion and insertion',r'\deleted{est le groupe} \inserted{$\simeq\mathcal E_{\widetilde K}$}')
sb(2,'double_tilde','formula',r'$\widetilde{\widetilde K}$')
sb(3,'strict','deletion',r'(\deleted{\illegible{2}} strict)')
sb(4,'Ns_replacement','deletion and insertion',r"\deleted{est celui du \unsure{corps de|complété}} \inserted{s'identifie de $=$ à}")
sb(5,'strict_end','text','hensélisé pas strict)')
sb(6,'de_composite','deletion',r'\deleted{de}')
sb(7,'composite','doubtful formula',r'$\mathcal E_K\mathrel{\text{---}}\mathcal E_{U_{\unsure{\eta|K}}}\mathrel{\text{---}}\mathcal E_U$')
sb(8,'a_priori','insertion',r"\inserted{(a priori, il envoie $I_{s'}$ dans $\pi$)}")
sb(9,'pour','deletion',r'\deleted{\unsure{pour}}')
sb(10,'first_que','deletion state and formula',r"\unsure{\deleted{que}|que} $s'\in S'\ldots$)")
sb(11,'second_que_hom','text','que un hom')
sb(12,'local_arrow','formula',r'$\mathcal E_{k(s)}\longrightarrow\mathcal E_{U_{\widetilde{\mathcal O}_s}}\xleftarrow{\sim}\mathcal E_{X_s}$')
sb(13,'peut_donc','deletion and insertion',r'qui \deleted{peut} \inserted{donc}')
sb(14,'prete','text',r'\unsure{prète|préter} comme')
sb(15,'Alors_vu','deletion and text',r'\deleted{\unsure{Alors}} On a vu que')
sb(16,'codim_one','handwritten number',r'de codim $1$')
sb(17,'reciproque','text',r"l'image \unsure{réciproque|inverse} du diviseur")
sb(18,'fonction','text',r'la fonction $f$')
sb(19,'conditions','text and handwritten numbers',r'définie si $g\geq1$ ou si $S$ de dim $1\ldots$)')
sb(20,'tantot','text','de tantot,')
sb(21,'number46','handwritten number',r'\mspage{46}')
sb(22,'folio92','handwritten number',r'\margin{92}')
sb(23,'en_fait','text and formula',r'en fait le $\mu=\mu_\alpha$')

notes=("The page identifies inertia and decomposition-type groups with Galois groups of strict and non-strict henselian fraction fields, then uses vanishing on inertia to obtain a residue-field homomorphism and interprets it as a section after a local comparison. It next recalls the codimension-one complement D = S minus S′ as an inverse image of a divisor and begins an unfinished reference to μ = μ_α. The quotient argument was checked conditionally as recorded below; the geometric hypotheses and earlier definitions are not supplied by this isolated leaf. "
"The first inserted group has a single tilde over K, whereas the immediately following body field has two distinct tildes. Both spellings are retained, without making the first match the strict-henselization description. The source calls f a fonction and says de X sur S; these words are not repaired to section or reversed. If that phrase is read as a literal direction X→S, the inverse image of T⊂X would require further clarification; no unqualified geometric proof is claimed. "
"The whole page and both supplied halves were checked against both witnesses, including agreed text; 23 unique crops were inspected, with no place recropped. The first que remains uncertain in deletion state, while the second que is live. The crossed strict fragments, corps de, pour, Alors, the word ending prète/préter, and compressed réciproque remain explicitly doubtful where appropriate. The plain composite shafts have only terminal pen returns; the local comparison has a genuine left arrowhead with a separate wavy sign above. The nested composite subscript is retained as η|K. The word tantot has no independently visible circumflex. The short forms hom, codim and dim and the literal shorthand = remain unexpanded. H’s extra ill before en fait and its final explanatory note have no source-text counterpart. H’s final note is editorial and is not transcribed. "
"There are 18 principal body baselines, four separately placed inserted runs, one additional upper crossed fragment before strict, and two isolated handwritten number lines: 25 source lines under this inclusive count. The lower crossed strict fragment is counted on the second principal baseline. C’s illegibility extent 2 is retained as an annotation for the crossed area, not asserted as a readable numeral or as two recovered words. The source word s’interprète/préter is divided between two baselines; the TeX percent at the break prevents an invented internal space. No standalone diagram, drawing, or additional marginal prose is present. Physical placement of the first inserted identification is recorded in the inventory and second box; identical wording expressed inline in H does not add a macro-only lexical collation row.")

check_events=[
 dict(statement_id='149093-quotient-section',type='targeted proof check',outcome="Conditional verification: let q:N→G be a continuous quotient map with kernel I, and let φ:N→E be continuous with φ(I)=1. Define barφ(q(n))=φ(n). If q(n)=q(n′), then n′⁻¹n∈I, so the value is independent of the representative. It is a homomorphism and is continuous by the quotient topology; surjectivity of q proves uniqueness. If p:E→G additionally satisfies pφ=q, then p barφ q=q, hence p barφ=id_G and barφ is a section. This checks the formal step asserted on the page under those assumptions; it does not establish the required geometric exact sequence or comparison isomorphism from this leaf alone."),
 dict(statement_id='149093-henselian-comparison',type='carried as background without fault found',outcome="The identifications of the inertia/decomposition groups with the relevant henselian-field Galois groups, and the displayed local comparison with E_{X_s}, are carried as the author's background. No independent proof of these geometric identifications was attempted from the isolated page. The visibly different tilde multiplicities are a transcription issue and were not silently corrected using this background."),
 dict(statement_id='149093-divisor-purity',type='carried as background without fault found',outcome="The codimension-one assertion is plausible for the inverse image of an effective Cartier divisor when the pullback remains an effective Cartier divisor on a suitable noetherian base. The needed morphism direction, non-zero-divisor condition and local hypotheses are not established on this leaf, and the stated alternative involving g or dim S is not proved here. The wording fonction f de X sur S is therefore preserved without treating the purity assertion as independently verified.")
]
hand_observations=[
 dict(habit='A literal equals sign substitutes for même in running French.',pages='149_scan093',evidence='The inserted s’identifie de = à has two separated horizontal bars between de and à.',witness_errors='H expands the sign to même.'),
 dict(habit='Tilde multiplicity and small nested letter form must be checked locally.',pages='149_scan093',evidence='The inserted first group has one tilde; the next body field has two. In the composite the outer K has distinct branches, whereas the small nested mark has a rounded hump and descending return.',witness_errors='H drops one body tilde; both witnesses make the nested index K without marking its η-like form.'),
 dict(habit='Terminal pen returns can resemble arrowheads or final letters.',pages='149_scan093',evidence='The two composite shafts end in a single short return, while the later arrow has two distinct arms. The ending after prète has a similar short return that does not settle e versus er.',witness_errors='H supplies arrows to the first two shafts and makes the final word ending certain.'),
 dict(habit='Accents and abbreviation points are not consistently supplied.',pages='149_scan093',evidence='No detached circumflex is visible in tantot, and no period follows hom, codim or dim.',witness_errors='C supplies a circumflex in tantôt; H adds a point to hom and paraphrases tantot.'),
 dict(habit='Corrections can be split over a baseline and a smaller interline with a curved leader.',pages='149_scan093',evidence='The first identification and s’identifie are above cancelled text; donc is reached by a curved leader after crossed peut; the strict cancellation occupies two vertical zones.',witness_errors='H leaves peut live and omits donc, and places the a priori parenthetical before the baseline clause.')
]
notation_additions=[
 dict(written='single tilde in first inserted group; two tildes on following body K',transcription=r'\mathcal E_{\widetilde K}; \widetilde{\widetilde K}',evidence='Separate strokes in the first_identification and double_tilde crops; retain their mismatch.'),
 dict(written='small rounded nested index after U',transcription=r'\mathcal E_{U_{\unsure{\eta|K}}}',evidence='The rounded hump/right return differs from the separate branches of outer K in the same composite crop.'),
 dict(written='plain composite shafts; later left arrow with separate wavy sign',transcription=r'\mathrel{\text{---}}; \xleftarrow{\sim}',evidence='Only the later relation has a distinct two-arm arrowhead; the wave is above its shaft.'),
 dict(written='tantot',transcription='tantot',evidence='No independent circumflex appears above the o in the final-line crop.')
]
abbreviations=[dict(form='=',expansion='même'),dict(form='hom',expansion='homomorphisme'),dict(form='codim',expansion='codimension'),dict(form='dim',expansion='dimension')]
unresolved=[
 dict(place='strict_cancelled_fragments',reading=r'\deleted{\illegible{2}}',alternatives='The two crossed vertical zones do not yield complete recoverable words; no proposed wording is promoted.',confidence='low'),
 dict(place='crossed_corps_de',reading=r'\unsure{corps de|complété}',alternatives='corps de preferred; complété retained because cancellation obscures interior letters.',confidence='medium'),
 dict(place='composite_nested_index',reading=r'\unsure{\eta|K}',alternatives='η preferred; K remains possible in the compressed small hand.',confidence='medium'),
 dict(place='cancelled_pour',reading=r'\deleted{\unsure{pour}}',alternatives='pour is tentative; strike conceals the interior and last letters.',confidence='low'),
 dict(place='first_que_state',reading=r'\unsure{\deleted{que}|que}',alternatives='Cancelled que preferred; live que cannot be excluded because the crossing might partly be a joining stroke.',confidence='medium'),
 dict(place='interpretation_ending',reading=r'\unsure{prète|préter}',alternatives='prète preferred; préter possible from the terminal return.',confidence='medium'),
 dict(place='cancelled_Alors',reading=r'\deleted{\unsure{Alors}}',alternatives='Alors remains tentative; the initial and interior letters are heavily cancelled.',confidence='low'),
 dict(place='reciprocal_word',reading=r'\unsure{réciproque|inverse}',alternatives='réciproque preferred from the initial stroke and extent; inverse retained under local doubt.',confidence='medium')
]

coverage=[]
def cov(id,place=None,reason=''):
    coverage.append(dict(diff_id=id,disposition='substantive' if place else 'macro/editorial only',change_place=place or '',reason=reason))
cov('D0365',reason='Scan and manuscript-page metadata use different macros; 46 is independently checked and inventoried. The scan number 93 is not source handwriting.')
cov('D0366',reason='H’s de l’auteur is editorial page-label prose, not manuscript text.')
cov('D0367','strict_parentheses','Opening parenthesis is source ink. The extracted 2 is C’s illegibility extent annotation, not a source numeral; that part is macro/editorial only.')
cov('D0368','strict_parentheses','Closing parenthesis after strict is a separate visible curve.')
cov('D0369','crossed_corps_de','Cancelled lexical disagreement retained with local uncertainty and C as preferred reading.')
cov('D0370','literal_equal','H expands the literal equals shorthand.')
cov('D0371','strict_no_stop','No point follows the closing parenthesis.')
cov('D0372','cancelled_de','H omits the legible cancelled de.')
cov('D0373','composite_connectors','First connector is a plain shaft with a single terminal return.')
cov('D0374','composite_connectors','Second connector is likewise retained as a plain shaft.')
cov('D0375','a_priori_placement','The baseline s’annule clause is not omitted in the source; the difference comes from H’s reordered interlinear parenthetical.')
cov('D0376','a_priori_word','The insertion starts a priori, with a distinct p descender and i dots.')
cov('D0377','cancelled_pour','H omits the cancelled word. The accompanying s’annule displacement is separately recorded under a_priori_placement.')
cov('D0378','s_prime','The prime on s is visible. The same extracted span also represents the independently recorded first_que_state uncertainty; the vertical bar itself is editorial alternative notation.')
cov('D0379',reason='C already has the source ellipsis as \\ldots; H has a Unicode ellipsis. The apparent addition is a tokenization/macro difference.')
cov('D0380','second_que','Only live que is present, without the added on a letters. The C alternative separator is editorial.')
cov('D0381','hom_no_stop','No abbreviation point is written after hom.')
cov('D0382','leftward_isomorphism','C’s arrow macro was suppressed by extraction; the source has an actual left arrowhead and an upper wave, unlike H’s bare relation.')
cov('D0383','peut_donc_state','Peut is struck and donc inserted. The associated ending difference is separately preserved under interpretation_ending and supplied mark M1270.')
cov('D0384','cancelled_Alors','H leaves the cancelled word wholly illegible; C’s tentative Alors remains the preferred unresolved reading.')
cov('D0385','On_a_vu','The ink reads separate a and vu, not sait.')
cov('D0386',reason='The tilde here is H’s TeX nonbreaking space after codim, not a manuscript sign.')
cov('D0387','reciprocal_word','Réciproque remains preferred with local doubt over compressed interior letters.')
cov('D0388','fonction_word','The tall looped and crossed initial f rules out section.')
cov('D0389','conditions','The written phrase starts si g, not hors codim.')
cov('D0390','conditions','Both numerals are 1, and the alternative ou si S de dim is present. H’s additional ill before en fait is also checked separately under no_extra_ink_before_en_fait.')
cov('D0391','tantot_word','The source has a single unaccented tantot; C’s accent and H’s expanded phrase are not supplied.')
cov('D0392','lower_folio','The handwritten marginal 92 is present. H’s long concluding note is explicitly editorial and has no source-text counterpart, so it creates no additional lexical collation row.')

report=dict(scan=93,line_count=25,changes=changes,marks=marks,inventory=inventory,second_boxes=second_boxes,notes=notes,check_events=check_events,hand_observations=hand_observations,notation_additions=notation_additions,abbreviations=abbreviations,unresolved=unresolved,diff_coverage=coverage)
(page/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'changes':len(changes),'against_C':sum(c['against_c'] for c in changes),'against_H':sum(c['against_h'] for c in changes),'marks':len(marks),'second_boxes':len(second_boxes),'inventory':len(inventory),'diffs':len(coverage),'unresolved':len(unresolved)},indent=2))
