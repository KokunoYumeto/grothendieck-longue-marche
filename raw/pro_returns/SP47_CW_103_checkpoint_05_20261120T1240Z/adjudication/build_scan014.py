from pathlib import Path
import json, copy
R = Path(__file__).resolve().parents[1]
D = {w: json.loads((R/f'readers/scan014/{w}/report.json').read_text()) for w in 'ABC'}
cp = lambda n: f'readers/scan014/C/crops/c{n:02}.png'
ap = lambda n: f'readers/scan014/A/crops/c{n:02}.png'
mp = lambda name: f'crops/scan014/{name}.png'
cm = {0:cp(1),1:cp(2),2:cp(3),3:cp(3),4:cp(3),5:mp('main01_example_morphism'),6:mp('main02_hook'),7:mp('main03_R'),8:mp('main04_brace'),9:cp(4),10:cp(4),11:cp(4),12:cp(5),13:cp(5),14:cp(5),15:cp(5),16:cp(5),17:mp('main05_le_cas'),18:cp(6),19:cp(7),20:cp(7),21:cp(8),22:cp(8),23:cp(8),24:cp(8),25:cp(9),26:cp(10),27:cp(11),28:cp(12),29:cp(13),30:cp(13),31:mp('main06_courtcircuiter'),32:cp(14),33:cp(15),34:cp(16),35:cp(17),36:cp(18),37:ap(22),38:cp(20),39:cp(21),40:cp(22),41:cp(23)}
aix = [0,1,2,3,4,5,6,7,8,9,10,11,12,14,13,15,16,17,18,19,19,20,21,36,37,None,23,24,None,25,26,27,28,29,30,31,32,33,34,42,39,35]
bix = [0,1,2,3,3,4,5,6,7,8,8,9,10,10,11,12,13,14,15,16,17,18,20,19,21,22,23,24,None,25,26,27,28,29,30,31,32,33,34,None,None,None]
def candidate(w, i, fallback):
    return D[w]['changes'][i]['reading'] if i is not None else fallback
ov = {}
for i, row in enumerate(D['C']['changes']):
    af = r'\uline{Question pour Illusie}' if i == 25 else ('G (resolved in complete reading)' if i == 28 else 'No separate mark transcribed')
    bf = 'G (resolved in complete reading)' if i == 28 else 'No separate mark transcribed'
    ov[str(i)] = dict(crops=[cm[i]], scan_shows='Main independently inspected '+cm[i]+': '+row['scan_shows'], readers={'A':candidate('A',aix[i],af),'B':candidate('B',bix[i],bf),'C':row['reading']})
def upd(i, **kw): ov[str(i)].update(kw)
upd(1,final=r'\unsure{q|g}',scan_shows='Main C/c02, C/c03, C/c04, C/c05 and main01: a small bowl joins a long nearly straight descender. The foot is swollen or has only a short nib, with no secure leftward return. This favours q first, as A read it, but does not exclude g. The unequivocal long left return of prose g in C/c11 is different. Retain q/g at the first occurrence, with q thereafter under that reservation.',consequential='The morphism family is q/g, with q first on its long straight descender; the expected functor notation does not decide the identity.')
for i in [3,4,5,9,10,12,13]:
    final = D['C']['changes'][i]['reading'].replace('g/q','q/g').replace('g_*','q_*').replace('g^*','q^*')
    if i == 5: final = 'q (under first-occurrence q/g reservation)'
    upd(i,final=final,against_c=True,against_h=False,scan_shows='Main '+cm[i]+': the small bowl and long descending stem have no independently secure g return; use q under the first-occurrence q/g reservation. Each lower or upper star retains its observed position. This repeated first candidate agrees with H, while the reservation is recorded at the first occurrence.')
upd(2,scan_shows='Main C/c03: one horizontal shaft has a short upward end turn, but no separately identifiable lower arrowhead arm. Retain dash/arrow uncertainty. The clear two-arm arrow in C/c05 is a visual comparison, not a mathematical reason to complete this head.',consequential='The small relation after F remains dash/arrow; the mathematical kernel check explicitly assumes a unit map without repairing the source mark.')
upd(6,scan_shows='Main main02: the starting hook curves back above the shaft, which continues to a separate rightward head with two arms. The relation is a hooked arrow, not a subset sign.',consequential='The example has a hooked inclusion arrow U→e_Y, preserving its visible left hook.')
upd(7,scan_shows='Main main03: two distinct parallel upright strokes form the left of R, with the outer loop and descending right leg. The alphabet is doubled R.')
upd(8,scan_shows='Main main04: the brace starts below C and ends below F before the first closing parenthesis. Its two raised ends and lower central cusp are distinct; the label reads rés. inj. with both stops. H is credited for the label, but its note does not preserve the brace extent.')
upd(11,scan_shows='Main C/c04: a broad C-shaped open curve joins the upper star arm, followed by a clear C and another opener before F. Four closes follow F in the complete display. The first curve remains (/C; H’s alternative C(C(F)) would require an additional opener not separately visible. No delimiter is supplied.',against_h=True,marked_in_H='yes',consequential='The first display retains its (/C ambiguity and exact delimiter sequence; no extra opening parenthesis is inserted to satisfy the suggested formula.')
upd(14,scan_shows='Main C/c05: two overlapping bows and a crossing stroke occupy the opening position. The old smaller C-like bow cannot securely be separated as C rather than (. It is kept as cancelled material alongside the live opener.')
upd(15,scan_shows='Main C/c05: the old bowed stroke after F) is heavily crossed by reverse strokes, while a separate outer closing curve remains live. Retain cancelled )/C without merging it into the live close.')
upd(16,final=r'\deleted{\unsure{*|q_*}}',scan_shows='Main C/c05: crossing strokes and a terminal star-like fork survive, but no complete old bowl/descender is recoverable. Star comes first; q_* is retained as the alternative under the common q/g reservation. A and C preferred the star-like remnant, while B preferred a whole morphism.',consequential='The cancelled tail is retained as */q_*; only the star-like crossing is directly recoverable, so the whole morphism is not restored as certain.')
upd(17,scan_shows='Main main05: a tall looped l and a low e-like exit are followed by a white gap before cas. No independent s occurs. Read le.')
upd(18,confidence='high',scan_shows='Main C/c06: after the dotted i, the terminal e/r run and downturn end the word; there is no further s body. Read particulier.')
upd(19,scan_shows='Main C/c07: the last complete letter is a tall closed l loop. Its long lower exit does not form an independent s. Read actuel; A’s plural alternative is not retained.')
upd(20,scan_shows='Main C/c07: the continuous exit from l ends in a down-left hook. There is no detached comma, but a punctuation function for the joined hook remains possible. Retain no independent comma first, comma second; do not decide from the sentence structure.')
upd(21,final='ESt',against_c=True,confidence='high',scan_shows='Main C/c08: S has a full-height upper curve and a broad lower return, rising to E’s height and reaching its baseline. Its capital structure, not merely size, supports ESt. The case doubt is removed, agreeing with A and B.')
upd(22,scan_shows='Main C/c08: the mark above initial e is a compact upright oval, with no independently secure acute shaft. Preserve the literal dot-above-e first, with acute and no-accent alternatives. The separate i-dot is visible farther right.')
upd(23,scan_shows='Main C/c08: a dark point is detached below-left of the hyphen. C’s spatial underset places it there; A uses a different underset and B a subscript-like position. Preserve the point without giving it an index or punctuation function.')
upd(24,scan_shows='Main C/c08: a short near-vertical mark is detached high to the right of the question mark at about source (1069,1154). A and B use a margin wrapper; C’s high trailing placement is retained to reproduce the relation to the question. Textual status remains uncertain.')
upd(25,scan_shows='Main C/c09: the single rule starts under u, after Q, and its right end lies at the final i/e connector. Q is certainly outside. The endpoint favours exclusion of e but does not securely exclude its leading stroke. Keep C’s partial-underline uncertainty; neither A’s full underline nor B’s resolved endpoint is adopted.')
upd(26,scan_shows='Main C/c10: a round black baseline point stands between m and t, separated from both by white space; no a loop survives. Read déform.tions literally, without expansion.')
upd(27,scan_shows='Main C/c11: the final low run and slight return may carry an s, but no independent s body is secure. Keep groupes/groupe. The initial g has a long leftward returning descender, unlike the formula-letter family.')
upd(28,scan_shows='Main C/c12: the low subscript is a broad open curve with a short down-right spur. The spur favours G, but a clear inner G bar is absent. Keep G/C; A and B’s resolved G is not adopted.',consequential='The B subscript remains G/C. Its identity is not restored from the expected cohomological notation.')
upd(29,scan_shows='Main C/c13: a near-vertical left stem and two rightward arms favour K; a retraced X remains possible. Retain K/X, with no independent old layer or doubled alphabet.',consequential='The first Ext argument is K/X, K first, rather than an unqualified X.')
upd(30,confidence='medium',scan_shows='Main C/c13: a separate upper point is paired with a long lower comma-like stroke tapering left beneath the letter, and a second comma lies farther right. These support semicolon followed by comma, as B and C read. A’s underline-plus-point alternative is not retained; the unusual written separator sequence and empty argument remain.')
upd(31,scan_shows='Main main06: courtcir is written continuously before the line-end hyphen, with cuiter at the next line start. No internal hyphen follows court. Join the ordinary line division as courtcircuiter.')
upd(32,scan_shows='Main C/c14: the large initial G has a loop, internal return and bar, while r is small. No lowercase-g descender or extra doubled-alphabet stroke is present. Read ordinary capital Gr.')
upd(33,scan_shows='Main C/c15: one short horizontal stroke separates the phrases. The curve below belongs to next-line Picard’s P, not another dash or an arrow.')
upd(34,scan_shows='Main C/c16: two black curves/loops and a lower comma-like curl stand inside a white gap from the reproduction border. The three readers differ in schematic TikZ coordinates, not a recoverable lexical reading. Retain C’s left-margin shape approximation and uncertain textual status.')
upd(35,scan_shows='Main C/c17: an upright fragment, a detached slightly rising lower bar and a lower black point are separately visible inside the border. Retain C’s left-margin graphic approximation. No word, bracket or mathematical role is established.')
upd(36,scan_shows='Main C/c18: a right-bowing curve has endpoints near the left paper edge, inside the white margin. Retain its uncertain shape, without completing a letter or assigning a function.')
upd(37,final='Left-margin right-bowing curve plus separate lower point, in an uncertain TikZ approximation',place='Left edge beside the question ending near y=1200–1235',scan_shows='Main A/c22: the right-bowing curve is followed lower down by a distinct dark oval point at about y=1235. A includes both; B and C included the curve alone. Add the lower point to C’s shape approximation. The gray diagonal wash farther right does not support additional text.')
upd(38,scan_shows='Main C/c20: a thick irregular curved/triangular black trace and a smaller detached lower oval stand inside a white strip beside the dark border. Preserve their shape and point without assigning a word or punctuation function.')
upd(39,scan_shows='Main C/c21: one larger irregular black point and a smaller round point sit at approximately the same level below the faint gray rule. A and C retain them; B omitted them. Their physical presence is clear, but their textual function is uncertain.')
upd(40,scan_shows='Main C/c22: the dark irregular oval is separated by white space from the reproduction border near source y=813. A and C retained it, B did not. Preserve point/no-textual-character uncertainty.')
upd(41,scan_shows='Main C/c23: an upper short gray-dark hooked mark, a black central point with a descending trace, and a separate lower oval form a vertical cluster. A and C retained it; B did not. Preserve a graphic approximation without lexical reconstruction.')
extras = []
def extra(ai, crop, **kw):
    row=copy.deepcopy(D['A']['changes'][ai]);row['final']=row.pop('reading');row.pop('crop_ids',None)
    row.update(crops=[crop],marked_in_H='no');row.update(kw);extras.append(row);return row
theory = r'\unsure{th\.{e}orie|théorie|theorie}'
extra(22,ap(13),final=theory,readers={'A':D['A']['changes'][22]['reading'],'B':'théorie','C':'théorie'},scan_shows='Main A/c13: the mark above the first e is a compact high upright oval without an independently secure acute shaft. Preserve literal dot-above-e, acute, and no-accent alternatives, in that order; this does not deny the physical mark.',against_c=True,against_h=True,confidence='medium')
extra(38,ap(25),final=r'\unsure{\cdot|\phantom{\cdot}}',readers={'A':D['A']['changes'][38]['reading'],'B':'Omitted','C':'Omitted'},scan_shows='Main A/c25: a compact dark triangular/oval point lies in the paragraph gap at source (510,1240), separate from the surrounding gray traces. Preserve it at that gap near the page centre, not as a word or semantically attached punctuation.')
extra(40,ap(27),final='Two small left-boundary protrusions in an uncertain TikZ approximation',readers={'A':D['A']['changes'][40]['reading'],'B':'Omitted','C':'Omitted'},scan_shows='Main A/c27: two localized black protrusions partly meet the dark reproduction border: an upper short oblique form and a lower blob. Their physical shapes are visible, but independent pen/text origin is uncertain. Preserve a low-confidence shape/phantom alternative, without claiming letters or authorial intention.')
extra(41,ap(28),final=r'\margin{$\unsure{\cdot|\phantom{\cdot}}$}',readers={'A':D['A']['changes'][41]['reading'],'B':'Omitted','C':'Omitted'},scan_shows='Main A/c28: a small black upright oval lies inside white paper near source y=914, detached from the dark border. Retain point/no-textual-character uncertainty in the left margin.')
uns=[]
uref={0:0,1:1,2:2,3:11,4:14,5:15,6:16,7:20,9:22,10:23,11:24,12:25,13:27,14:28,15:29,16:34,17:35,18:36,19:37,20:38,21:41,22:40,23:39}
for i, orig in enumerate(D['C']['unresolved']):
    if i==8:continue
    u=copy.deepcopy(orig);u['evidence']=ov[str(uref[i])]['scan_shows']
    if i==1:u.update(reading=r'\unsure{q|g}',alternatives=['q','g'])
    if i==3:u['place']='First display, curve immediately after q_*q^*'
    if i==6:u.update(reading=r'\deleted{\unsure{*|q_*}}',alternatives=['star-like old sign','q with lower star, under the q/g reservation'])
    if i==19:u.update(place='Left curved fragment and lower point beside question ending',reading='Graphic curve-and-point approximation with phantom alternative')
    uns.append(u)
for row in extras:
    alternatives = ['dot above e','acute accent','no textual accent'] if row is extras[0] else ['visible unassigned shape or point','no textual character; physical source mark acknowledged']
    uns.append(dict(place=row['place'],reading=row['final'],alternatives=alternatives,confidence=row['confidence'],evidence=row['scan_shows']))
ci=copy.deepcopy(D['C']['inventory'])
for row in ci:
    row['first_words_or_objects']=row['first_words_or_objects'].replace('g_*g^*','q_*q^*').replace('g_*(g^*(F))','q_*(q^*(F))').replace('*/g_*','*/q_*')
ci[17].update(element='Left curve and lower point beside question ending',position='left edge; main inspected A/c22, source [13,1184,74,1252]',first_words_or_objects='right-bowing fragment and detached lower point near y=1235')
ci[12]['first_words_or_objects']='Dans sa '+theory+' des déform.tions ... J’ai; includes H^3 and Ext^2 and blank arguments'
ai=copy.deepcopy(D['A']['inventory'])
ai[13]['first_words_or_objects']=r'H^3(B_{\unsure{G|C}}/X,\quad)'
ai[14]['first_words_or_objects']=r'\operatorname{Ext}^2(\unsure{K|X};,\quad); no underline imposed'
inv=[ci[0],ci[13],ci[1],ci[2],ci[3],ci[19],ci[4],ci[14],ci[5],ci[6],ci[7],ci[8],ci[9],ci[15],ai[28],ci[10],ci[16],ci[21],ci[20],ci[17],ai[25],ci[11],ai[27],ci[12],ci[18],ai[13],ai[14],ai[15],ci[23],ci[22]]
notation=copy.deepcopy(D['C']['notation'])
for row in notation:
    row['latex']=row['latex'].replace('g|q','q|g').replace('g_*','q_*').replace('g^*','q^*')
notation[1].update(sign='q/g',ink=ov['1']['scan_shows'],latex=r'\unsure{q|g};\quad q')
notation[13].update(sign='Capital S and high e point',ink=ov['21']['scan_shows']+' '+ov['22']['scan_shows'],latex=r'ESt;\quad\unsure{\.{e}vident|évident|evident}')
notation[17]['ink']=ov['29']['scan_shows']+' '+ov['30']['scan_shows']
notation.append(dict(place='First théorie after the rubric',sign='high mark over e',ink=extras[0]['scan_shows'],latex=theory))
notation.append(dict(place='Additional gap and left-edge marks',sign='unassigned points and boundary shapes',ink='Main A/c22, A/c25, A/c27 and A/c28 preserve the additional lower point, gap point, two boundary shapes and y=914 point. Their textual status is not inferred from physical presence.',latex=r'\unsure{\cdot|\phantom{\cdot}}; uncertain TikZ approximation'))
text=(R/'readers/scan014/C/reading.tex').read_text()
subs=[]
def sub(old,new,count=1):subs.append(dict(old=old,new=new,count=count))
sub(r'\unsure{g|q}',r'\unsure{q|g}')
sub(r'g_{*}',r'q_{*}',text.count(r'g_{*}'))
sub(r'g^{*}',r'q^{*}',text.count(r'g^{*}'))
sub('$g$','$q$')
sub(r'\unsure{ESt|Est}','ESt')
sub('Dans sa théorie des','Dans sa '+theory+' des')
old=r'\draw (0,3) .. controls (3,1) and (3,-2) .. (0,-3);'+'\n'+r'\end{tikzpicture}|\phantom{\rule{2mm}{3mm}}}'
new=r'\draw (0,3) .. controls (3,1) and (3,-2) .. (0,-3);'+'\n'+r'\fill (0,-9) ellipse (.25 and .4);'+'\n'+r'\end{tikzpicture}|\phantom{\rule{2mm}{5mm}}}'
sub(old,new)
sub('catégorie dérivée) p. r. à la flèche dont on veut prendre le cône.', 'catégorie dérivée) p. r. à la flèche dont on veut prendre le cône.\n% Detached left-margin point near source y=914; textual status uncertain.\n'+r'\reversemarginpar'+'\n'+r'\margin{$\unsure{\cdot|\phantom{\cdot}}$}'+'\n'+r'\normalmarginpar')
heading=r'\unsure{Q\uline{uestion pour Illusi}e|Q\uline{uestion pour Illusie}}'
prefix=r'''% Isolated point in the gap above the rubric, source (510,1240).
\noindent\hspace{.43\linewidth}$\unsure{\cdot|\phantom{\cdot}}$\par
% Two small boundary shapes beside the rubric underline; pen origin uncertain.
\reversemarginpar
\margin{\figure{\unsure{\begin{tikzpicture}[x=.4mm,y=-.4mm,line width=.5pt,line cap=round]
\draw (0,0)--(2,1.2);
\fill (1,12) circle (.8);
\end{tikzpicture}|\phantom{\rule{2mm}{6mm}}}}}
\normalmarginpar
'''
sub(heading,prefix+heading)
pending=json.loads((R/'adjudication/scan014_pending_checks.json').read_text())
events=copy.deepcopy(pending['events'])
for e in events:e['date']=pending['performed_utc']
events[0]['outcome']='For this check only, interpret the doubtful dash/arrow as the unit map. The calculation uses g as an abstract morphism name; the transcription retains q/g from the ink. '+events[0]['outcome']
events.append(dict(statement_id='S014.N5.examples_and_deformation_question',type='carried as background without fault found',outcome='The open-inclusion example, the references to Illusie’s deformation theory and its H^3/Ext^2 groups, and the proposed shortcut through Gr-champs or champs de Picard were transcribed without proof or external research. The source explicitly says supposée écrite and asks a question. No conclusion about absent continuation elsewhere in the dossier is adopted.'))
seen=set(cm.values())|{e['crops'][0] for e in extras}
config=dict(scan=14,folder='H103-02',filename='H103-02_103_scan014.tex',brief='brief_v11.md',base='C',adjudicated=True,inspected_crops=sorted(seen),change_overrides=ov,extra_changes=extras,substitutions=subs,unresolved=uns,inventory=inv,sheet_kind='letter',notation=notation,abbreviations=D['C']['abbreviations'],check_events=events,notes=[
'[S014.N1] This wholly handwritten continuation gives case b), discusses the cone construction, and ends with a Question pour Illusie. There is no new date, title, salutation, signature, author page number or total page count. The separate archive-pencil number is 13; the main hand remains unnamed. The last words are J’ai, without a completion on this leaf. H’s editorial statement about continuation elsewhere in the dossier is not adopted.',
'[S014.N2] Case b) states that for injective F on the faintly written Y, pullback remains injective and the written relation from F to the image-pullback object is an epimorphism; an open-inclusion example follows. The recurring letter is q/g, q first here, with low and high stars distinguished. The relation after F has one shaft and a short upturn, so dash/arrow remains uncertain. The first display has doubled R, an underbrace ending before the first close, and the label rés. inj. Its C-shaped opener remains (/C, and the exact closing sequence is retained.',
'[S014.N3] A restricted kernel calculation was actually checked. Interpret the epimorphism condition as a unit-map assumption, take an abelian sheaf F and a bounded-below injective resolution I on Y, and assume that each g^*I^n is injective and I^n→g_*g^*I^n is epic. Exactness of g^* makes g^*I an injective resolution, and its right adjoint g_* preserves injectives. Thus K=ker(I→g_*g^*I) fits 0→K→I→g_*g^*I→0, giving K→F→Rg_*g^*F→K[1]. RΓ_Y(K) is the relative fibre model in this restricted sheaf case, with no extra [-1] on the kernel. This checks the kernel placement, not a functorial choice on bare derived categories, the open-inclusion example or an unbounded extension. The source’s doubtful relation and q/g reading are unchanged by this interpretation.',
'[S014.N4] The page says that taking the cone is not functorial in the derived category relative to the arrow. A limited elementary check establishes nonuniqueness of a cone-map completion: for X=k[-1], Y=k and f=0 over a field, Cone(f)=k⊕k, and (y,x)↦(y+a x,x) for a=0 and a=1 gives distinct automorphisms preserving the inclusion and projection. Both complete the same identity square. This does not prove the impossibility of every global choice of cone functor. The author’s own qualification is retained: il devrait y avoir un choix fonctoriel, followed by ESt-ce and the accent-doubtful évident ? The special-case question is not answered by this check.',
'[S014.N5] The question to Illusie concerns déform.tions of flat group schemes, H^3(B_{G/C}/X, blank) and Ext^2(K/X ; , blank), and asks about a shortcut using the theory, explicitly supposée écrite, of Gr-champs, respectively champs de Picard. The empty slots are not filled. The small B subscript and Ext letter remain doubtful; the long lower comma stroke and its upper point support a semicolon followed by a separate comma. The prose spelling courtcircuiter joins an ordinary line division without adding an internal hyphen. These deformation-theoretic references were not researched or proved.',
'[S014.N6] Visual decisions resolve ESt, singular le cas particulier actuel, the abbreviation déform.tions and capital Gr. The joined flourish after actuel still permits a comma function. Dot/acute/no-accent alternatives are preserved over the initial e of évident and the first e of théorie. The heading rule excludes Q and has an uncertain right endpoint near the final i/e. Cancelled opener, close and tail are separated from the live middle formula; the tail favours a surviving star over a reconstructed whole morphism.',
'[S014.N7] Three complete independent readings and all difference lists were compared. Main inspected twenty-two retained C crops (c01–c18 and c20–c23), five retained A crops (c13, c22, c25, c27, c28), and six new crops for half-settled differences: thirty-three distinct crops. The failed display of C/c20 was redelivered from the same file before the decision; it was not recropped. Main viewed no whole image or half. Twenty-seven loci remain unresolved. Marginal fragments, extra points and the two boundary protrusions are retained with uncertain textual status; physical presence does not establish authorial intent. The faint gray rule and gray wash are not reconstructed as text.',
'[S014.N8] Reader A attempted a standalone pdflatex compilation, which could not start because pdflatex.fmt was missing. No PDF was generated or visually checked. Its report and working records are retained honestly. The main workflow uses syntax and integrity checks only; the next brief explicitly forbids compilation attempts. This tooling event is not a mathematical check or an additional scan reading.'
])
(R/'adjudication/scan014.json').write_text(json.dumps(config,ensure_ascii=False,indent=2)+'\n')
print('Config',len(ov)+len(extras),'rows;',len(uns),'doubts;',len(inv),'inventory;',len(seen),'main crops')
