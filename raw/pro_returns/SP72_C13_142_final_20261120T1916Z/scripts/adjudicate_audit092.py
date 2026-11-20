"""Keep the component functor distinct from the later acting-group notation."""
import json
import subprocess
import sys
from audit_support import load,replace_exact,commit,OUT

r,a,s=load(92)
c=a['changes'][0]
s=replace_exact(s,c['before'],c['after'])
row=next(x for x in r['changes'] if x['id']=='092-02')
row['first_consolidated_reading']=row['final']
row.update({'final':r'\pi_0','c_changed':False,'h_changed':False,
            'confidence':'medium','scan_shows':c['scan_shows'],
            'withdrawn_after_second_reading':True,
            'withdrawal_reason':'The accepted component-functor reading agrees with both witnesses. This corrects the first consolidation and is excluded from substantive error totals.',
            'math_note':'The upper component functor is distinguished from the later locally defined acting group. No mathematical assertion is changed.'})
for element in r['inventory']:
    if element['element']=='annotation on the covering':
        element['first_words_or_objects']=element['first_words_or_objects'].replace('Π₀ des fibres','π₀ des fibres')
first=r['hand_log'][0]
first.update({
    'habit':'A flat-capped pi-shaped sign needs its local notational role as well as its letter strokes to settle case.',
    'scope':'The upper fibres annotation reads π₀; the later explicitly defined acting group and fundamental groups retain Π. The curved right continuation supports the upper reading, but curved terminal strokes also occur in capitals and are not a universal case test.',
    'witness_errors':'Both C and H correctly have lowercase π₀ in the upper fibres annotation. The first consolidation incorrectly made it capital, withdrawn at 092-02 after the full second reading. Their lowercase readings at the separately identified fundamental/acting groups remain corrected where the ink supports Π.'
})
r['hand_log'][3]['scope'] += ' The later isolated point is physically present, but its attachment to cancelled or live text remains explicitly uncertain.'
r['notation'][0]['evidence']='Flat cap and two legs in the later definition, torsor phrase, operation group, subgroup clause, injection, quotient and lower annotation. The upper fibre-components notation is separately π₀. The cancelled Π₁( remains doubtful.'
r['notation'].append({'sign':r'\pi_0','reading':'component functor in the upper fibres annotation',
    'pages':[92],'evidence':c['scan_shows']})
r['notes']=[
    note.replace('Its ink is real; its attachment remains for root.', 'Its ink is real; its attachment remains uncertain after main-reader and second-reader inspection.')
        .replace('all 37 substantive comparison places', 'all 37 first-consolidation comparison places')
    for note in r['notes']
]
r['notes'].append('Second reading: the upper les π₀ des fibres identifies the component-set notation. Its right leg turns into a low continuation; the later definition Π₁(C,x₀)=Π₀ identifies a separate acting group. The root inspected both saved crops and restored lowercase π₀ at this one occurrence. This agrees with C and H, so former row 092-02 is retained only as withdrawn history, excluded from substantive totals. The remaining group capitals are unchanged. All twelve doubtful loci remain explicit, and no new mathematical check was performed.')

p=OUT/'documentation/notation_audit_updates.json'
overlay=json.loads(p.read_text())
overlay.append({'match_sign':r'\pi_0;\quad\{\pi_0\}(E_0)','fields':{
    'pages':'092, 097–098',
    'evidence':'The upper 092 phrase identifies components of fibres, separately from the later defined acting group Π₀=Π₁(C,x₀). Its curved right continuation supports π₀; the root inspected it against the later definition during the second reading. The 097 annotation identifies the component functor in the topos of Pi-sets, and 098 applies it three times in (52). These small outlines can resemble capitals; local definitions and use distinguish the notations rather than size or a single curve alone.'}})
abbr=next(x for x in overlay if x.get('sign')=='ie.; i.e.')
abbr['pages']='080, 086, 090'
abbr['evidence']+=' The full second reading of 090 confirms separate internal and terminal points in its i.e. occurrence.'
p.write_text(json.dumps(overlay,ensure_ascii=False,indent=2)+'\n')
subprocess.run([sys.executable,str(OUT/'scripts/canonical_notation.py')],check=True)
commit(92,r,a,s,
    'Complete independent second reading by reader_c; all 20 inventory elements, 37 first-consolidation comparison places, five assigned marks and six supplementary decisions checked. The main reader reused the upper annotation and later group-definition crops and accepted π₀ only in the component-functor phrase. Existing row 092-02 is withdrawn from substantive totals because both witnesses already have that reading. All twelve doubts remain; no new crop or mathematical check event.',
    [{'id':c['id'],'decision':'accepted; 092-02 withdrawn from substantive totals',
      'reading':r'\pi_0','evidence':c['scan_shows'],'crop':c['crop'],
      'comparison_crop':'crops/scan092_definition_abreg.jpg','confidence':'medium'}])
