"""Exact finite calculation for the written base lattice C/Z[i] (148_scan005).
Source 148_scan007 displays its i-fixed pair. No OCR or external input.
Represent (a+bi)/2 modulo Z[i] by (a,b) in {0,1}^2.
Multiplication by i is (-b,a) modulo 2. All four classes are listed.
"""
from pathlib import Path
from datetime import datetime, timezone
import json
root=Path(__file__).resolve().parents[1]
rows=[]
for a,b in [(0,0),(1,0),(0,1),(1,1)]:
    image=((-b)%2,a%2)
    rows.append({"class_numerator":[a,b],"denominator":2,"i_image_numerator":list(image),"fixed":image==(a,b),"zero":(a,b)==(0,0)})
result={"statement_id":"148_scan007-CHECK-i-on-2torsion","source":"148_scan005 base lattice C/Z[i]; 148_scan007 opening and inserted fixed-set formula","computed_at":datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),"rows":rows,"fixed_numerators":[r['class_numerator'] for r in rows if r['fixed']]}
(root/'work/square_two_torsion_check.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
