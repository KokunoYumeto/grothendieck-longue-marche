"""Document root's actual cross-page image checks without altering page text."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
w=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
res={
'NCR-01':{'reading':r'\mathfrak S_{I_{\alpha_0}} in (75); hatted I in the earlier targets','evidence':'Root personally viewed060 B07: the I has a vertical body and horizontal serifs but no detached two-arm roof. In060 B02 the corresponding I indices have detached roofs above those serifs. The058 B04 target likewise has a distinct roof;058 B03 shows the nearby hatted M-factor index. The local absence in(75) is therefore retained.','crops':['147_scan060_second_B07.png','147_scan060_second_B02.png','147_scan058_second_B03.png','147_scan058_second_B04.png']},
'NCR-02':{'reading':r'\widehat M_{0,4}\times\widehat M_{0,4} in the NB, without bangs','evidence':'Root personally viewed060 B03: both M roofs are clear, and the spaces to their upper right have no bang stem or dot. In060 B02, the third row has distinct raised uprights and detached dots beside both roofed M factors. Retain the NB’s local absence and the display’s definite bangs. The earlier metadata scope was already narrowed; this records the actual source confirmation.','crops':['147_scan060_second_B03.png','147_scan060_second_B02.png']},
'NCR-03':{'reading':r'077 (95): hatted I in M; bare I and bare nu in the two T products','evidence':'During root’s077 B02 adjudication the M-factor I had a distinct two-arm roof. Neither the upper Teichmüller I nor the lower nu had a detached roof. Root’s072 B14 adjudication had separately verified roofs on both nu indices there. Preserve these local written differences rather than regularizing the later product.','crops':['147_scan077_second_B02.png','147_scan072_second_B14.png']}}
p=w/'workflow/notation_crosspage_review.json';j=json.loads(p.read_text())
assert j['pending_source_check_count']==3
j['historical_pending_source_checks']=j['pending_source_checks']
j['source_checks']=[]
for old in j['pending_source_checks']:
 q=dict(old);q['status']='root_source_review_complete_local_variation_retained';q['source_resolution']={**res[q['id']],'root_viewed':True,'recorded_utc':now,'page_text_changed':False};j['source_checks'].append(q)
j['pending_source_checks']=[];j['pending_source_check_count']=0
j['status']='complete_after_root_source_review'
j['conclusion']='The cross-page comparison is complete. The three remaining decoration contrasts were personally checked against saved crops by root and confirmed as local written differences. No normalization or page-text change was made. Earlier doubtful readings remain explicit; completion does not assert that every buried stroke is decipherable.'
j['documentation_flags']['reviewed_json_scope_issue']='NCR-02 scope repaired in the earlier documentary pass; root has now confirmed the local NB exponent absences against the crop.'
j['documentation_flags']['source_checks']='NCR-01, NCR-02 and NCR-03 complete; see source_checks and dated root resolutions. Historical hashes and original pending findings are preserved.'
j['root_final_recheck']={'recorded_utc':now,'reviewer':'root','new_proof_or_computation':False,'page_text_changed':False,'source_check_ids':list(res),'page_snapshot_sha256':{str(p.relative_to(w)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((w/'pages').glob('*.tex'))}}
# Keep the original scan079 snapshot explicitly historical after its later blind audit.
j['scan079']['snapshot_note']='This section records the earlier documentary snapshot. Final079 blind decisions and source qualifications are in reviewed/147_scan079.json and second/147_scan079_adjudications.json.'
p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
p=w/'reviewed/147_scan060.json';r=json.loads(p.read_text())
r['notation'][1]['evidence']+=' Final cross-page source check: root viewed060 B03 and B02 and confirmed no bang stem/dot beside either NB factor, versus distinct bangs in row3 of(74).'
r['notation'].append({'sign':r'\mathfrak S_{I_{\alpha_0}}','reading':'Bare I in the first row of(75)','evidence':res['NCR-01']['evidence'],'scope':'Only the(75) target; the earlier(74) and058 targets retain their visible I roofs.'})
r['notes'].append('Final cross-page notation review: the first target in(75) has a bare I, while the related earlier targets have detached I roofs. The two NB M factors have roofs without bangs, while row3 of(74) has both bangs. Root checked these local differences on060 B07/B02/B03 and058 B03/B04 and retained the manuscript forms. This is a visual notation check, not a new proof of the group actions.')
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
review='''# Final cross-page notation review

All24 supplied pages have completed their first reading, independent blind reading and root adjudication. The notation comparison used the complete concordance, the page-specific handwriting records and the saved visual adjudications. Every remaining candidate for an unexplained decoration contrast received root source review before freezing. No text was regularized merely because a neighboring formula used another form.

## Final source checks

| Check | Root’s source finding | Disposition |
| --- | --- | --- |
| NCR-01 | 060(75) has a bare serifed I;060(74) and058(72) have a detached roof over I. | Preserve the local absence. |
| NCR-02 | Both NB factors on060 have M roofs but no raised bang; both factors in row3 of(74) have stems and detached dots. | Preserve the local absence; restrict the bang notation entry to its actual occurrences. |
| NCR-03 | 077(95) has a hatted I in M, bare I in the upper T factor, and bare nu in the lower T factor. Both nu indices in072’s earlier product have roofs. | Preserve each local accent. |

The dated structured evidence and crop paths are in `notation_crosspage_review.json`; the final per-box source evidence is in `root_audit_views.json` and `second/*_adjudications.json`.

## Other recurring families

The preceding review and source adjudications covered double-stroked P/E/Z, looped symmetric-group S, upper/lower Pi, phi-shaped empty-set signs, D graph/oval/1 indices, g/nu/mu and alpha indices, primes/bangs/Roman-numeral alternatives, G underlines, local Codim/codim, de/des and reduced à/colon, thin minus/plus strokes, Teichmuller/Teichmüller, short forms, quotation marks, and diagram hooks/heads. The concordance indexes all occurrences. Clear local differences and authorial slips remain; ambiguous alphabets, prime counts, operators, crossed words and punctuation retain their local uncertainty. None was resolved by restoring an expected mathematical identity.

The count audit separately removes certainty-only choices from the substantive witness-error totals. Those exclusions do not erase the transcription doubts, blind readings, root decisions or the original working records.

No new mathematical proof, external research, OCR, TeX compilation or rendering was performed in this final notation review.
'''
(w/'workflow/notation_review.md').write_text(review+f'\nCompleted and recorded {now}.\n')
p=w/'workflow/notation_review_queue.md';t=p.read_text();p.write_text('**Completed:** all questions below were reconciled in `notation_review.md`, the complete concordance and the final root source checks. The list is retained as the historical review queue.\n\n'+t)
p=w/'README.md';t=p.read_text();old='The requested independent second reading takes place after all first readings. Its box lists and the separately written first and second readings are in `second/`.';new='After all24 first readings were approved, three fresh readers wrote independent blind readings of all372 prescribed boxes, before comparison. Root personally examined every differing box. The frozen box lists, separately written first and second readings, token comparisons and explicit root adjudications are preserved in `second/`.';assert old in t;t=t.replace(old,new).replace('later audit decisions update these records','completed audit decisions are incorporated in these records');t=t.replace('The final freeze records SHA-256 hashes','The cross-page notation review is complete; its source resolutions and preserved historical snapshots are in `workflow/`. The final freeze records SHA-256 hashes');p.write_text(t)
with (w/'progress.log').open('a') as f:f.write(f'cross-page notation source review complete {now}: NCR-01, NCR-02, NCR-03; local ink variations retained; no page-text changes\n')
print(json.dumps({'source_checks_complete':3,'time':now}))
