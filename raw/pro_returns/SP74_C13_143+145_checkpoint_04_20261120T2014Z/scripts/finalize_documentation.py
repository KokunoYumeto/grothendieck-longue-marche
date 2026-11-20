#!/usr/bin/env python3
"""Reconcile final documentary status after all independent readings.

This script never changes a transcription fragment. Reading decisions are made
in the page-specific adjudication plans. Historical reader reports are retained.
"""
from pathlib import Path
from datetime import datetime, timezone
import json

ROOT = Path(__file__).resolve().parents[1]
WHO = 'GPT-6 Astra Pro; inherited effort not exposed; SP74 second pass; main reader'

ALIASES = {
    '143_scan008-(22)-(23)': '143_scan008-N1',
    '143_scan008-section5': '143_scan008-N3',
    '143_scan008-margin': '143_scan008-N2',
    '143_scan009-auditC-N1-upper': '143_scan009-N1',
    '143_scan009-auditC-N1-recap': '143_scan009-N2',
    '143_scan010-fundamental-identity': '143_scan010-N1',
    '143_scan010-extensions-and-lift': '143_scan010-N1',
    '143_scan010-final-I-J-notation': '143_scan010-audit-main-N1',
    '143_scan012-programme-a-b': '143_scan012-N1',
    '143_scan012-NB-cover': '143_scan012-N2',
    '143_scan012-NB-hole-operations': '143_scan012-N2',
    '143_scan015-splitting-data': '143_scan015-N2',
    '143_scan015-marked-cover': '143_scan015-N3',
    '143_scan015-equivariance-torsor': '143_scan015-N4',
    '143_scan019-beta-construction': '143_scan019-N1',
    '143_scan019-free-action-correspondence': '143_scan019-N2',
    '143_scan019-added-data': '143_scan019-N3',
    '143_scan025-pseudo-partition': '143_scan025-N1',
    '143_scan025-reconstruction': '143_scan025-N2',
    '143_scan025-stabilizers-compatibility': '143_scan025-N3',
    '143_scan028-triviality': '143_scan028-N1',
    '143_scan028-geometric-description': '143_scan028-N2',
    '143_scan028-braid-functoriality': '143_scan028-N3',
    '143_scan028-actions': '143_scan028-N4',
    '143_scan033-group-letter-notation': '143_scan033-N7',
    '143_scan034-N4-second-stack': '143_scan034-N4',
}

NOTE_UPDATES = {
    '143_scan015-N6': 'Main inspected the original, all eight reader crops and six additional crops. The first Splitt numerator is strongly E-shaped; the final cross-page comparison retains the same explicit E/Sigma alternative at each occurrence because the alphabet is not uniquely established. The bottom 14 is pencil pagination by an unidentified hand. No date is written.',
    '143_scan017-N2': 'The reformulation considers a group extension together with a nonempty set on which the extension group acts and the kernel acts freely; these systems form the category C. It then considers a connected groupoid with a universal cover and a group action, declaring a category C-prime. Beside connexe, the tiny addition is reproduced as the visible loop and short bar under a doubt mark. Neither the words non vide nor a complete nonempty-set formula are supplied from the intended mathematics.',
}

DOUBT_REASON_UPDATES = {
    'Rounded zigzag shape admits both; parent requests consistent unresolved shared notation pending cross-page adjudication.':
        'The rounded zigzag shape admits both. Final cross-page comparison retains the same unresolved E/Sigma identification consistently; no local definition uniquely names its alphabet.',
    'The glyph is rounded and two-lobed. Reader B prefers calligraphic E, but the main reader reports disagreement between readers and requires the same unresolved choice throughout until further evidence settles it.':
        'The glyph is rounded and two-lobed. Reader B prefers calligraphic E. Final main comparison retains E/Sigma throughout because the inspected forms do not uniquely establish the alphabet.',
    'The main pair-definition crop and upper-extension crop show two open bowls resembling a cursive E. The shared notation remains provisional pending comparison with the other pages; the uncertainty concerns alphabet encoding, not a different mathematical object.':
        'The main pair-definition crop and upper-extension crop show two open bowls resembling a cursive E. Final comparison with the other pages retains the shared E/Sigma alternative; the uncertainty concerns alphabet encoding, not a different mathematical object.',
}

def main():
    order = json.loads((ROOT/'page_order.json').read_text())
    paths = [ROOT/'reviews'/f"{p['key']}_accepted.json" for p in order]
    records = [json.loads(p.read_text()) for p in paths]
    assert len(records) == 24
    assert all(r.get('audited_at') and r.get('audit_reader') != r['reader'] for r in records)
    now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    added = 0
    for path, r in zip(paths, records):
        assert not r.get('final_documentary_review'), 'Already finalized'
        if 'unresolved_for_main' in r:
            r['first_reader_questions_for_main'] = r.pop('unresolved_for_main')
        r['unresolved_for_main'] = []
        for n in r.get('notes', []):
            if n['id'] in NOTE_UPDATES:
                n['text'] = NOTE_UPDATES[n['id']]
        for d in r.get('remaining_doubts', []):
            if d.get('reason') in DOUBT_REASON_UPDATES:
                d['reason'] = DOUBT_REASON_UPDATES[d['reason']]
        if r['key'] == '143_scan022':
            r.setdefault('hand_log', []).append({
                'habit': 'Subscript j can have a long leftward basal return resembling an attachment guide.',
                'places': 'Raised (T_j) family, particularly the outer j before membership in J; compared with the final indexed T forms.',
                'scope': 'The different reader inspected these local forms and the existing family crop. The returning stroke belongs to the subscript; no separate guide is secured.',
                'misreadings': 'No witness correction is required at this locus. The long return must not be duplicated as an invented insertion guide.',
            })
        for e in r.get('check_events', []):
            old = e['statement_id']
            if old in ALIASES:
                e['original_statement_id'] = old
                e['statement_id'] = ALIASES[old]
        note_ids = {n['id'] for n in r.get('notes', [])}
        event_ids = {e['statement_id'] for e in r.get('check_events', [])}
        for n in r.get('notes', []):
            if n['id'] not in event_ids:
                r.setdefault('check_events', []).append({
                    'statement_id': n['id'],
                    'date': now[:10],
                    'who': WHO,
                    'type': 'carried as background without fault found',
                    'outcome': 'Final documentary review of this note and its recorded visual adjudication. Its source account or editorial observation is carried with the stated qualifications. This event performs no additional mathematical proof or computation; any earlier targeted check remains separately recorded.',
                })
                added += 1
        assert note_ids <= {e['statement_id'] for e in r['check_events']}
        r['final_documentary_review'] = {
            'time': now,
            'who': WHO,
            'status': 'Every first-reader question has received main adjudication, and a different-reader full-page audit is complete. Remaining source uncertainties are intentionally retained in remaining_doubts; no main-reader decision is pending.',
        }
        path.write_text(json.dumps(r, ensure_ascii=False, indent=2))
    with (ROOT/'progress.log').open('a') as f:
        f.write(f'final documentary status and note/check-event references reconciled {now}; {added} explicitly background-only note review events added; transcription fragments unchanged\n')
    print(json.dumps({'pages': len(records), 'note_background_events_added': added}))

if __name__ == '__main__':
    main()
