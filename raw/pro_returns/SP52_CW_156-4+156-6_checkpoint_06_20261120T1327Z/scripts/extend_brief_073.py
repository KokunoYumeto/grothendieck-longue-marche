"""Record scan073's workflow lessons after that page is saved and marked done."""
from pathlib import Path
import datetime

O = Path(__file__).resolve().parents[1]
assert any(x.startswith('scan 073 done ') and 'cote 156-4' in x
           for x in (O/'progress.log').read_text().splitlines())
p = O/'briefs/brief_v10.md'
assert not p.exists(), 'Do not overwrite an earlier brief version.'
old = (O/'briefs/brief_v09.md').read_text()
addition = '''## Clarifications from scan 073

- For a broad cancellation, trace the actual endpoints before assigning a last line to the cancelled block. A line below every endpoint may have uncertain cancellation scope even when all its letters are clear. Reproduce the strokes at their real lengths and state exactly what a whole-line doubt concerns.
- Check an accent at every occurrence, including a repeated word on the next line. A separate acute at one occurrence does not supply an accent at another; distinguish a following letter's high curve from a detached accent.
- A small mark may correspond to an H unreadable placeholder placed earlier or later in the sentence. Align it once by the local ink, then distinguish identity/state from displacement; do not invent an additional word to fill the misplaced placeholder.
- The collation field marked_in_h concerns an actual uncertainty or unreadable mark at that precise locus. A deletion macro or an ordinary editorial note alone is not a doubt mark; a larger quotation containing an unrelated ill does not make its entire scope doubtful.
- Keep the physical line positions needed by a continuous cancellation drawing, including a compound split across its two drawn lines. In ordinary prose the line-end joining rule still applies. Compare each display's placement separately from its letters and signs.
- Use only the current page's local C context. Ignore its references to earlier-page comparisons, and report any unrelated batch-level tail in a supplied packet without opening another page. The coordinator now stops page-audit extraction at every following second-level section.

'''
assert '## Final return' in old
p.write_text(old.replace('## Final return', addition+'## Final return'))
now = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (O/'brief_changes.md').open('a') as f:
    f.write('\n## v10 — first used on 156-4 scan 074\n\n'
            'After scan073, R1 assigned the final line confidently to the cancelled block while R2/R3 left its scope open; root confirmed that all three diagonal endpoints stop above it. R1 alone questioned the final repeated accent, and root read unaccented resulte. The readers aligned H’s displaced strengthening placeholder differently. The new version makes endpoint/state scope, local repeated accents, exact placeholder alignment and doubt-flag scope explicit. R2/R3 also differed in the physical b-line wrap; root’s missing-continuation crop supplied the actual sous-/figure boundary for the cancellation drawing. An unrelated C batch-audit tail was trimmed from the distributed packet; all three readers were told to disregard it and did so. Original returns and brief versions remain unchanged.\n\nRecorded '+now+'.\n')
print(p)
