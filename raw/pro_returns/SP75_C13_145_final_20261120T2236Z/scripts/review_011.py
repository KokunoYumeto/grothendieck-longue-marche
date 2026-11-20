from pathlib import Path
import json

E=Path(__file__).resolve().parents[1]
r=json.loads((E/'reader_reports/145_scan011.json').read_text())
r['main_reader_reviewed']=True
r['crop_count']=13
r['root_review']={
    'whole_image':True,
    'crops_viewed':'All twelve initial crops and the separate previously uncropped header-4 crop directly inspected.',
    'decisions':'Gamma at both group-name occurrences; the long doubled left stem and short downturned right tip distinguish it from Pi. Accepted ou mieux, restant, caractère cyclotomique, inserted une and beta, the separate short underline and comma at beta, gamma attached after une autre, the readable marginal words, car and une relation, and both handwritten numbers. The cancellation strokes, marginal comparison sign and residual word-ending traces remain locally uncertain where reported.'
}
r['notes'].append('The main reader compared the two new group-name signs on their existing crops: both have a long doubled left stem and a short right tip on the top bar, supporting Γ rather than H’s Π. The indexed pi in the definition has curved feet. These local comparisons are paleographic and do not impose a case decision on every earlier group sign. The beta insertion has a distinct dark underline below its body and a comma at its lower right, separate from the lighter diagonal guide.')
(E/'reader_reports/145_scan011_reviewed.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
(E/'pages/145_scan011.tex').write_text((E/'reader_reports/145_scan011.tex').read_text())
