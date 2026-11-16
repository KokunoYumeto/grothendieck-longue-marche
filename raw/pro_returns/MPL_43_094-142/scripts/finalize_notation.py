from pathlib import Path
import difflib, json, sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from page_work import ROOT, PREFIX, utc, rebuild

changes = {
    100: [
        (r'\underline\unsure{\sigma|\gamma}', r'\underline{\unsure{\sigma|\gamma}}'),
        (r'\unsure{\unsure{\sigma|\gamma}}', r'\unsure{\sigma|\gamma}'),
    ],
    129: [
        ("si $Y$ est ``" + r'\unsure{en $y$}.',
         "si $Y$ est " + r"\unsure{''|``}" + r'\unsure{en $y$}.'),
    ],
}
record = ROOT/'records/final_notation_reconciliation.txt'
if record.exists():
    raise RuntimeError('Final reconciliation already recorded')
diffs = []
for scan, replacements in changes.items():
    path = ROOT/'pages'/f'{PREFIX}_43_scan{scan:03}.tex'
    before = path.read_text(encoding='utf-8')
    after = before
    for old, new in replacements:
        if old not in after:
            raise RuntimeError(f'Missing expected text on {scan}: {old!r}')
        after = after.replace(old,new)
    path.write_text(after,encoding='utf-8')
    diffs.append(''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile=f'scan{scan:03}-audited',tofile=f'scan{scan:03}-reconciled')))
record.write_text(
    'Final pre-context notation reconciliation by the sole visual reader.\n'
    'Completed '+utc()+'\n'
    'All 46 pages have first-reading and second-audit records. The text-only inventory located recurring forms; it did not decide any ink reading.\n'
    'Recompared whole scans094,096,100,102,109,114,120,140 and enlarged129 during reconciliation. Other recurring forms were checked during their logged second audits.\n'
    'N: matching flourished lower-left/upper-right strokes on096/097/140, represented consistently as mathcal N; scan140 changes are in its audit record.\n'
    'Coefficient: sigma is the common first reading on100/102/130/132/133/135/140. Gamma remains the local alternative on100/102; tau on the later sheets. Independent gamma at130 Hom0 and the unfinished114 margin have their own visible shapes and are not silently reassigned.\n'
    'Superscripts: examined the prime locations in the text inventory against the page readings, with further whole-image checks094,102,109,120,140. The uncertain vee/prime on109 and four dot/prime cases on140 remain marked. Subscript i! on135/140 and the !/* doubt on136 are retained. No raised exclamation stem with separate dot was resolved in the inventoried prime positions.\n'
    'Quotation marks: paired double marks use TeX backticks/apostrophes; the unclosed typed title on105 remains unclosed. The isolated repeat mark on129 is now itself doubtful, with closing/opening pair alternatives, since its slanted hooks do not decide the orientation. No missing quote was supplied.\n'
    'Math underlining: one, two and wavy strokes are retained as observed; double lines on133/136 were restored during those audits. Macro grouping on100 is repaired without changing its reading.\n'
    'Script/typed letters, zeros/circles, stars, hats, tildes, left/right torsion subscripts and arrowheads were compared during the second audits; unresolved alphabet pairs remain explicit (including124 and141).\n\n'
    +'\n'.join(diffs),encoding='utf-8')
overrides = {
    "method": "Manual confidence assessment by the sole reader after second visual audit; applies only to explicitly marked doubtful readings.",
    "scan_defaults": {"108":"low","129":"low","133":"low","135":"low"},
    "reason": "Dense cancellations and compressed cursive or crowded marginal material make even single proposed readings on these four sheets less secure. All alternative pairs and illegible groups remain low throughout the package."
}
(ROOT/'records/doubt_confidence_overrides.json').write_text(json.dumps(overrides,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
with (ROOT/'progress.log').open('a',encoding='utf-8') as f:
    f.write('notation reconciled '+utc()+'\n')
rebuild()
print('Final notation changes recorded; combined fragment and doubts rebuilt.')

