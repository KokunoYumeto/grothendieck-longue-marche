from workflow import *
# Sole reader's notation comparison after inspecting both pages in the audit.
p=ROOT/'records/scan337.py';r=ast.literal_eval(p.read_text())
t=(ROOT/'pages/136_scan337.tex').read_text()
for x in ('n','{n-1}','{n-2}'):
 t=repl(t,'=\\mathbb C_*^'+x,'=C_*^'+x)
(ROOT/'pages/136_scan337.tex').write_text(t)
r['changes']=[x for x in r['changes'] if x['place']!='three C objects in right diagram column']
r['hand']=[x for x in r['hand'] if not x.startswith('The three C objects on337')]
r['hand'].append('Notation comparison with338: the short inner strokes of the three exterior-power C objects can arise from retracing the curved C, and are not independently decisive for blackboard lettering. The explicitly repeated exterior-power notation on338 settles the ambiguous337 forms as plain C at all three occurrences. The temporary second-reading change to blackboard C was withdrawn; neither witness differs at this place.')
r['notation']=[x for x in r['notation'] if x[0]!='blackboard C']
r['notation'].append(('plain C in exterior-power column','Ambiguous retracing resolved by the repeated exterior-power notation and local alphabet contrast on338; three occurrences.'))
r['note']=r['note'].replace('The three C objects in the diagram have an inner upright stroke and are set as blackboard C; neither witness preserved this alphabet.','The three C objects were provisionally read as doubled during the second reading. Comparison with the explicit exterior-power notation and plain/doubled contrast on338 shows that the ambiguous inner strokes are compatible with retracing; the final notation remains plain C, as in both witnesses.')
p.write_text(pprint.pformat(r,sort_dicts=False,width=120)+'\n')
rebuild();log('notation comparison scans337/338 '+now()+' ambiguous exterior-power C forms retained plain; temporary doubled-C audit change withdrawn')
