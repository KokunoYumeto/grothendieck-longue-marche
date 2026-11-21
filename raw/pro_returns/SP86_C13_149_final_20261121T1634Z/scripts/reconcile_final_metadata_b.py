#!/usr/bin/env python3
"""Apply the explicit metadata-only reconciliation proposed in reader_b's report.

Prepared for root inspection; not executed by its author.

Default invocation performs a read-only preflight and prints a plan summary.
Use --apply to write the 19 current review JSON files and a completion journal.
No manuscript page, aggregate, source image, or frozen second-pass file is a
write target. Dated review history and all audit/adjudication records are
preserved. Every changed field is guarded against the exact value embedded
below, and all guards are checked before any authoritative review is written.

The count blocks are recalculated from the current review arrays. Root has
directed that scan075's saved_crops=29 remain explicitly scoped to the historical
first pass. Its additional R30 root crop is recorded separately in that count
block. No crop image is read by this script.

The journal preserves each complete before/after value, finding ID, file hash,
and UTC. A pre-existing journal is never overwritten.
"""

from __future__ import annotations

import argparse
import copy
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import tempfile

BASE = Path(__file__).resolve().parents[1]
REVIEWS = BASE / "reviews"
REPORT = REVIEWS / "final_metadata_review_b.json"
REPORT_SHA256 = "ee685ec159304151ac1044c0e1b1064fbdbbb3da9d335158b072144fb71b2918"
JOURNAL = REVIEWS / "final_metadata_b_journal.json"
SCOPE = (
    "149_scan054", "149_scan055", "149_scan056", "149_scan057",
    "149_scan058", "149_scan059", "149_scan060", "149_scan061",
    "149_scan062", "149_scan063", "149_scan064", "149_scan066",
    "149_scan067", "149_scan068", "149_scan070", "149_scan071",
    "149_scan072", "149_scan073", "149_scan074", "149_scan075",
    "149_scan076",
)
MUTABLE_METADATA = {
    "notes", "hand", "notation", "abbreviations", "open_issues",
    "diff_coverage", "additional_diff_coverage", "deletion_insertion_review",
    "changes", "nonmaterial_observations", "counts",
}
PROTECTED_REVIEW_FIELDS = {
    "audit", "audit_adjudications", "audit_root_viewed", "root_adjudication",
    "accepted_utc", "accounting_reviews", "post_audit_notation_changes",
    "root_viewed", "decisions", "doubts", "inventory", "source_line_map",
    "supplied_mark_ids", "audit_boxes", "audit_coverage", "check_events",
    "viewed", "viewing_log", "reading_scope",
}
HISTORICAL_CROP_SCOPE = (
    "Historical first-pass total from the viewed P01-P29 crop list; excludes "
    "the separately recorded additional root crop R30 and all blind second crops."
)
ROOT_SCOPE_DECISION = {
    "finding": "MB055",
    "authority": "root instruction in the current run before script delivery",
    "decision": (
        "Retain scan075 saved_crops=29 with an explicit historical first-pass "
        "scope, and record the additional root R30 crop separately."
    ),
}

# Each entry is a literal, field-specific replacement and exact before-value
# guard. For count entries, 'after' is the reviewed preview; the implementation
# below refreshes the same explicitly named count fields from current data.

PLAN = json.loads(r'''
[
  {
    "finding": "MB001",
    "page": "149_scan054",
    "field": "notes[2]",
    "before": "S54-M (source marginal qualification): \"C'est démontré sauf pour le type (0,3), qui mérite un examen approfondi.\" The author's qualification is preserved; H's peut-être has no separate ink group here.",
    "after": "S54-M (source marginal qualification): \"C'est démontré sauf pour le type (0,3), \\unsure{qui|que} mérite un examen approfondi\\unsure{.}\" The author's qualification and its local reading uncertainties are preserved; H's peut-être has no separate ink group here.",
    "mode": "replace",
    "basis": "The source quotation states qui and a final point without the local uncertainties retained in the current marginal text."
  },
  {
    "finding": "MB002",
    "page": "149_scan054",
    "field": "diff_coverage[13].status",
    "before": "material; P05",
    "after": "nonmaterial; nonmaterial_observations P05 (unresolved numeral alternatives)",
    "mode": "replace",
    "basis": "The coverage status still labels P05 material although the current records place these rows in nonmaterial_observations."
  },
  {
    "finding": "MB003",
    "page": "149_scan055",
    "field": "diff_coverage[13].reason",
    "before": "The source reads ça marche; its cedilla and letter strokes also settle H's proposed struck-span boundary.",
    "after": "The source reads Ça marche; its cedilla and letter strokes also settle H's proposed struck-span boundary.",
    "mode": "replace",
    "basis": "This current coverage description still says lowercase ça marche; the audited current page and P13 change read uppercase Ça marche."
  },
  {
    "finding": "MB004",
    "page": "149_scan055",
    "field": "diff_coverage[5].status",
    "before": "material; P04",
    "after": "nonmaterial; nonmaterial_observations P04 (uncertain cancelled ending)",
    "mode": "replace",
    "basis": "The coverage status still labels P04, P09a and P11 material although the current records place these rows in nonmaterial_observations."
  },
  {
    "finding": "MB004",
    "page": "149_scan055",
    "field": "diff_coverage[9].status",
    "before": "material; P09a",
    "after": "nonmaterial; nonmaterial_observations P09a (unresolved verb alternatives)",
    "mode": "replace",
    "basis": "The coverage status still labels P04, P09a and P11 material although the current records place these rows in nonmaterial_observations."
  },
  {
    "finding": "MB004",
    "page": "149_scan055",
    "field": "diff_coverage[11].status",
    "before": "material; P11",
    "after": "nonmaterial; nonmaterial_observations P11 (unresolved de/des ending)",
    "mode": "replace",
    "basis": "The coverage status still labels P04, P09a and P11 material although the current records place these rows in nonmaterial_observations."
  },
  {
    "finding": "MB005",
    "page": "149_scan056",
    "field": "diff_coverage[6].reason",
    "before": "The small insertion starts de plus and continues with a third short word.",
    "after": "The small insertion remains \\inserted{\\unsure{de plus|bcp} \\unsure{des|de}}: its opening and following short word have separate local uncertainties.",
    "mode": "replace",
    "basis": "The insertion is described as definitely starting de plus, but M1146 was reopened and current text preserves de plus/bcp."
  },
  {
    "finding": "MB006",
    "page": "149_scan056",
    "field": "diff_coverage[5].reason",
    "before": "A separate dotted i appears between i.e. and un.",
    "after": "A separate dotted i appears between i.e (without a terminal stop at this occurrence) and un.",
    "mode": "replace",
    "basis": "The coverage sentence gives i.e. before the repeated i, while B04 removed the final stop at this occurrence."
  },
  {
    "finding": "MB007",
    "page": "149_scan057",
    "field": "abbreviations[3].written",
    "before": "=",
    "after": "\\unsure{=|\\overline m}",
    "mode": "replace",
    "basis": "The abbreviation and coverage still specify equals alone; current page, hand, notation and audit preserve equals/barred-m uncertainty."
  },
  {
    "finding": "MB007",
    "page": "149_scan057",
    "field": "diff_coverage[19].reason",
    "before": "The two written equals strokes are retained as shorthand.",
    "after": "The written shorthand remains \\unsure{=|\\overline m}; the local equals/barred-m alternatives are retained without expansion.",
    "mode": "replace",
    "basis": "The abbreviation and coverage still specify equals alone; current page, hand, notation and audit preserve equals/barred-m uncertainty."
  },
  {
    "finding": "MB008",
    "page": "149_scan057",
    "field": "diff_coverage[4].reason",
    "before": "Live classes de insertion is separated from the cancelled baseline words; the latter retain local doubts.",
    "after": "The raised phrase retains live/cancelled insertion alternatives in \\inserted{\\unsure{classes de|\\deleted{\\unsure{classes} de}}}. The baseline group separately retains \\unsure{\\deleted{\\unsure{par}\\ \\unsure{des}}|par des}; neither revision state is resolved.",
    "mode": "replace",
    "basis": "The coverage asserts a live classes de insertion and cancelled baseline words, while the audited page leaves both revision states open."
  },
  {
    "finding": "MB009",
    "page": "149_scan057",
    "field": "diff_coverage[8].reason",
    "before": "The parenthesis following sections is cancelled; the live comma precedes it.",
    "after": "The live comma after sections precedes a cancelled body retained as \\deleted{\\unsure{)|f|et}}.",
    "mode": "replace",
    "basis": "The coverage still identifies a cancelled parenthesis followed by definite et en. Current text qualifies the cancelled body as )/f/et and the live following word as en/un."
  },
  {
    "finding": "MB009",
    "page": "149_scan057",
    "field": "diff_coverage[10].reason",
    "before": "The source ends line 3 et en and begins line 4 mettant; H's extra illegible placeholder has no separate word in ink.",
    "after": "The source ends line 3 et \\unsure{en|un} and begins line 4 mettant; H's extra illegible placeholder has no separate word in ink.",
    "mode": "replace",
    "basis": "The coverage still identifies a cancelled parenthesis followed by definite et en. Current text qualifies the cancelled body as )/f/et and the live following word as en/un."
  },
  {
    "finding": "MB010",
    "page": "149_scan057",
    "field": "diff_coverage[12].status",
    "before": "material; P07",
    "after": "nonmaterial; nonmaterial_observations P07 (unresolved Z/C initial)",
    "mode": "replace",
    "basis": "The coverage status still labels P07 and P16 material although the current records place these rows in nonmaterial_observations."
  },
  {
    "finding": "MB010",
    "page": "149_scan057",
    "field": "diff_coverage[21].status",
    "before": "material; P16",
    "after": "nonmaterial; nonmaterial_observations P16 (unresolved dash/arrow connector)",
    "mode": "replace",
    "basis": "The coverage status still labels P07 and P16 material although the current records place these rows in nonmaterial_observations."
  },
  {
    "finding": "MB011",
    "page": "149_scan058",
    "field": "diff_coverage[7].reason",
    "before": "The written shorthand consists of two horizontal strokes and is retained as =.",
    "after": "The written shorthand is retained unexpanded as \\unsure{=|\\overline m}; the equals/barred-m form remains unresolved.",
    "mode": "replace",
    "basis": "Coverage still says the shorthand is retained as equals, while current text and hand/notation retain equals/barred-m uncertainty."
  },
  {
    "finding": "MB012",
    "page": "149_scan058",
    "field": "diff_coverage[10].reason",
    "before": "The source reads le normalisé and has a raised cancelled de above X′.",
    "after": "The source reads le normalisé, followed before X′ by \\unsure{\\deleted{de}|\\inserted{\\deleted{de}}|\\inserted{de}}. The local deletion/insertion state remains open.",
    "mode": "replace",
    "basis": "Coverage calls the raised de definitely cancelled. Current page preserves three states, including a live insertion."
  },
  {
    "finding": "MB013",
    "page": "149_scan058",
    "field": "diff_coverage[17].reason",
    "before": "l′ stays live, ens is crossed, the following dot is retained with scope doubt, and fibre is singular.",
    "after": "The l'e remains live; only tentative ns is cancelled in l'e\\deleted{\\unsure{ns}}\\unsure{.|\\deleted{.}}. The following point retains its separate scope doubt, and fibre is singular.",
    "mode": "replace",
    "basis": "Coverage says ens is crossed and the abbreviation entry calls it a cancelled abbreviation. The audited text leaves l'e live and crosses only tentative ns."
  },
  {
    "finding": "MB013",
    "page": "149_scan058",
    "field": "abbreviations[1].places",
    "before": "cancelled abbreviation in main line 15; possible reading in the line-13 insertion",
    "after": "partially cancelled abbreviation in main line 15: e remains live, tentative ns is cancelled, and the following point has separate cancellation-scope uncertainty; possible reading in the line-13 insertion",
    "mode": "replace",
    "basis": "Coverage says ens is crossed and the abbreviation entry calls it a cancelled abbreviation. The audited text leaves l'e live and crosses only tentative ns."
  },
  {
    "finding": "MB014",
    "page": "149_scan059",
    "field": "diff_coverage[16].reason",
    "before": "Two parallel strokes resolve the written equals sign.",
    "after": "The written shorthand remains unresolved as \\unsure{=|\\overline m}; neither candidate is expanded in the transcription.",
    "mode": "replace",
    "basis": "The coverage says the equals sign is resolved, but the current marginal text, hand entry and notation preserve equals/barred-m uncertainty."
  },
  {
    "finding": "MB015",
    "page": "149_scan059",
    "field": "diff_coverage[3].status",
    "before": "material; P02a",
    "after": "nonmaterial; nonmaterial_observations P02a (unresolved U/possible cancelled-K state)",
    "mode": "replace",
    "basis": "The coverage status still labels P02a material although the current records place these rows in nonmaterial_observations."
  },
  {
    "finding": "MB016",
    "page": "149_scan060",
    "field": "notes[6]",
    "before": "The initial abbreviation in main line 1 and the one after the dash in line 5 read i.e without a separate stop after e. The occurrence after Gamma in line 6 has its separate terminal stop on the native half and is retained as i.e.",
    "after": "The initial abbreviation in main line 1 is i\\unsure{.|:}e, with its internal point/colon unresolved and no separate stop after e. The occurrence after the dash in line 5 reads i.e without a separate terminal stop. The occurrence after Gamma in line 6 reads i.e. with its separate terminal stop retained.",
    "mode": "replace",
    "basis": "The first i.e occurrence is still described with a definite internal period, although its internal mark was broadened to period/colon; the terminal-stop comparison remains applicable."
  },
  {
    "finding": "MB016",
    "page": "149_scan060",
    "field": "hand[5].form",
    "before": "i.e / i.e.",
    "after": "i\\unsure{.|:}e / i.e / i.e.",
    "mode": "replace",
    "basis": "The first i.e occurrence is still described with a definite internal period, although its internal mark was broadened to period/colon; the terminal-stop comparison remains applicable."
  },
  {
    "finding": "MB016",
    "page": "149_scan060",
    "field": "hand[5].observation",
    "before": "The two inspected i.e forms at lines 1 and 5 have no separate terminal stop, while the line 6 form visibly has one.",
    "after": "The line-1 form is i\\unsure{.|:}e: its internal point/colon remains unresolved. Both line-1 and line-5 occurrences have no separate terminal stop, while the line-6 i.e. form visibly has one.",
    "mode": "replace",
    "basis": "The first i.e occurrence is still described with a definite internal period, although its internal mark was broadened to period/colon; the terminal-stop comparison remains applicable."
  },
  {
    "finding": "MB016",
    "page": "149_scan060",
    "field": "abbreviations[2].written",
    "before": "i.e / i.e.",
    "after": "i\\unsure{.|:}e / i.e / i.e.",
    "mode": "replace",
    "basis": "The first i.e occurrence is still described with a definite internal period, although its internal mark was broadened to period/colon; the terminal-stop comparison remains applicable."
  },
  {
    "finding": "MB017",
    "page": "149_scan060",
    "field": "abbreviations[3]",
    "before": {
      "written": "=",
      "expansion": "même",
      "places": "main lines 2, 4, 7, 12"
    },
    "after": {
      "written": "\\unsure{=|\\overline m}",
      "expansion": "même",
      "places": "main lines 2, 4, 7, 12, and the final marginal line before écrire"
    },
    "mode": "replace",
    "basis": "These entries still identify or resolve the prose shorthand as equals. The page and updated hand/notation retain equals/barred-m at all five occurrences, including the recovered margin occurrence."
  },
  {
    "finding": "MB017",
    "page": "149_scan060",
    "field": "diff_coverage[3].reason",
    "before": "sur le and the written equals shorthand are visible, replacing H's au-dessus de.",
    "after": "The source has sur le followed by the unresolved written shorthand \\unsure{=|\\overline m}, replacing H's au-dessus de.",
    "mode": "replace",
    "basis": "These entries still identify or resolve the prose shorthand as equals. The page and updated hand/notation retain equals/barred-m at all five occurrences, including the recovered margin occurrence."
  },
  {
    "finding": "MB017",
    "page": "149_scan060",
    "field": "diff_coverage[4].reason",
    "before": "M1162 resolves to the written equals shorthand without expansion.",
    "after": "M1162 remains undecided as \\unsure{=|\\overline m}; the written shorthand is retained without expansion.",
    "mode": "replace",
    "basis": "These entries still identify or resolve the prose shorthand as equals. The page and updated hand/notation retain equals/barred-m at all five occurrences, including the recovered margin occurrence."
  },
  {
    "finding": "MB017",
    "page": "149_scan060",
    "field": "diff_coverage[7].reason",
    "before": "M1164 resolves to the written equals shorthand.",
    "after": "M1164 remains undecided as \\unsure{=|\\overline m}; the written shorthand is retained without expansion.",
    "mode": "replace",
    "basis": "These entries still identify or resolve the prose shorthand as equals. The page and updated hand/notation retain equals/barred-m at all five occurrences, including the recovered margin occurrence."
  },
  {
    "finding": "MB017",
    "page": "149_scan060",
    "field": "diff_coverage[13].reason",
    "before": "M1165 resolves to the written equals shorthand.",
    "after": "M1165 remains undecided as \\unsure{=|\\overline m}; the written shorthand is retained without expansion.",
    "mode": "replace",
    "basis": "These entries still identify or resolve the prose shorthand as equals. The page and updated hand/notation retain equals/barred-m at all five occurrences, including the recovered margin occurrence."
  },
  {
    "finding": "MB018",
    "page": "149_scan060",
    "field": "abbreviations[0].written",
    "before": "pt",
    "after": "p\\textsuperscript{t} / pt",
    "mode": "replace",
    "basis": "The abbreviation inventory represents both occurrences as baseline pt, while the audited first occurrence has a raised t."
  },
  {
    "finding": "MB018",
    "page": "149_scan060",
    "field": "abbreviations[0].places",
    "before": "main lines 2 and 4",
    "after": "main line 2: p\\textsuperscript{t} with raised t; main line 4: baseline pt",
    "mode": "replace",
    "basis": "The abbreviation inventory represents both occurrences as baseline pt, while the audited first occurrence has a raised t."
  },
  {
    "finding": "MB019",
    "page": "149_scan060",
    "field": "open_issues[0]",
    "before": "Unresolved after root review: older canceled x candidate at P07; the lower letters and their vertical placement after crossed Z at P15. Retained locally and listed for the independent reread.",
    "after": "Unresolved after the completed independent audit: the older cancelled P07 body remains \\deleted{\\unsure{x|\\mathrm{en}}}; at P15, the lower fragment after the crossed tentative Z remains baseline er/en or lowered en/pi, as encoded in the current doubt entry. The live tilde-x and the narrow strike scope are retained.",
    "mode": "replace",
    "basis": "The current open-issues prose still lists only the older x candidate and says it is awaiting the independent reread. The completed audit broadened that fragment to x/en and the later fragment to baseline er/en or lowered en/pi."
  },
  {
    "finding": "MB020",
    "page": "149_scan061",
    "field": "abbreviations[3].written",
    "before": "=",
    "after": "\\unsure{=|\\overline m}",
    "mode": "replace",
    "basis": "The abbreviation inventory says equals and coverage calls M1166 resolved, but the current text and updated hand/notation retain equals/barred-m uncertainty."
  },
  {
    "finding": "MB020",
    "page": "149_scan061",
    "field": "diff_coverage[3].reason",
    "before": "The literal shorthand sign is read on its crop; C mark M1166 is resolved and H's expansion is removed.",
    "after": "C mark M1166 remains undecided as \\unsure{=|\\overline m}. The written shorthand stays unexpanded; H's full expansion is excluded from the source text.",
    "mode": "replace",
    "basis": "The abbreviation inventory says equals and coverage calls M1166 resolved, but the current text and updated hand/notation retain equals/barred-m uncertainty."
  },
  {
    "finding": "MB021",
    "page": "149_scan061",
    "field": "diff_coverage[8].status",
    "before": "material; P04",
    "after": "nonmaterial; nonmaterial_observations P04 (unresolved des/de ending)",
    "mode": "replace",
    "basis": "The coverage status still labels P04 material although the current records place these rows in nonmaterial_observations."
  },
  {
    "finding": "MB022",
    "page": "149_scan062",
    "field": "notation[3]",
    "before": {
      "form": "=",
      "meaning": "Literal two-stroke sign written before the pair of barred curve names; no expansion or mathematical interpretation assigned here.",
      "places": "line 11, P06"
    },
    "after": {
      "form": "\\unsure{=}",
      "meaning": "The current transcription retains the sign before the barred curve names as tentative equals, matching notation[8]; no expansion or mathematical interpretation is assigned here.",
      "places": "line 11, P06"
    },
    "mode": "replace",
    "basis": "An older notation entry and coverage still call the sign literal equals and M1168 resolved, contradicting the current unsure equals and updated notation[8]."
  },
  {
    "finding": "MB022",
    "page": "149_scan062",
    "field": "diff_coverage[3].reason",
    "before": "The two-bar sign is present; M1168 is resolved to =.",
    "after": "The sign before the barred curve names remains \\unsure{=}; M1168 is undecided after the completed audit.",
    "mode": "replace",
    "basis": "An older notation entry and coverage still call the sign literal equals and M1168 resolved, contradicting the current unsure equals and updated notation[8]."
  },
  {
    "finding": "MB023",
    "page": "149_scan062",
    "field": "open_issues[0]",
    "before": "Unresolved after root review: P07 e/a; P09 E/É; P10 dark point status and separate-bar versus retraced-tilde decoration. Each remains explicit and is included in the blind reread.",
    "after": "Unresolved after the completed independent audit: P07 retains e/a in définiss\\unsure{e|a}nt; P10 retains the separate-bar versus retraced-tilde decoration alternatives; M1168/B04 retains \\unsure{=}; B09 retains the first completion-word accent in compl\\unsure{é|e}tée. Étant and the period after Poincaré are resolved and are not current open issues.",
    "mode": "replace",
    "basis": "The open-issues list says E/É and the dark point after Poincaré remain unresolved and await reread. The completed audit resolved Étant and the period, while retaining the upper-decoration doubt and adding tentative equals and completion-accent doubt."
  },
  {
    "finding": "MB024",
    "page": "149_scan062",
    "field": "diff_coverage[7].reason",
    "before": "The ink supports complétée and an inserted ordinary hatted U, with a curved leader and separate comma.",
    "after": "The completion word is retained as compl\\unsure{é|e}tée, with its first accent uncertain. The inserted ordinary hatted U, curved leader and separate comma remain as recorded.",
    "mode": "replace",
    "basis": "Coverage gives the completion word as definitely complétée, whereas the audited first accent is local é/e uncertainty."
  },
  {
    "finding": "MB025",
    "page": "149_scan062",
    "field": "diff_coverage[4].status",
    "before": "material; P07",
    "after": "nonmaterial; nonmaterial_observations P07 (unresolved e/a vowel)",
    "mode": "replace",
    "basis": "The coverage status still labels P07 material although the current records place these rows in nonmaterial_observations."
  },
  {
    "finding": "MB026",
    "page": "149_scan064",
    "field": "diff_coverage[0].reason",
    "before": "The source opening Que deviendraient is recovered from P01; the C scan marker 64 is editorial and is not source text.",
    "after": "The current source opening is Que \\unsure{deviendraient|donneraient}, with the verb alternatives retained from P01/B01. C's scan marker 64 is editorial and is not source text.",
    "mode": "replace",
    "basis": "The coverage identifies the opening verb as recovered deviendraient without the audited donneraient alternative."
  },
  {
    "finding": "MB027",
    "page": "149_scan064",
    "field": "diff_coverage[11].reason",
    "before": "M1175 is resolved to the first reading (5), at medium confidence, from the saved whole-diagram crop.",
    "after": "M1175 remains undecided as \\unsure{(5)|(4')}, with (5) first. The numeral observation is retained in nonmaterial_observations P13 and contributes no material-correction count.",
    "mode": "replace",
    "basis": "Coverage says M1175 is resolved to (5), contradicting the reopened (5)/(4-prime) decision and current diagram label."
  },
  {
    "finding": "MB028",
    "page": "149_scan064",
    "field": "diff_coverage[1].status",
    "before": "material; P02",
    "after": "nonmaterial; nonmaterial_observations P02 (unresolved à/colon)",
    "mode": "replace",
    "basis": "The coverage status still labels P02 and P13 material although the current records place these rows in nonmaterial_observations."
  },
  {
    "finding": "MB028",
    "page": "149_scan064",
    "field": "diff_coverage[11].status",
    "before": "material; P13",
    "after": "nonmaterial; nonmaterial_observations P13 (unresolved diagram numeral)",
    "mode": "replace",
    "basis": "The coverage status still labels P02 and P13 material although the current records place these rows in nonmaterial_observations."
  },
  {
    "finding": "MB029",
    "page": "149_scan064",
    "field": "additional_diff_coverage[0]",
    "before": "Plain E/U versus H's calligraphic alphabets, not isolated by the token-difference table, is inspected at every occurrence and covered by changes P04, P06, P08, P12, P16, P19, P21, P23 and P25.",
    "after": "Plain E/U versus H's calligraphic wrappers is documented in nonmaterial_observations P04, P06, P12, P16, P19, P21, P23 and P25. The same glyph-mapping observation in P08 contributes no separate alphabet count; P08 remains material for the independently recorded vertical diagram layout, downward arrow and number placement.",
    "mode": "replace",
    "basis": "The supplementary alphabet-coverage description still says moved E/U-wrapper rows are covered by changes, naming P04/P06/P12/P16/P19/P21/P23/P25 that are now nonmaterial observations."
  },
  {
    "finding": "MB030",
    "page": "149_scan064",
    "field": "nonmaterial_observations[0]",
    "before": {
      "id": "P05",
      "place": "Main line 6, immediately after relative",
      "C": "relative",
      "H": "relative",
      "final": "relative\\unsure{.}",
      "evidence": "A tiny isolated dark interword mark is visible just after relative, at about (758,711). Its position and ink permit a point, but its very small body does not establish punctuation with confidence. The tentative point is retained as uncertain, with the possibility of an incidental ink mark explicitly open.",
      "crop": "crops/149_scan064_P05.png",
      "box": [
        508,
        630,
        1545,
        773
      ],
      "confidence": "low",
      "against_C": true,
      "against_H": true,
      "kind": "omission",
      "error_category": "Other",
      "marked_in_H": false,
      "consequential": false,
      "exclusion_reason": "Added uncertainty about a possible point; retained in doubts, outside material-change counts."
    },
    "after": {
      "id": "P05",
      "place": "Main line 6, immediately after relative",
      "C": "relative",
      "H": "relative",
      "final": "relative\\unsure{.}",
      "evidence": "A tiny isolated dark interword mark is visible just after relative, at about (758,711). Its position and ink permit a point, but its very small body does not establish punctuation with confidence. The tentative point is retained as uncertain, with the possibility of an incidental ink mark explicitly open.",
      "crop": "crops/149_scan064_P05.png",
      "box": [
        508,
        630,
        1545,
        773
      ],
      "confidence": "low",
      "against_C": false,
      "against_H": false,
      "kind": "omission",
      "error_category": "Other",
      "marked_in_H": false,
      "consequential": false,
      "exclusion_reason": "Added uncertainty about a possible point; retained in doubts, outside material-change counts."
    },
    "mode": "replace",
    "basis": "P05 retains against_C/against_H=true despite its exclusion as added uncertainty; P23/P25 retain against_H=true despite their explicit E-wrapper-only exclusion. Other nonmaterial records use false flags."
  },
  {
    "finding": "MB030",
    "page": "149_scan064",
    "field": "nonmaterial_observations[1]",
    "before": {
      "id": "P23",
      "place": "Main line 12, expression after surjectif",
      "C": "E_K\\longrightarrow E_S",
      "H": "\\mathcal{E}_K\\to\\mathcal{E}_S",
      "final": "E_K\\longrightarrow E_S",
      "evidence": "The two E letters retain the recurring curved form under the plain E mapping; the first lower letter has the angular K limbs, and the second has the curved S body. A dark head is present at the right end of the connecting shaft.",
      "crop": "crops/149_scan064_P14.png",
      "box": [
        397,
        2083,
        1270,
        2202
      ],
      "confidence": "high",
      "against_C": false,
      "against_H": true,
      "kind": "misread symbol or index",
      "error_category": "Symbols and indices",
      "marked_in_H": false,
      "consequential": false,
      "exclusion_reason": "The recurring two-lobed E has a single established transcription mapping; the E/mathcal-E rendering difference alone supplies no independent source-letter distinction."
    },
    "after": {
      "id": "P23",
      "place": "Main line 12, expression after surjectif",
      "C": "E_K\\longrightarrow E_S",
      "H": "\\mathcal{E}_K\\to\\mathcal{E}_S",
      "final": "E_K\\longrightarrow E_S",
      "evidence": "The two E letters retain the recurring curved form under the plain E mapping; the first lower letter has the angular K limbs, and the second has the curved S body. A dark head is present at the right end of the connecting shaft.",
      "crop": "crops/149_scan064_P14.png",
      "box": [
        397,
        2083,
        1270,
        2202
      ],
      "confidence": "high",
      "against_C": false,
      "against_H": false,
      "kind": "misread symbol or index",
      "error_category": "Symbols and indices",
      "marked_in_H": false,
      "consequential": false,
      "exclusion_reason": "The recurring two-lobed E has a single established transcription mapping; the E/mathcal-E rendering difference alone supplies no independent source-letter distinction."
    },
    "mode": "replace",
    "basis": "P05 retains against_C/against_H=true despite its exclusion as added uncertainty; P23/P25 retain against_H=true despite their explicit E-wrapper-only exclusion. Other nonmaterial records use false flags."
  },
  {
    "finding": "MB030",
    "page": "149_scan064",
    "field": "nonmaterial_observations[2]",
    "before": {
      "id": "P25",
      "place": "Main line 14, final E_K to E_S expression",
      "C": "E_K\\longrightarrow E_S",
      "H": "\\mathcal{E}_K\\to\\mathcal{E}_S",
      "final": "E_K\\longrightarrow E_S",
      "evidence": "The first lower letter has the angular K limbs, the final lower letter has the S curve, and the right-pointing head is separated slightly from the shaft. Both main E bodies repeat the curved two-lobed form already mapped to plain E.",
      "crop": "crops/149_scan064_P16.png",
      "box": [
        421,
        2250,
        698,
        2343
      ],
      "confidence": "high",
      "against_C": false,
      "against_H": true,
      "kind": "misread symbol or index",
      "error_category": "Symbols and indices",
      "marked_in_H": false,
      "consequential": false,
      "exclusion_reason": "The recurring two-lobed E has a single established transcription mapping; the E/mathcal-E rendering difference alone supplies no independent source-letter distinction."
    },
    "after": {
      "id": "P25",
      "place": "Main line 14, final E_K to E_S expression",
      "C": "E_K\\longrightarrow E_S",
      "H": "\\mathcal{E}_K\\to\\mathcal{E}_S",
      "final": "E_K\\longrightarrow E_S",
      "evidence": "The first lower letter has the angular K limbs, the final lower letter has the S curve, and the right-pointing head is separated slightly from the shaft. Both main E bodies repeat the curved two-lobed form already mapped to plain E.",
      "crop": "crops/149_scan064_P16.png",
      "box": [
        421,
        2250,
        698,
        2343
      ],
      "confidence": "high",
      "against_C": false,
      "against_H": false,
      "kind": "misread symbol or index",
      "error_category": "Symbols and indices",
      "marked_in_H": false,
      "consequential": false,
      "exclusion_reason": "The recurring two-lobed E has a single established transcription mapping; the E/mathcal-E rendering difference alone supplies no independent source-letter distinction."
    },
    "mode": "replace",
    "basis": "P05 retains against_C/against_H=true despite its exclusion as added uncertainty; P23/P25 retain against_H=true despite their explicit E-wrapper-only exclusion. Other nonmaterial records use false flags."
  },
  {
    "finding": "MB031",
    "page": "149_scan066",
    "field": "open_issues[1]",
    "before": "M1176/P03: retain the single galoisiens doubt; medial letters remain crowded.",
    "after": "M1176/P03: the upper insertion retains three local alternatives, \\inserted{(\\unsure{en|ou} \\unsure{topos|types} \\unsure{galoisiques|galoisiens})}. Its crowded letters remain unresolved.",
    "mode": "replace",
    "basis": "The upper insertion is still described as a single galoisiens doubt with definite topos. Current text separately preserves en/ou, topos/types and galoisiques/galoisiens."
  },
  {
    "finding": "MB031",
    "page": "149_scan066",
    "field": "diff_coverage[2].reason",
    "before": "The last oval and s-like stroke support the written topos.",
    "after": "The current upper insertion retains \\unsure{en|ou}, \\unsure{topos|types} and \\unsure{galoisiques|galoisiens} as separate local uncertainties.",
    "mode": "replace",
    "basis": "The upper insertion is still described as a single galoisiens doubt with definite topos. Current text separately preserves en/ou, topos/types and galoisiques/galoisiens."
  },
  {
    "finding": "MB032",
    "page": "149_scan066",
    "field": "open_issues[3]",
    "before": "P12: retain de|des inside the deletion; the terminal body is obscured by the strike.",
    "after": "P12: retain \\deleted{\\unsure{de|des|du}} under the strike. The following insertion reads (plutôt sections) with \\unsure{du|dans} after its parenthesis; both local doubts remain open.",
    "mode": "replace",
    "basis": "Coverage retains the superseded (ou les sections) du insertion and the old de/des deletion choice. Current text reads (plutôt sections), leaves du/dans open and includes du in the cancelled-word alternatives."
  },
  {
    "finding": "MB032",
    "page": "149_scan066",
    "field": "diff_coverage[16].reason",
    "before": "The misaligned witness row is covered by the paired point-quotes, the cancelled de/des doubt, and the inserted (ou les sections) du at its actual attachment.",
    "after": "The misaligned witness row is covered by the paired point-quotes, \\deleted{\\unsure{de|des|du}}, and the inserted (plutôt sections) \\unsure{du|dans} at its recorded attachment.",
    "mode": "replace",
    "basis": "Coverage retains the superseded (ou les sections) du insertion and the old de/des deletion choice. Current text reads (plutôt sections), leaves du/dans open and includes du in the cancelled-word alternatives."
  },
  {
    "finding": "MB032",
    "page": "149_scan066",
    "field": "diff_coverage[17].reason",
    "before": "The cancelled word remains narrow; du follows the inserted parenthesis; topos remains live on the main baseline.",
    "after": "The cancelled word remains \\deleted{\\unsure{de|des|du}}. The inserted parenthesis reads (plutôt sections), followed by \\unsure{du|dans}; topos remains live on the main baseline.",
    "mode": "replace",
    "basis": "Coverage retains the superseded (ou les sections) du insertion and the old de/des deletion choice. Current text reads (plutôt sections), leaves du/dans open and includes du in the cancelled-word alternatives."
  },
  {
    "finding": "MB033",
    "page": "149_scan066",
    "field": "diff_coverage[22].reason",
    "before": "The visible words read deux cas., with the stop retained.",
    "after": "The current reading is \\unsure{isom|deux} can., with the first word unresolved and the written stop after can retained.",
    "mode": "replace",
    "basis": "Coverage says the words read deux cas.; current audited text has isom/deux uncertainty and can. with n."
  },
  {
    "finding": "MB034",
    "page": "149_scan066",
    "field": "diff_coverage[1].status",
    "before": "material; P01",
    "after": "nonmaterial; nonmaterial_observations P01 (unresolved le/ce article)",
    "mode": "replace",
    "basis": "The coverage status still labels P01, P11a and P12a material although the current records place these rows in nonmaterial_observations."
  },
  {
    "finding": "MB034",
    "page": "149_scan066",
    "field": "diff_coverage[14].status",
    "before": "material; P11a",
    "after": "nonmaterial; nonmaterial_observations P11a (same-source circular superscript mapping)",
    "mode": "replace",
    "basis": "The coverage status still labels P01, P11a and P12a material although the current records place these rows in nonmaterial_observations."
  },
  {
    "finding": "MB034",
    "page": "149_scan066",
    "field": "diff_coverage[16].status",
    "before": "material; P10c, P12a, P12b",
    "after": "material; P10c, P12b; nonmaterial_observations P12a (uncertain cancelled word)",
    "mode": "replace",
    "basis": "The coverage status still labels P01, P11a and P12a material although the current records place these rows in nonmaterial_observations."
  },
  {
    "finding": "MB034",
    "page": "149_scan066",
    "field": "diff_coverage[17].status",
    "before": "material; P12a, P12b, P12c",
    "after": "material; P12b, P12c; nonmaterial_observations P12a (uncertain cancelled word)",
    "mode": "replace",
    "basis": "The coverage status still labels P01, P11a and P12a material although the current records place these rows in nonmaterial_observations."
  },
  {
    "finding": "MB035",
    "page": "149_scan067",
    "field": "notation[4].form",
    "before": "K_1=Q(\\deleted{\\unsure{X_1|x_1}}\\,T_1)",
    "after": "K_1=Q(\\deleted{\\unsure{X|x}_{\\unsure{1|4}}}\\,T_1)",
    "mode": "replace",
    "basis": "These entries still make the cancelled low numeral a definite 1, while the completed audit reopened it as 1/4 independently of X/x case."
  },
  {
    "finding": "MB035",
    "page": "149_scan067",
    "field": "open_issues[2]",
    "before": "P16: canceled X_1/x_1 retains its case doubt; the visible low 1 is included.",
    "after": "P16: the cancelled variable retains separate X/x and 1/4 uncertainties, \\deleted{\\unsure{X|x}_{\\unsure{1|4}}}.",
    "mode": "replace",
    "basis": "These entries still make the cancelled low numeral a definite 1, while the completed audit reopened it as 1/4 independently of X/x case."
  },
  {
    "finding": "MB035",
    "page": "149_scan067",
    "field": "diff_coverage[17].reason",
    "before": "The canceled variable has a visible low 1; the X/x case remains uncertain.",
    "after": "The cancelled variable retains a low numeral with 1/4 alternatives, independently of its X/x case uncertainty.",
    "mode": "replace",
    "basis": "These entries still make the cancelled low numeral a definite 1, while the completed audit reopened it as 1/4 independently of X/x case."
  },
  {
    "finding": "MB035",
    "page": "149_scan067",
    "field": "deletion_insertion_review[3]",
    "before": "P16: C's canceled variable inside Q(…) is struck by diagonal hatching. A lower 1 remains visible. T_1 to its right is live. The X/x letter case remains doubtful.",
    "after": "P16: C's cancelled variable inside Q(…) is struck by diagonal hatching. The lower numeral remains 1/4, and the letter case remains X/x. T_1 to its right is live; the recorded cancellation scope is unchanged.",
    "mode": "replace",
    "basis": "These entries still make the cancelled low numeral a definite 1, while the completed audit reopened it as 1/4 independently of X/x case."
  },
  {
    "finding": "MB036",
    "page": "149_scan067",
    "field": "open_issues[0]",
    "before": "P05 / M1182: peut/pourra remains unresolved at the compressed terminal group.",
    "after": "P05 / M1182: peut/pourra/pour remains unresolved at the compressed terminal group.",
    "mode": "replace",
    "basis": "The current issue/abbreviation descriptions omit the new pour and ari alternatives, retaining the earlier narrower candidate sets."
  },
  {
    "finding": "MB036",
    "page": "149_scan067",
    "field": "open_issues[1]",
    "before": "P11: canceled ar. retains its narrow letter/punctuation uncertainty.",
    "after": "P11: the cancelled ending remains ar./ari. In the full fragment \\deleted{``sph\\unsure{è|ê}re \\unsure{ar.|ari}}, the accent and the abbreviation ending retain their separate uncertainties.",
    "mode": "replace",
    "basis": "The current issue/abbreviation descriptions omit the new pour and ari alternatives, retaining the earlier narrower candidate sets."
  },
  {
    "finding": "MB036",
    "page": "149_scan067",
    "field": "abbreviations[3].written",
    "before": "\\unsure{ar.}",
    "after": "\\unsure{ar.|ari}",
    "mode": "replace",
    "basis": "The current issue/abbreviation descriptions omit the new pour and ari alternatives, retaining the earlier narrower candidate sets."
  },
  {
    "finding": "MB036",
    "page": "149_scan067",
    "field": "diff_coverage[6].reason",
    "before": "The one compressed p-word remains peut/pourra under doubt; H reads two words prend deux.",
    "after": "The one compressed p-word remains peut/pourra/pour under doubt; H reads two words prend deux.",
    "mode": "replace",
    "basis": "The current issue/abbreviation descriptions omit the new pour and ari alternatives, retaining the earlier narrower candidate sets."
  },
  {
    "finding": "MB036",
    "page": "149_scan067",
    "field": "diff_coverage[10].reason",
    "before": "The short canceled ar. group is retained with its narrow uncertainty; H uses an illegibility mark.",
    "after": "The short cancelled group retains ar./ari alternatives; H uses an illegibility mark. The full cancelled phrase also preserves its separate è/ê accent uncertainty.",
    "mode": "replace",
    "basis": "The current issue/abbreviation descriptions omit the new pour and ari alternatives, retaining the earlier narrower candidate sets."
  },
  {
    "finding": "MB037",
    "page": "149_scan067",
    "field": "diff_coverage[8].reason",
    "before": "The ink reads on at the line end and trouve on the following line. H's illegibility mark spans this phrase; extra hyphen tokens represent a dash.",
    "after": "The current reading retains \\unsure{on|en} at the line end and trouve on the following line. H's illegibility mark spans this phrase; extra hyphen tokens represent a dash.",
    "mode": "replace",
    "basis": "Coverage still states definite on and remonte, whereas the current text qualifies on/en and remonte/prendre/prendra."
  },
  {
    "finding": "MB037",
    "page": "149_scan067",
    "field": "diff_coverage[22].reason",
    "before": "The m humps and final tall t support remonte.",
    "after": "The word before comme remains \\unsure{remonte|prendre|prendra}; the local alternatives are retained without settling the compressed letter sequence.",
    "mode": "replace",
    "basis": "Coverage still states definite on and remonte, whereas the current text qualifies on/en and remonte/prendre/prendra."
  },
  {
    "finding": "MB038",
    "page": "149_scan068",
    "field": "open_issues[0]",
    "before": "M1187: retain the uncertain comma after the first K_1.",
    "after": "M1187 remains undecided for the full expression \\unsure{K_{1\\deleted{2}}|K_1,|K_{12}}: the lower mark may be a cancelled 2, a comma after K_1, or a live 2 in K_{12}.",
    "mode": "replace",
    "basis": "The old comma-only description omits the current cancelled-2 and live-2 alternatives of M1187."
  },
  {
    "finding": "MB038",
    "page": "149_scan068",
    "field": "diff_coverage[3].reason",
    "before": "The dark mark after the first K_1 remains a tentative comma; M1187 is undecided, and its ink is retained.",
    "after": "The full expression remains \\unsure{K_{1\\deleted{2}}|K_1,|K_{12}}. M1187 is undecided across the cancelled-2, comma and live-2 alternatives, and its ink is retained.",
    "mode": "replace",
    "basis": "The old comma-only description omits the current cancelled-2 and live-2 alternatives of M1187."
  },
  {
    "finding": "MB039",
    "page": "149_scan070",
    "field": "deletion_insertion_review[2]",
    "before": "C nested la section: small phrase lies above the outer opening; its leader enters after composé de, before E_K. Both words retain inserted status there; P07/B08. H's de section after un relèvement differs from the observed letters and attachment.",
    "after": "C nested la section: small phrase lies above the outer opening; its leader enters after composé de, before the first inserted relation beginning E_{\\unsure{\\eta|K}}. Both words retain inserted status there; P07/B08. H's de section after un relèvement differs from the observed letters and attachment.",
    "mode": "replace",
    "basis": "The nested insertion description still locates la section immediately before definite E_K, although that left index was reopened by the blind audit."
  },
  {
    "finding": "MB040",
    "page": "149_scan071",
    "field": "abbreviations[1].expansion",
    "before": "même (prose shorthand; the exact written form remains unresolved)",
    "after": "même (editorial expansion of the prose shorthand; its written form is resolved to \\overline{m} by the separately dated final comparison)",
    "mode": "replace",
    "basis": "The expansion field still says the written shorthand remains unresolved, after the dated post-audit resolution to barred m."
  },
  {
    "finding": "MB041",
    "page": "149_scan071",
    "field": "open_issues[1]",
    "before": "P08: the canceled nor- fragment remains tentative under intersecting ink.",
    "after": "P08: the cancelled nor-/pro- fragment remains tentative under intersecting ink.",
    "mode": "replace",
    "basis": "The descriptive fields retain the earlier single nor- candidate rather than the current nor-/pro- alternatives."
  },
  {
    "finding": "MB041",
    "page": "149_scan071",
    "field": "diff_coverage[12].reason",
    "before": "The lower canceled fragment remains tentatively nor-, and the raised live replacement is fermé. H omits the fragment and cancels the replacement.",
    "after": "The lower cancelled fragment remains nor-/pro-, and the raised live replacement is fermé. H omits the fragment and cancels the replacement.",
    "mode": "replace",
    "basis": "The descriptive fields retain the earlier single nor- candidate rather than the current nor-/pro- alternatives."
  },
  {
    "finding": "MB041",
    "page": "149_scan071",
    "field": "deletion_insertion_review[3]",
    "before": "P08: the horizontal strike crosses the lower tentative nor- fragment after sous-groupe. The raised fermé is live and replaces it at that attachment, before engendré. The upper f descender enters the lower cancellation area and does not cancel the replacement. The underlying letters remain uncertain within the deletion.",
    "after": "P08: the horizontal strike crosses the lower tentative nor-/pro- fragment after sous-groupe. The raised fermé is live and replaces it at that attachment, before engendré. The upper f descender enters the lower cancellation area and does not cancel the replacement. The underlying letters remain uncertain within the deletion.",
    "mode": "replace",
    "basis": "The descriptive fields retain the earlier single nor- candidate rather than the current nor-/pro- alternatives."
  },
  {
    "finding": "MB042",
    "page": "149_scan071",
    "field": "open_issues[2]",
    "before": "P10: the canceled tant fragment remains tentative under the strike.",
    "after": "P10: live t. precedes the separately cancelled \\unsure{un|de} fragment. The following live short word remains \\unsure{ne|un}.",
    "mode": "replace",
    "basis": "These descriptions still treat the next line as beginning with a wholly cancelled tant fragment; the audited text instead has live t. followed by cancelled un/de."
  },
  {
    "finding": "MB042",
    "page": "149_scan071",
    "field": "diff_coverage[14].reason",
    "before": "The live line-end sequence is pour- followed on the next line by a canceled tentative tant. H supplies pourraient and a struck illegible fragment.",
    "after": "The live line-end sequence pour- is followed on the next line by live t., then \\deleted{\\unsure{un|de}} and live \\unsure{ne|un}. H supplies pourraient and a struck illegible fragment.",
    "mode": "replace",
    "basis": "These descriptions still treat the next line as beginning with a wholly cancelled tant fragment; the audited text instead has live t. followed by cancelled un/de."
  },
  {
    "finding": "MB042",
    "page": "149_scan071",
    "field": "deletion_insertion_review[4]",
    "before": "P09/P10: the line-end pour- remains live, including its hyphen. The following line begins with the canceled tentative tant fragment; the cancellation ends before the live ne recouvrent pas. No full underlying word or normalized line-break spelling is supplied.",
    "after": "P09/P10: the line-end pour- remains live, including its hyphen. The following line begins with live t. and its stop, followed by the separately cancelled \\unsure{un|de} fragment. The strike ends before live \\unsure{ne|un} recouvrent pas. No full underlying word or normalized line-break spelling is supplied.",
    "mode": "replace",
    "basis": "These descriptions still treat the next line as beginning with a wholly cancelled tant fragment; the audited text instead has live t. followed by cancelled un/de."
  },
  {
    "finding": "MB042",
    "page": "149_scan071",
    "field": "changes[6].evidence",
    "before": "The visible sequence is a descending p, closed o, low u, a short angular r shoulder, and a detached terminal hyphen. No further letters follow that hyphen on this line. The next line begins with a separately canceled fragment, recorded in P10. The written hyphen is retained.",
    "after": "The visible sequence is a descending p, closed o, low u, a short angular r shoulder, and a detached terminal hyphen. No further letters follow that hyphen on this line. The next line begins with live t. followed by the separately cancelled un/de fragment, recorded in P10. The written hyphen is retained.",
    "mode": "replace",
    "basis": "These descriptions still treat the next line as beginning with a wholly cancelled tant fragment; the audited text instead has live t. followed by cancelled un/de."
  },
  {
    "finding": "MB043",
    "page": "149_scan071",
    "field": "diff_coverage[15].reason",
    "before": "The live verb is recouvrent immediately after ne; the word order and ending are both visible.",
    "after": "The live verb recouvrent follows the uncertain \\unsure{ne|un} group and is followed by pas; the verb ending and this order remain visible.",
    "mode": "replace",
    "basis": "The live word before recouvrent is described as definite ne despite the current ne/un alternatives."
  },
  {
    "finding": "MB044",
    "page": "149_scan071",
    "field": "diff_coverage[10].reason",
    "before": "The tall looped f and surviving final re support préfère against H's tentative prend.",
    "after": "The tall looped f and surviving final re support pr\\unsure{é|e}fère against H's tentative prend; the first accent remains locally uncertain.",
    "mode": "replace",
    "basis": "The coverage explanation spells the first accent of préfère as settled, whereas the current text and P07 keep é/e uncertain."
  },
  {
    "finding": "MB045",
    "page": "149_scan071",
    "field": "deletion_insertion_review[1]",
    "before": "P02 / M1195: the live E_S is clear. Longer upright traces and a middle return allow an earlier F but do not establish its independent letter or cancellation state. The exact page encoding is \\unsure{E|\\deleted{F}E}_S, with the live-only/retraced reading first. M1195 resolves E alone; this state doubt is separate.",
    "after": "P02 / M1195: the live E component is visible. Longer upright traces and a middle return allow an earlier F but do not establish its independent letter or cancellation state. The exact page encoding is \\unsure{E|\\deleted{F}E}_S, with the live-only/retraced reading first. M1195 remains undecided for this full retracing/possible-earlier-F state, matching the current decision record.",
    "mode": "replace",
    "basis": "The sentence M1195 resolves E alone conflicts with the full-extent undecided decision now recorded for that supplied mark."
  },
  {
    "finding": "MB046",
    "page": "149_scan072",
    "field": "additional_diff_coverage[4].status",
    "before": "material; P07",
    "after": "nonmaterial; nonmaterial_observations P07 (ordinary/calligraphic U-wrapper mapping)",
    "mode": "replace",
    "basis": "The coverage status still labels P07 and P09 material although the current records place these rows in nonmaterial_observations."
  },
  {
    "finding": "MB046",
    "page": "149_scan072",
    "field": "additional_diff_coverage[5].status",
    "before": "material; P09",
    "after": "nonmaterial; nonmaterial_observations P09 (ordinary/calligraphic U-wrapper mapping)",
    "mode": "replace",
    "basis": "The coverage status still labels P07 and P09 material although the current records place these rows in nonmaterial_observations."
  },
  {
    "finding": "MB047",
    "page": "149_scan072",
    "field": "counts",
    "before": {
      "material_changes": 15,
      "against_C": 3,
      "against_H": 15,
      "nonmaterial_observations": 2,
      "crops": 11,
      "supplied_marks": 3,
      "resolved_supplied_marks": 3,
      "retained_doubts": 3,
      "audit_boxes": 11,
      "difference_rows": 12
    },
    "after": {
      "material_changes": 13,
      "against_C": 3,
      "against_H": 13,
      "nonmaterial_observations": 4,
      "crops": 11,
      "supplied_marks": 3,
      "resolved_supplied_marks": 3,
      "retained_doubts": 4,
      "audit_boxes": 11,
      "difference_rows": 12
    },
    "mode": "refresh_counts",
    "basis": "Stored counts predate the two U-wrapper rows moving to nonmaterial observations and the new audited ve doubt."
  },
  {
    "finding": "MB048",
    "page": "149_scan073",
    "field": "notes[3]",
    "before": "[S073.4; source oblique note] The NB note begins Le quotient de E_K and gives the written equality E_{\\underline O_x}=\\pi_1(\\operatorname{Spec}\\unsure{O_x|\\underline O_x}). The s. prefix and the I_x bar relation remain local reading doubts. No mathematical derivation is supplied by this transcription.",
    "after": "[S073.4; source oblique note] The NB note begins Le quotient de E_K and gives the written equality E_{\\underline O_x}=\\unsure{\\pi|\\Pi}_1(\\operatorname{Spec}\\unsure{O_x|\\underline O_x|\\underline U_x}). The s./s- prefix and the I_x bar relation also remain local reading doubts. No mathematical derivation is supplied by this transcription.",
    "mode": "replace",
    "basis": "The marginal-note summary still prints a settled pi and only two final O-decoration candidates, while the current equality includes pi/Pi and an underlined-U alternative."
  },
  {
    "finding": "MB048",
    "page": "149_scan073",
    "field": "notation[4].meaning",
    "before": "Equality written at the end of the source NB note. The first O underline is clear; the decoration of the final O remains uncertain.",
    "after": "Equality written at the end of the source NB note. The first O underline is clear; pi/Pi remains uncertain, and the final argument retains O_x, underlined O_x and underlined U_x alternatives, including both letter identity and decoration.",
    "mode": "replace",
    "basis": "The marginal-note summary still prints a settled pi and only two final O-decoration candidates, while the current equality includes pi/Pi and an underlined-U alternative."
  },
  {
    "finding": "MB049",
    "page": "149_scan073",
    "field": "abbreviations[6].written",
    "before": "\\unsure{s.}groupe",
    "after": "\\unsure{s.|s-}groupe",
    "mode": "replace",
    "basis": "The marginal prefix inventory retains only a tentative s. rather than the current s./s- alternatives."
  },
  {
    "finding": "MB049",
    "page": "149_scan073",
    "field": "abbreviations[6].expansion",
    "before": "sous-groupe; initial s. remains a reading doubt",
    "after": "sous-groupe (editorial expansion); the written initial prefix remains s./s- under uncertainty",
    "mode": "replace",
    "basis": "The marginal prefix inventory retains only a tentative s. rather than the current s./s- alternatives."
  },
  {
    "finding": "MB050",
    "page": "149_scan073",
    "field": "diff_coverage[22].reason",
    "before": "One live Les is followed by the attached canceled interlinear word, whose ending remains doubtful.",
    "after": "One Les, whose live, cancelled or underlined state remains open, is followed by the attached cancelled interlinear word, whose ending remains doubtful.",
    "mode": "replace",
    "basis": "The coverage row still calls Les definitely live; current text retains live/deleted/underlined state alternatives."
  },
  {
    "finding": "MB051",
    "page": "149_scan073",
    "field": "diff_coverage[24].reason",
    "before": "C eta and H K remain alternatives in one local nested-index doubt. The ordinary-U alphabet at this place is separately material in P10u.",
    "after": "The nested index retains eta/K/kappa alternatives. The ordinary-U wrapper observation at this place is documented in nonmaterial_observations P10u and contributes no material row.",
    "mode": "replace",
    "basis": "The row omits the current kappa index candidate and explicitly calls P10u material although P10u moved to nonmaterial_observations."
  },
  {
    "finding": "MB052",
    "page": "149_scan073",
    "field": "diff_coverage[31].reason",
    "before": "The crossed word remains one sur|dans cluster. Separate old/new word extents cannot be read securely.",
    "after": "The single cluster retains \\unsure{sur|dans|\\deleted{dan}\\unsure{s|\\deleted{s}}}. The possible cancelled dan and live/cancelled s state remain explicit alternatives; no secure sequence of two complete words or revision chronology is established.",
    "mode": "replace",
    "basis": "The preposition coverage row retains only sur/dans, omitting the newly encoded possible cancelled dan plus uncertain live/deleted s state."
  },
  {
    "finding": "MB053",
    "page": "149_scan075",
    "field": "hand[9].observation",
    "before": "The separate horizontal hyphen after finale precedes ment on the next line; preserve both the stroke and the division.",
    "after": "The separate horizontal hyphen after finale precedes the unresolved ment/vient group on the next line; preserve both the stroke and the division.",
    "mode": "replace",
    "basis": "The word-division observation still identifies the next-line letters as definite ment, whereas the current page keeps ment/vient uncertain."
  },
  {
    "finding": "MB054",
    "page": "149_scan075",
    "field": "additional_diff_coverage[2]",
    "before": {
      "place": "All nine U forms",
      "status": "material; P05, P06, P07, P08, P09, P19, P20, P24",
      "reason": "Each open U was inspected locally; H’s calligraphic alphabet is not imported globally."
    },
    "after": {
      "place": "All nine U forms",
      "status": "nonmaterial U-wrapper observations; nonmaterial_observations P07, P08, P09, P19, P24; companion glyph observations at P05, P06, P20",
      "reason": "Each open U remains locally documented. The handwriting/font-wrapper observations supply no material alphabet count. P05, P06 and P20 retain their independently recorded punctuation, wording or revision departures in changes."
    },
    "mode": "replace",
    "basis": "The all-nine-U coverage row still classifies the ordinary/calligraphic wrapper observations as material and includes P07/P08/P09/P19/P24 that have moved to nonmaterial_observations."
  },
  {
    "finding": "MB055",
    "page": "149_scan075",
    "field": "counts",
    "before": {
      "material_place_rows": 26,
      "against_C": 5,
      "against_H": 25,
      "saved_crops": 29,
      "audit_boxes": 26,
      "supplied_marks": 2,
      "resolved_supplied_marks": 1,
      "unresolved_supplied_marks": 1,
      "local_doubt_entries": 9,
      "nonmaterial_observations": 6,
      "supplied_difference_rows": 31,
      "actual_mathematical_check_events": 0,
      "counting_basis": "One material row per physical cropped place, with adjacent departures in that place listed explicitly. New certainty-only observations and same-ink macro wrappers are excluded."
    },
    "after": {
      "material_place_rows": 23,
      "against_C": 7,
      "against_H": 22,
      "saved_crops": 29,
      "audit_boxes": 27,
      "supplied_marks": 2,
      "resolved_supplied_marks": 1,
      "unresolved_supplied_marks": 1,
      "local_doubt_entries": 12,
      "nonmaterial_observations": 10,
      "supplied_difference_rows": 31,
      "actual_mathematical_check_events": 0,
      "counting_basis": "One material row per physical cropped place, with adjacent departures in that place listed explicitly. New certainty-only observations and same-ink macro wrappers are excluded.",
      "saved_crops_scope": "Historical first-pass total from the viewed P01-P29 crop list; excludes the separately recorded additional root crop R30 and all blind second crops.",
      "additional_root_crops": [
        {
          "id": "R30",
          "crop": "crops/149_scan075_R30.png"
        }
      ],
      "additional_root_crop_count": 1
    },
    "mode": "refresh_counts",
    "basis": "Stored counts predate moved wrapper rows, audit additions and the recovered line-break record."
  },
  {
    "finding": "MB056",
    "page": "149_scan075",
    "field": "notation[6].meaning",
    "before": "The expression explicitly written after la conclusion est que.",
    "after": "The expression written after la conclusion, tentative est, and que.",
    "mode": "replace",
    "basis": "The source-location phrase quotes la conclusion est que without the current local uncertainty on est."
  },
  {
    "finding": "MB057",
    "page": "149_scan076",
    "field": "notes[0]",
    "before": "Source setup, first paragraph: the author writes T subset X, calls it a sous schéma, fini étale sur S, writes T ≃ I_S and U=X\\setminus T, and describes the written family (g_i) of disjoint sections. The raised qualification names g as genre relatif, writes nu=card I and the pair condition (g,nu)≠(0,1). These are statements transcribed from the page.",
    "after": "Source setup, first paragraph: the author writes T subset X, calls it sous schém\\unsure{a|.}, fini étale sur S, writes T ≃ I_S and U=X\\setminus T, and describes the written family (g_i) of disjoint sections. The raised qualification names g as genre relatif, writes nu=card I and the pair condition (g,nu)≠(0,1). These are statements transcribed from the page.",
    "mode": "replace",
    "basis": "The opening description still quotes definite sous schéma, although the terminal a/abbreviation-stop distinction is now locally uncertain."
  },
  {
    "finding": "MB057",
    "page": "149_scan076",
    "field": "notation[0].meaning",
    "before": "The written opening setup calls T a sous schéma, fini étale sur S and I an ensemble fini.",
    "after": "The written opening setup calls T sous schém\\unsure{a|.}, fini étale sur S and I an ensemble fini.",
    "mode": "replace",
    "basis": "The opening description still quotes definite sous schéma, although the terminal a/abbreviation-stop distinction is now locally uncertain."
  },
  {
    "finding": "MB058",
    "page": "149_scan076",
    "field": "notes[9]",
    "before": "No OCR, image-to-text service, external research, TeX compilation, another-page inspection or blind-pass reading was used.",
    "after": "First-pass page-reader workflow attestation: No OCR, image-to-text service, external research, TeX compilation, another-page inspection or blind-pass reading was used. This attestation describes that first-pass stage; the subsequent independent audit and root cross-page comparisons remain recorded separately.",
    "mode": "replace",
    "basis": "The unqualified workflow statement says no blind-pass reading or other-page inspection was used, while current metadata records the completed independent audit and explicit cross-page letter-form comparisons."
  },
  {
    "finding": "MB059",
    "page": "149_scan076",
    "field": "diff_coverage[20].reason",
    "before": "H linearizes the added lower-right node and begins an editorial note in this token span. Source diagram placement is retained; pour comma, canceled tout and ell=nb are handled at their own crops.",
    "after": "H linearizes the added lower-right node and begins an editorial note in this token span. Source diagram placement is retained; pour comma, tentative cancelled tout and ell followed by the uncertain equals/colon-equals mark before nb are handled at their own crops.",
    "mode": "replace",
    "basis": "The alignment-row summary still gives ell=nb as a fixed equality, while the current local mark is equals/colon-equals."
  }
]
''')


class GuardError(RuntimeError):
    """A changed input or unsupported edit requires root review."""


def utc_now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def json_bytes(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def value_signature(value):
    # JSON types remain distinct (for example, true versus 1).
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def same_value(left, right):
    return value_signature(left) == value_signature(right)


def path_parts(field):
    if not re.fullmatch(r"[A-Za-z_]\w*(?:\[\d+\]|\.[A-Za-z_]\w*)*", field):
        raise GuardError(f"Unsupported field path: {field}")
    return [
        key if key else int(index)
        for key, index in re.findall(r"([A-Za-z_]\w*)|\[(\d+)\]", field)
    ]


def get_field(document, field):
    value = document
    try:
        for part in path_parts(field):
            value = value[part]
    except (KeyError, IndexError, TypeError) as exc:
        raise GuardError(f"Missing or structurally changed field: {field}") from exc
    return value


def set_field(document, field, value):
    parts = path_parts(field)
    parent = document
    for part in parts[:-1]:
        parent = parent[part]
    parent[parts[-1]] = copy.deepcopy(value)


def strings_in(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, list):
        for child in value:
            yield from strings_in(child)
    elif isinstance(value, dict):
        for child in value.values():
            yield from strings_in(child)


def first_pass_crop_references(document, page):
    pattern = re.compile(rf"crops/{re.escape(page)}_P\d+\.png")
    refs = {
        value for value in document.get("viewed", [])
        if isinstance(value, str) and pattern.fullmatch(value)
    }
    if not refs:
        raise GuardError(f"{page}: no first-pass crop references in viewed")
    return sorted(refs)


def additional_root_crops(document, page):
    if page != "149_scan075":
        return []
    rows = [row for row in document["changes"] if row["id"] == "R30"]
    expected_crop = "crops/149_scan075_R30.png"
    if len(rows) != 1 or rows[0].get("crop") != expected_crop:
        raise GuardError("scan075: the separately recorded R30 crop reference changed")
    return [{"id": "R30", "crop": expected_crop}]


def refresh_counts(document, page):
    changes = document["changes"]
    decisions = document["decisions"]
    if [row["id"] for row in decisions] != document["supplied_mark_ids"]:
        raise GuardError(f"{page}: decision order differs from supplied mark IDs")
    for row in changes:
        for key in ("against_C", "against_H"):
            if not isinstance(row.get(key), bool):
                raise GuardError(f"{page}: non-boolean material flag {row.get('id')}.{key}")
    resolved = sum(row["decision"] != "undecided" for row in decisions)
    undecided = len(decisions) - resolved
    fresh = copy.deepcopy(document["counts"])
    common = {
        "against_C": sum(row["against_C"] for row in changes),
        "against_H": sum(row["against_H"] for row in changes),
        "nonmaterial_observations": len(document["nonmaterial_observations"]),
        "supplied_marks": len(decisions),
        "resolved_supplied_marks": resolved,
        "audit_boxes": len(document["audit_boxes"]),
    }
    fresh.update(common)
    if page == "149_scan072":
        fresh.update({
            "material_changes": len(changes),
            "crops": len(first_pass_crop_references(document, page)),
            "retained_doubts": len(document["doubts"]),
            "difference_rows": len(document["diff_coverage"]),
        })
    elif page == "149_scan075":
        fresh.update({
            "material_place_rows": len(changes),
            "saved_crops": len(first_pass_crop_references(document, page)),
            "unresolved_supplied_marks": undecided,
            "local_doubt_entries": len(document["doubts"]),
            "supplied_difference_rows": len(document["diff_coverage"]),
            "actual_mathematical_check_events": len(document["check_events"]),
        })
        # Preserve the original declared counting basis verbatim.
        if fresh["saved_crops"] != 29:
            raise GuardError("scan075: the historical first-pass crop count changed")
        fresh["saved_crops_scope"] = HISTORICAL_CROP_SCOPE
        fresh["additional_root_crops"] = additional_root_crops(document, page)
        fresh["additional_root_crop_count"] = len(fresh["additional_root_crops"])
    else:
        raise GuardError(f"Count refresh is not authorized for {page}")
    added_keys = (
        {"saved_crops_scope", "additional_root_crops", "additional_root_crop_count"}
        if page == "149_scan075" else set()
    )
    if set(fresh) != set(document["counts"]) | added_keys:
        raise GuardError(f"{page}: count refresh changed the declared count schema")
    return fresh


def validate_declared_plan():
    if REPORT.is_symlink() or sha256(REPORT.read_bytes()) != REPORT_SHA256:
        raise GuardError("The source findings report changed or is a symlink")
    report = json.loads(REPORT.read_text(encoding="utf-8"))
    declared = {}
    for finding in report["findings"]:
        for entry in finding["current_metadata"]:
            key = (finding["id"], finding["page"], entry["field"])
            declared[key] = entry["current_text"]
    plan_keys = [(x["finding"], x["page"], x["field"]) for x in PLAN]
    if len(plan_keys) != len(set(plan_keys)):
        raise GuardError("Duplicate finding/page/field in the explicit plan")
    if set(plan_keys) != set(declared):
        raise GuardError("The explicit plan does not cover the report exactly")
    if len({x["finding"] for x in PLAN}) != 59 or len(PLAN) != 102:
        raise GuardError("Unexpected finding or field-replacement count")
    for edit in PLAN:
        key = (edit["finding"], edit["page"], edit["field"])
        if not same_value(edit["before"], declared[key]):
            raise GuardError(f"Before-value differs from report: {key}")
        if edit["page"] not in SCOPE:
            raise GuardError(f"Out-of-scope review: {edit['page']}")
        top = path_parts(edit["field"])[0]
        if top not in MUTABLE_METADATA or top in PROTECTED_REVIEW_FIELDS:
            raise GuardError(f"Protected metadata field: {edit['field']}")
        if top == "changes" and not (
            edit["page"] == "149_scan071"
            and edit["field"] == "changes[6].evidence"
            and edit["finding"] == "MB042"
        ):
            raise GuardError("Only the declared P09 descriptive evidence may change")
        if top == "nonmaterial_observations":
            before, after = edit["before"], edit["after"]
            if edit["finding"] != "MB030" or edit["page"] != "149_scan064":
                raise GuardError("Undeclared nonmaterial observation edit")
            if before.get("id") not in {"P05", "P23", "P25"}:
                raise GuardError("Unexpected excluded row identity")
            if not before.get("exclusion_reason"):
                raise GuardError("Excluded flags lack the prior explicit rationale")
            unchanged = copy.deepcopy(after)
            for flag in ("against_C", "against_H"):
                if after[flag] is not False:
                    raise GuardError("Excluded flags must both be false")
                unchanged[flag] = before[flag]
            if not same_value(unchanged, before):
                raise GuardError("The excluded-row edit changes more than its flags")
        if top == "counts" and edit["mode"] != "refresh_counts":
            raise GuardError("Counts must be refreshed from current records")
        if any(re.search(r"\b20\d{2}-\d{2}-\d{2}\b", s)
               for s in strings_in(edit["before"])):
            raise GuardError("A dated historical value requires separate root review")
        if edit["finding"] == "MB058":
            if edit["before"] not in edit["after"]:
                raise GuardError("The first-pass attestation must remain verbatim")


def validate_current_references(document, edit, after):
    nonmaterial = {row["id"] for row in document.get("nonmaterial_observations", [])}
    material = {row["id"] for row in document.get("changes", [])}
    for text in strings_in(after):
        for match in re.finditer(r"nonmaterial_observations ([^.;]+)", text):
            for row_id in re.findall(r"\bP\d+[a-z]?\b", match.group(1)):
                if row_id not in nonmaterial:
                    raise GuardError(
                        f"{edit['page']}: named nonmaterial row {row_id} is absent"
                    )
    status = after if edit["field"].endswith(".status") else (
        after.get("status") if isinstance(after, dict) else None
    )
    if isinstance(status, str):
        match = re.match(r"material; ([^;]+)", status)
        if match:
            for row_id in re.findall(r"\bP\d+[a-z]?\b", match.group(1)):
                if row_id not in material:
                    raise GuardError(
                        f"{edit['page']}: named material row {row_id} is absent"
                    )
    if edit["field"] == "changes[6].evidence":
        if document["changes"][6]["id"] != "P09":
            raise GuardError("The guarded scan071 change row is no longer P09")


def protected_file_hashes():
    # Hash bytes only. No page or frozen reading is interpreted or transformed.
    result = {}
    for page in SCOPE:
        path = BASE / "pages" / f"{page}.tex"
        if not path.is_file() or path.is_symlink():
            raise GuardError(f"Expected regular page file: {path}")
        result[str(path.relative_to(BASE))] = sha256(path.read_bytes())
    second = BASE / "second"
    if not second.is_dir() or second.is_symlink():
        raise GuardError("Expected regular second-pass directory")
    for path in second.rglob("*"):
        if not any(path.name.startswith(page + "_") for page in SCOPE):
            continue
        if path.is_symlink():
            raise GuardError(f"Frozen input/return is a symlink: {path}")
        if path.is_file():
            result[str(path.relative_to(BASE))] = sha256(path.read_bytes())
    return result


def preflight():
    validate_declared_plan()
    if REVIEWS.is_symlink():
        raise GuardError("The reviews directory must not be a symlink")
    originals, updated, raw_before = {}, {}, {}
    pages = sorted({edit["page"] for edit in PLAN})
    for page in pages:
        path = REVIEWS / f"{page}.json"
        if not path.is_file() or path.is_symlink():
            raise GuardError(f"Expected regular review: {path}")
        raw_before[page] = path.read_bytes()
        originals[page] = json.loads(raw_before[page].decode("utf-8"))
        updated[page] = copy.deepcopy(originals[page])
    effective = []
    errors = []
    for edit in PLAN:
        document = originals[edit["page"]]
        actual = get_field(document, edit["field"])
        if not same_value(actual, edit["before"]):
            errors.append(
                f"{edit['finding']} {edit['page']}.{edit['field']}: "
                "current value differs from the explicit before-value"
            )
            continue
        after = (
            refresh_counts(document, edit["page"])
            if edit["mode"] == "refresh_counts"
            else copy.deepcopy(edit["after"])
        )
        validate_current_references(document, edit, after)
        current_edit = copy.deepcopy(edit)
        current_edit["reviewed_preview_after"] = current_edit["after"]
        current_edit["after"] = after
        effective.append(current_edit)
        set_field(updated[edit["page"]], edit["field"], after)
    if errors:
        raise GuardError("No reviews written. Guard mismatches:\n" + "\n".join(errors))
    for page in pages:
        for field in PROTECTED_REVIEW_FIELDS:
            if not same_value(originals[page].get(field), updated[page].get(field)):
                raise GuardError(f"{page}: protected review field changed: {field}")
        for field in set(originals[page]) - MUTABLE_METADATA:
            if not same_value(originals[page][field], updated[page][field]):
                raise GuardError(f"{page}: undeclared top-level change: {field}")
    serialized = {page: json_bytes(updated[page]) for page in pages}
    preserved = protected_file_hashes()
    return raw_before, serialized, effective, preserved


def make_temp(path, payload):
    descriptor, name = tempfile.mkstemp(
        prefix=f".{path.name}.metadata_b.", suffix=".tmp", dir=path.parent
    )
    temporary = Path(name)
    try:
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(payload)
            stream.flush()
            os.fsync(stream.fileno())
        if path.exists():
            os.chmod(temporary, path.stat().st_mode & 0o777)
        return temporary
    except BaseException:
        temporary.unlink(missing_ok=True)
        raise


def write_journal(journal, first=False):
    payload = json_bytes(journal)
    if first:
        # Exclusive creation prevents an earlier completion record being erased.
        with JOURNAL.open("xb") as stream:
            stream.write(payload)
            stream.flush()
            os.fsync(stream.fileno())
        return
    temporary = make_temp(JOURNAL, payload)
    try:
        os.replace(temporary, JOURNAL)
    finally:
        temporary.unlink(missing_ok=True)


def apply_plan(raw_before, serialized, effective, preserved):
    if JOURNAL.exists() or JOURNAL.is_symlink():
        raise GuardError(f"Existing journal requires root review: {JOURNAL}")
    pages = sorted(serialized)
    journal = {
        "script": str(Path(__file__).resolve()),
        "script_sha256": sha256(Path(__file__).read_bytes()),
        "source_report": str(REPORT),
        "source_report_sha256": REPORT_SHA256,
        "started_utc": utc_now(),
        "completed_utc": None,
        "status": "prepared",
        "root_scope_decision": ROOT_SCOPE_DECISION,
        "protected_files_before": preserved,
        "pages": {
            page: {
                "path": str(REVIEWS / f"{page}.json"),
                "before_sha256": sha256(raw_before[page]),
                "after_sha256": sha256(serialized[page]),
                "written_utc": None,
            } for page in pages
        },
        "edits": [
            {**edit, "applied_utc": None}
            for edit in effective
        ],
    }
    staged, committed = {}, []
    write_journal(journal, first=True)
    try:
        for page in pages:
            path = REVIEWS / f"{page}.json"
            if path.read_bytes() != raw_before[page]:
                raise GuardError(f"{page}: review changed after preflight")
            staged[page] = make_temp(path, serialized[page])
        if protected_file_hashes() != preserved:
            raise GuardError("A protected page or frozen file changed before commit")
        # Recheck every review immediately before beginning the commit sequence.
        for page in pages:
            if (REVIEWS / f"{page}.json").read_bytes() != raw_before[page]:
                raise GuardError(f"{page}: review changed while staging")
        journal["status"] = "committing"
        write_journal(journal)
        for page in pages:
            path = REVIEWS / f"{page}.json"
            if path.read_bytes() != raw_before[page]:
                raise GuardError(f"{page}: review changed before its replacement")
            os.replace(staged[page], path)
            committed.append(page)
            when = utc_now()
            journal["pages"][page]["written_utc"] = when
            for edit in journal["edits"]:
                if edit["page"] == page:
                    edit["applied_utc"] = when
            write_journal(journal)
        for page in pages:
            if (REVIEWS / f"{page}.json").read_bytes() != serialized[page]:
                raise GuardError(f"{page}: post-write byte verification failed")
        preserved_after = protected_file_hashes()
        if preserved_after != preserved:
            raise GuardError("Protected page/frozen-file verification failed")
        journal["protected_files_after"] = preserved_after
        journal["status"] = "complete"
        journal["completed_utc"] = utc_now()
        write_journal(journal)
    except BaseException as exc:
        journal["status"] = "failed_partial" if committed else "aborted_before_commit"
        journal["failed_utc"] = utc_now()
        journal["error"] = f"{type(exc).__name__}: {exc}"
        journal["committed_pages"] = committed
        try:
            write_journal(journal)
        except BaseException:
            pass
        # No automatic rollback: the journal retains exact values for root review.
        raise
    finally:
        for temporary in staged.values():
            temporary.unlink(missing_ok=True)
    return journal


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--apply", action="store_true",
        help="Write the guarded current metadata edits and completion journal.",
    )
    args = parser.parse_args()
    raw_before, serialized, effective, preserved = preflight()
    summary = {
        "mode": "apply" if args.apply else "read-only preflight",
        "finding_count": len({x["finding"] for x in effective}),
        "field_replacements": len(effective),
        "review_files": sorted(serialized),
        "root_scope_decision": ROOT_SCOPE_DECISION,
        "count_blocks": {
            x["page"]: x["after"] for x in effective if x["field"] == "counts"
        },
        "journal": str(JOURNAL) if args.apply else None,
    }
    if args.apply:
        journal = apply_plan(
            raw_before, serialized, effective, preserved
        )
        summary["status"] = journal["status"]
        summary["completed_utc"] = journal["completed_utc"]
    else:
        summary["status"] = "all explicit guards passed; no files written"
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (GuardError, OSError, ValueError, KeyError, TypeError) as error:
        print(f"Reconciliation stopped: {error}", file=sys.stderr)
        raise SystemExit(1)

