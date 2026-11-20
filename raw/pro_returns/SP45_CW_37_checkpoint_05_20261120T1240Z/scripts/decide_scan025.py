#!/usr/bin/env python3
"""Explicit main-reader adjudication after the three independent scan 025 returns."""
from pathlib import Path
import copy,json
R=Path(__file__).resolve().parents[1]
D={r:json.loads((R/f'readers/scan025/{r}/report.json').read_text()) for r in ('r1','r2','r3')}
C=copy.deepcopy(D['r3']['changes'])
m32={0:0,1:12,2:13,3:15,4:1,5:14,6:2,7:24,8:25,9:26,10:27,11:28,12:29,13:16,14:30,15:3,16:31,17:32,18:33,19:17,21:34,22:35,23:4,24:18,25:36,26:37,27:38,28:19,29:5,30:39,31:20,32:40,33:41,34:42,35:45,36:44,37:46,38:47,39:6,40:48,41:48,42:48,43:49,44:49,45:50,46:7,47:53,48:54,50:55,51:57,52:58,53:22,55:59,56:60,57:23,58:9,59:10,60:61,61:62,62:63,63:64,64:11,65:65,66:40,67:40,68:49,69:51}
m21={0:37,1:1,2:38,3:9,4:39,5:40,6:41,7:26,8:28,9:42,10:43,11:44,12:2,13:0,14:1,15:46,16:45,17:11,18:47,19:48,20:49,21:50,22:52,23:51,24:3,25:3,26:4,27:5,28:6,29:7,30:8,31:9,32:10,33:10,34:12,35:24,36:13,37:13,38:14,39:15,40:16,41:17,42:53,43:18,44:19,45:19,46:20,47:21,48:22,49:23,50:25,51:25,52:26,53:26,54:26,55:54,56:27,57:27,58:28,59:30,60:31,61:32,62:33,63:34,64:35,65:36}
def clean(s):
    return s.replace('\\prime',"'").replace("cohérent\\'\\'","cohérent''")
for i,c in enumerate(C):
    c['readers']={'r3':c['reading']}
    if i in m32:
        j=m32[i];c['readers']['r2']=clean(D['r2']['changes'][j]['reading']);c['readers']['r1']=clean(D['r1']['changes'][m21[j]]['reading'])
    c['mathematical_consequence']=''
C[20]['readers'].update(r1=r'\deleted{\unsure{$\tilde X_{\mathrm{et}}$}} que; no extra word',r2=r'\deleted{$\tilde X_{\mathrm{et}}$} que; no extra word')
C[49]['readers'].update(r1=r'\deleted{\illegible{1}}',r2=r'\deleted{\illegible{1}}')
C[54]['readers'].update(r1=r'\deleted{et}',r2=r'\deleted{\illegible{1}}')
C[70]['readers'].update(r1='Corrected text with insertion attachment, but the two nested curved call lines are not drawn',r2='Corrected text with insertion attachment, but the two nested curved call lines are not drawn')
for i,js in {34:[42,43],46:[7,52],51:[56,57],52:[8,58]}.items():
    C[i]['readers']['r2']='; '.join(clean(D['r2']['changes'][j]['reading']) for j in js)
def p3(n):return f'readers/scan025/r3/crops/{n}.jpg'
def p1(n):return f'readers/scan025/r1/crops/r1_{n}.jpg'
def pm(n):return f'crops/scan025/main{n}.jpg'
paths={0:pm('02_heading'),1:p1('01_top_note'),2:p1('01_top_note'),3:p1('01_top_note'),4:p1('01_top_note'),5:p1('01_top_note'),6:pm('03_opening_ref_quotes'),7:p3('02_en_effet'),8:p3('02_en_effet'),9:pm('03_opening_ref_quotes'),10:p3('03_superseded_openings'),11:p3('03_superseded_openings'),12:p3('04_pleine'),13:p3('04_pleine'),14:p3('05_after_23'),15:p3('04_pleine'),16:p3('06_final_equality'),17:p3('25_identifie'),18:p3('25_identifie'),19:p3('06_final_equality'),20:p3('06_final_equality'),21:p3('06_final_equality'),22:pm('01_cancelled_geometry'),23:pm('04_cancelled_beginning'),24:pm('04_cancelled_beginning'),25:pm('04_cancelled_beginning'),26:pm('04_cancelled_beginning'),27:p3('07_crossed_VI'),28:p3('07_crossed_VI'),29:pm('04_cancelled_beginning'),30:pm('04_cancelled_beginning'),31:pm('05_cancelled_transition'),32:p3('09_inductive_reference'),33:pm('05_cancelled_transition'),34:pm('05_cancelled_transition'),35:p1('11_G_substitution'),36:p1('11_G_substitution'),37:p3('11_schema'),38:pm('06_cancelled_second_reference'),39:pm('06_cancelled_second_reference'),40:p3('13_nested_left'),41:p3('12_nested_right'),42:p3('13_nested_left'),43:p3('15_products'),44:p3('13_nested_left'),45:p1('13_left_note'),46:pm('08_live_opening'),47:pm('08_live_opening'),48:pm('08_live_opening'),49:p3('17_before_Compte'),50:pm('08_live_opening'),51:p3('18_live_corrections'),52:p3('18_live_corrections'),53:p1('16_after_G'),54:p1('16_after_G'),55:p3('20_et_est'),56:p3('21_comme_on'),57:pm('09_live_VII'),58:pm('09_live_VII'),59:pm('10_live_final'),60:pm('10_live_final'),61:p1('19_closing_insertions'),62:p1('19_closing_insertions'),63:p1('19_closing_insertions'),64:pm('11_closing_VI'),65:p3('23_complementaire'),66:p3('09_inductive_reference'),67:pm('04_cancelled_beginning'),68:pm('07_finis'),69:pm('01_cancelled_geometry'),70:p3('18_live_corrections')}
ev={
0:'The main heading crop shows distinct horizontal strokes above and below I/X; these are retained separately from the letters.',
1:'The top-note crop shows an open top, sloping left side with a lower loop, long lower edge and right upturn. The r3 drawing preserves the upper-right relationship to the heading; C puts it in a generic margin and H describes the frame without drawing it.',
2:'The top crop separates prouv-e-r-ons, including the medial e/r; it is the future prouverons, not H prouvons.',
3:'The top crop has a wave above X and a low e/t pair without a separate accent above e. This occurrence is read independently of the accented ones below.',
4:'The top crop shows a horizontal line above and below V/I, distinct from the frame.',
5:'The top crop shows the final digit with a short upper bar and hooked descending body: 5, followed by a dot. All readers resolve C001 to 1.25.',
6:'The opening-reference crop shows VI with separate upper/lower strokes and the digits 1.9.3.',
7:'The crop separates en, the two f stems of effet, C and le below the addition. The final cas-like run remains covered by the cancellation; only that word stays unsure.',
8:'Question étant is written above the cancelled en effet run and attached at that position; H treats it as ordinary baseline prose.',
9:'The crop shows donc coherent i.e. above the baseline, with two short raised strokes on each side of cohérent. These are paired quotation strokes, not guillemets.',
10:'The superseded-opening crop supports an extra C-like contour before the parenthesized C-prime and a sous-caté fragment after le. r1 retains both C(C-prime) and (C-prime); r2/r3 stop at sous and add an unreadable word. The visible fragment is retained tentatively, without supplying its ending or an extra complete word.',
11:'The superseded-opening crop shows a hooked capped J followed by a low e. All readers choose Je; grammatical Il is not substituted. F est constructible belongs to this same cancelled line.',
12:'A separate short word is heavily struck before the live pleine. Its low descender and remaining fragments favor pleine; quasi, proposed by r1, cannot be excluded under the strike. Both candidates remain, with pleine first.',
13:'The crop shows a separate short rising stroke immediately above the lowered e of the opening X subscript. r1/r3 and H read ét; r2 and C omit the visible acute.',
14:'The crop shows a distinct dense cancelled cluster after the comma following 2.3. Its letters cannot be separated; an estimated one word remains illegible, at this location.',
15:'The interlinear parenthesis crop has separate upper/lower bars around VI, followed by 1.9.3.',
16:'The larger faut prouver sits on the next baseline below the small interlinear parenthesis, which ends in il. Main also inspected the adjacent interlinear reference in crop 04_pleine. H extends its add macro too far.',
17:'The long cancelled-characterization crop supports s-identifie, including its apostrophe and the f/i run, rather than H est identique. The complete clause remains crossed.',
18:'The same crop shows a short underline under cohérents, independent of the long crossing line through the clause.',
19:'The equality crop separates the X arms, upper wave and low e/t under the cancellation. r2/r3 resolve the formula; r1 keeps the whole formula unsure. The formula is resolved at medium confidence, with bare et.',
20:'Between the cancelled formula and que the crop shows blank paper, not another written word. H additional ill marker is not retained. The formula doubt is treated in the preceding row.',
21:'The equality crop has a detached dot above a curved low stroke after C=C-prime: a semicolon, not a period.',
22:'The geometry crop shows the two hooked vertical strokes at the opening conclusion, stepped enclosing edges, six long obliques plus a short upper-right oblique, and nested hatched bands. The r3 paths are retained. C uses deletion macros; H expressly says it abridges this cancelled block and describes the strokes. The extra text/graphics here are recorded with that declared scope acknowledged.',
23:'The first cancelled-lines crop shows V plus two I strokes between separate upper and lower lines, then 5.6 a).',
24:'At the upper-right end of the first cancelled line, the crop shows a wave over X and low bare et. No acute is present at this occurrence.',
25:'The crop shows l’objet final X de struck at upper right, est cohérent, donc struck at the next left start, then C-prime est formé des objets coherents before de X (2.5). Formé has no extra final e. This preserves the source sequence and local cancellations inside the globally cancelled passage, which H declares abridged.',
26:'The first cancelled-lines crop has a short separate underline under cohérents, not merely generic emphasis.',
27:'The tight VI crop shows V/I and upper/lower bars beneath the cancellation. The left curved portion is continuous with the cancelling stroke, not a secure separate parenthesis. r3 resolved VI is adopted over the r1/r2 doubts.',
28:'The same crop shows bare lower e/t on the X before (2.5), with a separate wave above X.',
29:'The first cancelled-lines crop shows a capital E at the left start and separate upper/lower bars around VI before 1.24. H lower-case en and italic reference differ.',
30:'A separate crossed short loop/stem cluster stands between the comma after 1.24 and live et compte tenu. The et candidate remains uncertain; H omits this separate local cancellation.',
31:'The transition crop shows bare lower e/t on X after dans, with the wave above X. It is not normalized from other occurrences.',
32:'The reference crop leaves the last numeral overwritten/crowded between 6 and 8. Both visible candidates remain; H gives only a question mark.',
33:'The transition crop shows il suffit de prouver at the left, C subset C-prime followed by a comma, and capital Mais to its right; the next left line begins F in ob C. H moves Mais ahead of the il suffit clause. No punctuation repair is made.',
34:'The transition crop shows a low o before the rising b, and separate short underlines under quasi and compact. H capitalizes Ob and omits these underlines.',
35:'The replacement crop shows the old G/membership run crossed, but cannot settle whether ob precedes X. Descending p-like ink and other surviving pieces support tentative représentable par un on that same cancelled line, omitted by C. The whole word run stays unsure; r2 certainty on par un is not adopted.',
36:'The upper replacement has an open G/C contour, membership, X and a low e/t. A short raised mark sits over the e, but its attachment as an acute or X prime remains uncertain. G/C and ét versus prime-et alternatives are preserved; r1 certainty is not adopted.',
37:'The schéma crop shows the word, X and a high prime, followed by a separate open curved sign. Its horizontal middle overlaps the strike: membership or C remains possible. r3 preserves this extra contour; r1/r2 omit or absorb it in X uncertainty.',
38:'The second-reference crop shows a separately crossed (5.6.1) before the following Roman-numbered reference. H omits the cancelled old reference.',
39:'The same crop shows VII between separate upper and lower strokes before 5.6.1.',
40:'The nested-left crop retains fragments of voir que, F/possible prime, the crossed relation and target run before la diagonale. No candidate is selected from what the mathematics would require. The nested-right crop also gives D’autre part pour. r2 resolves voir que; r1/r3 uncertainty is retained under the hatching.',
41:'The nested-right crop shows F, a right arrow and F-times-F. The possible lower X crosses the hatching and cannot be isolated; r1/r3 indexed/unindexed alternatives are retained over r2 certainty.',
42:'The lower nested band leaves recognizable fragments of il suffit de voir que, pour tout, et que and the final produits run, with two short physically obscured prose stretches. All retained candidates and estimated two-word gaps remain explicit. H abridges these clauses as ill; no proof reconstruction supplies them.',
43:'The products crop shows produits above a separately struck limites projectives, with an insertion call. H prints produits without that added state.',
44:'The lower nested-left crop shows the added reference below the line, with two short i strokes/dots inside the inner parentheses. It is (2.6 (ii)), not H (2.6 (i)).',
45:'The rotated left-note crop supports pourq-like upper strokes and a detached final mark but does not settle pourquoi, abbreviated pourq., or the shorter pour. The lower p/a/r then e/x/e/m/p/l/e run is readable as par exemple. r1/r3 lower-line certainty is adopted over r2 doubt; C préciser is rejected.',
46:'The live-opening crop shows upper/lower bars around VI and a small low comma after the 9, before b).',
47:'The live-opening crop shows p, a rounded o, a u-like continuation and r: stable pour, not H par.',
48:'The live-opening crop follows the rising baselines: limites inductives finies precedes et limites projectives finies and qu’elle est génératrice; et formée begins the next left line. There is one 2.6(i), after Compte tenu, followed by et (2.7.2). H expressly doubts its order and states two occurrences; the source has one.',
49:'The tight crop supports an E/e loop and t beneath the dense strike before Compte. r3 Et|et is retained as a candidate rather than a fully unreadable word; the case remains open.',
50:'The live-opening crop shows low o before the ascending b in F in ob C. H capital O is not supported.',
51:'The correction crop shows cancelled cela résulte, added en vertu de above it, and a separately surviving baseline de before 2.7. r1/r3 retain both de occurrences; r2 omits the upper de. No grammatical smoothing is made.',
52:'The correction crop separates e/t before barred VI 1.3 under the local cancellation. C027 is resolved to et; the Roman bars are retained.',
53:'The object crop shows G in low ob X with bare lowered e/t. There is no separate acute at this occurrence, unlike the later X before VII 5.6.1.',
54:'The object crop shows the crossed word’s e loop and distinct tall t with cross and foot. r1 et is adopted at medium confidence; r2 leaves it unreadable and r3 tentative.',
55:'The et-est crop leaves the first e buried enough to retain unsure et. The second word has separate surviving e/s curves and the final t, so est is resolved. r1 resolves both and r2 doubts both; r3 partial resolution is adopted.',
56:'The crop shows an initial curved contour, low humps and the final oval/n fragments beneath parallel strikes. Comme on remains only a candidate; all readers retain the doubt.',
57:'The main crop shows a short separate rising stroke directly above the lowered e before t, well below the top of X. It is an acute on this subscript, distinct from the wave over X. All three readers and C omitted it; H ét matches this occurrence. The other independently checked et occurrences are not changed.',
58:'The same main crop shows V and two I strokes between upper and lower lines before 5.6.1.',
59:'The final-proof crop shows VI between separate upper and lower strokes before 1.3.',
60:'The final-proof crop shows q, f and d followed by a dot, with no preceding c. Literal qfd. is retained.',
61:'The closing crop places notamment above the start of en les rattachant, with its call ending before en. The letters are clear. It is not beside eu at the earlier position assigned by H.',
62:'The closing crop shows en les rattachant continuing along the baseline toward aux. The line above it belongs to the added notamment. r1/r3 baseline state is retained over r2/H insertion of the whole run.',
63:'The closing crop shows the tentative explicitement run above aux and connected by a short upward call, then heavily cancelled. r1 added-and-cancelled state is adopted; r2/r3 and C encode cancellation alone. H acknowledges an unread word in an ordinary note but does not transcribe it.',
64:'The final VI crop has separate upper and lower strokes around V/I, followed by a dot.',
65:'The complémentaire crop exposes an initial rounded run, p descender, tall l/t traces and a small upper ending mark, but the middle letters remain buried. The full word is tentative, not restored from grammar.',
66:'The tight inductive-reference crop shows one dotted i inside the inner parentheses; a long oblique strike is not a second i. H numeral doubt does not mark doubt on its distinct ii.',
67:'The first cancelled-lines crop places the 2.6/2.8(i) reference immediately after limites inductives finies, not after génératrice. H question mark belongs to the numeral, not the placement.',
68:'The tight final-line crop shows f, i, n, i and s before the comma and l’inclusion. The long enclosing line does not conceal the word finis.',
69:'The geometry crop places the tilted oval beside the middle of the cancelled block, level with the schéma/reference lines. Its enclosure and three crossing paths plus short outer stroke are drawn. All three readers draw the oval but anchor it before or after the whole block; main integrates it at its source coordinates inside the same TikZ picture. H describes it without drawing it.',
70:'The correction crop shows two separate nested curved calls: one beneath the cancelled et VI1.3 turning down after 2.7, and one beneath il existe turning down at un. The r3 local TikZ drawing retains both; r1/r2 insertion macros alone omit their shape.'}
for i,c in enumerate(C):
    c['crop']=paths[i];c['evidence']='Main inspected the cited crop: '+ev[i]
    if i in (16,40):c['evidence']+=' Companion crop: '+(p3('04_pleine') if i==16 else p3('12_nested_right'))+'.'
C[10].update(reading=r"\deleted{Soit $C$ la catégorie \unsure{Soit $C(C')$ le sous-caté|Soit $(C')$ le sous-caté}}",diff_c=True)
C[12].update(reading=r'\deleted{\unsure{pleine|quasi}}',diff_c=True)
C[45]['reading']=r'\unsure{pourquoi|pourq.|pour} par exemple'
C[47]['confidence']='high'
C[54].update(reading=r'\deleted{et}',confidence='medium')
C[57].update(reading=r'\tilde{X}_{\text{ét}}',diff_c=True,diff_h=False,confidence='high')
C[63].update(reading=r'\inserted{\deleted{\unsure{explicitement}}}',diff_c=True,kind='insertion or placement')
C[69]['reading']='Tilted left oval integrated at the middle of the cancelled-proof TikZ picture, with its text and crossing paths'
extra=copy.deepcopy(D['r2']['changes'][21])
extra.update(crop=pm('06_cancelled_second_reference'),evidence='Main second-reference crop shows a wave above X and a lowered bare e/t pair after comme objet de, before the cancelled old (5.6.1). No detached acute is visible there. All three complete readings agree; r3 did not separately list this H discrepancy.',mathematical_consequence='',readers={'r1':D['r1']['changes'][50]['reading'],'r2':D['r2']['changes'][21]['reading'],'r3':r'\tilde{X}_{\mathrm{et}} (complete reading.tex)'})
C.append(extra)
for i,why in {5:'The top claim’s reference is resolved as VI 1.25 rather than an uncertain closing after 1.2.',44:'The finite-product clause cites item (ii), whereas H cites (i).',66:'The finite-inductive-limit clause cites item (i), whereas H gives (ii); the preceding numeral remains 6/8.'}.items():C[i]['mathematical_consequence']=why
# All C marks, including unchanged retentions, remain explicit.
cd=copy.deepcopy(D['r3']['c_doubts'])
markrow={1:5,2:7,3:10,4:10,5:11,6:12,7:14,8:19,9:27,10:30,11:32,12:35,13:36,14:37,15:40,16:40,17:40,18:40,19:42,20:42,21:42,22:42,23:42,24:45,25:45,26:49,27:52,28:54,29:55,30:56,31:63,32:65}
for q in cd:
    if q.get('c_mark_ids'):
        n=int(q['c_mark_ids'][0][1:]);c=C[markrow[n]];q.update(evidence=c['evidence'],crop=c['crop']);q['reading']=clean(q['reading'])
cd[2]['reading']=C[10]['reading'];cd[3]['reading']='Tentative sous-caté fragment within the same unsure span; no extra complete word supplied'
cd[5]['reading']=r'\unsure{pleine|quasi}'
cd[23]['reading']=r'\unsure{pourquoi|pourq.|pour}'
cd[27].update(reading='et',decision='resolved')
cd[30]['reading']=C[63]['reading']
cd[32].update(crop=pm('05_cancelled_transition'),evidence='Main first-lines and transition crops confirm the separate puisque un, formé without a second final e, and comma followed by capital Mais; no elision, agreement or punctuation repair.')
cd[34].update(crop=p1('19_closing_insertions'),evidence='All three complete lower readings agree on the explicit deferral to générations futures; the main closing crop establishes notamment attachment and added/cancelled explicitement. The separate complémentaire crop remains uncertain.')
un=copy.deepcopy(D['r3']['unresolved'])
un[1]['reading']=r"\unsure{Soit $C(C')$ le sous-caté|Soit $(C')$ le sous-caté}"
un[2]['reading']='Terminal sous-caté fragment included in preceding uncertainty; no inferred ending'
un[3]['reading']=r'\unsure{pleine|quasi}'
un[19]['reading']=r'\unsure{pourquoi|pourq.|pour}'
un[24]['reading']=r'\inserted{\deleted{\unsure{explicitement}}}'
del un[21]
for q in un:q['reading']=clean(q['reading'])
inv=copy.deepcopy(D['r3']['inventory'])
inv[5]['first_words_or_objects']='Soit C la catégorie; unsure Soit C(C′) / (C′) le sous-caté'
inv[7]['first_words_or_objects']='unsure pleine / quasi'
inv[25]['first_words_or_objects']='et, resolved, after G in ob X_et'
inv[28]['first_words_or_objects']='explicitement, tentative, inserted above aux and then cancelled'
inv[43]['first_words_or_objects']='unsure pourquoi / pourq. / pour; par exemple, in the left oval at mid-block height'
inv[49]['position']='left of cancelled schéma/reference lines, integrated with the main cancellation graphic'
order=[0,1,46,2,3,4,31,32,5,6,7,33,8,34,9,10,47,11,12,13,14,15,16,35,43,49,17,18,19,48,20,36,37,44,21,22,38,23,24,39,51,25,40,26,27,45,41,42,28,29,30,50]
inv=[inv[i] for i in order]
idx=next(i for i,x in enumerate(inv) if x['first_words_or_objects'].startswith('explicitement'))
add=copy.deepcopy(inv[idx]);add.update(kind='insertion',first_words_or_objects='Tentative explicitement in the interline above aux, with its call');inv.insert(idx,add)
for i,x in enumerate(inv,1):x['element']=f'025-{i:02d}'
notes=copy.deepcopy(D['r3']['notes'][:7])
notes[5]['text']='The crossed oval has the tentative upper readings pourquoi/pourq./pour and the resolved lower words par exemple. Its physical position is beside the middle of the cancelled argument; no definite mathematical objection is inferred from it.'
notes += [
 {'id':'s025-note08','text':'H expressly gives the large cancelled passage in abridged form. The fuller text and graphic transcription here records local strikes, nested hatching and insertions inside that cancelled passage. The live proof has one 2.6 (i); the cancelled finite-product clause has (2.6 (ii)), while the other cancelled reference remains 2.6/2.8 (i). No cited result was looked up.','basis':'Documentary collation of H’s scope note with the three readings and main crops.'},
 {'id':'s025-note09','text':'The lower X before VII 5.6.1 has a visible acute on its lowered e. Main corrects the unanimous bare-et reader reading to ét there; H matches that occurrence. The opening category also has ét, whereas the separately inspected top note and several other occurrences have bare et. No uniform spelling is imposed.','basis':'Main crops 09_live_VII, r3 04_pleine, and separately inspected formula crops.'},
 {'id':'s025-note10','text':'A limited targeted proof check confirms the final descent step: under the usual topos definition, an epimorphic image F of a quasi-compact object G is quasi-compact. Pull back a covering family of subobjects of F to G, choose a finite subcover, and compose its epimorphic coproduct map with G→F. The resulting map factors through the corresponding finite coproduct of the original subobjects, so that finite family covers F. The live paragraph read here does use G→F in this direction. This check does not establish existence of G, its quasi-compactness as a topos object, the earlier coherence criterion, or the equality of constructibility notions.','basis':'Actual main-reader argument in decisions/scan025_math_work.md, connected to the finally read live paragraph. No research or transcription repair.', 'event_type':'targeted proof check','event_outcome':'Passed conditionally under the stated topos definition and pullback/epimorphism properties: finite-subcover proof of quasi-compactness descending along G→F. All earlier cited ingredients remain unchecked.'},
 {'id':'s025-note11','text':'The proof check uses stability of covering families under pullback in a topos and composition/factorization properties of epimorphisms as background. Those general properties were not independently proved in this run.','basis':'Explicit epistemic limit of the targeted check.', 'event_type':'carried as background without fault found','event_outcome':'Topos pullback stability and elementary epimorphism properties used as stated background; no independent re-proof or computation.'}]
nt=copy.deepcopy(D['r3']['notation'])
for q in nt:
    for k,v in q.items():
        if isinstance(v,str):q[k]=clean(v)
nt[1].update(locus='Top note; opening category; upper object replacement; each remaining occurrence, including the final X before VII5.6.1',evidence='Main inspected each reported occurrence separately. Opening category and final live X before VII5.6.1 have visible acute on e; the top note and other separately inspected occurrences have bare et. The upper replacement retains acute-versus-prime uncertainty.',alternatives='Upper replacement only: lower ét or X-prime with lower et. No global accent normalization.')
tex=(R/'readers/scan025/r3/reading.tex').read_text()
repls=[(r"\unsure{Soit $(C')$ le sous}\illegible{1}",r"\unsure{Soit $C(C')$ le sous-caté|Soit $(C')$ le sous-caté}"),(r'\deleted{\unsure{pleine}}',r'\deleted{\unsure{pleine|quasi}}'),(r'\unsure{pourquoi|pourq.}',r'\unsure{pourquoi|pourq.|pour}'),(r'$G\in\mathrm{ob}\,X_{\mathrm{et}}$ \deleted{\unsure{et}}',r'$G\in\mathrm{ob}\,X_{\mathrm{et}}$ \deleted{et}'),(r'est un objet quasi-compact de $\tilde{X}_{\mathrm{et}}$',r'est un objet quasi-compact de $\tilde{X}_{\text{ét}}$'),(r'\deleted{\unsure{explicitement}}',r'\inserted{\deleted{\unsure{explicitement}}}')]
for a,b in repls:assert a in tex,a;tex=tex.replace(a,b)
start=tex.index('\\reversemarginpar');end=tex.index('\\normalmarginpar',start)+len('\\normalmarginpar')
margin=tex[start:end]
inner=margin[margin.index('\n\\node'):margin.index('\\end{tikzpicture}')]
inner=inner.replace('\\node[anchor=center','\\node[font=\\tiny,anchor=center')
tex=tex[:start]+tex[end:]
anchor='% Irregular enclosing edges and long oblique cancellation strokes.'
assert anchor in tex
tex=tex.replace(anchor,'% Left oval aligned with its source position inside the cancelled proof.\n\\begin{scope}[shift={(29,924)}]'+inner+'\\end{scope}\n\n'+anchor)
viewed=list(dict.fromkeys(paths.values()))
# Some paths are shared by several decisions, but every image was actually emitted once.
assert len(viewed)==33,(len(viewed),viewed)
cfg={'approved_by_main_reader':True,'scan':25,'base_reader':'r3','brief_version':'v009','changes':C,'c_doubts':cd,'unresolved':un,'inventory':inv,'notes':notes,'notation':nt,'abbreviations':D['r3']['abbreviations'],'complete_tex':tex,'main_crop_count':11,'main_viewed_crops':viewed,'adjudications':[],
 'workflow_observation':'All three complete readings and all report sections compared. Main inspected 22 existing reader crops and 11 new crops, once each; no whole or half image was opened by main. Wider local crops were necessary for the cancellation geometry and the disputed order of sloping baselines; overlaps were incidental to distinct loci, not repeat adjudication. A report-output truncation was followed only by bounded text reads. The initially supplied conventions path was corrected to briefs/conventions.md; readers documented when they read it. r2 left-note crop was not rotated; main used the already upright r1 crop. Reader inventories grouped states out of physical order; main interleaved them top-to-bottom. Main found a visible final ét accent missed by all three readers.',
 'adjudication_note':'r3 complete setting, with r1 fuller superseded-opening fragment, a retained pleine/quasi alternative, all three permitted upper-margin readings, resolved et after live G, added-and-cancelled explicitement, and main final ét. The left oval is integrated at mid-proof source coordinates. All C001–C032 and prior C questions have explicit outcomes. Seven C marks are resolved and twenty-five retained. H’s declared abridgment is acknowledged. One limited targeted proof check is recorded separately from documentary observations.'}
(R/'decisions/approved_scan025_config.json').write_text(json.dumps(cfg,ensure_ascii=False,indent=2)+'\n')
print('Approved configuration:',len(C),'changes;',sum(c['diff_c'] for c in C),'C;',sum(c['diff_h'] for c in C),'H;',len(viewed),'main crop views;',len(inv),'inventory elements')
