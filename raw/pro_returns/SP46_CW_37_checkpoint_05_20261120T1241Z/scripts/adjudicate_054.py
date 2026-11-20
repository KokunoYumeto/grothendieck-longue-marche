from pathlib import Path
import json,copy
O=Path(__file__).resolve().parents[1]
R={a:json.loads((O/f'readers/scan054/{a}/report.json').read_text()) for a in 'ABC'}
A,B,C=[R[a]['decisions'] for a in 'ABC'];ds=copy.deepcopy(C)
am=[0,3,4,5,7,8,9,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,31,32,32,33,35,1,10]
bm=[0,1,4,6,2,3,5,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,26,27,27,28,29,None,None]
for i,d in enumerate(ds):
 d['readers']={'A':A[am[i]]['reading'],'B':B[bm[i]]['reading'] if bm[i] is not None else ('Open irregular frame after letterhead' if i==32 else 'Straight vertical pencil stroke'),'C':C[i]['reading']}
 d['marked_in_H']='no'
 if isinstance(d.get('alternatives'),list):d['alternatives']='; '.join(d['alternatives'])
 d['crop']=''
for i,af in [(0,0),(8,12),(10,14),(11,16),(12,17),(18,23),(19,24),(21,26),(24,29),(30,33),(31,35)]:
 ds[i]['crop']='readers/scan054/A/'+A[af]['crop']
def up(i,**kw):ds[i].update(kw)
up(0,reading='Jouanolou',diff_c=True,unresolved=False,alternatives='',confidence='high',scan_shows='The main crop shows the large descending J, low joined o-u, closed a, short n, oval o, tall looped l and terminal o-u. Their connections are compressed but continuous. The surname is resolved with A; B and C retained doubt about the medial joins.')
up(8,scan_shows='A, the two strong separators, 3 and 1 are distinct. The much paler speck to the lower right of 1 cannot securely be classed as an intentional final point. Retain both terminal-punctuation readings.')
up(10,scan_shows='The closed round outline has a short inward notch at its top and a connection toward the upper rule of the lowered III. Neither 0 nor O has a distinguishing stroke here. Both rules and all three smaller uprights are visible; retain 0|O.')
up(12,scan_shows='Heavy horizontal and oblique cancellation strokes cover the body of the short word. An exposed upper loop and a small terminal curl survive, but they do not separate the|from. The deletion and its uncertainty remain.')
up(18,scan_shows='A compact oblique oval follows 40. It has no independent descending tail and closely resembles the visible abbreviation point after p. Read a period with A and C; B retained a short-comma possibility.')
up(19,scan_shows='After the visible through sequence, a tall retraced oval is crossed by a horizontal stroke; final u and crossed t remain visible. The crossed middle permits either an overwritten o or an additional t before o. Keep throughout preferred and add throughtout as a possible unnormalized spelling, following reader C. This is a recorded alternative, not an asserted authorial error.')
dots=r'''\margin{\figure{\unsure{\begin{tikzpicture}[x=1mm,y=1mm]
\fill (0,0) .. controls (-0.28,0.02) and (-0.25,0.24) .. (-0.08,0.35) .. controls (0.08,0.43) and (0.26,0.10) .. (0.20,0.03) -- cycle;
\fill (0.55,0.92) .. controls (0.30,0.83) and (0.35,1.13) .. (0.48,1.27) .. controls (0.59,1.48) and (0.81,1.20) .. (0.76,1.06) -- cycle;
\end{tikzpicture}}}}'''
up(21,reading=dots,diff_c=True,kind='drawing or diagram',scan_shows='Two separate dark marks form a short rising-right diagonal; the upper mark has a small lower-left projection and the lower is roughly triangular. Reproduce the observed pair as an uncertain graphic instead of an upright literal colon. Its possible punctuation function remains unresolved; A/C retain a literal uncertain colon and B tilts that colon.',alternatives='colon-like marginal pair; incidental paired marks')
up(24,scan_shows='A separate dark point is plainly above the left end of the horizontal stroke, followed by an upright 1. All three readers and the main crop resolve the visible dot. Its intended function is not inferred.',consequential='The first line indicator includes a visible dot above its minus; the second remains plain -1. This preserves the written signs without assigning a mathematical operation to the dot.')
up(30,scan_shows='The second EGA glyph independently shows the same closed round outline with an inward top notch. Three lowered uprights stand between upper and lower rules. It is also graphically 0/O ambiguous; under the prescribed recurring-glyph convention the first occurrence carries the doubt and this one uses its preferred 0.')
up(32,diff_c=True,crop='crops/scan054/frame.jpg',reading='Open, slightly bowed pencil frame; note anchored before the printed university letterhead',scan_shows='The upper rule rises gently, rounds into a short right downstroke, and is separated from the longer lower-right stroke by a broad opening. The left and bottom strokes join. The note begins above the printed letterhead, so the A/C anchoring order is retained. C’s straight-edged approximation is replaced by the curved frame; the surname is decided separately.')
up(33,crop='crops/scan054/grouping.jpg',scan_shows='A single nearly vertical pencil stroke stands left of the title continuation and reference question, with a small widened foot. C reader’s TikZ path preserves the same grouping mark as the witness rule; this rendering adjustment is not counted as a textual change.')
for i in [26,28]:
 ds[i]['readers']={a:'n' for a in 'ABC'}
for i in [27,29]:ds[i]['readers']['A']='n+1' if i==27 else 'n-1'
extra=copy.deepcopy(A[2]);extra.update(crop='readers/scan054/A/'+A[2]['crop'],marked_in_H='no',alternatives='',readers={'A':A[2]['reading'],'B':'Omitted','C':'Omitted'},scan_shows='The main crop shows an isolated dark crescent-like blob with a rounded left body, upper-right notch and small lower-right projection. Preserve its visible shape without reading a letter or asserting an intended function. B, C reader and witness C omit it.')
ds.insert(1,extra)
s=(O/'readers/scan054/C/reading.tex').read_text().replace(r'\unsure{Jouanolou}','Jouanolou',1)
s=s.replace(r'\hfill Aug 4, 1969\\',r'\hfill Aug 4, 1969\\'+'\n% isolated mark at the far right of the date; function unassigned\n'+A[2]['reading'])
s=s.replace(r'\margin{\unsure{:}}',dots)
if not s.rstrip().endswith(r'\clearpage'):s=s.rstrip()+'\n\\clearpage\n'
(O/'pages/H37-01_37_scan054.tex').write_text(s)
inv=copy.deepcopy(R['A']['inventory'])
for x in inv:
 if x['element']=='Colon-like pair of marginal marks':x['kind']='drawing'
notes=R['A']['notes'].replace('An isolated dark mark by the date and a colon-like pair beside pro-A are also preserved.','An isolated dark mark by the date and a diagonally aligned pair beside pro-A are also preserved without assigning their function.')
notes+=' The retraced word is recorded as throughout|throughtout; this is a reader alternative, not a demonstrated slip. The p.40 stop and the dot over the first minus are resolved. No date, signature or title is supplied from another sheet or from H’s description.'
out=dict(scan=54,decisions=ds,inventory=inv,notes=notes,math_reading_decisions=R['A']['math_reading_decisions'],notation=R['C']['notation'],abbreviations=R['A']['abbreviations'],slips=['The point above the first minus is visible, but its purpose is unestablished.','The overwritten middle in throughout|throughtout does not establish an authorial misspelling.'],check_events=[],main_crops=json.loads((O/'crops/scan054/manifest.json').read_text()))
(O/'decisions/scan054.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print('Wrote scan 054:',len(ds),'decisions; eight explicit C doubts reviewed.')
