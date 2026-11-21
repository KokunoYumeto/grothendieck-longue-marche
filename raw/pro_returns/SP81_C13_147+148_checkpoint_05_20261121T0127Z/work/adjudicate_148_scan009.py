from pathlib import Path
from datetime import datetime, timezone
import csv, json, subprocess, sys

root=Path(__file__).resolve().parents[1]
p='148_scan009'
f={r['box']:r['reading'] for r in csv.DictReader((root/'second'/f'{p}_first.tsv').open(),delimiter='\t')}
s={r['box']:r['reading'] for r in csv.DictReader((root/'second'/f'{p}_second.tsv').open(),delimiter='\t')}
rp=root/'work'/f'{p}_final.json'; report=json.loads(rp.read_text())
assert not report.get('audit')
final=dict(f)
edge=r'''\unsure{\begin{tikzpicture}[x=.04em,y=-.04em,line cap=round,line join=round,baseline=-.15ex]
\draw[line width=.35pt] (0,14) .. controls (5,14) and (13,8) .. (11,3)
 .. controls (10,0) and (7,0) .. (6,3)
 .. controls (3,8) and (8,12) .. (23,14);
\end{tikzpicture}}'''
final['B04']=f['B04'].replace(r'\text{groupe des unités}',r'\text{groupe des unités '+edge+'}')
extra=r'''% Further exposed returns and white apertures checked in the blind audit.
\draw[line width=.45pt] (326,1182) .. controls (331,1177) and (336,1175) .. (341,1177);
\draw[gray,line width=.35pt] (329,1189) .. controls (341,1192) and (354,1192) .. (365,1191);
\draw[line width=.5pt] (531,1074) -- (539,1070) -- (537,1079);
\draw[line width=.55pt] (388,1143) -- (396,1148) -- (394,1153);
\fill[white] (317,1183) circle[radius=1.0];
\fill[white] (349,1132) circle[radius=.8];
\fill[white] (384,1185) circle[radius=.9];
'''
final['B06']=f['B06'].replace('% Written labels;',extra+'% Written labels;')
final['B10']=f['B10'].replace('comb.',r'\unsure{comb.|orient.}')
final['B12']=f['B12'].replace(r'\unsure{centre}',r'\unsure{centre|avec}').replace(r'\inserted{origine} étant',r'\inserted{origine} \unsure{étant|\inserted{étant}}')
final['B14']=f['B14'].replace('X_S=',r'X_S\unsure{=|\simeq}',1)
e={
'B01':'The manuscript 3 stands above the heading; the raised ell. and its attachment precede anharmoniques. The differing serialization moves the page-number macro, while the first reading keeps its observed order.',
'B03':'The whole identity has Z/6Z, mu with lowered 6, and C. The raised alg. remains compressed and locally uncertain. The Q has the existing single outline. Beneath the radical, the short line has a right upturn and a separate zeta below it; the first actual TikZ contour retains both features.',
'B04':'The lower de has a looped opening and a low separate line, and the cancellation reaches its terminal portion. The canceled ring expression ends in a slash. The equality upper stroke meets the cancellation, so the existing local doubt remains. The complete formula below has 1+T+T squared. At the extreme right end of the upper line, x1635–1649 has a small dark loop followed by a short tail through about x1659 at the scan edge. A complete additional de cannot be separated from these strokes. The blind reader independently withdrew the complete-word confidence in a saved supplement. Root preserves the exposed loop and tail graphically, with unresolved alphabetic reading and attachment, rather than completing hidden letters.',
'B05':'The last digit has a curved top, compressed waist and lower return. Both readers prefer 3, and the first local uncertainty remains because the waist is not fully exposed. The 2i before pi is retained.',
'B06':'The six ringed points, six additional ray marks, central mark, two separate small right-hand marks and three outer terminal marks remain individually drawn. The second count of thirteen counted the main interior marks and omitted the additional exterior marks from that subtotal. Root also sees three small white apertures in filled interior marks, the short curve just right of the center, a lower retrace along the right radius, a return across the upper-right ring, and a lower wing at the remote upper-right terminal; these are added as actual contours. The first drawing retains the downward curl at the heavy top edge, explicit dots and gaps, pale construction fragments, central 0|o, and endpoint uncertainty. No generic completion of the faint strokes is introduced.',
'B07':'The canceled second word begins with a tall descending stem and several low joined returns. Those exposed parts favor the existing pourra reading, while the strike hides the medial joins. The blind construit does not expose an independently readable con- sequence. The existing On pourra|On pose alternatives and the clearly raised On pose are retained.',
'B08':'The final short upper stroke is immediately above the left bracket upright, and ends before the main upper sweep of zeta. This supports the detached bracket cap already recorded in the first reading. The upper part of the canceled S remains crossed, and its uncertainty stays. The whole quotient and lowered 1 were checked.',
'B09':'Z/6Z is visibly below the wedge, with the final S back above it. Both readers give that placement; mathbin and display delimiters account for the difference.',
'B10':'The last abbreviated word has a low rounded opening, a compressed middle, a tall final stem with a low return, and a separate dark terminal dot. Those parts favor comb.; the middle remains compressed enough to retain the blind orient. alternative. The heading underline and absence of a period after Construction remain as first read.',
'B11':'The end of the adverb stretches into a long low run ending in a sharply raised return. Separate full-word ending letters remain unexposed. The existing contracted euclidiennem with raised t remains first, and euclidiennement remains the alternative. The open initial c and following a-loop support canonique; the last word retains the clear d-loop and low linked ans of dans.',
'B12':'The initial word has an overworked first region, so vectoriel remains uncertain. Under the later strike, the low first loop and joined middle are compatible with both centre and avec; neither exposes every letter. Origine is clearly above that strike. Etant continues on the raised level, and its placement alone does not settle whether it belongs to the insertion; both states are recorded with the same word. The final t and linked ending favor étant over en.',
'B13':'The canceled noun has a tall initial loop, two further tall strokes and a small detached dot above the later low run. These support the existing lattice reading, with the obscured joins still uncertain. Reseau is raised above that word. Both readers see V_S in the preceding baseline, and it is retained literally.',
'B14':'The small first relation has a short upper hooked stroke over a lower horizontal stroke. Equals remains the preferred reading, with simeq retained as the blind alternative. The second relation clearly has the raised wave over a lower bar. The full formula retains lowered S, elliptic index 1, V_S and Gamma_S.'}
pp=root/'pages'/f'{p}.tex';page=pp.read_text()
target=r'\simeq\text{groupe des unités}'
assert page.count(target)==1
page=page.replace(target,target[:-1]+' '+edge+'}')
for b in ['B06','B10','B12','B14']:
 assert page.count(f[b])==1,(b,page.count(f[b]))
 page=page.replace(f[b],final[b])
pp.write_text(page)
for ch in report['changes']:
 if ch['id']==p+'-04':ch['final']=final['B06'];ch['evidence']+=' Blind audit: '+e['B06'];ch['crop']=p+'_second_B06.png'
 if ch['id']==p+'-10':ch['final']=final['B12'];ch['evidence']+=' Blind audit: '+e['B12'];ch['crop']=p+'_second_B12.png'
report['changes'].append(dict(id=p+'-13',place='Upper units continuation, extreme right edge after the readable unités cluster',C='[edge fragment not separately represented]',H='[edge fragment not separately represented]',final=edge,evidence=e['B04'],crop=p+'_second_B04.png',box=[1030,773,1671,1016],confidence='medium',kind='omission',error_sheet_kind='Omissions',differs_C=True,differs_H=True,marked_in_H=False,consequential=False))
for d in report['doubts']:
 if d['reading']==r'\deleted{\unsure{centre}}':
  d['reading']=r'\deleted{\unsure{centre|avec}}';d['alternatives']='centre | avec';d['reason']+=' Blind crop B12 exposes low loops but not all intervening letters.'
report['doubts'].extend([
 dict(place='Upper units continuation, fragment at the right scan edge',reading=edge,alternatives='Small loop and tail retained graphically; de is a tentative alphabetic candidate, and attachment to the preceding cluster remains unresolved',confidence='low',reason=e['B04']),
 dict(place='Construction paragraph, abbreviation following hexagone',reading=r'\unsure{comb.|orient.}',alternatives='comb. | orient.',confidence='medium',reason=e['B10']),
 dict(place='Construction paragraph, placement of étant after raised origine',reading=r'\unsure{étant|\inserted{étant}}',alternatives='Continuation on the raised level | word included in the insertion',confidence='medium',reason=e['B12']),
 dict(place='Final displayed quotient, relation immediately after X_S',reading=r'\unsure{=|\simeq}',alternatives='= | simeq',confidence='medium',reason=e['B14'])
])
report['notes']+='\nBlind audit: the compressed comb. and the first relation in the final quotient now retain local alternatives. The canceled word under origine retains centre|avec, and the raised position of étant remains explicitly uncertain. The lattice drawing retains all first-read exterior marks and receives the additional small white apertures and exposed returns described in the audit.'
rp.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
diffs=json.loads((root/'second'/f'{p}_comparison.json').read_text())['differences']
choices=[]
for d in diffs:
 b=d['box'];changed=final[b]!=f[b]
 choices.append(dict(box=b,choice='literal' if changed else 'first',**({'final':final[b]} if changed else {}),changed=changed,evidence=e[b],confidence='low' if b=='B07' else ('high' if b in ('B01','B09') else 'medium')))
(root/'work'/f'{p}_audit_choices.json').write_text(json.dumps(dict(reader='audit_b',choices=choices),ensure_ascii=False,indent=2)+'\n')
stamp=datetime.now(timezone.utc).isoformat()
with (root/'work/root_views.tsv').open('a') as out:
 for b in range(1,16):out.write(f'{stamp}\t{p}_second_B{b:02d}.png\tRoot personally displayed and inspected this blind crop; B07 and B08 were individually redisplayed after a truncated combined output, and B06 and B04 revisited for the compared endpoints.\n')
subprocess.run([sys.executable,str(root/'scripts/prepare_audit_decisions.py'),p],check=True)
subprocess.run([sys.executable,str(root/'scripts/record_audit.py'),p],check=True)
