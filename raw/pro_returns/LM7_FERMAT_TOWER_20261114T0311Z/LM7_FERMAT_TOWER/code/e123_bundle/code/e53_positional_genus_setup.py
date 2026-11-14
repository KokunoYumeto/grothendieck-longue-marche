#!/usr/bin/env python3
"""Retain the actual stopped attempt and copy the certified lower idele input."""
from pathlib import Path
import hashlib,json,shutil
R=Path(__file__).resolve().parents[1]
W=R.parent
src=W/'research_e119/code/e53_positional_genus_transition.bin'
dst=R/'inputs/e119_positional_genus_transition.bin'
if dst.exists():assert dst.read_bytes()==src.read_bytes()
else:shutil.copyfile(src,dst)
status={
 'status':'RETAINED',
 'bounded_upper_certification':{
  'command':'timeout 180 /workspace/scratch/e34c61ec5a35/research_e52/vendor/pari-2.19.0/gp -q e53_positional_pivots.gp',
  'exec_session':89916,'exit_code':124,'timeout_seconds':180,
  'stage_reached':'saved candidate loaded; bnfcertify(B,1) did not return',
  'class_or_unit_conclusion':None,
  'source':'code/e53_positional_pivots.gp',
  'stdout':'code/e53_positional_pivots.out','stderr':'code/e53_positional_pivots.err'},
 'new_input':{'source':str(src.relative_to(W)),'copy':str(dst.relative_to(R)),
              'sha256':hashlib.sha256(dst.read_bytes()).hexdigest()},
 'new_method':'certified L1 ideal relations and E119 exact local Artin/Smith map; no upper BNF reconstruction or certification'
}
(R/'inputs/genus_pivot_manifest.json').write_text(json.dumps(status,indent=2)+'\n')
print(json.dumps(status,indent=2))
