from adjudication import *
n=29;rr=reports(n)
t=(O/'readers/R1/scan029.tex').read_text()
t=t.replace(r'\unsure{intersection|inter.}',r'\unsure{inter.|intersection}')
t=t.replace(r'\unsure{la propriété|la présentation}',r'\unsure{la priorité|la propriété|la présentation}')
t=t.replace(r'\unsure{, et des}',r'\unsure{, et des|, et de}')
t=t.replace('(Immédiat sur supports)',r'(\unsure{Immédit|Immédiat} sur supports)')
m2={1:2,2:1,**{i:i for i in range(3,15)},15:17,16:18,17:19,18:20,19:21,20:22,21:23,22:24,23:25,24:26,25:27,26:28,27:29,28:30,29:0,30:31,31:0}
assert len(m2)==31,'Supply R2 mapping after completed report is read'
m3={**{i:i for i in range(1,22)},22:28,23:22,24:23,25:24,26:25,27:26,28:27,29:0,30:0,31:0}
rows=[]
for i,x in enumerate(differences(rr[0]),1):
    cr='top' if i<=5 else 'warning' if i<=14 else 'middle' if i<=16 else 'term' if i==17 else 'deletedprop' if i==18 else 'word' if i in (19,20) else 'lastline' if i==28 else 'formula' if i==29 else 'middle' if i==31 else 'foot'
    r3=reading(differences(rr[2])[m3[i]-1]) if m3[i] else reading(x)+' (submitted page)'
    r2=reading(differences(rr[1])[m2[i]-1]) if m2[i] else reading(x)+' (submitted page)'
    y=row(n,i,x,[reading(x),r2,r3],f'crops/root/029_{cr}.png')
    if i==7:y['ink']+=' Main retains the doubt: the reduced middle may conceal contraction; no full expansion is forced.'
    if i==9:
        y['final']=r'\deleted{\unsure{inter.|intersection}}';y['against_C']=True
        y['ink']+=' Main inspected the rotated fourfold crop: the short extent and terminal point favour inter. first, with the longer reading retained under the crossing.'
    if i==17:y['ink']+=' Main agrees that the nearly straight initial favours l before s; the cancellation/retracing does not permit a firm resolution.'
    if i==18:
        y['final']=r'\deleted{\unsure{la priorité|la propriété|la présentation}} before à une propriété';y['against_C']=True
        y['ink']+=' Main isolated this phrase at fivefold scale: one long p descender and an early dotted stroke survive, whereas the adjacent live propriété has two p descenders. This supports R3’s added priorité as first candidate, without settling the obscured middle.'
    if i==19:y['confidence']='low';y['ink']+=' Main retains modération/médiation despite R2’s resolution: the compressed medial strokes do not clearly distinguish the full endings. H’s demi-treillis requires absent tall letters.';y['consequential']='The named property is modération/médiation, still uncertain; H’s demi-treillis is not supported by the letters.'
    if i==24:y['final']=r'\deleted{\unsure{, et des|, et de}}';y['against_C']=True;y['ink']+=' Main retains R2’s alternative without the terminal s because the end intersects the strike.'
    if i==25:
        y['final']=r'\unsure{Immédit|Immédiat}';y['against_C']=True;y['against_H']=True;y['confidence']='low';y['kind']='misread word'
        y['ink']='The initial has the bars of capital I and the ending has a tall t. Main viewed the foot and R1’s isolated enlargement: the low sequence between d and t does not securely supply an a. Immédit is therefore first, Immédiat remains possible; lowercase immédite is not supported by the barred initial and lack of an ending e. R1 resolves Immédiat, while R2/R3 retain the C alternatives.'
    if i==28:y['ink']+=' Main first mistook the diagonal for a p descender. The wider 029_lastline enlargement shows that line continuing from the cancelled F′ above; it cannot establish p. The remaining curve favours sur, with par still possible.'
    rows.append(y)
rows.append({'id':'029-32','place':'warning, punctuation after the cancelled final formula','C':'no full stop after cancelled G subset P(L)','H':'full stop after cancelled G subset P(L)','readers':['no full stop']*3,'final':'no full stop','ink':'No separate terminal point appears after the cancelled right-edge formula. The following Nous starts a new paragraph.','crop':'crops/root/029_warning.png','confidence':'high','kind':'other','against_C':False,'against_H':True,'marked_in_H':'no'})
rows.append(row(n,33,differences(rr[1])[15],['new paragraph']*3,'crops/root/029_middle.png'))
notes='[TXT029-infimum] Manuscript page 28 names the constructed infimum for ≪ the “figure intersection” F.G. It distinguishes this from the ordinary intersection F∩G of the families, saying the two coincide for compatible figures. It states that the construction works for an arbitrary family and writes |∧F_i|=∩|F_i|. These existence and compatibility assertions were read as statements, not independently established here. The missing verb in “où F et G compatibles” is retained.\n\n[TXT029-name] The final named property remains modération/médiation, underlined and in double quotes; H’s demi-treillis is not in the ink. The preceding verb is l’apparente/s’apparente, with l first on its nearly upright initial. The cancelled phrase before à une propriété may be la priorité: a fivefold enlargement exposes only one p descender. These doubts remain in place.\n\n[TXT029-cancelled] The three-line Propriété at the foot is cancelled. It states F′≼F implies F′.G≼F.G and adds “Immédit/Immédiat sur supports”, then “Subdivision induite sur/par un raffinement”. A wider view showed that the apparent p stem in the last preposition was a cancellation stroke, so sur/par is left uncertain. The check of equal supports is conditional on |F′|=|F| and the displayed support formula. It does not verify the full subdivision relation. R3 also checked the abstract monotonicity of meet in one preorder, explicitly distinguishing it from the manuscript’s separate subdivision relation.\n\nNo explicit question mark or à vérifier, date, title sheet or page count appears. The only page identifier is handwritten 28. The small brown damaged mark before l’appelle remains uncertain even as an erased-letter attribution.'
notation=[{'sign':'≪ versus ≼','form':'Double acute order strokes in the proposition; curved relation with lower stroke in the cancelled property.','evidence':'029_top and 029_foot.','ambiguity':'The relations are not conflated in the mathematical checks.'},{'sign':'meet and cap','form':'Angular bigwedge at left; rounded bigcap at right; i∈I below both.','evidence':'029_formula.','ambiguity':''},{'sign':'quotation marks','form':'Two short raised pen strokes on each side; rendered with two backticks and two apostrophes.','evidence':'029_top and 029_word.','ambiguity':''},{'sign':'powerset P and L','form':'P has an angular enclosure and low curl; L has upright/angled stroke and foot.','evidence':'029_warning.','ambiguity':'P alphabet remains mathfrak/mathscr/mathbb; L retained ordinary.'}]
inv=rr[1]['inventory']
inv[14]['first_words_or_objects']='la priorité|la propriété|la présentation'
inv[15]['first_words_or_objects']='modération|médiation'
inv[18]['first_words_or_objects']='(Immédit|Immédiat sur supports)'
inv[19]['first_words_or_objects']='Subdivision induite sur|par un raffinement'
save(n,t,rows,inv,notes,rr,notation,{'Inf':'infimum','inter.':'intersection (uncertain cancelled abbreviation)'},'Whole, both halves, the display and all doubtful/deleted/interlinear loci enlarged. Eleven inherited C doubts reviewed. The final preposition was re-examined in the wider cancellation context; the resulting uncertainty is explicit.')
