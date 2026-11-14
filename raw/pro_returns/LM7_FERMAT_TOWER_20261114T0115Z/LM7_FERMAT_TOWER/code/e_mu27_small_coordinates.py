import json
from pathlib import Path
rows=[json.loads(s) for s in Path("research_e94/code/e_mu27_export.out").read_text().splitlines() if s.startswith("{")]
d={r.get("name"):r.get("value") for r in rows if "name" in r}
for n in ["ordinary_norm_to_B3_genus","ordinary_transfer_from_B3_genus","ordinary_to_S_quotient","actual_six_S_prime_classes","six_S_prime_norms_to_B3_genus","relative_S_norm_to_original_C3","relative_S_G","relative_S_H","relative_ordinary_G","relative_ordinary_H"]:
    print(n, d[n])
