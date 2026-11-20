#!/usr/bin/env python3
"""Materialize the main reader's crop-adjudicated scan 032."""
from pathlib import Path
from copy import deepcopy
import json
R=Path(__file__).resolve().parents[1]
raw={w:json.loads((R/f'readers/scan032/{w}/review.json').read_text()) for w in 'ABC'}
a=raw['A']['loci'];b=raw['B']['loci'];c=raw['C']['loci']
loci=[]
bmap={1:5,2:9,3:2,4:3,5:6,6:7,7:8,8:10,9:11,10:4}
cmap={1:8,2:9,3:1,4:2,5:3,6:4,7:5,8:6,9:7,10:10}
for n,z in enumerate(a,1):
 x=deepcopy(z);x['id']=f'S032-{n:02}';x.pop('box',None)
 x['readers']={'A':z['reading'],'B':b[bmap[n]-1]['reading'] if n in bmap else ('Gap retained in page.tex, no separate difference row' if n in [11,12] else 'Observed isolated components; no figure reconstructed; origin and verbal role unassigned'),'C':c[cmap[n]-1]['reading'] if n in cmap else ('Gap retained in page.tex, treated as ordinary formula spacing' if n in [11,12] else ('Geometric preservation; origin and role unassigned' if n in [14,15,16] else 'No separate figure; isolated flecks yield no character sequence'))}
 x['crop']='scan032/'+('B/B_first_display.png' if n in [1,5,6,7,11] else 'B/B_second_display.png' if n in [2,8,9,12] else 'B/B_prose_fields.png' if n in [3,4,10] else 'A/'+z['crop'])
 x['decision']='Main reader inspected the listed existing crop and retained the visible reading.'
 loci.append(x)
q={n:loci[n-1] for n in range(1,18)}
q[1]['evidence']='A broad open outer curve surrounds a low folded inner return and upturned right foot. The rounded contour leaves the frak A / cal A choice open. The regular low 5 is typed. H identifies the group letters as hand-added in its batch comment and preceding note; its difference here is the unqualified alphabet reading.'
q[2].update(diff_H=False,evidence='The high turned-up top, broad outer curve and folded inner return support the handwritten frak S; the low 5 has the regular typed form. H’s batch comment explicitly identifies the gothic A5 and S5 on its pp. 30–31 as inked by hand, and its preceding note records hand additions in blank typing cells. The wrapper difference alone is excluded.',decision='Retain C. Correct the readers’ proposed H hand-state difference using the supplied H batch context; no separate collation row.')
for n in range(3,10):
 q[n]['confidence']='medium';q[n]['kind']='insertion or placement'
 q[n]['evidence']+=' The supplied H batch comment says the double-struck F4 and F5 look typed. The irregular outside stroke is therefore a material state disagreement, beyond macro spelling.'
q[11]['evidence']='The first displayed Sl is followed by a visibly empty typewriter position before the opening parenthesis; the first-row GP( and SO( are closer. The root formula crop confirms the gap encoded by C.'
q[12]['evidence']='The second-row GP is followed by a visible blank typewriter position before its opening parenthesis. Root inspected this gap in the full tight second-formula crop; the first-row GP( has the closer placement.'
for n in range(13,18):
 q[n]['decision']='Preserve the observed geometry with origin, hand and textual role unassigned. The inventory vocabulary drawing records this geometric reproduction without an attribution.'
q[16]['confidence']='low';q[17]['confidence']='low'
dot=deepcopy(b[0]);dot.update(id='S032-18',crop='scan032/B/B_deux_punctuation.png',readers={'A':'deux et cinq; no point recorded','B':r'deux\unsure{.|} et cinq','C':'deux et cinq; no point recorded'},decision='Adopt B’s qualified point. Root sees the pale oval centered at the baseline in the otherwise empty cell. The shape is visible; linguistic punctuation versus unassigned trace remains open.');dot.pop('box',None);loci.append(dot)
# Page content: reader A's complete wording/geometry, plus the separately adjudicated point.
page=(R/'readers/scan032/A/page.tex').read_text().replace('de caractéristique deux et cinq',r'de caractéristique deux\unsure{.|} et cinq')
upper=r'''% Unassigned compact hook above the text, source near (559,98).
\figure{\begin{tikzpicture}[x=0.006cm,y=-0.006cm,line cap=round,line join=round]
  \path[use as bounding box] (0,70) rectangle (1679,122);
  \draw[line width=0.3pt] (557.8,98.9) .. controls (560.3,99.3) and (560.8,98.0) .. (560.6,96.4);
\end{tikzpicture}}
'''
page=page.replace('En relation avec',upper+'En relation avec',1)
page=page.replace('  \\path[use as bounding box] (0,70) rectangle (1679,2233);','  \\path[use as bounding box] (0,1579) rectangle (1679,2233);')
needle='  \\draw[line width=0.3pt] (557.8,98.9) .. controls (560.3,99.3) and (560.8,98.0) .. (560.6,96.4);'
# Keep the upper occurrence and remove only the lower-map repetition.
pos=page.rfind(needle);page=page[:pos]+page[pos:].replace(needle+'\n','',1)
page=page.replace('% Upper hook near (559,98); right hook near (1469,1607); detached pair near (1504,1750);','% Upper hook is drawn above the text. Lower map: right hook near (1469,1607); detached pair near (1504,1750);')
(R/'pages/J75-04_75_scan032.tex').write_text(page)
# Inventory union, in top-to-bottom order; no claimed identity for an anonymous pen.
inv=deepcopy(raw['B']['inventory'])
for v in inv:
 if v['hand']=='his hand':v['hand']='unnamed hand'
inv.insert(0,deepcopy(raw['A']['inventory'][9]))
for j in [10,11,13,12]:inv.insert(-1,deepcopy(raw['A']['inventory'][j]))
for v in inv:
 if v['hand']=='unknown hand':v['hand']='unnamed hand; origin unassigned'
doubts=[]
for x in [q[1],dot,*[q[n] for n in range(13,18)]]:
 doubts.append({'location':x['location'],'reading':x['reading'],'alternatives':r'\mathcal A' if x is q[1] else 'point / unassigned trace' if x is dot else 'origin and textual role unassigned','confidence':x['confidence'],'reason':x['evidence']})
notes=r'''**N032.1 — Source statement.** This continuation of the course announcement names characteristics two and five, and the fields F₄ and F₅, in its proposed geometric and combinatorial dictionaries for the icosahedron. It prints two chains beginning with handwritten A₅ and S₅, followed respectively by Sl (2,F₄), GP(1,F₄), SO(3,F₄), and GP (1,F₅), SO(3,F₅). The source has no proof, author doubt, title or date here. Its lower-left archive numeral is 31. The orthogonal-group links and the proposed icosahedral dictionaries were carried as source claims; this run supplies no verification of them.

**N032.2 — Ink-led mathematical reading.** All three readers and the main crop inspection retain C’s frak A / cal A alphabet doubt and the typed low 5. The second capital reads frak S with typed low 5. All seven F bodies and their lowered digits remain typed; each irregular outer left stroke is separately hand-marked. The labels retain their printed case Sl, GP and SO, and all five relations retain one wave over one bar. Formula parsing directed attention to each index, argument, parenthesis and relation; no mathematical expectation supplied a character. The added pale point after “deux” remains qualified. Five peripheral groups are geometrically preserved with unassigned origin and role. H’s batch-wide note already records the handwritten gothic group capitals, so that state alone contributes no H correction. Its stated typed interpretation of the doubled fields remains a material disagreement.

**N032.3 — Concrete group maps checked by computation.** The script `scripts/check_projective_links.py` constructs the projective-line action of SL₂(F₄), with point order (∞,0,1,a,a+1) and a²+a+1=0, and verifies that its 60 distinct images are precisely the even permutations of five points. It also constructs a specific bijective homomorphism PGL₂(F₅) → S₅: conjugation on the six cyclic order-five subgroups of S₅ is matched to the projective-line action by the explicit relabelling u=(0,1,2,5,3,4), in zero-based image-list notation. Every product is checked in the finite tables. The exact morphisms and all 60 and 120 matrix-to-permutation images are recorded in `decisions/scan032_math_checks.md` and `decisions/scan032_projective_check.json`. These computations check the concrete SL₂/PGL₂ readings associated with the printed Sl/GP links. They do not select the manuscript alphabet.

**N032.4 — Explicit F₄ projectivization map.** For the field model above, each nonzero δ satisfies δ³=1, directly from the three elements 1,a,a+1. The map [M] ↦ det(M)M from PGL₂(F₄) to SL₂(F₄) is unchanged by every scalar representative replacement: det(sM)sM=s³det(M)M=det(M)M. Its determinant is det(M)³=1; multiplicativity follows by multiplying det(M)M and det(N)N. Its inverse is M ↦ [M]. This supplies the exact map relating the two concrete F₄ matrix groups in the first printed chain. This proof is recorded separately from the finite computation; no SO link is included.'''
rec={'scan':32,'loci':loci,'inventory':inv,'doubts':doubts,'notes':notes,'check_events':[
 {'statement_id':'N032.1','date':'2026-11-20','who':'GPT-6 Astra Pro; effort not exposed; root/scan032','type':'carried as background without fault found','outcome':'Course claims reported from the source. SO(3) links and geometric/combinatorial dictionaries remain unchecked.'},
 {'statement_id':'N032.3','date':'2026-11-20','who':'GPT-6 Astra Pro; effort not exposed; root/scan032','type':'computation or formal certificate','outcome':'Explicit bijective permutation morphisms SL2(F4)→A5 and PGL2(F5)→S5 constructed; all 3600 and 14400 products checked, with all 14400 products of the auxiliary S5 conjugation action also checked. Python computation, no proof assistant. Complete tables and scope in the two scan032 math files.'},
 {'statement_id':'N032.4','date':'2026-11-20','who':'GPT-6 Astra Pro; effort not exposed; root/scan032','type':'targeted proof check','outcome':'Map [M]→det(M)M explicitly checked for scalar-representative invariance, determinant one, multiplicativity and inverse M→[M] over the stated F4 model. Details in N032.4 and scan032_math_checks.md.'}],
 'abbreviations':[{'abbr':a,'expansion':e,'scans':[32]} for a,e in [('Sl','special linear group; observed capital S and lowercase l retained'),('GP','groupe projectif; concrete comparison uses PGL₂ on a projective line'),('SO','special orthogonal group; the page’s form/model is not further specified here')]],
 'consequential':['All field digits and five relation signs are retained exactly; no mathematical rewriting is made. The first handwritten group capital remains frak A / cal A.', 'Seven added field strokes are recorded against H’s typed interpretation; H already records the two handwritten group capitals in its batch context.']}
(R/'decisions/scan032.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'loci':len(loci),'inventory':len(inv),'doubts':len(doubts),'changes_C':sum(x['diff_C'] for x in loci),'changes_H':sum(x['diff_H'] for x in loci)}))
