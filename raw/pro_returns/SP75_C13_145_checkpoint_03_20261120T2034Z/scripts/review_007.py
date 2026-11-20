from pathlib import Path
import json
E=Path(__file__).resolve().parents[1]
r=json.loads((E/'reader_reports/145_scan007.json').read_text())
r['main_reader_reviewed']=True
r['crop_count']=12
r['root_review']={'whole_image':True,'crops_viewed':'All twelve distinct first-reading crops directly inspected; multiplier-insertion and double-starred-display crops consulted again for final placement and cancellation decisions.','decisions':'Signature, composition, unpunctuated autom/mod, the isomorphism sign and the terminal colon are supported by their strokes. The interlinear class-normalizing phrase attaches after extérieur; the comma-like stroke is on the added chi(u) line and stays inside the insertion. The two alphabet distinctions and two dense prose cancellations remain unresolved.'}
r['notes'].append('Main-reader adjudication accepts the comma as part of the upper-line addition: it is above the hatted-Z expression and separate from the long curved guide. The cancellation in the final display retains rho u: the rho loop and long descending stem, followed by the short u-like course under the strike, are visible. The doubtful prose cancellations un and est remain doubtful. No mathematical verification is claimed on this page.')
(E/'reader_reports/145_scan007_reviewed.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
(E/'pages/145_scan007.tex').write_text((E/'reader_reports/145_scan007.tex').read_text())
