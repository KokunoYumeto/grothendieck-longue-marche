from adjudication import *
n=33;rr=reports(n);a=[differences(d) for d in rr]
t=(O/'documentation/main_033_proposal.tex').read_text().replace('% Provisional main reading; all revisions remain subject to independent-reader comparison.','% Adjudicated after three independent full readings and focused supplements.')
m2={1:1,2:3,3:4,4:5,5:6,6:7,7:10,8:11,9:12,10:42,11:14,12:15,13:16,14:17,15:18,16:19,17:20,18:21,19:22,20:23,21:24,22:25,23:28,24:29,25:31,26:26,27:33,28:34,29:35,30:36,31:37,33:38,34:39,36:41,37:13}
r3={1:r'\deleted{\unsure{R|P|Or}}',2:'F',3:r'\unsure{va|voir}',4:r'\unsure{se|sa|une}',5:r'\unsure{simplifier|simplification}',6:'cf plus bas; rule drawn',7:r'\deleted{\unsure{\prime|\ast|?}}',8:r'\deleted{\unsure{\prime|\ast|?}}',9:'bracket drawn',10:'F; clipped close parenthesis uncertain',11:r'd’où A\in F',12:r'\deleted{\unsure{On a|Or}}',13:r'\deleted{et}',14:r'\inserted{il suffirait F′\ll F}',15:r'\deleted{)}',16:r'et \unsure{\uline{bien}|\deleted{bien}}',17:r'\deleted{\unsure{F|\in|\exists}}',18:r'\unsure{on a}',19:r'\deleted{\unsure{F|A}}A′',20:'opening before d’où; old close cancelled; qed inside later close',21:'Sinon on aurait',22:'pale left arrow-like trace drawn; function uncertain',23:'ouverte; underline includes F′',24:r'\deleted{dans \unsure{la}} de',25:r'\deleted{de}',26:'upper insertion and leader drawn within cancellation',27:'comma',28:r'I^{\unsure{\ast|k|+}}',29:r'\deleted{\unsure{\times|\setminus}}',30:r'\unsure{\setminus}',31:r'I′^{\ast}',32:'I',33:r'\deleted{\unsure{A|\Delta}}',34:'ens without point; no second outer close',35:'32.',36:'C relations except separately noted loci',37:r'A′\unsure{\in|=}A; earlier membership overwritten toward equality possible'}
cr={1:'first_cancel',2:'top',3:'margin',4:'margin',5:'margin',6:'margin',7:'boxed',8:'boxed',9:'boxed',10:'boxed',11:'upper',12:'upper',13:'et_wide',14:'insert',15:'insert',16:'after_lemma',17:'deleted_sign',18:'on_a',19:'revised_A_full',20:'lower',21:'si_verb_full',22:'faint_mark',23:'cancel',24:'cancel_local',25:'cancel',26:'cancel',27:'foot',28:'I_marks',29:'I_marks',30:'I_marks',31:'I_marks',32:'last_I',33:'last_I',34:'foot',35:'top',36:'middle',37:'equality_rewrite'}
kinds={1:'misread word',2:'other',3:'other',4:'other',5:'other',6:'readable ink left as `\\ill{}`',7:'omission',8:'omission',9:'drawing or diagram',10:'other',11:'misread symbol or index',12:'misread word',13:'other',14:'misread word',15:'omission',16:'misread word',17:'misread symbol or index',18:'other',19:'omission',20:'insertion or placement',21:'misread word',22:'drawing or diagram',23:'readable ink left as `\\ill{}`',24:'omission',25:'omission',26:'other',27:'other',28:'misread symbol or index',29:'omission',30:'other',31:'misread symbol or index',32:'other',33:'omission',34:'other',35:'omission',36:'other',37:'misread symbol or index'}
rows=[]
for i,x in enumerate(a[0][:37],1):
    rd2=reading(a[1][m2[i]-1]) if i in m2 else {32:'I',35:'32.'}[i]
    y=row(n,i,x,[reading(x),rd2,r3[i]],f'crops/root/033_{cr[i]}.png',kind=kinds[i])
    if i==1:
        y.update(final=r'\deleted{\unsure{R|P|Or}}',against_C=True,against_H=True)
        y['ink']='The initial upright and loop are heavily crossed. Main retains R/P and the less favoured Or possibility because the former lower strokes cannot be isolated; the rightward arrow-like extension is separately drawn and logged. R2 does not include Or; R1/R3 do.'
    if i==2:
        y.update(final='F',confidence='medium',against_C=True,against_H=False)
        y['ink']='A stem and two rightward arms match the ordinary F forms in the same first argument. R2 retains alphabet uncertainty; main with R1/R3 reads plain F, without using the set-family meaning to choose an alphabet.'
    if i in (3,4,5):
        y['against_H']=False
        y['ink']+=' R3 retains alternatives. Main resolves this word from the rotated enlarged strokes, agreeing with R1/R2; H already has the same preferred word under a shared uncertainty mark.'
    if i==6:
        y.update(place='vertical margin, final word',C='cf plus bas',H=r'cf plus \ill{}',final='cf plus bas',against_C=False,against_H=True)
        y['ink']='The rotated last word has the tall b entry and reduced as continuation; bas is readable. All three readers agree. The independent long rule is logged separately.'
    if i==9:y.update(against_C=False,final='long lower bracket with both upturned ends, drawn in TikZ');y['ink']+=' C already records the same shape using a lower line and end rules; changing its drawing mechanism is not counted as a reading correction against C.'
    if i==10:
        y.update(final=r'\unsure{\circ(F)}',against_C=True,against_H=False,confidence='low')
        y['ink']='The small ring and opening parenthesis are visible and F begins at the cropped paper edge. The closing/completion is not fully visible. Main marks the whole edge ending uncertain, without adding a prime; R1 doubts the ending, R3 doubts the closing parenthesis, and R2 retains the conventional completed form while noting the tight edge.'
    if i==12:
        y.update(final=r'\deleted{On a}',confidence='medium')
        y['ink']+=' Main compared the separated round entry and low terminal group with the earlier crossed On a in the same paragraph. R3 retains Or as an alternative; the same-hand comparison supports On a.'
    if i==13:
        y.update(final=r'\deleted{et}',against_C=True,against_H=False,confidence='high')
        y['ink']='The dedicated wider crop isolates an e loop and a tall crossed t beneath the diagonal cancellation. Main/R2/R3 resolve et; R1 retains the earlier doubt.'
    if i==16:
        y.update(final=r'et \unsure{\uline{bien}|\deleted{bien}}',against_C=True,against_H=True,confidence='medium')
        y['ink']='The short et and b-initial dotted word bien are visible. The additional low horizontal stroke is below the middle letters in places but meets their baseline elsewhere. R1/R3 favour an underline, R2 favours cancellation with a reservation. Main puts underline first and preserves cancellation as an explicit state alternative; H’s longer d’autre part is unsupported.'
    if i==17:
        y.update(final=r'\deleted{\unsure{F|\in|\exists}}',against_C=True,against_H=True)
        y['ink']+=' R2 does not find a secure right upright for an existential sign; main retains it only as a lower-ranked alternative because the dense crossing also obscures that edge.'
    if i==18:y['ink']='The isolated 5× crop shows only light initial remnants, a long low join and a tiny final group. All three readers and main retain on a as uncertain. Main’s initial provisional resolution was withdrawn after this isolated view; grammar does not settle the missing contours.'
    if i==21:
        y['confidence']='medium';y['ink']+=' Main compared the compressed non run with the earlier sinon on in this page (033_sinon_compare); the extra group is not discarded as in H.'
    if i==23:
        y.update(C='ouverte',H=r'\ill{}',final='ouverte',against_C=False,against_H=True)
        y['ink']='The o/u entrance, v/er run and final t/e can be followed between the diagonal strokes. All readers recover ouverte. Underline extent is separately adjudicated; this row does not adopt R1’s longer extent.'
    if i==26:
        y.update(final='complete raised On suppose b) i.e. φ induit ... statement, inserted and cancelled with the draft',against_C=False,against_H=False,review_type='insertion-state review')
        y['ink']+=' H’s explanatory note already records this complete wording, location and shared cancellation; its different macro arrangement alone is not counted as a textual difference.'
    if i==28:
        y.update(final=r'I^{\unsure{k|\ast|+}}',against_C=True,against_H=True,confidence='medium')
        y['ink']='The raised mark has a near-upright stem and two rightward branches. Main/R1 put k first on that shape; R2/R3 prefer a stylized asterisk. The asterisk and cross alternatives remain explicit. The same uncertainty is repeated at the second occurrence.'
    if i==30:y.update(against_C=False,against_H=False)
    if i==31:
        y.update(final=r'I′^{\unsure{k|\ast|+}}',against_C=True,against_H=True,confidence='medium')
        y['ink']='The second raised fork has the same stem and right branches as the first. R1 prints k while saying its first-occurrence uncertainty governs this occurrence; R2 explicitly repeats uncertainty; R3/C/H print a star. Main repeats all alternatives here so no uncertainty is merely implicit.'
    if i==32:
        y.update(final=r'\unsure{I|\vec I}',against_C=True,against_H=False,confidence='low')
        y['ink']='The upper serif of I ends in a thick downturned hook, with a faint oblique trace above it. R2/R3 keep plain I; R1 and main retain a possible arrow decoration. Plain I remains first, because the thin upper trace may be a retraced serif rather than an independent vector arrow.'
    if i==33:
        y.update(final=r'\deleted{\unsure{A|\Delta}}',against_C=False,against_H=True,confidence='low')
        y['ink']='The apex, two oblique sides and strong transverse stroke survive a diagonal crossing. R1 resolves A from a raised crossbar. Main with R2/R3 retains A/Delta because the transverse stroke is entangled with the cancellation and its original height is not independently secure.'
    if i==34:
        y.update(place='foot, abbreviation before d’indices',C='ens',H='ens.',final='ens',against_C=False,against_H=True)
        y['ink']='The low terminal s movement is followed directly by the next word; no separate point is visible. The outer parenthesis is logged at its own locus.'
    if i==35:y['crop']='Main enlargement crops/root/033_number.png; recipes in documentation/crops.jsonl.'
    if i==36:
        y.update(final='all C mathematical relations except the separately adjudicated overwritten equality and forked raised marks',review_type='C notation review')
        y['ink']='Individually checked the two initial inclusions, every membership and nonmembership sign, support bars, G≤F and G′≤F′, F^{A′}, all circle/F/F′ placements, baseline preceq versus inserted double-less-than, the tilde over the rightward map, and b⇔c. The relation after prouvons que is excluded here and treated separately. Reading these signs is not a proof of their claims.'
    if i==37:
        y.update(final=r"A'\unsure{\deleted{\unsure{\in|\subset}}=|\in}A",against_C=True,against_H=True,confidence='medium')
        y['ink']='Main’s isolated 5× crop shows two very thick horizontal bars, a thinner curved cap/left connector and a short middle bar in the gap. R1/R2 prefer an earlier membership-shaped relation overwritten by =; R3 allows membership as the final sign. Main puts the overwritten membership/subset followed by equality interpretation first but preserves a live membership alternative. Neither the desired equality conclusion nor a majority vote removes the surviving-state doubt.'
        y['consequential']='The heavily retraced A′–A relation is not flattened to a certain equals sign: the earlier membership/subset layer and a possible live membership reading are preserved.'
    rows.append(y)

def add(i,place,C,H,reads,final,ink,crop,kind='other',c=False,h=False,confidence='high',marked='no',review=None):
    x=dict(id=f'033-{i:02}',place=place,C=C,H=H,readers=reads,final=final,ink=ink,crop='Main enlargement crops/root/033_'+crop+'.png; recipes in documentation/crops.jsonl.',kind=kind,against_C=c,against_H=h,confidence=confidence,marked_in_H=marked)
    if review:x['review_type']=review
    rows.append(x)

add(38,'long line beside vertical note','note only; no full line drawing','editorial description of long rule',['long rule drawn']*3,'long thin curved separator drawn beside the full margin note','The line extends from beside the first argument to just above the abandoned draft and stays between note and body. H describes it but does not draw it.','margin','drawing or diagram',True,True)
add(39,'foot, outer parenthesis after I′(=F′)','no outer close','extra outer close after I′(=F′)',['no outer close']*3,'outer parenthesis left open on this page','Only the close of (=F′) and a point precede On a; the earlier opening before parties has no second matching close in the ink.','foot',h=True)
add(40,'2°), after first inclusion before Soit','no point','point',['no point']*3,'no point','The space after G and before Soit has no separate punctuation mark.','upper',h=True)
add(41,'initial cancellation, rightward extension','omitted distinct graphic','omitted distinct graphic',['arrow-like tail included as a candidate implication sign','arrow-like strokes drawn separately','no separate drawing in initial proposal'],'arrow-like extension drawn, with no assigned function','Two low roughly parallel lines extend rightward from the cancelled initial and meet an angled terminal. Their shape is retained without deciding whether they were an implication or part of the cancellation.','first_cancel','drawing or diagram',True,True,'medium')
add(42,'leader under il suffirait insertion','insertion words, no leader path','insertion words, no leader path',['attachment described, not drawn in TEX','attachment described, not drawn in TEX','leader drawn'],'curved attachment between raised note and old closing parenthesis','The thin line leaves the crossed parenthesis region, runs beneath the raised words and turns upward at the right. It is independent of the preceq sign.','insert','drawing or diagram',True,True)
add(43,'leader beneath On suppose insertion','no leader path','description of interline; no leader path',['leader recognized, not drawn','leader recognized, not drawn','leader drawn'],'long curved insertion leader drawn with the full words','Its left curve approaches Soit and continues below the entire added map statement to an upturned right end.','cancel','drawing or diagram',True,True)
add(44,'before Soit in cancelled draft','no lexical parenthesis','literal opening parenthesis',['no lexical parenthesis']*3,'no lexical opening parenthesis','The apparent opening curve is continuous with the long insertion leader; it is not a separate parenthesis character.','cancel','text not on the page',False,True)
add(45,'underline in abandoned draft','extends through F′','no underline',['extends through F′','ends before F′','extends through F′'],'underline ends after revised de and before F′','The line starts beneath strate but its right tip stops visibly to the left of F′. Main agrees with R2 from the enlarged whole line and limits the underline to the visible extent.','cancel','drawing or diagram',True,True)
add(46,'final Prouvons line below crossed draft','certainly deleted with block','certainly deleted with block',['deleted with block','deleted, with uncertainty only in comment','explicit live/deleted alternatives'],r'\unsure{\deleted{Prouvons $A′^{\circ(F′)}=A^{\circ(F)}$.}}','All five diagonal strokes end above this baseline. Its association with the abandoned argument may imply cancellation, but there is no direct crossing stroke on its words/formula. Main retains the complete line under an uncertain deletion marking, as a state doubt only.','cancel','deletion state (struck given live or live given struck)',True,True,'medium')
add(47,'large strokes through abandoned draft','global deleted macro only','five diagonals described in note',['deletion macro; no paths','deletion macro; no paths','five actual paths drawn'],'five oblique cancellation strokes drawn with the full draft','The parallel strokes rise rightward, crossing the upper insertion and three main baselines. Their lower endpoints leave the final Prouvons line uncrossed.','cancel','drawing or diagram',True,True)
add(48,'two faint stroke clusters right of margin rule','omitted','omitted',['see appended independent supplement','see appended independent supplement','two clusters drawn'],'two pale nonalphabetic clusters drawn without lexical assignment','Main’s 6× crop shows an upper rising oblique, a short bent stroke below it, and a lower broken rising oblique. They lie between the long rule and Je dis, separate from the dark body text. Their function and hand remain uncertain.','margin_traces','drawing or diagram',True,True,'medium')
rows[-1]['readers']=[reading(a[0][37]),reading(a[1][43]),reading(a[2][8])]
add(49,'foot, punctuation after I','I,','I followed directly by parenthesis',['comma','comma','comma'],'I, before the cancelled A/Delta','The detached low descending stroke after I is a comma, separate from both the cancelled triangular glyph and the subsequent opening parenthesis. H omits this comma.','last_I',h=True,confidence='medium')
rows[45]['against_H']=False
rows[45]['ink']+=' H shares the preferred paragraph-deletion interpretation; the new uncertainty alone is not counted as a demonstrated H error.'

inv=json.loads((O/'documentation/main_033_inventory.json').read_text())
inv[28]['hand']='unidentified hand (pale mark; attribution uncertain)'
inv.append(dict(element='033-E43',kind='drawing',position='right of left margin rule beside Je dis',first_words_or_objects='two pale stroke clusters; no secure lexical value',sheet_kind='text',hand='unidentified hand (pale marks; attribution uncertain)'))
inv.append(dict(element='033-E44',kind='deletion',position='relation between A′ and A after prouvons que',first_words_or_objects='possible earlier membership/subset under equality; final-state uncertainty retained',sheet_kind='text',hand='his hand'))
notes=(O/'documentation/main_033_notes.txt').read_text()
now=datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds').replace('+00:00','Z')
who='GPT-6 Astra Pro; main; inherited effort not separately exposed; SP34 second pass'
extra=[dict(statement_id='TXT033-unprimed-parenthesis',date=now,who=who,type='targeted proof check',outcome='Conditional equality substitution checked: A∈F and A′=A imply A′∈F. The ink nevertheless reads unprimed A in the d’où parenthesis, and the preceding overwritten relation remains uncertain; neither is repaired.'),dict(statement_id='M033-strata-inclusion',date=now,who=who,type='targeted proof check',outcome='Under explicit nonemptiness and pairwise-disjointness hypotheses for distinctly labelled strata, inclusion of S(A′) in S(A) forces A′=A: choose a point of S(A′), then use disjointness. This does not establish those hypotheses or the earlier common-cell stratum equality.'),dict(statement_id='M033-later-lemma',date=now,who=who,type='carried as background without fault found',outcome='The manuscript’s sufficiency claim under F′≪F and later-lemma reference were read as claims, not proved. No later page was opened for this check.'),dict(statement_id='M033-open-indices',date=now,who=who,type='carried as background without fault found',outcome='The b⇔c heading and open-index-set descriptions were transcribed; no independent proof of their equivalence was performed here.')]
notation=[dict(sign='worked relation A′ ... A',form=r"\unsure{\deleted{\unsure{\in|\subset}}=|\in}",evidence='033_equality_rewrite; two thick bars plus thin curved connector and middle remnant',ambiguity='Likely earlier membership/subset overwritten by =; a live membership sign remains possible. This is not resolved from the desired proof.'),dict(sign='forked raised index marks',form=r'I^{\unsure{k|\ast|+}}, I′^{\unsure{k|\ast|+}}',evidence='033_I_marks, separately inspected at both positions',ambiguity='Main/R1 favour k-like shape; R2/R3 favour stylized star. Uncertainty is repeated at both occurrences.'),dict(sign='I after ordonnés',form=r'\unsure{I|\vec I}',evidence='033_last_I, top serif with hooked end and faint upper trace',ambiguity='Plain I first; independent arrow decoration not secure.'),dict(sign='preceq and double-less-than',form='F′ preceq F on baseline; F′≪F in insertion',evidence='033_middle and 033_insert',ambiguity='Distinct signs retained; no normalization between them.'),dict(sign='clipped right edge',form=r'\unsure{\circ(F)}',evidence='033_boxed; final parenthesized ending meets black edge',ambiguity='Completion is not fully visible; no prime is supplied.')]
save(n,t,rows,inv,notes,rr,notation,{'él.':'élément','ens':'ensembles','i.e.':'id est','cf':'confer','qed':'quod erat demonstrandum'},'Whole page then both halves read by main and three independent readers. Every one of the seventeen C doubt occurrences reviewed, all C/H disagreements enlarged, vertical note rotated; dense revisions, graphical paths, clipped edge and faint annotations checked. All reader dissent is recorded; no later page consulted before finalization.',extra_checks=extra)
