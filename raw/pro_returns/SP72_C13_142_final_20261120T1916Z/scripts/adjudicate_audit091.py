"""Main-reader audit decision on the visible quotation strokes."""
from audit_support import load, replace_exact, commit

r, a, s = load(91)
c = a['changes'][0]
s = replace_exact(s, c['before'], c['after'])
row = next(x for x in r['changes'] if x['id'] == '091-05')
for key in ['place','c','h','final','c_changed','h_changed','category','kind','marked_in_H','confidence','scan_shows','box','crop','consequential','math_note']:
    row[key] = c[key]
r['notes'] = [
    'The first reader made no mathematical proof check while collating the ink. The main reader subsequently recorded the targeted conditional kernel-stability check 142-091-R1 below. Neither mathematical expectation nor that check decides the ambiguous lemma arrow.'
    if note.startswith('No mathematical proposition was independently proved or used to decide the ink.') else note
    for note in r['notes']
]
r['notes'].append('The complete second reading revises the quotation boundary at inductibilité. The crop shows d, one apostrophe, the low initial i with its higher-right dot, and the following word; no further opening pair is visible. The two closing ticks remain. The transcription deliberately leaves that quotation unbalanced rather than supplying absent opening marks.')
commit(91, r, a, s,
    'Complete independent second reading by reader_c; all 12 inventory elements and all 17 inherited change loci were reviewed. The main reader reused scan091_root_091-05 and accepted removal of the unsupported opening quote pair at existing locus 091-05, retaining the visible closing pair. The three existing doubts remain. No new crop or mathematical check event.',
    [{'id': c['id'], 'decision': 'accepted; existing locus 091-05 revised',
      'reading': c['final'], 'evidence': c['scan_shows'], 'crop': c['crop'], 'confidence': 'medium'}])
