from pathlib import Path
import json,copy
R=Path(__file__).resolve().parents[1]
D={l:json.loads((R/'readers/scan011'/l/'report.json').read_text()) for l in 'ABC'}
cp=lambda n:f'readers/scan011/C/c{n:02}.png'
m=lambda s:'crops/scan011/'+s+'.png'
a6='readers/scan011/A/c06.png'
cm={0:cp(1),1:cp(1),2:cp(2),3:cp(3),4:cp(4),5:cp(4),6:cp(12),7:cp(5),8:m('main01_universel_quotes'),9:a6,10:a6,11:cp(6),12:cp(6),13:m('main02_remonte_dash'),14:m('main02_remonte_dash'),15:m('main03_ensembliste_quotes'),16:m('main04_provient_quotes'),17:cp(7),18:cp(9),19:cp(10),20:cp(10),21:cp(8)}
ov={str(i):{'crops':[v]} for i,v in cm.items()}
for i in range(22):ov[str(i)]['scan_shows']='Main independently inspected '+cm[i]+': '+D['C']['changes'][i]['scan_shows']
def readers(i,a,b,c):ov[str(i)]['readers']={'A':a,'B':b,'C':c}
readers(1,D['A']['changes'][1]['reading'],D['B']['changes'][1]['reading'],D['C']['changes'][1]['reading'])
ov['1']['scan_shows']='Main C/c01: the raised replacement has a surviving c-like initial, tall h, pale middle traces, p descender and last s. The a/m joins are substantially faded and do not justify B’s fully resolved word. Retain champs under uncertainty.'
readers(2,D['A']['changes'][2]['reading'],D['B']['changes'][2]['reading'],D['C']['changes'][2]['reading'])
ov['2'].update(kind='misread word',scan_shows='Main C/c02: the interior between dotted-i region and descending g retains a short detached horizontal trace, with no secure n shoulder. Prefer épi-glés, retaining épinglés because much of the line is faded. C/c11 separately shows the clear n shoulder in the later singular épinglé; that clearer occurrence does not fill this one.')
readers(5,'Comma only; no independent high point recorded.','Comma only; no independent high point recorded.',D['C']['changes'][5]['reading'])
ov['5']['scan_shows']='Main C/c04: the clear low comma has a separate short dark point above-left, near the height of the L stem. Preserve the upper mark independently, with uncertain textual status; it could make the punctuation semicolon-like, but no semantic role is imposed.'
hook=r'{}^{\unsure{\text{,}|?|\phantom{?}}}\!N'
ov['6'].update(final='M,'+hook,scan_shows='Main C/c12: a short dark hook has a broad head and a descending leftward tail above-left of N; a smaller, lighter point lies below. The upper hook most directly resembles a raised comma, while a question-mark-like unit with the lower spot and a nontextual trace remain alternatives. It is detached from N and is not assigned a mathematical exponent meaning.')
readers(6,'M,N; no independent high mark.','M,N; no independent high mark.',D['C']['changes'][6]['reading'])
ov['8']['scan_shows']='Main main01: two high pen strokes precede universel and two follow its final l. No angled guillemet shapes occur.'
ov['9'].update(scan_shows='Main A/c06: a rounded left loop crosses into an oblique right tail, forming alpha. There is no opening parenthesis and no radiating asterisk.',consequential='Restore the source’s extension label α in place of H’s sequence reference (*); retain the separately written comma after it.')
ov['10']['scan_shows']='Main A/c06: a distinct curved descending stroke follows alpha before est. It is the separate comma recorded by all three readers, not a second component of an asterisk label.'
ov['13']['scan_shows']='Main main02: re is followed by a low joined m/o/n group, then a tall crossed t and a final e. There is no tall l or accented è at the position required by relève. Read remonte.'
ov['14']['scan_shows']='Main main02: a single short horizontal stroke, roughly a small-letter width, separates remonte from en. Preserve the short dash rather than an em dash.'
ov['15']['scan_shows']='Main main03: both ends of ensembliste carry two raised strokes. The low black stop after the closing pair is separate.'
ov['16']['scan_shows']='Main main04: two high narrow strokes occur on either side of provient; they are not angular guillemets.'
hfirst=r'{\unsure{\mathcal H|\mathscr H}}^{2}'
ov['17'].update(final=hfirst,against_c=False,scan_shows='Main C/c07: H has a lower-left loop, upper-right loop and transverse joining stroke, with a separate raised 2. It has no doubled parallel uprights. Both permitted script fonts approximate this calligraphic pen form; retain mathcal H first with mathscr H as the explicit alternative, rather than claiming the crop uniquely fixes a print font.')
readers(17,D['A']['changes'][14]['reading'],D['B']['changes'][15]['reading'],D['C']['changes'][17]['reading'])
ov['18']['scan_shows']='Main C/c09: one short detached oblique stands high at E’s right; the next oblique continues down into the opening parenthesis. No numeral-1 foot or full long upright occurs. Resolve E prime.'
ov['19']['scan_shows']='Main C/c10: a pale curved trace with a darker right tip lies below/right of the outer closing parenthesis, separate from the high dark point. Its comma-like shape is visible but its much lighter tone leaves a nontextual-trace alternative. Preserve comma first, with uncertain textual status.'
ov['20']['scan_shows']='Main C/c10: the upper black point survives fully inside the right edge, well above the distinct low curve. Preserve the point first at its actual height; a nontextual spot remains possible. The phantom alternative concerns its textual status, not whether the physical spot exists.'
readers(20,D['A']['changes'][17]['reading'],D['B']['changes'][18]['reading'],D['C']['changes'][20]['reading'])
ov['21'].update(final=r'\mathcal H^{2}',against_c=False,scan_shows='Main C/c08: the repeated H again has a lower-left and upper-right loop connected across the middle. Use the first candidate from the preceding uncertain script rendering; there are no blackboard-bold double uprights. Raised 2, closing parenthesis and separate final stop are clear.')
readers(21,D['A']['changes'][18]['reading'],D['B']['changes'][19]['reading'],D['C']['changes'][21]['reading'])
uns=copy.deepcopy(D['C']['unresolved'])
uns[5].update(reading=hook,alternatives=['raised comma-like hook','question-mark-like hook and lower point','nontextual trace'],evidence=ov['6']['scan_shows'])
uns[7].update(reading=r'\unsure{\mathcal H|\mathscr H}',alternatives=[r'\mathcal H',r'\mathscr H'],evidence=ov['17']['scan_shows'])
for u in uns:
 if u['evidence'].startswith('c'):u['evidence']='Reader C/'+u['evidence']+' Main independently inspected the retained crop(s).'
inv0=copy.deepcopy(D['C']['inventory']);inv=[inv0[i] for i in [0,2,1,*range(3,15)]]
for row in inv:
 row['sheet_kind']='letter'
 if row['element']=='Detached high hook/spot with uncertain textual status':row['first_words_or_objects']='raised comma-like / question-mark-like / nontextual trace'
notation=copy.deepcopy(D['C']['notation'])
notation[8].update(ink=ov['17']['scan_shows']+' The repeated form is checked in C/c08.',latex=hfirst+r';\quad\mathcal H^2')
notation[13].update(ink=ov['6']['scan_shows'],latex=hook)
events=copy.deepcopy(json.loads((R/'adjudication/scan011_pending_checks.json').read_text())['events'])
events.append({'statement_id':'S011.N2.realization_obstruction_lifting','type':'carried as background without fault found','outcome':'The author’s qualified realization claim, Ext^3 obstruction and claimed universal vanishing argument, objectwise lifting/ensembliste-section assertion, and stronger hypercohomology-origin assertion were transcribed. Their proofs are not given on this page and were not supplied in this run. The distinct limited symmetry calculation is recorded in S011.N3; it does not establish these stronger claims.'})
subs=[(r'{}^{\unsure{?|\text{,}|\phantom{?}}}\!N',hook),(r'{\unsure{\mathscr H|\mathcal H}}^{2}',hfirst),(r'(hypercohomologie $\mathscr H^{2}$)',r'(hypercohomologie $\mathcal H^{2}$)')]
c={'scan':11,'folder':'H103-02','filename':'H103-02_103_scan011.tex','brief':'brief_v09.md','base':'C','adjudicated':True,'inspected_crops':sorted(set(cm.values())|{cp(11)}),'change_overrides':ov,'substitutions':[{'old':a,'new':b} for a,b in subs],'unresolved':uns,'inventory':inv,'sheet_kind':'letter','notation':notation,'abbreviations':D['C']['abbreviations'],'notes':[
'[S011.N1] This wholly handwritten continuation completes the phrase begun at the end of scan010. One continuous paragraph carries a cancelled opening noun with a raised replacement, two further interlinear insertions, two later cancellations, and inline formulas. There is no new title, date, salutation, signature, author page number or total. The lower-left archive numeral is 10. The hand remains unnamed. H’s note about another dossier is not used as evidence from this sheet.',
'[S011.N2] Sigma is described through the symmetry of L tensor L, viewed as a section of the written left-subscript-2 N. Je sais prouver (sauf erreur) qualifies the claim that every indicated homomorphism comes from a suitable Picard champ. The author places an a priori obstruction in Ext³(X;M,N) and says an argument universel proves it zero. He then calls the extension α close to split, says tte section over an arbitrary object se remonte, paraphrases this as an ensembliste section, and asserts better provenance from the degree-two hypercohomology expression. These are separate source claims. The page gives neither the universal argument nor a proof of the final lifting assertion; no natural splitting is inferred merely from the displayed exact sequence on scan010.',
'[S011.N3] Limited calculation used and rechecked: for a symmetry with the usual involutivity axiom, c(L,L) composed with itself is the identity on L tensor L. Under the Picard translation identification of its automorphism sheaf with additive N, the corresponding n satisfies n+n=0. This explains the compatibility with a 2-torsion target, conditional on that notation convention. It does not prove additivity in L, the realization of every M→N[2], the obstruction’s vanishing, or the hypercohomology claim. The calculation did not change any source glyph.',
'[S011.N4] The extension label is the visible loop-and-tail α, followed by its own comma; H’s (*) is not restored from the preceding sequence label. The source abbreviation tte and verb remonte are preserved. Sigma and E prime are resolved from their strokes, and the a of a priori has no detached grave. The two hypercohomology H glyphs are looped calligraphic/script forms, not doubled upright H. The first keeps mathcal/mathscr uncertainty and the second uses its first candidate.',
'[S011.N5] The opening cancelled catégories/catégorie ending and the middle letters of raised champs remain too faint for certainty. The first adjective favours épi-glés but keeps épinglés as an alternative; the later singular épinglé has an actual n shoulder. The latter was checked on its own crop and was not used to complete the first. Cancelled K/L and u/un remain uncertain. Every ordinary insertion hook is represented at its attachment, not as a detached figure.',
'[S011.N6] Small marks are preserved at their physical positions: an uncertain high point over the comma after L tensor L; an uncertain comma-like/question-mark-like hook above-left of the N in the épinglé parenthesis; and a high dark point separate from a lower pale comma-like curve after the final formula. No semantic exponent, doubt about the mathematics, or layer membership is inferred for the hook. The final marks cannot be treated as one comma/full-stop alternative because both survive separately. Phantom alternatives denote uncertain textual status, not absence of the physical marks.',
'[S011.N7] All three fresh readers completed the whole/half_a/half_b sequence and local crop work. Main compared every complete return and inspected twelve C crops, A/c06 for alpha and its comma, and four new crops for half-settled quotation/verb/dash differences: seventeen distinct crops. No source whole or half was viewed by main. Ten loci remain unresolved. The v09 locator clarification worked: all uncropped witness differences had usable retained boxes, with no new image-location follow-up needed. No additional brief revision was needed after this page.'
],'check_events':events}
(R/'adjudication/scan011.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n')
print('Config:',len(ov),'rows;',len(uns),'doubts;',len(inv),'inventory;',len(c['inspected_crops']),'main crops')
