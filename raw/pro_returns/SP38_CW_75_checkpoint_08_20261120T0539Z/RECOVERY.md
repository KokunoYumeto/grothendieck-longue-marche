# Recovery instructions

The checkpoint is a complete snapshot of current deliverables and work documentation. Original scans and witnesses are intentionally excluded. The historical input and final output share the basename SP38_CW_75.zip; distinguish them by origin.

1. Restore the newest checkpoint into `out/` in the new workspace. Read `WORK_STATE.md`, `progress.log`, checkpoint manifests and receipts, and the conversation. The committed records and page files identify completed scans.
2. Obtain the original attached input ZIP and unpack its already-flat package once into `source/`. It should contain `SP38_CW_75_scans/`, `SP38_CW_75_witnesses/`, and `SP38_CW_75_sweep3/`. Do not unpack any of these folders again.
3. Run `python out/scripts/rebuild_packets.py`. This derives the new workspace path and recreates only the page inputs. It does not overwrite notation, briefs, decisions, pages, or raw reader returns. The historical `setup_work.py` is retained as an audit of initial preparation, not as the recovery command.
4. Continue at the first uncommitted page. If its three readers completed full reports before interruption, compare their complete returns and adjudicate the page. If any independent reading was incomplete and its context is lost, preserve all attempts and their original paths in an abandoned-attempt manifest, then start that page with three fresh independent readers. Incomplete reports do not count as completed readings.
5. Use the newest brief and the notation snapshot appropriate to that page. Complete the main crop decisions and all per-page records before starting the next scan.
6. Package only at the specified 45-minute work checkpoints. Checkpoint numbering reads both existing ZIPs and saved manifests/receipts, so recovery without the older local ZIPs cannot reset the counter. Never overwrite any earlier checkpoint, and never nest an earlier ZIP.

Crop metadata retains historical source paths as provenance; newly rebuilt metadata points at the restored source. Relative paths within the output identify retained crops and readings. A later final archive includes all accumulated output documentation, checkpoint manifests and receipts, but not the earlier archive containers or original attachments.
