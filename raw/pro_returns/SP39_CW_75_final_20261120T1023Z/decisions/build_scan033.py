#!/usr/bin/env python3
"""Materialize root's full comparison and crop decisions for scan 033."""
from pathlib import Path
from copy import deepcopy
import json
R=Path(__file__).resolve().parents[1]
raw={w:json.loads((R/f'readers/scan033/{w}/review.json').read_text()) for w in 'ABC'}
a=raw['A']['loci'];b=raw['B']['loci'];c=raw['C']['loci']
bm={1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:9,11:10,12:10,13:11,14:12,15:13,16:13,17:17,18:18,19:19,20:14,21:15}
cm={1:1,2:2,3:3,4:4,5:5,8:6,9:7,10:7,11:8,12:8,13:9,17:11,18:12,19:13,20:10}
cp={1:'main/01_title.png',2:'main/02_first_dash.png',3:'main/03_second_dash.png',4:'B/B01_reflexion.png',5:'B/B02_Z.png',6:'B/B02_Z.png',7:'B/B02_Z.png',8:'main/04_deux_gap.png',9:'B/B03_avec.png',10:'B/B03_avec.png',11:'B/B04_fondements.png',12:'B/B04_fondements.png',13:'B/B04_fondements.png',14:'B/B10_C4_spacing.png',15:'B/B10_C4_spacing.png',16:'B/B10_C4_spacing.png',17:'B/B06_voudrait_hook.png',18:'B/B07_active_pair.png',19:'B/B08_left_edge.png',20:'B/B05_affine_trace.png',21:'A/09_trace_under_reflexion.png'}
loci=[]
for n,z in enumerate(a,1):
 x=deepcopy(z);x['id']=f'S033-{n:02}';x.pop('box',None);x['crop']='scan033/'+cp[n]
 cr=c[cm[n]-1]['reading'] if n in cm else ('Ordinary spacing as in both witnesses' if n in [6,7,14,15] else 'Plain C4; no separate method qualification' if n==16 else 'No separate geometric transcription')
 br=b[bm[n]-1]['reading']
 if n==10:br='Live v retained; no separate method qualification'
 if n==16:br='Plain C4; both full-height upright characters, no separate method qualification'
 x['readers']={'A':z['reading'],'B':br,'C':cr}
 x['decision']='Main crop inspection supports the stated reading and its recorded scope.'
 loci.append(x)
q={n:loci[n-1] for n in range(1,22)}
q[1]['evidence']='The main title crop shows upright typewriter stems and serifs, the circumflex in polygônes, and a single continuous rule beneath the entire title. H uses italic type without that rule.'
q[2]['evidence']='The main first-dash crop shows one short horizontal stroke in the cell before avec. Its ends are separate from the letters.'
q[3]['evidence']='The main second-dash crop shows one short horizontal stroke between métrique and en, with clear spaces on each side.'
q[4]['evidence']='A pale upper left-facing curve, central turn and lower return survive in the cell after réflexion. The much darker comma crosses the lower-right part. Root resolves the underlying s with all three readers, retaining its deleted state.'
q[8]['evidence']='The root crop shows the final x of deux and initial d of donnera separated by an enlarged blank interval, wider than ordinary letter/word intervals. C’s explicit additional space is retained.'
q[9].update(evidence='A visible horizontal bar runs from the left rounded contour into the middle of the heavy v overstrike. The bar lies below the live v top and above its lower point. The following e remains separate. This supports recovery of the underlying e.',decision='Adopt A and B’s resolved e after root crop inspection; C retains o|e. The live v is secure, with its inscription method left open in a source comment.')
q[12].update(evidence='The final s of points, the opening parenthesis and d of de occupy successive positions. There is no additional empty typewriter cell before the parenthesis; its broad stroke falls within the immediate interval before d.',decision='Adopt A’s adjacency points(de after root inspection; B, C and both witnesses include an extra ordinary blank.')
q[16]['decision']='Retain the secure plain C4 glyphs and explicitly comment on the unresolved method, following A. The taller narrow C and unfooted 4 do not establish a hand attribution. This does not count as a changed glyph or H collation row.'
q[21].update(reading='Compact pale point and paler broken trace, geometrically reproduced; origin and role unassigned',evidence='The A crop and the previously inspected context in B01 show a compact pale oval point below de, plus a paler short broken horizontal/curved trace to its lower right. Root preserves both components without a verbal interpretation.',decision='Adopt B’s two-component geometry; A explicitly draws only the compact point, C supplies no drawing of this group.')
extra=deepcopy(b[15]);extra.update(id='S033-22',crop='scan033/B/B09_left_mid_trace.png',readers={'A':'No separate geometric transcription','B':b[15]['reading'],'C':'No separate geometric transcription'},decision='Root sees a pale tapered shape just inside the physical left edge, with a darker left end and attenuated right end. Preserve the geometry with its origin and role unassigned.');extra.pop('box',None);loci.append(extra)
# C's anchored layout preserves the local relation of marks to prose; ink choices come from root.
page=(R/'readers/scan033/C/page.tex').read_text().replace('s033C-','s033-')
page=page.replace(r'a\deleted{\unsure{o|e}}vec',r'a\deleted{e}vec')
page=page.replace(r"l'anneau ${\handwritten{\mathbb}{Z}}$ des",r"l'anneau \hspace{.5em}${\handwritten{\mathbb}{Z}}$\hspace{.5em} des")
page=page.replace(r'points \handwritten{(}de',r'points\handwritten{(}de')
page=page.replace('le cours C4 sur',r'le cours \hspace{.5em}C4\hspace{.5em} sur')
page=page.replace('comme celle de réflexion',r'comme celle \tikz[remember picture,overlay]{\coordinate (s033-de);}de réflexion')
page=page.replace('quelques points de fondements de géométrie',r'''quelques\\
\tikz[remember picture,overlay]{\coordinate (s033-points1);}points de fondements de géométrie''')
comments='\n'.join((R/'readers/scan033/A/page.tex').read_text().splitlines()[15:23])
# Exact method comments, independent of source line numbers.
comments=r'''% The underlying e in avec has a visible mid-height horizontal bar.
% The live v is clear; the heavy overstrike leaves its inscription method open.
% The opening parenthesis retains C's hand encoding; reinforcement of type remains open.
% Z has two obliques; the added diagonal retains hand encoding at medium confidence,
% with a second type impression remaining an instrument alternative.
% C4 characters are clear; the tall narrow C and descending unfooted 4 leave
% inscription method unresolved. Plain encoding is retained without a glyph doubt.
'''
page=page.replace('% Detached geometries:',comments+'\n% Detached geometries:')
add=r'''% Compact point and paler broken trace below de before réflexion, source (1019,877).
\begin{scope}[shift={(s033-de)},x=0.26pt,y=-0.26pt]
\fill[black!45] (19,19) ellipse[x radius=1.25,y radius=.95];
\draw[black!25,line width=.45pt] (25.5,21.7) .. controls (27,20.9) and (29.5,21.3) .. (30.7,22.7);
\end{scope}
% Pale taper beside the source line beginning points, source (55--60,1220--1224).
\begin{scope}[shift={(s033-points1)},x=0.26pt,y=-0.26pt]
\fill[black!40] (-199,7) -- (-194.5,9.6) -- (-198.8,9.9) -- cycle;
\end{scope}
'''
page=page.replace('% Detached dark hook below the end of voudrait',add+'% Detached dark hook below the end of voudrait')
page=page.replace('% The line break before le detail retains the left-edge mark’s line attachment.','% Source line breaks before points and le detail retain the two left-edge line attachments.')
(R/'pages/J75-04_75_scan033.tex').write_text(page)
# Inventory union, ordered by first source position; metadata qualifications preserved.
bi=deepcopy(raw['B']['inventory']);ai=deepcopy(raw['A']['inventory'])
bi[7]['hand']='unnamed hand or further type impression; method qualified in source comment'
bi[10]['hand']='unnamed hand; possible reinforcement of type remains open'
ordered=[bi[i] for i in [0,1,2,3,4,5,12,6,13,14,7,8,15,16,9]]+[ai[9],bi[10],bi[11],bi[17],ai[12],bi[18]]
doubts=[]
for n in [5,10,11,16,17,18,19,20,21]:
 x=q[n]
 doubts.append({'location':x['location'],'reading':x['reading'],'alternatives':'hand addition / further or reinforced type impression; glyph secure' if n in [5,10,11,16] else 'origin, hand and verbal role unassigned','confidence':x['confidence'],'reason':x['evidence']})
doubts.append({'location':extra['location'],'reading':extra['reading'],'alternatives':'origin, hand and verbal role unassigned','confidence':extra['confidence'],'reason':extra['evidence']})
notes=r'''### N033.1 — Programme, qualifications and metadata

The heading records “Cours DEA 1977/78 de A. Grothendieck” and the underlined topic “Géométrie arithmétique des polygônes réguliers”. The two paragraphs propose investigation of regular polygons over fields and general base rings, with vector, affine, projective and metric questions in dimensions one, two and three. The text mentions positive characteristic and finite fields, a general n-gon, and a proposed general regular icosahedron over a ring finite over the integers with residue fields of all characteristics. These are course proposals; no construction or proof is supplied on this sheet or checked in this review.

The programme carries its own qualifications: “sans doute”, “Si le temps le permet et si d'autres investigations ne nous retiennent”, and the parenthesis “La caractéristique deux donnera sans doute du fil à retordre !”. The second paragraph calls for active participation and personal work and recommends the parallel C4 course. Its typed “univers fascinant, pleins de mystères”, unaccented opening “A partir”, and spacing before the comma after “retiennent” remain as written. The marginal exclamation and underline of “en commun” have an unassigned hand. No day/month date or author page count appears. The lower-left archive number is 32.

### N033.2 — Reading decisions and their limits

The mathematical vocabulary directed attention to the circumflexes in polygône(s), the upright lowercase n, the doubled Z and the secure C4 designation. The extra Z diagonal is independently visible; its hand encoding is retained with an instrument qualification. The exact ink, rather than a conventional mathematical font, controls these letters. There is no mathematical proof or computation event on this page.

All three readers resolve the deleted s beneath the comma after réflexion. A, B and root recover the earlier e beneath v in avec from its middle bar; C retains o|e. The live v is clear while its inscription method remains open. The opening parenthesis before de fondements is heavier than its closing mate, and the final s is small, narrow and raised. A and root read points(de with no extra blank cell; B and C retain the witness space. Both sides of Z and C4 have an extra blank interval. Their gaps and the existing gap after deux are preserved independently.

Six detached mark groups receive geometric reproductions with origin and verbal role unassigned: the pale loop below affine, point and broken trace below de, left-margin taper, hook below voudrait, pair below active and joined shape at the physical left edge beside le détail. Zero-width TikZ anchors retain their local relation to the associated passage; two source line breaks retain the left-edge attachments. Instrument doubts for Z, v, the reinforced parenthesis and C4 are stated in source comments and the doubts table without adding a doubt about the clear glyphs. H's note already records the marginal ! and underline of en commun, so their equivalent state descriptions generate no H correction rows.'''
rec={'scan':33,'loci':loci,'inventory':ordered,'doubts':doubts,'notes':notes,'check_events':[{'statement_id':'N033.1','date':'2026-11-20','who':'GPT-6 Astra Pro; effort not exposed; root/scan033','type':'carried as background without fault found','outcome':'Course programme, proposed construction and its qualifications reported from the source. No proof or calculation of the polygon/icosahedron claims was performed; the inline mathematical glyph checks are visual reading events.'}],'abbreviations':[{'abbr':x,'expansion':y,'scans':[33]} for x,y in [('DEA','diplôme d’études approfondies'),('A.','initial of the author’s forename'),('C4','course designation C4')]],'consequential':['The overwritten letters are recovered as deleted s after réflexion and deleted e beneath v in avec; the source text is otherwise retained.', 'The doubled Z, extra spaces surrounding Z and C4, adjacency points(de and the small inserted s are preserved from the ink. No proposed mathematical construction is supplied by the transcribers.']}
(R/'decisions/scan033.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'loci':len(loci),'inventory':len(ordered),'doubts':len(doubts),'changes_C':sum(x['diff_C'] for x in loci),'changes_H':sum(x['diff_H'] for x in loci)}))
