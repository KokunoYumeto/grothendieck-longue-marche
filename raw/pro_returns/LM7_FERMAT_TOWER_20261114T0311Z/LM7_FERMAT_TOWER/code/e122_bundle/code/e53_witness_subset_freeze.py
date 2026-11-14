"""Freeze the stable minimal arithmetic subset for an independent replay."""
from pathlib import Path
import hashlib,json
r=Path(__file__).resolve().parents[1];(r/'ledger').mkdir(exist_ok=True)
files=['code/e53_higher_local.gp','code/e53_upper_witness_verify.gp','code/e53_literal_unit_ring.py',
       'inputs/e119_e53_genus_transition.bin','inputs/e122_literal_unit_witnesses.json',
       'inputs/e122_literal_unit_witnesses.txt',
       'code/e53_higher_local.out','code/e53_upper_witness_verify.out',
       'code/e53_literal_unit_ring.out','code/e53_literal_unit_ring.json']
d={'status':'FROZEN_ARITHMETIC_SUBSET','files':{f:{'sha256':hashlib.sha256((r/f).read_bytes()).hexdigest(),'bytes':(r/f).stat().st_size} for f in files},
   'replay':'In a fresh code/ plus inputs/ tree, run gp -fq e53_higher_local.gp, then gp -fq e53_upper_witness_verify.gp, then python e53_literal_unit_ring.py. Retain each stdout under the matching .out name.',
   'scope':'The mathematical sources and literal inputs listed here are stable. The enclosing proof and full research manifest are still being finalized.'}
t=json.dumps(d,indent=2)+'\n';(r/'ledger/e122_witness_subset_manifest.json').write_text(t);print(t,end='')
