"""Independent verification of the displayed D45 separator and exact masks."""
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
CODE = HERE / 'code'
central = json.loads((CODE/'d_cm_rank2_degree9.json').read_text())
complete = json.loads((CODE/'d_cm_rank2_centralizers.json').read_text())
corrected = json.loads((CODE/'d_cm_rank2_elliptic_corrected.json').read_text())
words = ['000011011','000010111','001001111','000101111']
positions = [sum(int(v) << j for j,v in enumerate(w)) for w in words]
assert positions == [432,464,484,488]
functional = sum(1 << j for j in positions)
target = int(central['certificates'][0]['target'],16)
columns = [int(v,16) for v in central['certificates'][0]['correction_columns']]
extra = [int(v,16) for v in complete['certificates'][0]['centralizer_degree9_defects']]
assert len(columns) == 112 and len(extra) == 38
assert [(target >> j) & 1 for j in positions] == [0,0,1,0]
assert all((functional & v).bit_count()%2 == 0 for v in columns+extra)
assert (functional & target).bit_count()%2 == 1

def rank(vectors):
    rows = list(vectors)
    pivot = 0
    for position in range(512):
        found = next((j for j in range(pivot,len(rows)) if (rows[j] >> position)&1),None)
        if found is None:
            continue
        rows[pivot],rows[found] = rows[found],rows[pivot]
        for j in range(pivot+1,len(rows)):
            if (rows[j] >> position)&1:
                rows[j] ^= rows[pivot]
        pivot += 1
    return pivot

assert rank(columns) == rank(columns+extra) == 47
assert rank(columns+extra+[target]) == 48
elliptic_columns = [int(v,16) for v in central['certificates'][1]['correction_columns']]
elliptic_extra = [int(v,16) for v in complete['certificates'][1]['centralizer_degree9_defects']]
assert len(elliptic_extra) == 50
assert rank(elliptic_columns) == 38
assert rank(elliptic_columns+elliptic_extra) == 56

record = corrected['literal_correction']
indices = lambda value: [j for j in range(int(value,16).bit_length()) if (int(value,16) >> j)&1]
assert indices(record['central_A_Lyndon_mask']) == [0,1,2,3,4,6,10,11,12,13,14,15,17,22,23,24,25,30,31,34,36,41]
assert indices(record['right_beta_centralizer_mask']) == [2,3,5,7,11,13,14,16,23]
assert int(record['central_beta_Lyndon_mask'],16) == 0
assert record['corrected_source_words']['A']['B_letter_length'] == 3386495
assert record['corrected_source_words']['beta']['B_letter_length'] == 3109533
assert corrected['summary']['same_elliptic_action_retained_modulo_D9']
assert corrected['summary']['results'][0]['relative_cusp_degree9_supports'] == [0]*6
result = {
    'status':'PASS', 'displayed_binary_words':words,
    'literal_little_endian_positions':positions,
    'sphere_target_coefficients':[0,0,1,0],
    'central_columns_killed':112, 'complete_centralizer_columns_killed':38,
    'sphere_correction_rank':47, 'sphere_target_adjoined_rank':48,
    'elliptic_central_rank':38, 'elliptic_complete_rank':56,
    'both_displayed_elliptic_masks_verified':True,
    'literal_elliptic_word_lengths':[3386495,3109533],
    'all_six_elliptic_cusps_zero':True,
    'entire_lower_elliptic_action_retained':True
}
HERE.joinpath('separator_check.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
