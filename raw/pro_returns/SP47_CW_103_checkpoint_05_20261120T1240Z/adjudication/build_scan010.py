from pathlib import Path
import json,copy
R=Path(__file__).resolve().parents[1]
D={l:json.loads((R/'readers/scan010'/l/'report.json').read_text()) for l in 'ABC'}
cp=lambda n:f'readers/scan010/C/c{n:02}.png'
m=lambda s:'crops/scan010/'+s+'.png'
cm={0:cp(1),1:m('main01_overbrace'),2:cp(2),3:cp(3),4:cp(3),5:m('main02_open_quote'),6:cp(4),7:cp(4),8:cp(5),9:m('main03_ta_theorie'),10:cp(6),11:cp(7),12:cp(8),13:cp(9),14:cp(10),15:cp(11),16:cp(11),17:cp(12),18:cp(13),19:cp(13),20:cp(14),21:cp(15),22:cp(15),23:m('main04_equivalence_quotes')}
ov={str(i):{'crops':[v]} for i,v in cm.items()}
def readers(i,a,b,c):ov[str(i)]['readers']={'A':a,'B':b,'C':c}
for i in range(24):
 ov[str(i)]['scan_shows']='Main independently inspected '+cm[i]+': '+D['C']['changes'][i]['scan_shows']
ov['1']['scan_shows']='Main main01: an upward central cusp and downward outer ends form a brace above H²(E′(M,N)); P(M,N) is above that brace. H’s underbrace placement is reversed.'
ov['5']['scan_shows']='Main main02: two separate short high strokes precede the baseline 2. They are double quotation strokes, with no angled guillemet.'
ov['9']['scan_shows']='Main main03: the first letter has an upright crossed near its lower part and a hooked foot, followed by a low joined a before the tall initial of théorie. Read ta, not la.'
ov['23']['scan_shows']='Main main04: two high narrow strokes precede équivalence, and a joined but visibly paired high mark follows its final e. Neither boundary is a guillemet.'
oldN=r'\deleted{\unsure{\phantom{M}|M|N}}'
ov['3'].update(final=oldN,scan_shows='Main C/c03: heavy uprights and diagonal strokes overlap, but no independent old letter can be isolated. Prefer no independent underlying character, retaining old M and N alternatives. The phantom denotes uncertainty about a separate textual layer, not absence of the visible heavy strokes.')
readers(3,D['A']['changes'][3]['reading'],D['B']['changes'][3]['reading'],D['C']['changes'][3]['reading'])
readers(4,D['A']['changes'][4]['reading'],D['B']['changes'][3]['reading'],D['C']['changes'][4]['reading'])
readers(6,D['A']['changes'][6]['reading'],D['B']['changes'][4]['reading'],D['C']['changes'][6]['reading'])
ov['6']['scan_shows']='Main C/c04: the high crossed group contains two short upper stubs, favouring an old double quote; cancellation merges the lower body enough to leave s possible. The struck state is clear; A’s resolution of the old shape is not adopted.'
readers(8,D['A']['changes'][8]['reading']+'; '+D['A']['changes'][9]['reading'],D['B']['changes'][6]['reading'],D['C']['changes'][8]['reading'])
under=r'\unsure{str\uline{ict}s|st\uline{rict}s}'
ov['11'].update(final=under,against_c=True,scan_shows='Main C/c07: the single line begins under the joined r/i region and ends beneath the final t, excluding initial st and terminal s. ict is the closest span, but the right part of r overlaps the starting endpoint; retain A’s ict/rict uncertainty.')
readers(11,D['A']['changes'][12]['reading'],D['B']['changes'][9]['reading'],D['C']['changes'][11]['reading'])
readers(16,D['A']['changes'][17]['reading'],D['B']['changes'][14]['reading'],D['C']['changes'][16]['reading'])
article=r'$\deleted{\unsure{\mathrm{d}|\mathrm{l}}}\overset{\unsure{\cdot|\phantom{\cdot}}}{\deleted{\mathrm{e}}}$'
ov['17'].update(final=r'\deleted{\unsure{de|le}} (letters positioned separately in the transcription to place the uncertain point over e)',against_c=True,scan_shows='Main C/c12: a low left loop and tall returning ascender favour d, followed by the shared e. The cancellation crosses the lower joins and prevents exclusion of le. Both letters remain deleted. The independent point over e is dealt with separately, without assigning it to the deleted layer.')
readers(17,D['A']['changes'][18]['reading'],D['B']['changes'][15]['reading'],D['C']['changes'][17]['reading'])
readers(20,D['A']['changes'][21]['reading'],D['B']['changes'][19]['reading'],D['C']['changes'][20]['reading'])
readers(22,D['A']['changes'][23]['reading'],D['B']['changes'][21]['reading'],D['C']['changes'][22]['reading'])
ov['21']['scan_shows']='Main C/c15: the old crossed group retains a low round loop and a higher stem with a possible short detached apostrophe. d\' is preferred, but cancellation also allows à. The live raised à is distinct from this old group.'
ov['22']['scan_shows']='Main C/c15: the raised à has a closed body and detached accent; its long hook ends on the baseline to the left of the cancelled old group. Place the insertion before that group, as B and C do, rather than after it as A and witness C do.'
point={'place':'Detached point above the cancelled article’s e region','c':'Not represented','h':'Not represented','final':r'\overset{\unsure{\cdot|\phantom{\cdot}}}{\deleted{\mathrm{e}}}', 'scan_shows':'Main C/c12: one isolated dark point sits above the right-hand e region, separate from the crossing strokes. Preserve its physical position with uncertain textual status. The point is outside the deleted wrapper so that its membership in an old or live layer is not asserted. The phantom alternative concerns textual status, not the physical spot.','confidence':'low','kind':'other','marked_in_H':'no','against_c':True,'against_h':True,'crops':[cp(12)],'readers':{'A':'No independent point represented.','B':D['B']['changes'][16]['reading'],'C':'No independent point represented.'}}
degree=r'i\unsure{\ne|+}2'
sign={'place':'Opening third line, degree relation after i','c':'i+2','h':'i+2','final':degree,'scan_shows':'Main main05: after the dotted i there is a long upper horizontal stroke and a shorter lower horizontal stroke, separated by a visible white gap at the right, crossed by a near-vertical stroke. Two bars favour ≠ over a single-bar plus; the compressed central join permits + as an alternative. The crop was prompted by the degree calculation, but the preferred reading is based on these two bars.','confidence':'medium','kind':'misread symbol or index','marked_in_H':'no','against_c':True,'against_h':True,'crops':[m('main05_degree')],'readers':{'A':'i+2','B':'i+2','C':'i+2'},'consequential':'Both witnesses and all three readers gave i+2. The main crop favours i≠2, with i+2 retained as an in-place alternative. This changes a putative degree shift to an exception at degree 2 without silently resolving the compressed sign.'}
uns=copy.deepcopy(D['C']['unresolved'])
uns[0].update(reading=oldN,alternatives=['no independent underlying letter','old M','old N'],evidence=ov['3']['scan_shows'])
uns[4].update(reading=r'\deleted{\unsure{de|le}}',alternatives=['de','le'],evidence=ov['17']['scan_shows'])
for u in uns:
 if u['evidence'].startswith('c'):u['evidence']='Reader C/'+u['evidence']+' Main independently inspected this retained crop.'
uns.insert(0,{'place':sign['place'],'reading':degree,'alternatives':['i≠2','i+2'],'confidence':'medium','evidence':sign['scan_shows']})
uns.insert(4,{'place':'Underline endpoint in stricts','reading':under,'alternatives':['ict underlined','rict underlined'],'confidence':'medium','evidence':ov['11']['scan_shows']})
uns.insert(7,{'place':point['place'],'reading':r'\unsure{\cdot|\phantom{\cdot}}','alternatives':['textual point of uncertain layer','nontextual physical spot'],'confidence':'low','evidence':point['scan_shows']})
inv0=copy.deepcopy(D['C']['inventory']);inv=[]
for i in [0,3,1,2,*range(4,16)]:
 row=inv0[i]
 if i==5:row['first_words_or_objects']='no independent underlying letter / old M / old N'
 if i==10:row['first_words_or_objects']='stricts with ict / rict underlined'
 if i==12:row['first_words_or_objects']='de / le'
 inv.append(row)
 if i==12:inv.append({'sheet_kind':'letter','hand':'unnamed mark; textual status uncertain','element':'Isolated point over cancelled article','kind':'text','position':'above e region, approximately x=213, y=1540','first_words_or_objects':'point / nontextual spot; old-layer attachment uncertain','transcribed':'yes'})
notation=copy.deepcopy(D['C']['notation'])
notation[2].update(sign='i≠2 / i+2; degree 2',ink=sign['scan_shows'],latex=degree+'; 2')
notation[8].update(ink=ov['3']['scan_shows']+' Live N retains ordinary/doubled-alphabet doubt.',latex=oldN+r'\unsure{N|\mathbb{N}}')
notation[11].update(ink=ov['11']['scan_shows'],latex=under)
notation.append({'place':point['place'],'sign':'isolated point','ink':point['scan_shows'],'latex':point['final']})
events=copy.deepcopy(json.loads((R/'adjudication/scan010_pending_checks.json').read_text())['events'])
events.append({'statement_id':'S010.N4.heuristic_interpretation','type':'carried as background without fault found','outcome':'The 2-champ interpretation, extension of the theory from strict 1-champs, and canonical construction of the displayed extension were transcribed as source claims. The source’s Heuristiquement, en admettant and ce qui pour moi ne fait guère de doute remain explicit; none of those constructions was proved in this run.'})
sub=[('i+2',degree),(r'\deleted{\unsure{M|N|\phantom{M}}}',oldN),(r'str\uline{ict}s',under),(r'\deleted{\unsure{le|de}}',article)]
c={'scan':10,'folder':'H103-01','filename':'H103-01_103_scan010.tex','brief':'brief_v08.md','base':'C','adjudicated':True,'inspected_crops':sorted(set(cm.values())|{m('main05_degree')}),'change_overrides':ov,'extra_changes':[point,sign],'substitutions':[{'old':a,'new':b} for a,b in sub],'unresolved':uns,'inventory':inv,'sheet_kind':'letter','notation':notation,'abbreviations':[{'form':'épi-glés','expansion':'Possible shortened or interrupted spelling of épinglés; the actual internal dash is retained and no expansion is made in the text.'}],'notes':[
'[S010.N1] This fully handwritten continuation begins donc and ends unfinished at près des. It contains an opening paragraph, a labelled exact-sequence display, a heuristic paragraph with two interlinear insertions, and the beginning of a final paragraph. A lighter archive numeral 9 appears below; no title, new date, salutation, signature, author page number or page total is present. The pen and pencil hands remain unnamed.',
'[S010.N2] The page relates the invariants of E′(M,N) to those of E(M,N), then states a degree-2 exact sequence 0→underlined Ext²(M,N)→P(M,N)→underlined Hom(M,₂N)→0. The middle identification P(M,N) is above the term under an overbrace. Sigma is resolved from its loop and long top stroke. The relation after i is newly uncertain: both witnesses and all three readers gave i+2, whereas the main crop shows two short separated horizontal bars crossed by a near-vertical stroke and favours i≠2. The transcription keeps ≠ first and + as an explicit alternative.',
'[S010.N3] Limited conditional check: if E has cohomology only in degrees 0,1,2, Q is a sheaf in degree zero, and the intended distinguished triangle is E→E′→Q[-2]→E[1], its long cohomology sequence gives H^i(E)≅H^i(E′) for i≠2 and 0→H²(E)→H²(E′)→Q→0. Q[-2] has only degree-2 cohomology, and the adjacent degree-1 and degree-3 terms vanish. Identifying H²(E) with Ext² gives the shape of the displayed extension. This prompted inspection of the degree sign; it does not settle an ambiguous stroke, construct the triangle, identify the written left-subscript 2, or prove canonicity. S009.N4 used a different explicitly conditional rotation. The preceding unlabelled cyclic picture does not identify the degree-one connecting edge by itself, so that earlier conditional calculation is not a source contradiction.',
'[S010.N4] The interpretation is introduced by Heuristiquement and assumes en admettant que ta théorie for strict 1-champs extends to strict 2-champs, adding ce qui pour moi ne fait guère de doute. The last paragraph separately asserts that the exact sequence is constructed en tous cas canoniquement, quoted à la main, and begins the description of the middle sheaf up to equivalence. These statements retain their original force and qualifications; no construction or equivalence theorem was proved here.',
'[S010.N5] Two occurrences have a detached dash after the dotted i and read épi-glés literally. The lower return is the g descender, not an underline. The lower stricts has an underline confined to the middle, with ict/rict endpoint uncertainty. The final word in en tous cas ends in the same long low s-like hook as cas, so C’s tout is changed to tous. The colon after donne lieu, correspond, canoniquement, terme and médian are resolved from the retained crops. Four quotation spans use paired high strokes, not guillemets.',
'[S010.N6] The heavy N is retained with both a no-independent-old-letter/M/N doubt and an ordinary/doubled-live-N doubt. The cancelled high mark before strict remains quotation strokes/s. The curve after à la main remains comma/closing parenthesis; there is only one independent mark. The cancelled article favours de over le; an isolated point is placed physically over its e, without forcing it into a deleted layer. classes/choses and the cancelled preposition d′/à remain uncertain. The raised live à hook meets the baseline before the cancelled preposition, fixing its insertion location.',
'[S010.N7] Three fresh isolated readers each viewed whole, half_a and half_b once, then their unresolved local crops. Main compared all complete returns and personally inspected fifteen C crops and five new crops: twenty distinct adjudication crops. The initial delivery of C15 and main01 was truncated before their images appeared; the same files were then delivered and inspected successfully, with no recrop. Ten loci remain uncertain. No whole page or half was viewed by the main reader.'
],'check_events':events}
(R/'adjudication/scan010.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n')
print('Config:',len(ov)+2,'rows;',len(uns),'doubts;',len(inv),'inventory;',len(c['inspected_crops']),'main crops')
