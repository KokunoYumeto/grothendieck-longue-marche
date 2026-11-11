## La Longue Marche

Grothendieck, *La Longue Marche à travers la théorie de Galois* (Montpellier archive, cotes 140-1 to 140-4, 1,588 scans): AI-transcribed diplomatic LaTeX transcription. First pass by GPT-6 Astra (ChatGPT Pro mode; LM_P057 over the API), second pass by Claude subagents.

**Time of this look:** 10 November 2026, from 17:19 local machine time (UTC+1); final snapshot 2026-11-10 17:31:09, which the table and counts describe. Second-pass agents were writing throughout the look (4 still running at the final snapshot). A file written after 16:51 is marked "in progress". Everything below was read from disk or from the GitHub API at that time; nothing was changed.

### Where the current version lives

| What | Where | Evidence |
|---|---|---|
| Working text (source of record) | `C:\Users\user\Documents\longue_marche_pro_pilot_20261104` | Per package the current text is the first of these that exists: `second_pass\LM_<KEY>_checked_fixed.tex`, `second_pass\LM_<KEY>_checked.tex`, `answers\fixed\LM_<KEY>_transcription.tex`, `answers\unzipped\LM_<KEY>\LM_<KEY>_transcription.tex` (pilot P01–P04: `answers\LM_P0n_transcription.tex`; P057: `second_pass\LM_P057api_checked.tex`). This is the order `lm_publish\rebuild_readers.py` uses (`text_of_raw`). |
| Staging copy for the publisher | `C:\Users\user\Documents\lm_publish\repo` (506 files), reader PDFs in `lm_publish\assets` | Files written 8 Nov 22:48 to 9 Nov 13:53; PDFs 9 Nov 13:49–13:50. Filled by `longue_marche_pro_pilot_20261104\publish_initial_edition.py` (copies only), cleaned by `lm_publish\clean_staged.py`, uploaded by `lm_publish\upload_update_via_api.py`. |
| Published edition | `github.com/KokunoYumeto/grothendieck-longue-marche`, `main` = `a04aad79f16e91341abf2c2bc54844906b893c94` (9 Nov 13:01:58Z = 14:01:58 local), release `update-2026-11-09` (4 PDFs, published 13:02:02Z) | Earlier: `9e175b154294f36776afd5bf7650d8306d6e7288`, tag and release `initial-2026-11-08` (8 Nov 21:54:14Z, 434 files); `41081036` (repository creation). No commit after `a04aad7`. |
| Readers (LaTeX sources) | Published: `reader/LM_reader_draft_140-{1,2,3,4}.tex` + `READER_SOURCES.md` in the repository; same bytes in `lm_publish\repo\reader` | The pilot folder's own `reader\` holds the 8 Nov 18:08 build (the initial edition's readers). The 9 Nov build that was published sits in a session temp folder (`...\scratchpad\reader_build_20261109`), byte-equal to the staging copy. |

Checks made on the published edition:

- All 506 blobs of `main` have the git blob hash of the 506 files in `lm_publish\repo`: none missing, none extra, none different.
- The four release PDFs: GitHub's SHA-256 digests equal the files in `lm_publish\assets`.
- Every published transcription file (`_first_pass.tex`, `_first_pass_fixed.tex`, `_checked.tex`, `_changes.md`, `_notes_checked.md`) is byte-equal to the working file it was copied from; the publisher does not transform transcription files. One blob (`LM_P067_checked.tex`) was downloaded and its SHA-256 compared: equal. Transformed files are only `methodology/METHODOLOGY.md` ("the user" → "the editor", a ledger path and one phrase removed) and `methodology/SECOND_PASS_PROMPT.md` (local path → `<project folder>`); their working sources are older than the staging copy.
- `reader/READER_SOURCES.md` says which text each scan range of the published readers uses; a line-level content test of the published reader sources agrees with it for every package (second-pass text through cote 140-3 scan 130; first pass after that).

Counts at 2026-11-10 17:31:09: 116 packages hold a returned first pass (cote 140-2: 58, 140-3: 41, 140-4: 15, 140-1: 2; all scans covered). A second pass with all three output files (`_checked.tex`, `_changes.md`, `_notes_checked.md`) exists for 92 packages: 60 are published byte-equal, 32 are not published. 4 more are running (0 of them already have a `_checked.tex`); 20 have no second pass.

### Source-of-record table

Paths are relative to `C:\Users\user\Documents\longue_marche_pro_pilot_20261104`. Full SHA-256 values and all other versions are in `longue_marche.jsonl`.

| Package | Cote, scans | Current file | Modified | SHA-256 (first 16) | Second pass | Current text in published edition (main a04aad7) |
|---|---|---|---|---|---|---|
| P01 | 140-2, 1–10 | `answers\LM_P01_transcription.tex` | 11-04 22:40 | `2a914fc6855d0d12` | no | yes, byte-equal |
| P02 | 140-2, 11–20 | `answers\LM_P02_transcription.tex` | 11-04 22:40 | `e073727b0de5a796` | no | yes, byte-equal |
| P03 | 140-2, 21–30 | `second_pass\LM_P03_checked.tex` | 11-05 14:03 | `f8b1ac2430230783` | yes, 11-05 14:03 | yes, byte-equal |
| P04 | 140-2, 31–40 | `answers\LM_P04_transcription.tex` | 11-04 23:43 | `139c8b81a4f5b8c0` | no | yes, byte-equal |
| P05 | 140-2, 41–50 | `answers\fixed\LM_P05_transcription.tex` | 11-08 09:59 | `79225705e3878e91` | no | yes, byte-equal |
| P06 | 140-2, 51–60 | `answers\fixed\LM_P06_transcription.tex` | 11-08 09:53 | `55cfa075affc0df4` | no | yes, byte-equal |
| P07 | 140-2, 61–70 | `answers\fixed\LM_P07_transcription.tex` | 11-08 09:53 | `23f59fce41a26332` | no | yes, byte-equal |
| P08 | 140-2, 71–80 | `answers\fixed\LM_P08_transcription.tex` | 11-08 09:53 | `66ce68b6b436f1b9` | no | yes, byte-equal |
| P09 | 140-2, 81–90 | `answers\fixed\LM_P09_transcription.tex` | 11-08 10:13 | `e813d308aec5d717` | no | yes, byte-equal |
| P10 | 140-2, 91–100 | `answers\fixed\LM_P10_transcription.tex` | 11-08 09:53 | `5771d382d3f9d863` | no | yes, byte-equal |
| P011 | 140-2, 101–110 | `second_pass\LM_P011_checked_fixed.tex` | 11-08 11:22 | `54777d2982b7b9fc` | yes, 11-05 18:15 | yes, byte-equal |
| P012 | 140-2, 111–120 | `second_pass\LM_P012_checked_fixed.tex` | 11-08 11:22 | `887571a7a7c4a93c` | yes, 11-05 19:51 | yes, byte-equal |
| P013 | 140-2, 121–130 | `second_pass\LM_P013_checked_fixed.tex` | 11-08 11:22 | `4a5b79aeeb8139d9` | yes, 11-05 20:19 | yes, byte-equal |
| P014 | 140-2, 131–140 | `second_pass\LM_P014_checked_fixed.tex` | 11-08 11:21 | `b08cd06a46658a05` | yes, 11-05 20:54 | yes, byte-equal |
| P015 | 140-2, 141–150 | `second_pass\LM_P015_checked.tex` | 11-05 23:09 | `bb6cf037332021fa` | yes, 11-05 23:09 | yes, byte-equal |
| P016 | 140-2, 151–160 | `second_pass\LM_P016_checked_fixed.tex` | 11-08 11:22 | `b736908ab281b24b` | yes, 11-06 00:55 | yes, byte-equal |
| P017 | 140-2, 161–170 | `second_pass\LM_P017_checked_fixed.tex` | 11-08 11:22 | `1add9abe08444298` | yes, 11-06 01:23 | yes, byte-equal |
| P018 | 140-2, 171–180 | `second_pass\LM_P018_checked_fixed.tex` | 11-08 11:22 | `3cce4ac3a1080305` | yes, 11-06 01:54 | yes, byte-equal |
| P019 | 140-2, 181–190 | `second_pass\LM_P019_checked_fixed.tex` | 11-08 11:22 | `b5ffc5627bcc8ee3` | yes, 11-06 02:34 | yes, byte-equal |
| P020 | 140-2, 191–200 | `second_pass\LM_P020_checked.tex` | 11-06 03:13 | `5e763e8e4e348e13` | yes, 11-06 03:13 | yes, byte-equal |
| P021 | 140-2, 201–210 | `second_pass\LM_P021_checked.tex` | 11-06 03:46 | `7a962612e2243d28` | yes, 11-06 03:46 | yes, byte-equal |
| P022 | 140-2, 211–220 | `second_pass\LM_P022_checked_fixed.tex` | 11-08 11:22 | `b401beaafaaedba4` | yes, 11-06 11:37 | yes, byte-equal |
| P023 | 140-2, 221–230 | `second_pass\LM_P023_checked_fixed.tex` | 11-08 11:22 | `913121e963eda8aa` | yes, 11-06 11:43 | yes, byte-equal |
| P024 | 140-2, 231–240 | `second_pass\LM_P024_checked_fixed.tex` | 11-08 11:22 | `06111656ad535037` | yes, 11-06 11:43 | yes, byte-equal |
| P025 | 140-2, 241–250 | `second_pass\LM_P025_checked_fixed.tex` | 11-08 11:22 | `0891836107bae6ea` | yes, 11-06 12:12 | yes, byte-equal |
| P026 | 140-2, 251–260 | `second_pass\LM_P026_checked_fixed.tex` | 11-08 11:22 | `ab466cf074eb309a` | yes, 11-06 12:28 | yes, byte-equal |
| P027 | 140-2, 261–270 | `second_pass\LM_P027_checked_fixed.tex` | 11-08 11:22 | `6ea610f61c899f9a` | yes, 11-06 12:12 | yes, byte-equal |
| P028 | 140-2, 271–280 | `second_pass\LM_P028_checked_fixed.tex` | 11-08 11:21 | `fbf3a40e8366afe4` | yes, 11-06 12:08 | yes, byte-equal |
| P029 | 140-2, 281–290 | `second_pass\LM_P029_checked_fixed.tex` | 11-08 11:21 | `97bcf707b9b42f53` | yes, 11-06 12:12 | yes, byte-equal |
| P030 | 140-2, 291–300 | `second_pass\LM_P030_checked_fixed.tex` | 11-08 11:22 | `91b100e4ba4965b9` | yes, 11-06 12:09 | yes, byte-equal |
| P031 | 140-2, 301–310 | `second_pass\LM_P031_checked_fixed.tex` | 11-08 11:22 | `5cb9d0d1a1b672c7` | yes, 11-06 12:08 | yes, byte-equal |
| P032 | 140-2, 311–320 | `second_pass\LM_P032_checked_fixed.tex` | 11-08 11:22 | `9217c0c9db413aac` | yes, 11-06 12:15 | yes, byte-equal |
| P033 | 140-2, 321–330 | `second_pass\LM_P033_checked_fixed.tex` | 11-08 11:22 | `fbbec41cf66b86f4` | yes, 11-06 12:15 | yes, byte-equal |
| P034 | 140-2, 331–340 | `second_pass\LM_P034_checked_fixed.tex` | 11-08 11:22 | `f320d31435419886` | yes, 11-06 12:16 | yes, byte-equal |
| P035 | 140-2, 341–350 | `second_pass\LM_P035_checked_fixed.tex` | 11-08 11:22 | `6ece507a9f15935b` | yes, 11-06 12:20 | yes, byte-equal |
| P036 | 140-2, 351–360 | `second_pass\LM_P036_checked_fixed.tex` | 11-08 11:21 | `cbdf5c86cda950aa` | yes, 11-06 12:45 | yes, byte-equal |
| P037 | 140-2, 361–370 | `second_pass\LM_P037_checked_fixed.tex` | 11-08 11:21 | `cba20abb3d6c5de6` | yes, 11-06 12:43 | yes, byte-equal |
| P038 | 140-2, 371–380 | `second_pass\LM_P038_checked_fixed.tex` | 11-08 11:22 | `47a92b9d15013c3b` | yes, 11-06 12:42 | yes, byte-equal |
| P039 | 140-2, 381–390 | `second_pass\LM_P039_checked_fixed.tex` | 11-08 11:21 | `61d6370b16054b9e` | yes, 11-06 12:47 | yes, byte-equal |
| P040 | 140-2, 391–400 | `second_pass\LM_P040_checked_fixed.tex` | 11-08 11:22 | `c503eed928dc3af2` | yes, 11-06 12:50 | yes, byte-equal |
| P041 | 140-2, 401–410 | `second_pass\LM_P041_checked.tex` | 11-08 11:58 | `230365486d07250a` | yes, 11-08 11:58 | yes, byte-equal |
| P042 | 140-2, 411–420 | `second_pass\LM_P042_checked.tex` | 11-08 12:24 | `60182b37466c9227` | yes, 11-08 12:24 | yes, byte-equal |
| P043 | 140-2, 421–430 | `second_pass\LM_P043_checked.tex` | 11-08 12:10 | `3414c03ba5387425` | yes, 11-08 12:10 | yes, byte-equal |
| P044 | 140-2, 431–440 | `second_pass\LM_P044_checked.tex` | 11-08 11:23 | `e36535a63d5652cc` | yes, 11-08 11:23 | yes, byte-equal |
| P045 | 140-2, 441–450 | `second_pass\LM_P045_checked.tex` | 11-08 23:01 | `fe16ce9b8f01b3ea` | yes, 11-08 23:01 | yes, byte-equal |
| P046 | 140-2, 451–460 | `second_pass\LM_P046_checked.tex` | 11-08 23:06 | `92d43fb43bc17340` | yes, 11-08 23:06 | yes, byte-equal |
| P047 | 140-2, 461–470 | `second_pass\LM_P047_checked.tex` | 11-08 22:58 | `71d03bf51f506356` | yes, 11-08 22:58 | yes, byte-equal |
| P048 | 140-2, 471–480 | `second_pass\LM_P048_checked.tex` | 11-09 03:21 | `2b3cec4a115e52dc` | yes, 11-09 03:21 | yes, byte-equal |
| P049 | 140-2, 481–490 | `second_pass\LM_P049_checked.tex` | 11-09 03:18 | `f5aa38e25df30d11` | yes, 11-09 03:18 | yes, byte-equal |
| P050 | 140-2, 491–500 | `second_pass\LM_P050_checked.tex` | 11-09 03:16 | `b865846e70dead12` | yes, 11-09 03:16 | yes, byte-equal |
| P051 | 140-2, 501–510 | `second_pass\LM_P051_checked.tex` | 11-09 03:49 | `2d973ee417cff674` | yes, 11-09 03:49 | yes, byte-equal |
| P052 | 140-2, 511–520 | `second_pass\LM_P052_checked.tex` | 11-09 03:49 | `9ada2eab21962fd7` | yes, 11-09 03:49 | yes, byte-equal |
| P053 | 140-2, 521–530 | `second_pass\LM_P053_checked.tex` | 11-09 04:28 | `840b6199c2a090e1` | yes, 11-09 04:28 | yes, byte-equal |
| P054 | 140-2, 531–540 | `second_pass\LM_P054_checked.tex` | 11-09 04:27 | `a28442f3a8ede434` | yes, 11-09 04:27 | yes, byte-equal |
| P055 | 140-2, 541–550 | `second_pass\LM_P055_checked.tex` | 11-09 05:03 | `e20bc628676eec14` | yes, 11-09 05:03 | yes, byte-equal |
| P056 | 140-2, 551–560 | `second_pass\LM_P056_checked.tex` | 11-09 05:31 | `0118d1d4a0db98d7` | yes, 11-09 05:31 | yes, byte-equal |
| P057 | 140-2, 561–570 | `second_pass\LM_P057api_checked.tex` | 11-06 15:11 | `999961d3622e6eca` | yes, 11-06 15:11 | yes, byte-equal |
| P058 | 140-2, 571–575 | `second_pass\LM_P058_checked.tex` | 11-09 07:56 | `0b18f89bba0edbed` | yes, 11-09 07:56 | yes, byte-equal |
| P059 | 140-3, 1–10 | `second_pass\LM_P059_checked.tex` | 11-09 08:32 | `809b04b6e23ee4a7` | yes, 11-09 08:32 | yes, byte-equal |
| P060 | 140-3, 11–20 | `second_pass\LM_P060_checked.tex` | 11-09 09:02 | `50bca80ff411acb0` | yes, 11-09 09:02 | yes, byte-equal |
| P061 | 140-3, 21–30 | `second_pass\LM_P061_checked.tex` | 11-09 09:33 | `adbeb2fbab4766ee` | yes, 11-09 09:33 | yes, byte-equal |
| P062 | 140-3, 31–40 | `second_pass\LM_P062_checked.tex` | 11-09 10:01 | `a1289397cf72e6d6` | yes, 11-09 10:01 | yes, byte-equal |
| P063 | 140-3, 41–50 | `second_pass\LM_P063_checked.tex` | 11-09 10:33 | `ad08aac3e6c76de7` | yes, 11-09 10:33 | yes, byte-equal |
| P064 | 140-3, 51–60 | `second_pass\LM_P064_checked.tex` | 11-09 11:08 | `c564866f0cb46c0f` | yes, 11-09 11:08 | yes, byte-equal |
| P065 | 140-3, 61–70 | `second_pass\LM_P065_checked.tex` | 11-09 11:36 | `9ec248b3c14847ff` | yes, 11-09 11:36 | yes, byte-equal |
| P066 | 140-3, 71–80 | `second_pass\LM_P066_checked.tex` | 11-09 12:01 | `9f95dcd6bb3e359f` | yes, 11-09 12:01 | yes, byte-equal |
| P067 | 140-3, 81–90 | `second_pass\LM_P067_checked.tex` | 11-09 12:37 | `9710f220a39335d1` | yes, 11-09 12:37 | yes, byte-equal |
| C3-131-149 | 140-3, 131–149 | `second_pass\LM_C3-131-149_checked.tex` | 11-09 13:58 | `ebb7885323547ff3` | yes, 11-09 13:58 | no; published has the fixed first pass |
| C3-150-168 | 140-3, 150–168 | `second_pass\LM_C3-150-168_checked.tex` | 11-09 14:26 | `cdfb4ba4e20d3f9f` | yes, 11-09 14:26 | no; published has the fixed first pass |
| C3-169-187 | 140-3, 169–187 | `second_pass\LM_C3-169-187_checked.tex` | 11-09 15:28 | `e17b88b4efd1cd81` | yes, 11-09 15:28 | no; published has the fixed first pass |
| C3-188-206 | 140-3, 188–206 | `second_pass\LM_C3-188-206_checked.tex` | 11-09 17:49 | `bd25db3a578c3d6f` | yes, 11-09 17:49 | no; published has the fixed first pass |
| C3-207-225 | 140-3, 207–225 | `second_pass\LM_C3-207-225_checked.tex` | 11-10 16:06 | `b3b8b114a0322125` | yes, 11-10 16:06 | no; published has the fixed first pass |
| C3-226-244 | 140-3, 226–244 | `second_pass\LM_C3-226-244_checked.tex` | 11-10 16:10 | `135501e81e795f21` | yes, 11-10 16:10 | no; published has the fixed first pass |
| C3-245-263 | 140-3, 245–263 | `second_pass\LM_C3-245-263_checked.tex` | 11-10 16:10 | `6bcf1d7f1c49a8d7` | yes, 11-10 16:10 | no; published has the fixed first pass |
| C3-264-282 | 140-3, 264–282 | `second_pass\LM_C3-264-282_checked.tex` | 11-10 16:03 | `8ba4d5e3fc0502ec` | yes, 11-10 16:03 | no; published has the fixed first pass |
| C3-283-301 | 140-3, 283–301 | `second_pass\LM_C3-283-301_checked.tex` | 11-10 16:08 | `9bc85b8b11d4080d` | yes, 11-10 16:08 | no; published has the fixed first pass |
| C3-302-320 | 140-3, 302–320 | `second_pass\LM_C3-302-320_checked.tex` | 11-10 16:08 | `0a366a4603cd5c7c` | yes, 11-10 16:08 | no; published has the fixed first pass |
| C3-321-339 | 140-3, 321–339 | `second_pass\LM_C3-321-339_checked.tex` | 11-10 16:09 | `58fbbf4d87cfbcf9` | yes, 11-10 16:09 | no; published has the fixed first pass |
| C3-340-358 | 140-3, 340–358 | `second_pass\LM_C3-340-358_checked.tex` | 11-10 16:07 | `e010e754877ed7f2` | yes, 11-10 16:07 | no; published has the original first pass |
| C3-359-377 | 140-3, 359–377 | `second_pass\LM_C3-359-377_checked.tex` | 11-10 16:06 | `19bff0f4d49f7063` | yes, 11-10 16:06 | no; published has the original first pass |
| C3-378-396 | 140-3, 378–396 | `second_pass\LM_C3-378-396_checked.tex` | 11-10 16:11 | `d8775202f19fe093` | yes, 11-10 16:11 | no; published has the original first pass |
| C3-397-415 | 140-3, 397–415 | `second_pass\LM_C3-397-415_checked.tex` | 11-10 16:05 | `4c2949715ff28209` | yes, 11-10 16:05 | no; published has the original first pass |
| C3-416-434 | 140-3, 416–434 | `second_pass\LM_C3-416-434_checked.tex` | 11-10 16:07 | `ad6b097d6f9b5231` | yes, 11-10 16:07 | no; published has the original first pass |
| C3-435-453 | 140-3, 435–453 | `second_pass\LM_C3-435-453_checked.tex` | 11-10 16:07 | `b8023ed01414da3f` | yes, 11-10 16:07 | no; published has the original first pass |
| C3-454-472 | 140-3, 454–472 | `second_pass\LM_C3-454-472_checked.tex` | 11-10 16:06 | `31558f8c63b5c516` | yes, 11-10 16:06 | no; published has the original first pass |
| C3-473-491 | 140-3, 473–491 | `second_pass\LM_C3-473-491_checked.tex` | 11-10 16:22 | `154e222a97261e8b` | yes, 11-10 16:22 | no; published has the original first pass |
| C3-492-510 | 140-3, 492–510 | `second_pass\LM_C3-492-510_checked.tex` | 11-10 16:37 | `aefcf2d4492a992e` | yes, 11-10 16:37 | no; published has the original first pass |
| C3-511-529 | 140-3, 511–529 | `second_pass\LM_C3-511-529_checked.tex` | 11-10 16:44 | `6b6b24332a0f5edf` | yes, 11-10 16:44 | no; published has the original first pass |
| C3-530-548 | 140-3, 530–548 | `second_pass\LM_C3-530-548_checked.tex` | 11-10 16:44 | `7fd67370b25c7333` | yes, 11-10 16:44 | no; published has the original first pass |
| C3-549-567 | 140-3, 549–567 | `second_pass\LM_C3-549-567_checked.tex` | 11-10 16:39 | `8ebda59fd3df797e` | yes, 11-10 16:39 | no; published has the original first pass |
| C3-568-586 | 140-3, 568–586 | `second_pass\LM_C3-568-586_checked.tex` | 11-10 16:43 | `15e30b8d517abd9c` | yes, 11-10 16:43 | no; published has the original first pass |
| C3-587-605 | 140-3, 587–605 | `second_pass\LM_C3-587-605_checked.tex` | 11-10 16:43 | `1a88407916daf392` | yes, 11-10 16:43 | no; published has the original first pass |
| C3-606-624 | 140-3, 606–624 | `second_pass\LM_C3-606-624_checked.tex` | 11-10 16:42 | `a7da7deef733f06c` | yes, 11-10 16:42 | no; published has the original first pass |
| C3-625-643 | 140-3, 625–643 | `second_pass\LM_C3-625-643_checked.tex` | 11-10 17:08 | `d9364543c1fa2015` | yes, 11-10 17:08; in progress | no; published has the original first pass |
| C3-644-662 | 140-3, 644–662 | `second_pass\LM_C3-644-662_checked.tex` | 11-10 17:27 | `dfedb54992b39024` | yes, 11-10 17:27; in progress | no; published has the fixed first pass |
| C3-663-681 | 140-3, 663–681 | `second_pass\LM_C3-663-681_checked.tex` | 11-10 17:17 | `d2b7b8e27f41b573` | yes, 11-10 17:17; in progress | no; published has the original first pass |
| C3-682-696 | 140-3, 682–696 | `second_pass\LM_C3-682-696_checked.tex` | 11-10 17:10 | `291b6493984b968d` | yes, 11-10 17:10; in progress | no; published has the original first pass |
| C4-001-019 | 140-4, 1–19 | `answers\unzipped\LM_C4-001-019\LM_C4-001-019_transcription.tex` | 11-08 17:02 | `f25206f3f1b07f94` | running, work folder 17:30 | yes, byte-equal |
| C4-020-038 | 140-4, 20–38 | `second_pass\LM_C4-020-038_checked.tex` | 11-10 17:12 | `b8ed457188b85def` | yes, 11-10 17:12; in progress | no; published has the original first pass |
| C4-039-057 | 140-4, 39–57 | `second_pass\LM_C4-039-057_checked.tex` | 11-10 17:19 | `fe9b25c17652a6bf` | yes, 11-10 17:19; in progress | no; published has the fixed first pass |
| C4-058-076 | 140-4, 58–76 | `answers\fixed\LM_C4-058-076_transcription.tex` | 11-08 17:31 | `7fd36cccedde7706` | running, work folder 17:30 | yes, byte-equal |
| C4-077-095 | 140-4, 77–95 | `answers\unzipped\LM_C4-077-095\LM_C4-077-095_transcription.tex` | 11-08 17:02 | `ed3034d0f7614aae` | running, work folder 17:30 | yes, byte-equal |
| C4-096-114 | 140-4, 96–114 | `answers\unzipped\LM_C4-096-114\LM_C4-096-114_transcription.tex` | 11-08 17:02 | `e87ee33a8d79dad9` | running, work folder 17:30 | yes, byte-equal |
| C4-115-133 | 140-4, 115–133 | `answers\unzipped\LM_C4-115-133\LM_C4-115-133_transcription.tex` | 11-08 17:02 | `88d7560a86ae3a67` | no | yes, byte-equal |
| C4-134-152 | 140-4, 134–152 | `answers\unzipped\LM_C4-134-152\LM_C4-134-152_transcription.tex` | 11-08 17:02 | `38b5228d760af4db` | no | yes, byte-equal |
| C4-153-171 | 140-4, 153–171 | `answers\fixed\LM_C4-153-171_transcription.tex` | 11-08 17:09 | `f129b47342af6492` | no | yes, byte-equal |
| C4-172-190 | 140-4, 172–190 | `answers\unzipped\LM_C4-172-190\LM_C4-172-190_transcription.tex` | 11-08 17:02 | `0d5f364fa1129bed` | no | yes, byte-equal |
| C4-191-209 | 140-4, 191–209 | `answers\fixed\LM_C4-191-209_transcription.tex` | 11-08 17:09 | `ce89776b5b7c418b` | no | yes, byte-equal |
| C4-210-228 | 140-4, 210–228 | `answers\unzipped\LM_C4-210-228\LM_C4-210-228_transcription.tex` | 11-08 17:02 | `ac81213a61f69849` | no | yes, byte-equal |
| C4-229-247 | 140-4, 229–247 | `answers\unzipped\LM_C4-229-247\LM_C4-229-247_transcription.tex` | 11-08 17:02 | `75aea5342d9d683a` | no | yes, byte-equal |
| C4-248-266 | 140-4, 248–266 | `answers\fixed\LM_C4-248-266_transcription.tex` | 11-08 17:09 | `7f04dcca43ed62dc` | no | yes, byte-equal |
| C4-267-280 | 140-4, 267–280 | `answers\unzipped\LM_C4-267-280\LM_C4-267-280_transcription.tex` | 11-08 17:02 | `c9498c82e518488c` | no | yes, byte-equal |
| C1-001-019 | 140-1, 1–19 | `answers\unzipped\LM_C1-001-019\LM_C1-001-019_transcription.tex` | 11-08 17:58 | `ddabbe24fd57c849` | no | yes, byte-equal |
| C1-020-037 | 140-1, 20–37 | `answers\unzipped\LM_C1-020-037\LM_C1-020-037_transcription.tex` | 11-08 17:58 | `7ae3b2acb2ccd01f` | no | yes, byte-equal |
| P068-069 | 140-3, 91–110 | `second_pass\LM_P068-069_checked.tex` | 11-09 13:09 | `e9a9c17f790c8c02` | yes, 11-09 13:09 | yes, byte-equal |
| P070-071 | 140-3, 111–130 | `second_pass\LM_P070-071_checked.tex` | 11-09 13:36 | `f2751f80d807cbe4` | yes, 11-09 13:36 | yes, byte-equal |

### Other versions

- **First-pass returns as received:** `answers\LM_<KEY>.zip` (112 zips for 111 packages; `LM_P060.zip` and `LM_P060(1).zip` are two different returns of one package; `LM_C3-682-696(1).zip` is the only return of its package). Unpacked copies in `answers\unzipped\<KEY>\`; for every package except LM_P060 the unpacked transcription equals the transcription inside the newest zip.
- **Fixed first pass:** `answers\fixed\<KEY>_transcription.tex` (77 packages, 7–8 Nov; diagrams and illegible marks from the LM_FIX_01–16 returns, and script repairs for C3-644-662 and five C4 packages: `fix_c3_644_662_math.py`, `fix_c4_compile*.py`). `answers\fixed\backup_20261108\` holds the pre-repair copies of LM_C4-039-057 and LM_C4-058-076 (8 Nov 17:20); the current ones are 11 minutes newer and differ.
- **Second pass before the fixes were merged:** `second_pass\LM_P0nn_checked.tex` for the 27 packages of P011–P040 that also have `_checked_fixed.tex` (8 Nov 11:21–11:22). The `_checked_fixed.tex` is current and is what was published as `_checked.tex`.
- **Staging and published copies:** see above; byte-equal to their sources, stopping at the state of 9 Nov 13:44.
- **Readers:** `reader\` in the pilot folder (8 Nov), `lm_publish\repo\reader` (9 Nov, published).
- **Collected research notes:** `second_pass\ALL_RESEARCH_NOTES.md`, `ALL_NOTES_MAP.md`, `NOTES_A/B/C_*.md`, `GLOBAL_PASS.md` (8 Nov 22:38–22:42). Built when the newest checked notes were those of LM_P044; for the 55 packages whose checked notes are newer, they hold the unchecked first-pass notes. Regenerable with `second_pass\collect_research_notes.py`.
- **Never run:** package folders LM_P068–LM_P071 (replaced by LM_P068-069 and LM_P070-071) and `superseded_10scan_P072-P160\` (replaced by the C3/C4/C1 packages); they hold prompts and images, no returns.
- **Not the project's transcription:** `second_pass\witness\*.txt` (CSG draft, IUT, Carmona–Künzer, Grothendieck Circle table; text extracted 5 Nov from the PDFs in `interlanguage\Post_Stacks_Open_Source_Library\Reference_Only\Grothendieck_Late_Works\La_Longue_Marche\transcription_witnesses`); the scan PDFs in `...\La_Longue_Marche\official_manuscript_witness` (14 Aug 2026); `C:\Users\user\Documents\longue_marche_ocr_test_20261104` (an OCR trial of 4 pages, 4 Nov); `C:\Users\user\Documents\Papors\OS\LA LONGUE MARCHE À TRAVERS LA.pdf` (same size as the Carmona–Künzer witness PDF, 1,240,622 bytes; content not compared).
- No other copy of the transcription was found in the top two levels of `C:\Users\user\Documents` or `F:\user\Documents` (names containing "longue", "marche", "lm_", "140-2"). `mlm_history_*` is unrelated.

### Work of 9–10 November: did it reach the current version?

Yes for every finished second pass; the published edition has only the part finished before 9 Nov 13:44.

- **9 Nov, 25 second passes** (LM_P048–P056, P058–P067, P068-069, P070-071, C3-131-149 to C3-188-206). Each was made from the latest first-pass file (the fixed one where it exists) and its `_checked.tex` is the current file. 21 of them (through LM_P070-071, 13:36) are in the published edition, byte-equal. The four C3 packages finished at 13:58, 14:26, 15:28 and 17:49, after the staging copy was made (13:44), and are not published.
- **10 Nov, 28 second passes** (C3-207-225, C3-226-244, C3-245-263, C3-264-282, C3-283-301, C3-302-320, C3-321-339, C3-340-358, C3-359-377, C3-378-396, C3-397-415, C3-416-434, C3-435-453, C3-454-472, C3-473-491, C3-492-510, C3-511-529, C3-530-548, C3-549-567, C3-568-586, C3-587-605, C3-606-624, C3-625-643, C3-644-662, C3-663-681, C3-682-696, C4-020-038, C4-039-057). Each was made from the latest first-pass file and its `_checked.tex` is the current file. None is staged or published.
- **Evidence for the input file:** each prompt `second_pass\PROMPT_LM_<KEY>.md` (generated 8 Nov 22:37 by `make_prompts_v3.py`) names `answers\fixed\...` where a fixed first pass exists and `answers\unzipped\...` otherwise; no fixed file is newer than its prompt. For 30 of the 32 unpublished packages the agent's helper script survives in the session scratchpad and reads exactly that file (none found for C3-131-149, C3-606-624). Where both an original and a fixed first pass exist, the checked text is closer to the named one (word-sequence similarity, in the jsonl). No agent transcript was read.
- **Running at 2026-11-10 17:31:09:** C4-001-019, C4-058-076, C4-077-095, C4-096-114 (work folder written in the last 40 minutes, output files not all there yet). Their prompts name the latest first-pass file.
- **Not started:** C4-115-133, C4-134-152, C4-153-171, C4-172-190, C4-191-209, C4-210-228, C4-229-247, C4-248-266, C4-267-280, C1-001-019, C1-020-037. The pilot packages LM_P01, P02, P04–P10 (cote 140-2 scans 1–20 and 31–100) have no second-pass prompt.

### Cases where work went into a non-current version

For the second passes of 9–10 November: **none found.** Checked: prompt input against the newest first-pass file for all 53; helper-script inputs where they survive; similarity of each checked text to both first-pass candidates; scan markers complete in every text; published and staged bytes against the working files; unpacked first passes against the newest zip.

Cases found elsewhere in this workstream:

1. **The published edition and the staging copy are behind `second_pass`** by 32 packages (those with a `_checked.tex`, finished or being written): C3-131-149, C3-150-168, C3-169-187, C3-188-206, C3-207-225, C3-226-244, C3-245-263, C3-264-282, C3-283-301, C3-302-320, C3-321-339, C3-340-358, C3-359-377, C3-378-396, C3-397-415, C3-416-434, C3-435-453, C3-454-472, C3-473-491, C3-492-510, C3-511-529, C3-530-548, C3-549-567, C3-568-586, C3-587-605, C3-606-624, C3-625-643, C3-644-662, C3-663-681, C3-682-696, C4-020-038, C4-039-057. For these scans the public readers and repository carry the first pass. No publish step has run since 9 Nov 14:02, so this is pending work, not misdirected work. `publish_initial_edition.py` restages from the working folder, so the next update picks them up.
2. **LM_P060 (cote 140-3, scans 11–20): the published first pass is the older of two returns.** `answers\LM_P060.zip` (6 Nov 15:53, transcription 18,620 bytes, SHA-256 `8b827098fbb42715…`) and `answers\LM_P060(1).zip` (16:23, 19,179 bytes, `844c589c7b63c860…`) differ. `apply_fixes.py` took the newest zip, so the fixed first pass and the checked text descend from the later return (similarity to it 0.77 and 0.73, to the earlier 0.57). `answers\unzipped\LM_P060\` holds the earlier return, and the staging step copied it: the published `transcription/140-3/LM_P060_first_pass.tex` and `notes/140-3/LM_P060_notes.md` are the earlier return, and the second pass checked the earlier return's notes. The published reader uses the checked text, so the reading text is not affected.
3. **P011–P040: fixes of 7–8 Nov that are in the fixed first pass but not in the current second-pass text.** These second passes (5–6 Nov) were made from the original first pass, before the fix packages. `merge_fixes_into_checked.py` carried what it could into `_checked_fixed.tex`; `second_pass\merge_fixes_open.md` (8 Nov 11:22) lists 33 fixes "still to merge by hand" in 20 packages, and nothing dated later resolves it. My own text test finds 24 fix replacements in 17 packages present verbatim in `answers\fixed` and absent from the current second-pass text (per package in the jsonl). LM_P021 has no `_checked_fixed.tex` at all: its one fix (LM_FIX_09-016, scan 205) is only in `answers\fixed\LM_P021_transcription.tex`. The published `_checked.tex` and readers carry the same gap. Whether a given fix is superseded by the second-pass reading of that place: NOT VERIFIED.
4. **Records that disagree with the files:**
   - `braindump_board\cards\longue-marche.md` (written 10 Nov 17:17) says "Cote 140-3 (C3) second pass COMPLETE on 10 Nov". At 17:23 LM_C3-644-662 had no `_checked.tex` (its agent was still writing crops); the file appeared at 17:27. At 2026-11-10 17:31:09 (card last written 17:17): C3-644-662 had its three output files on disk (checked text 17:27) and no line on the card; C3-663-681 had its three output files on disk (checked text 17:17) and no line on the card.
   - `braindump_board\cards\plan-now.md` lines 104 and 124 and `RUNBOOK_20261110.md` section 3.2 (9 Nov 16:35) give the state of 9 Nov afternoon ("C3 169-187 running", "44 packages left"). `LOGBOOK_20261110.md` lines 64–65 (17:14) agreed with the files when written.
   - RUNBOOK 3.2 defines a package as done "when `LM_<KEY>_checked.tex` exists". An agent writes `_checked.tex` several minutes before `_changes.md` and `_notes_checked.md` (LM_C4-039-057: 17:19, 17:22, 17:24), so that test reports a package done while it is being written.
5. **The pilot folder's `reader\` is the 8 Nov build.** Anyone opening `longue_marche_pro_pilot_20261104\reader\LM_reader_draft_140-2.tex` or `140-3.tex` gets the initial edition's reader, older than the published one; the 9 Nov build exists only in `lm_publish\repo\reader`, `lm_publish\assets` and a temp folder.

### Unknowns

- **State after 2026-11-10 17:31:09.** 4 agents were running and 6 finished packages had outputs written in the last 40 minutes. Settled by rerunning `tmp_lm\scripts\finalize.py` and `gen_md.py` once the agents have reported (they only read the project and rewrite this section's two files).
- **LM_P060: which return is the intended first pass.** Not recorded in `PLAN_RECORD.md`, `METHODOLOGY.md` or `NOTES_LEDGER.md`. Settled by the user (why the package was run twice) or by comparing both returns with scans 11–20.
- **The 33 open fixes of P011–P040.** Settled by looking at each listed place in the current text and on the scan (list: `second_pass\merge_fixes_open.md`).
- **That each agent read the file its prompt names** is shown by helper scripts for 30 of the 32 unpublished packages and by prompt and similarity alone for C3-131-149, C3-606-624; the agents' transcripts would settle those.
- **Release PDFs** were compared by the SHA-256 digest GitHub reports, not downloaded.
- **Copies outside the searched places** (deeper than two levels, other drives, cloud sessions): not searched.
