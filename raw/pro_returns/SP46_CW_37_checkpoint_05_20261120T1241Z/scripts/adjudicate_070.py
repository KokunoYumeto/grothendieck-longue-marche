from pathlib import Path
import json,copy
O=Path(__file__).resolve().parents[1]
R={a:json.loads((O/f'readers/scan070/{a}/report.json').read_text()) for a in 'ABC'}
A,B,C=[R[a]['decisions'] for a in 'ABC']
ds=copy.deepcopy(C)
am=[0,1,2,None,3,4,5,6,7,None,None,None,8,9]
bm=[0,1,2,3,4,5,6,7,None,10,11,12,None,None]
for i,d in enumerate(ds):
 d['readers']={'A':A[am[i]]['reading'] if am[i] is not None else ('.' if i==3 else r'\handwritten{\chi}'),'B':B[bm[i]]['reading'] if bm[i] is not None else (B[8]['reading']+'; '+B[9]['reading'] if i==8 else ('6.5.3' if i==12 else '6.6.4')),'C':C[i]['reading']}
 d['marked_in_H']='no'
 if isinstance(d.get('alternatives'),list):d['alternatives']='; '.join(d['alternatives'])
 d['crop']=''
bp=lambda f:'readers/scan070/B/crops/'+f
cp=lambda f:'readers/scan070/C/crops/'+f
for i in (2,3):ds[i]['crop']=bp('B070_01_added_reference.jpg')
for i,f in [(4,'scan070_C_02_romanIV.jpg'),(5,'scan070_C_03_romanIII.jpg')]:ds[i]['crop']=cp(f)
for i,f in [(6,'B070_02_first_x_index.jpg'),(7,'B070_03_second_x_index.jpg'),(8,'B070_04_trouve_separator.jpg'),(9,'B070_05_first_chi.jpg'),(10,'B070_06_second_chi_pair.jpg'),(11,'B070_06_second_chi_pair.jpg')]:ds[i]['crop']=bp(f)
for i in (12,13):ds[i]['crop']='readers/scan070/A/crops/A070_08_final_reference.jpg'
ds[0].update(crop='crops/scan070/pagination.jpg',scan_shows='A short descending dash stands left of the handwritten 5, and a separate shallow rising dash stands right of it. The main crop confirms the two flanking strokes reported by all three readers.')
ds[2]['scan_shows']='The separator is low and distinctly wider than high, with a short flat horizontal centre. B and C prefer a dash; A prefers an elongated point. The main crop supports the dash first, while retaining the point alternative rather than deciding from the reference function.'
point=r'\unsure{\handwritten{.}|.}'
ds[3].update(reading=point,unresolved=True,alternatives='handwritten point; typed point',confidence='medium',kind='other',scan_shows='The low terminal mark is a compact tapering triangle, unlike the round typed reference points elsewhere on this sheet. This favours the hand-written state, as C reads, but a small mark alone does not securely establish the writing operation. A leaves it typed and B marks the state uncertain. Preserve the point and the state uncertainty; no underprint is inferred.')
ds[6]['scan_shows']='The first lowered character is a small closed oval, about the height of the following s. A resolves o from this height; B and C retain o/0. The main crop shows the o-shaped impression but no internal or distinguishing stroke that fixes whether it serves alphabetically or numerically. Retain C’s o|0 without using the paired index to choose.'
ds[7]['scan_shows']='The tall lowered character has a short left-projecting head, a vertical stem and a broad basal foot; s is distinct after it. All three readers retain l/1. The crop does not supply a separate diagonal lead-in or other decisive feature, so the original alternatives remain.'
cluster=r"\makebox[0pt][l]{\hspace{0.15em}''}\unsure{\ldots|.\,:|.\,.|.}"
ds[8].update(place='Handwritten p.16, li.8 du bas, closing quotation and low punctuation cluster after on trouve',c_reading=r"''\unsure{:|.}",reading=cluster,alternatives='three low points (ellipsis); separate period and colon; two periods; one authored period with incidental specks',confidence='low',scan_shows='Two high short strokes form the closing quotation pair. Below and slightly to their right are a dark horizontal point, a much fainter middle point, and a darker right point. The main crop favours a horizontal three-point cluster. B instead assigns the first low point before the closing quotation and the far-right marks to a colon/period separator; A allows a single point with specks. Preserve these alternatives. A zero-width quotation placement retains the high pair over the start of the low cluster, rather than moving every point to its right.')
for i in (9,10,11):
 ds[i]['scan_shows']='The lowered chi has a flat upper-left serif, an upright member and a long lower-right foot, crossed by a rougher diagonal extending below-left. Each occurrence was separately inspected in the retained crops. B reads the repeated serifed form as typed; A calls it handwritten; C retains uncertainty. The main reading prefers typed/composite construction but cannot securely assign the diagonal’s production, so the first chi carries the recurring material-state alternative. No cancelled l or correction chronology is inferred.'
 ds[i]['confidence']='medium'
ds[12].update(reading=A[8]['reading'],scan_shows='The 6, 5 and 3 are thin, freely curved pen forms with variable widths. The two separating points are dark round typewriter impressions, like the surrounding typed punctuation. Main adopts A’s division of handwritten digits and typed points; C groups the whole number as handwritten, and B leaves it typed.')
ds[13].update(reading=A[9]['reading'],scan_shows='Both 6 digits have freely rising open upper hooks, and the 4 has a thin open-top angular construction. The two separating points are dense round machine impressions. Main adopts the handwritten digits with typed points, as A records; the numbers themselves are unchanged.')
s=(O/'readers/scan070/C/reading.tex').read_text()
s=s.replace(r'\handwritten{(7\unsure{-|.}15).}',r'\handwritten{(7\unsure{-|.}15)}'+point)
s=s.replace(r"''\unsure{\ldots|:|.}",cluster)
s=s.replace(r'\handwritten{6.5.3}',A[8]['reading']).replace(r'\handwritten{6.6.4}',A[9]['reading'])
s=s.rstrip()+'\n\\clearpage\n'
(O/'pages/B37-04_37_scan070.tex').write_text(s)
inv=copy.deepcopy(R['C']['inventory'])
inv[6]['hand']='unnamed hand; terminal point hand/type state uncertain'
inv[26]=copy.deepcopy(R['A']['inventory'][26]);inv[27]=copy.deepcopy(R['A']['inventory'][27])
notes="One typescript sheet of corrections and questions on pages 11–17, with fourteen typed reference entries, two handwritten added entries, two labelled identities, handwritten pagination - 5 -, and archive number 69 recorded only as a comment. There is no title, date, salutation or signature. The appended reference, the p.13 and p.16 added entries, the two psi signs and the six final citation digits are written by an unnamed hand; the citation points are typed. The terminal point after the appended reference and the construction of the three chi signs remain materially uncertain. The final sentence stops at ‘ne sont pas’. The author requests a reference in Exp.V; asks whether connectedness of C alone suffices, ending ‘ou est-ce que je me canule ?’; asks ‘SGA ou EGA ?’; says a connected-curve assertion was used ‘sans référence’; asks whether ‘propre et lisse’ suffices; and objects, with ‘il me semble’, that geometrically regular fibres do not make an X not assumed flat smooth. The author’s wording and single-n canule are preserved. These are reports of the page, not independently proved assertions. All three explicit C doubts were inspected: both index doubts remain, and the punctuation cluster now has a broader explicit alternative set. H is description-only and has no collation rows. No proof, computation, or external research was performed."
math=copy.deepcopy(R['C']['math_reading_decisions'])
math[-1]='The labels (i) and (ii), both formula-ending commas, absence of arrows/inequalities, and final reference digits 6.5.3 and 6.6.4 were checked from ink. The six digits are handwritten; the separating points are typed. No identity was proved or repaired.'
notation=copy.deepcopy(R['C']['notation'])
notation[-1].update(latex=cluster,evidence='Two high quotation strokes over the start of three low traces, with a faint middle point. Ellipsis preferred; separated punctuation and incidental-speck interpretations remain.')
notation.append(dict(sign='Terminal reference point, writing state uncertain',latex=point,evidence='Small tapering triangular mark favours handwriting, but its writing operation is not secure.',place='After the appended 7–15 reference'))
out=dict(scan=70,decisions=ds,inventory=inv,notes=notes,math_reading_decisions=math,notation=notation,abbreviations=R['C']['abbreviations'],slips=R['C']['slips'],check_events=[],main_crops=json.loads((O/'crops/scan070/manifest.json').read_text()))
(O/'decisions/scan070.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print('Wrote scan 070: 14 records; all three C doubts reviewed; 11 differences from C.')
