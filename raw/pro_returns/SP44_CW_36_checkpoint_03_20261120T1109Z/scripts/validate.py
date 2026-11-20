"""Structural checks only; no claim that balanced LaTeX proves faithful reading."""
from pathlib import Path
from collections import Counter
import re,json,csv,hashlib,argparse

OUT=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('--complete',action='store_true');a=p.parse_args()
problems=[]; reports=[]
sheet_kinds={'text','reused_typed','typescript','letter','list','cancelled_draft','cover'}
element_kinds={'text','display','diagram','drawing','margin note','insertion','deletion'}
collation_kinds={'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised',r'readable ink left as \ill{}','drawing or diagram','other'}
decisions=[json.loads(p.read_text()) for p in sorted((OUT/'decisions').glob('scan[0-9][0-9][0-9].json'))]
scans=[d['scan'] for d in decisions]
if a.complete and scans!=list(range(10,28)): problems.append('Expected decided scans 10–27 in order')
for d in decisions:
    n=d['scan'];f=OUT/'pages'/d['filename'];s=f.read_text()
    # Strip comments without erasing escaped percent signs.
    clean=re.sub(r'(?<!\\)%[^\n]*','',s)
    brace=0
    for m in re.finditer(r'(?<!\\)[{}]',clean):
        brace += 1 if m.group()=='{' else -1
        if brace<0: problems.append(f'{f.name}: closing brace before opening at {m.start()}')
    if brace: problems.append(f'{f.name}: brace balance {brace}')
    math=[]
    for m in re.finditer(r'\\\[|\\\]|\\\(|\\\)|(?<!\\)\$',clean):
        x=m.group()
        if x in ('\\[','\\('):
            if math: problems.append(f'{f.name}: nested math at {m.start()}')
            math.append(x)
        elif x in ('\\]','\\)'):
            want='\\[' if x=='\\]' else '\\('
            if not math or math.pop()!=want: problems.append(f'{f.name}: unmatched math closer {x}')
        elif math and math[-1]=='$': math.pop()
        elif math: problems.append(f'{f.name}: dollar in explicit math at {m.start()}')
        else: math.append('$')
    if math: problems.append(f'{f.name}: math left open {math}')
    env=[]
    for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',clean):
        op,name=m.groups()
        if op=='begin':env.append(name)
        elif not env or env.pop()!=name:problems.append(f'{f.name}: environment mismatch {name}')
    if env:problems.append(f'{f.name}: environments left open {env}')
    if re.findall(r'\\scanpage\{(\d+)\}',s)!=[str(n)]:problems.append(f'{f.name}: scanpage mismatch')
    if ('\\cotefile{36}' in s)!=(n==10):problems.append(f'{f.name}: cotefile location')
    leaked=re.findall(r'\\(?:ill|uncertain|struck|add|note|page|folder|batch|documentclass|newcommand)\b',clean)
    if leaked:problems.append(f'{f.name}: foreign/forbidden macros {leaked}')
    if any(r['transcribed']!='yes' for r in d['inventory']): problems.append(f'{f.name}: incomplete inventory')
    for r in d['inventory']:
        if r['sheet_kind'] not in sheet_kinds: problems.append(f'{f.name}: invalid sheet_kind {r["sheet_kind"]}')
        if r['kind'] not in element_kinds: problems.append(f'{f.name}: invalid inventory kind {r["kind"]}')
    for r in d['rows']:
        if r.get('against_H') and r['kind'] not in collation_kinds:problems.append(f'{f.name}: invalid H collation kind {r["kind"]}')
        if r['confidence'] not in {'high','medium','low'}:problems.append(f'{f.name}: invalid confidence')
        if len(r.get('readers',[]))!=3:problems.append(f'{f.name}: decision lacks three readings: {r["place"]}')
    for r in ('R1','R2','R3'):
        base=OUT/'readers'/f'scan{n:03d}'/r
        for name in ('reading.tex','report.md','result.json'):
            if not (base/name).exists():problems.append(f'{f.name}: missing {r}/{name}')
    counts={k:len(re.findall(r'\\'+k+r'\{',clean)) for k in ('unsure','illegible','deleted','inserted','margin','diagram','figure')}
    reports.append({'scan':n,'file':f.name,'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'marks':counts})
combined=OUT/'SP44_CW_36_transcription.tex'
expected='\n'.join((OUT/'pages'/d['filename']).read_text().rstrip() for d in decisions)+'\n' if decisions else ''
if combined.read_text()!=expected:problems.append('Combined transcription differs from ordered page concatenation')
if a.complete:
    notation_manifest=OUT/'validation/notation_final.json'
    if not notation_manifest.exists():problems.append('Final cross-page notation review is missing')
    else:
        notation_review=json.loads(notation_manifest.read_text())
        if notation_review.get('reviewed_scans')!=list(range(10,28)):problems.append('Final notation review does not cover all 18 scans')
        if not notation_review.get('entries') or not notation_review.get('review_summary'):problems.append('Final notation review lacks conventions or review summary')
    expected_s={x['where'] for x in json.loads((OUT/'validation/S_scope.json').read_text())}
    reviewed_s={x['where'] for d in decisions for x in d.get('sweep',[])}
    if expected_s-reviewed_s:problems.append('Unreviewed sweep rows: '+repr(sorted(expected_s-reviewed_s)))
    if reviewed_s-expected_s:problems.append('Unrecognized sweep row identifiers: '+repr(sorted(reviewed_s-expected_s)))
    # A joint sweep identifier does not prove that both separate page loci were reviewed.
    required_pairs={
        (12,'36/12 (n°2 a), NB) [A36-01]'),
        (14,'36/14, 36/16 [A36-01]'),
        (15,'36/15 (n°4) [A36-01]'),
        (16,'36/14, 36/16 [A36-01]'),
        (17,'36/17 [A36-01]'),
        (24,'36/24 (Lemma 7.6 proof) [A36-02]'),
    }
    reviewed_pairs={(d['scan'],r['where']) for d in decisions for r in d.get('sweep',[])}
    if required_pairs-reviewed_pairs:problems.append('Missing page-specific sweep reviews: '+repr(sorted(required_pairs-reviewed_pairs)))
    long_where='36/18-26 (Théorème 7.1, Cor. 7.2, Rem. 7.7 a)) [A36-01/02]'
    locus_manifest=OUT/'validation/S_required_loci.json'
    if not locus_manifest.exists():problems.append('Missing long-range sweep applicability/locus manifest')
    else:
        manifest=json.loads(locus_manifest.read_text())
        reviewed_pages={x['scan'] for x in manifest.get('range_pages_reviewed',[])}
        if reviewed_pages!=set(range(18,27)):problems.append('Sweep range applicability review is incomplete')
        if any(not x.get('reason') for x in manifest.get('range_pages_reviewed',[])):problems.append('Sweep applicability record lacks a reason')
        required_loci={(r['scan'],r['where'],r['locus_id']) for r in manifest.get('loci',[])}
        actual_loci={(d['scan'],r['where'],r.get('locus_id','')) for d in decisions for r in d.get('sweep',[]) if r['where']==long_where}
        if not required_loci:problems.append('Long-range sweep locus manifest is empty')
        if required_loci-actual_loci:problems.append('Missing sweep statement/margin reviews: '+repr(sorted(required_loci-actual_loci)))
        if actual_loci-required_loci:problems.append('Unrecognized sweep statement/margin reviews: '+repr(sorted(actual_loci-required_loci)))
summary={'scope':'structural balance and package consistency only; no TeX compilation','complete_required':a.complete,'scans':scans,'pages':reports,'totals':dict(sum((Counter(r['marks']) for r in reports),Counter())),'problems':problems,'pass':not problems}
(OUT/'validation/syntax_and_package.json').write_text(json.dumps(summary,indent=2))
print(json.dumps(summary,indent=2))
raise SystemExit(bool(problems))
