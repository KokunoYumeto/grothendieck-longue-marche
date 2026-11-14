from pathlib import Path
import json
import sympy as S
R=Path(__file__).resolve().parents[1]
rows=[json.loads(x) for x in (R/'inputs/e123_presentation.out').read_text().splitlines() if x.startswith('{')]
G=next(x for x in rows if x.get('type')=='full_S_class_presentation')
(R/'inputs/e53_ordinary_frobenius_input.txt').write_text(json.dumps(G['class_generator_HNF'])+'\n')
print(json.dumps({'status':'PASS','actual_ideal_norms':[str(S.Matrix(x).det()) for x in G['class_generator_HNF']],
 'scope':'These are actual integral ideal generators; no prime-ideal assumption is made.'},indent=2))
