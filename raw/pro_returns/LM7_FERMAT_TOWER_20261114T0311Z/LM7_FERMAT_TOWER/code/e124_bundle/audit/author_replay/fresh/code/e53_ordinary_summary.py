from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parent
rows=[json.loads(x) for x in (R/'e53_ordinary_kernel.out').read_text().splitlines() if x.startswith('{')]
err=(R/'e53_ordinary_kernel.err').read_text()
assert rows[-1]['status']=='PASS' and '***   at ' not in err
D=rows[0]
out={'status':'PASS','scope':'Actual subgroup only; no numerical completeness assumed.',
 'ordinary_character_rank':D['ordinary_character_rank'],
 'horizontal_rank':D['horizontal_rank'],
 'independent_columns':D['independent_columns'],
 'horizontal_character_row':D['horizontal_character_row'],
 'selected_ordinary_exponents':[[row[k-1] for row in D['ordinary_kernel']] for k in D['independent_columns']],
 'selected_ordinary_characters':[[row[k-1] for row in D['ordinary_characters']] for k in D['independent_columns']],
 'root_valuations':D['root_valuations'],
 'source_output_sha256':hashlib.sha256((R/'e53_ordinary_kernel.out').read_bytes()).hexdigest()}
s=json.dumps(out,indent=2)+'\n';(R/'e53_ordinary_summary.json').write_text(s);print(s,end='')
