"""Retain compact literal witnesses, independent of the root-search machinery."""
from pathlib import Path
from fractions import Fraction
import hashlib,json
r=Path(__file__).resolve().parents[1]
def one(p,tag):
    return next(x for x in (json.loads(l) for l in p.read_text().splitlines() if l.startswith('{')) if x['type']==tag)
lp=r/'inputs/e119_six_character_witness.out'
up=r/'code/e53_upper_unit_candidates.out'
rp=r/'code/e53_upper_witness_export.out'
cp=r/'code/e53_upper_root_characters.out'
l=one(lp,'six_characters');u=one(up,'verified_candidate_S_units');v=one(rp,'relative_root_witnesses');c=one(cp,'verified_root_upper_characters')
d={'field_relations':['xi^6+xi^3+1','beta2^9-53*xi^3'],
   'relative_order':'beta2^i*xi^j, i=0..8 then j=0..5',
   'lower_primitive_element':'xi-beta2^3/xi',
   'lower_units':l['unit_columns'],'upper_candidates':u['elements'],
   'roots':v['roots'],'root_exponents':v['exponents'],
   'lower_norm_coordinates':v['lower_norm_coordinates'],'lower_norm_signs':v['lower_norm_signs'],
   'norm_lattice_HNF':v['norm_lattice_HNF'],
   'provenance_sha256':{str(p.relative_to(r)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [lp,up,rp,cp]},
   'scope':'Literal algebraic witnesses. Their cube, divisor support, relative norm and local character identities are independently reverified by the final programs; no upper unit-basis completeness is assumed.'}
jp=r/'inputs/e122_literal_unit_witnesses.json';jp.write_text(json.dumps(d,indent=2)+'\n')
def gp(x):
    if isinstance(x,list):return '['+','.join(gp(t) for t in x)+']'
    return str(Fraction(x))
data=[d[k] for k in ['lower_units','upper_candidates','roots','root_exponents','lower_norm_coordinates','lower_norm_signs']]
tp=r/'inputs/e122_literal_unit_witnesses.txt';tp.write_text(gp(data)+'\n')
print(json.dumps({'status':'PASS','root_count':len(d['roots']),
                 'outputs':{str(p.relative_to(r)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [jp,tp]},
                 'provenance_sha256':d['provenance_sha256']},indent=2))
