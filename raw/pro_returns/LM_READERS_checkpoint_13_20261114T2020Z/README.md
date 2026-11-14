# La Longue Marche readers: checkpoint 13 of the GPT-6 Astra (ChatGPT Pro mode) run

The run's status file in this checkpoint is dated 17:42 UTC on 14 November 2026; the checkpoint was downloaded at
20:20 UTC. The run is still working; this is a progress checkpoint, not a release. **Second finished reader: the French
corrected text with apparatus (`LM_FR_corrige_apparat`, 1,538 pages), which has passed every final gate of the run.**
The French diplomatic edition (`LM_FR_diplomatique`) was declared finished at checkpoint 12. The other five books are
provisional: French reading text, French annotated master, English corrected text with apparatus, English reading
text, English annotated master.

The seven books are byte for byte those of checkpoint 12 (same SHA-256): the corrected text with apparatus was
declared finished without a change to its file. Against checkpoint 12, the checkpoint's logical inventory adds 15 files
and changes 3, all records of the run itself: how checkpoint 12 was saved (two uploads that failed with HTTP 503
errors, a diagnostic, and the save that succeeded at a lower upload concurrency) and the updated checkpoint status,
list of saves and archive log.

The checkpoint is a compact archive (every file stored once under its SHA-256, PNG page images as render recipes,
some book PDFs as deltas against earlier PDFs). What is here was restored from it by our own scripts, not by the run's
recovery helper, and every file was checked against the SHA-256 in the checkpoint's LOGICAL_MANIFEST.tsv:

- `work/records/`: the run's records (checkpoint and release status, gates, change lists, audits);
- `work/build_current/`: the seven current books with their TeX, build logs and link tables;
- `LOGICAL_MANIFEST.tsv`, `MANIFEST.tsv`, `COMPACT_CHECKPOINT.json`, `SOURCE_CHECKPOINT_DISPOSITIONS.tsv`,
  `README_RECOVERY.md`: the checkpoint's own inventory and recovery description;
- `PROMPT.md`: the prompt as sent.

The hash-named objects (2.5 GB) and the PNG recipes stay on our disk. The run is GPT-6 Astra (OpenAI, ChatGPT Pro
mode); the restore and this note are by Claude Opus 5.5 at effort max (Anthropic).
