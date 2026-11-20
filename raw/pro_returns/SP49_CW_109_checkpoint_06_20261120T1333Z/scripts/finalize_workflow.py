"""Complete the workflow account only after all27 scans are adjudicated."""
from pathlib import Path
import json,re
W=Path(__file__).resolve().parents[1]
records=[json.loads(p.read_text()) for p in sorted((W/'records').glob('scan*.json'))]
assert len(records)==27,'The final workflow account requires all27 page decisions.'
p=W/'SP49_CW_109_workflow.md';t=p.read_text()
assert '## Final consolidated crop accounting' not in t,'Already finalized; revise explicitly rather than duplicate.'
last=records[-1]['brief']
first_use=next(r['scan'] for r in records if r['brief']==last)
t=re.sub(r'Currently brief_v\d+\.md, first used scan \d+\.',f'Last used: {last}, first used scan {first_use:03}.',t,count=1)
reflection='''The complete independent readings mattered more than agreement counts. Readers repeatedly differed on cancellation extent, tiny quote groups and raised or lowered fragments. Retaining all three full texts, their frozen unresolved lists and crop logs made those differences reviewable. Reusing their crops usually avoided new image work; main-reader crops were reserved for disagreements without an existing suitable crop. Exact literal comparison prevented preliminary punctuation impressions from becoming false witness differences. The page commit guard kept the sequence intact, and timed durable ZIPs protected both completed pages and work in progress.

Several parts needed correction during the run. H’s explanatory note for scan011 had to be supplied as inherited context, since its running macros alone did not show the documented red stroke. The C-context extractor missed the new table layout at021; a same-page addendum was sent equally to all readers and extraction was fixed for later pages. The initial brief excerpt omitted the source instruction against compiling: one child’s attempt at021 failed before a format was available, and no compilation completed. The prohibition was then made explicit. Image output occasionally truncated; those outputs were not counted as inspected, and existing crops were displayed again in smaller groups. Tall crops at024 and026 were rotated only for viewing, without making second crops. The root’s initial anticipatory note about the026 wasnt opener was corrected after the actual crop display and before adjudication. A script quoting error at025 was corrected before any page record was written; a harmless escape warning at026 was corrected in the retained script. A transient execution transport error at019 recovered with the workspace intact.

The brief also had to make several representational distinctions explicit: each uncertain occurrence needs its own mark; a physical quote pair is represented once even if its attachment is uncertain; a left marginal note must stay on the left; and quote strokes at a cancellation’s edges are checked separately from the words. Long rules must remain related to the text rather than appearing in a detached drawing panel. Geometry can be certain while the mark’s linguistic function remains uncertain. A cancellation passing between an exclamation stem and dot does not prove the sign live when the crossing continues past it. Raised text and carets need explicit placement. An overwritten reference may share an unchanged leading glyph, which must appear once; faint trace extents also need evidence at their endpoints. At027, readable clipped fragments were separated from missing continuation; the visible part of a quote group also governs the first alternative. The cancelled would’nt was corrected only after its actual apostrophe position was compared, superseding an initial conventional root label.

At028, the readers differed over pale circular material features and tiny marks in the blank lower field. Root distinguished material appearance from manuscript ink, retained distinct dark marks with unassigned origin, and rejected continuous curves interpolated through separated flecks. Eighteen new crops were needed because most of those disagreements had no reader crop. An output lost at a context boundary was redisplayed from the same existing file. The brief was revised to make those distinctions explicit.

At029, all disagreements could be decided from existing reader crops. A null crop-field exception in the adjudication script was corrected before any page or record was written. At030, the context extractor mistakenly selected a numbered doubt row and an archive-corner row belonging to other scans because either of their first two cells matched030. The extractor was replaced with explicit table-header Scan-column selection; the corrected context and addendum were supplied equally to all three active readers, and future page contexts were regenerated. No other-page image was opened. The030 reader crop of an opener did not include the complete disputed closer; root made one crop of the uncovered closing edge and preceding ff descenders. One separate slant survived, and single/fused-double uncertainty replaced both certain-pair and absence proposals. Source-coordinate comparison also corrected a provisional root confusion between the first-row faint group and the separate black4. Brief_v15 makes complete edge coverage and coordinate-based identity checking explicit.

Fresh contexts reduce carry-over, but all readers and the main adjudicator used the same model family. They are independent runs, not independent human expertise, and their errors may remain correlated. Every uncertainty retained in the final transcription and apparatus is therefore material. No human review, OCR, external source comparison, completed LaTeX compilation or verification of absent cited text is claimed. The mathematical event log records only checks actually performed, with their hypotheses and limits; ordinary reading and static syntax validation are not mathematical proof events.'''
t=t.replace('To be completed from the actual run.',reflection,1)
table=['## Final consolidated crop accounting','',
       '| Scan | A | B | C | Main new | Main reused | Total distinct crops |',
       '| --- | ---: | ---: | ---: | ---: | ---: | ---: |']
tot={k:0 for k in ['A','B','C','main_new','main_reused']}
for r in records:
 c=r['crop_counts'];n=r['scan']
 for k in tot:tot[k]+=c[k]
 distinct=sum(c[k] for k in ['A','B','C','main_new'])
 table.append('| '+' | '.join([f'{n:03}',*[str(c[k]) for k in tot],str(distinct)])+' |')
table.append('| **Total** | '+' | '.join(str(tot[k]) for k in tot)+' | '+str(sum(tot[k] for k in ['A','B','C','main_new']))+' |')
table+=['','“Main reused” is a count of distinct existing reader crops inspected by the main reader, and is already included in A/B/C totals. It is not added to the distinct-crop total. Whole-page and half-page views, re-displays after truncation, and rotation-only viewing derivatives are not new crops. The retained crop logs give original coordinates and transformations.','']
t+='\n\n'+'\n'.join(table)
t+='\n## First brief as supplied\n\n````markdown\n'+(W/'briefs/brief_v01.md').read_text().rstrip()+'\n````\n'
t+='\n## Last brief as supplied\n\nThe last page used '+last+'.\n\n````markdown\n'+(W/'briefs'/last).read_text().rstrip()+'\n````\n'
p.write_text(t)
print('Workflow finalized:',last,';',sum(tot[k] for k in ['A','B','C','main_new']),'distinct crops.')
