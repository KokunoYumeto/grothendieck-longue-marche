#!/usr/bin/env python3
"""Unexecuted documentation-only cleanup proposal for audited scans 079–095.

Prepared from canonical reviewed records, final pages and completed adjudications.
No images were reread, no mathematical checks were conducted, and no source,
reading, check-event or adjudication file is changed by this proposal itself.

Default execution validates and prints the proposed changes without writing.
Only an explicit --apply writes the four permitted explanatory fields in the
canonical JSON files. Root review is required before applying this proposal.
All exact preconditions are validated before any write; drift aborts the batch.
The frozen first readings and adjudications retain the historical observations.
"""
from __future__ import annotations

import argparse
import copy
import json
import os
from pathlib import Path
import tempfile

WORK_ROOT = Path(__file__).resolve().parents[1]
ALLOWED_FIELDS = {"notes", "hand_observations", "notation_additions", "inventory"}

PATCHES = [{'scan': 79,
  'path': ['notes'],
  'operation': 'replace_once',
  'before': 'appends il faudrait quand même les vérifier ! to the marginal claims.',
  'after': 'appends il faudrait quand même les/le vérifier ! to the marginal claims, with the article '
           'explicitly doubtful.',
  'source': 'second/149_scan079_adjudications.tsv: B015'},
 {'scan': 79,
  'path': ['notes'],
  'operation': 'replace_once',
  'before': 'Visual attachment and state checks are kept in notes; check_events contains mathematical checks '
            'and the author’s mathematical caution only.',
  'after': 'Visual attachment and state checks and the author’s mathematical cautions are kept in notes. The '
           'recorded check_events entry is the separate targeted proof check 079-N1.',
  'source': 'review/149_scan079_reviewed.json: check_events (079-N1); operative PROMPT: CHECK_EVENTS scope'},
 {'scan': 79,
  'path': ['inventory', 2, 'first_words_or_objects'],
  'operation': 'set',
  'before': 'kappa_i0: T → pi_1(U_eta); T_infinity(k) beneath T with vertical equality',
  'after': 'kappa/k_i0: T → pi_1(U_eta/k); T_infinity(k) beneath T with vertical equality; both local letter '
           'choices remain doubtful',
  'source': 'second/149_scan079_adjudications.tsv: B002'},
 {'scan': 79,
  'path': ['inventory', 13, 'first_words_or_objects'],
  'operation': 'set',
  'before': 'il faudrait quand même les vérifier !',
  'after': 'il faudrait quand même les|le vérifier ! (article doubtful)',
  'source': 'second/149_scan079_adjudications.tsv: B015'},
 {'scan': 80,
  'path': ['notes'],
  'operation': 'replace_once',
  'before': 'The nested C doubts in deleted de and car. were not listed among the supplied M1220-M1222 '
            'marks; both remain unresolved and are explicitly listed below.',
  'after': 'The nested C doubts in deleted de and car were not listed among the supplied M1220-M1222 marks; '
           'both remain unresolved. The final stop after car is live and outside the cancellation.',
  'source': 'second/149_scan080_adjudications.tsv: B011'},
 {'scan': 80,
  'path': ['hand_observations', 0, 'habit'],
  'operation': 'set',
  'before': 'Small right-arrow heads can be one-sided terminal hooks rather than full chevrons.',
  'after': 'A tiny terminal hook may be an arrowhead or a pen return; each connector requires its own '
           'decision.',
  'source': 'second/149_scan080_adjudications.tsv: B005, B009, B010'},
 {'scan': 80,
  'path': ['hand_observations', 0, 'evidence'],
  'operation': 'set',
  'before': 'In (13) the first two heads are compact turns, comparable to the clearly directed first two '
            'connectors in (16). The first connector of (17) is weaker and remains doubtful rather than '
            'being generalized.',
  'after': 'Final adjudication retains arrow/shaft doubt at the first connector of (13) and the second '
           'connector of (16). The first connector of (16) remains headed; the first connector of (17) '
           'prefers a plain shaft with an arrow alternative.',
  'source': 'second/149_scan080_adjudications.tsv: B005, B009, B010'},
 {'scan': 80,
  'path': ['hand_observations', 0, 'witness_errors'],
  'operation': 'set',
  'before': 'C gives plain dashes for the first two connectors of (16); these have visible directed turns. '
            'The (17) case remains open.',
  'after': 'C gives shafts for the first two connectors of (16). The first is read as an arrow, while the '
           'second remains explicitly doubtful. The earlier first-pass claim that both heads were secure is '
           'superseded.',
  'source': 'second/149_scan080_adjudications.tsv: B005, B009, B010'},
 {'scan': 80,
  'path': ['inventory', 1, 'first_words_or_objects'],
  'operation': 'set',
  'before': '(13) 1 -> T -> N(L_i) -> E_S -> 1',
  'after': '(13) 1 [arrow|shaft] T -> N(L_i) -> E_S -> 1; first connector doubtful, arrow preferred',
  'source': 'second/149_scan080_adjudications.tsv: B005'},
 {'scan': 80,
  'path': ['inventory', 8, 'first_words_or_objects'],
  'operation': 'set',
  'before': '(16) 0 -> Pic(S)_n -> H^2(S,mu_n) -> _n H^2(S,G_m) -> 0',
  'after': '(16) 0 -> Pic(S)_n [arrow|shaft] H^2(S,mu_n) -> _n H^2(S,G_m) -> 0; second connector doubtful, '
           'arrow preferred',
  'source': 'second/149_scan080_adjudications.tsv: B009'},
 {'scan': 80,
  'path': ['inventory', 10, 'first_words_or_objects'],
  'operation': 'set',
  'before': '(17) 0 -> Pic(S)^wedge -> H^2(S,T) -> lim _n H^2(S,G_m); lower lim(Pic_n=Pic/nPic)',
  'after': '(17) 0 [shaft|arrow] Pic(S)^wedge -> H^2(S,T) -> lim _n H^2(S,G_m); lower lim(Pic_n=Pic/nPic); '
           'first connector doubtful, shaft preferred',
  'source': 'second/149_scan080_adjudications.tsv: B010'},
 {'scan': 80,
  'path': ['inventory', 11, 'first_words_or_objects'],
  'operation': 'set',
  'before': 'Dans le cas où S est un schéma élémentaire sur un corps de',
  'after': 'Dans le cas où S est un schéma. élémentaire sur un corps de',
  'source': 'second/149_scan080_adjudications.tsv: B011'},
 {'scan': 80,
  'path': ['inventory', 12, 'first_words_or_objects'],
  'operation': 'set',
  'before': 'car. (doubtful)',
  'after': 'car (doubtful), followed by a separate live stop',
  'source': 'second/149_scan080_adjudications.tsv: B011'},
 {'scan': 81,
  'path': ['notes'],
  'operation': 'replace_once',
  'before': 'The four struck words pour, de, le, Spec remain doubtful because their covered letters cannot '
            'all be resolved.',
  'after': 'After blind adjudication, the struck words groupe, pour, de, le, schéma and Spec remain doubtful '
           'because their covered letters cannot all be resolved.',
  'source': 'second/149_scan081_adjudications.tsv: B002, B014'},
 {'scan': 81,
  'path': ['inventory', 2, 'first_words_or_objects'],
  'operation': 'set',
  'before': 'groupe',
  'after': 'groupe (doubt retained)',
  'source': 'second/149_scan081_adjudications.tsv: B002'},
 {'scan': 81,
  'path': ['inventory', 14, 'first_words_or_objects'],
  'operation': 'set',
  'before': 'schéma',
  'after': 'schéma (doubt retained)',
  'source': 'second/149_scan081_adjudications.tsv: B014'},
 {'scan': 82,
  'path': ['notes'],
  'operation': 'replace_once',
  'before': "These are the page's statements, not independent proofs checked by this reader; check_events is "
            'therefore empty.',
  'after': "These are the page's statements. The first reader performed no independent mathematical check; "
           'the later conditional calculation 082-N1 is recorded separately below and in check_events.',
  'source': 'review/149_scan082_reviewed.json: check_events (082-N1) and appended root-check paragraph'},
 {'scan': 82,
  'path': ['notes'],
  'operation': 'replace_once',
  'before': 'Gamma/xi has extra retraced strokes here, so prior notation does not force a certain reading; '
            "si l'on is also compressed and left doubtful.",
  'after': 'The first class-equals-zero formula has extra retraced strokes and retains gamma/xi doubt; the '
           "later Quand gamma_i=0 is resolved separately by blind adjudication. Si l'on is also compressed "
           'and left doubtful.',
  'source': 'second/149_scan082_adjudications.tsv: B004, B008'},
 {'scan': 82,
  'path': ['notes'],
  'operation': 'replace_once',
  'before': 'Cancelled H^0(S)_n stays doubtful, but the cancelled (21) number has distinguishable digits.',
  'after': 'Cancelled H^0(S)_n stays doubtful. The cancelled label is preferably (21), but parts of its '
           'digits remain covered by hatching, so that label also retains explicit doubt.',
  'source': 'second/149_scan082_adjudications.tsv: B015, B016'},
 {'scan': 82,
  'path': ['inventory', 7, 'first_words_or_objects'],
  'operation': 'set',
  'before': 'cancelled (21), 0 arrow cancelled H^0(S)_n G_m(S)_n',
  'after': 'cancelled doubtful (21), 0 arrow cancelled doubtful H^0(S)_n followed by live G_m(S)_n',
  'source': 'second/149_scan082_adjudications.tsv: B015, B016'},
 {'scan': 82,
  'path': ['inventory', 8, 'first_words_or_objects'],
  'operation': 'set',
  'before': '(21)',
  'after': '(21) (doubt retained)',
  'source': 'second/149_scan082_adjudications.tsv: B015, B016'},
 {'scan': 82,
  'path': ['inventory', 13, 'first_words_or_objects'],
  'operation': 'set',
  'before': 'cancelled G_m; H^1(S,T) congruent G_m(S)^hat',
  'after': 'cancelled doubtful G_m; H^1(S,T) congruent G_m(S)^hat',
  'source': 'second/149_scan082_adjudications.tsv: B021'},
 {'scan': 82,
  'path': ['inventory', 14, 'first_words_or_objects'],
  'operation': 'set',
  'before': 'G_m',
  'after': 'G_m (doubt retained)',
  'source': 'second/149_scan082_adjudications.tsv: B021'},
 {'scan': 83,
  'path': ['notes'],
  'operation': 'replace_once',
  'before': 'The two deletions are the digit after live 2 and the phrase ce qui donne/devra; both retain '
            'doubts where the underlying strokes are obscured.',
  'after': 'The two deletions are the digit after live 2 and the phrase ce/et qui donne/devra/leur; both '
           'retain the local doubts established by adjudication where the underlying strokes are obscured.',
  'source': 'second/149_scan083_adjudications.tsv: B005, B011'},
 {'scan': 83,
  'path': ['inventory', 7, 'first_words_or_objects'],
  'operation': 'set',
  'before': 'ce qui donne|devra',
  'after': 'ce|et qui donne|devra|leur (cancelled and doubtful)',
  'source': 'second/149_scan083_adjudications.tsv: B011'},
 {'scan': 83,
  'path': ['inventory', 10, 'first_words_or_objects'],
  'operation': 'set',
  'before': 'et considérons son stabilisateur N_x dans le E_K ...',
  'after': 'et considérons son stabilisateur N_x dans le|E E_K ... (le/E doubtful)',
  'source': 'second/149_scan083_adjudications.tsv: B013'},
 {'scan': 84,
  'path': ['inventory', 1, 'first_words_or_objects'],
  'operation': 'set',
  'before': '1 – I_x-tilde → N_x-tilde → Gal(overline k(x)/k(x)) → 1',
  'after': '1 – I_x-tilde → N_x-tilde → Gal(overline k(x|dotted x)/k(x)) → 1; numerator x/dotted-x doubtful',
  'source': 'second/149_scan084_adjudications.tsv: B006'},
 {'scan': 84,
  'path': ['inventory', 9, 'first_words_or_objects'],
  'operation': 'set',
  'before': 'Soit donc U_underlined O_x',
  'after': 'Soit donc|sur U_underlined O_x (donc/sur doubtful)',
  'source': 'second/149_scan084_adjudications.tsv: B014'},
 {'scan': 85,
  'path': ['notes'],
  'operation': 'replace_once',
  'before': 'Author page 42 has 19 main baseline rows including display (22),',
  'after': 'Author page 42 has 19 main baseline rows including a display labelled (22)|(21),',
  'source': 'second/149_scan085_adjudications.tsv: B003'},
 {'scan': 85,
  'path': ['notes'],
  'operation': 'replace_once',
  'before': "These are the manuscript's assertions; this reader made no independent mathematical proof, "
            'use-check or computation, so check_events is empty.',
  'after': "These are the manuscript's assertions. The first reader made no independent mathematical proof, "
           'use-check or computation; the later formal injectivity check 085-N1 is recorded separately below '
           'and in check_events.',
  'source': 'review/149_scan085_reviewed.json: check_events (085-N1) and appended root-check paragraph'},
 {'scan': 85,
  'path': ['notes'],
  'operation': 'replace_once',
  'before': 'The cancelled terminal s and H^1(S,T) remain doubtful.',
  'after': 'The cancelled terminal s and H^1(S,T) remain doubtful. A cancelled relation immediately after '
           'H^1(S,T), recovered in blind adjudication, also remains doubtful between equals and isomorphism.',
  'source': 'second/149_scan085_adjudications.tsv: B009'},
 {'scan': 85,
  'path': ['inventory', 3, 'first_words_or_objects'],
  'operation': 'set',
  'before': '(22) G_m(S) arrow G_m(S)^hat congruent H^1(S,T)',
  'after': '(22)|(21) G_m(S) arrow G_m(S)^hat congruent H^1(S,T); label doubtful',
  'source': 'second/149_scan085_adjudications.tsv: B003'},
 {'scan': 85,
  'path': ['inventory', 7, 'first_words_or_objects'],
  'operation': 'set',
  'before': 'H^1(S,T) (doubt retained)',
  'after': 'H^1(S,T) followed by =|simeq, all cancelled with local doubts',
  'source': 'second/149_scan085_adjudications.tsv: B009'},
 {'scan': 86,
  'path': ['notes'],
  'operation': 'replace_once',
  'before': 'The composite E_K to E_{U_eta} to E_U is written on the same baseline as le composé and is not '
            'a separate manuscript display.',
  'after': 'The composite E_K to E_{U_K} to E_U is written on the same baseline as le composé and is not a '
           'separate manuscript display. The nested index is K after completed adjudication.',
  'source': 'second/149_scan086_adjudications.tsv: B008'},
 {'scan': 86,
  'path': ['notes'],
  'operation': 'replace_once',
  'before': 'The first opening relation has two very short faint horizontal bars with dark right ends, so '
            'its colon-like appearance is retained as an equals sign; the set-difference slash is oblique.',
  'after': 'The opening relation has two very short faint horizontal bars with dark right ends; equals is '
           'preferred, with colon retained as an explicit alternative. The set-difference slash is oblique.',
  'source': 'second/149_scan086_adjudications.tsv: B001'},
 {'scan': 86,
  'path': ['inventory', 0, 'first_words_or_objects'],
  'operation': 'set',
  'before': 'la sempiternelle situation de U=X\\T ... section de X',
  'after': 'la sempiternelle situation de U [=|:] X\\T ... section de X; opening relation doubtful',
  'source': 'second/149_scan086_adjudications.tsv: B001'},
 {'scan': 86,
  'path': ['inventory', 6, 'first_words_or_objects'],
  'operation': 'set',
  'before': 'E_K -> E_{U_eta} - E_U',
  'after': 'E_K -> E_{U_K} - E_U',
  'source': 'second/149_scan086_adjudications.tsv: B008'},
 {'scan': 86,
  'path': ['inventory', 7, 'first_words_or_objects'],
  'operation': 'set',
  'before': "(qui envoie en fait I_s' dans pi, et barred m dans les L_i, on l'a vu)",
  'after': "(qui envoie en fait I_s' dans pi, et = dans les L_i, on l'a vu)",
  'source': 'second/149_scan086_adjudications.tsv: B009'},
 {'scan': 87,
  'path': ['notes'],
  'operation': 'replace_once',
  'before': 'Root accepted the vertical isomorphism sign at medium confidence as a decided reading to be '
            'independently audited.',
  'after': 'First-pass root review accepted the vertical isomorphism sign at medium confidence; completed '
           'blind adjudication B016 retained that reading and its orientation.',
  'source': 'second/149_scan087_adjudications.tsv: B016'},
 {'scan': 87,
  'path': ['notes'],
  'operation': 'replace_once',
  'before': 'The left marginal note is wholly cancelled by repeated roughly vertical strokes and remains '
            'partially doubtful. Its three-line reading is retained tentatively; neither the tilde on K nor '
            'the complete wording is certified.',
  'after': 'The first two lines of the left marginal note are cancelled by repeated roughly vertical '
           'strokes. The detached last line reads tentatively à le s/à la s and has an explicitly doubtful '
           'cancellation state. The tilde on K and the obscured wording also remain uncertain.',
  'source': 'second/149_scan087_adjudications.tsv: B003'},
 {'scan': 87,
  'path': ['notes'],
  'operation': 'replace_once',
  'before': 'The cancelled Comme and the following struck interline are distinct physical passages.',
  'after': 'The cancelled Si on|Comme and the following struck interline are distinct physical passages.',
  'source': 'second/149_scan087_adjudications.tsv: B007'},
 {'scan': 87,
  'path': ['notes'],
  'operation': 'replace_once',
  'before': 'The local-symbol replacement is beneath the cancelled symbol. Adjacent curved strokes may be '
            'correction marks and do not warrant supplying a new pair of parentheses around the doubtful old '
            'Z.',
  'after': 'The local-symbol replacement is beneath the cancelled symbol. Adjudication admits enclosing '
           'curves and a small lower-right w/s in the old form, giving (tilde S)_w|(tilde S)_s|tilde Z. The '
           'replacement underlined O_s is clear, but its tilde remains doubtful because the upper trace '
           'overlaps the correction path.',
  'source': 'second/149_scan087_adjudications.tsv: B010'},
 {'scan': 87,
  'path': ['notes'],
  'operation': 'replace_once',
  'before': 'The inserted E is legible even though the resulting phrase et la E extension is syntactically '
            "awkward. The author's wording and insertion state are retained without repair.",
  'after': 'The inserted E is legible. The preceding article remains la|le, and the cancelled word remains '
           'suite|seule|sous. The resulting phrase is retained with these doubts and its insertion state, '
           'without grammatical repair.',
  'source': 'second/149_scan087_adjudications.tsv: B014'},
 {'scan': 87,
  'path': ['inventory', 2, 'first_words_or_objects'],
  'operation': 'set',
  'before': "c'est l'extension E_U...",
  'after': "cancelled first two lines: c'est l'extension E_U... correspondante|correspondant; detached à le "
           's|à la s has uncertain cancellation state',
  'source': 'second/149_scan087_adjudications.tsv: B003'},
 {'scan': 87,
  'path': ['inventory', 11, 'first_words_or_objects'],
  'operation': 'set',
  'before': "et la ... extension de ce groupe par π / n'est autre que",
  'after': 'et la|le ... E extension de ce groupe par π / n’est autre que; article and cancelled word '
           'doubtful',
  'source': 'second/149_scan087_adjudications.tsv: B014'},
 {'scan': 87,
  'path': ['inventory', 12, 'position'],
  'operation': 'set',
  'before': 'after et la',
  'after': 'after the doubtful article la|le',
  'source': 'second/149_scan087_adjudications.tsv: B014'},
 {'scan': 88,
  'path': ['notes'],
  'operation': 'replace_once',
  'before': 'The tiny barb on the top diagram map supports an arrow with medium confidence; the short maps '
            'in the prose and the local map T-pi retain their bare shafts.',
  'after': 'Completed adjudication reads the upper EU-to-E diagram link and the first three lower-row links '
           'as bare shafts. The prose kernel and composite links and the local map T-pi also retain bare '
           'shafts; the separately written prose map E_U-tildeK to E_tildeK retains its arrow.',
  'source': 'second/149_scan088_adjudications.tsv: B002, B005, B011, B014'},
 {'scan': 88,
  'path': ['notes'],
  'operation': 'replace_once',
  'before': 'Hom.-lacets is supported against both witnesses, including its separate hyphen and final t/s.',
  'after': 'The hom.-lacet(s) reading is supported against both witnesses, including its separate point, '
           'hyphen, tall l and crossed t; the final s remains doubtful against a terminal return, so '
           'lacets|lacet is retained.',
  'source': 'second/149_scan088_adjudications.tsv: B015'},
 {'scan': 88,
  'path': ['hand_observations', 1, 'evidence'],
  'operation': 'set',
  'before': 'B002: the upper middle link and the first three lower links have blunt or nearly upright '
            'terminal returns; neighboring clear arrow barbs provide the local contrast. The running-text '
            'maps are also headless.',
  'after': 'B002: the upper middle link and the first three lower links have blunt or nearly upright '
           'terminal returns; neighboring clear arrow barbs provide the local contrast. The prose '
           'kernel/composite links are also headless, while the separately written prose map E_U-tildeK to '
           'E_tildeK retains its arrow.',
  'source': 'second/149_scan088_adjudications.tsv: B002, B005, B011'},
 {'scan': 88,
  'path': ['inventory', 10, 'position'],
  'operation': 'set',
  'before': 'above the gap between Ainsi and E_K',
  'after': 'above the gap between Ainsi and E_tilde K',
  'source': 'second/149_scan088_adjudications.tsv: B016'},
 {'scan': 88,
  'path': ['inventory', 11, 'position'],
  'operation': 'set',
  'before': 'immediately after E_K in final sentence',
  'after': 'immediately after E_tilde K in final sentence',
  'source': 'second/149_scan088_adjudications.tsv: B016, B017'},
 {'scan': 89,
  'path': ['notes'],
  'operation': 'replace_once',
  'before': 'The internal pi-to-E link in (27) is pointed more distinctly than the two end links but is '
            'still marked with arrow first and dash alternative.',
  'after': 'After blind adjudication, the internal pi-to-E link in (27) prefers a shaft, with an arrow '
           'alternative; its rounded endpoint does not establish an independent barb.',
  'source': 'second/149_scan089_adjudications.tsv: B002'},
 {'scan': 89,
  'path': ['hand_observations', 2, 'habit'],
  'operation': 'set',
  'before': 'Low connected syllables can flatten while terminal t and final infinitive r remain distinct.',
  'after': 'Low connected syllables and terminal returns may leave verb forms unresolved.',
  'source': 'second/149_scan089_adjudications.tsv: B016, B017, B021'},
 {'scan': 89,
  'path': ['hand_observations', 2, 'evidence'],
  'operation': 'set',
  'before': 'dont has a tall final t; peut has a small angular t return; s’identifier ends with a separate r '
            'return.',
  'after': 'Dont retains a tall final t. In peut|par the middle is flattened and the t-like return only '
           'favors peut; in s’identifier|s’identifie the final curl does not establish an independent r.',
  'source': 'second/149_scan089_adjudications.tsv: B016, B017, B021'},
 {'scan': 89,
  'path': ['hand_observations', 2, 'witness_errors'],
  'operation': 'set',
  'before': 'H reads dans, par ailleurs and s’identifie.',
  'after': 'H reads dans, par ailleurs and s’identifie. Dont is retained, but par and s’identifie remain '
           'explicit alternatives in the later two places after adjudication.',
  'source': 'second/149_scan089_adjudications.tsv: B016, B017, B021'},
 {'scan': 89,
  'path': ['hand_observations', 3, 'evidence'],
  'operation': 'set',
  'before': 'ref26_dont crop shows one reference and a live6 over probable5.',
  'after': 'B006 shows one initial 2 and one parenthesis pair. The underlying digit prefers 6|5 and the live '
           'overstroke 5|6; the earlier live-6/old-5 preference is superseded.',
  'source': 'second/149_scan089_adjudications.tsv: B006'},
 {'scan': 89,
  'path': ['inventory', 2, 'first_words_or_objects'],
  'operation': 'set',
  'before': '(27) 1-\\pi\\to E_{U_s}\\to E_{k(s)}-1',
  'after': '(27) 1 [shaft|arrow] pi [shaft|arrow] E_{U_s} -> E_{k(s)} [shaft|arrow] 1; all three doubtful '
           'links prefer shafts',
  'source': 'second/149_scan089_adjudications.tsv: B002'},
 {'scan': 90,
  'path': ['notes'],
  'operation': 'replace_once',
  'before': 'The nested subscript under U in the insertion of d) and in the last main-baseline group has a '
            'low arch with a descending right leg. Eta is preferred, with K retained in a local doubt at '
            'each occurrence. Nearby outer K symbols have separate branches.',
  'after': 'The nested subscripts under U in the insertion of d) and in the last main-baseline group are '
           'read as K after completed adjudication. The short branched foot matches the same-page larger K '
           'and the documented cross-leaf controls; the earlier local eta preference is withdrawn.',
  'source': 'second/149_scan090_adjudications.tsv: B008, B021'},
 {'scan': 90,
  'path': ['notes'],
  'operation': 'replace_once',
  'before': 'The loc./cancelled les place has uncertain wording and uncertain deletion state.',
  'after': 'The following place prefers cancelled alors, retaining live loc. and cancelled les as '
           'alternatives; both wording and deletion state remain uncertain.',
  'source': 'second/149_scan090_adjudications.tsv: B014'},
 {'scan': 90,
  'path': ['notes'],
  'operation': 'replace_once',
  'before': 'The underlining begins below the compressed ns|nous and continues through identifier le groupe '
            'de décomposition.',
  'after': 'The underlining begins below the compressed ns|on|nous and continues through identifier le '
           'groupe de décomposition.',
  'source': 'second/149_scan090_adjudications.tsv: B018'},
 {'scan': 90,
  'path': ['notes'],
  'operation': 'replace_once',
  'before': 'The first final addition begins directly E_Ueta sur E_K, ou, without an added de.',
  'after': 'The first final addition begins directly E_UK sur E_K, ou, without an added de.',
  'source': 'second/149_scan090_adjudications.tsv: B021'},
 {'scan': 91,
  'path': ['notes'],
  'operation': 'replace_once',
  'before': 'K is preferred with U retained as an explicit alternative.',
  'after': 'Completed adjudication resolves both of these subgroup indices to K; the opening rounded U '
           'remains U.',
  'source': 'second/149_scan091_adjudications.tsv: B004, B012'},
 {'scan': 91,
  'path': ['notes'],
  'operation': 'replace_once',
  'before': 'The words trivial kummérien, transcendance, obstrue, tous, cette, mais de deuxième espèce, and '
            'parcourt l’ens are supported by their crops.',
  'after': 'The words trivial kummérien, obstrue, tous, cette, mais de deuxième espèce, and parcourt l’ens '
           'are supported by their crops. The abbreviated tr.-scend|tr.-scendance replaces the first-pass '
           'expansion transcendance; the final return does not settle the full ending.',
  'source': 'second/149_scan091_adjudications.tsv: B007'},
 {'scan': 91,
  'path': ['notes'],
  'operation': 'replace_once',
  'before': 'The small overwritten form below the first simeq is newly preserved as an uncertain cancelled '
            'sublabel. The question mark used inside the doubt macro is an editorial placeholder for its '
            'unknown identity, not a claimed author question mark.',
  'after': 'The small cancelled form below the first simeq is retained as doubtful de|d. Completed '
           'adjudication replaces the earlier editorial question-mark placeholder with these tentative '
           'letters; no author question mark is asserted.',
  'source': 'second/149_scan091_adjudications.tsv: B006'},
 {'scan': 91,
  'path': ['notes'],
  'operation': 'replace_once',
  'before': 'The struck word before the live article, the live le/de, the letter N after corps de, and the '
            'struck peut remain doubtful. The exact state of the tiny sublabel remains less secure than its '
            'visible presence.',
  'after': 'The struck word before the live article remains leur|le|sur; the live article remains le|de. '
           'After corps de, réf is preferred with N retained; the cancelled word before live peut remains '
           'peut|permet. The cancelled sublabel remains doubtful in its letters de|d.',
  'source': 'second/149_scan091_adjudications.tsv: B003, B006, B009, B017'},
 {'scan': 91,
  'path': ['notes'],
  'operation': 'replace_once',
  'before': 'The tentative struck le is retained with sur as an explicit alternative; its preferred-reading '
            'difference from H is counted at low confidence.',
  'after': 'The final cancelled-word reading is leur|le|sur at low confidence; this supersedes the '
           'first-pass le|sur preference.',
  'source': 'second/149_scan091_adjudications.tsv: B003'},
 {'scan': 91,
  'path': ['inventory', 2, 'first_words_or_objects'],
  'operation': 'set',
  'before': '\\unsure{le}',
  'after': '\\unsure{leur|le|sur}',
  'source': 'second/149_scan091_adjudications.tsv: B003'},
 {'scan': 91,
  'path': ['inventory', 3, 'first_words_or_objects'],
  'operation': 'set',
  'before': '\\unsure{?} (editorial placeholder for an unidentified crossed sign)',
  'after': '\\unsure{de|d} (cancelled letters; no question-mark placeholder)',
  'source': 'second/149_scan091_adjudications.tsv: B006'},
 {'scan': 91,
  'path': ['inventory', 8, 'first_words_or_objects'],
  'operation': 'set',
  'before': '\\unsure{peut}',
  'after': '\\unsure{peut|permet}',
  'source': 'second/149_scan091_adjudications.tsv: B017'},
 {'scan': 92,
  'path': ['notes'],
  'operation': 'replace_once',
  'before': 'The compressed sans and the two crossed-out words retain doubts. The live entre is heavily '
            'retraced, without a securely separable extra cancelled word.',
  'after': 'The compressed sans and the two crossed-out prose words retain doubts. The live entre|dentre is '
           'heavily retraced, without a securely separable extra cancelled word.',
  'source': 'second/149_scan092_adjudications.tsv: B002, B010, B011'},
 {'scan': 92,
  'path': ['notes'],
  'operation': 'replace_once',
  'before': 'The target in (29) has a live E outline and readable lower k(s), but its dense additional '
            'overdraw cannot be separated into a securely legible earlier cancelled symbol. The uncertainty '
            'is therefore kept on the whole term; no underlying deleted letter has been supplied.',
  'after': 'The target in (29) has a clear live replacement E and readable shared k(s). Completed '
           'adjudication tentatively reads the earlier crossed group name as Gal; its letters remain low '
           'confidence, and the deletion and replacement are now represented as separate layers.',
  'source': 'second/149_scan092_adjudications.tsv: B021'},
 {'scan': 92,
  'path': ['notes'],
  'operation': 'replace_once',
  'before': 'The singular extension and literal E_barK were confirmed; the final E target keeps an explicit '
            'uncertainty concerning the unresolved overdraw state.',
  'after': 'The singular extension and literal E_barK were confirmed. Final blind adjudication preserves de '
           'extension|d’extension and records tentative cancelled Gal beneath the live replacement E in the '
           'target of (29).',
  'source': 'second/149_scan092_adjudications.tsv: B006, B019, B021'},
 {'scan': 92,
  'path': ['inventory', 5, 'first_words_or_objects'],
  'operation': 'set',
  'before': '(29) 1---I_{s\\prime}\\to N_{s\\prime}\\to E_{k(s)}\\to1',
  'after': '(29) 1---I_s-prime -> N_s-prime -> cancelled doubtful Gal/replacement E with shared k(s) -> 1',
  'source': 'second/149_scan092_adjudications.tsv: B021'},
 {'scan': 93,
  'path': ['notes'],
  'operation': 'replace_once',
  'before': 'The crossed strict fragments, corps de, pour, Alors, the word ending prète/préter, and '
            'compressed réciproque remain explicitly doubtful where appropriate.',
  'after': 'The crossed strict fragments now read tentative raised ou and lower pas|non. The cancelled '
           'phrase after N_s-prime retains du|qui and correspond|corps de|complété; pour remains doubtful. '
           'The later cancelled word is Ainsi|Aussi, the broken-line ending prete|prète|préter remains '
           'doubtful, and the live image adjective is resolved as inverse.',
  'source': 'second/149_scan093_adjudications.tsv: B003, B004, B009, B014, B015, B017'},
 {'scan': 93,
  'path': ['notes'],
  'operation': 'replace_once',
  'before': 'The nested composite subscript is retained as η|K.',
  'after': 'The nested composite subscript is K after completed adjudication; the earlier η|K reading is '
           'superseded.',
  'source': 'second/149_scan093_adjudications.tsv: B007'},
 {'scan': 93,
  'path': ['notes'],
  'operation': 'replace_once',
  'before': 'C’s illegibility extent 2 is retained as an annotation for the crossed area, not asserted as a '
            'readable numeral or as two recovered words.',
  'after': 'C’s former illegibility extent 2 has been replaced by tentative readings of the two crossed '
           'layers before strict: raised ou and lower pas|non. Both remain cancelled and uncertain.',
  'source': 'second/149_scan093_adjudications.tsv: B003'},
 {'scan': 93,
  'path': ['notes'],
  'operation': 'replace_once',
  'before': 'The source word s’interprète/préter is divided between two baselines;',
  'after': 'The source word s’inter-prete/prète/préter is divided between two baselines;',
  'source': 'second/149_scan093_adjudications.tsv: B014'},
 {'scan': 93,
  'path': ['hand_observations', 1, 'evidence'],
  'operation': 'set',
  'before': 'The inserted first group has one tilde; the next body field has two. In the composite the outer '
            'K has distinct branches, whereas the small nested mark has a rounded hump and descending '
            'return.',
  'after': 'The inserted first group has one tilde; the next body field has two. Completed adjudication '
           'reads the nested composite index as K from its sharp low junction, rising branch and short right '
           'foot, compared with the same-page larger K and the documented controls.',
  'source': 'second/149_scan093_adjudications.tsv: B001, B007; review/149_scan093_reviewed.json: final-page '
            'double tilde and existing first-pass comparison'},
 {'scan': 93,
  'path': ['hand_observations', 1, 'witness_errors'],
  'operation': 'set',
  'before': 'H drops one body tilde; both witnesses make the nested index K without marking its η-like form.',
  'after': 'H drops one body tilde. Both witnesses’ K in the nested composite is retained after '
           'adjudication; the first-pass eta preference is withdrawn.',
  'source': 'second/149_scan093_adjudications.tsv: B001, B007; review/149_scan093_reviewed.json: final-page '
            'double tilde and existing first-pass comparison'},
 {'scan': 93,
  'path': ['notation_additions', 1, 'written'],
  'operation': 'set',
  'before': 'small rounded nested index after U',
  'after': 'small nested K with a short branched right foot after U',
  'source': 'second/149_scan093_adjudications.tsv: B007'},
 {'scan': 93,
  'path': ['notation_additions', 1, 'transcription'],
  'operation': 'set',
  'before': '\\mathcal E_{U_{\\unsure{\\eta|K}}}',
  'after': '\\mathcal E_{U_K}',
  'source': 'second/149_scan093_adjudications.tsv: B007'},
 {'scan': 93,
  'path': ['notation_additions', 1, 'evidence'],
  'operation': 'set',
  'before': 'The rounded hump/right return differs from the separate branches of outer K in the same '
            'composite crop.',
  'after': 'Completed adjudication identifies the short branched form with the same-page larger K and the '
           'documented cross-leaf K controls; the earlier eta alternative is withdrawn.',
  'source': 'second/149_scan093_adjudications.tsv: B007'},
 {'scan': 94,
  'path': ['notes'],
  'operation': 'replace_once',
  'before': 'Reading decisions: C is supported for the extra de after donc, capital cancelled On with '
            'inserted et, regardons, inline alpha fixé without pour, déduite, the capital S in the earlier '
            'U_Salpha, and the later words on n’a qu’un pt à l’infini.',
  'after': 'Reading decisions: the extra de after donc, inserted et, déduite and the absence of an added '
           'pour before alpha are retained. Completed adjudication leaves ce|en, cancelled On|(les, raised '
           'regarder.|regardons, inline alpha pris|fixés|fixé and the earlier U_Salpha|U_salpha doubtful. '
           'The later point phrase has a literal colon: on n’a qu’un pt : l’infini.',
  'source': 'second/149_scan094_adjudications.tsv: B002, B003, B004, B005, B008, B011'},
 {'scan': 94,
  'path': ['notes'],
  'operation': 'replace_once',
  'before': 'The k_alpha expression retains its doubt because the dense right-side retracing and small trace '
            'cannot be separated confidently from the visible k and lower alpha.',
  'after': 'The field expression retains its uncertain k/K and lower alpha, together with a separately '
           'recorded xi-like form and raised point to their right. Adjudication does not establish a '
           'cancellation layer there.',
  'source': 'second/149_scan094_adjudications.tsv: B012'},
 {'scan': 94,
  'path': ['notes'],
  'operation': 'replace_once',
  'before': 'The long word after comme is tantot rather than tout; the circumflex is retained as the '
            'preferred possibility, but its exact accent state remains uncertain because the crop clips part '
            'of the upper ascenders. Its anonymous second-reading box extends upward beyond the crop so this '
            'can be checked without assuming an accent absent.',
  'after': 'The long word after comme is tantot rather than tout. The first crop clipped part of the upper '
           'ascenders; completed adjudication of the expanded second-reading box still leaves the faint '
           'upper trace insufficient to settle a circumflex, so tantôt|tantot remains.',
  'source': 'second/149_scan094_adjudications.tsv: B006'},
 {'scan': 94,
  'path': ['hand_observations', 0, 'evidence'],
  'operation': 'set',
  'before': 'On_et crop: the small et is above the barred capital On; the separate voit que cancellation '
            'follows on the next slanted row.',
  'after': 'B003 places the separate live et above a cancelled group preferred as On, with (les retained '
           'because the crossing hides its small letters. The separate voit que cancellation follows on the '
           'next slanted row.',
  'source': 'second/149_scan094_adjudications.tsv: B003'},
 {'scan': 94,
  'path': ['hand_observations', 0, 'witness_errors'],
  'operation': 'set',
  'before': 'H reads the cancelled On as ou.',
  'after': 'H reads the cancelled group as ou. Final adjudication retains On|(les rather than the first-pass '
           'certainty about capital On.',
  'source': 'second/149_scan094_adjudications.tsv: B003'},
 {'scan': 94,
  'path': ['hand_observations', 3, 'habit'],
  'operation': 'set',
  'before': 'A narrow, vertically extended capital S can occur in a small subscript.',
  'after': 'Subscript height may favor capital S without excluding a compressed lowercase s.',
  'source': 'second/149_scan094_adjudications.tsv: B008, B010'},
 {'scan': 94,
  'path': ['hand_observations', 3, 'evidence'],
  'operation': 'set',
  'before': 'U_Salpha crop: the long curved S and its lower hook precede a smaller alpha. The later crowded '
            'subscript is assessed separately and left uncertain.',
  'after': 'B008 records a tall narrow curved body and lower return before alpha: capital S is preferred, '
           'but lowercase s remains possible. The later crowded generic-fibre subscript is separately '
           'retained as s|S.',
  'source': 'second/149_scan094_adjudications.tsv: B008, B010'},
 {'scan': 94,
  'path': ['hand_observations', 3, 'witness_errors'],
  'operation': 'set',
  'before': 'H reads lowercase s in the earlier open-subset notation.',
  'after': 'H has lowercase s in the earlier open-subset notation. Completed adjudication retains both '
           'cases, superseding the first-pass certain capital S.',
  'source': 'second/149_scan094_adjudications.tsv: B008, B010'},
 {'scan': 94,
  'path': ['inventory', 2, 'first_words_or_objects'],
  'operation': 'set',
  'before': 'Ceci rappelé, on se demande donc de ce qui se passe',
  'after': 'Ceci rappelé, on se demande donc de ce|en qui se passe (ce/en doubtful)',
  'source': 'second/149_scan094_adjudications.tsv: B002'},
 {'scan': 94,
  'path': ['inventory', 3, 'first_words_or_objects'],
  'operation': 'set',
  'before': 'On',
  'after': 'On|(les (cancelled and doubtful)',
  'source': 'second/149_scan094_adjudications.tsv: B003'},
 {'scan': 95,
  'path': ['notes'],
  'operation': 'replace_once',
  'before': 'the final sentence ends unfinished at car cela n’est.',
  'after': 'the final sentence ends unfinished at car cela vient|n’est, with vient preferred and both '
           'readings doubtful.',
  'source': 'second/149_scan095_adjudications.tsv: B030'},
 {'scan': 95,
  'path': ['notes'],
  'operation': 'replace_once',
  'before': 'four raised insertions, three cancellations, the author’s 47 above and a fine other-hand 94 '
            'below left.',
  'after': 'four raised insertions, three cancelled text groups and a further altered closing-parenthesis '
           'form with doubtful cancellation state, the author’s 47 above and a fine other-hand 94 below '
           'left.',
  'source': 'second/149_scan095_adjudications.tsv: B018, B021'},
 {'scan': 95,
  'path': ['notes'],
  'operation': 'replace_once',
  'before': 'Diplomatic cautions: preserve XB literally, without identifying or normalizing B.',
  'after': 'Diplomatic cautions: preserve the nested B followed by its small point as B.|B_0 under doubt, '
           'without identifying or normalizing B.',
  'source': 'second/149_scan095_adjudications.tsv: B007'},
 {'scan': 95,
  'path': ['notes'],
  'operation': 'replace_once',
  'before': 'The first superscript remains r|vee despite the familiar conormal context; no mathematical '
            'expectation settles that stroke.',
  'after': 'The first superscript remains r|+|vee despite the familiar conormal context; no mathematical '
           'expectation settles that stroke.',
  'source': 'second/149_scan095_adjudications.tsv: B017'},
 {'scan': 95,
  'path': ['notes'],
  'operation': 'replace_once',
  'before': 'The plural reading of the crowded raised verb and biais remain locally uncertain.',
  'after': 'The raised verb remains intervient|interviennent, its following short form p-with-raised-r|par, '
           'and the noun brin|biais|bon|bout. The subsequent elles définissent is resolved.',
  'source': 'second/149_scan095_adjudications.tsv: B013'},
 {'scan': 95,
  'path': ['notes'],
  'operation': 'replace_once',
  'before': 'The en before lesquels is retraced on its existing strokes, with no separable earlier word or '
            'cancellation.',
  'after': 'The retraced preposition remains sur|en, followed by the separately written les quels; no '
           'distinct earlier cancelled word is supplied.',
  'source': 'second/149_scan095_adjudications.tsv: B016'},
 {'scan': 95,
  'path': ['notes'],
  'operation': 'replace_once',
  'before': 'Tiny isolated dots near XB and before the second N have no secure role as punctuation or '
            'mathematical signs and are not promoted to text.',
  'after': 'Completed adjudication explicitly retains the point beside nested B as B.|B_0 and the two points '
           'before the second N as ..|:. Their exact roles remain uncertain, but the visible marks are not '
           'omitted.',
  'source': 'second/149_scan095_adjudications.tsv: B007, B019'},
 {'scan': 95,
  'path': ['notes'],
  'operation': 'replace_once',
  'before': 'Scope of checks: this is visual transcription and comparison only.',
  'after': 'First-reader scope of checks: this was visual transcription and comparison only; the later '
           'main-reader conditional calculation is recorded separately below.',
  'source': 'review/149_scan095_reviewed.json: notes and check_events (149095-conormal-local-generator)'},
 {'scan': 95,
  'path': ['hand_observations', 0, 'evidence'],
  'operation': 'set',
  'before': 'The article before classes, the small final loop of classes, the g-e ending and detached glyph '
            'of scindages, and donc/du are treated separately rather than regularized by agreement.',
  'after': 'The article is resolved as la independently of classes|classe. The scindages comma is resolved, '
           'while the later compressed word remains de|donc|du followed by two explicit points, ..|:. These '
           'decisions preserve local ink without grammatical regularization.',
  'source': 'second/149_scan095_adjudications.tsv: B004, B005, B006, B019'},
 {'scan': 95,
  'path': ['hand_observations', 0, 'witness_errors'],
  'operation': 'set',
  'before': 'C and H differ on article/number and punctuation; some local alternatives remain unresolved.',
  'after': 'C and H differ on article/number and punctuation. Completed adjudication resolves la and the '
           'scindages comma, while retaining the noun-number and later word/point alternatives.',
  'source': 'second/149_scan095_adjudications.tsv: B004, B005, B006, B019'},
 {'scan': 95,
  'path': ['inventory', 3, 'first_words_or_objects'],
  'operation': 'set',
  'before': '(qui intervient par le biais …)',
  'after': '(qui \\unsure{intervient|interviennent} \\unsure{p\\textsuperscript{r}|par} le '
           '\\unsure{brin|biais|bon|bout} qu’elles définissent …)',
  'source': 'second/149_scan095_adjudications.tsv: B013'},
 {'scan': 95,
  'path': ['inventory', 4, 'first_words_or_objects'],
  'operation': 'set',
  'before': 'On peut se proposer d’étudier … car cela n’est',
  'after': 'On peut se proposer d’étudier … car cela vient|n’est (ending doubtful)',
  'source': 'second/149_scan095_adjudications.tsv: B030'},
 {'scan': 95,
  'path': ['inventory', 8, 'first_words_or_objects'],
  'operation': 'set',
  'before': 'moins',
  'after': 'unique|moins (cancelled and doubtful)',
  'source': 'second/149_scan095_adjudications.tsv: B027'},
 {'scan': 95,
  'path': ['inventory', 9, 'position'],
  'operation': 'set',
  'before': 'above cancelled moins at right end of baseline 19',
  'after': 'above cancelled unique|moins at right end of baseline 19',
  'source': 'second/149_scan095_adjudications.tsv: B027'},
 {'scan': 80,
  'path': ['inventory', 0, 'hand'],
  'operation': 'set',
  'before': 'main manuscript hand',
  'after': 'his hand',
  'source': 'review/149_scan080_reviewed.json: existing main-manuscript attribution for opening paragraph; '
            'operative PROMPT: inventory hand field'},
 {'scan': 80,
  'path': ['inventory', 1, 'hand'],
  'operation': 'set',
  'before': 'main manuscript hand',
  'after': 'his hand',
  'source': 'review/149_scan080_reviewed.json: existing main-manuscript attribution for display 13; '
            'operative PROMPT: inventory hand field'},
 {'scan': 80,
  'path': ['inventory', 2, 'hand'],
  'operation': 'set',
  'before': 'main manuscript hand',
  'after': 'his hand',
  'source': 'review/149_scan080_reviewed.json: existing main-manuscript attribution for class sentence; '
            'operative PROMPT: inventory hand field'},
 {'scan': 80,
  'path': ['inventory', 3, 'hand'],
  'operation': 'set',
  'before': 'main manuscript hand',
  'after': 'his hand',
  'source': 'review/149_scan080_reviewed.json: existing main-manuscript attribution for cancelled de '
            'candidate; operative PROMPT: inventory hand field'},
 {'scan': 80,
  'path': ['inventory', 4, 'hand'],
  'operation': 'set',
  'before': 'main manuscript hand',
  'after': 'his hand',
  'source': 'review/149_scan080_reviewed.json: existing main-manuscript attribution for display 14 and lower '
            'identification; operative PROMPT: inventory hand field'},
 {'scan': 80,
  'path': ['inventory', 5, 'hand'],
  'operation': 'set',
  'before': 'main manuscript hand',
  'after': 'his hand',
  'source': 'review/149_scan080_reviewed.json: existing main-manuscript attribution for K(pi,1) condition; '
            'operative PROMPT: inventory hand field'},
 {'scan': 80,
  'path': ['inventory', 6, 'hand'],
  'operation': 'set',
  'before': 'main manuscript hand',
  'after': 'his hand',
  'source': 'review/149_scan080_reviewed.json: existing main-manuscript attribution for display 15; '
            'operative PROMPT: inventory hand field'},
 {'scan': 80,
  'path': ['inventory', 7, 'hand'],
  'operation': 'set',
  'before': 'main manuscript hand',
  'after': 'his hand',
  'source': 'review/149_scan080_reviewed.json: existing main-manuscript attribution for Kummer sentence and '
            'parenthesis; operative PROMPT: inventory hand field'},
 {'scan': 80,
  'path': ['inventory', 8, 'hand'],
  'operation': 'set',
  'before': 'main manuscript hand',
  'after': 'his hand',
  'source': 'review/149_scan080_reviewed.json: existing main-manuscript attribution for display 16; '
            'operative PROMPT: inventory hand field'},
 {'scan': 80,
  'path': ['inventory', 9, 'hand'],
  'operation': 'set',
  'before': 'main manuscript hand',
  'after': 'his hand',
  'source': 'review/149_scan080_reviewed.json: existing main-manuscript attribution for limit transition; '
            'operative PROMPT: inventory hand field'},
 {'scan': 80,
  'path': ['inventory', 10, 'hand'],
  'operation': 'set',
  'before': 'main manuscript hand',
  'after': 'his hand',
  'source': 'review/149_scan080_reviewed.json: existing main-manuscript attribution for display 17 and lower '
            'definition; operative PROMPT: inventory hand field'},
 {'scan': 80,
  'path': ['inventory', 11, 'hand'],
  'operation': 'set',
  'before': 'main manuscript hand',
  'after': 'his hand',
  'source': 'review/149_scan080_reviewed.json: existing main-manuscript attribution for unfinished final '
            'sentence; operative PROMPT: inventory hand field'},
 {'scan': 80,
  'path': ['inventory', 12, 'hand'],
  'operation': 'set',
  'before': 'main manuscript hand',
  'after': 'his hand',
  'source': 'review/149_scan080_reviewed.json: existing main-manuscript attribution for cancelled car '
            'candidate; operative PROMPT: inventory hand field'},
 {'scan': 80,
  'path': ['inventory', 13, 'hand'],
  'operation': 'set',
  'before': 'main manuscript hand',
  'after': 'his hand',
  'source': 'review/149_scan080_reviewed.json: existing main-manuscript attribution for final abbreviation; '
            'operative PROMPT: inventory hand field'},
 {'scan': 80,
  'path': ['inventory', 14, 'hand'],
  'operation': 'set',
  'before': 'unidentified finer foliation hand',
  'after': 'another unnamed hand',
  'source': 'review/149_scan080_reviewed.json: existing finer foliation-hand distinction; operative PROMPT: '
            'inventory hand field'},
 {'scan': 87,
  'path': ['inventory', 1, 'hand'],
  'operation': 'set',
  'before': 'main cursive mathematical hand',
  'after': 'his hand',
  'source': 'review/149_scan087_reviewed.json: existing main-manuscript attribution for continuation; '
            'operative PROMPT: inventory hand field'},
 {'scan': 87,
  'path': ['inventory', 2, 'hand'],
  'operation': 'set',
  'before': 'main cursive mathematical hand; vertically cancelled',
  'after': 'his hand',
  'source': 'review/149_scan087_reviewed.json: existing main-manuscript attribution for cancelled_margin; '
            'operative PROMPT: inventory hand field'},
 {'scan': 87,
  'path': ['inventory', 3, 'hand'],
  'operation': 'set',
  'before': 'main hand, horizontal cancellation',
  'after': 'his hand',
  'source': 'review/149_scan087_reviewed.json: existing main-manuscript attribution for cancelled_comme; '
            'operative PROMPT: inventory hand field'},
 {'scan': 87,
  'path': ['inventory', 4, 'hand'],
  'operation': 'set',
  'before': 'main cursive mathematical hand',
  'after': 'his hand',
  'source': 'review/149_scan087_reviewed.json: existing main-manuscript attribution for '
            'geometric_interpretation; operative PROMPT: inventory hand field'},
 {'scan': 87,
  'path': ['inventory', 5, 'hand'],
  'operation': 'set',
  'before': 'main hand, horizontal cancellation',
  'after': 'his hand',
  'source': 'review/149_scan087_reviewed.json: existing main-manuscript attribution for cancelled_interline; '
            'operative PROMPT: inventory hand field'},
 {'scan': 87,
  'path': ['inventory', 6, 'hand'],
  'operation': 'set',
  'before': 'main hand, multiple cancellation strokes',
  'after': 'his hand',
  'source': 'review/149_scan087_reviewed.json: existing main-manuscript attribution for old_local_symbol; '
            'operative PROMPT: inventory hand field'},
 {'scan': 87,
  'path': ['inventory', 7, 'hand'],
  'operation': 'set',
  'before': 'main mathematical hand',
  'after': 'his hand',
  'source': 'review/149_scan087_reviewed.json: existing main-manuscript attribution for new_local_symbol; '
            'operative PROMPT: inventory hand field'},
 {'scan': 87,
  'path': ['inventory', 8, 'hand'],
  'operation': 'set',
  'before': 'main cursive hand',
  'after': 'his hand',
  'source': 'review/149_scan087_reviewed.json: existing main-manuscript attribution for trait_note; '
            'operative PROMPT: inventory hand field'},
 {'scan': 87,
  'path': ['inventory', 9, 'hand'],
  'operation': 'set',
  'before': 'main hand, horizontal cancellation',
  'after': 'his hand',
  'source': 'review/149_scan087_reviewed.json: existing main-manuscript attribution for cancelled_extension; '
            'operative PROMPT: inventory hand field'},
 {'scan': 87,
  'path': ['inventory', 10, 'hand'],
  'operation': 'set',
  'before': 'main mathematical hand',
  'after': 'his hand',
  'source': 'review/149_scan087_reviewed.json: existing main-manuscript attribution for display_23; '
            'operative PROMPT: inventory hand field'},
 {'scan': 87,
  'path': ['inventory', 11, 'hand'],
  'operation': 'set',
  'before': 'main cursive mathematical hand',
  'after': 'his hand',
  'source': 'review/149_scan087_reviewed.json: existing main-manuscript attribution for extension_sentence; '
            'operative PROMPT: inventory hand field'},
 {'scan': 87,
  'path': ['inventory', 12, 'hand'],
  'operation': 'set',
  'before': 'main hand, horizontal cancellation',
  'after': 'his hand',
  'source': 'review/149_scan087_reviewed.json: existing main-manuscript attribution for cancelled_suite; '
            'operative PROMPT: inventory hand field'},
 {'scan': 87,
  'path': ['inventory', 13, 'hand'],
  'operation': 'set',
  'before': 'main mathematical hand',
  'after': 'his hand',
  'source': 'review/149_scan087_reviewed.json: existing main-manuscript attribution for inserted_E; '
            'operative PROMPT: inventory hand field'},
 {'scan': 87,
  'path': ['inventory', 14, 'hand'],
  'operation': 'set',
  'before': 'main mathematical hand',
  'after': 'his hand',
  'source': 'review/149_scan087_reviewed.json: existing main-manuscript attribution for diagram_24_25; '
            'operative PROMPT: inventory hand field'},
 {'scan': 87,
  'path': ['inventory', 15, 'hand'],
  'operation': 'set',
  'before': 'main cursive mathematical hand',
  'after': 'his hand',
  'source': 'review/149_scan087_reviewed.json: existing main-manuscript attribution for residue_sentence; '
            'operative PROMPT: inventory hand field'},
 {'scan': 90,
  'path': ['inventory', 0, 'hand'],
  'operation': 'set',
  'before': 'main cursive mathematical hand',
  'after': 'his hand',
  'source': 'review/149_scan090_reviewed.json: existing main-manuscript attribution for heading; operative '
            'PROMPT: inventory hand field'},
 {'scan': 90,
  'path': ['inventory', 1, 'hand'],
  'operation': 'set',
  'before': 'main cursive mathematical hand',
  'after': 'his hand',
  'source': 'review/149_scan090_reviewed.json: existing main-manuscript attribution for condition_a; '
            'operative PROMPT: inventory hand field'},
 {'scan': 90,
  'path': ['inventory', 2, 'hand'],
  'operation': 'set',
  'before': 'main cursive mathematical hand',
  'after': 'his hand',
  'source': 'review/149_scan090_reviewed.json: existing main-manuscript attribution for condition_b; '
            'operative PROMPT: inventory hand field'},
 {'scan': 90,
  'path': ['inventory', 3, 'hand'],
  'operation': 'set',
  'before': 'main cursive mathematical hand',
  'after': 'his hand',
  'source': 'review/149_scan090_reviewed.json: existing main-manuscript attribution for condition_c; '
            'operative PROMPT: inventory hand field'},
 {'scan': 90,
  'path': ['inventory', 4, 'hand'],
  'operation': 'set',
  'before': 'main cursive mathematical hand',
  'after': 'his hand',
  'source': 'review/149_scan090_reviewed.json: existing main-manuscript attribution for condition_d; '
            'operative PROMPT: inventory hand field'},
 {'scan': 90,
  'path': ['inventory', 5, 'hand'],
  'operation': 'set',
  'before': 'main cursive mathematical hand',
  'after': 'his hand',
  'source': 'review/149_scan090_reviewed.json: existing main-manuscript attribution for d_group_insertion; '
            'operative PROMPT: inventory hand field'},
 {'scan': 90,
  'path': ['inventory', 6, 'hand'],
  'operation': 'set',
  'before': 'main cursive mathematical hand',
  'after': 'his hand',
  'source': 'review/149_scan090_reviewed.json: existing main-manuscript attribution for d_cancelled_verb; '
            'operative PROMPT: inventory hand field'},
 {'scan': 90,
  'path': ['inventory', 7, 'hand'],
  'operation': 'set',
  'before': 'main cursive mathematical hand',
  'after': 'his hand',
  'source': 'review/149_scan090_reviewed.json: existing main-manuscript attribution for d_inserted_verb; '
            'operative PROMPT: inventory hand field'},
 {'scan': 90,
  'path': ['inventory', 8, 'hand'],
  'operation': 'set',
  'before': 'main cursive mathematical hand',
  'after': 'his hand',
  'source': 'review/149_scan090_reviewed.json: existing main-manuscript attribution for condition_e; '
            'operative PROMPT: inventory hand field'},
 {'scan': 90,
  'path': ['inventory', 9, 'hand'],
  'operation': 'set',
  'before': 'main cursive mathematical hand',
  'after': 'his hand',
  'source': 'review/149_scan090_reviewed.json: existing main-manuscript attribution for e_cancelled_regular; '
            'operative PROMPT: inventory hand field'},
 {'scan': 90,
  'path': ['inventory', 10, 'hand'],
  'operation': 'set',
  'before': 'main cursive mathematical hand',
  'after': 'his hand',
  'source': 'review/149_scan090_reviewed.json: existing main-manuscript attribution for cancelled_f_label; '
            'operative PROMPT: inventory hand field'},
 {'scan': 90,
  'path': ['inventory', 11, 'hand'],
  'operation': 'set',
  'before': 'main cursive mathematical hand',
  'after': 'his hand',
  'source': 'review/149_scan090_reviewed.json: existing main-manuscript attribution for cancelled_Si; '
            'operative PROMPT: inventory hand field'},
 {'scan': 90,
  'path': ['inventory', 12, 'hand'],
  'operation': 'set',
  'before': 'main cursive mathematical hand',
  'after': 'his hand',
  'source': 'review/149_scan090_reviewed.json: existing main-manuscript attribution for inserted_Designons; '
            'operative PROMPT: inventory hand field'},
 {'scan': 90,
  'path': ['inventory', 13, 'hand'],
  'operation': 'set',
  'before': 'main cursive mathematical hand',
  'after': 'his hand',
  'source': 'review/149_scan090_reviewed.json: existing main-manuscript attribution for '
            'cancelled_designation; operative PROMPT: inventory hand field'},
 {'scan': 90,
  'path': ['inventory', 14, 'hand'],
  'operation': 'set',
  'before': 'main cursive mathematical hand',
  'after': 'his hand',
  'source': 'review/149_scan090_reviewed.json: existing main-manuscript attribution for rewritten_section; '
            'operative PROMPT: inventory hand field'},
 {'scan': 90,
  'path': ['inventory', 15, 'hand'],
  'operation': 'set',
  'before': 'main cursive mathematical hand; deletion state uncertain',
  'after': 'his hand',
  'source': 'review/149_scan090_reviewed.json: existing main-manuscript attribution for uncertain_loc; '
            'operative PROMPT: inventory hand field'},
 {'scan': 90,
  'path': ['inventory', 16, 'hand'],
  'operation': 'set',
  'before': 'main cursive mathematical hand',
  'after': 'his hand',
  'source': 'review/149_scan090_reviewed.json: existing main-manuscript attribution for cancelled_existence; '
            'operative PROMPT: inventory hand field'},
 {'scan': 90,
  'path': ['inventory', 17, 'hand'],
  'operation': 'set',
  'before': 'main cursive mathematical hand',
  'after': 'his hand',
  'source': 'review/149_scan090_reviewed.json: existing main-manuscript attribution for '
            'cancelled_formula_insertion; operative PROMPT: inventory hand field'},
 {'scan': 90,
  'path': ['inventory', 18, 'hand'],
  'operation': 'set',
  'before': 'main cursive mathematical hand',
  'after': 'his hand',
  'source': 'review/149_scan090_reviewed.json: existing main-manuscript attribution for boundary_formula; '
            'operative PROMPT: inventory hand field'},
 {'scan': 90,
  'path': ['inventory', 19, 'hand'],
  'operation': 'set',
  'before': 'main cursive mathematical hand',
  'after': 'his hand',
  'source': 'review/149_scan090_reviewed.json: existing main-manuscript attribution for '
            'index_identification; operative PROMPT: inventory hand field'},
 {'scan': 90,
  'path': ['inventory', 20, 'hand'],
  'operation': 'set',
  'before': 'main cursive mathematical hand',
  'after': 'his hand',
  'source': 'review/149_scan090_reviewed.json: existing main-manuscript attribution for '
            'decomposition_paragraph; operative PROMPT: inventory hand field'},
 {'scan': 90,
  'path': ['inventory', 21, 'hand'],
  'operation': 'set',
  'before': 'main cursive mathematical hand',
  'after': 'his hand',
  'source': 'review/149_scan090_reviewed.json: existing main-manuscript attribution for '
            'underlined_identification; operative PROMPT: inventory hand field'},
 {'scan': 90,
  'path': ['inventory', 22, 'hand'],
  'operation': 'set',
  'before': 'main cursive mathematical hand',
  'after': 'his hand',
  'source': 'review/149_scan090_reviewed.json: existing main-manuscript attribution for cancelled_pi_s; '
            'operative PROMPT: inventory hand field'},
 {'scan': 90,
  'path': ['inventory', 23, 'hand'],
  'operation': 'set',
  'before': 'main cursive mathematical hand',
  'after': 'his hand',
  'source': 'review/149_scan090_reviewed.json: existing main-manuscript attribution for '
            'inserted_extension_note; operative PROMPT: inventory hand field'},
 {'scan': 90,
  'path': ['inventory', 24, 'hand'],
  'operation': 'set',
  'before': 'main cursive mathematical hand',
  'after': 'his hand',
  'source': 'review/149_scan090_reviewed.json: existing main-manuscript attribution for inserted_un; '
            'operative PROMPT: inventory hand field'},
 {'scan': 90,
  'path': ['inventory', 25, 'hand'],
  'operation': 'set',
  'before': 'main cursive mathematical hand',
  'after': 'his hand',
  'source': 'review/149_scan090_reviewed.json: existing main-manuscript attribution for '
            'inserted_global_scindage; operative PROMPT: inventory hand field'},
 {'scan': 90,
  'path': ['inventory', 26, 'hand'],
  'operation': 'set',
  'before': 'main cursive mathematical hand',
  'after': 'his hand',
  'source': 'review/149_scan090_reviewed.json: existing main-manuscript attribution for inserted_E_Xs; '
            'operative PROMPT: inventory hand field'},
 {'scan': 93,
  'path': ['inventory', 0, 'hand'],
  'operation': 'set',
  'before': 'main manuscript hand',
  'after': 'his hand',
  'source': 'review/149_scan093_reviewed.json: existing main-manuscript attribution for main_text_1; '
            'operative PROMPT: inventory hand field'},
 {'scan': 93,
  'path': ['inventory', 1, 'hand'],
  'operation': 'set',
  'before': 'main manuscript hand',
  'after': 'his hand',
  'source': 'review/149_scan093_reviewed.json: existing main-manuscript attribution for main_text_2; '
            'operative PROMPT: inventory hand field'},
 {'scan': 93,
  'path': ['inventory', 4, 'hand'],
  'operation': 'set',
  'before': 'main manuscript hand',
  'after': 'his hand',
  'source': 'review/149_scan093_reviewed.json: existing main-manuscript attribution for '
            'first_deleted_phrase; operative PROMPT: inventory hand field'},
 {'scan': 93,
  'path': ['inventory', 5, 'hand'],
  'operation': 'set',
  'before': 'main manuscript hand',
  'after': 'his hand',
  'source': 'review/149_scan093_reviewed.json: existing main-manuscript attribution for '
            'first_inserted_identification; operative PROMPT: inventory hand field'},
 {'scan': 93,
  'path': ['inventory', 6, 'hand'],
  'operation': 'set',
  'before': 'main manuscript hand',
  'after': 'his hand',
  'source': 'review/149_scan093_reviewed.json: existing main-manuscript attribution for '
            'strict_cancelled_fragments; operative PROMPT: inventory hand field'},
 {'scan': 93,
  'path': ['inventory', 7, 'hand'],
  'operation': 'set',
  'before': 'main manuscript hand',
  'after': 'his hand',
  'source': 'review/149_scan093_reviewed.json: existing main-manuscript attribution for Ns_deleted_phrase; '
            'operative PROMPT: inventory hand field'},
 {'scan': 93,
  'path': ['inventory', 8, 'hand'],
  'operation': 'set',
  'before': 'main manuscript hand',
  'after': 'his hand',
  'source': 'review/149_scan093_reviewed.json: existing main-manuscript attribution for '
            'Ns_inserted_identification; operative PROMPT: inventory hand field'},
 {'scan': 93,
  'path': ['inventory', 9, 'hand'],
  'operation': 'set',
  'before': 'main manuscript hand',
  'after': 'his hand',
  'source': 'review/149_scan093_reviewed.json: existing main-manuscript attribution for deleted_de; '
            'operative PROMPT: inventory hand field'},
 {'scan': 93,
  'path': ['inventory', 10, 'hand'],
  'operation': 'set',
  'before': 'main manuscript hand',
  'after': 'his hand',
  'source': 'review/149_scan093_reviewed.json: existing main-manuscript attribution for '
            'a_priori_parenthetical; operative PROMPT: inventory hand field'},
 {'scan': 93,
  'path': ['inventory', 11, 'hand'],
  'operation': 'set',
  'before': 'main manuscript hand',
  'after': 'his hand',
  'source': 'review/149_scan093_reviewed.json: existing main-manuscript attribution for deleted_pour; '
            'operative PROMPT: inventory hand field'},
 {'scan': 93,
  'path': ['inventory', 12, 'hand'],
  'operation': 'set',
  'before': 'main manuscript hand',
  'after': 'his hand',
  'source': 'review/149_scan093_reviewed.json: existing main-manuscript attribution for '
            'first_que_possible_deletion; operative PROMPT: inventory hand field'},
 {'scan': 93,
  'path': ['inventory', 13, 'hand'],
  'operation': 'set',
  'before': 'main manuscript hand',
  'after': 'his hand',
  'source': 'review/149_scan093_reviewed.json: existing main-manuscript attribution for peut_deletion; '
            'operative PROMPT: inventory hand field'},
 {'scan': 93,
  'path': ['inventory', 14, 'hand'],
  'operation': 'set',
  'before': 'main manuscript hand',
  'after': 'his hand',
  'source': 'review/149_scan093_reviewed.json: existing main-manuscript attribution for donc_insertion; '
            'operative PROMPT: inventory hand field'},
 {'scan': 93,
  'path': ['inventory', 15, 'hand'],
  'operation': 'set',
  'before': 'main manuscript hand',
  'after': 'his hand',
  'source': 'review/149_scan093_reviewed.json: existing main-manuscript attribution for Alors_deletion; '
            'operative PROMPT: inventory hand field'},
 {'scan': 95,
  'path': ['inventory', 11, 'hand'],
  'operation': 'set',
  'before': 'main manuscript hand',
  'after': 'his hand',
  'source': 'review/149_scan095_reviewed.json: existing main-manuscript attribution for '
            'altered_parenthesis_after_regulier; operative PROMPT: inventory hand field'}]

def parent_and_key(record, path):
    current = record
    for component in path[:-1]:
        current = current[component]
    return current, path[-1]


def prepare_changes():
    originals = {}
    proposed = {}
    for patch in PATCHES:
        scan = patch["scan"]
        path = patch["path"]
        if scan not in range(79, 96) or not path or path[0] not in ALLOWED_FIELDS:
            raise ValueError(f"Disallowed target: {scan} {path}")
        if scan not in originals:
            source = WORK_ROOT / "review" / f"149_scan{scan:03d}_reviewed.json"
            originals[scan] = json.loads(source.read_text(encoding="utf-8"))
            proposed[scan] = copy.deepcopy(originals[scan])
        parent, key = parent_and_key(proposed[scan], path)
        current = parent[key]
        before = patch["before"]
        if patch["operation"] == "replace_once":
            if not isinstance(current, str) or current.count(before) != 1:
                raise ValueError(f"Precondition failed: scan {scan:03d}, {path}; {patch['source']}")
            parent[key] = current.replace(before, patch["after"], 1)
        elif patch["operation"] == "set":
            if current != before:
                raise ValueError(f"Precondition failed: scan {scan:03d}, {path}; {patch['source']}")
            parent[key] = copy.deepcopy(patch["after"])
        else:
            raise ValueError(f"Unknown operation: {patch['operation']}")
    for scan, original in originals.items():
        final = proposed[scan]
        if original.keys() != final.keys():
            raise ValueError(f"Unexpected schema change on scan {scan:03d}")
        for field in original:
            if field not in ALLOWED_FIELDS and final[field] != original[field]:
                raise ValueError(f"Disallowed field changed: scan {scan:03d}, {field}")
    return originals, proposed


def atomic_write_json(path, value):
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent,
                                         prefix=path.name + ".", suffix=".tmp", delete=False) as handle:
            temporary = Path(handle.name)
            json.dump(value, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="Apply only after root review; default is validation only")
    args = parser.parse_args()
    originals, proposed = prepare_changes()
    for scan in sorted(proposed):
        fields = sorted(field for field in ALLOWED_FIELDS if originals[scan][field] != proposed[scan][field])
        print(f"149_scan{scan:03d}: " + ", ".join(fields))
    if not args.apply:
        print("Proposal validated only; no files written.")
        return
    # Preconditions for every leaf have already passed before the first write.
    for scan in sorted(proposed):
        path = WORK_ROOT / "review" / f"149_scan{scan:03d}_reviewed.json"
        atomic_write_json(path, proposed[scan])
    print("Explanatory fields updated. No pages, frozen readings, adjudications or generated documents were touched.")


if __name__ == "__main__":
    main()
