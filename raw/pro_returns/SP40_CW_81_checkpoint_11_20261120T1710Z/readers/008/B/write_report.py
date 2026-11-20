from pathlib import Path
from datetime import datetime, timezone
import json

out = Path('/workspace/scratch/94548b74fbe0/out/readers/008/B')
rows = []
def row(id, location, C, reading, evidence, confidence, kind, diff_C,
        crop=None, bbox=None, doubt=None, source=None, consequence=None):
    d = dict(id=id, location=location, C=C, H=None, reading=reading,
             evidence=evidence, confidence=confidence, kind=kind,
             diff_C=diff_C, diff_H=False, C_doubt_status=doubt,
             readers_crop=crop, bbox=bbox)
    if source is not None:
        d['C_doubt_source'] = source
    if consequence is not None:
        d['mathematical_consequence'] = consequence
    rows.append(d)

row('B008_D01', 'Isolated struck line between the upper coprimality prose and the next (1)',
    r'\deleted{donc si $\unsure{p\ne1|p\ne q}$}',
    r'\deleted{donc si $\unsure{p\ne1|p\ne q}$}',
    'The d ascender, final c, si and a descending p remain visible under the long cancellation. The final character has a right-hand upright and an upper slant favouring 1; intersecting cancellation strokes continue to obscure its head, leaving q supported as the alternative.',
    'low', 'other', False, '02_isolated_cancel.png', [90,379,483,453], 'retained',
    'Doubtful readings: First isolated struck line')
row('B008_D02', 'Second existential line: letter after the second existential sign',
    r'\unsure{\zeta|\delta}', r'\unsure{\zeta|\delta}',
    'A descending upper diagonal turns at the left into a rounded lower stroke with a closed little return. The same form is visible as the exponent in this line and in the later product and assumption. The return does not settle the supplied zeta/delta alternatives.',
    'medium', 'other', False, '04_zeta.png', [548,880,1160,978], 'retained',
    'Doubtful readings: Second existential line')
row('B008_D03', 'Small cancelled subscript below a prime before the second bowl relation',
    r"a_{\deleted{\unsure{0}}}'", r"a_{\deleted{\unsure{0}}}'",
    'The lowered cluster has a rounded outside edge but a substantially filled dark interior. The cancellation is clear; no open oval or alternative complete glyph can be recovered. The candidate 0 remains qualified.',
    'low', 'other', False, '06_a_subscript.png', [403,1052,652,1135], 'retained',
    'Doubtful readings: Before second bowl in or a…')
row('B008_D04', 'Struck word immediately before on a below the ruled hypothesis',
    r'\deleted{\unsure{alors}}', r'\deleted{alors}',
    'Beneath the oblique zigzag, the initial low a, the tall l, a round o, and the final r/s strokes can be followed. The enlargement supports all five letters, with the cancellation retained.',
    'medium', 'other', True, '08_lower_alors.png', [313,1387,775,1455], 'resolved',
    'Doubtful readings: Above last two implications')
row('B008_D05', 'Cancelled predecessor before q squared in the first lower implication',
    r'\deleted{\unsure{p^{2}|p}}', r'\deleted{\unsure{p^{2}|p}}',
    'The lower portion has a p-like descending stem and right bowl. A separate raised cluster survives above it, but the original digit and the cancellation strokes cannot be disentangled. The p-squared candidate and p alternative are retained.',
    'low', 'other', False, '10_lower_p.png', [92,1454,550,1535], 'retained',
    'Doubtful readings: After (1)⇒ in lower left')
row('B008_D06', 'Final equality after the second gamma equals sign',
    r'{\deleted{q}}^{q\alpha-1}',
    'A cancelled lower q, crossed by a returning zigzag, with the live q alpha minus 1 drawn above; reading.tex preserves the stack in TikZ.',
    'The lower oval and right descending q stem are separately visible beneath the crossing strokes. Above, q, alpha, a horizontal minus and 1 are all readable. The upper initial q starts almost directly above the lower q. The physical glyphs and cancellation are resolved; the drawing leaves the algebraic attachment of the raised entry unassigned.',
    'high', 'insertion or placement', True, '12_final_gamma.png', [199,1579,735,1699], 'resolved',
    'Doubtful readings: End of final line; this is a table doubt despite the absence of an unsure macro in C.tex')
row('B008_D07', 'Pale formula after on a below the ruled hypothesis',
    r"p=q,\ {\unsure{a|\alpha}}'=\gamma",
    r"p=q,\ {\unsure{a|\alpha}}'=\gamma",
    'The primed letter has a small closed bowl and a short right-hand stroke. These favour a, while the pale join continues to admit alpha. p=q, its comma, the prime, equality and gamma are readable. The lower comma-like mark visible at the edge of this crop belongs to the C\'est apostrophe on the following line, as its placement in the lower half shows.',
    'medium', 'other', False, '09_pale_formula.png', [760,1382,1014,1457], 'retained',
    'Doubtful readings: Lower line, light addition after on a')
row('B008_D08', 'Detached mark above a in et si a=a0 a-double-prime',
    r"a=a_0a''", r"\overset{\unsure{\cdot|\prime}}{a}=a_0a''",
    'A short dark upright, with a small thickening at its foot, is detached above the left/central portion of a. It survives the enlargement distinctly from the surrounding paper. A dot made with a short stroke and a prime-shaped tick are supported candidates; the mark\'s role and hand remain open.',
    'low', 'omission', True, '05_a_overmark.png', [456,959,849,1043],
    consequence='The extra mark is retained without choosing a mathematical operation or changing the base a.')
row('B008_D09', 'Two-line cancelled parenthesis after alpha-prime=q alpha',
    r"\deleted{(on l'impose sans risque si $p=1$)}",
    'Same words and cancellation state, arranged on two lines and crossed by two separate rising diagonal paths in TikZ.',
    'The left diagonal runs from below the left parenthesis through si and impose. A distinct parallel diagonal runs from below the second row through risque to the top of the closing parenthesis. Both full paths are visible in the complete local crop.',
    'high', 'drawing or diagram', True, '03_parenthesis_cancel.png', [877,579,1358,709])
row('B008_D10', 'First lower ou p=1 cancellation',
    r'\deleted{\text{ou }p=1}',
    'Same cancelled words, with the visible long crossing and its curved lower return drawn explicitly.',
    'The stroke crosses ou and p=1, curves around the right end, then returns beneath the equality and numeral. The distinct lower return is represented in addition to the crossing.',
    'high', 'drawing or diagram', True, '11_lower_cancellations.png', [452,1458,835,1595])
row('B008_D11', 'Second lower cancelled continuation and pale absurde addition',
    r'\deleted{\text{ou }p=1\Longrightarrow p=1}\ \inserted{\text{absurde car }q\nmid a}',
    'The pale inserted absurde car q nondivides a is positioned above the cancelled ou p=1 implies p=1; the crossing rises to the right.',
    'The pale phrase sits between the two implication baselines, directly above the second crossed continuation. Its q, crossed upright and final a are all visible. A single long ascending crossing traverses the old continuation.',
    'high', 'insertion or placement', True, '11_lower_cancellations.png', [452,1458,835,1595])
row('B008_D12', 'Right-hand return arrow beside the final parenthesis and note',
    'Continuous TikZ return arrow from the note\'s south-east corner to its north-east corner; no detached point.',
    'Return arrow starting below the note beside the closing final parenthesis, with a detached round point before its lower horizontal stroke and an explicit left-pointing hooked head.',
    'The small round mark sits just to the right of the final closing parenthesis and is separated from the lower horizontal arrow segment by a visible gap. The shaft rises on the far right and turns left into two curved head strokes. The dot is reproduced graphically, without a punctuation assignment.',
    'high', 'drawing or diagram', True, '14_right_note.png', [840,1446,1374,1646])

inventory = []
def inv(kind, position, first, hand='another unnamed hand'):
    inventory.append(dict(sheet_kind='text', hand=hand,
                          element=f'B008.{len(inventory)+1:02d}', kind=kind,
                          position=position, first_words_or_objects=first,
                          transcribed='yes'))

inv('text','top line','Supposons que q alpha minus alpha prime nonzero alors')
inv('display','upper first implication','(1) implies p divides the binomial sum plus b-prime^(q-1)')
inv('display','upper second implication','p divides q a^(q-1), car p divides b-prime…')
inv('deletion','right end of upper second implication','cancelled nonzero before greater-than zero')
inv('text','below upper implications','or p divides b-prime et b-prime divides b^q…')
inv('deletion','isolated line above next (1)','donc si p non-equals 1 / q')
inv('display','upper-middle next (1)','p divides q donc p=q (si q alpha minus alpha prime nonzero)')
inv('deletion','within preceding display','p=1 ou')
inv('text','line beginning Donc si','Donc si p non-equals q p premier… alpha-prime=q alpha')
inv('insertion','under p premier','ou p=1')
inv('deletion','two lines at right after Donc si paragraph',"(on l'impose sans risque si p=1)")
inv('drawing','across preceding parenthesis','two separate rising diagonal cancellation paths')
inv('text','first existential line above fold','Donc exists b0 in N-star et exists gamma in N tel que b-prime=q^gamma b0^q')
inv('margin note','right of first existential line','q nondivides b0','undetermined hand')
inv('text','line just above fold','de plus b0 divides b et si b=b0 b-double-prime alors b0 bowl-1 b-double-prime ?')
inv('text','first two lines below fold','De même exists a0 in N-star et exists zeta/delta in N… avec a0 divides a… ?')
inv('text','above the a in et si a=a0 a-double-prime','detached short upright, dot/prime candidate','undetermined hand')
inv('text','or line below second existential passage','or a bowl-1 b implies a-prime bowl-1 b-prime implies zeta times gamma=0 (et aussi a0 bowl-1 b0)')
inv('deletion','lower right of a-prime before second bowl','small blacked-out subscript, doubtful 0')
inv('text','Je suppose line','Je suppose désormais que zeta=0 donc a-prime=a0^q')
inv('display','Donc equation above upper horizontal rule','c=b+a0^q=a+q^gamma b0^q')
inv('margin note','two lines at right of c equation','pour q=2 on a, a0=b0=1, gamma=1, b=4, a=3, c=5')
inv('drawing','around numerical example','top and left frame; open right edge; lower side joins the upper long rule')
inv('text','between two long rules',"Je fais l'hypothése suivante si q premier et 1<=i<q alors q divides C_q^i")
inv('drawing','above and below the hypothesis sentence','two long, slightly sloping rules, upper one continuous with the example frame')
inv('text','below lower rule','alors Si q>=3 et q alpha minus alpha-prime>=2… on a')
inv('deletion','before on a','alors')
inv('insertion','pale addition after on a','p=q, a-prime/alpha-prime=gamma','undetermined hand')
inv('display','first lower implication','(1) implies q squared divides q a^(q-1)')
inv('deletion','before q squared','p squared / p')
inv('deletion','right of first lower implication','ou p=1')
inv('drawing','over first lower ou p=1','crossing stroke with a curved lower return')
inv('display','second lower implication','implies q divides a^(q-1)')
inv('deletion','right of second lower implication','ou p=1 implies p=1')
inv('insertion','above preceding cancelled continuation','absurde car q nondivides a','undetermined hand')
inv('text','final line',"Donc gamma=0 ou gamma=… (sous réserve que l'hypothése est vraie)")
inv('deletion','after final gamma equals sign','lower q')
inv('insertion','raised over cancelled lower q','q alpha minus 1; visible placement retained, algebraic attachment unassigned')
inv('drawing','around lower cancelled q','returning zigzag crossing paths')
inv('margin note','three-line lower-right note',"C'est peut-être interessant car ici 2 est mis à part dans l'ensemble des nombres premiers")
inv('drawing','far right beside final parenthesis and note','detached point, lower horizontal stroke, rising return shaft, left-pointing hooked head')
inv('text','bottom-left corner, recorded as archive comment','archive sheet number: 7','another unnamed hand')

report = dict(
    scan=8, reader='B', start_utc='2026-11-20 11:20:56 UTC',
    end_utc=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
    full_image_viewed=True, halves_viewed=True, complete_visual_read=True,
    differences=rows,
    doubts=[
        dict(location='Isolated struck donc si line', reading='p non-equals 1', alternatives=['p non-equals q'], confidence='low', reason='The final character is crossed through its head; the final upright supports 1 most strongly.', crop='02_isolated_cancel.png'),
        dict(location='Second existential letter', reading='zeta', alternatives=['delta'], confidence='medium', reason='Angled top and closed lower return admit both supplied candidates.', crop='04_zeta.png'),
        dict(location='Cancelled subscript below a-prime', reading='0', alternatives=[], confidence='low', reason='Rounded blacked-out patch; no further recoverable mathematical glyph.', crop='06_a_subscript.png'),
        dict(location='Cancelled predecessor before lower q squared', reading='p squared', alternatives=['p'], confidence='low', reason='Raised cluster survives but its original numeral is inseparable from crossing strokes.', crop='10_lower_p.png'),
        dict(location='Pale primed letter after p=q', reading='a prime', alternatives=['alpha prime'], confidence='medium', reason='Small closed body and short right-hand stroke remain insufficiently distinct.', crop='09_pale_formula.png'),
        dict(location='Detached mark above a in et si a=a0 a-double-prime', reading='short upright dot', alternatives=['prime-shaped tick'], confidence='low', reason='The mark is visible but its glyph identity, hand and role remain unsettled.', crop='05_a_overmark.png'),
    ],
    inventory=inventory,
    notes={
        'page_content':'Handwritten divisibility calculations, two factorization passages with question marks, a numerical q=2 example, a sentence between rules labelled an hypothesis by the writer, corrected lower implications, and a concluding right-hand comment. All are transcribed as visible.',
        'author_uncertainty':[
            'A question mark follows each of the two coprimality questions: b0 with b-double-prime, and a0 with a-double-prime.',
            'The writer says “Je suppose désormais que” before zeta=0.',
            'The ruled sentence begins “Je fais l’hypothése suivante”.',
            'The last parenthesis reads “sous réserve que l’hypothése est vraie”.',
            'The right note begins “C’est peut-être interessant”.'
        ],
        'title_date_page_numbers':'No title or date is visible. The lower-left archive numeral is 7 and is recorded only as the required comment. The scan marker is 8. H is an empty file and metadata says nothing.',
        'C_doubt_accounting':'Seven actual rows under the source heading Doubtful readings are mapped individually in B008_D01–D07. D04 and D06 are resolved; the other five are retained. The six notation rows and the two Slips retained rows are recorded as notation/audit material, without invented C-doubt statuses.',
        'mathematics_led_reading_decisions':'No formula was repaired. The final lower q and raised q alpha minus 1 are drawn with their actual relative placement; the algebraic attachment of the raised text is left unassigned. The added mark above a likewise receives no algebraic role. One arithmetic substitution check of the written numerical example was performed and is recorded below; no general proof check was performed.',
        'physical_details':'The example has an open right edge; its bottom is continuous with the upper hypothesis rule. The cancelled parenthesis has two distinct diagonal strokes. The first lower ou p=1 cancellation returns beneath the words. The pale absurde phrase is above the second cancelled continuation. The final return arrow has a detached round point beside its lower start.',
        'crop_boundary_disclosure':'All target loci and their relevant cancellation extents are included. Crop 14 begins within the high apostrophe of C’est and clips part of that already-read contextual stroke; its full reading was available on half b and the overlapping lower edge of crop 09. The target interesting spelling and the complete return arrow are included. No crop was repeated or enlarged a second time.',
        'inspection_limit':'A few pale interior specks within the cancelled parenthesis do not support a further character reading. The mottled upper-right trace was inspected in crop 15; its irregular dispersed dark patches and pale central region supply no coherent glyph candidate. No character has been supplied for these areas.',
        'technical_validation':'A LuaLaTeX compilation attempt stopped before processing reading.tex because the runtime has no lualatex.fmt. No successful compilation or rendered-page validation is claimed; the source and report received a consistency check.'
    },
    notation=[
        dict(location='Upper implications and both coprimality passages', sign='shallow bowl with separately lowered hooked 1', latex=r'\mathrel{\underset{1}{\smile}}'),
        dict(location='First expansion', sign='capital C with raised dotted i and lowered q; matching dotted i in sum and exponents', latex=r"C_q^i,\ \sum_{i=1}^{q-1},\ a^i,\ b'^{\,q-i-1}"),
        dict(location='First existential line and numerical example', sign='forked gamma with rounded lower loop', latex=r'\gamma'),
        dict(location='Both existential lines', sign='doubled N and raised star where present; lowered small zero', latex=r'\mathbb N^*,\ \mathbb N,\ a_0,\ b_0'),
        dict(location='End of upper second implication, crop 01', sign='cancelled nonzero followed by a live greater-than and zero; no witness change', latex=r'\deleted{\ne0}>0'),
        dict(location='Ruled hypothesis, crop 07', sign='rising acute stroke above the e in hypothése', latex='hypothése'),
        dict(location='Final parenthesis, crop 13', sign='rising acute stroke above the e in hypothése; closing round parenthesis', latex='hypothése'),
        dict(location='Right note, crop 14', sign='interessant without a discernible acute over its first e', latex='interessant'),
        dict(location='Right note and final line', sign='peut-être with lexical hyphen and circumflex; à and réserve carry their visible accents', latex='peut-être, à, réserve'),
        dict(location='Below hypothesis and in hypothesis', sign='separate lower slant on comparison signs', latex=r'\geqslant,\ \leqslant'),
        dict(location='Pale lower correction, crop 11', sign='absurde car q crossed upright a, above the crossed old continuation', latex=r'\inserted{\text{absurde car }q\nmid a}'),
        dict(location='Final equality, crop 12', sign='cancelled lower q and live raised q alpha minus 1, retained geometrically', latex=r'\begin{tikzpicture}...\end{tikzpicture}'),
        dict(location='Lower start of return arrow, crops 13–14', sign='detached round point aligned with the initial horizontal stroke; no punctuation role assigned', latex=r'\fill ... circle(.022cm);'),
    ],
    check_events=[dict(
        statement='The numerical example q=2, a0=b0=1, gamma=1, b=4, a=3, c=5 beside c=b+a0^q=a+q^gamma b0^q',
        location='Right of the Donc c equality, full scan approximately [792,1205,1376,1346]',
        type='exact arithmetic substitution',
        result='Using precisely the written assignments, 4+1^2=5 and 3+2^1*1^2=5; both expressions equal the written c=5. This local computation supplies no repair or proof of the surrounding assertions.'
    )],
    crops=json.loads((out/'crop_manifest.json').read_text()),
    brief_feedback=[
        'The supplied C_doubts.txt excerpt omits source-section headings. The parent clarified the seven actual Doubtful readings rows and the two Slips retained rows; this report records that mapping explicitly.',
        'A known upper/lower arrangement can remain algebraically unassigned. For the final q stack, explicit TikZ preserves the ink without forcing an exponent/replacement interpretation.'
    ],
    view_attestation={
        'full_image':{'path':'source/SP40_CW_81_scans/J81-01_81_scan008.jpg','dimensions':[1404,1721],'view_count':1},
        'half_a':{'path':'source/SP40_CW_81_scans/J81-01_81_scan008_a.jpg','dimensions':[1404,940],'view_count':1,'full_scan_y_offset':0},
        'half_b':{'path':'source/SP40_CW_81_scans/J81-01_81_scan008_b.jpg','dimensions':[1404,941],'view_count':1,'full_scan_y_offset':780},
        'crop_count':15,'each_crop_view_count':1,
        'order':'UTC start recorded, packet and brief read; whole once; half a once; half b once; 14 locally enlarged crops, each once, followed during the final audit by one additional tight crop of the upper-right trace. No whole or half was reopened.',
        'processing':'One original full-scan box per locus; PIL autocontrast, LANCZOS enlargement to 2400–3200 px, UnsharpMask; rotation 0 because the targets are upright.',
        'independence':'Only scan008 packet, supplied notation snapshot, brief, preamble, allowed helper, this page’s source images, and own outputs were read. No OCR, internet, other pages, other readers or delegation.'
    },
    counts={'difference_rows':len(rows),'diff_C_true':sum(r['diff_C'] for r in rows),'diff_H_true':0,'actual_C_doubts':7,'C_doubts_resolved':2,'C_doubts_retained':5,'unresolved_reading_loci':6,'inventory_items':len(inventory),'mathematical_check_events':1}
)
(out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report['counts']))
