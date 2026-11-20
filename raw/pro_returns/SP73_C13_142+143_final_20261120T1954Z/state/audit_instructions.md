# Independent second reading of one assigned page
You must not be the first reader of this page. Read ONLY the assigned page's original scan, already-made halves, consolidated page text, original C/H witnesses, its marks and existing evidence crops. Read the shared error sheet/conventions and current notation table. No OCR, external research, compilation, or repeated crops of decided places.

Personally inspect the original page once for layout, then each half once line by line against the consolidated text. Check every token, formula, diagram and drawing, not just earlier doubts. Start with the error-sheet categories, especially Greek case, small digits/primes, arrows and labels, inserted and deleted material, abbreviation, and omissions shared by the witnesses. Check that every inventory element is complete. Use existing crops to settle open places before making ONE crop for a genuinely new open location. Never enlarge an already decisive half or recrop an already decided place. Treat ink as authority, not expected mathematics or witness agreement.

Read the original and both halves independently before consulting the packet's current mark decisions and remaining-doubt descriptions. Those fields support complete bookkeeping after the visual reading; they are not evidence for a reading. The current transcription is itself a draft to verify.

Write audits/{page}.tex as the full proposed post-audit text and audits/{page}.json with:
page, auditor, first_reader, views (actual paths personally viewed), findings (list; empty if none) each {id,page,place,before,final,c,h,differs_c,differs_h,marked_in_H,ink,confidence,kind,error_category,consequential,unresolved,box,crop,existing_change_id (if revising an earlier change)}. Each finding is a proposed substantive change to the consolidated page. Pure certainty changes, including a new doubt wrapper around an unchanged reading, belong to marks_updates where applicable and remaining_doubts, not substantive findings. A revised earlier substantive row may be supplied to keep its final reading/evidence current without adding a new location. Record exact original-witness readings. Record any author's mathematical slip in notes, not a correction to his text.
marks_updates: list of changed source mark decisions {id,cote,scan,decision,reading,ink,crop,confidence}; leave unaltered decisions alone.
remaining_doubts: complete final proposed list {place,reading,alternatives,confidence,reason}.
inventory_updates: additions or revised elements with standard inventory fields; identify existing element ids if revising.
If adding an inventory element, also give inventory_order as the complete ordered list of element ids, top to bottom, with insertions/deletions beside their parent block. Do not append a newly noticed upper-page element at the bottom of the inventory.
notes: actual findings of the second reading, mathematical tensions, not generic assurance.
check_events: actual mathematical checks only, with statement_id,statement,place,type,outcome. Looking at a formula is not proving it.
notation and hand_log: new/revised observations only, same schema as first reading.
coverage: concise honest statement identifying full-page, halves, inventory and relevant high-risk areas actually inspected; no unsupported coverage claim.
crop_boxes: every newly created crop's relative filename and original pixel box. Reuse the existing crop at a location; do not create a second crop merely because this is a second reading. If an image tool output is truncated, the image was not seen and must be emitted again before claiming inspection.

Do not modify pages/, accepted records, global reports or progress.log. Return paths and findings; main reader reviews and accepts. Your output is documentation and will be included in the final package. Then wait for one next page.
