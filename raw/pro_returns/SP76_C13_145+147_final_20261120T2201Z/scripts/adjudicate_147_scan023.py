"""Root crop adjudications for scan023; historical one-shot script."""
from pathlib import Path
import csv, json, subprocess, sys
W = Path(__file__).resolve().parents[1]
pg = '147_scan023'
rp = W/'reports'/f'{pg}.json'
r = json.loads(rp.read_text())
assert not r.get('audited')
tp = W/'pages'/f'{pg}.tex'
t = tp.read_text()
repls = {r'\unsure{autismes}': r'\unsure{autismes|conditions}', r'($=$ sur': r'($\bar m$ sur'}
for a,b in repls.items():
    assert t.count(a) == 1
    t = t.replace(a,b)
tp.write_text(t)
for group,field in [('changes','final'),('inventory','first_words_or_objects'),('doubts','reading'),('abbreviations','form')]:
    for q in r[group]:
        for a,b in repls.items():
            q[field] = q[field].replace(a,b)
boxes = {x['box']:[int(x[k]) for k in ('x0','y0','x1','y1')] for x in csv.DictReader((W/'second'/f'{pg}_boxes.tsv').open(),delimiter='\t')}
for q in r['changes']:
    if q['place'] == 'Inserted parenthesis, contracted word':
        q['evidence'] += ' Independent audit B04 retains the clearly separate en and both parentheses. The low initial curves, tall looped middle and dotted ending also admit conditions; that alternative is added without pretending that the compressed internal letters are settled. No p descender or complete morphismes sequence is visible.'
    if q['place'] == 'Opening of the base parenthesis':
        q.update(final=r'$\bar m$', against_C=True, confidence='medium', crop=f'crops/{pg}_second_B09.png', box=boxes['B09'], evidence='The lower part has a pronounced curved entry, a raised join and a shallow extended body; a separate straight bar lies above it. Root compared this crop with the barred-m form in 147_scan022 B07, which has the same detached bar and shallow curved body. It is not two straight equals strokes, and the upper bar is not accounted for by the blind ou. The literal barred m remains unexpanded.')
for q in r['doubts']:
    if q['place'] == 'Inserted parenthesis, contracted word':
        q['alternatives'] = ['autismes', 'conditions']
        q['reason'] = 'En and the enclosing parentheses are clear. The following low initial curves, tall looped middle and compressed dotted ending support the retained contracted candidate but also admit conditions. The middle letters cannot be separated securely; no full morphismes sequence is restored.'
for q in r['notation']:
    if q['form'] == '=':
        q.update(form=r'\bar m', meaning_or_use='Detached straight bar above a curved lower letter body; the same shorthand shape was checked on scan022 B07.')
for q in r['abbreviations']:
    if q['form'] == '=':
        q.update(form=r'\bar m', expansion='même; the letter and bar are retained literally in the transcription.')
    if q['form'] == r'\unsure{autismes|conditions}':
        q['expansion'] = 'If the preferred contracted reading is right, probably automorphismes; conditions remains an alternative reading, so the expansion is conditional.'
for q in r['hand_habits']:
    if q['habit'].startswith('The written contraction after en'):
        q.update(habit='The small raised word after en has low opening curves, a tall looped middle and a compressed dotted ending.', scope='This occurrence remains autismes|conditions; the contraction and its internal letters are not settled.', witness_errors='C gives the expanded automorphismes; H leaves the parenthesis unread. Neither supplies an authoritative reading.')
r['hand_habits'].append(dict(habit='A barred-m shorthand can resemble an equals sign at ordinary scale; its lower stroke is a curved letter body.', places='147_scan023 Before sur une base; compared with 147_scan022 B07', scope='Both occurrences have a detached upper bar and shallow joined lower body. Genuinely straight equals signs elsewhere are retained.', witness_errors='C reads equals on scan023 and H omits the sign.'))
if isinstance(r['notes'],str):
    r['notes'] = [r['notes']]
r['notes'] = [n.replace('The contraction is kept as the doubtful literal autismes; its suggested expansion appears only in the abbreviation list.', 'The raised word is retained as autismes|conditions; any proposed expansion of the first candidate appears only in the abbreviation list.') for n in r['notes']]
r['notes'].append('Independent audit: all four curve symbols retain fraktur X after individual checks of their opposed curves and central cross-strokes, consistent with scan022. The first and final I forms have a separate underline; the two middle forms have only an ordinary lower serif. The long-stemmed loop remains phi|varnothing. The heavy et is live over lighter retracing, with no independent cancellation across both letters. Les has an ascending initial stroke; the ts endings of pts meet the p body at the word baseline and are not separately raised. The quoted phrase is poids marqué: the noun has a looped d, not n followed by a crossed t, and the adjective has no separate final s. The sign before sur une base is revised to barred m after comparison with scan022 B07. The canceled base expression and final des/de remain uncertain. Both clipped edge fragments are preserved, with the lower cancellation state unresolved. The complete lower chi expression was reread; no invariance proof was performed.')
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
first = {x['box']:x['reading'] for x in csv.DictReader((W/'second'/f'{pg}_first.tsv').open(),delimiter='\t')}
ev = {
'B01': ('high','The X consists of two opposed curved strokes and an independent central horizontal cross-stroke, matching the fraktur form individually checked on scan022. Its barred-s index is separate. I has both a lower serif and another underline. The raised MD- has its own leader to courbe. Retain the complete first reading.'),
'B02': ('high','The second X repeats the paired curves and separate transverse stroke. Its s has a distinct bar, while k(s) is plain. The zero is a small closed oval with a following hyphen. The dash encoding is a typographic difference only.'),
'B03': ('medium','The live article begins with an ascending l stroke before the low e and long s. In both pts forms, the t ascender is tall but the final s and p body meet at the same word baseline; no separate superscript level is established. The cancellation crosses the q-shaped terminal loop as well as the obscured first word; the whole ainsi q. candidate remains doubtful. The insertion begins with not-in, plain I and barred s, then et sont; the baseline sont remains live. The whole two-line passage was checked.'),
'B04': ('low','The first parenthetical word is en, with a separate low e curve and n run; it is not ces. The following compressed word has low opening curves, a tall looped middle and a dotted ending. Those traces do not securely distinguish the first contracted candidate autismes from conditions, so the latter is added as an alternative. Both parentheses and the raised placement are clear. A separate strike crosses donc, and no p-descender/full morphismes sequence is supplied.'),
'B05': ('high','The third X has the same opposed curves with a separate middle cross-stroke and barred s. The numeral has an angled cap and straight base, reading 1. The low three-part avec remains, with its first part almost a dot. The whole genus-1 line is retained.'),
'B06': ('medium','The entire formula was inspected. I is retraced but has no distinct second lower line; s has its own upper bar. The empty-marking sign is an oval crossed by a long stem extending well above and below it, so the existing phi/varnothing doubt remains. The heavy e-loop and tall t are legible over lighter retracing; no independent cancellation traverses both letters, so live et and the M0946 resolution stand.'),
'B07': ('high','The fourth ornate X repeats the opposed curves and transverse stroke. Soient begins with an s-shaped hook followed by the o/i cluster and raised dot. De has no separate final s before the opening ticks. Poids has a looped ascending d before its final s, not an n and crossed t. Marqué ends before the closing pair of ticks with no additional s. The zero is a closed small oval. Retain the complete quoted-weight condition.'),
'B08': ('high','The greater-than angle has a separate lower stroke slanting with its lower arm; the numeral has two rounded right lobes and is followed by a dark point. Retain the display and geqslant rendering; the blind geq is the same mathematical sign in different typography.'),
'B09': ('medium','At the opening parenthesis, a straight detached bar sits over a curved lower body with a raised join and extended shallow tail. Direct comparison with scan022 B07 supports barred m, not equals or ou. The live base S has an inward spiral. Both canceled clusters remain covered by the whole doubtful S= candidate; crossing obscures the second sign, so no q or revision order is certified. The underline belongs to types, not its descender.'),
'B10': ('medium','The complete numerical pair and chi expression were reread: both X forms are plain crossed X with hats, O has a separate underline, and final I has a lower serif plus underline with plain subscript s. The ending after invariance has an extended exit and downward hook, retaining des|de rather than forcing de. There are two distinct dark fragments at the right boundary, one beside the chi line and another lower cluster of crossing strokes; both remain physically clipped and unreadable, with the lower state uncertain.')
}
out=[]
for box,(conf,evidence) in ev.items():
    final=first[box]
    for a,b in repls.items():final=final.replace(a,b)
    d=dict(box=box,changed='yes' if final!=first[box] else 'no',confidence=conf,evidence=evidence)
    if final!=first[box]:d['final_reading']=final
    else:d['use_first']=True
    out.append(d)
subprocess.run([sys.executable,str(W/'scripts/record_audit.py'),pg],input=json.dumps(out),text=True,check=True)
