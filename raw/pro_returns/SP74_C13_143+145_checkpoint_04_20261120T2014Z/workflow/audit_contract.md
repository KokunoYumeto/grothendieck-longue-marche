# Second-reading contract

You receive exactly one assigned page. Read its whole original image once, then its two existing native halves once each, line by line, checking the accepted consolidated text against the ink and the supplied C/H witnesses. Use the recurring-error sheet and current notation table. Do not use OCR, text recognition, external research, or TeX compilation. Do not normalize the author's wording, notation, slips, cancellation state, insertions, abbreviations, arrows or punctuation.

You must be a different reader from the first reader. Inspect all material, with particular attention to error-sheet categories. The accepted text is a candidate for this second reading, not an authority. Do not assume that agreement of witnesses or earlier decisions establishes a reading.

For a locus unresolved in these views, reuse its existing crop when present; create at most one crop only for a newly unresolved locus. Do not make a second crop of the same locus. Save new crops in the worktree crops directory with a name containing the page key and audit reader. Keep native coordinate boxes and crop paths.

Return reviews/KEY_auditX.tex (the complete proposed final fragment, even if unchanged) and reviews/KEY_auditX.json. Do not alter pages/ or accepted reports.

Audit JSON fields: key, reader, stage='second reading', first_reader, image_views; findings (a list, possibly empty); confirmed (specific checks actually performed, not a generic claim); remaining_doubts (the doubts you think should remain); notes; check_events; hand_log. Each finding: place, before (literal accepted text), after (literal proposed text), reason (visible strokes and placement), confidence, crop, box, against_C, against_H, C (literal witness excerpt), H (literal witness excerpt, or '[no witness]'), kind (one of the authorized categories), consequential, marked_in_H, decision_updates (original MARKS IDs only), certainty_only (boolean). If an existing difference row needs revised evidence or confidence, identify it explicitly. If no change is proposed, say so after a complete reading, with what was checked. For a new manuscript element, include inventory additions. For a doubt removed or narrowed, explicitly identify the existing remaining-doubt entry.

Check-event types must match what actually happened. Reading a mathematical claim while transcribing it is not a proof check; use 'carried as background without fault found' unless you actually perform a specific mathematical check and describe it. No unsupported author identification for pencil pagination.

Finish by reporting the paths and concise findings to the main reader. Wait for a new single-page assignment.
