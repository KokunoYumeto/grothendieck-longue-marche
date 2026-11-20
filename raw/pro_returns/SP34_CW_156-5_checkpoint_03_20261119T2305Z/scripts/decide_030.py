from adjudication import *
n=30;rr=reports(n)
t=(O/'readers/R1/scan030.tex').read_text()
t=t.replace(r'\quad *',r'\quad{}^{*}')
t=t.replace(r'\unsure{déf.}',r'\unsure{def.|déf.}')
t=t.replace(r'\uline{explicitation}',r'\uline{\unsure{explication|explicitation|expliciter|explicitons}}')
t=t.replace(r'\unsure{G|L}',r'\unsure{L|G}')
t=t.replace(r'\unsure{dans|ds}',r'\unsure{ds|dans}')
t=t.replace(r'\unsure{\text{i.e.}}',r'\unsure{\text{bien}|\text{i.e.}}')
t=t.replace(r'\unsure{\text{où}|\omega}',r'\unsure{\text{Cor.}|\text{où}|\omega}')
t=t.replace('Vérifions quand même C7$_0$.','Vérifions quand même C7$_0$')
# These triples are explicit comparisons of the submitted page readings, not votes.
triples={
 1:[r'\uline{Proposition}']*3,
 2:["F'"]*3,
 3:['trivial']*3,
 4:[r'\unsure{déf.}',r'\unsure{déf.|def.}',r'\unsure{déf.}'],
 5:['résulte',r'\unsure{résulte}',r'\unsure{résulte}'],
 6:['en regardant supports']*3,
 7:[r'\uline{explicitation}',r'\unsure{explicitation|expliciter|explicitons}',r'\unsure{explication|explicitation|expliciter|explicitons}'],
 8:[r'\deleted{\unsure{or}}']*3,
 9:["Or F'.G"]*3,
 10:[r'\unsure{G|L}',r'\unsure{L|G}',r'\unsure{G|L}'],
 11:['le sens de A circle',r'le \unsure{sens} de A circle',r'le \unsure{sens} de A circle'],
 12:['p.r. à F','p.r. à F',r'\unsure{p.r.} à F'],
 13:[r'\unsure{dans|ds}',r'\unsure{ds|dans}',r'\unsure{dans|ds}'],
 14:['est le =']*3,
 15:[r'\deleted{(A\cap B\quad A,A\prime\in F,}']*3,
 16:['four rotated memberships above the four family labels']*3,
 17:['interlinear insertion under F.G with curved placement leader']*3,
 18:[r'\deleted{\unsure{i.e.}}',r'\deleted{\unsure{i.e.}}',r'\deleted{\unsure{bien|i.e.}}'],
 19:['Or on sait que (d’après...) que']*3,
 20:[r'\uline{Expliciter}']*3,
 21:['two-row G,F / F-prime order diagram']*3,
 22:[r'\underset{\unsure{\text{où}|\omega}}{\varphi}^{-1}(G)','not recorded in submitted page',r'\unsure{Cor.}'],
 23:['Un peu vif']*3,
 24:["on trouve par F'.G=G' un G' tel que"]*3,
 25:['square in tikz-cd','square reproduced with TikZ nodes','square in tikz-cd'],
 26:[r'encore l’\uline{unicité}']*3,
 27:['Cela amène à dégager']*3,
 28:['et','et',r'\unsure{et}'],
 29:[r'\unsure{\leq|<}']*3,
 30:['vertical and stepped bounding strokes in TikZ','vertical and stepped bounding strokes in TikZ','vertical and stepped bounding strokes in TikZ'],
 31:[r'\uline{Cor}.']*3,
 32:['valable']*3,
 33:['Vérifions quand même']*3,
 34:['C7 subscript 0 in main sentence']*3,
 35:['two-row G,F / G-prime diagram']*3,
 36:[r'\deleted{\unsure{(F.G)}}']*3,
 37:['réunion disjointe']*3,
 38:[r'\unsure{que|qui}',r'\unsure{qui|que}',r'\unsure{qui|que}'],
 39:[r'\deleted{raffine}',r'\deleted{\unsure{raffine}}',r'\deleted{raffine}'],
 40:[r'\inserted{subdivise}']*3,
 41:['F et c)']*3,
 42:['three distinct orders: ll, preceq, leq; all product primes and low dots retained']*3,
 43:["F'.G={A in F.G | A subset |F'|}"]*3,
 44:["G'={A' in F' | A' subset |G|}=phi inverse(G); phi:F' to F"]*3,
 45:['all live P,Q,R relations retained']*3,
}
rows=[]
for i,x in enumerate(differences(rr[0])[:45],1):
    cr='top' if i in (1,2,42) else 'topnotes' if i in (3,4,5,6) else 'star_word' if i==7 else 'star' if i==43 else 'edge_G' if i==10 else 'cancel_context' if i==15 else 'tiny_ie' if i==18 else 'extra' if i==22 else 'left_upright' if i in (20,21,44) else 'right' if 23<=i<=30 or i==45 else 'C7label' if i==34 else 'bottom_terms' if 36<=i<=41 else 'bottom' if 31<=i<=35 else 'proof3' if i==19 else 'proof2' if i in (16,17) else 'proof1'
    y=row(n,i,x,triples[i],f'crops/root/030_{cr}.png')
    if i==4:
        y.update(final=r'\unsure{def.|déf.}',against_C=True,against_H=True,confidence='low',kind='abbreviation expanded or spelling modernised',crop='crops/root/030_def_context.png; recipe in documentation/crops.jsonl.')
        y['ink']='The abbreviation has d/e loops, a tall f and a separate point. Main enlarged the whole area above e: no independent acute can be securely assigned. Unaccented def. is first; déf. remains possible. This is a spelling uncertainty, not an expansion.'
    if i==5:y['ink']+=' Main distinguishes the tall l/t and final e despite the retraced initial and resolves the word; R2/R3 retain doubt.'
    if i==7:
        y.update(final=r'\uline{\unsure{explication|explicitation|expliciter|explicitons}}',against_C=True,against_H=True,confidence='low')
        y['ink']='An i dot follows the tall l; after the c and low stroke there is a t-like form, another dotted i and a final on-like wave. No separate medial i between c and a can be confirmed. Thus explication (R3) is first; the compressed middle leaves the longer candidates possible. The descending stroke beneath the ending belongs to Prouvons below. The underline is definite.'
    if i==8:
        y['against_H']=True;y['kind']='other'
        y['ink']+=' The surviving initial is small; H capitalizes it. The separate live Or is counted at the next locus.'
    if i==10:
        y.update(final=r'\unsure{L|G}',against_C=True,against_H=True,kind='misread symbol or index',confidence='low')
        y['ink']='The surviving right-edge letter is an oblique upright turning into a rightward foot, visually L-like. G may have lost its right part at the image edge. Main therefore follows R2 in putting L first, without allowing the expected family G to decide the clipped ink.'
    if i==11:y['ink']+=' Main sees the low s/e/n/s sequence in the enlarged line, and resolves sens despite the two more cautious reader proposals.'
    if i==12:y['ink']+=' Main confirms the two separate abbreviation points, so does not expand the letters or retain H’s pris.'
    if i==13:
        y.update(final=r'\unsure{ds|dans}',against_C=True)
        y['ink']+=' Main sees no separable a/n in the short trace after d. The abbreviated candidate ds (R2) is first; dans is retained as an alternative.'
    if i==15:
        y.update(final=r'\deleted{$(A\cap B\qquad A,A\prime\in F,$}',against_C=True,against_H=True,kind='omission',confidence='high',consequential='The cancelled central setup ends A,A′∈F, unprimed; C’s apparent prime is the descender of que on the preceding line.')
        y['ink']='A contextual enlargement follows the supposed prime continuously into the q of que above. The F itself is unprimed. All three readers corrected their narrow-crop reading after independent contextual rechecks. The opening parenthesis omitted by H survives, and one long strike crosses both fragments, with heavier local retracing at A cap B.'
    if i==18:
        y.update(final=r'\deleted{\unsure{\text{bien}|\text{i.e.}}}',against_C=True,confidence='low')
        y['ink']='The first surviving stroke is tall and looped, followed by a separate i-like dot and a low e/n-like run. These favour R3’s bien over the abbreviation i.e.; the heavy deletion prevents resolution, so both are retained.'
    if i==22:
        y.update(final=r'\underset{\unsure{\text{Cor.}|\text{où}|\omega}}{\varphi}^{-1}(G)',against_C=True,against_H=True,confidence='low')
        y['ink']='The rotated extra inscription is an open C-like curve joined to a small low wave and a point. Main adds R3’s Cor. as first candidate; où and omega remain possible. It is below-left of the inverse phi, separate from the clearly written où farther right. Underset records the low position only, not a claim that this is a mathematical subscript.'
    if i==28:y['ink']+=' Main confirms the separate crossed t and resolves the word, despite R3’s retained doubt.'
    if i==34:y['consequential']='Restore the visible low zero in C7₀ and keep that axiom label at the end of the main sentence, outside the marginal note.'
    if i==39:y['ink']+=' Main sees the paired f stems and low terminal run through the single strike, resolving the cancelled word while R2 remains cautious.'
    rows.append(y)
rows.append({'id':'030-46','place':'top implication c), star height','C':'baseline *','H':'raised *','readers':['baseline *','raised *','raised *'],'final':r'{}^{*}','ink':'The star is distinctly above the formula baseline to the right of F.G.','crop':'crops/root/030_top.png','confidence':'high','kind':'insertion or placement','against_C':True,'against_H':False,'marked_in_H':'no'})
rows.append({'id':'030-47','place':'after main C7₀ label','C':'C7.','H':'C7. in main text, C7₀ : in margin','readers':['C7₀.','C7₀ without period','C7₀ without period'],'final':'C7₀ without additional period','ink':'The supposed punctuation is the low outlined zero itself. No separate point follows it before the marginal boundary.','crop':'crops/root/030_C7label.png','confidence':'high','kind':'other','against_C':True,'against_H':True,'marked_in_H':'no'})
rows.append({'id':'030-48','place':'central setup, initial case','C':'Si','H':'si','readers':['Si']*3,'final':'Si','ink':'A large initial S begins the separate setup immediately before the cancelled line.','crop':'crops/root/030_proof2.png','confidence':'high','kind':'other','against_C':False,'against_H':True,'marked_in_H':'no'})
rows.append({'id':'030-49','place':'right marginal b), after P≤R','C':'no comma','H':'comma','readers':['no comma']*3,'final':'no comma','ink':'The next surviving term Q≤R follows on the lower line after the cancelled partial implication. No comma is visible after the preceding R.','crop':'crops/root/030_right.png','confidence':'high','kind':'other','against_C':False,'against_H':True,'marked_in_H':'no'})
rows.append({'id':'030-50','place':'oblique margin, after Expliciter colon','C':'soit','H':'omitted','readers':['soit']*3,'final':'soit','ink':'After the colon, the rotated line has a short s, small o/i trace and terminal crossed t, before the three-object diagram.','crop':'crops/root/030_left_upright.png','confidence':'high','kind':'omission','against_C':False,'against_H':True,'marked_in_H':'no'})
inv=rr[0]['inventory']
inv[3]['first_words_or_objects']='trivial par def.|déf.'
inv[5]['first_words_or_objects']='explication|explicitation|expliciter|explicitons'
inv[19]['first_words_or_objects']='bien|i.e.'
inv[23]['first_words_or_objects']='Cor.|où|omega, uncertain separate inscription'
notes='[TXT030-orders] Manuscript page 29 gives three monotonicity statements for F.G, separately for ≪, ≼ and ≤. The starred set description says F′.G={A∈F.G | A⊂|F′|}. The abbreviated explanation calls the operation Inf. Conditional on that greatest-lower-bound interpretation, the ordinary monotonicity argument for a) is valid; this is not a new existence proof. The readers’ individual targeted checks are recorded separately.\n\n[TXT030-closure] The text attempts c) with “Prouvons c. Il faut prouver que” and “Prouvons que c’est fermé”. Its last step is valid if the cited theory of F.G really gives componentwise containment and if F′ is lower closed in F. Those premises are not established just by reading this page. In particular, inclusion of intersections does not in general imply either component inclusion for arbitrary sets; R2 checked the precise failure independently. The page’s figure-specific assertion is therefore retained as written, not replaced by a general-set claim. The repeated que, the literal “est le =” and the clipped L/G are preserved without grammatical or mathematical repair. A contextual enlargement removes the false prime in the cancelled A,A′∈F: that stroke descends from que above.\n\n[TXT030-C7] The corollary says C6 is valable. The main line then says “Vérifions quand même C7₀”, with a visible small zero. The proposed extension is F′=G′∪(F\\G), called réunion disjointe. Its three remaining tasks are explicitly listed after “Il faut vérifier”. The right note says “Un peu vif” and “mais il faut vérifier encore l’unicité”, then extracts two implications under “Cela amène à dégager”. No full verification of existence, figure structure, subdivision, or uniqueness is claimed by this run. The left note identifies the restriction with an inverse image.\n\n[TXT030-ink] The lower-right boundary strokes are reproduced with TikZ around the complete marginal text and its tikz-cd square. The small inscription below-left of inverse phi, absent from both witnesses, remains Cor./où/omega; its position is preserved without interpreting it as a subscript. The starred word remains explication/explicitation/expliciter/explicitons, and the cancelled short word remains bien/i.e. The spelling def./déf. is uncertain at the accent. No date, title sheet or total-page statement occurs; manuscript number 29 is present.'
notation=[{'sign':'three orders','form':r'\ll,\preceq,\leq','evidence':'030_top and 030_right; different glyphs checked at every occurrence.','ambiguity':'The cancelled right-margin comparison remains leq/<.'},{'sign':'downward membership','form':r'\rotatebox{-90}{$\in$}','evidence':'Four arch-plus-middle-stroke glyphs in 030_proof2.','ambiguity':''},{'sign':'C7₀','form':'C7 with a closed low oval zero, no separate period','evidence':'030_C7label.','ambiguity':'C loses the zero; H displaces it.'},{'sign':'phi inverse','form':r'\varphi^{-1}(G),\varphi:F\prime\to F\ldots','evidence':'030_left_upright.','ambiguity':'Separate inscription beneath phi is not silently interpreted as part of its notation.'}]
# The final execution follows comparison with all completed reader reports.
extra=[{'statement_id':'TXT030-orders-conditional-main','date':'2026-11-19','who':'GPT-6 Astra Pro; main reader; inherited effort not separately exposed; SP34 second pass','type':'targeted proof check','outcome':'Given F.G is greatest lower bound for the stated order, F′.G is below F′ and G; F′≪F makes it a lower bound of F,G, hence it is below F.G. This proves only the conditional order step.'},{'statement_id':'TXT030-closure-conditional-main','date':'2026-11-19','who':'GPT-6 Astra Pro; main reader; inherited effort not separately exposed; SP34 second pass','type':'targeted proof check','outcome':'Assuming the figure-product componentwise containment lemma and lower closure of F′ in F, A′⊂A with A∈F′ implies A′∈F′. Together with the already stipulated interior condition this gives membership in F′.G. The figure lemma, interior invariance and uniqueness are not proved.'}]
save(n,t,rows,inv,notes,rr,notation,{'def. / déf.':'définition (accent uncertain)','p.r.':'par rapport','ds':'dans (uncertain abbreviation)','i.e.':'id est','Inf':'infimum','Cor.':'corollaire'},'Whole page and both halves viewed; all 18 C doubts and all C/H disagreements enlarged. Slanted left note rotated upright; right-margin rules reconstructed. Every reader’s complete proposal and follow-up retained.',extra_checks=extra)
