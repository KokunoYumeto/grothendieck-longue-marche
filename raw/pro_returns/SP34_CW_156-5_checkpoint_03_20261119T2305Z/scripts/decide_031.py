from adjudication import *
n=31;rr=reports(n)
t=(O/'readers/R3/scan031.tex').read_text()
t=t.replace(r'\unsure{=|\geq}',r'\unsure{=|\supseteq|\geq}')
t=t.replace(r"G'\deleted{\unsure{\circ}}",r"\unsure{{G'}^\bullet|{G'}^{\deleted{\circ}}}")
t=t.replace(r'\deleted{$\unsure{B}\ni$}',r'\deleted{$B\unsure{\ni|\supset}$}')
t=t.replace(r'\deleted{\unsure{B}}A',r'\deleted{B}A')
t=t.replace(r'\unsure{est contenu dans}',r'\unsure{est|et} \unsure{contenu dans}')
# Attach the separately drawn small hook beside the replacement where its ink stands.
marker='% @ far right edge, beside the final replacement: two unlabelled curved pen strokes'
if marker in t:
    body,hook=t.split(marker,1)
    hook=hook.strip()
    t=body.replace(r"\inserted{fermé dans $F'$},",r"\inserted{fermé dans $F'$}"+'\n'+marker+'\n'+hook+'\n,').rstrip()+'\n'
triples={
1:["F'"]*3,
2:[r'\deleted{\unsure{=|\supset}}']*3,
3:[r'\unsure{\supseteq|\geq}',r'\unsure{\supseteq|=}',r'\unsure{=|\geq}'],
4:['no full stop']*3,
5:[r'\unsure{élémt|élément|élt}']*3,
6:[r'\unsure{{G\prime}^\bullet|G\prime\deleted{\circ}}',r'G\prime\deleted{\unsure{\circ}}',r'G\prime\deleted{\unsure{\circ}}'],
7:[r'\deleted{\unsure{)|?}}']*3,
8:[r'\deleted{B\unsure{\ni|\supset}}',r'\deleted{B\ni}',r'\deleted{\unsure{B}\ni}'],
9:[r'A^{\unsure{\bullet|\circ}}',r'A^{\unsure{\circ|\bullet}}',r'A^{\unsure{\bullet|\circ}}'],
10:[r'\deleted{\unsure{G}}F']*3,
11:[r'\deleted{\unsure{B}}A',r'\deleted{B}A',r'\deleted{\unsure{B}}A'],
12:[r'\unsure{élémt|élément|élt}']*3,
13:[r'\deleted{\unsure{si x\in A}}']*3,
14:['lui']*3,
15:['plus petit él. de F (et à fortiori de F minus G) qui contient x']*3,
16:[r'\deleted{raffine}']*3,
17:['seult']*3,
18:['no erased word']*3,
19:[r'\deleted{que \unsure{tout}}']*3,
20:['live que after cancelled que tout']*3,
21:[r'\deleted{\unsure{Soit|\forall}}',r'\deleted{\forall}',r'\deleted{\forall}'],
22:[r'additional \unsure{et|est} before the higher family phrase',r'single \unsure{est|et} before contenu dans','single est within unsure est contenu dans'],
23:[r'\unsure{est contenu dans}',r'\unsure{est|et} \unsure{contenu dans}',r'\unsure{est contenu dans}'],
24:[r'\inserted{\unsure{a un plus petit}}',r'\inserted{a un plus petit}',r'\inserted{\unsure{a un plus petit}}'],
25:[r'\unsure{élémt|élément|élt}']*3,
26:[r'\unsure{str.}']*3,
27:['de de F prime']*3,
28:['C linear order provisionally retained','family phrase is interlinear insertion; one est/et on base line','family phrase is interlinear insertion; one est on base line'],
29:[r'\deleted{\unsure{Soit|\forall}}',r'\deleted{\forall}',r'\deleted{\forall}'],
30:[r'\deleted{\unsure{B}}A',r'\deleted{B}A',r'\deleted{\unsure{B}}A'],
31:[r'\unsure{élémt|élément|élt}']*3,
32:[r'\deleted{\unsure{$\mathcal R_{F\prime}$-satu.|$\mathscr R_{F\prime}$-satu.}}']*3,
33:["l'ens, without period"]*3,
34:['live support calculation and brace labels as C']*3,
35:['open circle followed by elevated (G prime) or (F)']*3,
36:['à fortiori']*3,
37:['F^A={B in F | A subset B}, with separately recorded overwrite']*3,
38:['fermé dans F prime inserted; final strata sentences as C']*3,
}
rows=[]
for i,x in enumerate(differences(rr[0]),1):
    cr='top' if i in (1,2,34) else 'eq_top' if i in (3,4) else 'uppertext' if i==5 else 'Gprime_mark' if i==6 else 'A_end' if i==7 else 'deleted_before_x' if i==8 else 'lastA_mark' if i==9 else 'case2_overwrites' if i in (10,11) else 'cest_word' if i==14 else 'case2' if i in (12,13,15,36) else 'bintro' if 16<=i<=20 else 'quantifier_compare' if i in (21,29) else 'inserted_line' if i in (22,23,28) else 'cancelwords_left' if 24<=i<=27 else 'restated_set' if i in (30,33,37) else 'condition1' if i==31 else 'R_deleted' if i==32 else 'case1' if i==35 else 'condition2'
    y=row(n,i,x,triples[i],f'crops/root/031_{cr}.png')
    if i==3:
        y.update(final=r'\unsure{=|\supseteq|\geq}',against_C=True,against_H=False,confidence='low',kind='other',review_type='previously unmarked relation reviewed')
        y['ink']='The upper component is short and bends right, above a separate lower bar. Main compared the standalone mark, the matching mark after Comme in b), and the shallower hooked upper bar in the inline equality after forall x. The same-hand comparison leaves a curled equals sign plausible, so = is first; superset-or-equal and greater-or-equal remain explicit alternatives. No relation is selected from the proof’s intended conclusion.'
        y['crop']='crops/root/031_eq_top.png, 031_b_relation.png, 031_inline_relation.png; recipes in documentation/crops.jsonl.'
        y['consequential']='The standalone support comparison and its recurrence in b) are now explicitly uncertain (= / ⊇ / ≥); the support proof does not settle the written glyph.'
    if i==6:
        y['final']=r'\unsure{{G\prime}^\bullet|{G\prime}^{\deleted{\circ}}}'
        y['ink']+=' Main confirms the mark is raised: both alternatives preserve that height. A solid glyph with no separate crossing favours the live-dot alternative, but erasure of an old circle cannot be excluded.'
        y['consequential']='The raised mark after G′ is preserved with uncertain live/deleted state, rather than certainly deleting it or omitting it.'
    if i==8:y['ink']+=' Main sees the B bowls and retains ni/supset uncertainty because the middle horizontal overlaps the cancellation.'
    if i==9:y['ink']+=' R2 puts circle first because of the small pale centre. Main keeps bullet first for the predominantly solid body, without excluding a retraced circle.'
    if i in (11,30):
        y.update(final=r'\deleted{B}A',against_C=True,confidence='high')
        y['ink']='Main enlarged this overwrite individually. The earlier upright and separate upper/lower bowls remain behind the final triangular A; these identify B, agreeing with R2. The live A and deletion state are retained.'
    if i==14:y['consequential']='Retain the literal c’est lui plus petit él. de F; C’s le is corrected to the visibly dotted lui, without adding a missing article.'
    if i in (21,29):
        y.update(final=r'\deleted{$\forall$}',against_C=True,against_H=(i==21),confidence='high',kind='misread symbol or index')
        y['ink']='Both isolated glyphs have two converging legs and a crossbar, matching the earlier universal sign in structure; no separate o/i letter sequence or i dot survives. Main follows R2/R3 in reading a cancelled forall. R1 retains Soit/forall uncertainty; the full proposals preserve that dissent.'
    if i==22:
        y.update(final=r'one \unsure{est|et} before \unsure{contenu dans}; no separate word before the interlinear family phrase',against_C=True,against_H=True,confidence='medium')
        y['ink']='A∈F′, is followed on the base line by one short crossed word, then contenu dans un plus petit. The family description starts higher, over that base sentence. C’s isolated et before l’ens duplicates the beginning of its later est contenu dans. The surviving short word itself remains est/et, but is transcribed only once.'
    if i==23:
        y['final']=r'\unsure{est|et} \unsure{contenu dans} un plus petit'
        y['ink']+=' The leading short word is the same locus discussed above, not an additional occurrence.'
    if i==28:
        y.update(final=r'interlinear \inserted{l’ens F^A des B∈F tels que A⊂B}, above the base sentence; separate left insertion before element word',against_C=True,against_H=True,confidence='high')
        y['ink']='The family phrase has its own raised baseline, well above A∈F′ and est/et contenu dans un plus petit. The small a un plus petit is farther left with a curved leader to the following element abbreviation. TikZ preserves these levels within the cancelled draft. Main/R2/R3 differ from R1’s provisional linear order.'
    rows.append(y)
rows.append({'id':'031-39','place':'part b, comparison after Comme','C':'=','H':'=','readers':['=',r'\unsure{\supseteq|=}',r'\unsure{=|\geq}'],'final':r'\unsure{=|\supseteq|\geq}','ink':'The same short bent upper component over a separate lower bar recurs after Comme. The main comparison with the standalone sign and the inline equality leaves the same alternatives; no silent context-based distinction is made.','crop':'crops/root/031_b_relation.png and 031_inline_relation.png','confidence':'low','kind':'other','against_C':True,'against_H':False,'marked_in_H':'no','review_type':'previously unmarked relation reviewed'})
rows.append({'id':'031-40','place':'cancelled draft, enclosure and left insertion leader','C':'no graphic enclosure or leader','H':'editorial description of three crossed and boxed lines','readers':['not drawn','not drawn','drawn around the complete cancelled text'],'final':'TikZ enclosure around the lower abandoned lines and curved attachment beside a un plus petit','ink':'The lower two lines are bordered by a curved left turn, bottom horizontal and short right rise. A separate curved line links the small left insertion to the element word. Those paths are distinct from the strikes through the text.','crop':'crops/root/031_cancel.png and 031_cancelwords_left.png','confidence':'high','kind':'drawing or diagram','against_C':True,'against_H':True,'marked_in_H':'no'})
rows.append({'id':'031-41','place':'far-right edge beside final replacement','C':'omitted','H':'omitted','readers':['not recorded','not recorded','two unlabelled curved strokes drawn'],'final':'two unlabelled curved pen strokes reproduced in TikZ beside the replacement','ink':'At the right edge below inserted F′ are two nested dark hooks, separate from the word and the margin edge. Their function is uncertain; no lexical label or arrowhead is invented.','crop':'crops/root/031_edge_hook.png','confidence':'high','kind':'drawing or diagram','against_C':True,'against_H':True,'marked_in_H':'no'})
# Full inventory will be checked against the complete R3 proposal before execution.
inv=[{'element':i,'kind':e['kind'],'position':e['position'],'first_words_or_objects':e['content'],'sheet_kind':'text','hand':'his hand'} for i,e in enumerate(rr[2]['inventory'],1)]
inv[8]['first_words_or_objects']='|F′| unsure =|⊇|≥ |F|.'
inv[11]['first_words_or_objects']='Raised mark beside G′: live bullet / cancelled circle uncertain; extra cancelled hook after closing °(G′).'
inv[13]['first_words_or_objects']='Cancelled B followed by uncertain ∋|⊃.'
inv[18]['first_words_or_objects']='Previous B overwritten by A.'
inv[32]['first_words_or_objects']='B underneath live A in A⊂B.'
rows.append({'id':'031-42','place':'cancelled draft, first condition label','C':'1°) before the cancelled opening','H':'1) assigned to the later noun fragment','readers':['1°) before opening','1°) before opening','1°) before opening'],'final':'1°) at the start of the cancelled baseline before the quantifier','ink':'The numeral and raised small circle are at the left of the baseline containing the cancelled quantifier and A∈F′, above the separate left insertion. H assigns the label to a later fragment.','crop':'crops/root/031_cancelwords_left.png and 031_quantifier_compare.png','confidence':'high','kind':'insertion or placement','against_C':False,'against_H':True,'marked_in_H':'no'})
notes='[TXT031-support] Manuscript page 30 continues a), the assertion that F′=G′∪(F\\G) is a figure. It first treats supports, then seeks a least member through each point by separating points in |G| from those outside |G|. The displayed brace labels give |G′|=|G| and |F\\G|⊃|F|\\|G|. Under the stated containment in |F|, these inclusions establish support equality. The main reader also checked why a point of |F| outside |G| must lie in some member of F outside G. This conditional set argument does not prove figurehood.\n\n[TXT031-glyphs] The standalone comparison below donc, comme and the comparison after Comme in b) have a hooked upper stroke over a detached lower bar. Main compared both with the shallower hooked equality in the quantified line and retains =/⊇/≥ explicitly; equality is the first candidate from that same-hand comparison, not from the proof’s desired result. R1/R2 prefer the containment-with-bar shape; R3 prefers equality. The raised mark following G′ has uncertain live-dot versus cancelled-circle state. The final A mark in the first case is bullet/circle, without clear star arms. The extra reversed-membership/superset sign in the small cancelled fragment is restored. None is repaired from the expected mathematics.\n\n[TXT031-wording] The second case literally reads c’est lui plus petit él. de F (et à fortiori de F\\G) qui contient x. The dotted i establishes lui; the missing article is not supplied. H’s cf. définition phrase and rearrangement are not in the ink. Both OK checks are retained. The two cancelled introductions before A∈F′ are universal signs, with R1’s Soit/forall dissent recorded.\n\n[TXT031-refinement] Part b replaces raffine by inserted subdivise, then says it suffices to check refinement. Its first attempt is cancelled: l’ens F^A des B∈F tels que A⊂B is an interlinear addition above the base est/et contenu dans sentence; a un plus petit is a separate left addition. C’s extra et duplicates the beginning of the lower phrase. The restatement uses F^A={B∈F | A⊂B} and asks for a least element. For A∈F, A itself is a member of this set and lies below every member by definition; that branch was checked directly. The G′ branch and the subsequent assertion that intersections are unions of strata are carried as the author’s claims, not independently proved. The final line replaces the uncertain R-subscript-F′ saturation wording by fermé dans F′.\n\nThe manuscript’s own checking language is Il faut prouver, prouvons A⊂B, OK, OK !, il faut voir seult, and the several c’est évident/c’est vrai assertions. No date, title sheet or total-page statement occurs; manuscript number 30 is present. The small unlabeled hooks at the right edge are drawn without assigning a meaning.'
notation=[{'sign':'small support comparison','form':r'\unsure{=|\supseteq|\geq}','evidence':'031_eq_top, 031_b_relation and 031_inline_relation.','ambiguity':'Same hooked-upper-stroke pattern at two disputed occurrences; all readers’ alternatives retained.'},{'sign':'universal quantifier','form':r'\forall','evidence':'Earlier live quantifier; both cancelled glyphs in 031_quantifier_compare.','ambiguity':'R1 retains Soit as an alternative; main/R2/R3 read two legs and crossbar.'},{'sign':'filled raised marks','form':'G-prime with live bullet / deleted circle; final A with bullet/circle','evidence':'031_Gprime_mark and 031_lastA_mark.','ambiguity':'Filled body does not establish deletion state; final mark has a tiny pale centre.'},{'sign':'script R with F-prime subscript','form':r'\mathcal R_{F\prime}|\mathscr R_{F\prime}','evidence':'031_R_deleted.','ambiguity':'Crossing obscures alphabet and following abbreviated saturation word.'}]
extra=[{'statement_id':'TXT031-support-main','date':'2026-11-19','who':'GPT-6 Astra Pro; main reader; inherited effort not separately exposed; SP34 second pass','type':'targeted proof check','outcome':'Assuming |G′|=|G|⊂|F| and F′=G′∪(F\\G), any x∈|F| outside |G| lies in a member A∈F and that A cannot be in G. Thus |F|\\|G|⊂|F\\G|. Combining with |G′|=|G| gives coverage of |F|; the reverse inclusion follows from the stated containment. No figurehood, stratum or refinement theorem is proved.'},{'statement_id':'TXT031-least-element-A-in-F-main','date':'2026-11-19','who':'GPT-6 Astra Pro; main reader; inherited effort not separately exposed; SP34 second pass','type':'targeted proof check','outcome':'For A∈F, the defined family F^A={B∈F | A⊂B} contains A and every member contains A. Hence A is its least element for inclusion. This verifies only the stated A∈F branch.'}]
extra.extend([{'statement_id':'R2-031-mutual-containment','date':'2026-11-19','who':'GPT-6 Astra Pro; R2; inherited effort not separately exposed; SP34 second pass','type':'targeted proof check','outcome':rr[1]['checks_performed'][2]['result']},{'statement_id':'R2-031-full-proof-background','date':'2026-11-19','who':'GPT-6 Astra Pro; R2; inherited effort not separately exposed; SP34 second pass','type':'carried as background without fault found','outcome':rr[1]['checks_performed'][3]['result']}])
save(n,t,rows,inv,notes,rr,notation,{'élémt / élt':'élément (abbreviation remains uncertain)','él.':'élément','seult':'seulement','ens':'ensemble','str.':'strates (uncertain cancelled abbreviation)','satu.':'saturé (uncertain cancelled abbreviation)','i.e.':'id est'},'Whole page then both halves, all 22 C doubt occurrences and all disagreements enlarged. Slanted cancelled draft rotated; raised and baseline layers separated. Uncertain support signs compared across three locations. Complete proposals of all three readers retained.',extra_checks=extra)
