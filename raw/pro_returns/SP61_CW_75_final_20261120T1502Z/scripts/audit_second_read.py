"""Recorded second-reading edits; execute only the newly audited scan once.

The reader, not this script, performed the image comparison. No image analysis,
OCR, mathematical normalization or witness inference is performed here.
"""
import csv
import sys
from reading_support import ROOT, PREFIX, read_table, append_md, log, doubts, assemble, build_changes, utc

def write_table(name, rows):
    with (ROOT/name).open('w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]), delimiter='\t')
        w.writeheader()
        w.writerows(rows)

def replace_in(name, old, new):
    p = ROOT/name
    s = p.read_text()
    if old not in s:
        raise RuntimeError('Expected text absent: '+name)
    p.write_text(s.replace(old, new))

def finish(scan, description):
    append_md(PREFIX+'_audit.md', f'## Scan {scan:03} — second image reading\n\n{description}\n\nCompleted {utc()}.')
    assemble()
    build_changes()
    log(f'scan {scan:03} audited')

def audit17():
    name='pages/J75-02_75_scan017.tex'
    replace_in(name, r'\operatorname{Isom}_{\mathcal C}', r'\operatorname{Isom}_{C}')
    p=ROOT/name
    p.write_text(p.read_text().replace(r'\operatorname{Isom}_{C}', r'\operatorname{Isom}_{\unsure{C|\mathcal C}}', 1))
    rows=read_table('reading_decisions.tsv')
    for r in rows:
        if r['id']=='S017-011':
            r.update(final=r'\unsure{C|\mathcal C}', against_C='yes', against_H='yes', consequence='The repeated category letter is C; ordinary versus calligraphic alphabet remains uncertain rather than being silently fixed as e or calligraphic C.')
            r['evidence']+=' Second reading of both halves, with the recurring category forms on scans 018–019 and 022: the letter is C, but the inward curl does not establish a calligraphic alphabet.'
        elif r['id'] in ['S017-016','S017-019']:
            r.update(final='C', against_C='no', against_H='yes')
            r['evidence']+=' Second reading: the open form is retained as plain C, governed by the alphabet doubt at the first occurrence.'
    write_table('reading_decisions.tsv',rows)
    doubts(17, [('first Isom subscript and two later occurrences',r'\unsure{C|\mathcal C}',r'\mathcal C','medium','Second reading identifies the recurring letter C but does not securely distinguish its typographic alphabet. The later occurrences use plain C under this first alphabet doubt.')])
    replace_in(PREFIX+'_hand_log.md', 'Across these three occurrences the notation is read `\\mathcal C`. C’s first candidate was e, and its two later forms were plain C; H consistently supplied calligraphic C. This is an interpretation of the recurrent letter, not a silent correction of an isolated e.', 'Across these three occurrences the letter is C. The second reading qualifies the first pass: an inward curl does not establish a calligraphic alphabet. The first occurrence is `\\unsure{C|\\mathcal C}`, the next two plain C. C’s first candidate was e; H consistently supplied calligraphic C. This alphabet doubt also governs the category C family on scans 018–019 and 022.')
    replace_in(PREFIX+'_doubts.md', '`\\mathcal C` is the repeated category subscript on the three Isom expressions. Its first form curls inward like e; subsequent forms are open.', 'The repeated category subscript on the three Isom expressions is C. The second reading changes the first pass’s overconfident calligraphic choice to `\\unsure{C|\\mathcal C}` at the first occurrence, plain C thereafter. Its first form curls inward like e; subsequent forms are open.')
    replace_in(PREFIX+'_doubts.md', 'The seven remaining doubt loci are retained', 'The eight remaining doubt loci are retained')
    finish(17, 'Read the upper and lower halves in full against the consolidated fragment, including the mixed-structure family, cancelled heading, all four correspondences, evaluation formula and final crossed attempt. The previous tool output containing the halves had been truncated before it was visible; the accessible displays used here are the actual second reading. Qualified the category alphabet at three Isom subscripts (S017-011, S017-016, S017-019); retained C as the recurring letter and kept ordinary/calligraphic uncertainty explicit. Rechecked the detached first P bar, source bars versus arrowheads, muni without s, insertion attachment and cancelled `(ug`. No extra crop was taken and no other reading changed.')

def audit24():
    replace_in('pages/J75-03_75_scan024.tex', r'\unsure{:|à}', r'\unsure{à|:}')
    rows=read_table('reading_decisions.tsv')
    rows=[r for r in rows if r['id']!='S024-007']
    for r in rows:
        if r['id']=='S024-008':
            r['id']='S024-007'
    write_table('reading_decisions.tsv',rows)
    rows=read_table('remaining_doubts.tsv')
    for r in rows:
        if r['scan']=='24' and r['line']=='before celle de':
            r.update(reading='à', alternatives=':', reason='Crop (1234,400,1280,459), reviewed through the second half in the second reading: the lower short stroke and upper accent resemble the reduced à before à la donnée / à E on scan 018 and à celle on scan 019, and the similar prose marks on scan 025. This recurring hand favours à; the two-point punctuation reading remains possible.')
    write_table('remaining_doubts.tsv',rows)
    replace_in(PREFIX+'_hand_log.md', 'The literal colon outline is preferred cautiously to à; this does not establish a rule for other à occurrences.', 'The first pass preferred a colon, but the second reading compares the same reduced à forms on scans 018, 019 and 025 and prefers à, with colon retained as an alternative. This does not turn the clear colon after G on scan 019 into a word.')
    replace_in(PREFIX+'_doubts.md', 'The first overwritten letter, donnée/donné ending, and colon/à remain explicitly doubtful after their single crops.', 'The first overwritten letter and donnée/donné ending remain doubtful after their single crops. The second reading prefers à over colon before celle de by the recurring two-stroke à habit, while retaining colon as an alternative. This agrees with C’s and H’s preferred word, so the former first-pass change row is removed as certainty-only.')
    replace_in(PREFIX+'_notes.md', '“contour.” on scan 024', '“contour” (without a stop) on scan 024')
    replace_in(PREFIX+'_notes.md', 'It does not resolve the two tiny marks before celle de: the transcription preserves colon as the closer visible shape with à as alternative, without correcting the sentence.', 'The two tiny marks before celle de are addressed by the handwriting comparison, not by the proof: the second reading prefers the reduced word à, matching the same accent-plus-short-stroke form on scans 018, 019 and 025, while retaining colon as an alternative.')
    finish(24, 'Read the landscape sheet across both halves, including the overwritten factor names, inserted T, exercise labels and the isolated curved lower stroke. The mark before celle de has the same reduced à form seen elsewhere in this run; changed the first-pass colon-first ordering to à-first while keeping the punctuation alternative. Both witnesses already preferred à, so this is now a certainty-only locus: former S024-007 was removed from the difference table, and the following free-stroke row was renumbered S024-007. All other readings were retained; no extra crop was taken.')

def audit25():
    rows=read_table('reading_decisions.tsv')
    rows=[r for r in rows if r['id']!='S025-018']
    write_table('reading_decisions.tsv',rows)
    replace_in(PREFIX+'_notes.md', 'The reduced two-mark à in the prose resembles the doubtful mark on scan 024; the second reading will compare these occurrences as one handwriting habit.', 'The reduced two-mark à in the prose confirms the recurring handwriting habit used in the second reading of scan 024. That page now prefers à but retains the punctuation alternative.')
    append_md(PREFIX+'_doubts.md', 'The emphasized compatibility heading is underlined in the fragment. H uses italics for the same words; this is treated as a rendering-convention difference, not an additional collation locus. The former first-pass S025-018 row is therefore excluded from the final counts.')
    finish(25, 'Read both halves in full against the consolidated fragment, including all three diagrams, the small old terms and the quadratic hypothesis. Reconfirmed the shortened words without added stops, the explicit orthonormal-basis bracket, the plain/doubled R distinction, both k labels in the bottom diagram and the reduced à habit. Reviewed the existing det_arrow crop only: the small group beneath det=s is still possibly an earlier crossed sgn and possibly smear, so the low-confidence mark covering both reading and deletion status remains. No additional crop or source-text change. Removed former S025-018 from the collation/counts because italic versus underlined presentation of the same emphasized heading is a macro/convention difference alone.')

if __name__=='__main__':
    n=int(sys.argv[1])
    if f'scan {n:03} audited ' in (ROOT/'progress.log').read_text():
        raise RuntimeError('This scan is already audited; do not repeat an audit record.')
    if n==17:
        audit17()
    elif n==24:
        audit24()
    elif n==25:
        audit25()
    else:
        raise RuntimeError('No recorded audit for this scan yet.')
