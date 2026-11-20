#!/usr/bin/env python3
"""Complete documentation after the root reader's two image readings.

No page text is edited. Retained uncertainty arguments are copied exactly from
the page files to make the previously grouped deleted-text doubts explicit.
This is a documentation operation, not a new reading or proof check.
"""
import json
import re
from pathlib import Path
from record import ROOT, RECORDS, build, utc


def escaped(text, position):
    backslashes = 0
    position -= 1
    while position >= 0 and text[position] == '\\':
        backslashes += 1
        position -= 1
    return backslashes % 2 == 1


def arguments(text, macro):
    for match in re.finditer(r'\\' + macro + r'\s*\{', text):
        start = match.end()
        depth = 1
        end = start
        while depth:
            if end >= len(text):
                raise ValueError('Unbalanced macro while documenting doubts')
            if not escaped(text, end):
                if text[end] == '{':
                    depth += 1
                elif text[end] == '}':
                    depth -= 1
            end += 1
        yield match.start(), end, text[start:end-1]


# Positions reviewed by the root reader; all are inside retained deleted text.
# Lines refer to the final per-page TeX fragments, before the freeze.
TARGETS = {
    18: {3: 'opening definition', 5: 'NB after the graded module',
         15: 'cancelled brace in the nonvanishing chain',
         16: 'cancelled chain continuation'},
    20: {27: 'cancelled isolated symbol', 76: 'cancelled coefficient ring'},
    22: {27: 'cancelled symbol before the example'},
    29: {7: 'cancelled opening consequence', 17: 'cancelled tensor product',
         18: 'cancelled final symbol'},
    33: {28: 'cancelled range in (4′)', 29: 'cancelled range in (4′)',
         36: 'cancelled identity (4′′)', 49: 'cancelled identity after (5′)',
         58: 'cancelled formula reference', 61: 'cancelled first line of (7)',
         62: 'cancelled continuation of (7)', 64: 'cancelled definition of T'},
    34: {14: 'cancelled quantifier'},
    36: {12: 'cancelled summation and exponent', 14: 'cancelled isomorphism phrase',
         19: 'cancelled projector range'},
    38: {11: 'cancelled lower bound', 27: 'cancelled commuting formula'},
    42: {17: 'cancelled xi expression', 28: 'cancelled draft, left formula',
         30: 'cancelled draft, lower right formula'},
    43: {3: 'cancelled first map label', 6: 'cancelled differential map',
         7: 'cancelled lower map label or injectivity phrase'},
    48: {17: 'cancelled sign factor'},
    51: {24: 'cancelled symbol before projections'},
}

# Other doubts share these long TeX lines and already have explicit entries.
ALREADY_EXPLICIT = {
    18: {'En dehors', 'transposé'},
    29: {'de'},
    43: {'son', 'donc', 'et|qui', 'un', 'immersion ouverte|immersion fermée'},
}


def main():
    log = (ROOT/'progress.log').read_text()
    if re.search(r'^transcription frozen\b', log, re.M):
        raise ValueError('Documentation finalization must precede freezing')
    if len(re.findall(r'^scan \d+ audited ', log, re.M)) != 25:
        raise ValueError('All 25 image audits must already be recorded')
    explicit = 0
    for path in sorted(RECORDS.glob('*.json')):
        data = json.loads(path.read_text())
        scan = data['scan']
        data['doubts'] = [row for row in data['doubts']
                          if not ('— fragment line' in row[0] and 'retained doubt' in row[0])]
        for event in data.get('checks', []):
            event[2] = 'GPT-6 Astra Pro; effort not exposed; current run SP65_C13_16'
        if scan in TARGETS:
            text = (ROOT/'pages'/f'16_scan{scan:03}.tex').read_text()
            deleted = [(a,b) for a,b,_ in arguments(text, 'deleted')]
            occurrences = {}
            for start,end,argument in arguments(text, 'unsure'):
                line = text.count('\n', 0, start) + 1
                if line not in TARGETS[scan]:
                    continue
                if argument in ALREADY_EXPLICIT.get(scan, set()):
                    continue
                if not any(a < start and end <= b for a,b in deleted):
                    continue
                occurrences[line] = occurrences.get(line, 0) + 1
                place = (f"{TARGETS[scan][line]} — fragment line {line}, "
                         f"retained doubt {occurrences[line]}")
                if not any(row[0] == place for row in data['doubts']):
                    data['doubts'].append([
                        place, argument,
                        'Retained under cancellation. The crossed or overwritten strokes leave this reading unresolved; this entry gives the exact text of the existing in-place doubt.',
                        'low',
                    ])
                explicit += 1
        if scan == 17:
            data['feedback'] = [
                'No additional recurring error class was established beyond the ten categories above. The following refinements record repeated difficulties within those categories; they are not additional counted loci.',
                '- Typewriter letterforms and alphabets need separate attention from mathematical role: the crossed χ parameter on 044–050, the two handwritten ℓ subscripts on 045, the plain 1 on 048, roman product x on 033 and 044–050, and underlined Q/Z on 044/049. Repeated roles alone did not settle the glyph.',
                '- Typewriter overcorrections can retain readable parts of both states in one position. Examples are will and birationally on 047, an→the on 048, in→it and an→of on 049, and the cancelled early target on 050. The uncertain direction or extent of a correction remains marked.',
                '- Clipped right edges and unfilled slots need explicit preservation: the blank degree below L³ on 022, the blank polarization slot on 044, and the clipped groups on 045–046. Neither the continuation of the sentence nor the formula supplies absent ink.',
                '- Small nonverbal marks survive beside text: the crossed-formula connectors on 022/029, the open associativity frame on 025, the pencil operator question on 040, the N.B. leader on 046, and the degree/vice-versa strokes on 051. Their position and stroke structure belong to the record.',
                '- Pale reversed type and a printed paper pattern can interfere with foreground reading: 018/020/034 and the Gevaert sheet 042. The page inventory records the observed sheet structure and visible background without importing a proposed underlying passage.',
            ]
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n')
    if explicit != 36:
        raise ValueError(f'Expected 36 explicitly located retained doubts, found {explicit}')
    # A raw-string prefix removes a Python warning while preserving the exact
    # string value recorded by the original first-reading script.
    script = ROOT/'scripts/read_044.py'
    old = "kind='readable ink left as `\\ill{}`'"
    new = "kind=r'readable ink left as `\\ill{}`'"
    content = script.read_text()
    if old in content:
        script.write_text(content.replace(old, new))
    build()
    stamp = utc()
    (ROOT/'reading_state.txt').write_text(
        'All 25 first readings and all 25 second image readings are complete, once each in the prescribed order.\n'
        'All 211 live witness-C marks have decisions. Recurring notation has been compared across the completed sequence.\n'
        'The final assessment and error-sheet feedback are complete. Thirty-six retained doubts in deleted text now have explicit occurrence entries in addition to the earlier grouped entries; page readings are unchanged by this documentation step.\n'
        'Next steps: pre-freeze structural validation, SHA-256 freeze of the 25 pages and combined fragment, unchanged-hash verification, final ZIP packaging and archive validation.\n'
        'Documentation completed '+stamp+'\n'
    )
    with (ROOT/'progress.log').open('a') as handle:
        handle.write('recurring notation compared across all pages '+stamp+'; no further reading change\n')
        handle.write('final assessment and feedback completed '+stamp+'\n')
        handle.write('doubt coverage expanded '+stamp+'; 36 retained deleted-text occurrences explicitly indexed; page readings unchanged\n')
        handle.write('check-event identity fields completed '+stamp+'; 25 events, no new mathematical check claimed\n')
    print('Completed documentation; explicitly indexed 36 retained deleted-text doubts. No page file edited.')


if __name__ == '__main__':
    main()
