"""Historical pre-blind review; do not rerun after the baseline is frozen."""
from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
d=json.loads((R/'reports/147_scan130_report.json').read_text())
r=d['rows'][5]
r['C']=''; r['final']=''
r['crop']='crops/147_scan130_opening_baseline.jpg'
r['scan_shows']='The first complete main-baseline word is les, followed by flèches verticales sont des morphismes. Its leading l and low es lie at the left boundary of the first-reader box; there is no separate word corresponding to H’s initial illegibility mark. Root inspected the first crop of this previously uncropped disagreement.'
r.pop('source_image',None); r.pop('evidence_scope',None)
d['rows'][9]['math_consequential']=False
d['rows'][30]['C']=next(x for x in (R.parent/'packets/147_scan130/C.tex').read_text().splitlines() if x.startswith(r'G^*_{\Delta_r}'))
d['rows'][31]['H']=''
d['decisions'][1]['decision']='undecided'
d['decisions'][1]['ink']+=' The additional etc. reading is excluded, but the internal punctuation remains uncertain; the whole supplied mark is therefore not counted as fully resolved.'
for i,e in enumerate(d['check_events'],1): e['statement_id']+=f'; N130-{i:02d}'
d['notes'][0]=d['notes'][0].replace('no homotopy-exact-sequence proof was attempted.','the first reader did not attempt a homotopy-exact-sequence proof. Root’s later conditional check is recorded in N130-16.')
d['notes'][13]='S130-14. Every supplied C uncertainty, including the unindexed nested uncertainties, and every C deletion/insertion was checked against this page’s images. The first reader used 24 crops. Root subsequently made and inspected one first crop of the previously uncropped H-only initial illegibility mark, confirming that no separate main-baseline word precedes les. Its already-planned blind box is B02; no duplicate box was added.'
d['notes'].append('MC130-R: for a locally trivial bundle with connected fibre (C*)^d, the homotopy exact sequence identifies the kernel of π₁(E)→π₁(B) with Z^d modulo the image of π₂(B). Thus π₂(B)=0 suffices for the fibre lattice to inject and to equal that kernel. Root checked this consequence using the standard exact sequence as background, and the coordinate retraction of (C*)^d onto (S¹)^d. This does not prove that every written object satisfies the bundle hypotheses or settle Π/π glyph case. See review/mathematical_checks.md, MC130-R.')
d['check_events'].append({'statement_id':'MC130-R; N130-16','type':'targeted proof check','outcome':'Root checked the kernel/image and injectivity consequence under the stated bundle and connectedness hypotheses. The homotopy exact sequence is carried as standard background, not independently reproved. No ink is emended from this check.'})
(R/'review/147_scan130_reviewed.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
with (R/'notation.md').open('a') as f:
    f.write('\n- Scan130: all index dashes and commas were checked separately; d_0-d_r, d_0,-d_r and d_0,-,d_r coexist. The high loop in the upper margin remains circle/zero doubtful. Four homotopy signs are Π-like but retain pi alternatives; two Z letters and N have doubled diagonals. The right211 summand remains B-leading, while the left group letter is G-leading.\n')
with (R/'review/root_visual_readings.md').open('a') as f:
    f.write('\n### Scan130 final return review\nRoot inspected all24 reader crops and the additional first opening_baseline crop [395,65,1675,139]. The latter confirms les flèches verticales sont des morphismes with no extra word preceding les; B02 already covers it. All32 returned rows were reviewed, pseudo-source absence strings replaced by empty spans, and the brace row given the actual C span. The connector-shape row is not counted as a mathematical correction. M1291 remains undecided overall because its internal punctuation is still doubtful. All16 notes have scoped check events, including MC130-R.\n')
