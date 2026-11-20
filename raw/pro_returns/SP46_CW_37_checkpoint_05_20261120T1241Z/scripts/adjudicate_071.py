from pathlib import Path
import json,copy
O=Path(__file__).resolve().parents[1]
R={a:json.loads((O/f'readers/scan071/{a}/report.json').read_text()) for a in 'ABC'}
A,B,C=[R[a]['decisions'] for a in 'ABC']
# Mandatory rows only: witness differences, explicit C doubts and new uncertainties.
ci=[0,8,9,10,11,12,14,15,16]
ai=[0,None,1,None,2,3,4,5,6]
bi=[0,None,2,3,4,5,7,8,9]
ds=[]
for k,j in enumerate(ci):
 d=copy.deepcopy(C[j]);d['id']=f'M071-{k+1:02}'
 d['readers']={'A':A[ai[k]]['reading'] if ai[k] is not None else ('No trace pair represented; flèche.' if k==1 else 'Curved short stroke in TikZ; rendering-only change, not counted.'),'B':B[bi[k]]['reading'] if bi[k] is not None else 'No trace pair represented; flèche.','C':C[j]['reading']}
 d['marked_in_H']='no'
 if isinstance(d.get('alternatives'),list):d['alternatives']='; '.join(d['alternatives'])
 ds.append(d)
bp=lambda f:'readers/scan071/B/crops/'+f
for k,f in [(0,'scan071_B_01_page_number.jpg'),(2,'scan071_B_21_p22_li5.jpg'),(3,'scan071_B_24_short_margin_stroke.jpg'),(4,'scan071_B_29_dots_after_et.jpg'),(5,'scan071_B_30_long_margin_stroke.jpg'),(6,'scan071_B_31_donne_overprints.jpg'),(7,'scan071_B_32_demonstration_overprint.jpg'),(8,'scan071_B_34_malsonnante.jpg')]:ds[k]['crop']=bp(f)
ds[1]['crop']='readers/scan071/C/crops/C_071_07_above_fleche.jpg'
ds[0]['scan_shows']='The looped 6 has two distinct flanking strokes: a short pale left dash and a darker, longer right dash. All three readers restore them, and the main crop confirms their separation from the numeral.'
ds[1]['scan_shows']='Two pale grey shapes stand apart from the final e of flèche: an upper short nearly vertical trace and a lower-left horizontal/oblique trace. They are larger and more coherent than the surrounding fine grain, but their origin is not established. C records them; A and B leave them unrepresented. Main preserves the observed pair graphically and uncertainly, without calling it an exclamation mark, punctuation, or authored pen ink.'
ds[2].update(reading=A[1]['reading'],diff_c=True,alternatives='Z; 2; 3',scan_shows='The live 2 has a rounded upper-right turn, a descending diagonal and a low foot. Additional straight top and bottom bars have short terminal spurs down at upper-left and up at lower-right, supporting the Z alternative found by A and B. The merged impression still permits a covered 2 or 3. Main adds Z first and retains both older numeric alternatives; no typing chronology beyond the recorded overprint is inferred.')
ds[3].update(reading=B[3]['reading'],diff_c=True,scan_shows='The short margin stroke has a rounded dark left end, a shallow arch through its middle and a fading narrow right end immediately before p. A and C treat conversion from an em dash as rendering-only; B records the contour. Main counts the restored arch/taper and line-relative placement as a graphic difference, while the choice of TikZ wrapper itself is not a change.')
ds[4].update(reading=B[4]['reading'],confidence='medium',scan_shows='The lower-left mark is a compact horizontal oval and the upper-right mark is a narrower oblique oval. Both are high relative to the baseline of et; their centres are not vertically aligned. Main retains the high diagonal pair, with its colon-like function and authored status unresolved. All three readers agree on the physical arrangement.')
ds[5].update(reading=B[5]['reading'],scan_shows='A long lower branch starts with a nearly horizontal run far left and rises toward p.24; an upper return branch bends back left into a narrow open loop. The dark flattened right portion crosses the upper part of p. and extends above its point toward the 2. All readers identify this overlap. Main adopts B’s anchored drawing instead of C’s detached margin placement; the p.24 remains live text.')
ds[6]['scan_shows']='The second live n encloses an extra upper aperture, middle curved bar and lower bowl. The overprinting covers the distinguishing right joins, allowing either e or a underneath. All readers retain e|a, and the main crop confirms that limit. The separate tall stem and crossbar under the first n support the unchanged deleted t.'
ds[7].update(reading=r'\deleted{m}démonstration',diff_c=True,unresolved=False,alternatives='',confidence='high',kind='misread word',scan_shows='The underprint beneath the initial live d shows a left serifed stem, a central upright and two adjacent low counters/shoulders. The central upright divides the d bowl into the two arches of m. A and B resolve m; C retains doubt. The main crop supports m distinctly enough to remove that doubt while keeping it deleted.')
ds[8]['scan_shows']='Eleven x impressions cross the word. The tall l and t and the round o and final e remnants are visible, with initial m/a and middle arches supporting malsonnante. A resolves the word; B and C retain doubt. In the main crop the fourth-cell curves and several middle joins remain merged with the cancellation, so the preferred word stays explicitly unsure rather than being completed from the surrounding sentence.'
s=(O/'readers/scan071/B/reading.tex').read_text()
s=s.replace(B[2]['reading'],A[1]['reading'])
cs=(O/'readers/scan071/C/reading.tex').read_text()
a=cs.index('% Two faint detached traces');b=cs.index('\np.22, li.8',a)
s=s.replace('p.20, li. 3 du bas : manque flèche.\n',cs[a:b].rstrip()+'\n')
s=s.rstrip()+'\n\\clearpage\n'
(O/'pages/B37-04_37_scan071.tex').write_text(s)
inv=copy.deepcopy(R['C']['inventory'])
inv[13]['hand']='unnamed source; authorship or incidental origin unresolved'
inv[17]['element']='Overtyped last page-reference character';inv[17]['first_words_or_objects']='Possible Z, 2 or 3 beneath live final 2'
inv[24]['hand']='unnamed source; punctuation and authorship unresolved'
inv[28]['first_words_or_objects']='m beneath live d, resolved'
notes="""One typescript continuation: an opening fragment followed by twenty page-and-line comments on pages 18–25. Handwritten own number - 6 - and archive number 70 are present; there is no title, date, salutation or signature. The opening continues the preceding sheet’s ‘ne sont pas’ with a cancelled mis followed by live mis en lumière. The text states ‘la référence (V 3.3.2) est vide’ and leaves the spaces after VII and SGA 5 IV unfilled; no reference numbers are supplied editorially. Body words and reference digits are typed, including their curved numeral designs. The Gr arrow and tilde and the two large marginal strokes are hand-drawn; the two detached pairs have unassigned origin.

Authorial questions and reservations are preserved in the author’s words: ‘est-ce vraiment possible sans autre hypothèse sur Z ?’; ‘linéairement’ = ‘rationnellement’ ?; ‘Il faudrait aussi une référence pour le fait que’ dim(Z_s) = dim(Z_t); ‘N’est-il pas prudent de supposer f lisse ?’; ‘Supposer X plat sur S.’; ‘hypothèses sur X ?’; ‘donner le corollaire pour NS ?’; the request for ‘références pour’ ‘essentiellement de type fini’ and ‘universellement japonais’; and ‘dommage qu’on ne donne pas de démonstration.’ The phrase ‘manque flèche’ is an instruction in the prose, not a missing diagram supplied by this edition. The quoted standard/standart and rationnelle/rationelle pairs and the literal quoted ellipsis are retained as the proposed corrections, not silently modernized.

All five explicit C doubts were inspected. The old m in démonstration is resolved; the covered reference character gains Z as its preferred candidate; e/a and the cancelled malsonnante remain uncertain. The pair after et is preserved by its high diagonal shape, and the pale pair above final e in flèche is newly retained without a punctuation or authorship claim. The long margin stroke overlaps the prefix p.24 and is anchored accordingly. H supplies description only and has no collation rows. These notes report the page’s assertions and requests; no proof or computation was performed."""
math=copy.deepcopy(R['C']['math_reading_decisions'])
math.append('The new Z alternative concerns an overprinted character in a page reference, not a changed live mathematical variable. The live number remains p.22. The initial underprint of démonstration is resolved from two low arches, not from the expected live word.')
notation=copy.deepcopy(R['C']['notation'])
notation[5]['latex']=ds[4]['reading']
notation.append(dict(sign='Overprinted reference character',latex=A[1]['reading'],evidence='Straight upper/lower bars with opposing terminal spurs support Z; merged numeric contours still allow 2 or 3.',place='p.22, li.5 reference'))
out=dict(scan=71,decisions=ds,inventory=inv,notes=notes,math_reading_decisions=math,notation=notation,abbreviations=R['C']['abbreviations'],slips=R['C']['slips'],check_events=[],main_crops=[])
(O/'decisions/scan071.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print('Wrote scan 071: 9 mandatory records; five C doubts reviewed; seven C differences.')
