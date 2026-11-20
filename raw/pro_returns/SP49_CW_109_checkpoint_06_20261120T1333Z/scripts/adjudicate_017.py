"""Main-reader decisions after comparison and three inspected crops."""
from common import *
R=load_page(17)
texts={r:(W/f'readers/017/{r}/reading.tex').read_text() for r in 'ABC'}
assert normalized(texts['A'])==normalized(texts['C'])
assert normalized(texts['B'].replace(r'\unsure{or|+|\&}',r'\unsure{or|\&}'))==normalized(texts['C'])
viewed=[f'readers/017/C/crops/{x}' for x in ['03_reflections_underline.jpg','04_modelizer_quotation.jpg','05_centuries_connector.jpg']]
decisions=[]
for i,x in enumerate(R['C']['changes']):
 d=copy.deepcopy(x);d['final']=d.pop('reading');d['crops']=[f'readers/017/C/'+d.pop('crop')]
 d['readers']={r:(R[r]['changes'][i]['reading'] if i<2 else (r'\unsure{or|+|\&}' if r=='B' else r'\unsure{or|\&}')) for r in 'ABC'}
 if i==0:
  d['kind']='other';d['evidence']='Main reader inspected the retained crop: the left rule is below Re; the right rule begins directly below the left edge of c, beyond the preceding e, and continues to s. All three readers correct the same extent.'
 elif i==1:
  d['kind']='other';d['confidence']='high';d['evidence']='Main reader inspected one solid tapered opening stroke with no second branch, and the two-legged closing mark. All three readers resolve the opening to one stroke; the asymmetric quotation is preserved.'
 else:
  d['kind']='other';d['evidence']='Main reader inspected the closed horizontal left loop, descending stem and short rightward shoulder. The closed loop excludes a plain plus, so A/C are adopted against B at that alternative. Compressed or is favoured, but the joined strokes do not securely exclude a cursive ampersand; uncertainty remains.'
 decisions.append(d)
notes=R['C']['notes']+['This is a correction list in another unnamed hand; no signature establishes its writer. The corrections are transcribed as proposals, not applied to any other sheet. No linguistic or historical claim was researched, and the n-tuples and therefore signs were ink checks rather than mathematical check events.']
write_record(17,'C','brief_v05.md',texts['C'],decisions,doubt_decisions(R['C'],17,'C'),R['C']['remaining_doubts'],notes,
 'All three full readings agree except for whether plus remains an alternative in the century connector. Root inspected all three changed loci on C’s retained crops. The 30-row inventory includes the live overwrite separately, every correction entry and nested underline, and the archive-number comment. Contextual alternatives and both explicit C doubt macros are decided. Root’s earlier attempted multi-item output was truncated before any crop became visible; only the three subsequently displayed crops count as viewed.',viewed=viewed)
with (W/'SP49_CW_109_workflow.md').open('a') as f:
 f.write('\nAfter scan 017, version 05 remains unchanged. The underline and quotation changes were unanimous; B retained the plus alternative that A/C and the main reader excluded from the closed loop. This was an ink judgement, not a brief ambiguity. The main reader reused three crops. One earlier output was truncated and did not count as a view; those three crops were subsequently displayed singly.\n\n| Scan | A | B | C | Main new | Main reused | Total distinct crops |\n| --- | ---: | ---: | ---: | ---: | ---: | ---: |\n| 017 | 5 | 7 | 5 | 0 | 3 | 17 |\n')
print('Scan 017: three C changes, one remaining doubt, thirty inventory rows, no mathematical events.')
