"""Main-reader decisions after personally inspecting all 19 differing crops."""
from pathlib import Path
from datetime import datetime, timezone
import csv, json, re

B = Path(__file__).resolve().parents[2]
stem = B/'second/148_scan023'
with Path(str(stem)+'_comparison.tsv').open() as f:
    comp = {r['box']: r for r in csv.DictReader(f, delimiter='\t')}
with Path(str(stem)+'_boxes.tsv').open() as f:
    boxes = {r['box']: r for r in csv.DictReader(f, delimiter='\t')}
rp = B/'reviews/148_scan023.json'
p = json.loads(rp.read_text())
page = B/'pages/148_scan023.tex'
t = page.read_text()
assert not p.get('second_audit')

def graphic(key):
    s = comp[key]['second']
    return s[s.index(r'\figure{'):]

finals = {}
# Overlapping printing is transcribed in its own text/table elements already.
finals['B023-05'] = '\n'.join(x for x in graphic('B023-05').splitlines()
                             if not x.startswith(r'\node['))
finals['B023-05'] += '\n% crop-candidate: scan 23'
finals['B023-06'] = graphic('B023-06').replace(r'\unsure{?|\beta}', r'\unsure{\beta|?}')
finals['B023-08'] = r'\unsure{G|A|a}_{\unsure{4}}'
for key in ['B023-11','B023-13','B023-14','B023-16','B023-17','B023-18']:
    finals[key] = graphic(key)
finals['B023-19'] = (r'\unsure{\deleted{2}\inserted{4}|\deleted{4}\inserted{2}}'
                    r'\text{ carrés}\\8\text{ arêtes}\\4\text{ sommets}')
diag = comp['B023-20']['first']
diag = diag.replace(r'\arrow[d,leftrightarrow,very thick]',
                    r'\arrow[d,shift right=.35ex,very thick]', 1)
diag = diag.replace(r'\arrow[d,leftrightarrow,very thick]',
                    r'\arrow[d,shift left=.35ex,very thick]', 1)
diag = diag.replace(r'\unsure{E_Q|\overline E_Q}\arrow[r,very thick]',
                    r'\unsure{E_Q|\overline E_Q}\arrow[u,shift right=.35ex,very thick]\arrow[r,very thick]')
diag = diag.replace(r'\unsure{E_H|\overline E_H}',
                    r'\unsure{E_H|\overline E_H}\arrow[u,shift left=.35ex,very thick]')
finals['B023-20'] = diag

for key, val in finals.items():
    if key == 'B023-19':
        old = r'$\deleted{2}\inserted{4}$ carrés'
        new = r'$\unsure{\deleted{2}\inserted{4}|\deleted{4}\inserted{2}}$ carrés'
    else:
        old, new = comp[key]['first'], val
    assert old in t, (key, 'First reading not found in page')
    t = t.replace(old, new, 1)
# Avoid two adjacent identical crop-candidate comments if the box excluded it.
t = t.replace('% crop-candidate: scan 23\n% crop-candidate: scan 23',
              '% crop-candidate: scan 23')

ink = {
'B023-01': 'The last visible date character retains the curved left and right sides of 0 at the cut edge. No missing continuation is supplied. The raised curved apostrophe is handwritten. Paragraph and texttt wrappers do not change the reading.',
'B023-02': 'The seven codes and hour values agree. The last value has two lobes in its terminal 8, and the decimal separators have low tails. The two covered HEURES readings remain doubtful. Splitting the table into additional columns changes no ink reading.',
'B023-03': 'POUR and the terminal ATION DE are visible, but heavy front-side patches obscure the intervening beginning. The crop neither establishes nor excludes the proposed LA. Retain the whole phrase as an explicitly unresolved low-confidence reading; do not treat the blind omission of LA as a legible deletion.',
'B023-04': 'The separator after 418 is below the digit body and has a descending tail, like the commas in the table. Thus 418,60 remains. The following phrase is still patch-covered; partial R and E CES survive but do not resolve PRIX DE CES. The first doubt remains, rather than claiming a complete reading from the second version.',
'B023-05': 'The crop shows irregular lobed black patches, a hooked central stroke, four unequal radiating shapes, short separated strokes and a top blot over the printing. The independent explicit outline follows their irregular boundaries and gaps more closely than the former smooth ellipses. Adopt that tracing. Printed fragments in this overlapping crop are already transcribed in the table and printed lines and are not duplicated.',
'B023-06': 'Four vertices and six edges agree. The second tracing preserves the incomplete upper arc as two separated parts, the partial retracing of the central edge, the three small triangular edge marks, and the two wings of the broad external arrow. Retain beta/question-mark doubt at the left; no certain letter is inferred from the drawing.',
'B023-07': 'The first count contains both a lower looped 6-shaped remnant and the angular crossbar/right stem of 4; the long strike crosses the whole corrected number and hexagones. The second line is also struck. The brace and separate upward-curved arrow lead to the clear live 8 triangles, 4 sommets d’ordre 6, and 12 arêtes. Preserve these layers and the clear word ordre; the second version loses the underlying numeral.',
'B023-08': 'The large form is an open rounded loop with an independent tall right return, extending below the bowl. This favors G, but the same strokes admit an open cursive A/a. There is no securely separate A crossbar. Reopen the base-letter doubt instead of selecting A from a symmetry expectation. The current index is 4-shaped and heavily retraced; its prior state remains unknown.',
'B023-09': 'The two live initial signs have the same tall doubled left strokes and joining bar: the mu form already recorded for this page. Their indices are 6 and 4. Each denominator has the curved top, descending oblique and rightward foot of 2, not n. The canceled initial group remains obscured; the blind H/C guesses do not resolve it. The mesh fragment belongs to the separately transcribed lattice.',
'B023-10': 'The initial O of the second line is a tall angular closed bowl, materially higher than the r/i/e/n bodies and the lowercase o in the other heading. Preserve capital Orienté and the two separate underlines.',
'B023-11': 'The nine horizontal levels and eight triangular bands agree. The independent tracing more closely follows the unequal vertices, explicit gaps and individual hatching. It also follows the descending leftward end of the right bold oblique and the curved end strokes, whereas the first version regularized several ends into generic arrows. Adopt the literal paths and omit the overlapping formula fragments, which are already transcribed separately.',
'B023-13': 'The two versions preserve the same principal polyhedral outline. The crop additionally shows disconnected short internal strokes, partially retraced edges, and V-like endpoint strokes at the central and bottom vertices. The second paths reproduce those details without assigning a new direction to the V-like marks. The partial heading belongs to the preceding text and is not repeated.',
'B023-14': 'All four sides are heavily retraced, the top has a narrow doubled trace, and a separate thin stroke lies outside the right edge. The lower-left dark patch is larger than the lower-right corner patch. Adopt these visible weights and partial retracings; do not add a vertex label.',
'B023-16': 'The top and right strokes stop short of each other. The left shaft ends in a downward hook/head, with a second disconnected angled stroke at its lower right; the upper-left also has a detached angled mark. The second literal paths preserve these gaps and paired marks better than the first generic arrow and short tick.',
'B023-17': 'Five long verticals, six uneven horizontal levels, and the diagonals are visible. The independent paths retain the open top and bottom sections, small left-of-center arrow-like strokes, separate top/right corner marks, and low right vertical extension. These replace the overly regular generic arrows in the first version. No algebraic labels or unstated orientation are supplied.',
'B023-18': 'The outline has a gap below the upper-right dark vertex, an open lower-right ring with a short outward stroke, and a curved rotation mark with visible interruptions before its detached upper head. Adopt these gaps and the literal head instead of the continuous first arrow.',
'B023-19': 'The first numeral visibly superposes a curved 2 head and diagonal with a 4 crossbar and long right descending stem. The latter favors a final 4, but the black intersections do not establish stroke order securely. Retain 2-to-4 first, with the reverse order explicit as an alternative. The 8 arêtes and 4 sommets are clear. No Euler-characteristic expectation is used to choose an order.',
'B023-20': 'The two upper curved arrows and lower rightward arrow agree. Each vertical connection visibly contains two parallel dark stems and both an upper and lower head; preserve both stems rather than merging them into one shaft. Their semantic status as separate maps versus graphic retracing is not asserted. The upper-left E is heavily retraced, insufficient to establish a distinct double-struck alphabet. Each lower E has only three horizontals in total, so its detached top remains ambiguous between the letter top and an overbar. Keep those doubts and both epsilon readings.',
'B023-21': 'Both readings are the pencil number 22: each digit has a rounded head, oblique descent and rightward foot. The margin wrapper already records its location; mspage versus margin is not a change of the numeral.'
}
entries=[]
for key,c in comp.items():
    if c['different']!='yes': continue
    d=dict(box=key,choice='revised' if key in finals else 'first',viewed_by_main=True,
           ink=ink[key],confidence='low' if key in ['B023-03','B023-04','B023-08','B023-09']
           else 'medium' if key in finals or key=='B023-07' else 'high')
    if key in finals:d['final']=finals[key]
    entries.append(d)

places={'B023-05':'upper ink figures','B023-06':'tetrahedron drawing',
        'B023-08':'isolated group','B023-11':'triangular lattice','B023-13':'pencil polyhedron',
        'B023-14':'small parallelogram','B023-16':'three-sided open drawing',
        'B023-17':'square lattice','B023-18':'lower-left rotation parallelogram',
        'B023-19':'square count correction'}
for key,place in places.items():
    row=next(x for x in p['changes'] if x['place']==place)
    b=boxes[key]
    row.update(final=finals[key],ink=ink[key],crop=f'crops/second/148_scan023/{key}.png',
               box=[int(b[k]) for k in ['x0','y0','x1','y1']],
               confidence='low' if key=='B023-08' else 'medium')
key='B023-20';b=boxes[key]
p['changes'].append(dict(place='vertical connections in framed diagram',
    c=r'\arrow[d,leftrightarrow] (one vertical shaft on each side)',
    h=r'\arrow[d,leftrightarrow] (one vertical shaft on each side)',
    final=finals[key],ink=ink[key],crop=f'crops/second/148_scan023/{key}.png',
    box=[int(b[k]) for k in ['x0','y0','x1','y1']],confidence='medium',
    kind='drawing or diagram',against_c=True,against_h=True,math=True))
for d in p['decisions']:
    if d['id']=='M0245':
        d.update(decision='undecided',reading=finals['B023-08'],ink=ink['B023-08'],
                 crop='crops/second/148_scan023/B023-08.jxl',confidence='low')
for u in p['unresolved']:
    if u['place']=='isolated group index':
        u.update(place='isolated group letter and index',reading=finals['B023-08'],
                 reason=ink['B023-08'],alternatives=r'G, A, or a; current 4 with unknown prior index',
                 crop='crops/second/148_scan023/B023-08.jxl',confidence='low')
p['unresolved'].append(dict(place='square count overtrace',
    reading=r'\unsure{\deleted{2}\inserted{4}|\deleted{4}\inserted{2}}',
    alternatives='2 corrected to 4 favored; reverse order not excluded',reason=ink['B023-19'],
    crop='crops/second/148_scan023/B023-19.jxl',confidence='medium'))
for h in p['hand_log']:
    if h['habit'].startswith('A large open loop'):
        h.update(habit='An open rounded loop and an independent descending right stroke admit G and cursive A/a; this single occurrence does not establish a general hand rule.',
                 witness_effect='Blind reader favored A/a; main reader reopened the base-letter doubt, favoring G provisionally.')
    if h['habit'].startswith('Corrections of numerals'):
        h['holds_at_every_observed_occurrence']='Superposed numeral strokes occur in both places, but their order is not equally secure.'
        h['witness_effect']='The square count now explicitly retains uncertainty about 2-to-4 versus 4-to-2; no general direction of overwriting is inferred.'
for note in p['notes']:
    if note['id']=='N023-04': note['note']='The square count visibly superposes 2 and 4; 2 corrected to 4 remains favored, with the reverse order now retained as a doubt. Eight edges and four vertices are clear. No topological count is used to settle stroke order.'
    if note['id']=='N023-06': note['note']=ink['B023-08']
p['notes'].append(dict(id='N023-BLIND',type='audit',place='independent second reading',
    note='All 19 literally differing boxes were personally inspected by the main reader. Eight drawing traces were refined, the framed diagram retains both visible vertical stems, and doubts were reopened in the isolated group letter and the order of the square-count overtrace. Printing or formula fragments overlapping a drawing crop were not duplicated. Drawing refinements do not constitute proofs of the geometric claims.'))

page.write_text(t)
rp.write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n')
Path(str(stem)+'_adjudications.json').write_text(json.dumps(entries,ensure_ascii=False,indent=2)+'\n')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (B/'reviews/visual_log.tsv').open('a') as f:
    for e in entries:f.write(f'{now}\t023\tcrops/second/148_scan023/{e["box"]}.png\tMain reader viewed differing blind box; {e["ink"]}\n')
print('023: all 19 crop decisions and page corrections recorded; first readings unchanged.')
