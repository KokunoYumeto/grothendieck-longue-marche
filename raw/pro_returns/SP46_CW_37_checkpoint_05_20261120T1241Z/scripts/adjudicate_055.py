from pathlib import Path
import json,copy
O=Path(__file__).resolve().parents[1]
R={a:json.loads((O/f'readers/scan055/{a}/report.json').read_text()) for a in 'ABC'}
A,B,C=[R[a]['decisions'] for a in 'ABC'];ds=copy.deepcopy(A)
for i,d in enumerate(ds):
 d['readers']={'A':A[i]['reading'],'B':B[[2,12,13,15][i]]['reading'],'C':C[[3,19,20,22][i]]['reading']}
 d['crop']='readers/scan055/A/'+Path(d['crop']).name
 d['marked_in_H']='no'
 if isinstance(d.get('alternatives'),list):d['alternatives']='; '.join(d['alternatives'])
ds[0]['scan_shows']='Before X, n, + and a separate 1 are distinct. Before Y and Z the right end of the plus bends down into a short stroke without a visible gap. The stroke can be an attached 1 or an extended plus. Retain the incomplete-exponent alternative at the first ambiguous occurrence, before Y, and the preferred n+1 at the recurrence before Z under the prescribed convention. Mathematical expectation does not settle the attached stroke.'
ds[1]['scan_shows']='After the tall looped h, a short open low stroke leads directly into w. Its opening favours e, but a compressed unclosed o remains possible. The final s is visible. Retain shews|shows without modernizing the spelling.'
ds[2]['scan_shows']='The short word is covered by a thick blue-black cancellation. A narrow pale opening and a small right projection survive, but no separable letter sequence can be recovered; retain one cancelled illegible word.'
dots=r'''\margin{\figure{\unsure{\begin{tikzpicture}[x=1mm,y=1mm]
\fill (0,0) .. controls (-0.24,0.01) and (-0.26,0.20) .. (-0.06,0.33) .. controls (0.09,0.40) and (0.25,0.12) .. (0.19,0.03) -- cycle;
\fill (0.55,0.97) ellipse[x radius=0.18,y radius=0.24,rotate=-25];
\end{tikzpicture}}}}'''
ds[3].update(reading=dots,diff_c=True,kind='drawing or diagram',scan_shows='Two small dark marks lie on a rising-right diagonal, the upper oval and the lower roughly triangular. Their presence is visible but an intended colon is not established. The main reading reproduces the oblique pair as an uncertain graphic, consistently with the separately inspected pair on scan 054; the three readers retained a literal uncertain colon.',alternatives='colon-like marginal pair; incidental paired marks')
s=(O/'readers/scan055/A/reading.tex').read_text().replace(r'\margin{\unsure{:}}',dots)
if not s.rstrip().endswith(r'\clearpage'):s=s.rstrip()+'\n\\clearpage\n'
(O/'pages/H37-01_37_scan055.tex').write_text(s)
inv=copy.deepcopy(R['C']['inventory'])
for x in inv:
 if x['element']=='Small marginal dot pair':x['kind']='drawing';x['first_words_or_objects']='Two obliquely aligned dark points, function uncertain'
notes=R['C']['notes'].replace('The marginal pair remains an uncertain colon.','The marginal pair remains uncertain in function and is reproduced as two oblique points in TikZ.').replace('No substantive C difference was found; all four explicit C doubts were independently inspected and retained.','All four explicit C doubts were independently inspected and remain unresolved. The main reader refines the marginal pair’s graphic placement; no prose or mathematical word is changed.')
math=R['A']['math_reading_decisions']+['The cropped exponent chain does not license completing a missing 1 from the mathematical pattern. Both attached forms retain the same declared uncertainty.','The letter’s inverse-limit exactness, Artin–Rees step and isomorphism conclusion were read, not independently proved, used as established background or checked against another source.']
notation=copy.deepcopy(R['C']['notation'])
notation.append(dict(sign='Detached marginal point pair',latex=dots,evidence='Upper oval point to the right of a lower triangular point; punctuation status unresolved.',place='Right margin by the publication sentence; compare the independently read pair on scan 054.'))
out=dict(scan=55,decisions=ds,inventory=inv,notes=notes,math_reading_decisions=math,notation=notation,abbreviations=R['C']['abbreviations'],slips=['The lowercase let after a full stop is visible and preserved; no correction is supplied.'],check_events=[],main_crops=[])
(O/'decisions/scan055.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print('Wrote scan 055: four C doubts retained, marginal graphic refined.')
