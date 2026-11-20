from decision_helpers import *
import copy

r=load_reports(183)
diffs=[row(r,'C',i) for i in range(35)]
cm={0:'A/l3_donc_categories.png',1:'A/l3_donc_categories.png',2:'B/l04_constant_ending.png',7:'A/l6_cancellation_replacement.png',10:'main/01_etc_stop.jpg',12:'main/02_paragraph_boundary.jpg',13:'A/l10_first_addition.png',15:'A/l11_second_addition.png',26:'main/03_linearisation_quotes.jpg',33:'B/l23_sur_x.png'}
for i,p in cm.items():diffs[i]['crop']='crops/scan183/'+p
diffs[0]['evidence']='The looped d, closed low o, low n and open terminal c are separately supported. The extra middle ink is retracing, without a distinct cancellation shaft. All three readers and root resolve donc.'
diffs[1]['evidence']='One compressed des group follows donc; there is no intervening la. The end of catégories has the separate downward-curled s movement. The plural phrase is read from the strokes, independently of the category interpretation.'
diffs[2]['evidence']='The last t runs into a long exit without a securely isolated s. The adjoining tordus has a more distinct terminal curl. Constant remains first, but a reduced s cannot be excluded; grammatical agreement does not settle it.'
diffs[3].update(final=r'\unsure{module|modules}',differs_C=True,evidence='Root selects A/B’s module-first reading against C’s modules-first reading. A low e-like element and flat terminal exit follow l; there is no separately formed s before the distinct comma. A reduced s remains possible, so the doubt is retained with its preferred order changed.')
diffs[4].update(evidence='A compact high point around (344,446) and a larger comma-shaped lower stroke to its lower right are physically distinct; the superscript i has its own separate dot. Root selects C’s semicolon-first uncertainty over A’s comma plus separately drawn point and B’s plain comma. The alternative is a comma with the same upper point of unassigned role, not absence of that point. Minus, M, degree i and parentheses remain secure.',consequential='Against C/H: the argument separator of H^i has an additional upper point. Semicolon is preferred, with comma plus a detached point retained; expected cohomology notation does not determine the mark.')
diffs[5]['evidence']='Root selects A/C’s le-first uncertainty over B’s la-first order. The tall l loop is followed by a small flat loop; no separate a downstroke is secure. The adjacent beginning of structure has no independently recoverable older text at this occurrence.'
diffs[7]['evidence']='The a-like body and tall b loop survive the cancellation; a possible abbreviation stop lies under its rule. A distinct descending comma and de remain readable. The tall f and following stems support foncteur, with its final s unresolved. The raised cohomologique has a long terminal curve that may include s. The contiguous cancellation and replacement are one change site, with the three sub-doubts retained. H marks the cancelled material, but not its raised cohomologiques ending, as uncertain.'
diffs[8]['evidence']='Root selects A/C’s uncertainty against B’s resolved la. This occurrence has a tall l and a compressed low loop with a rightward exit resembling e; a remains possible. It was assessed independently of L5.'
diffs[9]['evidence']='Extra older struc-like strokes overlap the live beginning, while ture is clearer. The older word fragment and detailed chronology cannot be completely separated. H mentions overloading in a note but omits the old layer from its main text; this is an omission, not old text given live.'
diffs[10]['evidence']='The dedicated main crop shows no separate point after the terminal exit of etc. The following dash belongs to the next baseline.'
diffs[12]['evidence']='The dedicated main crop shows Une beginning at the ordinary left edge, slightly left of the preceding opening dash, with ordinary baseline spacing. All three complete half readings also report the preceding line filled to the right. Root retains continuous prose rather than H’s paragraph break.'
diffs[13]['evidence']='The full raised phrase reads sous catégorie de la catégorie dérivée des. There is a gap, without a hyphen, between sous and catégorie. Its long lower guide attaches it after la and before complexes; it is not an underline or part of the word. No X occurs in this addition.'
diffs[14].update(final=r'\unsure{formee|forme|formée|form-}',evidence='Root prefers C’s accentless formee: after m there are two small low e-like elements, the last detached. A’s single-e forme remains possible if the first small element is the m exit. No independent acute is secure beneath the nearby guide, so formée remains an alternative rather than a supplied accent. The earlier form- alternative is retained; there is no separate s body supporting formés. The malformed ending is not repaired from syntax.')
diffs[15]['evidence']='A low a oval, following u and crossing x identify aux, without the tall d required by H’s des. The complete raised phrase is aux complexes de; its separate lower guide returns before faisceaux.'
diffs[18]['evidence']='Root selects B/C’s resolved triangulé against A’s retained second-e alternative. The l has a straight low foot, followed by one separate open e with its rising acute. There is no second e body. The stroke below the middle is the g descender, not an underline; the faint line above is background texture.'
diffs[19].update(final=r'\deleted{\unsure{m|sou|de}}multiplicative',evidence='Root selects A/C’s m-first reading against B’s sou-first order. Pointed humps and low crossed loops precede the clear ulti; no secure d body is isolated. The older m-like group merges with the live initial m. Sou and de remain alternatives, and the exact old/live sequence remains doubtful.')
diffs[21].update(final='donnant',differs_H=True,confidence='high',evidence='Root selects A/B’s resolved donnant against C’s donnant/donnait uncertainty. The low segment after a has the extended n movement seen in the earlier nn run, followed by t. There is no independent i body or dot. The visible run supports n; the merely conceivable undotted-i alternative is not retained. H’s uncertainty is therefore resolved, and C’s donnait changes.')
diffs[22].update(final='short bent, two-lobed stroke below si, drawn in TikZ',evidence='The small separated dark stroke near (241,1836) has a slight kink and lower lobe/foot, not a perfectly straight vertical. Root preserves that bent shape, without assigning it a word, punctuation function, or hand.')
diffs[26]['evidence']='The dedicated main crop includes both boundaries: two short elevated strokes open linéarisation and two close it. Neither boundary forms angular guillemets.'
diffs[28]['evidence']='The two ruled segments lie on one level: approximately (318,2273)–(556,2261) and (581,2262)–(673,2264). The first stops before l; the second starts under its terminal horizontal extent and continues under ien. Root selects C’s split underline plus small partial-l overlay. A’s continuous underline with a comment would fill the physical gap; B’s split at whole-letter boundaries omits the small partial-l span. No intended semantic emphasis is inferred.'
diffs[29].update(final=r'\unsure{sans|sa|san}',differs_C=False,differs_H=True,confidence='medium',evidence='Root retains A/B’s doubt against C’s resolved sans. The a oval has a long low extension ending in a short upward/downward shoulder, favouring compressed ns, but n and s cannot be separately assigned. B’s san alternative is also supported by a final n shoulder. The unchanged preferred sans is already doubtful in C; adding san alone is not counted as a new C change.')
diffs[30]['evidence']='Root retains A/C’s structures/structure uncertainty against B’s resolution. The low e-like terminal sequence has a long exit and final downward curl, favouring s, but the e exit and s are not separately recoverable.'
diffs[31]['evidence']='Root retains A/C’s plural-first uncertainty against B’s resolved supplémentaires. The terminal re-like group runs into a downward curl that may be s or a singular ending stroke. The medial accent is present, but neither agreement with structures nor an editorial translation settles the ending.'
diffs[33].update(final=r'\unsure{\inserted{\unsure{sur} $X$}}',evidence='The raised group has a heavily retraced sur-like word followed by a securely crossed X. A curved guide descends to the gap before pour. No independent straight cancellation stroke can be separated from the dense word/X strokes, so a live insertion is preferred; cancellation or an older superposed layer remains possible. Root retains A/C’s state doubt, while adopting B’s distinction between the uncertain word and the clear X. The inner doubt marks sur; the outer doubt marks the insertion state. This refines C’s already doubtful preferred addition without changing its preferred content or state.',confidence='medium')

comparisons=[
 {'place':'L4 module ending','A':'module|modules','B':'module|modules','C':'modules|module','decision':diffs[3]['evidence']},
 {'place':'L5 separator','A':'comma plus a detached upper point; joint role open','B':'plain comma','C':'semicolon|comma, with both physical components recorded','decision':diffs[4]['evidence']},
 {'place':'L5 article','A':'le|la','B':'la|le','C':'le|la','decision':diffs[5]['evidence']},
 {'place':'L7 article','A':'le|la','B':'la resolved','C':'le|la','decision':diffs[8]['evidence']},
 {'place':'L10 form ending','A':'forme|formée|formés|form-','B':'form-|formée|formés','C':'formee|formée|form-','decision':diffs[14]['evidence']},
 {'place':'L12 triangulé','A':'triangulé|triangulée','B':'triangulé resolved','C':'triangulé resolved','decision':diffs[18]['evidence']},
 {'place':'L13 older fragment','A':'m|sou|de','B':'sou|de|m','C':'m|de|sou','decision':diffs[19]['evidence']},
 {'place':'L14 donnant','A':'donnant resolved','B':'donnant resolved','C':'donnant|donnait','decision':diffs[21]['evidence']},
 {'place':'L17 and L23 detached spots','A':'omits the two spots at ils/permettent and the point by constants','B':'retains the two spots at ils/permettent; omits the point by constants','C':'retains all three sites','decision':'Root preserves all three physically separate compact marks from C/18_ils_marks.png and C/24_supplementaires.png. Their positions are clear, but colour, hand and semantic role remain unassigned.'},
 {'place':'L21 underline gap','A':'continuous uline plus comment on gap','B':'split non abé / l / ien','C':'split non abé / partial-l rule / ien','decision':diffs[28]['evidence']},
 {'place':'L22 sans','A':'sans|sa','B':'sans|sa|san','C':'sans resolved','decision':diffs[29]['evidence']},
 {'place':'L22 structures','A':'structures|structure','B':'structures resolved','C':'structures|structure','decision':diffs[30]['evidence']},
 {'place':'L22 supplémentaires','A':'supplémentaires|supplémentaire','B':'supplémentaires resolved','C':'supplémentaires|supplémentaire','decision':diffs[31]['evidence']},
 {'place':'L23 sur X and its state','A':'whole phrase doubtful, preferred live insertion; state open','B':'sur doubtful, X clear, live insertion','C':'whole phrase doubtful, preferred live insertion; cancellation alternative','decision':diffs[33]['evidence']},
 {'place':'L6 contiguous cancellation and replacement; H metadata','A':'separate rows for old phrase and replacement','B':'one grouped site','C':'one grouped site; H doubt scope explicit','decision':'One contiguous change row preserves every sub-doubt. H marks the illegible/cancelled material, not the raised cohomologiques. The scope is recorded explicitly rather than treating every component as already doubtful in H.'}
]

unresolved=[]
umap={0:2,1:3,2:4,3:5,4:6,5:7,6:7,7:7,8:8,9:9,10:14,11:19,13:30,14:31}
for i,j in umap.items():
 u=copy.deepcopy(r['C']['unresolved'][i]);u['crop']=diffs[j]['crop']
 if i==1:u.update(reading='module',alternatives=['modules'],reason=diffs[3]['evidence'])
 if i==10:u.update(alternatives=['forme','formée','form-'],reason=diffs[14]['evidence'])
 if i==11:u.update(alternatives=['sou','de'],reason=diffs[19]['evidence'])
 unresolved.append(u)
unresolved.insert(12,{'place':'L22 sans','reading':'sans','alternatives':['sa','san'],'confidence':'medium','reason':diffs[29]['evidence'],'crop':diffs[29]['crop']})
unresolved.extend([
 {'place':'L23 raised word before X','reading':'sur','alternatives':[],'confidence':'medium','reason':'The word is strongly retraced and its letter contours cannot all be separated; the following X is clear.','crop':diffs[33]['crop']},
 {'place':'L23 state of raised sur X','reading':'live insertion after constants, before pour','alternatives':['same letters cancelled or bearing an older superposed layer'],'confidence':'medium','reason':'The curved guide favours attachment, but heavy overlapping ink leaves chronology/cancellation uncertain. The outer uncertainty wrapper marks this state doubt.','crop':diffs[33]['crop']}
])

qmap={1:[0],2:[3],3:[2],4:[7],5:[7],6:[9],7:[14],8:[18],9:[19],10:[29],11:[30],12:[32],13:[33],14:[1,2,3,4],15:[13,14,15,16,17,18],16:[20],17:[28,29,30,31,32,33,34]}
review=[]
for i,q in enumerate(r['C']['C_doubt_review'],1):
 js=qmap[i];final=q['final_reading'];status=q['decision']
 if i in [1,2,3,6,7,8,9,10,11,12,13]:final=diffs[js[0]]['final']
 if i==10:status='retained'
 if i==14:final=r'des catégories; coeff.; constant|constants tordus = π₁-module|modules; H^i(-[;|,]M); formelles.'
 if i==17:final=r'(n+1)-catégorie (sans|sa|san structures|structure supplémentaires|supplémentaire dessus!) des n-champs loc. constants; sur uncertain, X clear; insertion state uncertain; pour tout n'
 ev=' '.join(diffs[j]['evidence'] for j in js)
 if i==14:ev+=' The three complete half readings agree on coeff., the unbracketed equality and only a full stop after formelles, with no question mark or closing parenthesis.'
 if i==15:ev+=' The two additions are distinct and the only X in this passage is the one after sur on the ordinary baseline; no intermediate X is supplied.'
 if i==16:ev+=' Root also inspected A/l14_rhom.png: the R has doubled uprights with a bowl/leg, Hom has no underline, and the following ellipsis and parenthesis are separate. All three half readings confirm en effet is the complete local addition and that no editorial footnote is present.'
 if i==17:ev+=' All three complete half readings agree on the n/plus/1 forms, the parenthesis and exclamation, n-champs loc. constants and the complete final n. No constructible-sheaf phrase is supplied.'
 ev+=' Main inspected '+', '.join(dict.fromkeys(diffs[j]['crop'] for j in js))+'.'
 review.append({'place':q['supplied_question'],'earlier':q['supplied_question'],'decision':status+': '+final,'evidence':ev})
for q in r['C']['notes']['earlier_note_review']:
 review.append({'place':'Earlier C note: '+q['topic'],'earlier':q['topic'],'decision':q['review'],'evidence':'All three complete current-page readings reviewed this topic; other-page wording was not imported as image evidence.'})
for q in r['C']['notes']['H_editorial_claims']:
 answer=q['review']
 if q['claim'].startswith('donnant'):answer='Root resolves donnant from the low n movement; the proposed grammatical donne is not substituted.'
 if q['claim'].startswith('The final raised'):answer='Sur remains doubtful, X is clear, and the live insertion is preferred with cancellation/overwriting retained as a separate state uncertainty.'
 review.append({'place':'H editorial note: '+q['claim'],'earlier':q['claim'],'decision':answer,'evidence':'The current-page half reports and the separately recorded main crops control the transcription. H editorial translations or external references were not consulted as sources.'})

inv=copy.deepcopy(r['C']['inventory'])
inv=[inv[i] for i in [0,2,4,3,5,12,6,7,8,13,15,16,14,9,17,10,18,11,1]]
for x in inv:
 if x['element']=='old group by multiplicative':x['first_words_or_objects']='m/sou/de (uncertain)'
 if x['element']=='short stroke below si':x['first_words_or_objects']='short bent upright with two lobes and a small foot'
 if x['element']=='raised final phrase':x['first_words_or_objects']='sur (uncertain) X (clear); insertion state uncertain'

notes=r'''**S183-notes.** The page continues the previous page’s qualification with **“dans cette première approche pré-catégorie dérivée”**. It lists the fundamental group π₁, categories of twisted coefficients, the cohomology functors Hⁱ with their exact-sequence structure, and cup-product structure, related by formal properties. The awkward endings, the word relatif and the unbracketed equality before π₁-module(s) are preserved; they are not repaired by category agreement. Des catégories is visibly plural and contains no separate la.

With the language of derived categories, the writer proposes a candidate involving complexes of abelian sheaves with locally constant cohomology, a triangulated structure and a multiplicative derived tensor structure, possibly also derived Hom. The two guided additions are independently placed: **“sous catégorie de la catégorie dérivée des”** between la and complexes, and **“aux complexes de”** before faisceaux. The malformed formee/forme/formée/form- ending remains doubtful. Triangulé has exactly one final accented e; constante and the unpointed loc are kept literally. The verb is resolved as donnant from its n strokes, without replacing it by a grammatically smoother form.

The source says **“Je n’ai guère d’idée si oui ou non ils permettent de le récupérer”**, with the raised **“en effet”** attached before the comma. It then says **“mais par contre n’ai guère de doute”** concerning going to the end of the quoted linéarisation, passing into the nonabelian setting and working with an (n+1)-category of locally constant n-champs for every n. This is the author’s stated uncertainty and confidence, not a theorem established here. No je is supplied before n’ai guère in the latter clause, and H’s passant is replaced by the visible partant.

Mathematical notation prompted careful inspection of the degree and separator in Hⁱ, the L above tensor, R beside Hom, and the n+1 parenthesis. The H separator has a separate high point and lower comma-shaped stroke: semicolon is preferred, with comma plus an unassigned detached point as alternative. The upper point is not erased to match expected notation. The L has doubled stems and a common foot; the R has doubled uprights and a bowl/leg. Hom is not underlined. A separate point below tensor is reproduced without becoming an index or operator. These are visual decisions, not proof checks; all three reader check_events arrays are empty and no proof, re-proof, computation or mathematical verification was performed.

The underline beneath non abélien consists of two strokes separated mainly beneath l. Its second segment begins under the end of that letter and continues under ien; the small partial-letter span is drawn without filling the gap. The uncertain sans/sa/san, structures/structure and supplémentaires/supplémentaire endings remain doubtful, while dessus and its exclamation are resolved. At the foot the word sur is heavily retraced but the following X is clear. A curved attachment supports a live insertion after constants and before pour, with cancellation or an older layer still possible. Separate uncertainty wrappers distinguish the word from the insertion state. No constructible-sheaf wording or editorial footnote is imported.

Seven sites of separate nontext marks are preserved: the point below the opening dash; the point below tensor; the bent stroke below si; the two separate spots beside ils and permettent; the diagonal pair of points below the beginning of contre; and the point above/right of constants. Their physical presence and positions are distinguished from unknown origin, hand or function. Colour alone does not establish manuscript origin. Pale diffuse reproduction texture is not promoted to writing.

This is one continuous prose block with 23 main baselines, five raised additions, three cancelled/overwritten sites and one interrupted underline. There is no independent display, mathematical diagram, verbal margin note, date, heading, closing or signature. Author page **38** and archive pencil **183** are separate entries. All 17 supplied C questions and the earlier C/H note topics were reviewed. External versions and other-page quotations were not used to determine this page’s ink.
'''

text=(ROOT/'records/scan183/C/reading.tex').read_text()
text=text.replace(r'\unsure{modules|module}',r'\unsure{module|modules}')
text=text.replace(r'\unsure{formee|formée|form-}',r'\unsure{formee|forme|formée|form-}')
text=text.replace(r'\unsure{m|de|sou}',r'\unsure{m|sou|de}')
text=text.replace(r'\unsure{donnant|donnait}','donnant')
text=text.replace(r'(sans \unsure{structures|structure}',r'(\unsure{sans|sa|san} \unsure{structures|structure}')
text=text.replace(r'(-0.45,-0.80) -- (-0.40,-0.97);',r'(-0.45,-0.80) -- (-0.42,-0.87) -- (-0.45,-0.90) -- (-0.40,-0.97) -- (-0.37,-0.96);')
text=text.replace('% L23: preferred live raised addition, with curved attachment before pour; cancellation remains a state alternative.', '% L23: inner doubt concerns sur, not the clear X. The outer doubt concerns the insertion state.\n% A curved guide attaches before pour; cancellation/older superposed ink remains a state alternative.')
text=text.replace(r'\inserted{\unsure{sur $X$}}',r'\unsure{\inserted{\unsure{sur} $X$}}')
viewed=(ROOT/'records/scan183/main_viewed_crops.txt').read_text().splitlines()
d=write_decision(183,'C',[],diffs,comparisons,unresolved,inv,notes,r['C']['abbreviations'],review,viewed,brief='briefs/brief_v14_scan183.md',workflow_note='Three fresh independent readers each inspected whole/a/b once and completed all 23 baselines, five additions, all 17 supplied C questions and earlier-note topics. A made 31 crops, B 26, C 26; A’s final three distinct coverage crops are recorded in its return. Main fully read all fields and each complete reading.tex before image adjudication. Main reused 28 saved reader crops and made three new crops for uncropped witness differences: etc punctuation, the paragraph boundary, and both linéarisation quotation boundaries. All 31 unique crops were successfully inspected. One attempted output of three images exceeded model context capacity; none was counted from that failed output, and each exact saved file was then displayed successfully without recropping. The failure and reuse are recorded in main_display_failures.json. All reader/witness differences were adjudicated, including the union of nontext marks, partial-letter underline, and separate word/state uncertainty at sur X. Static text checks only; no TeX engine, rendering, OCR, extraction or external research.',text_override=text)
by={c['path']:c.get('bbox') for rep in r.values() for c in rep['crops']}
for p in (ROOT/'crops/scan183/main').glob('*.json'):
 c=json.loads(p.read_text());by[str(p.with_suffix('.jpg').relative_to(ROOT))]=c['bbox']
for x in d['differences']:
 if x.get('crop') in by:
  if x.get('bbox')!=by[x['crop']]:x['reader_report_bbox']=x.get('bbox')
  x['bbox']=by[x['crop']]
d['main_successful_crop_inspections']=31
d['main_reused_crop_inspections']=28
d['main_failed_image_outputs']=1
d['main_failed_image_items']=3
(ROOT/'records/scan183/decision.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
add_notation([
 ('Derived L and R on scan 183',r'\mathbb{L}, \mathbb{R}\mathrm{Hom}','183 L13/L14: distinct doubled stems visible in root-inspected tensor and Hom crops; L above tensor, R on the Hom baseline, no Hom underline. Compare earlier forms individually in final review.'),
 ('Two-part H separator',r'\unsure{;|,}','183 L5: high point plus lower comma; semicolon preferred, comma-with-detached-point role alternative. Both physical components retained.'),
 ('Interrupted partial-letter underline',r'\uline{non abé}l [short partial-l rule] \uline{ien}','183 L21: physical gap mainly under l; same-level second segment begins under its terminal extent. Do not extend the rule through the gap.'),
 ('Local abbreviation stops','loc / loc.; etc','183 L11 loc has no point; foot loc. has one; L7 etc has none. Each occurrence read locally.'),
 ('Letter versus state uncertainty',r'\unsure{\inserted{\unsure{sur} $X$}}','183 L23: inner doubt is sur; X is clear; outer doubt records live-insertion versus cancellation/older-layer state.')
])
register_note_statements(183,[
 {'place':'L1–L8; notes paragraph 1','statement':'The page lists fundamental group, twisted coefficient categories, cohomology functors and cup-product information as the first pre-derived-category approach.'},
 {'place':'L9–L18; notes paragraphs 2–3','statement':'The author proposes derived-category data with triangulated and multiplicative structure, possibly derived Hom, but expressly does not know whether these recover the homotopy type.'},
 {'place':'L18–L23; notes paragraph 3','statement':'The author expresses greater confidence in continuing to the nonabelian setting using an (n+1)-category of locally constant n-champs for every n; the sentence continues.'}
])
