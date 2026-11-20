# Environment recovery on 2026-11-20

An unexpected empty workspace was observed at 12:10:57 UTC after the scan181 main image adjudication and creation of decide_181.py. The surviving decision script and retained conversation contained the completed decisions. The latest durable checkpoint04 was restored; its ZIP passed integrity checking. The original input ZIP was unpacked into the replacement environment to restore source paths. No nested source ZIPs were unpacked.

Checkpoint04: 344,744,305 bytes; SHA-256 03113527d25bd37304e2113c63e716efff1116cadcafa0bc7770dea5161e292b; Library identity libfile_d2d21d306d2c8191b7739a4d6d0d7333. It contains scans170–180 complete and all scan181 A/B/C saved crops, but not their final reports. The same three original readers were asked to restore their completed written artifacts from retained tool-call text, with no images, new crops, new readers or re-adjudication.

Root had read all fields of all three final returns and successfully inspected 17 saved reader crops plus three new main crops before the loss. The saved reader crops were restored byte-for-byte from the checkpoint. The three lost main crop files were recreated from the identical original image rectangles [275,277,1050,381], [1163,1710,1523,1820], and [715,595,1265,711], at the same width2800 with the same helper. This reinstates the already inspected crops; no new image inspection or changed rectangle was used. The existing twenty-entry inspection ledger records those original successful views.

The lost archive-hand metadata corrections for scans172 and180 were reapplied from the retained written audit findings. They do not alter any page text. The checkpoint04 save receipt was also restored from its retained successful upload result. No unscheduled checkpoint was made; the next remains due12:42:25 UTC.

All three original readers completed their artifact restorations, retaining complete=true and the original A13/B14/C17 crop counts. Each supplied a separate recovery note. Root then generated the page from its retained decision script and ran structural, reader-count and crop-reference checks; all passed. No replacement readers were recruited.

The restored checkpoint’s local SHA-256 was explicitly computed and matched the digest above, in addition to ZIP member CRC/integrity verification.
